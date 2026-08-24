import os
import sys
import json
import re
import subprocess

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True, encoding='utf-8')
        if result.stdout:
            return result.stdout.strip()
        return ""
    except subprocess.CalledProcessError as e:
        print(f"Error running command {cmd}: {e}")
        return ""

def write_output(key, value):
    output_file = os.environ.get("GITHUB_OUTPUT")
    if output_file:
        with open(output_file, "a", encoding="utf-8") as f:
            f.write(f"{key}<<__EOF__\n{value}\n__EOF__\n")

def get_config():
    config_path = ".github/artifacts/workflow-config.json"
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f).get("workflow", {}).get("ingest", {})
    except Exception as e:
        print(f"Error loading config: {e}")
        return {}

def extract_pdf_attachment(body):
    """Scan the issue body for GitHub PDF attachment links."""
    # Look for [some name.pdf](https://github.com/user-attachments/assets/...)
    # or just raw https://github.com/user-attachments/assets/...pdf links
    attachments = re.findall(r'(https://github\.com/(?:[^/]+/[^/]+/)?user-attachments/(?:assets|files)/[^)]+\.pdf)', body, re.IGNORECASE)
    if attachments:
        return attachments[0]
    return None

def main():
    issue_number = os.environ.get("ISSUE_NUMBER")
    if not issue_number:
        print("ISSUE_NUMBER environment variable is required")
        sys.exit(1)

    body = run_cmd(f"gh issue view {issue_number} --json body -q .body")
    if not body:
        print("Could not retrieve issue body.")
        sys.exit(1)

    # We want to check comments too, but ONLY from trusted authors.
    comments_json = run_cmd(f"gh issue view {issue_number} --json comments -q .comments")
    comments = []
    if comments_json:
        try:
            comments_data = json.loads(comments_json)
            trusted_roles = ["OWNER", "COLLABORATOR", "MEMBER"]
            for c in comments_data:
                author_assoc = c.get("authorAssociation", "")
                if author_assoc in trusted_roles:
                    comments.append(c.get("body", ""))
                else:
                    print(f"Ignoring comment from untrusted author with association: {author_assoc}")
        except Exception as e:
            print(f"Error parsing comments: {e}")

    config = get_config()
    form_fields = config.get("form_fields", {
        "org": "Organization Name",
        "title": "Report Title",
        "year": "Report Year",
        "url": "Direct PDF URL",
        "category": "Category"
    })
    table_fields = config.get("table_fields", {
        "org": "Organization",
        "title": "Report",
        "year": "Year",
        "url": "URL",
        "category": "Category"
    })

    def parse_field(form_heading, table_heading):
        # 1. Try to find it in a Markdown table: | **Heading** | Value |
        table_pattern = rf"\|\s*\*\*{re.escape(table_heading)}\*\*\s*\|\s*([^|]+?)\s*\|"
        table_match = re.search(table_pattern, body, re.IGNORECASE)
        if table_match:
            return table_match.group(1).strip()

        # 2. Try to find it in Issue Forms format: ### Heading \n Value
        lines = body.split("\n")
        found = False
        for line in lines:
            if line.strip().lower() == f"### {form_heading}".lower():
                found = True
                continue
            if found:
                if not line.strip():
                    continue
                return line.strip()
        return ""

    org = parse_field(form_fields["org"], table_fields["org"])
    title = parse_field(form_fields["title"], table_fields["title"])
    year = parse_field(form_fields["year"], table_fields["year"])
    url = parse_field(form_fields["url"], table_fields["url"])
    category = parse_field(form_fields["category"], table_fields["category"])

    # Overwrite the URL if we find a GitHub PDF attachment in the body or comments
    all_text = body + "\n" + "\n".join(comments)
    attachment_url = extract_pdf_attachment(all_text)
    if attachment_url:
        print(f"Found GitHub attachment PDF link! Overriding original URL.")
        url = attachment_url

    print("Parsed fields:")
    print(f"  organization_name = '{org}'")
    print(f"  report_title      = '{title}'")
    print(f"  report_year       = '{year}'")
    print(f"  report_url        = '{url}'")
    print(f"  report_category   = '{category}'")

    write_output("organization_name", org)
    write_output("report_title", title)
    write_output("report_year", year)
    write_output("report_url", url)
    write_output("report_category", category)

if __name__ == "__main__":
    main()
