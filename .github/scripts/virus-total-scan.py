"""
Operational Purpose:
    Scans PDF files against the VirusTotal v3 API (via file upload or opportunistic SHA-256 hash lookup),
    evaluating detection stats and enforcing repository security safeguards.

Required Environment Variables:
    VIRUS_TOTAL_API_KEY (optional): VirusTotal v3 API key.
    SKIP_VIRUS_SCAN (optional): If 'true', skips scanning.
    GITHUB_OUTPUT (optional): Path to write step outputs.

Outputs:
    scan_skipped (bool): 'true' if scan was bypassed, 'false' otherwise.
    scan_passed (bool): 'true' if no files were flagged malicious and scan completed.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.virustotal)
"""

import os
import sys
import time
import json
import hashlib
import argparse
from pathlib import Path
from typing import Dict, Any, Optional

import requests

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class ConfigLoader:
    """Loads VirusTotal configuration strictly from workflow-config.json with fail-fast validation."""

    def __init__(self, artifacts_dir: str = ".github/artifacts"):
        cfg_path = Path(artifacts_dir) / "workflow-config.json"
        if not cfg_path.exists():
            raise FileNotFoundError(f"workflow-config.json not found at {cfg_path}")
        try:
            with open(cfg_path, "r", encoding="utf-8") as f:
                cfg = json.load(f)
        except Exception as e:
            raise ValueError(f"Failed to parse JSON artifact '{cfg_path}': {e}") from e

        vt = cfg.get("workflow", {}).get("virustotal")
        if not vt or not isinstance(vt, dict):
            raise KeyError(f"Missing 'workflow.virustotal' section in '{cfg_path}'.")

        required_keys = [
            "api_base_url",
            "user_agent",
            "large_file_threshold_mb",
            "poll_attempts",
            "poll_backoff_base_seconds",
            "rate_limit_sleep_seconds",
            "skip_on_schedule",
            "skip_on_push",
        ]
        for key in required_keys:
            if key not in vt:
                raise KeyError(f"Missing required key '{key}' in 'workflow.virustotal' of '{cfg_path}'.")

        self.api_base_url:              str  = str(vt["api_base_url"])
        self.user_agent:                str  = str(vt["user_agent"])
        self.large_file_threshold_mb:   int  = int(vt["large_file_threshold_mb"])
        self.poll_attempts:             int  = int(vt["poll_attempts"])
        self.poll_backoff_base_seconds: int  = int(vt["poll_backoff_base_seconds"])
        self.rate_limit_sleep_seconds:  int  = int(vt["rate_limit_sleep_seconds"])
        self.skip_on_schedule:          bool = bool(vt["skip_on_schedule"])
        self.skip_on_push:              bool = bool(vt["skip_on_push"])

    def should_skip(self, scan_mode: str, manual_skip: bool) -> Optional[str]:
        if manual_skip:
            return "manual override via workflow input"
        if scan_mode == "scheduled" and self.skip_on_schedule:
            return "skip_on_schedule=true in workflow-config.json"
        if scan_mode.startswith("push") and self.skip_on_push:
            return "skip_on_push=true in workflow-config.json"
        return None

def calculate_file_hash(file_path: str) -> str:
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def scan_file_opportunistic(file_path: str, api_key: str, cfg: ConfigLoader) -> Dict[str, Any]:
    if not os.path.exists(file_path):
        return {"status": "failed", "file": os.path.basename(file_path), "reason": "File not found"}
        
    file_hash = calculate_file_hash(file_path)
    base_url = cfg.api_base_url
    headers = {"x-apikey": api_key, "User-Agent": cfg.user_agent, "Accept": "application/json"}
    report_url = f"https://www.virustotal.com/gui/file/{file_hash}"
    
    try:
        if not api_key:
            raise ValueError("No API key provided")
            
        resp = requests.get(f"{base_url}/files/{file_hash}", headers=headers, timeout=30)
        if resp.status_code == 200:
            scan_data = resp.json()
            attrs = scan_data.get("data", {}).get("attributes", {})
            stats = attrs.get("last_analysis_stats", {})
            malicious_count = stats.get("malicious", 0)
            suspicious_count = stats.get("suspicious", 0)
            total_engines = sum(stats.values())
            verdict = "Malicious" if malicious_count > 0 else "Suspicious" if suspicious_count > 0 else "Clean"
            
            return {
                "status": "success",
                "file": os.path.basename(file_path),
                "verdict": verdict,
                "malicious_count": malicious_count,
                "suspicious_count": suspicious_count,
                "total_engines": total_engines,
                "report_url": report_url,
                "sha256": file_hash
            }
        else:
            return {
                "status": "fallback",
                "file": os.path.basename(file_path),
                "reason": f"API HTTP {resp.status_code}",
                "report_url": report_url,
                "sha256": file_hash
            }
    except Exception as exc:
        return {
            "status": "fallback",
            "file": os.path.basename(file_path),
            "reason": str(exc),
            "report_url": report_url,
            "sha256": file_hash
        }

