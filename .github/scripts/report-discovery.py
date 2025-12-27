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
            
            for item in items:
                link = item['link']
                snippet = item.get('snippet', '')
                item_title = item.get('title', '')
                
                # Validation: Must contain the next year in title or snippet
                if str(next_year) in item_title or str(next_year) in snippet:
                    
                    # 5. Create Issue using Template
                    # We use the template to ensure labels and metadata are applied correctly.
                    # The body must match the structure expected by the issue parser in ingest-suggestion.yml
                    
                    issue_title = f"[REPORT SUGGESTION]: {org} ({next_year})"
                    issue_body = (
                        f"### Report URL\n{link}\n\n"
                        f"### Report Year\n{next_year}\n\n"
                        f"### Description\nAutomated discovery found a potential update.\n\n"
                        f"**Snippet from Google:**\n> {snippet}"
                    )
                    
                    create_cmd = [
                        'gh', 'issue', 'create',
                        '--template', 'report-suggestion.yml',
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