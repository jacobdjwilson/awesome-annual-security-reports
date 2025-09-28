import os
import sys
import json
import re
import argparse
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional

class ReadmeParser:
    def __init__(self, readme_path: str):
        self.readme_path = Path(readme_path)
        if not self.readme_path.exists():
            raise FileNotFoundError(f"README.md not found: {readme_path}")
        
        self.content = self.readme_path.read_text(encoding='utf-8')
        self.toc_structure = self._parse_toc()

    def _parse_toc(self) -> Dict[str, Any]:
        """Parse the table of contents - this is where the original parsing failed"""
        # The logs show that Survey Reports exists but has no subsections
        # This means the README structure is likely:
        # ## Survey Reports 
        # ### Industry Trends
        # - [entries]
        
        # Instead of looking for TOC, let's find actual sections in the content
        structure = {"Analysis": {"subsections": {}}, "Survey": {"subsections": {}}}
        
        # Find all ## headings in the content
        section_pattern = r'^## (.+)$'
        sections = re.findall(section_pattern, self.content, re.MULTILINE)
        
        print(f"Found sections in README: {sections}")
        
        # Map sections to structure
        for section in sections:
            if 'Analysis Reports' in section:
                structure["Analysis Reports"] = {"subsections": {}}
            elif 'Survey Reports' in section:
                structure["Survey Reports"] = {"subsections": {}}
            elif section in ['Threat Intelligence', 'Application Security', 'Cloud Security', 'Vulnerabilities', 
                           'Ransomware', 'Data Breaches', 'Physical Security', 'AI and Emerging Technologies']:
                # These are likely analysis subsections
                if "Analysis Reports" not in structure:
                    structure["Analysis Reports"] = {"subsections": {}}
                structure["Analysis Reports"]["subsections"][section] = {}
            elif section in ['Industry Trends', 'Identity Security', 'Penetration Testing', 'Privacy and Data Protection', 'Voice']:
                # These are likely survey subsections  
                if "Survey Reports" not in structure:
                    structure["Survey Reports"] = {"subsections": {}}
                structure["Survey Reports"]["subsections"][section] = {}
        
        # If we didn't find the main report sections, add them
        if "Analysis Reports" not in structure:
            structure["Analysis Reports"] = {"subsections": {"Industry Trends": {}}}
        if "Survey Reports" not in structure:
            structure["Survey Reports"] = {"subsections": {"Industry Trends": {}}}
            
        # Ensure Survey Reports has some basic categories
        if not structure["Survey Reports"]["subsections"]:
            structure["Survey Reports"]["subsections"] = {
                "Industry Trends": {},
                "Voice": {}
            }
        
        print(f"Final parsed structure: {list(structure.keys())}")
        for main, data in structure.items():
            if isinstance(data, dict) and 'subsections' in data:
                print(f"  {main}: {list(data['subsections'].keys())}")
        
        return structure

    def find_section_content(self, heading_name: str) -> Tuple[int, int]:
        """Find the start and end positions of a section's content"""
        pattern = rf'^## {re.escape(heading_name)}$'
        match = re.search(pattern, self.content, re.MULTILINE)
        if not match:
            pattern = rf'^### {re.escape(heading_name)}$'
            match = re.search(pattern, self.content, re.MULTILINE)
        if not match:
            print(f"Could not find section: {heading_name}")
            return -1, -1
        
        start = match.end() + 1
        
        # Find the next header (## or ###)
        next_header = re.search(r'\n##', self.content[start:])
        end = start + next_header.start() if next_header else len(self.content)
        
        return start, end

