"""
Operational Purpose:
    Performs comprehensive structural audit of README.md against repository standards:
    identifies outdated reports past retention threshold, redundant multi-year entries,
    fuzzy duplicates, missing markdown conversions, and category keyword mismatches.

Required Environment Variables:
    None.

Outputs:
    .github/artifacts/readme_audit_findings.json: Structured findings across all audit dimensions.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json
    .github/artifacts/report-categories.json
    .github/artifacts/readme-updater-config.json
"""

import os
import re
import sys
import json
import difflib
import datetime
import argparse
from pathlib import Path
from collections import defaultdict
from typing import Dict, Any, List, Optional

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class ReadmeAuditConfigLoader:
    """Loads configuration artifacts for README audit with fail-fast validation."""

    def __init__(self, artifacts_dir: str = ".github/artifacts") -> None:
        self.artifacts_dir = Path(artifacts_dir)
        self.updater_cfg_path = self.artifacts_dir / "readme-updater-config.json"
        self.categories_cfg_path = self.artifacts_dir / "report-categories.json"
        self.workflow_cfg_path = self.artifacts_dir / "workflow-config.json"

        self.updater_cfg = self._load_json(self.updater_cfg_path)
        self.categories_cfg = self._load_json(self.categories_cfg_path)
        self.workflow_cfg = self._load_json(self.workflow_cfg_path)

    def _load_json(self, path: Path) -> Dict[str, Any]:
        if not path.exists():
            raise FileNotFoundError(f"Missing required artifact: '{path}'.")
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            raise ValueError(f"Failed to parse JSON artifact '{path}': {e}") from e

    @property
    def age_threshold_years(self) -> int:
        val = self.updater_cfg.get("processing", {}).get("age_threshold_years")
        if val is None:
            raise KeyError(f"Missing 'processing.age_threshold_years' in '{self.updater_cfg_path}'.")
        return int(val)

    @property
    def category_keywords(self) -> Dict[str, List[str]]:
        cats = self.categories_cfg.get("categories")
        if not isinstance(cats, list) or not cats:
            raise KeyError(f"Missing or empty 'categories' in '{self.categories_cfg_path}'.")

        cat_keywords: Dict[str, List[str]] = {}
        for parent in cats:
            for sub in parent.get("sub_categories", []):
                cat_keywords[sub["name"]] = sub.get("keywords", [])
        return cat_keywords

    @property
    def valid_years(self) -> List[int]:
        threshold = self.age_threshold_years
        current_year = datetime.datetime.now().year
        return list(range(current_year - threshold + 1, current_year + 1))

    @property
    def md_dir(self) -> Path:
        folder = self.workflow_cfg.get("workflow", {}).get("folders", {}).get("markdown_conversions", "Markdown Conversions")
        return Path(folder)


