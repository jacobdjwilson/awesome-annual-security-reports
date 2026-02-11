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
# CONFIGURATION
# ==========================
MAX_SUMMARY_LENGTH = 400
MIN_SUMMARY_LENGTH = 40
REQUIRED_VERBS = [
    'analyzes', 'examines', 'evaluates', 'assesses', 'reviews',
    'interprets', 'dissects', 'deconstructs', 'scrutinizes',
    'compares', 'investigates', 'explores', 'probes', 'surveys',
    'inquires', 'studies', 'documents', 'traces', 'maps',
    'highlights', 'focuses', 'provides', 'offers', 'outlines'
]
FORBIDDEN_PHRASES = [
    'this report', 'the report', 'this document', 'the document',
    'this study', 'the study', 'this analysis', 'the analysis'
]
MARKETING_WORDS = [
    'revolutionary', 'groundbreaking', 'cutting-edge',
    'game-changing', 'unprecedented', 'innovative'
]

# Boundary markers
START_MARKER = "## Analysis Reports"
END_MARKER = "## Resources"

# ==========================
# SUMMARY VALIDATOR
# ==========================
class SummaryValidator:
    """Programmatic validation of AI-generated summaries."""
    
    @staticmethod
    def validate(summary: str) -> Tuple[bool, List[str]]:
        """Comprehensive summary validation. Returns: (is_valid, list_of_errors)"""
        errors = []
        
        if not summary or not summary.strip():
            errors.append("Summary is empty")
            return False, errors
        
        summary = summary.strip()
        
        # 1. Length validation
        if len(summary) > MAX_SUMMARY_LENGTH:
            errors.append(f"Too long: {len(summary)} chars (max {MAX_SUMMARY_LENGTH})")
        elif len(summary) < MIN_SUMMARY_LENGTH:
            errors.append(f"Too short: {len(summary)} chars (min {MIN_SUMMARY_LENGTH})")
        
        # 2. Single line check
        if '\n' in summary or '\r' in summary:
            errors.append("Contains newlines (must be single line)")
            summary = ' '.join(summary.split())
        
        # 3. Sentence count (1-3 sentences)
        sentences = [s.strip() for s in summary.split('.') if s.strip()]
        if len(sentences) > 3:
            errors.append(f"Too many sentences: {len(sentences)} (max 3)")
        elif len(sentences) < 1:
            errors.append("No complete sentences")
        
        # 4. Starting verb check
        first_word = summary.split()[0].lower().rstrip('.,;:') if summary.split() else ''
        if first_word not in REQUIRED_VERBS:
            errors.append(f"Must start with required verb, found '{first_word}'")
        
        # 5. Forbidden phrases
        summary_lower = summary.lower()
        for phrase in FORBIDDEN_PHRASES:
            if phrase in summary_lower:
                errors.append(f"Contains forbidden phrase: '{phrase}'")
        
        # 6. Character validation
        if not re.match(r"^[a-zA-Z0-9\s',.\-]+$", summary):
            errors.append("Contains invalid characters")
        
        # 7. Parentheses/quotes check
        if '(' in summary or ')' in summary:
            errors.append("Contains parentheses (not allowed)")
        if '"' in summary:
            errors.append("Contains quotes (not allowed)")
        
        # 8. Marketing language
        for word in MARKETING_WORDS:
            if word in summary_lower:
                errors.append(f"Contains marketing language: '{word}'")
        
        # 9. Multiple spaces check
        if '  ' in summary:
            errors.append("Contains multiple consecutive spaces")
        
        # 10. Ends with period
        if not summary.endswith('.'):
            errors.append("Must end with period")
        
        return len(errors) == 0, errors
    
    @staticmethod
    def sanitize(summary: str) -> str:
        """Attempt to fix common issues in summary."""
        if not summary:
            return ""
        
        # Remove newlines and collapse spaces
        summary = ' '.join(summary.split())
        
        # Remove quotes and parentheses
        summary = re.sub(r'[()"\']', '', summary)
        
        # Ensure ends with period
        if summary and not summary.endswith('.'):
            summary += '.'
        
        # Limit length
        if len(summary) > MAX_SUMMARY_LENGTH:
            sentences = summary.split('. ')
            summary = ''
            for sentence in sentences:
                if len(summary + sentence + '. ') <= MAX_SUMMARY_LENGTH:
                    summary += sentence + '. '
                else:
                    break
            summary = summary.strip()
        
        return summary