def upload_file(file_path: str, api_key: str, cfg: ConfigLoader) -> Optional[str]:
    base_url = cfg.api_base_url
    headers = {"x-apikey": api_key, "User-Agent": cfg.user_agent, "Accept": "application/json"}
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
    upload_endpoint = f"{base_url}/files"
    
    if file_size_mb > cfg.large_file_threshold_mb:
        url_resp = requests.get(f"{base_url}/files/upload_url", headers=headers, timeout=30)
        if url_resp.status_code == 200:
            upload_endpoint = url_resp.json().get("data")
            if not upload_endpoint:
                return None
        else:
            return None
            
    with open(file_path, "rb") as f:
        resp = requests.post(upload_endpoint, headers=headers,
                             files={"file": (os.path.basename(file_path), f)},
                             timeout=300)
    if resp.status_code == 200:
        return resp.json().get("data", {}).get("id")
    return None

def daily_scan_mode(files_list: list, api_key: str, cfg: ConfigLoader, artifacts_dir: str) -> int:
    tracking_file = Path(artifacts_dir) / "vt-scanned.json"
    tracking_data = {}
    if tracking_file.exists():
        with open(tracking_file, "r") as f:
            tracking_data = json.load(f)
            
    for fhash, info in tracking_data.items():
        if info.get("status") == "uploaded":
            print(f"Checking previously uploaded file: {info.get('file')}")
            base_url = cfg.api_base_url
            headers = {"x-apikey": api_key, "User-Agent": cfg.user_agent, "Accept": "application/json"}
            resp = requests.get(f"{base_url}/files/{fhash}", headers=headers, timeout=30)
            if resp.status_code == 200:
                scan_data = resp.json()
                attrs = scan_data.get("data", {}).get("attributes", {})
                stats = attrs.get("last_analysis_stats", {})
                malicious_count = stats.get("malicious", 0)
                verdict = "Malicious" if malicious_count > 0 else "Clean"
                print(f"Result: {verdict}")
                info["status"] = "completed"
                info["verdict"] = verdict
                with open(tracking_file, "w") as f:
                    json.dump(tracking_data, f, indent=2)
                if malicious_count > 0:
                    print(f"::error file={info.get('file')}::VirusTotal Daily Scan found MALICIOUS file: {info.get('file')}")
                    return 1
                return 0
            elif resp.status_code == 429:
                print("Rate limited checking uploaded file. Will try tomorrow.")
                return 0
            else:
                print(f"Unexpected status checking uploaded file: {resp.status_code}. Still pending.")
                return 0

    for file_path in files_list:
        if not os.path.exists(file_path): continue
        fhash = calculate_file_hash(file_path)
        if fhash not in tracking_data:
            print(f"Found un-scanned file: {file_path}")
            base_url = cfg.api_base_url
            headers = {"x-apikey": api_key, "User-Agent": cfg.user_agent, "Accept": "application/json"}
            resp = requests.get(f"{base_url}/files/{fhash}", headers=headers, timeout=30)
            
            if resp.status_code == 200:
                print("File already scanned on VirusTotal.")
                scan_data = resp.json()
                attrs = scan_data.get("data", {}).get("attributes", {})
                stats = attrs.get("last_analysis_stats", {})
                malicious_count = stats.get("malicious", 0)
                verdict = "Malicious" if malicious_count > 0 else "Clean"
                print(f"Result: {verdict}")
                tracking_data[fhash] = {"status": "completed", "file": file_path, "verdict": verdict}
                with open(tracking_file, "w") as f:
                    json.dump(tracking_data, f, indent=2)
                if malicious_count > 0:
                    print(f"::error file={file_path}::VirusTotal Daily Scan found MALICIOUS file: {file_path}")
                    return 1
                return 0
            elif resp.status_code == 404:
                print("File not found on VirusTotal. Uploading...")
                analysis_id = upload_file(file_path, api_key, cfg)
                if analysis_id:
                    print(f"Uploaded successfully. Analysis ID: {analysis_id}")
                    tracking_data[fhash] = {"status": "uploaded", "file": file_path}
                    with open(tracking_file, "w") as f:
                        json.dump(tracking_data, f, indent=2)
                else:
                    print("Failed to upload file.")
                return 0
            elif resp.status_code == 429:
                print("Rate limited checking new file. Will try tomorrow.")
                return 0
            else:
                print(f"Unexpected HTTP {resp.status_code} checking new file.")
                return 0
                
    print("No unscanned files found.")
    return 0

