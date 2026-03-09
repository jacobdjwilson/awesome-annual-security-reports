import os
import sys
import json
import re
import hashlib
import argparse
import time
from pathlib import Path
from datetime import datetime, date
from typing import Dict, Any, List, Optional, Tuple

try:
    import requests
except ImportError:
    print("ERROR: requests required.  pip install requests")
    sys.exit(1)


# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

class Config:
    """
    Loads all settings from .github/artifacts/.
    No values are hardcoded — everything is overridable via JSON.
    """

    PDF_ROOT = Path("Annual Security Reports")

    def __init__(self, artifacts_dir: str = ".github/artifacts"):
        self.artifacts_dir = Path(artifacts_dir)

        wf  = self._load("workflow-config.json")
        gsc = self._load("google-search-config.json")

        # ── Discovery limits ──────────────────────────────────────────────
        disc = wf.get("workflow", {}).get("discovery", {})
        self.max_issues:   int = disc.get("default_limit", 10)
        self.max_searches: int = disc.get("max_searches_per_run", 25)

        # ── Rotation periods by tier (days) ───────────────────────────────
        rot = disc.get("rotation_days", {})
        self.rotation_current: int = rot.get("current", 30)   # gap == 1 year
        self.rotation_stale:   int = rot.get("stale",   91)   # gap == 2 years
        self.rotation_old:     int = rot.get("old",     182)  # gap >= 3 years

        # ── Google Search ─────────────────────────────────────────────────
        gs = gsc.get("google_search", {})
        self.gs_base_url:    str       = gs.get("base_url", "https://www.googleapis.com/customsearch/v1")
        self.gs_env_api_key: str       = gs.get("env_api_key", "GOOGLE_SEARCH_API_KEY")
        self.gs_env_cse_id:  str       = gs.get("env_cse_id",  "GOOGLE_CSE_ID")
        self.gs_timeout:     int       = gs.get("request_timeout_seconds", 10)
        self.gs_rate_sleep:  float     = gs.get("rate_limit_sleep_seconds", 1.0)

        retry = gs.get("retry_policy", {})
        self.gs_max_retries:   int   = retry.get("max_attempts",          3)
        self.gs_initial_delay: float = retry.get("initial_delay_seconds", 2)
        self.gs_backoff_mult:  float = retry.get("backoff_multiplier",    2)
        self.gs_max_delay:     float = retry.get("max_delay_seconds",    15)

        mode = gs.get("modes", {}).get("report_discovery", {})
        self.gs_query_template: str       = mode.get("query_template",
            "{organization} {title} {year} annual security report filetype:pdf")
        self.gs_num_results:    int       = mode.get("num_results", 8)
        self.gs_skip_domains:   List[str] = mode.get("skip_domains", [])

        # ── Discovery heuristics ──────────────────────────────────────────
        h = gs.get("discovery_heuristics", {})
        self.score_threshold:      int             = h.get("score_threshold", 15)
        self.positive_signals:     Dict[str, int]  = h.get("positive_signals", {})
        self.negative_signals:     Dict[str, int]  = h.get("negative_signals", {})
        self.year_in_url_bonus:    int             = h.get("year_in_url_bonus",   20)
        self.year_in_title_bonus:  int             = h.get("year_in_title_bonus", 15)
        self.pdf_url_bonus:        int             = h.get("pdf_url_bonus",       10)
        self.url_reject_patterns:  List[str]       = h.get("url_reject_patterns", [])
        self.financial_title_terms:List[str]       = h.get("financial_title_terms", [])
        self.exclude_terms:        List[str]       = h.get("exclude_terms", [])
        self.pdf_path_patterns:    List[str]       = h.get("pdf_path_patterns", [".pdf"])

    def _load(self, filename: str) -> Dict[str, Any]:
        path = self.artifacts_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"Required config missing: {path}")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)


# ══════════════════════════════════════════════════════════════════════════════
# REPOSITORY LINEAGE INDEX
# ══════════════════════════════════════════════════════════════════════════════

