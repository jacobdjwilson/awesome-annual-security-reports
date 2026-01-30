import os
import sys
import json
import re
import argparse
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional
from datetime import datetime

class CategoryManager:
    """Manages report categories from the centralized JSON definition."""
    
    def __init__(self, categories_path: str = ".github/report-categories.json"):
        self.categories_path = Path(categories_path)
        self.categories = self._load_categories()
        self.category_map = self._build_category_map()
        
    def _load_categories(self) -> Dict[str, Any]:
        """Load categories from JSON file."""
        if not self.categories_path.exists():
            print(f"WARNING: Categories file not found at {self.categories_path}")
            print("Using fallback categories...")
            return self._get_fallback_categories()
        
        try:
            with open(self.categories_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"✓ Loaded categories from {self.categories_path}")
                return data
        except json.JSONDecodeError as e:
            print(f"ERROR: Failed to parse categories JSON: {e}")
            return self._get_fallback_categories()
    
    def _get_fallback_categories(self) -> Dict[str, Any]:
        """Fallback categories if JSON file is not available."""
        return {
            "categories": [
                {
                    "parent": "Analysis Reports",
                    "parent_id": "analysis-reports",
                    "sub_categories": [
                        {"id": "global-threat-intelligence", "name": "Global Threat Intelligence"},
                        {"id": "application-security", "name": "Application Security"},
                        {"id": "cloud-security", "name": "Cloud Security"},
                        {"id": "vulnerabilities", "name": "Vulnerabilities"},
                        {"id": "ransomware", "name": "Ransomware"},
                        {"id": "data-breaches", "name": "Data Breaches"}
                    ]
                },
                {
                    "parent": "Survey Reports",
                    "parent_id": "survey-reports",
                    "sub_categories": [
                        {"id": "industry-trends", "name": "Industry Trends"},
                        {"id": "executive-perspectives", "name": "Executive Perspectives"},
                        {"id": "identity-security", "name": "Identity Security"}
                    ]
                }
            ]
        }
    
    def _build_category_map(self) -> Dict[str, Dict[str, str]]:
        """Build a searchable map of categories for quick lookup."""
        cat_map = {}
        
        for parent_cat in self.categories.get("categories", []):
            parent_name = parent_cat["parent"]
            
            for sub_cat in parent_cat.get("sub_categories", []):
                cat_id = sub_cat["id"]
                cat_name = sub_cat["name"]
                
                # Store both by ID and by name (normalized)
                cat_map[cat_id] = {
                    "name": cat_name,
                    "parent": parent_name,
                    "id": cat_id
                }
                
                # Also map by normalized name for fuzzy matching
                normalized_name = self._normalize_text(cat_name)
                cat_map[normalized_name] = {
                    "name": cat_name,
                    "parent": parent_name,
                    "id": cat_id
                }
        
        return cat_map
    
    def _normalize_text(self, text: str) -> str:
        """Normalize text for comparison."""
        # Remove common words, spaces, hyphens, and convert to lowercase
        text = re.sub(r'\s+|-|_', '', text.lower())
        text = re.sub(r'the|and|of|for|in|on|at|to|a|an', '', text)
        return text
    
    def match_category(self, category_hint: str, report_type: str = "Analysis") -> Tuple[str, str, float]:
        """
        Match a category hint to the best category.
        
        Returns: (category_name, parent_type, confidence_score)
        """
        if not category_hint:
            return self._get_default_category(report_type)
        
        # Try exact match first
        normalized_hint = self._normalize_text(category_hint)
        
        if normalized_hint in self.category_map:
            match = self.category_map[normalized_hint]
            return match["name"], match["parent"], 1.0
        
        # Try fuzzy matching
        best_match = None
        best_score = 0.0
        
        for key, cat_info in self.category_map.items():
            if isinstance(key, str) and not key.startswith("_"):
                score = self._similarity_score(normalized_hint, key)
                if score > best_score and score > 0.5:  # Minimum threshold
                    best_score = score
                    best_match = cat_info
        
        if best_match:
            return best_match["name"], best_match["parent"], best_score
        
        # No good match found, use default
        return self._get_default_category(report_type)
    
    def _similarity_score(self, str1: str, str2: str) -> float:
        """Calculate simple similarity score between two strings."""
        if not str1 or not str2:
            return 0.0
        
        # Jaccard similarity on character bigrams
        bigrams1 = set(str1[i:i+2] for i in range(len(str1)-1))
        bigrams2 = set(str2[i:i+2] for i in range(len(str2)-1))
        
        if not bigrams1 or not bigrams2:
            return 0.0
        
        intersection = len(bigrams1.intersection(bigrams2))
        union = len(bigrams1.union(bigrams2))
        
        return intersection / union if union > 0 else 0.0
    
    def _get_default_category(self, report_type: str) -> Tuple[str, str, float]:
        """Get default category based on report type."""
        if "survey" in report_type.lower():
            return "Industry Trends", "Survey Reports", 0.0
        else:
            return "Global Threat Intelligence", "Analysis Reports", 0.0
    
    def get_all_categories(self) -> Dict[str, List[str]]:
        """Get all categories organized by parent."""
        result = {}
        
        for parent_cat in self.categories.get("categories", []):
            parent_name = parent_cat["parent"]
            sub_cats = [sub["name"] for sub in parent_cat.get("sub_categories", [])]
            result[parent_name] = sub_cats
        
        return result
    
    def validate_toc(self, readme_content: str) -> Tuple[bool, List[str]]:
        """
        Validate that README TOC matches category definitions.
        
        Returns: (is_valid, list_of_issues)
        """
        issues = []
        all_categories = self.get_all_categories()
        
        # Extract TOC section from README
        toc_match = re.search(r'<!-- TOC -->(.*?)<!-- /TOC -->', readme_content, re.DOTALL)
        if not toc_match:
            issues.append("TOC markers not found in README")
            return False, issues
        
        toc_content = toc_match.group(1)
        
        # Check each category exists in TOC
        for parent, subcats in all_categories.items():
            # Check parent section
            parent_pattern = rf'-\s*\[{re.escape(parent)}\]'
            if not re.search(parent_pattern, toc_content):
                issues.append(f"Missing parent section in TOC: {parent}")
            
            # Check subcategories
            for subcat in subcats:
                subcat_pattern = rf'-\s*\[{re.escape(subcat)}\]'
                if not re.search(subcat_pattern, toc_content):
                    issues.append(f"Missing subcategory in TOC: {subcat} (under {parent})")
        
        return len(issues) == 0, issues

