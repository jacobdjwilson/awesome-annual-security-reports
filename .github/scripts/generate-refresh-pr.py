"""
Operational Purpose:
    Executes README updates for refreshed conversions, inspects git diffs,
    and generates PR title, commit message, branch name, and markdown body.
    Replaces inline bash in refresh-old-conversions.yml.

Required Environment Variables:
    GITHUB_OUTPUT (optional): Path to write step outputs.
    GITHUB_RUN_ID (optional): Workflow run ID for branch naming.
    GITHUB_REPOSITORY (optional): Repository slug.

Outputs:
    changes_detected (bool): 'true' if README or conversions changed, 'false' otherwise.
    pr_title (str): Formatted PR title.
    commit_message (str): Formatted git commit message.
    branch_name (str): Unique branch name.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.validation.validate_toc)
"""

import os
import sys
import json
import argparse
import subprocess
from pathlib import Path
from typing import Dict, Any, List

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class RefreshPrConfigLoader:
    """Loads refresh configuration from workflow-config.json with fail-fast validation."""

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
        val_cfg = workflow.get("validation")
        if not val_cfg or not isinstance(val_cfg, dict):
            raise KeyError(f"Missing 'workflow.validation' in '{self.config_path}'.")
        return val_cfg

    @property
    def validate_toc(self) -> bool:
        val = self.config.get("validate_toc")
        if val is None:
            raise KeyError(f"Missing 'validate_toc' in 'workflow.validation' of '{self.config_path}'.")
        return bool(val)


def main() -> int:
    parser = argparse.ArgumentParser(description="Update README and generate refresh PR content.")
    parser.add_argument("--analysis-file", default="analysis.json", help="Path to analysis.json")
    parser.add_argument("--readme-path", default="README.md", help="Path to README.md")
    parser.add_argument("--artifacts-dir", default=".github/artifacts", help="Path to artifacts directory")
    parser.add_argument("--file-count", default="1", help="Count of refreshed files")
    parser.add_argument("--days-old", default="90", help="Age threshold in days")
    parser.add_argument("--output-body-file", default="refresh_pr_body.md", help="Path to write PR body")
    args = parser.parse_args()

    gh_output = os.environ.get("GITHUB_OUTPUT")

    if not Path(args.analysis_file).exists():
        print(f"No analysis file '{args.analysis_file}' found. Skipping PR generation.")
        if gh_output:
            with open(gh_output, "a", encoding="utf-8") as f:
                f.write("changes_detected=false\n")
        return 0

    loader = RefreshPrConfigLoader(artifacts_dir=args.artifacts_dir)

    cmd = [
        sys.executable,
        ".github/scripts/readme-updater.py",
        args.analysis_file,
        "--readme-path",
        args.readme_path,
        "--artifacts-dir",
        args.artifacts_dir,
    ]
    if loader.validate_toc:
        cmd.append("--validate-toc")

    print(f"Running README updater: {' '.join(cmd)}")
    res = subprocess.run(cmd)
    if res.returncode != 0:
        print("README updater failed.", file=sys.stderr)
        return res.returncode

    # Check git diff for changes
    diff_res = subprocess.run(
        ["git", "diff", "--quiet", "HEAD", "--", args.readme_path, "Markdown Conversions/"],
        capture_output=True,
    )

    if diff_res.returncode == 0:
        print("⊘ No changes detected to commit.")
        if gh_output:
            with open(gh_output, "a", encoding="utf-8") as f:
                f.write("changes_detected=false\n")
        return 0

    print("✓ Changes detected.")
    run_id = os.environ.get("GITHUB_RUN_ID", "local")
    repo = os.environ.get("GITHUB_REPOSITORY", "jacobdjwilson/awesome-annual-security-reports")
    file_count = args.file_count
    days_old = args.days_old

    pr_title = f"♻️ Refresh {file_count} Security Reports"
    commit_msg = f"♻️ Refresh {file_count} stale conversions"
    branch_name = f"refresh-reports-{run_id}"

    body_lines = [
        "## Automated Report Refresh\n",
        f"Refreshed {file_count} reports that were either:\n",
        "- Missing markdown conversions\n",
        f"- Older than {days_old} days\n\n",
        "Markdown files were regenerated from scratch using the full markitdown + AI polish pipeline.\n\n",
        f"**Run:** [#{run_id}](https://github.com/{repo}/actions/runs/{run_id})\n\n",
        "---\n",
        "*Auto-generated by Refresh Old Conversions workflow*\n",
    ]
    body = "".join(body_lines)
    with open(args.output_body_file, "w", encoding="utf-8") as f:
        f.write(body)

    if gh_output:
        with open(gh_output, "a", encoding="utf-8") as f:
            f.write("changes_detected=true\n")
            f.write(f"pr_title={pr_title}\n")
            f.write(f"commit_message={commit_msg}\n")
            f.write(f"branch_name={branch_name}\n")

    print(f"✓ PR metadata written: {pr_title} ({branch_name})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
