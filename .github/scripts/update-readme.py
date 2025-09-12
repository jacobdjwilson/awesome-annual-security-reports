import os
import sys
import json
import yaml
import re
import glob
from pathlib import Path
from datetime import datetime
import google.generativeai as genai
import requests
import time
from typing import List, Dict, Optional, Tuple

class ReadmeParser:
    def __init__(self, readme_path: str):
        self.readme_path = readme_path
        self.content = self._read_readme()
        self.toc_structure = self._parse_toc()
        
    def _read_readme(self) -> str:
        try:
            with open(self.readme_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"❌ README not found at {self.readme_path}")
            return ""
        
    def _parse_toc(self) -> Dict:
        """Parse Table of Contents structure dynamically"""
        toc_pattern = r'## Contents\n<!-- TOC -->\n(.*?)\n<!-- /TOC -->'
        toc_match = re.search(toc_pattern, self.content, re.DOTALL)
        
        if not toc_match:
            print("⚠️ No Table of Contents found within <!-- TOC --> markers")
            return {}
        
        toc_content = toc_match.group(1)
        structure = {}
        current_main_section = None
        
        lines = toc_content.split('\n')
        
        for line in lines:
            if not line.strip():
                continue
                
            if line.startswith('- ') and not line.startswith('    - '):
                stripped_line = line.strip()
                match = re.search(r'\[([^\]]+)\]', stripped_line)
                if match:
                    section_name = match.group(1)
                    current_main_section = section_name
                    structure[current_main_section] = {'subsections': {}}
                
            elif line.startswith('    - ') and current_main_section:
                stripped_line = line.strip()
                match = re.search(r'\[([^\]]+)\]', stripped_line)
                if match:
                    subsection_name = match.group(1)
                    structure[current_main_section]['subsections'][subsection_name] = {}
        
        return structure
        
    def find_section_content(self, heading_name: str) -> Tuple[int, int]:
        """Find the start and end positions of a heading in the README"""
        pattern = rf'## {re.escape(heading_name)}\n'
        match = re.search(pattern, self.content)
        if not match:
            return -1, -1
        
        start = match.end()
        
        next_header = re.search(r'\n## ', self.content[start:])
        if next_header:
            end = start + next_header.start()
        else:
            end = len(self.content)
        
        return start, end

