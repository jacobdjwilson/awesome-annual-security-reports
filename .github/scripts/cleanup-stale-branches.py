import os
import sys
import subprocess
import json

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return ""

def run_cmd_bool(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False

def write_output(key, value):
    output_file = os.environ.get("GITHUB_OUTPUT")
    if output_file:
        with open(output_file, "a") as f:
            f.write(f"{key}={value}\n")

def main():
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    protected_branches = ["main", "development"]

    deleted = []
    skipped = []

    print("Scanning for stale branches from closed (unmerged) PRs...\n")

    page = 1
    while True:
        batch_str = run_cmd(f"gh api 'repos/{repo}/pulls?state=closed&per_page=100&page={page}' --jq '[.[] | select(.merged_at == null) | {{number: .number, branch: .head.ref, closed_at: .closed_at}}]'")
        
        try:
            batch = json.loads(batch_str)
        except json.JSONDecodeError:
            break

        if not batch:
            break

        for pr in batch:
            pr_num = pr.get("number")
            branch = pr.get("branch")
            closed_at = pr.get("closed_at")

            if branch in protected_branches:
                print(f"  [PR #{pr_num}] ⊘ Skipping protected branch: {branch}")
                skipped.append(f"{branch} (PR #{pr_num} — protected)")
                continue

            # Check if branch exists
            if not run_cmd_bool(f"gh api 'repos/{repo}/git/refs/heads/{branch}' --silent"):
                print(f"  [PR #{pr_num}] ⊘ Branch already gone: {branch}")
                continue

            pr_sha = run_cmd(f"gh api 'repos/{repo}/pulls/{pr_num}' --jq '.head.sha'")
            branch_sha = run_cmd(f"gh api 'repos/{repo}/git/refs/heads/{branch}' --jq '.object.sha'")

            if pr_sha != branch_sha:
                print(f"  [PR #{pr_num}] ⊘ Branch has new commits since PR closed — skipping: {branch}")
                skipped.append(f"{branch} (PR #{pr_num} — new commits after close)")
                continue

            # Delete branch
            run_cmd_bool(f"gh api --method DELETE 'repos/{repo}/git/refs/heads/{branch}'")
            print(f"  [PR #{pr_num}] 🗑️  Deleted: {branch} (closed {closed_at})")
            deleted.append(f"{branch} (PR #{pr_num}, closed {closed_at})")

        page += 1

    print(f"\nDone. Deleted: {len(deleted)} branch(es), skipped: {len(skipped)}.")

    with open("/tmp/deleted_branches.txt", "w") as f:
        f.write("\n".join(deleted) + "\n" if deleted else "")
    with open("/tmp/skipped_branches.txt", "w") as f:
        f.write("\n".join(skipped) + "\n" if skipped else "")

    write_output("deleted_count", len(deleted))
    write_output("skipped_count", len(skipped))

if __name__ == "__main__":
    main()
