import os
import sys
import json
import subprocess
from datetime import datetime
from typing import Dict, List, Any

# Group categories into separate tickets to prevent issue fatigue
ISSUE_DOMAINS = {
    "Links": ["dead_link", "missing_readme"],
    "Integrity": ["invalid_pdf", "invalid_md", "oversized_file", "duplicate_pdf", "duplicate_md"],
    "Structure": ["orphaned_pdf", "orphaned_md", "stub_markdown", "year_mismatch", "naming_convention"]
}

CATEGORY_LABELS = {
    "orphaned_pdf":  "🔴 Orphaned PDFs (no Markdown conversion)",
    "orphaned_md":   "🔴 Orphaned Markdowns (no PDF)",
    "stub_markdown":       "🔴 Stub / Failed Conversions",
    "invalid_pdf":   "🔴 Invalid or Unreadable PDFs",
    "year_mismatch": "🔴 Year Inconsistencies",
    "dead_link":     "🔴 Dead External Links",
    "missing_readme":"🔴 Missing README Entries (Active Window)",
    "duplicate_pdf": "🔴 Exact PDF Duplicates (Hash Match)",
    "duplicate_md":  "🟡 Potential Content Duplicates (Markdown Similarity)",
    "invalid_md":    "🟡 Invalid or Short Markdown Files",
    "naming_convention":        "🟡 Filename Convention Violations",
    "oversized_file":     "🟡 Oversized Files",
}

def run_gh(command: List[str]) -> str:
    try:
        result = subprocess.run(
            ["gh"] + command,
            check=True,
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running gh command {' '.join(command)}:")
        print(e.stderr)
        return ""

def generate_markdown(domain: str, findings: List[Dict[str, Any]]) -> str:
    errors = [f for f in findings if f["severity"] == "error"]
    warnings = [f for f in findings if f["severity"] == "warning"]
    
    lines = [
        f"# Repository Integrity Validation: {domain}\n",
        f"*Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}*\n",
    ]
    
    if not findings:
        lines += [
            "## ✅ All Checks Passed\n",
            f"No issues found in the {domain} domain.\n",
        ]
    else:
        lines += [
            "## ⚠️ Issues Found\n",
            f"Found **{len(errors)}** error(s) and **{len(warnings)}** warning(s):\n",
        ]
        
        grouped: Dict[str, List[Dict[str, Any]]] = {}
        for f in findings:
            grouped.setdefault(f["category"], []).append(f)
            
        for cat, label in CATEGORY_LABELS.items():
            if cat not in grouped:
                continue
            lines.append(f"### {label}\n")
            for f in grouped[cat]:
                icon = "❌" if f["severity"] == "error" else "⚠️"
                lines.append(f"- {icon} **`{f['file']}`**")
                if f["message"]:
                    lines.append(f"  <br/>*{f['message']}*")
            lines.append("")
            
    # Embed fingerprints for diffing
    fps = [f["category"] + ":" + f["file"] for f in findings]
    fps.sort()
    lines.append(f"\n<!-- fingerprints: {';'.join(fps)} -->\n")
    
    return "\n".join(lines)

def manage_issues():
    if not os.path.exists("validation_findings.json"):
        print("validation_findings.json not found.")
        sys.exit(0)
        
    with open("validation_findings.json", "r") as f:
        data = json.load(f)
        
    all_findings = data.get("findings", [])
    
    for domain, categories in ISSUE_DOMAINS.items():
        domain_findings = [f for f in all_findings if f["category"] in categories]
        
        title = f"Repository Integrity Validation: {domain}"
        print(f"Processing domain: {domain} ({len(domain_findings)} findings)")
        
        # 1. Find existing issue
        search_res = run_gh(["issue", "list", "--state", "open", "--label", "automated-check", "--search", f'"{title}" in:title', "--json", "number,body"])
        existing_issue = None
        if search_res:
            issues = json.loads(search_res)
            if issues:
                existing_issue = issues[0]
                
        # 2. Compute fingerprints
        current_fps = sorted([f["category"] + ":" + f["file"] for f in domain_findings])
        current_fp_str = ";".join(current_fps)
        
        previous_fp_str = ""
        if existing_issue and "body" in existing_issue:
            import re
            m = re.search(r'<!-- fingerprints:\s*(.*?)\s*-->', existing_issue["body"])
            if m:
                previous_fp_str = m.group(1)
                
        if not domain_findings:
            if existing_issue:
                print(f"  Closing issue #{existing_issue['number']} - all issues resolved!")
                run_gh(["issue", "comment", str(existing_issue["number"]), "--body", "✅ All issues in this domain have been resolved!"])
                run_gh(["issue", "close", str(existing_issue["number"])])
            else:
                print("  No findings, no issue exists. Skipping.")
            continue
            
        if existing_issue and current_fp_str == previous_fp_str:
            print("  Fingerprints unchanged. Skipping update to prevent spam.")
            continue
            
        # 3. Create or update issue
        markdown_body = generate_markdown(domain, domain_findings)
        
        if existing_issue:
            print(f"  Closing outdated issue #{existing_issue['number']} and opening a new one...")
            run_gh(["issue", "close", str(existing_issue["number"]), "-r", "not planned"])
            
        print("  Creating new issue...")
        with open("temp_issue.md", "w", encoding="utf-8") as f:
            f.write(markdown_body)
            
        run_gh(["issue", "create", "--title", title, "--body-file", "temp_issue.md", "--label", "automated-check,bug"])
        if os.path.exists("temp_issue.md"):
            os.remove("temp_issue.md")
            
if __name__ == "__main__":
    manage_issues()
