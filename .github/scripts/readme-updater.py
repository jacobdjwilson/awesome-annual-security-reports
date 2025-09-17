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
        """Parse the table of contents from the README.md file"""
        toc_pattern = r'## Contents\n<!-- TOC -->\n(.*?)\n<!-- /TOC -->'
        toc_match = re.search(toc_pattern, self.content, re.DOTALL)
        if not toc_match:
            print("Warning: Could not find TOC section in README.md")
            return {}
        
        toc_content = toc_match.group(1)
        structure: Dict[str, Any] = {}
        current_main_section = None
        
        for line in toc_content.split('\n'):
            line = line.strip()
            if not line:
                continue
            # Main section (e.g., - [Analysis Reports](#analysis-reports))
            if line.startswith('- ') and not line.startswith('    - '):
                match = re.search(r'\[([^\]]+)\]', line)
                if match:
                    section_name = match.group(1)
                    current_main_section = section_name
                    structure[current_main_section] = {'subsections': {}}
            # Subsection (e.g.,     - [Threat Intelligence](#threat-intelligence))
            elif line.startswith('    - ') and current_main_section:
                match = re.search(r'\[([^\]]+)\]', line)
                if match:
                    subsection_name = match.group(1)
                    structure[current_main_section]['subsections'][subsection_name] = {}
        
        print(f"Parsed TOC structure: {list(structure.keys())}")
        for main, data in structure.items():
            print(f"  {main}: {list(data['subsections'].keys())}")
        
        return structure

    def find_section_content(self, heading_name: str) -> Tuple[int, int]:
        """Find the start and end positions of a section's content"""
        # Try exact match first
        pattern = rf'^## {re.escape(heading_name)}$'
        match = re.search(pattern, self.content, re.MULTILINE)
        if not match:
            # Try case-insensitive match
            pattern = rf'^## {re.escape(heading_name)}$'
            match = re.search(pattern, self.content, re.MULTILINE | re.IGNORECASE)
        
        if not match:
            print(f"Could not find section: {heading_name}")
            return -1, -1
        
        start = match.end() + 1  # Start after the heading line
        
        # Find the next ## heading
        next_header = re.search(r'\n## ', self.content[start:])
        end = start + next_header.start() if next_header else len(self.content)
        
        return start, end

