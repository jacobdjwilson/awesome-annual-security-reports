"""
Operational Purpose:
    Validates mandatory issue fields (URL, 4-digit Year, Organization) extracted from
    an issue form suggestion. If invalid, logs descriptive errors, optionally posts
    a remediation guide comment directly to the GitHub Issue via the GitHub CLI, and exits
    with a non-zero code. Replaces inline bash validation in ingest-suggestion.yml.

Required Environment Variables:
    URL (optional): Report URL.
    YEAR (optional): Report Year.
    ORG (optional): Organization Name.
    ISSUE_NUMBER (optional): Issue number to comment upon failure.
    GH_TOKEN (optional): GitHub token for issue comment posting.
    GITHUB_OUTPUT (optional): Path to write step outputs.

Outputs:
    valid (bool): 'true' if all fields pass validation, 'false' otherwise.
    errors (str): Multi-line string describing validation failures.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.ingest)
"""

import os
import sys
import re
import json
import subprocess
from pathlib import Path
from typing import Dict, Any, List

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class IngestValidationConfigLoader:
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
    _ = IngestValidationConfigLoader()

    url = (os.environ.get("URL") or "").strip()
    year = (os.environ.get("YEAR") or "").strip()
    org = (os.environ.get("ORG") or "").strip()
    issue_number = os.environ.get("ISSUE_NUMBER")
    gh_output = os.environ.get("GITHUB_OUTPUT")

    errors: List[str] = []

    if not url:
        errors.append("- Report URL is empty")
    elif not (url.startswith("http://") or url.startswith("https://")):
        errors.append(f"- Report URL must be an HTTP(S) link: {url}")

    if not year or not re.match(r"^[0-9]{4}$", year):
        errors.append("- Report year is missing or not a 4-digit number")

    if not org:
        errors.append("- Organization name is empty")

    if errors:
        error_msg = "\n".join(errors)
        print(f"Validation failed:\n{error_msg}", file=sys.stderr)

        if gh_output:
            with open(gh_output, "a", encoding="utf-8") as f:
                f.write("valid=false\n")
                f.write(f"errors={error_msg}\n")

        if issue_number and os.environ.get("GH_TOKEN"):
            comment_body = (
                "❌ **Could not process this suggestion** — one or more required fields are missing or invalid.\n\n"
                "Please edit the issue and ensure the following fields are correctly filled in:\n"
                f"{error_msg}\n\n"
                "Once corrected, remove and re-add the `report-suggestion` label to re-trigger processing."
            )
            print(f"Posting validation failure comment to #{issue_number}...")
            subprocess.run(
                ["gh", "issue", "comment", str(issue_number), "--body", comment_body],
                capture_output=True,
                text=True,
            )

        return 1

    print("✓ Ingest fields validated successfully.")
    if gh_output:
        with open(gh_output, "a", encoding="utf-8") as f:
            f.write("valid=true\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
