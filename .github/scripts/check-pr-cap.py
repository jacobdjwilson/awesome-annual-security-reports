import os
import subprocess
import sys

def run_gh_query(args):
    result = subprocess.run(
        ["gh", "pr", "list", "--json", "number", "-q", "length"] + args,
        capture_output=True, text=True, check=False
    )
    if result.returncode != 0:
        print(f"Error running gh: {result.stderr}")
        sys.exit(1)
    return int(result.stdout.strip() or "0")

def main():
    max_open_prs = int(os.environ.get("MAX_OPEN_PRS", "5"))
    workflow = os.environ.get("WORKFLOW_TYPE", "general")
    
    github_output = os.environ.get("GITHUB_OUTPUT")
    if not github_output:
        print("Error: GITHUB_OUTPUT environment variable not set.")
        sys.exit(1)

    with open(github_output, "a") as f:
        if workflow == "refresh":
            refresh_pr_count = run_gh_query(["--state", "open", "--label", "maintenance", "--search", "Refresh in:title"])
            if refresh_pr_count > 0:
                print("⊘ Existing refresh PR found, skipping")
                f.write("pr_exists=true\n")
                f.write("skip_reason=existing_refresh_pr\n")
                f.write("cap_reached=true\n")
                return

        open_count = run_gh_query(["--state", "open", "--label", "automated"])
        print(f"Open automated PRs: {open_count} / {max_open_prs}")
        
        f.write(f"open_count={open_count}\n")
        if open_count >= max_open_prs:
            print(f"⊘ PR cap reached ({open_count} >= {max_open_prs}) — skipping")
            f.write("pr_exists=true\n")
            f.write("skip_reason=pr_cap_reached\n")
            f.write("cap_reached=true\n")
        else:
            print(f"✓ PR cap OK ({open_count} < {max_open_prs})")
            f.write("pr_exists=false\n")
            f.write("skip_reason=\n")
            f.write("cap_reached=false\n")

if __name__ == "__main__":
    main()
