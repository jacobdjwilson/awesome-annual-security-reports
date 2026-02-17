import os
import re
import sys
import json
import argparse
from pathlib import Path
from urllib.parse import unquote
from typing import List, Dict, Set, Tuple
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

def load_category_structure(json_path: Path) -> Tuple[Dict, List[str]]:
    """Load and parse the category structure from JSON."""
    issues = []
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data, issues
    except FileNotFoundError:
        issues.append(f"Category JSON file not found: {json_path}")
        return {}, issues
    except json.JSONDecodeError as e:
        issues.append(f"Invalid JSON in category file: {str(e)}")
        return {}, issues
    except Exception as e:
        issues.append(f"Error loading category file: {str(e)}")
        return {}, issues

def extract_readme_structure(readme_path: Path) -> Tuple[Dict[str, List[str]], List[str]]:
    """
    Extract the category structure from README.md.
    Returns a dict mapping parent categories to their subcategories,
    and a list of issues encountered.
    """
    issues = []
    structure = {}
    
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the start of category sections (after "## Analysis Reports" or "## Survey Reports")
        parent_pattern = r'^##\s+(Analysis Reports|Survey Reports)\s*$'
        subcat_pattern = r'^###\s+(.+?)\s*$'
        
        lines = content.split('\n')
        current_parent = None
        
        for line in lines:
            parent_match = re.match(parent_pattern, line)
            if parent_match:
                current_parent = parent_match.group(1)
                structure[current_parent] = []
                continue
            
            if current_parent:
                subcat_match = re.match(subcat_pattern, line)
                if subcat_match:
                    subcat_name = subcat_match.group(1)
                    structure[current_parent].append(subcat_name)
                    
                # Stop collecting when we hit "## Resources" or another major section
                if re.match(r'^##\s+(?!Analysis|Survey)', line):
                    current_parent = None
        
    except FileNotFoundError:
        issues.append(f"README.md not found: {readme_path}")
    except Exception as e:
        issues.append(f"Error reading README.md: {str(e)}")
    
    return structure, issues

def validate_readme_structure(readme_path: Path, categories_path: Path) -> List[str]:
    """
    Validate that README.md structure matches report-categories.json.
    """
    issues = []
    
    # Load expected structure from JSON
    json_data, json_issues = load_category_structure(categories_path)
    issues.extend(json_issues)
    if json_issues:
        return issues
    
    # Extract actual structure from README
    readme_structure, readme_issues = extract_readme_structure(readme_path)
    issues.extend(readme_issues)
    if readme_issues:
        return issues
    
    # Build expected structure from JSON
    expected_structure = {}
    if 'categories' in json_data:
        for category in json_data['categories']:
            parent_name = category.get('parent')
            if parent_name:
                expected_structure[parent_name] = [
                    sub.get('name') for sub in category.get('sub_categories', [])
                ]
    
    # Compare structures
    # 1. Check parent categories
    expected_parents = set(expected_structure.keys())
    actual_parents = set(readme_structure.keys())
    
    missing_parents = expected_parents - actual_parents
    extra_parents = actual_parents - expected_parents
    
    for parent in missing_parents:
        issues.append(f"README.md missing parent category: '{parent}'")
    
    for parent in extra_parents:
        issues.append(f"README.md has unexpected parent category: '{parent}'")
    
    # 2. Check subcategories for each parent
    for parent in expected_parents & actual_parents:
        expected_subs = set(expected_structure[parent])
        actual_subs = set(readme_structure[parent])
        
        missing_subs = expected_subs - actual_subs
        extra_subs = actual_subs - expected_subs
        
        for sub in missing_subs:
            issues.append(f"README.md missing subcategory '{sub}' under '{parent}'")
        
        for sub in extra_subs:
            issues.append(f"README.md has unexpected subcategory '{sub}' under '{parent}'")
        
        # 3. Check order of subcategories (should match JSON order)
        if expected_subs == actual_subs:
            expected_order = expected_structure[parent]
            actual_order = readme_structure[parent]
            
            if expected_order != actual_order:
                issues.append(
                    f"README.md subcategory order mismatch under '{parent}'. "
                    f"Expected: {expected_order}, Found: {actual_order}"
                )
    
    return issues

