#!/usr/bin/env python3

import os
import sys
import time
import requests
import json
import hashlib
import re
from pathlib import Path

# Constants
API_BASE_URL = "https://www.virustotal.com/api/v3"
URL_REGEX = r'https?://[^\s"\'<>]+'

def get_api_headers(api_key):
    """Returns the headers for VirusTotal API requests."""
    return {
        "x-apikey": api_key,
        "User-Agent": "VirusTotal GitHub Action",
        "Accept": "application/json"
    }

def rate_limit_delay():
    """Sleep to respect the public API rate limit (4 requests/min)."""
    time.sleep(16) # Just over 15 seconds to be safe

def calculate_file_hash(file_path):
    """Calculate SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def create_annotation(level, file_path, message, title):
    """Create a GitHub annotation."""
    print(f"::{level} file={file_path},title={title}::{message}")

def scan_file(file_path, api_key):
    """Scan a single file with VirusTotal."""
    if not os.path.exists(file_path):
        return {"status": "failed", "reason": "File not found"}

    try:
        headers = get_api_headers(api_key)
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)

        if file_size_mb > 32:
            reason = f"File size ({file_size_mb:.2f} MB) exceeds 32MB limit"
            create_annotation("warning", file_path, reason, "VirusTotal Scan Skipped")
            return {"status": "skipped", "reason": reason}

        file_hash = calculate_file_hash(file_path)
        print(f"Checking file hash: {file_hash}")

        # Check if file has been scanned before
        rate_limit_delay()
        lookup_response = requests.get(f"{API_BASE_URL}/files/{file_hash}", headers=headers, timeout=30)

        if lookup_response.status_code == 200:
            print("File found in VirusTotal database.")
            scan_data = lookup_response.json()
        elif lookup_response.status_code == 404:
            print("File not found in database, uploading for a new scan...")
            with open(file_path, 'rb') as f:
                files = {"file": (os.path.basename(file_path), f)}
                rate_limit_delay()
                upload_response = requests.post(f"{API_BASE_URL}/files", headers=headers, files=files, timeout=300)

            if upload_response.status_code != 200:
                return {"status": "failed", "reason": f"Upload failed (Status: {upload_response.status_code})"}

            analysis_id = upload_response.json().get('data', {}).get('id')
            if not analysis_id:
                return {"status": "failed", "reason": "No analysis ID in upload response"}

            print(f"File uploaded. Waiting for analysis ID: {analysis_id}")
            # Wait for analysis to complete
            for _ in range(5): # Poll up to 5 times
                rate_limit_delay()
                status_response = requests.get(f"{API_BASE_URL}/analyses/{analysis_id}", headers=headers, timeout=30)
                if status_response.status_code == 200:
                    analysis_result = status_response.json()
                    status = analysis_result.get('data', {}).get('attributes', {}).get('status')
                    if status == 'completed':
                        print("Scan completed!")
                        # Fetch final results using file hash
                        rate_limit_delay()
                        final_response = requests.get(f"{API_BASE_URL}/files/{file_hash}", headers=headers, timeout=30)
                        if final_response.status_code == 200:
                            scan_data = final_response.json()
                            break
                time.sleep(30) # Wait 30s between polls
            else:
                return {"status": "failed", "reason": "Scan did not complete in time"}
        else:
            return {"status": "failed", "reason": f"API error (Status: {lookup_response.status_code})"}

        # Process results
        attributes = scan_data.get('data', {}).get('attributes', {})
        stats = attributes.get('last_analysis_stats', {})
        malicious = stats.get('malicious', 0)
        suspicious = stats.get('suspicious', 0)
        total_engines = sum(stats.values())
        report_url = f"https://www.virustotal.com/gui/file/{file_hash}"

        verdict = "Clean"
        level = "notice"
        icon = "✅"
        if malicious > 0:
            verdict = "Malicious"
            level = "error"
            icon = "🔴"
        elif suspicious > 0:
            verdict = "Suspicious"
            level = "warning"
            icon = "🟠"

        detection_summary = f"{malicious + suspicious}/{total_engines} engines"
        message = f"VirusTotal Scan: {verdict} ({detection_summary}). Report: {report_url}"
        create_annotation(level, file_path, message, f"VirusTotal File Scan: {verdict}")

        return {
            "status": "success", "type": "file", "path": file_path,
            "verdict": verdict, "icon": icon, "summary": detection_summary, "url": report_url
        }

    except Exception as e:
        print(f"Error scanning file {file_path}: {e}")
        return {"status": "failed", "reason": str(e)}

def scan_url(url, file_path, api_key):
    """Scan a single URL with VirusTotal."""
    try:
        headers = get_api_headers(api_key)
        payload = {"url": url}
        rate_limit_delay()
        response = requests.post(f"{API_BASE_URL}/urls", headers=headers, data=payload, timeout=30)

        if response.status_code != 200:
            return {"status": "failed", "reason": f"URL submission failed (Status: {response.status_code})"}

        analysis_id = response.json().get('data', {}).get('id')
        if not analysis_id:
            return {"status": "failed", "reason": "No analysis ID in URL response"}

        print(f"URL submitted. Waiting for analysis ID: {analysis_id}")
        rate_limit_delay()
        analysis_response = requests.get(f"{API_BASE_URL}/analyses/{analysis_id}", headers=headers, timeout=30)

        if analysis_response.status_code != 200:
            return {"status": "failed", "reason": f"URL analysis retrieval failed (Status: {analysis_response.status_code})"}

        attributes = analysis_response.json().get('data', {}).get('attributes', {})
        stats = attributes.get('stats', {})
        malicious = stats.get('malicious', 0)
        suspicious = stats.get('suspicious', 0)
        total_engines = sum(stats.values())
        url_hash = hashlib.sha256(url.encode()).hexdigest()
        report_url = f"https://www.virustotal.com/gui/url/{url_hash}"

        verdict = "Clean"
        level = "notice"
        icon = "✅"
        if malicious > 0:
            verdict = "Malicious"
            level = "error"
            icon = "🔴"
        elif suspicious > 0:
            verdict = "Suspicious"
            level = "warning"
            icon = "🟠"

        if verdict != "Clean":
            detection_summary = f"{malicious + suspicious}/{total_engines} engines"
            message = f"Malicious URL detected: {url}. Verdict: {verdict} ({detection_summary}). Report: {report_url}"
            create_annotation(level, file_path, message, f"VirusTotal URL Scan: {verdict}")

        return {
            "status": "success", "type": "url", "path": url,
            "verdict": verdict, "icon": icon, "summary": detection_summary, "url": report_url
        }

    except Exception as e:
        print(f"Error scanning URL {url}: {e}")
        return {"status": "failed", "reason": str(e)}

def process_file_for_urls(file_path, api_key):
    """Extracts and scans URLs from a given file."""
    results = []
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        found_urls = set(re.findall(URL_REGEX, content))
        if not found_urls:
            return results

        print(f"Found {len(found_urls)} unique URLs in {file_path}. Scanning...")
        for url in found_urls:
            # Basic filtering to avoid scanning common, trusted domains
            if any(domain in url for domain in ['github.com', 'google.com', 'microsoft.com']):
                continue
            
            result = scan_url(url, file_path, api_key)
            # Only report on non-clean URLs to reduce noise
            if result.get("status") == "success" and result.get("verdict") != "Clean":
                results.append(result)
    except Exception as e:
        print(f"Could not process {file_path} for URLs: {e}")
    return results

def write_summary(results, failed_items, skipped_items):
    """Writes the results to the GitHub step summary."""
    summary_path = os.environ.get('GITHUB_STEP_SUMMARY', 'summary.md')
    
    file_results = [r for r in results if r.get("type") == "file"]
    url_results = [r for r in results if r.get("type") == "url"]

    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write("## 🛡️ VirusTotal Security Scan Results\n\n")

        if not results and not failed_items and not skipped_items:
            f.write("No new or modified files required scanning.\n")
            return

        if file_results:
            f.write("### 📄 File Scans\n")
            f.write("| File | Verdict | Detections | Report |\n")
            f.write("|------|---------|------------|--------|\n")
            for res in sorted(file_results, key=lambda x: x['path']):
                f.write(f"| `{Path(res['path']).name}` | {res['icon']} {res['verdict']} | {res['summary']} | [View Report]({res['url']}) |\n")
            f.write("\n")

        if url_results:
            f.write("### 🔗 URL Scans (from modified files)\n")
            f.write("Only suspicious or malicious URLs are listed.\n\n")
            f.write("| URL | Verdict | Detections | Report |\n")
            f.write("|-----|---------|------------|--------|\n")
            for res in sorted(url_results, key=lambda x: x['path']):
                f.write(f"| `{res['path']}` | {res['icon']} {res['verdict']} | {res['summary']} | [View Report]({res['url']}) |\n")
            f.write("\n")

        if failed_items:
            f.write("### ❌ Failed Scans\n")
            for item in failed_items:
                f.write(f"- **{item.get('path', 'Unknown')}**: {item.get('reason', 'Unknown error')}\n")
            f.write("\n")

        if skipped_items:
            f.write("### ⏩ Skipped Scans\n")
            for item in skipped_items:
                f.write(f"- **{item.get('path', 'Unknown')}**: {item.get('reason', 'Not scanned')}\n")
            f.write("\n")

        # Overall Summary
        total_scanned = len(file_results)
        malicious_files = sum(1 for r in file_results if r["verdict"] == "Malicious")
        suspicious_files = sum(1 for r in file_results if r["verdict"] == "Suspicious")
        malicious_urls = sum(1 for r in url_results if r["verdict"] == "Malicious")
        suspicious_urls = sum(1 for r in url_results if r["verdict"] == "Suspicious")

        f.write("### 📊 Overall Summary\n")
        f.write(f"- **Files Scanned**: {total_scanned}\n")
        f.write(f"  - 🔴 Malicious: {malicious_files}\n")
        f.write(f"  - 🟠 Suspicious: {suspicious_files}\n")
        f.write(f"- **Malicious/Suspicious URLs Detected**: {malicious_urls + suspicious_urls}\n")
        f.write(f"- **Failed Scans**: {len(failed_items)}\n")
        f.write(f"- **Skipped Scans**: {len(skipped_items)}\n")

def main():
    """Main function to run the script."""
    api_key = os.environ.get('VIRUS_TOTAL_API_KEY')
    if not api_key:
        sys.exit("Error: VIRUS_TOTAL_API_KEY environment variable not set.")

    files_to_scan = sys.argv[1:]
    if not files_to_scan:
        print("No files to scan.")
        write_summary([], [], [])
        return

    print(f"Found {len(files_to_scan)} files to process.")

    all_results = []
    failed_items = []
    skipped_items = []

    for file_path in files_to_scan:
        print(f"\n--- Processing: {file_path} ---")
        
        # 1. Scan the file itself
        file_result = scan_file(file_path, api_key)
        if file_result.get("status") == "success":
            all_results.append(file_result)
        elif file_result.get("status") == "failed":
            failed_items.append({"path": file_path, **file_result})
        elif file_result.get("status") == "skipped":
            skipped_items.append({"path": file_path, **file_result})

        # 2. Scan for URLs within the file (for both PDF and MD)
        url_results = process_file_for_urls(file_path, api_key)
        all_results.extend(url_results)

    print("\n--- All scans complete. Generating summary. ---")
    write_summary(all_results, failed_items, skipped_items)

    # Determine exit code: fail if any malicious files were found.
    if any(r.get("type") == "file" and r.get("verdict") == "Malicious" for r in all_results):
        print("\n🔴 Malicious files detected. Failing workflow.")
        sys.exit(1)

    print("\n✅ Scan finished. No high-severity threats found in files.")

if __name__ == "__main__":
    main()
