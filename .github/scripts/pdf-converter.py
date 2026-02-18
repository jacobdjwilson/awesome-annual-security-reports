import os
import sys
import re
import json
import hashlib
import argparse
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
    """Loads configuration from .github/artifacts/"""

    def __init__(self, artifacts_dir: str = ".github/artifacts"):
        self.artifacts_dir = Path(artifacts_dir)

        self.ai_config = self._load_json("ai-models.json")
        self.workflow_config = self._load_json("workflow-config.json")

        if not self.ai_config:
            raise ValueError("ai-models.json is required")
        if not self.workflow_config:
            raise ValueError("workflow-config.json is required")

        # AI model names
        models = self.ai_config.get("models", {})
        self.primary_model: str = models.get("primary", "gemini-2.5-flash")
        self.secondary_model: str = models.get("secondary", "gemini-2.5-flash")

        # Generation config
        self.gen_config: Dict[str, Any] = (
            self.ai_config.get("configurations", {}).get("default", {})
        )

        # Retry policy
        retry = self.ai_config.get("retry_policy", {})
        self.max_retries: int = retry.get("max_attempts", 3)
        self.initial_delay: float = retry.get("initial_delay_seconds", 1)
        self.backoff_mult: float = retry.get("backoff_multiplier", 2)

        # Conversion limits from workflow-config
        disc = self.workflow_config.get("workflow", {}).get("discovery", {})
        self.max_file_size_mb: int = disc.get("max_file_size_mb", 100)

        # Content processing thresholds
        self.min_text_length: int = 100
        self.max_pdf_chars: int = 500_000

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
# CONVERSION CACHE
# ================
class ConversionCache:
    """Caches PDF→Markdown conversion paths to avoid redundant work."""

    def __init__(self, cache_file: str = ".conversion_cache.json"):
        self.cache_file = Path(cache_file)
        self.cache: Dict[str, str] = self._load()
        self.hits = 0
        self.misses = 0

    def _load(self) -> Dict[str, str]:
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
            print(f"WARNING: Could not save conversion cache: {e}")

    def _key(self, pdf_path: str) -> str:
        """Cache key is the absolute path hash."""
        return hashlib.md5(str(Path(pdf_path).resolve()).encode()).hexdigest()

    def get(self, pdf_path: str) -> Optional[str]:
        key = self._key(pdf_path)
        result = self.cache.get(key)
        if result:
            self.hits += 1
        else:
            self.misses += 1
        return result

    def set(self, pdf_path: str, md_path: str):
        self.cache[self._key(pdf_path)] = md_path
        self._save()

    def stats(self) -> str:
        total = self.hits + self.misses
        rate = (self.hits / total * 100) if total > 0 else 0
        return f"Cache: {self.hits} hits, {self.misses} misses ({rate:.1f}% hit rate)"


# ====================
# AI SETUP
# ====================
def setup_gemini(api_key: str, config: ConfigLoader) -> Tuple[bool, Optional[str]]:
    """Probe primary then secondary model to confirm API access."""
    for model_name in [config.primary_model, config.secondary_model]:
        try:
            if USE_NEW_SDK:
                client = genai.Client(api_key=api_key)
                response = client.models.generate_content(model=model_name, contents="test")
                if response.text:
                    print(f"✓ AI Model: {model_name}")
                    return True, model_name
            else:
                genai.configure(api_key=api_key)
                test_model = genai.GenerativeModel(model_name)
                resp = test_model.count_tokens("test")
                if resp.total_tokens:
                    print(f"✓ AI Model: {model_name}")
                    return True, model_name
        except Exception:
            continue

    print("WARNING: No AI models available — proceeding with markitdown only")
    return False, None


