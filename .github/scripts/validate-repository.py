import os
import sys
import json
import argparse
from pathlib import Path
from typing import List, Dict, Any, Tuple

try:
    from pypdf import PdfReader
except ImportError:
    print("ERROR: pypdf not installed")
    sys.exit(1)

# ==========================
# CONFIGURATION LOADER
# ==========================
class ConfigLoader:
    """Loads configuration from .github/artifacts/"""
    
    def __init__(self, artifacts_dir: str = ".github/artifacts"):
        self.artifacts_dir = Path(artifacts_dir)
        self.pipeline_config = self._load_json("pipeline-config.json")
        
        if not self.pipeline_config:
            raise ValueError("pipeline-config.json is required")
    
    def _load_json(self, filename: str) -> Dict[str, Any]:
        """Load JSON file."""
        path = self.artifacts_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"{filename} not found in {self.artifacts_dir}")
        
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {filename}: {e}")
    
    def get_repository_config(self) -> Dict[str, Any]:
        """Get repository paths."""
        return self.pipeline_config.get("repository", {})
    
    def get_validation_config(self) -> Dict[str, Any]:
        """Get validation rules."""
        return self.pipeline_config.get("validation", {})

# ==========================
# VALIDATOR
# ==========================
class RepositoryValidator:
    """Validates repository integrity."""
    
    def __init__(self, config: ConfigLoader):
        self.config = config
        
        repo_config = config.get_repository_config()
        self.pdf_root = Path(repo_config.get("pdf_root", "Annual Security Reports"))
        self.md_root = Path(repo_config.get("markdown_root", "Markdown Conversions"))
        
        val_config = config.get_validation_config()
        self.max_file_size_mb = val_config.get("max_file_size_mb", 100)
        self.min_markdown_chars = val_config.get("min_markdown_chars", 50)
        self.magic_number = val_config.get("magic_number", "%PDF")
        
        self.issues = []
        self.stats = {
            "pdf_files": 0,
            "md_files": 0,
            "orphaned_pdfs": 0,
            "orphaned_mds": 0,
            "invalid_pdfs": 0,
            "invalid_mds": 0,
            "oversized_files": 0
        }
    
    def validate(self) -> Tuple[bool, List[str]]:
        """
        Run full validation.
        Returns: (has_issues, issue_list)
        """
        
        print(f"Validating repository structure...")
        print(f"  PDF root: {self.pdf_root}")
        print(f"  MD root: {self.md_root}")
        print()
        
        if not self.pdf_root.exists():
            self.issues.append(f"ERROR: PDF directory not found: {self.pdf_root}")
            return True, self.issues
        
        if not self.md_root.exists():
            self.issues.append(f"ERROR: Markdown directory not found: {self.md_root}")
            return True, self.issues
        
        # Scan directories
        pdf_files = self._scan_pdfs()
        md_files = self._scan_markdowns()
        
        self.stats["pdf_files"] = len(pdf_files)
        self.stats["md_files"] = len(md_files)
        
        print(f"Found {len(pdf_files)} PDFs, {len(md_files)} Markdown files")
        print()
        
        # Check for orphaned files
        self._check_orphaned_pdfs(pdf_files, md_files)
        self._check_orphaned_markdowns(md_files, pdf_files)
        
        # Validate file integrity
        self._validate_pdf_integrity(pdf_files)
        self._validate_markdown_integrity(md_files)
        
        return len(self.issues) > 0, self.issues
    
    def _scan_pdfs(self) -> Dict[str, Path]:
        """Scan for PDF files. Returns: {relative_path: full_path}"""
        pdfs = {}
        for pdf_file in self.pdf_root.rglob("*.pdf"):
            if pdf_file.is_file():
                rel_path = pdf_file.relative_to(self.pdf_root)
                pdfs[str(rel_path)] = pdf_file
        return pdfs
    
    def _scan_markdowns(self) -> Dict[str, Path]:
        """Scan for Markdown files. Returns: {relative_path: full_path}"""
        mds = {}
        for md_file in self.md_root.rglob("*.md"):
            if md_file.is_file():
                rel_path = md_file.relative_to(self.md_root)
                mds[str(rel_path)] = md_file
        return mds
    
    def _check_orphaned_pdfs(self, pdfs: Dict[str, Path], mds: Dict[str, Path]):
        """Check for PDFs without corresponding Markdown."""
        for pdf_rel, pdf_path in pdfs.items():
            md_rel = pdf_rel.replace('.pdf', '.md')
            
            if md_rel not in mds:
                self.issues.append(f"Orphaned PDF (no markdown): {pdf_rel}")
                self.stats["orphaned_pdfs"] += 1
    
    def _check_orphaned_markdowns(self, mds: Dict[str, Path], pdfs: Dict[str, Path]):
        """Check for Markdowns without corresponding PDF."""
        for md_rel, md_path in mds.items():
            pdf_rel = md_rel.replace('.md', '.pdf')
            
            if pdf_rel not in pdfs:
                self.issues.append(f"Orphaned Markdown (no PDF): {md_rel}")
                self.stats["orphaned_mds"] += 1
    
    def _validate_pdf_integrity(self, pdfs: Dict[str, Path]):
        """Validate PDF file integrity."""
        for pdf_rel, pdf_path in pdfs.items():
            # Check size
            size_mb = pdf_path.stat().st_size / (1024 * 1024)
            if size_mb > self.max_file_size_mb:
                self.issues.append(f"Oversized PDF ({size_mb:.1f}MB): {pdf_rel}")
                self.stats["oversized_files"] += 1
            
            # Check magic number
            try:
                with open(pdf_path, 'rb') as f:
                    header = f.read(10).decode('latin-1')
                    if not header.startswith(self.magic_number):
                        self.issues.append(f"Invalid PDF (bad magic number): {pdf_rel}")
                        self.stats["invalid_pdfs"] += 1
            except Exception as e:
                self.issues.append(f"Cannot read PDF: {pdf_rel} ({str(e)[:50]})")
                self.stats["invalid_pdfs"] += 1
            
            # Try to open with pypdf
            try:
                reader = PdfReader(pdf_path)
                if len(reader.pages) == 0:
                    self.issues.append(f"Empty PDF (0 pages): {pdf_rel}")
                    self.stats["invalid_pdfs"] += 1
            except Exception as e:
                self.issues.append(f"Corrupted PDF: {pdf_rel} ({str(e)[:50]})")
                self.stats["invalid_pdfs"] += 1
    
    def _validate_markdown_integrity(self, mds: Dict[str, Path]):
        """Validate Markdown file integrity."""
        for md_rel, md_path in mds.items():
            try:
                content = md_path.read_text(encoding='utf-8')
                
                if len(content) < self.min_markdown_chars:
                    self.issues.append(f"Empty/short Markdown ({len(content)} chars): {md_rel}")
                    self.stats["invalid_mds"] += 1
            except Exception as e:
                self.issues.append(f"Cannot read Markdown: {md_rel} ({str(e)[:50]})")
                self.stats["invalid_mds"] += 1
    
    def generate_report(self, output_path: str = "validation_report.md"):
        """Generate validation report."""
        with open(output_path, 'w') as f:
            f.write("# Repository Integrity Validation Report\n\n")
            
            if not self.issues:
                f.write("## ✅ All Checks Passed\n\n")
                f.write("Repository structure is consistent and all files are properly paired.\n\n")
            else:
                f.write("## ⚠️ Issues Found\n\n")
                f.write(f"Found {len(self.issues)} issues that need attention:\n\n")
                
                for i, issue in enumerate(self.issues, 1):
                    f.write(f"{i}. {issue}\n")
                
                f.write("\n")
            
            f.write("## 📊 Statistics\n\n")
            f.write(f"- PDF Files: {self.stats['pdf_files']}\n")
            f.write(f"- Markdown Files: {self.stats['md_files']}\n")
            f.write(f"- Orphaned PDFs: {self.stats['orphaned_pdfs']}\n")
            f.write(f"- Orphaned Markdowns: {self.stats['orphaned_mds']}\n")
            f.write(f"- Invalid PDFs: {self.stats['invalid_pdfs']}\n")
            f.write(f"- Invalid Markdowns: {self.stats['invalid_mds']}\n")
            f.write(f"- Oversized Files: {self.stats['oversized_files']}\n")
            f.write("\n")
            
            f.write("---\n")
            f.write(f"*Generated: {Path.cwd()}*\n")
        
        print(f"✓ Report saved: {output_path}")

