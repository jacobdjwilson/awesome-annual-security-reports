import os
import sys

def get_env(key, default=""):
    return os.environ.get(key, default)

def write_validate_summary(f):
    run_id = get_env("GITHUB_RUN_ID")
    repo = get_env("GITHUB_REPO")
    event = get_env("GITHUB_EVENT_NAME")
    trigger_sha = get_env("TRIGGER_SHA")
    has_findings = get_env("HAS_FINDINGS") == "true"
    errs = get_env("ERROR_COUNT", "0")
    warns = get_env("WARNING_COUNT", "0")
    new_issue = get_env("NEW_ISSUE")
    closed_issue = get_env("CLOSED_ISSUE")
    unchanged_issue = get_env("UNCHANGED_ISSUE")

    run_url = f"https://github.com/{repo}/actions/runs/{run_id}"

    f.write("## 📋 Repository Integrity Validator\n\n")
    f.write("| Detail | Value |\n|--------|-------|\n")
    f.write(f"| Run | [#{run_id}]({run_url}) |\n")
    f.write(f"| Trigger | `{event}` |\n")
    f.write(f"| Commit | `{trigger_sha}` |\n")
    f.write(f"| Errors | {errs} |\n")
    f.write(f"| Warnings | {warns} |\n\n")

    if not has_findings:
        f.write("### ✅ Validation Passed\n\n")
        f.write("All PDF ↔ Markdown pairs are consistent, correctly named, and structurally valid.\n")
        if closed_issue:
            f.write(f"\n✅ Closed previously open issue [#{closed_issue}](https://github.com/{repo}/issues/{closed_issue}) — all issues resolved.\n")
    else:
        f.write("### ⚠️ Issues Detected\n\n")
        if new_issue:
            f.write(f"Opened issue [#{new_issue}](https://github.com/{repo}/issues/{new_issue}) with full details.\n")
        elif unchanged_issue:
            f.write(f"Findings unchanged — no update to open issue [#{unchanged_issue}](https://github.com/{repo}/issues/{unchanged_issue}).\n")
        
        f.write("\n<details><summary>📄 Validation Report</summary>\n\n```\n")
        try:
            with open("validation_report.md", "r") as report:
                f.write(report.read())
        except Exception:
            f.write("(report not available)\n")
        f.write("```\n</details>\n")

    f.write(f"\n📎 Full report available in [workflow artifacts]({run_url}).\n")

def write_cleanup_summary(f):
    run_id = get_env("GITHUB_RUN_ID")
    repo = get_env("GITHUB_REPO")
    event = get_env("GITHUB_EVENT_NAME")
    deleted = get_env("DELETED", "0")
    skipped = get_env("SKIPPED", "0")
    run_url = f"https://github.com/{repo}/actions/runs/{run_id}"

    f.write("## 🧹 Stale Branch Cleanup\n\n")
    f.write("| Detail | Value |\n|--------|-------|\n")
    f.write(f"| Trigger | `{event}` |\n")
    f.write(f"| Branches deleted | {deleted} |\n")
    f.write(f"| Branches skipped | {skipped} |\n\n")

    if int(deleted) > 0:
        f.write("### 🗑️ Deleted Branches\n\n")
        try:
            with open("/tmp/deleted_branches.txt", "r") as db:
                for line in db:
                    if line.strip():
                        f.write(f"- `{line.strip()}`\n")
        except Exception:
            pass
        f.write("\n")
    else:
        f.write("✅ No stale branches found — repo is already tidy.\n\n")

    if int(skipped) > 0:
        f.write(f"<details><summary>⊘ Skipped branches ({skipped})</summary>\n\n")
        try:
            with open("/tmp/skipped_branches.txt", "r") as sb:
                for line in sb:
                    if line.strip():
                        f.write(f"- `{line.strip()}`\n")
        except Exception:
            pass
        f.write("\n</details>\n\n")

    f.write(f"📎 Full log: [workflow run]({run_url})\n")

def write_skipped_summary(f):
    run_id = get_env("GITHUB_RUN_ID")
    repo = get_env("GITHUB_REPO")
    event = get_env("GITHUB_EVENT_NAME")
    trigger_sha = get_env("TRIGGER_SHA")
    reason = get_env("REASON")
    run_url = f"https://github.com/{repo}/actions/runs/{run_id}"

    f.write("## 📋 Repository Integrity Validator\n\n")
    f.write("| Detail | Value |\n|--------|-------|\n")
    f.write(f"| Run | [#{run_id}]({run_url}) |\n")
    f.write(f"| Trigger | `{event}` |\n")
    f.write(f"| SHA | `{trigger_sha}` |\n\n")
    f.write("### ⊘ Validation Skipped\n\n")

    if reason == "pipeline_did_not_succeed":
        f.write("The triggering pipeline did not complete successfully — validation skipped to avoid acting on a broken or partial state.\n")
    elif reason == "pipelines_still_running":
        f.write("One or more monitored pipelines are still running on this commit.\n")
        f.write("Validation will run automatically when they finish.\n")
    elif reason == "no_relevant_changes":
        f.write("No files changed in `Annual Security Reports/` or `Markdown Conversions/` — nothing to validate.\n")
    else:
        f.write("Validation was not required for this run.\n")

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--step", required=True)
    args = parser.parse_args()

    step_summary = get_env("GITHUB_STEP_SUMMARY")
    if not step_summary:
        print("GITHUB_STEP_SUMMARY not set")
        sys.exit(1)

    with open(step_summary, "a", encoding="utf-8") as f:
        if args.step == "validate": write_validate_summary(f)
        elif args.step == "cleanup": write_cleanup_summary(f)
        elif args.step == "skipped": write_skipped_summary(f)

if __name__ == "__main__":
    main()
