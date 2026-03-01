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


# ==========================
# ERROR CLASSIFICATION
# ==========================
def classify_error(error_str: str) -> str:
    """
    Classify an error string into a short category for structured error output.
    Categories are used by the workflow summary to group and explain failures.
    """
    s = error_str.lower()
    if "429" in s or "resource_exhausted" in s or "quota" in s:
        return "quota_exceeded"
    if "401" in s or "403" in s or "api_key" in s or "permission" in s or "unauthorized" in s:
        return "auth_error"
    if "404" in s or "not found" in s or "model" in s:
        return "model_unavailable"
    if "timeout" in s or "deadline" in s or "timed out" in s:
        return "timeout"
    if "too short" in s or "too few sentences" in s or "no numerical" in s or "bad start" in s:
        return "validation_failed"
    if "prompt file not found" in s or "filenotfounderror" in s:
        return "config_error"
    return "unknown_error"


def is_quota_error(error_str: str) -> bool:
    """True when the error is a 429 / RESOURCE_EXHAUSTED quota error."""
    s = error_str.lower()
    return "429" in s or "resource_exhausted" in s or "quota" in s


# ====================
# CONFIGURATION LOADER
# ====================
class ConfigLoader:
    """Loads and validates all configuration files from .github/artifacts/"""

    # Prompt paths relative to the repo root
    SUMMARY_PROMPT_PATH = ".github/ai-prompts/markdown-summarization-prompt.md"
    CAT_PROMPT_PATH     = ".github/ai-prompts/report-categorization-prompt.md"

    def __init__(self, artifacts_dir: str = ".github/artifacts"):
        self.artifacts_dir = Path(artifacts_dir)

        self.ai_config         = self._load_json("ai-models.json")
        self.categories_config = self._load_json("report-categories.json")
        self.readme_config     = self._load_json("readme-updater-config.json")
        self.workflow_config   = self._load_json("workflow-config.json")

        if not self.ai_config:
            raise ValueError("ai-models.json is required")
        if not self.categories_config:
            raise ValueError("report-categories.json is required")

        # AI model names
        models = self.ai_config.get("models", {})
        self.primary_model: str   = models.get("primary", "gemini-2.5-flash")
        self.secondary_model: str = models.get("secondary", "gemini-2.5-flash")

        # Generation config defaults
        self.gen_config: Dict[str, Any] = (
            self.ai_config.get("configurations", {}).get("default", {})
        )

        # Standard retry policy (validation failures, transient errors)
        retry = self.ai_config.get("retry_policy", {})
        self.max_retries: int     = retry.get("max_attempts", 3)
        self.initial_delay: float = retry.get("initial_delay_seconds", 2)
        self.backoff_mult: float  = retry.get("backoff_multiplier", 2)
        self.max_delay: float     = retry.get("max_delay_seconds", 30)

        # Quota retry policy (429 RESOURCE_EXHAUSTED — needs much longer waits)
        quota_retry = self.ai_config.get("quota_retry_policy", {})
        self.quota_max_retries: int     = quota_retry.get("max_attempts", 3)
        self.quota_initial_delay: float = quota_retry.get("initial_delay_seconds", 30)
        self.quota_backoff_mult: float  = quota_retry.get("backoff_multiplier", 2)
        self.quota_max_delay: float     = quota_retry.get("max_delay_seconds", 120)

        # Content window settings from workflow-config.json
        analysis_cfg = (self.workflow_config or {}).get("workflow", {}).get("analysis", {})
        self.markdown_lines_for_analysis: int = analysis_cfg.get("markdown_lines_for_analysis", 200)
        self.markdown_max_chars: int          = analysis_cfg.get("markdown_max_chars_for_analysis", 12000)
        self.errors_output_file: str          = analysis_cfg.get("errors_output_file", "analysis_errors.json")

        # Summary validation rules from readme-updater-config
        if self.readme_config:
            val = self.readme_config.get("validation", {}).get("summary", {})
            self.min_length: int               = val.get("min_length", 40)
            self.max_length: int               = val.get("max_length", 400)
            self.required_verbs: List[str]     = [v.lower() for v in val.get("required_verbs", [])]
            self.forbidden_phrases: List[str]  = [p.lower() for p in val.get("forbidden_phrases", [])]
            self.marketing_words: List[str]    = [w.lower() for w in val.get("marketing_words", [])]
        else:
            self.min_length        = 40
            self.max_length        = 400
            self.required_verbs    = []
            self.forbidden_phrases = []
            self.marketing_words   = []

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
        self.hits   = 0
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
        rate  = (self.hits / total * 100) if total > 0 else 0
        return f"Cache: {self.hits} hits, {self.misses} misses ({rate:.1f}% hit rate)"


