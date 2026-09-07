"""
Operational Purpose:
    Scans PDF files against the VirusTotal v3 API (via file upload or opportunistic SHA-256 hash lookup),
    evaluating detection stats, enforcing a 24-hour cache freshness policy, and progressing daily submissions.

Required Environment Variables:
    VIRUS_TOTAL_API_KEY (optional): VirusTotal v3 API key.
    SKIP_VIRUS_SCAN (optional): If 'true', skips scanning.
    GITHUB_OUTPUT (optional): Path to write step outputs.

Outputs:
    scan_skipped (bool): 'true' if scan was bypassed, 'false' otherwise.
    scan_passed (bool): 'true' if no files were flagged malicious and scan completed.
    unseen_count (int): Count of files not yet on VirusTotal.
    uploaded_file (str): Path of file uploaded in daily run if applicable.
    completed_count (int): Count of files with completed scans on VirusTotal.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.virustotal)
"""

import os
import sys
import time
import json
import hashlib
import argparse
import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List

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
            "cache_ttl_hours",
            "daily_scan_max_lookups",
            "tracking_cache_file",
            "unseen_output_file",
            "unseen_output_json",
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
        self.cache_ttl_hours:           int  = int(vt["cache_ttl_hours"])
        self.daily_scan_max_lookups:    int  = int(vt["daily_scan_max_lookups"])
        self.tracking_cache_file:       str  = str(vt["tracking_cache_file"])
        self.unseen_output_file:        str  = str(vt["unseen_output_file"])
        self.unseen_output_json:        str  = str(vt["unseen_output_json"])

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


def is_cache_fresh(entry: Optional[Dict[str, Any]], ttl_hours: int) -> bool:
    """Returns True if the file entry has been evaluated within ttl_hours or is confirmed clean."""
    if not entry or not isinstance(entry, dict):
        return False

    status = entry.get("status")
    if status not in ("completed", "uploaded"):
        return False

    last_checked = entry.get("last_checked")
    if not last_checked:
        return status == "completed" and entry.get("verdict") == "Clean"

    try:
        ts = last_checked.replace("Z", "+00:00")
        checked_dt = datetime.datetime.fromisoformat(ts)
        now_dt = datetime.datetime.now(datetime.timezone.utc)
        age_seconds = (now_dt - checked_dt).total_seconds()
        return -300 <= age_seconds < (ttl_hours * 3600)
    except Exception:
        return False


def scan_file_opportunistic(
    file_path: str,
    api_key: str,
    cfg: ConfigLoader,
    fhash: Optional[str] = None
) -> Dict[str, Any]:
    if not os.path.exists(file_path):
        return {"status": "failed", "file": os.path.basename(file_path), "reason": "File not found"}

    file_hash = fhash or calculate_file_hash(file_path)
    base_url = cfg.api_base_url
    headers = {"x-apikey": api_key, "User-Agent": cfg.user_agent, "Accept": "application/json"}
    report_url = f"https://www.virustotal.com/gui/file/{file_hash}"

    try:
        if not api_key:
            raise ValueError("No API key provided")

        resp = requests.get(f"{base_url}/files/{file_hash}", headers=headers, timeout=30)
        if resp.status_code == 429:
            print(f"  ⚠ Rate limited (HTTP 429), waiting {cfg.rate_limit_sleep_seconds}s before retry...")
            time.sleep(cfg.rate_limit_sleep_seconds)
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
                "http_code": 200,
                "file": os.path.basename(file_path),
                "verdict": verdict,
                "malicious_count": malicious_count,
                "suspicious_count": suspicious_count,
                "total_engines": total_engines,
                "report_url": report_url,
                "sha256": file_hash,
            }
        elif resp.status_code == 404:
            return {
                "status": "fallback",
                "http_code": 404,
                "file": os.path.basename(file_path),
                "reason": "File not yet seen on VirusTotal (HTTP 404)",
                "report_url": report_url,
                "sha256": file_hash,
            }
        else:
            reason_text = "Rate limited (HTTP 429)" if resp.status_code == 429 else f"API HTTP {resp.status_code}"
            return {
                "status": "fallback",
                "http_code": resp.status_code,
                "file": os.path.basename(file_path),
                "reason": reason_text,
                "report_url": report_url,
                "sha256": file_hash,
            }
    except Exception as exc:
        return {
            "status": "fallback",
            "http_code": 0,
            "file": os.path.basename(file_path),
            "reason": str(exc),
            "report_url": report_url,
            "sha256": file_hash,
        }


