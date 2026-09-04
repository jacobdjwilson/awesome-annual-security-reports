"""
Operational Purpose:
    Renders discovery execution statistics, VirusTotal verdicts, and learning feedback telemetry
    to $GITHUB_STEP_SUMMARY for the report discovery workflow.

Required Environment Variables:
    GITHUB_STEP_SUMMARY: Path to GitHub Actions step summary file.
    GITHUB_REPO (optional): Repository identifier.
    GITHUB_RUN_ID (optional): Workflow run identifier.
    GITHUB_EVENT_NAME (optional): Triggering event name.

Outputs:
    Appends discovery and feedback summary tables to $GITHUB_STEP_SUMMARY.

JSON Artifact Dependencies:
    None.
"""

import os
import sys
import json
import datetime

def get_env(key, default=""):
    return os.environ.get(key, default)

def write_discovery_summary(f):
    repo = get_env("GITHUB_REPO")
    run_id = get_env("GITHUB_RUN_ID")
    event = get_env("GITHUB_EVENT_NAME")
    override_date = get_env("OVERRIDE_DATE")
    
    cap_reached = get_env("CAP_REACHED") == "true"
    open_issues = get_env("OPEN_ISSUES", "0")
    max_issues = get_env("MAX_ISSUES", "20")
    
    created = int(get_env("CREATED", "0"))
    tasks = get_env("TASKS", "0")
    suppressed = int(get_env("SUPPRESSED", "0"))
    skipped = get_env("SKIPPED", "0")
    
    pdf_f = get_env("PDF_F", "0")
    land_f = get_env("LAND_F", "0")
    
    t_curr = get_env("T_CURR", "0")
    t_stale = get_env("T_STALE", "0")
    t_old = get_env("T_OLD", "0")
    
    vt_clean = int(get_env("VT_CLEAN", "0"))
    vt_susp = int(get_env("VT_SUSP", "0"))
    vt_mal = int(get_env("VT_MAL", "0"))
    
    run_url = f"https://github.com/{repo}/actions/runs/{run_id}"
    date_used = override_date if override_date else f"{datetime.datetime.now().strftime('%Y-%m-%d')} (today)"

    f.write("## 🔍 Security Report Discovery\n\n")
    f.write("| Detail | Value |\n|--------|-------|\n")
    f.write(f"| Trigger | `{event}` |\n")
    f.write(f"| Date    | {date_used} |\n")
    f.write(f"| Open Automated Issues | {open_issues} / {max_issues} |\n\n")

    if cap_reached:
        f.write("### ⏸️ Issue Cap Reached\n\n")
        f.write(f"**{open_issues} open automated issues** — at or above the cap of **{max_issues}**.\n\n")
        f.write("Triage and close open discovery issues to unblock future runs.\n\n")
        f.write(f"📎 Full log: [workflow artifacts]({run_url})\n")
        return

    f.write("### 🔭 Search Coverage\n\n")
    f.write("| Metric | Value |\n|--------|-------|\n")
    f.write(f"| Tasks run (2 API calls each)   | {tasks} |\n")
    f.write(f"| — Current year (gap = 1yr)     | {t_curr} |\n")
    f.write(f"| — One year stale (gap = 2yr)   | {t_stale} |\n")
    f.write(f"| — Older gaps (gap ≥ 3yr)       | {t_old} |\n")
    f.write(f"| Suppressed (below threshold)   | {suppressed} |\n\n")

    f.write(f"### 📋 Issues Created: {created}\n\n")
    f.write("| Find Type | Count |\n|-----------|-------|\n")
    f.write(f"| 📥 Direct PDF        | {pdf_f} |\n")
    f.write(f"| 🔒 Gated landing page | {land_f} |\n\n")

    url_seen = int(get_env("URL_SEEN", "0"))
    gem_rej = int(get_env("GEM_REJ", "0"))
    sim_dup = int(get_env("SIM_DUP", "0"))
    if (url_seen + gem_rej + sim_dup) > 0:
        f.write("### 🔬 Pre-issue Filters\n\n")
        f.write("| Filter | Count |\n|--------|-------|\n")
        f.write(f"| 🔁 URL already seen | {url_seen} |\n")
        f.write(f"| 🤖 Gemini rejected  | {gem_rej} |\n")
        f.write(f"| 📄 Similarity dup   | {sim_dup} |\n\n")

    vt_total = vt_clean + vt_susp + vt_mal
    if vt_total > 0:
        f.write(f"### 🛡️ VirusTotal Pre-Scans: {vt_total}\n\n")
        f.write("| Verdict | Count |\n|---------|-------|\n")
        f.write(f"| ✅ Clean      | {vt_clean} |\n")
        f.write(f"| ⚠️ Suspicious | {vt_susp} |\n")
        f.write(f"| ❌ Malicious  | {vt_mal} |\n\n")
        if vt_mal > 0:
            f.write(f"⚠️ **{vt_mal} PDF(s) flagged as Malicious** — issues are labeled `malicious-pdf` for triage.\n\n")
        if vt_susp > 0:
            f.write(f"⚠️ **{vt_susp} PDF(s) flagged as Suspicious** — issues are labeled `suspicious-pdf` for triage.\n\n")

    # Read from log
    log_file = "discovery_output.log"
    issues_created = []
    issues_suppressed = []
    try:
        with open(log_file, "r") as log:
            for line in log:
                if "✓ Created issue" in line:
                    issues_created.append("- " + line.split("Created issue ")[1].strip())
                elif "⊘ Best score" in line:
                    issues_suppressed.append("- " + line.strip().replace("⊘ Best score", "").strip())
    except Exception:
        pass

    if created > 0:
        f.write("#### New issues\n\n")
        for ic in issues_created:
            f.write(f"{ic}\n")
        f.write("\n")
    else:
        f.write("⊘ No new issues created this run.\n\n")

    if suppressed > 0:
        f.write("<details><summary>🔻 Suppressed candidates</summary>\n\n")
        for s in issues_suppressed:
            f.write(f"{s}\n")
        f.write("\n</details>\n\n")

    f.write(f"📎 Full log: [workflow artifacts]({run_url})\n")

