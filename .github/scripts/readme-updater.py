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
        self.structure = self._parse_structure()

    def _parse_structure(self) -> Dict[str, Any]:
        """Parses the README structure to identify main report sections."""
        structure = {
            "Analysis Reports": {"subsections": {}}, 
            "Survey Reports": {"subsections": {}}
        }
        
        # Regex to identify Level 2 headers (##)
        sections = re.findall(r'^## (.+)$', self.content, re.MULTILINE)
        
        for section in sections:
            # Main Section Detection
            if 'Analysis Reports' in section:
                pass # Already initialized
            elif 'Survey Reports' in section:
                pass # Already initialized
            
            # Sub-section Mapping (Inferred based on known categories)
            elif section in ['Threat Intelligence', 'Application Security', 'Cloud Security', 'Vulnerabilities', 
                           'Ransomware', 'Data Breaches', 'Physical Security', 'AI and Emerging Technologies']:
                structure["Analysis Reports"]["subsections"][section] = {}
            
            elif section in ['Industry Trends', 'Identity Security', 'Penetration Testing', 'Privacy and Data Protection', 'Voice']:
                structure["Survey Reports"]["subsections"][section] = {}

        # Default Fallbacks if specific sections are missing
        if not structure["Analysis Reports"]["subsections"]:
            structure["Analysis Reports"]["subsections"]["Industry Trends"] = {}
        if not structure["Survey Reports"]["subsections"]:
            structure["Survey Reports"]["subsections"] = {"Industry Trends": {}, "Voice": {}}
            
        return structure

    def find_section_bounds(self, heading_name: str) -> Tuple[int, int]:
        """Finds start and end indices of a specific section content."""
        # Try Level 2 (##) then Level 3 (###)
        for pattern in [rf'^## {re.escape(heading_name)}$', rf'^### {re.escape(heading_name)}$']:
            match = re.search(pattern, self.content, re.MULTILINE)
            if match:
                start = match.end() + 1
                # Find next header to determine end
                next_header = re.search(r'\n##', self.content[start:])
                end = start + next_header.start() if next_header else len(self.content)
                return start, end
        
        return -1, -1