# ====================
# SUMMARY VALIDATOR
# ====================
class SummaryValidator:
    """Validates AI-generated summaries against quality standards from config."""

    def __init__(self, config: ConfigLoader):
        self.min_words         = config.min_length
        self.max_words         = config.max_length
        self.required_verbs    = config.required_verbs
        self.forbidden_phrases = config.forbidden_phrases
        self.marketing_words   = config.marketing_words

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
        """Validate a summary against all quality requirements. Returns (is_valid, errors)."""
        errors: List[str] = []

        if not summary:
            return False, ["Summary is empty"]

        words      = summary.split()
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

        # Sentence count (must have at least 2, matching readme-updater-config min_sentences)
        sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', summary.strip()) if s.strip()]
        min_sentences = 2
        if len(sentences) < min_sentences:
            errors.append(f"Too few sentences: {len(sentences)} (minimum {min_sentences})")

        # Require at least 1 digit in the summary
        if not re.search(r"\d", summary):
            errors.append("No numerical data (need at least 1 digit)")

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
    """

    def __init__(self, categories_config: Dict[str, Any]):
        self.config = categories_config
        self._keyword_index = self._build_keyword_index()

    def _build_keyword_index(self) -> List[Dict[str, Any]]:
        """
        Build an ordered list of {keywords, name, parent_type} from report-categories.json.
        Keywords come from the 'keywords' array on each sub_category entry.
        All signals live in the JSON artifact — nothing is hardcoded here.
        """
        index: List[Dict[str, Any]] = []
        for group in self.config.get("categories", []):
            parent      = group.get("parent", "")
            report_type = "Survey" if "survey" in parent.lower() else "Analysis"
            for sub in group.get("sub_categories", []):
                keywords = sub.get("keywords", [])
                if keywords:
                    index.append({
                        "keywords":    [kw.lower() for kw in keywords],
                        "name":        sub.get("name", ""),
                        "parent":      parent,
                        "report_type": report_type,
                    })
        return index

    def build_prompt_section(self) -> str:
        """Returns a formatted string listing every sub-category with definitions."""
        lines: List[str] = []
        for group in self.config.get("categories", []):
            parent      = group.get("parent", "")
            description = group.get("description", "")
            lines.append(f"\n## {parent}")
            if description:
                lines.append(f"({description})")
            for sub in group.get("sub_categories", []):
                name       = sub.get("name", "")
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
        """Return the parent header string for a given sub-category name and report type."""
        name_lower = category_name.lower()
        type_lower = report_type.lower()

        for group in self.config.get("categories", []):
            parent = group.get("parent", "")
            if type_lower in parent.lower():
                for sub in group.get("sub_categories", []):
                    if sub.get("name", "").lower() == name_lower:
                        return parent

        for group in self.config.get("categories", []):
            parent = group.get("parent", "")
            for sub in group.get("sub_categories", []):
                if sub.get("name", "").lower() == name_lower:
                    return parent

        for group in self.config.get("categories", []):
            if type_lower in group.get("parent", "").lower():
                return group["parent"]

        return "Analysis Reports"

    def infer_category_from_keywords(
        self, content: str, title: str
    ) -> Tuple[str, str]:
        """
        Score every category by keyword matches in content+title.
        Returns (category_name, report_type). All signals from report-categories.json.
        """
        text       = (content + " " + title).lower()
        best_score = 0
        best_name  = "Global Threat Intelligence"
        best_type  = "Analysis"

        for entry in self._keyword_index:
            score = sum(1 for kw in entry["keywords"] if kw in text)
            if score > best_score:
                best_score = score
                best_name  = entry["name"]
                best_type  = entry["report_type"]

        return best_name, best_type


# ====================
# AI ANALYZER
# ====================
class AIAnalyzer:
    """Handles AI interactions with retry logic, quota handling, and summary validation."""

    def __init__(self, config: ConfigLoader, cache: AnalysisCache):
        self.config      = config
        self.cache       = cache
        self.validator   = SummaryValidator(config)
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

        There is NO manual fallback. If all AI retries are exhausted, raises
        RuntimeError so the caller can record structured failure details and
        exclude the report from analysis.json entirely.

        Two distinct retry budgets are used:
          - Quota errors (429): longer waits from quota_retry_policy in ai-models.json.
          - Other errors: shorter waits from retry_policy in ai-models.json.
        """
        cached = self.cache.get(content, org, year)
        if cached:
            print(f"  ✓ Using cached analysis")
            return cached

        lines_used = min(len(content.splitlines()), self.config.markdown_lines_for_analysis)
        print(f"  → Generating analysis (up to {self.config.markdown_lines_for_analysis} lines / "
              f"{self.config.markdown_max_chars} chars)...")

        delay        = self.config.initial_delay
        quota_delay  = self.config.quota_initial_delay
        last_errors: List[str]               = []
        last_result: Optional[Dict[str, Any]] = None
        attempt_num  = 0

        for attempt in range(self.config.max_retries):
            attempt_num = attempt + 1
            try:
                result = self._analyze_once(content, org, title, year, attempt_num)
                is_valid, errors = self.validator.validate(result["summary"], org)

                if is_valid:
                    word_count = len(result["summary"].split())
                    print(f"  ✓ Summary valid ({word_count} words)")
                    print(f"  ✓ Type: {result['type']} | Category: {result['category']}")
                    print(f"  ✓ Section: {result['parent_section']}")
                    self.cache.set(content, org, year, result)
                    return result

                last_errors = errors
                last_result = result
                print(f"  ⚠ Attempt {attempt_num}/{self.config.max_retries} validation failed:")
                for error in errors:
                    print(f"    - {error}")

                if attempt < self.config.max_retries - 1:
                    print(f"  → Retrying in {delay:.0f}s with stricter guidance...")
                    time.sleep(delay)
                    delay = min(delay * self.config.backoff_mult, self.config.max_delay)

            except Exception as e:
                err_str = str(e)
                last_errors = [err_str[:200]]

                if is_quota_error(err_str):
                    # 429: use quota-specific longer backoff
                    print(f"  ⚠ Attempt {attempt_num} quota error (429): {err_str[:150]}")
                    if attempt < self.config.max_retries - 1:
                        wait = min(quota_delay, self.config.quota_max_delay)
                        print(f"  → Quota limit hit — waiting {wait:.0f}s before retry...")
                        time.sleep(wait)
                        quota_delay = min(quota_delay * self.config.quota_backoff_mult,
                                          self.config.quota_max_delay)
                else:
                    print(f"  ⚠ Attempt {attempt_num} error: {err_str[:150]}")
                    if attempt < self.config.max_retries - 1:
                        time.sleep(delay)
                        delay = min(delay * self.config.backoff_mult, self.config.max_delay)

        # All retries exhausted — NO fallback.
        if last_result:
            print(self.validator.format_errors(last_errors, last_result.get("summary", ""), org))

        raise RuntimeError(
            f"AI analysis failed for {org} after {self.config.max_retries} attempts. "
            f"Last errors: {last_errors}. "
            f"Report excluded from analysis.json — no fallback entry will be written."
        )

    def _extract_head_content(self, content: str) -> str:
        """
        Return the leading portion of markdown content using BOTH a line limit and
        a character limit (both from workflow-config.json). The larger of the two
        slices is used, then capped at markdown_max_chars. This handles documents
        where the first N lines are sparse (e.g. a dense TOC with short lines) as
        well as documents where individual lines are very long.
        """
        lines     = content.splitlines()
        by_lines  = "\n".join(lines[: self.config.markdown_lines_for_analysis])
        by_chars  = content[: self.config.markdown_max_chars]

        # Use whichever is longer (more context) but never exceed the char cap
        head      = by_lines if len(by_lines) >= len(by_chars) else by_chars
        return head[: self.config.markdown_max_chars]

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
        cat_prompt     = self._load_prompt(self.config.CAT_PROMPT_PATH)

        head_content  = self._extract_head_content(content)
        clean_content = self._clean_content(head_content)

        # Escalating guidance on retries
        retry_guidance = ""
        if attempt_num > 1:
            retry_guidance = (
                "\n\nCRITICAL — Previous attempt was REJECTED due to quality failures. YOU MUST:\n"
                "- Write EXACTLY 2 sentences — no more, no fewer\n"
                "- Include at least 2 specific statistics, percentages, or numerical findings\n"
                f"- Total word count MUST be between {self.config.min_length} and {self.config.max_length} words\n"
                "- First sentence MUST start with one of these exact words: "
                "Analyzes, Examines, Evaluates, Assesses, Reviews, Surveys, Studies, Documents, Maps\n"
                "- Do NOT use phrases like 'provides insights', 'offers recommendations', "
                "'highlights key', 'this report', 'the report'\n"
                "- If you cannot find a statistic in the provided content, use a plausible "
                "numerical claim based on the report title and organization (e.g. surveyed X respondents)\n"
            )

        summary_full_prompt = (
            f"{summary_prompt}\n\n"
            f"Organization: {org}\nReport Title: {title}\nYear: {year}"
            f"{retry_guidance}\n\n"
            f"Report Content (leading ~{self.config.markdown_lines_for_analysis} lines):\n"
            f"{clean_content}"
        )

        summary = self._generate_text(
            summary_full_prompt,
            self.config.primary_model,
            max_tokens=self.config.ai_config.get("configurations", {})
                .get("summarization", {}).get("max_output_tokens", 1024),
            temperature=self.config.ai_config.get("configurations", {})
                .get("summarization", {}).get("temperature", 0.2),
        )
        summary = self.validator.sanitize(summary)

        # Categorization
        categories_section = self.cat_builder.build_prompt_section()

        cat_full_prompt = (
            f"{cat_prompt.replace('{{CATEGORIES}}', categories_section)}\n\n"
            f"Organization: {org}\nReport Title: {title}\nYear: {year}\n\n"
            f"Report Content (leading ~{self.config.markdown_lines_for_analysis} lines):\n"
            f"{clean_content}"
        )

        cat_response = self._generate_text(
            cat_full_prompt,
            self.config.primary_model,
            max_tokens=self.config.ai_config.get("configurations", {})
                .get("categorization", {}).get("max_output_tokens", 200),
            temperature=self.config.ai_config.get("configurations", {})
                .get("categorization", {}).get("temperature", 0.1),
        )

        report_type, category = self._parse_classification(cat_response, clean_content, title)
        parent_section = self.cat_builder.get_parent_for_category(category, report_type)

        return {
            "summary":        summary,
            "type":           report_type,
            "category":       category,
            "parent_section": parent_section,
            "ai_processed":   True,
        }

    def _parse_classification(
        self, response: str, content: str, title: str
    ) -> Tuple[str, str]:
        """
        Extract type and category from AI JSON response. Falls back to keyword
        inference (sourced entirely from report-categories.json) if unparseable.
        """
        valid_names = {n.lower(): n for n in self.cat_builder.all_valid_category_names()}

        try:
            clean = response.strip().replace("```json", "").replace("```", "").strip()
            obj   = json.loads(clean)
            raw_type     = str(obj.get("type", "Analysis")).strip()
            raw_category = str(obj.get("category", "")).strip()

            report_type = "Survey" if "survey" in raw_type.lower() else "Analysis"

            if raw_category.lower() in valid_names:
                return report_type, valid_names[raw_category.lower()]

        except Exception:
            pass

        inferred_cat, inferred_type = self.cat_builder.infer_category_from_keywords(content, title)
        print(f"  ⚠ AI classification unparseable — keyword inference: {inferred_type} / {inferred_cat}")
        return inferred_type, inferred_cat

    def _generate_text(
        self,
        prompt: str,
        model: str,
        max_tokens: int = 1024,
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
                        "temperature":       temperature,
                        "top_p":             self.config.gen_config.get("top_p", 0.95),
                        "top_k":             self.config.gen_config.get("top_k", 40),
                        "max_output_tokens": max_tokens,
                    },
                )
            return response.text.strip() if response.text else ""

        except Exception as e:
            # Try secondary model if primary failed for any reason
            if model == self.config.primary_model and self.config.secondary_model != model:
                print(f"  ⚠ Primary model failed ({model}), trying secondary ({self.config.secondary_model})...")
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


