
import os
import sys
import json
import re
import argparse
import google.generativeai as genai
from typing import List, Dict, Any

# Configure Gemini API
MODELS = ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-1.0-pro"]
MODEL = None

KEYWORD_MAPPING = {
    'Threat Intelligence': ['threat intelligence', 'threat landscape', 'threat report', 'apt', 'advanced persistent threat', 'malware', 'phishing', 'cybercrime'],
    'Application Security': ['application security', 'appsec', 'devsecops', 'owasp', 'sast', 'dast', 'software security', 'vulnerability'],
    'Cloud Security': ['cloud security', 'aws', 'azure', 'gcp', 'container security', 'kubernetes', 'serverless'],
    'Vulnerabilities': ['vulnerability', 'cve', 'vulnerability management', 'patching', 'zero-day'],
    'Ransomware': ['ransomware', 'extortion', 'data breach'],
    'Data Breaches': ['data breach', 'data leak', 'incident report'],
    'Physical Security': ['physical security', 'ot security', 'operational technology', 'ics', 'industrial control systems'],
    'AI and Emerging Technologies': ['artificial intelligence', 'ai', 'machine learning', 'ml', 'emerging technology'],
    'Industry Trends': ['industry trends', 'cybersecurity trends', 'security report', 'annual report'],
    'Identity Security': ['identity', 'iam', 'identity and access management', 'authentication', 'mfa', 'zero trust'],
    'Penetration Testing': ['penetration testing', 'pentesting', 'red team', 'offensive security'],
    'Privacy and Data Protection': ['privacy', 'data protection', 'gdpr', 'ccpa', 'data privacy'],
}

def setup_gemini(api_key: str):
    global MODEL
    genai.configure(api_key=api_key)
    for model_name in MODELS:
        try:
            test_model = genai.GenerativeModel(model_name)
            test_response = test_model.generate_content("Hello")
            MODEL = model_name
            print(f"Successfully verified model: {MODEL}")
            break
        except Exception as e:
            print(f"Model {model_name} not available or failed verification: {str(e)}")
            continue

def analyze_content(content: str, org_name: str, year: str, report_title: str) -> Dict[str, Any]:
    if not MODEL:
        return fallback_analysis(content, org_name, year, report_title)

    try:
        # Summarization
        summary_prompt = f"Summarize the key findings of this security report titled '{report_title}' from {org_name} ({year}). The summary should be concise and no more than 3 sentences. Report content: {content[:4000]}"
        summary_response = genai.GenerativeModel(MODEL).generate_content(summary_prompt)
        summary = summary_response.text.strip()

        # Report Type Classification
        type_prompt = f"Is this an 'Analysis' report (technical analysis, sensor data) or a 'Survey' report (interviews, sentiment)? Respond with only 'Analysis' or 'Survey'. Content: {content[:2000]}"
        type_response = genai.GenerativeModel(MODEL).generate_content(type_prompt)
        report_type = "Analysis" if "analysis" in type_response.text.lower() else "Survey"

        # Categorization
        category = categorize_content(content)

        return {
            'organization': org_name,
            'year': year,
            'title': report_title,
            'summary': summary,
            'type': report_type,
            'category': category,
            'ai_processed': True
        }
    except Exception as e:
        print(f"AI analysis failed: {e}")
        return fallback_analysis(content, org_name, year, report_title)

def categorize_content(content: str) -> str:
    content_lower = content.lower()
    scores = {category: sum(content_lower.count(keyword) for keyword in keywords) for category, keywords in KEYWORD_MAPPING.items()}
    return max(scores, key=scores.get) if any(scores.values()) else "Industry Trends"

def fallback_analysis(content: str, org_name: str, year: str, report_title: str) -> Dict[str, Any]:
    summary = ' '.join(content.split()[:60]) + '...'
    category = categorize_content(content)
    return {
        'organization': org_name,
        'year': year,
        'title': report_title,
        'summary': summary,
        'type': "Analysis",
        'category': category,
        'ai_processed': False
    }

def main():
    parser = argparse.ArgumentParser(description="Analyze markdown content of security reports.")
    parser.add_argument("conversions_json", help="Path to the JSON file with conversion results.")
    parser.add_argument("--output-json", help="Path to save the analysis results as a JSON file.", default="analysis.json")
    args = parser.parse_args()

    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        print("Warning: GEMINI_API_KEY not set. Using fallback analysis.")
    else:
        setup_gemini(gemini_api_key)

    with open(args.conversions_json, 'r') as f:
        conversions = json.load(f)

    analysis_results = []
    for conv in conversions:
        if conv['status'] == 'success':
            with open(conv['output_path'], 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract info from path
            path_parts = conv['output_path'].split('/')
            year = [part for part in path_parts if part.isdigit() and len(part) == 4][0]
            filename = os.path.basename(conv['output_path'])
            org_name = filename.split(' - ')[0]
            report_title = ' - '.join(filename.split(' - ')[1:]).replace('.md', '')

            analysis = analyze_content(content, org_name, year, report_title)
            analysis['file_path'] = conv['output_path']
            analysis_results.append(analysis)

    with open(args.output_json, 'w') as f:
        json.dump(analysis_results, f, indent=2)

    # Summary
    summary_path = os.environ.get('GITHUB_STEP_SUMMARY', 'summary.md')
    with open(summary_path, 'a') as f:
        f.write("\n## 🤖 AI-Powered Report Analysis Summary\n\n")
        if analysis_results:
            f.write("| File | Category | Type | AI Processed |\n")
            f.write("|------|----------|------|--------------|\n")
            for res in analysis_results:
                ai_icon = "✅" if res['ai_processed'] else "⚠️"
                f.write(f"| {os.path.basename(res['file_path'])} | {res['category']} | {res['type']} | {ai_icon} |\n")
        else:
            f.write("No reports were analyzed.\n")

if __name__ == "__main__":
    main()
