#!/usr/bin/env python3
import os
import sys
import re
import json
import google.generativeai as genai
from pathlib import Path
import subprocess
from markitdown import MarkItDown
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Setup Gemini API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Print available models for debugging
def list_available_models():
    try:
        print("Attempting to list available models...")
        models = genai.list_models()
        print("Available models:")
        for model in models:
            print(f"- {model.name}")
        return models
    except Exception as e:
        print(f"Error listing models: {str(e)}")
        return []

# List available models
available_models = list_available_models()

# Define models to try in order of preference - using currently available models
MODELS = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash"]

# Get the first available model
MODEL = None
for model in MODELS:
    try:
        print(f"Attempting to use model: {model}")
        test_model = genai.GenerativeModel(model)
        # Test a simple generation to verify it works
        test_response = test_model.generate_content("Hello")
        MODEL = model
        print(f"Successfully verified model: {MODEL}")
        break
    except Exception as e:
        print(f"Model {model} not available or failed verification: {str(e)}")
        continue

if not MODEL:
    print("No models available. Exiting.")
    sys.exit(1)

def read_prompt_file(path):
    try:
        with open(path, "r") as file:
            return file.read()
    except Exception as e:
        print(f"Error reading prompt file: {str(e)}")
        sys.exit(1)

def extract_text_from_pdf(pdf_path):
    try:
        # Use markitdown to extract text from PDF
        print(f"Extracting text from PDF: {pdf_path}")
        md = MarkItDown(enable_plugins=False)
        result = md.convert(str(pdf_path))
        text_length = len(result.text_content)
        print(f"Successfully extracted {text_length} characters from PDF")
        return result.text_content
    except Exception as e:
        print(f"Error extracting text from PDF: {str(e)}")
        raise

def perform_google_search(organization_name, report_title, pdf_path, api_key, cse_id):
    """
    Performs a Google Custom Search to find the official report URL,
    excluding direct PDF links, CDNs, and media outlets.
    """
    try:
        service = build("customsearch", "v1", developerKey=api_key)

        # Extract year from pdf_path
        year_match = re.search(r'Annual Security Reports/(\d{4})/', str(pdf_path))
        year = year_match.group(1) if year_match else ""

        # Derive main domain from organization name for site-specific search
        # Simple heuristic: remove spaces and common suffixes, then add .com
        # This might need more sophisticated logic for edge cases
        derived_domain = ""
        if organization_name:
            # Basic cleaning and domain inference
            cleaned_name = re.sub(r'[^a-zA-Z0-9]', '', organization_name).lower()
            if "security" in cleaned_name:
                cleaned_name = cleaned_name.replace("security", "")
            if "inc" in cleaned_name:
                cleaned_name = cleaned_name.replace("inc", "")
            if "corp" in cleaned_name:
                cleaned_name = cleaned_name.replace("corp", "")
            
            # Attempt to find a common domain for known organizations
            domain_map = {
                "guidepoint": "guidepointsecurity.com",
                # Add more mappings as needed
            }
            derived_domain = domain_map.get(cleaned_name, f"{cleaned_name}.com")
            
            # Fallback if the derived domain seems too generic or short
            if len(derived_domain) < 10 and "." not in derived_domain: # Heuristic for potentially bad domain
                derived_domain = "" # Don't use a potentially bad domain filter

        # Construct the search query
        search_query = f'"{organization_name} {report_title} {year} report" -inurl:pdf'
        if derived_domain:
            search_query += f' site:{derived_domain}'
        
        print(f"Performing Google search for: '{search_query}'")

        # Fetch multiple results to filter
        res = service.cse().list(q=search_query, cx=cse_id, num=5).execute() # Fetch up to 5 results

        if 'items' in res and len(res['items']) > 0:
            for item in res['items']:
                link = item['link']
                # Exclude known CDN/media patterns (can be expanded)
                if not re.search(r'\.(cdn|media|assets)\.', link, re.IGNORECASE) and \
                   not re.search(r'(\.(pdf|doc|docx))$', link, re.IGNORECASE) and \
                   not re.search(r'(issuu\.com|slideshare\.net|scmagazine\.com|darkreading\.com)', link, re.IGNORECASE):
                    print(f"Google Search found suitable URL: {link}")
                    return link
            print("No suitable Google search results found after filtering.")
            return None
        else:
            print("No Google search results found.")
            return None
    except HttpError as e:
        print(f"Google Search API error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during Google Search: {e}")
        return None