class ReportLineageIndex:
    """
    Walks the PDF root directory and builds a year-indexed fingerprint map.

    Fingerprint: sha256 of "<org_lower>|<title_lower>" so it's stable even
    if the filename uses different capitalization or separators over the years.

    Answers: "Which years of series X are already in the repo?"
    """

    YEAR_RE = re.compile(r"-(\d{4})\.pdf$", re.IGNORECASE)

    def __init__(self, pdf_root: Path):
        self.pdf_root = pdf_root
        # fp -> set of years present
        self.index: Dict[str, set] = {}
        self._build()

    def _build(self):
        if not self.pdf_root.exists():
            print(f"WARNING: PDF root not found: {self.pdf_root}")
            return
        for pdf in self.pdf_root.rglob("*.pdf"):
            m = self.YEAR_RE.search(pdf.name)
            if not m:
                continue
            year = int(m.group(1))
            stem = pdf.name[: m.start()]
            fp   = self._fp(stem)
            self.index.setdefault(fp, set()).add(year)

        total = sum(len(v) for v in self.index.values())
        print(f"Lineage index: {total} PDF(s) across {len(self.index)} series")

    @staticmethod
    def _fp(stem: str) -> str:
        parts = stem.split("-", 1)
        org   = parts[0].lower().strip()
        title = parts[1].lower().strip() if len(parts) > 1 else ""
        title = re.sub(r"[-_ ]+", "-", title).strip("-")
        return f"{org}|{title}"

    def years_present(self, stem: str) -> set:
        return self.index.get(self._fp(stem), set())

    def has_year(self, stem: str, year: int) -> bool:
        return year in self.years_present(stem)


# ══════════════════════════════════════════════════════════════════════════════
# SLOT SCHEDULER  (the no-database rotation)
# ══════════════════════════════════════════════════════════════════════════════

class SlotScheduler:
    """
    Assigns each series to a deterministic daily search slot without any
    persistent state.

    Algorithm
    ---------
    1.  Compute a stable integer hash of the series stem:
            slot_id = int(sha256(stem.lower())[:8], 16)

    2.  Each priority tier has a rotation_period (days).  A series is
        scheduled for today when:
            slot_id % rotation_period  ==  epoch_day % rotation_period

        where epoch_day = date.toordinal() (a monotonically increasing int
        that advances by 1 each calendar day, independent of year).

    Properties
    ----------
    - Deterministic: same stem always lands on the same calendar days.
    - Even distribution: sha256 output is uniform, so series spread
      naturally across the rotation window.
    - No storage: re-computed fresh on every run.
    - Stable across year boundaries: ordinal day doesn't reset on Jan 1.
    - Predictable: operators can calculate any series' next run date offline.

    Example
    -------
    Stem "Microsoft-Digital-Defense-Report" with rotation_period=30:
        slot_id = 0x3fa7... → some integer, mod 30 = e.g. 17
        If today's ordinal mod 30 == 17 → searched today.
        Next search: 30 days later. No log entry needed.
    """

    def __init__(self, today: date):
        self.epoch_day = today.toordinal()

    def is_due(self, stem: str, rotation_period: int) -> bool:
        slot_id = int(hashlib.sha256(stem.lower().encode()).hexdigest()[:8], 16)
        return (slot_id % rotation_period) == (self.epoch_day % rotation_period)

    def days_until_next(self, stem: str, rotation_period: int) -> int:
        """How many days until this series is next scheduled (for logging)."""
        slot_id   = int(hashlib.sha256(stem.lower().encode()).hexdigest()[:8], 16)
        slot_pos  = slot_id % rotation_period
        today_pos = self.epoch_day % rotation_period
        delta     = (slot_pos - today_pos) % rotation_period
        return delta if delta > 0 else rotation_period


# ══════════════════════════════════════════════════════════════════════════════
# REPORT SCANNER
# ══════════════════════════════════════════════════════════════════════════════

TIER_CURRENT = "CURRENT"   # gap 1 year   — highest search frequency
TIER_STALE   = "STALE"     # gap 2 years
TIER_OLD     = "OLD"       # gap 3+ years — lowest search frequency