def write_ingest_summary(f):
    repo = get_env("GITHUB_REPO")
    run_id = get_env("GITHUB_RUN_ID")
    issue_num = get_env("ISSUE_NUMBER")
    
    org = get_env("ORG_NAME")
    title = get_env("REPORT_TITLE")
    year = get_env("REPORT_YEAR")
    cat = get_env("REPORT_CATEGORY")
    file_name = get_env("FILE_NAME")
    pr_num = get_env("PR_NUM")
    valid = get_env("VALID", "true")
    download_conclusion = get_env("DOWNLOAD_CONCLUSION")
    
    run_url = f"https://github.com/{repo}/actions/runs/{run_id}"
    issue_url = f"https://github.com/{repo}/issues/{issue_num}"

    f.write("## 📥 Report Ingestion\n\n")
    f.write("| Field | Value |\n|-------|-------|\n")
    f.write(f"| Issue | [#{issue_num}]({issue_url}) |\n")
    f.write(f"| Organization | {org} |\n")
    f.write(f"| Title | {title} |\n")
    f.write(f"| Year | {year} |\n")
    f.write(f"| Category | {cat} |\n")
    f.write(f"| File | `{file_name}` |\n\n")

    if pr_num:
        pr_url = f"https://github.com/{repo}/pull/{pr_num}"
        f.write(f"✅ Pull request created: [PR #{pr_num}]({pr_url})\n")
    elif valid == "false":
        f.write("❌ Validation failed — required fields missing or invalid.\n")
    elif download_conclusion == "failure":
        f.write("❌ Download failed — PDF could not be retrieved from URL.\n")
    else:
        f.write(f"❌ Pull request creation failed. Check [workflow logs]({run_url}).\n")

