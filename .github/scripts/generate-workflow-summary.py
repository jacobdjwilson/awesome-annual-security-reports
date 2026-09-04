"""
Operational Purpose:
    Universal Step Summary generator for GitHub Actions workflows. Formats rich telemetry,
    status indicators, issue tables, and metrics across all workflows (security pipeline,
    integrity validator, refresh conversions, README audit, discovery, ingest, learner, and lint)
    and writes them to $GITHUB_STEP_SUMMARY.

Required Environment Variables:
    GITHUB_STEP_SUMMARY: Path to GitHub Actions step summary markdown file.
    GITHUB_REPO (optional): Repository identifier (owner/repo).
    GITHUB_RUN_ID (optional): Workflow run identifier.
    GITHUB_EVENT_NAME (optional): Triggering event name.

Outputs:
    Appends formatted markdown tables and status indicators directly to $GITHUB_STEP_SUMMARY.

JSON Artifact Dependencies:
    None.
"""

import os
import sys
import json
import argparse
import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def get_env(key: str, default: str = "") -> str:
    return os.environ.get(key, default)


def parse_json_file(filepath: str) -> Any:
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8", errors="replace") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error parsing {filepath}: {e}", file=sys.stderr)
    return []


# ============================================================
# SECURITY REPORTS PIPELINE SUMMARIES
# ============================================================
def write_pipeline_discovery(f):
    event = get_env("GITHUB_EVENT_NAME")
    scan_mode = get_env("SCAN_MODE", "unknown")
    push_mode = get_env("PUSH_MODE")
    push_limit = get_env("PUSH_BATCH_LIMIT")
    open_count = get_env("OPEN_COUNT", "0")
    max_open = get_env("MAX_OPEN_PRS", "5")
    pending = get_env("PENDING_COUNT", "0")
    file_count = get_env("FILE_COUNT", "0")
    cap_reached = get_env("CAP_REACHED") == "true"

    f.write("## 🔍 File Discovery\n\n")
    f.write("| Detail | Value |\n|--------|-------|\n")
    f.write(f"| Trigger | `{event}` |\n")
    f.write(f"| Mode | `{scan_mode}` |\n")
    if event == "push":
        f.write(f"| Push Strategy | `{push_mode}` (batch limit: {push_limit}) |\n")
    f.write(f"| Open Automated PRs | {open_count} / {max_open} |\n")
    f.write(f"| PDFs skipped (open PR) | {pending} |\n")
    f.write(f"| Files Found | {file_count} |\n\n")

    if cap_reached:
        f.write("### ⏸️ PR Cap Reached\n\n")
        f.write(f"**{open_count} open automated PRs** — at or above the cap of **{max_open}**.\n\n")
        f.write("Review and merge or close open automated PRs to unblock future runs.\n")
    elif scan_mode.endswith("delete_only"):
        f.write("⊘ **Skipped** — changeset contained only PDF deletions. No processing needed.\n")
    elif os.path.exists("files_to_process.txt") and os.path.getsize("files_to_process.txt") > 0:
        f.write("**Files to Process:**\n```\n")
        with open("files_to_process.txt", "r", encoding="utf-8", errors="replace") as p:
            f.write(p.read())
        f.write("```\n")
    else:
        if event == "push" and push_mode == "missing_conversion":
            f.write("⊘ No unprocessed PDF files found — all PDFs already have a Markdown conversion.\n")
        else:
            f.write("⊘ No new PDF files detected in this changeset.\n")


