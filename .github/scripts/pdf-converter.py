import os
import sys
import re
from pathlib import Path
from googleapiclient.discovery import build
import argparse
import json
from typing import List, Dict, Any, Optional
import time

# --- Dependency Handling ---
try:
    from markitdown import MarkItDown
except ImportError:
    print("ERROR: The 'markitdown' module is required but not installed.")
    print("Please install it using: pip install markitdown")
    sys.exit(1)

try:
    from google import genai
    from google.genai import types
    from google.api_core import exceptions
except ImportError:
    print("ERROR: The 'google-genai' module is required but not installed.")
    print("Please install the new SDK using: pip install google-genai")
    sys.exit(1)

# Configure Gemini API
def load_ai_config():
    try:
        config_path = Path(__file__).parent.parent / "artifacts" / "ai-models.json"
        with open(config_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Warning: Failed to load AI config: {e}. Using defaults.")
        return None

AI_CONFIG = load_ai_config()
MODELS = AI_CONFIG["models"]["priority_list"] if AI_CONFIG else ["gemini-2.0-flash", "gemini-1.5-flash", "gemini-1.5-pro"]

MODEL = None
CLIENT = None

def setup_gemini(api_key: str):
    global MODEL, CLIENT
    
    try:
        # Initialize the new Client
        CLIENT = genai.Client(api_key=api_key)
    except Exception as e:
        print(f"ERROR: Failed to initialize Gemini Client: {e}")
        return False

    for model_name in MODELS:
        try:
            # Verify model availability using count_tokens
            response = CLIENT.models.count_tokens(
                model=model_name,
                contents="Hello"
            )
            
            if response.total_tokens is not None:
                MODEL = model_name
                print(f"Successfully verified model: {MODEL}")
                break   
        except Exception as e:
            # Catching general exceptions as SDK specific exceptions might vary
            print(f"Model {model_name} verification failed: {e}")
            continue
            
    if not MODEL:
        print("ERROR: No models available. Check API key and quota.")
        return False
    return True

def read_prompt_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if not content:
                raise ValueError(f"Prompt file {path} is empty")
            return content
    except FileNotFoundError:
        print(f"ERROR: Prompt file not found: {path}")
        raise
    except Exception as e:
        print(f"ERROR: Failed to read prompt file {path}: {str(e)}")
        raise

def extract_text_from_pdf(pdf_path: Path, min_text_length: int = 100) -> str:
    """
    Extracts text from a PDF, attempting standard conversion first and
    falling back to OCR if the initial attempt yields insufficient content.
    """
    try:
        print(f"Extracting text from PDF: {pdf_path}")
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")

        file_size = pdf_path.stat().st_size
        print(f"PDF file size: {file_size / (1024*1024):.2f} MB")

        md = MarkItDown(enable_plugins=False)

        # --- 1. Attempt standard conversion ---
        print("Attempting standard text extraction...")
        result = md.convert(str(pdf_path))
        text_content = result.text_content if result else ""
        text_length = len(text_content)

        # --- 2. Check for failure and fallback to OCR ---
        if text_length < min_text_length:
            print(f"WARNING: Standard extraction yielded only {text_length} characters. Falling back to OCR.")
            ocr_result = md.convert(str(pdf_path), ocr=True)
            text_content = ocr_result.text_content if ocr_result else ""
            text_length = len(text_content)

        # --- 3. Final validation ---
        if text_length < min_text_length:
            raise ValueError(f"Both standard and OCR extraction failed. Only got {text_length} characters.")

        print(f"Successfully extracted {text_length} characters from PDF.")
        return text_content
    except Exception as e:
        print(f"ERROR: Failed to extract text from PDF {pdf_path}: {str(e)}")
        raise

def parse_filename_to_org_and_title(filename_stem: str) -> tuple[str, str]:
    """Parse filename to extract organization and title"""
    print(f"Parsing filename: {filename_stem}")
    
    # Special handling for known patterns
    filename_lower = filename_stem.lower()
    
    # General parsing - try different separators
    separators = [' - ', '_-_', '--', '_', '-'] # Added single hyphen
    for sep in separators:
        if sep in filename_stem:
            parts = filename_stem.split(sep, 1)
            if len(parts) == 2:
                org_part = parts[0].strip()
                title_part = parts[1].strip()
                
                # Clean organization name
                org_name = org_part.replace('_', ' ').replace('-', ' ')
                org_name = ' '.join(word.capitalize() for word in org_name.split())
                
                # Clean title
                title = title_part.replace('_', ' ').replace('-', ' ')
                title = ' '.join(word.capitalize() for word in title.split())
                
                # Remove year from title if present
                title = re.sub(r'\s*20\d{2}\s*', '', title).strip()

                # Sanity check to prevent org and title from being the same on a bad split
                if org_name.lower() == title.lower():
                    print(f"Parsing with '{sep}' resulted in identical org and title. Skipping.")
                    continue
                
                # Apply organization name mappings
                org_mapping = {
                    'Ai': 'AI',
                    'Cyberark': 'CyberArk',
                    'Sailpoint': 'SailPoint',
                    'Crowdstrike': 'CrowdStrike',
                    'Palo Alto': 'Palo Alto Networks',
                }
                
                for old_name, new_name in org_mapping.items():
                    if org_name.lower() == old_name.lower():
                        org_name = new_name
                        break

                # Apply title name mappings
                title_mapping = {
                    'Ai': 'AI',
                    'Api': 'API',
                    'Id': 'ID',
                    'Dns': 'DNS',
                    'Dos': 'DoS',
                    'Ddos': 'DDoS',
                    'Cve': 'CVE',
                }

                for old_title, new_title in title_mapping.items():
                    # Use regex to replace whole words, case-insensitively
                    title = re.sub(r'\b' + re.escape(old_title) + r'\b', new_title, title, flags=re.IGNORECASE)
                
                print(f"Parsed with separator '{sep}': Org='{org_name}', Title='{title}'")
                return org_name, title
    
    # Fallback: try to extract from the beginning
    words = filename_stem.replace('_', ' ').replace('-', ' ').split()
    if words:
        org_name = words[0].capitalize()
        if len(words) > 1:
            title = ' '.join(word.capitalize() for word in words[1:])
            # Remove year if present
            title = re.sub(r'\s*20\d{2}\s*', '', title).strip()
        else:
            title = "Security Report"
        
        print(f"Fallback parsing: Org='{org_name}', Title='{title}'")
        return org_name, title
    
    # Ultimate fallback
    return "Unknown Organization", "Security Report"

def get_organization_url(org_name: str, title: str, year: str) -> Optional[str]:
    """
    Performs an optimized Google search and returns the best URL.
    """
    api_key = os.environ.get("GOOGLE_SEARCH_API_KEY")
    cse_id = os.environ.get("GOOGLE_CSE_ID")

    if not api_key or not cse_id:
        print("Warning: GOOGLE_SEARCH_API_KEY or GOOGLE_CSE_ID not set. Skipping URL search.")
        return None

    # Use a less restrictive query without quotes for more flexible matching
    query = f'{org_name} {title} {year}'
    print(f"Performing Google Custom Search with query: {query}")

    try:
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=query, cx=cse_id, num=5).execute()

        items = res.get('items', [])
        if not items:
            print("No results found from Google Custom Search.")
            return None

        # --- Simplified Result Prioritization ---
        org_lower = org_name.lower()
        title_keywords = {word for word in re.findall(r'\b\w{4,}\b', title.lower())}
        results_urls = [item['link'] for item in items]

        # 1. High priority: URL contains org name and at least one significant title keyword
        for url in results_urls:
            url_lower = url.lower()
            if org_lower in url_lower and any(keyword in url_lower for keyword in title_keywords):
                print(f"Found high-priority match (org + title keyword): {url}")
                return url

        # 2. Medium priority: URL contains just the org name
        for url in results_urls:
            if org_lower in url.lower():
                print(f"Found medium-priority match (org name only): {url}")
                return url

        # 3. Fallback: Return the first result
        print(f"No specific match found, returning the first result: {results_urls[0]}")
        return results_urls[0]

    except Exception as e:
        print(f"An error occurred during Google search for query '{query}': {e}")
        # Return a fallback search URL instead of None to prevent downstream failures
        fallback_url = f"https://www.google.com/search?q={org_name.replace(' ', '+')}+{title.replace(' ', '+')}"
        print(f"Using fallback search URL: {fallback_url}")
        return fallback_url