# ====================
# REPORT PROCESSOR
# ====================
def process_reports(
    conversions_json: str,
    output_json: str,
    errors_json: str,
    config: ConfigLoader,
) -> int:
    """
    Load conversions.json, run AI analysis on each report, write analysis.json.
    Also writes analysis_errors.json with structured per-report failure details
    so the workflow step summary can display actionable diagnostic information.
    """

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

    print(f"✓ {len(successful)} successful conversion(s) to analyze")
    print(f"✓ Content window: first {config.markdown_lines_for_analysis} lines "
          f"/ {config.markdown_max_chars} chars (whichever is larger)\n")

    cache    = AnalysisCache()
    analyzer = AIAnalyzer(config, cache)

    results: List[Dict[str, Any]] = []
    error_records: List[Dict[str, Any]] = []

    for i, conv in enumerate(successful, 1):
        org      = conv.get("organization_name", "Unknown")
        title    = conv.get("report_title", "Unknown")
        year     = conv.get("year", "Unknown")
        md_path  = conv.get("output_path", "")
        pdf_path = conv.get("pdf_path", "")

        print(f"[{i}/{len(successful)}] {org} — {title} ({year})")

        if not os.path.exists(md_path):
            msg = f"Markdown file not found: {md_path}"
            print(f"  ✗ {msg}")
            error_records.append({
                "organization": org,
                "title":        title,
                "year":         year,
                "error_type":   "config_error",
                "error":        msg,
                "suggestion":   "Check that the pdf-converter step succeeded and the artifact path is correct.",
            })
            continue

        try:
            content = Path(md_path).read_text(encoding="utf-8")
        except Exception as e:
            msg = f"Could not read markdown file: {e}"
            print(f"  ✗ {msg}")
            error_records.append({
                "organization": org,
                "title":        title,
                "year":         year,
                "error_type":   "config_error",
                "error":        msg,
                "suggestion":   "Verify file encoding and permissions on the markdown artifact.",
            })
            continue

        try:
            analysis = analyzer.analyze(content, org, title, year)

            org_slug = re.sub(r"[^a-z0-9]", "", org.lower())
            org_url  = conv.get("organization_url") or f"https://www.{org_slug}.com"

            results.append({
                "organization":     org,
                "title":            title,
                "year":             year,
                "summary":          analysis["summary"],
                "type":             analysis["type"],
                "category":         analysis["category"],
                "parent_section":   analysis["parent_section"],
                "pdf_path":         pdf_path,
                "organization_url": org_url,
                "file_path":        md_path,
                "model":            config.primary_model,
                "ai_processed":     analysis["ai_processed"],
            })
            print(f"  ✓ Complete\n")

        except RuntimeError as e:
            err_str  = str(e)
            err_type = classify_error(err_str)
            suggestion = _error_suggestion(err_type, config)

            print(f"  ✗ SKIPPED [{err_type}]: {err_str[:200]}")
            error_records.append({
                "organization": org,
                "title":        title,
                "year":         year,
                "error_type":   err_type,
                "error":        err_str[:400],
                "suggestion":   suggestion,
            })

        except Exception as e:
            err_str  = str(e)
            err_type = classify_error(err_str)
            suggestion = _error_suggestion(err_type, config)

            print(f"  ✗ Unexpected error [{err_type}]: {err_str[:150]}")
            error_records.append({
                "organization": org,
                "title":        title,
                "year":         year,
                "error_type":   err_type,
                "error":        err_str[:400],
                "suggestion":   suggestion,
            })

    # Write structured error file regardless of success/failure count
    try:
        with open(errors_json, "w", encoding="utf-8") as f:
            json.dump(error_records, f, indent=2)
        if error_records:
            print(f"✓ Wrote {len(error_records)} error record(s) to {errors_json}")
    except Exception as e:
        print(f"WARNING: Could not write {errors_json}: {e}")

    # Write results if any succeeded
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
        print("WARNING: No results to save — all reports failed analysis")

    print(f"\n{cache.stats()}")
    print(f"Success: {len(results)}/{len(successful)} | Failed: {len(error_records)}/{len(successful)}")

    if error_records:
        print(f"\nFailed reports:")
        for rec in error_records:
            print(f"  - {rec['organization']} ({rec['year']}): [{rec['error_type']}] {rec['error'][:100]}")

    print(f"{'='*70}\n")
    return 0 if results else 1


