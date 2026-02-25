"""
google-search.py — Standalone Google Custom Search wrapper

Accepts a JSON file of search queries, executes each one against the
Google Custom Search JSON API, and writes a results JSON file.

Designed to be called from any GitHub Actions workflow step, or imported
as a module by other scripts (e.g. readme-updater.py) so that search
logic lives in exactly one place.

All credentials, endpoints, retry policy, scoring weights, and
skip-domain lists are read from .github/artifacts/google-search-config.json.
No values are hardcoded in this file.

Usage (CLI):
    python google-search.py \\
        --queries-json  queries.json \\
        --output-json   search_results.json \\
        --artifacts-dir .github/artifacts \\
        --mode          report_url

Input schema (queries.json):
    [
      {
        "id":           "upstream-2026",          // caller-defined correlation ID
        "organization": "Upstream",               // substituted into {organization}
        "title":        "Global Automotive Cybersecurity Report",
        "year":         "2026"
      },
      ...
    ]
    For "generic" mode, supply {"id": "...", "query": "raw search string"} instead.

Output schema (search_results.json):
    [
      {
        "id":     "upstream-2026",
        "status": "success" | "no_results" | "skipped" | "error",
        "query":  "Upstream \"Global Automotive...\" 2026 report",
        "url":    "https://upstream.auto/reports/...",
        "title":  "Global Automotive Cybersecurity Report 2026",
        "snippet":"...",
        "score":  8,
        "reason": ""           // populated on non-success statuses
      },
      ...
    ]
"""

import os
import sys
import json
import re
import time
import argparse
import urllib.parse
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

# ==========================
# DEPENDENCY CHECK
# ==========================
try:
    import requests
except ImportError:
    print("ERROR: requests required. Install: pip install requests")
    sys.exit(1)


# ==========================
# CONFIGURATION LOADER
# ==========================
class ConfigLoader:
    """
    Loads all Google Search settings from .github/artifacts/google-search-config.json.
    Nothing is hardcoded — credentials, endpoints, retry policy, per-mode scoring
    weights, and skip-domain lists are all sourced from the config file.
    """

    CONFIG_FILE = "google-search-config.json"

    def __init__(self, artifacts_dir: str = ".github/artifacts", mode: str = "report_url"):
        self.artifacts_dir = Path(artifacts_dir)
        self.mode          = mode

        raw = self._load_json(self.CONFIG_FILE)
        if not raw:
            raise ValueError(f"{self.CONFIG_FILE} is required but could not be loaded")

        cfg = raw.get("google_search", {})

        # ── API connection ────────────────────────────────────────────────
        self.base_url:         str = cfg.get("base_url", "https://www.googleapis.com/customsearch/v1")
        self.env_api_key:      str = cfg.get("env_api_key", "GOOGLE_SEARCH_API_KEY")
        self.env_cse_id:       str = cfg.get("env_cse_id",  "GOOGLE_CSE_ID")
        self.request_timeout:  int = cfg.get("request_timeout_seconds", 10)
        self.rate_limit_sleep: float = cfg.get("rate_limit_sleep_seconds", 1)

        # ── Retry policy ──────────────────────────────────────────────────
        retry = cfg.get("retry_policy", {})
        self.max_retries:   int   = retry.get("max_attempts",          3)
        self.initial_delay: float = retry.get("initial_delay_seconds", 2)
        self.backoff_mult:  float = retry.get("backoff_multiplier",    2)
        self.max_delay:     float = retry.get("max_delay_seconds",    15)

        # ── Mode-specific settings ────────────────────────────────────────
        modes = cfg.get("modes", {})
        if mode not in modes:
            available = ", ".join(modes.keys())
            raise ValueError(
                f"Unknown search mode '{mode}'. Available modes: {available}"
            )

        mode_cfg = modes[mode]
        self.query_template: str       = mode_cfg.get("query_template", "{query}")
        self.num_results:    int       = mode_cfg.get("num_results", 5)
        self.skip_domains:   List[str] = mode_cfg.get("skip_domains",   [])
        self.exclude_terms:  List[str] = mode_cfg.get("exclude_terms",  [])
        self.financial_terms:List[str] = mode_cfg.get("financial_terms",[])

        # Scoring weights (all default 0 so generic mode works with empty block)
        scoring = mode_cfg.get("scoring", {})
        self.score_org_in_link:      int = scoring.get("org_in_link",         0)
        self.score_year_in_link:     int = scoring.get("year_in_link",        0)
        self.score_report_in_link:   int = scoring.get("report_in_link",      0)
        self.score_year_in_title:    int = scoring.get("year_in_title",       0)
        self.score_org_in_title:     int = scoring.get("org_in_title",        0)
        self.score_short_path_penalty: int = scoring.get("short_path_penalty", 0)
        self.score_short_path_threshold: int = scoring.get("short_path_threshold", 3)

    def _load_json(self, filename: str) -> Optional[Dict[str, Any]]:
        path = self.artifacts_dir / filename
        if not path.exists():
            print(f"ERROR: {filename} not found at {path}")
            return None
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid JSON in {filename}: {e}")
            return None
        except Exception as e:
            print(f"ERROR: Could not read {filename}: {e}")
            return None


