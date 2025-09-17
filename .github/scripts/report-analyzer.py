import os
import sys
import json
import re
import argparse
import google.generativeai as genai
from typing import List, Dict, Any, Tuple
from pathlib import Path

# Configure Gemini API
MODELS = ["gemini-2.0-flash-exp", "gemini-2.0-flash", "gemini-1.5-flash", "gemini-1.5-pro"]
MODEL = None

def setup_gemini(api_key: str):
    global MODEL
    genai.configure(api_key=api_key)
    for model_name in MODELS:
        try:
            test_model = genai.GenerativeModel(model_name)
            test_response = test_model.generate_content("Hello", generation_config={"max_output_tokens": 10})
            if test_response and test_response.text:
                MODEL = model_name
                print(f"Successfully verified model: {MODEL}")
                break
        except Exception as e:
            print(f"Model {model_name} not available or failed verification: {str(e)}")
            continue
    
    if not MODEL:
        print("Warning: No AI models available. Will use fallback analysis.")
        return False
    return True

def parse_toc_from_readme(readme_path: str) -> Dict[str, List[str]]:
    """Parse TOC from README.md and return categorized sections"""
    try:
        content = Path(readme_path).read_text(encoding='utf-8')
        toc_pattern = r'## Contents\n<!-- TOC -->\n(.*?)\n<!-- /TOC -->'
        toc_match = re.search(toc_pattern, content, re.DOTALL)
        
        if not toc_match:
            print("Warning: Could not find TOC section in README.md")
            return {"Analysis": ["Industry Trends"], "Survey": ["Industry Trends"]}
        
        toc_content = toc_match.group(1)
        structure = {"Analysis": [], "Survey": []}
        current_type = None
        
        for line in toc_content.split('\n'):
            line = line.strip()
            if not line:
                continue
                
            # Main section detection
            if line.startswith('- ') and not line.startswith('    - '):
                match = re.search(r'\[([^\]]+)\]', line)
                if match:
                    section_name = match.group(1)
                    if 'Analysis Reports' in section_name:
                        current_type = "Analysis"
                    elif 'Survey Reports' in section_name:
                        current_type = "Survey"
                    else:
                        current_type = None
            
            # Subsection detection
            elif line.startswith('    - ') and current_type:
                match = re.search(r'\[([^\]]+)\]', line)
                if match:
                    subsection_name = match.group(1)
                    if subsection_name not in structure[current_type]:
                        structure[current_type].append(subsection_name)
        
        print(f"Parsed categories from README:")
        print(f"  Analysis: {structure['Analysis']}")
        print(f"  Survey: {structure['Survey']}")
        
        # Ensure we have at least some default categories
        if not structure["Analysis"]:
            structure["Analysis"] = ["Threat Intelligence", "Application Security", "Cloud Security", "Vulnerabilities", "Industry Trends"]
        if not structure["Survey"]:
            structure["Survey"] = ["Industry Trends", "Identity Security", "Application Security", "Cloud Security"]
            
        return structure
        
    except FileNotFoundError:
        print("Warning: README.md not found, using default categories")
        return {
            "Analysis": ["Threat Intelligence", "Application Security", "Cloud Security", "Vulnerabilities", "Industry Trends"],
            "Survey": ["Industry Trends", "Identity Security", "Application Security", "Cloud Security"]
        }
    except Exception as e:
        print(f"Warning: Error parsing README.md: {e}, using default categories")
        return {
            "Analysis": ["Threat Intelligence", "Application Security", "Cloud Security", "Vulnerabilities", "Industry Trends"],
            "Survey": ["Industry Trends", "Identity Security", "Application Security", "Cloud Security"]
        }

def extract_info_from_path(file_path: str) -> Tuple[str, str, str]:
    """Extract organization, year, and title from file path"""
    path = Path(file_path)
    
    # Extract year from path
    year = "Unknown"
    for part in path.parts:
        if part.isdigit() and len(part) == 4 and part.startswith("20"):
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
            'Proofpoint': 'Proofpoint',
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

