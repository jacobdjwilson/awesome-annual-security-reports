import os
import sys
import json
import re
import argparse
import google.generativeai as genai
import urllib.parse
from googleapiclient.discovery import build
from typing import List, Dict, Any, Tuple, Optional
from pathlib import Path

# Configure Gemini API
MODELS = ["gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-3-pro"]
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
            structure["Survey"] = ["Industry Trends", "Identity Security", "Application Security", "Cloud Security", "Voice"]
            
        return structure
        
    except Exception as e:
        print(f"Warning: Error parsing README.md: {e}, using default categories")
        return {
            "Analysis": ["Threat Intelligence", "Application Security", "Cloud Security", "Vulnerabilities", "Industry Trends"],
            "Survey": ["Industry Trends", "Identity Security", "Application Security", "Cloud Security", "Voice"]
        }

def extract_info_from_path(file_path: str) -> Tuple[str, str, str]:
    """Extract organization, year, and title from file path with improved parsing"""
    path = Path(file_path)
    
    # Extract year from path
    year = "Unknown"
    for part in path.parts:
        if part.isdigit() and len(part) == 4 and part.startswith("20"):
            year = part
            break
    
    # Parse filename to extract organization and title
    filename = path.stem
    print(f"Parsing filename: {filename}")
    
    # General parsing - try different separators
    separators = [' - ', '_-_', '--', '_', '-']
    org_name = None
    title = None

    for sep in separators:
        if sep in filename:
            parts = filename.split(sep, 1)
            if len(parts) != 2:
                continue

            org_part, title_part = parts
            if not org_part.strip() or not title_part.strip():
                continue
        
            # Clean up organization name
            org_name = ' '.join(word.capitalize() for word in org_part.replace('_', ' ').replace('-', ' ').split())
        
            # Clean up title - convert dashes/underscores to spaces and capitalize
            title = ' '.join(word.capitalize() for word in title_part.replace('_', ' ').replace('-', ' ').split())
            title = re.sub(r'\s*20\d{2}\s*', '', title).strip()

            if org_name.lower() == title.lower():
                org_name, title = None, None # Reset on bad parse
                continue
        
            # Handle special cases for well-known organizations
            org_mapping = {
                'Blackduck': 'BlackDuck',
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
                
            # Clean up common title patterns
            title = re.sub(r'\b(report|security|annual)\b', lambda m: m.group(1).capitalize(), title, flags=re.IGNORECASE)
            break # Successful parse, exit loop

    if not org_name or not title:
        # Fallback if parsing fails - try to extract organization from start
        words = filename.replace('_', ' ').replace('-', ' ').split()
        if words:
            # First word is likely the organization
            org_name = words[0].capitalize()
            if len(words) > 1:
                title = ' '.join(word.capitalize() for word in words[1:])
            else:
                title = f"Security Report {year}"
        else:
            org_name = "Unknown Organization"
            title = f"Security Report {year}"
    
    print(f"Extracted - Org: '{org_name}', Title: '{title}', Year: '{year}'")
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
        'Voice': ['voice', 'ciso', 'chief information security officer', 'leadership', 'executive', 'voice of'],
    }
    
    content_lower = content.lower()
    title_lower = title.lower()
    org_lower = org_name.lower()
    
    # Check for survey indicators first
    survey_indicators = ['survey', 'study', 'poll', 'respondents', 'interviewed', 'questionnaire', 'feedback', 'voice of', 'findings']
    is_survey = any(indicator in content_lower or indicator in title_lower for indicator in survey_indicators)
    
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

def get_organization_url(org_name: str, title: str, year: str) -> Optional[str]:
    """
    Performs an optimized Google search and returns the best URL.
    """
    api_key = os.environ.get("GOOGLE_SEARCH_API_KEY")
    cse_id = os.environ.get("GOOGLE_CSE_ID")

    if not api_key or not cse_id:
        print("Warning: GOOGLE_SEARCH_API_KEY or GOOGLE_CSE_ID not set. Skipping URL search.")
        return f"https://www.{''.join(e for e in org_name if e.isalnum()).lower()}.com"

    # Simplified search query
    # Use a less restrictive query without quotes for more flexible matching
    query = f'{org_name} {title} {year}'
    print(f"Performing Google Custom Search with query: {query}")

    try:
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=query, cx=cse_id, num=5).execute()

        items = res.get('items', [])
        if not items:
            print("No results found from Google Custom Search.")
            return None

        # --- Simplified Result Prioritization ---
        org_lower = org_name.lower()
        # Get significant keywords from the title (more than 3 letters)
        title_keywords = {word for word in re.findall(r'\b\w{4,}\b', title.lower())}
        results_urls = [item['link'] for item in items]

        # 1. High priority: URL contains org name and at least one significant title keyword
        for url in results_urls:
            url_lower = url.lower()
            if org_lower in url_lower:
                # Check if any title keyword is in the URL
                if any(keyword in url_lower for keyword in title_keywords):
                    print(f"Found high-priority match (org + title keyword): {url}")
                    return url

        # 2. Medium priority: URL contains just the org name (if no title keyword match)
        for url in results_urls:
            if org_lower in url.lower():
                print(f"Found medium-priority match (org name only): {url}")
                return url

        # 3. Low priority (Fallback): Return the very first result
        print(f"No specific match found, returning the first result: {results_urls[0]}")
        return results_urls[0]

    except Exception as e:
        print(f"Error during Google Custom Search API call: {e}")
        return f"https://www.{''.join(e for e in org_name if e.isalnum()).lower()}.com"

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
            
            # Use data from conversion if available, otherwise extract from path
            if conv.get('organization_name') and conv.get('report_title'):
                org_name = conv['organization_name']
                report_title = conv['report_title']
                # Extract year from path or use current year dynamically
                from datetime import datetime
                year = str(datetime.now().year)
                for part in Path(pdf_path).parts:
                    if part.isdigit() and len(part) == 4 and part.startswith("20"):
                        year = part
                        break
            else:
                org_name, year, report_title = extract_info_from_path(pdf_path)
            
            print(f"Analyzing: {org_name} - {report_title} ({year})")

            analysis = analyze_content(content, org_name, year, report_title, available_categories)
            analysis['file_path'] = output_path
            analysis['pdf_path'] = pdf_path

            # Use the URL from the conversion step, or generate a search URL as a reliable fallback.
            org_url = conv.get('organization_url') if conv.get('organization_url') else get_organization_url(org_name, report_title, year)
            analysis['organization_url'] = org_url
            
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
            ai_indicator = "AI" if result.get('ai_processed') else "FB"
            print(f"  {ai_indicator} {result['organization']} - {result['title']} -> {result['type']} / {result['category']}")
    else:
        print("WARNING: No reports were successfully analyzed")

    return 0 if analysis_results else 1

if __name__ == "__main__":
    sys.exit(main())