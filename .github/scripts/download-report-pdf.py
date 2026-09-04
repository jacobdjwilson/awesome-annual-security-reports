"""
Operational Purpose:
    Downloads a suggested report PDF, verifies its canonical filename and '%PDF' magic
    byte header, ensures integrity, writes step outputs to $GITHUB_OUTPUT, and optionally
    comments on failure. Replaces inline bash download logic in ingest-suggestion.yml.

Required Environment Variables:
    URL: Direct link to PDF.
    YEAR: Report year.
    ORG: Organization name.
    TITLE (optional): Report title.
    ISSUE_NUMBER (optional): Issue number for failure commenting.
    GH_TOKEN (optional): GitHub token for issue interaction.
    GITHUB_OUTPUT (optional): Path to write step outputs.

Outputs:
    file_path: Relative path to saved PDF.
    file_name: Canonical filename of the saved PDF.
    file_size: Size in bytes of the downloaded PDF.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.folders.pdf_source, workflow.discovery.pdf_magic_number)
"""

import os
import sys
import re
import time
import json
import urllib.parse
import urllib.request
import subprocess
from pathlib import Path
from typing import Dict, Any

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class DownloadPdfConfigLoader:
    """Loads pdf folder configuration from workflow-config.json with fail-fast validation."""

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
        discovery = workflow.get("discovery")
        if not folders or not isinstance(folders, dict):
            raise KeyError(f"Missing 'workflow.folders' in '{self.config_path}'.")
        if not discovery or not isinstance(discovery, dict):
            raise KeyError(f"Missing 'workflow.discovery' in '{self.config_path}'.")
        return {"folders": folders, "discovery": discovery}

    @property
    def pdf_source_folder(self) -> str:
        f = self.config["folders"].get("pdf_source")
        if not f:
            raise KeyError(f"Missing 'pdf_source' in workflow.folders of '{self.config_path}'.")
        return str(f)

    @property
    def pdf_magic_number(self) -> str:
        m = self.config["discovery"].get("pdf_magic_number")
        if not m:
            raise KeyError(f"Missing 'pdf_magic_number' in workflow.discovery of '{self.config_path}'.")
        return str(m)


def derive_filename(url: str, org: str, title: str, year: str) -> str:
    parsed = urllib.parse.urlparse(url)
    raw_name = Path(parsed.path).name.split("?")[0].split("#")[0]
    if raw_name.lower().endswith(".pdf") and len(raw_name) > 4:
        return raw_name

    safe_org = re.sub(r"[^A-Za-z0-9\-]", "", org.replace(" ", "-"))
    safe_title = re.sub(r"[^A-Za-z0-9\-]", "", title.replace(" ", "-")) if title else "Security-Report"
    return f"{safe_org}-{safe_title}-{year}.pdf"


def download_file(url: str, dest_path: Path, max_attempts: int = 3, timeout: int = 120) -> bool:
    headers = {"User-Agent": "Mozilla/5.0 (compatible; awesome-annual-security-reports/1.0)"}
    req = urllib.request.Request(url, headers=headers)

    for attempt in range(1, max_attempts + 1):
        try:
            print(f"Downloading from '{url}' (attempt {attempt}/{max_attempts})...")
            with urllib.request.urlopen(req, timeout=timeout) as response, open(dest_path, "wb") as out_file:
                out_file.write(response.read())
            print(f"✓ Downloaded successfully: {dest_path.name}")
            return True
        except Exception as e:
            print(f"! Attempt {attempt} failed: {e}", file=sys.stderr)
            if attempt < max_attempts:
                time.sleep(5)
    return False


def main() -> int:
    loader = DownloadPdfConfigLoader()
    pdf_source = loader.pdf_source_folder
    expected_magic = loader.pdf_magic_number

    url = (os.environ.get("URL") or "").strip()
    year = (os.environ.get("YEAR") or "").strip()
    org = (os.environ.get("ORG") or "").strip()
    title = (os.environ.get("TITLE") or "").strip()
    issue_number = os.environ.get("ISSUE_NUMBER")
    gh_output = os.environ.get("GITHUB_OUTPUT")

    if not url or not year or not org:
        print("Error: Missing required environment variables URL, YEAR, or ORG.", file=sys.stderr)
        return 1

    dest_dir = Path(pdf_source) / year
    dest_dir.mkdir(parents=True, exist_ok=True)

    filename = derive_filename(url, org, title, year)
    dest_path = dest_dir / filename

    success = download_file(url, dest_path)
    if not success:
        print(f"❌ Download failed after multiple attempts.", file=sys.stderr)
        if issue_number and os.environ.get("GH_TOKEN"):
            comment_body = (
                "❌ **Download failed** — the PDF could not be retrieved from the provided URL.\n\n"
                "Common causes:\n"
                "- The URL requires a login or redirects to an interactive landing page\n"
                "- The link has expired or the file has moved\n"
                "- The server blocked automated download requests\n\n"
                "Please verify the URL is a **direct, public link to the PDF** and update the issue.\n"
                "Remove and re-add the `report-suggestion` label to retry."
            )
            subprocess.run(["gh", "issue", "comment", str(issue_number), "--body", comment_body], capture_output=True)
        return 1

    # Verify magic bytes
    try:
        with open(dest_path, "rb") as f:
            header = f.read(len(expected_magic)).decode("latin1", errors="ignore")
    except Exception as e:
        print(f"Error reading downloaded file: {e}", file=sys.stderr)
        dest_path.unlink(missing_ok=True)
        return 1

    if header != expected_magic:
        print(f"❌ Downloaded file is not a valid PDF (header: '{header}', expected: '{expected_magic}').", file=sys.stderr)
        dest_path.unlink(missing_ok=True)
        return 1

    file_size = dest_path.stat().st_size
    print(f"✓ PDF verified — {file_size} bytes at {dest_path.as_posix()}")

    if gh_output:
        with open(gh_output, "a", encoding="utf-8") as f:
            f.write(f"file_path={dest_path.as_posix()}\n")
            f.write(f"file_name={filename}\n")
            f.write(f"file_size={file_size}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
