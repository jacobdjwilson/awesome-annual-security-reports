import os
import sys
import re
import json
import argparse
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional
from datetime import datetime

try:
    from pypdf import PdfReader
except ImportError:
    print("ERROR: pypdf not installed. Install: pip install 'pypdf[crypto]'")
    sys.exit(1)


# ============================================================
# ISSUE CATEGORIES
# Each finding carries a category so the workflow can group,
# deduplicate, and route them intelligently in GitHub Issues.
# ============================================================
CATEGORY_ORPHANED_PDF   = "orphaned_pdf"
CATEGORY_ORPHANED_MD    = "orphaned_md"
CATEGORY_INVALID_PDF    = "invalid_pdf"
CATEGORY_INVALID_MD     = "invalid_md"
CATEGORY_OVERSIZED      = "oversized_file"
CATEGORY_NAMING         = "naming_convention"
CATEGORY_YEAR_MISMATCH  = "year_mismatch"
CATEGORY_STUB_MD        = "stub_markdown"

# ── Filename convention ──────────────────────────────────────
# Expected pattern: <Org>-<Title-Words>-<YYYY>.pdf
# e.g.  Microsoft-Digital-Defense-Report-2024.pdf
FILENAME_YEAR_RE   = re.compile(r"-(\d{4})\.(pdf|md)$", re.IGNORECASE)
FILENAME_VALID_RE  = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 _\-\.]+\-\d{4}\.(pdf|md)$")

