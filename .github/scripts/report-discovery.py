import os
import re
import sys
import subprocess
import datetime
import requests
import json
from pathlib import Path
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from urllib.parse import urlparse

# --- Configuration ---
MAX_ISSUES_PER_RUN = 10
LOOKBACK_DAYS = 90
TIMEOUT_SECONDS = 15
CURRENT_YEAR = datetime.date.today().year
REPORTS_BASE_DIR = "Annual Security Reports"

# Terms that indicate false positives
EXCLUDE_TERMS = [
    "webinar", "award", "sponsorship", "press release", 
    "conference", "summit", "call for speakers", "earnings call",
    "podcast", "pre-register", "pre-registration", "coming soon",
    "save the date", "register now", "registration open"
]

# Terms that usually indicate financial reports (not security reports)
FINANCIAL_TERMS = ["fiscal", "investor", "shareholder", "10-k", "10-q", "financial results"]

# Low-quality source domains (prefer original sources over these)
SECONDARY_SOURCE_DOMAINS = [
    "linkedin.com", "twitter.com", "x.com", "reddit.com", "facebook.com",
    "medium.com", "forbes.com", "techcrunch.com", "zdnet.com",
    "darkreading.com", "bleepingcomputer.com", "thehackernews.com",
    "securityweek.com", "infosecurity-magazine.com", "hendryadrian.com",
    "hardenstance.com", "zoominfo.com", "brianpennington.co.uk",
    "coconote.app", "demandtalk.com", "spotify.com"
]

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

def is_secondary_source(url):
    """
    Check if URL is from a secondary/aggregator source.
    Returns: Boolean
    """
    domain = extract_domain(url)
    if not domain:
        return False
    return any(secondary in domain for secondary in SECONDARY_SOURCE_DOMAINS)

def parse_pdf_filename(filename):
    """
    Parse PDF filename to extract organization, report title, and year.
    Expected format: Organization-Report-Title-Year.pdf
    
    Returns: tuple (organization, report_title, year) or None if cannot parse
    """
    # Remove .pdf extension
    name = filename.replace('.pdf', '')
    
    # Try to find year at the end (4 digits)
    year_match = re.search(r'-(\d{4})$', name)
    if not year_match:
        return None
    
    year = int(year_match.group(1))
    # Remove year from name
    name_without_year = name[:year_match.start()]
    
    # Split by hyphens to get parts
    parts = name_without_year.split('-')
    if len(parts) < 2:
        return None
    
    # First part is organization, rest is report title
    organization = parts[0]
    report_title = '-'.join(parts[1:])
    
    return (organization, report_title, year)

def scan_repository_reports():
    """
    Scan the Annual Security Reports directory for all PDF files from previous years.
    Returns: list of tuples (organization, report_title, year, file_path, category_from_year)
    """
    reports = []
    
    if not os.path.exists(REPORTS_BASE_DIR):
        print(f"ERROR: Reports directory '{REPORTS_BASE_DIR}' not found.")
        return reports
    
    # Iterate through year directories
    for year_dir in sorted(os.listdir(REPORTS_BASE_DIR)):
        year_path = os.path.join(REPORTS_BASE_DIR, year_dir)
        
        # Skip if not a directory
        if not os.path.isdir(year_path):
            continue
        
        # Extract year from directory name
        try:
            dir_year = int(year_dir)
        except ValueError:
            continue
        
        # Only process years older than current year
        if dir_year >= CURRENT_YEAR:
            print(f"DEBUG: Skipping current/future year directory: {year_dir}")
            continue
        
        print(f"INFO: Scanning directory: {year_dir}")
        
        # Scan PDFs in this year directory
        for filename in os.listdir(year_path):
            if not filename.endswith('.pdf'):
                continue
            
            # Parse filename
            parsed = parse_pdf_filename(filename)
            if not parsed:
                print(f"DEBUG: Could not parse filename: {filename}")
                continue
            
            org, report_title, file_year = parsed
            file_path = os.path.join(year_path, filename)
            
            # Verify file year matches directory year
            if file_year != dir_year:
                print(f"DEBUG: Year mismatch in {filename}: file has {file_year}, directory is {dir_year}")
            
            reports.append((org, report_title, file_year, file_path, year_dir))
            
    print(f"INFO: Found {len(reports)} historical reports to check for updates")
    return reports

def get_category_from_readme(org, report_title):
    """
    Try to find the category for this report from README.md.
    Returns: category string or "Unknown"
    """
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()
            lines = content.split('\n')
            
            current_category = None
            for line in lines:
                # Detect category headers
                if line.startswith('### '):
                    current_category = line.replace('### ', '').strip()
                    continue
                
                # Check if this line contains our org and report
                if org in line and current_category:
                    return current_category
    except:
        pass
    
    return "Unknown"

