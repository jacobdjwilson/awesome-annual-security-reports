import sys
import re

def main():
    has_error = False
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                original_line = line
                line = line.strip()
                # Skip if there's an ignore directive
                if "<!-- pdf-link ignore -->" in original_line or "<!-- lint ignore -->" in original_line:
                    continue

                if line.startswith("- ["):
                    match = re.match(r'^-\s+\[[^\]]+\]\(([^)]+)\)', line)
                    if match:
                        url = match.group(1).strip()
                        if url.lower().endswith(".pdf"):
                            print(f"::error file=README.md,line={i}::Direct link to PDF found in the source link: {url}")
                            has_error = True

    except Exception as e:
        print(f"Error reading README.md: {e}")
        sys.exit(1)

    if has_error:
        print("Error: README.md contains direct links to PDFs. Please use landing pages instead. If you must link to a PDF, add '<!-- pdf-link ignore -->' to the end of the line.")
        sys.exit(1)
    else:
        print("No direct PDF links found in source links.")

if __name__ == "__main__":
    main()
