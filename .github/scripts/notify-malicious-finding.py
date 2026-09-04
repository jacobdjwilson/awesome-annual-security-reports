"""
Operational Purpose:
    Creates an urgent security incident issue when the daily VirusTotal scanner
    identifies a malicious PDF in the repository. Replaces inline actions/github-script
    in virustotal-daily-scan.yml.

Required Environment Variables:
    GH_TOKEN: GitHub authentication token.
    GITHUB_REPOSITORY (optional): Repository slug.
    GITHUB_RUN_ID (optional): Workflow run ID for action log reference.

Outputs:
    Standard output logs of GitHub issue creation.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.virustotal)
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


class VtNotificationConfigLoader:
    """Loads VirusTotal configuration from workflow-config.json with fail-fast validation."""

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
        vt_cfg = workflow.get("virustotal")
        if not vt_cfg or not isinstance(vt_cfg, dict):
            raise KeyError(f"Missing 'workflow.virustotal' in '{self.config_path}'.")
        return vt_cfg


def main() -> int:
    _ = VtNotificationConfigLoader()

    run_id = os.environ.get("GITHUB_RUN_ID", "unknown")
    repo = os.environ.get("GITHUB_REPOSITORY", "jacobdjwilson/awesome-annual-security-reports")

    title = "🚨 Malicious File Detected in Repository"
    body = (
        "The daily VirusTotal background scanner detected one or more Malicious files in the repository.\n\n"
        f"Please check the [Action Run Logs](https://github.com/{repo}/actions/runs/{run_id}) for details "
        "and remove or quarantine the affected file(s) immediately."
    )

    print(f"Creating incident issue: '{title}'...")
    res = subprocess.run(
        ["gh", "issue", "create", "--title", title, "--body", body, "--label", "security"],
        capture_output=True,
        text=True,
    )
    if res.returncode != 0:
        # Retry without label if label doesn't exist
        res = subprocess.run(
            ["gh", "issue", "create", "--title", title, "--body", body],
            capture_output=True,
            text=True,
        )
        if res.returncode != 0:
            print(f"Failed to create incident issue: {res.stderr.strip()}", file=sys.stderr)
            return 1

    print(f"✓ Incident issue created: {res.stdout.strip()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