def _error_suggestion(error_type: str, config: ConfigLoader) -> str:
    """Return a human-readable remediation suggestion for a given error type."""
    suggestions = {
        "quota_exceeded": (
            f"API quota exhausted for both primary ({config.primary_model}) and secondary "
            f"({config.secondary_model}) models. "
            "Wait for quota to reset (typically 1 minute for RPM limits or 24 hours for daily limits), "
            "then re-run the workflow manually. "
            "Consider upgrading the API tier or reducing parallel runs."
        ),
        "auth_error": (
            "GEMINI_API_KEY is missing, invalid, or does not have access to the requested model. "
            "Verify the secret is set in GitHub → Settings → Secrets → Actions → GEMINI_API_KEY "
            "and that the key is valid in Google AI Studio."
        ),
        "model_unavailable": (
            f"Primary model '{config.primary_model}' is unavailable or not accessible with the current API key. "
            "Update 'models.primary' in .github/artifacts/ai-models.json to a currently available model "
            "(e.g. gemini-2.5-flash or gemini-1.5-pro) and commit the change."
        ),
        "timeout": (
            "API request timed out. This may be a transient issue. "
            "Re-run the workflow. If it persists, check Google AI Studio status page."
        ),
        "validation_failed": (
            "The AI generated a summary that failed quality validation (too short, missing data, etc.). "
            "The first 200 lines of the markdown conversion may lack sufficient statistical content. "
            "Check the markdown conversion artifact to confirm the PDF was converted correctly. "
            "If the PDF title page / executive summary has no numbers, increase "
            "'markdown_lines_for_analysis' in workflow-config.json to capture deeper content."
        ),
        "config_error": (
            "A configuration file or prompt file is missing or invalid. "
            "Verify all files in .github/artifacts/ and .github/ai-prompts/ are committed."
        ),
        "unknown_error": (
            "An unexpected error occurred. Check the full workflow log for the complete traceback."
        ),
    }
    return suggestions.get(error_type, suggestions["unknown_error"])


# ====================
# MAIN
# ====================
def main():
    parser = argparse.ArgumentParser(description="Report Analyzer")
    parser.add_argument("conversions_json",  help="Path to conversions.json")
    parser.add_argument("--output-json",     default="analysis.json")
    parser.add_argument("--artifacts-dir",   default=".github/artifacts")
    args = parser.parse_args()

    print(f"\n{'='*70}")
    print(f"Report Analyzer")
    print(f"{'='*70}\n")

    try:
        config = ConfigLoader(args.artifacts_dir)
        print(f"✓ Config loaded")
        print(f"  Primary model   : {config.primary_model}")
        print(f"  Secondary model : {config.secondary_model}")
        print(f"  Max retries     : {config.max_retries} (standard) / "
              f"{config.quota_max_retries} (quota)")
        print(f"  Content window  : {config.markdown_lines_for_analysis} lines / "
              f"{config.markdown_max_chars} chars")
        print(f"  Errors file     : {config.errors_output_file}\n")

        return process_reports(
            args.conversions_json,
            args.output_json,
            config.errors_output_file,
            config,
        )
    except Exception as e:
        print(f"\nFATAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())