"""
Operational Purpose:
    Prepares the target markdown file (README.md) for linting. When invoked during
    pull_request_target workflow events, safely fetches and checks out the target file
    from the pull request head commit while keeping all trusted scripts and configurations
    from the base branch intact.

Required Environment Variables:
    GITHUB_EVENT_NAME: Workflow event trigger name (e.g. 'pull_request_target').
    GITHUB_EVENT_PATH (optional): Path to event JSON payload.
    PR_HEAD_SHA (optional): Specific commit SHA to checkout.

Outputs:
    None. Modifies working tree target file only.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.lint configuration)
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple

# Ensure UTF-8 output across platforms
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class LintConfigLoader:
    """Encapsulates configuration retrieval from workflow-config.json with fail-fast validation."""

    def __init__(self, config_path: str = ".github/artifacts/workflow-config.json") -> None:
        self.config_path = Path(config_path)
        self.config = self._load()

    def _load(self) -> Dict[str, Any]:
        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Missing required artifact: '{self.config_path}'. Ensure repository artifacts are present."
            )
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            raise ValueError(f"Failed to parse JSON artifact '{self.config_path}': {e}") from e

        workflow = data.get("workflow", {})
        lint_config = workflow.get("lint", {})
        if not lint_config:
            raise KeyError(f"Missing 'workflow.lint' section in '{self.config_path}'.")
        return lint_config

    @property
    def target_file(self) -> str:
        return str(self.config.get("target_file", "README.md"))


def run_cmd(cmd: List[str]) -> Tuple[int, str, str]:
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def get_pr_head_sha() -> Optional[str]:
    explicit_sha = os.environ.get("PR_HEAD_SHA")
    if explicit_sha:
        return explicit_sha.strip()

    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if event_path and Path(event_path).exists():
        try:
            with open(event_path, "r", encoding="utf-8") as f:
                payload = json.load(f)
            return payload.get("pull_request", {}).get("head", {}).get("sha")
        except Exception as e:
            print(f"Warning: Failed to parse GITHUB_EVENT_PATH: {e}", file=sys.stderr)
    return None


def main() -> int:
    config_loader = LintConfigLoader()
    target_file = config_loader.target_file

    event_name = os.environ.get("GITHUB_EVENT_NAME", "")
    if event_name != "pull_request_target":
        print(f"Event is '{event_name}'. Target file '{target_file}' remains from current checkout.")
        return 0

    head_sha = get_pr_head_sha()
    if not head_sha:
        print("Warning: Could not determine PR head SHA; using default checked out target file.", file=sys.stderr)
        return 0

    print(f"Fetching and checking out '{target_file}' from PR head SHA: {head_sha}")
    ret, out, err = run_cmd(["git", "fetch", "origin", head_sha, "--depth=1"])
    if ret != 0:
        print(f"Error fetching PR head commit {head_sha}: {err}", file=sys.stderr)
        return 1

    ret, out, err = run_cmd(["git", "checkout", "FETCH_HEAD", "--", target_file])
    if ret != 0:
        print(f"Error checking out {target_file} from FETCH_HEAD: {err}", file=sys.stderr)
        return 1

    print(f"Successfully prepared '{target_file}' from PR head {head_sha} for linting.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
