import os
import re
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Set, Tuple

def get_year_from_dir(path: Path) -> str:
    """Extract year from the immediate parent directory."""
    if re.match(r'^\d{4}$', path.parent.name):
        return path.parent.name
    return "Unknown"

def get_year_from_filename(filename: str) -> str:
    """Extract year from filename (e.g., Report-2025 -> 2025)."""
    match = re.search(r'(\d{4})', filename)
    return match.group(1) if match else "Unknown"

def check_markdown_content(file_path: Path) -> List[str]:
    """Check for formatting issues like leftover AI instructions or code fences."""
    issues = []
    try:
        content = file_path.read_text(encoding='utf-8')
        
        # Check 1: Unremoved code block fences at start/end
        if content.strip().startswith('```') or content.strip().endswith('```'):
            issues.append("Contains leftover code block fences (```)")
            
        # Check 2: Common AI chat instructions
        ai_patterns = [
            r'^Here is the converted markdown',
            r'^Sure, I can help',
            r'^I have converted the PDF',
            r'I cannot convert this file'
        ]
        for pattern in ai_patterns:
            if re.search(pattern, content, re.IGNORECASE | re.MULTILINE):
                issues.append(f"Contains AI conversational text ('{pattern}')")
                break
                
        # Check 3: Empty or too short
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
    
    # Collect files
    pdf_files = {p.stem: p for p in pdf_root.rglob("*.pdf")}
    md_files = {p.stem: p for p in md_root.rglob("*.md")}
    all_stems = set(pdf_files.keys()) | set(md_files.keys())
    
    report_lines = []
    issues_found = False

    # 1. Missing Files & Pairing
    missing_md = []
    missing_pdf = []
    
    for stem in sorted(all_stems):
        if stem in pdf_files and stem not in md_files:
            missing_md.append(f"- **{stem}**: PDF exists in `{get_year_from_dir(pdf_files[stem])}`, but Markdown is missing.")
        elif stem in md_files and stem not in pdf_files:
            missing_pdf.append(f"- **{stem}**: Markdown exists in `{get_year_from_dir(md_files[stem])}`, but PDF is missing (Orphaned).")

    if missing_md:
        report_lines.append(f"### ❌ Missing Markdown Conversions ({len(missing_md)})\n" + "\n".join(missing_md))
        issues_found = True
    if missing_pdf:
        report_lines.append(f"### ❓ Orphaned Markdown Files ({len(missing_pdf)})\n" + "\n".join(missing_pdf))
        issues_found = True

    # 2. Year & Directory Mismatches
    mismatches = []
    for stem, path in {**pdf_files, **md_files}.items():
        dir_year = get_year_from_dir(path)
        file_year = get_year_from_filename(stem)
        
        # Only check if both are known/valid years
        if dir_year != "Unknown" and file_year != "Unknown":
            if dir_year != file_year:
                mismatches.append(f"- `{path}`: Directory is **{dir_year}** but filename indicates **{file_year}**.")

    if mismatches:
        report_lines.append(f"### 📅 Year Mismatches ({len(mismatches)})\n" + "\n".join(mismatches))
        issues_found = True

    # 3. Content Formatting Checks
    formatting_errors = []
    for stem, path in md_files.items():
        file_issues = check_markdown_content(path)
        if file_issues:
            formatting_errors.append(f"- `{path}`: {', '.join(file_issues)}")

    if formatting_errors:
        report_lines.append(f"### ⚠️ Formatting & Content Issues ({len(formatting_errors)})\n" + "\n".join(formatting_errors))
        issues_found = True

    # Output generation
    if issues_found:
        header = "# 🚨 Repository Validation Failed\n\nThe following inconsistencies were detected in the repository:\n\n"
        with open(args.output_report, "w", encoding="utf-8") as f:
            f.write(header + "\n\n".join(report_lines))
        print("Issues found. Report generated.")
        sys.exit(1)
    else:
        print("No issues found.")
        sys.exit(0)

if __name__ == "__main__":
    main()