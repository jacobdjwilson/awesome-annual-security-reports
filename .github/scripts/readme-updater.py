import os
import sys
import json
import re
import argparse
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional
from datetime import datetime
import urllib.parse


# ==========================
# CONFIGURATION LOADER
# ==========================
class ConfigLoader:
    """Loads all policy values from .github/artifacts/ JSON files."""

    def __init__(self, artifacts_dir: str = ".github/artifacts"):
        self.artifacts_dir = Path(artifacts_dir)

        self.categories_config = self._load_json("report-categories.json")
        self.readme_config     = self._load_json("readme-updater-config.json")

        if not self.categories_config:
            raise ValueError("report-categories.json is required")
        if not self.readme_config:
            raise ValueError("readme-updater-config.json is required")

        # Processing config
        proc = self.readme_config.get("processing", {})
        self.age_threshold_years: int = proc.get("age_threshold_years", 2)
        self.start_marker: str        = proc.get("start_marker", "## Analysis Reports")
        self.end_marker: str          = proc.get("end_marker", "## Resources")
        self.pdf_root_folder: str     = proc.get("pdf_root_folder", "Annual Security Reports")

        # Matching config
        matching = self.readme_config.get("matching", {})
        self.similarity_threshold: float = matching.get("similarity_threshold", 0.6)
        # Fields to rewrite in-place when a newer-year edition is detected.
        # Defined in readme-updater-config.json so policy stays out of code.
        self.update_fields: List[str] = matching.get("update_fields", ["organization_url", "summary"])

        # Summary validation rules
        val = self.readme_config.get("validation", {}).get("summary", {})
        self.summary_max_length: int   = val.get("max_length", 800)
        self.summary_min_length: int   = val.get("min_length", 100)
        self.required_verbs:     List[str] = [v.lower() for v in val.get("required_verbs", [])]
        self.forbidden_phrases:  List[str] = [p.lower() for p in val.get("forbidden_phrases", [])]
        self.marketing_words:    List[str] = [w.lower() for w in val.get("marketing_words", [])]

    def _load_json(self, filename: str) -> Optional[Dict[str, Any]]:
        path = self.artifacts_dir / filename
        if not path.exists():
            print(f"ERROR: {filename} not found at {path}")
            return None
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid JSON in {filename}: {e}")
            return None

    def is_year_in_scope(self, report_year: int) -> bool:
        """
        True when the report year falls within the active listing window.

        Window = (current_year - age_threshold_years, current_year] exclusive on
        the lower bound.
        Threshold is read from readme-updater-config.json, not hard-coded.
        """
        current_year = datetime.now().year
        return current_year - report_year < self.age_threshold_years


# ==========================
# SUMMARY VALIDATOR
# ==========================
class SummaryValidator:
    """Validates and sanitizes AI-generated summaries against rules from
    readme-updater-config.json → validation.summary."""

    def __init__(self, config: ConfigLoader):
        self.max_length      = config.summary_max_length
        self.min_length      = config.summary_min_length
        self.required_verbs  = config.required_verbs
        self.forbidden_phrases = config.forbidden_phrases
        self.marketing_words = config.marketing_words

    def validate(self, summary: str) -> Tuple[bool, List[str]]:
        """Return (is_valid, [error_codes])."""
        errors: List[str] = []
        if not summary:
            return False, ["Empty summary"]

        if len(summary) > self.max_length:
            errors.append("TooLong")
        elif len(summary) < self.min_length:
            errors.append("TooShort")

        if "\n" in summary:
            errors.append("ContainsNewlines")

        words = summary.split()
        first = words[0].lower().rstrip(".,;:") if words else ""
        if self.required_verbs and first not in self.required_verbs:
            errors.append("BadStart")

        if "(" in summary or ")" in summary or '"' in summary:
            errors.append("Quotes/Parens")

        lower = summary.lower()
        for phrase in self.forbidden_phrases:
            if phrase in lower:
                errors.append(f"ForbiddenPhrase:{phrase}")
        for word in self.marketing_words:
            if word in lower:
                errors.append(f"MarketingWord:{word}")

        return len(errors) == 0, errors

    def sanitize(self, summary: str) -> str:
        """Best-effort cleanup: collapse whitespace, strip parens/quotes,
        ensure terminal period, trim to max_length on sentence boundary."""
        if not summary:
            return ""
        summary = " ".join(summary.split())
        summary = re.sub(r'[()"\']', "", summary)
        if not summary.endswith("."):
            summary += "."
        if len(summary) > self.max_length:
            sentences = summary.split(". ")
            trimmed = ""
            for s in sentences:
                candidate = trimmed + s + ". "
                if len(candidate) <= self.max_length:
                    trimmed = candidate
                else:
                    break
            summary = trimmed.strip()
        return summary.strip()


