"""
Operational Purpose:
    Executes the report-discovery.py pipeline runner while streaming logs to stdout and
    teeing to discovery_output.log. Invokes parse-discovery-output.py to export step
    telemetry to $GITHUB_OUTPUT and preserves the discovery process exit code.
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

    # Export outputs via parse-discovery-output.py
    parse_env = dict(os.environ)
    parse_env["EXIT_CODE"] = str(exit_code)
    subprocess.run([sys.executable, ".github/scripts/parse-discovery-output.py"], env=parse_env)

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