class ReportScanner:
    """
    Scans the repository file tree and produces a prioritised list of
    search tasks for today based on the slot scheduler.

    For each series that is due today:
    - Determines which target years are missing from the repo (up to current year).
    - Emits one search task per missing year so each gap is checked independently.

    Example: repo has Acme-2023, current year 2026, series is due today.
    → Tasks: search for Acme-2024, Acme-2025, Acme-2026 (three tasks).
    """

    def __init__(self, config: Config, lineage: ReportLineageIndex, scheduler: SlotScheduler):
        self.config       = config
        self.lineage      = lineage
        self.scheduler    = scheduler
        self.current_year = datetime.now().year

    def get_todays_tasks(self) -> List[Dict[str, Any]]:
        """
        Return search tasks scheduled for today, sorted by priority tier.
        Each task represents one (series, target_year) pair.
        """
        if not self.config.PDF_ROOT.exists():
            print(f"ERROR: PDF root not found: {self.config.PDF_ROOT}")
            return []

        print(f"Scanning {self.config.PDF_ROOT}...")

        # Collect the most-recent year per series from the file tree
        series_latest: Dict[str, Dict[str, Any]] = {}
        for pdf in self.config.PDF_ROOT.rglob("*.pdf"):
            r = self._parse(pdf)
            if not r:
                continue
            key = r["stem"]
            if key not in series_latest or r["year"] > series_latest[key]["year"]:
                series_latest[key] = r

        print(f"  {len(series_latest)} unique series in repo")

        tasks: List[Dict[str, Any]] = []
        skipped_uptodate = 0
        skipped_schedule = 0

        for stem, report in series_latest.items():
            latest_year = report["year"]

            # Find all years that are missing between latest+1 and current_year
            missing_years = [
                y for y in range(latest_year + 1, self.current_year + 1)
                if not self.lineage.has_year(stem, y)
            ]

            if not missing_years:
                skipped_uptodate += 1
                continue

            # Assign priority tier based on how stale the newest repo copy is
            gap = self.current_year - latest_year
            if gap == 1:
                tier, rotation = TIER_CURRENT, self.config.rotation_current
            elif gap == 2:
                tier, rotation = TIER_STALE,   self.config.rotation_stale
            else:
                tier, rotation = TIER_OLD,     self.config.rotation_old

            # Check if this series is scheduled for today
            if not self.scheduler.is_due(stem, rotation):
                skipped_schedule += 1
                continue

            # Emit one task per missing year (newest first — most likely to exist)
            for target_year in sorted(missing_years, reverse=True):
                tasks.append({
                    "org":         report["org"],
                    "title":       report["title"].replace("-", " "),
                    "stem":        stem,
                    "latest_year": latest_year,
                    "target_year": target_year,
                    "tier":        tier,
                    "gap":         gap,
                })

        # Sort: CURRENT first, then STALE, then OLD; newest target year within tier
        tier_order = {TIER_CURRENT: 0, TIER_STALE: 1, TIER_OLD: 2}
        tasks.sort(key=lambda t: (tier_order[t["tier"]], -t["target_year"]))

        print(f"  {skipped_uptodate} series already up-to-date in repo")
        print(f"  {skipped_schedule} series not scheduled for today")
        print(f"  {len(tasks)} search task(s) due today across "
              f"{len({t['stem'] for t in tasks})} series")

        return tasks


    def _parse(self, pdf_path: Path) -> Optional[Dict[str, Any]]:
        m = re.search(r"-(\d{4})\.pdf$", pdf_path.name)
        if not m:
            return None
        year  = int(m.group(1))
        stem  = pdf_path.name[: m.start()]
        parts = stem.split("-", 1)
        return {
            "org":   parts[0],
            "title": parts[1] if len(parts) >= 2 else "Security Report",
            "year":  year,
            "stem":  stem,
        }


# ══════════════════════════════════════════════════════════════════════════════
# HEURISTIC VALIDATOR
# ══════════════════════════════════════════════════════════════════════════════

class HeuristicValidator:
    """
    Scores a search result candidate using the signal tables in
    google-search-config.json → discovery_heuristics.

    Scoring pipeline:
      1. URL pattern reject (instant -999 for /webinar/, /blog/, etc.)
      2. Financial title filter (instant -999)
      3. Exclude term filter (instant -999)
      4. Positive keyword signals (+weight)
      5. Negative keyword signals (+weight, weights are negative)
      6. Structural bonuses: year in URL, year in title, PDF path

    Returns (score, description_string).
    """

    def __init__(self, config: Config):
        self.config = config

    def score(self, url: str, title: str, snippet: str, year: int) -> Tuple[int, str]:
        url_l    = url.lower()
        title_l  = title.lower()
        snip_l   = snippet.lower()
        combined = f"{url_l} {title_l} {snip_l}"
        year_str = str(year)

        # ── Structural rejects ────────────────────────────────────────────
        for pat in self.config.url_reject_patterns:
            if pat.lower() in url_l:
                return -999, f"url pattern '{pat}'"

        for term in self.config.financial_title_terms:
            if term.lower() in title_l:
                return -999, f"financial title term '{term}'"

        for term in self.config.exclude_terms:
            if term.lower() in combined:
                return -999, f"exclude term '{term}'"

        total = 0

        # ── Positive signals ──────────────────────────────────────────────
        for signal, w in self.config.positive_signals.items():
            if signal.lower() in combined:
                total += w

        # ── Negative signals ──────────────────────────────────────────────
        for signal, w in self.config.negative_signals.items():
            if signal.lower() in combined:
                total += w   # w is already negative

        # ── Structural bonuses ────────────────────────────────────────────
        if year_str in url_l:
            total += self.config.year_in_url_bonus

        if year_str in title_l:
            total += self.config.year_in_title_bonus

        for pat in self.config.pdf_path_patterns:
            if pat.lower() in url_l:
                total += self.config.pdf_url_bonus
                break

        return total, ""


