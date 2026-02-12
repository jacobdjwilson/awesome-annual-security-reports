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
    """Loads all configuration from JSON files."""
    
    def __init__(self, artifacts_dir: str = ".github/artifacts"):
        self.artifacts_dir = Path(artifacts_dir)
        self.updater_config = self._load_updater_config()
        self.categories_config = self._load_categories_config()
    
    def _load_updater_config(self) -> Dict[str, Any]:
        """Load readme-updater configuration."""
        config_path = self.artifacts_dir / "readme-updater-config.json"
        
        if not config_path.exists():
            print(f"WARNING: Config not found: {config_path}")
            return self._get_default_updater_config()
        
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid config JSON: {e}")
            return self._get_default_updater_config()
    
    def _load_categories_config(self) -> Dict[str, Any]:
        """Load categories configuration."""
        config_path = self.artifacts_dir / "report-categories.json"
        
        if not config_path.exists():
            print(f"WARNING: Categories not found: {config_path}")
            return self._get_default_categories()
        
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid categories JSON: {e}")
            return self._get_default_categories()
    
    def _get_default_updater_config(self) -> Dict[str, Any]:
        """Default configuration."""
        return {
            "validation": {
                "summary": {
                    "max_length": 400,
                    "min_length": 40,
                    "required_verbs": ["analyzes", "examines", "evaluates"],
                    "forbidden_phrases": ["this report", "the report"],
                    "marketing_words": ["revolutionary", "groundbreaking"]
                }
            },
            "processing": {
                "age_threshold_years": 2,
                "start_marker": "## Analysis Reports",
                "end_marker": "## Resources"
            },
            "matching": {
                "similarity_threshold": 0.6,
                "exact_match_priority": True,
                "use_pdf_filename_matching": True,
                "trust_existing_entries": True
            }
        }
    
    def _get_default_categories(self) -> Dict[str, Any]:
        """Default categories."""
        return {
            "categories": [
                {
                    "parent": "Analysis Reports",
                    "sub_categories": [
                        {"name": "Global Threat Intelligence"},
                        {"name": "Cloud Security"}
                    ]
                },
                {
                    "parent": "Survey Reports",
                    "sub_categories": [
                        {"name": "Industry Trends"}
                    ]
                }
            ]
        }

# ==========================
# SUMMARY VALIDATOR
# ==========================
class SummaryValidator:
    """Validates summaries using configuration."""
    
    def __init__(self, config: Dict[str, Any]):
        val_config = config.get("validation", {}).get("summary", {})
        self.max_length = val_config.get("max_length", 400)
        self.min_length = val_config.get("min_length", 40)
        self.required_verbs = val_config.get("required_verbs", [])
        self.forbidden_phrases = val_config.get("forbidden_phrases", [])
        self.marketing_words = val_config.get("marketing_words", [])
    
    def validate(self, summary: str) -> Tuple[bool, List[str]]:
        """Validate summary. Returns: (is_valid, errors)"""
        errors = []
        
        if not summary or not summary.strip():
            return False, ["Empty summary"]
        
        summary = summary.strip()
        
        # Length
        if len(summary) > self.max_length:
            errors.append(f"Too long: {len(summary)} > {self.max_length}")
        elif len(summary) < self.min_length:
            errors.append(f"Too short: {len(summary)} < {self.min_length}")
        
        # Single line
        if '\n' in summary or '\r' in summary:
            errors.append("Contains newlines")
        
        # Starting verb
        if self.required_verbs:
            first_word = summary.split()[0].lower().rstrip('.,;:') if summary.split() else ''
            if first_word not in self.required_verbs:
                errors.append(f"Bad start: '{first_word}'")
        
        # Forbidden phrases
        summary_lower = summary.lower()
        for phrase in self.forbidden_phrases:
            if phrase in summary_lower:
                errors.append(f"Forbidden: '{phrase}'")
        
        # Marketing words
        for word in self.marketing_words:
            if word in summary_lower:
                errors.append(f"Marketing: '{word}'")
        
        # Characters
        if not re.match(r"^[a-zA-Z0-9\s',.\-]+$", summary):
            errors.append("Invalid characters")
        
        # Parentheses/quotes
        if '(' in summary or ')' in summary or '"' in summary:
            errors.append("Has parentheses/quotes")
        
        return len(errors) == 0, errors
    
    def sanitize(self, summary: str) -> str:
        """Fix common issues."""
        if not summary:
            return ""
        
        summary = ' '.join(summary.split())
        summary = re.sub(r'[()"\']', '', summary)
        
        if summary and not summary.endswith('.'):
            summary += '.'
        
        if len(summary) > self.max_length:
            sentences = summary.split('. ')
            summary = ''
            for s in sentences:
                if len(summary + s + '. ') <= self.max_length:
                    summary += s + '. '
                else:
                    break
        
        return summary.strip()

