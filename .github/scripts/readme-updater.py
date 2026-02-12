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
    """Loads configuration from .github/artifacts/"""
    
    def __init__(self, artifacts_dir: str = ".github/artifacts"):
        self.artifacts_dir = Path(artifacts_dir)
        
        self.pipeline_config = self._load_json("pipeline-config.json")
        self.categories_config = self._load_json("report-categories.json")
        
        if not self.pipeline_config:
            raise ValueError("pipeline-config.json is required")
        if not self.categories_config:
            raise ValueError("report-categories.json is required")
    
    def _load_json(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load JSON file."""
        path = self.artifacts_dir / filename
        if not path.exists():
            print(f"ERROR: {filename} not found")
            return None
        
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid JSON in {filename}: {e}")
            return None
    
    def get_processing_config(self) -> Dict[str, Any]:
        return self.pipeline_config.get("processing", {})

# ==========================
# SUMMARY VALIDATOR
# ==========================
class SummaryValidator:
    """Validates summaries."""
    
    REQUIRED_VERBS = [
        'analyzes', 'examines', 'evaluates', 'assesses', 'reviews',
        'interprets', 'dissects', 'deconstructs', 'scrutinizes',
        'compares', 'investigates', 'explores', 'probes', 'surveys',
        'inquires', 'studies', 'documents', 'traces', 'maps',
        'highlights', 'focuses', 'provides', 'offers', 'outlines'
    ]
    
    @classmethod
    def validate(cls, summary: str) -> Tuple[bool, List[str]]:
        """Validate summary."""
        errors = []
        
        if not summary:
            return False, ["Empty"]
        
        if len(summary) > 400:
            errors.append("TooLong")
        elif len(summary) < 40:
            errors.append("TooShort")
        
        if '\n' in summary:
            errors.append("Newlines")
        
        first = summary.split()[0].lower().rstrip('.,;:') if summary.split() else ''
        if first not in cls.REQUIRED_VERBS:
            errors.append(f"BadStart")
        
        if '(' in summary or ')' in summary or '"' in summary:
            errors.append("Quotes/Parens")
        
        return len(errors) == 0, errors
    
    @classmethod
    def sanitize(cls, summary: str) -> str:
        """Fix issues."""
        if not summary:
            return ""
        
        summary = ' '.join(summary.split())
        summary = re.sub(r'[()"\']', '', summary)
        
        if summary and not summary.endswith('.'):
            summary += '.'
        
        if len(summary) > 400:
            sentences = summary.split('. ')
            summary = ''
            for s in sentences:
                if len(summary + s + '. ') <= 400:
                    summary += s + '. '
                else:
                    break
        
        return summary.strip()

# ==========================
# CATEGORY MANAGER
# ==========================
class CategoryManager:
    """Manages categories."""
    
    def __init__(self, categories_config: Dict[str, Any]):
        self.categories = categories_config
        self.category_map = self._build_map()
    
    def _build_map(self) -> Dict[str, Dict[str, str]]:
        """Build category map."""
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
        """Match category."""
        if not hint:
            return self._get_default(report_type)
        
        normalized = hint.lower().strip()
        if normalized in self.category_map:
            match = self.category_map[normalized]
            return match["name"], match["parent"]
        
        # Fuzzy match
        best_score = 0.0
        best_match = None
        for key, cat_info in self.category_map.items():
            words1 = set(normalized.split())
            words2 = set(key.split())
            if words1 and words2:
                score = len(words1 & words2) / max(len(words1), len(words2))
                if score > best_score:
                    best_score = score
                    best_match = cat_info
        
        if best_match and best_score > 0.6:
            return best_match["name"], best_match["parent"]
        
        return self._get_default(report_type)
    
    def _get_default(self, report_type: str) -> Tuple[str, str]:
        """Default category."""
        if "survey" in report_type.lower():
            return "Industry Trends", "Survey Reports"
        return "Global Threat Intelligence", "Analysis Reports"

# ==========================
# README PARSER
# ==========================
class ReadmeParser:
    """Parses README with smart duplicate detection."""
    
    def __init__(self, readme_path: str, config: ConfigLoader):
        self.readme_path = Path(readme_path)
        self.config = config
        
        self.start_marker = "## Analysis Reports"
        self.end_marker = "## Resources"
        
        if not self.readme_path.exists():
            raise FileNotFoundError(f"README not found")
        
        self.full_content = self.readme_path.read_text(encoding='utf-8')
        self.start_pos, self.end_pos = self._find_boundaries()
        self.content = self.full_content[self.start_pos:self.end_pos]
    
    def _find_boundaries(self) -> Tuple[int, int]:
        """Find section boundaries."""
        start_match = re.search(rf'^{re.escape(self.start_marker)}\s*$', self.full_content, re.MULTILINE)
        end_match = re.search(rf'^{re.escape(self.end_marker)}\s*$', self.full_content, re.MULTILINE)
        
        if not start_match or not end_match:
            raise ValueError("Boundary markers not found")
        
        return start_match.end(), end_match.start()
    
    def find_existing_entry(self, org: str, title: str, pdf_path: str) -> Optional[Tuple[str, int, str]]:
        """
        Find existing entry using multiple signals.
        
        Priority:
        1. Org + Title match (catches category moves)
        2. PDF filename match (catches series updates)
        
        Returns: (full_line, year, match_type) or (None, None, None)
        """
        org_lower = org.lower()
        title_normalized = self._normalize_title(title)
        
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
            
            curr_org = match.group(1).lower()
            curr_title = match.group(3)
            curr_report_url = match.group(4).lower()
            curr_year = int(match.group(5))
            
            # PRIORITY 1: Org + Title match (prevents category move duplicates)
            if curr_org == org_lower and self._normalize_title(curr_title) == title_normalized:
                return line, curr_year, "org_title"
            
            # PRIORITY 2: PDF filename match
            if 'annual%20security%20reports' in curr_report_url or 'annual security reports' in curr_report_url:
                curr_filename = Path(urllib.parse.unquote(curr_report_url)).name.lower()
                curr_base = re.sub(r'\d{4}', '', curr_filename).replace('%20', ' ').strip('-_ .').replace('.pdf', '')
                
                if pdf_base and curr_base and pdf_base == curr_base:
                    return line, curr_year, "pdf_filename"
        
        return None, None, None
    
    def _normalize_title(self, title: str) -> str:
        """Normalize title for comparison."""
        # Remove all non-alphanumeric, lowercase
        return re.sub(r'[^a-z0-9]', '', title.lower())
    
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
    """Updates README - ONLY processes reports in analysis file."""
    
    def __init__(self, parser: ReadmeParser, category_manager: CategoryManager, config: ConfigLoader):
        self.parser = parser
        self.category_manager = category_manager
        self.config = config
        self.validator = SummaryValidator()
    
    def process_report(self, analysis: Dict[str, Any]) -> Tuple[bool, str]:
        """Process a single report. Returns: (success, action)"""
        
        if not self._validate_data(analysis):
            return False, "invalid_data"
        
        # Validate summary
        is_valid, errors = self.validator.validate(analysis['summary'])
        if not is_valid:
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
        
        # Check if entry exists (by Org+Title OR PDF filename)
        existing_line, existing_year, match_type = self.parser.find_existing_entry(
            analysis['organization'],
            analysis['title'],
            analysis['pdf_path']
        )
        
        if existing_line:
            # Found existing entry
            new_year = int(analysis['year'])
            
            if new_year > existing_year:
                # Year is newer - update it
                return self._update_existing(existing_line, existing_year, analysis, match_type)
            else:
                # Year is same or older - skip (already exists)
                return False, f"exists (year {existing_year}, matched by {match_type})"
        else:
            # New report - add it
            return self._insert_new(analysis)
    
    def _update_existing(self, old_line: str, old_year: int, new: Dict[str, Any], match_type: str) -> Tuple[bool, str]:
        """Update existing entry."""
        pdf_name = Path(new['pdf_path']).name
        report_url = f"Annual%20Security%20Reports/{new['year']}/{pdf_name}".replace(' ', '%20')
        summary = self.validator.sanitize(new['summary'])
        
        new_line = (f"- [{new['organization']}]({new['organization_url']}) "
                   f"- [{new['title']}]({report_url}) "
                   f"({new['year']}) - {summary}")
        
        self.parser.content = self.parser.content.replace(old_line, new_line)
        
        return True, f"updated ({old_year}→{new['year']}, {match_type})"
    
    def _insert_new(self, analysis: Dict[str, Any]) -> Tuple[bool, str]:
        """Insert new report."""
        category = analysis['category']
        
        start, end = self.parser.find_section_bounds(category)
        if start == -1:
            category = "Global Threat Intelligence"
            start, end = self.parser.find_section_bounds(category)
            if start == -1:
                return False, "no_section"
        
        section = self.parser.content[start:end]
        entries = [l for l in section.split('\n') if l.strip().startswith('- [')]
        
        pdf_name = Path(analysis['pdf_path']).name
        report_url = f"Annual%20Security%20Reports/{analysis['year']}/{pdf_name}".replace(' ', '%20')
        summary = self.validator.sanitize(analysis['summary'])
        
        new_entry = (f"- [{analysis['organization']}]({analysis['organization_url']}) "
                    f"- [{analysis['title']}]({report_url}) "
                    f"({analysis['year']}) - {summary}")
        
        entries.append(new_entry)
        entries.sort(key=lambda x: self._extract_org(x).lower())
        
        new_section = '\n'.join(entries) + '\n'
        self.parser.content = self.parser.content[:start] + new_section + self.parser.content[end:]
        
        return True, "new"
    
    def _extract_org(self, line: str) -> str:
        """Extract org name."""
        match = re.search(r'-\s*\[([^\]]+)\]', line)
        return match.group(1) if match else ''
    
    def _validate_data(self, data: Dict[str, Any]) -> bool:
        """Validate required fields."""
        required = ['organization', 'title', 'year', 'summary', 'pdf_path', 'organization_url']
        
        if any(not data.get(f) for f in required):
            return False
        
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
    parser = argparse.ArgumentParser(description="README Updater - Production")
    parser.add_argument("analysis_json")
    parser.add_argument("--readme-path", default="README.md")
    parser.add_argument("--artifacts-dir", default=".github/artifacts")
    args = parser.parse_args()
    
    print(f"\n{'='*70}")
    print(f"README Updater")
    print(f"{'='*70}\n")
    
    try:
        config_loader = ConfigLoader(args.artifacts_dir)
        print(f"✓ Config loaded")
    except Exception as e:
        print(f"ERROR: Config load failed: {e}")
        sys.exit(1)
    
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
    
    print(f"✓ {len(analysis_reports)} reports to process\n")
    
    try:
        category_mgr = CategoryManager(config_loader.categories_config)
        readme_parser = ReadmeParser(args.readme_path, config_loader)
        updater = ReadmeUpdater(readme_parser, category_mgr, config_loader)
    except Exception as e:
        print(f"ERROR: Init failed: {e}")
        sys.exit(1)
    
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
    
    print(f"\n{'='*70}")
    print(f"New: {stats['new']} | Updated: {stats['updated']} | Skipped: {stats['skipped']}")
    
    if changes:
        updater.save()
    else:
        print("\n⊘ No changes needed")
    
    return 0 if changes else 1

if __name__ == "__main__":
    sys.exit(main())