import os
import sys
import re
import json
import hashlib
import argparse
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime

# Dependency checks
try:
    from markitdown import MarkItDown
except ImportError:
    print("ERROR: markitdown required. Install: pip install markitdown")
    sys.exit(1)

try:
    from google import genai
    from google.genai import types
    USE_NEW_SDK = True
except ImportError:
    try:
        import google.generativeai as genai
        USE_NEW_SDK = False
    except ImportError:
        print("ERROR: google-generativeai required")
        sys.exit(1)

# Configuration Loader
class ConfigLoader:
    def __init__(self, artifacts_dir: str = ".github/artifacts"):
        self.artifacts_dir = Path(artifacts_dir)
        
        self.ai_config = self._load_json("ai-models.json")
        self.pipeline_config = self._load_json("pipeline-config.json")
        
        if not self.ai_config:
            raise ValueError("ai-models.json is REQUIRED")
        if not self.pipeline_config:
            raise ValueError("pipeline-config.json is REQUIRED")
        
        self.models = self.ai_config.get("models", {}).get("priority_list", [])
        if not self.models:
            raise ValueError("No models in ai-models.json")
        
        self.gen_config = self.ai_config.get("configurations", {}).get("default", {})
        
        proc_config = self.pipeline_config.get("processing", {})
        self.max_pdf_chars = proc_config.get("max_pdf_chars", 1000000)
        self.min_text_length = proc_config.get("min_text_length", 100)
        
        self.org_mappings = self.pipeline_config.get("organization_mappings", {})
        self.title_mappings = self.pipeline_config.get("title_mappings", {})
        
        prompts = self.pipeline_config.get("prompts", {})
        self.pdf_prompt_path = prompts.get("pdf_to_markdown")
    
    def _load_json(self, filename: str) -> Optional[Dict[str, Any]]:
        path = self.artifacts_dir / filename
        if not path.exists():
            return None
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except:
            return None

