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
    parser.add_argument("--target", default="development", help="Target branch to merge into (default: development)")
    parser.add_argument("--author-name", default="GitHub Action", help="Git commit author name")
    parser.add_argument("--author-email", default="action@github.com", help="Git commit author email")
    args = parser.parse_args()

    run_git(["config", "user.name", args.author_name])
    run_git(["config", "user.email", args.author_email])

    # Fetch latest remote references
    print("Fetching remote references...")
    run_git(["fetch", "origin"])

    # Ensure target branch is checked out
    print(f"Checking out target branch '{args.target}'...")
    ret, out, err = run_git(["checkout", args.target])
    if ret != 0:
        # Try checking out tracking branch from origin
        ret, out, err = run_git(["checkout", "-b", args.target, f"origin/{args.target}"])
        if ret != 0:
            print(f"Failed to check out target branch '{args.target}': {err}\n{out}", file=sys.stderr)
            return 1

    print(f"Merging {args.source} into {args.target}...")
    ret, out, err = run_git(["merge", args.source, "-m", f"Merge {args.source} into {args.target}"])
    if ret != 0:
        print(f"Git merge failed: {err}\n{out}", file=sys.stderr)
        return 1
    print(out)

    print(f"Pushing merged branch '{args.target}' to origin...")
    ret, out, err = run_git(["push", "origin", args.target])
    if ret != 0:
        print(f"Git push failed: {err}\n{out}", file=sys.stderr)
        return 1
    print(out)

    print(f"Branch synchronization of '{args.target}' completed successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
