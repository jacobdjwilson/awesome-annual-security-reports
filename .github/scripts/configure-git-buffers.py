"""
Operational Purpose:
    Configures local/global Git HTTP buffers and timeout parameters to support
    reliable push operations for large annual security report PDF files.
    Replaces inline bash git configuration in ingest-suggestion.yml.

Required Environment Variables:
    None.

Outputs:
    Standard output logs of Git configuration updates.

JSON Artifact Dependencies:
    None.
"""

import os
import sys
import subprocess

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def main() -> int:
    settings = [
        ("http.postBuffer", "524288000"),
        ("http.lowSpeedLimit", "0"),
        ("http.lowSpeedTime", "300"),
    ]

    for key, val in settings:
        res = subprocess.run(["git", "config", "--global", key, val], capture_output=True, text=True)
        if res.returncode != 0:
            print(f"Warning: Failed to set git config {key}: {res.stderr.strip()}", file=sys.stderr)

    print("✓ Git HTTP buffers and timeouts configured for large files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
