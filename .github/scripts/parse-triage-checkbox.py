"""
Operational Purpose:
    Parses issue checkboxes edited by human maintainers to determine the triage outcome
    (Accept, Duplicate, False Positive, Mismatch), mapping the outcome to appropriate
    issue labels and lifecycle actions (closing negative suggestions). Replaces inline bash
    in issue-triage.yml.

Required Environment Variables:
    GH_TOKEN: GitHub token for CLI authentication.
    ISSUE_NUMBER: Issue number being triaged.
    ISSUE_AUTHOR: Actor performing the edit.
    ISSUE_TITLE: Title of the issue being triaged.
    GITHUB_OUTPUT (optional): Path to write step outputs.

Outputs:
    valid (bool): 'true' if an actionable checkbox was checked, 'false' otherwise.
    outcome (str): One of 'true_positive', 'duplicate', 'false_positive', 'mismatch'.
    label (str): Associated label name defined in workflow-config.json.
    close (bool): 'true' if the issue should be closed, 'false' if accepted.
    author (str): Maintainer username.
    issue (str): Issue number.
    title (str): Issue title.
    reason (str): Reason description for audit trail.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.issue_triage)
"""

import os
import sys
import json
import re
import uuid
import subprocess
from pathlib import Path
from typing import Dict, Any, Optional, Tuple

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class TriageCheckboxConfigLoader:
    """Loads issue triage configuration from workflow-config.json with fail-fast validation."""

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
        triage_cfg = workflow.get("issue_triage")
        if not triage_cfg or not isinstance(triage_cfg, dict):
            raise KeyError(f"Missing 'workflow.issue_triage' section in '{self.config_path}'.")
        return triage_cfg

    @property
    def labels(self) -> Dict[str, Any]:
        lbls = self.config.get("labels")
        if not isinstance(lbls, dict) or not lbls:
            raise KeyError(f"Missing 'labels' dictionary in 'workflow.issue_triage' of '{self.config_path}'.")
        return lbls


def get_issue_body(issue_number: str) -> str:
    """Fetch the raw issue body via gh CLI."""
    cmd = ["gh", "issue", "view", str(issue_number), "--json", "body", "-q", ".body"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"Failed to fetch issue body for #{issue_number}: {res.stderr.strip()}")
    return res.stdout.strip()


def parse_checkboxes(body: str) -> Optional[Tuple[str, str, bool]]:
    """
    Parses issue body for checked triage boxes.
    Returns (outcome, label, close_issue) or None if no match.
    """
    patterns = [
        (r"\[x\]\s+\*\*Accept\*\*", "true_positive", "accepted", False),
        (r"\[x\]\s+\*\*Duplicate\*\*", "duplicate", "duplicate", True),
        (r"\[x\]\s+\*\*False\s+Positive\*\*", "false_positive", "false-positive", True),
        (r"\[x\]\s+\*\*Mismatch\*\*", "mismatch", "mismatch", True),
    ]

    for pattern, outcome, label, close in patterns:
        if re.search(pattern, body, re.IGNORECASE):
            return outcome, label, close
    return None


def main() -> int:
    issue_number = os.environ.get("ISSUE_NUMBER")
    if not issue_number:
        print("Error: Required environment variable 'ISSUE_NUMBER' is missing.", file=sys.stderr)
        return 1

    issue_author = os.environ.get("ISSUE_AUTHOR", "unknown")
    issue_title = os.environ.get("ISSUE_TITLE", "")
    gh_output = os.environ.get("GITHUB_OUTPUT")

    loader = TriageCheckboxConfigLoader()
    allowed_labels = loader.labels

    try:
        body = get_issue_body(issue_number)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    match = parse_checkboxes(body)
    if not match:
        print("No triage checkboxes checked. Setting valid=false.")
        if gh_output:
            with open(gh_output, "a", encoding="utf-8") as f:
                f.write("valid=false\n")
        return 0

    outcome, label, close = match
    if label not in allowed_labels:
        raise KeyError(
            f"Derived label '{label}' is not configured under 'workflow.issue_triage.labels' in workflow-config.json."
        )

    print(f"✓ Triage matched: outcome='{outcome}', label='{label}', close={close}")

    if gh_output:
        delim = str(uuid.uuid4())
        with open(gh_output, "a", encoding="utf-8") as f:
            f.write("valid=true\n")
            f.write(f"outcome={outcome}\n")
            f.write(f"label={label}\n")
            f.write(f"close={'true' if close else 'false'}\n")
            f.write(f"author={issue_author}\n")
            f.write(f"issue={issue_number}\n")
            f.write(f"title<<{delim}\n{issue_title}\n{delim}\n")
            f.write("reason=Triaged via issue checkbox\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
