"""
Operational Purpose:
    Manages automated pipeline retries upon AI quota exhaustion (HTTP 429).
    Loads retry delays and operational caps from workflow-config.json, performs
    the backoff sleep, and re-dispatches security-reports-pipeline.yml.
    Replaces inline bash in security-reports-pipeline.yml.

Required Environment Variables:
    GH_TOKEN: GitHub authentication token.
    GITHUB_REPO: Repository slug (e.g. owner/repo).
    GITHUB_REF_NAME (optional): Branch or ref to target for dispatch (default: main).
    RETRY_ATTEMPT (optional): Current retry attempt index (1, 2, 3).

Outputs:
    Standard output logs of backoff sleep and workflow dispatch execution.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.conversion.quota_retry_delays_seconds, workflow.conversion.max_quota_retry_attempts)
"""

import os
import sys
import time
import json
import subprocess
from pathlib import Path
from typing import Dict, Any

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class QuotaRetryConfigLoader:
    """Loads quota retry configuration from workflow-config.json with fail-fast validation."""

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
        conv_cfg = workflow.get("conversion")
        if not conv_cfg or not isinstance(conv_cfg, dict):
            raise KeyError(f"Missing 'workflow.conversion' in '{self.config_path}'.")
        return conv_cfg

    @property
    def max_attempts(self) -> int:
        val = self.config.get("max_quota_retry_attempts")
        if val is None:
            raise KeyError(f"Missing 'max_quota_retry_attempts' in workflow.conversion of '{self.config_path}'.")
        return int(val)

    @property
    def delays_by_attempt(self) -> Dict[str, int]:
        delays = self.config.get("quota_retry_delays_seconds")
        if not isinstance(delays, dict) or not delays:
            raise KeyError(f"Missing 'quota_retry_delays_seconds' dictionary in workflow.conversion of '{self.config_path}'.")
        return {str(k): int(v) for k, v in delays.items()}


def main() -> int:
    loader = QuotaRetryConfigLoader()
    max_attempts = loader.max_attempts
    delays = loader.delays_by_attempt

    raw_attempt = os.environ.get("RETRY_ATTEMPT", "1").strip()
    try:
        attempt = int(raw_attempt) if raw_attempt else 1
    except ValueError:
        attempt = 1

    if attempt >= max_attempts:
        print(f"⊘ Quota retry attempt {attempt} — reached limit ({max_attempts}). Giving up for today.")
        print("  Check Google AI Studio status page or quota dashboard.")
        return 0

    wait_seconds = delays.get(str(attempt))
    if wait_seconds is None:
        raise KeyError(
            f"No retry delay configured for attempt '{attempt}' in 'workflow.conversion.quota_retry_delays_seconds'."
        )

    next_attempt = attempt + 1
    wait_min = wait_seconds // 60
    print(f"⏳ Quota exhausted — sleeping {wait_min}m before retry attempt {next_attempt}...")
    time.sleep(wait_seconds)

    repo = os.environ.get("GITHUB_REPO", "jacobdjwilson/awesome-annual-security-reports")
    ref = os.environ.get("GITHUB_REF_NAME", "main")

    print(f"🔄 Dispatching retry run (attempt {next_attempt}) on {ref}...")
    cmd = [
        "gh", "workflow", "run", "security-reports-pipeline.yml",
        "--repo", repo,
        "--ref", ref,
        "--field", f"quota_retry_attempt={next_attempt}",
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error dispatching retry: {res.stderr.strip()}", file=sys.stderr)
        return 1

    print("✓ Retry dispatched successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