def generate_markdown_with_ai(pdf_text: str, prompt_text: str, organization_url: Optional[str]) -> str:
    if not CLIENT or not MODEL:
        raise ValueError("Gemini Client or Model not initialized.")
    
    try:
        print(f"Generating markdown with {MODEL}...")
        
        # Truncate PDF text if too long
        max_pdf_chars = 1000000
        if len(pdf_text) > max_pdf_chars:
            print(f"Truncating PDF text from {len(pdf_text)} to {max_pdf_chars} characters")
            pdf_text = pdf_text[:max_pdf_chars] + "\n\n[Content truncated due to length...]"
        
        full_prompt = f"{prompt_text}\n\n"
        if organization_url:
            full_prompt += f"The official report URL is: {organization_url}\n\n"
        full_prompt += f"# Report Content Below\n\n{pdf_text}"
        
        gen_config = AI_CONFIG.get("configurations", {}).get("default", {}) if AI_CONFIG else {}

        # Configure generation parameters using the new SDK types
        config = types.GenerateContentConfig(
            temperature=gen_config.get("temperature", 0.1),
            max_output_tokens=gen_config.get("max_output_tokens", 8192),
            top_p=gen_config.get("top_p", 0.95),
            top_k=gen_config.get("top_k", 40),
            safety_settings=[
                types.SafetySetting(
                    category="HARM_CATEGORY_HARASSMENT",
                    threshold="BLOCK_ONLY_HIGH"
                ),
                types.SafetySetting(
                    category="HARM_CATEGORY_HATE_SPEECH",
                    threshold="BLOCK_ONLY_HIGH"
                ),
                types.SafetySetting(
                    category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    threshold="BLOCK_ONLY_HIGH"
                ),
                types.SafetySetting(
                    category="HARM_CATEGORY_DANGEROUS_CONTENT",
                    threshold="BLOCK_ONLY_HIGH"
                ),
            ],
            response_mime_type="text/plain"
        )
        
        # Call the API using the new Client structure
        # Note: request_options like timeout are handled via http_options if needed, 
        # or simplified in standard calls.
        response = CLIENT.models.generate_content(
            model=MODEL, 
            contents=full_prompt,
            config=config
        )

        if not response.text:
            # Check for safety blocks if text is empty
            if response.candidates and response.candidates[0].finish_reason:
                 raise ValueError(f"Content generation blocked: {response.candidates[0].finish_reason}")
            raise ValueError("The response did not contain valid text content.")

        generated_text = response.text.strip()
        if len(generated_text) < 100:
            raise ValueError("Generated markdown content is too short")

        print(f"Successfully generated markdown ({len(generated_text)} characters)")
        return generated_text
        
    except Exception as e:
        print(f"ERROR: Failed to generate markdown: {str(e)}")
        raise

