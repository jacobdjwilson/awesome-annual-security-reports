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
            test_response = test_model.generate_content("Hello")
            MODEL = model_name
            print(f"Successfully verified model: {MODEL}")
            break
        except Exception as e:
            print(f"Model {model_name} not available or failed verification: {str(e)}")
            continue
    if not MODEL:
        print("No models available. Exiting.")
        sys.exit(1)

def read_prompt_file(path: str) -> str:
    with open(path, "r") as file:
        return file.read()

def extract_text_from_pdf(pdf_path: Path) -> str:
    try:
        print(f"Extracting text from PDF: {pdf_path}")
        md = MarkItDown(enable_plugins=False)
        result = md.convert(str(pdf_path))
        text_length = len(result.text_content)
        print(f"Successfully extracted {text_length} characters from PDF")
        return result.text_content
    except Exception as e:
        print(f"Error extracting text from PDF: {str(e)}")
        raise

def perform_google_search(query: str, api_key: str, cse_id: str) -> Optional[str]:
    try:
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=query, cx=cse_id, num=1).execute()
        return res['items'][0]['link'] if 'items' in res and len(res['items']) > 0 else None
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
        full_prompt = f"{prompt_text}\n\n"
        if organization_url:
            full_prompt += f"The official report URL is: {organization_url}\n\n"
        full_prompt += f"# Report Content Below\n\n{pdf_text}"
        
        generation_config = {
            "temperature": 0.2,
            "max_output_tokens": 8192,
        }
        
        response = model.generate_content(full_prompt, generation_config=generation_config)

        # Log prompt feedback
        if response.prompt_feedback:
            print(f"Prompt feedback: {response.prompt_feedback}")

        # Log candidate details for debugging
        if response.candidates:
            for i, candidate in enumerate(response.candidates):
                print(f"Candidate {i} finish reason: {candidate.finish_reason}")
                if candidate.safety_ratings:
                    print(f"Candidate {i} safety ratings: {candidate.safety_ratings})")
        
        if not response.text:
            error_message = "The `response.text` quick accessor requires the response to contain a valid `Part`, but none were returned."
            if response.candidates and response.candidates[0].finish_reason:
                error_message += f" The candidate's finish_reason is {response.candidates[0].finish_reason}."
            if response.candidates and response.candidates[0].safety_ratings:
                error_message += f" Safety ratings: {response.candidates[0].safety_ratings}. "
            raise ValueError(error_message)

        print(f"Successfully generated markdown ({len(response.text)} characters)")
        return response.text
    except Exception as e:
        print(f"Error generating markdown with AI: {str(e)}")
        raise


def process_pdf(pdf_path: Path, prompt_path: str, prompt_version: str, branch: str, google_search_api_key: Optional[str], google_cse_id: Optional[str]) -> Dict[str, Any]:
    try:
        print(f"Processing: {pdf_path} (Branch: {branch})")
        prompt_text = read_prompt_file(prompt_path)
        print(f"Loaded prompt file ({len(prompt_text)} characters)")
        pdf_text = extract_text_from_pdf(pdf_path)
        
        filename_stem = pdf_path.stem
        parts = filename_stem.split(' - ', 1)
        organization_name = parts[0].strip() if len(parts) > 0 else ""
        report_title = parts[1].strip() if len(parts) > 1 else filename_stem
        
        organization_url = None
        if google_search_api_key and google_cse_id:
            search_query = f"{organization_name} {report_title} report"
            print(f"Performing Google search for: '{search_query}'")
            organization_url = perform_google_search(search_query, google_search_api_key, google_cse_id)
        else:
            print("Google Search API keys not provided. Skipping URL search.")

        markdown_content = generate_markdown_with_ai(pdf_text, prompt_text, organization_url)
        
        relative_path = pdf_path.relative_to(Path("Annual Security Reports"))
        output_dir = Path("Markdown Conversions") / relative_path.parent
        output_path = output_dir / f"{pdf_path.stem}.md"
        
        print(f"Writing output to: {output_path}")
        os.makedirs(output_dir, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)

        if not output_path.exists():
            print(f"Error: Failed to create {output_path}")
            return {"status": "failed", "pdf_path": str(pdf_path), "reason": f"Failed to create {output_path}"}

        print(f"Created/Updated: {output_path}")

        return {
            "status": "success",
            "pdf_path": str(pdf_path),
            "output_path": str(output_path),
            "model_used": MODEL
        }
    except Exception as e:
        error_message = f"Error processing {pdf_path}: {str(e)}"
        print(error_message, file=sys.stderr) # Print to stderr for visibility in GitHub Actions logs
        return {"status": "failed", "pdf_path": str(pdf_path), "reason": str(e)}

def main():
    parser = argparse.ArgumentParser(description="Convert PDF files to Markdown using AI.")
    parser.add_argument("files_list", help="Path to a file containing a list of PDF paths.")
    parser.add_argument("prompt_path", help="Path to the AI prompt file.")
    parser.add_argument("prompt_version", help="Version of the AI prompt.")
    parser.add_argument("branch", help="Current Git branch.")
    parser.add_argument("--output-json", help="Path to save the conversion results as a JSON file.", default="conversions.json")
    args = parser.parse_args()

    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        sys.exit(1)
    setup_gemini(gemini_api_key)

    google_search_api_key = os.environ.get("GOOGLE_SEARCH_API_KEY")
    google_cse_id = os.environ.get("GOOGLE_CSE_ID")

    with open(args.files_list, 'r') as f:
        pdf_paths = [Path(line.strip()) for line in f if line.strip()]

    results = []
    converted_output_paths = []
    for pdf_path in pdf_paths:
        result = process_pdf(pdf_path, args.prompt_path, args.prompt_version, args.branch, google_search_api_key, google_cse_id)
        results.append(result)
        if result['status'] == 'success':
            converted_output_paths.append(result['output_path'])

    with open(args.output_json, 'w') as f:
        json.dump(results, f, indent=2)

    # Commit changes if any files were converted
    if converted_output_paths:
        try:
            subprocess.run(["git", "config", "user.name", "GitHub Action"], check=True)
            subprocess.run(["git", "config", "user.email", "action@github.com"], check=True)
            for path in converted_output_paths:
                subprocess.run(["git", "add", path], check=True)
            
            commit_message = f"Converted {len(converted_output_paths)} PDF(s) to Markdown using AI Prompt {args.prompt_version} (Model {MODEL}, Branch {args.branch})"
            subprocess.run(["git", "commit", "-m", commit_message], check=True)
            print(f"Committed changes: {commit_message}")
        except Exception as e:
            print(f"Error during git operations: {str(e)}")

    # Create or clear the converted files list
    converted_files_path = os.environ.get("CONVERTED_FILES_PATH", "converted_files.txt")
    with open(converted_files_path, "w") as f:
        for path in converted_output_paths:
            f.write(f"{path}\n")

    # Summary
    summary_path = os.environ.get('GITHUB_STEP_SUMMARY', 'summary.md')
    with open(summary_path, 'w') as f:
        f.write("\n## 📄 PDF to Markdown Conversion Summary\n\n")
        if results:
            f.write("| PDF File | Markdown Output | Model Used | Status |\n")
            f.write("|----------|-----------------|------------|--------|\n")
            for res in results:
                status_icon = "✅" if res['status'] == 'success' else "❌"
                f.write(f"| {res['pdf_path']} | {res.get('output_path', 'N/A')} | {res.get('model_used', 'N/A')} | {status_icon} {res['status']} |\n")
        else:
            f.write("No PDFs were processed.")

    return 0

if __name__ == "__main__":
    sys.exit(main())