class ReadmeUpdater:
    def __init__(self, parser: ReadmeParser):
        self.parser = parser

    def add_report_entry(self, analysis: Dict[str, Any]) -> Tuple[bool, str, int, str]:
        """Orchestrates adding a report entry using a prioritized strategy."""
        if not self._validate_data(analysis):
            return False, "", -1, "invalid_data"
        
        report_type = analysis.get('type', 'Analysis')
        category = analysis.get('category', 'Industry Trends')
        
        main_section = f"{report_type} Reports"
        
        # Strategy 1: Logical Subsection Match
        if main_section in self.parser.structure:
            subsections = list(self.parser.structure[main_section]['subsections'].keys())
            
            # Exact match
            if category in subsections:
                return self._insert_into_section(analysis, category)
            
            # Fuzzy/Similar match
            similar = self._find_similar_section(category, subsections)
            if similar:
                return self._insert_into_section(analysis, similar)
            
            # First available fallback
            if subsections:
                return self._insert_into_section(analysis, subsections[0])
        
        # Strategy 2: Direct Section Lookup
        if self._insert_into_section(analysis, category)[0]:
            return self._insert_into_section(analysis, category)

        # Strategy 3: Generic Fallbacks
        for fallback in ['Industry Trends', 'Other', 'General']:
            res = self._insert_into_section(analysis, fallback)
            if res[0]: return res
        
        # Strategy 4: Append to End (Last Resort)
        return self._append_to_file(analysis)

    def _insert_into_section(self, analysis: Dict[str, Any], section_name: str) -> Tuple[bool, str, int, str]:
        """Inserts or updates an entry within a specific section."""
        start, end = self.parser.find_section_bounds(section_name)
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

    def _append_to_file(self, analysis: Dict[str, Any]) -> Tuple[bool, str, int, str]:
        """Appends entry to the end of the file as a fallback."""
        entry_text = self._format_entry(analysis)
        new_content = f"\n\n## Emergency Entries\n\n{entry_text}\n"
        self.parser.content = self.parser.content.rstrip() + new_content
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
        2. Organization URL match (handles rebranding like WEF vs World Economic Forum).
        3. PDF Filename match (handles series updates).
        """
        org_norm = analysis['organization'].lower()
        title_norm = self._normalize_title(analysis['title'])
        target_url = analysis['organization_url'].lower().rstrip('/')
        target_pdf = Path(analysis['pdf_path']).name.lower()

        # Remove year from PDF filename for generic series matching (e.g., Report-2025.pdf -> Report)
        target_pdf_base = re.sub(r'\d{4}', '', target_pdf).strip('-_ ')

        for line in content.split('\n'):
            if not line.strip().startswith('- ['): continue
            
            # Extract Components: - [Org](OrgURL) - [Title](PdfURL) (Year)
            match = re.search(r'^- \[([^\]]+)\]\(([^\)]+)\) - \[([^\]]+)\]\(([^\)]+)\)\s*\((\d{4})\)', line.strip())
            if match:
                curr_org = match.group(1).lower()
                curr_org_url = match.group(2).lower().rstrip('/')
                curr_title = self._normalize_title(match.group(3))
                curr_pdf_url = match.group(4).lower()
                curr_year = int(match.group(5))

                # Check 1: URL Match (Strongest signal for same organization)
                if target_url == curr_org_url:
                    return line, curr_year

                # Check 2: PDF Filename Match (Strong signal for report series)
                curr_pdf_name = Path(curr_pdf_url).name
                curr_pdf_base = re.sub(r'\d{4}', '', curr_pdf_name).strip('-_ ')
                if target_pdf_base == curr_pdf_base and target_pdf_base != "":
                    return line, curr_year

                # Check 3: Org and Title Match (Original Logic)
                if curr_org == org_norm and curr_title == title_norm:
                    return line, curr_year

        return None, None

    def _normalize_title(self, title: str) -> str:
        return re.sub(r'\s+|the|of|and', '', title.lower())

    def _find_similar_section(self, target: str, options: List[str]) -> Optional[str]:
        target_set = set(target.lower().split())
        best_match, best_score = None, 0
        
        for opt in options:
            score = len(target_set.intersection(set(opt.lower().split())))
            if score > best_score:
                best_match, best_score = opt, score
        return best_match

    def _find_line_number(self, text: str) -> int:
        for i, line in enumerate(self.parser.content.split('\n'), 1):
            if text in line: return i
        return -1

    def _validate_data(self, data: Dict[str, Any]) -> bool:
        required = ['organization', 'title', 'year', 'summary', 'type', 'category', 'pdf_path', 'organization_url']
        if any(not data.get(f) for f in required):
            print(f"ERROR: Missing fields in analysis: {[f for f in required if not data.get(f)]}")
            return False
        return str(data.get('year', '')).isdigit()

    def save(self):
        self.parser.readme_path.write_text(self.parser.content, encoding='utf-8')
        print(f"README successfully updated: {self.parser.readme_path}")

def main():
    parser = argparse.ArgumentParser(description="Update README with security reports")
    parser.add_argument("analysis_json", help="Path to analysis results JSON")
    parser.add_argument("--readme-path", default="README.md", help="Path to README.md")
    args = parser.parse_args()

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
    
    try:
        updater = ReadmeUpdater(ReadmeParser(args.readme_path))
    except Exception as e:
        print(f"ERROR: Parser init failed: {e}")
        sys.exit(1)

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
            print(f"  -> FAILED: {action}")

    print("\n=== Summary ===")
    print(f"Processed: {len(results)} | New: {stats['new']} | Updated: {stats['updated']} | Errors: {stats['errors']}")

    if changes_pending:
        updater.save()
    else:
        print("No changes required.")

    return 0

if __name__ == "__main__":
    sys.exit(main())