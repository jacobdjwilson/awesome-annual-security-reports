"""
Operational Purpose:
    Posts a formatted maintainer triage acknowledgement comment to the specified GitHub Issue
    and automatically closes the issue if the triage outcome indicates a negative result
    (duplicate, false positive, mismatch). Replaces inline bash in issue-triage.yml.

Required Environment Variables:
    GH_TOKEN: GitHub authentication token.
    ISSUE_NUMBER: Target issue number.
    OUTCOME: Triage outcome (true_positive, duplicate, false_positive, mismatch).
    AUTHOR: Maintainer username who performed the triage.
    CLOSE (optional): 'true' to close the issue, 'false' otherwise.

Outputs:
    Standard output logs of comment posting and closure operations.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.issue_triage)
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


class TriageAckConfigLoader:
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


ICONS = {
    "true_positive": "✅",
    "false_positive": "🚫",
    "duplicate": "🔁",
    "mismatch": "⚠️",
}


def run_gh(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(["gh"] + cmd, capture_output=True, text=True)


def main() -> int:
    issue_number = os.environ.get("ISSUE_NUMBER")
    outcome = os.environ.get("OUTCOME")
    author = os.environ.get("AUTHOR", "maintainer")
    should_close = os.environ.get("CLOSE", "false").lower() == "true"

    if not issue_number or not outcome:
        print("Error: Missing required environment variables 'ISSUE_NUMBER' or 'OUTCOME'.", file=sys.stderr)
        return 1

    # Validate config artifact presence
    _ = TriageAckConfigLoader()

    icon = ICONS.get(outcome, "ℹ️")
    comment_body = (
        f"{icon} **Triaged as `{outcome}`** by @{author} via checkbox.\n\n"
        "_This outcome will be incorporated into the next discovery feedback learner run to improve future searches._"
    )

    print(f"Posting triage comment to #{issue_number}...")
    res = run_gh(["issue", "comment", str(issue_number), "--body", comment_body])
    if res.returncode != 0:
        print(f"Warning: Failed to post triage comment: {res.stderr.strip()}", file=sys.stderr)
    else:
        print(f"✓ Comment posted to #{issue_number}.")

    if should_close:
        print(f"Closing issue #{issue_number} (outcome: {outcome})...")
        res = run_gh(["issue", "close", str(issue_number), "--reason", "not planned"])
        if res.returncode != 0:
            # Retry without --reason if unsupported
            res = run_gh(["issue", "close", str(issue_number)])
            if res.returncode != 0:
                print(f"Error closing issue #{issue_number}: {res.stderr.strip()}", file=sys.stderr)
                return 1
        print(f"✓ Issue #{issue_number} closed.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
