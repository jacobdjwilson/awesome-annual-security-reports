import os
import json
import sys

def main():
    github_step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if not github_step_summary:
        print("Error: GITHUB_STEP_SUMMARY not set.")
        sys.exit(1)

    repo = os.environ.get("GITHUB_REPO", "")
    run_id = os.environ.get("GITHUB_RUN_ID", "")
    run_url = f"https://github.com/{repo}/actions/runs/{run_id}"

    # Load config for defaults
    config_path = ".github/artifacts/workflow-config.json"
    config = {}
    if os.path.exists(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                config = json.load(f).get("workflow", {})
        except Exception:
            pass

    default_days_old = str(config.get("conversion", {}).get("max_age_days"))
    default_errors_file = config.get("analysis", {}).get("errors_output_file")

    file_count = os.environ.get("FILE_COUNT") or "0"
    successful = os.environ.get("SUCCESSFUL") or "0"
    failed = os.environ.get("FAILED") or "0"
    pr_num = os.environ.get("PR_NUM") or ""
    days_old = os.environ.get("INPUT_DAYS_OLD") or default_days_old
    changes_detected = os.environ.get("CHANGES_DETECTED") or "false"
    analysis_count = os.environ.get("ANALYSIS_COUNT") or "0"
    analysis_error_count = os.environ.get("ANALYSIS_ERROR_COUNT") or "0"
    errors_file = os.environ.get("ERRORS_FILE") or default_errors_file

    with open(github_step_summary, "a", encoding="utf-8") as summary:
        summary.write("## ♻️ Refresh Old Conversions — Processing\n\n")
        summary.write("| Result | Count |\n")
        summary.write("|--------|-------|\n")
        summary.write(f"| Files Targeted | {file_count} |\n")
        summary.write(f"| ✅ Conversions Successful | {successful} |\n")
        summary.write(f"| ❌ Conversions Failed | {failed} |\n")
        summary.write(f"| Min Age | {days_old} days |\n")
        summary.write("| Conversion Method | markitdown + AI polish (force-reconvert) |\n\n")

        if changes_detected == "true":
            if pr_num:
                pr_url = f"https://github.com/{repo}/pull/{pr_num}"
                summary.write(f"✅ Pull request created: [PR #{pr_num}]({pr_url})\n\n")
        else:
            summary.write("⊘ No README changes detected.\n\n")

        if os.path.exists("conversions.json"):
            try:
                with open("conversions.json", "r", encoding="utf-8") as f:
                    conversions = json.load(f)
                if conversions:
                    summary.write("### 📄 Conversion Detail\n\n")
                    summary.write("| File | Method | Model | Chars | Status |\n")
                    summary.write("|------|--------|-------|-------|--------|\n")
                    for c in conversions:
                        filename = c.get("pdf_path", "").split("/")[-1]
                        method = c.get("method", "—")
                        model = c.get("model", "—")
                        chars = str(c.get("output_chars")) if c.get("output_chars") else "—"
                        status = "✅" if c.get("status") == "success" else f"❌ {c.get('message', '')}"
                        summary.write(f"| `{filename}` | {method} | {model} | {chars} | {status} |\n")
                    summary.write("\n")
            except Exception as e:
                print(f"Error parsing conversions.json: {e}")

        if os.path.exists("readme-update-results.json"):
            try:
                with open("readme-update-results.json", "r", encoding="utf-8") as f:
                    results = json.load(f)
                if results:
                    summary.write("### 📋 README Update Disposition\n\n")
                    summary.write("| Organization | Year | Action | Reason |\n")
                    summary.write("|--------------|------|--------|--------|\n")
                    for r in results:
                        org = r.get("organization", "")
                        year = r.get("year", "")
                        action = "✅ " + r.get("action", "") if r.get("status") == "changed" else "⊘ skipped"
                        reason = r.get("reason", "")
                        summary.write(f"| {org} | {year} | {action} | {reason} |\n")
                    summary.write("\n")
            except Exception as e:
                print(f"Error parsing readme-update-results.json: {e}")

        summary.write("### 🧠 Analysis Results\n\n")
        if int(analysis_count) > 0:
            summary.write("| ✅ Reports Analyzed | ❌ Analysis Failed |\n")
            summary.write("|---|---|\n")
            summary.write(f"| {analysis_count} | {analysis_error_count} |\n\n")
        elif os.path.exists(errors_file) and int(analysis_error_count) > 0:
            summary.write("❌ **All report(s) failed AI analysis.**\n\n")
            summary.write("| Organization | Year | Error Type | Suggested Fix |\n")
            summary.write("|---|---|---|---|\n")
            try:
                with open(errors_file, "r", encoding="utf-8") as f:
                    errors = json.load(f)
                for e in errors:
                    org = e.get("organization", "")
                    year = e.get("year", "")
                    err_type = e.get("error_type", "")
                    sugg = e.get("suggestion", "")[:150].replace("\n", " ").replace("|", "\\|")
                    summary.write(f"| **{org}** | {year} | `{err_type}` | {sugg} |\n")
            except Exception as e:
                print(f"Error parsing {errors_file}: {e}")
        else:
            summary.write("⊘ No analysis was attempted or data is unavailable.\n\n")

        summary.write(f"📎 Full details available in [workflow artifacts]({run_url}).\n")

if __name__ == "__main__":
    main()