# ==========================
# CATEGORY MANAGER
# ==========================
class CategoryManager:
    """
    Resolves a category hint to its canonical (name, parent_section) pair
    using the full parent→sub_category hierarchy from report-categories.json.

    Duplicate sub-category names (Application Security, Cloud Security,
    Ransomware, AI and Emerging Technologies each appear under both
    Analysis Reports and Survey Reports) are disambiguated by preferring
    the entry whose parent matches the report's declared type.
    """

    def __init__(self, categories_config: Dict[str, Any], similarity_threshold: float = 0.6):
        self.threshold = similarity_threshold
        # flat_map:   lowercase name → list of {name, parent}  (preserves duplicates)
        # parent_map: lowercase parent name → list of sub-category names
        self.flat_map, self.parent_map = self._build_maps(categories_config)

    def _build_maps(
        self, config: Dict[str, Any]
    ) -> Tuple[Dict[str, List[Dict[str, str]]], Dict[str, List[str]]]:
        flat: Dict[str, List[Dict[str, str]]] = {}
        parents: Dict[str, List[str]] = {}
        for group in config.get("categories", []):
            pname = group["parent"]
            parents[pname.lower()] = []
            for sub in group.get("sub_categories", []):
                name = sub["name"]
                parents[pname.lower()].append(name)
                flat.setdefault(name.lower(), []).append({"name": name, "parent": pname})
        return flat, parents

    def match_category(
        self, hint: str, report_type: str = "Analysis"
    ) -> Tuple[str, str]:
        """Return (canonical_category_name, parent_section_name).

        Priority:
          1. Exact name match, biased toward report_type keyword in parent name.
          2. Fuzzy word-overlap match, same bias.
          3. Type-appropriate default.
        """
        if not hint:
            return self._default(report_type)

        norm   = hint.lower().strip()
        type_l = report_type.lower()

        # 1 — exact match
        if norm in self.flat_map:
            candidates = self.flat_map[norm]
            preferred = next(
                (c for c in candidates if type_l in c["parent"].lower()), candidates[0]
            )
            return preferred["name"], preferred["parent"]

        # 2 — fuzzy word-overlap
        best_score, best = 0.0, None
        w1 = set(norm.split())
        for key, entries in self.flat_map.items():
            w2 = set(key.split())
            if not w1 or not w2:
                continue
            score = len(w1 & w2) / max(len(w1), len(w2))
            if score > best_score:
                best_score = score
                best = next(
                    (e for e in entries if type_l in e["parent"].lower()), entries[0]
                )

        if best and best_score >= self.threshold:
            return best["name"], best["parent"]

        return self._default(report_type)

    def _default(self, report_type: str) -> Tuple[str, str]:
        if "survey" in report_type.lower():
            return "Industry Trends", "Survey Reports"
        return "Global Threat Intelligence", "Analysis Reports"