def categorize_content_fallback(content: str, available_categories: Dict[str, List[str]], org_name: str = "", title: str = "") -> Tuple[str, str]:
    """Fallback categorization based on keyword matching"""
    # Extended keyword mapping
    keyword_mapping = {
        'Threat Intelligence': ['threat intelligence', 'threat landscape', 'threat report', 'apt', 'advanced persistent threat', 'malware', 'phishing', 'cybercrime', 'attack', 'attacker'],
        'Application Security': ['application security', 'appsec', 'devsecops', 'owasp', 'sast', 'dast', 'software security', 'code security'],
        'Cloud Security': ['cloud security', 'aws', 'azure', 'gcp', 'container security', 'kubernetes', 'serverless', 'cloud infrastructure'],
        'Vulnerabilities': ['vulnerability', 'cve', 'vulnerability management', 'patching', 'zero-day', 'exploit'],
        'Ransomware': ['ransomware', 'extortion', 'encryption', 'ransom'],
        'Data Breaches': ['data breach', 'data leak', 'incident report', 'security incident'],
        'Physical Security': ['physical security', 'ot security', 'operational technology', 'ics', 'industrial control systems'],
        'AI and Emerging Technologies': ['artificial intelligence', 'ai', 'machine learning', 'ml', 'emerging technology', 'generative ai'],
        'Industry Trends': ['industry trends', 'cybersecurity trends', 'security report', 'annual report', 'survey', 'study', 'statistics', 'findings'],
        'Identity Security': ['identity', 'iam', 'identity and access management', 'authentication', 'mfa', 'zero trust', 'access control'],
        'Penetration Testing': ['penetration testing', 'pentesting', 'red team', 'offensive security', 'security testing'],
        'Privacy and Data Protection': ['privacy', 'data protection', 'gdpr', 'ccpa', 'data privacy', 'compliance'],
        'Email Security': ['email security', 'email threats', 'phishing', 'business email compromise', 'bec'],
        'Voice': ['voice', 'ciso', 'chief information security officer', 'leadership', 'executive'],
    }
    
    content_lower = content.lower()
    title_lower = title.lower()
    org_lower = org_name.lower()
    
    # Check for survey indicators first
    survey_indicators = ['survey', 'study', 'poll', 'respondents', 'interviewed', 'questionnaire', 'feedback', 'voice of', 'findings']
    is_survey = any(indicator in content_lower or indicator in title_lower for indicator in survey_indicators)
    
    # Special handling for specific organizations and titles
    if 'proofpoint' in org_lower and 'voice' in title_lower:
        if 'Voice' in available_categories.get("Survey", []):
            return "Survey", "Voice"
        elif 'Industry Trends' in available_categories.get("Survey", []):
            return "Survey", "Industry Trends"
    
    # Score categories based on keyword frequency
    category_scores = {}
    for category, keywords in keyword_mapping.items():
        score = sum(content_lower.count(keyword) for keyword in keywords)
        # Boost score if keywords appear in title
        score += sum(title_lower.count(keyword) * 2 for keyword in keywords)
        category_scores[category] = score
    
    # Find the best matching category
    best_category = max(category_scores, key=category_scores.get) if any(category_scores.values()) else "Industry Trends"
    
    print(f"Category scores for {org_name}: {dict(sorted(category_scores.items(), key=lambda x: x[1], reverse=True)[:5])}")
    print(f"Best category: {best_category}, Is survey: {is_survey}")
    
    # Determine report type and ensure category exists
    report_type = "Survey" if is_survey else "Analysis"
    
    # Check if the best category exists in the available categories for this type
    if best_category in available_categories[report_type]:
        return report_type, best_category
    
    # Check if it exists in the other type
    other_type = "Analysis" if report_type == "Survey" else "Survey"
    if best_category in available_categories[other_type]:
        return other_type, best_category
    
    # Fall back to a generic category that exists
    for generic in ["Industry Trends", "Other"]:
        if generic in available_categories[report_type]:
            return report_type, generic
        if generic in available_categories[other_type]:
            return other_type, generic
    
    # Ultimate fallback - use the first available category
    if available_categories[report_type]:
        return report_type, available_categories[report_type][0]
    if available_categories[other_type]:
        return other_type, available_categories[other_type][0]
    
    return "Analysis", "Industry Trends"

