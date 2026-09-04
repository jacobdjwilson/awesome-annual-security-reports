"""
Operational Purpose:
    Generates markdown Step Summaries for both the 'discovery' and 'processing' phases
    of the Refresh Old Conversions workflow, formatting status tables and metrics.
    Replaces inline bash step summary scripts in refresh-old-conversions.yml.

Required Environment Variables:
    GITHUB_STEP_SUMMARY (optional): Path to step summary markdown file.
    GITHUB_REPO (optional): Repository slug.
    GITHUB_RUN_ID (optional): Workflow run ID.

Outputs:
    Appends formatted markdown tables to $GITHUB_STEP_SUMMARY.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.conversion, workflow.analysis, workflow.pull_request)
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, Any, Optional

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class RefreshSummaryConfigLoader:
    """Loads workflow configuration from workflow-config.json with fail-fast validation."""

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
        if not workflow or not isinstance(workflow, dict):
            raise KeyError(f"Missing 'workflow' section in '{self.config_path}'.")
        return workflow

    @property
    def max_age_days(self) -> int:
        val = self.config.get("conversion", {}).get("max_age_days")
        if val is None:
            raise KeyError("Missing 'conversion.max_age_days' in workflow-config.json.")
        return int(val)

    @property
    def default_limit(self) -> int:
        val = self.config.get("discovery", {}).get("default_limit")
        if val is None:
            raise KeyError("Missing 'discovery.default_limit' in workflow-config.json.")
        return int(val)

    @property
    def max_open_prs(self) -> int:
        val = self.config.get("pull_request", {}).get("max_open_automated_prs")
        if val is None:
            raise KeyError("Missing 'pull_request.max_open_automated_prs' in workflow-config.json.")
        return int(val)

    @property
    def errors_output_file(self) -> str:
        val = self.config.get("analysis", {}).get("errors_output_file")
        if not val:
            raise KeyError("Missing 'analysis.errors_output_file' in workflow-config.json.")
        return str(val)


def render_discovery_summary(loader: RefreshSummaryConfigLoader) -> str:
    event_name = os.environ.get("GITHUB_EVENT_NAME", "unknown")
    input_limit = os.environ.get("INPUT_LIMIT")
    input_days_old = os.environ.get("INPUT_DAYS_OLD")
    pr_exists = os.environ.get("PR_EXISTS", "false")
    skip_reason = os.environ.get("SKIP_REASON", "")
    open_count = os.environ.get("OPEN_COUNT", "0")
    has_files = os.environ.get("HAS_FILES", "false")
    count = os.environ.get("COUNT", "0")

    final_limit = input_limit if input_limit and input_limit.strip() else str(loader.default_limit)
    final_days = input_days_old if input_days_old and input_days_old.strip() else str(loader.max_age_days)
    max_prs = str(loader.max_open_prs)

    lines = [
        "## ♻️ Refresh Old Conversions — Discovery\n",
        "| Detail | Value |",
        "|--------|-------|",
        f"| Trigger | `{event_name}` |",
        f"| Limit | `{final_limit}` |",
        f"| Min Age (days) | `{final_days}` |",
        f"| Open Automated PRs | {open_count} / {max_prs} |\n",
    ]

    if pr_exists == "true":
        if skip_reason == "pr_cap_reached":
            lines.extend([
                "### ⏸️ PR Cap Reached\n",
                f"**{open_count} open automated PRs** — at or above the cap of **{max_prs}**.\n",
                "Review and merge or close open automated PRs to unblock future refresh runs.\n",
            ])
        else:
            lines.append("⊘ **Skipped** — An open refresh PR already exists.\n")
    elif has_files == "true":
        lines.append(f"✅ Found **{count}** file(s) to refresh. Processing job will follow.\n")
    else:
        lines.append("⊘ No stale conversions found requiring refresh.\n")

    return "\n".join(lines)


def render_processing_summary(loader: RefreshSummaryConfigLoader) -> str:
    repo = os.environ.get("GITHUB_REPO", "jacobdjwilson/awesome-annual-security-reports")
    run_id = os.environ.get("GITHUB_RUN_ID", "")
    run_url = f"https://github.com/{repo}/actions/runs/{run_id}"

    file_count = os.environ.get("FILE_COUNT") or "0"
    successful = os.environ.get("SUCCESSFUL") or "0"
    failed = os.environ.get("FAILED") or "0"
    pr_num = os.environ.get("PR_NUM") or ""
    days_old = os.environ.get("INPUT_DAYS_OLD") or str(loader.max_age_days)
    changes_detected = os.environ.get("CHANGES_DETECTED") or "false"
    analysis_count = os.environ.get("ANALYSIS_COUNT") or "0"
    analysis_error_count = os.environ.get("ANALYSIS_ERROR_COUNT") or "0"
    errors_file = os.environ.get("ERRORS_FILE") or loader.errors_output_file

    lines = [
        "## ♻️ Refresh Old Conversions — Processing\n",
        "| Result | Count |",
        "|--------|-------|",
        f"| Files Targeted | {file_count} |",
        f"| ✅ Conversions Successful | {successful} |",
        f"| ❌ Conversions Failed | {failed} |",
        f"| Min Age | {days_old} days |",
        "| Conversion Method | markitdown + AI polish (force-reconvert) |\n",
    ]

    if changes_detected == "true":
        if pr_num:
            pr_url = f"https://github.com/{repo}/pull/{pr_num}"
            lines.append(f"✅ Pull request created: [PR #{pr_num}]({pr_url})\n")
    else:
        lines.append("⊘ No README changes detected.\n")

    if Path("conversions.json").exists():
        try:
            with open("conversions.json", "r", encoding="utf-8") as f:
                conversions = json.load(f)
            if conversions:
                lines.append("### 📄 Conversion Detail\n")
                lines.append("| File | Method | Model | Chars | Status |")
                lines.append("|------|--------|-------|-------|--------|")
                for c in conversions:
                    filename = Path(c.get("pdf_path", "")).name
                    method = c.get("method", "—")
                    model = c.get("model", "—")
                    chars = str(c.get("output_chars")) if c.get("output_chars") else "—"
                    status = "✅" if c.get("status") == "success" else f"❌ {c.get('message', '')}"
                    lines.append(f"| `{filename}` | {method} | {model} | {chars} | {status} |")
                lines.append("\n")
        except Exception as e:
            print(f"Error parsing conversions.json: {e}", file=sys.stderr)

    lines.append("### 🧠 Analysis Results\n")
    if int(analysis_count) > 0:
        lines.append("| ✅ Reports Analyzed | ❌ Analysis Failed |")
        lines.append("|---|---|")
        lines.append(f"| {analysis_count} | {analysis_error_count} |\n")
    elif Path(errors_file).exists() and int(analysis_error_count) > 0:
        lines.append("❌ **All report(s) failed AI analysis.**\n")
        lines.append("| Organization | Year | Error Type | Suggested Fix |")
        lines.append("|---|---|---|---|")
        try:
            with open(errors_file, "r", encoding="utf-8") as f:
                errors = json.load(f)
            for e in errors:
                org = e.get("organization", "")
                year = e.get("year", "")
                err_type = e.get("error_type", "")
                sugg = e.get("suggestion", "")[:150].replace("\n", " ").replace("|", "\\|")
                lines.append(f"| **{org}** | {year} | `{err_type}` | {sugg} |")
            lines.append("\n")
        except Exception as e:
            print(f"Error parsing {errors_file}: {e}", file=sys.stderr)
    else:
        lines.append("⊘ No analysis was attempted or data is unavailable.\n")

    lines.append(f"📎 Full details available in [workflow artifacts]({run_url}).\n")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Refresh Old Conversions step summary.")
    parser.add_argument("--step", choices=["discovery", "processing"], default="processing", help="Pipeline step")
    parser.add_argument("--artifacts-dir", default=".github/artifacts", help="Path to artifacts directory")
    args = parser.parse_args()

    loader = RefreshSummaryConfigLoader(artifacts_dir=args.artifacts_dir)

    if args.step == "discovery":
        content = render_discovery_summary(loader)
    else:
        content = render_processing_summary(loader)

    print(content)

    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_file:
        with open(summary_file, "a", encoding="utf-8") as f:
            f.write(content + "\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
