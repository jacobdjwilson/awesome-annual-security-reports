"""
Operational Purpose:
    Merges upstream source branch into a target branch (e.g. main into development)
    and pushes the merged commits, replacing embedded inline git bash in sync-dev.yml.

Required Environment Variables:
    None. Uses local git configuration / runner context.

Outputs:
    Standard output logs of the git merge and push operations.

JSON Artifact Dependencies:
    None.
"""

import os
import sys
import argparse
import subprocess
from typing import List, Tuple

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def run_git(args: List[str]) -> Tuple[int, str, str]:
    cmd = ["git"] + args
    res = subprocess.run(cmd, capture_output=True, text=True)
    return res.returncode, res.stdout.strip(), res.stderr.strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Merge source branch into target branch.")
    parser.add_argument("--source", default="origin/main", help="Source branch to merge (default: origin/main)")
    parser.add_argument("--author-name", default="GitHub Action", help="Git commit author name")
    parser.add_argument("--author-email", default="action@github.com", help="Git commit author email")
    args = parser.parse_args()

    run_git(["config", "user.name", args.author_name])
    run_git(["config", "user.email", args.author_email])

    print(f"Merging {args.source} into current branch...")
    ret, out, err = run_git(["merge", args.source])
    if ret != 0:
        print(f"Git merge failed: {err}\n{out}", file=sys.stderr)
        return 1
    print(out)

    print("Pushing merged branch to remote...")
    ret, out, err = run_git(["push"])
    if ret != 0:
        print(f"Git push failed: {err}\n{out}", file=sys.stderr)
        return 1
    print(out)

    print("Branch synchronization completed successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
