"""
Operational Purpose:
    Generates Pull Request title, branch name, labels, and markdown body from report
    analysis results and VirusTotal scan outputs, replacing embedded inline jq/sed/bash
    logic in security-reports-pipeline.yml.

Required Environment Variables:
    GITHUB_OUTPUT (optional): Path to export pr_title, branch_name, and labels.
    GITHUB_RUN_ID (optional): Action run ID for branch naming and telemetry links.
    GITHUB_REPOSITORY (optional): Repository identifier (owner/repo).

Outputs:
    Writes pr_body.md to working directory.
    Exports pr_title, branch_name, and labels to $GITHUB_OUTPUT.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.pull_request)
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, Any, List, Optional

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class PrContentConfigLoader:
    """Loads pull request configuration from workflow-config.json with fail-fast validation."""

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
        pr_cfg = workflow.get("pull_request")
        if not pr_cfg or not isinstance(pr_cfg, dict):
            raise KeyError(f"Missing 'workflow.pull_request' section in '{self.config_path}'.")
        return pr_cfg

    @property
    def single_template(self) -> str:
        t = self.config.get("single_report_title_template")
        if not t:
            raise KeyError("Missing 'single_report_title_template' in workflow.pull_request.")
        return str(t)

    @property
    def multi_template(self) -> str:
        t = self.config.get("multiple_report_title_template")
        if not t:
            raise KeyError("Missing 'multiple_report_title_template' in workflow.pull_request.")
        return str(t)

    @property
    def branch_prefix(self) -> str:
        p = self.config.get("branch_prefix")
        if not p:
            raise KeyError("Missing 'branch_prefix' in workflow.pull_request.")
        return str(p)

    @property
    def labels(self) -> List[str]:
        lbls = self.config.get("labels", [])
        if not isinstance(lbls, list):
            raise ValueError("'labels' in workflow.pull_request must be a list.")
        return [str(l).strip() for l in lbls if str(l).strip()]


def generate_pr_title(reports: List[Dict[str, Any]], loader: PrContentConfigLoader) -> str:
    count = len(reports)
    if count == 1:
        first = reports[0]
        org = first.get("organization", "Unknown")
        title = first.get("title", "Security Report")
        year = str(first.get("year", ""))
        return loader.single_template.replace("{organization}", org).replace("{title}", title).replace("{year}", year)
    return loader.multi_template.replace("{count}", str(count))


def build_pr_body(
    reports: List[Dict[str, Any]],
    scan_results: List[Dict[str, Any]],
    scan_mode: str,
    conv_ok: str,
    conv_fail: str,
    vt_skipped: bool,
    run_id: str,
    repo: str
) -> str:
    lines = [
        "## 📊 Security Reports Update\n",
        f"**Mode:** `{scan_mode}`  **Reports:** {len(reports)}\n",
        "### 📄 Reports\n"
    ]

    for r in reports:
        org = r.get("organization", "")
        title = r.get("title", "")
        year = r.get("year", "")
        cat = r.get("category", "")
        rtype = r.get("type") or "—"
        summary = r.get("summary", "")
        lines.append(f"#### {org} — {title} ({year})\n")
        lines.append(f"**Category:** {cat}  **Type:** {rtype}\n")
        lines.append(f"**Summary:** {summary}\n")
        lines.append("---\n")

    lines.append("### 🛡️ VirusTotal\n")
    if vt_skipped:
        lines.append("Scan skipped for this run mode.\n")
    elif scan_results:
        lines.append("| File | Verdict | Detections | Report |")
        lines.append("|------|---------|------------|--------|")
        for s in scan_results:
            if s.get("status") == "success":
                f_name = s.get("file", "")
                verdict = s.get("verdict", "")
                detections = f"{s.get('malicious_count', 0) + s.get('suspicious_count', 0)}/{s.get('total_engines', 0)}"
                url = s.get("report_url", "#")
                lines.append(f"| {f_name} | {verdict} | {detections} | [View]({url}) |")
        lines.append("\n")
    else:
        lines.append("No scan results.\n")

    lines.append("### 📈 Conversions\n")
    lines.append(f"- Successful: {conv_ok}  Failed: {conv_fail}\n")
    lines.append("---\n")
    lines.append(f"*Auto-generated by Security Reports Pipeline · [Run #{run_id}](https://github.com/{repo}/actions/runs/{run_id})*\n")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate PR title, body, and metadata.")
    parser.add_argument("--analysis-file", default="analysis.json", help="Path to analysis.json")
    parser.add_argument("--scan-results-file", default="scan_results.json", help="Path to scan_results.json")
    parser.add_argument("--artifacts-dir", default=".github/artifacts", help="Path to artifacts directory")
    parser.add_argument("--output-body-file", default="pr_body.md", help="File to write markdown PR body")
    parser.add_argument("--scan-mode", default="unknown", help="Discovery scan mode")
    parser.add_argument("--conv-ok", default="0", help="Successful conversions count")
    parser.add_argument("--conv-fail", default="0", help="Failed conversions count")
    parser.add_argument("--vt-skipped", default="false", help="Whether VT scan was skipped")
    args = parser.parse_args()

    loader = PrContentConfigLoader(artifacts_dir=args.artifacts_dir)

    analysis_path = Path(args.analysis_file)
    if not analysis_path.exists():
        print(f"Error: Analysis file '{analysis_path}' not found.", file=sys.stderr)
        return 1

    try:
        with open(analysis_path, "r", encoding="utf-8") as f:
            reports = json.load(f)
    except Exception as e:
        print(f"Error reading analysis file '{analysis_path}': {e}", file=sys.stderr)
        return 1

    scan_results = []
    scan_path = Path(args.scan_results_file)
    if scan_path.exists():
        try:
            with open(scan_path, "r", encoding="utf-8") as f:
                scan_results = json.load(f)
        except Exception:
            scan_results = []

    pr_title = generate_pr_title(reports, loader)
    run_id = os.environ.get("GITHUB_RUN_ID", "local")
    repo = os.environ.get("GITHUB_REPOSITORY", "unknown/repo")
    branch_name = f"{loader.branch_prefix}{run_id}"

    body = build_pr_body(
        reports=reports,
        scan_results=scan_results,
        scan_mode=args.scan_mode,
        conv_ok=args.conv_ok,
        conv_fail=args.conv_fail,
        vt_skipped=(args.vt_skipped.lower() == "true"),
        run_id=run_id,
        repo=repo
    )

    with open(args.output_body_file, "w", encoding="utf-8") as f:
        f.write(body)

    gh_output = os.environ.get("GITHUB_OUTPUT")
    if gh_output:
        with open(gh_output, "a", encoding="utf-8") as f:
            f.write(f"pr_title={pr_title}\n")
            f.write(f"branch_name={branch_name}\n")
            f.write("labels<<__EOF__\n")
            for lbl in loader.labels:
                f.write(f"{lbl}\n")
            f.write("__EOF__\n")

    print(f"✓ PR Title: {pr_title}")
    print(f"✓ Branch:   {branch_name}")
    print(f"✓ Labels:   {', '.join(loader.labels)}")
    print(f"✓ Body generated: {args.output_body_file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
