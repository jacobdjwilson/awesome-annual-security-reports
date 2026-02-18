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
    """Loads configuration from .github/artifacts/"""

    def __init__(self, artifacts_dir: str = ".github/artifacts"):
        self.artifacts_dir = Path(artifacts_dir)

        self.categories_config = self._load_json("report-categories.json")
        self.readme_config = self._load_json("readme-updater-config.json")

        if not self.categories_config:
            raise ValueError("report-categories.json is required")
        if not self.readme_config:
            raise ValueError("readme-updater-config.json is required")

        # Processing config
        proc = self.readme_config.get("processing", {})
        self.age_threshold_years: int = proc.get("age_threshold_years", 2)
        self.start_marker: str = proc.get("start_marker", "## Analysis Reports")
        self.end_marker: str = proc.get("end_marker", "## Resources")

        # Matching config
        matching = self.readme_config.get("matching", {})
        self.similarity_threshold: float = matching.get("similarity_threshold", 0.6)

        # Summary validation rules
        val = self.readme_config.get("validation", {}).get("summary", {})
        self.summary_max_length: int = val.get("max_length", 400)
        self.summary_min_length: int = val.get("min_length", 40)
        self.required_verbs: List[str] = [v.lower() for v in val.get("required_verbs", [])]
        self.forbidden_phrases: List[str] = [p.lower() for p in val.get("forbidden_phrases", [])]
        self.marketing_words: List[str] = [w.lower() for w in val.get("marketing_words", [])]

    def _load_json(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load JSON file."""
        path = self.artifacts_dir / filename
        if not path.exists():
            print(f"ERROR: {filename} not found")
            return None
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid JSON in {filename}: {e}")
            return None


# ==========================
# SUMMARY VALIDATOR
# ==========================
class SummaryValidator:
    """Validates and sanitizes report summaries."""

    def __init__(self, config: ConfigLoader):
        self.max_length = config.summary_max_length
        self.min_length = config.summary_min_length
        self.required_verbs = config.required_verbs
        self.forbidden_phrases = config.forbidden_phrases
        self.marketing_words = config.marketing_words

    def validate(self, summary: str) -> Tuple[bool, List[str]]:
        """Validate summary and return (is_valid, errors)."""
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
            errors.append(f"BadStart")

        if "(" in summary or ")" in summary or '"' in summary:
            errors.append("Quotes/Parens")

        summary_lower = summary.lower()
        for phrase in self.forbidden_phrases:
            if phrase in summary_lower:
                errors.append(f"ForbiddenPhrase:{phrase}")
        for word in self.marketing_words:
            if word in summary_lower:
                errors.append(f"MarketingWord:{word}")

        return len(errors) == 0, errors

    def sanitize(self, summary: str) -> str:
        """Fix common issues in a summary string."""
        if not summary:
            return ""

        # Collapse whitespace and remove problematic chars
        summary = " ".join(summary.split())
        summary = re.sub(r'[()"\']', "", summary)

        if summary and not summary.endswith("."):
            summary += "."

        # Trim to max_length by whole sentences
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
    Resolves (report_type, category_hint) → (canonical_name, parent_group_name).

    The README has subcategory names that appear under BOTH ## Analysis Reports
    and ## Survey Reports (e.g. "Application Security", "Cloud Security",
    "Ransomware", "AI and Emerging Technologies").  A flat map keyed only by
    the lowercase name loses this distinction and always returns the last entry
    written, which is whichever parent group appears second in the JSON.

    The fix: key the internal map by (parent_type, lower_name) so lookups are
    always scoped to the correct parent group first.
    """

    def __init__(self, categories_config: Dict[str, Any], similarity_threshold: float = 0.6):
        self.threshold = similarity_threshold
        # Map: (parent_type_key, lower_name) → {name, parent, parent_type}
        # parent_type_key is "analysis" or "survey"
        self._map: Dict[Tuple[str, str], Dict[str, str]] = {}
        self._build_map(categories_config)

    def _build_map(self, config: Dict[str, Any]) -> None:
        for parent_cat in config.get("categories", []):
            parent_name: str = parent_cat.get("parent", "")
            pt = "survey" if "survey" in parent_name.lower() else "analysis"
            for sub in parent_cat.get("sub_categories", []):
                name: str = sub.get("name", "")
                if name:
                    self._map[(pt, name.lower())] = {
                        "name": name,
                        "parent": parent_name,
                        "parent_type": pt,
                    }

    def match_category(self, hint: str, report_type: str = "Analysis") -> Tuple[str, str]:
        """
        Returns (canonical_category_name, parent_group_name).

        Lookup order:
          1. Exact match within the correct parent type.
          2. Fuzzy word-overlap within the correct parent type.
          3. Exact match across all types (last resort, prevents total failure).
          4. Built-in defaults.
        """
        pt = "survey" if "survey" in report_type.lower() else "analysis"

        if not hint:
            return self._default(pt)

        normalized = hint.lower().strip()

        # 1. Exact scoped match
        key = (pt, normalized)
        if key in self._map:
            m = self._map[key]
            return m["name"], m["parent"]

        # 2. Fuzzy scoped match
        words1 = set(normalized.split())
        best_score = 0.0
        best_match: Optional[Dict[str, str]] = None
        for (entry_pt, entry_name), info in self._map.items():
            if entry_pt != pt:
                continue
            words2 = set(entry_name.split())
            if words1 and words2:
                score = len(words1 & words2) / max(len(words1), len(words2))
                if score > best_score:
                    best_score = score
                    best_match = info

        if best_match and best_score >= self.threshold:
            return best_match["name"], best_match["parent"]

        # 3. Cross-type exact match (e.g. AI returns "Identity Security" for an Analysis report
        #    — it only exists under Survey, so accept it and correct the parent)
        for (entry_pt, entry_name), info in self._map.items():
            if entry_name == normalized:
                return info["name"], info["parent"]

        # 4. Default
        return self._default(pt)

    def _default(self, parent_type: str) -> Tuple[str, str]:
        if parent_type == "survey":
            return "Industry Trends", "Survey Reports"
        return "Global Threat Intelligence", "Analysis Reports"


# ==========================
# README PARSER
# ==========================
class ReadmeParser:
    """
    Parses the section of README between start_marker and end_marker.
    All mutations happen within self.content; the rest of the file is untouched.
    """

    def __init__(self, readme_path: str, config: ConfigLoader):
        self.readme_path = Path(readme_path)
        self.start_marker = config.start_marker
        self.end_marker = config.end_marker

        if not self.readme_path.exists():
            raise FileNotFoundError(f"README not found: {readme_path}")

        self.full_content = self.readme_path.read_text(encoding="utf-8")
        self.start_pos, self.end_pos = self._find_boundaries()
        self.content = self.full_content[self.start_pos : self.end_pos]

    def _find_boundaries(self) -> Tuple[int, int]:
        start_match = re.search(
            rf"^{re.escape(self.start_marker)}\s*$", self.full_content, re.MULTILINE
        )
        end_match = re.search(
            rf"^{re.escape(self.end_marker)}\s*$", self.full_content, re.MULTILINE
        )
        if not start_match or not end_match:
            raise ValueError(
                f"Boundary markers not found.\n"
                f"  start_marker: '{self.start_marker}'\n"
                f"  end_marker:   '{self.end_marker}'"
            )
        return start_match.end(), end_match.start()

    def find_existing_entry(
        self, org: str, title: str, pdf_path: str
    ) -> Tuple[Optional[str], Optional[int], Optional[str]]:
        """
        Search for an existing README entry using two signals:
          1. Org + normalized title match (catches category moves)
          2. PDF base filename match   (catches series year updates)

        Returns: (full_line, year, match_type) or (None, None, None)
        """
        org_lower = org.lower()
        title_normalized = self._normalize_title(title)

        pdf_filename = Path(pdf_path).name.lower()
        pdf_base = (
            re.sub(r"\d{4}", "", pdf_filename)
            .replace("%20", " ")
            .strip("-_ .")
            .replace(".pdf", "")
        )

        entry_re = re.compile(
            r"^-\s*\[([^\]]+)\]\(([^\)]+)\)\s*-\s*\[([^\]]+)\]\(([^\)]+)\)\s*\((\d{4})\)",
            re.MULTILINE,
        )

        for line in self.content.split("\n"):
            if not line.strip().startswith("- ["):
                continue

            m = entry_re.match(line.strip())
            if not m:
                continue

            curr_org = m.group(1).lower()
            curr_title = m.group(3)
            curr_report_url = m.group(4).lower()
            curr_year = int(m.group(5))

            # Priority 1: org + title
            if curr_org == org_lower and self._normalize_title(curr_title) == title_normalized:
                return line, curr_year, "org_title"

            # Priority 2: PDF base filename
            if (
                "annual%20security%20reports" in curr_report_url
                or "annual security reports" in curr_report_url
            ):
                curr_filename = Path(urllib.parse.unquote(curr_report_url)).name.lower()
                curr_base = (
                    re.sub(r"\d{4}", "", curr_filename)
                    .replace("%20", " ")
                    .strip("-_ .")
                    .replace(".pdf", "")
                )
                if pdf_base and curr_base and pdf_base == curr_base:
                    return line, curr_year, "pdf_filename"

        return None, None, None

    def _normalize_title(self, title: str) -> str:
        """Remove all non-alphanumeric characters and lowercase for comparison."""
        return re.sub(r"[^a-z0-9]", "", title.lower())

    def find_section_bounds(
        self,
        heading: str,
        level: int = 3,
        parent_heading: Optional[str] = None,
    ) -> Tuple[int, int]:
        """
        Return (start, end) character offsets within self.content for a subsection.

        When parent_heading is provided the search is restricted to the slice of
        content that falls under that ## block, preventing identically-named
        ### subsections (e.g. "Application Security" appears under both
        ## Analysis Reports and ## Survey Reports) from resolving to the wrong one.
        """
        search_content = self.content
        base_offset = 0

        if parent_heading:
            # Locate the ## parent block within self.content
            parent_pat = rf"^## {re.escape(parent_heading)}\s*$"
            parent_m = re.search(parent_pat, self.content, re.MULTILINE)
            if parent_m:
                # The block ends at the next ## heading or end-of-content
                after = self.content[parent_m.end():]
                next_h2 = re.search(r"\n## ", after)
                block_end = parent_m.end() + (next_h2.start() if next_h2 else len(after))
                search_content = self.content[parent_m.end():block_end]
                base_offset = parent_m.end()

        pattern = rf'^{"#" * level}\s+{re.escape(heading)}\s*$'
        match = re.search(pattern, search_content, re.MULTILINE)

        if not match:
            return -1, -1

        abs_start = base_offset + match.end() + 1  # character after the heading newline
        # End = start of the next heading at same-or-higher level in the search slice
        remaining = search_content[match.end():]
        next_heading = re.search(rf"\n#{{{1,{level}}}}\s+", remaining)
        abs_end = (base_offset + match.end() + next_heading.start()
                   if next_heading else base_offset + len(search_content))
        return abs_start, abs_end

    def get_full_content(self) -> str:
        """Reconstruct the full README with updated content section."""
        return self.full_content[: self.start_pos] + self.content + self.full_content[self.end_pos :]


# ==========================
# README UPDATER
# ==========================
class ReadmeUpdater:
    """Updates README entries for reports in the analysis file."""

    def __init__(
        self,
        parser: ReadmeParser,
        category_manager: CategoryManager,
        config: ConfigLoader,
    ):
        self.parser = parser
        self.category_manager = category_manager
        self.config = config
        self.validator = SummaryValidator(config)

    def process_report(self, analysis: Dict[str, Any]) -> Tuple[bool, str]:
        """
        Process a single analysis result.
        Returns: (success, action_description)
        """
        if not self._validate_data(analysis):
            return False, "invalid_data"

        # Sanitize summary
        is_valid, _ = self.validator.validate(analysis["summary"])
        if not is_valid:
            analysis["summary"] = self.validator.sanitize(analysis["summary"])

        # Replace Google search URLs with a best-guess org homepage
        org_url = analysis.get("organization_url", "")
        if "google.com/search" in org_url:
            slug = re.sub(r"[^a-z0-9]", "", analysis["organization"].lower())
            analysis["organization_url"] = f"https://www.{slug}.com"

        # Resolve category AND parent group — both are needed for correct section placement
        cat_name, parent_group = self.category_manager.match_category(
            analysis.get("category", ""), analysis.get("type", "Analysis")
        )
        analysis["category"] = cat_name
        analysis["parent_group"] = parent_group  # e.g. "Analysis Reports" or "Survey Reports"

        print(f"  → Type: {analysis.get('type')} | Category: {cat_name} | Parent: {parent_group}")

        # Check for existing entry
        existing_line, existing_year, match_type = self.parser.find_existing_entry(
            analysis["organization"], analysis["title"], analysis["pdf_path"]
        )

        if existing_line is not None:
            new_year = int(analysis["year"])
            if new_year > existing_year:
                return self._update_existing(existing_line, existing_year, analysis, match_type)
            else:
                return False, f"exists (year {existing_year}, matched by {match_type})"

        return self._insert_new(analysis)

    def _update_existing(
        self,
        old_line: str,
        old_year: int,
        new: Dict[str, Any],
        match_type: str,
    ) -> Tuple[bool, str]:
        """Replace an existing README entry with updated data."""
        new_line = self._build_entry(new)
        self.parser.content = self.parser.content.replace(old_line, new_line)
        return True, f"updated ({old_year}→{new['year']}, {match_type})"

    def _insert_new(self, analysis: Dict[str, Any]) -> Tuple[bool, str]:
        """Insert a new entry into the correct parent/category subsection."""
        category = analysis["category"]
        parent_group = analysis.get("parent_group", "")

        start, end = self.parser.find_section_bounds(category, parent_heading=parent_group)

        if start == -1:
            start, end = self.parser.find_section_bounds(category)

        if start == -1:
            if "survey" in analysis.get("type", "").lower():
                category = "Industry Trends"
                start, end = self.parser.find_section_bounds(
                    category, parent_heading="Survey Reports"
                )
            else:
                category = "Global Threat Intelligence"
                start, end = self.parser.find_section_bounds(
                    category, parent_heading="Analysis Reports"
                )

        if start == -1:
            return False, "no_section"

        section = self.parser.content[start:end]
        entries = [ln for ln in section.split("\n") if ln.strip().startswith("- [")]

        entries.append(self._build_entry(analysis))
        entries.sort(key=lambda x: self._extract_org(x).lower())

        new_section = "\n".join(entries) + "\n"
        self.parser.content = (
            self.parser.content[:start] + new_section + self.parser.content[end:]
        )
        return True, "new"

    def _build_entry(self, analysis: Dict[str, Any]) -> str:
        """Format a README list entry."""
        pdf_name = Path(analysis["pdf_path"]).name
        report_url = (
            f"Annual%20Security%20Reports/{analysis['year']}/{pdf_name}".replace(" ", "%20")
        )
        summary = self.validator.sanitize(analysis["summary"])
        return (
            f"- [{analysis['organization']}]({analysis['organization_url']}) "
            f"- [{analysis['title']}]({report_url}) "
            f"({analysis['year']}) - {summary}"
        )

    def _extract_org(self, line: str) -> str:
        m = re.search(r"-\s*\[([^\]]+)\]", line)
        return m.group(1) if m else ""

    def _validate_data(self, data: Dict[str, Any]) -> bool:
        """Check that all required fields are present and the report is recent enough."""
        required = ["organization", "title", "year", "summary", "pdf_path", "organization_url"]
        if any(not data.get(f) for f in required):
            return False

        try:
            year = int(data["year"])
            if datetime.now().year - year >= self.config.age_threshold_years:
                return False
        except (ValueError, TypeError):
            return False

        return True

    def save(self):
        """Write the updated README back to disk."""
        self.parser.readme_path.write_text(
            self.parser.get_full_content(), encoding="utf-8"
        )
        print(f"✓ README saved")


# ==========================
# TOC VALIDATOR
# ==========================
def validate_table_of_contents(readme_path: str) -> bool:
    """
    Validate that every TOC anchor link resolves to an actual section header.
    Only validates links in the TOC region (before the first ## section).
    Returns True if all links resolve correctly.
    """
    try:
        content = Path(readme_path).read_text(encoding="utf-8")

        toc_links = re.findall(r"\[([^\]]+)\]\(#([^\)]+)\)", content)
        headers = re.findall(r"^#{2,3}\s+(.+)$", content, re.MULTILINE)

        def to_anchor(text: str) -> str:
            anchor = text.lower()
            anchor = re.sub(r"[^\w\s-]", "", anchor)
            anchor = re.sub(r"\s+", "-", anchor)
            anchor = re.sub(r"-+", "-", anchor)
            return anchor.strip("-")

        valid_anchors = {to_anchor(h) for h in headers}

        missing = [
            f"'{text}' → #{anchor}"
            for text, anchor in toc_links
            if anchor not in valid_anchors
        ]

        if missing:
            print("❌ TOC Validation Failed:")
            for m in missing:
                print(f"  - {m}")
            return False

        print(f"✅ TOC validation passed ({len(toc_links)} link(s) verified)")
        return True

    except Exception as e:
        print(f"⚠️ TOC validation error: {e}")
        return False


# ==========================
# MAIN
# ==========================
def main():
    parser = argparse.ArgumentParser(description="README Updater")
    parser.add_argument("analysis_json", help="Path to analysis.json")
    parser.add_argument("--readme-path", default="README.md")
    parser.add_argument("--artifacts-dir", default=".github/artifacts")
    parser.add_argument(
        "--validate-toc",
        action="store_true",
        help="Validate Table of Contents anchors after updating",
    )
    args = parser.parse_args()

    print(f"\n{'='*70}")
    print(f"README Updater")
    print(f"{'='*70}\n")

    try:
        config = ConfigLoader(args.artifacts_dir)
        print(f"✓ Config loaded")
        print(f"  Section: '{config.start_marker}' → '{config.end_marker}'")
        print(f"  Age threshold: {config.age_threshold_years} year(s)\n")
    except Exception as e:
        print(f"ERROR: Config load failed: {e}")
        sys.exit(1)

    if not os.path.exists(args.analysis_json):
        print(f"ERROR: Analysis file not found: {args.analysis_json}")
        sys.exit(1)

    try:
        with open(args.analysis_json, "r") as f:
            analysis_reports = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: JSON decode error: {e}")
        sys.exit(1)

    if not analysis_reports:
        print("No reports in analysis file")
        sys.exit(0)

    print(f"✓ {len(analysis_reports)} report(s) to process\n")

    try:
        category_mgr = CategoryManager(
            config.categories_config, config.similarity_threshold
        )
        readme_parser = ReadmeParser(args.readme_path, config)
        updater = ReadmeUpdater(readme_parser, category_mgr, config)
    except Exception as e:
        print(f"ERROR: Initialization failed: {e}")
        sys.exit(1)

    stats = {"new": 0, "updated": 0, "skipped": 0}
    changes = False

    for i, analysis in enumerate(analysis_reports, 1):
        org = analysis.get("organization", "Unknown")
        print(f"[{i}/{len(analysis_reports)}] {org}")

        success, action = updater.process_report(analysis)

        if success:
            if "updated" in action:
                stats["updated"] += 1
            else:
                stats["new"] += 1
            changes = True
            print(f"  ✓ {action.upper()}")
        else:
            stats["skipped"] += 1
            print(f"  ⊘ SKIP: {action}")

    print(f"\n{'='*70}")
    print(f"New: {stats['new']} | Updated: {stats['updated']} | Skipped: {stats['skipped']}")

    if changes:
        updater.save()
        if args.validate_toc:
            print("\nValidating Table of Contents...")
            validate_table_of_contents(args.readme_path)
    else:
        print("\n⊘ No changes needed")

    # Exit 0 whether changes were made or not — the workflow checks git diff
    return 0


if __name__ == "__main__":
    sys.exit(main())