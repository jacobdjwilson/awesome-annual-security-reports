import os
import re
import sys
import subprocess
import datetime
import requests
import json
from bs4 import BeautifulSoup
from googleapiclient.discovery import build

# --- Configuration ---
MAX_ISSUES_PER_RUN = 10
LOOKBACK_DAYS = 90
TIMEOUT_SECONDS = 15

# Terms that indicate false positives
EXCLUDE_TERMS = [
    "webinar", "award", "sponsorship", "press release", 
    "conference", "summit", "call for speakers", "earnings call"
]

# Terms that usually indicate financial reports (not security reports)
FINANCIAL_TERMS = ["fiscal", "investor", "shareholder", "10-k", "10-q", "financial results"]

def get_existing_issues(org, year):
    """
    Checks if an issue (Open or Closed) already exists for this Org + Year.
    Returns: Boolean
    """
    # 1. Check Open Issues
    cmd_open = [
        'gh', 'issue', 'list',
        '--state', 'open',
        '--label', 'report-suggestion',
        '--search', f'"{org}" "{year}" in:title',
        '--json', 'number',
        '--limit', '1'
    ]
    
    # 2. Check Closed Issues (limit lookback to avoid re-opening ancient history)
    since_date = (datetime.date.today() - datetime.timedelta(days=LOOKBACK_DAYS)).isoformat()
    cmd_closed = [
        'gh', 'issue', 'list',
        '--state', 'closed',
        '--label', 'report-suggestion',
        '--search', f'"{org}" "{year}" in:title created:>{since_date}',
        '--json', 'number',
        '--limit', '1'
    ]

    for cmd in [cmd_open, cmd_closed]:
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0 and res.stdout.strip() != "[]":
            return True
            
    return False

def validate_url_content(url, target_year):
    """
    Visits the URL to perform deep validation.
    Returns: (Confidence: str, Reasoning: str)
    """
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=TIMEOUT_SECONDS, verify=False) # verify=False to handle potential cert issues on some corporate sites
        
        # 1. Check for Dead Links
        if response.status_code != 200:
            return "Low", f"URL returned status {response.status_code}"

        content_type = response.headers.get('Content-Type', '').lower()

        # 2. PDF Handling
        if 'application/pdf' in content_type or url.lower().endswith('.pdf'):
            if str(target_year) in url:
                return "High", f"Direct PDF detected with {target_year} in URL."
            return "Medium", "Direct PDF detected. Year not in URL, manual verification required."

        # 3. HTML Handling (The Anti-Footer Logic)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove noise: Footers, Navs, Copyright divs
        for noise in soup.select('footer, nav, .footer, .nav, .copyright, .legal, #footer, #copyright'):
            noise.decompose()

        # Get text from valid areas (Headings, Paragraphs, Lists)
        # Limiting to specific tags avoids pulling hidden metadata or scripts
        valid_tags = ['h1', 'h2', 'h3', 'p', 'li', 'article', 'main']
        body_text = " ".join([t.get_text() for t in soup.find_all(valid_tags)]).lower()
        title_text = (soup.title.string if soup.title else "").lower()

        full_clean_text = title_text + " " + body_text

        # 4. Keyword Checks
        # A. Check for False Positive Terms (Award, Webinar, etc)
        for term in EXCLUDE_TERMS:
            if term in full_clean_text:
                return "n/a", f"Page contains excluded term: '{term}'"

        # B. Check for Target Year
        if str(target_year) not in full_clean_text:
            return "n/a", f"Year {target_year} not found in main content (footer excluded)."

        # C. Check for Relevance ("Report", "Threat", "Security")
        if "report" not in full_clean_text and "threat" not in full_clean_text:
             return "n/a", "Page text lacks 'report' or 'threat' keywords."

        return "High", f"Found {target_year} and relevant keywords in body content."

    except Exception as e:
        return "Medium", f"Scraping failed ({str(e)[:50]}). relying on search snippet."

def main():
    # 1. Environment Check
    api_key = os.environ.get("GOOGLE_SEARCH_API_KEY")
    cse_id = os.environ.get("GOOGLE_CSE_ID")
    if not api_key or not cse_id:
        print("ERROR: Missing Google API keys.")
        sys.exit(1)

    # 2. Parse README for Targets
    print("INFO: Parsing README.md for targets...")
    targets = []
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            # Matches: - [Org Name](url) - [Report Title](url) (2024)
            pattern = r'-\s*\[([^\]]+)\]\([^)]+\)\s*-\s*\[([^\]]+)\]\([^)]+\)\s*\((\d{4})\)'
            targets = re.findall(pattern, f.read())
    except FileNotFoundError:
        print("ERROR: README.md not found.")
        sys.exit(1)

    print(f"INFO: Found {len(targets)} targets to check.")
    
    service = build("customsearch", "v1", developerKey=api_key)
    issues_created = 0

    # 3. Execution Loop
    for org, report_title, last_year in targets:
        if issues_created >= MAX_ISSUES_PER_RUN:
            print("INFO: Hit max issues limit. Stopping.")
            break

        current_year = int(last_year)
        target_year = current_year + 1
        
        # Skip Financial Reports based on title keywords
        if any(term in report_title.lower() for term in FINANCIAL_TERMS):
            print(f"DEBUG: Skipping {org} (Financial Report Filter)")
            continue

        # Check GitHub for duplicates
        if get_existing_issues(org, target_year):
            print(f"DEBUG: Skipping {org} {target_year} (Issue exists)")
            continue

        print(f"INFO: Searching for {org} {target_year}...")
        
        try:
            # Refined Query: Force filetypes to avoid generic landing pages if possible
            query = f'"{org}" "{report_title}" {target_year}'
            res = service.cse().list(q=query, cx=cse_id, num=3).execute()
            items = res.get('items', [])

            for item in items:
                link = item.get('link')
                title = item.get('title')
                snippet = item.get('snippet', '').replace('\n', ' ')

                # Phase 1: Quick exclusion (Blacklist/Regex)
                if "github.com" in link: continue
                
                # Check for excluded terms in Title/Snippet before scraping
                if any(term in title.lower() for term in EXCLUDE_TERMS):
                    print(f"DEBUG: Fast-skip {org}: Title contains excluded term.")
                    continue

                # Phase 2: Deep Validation (Scraping)
                confidence, reasoning = validate_url_content(link, target_year)

                if confidence == "n/a":
                    print(f"DEBUG: Rejecting {link} - {reasoning}")
                    continue

                # Phase 3: Create Issue
                print(f"SUCCESS: Found candidate for {org} - {confidence}")
                
                body = f"""
### 🔍 Discovery Analysis
**Confidence:** {confidence}
**Reasoning:** {reasoning}
**Snippet:** _{snippet}_

---

### Report Details
- **Organization:** {org}
- **Detected Year:** {target_year}
- **Source URL:** {link}

*Auto-generated by Security Report Discovery Workflow*
                """

                subprocess.run([
                    'gh', 'issue', 'create',
                    '--title', f"[REPORT SUGGESTION]: {org} ({target_year})",
                    '--body', body,
                    '--label', 'report-suggestion'
                ], check=True)

                issues_created += 1
                break # Move to next Org after finding one valid candidate

        except Exception as e:
            print(f"ERROR: processing {org}: {e}")

if __name__ == "__main__":
    main()