# ==========================
# MAIN
# ==========================
def main():
    parser = argparse.ArgumentParser(description="Repository Integrity Validator")
    parser.add_argument("--artifacts-dir", default=".github/artifacts")
    parser.add_argument("--output-report", default="validation_report.md")
    args = parser.parse_args()
    
    print(f"\n{'='*70}")
    print(f"Repository Integrity Validator")
    print(f"{'='*70}\n")
    
    try:
        config = ConfigLoader(args.artifacts_dir)
        print(f"✓ Config loaded\n")
    except Exception as e:
        print(f"ERROR: Config load failed: {e}")
        return 1
    
    try:
        validator = RepositoryValidator(config)
        has_issues, issues = validator.validate()
        
        print(f"\n{'='*70}")
        print(f"Validation Complete")
        print(f"{'='*70}\n")
        
        validator.generate_report(args.output_report)
        
        if has_issues:
            print(f"⚠️  Found {len(issues)} issues")
            print(f"✓ GitHub issue will be created/updated")
            return 0  # SUCCESS - issues found and reported
        else:
            print(f"✅ No issues found")
            return 0  # SUCCESS - clean validation
            
    except Exception as e:
        print(f"ERROR: Validation failed: {e}")
        return 1  # FAILURE - script error

if __name__ == "__main__":
    sys.exit(main())