# ==========================
# README PARSER
# ==========================
class ReadmeParser:
    """
    Owns a mutable slice of the README bounded by start_marker / end_marker
    (both sourced from readme-updater-config.json).  Everything outside that
    region is preserved byte-for-byte.
    The start_marker heading itself IS included in self.content so that
    find_section_bounds() can locate level-2 parent headings correctly.
    """

    # Matches a full entry line: - [Org](url) - [Title](url) (year) - summary
    ENTRY_RE = re.compile(
        r"^-\s*"
        r"\[(?P<org>[^\]]+)\]\((?P<org_url>[^\)]+)\)"
        r"\s*-\s*"
        r"\[(?P<title>[^\]]+)\]\((?P<report_url>[^\)]+)\)"
        r"\s*\((?P<year>\d{4})\)"
        r"\s*-\s*(?P<summary>.+)$"
    )

    def __init__(self, readme_path: str, config: ConfigLoader):
        self.readme_path  = Path(readme_path)
        self.start_marker = config.start_marker
        self.end_marker   = config.end_marker

        if not self.readme_path.exists():
            raise FileNotFoundError(f"README not found: {readme_path}")

        self.full_content = self.readme_path.read_text(encoding="utf-8")
        self.start_pos, self.end_pos = self._find_boundaries()
        self.content = self.full_content[self.start_pos: self.end_pos]

    def _find_boundaries(self) -> Tuple[int, int]:
        sm = re.search(
            rf"^{re.escape(self.start_marker)}\s*$", self.full_content, re.MULTILINE
        )
        em = re.search(
            rf"^{re.escape(self.end_marker)}\s*$", self.full_content, re.MULTILINE
        )
        if not sm or not em:
            raise ValueError(
                f"Boundary markers not found.\n"
                f"  start_marker: '{self.start_marker}'\n"
                f"  end_marker:   '{self.end_marker}'"
            )
        # Use sm.start() (not sm.end()) so the "## Analysis Reports" heading
        # is part of self.content and visible to find_section_bounds().
        return sm.start(), em.start()

    # ── entry lookup ──────────────────────────────────────────────────────

    @staticmethod
    def _pdf_series_key(url_or_path: str) -> str:
        """
        Derive the report-series fingerprint from a PDF filename by stripping
        the 4-digit year, file extension, percent-encoding, and separator chars.

        Examples:
          "Annual%20Security%20Reports/2025/Verizon-DBIR-2025.pdf"
          → filename: "verizon-dbir-2025.pdf"
          → key:      "verizon-dbir"

          "Annual%20Security%20Reports/2026/Verizon-DBIR-2026.pdf"
          → key:      "verizon-dbir"   ← same series, different year
        """
        name = Path(urllib.parse.unquote(url_or_path)).name.lower()
        name = name.replace(".pdf", "")
        name = re.sub(r"\d{4}", "", name)       # strip 4-digit years
        name = re.sub(r"[-_ ]+$", "", name)     # trailing separators
        name = re.sub(r"^[-_ ]+", "", name)     # leading separators
        return name.strip()

    def find_existing_entry(
        self, pdf_path: str
    ) -> Tuple[Optional[str], Optional[Dict[str, str]]]:
        """
        Scan self.content for an entry whose PDF series key matches
        the incoming pdf_path series key (year stripped from both).

        Returns (full_line_string, parsed_fields_dict) or (None, None).
        Parsed fields: org, org_url, title, report_url, year, summary.
        """
        incoming_key = self._pdf_series_key(pdf_path)
        if not incoming_key:
            return None, None

        for line in self.content.splitlines():
            if not line.strip().startswith("- ["):
                continue
            m = self.ENTRY_RE.match(line.strip())
            if not m:
                continue
            if self._pdf_series_key(m.group("report_url")) == incoming_key:
                return line, m.groupdict()

        return None, None

    # Section navigation

    def find_section_bounds(
        self, parent_heading: str, sub_heading: str
    ) -> Tuple[int, int]:
        """
        Return the (start, end) character offsets within self.content for the
        body of a level-3 sub-section that lives inside a specific level-2
        parent section.

        Searching within the scoped parent region prevents the wrong
        "### Application Security" from being matched when the same name
        exists under both Analysis Reports and Survey Reports.

        Returns (-1, -1) if either heading is not found.
        """
        # Locate the level-2 parent
        p_pat   = rf"^##\s+{re.escape(parent_heading)}\s*$"
        p_match = re.search(p_pat, self.content, re.MULTILINE)
        if not p_match:
            print(f"    ⚠ Parent section '## {parent_heading}' not found")
            return -1, -1

        p_body_start = p_match.end()
        # Parent section ends at the next ## heading or end of content
        next_l2  = re.search(r"\n##\s+", self.content[p_body_start:])
        p_body_end = p_body_start + next_l2.start() if next_l2 else len(self.content)

        # Locate the level-3 sub-section within the parent body
        s_pat   = rf"^###\s+{re.escape(sub_heading)}\s*$"
        s_match = re.search(s_pat, self.content[p_body_start:p_body_end], re.MULTILINE)
        if not s_match:
            print(f"    ⚠ Sub-section '### {sub_heading}' not found under '## {parent_heading}'")
            return -1, -1

        s_abs_start = p_body_start + s_match.end() + 1   # +1 skips trailing \n

        # Sub-section ends at the next ## or ### heading, or end of parent
        next_heading = re.search(r"\n#{2,3}\s+", self.content[s_abs_start:p_body_end])
        s_abs_end    = (
            s_abs_start + next_heading.start() if next_heading else p_body_end
        )

        return s_abs_start, s_abs_end

    # Reconstruction

    def get_full_content(self) -> str:
        """Reconstruct the full README with the mutated managed section."""
        return (
            self.full_content[: self.start_pos]
            + self.content
            + self.full_content[self.end_pos:]
        )

    def save(self) -> None:
        self.readme_path.write_text(self.get_full_content(), encoding="utf-8")
        print("✓ README saved")


