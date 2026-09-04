"""
Operational Purpose:
    Loads core workflow configuration thresholds from workflow-config.json and exports
    them as step outputs to $GITHUB_OUTPUT for downstream workflow orchestration.

Required Environment Variables:
    GITHUB_OUTPUT (optional): Path to write step output variables.

Outputs:
    max_size_mb, default_limit, pdf_magic, pdf_source, md_folder, max_age_days,
    push_mode, push_batch_limit, max_open_prs exported to $GITHUB_OUTPUT.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.discovery, workflow.folders, workflow.conversion, workflow.pull_request)
"""

import json
import os
import sys

from pathlib import Path

def main():
    config_path = Path(".github/artifacts/workflow-config.json")
    if not config_path.exists():
        raise FileNotFoundError(f"Missing required artifact: {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    wf = config.get("workflow", {})
    discovery = wf.get("discovery", {})
    folders = wf.get("folders", {})
    conversion = wf.get("conversion", {})
    pull_request = wf.get("pull_request", {})

    outputs = {
        "max_size_mb": discovery.get("max_file_size_mb"),
        "default_limit": discovery.get("default_limit"),
        "pdf_magic": discovery.get("pdf_magic_number"),
        "pdf_source": folders.get("pdf_source"),
        "md_folder": folders.get("markdown_conversions"),
        "max_age_days": conversion.get("max_age_days"),
        "push_mode": discovery.get("push_mode"),
        "push_batch_limit": discovery.get("push_batch_limit"),
        "max_open_prs": pull_request.get("max_open_automated_prs"),
    }

    for key, val in outputs.items():
        if val is None:
            raise KeyError(f"Required configuration key missing from workflow-config.json: {key}")

    print("✓ Loaded configuration:")
    for k, v in outputs.items():
        print(f"  {k}: {v}")

    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a") as f:
            for k, v in outputs.items():
                f.write(f"{k}={v}\n")

if __name__ == "__main__":
    main()
