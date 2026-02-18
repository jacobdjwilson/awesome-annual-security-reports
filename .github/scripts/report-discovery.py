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
# REPORT SCANNER
# ==========================
class ReportScanner:
    """Scans repository for historical reports to check for newer versions."""

    def __init__(self, config: ConfigLoader):
        self.config = config
        self.current_year = datetime.now().year

    def scan_repository(self) -> List[Dict[str, Any]]:
        """Return all historical (non-current-year) reports found in the PDF root."""
        if not self.config.PDF_ROOT.exists():
            print(f"ERROR: PDF root not found: {self.config.PDF_ROOT}")
            return []

        print(f"Scanning {self.config.PDF_ROOT}...")
        reports = []

        for pdf_file in self.config.PDF_ROOT.rglob("*.pdf"):
            report = self._parse_report(pdf_file)
            if report and report["year"] < self.current_year:
                reports.append(report)

        print(f"✓ Found {len(reports)} historical report(s) to check")
        return reports

    def _parse_report(self, pdf_path: Path) -> Optional[Dict[str, Any]]:
        """Parse report metadata from filename."""
        filename = pdf_path.name
        year_match = re.search(r"-(\d{4})\.pdf$", filename)
        if not year_match:
            return None

        year = int(year_match.group(1))
        name = filename[: year_match.start()]
        parts = name.split("-", 1)

        return {
            "org": parts[0],
            "title": parts[1] if len(parts) >= 2 else "Security Report",
            "year": year,
            "path": str(pdf_path),
        }


# ==========================
# GOOGLE SEARCH
# ==========================
class GoogleSearcher:
    """Searches for updated report versions using Google Custom Search."""

    # Terms that indicate a result is not a security report
    EXCLUDE_TERMS = ["job", "career", "hiring", "stock", "investor", "earnings"]
    FINANCIAL_TERMS = ["annual report", "financial results", "quarterly"]

    def __init__(self, api_key: str, cse_id: str):
        self.service = build("customsearch", "v1", developerKey=api_key)
        self.cse_id = cse_id

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
                        "url": item["link"],
                        "title": item["title"],
                        "snippet": item.get("snippet", ""),
                        "year": next_year,
                        "org": report["org"],
                    }

            return None

        except Exception as e:
            print(f"  ! Search error: {str(e)[:80]}")
            return None

    def _is_valid_result(self, item: Dict[str, Any], year: int) -> bool:
        """Return True if the search result looks like a real security report."""
        url = item["link"].lower()
        title = item["title"].lower()
        snippet = item.get("snippet", "").lower()
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
            "Accept": "application/vnd.github.v3+json",
        }
        self.repo = os.environ.get("GITHUB_REPOSITORY", "unknown/repo")

    def issue_exists(self, org: str, year: int) -> bool:
        """Check whether an open issue already exists for this org+year."""
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
                    print(f"  ⊘ Issue already exists for {org} {year}")
                    return True

            return False
        except Exception as e:
            print(f"  ! Could not check existing issues: {str(e)[:80]}")
            return False

    def create_issue(self, candidate: Dict[str, Any]) -> bool:
        """Create a GitHub issue for a newly discovered candidate report."""
        org = candidate["org"]
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
                json={"title": title, "body": body, "labels": ["report-suggestion", "automated"]},
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
    parser.add_argument("--artifacts-dir", default=".github/artifacts")
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
    max_discoveries = args.max_discoveries if args.max_discoveries is not None else config.max_discoveries
    print(f"✓ Max discoveries: {max_discoveries}\n")

    # Check required credentials
    search_key = os.environ.get("GOOGLE_SEARCH_API_KEY")
    cse_id = os.environ.get("GOOGLE_CSE_ID")
    gh_token = os.environ.get("GH_TOKEN")

    if not search_key or not cse_id:
        print("ERROR: GOOGLE_SEARCH_API_KEY and GOOGLE_CSE_ID are required")
        return 1

    if not gh_token:
        print("ERROR: GH_TOKEN is required")
        return 1

    # Scan repository for historical reports
    scanner = ReportScanner(config)
    reports = scanner.scan_repository()

    if not reports:
        print("No historical reports found to check for updates")
        return 0

    print(f"\n{'='*70}")
    print(f"Searching for updates ({min(len(reports), 50)} reports, limit {max_discoveries})")
    print(f"{'='*70}\n")

    searcher = GoogleSearcher(search_key, cse_id)
    issue_creator = IssueCreator(gh_token)

    candidates = []
    # Cap searches at 50 to avoid excessive API usage
    for i, report in enumerate(reports[:50], 1):
        if len(candidates) >= max_discoveries:
            break

        print(f"[{i}] {report['org']} ({report['year']})")
        candidate = searcher.search_for_update(report)

        if candidate:
            candidates.append(candidate)
            print(f"  ✓ Found candidate!")

        time.sleep(1)  # Respect API rate limits

    print(f"\n{'='*70}")
    print(f"Creating issues for {len(candidates)} candidate(s)")
    print(f"{'='*70}\n")

    created = 0
    for candidate in candidates:
        if issue_creator.create_issue(candidate):
            created += 1

    print(f"\n{'='*70}")
    print(f"✓ Created {created} new issue(s)")
    print(f"{'='*70}")

    return 0


if __name__ == "__main__":
    sys.exit(main())