# ══════════════════════════════════════════════════════════════════════════════
# GOOGLE SEARCHER
# ══════════════════════════════════════════════════════════════════════════════

class GoogleSearcher:
    """
    Issues a single Google Custom Search query and returns raw result items.
    All HTTP settings (timeout, retry, rate-limit) come from Config.
    """

    def __init__(self, config: Config):
        self.config  = config
        self.api_key = os.environ.get(config.gs_env_api_key, "")
        self.cse_id  = os.environ.get(config.gs_env_cse_id,  "")
        if not self.api_key or not self.cse_id:
            raise RuntimeError(
                f"Missing credentials: set {config.gs_env_api_key} "
                f"and {config.gs_env_cse_id}"
            )

    def search(self, task: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Search for one (org, title, target_year) task. Returns raw items."""
        q = (self.config.gs_query_template
             .replace("{organization}", task["org"])
             .replace("{title}",        task["title"])
             .replace("{year}",         str(task["target_year"])))
        print(f"  Query: {q[:100]}")

        delay = self.config.gs_initial_delay
        for attempt in range(1, self.config.gs_max_retries + 1):
            try:
                resp = requests.get(
                    self.config.gs_base_url,
                    params={"key": self.api_key, "cx": self.cse_id,
                            "q": q, "num": self.config.gs_num_results},
                    timeout=self.config.gs_timeout,
                )
                if resp.status_code == 200:
                    return [
                        {"url": i.get("link",""), "title": i.get("title",""),
                         "snippet": i.get("snippet","")}
                        for i in resp.json().get("items", [])
                        if i.get("link")
                    ]
                if resp.status_code == 429:
                    print(f"  ⚠ Rate limited — waiting {delay:.0f}s")
                    time.sleep(delay)
                    delay = min(delay * self.config.gs_backoff_mult, self.config.gs_max_delay)
                else:
                    print(f"  ! HTTP {resp.status_code}")
                    return []
            except Exception as e:
                print(f"  ! Exception: {str(e)[:80]}")
                if attempt < self.config.gs_max_retries:
                    time.sleep(delay)
                    delay = min(delay * self.config.gs_backoff_mult, self.config.gs_max_delay)
        return []


# ══════════════════════════════════════════════════════════════════════════════
# GITHUB ISSUE CREATOR
# ══════════════════════════════════════════════════════════════════════════════

class IssueCreator:
    """
    Creates GitHub issues for confirmed discovery candidates and checks for
    existing open issues to prevent duplicates.
    """

    API = "https://api.github.com"

    def __init__(self, token: str, repo: str):
        self.headers = {
            "Authorization": f"token {token}",
            "Accept":        "application/vnd.github.v3+json",
        }
        self.repo = repo
        # Cache open issues fetched once per run
        self._open_titles: Optional[List[str]] = None

    def _fetch_open_titles(self) -> List[str]:
        if self._open_titles is not None:
            return self._open_titles
        try:
            resp = requests.get(
                f"{self.API}/repos/{self.repo}/issues",
                headers=self.headers,
                params={"state": "open", "labels": "report-suggestion", "per_page": 100},
                timeout=15,
            )
            if resp.status_code == 200:
                self._open_titles = [i.get("title","").lower() for i in resp.json()]
                return self._open_titles
        except Exception as e:
            print(f"  ! Could not fetch open issues: {e}")
        self._open_titles = []
        return self._open_titles

    def issue_exists(self, org: str, year: int) -> bool:
        fragment = f"{org} {year}".lower()
        exists = any(fragment in t for t in self._fetch_open_titles())
        if exists:
            print(f"  ⊘ Issue already open for {org} {year}")
        return exists

    def create(self, candidate: Dict[str, Any]) -> bool:
        org  = candidate["org"]
        year = candidate["target_year"]

        if self.issue_exists(org, year):
            return False

        tier_label = {
            TIER_CURRENT: "🔴 Current year",
            TIER_STALE:   "🟡 One year stale",
            TIER_OLD:     "🔵 Older gap",
        }.get(candidate["tier"], candidate["tier"])

        title = f"[Report Discovery] {org} {year} — {candidate['title']}"
        body  = (
            f"## 📄 New Security Report Discovered\n\n"
            f"| Field | Value |\n"
            f"|-------|-------|\n"
            f"| **Organization** | {org} |\n"
            f"| **Year** | {year} |\n"
            f"| **Report** | {candidate['title']} |\n"
            f"| **URL** | {candidate['url']} |\n"
            f"| **Heuristic Score** | {candidate['score']} (threshold: {candidate['threshold']}) |\n"
            f"| **Priority** | {tier_label} (repo latest: {candidate['latest_year']}) |\n\n"
            f"**Snippet:**\n> {candidate['snippet'][:400]}\n\n"
            f"---\n"
            f"*Auto-discovered by the Security Report Discovery workflow.*\n"
            f"*Verify the URL resolves to a valid PDF before merging.*"
        )

        try:
            resp = requests.post(
                f"{self.API}/repos/{self.repo}/issues",
                headers=self.headers,
                json={"title": title, "body": body,
                      "labels": ["report-suggestion", "automated"]},
                timeout=15,
            )
            if resp.status_code == 201:
                html_url = resp.json().get("html_url", "")
                print(f"  ✓ Created issue: {title}")
                print(f"    {html_url}")
                # Add to local cache so same-run dedup works
                self._open_titles.append(title.lower())
                return True
            else:
                print(f"  ! Failed to create issue: HTTP {resp.status_code}")
                return False
        except Exception as e:
            print(f"  ! Error creating issue: {str(e)[:80]}")
            return False


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main() -> int:
    ap = argparse.ArgumentParser(description="Security Report Discovery")
    ap.add_argument("--artifacts-dir",   default=".github/artifacts")
    ap.add_argument("--max-discoveries", type=int, default=None,
                    help="Override max issues to create (default: from workflow-config.json)")
    ap.add_argument("--date", default=None,
                    help="Override today's date for testing (YYYY-MM-DD)")
    args = ap.parse_args()

    today = date.fromisoformat(args.date) if args.date else date.today()

    print(f"\n{'='*70}")
    print(f"Security Report Discovery  —  {today.isoformat()}")
    print(f"{'='*70}\n")

    # ── Config ────────────────────────────────────────────────────────────
    try:
        config = Config(args.artifacts_dir)
    except Exception as e:
        print(f"ERROR loading config: {e}")
        return 1

    max_issues = args.max_discoveries if args.max_discoveries is not None else config.max_issues

    print(f"✓ Config loaded")
    print(f"  Max issues/run    : {max_issues}")
    print(f"  Max searches/run  : {config.max_searches}")
    print(f"  Score threshold   : {config.score_threshold}")
    print(f"  Rotation (current): {config.rotation_current} days")
    print(f"  Rotation (stale)  : {config.rotation_stale} days")
    print(f"  Rotation (old)    : {config.rotation_old} days")
    print()

    # ── Credentials ───────────────────────────────────────────────────────
    gh_token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN", "")
    repo     = os.environ.get("GITHUB_REPOSITORY", "")
    if not gh_token or not repo:
        print("ERROR: GH_TOKEN / GITHUB_REPOSITORY required")
        return 1

    # ── Build lineage index ───────────────────────────────────────────────
    print(f"{'='*70}")
    print("Building lineage index...")
    print(f"{'='*70}\n")
    lineage   = ReportLineageIndex(config.PDF_ROOT)
    scheduler = SlotScheduler(today)
    scanner   = ReportScanner(config, lineage, scheduler)

    # ── Get today's search tasks ──────────────────────────────────────────
    print()
    tasks = scanner.get_todays_tasks()

    if not tasks:
        print("\n⊘ No searches scheduled for today — all series either")
        print("  up-to-date or not in their rotation slot.")
        return 0

    # Cap total searches to avoid excessive API usage
    tasks_to_run = tasks[: config.max_searches]
    if len(tasks) > config.max_searches:
        print(f"\n⚠ {len(tasks)} tasks due today — capping at {config.max_searches}")

    print(f"\n{'='*70}")
    print(f"Running {len(tasks_to_run)} search(es)  [issue limit: {max_issues}]")
    print(f"{'='*70}\n")

    # ── Search + score + create issues ───────────────────────────────────
    try:
        searcher = GoogleSearcher(config)
    except RuntimeError as e:
        print(f"ERROR: {e}")
        return 1

    validator = HeuristicValidator(config)
    creator   = IssueCreator(gh_token, repo)

    stats = {
        "searched":        0,
        "skip_domains":    0,
        "skip_score":      0,
        "candidates":      0,
        "issues_created":  0,
        "issues_skipped":  0,
    }
    tier_counts = {TIER_CURRENT: 0, TIER_STALE: 0, TIER_OLD: 0}

    for i, task in enumerate(tasks_to_run, 1):
        if stats["issues_created"] >= max_issues:
            print(f"\n⊘ Issue limit ({max_issues}) reached — stopping early")
            break

        org  = task["org"]
        year = task["target_year"]
        tier = task["tier"]

        print(f"[{i}/{len(tasks_to_run)}] {org} → {year}  [{tier}]")
        raw_results = searcher.search(task)
        stats["searched"] += 1
        tier_counts[tier] += 1

        # Score all results, pick the best above threshold
        best: Optional[Dict[str, Any]] = None
        best_score = -9999

        for item in raw_results:
            url     = item["url"]
            title   = item["title"]
            snippet = item["snippet"]

            # Skip noise domains
            if any(d.lower() in url.lower() for d in config.gs_skip_domains):
                stats["skip_domains"] += 1
                continue

            score, reject_reason = validator.score(url, title, snippet, year)

            if score == -999:
                print(f"  — rejected ({reject_reason}): {url[:60]}")
                continue

            if score > best_score:
                best_score = score
                best = {
                    "org":         org,
                    "title":       task["title"],
                    "url":         url,
                    "snippet":     snippet,
                    "target_year": year,
                    "latest_year": task["latest_year"],
                    "score":       score,
                    "threshold":   config.score_threshold,
                    "tier":        tier,
                }

        if best is None:
            print(f"  ⊘ No results after filtering")
        elif best_score < config.score_threshold:
            print(f"  ⊘ Best score {best_score} < threshold {config.score_threshold} — suppressed")
            print(f"    {best['url'][:70]}")
            stats["skip_score"] += 1
        else:
            print(f"  ✓ Candidate (score {best_score}): {best['url'][:70]}")
            stats["candidates"] += 1
            if creator.create(best):
                stats["issues_created"] += 1
            else:
                stats["issues_skipped"] += 1

        time.sleep(config.gs_rate_sleep)

    # ── Summary ───────────────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print("Discovery Summary")
    print(f"{'='*70}")
    print(f"  Searches run        : {stats['searched']}")
    print(f"    CURRENT tier      : {tier_counts[TIER_CURRENT]}")
    print(f"    STALE tier        : {tier_counts[TIER_STALE]}")
    print(f"    OLD tier          : {tier_counts[TIER_OLD]}")
    print(f"  Candidates found    : {stats['candidates']}")
    print(f"  Suppressed (score)  : {stats['skip_score']}")
    print(f"  Issues created      : {stats['issues_created']}")
    print(f"  Issues skipped(dup) : {stats['issues_skipped']}")
    print(f"{'='*70}")

    # Structured lines for workflow step summary to parse
    print(f"DISCOVERY_SEARCHED={stats['searched']}")
    print(f"DISCOVERY_CANDIDATES={stats['candidates']}")
    print(f"DISCOVERY_CREATED={stats['issues_created']}")
    print(f"DISCOVERY_SUPPRESSED={stats['skip_score']}")
    print(f"DISCOVERY_SKIPPED={stats['issues_skipped']}")
    print(f"DISCOVERY_TIER_CURRENT={tier_counts[TIER_CURRENT]}")
    print(f"DISCOVERY_TIER_STALE={tier_counts[TIER_STALE]}")
    print(f"DISCOVERY_TIER_OLD={tier_counts[TIER_OLD]}")

    return 0


if __name__ == "__main__":
    sys.exit(main())