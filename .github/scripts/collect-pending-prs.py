import os
import subprocess
import json
import sys

def main():
    with open(".github/artifacts/workflow-config.json") as f:
        config = json.load(f)
        md_folder = config.get("workflow", {}).get("folders", {}).get("markdown_conversions", "Markdown Conversions")
        pdf_source = config.get("workflow", {}).get("folders", {}).get("pdf_source", "Annual Security Reports")

    result = subprocess.run(
        ["gh", "pr", "list", "--state", "open", "--label", "automated", "--json", "headRefName", "-q", ".[].headRefName"],
        capture_output=True, text=True, check=False
    )
    if result.returncode != 0:
        print(f"Error fetching PRs: {result.stderr}")
        sys.exit(1)

    branches = [b.strip() for b in result.stdout.split('\n') if b.strip()]
    
    pending_pdfs = []
    
    if not branches:
        print("⊘ No open automated PRs — no paths to exclude")
    else:
        print("Open automated PR branches:")
        for branch in branches:
            print(f"  {branch}")
            # Fetch branch
            subprocess.run(["git", "fetch", "origin", branch, "--depth=1"], capture_output=True, check=False)
            
            # Diff
            diff_res = subprocess.run(
                ["git", "diff", "--name-only", "HEAD", f"origin/{branch}", "--", f"{md_folder}/"],
                capture_output=True, text=True, check=False
            )
            
            md_files = [m.strip() for m in diff_res.stdout.split('\n') if m.strip()]
            for md_file in md_files:
                pdf_path = md_file.replace(md_folder, pdf_source).replace(".md", ".pdf")
                pending_pdfs.append(pdf_path)
                print(f"    → will skip: {pdf_path}")

    with open("pending_pdf_paths.txt", "w") as f:
        for pdf in pending_pdfs:
            f.write(pdf + "\n")

    pending_count = len(pending_pdfs)
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a") as f:
            f.write(f"pending_count={pending_count}\n")
            
    print(f"✓ PDFs with pending conversions in open PRs: {pending_count}")

if __name__ == "__main__":
    main()