class ReadmeParser:
    def __init__(self, readme_path: str, category_manager: CategoryManager):
        self.readme_path = Path(readme_path)
        self.category_manager = category_manager
        
        if not self.readme_path.exists():
            raise FileNotFoundError(f"README.md not found: {readme_path}")
        
        self.content = self.readme_path.read_text(encoding='utf-8')
        self.structure = self._parse_structure()

    def _parse_structure(self) -> Dict[str, Any]:
        """Parses the README structure using category definitions."""
        structure = {}
        all_categories = self.category_manager.get_all_categories()
        
        for parent, subcats in all_categories.items():
            structure[parent] = {
                "subsections": {subcat: {} for subcat in subcats}
            }
        
        return structure

    def find_section_bounds(self, heading_name: str, level: int = 3) -> Tuple[int, int]:
        """
        Finds start and end indices of a specific section content.
        
        Args:
            heading_name: The section heading to find
            level: Heading level (2 for ##, 3 for ###)
        """
        # Build pattern for the specified heading level
        header_marker = '#' * level
        pattern = rf'^{header_marker}\s+{re.escape(heading_name)}\s*$'
        
        match = re.search(pattern, self.content, re.MULTILINE)
        if not match:
            return -1, -1
        
        start = match.end() + 1
        
        # Find next header of same or higher level to determine end
        next_header_pattern = rf'\n#{{{1,{level}}}}\s+'
        next_header = re.search(next_header_pattern, self.content[start:])
        end = start + next_header.start() if next_header else len(self.content)
        
        return start, end

