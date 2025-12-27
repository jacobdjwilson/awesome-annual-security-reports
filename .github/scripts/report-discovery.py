import os
import re
import json
import datetime
import subprocess
import sys
from googleapiclient.discovery import build

# --- Configuration Constants ---
MAX_ISSUES_PER_RUN = 10
LOOKBACK_DAYS = 90
URL_BLACKLIST = [
    "github.com/jacobdjwilson/awesome-annual-security-reports"
]
FINANCIAL_TERMS = ["fiscal year", "quarter", "financial", "earnings", "investor"]

def is_valid_report(item, next_year, current_year):
    """
    Applies a series of validation rules to a Google search result item
    to determine if it's a high-fidelity candidate for a new report.

    Args:
        item (dict): A Google search result item.
        next_year (int): The year we are looking for.
        current_year (int): The year of the last known report.

    Returns:
        bool: True if the item is a valid candidate, False otherwise.
    """
    link = item.get('link', '')
    item_title = item.get('title', '').lower()
    snippet = item.get('snippet', '').lower()

    # Rule 1: Skip blacklisted URLs (e.g., the repo itself)
    if any(blacklisted in link for blacklisted in URL_BLACKLIST):
        print(f"DEBUG: Skipping blacklisted URL: {link}")
        return False

    # Rule 2: Skip URLs that explicitly contain the previous report's year
    url_years = re.findall(r'\b(20\d{2})\b', link)
    if str(current_year) in url_years:
        print(f"DEBUG: Skipping URL containing previous year '{current_year}': {link}")
        return False

    # Rule 3: Filter out financial reports which have confusing "fiscal years"
    if any(term in item_title for term in FINANCIAL_TERMS) or any(term in link for term in FINANCIAL_TERMS):
        print(f"DEBUG: Skipping likely financial report: {item_title}")
        return False

    year_pattern = r'\b' + str(next_year) + r'\b'
    current_year_pattern = r'\b' + str(current_year) + r'\b'

    title_has_next_year = re.search(year_pattern, item_title)
    snippet_has_next_year = re.search(year_pattern, snippet)

    # Rule 4: The target year must be present in the title or snippet
    if not title_has_next_year and not snippet_has_next_year:
        return False

    # Rule 5: If the target year is only in the snippet, apply extra scrutiny
    if snippet_has_next_year and not title_has_next_year:
        # Check for copyright notices
        if 'copyright' in snippet or '©' in snippet:
            print(f"DEBUG: Skipping snippet with copyright year: {snippet}")
            return False
        # Check for ambiguous snippets that mention the current year's report
        if re.search(current_year_pattern, snippet) and "report" in snippet:
            print(f"DEBUG: Skipping ambiguous snippet: {snippet}")
            return False
            
    # Rule 6: Handle conflicts if the target year is in the title
    if title_has_next_year:
        # Title has "next_year", but snippet has "current_year report"
        if re.search(current_year_pattern + r'\b.*report', snippet, re.IGNORECASE):
            print(f"DEBUG: Skipping due to conflict between title year ({next_year}) and snippet year ({current_year}): {snippet}")
            return False
        # Title has "next_year" AND "current_year report" (likely a retrospective)
        if re.search(current_year_pattern, item_title) and "report" in item_title:
            print(f"DEBUG: Skipping likely retrospective: {item_title}")
            return False

    return True

def main():
    """
    Main function to discover new security reports.
    """
    # 1. Initial Setup
    if "GOOGLE_SEARCH_API_KEY" not in os.environ or "GOOGLE_CSE_ID" not in os.environ:
        print("ERROR: Missing Google API keys.")
        sys.exit(1)

    # Ensure the 'report-suggestion' label exists in the repo
    subprocess.run(['gh', 'label', 'create', 'report-suggestion', '--description', 'Suggest a new annual security report', '--color', '0E8A16'], stderr=subprocess.DEVNULL, check=False)

    # 2. Read existing report entries from README
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            # Pattern: - [Org](link) - [Title](link) (Year)
            pattern = r'-\s*\[([^\]]+)\]\([^)]+\)\s*-\s*\[([^\]]+)\]\([^)]+\)\s*\((\d{4})\)'
            entries = re.findall(pattern, f.read())
    except FileNotFoundError:
        print("ERROR: README.md not found.")
        sys.exit(1)

    # 3. Perform Searches
    service = build("customsearch", "v1", developerKey=os.environ["GOOGLE_SEARCH_API_KEY"])
    since_date = (datetime.date.today() - datetime.timedelta(days=LOOKBACK_DAYS)).isoformat()
    issues_created = 0

    # Search for all entries, but limit the number of issues created
    for org, title, year_str in entries:
        if issues_created >= MAX_ISSUES_PER_RUN:
            print(f"INFO: Reached maximum of {MAX_ISSUES_PER_RUN} issues for this run.")
            break

        current_year = int(year_str)
        next_year = current_year + 1
        
        # Check if a suggestion for this org and year already exists
        check_q = f'"{org}" "{next_year}" label:report-suggestion created:>{since_date}'
        check_cmd = ['gh', 'issue', 'list', '--state', 'all', '--search', check_q, '--json', 'number']
        result = subprocess.run(check_cmd, capture_output=True, text=True, check=False)
        
        if result.returncode == 0 and result.stdout and json.loads(result.stdout):
            print(f"INFO: Skipping {org} {next_year}: Recent issue exists.")
            continue

        # Perform the Google search
        try:
            search_query = f'"{org}" "{title}" {next_year}'
            res = service.cse().list(q=search_query, cx=os.environ["GOOGLE_CSE_ID"], num=3).execute()
            
            for item in res.get('items', []):
                if is_valid_report(item, next_year, current_year):
                    # Found a valid report, create an issue
                    issue_title = f"[REPORT SUGGESTION]: {org} ({next_year})"
                    issue_body = (
                        f"### Report URL\n{item['link']}\n\n"
                        f"### Report Year\n{next_year}\n\n"
                        f"### Description\nAutomated discovery found a potential update.\n\n"
                        f"**Snippet from Google:**\n> {item.get('snippet', '')}"
                    )
                    
                    create_cmd = ['gh', 'issue', 'create', '--title', issue_title, '--body', issue_body]
                    subprocess.run(create_cmd, check=True)
                    
                    print(f"SUCCESS: Created suggestion for {org} {next_year}")
                    issues_created += 1
                    break  # Move to the next organization
                    
        except Exception as e:
            print(f"ERROR: Search failed for {org}: {e}")

if __name__ == "__main__":
    main()
