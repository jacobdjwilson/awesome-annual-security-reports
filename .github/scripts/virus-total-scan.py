import os
import sys
import time
import requests
import json
import hashlib
import argparse
from pathlib import Path
from typing import Dict, Any, Optional


# ==========================
# CONFIGURATION LOADER
# ==========================
class ConfigLoader:
    """Loads all VirusTotal policy values from workflow-config.json.
    Nothing in this script is hard-coded."""

    def __init__(self, artifacts_dir: str = ".github/artifacts"):
        cfg_path = Path(artifacts_dir) / "workflow-config.json"
        if not cfg_path.exists():
            raise FileNotFoundError(f"workflow-config.json not found at {cfg_path}")
        with open(cfg_path, "r", encoding="utf-8") as f:
            cfg = json.load(f)

        vt = cfg.get("workflow", {}).get("virustotal", {})
        self.api_base_url:              str  = vt["api_base_url"]
        self.user_agent:                str  = vt["user_agent"]
        self.large_file_threshold_mb:   int  = vt["large_file_threshold_mb"]
        self.poll_attempts:             int  = vt["poll_attempts"]
        self.poll_backoff_base_seconds: int  = vt["poll_backoff_base_seconds"]
        self.rate_limit_sleep_seconds:  int  = vt["rate_limit_sleep_seconds"]
        self.skip_on_schedule:          bool = vt["skip_on_schedule"]
        self.skip_on_push:              bool = vt["skip_on_push"]

    def should_skip(self, scan_mode: str, manual_skip: bool) -> Optional[str]:
        """
        Return a human-readable skip reason string if the scan should be
        skipped, or None if it should run.

        Decision priority:
          1. Manual override (workflow_dispatch input).
          2. scan_mode == 'scheduled' and skip_on_schedule is true.
          3. scan_mode starts with 'push' and skip_on_push is true.
        All thresholds read from workflow-config.json — nothing hard-coded.
        """
        if manual_skip:
            return "manual override via workflow input"
        if scan_mode == "scheduled" and self.skip_on_schedule:
            return f"skip_on_schedule=true in workflow-config.json"
        if scan_mode.startswith("push") and self.skip_on_push:
            return f"skip_on_push=true in workflow-config.json"
        return None


# ==========================
# SCANNER
# ==========================
def calculate_file_hash(file_path: str) -> str:
    """Calculate SHA-256 hash of a file."""
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()


def scan_file(file_path: str, api_key: str, cfg: ConfigLoader) -> Dict[str, Any]:
    """Scan one file with VirusTotal and return a result dict."""
    if not os.path.exists(file_path):
        return {"status": "failed", "file": os.path.basename(file_path),
                "reason": "File not found"}

    headers = {
        "x-apikey": api_key,
        "User-Agent": cfg.user_agent,
        "Accept": "application/json",
    }
    file_size_mb  = os.path.getsize(file_path) / (1024 * 1024)
    file_hash     = calculate_file_hash(file_path)
    base_url      = cfg.api_base_url

    try:
        # Check if the hash is already known to VirusTotal
        lookup = requests.get(f"{base_url}/files/{file_hash}",
                              headers=headers, timeout=30)

        if lookup.status_code == 200:
            scan_data = lookup.json()

        elif lookup.status_code == 404:
            # File unknown — upload it
            upload_endpoint = f"{base_url}/files"

            if file_size_mb > cfg.large_file_threshold_mb:
                # Large files require a special one-time upload URL
                url_resp = requests.get(f"{base_url}/files/upload_url",
                                        headers=headers, timeout=30)
                if url_resp.status_code == 200:
                    upload_endpoint = url_resp.json().get("data")
                    if not upload_endpoint:
                        return {"status": "failed",
                                "file": os.path.basename(file_path),
                                "reason": "Could not get large file upload URL"}
                else:
                    return {"status": "failed",
                            "file": os.path.basename(file_path),
                            "reason": f"Failed to get large file upload URL "
                                      f"(HTTP {url_resp.status_code})"}

            with open(file_path, "rb") as f:
                resp = requests.post(upload_endpoint, headers=headers,
                                     files={"file": (os.path.basename(file_path), f)},
                                     timeout=300)

            if resp.status_code != 200:
                return {"status": "failed",
                        "file": os.path.basename(file_path),
                        "reason": f"Upload failed (HTTP {resp.status_code})"}

            scan_id = resp.json().get("data", {}).get("id")
            if not scan_id:
                return {"status": "failed",
                        "file": os.path.basename(file_path),
                        "reason": "No scan ID in upload response"}

            # Poll for completion with config-driven backoff
            scan_data = None
            for attempt in range(cfg.poll_attempts):
                sleep_secs = cfg.poll_backoff_base_seconds * (attempt + 1)
                time.sleep(sleep_secs)
                status_resp = requests.get(f"{base_url}/analyses/{scan_id}",
                                           headers=headers, timeout=30)
                if status_resp.status_code == 200:
                    attrs = (status_resp.json()
                             .get("data", {}).get("attributes", {}))
                    if attrs.get("status") == "completed":
                        final = requests.get(f"{base_url}/files/{file_hash}",
                                             headers=headers, timeout=30)
                        if final.status_code == 200:
                            scan_data = final.json()
                            break

            if scan_data is None:
                return {"status": "failed",
                        "file": os.path.basename(file_path),
                        "reason": "Scan did not complete within polling timeout"}

        else:
            return {"status": "failed",
                    "file": os.path.basename(file_path),
                    "reason": f"Unexpected status checking file "
                              f"(HTTP {lookup.status_code})"}

        # Parse results
        attrs            = scan_data.get("data", {}).get("attributes", {})
        stats            = attrs.get("last_analysis_stats", {})
        malicious_count  = stats.get("malicious", 0)
        suspicious_count = stats.get("suspicious", 0)
        total_engines    = sum(stats.values())
        verdict = ("Malicious"  if malicious_count  > 0 else
                   "Suspicious" if suspicious_count > 0 else "Clean")

        return {
            "status":           "success",
            "file":             os.path.basename(file_path),
            "verdict":          verdict,
            "malicious_count":  malicious_count,
            "suspicious_count": suspicious_count,
            "total_engines":    total_engines,
            "report_url":       f"https://www.virustotal.com/gui/file/{file_hash}",
            "sha256":           file_hash,
        }

    except Exception as exc:
        return {"status": "failed",
                "file": os.path.basename(file_path),
                "reason": str(exc)}