class ReadmeUpdater:
    def __init__(self, parser: ReadmeParser, category_manager: CategoryManager):
        self.parser = parser
        self.category_manager = category_manager

    def add_report_entry(self, analysis: Dict[str, Any]) -> Tuple[bool, str, int, str]:
        """Orchestrates adding a report entry using category-aware logic."""
        if not self._validate_data(analysis):
            return False, "", -1, "invalid_or_stale_data"
        
        # Use CategoryManager to determine best category
        category_hint = analysis.get('category', '')
        report_type = analysis.get('type', 'Analysis')
        
        category_name, parent_type, confidence = self.category_manager.match_category(
            category_hint, report_type
        )
        
        # Log category matching
        if confidence < 1.0:
            print(f"  Category matching: '{category_hint}' -> '{category_name}' "
                  f"(confidence: {confidence:.2f})")
        else:
            print(f"  Category: {category_name} (exact match)")
        
        # Update analysis with matched category
        analysis['category'] = category_name
        analysis['type'] = parent_type.replace(" Reports", "")
        
        # Try to insert into the matched section
        success, entry_text, line_num, action = self._insert_into_section(analysis, category_name)
        
        if success:
            return success, entry_text, line_num, action
        
        # Fallback: try parent section
        main_section = f"{parent_type}"
        success, entry_text, line_num, action = self._insert_into_parent_section(
            analysis, main_section
        )
        
        if success:
            return success, entry_text, line_num, action
        
        # Last resort: append to file
        return self._append_to_file(analysis)

    def _insert_into_section(self, analysis: Dict[str, Any], section_name: str) -> Tuple[bool, str, int, str]:
        """Inserts or updates an entry within a specific section."""
        start, end = self.parser.find_section_bounds(section_name, level=3)
        if start == -1:
            return False, "", -1, "section_not_found"
        
        content_slice = self.parser.content[start:end]
        entry_text = self._format_entry(analysis)
        
        existing_line, existing_year = self._find_existing(content_slice, analysis)
        
        if existing_line:
            try:
                if int(analysis['year']) >= existing_year:
                    new_slice = content_slice.replace(existing_line, entry_text)
                    action = "updated" if int(analysis['year']) > existing_year else "refreshed"
                else:
                    return False, "", -1, "older_version"
            except (ValueError, TypeError):
                return False, "", -1, "invalid_year"
        else:
            new_slice = self._sort_and_insert(content_slice, entry_text)
            action = "new"
        
        self.parser.content = self.parser.content[:start] + new_slice + self.parser.content[end:]
        return True, entry_text, self._find_line_number(entry_text.strip()), action

    def _insert_into_parent_section(self, analysis: Dict[str, Any], parent_section: str) -> Tuple[bool, str, int, str]:
        """Insert into parent section (## level) as fallback."""
        start, end = self.parser.find_section_bounds(parent_section, level=2)
        if start == -1:
            return False, "", -1, "parent_section_not_found"
        
        # Find or create a "General" subsection
        general_header = "\n### General\n\n"
        if "### General" not in self.parser.content[start:end]:
            # Insert General section at the beginning of parent section
            self.parser.content = (
                self.parser.content[:start] + 
                general_header + 
                self.parser.content[start:]
            )
            # Adjust end pointer
            end += len(general_header)
        
        # Now insert into General subsection
        return self._insert_into_section(analysis, "General")

    def _append_to_file(self, analysis: Dict[str, Any]) -> Tuple[bool, str, int, str]:
        """Appends entry to the end of the file as a last resort fallback."""
        entry_text = self._format_entry(analysis)
        new_content = f"\n\n## Uncategorized Reports\n\n### General\n\n{entry_text}\n"
        self.parser.content = self.parser.content.rstrip() + new_content
        print("WARNING: Entry appended to end of file as 'Uncategorized' - manual review recommended")
        return True, entry_text, self._find_line_number(entry_text.strip()), "new"

    def _format_entry(self, analysis: Dict[str, Any]) -> str:
        """Formats the markdown list item, ensuring summary is a single line."""
        pdf_name = Path(analysis['pdf_path']).name
        pdf_link = f"Annual Security Reports/{analysis['year']}/{pdf_name}".replace(' ', '%20')
        
        # Sanitize summary: remove newlines/tabs and collapse spaces
        summary = ' '.join(analysis['summary'].strip('"').split())

        return (f"- [{analysis['organization']}]({analysis['organization_url']}) "
                f"- [{analysis['title']}]({pdf_link}) ({analysis['year']}) - {summary}")

    def _sort_and_insert(self, content: str, entry: str) -> str:
        """Inserts new entry while maintaining alphabetical order by Organization."""
        lines = [l for l in content.strip().split('\n') if l.strip().startswith('- [')]
        lines.append(entry)
        
        # Sort based on Organization name extracted from markdown link
        lines.sort(key=lambda x: re.search(r'- \[([^\]]+)\]', x).group(1).lower() if re.search(r'- \[([^\]]+)\]', x) else x.lower())
        return '\n'.join(lines) + '\n'

    def _find_existing(self, content: str, analysis: Dict[str, Any]) -> Tuple[Optional[str], Optional[int]]:
        """
        Checks for existing entry to prevent duplicates using three signals:
        1. Exact Organization and Title match.
        2. Organization URL match (handles rebranding).
        3. PDF Filename match (handles series updates).
        """
        org_norm = analysis['organization'].lower()
        title_norm = self._normalize_title(analysis['title'])
        target_url = analysis['organization_url'].lower().rstrip('/')
        target_pdf = Path(analysis['pdf_path']).name.lower()

        # Remove year from PDF filename for generic series matching
        target_pdf_base = re.sub(r'\d{4}', '', target_pdf).strip('-_ ')

        for line in content.split('\n'):
            if not line.strip().startswith('- ['): 
                continue
            
            # Extract Components: - [Org](OrgURL) - [Title](PdfURL) (Year)
            match = re.search(r'^- \[([^\]]+)\]\(([^\)]+)\) - \[([^\]]+)\]\(([^\)]+)\)\s*\((\d{4})\)', line.strip())
            if match:
                curr_org = match.group(1).lower()
                curr_org_url = match.group(2).lower().rstrip('/')
                curr_title = self._normalize_title(match.group(3))
                curr_pdf_url = match.group(4).lower()
                curr_year = int(match.group(5))

                # Check 1: URL Match (Strongest signal)
                if target_url == curr_org_url:
                    return line, curr_year

                # Check 2: PDF Filename Match
                curr_pdf_name = Path(curr_pdf_url).name
                curr_pdf_base = re.sub(r'\d{4}', '', curr_pdf_name).strip('-_ ')
                if target_pdf_base == curr_pdf_base and target_pdf_base != "":
                    return line, curr_year

                # Check 3: Org and Title Match
                if curr_org == org_norm and curr_title == title_norm:
                    return line, curr_year

        return None, None

    def _normalize_title(self, title: str) -> str:
        """Normalize title for comparison."""
        return re.sub(r'\s+|the|of|and', '', title.lower())

    def _find_line_number(self, text: str) -> int:
        """Find line number of text in content."""
        for i, line in enumerate(self.parser.content.split('\n'), 1):
            if text in line: 
                return i
        return -1

    def _validate_data(self, data: Dict[str, Any]) -> bool:
        """Validates presence of data and ensures report is not older than 2 years."""
        required = ['organization', 'title', 'year', 'summary', 'type', 'category', 'pdf_path', 'organization_url']
        
        # Basic field validation
        if any(not data.get(f) for f in required):
            print(f"ERROR: Missing fields in analysis: {[f for f in required if not data.get(f)]}")
            return False
        
        # Date threshold validation
        try:
            report_year = int(data.get('year'))
            current_year = datetime.now().year
            if (current_year - report_year) >= 2:
                print(f"SKIPPING: Report from {report_year} is older than the 2-year threshold.")
                return False
        except (ValueError, TypeError):
            print(f"ERROR: Invalid year format for {data.get('organization')}")
            return False

        return True

    def save(self):
        """Save updated content to README."""
        self.parser.readme_path.write_text(self.parser.content, encoding='utf-8')
        print(f"README successfully updated: {self.parser.readme_path}")

    def validate_and_report_toc(self):
        """Validate TOC against category definitions and report issues."""
        is_valid, issues = self.category_manager.validate_toc(self.parser.content)
        
        if is_valid:
            print("✓ TOC validation passed - all categories present")
        else:
            print("⚠ TOC validation issues found:")
            for issue in issues:
                print(f"  - {issue}")
        
        return is_valid, issues