# ==========================
# CATEGORY MANAGER
# ==========================
class CategoryManager:
    """Manages report categories from centralized JSON."""
    
    def __init__(self, categories_path: str = ".github/artifacts/report-categories.json"):
        self.categories_path = Path(categories_path)
        self.categories = self._load_categories()
        self.category_map = self._build_category_map()
    
    def _load_categories(self) -> Dict[str, Any]:
        """Load categories with fallback."""
        if not self.categories_path.exists():
            print(f"WARNING: Categories file not found: {self.categories_path}")
            return self._get_fallback_categories()
        
        try:
            with open(self.categories_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid categories JSON: {e}")
            return self._get_fallback_categories()
    
    def _get_fallback_categories(self) -> Dict[str, Any]:
        """Fallback category structure."""
        return {
            "categories": [
                {
                    "parent": "Analysis Reports",
                    "sub_categories": [
                        {"name": "Global Threat Intelligence"},
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
        """Build searchable category map - O(n) complexity."""
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
    
    def match_category(self, category_hint: str, report_type: str = "Analysis") -> Tuple[str, str, float]:
        """Match category with confidence score."""
        if not category_hint:
            return self._get_default_category(report_type)
        
        # Exact match
        normalized = category_hint.lower().strip()
        if normalized in self.category_map:
            match = self.category_map[normalized]
            return match["name"], match["parent"], 1.0
        
        # Fuzzy match
        best_score = 0.0
        best_match = None
        for key, cat_info in self.category_map.items():
            score = self._similarity_score(normalized, key)
            if score > best_score:
                best_score = score
                best_match = cat_info
        
        if best_match and best_score > 0.6:
            return best_match["name"], best_match["parent"], best_score
        
        return self._get_default_category(report_type)
    
    def _similarity_score(self, str1: str, str2: str) -> float:
        """Calculate word overlap similarity."""
        words1 = set(str1.split())
        words2 = set(str2.split())
        if not words1 or not words2:
            return 0.0
        overlap = len(words1.intersection(words2))
        return overlap / max(len(words1), len(words2))
    
    def _get_default_category(self, report_type: str) -> Tuple[str, str, float]:
        """Default category based on type."""
        if "survey" in report_type.lower():
            return "Industry Trends", "Survey Reports", 0.0
        return "Global Threat Intelligence", "Analysis Reports", 0.0
    
    def get_all_categories(self) -> Dict[str, List[str]]:
        """Get all categories organized by parent."""
        result = {}
        for parent_cat in self.categories.get("categories", []):
            parent_name = parent_cat["parent"]
            sub_cats = [sub["name"] for sub in parent_cat.get("sub_categories", [])]
            result[parent_name] = sub_cats
        return result

# ==========================
# README PARSER WITH BOUNDARIES
# ==========================
class ReadmeParser:
    """Efficiently parses README structure with strict boundary enforcement."""
    
    def __init__(self, readme_path: str, category_manager: CategoryManager = None):
        self.readme_path = Path(readme_path)
        self.category_manager = category_manager
        
        if not self.readme_path.exists():
            raise FileNotFoundError(f"README not found: {readme_path}")
        
        self.full_content = self.readme_path.read_text(encoding='utf-8')
        self.start_boundary, self.end_boundary = self._find_boundaries()
        
        # Extract only the modifiable section
        self.content = self.full_content[self.start_boundary:self.end_boundary]
        self.structure = self._parse_structure()
    
    def _find_boundaries(self) -> Tuple[int, int]:
        """Find start and end positions of modifiable section."""
        start_match = re.search(rf'^{re.escape(START_MARKER)}\s*$', self.full_content, re.MULTILINE)
        end_match = re.search(rf'^{re.escape(END_MARKER)}\s*$', self.full_content, re.MULTILINE)
        
        if not start_match:
            raise ValueError(f"Start marker '{START_MARKER}' not found in README")
        if not end_match:
            raise ValueError(f"End marker '{END_MARKER}' not found in README")
        
        start_pos = start_match.end()
        end_pos = end_match.start()
        
        if start_pos >= end_pos:
            raise ValueError("Start marker appears after end marker")
        
        print(f"✓ Found modifiable section: lines {self.full_content[:start_pos].count(chr(10))+1} to {self.full_content[:end_pos].count(chr(10))+1}")
        
        return start_pos, end_pos
    
    def _parse_structure(self) -> Dict[str, Any]:
        """Parse README structure from categories."""
        if self.category_manager:
            structure = {}
            for parent, subcats in self.category_manager.get_all_categories().items():
                structure[parent] = {"subsections": {subcat: {} for subcat in subcats}}
            return structure
        
        # Fallback structure
        return {
            "Analysis Reports": {"subsections": {"Global Threat Intelligence": {}}},
            "Survey Reports": {"subsections": {"Industry Trends": {}}}
        }
    
    def find_section_bounds(self, heading_name: str, level: int = 3) -> Tuple[int, int]:
        """Find section boundaries within modifiable content - O(n) complexity."""
        pattern = rf'^{"#" * level}\s+{re.escape(heading_name)}\s*$'
        match = re.search(pattern, self.content, re.MULTILINE)
        
        if not match:
            return -1, -1
        
        start = match.end() + 1
        next_pattern = rf'\n#{{{1,{level}}}}\s+'
        next_match = re.search(next_pattern, self.content[start:])
        end = start + next_match.start() if next_match else len(self.content)
        
        return start, end
    
    def get_full_content(self) -> str:
        """Reconstruct full README with updated modifiable section."""
        return (self.full_content[:self.start_boundary] + 
                self.content + 
                self.full_content[self.end_boundary:])

# ==========================
# README UPDATER
# ==========================
class ReadmeUpdater:
    """Intelligent README updates with strict boundary enforcement."""
    
    def __init__(self, parser: ReadmeParser, category_manager: CategoryManager = None):
        self.parser = parser
        self.category_manager = category_manager
        self.validator = SummaryValidator()
    
    def add_report_entry(self, analysis: Dict[str, Any]) -> Tuple[bool, str, int, str]:
        """Main entry point - handles add/update logic within boundaries."""
        
        # Validate data
        if not self._validate_data(analysis):
            return False, "", -1, "invalid_data"
        
        # Validate and sanitize summary
        is_valid, errors = self.validator.validate(analysis['summary'])
        if not is_valid:
            print(f"  WARNING: Summary validation failed:")
            for error in errors:
                print(f"    - {error}")
            # Attempt to fix
            analysis['summary'] = self.validator.sanitize(analysis['summary'])
            print(f"  Sanitized summary: {analysis['summary'][:50]}...")
        
        # Ensure report_url is NOT a Google search link
        if 'organization_url' in analysis and 'google.com/search' in analysis['organization_url']:
            org_name = analysis['organization']
            analysis['organization_url'] = f"https://www.{''.join(c for c in org_name if c.isalnum()).lower()}.com"
            print(f"  Fixed Google search URL to: {analysis['organization_url']}")
        
        # Determine category
        if self.category_manager:
            category_name, parent_type, confidence = self.category_manager.match_category(
                analysis.get('category', ''), analysis.get('type', 'Analysis')
            )
            if confidence < 1.0:
                print(f"  Category: '{analysis.get('category')}' → '{category_name}' (conf: {confidence:.2f})")
            analysis['category'] = category_name
            analysis['type'] = parent_type.replace(" Reports", "")
        
        # Check for existing report
        existing = self._find_existing_report(analysis)
        
        if existing:
            return self._update_existing(existing, analysis)
        else:
            return self._insert_new(analysis)
    
    def _find_existing_report(self, analysis: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Find existing report using Annual%20Security link matching as PRIMARY signal."""
        pdf_filename = Path(analysis['pdf_path']).name.lower()
        pdf_base = re.sub(r'\d{4}', '', pdf_filename).replace('%20', ' ').strip('-_ ')
        org_lower = analysis['organization'].lower()
        title_norm = self._normalize_title(analysis['title'])
        
        # Parse all entries in modifiable section only
        for line in self.parser.content.split('\n'):
            if not line.strip().startswith('- ['):
                continue
            
            # Parse: - [Org](OrgURL) - [Title](ReportURL) (Year) - Summary
            match = re.match(
                r'^-\s*\[([^\]]+)\]\(([^\)]+)\)\s*-\s*\[([^\]]+)\]\(([^\)]+)\)\s*\((\d{4})\)',
                line.strip()
            )
            if not match:
                continue
            
            curr_org = match.group(1).lower()
            curr_report_url = match.group(4).lower()
            curr_title = match.group(3)
            curr_year = int(match.group(5))
            
            # Signal 1: Annual%20Security link match (STRONGEST)
            if 'annual%20security%20reports' in curr_report_url or 'annual security reports' in curr_report_url:
                curr_filename = Path(urllib.parse.unquote(curr_report_url)).name.lower()
                curr_base = re.sub(r'\d{4}', '', curr_filename).replace('%20', ' ').strip('-_ ')
                
                if pdf_base and curr_base and pdf_base == curr_base:
                    return {
                        'line': line,
                        'year': curr_year,
                        'org': match.group(1),
                        'title': match.group(3),
                        'match_type': 'pdf_filename'
                    }
            
            # Signal 2: Org + Title match
            if curr_org == org_lower and self._normalize_title(curr_title) == title_norm:
                return {
                    'line': line,
                    'year': curr_year,
                    'org': match.group(1),
                    'title': match.group(3),
                    'match_type': 'org_title'
                }
        
        return None
    
    def _update_existing(self, existing: Dict[str, Any], analysis: Dict[str, Any]) -> Tuple[bool, str, int, str]:
        """Update existing entry with new year."""
        new_year = int(analysis['year'])
        old_year = existing['year']
        
        if new_year <= old_year:
            return False, "", -1, f"older_or_same_year ({new_year} <= {old_year})"
        
        # Format new entry
        new_line = self._format_entry(analysis)
        
        # Replace old with new in modifiable content only
        self.parser.content = self.parser.content.replace(existing['line'], new_line)
        
        return True, new_line, self._find_line_number(new_line), "updated"
    
    def _insert_new(self, analysis: Dict[str, Any]) -> Tuple[bool, str, int, str]:
        """Insert new report in correct category, alphabetically."""
        category = analysis['category']
        
        # Find section
        start, end = self.parser.find_section_bounds(category)
        if start == -1:
            # Try default fallback
            category = "Global Threat Intelligence" if "Analysis" in analysis.get('type', '') else "Industry Trends"
            start, end = self.parser.find_section_bounds(category)
            if start == -1:
                return False, "", -1, "no_valid_section"
        
        # Get section content
        section = self.parser.content[start:end]
        
        # Extract existing entries
        entries = [l for l in section.split('\n') if l.strip().startswith('- [')]
        
        # Add new entry
        new_entry = self._format_entry(analysis)
        entries.append(new_entry)
        
        # Sort alphabetically by organization
        entries.sort(key=lambda x: self._extract_org(x).lower())
        
        # Rebuild section
        new_section = '\n'.join(entries) + '\n'
        self.parser.content = self.parser.content[:start] + new_section + self.parser.content[end:]
        
        return True, new_entry, self._find_line_number(new_entry), "new"
    
    def _format_entry(self, analysis: Dict[str, Any]) -> str:
        """Format entry line with actual report URL (NOT Google search)."""
        # Construct proper report URL
        pdf_name = Path(analysis['pdf_path']).name
        report_url = f"Annual%20Security%20Reports/{analysis['year']}/{pdf_name}".replace(' ', '%20')
        
        # Sanitize summary
        summary = self.validator.sanitize(analysis['summary'])
        
        return (f"- [{analysis['organization']}]({analysis['organization_url']}) "
                f"- [{analysis['title']}]({report_url}) "
                f"({analysis['year']}) - {summary}")
    
    def _extract_org(self, line: str) -> str:
        """Extract organization name from entry line."""
        match = re.search(r'-\s*\[([^\]]+)\]', line)
        return match.group(1) if match else ''
    
    def _normalize_title(self, title: str) -> str:
        """Normalize title for comparison."""
        return re.sub(r'[^a-z0-9]', '', title.lower())
    
    def _find_line_number(self, text: str) -> int:
        """Find line number in full content."""
        full = self.parser.get_full_content()
        for i, line in enumerate(full.split('\n'), 1):
            if text in line:
                return i
        return -1
    
    def _validate_data(self, data: Dict[str, Any]) -> bool:
        """Validate required fields and age threshold."""
        required = ['organization', 'title', 'year', 'summary', 'pdf_path', 'organization_url']
        
        if any(not data.get(f) for f in required):
            missing = [f for f in required if not data.get(f)]
            print(f"  ERROR: Missing fields: {missing}")
            return False
        
        # Age check
        try:
            year = int(data['year'])
            if datetime.now().year - year >= 2:
                print(f"  SKIPPED: Report from {year} exceeds 2-year threshold")
                return False
        except (ValueError, TypeError):
            print(f"  ERROR: Invalid year: {data.get('year')}")
            return False
        
        return True
    
    def save(self):
        """Save updated README with modified section."""
        full_content = self.parser.get_full_content()
        self.parser.readme_path.write_text(full_content, encoding='utf-8')
        print(f"✓ README saved: {self.parser.readme_path}")
        print(f"✓ Modified section between '{START_MARKER}' and '{END_MARKER}'")

# ==========================
# MAIN
# ==========================
def main():
    parser = argparse.ArgumentParser(
        description="Optimized README Updater with boundary enforcement"
    )
    parser.add_argument("analysis_json", help="Path to analysis results JSON")
    parser.add_argument("--readme-path", default="README.md")
    parser.add_argument("--categories-path", default=".github/artifacts/report-categories.json")
    args = parser.parse_args()
    
    # Load analysis
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
        print("No results to process")
        sys.exit(0)
    
    print(f"\n{'='*70}")
    print(f"README Updater - Processing {len(results)} reports")
    print(f"Boundary: '{START_MARKER}' to '{END_MARKER}'")
    print(f"{'='*70}\n")
    
    # Initialize
    try:
        category_mgr = CategoryManager(args.categories_path)
        readme_parser = ReadmeParser(args.readme_path, category_mgr)
        updater = ReadmeUpdater(readme_parser, category_mgr)
    except Exception as e:
        print(f"ERROR: Initialization failed: {e}")
        sys.exit(1)
    
    # Process
    stats = {"new": 0, "updated": 0, "skipped": 0, "errors": 0}
    changes = False
    
    for i, analysis in enumerate(results, 1):
        org = analysis.get('organization', 'Unknown')
        title = analysis.get('title', 'Unknown')
        
        print(f"[{i}/{len(results)}] {org} - {title}")
        
        success, _, _, action = updater.add_report_entry(analysis)
        
        if success:
            stats[action] += 1
            changes = True
            print(f"  ✓ {action.upper()}")
        else:
            if action.startswith("older_or_same"):
                stats["skipped"] += 1
                print(f"  ⊘ SKIPPED: {action}")
            else:
                stats["errors"] += 1
                print(f"  ✗ ERROR: {action}")
    
    # Summary
    print(f"\n{'='*70}")
    print(f"SUMMARY")
    print(f"{'='*70}")
    print(f"New: {stats['new']} | Updated: {stats['updated']} | "
          f"Skipped: {stats['skipped']} | Errors: {stats['errors']}")
    
    if changes:
        updater.save()
        print(f"\n✓ Changes committed to README")
        print(f"✓ Only section between boundaries was modified")
    else:
        print(f"\n⊘ No changes needed")
    
    return 0 if stats['new'] + stats['updated'] > 0 else 1

if __name__ == "__main__":
    sys.exit(main())