def get_report_url_from_readme(org, report_title, year):
    """
    Try to find the report URL from README.md for a specific year.
    Returns: URL string or None
    """
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()
            lines = content.split('\n')
            
            for line in lines:
                # Match report entries with year
                if org in line and str(year) in line:
                    # Extract URL from markdown link
                    url_matches = re.findall(r'\]\(([^)]+)\)', line)
                    if len(url_matches) >= 2:
                        # Second URL is usually the report URL
                        return url_matches[1]
    except:
        pass
    
    return None

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

def check_future_year(year):
    """
    Check if year is in the future (always a false positive).
    Returns: (is_future: bool, reason: str)
    """
    if year > CURRENT_YEAR:
        return True, f"Future year detected ({year} > {CURRENT_YEAR}) - likely prediction/planning content"
    return False, ""

def extract_date_from_snippet_start(snippet):
    """
    Extract date from the beginning of snippet (blog/article pattern).
    Returns: (year: int or None, date_string: str or None)
    """
    # Pattern: "Jan 15, 2023" or "2023-01-15" or "January 15, 2023" at the beginning
    date_start_patterns = [
        (r'^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+(\d{4})', 2),
        (r'^(\d{4})-\d{2}-\d{2}', 1),
        (r'^(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+(\d{4})', 2),
        (r'^(\d{1,2})\s+(days?|weeks?|months?)\s+ago', None),  # Relative dates
    ]
    
    snippet_start = snippet.strip()[:100]  # Check first 100 chars
    
    for pattern, year_group_idx in date_start_patterns:
        match = re.search(pattern, snippet_start, re.IGNORECASE)
        if match:
            if year_group_idx is None:
                # Relative date like "5 days ago"
                return CURRENT_YEAR, match.group(0)
            else:
                year = int(match.group(year_group_idx))
                return year, match.group(0)
    
    return None, None

def check_snippet_validity(snippet, title, target_year):
    """
    Comprehensive snippet validation with detailed reasoning.
    Returns: (is_valid: bool, confidence_adjustment: str, reason: str)
    """
    snippet_lower = snippet.lower()
    title_lower = title.lower()
    
    # 1. Check for copyright year mismatches
    copyright_pattern = r'©\s*(\d{4})|copyright\s+©?\s*(\d{4})'
    copyright_matches = re.findall(copyright_pattern, snippet_lower)
    for match in copyright_matches:
        copyright_year = int(match[0] or match[1])
        if copyright_year != target_year and copyright_year == CURRENT_YEAR:
            return False, "", f"Copyright year {copyright_year} != target year {target_year} (likely footer/copyright date)"
    
    # 2. Check for blog/article pre-dating the report
    snippet_date_year, date_string = extract_date_from_snippet_start(snippet)
    if snippet_date_year and snippet_date_year < target_year:
        return False, "", f"Snippet contains pre-dated article ({date_string}) - likely blog post announcing report release"
    
    # 3. Extract all years from title and snippet
    title_years = extract_years_from_text(title)
    snippet_years = extract_years_from_text(snippet)
    
    # Check for years that don't match target
    mismatched_years = [y for y in (title_years + snippet_years) if y != target_year and y >= 2020]
    if mismatched_years and target_year not in (title_years + snippet_years):
        return False, "", f"Year {mismatched_years[0]} found but not {target_year} (likely different report year)"
    
    # 4. Check if target year is present
    if target_year not in (title_years + snippet_years):
        # More lenient if snippet is short or truncated
        if len(snippet) < 50:
            return True, "upgrade_medium", f"Short snippet but no conflicting years"
        return False, "", f"Year {target_year} not found in title or snippet"
    
    # 5. Look for positive signals
    positive_signals = ["report", "study", "analysis", "survey", "threat", "security", "annual"]
    has_positive = any(signal in snippet_lower or signal in title_lower for signal in positive_signals)
    
    if not has_positive:
        return False, "", "Lacks report-related keywords"
    
    # 6. Check for strong date match in title
    if target_year in title_years:
        return True, "upgrade_medium", f"Year {target_year} prominently in title"
    
    return True, "", f"Year {target_year} found with relevant context"

