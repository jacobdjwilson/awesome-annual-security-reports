import os
import re
import json
import datetime
import subprocess
import sys
from googleapiclient.discovery import build

def main():
    # 1. Configuration
    SEARCH_LIMIT = 10 # Stay within daily API limits
    LOOKBACK_DAYS = 90
    
    # Ensure the label exists so automation downstream works
    # We swallow stderr to ignore "already exists" errors
    subprocess.run(['gh', 'label', 'create', 'report-suggestion', '--description', 'Suggest a new annual security report', '--color', '0E8A16'], stderr=subprocess.DEVNULL)

    # 2. Extract targets from README
    # Pattern: - [Org](link) - [Title](link) (Year)
    pattern = r'-\s*\[([^\]]+)\]\([^\)]+\)\s*-\s*\[([^\]]+)\]\([^\)]+\)\s*\((\d{4})\)'
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            entries = re.findall(pattern, f.read())
    except FileNotFoundError:
        print("README.md not found.")
        sys.exit(1)

    # Rolling window based on day of year for optimal coverage
    day_of_year = datetime.date.today().timetuple().tm_yday
    start_idx = (day_of_year * SEARCH_LIMIT) % len(entries)
    batch = (entries + entries)[start_idx : start_idx + SEARCH_LIMIT]

    if "GOOGLE_SEARCH_API_KEY" not in os.environ or "GOOGLE_CSE_ID" not in os.environ:
        print("Missing Google API keys.")
        sys.exit(1)

    service = build("customsearch", "v1", developerKey=os.environ["GOOGLE_SEARCH_API_KEY"])
    since_date = (datetime.date.today() - datetime.timedelta(days=LOOKBACK_DAYS)).isoformat()

    for org, title, year in batch:
        next_year = int(year) + 1
        # Query for BOTH landing pages and direct PDFs
        search_query = f'"{org}" "{title}" {next_year}'
        
        # 3. Precise Duplicate Check (Stateless)
        # Checks for the Org + Year + Label in issues from the last 90 days
        check_q = f'"{org}" "{next_year}" label:report-suggestion created:>{since_date}'
        
        # Use subprocess for safer execution
        check_cmd = ['gh', 'issue', 'list', '--state', 'all', '--search', check_q, '--json', 'number']
        result = subprocess.run(check_cmd, capture_output=True, text=True)
        
        if result.returncode == 0 and json.loads(result.stdout):
            print(f"Skipping {org} {next_year}: Recent issue exists.")
            continue

        # 4. Search and Validate
        try:
            res = service.cse().list(q=search_query, cx=os.environ["GOOGLE_CSE_ID"], num=3).execute()
            items = res.get('items', [])
            
            # Basic filtering for obviously incorrect URLs
            URL_BLACKLIST = [
                "github.com/jacobdjwilson/awesome-annual-security-reports"
            ]

            for item in items:
                link = item['link']
                snippet = item.get('snippet', '')
                item_title = item.get('title', '')

                # --- Start of new validation logic ---

                # Rule 1: Skip blacklisted URLs
                if any(blacklisted in link for blacklisted in URL_BLACKLIST):
                    print(f"Skipping blacklisted URL: {link}")
                    continue

                year_pattern = r'\b' + str(next_year) + r'\b'
                current_year_pattern = r'\b' + str(year) + r'\b' # 'year' is the year from the README

                title_has_next_year = re.search(year_pattern, item_title)
                snippet_has_next_year = re.search(year_pattern, snippet)

                # Rule 2: If the next year is not in the title or snippet, it's not a match.
                if not title_has_next_year and not snippet_has_next_year:
                    continue

                # Rule 3: If the next year is only in the snippet, be more skeptical.
                if snippet_has_next_year and not title_has_next_year:
                    # If the current year is also in the snippet with context words, it's likely a false positive.
                    if re.search(current_year_pattern, snippet) and "report" in snippet.lower():
                        print(f"Skipping ambiguous snippet: {snippet}")
                        continue
                
                # Rule 4: If the *current* year is in the title with "report", it might be a retrospective.
                if title_has_next_year:
                    if re.search(current_year_pattern, item_title) and "report" in item_title.lower():
                        print(f"Skipping likely retrospective: {item_title}")
                        continue

                # --- End of new validation logic ---

                # If we get here, the result is considered high-fidelity
                issue_title = f"[REPORT SUGGESTION]: {org} ({next_year})"
                issue_body = (
                    f"### Report URL\n{link}\n\n"
                    f"### Report Year\n{next_year}\n\n"
                    f"### Description\nAutomated discovery found a potential update.\n\n"
                    f"**Snippet from Google:**\n> {snippet}"
                )
                
                create_cmd = [
                    'gh', 'issue', 'create',
                    '--title', issue_title,
                    '--body', issue_body
                ]
                subprocess.run(create_cmd, check=True)
                print(f"Created suggestion for {org} {next_year}")
                break 
                    
        except Exception as e:
            print(f"Search failed for {org}: {e}")

if __name__ == "__main__":
    main()