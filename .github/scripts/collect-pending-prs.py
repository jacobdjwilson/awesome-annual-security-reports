"""
Operational Purpose:
    Gathers list of PDF files that are currently under active conversion or update
    in open automated pull requests. Ensures duplicate PR branches are not created
    and duplicate compute is avoided.

Required Environment Variables:
    GH_TOKEN (optional): GitHub API token for querying open pull requests.
    GITHUB_OUTPUT (optional): Path to write pending_count step output.

Outputs:
    pending_pdf_paths.txt: List of PDF paths currently being processed in open PRs.
    pending_count (int): Count of pending PDF files.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.folders, workflow.pull_request)
"""

import os
import sys
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


class PendingPrsConfigLoader:
    """Loads directory folder paths and PR filters from workflow-config.json with fail-fast validation."""

    def __init__(self, artifacts_dir: str = ".github/artifacts") -> None:
        self.config_path = Path(artifacts_dir) / "workflow-config.json"
        self.folders_cfg, self.pr_cfg = self._load()

    def _load(self) -> tuple[Dict[str, Any], Dict[str, Any]]:
        if not self.config_path.exists():
            raise FileNotFoundError(f"Missing required artifact: '{self.config_path}'.")
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            raise ValueError(f"Failed to parse JSON artifact '{self.config_path}': {e}") from e

        workflow = data.get("workflow", {})
        folders = workflow.get("folders")
        pr = workflow.get("pull_request")

        if not folders or not isinstance(folders, dict):
            raise KeyError(f"Missing 'workflow.folders' in '{self.config_path}'.")
        if not pr or not isinstance(pr, dict):
            raise KeyError(f"Missing 'workflow.pull_request' in '{self.config_path}'.")

        return folders, pr

    @property
    def md_folder(self) -> str:
        val = self.folders_cfg.get("markdown_conversions")
        if not val:
            raise KeyError(f"Missing 'markdown_conversions' in workflow.folders of '{self.config_path}'.")
        return str(val)

    @property
    def pdf_source(self) -> str:
        val = self.folders_cfg.get("pdf_source")
        if not val:
            raise KeyError(f"Missing 'pdf_source' in workflow.folders of '{self.config_path}'.")
        return str(val)

    @property
    def automated_labels(self) -> List[str]:
        labels = self.pr_cfg.get("labels")
        if not isinstance(labels, list) or not labels:
            raise KeyError(f"Missing or empty 'labels' in workflow.pull_request of '{self.config_path}'.")
        return [str(lbl) for lbl in labels]

    @property
    def branch_prefix(self) -> str:
        prefix = self.pr_cfg.get("branch_prefix")
        if not prefix:
            raise KeyError(f"Missing 'branch_prefix' in workflow.pull_request of '{self.config_path}'.")
        return str(prefix)


def main() -> int:
    loader = PendingPrsConfigLoader()
    md_folder = loader.md_folder
    pdf_source = loader.pdf_source
    primary_label = loader.automated_labels[0]

    result = subprocess.run(
        [
            "gh",
            "pr",
            "list",
            "--state",
            "open",
            "--label",
            primary_label,
            "--json",
            "headRefName",
            "-q",
            ".[].headRefName",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        print(f"Error fetching open PRs via gh CLI: {result.stderr}", file=sys.stderr)
        return 1

    branches = [b.strip() for b in result.stdout.split("\n") if b.strip()]
    pending_pdfs: List[str] = []

    if not branches:
        print("⊘ No open automated PRs — no paths to exclude")
    else:
        print("Open automated PR branches:")
        for branch in branches:
            print(f"  {branch}")
            subprocess.run(
                ["git", "fetch", "origin", branch, "--depth=1"],
                capture_output=True,
                check=False,
            )

            diff_res = subprocess.run(
                [
                    "git",
                    "diff",
                    "--name-only",
                    "HEAD",
                    f"origin/{branch}",
                    "--",
                    f"{md_folder}/",
                ],
                capture_output=True,
                text=True,
                check=False,
            )

            md_files = [m.strip() for m in diff_res.stdout.split("\n") if m.strip()]
            for md_file in md_files:
                pdf_path = md_file.replace(md_folder, pdf_source).replace(".md", ".pdf")
                pending_pdfs.append(pdf_path)
                print(f"    → will skip: {pdf_path}")

    with open("pending_pdf_paths.txt", "w", encoding="utf-8") as f:
        for pdf in pending_pdfs:
            f.write(pdf + "\n")

    pending_count = len(pending_pdfs)
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as f:
            f.write(f"pending_count={pending_count}\n")

    print(f"✓ PDFs with pending conversions in open PRs: {pending_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
