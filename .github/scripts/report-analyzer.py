import os
import sys
import json
import re
import argparse
from typing import List, Dict, Any, Tuple, Optional
from pathlib import Path
from datetime import datetime
import hashlib

# Dual SDK support
try:
    from google import genai
    from google.genai import types
    USE_NEW_SDK = True
except ImportError:
    import google.generativeai as genai
    from google.api_core import exceptions
    USE_NEW_SDK = False

# ==========================
# CONFIGURATION LOADER
# ==========================
def load_json_config(config_path: Path) -> Optional[Dict[str, Any]]:
    """Load JSON config with error handling."""
    try:
        if config_path.exists():
            with open(config_path, 'r') as f:
                return json.load(f)
    except (json.JSONDecodeError, IOError):
        pass
    return None

ARTIFACTS_DIR = Path(__file__).parent.parent / "artifacts"
AI_CONFIG = load_json_config(ARTIFACTS_DIR / "ai-models.json")
PIPELINE_CONFIG = load_json_config(ARTIFACTS_DIR / "pipeline-config.json")
CATEGORIES_CONFIG = load_json_config(ARTIFACTS_DIR / "report-categories.json")

# Extract configuration with fallbacks
if AI_CONFIG:
    MODELS = AI_CONFIG.get("models", {}).get("priority_list", ["gemini-2.0-flash-exp"])
    GEN_CONFIG = AI_CONFIG.get("configurations", {}).get("default", {})
else:
    MODELS = ["gemini-2.0-flash-exp", "gemini-1.5-flash", "gemini-1.5-pro"]
    GEN_CONFIG = {"temperature": 0.1, "max_output_tokens": 200}

if PIPELINE_CONFIG:
    AGE_THRESHOLD = PIPELINE_CONFIG.get("processing", {}).get("age_threshold_years", 2)
    ORG_MAPPINGS = PIPELINE_CONFIG.get("organization_mappings", {})
else:
    AGE_THRESHOLD = 2
    ORG_MAPPINGS = {}

MODEL = None
CLIENT = None

