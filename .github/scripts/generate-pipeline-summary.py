"""
Operational Purpose:
    Renders structured Markdown summary tables to $GITHUB_STEP_SUMMARY for each stage
    of the security reports processing pipeline (discovery, virustotal, conversion, analysis, readme).

Required Environment Variables:
    GITHUB_STEP_SUMMARY: Path to GitHub Actions step summary file.
    GITHUB_EVENT_NAME (optional): Event triggering the pipeline.
    SCAN_MODE (optional): Discovery scan mode.
    GITHUB_REPO (optional): Repository identifier.
    GITHUB_RUN_ID (optional): Workflow run ID.

Outputs:
    Appends rich telemetry Markdown tables directly to $GITHUB_STEP_SUMMARY.

JSON Artifact Dependencies:
    None.
"""

import os
import json
import sys
import argparse

def get_env(key, default=""):
    return os.environ.get(key, default)

def parse_json_file(filepath):
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error parsing {filepath}: {e}")
    return []

def write_discovery_summary(f):
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
        with open("files_to_process.txt", "r") as p:
            f.write(p.read())
        f.write("```\n")
    else:
        if event == "push" and push_mode == "missing_conversion":
            f.write("⊘ No unprocessed PDF files found — all PDFs already have a Markdown conversion.\n")
        else:
            f.write("⊘ No new PDF files detected in this changeset.\n")

def write_virustotal_summary(f):
    scan_mode = get_env("SCAN_MODE")
    skipped = get_env("VT_SKIPPED") == "true"
    run_url = f"https://github.com/{get_env('GITHUB_REPO')}/actions/runs/{get_env('GITHUB_RUN_ID')}"

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
            f.write(f"| `{r.get('file', '')}` | {icon} | {dets} | {engines} | [🔗 View Report]({r.get('report_url', '')}) |\n")
        else:
            malicious += 1
            f.write(f"| `{r.get('file', '')}` | ❌ Error | — | — | {r.get('error', '')} |\n")

    f.write("\n")
    if malicious > 0:
        f.write("### 🚨 Threats Detected\n\n")
        f.write("One or more files were flagged as malicious or failed to scan. Pipeline halted.\n\n")
    else:
        f.write("### ✅ All Files Clean\n\n")

    f.write(f"📎 Full scan details available in [workflow artifacts]({run_url}).\n")

def write_conversion_summary(f):
    success_count = get_env("SUCCESSFUL", "0")
    failed_count = get_env("FAILED", "0")
    run_url = f"https://github.com/{get_env('GITHUB_REPO')}/actions/runs/{get_env('GITHUB_RUN_ID')}"

    f.write("## 📄 PDF → Markdown Conversion\n\n")
    f.write("| Result | Count |\n|--------|-------|\n")
    f.write(f"| ✅ Successful | {success_count} |\n")
    f.write(f"| ❌ Failed | {failed_count} |\n\n")

    conversions = parse_json_file("conversions.json")
    if conversions:
        successes = [c for c in conversions if c.get("status") == "success"]
        failures = [c for c in conversions if c.get("status") != "success"]

        if successes:
            f.write("### ✅ Successful Conversions\n\n")
            f.write("| File | AI Model | Method | Attempts | Output |\n")
            f.write("|------|----------|--------|----------|--------|\n")
            for c in successes:
                filename = c.get("pdf_path", "").split("/")[-1]
                model = c.get("model", "—")
                method = c.get("method", "—")
                attempts = c.get("attempts", 1)
                out = c.get("output_path", "—").split("/")[-1]
                f.write(f"| `{filename}` | {model} | {method} | {attempts} | `{out}` |\n")
            f.write("\n")

        if failures:
            f.write("### ❌ Failed Conversions\n\n")
            f.write("| File | Error | Attempts |\n")
            f.write("|------|-------|----------|\n")
            for c in failures:
                filename = c.get("pdf_path", "").split("/")[-1]
                err = c.get("error", "unknown error")
                attempts = c.get("attempts", "—")
                f.write(f"| `{filename}` | {err} | {attempts} |\n")
            f.write("\n")

    f.write(f"📎 Full conversion details available in [workflow artifacts]({run_url}).\n")

