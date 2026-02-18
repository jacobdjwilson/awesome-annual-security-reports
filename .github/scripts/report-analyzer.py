import os
import sys
import json
import re
import argparse
import time
from typing import Dict, Any, Optional, List, Tuple
from pathlib import Path
from datetime import datetime
import hashlib

# Dual SDK support
try:
    from google import genai
    from google.genai import types
    USE_NEW_SDK = True
except ImportError:
    try:
        import google.generativeai as genai
        USE_NEW_SDK = False
    except ImportError:
        print("ERROR: google-generativeai package required")
        print("Install: pip install google-generativeai")
        sys.exit(1)

# ====================
# CONFIGURATION LOADER
# ====================
class ConfigLoader:
    """Loads and validates all configuration files."""
    
    def __init__(self, artifacts_dir: str = ".github/artifacts"):
        self.artifacts_dir = Path(artifacts_dir)
        
        # Load all configs
        self.ai_config = self._load_json("ai-models.json")
        self.pipeline_config = self._load_json("pipeline-config.json")
        self.categories_config = self._load_json("report-categories.json")
        self.readme_config = self._load_json("readme-updater-config.json")
        
        # Validate required configs
        if not self.ai_config:
            raise ValueError("ai-models.json is REQUIRED")
        if not self.pipeline_config:
            raise ValueError("pipeline-config.json is REQUIRED")
        if not self.categories_config:
            raise ValueError("report-categories.json is REQUIRED")
        
        # Extract AI model configuration
        models = self.ai_config.get("models", {})
        self.primary_model = models.get("primary", "gemini-3-flash-preview")
        self.secondary_model = models.get("secondary", "gemini-2.5-flash")
        
        self.gen_config = self.ai_config.get("configurations", {}).get("default", {})
        
        # Extract processing configuration
        proc_config = self.pipeline_config.get("processing", {})
        self.age_threshold = proc_config.get("age_threshold_years", 2)
        self.org_mappings = self.pipeline_config.get("organization_mappings", {})
        
        # Extract prompt paths
        prompts = self.pipeline_config.get("prompts", {})
        self.summary_prompt_path = prompts.get("summarization")
        self.cat_prompt_path = prompts.get("categorization")
        
        if not self.summary_prompt_path or not self.cat_prompt_path:
            raise ValueError("Prompt paths not in pipeline-config.json")
        
        # Extract validation rules
        if self.readme_config:
            validation = self.readme_config.get("validation", {}).get("summary", {})
            self.min_length = validation.get("min_length", 40)
            self.max_length = validation.get("max_length", 400)
            self.required_verbs = validation.get("required_verbs", [])
            self.forbidden_phrases = validation.get("forbidden_phrases", [])
            self.marketing_words = validation.get("marketing_words", [])
        else:
            self.min_length = 40
            self.max_length = 400
            self.required_verbs = []
            self.forbidden_phrases = []
            self.marketing_words = []
    
    def _load_json(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load and parse JSON configuration file."""
        path = self.artifacts_dir / filename
        if not path.exists():
            print(f"WARNING: {filename} not found at {path}")
            return None
        
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid JSON in {filename}: {e}")
            return None
        except Exception as e:
            print(f"ERROR: Could not read {filename}: {e}")
            return None

# ================
# ANALYSIS CACHE
# ================
class AnalysisCache:
    """Caches AI analysis results to avoid redundant API calls."""
    
    def __init__(self, cache_file: str = ".analysis_cache.json"):
        self.cache_file = Path(cache_file)
        self.cache = self._load()
        self.hits = 0
        self.misses = 0
    
    def _load(self) -> Dict[str, Any]:
        """Load cache from disk."""
        if self.cache_file.exists():
            try:
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}
    
    def _save(self):
        """Save cache to disk."""
        try:
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(self.cache, f, indent=2)
        except Exception as e:
            print(f"WARNING: Could not save cache: {e}")
    
    def _hash(self, content: str, org: str, year: str) -> str:
        """Generate cache key from content."""
        key = f"{org}:{year}:{content[:1000]}"
        return hashlib.md5(key.encode()).hexdigest()
    
    def get(self, content: str, org: str, year: str) -> Optional[Dict[str, Any]]:
        """Retrieve cached analysis if available."""
        key = self._hash(content, org, year)
        if key in self.cache:
            self.hits += 1
            return self.cache[key]
        self.misses += 1
        return None
    
    def set(self, content: str, org: str, year: str, result: Dict[str, Any]):
        """Store analysis result in cache."""
        key = self._hash(content, org, year)
        self.cache[key] = result
        self._save()
    
    def stats(self) -> str:
        """Return cache statistics."""
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0
        return f"Cache: {self.hits} hits, {self.misses} misses ({hit_rate:.1f}% hit rate)"

# ====================
# SUMMARY VALIDATOR
# ====================
class SummaryValidator:
    """Validates AI-generated summaries against quality standards."""
    
    def __init__(self, config: ConfigLoader):
        self.min_words = config.min_length  # Min 40 words
        self.max_words = config.max_length  # Max 400 words (but really aim for 120)
        self.required_verbs = [v.lower() for v in config.required_verbs]
        self.forbidden_phrases = [p.lower() for p in config.forbidden_phrases]
        self.marketing_words = [w.lower() for w in config.marketing_words]
    
    @staticmethod
    def sanitize(text: str) -> str:
        """Clean and normalize summary text."""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Remove any markdown formatting that slipped through
        text = re.sub(r'\*\*?(.*?)\*\*?', r'\1', text)
        text = re.sub(r'`(.*?)`', r'\1', text)
        
        # Remove parentheses and their contents (per requirements)
        text = re.sub(r'\([^)]*\)', '', text)
        
        # Remove quotes
        text = text.replace('"', '').replace("'", "'")  # Keep apostrophes
        
        # Clean up punctuation
        text = re.sub(r'\s+([.,;:])', r'\1', text)
        text = re.sub(r'([.,;:])\s*([.,;:])', r'\1', text)
        
        # Remove multiple periods
        text = re.sub(r'\.{2,}', '.', text)
        
        return text.strip()
    
    def validate(self, summary: str, org: str = "") -> Tuple[bool, List[str]]:
        """
        Validate summary against all quality requirements.
        
        Returns:
            (is_valid, list_of_errors)
        """
        errors = []
        
        if not summary:
            errors.append("Summary is empty")
            return False, errors
        
        # Word count validation (CRITICAL)
        words = summary.split()
        word_count = len(words)
        
        if word_count < self.min_words:
            errors.append(f"Too short: {word_count} words (minimum {self.min_words})")
        
        if word_count > self.max_words:
            errors.append(f"Too long: {word_count} words (maximum {self.max_words})")
        
        # Check for required verb at start
        first_word = words[0].lower() if words else ""
        if self.required_verbs and first_word not in self.required_verbs:
            errors.append(f"Must start with approved verb, got: '{words[0]}'")
        
        # Check for forbidden phrases
        summary_lower = summary.lower()
        for phrase in self.forbidden_phrases:
            if phrase in summary_lower:
                errors.append(f"Contains forbidden phrase: '{phrase}'")
        
        # Check for marketing words
        for word in self.marketing_words:
            if word in summary_lower:
                errors.append(f"Contains marketing word: '{word}'")
        
        # Check for data/statistics (should have at least 2 numbers)
        numbers = re.findall(r'\b\d+%?\b', summary)
        if len(numbers) < 2:
            errors.append(f"Needs more data points (found {len(numbers)}, need 2+)")
        
        # Check for generic content
        generic_phrases = [
            "provides insights",
            "offers recommendations",
            "highlights key",
            "discusses various",
            "explores different"
        ]
        for phrase in generic_phrases:
            if phrase in summary_lower:
                errors.append(f"Too generic: '{phrase}'")
        
        is_valid = len(errors) == 0
        return is_valid, errors
    
    def format_errors(self, errors: List[str], summary: str, org: str) -> str:
        """Format validation errors for logging."""
        msg = f"\n{'='*70}\nVALIDATION FAILED: {org}\n{'='*70}\n"
        for error in errors:
            msg += f"  ❌ {error}\n"
        msg += f"\nGenerated summary:\n  {summary}\n"
        msg += f"{'='*70}\n"
        return msg

# ====================
# AI ANALYZER
# ====================
class AIAnalyzer:
    """Handles all AI interactions with retry logic and validation."""
    
    def __init__(self, config: ConfigLoader, cache: AnalysisCache):
        self.config = config
        self.cache = cache
        self.validator = SummaryValidator(config)
        
        # Initialize AI
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable required")
        
        if USE_NEW_SDK:
            self.client = genai.Client(api_key=api_key)
        else:
            genai.configure(api_key=api_key)
    
    def analyze(
        self,
        content: str,
        org: str,
        title: str,
        year: str,
        max_retries: int = 3
    ) -> Dict[str, Any]:
        """
        Analyze report with retry logic and validation.
        
        Args:
            content: Markdown content to analyze
            org: Organization name
            title: Report title
            year: Publication year
            max_retries: Maximum retry attempts for failed validations
            
        Returns:
            Dictionary with summary, type, category, ai_processed flag
        """
        # Check cache first
        cached = self.cache.get(content, org, year)
        if cached:
            print(f"  ✓ Using cached analysis")
            return cached
        
        print(f"  → Generating analysis...")
        
        # Try with retries
        for attempt in range(max_retries):
            try:
                result = self._analyze_once(content, org, title, year, attempt + 1)
                
                # Validate summary
                is_valid, errors = self.validator.validate(result['summary'], org)
                
                if is_valid:
                    print(f"  ✓ Analysis complete ({len(result['summary'].split())} words)")
                    self.cache.set(content, org, year, result)
                    return result
                else:
                    print(f"  ⚠ Attempt {attempt + 1}/{max_retries} validation failed:")
                    for error in errors:
                        print(f"    - {error}")
                    
                    if attempt < max_retries - 1:
                        print(f"  → Retrying with stricter guidance...")
                        time.sleep(1)  # Brief pause before retry
                    else:
                        print(self.validator.format_errors(errors, result['summary'], org))
                        raise ValueError(f"Failed validation after {max_retries} attempts")
            
            except Exception as e:
                if attempt < max_retries - 1:
                    print(f"  ⚠ Attempt {attempt + 1} error: {str(e)[:100]}")
                    time.sleep(2)
                else:
                    raise
        
        # Should never reach here, but provide fallback
        return self._fallback_result(org, title, year)
    
    def _analyze_once(
        self,
        content: str,
        org: str,
        title: str,
        year: str,
        attempt_num: int
    ) -> Dict[str, Any]:
        """Single analysis attempt."""
        
        # Load prompts
        summary_prompt = self._load_prompt(self.config.summary_prompt_path)
        cat_prompt = self._load_prompt(self.config.cat_prompt_path)
        
        # Clean and truncate content
        clean_content = self._clean_content(content)
        
        # Generate summary with increasing strictness on retries
        summary_content = clean_content[:20000]
        
        # Add retry-specific guidance
        retry_guidance = ""
        if attempt_num > 1:
            retry_guidance = f"\n\nIMPORTANT: Previous attempt was rejected. YOU MUST:\n"
            retry_guidance += f"- Include at least 3 specific statistics or percentages\n"
            retry_guidance += f"- Write between 40-120 words (count carefully)\n"
            retry_guidance += f"- Start with an approved verb (Analyzes, Examines, Surveys, etc.)\n"
            retry_guidance += f"- NO generic phrases like 'provides insights' or 'offers recommendations'\n"
            retry_guidance += f"- NO forbidden phrases like 'this report' or 'the report'\n"
        
        summary_full_prompt = f"{summary_prompt}\n\nOrganization: {org}\nReport Title: {title}\nYear: {year}{retry_guidance}\n\nReport Content:\n{summary_content}"
        
        summary = self._generate_text(
            summary_full_prompt,
            self.config.primary_model,
            max_tokens=400,  # Allow enough tokens for 120 words
            temperature=0.2  # Lower temperature for more focused output
        )
        
        summary = self.validator.sanitize(summary)
        
        # Generate categorization
        categories = self._load_categories()
        cat_list = '\n'.join([f"- {cat}" for cats in categories.values() for cat in cats])
        cat_prompt_filled = cat_prompt.replace("{{CATEGORIES}}", cat_list)
        
        cat_content = clean_content[:12000]
        cat_full_prompt = f"{cat_prompt_filled}\n\nOrganization: {org}\nReport Title: {title}\nYear: {year}\n\nReport Content:\n{cat_content}"
        
        cat_response = self._generate_text(
            cat_full_prompt,
            self.config.primary_model,
            max_tokens=100,
            temperature=0.1  # Very low for classification
        )
        
        # Parse categorization
        try:
            cat_text = cat_response.strip().replace('```json', '').replace('```', '').strip()
            classification = json.loads(cat_text)
            report_type = classification.get('type', 'Analysis')
            category = classification.get('category', 'Global Threat Intelligence')
        except Exception:
            # Fallback categorization
            report_type = 'Analysis'
            category = self._infer_category(content, title)
        
        return {
            'summary': summary,
            'type': report_type,
            'category': category,
            'ai_processed': True
        }
    
    def _generate_text(
        self,
        prompt: str,
        model: str,
        max_tokens: int = 200,
        temperature: float = 0.2
    ) -> str:
        """Generate text using AI model."""
        
        try:
            if USE_NEW_SDK:
                response = self.client.models.generate_content(
                    model=model,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        temperature=temperature,
                        top_p=self.config.gen_config.get("top_p", 0.95),
                        top_k=self.config.gen_config.get("top_k", 40),
                        max_output_tokens=max_tokens
                    )
                )
            else:
                response = genai.GenerativeModel(model).generate_content(
                    prompt,
                    generation_config={
                        "temperature": temperature,
                        "top_p": self.config.gen_config.get("top_p", 0.95),
                        "top_k": self.config.gen_config.get("top_k", 40),
                        "max_output_tokens": max_tokens
                    }
                )
            
            return response.text.strip() if response.text else ""
        
        except Exception as e:
            # Try secondary model if primary fails
            if model == self.config.primary_model:
                print(f"  ⚠ Primary model failed, trying secondary...")
                return self._generate_text(prompt, self.config.secondary_model, max_tokens, temperature)
            raise
    
    def _load_prompt(self, prompt_path: str) -> str:
        """Load prompt template from file."""
        if not os.path.exists(prompt_path):
            raise FileNotFoundError(f"Prompt file not found: {prompt_path}")
        
        with open(prompt_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def _clean_content(self, content: str) -> str:
        """Clean markdown content for AI processing."""
        # Remove images
        content = re.sub(r'!\[.*?\]\(.*?\)', '', content, flags=re.DOTALL)
        
        # Remove HTML tags
        content = re.sub(r'<[^>]+>', '', content)
        
        # Normalize whitespace
        content = re.sub(r'\n{3,}', '\n\n', content)
        content = re.sub(r' {2,}', ' ', content)
        
        return content.strip()
    
    def _load_categories(self) -> Dict[str, List[str]]:
        """Extract category names from config."""
        categories = {"Analysis": [], "Survey": []}
        
        for cat_group in self.config.categories_config.get("categories", []):
            parent = cat_group.get("parent", "")
            parent_type = "Analysis" if "Analysis" in parent else "Survey"
            
            for sub_cat in cat_group.get("sub_categories", []):
                cat_name = sub_cat.get("name", "")
                if cat_name and cat_name not in categories[parent_type]:
                    categories[parent_type].append(cat_name)
        
        return categories
    
    def _infer_category(self, content: str, title: str) -> str:
        """Infer category from content keywords when AI fails."""
        content_lower = (content + " " + title).lower()
        
        # Simple keyword matching
        if any(word in content_lower for word in ['ransomware', 'extortion', 'raas']):
            return 'Ransomware'
        elif any(word in content_lower for word in ['cloud', 'iaas', 'paas', 'saas', 'container', 'kubernetes']):
            return 'Cloud Security'
        elif any(word in content_lower for word in ['identity', 'iam', 'authentication', 'authorization', 'zero trust']):
            return 'Identity Security'
        elif any(word in content_lower for word in ['application', 'appsec', 'devsecops', 'code', 'software supply']):
            return 'Application Security'
        elif any(word in content_lower for word in ['vulnerability', 'cve', 'patch', 'exploit']):
            return 'Vulnerabilities'
        elif any(word in content_lower for word in ['breach', 'data exfiltration', 'leak']):
            return 'Data Breaches'
        elif any(word in content_lower for word in ['ai', 'llm', 'machine learning', 'artificial intelligence']):
            return 'AI and Emerging Technologies'
        elif any(word in content_lower for word in ['ot', 'ics', 'scada', 'industrial']):
            return 'Physical Security'
        else:
            return 'Global Threat Intelligence'
    
    def _fallback_result(self, org: str, title: str, year: str) -> Dict[str, Any]:
        """Generate fallback result when AI fails completely."""
        return {
            'summary': f"Analyzes security findings and trends from {org} for {year}, examining key threats and vulnerabilities.",
            'type': 'Analysis',
            'category': 'Global Threat Intelligence',
            'ai_processed': False
        }

# ====================
# REPORT PROCESSOR
# ====================
def process_reports(conversions_json: str, output_json: str, config: ConfigLoader) -> int:
    """Process all reports from conversions.json."""
    
    print(f"\n{'='*70}")
    print(f"Report Analyzer - Production")
    print(f"{'='*70}\n")
    
    # Load conversions
    if not os.path.exists(conversions_json):
        print(f"ERROR: {conversions_json} not found")
        return 1
    
    try:
        with open(conversions_json, 'r', encoding='utf-8') as f:
            conversions = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in {conversions_json}: {e}")
        return 1
    
    if not conversions:
        print("No conversions to process")
        return 0
    
    print(f"✓ Loaded {len(conversions)} conversion(s)\n")
    
    # Filter successful conversions
    successful = [c for c in conversions if c.get('status') == 'success']
    
    if not successful:
        print("No successful conversions to analyze")
        return 0
    
    print(f"✓ {len(successful)} successful conversion(s) to analyze\n")
    
    # Initialize analyzer and cache
    cache = AnalysisCache()
    analyzer = AIAnalyzer(config, cache)
    
    # Process each report
    results = []
    errors = []
    
    for i, conv in enumerate(successful, 1):
        org = conv.get('organization_name', 'Unknown')
        title = conv.get('report_title', 'Unknown')
        year = conv.get('year', 'Unknown')
        md_path = conv.get('output_path', '')
        pdf_path = conv.get('pdf_path', '')
        
        print(f"[{i}/{len(successful)}] {org} ({year})")
        
        # Read markdown content
        if not os.path.exists(md_path):
            print(f"  ✗ Markdown not found: {md_path}")
            errors.append(f"{org}: Markdown file missing")
            continue
        
        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"  ✗ Could not read markdown: {e}")
            errors.append(f"{org}: Read error")
            continue
        
        # Analyze with AI
        try:
            analysis = analyzer.analyze(content, org, title, year)
            
            # Build result
            result = {
                'organization': org,
                'title': title,
                'year': year,
                'summary': analysis['summary'],
                'type': analysis['type'],
                'category': analysis['category'],
                'pdf_path': pdf_path,
                'report_url': pdf_path.replace(' ', '%20'),
                'organization_url': f"https://www.{org.lower().replace(' ', '')}.com",
                'file_path': md_path,
                'ai_processed': analysis['ai_processed']
            }
            
            results.append(result)
            print(f"  ✓ Complete\n")
        
        except Exception as e:
            print(f"  ✗ Analysis failed: {str(e)[:100]}")
            errors.append(f"{org}: {str(e)[:50]}")
            continue
    
    # Save results
    if results:
        try:
            with open(output_json, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2)
            print(f"\n{'='*70}")
            print(f"✓ Saved {len(results)} analysis result(s) to {output_json}")
        except Exception as e:
            print(f"\nERROR: Could not save {output_json}: {e}")
            return 1
    else:
        print(f"\n{'='*70}")
        print("WARNING: No results to save")
    
    # Print statistics
    print(f"\n{cache.stats()}")
    print(f"Success: {len(results)}/{len(successful)}")
    
    if errors:
        print(f"\nErrors ({len(errors)}):")
        for error in errors:
            print(f"  - {error}")
    
    print(f"{'='*70}\n")
    
    return 0 if results else 1

# ====================
# MAIN
# ====================
def main():
    parser = argparse.ArgumentParser(description="Report Analyzer - Production")
    parser.add_argument("conversions_json", help="Path to conversions.json")
    parser.add_argument("--output-json", default="analysis.json", help="Output file")
    parser.add_argument("--artifacts-dir", default=".github/artifacts", help="Artifacts directory")
    
    args = parser.parse_args()
    
    try:
        config = ConfigLoader(args.artifacts_dir)
        return process_reports(args.conversions_json, args.output_json, config)
    except Exception as e:
        print(f"\nFATAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())