import os
import sys
import json
import re
import argparse
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime
import time

# ==========================
# DEPENDENCY CHECKS
# ==========================
try:
    from googleapiclient.discovery import build
except ImportError:
    print("ERROR: google-api-python-client required")
    print("Install: pip install google-api-python-client")
    sys.exit(1)

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("ERROR: requests and beautifulsoup4 required")
    print("Install: pip install requests beautifulsoup4")
    sys.exit(1)


# ==========================
# CONFIGURATION LOADER
# ==========================
class ConfigLoader:
    """Loads configuration from .github/artifacts/"""

    PDF_ROOT = Path("Annual Security Reports")

    def __init__(self, artifacts_dir: str = ".github/artifacts"):
        self.artifacts_dir = Path(artifacts_dir)

        self.workflow_config = self._load_json("workflow-config.json")
        if not self.workflow_config:
            raise ValueError("workflow-config.json is required")

        # Discovery limits — sourced from workflow-config.json
        disc_config = self.workflow_config.get("workflow", {}).get("discovery", {})
        self.max_discoveries: int = disc_config.get("default_limit", 10)
        self.max_file_size_mb: int = disc_config.get("max_file_size_mb", 100)

    def _load_json(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load JSON file."""
        path = self.artifacts_dir / filename
        if not path.exists():
            print(f"ERROR: {filename} not found in {self.artifacts_dir}")
            return None

        try:
            with open(path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid JSON in {filename}: {e}")
            return None


# ==========================
# REPOSITORY LINEAGE INDEX
# ==========================
class ReportLineageIndex:
    """
    Builds an index of every PDF in the repository, keyed by a
    series fingerprint (org + normalised title, year-agnostic).

    This lets the discovery workflow answer:
      "Does the repository already contain year N+1 of this series?"

    without touching the README or GitHub issues — the source of truth
    is the file tree itself.

    Fingerprint format:  "<org_lower>|<normalised_title_lower>"
    Example: "microsoft|digital-defense-report"

    The index maps: fingerprint -> {year -> pdf_path}
    """

    YEAR_RE = re.compile(r"-(\d{4})\.pdf$", re.IGNORECASE)

    def __init__(self, pdf_root: Path):
        self.pdf_root = pdf_root
        # fingerprint -> dict[int, str]   (year -> repo-relative path)
        self.index: Dict[str, Dict[int, str]] = {}
        self._build()

    def _build(self):
        """Walk the PDF root and populate self.index."""
        if not self.pdf_root.exists():
            print(f"WARNING: PDF root not found: {self.pdf_root}")
            return

        for pdf_file in self.pdf_root.rglob("*.pdf"):
            year_match = self.YEAR_RE.search(pdf_file.name)
            if not year_match:
                continue  # Skip files without a year suffix

            year = int(year_match.group(1))
            stem = pdf_file.name[: year_match.start()]  # e.g. "Microsoft-Digital-Defense-Report"
            fp = self._fingerprint(stem)

            if fp not in self.index:
                self.index[fp] = {}
            self.index[fp][year] = str(pdf_file)

        total_series = len(self.index)
        total_files = sum(len(v) for v in self.index.values())
        print(f"Lineage index: {total_files} PDF(s) across {total_series} series")

    @staticmethod
    def _fingerprint(stem: str) -> str:
        """
        Normalise a filename stem (org-title, no year, no extension)
        to a case-insensitive, separator-agnostic key.
        e.g. "Microsoft-Digital-Defense-Report" -> "microsoft|digital-defense-report"
        """
        parts = stem.split("-", 1)
        org = parts[0].lower().strip()
        title = parts[1].lower().strip() if len(parts) > 1 else ""
        # Collapse multiple separators and strip trailing separators
        title = re.sub(r"[-_ ]+", "-", title).strip("-")
        return f"{org}|{title}"

    def next_year_exists(self, stem: str, current_year: int) -> bool:
        """
        Return True if year (current_year + 1) already exists in the repo
        for the series identified by this stem.
        """
        fp = self._fingerprint(stem)
        return (current_year + 1) in self.index.get(fp, {})

    def get_years(self, stem: str) -> List[int]:
        """Return all years present in the repo for a given series stem."""
        fp = self._fingerprint(stem)
        return sorted(self.index.get(fp, {}).keys())


# ==========================
# REPORT SCANNER
# ==========================
class ReportScanner:
    """
    Scans the repository for historical reports and determines which ones
    need a newer-year search, using the lineage index as the source of truth.

    A report qualifies for a search when:
      1. Its year is strictly less than the current calendar year (not brand-new).
      2. The next year's version does NOT already exist in the repository file tree.

    Only the most-recent version of each series is returned, so a series with
    both a 2022 and 2023 version only generates one search (for 2024), not two.
    """

    def __init__(self, config: ConfigLoader, lineage: ReportLineageIndex):
        self.config = config
        self.lineage = lineage
        self.current_year = datetime.now().year

    def scan_repository(self) -> List[Dict[str, Any]]:
        """
        Return reports that are missing their next-year update in the repo.
        Skips series where year+1 is already present in Annual Security Reports/.
        """
        if not self.config.PDF_ROOT.exists():
            print(f"ERROR: PDF root not found: {self.config.PDF_ROOT}")
            return []

        print(f"Scanning {self.config.PDF_ROOT}...")

        # Collect the most-recent year for each series
        series_latest: Dict[str, Dict[str, Any]] = {}
        skipped_existing = 0

        for pdf_file in self.config.PDF_ROOT.rglob("*.pdf"):
            report = self._parse_report(pdf_file)
            if not report:
                continue

            # Only consider reports that are not already current-year
            if report["year"] >= self.current_year:
                continue

            # Skip if the next year is already present in the repo file tree
            if self.lineage.next_year_exists(report["stem"], report["year"]):
                skipped_existing += 1
                continue

            # Keep only the most recent version of each series for searching
            key = report["stem"]
            if key not in series_latest or report["year"] > series_latest[key]["year"]:
                series_latest[key] = report

        reports = list(series_latest.values())
        print(f"  {skipped_existing} series skipped — next year already in repo")
        print(f"  {len(reports)} series without a next-year version in the repository")
        return reports

    def _parse_report(self, pdf_path: Path) -> Optional[Dict[str, Any]]:
        """Parse report metadata from filename."""
        filename = pdf_path.name
        year_match = re.search(r"-(\d{4})\.pdf$", filename)
        if not year_match:
            return None

        year = int(year_match.group(1))
        stem = filename[: year_match.start()]   # e.g. "Microsoft-Digital-Defense-Report"
        parts = stem.split("-", 1)

        return {
            "org":   parts[0],
            "title": parts[1] if len(parts) >= 2 else "Security Report",
            "year":  year,
            "stem":  stem,
            "path":  str(pdf_path),
        }


# ==========================
# GOOGLE SEARCH
# ==========================
class GoogleSearcher:
    """Searches for updated report versions using Google Custom Search."""

    EXCLUDE_TERMS   = ["job", "career", "hiring", "stock", "investor", "earnings"]
    FINANCIAL_TERMS = ["annual report", "financial results", "quarterly"]

    def __init__(self, api_key: str, cse_id: str):
        self.service = build("customsearch", "v1", developerKey=api_key)
        self.cse_id  = cse_id

    def search_for_update(self, report: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Search for a newer version of the given report."""
        next_year = report["year"] + 1
        query = f"{report['org']} {report['title']} {next_year} security report filetype:pdf"

        print(f"  Searching: {report['org']} {report['title']} {next_year}...")

        try:
            result = self.service.cse().list(
                q=query, cx=self.cse_id, num=5
            ).execute()

            for item in result.get("items", []):
                if self._is_valid_result(item, next_year):
                    return {
                        "url":     item["link"],
                        "title":   item["title"],
                        "snippet": item.get("snippet", ""),
                        "year":    next_year,
                        "org":     report["org"],
                        "stem":    report["stem"],
                    }

            return None

        except Exception as e:
            print(f"  ! Search error: {str(e)[:80]}")
            return None

    def _is_valid_result(self, item: Dict[str, Any], year: int) -> bool:
        """Return True if the search result looks like a real security report."""
        url      = item["link"].lower()
        title    = item["title"].lower()
        snippet  = item.get("snippet", "").lower()
        combined = f"{title} {snippet}"

        for term in self.EXCLUDE_TERMS:
            if term in combined:
                return False

        for term in self.FINANCIAL_TERMS:
            if term in title:
                return False

        if str(year) not in url and str(year) not in title:
            return False

        if "report" not in title and "report" not in snippet:
            return False

        return True


# ==========================
# GITHUB ISSUE CREATOR
# ==========================
class IssueCreator:
    """Creates GitHub issues for newly discovered reports."""

    def __init__(self, token: str):
        self.headers = {
            "Authorization": f"token {token}",
            "Accept":        "application/vnd.github.v3+json",
        }
        self.repo = os.environ.get("GITHUB_REPOSITORY", "unknown/repo")

    def issue_exists(self, org: str, year: int) -> bool:
        """
        Check whether an open issue already exists for this org+year.

        This is a secondary guard — the primary deduplication is the file-tree
        lineage check in ReportScanner.  This prevents duplicate issues for
        the same candidate within a single run (e.g. across multiple search
        result pages) and catches edge cases where a report was recently
        discovered but not yet ingested.
        """
        try:
            response = requests.get(
                f"https://api.github.com/repos/{self.repo}/issues",
                headers=self.headers,
                params={"state": "open", "labels": "report-suggestion", "per_page": 100},
                timeout=15,
            )
            if response.status_code != 200:
                return False

            title_fragment = f"{org} {year}".lower()
            for issue in response.json():
                if title_fragment in issue.get("title", "").lower():
                    print(f"  ⊘ Issue already open for {org} {year}")
                    return True

            return False
        except Exception as e:
            print(f"  ! Could not check existing issues: {str(e)[:80]}")
            return False

    def create_issue(self, candidate: Dict[str, Any]) -> bool:
        """Create a GitHub issue for a newly discovered candidate report."""
        org  = candidate["org"]
        year = candidate["year"]

        if self.issue_exists(org, year):
            return False

        title = f"New Report: {org} {year}"
        body = (
            f"## 📄 New Security Report Discovered\n\n"
            f"**Organization:** {org}\n"
            f"**Year:** {year}\n"
            f"**URL:** {candidate['url']}\n\n"
            f"**Title:** {candidate['title']}\n\n"
            f"**Snippet:**\n> {candidate['snippet']}\n\n"
            f"---\n*Auto-discovered by the Security Report Discovery workflow*"
        )

        try:
            response = requests.post(
                f"https://api.github.com/repos/{self.repo}/issues",
                headers=self.headers,
                json={
                    "title":  title,
                    "body":   body,
                    "labels": ["report-suggestion", "automated"],
                },
                timeout=15,
            )

            if response.status_code == 201:
                print(f"  ✓ Created issue: {title}")
                return True
            else:
                print(f"  ! Failed to create issue: HTTP {response.status_code}")
                return False

        except Exception as e:
            print(f"  ! Error creating issue: {str(e)[:80]}")
            return False


# ==========================
# MAIN
# ==========================
def main():
    parser = argparse.ArgumentParser(description="Security Report Discovery")
    parser.add_argument("--artifacts-dir",   default=".github/artifacts")
    parser.add_argument("--max-discoveries", type=int, default=None)
    args = parser.parse_args()

    print(f"\n{'='*70}")
    print(f"Security Report Discovery")
    print(f"{'='*70}\n")

    # Load config
    try:
        config = ConfigLoader(args.artifacts_dir)
        print(f"✓ Config loaded")
    except Exception as e:
        print(f"ERROR: Config failed: {e}")
        return 1

    # Resolve limit: CLI flag > config default
    max_discoveries = (
        args.max_discoveries if args.max_discoveries is not None
        else config.max_discoveries
    )
    print(f"✓ Max discoveries: {max_discoveries}\n")

    # Check required credentials
    search_key = os.environ.get("GOOGLE_SEARCH_API_KEY")
    cse_id     = os.environ.get("GOOGLE_CSE_ID")
    gh_token   = os.environ.get("GH_TOKEN")

    if not search_key or not cse_id:
        print("ERROR: GOOGLE_SEARCH_API_KEY and GOOGLE_CSE_ID are required")
        return 1

    if not gh_token:
        print("ERROR: GH_TOKEN is required")
        return 1

    # Build file-tree lineage index — primary deduplication mechanism.
    # This replaces the old README / GitHub issues check: a report is only
    # a discovery candidate if its next year is absent from the file tree.
    print(f"{'='*70}")
    print("Building repository lineage index...")
    print(f"{'='*70}\n")
    lineage = ReportLineageIndex(config.PDF_ROOT)

    # Scan for series that lack a next-year version in the repo
    print()
    scanner = ReportScanner(config, lineage)
    reports = scanner.scan_repository()

    if not reports:
        print("\nAll report series already have up-to-date versions in the repository.")
        return 0

    print(f"\n{'='*70}")
    print(f"Searching for updates ({min(len(reports), 50)} series, limit {max_discoveries})")
    print(f"{'='*70}\n")

    searcher      = GoogleSearcher(search_key, cse_id)
    issue_creator = IssueCreator(gh_token)

    candidates: List[Dict[str, Any]] = []

    # Cap searches at 50 to avoid excessive API usage
    for i, report in enumerate(reports[:50], 1):
        if len(candidates) >= max_discoveries:
            break

        print(f"[{i}] {report['org']} ({report['year']})")
        candidate = searcher.search_for_update(report)

        if candidate:
            candidates.append(candidate)
            print(f"  ✓ Found candidate: {candidate['url'][:80]}")

        time.sleep(1)  # Respect API rate limits

    print(f"\n{'='*70}")
    print(f"Creating issues for {len(candidates)} candidate(s)")
    print(f"{'='*70}\n")

    created = 0
    skipped = 0
    for candidate in candidates:
        if issue_creator.create_issue(candidate):
            created += 1
        else:
            skipped += 1

    print(f"\n{'='*70}")
    print(f"✓ Created {created} new issue(s)")
    if skipped:
        print(f"⊘ Skipped {skipped} (issue already open)")
    print(f"{'='*70}")

    return 0


if __name__ == "__main__":
    sys.exit(main())