def parse_readme(readme_path: Path) -> List[Dict[str, Any]]:
    if not readme_path.exists():
        raise FileNotFoundError(f"README file not found: '{readme_path}'.")

    with open(readme_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    entries: List[Dict[str, Any]] = []
    current_category: Optional[str] = None
    category_regex = re.compile(r"^###\s+(.*)$")
    entry_regex = re.compile(r"^-\s+\[(.*?)\]\((.*?)\)\s+-\s+\[(.*?)\]\((.*?)\)\s+\((\d{4})\)\s+-\s+(.*)$")

    for i, line in enumerate(lines):
        s_line = line.strip()
        cat_match = category_regex.match(s_line)
        if cat_match:
            current_category = cat_match.group(1).strip()
            continue

        entry_match = entry_regex.match(s_line)
        if entry_match and current_category:
            entries.append({
                "line_number": i + 1,
                "category": current_category,
                "vendor": entry_match.group(1).strip(),
                "vendor_link": entry_match.group(2).strip(),
                "report_name": entry_match.group(3).strip(),
                "pdf_link": entry_match.group(4).strip(),
                "year": int(entry_match.group(5).strip()),
                "summary": entry_match.group(6).strip(),
            })

    return entries


def check_multiple_years_and_retention(entries: List[Dict[str, Any]], valid_years: List[int]) -> List[Dict[str, Any]]:
    grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for entry in entries:
        key = f"{entry['vendor'].lower()} - {entry['report_name'].lower()}"
        grouped[key].append(entry)

    findings: List[Dict[str, Any]] = []
    for key, group in grouped.items():
        group.sort(key=lambda x: x["year"], reverse=True)
        latest_year = group[0]["year"]

        if latest_year not in valid_years:
            findings.append({
                "type": "outdated_report",
                "vendor": group[0]["vendor"],
                "report_name": group[0]["report_name"],
                "latest_year": latest_year,
                "message": f"Latest year {latest_year} is older than allowed retention ({valid_years}). Should be removed.",
            })

        for entry in group[1:]:
            findings.append({
                "type": "duplicate_older_year",
                "vendor": entry["vendor"],
                "report_name": entry["report_name"],
                "year": entry["year"],
                "latest_year": latest_year,
                "message": f"Older year {entry['year']} present while {latest_year} exists. Should be removed.",
            })

    return findings


def check_fuzzy_duplicates(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    findings: List[Dict[str, Any]] = []
    texts = [f"{e['vendor']} - {e['report_name']}" for e in entries]
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            similarity = difflib.SequenceMatcher(None, texts[i].lower(), texts[j].lower()).ratio()
            if 0.85 < similarity < 1.0:
                findings.append({
                    "type": "fuzzy_duplicate",
                    "entry1": f"{texts[i]} ({entries[i]['year']})",
                    "entry2": f"{texts[j]} ({entries[j]['year']})",
                    "similarity": round(similarity, 2),
                    "message": "Potential duplicate with slightly different wording.",
                })
    return findings


def check_missing_reports(entries: List[Dict[str, Any]], valid_years: List[int], md_dir: Path) -> List[Dict[str, Any]]:
    findings: List[Dict[str, Any]] = []
    readme_files = set()
    for e in entries:
        pdf_path = e["pdf_link"]
        filename = Path(pdf_path).name
        md_filename = filename.replace(".pdf", ".md")
        readme_files.add(f"{e['year']}/{md_filename}")

    for year in valid_years:
        year_dir = md_dir / str(year)
        if not year_dir.exists():
            continue
        for md_file in year_dir.glob("*.md"):
            md_rel_path = f"{year}/{md_file.name}"
            if md_rel_path not in readme_files:
                findings.append({
                    "type": "missing_in_readme",
                    "file": md_rel_path,
                    "message": f"Markdown file {md_rel_path} exists within retention period but is not listed in README.md.",
                })
    return findings


def score_category(text: str, cat_keywords: Dict[str, List[str]]) -> Dict[str, int]:
    text_lower = text.lower()
    scores: Dict[str, int] = {}
    for cat, keywords in cat_keywords.items():
        score = 0
        for kw in keywords:
            score += len(re.findall(r"\b" + re.escape(kw.lower()) + r"\b", text_lower))
        scores[cat] = score
    return scores


def check_categories(
    entries: List[Dict[str, Any]],
    cat_keywords: Dict[str, List[str]],
    md_dir: Path,
) -> List[Dict[str, Any]]:
    findings: List[Dict[str, Any]] = []
    for e in entries:
        pdf_path = e["pdf_link"]
        filename = Path(pdf_path).name
        md_filename = filename.replace(".pdf", ".md")
        md_path = md_dir / str(e["year"]) / md_filename

        content = e["summary"]
        if md_path.exists():
            try:
                content += " " + md_path.read_text(encoding="utf-8", errors="ignore")[:5000]
            except Exception:
                pass

        scores = score_category(content, cat_keywords)
        if scores:
            best_cat = max(scores, key=scores.get)
            best_score = scores[best_cat]
            current_cat = e["category"]
            current_score = scores.get(current_cat, 0)

            if current_score == 0 and best_score > 2 and best_cat != current_cat:
                findings.append({
                    "type": "category_mismatch",
                    "vendor": e["vendor"],
                    "report_name": e["report_name"],
                    "current_category": current_cat,
                    "suggested_category": best_cat,
                    "message": f"Report might be miscategorized. Score for '{current_cat}' is {current_score}, but '{best_cat}' scored {best_score} based on keywords.",
                })

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit README.md against repository standards.")
    parser.add_argument("--readme-path", default="README.md", help="Path to README.md")
    parser.add_argument("--artifacts-dir", default=".github/artifacts", help="Path to artifacts directory")
    parser.add_argument("--output-findings", default=".github/artifacts/readme_audit_findings.json", help="Path to write audit findings")
    args = parser.parse_args()

    config = ReadmeAuditConfigLoader(artifacts_dir=args.artifacts_dir)
    cat_keywords = config.category_keywords
    valid_years = config.valid_years
    md_dir = config.md_dir

    entries = parse_readme(Path(args.readme_path))

    findings = {
        "multiple_years_retention": check_multiple_years_and_retention(entries, valid_years),
        "fuzzy_duplicates": check_fuzzy_duplicates(entries),
        "missing_reports": check_missing_reports(entries, valid_years, md_dir),
        "category_mismatches": check_categories(entries, cat_keywords, md_dir),
    }

    output_path = Path(args.output_findings)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(findings, f, indent=2)

    total_findings = sum(len(v) for v in findings.values())
    print(f"✓ Audit complete. Findings written to '{output_path}'.")
    if total_findings > 0:
        print(f"  Found {total_findings} potential issue(s).")
    else:
        print("  No issues found.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