# Markdown files that look like stubs from a failed / partial conversion
STUB_PATTERNS = [
    re.compile(r"Security report conversion pending", re.IGNORECASE),
    re.compile(r"^#.+\n\nConversion error:", re.IGNORECASE | re.MULTILINE),
    re.compile(r"Conversion error:", re.IGNORECASE),
]


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
        path = self.artifacts_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"{filename} not found in {self.artifacts_dir}")
        try:
            with open(path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {filename}: {e}")

    def get_validation_config(self) -> Dict[str, Any]:
        return self.workflow_config.get("workflow", {}).get("validation", {})

    def get_discovery_config(self) -> Dict[str, Any]:
        return self.workflow_config.get("workflow", {}).get("discovery", {})


# ==========================
# FINDING
# ==========================
class Finding:
    """
    A single validation finding.

    severity : "error"   — must be fixed (orphan, corrupt, mismatch)
               "warning" — should be reviewed (naming, size, short content)
    category : one of the CATEGORY_* constants above
    file     : repo-relative path of the affected file (empty for global issues)
    message  : human-readable description
    """
    def __init__(self, severity: str, category: str, file: str, message: str):
        self.severity = severity
        self.category = category
        self.file     = file
        self.message  = message

    def to_dict(self) -> Dict[str, str]:
        return {
            "severity": self.severity,
            "category": self.category,
            "file":     self.file,
            "message":  self.message,
        }

    @property
    def fingerprint(self) -> str:
        """Stable identity key — used for issue deduplication."""
        return f"{self.category}|{self.file}"

    def __str__(self) -> str:
        icon = "❌" if self.severity == "error" else "⚠️"
        suffix = f" — `{self.file}`" if self.file else ""
        return f"{icon} [{self.category}] {self.message}{suffix}"


# ==========================
# REPOSITORY VALIDATOR
# ==========================
class RepositoryValidator:
    """
    Comprehensive repository integrity validator.

    Checks performed:
      1. PDF <-> Markdown pair completeness  (orphans in both directions)
      2. PDF file integrity                  (magic number, page count, size)
      3. Markdown integrity                  (readability, length, stub detection)
      4. Filename naming convention          (Org-Title-YYYY.ext)
      5. Year consistency                    (folder year matches filename year)
      6. Stub / failed-conversion detection  (conversion error placeholders)
    """

    PDF_ROOT = Path("Annual Security Reports")
    MD_ROOT  = Path("Markdown Conversions")

    def __init__(self, config: ConfigLoader):
        self.config = config

        disc_config = config.get_discovery_config()
        val_config  = config.get_validation_config()

        self.max_file_size_mb:   int = disc_config.get("max_file_size_mb",   100)
        self.pdf_magic:          str = disc_config.get("pdf_magic_number",   "%PDF")
        self.min_markdown_chars: int = val_config.get("min_markdown_chars",  200)

        self.findings: List[Finding] = []
        self.stats: Dict[str, int] = {
            "pdf_files":       0,
            "md_files":        0,
            "orphaned_pdfs":   0,
            "orphaned_mds":    0,
            "invalid_pdfs":    0,
            "invalid_mds":     0,
            "stub_mds":        0,
            "oversized_files": 0,
            "naming_issues":   0,
            "year_mismatches": 0,
        }

    # ── Public API ────────────────────────────────────────────────────────

    def validate(self) -> Tuple[bool, List[Finding]]:
        """
        Run all checks.  Returns (has_findings, findings_list).
        Never raises — script-level exceptions must not look like findings.
        """
        print("Validating repository structure...")
        print(f"  PDF root:      {self.PDF_ROOT}")
        print(f"  Markdown root: {self.MD_ROOT}")
        print()

        if not self.PDF_ROOT.exists():
            self._add(Finding("error", CATEGORY_INVALID_PDF, "",
                               f"PDF directory not found: {self.PDF_ROOT}"))
            return True, self.findings

        if not self.MD_ROOT.exists():
            self._add(Finding("error", CATEGORY_INVALID_MD, "",
                               f"Markdown directory not found: {self.MD_ROOT}"))
            return True, self.findings

        pdf_files = self._scan_pdfs()
        md_files  = self._scan_markdowns()

        self.stats["pdf_files"] = len(pdf_files)
        self.stats["md_files"]  = len(md_files)

        print(f"Found {len(pdf_files)} PDF(s) and {len(md_files)} Markdown file(s)\n")

        self._check_orphaned_pdfs(pdf_files, md_files)
        self._check_orphaned_markdowns(md_files, pdf_files)
        self._validate_pdf_integrity(pdf_files)
        self._validate_markdown_integrity(md_files)
        self._check_naming_conventions(pdf_files, md_files)
        self._check_year_consistency(pdf_files, md_files)

        errors   = sum(1 for f in self.findings if f.severity == "error")
        warnings = sum(1 for f in self.findings if f.severity == "warning")
        print(f"Validation complete: {errors} error(s), {warnings} warning(s)")

        return len(self.findings) > 0, self.findings

    def generate_report(self, output_md: str = "validation_report.md",
                        output_json: str = "validation_findings.json"):
        """Write human-readable Markdown + machine-readable JSON findings."""
        self._write_markdown(output_md)
        self._write_json(output_json)

    # ── Scanning helpers ──────────────────────────────────────────────────

    def _scan_pdfs(self) -> Dict[str, Path]:
        return {
            str(f.relative_to(self.PDF_ROOT)): f
            for f in self.PDF_ROOT.rglob("*.pdf")
            if f.is_file()
        }

    def _scan_markdowns(self) -> Dict[str, Path]:
        return {
            str(f.relative_to(self.MD_ROOT)): f
            for f in self.MD_ROOT.rglob("*.md")
            if f.is_file()
        }

    def _add(self, finding: Finding):
        self.findings.append(finding)
        print(f"  {finding}")

    # ── Check 1: Orphaned pairs ───────────────────────────────────────────

    def _check_orphaned_pdfs(self, pdfs: Dict[str, Path], mds: Dict[str, Path]):
        print("Checking PDF → Markdown pairs...")
        for pdf_rel in pdfs:
            md_rel = pdf_rel[:-4] + ".md"
            if md_rel not in mds:
                self._add(Finding(
                    "error", CATEGORY_ORPHANED_PDF, pdf_rel,
                    f"PDF has no matching Markdown conversion: {pdf_rel}"
                ))
                self.stats["orphaned_pdfs"] += 1

    def _check_orphaned_markdowns(self, mds: Dict[str, Path], pdfs: Dict[str, Path]):
        print("Checking Markdown → PDF pairs...")
        for md_rel in mds:
            pdf_rel = md_rel[:-3] + ".pdf"
            if pdf_rel not in pdfs:
                self._add(Finding(
                    "error", CATEGORY_ORPHANED_MD, md_rel,
                    f"Markdown has no matching PDF: {md_rel}"
                ))
                self.stats["orphaned_mds"] += 1

    # ── Check 2: PDF file integrity ───────────────────────────────────────

    def _validate_pdf_integrity(self, pdfs: Dict[str, Path]):
        print("Validating PDF integrity...")
        for pdf_rel, pdf_path in pdfs.items():
            # Size
            size_mb = pdf_path.stat().st_size / (1024 * 1024)
            if size_mb > self.max_file_size_mb:
                self._add(Finding(
                    "warning", CATEGORY_OVERSIZED, pdf_rel,
                    f"File is {size_mb:.1f} MB (limit {self.max_file_size_mb} MB)"
                ))
                self.stats["oversized_files"] += 1

            # Magic number
            try:
                header = pdf_path.read_bytes()[:10].decode("latin-1")
                if not header.startswith(self.pdf_magic):
                    self._add(Finding(
                        "error", CATEGORY_INVALID_PDF, pdf_rel,
                        f"Not a valid PDF (bad header): {pdf_rel}"
                    ))
                    self.stats["invalid_pdfs"] += 1
                    continue
            except Exception as e:
                self._add(Finding(
                    "error", CATEGORY_INVALID_PDF, pdf_rel,
                    f"Cannot read PDF header ({str(e)[:80]})"
                ))
                self.stats["invalid_pdfs"] += 1
                continue

            # Page count
            try:
                reader = PdfReader(pdf_path)
                if len(reader.pages) == 0:
                    self._add(Finding(
                        "error", CATEGORY_INVALID_PDF, pdf_rel,
                        f"PDF has 0 pages"
                    ))
                    self.stats["invalid_pdfs"] += 1
            except Exception as e:
                self._add(Finding(
                    "error", CATEGORY_INVALID_PDF, pdf_rel,
                    f"Corrupted or unreadable PDF ({str(e)[:80]})"
                ))
                self.stats["invalid_pdfs"] += 1

    # ── Check 3: Markdown integrity ───────────────────────────────────────

    def _validate_markdown_integrity(self, mds: Dict[str, Path]):
        print("Validating Markdown integrity...")
        for md_rel, md_path in mds.items():
            try:
                content = md_path.read_text(encoding="utf-8")
            except Exception as e:
                self._add(Finding(
                    "error", CATEGORY_INVALID_MD, md_rel,
                    f"Cannot read Markdown file ({str(e)[:80]})"
                ))
                self.stats["invalid_mds"] += 1
                continue

            # Stub / failed-conversion detection (check before length)
            is_stub = False
            for pat in STUB_PATTERNS:
                if pat.search(content):
                    self._add(Finding(
                        "error", CATEGORY_STUB_MD, md_rel,
                        f"Markdown is a conversion stub or error placeholder"
                    ))
                    self.stats["stub_mds"] += 1
                    is_stub = True
                    break

            if not is_stub and len(content) < self.min_markdown_chars:
                self._add(Finding(
                    "warning", CATEGORY_INVALID_MD, md_rel,
                    f"Markdown is suspiciously short "
                    f"({len(content)} chars, min {self.min_markdown_chars})"
                ))
                self.stats["invalid_mds"] += 1

    # ── Check 4: Naming conventions ───────────────────────────────────────

    def _check_naming_conventions(self, pdfs: Dict[str, Path], mds: Dict[str, Path]):
        """
        Files must follow: Org-Title-Words-YYYY.ext
          - End with a hyphen-separated 4-digit year
          - Characters: alphanumerics, hyphens, underscores, dots, spaces
          - First character must be alphanumeric
        """
        print("Checking filename conventions...")
        for rel_path in list(pdfs.keys()) + list(mds.keys()):
            filename = Path(rel_path).name
            if not FILENAME_VALID_RE.match(filename):
                self._add(Finding(
                    "warning", CATEGORY_NAMING, rel_path,
                    f"Filename does not follow Org-Title-YYYY convention: {filename}"
                ))
                self.stats["naming_issues"] += 1

    # ── Check 5: Year consistency ─────────────────────────────────────────

    def _check_year_consistency(self, pdfs: Dict[str, Path], mds: Dict[str, Path]):
        """
        The year in the filename must match the year component of the
        enclosing folder, when a year folder is present.

        Consistent:   2024/Microsoft-Report-2024.pdf
        Inconsistent: 2023/Microsoft-Report-2024.pdf  ← flag this
        """
        print("Checking year consistency...")
        for rel_path in list(pdfs.keys()) + list(mds.keys()):
            filename   = Path(rel_path).name
            year_match = FILENAME_YEAR_RE.search(filename)
            if not year_match:
                continue  # Already caught by naming check

            file_year = year_match.group(1)
            parts     = Path(rel_path).parts
            # Look at every path component except the filename itself
            folder_years = [p for p in parts[:-1] if re.fullmatch(r"\d{4}", p)]

            if not folder_years:
                continue  # Flat layout — no folder year to check against

            for folder_year in folder_years:
                if folder_year != file_year:
                    self._add(Finding(
                        "error", CATEGORY_YEAR_MISMATCH, rel_path,
                        f"Filename year ({file_year}) does not match "
                        f"folder year ({folder_year}): {rel_path}"
                    ))
                    self.stats["year_mismatches"] += 1
                    break

    # ── Report writers ────────────────────────────────────────────────────

    def _write_markdown(self, output_path: str):
        errors   = [f for f in self.findings if f.severity == "error"]
        warnings = [f for f in self.findings if f.severity == "warning"]

        lines = [
            "# Repository Integrity Validation Report\n",
            f"*Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}*\n",
        ]

        if not self.findings:
            lines += [
                "## ✅ All Checks Passed\n",
                "Repository structure is consistent — all files are properly "
                "paired, correctly named, and structurally valid.\n",
            ]
        else:
            lines += [
                "## ⚠️ Issues Found\n",
                f"Found **{len(errors)}** error(s) and **{len(warnings)}** warning(s):\n",
            ]

            category_labels = {
                CATEGORY_ORPHANED_PDF:  "🔴 Orphaned PDFs (no Markdown conversion)",
                CATEGORY_ORPHANED_MD:   "🔴 Orphaned Markdowns (no PDF)",
                CATEGORY_STUB_MD:       "🔴 Stub / Failed Conversions",
                CATEGORY_INVALID_PDF:   "🔴 Invalid or Unreadable PDFs",
                CATEGORY_YEAR_MISMATCH: "🔴 Year Inconsistencies",
                CATEGORY_INVALID_MD:    "🟡 Invalid or Short Markdown Files",
                CATEGORY_NAMING:        "🟡 Filename Convention Violations",
                CATEGORY_OVERSIZED:     "🟡 Oversized Files",
            }

            grouped: Dict[str, List[Finding]] = {}
            for f in self.findings:
                grouped.setdefault(f.category, []).append(f)

            for cat, label in category_labels.items():
                if cat not in grouped:
                    continue
                lines.append(f"\n### {label}\n")
                for f in grouped[cat]:
                    lines.append(f"- {f.message}" + (f" — `{f.file}`" if f.file else ""))
            lines.append("")

        lines += [
            "\n## 📊 Statistics\n",
            "| Metric | Count |",
            "|--------|-------|",
            f"| PDF Files | {self.stats['pdf_files']} |",
            f"| Markdown Files | {self.stats['md_files']} |",
            f"| Orphaned PDFs | {self.stats['orphaned_pdfs']} |",
            f"| Orphaned Markdowns | {self.stats['orphaned_mds']} |",
            f"| Invalid PDFs | {self.stats['invalid_pdfs']} |",
            f"| Invalid / Short Markdowns | {self.stats['invalid_mds']} |",
            f"| Stub Markdowns | {self.stats['stub_mds']} |",
            f"| Year Mismatches | {self.stats['year_mismatches']} |",
            f"| Naming Issues | {self.stats['naming_issues']} |",
            f"| Oversized Files | {self.stats['oversized_files']} |",
            "",
            "---",
            f"*Validated from: {Path.cwd()}*",
        ]

        Path(output_path).write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"\n✓ Markdown report saved: {output_path}")

    def _write_json(self, output_path: str):
        """
        Write machine-readable findings for the workflow's issue-management logic.

        The 'fingerprints' list is a stable, sorted set of category|file strings.
        The workflow compares this against the fingerprints embedded in the
        currently-open GitHub issue body to determine what is new, resolved, or
        unchanged — enabling partial issue updates without duplication.
        """
        payload = {
            "timestamp":     datetime.utcnow().isoformat() + "Z",
            "has_findings":  len(self.findings) > 0,
            "error_count":   sum(1 for f in self.findings if f.severity == "error"),
            "warning_count": sum(1 for f in self.findings if f.severity == "warning"),
            "stats":         self.stats,
            "findings":      [f.to_dict() for f in self.findings],
            "fingerprints":  sorted({f.fingerprint for f in self.findings}),
        }
        Path(output_path).write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print(f"✓ JSON findings saved: {output_path}")