def validate_url_content(url, target_year, expected_domain, title, snippet):
    """
    Fetch and validate URL content with comprehensive checks.
    Returns: (confidence: str, reasoning: str, validation_details: dict)
    
    Confidence levels: "High", "Medium", "Low", "n/a" (rejected)
    """
    validation_details = {
        "domain_match": None,
        "year_in_url": [],
        "is_secondary_source": False,
        "content_type": None,
    }
    
    try:
        # A. Domain validation
        url_domain = extract_domain(url)
        validation_details["is_secondary_source"] = is_secondary_source(url)
        
        if expected_domain:
            validation_details["domain_match"] = (url_domain == expected_domain)
        
        # B. URL structure analysis
        url_years = extract_years_from_text(url)
        validation_details["year_in_url"] = url_years
        
        # Reject if URL contains a different year prominently
        if url_years and target_year not in url_years:
            conflicting_years = [y for y in url_years if y != target_year and y >= 2020 and y <= CURRENT_YEAR]
            if conflicting_years:
                return "n/a", f"URL contains different year: {conflicting_years[0]}", validation_details
        
        # C. Fetch and analyze content
        headers = {'User-Agent': 'Mozilla/5.0 (Security-Report-Discovery-Bot)'}
        response = requests.get(url, timeout=TIMEOUT_SECONDS, headers=headers, allow_redirects=True)
        
        content_type = response.headers.get('Content-Type', '').lower()
        validation_details["content_type"] = content_type
        
        # Handle PDF files
        if 'pdf' in content_type:
            # For PDFs, rely more on URL and title analysis
            if target_year in url_years or str(target_year) in url:
                return "High", f"PDF with {target_year} in URL", validation_details
            elif validation_details["domain_match"]:
                return "Medium", f"PDF from expected domain", validation_details
            else:
                return "Low", f"PDF from unexpected source", validation_details
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Get text
        full_text = soup.get_text()
        full_clean_text = ' '.join(full_text.split()).lower()
        
        # D. Check for copyright year in content
        copyright_pattern = r'©\s*(\d{4})|copyright\s+©?\s*(\d{4})'
        copyright_matches = re.findall(copyright_pattern, full_clean_text)
        for match in copyright_matches:
            copyright_year = int(match[0] or match[1])
            if copyright_year < target_year:
                # Only reject if this appears prominently
                if full_clean_text.find(f'© {copyright_year}') < 1000 or full_clean_text.find(f'copyright {copyright_year}') < 1000:
                    return "n/a", f"Prominent copyright year {copyright_year} < target {target_year}", validation_details

        # E. Check for Relevance
        if "report" not in full_clean_text and "threat" not in full_clean_text and "study" not in full_clean_text:
             return "n/a", "Page lacks report/threat/study keywords", validation_details

        # F. Check for target year in content
        content_years = extract_years_from_text(full_clean_text)
        if target_year not in content_years:
            return "n/a", f"Target year {target_year} not found in page content", validation_details

        # Confidence determination
        confidence = "High" if validation_details["domain_match"] else "Medium"
        if validation_details["is_secondary_source"]:
            confidence = "Low"
        
        reasoning_parts = [f"Found {target_year} with relevant keywords"]
        if validation_details["domain_match"]:
            reasoning_parts.append("domain matches expected source")
        elif validation_details["is_secondary_source"]:
            reasoning_parts.append(f"secondary source ({url_domain})")
        
        return confidence, "; ".join(reasoning_parts), validation_details

    except Exception as e:
        return "Medium", f"Validation failed: {str(e)[:100]}", validation_details