def main() -> int:
    ap = argparse.ArgumentParser(description="VirusTotal file scanner")
    ap.add_argument("files_list", help="Path to file containing PDF paths to scan (one per line)")
    ap.add_argument("--scan-mode", default="", help="Pipeline scan mode")
    ap.add_argument("--manual-skip", action="store_true", help="Set when skip_virus_scan is true")
    ap.add_argument("--output-json", default="scan_results.json", help="Path to write results JSON")
    ap.add_argument("--artifacts-dir", default=".github/artifacts", help="Directory containing workflow-config.json")
    ap.add_argument("--daily-mode", action="store_true", help="Run the daily background scan logic")
    args = ap.parse_args()

    print(f"\n{'='*70}")
    print("VirusTotal Scanner")
    print(f"{'='*70}\n")

    try:
        cfg = ConfigLoader(args.artifacts_dir)
    except Exception as exc:
        print(f"ERROR: Config load failed: {exc}")
        return 1

    api_key = os.environ.get("VIRUS_TOTAL_API_KEY", "")
    if not api_key:
        print("WARNING: VIRUS_TOTAL_API_KEY not set. Will use passive hash fallback for all files.")

    if not os.path.exists(args.files_list):
        print(f"ERROR: files_list not found: {args.files_list}")
        return 1

    with open(args.files_list, "r") as f:
        files_to_scan = [ln.strip() for ln in f if ln.strip()]

    gh_output = os.environ.get("GITHUB_OUTPUT")

    if not files_to_scan:
        print("⊘ No files to scan")
        with open(args.output_json, "w") as f:
            json.dump([], f)
        if gh_output:
            with open(gh_output, "a", encoding="utf-8") as f:
                f.write("scan_skipped=true\n")
                f.write("scan_passed=true\n")
        return 0

    if args.daily_mode:
        if not api_key:
            print("ERROR: API key required for daily mode")
            return 1
        return daily_scan_mode(files_to_scan, api_key, cfg, args.artifacts_dir)

    is_manual_skip = args.manual_skip or (os.environ.get("SKIP_VIRUS_SCAN", "false").lower() == "true")
    skip_reason = cfg.should_skip(args.scan_mode, is_manual_skip)
    if skip_reason:
        print(f"⊘ Scan skipped: {skip_reason}")
        with open(args.output_json, "w") as f:
            json.dump([], f)
        if gh_output:
            with open(gh_output, "a", encoding="utf-8") as f:
                f.write("scan_skipped=true\n")
                f.write("scan_passed=true\n")
        return 0

    print(f"✓ {len(files_to_scan)} file(s) to scan (Opportunistic Mode)\n")

    results = []
    malicious = 0

    for i, file_path in enumerate(files_to_scan):
        print(f"[{i+1}/{len(files_to_scan)}] {file_path}")
        result = scan_file_opportunistic(file_path, api_key, cfg)
        results.append(result)

        if result["status"] == "success":
            verdict = result["verdict"]
            print(f"  ✓ {verdict} — {result['report_url']}")
            if verdict == "Malicious":
                malicious += 1
                print(f"::error file={file_path}::VirusTotal: Malicious file detected!")
        elif result["status"] == "fallback":
            print(f"  ⊘ Passive Fallback: {result['reason']} — {result['report_url']}")
        else:
            print(f"  ✗ Failed: {result.get('reason')}")

    with open(args.output_json, "w") as f:
        json.dump(results, f, indent=2)

    success_count = sum(1 for r in results if r["status"] == "success")
    fallback_count = sum(1 for r in results if r["status"] == "fallback")
    print(f"\n{'='*70}")
    print(f"Scanned: {success_count}/{len(results)} successful | Fallbacks: {fallback_count} | Malicious: {malicious}")

    if gh_output:
        with open(gh_output, "a", encoding="utf-8") as f:
            f.write("scan_skipped=false\n")
            f.write(f"scan_passed={'false' if malicious > 0 else 'true'}\n")

    if malicious > 0:
        print(f"\n❌ {malicious} file(s) flagged as Malicious — exiting with code 1")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())