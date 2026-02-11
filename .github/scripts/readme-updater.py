import os
import sys
import json
import re
import argparse
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional
from datetime import datetime
import urllib.parse

# Configuration
MAX_SUMMARY_LENGTH = 400
MIN_SUMMARY_LENGTH = 50
REQUIRED_SUMMARY_START_VERBS = [
    'analyzes', 'examines', 'evaluates', 'assesses', 'reviews', 
    'interprets', 'dissects', 'deconstructs', 'scrutinizes', 
    'compares', 'investigates', 'explores', 'probes', 'surveys',
    'inquires', 'studies', 'documents', 'traces', 'maps', 'highlights',
    'focuses', 'provides', 'offers', 'outlines'
]

class SummaryValidator:
    """Validates AI-generated summaries programmatically."""
    
    @staticmethod
    def validate(summary: str) -> Tuple[bool, List[str]]:
        """
        Validate summary against strict criteria.
        Returns: (is_valid, list_of_errors)
        """
        errors = []
        
        # 1. Length check
        if len(summary) > MAX_SUMMARY_LENGTH:
            errors.append(f"Summary too long: {len(summary)} chars (max {MAX_SUMMARY_LENGTH})")
        elif len(summary) < MIN_SUMMARY_LENGTH:
            errors.append(f"Summary too short: {len(summary)} chars (min {MIN_SUMMARY_LENGTH})")
        
        # 2. Single line check (no newlines)
        if '\n' in summary or '\r' in summary:
            errors.append("Summary contains newlines (must be single line)")
        
        # 3. Sentence count check (max 2-3 sentences)
        sentences = [s.strip() for s in summary.split('.') if s.strip()]
        if len(sentences) > 3:
            errors.append(f"Too many sentences: {len(sentences)} (max 3)")
        elif len(sentences) < 1:
            errors.append("No complete sentences found")
        
        # 4. Starting verb check
        first_word = summary.split()[0].lower().rstrip('.,;:') if summary.split() else ''
        if first_word not in REQUIRED_SUMMARY_START_VERBS:
            errors.append(f"Summary must start with required verb, found: '{first_word}'")
        
        # 5. Forbidden phrases check
        forbidden_phrases = [
            'this report', 'the report', 'this document', 'the document',
            'this study', 'the study', 'this analysis', 'the analysis'
        ]
        summary_lower = summary.lower()
        for phrase in forbidden_phrases:
            if phrase in summary_lower:
                errors.append(f"Summary contains forbidden phrase: '{phrase}'")
        
        # 6. Character validation (only letters, spaces, apostrophes, commas, periods)
        allowed_pattern = re.compile(r"^[a-zA-Z0-9\s',.\-]+$")
        if not allowed_pattern.match(summary):
            errors.append("Summary contains invalid characters (only letters, numbers, spaces, apostrophes, commas, periods, hyphens allowed)")
        
        # 7. Parentheses and quotes check
        if '(' in summary or ')' in summary or '"' in summary or "'" in summary.split()[0]:
            errors.append("Summary contains parentheses or quotes (not allowed)")
        
        # 8. Marketing language check
        marketing_words = ['revolutionary', 'groundbreaking', 'cutting-edge', 'game-changing', 'unprecedented']
        for word in marketing_words:
            if word in summary_lower:
                errors.append(f"Summary contains marketing language: '{word}'")
        
        return len(errors) == 0, errors