# ==========================
# GOOGLE SEARCH CLIENT
# ==========================
class GoogleSearchClient:
    """
    Executes Google Custom Search API queries with retry logic and result scoring.

    Credentials are read from the environment variables named in
    google-search-config.json (env_api_key, env_cse_id) — never hardcoded.
    """

    def __init__(self, config: ConfigLoader):
        self.config  = config
        self.api_key = os.environ.get(config.env_api_key, "")
        self.cse_id  = os.environ.get(config.env_cse_id,  "")

        self._available = bool(self.api_key and self.cse_id)
        if not self._available:
            print(
                f"⚠ Google Search credentials not found.\n"
                f"  Set {config.env_api_key} and {config.env_cse_id} "
                f"environment variables."
            )

    def is_available(self) -> bool:
        return self._available

    # ── Query builder ─────────────────────────────────────────────────────

    def build_query(self, query_record: Dict[str, Any]) -> str:
        """
        Substitute placeholders in the mode's query_template using fields
        from the query record.  Supports {organization}, {title}, {year},
        and {query} (generic mode).
        """
        q = self.config.query_template
        q = q.replace("{organization}", query_record.get("organization", ""))
        q = q.replace("{title}",        query_record.get("title",        ""))
        q = q.replace("{year}",         str(query_record.get("year",     "")))
        q = q.replace("{query}",        query_record.get("query",        ""))
        return q.strip()

    # ── Scoring ───────────────────────────────────────────────────────────

    def _score_item(
        self,
        item: Dict[str, Any],
        query_record: Dict[str, Any],
    ) -> int:
        """
        Score a single search result using weights from google-search-config.json.
        Returns -1 to disqualify results from skip_domains.
        """
        cfg       = self.config
        link      = item.get("link", "").lower()
        title_txt = item.get("title",   "").lower()
        snippet   = item.get("snippet", "").lower()
        combined  = f"{title_txt} {snippet}"

        org_lower = query_record.get("organization", "").lower()
        year_str  = str(query_record.get("year", ""))

        # Disqualify noise domains
        for domain in cfg.skip_domains:
            if domain.lower() in link:
                return -1

        # Disqualify results that match exclude_terms (discovery mode)
        if cfg.exclude_terms:
            for term in cfg.exclude_terms:
                if term.lower() in combined:
                    return -1

        # Disqualify financial reports masquerading as security reports
        if cfg.financial_terms:
            for term in cfg.financial_terms:
                if term.lower() in title_txt:
                    return -1

        score = 0
        if org_lower  and org_lower  in link:       score += cfg.score_org_in_link
        if year_str   and year_str   in link:       score += cfg.score_year_in_link
        if "report"                  in link:       score += cfg.score_report_in_link
        if year_str   and year_str   in title_txt:  score += cfg.score_year_in_title
        if org_lower  and org_lower  in title_txt:  score += cfg.score_org_in_title

        # Penalise bare homepage URLs (very short path → unlikely a report page)
        if cfg.score_short_path_penalty:
            parsed = urllib.parse.urlparse(item.get("link", ""))
            path   = parsed.path.strip("/")
            if len(path) < cfg.score_short_path_threshold:
                score += cfg.score_short_path_penalty  # value is negative

        return score

    # ── API call with retry ───────────────────────────────────────────────

    def _call_api(self, query: str, num: int) -> Optional[List[Dict[str, Any]]]:
        """
        Execute one API request with exponential-backoff retry.
        Returns the list of result items, or None on terminal failure.
        """
        params = {
            "key": self.api_key,
            "cx":  self.cse_id,
            "q":   query,
            "num": num,
        }

        delay = self.config.initial_delay

        for attempt in range(self.config.max_retries):
            try:
                resp = requests.get(
                    self.config.base_url,
                    params=params,
                    timeout=self.config.request_timeout,
                )

                if resp.status_code == 429:
                    # Rate limited — sleep and retry
                    wait = delay
                    print(f"  ! Rate limited (429) — waiting {wait:.0f}s...")
                    time.sleep(wait)
                    delay = min(delay * self.config.backoff_mult, self.config.max_delay)
                    continue

                if resp.status_code != 200:
                    print(f"  ! API error {resp.status_code}: {resp.text[:120]}")
                    return None

                data = resp.json()
                return data.get("items", [])

            except requests.RequestException as e:
                print(f"  ! Request failed (attempt {attempt + 1}): {str(e)[:100]}")
                if attempt < self.config.max_retries - 1:
                    time.sleep(delay)
                    delay = min(delay * self.config.backoff_mult, self.config.max_delay)

        return None

    # ── Public search API ─────────────────────────────────────────────────

    def search(self, query_record: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a single search for the given query_record dict.
        Returns a result dict conforming to the output schema documented
        at the top of this file.

        This method is the integration point for other scripts importing
        this module — call it directly rather than going through main().
        """
        query_id = query_record.get("id", "unknown")
        query    = self.build_query(query_record)

        base_result: Dict[str, Any] = {
            "id":      query_id,
            "status":  "error",
            "query":   query,
            "url":     "",
            "title":   "",
            "snippet": "",
            "score":   -1,
            "reason":  "",
        }

        if not self._available:
            base_result["status"] = "skipped"
            base_result["reason"] = "Google Search credentials not configured"
            return base_result

        print(f"  Searching: {query[:90]}...")
        items = self._call_api(query, self.config.num_results)

        if items is None:
            base_result["reason"] = "API call failed after retries"
            return base_result

        if not items:
            base_result["status"] = "no_results"
            base_result["reason"] = "Query returned no results"
            return base_result

        # Score all results and select the best non-disqualified one
        scored = [
            (self._score_item(item, query_record), item)
            for item in items
        ]
        scored.sort(key=lambda x: x[0], reverse=True)

        best_score, best_item = scored[0]

        if best_score < 0:
            base_result["status"] = "no_results"
            base_result["reason"] = "All results disqualified by domain/term filters"
            return base_result

        return {
            "id":      query_id,
            "status":  "success",
            "query":   query,
            "url":     best_item.get("link",    ""),
            "title":   best_item.get("title",   ""),
            "snippet": best_item.get("snippet", ""),
            "score":   best_score,
            "reason":  "",
        }

    def search_batch(
        self,
        query_records: List[Dict[str, Any]],
    ) -> List[Dict[str, Any]]:
        """
        Execute search() for each record, respecting the configured rate-limit
        sleep between requests.  Returns a list of result dicts in the same
        order as the input.
        """
        results = []
        for i, record in enumerate(query_records, 1):
            qid = record.get("id", f"query-{i}")
            print(f"[{i}/{len(query_records)}] {qid}")
            result = self.search(record)
            results.append(result)
            if i < len(query_records):
                time.sleep(self.config.rate_limit_sleep)
        return results


# ==========================
# MODULE-LEVEL HELPER
# ==========================
def search_one(
    organization: str,
    title: str,
    year: str,
    artifacts_dir: str = ".github/artifacts",
    mode: str = "report_url",
) -> Optional[str]:
    """
    Convenience function for other scripts that want to resolve a single
    report URL without constructing config/client objects themselves.

    Returns the best result URL string, or None if unavailable.

    Example usage in readme-updater.py:
        from google_search import search_one
        url = search_one(org, title, year, artifacts_dir=args.artifacts_dir)
    """
    try:
        config = ConfigLoader(artifacts_dir, mode=mode)
        client = GoogleSearchClient(config)
        if not client.is_available():
            return None
        record = {
            "id":           f"{organization}-{year}",
            "organization": organization,
            "title":        title,
            "year":         year,
        }
        result = client.search(record)
        if result["status"] == "success" and result["url"]:
            return result["url"]
    except Exception as e:
        print(f"  ⚠ search_one failed: {str(e)[:100]}")
    return None


# ==========================
# MAIN
# ==========================
def main() -> int:
    parser = argparse.ArgumentParser(
        description="Google Custom Search — batch query runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--queries-json",
        required=True,
        help="Path to JSON file containing an array of query objects",
    )
    parser.add_argument(
        "--output-json",
        default="search_results.json",
        help="Path to write the results JSON array (default: search_results.json)",
    )
    parser.add_argument(
        "--artifacts-dir",
        default=".github/artifacts",
        help="Directory containing google-search-config.json (default: .github/artifacts)",
    )
    parser.add_argument(
        "--mode",
        default="report_url",
        help=(
            "Search mode defined in google-search-config.json → google_search.modes "
            "(default: report_url)"
        ),
    )
    args = parser.parse_args()

    print(f"\n{'='*70}")
    print("Google Custom Search")
    print(f"{'='*70}\n")

    # ── Load config ───────────────────────────────────────────────────────
    try:
        config = ConfigLoader(args.artifacts_dir, mode=args.mode)
    except Exception as e:
        print(f"ERROR: Config failed: {e}")
        return 1

    print(f"✓ Config loaded")
    print(f"  Mode           : {args.mode}")
    print(f"  Query template : {config.query_template}")
    print(f"  Results per q  : {config.num_results}")
    print(f"  Skip domains   : {len(config.skip_domains)}")
    print()

    # ── Build client ──────────────────────────────────────────────────────
    client = GoogleSearchClient(config)
    print(
        f"  Google Search  : "
        f"{'available' if client.is_available() else 'unavailable — credentials missing'}"
    )
    print()

    # ── Load queries ──────────────────────────────────────────────────────
    queries_path = Path(args.queries_json)
    if not queries_path.exists():
        print(f"ERROR: Queries file not found: {args.queries_json}")
        return 1

    try:
        with open(queries_path, "r", encoding="utf-8") as f:
            queries = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in {args.queries_json}: {e}")
        return 1

    if not isinstance(queries, list) or not queries:
        print("⊘ No queries to process")
        with open(args.output_json, "w", encoding="utf-8") as f:
            json.dump([], f)
        return 0

    print(f"✓ {len(queries)} query/queries to execute\n")

    # ── Execute ───────────────────────────────────────────────────────────
    results = client.search_batch(queries)

    # ── Save results ──────────────────────────────────────────────────────
    with open(args.output_json, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    successful   = sum(1 for r in results if r["status"] == "success")
    no_results   = sum(1 for r in results if r["status"] == "no_results")
    skipped      = sum(1 for r in results if r["status"] == "skipped")
    errors       = sum(1 for r in results if r["status"] == "error")

    print(f"\n{'='*70}")
    print(f"✓ Success    : {successful}/{len(results)}")
    if no_results: print(f"⊘ No results : {no_results}/{len(results)}")
    if skipped:    print(f"⊘ Skipped    : {skipped}/{len(results)}")
    if errors:     print(f"✗ Errors     : {errors}/{len(results)}")
    print(f"✓ Results saved to: {args.output_json}")
    print(f"{'='*70}\n")

    return 0 if successful > 0 or skipped > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
