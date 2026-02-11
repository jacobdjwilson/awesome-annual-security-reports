import os
import sys
import json
import re
import argparse
from typing import List, Dict, Any, Tuple, Optional
from pathlib import Path
from datetime import datetime

# Try new SDK first, fallback to old
try:
    from google import genai
    from google.genai import types
    USE_NEW_SDK = True
except ImportError:
    import google.generativeai as genai
    from google.api_core import exceptions
    USE_NEW_SDK = False

from googleapiclient.discovery import build

# Load configuration (same as before)
def load_json_config(config_path: Path) -> Dict[str, Any]:
    """Load JSON configuration file with fallback"""
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

ARTIFACTS_DIR = Path(__file__).parent.parent / "artifacts"
AI_CONFIG = load_json_config(ARTIFACTS_DIR / "ai-models.json")
PIPELINE_CONFIG = load_json_config(ARTIFACTS_DIR / "pipeline-config.json")

# Extract configuration with fallbacks
if AI_CONFIG:
    MODELS = AI_CONFIG.get("models", {}).get("priority_list", ["gemini-2.0-flash-exp", "gemini-1.5-flash"])
else:
    MODELS = ["gemini-2.0-flash-exp", "gemini-1.5-flash", "gemini-1.5-pro"]

if PIPELINE_CONFIG:
    AGE_THRESHOLD_YEARS = PIPELINE_CONFIG.get("processing", {}).get("age_threshold_years", 2)
else:
    AGE_THRESHOLD_YEARS = 2

MODEL = None
CLIENT = None

def setup_gemini(api_key: str):
    """Setup Gemini AI with SDK detection."""
    global MODEL, CLIENT
    
    if USE_NEW_SDK:
        CLIENT = genai.Client(api_key=api_key)
        for model_name in MODELS:
            try:
                response = CLIENT.models.generate_content(model=model_name, contents="Test")
                if response.text:
                    MODEL = model_name
                    print(f"✓ Verified model: {MODEL}")
                    return True
            except Exception as e:
                print(f"Model {model_name} unavailable: {str(e)[:50]}")
                continue
    else:
        genai.configure(api_key=api_key)
        for model_name in MODELS:
            try:
                test_model = genai.GenerativeModel(model_name)
                test_response = test_model.count_tokens("Test")
                if test_response.total_tokens:
                    MODEL = model_name
                    print(f"✓ Verified model: {MODEL}")
                    return True
            except Exception as e:
                print(f"Model {model_name} unavailable: {str(e)[:50]}")
                continue
    
    if not MODEL:
        print("WARNING: No AI models available. Using fallback analysis.")
        return False
    return True

def construct_report_url(pdf_path: str, year: str) -> str:
    """
    Construct proper Annual%20Security%20Reports URL from PDF path.
    This ensures we use the actual report URL, not a Google search link.
    """
    pdf_filename = Path(pdf_path).name
    # URL encode the filename
    encoded_filename = pdf_filename.replace(' ', '%20')
    # Construct the full URL
    report_url = f"Annual%20Security%20Reports/{year}/{encoded_filename}"
    return report_url

def analyze_with_ai(content: str, org_name: str, year: str, report_title: str) -> Dict[str, Any]:
    """Analyze content using AI with enhanced validation."""
    
    try:
        # Summarization
        summary_prompt_path = ".github/ai-prompts/markdown-summarization-prompt.md"
        if not os.path.exists(summary_prompt_path):
            raise FileNotFoundError(f"Prompt not found: {summary_prompt_path}")
        
        with open(summary_prompt_path, 'r') as f:
            summary_prompt = f.read()
        
        # Clean content
        clean_content = re.sub(r'!\[.*?\]\(.*?\)', '', content, flags=re.DOTALL)
        summary_content = clean_content[:20000] if len(clean_content) > 20000 else clean_content
        
        full_summary_prompt = f"{summary_prompt}\n\nOrganization: {org_name}\nTitle: {report_title}\nYear: {year}\n\n{summary_content}"
        
        if USE_NEW_SDK:
            response = CLIENT.models.generate_content(
                model=MODEL,
                contents=full_summary_prompt,
                config=types.GenerateContentConfig(temperature=0.1, max_output_tokens=200)
            )
        else:
            model = genai.GenerativeModel(MODEL)
            response = model.generate_content(
                full_summary_prompt,
                generation_config={"temperature": 0.1, "max_output_tokens": 200}
            )
        
        summary = response.text.strip() if response.text else ""
        
        # Enhanced summary validation
        if summary:
            # Clean up
            summary = ' '.join(summary.split())
            # Remove any parentheses or quotes that slipped through
            summary = re.sub(r'[()"\']', '', summary)
            # Limit length
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
            summary = f"Analyzes security trends and insights from {org_name} covering {year} findings."
        
        # Categorization (keeping existing logic)
        categorization_prompt_path = ".github/ai-prompts/report-categorization-prompt.md"
        if not os.path.exists(categorization_prompt_path):
            raise FileNotFoundError(f"Prompt not found: {categorization_prompt_path}")
        
        with open(categorization_prompt_path, 'r') as f:
            categorization_prompt = f.read()
        
        # Stub categories (will be replaced by actual categories in production)
        categories_str = "- Threat Intelligence\n- Cloud Security\n- Application Security"
        categorization_prompt = categorization_prompt.replace("{{CATEGORIES}}", categories_str)
        
        categorization_content = clean_content[:12000] if len(clean_content) > 12000 else clean_content
        full_cat_prompt = f"{categorization_prompt}\n\nOrganization: {org_name}\nTitle: {report_title}\nYear: {year}\n\n{categorization_content}"
        
        if USE_NEW_SDK:
            cat_response = CLIENT.models.generate_content(
                model=MODEL,
                contents=full_cat_prompt,
                config=types.GenerateContentConfig(temperature=0.1, max_output_tokens=100)
            )
        else:
            cat_model = genai.GenerativeModel(MODEL)
            cat_response = cat_model.generate_content(
                full_cat_prompt,
                generation_config={"temperature": 0.1, "max_output_tokens": 100}
            )
        
        try:
            response_text = cat_response.text.strip().replace('```json', '').replace('```', '').strip()
            classification = json.loads(response_text)
            
            report_type = classification.get('type', 'Analysis')
            category = classification.get('category', 'Industry Trends')
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Could not parse categorization: {e}. Using defaults.")
            report_type = 'Analysis'
            category = 'Industry Trends'
        
        return {
            'type': report_type,
            'category': category,
            'summary': summary,
            'ai_processed': True
        }
        
    except Exception as e:
        print(f"AI analysis failed: {e}")
        return {
            'type': 'Analysis',
            'category': 'Industry Trends',
            'summary': f"Analyzes security findings from {org_name} for {year}.",
            'ai_processed': False
        }

