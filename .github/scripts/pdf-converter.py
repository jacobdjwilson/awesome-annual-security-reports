import os
import sys
import re
import json
import hashlib
import argparse
import time
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime

# ==========================
# DEPENDENCY CHECKS
# ==========================
try:
    from markitdown import MarkItDown
except ImportError:
    print("ERROR: markitdown required. Install: pip install markitdown")
    sys.exit(1)

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
    """
    Loads all runtime configuration from .github/artifacts/ JSON files.
    No values are hardcoded in this script — everything is sourced from:
      - ai-models.json       : model names, generation params, retry policy
      - workflow-config.json : file size limits, content thresholds, prompt path
    """

    # Safe fallback path if workflow-config.json is missing the key
    DEFAULT_CONVERSION_PROMPT_PATH = ".github/ai-prompts/pdf-to-markdown-prompt.md"

    def __init__(self, artifacts_dir: str = ".github/artifacts"):
        self.artifacts_dir = Path(artifacts_dir)

        self.ai_config       = self._load_json("ai-models.json")
        self.workflow_config = self._load_json("workflow-config.json")

        if not self.ai_config:
            raise ValueError("ai-models.json is required")
        if not self.workflow_config:
            raise ValueError("workflow-config.json is required")

        # ── AI model names ────────────────────────────────────────────────
        models = self.ai_config.get("models", {})
        self.primary_model:   str = models.get("primary",   "gemini-2.5-flash")
        self.secondary_model: str = models.get("secondary", "gemini-2.5-flash")

        # ── Generation configs (keyed by task) ────────────────────────────
        configs = self.ai_config.get("configurations", {})
        self.default_gen_config:    Dict[str, Any] = configs.get("default",    {})
        self.conversion_gen_config: Dict[str, Any] = configs.get("conversion", {})

        # ── Retry / rate-limit policy ─────────────────────────────────────
        retry = self.ai_config.get("retry_policy", {})
        self.max_retries:   int   = retry.get("max_attempts",          3)
        self.initial_delay: float = retry.get("initial_delay_seconds", 1)
        self.backoff_mult:  float = retry.get("backoff_multiplier",    2)
        self.max_delay:     float = retry.get("max_delay_seconds",    10)

        # ── Conversion settings from workflow-config ──────────────────────
        conv = self.workflow_config.get("workflow", {}).get("conversion", {})
        disc = self.workflow_config.get("workflow", {}).get("discovery",  {})

        self.max_file_size_mb:       int = disc.get("max_file_size_mb",       100)
        self.min_text_length:        int = conv.get("min_text_length",         100)
        self.max_pdf_chars:          int = conv.get("max_pdf_chars",       500_000)
        self.max_polish_input_chars: int = conv.get("max_polish_input_chars", 60_000)
        self.conversion_prompt_path: str = conv.get(
            "prompt_path", self.DEFAULT_CONVERSION_PROMPT_PATH
        )

        # ── Folder names ──────────────────────────────────────────────────
        folders = self.workflow_config.get("workflow", {}).get("folders", {})
        self.pdf_source_folder:      str = folders.get("pdf_source",           "Annual Security Reports")
        self.markdown_output_folder: str = folders.get("markdown_conversions", "Markdown Conversions")

        # ── Validation settings ───────────────────────────────────────────
        val = self.workflow_config.get("workflow", {}).get("validation", {})
        self.min_markdown_chars:     int = val.get("min_markdown_chars",       200)

    def _load_json(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load and parse a JSON config file from artifacts_dir."""
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
# CONVERSION CACHE
# ================
class ConversionCache:
    """Caches PDF to Markdown conversion output paths and metadata to avoid redundant work."""

    def __init__(self, cache_file: str = ".conversion_cache.json"):
        self.cache_file = Path(cache_file)
        self.cache: Dict[str, Any] = self._load()
        self.hits   = 0
        self.misses = 0

    def _load(self) -> Dict[str, Any]:
        if self.cache_file.exists():
            try:
                with open(self.cache_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    # Migrate old string paths to dicts
                    for k, v in list(data.items()):
                        if isinstance(v, str):
                            data[k] = {
                                "path": v,
                                "model": "unknown",
                                "timestamp": 0
                            }
                    return data
            except Exception:
                return {}
        return {}

    def _save(self):
        try:
            with open(self.cache_file, "w", encoding="utf-8") as f:
                json.dump(self.cache, f, indent=2)
        except Exception as e:
            print(f"WARNING: Could not save conversion cache: {e}")

    def _key(self, pdf_path: str) -> str:
        return hashlib.md5(str(Path(pdf_path).resolve()).encode()).hexdigest()

    def get_entry(self, pdf_path: str) -> Optional[Dict[str, Any]]:
        key    = self._key(pdf_path)
        result = self.cache.get(key)
        if result:
            self.hits += 1
        else:
            self.misses += 1
        return result

    def get(self, pdf_path: str) -> Optional[str]:
        entry = self.get_entry(pdf_path)
        return entry["path"] if entry else None

    def set(self, pdf_path: str, md_path: str, model_name: str = "unknown"):
        import time
        self.cache[self._key(pdf_path)] = {
            "path": md_path,
            "model": model_name,
            "timestamp": int(time.time())
        }
        self._save()

    def stats(self) -> str:
        total = self.hits + self.misses
        rate  = (self.hits / total * 100) if total > 0 else 0
        return f"Cache: {self.hits} hits, {self.misses} misses ({rate:.1f}% hit rate)"


# ====================
# AI SETUP
# ====================
def setup_gemini(api_key: str, config: ConfigLoader) -> Tuple[bool, Optional[str]]:
    """
    Probe primary then secondary model to confirm API access.
    Returns (success, active_model_name).
    """
    for model_name in [config.primary_model, config.secondary_model]:
        try:
            if USE_NEW_SDK:
                client   = genai.Client(api_key=api_key)
                response = client.models.generate_content(model=model_name, contents="test")
                if response.text:
                    print(f"✓ AI Model: {model_name}")
                    return True, model_name
            else:
                genai.configure(api_key=api_key)
                test_model = genai.GenerativeModel(model_name)
                resp       = test_model.count_tokens("test")
                if resp.total_tokens:
                    print(f"✓ AI Model: {model_name}")
                    return True, model_name
        except Exception:
            continue

    print("WARNING: No AI models available — proceeding with markitdown only")
    return False, None


# ====================
# MARKDOWN POLISHER
# ====================
class MarkdownPolisher:
    """
    Uses the Gemini API to reformat raw markitdown output into clean,
    well-structured Markdown with a proper Table of Contents.

    Prompt:
      Loaded from the path in workflow-config.json → workflow.conversion.prompt_path
      (default: .github/ai-prompts/pdf-to-markdown-prompt.md).
      No prompt text is hardcoded in this file.

    Generation parameters:
      Sourced from ai-models.json → configurations.conversion.
      No AI settings are hardcoded in this file.
    """

    def __init__(self, api_key: str, config: ConfigLoader):
        self.config  = config
        self.api_key = api_key
        self._active_model: Optional[str] = None

        # Load prompt from disk — path comes from workflow-config.json
        self._prompt_template: str = self._load_prompt(config.conversion_prompt_path)

        # Generation params — all from ai-models.json → configurations.conversion
        conv_cfg = config.conversion_gen_config
        self._temperature:    float = conv_cfg.get("temperature",        0.1)
        self._top_p:          float = conv_cfg.get("top_p",              0.95)
        self._top_k:          int   = conv_cfg.get("top_k",              40)
        self._max_out_tokens: int   = conv_cfg.get("max_output_tokens",  65536)

        if USE_NEW_SDK:
            self.client = genai.Client(api_key=api_key)
        else:
            genai.configure(api_key=api_key)

    # ── Prompt loading ────────────────────────────────────────────────────

    def _load_prompt(self, prompt_path: str) -> str:
        """
        Read the prompt file from disk.
        pdf-to-markdown-prompt.md already ends with a '# Report Content Below'
        sentinel line — we append the report metadata and raw content after it.
        """
        p = Path(prompt_path)
        if not p.exists():
            raise FileNotFoundError(
                f"Conversion prompt not found: {prompt_path}\n"
                f"  Expected at: {p.resolve()}"
            )
        return p.read_text(encoding="utf-8")

    def _build_prompt(self, org: str, title: str, year: str, raw_content: str) -> str:
        """
        Compose the full prompt by appending report metadata and raw content
        after the prompt's sentinel line ('# Report Content Below').
        """
        header = (
            f"\nOrganization: {org}\n"
            f"Report Title:  {title}\n"
            f"Year:          {year}\n\n"
            f"Raw Extracted Content:\n"
        )
        return self._prompt_template + header + raw_content

    # ── Model call ────────────────────────────────────────────────────────

    def _call_model(self, model_name: str, prompt: str) -> Optional[str]:
        """Single generation attempt; returns cleaned text or None on failure."""
        try:
            if USE_NEW_SDK:
                response = self.client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        temperature=self._temperature,
                        top_p=self._top_p,
                        top_k=self._top_k,
                        max_output_tokens=self._max_out_tokens,
                    ),
                )
            else:
                model    = genai.GenerativeModel(model_name)
                response = model.generate_content(
                    prompt,
                    generation_config={
                        "temperature":       self._temperature,
                        "top_p":             self._top_p,
                        "top_k":             self._top_k,
                        "max_output_tokens": self._max_out_tokens,
                    },
                )

            text = response.text.strip() if response.text else ""
            if not text:
                return None

            # The prompt tells the model not to wrap output in code fences,
            # but we strip them defensively if it does so anyway.
            if text.startswith("```markdown"):
                text = text[len("```markdown"):].lstrip()
            if text.startswith("```"):
                text = text[3:].lstrip()
            if text.endswith("```"):
                text = text[:-3].rstrip()

            return text.strip()

        except Exception as e:
            err = str(e)
            if is_quota_error(err):
                raise  # propagate so polish() retry loop can apply the right wait
            print(f"  ! Model {model_name} error: {err[:120]}")
            return None

    # ── Public API ────────────────────────────────────────────────────────

    def polish(self, raw_markdown: str, org: str, title: str, year: str) -> str:
        """
        Reformat raw_markdown using Gemini with retry logic and primary/secondary
        model fallback.  Returns the raw text unchanged if AI is unavailable.

        Large documents are chunked: the first max_polish_input_chars characters
        are reformatted by the AI; any overflow is appended as-is after a separator.
        """
        if not raw_markdown or not raw_markdown.strip():
            return raw_markdown

        max_in = self.config.max_polish_input_chars
        if len(raw_markdown) > max_in:
            first_chunk = raw_markdown[:max_in]
            remainder   = raw_markdown[max_in:]
        else:
            first_chunk = raw_markdown
            remainder   = ""

        prompt = self._build_prompt(org, title, year, first_chunk)

        polished: Optional[str] = None
        delay = self.config.initial_delay

        quota_exhausted = False
        for attempt in range(self.config.max_retries):
            try:
                for model_name in [self.config.primary_model, self.config.secondary_model]:
                    polished = self._call_model(model_name, prompt)
                    if polished:
                        self._active_model = model_name
                        break
            except Exception as e:
                err = str(e)
                if is_quota_error(err):
                    api_delay = extract_retry_delay(err)
                    if attempt < self.config.max_retries - 1:
                        wait = api_delay if api_delay else min(delay * 4, 120)
                        print(f"  ! Quota error (429) — waiting {wait:.0f}s "
                              f"(source: {'API' if api_delay else 'config'})...")
                        time.sleep(wait)
                        if not api_delay:
                            delay = min(delay * self.config.backoff_mult, self.config.max_delay)
                    else:
                        quota_exhausted = True
                    continue
                print(f"  ! Unexpected error: {err[:120]}")
            if polished:
                break
            if attempt < self.config.max_retries - 1:
                print(f"  ! Retry {attempt + 1}/{self.config.max_retries} after {delay:.0f}s...")
                time.sleep(delay)
                delay = min(delay * self.config.backoff_mult, self.config.max_delay)

        if quota_exhausted:
            raise RuntimeError("quota_exhausted: Gemini 429 after all retries in polish()")

        if not polished:
            print("  ! AI polish unavailable — returning raw markitdown output")
            return raw_markdown

        if remainder:
            polished = polished + "\n\n---\n\n" + remainder.strip()

        return polished


# ====================
# PDF CONVERTER
# ====================
class PDFConverter:
    """
    Converts PDF files to Markdown using markitdown for text extraction,
    then uses the Gemini-powered MarkdownPolisher to structure the output
    (proper TOC, heading hierarchy, clean paragraphs, OCR noise removal).

    All paths and thresholds are sourced from ConfigLoader.
    """

    def __init__(self, config: ConfigLoader, polisher: Optional[MarkdownPolisher] = None,
                 force_reconvert: bool = False, smart_reconvert: bool = False):
        self.config          = config
        self.cache           = ConversionCache()
        self.polisher        = polisher
        self.force_reconvert = force_reconvert
        self.smart_reconvert = smart_reconvert

        try:
            self.markitdown = MarkItDown()
            print("✓ MarkItDown initialized")
        except Exception as e:
            print(f"! MarkItDown init warning: {str(e)[:80]}")
            self.markitdown = MarkItDown()

    def convert(self, pdf_path: str) -> Tuple[bool, str, str]:
        """
        Convert a single PDF to Markdown.
        Returns: (success, md_output_path, status_message)
        """
        pdf_path_obj = Path(pdf_path)
        if not pdf_path_obj.exists():
            return False, "", "File not found"

        # Return cached result if the output file still exists on disk,
        # unless force_reconvert is set or smart_reconvert indicates a better
        # model is available or the previous conversion was structurally invalid.
        cached_entry = self.cache.get_entry(pdf_path)
        cached_path = cached_entry["path"] if cached_entry else None
        existing_md = self._get_markdown_path(pdf_path_obj)
        
        needs_reconvert = False
        reconvert_reason = ""
        
        if self.force_reconvert:
            needs_reconvert = True
            reconvert_reason = "force-reconvert requested"
        elif self.smart_reconvert:
            if not cached_entry:
                needs_reconvert = True
                reconvert_reason = "not in cache"
            elif not existing_md.exists():
                needs_reconvert = True
                reconvert_reason = "cached file missing from disk"
            else:
                cached_model = cached_entry.get("model", "unknown")
                current_model = self.config.primary_model
                if cached_model != current_model:
                    needs_reconvert = True
                    reconvert_reason = f"model changed ({cached_model} -> {current_model})"
                else:
                    md_text = existing_md.read_text(encoding="utf-8", errors="ignore")
                    if len(md_text) < self.config.min_markdown_chars:
                        needs_reconvert = True
                        reconvert_reason = f"markdown too short ({len(md_text)} chars < {self.config.min_markdown_chars})"
        elif not cached_entry or not existing_md.exists():
            needs_reconvert = True
            reconvert_reason = "not in cache or missing from disk"
            
        if not needs_reconvert:
            print(f"  ✓ Cached: {existing_md}")
            return True, str(existing_md), "cached"
        else:
            if existing_md.exists():
                existing_md.unlink()
                print(f"  ♻ Reconvert ({reconvert_reason}): removed stale {existing_md.name}")
            else:
                print(f"  ♻ Convert: {reconvert_reason}")

        org_name, report_title, year = self._parse_filename(pdf_path_obj.name)
        md_path = self._get_markdown_path(pdf_path_obj)
        md_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            # ── Step 1: raw extraction via markitdown ─────────────────────
            print(f"  → Extracting with markitdown...")
            result = self.markitdown.convert(str(pdf_path_obj))

            if hasattr(result, "text_content"):
                markdown_text = result.text_content
            elif isinstance(result, str):
                markdown_text = result
            else:
                markdown_text = str(result)

            is_stub = False
            if not markdown_text:
                print(f"  ! No text extracted — saving minimal placeholder")
                markdown_text = (
                    f"# {org_name} - {report_title} ({year})\n\n"
                    "Security report conversion pending."
                )
                is_stub = True

            markdown_text = markdown_text.strip()

            if len(markdown_text) < self.config.min_text_length:
                print(f"  ! Short extraction ({len(markdown_text)} chars)")
                is_stub = True

            # Hard cap before sending to AI (avoids token/cost overrun)
            if len(markdown_text) > self.config.max_pdf_chars:
                markdown_text = markdown_text[: self.config.max_pdf_chars]
                print(f"  ! Truncated raw text to {self.config.max_pdf_chars:,} chars")

            # ── Step 2: AI polish — structure, TOC, clean paragraphs ──────
            if self.polisher and not is_stub:
                print(f"  → Polishing with AI ({self.config.primary_model})...")
                markdown_text = self.polisher.polish(
                    markdown_text, org_name, report_title, year
                )
                model_used = self.polisher._active_model or "unknown"
                print(f"  ✓ Polished via {model_used} ({len(markdown_text):,} chars)")
            else:
                print(f"  ⚠ No AI polisher — saving raw markitdown output")

            md_path.write_text(markdown_text, encoding="utf-8")
            
            model_to_cache = self.polisher._active_model if self.polisher and getattr(self.polisher, '_active_model', None) else "unknown"
            self.cache.set(pdf_path, str(md_path), model_to_cache)

            print(f"  ✓ Saved: {md_path}")
            if is_stub:
                return False, str(md_path), "failed (stub)"
            return True, str(md_path), "success"

        except Exception as e:
            error_msg = str(e)[:200]
            print(f"  ! Conversion error: {error_msg}")

            # Save a minimal stub so downstream steps can still run
            try:
                stub = (
                    f"# {org_name} - {report_title} ({year})\n\n"
                    f"Conversion error: {error_msg}\n"
                )
                md_path.write_text(stub, encoding="utf-8")
                print(f"  ! Saved minimal stub to {md_path}")
                return False, str(md_path), f"partial ({error_msg[:80]})"
            except Exception:
                return False, "", f"Failed: {error_msg}"

    def _parse_filename(self, filename: str) -> Tuple[str, str, str]:
        """Extract (org, title, year) from a filename like Org-Title-Words-YYYY.pdf"""
        name       = filename.replace(".pdf", "")
        year_match = re.search(r"-(\d{4})$", name)

        if year_match:
            year = year_match.group(1)
            name = name[: year_match.start()]
        else:
            year = str(datetime.now().year)

        parts        = name.split("-", 1)
        org_name     = parts[0]
        report_title = parts[1] if len(parts) >= 2 else "Security Report"
        return org_name, report_title, year

    def _get_markdown_path(self, pdf_path: Path) -> Path:
        """
        Mirror the PDF path under the Markdown Conversions folder.
        Folder names are read from workflow-config.json → workflow.folders.
        """
        parts = list(pdf_path.parts)
        if self.config.pdf_source_folder in parts:
            idx        = parts.index(self.config.pdf_source_folder)
            parts[idx] = self.config.markdown_output_folder
        return Path(*parts).with_suffix(".md")


# ====================
# MAIN
# ====================
def main():
    parser = argparse.ArgumentParser(description="PDF to Markdown Converter")
    parser.add_argument("--file-list",       required=True, help="Text file listing PDFs to convert")
    parser.add_argument("--output-json",     default="conversions.json")
    parser.add_argument("--artifacts-dir",   default=".github/artifacts")
    parser.add_argument("--force-reconvert", action="store_true", help="Bypass cache and force reconversion of all PDFs")
    parser.add_argument("--smart-reconvert", action="store_true", help="Reconvert only if a newer AI model is available or current Markdown is bad")
    
    args = parser.parse_args()

    print(f"\n{'='*70}")
    print("PDF to Markdown Converter")
    print(f"{'='*70}\n")

    # ── Load configuration ────────────────────────────────────────────────
    try:
        config = ConfigLoader(args.artifacts_dir)
    except Exception as e:
        print(f"ERROR: Config failed: {e}")
        return 1

    print(f"✓ Config loaded")
    print(f"  Primary model    : {config.primary_model}")
    print(f"  Secondary model  : {config.secondary_model}")
    print(f"  Conversion prompt: {config.conversion_prompt_path}")
    print(f"  Max PDF chars    : {config.max_pdf_chars:,}")
    print(f"  Max polish input : {config.max_polish_input_chars:,}")
    print()

    # ── Set up AI polisher ────────────────────────────────────────────────
    gemini_key = os.environ.get("GEMINI_API_KEY")
    polisher: Optional[MarkdownPolisher] = None

    if gemini_key:
        ai_ok, _ = setup_gemini(gemini_key, config)
        if ai_ok:
            try:
                polisher = MarkdownPolisher(gemini_key, config)
                print(f"✓ Markdown polisher ready (prompt: {config.conversion_prompt_path})\n")
            except FileNotFoundError as e:
                print(f"WARNING: {e}")
                print("  Markdown will not be AI-polished — prompt file missing\n")
        else:
            print("INFO: No AI models responded — markdown will not be polished\n")
    else:
        print("INFO: No GEMINI_API_KEY — markdown will not be polished\n")

    # ── Load file list ────────────────────────────────────────────────────
    if not os.path.exists(args.file_list):
        print(f"ERROR: File list not found: {args.file_list}")
        return 1

    with open(args.file_list, "r") as f:
        pdf_files = [line.strip() for line in f if line.strip()]

    if not pdf_files:
        print("No files to process")
        with open(args.output_json, "w") as f:
            json.dump([], f)
        return 0

    print(f"✓ {len(pdf_files)} file(s) to convert\n")

    # ── Convert ───────────────────────────────────────────────────────────
    converter = PDFConverter(config, polisher=polisher,
                            force_reconvert=args.force_reconvert,
                            smart_reconvert=args.smart_reconvert)
    results: List[Dict[str, Any]] = []

    quota_exhausted_flag = False

    for i, pdf_path in enumerate(pdf_files, 1):
        print(f"[{i}/{len(pdf_files)}] {Path(pdf_path).name}")

        try:
            success, md_path, message = converter.convert(pdf_path)
        except RuntimeError as e:
            if is_quota_error(str(e)):
                quota_exhausted_flag = True
                results.append({
                    "pdf_path": pdf_path, "output_path": "", "status": "failed",
                    "message": str(e)[:200], "organization_name": "",
                    "report_title": "", "year": "", "model": None,
                    "method": "", "attempts": 1, "output_chars": None,
                })
                continue
            raise
        org_name, report_title, year = converter._parse_filename(Path(pdf_path).name)

        # Determine method and model used
        if message == "cached":
            method = "cached"
        elif args.force_reconvert or args.smart_reconvert:
            method = "reconverted+ai" if polisher else "reconverted"
        else:
            method = "markitdown+ai" if polisher else "markitdown"
        model_used = (polisher._active_model if polisher and polisher._active_model else None)

        # Count output chars for visibility
        output_chars: Optional[int] = None
        if success and md_path and Path(md_path).exists():
            try:
                output_chars = len(Path(md_path).read_text(encoding="utf-8"))
            except Exception:
                pass

        results.append({
            "pdf_path":          pdf_path,
            "output_path":       md_path,
            "status":            "success" if success else "failed",
            "message":           message,
            "organization_name": org_name,
            "report_title":      report_title,
            "year":              year,
            "model":             model_used,
            "method":            method,
            "attempts":          1,
            "output_chars":      output_chars,
        })

    # ── Save results ──────────────────────────────────────────────────────
    with open(args.output_json, "w") as f:
        json.dump(results, f, indent=2)

    successful = sum(1 for r in results if r["status"] == "success")
    failed     = len(results) - successful

    print(f"\n{'='*70}")
    print(f"✓ Converted: {successful}/{len(results)}")
    if failed:
        print(f"✗ Failed:    {failed}/{len(results)}")
    print(f"\n{converter.cache.stats()}")
    print(f"✓ Results saved to: {args.output_json}")
    print(f"{'='*70}\n")

    if successful == 0 and quota_exhausted_flag:
        print("QUOTA_EXHAUSTED=true")
        return EXIT_QUOTA_EXHAUSTED
    return 0 if successful > 0 else 1


if __name__ == "__main__":
    sys.exit(main())