# ==========================
# CATEGORY MANAGER
# ==========================
class CategoryManager:
    """Manages categories from configuration."""
    
    def __init__(self, categories_config: Dict[str, Any], matching_config: Dict[str, Any]):
        self.categories = categories_config
        self.similarity_threshold = matching_config.get("similarity_threshold", 0.6)
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
    
    def match_category(self, hint: str, report_type: str = "Analysis") -> Tuple[str, str, float]:
        """Match category with confidence."""
        if not hint:
            return self._get_default(report_type)
        
        # Exact match
        normalized = hint.lower().strip()
        if normalized in self.category_map:
            match = self.category_map[normalized]
            return match["name"], match["parent"], 1.0
        
        # Fuzzy match
        best_score = 0.0
        best_match = None
        for key, cat_info in self.category_map.items():
            score = self._similarity(normalized, key)
            if score > best_score:
                best_score = score
                best_match = cat_info
        
        if best_match and best_score > self.similarity_threshold:
            return best_match["name"], best_match["parent"], best_score
        
        return self._get_default(report_type)
    
    def _similarity(self, str1: str, str2: str) -> float:
        """Word overlap similarity."""
        words1 = set(str1.split())
        words2 = set(str2.split())
        if not words1 or not words2:
            return 0.0
        return len(words1 & words2) / max(len(words1), len(words2))
    
    def _get_default(self, report_type: str) -> Tuple[str, str, float]:
        """Default category."""
        if "survey" in report_type.lower():
            return "Industry Trends", "Survey Reports", 0.0
        return "Global Threat Intelligence", "Analysis Reports", 0.0
    
    def get_all_categories(self) -> Dict[str, List[str]]:
        """Get all categories."""
        result = {}
        for parent_cat in self.categories.get("categories", []):
            parent_name = parent_cat["parent"]
            result[parent_name] = [sub["name"] for sub in parent_cat.get("sub_categories", [])]
        return result

