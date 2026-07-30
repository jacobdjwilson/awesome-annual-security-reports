import os
import re
import json
import datetime
from collections import defaultdict
import difflib

# Configuration
README_PATH = "../../README.md"
CATEGORIES_PATH = "../artifacts/report-categories.json"
MD_DIR = "../../Markdown Conversions"
CURRENT_YEAR = 2026 # Hardcoded for now based on current repo state / clock
VALID_YEARS = [CURRENT_YEAR, CURRENT_YEAR - 1] # e.g., 2026, 2025

def load_categories():
    with open(CATEGORIES_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    cat_keywords = {}
    for parent in data.get('categories', []):
        for sub in parent.get('sub_categories', []):
            cat_keywords[sub['name']] = sub.get('keywords', [])
    return cat_keywords

def parse_readme():
    entries = []
    with open(README_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    current_category = None
    category_regex = re.compile(r'^###\s+(.*)$')
    # Regex to match: - [Vendor](link) - [Report Name](PDF_Link) (Year) - Summary
    # Handle possible bolding or other slight variations, but the main format is standard
    entry_regex = re.compile(r'^-\s+\[(.*?)\]\((.*?)\)\s+-\s+\[(.*?)\]\((.*?)\)\s+\((\d{4})\)\s+-\s+(.*)$')
    
    for i, line in enumerate(lines):
        line = line.strip()
        cat_match = category_regex.match(line)
        if cat_match:
            current_category = cat_match.group(1).strip()
            continue
            
        entry_match = entry_regex.match(line)
        if entry_match and current_category:
            vendor = entry_match.group(1).strip()
            vendor_link = entry_match.group(2).strip()
            report_name = entry_match.group(3).strip()
            pdf_link = entry_match.group(4).strip()
            year = int(entry_match.group(5).strip())
            summary = entry_match.group(6).strip()
            
            entries.append({
                'line_number': i + 1,
                'category': current_category,
                'vendor': vendor,
                'vendor_link': vendor_link,
                'report_name': report_name,
                'pdf_link': pdf_link,
                'year': year,
                'summary': summary
            })
            
    return entries

def check_multiple_years_and_retention(entries):
    # Group by normalized vendor + report name
    grouped = defaultdict(list)
    for entry in entries:
        # Remove common words like 'report', 'intelligence' for better grouping if needed, 
        # but exact string is safer for now.
        key = f"{entry['vendor'].lower()} - {entry['report_name'].lower()}"
        grouped[key].append(entry)
        
    findings = []
    for key, group in grouped.items():
        # Sort by year descending
        group.sort(key=lambda x: x['year'], reverse=True)
        latest_year = group[0]['year']
        
        # Check if latest year is out of retention
        if latest_year not in VALID_YEARS:
            findings.append({
                'type': 'outdated_report',
                'vendor': group[0]['vendor'],
                'report_name': group[0]['report_name'],
                'latest_year': latest_year,
                'message': f"Latest year {latest_year} is older than allowed retention ({VALID_YEARS}). Should be removed."
            })
            
        # Check for multiple years (older than latest)
        for entry in group[1:]:
            findings.append({
                'type': 'duplicate_older_year',
                'vendor': entry['vendor'],
                'report_name': entry['report_name'],
                'year': entry['year'],
                'latest_year': latest_year,
                'message': f"Older year {entry['year']} present while {latest_year} exists. Should be removed."
            })
            
    return findings

def check_fuzzy_duplicates(entries):
    findings = []
    texts = [f"{e['vendor']} - {e['report_name']}" for e in entries]
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            similarity = difflib.SequenceMatcher(None, texts[i].lower(), texts[j].lower()).ratio()
            if similarity > 0.85 and similarity < 1.0:
                # To reduce noise, only alert if years are also the same or very close, 
                # but let's just output it for human review.
                findings.append({
                    'type': 'fuzzy_duplicate',
                    'entry1': f"{texts[i]} ({entries[i]['year']})",
                    'entry2': f"{texts[j]} ({entries[j]['year']})",
                    'similarity': round(similarity, 2),
                    'message': "Potential duplicate with slightly different wording."
                })
    return findings

def check_missing_reports(entries):
    findings = []
    readme_files = set()
    for e in entries:
        pdf_path = e['pdf_link']
        filename = os.path.basename(pdf_path)
        md_filename = filename.replace('.pdf', '.md')
        readme_files.add(f"{e['year']}/{md_filename}")
        
    for year in VALID_YEARS:
        year_dir = os.path.join(MD_DIR, str(year))
        if not os.path.exists(year_dir):
            continue
        for f in os.listdir(year_dir):
            if f.endswith('.md'):
                md_rel_path = f"{year}/{f}"
                if md_rel_path not in readme_files:
                    findings.append({
                        'type': 'missing_in_readme',
                        'file': md_rel_path,
                        'message': f"Markdown file {md_rel_path} exists within retention period but is not listed in README.md."
                    })
    return findings

def score_category(text, cat_keywords):
    text_lower = text.lower()
    scores = {}
    for cat, keywords in cat_keywords.items():
        score = 0
        for kw in keywords:
            count = len(re.findall(r'\b' + re.escape(kw.lower()) + r'\b', text_lower))
            score += count
        scores[cat] = score
    return scores

def check_categories(entries, cat_keywords):
    findings = []
    for e in entries:
        pdf_path = e['pdf_link']
        filename = os.path.basename(pdf_path)
        md_filename = filename.replace('.pdf', '.md')
        md_path = os.path.join(MD_DIR, str(e['year']), md_filename)
        
        content = e['summary']
        if os.path.exists(md_path):
            with open(md_path, 'r', encoding='utf-8', errors='ignore') as f:
                content += " " + f.read(5000)
                
        scores = score_category(content, cat_keywords)
        if scores:
            best_cat = max(scores, key=scores.get)
            best_score = scores[best_cat]
            current_cat = e['category']
            
            current_score = scores.get(current_cat, 0)
            
            if current_score == 0 and best_score > 2 and best_cat != current_cat:
                findings.append({
                    'type': 'category_mismatch',
                    'vendor': e['vendor'],
                    'report_name': e['report_name'],
                    'current_category': current_cat,
                    'suggested_category': best_cat,
                    'message': f"Report might be miscategorized. Score for '{current_cat}' is {current_score}, but '{best_cat}' scored {best_score} based on keywords."
                })
                
    return findings

def main():
    cat_keywords = load_categories()
    entries = parse_readme()
    
    findings = {
        'multiple_years_retention': check_multiple_years_and_retention(entries),
        'fuzzy_duplicates': check_fuzzy_duplicates(entries),
        'missing_reports': check_missing_reports(entries),
        'category_mismatches': check_categories(entries, cat_keywords)
    }
    
    with open('readme_audit_findings.json', 'w', encoding='utf-8') as f:
        json.dump(findings, f, indent=2)
        
    print("Audit complete. Findings written to readme_audit_findings.json")
    
    total_findings = sum(len(v) for v in findings.values())
    if total_findings > 0:
        print(f"Found {total_findings} potential issues.")
    else:
        print("No issues found.")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
