"""
Operational Purpose:
    Scans converted Markdown reports to detect stale conversions that were generated
    using older AI models, exceed age thresholds, or fall below minimum length requirements.
    Prioritizes lowest model tiers and oldest conversion dates to enforce model upgrade invariance.

Required Environment Variables:
    PDF_SOURCE (optional): Directory containing PDF source reports.
    MD_FOLDER (optional): Directory containing Markdown conversions.
    LIMIT (optional): Batch size limit for stale file queue.
    DAYS_OLD (optional): Maximum age in days before a conversion is deemed stale.

Outputs:
    files_to_process.txt: List of PDF file paths queued for reconversion.

JSON Artifact Dependencies:
    .github/artifacts/ai-models.json (task_models.conversion.primary, models.primary, model_hierarchy)
    .github/artifacts/workflow-config.json (workflow.conversion, workflow.folders)
"""

import os
import sys
import json
import time
import re
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple, Set


class StaleCheckerConfigLoader:
    """Loads configuration and model hierarchy from .github/artifacts with fail-fast validation."""

    def __init__(self, artifacts_dir: str = ".github/artifacts") -> None:
        self.artifacts_dir = Path(artifacts_dir)
        self.models_path = self.artifacts_dir / "ai-models.json"
        self.wf_path = self.artifacts_dir / "workflow-config.json"

        if not self.models_path.exists():
            raise FileNotFoundError(f"Missing required artifact: {self.models_path}")
        if not self.wf_path.exists():
            raise FileNotFoundError(f"Missing required artifact: {self.wf_path}")

        try:
            with open(self.models_path, "r", encoding="utf-8") as f:
                self.models_data: Dict[str, Any] = json.load(f)
        except Exception as e:
            raise ValueError(f"Failed to parse {self.models_path}: {e}") from e

        try:
            with open(self.wf_path, "r", encoding="utf-8") as f:
                self.wf_data: Dict[str, Any] = json.load(f).get("workflow", {})
        except Exception as e:
            raise ValueError(f"Failed to parse {self.wf_path}: {e}") from e

        conversion_task_models = self.models_data.get("task_models", {}).get("conversion", {})
        self.primary_model: str = (
            conversion_task_models.get("primary")
            or self.models_data.get("models", {}).get("primary")
        )
        if not self.primary_model:
            raise ValueError("Missing 'task_models.conversion.primary' or 'models.primary' in ai-models.json")

        self.model_hierarchy: List[str] = self.models_data.get("model_hierarchy", [
            "gemini-3.1-flash-lite-preview",
            "gemini-3.1-flash-lite",
            "gemini-3.5-flash-lite",
            "gemini-3.7-flash",
            "gemini-3.8-flash",
        ])

        folders_cfg = self.wf_data.get("folders", {})
        conversion_cfg = self.wf_data.get("conversion", {})

        self.pdf_source: str = os.environ.get("PDF_SOURCE") or folders_cfg.get("pdf_source")
        self.md_folder: str = os.environ.get("MD_FOLDER") or folders_cfg.get("markdown_conversions")
        if not self.pdf_source or not self.md_folder:
            raise ValueError("Missing 'folders.pdf_source' or 'folders.markdown_conversions' in workflow-config.json")

        env_limit = os.environ.get("LIMIT")
        self.limit: int = int(env_limit) if env_limit else conversion_cfg.get("refresh_batch_limit", 10)

        env_days_old = os.environ.get("DAYS_OLD")
        self.days_old: int = int(env_days_old) if env_days_old else conversion_cfg.get("max_age_days", 90)


def get_model_rank(model_name: Optional[str], hierarchy: List[str]) -> int:
    """
    Returns an integer rank for model comparison based on canonical hierarchy.
    Higher values indicate newer or higher capability models.
    """
    if not model_name:
        return -1
    if model_name in hierarchy:
        return hierarchy.index(model_name)

    # Version-based heuristic fallback if model name contains decimal version
    m = re.search(r"(\d+(?:\.\d+)?)", model_name)
    if m:
        try:
            val = int(float(m.group(1)) * 100)
            if "preview" in model_name.lower():
                val -= 1
            return val
        except ValueError:
            pass
    return -1


def main() -> int:
    config = StaleCheckerConfigLoader()
    primary_model = config.primary_model
    hierarchy = config.model_hierarchy
    primary_rank = get_model_rank(primary_model, hierarchy)

    threshold_timestamp = time.time() - (config.days_old * 86400)
    candidates: List[Tuple[int, int, float, str]] = []

    pending_pdfs: Set[str] = set()
    if os.path.exists("pending_pdf_paths.txt"):
        with open("pending_pdf_paths.txt", "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    pending_pdfs.add(line.strip())

    for root, _, files in os.walk(config.pdf_source):
        for file in files:
            if not file.endswith(".pdf"):
                continue

            pdf_path = Path(root) / file
            if pdf_path.as_posix() in pending_pdfs:
                continue

            rel_path = pdf_path.relative_to(config.pdf_source)
            md_path = Path(config.md_folder) / rel_path.with_suffix(".md")

            # Priority 0: Missing Markdown conversion
            if not md_path.exists():
                candidates.append((0, 0, 0.0, str(pdf_path)))
                continue

            try:
                content = md_path.read_text(encoding="utf-8", errors="ignore")
                match = re.search(r"<!-- CONVERSION_METADATA: (\{.*?\}) -->", content)

                # Priority 1: Missing metadata tag
                if not match:
                    candidates.append((1, 0, 0.0, str(pdf_path)))
                    continue

                meta = json.loads(match.group(1))
                cached_model = meta.get("model")
                cached_rank = get_model_rank(cached_model, hierarchy)

                date_str = meta.get("date")
                ts = 0.0
                if date_str:
                    try:
                        ts = datetime.strptime(date_str, "%Y-%m-%d").timestamp()
                    except ValueError:
                        ts = 0.0

                # Priority 2: Converted with lower-tier model (prioritize lowest rank and oldest date)
                if cached_rank < primary_rank:
                    candidates.append((2, cached_rank, ts, str(pdf_path)))
                    continue

                # Priority 3: Converted with primary or higher model, but exceeds max age threshold
                if ts and ts < threshold_timestamp:
                    candidates.append((3, 0, ts, str(pdf_path)))

            except Exception:
                candidates.append((1, 0, 0.0, str(pdf_path)))

    # Sort candidates by:
    # 1. Candidate tier (0 = missing md, 1 = missing meta, 2 = lower model, 3 = expired age)
    # 2. Model rank ascending (lowest model tier processed first)
    # 3. Timestamp ascending (oldest conversions processed first)
    # 4. Filepath as deterministic tiebreaker
    candidates.sort(key=lambda x: (x[0], x[1], x[2], x[3]))

    file_count = min(len(candidates), config.limit)
    with open("files_to_process.txt", "w", encoding="utf-8") as f:
        for c in candidates[:config.limit]:
            f.write(c[3] + "\n")

    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as f:
            if file_count > 0:
                f.write("has_files=true\n")
                f.write(f"file_count={file_count}\n")
                print(f"✓ Found {file_count} files to refresh (from {len(candidates)} total candidates)")
            else:
                f.write("has_files=false\n")
                f.write("file_count=0\n")
                print("⊘ No stale files found")

    return 0


if __name__ == "__main__":
    sys.exit(main())
