import os
import sys
import google.generativeai as genai
from pathlib import Path
import subprocess
from markitdown import MarkItDown
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import argparse
import json
from typing import List, Dict, Any, Optional

# Configure Gemini API
MODELS = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash"]
MODEL = None

def setup_gemini(api_key: str):
    global MODEL
    genai.configure(api_key=api_key)
    for model_name in MODELS:
        try:
            test_model = genai.GenerativeModel(model_name)
            test_response = test_model.generate_content("Hello", generation_config={"max_output_tokens": 10})
            if test_response and test_response.text:
                MODEL = model_name
                print(f"Successfully verified model: {MODEL}")
                break
        except Exception as e:
            print(f"Model {model_name} not available or failed verification: {str(e)}")
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

def extract_text_from_pdf(pdf_path: Path) -> str:
    try:
        print(f"Extracting text from PDF: {pdf_path}")
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        # Check file size
        file_size = pdf_path.stat().st_size
        print(f"PDF file size: {file_size / (1024*1024):.2f} MB")
        
        md = MarkItDown(enable_plugins=False)
        result = md.convert(str(pdf_path))
        
        if not result or not result.text_content:
            raise ValueError("MarkItDown returned empty content")
        
        text_length = len(result.text_content)
        print(f"Successfully extracted {text_length} characters from PDF")
        
        # Basic validation of extracted content
        if text_length < 100:
            print("WARNING: Extracted text is very short, PDF might be image-based or corrupted")
        
        return result.text_content
    except Exception as e:
        print(f"ERROR: Failed to extract text from PDF {pdf_path}: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        raise

def perform_google_search(query: str, api_key: str, cse_id: str) -> Optional[str]:
    if not api_key or not cse_id:
        print("Google Search API credentials not provided")
        return None
    
    try:
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=query, cx=cse_id, num=10).execute()
        
        if 'items' in res and len(res['items']) > 0:
            # Filter out PDF links, media articles, and prefer official organization sites
            for item in res['items']:
                url = item['link']
                title = item.get('title', '').lower()
                snippet = item.get('snippet', '').lower()
                
                # Skip PDF links and media articles
                if url.endswith('.pdf') or any(x in url.lower() for x in ['/media/', '/news/', '/press-release', '/blog/', 'linkedin', 'twitter', 'facebook']):
                    continue
                    
                # Skip third-party sites that just mention the report
                if any(x in url.lower() for x in ['cybersecuritynews', 'darkreading', 'securityweek', 'infosecurity-magazine', 'techrepublic', 'zdnet']):
                    continue
                
                # Prefer official organization sites (domains that contain the org name or are well-known)
                print(f"Found potential URL: {url}")
                return url
            
            # If no good match found, return the first result that isn't blocked
            for item in res['items']:
                url = item['link']
                if not url.endswith('.pdf'):
                    print(f"Using fallback URL: {url}")
                    return url
        
        return None
    except HttpError as e:
        print(f"Google Search API error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during Google Search: {e}")
        return None

