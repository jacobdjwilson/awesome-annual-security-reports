import os
import sys
import json
import re
import argparse
import google.generativeai as genai
from typing import List, Dict, Any, Tuple
from pathlib import Path

# Configure Gemini API
MODELS = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash"]
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
    
    # Extract year from path
    year = "Unknown"
    for part in path.parts:
        if part.isdigit() and len(part) == 4:
            year = part
            break
    
    # Parse filename to extract organization and title
    filename = path.stem
    
    # Remove year suffixes and common separators
    filename_clean = re.sub(r'[-_\s]*20\d{2}[-_\s]*', '', filename)
    
    # Split on common separators
    parts = re.split(r'[-_]+', filename_clean, 1)
    
    if len(parts) >= 2:
        org_part = parts[0].strip()
        title_part = parts[1].strip()
        
        # Clean up organization name
        org_name = re.sub(r'[_-]', ' ', org_part)
        org_name = ' '.join(word.capitalize() for word in org_name.split())
        
        # Clean up title
        title = re.sub(r'[_-]', ' ', title_part)
        title = ' '.join(word.capitalize() for word in title.split())
        
        # Handle special cases for well-known organizations
        org_mapping = {
            'Cyberark': 'CyberArk',
            'Sailpoint': 'SailPoint',
            'Crowdstrike': 'CrowdStrike',
            'Palo Alto': 'Palo Alto Networks',
        }
        
        for old_name, new_name in org_mapping.items():
            if org_name.lower() == old_name.lower():
                org_name = new_name
                break
    else:
        # Fallback if parsing fails
        org_name = ' '.join(word.capitalize() for word in filename_clean.replace('_', ' ').replace('-', ' ').split())
        title = f"Security Report {year}"
    
    return org_name, year, title

def analyze_content(content: str, org_name: str, year: str, report_title: str, categories: List[str]) -> Dict[str, Any]:
    if not MODEL:
        return fallback_analysis(content, org_name, year, report_title)

    try:
        # Summarization
        with open(".github/ai-prompts/markdown-summarization-prompt.md", 'r', encoding='utf-8') as f:
            summary_base_prompt = f.read()
        summary_prompt = f"{summary_base_prompt}\n\nOrganization: {org_name}\nReport Title: {report_title}\nYear: {year}\n\nReport Content:\n{content[:15000]}"
        
        summary_model = genai.GenerativeModel(MODEL)
        summary_response = summary_model.generate_content(summary_prompt)
        summary = ' '.join(summary_response.text.strip().split())
        
        # Ensure summary is not too long (limit to ~400 chars for README formatting)
        if len(summary) > 400:
            sentences = summary.split('. ')
            summary = ''
            for sentence in sentences:
                if len(summary + sentence + '. ') <= 400:
                    summary += sentence + '. '
                else:
                    break
            summary = summary.strip()

        # Classification and Categorization
        with open(".github/ai-prompts/report-categorization-prompt.md", 'r', encoding='utf-8') as f:
            categorization_base_prompt = f.read()
        
        category_str = '\n'.join([f"- {cat}" for cat in categories])
        categorization_prompt = categorization_base_prompt.replace("{{CATEGORIES}}", category_str)
        categorization_prompt += f"\n\nOrganization: {org_name}\nTitle: {report_title}\nYear: {year}\n\n{content[:8000]}"

        category_model = genai.GenerativeModel(MODEL)
        category_response = category_model.generate_content(categorization_prompt)
        
        try:
            response_text = category_response.text.strip().replace('```json', '').replace('```', '')
            classification = json.loads(response_text)
            if 'type' not in classification or 'category' not in classification:
                raise ValueError("Missing 'type' or 'category' in AI response.")
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Could not parse AI response for classification: {e}. Falling back to keyword matching.")
            classification = {
                'type': 'Analysis',  # Default type
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
    # Create a more meaningful summary from the content
    sentences = content.split('. ')
    # Take first few meaningful sentences (skip headers and empty content)
    meaningful_sentences = [s.strip() for s in sentences if len(s.strip()) > 20 and not s.strip().startswith('#')]
    summary_sentences = meaningful_sentences[:3] if meaningful_sentences else [f"Security report from {org_name}"]
    summary = '. '.join(summary_sentences)
    if not summary.endswith('.'):
        summary += '.'
    
    # Limit summary length
    if len(summary) > 400:
        summary = summary[:400].rsplit('. ', 1)[0] + '.'
    
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
            try:
                with open(conv['output_path'], 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract info using the correct path
                org_name, year, report_title = extract_info_from_path(conv['pdf_path'])
                
                print(f"Analyzing: {org_name} - {report_title} ({year})")

                analysis = analyze_content(content, org_name, year, report_title, categories)
                analysis['file_path'] = conv['output_path']
                analysis['pdf_path'] = conv['pdf_path']
                
                # Include organization URL from conversion if available
                if 'organization_url' in conv and conv['organization_url']:
                    analysis['organization_url'] = conv['organization_url']
                else:
                    # Generate a default organization URL based on the organization name
                    analysis['organization_url'] = generate_default_org_url(org_name)
                
                analysis_results.append(analysis)
                
            except Exception as e:
                print(f"Error analyzing {conv['output_path']}: {e}")
                continue

    with open(args.output_json, 'w') as f:
        json.dump(analysis_results, f, indent=2)

    print(f"Analysis completed. {len(analysis_results)} reports analyzed.")

    return 0

def generate_default_org_url(org_name: str) -> str:
    """Generate a default organization URL based on the organization name"""
    org_name_lower = org_name.lower()
    
    # Special cases for well-known organizations
    special_cases = {
        'cyberark': 'https://www.cyberark.com/threat-landscape/',
        'sailpoint': 'https://www.sailpoint.com/horizons',
        'okta': 'https://www.okta.com',
        'crowdstrike': 'https://www.crowdstrike.com',
        'palo alto networks': 'https://www.paloaltonetworks.com',
        'microsoft': 'https://www.microsoft.com',
        'google': 'https://www.google.com',
        'amazon': 'https://aws.amazon.com',
        'ibm': 'https://www.ibm.com'
    }
    
    for key, url in special_cases.items():
        if key in org_name_lower:
            return url
    
    # Default URL generation
    domain_base = re.sub(r'\b(company|corp|corporation|inc|llc|ltd|group|security|cyber|tech|technologies)\b', '', org_name.lower())
    domain_base = re.sub(r'[^a-z0-9]', '', domain_base)
    if len(domain_base) < 3:
        domain_base = re.sub(r'[^a-z0-9]', '', org_name.lower())
    
    return f"https://www.{domain_base}.com"

if __name__ == "__main__":
    main()