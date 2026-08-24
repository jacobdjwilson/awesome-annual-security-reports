import os
import sys
import json
import subprocess

def run_cmd(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True, encoding='utf-8')
    except subprocess.CalledProcessError as e:
        print(f"Command failed (ignored): {cmd}")
        # We ignore errors because removing non-existent labels or creating existing ones might fail.

def main():
    issue_number = os.environ.get("ISSUE_NUMBER")
    label = os.environ.get("LABEL")

    if not issue_number or not label:
        print("ISSUE_NUMBER and LABEL environment variables are required.")
        sys.exit(1)

    # Load config
    config_path = ".github/artifacts/workflow-config.json"
    try:
        with open(config_path, "r") as f:
            config = json.load(f)
    except Exception as e:
        print(f"Error loading config: {e}")
        sys.exit(1)

    labels_config = config.get("workflow", {}).get("issue_triage", {}).get("labels", {})
    
    if label not in labels_config:
        print(f"Warning: label '{label}' not found in workflow-config.json. Proceeding with defaults.")
        color = "e4e669"
        description = ""
    else:
        color = labels_config[label].get("color", "e4e669")
        description = labels_config[label].get("description", "")

    # Create label if it doesn't exist
    run_cmd(f'gh label create "{label}" --color "{color}" --description "{description}"')

    # Remove all known triage outcome labels before applying the new one
    for old_label in labels_config.keys():
        run_cmd(f'gh issue edit "{issue_number}" --remove-label "{old_label}"')

    # Add the new label
    print(f"Applying label '{label}' to issue {issue_number}")
    run_cmd(f'gh issue edit "{issue_number}" --add-label "{label}"')

if __name__ == "__main__":
    main()