class ReportAnalyzer:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.models = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash"]
        self.current_model = None
        self._setup_ai()
        
        self.acronyms = ["AI", "IT", "API", "ML", "IoT", "GRC", "IAM", "SSO", "MFA", "AWS", "GCP", "VPN", "IDS", "IPS", "DDoS", "DLP", "MDM", "SOC", "SIEM", "monitoring", "detection", "response", "incident"]

        self.categories = [
            'Identity and Access Management',
            'Cloud Security',
            'Application Security',
            'Ransomware and Malware',
            'Compliance and Governance',
            'Network Security',
            'Data Security',
            'Endpoint Security',
            'Security Operations',
            'Emerging Technologies',
            'Vulnerabilities',
            'Penetration Testing',
            'Industry Trends'
        ]
        
    def _setup_ai(self):
        """Setup AI with fallback models"""
        if not self.api_key:
            print("⚠️ No Gemini API key provided")
            return
            
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        
        for model_name in self.models:
            try:
                model = genai.GenerativeModel(model_name)
                response = model.generate_content("Hello")
                if response.text:
                    self.current_model = model
                    print(f"✅ Using AI model: {model_name}")
                    break
            except Exception as e:
                print(f"❌ Failed to initialize {model_name}: {e}")
                continue
        
        if not self.current_model:
            print("⚠️ No AI models available")
            
    def extract_info_from_path(self, file_path: str) -> Tuple[str, str, str]:
        """Extract organization name, year, and report title from file path"""
        path_parts = Path(file_path).parts
        
        year = "Unknown"
        for part in path_parts:
            if part.isdigit() and len(part) == 4:
                year = part
                break
        
        filename = Path(file_path).stem
        name_parts = filename.split('-')
        org_name = name_parts[0].strip()
        
        # The last part is the year, so the report title is everything in between
        year_part = name_parts[-1]
        if year_part.isdigit() and len(year_part) == 4:
            title_parts = name_parts[1:-1]
            report_title = ' '.join(title_parts).strip()
        else:
            title_parts = name_parts[1:]
            report_title = ' '.join(title_parts).strip()
        
        org_name = org_name.replace('_', ' ').replace('-', ' ')
        org_name = ' '.join(word.capitalize() for word in org_name.split())
        
        report_title = report_title.replace('_', ' ').replace('-', ' ')
        
        processed_title_words = []
        for word in report_title.split():
            if word.upper() in self.acronyms:
                processed_title_words.append(word.upper())
            else:
                processed_title_words.append(word.capitalize())
        
        report_title = ' '.join(processed_title_words)
        
        return org_name, year, report_title
        
    def analyze_content(self, content: str, org_name: str, year: str, report_title: str, organization_url: Optional[str] = None) -> Dict:
        """Analyze content using AI with retry logic"""
        if not self.current_model:
            return self._fallback_analysis(content, org_name, year, report_title, organization_url)
        
        prompt_path = ".github/ai-prompts/markdown-summarization-prompt.md"
        base_prompt = "Analyze this security report and provide a concise summary focusing on key findings and recommendations."
        
        try:
            with open(prompt_path, 'r', encoding='utf-8') as f:
                base_prompt = f.read()
                print(f"✅ Loaded AI prompt from {prompt_path}")
        except FileNotFoundError:
            print(f"⚠️ Prompt file not found at {prompt_path}, using default")
        
        truncated_content = content[:15000] if len(content) > 15000 else content
        
        retries = 3
        delay = 5  # seconds
        for i in range(retries):
            try:
                summary_prompt = f"{base_prompt}\n\nOrganization: {org_name}\nReport Title: {report_title}\nYear: {year}\n\nReport Content:\n{truncated_content}"
                summary_response = self.current_model.generate_content(summary_prompt)
                summary = summary_response.text if summary_response.text else "No summary generated"
                
                summary = ' '.join(summary.split())
                if len(summary) > 400:
                    sentences = summary.split('. ')
                    truncated_summary = ""
                    for sentence in sentences:
                        if len(truncated_summary + sentence + '. ') <= 400:
                            truncated_summary += sentence + '. '
                        else:
                            break
                    summary = truncated_summary.strip()
                
                type_prompt = f"Based on this content, is this an 'Analysis' report (detailed technical analysis) or 'Survey' report (industry survey/statistics)? Respond with only 'Analysis' or 'Survey'. Content preview: {truncated_content[:1000]}"
                type_response = self.current_model.generate_content(type_prompt)
                report_type = "Analysis" if "analysis" in type_response.text.lower() else "Survey"
                
                # AI-driven sub-categorization
                category_prompt = f"Given the following categories: {self.categories}. Which category best describes the content of this report? Respond with only the category name. Report content: {truncated_content[:2000]}"
                category_response = self.current_model.generate_content(category_prompt)
                category = category_response.text.strip()
                
                # Fallback to keyword matching if AI returns an invalid category
                if category not in self.categories:
                    print(f"⚠️ AI returned invalid category '{category}'. Falling back to keyword matching.")
                    category = self._categorize_content_fallback(truncated_content)
                
                return {
                    'organization': org_name,
                    'year': year,
                    'title': report_title,
                    'summary': summary,
                    'type': report_type,
                    'category': category,
                    'organization_url': organization_url, # Pass through the URL
                    'ai_processed': True
                }
            except Exception as e:
                print(f"❌ AI analysis failed (attempt {i+1}/{retries}): {e}")
                if "429" in str(e) and i < retries - 1:
                    time.sleep(delay * (2 ** i)) # Exponential backoff
                else:
                    return self._fallback_analysis(content, org_name, year, report_title, organization_url)
        return self._fallback_analysis(content, org_name, year, report_title, organization_url)
            
    def _categorize_content_fallback(self, content: str) -> str:
        """Categorize content based on keywords (fallback if AI fails)"""
        keyword_mapping = {
            'Identity and Access Management': ['identity', 'access', 'authentication', 'authorization', 'IAM', 'SSO', 'MFA'],
            'Cloud Security': ['cloud', 'AWS', 'Azure', 'GCP', 'kubernetes', 'container', 'serverless'],
            'Application Security': ['application', 'software', 'code', 'development', 'SAST', 'DAST', 'API'],
            'Ransomware and Malware': ['ransomware', 'malware', 'threat', 'attack', 'breach', 'incident'],
            'Compliance and Governance': ['compliance', 'governance', 'regulation', 'policy', 'audit', 'GRC'],
            'Network Security': ['network', 'firewall', 'VPN', 'intrusion', 'IDS', 'IPS', 'DDoS'],
            'Data Security': ['data', 'privacy', 'encryption', 'DLP', 'database', 'backup'],
            'Endpoint Security': ['endpoint', 'device', 'mobile', 'laptop', 'workstation', 'MDM'],
            'Security Operations': ['SOC', 'SIEM', 'monitoring', 'detection', 'response', 'incident'],
            'Emerging Technologies': ['AI', 'ML', 'IoT', 'blockchain', 'quantum', 'edge'],
            'Vulnerabilities': ['vulnerability', 'assessment'],
            'Penetration Testing': ['penetration', 'testing'],
            'Industry Trends': ['risk']
        }
        content_lower = content.lower()
        scores = {}
        
        for category, keywords in keyword_mapping.items():
            score = sum(content_lower.count(keyword.lower()) for keyword in keywords)
            scores[category] = score
        
        best_category = max(scores, key=scores.get) if scores else "Security Operations"
        return best_category if scores[best_category] > 0 else "Security Operations"
        
    def _fallback_analysis(self, content: str, org_name: str, year: str, report_title: str, organization_url: Optional[str] = None) -> Dict:
        """Fallback analysis without AI"""
        category = self._categorize_content_fallback(content)
        
        sentences = content.split('. ')
        summary = '. '.join(sentences[:3]) + '.' if len(sentences) > 3 else content[:300]
        
        return {
            'organization': org_name,
            'year': year,
            'title': report_title,
            'summary': summary,
            'type': "Analysis",
            'category': category,
            'organization_url': organization_url, # Pass through the URL
            'ai_processed': False
        }

