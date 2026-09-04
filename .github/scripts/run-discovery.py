"""
Operational Purpose:
    Executes the report-discovery.py pipeline runner while streaming logs to stdout and
    teeing to discovery_output.log. Parses emitted telemetry metrics directly to $GITHUB_OUTPUT
    and preserves the discovery process exit code.
    Replaces inline bash orchestration in report-discovery.yml.

Required Environment Variables:
    MAX_DISCOVERIES (optional): Maximum candidate reports to process.
    OVERRIDE_DATE (optional): Date override for deterministic testing (YYYY-MM-DD).
    GITHUB_OUTPUT (optional): Path to write step outputs.

Outputs:
    Writes discovery_output.log to working directory.
    Exports discovery counts to $GITHUB_OUTPUT.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json
"""

import os
import sys
import subprocess
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def main() -> int:
    cmd = [
        sys.executable,
        ".github/scripts/report-discovery.py",
        "--artifacts-dir",
        ".github/artifacts",
    ]

    max_disc = os.environ.get("MAX_DISCOVERIES")
    if max_disc and max_disc.strip():
        cmd.extend(["--max-discoveries", max_disc.strip()])

    override_date = os.environ.get("OVERRIDE_DATE")
    if override_date and override_date.strip():
        cmd.extend(["--date", override_date.strip()])

    log_path = Path("discovery_output.log")
    print(f"Executing discovery command: {' '.join(cmd)}")

    with open(log_path, "w", encoding="utf-8") as log_file:
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            encoding="utf-8",
            errors="replace",
        )
        if proc.stdout:
            for line in proc.stdout:
                sys.stdout.write(line)
                log_file.write(line)
        proc.wait()
        exit_code = proc.returncode

    # Export discovery telemetry metrics directly to $GITHUB_OUTPUT
    output_path = os.environ.get("GITHUB_OUTPUT")
    if output_path and log_path.exists():
        data = {}
        with open(log_path, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                if "=" in line:
                    parts = line.strip().split("=", 1)
                    if parts[0].startswith("DISCOVERY_"):
                        data[parts[0]] = parts[1]

        def parse(key: str) -> str:
            return data.get(key, "0")

        try:
            with open(output_path, "a", encoding="utf-8") as f:
                f.write(f"tasks={parse('DISCOVERY_TASKS')}\n")
                f.write(f"created={parse('DISCOVERY_CREATED')}\n")
                f.write(f"suppressed={parse('DISCOVERY_SUPPRESSED')}\n")
                f.write(f"skipped={parse('DISCOVERY_SKIPPED')}\n")
                f.write(f"pdf_finds={parse('DISCOVERY_PDF_FINDS')}\n")
                f.write(f"landing_finds={parse('DISCOVERY_LANDING_FINDS')}\n")
                f.write(f"tier_current={parse('DISCOVERY_TIER_CURRENT')}\n")
                f.write(f"tier_stale={parse('DISCOVERY_TIER_STALE')}\n")
                f.write(f"tier_old={parse('DISCOVERY_TIER_OLD')}\n")
                f.write(f"vt_clean={parse('DISCOVERY_VT_CLEAN')}\n")
                f.write(f"vt_suspicious={parse('DISCOVERY_VT_SUSPICIOUS')}\n")
                f.write(f"vt_malicious={parse('DISCOVERY_VT_MALICIOUS')}\n")
                f.write(f"exit_code={exit_code}\n")
        except Exception as e:
            print(f"Warning: Failed to export discovery metrics to GITHUB_OUTPUT: {e}", file=sys.stderr)

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
