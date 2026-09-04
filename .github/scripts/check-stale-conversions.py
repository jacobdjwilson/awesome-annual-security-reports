import os
import json
import time
import re
from pathlib import Path
from datetime import datetime
import sys

def main():
    models_json_path = Path(".github/artifacts/ai-models.json")
    wf_config_path = Path(".github/artifacts/workflow-config.json")

    if not models_json_path.exists():
        raise FileNotFoundError(f"Missing required artifact: {models_json_path}")
    if not wf_config_path.exists():
        raise FileNotFoundError(f"Missing required artifact: {wf_config_path}")

    with open(models_json_path, "r", encoding="utf-8") as f:
        models_data = json.load(f)
    
    conversion_task_models = models_data.get("task_models", {}).get("conversion", {})
    primary_model = (
        conversion_task_models.get("primary")
        or models_data.get("models", {}).get("primary")
    )
    if not primary_model:
        raise ValueError("Missing 'task_models.conversion.primary' or 'models.primary' in ai-models.json")

    with open(wf_config_path, "r", encoding="utf-8") as f:
        wf_data = json.load(f).get("workflow", {})

    conversion_cfg = wf_data.get("conversion", {})
    folders_cfg = wf_data.get("folders", {})

    pdf_source = os.environ.get("PDF_SOURCE") or folders_cfg.get("pdf_source")
    md_folder = os.environ.get("MD_FOLDER") or folders_cfg.get("markdown_conversions")
    if not pdf_source or not md_folder:
        raise ValueError("Missing 'folders.pdf_source' or 'folders.markdown_conversions' in workflow-config.json")

    env_limit = os.environ.get("LIMIT")
    limit = int(env_limit) if env_limit else conversion_cfg.get("refresh_batch_limit")
    if limit is None:
        raise ValueError("Missing 'conversion.refresh_batch_limit' in workflow-config.json")

    env_days_old = os.environ.get("DAYS_OLD")
    days_old = int(env_days_old) if env_days_old else conversion_cfg.get("max_age_days")
    if days_old is None:
        raise ValueError("Missing 'conversion.max_age_days' in workflow-config.json")

    threshold_timestamp = time.time() - (days_old * 86400)
    candidates = []
    
    pending_pdfs = set()
    if os.path.exists("pending_pdf_paths.txt"):
        with open("pending_pdf_paths.txt", "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    pending_pdfs.add(line.strip())

    for root, _, files in os.walk(pdf_source):
        for file in files:
            if not file.endswith(".pdf"):
                continue
            
            pdf_path = Path(root) / file
            
            # Convert to POSIX string for comparison with pending paths
            if pdf_path.as_posix() in pending_pdfs:
                continue

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
