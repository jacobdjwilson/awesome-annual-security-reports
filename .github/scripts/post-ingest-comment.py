"""
Operational Purpose:
    Posts a success acknowledgement comment containing the Pull Request link to
    the ingested suggestion issue and adjusts issue labels ('ingested' added,
    'report-suggestion' removed). Replaces inline bash in ingest-suggestion.yml.

Required Environment Variables:
    GH_TOKEN: GitHub authentication token.
    ISSUE_NUMBER: Target issue number.
    PR_NUMBER: Generated Pull Request number.
    FILE_NAME: Canonical filename of the ingested report.
    GITHUB_REPOSITORY (optional): Repository slug (e.g. owner/repo).

Outputs:
    Standard output logs of GitHub API calls.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.ingest)
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from typing import Dict, Any

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class PostIngestConfigLoader:
    """Loads ingest configuration from workflow-config.json with fail-fast validation."""

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
            raise KeyError(f"Missing 'workflow.ingest' section in '{self.config_path}'.")
        return ingest_cfg


def main() -> int:
    _ = PostIngestConfigLoader()

    issue_number = os.environ.get("ISSUE_NUMBER")
    pr_number = os.environ.get("PR_NUMBER")
    file_name = os.environ.get("FILE_NAME", "Report")
    repo = os.environ.get("GITHUB_REPOSITORY", "jacobdjwilson/awesome-annual-security-reports")

    if not issue_number or not pr_number:
        print("Missing ISSUE_NUMBER or PR_NUMBER. Skipping post-ingest actions.")
        return 0

    pr_url = f"https://github.com/{repo}/pull/{pr_number}"
    comment_body = (
        "✅ **Report successfully ingested!**\n\n"
        f"A pull request has been created to add this report to the repository:\n"
        f"👉 **#{pr_number}** — [{file_name}]({pr_url})\n\n"
        "Once the PR is merged, the **Security Reports Processing Pipeline** will automatically:\n"
        "1. Scan the PDF with VirusTotal\n"
        "2. Convert the PDF to Markdown\n"
        "3. Generate an AI summary and category assignment\n"
        "4. Add the report to the README\n\n"
        "Thank you for contributing to **Awesome Annual Security Reports**! 🎉"
    )

    print(f"Posting PR ingestion comment to #{issue_number}...")
    subprocess.run(["gh", "issue", "comment", str(issue_number), "--body", comment_body], capture_output=True)

    print("Updating issue labels...")
    subprocess.run(
        ["gh", "label", "create", "ingested", "--color", "0e8a16", "--description", "Report has been ingested into a PR"],
        capture_output=True,
    )
    subprocess.run(
        ["gh", "issue", "edit", str(issue_number), "--add-label", "ingested", "--remove-label", "report-suggestion"],
        capture_output=True,
    )

    print("✓ Ingestion acknowledgement complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
