import os
import sys
import json
import re
import argparse
from google import genai
from google.genai import types
import urllib.parse
from googleapiclient.discovery import build
from typing import List, Dict, Any, Tuple, Optional
from pathlib import Path
from datetime import datetime

# Configure Gemini API
def load_ai_config():
    try:
        config_path = Path(__file__).parent.parent / "artifacts" / "ai-models.json"
        with open(config_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Warning: Failed to load AI config: {e}. Using defaults.")
        return None

AI_CONFIG = load_ai_config()
if not AI_CONFIG:
    print("ERROR: AI config file 'artifacts/ai-models.json' not found or is invalid. Cannot proceed.")
    sys.exit(1)
MODELS = AI_CONFIG["models"]["priority_list"]
MODEL = None
CLIENT = None

def setup_gemini(api_key: str):
    global MODEL, CLIENT
    CLIENT = genai.Client(api_key=api_key)
    for model_name in MODELS:
        try:
            response = CLIENT.models.generate_content(
                model=model_name,
                contents="Hello"
            )
            if response.text:
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
        "Threat Intelligence": ["threat", "actor", "malware", "apt", "campaign", "intelligence", "ioc", "ttps"],
        "Application Security": ["appsec", "application", "software", "code", "devsecops", "sast", "dast", "dependency"],
        "Cloud Security": ["cloud", "aws", "azure", "gcp", "kubernetes", "container", "serverless"],
        "Vulnerabilities": ["vulnerability", "cve", "exploit", "patch", "zero-day", "disclosure"],
        "Ransomware": ["ransomware", "extortion", "encryption", "ransom"],
        "Data Breaches": ["breach", "leak", "exposure", "incident", "compromise"],
        "Identity Security": ["identity", "iam", "authentication", "sso", "mfa", "passwordless"],
        "Industry Trends": ["trend", "survey", "report", "state of", "annual", "industry", "statistics"],
    }

    content_lower = content.lower()
    title_lower = title.lower()
    
    scores = {}
    for category, keywords in keyword_mapping.items():
        score = sum(content_lower.count(keyword) for keyword in keywords)
        title_score = sum(title_lower.count(keyword) * 3 for keyword in keywords)  # Weight title matches higher
        scores[category] = score + title_score
    
    if scores:
        best_category = max(scores, key=scores.get)
        if scores[best_category] > 0:
            # Determine report type based on category
            survey_categories = ["Industry Trends", "Identity Security"]
            report_type = "Survey" if best_category in survey_categories else "Analysis"
            
            # Verify category exists in available categories
            if report_type in available_categories and best_category in available_categories[report_type]:
                print(f"Fallback categorization: {report_type} / {best_category} (score: {scores[best_category]})")
                return report_type, best_category
    
    # Default fallback
    print("Using default category: Analysis / Threat Intelligence")
    return "Analysis", available_categories["Analysis"][0] if available_categories["Analysis"] else "Threat Intelligence"

def generate_summary_with_ai(content: str, org_name: str, title: str) -> str:
    """Generate a summary using Gemini API"""
    try:
        prompt = f"""Provide a 2-3 sentence summary of this security report from {org_name} titled "{title}".

Focus on:
1. Main topic/theme of the report
2. Key findings or statistics (if any)
3. Primary audience or use case

Report content (first 5000 characters):
{content[:5000]}"""

        response = CLIENT.models.generate_content(
            model=MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.3,
                max_output_tokens=200
            )
        )
        
        if response.text:
            summary = response.text.strip()
            print(f"AI-generated summary: {summary[:100]}...")
            return summary
        else:
            raise ValueError("Empty response from AI")
            
    except Exception as e:
        print(f"AI summary generation failed: {e}")
        return None

