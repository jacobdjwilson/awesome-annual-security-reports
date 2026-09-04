"""
Operational Purpose:
    Discovers, validates, and batches PDF files needing processing based on workflow triggers
    (push, pull_request, schedule, workflow_dispatch). Enforces size and magic byte constraints,
    excludes pending PR branches, and exports files_to_process.txt and step outputs.

Required Environment Variables:
    GITHUB_EVENT_NAME: Workflow event name.
    CAP_REACHED (optional): If 'true', skips discovery due to automated PR limit.
    LIMIT_COUNT (optional): Manual batch size limit override.
    YEAR_FILTER (optional): Year filter string.
    CATEGORY_FILTER (optional): Category directory filter string.
    ORG_FILTER (optional): Organization name filter substring.
    SKIP_EXISTING (optional): If 'true', skips files that already have markdown conversions.
    GITHUB_OUTPUT (optional): Path to write step outputs.

Outputs:
    Writes files_to_process.txt and invalid_files.txt.
    Exports has_files, file_count, and scan_mode to $GITHUB_OUTPUT.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.discovery, workflow.conversion, workflow.folders)
"""

import os
import sys
import json
import time
import subprocess
from pathlib import Path
from typing import Dict, Any, List, Tuple, Set

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class FileFinderConfigLoader:
    """Loads file discovery and folder settings from workflow-config.json with fail-fast validation."""

    def __init__(self, artifacts_dir: str = ".github/artifacts") -> None:
        self.config_path = Path(artifacts_dir) / "workflow-config.json"
        self.config = self._load()

    def _load(self) -> Dict[str, Any]:
        if not self.config_path.exists():
            raise FileNotFoundError(f"Missing required artifact: '{self.config_path}'.")
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            raise ValueError(f"Failed to parse JSON artifact '{self.config_path}': {e}") from e

        workflow = data.get("workflow", {})
        discovery = workflow.get("discovery")
        conversion = workflow.get("conversion")
        folders = workflow.get("folders")

        if not discovery or not isinstance(discovery, dict):
            raise KeyError(f"Missing 'workflow.discovery' in '{self.config_path}'.")
        if not conversion or not isinstance(conversion, dict):
            raise KeyError(f"Missing 'workflow.conversion' in '{self.config_path}'.")
        if not folders or not isinstance(folders, dict):
            raise KeyError(f"Missing 'workflow.folders' in '{self.config_path}'.")

        return {"discovery": discovery, "conversion": conversion, "folders": folders}

    @property
    def max_size_mb(self) -> int:
        val = self.config["discovery"].get("max_file_size_mb")
        if val is None:
            raise KeyError("Missing 'max_file_size_mb' in workflow.discovery.")
        return int(val)

    @property
    def default_limit(self) -> int:
        val = self.config["discovery"].get("default_limit")
        if val is None:
            raise KeyError("Missing 'default_limit' in workflow.discovery.")
        return int(val)

    @property
    def pdf_magic(self) -> str:
        val = self.config["discovery"].get("pdf_magic_number")
        if not val:
            raise KeyError("Missing 'pdf_magic_number' in workflow.discovery.")
        return str(val)

    @property
    def push_mode(self) -> str:
        val = self.config["discovery"].get("push_mode")
        if not val:
            raise KeyError("Missing 'push_mode' in workflow.discovery.")
        return str(val)

    @property
    def push_batch_limit(self) -> int:
        val = self.config["discovery"].get("push_batch_limit")
        if val is None:
            raise KeyError("Missing 'push_batch_limit' in workflow.discovery.")
        return int(val)

    @property
    def pdf_source(self) -> str:
        val = self.config["folders"].get("pdf_source")
        if not val:
            raise KeyError("Missing 'pdf_source' in workflow.folders.")
        return str(val)

    @property
    def md_folder(self) -> str:
        val = self.config["folders"].get("markdown_conversions")
        if not val:
            raise KeyError("Missing 'markdown_conversions' in workflow.folders.")
        return str(val)

    @property
    def max_age_days(self) -> int:
        val = self.config["conversion"].get("max_age_days")
        if val is None:
            raise KeyError("Missing 'max_age_days' in workflow.conversion.")
        return int(val)


