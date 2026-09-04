"""
Operational Purpose:
    Applies triage outcome labels to GitHub issues and removes conflicting previous
    triage labels according to the schema defined in workflow-config.json.

Required Environment Variables:
    ISSUE_NUMBER: Target GitHub issue number.
    LABEL: Name of the label to apply.
    GH_TOKEN (optional): GitHub authentication token.

Outputs:
    Standard output logs of label creation and issue tagging operations.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.issue_triage.labels, workflow.issue_triage.default_label_color)
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


class TriageLabelConfigLoader:
    """Loads issue triage label configurations with fail-fast validation."""

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
            raise KeyError(f"Missing 'workflow.issue_triage' in '{self.config_path}'.")

        required_keys = ["labels", "default_label_color"]
        for k in required_keys:
            if k not in triage_cfg:
                raise KeyError(f"Missing required key '{k}' in 'workflow.issue_triage' of '{self.config_path}'.")

        return triage_cfg

    @property
    def labels(self) -> Dict[str, Dict[str, str]]:
        return dict(self.config["labels"])

    @property
    def default_color(self) -> str:
        return str(self.config["default_label_color"])


def run_cmd(cmd: str) -> None:
    """Runs command ignoring expected idempotent errors (e.g. label already exists or not on issue)."""
    try:
        subprocess.run(
            cmd,
            shell=True,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    except subprocess.CalledProcessError:
        pass


def main() -> int:
    issue_number = os.environ.get("ISSUE_NUMBER")
    label = os.environ.get("LABEL")

    if not issue_number or not label:
        print("ISSUE_NUMBER and LABEL environment variables are required.", file=sys.stderr)
        return 1

    loader = TriageLabelConfigLoader()
    labels_config = loader.labels
    default_color = loader.default_color

    if label not in labels_config:
        print(f"Warning: label '{label}' not explicitly defined in labels config. Using default color: {default_color}")
        color = default_color
        description = ""
    else:
        label_meta = labels_config[label]
        color = label_meta.get("color", default_color)
        description = label_meta.get("description", "")

    # Ensure label exists in repository
    run_cmd(f'gh label create "{label}" --color "{color}" --description "{description}"')

    # Remove all mutually exclusive triage outcome labels
    for old_label in labels_config.keys():
        run_cmd(f'gh issue edit "{issue_number}" --remove-label "{old_label}"')

    # Apply the selected label
    print(f"Applying label '{label}' to issue #{issue_number}")
    run_cmd(f'gh issue edit "{issue_number}" --add-label "{label}"')

    return 0


if __name__ == "__main__":
    sys.exit(main())
