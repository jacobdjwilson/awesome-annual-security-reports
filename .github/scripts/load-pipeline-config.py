import json
import os
import sys

def main():
    with open(".github/artifacts/workflow-config.json") as f:
        config = json.load(f)

    discovery = config.get("workflow", {}).get("discovery", {})
    folders = config.get("workflow", {}).get("folders", {})
    conversion = config.get("workflow", {}).get("conversion", {})
    pull_request = config.get("workflow", {}).get("pull_request", {})

    outputs = {
        "max_size_mb": discovery.get("max_file_size_mb", 100),
        "default_limit": discovery.get("default_limit", 10),
        "pdf_magic": discovery.get("pdf_magic_number", "%PDF"),
        "pdf_source": folders.get("pdf_source", "Annual Security Reports"),
        "md_folder": folders.get("markdown_conversions", "Markdown Conversions"),
        "max_age_days": conversion.get("max_age_days", 90),
        "push_mode": discovery.get("push_mode", "missing_conversion"),
        "push_batch_limit": discovery.get("push_batch_limit", 20),
        "max_open_prs": pull_request.get("max_open_automated_prs", 5)
    }

    print("✓ Loaded configuration:")
    for k, v in outputs.items():
        print(f"  {k}: {v}")

    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a") as f:
            for k, v in outputs.items():
                f.write(f"{k}={v}\n")

if __name__ == "__main__":
    main()