def run_cmd(cmd: List[str]) -> List[str]:
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    return result.stdout.split("\n") if result.returncode == 0 else []


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(description="Discover and batch PDF files for processing.")
    parser.add_argument("--all", action="store_true", help="Discover all PDF files in the repository.")
    args, _ = parser.parse_known_args()

    gh_output = os.environ.get("GITHUB_OUTPUT")
    loader = FileFinderConfigLoader()
    pdf_source = loader.pdf_source

    if args.all:
        print(f"Mode: Discover all PDFs in '{pdf_source}'")
        source_dir = Path(pdf_source)
        if not source_dir.exists():
            raise FileNotFoundError(f"PDF source directory '{source_dir}' does not exist.")
        all_pdfs = [p.as_posix() for p in sorted(source_dir.rglob("*.pdf"))]
        with open("files_to_process.txt", "w", encoding="utf-8") as f:
            for pf in all_pdfs:
                f.write(pf + "\n")
        print(f"✓ Discovered {len(all_pdfs)} PDF file(s) in '{pdf_source}'. Saved to 'files_to_process.txt'.")
        if gh_output:
            with open(gh_output, "a", encoding="utf-8") as f:
                f.write(f"has_files={'true' if all_pdfs else 'false'}\n")
                f.write(f"file_count={len(all_pdfs)}\n")
                f.write("scan_mode=all\n")
        return 0

    # If automated PR cap is reached, skip immediately and emit safe outputs
    if os.environ.get("CAP_REACHED", "").lower() == "true":
        print("⊘ Automated PR cap reached — skipping file discovery.")
        if gh_output:
            with open(gh_output, "a", encoding="utf-8") as f:
                f.write("has_files=false\n")
                f.write("file_count=0\n")
                f.write("scan_mode=skipped_pr_cap\n")
        return 0

    github_event_name = os.environ.get("GITHUB_EVENT_NAME", "")

    max_size_mb = loader.max_size_mb
    default_limit = loader.default_limit
    pdf_magic = loader.pdf_magic
    push_mode = loader.push_mode
    push_batch_limit = loader.push_batch_limit
    md_folder = loader.md_folder
    max_age_days = loader.max_age_days

    raw_limit = os.environ.get("LIMIT_COUNT")
    limit = int(raw_limit) if raw_limit and raw_limit.strip() else default_limit

    year_filter = os.environ.get("YEAR_FILTER", "").strip()
    category_filter = os.environ.get("CATEGORY_FILTER", "").strip()
    org_filter = os.environ.get("ORG_FILTER", "").strip()
    skip_existing = os.environ.get("SKIP_EXISTING", "true").lower() == "true"

    all_pdfs: List[str] = []
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

        needs_conversion: List[Tuple[float, str]] = []
        now = time.time()
        for root, _, files in os.walk(pdf_source):
            for file in files:
                if file.endswith(".pdf"):
                    pdf_path = os.path.join(root, file)
                    rel_path = Path(pdf_path).relative_to(pdf_source)
                    md_path = Path(md_folder) / rel_path.with_suffix(".md")

                    if not md_path.exists():
                        needs_conversion.append((0.0, pdf_path))
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
            all_missing: List[str] = []
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
        base_ref = os.environ.get("GITHUB_BASE_REF") or "main"
        target_ref = f"origin/{base_ref}...HEAD" if not base_ref.startswith("origin/") else f"{base_ref}...HEAD"
        added = run_cmd(["git", "diff", "--name-only", "--diff-filter=A", target_ref])
        deleted = run_cmd(["git", "diff", "--name-only", "--diff-filter=D", target_ref])
        added = [f for f in added if f.startswith(pdf_source) and f.endswith(".pdf")]
        deleted = [f for f in deleted if f.startswith(pdf_source) and f.endswith(".pdf")]

        if not added and deleted:
            print("⊘ Only deletions detected — nothing to process")
            scan_mode = "pr_delete_only"
        else:
            all_pdfs = added

    # Exclude pending PR branches
    if os.path.exists("pending_pdf_paths.txt"):
        with open("pending_pdf_paths.txt", "r", encoding="utf-8") as f:
            pending: Set[str] = set(line.strip() for line in f if line.strip())
        before = len(all_pdfs)
        all_pdfs = [p for p in all_pdfs if p not in pending]
        excluded = before - len(all_pdfs)
        if excluded > 0:
            print(f"⊘ Excluded {excluded} PDF(s) already covered by an open automated PR")

    valid_files: List[str] = []
    max_size_bytes = max_size_mb * 1024 * 1024
    with open("invalid_files.txt", "w", encoding="utf-8") as invalid_f:
        for pdf_path in all_pdfs:
            if not os.path.exists(pdf_path):
                invalid_f.write(f"{pdf_path}|File Not Found\n")
                continue

            file_size = os.path.getsize(pdf_path)
            if file_size > max_size_bytes:
                invalid_f.write(
                    f"{pdf_path}|Size Limit Exceeded ({file_size / 1024 / 1024:.1f} MB > {max_size_mb} MB)\n"
                )
                continue

            with open(pdf_path, "rb") as pf:
                magic = pf.read(len(pdf_magic)).decode("latin1", errors="ignore")
                if magic != pdf_magic:
                    invalid_f.write(f"{pdf_path}|Invalid PDF (Magic: '{magic}')\n")
                    continue

            valid_files.append(pdf_path)
            print(f"✓ Valid: {pdf_path}")

    with open("files_to_process.txt", "w", encoding="utf-8") as f:
        for vf in valid_files:
            f.write(vf + "\n")

    has_files_val = "true" if valid_files else "false"
    file_count_val = len(valid_files)

    if gh_output:
        with open(gh_output, "a", encoding="utf-8") as f:
            f.write(f"has_files={has_files_val}\n")
            f.write(f"file_count={file_count_val}\n")
            f.write(f"scan_mode={scan_mode}\n")

    if valid_files:
        print(f"✓ {file_count_val} files to process")
    else:
        print("⊘ No files to process")

    return 0


if __name__ == "__main__":
    sys.exit(main())