class ReadmeUpdater:
    def __init__(self, readme_parser: ReadmeParser):
        self.parser = readme_parser
        
    def add_report_entry(self, analysis: Dict, file_path: str) -> Tuple[bool, str, int, str]:
        """Add or update a report entry in the README"""
        action_taken = ""
        try:
            logical_main_section = f"{analysis['type']} Reports"
            logical_subsection = analysis['category']
            
            if logical_main_section not in self.parser.toc_structure:
                print(f"⚠️ Logical main section '{logical_main_section}' not found in TOC structure.")
                return False, "", -1, ""
            
            if logical_subsection not in self.parser.toc_structure[logical_main_section]['subsections']:
                print(f"⚠️ Logical subsection '{logical_subsection}' not found under '{logical_main_section}' in TOC structure.")
                similar_subsection_in_toc = self._find_similar_section(logical_subsection, logical_main_section)
                if similar_subsection_in_toc:
                    logical_subsection = similar_subsection_in_toc
                    print(f"📍 Using similar logical subsection from TOC: {logical_subsection}")
                else:
                    return False, "", -1, ""
            
            target_heading_in_readme = logical_subsection
            
            start, end = self.parser.find_section_content(target_heading_in_readme)
            if start == -1:
                print(f"❌ Could not find content area for actual README heading: '## {target_heading_in_readme}'")
                return False, "", -1, ""
            
            section_content = self.parser.content[start:end]
            
            entry_text = self._format_entry(analysis, file_path, analysis.get('organization_url'))
            
            org_pattern = re.escape(analysis['organization'])
            title_pattern = re.escape(analysis['title'])
            existing_entry_pattern = rf"^- \[({org_pattern})\]\(.*?\) - \[({title_pattern})\]\(.*?\) \((\d{{4}})\).*$" # More robust pattern
            
            lines = section_content.strip().split('\n')
            updated_lines = []
            entry_updated = False

            for line in lines:
                match = re.search(existing_entry_pattern, line)
                if match:
                    existing_org = match.group(1)
                    existing_title = match.group(2)
                    existing_year = int(match.group(3))
                    
                    if existing_org == analysis['organization'] and existing_title == analysis['title']:
                        new_report_year = int(analysis['year'])
                        if new_report_year > existing_year:
                            print(f"📝 Updating existing entry for {analysis['organization']} - {analysis['title']} (from {existing_year} to {new_report_year})")
                            updated_lines.append(entry_text)
                            entry_updated = True
                            action_taken = "📝 Updated"
                        else:
                            print(f"ℹ️ Existing entry for {analysis['organization']} - {analysis['title']} ({existing_year}) is newer or same year as new report ({new_report_year}). No update needed.")
                            updated_lines.append(line)
                    else:
                        updated_lines.append(line)
                else:
                    updated_lines.append(line)

            if not entry_updated:
                print(f"➕ Adding new entry for {analysis['organization']} - {analysis['title']} ({analysis['year']})")
                updated_lines.append(entry_text)
                action_taken = "➕ Added"

            # Sort only the entries, preserve other lines
            other_lines = [line for line in lines if not re.match(r"^- \[.*?\]\(.*?\) - \[.*?\]\(.*?\) \d{4}.*$", line.strip())]
            entry_lines = [line for line in updated_lines if re.match(r"^- \[.*?\]\(.*?\) - \[.*?\]\(.*?\) \d{4}.*$", line.strip())]
            entry_lines.sort(key=lambda x: (self._extract_org_name_for_sorting(x), self._extract_report_title_for_sorting(x)))
            
            # Reconstruct the section content
            updated_section_content = "\n".join(other_lines + entry_lines) + "\n"

            self.parser.content = (
                self.parser.content[:start] + 
                updated_section_content + 
                self.parser.content[end:]
            )
            
            inserted_line_number = -1
            updated_content_lines = self.parser.content.split('\n')
            for i, line in enumerate(updated_content_lines):
                if line.strip() == entry_text.strip():
                    inserted_line_number = i + 1
                    break
            
            return True, entry_text, inserted_line_number, action_taken
            
        except Exception as e:
            print(f"❌ Error updating README: {e}")
            return False, "", -1, ""
            
    def _format_entry(self, analysis: Dict, file_path: str, organization_url: Optional[str] = None) -> str:
        """Format entry according to specified template"""
        title = analysis['title']
        org_name = analysis['organization']
        
        # Use provided organization_url if available, otherwise generate from name
        if organization_url:
            org_link = organization_url
        else:
            domain_base = re.sub(r'\b(company|corp|corporation|inc|llc|ltd|group|security|cyber|tech|technologies)\b', '', org_name.lower())
            domain_base = re.sub(r'[^a-z0-9]', '', domain_base)
            if len(domain_base) < 3:
                domain_base = re.sub(r'[^a-z0-9]', '', org_name.lower())
            org_link = f"https://{domain_base}.com"
        
        path_parts = Path(file_path).parts
        year = "Unknown"
        for part in path_parts:
            if part.isdigit() and len(part) == 4:
                year = part
                break
        
        original_filename_stem = Path(file_path).stem
        correct_pdf_path = Path("Annual Security Reports") / year / f"{original_filename_stem}.pdf"
        pdf_path_encoded = str(correct_pdf_path).replace(' ', '%20')
        
        entry = f"- [{org_name}]({org_link}) - [{title}]({pdf_path_encoded}) ({analysis['year']}) - {analysis['summary']}"
        
        return entry
        
    def _extract_org_name_for_sorting(self, entry_line: str) -> str:
        match = re.search(r'- \[([^\]]+)\]', entry_line)
        return match.group(1) if match else entry_line
    
    def _extract_report_title_for_sorting(self, entry_line: str) -> str:
        match = re.search(r'\]\(.*?\) - \[([^\]]+)\]', entry_line)
        return match.group(1) if match else entry_line
            
    def _find_similar_section(self, target: str, main_section: str) -> Optional[str]:
        """Find similar section name"""
        available_sections = list(self.parser.toc_structure[main_section]['subsections'].keys())
        for section in available_sections:
            if any(word in section.lower() for word in target.lower().split()):
                return section
        return None
        
    def save_readme(self) -> bool:
        try:
            with open(self.parser.readme_path, 'w', encoding='utf-8') as f:
                f.write(self.parser.content)
            return True
        except Exception as e:
            print(f"❌ Error saving README: {e}")
            return False