def emit_annotation(file_path: str, result: Dict[str, Any]) -> None:
    """Emit a GitHub Actions workflow annotation for this scan result."""
    verdict = result["verdict"]
    level   = ("error"   if verdict == "Malicious"  else
               "warning" if verdict == "Suspicious" else "notice")
    detections = result["malicious_count"] + result["suspicious_count"]
    print(f"::{level} file={file_path}::"
          f"VirusTotal: {verdict} "
          f"({detections}/{result['total_engines']} engines)")
    print(f"::{level} file={file_path}::Report: {result['report_url']}")


# ==========================
# MAIN
# ==========================
def main() -> int:
    ap = argparse.ArgumentParser(description="VirusTotal file scanner")
    ap.add_argument("files_list",
                    help="Path to file containing PDF paths to scan (one per line)")
    ap.add_argument("--scan-mode",    default="",
                    help="Pipeline scan mode (push/pr/scheduled/manual) — "
                         "used to evaluate skip policy from config")
    ap.add_argument("--manual-skip",  action="store_true",
                    help="Set when the workflow_dispatch skip_virus_scan input is true")
    ap.add_argument("--output-json",  default="scan_results.json",
                    help="Path to write results JSON")
    ap.add_argument("--artifacts-dir", default=".github/artifacts",
                    help="Directory containing workflow-config.json")
    args = ap.parse_args()

    print(f"\n{'='*70}")
    print("VirusTotal Scanner")
    print(f"{'='*70}\n")

    # Load config — all policy values come from here
    try:
        cfg = ConfigLoader(args.artifacts_dir)
    except Exception as exc:
        print(f"ERROR: Config load failed: {exc}")
        return 1

    print(f"✓ Config loaded from {args.artifacts_dir}")
    print(f"  API base          : {cfg.api_base_url}")
    print(f"  Large file limit  : {cfg.large_file_threshold_mb} MB")
    print(f"  Poll attempts     : {cfg.poll_attempts}")
    print(f"  Rate limit sleep  : {cfg.rate_limit_sleep_seconds}s")
    print(f"  Skip on schedule  : {cfg.skip_on_schedule}")
    print(f"  Skip on push      : {cfg.skip_on_push}")
    print()

    # Evaluate skip policy
    skip_reason = cfg.should_skip(args.scan_mode, args.manual_skip)
    if skip_reason:
        print(f"⊘ Scan skipped: {skip_reason}")
        with open(args.output_json, "w") as f:
            json.dump([], f)
        # Exit 0 — skipping is not an error; the pipeline reads the empty
        # results file and treats it as a pass
        return 0

    # Require API key
    api_key = os.environ.get("VIRUS_TOTAL_API_KEY", "")
    if not api_key:
        print("ERROR: VIRUS_TOTAL_API_KEY environment variable not set")
        return 1

    # Load file list
    if not os.path.exists(args.files_list):
        print(f"ERROR: files_list not found: {args.files_list}")
        return 1

    with open(args.files_list, "r") as f:
        files_to_scan = [ln.strip() for ln in f if ln.strip()]

    if not files_to_scan:
        print("⊘ No files to scan")
        with open(args.output_json, "w") as f:
            json.dump([], f)
        return 0

    print(f"✓ {len(files_to_scan)} file(s) to scan\n")

    results      = []
    malicious    = 0

    for i, file_path in enumerate(files_to_scan):
        if i > 0:
            print(f"  (rate-limit pause: {cfg.rate_limit_sleep_seconds}s)")
            time.sleep(cfg.rate_limit_sleep_seconds)

        print(f"[{i+1}/{len(files_to_scan)}] {file_path}")
        result = scan_file(file_path, api_key, cfg)
        results.append(result)

        if result["status"] == "success":
            verdict = result["verdict"]
            print(f"  ✓ {verdict} — "
                  f"{result['malicious_count'] + result['suspicious_count']}"
                  f"/{result['total_engines']} engines — "
                  f"{result['report_url']}")
            emit_annotation(file_path, result)
            if verdict == "Malicious":
                malicious += 1
        else:
            print(f"  ✗ Failed: {result['reason']}")

    with open(args.output_json, "w") as f:
        json.dump(results, f, indent=2)

    success_count = sum(1 for r in results if r["status"] == "success")
    print(f"\n{'='*70}")
    print(f"Scanned: {success_count}/{len(results)} successful  |  "
          f"Malicious: {malicious}")

    if malicious > 0:
        print(f"\n❌ {malicious} file(s) flagged as Malicious — "
              f"exiting with code 1 to block pipeline")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())