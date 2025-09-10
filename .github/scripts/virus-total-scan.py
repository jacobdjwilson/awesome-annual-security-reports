import os
import sys
import time
import requests
import json
import hashlib
import base64

# Constants
API_BASE_URL = "https://www.virustotal.com/api/v3"

def calculate_file_hash(file_path):
    """Calculate SHA256 hash of a file"""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def scan_file(file_path, api_key):
    """Scan a file with VirusTotal and create annotation with results"""
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return {"status": "failed", "reason": "File not found"}
    
    try:
        headers = {
            "x-apikey": api_key,
            "User-Agent": "VirusTotal GitHub Action",
            "Accept": "application/json"
        }
        
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
        file_size_bytes = os.path.getsize(file_path)
        print(f"File: {os.path.basename(file_path)} ({file_size_mb:.2f} MB)")
        
        if file_size_bytes > 32 * 1024 * 1024:
            print(f"Warning: File size ({file_size_mb:.2f} MB) exceeds free API limit (32 MB)")
            return {"status": "failed", "reason": "File size exceeds 32MB limit for free accounts"}
        
        file_hash = calculate_file_hash(file_path)
        print(f"File SHA256: {file_hash}")
        
        print("Checking if file has been scanned before...")
        lookup_response = requests.get(
            f"{API_BASE_URL}/files/{file_hash}",
            headers=headers,
            timeout=30
        )
        
        scan_id = None
        
        if lookup_response.status_code == 200:
            print("File found in VirusTotal database, using existing scan results")
            scan_data = lookup_response.json()
        elif lookup_response.status_code == 404:
            print("File not found in database, uploading for new scan...")
            
            with open(file_path, 'rb') as f:
                files = {"file": (os.path.basename(file_path), f, "application/octet-stream")}
                
                response = requests.post(
                    f"{API_BASE_URL}/files",
                    headers=headers,
                    files=files,
                    timeout=300
                )
            
            if response.status_code != 200:
                print(f"Error: File upload failed with status {response.status_code}")
                print(f"Response: {response.text}")
                return {"status": "failed", "reason": f"File upload failed (Status: {response.status_code})"}
            
            upload_result = response.json()
            scan_id = upload_result.get('data', {}).get('id')
            
            if not scan_id:
                print("Error: No scan ID in upload response")
                return {"status": "failed", "reason": "No scan ID in upload response"}
            
            print(f"File uploaded successfully. Analysis ID: {scan_id}")
            
            print("Waiting for scan to complete...")
            
            wait_times = [10, 20, 30, 60, 120]
            
            for attempt, wait_time in enumerate(wait_times, 1):
                if attempt > 1:
                    print(f"Waiting {wait_time} seconds before next check...")
                    time.sleep(wait_time)
                
                print(f"Checking scan status (attempt {attempt}/{len(wait_times)})...")
                
                try:
                    status_response = requests.get(
                        f"{API_BASE_URL}/analyses/{scan_id}",
                        headers=headers,
                        timeout=30
                    )
                    
                    if status_response.status_code != 200:
                        print(f"Warning: Status check failed with code {status_response.status_code}")
                        continue
                    
                    analysis_result = status_response.json()
                    status = analysis_result.get('data', {}).get('attributes', {}).get('status')
                    
                    if status == 'completed':
                        print("Scan completed!")
                        final_response = requests.get(
                            f"{API_BASE_URL}/files/{file_hash}",
                            headers=headers,
                            timeout=30
                        )
                        
                        if final_response.status_code == 200:
                            scan_data = final_response.json()
                            break
                        else:
                            print("Error retrieving final scan results")
                            return {"status": "failed", "reason": "Error retrieving final scan results"}
                    else:
                        print(f"Scan status: {status}")
                except Exception as e:
                    print(f"Error checking scan status: {e}")
            else:
                print("Scan did not complete within timeout period")
                return {"status": "failed", "reason": "Scan did not complete within timeout period"}
        else:
            print(f"Error checking file status: {lookup_response.status_code}")
            return {"status": "failed", "reason": f"Error checking file status (Status: {lookup_response.status_code})"}
        
        attributes = scan_data.get('data', {}).get('attributes', {})
        stats = attributes.get('last_analysis_stats', {})
        results = attributes.get('last_analysis_results', {})
        
        malicious_count = stats.get('malicious', 0)
        suspicious_count = stats.get('suspicious', 0)
        total_engines = sum(stats.values())
        
        if malicious_count > 0:
            verdict = "Malicious"
        elif suspicious_count > 0:
            verdict = "Suspicious"
        else:
            verdict = "Clean"
        
        detections = []
        for engine_name, engine_result in results.items():
            if engine_result.get('category') in ['malicious', 'suspicious']:
                engine_verdict = engine_result.get('result', 'Unknown')
                detections.append(f"{engine_name}: {engine_verdict}")
        
        report_url = f"https://www.virustotal.com/gui/file/{file_hash}"
        
        create_annotation(file_path, verdict, malicious_count, suspicious_count, total_engines, report_url)
        
        return {
            "status": "success",
            "file": os.path.basename(file_path),
            "verdict": verdict,
            "malicious_count": malicious_count,
            "suspicious_count": suspicious_count,
            "total_engines": total_engines,
            "report_url": report_url,
            "sha256": file_hash,
            "detections": detections
        }
        
    except Exception as e:
        print(f"Error scanning file: {str(e)}")
        import traceback
        traceback.print_exc()
        return {"status": "failed", "reason": f"Exception during scan: {str(e)}"}