def analyze_content(content: str, org_name: str, year: str, report_title: str, available_categories: Dict[str, List[str]]) -> Dict[str, Any]:
    """Analyze content using AI or fallback methods"""
    if not MODEL:
        print("No AI model available, using fallback analysis")
        return fallback_analysis(content, org_name, year, report_title, available_categories)

    try:
        # First, get basic categorization using fallback
        fallback_type, fallback_category = categorize_content_fallback(content, available_categories, org_name, report_title)
        
        # Summarization with AI
        summary_prompt_path = ".github/ai-prompts/markdown-summarization-prompt.md"
        try:
            with open(summary_prompt_path, 'r', encoding='utf-8') as f:
                summary_base_prompt = f.read()
        except FileNotFoundError:
            summary_base_prompt = """Please create a concise summary of this security report in 1-2 sentences. 
Focus on the key findings, threats, or insights. Keep it under 400 characters and professional."""
        
        # Truncate content for summary (keep within token limits)
        summary_content = content[:20000] if len(content) > 20000 else content
        summary_prompt = f"{summary_base_prompt}\n\nOrganization: {org_name}\nReport Title: {report_title}\nYear: {year}\n\nReport Content:\n{summary_content}"
        
        summary_model = genai.GenerativeModel(MODEL)
        summary_response = summary_model.generate_content(
            summary_prompt,
            generation_config={"temperature": 0.1, "max_output_tokens": 200}
        )
        
        summary = summary_response.text.strip() if summary_response.text else ""
        
        # Clean up and ensure reasonable length
        if summary:
            summary = ' '.join(summary.split())
            if len(summary) > 400:
                sentences = summary.split('. ')
                summary = ''
                for sentence in sentences:
                    if len(summary + sentence + '. ') <= 400:
                        summary += sentence + '. '
                    else:
                        break
                summary = summary.strip()
        else:
            summary = f"Security report from {org_name} covering industry insights and cybersecurity trends."

        # Classification and Categorization with AI
        categorization_prompt_path = ".github/ai-prompts/report-categorization-prompt.md"
        try:
            with open(categorization_prompt_path, 'r', encoding='utf-8') as f:
                categorization_base_prompt = f.read()
        except FileNotFoundError:
            categorization_base_prompt = """Analyze this security report and classify it into the appropriate type and category.

Return your response as JSON with the following structure:
{
  "type": "Analysis" or "Survey",
  "category": "category_name"
}

Available categories:
{{CATEGORIES}}

Guidelines:
- "Analysis" reports focus on technical analysis, threat intelligence, vulnerabilities
- "Survey" reports focus on industry trends, polling data, executive perspectives
- Choose the most specific applicable category"""

        # Build category list from available categories
        all_categories = []
        for report_type, categories in available_categories.items():
            all_categories.extend(categories)
        all_categories = sorted(list(set(all_categories)))  # Remove duplicates and sort
        
        category_str = '\n'.join([f"- {cat}" for cat in all_categories])
        categorization_prompt = categorization_base_prompt.replace("{{CATEGORIES}}", category_str)
        
        # Truncate content for categorization
        categorization_content = content[:12000] if len(content) > 12000 else content
        categorization_prompt += f"\n\nOrganization: {org_name}\nTitle: {report_title}\nYear: {year}\n\n{categorization_content}"

        category_model = genai.GenerativeModel(MODEL)
        category_response = category_model.generate_content(
            categorization_prompt,
            generation_config={"temperature": 0.1, "max_output_tokens": 100}
        )
        
        try:
            response_text = category_response.text.strip().replace('```json', '').replace('```', '').strip()
            classification = json.loads(response_text)
            
            if 'type' not in classification or 'category' not in classification:
                raise ValueError("Missing 'type' or 'category' in AI response.")
            
            # Validate that the category exists in our available categories
            report_type = classification.get('type', 'Analysis')
            category = classification.get('category', 'Industry Trends')
            
            # Check if category exists in the specified type
            if category not in available_categories.get(report_type, []):
                print(f"AI suggested category '{category}' not found in {report_type} categories, using fallback")
                report_type, category = fallback_type, fallback_category
                
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Could not parse AI response for classification: {e}. Using fallback.")
            report_type, category = fallback_type, fallback_category

        print(f"Final classification: {report_type} / {category}")

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
        return fallback_analysis(content, org_name, year, report_title, available_categories)

