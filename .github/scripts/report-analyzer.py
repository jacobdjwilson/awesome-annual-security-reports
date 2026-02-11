import os
import sys
import json
import re
import argparse
from typing import List, Dict, Any, Tuple, Optional
from pathlib import Path
from datetime import datetime

# Dual SDK support
try:
    from google import genai
    from google.genai import types
    USE_NEW_SDK = True
except ImportError:
    import google.generativeai as genai
    from google.api_core import exceptions
    USE_NEW_SDK = False

from googleapiclient.discovery import build

# ==========================
# CONFIGURATION LOADING
# ==========================
def load_json_config(config_path: Path) -> Optional[Dict[str, Any]]:
    """Load JSON config with error handling."""
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return None

ARTIFACTS_DIR = Path(__file__).parent.parent / "artifacts"
AI_CONFIG = load_json_config(ARTIFACTS_DIR / "ai-models.json")
PIPELINE_CONFIG = load_json_config(ARTIFACTS_DIR / "pipeline-config.json")
CATEGORIES_CONFIG = load_json_config(ARTIFACTS_DIR / "report-categories.json")

# Extract with fallbacks
if AI_CONFIG:
    MODELS = AI_CONFIG.get("models", {}).get("priority_list", ["gemini-2.0-flash-exp", "gemini-1.5-flash"])
else:
    MODELS = ["gemini-2.0-flash-exp", "gemini-1.5-flash", "gemini-1.5-pro"]

if PIPELINE_CONFIG:
    AGE_THRESHOLD = PIPELINE_CONFIG.get("processing", {}).get("age_threshold_years", 2)
    ORG_MAPPINGS = PIPELINE_CONFIG.get("organization_mappings", {})
else:
    AGE_THRESHOLD = 2
    ORG_MAPPINGS = {
        'Blackduck': 'BlackDuck',
        'Cyberark': 'CyberArk',
        'Sailpoint': 'SailPoint',
        'Crowdstrike': 'CrowdStrike',
        'Palo Alto': 'Palo Alto Networks',
        'Proofpoint': 'Proofpoint'
    }

MODEL = None
CLIENT = None

# ==========================
# AI SETUP
# ==========================
def setup_gemini(api_key: str) -> bool:
    """Setup Gemini with dual SDK support."""
    global MODEL, CLIENT
    
    if USE_NEW_SDK:
        CLIENT = genai.Client(api_key=api_key)
        for model_name in MODELS:
            try:
                response = CLIENT.models.generate_content(
                    model=model_name,
                    contents="test"
                )
                if response.text:
                    MODEL = model_name
                    print(f"✓ Verified model: {MODEL}")
                    return True
            except Exception as e:
                print(f"  Model {model_name} unavailable: {str(e)[:40]}")
                continue
    else:
        genai.configure(api_key=api_key)
        for model_name in MODELS:
            try:
                test_model = genai.GenerativeModel(model_name)
                test_response = test_model.count_tokens("test")
                if test_response.total_tokens:
                    MODEL = model_name
                    print(f"✓ Verified model: {MODEL}")
                    return True
            except Exception as e:
                print(f"  Model {model_name} unavailable: {str(e)[:40]}")
                continue
    
    print("WARNING: No AI models available")
    return False