def generate_markdown_with_ai(pdf_text, prompt_text, organization_url=None):
    try:
        print(f"Generating markdown with {MODEL}...")
        model = genai.GenerativeModel(MODEL)
        
        full_prompt = f"{prompt_text}\n\n"
        if organization_url:
            full_prompt += f"The official report URL is: {organization_url}\n\n"
        full_prompt += f"# Report Content Below\n\n{pdf_text}"
        
        # Set generation parameters for better output
        generation_config = {
            "temperature": 0.2,  # Lower temperature for more predictable output
            "max_output_tokens": 8192,
        }
        
        response = model.generate_content(
            full_prompt,
            generation_config=generation_config
        )
        
        # Log prompt feedback
        if response.prompt_feedback:
            print(f"Prompt feedback: {response.prompt_feedback}")

        # Log candidate details for debugging
        if response.candidates:
            for i, candidate in enumerate(response.candidates):
                print(f"Candidate {i} finish reason: {candidate.finish_reason}")
                if candidate.safety_ratings:
                    print(f"Candidate {i} safety ratings: {candidate.safety_ratings}")
        
        if not response.text:
            error_message = "The `response.text` quick accessor requires the response to contain a valid `Part`, but none were returned."
            if response.candidates and response.candidates[0].finish_reason:
                error_message += f" The candidate's finish_reason is {response.candidates[0].finish_reason}."
            if response.candidates and response.candidates[0].safety_ratings:
                error_message += f" Safety ratings: {response.candidates[0].safety_ratings}."
            raise ValueError(error_message)

        print(f"Successfully generated markdown ({len(response.text)} characters)")
        return response.text
    except Exception as e:
        print(f"Error generating markdown with AI: {str(e)}")
        raise

def process_pdf(pdf_path, prompt_path, prompt_version, branch):
    """Process a PDF file and convert it to markdown
    
    Args:
        pdf_path: Path to the PDF file
        prompt_path: Path to the prompt file
        prompt_version: Version of the prompt
        branch: Current branch (main or development)
        
    Returns:
        bool: True if successful, False otherwise
    """
    print(f"Processing: {pdf_path} (Branch: {branch})")
    
    # Read the prompt from repository
    prompt_text = read_prompt_file(prompt_path)
    print(f"Loaded prompt file ({len(prompt_text)} characters)")
    
    # Extract text from PDF using markitdown
    pdf_text = extract_text_from_pdf(pdf_path)
    
    # Extract organization and title from PDF filename
    # Example: Annual Security Reports/2024/Varonis - The Identity Crisis 2024.pdf
    # Organization: Varonis
    # Title: The Identity Crisis 2024
    filename_stem = pdf_path.stem
    name_parts = filename_stem.split('-')
    organization_name = name_parts[0].strip()
    
    # The last part is the year, so the report title is everything in between
    year_part = name_parts[-1]
    if year_part.isdigit() and len(year_part) == 4:
        report_title_parts = name_parts[1:-1]
        report_title = ' '.join(report_title_parts).strip()
    else:
        report_title_parts = name_parts[1:]
        report_title = ' '.join(report_title_parts).strip()
    
    # Perform Google Search for the official report URL
    google_search_api_key = os.environ.get("GOOGLE_SEARCH_API_KEY")
    google_cse_id = os.environ.get("GOOGLE_CSE_ID")
    organization_url = None
    
    if google_search_api_key and google_cse_id:
        organization_url = perform_google_search(organization_name, report_title, pdf_path, google_search_api_key, google_cse_id)
    else:
        print("Google Search API keys not provided. Skipping URL search.")
    
    # Generate markdown with Gemini, passing the organization URL
    markdown_content = generate_markdown_with_ai(pdf_text, prompt_text, organization_url)
    
    # Determine the output path that matches the input directory structure
    # e.g., Annual Security Reports/2025/file.pdf -> Markdown Conversions/2025/file.md
    relative_path = pdf_path.relative_to(Path("Annual Security Reports"))
    output_dir = Path("Markdown Conversions") / relative_path.parent
    output_path = output_dir / f"{pdf_path.stem}.md"
    
    print(f"Writing output to: {output_path}")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Write the markdown content to file, overwriting if it already exists
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    
    # Check if file was created or updated
    if not output_path.exists():
        print(f"Error: Failed to create {output_path}")
        return {"pdf_path": str(pdf_path), "output_path": "", "model_used": MODEL, "status": "Failed: Output file not created"}
        
    print(f"Created/Updated: {output_path}")
    
    # Commit the file
    try:
        # Add the file
        subprocess.run(["git", "config", "user.name", "GitHub Action"], check=True)
        subprocess.run(["git", "config", "user.email", "action@github.com"], check=True)
        subprocess.run(["git", "add", str(output_path)], check=True)
        
        # Check if file is modified or new
        status_result = subprocess.run(
            ["git", "status", "--porcelain", str(output_path)], 
            capture_output=True, 
            text=True
        )
        
        if status_result.returncode != 0:
            print(f"Warning: Git status check failed: {status_result.stderr}")
            action = "Updated"
        else:
            status = status_result.stdout.strip()
            action = "📝 Updated" if status.startswith("M") else "✨ Created"
        
        # Commit the file
        commit_message = f"{action} {output_path.name} from {pdf_path.name} using AI Prompt {prompt_version} (Model {MODEL}, Branch {branch})"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print(f"Committed changes: {commit_message}")
        return {
            "pdf_path": str(pdf_path),
            "output_path": str(output_path),
            "model_used": MODEL,
            "status": "Converted Successfully",
            "organization_url": organization_url # Include organization URL
        }
    except Exception as e:
        print(f"Error during git operations: {str(e)}")
        return {
            "pdf_path": str(pdf_path),
            "output_path": "", # No output path if failed
            "model_used": MODEL,
            "status": f"Failed: {str(e)}",
            "organization_url": organization_url # Include organization URL even on failure
        }

