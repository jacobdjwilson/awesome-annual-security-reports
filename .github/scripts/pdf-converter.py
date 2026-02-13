import os
import sys
import re
import json
import hashlib
import argparse
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime

# ==========================
# DEPENDENCY CHECKS
# ==========================
try:
    from markitdown import MarkItDown
except ImportError:
    print("ERROR: markitdown module required")
    print("Install: pip install markitdown")
    sys.exit(1)

try:
    from google import genai
    from google.genai import types
    USE_NEW_SDK = True
except ImportError:
    try:
        import google.generativeai as genai
        from google.api_core import exceptions
        USE_NEW_SDK = False
    except ImportError:
        print("ERROR: google-generativeai required")
        print("Install: pip install google-generativeai")
        sys.exit(1)

# ==========================
# CONFIGURATION LOADER
# ==========================
class ConfigLoader:
    """Loads configuration from .github/artifacts/"""
    
    def __init__(self, artifacts_dir: str = ".github/artifacts"):
        self.artifacts_dir = Path(artifacts_dir)
        
        self.ai_config = self._load_json("ai-models.json")
        self.pipeline_config = self._load_json("pipeline-config.json")
        
        if not self.ai_config:
            raise ValueError("ai-models.json is REQUIRED")
        if not self.pipeline_config:
            raise ValueError("pipeline-config.json is REQUIRED")
        
        # Extract AI config
        self.models = self.ai_config.get("models", {}).get("priority_list", [])
        if not self.models:
            raise ValueError("No models in ai-models.json")
        
        self.gen_config = self.ai_config.get("configurations", {}).get("default", {})
        
        # Extract pipeline config
        proc_config = self.pipeline_config.get("processing", {})
        self.max_pdf_chars = proc_config.get("max_pdf_chars", 1000000)
        self.min_text_length = proc_config.get("min_text_length", 100)
        
        self.org_mappings = self.pipeline_config.get("organization_mappings", {})
        self.title_mappings = self.pipeline_config.get("title_mappings", {})
        
        # Prompt paths
        prompts = self.pipeline_config.get("prompts", {})
        self.pdf_prompt_path = prompts.get("pdf_to_markdown")
        if not self.pdf_prompt_path:
            raise ValueError("pdf_to_markdown prompt path not in config")
    
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

# ==========================
# CONVERSION CACHE
# ==========================
class ConversionCache:
    """Cache for conversion results."""
    
    def __init__(self, cache_file: str = "conversion_cache.json"):
        self.cache_file = Path(cache_file)
        self.cache = self._load()
        self.hits = 0
        self.misses = 0
    
    def _load(self) -> Dict[str, Any]:
        """Load cache."""
        if self.cache_file.exists():
            try:
                with open(self.cache_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def _save(self):
        """Save cache."""
        try:
            with open(self.cache_file, 'w') as f:
                json.dump(self.cache, f, indent=2)
        except:
            pass
    
    def _hash(self, pdf_path: str) -> str:
        """Generate hash for PDF."""
        stat = Path(pdf_path).stat()
        key = f"{pdf_path}:{stat.st_size}:{stat.st_mtime}"
        return hashlib.md5(key.encode()).hexdigest()
    
    def get(self, pdf_path: str) -> Optional[str]:
        """Get cached conversion."""
        cache_key = self._hash(pdf_path)
        if cache_key in self.cache:
            self.hits += 1
            return self.cache[cache_key]
        self.misses += 1
        return None
    
    def set(self, pdf_path: str, md_path: str):
        """Cache conversion."""
        cache_key = self._hash(pdf_path)
        self.cache[cache_key] = md_path
        self._save()

# ==========================
# AI SETUP
# ==========================
def setup_gemini(api_key: str, config: ConfigLoader) -> Tuple[bool, Optional[str]]:
    """Setup Gemini."""
    
    if USE_NEW_SDK:
        client = genai.Client(api_key=api_key)
        for model_name in config.models:
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents="test"
                )
                if response.text:
                    print(f"✓ AI Model: {model_name}")
                    return True, model_name
            except Exception:
                continue
    else:
        genai.configure(api_key=api_key)
        for model_name in config.models:
            try:
                test_model = genai.GenerativeModel(model_name)
                test_response = test_model.count_tokens("test")
                if test_response.total_tokens:
                    print(f"✓ AI Model: {model_name}")
                    return True, model_name
            except Exception:
                continue
    
    print("WARNING: No AI models available")
    return False, None