class ReadmeUpdater:
    def __init__(self, readme_parser: ReadmeParser):
        self.parser = readme_parser

    def add_report_entry(self, analysis: Dict[str, Any]) -> Tuple[bool, str, int, str]:
        """Add or update a report entry with emergency fallback handling"""
        if not self._validate_analysis_data(analysis):
            return False, "", -1, "invalid_data"
        
        report_type = analysis.get('type', 'Analysis')
        category = analysis.get('category', 'Industry Trends')
        
        logical_main_section = f"{report_type} Reports"
        logical_subsection = category

        print(f"Looking for: '{logical_main_section}' -> '{logical_subsection}'")
        
        # EMERGENCY FIX: Try multiple approaches to find where to put the entry
        
        # Approach 1: Try the logical structure
        if logical_main_section in self.parser.toc_structure:
            available_subsections = list(self.parser.toc_structure[logical_main_section].get('subsections', {}).keys())
            
            if logical_subsection in available_subsections:
                return self._add_to_subsection(analysis, logical_subsection)
            
            # Try similar subsection
            similar = self._find_similar_section(logical_subsection, available_subsections)
            if similar:
                print(f"Using similar subsection: {similar}")
                return self._add_to_subsection(analysis, similar)
            
            # Use first available subsection
            if available_subsections:
                fallback_section = available_subsections[0]
                print(f"Using fallback subsection: {fallback_section}")
                return self._add_to_subsection(analysis, fallback_section)
        
        # Approach 2: Try direct section lookup (e.g., ## Industry Trends)
        direct_result = self._try_direct_section(analysis, logical_subsection)
        if direct_result[0]:  # Success
            return direct_result
            
        # Approach 3: Try common fallback sections
        fallback_sections = ['Industry Trends', 'Other', 'General']
        for section in fallback_sections:
            result = self._try_direct_section(analysis, section)
            if result[0]:  # Success
                print(f"Used fallback section: {section}")
                return result
        
        # Approach 4: Add to the end of the file as last resort
        print("Using emergency fallback: adding to end of file")
        return self._add_to_end_of_file(analysis)

    def _add_to_subsection(self, analysis: Dict[str, Any], subsection: str) -> Tuple[bool, str, int, str]:
        """Add entry to a specific subsection"""
        start, end = self.parser.find_section_content(subsection)
        if start == -1:
            return False, "", -1, "section_not_found"
        
        section_content = self.parser.content[start:end]
        entry_text = self._format_entry(analysis)
        
        # Check for existing entries
        org_name = analysis['organization']
        report_title = analysis['title']
        existing_line, existing_year = self._find_existing_entry(section_content, org_name, report_title)
        
        if existing_line and existing_year:
            try:
                current_year = int(analysis['year'])
                if current_year >= existing_year:
                    updated_section = section_content.replace(existing_line, entry_text)
                    entry_action = "updated" if current_year > existing_year else "refreshed"
                else:
                    return False, "", -1, "older_version"
            except (ValueError, TypeError):
                return False, "", -1, "invalid_year"
        else:
            updated_section = self._add_new_entry_sorted(section_content, entry_text)
            entry_action = "new"
        
        # Update content
        self.parser.content = self.parser.content[:start] + updated_section + self.parser.content[end:]
        line_number = self._find_line_number(entry_text.strip())
        
        return True, entry_text, line_number, entry_action

    def _try_direct_section(self, analysis: Dict[str, Any], section_name: str) -> Tuple[bool, str, int, str]:
        """Try to add to a section directly (e.g., ## Industry Trends)"""
        start, end = self.parser.find_section_content(section_name)
        if start == -1:
            return False, "", -1, "section_not_found"
        
        return self._add_to_subsection(analysis, section_name)

    def _add_to_end_of_file(self, analysis: Dict[str, Any]) -> Tuple[bool, str, int, str]:
        """Emergency fallback: add entry to end of file"""
        entry_text = self._format_entry(analysis)
        
        # Find a good place to insert - after last content but before any final sections
        insert_point = len(self.parser.content.rstrip())
        
        # Add a new section if needed
        new_content = f"\n\n## Emergency Entries\n\n{entry_text}\n"
        
        self.parser.content = self.parser.content[:insert_point] + new_content
        line_number = self._find_line_number(entry_text.strip())
        
        return True, entry_text, line_number, "new"

    def _validate_analysis_data(self, analysis: Dict[str, Any]) -> bool:
        """Validate analysis data with better error reporting"""
        required_fields = ['organization', 'title', 'year', 'summary', 'type', 'category', 'pdf_path']
        missing_fields = []
        
        for field in required_fields:
            value = analysis.get(field)
            if not value or (isinstance(value, str) and not value.strip()):
                missing_fields.append(field)
        
        if missing_fields:
            print(f"ERROR: Missing required fields: {missing_fields}")
            return False
        
        # Check for the filename parsing bug
        org = analysis.get('organization', '')
        title = analysis.get('title', '')
        
        if org == title and '-' in org:
            print(f"ERROR: Detected filename parsing bug - org and title are identical: '{org}'")
            return False
            
        # Validate year
        year_str = str(analysis.get('year', ''))
        if not year_str.isdigit() or len(year_str) != 4:
            print(f"ERROR: Invalid year: '{year_str}'")
            return False
        
        return True

    def _find_existing_entry(self, section_content: str, org_name: str, report_title: str) -> Tuple[Optional[str], Optional[int]]:
        """Find existing entry for a specific report from an organization."""
        lines = section_content.split('\n')
        org_name_lower = org_name.lower()
        # Normalize title for comparison: lower, remove "the", "of", "and", and spaces
        title_norm = re.sub(r'\s+|the|of|and', '', report_title.lower())
        
        for line in lines:
            if not line.strip().startswith('- ['):
                continue
                
            # Match organization and title from the markdown link format
            entry_match = re.search(r'^- \[([^\]]+)\]\(.*\) - \[([^\]]+)\]\(.*\)', line.strip())
            if entry_match:
                line_org = entry_match.group(1)
                line_title = entry_match.group(2)
                line_title_norm = re.sub(r'\s+|the|of|and', '', line_title.lower())
                
                if line_org.lower() == org_name_lower and line_title_norm == title_norm:
                    year_match = re.search(r'\((\d{4})\)', line)
                    year = int(year_match.group(1)) if year_match else None
                    return line, year
        
        return None, None

    def _add_new_entry_sorted(self, section_content: str, entry_text: str) -> str:
        """Add new entry in alphabetical order"""
        lines = section_content.strip().split('\n')
        entry_lines = [line for line in lines if line.strip() and line.strip().startswith('- [')]
        entry_lines.append(entry_text)
        
        # Sort by organization name
        entry_lines.sort(key=lambda x: self._extract_org_name_for_sorting(x))
        
        return '\n'.join(entry_lines) + '\n'

    def _find_line_number(self, entry_text: str) -> int:
        """Find line number of entry"""
        for i, line in enumerate(self.parser.content.split('\n'), 1):
            if entry_text in line:
                return i
        return -1

    def _format_entry(self, analysis: Dict[str, Any]) -> str:
        """Format entry for README"""
        org_name = analysis['organization']
        org_url = analysis['organization_url'] # This is now a required field from the analyzer
        
        filename = Path(analysis['pdf_path']).name
        year = analysis['year']
        pdf_relative_path = f"Annual Security Reports/{year}/{filename}"
        pdf_url_encoded = pdf_relative_path.replace(' ', '%20')

        return f"- [{org_name}]({org_url}) - [{analysis['title']}]({pdf_url_encoded}) ({year}) - {analysis['summary']}"

    def _extract_org_name_for_sorting(self, entry_line: str) -> str:
        """Extract org name for sorting"""
        match = re.search(r'- \[([^\]]+)\]', entry_line)
        return match.group(1).lower() if match else entry_line.lower()

    def _find_similar_section(self, target: str, available_sections: List[str]) -> Optional[str]:
        """Find similar section name"""
        target_words = set(target.lower().split())
        
        best_match = None
        best_score = 0
        
        for section in available_sections:
            section_words = set(section.lower().split())
            overlap = len(target_words.intersection(section_words))
            if overlap > best_score:
                best_score = overlap
                best_match = section
        
        return best_match if best_score > 0 else None

    def save_readme(self):
        """Save updated README"""
        self.parser.readme_path.write_text(self.parser.content, encoding='utf-8')
        print(f"README updated: {self.parser.readme_path}")

