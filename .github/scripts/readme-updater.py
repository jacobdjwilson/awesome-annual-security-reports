import os
import sys
import json
import re
import argparse
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional
from datetime import datetime
import urllib.parse

# ==========================
# CONFIGURATION LOADER
# ==========================
class ConfigLoader:
    """Loads all configuration from .github/artifacts/"""
    
    def __init__(self, artifacts_dir: str = ".github/artifacts"):
        self.artifacts_dir = Path(artifacts_dir)
        
        # Load all config files
        self.pipeline_config = self._load_json("pipeline-config.json")
        self.categories_config = self._load_json("report-categories.json")
        
        # Validate required configs loaded
        if not self.pipeline_config:
            raise ValueError("pipeline-config.json is required but not found")
        if not self.categories_config:
            raise ValueError("report-categories.json is required but not found")
    
    def _load_json(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load JSON file from artifacts directory."""
        path = self.artifacts_dir / filename
        if not path.exists():
            print(f"WARNING: {filename} not found in {self.artifacts_dir}")
            return None
        
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid JSON in {filename}: {e}")
            return None
    
    def get_processing_config(self) -> Dict[str, Any]:
        """Get processing configuration."""
        return self.pipeline_config.get("processing", {})
    
    def get_validation_config(self) -> Dict[str, Any]:
        """Get validation configuration."""
        return self.pipeline_config.get("validation", {})

# ==========================
# SUMMARY VALIDATOR
# ==========================
class SummaryValidator:
    """Validates summaries using pipeline config."""
    
    # These are the ONLY constants - validation rules
    REQUIRED_VERBS = [
        'analyzes', 'examines', 'evaluates', 'assesses', 'reviews',
        'interprets', 'dissects', 'deconstructs', 'scrutinizes',
        'compares', 'investigates', 'explores', 'probes', 'surveys',
        'inquires', 'studies', 'documents', 'traces', 'maps',
        'highlights', 'focuses', 'provides', 'offers', 'outlines'
    ]
    MAX_LENGTH = 400
    MIN_LENGTH = 40
    
    @classmethod
    def validate(cls, summary: str) -> Tuple[bool, List[str]]:
        """Validate summary against rules."""
        errors = []
        
        if not summary or not summary.strip():
            return False, ["Empty summary"]
        
        summary = summary.strip()
        
        if len(summary) > cls.MAX_LENGTH:
            errors.append(f"TooLong:{len(summary)}")
        elif len(summary) < cls.MIN_LENGTH:
            errors.append(f"TooShort:{len(summary)}")
        
        if '\n' in summary or '\r' in summary:
            errors.append("HasNewlines")
        
        first_word = summary.split()[0].lower().rstrip('.,;:') if summary.split() else ''
        if first_word not in cls.REQUIRED_VERBS:
            errors.append(f"BadStart:{first_word}")
        
        if not re.match(r"^[a-zA-Z0-9\s',.\-]+$", summary):
            errors.append("InvalidChars")
        
        if '(' in summary or ')' in summary or '"' in summary:
            errors.append("HasQuotes/Parens")
        
        return len(errors) == 0, errors
    
    @classmethod
    def sanitize(cls, summary: str) -> str:
        """Fix common issues."""
        if not summary:
            return ""
        
        summary = ' '.join(summary.split())
        summary = re.sub(r'[()"\']', '', summary)
        
        if summary and not summary.endswith('.'):
            summary += '.'
        
        if len(summary) > cls.MAX_LENGTH:
            sentences = summary.split('. ')
            summary = ''
            for s in sentences:
                if len(summary + s + '. ') <= cls.MAX_LENGTH:
                    summary += s + '. '
                else:
                    break
        
        return summary.strip()

# ==========================
# CATEGORY MANAGER
# ==========================
class CategoryManager:
    """Manages categories from report-categories.json."""
    
    def __init__(self, categories_config: Dict[str, Any]):
        self.categories = categories_config
        self.category_map = self._build_map()
    
    def _build_map(self) -> Dict[str, Dict[str, str]]:
        """Build category lookup map."""
        cat_map = {}
        for parent_cat in self.categories.get("categories", []):
            parent_name = parent_cat["parent"]
            for sub_cat in parent_cat.get("sub_categories", []):
                cat_name = sub_cat["name"]
                cat_map[cat_name.lower()] = {
                    "name": cat_name,
                    "parent": parent_name
                }
        return cat_map
    
    def match_category(self, hint: str, report_type: str = "Analysis") -> Tuple[str, str]:
        """Match category. Returns: (category_name, parent_type)"""
        if not hint:
            return self._get_default(report_type)
        
        # Exact match
        normalized = hint.lower().strip()
        if normalized in self.category_map:
            match = self.category_map[normalized]
            return match["name"], match["parent"]
        
        # Fuzzy match
        best_score = 0.0
        best_match = None
        for key, cat_info in self.category_map.items():
            score = self._similarity(normalized, key)
            if score > best_score:
                best_score = score
                best_match = cat_info
        
        if best_match and best_score > 0.6:
            return best_match["name"], best_match["parent"]
        
        return self._get_default(report_type)
    
    def _similarity(self, str1: str, str2: str) -> float:
        """Word overlap similarity."""
        words1 = set(str1.split())
        words2 = set(str2.split())
        if not words1 or not words2:
            return 0.0
        return len(words1 & words2) / max(len(words1), len(words2))
    
    def _get_default(self, report_type: str) -> Tuple[str, str]:
        """Default category based on type."""
        if "survey" in report_type.lower():
            return "Industry Trends", "Survey Reports"
        return "Global Threat Intelligence", "Analysis Reports"

# ==========================
# README PARSER
# ==========================
class ReadmeParser:
    """Parses README with boundary enforcement."""
    
    def __init__(self, readme_path: str, config: ConfigLoader):
        self.readme_path = Path(readme_path)
        self.config = config
        
        # Get boundaries from config
        repo_config = config.pipeline_config.get("repository", {})
        self.start_marker = "## Analysis Reports"
        self.end_marker = "## Resources"
        
        if not self.readme_path.exists():
            raise FileNotFoundError(f"README not found: {readme_path}")
        
        self.full_content = self.readme_path.read_text(encoding='utf-8')
        self.start_pos, self.end_pos = self._find_boundaries()
        self.content = self.full_content[self.start_pos:self.end_pos]
    
    def _find_boundaries(self) -> Tuple[int, int]:
        """Find section boundaries."""
        start_match = re.search(rf'^{re.escape(self.start_marker)}\s*$', self.full_content, re.MULTILINE)
        end_match = re.search(rf'^{re.escape(self.end_marker)}\s*$', self.full_content, re.MULTILINE)
        
        if not start_match or not end_match:
            raise ValueError(f"Boundary markers not found in README")
        
        start = start_match.end()
        end = end_match.start()
        
        if start >= end:
            raise ValueError("Invalid boundary positions")
        
        return start, end
    
    def find_existing_entry(self, pdf_path: str) -> Optional[Tuple[str, int]]:
        """
        Find existing entry by Annual%20Security PDF filename matching.
        Returns: (full_line, year) or (None, None)
        """
        pdf_filename = Path(pdf_path).name.lower()
        pdf_base = re.sub(r'\d{4}', '', pdf_filename).replace('%20', ' ').strip('-_ .').replace('.pdf', '')
        
        for line in self.content.split('\n'):
            if not line.strip().startswith('- ['):
                continue
            
            match = re.match(
                r'^-\s*\[([^\]]+)\]\(([^\)]+)\)\s*-\s*\[([^\]]+)\]\(([^\)]+)\)\s*\((\d{4})\)',
                line.strip()
            )
            
            if not match:
                continue
            
            report_url = match.group(4).lower()
            year = int(match.group(5))
            
            # Check if this is an Annual Security Reports link
            if 'annual%20security%20reports' in report_url or 'annual security reports' in report_url:
                curr_filename = Path(urllib.parse.unquote(report_url)).name.lower()
                curr_base = re.sub(r'\d{4}', '', curr_filename).replace('%20', ' ').strip('-_ .').replace('.pdf', '')
                
                if pdf_base and curr_base and pdf_base == curr_base:
                    return line, year
        
        return None, None
    
    def find_section_bounds(self, heading: str, level: int = 3) -> Tuple[int, int]:
        """Find section boundaries."""
        pattern = rf'^{"#" * level}\s+{re.escape(heading)}\s*$'
        match = re.search(pattern, self.content, re.MULTILINE)
        
        if not match:
            return -1, -1
        
        start = match.end() + 1
        next_pattern = rf'\n#{{{1,{level}}}}\s+'
        next_match = re.search(next_pattern, self.content[start:])
        end = start + next_match.start() if next_match else len(self.content)
        
        return start, end
    
    def get_full_content(self) -> str:
        """Reconstruct full README."""
        return self.full_content[:self.start_pos] + self.content + self.full_content[self.end_pos:]

# ==========================
# README UPDATER
# ==========================
class ReadmeUpdater:
    """
    Updates README for ONLY the reports being processed.
    NEVER scans or modifies other entries.
    """
    
    def __init__(self, parser: ReadmeParser, category_manager: CategoryManager, config: ConfigLoader):
        self.parser = parser
        self.category_manager = category_manager
        self.config = config
        self.validator = SummaryValidator()
    
    def process_report(self, analysis: Dict[str, Any]) -> Tuple[bool, str]:
        """
        Process a single report from analysis file.
        Returns: (success, action)
        """
        
        # Validate data
        if not self._validate_data(analysis):
            return False, "invalid_data"
        
        # Validate summary
        is_valid, errors = self.validator.validate(analysis['summary'])
        if not is_valid:
            print(f"  ! Summary: {', '.join(errors[:2])}")
            analysis['summary'] = self.validator.sanitize(analysis['summary'])
        
        # Fix Google search URLs
        if 'organization_url' in analysis and 'google.com/search' in analysis['organization_url']:
            org_name = analysis['organization']
            analysis['organization_url'] = f"https://www.{''.join(c for c in org_name if c.isalnum()).lower()}.com"
        
        # Determine category
        cat_name, parent_type = self.category_manager.match_category(
            analysis.get('category', ''), analysis.get('type', 'Analysis')
        )
        analysis['category'] = cat_name
        
        # Check if report exists
        existing_line, existing_year = self.parser.find_existing_entry(analysis['pdf_path'])
        
        if existing_line:
            # Report exists - check if we need to update
            new_year = int(analysis['year'])
            if new_year > existing_year:
                return self._update_existing(existing_line, existing_year, analysis)
            else:
                return False, f"current (year {existing_year})"
        else:
            # New report - add it
            return self._insert_new(analysis)
    
    def _update_existing(self, old_line: str, old_year: int, new: Dict[str, Any]) -> Tuple[bool, str]:
        """Update existing entry with new year."""
        # Build new line with updated year and PDF path
        pdf_name = Path(new['pdf_path']).name
        report_url = f"Annual%20Security%20Reports/{new['year']}/{pdf_name}".replace(' ', '%20')
        summary = self.validator.sanitize(new['summary'])
        
        new_line = (f"- [{new['organization']}]({new['organization_url']}) "
                   f"- [{new['title']}]({report_url}) "
                   f"({new['year']}) - {summary}")
        
        # Replace in content
        self.parser.content = self.parser.content.replace(old_line, new_line)
        
        return True, f"updated ({old_year}→{new['year']})"
    
    def _insert_new(self, analysis: Dict[str, Any]) -> Tuple[bool, str]:
        """Insert new report alphabetically in correct category."""
        category = analysis['category']
        
        # Find section
        start, end = self.parser.find_section_bounds(category)
        if start == -1:
            category = "Global Threat Intelligence"
            start, end = self.parser.find_section_bounds(category)
            if start == -1:
                return False, "no_section"
        
        # Get section
        section = self.parser.content[start:end]
        
        # Extract entries
        entries = [l for l in section.split('\n') if l.strip().startswith('- [')]
        
        # Add new entry
        pdf_name = Path(analysis['pdf_path']).name
        report_url = f"Annual%20Security%20Reports/{analysis['year']}/{pdf_name}".replace(' ', '%20')
        summary = self.validator.sanitize(analysis['summary'])
        
        new_entry = (f"- [{analysis['organization']}]({analysis['organization_url']}) "
                    f"- [{analysis['title']}]({report_url}) "
                    f"({analysis['year']}) - {summary}")
        
        entries.append(new_entry)
        
        # Sort alphabetically
        entries.sort(key=lambda x: self._extract_org(x).lower())
        
        # Rebuild section
        new_section = '\n'.join(entries) + '\n'
        self.parser.content = self.parser.content[:start] + new_section + self.parser.content[end:]
        
        return True, "new"
    
    def _extract_org(self, line: str) -> str:
        """Extract org name from line."""
        match = re.search(r'-\s*\[([^\]]+)\]', line)
        return match.group(1) if match else ''
    
    def _validate_data(self, data: Dict[str, Any]) -> bool:
        """Validate required fields."""
        required = ['organization', 'title', 'year', 'summary', 'pdf_path', 'organization_url']
        
        if any(not data.get(f) for f in required):
            return False
        
        # Age check
        proc_config = self.config.get_processing_config()
        age_threshold = proc_config.get("age_threshold_years", 2)
        
        try:
            year = int(data['year'])
            if datetime.now().year - year >= age_threshold:
                return False
        except (ValueError, TypeError):
            return False
        
        return True
    
    def save(self):
        """Save README."""
        full_content = self.parser.get_full_content()
        self.parser.readme_path.write_text(full_content, encoding='utf-8')
        print(f"✓ README saved")

# ==========================
# MAIN
# ==========================
def main():
    parser = argparse.ArgumentParser(description="README Updater - Processes ONLY reports in analysis file")
    parser.add_argument("analysis_json", help="Path to analysis.json")
    parser.add_argument("--readme-path", default="README.md")
    parser.add_argument("--artifacts-dir", default=".github/artifacts")
    args = parser.parse_args()
    
    print(f"\n{'='*70}")
    print(f"README Updater")
    print(f"{'='*70}\n")
    
    # Load configuration
    try:
        config_loader = ConfigLoader(args.artifacts_dir)
        print(f"✓ Config loaded from {args.artifacts_dir}")
    except Exception as e:
        print(f"ERROR: Config load failed: {e}")
        sys.exit(1)
    
    # Load analysis file
    if not os.path.exists(args.analysis_json):
        print(f"ERROR: Analysis file not found: {args.analysis_json}")
        sys.exit(1)
    
    try:
        with open(args.analysis_json, 'r') as f:
            analysis_reports = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON: {e}")
        sys.exit(1)
    
    if not analysis_reports:
        print("No reports in analysis file")
        sys.exit(0)
    
    print(f"✓ Loaded {len(analysis_reports)} reports from analysis file\n")
    
    # Initialize
    try:
        category_mgr = CategoryManager(config_loader.categories_config)
        readme_parser = ReadmeParser(args.readme_path, config_loader)
        updater = ReadmeUpdater(readme_parser, category_mgr, config_loader)
    except Exception as e:
        print(f"ERROR: Init failed: {e}")
        sys.exit(1)
    
    # Process ONLY the reports in the analysis file
    stats = {"new": 0, "updated": 0, "skipped": 0}
    changes = False
    
    for i, analysis in enumerate(analysis_reports, 1):
        org = analysis.get('organization', 'Unknown')
        
        print(f"[{i}/{len(analysis_reports)}] {org}")
        
        success, action = updater.process_report(analysis)
        
        if success:
            if "updated" in action:
                stats["updated"] += 1
            else:
                stats["new"] += 1
            changes = True
            print(f"  ✓ {action.upper()}")
        else:
            stats["skipped"] += 1
            print(f"  ⊘ SKIP: {action}")
    
    # Summary
    print(f"\n{'='*70}")
    print(f"New: {stats['new']} | Updated: {stats['updated']} | Skipped: {stats['skipped']}")
    
    if changes:
        updater.save()
    else:
        print("\n⊘ No changes needed")
    
    return 0 if changes else 1

if __name__ == "__main__":
    sys.exit(main())