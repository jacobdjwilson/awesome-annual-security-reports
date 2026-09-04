"""
Operational Purpose:
    Inspects validation findings for orphaned PDFs or stub conversions. If unhandled
    orphaned reports exist and the security reports pipeline is not actively running,
    dispatches a new run of security-reports-pipeline.yml on main. Replaces inline bash
    in repository-validator.yml.

Required Environment Variables:
    GH_TOKEN: GitHub authentication token.
    GITHUB_REPOSITORY (optional): Target repository slug.

Outputs:
    Standard output logs of finding evaluation and workflow dispatch status.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.gating.monitored_statuses)
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from typing import Dict, Any, List

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class OrphanDispatchConfigLoader:
    """Loads gating configuration from workflow-config.json with fail-fast validation."""

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
        gating_cfg = workflow.get("gating")
        if not gating_cfg or not isinstance(gating_cfg, dict):
            raise KeyError(f"Missing 'workflow.gating' section in '{self.config_path}'.")
        return gating_cfg

    @property
    def monitored_statuses(self) -> List[str]:
        statuses = self.config.get("monitored_statuses")
        if not isinstance(statuses, list) or not statuses:
            raise KeyError(f"Missing 'monitored_statuses' in 'workflow.gating' of '{self.config_path}'.")
        return [str(s).strip() for s in statuses]


def main() -> int:
    findings_path = Path("validation_findings.json")
    if not findings_path.exists():
        print(f"Findings file '{findings_path}' does not exist. Skipping dispatch.")
        return 0

    loader = OrphanDispatchConfigLoader()
    active_statuses = set(loader.monitored_statuses)

    try:
        with open(findings_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading '{findings_path}': {e}", file=sys.stderr)
        return 1

    findings = data.get("findings", [])
    orphan_or_stubs = [
        f for f in findings if f.get("category") in ("orphaned_pdf", "stub_markdown")
    ]

    if not orphan_or_stubs:
        print("⊘ No orphaned PDFs or stub conversions found — skipping auto-dispatch.")
        return 0

    print(f"Found {len(orphan_or_stubs)} orphaned or stub report(s). Checking pipeline activity...")

    repo = os.environ.get("GITHUB_REPOSITORY", "jacobdjwilson/awesome-annual-security-reports")
    cmd = [
        "gh", "run", "list",
        "--workflow", "security-reports-pipeline.yml",
        "--repo", repo,
        "--json", "status",
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0 and res.stdout.strip():
        try:
            runs = json.load(res.stdout)
            active_runs = [r for r in runs if r.get("status") in active_statuses]
            if active_runs:
                print(f"⊘ Pipeline already active ({len(active_runs)} active run(s)) — skipping dispatch.")
                return 0
        except Exception as e:
            print(f"Warning: Could not parse active runs: {e}", file=sys.stderr)

    print("🔄 Dispatching security-reports-pipeline.yml to convert orphaned PDFs...")
    dispatch_cmd = [
        "gh", "workflow", "run", "security-reports-pipeline.yml",
        "--repo", repo,
        "--ref", "main",
    ]
    dispatch_res = subprocess.run(dispatch_cmd, capture_output=True, text=True)
    if dispatch_res.returncode != 0:
        print(f"Error dispatching pipeline: {dispatch_res.stderr.strip()}", file=sys.stderr)
        return 1

    print("✓ Pipeline successfully dispatched on main.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