def main():
    if len(sys.argv) < 5:
        print("Usage: python pdf-converter.py <pdf_paths_file> <prompt_path> <prompt_version> <branch>")
        return 1
    
    pdf_paths_file = sys.argv[1]
    prompt_path = sys.argv[2]
    prompt_version = sys.argv[3]
    branch = sys.argv[4]
    
    # Read PDF paths
    with open(pdf_paths_file, "r") as f:
        pdf_paths = [line.strip() for line in f.readlines() if line.strip()]
    
    print(f"Processing {len(pdf_paths)} PDF files on branch {branch}")
    
    success_count = 0
    all_results = [] # Initialize all_results list
    
    # Process each PDF
    for pdf_path_str in pdf_paths:
        pdf_path = Path(pdf_path_str)
        try:
            result = process_pdf(pdf_path, prompt_path, prompt_version, branch)
            all_results.append(result)
            if result["status"] == "Converted Successfully":
                success_count += 1
        except Exception as e:
            print(f"Error processing {pdf_path}: {str(e)}")
            all_results.append({
                "pdf_path": str(pdf_path),
                "output_path": "",
                "model_used": MODEL,
                "status": f"Failed: {str(e)}",
                "organization_url": None # No organization URL on processing failure
            })
    
    print(f"Successfully processed {success_count}/{len(pdf_paths)} PDFs")
    
    # Write results to a JSON file for the next workflow
    output_json_path = os.environ.get("CONVERTED_REPORTS_JSON_PATH", "converted_reports.json")
    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2)
    print(f"Wrote conversion results to {output_json_path}")

    # Generate and write summary to GITHUB_STEP_SUMMARY
    summary_path = os.environ.get('GITHUB_STEP_SUMMARY', 'summary.md')
    with open(summary_path, 'a', encoding='utf-8') as f:
        f.write("## ⚙️ PDF to Markdown Conversion Summary\n\n")
        f.write("| PDF File | Markdown Output | Model Used | Status | Organization URL |\n")
        f.write("|----------|-----------------|------------|--------|------------------|\n")
        for result in all_results:
            status_icon = "✅" if result['status'] == 'Converted Successfully' else "❌"
            org_url_display = result['organization_url'] if result['organization_url'] else "N/A"
            f.write(f"| {result['pdf_path']} | {result['output_path']} | {result['model_used']} | {status_icon} {result['status']} | {org_url_display} |\n")
        
        f.write(f"\n### 📝 Summary\n")
        f.write(f"- ✅ Successfully converted: {success_count}\n")
        f.write(f"- ❌ Failed conversions: {len(pdf_paths) - success_count}\n")
        f.write(f"- 📊 Total PDFs processed: {len(pdf_paths)}\n")
        
        f.write("\n### ℹ️ About the Conversion\n")
        f.write("- ⚙️ PDF text extracted using `markitdown[pdf]`.\n")
        f.write("- 🤖 Markdown generated using Google Gemini API.\n")
        f.write("- 📝 AI prompt from `.github/ai-prompts/pdf-to-markdown-prompt.md`.\n")
        f.write("- ⬆️ Output files are committed to the repository.\n")

        return 0 if success_count > 0 else 1

if __name__ == "__main__":
    # Corrected argument check in main
    if len(sys.argv) < 5:
        print("Usage: python pdf-converter.py <pdf_paths_file> <prompt_path> <prompt_version> <branch>")
        sys.exit(1)
    sys.exit(main())
