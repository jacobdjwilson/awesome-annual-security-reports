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

# ==========================
# DEPENDENCY CHECKS
# ==========================
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
    """Loads and validates all configuration files from .github/artifacts/"""

    # Prompt paths relative to the repo root
    SUMMARY_PROMPT_PATH = ".github/ai-prompts/markdown-summarization-prompt.md"
    CAT_PROMPT_PATH = ".github/ai-prompts/report-categorization-prompt.md"

    def __init__(self, artifacts_dir: str = ".github/artifacts"):
        self.artifacts_dir = Path(artifacts_dir)

        self.ai_config = self._load_json("ai-models.json")
        self.categories_config = self._load_json("report-categories.json")
        self.readme_config = self._load_json("readme-updater-config.json")

        if not self.ai_config:
            raise ValueError("ai-models.json is required")
        if not self.categories_config:
            raise ValueError("report-categories.json is required")

        # AI model names
        models = self.ai_config.get("models", {})
        self.primary_model: str = models.get("primary", "gemini-2.5-flash")
        self.secondary_model: str = models.get("secondary", "gemini-2.5-flash")

        # Generation config defaults
        self.gen_config: Dict[str, Any] = (
            self.ai_config.get("configurations", {}).get("default", {})
        )

        # Retry / rate-limit policy
        retry = self.ai_config.get("retry_policy", {})
        self.max_retries: int = retry.get("max_attempts", 3)
        self.initial_delay: float = retry.get("initial_delay_seconds", 1)
        self.backoff_mult: float = retry.get("backoff_multiplier", 2)

        # Summary validation rules from readme-updater-config
        if self.readme_config:
            val = self.readme_config.get("validation", {}).get("summary", {})
            self.min_length: int = val.get("min_length", 40)
            self.max_length: int = val.get("max_length", 400)
            self.required_verbs: List[str] = [v.lower() for v in val.get("required_verbs", [])]
            self.forbidden_phrases: List[str] = [p.lower() for p in val.get("forbidden_phrases", [])]
            self.marketing_words: List[str] = [w.lower() for w in val.get("marketing_words", [])]
        else:
            self.min_length = 40
            self.max_length = 400
            self.required_verbs = []
            self.forbidden_phrases = []
            self.marketing_words = []

    def _load_json(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load and parse a JSON config file."""
        path = self.artifacts_dir / filename
        if not path.exists():
            print(f"WARNING: {filename} not found at {path}")
            return None
        try:
            with open(path, "r", encoding="utf-8") as f:
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
        if self.cache_file.exists():
            try:
                with open(self.cache_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def _save(self):
        try:
            with open(self.cache_file, "w", encoding="utf-8") as f:
                json.dump(self.cache, f, indent=2)
        except Exception as e:
            print(f"WARNING: Could not save cache: {e}")

    def _key(self, content: str, org: str, year: str) -> str:
        raw = f"{org}:{year}:{content[:1000]}"
        return hashlib.md5(raw.encode()).hexdigest()

    def get(self, content: str, org: str, year: str) -> Optional[Dict[str, Any]]:
        key = self._key(content, org, year)
        if key in self.cache:
            self.hits += 1
            return self.cache[key]
        self.misses += 1
        return None

    def set(self, content: str, org: str, year: str, result: Dict[str, Any]):
        self.cache[self._key(content, org, year)] = result
        self._save()

    def stats(self) -> str:
        total = self.hits + self.misses
        rate = (self.hits / total * 100) if total > 0 else 0
        return f"Cache: {self.hits} hits, {self.misses} misses ({rate:.1f}% hit rate)"


# ====================
# SUMMARY VALIDATOR
# ====================
class SummaryValidator:
    """Validates AI-generated summaries against quality standards from config."""

    def __init__(self, config: ConfigLoader):
        self.min_words = config.min_length
        self.max_words = config.max_length
        self.required_verbs = config.required_verbs
        self.forbidden_phrases = config.forbidden_phrases
        self.marketing_words = config.marketing_words

    @staticmethod
    def sanitize(text: str) -> str:
        """Clean and normalize summary text."""
        text = re.sub(r"\s+", " ", text).strip()
        text = re.sub(r"\*\*?(.*?)\*\*?", r"\1", text)   # Bold
        text = re.sub(r"`(.*?)`", r"\1", text)             # Code spans
        text = re.sub(r"\([^)]*\)", "", text)               # Parenthesised content
        text = text.replace('"', "")
        text = re.sub(r"\s+([.,;:])", r"\1", text)
        text = re.sub(r"([.,;:])\s*([.,;:])", r"\1", text)
        text = re.sub(r"\.{2,}", ".", text)
        return text.strip()

    def validate(self, summary: str, org: str = "") -> Tuple[bool, List[str]]:
        """
        Validate a summary against all quality requirements.
        Returns (is_valid, errors).
        """
        errors: List[str] = []

        if not summary:
            return False, ["Summary is empty"]

        words = summary.split()
        word_count = len(words)

        if word_count < self.min_words:
            errors.append(f"Too short: {word_count} words (minimum {self.min_words})")
        if word_count > self.max_words:
            errors.append(f"Too long: {word_count} words (maximum {self.max_words})")

        first_word = words[0].lower() if words else ""
        if self.required_verbs and first_word not in self.required_verbs:
            errors.append(f"Must start with an approved verb, got: '{words[0]}'")

        summary_lower = summary.lower()
        for phrase in self.forbidden_phrases:
            if phrase in summary_lower:
                errors.append(f"Contains forbidden phrase: '{phrase}'")
        for word in self.marketing_words:
            if word in summary_lower:
                errors.append(f"Contains marketing word: '{word}'")

        numbers = re.findall(r"\b\d+%?\b", summary)
        if len(numbers) < 2:
            errors.append(f"Needs more data points (found {len(numbers)}, need 2+)")

        generic_phrases = [
            "provides insights", "offers recommendations",
            "highlights key", "discusses various", "explores different",
        ]
        for phrase in generic_phrases:
            if phrase in summary_lower:
                errors.append(f"Too generic: '{phrase}'")

        return len(errors) == 0, errors

    def format_errors(self, errors: List[str], summary: str, org: str) -> str:
        msg = f"\n{'='*70}\nVALIDATION FAILED: {org}\n{'='*70}\n"
        for error in errors:
            msg += f"  ❌ {error}\n"
        msg += f"\nGenerated summary:\n  {summary}\n{'='*70}\n"
        return msg


# ====================
# CATEGORY BUILDER
# ====================
class CategoryBuilder:
    """
    Reads report-categories.json and produces structured text for AI prompts
    that clearly shows the type → sub-category → definition hierarchy.

    This prevents the AI from confusing Analysis and Survey sub-categories
    that share the same name (e.g. 'Application Security', 'Cloud Security',
    'Ransomware' exist under both parent types).
    """

    def __init__(self, categories_config: Dict[str, Any]):
        self.config = categories_config

    def build_prompt_section(self) -> str:
        """
        Returns a formatted string listing every sub-category under its parent
        type, with definitions. This is injected into the {{CATEGORIES}}
        placeholder in the categorization prompt.

        Format:
            ## Analysis Reports
            (description of Analysis Reports)
            - Global Threat Intelligence: Broad-scale analysis...
            - Cloud Security: Analysis of threats, misconfigurations...

            ## Survey Reports
            (description of Survey Reports)
            - Industry Trends: Broad-market sentiment...
            - Cloud Security: Industry sentiment and organizational challenges...
        """
        lines: List[str] = []
        for group in self.config.get("categories", []):
            parent = group.get("parent", "")
            description = group.get("description", "")
            lines.append(f"\n## {parent}")
            if description:
                lines.append(f"({description})")
            for sub in group.get("sub_categories", []):
                name = sub.get("name", "")
                definition = sub.get("definition", "")
                lines.append(f"- {name}: {definition}")
        return "\n".join(lines)

    def all_valid_category_names(self) -> List[str]:
        """Return every sub-category name (original casing) across all parent types."""
        names: List[str] = []
        for group in self.config.get("categories", []):
            for sub in group.get("sub_categories", []):
                name = sub.get("name", "")
                if name:
                    names.append(name)
        return names

    def get_parent_for_category(self, category_name: str, report_type: str) -> str:
        """
        Given a sub-category name and the report type ('Analysis' or 'Survey'),
        return the correct parent header string from report-categories.json.

        Example: get_parent_for_category("Cloud Security", "Survey")
                 → "Survey Reports"
        """
        name_lower = category_name.lower()
        type_lower = report_type.lower()

        # First pass: exact match within the correct parent type
        for group in self.config.get("categories", []):
            parent = group.get("parent", "")
            if type_lower in parent.lower():
                for sub in group.get("sub_categories", []):
                    if sub.get("name", "").lower() == name_lower:
                        return parent

        # Second pass: any group containing the category (type mismatch fallback)
        for group in self.config.get("categories", []):
            parent = group.get("parent", "")
            for sub in group.get("sub_categories", []):
                if sub.get("name", "").lower() == name_lower:
                    return parent

        # Final fallback: first group whose parent matches the type keyword
        for group in self.config.get("categories", []):
            if type_lower in group.get("parent", "").lower():
                return group["parent"]

        return "Analysis Reports"


# ====================
# AI ANALYZER
# ====================
class AIAnalyzer:
    """Handles AI interactions with retry logic and summary validation."""

    def __init__(self, config: ConfigLoader, cache: AnalysisCache):
        self.config = config
        self.cache = cache
        self.validator = SummaryValidator(config)
        self.cat_builder = CategoryBuilder(config.categories_config)

        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is required")

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
    ) -> Dict[str, Any]:
        """
        Analyze a report with retry logic and validation.
        Returns dict with summary, type, category, parent_section, ai_processed.
        """
        cached = self.cache.get(content, org, year)
        if cached:
            print(f"  ✓ Using cached analysis")
            return cached

        print(f"  → Generating analysis...")

        delay = self.config.initial_delay
        for attempt in range(self.config.max_retries):
            try:
                result = self._analyze_once(content, org, title, year, attempt + 1)
                is_valid, errors = self.validator.validate(result["summary"], org)

                if is_valid:
                    word_count = len(result["summary"].split())
                    print(f"  ✓ Summary valid ({word_count} words)")
                    print(f"  ✓ Type: {result['type']} | Category: {result['category']}")
                    print(f"  ✓ Section: {result['parent_section']}")
                    self.cache.set(content, org, year, result)
                    return result

                print(f"  ⚠ Attempt {attempt + 1}/{self.config.max_retries} validation failed:")
                for error in errors:
                    print(f"    - {error}")

                if attempt < self.config.max_retries - 1:
                    print(f"  → Retrying with stricter guidance...")
                    time.sleep(delay)
                    delay *= self.config.backoff_mult
                else:
                    print(self.validator.format_errors(errors, result["summary"], org))
                    print(f"  ⚠ All retries exhausted with invalid summary — using fallback result")
                    fallback = self._fallback_result(org, title, year)
                    fallback["type"]           = result.get("type", fallback["type"])
                    fallback["category"]       = result.get("category", fallback["category"])
                    fallback["parent_section"] = result.get("parent_section", fallback["parent_section"])
                    self.cache.set(content, org, year, fallback)
                    return fallback

            except Exception as e:
                print(f"  ⚠ Attempt {attempt + 1} error: {str(e)[:100]}")
                if attempt < self.config.max_retries - 1:
                    time.sleep(delay)
                    delay *= self.config.backoff_mult

        print(f"  ⚠ All retries exhausted — using fallback result")
        return self._fallback_result(org, title, year)

    def _analyze_once(
        self,
        content: str,
        org: str,
        title: str,
        year: str,
        attempt_num: int,
    ) -> Dict[str, Any]:
        """Single analysis attempt: generates summary then classification."""
        summary_prompt = self._load_prompt(self.config.SUMMARY_PROMPT_PATH)
        cat_prompt = self._load_prompt(self.config.CAT_PROMPT_PATH)

        clean_content = self._clean_content(content)

        # Escalating guidance on retries
        retry_guidance = ""
        if attempt_num > 1:
            retry_guidance = (
                "\n\nIMPORTANT: Previous attempt was rejected. YOU MUST:\n"
                "- Include at least 3 specific statistics or percentages\n"
                f"- Write between {self.config.min_length}–{self.config.max_length} words (count carefully)\n"
                "- Start with an approved verb (Analyzes, Examines, Surveys, etc.)\n"
                "- NO generic phrases like 'provides insights' or 'offers recommendations'\n"
                "- NO forbidden phrases like 'this report' or 'the report'\n"
            )

        summary_full_prompt = (
            f"{summary_prompt}\n\nOrganization: {org}\nReport Title: {title}\nYear: {year}"
            f"{retry_guidance}\n\nReport Content:\n{clean_content[:20000]}"
        )

        summary = self._generate_text(
            summary_full_prompt,
            self.config.primary_model,
            max_tokens=self.config.ai_config.get("configurations", {})
                .get("summarization", {}).get("max_output_tokens", 400),
            temperature=self.config.ai_config.get("configurations", {})
                .get("summarization", {}).get("temperature", 0.2),
        )
        summary = self.validator.sanitize(summary)

        # Categorization
        categories_section = self.cat_builder.build_prompt_section()

        cat_full_prompt = (
            f"{cat_prompt.replace('{{CATEGORIES}}', categories_section)}\n\n"
            f"Organization: {org}\nReport Title: {title}\nYear: {year}\n\n"
            f"Report Content:\n{clean_content[:12000]}"
        )

        cat_response = self._generate_text(
            cat_full_prompt,
            self.config.primary_model,
            max_tokens=self.config.ai_config.get("configurations", {})
                .get("categorization", {}).get("max_output_tokens", 100),
            temperature=self.config.ai_config.get("configurations", {})
                .get("categorization", {}).get("temperature", 0.1),
        )

        # Parse and validate classification
        report_type, category = self._parse_classification(cat_response, content, title)

        # Resolve the correct parent section header from config
        parent_section = self.cat_builder.get_parent_for_category(category, report_type)

        return {
            "summary": summary,
            "type": report_type,
            "category": category,
            "parent_section": parent_section,
            "ai_processed": True,
        }

    def _parse_classification(
        self, response: str, content: str, title: str
    ) -> Tuple[str, str]:
        """
        Extract type and category from the AI JSON response.
        Validates the category name against the full config list (case-insensitive).
        Falls back to keyword inference if JSON is malformed or category is unknown.
        """
        valid_names = {n.lower(): n for n in self.cat_builder.all_valid_category_names()}

        try:
            clean = response.strip().replace("```json", "").replace("```", "").strip()
            obj = json.loads(clean)
            raw_type = str(obj.get("type", "Analysis")).strip()
            raw_category = str(obj.get("category", "")).strip()

            # Normalize type to exactly "Analysis" or "Survey"
            report_type = "Survey" if "survey" in raw_type.lower() else "Analysis"

            # Accept only categories present in the config; recover correct casing
            if raw_category.lower() in valid_names:
                return report_type, valid_names[raw_category.lower()]

        except Exception:
            pass

        # Keyword fallback when AI response is unusable
        return "Analysis", self._infer_category(content, title)

    def _generate_text(
        self,
        prompt: str,
        model: str,
        max_tokens: int = 200,
        temperature: float = 0.2,
    ) -> str:
        """Generate text using the configured AI model, with secondary fallback."""
        try:
            if USE_NEW_SDK:
                response = self.client.models.generate_content(
                    model=model,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        temperature=temperature,
                        top_p=self.config.gen_config.get("top_p", 0.95),
                        top_k=self.config.gen_config.get("top_k", 40),
                        max_output_tokens=max_tokens,
                    ),
                )
            else:
                response = genai.GenerativeModel(model).generate_content(
                    prompt,
                    generation_config={
                        "temperature": temperature,
                        "top_p": self.config.gen_config.get("top_p", 0.95),
                        "top_k": self.config.gen_config.get("top_k", 40),
                        "max_output_tokens": max_tokens,
                    },
                )
            return response.text.strip() if response.text else ""

        except Exception:
            if model == self.config.primary_model and self.config.secondary_model != model:
                print(f"  ⚠ Primary model failed, trying secondary ({self.config.secondary_model})...")
                return self._generate_text(
                    prompt, self.config.secondary_model, max_tokens, temperature
                )
            raise

    def _load_prompt(self, prompt_path: str) -> str:
        """Load a prompt template from disk."""
        if not os.path.exists(prompt_path):
            raise FileNotFoundError(f"Prompt file not found: {prompt_path}")
        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read()

    def _clean_content(self, content: str) -> str:
        """Strip images, HTML, and excess whitespace from markdown content."""
        content = re.sub(r"!\[.*?\]\(.*?\)", "", content, flags=re.DOTALL)
        content = re.sub(r"<[^>]+>", "", content)
        content = re.sub(r"\n{3,}", "\n\n", content)
        content = re.sub(r" {2,}", " ", content)
        return content.strip()

    def _infer_category(self, content: str, title: str) -> str:
        """Keyword-based category fallback when AI classification fails."""
        text = (content + " " + title).lower()
        if any(w in text for w in ["ransomware", "extortion", "raas"]):
            return "Ransomware"
        if any(w in text for w in ["cloud", "iaas", "paas", "saas", "container", "kubernetes"]):
            return "Cloud Security"
        if any(w in text for w in ["identity", "iam", "authentication", "zero trust"]):
            return "Identity Security"
        if any(w in text for w in ["application", "appsec", "devsecops", "software supply"]):
            return "Application Security"
        if any(w in text for w in ["vulnerability", "cve", "patch", "exploit"]):
            return "Vulnerabilities"
        if any(w in text for w in ["breach", "data exfiltration", "leak"]):
            return "Data Breaches"
        if any(w in text for w in ["ai", "llm", "machine learning", "artificial intelligence"]):
            return "AI and Emerging Technologies"
        if any(w in text for w in ["ot", "ics", "scada", "industrial"]):
            return "Physical Security"
        return "Global Threat Intelligence"

    def _fallback_result(self, org: str, title: str, year: str) -> Dict[str, Any]:
        category = self._infer_category(title, title)
        parent = self.cat_builder.get_parent_for_category(category, "Analysis")
        return {
            "summary": (
                f"Analyzes security findings and threat trends reported by {org} for {year}, "
                f"examining key attack patterns, vulnerability data, and defensive recommendations."
            ),
            "type": "Analysis",
            "category": category,
            "parent_section": parent,
            "ai_processed": False,
        }


# ====================
# REPORT PROCESSOR
# ====================
def process_reports(conversions_json: str, output_json: str, config: ConfigLoader) -> int:
    """Load conversions.json, run AI analysis on each, write analysis.json."""

    if not os.path.exists(conversions_json):
        print(f"ERROR: {conversions_json} not found")
        return 1

    try:
        with open(conversions_json, "r", encoding="utf-8") as f:
            conversions = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in {conversions_json}: {e}")
        return 1

    if not conversions:
        print("No conversions to process")
        return 0

    successful = [c for c in conversions if c.get("status") == "success"]
    if not successful:
        print("No successful conversions to analyze")
        return 0

    print(f"✓ {len(successful)} successful conversion(s) to analyze\n")

    cache = AnalysisCache()
    analyzer = AIAnalyzer(config, cache)

    results: List[Dict[str, Any]] = []
    errors: List[str] = []

    for i, conv in enumerate(successful, 1):
        org = conv.get("organization_name", "Unknown")
        title = conv.get("report_title", "Unknown")
        year = conv.get("year", "Unknown")
        md_path = conv.get("output_path", "")
        pdf_path = conv.get("pdf_path", "")

        print(f"[{i}/{len(successful)}] {org} ({year})")

        if not os.path.exists(md_path):
            print(f"  ✗ Markdown not found: {md_path}")
            errors.append(f"{org}: Markdown file missing")
            continue

        try:
            content = Path(md_path).read_text(encoding="utf-8")
        except Exception as e:
            print(f"  ✗ Could not read markdown: {e}")
            errors.append(f"{org}: Read error")
            continue

        try:
            analysis = analyzer.analyze(content, org, title, year)

            # Build a best-guess org URL: strip non-alphanumeric chars from org name.
            # Prefer organization_url if the converter already resolved it.
            org_slug = re.sub(r"[^a-z0-9]", "", org.lower())
            org_url = conv.get("organization_url") or f"https://www.{org_slug}.com"

            results.append({
                "organization": org,
                "title": title,
                "year": year,
                "summary": analysis["summary"],
                "type": analysis["type"],
                "category": analysis["category"],
                "parent_section": analysis["parent_section"],
                "pdf_path": pdf_path,
                "organization_url": org_url,
                "file_path": md_path,
                "model": config.primary_model,
                "ai_processed": analysis["ai_processed"],
            })
            print(f"  ✓ Complete\n")

        except Exception as e:
            print(f"  ✗ Analysis failed: {str(e)[:100]}")
            errors.append(f"{org}: {str(e)[:80]}")

    if results:
        try:
            with open(output_json, "w", encoding="utf-8") as f:
                json.dump(results, f, indent=2)
            print(f"\n{'='*70}")
            print(f"✓ Saved {len(results)} result(s) to {output_json}")
        except Exception as e:
            print(f"ERROR: Could not save {output_json}: {e}")
            return 1
    else:
        print(f"\n{'='*70}")
        print("WARNING: No results to save")

    print(f"\n{cache.stats()}")
    print(f"Success: {len(results)}/{len(successful)}")

    if errors:
        print(f"\nErrors ({len(errors)}):")
        for err in errors:
            print(f"  - {err}")

    print(f"{'='*70}\n")
    return 0 if results else 1


# ====================
# MAIN
# ====================
def main():
    parser = argparse.ArgumentParser(description="Report Analyzer")
    parser.add_argument("conversions_json", help="Path to conversions.json")
    parser.add_argument("--output-json", default="analysis.json")
    parser.add_argument("--artifacts-dir", default=".github/artifacts")
    args = parser.parse_args()

    print(f"\n{'='*70}")
    print(f"Report Analyzer")
    print(f"{'='*70}\n")

    try:
        config = ConfigLoader(args.artifacts_dir)
        print(f"✓ Config loaded\n")
        return process_reports(args.conversions_json, args.output_json, config)
    except Exception as e:
        print(f"\nFATAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())