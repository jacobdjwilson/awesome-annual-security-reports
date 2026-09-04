"""
Operational Purpose:
    Parses awesome-lint output, filters allowed rule exceptions (e.g., duplicate vendor
    landing pages configured in .github/artifacts/workflow-config.json), emits GitHub
    Actions diagnostic annotations (::error and ::warning), and exports workflow step
    outputs (lint_status, error_count) with standardized process exit codes.

Required Environment Variables:
    GITHUB_OUTPUT (optional): Path to write step output key-value pairs in GitHub Actions.

Outputs:
    lint_status: 'succeeded' or 'failed'
    error_count: Number of unhandled/fatal lint errors detected.
    awesome_lint_findings.json: Structured findings JSON for GitHub issue management.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.lint configuration)
"""

import os
import sys
import re
import json
from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional

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

        workflow = data.get("workflow")
        if not workflow or not isinstance(workflow, dict):
            raise KeyError(f"Root object 'workflow' missing or invalid in '{self.config_path}'.")

        lint_config = workflow.get("lint")
        if not lint_config or not isinstance(lint_config, dict):
            raise KeyError(
                f"Missing 'workflow.lint' section in '{self.config_path}'. "
                "Define 'workflow.lint' with 'output_file' and 'ignored_rules'."
            )
        return lint_config

    @property
    def output_file(self) -> str:
        out_file = self.config.get("output_file")
        if not out_file:
            raise KeyError(f"Missing 'output_file' in 'workflow.lint' within '{self.config_path}'.")
        return str(out_file)

    @property
    def ignored_rules(self) -> List[str]:
        rules = self.config.get("ignored_rules", [])
        if not isinstance(rules, list):
            raise ValueError(f"'ignored_rules' in 'workflow.lint' must be a list of strings.")
        return [str(r).lower() for r in rules]

    @property
    def target_file(self) -> str:
        return str(self.config.get("target_file", "README.md"))


def parse_lint_output(
    lines: List[str],
    default_file: str,
    ignored_rules: List[str]
) -> Tuple[List[Tuple[str, str, str, str, str]], List[Tuple[str, str, str, str, str]], int]:
    """
    Parses awesome-lint console output.
    Returns:
        (errors, warnings, ignored_count)
        Each tuple contains (file_name, line_num, col_num, message, rule)
    """
    errors: List[Tuple[str, str, str, str, str]] = []
    warnings: List[Tuple[str, str, str, str, str]] = []
    ignored_count = 0

    issue_pattern = re.compile(r'^\s*([✖⚠])\s+(\d+):(\d+)\s+(.*?)\s{2,}([\w\-:/]+)\s*$')
    file_pattern = re.compile(r'^\s*([a-zA-Z0-9_\-./\\]+\.md)(?::(\d+):(\d+))?\s*$')

    current_file = default_file

    for line in lines:
        clean_line = line.rstrip()
        if not clean_line:
            continue

        # Skip awesome-lint execution banner and summary lines
        stripped = clean_line.strip()
        if stripped in ("✖ Linting", "- Linting", "✔ Linting") or re.match(r'^\d+\s+(?:warning|error)s?$', stripped):
            continue

        file_match = file_pattern.match(clean_line)
        if file_match and not clean_line.strip().startswith(('✖', '⚠', '-')):
            current_file = file_match.group(1).strip()
            continue

        issue_match = issue_pattern.match(clean_line)
        if issue_match:
            severity_char, line_num, col_num, message, rule = issue_match.groups()
            rule = rule.strip()
            message = message.strip()

            if any(ignored in rule.lower() for ignored in ignored_rules):
                ignored_count += 1
                continue

            if severity_char == '✖':
                errors.append((current_file, line_num, col_num, message, rule))
            else:
                warnings.append((current_file, line_num, col_num, message, rule))
            continue

        # Fallback for alternative single-line or colon-separated formats
        if "✖" in clean_line or "⚠" in clean_line:
            is_error = "✖" in clean_line
            sep = '✖' if is_error else '⚠'
            if any(ignored in clean_line.lower() for ignored in ignored_rules):
                ignored_count += 1
                continue
            parts = re.split(f'[:{sep}]', clean_line)
            if len(parts) >= 5:
                fn = parts[0].strip() or current_file
                ln = parts[1].strip()
                col = parts[2].strip()
                msg = ":".join(parts[3:]).strip()
                target_list = errors if is_error else warnings
                target_list.append((fn, ln, col, msg, "general-error" if is_error else "general-warning"))
            else:
                target_list = errors if is_error else warnings
                target_list.append((current_file, "1", "1", clean_line.strip(), "general-error" if is_error else "general-warning"))

    return errors, warnings, ignored_count


def write_github_output(status: str, error_count: int) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT")
    if output_path:
        try:
            with open(output_path, "a", encoding="utf-8") as f:
                f.write(f"lint_status={status}\n")
                f.write(f"error_count={error_count}\n")
        except Exception as e:
            print(f"Warning: Failed to write to GITHUB_OUTPUT: {e}", file=sys.stderr)


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(description="Parse awesome-lint output and emit annotations / findings.")
    parser.add_argument("--findings-output", default="awesome_lint_findings.json", help="Path to write structured JSON findings.")
    args = parser.parse_args()

    config_loader = LintConfigLoader()
    output_file_path = Path(config_loader.output_file)
    ignored_rules = config_loader.ignored_rules
    target_file = config_loader.target_file
    findings_out_path = Path(args.findings_output)

    if not output_file_path.exists():
        print(f"Lint output file '{output_file_path}' not found. Assuming clean run.", file=sys.stderr)
        write_github_output("succeeded", 0)
        try:
            with open(findings_out_path, "w", encoding="utf-8") as f:
                json.dump({"findings": []}, f, indent=2)
        except Exception as e:
            print(f"Warning: Failed to write empty findings: {e}", file=sys.stderr)
        return 0

    with open(output_file_path, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()

    errors, warnings, ignored_count = parse_lint_output(lines, target_file, ignored_rules)

    if ignored_count > 0:
        print(f"Suppressed {ignored_count} permissible lint warning(s)/error(s) based on configuration.")

    for fn, ln, col, msg, rule in warnings:
        print(f"::warning file={fn},line={ln},col={col}::{msg} ({rule})")

    for fn, ln, col, msg, rule in errors:
        print(f"::error file={fn},line={ln},col={col}::{msg} ({rule})")

    # Construct structured findings for GitHub Issue synchronization
    findings = []
    for fn, ln, col, msg, rule in errors:
        findings.append({
            "category": "awesome_lint_error",
            "severity": "error",
            "file": f"{fn} (Line {ln}:{col})",
            "message": f"{msg} (`{rule}`)"
        })
    for fn, ln, col, msg, rule in warnings:
        findings.append({
            "category": "awesome_lint_warning",
            "severity": "warning",
            "file": f"{fn} (Line {ln}:{col})",
            "message": f"{msg} (`{rule}`)"
        })

    try:
        with open(findings_out_path, "w", encoding="utf-8") as f:
            json.dump({"findings": findings}, f, indent=2)
        print(f"Structured lint findings saved to '{findings_out_path}'.")
    except Exception as e:
        print(f"Warning: Failed to write findings to '{findings_out_path}': {e}", file=sys.stderr)

    error_count = len(errors)
    status = "succeeded" if error_count == 0 else "failed"
    write_github_output(status, error_count)

    if error_count == 0:
        print("Linting succeeded! No unhandled errors found.")
        return 0
    else:
        print(f"::error::Linting failed with {error_count} error(s). See annotations above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
