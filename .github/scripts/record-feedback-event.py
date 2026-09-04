"""
Operational Purpose:
    Appends maintainer issue triage outcomes (accepted, false-positive, duplicate, mismatch)
    to the discovery feedback event log in discovery-feedback.json for machine learning.

Required Environment Variables:
    ISSUE: Issue number being triaged.
    ISSUE_TITLE: Issue title string.
    OUTCOME: Triage verdict (e.g. accepted, false-positive, duplicate).
    REASON: Optional rationale notes.
    AUTHOR: Username of triage reviewer.

Outputs:
    .github/artifacts/discovery-feedback.json: Updated event log.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.issue_triage.feedback_artifact_path)
    .github/artifacts/discovery-feedback.json
"""

import json
import os
import datetime
import re
import subprocess
import sys

def main():
    issue_number = os.environ.get("ISSUE", "0")
    issue_title = os.environ.get("ISSUE_TITLE", "")
    outcome = os.environ.get("OUTCOME", "")
    reason = os.environ.get("REASON", "")
    author = os.environ.get("AUTHOR", "")

    # Load config to get the feedback_path
    config_path = ".github/artifacts/workflow-config.json"
    try:
        with open(config_path, "r") as f:
            config = json.load(f)
    except Exception as e:
        print(f"Error loading config: {e}")
        sys.exit(1)

    feedback_path = config.get("workflow", {}).get("issue_triage", {}).get("feedback_artifact_path", ".github/artifacts/discovery-feedback.json")

    # Load existing feedback file
    try:
        with open(feedback_path, "r") as f:
            data = json.load(f)
    except Exception as e:
        print(f"ERROR loading feedback file at {feedback_path}: {e}")
        sys.exit(1)

    if "feedback_events" not in data:
        data["feedback_events"] = []

    # Extract org and URL from the issue body if possible
    org = ""
    url = ""
    try:
        body_output = subprocess.check_output(
            ["gh", "issue", "view", issue_number, "--json", "body", "-q", ".body"],
            text=True, encoding='utf-8'
        )
        # e.g., | **Organization** | Acme Corp |
        org_match = re.search(r"\|\s*\*\*Organization\*\*\s*\|\s*([^|]+?)\s*\|", body_output)
        if org_match: org = org_match.group(1).strip()
        
        url_match = re.search(r"\|\s*\*\*URL\*\*\s*\|\s*([^|]+?)\s*\|", body_output)
        if url_match: url = url_match.group(1).strip()
    except Exception as e:
        print(f"Could not extract org/url: {e}")

    event = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "issue_number": int(issue_number),
        "issue_title": issue_title,
        "org": org,
        "url": url,
        "outcome": outcome,
        "reason": reason,
        "author": author
    }

    data["feedback_events"].append(event)
    data["total_feedback_events"] = data.get("total_feedback_events", 0) + 1

    # Recompute outcome_counts
    counts = {"true_positive": 0, "false_positive": 0, "duplicate": 0, "mismatch": 0}
    for ev in data["feedback_events"]:
        o = ev.get("outcome")
        if o in counts: counts[o] += 1
    data["outcome_counts"] = counts

    try:
        with open(feedback_path, "w") as f:
            json.dump(data, f, indent=2)
            f.write("\n")
        print(f"✓ Feedback event recorded in {feedback_path}")
    except Exception as e:
        print(f"ERROR saving feedback file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