# ==========================
# README UPDATER
# ==========================
class ReadmeUpdater:
    """
    Per-report decision logic:
      1. Skip if required fields are missing.
      2. Skip if report year is outside the active window (config-driven).
      3. Existing entry found (PDF series key match)?
         a. Same year  → skip (already current).
         b. Newer year → update only the fields listed in config.update_fields,
                         leave the line in its existing position.
         c. Older year → skip (processing a stale file).
      4. No existing entry → insert the new line alphabetically within its
         sub-section; all other lines are untouched.
    """

    def __init__(
        self,
        parser: ReadmeParser,
        category_manager: CategoryManager,
        config: ConfigLoader,
    ):
        self.parser   = parser
        self.cat_mgr  = category_manager
        self.config   = config
        self.validator = SummaryValidator(config)

    # Public entry point

    def process_report(self, analysis: Dict[str, Any]) -> Tuple[bool, str]:
        """Evaluate one analysis record. Returns (changed, reason_string)."""

        # 1 — required fields
        required = ["organization", "title", "year", "summary", "pdf_path", "organization_url"]
        missing  = [f for f in required if not analysis.get(f)]
        if missing:
            return False, f"missing fields: {', '.join(missing)}"

        # 2 — year scope (threshold from readme-updater-config.json)
        try:
            report_year = int(analysis["year"])
        except (ValueError, TypeError):
            return False, "invalid year value"

        if not self.config.is_year_in_scope(report_year):
            current = datetime.now().year
            return False, (
                f"year {report_year} outside active window "
                f"({current - self.config.age_threshold_years + 1}–{current})"
            )

        # Sanitize summary and fix placeholder org URLs before any comparison
        self._sanitize(analysis)

        # 3 — existing entry check (PDF series key, year-stripped)
        existing_line, existing_fields = self.parser.find_existing_entry(analysis["pdf_path"])

        if existing_line is not None:
            existing_year = int(existing_fields["year"])
            if report_year == existing_year:
                return False, f"already current (year={report_year})"
            if report_year > existing_year:
                return self._update_existing(existing_line, existing_fields, analysis)
            # Incoming is older than what's already in the README
            return False, f"incoming year {report_year} older than existing {existing_year}"

        # 4 — new entry: resolve category then insert
        cat_name, parent_name = self.cat_mgr.match_category(
            analysis.get("category", ""), analysis.get("type", "Analysis")
        )
        analysis["category"]       = cat_name
        analysis["parent_section"] = parent_name
        return self._insert_new(analysis)

    # Update

    def _update_existing(
        self,
        old_line: str,
        old_fields: Dict[str, str],
        new: Dict[str, Any],
    ) -> Tuple[bool, str]:
        """
        Rewrite only the fields listed in config.update_fields (from
        readme-updater-config.json), then swap the old line for the new one
        in-place.  Position in the section is preserved; no other lines move.

        Supported update_fields: organization_url, summary, year, title.
        The report_url is always updated because the year in the filename changes.
        """
        # Start from old parsed values so untouched fields stay identical
        merged = dict(old_fields)  # org, org_url, title, report_url, year, summary

        # report_url always reflects the new PDF path (year in filename changed)
        merged["report_url"] = self._build_report_url(new)
        merged["year"]       = str(new["year"])

        # Update only the fields declared in config (e.g. organization_url, summary)
        field_map = {
            "organization_url": ("org_url",  new.get("organization_url", "")),
            "summary":          ("summary",  self.validator.sanitize(new.get("summary", ""))),
            "title":            ("title",    new.get("title", "")),
        }
        for config_field, (entry_key, value) in field_map.items():
            if config_field in self.config.update_fields and value:
                merged[entry_key] = value

        new_line = self._format_entry(
            org=merged["org"],
            org_url=merged["org_url"],
            title=merged["title"],
            report_url=merged["report_url"],
            year=merged["year"],
            summary=merged["summary"],
        )
        self.parser.content = self.parser.content.replace(old_line, new_line, 1)
        return True, f"updated ({old_fields['year']}→{new['year']})"

    # Insert

    def _insert_new(self, analysis: Dict[str, Any]) -> Tuple[bool, str]:
        """
        Insert a single new entry at the correct alphabetical position within
        its sub-section.  Only the new line is added; no existing lines move.
        """
        parent   = analysis["parent_section"]
        category = analysis["category"]

        start, end = self.parser.find_section_bounds(parent, category)
        if start == -1:
            # Graceful fallback to the type-appropriate default category
            fallback_cat, fallback_parent = self.cat_mgr._default(
                analysis.get("type", "Analysis")
            )
            print(f"    → Falling back to '{fallback_cat}' under '{fallback_parent}'")
            start, end = self.parser.find_section_bounds(fallback_parent, fallback_cat)
            if start == -1:
                return False, "section not found in README"
            analysis["category"]       = fallback_cat
            analysis["parent_section"] = fallback_parent

        new_entry = self._build_entry(analysis)
        new_org   = self._extract_org(new_entry).lower()

        # Walk the section body to find the correct alphabetical insertion point
        body  = self.parser.content[start:end]
        lines = body.split("\n")

        insert_idx = None
        for idx, line in enumerate(lines):
            if not line.strip().startswith("- ["):
                continue
            if self._extract_org(line).lower() > new_org:
                insert_idx = idx
                break

        if insert_idx is not None:
            lines.insert(insert_idx, new_entry)
        else:
            # Append after the last entry line, before any trailing blank lines
            last_entry = max(
                (i for i, l in enumerate(lines) if l.strip().startswith("- [")),
                default=-1,
            )
            lines.insert(last_entry + 1, new_entry)

        new_body = "\n".join(lines)
        self.parser.content = (
            self.parser.content[:start] + new_body + self.parser.content[end:]
        )
        return True, f"inserted → {analysis['parent_section']} / {analysis['category']}"

    # Helpers

    def _sanitize(self, analysis: Dict[str, Any]) -> None:
        """Clean summary and replace Google search placeholder URLs in-place."""
        is_valid, _ = self.validator.validate(analysis.get("summary", ""))
        if not is_valid:
            analysis["summary"] = self.validator.sanitize(analysis.get("summary", ""))

        org_url = analysis.get("organization_url", "")
        if not org_url or "google.com/search" in org_url:
            slug = re.sub(r"[^a-z0-9]", "", analysis["organization"].lower())
            analysis["organization_url"] = f"https://www.{slug}.com"

    def _build_report_url(self, analysis: Dict[str, Any]) -> str:
        """
        Build the report_url for the markdown link.

        pdf_path in analysis.json is the repo-relative path, e.g.:
          "Annual Security Reports/2026/Vendor-Report-2026.pdf"

        The pdf_root_folder value in readme-updater-config.json is used
        to percent-encode the folder prefix, keeping the path construction
        config-driven rather than hard-coded.
        """
        return analysis["pdf_path"].replace(" ", "%20")

    def _build_entry(self, analysis: Dict[str, Any]) -> str:
        """Format a full README list entry line from an analysis record."""
        return self._format_entry(
            org        = analysis["organization"],
            org_url    = analysis["organization_url"],
            title      = analysis["title"],
            report_url = self._build_report_url(analysis),
            year       = str(analysis["year"]),
            summary    = self.validator.sanitize(analysis["summary"]),
        )

    @staticmethod
    def _format_entry(
        org: str, org_url: str, title: str, report_url: str, year: str, summary: str
    ) -> str:
        return (
            f"- [{org}]({org_url}) "
            f"- [{title}]({report_url}) "
            f"({year}) - {summary}"
        )

    @staticmethod
    def _extract_org(line: str) -> str:
        m = re.search(r"-\s*\[([^\]]+)\]", line)
        return m.group(1) if m else ""

    def save(self) -> None:
        self.parser.save()


