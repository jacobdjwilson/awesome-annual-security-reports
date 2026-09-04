"""
Operational Purpose:
    Parses readme_audit_findings.json and writes a formatted markdown breakdown of
    audit issues into the GitHub Actions Step Summary. Replaces inline bash in readme-audit.yml.

Required Environment Variables:
    GITHUB_STEP_SUMMARY (optional): Path to step summary markdown file.

Outputs:
    Writes summary markdown to $GITHUB_STEP_SUMMARY.

JSON Artifact Dependencies:
    .github/artifacts/readme_audit_findings.json
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, Any, List

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate README audit step summary.")
    parser.add_argument(
        "--findings-file",
        default=".github/artifacts/readme_audit_findings.json",
        help="Path to audit findings file",
    )
    args = parser.parse_args()

    findings_path = Path(args.findings_file)
    summary_lines = ["## 📊 README Audit Results\n"]

    if not findings_path.exists():
        summary_lines.append("Audit failed to produce a findings file.\n")
    else:
        try:
            with open(findings_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            total = 0
            category_counts = {}
            if isinstance(data, dict):
                for cat, items in data.items():
                    cnt = len(items) if isinstance(items, list) else 0
                    category_counts[cat] = cnt
                    total += cnt

            summary_lines.append(f"Found **{total}** potential issues.\n")
            if category_counts:
                summary_lines.append("| Category | Count |")
                summary_lines.append("| :--- | :--- |")
                for cat, cnt in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
                    summary_lines.append(f"| {cat} | {cnt} |")
                summary_lines.append("\n")

            summary_lines.append("Please download the artifact to review the detailed findings.\n")
        except Exception as e:
            summary_lines.append(f"Error parsing audit findings file: {e}\n")

    summary_content = "\n".join(summary_lines)
    print(summary_content)

    step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if step_summary:
        with open(step_summary, "a", encoding="utf-8") as f:
            f.write(summary_content + "\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