def create_annotation(file_path, verdict, malicious_count, suspicious_count, total_engines, report_url):
    if verdict.lower() == "malicious":
        level = "error"
        icon = "🔴"
    elif verdict.lower() == "suspicious":
        level = "warning"
        icon = "🟠"
    else:
        level = "notice"
        icon = "✅"
    
    detection_summary = f"{malicious_count + suspicious_count}/{total_engines} engines"
    message = f"VirusTotal Scan: {verdict} {icon} ({detection_summary})"
    
    print(f"::{level} file={file_path}::{message}")
    print(f"::{level} file={file_path}::Report: {report_url}")

def main():
    api_key = os.environ.get('VIRUS_TOTAL_API_KEY')
    if not api_key:
        print("Error: VIRUS_TOTAL_API_KEY environment variable not set")
        sys.exit(1)
    
    if len(sys.argv) < 2:
        print("No files provided to scan.")
        return

    files_to_scan_file = sys.argv[1]
    with open(files_to_scan_file, "r") as f:
        files_to_scan = [line.strip() for line in f.readlines() if line.strip()]

    results = []
    failed_scans = []
    
    for file_path in files_to_scan:
        print(f"\n--- Scanning: {file_path} ---")
        result = scan_file(file_path, api_key)
        if result and result["status"] == "success":
            results.append(result)
        elif result and result["status"] == "failed":
            failed_scans.append({"file": os.path.basename(file_path), "reason": result["reason"]})
        else:
            failed_scans.append({"file": os.path.basename(file_path), "reason": "Unknown error"})
        print(f"--- Completed: {file_path} ---\n")

    # Write results to a JSON file
    output_json_path = os.environ.get("VIRUSTOTAL_RESULTS_JSON_PATH", "virustotal_results.json")
    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"Wrote VirusTotal results to {output_json_path}")

    summary_path = os.environ.get('GITHUB_STEP_SUMMARY', 'summary.md')
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write("## 🛡️ VirusTotal Security Scan Results\n\n")
        if results:
            f.write("| File | Verdict | Detections | Engines | Report |\n")
            f.write("|------|---------|------------|---------|--------|\n")
            for result in results:
                icon = ""
                verdict = result["verdict"]
                if "malicious" in verdict.lower():
                    icon = "🔴 "
                elif "suspicious" in verdict.lower():
                    icon = "🟠 "
                else:
                    icon = "✅ "
                detection_count = result["malicious_count"] + result["suspicious_count"]
                detection_summary = f"{detection_count}/{result['total_engines']}"
                detections = result.get("detections", [])
                if detections:
                    top_detections = ", ".join([d.split(":")[0] for d in detections[:3]])
                    if len(detections) > 3:
                        top_detections += f" (+{len(detections) - 3} more)"
                else:
                    top_detections = "None"
                f.write(f"| {result['file']} | {icon}{verdict} | {top_detections} | {detection_summary} | [View Report]({result['report_url']}) |\n")
        else:
            f.write("No files were successfully scanned.\n")
        
        if failed_scans:
            f.write("\n### ❌ Failed Scans\n")
            for f_scan in failed_scans:
                f.write(f"- {f_scan['file']}: {f_scan['reason']}\n")

    if any(r["verdict"] == "Malicious" for r in results):
        sys.exit(1)

if __name__ == "__main__":
    main()
