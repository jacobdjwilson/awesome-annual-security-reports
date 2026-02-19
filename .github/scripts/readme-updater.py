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
    Matches report categories from report-categories.json.

    Maintains the full parent → sub-category hierarchy so that
    duplicate sub-category names (Application Security, Cloud Security,
    Ransomware, AI and Emerging Technologies — which exist under both
    Analysis Reports and Survey Reports) resolve to the correct parent.
    """

    def __init__(self, categories_config: Dict[str, Any], similarity_threshold: float = 0.6):
        self.threshold = similarity_threshold
        # Build two maps:
        #   flat_map:    lowercase name → list of {name, parent} (handles duplicates)
        #   parent_map:  lowercase parent → list of sub-category names
        self.flat_map, self.parent_map = self._build_maps(categories_config)

    def _build_maps(
        self, config: Dict[str, Any]
    ) -> Tuple[Dict[str, List[Dict[str, str]]], Dict[str, List[str]]]:
        flat: Dict[str, List[Dict[str, str]]] = {}
        parents: Dict[str, List[str]] = {}
        for parent_cat in config.get("categories", []):
            parent_name = parent_cat["parent"]
            parents[parent_name.lower()] = []
            for sub in parent_cat.get("sub_categories", []):
                name = sub["name"]
                parents[parent_name.lower()].append(name)
                entry = {"name": name, "parent": parent_name}
                key = name.lower()
                if key not in flat:
                    flat[key] = []
                flat[key].append(entry)
        return flat, parents

    def match_category(
        self, hint: str, report_type: str = "Analysis", parent_section: str = ""
    ) -> Tuple[str, str]:
        """
        Match a category hint to a known category.

        Priority:
          1. Exact name match within the parent_section (if provided).
          2. Exact name match biased by report_type keyword.
          3. Fuzzy word-overlap match, same bias.
          4. Type-appropriate default.

        Returns (category_name, parent_name).
        """
        if not hint:
            return self._default(report_type)

        normalized = hint.lower().strip()

        # 1. Exact match constrained to parent_section
        if parent_section:
            parent_lower = parent_section.lower()
            if parent_lower in self.parent_map:
                for name in self.parent_map[parent_lower]:
                    if name.lower() == normalized:
                        return name, parent_section

        # 2. Exact match biased by report_type
        if normalized in self.flat_map:
            candidates = self.flat_map[normalized]
            # Prefer candidate whose parent matches report_type
            type_lower = report_type.lower()
            for c in candidates:
                if type_lower in c["parent"].lower():
                    return c["name"], c["parent"]
            # Fall back to first candidate
            return candidates[0]["name"], candidates[0]["parent"]

        # 3. Fuzzy word-overlap across all categories
        best_score = 0.0
        best_match: Optional[Dict[str, str]] = None
        words1 = set(normalized.split())
        for key, cat_list in self.flat_map.items():
            words2 = set(key.split())
            if words1 and words2:
                score = len(words1 & words2) / max(len(words1), len(words2))
                if score > best_score:
                    best_score = score
                    # Prefer the candidate whose parent matches the type
                    type_lower = report_type.lower()
                    for c in cat_list:
                        if type_lower in c["parent"].lower():
                            best_match = c
                            break
                    if not best_match:
                        best_match = cat_list[0]

        if best_match and best_score >= self.threshold:
            return best_match["name"], best_match["parent"]

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
    Parses the section of README between start_marker and end_marker.
    All mutations happen within self.content; the rest of the file is untouched.

    Section structure (within the managed region):
        ## Analysis Reports          ← level-2 parent heading
        ### Global Threat Intel      ← level-3 sub-section
        - [Org](url) - [Title](pdf)  ← entry lines
        ...
        ## Survey Reports            ← level-2 parent heading
        ### Industry Trends          ← level-3 sub-section
        ...
    """

    def __init__(self, readme_path: str, config: ConfigLoader):
        self.readme_path = Path(readme_path)
        self.start_marker = config.start_marker
        self.end_marker = config.end_marker

        if not self.readme_path.exists():
            raise FileNotFoundError(f"README not found: {readme_path}")

        self.full_content = self.readme_path.read_text(encoding="utf-8")
        self.start_pos, self.end_pos = self._find_boundaries()
        self.content = self.full_content[self.start_pos: self.end_pos]

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
        return start_match.start(), end_match.start()

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

    def find_subsection_bounds(self, parent_heading: str, sub_heading: str) -> Tuple[int, int]:
        """
        Find the byte range within self.content for a level-3 sub-section
        that lives inside a specific level-2 parent section.

        This prevents the common mistake of finding the first ## Application Security
        heading when the target is the one under ## Survey Reports.

        Returns (content_start, content_end) or (-1, -1) if not found.
        """
        # Find the level-2 parent section first
        parent_pattern = rf"^##\s+{re.escape(parent_heading)}\s*$"
        parent_match = re.search(parent_pattern, self.content, re.MULTILINE)
        if not parent_match:
            print(f"    ⚠ Parent section '## {parent_heading}' not found in README")
            return -1, -1

        parent_start = parent_match.end()

        # Find the end of this level-2 section (next ## heading or EOF)
        next_l2 = re.search(r"\n##\s+", self.content[parent_start:])
        parent_end = parent_start + next_l2.start() if next_l2 else len(self.content)

        # Within the parent section, locate the level-3 sub-section
        sub_pattern = rf"^###\s+{re.escape(sub_heading)}\s*$"
        sub_match = re.search(sub_pattern, self.content[parent_start:parent_end], re.MULTILINE)
        if not sub_match:
            print(f"    ⚠ Sub-section '### {sub_heading}' not found under '## {parent_heading}'")
            return -1, -1

        sub_abs_start = parent_start + sub_match.end() + 1  # skip the newline after heading

        # End of this level-3 section: next ## or ### heading, or end of parent section
        next_heading = re.search(r"\n#{2,3}\s+", self.content[sub_abs_start:parent_end])
        sub_abs_end = (
            sub_abs_start + next_heading.start()
            if next_heading
            else parent_end
        )

        return sub_abs_start, sub_abs_end

    def get_full_content(self) -> str:
        """Reconstruct the full README with updated content section."""
        return self.full_content[: self.start_pos] + self.content + self.full_content[self.end_pos:]


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

        # Resolve category and parent section
        parent_section_hint = analysis.get("parent_section", "")
        cat_name, parent_name = self.category_manager.match_category(
            analysis.get("category", ""),
            analysis.get("type", "Analysis"),
            parent_section=parent_section_hint,
        )
        analysis["category"] = cat_name
        analysis["parent_section"] = parent_name

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
        """
        Replace an existing README entry with updated data.
        The new entry stays in the same line position so ordering is preserved.
        """
        new_line = self._build_entry(new)
        self.parser.content = self.parser.content.replace(old_line, new_line)
        return True, f"updated ({old_year}→{new['year']}, {match_type})"

    def _insert_new(self, analysis: Dict[str, Any]) -> Tuple[bool, str]:
        """
        Insert a new entry into the correct sub-section under the correct
        parent section (Analysis Reports or Survey Reports).

        Uses find_subsection_bounds() which is parent-aware, preventing
        duplicate sub-heading names from landing in the wrong section.
        """
        parent_name = analysis["parent_section"]
        category = analysis["category"]

        start, end = self.parser.find_subsection_bounds(parent_name, category)

        if start == -1:
            # Attempt default category fallback within the same parent
            fallback_cat, fallback_parent = self.category_manager._default(analysis.get("type", "Analysis"))
            print(f"    → Falling back to '{fallback_cat}' under '{fallback_parent}'")
            start, end = self.parser.find_subsection_bounds(fallback_parent, fallback_cat)
            if start == -1:
                return False, "no_section"
            analysis["category"] = fallback_cat
            analysis["parent_section"] = fallback_parent

        section_text = self.parser.content[start:end]
        entries = [l for l in section_text.split("\n") if l.strip().startswith("- [")]

        entries.append(self._build_entry(analysis))
        entries.sort(key=lambda x: self._extract_org(x).lower())

        new_section = "\n".join(entries) + "\n"
        self.parser.content = (
            self.parser.content[:start] + new_section + self.parser.content[end:]
        )
        return True, "new"

    def _build_entry(self, analysis: Dict[str, Any]) -> str:
        """
        Format a README list entry.

        The pdf_path in analysis.json is already the full relative path from
        the repo root, e.g. "Annual Security Reports/2025/Foo-Report-2025.pdf".
        It is used as-is for the link, with spaces percent-encoded.
        """
        # pdf_path is the repo-relative path; encode spaces for the markdown link
        pdf_path = analysis["pdf_path"]
        report_url = pdf_path.replace(" ", "%20")

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
            missing = [f for f in required if not data.get(f)]
            print(f"    ⚠ Missing fields: {missing}")
            return False

        try:
            year = int(data["year"])
            current_year = datetime.now().year
            if current_year - year >= self.config.age_threshold_years:
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