# ==========================
# SUMMARY VALIDATOR
# ==========================
class SummaryValidator:
    """Validates and sanitizes AI summaries."""
    
    REQUIRED_VERBS = [
        'analyzes', 'examines', 'evaluates', 'assesses', 'reviews',
        'interprets', 'dissects', 'deconstructs', 'scrutinizes',
        'compares', 'investigates', 'explores', 'probes', 'surveys',
        'inquires', 'studies', 'documents', 'traces', 'maps',
        'highlights', 'focuses', 'provides', 'offers', 'outlines'
    ]
    
    MAX_LENGTH = 400
    MIN_LENGTH = 40
    
    @classmethod
    def validate(cls, summary: str) -> Tuple[bool, List[str]]:
        """Validate summary against rules."""
        errors = []
        
        if not summary:
            return False, ["Empty summary"]
        
        # Length
        if len(summary) > cls.MAX_LENGTH:
            errors.append(f"Too long: {len(summary)} > {cls.MAX_LENGTH}")
        elif len(summary) < cls.MIN_LENGTH:
            errors.append(f"Too short: {len(summary)} < {cls.MIN_LENGTH}")
        
        # Single line
        if '\n' in summary:
            errors.append("Contains newlines")
        
        # Starting verb
        first_word = summary.split()[0].lower().rstrip('.,;:') if summary.split() else ''
        if first_word not in cls.REQUIRED_VERBS:
            errors.append(f"Bad start word: '{first_word}'")
        
        # Invalid characters
        if not re.match(r"^[a-zA-Z0-9\s',.\-]+$", summary):
            errors.append("Invalid characters")
        
        # Parentheses/quotes
        if '(' in summary or ')' in summary or '"' in summary:
            errors.append("Contains parentheses or quotes")
        
        return len(errors) == 0, errors
    
    @classmethod
    def sanitize(cls, summary: str) -> str:
        """Fix common issues."""
        if not summary:
            return ""
        
        # Clean up
        summary = ' '.join(summary.split())
        summary = re.sub(r'[()"\']', '', summary)
        
        # Limit length
        if len(summary) > cls.MAX_LENGTH:
            sentences = summary.split('. ')
            summary = ''
            for s in sentences:
                if len(summary + s + '. ') <= cls.MAX_LENGTH:
                    summary += s + '. '
                else:
                    break
        
        # Ensure period
        if summary and not summary.endswith('.'):
            summary += '.'
        
        return summary.strip()

# ==========================
# URL CONSTRUCTOR
# ==========================
def construct_report_url(pdf_path: str, year: str) -> str:
    """
    Construct proper Annual%20Security URL.
    NEVER returns Google search links.
    """
    pdf_filename = Path(pdf_path).name
    encoded = pdf_filename.replace(' ', '%20')
    return f"Annual%20Security%20Reports/{year}/{encoded}"

def construct_org_url(org_name: str, search_url: Optional[str] = None) -> str:
    """
    Construct organization URL.
    If search_url is a Google search, extract intended domain or use fallback.
    """
    if search_url and 'google.com/search' not in search_url:
        return search_url
    
    # Create fallback URL
    clean_name = ''.join(c for c in org_name if c.isalnum()).lower()
    return f"https://www.{clean_name}.com"

# ==========================
# CATEGORY LOADER
# ==========================
def load_categories() -> Dict[str, List[str]]:
    """Load categories from config."""
    if not CATEGORIES_CONFIG:
        return {
            "Analysis": ["Threat Intelligence", "Cloud Security", "Application Security"],
            "Survey": ["Industry Trends", "Identity Security"]
        }
    
    categories = {"Analysis": [], "Survey": []}
    for parent_cat in CATEGORIES_CONFIG.get("categories", []):
        parent_name = parent_cat["parent"].replace(" Reports", "")
        for sub_cat in parent_cat.get("sub_categories", []):
            categories[parent_name].append(sub_cat["name"])
    
    return categories

