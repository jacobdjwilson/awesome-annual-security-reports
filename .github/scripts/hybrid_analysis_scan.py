#!/usr/bin/env python3
"""
Hybrid Analysis PDF Scanner for GitHub Actions
This script submits a PDF file to the Hybrid Analysis v2 Quick Scan API and checks for threats.
Uses GitHub secrets for authentication.
"""

import os
import sys
import time
import json
import requests
import logging
from datetime import datetime

# Configure logging
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[console_handler]
)

def get_api_key():
    """Get the API key from environment variable."""
    api_key = os.environ.get("HYBRID_ANALYSIS_API_KEY")
    if not api_key:
        logging.error("HYBRID_ANALYSIS_API_KEY environment variable not set")
        sys.exit(1)
    logging.info(f"API key found. Length: {len(api_key)} characters")
    return api_key

def submit_file(file_path, api_key):
    """Submit a file to the Hybrid Analysis v2 Quick Scan API."""
    logging.info(f"Submitting file: {file_path}")
    
    # Verify file exists and check size
    file_size = os.path.getsize(file_path)
    logging.info(f"File size: {file_size} bytes ({file_size / (1024*1024):.2f} MB)")
    
    url = "https://www.hybrid-analysis.com/api/v2/quick-scan/file"
    logging.info(f"API endpoint: {url}")
    
    headers = {
        "api-key": api_key,
        "User-Agent": "Hybrid Analysis GitHub Actions Scanner",
        "Accept": "application/json"
    }
    
    # Check file content type
    import mimetypes
    mime_type = mimetypes.guess_type(file_path)[0]
    logging.info(f"File MIME type: {mime_type}")
    
    with open(file_path, 'rb') as f:
        files = {'file': (os.path.basename(file_path), f)}
        
        # Using Windows 11 64-bit as default environment
        data = {
            "environment_id": "160",  # Windows 11 64-bit
            "scan_type": "all"
        }
        
        try:
            logging.info("Sending API request...")
            response = requests.post(url, headers=headers, files=files, data=data)
            logging.info(f"Response status code: {response.status_code}")
            
            # Log rate limit information if available
            if 'Sample-Download-Limits' in response.headers:
                logging.info(f"Sample-Download-Limits: {response.headers['Sample-Download-Limits']}")
            
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error submitting file: {e}")
            if hasattr(e, 'response') and e.response:
                try:
                    err_json = e.response.json()
                    logging.error(f"Error details: {json.dumps(err_json)}")
                except json.JSONDecodeError:
                    logging.error(f"Error response: {e.response.text}")
            
            # Try alternative endpoint
            alt_url = "https://www.hybrid-analysis.com/api/v2/submit/file"
            logging.info(f"Trying alternative API endpoint: {alt_url}")
            
            try:
                with open(file_path, 'rb') as alt_f:
                    alt_data = {
                        "environment_id": "160",  # Windows 11 64-bit
                        "comment": "Submitted via GitHub Actions"
                    }
                    response = requests.post(alt_url, headers=headers, files={'file': (os.path.basename(file_path), alt_f)}, data=alt_data)
                    logging.info(f"Alternative response status code: {response.status_code}")
                    
                    if response.status_code == 201:
                        return response.json()
                    else:
                        logging.error(f"Alternative endpoint failed: {response.text}")
            except Exception as alt_e:
                logging.error(f"Alternative endpoint error: {alt_e}")
            
            sys.exit(1)

