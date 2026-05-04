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
        self.score_toplevel_domain_penalty: int = scoring.get("toplevel_domain_penalty", 0)
        self.score_existing_domain_match_bonus: int = scoring.get("existing_domain_match_bonus", 0)
        self.score_existing_subdomain_match_bonus: int = scoring.get("existing_subdomain_match_bonus", 0)
        # Minimum score a result must reach to be accepted (0 = disabled)
        self.score_min_accept: int = scoring.get("min_accept_score", 0)

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
# URL UTILITIES
# ==========================
def _extract_registered_domain(url: str) -> str:
    """
    Return the registered domain (last two labels) from a URL, lowercased.
    Returns "" on parse failure.
    """
    try:
        host = urllib.parse.urlparse(url).netloc.lower().lstrip("www.")
        parts = host.split(".")
        return ".".join(parts[-2:]) if len(parts) >= 2 else host
    except Exception:
        return ""


def _extract_full_host(url: str) -> str:
    """
    Return the full host (netloc), lowercased, without www. prefix.
    """
    try:
        return urllib.parse.urlparse(url).netloc.lower().lstrip("www.")
    except Exception:
        return ""


def _is_toplevel_domain(url: str) -> bool:
    """
    Return True if the URL has an empty or trivially short path — i.e. it
    points to a site homepage rather than a specific report page.
    """
    try:
        path = urllib.parse.urlparse(url).path.strip("/")
        return len(path) < 3
    except Exception:
        return False


def _build_site_scoped_query(query_template: str, query_record: Dict[str, Any], domain: str) -> str:
    """
    Build a query using the template but prepend site:<domain> so Google
    restricts results to that domain only.
    """
    base = query_template
    base = base.replace("{organization}", query_record.get("organization", ""))
    base = base.replace("{title}",        query_record.get("title",        ""))
    base = base.replace("{year}",         str(query_record.get("year",     "")))
    base = base.replace("{query}",        query_record.get("query",        ""))
    return f"site:{domain} {base.strip()}"