# ==========================
# ANALYSIS CACHE
# ==========================
class AnalysisCache:
    """
    Cache for AI analysis results to minimize API calls.
    Uses content hash to detect if we've already analyzed similar content.
    """
    
    def __init__(self, cache_file: str = "analysis_cache.json"):
        self.cache_file = Path(cache_file)
        self.cache = self._load_cache()
        self.hits = 0
        self.misses = 0
    
    def _load_cache(self) -> Dict[str, Any]:
        """Load cache from disk."""
        if self.cache_file.exists():
            try:
                with open(self.cache_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return {}
    
    def _save_cache(self):
        """Save cache to disk."""
        try:
            with open(self.cache_file, 'w') as f:
                json.dump(self.cache, f, indent=2)
        except:
            pass
    
    def _hash_content(self, content: str, org: str, year: str) -> str:
        """Generate hash for content."""
        key = f"{org}:{year}:{content[:1000]}"
        return hashlib.md5(key.encode()).hexdigest()
    
    def get(self, content: str, org: str, year: str) -> Optional[Dict[str, Any]]:
        """Get cached analysis."""
        cache_key = self._hash_content(content, org, year)
        if cache_key in self.cache:
            self.hits += 1
            return self.cache[cache_key]
        self.misses += 1
        return None
    
    def set(self, content: str, org: str, year: str, analysis: Dict[str, Any]):
        """Cache analysis result."""
        cache_key = self._hash_content(content, org, year)
        self.cache[cache_key] = analysis
        self._save_cache()
    
    def stats(self) -> str:
        """Get cache statistics."""
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0
        return f"Cache: {self.hits} hits, {self.misses} misses ({hit_rate:.1f}% hit rate)"

# ==========================
# AI SETUP
# ==========================
def setup_gemini(api_key: str) -> bool:
    """Setup Gemini with SDK detection."""
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
                    print(f"✓ AI Model: {MODEL}")
                    return True
            except Exception:
                continue
    else:
        genai.configure(api_key=api_key)
        for model_name in MODELS:
            try:
                test_model = genai.GenerativeModel(model_name)
                test_response = test_model.count_tokens("test")
                if test_response.total_tokens:
                    MODEL = model_name
                    print(f"✓ AI Model: {MODEL}")
                    return True
            except Exception:
                continue
    
    print("WARNING: No AI models available")
    return False

# ==========================
# SUMMARY VALIDATOR
# ==========================
class SummaryValidator:
    """Validates and sanitizes summaries."""
    
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
        """Validate summary."""
        errors = []
        
        if not summary:
            return False, ["Empty"]
        
        if len(summary) > cls.MAX_LENGTH:
            errors.append(f"Long:{len(summary)}")
        elif len(summary) < cls.MIN_LENGTH:
            errors.append(f"Short:{len(summary)}")
        
        if '\n' in summary:
            errors.append("Newlines")
        
        first_word = summary.split()[0].lower().rstrip('.,;:') if summary.split() else ''
        if first_word not in cls.REQUIRED_VERBS:
            errors.append(f"BadStart:{first_word}")
        
        if not re.match(r"^[a-zA-Z0-9\s',.\-]+$", summary):
            errors.append("InvalidChars")
        
        if '(' in summary or ')' in summary or '"' in summary:
            errors.append("Quotes/Parens")
        
        return len(errors) == 0, errors
    
    @classmethod
    def sanitize(cls, summary: str) -> str:
        """Fix common issues."""
        if not summary:
            return ""
        
        summary = ' '.join(summary.split())
        summary = re.sub(r'[()"\']', '', summary)
        
        if summary and not summary.endswith('.'):
            summary += '.'
        
        if len(summary) > cls.MAX_LENGTH:
            sentences = summary.split('. ')
            summary = ''
            for s in sentences:
                if len(summary + s + '. ') <= cls.MAX_LENGTH:
                    summary += s + '. '
                else:
                    break
        
        return summary.strip()

# ==========================
# URL CONSTRUCTORS
# ==========================
def construct_report_url(pdf_path: str, year: str) -> str:
    """Construct proper Annual%20Security URL."""
    pdf_filename = Path(pdf_path).name
    encoded = pdf_filename.replace(' ', '%20')
    return f"Annual%20Security%20Reports/{year}/{encoded}"

def construct_org_url(org_name: str, search_url: Optional[str] = None) -> str:
    """Construct organization URL."""
    if search_url and 'google.com/search' not in search_url:
        return search_url
    
    clean_name = ''.join(c for c in org_name if c.isalnum()).lower()
    return f"https://www.{clean_name}.com"

# ==========================
# CATEGORY LOADER
# ==========================
def load_categories() -> Dict[str, List[str]]:
    """Load categories from config."""
    if not CATEGORIES_CONFIG:
        return {
            "Analysis": ["Global Threat Intelligence", "Cloud Security"],
            "Survey": ["Industry Trends"]
        }
    
    categories = {"Analysis": [], "Survey": []}
    for parent_cat in CATEGORIES_CONFIG.get("categories", []):
        parent_name = parent_cat["parent"].replace(" Reports", "")
        for sub_cat in parent_cat.get("sub_categories", []):
            categories[parent_name].append(sub_cat["name"])
    
    return categories

# ==========================
# AI ANALYSIS WITH CACHING
# ==========================
def analyze_with_ai(content: str, org: str, year: str, title: str, cache: AnalysisCache) -> Dict[str, Any]:
    """
    Analyze content with AI.
    Uses cache to minimize API calls.
    """
    
    # Check cache first
    cached = cache.get(content, org, year)
    if cached:
        print(f"  ✓ Using cached analysis")
        return cached
    
    try:
        # Summarization
        summary_prompt_path = ".github/ai-prompts/markdown-summarization-prompt.md"
        if not os.path.exists(summary_prompt_path):
            raise FileNotFoundError(f"Prompt not found: {summary_prompt_path}")
        
        with open(summary_prompt_path, 'r') as f:
            summary_prompt = f.read()
        
        # Clean and truncate content
        clean_content = re.sub(r'!\[.*?\]\(.*?\)', '', content, flags=re.DOTALL)
        truncated = clean_content[:20000] if len(clean_content) > 20000 else clean_content
        
        full_prompt = f"{summary_prompt}\n\nOrg: {org}\nTitle: {title}\nYear: {year}\n\n{truncated}"
        
        # Generate summary
        if USE_NEW_SDK:
            config = types.GenerateContentConfig(
                temperature=GEN_CONFIG.get("temperature", 0.1),
                max_output_tokens=GEN_CONFIG.get("max_output_tokens", 200)
            )
            response = CLIENT.models.generate_content(
                model=MODEL,
                contents=full_prompt,
                config=config
            )
        else:
            response = genai.GenerativeModel(MODEL).generate_content(
                full_prompt,
                generation_config={
                    "temperature": GEN_CONFIG.get("temperature", 0.1),
                    "max_output_tokens": GEN_CONFIG.get("max_output_tokens", 200)
                }
            )
        
        summary = response.text.strip() if response.text else ""
        
        # Validate and sanitize
        is_valid, errors = SummaryValidator.validate(summary)
        if not is_valid:
            print(f"  ! Summary issues: {', '.join(errors[:2])}")
            summary = SummaryValidator.sanitize(summary)
        
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
            cat_response = genai.GenerativeModel(MODEL).generate_content(
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
        except (json.JSONDecodeError, ValueError):
            report_type = 'Analysis'
            category = 'Global Threat Intelligence'
        
        result = {
            'type': report_type,
            'category': category,
            'summary': summary,
            'ai_processed': True
        }
        
        # Cache the result
        cache.set(content, org, year, result)
        
        return result
        
    except Exception as e:
        print(f"  ! AI failed: {str(e)[:50]}")
        return {
            'type': 'Analysis',
            'category': 'Global Threat Intelligence',
            'summary': f"Analyzes security findings from {org} for {year}.",
            'ai_processed': False
        }

# ==========================
# FALLBACK ANALYSIS
# ==========================
def fallback_analysis(content: str, org: str, year: str, title: str) -> Dict[str, Any]:
    """Simple fallback when AI unavailable."""
    sentences = [s.strip() for s in content.split('.') if len(s.strip()) > 20][:2]
    summary = '. '.join(sentences) if sentences else f"Security report from {org}"
    
    if not summary.endswith('.'):
        summary += '.'
    
    summary = SummaryValidator.sanitize(summary)
    
    # Simple categorization
    content_lower = content.lower()
    if 'survey' in title.lower():
        report_type = 'Survey'
        category = 'Industry Trends'
    else:
        report_type = 'Analysis'
        if 'cloud' in content_lower:
            category = 'Cloud Security'
        elif 'threat' in content_lower:
            category = 'Global Threat Intelligence'
        else:
            category = 'Global Threat Intelligence'
    
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
    parser.add_argument("conversions_json")
    parser.add_argument("--output-json", default="analysis.json")
    args = parser.parse_args()
    
    # Validate input
    if not os.path.exists(args.conversions_json):
        print(f"ERROR: Conversions file not found")
        sys.exit(1)
    
    # Setup AI
    gemini_key = os.environ.get("GEMINI_API_KEY")
    ai_available = False
    cache = AnalysisCache()
    
    if gemini_key:
        ai_available = setup_gemini(gemini_key)
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
    
    print(f"\n{'='*70}")
    print(f"Report Analyzer - {len(conversions)} conversions")
    print(f"{'='*70}\n")
    
    results = []
    current_year = datetime.now().year
    api_calls = 0
    
    for i, conv in enumerate(conversions, 1):
        if conv['status'] != 'success':
            continue
        
        try:
            output_path = conv.get('output_path')
            if not output_path or not os.path.exists(output_path):
                continue
            
            with open(output_path, 'r') as f:
                content = f.read()
            
            if not content.strip():
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
                    print(f"[{i}/{len(conversions)}] {org_name} - OLD ({year})")
                    continue
            except ValueError:
                pass
            
            print(f"[{i}/{len(conversions)}] {org_name} ({year})")
            
            # Analyze
            if ai_available and MODEL:
                analysis = analyze_with_ai(content, org_name, year, report_title, cache)
                if analysis['ai_processed']:
                    api_calls += 1
            else:
                analysis = fallback_analysis(content, org_name, year, report_title)
            
            # Construct URLs
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
                'report_url': report_url,
                'organization_url': org_url,
                'file_path': output_path,
                'ai_processed': analysis['ai_processed']
            }
            
            results.append(result)
            print(f"  ✓ {analysis['type']}/{analysis['category']}")
            
        except Exception as e:
            print(f"[{i}/{len(conversions)}] ERROR: {str(e)[:50]}")
            continue
    
    # Save
    with open(args.output_json, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n{'='*70}")
    print(f"SUMMARY")
    print(f"{'='*70}")
    print(f"Analyzed: {len(results)}/{len(conversions)}")
    
    ai_count = len([r for r in results if r['ai_processed']])
    print(f"AI: {ai_count} | Fallback: {len(results) - ai_count}")
    
    if ai_available:
        print(f"API Calls: {api_calls} (saved {cache.hits} via cache)")
        print(cache.stats())
    
    print(f"\n✓ Saved to: {args.output_json}")
    
    return 0 if results else 1

if __name__ == "__main__":
    sys.exit(main())