# ==========================
# MAIN
# ==========================
def main():
    parser = argparse.ArgumentParser(description="Repository Integrity Validator")
    parser.add_argument("--artifacts-dir",   default=".github/artifacts")
    parser.add_argument("--output-report",   default="validation_report.md")
    parser.add_argument("--output-findings", default="validation_findings.json")
    args = parser.parse_args()

    print(f"\n{'='*70}")
    print("Repository Integrity Validator")
    print(f"{'='*70}\n")

    try:
        config = ConfigLoader(args.artifacts_dir)
        print("✓ Config loaded\n")
    except Exception as e:
        print(f"ERROR: Config load failed: {e}")
        return 1

    try:
        validator = RepositoryValidator(config)
        has_findings, findings = validator.validate()

        print(f"\n{'='*70}")
        print("Validation Complete")
        print(f"{'='*70}\n")

        validator.generate_report(
            output_md=args.output_report,
            output_json=args.output_findings,
        )

        errors   = sum(1 for f in findings if f.severity == "error")
        warnings = sum(1 for f in findings if f.severity == "warning")

        if has_findings:
            print(f"\n⚠️  {errors} error(s), {warnings} warning(s) found")
            print("   GitHub issue will be managed by the workflow")
        else:
            print("\n✅ No issues found — repository integrity confirmed")

        # Always exit 0 when the script itself ran without errors.
        # Validation findings are handled by the workflow through the JSON output;
        # they are not script failures.
        return 0

    except Exception as e:
        print(f"\nFATAL: Validation script error: {e}")
        import traceback
        traceback.print_exc()
        # Exit 1 only for genuine script errors (not for validation findings).
        return 1


if __name__ == "__main__":
    sys.exit(main())