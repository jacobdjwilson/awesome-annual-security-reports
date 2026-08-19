import os
import sys
import subprocess

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command {cmd}: {e}")
        return ""

def write_output(key, value):
    output_file = os.environ.get("GITHUB_OUTPUT")
    if output_file:
        with open(output_file, "a") as f:
            f.write(f"{key}<<__EOF__\n{value}\n__EOF__\n")

def main():
    issue_number = os.environ.get("ISSUE_NUMBER")
    if not issue_number:
        print("ISSUE_NUMBER environment variable is required")
        sys.exit(1)

    body = run_cmd(f"gh issue view {issue_number} --json body -q .body")

    def parse_field(heading):
        lines = body.split("\n")
        found = False
        for line in lines:
            if line.strip().lower() == f"### {heading}".lower():
                found = True
                continue
            if found:
                if not line.strip():
                    continue
                return line.strip()
        return ""

    org = parse_field("Organization Name")
    title = parse_field("Report Title")
    year = parse_field("Report Year")
    url = parse_field("Direct PDF URL")
    category = parse_field("Category")

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