def main():
    # 1. Environment Check
    api_key = os.environ.get("GOOGLE_SEARCH_API_KEY")
    cse_id = os.environ.get("GOOGLE_CSE_ID")
    if not api_key or not cse_id:
        print("ERROR: Missing Google API keys.")
        sys.exit(1)

    # 2. Scan Repository for Historical Reports
    print("INFO: Scanning repository for historical reports...")
    reports = scan_repository_reports()
    
    if not reports:
        print("WARNING: No historical reports found in repository")
        sys.exit(0)

    print(f"INFO: Found {len(reports)} reports to check for updates.")
    print(f"INFO: Current year: {CURRENT_YEAR}")
    
    service = build("customsearch", "v1", developerKey=api_key)
    issues_created = 0

    # 3. Execution Loop - Check each report for newer version
    for org, report_title, last_year, file_path, year_dir in reports:
        if issues_created >= MAX_ISSUES_PER_RUN:
            print("INFO: Hit max issues limit. Stopping.")
            break

        target_year = last_year + 1
        
        # Skip if target year is in the future
        is_future, future_reason = check_future_year(target_year)
        if is_future:
            print(f"DEBUG: Skipping {org} - {future_reason}")
            continue
        
        # Skip Financial Reports based on title keywords
        if any(term in report_title.lower() for term in FINANCIAL_TERMS):
            print(f"DEBUG: Skipping {org} (Financial Report Filter)")
            continue

        # Check GitHub for duplicates
        if get_existing_issues(org, target_year):
            print(f"DEBUG: Skipping {org} {target_year} (Issue exists)")
            continue

        # Get category and existing URL from README if available
        category = get_category_from_readme(org, report_title)
        last_year_url = get_report_url_from_readme(org, report_title, last_year)
        existing_report_domain = get_existing_report_domain(last_year_url)
        
        if existing_report_domain:
            print(f"INFO: Expected domain for {org}: {existing_report_domain}")
        else:
            print(f"WARNING: Could not determine domain for {org}")

        print(f"INFO: Searching for {org} {report_title} {target_year}...")
        
        try:
            # Refined Query - search for organization + report title + target year
            query = f'"{org}" "{report_title}" {target_year}'
            res = service.cse().list(q=query, cx=cse_id, num=5).execute()
            items = res.get('items', [])

            if not items:
                print(f"DEBUG: No search results for {org} {target_year}")
                continue

            for item in items:
                link = item.get('link')
                title = item.get('title')
                snippet = item.get('snippet', '').replace('\n', ' ')

                # Phase 1: Quick exclusion
                if "github.com" in link:
                    print(f"DEBUG: Skipping GitHub URL: {link}")
                    continue
                
                # Check for excluded terms in Title/Snippet
                if any(term in title.lower() for term in EXCLUDE_TERMS):
                    print(f"DEBUG: Rejecting {link} - Title contains excluded term")
                    continue
                
                if any(term in snippet.lower() for term in EXCLUDE_TERMS):
                    print(f"DEBUG: Rejecting {link} - Snippet contains excluded term")
                    continue
                
                # Phase 1.5: Validate snippet
                snippet_valid, confidence_adj, snippet_reason = check_snippet_validity(snippet, title, target_year)
                if not snippet_valid:
                    print(f"DEBUG: Rejecting {link} - {snippet_reason}")
                    continue

                # Phase 2: Deep Validation
                confidence, reasoning, validation_details = validate_url_content(
                    link, target_year, existing_report_domain, title, snippet
                )

                # Apply confidence adjustments from snippet analysis
                if confidence_adj == "upgrade_medium" and confidence == "Medium":
                    confidence = "High"
                elif confidence_adj == "downgrade_medium" and confidence == "High":
                    confidence = "Medium"

                if confidence == "n/a":
                    print(f"DEBUG: Rejecting {link} - {reasoning}")
                    continue

                # Phase 3: Create Issue with Enhanced Details
                print(f"SUCCESS: Found candidate for {org} - Confidence: {confidence}")
                
                # Build validation details summary
                validation_summary = []
                if validation_details["is_secondary_source"]:
                    validation_summary.append("⚠️ **Secondary source** (prefer original publisher)")
                if validation_details["domain_match"] is True:
                    validation_summary.append("✅ Domain matches expected source")
                elif validation_details["domain_match"] is False:
                    validation_summary.append(f"⚠️ Domain differs from expected ({existing_report_domain})")
                if validation_details["year_in_url"]:
                    validation_summary.append(f"📅 Years in URL: {validation_details['year_in_url']}")
                if validation_details["content_type"]:
                    validation_summary.append(f"📄 Content type: {validation_details['content_type']}")
                
                validation_summary_text = "\n".join([f"- {item}" for item in validation_summary]) if validation_summary else "- No special validation notes"
                
                body = f"""
### 🔍 Discovery Analysis
**Confidence:** {confidence}
**Reasoning:** {reasoning}
**Discovery Method:** Repository scan of historical reports

### 📊 Validation Details
{validation_summary_text}

### 📝 Source Information
**Title:** {title}
**Snippet:** _{snippet}_
**URL:** {link}

### 📚 Report Details
- **Organization:** {org}
- **Report Name:** {report_title}
- **Category:** {category}
- **Target Year:** {target_year}
- **Previous Year:** {last_year}
- **Previous File:** `{file_path}`
- **Expected Domain:** {existing_report_domain or 'Unknown'}
- **Found Domain:** {validation_details.get('domain_match') if validation_details.get('domain_match') is not None else extract_domain(link)}

### 🤖 Review Checklist
- [ ] Verify this is the official {target_year} report (not a blog post/announcement about it)
- [ ] Check if URL points to the actual report document
- [ ] Confirm the report year matches {target_year}
- [ ] Validate the source is authoritative (original publisher preferred)
- [ ] Compare with previous report: `{file_path}`

*Auto-generated by Security Report Discovery Workflow (Repository Scanner)*
                """

                subprocess.run([
                    'gh', 'issue', 'create',
                    '--title', f"[REPORT SUGGESTION]: {org} - {report_title} ({target_year})",
                    '--body', body,
                    '--label', 'report-suggestion'
                ], check=True)

                issues_created += 1
                break  # Move to next report after finding one valid candidate

        except Exception as e:
            print(f"ERROR: processing {org}: {e}")
            import traceback
            traceback.print_exc()

    print(f"INFO: Discovery complete. Created {issues_created} issues.")

if __name__ == "__main__":
    main()