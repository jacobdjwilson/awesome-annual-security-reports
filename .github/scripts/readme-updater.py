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
        self.content = self.readme_path.read_text(encoding='utf-8')
        self.toc_structure = self._parse_toc()

    def _parse_toc(self) -> Dict[str, Any]:
        toc_pattern = r'## Contents\n<!-- TOC -->\n(.*?)\n<!-- /TOC -->'
        toc_match = re.search(toc_pattern, self.content, re.DOTALL)
        if not toc_match:
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
        return structure

    def find_section_content(self, heading_name: str) -> Tuple[int, int]:
        pattern = rf'## {re.escape(heading_name)}\n'
        match = re.search(pattern, self.content)
        if not match:
            return -1, -1
        
        start = match.end()
        next_header = re.search(r'\n## ', self.content[start:])
        end = start + next_header.start() if next_header else len(self.content)
        return start, end

class ReadmeUpdater:
    def __init__(self, readme_parser: ReadmeParser):
        self.parser = readme_parser

    def add_report_entry(self, analysis: Dict[str, Any]) -> Tuple[bool, str, int, str]:
        logical_main_section = f"{analysis['type']} Reports"
        logical_subsection = analysis['category']

        if logical_main_section not in self.parser.toc_structure:
            return False, "", -1, "error"
        
        if logical_subsection not in self.parser.toc_structure[logical_main_section]['subsections']:
            similar_subsection = self._find_similar_section(logical_subsection, logical_main_section)
            if similar_subsection:
                logical_subsection = similar_subsection
            else:
                return False, "", -1, "error"

        start, end = self.parser.find_section_content(logical_subsection)
        if start == -1:
            return False, "", -1, "error"

        section_content = self.parser.content[start:end]
        entry_text = self._format_entry(analysis)
        
        # More flexible matching patterns
        org_name = analysis['organization']
        report_title_words = analysis['title'].split()
        
        # Try different matching patterns
        patterns_to_try = [
            # Exact organization and title match
            rf"^- \[{re.escape(org_name)}\]\([^)]+\) - \[.*{re.escape(analysis['title'])}.*\]\([^)]+\) \((\d{{4}})\)",
            # Organization match with partial title match
            rf"^- \[{re.escape(org_name)}\]\([^)]+\) - \[.*{re.escape(' '.join(report_title_words[:3]))}.*\]\([^)]+\) \((\d{{4}})\)",
            # Fuzzy organization match (handle variations like "CyberArk" vs "Cyberark")
            rf"^- \[{re.escape(org_name.lower())}\]\([^)]+\) - \[.*\]\([^)]+\) \((\d{{4}})\)",
            # Match by key title words
            rf"^- \[[^\]]+\]\([^)]+\) - \[.*(?:{'|'.join(report_title_words[:2])}).*\]\([^)]+\) \((\d{{4}})\)"
        ]
        
        existing_match = None
        for pattern in patterns_to_try:
            existing_match = re.search(pattern, section_content, re.MULTILINE | re.IGNORECASE)
            if existing_match:
                break

        updated_section = section_content
        entry_action = "new"

        if existing_match:
            existing_year = int(existing_match.group(1))
            current_year = int(analysis['year'])
            if current_year >= existing_year:
                # Replace the existing entry
                updated_section = re.sub(patterns_to_try[0], entry_text, section_content, 1, re.MULTILINE | re.IGNORECASE)
                # If first pattern didn't work, try the others
                if updated_section == section_content:
                    for pattern in patterns_to_try[1:]:
                        updated_section = re.sub(pattern, entry_text, section_content, 1, re.MULTILINE | re.IGNORECASE)
                        if updated_section != section_content:
                            break
                entry_action = "updated" if current_year > existing_year else "refreshed"
            else:
                return False, "", -1, "older_version"
        
        # If no existing match found or replacement didn't work, add as new entry
        if updated_section == section_content and not existing_match:
            lines = updated_section.strip().split('\n')
            # Filter out empty lines and get only entry lines
            entry_lines = [line for line in lines if line.strip() and line.strip().startswith('- [')]
            entry_lines.append(entry_text)
            # Sort entries alphabetically by organization name, then by title
            entry_lines.sort(key=lambda x: (self._extract_org_name_for_sorting(x), self._extract_report_title_for_sorting(x)))
            
            # Reconstruct section with proper spacing
            updated_section = '\n'.join(entry_lines) + '\n\n'

        self.parser.content = self.parser.content[:start] + updated_section + self.parser.content[end:]
        
        # Find line number of the entry
        inserted_line_number = -1
        for i, line in enumerate(self.parser.content.split('\n')):
            if entry_text.strip() in line:
                inserted_line_number = i + 1
                break

        return True, entry_text, inserted_line_number, entry_action

    def _format_entry(self, analysis: Dict[str, Any]) -> str:
        org_name = analysis['organization']
        
        # Generate organization URL more intelligently
        org_url = self._generate_org_url(org_name)
        
        # Use the correct file path structure
        pdf_path = Path("Annual Security Reports") / analysis['year'] / f"{Path(analysis['file_path']).stem}.pdf"
        pdf_path_encoded = str(pdf_path).replace(' ', '%20')

        return f"- [{org_name}]({org_url}) - [{analysis['title']}]({pdf_path_encoded}) ({analysis['year']}) - {analysis['summary']}"

    def _generate_org_url(self, org_name: str) -> str:
        # Handle special cases first
        org_name_lower = org_name.lower()
        
        special_cases = {
            'cyberark': 'https://cyberark.com',
            'sailpoint': 'https://sailpoint.com',
            'okta': 'https://okta.com',
            'crowdstrike': 'https://crowdstrike.com',
            'palo alto networks': 'https://paloaltonetworks.com',
            'microsoft': 'https://microsoft.com',
            'google': 'https://google.com',
            'amazon': 'https://aws.amazon.com',
            'ibm': 'https://ibm.com'
        }
        
        for key, url in special_cases.items():
            if key in org_name_lower:
                return url
        
        # Default URL generation
        domain_base = re.sub(r'\b(company|corp|corporation|inc|llc|ltd|group|security|cyber|tech|technologies)\b', '', org_name.lower())
        domain_base = re.sub(r'[^a-z0-9]', '', domain_base)
        if len(domain_base) < 3:
            domain_base = re.sub(r'[^a-z0-9]', '', org_name.lower())
        
        return f"https://{domain_base}.com"

    def _extract_org_name_for_sorting(self, entry_line: str) -> str:
        match = re.search(r'- \[([^\]]+)\]', entry_line)
        return match.group(1).lower() if match else entry_line

    def _extract_report_title_for_sorting(self, entry_line: str) -> str:
        match = re.search(r'\]\([^)]+\) - \[([^\]]+)\]', entry_line)
        return match.group(1).lower() if match else entry_line

    def _find_similar_section(self, target: str, main_section: str) -> Optional[str]:
        available_sections = list(self.parser.toc_structure[main_section]['subsections'].keys())
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
        self.parser.readme_path.write_text(self.parser.content, encoding='utf-8')

