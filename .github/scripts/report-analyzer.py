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
    USE_NEW_SDK = False

# ==========================
# CONFIGURATION LOADER
# ==========================
class ConfigLoader:
    """Loads ALL config from .github/artifacts/"""
    
    def __init__(self, artifacts_dir: str = ".github/artifacts"):
        self.artifacts_dir = Path(artifacts_dir)
        
        self.ai_config = self._load_json("ai-models.json")
        self.pipeline_config = self._load_json("pipeline-config.json")
        self.categories_config = self._load_json("report-categories.json")
        
        if not self.ai_config:
            raise ValueError("ai-models.json is REQUIRED")
        if not self.pipeline_config:
            raise ValueError("pipeline-config.json is REQUIRED")
        if not self.categories_config:
            raise ValueError("report-categories.json is REQUIRED")
        
        self.models = self.ai_config.get("models", {}).get("priority_list", [])
        if not self.models:
            raise ValueError("No models in ai-models.json")
        
        self.gen_config = self.ai_config.get("configurations", {}).get("default", {})
        if not self.gen_config:
            raise ValueError("No default config in ai-models.json")
        
        proc_config = self.pipeline_config.get("processing", {})
        self.age_threshold = proc_config.get("age_threshold_years")
        if self.age_threshold is None:
            raise ValueError("age_threshold_years not in pipeline-config.json")
        
        self.org_mappings = self.pipeline_config.get("organization_mappings", {})
        
        prompts = self.pipeline_config.get("prompts", {})
        self.summary_prompt_path = prompts.get("summarization")
        self.cat_prompt_path = prompts.get("categorization")
        
        if not self.summary_prompt_path or not self.cat_prompt_path:
            raise ValueError("Prompt paths not in pipeline-config.json")
    
    def _load_json(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load JSON."""
        path = self.artifacts_dir / filename
        if not path.exists():
            print(f"ERROR: {filename} not found")
            return None
        
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid JSON in {filename}: {e}")
            return None

# ==========================
# ANALYSIS CACHE
# ==========================
class AnalysisCache:
    """Persistent cache to minimize API calls."""
    
    def __init__(self, cache_file: str = "analysis_cache.json"):
        self.cache_file = Path(cache_file)
        self.cache = self._load()
        self.hits = 0
        self.misses = 0
    
    def _load(self) -> Dict[str, Any]:
        """Load cache."""
        if self.cache_file.exists():
            try:
                with open(self.cache_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def _save(self):
        """Save cache."""
        try:
            with open(self.cache_file, 'w') as f:
                json.dump(self.cache, f, indent=2)
        except:
            pass
    
    def _hash(self, content: str, org: str, year: str) -> str:
        """Generate hash."""
        key = f"{org}:{year}:{content[:1000]}"
        return hashlib.md5(key.encode()).hexdigest()
    
    def get(self, content: str, org: str, year: str) -> Optional[Dict[str, Any]]:
        """Get cached."""
        cache_key = self._hash(content, org, year)
        if cache_key in self.cache:
            self.hits += 1
            return self.cache[cache_key]
        self.misses += 1
        return None
    
    def set(self, content: str, org: str, year: str, analysis: Dict[str, Any]):
        """Cache result."""
        cache_key = self._hash(content, org, year)
        self.cache[cache_key] = analysis
        self._save()
    
    def stats(self) -> str:
        """Stats."""
        total = self.hits + self.misses
        rate = (self.hits / total * 100) if total > 0 else 0
        return f"{self.hits} hits, {self.misses} misses ({rate:.1f}% hit rate)"

# ==========================
# AI SETUP
# ==========================
def setup_gemini(api_key: str, config: ConfigLoader) -> Tuple[bool, Optional[str]]:
    """Setup Gemini."""
    
    if USE_NEW_SDK:
        client = genai.Client(api_key=api_key)
        for model_name in config.models:
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents="test"
                )
                if response.text:
                    print(f"✓ Model: {model_name}")
                    return True, model_name
            except Exception:
                continue
    else:
        genai.configure(api_key=api_key)
        for model_name in config.models:
            try:
                test_model = genai.GenerativeModel(model_name)
                test_response = test_model.count_tokens("test")
                if test_response.total_tokens:
                    print(f"✓ Model: {model_name}")
                    return True, model_name
            except Exception:
                continue
    
    print("ERROR: No AI models available")
    return False, None

# ==========================
# SUMMARY VALIDATOR
# ==========================
class SummaryValidator:
    """Validates summaries."""
    
    REQUIRED_VERBS = [
        'analyzes', 'examines', 'evaluates', 'assesses', 'reviews',
        'interprets', 'dissects', 'deconstructs', 'scrutinizes',
        'compares', 'investigates', 'explores', 'probes', 'surveys',
        'inquires', 'studies', 'documents', 'traces', 'maps',
        'highlights', 'focuses', 'provides', 'offers', 'outlines'
    ]
    
    @classmethod
    def sanitize(cls, summary: str) -> str:
        """Fix issues."""
        if not summary:
            return ""
        
        summary = ' '.join(summary.split())
        summary = re.sub(r'[()"\']', '', summary)
        
        if summary and not summary.endswith('.'):
            summary += '.'
        
        if len(summary) > 400:
            sentences = summary.split('. ')
            summary = ''
            for s in sentences:
                if len(summary + s + '. ') <= 400:
                    summary += s + '. '
                else:
                    break
        
        return summary.strip()

# ==========================
# URL CONSTRUCTORS
# ==========================
def construct_report_url(pdf_path: str, year: str) -> str:
    """Construct Annual%20Security URL."""
    pdf_name = Path(pdf_path).name
    encoded = pdf_name.replace(' ', '%20')
    return f"Annual%20Security%20Reports/{year}/{encoded}"

def construct_org_url(org_name: str, search_url: Optional[str] = None) -> str:
    """Construct org URL."""
    if search_url and 'google.com/search' not in search_url:
        return search_url
    
    clean = ''.join(c for c in org_name if c.isalnum()).lower()
    return f"https://www.{clean}.com"

# ==========================
# CATEGORY LOADER
# ==========================
def load_categories(config: ConfigLoader) -> Dict[str, List[str]]:
    """Load categories."""
    categories = {"Analysis": [], "Survey": []}
    
    for parent_cat in config.categories_config.get("categories", []):
        parent_name = parent_cat["parent"].replace(" Reports", "")
        for sub_cat in parent_cat.get("sub_categories", []):
            categories[parent_name].append(sub_cat["name"])
    
    return categories

# ==========================
# AI ANALYSIS
# ==========================
def analyze_with_ai(content: str, org: str, year: str, title: str, 
                   config: ConfigLoader, model: str, cache: AnalysisCache) -> Dict[str, Any]:
    """Analyze with AI."""
    
    # Check cache FIRST
    cached = cache.get(content, org, year)
    if cached:
        print(f"  ✓ Cached")
        return cached
    
    try:
        # Load prompts
        if not os.path.exists(config.summary_prompt_path):
            raise FileNotFoundError(f"Prompt not found: {config.summary_prompt_path}")
        
        with open(config.summary_prompt_path, 'r') as f:
            summary_prompt = f.read()
        
        # Clean content
        clean = re.sub(r'!\[.*?\]\(.*?\)', '', content, flags=re.DOTALL)
        truncated = clean[:20000] if len(clean) > 20000 else clean
        
        full_prompt = f"{summary_prompt}\n\nOrg: {org}\nTitle: {title}\nYear: {year}\n\n{truncated}"
        
        # Generate summary
        if USE_NEW_SDK:
            client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
            gen_config = types.GenerateContentConfig(
                temperature=config.gen_config.get("temperature", 0.7),
                top_p=config.gen_config.get("top_p", 0.95),
                top_k=config.gen_config.get("top_k", 64),
                max_output_tokens=min(config.gen_config.get("max_output_tokens", 200), 200)
            )
            response = client.models.generate_content(
                model=model,
                contents=full_prompt,
                config=gen_config
            )
        else:
            response = genai.GenerativeModel(model).generate_content(
                full_prompt,
                generation_config={
                    "temperature": config.gen_config.get("temperature", 0.7),
                    "top_p": config.gen_config.get("top_p", 0.95),
                    "top_k": config.gen_config.get("top_k", 64),
                    "max_output_tokens": min(config.gen_config.get("max_output_tokens", 200), 200)
                }
            )
        
        summary = response.text.strip() if response.text else ""
        summary = SummaryValidator.sanitize(summary)
        
        # Categorization
        if not os.path.exists(config.cat_prompt_path):
            raise FileNotFoundError(f"Prompt not found: {config.cat_prompt_path}")
        
        with open(config.cat_prompt_path, 'r') as f:
            cat_prompt = f.read()
        
        categories = load_categories(config)
        cat_list = '\n'.join([f"- {cat}" for cats in categories.values() for cat in cats])
        cat_prompt = cat_prompt.replace("{{CATEGORIES}}", cat_list)
        
        cat_content = clean[:12000] if len(clean) > 12000 else clean
        full_cat = f"{cat_prompt}\n\nOrg: {org}\nTitle: {title}\nYear: {year}\n\n{cat_content}"
        
        if USE_NEW_SDK:
            cat_response = client.models.generate_content(
                model=model,
                contents=full_cat,
                config=types.GenerateContentConfig(temperature=0.1, max_output_tokens=100)
            )
        else:
            cat_response = genai.GenerativeModel(model).generate_content(
                full_cat,
                generation_config={"temperature": 0.1, "max_output_tokens": 100}
            )
        
        # Parse
        try:
            text = cat_response.text.strip().replace('```json', '').replace('```', '').strip()
            classification = json.loads(text)
            report_type = classification.get('type', 'Analysis')
            category = classification.get('category', 'Global Threat Intelligence')
        except:
            report_type = 'Analysis'
            category = 'Global Threat Intelligence'
        
        result = {
            'type': report_type,
            'category': category,
            'summary': summary,
            'ai_processed': True
        }
        
        # Cache
        cache.set(content, org, year, result)
        
        return result
        
    except Exception as e:
        print(f"  ! AI error: {str(e)[:50]}")
        raise

# ==========================
# MAIN
# ==========================
def main():
    parser = argparse.ArgumentParser(description="Report Analyzer - Production")
    parser.add_argument("conversions_json")
    parser.add_argument("--output-json", default="analysis.json")
    parser.add_argument("--artifacts-dir", default=".github/artifacts")
    args = parser.parse_args()
    
    print(f"\n{'='*70}")
    print(f"Report Analyzer")
    print(f"{'='*70}\n")
    
    try:
        config = ConfigLoader(args.artifacts_dir)
        print(f"✓ Config loaded")
        print(f"  Models: {', '.join(config.models[:2])}...")
        print(f"  Temp: {config.gen_config.get('temperature')}")
    except Exception as e:
        print(f"ERROR: Config failed: {e}")
        sys.exit(1)
    
    gemini_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_key:
        print("ERROR: GEMINI_API_KEY not set")
        sys.exit(1)
    
    ai_ok, model = setup_gemini(gemini_key, config)
    if not ai_ok:
        print("ERROR: AI setup failed")
        sys.exit(1)
    
    cache = AnalysisCache()
    
    if not os.path.exists(args.conversions_json):
        print(f"ERROR: File not found: {args.conversions_json}")
        sys.exit(1)
    
    with open(args.conversions_json, 'r') as f:
        conversions = json.load(f)
    
    if not conversions:
        print("No conversions")
        with open(args.output_json, 'w') as f:
            json.dump([], f)
        sys.exit(0)
    
    print(f"✓ {len(conversions)} conversions\n")
    
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
            
            pdf_path = conv.get('pdf_path', '')
            org_name = conv.get('organization_name', 'Unknown')
            report_title = conv.get('report_title', 'Security Report')
            
            org_name = config.org_mappings.get(org_name, org_name)
            
            year = str(current_year)
            for part in Path(pdf_path).parts:
                if part.isdigit() and len(part) == 4 and part.startswith("20"):
                    year = part
                    break
            
            if int(year) < (current_year - config.age_threshold):
                print(f"[{i}/{len(conversions)}] {org_name} - OLD ({year})")
                continue
            
            print(f"[{i}/{len(conversions)}] {org_name} ({year})")
            
            analysis = analyze_with_ai(content, org_name, year, report_title, config, model, cache)
            if analysis['ai_processed'] and cache.misses > cache.hits:
                api_calls += 1
            
            report_url = construct_report_url(pdf_path, year)
            org_url = construct_org_url(org_name, conv.get('organization_url'))
            
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
    
    with open(args.output_json, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n{'='*70}")
    print(f"Processed: {len(results)}/{len(conversions)}")
    print(f"API calls: {api_calls}")
    print(f"Cache: {cache.stats()}")
    print(f"\n✓ Saved: {args.output_json}")
    
    return 0 if results else 1

if __name__ == "__main__":
    sys.exit(main())