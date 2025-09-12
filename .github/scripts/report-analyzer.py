import os
import sys
import json
import re
import argparse
import google.generativeai as genai
from typing import List, Dict, Any, Tuple
from pathlib import Path

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

def parse_toc_from_readme(readme_path: str) -> List[str]:
    try:
        content = Path(readme_path).read_text(encoding='utf-8')
        toc_pattern = r'## Contents\n<!-- TOC -->\n(.*?)\n<!-- /TOC -->'
        toc_match = re.search(toc_pattern, content, re.DOTALL)
        if not toc_match:
            return []
        
        toc_content = toc_match.group(1)
        categories = set()
        for line in toc_content.split('\n'):
            if line.strip().startswith('    - '):
                match = re.search(r'\[([^\]]+)\]', line)
                if match:
                    categories.add(match.group(1))
        return sorted(list(categories))
    except FileNotFoundError:
        return []

def extract_info_from_path(file_path: str) -> Tuple[str, str, str]:
    path = Path(file_path)
    year = "Unknown"
    for part in path.parts:
        if part.isdigit() and len(part) == 4:
            year = part
            break
    
    filename_clean = re.sub(r'(_|-)?20\d{2}.*', '', path.stem)
    parts = re.split(r'[-_\s]+', filename_clean)
    
    if len(parts) >= 2:
        org_name = parts[0]
        report_title = ' '.join(parts[1:])
    else:
        org_name = filename_clean
        report_title = f"Security Report {year}"

    org_name = ' '.join(word.capitalize() for word in org_name.replace('_', ' ').replace('-', ' ').split())
    report_title = ' '.join(word.capitalize() for word in report_title.replace('_', ' ').replace('-', ' ').split())
    
    return org_name, year, report_title

def analyze_content(content: str, org_name: str, year: str, report_title: str, categories: List[str]) -> Dict[str, Any]:
    if not MODEL:
        return fallback_analysis(content, org_name, year, report_title)

    try:
        # Summarization
        with open(".github/ai-prompts/markdown-summarization-prompt.md", 'r', encoding='utf-8') as f:
            summary_base_prompt = f.read()
        summary_prompt = f"{summary_base_prompt}\n\nOrganization: {org_name}\nReport Title: {report_title}\nYear: {year}\n\nReport Content:\n{content[:15000]}"
        summary_response = genai.GenerativeModel(MODEL).generate_content(summary_prompt)
        summary = ' '.join(summary_response.text.strip().split())
        if len(summary) > 400:
            sentences = summary.split('. ')
            summary = ''.join(s + '. ' for s in sentences if len(summary) <= 400)

        # Classification and Categorization
        with open(".github/ai-prompts/report-categorization-prompt.md", 'r', encoding='utf-8') as f:
            categorization_base_prompt = f.read()
        
        category_str = '\n'.join([f"- {cat}" for cat in categories])
        categorization_prompt = categorization_base_prompt.replace("{{CATEGORIES}}", category_str)
        categorization_prompt += f"\n\n{content[:8000]}"

        category_response = genai.GenerativeModel(MODEL).generate_content(categorization_prompt)
        
        try:
            response_text = category_response.text.strip().replace('```json', '').replace('```', '')
            classification = json.loads(response_text)
            if 'type' not in classification or 'category' not in classification:
                raise ValueError("Missing 'type' or 'category' in AI response.")
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Could not parse AI response for classification: {e}. Falling back to keyword matching.")
            classification = {
                'type': 'Analysis', # Default type
                'category': categorize_content_fallback(content)
            }

        return {
            'organization': org_name,
            'year': year,
            'title': report_title,
            'summary': summary,
            'type': classification.get('type', 'Analysis'),
            'category': classification.get('category', 'Industry Trends'),
            'ai_processed': True
        }
    except Exception as e:
        print(f"AI analysis failed: {e}")
        return fallback_analysis(content, org_name, year, report_title)

def categorize_content_fallback(content: str) -> str:
    content_lower = content.lower()
    scores = {category: sum(content_lower.count(keyword) for keyword in keywords) for category, keywords in KEYWORD_MAPPING.items()}
    return max(scores, key=scores.get) if any(scores.values()) else "Industry Trends"

def fallback_analysis(content: str, org_name: str, year: str, report_title: str) -> Dict[str, Any]:
    summary = '. '.join(content.split('. ')[:3]) + '.'
    category = categorize_content_fallback(content)
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
    parser.add_argument("--readme-path", help="Path to the README.md file.", default="README.md")
    parser.add_argument("--output-json", help="Path to save the analysis results as a JSON file.", default="analysis.json")
    args = parser.parse_args()

    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        print("Warning: GEMINI_API_KEY not set. Using fallback analysis.")
    else:
        setup_gemini(gemini_api_key)

    categories = parse_toc_from_readme(args.readme_path)
    if not categories:
        print("Error: Could not parse categories from README.md. Using keyword mapping as fallback.")
        categories = list(KEYWORD_MAPPING.keys())

    with open(args.conversions_json, 'r') as f:
        conversions = json.load(f)

    analysis_results = []
    for conv in conversions:
        if conv['status'] == 'success':
            with open(conv['output_path'], 'r', encoding='utf-8') as f:
                content = f.read()
            
            org_name, year, report_title = extract_info_from_path(conv['output_path'])

            analysis = analyze_content(content, org_name, year, report_title, categories)
            analysis['file_path'] = conv['output_path']
            analysis_results.append(analysis)

    with open(args.output_json, 'w') as f:
        json.dump(analysis_results, f, indent=2)

    summary_path = os.environ.get('GITHUB_STEP_SUMMARY', 'summary.md')
    with open(summary_path, 'w') as f:
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