def write_pipeline_virustotal(f):
    scan_mode = get_env("SCAN_MODE")
    skipped = get_env("VT_SKIPPED") == "true"

    f.write("## 🛡️ VirusTotal Scan\n\n")
    if skipped:
        f.write(f"⊘ **Skipped** — `skip_on_push` or `skip_on_schedule` is enabled for `{scan_mode}`.\n")
        return

    results = parse_json_file("scan_results.json")
    if not results:
        f.write("❌ **Scan Failed** — no results generated.\n")
        return

    f.write("| File | Verdict | Detections | Engines | Report |\n")
    f.write("|------|---------|------------|---------|--------|\n")
    
    malicious = 0
    for r in results:
        if r.get("status") == "success":
            verdict = r.get("verdict", "")
            icon = "❌ Malicious" if verdict == "Malicious" else "⚠️ Suspicious" if verdict == "Suspicious" else "✅ Clean"
            if verdict != "Clean": malicious += 1
            dets = r.get("malicious_count", 0) + r.get("suspicious_count", 0)
            engines = r.get("total_engines", 0)
            link = f"[VirusTotal]({r.get('permalink')})" if r.get("permalink") else "—"
            f.write(f"| `{r.get('file')}` | {icon} | {dets} | {engines} | {link} |\n")
        else:
            f.write(f"| `{r.get('file')}` | ⚠️ Error | — | — | {r.get('message', 'Unknown error')} |\n")
    f.write("\n")

    if malicious > 0:
        f.write(f"⚠️ **{malicious} file(s) flagged** — review before merging.\n")
    else:
        f.write("✅ **All files clean.**\n")


def write_pipeline_conversion(f):
    ok = get_env("CONV_OK", "0")
    fail = get_env("CONV_FAIL", "0")
    quota = get_env("QUOTA_EXHAUSTED") == "true"
    quota_code = get_env("QUOTA_CODE") == "true"
    delay = get_env("RETRY_DELAY", "0")
    attempt = get_env("RETRY_ATTEMPT", "1")
    f.write("## 📄 PDF to Markdown Conversion\n\n")

    if quota or quota_code:
        f.write("### ⏸️ Gemini Quota Exhausted\n\n")
        f.write("API quota limit reached during conversion.\n\n")
        f.write(f"| Detail | Value |\n|--------|-------|\n")
        f.write(f"| Attempt | {attempt} / 3 |\n")
        f.write(f"| Retry Delay | {int(delay)//60}m ({delay}s) |\n")
        f.write(f"| Status | Quota retry job scheduled |\n\n")
        return

    conversions = parse_json_file("conversions.json")
    if not conversions:
        f.write("No conversions performed.\n")
        return

    f.write(f"| Status | Count |\n|--------|-------|\n| ✅ Succeeded | {ok} |\n| ❌ Failed | {fail} |\n\n")
    f.write("| PDF | Output | Model | Characters | Status |\n")
    f.write("|-----|--------|-------|------------|--------|\n")
    for c in conversions:
        status_icon = "✅" if c.get("status") == "success" else "❌"
        chars = c.get("output_chars", "—")
        model = c.get("model", "—")
        f.write(f"| `{c.get('pdf_path')}` | `{c.get('output_path')}` | `{model}` | {chars} | {status_icon} {c.get('message', '')} |\n")
    f.write("\n")


def write_pipeline_analysis(f):
    analyzed = get_env("ANALYZED", "0")
    failed = get_env("FAILED", "0")
    quota = get_env("QUOTA_EXHAUSTED") == "true"
    delay = get_env("RETRY_DELAY", "0")
    attempt = get_env("RETRY_ATTEMPT", "1")

    f.write("## 🤖 AI Report Analysis\n\n")
    if quota:
        f.write("### ⏸️ Gemini Quota Exhausted\n\n")
        f.write("API quota limit reached during analysis.\n\n")
        f.write(f"| Detail | Value |\n|--------|-------|\n")
        f.write(f"| Attempt | {attempt} / 3 |\n")
        f.write(f"| Retry Delay | {int(delay)//60}m ({delay}s) |\n")
        f.write(f"| Status | Quota retry job scheduled |\n\n")
        return

    analysis = parse_json_file("analysis.json")
    if not analysis:
        f.write("No reports analyzed.\n")
        return

    f.write(f"| Status | Count |\n|--------|-------|\n| ✅ Analyzed | {analyzed} |\n| ❌ Failed | {failed} |\n\n")
    f.write("| Organization | Title | Year | Category | Summary Preview |\n")
    f.write("|--------------|-------|------|----------|-----------------|\n")
    for a in analysis:
        summary = a.get("summary", "")
        preview = (summary[:80] + "...") if len(summary) > 80 else summary
        f.write(f"| {a.get('organization')} | {a.get('title')} | {a.get('year')} | `{a.get('category')}` | {preview} |\n")
    f.write("\n")