def main():
    parser = argparse.ArgumentParser(description="Analyze security reports (enhanced)")
    parser.add_argument("conversions_json", help="Path to conversions JSON")
    parser.add_argument("--output-json", default="analysis.json", help="Output JSON path")
    args = parser.parse_args()
    
    if not os.path.exists(args.conversions_json):
        print(f"ERROR: Conversions file not found: {args.conversions_json}")
        sys.exit(1)
    
    # Setup AI
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if gemini_api_key:
        setup_gemini(gemini_api_key)
    else:
        print("WARNING: GEMINI_API_KEY not set. Using fallback analysis.")
    
    # Load conversions
    with open(args.conversions_json, 'r') as f:
        conversions = json.load(f)
    
    if not conversions:
        print("No conversions found")
        with open(args.output_json, 'w') as f:
            json.dump([], f)
        sys.exit(0)
    
    print(f"Processing {len(conversions)} conversions...")
    
    results = []
    current_year = datetime.now().year
    
    for i, conv in enumerate(conversions, 1):
        if conv['status'] != 'success':
            print(f"[{i}/{len(conversions)}] Skipping failed conversion")
            continue
        
        try:
            output_path = conv.get('output_path')
            if not output_path or not os.path.exists(output_path):
                print(f"[{i}/{len(conversions)}] Markdown not found: {output_path}")
                continue
            
            with open(output_path, 'r') as f:
                content = f.read()
            
            if not content.strip():
                print(f"[{i}/{len(conversions)}] Empty markdown file")
                continue
            
            pdf_path = conv.get('pdf_path', '')
            org_name = conv.get('organization_name', 'Unknown')
            report_title = conv.get('report_title', 'Security Report')
            
            # Extract year from path
            year = str(current_year)
            for part in Path(pdf_path).parts:
                if part.isdigit() and len(part) == 4 and part.startswith("20"):
                    year = part
                    break
            
            # Check age threshold
            try:
                if int(year) < (current_year - AGE_THRESHOLD_YEARS):
                    print(f"[{i}/{len(conversions)}] Skipping old report: {org_name} ({year})")
                    continue
            except ValueError:
                pass
            
            print(f"[{i}/{len(conversions)}] Analyzing: {org_name} - {report_title} ({year})")
            
            # Analyze content
            if MODEL:
                analysis = analyze_with_ai(content, org_name, year, report_title)
            else:
                analysis = {
                    'type': 'Analysis',
                    'category': 'Industry Trends',
                    'summary': f"Analyzes security trends from {org_name}.",
                    'ai_processed': False
                }
            
            # Construct proper report URL
            report_url = construct_report_url(pdf_path, year)
            
            # Get organization URL from conversion or construct fallback
            org_url = conv.get('organization_url')
            if not org_url or 'google.com/search' in org_url:
                # Construct fallback URL
                org_url = f"https://www.{''.join(e for e in org_name if e.isalnum()).lower()}.com"
            
            # Build final result
            result = {
                'organization': org_name,
                'title': report_title,
                'year': year,
                'summary': analysis['summary'],
                'type': analysis['type'],
                'category': analysis['category'],
                'pdf_path': pdf_path,
                'report_url': report_url,  # KEY: Actual report URL, not Google search
                'organization_url': org_url,
                'file_path': output_path,
                'ai_processed': analysis['ai_processed']
            }
            
            results.append(result)
            print(f"  ✓ {analysis['type']} / {analysis['category']}")
            
        except Exception as e:
            print(f"[{i}/{len(conversions)}] ERROR: {e}")
            continue
    
    # Save results
    with open(args.output_json, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n=== Summary ===")
    print(f"Analyzed: {len(results)}/{len(conversions)}")
    ai_processed = len([r for r in results if r['ai_processed']])
    print(f"AI Processed: {ai_processed} | Fallback: {len(results) - ai_processed}")
    
    return 0 if results else 1

if __name__ == "__main__":
    sys.exit(main())