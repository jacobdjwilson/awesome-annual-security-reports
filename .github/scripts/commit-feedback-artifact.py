"""
Operational Purpose:
    Safely commits and pushes updates to .github/artifacts/discovery-feedback.json
    when triage feedback or learner adjustments are recorded. Replaces inline bash
    git operations in issue-triage.yml and discovery-feedback-learner.yml.

Required Environment Variables:
    None. (Uses Git CLI context and optional ISSUE_NUMBER or COMMIT_MESSAGE).

Outputs:
    Standard output logs of git stage, commit, and push operations.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.issue_triage.feedback_artifact_path)
"""

import os
import sys
import json
import argparse
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Tuple

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class FeedbackCommitConfigLoader:
    """Loads triage configuration from workflow-config.json with fail-fast validation."""

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
    def feedback_path(self) -> str:
        p = self.config.get("feedback_artifact_path")
        if not p:
            raise KeyError(f"Missing 'feedback_artifact_path' in 'workflow.issue_triage' of '{self.config_path}'.")
        return str(p)


def run_git(args: List[str]) -> Tuple[int, str, str]:
    res = subprocess.run(["git"] + args, capture_output=True, text=True)
    return res.returncode, res.stdout.strip(), res.stderr.strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Commit and push updated discovery feedback artifact.")
    parser.add_argument("--message", help="Explicit commit message")
    parser.add_argument("--issue", help="Associated issue number")
    parser.add_argument("--artifacts-dir", default=".github/artifacts", help="Path to artifacts directory")
    args = parser.parse_args()

    loader = FeedbackCommitConfigLoader(artifacts_dir=args.artifacts_dir)
    target_file = loader.feedback_path

    if not Path(target_file).exists():
        print(f"Error: Target feedback artifact '{target_file}' does not exist.", file=sys.stderr)
        return 1

    issue_num = args.issue or os.environ.get("ISSUE") or os.environ.get("ISSUE_NUMBER")
    if args.message:
        commit_msg = args.message
    elif issue_num:
        commit_msg = f"chore: record triage feedback for #{issue_num}"
    else:
        date_str = datetime.now().strftime("%Y-%m-%d")
        commit_msg = f"chore: update discovery scoring from feedback learner [{date_str}]"

    run_git(["config", "user.name", "github-actions[bot]"])
    run_git(["config", "user.email", "github-actions[bot]@users.noreply.github.com"])

    ret, _, err = run_git(["add", target_file])
    if ret != 0:
        print(f"Error staging {target_file}: {err}", file=sys.stderr)
        return 1

    ret, _, _ = run_git(["diff", "--cached", "--quiet"])
    if ret == 0:
        print(f"No changes detected in '{target_file}'. Skipping commit.")
        return 0

    print(f"Committing changes: {commit_msg}")
    ret, out, err = run_git(["commit", "-m", commit_msg])
    if ret != 0:
        print(f"Commit failed: {err}\n{out}", file=sys.stderr)
        return 1

    print("Pushing to remote...")
    ret, out, err = run_git(["push"])
    if ret != 0:
        print(f"Push failed (concurrent commit possible): {err}\nAttempting rebase push...", file=sys.stderr)
        rebase_ret, _, rebase_err = run_git(["pull", "--rebase", "origin", "main"])
        if rebase_ret == 0:
            retry_push_ret, _, retry_push_err = run_git(["push"])
            if retry_push_ret == 0:
                print("✓ Successfully pushed after rebase.")
                return 0
            print(f"Push retry failed: {retry_push_err}", file=sys.stderr)
        else:
            print(f"Rebase failed: {rebase_err}", file=sys.stderr)
        # Avoid failing the triage job if a concurrent push won
        return 0

    print("✓ Successfully committed and pushed feedback artifact.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
