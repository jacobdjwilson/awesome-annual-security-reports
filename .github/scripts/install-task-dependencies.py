"""
Operational Purpose:
    Installs Python package dependencies for a specified workflow task by dynamically
    loading the required package list from .github/artifacts/workflow-config.json.
    Eliminates inline jq/pip script logic from GitHub Actions workflows.

Required Environment Variables:
    None.

Outputs:
    Standard output / error streams logging package installation progress.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.<task>.python_packages)
"""

import os
import sys
import json
import argparse
import subprocess
from pathlib import Path
from typing import Dict, Any, List

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class TaskDependencyConfigLoader:
    """Loads Python and system package dependencies from workflow-config.json with fail-fast validation."""

    def __init__(self, task: str, artifacts_dir: str = ".github/artifacts") -> None:
        self.task = task
        self.config_path = Path(artifacts_dir) / "workflow-config.json"
        self.task_cfg = self._load_task_cfg()
        self.packages = self._load_python_packages()
        self.system_packages = self._load_system_packages()

    def _load_task_cfg(self) -> Dict[str, Any]:
        if not self.config_path.exists():
            raise FileNotFoundError(f"Missing required artifact: '{self.config_path}'.")
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            raise ValueError(f"Failed to parse JSON artifact '{self.config_path}': {e}") from e

        workflow = data.get("workflow", {})
        task_cfg = workflow.get(self.task)
        if not task_cfg or not isinstance(task_cfg, dict):
            raise KeyError(f"Task '{self.task}' missing or invalid in 'workflow' section of '{self.config_path}'.")
        return task_cfg

    def _load_python_packages(self) -> List[str]:
        packages = self.task_cfg.get("python_packages")
        if not packages or not isinstance(packages, list):
            raise KeyError(f"Missing 'python_packages' list for task '{self.task}' in '{self.config_path}'.")
        return [str(p).strip() for p in packages if str(p).strip()]

    def _load_system_packages(self) -> List[str]:
        sys_pkgs = self.task_cfg.get("system_packages", [])
        if not isinstance(sys_pkgs, list):
            raise ValueError(f"'system_packages' for task '{self.task}' in '{self.config_path}' must be a list.")
        return [str(p).strip() for p in sys_pkgs if str(p).strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Install dependencies for a workflow task.")
    parser.add_argument("--task", required=True, help="Task identifier in workflow-config.json (e.g. virustotal, conversion)")
    parser.add_argument("--system", action="store_true", help="Also install system apt packages if declared")
    parser.add_argument("--artifacts-dir", default=".github/artifacts", help="Directory containing JSON artifacts")
    args = parser.parse_args()

    loader = TaskDependencyConfigLoader(task=args.task, artifacts_dir=args.artifacts_dir)

    if args.system and loader.system_packages:
        print(f"Installing system packages for task '{args.task}': {' '.join(loader.system_packages)}")
        subprocess.run(["sudo", "apt-get", "update"])
        sys_cmd = ["sudo", "apt-get", "install", "-y"] + loader.system_packages
        sys_res = subprocess.run(sys_cmd)
        if sys_res.returncode != 0:
            print(f"Failed to install system packages for task '{args.task}'.", file=sys.stderr)
            return sys_res.returncode

    packages = loader.packages
    if not packages:
        print(f"No Python packages declared for task '{args.task}'.")
        return 0

    print(f"Installing Python dependencies for task '{args.task}': {' '.join(packages)}")
    cmd = [sys.executable, "-m", "pip", "install", "--break-system-packages"] + packages
    res = subprocess.run(cmd)
    if res.returncode != 0:
        print(f"Failed to install Python dependencies for task '{args.task}'. Exit code: {res.returncode}", file=sys.stderr)
        return 1

    print(f"Successfully installed dependencies for task '{args.task}'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
