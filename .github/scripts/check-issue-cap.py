import os
import sys
import subprocess
import json

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command {cmd}: {e}")
        return ""

def write_output(key, value):
    output_file = os.environ.get("GITHUB_OUTPUT")
    if output_file:
        with open(output_file, "a") as f:
            f.write(f"{key}={value}\n")

def main():
    config_path = ".github/artifacts/workflow-config.json"
    max_issues = 20
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            try:
                config = json.load(f)
                max_issues = config.get("workflow", {}).get("discovery", {}).get("max_open_automated_issues", 20)
            except Exception:
                pass

    open_count_str = run_cmd('gh issue list --state open --label "automated" --json number -q length')
    open_count = int(open_count_str) if open_count_str.isdigit() else 0

    print(f"Open automated issues: {open_count} / {max_issues}")

    if open_count >= max_issues:
        write_output("cap_reached", "true")
        write_output("open_count", open_count)
        write_output("max_issues", max_issues)
        print(f"⊘ Issue cap reached ({open_count} >= {max_issues}) — skipping discovery.")
        print("  Triage and close open automated issues to unblock future discovery runs.")
    else:
        write_output("cap_reached", "false")
        write_output("open_count", open_count)
        write_output("max_issues", max_issues)
        print(f"✓ Issue cap OK ({open_count} < {max_issues})")

if __name__ == "__main__":
    main()
