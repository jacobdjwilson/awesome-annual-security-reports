"""
Operational Purpose:
    Scans the repository's PDF source directory for all PDF documents and writes
    their paths to files_to_process.txt for downstream workflow ingestion and scanning.

Required Environment Variables:
    None.

Outputs:
    files_to_process.txt: Text file containing all discovered PDF file paths.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.folders.pdf_source)
"""

import os
import sys
import json
from pathlib import Path
from typing import Dict, Any, List

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class PdfFinderConfigLoader:
    """Loads directory folder paths from workflow-config.json with fail-fast validation."""

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
        folders = workflow.get("folders")
        if not folders or not isinstance(folders, dict):
            raise KeyError(f"Missing 'workflow.folders' in '{self.config_path}'.")
        return folders

    @property
    def pdf_source(self) -> str:
        val = self.config.get("pdf_source")
        if not val:
            raise KeyError(f"Missing 'pdf_source' in workflow.folders of '{self.config_path}'.")
        return str(val)


def main() -> int:
    loader = PdfFinderConfigLoader()
    pdf_source = loader.pdf_source

    source_dir = Path(pdf_source)
    if not source_dir.exists():
        raise FileNotFoundError(f"PDF source directory '{source_dir}' does not exist.")

    pdf_files: List[str] = []
    for pdf_path in sorted(source_dir.rglob("*.pdf")):
        # Use POSIX formatting for consistency across platforms
        pdf_files.append(pdf_path.as_posix())

    output_file = Path("files_to_process.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        for pf in pdf_files:
            f.write(pf + "\n")

    print(f"✓ Discovered {len(pdf_files)} PDF file(s) in '{pdf_source}'. Saved to '{output_file}'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