# ====================
# PDF CONVERTER
# ====================
class PDFConverter:
    """Converts PDF files to Markdown using markitdown."""

    def __init__(self, config: ConfigLoader):
        self.config = config
        self.cache = ConversionCache()

        try:
            self.markitdown = MarkItDown()
            print("✓ MarkItDown initialized")
        except Exception as e:
            print(f"! MarkItDown init warning: {str(e)[:80]}")
            self.markitdown = MarkItDown()

    def convert(self, pdf_path: str) -> Tuple[bool, str, str]:
        """
        Convert a PDF to Markdown.
        Returns: (success, md_path, message)
        """
        pdf_path_obj = Path(pdf_path)
        if not pdf_path_obj.exists():
            return False, "", "File not found"

        # Return cached result if the output file still exists
        cached = self.cache.get(pdf_path)
        if cached and Path(cached).exists():
            print(f"  ✓ Cached: {cached}")
            return True, cached, "cached"

        org_name, report_title, year = self._parse_filename(pdf_path_obj.name)
        md_path = self._get_markdown_path(pdf_path_obj)
        md_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            print(f"  Converting with markitdown...")
            result = self.markitdown.convert(str(pdf_path_obj))

            if hasattr(result, "text_content"):
                markdown_text = result.text_content
            elif isinstance(result, str):
                markdown_text = result
            else:
                markdown_text = str(result)

            if not markdown_text:
                print(f"  ! No text extracted, saving minimal placeholder")
                markdown_text = f"# {org_name} - {report_title} ({year})\n\nSecurity report conversion pending."

            markdown_text = markdown_text.strip()

            if len(markdown_text) < self.config.min_text_length:
                print(f"  ! Short extraction ({len(markdown_text)} chars)")

            if len(markdown_text) > self.config.max_pdf_chars:
                markdown_text = markdown_text[: self.config.max_pdf_chars]
                print(f"  ! Truncated to {self.config.max_pdf_chars} chars")

            md_path.write_text(markdown_text, encoding="utf-8")
            self.cache.set(pdf_path, str(md_path))

            print(f"  ✓ Converted: {md_path}")
            return True, str(md_path), "success"

        except Exception as e:
            error_msg = str(e)[:200]
            print(f"  ! Conversion error: {error_msg}")

            # Save a minimal stub so downstream steps can still run
            try:
                stub = f"# {org_name} - {report_title} ({year})\n\nConversion error: {error_msg}\n"
                md_path.write_text(stub, encoding="utf-8")
                print(f"  ! Saved minimal stub")
                return True, str(md_path), f"partial ({error_msg[:80]})"
            except Exception:
                return False, "", f"Failed: {error_msg}"

    def _parse_filename(self, filename: str) -> Tuple[str, str, str]:
        """Extract (org, title, year) from a filename like Org-Title-Words-YYYY.pdf"""
        name = filename.replace(".pdf", "")
        year_match = re.search(r"-(\d{4})$", name)

        if year_match:
            year = year_match.group(1)
            name = name[: year_match.start()]
        else:
            year = str(datetime.now().year)

        parts = name.split("-", 1)
        org_name = parts[0]
        report_title = parts[1] if len(parts) >= 2 else "Security Report"
        return org_name, report_title, year

    def _get_markdown_path(self, pdf_path: Path) -> Path:
        """Mirror the PDF path under Markdown Conversions/."""
        parts = list(pdf_path.parts)
        if "Annual Security Reports" in parts:
            idx = parts.index("Annual Security Reports")
            parts[idx] = "Markdown Conversions"
        return Path(*parts).with_suffix(".md")


# ====================
# MAIN
# ====================
def main():
    parser = argparse.ArgumentParser(description="PDF to Markdown Converter")
    parser.add_argument("--file-list", required=True, help="Text file listing PDFs to convert")
    parser.add_argument("--output-json", default="conversions.json")
    parser.add_argument("--artifacts-dir", default=".github/artifacts")
    args = parser.parse_args()

    print(f"\n{'='*70}")
    print(f"PDF to Markdown Converter")
    print(f"{'='*70}\n")

    # Load config
    try:
        config = ConfigLoader(args.artifacts_dir)
        print(f"✓ Config loaded\n")
    except Exception as e:
        print(f"ERROR: Config failed: {e}")
        return 1

    # Optional AI setup (used for future enhancement, not conversion itself)
    gemini_key = os.environ.get("GEMINI_API_KEY")
    if gemini_key:
        setup_gemini(gemini_key, config)
    else:
        print("INFO: No GEMINI_API_KEY — using markitdown only\n")

    # Load file list
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

    # Convert
    converter = PDFConverter(config)
    results: List[Dict[str, Any]] = []

    for i, pdf_path in enumerate(pdf_files, 1):
        print(f"[{i}/{len(pdf_files)}] {Path(pdf_path).name}")

        success, md_path, message = converter.convert(pdf_path)
        org_name, report_title, year = converter._parse_filename(Path(pdf_path).name)

        results.append({
            "pdf_path": pdf_path,
            "output_path": md_path if success else "",
            "status": "success" if success else "failed",
            "message": message,
            "organization_name": org_name,
            "report_title": report_title,
            "year": year,
        })

    # Save results
    with open(args.output_json, "w") as f:
        json.dump(results, f, indent=2)

    successful = sum(1 for r in results if r["status"] == "success")
    failed = len(results) - successful

    print(f"\n{'='*70}")
    print(f"✓ Converted: {successful}/{len(results)}")
    if failed:
        print(f"✗ Failed:    {failed}/{len(results)}")
    print(f"\n{converter.cache.stats()}")
    print(f"✓ Results saved to: {args.output_json}")
    print(f"{'='*70}\n")

    return 0 if successful > 0 else 1


if __name__ == "__main__":
    sys.exit(main())