def main():
    parser = argparse.ArgumentParser(description="Update README.md with security report analysis.")
    parser.add_argument("analysis_json", help="Path to the JSON file with analysis results.")
    parser.add_argument("--readme-path", help="Path to the README.md file.", default="README.md")
    args = parser.parse_args()

    readme_parser = ReadmeParser(args.readme_path)
    updater = ReadmeUpdater(readme_parser)

    with open(args.analysis_json, 'r') as f:
        analysis_results = json.load(f)

    processed_files = []
    summaries = []
    actions_taken = {"new": 0, "updated": 0, "refreshed": 0, "errors": 0}
    
    for analysis in analysis_results:
        success, entry_text, line_number, action = updater.add_report_entry(analysis)
        if success:
            processed_files.append(analysis['file_path'])
            action_icon = "🆕" if action == "new" else "🔄" if action == "updated" else "✅"
            summaries.append(f"{action_icon} {action.capitalize()}: {analysis['organization']} - {analysis['title']} ({analysis['year']}) (Line: {line_number})")
            actions_taken[action] = actions_taken.get(action, 0) + 1
        else:
            actions_taken["errors"] += 1
            summaries.append(f"❌ Error: {analysis['organization']} - {analysis['title']} ({action})")

    if processed_files:
        updater.save_readme()
        
        # Create detailed summary
        summary_text = f"Updated README.md with {len(processed_files)} reports:\n\n"
        summary_text += f"Actions taken:\n"
        for action, count in actions_taken.items():
            if count > 0:
                summary_text += f"- {action.capitalize()}: {count}\n"
        summary_text += "\nDetails:\n" + "\n".join(summaries)
        
        with open("pr_summary.txt", "w") as f:
            f.write(summary_text)

    # Generate GitHub step summary
    summary_path = os.environ.get('GITHUB_STEP_SUMMARY', 'summary.md')
    with open(summary_path, 'w') as f:
        f.write("\n## ✏️ README Update Summary\n\n")
        if processed_files:
            f.write(f"Successfully processed {len(processed_files)} reports with the following actions:\n\n")
            for action, count in actions_taken.items():
                if count > 0:
                    f.write(f"- **{action.capitalize()}**: {count}\n")
            f.write("\n### Details:\n")
            for summary in summaries:
                f.write(f"{summary}\n")
        else:
            f.write("No updates were made to the README.md.\n")
            if actions_taken["errors"] > 0:
                f.write(f"\n⚠️ {actions_taken['errors']} entries could not be processed due to errors.\n")

if __name__ == "__main__":
    main()