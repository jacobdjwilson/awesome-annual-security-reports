"""
Operational Purpose:
    Evaluates concurrency gating between pipelines to ensure dependent validation workflows
    only execute when prerequisite workflows have completed successfully on shared assets.

Required Environment Variables:
    GITHUB_EVENT_NAME: Event that triggered the run (e.g. workflow_dispatch, workflow_run).
    GITHUB_REPOSITORY: Repository identifier (owner/repo).
    GITHUB_SHA (optional): Commit SHA for manual/scheduled runs.
    WORKFLOW_RUN_HEAD_SHA (optional): Commit SHA of triggering workflow run.
    WORKFLOW_RUN_CONCLUSION (optional): Conclusion of triggering workflow (success, failure).
    WORKFLOW_RUN_NAME (optional): Name of triggering workflow.
    GITHUB_OUTPUT (optional): Path to export proceed, skip_reason, and trigger_sha.

Outputs:
    proceed (bool): 'true' if gating passes and downstream processing should run, 'false' otherwise.
    skip_reason (str): Diagnostic reason when execution is deferred or skipped.
    trigger_sha (str): Target commit SHA.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.gating.monitored_workflows, workflow.gating.monitored_statuses)
"""

import os
import sys
import subprocess
import json
import urllib.parse

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return ""

def write_output(key, value):
    output_file = os.environ.get("GITHUB_OUTPUT")
    if output_file:
        with open(output_file, "a") as f:
            f.write(f"{key}={value}\n")

def main():
    event = os.environ.get("GITHUB_EVENT_NAME", "")
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    sha = os.environ.get("GITHUB_SHA", "")

    if event in ["workflow_dispatch", "schedule"]:
        write_output("proceed", "true")
        write_output("skip_reason", "")
        write_output("trigger_sha", sha)
        print("✓ Manual/scheduled — proceeding")
        sys.exit(0)

    trigger_sha = os.environ.get("WORKFLOW_RUN_HEAD_SHA", "")
    conclusion = os.environ.get("WORKFLOW_RUN_CONCLUSION", "")
    run_name = os.environ.get("WORKFLOW_RUN_NAME", "")

    print(f"Triggered by: {run_name}")
    print(f"Conclusion:   {conclusion}")
    print(f"Head SHA:     {trigger_sha}\n")

    if conclusion != "success":
        write_output("proceed", "false")
        write_output("skip_reason", "pipeline_did_not_succeed")
        write_output("trigger_sha", trigger_sha)
        print("⊘ Triggering workflow did not succeed — skipping")
        sys.exit(0)

    from pathlib import Path
    config_path = Path(".github/artifacts/workflow-config.json")
    if not config_path.exists():
        raise FileNotFoundError(f"Missing required artifact: {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f).get("workflow", {})

    gating_cfg = config.get("gating", {})
    monitored_workflows = gating_cfg.get("monitored_workflows")
    if not monitored_workflows:
        raise ValueError("Missing 'gating.monitored_workflows' in workflow-config.json")

    monitored_statuses = gating_cfg.get("monitored_statuses", ["in_progress", "queued", "waiting"])
    busy = False

    for wf_name in monitored_workflows:
        print(f"Checking: {wf_name}")
        encoded = urllib.parse.quote(wf_name)
        for status in monitored_statuses:
            count_str = run_cmd(f"gh api 'repos/{repo}/actions/workflows/{encoded}/runs?head_sha={trigger_sha}&status={status}' --jq '.total_count'")
            count = int(count_str) if count_str.isdigit() else 0
            print(f"  {status}: {count}")
            if count > 0:
                busy = True
                break
        if busy:
            break
    print("")

    if busy:
        write_output("proceed", "false")
        write_output("skip_reason", "pipelines_still_running")
        write_output("trigger_sha", trigger_sha)
        print("⊘ A monitored pipeline is still running — deferring validation")
        print("  The validator will run again when the other pipeline finishes.")
        sys.exit(0)

    changed_str = run_cmd(f"gh api 'repos/{repo}/commits/{trigger_sha}' --jq '[.files[].filename | select(startswith(\"Annual Security Reports/\") or startswith(\"Markdown Conversions/\"))] | length'")
    changed = int(changed_str) if changed_str.lstrip("-").isdigit() else -1
    print(f"Files changed in monitored directories: {changed}")

    if changed == 0:
        write_output("proceed", "false")
        write_output("skip_reason", "no_relevant_changes")
        write_output("trigger_sha", trigger_sha)
        print("⊘ No changes in monitored directories — skipping")
        sys.exit(0)

    write_output("proceed", "true")
    write_output("skip_reason", "")
    write_output("trigger_sha", trigger_sha)
    print("✓ Gate passed — proceeding with validation")

if __name__ == "__main__":
    main()
