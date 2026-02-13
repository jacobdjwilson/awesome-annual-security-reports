import os
import sys
import json
import re
import argparse
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
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
    
    def __init__(self, artifacts_dir: str = ".github/artifacts"):
        self.artifacts_dir = Path(artifacts_dir)
        
        self.pipeline_config = self._load_json("pipeline-config.json")
        if not self.pipeline_config:
            raise ValueError("pipeline-config.json is REQUIRED")
        
        # Extract discovery config
        disc_config = self.pipeline_config.get("discovery", {})
        self.max_issues = disc_config.get("max_issues_per_run", 10)
        self.lookback_days = disc_config.get("lookback_days", 90)
        self.timeout = disc_config.get("timeout_seconds", 15)
        self.exclude_terms = disc_config.get("exclude_terms", [])
        self.financial_terms = disc_config.get("financial_terms", [])
        self.secondary_domains = disc_config.get("secondary_source_domains", [])
        
        # Repository paths
        repo_config = self.pipeline_config.get("repository", {})
        self.pdf_root = Path(repo_config.get("pdf_root", "Annual Security Reports"))
    
    def _load_json(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load JSON file."""
        path = self.artifacts_dir / filename
        if not path.exists():
            print(f"ERROR: {filename} not found")
            return None
        
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid JSON in {filename}: {e}")
            return None

# ==========================
# REPORT SCANNER
# ==========================
class ReportScanner:
    """Scans repository for historical reports."""
    
    def __init__(self, config: ConfigLoader):
        self.config = config
        self.current_year = datetime.now().year
    
    def scan_repository(self) -> List[Dict[str, Any]]:
        """Scan repository for historical reports."""
        reports = []
        
        if not self.config.pdf_root.exists():
            print(f"ERROR: PDF root not found: {self.config.pdf_root}")
            return reports
        
        print(f"Scanning {self.config.pdf_root}...")
        
        for pdf_file in self.config.pdf_root.rglob("*.pdf"):
            report = self._parse_report(pdf_file)
            if report and report['year'] < self.current_year:
                reports.append(report)
        
        print(f"✓ Found {len(reports)} historical reports")
        return reports
    
    def _parse_report(self, pdf_path: Path) -> Optional[Dict[str, Any]]:
        """Parse report metadata from filename."""
        filename = pdf_path.name
        
        # Extract year
        year_match = re.search(r'-(\d{4})\.pdf$', filename)
        if not year_match:
            return None
        
        year = int(year_match.group(1))
        
        # Extract org and title
        name = filename.replace('.pdf', '')
        name_without_year = name[:year_match.start()]
        
        parts = name_without_year.split('-', 1)
        if len(parts) >= 2:
            org = parts[0]
            title = parts[1]
        else:
            org = parts[0]
            title = "Security Report"
        
        return {
            'org': org,
            'title': title,
            'year': year,
            'path': str(pdf_path)
        }

# ==========================
# GOOGLE SEARCH
# ==========================
class GoogleSearcher:
    """Searches for updated reports using Google Custom Search."""
    
    def __init__(self, api_key: str, cse_id: str, config: ConfigLoader):
        self.api_key = api_key
        self.cse_id = cse_id
        self.config = config
        self.service = build("customsearch", "v1", developerKey=api_key)
    
    def search_for_update(self, report: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Search for updated version of report."""
        next_year = report['year'] + 1
        query = f"{report['org']} {report['title']} {next_year} security report"
        
        print(f"  Searching: {report['org']} {next_year}...")
        
        try:
            result = self.service.cse().list(
                q=query,
                cx=self.cse_id,
                num=3
            ).execute()
            
            if 'items' not in result:
                return None
            
            # Validate results
            for item in result['items']:
                if self._validate_result(item, report, next_year):
                    return {
                        'url': item['link'],
                        'title': item['title'],
                        'snippet': item.get('snippet', ''),
                        'year': next_year,
                        'org': report['org']
                    }
            
            return None
            
        except Exception as e:
            print(f"  ! Search error: {str(e)[:50]}")
            return None
    
    def _validate_result(self, item: Dict[str, Any], report: Dict[str, Any], year: int) -> bool:
        """Validate search result."""
        url = item['link'].lower()
        title = item['title'].lower()
        snippet = item.get('snippet', '').lower()
        
        # Check exclude terms
        for term in self.config.exclude_terms:
            if term.lower() in title or term.lower() in snippet:
                return False
        
        # Check financial terms
        for term in self.config.financial_terms:
            if term.lower() in title:
                return False
        
        # Check year in URL
        if str(year) not in url and str(year) not in title:
            return False
        
        # Check for 'report' keyword
        if 'report' not in title.lower() and 'report' not in snippet:
            return False
        
        return True

# ==========================
# GITHUB ISSUE CREATOR
# ==========================
class IssueCreator:
    """Creates GitHub issues for discovered reports."""
    
    def __init__(self, token: str):
        self.token = token
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        self.repo = os.environ.get('GITHUB_REPOSITORY', 'unknown/repo')
    
    def create_issue(self, candidate: Dict[str, Any]) -> bool:
        """Create GitHub issue for candidate report."""
        
        title = f"New Report: {candidate['org']} {candidate['year']}"
        body = f"""## 📄 New Security Report Discovered

**Organization:** {candidate['org']}
**Year:** {candidate['year']}
**URL:** {candidate['url']}

**Title:** {candidate['title']}

**Snippet:**
> {candidate['snippet']}

---
*Auto-discovered by Report Discovery workflow*
"""
        
        data = {
            'title': title,
            'body': body,
            'labels': ['report-suggestion', 'automated']
        }
        
        try:
            response = requests.post(
                f"https://api.github.com/repos/{self.repo}/issues",
                headers=self.headers,
                json=data
            )
            
            if response.status_code == 201:
                print(f"  ✓ Created issue: {title}")
                return True
            else:
                print(f"  ! Failed to create issue: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"  ! Error creating issue: {str(e)[:50]}")
            return False

# ==========================
# MAIN
# ==========================
def main():
    parser = argparse.ArgumentParser(description="Security Report Discovery")
    parser.add_argument("--artifacts-dir", default=".github/artifacts")
    parser.add_argument("--max-discoveries", type=int, default=10)
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
    
    # Check API keys
    search_key = os.environ.get("GOOGLE_SEARCH_API_KEY")
    cse_id = os.environ.get("GOOGLE_CSE_ID")
    gh_token = os.environ.get("GH_TOKEN")
    
    if not search_key or not cse_id:
        print("ERROR: Google Search API credentials required")
        return 1
    
    if not gh_token:
        print("ERROR: GH_TOKEN required")
        return 1
    
    # Scan repository
    scanner = ReportScanner(config)
    reports = scanner.scan_repository()
    
    if not reports:
        print("No historical reports found")
        return 0
    
    print(f"✓ {len(reports)} reports to check\n")
    
    # Search for updates
    searcher = GoogleSearcher(search_key, cse_id, config)
    issue_creator = IssueCreator(gh_token)
    
    candidates = []
    max_discoveries = min(args.max_discoveries, config.max_issues)
    
    for i, report in enumerate(reports[:50], 1):  # Limit to 50 searches
        if len(candidates) >= max_discoveries:
            break
        
        print(f"[{i}/50] {report['org']} ({report['year']})")
        
        candidate = searcher.search_for_update(report)
        if candidate:
            candidates.append(candidate)
            print(f"  ✓ Found candidate!")
        
        time.sleep(1)  # Rate limiting
    
    # Create issues
    print(f"\n{'='*70}")
    print(f"Creating issues for {len(candidates)} candidates")
    print(f"{'='*70}\n")
    
    created = 0
    for candidate in candidates:
        if issue_creator.create_issue(candidate):
            created += 1
    
    print(f"\n{'='*70}")
    print(f"Created {created} issues")
    print(f"{'='*70}")
    
    return 0 if created > 0 else 1

if __name__ == "__main__":
    sys.exit(main())