# ==========================
# PDF CONVERTER
# ==========================
class PDFConverter:
    """Converts PDFs to Markdown using markitdown."""
    
    def __init__(self, config: ConfigLoader, model: Optional[str] = None):
        self.config = config
        self.model = model
        self.markitdown = MarkItDown()
        self.cache = ConversionCache()
    
    def convert(self, pdf_path: str) -> Tuple[bool, str, str]:
        """
        Convert PDF to Markdown.
        Returns: (success, md_path, message)
        """
        
        pdf_path_obj = Path(pdf_path)
        if not pdf_path_obj.exists():
            return False, "", "File not found"
        
        # Check cache
        cached = self.cache.get(pdf_path)
        if cached and Path(cached).exists():
            print(f"  ✓ Cached: {cached}")
            return True, cached, "cached"
        
        # Extract metadata
        org_name, report_title, year = self._parse_filename(pdf_path_obj.name)
        
        # Apply mappings
        org_name = self.config.org_mappings.get(org_name, org_name)
        report_title = self._apply_title_mappings(report_title)
        
        # Construct output path
        md_path = self._get_markdown_path(pdf_path_obj, year)
        md_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            # Convert with markitdown
            print(f"  Converting with markitdown...")
            result = self.markitdown.convert(str(pdf_path_obj))
            
            if not result or not result.text_content:
                return False, "", "No text extracted"
            
            markdown_text = result.text_content.strip()
            
            # Validate length
            if len(markdown_text) < self.config.min_text_length:
                return False, "", f"Too short ({len(markdown_text)} chars)"
            
            # Truncate if needed
            if len(markdown_text) > self.config.max_pdf_chars:
                markdown_text = markdown_text[:self.config.max_pdf_chars]
                print(f"  ! Truncated to {self.config.max_pdf_chars} chars")
            
            # Optional: Enhance with AI (only if available and needed)
            if self.model and len(markdown_text) < 500:
                print(f"  Enhancing with AI...")
                markdown_text = self._enhance_with_ai(markdown_text, org_name, report_title, year)
            
            # Save
            md_path.write_text(markdown_text, encoding='utf-8')
            
            # Cache
            self.cache.set(pdf_path, str(md_path))
            
            print(f"  ✓ Converted: {md_path}")
            return True, str(md_path), "success"
            
        except Exception as e:
            return False, "", f"Conversion error: {str(e)[:100]}"
    
    def _parse_filename(self, filename: str) -> Tuple[str, str, str]:
        """Parse Organization-Title-Year.pdf"""
        name = filename.replace('.pdf', '')
        
        # Extract year
        year_match = re.search(r'-(\d{4})$', name)
        if year_match:
            year = year_match.group(1)
            name_without_year = name[:year_match.start()]
        else:
            year = str(datetime.now().year)
            name_without_year = name
        
        # Split org and title
        parts = name_without_year.split('-', 1)
        if len(parts) >= 2:
            org_name = parts[0]
            report_title = parts[1]
        else:
            org_name = parts[0]
            report_title = "Security Report"
        
        return org_name, report_title, year
    
    def _apply_title_mappings(self, title: str) -> str:
        """Apply title case mappings."""
        words = title.split('-')
        mapped_words = []
        
        for word in words:
            # Check if mapping exists (case-insensitive)
            mapped = self.config.title_mappings.get(word)
            if mapped:
                mapped_words.append(mapped)
            else:
                # Capitalize first letter
                mapped_words.append(word.capitalize())
        
        return ' '.join(mapped_words)
    
    def _get_markdown_path(self, pdf_path: Path, year: str) -> Path:
        """Construct markdown output path."""
        # Replace 'Annual Security Reports' with 'Markdown Conversions'
        parts = list(pdf_path.parts)
        
        # Find and replace root directory
        if 'Annual Security Reports' in parts:
            idx = parts.index('Annual Security Reports')
            parts[idx] = 'Markdown Conversions'
        
        # Change extension
        md_path = Path(*parts).with_suffix('.md')
        
        return md_path
    
    def _enhance_with_ai(self, text: str, org: str, title: str, year: str) -> str:
        """Optional AI enhancement for very short extractions."""
        if not self.model:
            return text
        
        try:
            # Load prompt
            if not os.path.exists(self.config.pdf_prompt_path):
                return text
            
            with open(self.config.pdf_prompt_path, 'r') as f:
                prompt = f.read()
            
            full_prompt = f"{prompt}\n\nOrg: {org}\nTitle: {title}\nYear: {year}\n\n{text}"
            
            if USE_NEW_SDK:
                client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
                response = client.models.generate_content(
                    model=self.model,
                    contents=full_prompt,
                    config=types.GenerateContentConfig(
                        temperature=self.config.gen_config.get("temperature", 0.7),
                        max_output_tokens=2000
                    )
                )
            else:
                model_obj = genai.GenerativeModel(self.model)
                response = model_obj.generate_content(
                    full_prompt,
                    generation_config={
                        "temperature": self.config.gen_config.get("temperature", 0.7),
                        "max_output_tokens": 2000
                    }
                )
            
            if response.text:
                return response.text.strip()
            
        except Exception as e:
            print(f"  ! AI enhancement failed: {str(e)[:50]}")
        
        return text