def write_pipeline_readme(f):
    updated = get_env("README_UPDATED") == "true"
    pr_num = get_env("PR_NUM")
    repo = get_env("GITHUB_REPO")
    scan_mode = get_env("SCAN_MODE")
    conv_ok = get_env("CONV_OK", "0")
    conv_fail = get_env("CONV_FAIL", "0")
    vt_skipped = get_env("VT_SKIPPED") == "true"

    f.write("## 📊 README Update & PR Summary\n\n")
    f.write("| Step | Result |\n|------|--------|\n")
    f.write(f"| Mode | `{scan_mode}` |\n")
    f.write(f"| VirusTotal Scan | {'⊘ Skipped' if vt_skipped else '✅ Completed'} |\n")
    f.write(f"| PDF Conversions | {conv_ok} ok, {conv_fail} failed |\n")
    f.write(f"| README.md Updated | {'✅ Yes' if updated else '⊘ No changes'} |\n")

    if pr_num and pr_num.isdigit():
        pr_url = f"https://github.com/{repo}/pull/{pr_num}"
        f.write(f"| Pull Request | [#{pr_num}]({pr_url}) |\n\n")
        f.write(f"### 🎉 Pipeline Complete — PR [#{pr_num}]({pr_url}) is ready for review\n")
    elif updated:
        f.write("| Pull Request | ⚠️ PR creation skipped or failed |\n\n")
    else:
        f.write("| Pull Request | ⊘ None created |\n\n")


# ============================================================
# REPOSITORY INTEGRITY VALIDATOR SUMMARIES
# ============================================================
def write_validator_validate(f):
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


def write_validator_cleanup(f):
    repo = get_env("GITHUB_REPO")
    run_id = get_env("GITHUB_RUN_ID")
    event = get_env("GITHUB_EVENT_NAME")
    deleted = get_env("DELETED", "0")
    skipped = get_env("SKIPPED", "0")

    run_url = f"https://github.com/{repo}/actions/runs/{run_id}"

    f.write("## 🧹 Stale Branch Cleanup\n\n")
    f.write("| Detail | Value |\n|--------|-------|\n")
    f.write(f"| Run | [#{run_id}]({run_url}) |\n")
    f.write(f"| Trigger | `{event}` |\n")
    f.write(f"| Deleted Branches | {deleted} |\n")
    f.write(f"| Skipped Branches | {skipped} |\n\n")

    if int(deleted) > 0:
        f.write(f"✅ Deleted **{deleted}** branch(es) from closed, unmerged PRs.\n")
    else:
        f.write("ℹ️ No stale branches eligible for deletion.\n")


def write_validator_skipped(f):
    repo = get_env("GITHUB_REPO")
    run_id = get_env("GITHUB_RUN_ID")
    event = get_env("GITHUB_EVENT_NAME")
    trigger_sha = get_env("TRIGGER_SHA")
    reason = get_env("REASON", "Gate conditions not met")

    run_url = f"https://github.com/{repo}/actions/runs/{run_id}"

    f.write("## 📋 Repository Integrity Validator — Skipped\n\n")
    f.write("| Detail | Value |\n|--------|-------|\n")
    f.write(f"| Run | [#{run_id}]({run_url}) |\n")
    f.write(f"| Trigger | `{event}` |\n")
    f.write(f"| Commit | `{trigger_sha}` |\n")
    f.write(f"| Status | ⏭️ Skipped |\n\n")
    f.write(f"**Reason:** {reason}\n")