def write_learner_summary(f):
    feedback_file = ".github/artifacts/discovery-feedback.json"
    if not os.path.exists(feedback_file):
        f.write("⚠️ Feedback file not found.\n")
        return

    try:
        with open(feedback_file, "r") as fb:
            data = json.load(fb)
    except Exception:
        f.write("⚠️ Could not parse feedback JSON.\n")
        return

    total = data.get("total_feedback_events", 0)
    outcomes = data.get("outcome_counts", {})
    tp = outcomes.get("true_positive", 0)
    fp = outcomes.get("false_positive", 0)
    dup = outcomes.get("duplicate", 0)
    mm = outcomes.get("mismatch", 0)
    
    learned = data.get("learned", {})
    summary = learned.get("summary", "(not yet run)")
    last_run = data.get("last_learner_run", "never")
    thresh_delta = learned.get("score_threshold_delta", 0)
    
    block_count = len(learned.get("domain_blocklist", {}).get("domains", []))
    trust_count = len(learned.get("domain_trustlist", {}).get("domains", []))

    f.write("## 🧠 Discovery Feedback Learner\n\n")
    f.write("| Metric | Value |\n|--------|-------|\n")
    f.write(f"| Last run | {last_run} |\n")
    f.write(f"| Total feedback events | {total} |\n")
    f.write(f"| ✅ True positives | {tp} |\n")
    f.write(f"| 🚫 False positives | {fp} |\n")
    f.write(f"| 🔁 Duplicates | {dup} |\n")
    f.write(f"| ⚠️ Mismatches | {mm} |\n")
    f.write(f"| Score threshold delta | {thresh_delta} |\n")
    f.write(f"| Domains blocked | {block_count} |\n")
    f.write(f"| Domains trusted | {trust_count} |\n\n")
    f.write("### Gemini Summary\n\n")
    f.write(f"{summary}\n")

def write_lint_summary(f):
    run_url = get_env("RUN_URL")
    status = get_env("STATUS")
    error_count = get_env("ERROR_COUNT", "0")
    ref_name = get_env("REF_NAME")
    event_name = get_env("EVENT_NAME")

    f.write("## 🧹 Awesome Lint\n\n")
    f.write("| Detail | Value |\n|--------|-------|\n")
    f.write(f"| Branch | `{ref_name}` |\n")
    f.write(f"| Trigger | `{event_name}` |\n")
    f.write(f"| Errors | {error_count} |\n\n")

    if status == "succeeded":
        f.write("### ✅ Lint Passed\n\n")
        f.write("`README.md` passed all awesome-lint checks.\n")
    else:
        f.write("### ❌ Lint Failed\n\n")
        f.write(f"**{error_count}** error(s) found in `README.md`. Review the annotations in the [workflow run]({run_url}) for details.\n\n")
        f.write("<details><summary>🔍 Lint Output</summary>\n\n```\n")
        try:
            with open("lint_output.txt", "r") as lf:
                f.write(lf.read())
        except Exception:
            pass
        f.write("```\n</details>\n\n")
        f.write("If these are expected issues, add appropriate `lint ignore` directives to `README.md`.\n")

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--workflow", required=True)
    args = parser.parse_args()

    step_summary = get_env("GITHUB_STEP_SUMMARY")
    if not step_summary:
        print("GITHUB_STEP_SUMMARY not set")
        sys.exit(1)

    with open(step_summary, "a", encoding="utf-8") as f:
        if args.workflow == "discovery":
            write_discovery_summary(f)
        elif args.workflow == "ingest":
            write_ingest_summary(f)
        elif args.workflow == "learner":
            write_learner_summary(f)
        elif args.workflow == "lint":
            write_lint_summary(f)

if __name__ == "__main__":
    main()
