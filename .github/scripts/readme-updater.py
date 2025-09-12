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
            if line.startswith('- ') and not line.startswith('    - '):
                match = re.search(r'\[([^\]]+)\]', line)
                if match:
                    current_main_section = match.group(1)
                    structure[current_main_section] = {'subsections': {}}
            elif line.startswith('- ') and current_main_section:
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

    def add_report_entry(self, analysis: Dict[str, Any]) -> Tuple[bool, str, int]:
        logical_main_section = f"{analysis['type']} Reports"
        logical_subsection = analysis['category']

        if logical_main_section not in self.parser.toc_structure:
            return False, "", -1
        
        if logical_subsection not in self.parser.toc_structure[logical_main_section]['subsections']:
            similar_subsection = self._find_similar_section(logical_subsection, logical_main_section)
            if similar_subsection:
                logical_subsection = similar_subsection
            else:
                return False, "", -1

        start, end = self.parser.find_section_content(logical_subsection)
        if start == -1:
            return False, "", -1

        section_content = self.parser.content[start:end]
        entry_text = self._format_entry(analysis)
        
        org_pattern = re.escape(analysis['organization'])
        title_pattern = re.escape(analysis['title'])
        existing_entry_pattern = rf"^- \[{{{org_pattern}}}\]\([^)]+\) - \[{{{title_pattern}}}\]\([^)]+\) ((\d{{4}}))"

        existing_match = re.search(existing_entry_pattern, section_content, re.MULTILINE)
        
        updated_section = section_content
        entry_replaced = False

        if existing_match:
            existing_year = int(existing_match.group(1))
            if int(analysis['year']) > existing_year:
                updated_section = re.sub(existing_entry_pattern, entry_text, section_content, 1, re.MULTILINE)
                entry_replaced = True
            else:
                return False, "", -1 # No update needed
        
        if not entry_replaced:
            lines = updated_section.strip().split('\n')
            entries = [line for line in lines if line.strip().startswith('- [')] + [entry_text]
            entries.sort(key=lambda x: (self._extract_org_name_for_sorting(x), self._extract_report_title_for_sorting(x)))
            updated_section = '\n'.join(entries) + '\n'

        self.parser.content = self.parser.content[:start] + updated_section + self.parser.content[end:]
        
        inserted_line_number = -1
        for i, line in enumerate(self.parser.content.split('\n')):
            if entry_text in line:
                inserted_line_number = i + 1
                break

        return True, entry_text, inserted_line_number

    def _format_entry(self, analysis: Dict[str, Any]) -> str:
        org_name = analysis['organization']
        domain_base = re.sub(r'\b(company|corp|corporation|inc|llc|ltd|group|security|cyber|tech|technologies)\b', '', org_name.lower())
        domain_base = re.sub(r'[^a-z0-9]', '', domain_base)
        if len(domain_base) < 3:
            domain_base = re.sub(r'[^a-z0-9]', '', org_name.lower())
        org_url = f"https://{domain_base}.com"
        
        pdf_path = Path("Annual Security Reports") / analysis['year'] / f"{Path(analysis['file_path']).stem}.pdf"
        pdf_path_encoded = str(pdf_path).replace(' ', '%20')

        return f"- [{org_name}]({org_url}) - [{analysis['title']}]({pdf_path_encoded}) ({analysis['year']}) - {analysis['summary']}"

    def _extract_org_name_for_sorting(self, entry_line: str) -> str:
        match = re.search(r'- \[([^\\]+)\]', entry_line)
        return match.group(1).lower() if match else entry_line

    def _extract_report_title_for_sorting(self, entry_line: str) -> str:
        match = re.search(r'\]\(.*?)\) - \[([^\\]+)\]', entry_line)
        return match.group(1).lower() if match else entry_line

    def _find_similar_section(self, target: str, main_section: str) -> Optional[str]:
        available_sections = list(self.parser.toc_structure[main_section]['subsections'].keys())
        for section in available_sections:
            if any(word in section.lower() for word in target.lower().split()):
                return section
        return None

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
    for analysis in analysis_results:
        success, entry_text, line_number = updater.add_report_entry(analysis)
        if success:
            processed_files.append(analysis['file_path'])
            summaries.append(f"✅ Added/Updated: {entry_text} (Line: {line_number})")

    if processed_files:
        updater.save_readme()
        with open("pr_summary.txt", "w") as f:
            f.write(f"Updated README.md with {len(processed_files)} reports:\n\n" + "\n".join(summaries))

    summary_path = os.environ.get('GITHUB_STEP_SUMMARY', 'summary.md')
    with open(summary_path, 'w') as f:
        f.write("\n## ✍️ README Update Summary\n\n")
        if processed_files:
            f.write(f"Successfully updated README.md with {len(processed_files)} reports.\n")
            f.write("\n".join(summaries))
        else:
            f.write("No updates were made to the README.md.\n")

if __name__ == "__main__":
    main()