# ==========================
# AI ANALYSIS
# ==========================
def analyze_with_ai(content: str, org: str, year: str, title: str) -> Dict[str, Any]:
    """Analyze content with AI."""
    try:
        # Summarization
        summary_prompt_path = ".github/ai-prompts/markdown-summarization-prompt.md"
        if not os.path.exists(summary_prompt_path):
            raise FileNotFoundError(f"Prompt not found: {summary_prompt_path}")
        
        with open(summary_prompt_path, 'r') as f:
            summary_prompt = f.read()
        
        # Clean content
        clean_content = re.sub(r'!\[.*?\]\(.*?\)', '', content, flags=re.DOTALL)
        truncated = clean_content[:20000] if len(clean_content) > 20000 else clean_content
        
        full_prompt = f"{summary_prompt}\n\nOrg: {org}\nTitle: {title}\nYear: {year}\n\n{truncated}"
        
        # Generate summary
        if USE_NEW_SDK:
            response = CLIENT.models.generate_content(
                model=MODEL,
                contents=full_prompt,
                config=types.GenerateContentConfig(temperature=0.1, max_output_tokens=200)
            )
        else:
            model = genai.GenerativeModel(MODEL)
            response = model.generate_content(
                full_prompt,
                generation_config={"temperature": 0.1, "max_output_tokens": 200}
            )
        
        summary = response.text.strip() if response.text else ""
        
        # Validate and sanitize
        is_valid, errors = SummaryValidator.validate(summary)
        if not is_valid:
            print(f"  WARNING: Summary validation failed:")
            for err in errors:
                print(f"    - {err}")
            summary = SummaryValidator.sanitize(summary)
            print(f"  Sanitized: {summary[:50]}...")
        
        # Categorization
        cat_prompt_path = ".github/ai-prompts/report-categorization-prompt.md"
        if not os.path.exists(cat_prompt_path):
            raise FileNotFoundError(f"Prompt not found: {cat_prompt_path}")
        
        with open(cat_prompt_path, 'r') as f:
            cat_prompt = f.read()
        
        # Build category list
        categories = load_categories()
        cat_list = '\n'.join([f"- {cat}" for cats in categories.values() for cat in cats])
        cat_prompt = cat_prompt.replace("{{CATEGORIES}}", cat_list)
        
        cat_content = clean_content[:12000] if len(clean_content) > 12000 else clean_content
        full_cat = f"{cat_prompt}\n\nOrg: {org}\nTitle: {title}\nYear: {year}\n\n{cat_content}"
        
        if USE_NEW_SDK:
            cat_response = CLIENT.models.generate_content(
                model=MODEL,
                contents=full_cat,
                config=types.GenerateContentConfig(temperature=0.1, max_output_tokens=100)
            )
        else:
            cat_model = genai.GenerativeModel(MODEL)
            cat_response = cat_model.generate_content(
                full_cat,
                generation_config={"temperature": 0.1, "max_output_tokens": 100}
            )
        
        # Parse categorization
        try:
            response_text = cat_response.text.strip()
            response_text = response_text.replace('```json', '').replace('```', '').strip()
            classification = json.loads(response_text)
            
            report_type = classification.get('type', 'Analysis')
            category = classification.get('category', 'Industry Trends')
        except (json.JSONDecodeError, ValueError) as e:
            print(f"  WARNING: Categorization parse failed: {e}")
            report_type = 'Analysis'
            category = 'Industry Trends'
        
        return {
            'type': report_type,
            'category': category,
            'summary': summary,
            'ai_processed': True
        }
        
    except Exception as e:
        print(f"  ERROR: AI analysis failed: {e}")
        return {
            'type': 'Analysis',
            'category': 'Industry Trends',
            'summary': f"Analyzes security findings from {org} for {year}.",
            'ai_processed': False
        }

# ==========================
# FALLBACK ANALYSIS
# ==========================
def fallback_analysis(content: str, org: str, year: str, title: str) -> Dict[str, Any]:
    """Simple fallback when AI unavailable."""
    # Extract meaningful sentences
    sentences = [s.strip() for s in content.split('.') if len(s.strip()) > 20 and not s.strip().startswith('#')]
    meaningful = sentences[:2] if sentences else [f"Security report from {org}"]
    
    summary = '. '.join(meaningful)
    if not summary.endswith('.'):
        summary += '.'
    
    # Limit and sanitize
    summary = SummaryValidator.sanitize(summary)
    
    # Simple categorization
    content_lower = content.lower()
    if 'survey' in title.lower() or 'survey' in content_lower:
        report_type = 'Survey'
        category = 'Industry Trends'
    else:
        report_type = 'Analysis'
        if 'cloud' in content_lower:
            category = 'Cloud Security'
        elif 'application' in content_lower or 'appsec' in content_lower:
            category = 'Application Security'
        elif 'threat' in content_lower:
            category = 'Threat Intelligence'
        else:
            category = 'Industry Trends'
    
    return {
        'type': report_type,
        'category': category,
        'summary': summary,
        'ai_processed': False
    }