class CategoryManager:
    """Manages report categories from centralized configuration."""
    
    def __init__(self, categories_path: str = ".github/artifacts/report-categories.json"):
        self.categories_path = Path(categories_path)
        self.categories = self._load_categories()
        self.category_map = self._build_category_map()
    
    def _load_categories(self) -> Dict[str, Any]:
        """Load categories from JSON with fallback."""
        if not self.categories_path.exists():
            print(f"WARNING: Categories file not found: {self.categories_path}")
            return self._get_fallback_categories()
        
        try:
            with open(self.categories_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid JSON in categories: {e}")
            return self._get_fallback_categories()
    
    def _get_fallback_categories(self) -> Dict[str, Any]:
        """Fallback categories structure."""
        return {
            "categories": [
                {
                    "parent": "Analysis Reports",
                    "sub_categories": [
                        {"name": "Threat Intelligence"},
                        {"name": "Application Security"},
                        {"name": "Cloud Security"},
                        {"name": "Vulnerabilities"},
                        {"name": "Ransomware"},
                        {"name": "Data Breaches"},
                        {"name": "Physical Security"},
                        {"name": "AI and Emerging Technologies"}
                    ]
                },
                {
                    "parent": "Survey Reports",
                    "sub_categories": [
                        {"name": "Industry Trends"},
                        {"name": "Identity Security"},
                        {"name": "Penetration Testing"},
                        {"name": "Privacy and Data Protection"},
                        {"name": "Voice"}
                    ]
                }
            ]
        }
    
    def _build_category_map(self) -> Dict[str, Dict[str, str]]:
        """Build searchable category map."""
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
    
    def match_category(self, category_hint: str) -> Tuple[str, str]:
        """
        Match category hint to best category.
        Returns: (category_name, parent_type)
        """
        if not category_hint:
            return "Industry Trends", "Analysis Reports"
        
        # Exact match
        normalized = category_hint.lower().strip()
        if normalized in self.category_map:
            match = self.category_map[normalized]
            return match["name"], match["parent"]
        
        # Fuzzy match
        best_score = 0
        best_match = None
        for key, cat_info in self.category_map.items():
            score = self._similarity_score(normalized, key)
            if score > best_score:
                best_score = score
                best_match = cat_info
        
        if best_match and best_score > 0.6:
            return best_match["name"], best_match["parent"]
        
        # Default fallback
        return "Industry Trends", "Analysis Reports"
    
    def _similarity_score(self, str1: str, str2: str) -> float:
        """Calculate similarity score between two strings."""
        if not str1 or not str2:
            return 0.0
        
        # Word overlap score
        words1 = set(str1.split())
        words2 = set(str2.split())
        if words1 and words2:
            overlap = len(words1.intersection(words2))
            return overlap / max(len(words1), len(words2))
        return 0.0

class ReadmeParser:
    """Parses README.md structure."""
    
    def __init__(self, readme_path: str, category_manager: CategoryManager):
        self.readme_path = Path(readme_path)
        self.category_manager = category_manager
        
        if not self.readme_path.exists():
            raise FileNotFoundError(f"README.md not found: {readme_path}")
        
        self.content = self.readme_path.read_text(encoding='utf-8')
        self.entries = self._parse_all_entries()
    
    def _parse_all_entries(self) -> List[Dict[str, Any]]:
        """Parse all report entries from README."""
        entries = []
        current_category = None
        
        for line in self.content.split('\n'):
            # Detect category headers
            if line.startswith('### '):
                current_category = line.replace('### ', '').strip()
                continue
            
            # Parse report entry
            # Pattern: - [Org](url) - [Title](url) (year) - summary
            pattern = r'^-\s*\[([^\]]+)\]\(([^)]+)\)\s*-\s*\[([^\]]+)\]\(([^)]+)\)\s*\((\d{4})\)\s*-\s*(.+)$'
            match = re.match(pattern, line.strip())
            
            if match and current_category:
                entries.append({
                    'organization': match.group(1),
                    'org_url': match.group(2),
                    'title': match.group(3),
                    'report_url': match.group(4),
                    'year': int(match.group(5)),
                    'summary': match.group(6).strip(),
                    'category': current_category,
                    'original_line': line
                })
        
        return entries
    
    def find_existing_report(self, pdf_path: str, org_name: str, title: str) -> Optional[Dict[str, Any]]:
        """
        Find existing report entry using multiple signals.
        Uses PDF path matching as primary signal.
        """
        # Extract PDF filename from path
        pdf_filename = Path(pdf_path).name
        pdf_filename_normalized = pdf_filename.lower().replace('%20', ' ').replace('-', ' ')
        
        for entry in self.entries:
            # Signal 1: Check if report_url contains same PDF filename
            if 'Annual%20Security%20Reports' in entry['report_url'] or 'Annual Security Reports' in entry['report_url']:
                entry_filename = Path(urllib.parse.unquote(entry['report_url'])).name.lower().replace('-', ' ')
                
                # Extract base filename without year
                pdf_base = re.sub(r'\d{4}', '', pdf_filename_normalized).strip()
                entry_base = re.sub(r'\d{4}', '', entry_filename).strip()
                
                if pdf_base and entry_base and pdf_base == entry_base:
                    return entry
            
            # Signal 2: Org + Title match (case-insensitive)
            if (entry['organization'].lower() == org_name.lower() and 
                self._normalize_title(entry['title']) == self._normalize_title(title)):
                return entry
        
        return None
    
    def _normalize_title(self, title: str) -> str:
        """Normalize title for comparison."""
        return re.sub(r'[^a-z0-9]', '', title.lower())
    
    def find_section_bounds(self, category_name: str) -> Tuple[int, int]:
        """Find start and end line indices for a category section."""
        lines = self.content.split('\n')
        start_idx = -1
        end_idx = len(lines)
        
        for i, line in enumerate(lines):
            if line.startswith('### ') and category_name in line:
                start_idx = i + 1
                # Find next section header
                for j in range(i + 1, len(lines)):
                    if lines[j].startswith('###') or lines[j].startswith('##'):
                        end_idx = j
                        break
                break
        
        return start_idx, end_idx

class ReadmeUpdater:
    """Updates README with intelligent logic."""
    
    def __init__(self, parser: ReadmeParser, category_manager: CategoryManager):
        self.parser = parser
        self.category_manager = category_manager
        self.validator = SummaryValidator()
    
    def add_or_update_report(self, analysis: Dict[str, Any]) -> Tuple[bool, str, str]:
        """
        Add new report or update existing one.
        Returns: (success, action, message)
        """
        # Validate required fields
        if not self._validate_analysis(analysis):
            return False, "error", "Missing required fields"
        
        # Validate summary
        summary_valid, summary_errors = self.validator.validate(analysis['summary'])
        if not summary_valid:
            print(f"WARNING: Summary validation failed:")
            for error in summary_errors:
                print(f"  - {error}")
            # Continue anyway but log the issues
        
        # Check for existing report
        existing = self.parser.find_existing_report(
            analysis['pdf_path'],
            analysis['organization'],
            analysis['title']
        )
        
        if existing:
            # Update existing entry
            return self._update_existing_report(existing, analysis)
        else:
            # Add new entry
            return self._add_new_report(analysis)
    
    def _update_existing_report(self, existing: Dict[str, Any], new_data: Dict[str, Any]) -> Tuple[bool, str, str]:
        """Update existing report entry with new year data."""
        new_year = int(new_data['year'])
        old_year = existing['year']
        
        if new_year <= old_year:
            return False, "skipped", f"New year ({new_year}) not newer than existing ({old_year})"
        
        # Create updated entry line
        new_line = self._format_entry(new_data)
        
        # Replace old line with new line
        self.parser.content = self.parser.content.replace(existing['original_line'], new_line)
        
        return True, "updated", f"Updated {existing['organization']} from {old_year} to {new_year}"
    
    def _add_new_report(self, analysis: Dict[str, Any]) -> Tuple[bool, str, str]:
        """Add new report entry to appropriate category."""
        # Determine best category
        category_name, parent_type = self.category_manager.match_category(analysis.get('category', ''))
        
        print(f"  Placing in category: {category_name} (under {parent_type})")
        
        # Find section bounds
        start_idx, end_idx = self.parser.find_section_bounds(category_name)
        
        if start_idx == -1:
            return False, "error", f"Category not found: {category_name}"
        
        # Get section content
        lines = self.parser.content.split('\n')
        section_lines = lines[start_idx:end_idx]
        
        # Extract existing entries
        entry_lines = [line for line in section_lines if line.strip().startswith('- [')]
        
        # Add new entry
        new_entry = self._format_entry(analysis)
        entry_lines.append(new_entry)
        
        # Sort alphabetically by organization name
        entry_lines.sort(key=lambda x: self._extract_org_name(x).lower())
        
        # Reconstruct section
        new_section = entry_lines
        
        # Replace section in content
        lines[start_idx:end_idx] = new_section + ['']  # Add blank line after section
        self.parser.content = '\n'.join(lines)
        
        return True, "new", f"Added {analysis['organization']} to {category_name}"
    
    def _format_entry(self, analysis: Dict[str, Any]) -> str:
        """Format report entry line."""
        # Ensure we use the actual report URL, not a Google search URL
        report_url = analysis.get('report_url', analysis['pdf_path'])
        
        # If it's still a Google search URL, extract the intended path
        if 'google.com/search' in report_url:
            # Try to extract from pdf_path
            report_url = analysis['pdf_path']
        
        # Ensure PDF path is properly formatted
        if not report_url.startswith('http') and not report_url.startswith('Annual'):
            # It's a local path, format it
            report_url = f"Annual%20Security%20Reports/{analysis['year']}/{Path(analysis['pdf_path']).name}"
        
        # URL encode spaces
        report_url = report_url.replace(' ', '%20')
        
        # Sanitize summary
        summary = analysis['summary'].strip()
        # Remove any quotes or parentheses that may have slipped through
        summary = summary.replace('"', '').replace("'", "")
        summary = re.sub(r'\([^)]*\)', '', summary).strip()
        
        # Format line
        return (f"- [{analysis['organization']}]({analysis['organization_url']}) "
                f"- [{analysis['title']}]({report_url}) "
                f"({analysis['year']}) - {summary}")
    
    def _extract_org_name(self, line: str) -> str:
        """Extract organization name from entry line."""
        match = re.search(r'-\s*\[([^\]]+)\]', line)
        return match.group(1) if match else ''
    
    def _validate_analysis(self, data: Dict[str, Any]) -> bool:
        """Validate analysis data has required fields."""
        required = ['organization', 'title', 'year', 'summary', 'pdf_path', 'organization_url']
        return all(field in data and data[field] for field in required)
    
    def save(self):
        """Save updated README."""
        self.parser.readme_path.write_text(self.parser.content, encoding='utf-8')
        print(f"✓ README updated: {self.parser.readme_path}")

def main():
    parser = argparse.ArgumentParser(description="Update README with security reports (optimized)")
    parser.add_argument("analysis_json", help="Path to analysis results JSON")
    parser.add_argument("--readme-path", default="README.md", help="Path to README.md")
    parser.add_argument("--categories-path", default=".github/artifacts/report-categories.json",
                       help="Path to categories JSON")
    args = parser.parse_args()
    
    # Load analysis results
    if not os.path.exists(args.analysis_json):
        print(f"ERROR: Analysis file not found: {args.analysis_json}")
        sys.exit(1)
    
    try:
        with open(args.analysis_json, 'r') as f:
            results = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON: {e}")
        sys.exit(1)
    
    if not results:
        print("No analysis results found")
        sys.exit(0)
    
    print(f"Processing {len(results)} reports...")
    
    # Initialize managers
    try:
        category_manager = CategoryManager(args.categories_path)
        readme_parser = ReadmeParser(args.readme_path, category_manager)
        updater = ReadmeUpdater(readme_parser, category_manager)
    except Exception as e:
        print(f"ERROR: Initialization failed: {e}")
        sys.exit(1)
    
    # Process reports
    stats = {"new": 0, "updated": 0, "skipped": 0, "errors": 0}
    changes_made = False
    
    for i, analysis in enumerate(results, 1):
        org = analysis.get('organization', 'Unknown')
        title = analysis.get('title', 'Unknown')
        
        print(f"[{i}/{len(results)}] {org} - {title}")
        
        success, action, message = updater.add_or_update_report(analysis)
        
        if success:
            stats[action] += 1
            changes_made = True
            print(f"  ✓ {action.upper()}: {message}")
        else:
            stats["errors" if action == "error" else "skipped"] += 1
            print(f"  ✗ {action.upper()}: {message}")
    
    # Summary
    print("\n=== Summary ===")
    print(f"New: {stats['new']} | Updated: {stats['updated']} | "
          f"Skipped: {stats['skipped']} | Errors: {stats['errors']}")
    
    # Save if changes made
    if changes_made:
        updater.save()
    else:
        print("No changes needed.")
    
    return 0 if stats['new'] + stats['updated'] > 0 else 1

if __name__ == "__main__":
    sys.exit(main())