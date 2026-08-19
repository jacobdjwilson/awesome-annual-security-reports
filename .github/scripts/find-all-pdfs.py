import os
import json

def main():
    config_path = ".github/artifacts/workflow-config.json"
    pdf_source = "Annual Security Reports"
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            try:
                config = json.load(f)
                pdf_source = config.get("workflow", {}).get("folders", {}).get("pdf_source", "Annual Security Reports")
            except Exception:
                pass

    pdf_files = []
    for root, _, files in os.walk(pdf_source):
        for file in files:
            if file.endswith(".pdf"):
                pdf_files.append(os.path.join(root, file))

    with open("files_to_process.txt", "w", encoding="utf-8") as f:
        for pf in pdf_files:
            f.write(pf + "\n")

    print(f"Found {len(pdf_files)} PDFs.")

if __name__ == "__main__":
    main()
