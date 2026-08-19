import os
import sys
import json
import time
import subprocess
from pathlib import Path

def run_cmd(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    return result.stdout.split('\n') if result.returncode == 0 else []

def main():
    github_event_name = os.environ.get("GITHUB_EVENT_NAME", "")
    
    with open(".github/artifacts/workflow-config.json") as f:
        config = json.load(f)
        discovery_cfg = config.get("workflow", {}).get("discovery", {})
        conversion_cfg = config.get("workflow", {}).get("conversion", {})
        folders_cfg = config.get("workflow", {}).get("folders", {})
        
        max_size_mb = discovery_cfg.get("max_file_size_mb", 100)
        default_limit = discovery_cfg.get("default_limit", 10)
        pdf_magic = discovery_cfg.get("pdf_magic_number", "%PDF")
        push_mode = discovery_cfg.get("push_mode", "missing_conversion")
        push_batch_limit = discovery_cfg.get("push_batch_limit", 20)
        
        pdf_source = folders_cfg.get("pdf_source", "Annual Security Reports")
        md_folder = folders_cfg.get("markdown_conversions", "Markdown Conversions")
        max_age_days = conversion_cfg.get("max_age_days", 90)

    limit = int(os.environ.get("LIMIT_COUNT") or default_limit)
    year_filter = os.environ.get("YEAR_FILTER", "")
    category_filter = os.environ.get("CATEGORY_FILTER", "")
    org_filter = os.environ.get("ORG_FILTER", "")
    skip_existing = os.environ.get("SKIP_EXISTING", "true").lower() == "true"

    all_pdfs = []
    scan_mode = "unknown"

    if github_event_name == "workflow_dispatch":
        print("Mode: Manual Dispatch")
        scan_mode = "dispatch"
        
        for root, _, files in os.walk(pdf_source):
            for file in files:
                if file.endswith(".pdf"):
                    pdf_path = os.path.join(root, file)
                    if year_filter and f"({year_filter})" not in file:
                        continue
                    if category_filter and f"{category_filter}/" not in pdf_path.replace("\\", "/"):
                        continue
                    if org_filter and org_filter.lower() not in pdf_path.lower():
                        continue
                    
                    if skip_existing:
                        rel_path = Path(pdf_path).relative_to(pdf_source)
                        md_path = Path(md_folder) / rel_path.with_suffix(".md")
                        if md_path.exists():
                            continue
                    
                    all_pdfs.append(pdf_path)
        all_pdfs = all_pdfs[:limit]

    elif github_event_name == "schedule":
        print("Mode: Scheduled")
        scan_mode = "scheduled"
        
        needs_conversion = []
        now = time.time()
        for root, _, files in os.walk(pdf_source):
            for file in files:
                if file.endswith(".pdf"):
                    pdf_path = os.path.join(root, file)
                    rel_path = Path(pdf_path).relative_to(pdf_source)
                    md_path = Path(md_folder) / rel_path.with_suffix(".md")
                    
                    if not md_path.exists():
                        needs_conversion.append((0, pdf_path))
                    else:
                        mtime = md_path.stat().st_mtime
                        age_days = (now - mtime) / 86400
                        if age_days > max_age_days:
                            needs_conversion.append((mtime, pdf_path))
                            
        if needs_conversion:
            needs_conversion.sort(key=lambda x: x[0])
            all_pdfs = [needs_conversion[0][1]]

    elif github_event_name == "push":
        print(f"Mode: Push ({push_mode})")
        scan_mode = "push"
        if push_mode == "missing_conversion":
            print("  Strategy: scan for PDFs missing a Markdown conversion")
            all_missing = []
            for root, _, files in os.walk(pdf_source):
                for file in files:
                    if file.endswith(".pdf"):
                        pdf_path = os.path.join(root, file)
                        rel_path = Path(pdf_path).relative_to(pdf_source)
                        md_path = Path(md_folder) / rel_path.with_suffix(".md")
                        if not md_path.exists():
                            all_missing.append(pdf_path)
            all_missing.sort()
            all_pdfs = all_missing[:push_batch_limit] if push_batch_limit > 0 else all_missing
            print(f"  PDFs without Markdown : {len(all_missing)}")
            print(f"  Queued for this run   : {len(all_pdfs)} (batch limit: {push_batch_limit})")
        else:
            print("  Strategy: git diff HEAD~1 (legacy)")
            added = run_cmd(["git", "diff", "--name-only", "--diff-filter=A", "HEAD~1", "HEAD"])
            deleted = run_cmd(["git", "diff", "--name-only", "--diff-filter=D", "HEAD~1", "HEAD"])
            added = [f for f in added if f.startswith(pdf_source) and f.endswith(".pdf")]
            deleted = [f for f in deleted if f.startswith(pdf_source) and f.endswith(".pdf")]
            
            if not added and deleted:
                print("⊘ Only deletions detected — nothing to process")
                scan_mode = "push_delete_only"
            else:
                all_pdfs = added

    else:
        print("Mode: Pull request")
        scan_mode = "pr"
        added = run_cmd(["git", "diff", "--name-only", "--diff-filter=A", "origin/main...HEAD"])
        deleted = run_cmd(["git", "diff", "--name-only", "--diff-filter=D", "origin/main...HEAD"])
        added = [f for f in added if f.startswith(pdf_source) and f.endswith(".pdf")]
        deleted = [f for f in deleted if f.startswith(pdf_source) and f.endswith(".pdf")]
        
        if not added and deleted:
            print("⊘ Only deletions detected — nothing to process")
            scan_mode = "pr_delete_only"
        else:
            all_pdfs = added

    # Exclude pending
    if os.path.exists("pending_pdf_paths.txt"):
        with open("pending_pdf_paths.txt") as f:
            pending = set(line.strip() for line in f if line.strip())
        before = len(all_pdfs)
        all_pdfs = [p for p in all_pdfs if p not in pending]
        excluded = before - len(all_pdfs)
        if excluded > 0:
            print(f"⊘ Excluded {excluded} PDF(s) already covered by an open automated PR")

    valid_files = []
    max_size_bytes = max_size_mb * 1024 * 1024
    with open("invalid_files.txt", "w", encoding="utf-8") as invalid_f:
        for pdf_path in all_pdfs:
            if not os.path.exists(pdf_path):
                invalid_f.write(f"{pdf_path}|File Not Found\n")
                continue
            
            file_size = os.path.getsize(pdf_path)
            if file_size > max_size_bytes:
                invalid_f.write(f"{pdf_path}|Size Limit Exceeded ({file_size/1024/1024:.1f} MB > {max_size_mb} MB)\n")
                continue
                
            with open(pdf_path, "rb") as pf:
                magic = pf.read(4).decode("latin1", errors="ignore")
                if magic != pdf_magic:
                    invalid_f.write(f"{pdf_path}|Invalid PDF (Magic: '{magic}')\n")
                    continue
                    
            valid_files.append(pdf_path)
            print(f"✓ Valid: {pdf_path}")

    with open("files_to_process.txt", "w", encoding="utf-8") as f:
        for vf in valid_files:
            f.write(vf + "\n")

    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a") as f:
            if valid_files:
                f.write("has_files=true\n")
                f.write(f"file_count={len(valid_files)}\n")
                f.write(f"scan_mode={scan_mode}\n")
                print(f"✓ {len(valid_files)} files to process")
            else:
                f.write("has_files=false\n")
                f.write("file_count=0\n")
                f.write(f"scan_mode={scan_mode}\n")
                print("⊘ No files to process")

if __name__ == "__main__":
    main()
