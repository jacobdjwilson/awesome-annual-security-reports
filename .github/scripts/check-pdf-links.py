import sys
import re
import urllib.parse

def is_direct_pdf(url: str) -> bool:
    try:
        path = urllib.parse.urlparse(url).path.lower()
        return path.endswith(".pdf") or ".pdf/" in path or path.endswith(".pdf.gz")
    except Exception:
        return url.lower().endswith(".pdf")

def main():
    has_error = False
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                original_line = line
                line = line.strip()

                if line.startswith("- ["):
                    match = re.match(r'^-\s+\[[^\]]+\]\(([^)]+)\)', line)
                    if match:
                        url = match.group(1).strip()
                        if is_direct_pdf(url):
                            print(f"::error file=README.md,line={i}::Direct link to PDF found in the source link: {url}")
                            has_error = True

    except Exception as e:
        print(f"Error reading README.md: {e}")
        sys.exit(1)

    if has_error:
        print("Error: README.md contains direct links to PDFs in the author/organization source link. Please use the author's website or report landing page instead.")
        sys.exit(1)
    else:
        print("No direct PDF links found in source links.")

if __name__ == "__main__":
    main()