# ============================================================
# REFRESH CONVERSIONS SUMMARIES
# ============================================================
def write_refresh_summary(f, phase: str):
    repo = get_env("GITHUB_REPO", "jacobdjwilson/awesome-annual-security-reports")
    run_id = get_env("GITHUB_RUN_ID", "")
    run_url = f"https://github.com/{repo}/actions/runs/{run_id}"

    if phase == "discovery":
        event_name = get_env("GITHUB_EVENT_NAME", "unknown")
        input_limit = get_env("INPUT_LIMIT")
        input_days = get_env("INPUT_DAYS_OLD")
        pr_exists = get_env("PR_EXISTS", "false")
        skip_reason = get_env("SKIP_REASON", "")
        open_count = get_env("OPEN_COUNT") or get_env("OPEN_PRS", "0")
        has_files = get_env("HAS_FILES", "false")
        count = get_env("COUNT") or get_env("STALE_COUNT", "0")
        max_prs = get_env("MAX_PRS", "5")
        limit = input_limit or get_env("BATCH_LIMIT", "10")
        days = input_days or "30"

        f.write("## ♻️ Refresh Old Conversions — Discovery\n\n")
        f.write("| Detail | Value |\n|--------|-------|\n")
        f.write(f"| Trigger | `{event_name}` |\n")
        f.write(f"| Limit | `{limit}` |\n")
        f.write(f"| Min Age (days) | `{days}` |\n")
        f.write(f"| Open Automated PRs | {open_count} / {max_prs} |\n\n")

        if pr_exists == "true":
            if skip_reason == "pr_cap_reached":
                f.write("### ⏸️ PR Cap Reached\n\n")
                f.write(f"**{open_count} open automated PRs** — at or above the cap of **{max_prs}**.\n\n")
                f.write("Review and merge or close open automated PRs to unblock future refresh runs.\n")
            else:
                f.write("⊘ **Skipped** — An open refresh PR already exists.\n")
        elif has_files == "true":
            f.write(f"✅ Found **{count}** file(s) to refresh. Processing job will follow.\n")
        else:
            f.write("⊘ No stale conversions found requiring refresh.\n")

    elif phase == "processing":
        file_count = get_env("FILE_COUNT", "0")
        successful = get_env("SUCCESSFUL") or get_env("CONV_OK", "0")
        failed = get_env("FAILED") or get_env("CONV_FAIL", "0")
        pr_num = get_env("PR_NUM", "")
        days_old = get_env("INPUT_DAYS_OLD", "30")
        changes_detected = get_env("CHANGES_DETECTED", "false")
        analysis_count = get_env("ANALYSIS_COUNT") or get_env("ANALYZED", "0")
        analysis_error_count = get_env("ANALYSIS_ERROR_COUNT") or get_env("ANALYSIS_FAIL", "0")

        f.write("## ♻️ Refresh Old Conversions — Processing\n\n")
        f.write("| Result | Count |\n|--------|-------|\n")
        f.write(f"| Files Targeted | {file_count} |\n")
        f.write(f"| ✅ Conversions Successful | {successful} |\n")
        f.write(f"| ❌ Conversions Failed | {failed} |\n")
        f.write(f"| ✅ Analyzed | {analysis_count} |\n")
        f.write(f"| ❌ Analysis Failed | {analysis_error_count} |\n")
        f.write(f"| Min Age | {days_old} days |\n\n")

        if changes_detected == "true":
            if pr_num and pr_num.isdigit():
                pr_url = f"https://github.com/{repo}/pull/{pr_num}"
                f.write(f"✅ Pull request created: [PR #{pr_num}]({pr_url})\n\n")
        else:
            f.write("⊘ No README changes detected.\n\n")

        conversions = parse_json_file("conversions.json")
        if conversions:
            f.write("| PDF | Output | Model | Characters | Status |\n")
            f.write("|-----|--------|-------|------------|--------|\n")
            for c in conversions:
                icon = "✅" if c.get("status") == "success" else "❌"
                f.write(f"| `{c.get('pdf_path')}` | `{c.get('output_path')}` | `{c.get('model', '—')}` | {c.get('output_chars', '—')} | {icon} {c.get('message', '')} |\n")


# ============================================================
# README AUDIT SUMMARY
# ============================================================
def write_readme_audit_summary(f, findings_file: str = ".github/artifacts/readme_audit_findings.json"):
    findings_path = Path(findings_file)
    f.write("## 📊 README Audit Results\n\n")

    if not findings_path.exists():
        f.write("Audit completed without producing a findings file.\n")
        return

    data = parse_json_file(str(findings_path))
    total = 0
    category_counts = {}
    if isinstance(data, dict):
        for cat, items in data.items():
            cnt = len(items) if isinstance(items, list) else 0
            category_counts[cat] = cnt
            total += cnt

    f.write(f"Found **{total}** potential audit finding(s).\n\n")
    if category_counts:
        f.write("| Category | Count |\n|----------|-------|\n")
        for cat, count in category_counts.items():
            f.write(f"| `{cat}` | {count} |\n")
        f.write("\n")