def fallback_analysis(content: str, org_name: str, year: str, report_title: str, available_categories: Dict[str, List[str]]) -> Dict[str, Any]:
    """Create analysis using fallback methods when AI is not available"""
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
    
    report_type, category = categorize_content_fallback(content, available_categories, org_name, report_title)
    
    return {
        'organization': org_name,
        'year': year,
        'title': report_title,
        'summary': summary,
        'type': report_type,
        'category': category,
        'ai_processed': False
    }

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
        'ibm': 'https://www.ibm.com',
        'proofpoint': 'https://www.proofpoint.com'
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

def main():
    parser = argparse.ArgumentParser(description="Analyze markdown content of security reports.")
    parser.add_argument("conversions_json", help="Path to the JSON file with conversion results.")
    parser.add_argument("--readme-path", help="Path to the README.md file.", default="README.md")
    parser.add_argument("--output-json", help="Path to save the analysis results as a JSON file.", default="analysis.json")
    args = parser.parse_args()

    # Validate input files
    if not os.path.exists(args.conversions_json):
        print(f"ERROR: Conversion results file not found: {args.conversions_json}")
        sys.exit(1)

    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        print("Warning: GEMINI_API_KEY not set. Using fallback analysis.")
    else:
        setup_gemini(gemini_api_key)

    available_categories = parse_toc_from_readme(args.readme_path)
    print(f"Available categories: {available_categories}")

    with open(args.conversions_json, 'r') as f:
        conversions = json.load(f)

    if not conversions:
        print("No conversion results found")
        with open(args.output_json, 'w') as f:
            json.dump([], f)
        sys.exit(0)

    print(f"Processing {len(conversions)} conversion results...")

    analysis_results = []
    for i, conv in enumerate(conversions, 1):
        print(f"\n=== Analyzing {i}/{len(conversions)} ===")
        
        if conv['status'] != 'success':
            print(f"Skipping failed conversion: {conv.get('pdf_path', 'unknown')}")
            continue
            
        try:
            output_path = conv.get('output_path')
            if not output_path or not os.path.exists(output_path):
                print(f"Markdown file not found: {output_path}")
                continue
                
            with open(output_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if not content.strip():
                print(f"Markdown file is empty: {output_path}")
                continue
            
            # Extract info using the correct path
            pdf_path = conv.get('pdf_path', output_path)
            org_name, year, report_title = extract_info_from_path(pdf_path)
            
            # Use data from conversion if available
            if 'organization_name' in conv:
                org_name = conv['organization_name']
            if 'report_title' in conv:
                report_title = conv['report_title']
            
            print(f"Analyzing: {org_name} - {report_title} ({year})")

            analysis = analyze_content(content, org_name, year, report_title, available_categories)
            analysis['file_path'] = output_path
            analysis['pdf_path'] = pdf_path
            
            # Include organization URL from conversion if available
            if 'organization_url' in conv and conv['organization_url']:
                analysis['organization_url'] = conv['organization_url']
            else:
                # Generate a default organization URL based on the organization name
                analysis['organization_url'] = generate_default_org_url(org_name)
            
            analysis_results.append(analysis)
            print(f"SUCCESS: {org_name} -> {analysis['type']} / {analysis['category']}")
            
        except Exception as e:
            print(f"ERROR: Failed to analyze {conv.get('output_path', 'unknown')}: {e}")
            continue

    # Save results
    with open(args.output_json, 'w') as f:
        json.dump(analysis_results, f, indent=2)

    print(f"\n=== ANALYSIS SUMMARY ===")
    print(f"Total conversions: {len(conversions)}")
    print(f"Successful conversions: {len([c for c in conversions if c['status'] == 'success'])}")
    print(f"Successfully analyzed: {len(analysis_results)}")
    
    if analysis_results:
        print("\nResults:")
        for result in analysis_results:
            ai_indicator = "🤖" if result.get('ai_processed') else "📝"
            print(f"  {ai_indicator} {result['organization']} - {result['title']} -> {result['type']} / {result['category']}")
    else:
        print("⚠️  No reports were successfully analyzed")

    return 0 if analysis_results else 1

if __name__ == "__main__":
    sys.exit(main())