class ReadmeUpdater:
    def __init__(self, readme_parser: ReadmeParser):
        self.parser = readme_parser

    def add_report_entry(self, analysis: Dict[str, Any]) -> Tuple[bool, str, int, str]:
        """Add or update a report entry in the README.md file"""
        report_type = analysis.get('type', 'Analysis')
        category = analysis.get('category', 'Industry Trends')
        
        logical_main_section = f"{report_type} Reports"
        logical_subsection = category

        print(f"Looking for main section: '{logical_main_section}'")
        print(f"Looking for subsection: '{logical_subsection}'")
        
        # Check if main section exists
        if logical_main_section not in self.parser.toc_structure:
            available_main = list(self.parser.toc_structure.keys())
            print(f"Main section '{logical_main_section}' not found. Available: {available_main}")
            return False, "", -1, "main_section_not_found"
        
        # Check if subsection exists, if not try to find similar or create it
        available_subsections = list(self.parser.toc_structure[logical_main_section]['subsections'].keys())
        
        if logical_subsection not in available_subsections:
            print(f"Subsection '{logical_subsection}' not found. Available: {available_subsections}")
            
            # Try to find similar subsection
            similar_subsection = self._find_similar_section(logical_subsection, available_subsections)
            if similar_subsection:
                logical_subsection = similar_subsection
                print(f"Using similar subsection: '{similar_subsection}'")
            else:
                # If no similar section found, add to the first available subsection or create new one
                if available_subsections:
                    # Use the most generic subsection available
                    generic_sections = ['Industry Trends', 'Other', 'General']
                    for generic in generic_sections:
                        if generic in available_subsections:
                            logical_subsection = generic
                            print(f"Using generic subsection: '{logical_subsection}'")
                            break
                    else:
                        # Use the first available subsection
                        logical_subsection = available_subsections[0]
                        print(f"Using first available subsection: '{logical_subsection}'")
                else:
                    print(f"No subsections found under '{logical_main_section}'")
                    return False, "", -1, "no_subsections_found"

        # Find section content
        start, end = self.parser.find_section_content(logical_subsection)
        if start == -1:
            print(f"Could not find section content for '{logical_subsection}'")
            return False, "", -1, "section_content_not_found"

        section_content = self.parser.content[start:end]
        entry_text = self._format_entry(analysis)
        
        # Check for existing entries from the same organization
        org_name = analysis['organization']
        existing_line, existing_year = self._find_existing_entry(section_content, org_name)
        
        updated_section = section_content
        entry_action = "new"

        if existing_line and existing_year:
            current_year = int(analysis['year'])
            
            if current_year >= existing_year:
                # Replace the existing entry
                updated_section = section_content.replace(existing_line, entry_text)
                entry_action = "updated" if current_year > existing_year else "refreshed"
                print(f"Replacing existing entry: {existing_line}")
                print(f"With new entry: {entry_text}")
            else:
                print(f"Current year {current_year} is older than existing year {existing_year}, skipping update")
                return False, "", -1, "older_version"
        else:
            # Add as new entry
            updated_section = self._add_new_entry_sorted(section_content, entry_text)
            print(f"Adding new entry: {entry_text}")

        # Update the main content
        self.parser.content = self.parser.content[:start] + updated_section + self.parser.content[end:]
        
        # Find line number of the entry
        inserted_line_number = self._find_line_number(entry_text.strip())

        return True, entry_text, inserted_line_number, entry_action

    def _find_existing_entry(self, section_content: str, org_name: str) -> Tuple[Optional[str], Optional[int]]:
        """Find existing entry for the same organization"""
        lines = section_content.split('\n')
        
        for line in lines:
            if not line.strip().startswith('- ['):
                continue
                
            # Extract organization name from the line
            org_match = re.search(r'^- \[([^\]]+)\]', line.strip())
            if org_match:
                line_org = org_match.group(1)
                if line_org.lower() == org_name.lower():
                    # Extract year from the line
                    year_match = re.search(r'\((\d{4})\)', line)
                    year = int(year_match.group(1)) if year_match else None
                    return line, year
        
        return None, None

    def _add_new_entry_sorted(self, section_content: str, entry_text: str) -> str:
        """Add new entry in alphabetical order"""
        lines = section_content.strip().split('\n')
        entry_lines = [line for line in lines if line.strip() and line.strip().startswith('- [')]
        entry_lines.append(entry_text)
        
        # Sort entries alphabetically by organization name
        entry_lines.sort(key=lambda x: self._extract_org_name_for_sorting(x))
        
        # Reconstruct section with proper spacing
        return '\n'.join(entry_lines) + '\n\n'

    def _find_line_number(self, entry_text: str) -> int:
        """Find the line number where the entry was inserted"""
        for i, line in enumerate(self.parser.content.split('\n')):
            if entry_text in line:
                return i + 1
        return -1

    def _format_entry(self, analysis: Dict[str, Any]) -> str:
        """Format the entry text for the README.md file"""
        org_name = analysis['organization']
        
        # Use organization URL if provided, otherwise generate one
        if 'organization_url' in analysis and analysis['organization_url']:
            org_url = analysis['organization_url']
        else:
            org_url = self._generate_org_url(org_name)
        
        # Construct the PDF path correctly - use relative path for GitHub
        pdf_relative_path = f"Annual Security Reports/{analysis['year']}/{Path(analysis['pdf_path']).name}"
        pdf_url_encoded = pdf_relative_path.replace(' ', '%20')

        return f"- [{org_name}]({org_url}) - [{analysis['title']}]({pdf_url_encoded}) ({analysis['year']}) - {analysis['summary']}"

    def _generate_org_url(self, org_name: str) -> str:
        """Generate organization URL based on name"""
        org_name_lower = org_name.lower()
        
        special_cases = {
            'cyberark': 'https://www.cyberark.com/threat-landscape/',
            'sailpoint': 'https://www.sailpoint.com/horizons',
            'okta': 'https://www.okta.com',
            'crowdstrike': 'https://www.crowdstrike.com',
            'palo alto networks': 'https://www.paloaltonetworks.com',
            'microsoft': 'https://www.microsoft.com',
            'google': 'https://www.google.com',
            'amazon': 'https://aws.amazon.com',
            'ibm': 'https://www.ibm.com',
            'proofpoint': 'https://www.proofpoint.com'
        }
        
        for key, url in special_cases.items():
            if key in org_name_lower:
                return url
        
        # Default URL generation
        domain_base = re.sub(r'\b(company|corp|corporation|inc|llc|ltd|group|security|cyber|tech|technologies)\b', '', org_name.lower())
        domain_base = re.sub(r'[^a-z0-9]', '', domain_base)
        if len(domain_base) < 3:
            domain_base = re.sub(r'[^a-z0-9]', '', org_name.lower())
        
        return f"https://www.{domain_base}.com"

    def _extract_org_name_for_sorting(self, entry_line: str) -> str:
        """Extract organization name for sorting purposes"""
        match = re.search(r'- \[([^\]]+)\]', entry_line)
        return match.group(1).lower() if match else entry_line.lower()

    def _find_similar_section(self, target: str, available_sections: List[str]) -> Optional[str]:
        """Find similar section name using keyword matching"""
        target_words = set(target.lower().split())
        
        best_match = None
        best_score = 0
        
        for section in available_sections:
            section_words = set(section.lower().split())
            # Calculate overlap score
            overlap = len(target_words.intersection(section_words))
            if overlap > best_score:
                best_score = overlap
                best_match = section
        
        return best_match if best_score > 0 else None

    def save_readme(self):
        """Save the updated README.md file"""
        self.parser.readme_path.write_text(self.parser.content, encoding='utf-8')
        print(f"README.md saved to {self.parser.readme_path}")