# ==========================
# README PARSER
# ==========================
class ReadmeParser:
    """Parses README with boundary enforcement."""
    
    def __init__(self, readme_path: str, config: Dict[str, Any], category_manager: CategoryManager):
        self.readme_path = Path(readme_path)
        self.config = config
        self.category_manager = category_manager
        
        proc_config = config.get("processing", {})
        self.start_marker = proc_config.get("start_marker", "## Analysis Reports")
        self.end_marker = proc_config.get("end_marker", "## Resources")
        
        if not self.readme_path.exists():
            raise FileNotFoundError(f"README not found: {readme_path}")
        
        self.full_content = self.readme_path.read_text(encoding='utf-8')
        self.start_pos, self.end_pos = self._find_boundaries()
        self.content = self.full_content[self.start_pos:self.end_pos]
        
        # Parse existing entries once (for efficient lookup)
        self.existing_entries = self._parse_existing_entries()
    
    def _find_boundaries(self) -> Tuple[int, int]:
        """Find section boundaries."""
        start_match = re.search(rf'^{re.escape(self.start_marker)}\s*$', self.full_content, re.MULTILINE)
        end_match = re.search(rf'^{re.escape(self.end_marker)}\s*$', self.full_content, re.MULTILINE)
        
        if not start_match or not end_match:
            raise ValueError("Boundary markers not found")
        
        start = start_match.end()
        end = end_match.start()
        
        if start >= end:
            raise ValueError("Invalid boundary positions")
        
        return start, end
    
    def _parse_existing_entries(self) -> Dict[str, Dict[str, Any]]:
        """
        Parse all existing entries ONCE for efficient lookup.
        Key: normalized PDF base filename (year removed)
        """
        entries = {}
        
        for line in self.content.split('\n'):
            if not line.strip().startswith('- ['):
                continue
            
            match = re.match(
                r'^-\s*\[([^\]]+)\]\(([^\)]+)\)\s*-\s*\[([^\]]+)\]\(([^\)]+)\)\s*\((\d{4})\)\s*-\s*(.+)$',
                line.strip()
            )
            
            if not match:
                continue
            
            org = match.group(1)
            org_url = match.group(2)
            title = match.group(3)
            report_url = match.group(4)
            year = int(match.group(5))
            summary = match.group(6)
            
            # Extract PDF filename and create normalized key
            if 'annual%20security%20reports' in report_url.lower() or 'annual security reports' in report_url.lower():
                pdf_filename = Path(urllib.parse.unquote(report_url)).name.lower()
                # Remove year and special chars for matching
                pdf_base = re.sub(r'\d{4}', '', pdf_filename).replace('%20', ' ').strip('-_ .').replace('.pdf', '')
                
                # Store by PDF base name
                entries[pdf_base] = {
                    'line': line,
                    'org': org,
                    'title': title,
                    'year': year,
                    'report_url': report_url,
                    'org_url': org_url,
                    'summary': summary,
                    'pdf_base': pdf_base
                }
        
        return entries
    
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
    """Updates README with minimal modifications."""
    
    def __init__(self, parser: ReadmeParser, category_manager: CategoryManager, validator: SummaryValidator, config: Dict[str, Any]):
        self.parser = parser
        self.category_manager = category_manager
        self.validator = validator
        self.config = config
        self.trust_existing = config.get("matching", {}).get("trust_existing_entries", True)
    
    def add_report_entry(self, analysis: Dict[str, Any]) -> Tuple[bool, str, int, str]:
        """
        Main entry point.
        ONLY modifies if:
        1. Report doesn't exist (new entry)
        2. Report exists with older year (update year)
        """
        
        # Validate
        if not self._validate_data(analysis):
            return False, "", -1, "invalid_data"
        
        # Validate summary
        is_valid, errors = self.validator.validate(analysis['summary'])
        if not is_valid:
            print(f"  WARNING: Summary issues: {errors[:2]}")
            analysis['summary'] = self.validator.sanitize(analysis['summary'])
        
        # Fix Google search URLs
        if 'organization_url' in analysis and 'google.com/search' in analysis['organization_url']:
            org_name = analysis['organization']
            analysis['organization_url'] = f"https://www.{''.join(c for c in org_name if c.isalnum()).lower()}.com"
        
        # Determine category
        cat_name, parent_type, conf = self.category_manager.match_category(
            analysis.get('category', ''), analysis.get('type', 'Analysis')
        )
        analysis['category'] = cat_name
        analysis['type'] = parent_type.replace(" Reports", "")
        
        # Check if report already exists
        existing = self._find_existing(analysis)
        
        if existing:
            # Report exists - only update if year is newer
            return self._update_if_newer(existing, analysis)
        else:
            # New report - add it
            return self._insert_new(analysis)
    
    def _find_existing(self, analysis: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Find existing report by PDF filename matching.
        Uses pre-parsed entries for O(1) lookup.
        """
        pdf_filename = Path(analysis['pdf_path']).name.lower()
        pdf_base = re.sub(r'\d{4}', '', pdf_filename).replace('%20', ' ').strip('-_ .').replace('.pdf', '')
        
        # O(1) lookup in pre-parsed entries
        return self.parser.existing_entries.get(pdf_base)
    
    def _update_if_newer(self, existing: Dict[str, Any], new: Dict[str, Any]) -> Tuple[bool, str, int, str]:
        """
        Update ONLY if new year > existing year.
        Preserves existing summary and all other details.
        """
        new_year = int(new['year'])
        old_year = existing['year']
        
        if new_year <= old_year:
            return False, "", -1, f"existing_current (year {old_year})"
        
        # Build updated line - use NEW summary (it's from the new report)
        pdf_name = Path(new['pdf_path']).name
        report_url = f"Annual%20Security%20Reports/{new['year']}/{pdf_name}".replace(' ', '%20')
        
        new_line = (f"- [{existing['org']}]({existing['org_url']}) "
                   f"- [{existing['title']}]({report_url}) "
                   f"({new['year']}) - {new['summary']}")
        
        # Replace in content
        self.parser.content = self.parser.content.replace(existing['line'], new_line)
        
        # Update cache
        self.parser.existing_entries[existing['pdf_base']] = {
            **existing,
            'line': new_line,
            'year': new_year
        }
        
        return True, new_line, -1, "updated"
    
    def _insert_new(self, analysis: Dict[str, Any]) -> Tuple[bool, str, int, str]:
        """Insert new report alphabetically in correct category."""
        category = analysis['category']
        
        # Find section
        start, end = self.parser.find_section_bounds(category)
        if start == -1:
            category = "Global Threat Intelligence" if "Analysis" in analysis.get('type', '') else "Industry Trends"
            start, end = self.parser.find_section_bounds(category)
            if start == -1:
                return False, "", -1, "no_section"
        
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
        
        # Sort alphabetically by org name
        entries.sort(key=lambda x: self._extract_org(x).lower())
        
        # Rebuild section
        new_section = '\n'.join(entries) + '\n'
        self.parser.content = self.parser.content[:start] + new_section + self.parser.content[end:]
        
        return True, new_entry, -1, "new"
    
    def _extract_org(self, line: str) -> str:
        """Extract org name."""
        match = re.search(r'-\s*\[([^\]]+)\]', line)
        return match.group(1) if match else ''
    
    def _validate_data(self, data: Dict[str, Any]) -> bool:
        """Validate required fields."""
        required = ['organization', 'title', 'year', 'summary', 'pdf_path', 'organization_url']
        
        if any(not data.get(f) for f in required):
            return False
        
        # Age check
        age_threshold = self.config.get("processing", {}).get("age_threshold_years", 2)
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
    parser = argparse.ArgumentParser(description="Optimized README Updater")
    parser.add_argument("analysis_json")
    parser.add_argument("--readme-path", default="README.md")
    parser.add_argument("--artifacts-dir", default=".github/artifacts")
    args = parser.parse_args()
    
    # Load config
    config_loader = ConfigLoader(args.artifacts_dir)
    
    # Load analysis
    if not os.path.exists(args.analysis_json):
        print(f"ERROR: Analysis file not found")
        sys.exit(1)
    
    try:
        with open(args.analysis_json, 'r') as f:
            results = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON: {e}")
        sys.exit(1)
    
    if not results:
        print("No results to process")
        sys.exit(0)
    
    print(f"\n{'='*70}")
    print(f"README Updater - {len(results)} reports")
    print(f"{'='*70}\n")
    
    # Initialize
    try:
        category_mgr = CategoryManager(
            config_loader.categories_config,
            config_loader.updater_config.get("matching", {})
        )
        validator = SummaryValidator(config_loader.updater_config)
        readme_parser = ReadmeParser(args.readme_path, config_loader.updater_config, category_mgr)
        updater = ReadmeUpdater(readme_parser, category_mgr, validator, config_loader.updater_config)
        
        print(f"✓ Loaded {len(readme_parser.existing_entries)} existing entries")
        print()
        
    except Exception as e:
        print(f"ERROR: Init failed: {e}")
        sys.exit(1)
    
    # Process
    stats = {"new": 0, "updated": 0, "skipped": 0}
    changes = False
    
    for i, analysis in enumerate(results, 1):
        org = analysis.get('organization', 'Unknown')
        
        print(f"[{i}/{len(results)}] {org}")
        
        success, _, _, action = updater.add_report_entry(analysis)
        
        if success:
            stats[action] += 1
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
        print("\n⊘ No changes")
    
    return 0 if changes else 1

if __name__ == "__main__":
    sys.exit(main())