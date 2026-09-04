"""
Operational Purpose:
    Parses community report ingestion issue forms and issue comments to extract
    structured metadata (organization name, report title, year, PDF URL, category).
    Validates commenter permissions against trusted roles configured in workflow-config.json.

Required Environment Variables:
    ISSUE_NUMBER: GitHub issue number to inspect.
    GITHUB_OUTPUT (optional): Path to export parsed fields for downstream workflow steps.

Outputs:
    organization_name: Extracted organization name.
    report_title: Extracted report title.
    report_year: Extracted report publication year.
    report_url: Extracted direct PDF URL or user attachment link.
    report_category: Extracted report category.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.ingest)
"""

import os
import sys
import json
import re
import subprocess
from pathlib import Path
from typing import Dict, Any, List, Optional

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class IssueFormConfigLoader:
    """Loads ingestion and form parsing configuration with fail-fast validation."""

    def __init__(self, artifacts_dir: str = ".github/artifacts") -> None:
        self.config_path = Path(artifacts_dir) / "workflow-config.json"
        self.config = self._load()

    def _load(self) -> Dict[str, Any]:
        if not self.config_path.exists():
            raise FileNotFoundError(f"Missing required artifact: '{self.config_path}'.")
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            raise ValueError(f"Failed to parse JSON artifact '{self.config_path}': {e}") from e

        workflow = data.get("workflow", {})
        ingest_cfg = workflow.get("ingest")
        if not ingest_cfg or not isinstance(ingest_cfg, dict):
            raise KeyError(f"Missing 'workflow.ingest' configuration in '{self.config_path}'.")

        required_keys = ["trusted_roles", "form_fields", "table_fields"]
        for key in required_keys:
            if key not in ingest_cfg:
                raise KeyError(f"Missing required key '{key}' in 'workflow.ingest' of '{self.config_path}'.")

        return ingest_cfg

    @property
    def trusted_roles(self) -> List[str]:
        return list(self.config["trusted_roles"])

    @property
    def form_fields(self) -> Dict[str, str]:
        return dict(self.config["form_fields"])

    @property
    def table_fields(self) -> Dict[str, str]:
        return dict(self.config["table_fields"])


def run_cmd(cmd: str) -> str:
    """Runs a shell command safely, returning stripped stdout."""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        if result.stdout:
            return result.stdout.strip()
        return ""
    except subprocess.CalledProcessError as e:
        print(f"Command '{cmd}' failed with code {e.returncode}: {e.stderr}", file=sys.stderr)
        return ""


def write_output(key: str, value: str) -> None:
    """Exports key/value pair to GITHUB_OUTPUT using EOF delimiter."""
    output_file = os.environ.get("GITHUB_OUTPUT")
    if output_file:
        with open(output_file, "a", encoding="utf-8") as f:
            f.write(f"{key}<<__EOF__\n{value}\n__EOF__\n")


def extract_pdf_attachment(body: str) -> Optional[str]:
    """Scans text for GitHub user attachment PDF links."""
    attachments = re.findall(
        r"(https://github\.com/(?:[^/]+/[^/]+/)?user-attachments/(?:assets|files)/[^)]+\.pdf)",
        body,
        re.IGNORECASE,
    )
    if attachments:
        return attachments[0]
    return None


def parse_field(body: str, form_heading: str, table_heading: str) -> str:
    """Extracts field value from either a Markdown table or an Issue Form header."""
    table_pattern = rf"\|\s*\*\*{re.escape(table_heading)}\*\*\s*\|\s*([^|]+?)\s*\|"
    table_match = re.search(table_pattern, body, re.IGNORECASE)
    if table_match:
        return table_match.group(1).strip()

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


def main() -> int:
    issue_number = os.environ.get("ISSUE_NUMBER")
    if not issue_number:
        print("ISSUE_NUMBER environment variable is required", file=sys.stderr)
        return 1

    config_loader = IssueFormConfigLoader()
    trusted_roles = config_loader.trusted_roles
    form_fields = config_loader.form_fields
    table_fields = config_loader.table_fields

    body = run_cmd(f"gh issue view {issue_number} --json body -q .body")
    if not body:
        print(f"Could not retrieve issue #{issue_number} body.", file=sys.stderr)
        return 1

    comments_json = run_cmd(f"gh issue view {issue_number} --json comments -q .comments")
    comments: List[str] = []
    if comments_json:
        try:
            comments_data = json.loads(comments_json)
            if isinstance(comments_data, list):
                for c in comments_data:
                    author_assoc = c.get("authorAssociation", "")
                    if author_assoc in trusted_roles:
                        comments.append(c.get("body", ""))
                    else:
                        print(f"Ignoring comment from untrusted author with association: {author_assoc}")
        except Exception as e:
            print(f"Error parsing comments: {e}", file=sys.stderr)

    org = parse_field(body, form_fields["org"], table_fields["org"])
    title = parse_field(body, form_fields["title"], table_fields["title"])
    year = parse_field(body, form_fields["year"], table_fields["year"])
    url = parse_field(body, form_fields["url"], table_fields["url"])
    category = parse_field(body, form_fields["category"], table_fields["category"])

    all_text = body + "\n" + "\n".join(comments)
    attachment_url = extract_pdf_attachment(all_text)
    if attachment_url:
        print("Found GitHub attachment PDF link! Overriding original URL.")
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

    return 0


if __name__ == "__main__":
    sys.exit(main())