# ============================================================
# REPORT DISCOVERY, INGEST, LEARNER, AND LINT SUMMARIES
# ============================================================
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
        f.write(f"**{open_issues} open automated issues** — at or above cap of **{max_issues}**.\n\n")
        return

    f.write("### 🔭 Search Coverage\n\n")
    f.write("| Metric | Value |\n|--------|-------|\n")
    f.write(f"| Tasks run | {tasks} |\n")
    f.write(f"| — Current year | {t_curr} |\n")
    f.write(f"| — One year stale | {t_stale} |\n")
    f.write(f"| — Older gaps | {t_old} |\n")
    f.write(f"| Suppressed | {suppressed} |\n\n")

    f.write(f"### 📋 Issues Created: {created}\n\n")
    f.write("| Find Type | Count |\n|-----------|-------|\n")
    f.write(f"| 📥 Direct PDF | {pdf_f} |\n")
    f.write(f"| 🔒 Gated landing page | {land_f} |\n\n")

    vt_total = vt_clean + vt_susp + vt_mal
    if vt_total > 0:
        f.write(f"### 🛡️ VirusTotal Pre-Scans: {vt_total}\n\n")
        f.write(f"| Clean: {vt_clean} | Suspicious: {vt_susp} | Malicious: {vt_mal} |\n\n")


def write_ingest_summary(f):
    action = get_env("ACTION", "skipped")
    issue_num = get_env("ISSUE_NUM", "unknown")
    org = get_env("ORG", "unknown")
    year = get_env("YEAR", "unknown")
    title = get_env("TITLE", "unknown")
    url = get_env("URL", "unknown")
    pdf_path = get_env("PDF_PATH", "unknown")
    pr_num = get_env("PR_NUM", "")
    repo = get_env("GITHUB_REPO")

    f.write("## 📥 Ingest Suggestion\n\n")
    f.write(f"| Field | Value |\n|---|---|\n")
    f.write(f"| Issue | [#{issue_num}](https://github.com/{repo}/issues/{issue_num}) |\n")
    f.write(f"| Action | `{action}` |\n")
    f.write(f"| Organization | {org} |\n")
    f.write(f"| Year | {year} |\n")
    f.write(f"| Title | {title} |\n")
    f.write(f"| Source URL | [Link]({url}) |\n")
    f.write(f"| PDF Path | `{pdf_path}` |\n")

    if pr_num:
        f.write(f"| Pull Request | [#{pr_num}](https://github.com/{repo}/pull/{pr_num}) |\n")


def write_learner_summary(f):
    run_url = get_env("RUN_URL")
    last_run = get_env("LAST_RUN")
    total = get_env("TOTAL_EVENTS", "0")
    tp = get_env("TRUE_POS", "0")
    fp = get_env("FALSE_POS", "0")
    dup = get_env("DUPLICATES", "0")
    mm = get_env("MISMATCHES", "0")
    thresh_delta = get_env("THRESH_DELTA", "0")
    block_count = get_env("BLOCKED_DOMAINS", "0")
    trust_count = get_env("TRUSTED_DOMAINS", "0")
    summary = get_env("GEMINI_SUMMARY", "No summary provided.")

    f.write("## 🧠 Discovery Feedback Learner\n\n")
    f.write("| Detail | Value |\n|---|---|\n")
    f.write(f"| Last run | {last_run} |\n")
    f.write(f"| Total feedback events | {total} |\n")
    f.write(f"| ✅ True positives | {tp} |\n")
    f.write(f"| 🚫 False positives | {fp} |\n")
    f.write(f"| 🔁 Duplicates | {dup} |\n")
    f.write(f"| ⚠️ Mismatches | {mm} |\n")
    f.write(f"| Score threshold delta | {thresh_delta} |\n")
    f.write(f"| Domains blocked | {block_count} |\n")
    f.write(f"| Domains trusted | {trust_count} |\n\n")
    f.write(f"### Gemini Summary\n\n{summary}\n")


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
        f.write("### ✅ Lint Passed\n\n`README.md` passed all awesome-lint checks.\n")
    else:
        f.write("### ❌ Lint Failed\n\n")
        f.write(f"**{error_count}** error(s) found in `README.md`. See annotations and the [Linting Issue] for details.\n\n")


