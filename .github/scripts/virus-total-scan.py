
import os
import sys
import time
import requests
import json
import hashlib
import argparse
from typing import List, Dict, Any

# Constants
API_BASE_URL = "https://www.virustotal.com/api/v3"

def calculate_file_hash(file_path: str) -> str:
    """Calculate SHA256 hash of a file"""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def scan_file(file_path: str, api_key: str) -> Dict[str, Any]:
    """Scan a file with VirusTotal and return results"""
    if not os.path.exists(file_path):
        return {"status": "failed", "reason": "File not found"}

    headers = {
        "x-apikey": api_key,
        "User-Agent": "VirusTotal GitHub Action",
        "Accept": "application/json"
    }
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)

    if file_size_mb > 32:
        return {"status": "failed", "reason": "File size exceeds 32MB limit"}

    file_hash = calculate_file_hash(file_path)
    
    try:
        # Check if file has been scanned before
        lookup_response = requests.get(f"{API_BASE_URL}/files/{file_hash}", headers=headers, timeout=30)
        
        if lookup_response.status_code == 200:
            scan_data = lookup_response.json()
        elif lookup_response.status_code == 404:
            # Upload file for scanning
            with open(file_path, 'rb') as f:
                files = {"file": (os.path.basename(file_path), f)}
                response = requests.post(f"{API_BASE_URL}/files", headers=headers, files=files, timeout=300)
            
            if response.status_code != 200:
                return {"status": "failed", "reason": f"File upload failed (Status: {response.status_code})"}
            
            scan_id = response.json().get('data', {}).get('id')
            if not scan_id:
                return {"status": "failed", "reason": "No scan ID in upload response"}

            # Poll for results
            for attempt in range(5):
                time.sleep(10 * (attempt + 1)) # Exponential backoff
                status_response = requests.get(f"{API_BASE_URL}/analyses/{scan_id}", headers=headers, timeout=30)
                if status_response.status_code == 200:
                    analysis_result = status_response.json()
                    if analysis_result.get('data', {}).get('attributes', {}).get('status') == 'completed':
                        final_response = requests.get(f"{API_BASE_URL}/files/{file_hash}", headers=headers, timeout=30)
                        if final_response.status_code == 200:
                            scan_data = final_response.json()
                            break
            else:
                return {"status": "failed", "reason": "Scan did not complete within timeout"}
        else:
            return {"status": "failed", "reason": f"Error checking file status (Status: {lookup_response.status_code})"}

        # Process results
        attributes = scan_data.get('data', {}).get('attributes', {})
        stats = attributes.get('last_analysis_stats', {})
        malicious_count = stats.get('malicious', 0)
        suspicious_count = stats.get('suspicious', 0)
        total_engines = sum(stats.values())
        verdict = "Malicious" if malicious_count > 0 else "Suspicious" if suspicious_count > 0 else "Clean"
        
        return {
            "status": "success",
            "file": os.path.basename(file_path),
            "verdict": verdict,
            "malicious_count": malicious_count,
            "suspicious_count": suspicious_count,
            "total_engines": total_engines,
            "report_url": f"https://www.virustotal.com/gui/file/{file_hash}",
            "sha256": file_hash
        }

    except Exception as e:
        return {"status": "failed", "reason": str(e)}

def create_annotation(file_path: str, result: Dict[str, Any]):
    """Create GitHub annotation with scan results"""
    verdict = result['verdict']
    level = "error" if verdict == "Malicious" else "warning" if verdict == "Suspicious" else "notice"
    icon = "🔴" if level == "error" else "🟠" if level == "warning" else "✅"
    message = f"VirusTotal Scan: {verdict} {icon} ({result['malicious_count'] + result['suspicious_count']}/{result['total_engines']} engines)"
    print(f"::{level} file={file_path}::{message}")
    print(f"::{level} file={file_path}::Report: {result['report_url']}")

def main():
    parser = argparse.ArgumentParser(description="Scan files with VirusTotal.")
    parser.add_argument("files_list", help="Path to a file containing a list of PDF paths to scan.")
    parser.add_argument("--output-json", help="Path to save the results as a JSON file.", default="scan_results.json")
    args = parser.parse_args()

    api_key = os.environ.get('VIRUS_TOTAL_API_KEY')
    if not api_key:
        print("Error: VIRUS_TOTAL_API_KEY environment variable not set.")
        sys.exit(1)

    with open(args.files_list, 'r') as f:
        files_to_scan = [line.strip() for line in f if line.strip()]

    results = []
    for file_path in files_to_scan:
        result = scan_file(file_path, api_key)
        results.append(result)
        if result['status'] == 'success':
            create_annotation(file_path, result)

    with open(args.output_json, 'w') as f:
        json.dump(results, f, indent=2)

    # Summary
    summary_path = os.environ.get('GITHUB_STEP_SUMMARY', 'summary.md')
    with open(summary_path, 'w') as f:
        f.write("## 🛡️ VirusTotal Security Scan Results\n\n")
        if results:
            f.write("| File | Verdict | Detections | Engines | Report |\n")
            f.write("|------|---------|------------|---------|--------|\n")
            for res in results:
                if res['status'] == 'success':
                    icon = "🔴" if res['verdict'] == "Malicious" else "🟠" if res['verdict'] == "Suspicious" else "✅"
                    detections = f"{res['malicious_count'] + res['suspicious_count']}/{res['total_engines']}"
                    f.write(f"| {res['file']} | {icon} {res['verdict']} | {detections} | {res['total_engines']} | [View Report]({res['report_url']}) |\n")
        else:
            f.write("No files were scanned.\n")

if __name__ == "__main__":
    main()
