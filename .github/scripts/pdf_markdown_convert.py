#!/usr/bin/env python3
"""
PDF to Markdown Converter using Google Gemini AI
This script extracts text from a PDF and uses Google Gemini AI to convert it to well-formatted markdown.
For use in GitHub Actions workflows.
"""

import os
import sys
import logging
import argparse
import json
import time
import requests
import base64
from pathlib import Path
import tempfile
import re

# Try to import PyPDF2, use pdfminer.six as fallback
try:
    import PyPDF2
    PDF_LIBRARY = "PyPDF2"
except ImportError:
    try:
        from pdfminer.high_level import extract_text as pdfminer_extract_text
        PDF_LIBRARY = "pdfminer"
    except ImportError:
        print("::error::Neither PyPDF2 nor pdfminer.six is installed. Please install one of them.")
        sys.exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF using available library"""
    logging.info(f"Extracting text from PDF: {pdf_path}")
    
    if PDF_LIBRARY == "PyPDF2":
        logging.info("Using PyPDF2 for text extraction")
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            total_pages = len(reader.pages)
            logging.info(f"PDF has {total_pages} pages")
            
            for i, page in enumerate(reader.pages):
                logging.info(f"Extracting page {i+1}/{total_pages}")
                text += page.extract_text() + "\n\n"
    else:
        logging.info("Using pdfminer.six for text extraction")
        text = pdfminer_extract_text(pdf_path)
        
    logging.info(f"Extracted {len(text)} characters from PDF")
    return text

def chunk_text(text, max_chunk_size=8000):
    """Split text into chunks for API processing"""
    # If text is small enough, return as is
    if len(text) <= max_chunk_size:
        return [text]
    
    chunks = []
    
    # Try to split by double newlines (paragraphs)
    paragraphs = re.split(r'\n\s*\n', text)
    current_chunk = ""
    
    for paragraph in paragraphs:
        # If adding this paragraph would exceed the chunk size, start a new chunk
        if len(current_chunk) + len(paragraph) > max_chunk_size:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = paragraph + "\n\n"
        else:
            current_chunk += paragraph + "\n\n"
    
    # Add the last chunk if it's not empty
    if current_chunk:
        chunks.append(current_chunk)
    
    logging.info(f"Split text into {len(chunks)} chunks")
    return chunks

def get_gemini_api_key():
    """Get Gemini API key from environment"""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        logging.error("GEMINI_API_KEY environment variable not set")
        sys.exit(1)
    return api_key

def convert_to_markdown_with_gemini(text_chunks, model="gemini-2.0-flash"):
    """Convert text to markdown using Google Gemini AI"""
    api_key = get_gemini_api_key()
    endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    headers = {
        "Content-Type": "application/json"
    }
    
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".github", "ai_prompts", "pdf_to_markdown_prompt.md"), 'r') as f:
        prompt_template = f.read()
    
    # If we can't find the prompt file, use a default prompt
    if not prompt_template or len(prompt_template) < 10:
        logging.warning("Could not read prompt template, using default prompt")
        prompt_template = """
        Convert the following text extracted from a PDF into clean, well-formatted markdown.
        Follow these guidelines:
        - Preserve the document structure (headings, paragraphs, lists)
        - Use proper markdown syntax for headings, lists, emphasis, and other elements
        - Clean up any artifacts from the PDF extraction process
        - Format tables properly if present
        - Ensure code blocks are properly formatted
        - Maintain the original meaning and content
        
        Here's the text to convert:
        
        {{TEXT}}
        """
    
    all_markdown = []
    total_chunks = len(text_chunks)
    
    for i, chunk in enumerate(text_chunks):
        logging.info(f"Processing chunk {i+1}/{total_chunks} with {model}")
        
        # Replace {{TEXT}} placeholder with the actual text
        prompt = prompt_template.replace("{{TEXT}}", chunk)
        
        # Prepare the request payload
        data = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.2,
                "topP": 0.8,
                "topK": 40,
                "maxOutputTokens": 8192
            }
        }
        
        # Add API key to the URL
        url = f"{endpoint}?key={api_key}"
        
        retry_count = 0
        max_retries = 3
        
        while retry_count < max_retries:
            try:
                response = requests.post(url, headers=headers, json=data)
                response.raise_for_status()
                
                result = response.json()
                if "candidates" in result and result["candidates"]:
                    # Extract the markdown text from the response
                    content = result["candidates"][0]["content"]
                    markdown_text = ""
                    
                    for part in content.get("parts", []):
                        if "text" in part:
                            markdown_text += part["text"]
                    
                    all_markdown.append(markdown_text)
                    break
                else:
                    logging.error(f"No candidates in response: {result}")
                    retry_count += 1
                    
            except requests.exceptions.RequestException as e:
                logging.error(f"API request failed: {str(e)}")
                if retry_count == max_retries - 1:
                    # If we're on the last retry and using the primary model, try the fallback model
                    if model == "gemini-2.0-flash":
                        logging.info("Falling back to gemini-2.0-flash-lite model")
                        return convert_to_markdown_with_gemini([chunk], model="gemini-2.0-flash-lite")
                
                retry_count += 1
                time.sleep(5)  # Wait before retrying
    
    # Combine all chunks of markdown
    return "\n\n".join(all_markdown)

def add_frontmatter(markdown_text, pdf_path):
    """Add Jekyll frontmatter to the markdown"""
    # Extract filename without extension
    filename = os.path.basename(pdf_path)
    title = os.path.splitext(filename)[0].replace("-", " ")
    
    # Get current date
    from datetime import datetime
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    frontmatter = f"""---
layout: post
title: "{title}"
date: {current_date}
categories: reports
source_file: "{filename}"
---

"""
    return frontmatter + markdown_text

def main():
    parser = argparse.ArgumentParser(description="Convert PDF to Markdown using Google Gemini AI")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("--output", "-o", help="Output markdown file path")
    args = parser.parse_args()
    
    # Validate PDF path
    pdf_path = args.pdf_path
    if not os.path.isfile(pdf_path):
        logging.error(f"PDF file not found: {pdf_path}")
        print(f"::error::PDF file not found: {pdf_path}")
        sys.exit(1)
    
    # Determine output path if not provided
    output_path = args.output
    if not output_path:
        pdf_dir = os.path.dirname(pdf_path)
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
        output_path = os.path.join(pdf_dir, f"{pdf_name}.md")
    
    try:
        # Extract text from PDF
        extracted_text = extract_text_from_pdf(pdf_path)
        
        if not extracted_text or len(extracted_text.strip()) < 100:
            logging.error("Failed to extract meaningful text from PDF")
            print("::error::Failed to extract meaningful text from PDF")
            sys.exit(1)
        
        # Split text into chunks for processing
        text_chunks = chunk_text(extracted_text)
        
        # Convert text to markdown using Gemini
        markdown_text = convert_to_markdown_with_gemini(text_chunks)
        
        # Add frontmatter for Jekyll
        final_markdown = add_frontmatter(markdown_text, pdf_path)
        
        # Write markdown to output file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(final_markdown)
        
        logging.info(f"Markdown conversion complete. Output saved to: {output_path}")
        print(f"::notice::Markdown conversion complete. Output saved to: {output_path}")
        
        # Set outputs for GitHub Actions
        if 'GITHUB_OUTPUT' in os.environ:
            with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
                f.write(f"markdown_file={output_path}\n")
        
        return 0
        
    except Exception as e:
        logging.exception(f"Error converting PDF to markdown: {str(e)}")
        print(f"::error::Error converting PDF to markdown: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
