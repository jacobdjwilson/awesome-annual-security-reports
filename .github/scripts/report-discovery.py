import os
import re
import sys
import subprocess
import datetime
import requests
import json
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from urllib.parse import urlparse

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

def extract_domain(url):
    """
    Extract the top-level domain from a URL.
    Returns: domain string (e.g., 'example.com')
    """
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        # Remove 'www.' prefix if present
        if domain.startswith('www.'):
            domain = domain[4:]
        return domain
    except:
        return None

def parse_readme_for_targets():
    """
    Parse README.md to extract organization details including category.
    Returns: list of tuples (org, report_title, last_year, category, report_url)
    """
    targets = []
    current_category = None
    
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()
            lines = content.split('\n')
            
            for line in lines:
                # Detect category headers (### headers under ## Analysis Reports or ## Survey Reports)
                if line.startswith('### '):
                    current_category = line.replace('### ', '').strip()
                    continue
                
                # Match report entries: - [Org Name](url) - [Report Title](url) (year)
                pattern = r'-\s*\[([^\]]+)\]\(([^)]+)\)\s*-\s*\[([^\]]+)\]\(([^)]+)\)\s*\((\d{4})\)'
                match = re.search(pattern, line)
                
                if match and current_category:
                    org = match.group(1)
                    org_url = match.group(2)
                    report_title = match.group(3)
                    report_url = match.group(4)
                    last_year = match.group(5)
                    
                    targets.append((org, report_title, last_year, current_category, report_url))
    
    except FileNotFoundError:
        print("ERROR: README.md not found.")
        sys.exit(1)
    
    return targets

def get_existing_report_domain(report_url):
    """
    Extract domain from the existing report URL.
    Returns: domain string or None
    """
    if not report_url:
        return None
    return extract_domain(report_url)

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

def extract_years_from_text(text):
    """
    Extract all 4-digit years from text.
    Returns: list of integers
    """
    years = re.findall(r'\b(19|20)\d{2}\b', text)
    return [int(year) for year in years]

def check_snippet_date_validity(snippet, target_year):
    """
    Check if snippet contains dates that invalidate it as a candidate.
    Returns: (is_valid: bool, reason: str)
    """
    # Check for copyright symbol followed by year
    copyright_pattern = r'©\s*(\d{4})|copyright\s+©?\s*(\d{4})'
    copyright_matches = re.findall(copyright_pattern, snippet.lower())
    for match in copyright_matches:
        copyright_year = int(match[0] or match[1])
        if copyright_year < target_year:
            return False, f"copyright year mismatch (© {copyright_year} < {target_year})"
    
    # Check if snippet starts with a date (blog/article pattern)
    # Pattern: "Jan 15, 2023" or "2023-01-15" or "January 15, 2023" at the beginning
    date_start_patterns = [
        r'^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+(\d{4})',
        r'^(\d{4})-\d{2}-\d{2}',
        r'^(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+(\d{4})'
    ]
    
    snippet_start = snippet.strip()[:50]  # Check first 50 chars
    for pattern in date_start_patterns:
        match = re.search(pattern, snippet_start, re.IGNORECASE)
        if match:
            # Extract year from the match
            year_groups = [g for g in match.groups() if g and g.isdigit() and len(g) == 4]
            if year_groups:
                blog_year = int(year_groups[0])
                if blog_year < target_year:
                    return False, f"blog/article pre-dates report year ({blog_year} < {target_year})"
    
    # Check for any dates in the snippet that pre-date the target year
    years_in_snippet = extract_years_from_text(snippet)
    if years_in_snippet:
        # Filter out the target year itself
        other_years = [y for y in years_in_snippet if y != target_year]
        if other_years:
            # Check if there are earlier years mentioned prominently
            earliest_year = min(other_years)
            if earliest_year < target_year and snippet.lower().find(str(earliest_year)) < snippet.lower().find(str(target_year)):
                return False, f"snippet contains pre-dated year prominently ({earliest_year} < {target_year})"
    
    return True, ""