def upload_file(file_path: str, api_key: str, cfg: ConfigLoader) -> Optional[str]:
    base_url = cfg.api_base_url
    headers = {"x-apikey": api_key, "User-Agent": cfg.user_agent, "Accept": "application/json"}
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
    upload_endpoint = f"{base_url}/files"

    if file_size_mb > cfg.large_file_threshold_mb:
        try:
            url_resp = requests.get(f"{base_url}/files/upload_url", headers=headers, timeout=30)
            if url_resp.status_code == 200:
                upload_endpoint = url_resp.json().get("data")
                if not upload_endpoint:
                    return None
            else:
                return None
        except Exception:
            return None

    try:
        with open(file_path, "rb") as f:
            resp = requests.post(
                upload_endpoint,
                headers=headers,
                files={"file": (os.path.basename(file_path), f)},
                timeout=300,
            )
        if resp.status_code == 200:
            return resp.json().get("data", {}).get("id")
    except Exception as e:
        print(f"  Upload error for {file_path}: {e}")
    return None


def _save_tracking_data(tracking_file: Path, tracking_data: Dict[str, Any]) -> None:
    try:
        tracking_file.parent.mkdir(parents=True, exist_ok=True)
        with open(tracking_file, "w", encoding="utf-8") as f:
            json.dump(tracking_data, f, indent=2)
    except Exception as e:
        print(f"Warning: Failed to save tracking data to {tracking_file}: {e}")


def _export_unseen_artifacts(tracking_data: Dict[str, Any], cfg: ConfigLoader) -> int:
    unseen_list = []
    for fhash, info in tracking_data.items():
        if info.get("status") in ("unseen", "uploaded"):
            unseen_list.append({
                "file": info.get("file"),
                "sha256": fhash,
                "status": info.get("status"),
                "last_checked": info.get("last_checked", ""),
                "upload_date": info.get("upload_date", ""),
            })

    unseen_list.sort(key=lambda x: str(x.get("file", "")))

    unseen_txt_path = Path(cfg.unseen_output_file)
    try:
        with open(unseen_txt_path, "w", encoding="utf-8") as f:
            for item in unseen_list:
                if item.get("file"):
                    f.write(f"{item['file']}\n")
    except Exception as e:
        print(f"Warning: Failed to write {unseen_txt_path}: {e}")

    unseen_json_path = Path(cfg.unseen_output_json)
    try:
        with open(unseen_json_path, "w", encoding="utf-8") as f:
            json.dump(unseen_list, f, indent=2)
    except Exception as e:
        print(f"Warning: Failed to write {unseen_json_path}: {e}")

    return len(unseen_list)