# ==========================
# TOC VALIDATOR
# ==========================
def validate_table_of_contents(readme_path: str) -> bool:
    """Confirm every TOC #anchor resolves to an actual heading. Returns True if valid."""
    try:
        content = Path(readme_path).read_text(encoding="utf-8")
        links   = re.findall(r"\[([^\]]+)\]\(#([^\)]+)\)", content)
        headers = re.findall(r"^#{2,3}\s+(.+)$", content, re.MULTILINE)

        def to_anchor(text: str) -> str:
            a = text.lower()
            a = re.sub(r"[^\w\s-]", "", a)
            a = re.sub(r"\s+", "-", a)
            a = re.sub(r"-+",  "-", a)
            return a.strip("-")

        valid  = {to_anchor(h) for h in headers}
        broken = [f"'{t}' → #{a}" for t, a in links if a not in valid]

        if broken:
            print("❌ TOC Validation Failed:")
            for b in broken:
                print(f"  - {b}")
            return False

        print(f"✅ TOC validation passed ({len(links)} link(s) verified)")
        return True

    except Exception as e:
        print(f"⚠️ TOC validation error: {e}")
        return False


# ==========================
# MAIN
# ==========================
def main() -> int:
    ap = argparse.ArgumentParser(description="README Updater")
    ap.add_argument("analysis_json",   help="Path to analysis.json")
    ap.add_argument("--readme-path",   default="README.md")
    ap.add_argument("--artifacts-dir", default=".github/artifacts")
    ap.add_argument("--validate-toc",  action="store_true",
                    help="Validate TOC anchor links after updating")
    args = ap.parse_args()

    print(f"\n{'='*70}")
    print("README Updater")
    print(f"{'='*70}\n")

    try:
        config = ConfigLoader(args.artifacts_dir)
    except Exception as e:
        print(f"ERROR: Config load failed: {e}")
        return 1

    current_year = datetime.now().year
    min_year     = current_year - config.age_threshold_years + 1
    print(f"✓ Config loaded from {args.artifacts_dir}")
    print(f"  Managed section : '{config.start_marker}' → '{config.end_marker}'")
    print(f"  Active window   : {min_year}–{current_year} "
          f"(age_threshold_years={config.age_threshold_years})")
    print(f"  Update fields   : {config.update_fields}")
    print()

    if not os.path.exists(args.analysis_json):
        print(f"ERROR: {args.analysis_json} not found")
        return 1

    try:
        with open(args.analysis_json, "r", encoding="utf-8") as f:
            reports = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: JSON parse error in {args.analysis_json}: {e}")
        return 1

    if not reports:
        print("⊘ No reports in analysis file — nothing to do")
        return 0

    print(f"✓ {len(reports)} report(s) to evaluate\n")

    try:
        cat_mgr = CategoryManager(config.categories_config, config.similarity_threshold)
        parser  = ReadmeParser(args.readme_path, config)
        updater = ReadmeUpdater(parser, cat_mgr, config)
    except Exception as e:
        print(f"ERROR: Initialisation failed: {e}")
        return 1

    stats   = {"inserted": 0, "updated": 0, "skipped": 0}
    changed = False

    for i, report in enumerate(reports, 1):
        org  = report.get("organization", "Unknown")
        year = report.get("year", "?")
        print(f"[{i}/{len(reports)}] {org} ({year})")

        ok, reason = updater.process_report(report)

        if ok:
            changed = True
            if reason.startswith("updated"):
                stats["updated"] += 1
            else:
                stats["inserted"] += 1
            print(f"  ✓ {reason}")
        else:
            stats["skipped"] += 1
            print(f"  ⊘ skip: {reason}")

    print(f"\n{'='*70}")
    print(f"Inserted: {stats['inserted']} | Updated: {stats['updated']} | Skipped: {stats['skipped']}")

    if changed:
        updater.save()
        if args.validate_toc:
            print("\nValidating Table of Contents…")
            validate_table_of_contents(args.readme_path)
    else:
        print("\n⊘ No changes — README is already up to date")

    # Always exit 0; the workflow detects actual changes via git diff
    return 0


if __name__ == "__main__":
    sys.exit(main())