# ==========================
# MAIN
# ==========================
def main():
    parser = argparse.ArgumentParser(description="PDF to Markdown Converter")
    parser.add_argument("--file-list", help="File containing list of PDFs to process")
    parser.add_argument("--output-json", default="conversions.json")
    parser.add_argument("--artifacts-dir", default=".github/artifacts")
    args = parser.parse_args()
    
    print(f"\n{'='*70}")
    print(f"PDF to Markdown Converter")
    print(f"{'='*70}\n")
    
    # Load config
    try:
        config = ConfigLoader(args.artifacts_dir)
        print(f"✓ Config loaded")
    except Exception as e:
        print(f"ERROR: Config failed: {e}")
        return 1
    
    # Setup AI (optional)
    gemini_key = os.environ.get("GEMINI_API_KEY")
    model = None
    if gemini_key:
        ai_ok, model = setup_gemini(gemini_key, config)
        if not ai_ok:
            print("WARNING: AI not available, using markitdown only")
    else:
        print("INFO: No GEMINI_API_KEY, using markitdown only")
    
    # Load file list
    if not args.file_list or not os.path.exists(args.file_list):
        print(f"ERROR: File list not found: {args.file_list}")
        return 1
    
    with open(args.file_list, 'r') as f:
        pdf_files = [line.strip() for line in f if line.strip()]
    
    if not pdf_files:
        print("No files to process")
        with open(args.output_json, 'w') as f:
            json.dump([], f)
        return 0
    
    print(f"✓ {len(pdf_files)} files to convert\n")
    
    # Convert
    converter = PDFConverter(config, model)
    results = []
    
    for i, pdf_path in enumerate(pdf_files, 1):
        print(f"[{i}/{len(pdf_files)}] {Path(pdf_path).name}")
        
        success, md_path, message = converter.convert(pdf_path)
        
        # Parse metadata for result
        org_name, report_title, year = converter._parse_filename(Path(pdf_path).name)
        org_name = config.org_mappings.get(org_name, org_name)
        report_title = converter._apply_title_mappings(report_title)
        
        result = {
            'pdf_path': pdf_path,
            'output_path': md_path if success else '',
            'status': 'success' if success else 'failed',
            'message': message,
            'organization_name': org_name,
            'report_title': report_title,
            'year': year
        }
        
        results.append(result)
    
    # Save results
    with open(args.output_json, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Summary
    successful = len([r for r in results if r['status'] == 'success'])
    
    print(f"\n{'='*70}")
    print(f"Converted: {successful}/{len(results)}")
    
    if converter.cache.hits + converter.cache.misses > 0:
        rate = (converter.cache.hits / (converter.cache.hits + converter.cache.misses) * 100)
        print(f"Cache: {converter.cache.hits} hits, {converter.cache.misses} misses ({rate:.1f}%)")
    
    print(f"\n✓ Results: {args.output_json}")
    
    return 0 if successful > 0 else 1

if __name__ == "__main__":
    sys.exit(main())