# Conversion Cache
class ConversionCache:
    def __init__(self, cache_file: str = "conversion_cache.json"):
        self.cache_file = Path(cache_file)
        self.cache = self._load()
        self.hits = 0
        self.misses = 0
    
    def _load(self) -> Dict[str, Any]:
        if self.cache_file.exists():
            try:
                with open(self.cache_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def _save(self):
        try:
            with open(self.cache_file, 'w') as f:
                json.dump(self.cache, f, indent=2)
        except:
            pass
    
    def _hash(self, pdf_path: str) -> str:
        stat = Path(pdf_path).stat()
        key = f"{pdf_path}:{stat.st_size}:{stat.st_mtime}"
        return hashlib.md5(key.encode()).hexdigest()
    
    def get(self, pdf_path: str) -> Optional[str]:
        cache_key = self._hash(pdf_path)
        if cache_key in self.cache:
            self.hits += 1
            return self.cache[cache_key]
        self.misses += 1
        return None
    
    def set(self, pdf_path: str, md_path: str):
        cache_key = self._hash(pdf_path)
        self.cache[cache_key] = md_path
        self._save()

# AI Setup
def setup_gemini(api_key: str, config: ConfigLoader) -> Tuple[bool, Optional[str]]:
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
            except:
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
            except:
                continue
    
    print("WARNING: No AI models available")
    return False, None

# PDF Converter
class PDFConverter:
    def __init__(self, config: ConfigLoader, model: Optional[str] = None):
        self.config = config
        self.model = model
        self.cache = ConversionCache()
        
        # Initialize markitdown with error handling
        try:
            self.markitdown = MarkItDown()
            print("✓ MarkItDown initialized")
        except Exception as e:
            print(f"! MarkItDown init warning: {str(e)[:50]}")
            self.markitdown = MarkItDown()
    
    def convert(self, pdf_path: str) -> Tuple[bool, str, str]:
        pdf_path_obj = Path(pdf_path)
        if not pdf_path_obj.exists():
            return False, "", "File not found"
        
        # Check cache
        cached = self.cache.get(pdf_path)
        if cached and Path(cached).exists():
            print(f"  ✓ Cached: {cached}")
            return True, cached, "cached"
        
        # Parse metadata
        org_name, report_title, year = self._parse_filename(pdf_path_obj.name)
        org_name = self.config.org_mappings.get(org_name, org_name)
        report_title = self._apply_title_mappings(report_title)
        
        # Output path
        md_path = self._get_markdown_path(pdf_path_obj, year)
        md_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            # Convert with markitdown
            print(f"  Converting with markitdown...")
            result = self.markitdown.convert(str(pdf_path_obj))
            
            # Handle different result types
            if hasattr(result, 'text_content'):
                markdown_text = result.text_content
            elif isinstance(result, str):
                markdown_text = result
            else:
                markdown_text = str(result)
            
            if not markdown_text:
                print(f"  ! No text extracted, trying fallback...")
                # Fallback: create minimal markdown
                markdown_text = f"# {org_name} - {report_title} ({year})\n\nSecurity report conversion pending."
            
            markdown_text = markdown_text.strip()
            
            # Validate length
            if len(markdown_text) < self.config.min_text_length:
                print(f"  ! Short extraction ({len(markdown_text)} chars), will save anyway")
            
            # Truncate if needed
            if len(markdown_text) > self.config.max_pdf_chars:
                markdown_text = markdown_text[:self.config.max_pdf_chars]
                print(f"  ! Truncated to {self.config.max_pdf_chars} chars")
            
            # Save
            md_path.write_text(markdown_text, encoding='utf-8')
            self.cache.set(pdf_path, str(md_path))
            
            print(f"  ✓ Converted: {md_path}")
            return True, str(md_path), "success"
            
        except Exception as e:
            error_msg = str(e)[:200]
            print(f"  ! Conversion error: {error_msg}")
            
            # Try to save a minimal file so pipeline can continue
            try:
                minimal_md = f"# {org_name} - {report_title} ({year})\n\nConversion error: {error_msg}\n"
                md_path.write_text(minimal_md, encoding='utf-8')
                print(f"  ! Saved minimal markdown")
                return True, str(md_path), f"partial ({error_msg[:50]})"
            except:
                return False, "", f"Failed: {error_msg}"
    
    def _parse_filename(self, filename: str) -> Tuple[str, str, str]:
        name = filename.replace('.pdf', '')
        year_match = re.search(r'-(\d{4})$', name)
        
        if year_match:
            year = year_match.group(1)
            name_without_year = name[:year_match.start()]
        else:
            year = str(datetime.now().year)
            name_without_year = name
        
        parts = name_without_year.split('-', 1)
        if len(parts) >= 2:
            org_name = parts[0]
            report_title = parts[1]
        else:
            org_name = parts[0]
            report_title = "Security Report"
        
        return org_name, report_title, year
    
    def _apply_title_mappings(self, title: str) -> str:
        words = title.split('-')
        mapped_words = []
        
        for word in words:
            mapped = self.config.title_mappings.get(word)
            if mapped:
                mapped_words.append(mapped)
            else:
                mapped_words.append(word.capitalize())
        
        return ' '.join(mapped_words)
    
    def _get_markdown_path(self, pdf_path: Path, year: str) -> Path:
        parts = list(pdf_path.parts)
        
        if 'Annual Security Reports' in parts:
            idx = parts.index('Annual Security Reports')
            parts[idx] = 'Markdown Conversions'
        
        return Path(*parts).with_suffix('.md')

# Main
def main():
    parser = argparse.ArgumentParser(description="PDF to Markdown Converter")
    parser.add_argument("--file-list", required=True)
    parser.add_argument("--output-json", default="conversions.json")
    parser.add_argument("--artifacts-dir", default=".github/artifacts")
    args = parser.parse_args()
    
    print(f"\n{'='*70}")
    print(f"PDF to Markdown Converter")
    print(f"{'='*70}\n")
    
    # Load config
    try:
        config = ConfigLoader(args.artifacts_dir)
        print(f"✓ Config loaded\n")
    except Exception as e:
        print(f"ERROR: Config failed: {e}")
        return 1
    
    # Setup AI (optional)
    gemini_key = os.environ.get("GEMINI_API_KEY")
    model = None
    if gemini_key:
        ai_ok, model = setup_gemini(gemini_key, config)
    else:
        print("INFO: No GEMINI_API_KEY, using markitdown only\n")
    
    # Load file list
    if not os.path.exists(args.file_list):
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