def process_pdf(pdf_path: Path, prompt_path: str, prompt_version: str, branch: str) -> Dict[str, Any]:
    result_base = {
        "pdf_path": str(pdf_path),
        "model_used": MODEL,
        "prompt_version": prompt_version,
        "branch": branch
    }
    
    try:
        print(f"Processing: {pdf_path}")
        prompt_text = read_prompt_file(prompt_path)
        print(f"Loaded prompt file ({len(prompt_text)} characters)")
        
        pdf_text = extract_text_from_pdf(pdf_path)
        
        filename_stem = pdf_path.stem
        organization_name, report_title = parse_filename_to_org_and_title(filename_stem)
        
        print(f"Final parsed result: Organization='{organization_name}', Title='{report_title}'")

        # Extract year from path
        year = "Unknown"
        for part in pdf_path.parts:
            if part.isdigit() and len(part) == 4 and part.startswith("20"):
                year = part
                break
        
        # Search for organization URL
        organization_url = None
        if organization_name and report_title and year:
            organization_url = get_organization_url(organization_name, report_title, year)
                
        if not organization_url:
            # Ultimate fallback: construct a generic domain
            organization_url = f"https://www.{''.join(e for e in organization_name if e.isalnum()).lower()}.com"
            print(f"Ultimate fallback: constructed generic URL: {organization_url}")

        markdown_content = generate_markdown_with_ai(pdf_text, prompt_text, organization_url)
        
        # Post Processing Cleanup

        # 1. Remove markdown code block wrappers if AI incorrectly added them
        markdown_content = re.sub(r'^\s*```(?:markdown)?\s*\n', '', markdown_content, 1)
        markdown_content = re.sub(r'\n\s*```\s*$', '', markdown_content, 1)

        # 2. Fix: Remove prompt instructions if they leaked into the output
        marker = "# Report Content Below"
        if marker in markdown_content:
            print(f"Detected prompt leakage. Cleaning content above marker: '{marker}'")
            # Find the LAST instance of the marker (rfind) to ensure we get past all instructions
            last_index = markdown_content.rfind(marker)
            # Slice the content to start immediately after the marker
            markdown_content = markdown_content[last_index + len(marker):].strip()

        # Prepare output
        relative_path = pdf_path.relative_to(Path("Annual Security Reports"))
        output_dir = Path("Markdown Conversions") / relative_path.parent
        output_path = output_dir / f"{pdf_path.stem}.md"
        
        os.makedirs(output_dir, exist_ok=True)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)

        if not output_path.exists():
            raise RuntimeError(f"Failed to create output file: {output_path}")
        
        output_size = output_path.stat().st_size
        if output_size < 100:
            raise RuntimeError(f"Output file is too small: {output_path}")

        print(f"Successfully created: {output_path} ({output_size} bytes)")

        return {
            "status": "success",
            "output_path": str(output_path),
            "organization_url": organization_url,
            "organization_name": organization_name,
            "report_title": report_title,
            **result_base
        }
        
    except Exception as e:
        error_message = f"Failed to process {pdf_path}: {str(e)}"
        print(f"ERROR: {error_message}", file=sys.stderr)
        return {
            "status": "failed", 
            "reason": str(e),
            **result_base
        }