def generate_markdown_with_ai(pdf_text: str, prompt_text: str, organization_url: Optional[str]) -> str:
    if not MODEL:
        raise ValueError("No available Gemini model.")
    
    try:
        print(f"Generating markdown with {MODEL}...")
        model = genai.GenerativeModel(MODEL)
        
        # Truncate PDF text if too long (keep within token limits)
        max_pdf_chars = 100000  # Approximately 25k tokens
        if len(pdf_text) > max_pdf_chars:
            print(f"Truncating PDF text from {len(pdf_text)} to {max_pdf_chars} characters")
            pdf_text = pdf_text[:max_pdf_chars] + "\n\n[Content truncated due to length...]"
        
        full_prompt = f"{prompt_text}\n\n"
        if organization_url:
            full_prompt += f"The official report URL is: {organization_url}\n\n"
        full_prompt += f"# Report Content Below\n\n{pdf_text}"
        
        generation_config = {
            "temperature": 0.1,
            "max_output_tokens": 8192,
            "top_p": 0.95,
            "top_k": 40
        }
        
        # Add safety settings to be more permissive for business content
        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_ONLY_HIGH"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_ONLY_HIGH"},
        ]
        
        response = model.generate_content(
            full_prompt, 
            generation_config=generation_config,
            safety_settings=safety_settings
        )

        # Enhanced error handling and logging
        if response.prompt_feedback:
            print(f"Prompt feedback: {response.prompt_feedback}")
            if hasattr(response.prompt_feedback, 'block_reason') and response.prompt_feedback.block_reason:
                raise ValueError(f"Request blocked: {response.prompt_feedback.block_reason}")

        if response.candidates:
            for i, candidate in enumerate(response.candidates):
                print(f"Candidate {i} finish reason: {candidate.finish_reason}")
                if candidate.safety_ratings:
                    print(f"Candidate {i} safety ratings: {candidate.safety_ratings}")
                
                # Check for content filtering
                if candidate.finish_reason == "SAFETY":
                    raise ValueError(f"Content generation blocked due to safety filters")
                elif candidate.finish_reason == "RECITATION":
                    raise ValueError(f"Content generation blocked due to recitation concerns")
        
        if not response.text:
            error_message = "The response did not contain valid text content."
            if response.candidates and response.candidates[0].finish_reason:
                error_message += f" Finish reason: {response.candidates[0].finish_reason}."
            if response.candidates and response.candidates[0].safety_ratings:
                error_message += f" Safety ratings: {response.candidates[0].safety_ratings}."
            raise ValueError(error_message)

        generated_text = response.text.strip()
        if len(generated_text) < 100:
            raise ValueError("Generated markdown content is too short - possible generation issue")

        print(f"Successfully generated markdown ({len(generated_text)} characters)")
        return generated_text
        
    except Exception as e:
        print(f"ERROR: Failed to generate markdown with AI: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        raise

def process_pdf(pdf_path: Path, prompt_path: str, prompt_version: str, branch: str, google_search_api_key: Optional[str], google_cse_id: Optional[str]) -> Dict[str, Any]:
    result_base = {
        "pdf_path": str(pdf_path),
        "model_used": MODEL,
        "prompt_version": prompt_version,
        "branch": branch
    }
    
    try:
        print(f"Processing: {pdf_path} (Branch: {branch})")
        
        # Validate inputs
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        # Read and validate prompt
        prompt_text = read_prompt_file(prompt_path)
        print(f"Loaded prompt file ({len(prompt_text)} characters)")
        
        # Extract text from PDF
        pdf_text = extract_text_from_pdf(pdf_path)
        
        # Parse filename for organization and title
        filename_stem = pdf_path.stem
        parts = filename_stem.split(' - ', 1)
        organization_name = parts[0].strip() if len(parts) > 0 else ""
        report_title = parts[1].strip() if len(parts) > 1 else filename_stem
        
        print(f"Organization: {organization_name}")
        print(f"Report Title: {report_title}")
        
        # Try to find organization URL
        organization_url = None
        if google_search_api_key and google_cse_id and organization_name:
            search_queries = [
                f"{organization_name} {report_title} report",
                f"{organization_name} official website reports",
                f"{organization_name} cybersecurity report",
                f"site:{organization_name.lower().replace(' ', '')}.com {report_title}",
                f"{organization_name} official site"
            ]
            
            for query in search_queries:
                print(f"Searching: '{query}'")
                organization_url = perform_google_search(query, google_search_api_key, google_cse_id)
                if organization_url:
                    print(f"Found organization URL: {organization_url}")
                    break
            
            if not organization_url:
                print("No suitable organization URL found via search")
        else:
            print("Google Search API keys not provided or organization name missing")

        # Generate markdown
        markdown_content = generate_markdown_with_ai(pdf_text, prompt_text, organization_url)
        
        # Prepare output path
        relative_path = pdf_path.relative_to(Path("Annual Security Reports"))
        output_dir = Path("Markdown Conversions") / relative_path.parent
        output_path = output_dir / f"{pdf_path.stem}.md"
        
        print(f"Writing output to: {output_path}")
        os.makedirs(output_dir, exist_ok=True)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)

        # Verify file was created and has content
        if not output_path.exists():
            raise RuntimeError(f"Failed to create output file: {output_path}")
        
        output_size = output_path.stat().st_size
        if output_size < 100:
            raise RuntimeError(f"Output file is too small ({output_size} bytes): {output_path}")

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
            "error_type": type(e).__name__,
            **result_base
        }

def main():
    parser = argparse.ArgumentParser(description="Convert PDF files to Markdown using AI.")
    parser.add_argument("files_list", help="Path to a file containing a list of PDF paths.")
    parser.add_argument("prompt_path", help="Path to the AI prompt file.")
    parser.add_argument("prompt_version", help="Version of the AI prompt.")
    parser.add_argument("branch", help="Current Git branch.")
    parser.add_argument("--output-json", help="Path to save the conversion results as a JSON file.", default="conversions.json")
    args = parser.parse_args()

    # Validate environment
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        print("ERROR: GEMINI_API_KEY environment variable not set.")
        sys.exit(1)
    
    if not setup_gemini(gemini_api_key):
        print("ERROR: Failed to setup Gemini API")
        sys.exit(1)

    google_search_api_key = os.environ.get("GOOGLE_SEARCH_API_KEY")
    google_cse_id = os.environ.get("GOOGLE_CSE_ID")

    # Read files to process
    try:
        with open(args.files_list, 'r') as f:
            pdf_paths = [Path(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        print(f"ERROR: Files list not found: {args.files_list}")
        sys.exit(1)

    if not pdf_paths:
        print("No files to process")
        sys.exit(0)

    print(f"Processing {len(pdf_paths)} PDF files...")

    results = []
    converted_output_paths = []
    
    for i, pdf_path in enumerate(pdf_paths, 1):
        print(f"\n=== Processing file {i}/{len(pdf_paths)} ===")
        result = process_pdf(pdf_path, args.prompt_path, args.prompt_version, args.branch, google_search_api_key, google_cse_id)
        results.append(result)
        
        if result['status'] == 'success':
            converted_output_paths.append(result['output_path'])
            print(f"SUCCESS: {pdf_path.name}")
        else:
            print(f"FAILED: {pdf_path.name} - {result.get('reason', 'Unknown error')}")

    # Save results
    with open(args.output_json, 'w') as f:
        json.dump(results, f, indent=2)

    # Create converted files list
    converted_files_path = os.environ.get("CONVERTED_FILES_PATH", "converted_files.txt")
    with open(converted_files_path, "w") as f:
        for path in converted_output_paths:
            f.write(f"{path}\n")

    success_count = len([r for r in results if r['status'] == 'success'])
    failure_count = len(results) - success_count
    
    print(f"\n=== CONVERSION SUMMARY ===")
    print(f"Total files: {len(results)}")
    print(f"Successful: {success_count}")
    print(f"Failed: {failure_count}")
    
    if failure_count > 0:
        print("\nFailed conversions:")
        for result in results:
            if result['status'] == 'failed':
                print(f"  - {Path(result['pdf_path']).name}: {result.get('reason', 'Unknown error')}")

    return 0 if success_count > 0 else 1

if __name__ == "__main__":
    sys.exit(main())