# ==========================
# MAIN PROCESSING
# ==========================
def main():
    parser = argparse.ArgumentParser(description="Optimized Report Analyzer")
    parser.add_argument("conversions_json", help="Conversions JSON path")
    parser.add_argument("--output-json", default="analysis.json")
    args = parser.parse_args()
    
    # Validate input
    if not os.path.exists(args.conversions_json):
        print(f"ERROR: Conversions file not found: {args.conversions_json}")
        sys.exit(1)
    
    # Setup AI
    gemini_key = os.environ.get("GEMINI_API_KEY")
    if gemini_key:
        setup_gemini(gemini_key)
    else:
        print("WARNING: GEMINI_API_KEY not set")
    
    # Load conversions
    with open(args.conversions_json, 'r') as f:
        conversions = json.load(f)
    
    if not conversions:
        print("No conversions to process")
        with open(args.output_json, 'w') as f:
            json.dump([], f)
        sys.exit(0)
    
    print(f"\n{'='*60}")
    print(f"Processing {len(conversions)} conversions")
    print(f"{'='*60}\n")
    
    results = []
    current_year = datetime.now().year
    
    for i, conv in enumerate(conversions, 1):
        if conv['status'] != 'success':
            print(f"[{i}/{len(conversions)}] Skipping failed conversion")
            continue
        
        try:
            output_path = conv.get('output_path')
            if not output_path or not os.path.exists(output_path):
                print(f"[{i}/{len(conversions)}] Markdown not found")
                continue
            
            with open(output_path, 'r') as f:
                content = f.read()
            
            if not content.strip():
                print(f"[{i}/{len(conversions)}] Empty file")
                continue
            
            # Extract metadata
            pdf_path = conv.get('pdf_path', '')
            org_name = conv.get('organization_name', 'Unknown')
            report_title = conv.get('report_title', 'Security Report')
            
            # Apply org mappings
            for old, new in ORG_MAPPINGS.items():
                if org_name.lower() == old.lower():
                    org_name = new
                    break
            
            # Extract year
            year = str(current_year)
            for part in Path(pdf_path).parts:
                if part.isdigit() and len(part) == 4 and part.startswith("20"):
                    year = part
                    break
            
            # Age check
            try:
                if int(year) < (current_year - AGE_THRESHOLD):
                    print(f"[{i}/{len(conversions)}] Skipping old: {org_name} ({year})")
                    continue
            except ValueError:
                pass
            
            print(f"[{i}/{len(conversions)}] {org_name} - {report_title} ({year})")
            
            # Analyze
            if MODEL:
                analysis = analyze_with_ai(content, org_name, year, report_title)
            else:
                analysis = fallback_analysis(content, org_name, year, report_title)
            
            # Construct URLs - CRITICAL: Use actual URLs, not Google search
            report_url = construct_report_url(pdf_path, year)
            org_url = construct_org_url(org_name, conv.get('organization_url'))
            
            # Build result
            result = {
                'organization': org_name,
                'title': report_title,
                'year': year,
                'summary': analysis['summary'],
                'type': analysis['type'],
                'category': analysis['category'],
                'pdf_path': pdf_path,
                'report_url': report_url,  # Actual URL
                'organization_url': org_url,  # Not Google search
                'file_path': output_path,
                'ai_processed': analysis['ai_processed']
            }
            
            results.append(result)
            print(f"  ✓ {analysis['type']} / {analysis['category']}")
            
        except Exception as e:
            print(f"[{i}/{len(conversions)}] ERROR: {e}")
            continue
    
    # Save
    with open(args.output_json, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Analyzed: {len(results)}/{len(conversions)}")
    ai_count = len([r for r in results if r['ai_processed']])
    print(f"AI: {ai_count} | Fallback: {len(results) - ai_count}")
    print(f"\n✓ Results saved to: {args.output_json}")
    
    return 0 if results else 1

if __name__ == "__main__":
    sys.exit(main())