def main():
    parser = argparse.ArgumentParser(description="Convert PDF files to Markdown using AI.")
    parser.add_argument("files_list", help="Path to a file containing a list of PDF paths.")
    parser.add_argument("prompt_path", help="Path to the AI prompt file.")
    parser.add_argument("prompt_version", help="Version of the AI prompt.")
    parser.add_argument("branch", help="Current Git branch.")
    parser.add_argument("--output-json", help="Path to save the conversion results.", default="conversions.json")
    args = parser.parse_args()

    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        print("ERROR: GEMINI_API_KEY environment variable not set.")
        sys.exit(1)
    
    if not setup_gemini(gemini_api_key):
        sys.exit(1)

    try:
        with open(args.files_list, 'r') as f:
            pdf_paths = [Path(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        print(f"ERROR: Files list not found: {args.files_list}")
        sys.exit(1)

    if not pdf_paths:
        print("No files to process")
        sys.exit(0)

    results = []
    converted_output_paths = []
    
    for i, pdf_path in enumerate(pdf_paths, 1):
        print(f"\n=== Processing file {i}/{len(pdf_paths)} ===")
        result = process_pdf(pdf_path, args.prompt_path, args.prompt_version, args.branch)
        results.append(result)
        
        if result['status'] == 'success':
            converted_output_paths.append(result['output_path'])

    with open(args.output_json, 'w') as f:
        json.dump(results, f, indent=2)

    converted_files_path = os.environ.get("CONVERTED_FILES_PATH", "converted_files.txt")
    with open(converted_files_path, "w") as f:
        for path in converted_output_paths:
            f.write(f"{path}\n")

    success_count = len([r for r in results if r['status'] == 'success'])
    print(f"\nConversion completed: {success_count}/{len(results)} successful")

    return 0 if success_count > 0 else 1

if __name__ == "__main__":
    sys.exit(main())