def write_analysis_summary(f):
    success_count = get_env("COUNT", "0")
    error_count = get_env("ERROR_COUNT", "0")
    has_successful = get_env("HAS_SUCCESSFUL") == "true"
    analysis_success = get_env("ANALYSIS_SUCCESS") == "true"
    errors_file = get_env("ERRORS_FILE", "analysis_errors.json")
    run_url = f"https://github.com/{get_env('GITHUB_REPO')}/actions/runs/{get_env('GITHUB_RUN_ID')}"

    f.write("## 🧠 Report Analysis\n\n")

    if not has_successful:
        f.write("⊘ No successful conversions available for analysis.\n")
        return

    if analysis_success:
        if error_count == "0":
            f.write(f"✅ **{success_count} report(s) analyzed successfully.**\n\n")
        else:
            f.write(f"⚠️ **{success_count} report(s) succeeded, {error_count} failed.**\n\n")

        analysis = parse_json_file("analysis.json")
        if analysis:
            f.write("### ✅ Reports Analyzed\n\n")
            for a in analysis:
                f.write(f"#### {a.get('organization', '')} — {a.get('title', '')} ({a.get('year', '')})\n\n")
                f.write("| Field | Value |\n|-------|-------|\n")
                f.write(f"| **Category** | {a.get('category', '')} |\n")
                f.write(f"| **Type** | {a.get('type', '—')} |\n")
                url = a.get('organization_url')
                f.write(f"| **Organization URL** | {f'[{url}]({url})' if url else '—'} |\n")
                f.write(f"| **AI Model** | {a.get('model', '—')} |\n\n")
                f.write(f"**Summary:** {a.get('summary', '')}\n\n---\n\n")
            
        f.write(f"📎 Full analysis JSON available in [workflow artifacts]({run_url}).\n")

        if int(error_count) > 0 and os.path.exists(errors_file):
            f.write(f"\n### ❌ Failed Reports ({error_count})\n\n")
            f.write("| Organization | Year | Error Type | Error | Suggested Fix |\n")
            f.write("|---|---|---|---|---|\n")
            errors = parse_json_file(errors_file)
            for e in errors:
                err = e.get("error", "")[:120].replace("\n", " ").replace("|", "\\|")
                sugg = e.get("suggestion", "")[:150].replace("\n", " ").replace("|", "\\|")
                f.write(f"| **{e.get('organization', '')}** | {e.get('year', '')} | `{e.get('error_type', '')}` | {err} | {sugg} |\n")
    else:
        f.write("❌ **All reports failed analysis — no README update will be created.**\n\n")
        f.write(f"Check the [workflow logs]({run_url}) for the full error output.\n\n")

def write_readme_summary(f):
    readme_updated = get_env("README_UPDATED") == "true"
    pr_num = get_env("PR_NUM")
    scan_mode = get_env("SCAN_MODE")
    vt_skipped = get_env("VT_SKIPPED") == "true"
    conv_ok = get_env("CONV_OK", "0")
    conv_fail = get_env("CONV_FAIL", "0")
    event = get_env("GITHUB_EVENT_NAME")
    run_url = f"https://github.com/{get_env('GITHUB_REPO')}/actions/runs/{get_env('GITHUB_RUN_ID')}"

    f.write("## 📝 README Update\n\n")

    if readme_updated:
        if pr_num:
            f.write(f"✅ Pull request created: [PR #{pr_num}](https://github.com/{get_env('GITHUB_REPO')}/pull/{pr_num})\n\n")
        else:
            f.write("✅ README updated (PR creation may have been skipped or is pending).\n\n")
    else:
        f.write("⊘ No changes detected — README is already up to date.\n\n")

    f.write("### 🔧 Pipeline Metadata\n\n")
    f.write("| Detail | Value |\n|--------|-------|\n")
    f.write(f"| Trigger | `{event}` |\n")
    f.write(f"| Scan Mode | `{scan_mode}` |\n")
    f.write(f"| Conversions | ✅ {conv_ok} succeeded · ❌ {conv_fail} failed |\n")
    f.write(f"| VirusTotal | {'⊘ Skipped' if vt_skipped else '✅ Passed'} |\n")
    f.write(f"| Run | [#{get_env('GITHUB_RUN_ID')}]({run_url}) |\n\n")

    if os.path.exists("skip_log.json"):
        skip_log = parse_json_file("skip_log.json")
        if skip_log:
            f.write("### 📋 Per-Report Outcomes\n\n")
            f.write("| Organization | Year | Result | Reason |\n|-------------|------|--------|--------|\n")
            for r in skip_log:
                status = "✅ ok" if r.get("status") == "ok" else f"⊘ {r.get('status')}"
                f.write(f"| {r.get('org', '')} | {r.get('year', '')} | {status} | {r.get('reason', '')} |\n")
            f.write("\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--step", required=True)
    args = parser.parse_json_file = parser.parse_args()

    step_summary = get_env("GITHUB_STEP_SUMMARY")
    if not step_summary:
        print("GITHUB_STEP_SUMMARY not set")
        sys.exit(1)

    with open(step_summary, "a", encoding="utf-8") as f:
        if args.step == "discovery": write_discovery_summary(f)
        elif args.step == "virustotal": write_virustotal_summary(f)
        elif args.step == "conversion": write_conversion_summary(f)
        elif args.step == "analysis": write_analysis_summary(f)
        elif args.step == "readme": write_readme_summary(f)

if __name__ == "__main__":
    main()