def validate_readme_report_entries(readme_path: Path, pdf_root: Path) -> List[str]:
    """
    Validate that all PDF reports are listed in README.md with proper formatting.
    """
    issues = []
    
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()
    except Exception as e:
        issues.append(f"Error reading README.md: {str(e)}")
        return issues
    
    # Get all PDF files
    pdf_files = list(pdf_root.rglob("*.pdf"))
    
    # Pattern to match report entries in README
    # Example: - [Source](url) - [Report Name](path/to/report.pdf) (YYYY) - Description
    report_pattern = r'-\s+\[([^\]]+)\]\(([^)]+)\)\s+-\s+\[([^\]]+)\]\(([^)]+)\)\s+\((\d{4})\)'
    
    # Extract all report entries from README
    readme_reports = {}
    for match in re.finditer(report_pattern, readme_content):
        source = match.group(1)
        raw_path = match.group(4)
        pdf_path = unquote(raw_path) 
        year = match.group(5)
        
        # Store using the decoded path as key so checking keys later works
        readme_reports[pdf_path] = {
            'source': source,
            'year': year,
            'line': match.group(0),
            'raw_path': raw_path # Keep raw path if needed for reporting
        }
    
    # Check each PDF file is listed in README
    for pdf_file in pdf_files:
        # Convert to relative path from root
        try:
            rel_path = pdf_file.relative_to(Path.cwd())
            rel_path_str = str(rel_path).replace('\\', '/')
            
            # Check if this PDF is in README
            if rel_path_str not in readme_reports:
                issues.append(f"PDF not listed in README.md: {rel_path_str}")
            else:
                # Validate year matches directory
                entry = readme_reports[rel_path_str]
                dir_year = get_year_from_dir(pdf_file)
                
                if dir_year != "Unknown" and entry['year'] != dir_year:
                    issues.append(
                        f"Year mismatch for {rel_path_str}: "
                        f"README shows ({entry['year']}), file is in {dir_year}/ directory"
                    )
        except ValueError:
            # Path is not relative to CWD
            pass
    
    # Check for entries in README that don't have corresponding PDFs
    for pdf_path in readme_reports.keys():
        full_path = Path(pdf_path)
        if not full_path.exists():
            issues.append(f"README.md references non-existent PDF: {pdf_path}")
    
    return issues

def validate_readme_links(readme_path: Path) -> List[str]:
    """
    Validate that all markdown links in README are properly formatted.
    """
    issues = []
    
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        issues.append(f"Error reading README.md: {str(e)}")
        return issues
    
    # Check for broken markdown link syntax
    # Pattern: text without proper link formatting
    broken_link_patterns = [
        r'\]\([^\)]*\s+[^\)]*\)',  # Space in URL
        r'\[[^\]]*\]\(\)',  # Empty URL
        r'\[\]\([^\)]+\)',  # Empty link text
    ]
    
    for pattern in broken_link_patterns:
        matches = re.finditer(pattern, content)
        for match in matches:
            issues.append(f"Malformed markdown link: {match.group(0)}")
    
    return issues

def main():
    parser = argparse.ArgumentParser(description="Validate repository consistency")
    parser.add_argument("--pdf-root", default="Annual Security Reports", help="PDF root directory")
    parser.add_argument("--md-root", default="Markdown Conversions", help="Markdown root directory")
    parser.add_argument("--readme", default="README.md", help="README file path")
    parser.add_argument("--categories", default=".github/report-categories.json", help="Categories JSON file path")
    parser.add_argument("--output-report", default="validation_report.md", help="Output report file")
    args = parser.parse_args()

    pdf_root = Path(args.pdf_root)
    md_root = Path(args.md_root)
    readme_path = Path(args.readme)
    categories_path = Path(args.categories)
    
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

    # --- Check 5: README Structure Validation ---
    structure_issues = validate_readme_structure(readme_path, categories_path)
    if structure_issues:
        formatted_issues = [f"- {issue}" for issue in structure_issues]
        report_lines.append(
            f"### 📋 README.md Structure Issues ({len(structure_issues)})\n" + 
            "\n".join(formatted_issues)
        )
        issues_found = True

    # --- Check 6: README Report Entries ---
    entry_issues = validate_readme_report_entries(readme_path, pdf_root)
    if entry_issues:
        formatted_issues = [f"- {issue}" for issue in entry_issues]
        report_lines.append(
            f"### 📝 README.md Report Entry Issues ({len(entry_issues)})\n" + 
            "\n".join(formatted_issues)
        )
        issues_found = True

    # --- Check 7: README Link Validation ---
    link_issues = validate_readme_links(readme_path)
    if link_issues:
        formatted_issues = [f"- {issue}" for issue in link_issues]
        report_lines.append(
            f"### 🔗 README.md Link Issues ({len(link_issues)})\n" + 
            "\n".join(formatted_issues)
        )
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