# ==========================
# GOOGLE SEARCH CLIENT
# ==========================
class GoogleSearchClient:
    """
    Executes Google Custom Search API queries with retry logic and result scoring.

    Two-phase search strategy (report_url mode with existing_url):
      Phase 1 — site-scoped: restrict query to the known domain from existing_url.
                Finds the new year's report on the same subdomain/domain first.
                This prevents regression to bare homepages or wrong domains.
      Phase 2 — broad fallback: run unscoped query only if Phase 1 finds nothing
                above the minimum acceptance threshold.

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

    def build_query(self, query_record: Dict[str, Any], site_domain: str = "") -> str:
        """
        Substitute placeholders in the mode's query_template.
        If site_domain is provided, prepend site:<domain> to the query.
        """
        q = self.config.query_template
        q = q.replace("{organization}", query_record.get("organization", ""))
        q = q.replace("{title}",        query_record.get("title",        ""))
        q = q.replace("{year}",         str(query_record.get("year",     "")))
        q = q.replace("{query}",        query_record.get("query",        ""))
        q = q.strip()
        if site_domain:
            q = f"site:{site_domain} {q}"
        return q

    # ── Scoring ───────────────────────────────────────────────────────────

    def _score_item(
        self,
        item: Dict[str, Any],
        query_record: Dict[str, Any],
        existing_host: str = "",
        existing_reg_domain: str = "",
    ) -> int:
        """
        Score a single search result using weights from google-search-config.json.

        Key behaviours:
        - Returns -1 to hard-disqualify results (skip_domains, exclude_terms, etc.)
        - Applies a large bonus for exact host match with existing_url (same subdomain)
        - Applies a smaller bonus for registered-domain match (different subdomain)
        - Heavily penalises bare top-level domain URLs (no meaningful path)
        - Requires min_accept_score if configured — bare homepages that only earn
          the subdomain bonus but nothing else will fall below the threshold.
        """
        cfg       = self.config
        link      = item.get("link", "").lower()
        title_txt = item.get("title",   "").lower()
        snippet   = item.get("snippet", "").lower()
        combined  = f"{title_txt} {snippet}"

        org_lower = query_record.get("organization", "").lower()
        year_str  = str(query_record.get("year", ""))

        # ── Hard disqualifiers ────────────────────────────────────────────
        for domain in cfg.skip_domains:
            if domain.lower() in link:
                return -1

        if cfg.exclude_terms:
            for term in cfg.exclude_terms:
                if term.lower() in combined:
                    return -1

        if cfg.financial_terms:
            for term in cfg.financial_terms:
                if term.lower() in title_txt:
                    return -1

        # ── Positive signals ──────────────────────────────────────────────
        score = 0
        if org_lower  and org_lower  in link:       score += cfg.score_org_in_link
        if year_str   and year_str   in link:       score += cfg.score_year_in_link
        if "report"                  in link:       score += cfg.score_report_in_link
        if year_str   and year_str   in title_txt:  score += cfg.score_year_in_title
        if org_lower  and org_lower  in title_txt:  score += cfg.score_org_in_title

        # ── Path-based penalties ─────────────────────────────────────────
        parsed = urllib.parse.urlparse(item.get("link", ""))
        path   = parsed.path.strip("/")

        if cfg.score_short_path_penalty:
            if len(path) < cfg.score_short_path_threshold:
                score += cfg.score_short_path_penalty  # negative

        # Hard penalty: URL is bare homepage (empty path)
        if cfg.score_toplevel_domain_penalty and not path:
            score += cfg.score_toplevel_domain_penalty  # negative

        # ── Domain anchoring bonus ────────────────────────────────────────
        # Two-tier: exact subdomain match > registered-domain match.
        # This is the primary defence against domain regression.
        result_host       = parsed.netloc.lower().lstrip("www.")
        result_reg_domain = _extract_registered_domain(item.get("link", ""))

        if existing_host and cfg.score_existing_domain_match_bonus:
            if result_host == existing_host:
                # Exact host match including any subdomain
                score += cfg.score_existing_domain_match_bonus
            elif (existing_reg_domain and result_reg_domain == existing_reg_domain
                  and cfg.score_existing_subdomain_match_bonus):
                # Same registered domain, different subdomain
                score += cfg.score_existing_subdomain_match_bonus

        return score

    def _is_acceptable(self, score: int) -> bool:
        """True if score meets the minimum acceptance threshold (if configured)."""
        if self.config.score_min_accept > 0:
            return score >= self.config.score_min_accept
        return score >= 0

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

    # ── Best result picker ────────────────────────────────────────────────

    def _pick_best(
        self,
        items: List[Dict[str, Any]],
        query_record: Dict[str, Any],
        existing_host: str = "",
        existing_reg_domain: str = "",
    ) -> Tuple[int, Optional[Dict[str, Any]]]:
        """
        Score all items, return (best_score, best_item).
        Returns (-1, None) if all items are disqualified.
        """
        scored = [
            (self._score_item(item, query_record, existing_host, existing_reg_domain), item)
            for item in items
        ]
        scored.sort(key=lambda x: x[0], reverse=True)
        best_score, best_item = scored[0]
        return best_score, best_item if best_score >= 0 else None

    # ── Public search API ─────────────────────────────────────────────────

    def search(self, query_record: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a search for the given query_record dict.

        Two-phase strategy when existing_url is present:
          Phase 1 — site-scoped query restricted to the existing URL's exact
                    host. Strongly prefers results that stay on the known domain
                    and finds the new year's page. Accepted if score >= min_accept_score.
          Phase 2 — broad unscoped fallback, only when Phase 1 yields nothing
                    acceptable. Domain-anchoring bonuses still apply so on-domain
                    results are preferred over foreign ones.

        If no existing_url, a single broad query is executed (original behaviour).

        Optional key in query_record:
          "existing_url" — the current known URL for this entry from the README.
        """
        query_id     = query_record.get("id", "unknown")
        existing_url = query_record.get("existing_url", "")

        base_result: Dict[str, Any] = {
            "id":      query_id,
            "status":  "error",
            "query":   "",
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

        # Pre-compute domain components from existing URL for scoring reuse
        existing_host       = _extract_full_host(existing_url)       if existing_url else ""
        existing_reg_domain = _extract_registered_domain(existing_url) if existing_url else ""

        # ── Phase 1: site-scoped search (only when existing_url is available) ──
        if existing_host:
            site_query = self.build_query(query_record, site_domain=existing_host)
            base_result["query"] = site_query
            print(f"  Phase 1 (site-scoped): {site_query[:90]}...")

            items = self._call_api(site_query, self.config.num_results)
            if items:
                best_score, best_item = self._pick_best(
                    items, query_record, existing_host, existing_reg_domain
                )
                if best_item is not None and self._is_acceptable(best_score):
                    # Only accept a site-scoped result if it is NOT a bare homepage.
                    # A site: search for the homepage itself can return the homepage —
                    # we want a specific report page, not just "something on this domain."
                    result_url = best_item.get("link", "")
                    if not _is_toplevel_domain(result_url):
                        print(f"  ✓ Phase 1 hit (score={best_score}): {result_url}")
                        return {
                            "id":      query_id,
                            "status":  "success",
                            "query":   site_query,
                            "url":     result_url,
                            "title":   best_item.get("title",   ""),
                            "snippet": best_item.get("snippet", ""),
                            "score":   best_score,
                            "reason":  "site-scoped",
                        }
                    else:
                        print(f"  ⊘ Phase 1 result is bare homepage — falling through to Phase 2")
                else:
                    print(f"  ⊘ Phase 1: no acceptable result (best score={best_score}) — trying broad search")
            else:
                print(f"  ⊘ Phase 1: no results — trying broad search")

            # Rate limit pause between phase 1 and phase 2
            time.sleep(self.config.rate_limit_sleep)

        # ── Phase 2 (or sole query): broad unscoped search ────────────────
        broad_query = self.build_query(query_record)
        base_result["query"] = broad_query
        print(f"  {'Phase 2 (broad):' if existing_host else 'Searching:'} {broad_query[:90]}...")

        items = self._call_api(broad_query, self.config.num_results)

        if items is None:
            base_result["reason"] = "API call failed after retries"
            return base_result

        if not items:
            base_result["status"] = "no_results"
            base_result["reason"] = "Query returned no results"
            return base_result

        best_score, best_item = self._pick_best(
            items, query_record, existing_host, existing_reg_domain
        )

        if best_item is None:
            base_result["status"] = "no_results"
            base_result["reason"] = "All results disqualified by domain/term filters"
            return base_result

        result_url = best_item.get("link", "")

        # Final guard: if the best result is still a bare homepage and we have
        # an existing specific URL, keep the existing URL rather than regressing.
        if _is_toplevel_domain(result_url) and existing_url and not _is_toplevel_domain(existing_url):
            print(f"  ⊘ Broad search best result is bare homepage — keeping existing URL")
            base_result["status"] = "no_results"
            base_result["reason"] = "Best result was bare homepage; existing specific URL preferred"
            return base_result

        # Enforce minimum acceptance score for broad results too
        if not self._is_acceptable(best_score):
            print(f"  ⊘ Best broad result score {best_score} below min_accept_score "
                  f"{self.config.score_min_accept}")
            base_result["status"] = "no_results"
            base_result["reason"] = f"Best score {best_score} below acceptance threshold"
            return base_result

        return {
            "id":      query_id,
            "status":  "success",
            "query":   broad_query,
            "url":     result_url,
            "title":   best_item.get("title",   ""),
            "snippet": best_item.get("snippet", ""),
            "score":   best_score,
            "reason":  "broad",
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
    existing_url: str = "",
) -> Optional[str]:
    """
    Convenience function for other scripts that want to resolve a single
    report URL without constructing config/client objects themselves.

    Returns the best result URL string, or None if unavailable / below threshold.

    Pass ``existing_url`` (the current org_url from the README entry) to
    enable Phase 1 site-scoped search — this finds the new year's report on
    the same domain before falling back to a broad query.  Without it, only
    a broad query is run.

    Example usage in readme-updater.py:
        from google_search import search_one
        url = search_one(org, title, year, artifacts_dir=args.artifacts_dir,
                         existing_url=existing_org_url)
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
            "existing_url": existing_url,
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
    print(f"  Min accept     : {config.score_min_accept}")
    print()

    client = GoogleSearchClient(config)
    print(
        f"  Google Search  : "
        f"{'available' if client.is_available() else 'unavailable — credentials missing'}"
    )
    print()

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

    results = client.search_batch(queries)

    with open(args.output_json, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    successful   = sum(1 for r in results if r["status"] == "success")
    no_results   = sum(1 for r in results if r["status"] == "no_results")
    skipped      = sum(1 for r in results if r["status"] == "skipped")
    errors       = sum(1 for r in results if r["status"] == "error")

    print(f"\n{'='*70}")
    print(f"✓ Success    : {successful}/{len(results)}")
    if no_results: print(f"⊘ No results : {no_results}/{len(results)}")
    if skipped:    print(f"⊘ Skipped    : {skipped}/{len(results)}  (phase-1 site hits count as success)")
    if errors:     print(f"✗ Errors     : {errors}/{len(results)}")
    print(f"✓ Results saved to: {args.output_json}")
    print(f"{'='*70}\n")

    return 0 if successful > 0 or skipped > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
