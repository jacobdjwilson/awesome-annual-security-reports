import os
import re
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Set
import pypdf

# Configuration
MAX_FILE_SIZE_MB = 100
MAGIC_NUMBER = b"%PDF"

def get_year_from_dir(path: Path) -> str:
    """Extract year from the parent directory name."""
    if re.match(r'^\d{4}$', path.parent.name):
        return path.parent.name
    return "Unknown"

def get_year_from_filename(filename: str) -> str:
    """Extract year from filename (e.g., Report-2025 -> 2025)."""
    match = re.search(r'(\d{4})', filename)
    return match.group(1) if match else "Unknown"

def validate_pdf(file_path: Path) -> List[str]:
    """Validates PDF structure, magic numbers, and size."""
    issues = []
    
    # 1. Magic Number Check
    try:
        with open(file_path, 'rb') as f:
            header = f.read(4)
            if header != MAGIC_NUMBER:
                issues.append(f"Invalid file signature: Found {header}, expected {MAGIC_NUMBER}")
    except Exception as e:
        issues.append(f"Could not read file: {str(e)}")
        return issues

    # 2. File Size Check
    try:
        size_mb = file_path.stat().st_size / (1024 * 1024)
        if size_mb > MAX_FILE_SIZE_MB:
            issues.append(f"File size too large: {size_mb:.2f}MB > {MAX_FILE_SIZE_MB}MB")
    except Exception:
        pass # specific error caught above

    # 3. Structural Validity (pypdf)
    try:
        # strict=True checks for EOF markers and valid xref tables
        reader = pypdf.PdfReader(file_path, strict=True)
        if len(reader.pages) < 1:
            issues.append("PDF has 0 pages.")
    except Exception as e:
        issues.append(f"Corrupt PDF structure: {str(e)}")

    return issues

def check_markdown_content(file_path: Path) -> List[str]:
    """Checks for formatting issues and AI artifacts."""
    issues = []
    try:
        content = file_path.read_text(encoding='utf-8')
        
        # Check 1: Leftover code fences
        if content.strip().startswith('```') or content.strip().endswith('```'):
            issues.append("Contains leftover code block fences (```)")
            
        # Check 2: Conversational AI text
        ai_patterns = [
            r'^Here is the converted',
            r'^Sure, I can help',
            r'^I have converted',
            r'I cannot convert this file',
            r'I apologize, but',
            r'As an AI language model'
        ]
        for pattern in ai_patterns:
            if re.search(pattern, content, re.IGNORECASE | re.MULTILINE):
                issues.append(f"Contains AI conversational artifacts ('{pattern}')")
                break
        
        # Check 3: Specific Header Artifacts
        if content.strip().startswith('# Report Content Below'):
            issues.append("Begins with artifact header '# Report Content Below'")
        
        if content.strip().startswith('# AI Instruction Set for Converting Technical PDFs to Markdown'):
            issues.append("Begins with artifact header '# AI Instruction Set...'")

        # Check 4: Suspiciously short content
        if len(content.strip()) < 50:
            issues.append("File is suspiciously short (< 50 chars)")

    except Exception as e:
        issues.append(f"Error reading file: {str(e)}")
    
    return issues

def main():
    parser = argparse.ArgumentParser(description="Validate repository consistency")
    parser.add_argument("--pdf-root", default="Annual Security Reports", help="PDF root directory")
    parser.add_argument("--md-root", default="Markdown Conversions", help="Markdown root directory")
    parser.add_argument("--output-report", default="validation_report.md", help="Output report file")
    args = parser.parse_args()

    pdf_root = Path(args.pdf_root)
    md_root = Path(args.md_root)
    
    # Collect files recursively
    pdf_files = {p.stem: p for p in pdf_root.rglob("*.pdf")}
    md_files = {p.stem: p for p in md_root.rglob("*.md")}
    all_stems = sorted(list(set(pdf_files.keys()) | set(md_files.keys())))
    
    report_lines = []
    issues_found = False

    # --- Check 1: Corrupt PDFs ---
    pdf_issues = []
    for stem, path in pdf_files.items():
        errors = validate_pdf(path)
        if errors:
            pdf_issues.append(f"- **{path.name}** (`{path.parent.name}`): {'; '.join(errors)}")
            
    if pdf_issues:
        report_lines.append(f"### 📄 Corrupt or Invalid PDFs ({len(pdf_issues)})\n" + "\n".join(pdf_issues))
        issues_found = True

    # --- Check 2: Markdown Formatting ---
    md_errors = []
    for stem, path in md_files.items():
        file_issues = check_markdown_content(path)
        if file_issues:
            md_errors.append(f"- **{path.name}**: {', '.join(file_issues)}")

    if md_errors:
        report_lines.append(f"### ⚠️ Formatting & AI Artifacts ({len(md_errors)})\n" + "\n".join(md_errors))
        issues_found = True

    # --- Check 3: Year Mismatches ---
    mismatches = []
    for stem, path in {**pdf_files, **md_files}.items():
        dir_year = get_year_from_dir(path)
        file_year = get_year_from_filename(stem)
        
        if dir_year != "Unknown" and file_year != "Unknown":
            if dir_year != file_year:
                mismatches.append(f"- `{path}`: Directory is **{dir_year}** but filename indicates **{file_year}**.")

    if mismatches:
        report_lines.append(f"### 📅 Year Mismatches ({len(mismatches)})\n" + "\n".join(mismatches))
        issues_found = True

    # --- Check 4: Missing Conversions ---
    missing_md = []
    missing_pdf = []
    
    for stem in all_stems:
        if stem in pdf_files and stem not in md_files:
            missing_md.append(f"- **{stem}**: PDF exists in `{get_year_from_dir(pdf_files[stem])}`, missing Markdown.")
        elif stem in md_files and stem not in pdf_files:
            missing_pdf.append(f"- **{stem}**: Markdown exists in `{get_year_from_dir(md_files[stem])}`, missing PDF (Orphaned).")

    if missing_md:
        report_lines.append(f"### ❌ Missing Markdown Conversions ({len(missing_md)})\n" + "\n".join(missing_md))
        issues_found = True
    if missing_pdf:
        report_lines.append(f"### ❓ Orphaned Markdown Files ({len(missing_pdf)})\n" + "\n".join(missing_pdf))
        issues_found = True

    # Generate Report
    if issues_found:
        header = "# 🚨 Repository Validation Failed\n\nThe following inconsistencies were detected:\n\n"
        with open(args.output_report, "w", encoding="utf-8") as f:
            f.write(header + "\n\n".join(report_lines))
        print("Validation failed. Issues found.")
        sys.exit(1)
    else:
        print("Validation passed. No issues found.")
        sys.exit(0)

if __name__ == "__main__":
    main()