def validate_url_content(url, target_year, existing_report_domain):
    """
    Visits the URL to perform deep validation.
    Returns: (Confidence: str, Reasoning: str)
    """
    try:
        # Check URL for year mismatches before even fetching
        years_in_url = extract_years_from_text(url)
        if years_in_url:
            # If URL contains a year different from target_year, especially earlier years
            for year in years_in_url:
                if year != target_year and year < target_year:
                    return "n/a", f"URL contains different year ({year} < {target_year})"
        
        # Check domain match with existing report
        url_domain = extract_domain(url)
        if existing_report_domain and url_domain:
            if url_domain != existing_report_domain:
                return "n/a", f"domain mismatch (found: {url_domain}, expected: {existing_report_domain})"
        
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=TIMEOUT_SECONDS, verify=False)
        
        # 1. Check for Dead Links
        if response.status_code != 200:
            return "Low", f"URL returned status {response.status_code}"

        content_type = response.headers.get('Content-Type', '').lower()

        # 2. PDF Handling
        if 'application/pdf' in content_type or url.lower().endswith('.pdf'):
            if str(target_year) in url:
                return "High", f"Direct PDF detected with {target_year} in URL."
            return "Medium", "Direct PDF detected. Year not in URL, manual verification required."

        # 3. HTML Handling
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove noise: Footers, Navs, Copyright divs
        for noise in soup.select('footer, nav, .footer, .nav, .copyright, .legal, #footer, #copyright'):
            noise.decompose()

        # Get text from valid areas
        valid_tags = ['h1', 'h2', 'h3', 'p', 'li', 'article', 'main']
        body_text = " ".join([t.get_text() for t in soup.find_all(valid_tags)]).lower()
        title_text = (soup.title.string if soup.title else "").lower()

        full_clean_text = title_text + " " + body_text

        # 4. Keyword Checks
        # A. Check for False Positive Terms
        for term in EXCLUDE_TERMS:
            if term in full_clean_text:
                return "n/a", f"Page contains excluded term: '{term}'"

        # B. Check for Target Year
        if str(target_year) not in full_clean_text:
            return "n/a", f"Year {target_year} not found in main content (footer excluded)."

        # C. Check for copyright year that differs from target year
        copyright_pattern = r'©\s*(\d{4})|copyright\s+©?\s*(\d{4})'
        copyright_matches = re.findall(copyright_pattern, full_clean_text)
        for match in copyright_matches:
            copyright_year = int(match[0] or match[1])
            if copyright_year < target_year:
                # Only reject if this is prominent (appears early in text)
                if full_clean_text.find(f'© {copyright_year}') < 1000 or full_clean_text.find(f'copyright {copyright_year}') < 1000:
                    return "n/a", f"copyright year mismatch in content (© {copyright_year} < {target_year})"

        # D. Check for Relevance
        if "report" not in full_clean_text and "threat" not in full_clean_text:
             return "n/a", "Page text lacks 'report' or 'threat' keywords."

        return "High", f"Found {target_year} and relevant keywords in body content."

    except Exception as e:
        return "Medium", f"Scraping failed ({str(e)[:50]}). Relying on search snippet."

def main():
    # 1. Environment Check
    api_key = os.environ.get("GOOGLE_SEARCH_API_KEY")
    cse_id = os.environ.get("GOOGLE_CSE_ID")
    if not api_key or not cse_id:
        print("ERROR: Missing Google API keys.")
        sys.exit(1)

    # 2. Parse README for Targets
    print("INFO: Parsing README.md for targets...")
    targets = parse_readme_for_targets()

    print(f"INFO: Found {len(targets)} targets to check.")
    
    service = build("customsearch", "v1", developerKey=api_key)
    issues_created = 0

    # 3. Execution Loop
    for org, report_title, last_year, category, report_url in targets:
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

        # Get existing report domain for validation
        existing_report_domain = get_existing_report_domain(report_url)
        
        if existing_report_domain:
            print(f"INFO: Existing domain for {org}: {existing_report_domain}")
        else:
            print(f"WARNING: Could not extract domain from report URL for {org}")

        print(f"INFO: Searching for {org} {target_year}...")
        
        try:
            # Refined Query
            query = f'"{org}" "{report_title}" {target_year}'
            res = service.cse().list(q=query, cx=cse_id, num=3).execute()
            items = res.get('items', [])

            for item in items:
                link = item.get('link')
                title = item.get('title')
                snippet = item.get('snippet', '').replace('\n', ' ')

                # Phase 1: Quick exclusion (Blacklist/Regex)
                if "github.com" in link:
                    continue
                
                # Check for excluded terms in Title/Snippet before scraping
                if any(term in title.lower() for term in EXCLUDE_TERMS):
                    print(f"DEBUG: Rejecting {link} - Title contains excluded term.")
                    continue
                
                if any(term in snippet.lower() for term in EXCLUDE_TERMS):
                    print(f"DEBUG: Rejecting {link} - Snippet contains excluded term.")
                    continue
                
                # Phase 1.5: Validate snippet dates
                snippet_valid, snippet_reason = check_snippet_date_validity(snippet, target_year)
                if not snippet_valid:
                    print(f"DEBUG: Rejecting {link} - {snippet_reason}")
                    continue

                # Phase 2: Deep Validation (Scraping)
                confidence, reasoning = validate_url_content(link, target_year, existing_report_domain)

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
**Source:** {link}

---

### Report Details
- **Organization:** {org}
- **Report Name:** {report_title}
- **Category:** {category}
- **Detected Year:** {target_year}
- **Expected Domain:** {existing_report_domain or 'N/A'}

*Auto-generated by Security Report Discovery Workflow*
                """

                subprocess.run([
                    'gh', 'issue', 'create',
                    '--title', f"[REPORT SUGGESTION]: {org} - {report_title} ({target_year})",
                    '--body', body,
                    '--label', 'report-suggestion'
                ], check=True)

                issues_created += 1
                break  # Move to next Org after finding one valid candidate

        except Exception as e:
            print(f"ERROR: processing {org}: {e}")

if __name__ == "__main__":
    main()