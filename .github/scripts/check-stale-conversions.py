import os
import json
import time
import re
from pathlib import Path
from datetime import datetime
import sys

def main():
    limit = int(os.environ.get("LIMIT", "10"))
    days_old = int(os.environ.get("DAYS_OLD", "90"))
    pdf_source = os.environ.get("PDF_SOURCE", "Annual Security Reports")
    md_folder = os.environ.get("MD_FOLDER", "Markdown Conversions")

    models_json_path = ".github/artifacts/ai-models.json"
    
    primary_model = "gemini-3.5-flash-lite"
    if os.path.exists(models_json_path):
        with open(models_json_path) as f:
            primary_model = json.load(f).get("models", {}).get("primary", primary_model)

    threshold_timestamp = time.time() - (days_old * 86400)
    candidates = []

    for root, _, files in os.walk(pdf_source):
        for file in files:
            if not file.endswith(".pdf"):
                continue
            
            pdf_path = Path(root) / file
            rel_path = pdf_path.relative_to(pdf_source)
            md_path = Path(md_folder) / rel_path.with_suffix(".md")
            
            if not md_path.exists():
                candidates.append((0, 0, str(pdf_path)))
                continue
                
            try:
                content = md_path.read_text(encoding="utf-8")
                match = re.search(r"<!-- CONVERSION_METADATA: (\{.*?\}) -->", content)
                if not match:
                    candidates.append((1, 0, str(pdf_path)))
                    continue
                
                meta = json.loads(match.group(1))
                if meta.get("model") != primary_model:
                    candidates.append((1, 1, str(pdf_path)))
                    continue
                    
                date_str = meta.get("date")
                if date_str:
                    dt = datetime.strptime(date_str, "%Y-%m-%d")
                    ts = dt.timestamp()
                    if ts < threshold_timestamp:
                        candidates.append((2, ts, str(pdf_path)))
            except Exception:
                candidates.append((1, 0, str(pdf_path)))

    candidates.sort(key=lambda x: (x[0], x[1]))
    
    file_count = min(len(candidates), limit)
    with open("files_to_process.txt", "w") as f:
        for c in candidates[:limit]:
            f.write(c[2] + "\n")

    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a") as f:
            if file_count > 0:
                f.write("has_files=true\n")
                f.write(f"file_count={file_count}\n")
                print(f"✓ Found {file_count} files to refresh")
            else:
                f.write("has_files=false\n")
                f.write("file_count=0\n")
                print("⊘ No stale files found")

if __name__ == "__main__":
    main()
