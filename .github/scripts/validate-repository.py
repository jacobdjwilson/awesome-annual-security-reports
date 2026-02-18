import os
import sys
import json
import argparse
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional

try:
    from pypdf import PdfReader
except ImportError:
    print("ERROR: pypdf not installed. Install: pip install 'pypdf[crypto]'")
    sys.exit(1)


# ==========================
# CONFIGURATION LOADER
# ==========================
class ConfigLoader:
    """Loads configuration from .github/artifacts/"""

    def __init__(self, artifacts_dir: str = ".github/artifacts"):
        self.artifacts_dir = Path(artifacts_dir)

        self.workflow_config = self._load_json("workflow-config.json")

        if not self.workflow_config:
            raise ValueError("workflow-config.json is required")

    def _load_json(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load JSON file."""
        path = self.artifacts_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"{filename} not found in {self.artifacts_dir}")

        try:
            with open(path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {filename}: {e}")

    def get_validation_config(self) -> Dict[str, Any]:
        """Get validation settings from workflow-config.json."""
        return self.workflow_config.get("workflow", {}).get("validation", {})

    def get_discovery_config(self) -> Dict[str, Any]:
        """Get discovery settings (for file size limits, magic number)."""
        return self.workflow_config.get("workflow", {}).get("discovery", {})


# ==========================
# VALIDATOR
# ==========================
class RepositoryValidator:
    """Validates repository integrity."""

    PDF_ROOT = Path("Annual Security Reports")
    MD_ROOT = Path("Markdown Conversions")

    def __init__(self, config: ConfigLoader):
        self.config = config

        disc_config = config.get_discovery_config()
        val_config = config.get_validation_config()

        self.max_file_size_mb: int = disc_config.get("max_file_size_mb", 100)
        self.pdf_magic: str = disc_config.get("pdf_magic_number", "%PDF")
        self.min_markdown_chars: int = val_config.get("min_markdown_chars", 50)

        self.issues: List[str] = []
        self.stats: Dict[str, int] = {
            "pdf_files": 0,
            "md_files": 0,
            "orphaned_pdfs": 0,
            "orphaned_mds": 0,
            "invalid_pdfs": 0,
            "invalid_mds": 0,
            "oversized_files": 0,
        }

    def validate(self) -> Tuple[bool, List[str]]:
        """
        Run full validation.
        Returns: (has_issues, issue_list)
        """
        print(f"Validating repository structure...")
        print(f"  PDF root:      {self.PDF_ROOT}")
        print(f"  Markdown root: {self.MD_ROOT}")
        print()

        if not self.PDF_ROOT.exists():
            self.issues.append(f"ERROR: PDF directory not found: {self.PDF_ROOT}")
            return True, self.issues

        if not self.MD_ROOT.exists():
            self.issues.append(f"ERROR: Markdown directory not found: {self.MD_ROOT}")
            return True, self.issues

        pdf_files = self._scan_pdfs()
        md_files = self._scan_markdowns()

        self.stats["pdf_files"] = len(pdf_files)
        self.stats["md_files"] = len(md_files)

        print(f"Found {len(pdf_files)} PDF(s) and {len(md_files)} Markdown file(s)\n")

        self._check_orphaned_pdfs(pdf_files, md_files)
        self._check_orphaned_markdowns(md_files, pdf_files)
        self._validate_pdf_integrity(pdf_files)
        self._validate_markdown_integrity(md_files)

        return len(self.issues) > 0, self.issues

    def _scan_pdfs(self) -> Dict[str, Path]:
        """Scan for PDF files. Returns {relative_path: full_path}"""
        return {
            str(f.relative_to(self.PDF_ROOT)): f
            for f in self.PDF_ROOT.rglob("*.pdf")
            if f.is_file()
        }

    def _scan_markdowns(self) -> Dict[str, Path]:
        """Scan for Markdown files. Returns {relative_path: full_path}"""
        return {
            str(f.relative_to(self.MD_ROOT)): f
            for f in self.MD_ROOT.rglob("*.md")
            if f.is_file()
        }

    def _check_orphaned_pdfs(self, pdfs: Dict[str, Path], mds: Dict[str, Path]):
        """Flag PDFs that have no corresponding Markdown conversion."""
        for pdf_rel in pdfs:
            md_rel = pdf_rel.replace(".pdf", ".md")
            if md_rel not in mds:
                self.issues.append(f"Orphaned PDF (no markdown): {pdf_rel}")
                self.stats["orphaned_pdfs"] += 1

    def _check_orphaned_markdowns(self, mds: Dict[str, Path], pdfs: Dict[str, Path]):
        """Flag Markdown files that have no corresponding PDF."""
        for md_rel in mds:
            pdf_rel = md_rel.replace(".md", ".pdf")
            if pdf_rel not in pdfs:
                self.issues.append(f"Orphaned Markdown (no PDF): {md_rel}")
                self.stats["orphaned_mds"] += 1

    def _validate_pdf_integrity(self, pdfs: Dict[str, Path]):
        """Validate each PDF: size, magic number, and readability."""
        for pdf_rel, pdf_path in pdfs.items():
            size_mb = pdf_path.stat().st_size / (1024 * 1024)
            if size_mb > self.max_file_size_mb:
                self.issues.append(
                    f"Oversized PDF ({size_mb:.1f} MB > {self.max_file_size_mb} MB): {pdf_rel}"
                )
                self.stats["oversized_files"] += 1

            try:
                header = pdf_path.read_bytes()[:10].decode("latin-1")
                if not header.startswith(self.pdf_magic):
                    self.issues.append(f"Invalid PDF (bad magic number): {pdf_rel}")
                    self.stats["invalid_pdfs"] += 1
                    continue
            except Exception as e:
                self.issues.append(f"Cannot read PDF: {pdf_rel} ({str(e)[:80]})")
                self.stats["invalid_pdfs"] += 1
                continue

            try:
                reader = PdfReader(pdf_path)
                if len(reader.pages) == 0:
                    self.issues.append(f"Empty PDF (0 pages): {pdf_rel}")
                    self.stats["invalid_pdfs"] += 1
            except Exception as e:
                self.issues.append(f"Corrupted PDF: {pdf_rel} ({str(e)[:80]})")
                self.stats["invalid_pdfs"] += 1

    def _validate_markdown_integrity(self, mds: Dict[str, Path]):
        """Validate each Markdown file is readable and non-trivially empty."""
        for md_rel, md_path in mds.items():
            try:
                content = md_path.read_text(encoding="utf-8")
                if len(content) < self.min_markdown_chars:
                    self.issues.append(
                        f"Empty/short Markdown ({len(content)} chars < {self.min_markdown_chars}): {md_rel}"
                    )
                    self.stats["invalid_mds"] += 1
            except Exception as e:
                self.issues.append(f"Cannot read Markdown: {md_rel} ({str(e)[:80]})")
                self.stats["invalid_mds"] += 1

    def generate_report(self, output_path: str = "validation_report.md"):
        """Write a structured Markdown validation report."""
        lines = ["# Repository Integrity Validation Report\n"]

        if not self.issues:
            lines.append("## ✅ All Checks Passed\n")
            lines.append(
                "Repository structure is consistent and all files are properly paired.\n"
            )
        else:
            lines.append("## ⚠️ Issues Found\n")
            lines.append(f"Found **{len(self.issues)}** issue(s) requiring attention:\n")
            for i, issue in enumerate(self.issues, 1):
                lines.append(f"{i}. {issue}")
            lines.append("")

        lines.append("## 📊 Statistics\n")
        lines.append(f"| Metric | Count |")
        lines.append(f"|--------|-------|")
        lines.append(f"| PDF Files | {self.stats['pdf_files']} |")
        lines.append(f"| Markdown Files | {self.stats['md_files']} |")
        lines.append(f"| Orphaned PDFs | {self.stats['orphaned_pdfs']} |")
        lines.append(f"| Orphaned Markdowns | {self.stats['orphaned_mds']} |")
        lines.append(f"| Invalid PDFs | {self.stats['invalid_pdfs']} |")
        lines.append(f"| Invalid Markdowns | {self.stats['invalid_mds']} |")
        lines.append(f"| Oversized Files | {self.stats['oversized_files']} |")
        lines.append("")
        lines.append("---")
        lines.append(f"*Generated from: {Path.cwd()}*")

        Path(output_path).write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"✓ Report saved: {output_path}")


# ==========================
# MAIN
# ==========================
def main():
    parser = argparse.ArgumentParser(description="Repository Integrity Validator")
    parser.add_argument("--artifacts-dir", default=".github/artifacts")
    parser.add_argument("--output-report", default="validation_report.md")
    args = parser.parse_args()

    print(f"\n{'='*70}")
    print(f"Repository Integrity Validator")
    print(f"{'='*70}\n")

    try:
        config = ConfigLoader(args.artifacts_dir)
        print(f"✓ Config loaded\n")
    except Exception as e:
        print(f"ERROR: Config load failed: {e}")
        return 1

    try:
        validator = RepositoryValidator(config)
        has_issues, issues = validator.validate()

        print(f"\n{'='*70}")
        print(f"Validation Complete")
        print(f"{'='*70}\n")

        validator.generate_report(args.output_report)

        if has_issues:
            print(f"⚠️  Found {len(issues)} issue(s)")
            print(f"✓  GitHub issue will be created/updated by the workflow")
            return 0  # SUCCESS — issues are reported, not a script failure
        else:
            print(f"✅ No issues found — repository integrity confirmed")
            return 0  # SUCCESS — clean

    except Exception as e:
        print(f"ERROR: Validation failed unexpectedly: {e}")
        import traceback
        traceback.print_exc()
        return 1  # FAILURE — script error, not a validation finding


if __name__ == "__main__":
    sys.exit(main())