def main():
    parser = argparse.ArgumentParser(description="Update README with security reports")
    parser.add_argument("analysis_json", help="Path to analysis results JSON")
    parser.add_argument("--readme-path", default="README.md", help="Path to README.md")
    parser.add_argument("--categories-path", default=".github/report-categories.json", 
                       help="Path to categories JSON")
    parser.add_argument("--validate-toc", action="store_true", 
                       help="Validate TOC against category definitions")
    args = parser.parse_args()

    # Initialize category manager
    try:
        category_manager = CategoryManager(args.categories_path)
        print(f"✓ Category manager initialized with {len(category_manager.category_map)} categories")
    except Exception as e:
        print(f"ERROR: Failed to initialize category manager: {e}")
        sys.exit(1)

    # Load analysis results
    if not os.path.exists(args.analysis_json) or os.path.getsize(args.analysis_json) < 2:
        print(f"ERROR: Invalid analysis file: {args.analysis_json}")
        sys.exit(1)

    try:
        with open(args.analysis_json, 'r') as f:
            results = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: JSON Decode Error: {e}")
        sys.exit(1)

    if not results:
        print("No analysis results found. Exiting.")
        sys.exit(0)

    print(f"Processing {len(results)} reports...")
    
    # Initialize updater
    try:
        readme_parser = ReadmeParser(args.readme_path, category_manager)
        updater = ReadmeUpdater(readme_parser, category_manager)
    except Exception as e:
        print(f"ERROR: Parser init failed: {e}")
        sys.exit(1)

    # Validate TOC if requested
    if args.validate_toc:
        print("\n=== TOC Validation ===")
        updater.validate_and_report_toc()
        print()

    # Process reports
    stats = {"new": 0, "updated": 0, "refreshed": 0, "errors": 0}
    changes_pending = False

    for i, analysis in enumerate(results, 1):
        print(f"[{i}/{len(results)}] Processing: {analysis.get('organization')} - {analysis.get('title')}")
        
        success, _, _, action = updater.add_report_entry(analysis)
        
        if success:
            stats[action] += 1
            changes_pending = True
            print(f"  -> SUCCESS ({action.upper()})")
        else:
            stats["errors"] += 1
            print(f"  -> FAILED/SKIPPED: {action}")

    # Summary
    print("\n=== Summary ===")
    print(f"Processed: {len(results)} | New: {stats['new']} | Updated: {stats['updated']} | "
          f"Refreshed: {stats['refreshed']} | Errors/Skipped: {stats['errors']}")

    # Save if changes were made
    if changes_pending:
        updater.save()
        
        # Final TOC validation
        print("\n=== Final TOC Validation ===")
        is_valid, issues = updater.validate_and_report_toc()
        if not is_valid:
            print("\nWARNING: TOC validation failed after updates.")
            print("Manual review recommended to ensure all categories are properly defined.")
    else:
        print("No changes required.")

    return 0

if __name__ == "__main__":
    sys.exit(main())