def check_report_status(job_id, api_key):
    """Check the status of a submitted analysis job."""
    url = f"https://www.hybrid-analysis.com/api/v2/report/{job_id}/summary"
    
    headers = {
        "api-key": api_key,
        "User-Agent": "Hybrid Analysis GitHub Actions Scanner",
        "Accept": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            return None
        
        return response.json()
    except requests.exceptions.RequestException:
        return None

def test_api_connectivity(api_key):
    """Test API connectivity and check quota."""
    test_url = "https://www.hybrid-analysis.com/api/v2/key/current"
    logging.info("Testing API connectivity")
    try:
        headers = {
            "api-key": api_key,
            "User-Agent": "Hybrid Analysis GitHub Actions Scanner",
            "Accept": "application/json"
        }
        response = requests.get(test_url, headers=headers)
        if response.status_code == 200:
            api_info = response.json()
            logging.info(f"API key is valid. Quota remaining: {api_info.get('quota_remaining', 'unknown')}")
            return True
        else:
            logging.warning(f"API test failed with status {response.status_code}")
            return False
    except Exception as e:
        logging.warning(f"API connection test failed: {e}")
        return False

def generate_report_markdown(report, job_id):
    """Generate a markdown report for GitHub."""
    threat_score = report.get('threat_score', 0)
    verdict = report.get('verdict', 'Unknown')
    sha256 = report.get('sha256', '')
    report_url = f"https://www.hybrid-analysis.com/sample/{sha256}" if sha256 else ""
    
    markdown = f"""## Hybrid Analysis Security Scan Results

- **File**: {report.get('file_name', 'Unknown')}
- **Threat Score**: {threat_score}/100
- **Verdict**: {verdict}
- **Job ID**: {job_id}
"""

    if report_url:
        markdown += f"- **Full Report**: [View on Hybrid Analysis]({report_url})\n"
        
    markdown += "\n### ⚠️ Note: Quick scan results expire after 24 hours\n"
    
    # Add threats if any
    if 'threats' in report and report['threats']:
        markdown += "\n### Detected Threats:\n"
        for threat in report['threats']:
            markdown += f"- {threat}\n"
    
    # Add signatures if any
    if 'signatures' in report:
        markdown += "\n### Behavioral Signatures:\n"
        for sig in report.get('signatures', [])[:10]:  # Show only first 10
            markdown += f"- {sig.get('name', 'Unknown')} ({sig.get('severity', 'unknown')})\n"
            
        if len(report.get('signatures', [])) > 10:
            markdown += f"- ...and {len(report.get('signatures', [])) - 10} more (see full report)\n"
    
    return markdown

def main():
    logging.info("Starting Hybrid Analysis PDF Scanner for GitHub Actions")
    
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <pdf_file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1].strip("'\"")  # Remove any quotes that might be present
    
    # Expand path to absolute
    file_path = os.path.abspath(file_path)
    logging.info(f"Processing file: {file_path}")
    
    # Validate file exists and is a PDF
    if not os.path.isfile(file_path):
        logging.error(f"File '{file_path}' not found")
        print(f"::error::File '{file_path}' not found.")
        sys.exit(1)
    
    # Check file permissions
    try:
        with open(file_path, 'rb') as f:
            pass
    except PermissionError:
        logging.error(f"Permission denied: Cannot read file '{file_path}'")
        print(f"::error::Permission denied when trying to read '{file_path}'")
        sys.exit(1)
    
    if not file_path.lower().endswith('.pdf'):
        logging.warning(f"File '{file_path}' does not appear to be a PDF file")
        print(f"::warning::File '{file_path}' does not appear to be a PDF file.")
        # In GitHub Actions, we'll continue anyway rather than asking for input
    
    # Get API key from environment variable
    api_key = get_api_key()
    
    # Test API connectivity
    if not test_api_connectivity(api_key):
        print("::error::Failed to connect to Hybrid Analysis API. Check API key.")
        sys.exit(1)
    
    # Submit file for analysis
    submission = submit_file(file_path, api_key)
    
    if not submission:
        print("::error::Failed to get response from submission API.")
        sys.exit(1)
        
    if 'job_id' not in submission:
        logging.error("Failed to get job ID from submission.")
        
        # Check for alternative IDs or SHA256
        if 'sha256' in submission:
            sha256 = submission['sha256']
            logging.info(f"SHA256 hash found: {sha256}")
            print(f"::notice::SHA256 hash: {sha256}")
            print(f"::notice::You can check results at: https://www.hybrid-analysis.com/sample/{sha256}")
            
        if 'scan_id' in submission:
            job_id = submission['scan_id']
            logging.info(f"Using scan_id as job_id for polling: {job_id}")
        else:
            print("::error::No job_id or scan_id found in submission response.")
            sys.exit(1)
    else:
        job_id = submission['job_id']
        logging.info(f"File submitted successfully. Job ID: {job_id}")
        print(f"::notice::File submitted successfully. Job ID: {job_id}")
    
    # Poll for results
    logging.info("Waiting for analysis to complete...")
    max_attempts = 20
    attempt = 0
    
    while attempt < max_attempts:
        attempt += 1
        time.sleep(15)  # Wait 15 seconds between status checks
        
        report = check_report_status(job_id, api_key)
        
        if not report:
            logging.info(f"Attempt {attempt}/{max_attempts}: No report data yet.")
            continue
        
        status = report.get('state', '')
        
        if status == 'SUCCESS':
            logging.info("Analysis complete!")
            
            # Check for threats
            threat_score = report.get('threat_score', 0)
            verdict = report.get('verdict', 'Unknown')
            
            logging.info(f"Threat Score: {threat_score}/100")
            logging.info(f"Verdict: {verdict}")
            
            # Generate markdown report
            markdown_report = generate_report_markdown(report, job_id)
            
            # For GitHub Actions, output to both console and a summary file
            print(markdown_report)
            
            # Write markdown report to GitHub step summary
            summary_path = os.environ.get('GITHUB_STEP_SUMMARY')
            if summary_path:
                with open(summary_path, 'a') as f:
                    f.write(markdown_report)
            
            # Set output for GitHub Actions
            if 'GITHUB_OUTPUT' in os.environ:
                with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
                    f.write(f"threat_score={threat_score}\n")
                    f.write(f"verdict={verdict}\n")
                    if 'sha256' in report:
                        f.write(f"sha256={report['sha256']}\n")
                    
                    # For GitHub Actions, we also want to fail the workflow if the threat score is high
                    if threat_score > 75:  # You can adjust this threshold
                        print("::error::High threat score detected. This file may be malicious.")
                    elif threat_score > 50:
                        print("::warning::Medium threat score detected. Please review the file carefully.")
            
            return 0
        
        elif status == 'ERROR':
            error_msg = report.get('error', 'Unknown error')
            logging.error(f"Analysis failed: {error_msg}")
            print(f"::error::Analysis failed: {error_msg}")
            return 1
        
        elif status == 'IN_PROGRESS':
            logging.info(f"Attempt {attempt}/{max_attempts}: Analysis in progress...")
        
        else:
            logging.info(f"Attempt {attempt}/{max_attempts}: Status: {status}")
    
    logging.warning("Timeout waiting for analysis to complete.")
    print("::warning::Timeout waiting for analysis to complete. Please check the website for results.")
    if 'sha256' in submission:
        print(f"::notice::You can check status at: https://www.hybrid-analysis.com/sample/{submission['sha256']}")
    elif job_id:
        print(f"::notice::Job ID: {job_id}")
    
    return 1

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        logging.info("Process interrupted by user.")
        sys.exit(130)  # 130 is the standard exit code for SIGINT
    except Exception as e:
        logging.exception(f"Unhandled error: {str(e)}")
        print(f"::error::Unhandled error: {str(e)}")
        sys.exit(1)