def write_ci_gate_summary(f):
    passed = get_env("CHECKS_PASSED") == "true"
    errors = get_env("ERROR_COUNT", "0")
    scripts = get_env("SCRIPT_COUNT", "0")
    artifacts = get_env("ARTIFACT_COUNT", "0")
    prompts = get_env("PROMPT_COUNT", "0")
    ref = get_env("GITHUB_REF_NAME", "")
    event = get_env("GITHUB_EVENT_NAME", "")

    f.write("## 🛡️ CI Code & Configuration Integrity Gate\n\n")
    f.write("| Detail | Value |\n|--------|-------|\n")
    f.write(f"| Branch / Ref | `{ref}` |\n")
    f.write(f"| Trigger | `{event}` |\n")
    f.write(f"| Python Scripts | {scripts} verified |\n")
    f.write(f"| JSON Artifacts | {artifacts} verified |\n")
    f.write(f"| AI Prompts | {prompts} verified |\n")
    f.write(f"| Violations | {errors} |\n\n")

    if passed:
        f.write("### ✅ Release Gating Passed\n\nAll scripts compile, follow AGENTS.md docstring standards, and configuration schemas are strictly valid.\n")
    else:
        f.write(f"### ❌ Release Gating Failed\n\n**{errors}** violation(s) detected. Check the annotations and workflow log for remediation.\n")


# ============================================================
# MAIN ENTRYPOINT
# ============================================================
def main() -> int:
    parser = argparse.ArgumentParser(description="Universal GitHub Step Summary Generator.")
    parser.add_argument("--workflow", required=True, help="Target workflow identifier.")
    parser.add_argument("--step", default=None, help="Step identifier within the workflow.")
    parser.add_argument("--phase", default=None, help="Phase identifier (alias for --step).")
    parser.add_argument("--findings-file", default=None, help="Optional findings JSON file path.")
    args = parser.parse_args()

    step_target = args.step or args.phase or ""
    step_summary = get_env("GITHUB_STEP_SUMMARY")
    if not step_summary:
        print("GITHUB_STEP_SUMMARY environment variable not set — writing to stdout:\n")
        summary_file = sys.stdout
        should_close = False
    else:
        summary_file = open(step_summary, "a", encoding="utf-8", errors="replace")
        should_close = True

    try:
        wf = args.workflow.lower()
        if wf == "pipeline":
            if step_target == "discovery":
                write_pipeline_discovery(summary_file)
            elif step_target == "virustotal":
                write_pipeline_virustotal(summary_file)
            elif step_target == "conversion":
                write_pipeline_conversion(summary_file)
            elif step_target == "analysis":
                write_pipeline_analysis(summary_file)
            elif step_target == "readme":
                write_pipeline_readme(summary_file)
            else:
                print(f"Unknown pipeline step: {step_target}", file=sys.stderr)
        elif wf == "validator":
            if step_target == "validate":
                write_validator_validate(summary_file)
            elif step_target == "cleanup":
                write_validator_cleanup(summary_file)
            elif step_target == "skipped":
                write_validator_skipped(summary_file)
            else:
                print(f"Unknown validator step: {step_target}", file=sys.stderr)
        elif wf == "refresh":
            write_refresh_summary(summary_file, step_target or "discovery")
        elif wf in ("readme_audit", "readme-audit"):
            ff = args.findings_file or ".github/artifacts/readme_audit_findings.json"
            write_readme_audit_summary(summary_file, ff)
        elif wf == "discovery":
            write_discovery_summary(summary_file)
        elif wf == "ingest":
            write_ingest_summary(summary_file)
        elif wf == "learner":
            write_learner_summary(summary_file)
        elif wf == "lint":
            write_lint_summary(summary_file)
        elif wf in ("ci_gate", "ci-gate", "ci"):
            write_ci_gate_summary(summary_file)
        else:
            print(f"Unknown workflow: {wf}", file=sys.stderr)
            return 1

        return 0
    finally:
        if should_close:
            summary_file.close()


if __name__ == "__main__":
    sys.exit(main())