def get_file_path_from_env_or_argv():
    """Gets the file path from CHANGED_MD_FILES env var or script argument."""
    if 'CHANGED_MD_FILES' in os.environ and os.environ['CHANGED_MD_FILES']:
        # Assuming the first file is the one to process if multiple are passed
        return os.environ['CHANGED_MD_FILES'].split('\n')[0].strip()
    if len(sys.argv) > 1:
        return sys.argv[1]
    return None

def main():
    file_path = get_file_path_from_env_or_argv()
    if not file_path:
        print("Usage: python update-readme.py <markdown_file_path> OR set CHANGED_MD_FILES env var")
        sys.exit(1)
    
    print("🚀 Starting AI README update process")
    
    readme_parser = ReadmeParser("README.md")
    if not readme_parser.content:
        print("❌ Could not read README.md. Exiting.")
        sys.exit(1)
    
    analyzer = ReportAnalyzer(os.getenv('GEMINI_API_KEY'))
    updater = ReadmeUpdater(readme_parser)
    
    try:
        print(f"\n🔍 Processing: {file_path}")
        
        if not os.path.exists(file_path):
            print(f"❌ File not found: {file_path}")
            sys.exit(1)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.strip():
            print(f"⚠️ Empty file: {file_path}")
            sys.exit(1)
        
        org_name, year, report_title = analyzer.extract_info_from_path(file_path)
        analysis = analyzer.analyze_content(content, org_name, year, report_title)
        success, _, _, action_taken = updater.add_report_entry(analysis, file_path)
        
        if success:
            if updater.save_readme():
                print(f"\n✅ Successfully updated README.md with {org_name} ({year})")
                summary_text = f"✍ {action_taken} {analysis['organization']} - {analysis['title']} ({analysis['year']})"
                with open("pr_summary.txt", "w") as f:
                    f.write(summary_text)
            else:
                print("❌ Failed to save README.md")
                sys.exit(1)
        else:
            print(f"❌ Failed to update README for {org_name} ({year})")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()