def main():
    parser = argparse.ArgumentParser(description="Update README with security reports")
    parser.add_argument("analysis_json", help="Analysis results JSON file")
    parser.add_argument("--readme-path", default="README.md", help="README path")
    args = parser.parse_args()

    if not os.path.exists(args.analysis_json):
        print(f"ERROR: Analysis file not found: {args.analysis_json}")
        sys.exit(1)
    
    file_size = os.path.getsize(args.analysis_json)
    print(f"Analysis file size: {file_size} bytes")
    
    if file_size < 10:
        print(f"ERROR: Analysis file too small ({file_size} bytes)")
        sys.exit(1)
    
    try:
        with open(args.analysis_json, 'r') as f:
            analysis_results = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON: {e}")
        sys.exit(1)
    
    if not analysis_results:
        print("ERROR: No analysis results")
        sys.exit(1)

    print(f"Processing {len(analysis_results)} analysis results")
    
    # Debug the first result
    if analysis_results:
        first = analysis_results[0]
        print(f"First result: {first.get('organization')} - {first.get('title')} ({first.get('year')})")

    try:
        readme_parser = ReadmeParser(args.readme_path)
        updater = ReadmeUpdater(readme_parser)
    except Exception as e:
        print(f"ERROR: Failed to initialize README parser: {e}")
        sys.exit(1)

    processed_entries = []
    actions_taken = {"new": 0, "updated": 0, "refreshed": 0, "errors": 0, "skipped": 0}
    
    for i, analysis in enumerate(analysis_results, 1):
        print(f"\n=== Processing {i}/{len(analysis_results)} ===")
        
        success, entry_text, line_number, action = updater.add_report_entry(analysis)
        
        if success:
            processed_entries.append({
                'organization': analysis['organization'],
                'title': analysis['title'],
                'year': analysis['year'],
                'entry_text': entry_text,
                'line_number': line_number,
                'action': action
            })
            actions_taken[action] += 1
            print(f"SUCCESS: {action.upper()} - {analysis['organization']}")
        else:
            actions_taken["errors"] += 1
            print(f"FAILED: {analysis['organization']} - {action}")

    print(f"\n=== SUMMARY ===")
    print(f"Processed: {len(analysis_results)}")
    print(f"Successful: {len(processed_entries)}")
    print(f"Actions: {actions_taken}")

    if processed_entries:
        updater.save_readme()
        print("SUCCESS: README updated")
    else:
        print("ERROR: No successful updates")

    return 0 if processed_entries else 1

if __name__ == "__main__":
    sys.exit(main())