def categorize_with_ai(content: str, available_categories: Dict[str, List[str]], org_name: str, title: str) -> Tuple[str, str]:
    """Use AI to categorize the report"""
    try:
        categories_list_analysis = ', '.join(available_categories.get("Analysis", []))
        categories_list_survey = ', '.join(available_categories.get("Survey", []))
        
        prompt = f"""Categorize this security report from {org_name} titled "{title}".

Available Report Types and Categories:
- Analysis Reports: {categories_list_analysis}
- Survey Reports: {categories_list_survey}

Guidelines:
- "Analysis Reports" are technical reports analyzing threats, vulnerabilities, security trends
- "Survey Reports" are research-based reports with statistics, industry surveys, executive perspectives

Respond with ONLY:
Type: [Analysis or Survey]
Category: [exact category name from the list above]

Report content (first 3000 characters):
{content[:3000]}"""

        response = CLIENT.models.generate_content(
            model=MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.1,
                max_output_tokens=100
            )
        )
        
        if not response.text:
            raise ValueError("Empty response from AI")
            
        response_text = response.text.strip()
        print(f"AI categorization response: {response_text}")
        
        # Parse response
        type_match = re.search(r'Type:\s*(Analysis|Survey)', response_text, re.IGNORECASE)
        category_match = re.search(r'Category:\s*(.+?)(?:\n|$)', response_text, re.IGNORECASE)
        
        if type_match and category_match:
            report_type = type_match.group(1).capitalize()
            category = category_match.group(1).strip()
            
            # Validate category exists in available categories
            if report_type in available_categories and category in available_categories[report_type]:
                print(f"AI categorization: {report_type} / {category}")
                return report_type, category
            else:
                print(f"AI category '{category}' not in available list, using fallback")
        else:
            print("Could not parse AI categorization response, using fallback")
            
    except Exception as e:
        print(f"AI categorization failed: {e}")
    
    # Fallback to keyword-based categorization
    return categorize_content_fallback(content, available_categories, org_name, title)

def analyze_content(content: str, org_name: str, year: str, report_title: str, available_categories: Dict[str, List[str]]) -> Dict[str, Any]:
    """Analyze the markdown content and extract/generate metadata"""
    
    # Try AI-based analysis first if MODEL is available
    if MODEL and CLIENT:
        try:
            print("Attempting AI-based analysis...")
            summary = generate_summary_with_ai(content, org_name, report_title)
            if summary:
                report_type, category = categorize_with_ai(content, available_categories, org_name, report_title)
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
            print(f"AI analysis failed, falling back to rule-based: {e}")
    
    # Fallback: Extract summary from content
    print("Using fallback analysis...")
    lines = [line.strip() for line in content.split('\n') if line.strip()]
    summary_candidates = []
    
    # Try to find introduction or summary section
    in_intro = False
    for i, line in enumerate(lines):
        if any(keyword in line.lower() for keyword in ['introduction', 'executive summary', 'overview', 'abstract']):
            in_intro = True
            continue
        if in_intro and len(line) > 50 and not line.startswith('#'):
            summary_candidates.append(line)
            if len(summary_candidates) >= 3:
                break
        if in_intro and line.startswith('#'):
            break
    
    # If no good summary found, use first substantial paragraphs
    if not summary_candidates:
        summary_candidates = [line for line in lines if len(line) > 50 and not line.startswith('#')][:3]
    
    summary = ' '.join(summary_candidates[:2]) if summary_candidates else f"Security report from {org_name} covering {report_title.lower()}."
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
    query = f'{org_name} {title} {year}'
    print(f"Performing Google Custom Search with query: {query}")

    try:
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=query, cx=cse_id, num=5).execute()

        items = res.get('items', [])
        if not items:
            print("No results found from Google Custom Search.")
            return None

        # Simplified Result Prioritization
        org_lower = org_name.lower()
        title_keywords = {word for word in re.findall(r'\b\w{4,}\b', title.lower())}
        results_urls = [item['link'] for item in items]

        # 1. High priority: URL contains org name and at least one significant title keyword
        for url in results_urls:
            url_lower = url.lower()
            if org_lower in url_lower:
                if any(keyword in url_lower for keyword in title_keywords):
                    print(f"Found high-priority match (org + title keyword): {url}")
                    return url

        # 2. Medium priority: URL contains just the org name
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
    current_year = datetime.now().year
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
            
            pdf_path = conv.get('pdf_path', output_path)
            
            # Use data from conversion if available, otherwise extract from path
            if conv.get('organization_name') and conv.get('report_title'):
                org_name = conv['organization_name']
                report_title = conv['report_title']
                # Extract year from path or use current year dynamically
                year = str(current_year)
                for part in Path(pdf_path).parts:
                    if part.isdigit() and len(part) == 4 and part.startswith("20"):
                        year = part
                        break
            else:
                org_name, year, report_title = extract_info_from_path(pdf_path)
            
            # Check if report is older than 2 years
            try:
                report_year_int = int(year)
                if report_year_int < (current_year - 2):
                    print(f"SKIPPING: {org_name} - {report_title} ({year}) is older than 2 years. Skipping analysis and README update.")
                    continue
            except ValueError:
                print(f"Warning: Could not parse year '{year}' for age check. Proceeding...")

            print(f"Analyzing: {org_name} - {report_title} ({year})")

            analysis = analyze_content(content, org_name, year, report_title, available_categories)
            analysis['file_path'] = output_path
            analysis['pdf_path'] = pdf_path

            # Get organization URL (this is where we do the search, not in pdf-converter)
            org_url = get_organization_url(org_name, report_title, year)
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

    return 0

if __name__ == "__main__":
    sys.exit(main())