def main():
    parser = argparse.ArgumentParser(description="Update README.md with security report analysis.")
    parser.add_argument("analysis_json", help="Path to the JSON file with analysis results.")
    parser.add_argument("--readme-path", help="Path to the README.md file.", default="README.md")
    args = parser.parse_args()

    # Check if analysis file exists and has content
    if not os.path.exists(args.analysis_json):
        print(f"ERROR: Analysis file {args.analysis_json} not found")
        sys.exit(1)
    
    # Check file size to ensure it's not empty
    file_size = os.path.getsize(args.analysis_json)
    print(f"Analysis file size: {file_size} bytes")
    
    if file_size < 10:  # Less than 10 bytes is likely just "[]" or empty
        print(f"ERROR: Analysis file {args.analysis_json} is too small ({file_size} bytes) - likely empty or contains no results")
        sys.exit(1)
    
    try:
        with open(args.analysis_json, 'r') as f:
            analysis_results = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in analysis file: {e}")
        sys.exit(1)
    
    if not analysis_results:
        print("ERROR: Analysis file contains no results")
        sys.exit(1)

    print(f"Found {len(analysis_results)} analysis results to process")

    try:
        readme_parser = ReadmeParser(args.readme_path)
        if not readme_parser.toc_structure:
            print("ERROR: Could not parse README.md structure")
            sys.exit(1)
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        sys.exit(1)
        
    updater = ReadmeUpdater(readme_parser)

    processed_entries = []
    summaries = []
    actions_taken = {"new": 0, "updated": 0, "refreshed": 0, "errors": 0, "skipped": 0}
    
    for i, analysis in enumerate(analysis_results, 1):
        print(f"\n=== Processing {i}/{len(analysis_results)} ===")
        print(f"Processing: {analysis.get('organization', 'Unknown')} - {analysis.get('title', 'Unknown')} ({analysis.get('year', 'Unknown')})")
        
        # Validate required fields
        required_fields = ['organization', 'title', 'year', 'summary', 'type', 'category']
        missing_fields = [field for field in required_fields if not analysis.get(field)]
        
        if missing_fields:
            print(f"ERROR: Missing required fields: {missing_fields}")
            actions_taken["errors"] += 1
            summaries.append(f"❌ Error (missing fields): {analysis.get('organization', 'Unknown')} - {missing_fields}")
            continue
        
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
            
            action_icon = "🆕" if action == "new" else "🔄" if action == "updated" else "✅"
            summaries.append(f"{action_icon} {action.capitalize()}: {analysis['organization']} - {analysis['title']} ({analysis['year']}) (Line: {line_number})")
            actions_taken[action] = actions_taken.get(action, 0) + 1
            print(f"SUCCESS: {action} - {analysis['organization']}")
        else:
            if action == "older_version":
                actions_taken["skipped"] += 1
                summaries.append(f"⏭️ Skipped (older version): {analysis['organization']} - {analysis['title']} ({analysis['year']})")
                print(f"SKIPPED: {analysis['organization']} (older version)")
            else:
                actions_taken["errors"] += 1
                summaries.append(f"❌ Error ({action}): {analysis['organization']} - {analysis['title']}")
                print(f"ERROR: {analysis['organization']} - {action}")

    print(f"\n=== README UPDATE SUMMARY ===")
    print(f"Total entries processed: {len(analysis_results)}")
    print(f"Successful updates: {len(processed_entries)}")
    print(f"Actions taken: {actions_taken}")

    if processed_entries:
        updater.save_readme()
        
        # Create detailed summary for PR description
        summary_text = f"Updated README.md with {len(processed_entries)} report entries:\n\n"
        summary_text += f"**Actions taken:**\n"
        for action, count in actions_taken.items():
            if count > 0:
                summary_text += f"- {action.capitalize()}: {count}\n"
        
        summary_text += "\n**Entry details:**\n"
        for entry in processed_entries:
            summary_text += f"- **{entry['action'].capitalize()}**: {entry['organization']} - {entry['title']} ({entry['year']})\n"
            summary_text += f"  - Line {entry['line_number']}: `{entry['entry_text']}`\n\n"
        
        with open("pr_summary.txt", "w") as f:
            f.write(summary_text)
        
        print(f"✅ Successfully processed {len(processed_entries)} entries")
    else:
        print("❌ No entries were processed successfully")

    # Generate GitHub step summary
    summary_path = os.environ.get('GITHUB_STEP_SUMMARY', 'summary.md')
    with open(summary_path, 'w') as f:
        f.write("## ✏️ README Update Summary\n\n")
        if processed_entries:
            f.write(f"Successfully processed {len(processed_entries)} report entries with the following actions:\n\n")
            for action, count in actions_taken.items():
                if count > 0:
                    f.write(f"- **{action.capitalize()}**: {count}\n")
            f.write("\n### Entry Details:\n")
            for summary in summaries:
                f.write(f"{summary}\n")
        else:
            f.write("No updates were made to the README.md.\n")
            if actions_taken["errors"] > 0:
                f.write(f"\n⚠️ {actions_taken['errors']} entries could not be processed due to errors.\n")
            if actions_taken["skipped"] > 0:
                f.write(f"\n⏭️ {actions_taken['skipped']} entries were skipped (older versions).\n")

    return 0 if processed_entries else 1

if __name__ == "__main__":
    sys.exit(main())