def daily_scan_mode(files_list: List[str], api_key: str, cfg: ConfigLoader, artifacts_dir: str) -> int:
    tracking_file = Path(artifacts_dir) / cfg.tracking_cache_file
    tracking_data: Dict[str, Any] = {}
    if tracking_file.exists():
        try:
            with open(tracking_file, "r", encoding="utf-8") as f:
                tracking_data = json.load(f)
        except Exception as e:
            print(f"Warning: Failed to load existing tracking file {tracking_file}: {e}")
            tracking_data = {}

    headers = {"x-apikey": api_key, "User-Agent": cfg.user_agent, "Accept": "application/json"}
    base_url = cfg.api_base_url
    now_iso = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Step 1: Check previously uploaded files awaiting analysis completion
    for fhash, info in list(tracking_data.items()):
        if info.get("status") == "uploaded":
            file_name = info.get("file", fhash)
            print(f"Checking previously uploaded file: {file_name}")
            try:
                resp = requests.get(f"{base_url}/files/{fhash}", headers=headers, timeout=30)
                if resp.status_code == 200:
                    scan_data = resp.json()
                    attrs = scan_data.get("data", {}).get("attributes", {})
                    stats = attrs.get("last_analysis_stats", {})
                    malicious_count = stats.get("malicious", 0)
                    suspicious_count = stats.get("suspicious", 0)
                    total_engines = sum(stats.values())
                    verdict = "Malicious" if malicious_count > 0 else "Suspicious" if suspicious_count > 0 else "Clean"
                    print(f"  Analysis complete for uploaded file: {verdict}")
                    info["status"] = "completed"
                    info["verdict"] = verdict
                    info["last_checked"] = now_iso
                    info["malicious_count"] = malicious_count
                    info["suspicious_count"] = suspicious_count
                    info["total_engines"] = total_engines
                    info["report_url"] = f"https://www.virustotal.com/gui/file/{fhash}"
                    _save_tracking_data(tracking_file, tracking_data)

                    if malicious_count > 0:
                        print(f"::error file={file_name}::VirusTotal Daily Scan found MALICIOUS file: {file_name}")
                        _export_unseen_artifacts(tracking_data, cfg)
                        return 1
                elif resp.status_code == 429:
                    print("  Rate limited checking uploaded file (HTTP 429). Will retry tomorrow.")
                    break
                else:
                    print(f"  Analysis still pending (HTTP {resp.status_code}).")
            except Exception as e:
                print(f"  Error checking uploaded file {fhash}: {e}")

    # Step 2: Query untracked files up to daily_scan_max_lookups
    lookups_performed = 0
    quota_exhausted = False
    uploaded_file_path: Optional[str] = None

    has_active_upload = any(info.get("status") == "uploaded" for info in tracking_data.values())

    for file_path in files_list:
        if not os.path.exists(file_path):
            continue

        fhash = calculate_file_hash(file_path)

        # Skip files already scanned or already known to be unseen/uploaded
        if fhash in tracking_data:
            entry = tracking_data[fhash]
            if entry.get("status") in ("completed", "unseen", "uploaded"):
                continue

        if lookups_performed >= cfg.daily_scan_max_lookups:
            print(f"Reached daily lookup limit ({cfg.daily_scan_max_lookups}). Halting new lookups for today.")
            break

        print(f"[{lookups_performed + 1}/{cfg.daily_scan_max_lookups}] Checking untracked file: {file_path}")
        try:
            if lookups_performed > 0:
                time.sleep(cfg.rate_limit_sleep_seconds)

            resp = requests.get(f"{base_url}/files/{fhash}", headers=headers, timeout=30)
            lookups_performed += 1

            if resp.status_code == 200:
                scan_data = resp.json()
                attrs = scan_data.get("data", {}).get("attributes", {})
                stats = attrs.get("last_analysis_stats", {})
                malicious_count = stats.get("malicious", 0)
                suspicious_count = stats.get("suspicious", 0)
                total_engines = sum(stats.values())
                verdict = "Malicious" if malicious_count > 0 else "Suspicious" if suspicious_count > 0 else "Clean"
                print(f"  ✓ Already scanned on VirusTotal: {verdict}")

                tracking_data[fhash] = {
                    "status": "completed",
                    "file": file_path,
                    "verdict": verdict,
                    "sha256": fhash,
                    "last_checked": now_iso,
                    "malicious_count": malicious_count,
                    "suspicious_count": suspicious_count,
                    "total_engines": total_engines,
                    "report_url": f"https://www.virustotal.com/gui/file/{fhash}",
                }
                _save_tracking_data(tracking_file, tracking_data)

                if malicious_count > 0:
                    print(f"::error file={file_path}::VirusTotal Daily Scan found MALICIOUS file: {file_path}")
                    _export_unseen_artifacts(tracking_data, cfg)
                    return 1

            elif resp.status_code == 404:
                print("  ⊘ Not found on VirusTotal (404) -> Added to unseen submission queue.")
                tracking_data[fhash] = {
                    "status": "unseen",
                    "file": file_path,
                    "sha256": fhash,
                    "last_checked": now_iso,
                }
                _save_tracking_data(tracking_file, tracking_data)

            elif resp.status_code == 429:
                print("  ⚠ VirusTotal rate limit / quota exceeded (HTTP 429). Halting queries for today.")
                quota_exhausted = True
                break
            else:
                print(f"  Unexpected HTTP {resp.status_code} for {file_path}.")

        except Exception as e:
            print(f"  Error checking {file_path}: {e}")

    # Step 3: Upload 1 unseen file (enforcing 1 upload per day quota)
    if not has_active_upload and not quota_exhausted:
        unseen_candidates = [
            (fhash, info) for fhash, info in tracking_data.items()
            if info.get("status") == "unseen" and os.path.exists(info.get("file", ""))
        ]
        if unseen_candidates:
            target_hash, target_info = unseen_candidates[0]
            target_path = target_info["file"]
            print(f"\nUploading 1 unscanned file to VirusTotal (daily limit = 1): {target_path}")
            time.sleep(cfg.rate_limit_sleep_seconds)
            analysis_id = upload_file(target_path, api_key, cfg)
            if analysis_id:
                print(f"  ✓ Uploaded successfully. Analysis ID: {analysis_id}")
                target_info["status"] = "uploaded"
                target_info["analysis_id"] = analysis_id
                target_info["upload_date"] = now_iso
                uploaded_file_path = target_path
                _save_tracking_data(tracking_file, tracking_data)
            else:
                print(f"  ✗ Failed to upload {target_path}.")
        else:
            print("\nNo unseen files waiting in queue for upload.")

    # Step 4: Export unseen files artifacts
    unseen_count = _export_unseen_artifacts(tracking_data, cfg)

    # Step 5: Summary and outputs
    completed_count = sum(1 for info in tracking_data.values() if info.get("status") == "completed")

    print(f"\n{'='*70}")
    print("VirusTotal Daily Scan Summary:")
    print(f"  Completed / Clean on VT : {completed_count}")
    print(f"  Unseen Queue            : {unseen_count}")
    print(f"  Lookups Performed Today : {lookups_performed}")
    print(f"  File Uploaded Today     : {uploaded_file_path or 'None'}")
    print(f"{'='*70}\n")

    gh_output = os.environ.get("GITHUB_OUTPUT")
    if gh_output:
        with open(gh_output, "a", encoding="utf-8") as f:
            f.write("scan_skipped=false\n")
            f.write("scan_passed=true\n")
            f.write(f"unseen_count={unseen_count}\n")
            f.write(f"uploaded_file={uploaded_file_path or ''}\n")
            f.write(f"completed_count={completed_count}\n")

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

    with open(args.files_list, "r", encoding="utf-8", errors="replace") as f:
        files_to_scan = [ln.strip() for ln in f if ln.strip()]

    gh_output = os.environ.get("GITHUB_OUTPUT")

    if not files_to_scan:
        print("⊘ No files to scan")
        with open(args.output_json, "w", encoding="utf-8") as f:
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
        with open(args.output_json, "w", encoding="utf-8") as f:
            json.dump([], f)
        if gh_output:
            with open(gh_output, "a", encoding="utf-8") as f:
                f.write("scan_skipped=true\n")
                f.write("scan_passed=true\n")
        return 0

    print(f"✓ {len(files_to_scan)} file(s) to scan (Opportunistic Mode)\n")

    tracking_file = Path(args.artifacts_dir) / cfg.tracking_cache_file
    tracking_data: Dict[str, Any] = {}
    if tracking_file.exists():
        try:
            with open(tracking_file, "r", encoding="utf-8") as f:
                tracking_data = json.load(f)
        except Exception as e:
            print(f"Warning: Failed to load tracking cache {tracking_file}: {e}")

    results = []
    malicious = 0
    cache_hits = 0
    cache_updated = False
    now_iso = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    for i, file_path in enumerate(files_to_scan):
        print(f"[{i+1}/{len(files_to_scan)}] {file_path}")
        if not os.path.exists(file_path):
            results.append({"status": "failed", "file": os.path.basename(file_path), "reason": "File not found"})
            continue

        fhash = calculate_file_hash(file_path)
        cached_entry = tracking_data.get(fhash)

        # Check 24-hour cache freshness policy
        if is_cache_fresh(cached_entry, cfg.cache_ttl_hours):
            cache_hits += 1
            verdict = cached_entry.get("verdict", "Clean")
            print(f"  ⚡ Using cached VirusTotal result (< {cfg.cache_ttl_hours}h old): {verdict} — {cached_entry.get('report_url', '')}")
            res = {
                "status": "cached",
                "file": os.path.basename(file_path),
                "verdict": verdict,
                "malicious_count": cached_entry.get("malicious_count", 0),
                "suspicious_count": cached_entry.get("suspicious_count", 0),
                "total_engines": cached_entry.get("total_engines", 0),
                "report_url": cached_entry.get("report_url", f"https://www.virustotal.com/gui/file/{fhash}"),
                "sha256": fhash,
            }
            results.append(res)
            if verdict == "Malicious":
                malicious += 1
                print(f"::error file={file_path}::VirusTotal: Malicious file detected in cache!")
            continue

        # Not fresh in cache -> query API
        result = scan_file_opportunistic(file_path, api_key, cfg, fhash=fhash)
        results.append(result)

        if result["status"] == "success":
            verdict = result["verdict"]
            print(f"  ✓ {verdict} — {result['report_url']}")
            tracking_data[fhash] = {
                "status": "completed",
                "file": file_path,
                "verdict": verdict,
                "sha256": fhash,
                "last_checked": now_iso,
                "malicious_count": result.get("malicious_count", 0),
                "suspicious_count": result.get("suspicious_count", 0),
                "total_engines": result.get("total_engines", 0),
                "report_url": result.get("report_url"),
            }
            cache_updated = True
            if verdict == "Malicious":
                malicious += 1
                print(f"::error file={file_path}::VirusTotal: Malicious file detected!")
        elif result.get("http_code") == 404:
            print(f"  ⊘ File unseen by VirusTotal (404) -> Enqueued for daily submission: {result['report_url']}")
            tracking_data[fhash] = {
                "status": "unseen",
                "file": file_path,
                "sha256": fhash,
                "last_checked": now_iso,
            }
            cache_updated = True
        elif result["status"] == "fallback":
            print(f"  ⊘ Passive Fallback: {result['reason']} — {result['report_url']}")
        else:
            print(f"  ✗ Failed: {result.get('reason')}")

        if api_key and i < len(files_to_scan) - 1:
            time.sleep(cfg.rate_limit_sleep_seconds)

    if cache_updated:
        _save_tracking_data(tracking_file, tracking_data)

    with open(args.output_json, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    success_count = sum(1 for r in results if r["status"] in ("success", "cached"))
    fallback_count = sum(1 for r in results if r["status"] == "fallback")
    print(f"\n{'='*70}")
    print(f"Scanned: {success_count}/{len(results)} clean/cached ({cache_hits} from cache) | Fallbacks: {fallback_count} | Malicious: {malicious}")

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