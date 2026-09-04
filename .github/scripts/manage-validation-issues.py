"""
Operational Purpose:
    Synchronizes repository validation findings (from validation_findings.json)
    with GitHub Issues across validation domains (Links, Integrity, Structure).
    Deduplicates updates via embedded issue body fingerprints and automatically closes
    resolved domain issues.

Required Environment Variables:
    GH_TOKEN (optional): GitHub authentication token for gh CLI issue commands.

Outputs:
    Standard output logs of issue search, update, close, and creation actions.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.validation.issue_domains, workflow.validation.category_labels)
"""

import os
import re
import sys
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Any, Optional

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class ValidationIssuesConfigLoader:
    """Loads validation domains and category labels configuration with fail-fast validation."""

    def __init__(self, artifacts_dir: str = ".github/artifacts") -> None:
        self.config_path = Path(artifacts_dir) / "workflow-config.json"
        self.validation_cfg = self._load()

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
            raise KeyError(f"Missing 'workflow.validation' configuration in '{self.config_path}'.")

        required_keys = ["issue_domains", "category_labels"]
        for key in required_keys:
            if key not in val_cfg:
                raise KeyError(f"Missing required key '{key}' in 'workflow.validation' of '{self.config_path}'.")

        return val_cfg

    @property
    def issue_domains(self) -> Dict[str, List[str]]:
        return dict(self.validation_cfg["issue_domains"])

    @property
    def category_labels(self) -> Dict[str, str]:
        return dict(self.validation_cfg["category_labels"])


def run_gh(command: List[str]) -> str:
    """Runs a gh CLI command and returns stripped stdout."""
    try:
        result = subprocess.run(
            ["gh"] + command,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running gh command {' '.join(command)}: {e.stderr}", file=sys.stderr)
        return ""


def generate_markdown(
    domain: str,
    findings: List[Dict[str, Any]],
    category_labels: Dict[str, str],
) -> str:
    """Renders GitHub Issue Markdown body with embedded fingerprints."""
    errors = [f for f in findings if f.get("severity") == "error"]
    warnings = [f for f in findings if f.get("severity") == "warning"]

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        f"# Repository Integrity Validation: {domain}\n",
        f"*Generated: {timestamp}*\n",
    ]

    if not findings:
        lines += [
            "## ✅ All Checks Passed\n",
            f"No issues found in the {domain} domain.\n",
        ]
    else:
        lines += [
            "## ⚠️ Issues Found\n",
            f"Found **{len(errors)}** error(s) and **{len(warnings)}** warning(s):\n",
        ]

        grouped: Dict[str, List[Dict[str, Any]]] = {}
        for f in findings:
            grouped.setdefault(f["category"], []).append(f)

        for cat, label in category_labels.items():
            if cat not in grouped:
                continue
            lines.append(f"### {label}\n")
            for f in grouped[cat]:
                icon = "❌" if f.get("severity") == "error" else "⚠️"
                lines.append(f"- {icon} **`{f['file']}`**")
                if f.get("message"):
                    lines.append(f"  <br/>*{f['message']}*")
            lines.append("")

    fps = [f"{f['category']}:{f['file']}" for f in findings]
    fps.sort()
    lines.append(f"\n<!-- fingerprints: {';'.join(fps)} -->\n")

    return "\n".join(lines)


def main() -> int:
    findings_path = Path("validation_findings.json")
    if not findings_path.exists():
        print(f"'{findings_path}' not found — nothing to process.")
        return 0

    loader = ValidationIssuesConfigLoader()
    issue_domains = loader.issue_domains
    category_labels = loader.category_labels

    try:
        with open(findings_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error parsing '{findings_path}': {e}", file=sys.stderr)
        return 1

    all_findings = data.get("findings", [])

    for domain, categories in issue_domains.items():
        domain_findings = [f for f in all_findings if f.get("category") in categories]
        title = f"Repository Integrity Validation: {domain}"
        print(f"Processing domain: {domain} ({len(domain_findings)} findings)")

        search_res = run_gh([
            "issue",
            "list",
            "--state",
            "open",
            "--label",
            "automated-check",
            "--search",
            f'"{title}" in:title',
            "--json",
            "number,body",
        ])

        existing_issue: Optional[Dict[str, Any]] = None
        if search_res:
            try:
                issues = json.loads(search_res)
                if issues and isinstance(issues, list):
                    existing_issue = issues[0]
            except Exception:
                pass

        current_fps = sorted([f"{f['category']}:{f['file']}" for f in domain_findings])
        current_fp_str = ";".join(current_fps)

        previous_fp_str = ""
        if existing_issue and "body" in existing_issue:
            m = re.search(r"<!-- fingerprints:\s*(.*?)\s*-->", existing_issue["body"])
            if m:
                previous_fp_str = m.group(1).strip()

        if not domain_findings:
            if existing_issue:
                print(f"  Closing issue #{existing_issue['number']} - all issues resolved!")
                run_gh(["issue", "comment", str(existing_issue["number"]), "--body", "✅ All issues in this domain have been resolved!"])
                run_gh(["issue", "close", str(existing_issue["number"])])
            else:
                print("  No findings, no issue exists. Skipping.")
            continue

        if existing_issue and current_fp_str == previous_fp_str:
            print("  Fingerprints unchanged. Skipping update to prevent duplicate noise.")
            continue

        markdown_body = generate_markdown(domain, domain_findings, category_labels)

        if existing_issue:
            print(f"  Closing outdated issue #{existing_issue['number']} and opening refreshed issue...")
            run_gh(["issue", "close", str(existing_issue["number"]), "-r", "not planned"])

        print("  Creating new issue...")
        temp_file = Path("temp_issue.md")
        with open(temp_file, "w", encoding="utf-8") as f:
            f.write(markdown_body)

        run_gh(["issue", "create", "--title", title, "--body-file", str(temp_file), "--label", "automated-check,bug"])
        if temp_file.exists():
            temp_file.unlink()

    return 0


if __name__ == "__main__":
    sys.exit(main())
