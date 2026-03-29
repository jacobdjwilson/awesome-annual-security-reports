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
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    print("ERROR: requests required.  pip install requests")
    sys.exit(1)

import hashlib
import urllib.request


# ══════════════════════════════════════════════════════════════════════════════
# FIND TYPE CONSTANTS
# ══════════════════════════════════════════════════════════════════════════════

FIND_PDF     = "PDF"      # direct PDF download link
FIND_LANDING = "LANDING"  # gated landing / download page
FIND_UNKNOWN = "UNKNOWN"  # could not classify


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
        self.max_tasks:    int = disc.get("max_searches_per_run", 12)

        # ── Rotation periods by tier (days) ───────────────────────────────
        rot = disc.get("rotation_days", {})
        self.rotation_current: int = rot.get("current", 30)
        self.rotation_stale:   int = rot.get("stale",   91)
        self.rotation_old:     int = rot.get("old",     182)

        # ── Google Search ─────────────────────────────────────────────────
        gs = gsc.get("google_search", {})
        self.gs_base_url:    str   = gs.get("base_url", "https://www.googleapis.com/customsearch/v1")
        self.gs_env_api_key: str   = gs.get("env_api_key", "GOOGLE_SEARCH_API_KEY")
        self.gs_env_cse_id:  str   = gs.get("env_cse_id",  "GOOGLE_CSE_ID")
        self.gs_timeout:     int   = gs.get("request_timeout_seconds", 10)
        self.gs_rate_sleep:  float = gs.get("rate_limit_sleep_seconds", 1.0)

        retry = gs.get("retry_policy", {})
        self.gs_max_retries:   int   = retry.get("max_attempts",          3)
        self.gs_initial_delay: float = retry.get("initial_delay_seconds", 2)
        self.gs_backoff_mult:  float = retry.get("backoff_multiplier",    2)
        self.gs_max_delay:     float = retry.get("max_delay_seconds",    15)

        modes = gs.get("modes", {})
        pdf_mode     = modes.get("report_discovery_pdf",     {})
        landing_mode = modes.get("report_discovery_landing", {})

        self.gs_pdf_query:     str       = pdf_mode.get("query_template",
            "{organization} {title} {year} annual security report filetype:pdf")
        self.gs_landing_query: str       = landing_mode.get("query_template",
            "{organization} {title} {year} annual security report download")
        self.gs_num_results:   int       = pdf_mode.get("num_results", 8)
        self.gs_skip_domains:  List[str] = pdf_mode.get("skip_domains", [])

        # ── Find-type classification ──────────────────────────────────────
        ftc = gs.get("find_type_classification", {})
        self.pdf_indicators:      List[str] = ftc.get("pdf_indicators",      [".pdf"])
        self.landing_indicators:  List[str] = ftc.get("landing_page_indicators", [])
        self.gated_signals:       List[str] = ftc.get("gated_page_signals",  [])
        self.gated_bonus:         int       = ftc.get("gated_bonus", 12)

        # ── Discovery heuristics ──────────────────────────────────────────
        h = gs.get("discovery_heuristics", {})
        self.score_threshold:          int            = h.get("score_threshold", 15)
        self.positive_signals:         Dict[str, int] = h.get("positive_signals", {})
        self.negative_signals:         Dict[str, int] = h.get("negative_signals", {})
        self.year_in_url_bonus:        int            = h.get("year_in_url_bonus",   20)
        self.year_in_title_bonus:      int            = h.get("year_in_title_bonus", 15)
        self.pdf_url_bonus:            int            = h.get("pdf_url_bonus",       10)
        self.url_reject_patterns:      List[str]      = h.get("url_reject_patterns", [])
        self.financial_title_terms:    List[str]      = h.get("financial_title_terms", [])
        self.exclude_terms:            List[str]      = h.get("exclude_terms", [])
        self.pdf_path_patterns:        List[str]      = h.get("pdf_path_patterns", [".pdf"])

        # ── Domain-anchoring scoring ──────────────────────────────────────
        self.org_domain_match_bonus:   int = h.get("org_domain_match_bonus",   25)
        self.org_domain_mismatch_pdf_penalty: int = h.get("org_domain_mismatch_pdf_penalty", -20)
        self.wrong_year_in_url_penalty: int = h.get("wrong_year_in_url_penalty", -30)
        self.self_reference_domains:   List[str] = h.get("self_reference_domains", [
            "github.com/jacobdjwilson",
            "raw.githubusercontent.com/jacobdjwilson",
        ])

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
    Walks the PDF root and builds a year-indexed fingerprint map.
    Answers: "Which years of series X are already in the repo?"
    """

    YEAR_RE = re.compile(r"-(\d{4})\.pdf$", re.IGNORECASE)

    def __init__(self, pdf_root: Path):
        self.pdf_root = pdf_root
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
            self.index.setdefault(self._fp(stem), set()).add(year)

        total = sum(len(v) for v in self.index.values())
        print(f"Lineage index: {total} PDF(s) across {len(self.index)} series")

    @staticmethod
    def _fp(stem: str) -> str:
        parts = stem.split("-", 1)
        org   = parts[0].lower().strip()
        title = parts[1].lower().strip() if len(parts) > 1 else ""
        title = re.sub(r"[-_ ]+", "-", title).strip("-")
        return f"{org}|{title}"

    def has_year(self, stem: str, year: int) -> bool:
        return year in self.index.get(self._fp(stem), set())


# ══════════════════════════════════════════════════════════════════════════════
# ORG DOMAIN INDEX  (new)
# ══════════════════════════════════════════════════════════════════════════════

class OrgDomainIndex:
    """
    Parses README.md to extract the known org_url for each report series,
    then maps the PDF filename stem → registered domain (e.g. "crowdstrike.com").

    README format expected:
        | [CrowdStrike](https://crowdstrike.com) | ... | CrowdStrike-Global-Threat-Report-2024.pdf | ...

    Falls back gracefully if README is absent or the pattern is unrecognised.
    """

    # Matches a markdown link in a table cell: [text](url)
    _MD_LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)")

    def __init__(self, readme_path: Path = Path("README.md")):
        self.stem_to_domain: Dict[str, str] = {}
        self._parse(readme_path)

    def _parse(self, readme_path: Path):
        if not readme_path.exists():
            print("WARNING: README.md not found — org domain anchoring disabled")
            return

        text = readme_path.read_text(encoding="utf-8", errors="replace")

        # Each table row that contains a .pdf filename also has a markdown
        # org link somewhere on the same line.  We extract both.
        for line in text.splitlines():
            pdf_match = re.search(r"([\w\-]+)-(\d{4})\.pdf", line, re.IGNORECASE)
            if not pdf_match:
                continue
            stem = pdf_match.group(1)          # e.g. "CrowdStrike-Global-Threat-Report"
            # Find the first http(s) link in this line
            link_match = self._MD_LINK_RE.search(line)
            if not link_match:
                continue
            url = link_match.group(2)
            domain = self._extract_domain(url)
            if domain:
                # Store lower-case stem → domain; keep the first (most specific) match
                key = stem.lower()
                if key not in self.stem_to_domain:
                    self.stem_to_domain[key] = domain

        print(f"Org domain index: {len(self.stem_to_domain)} series with known domains")

    @staticmethod
    def _extract_domain(url: str) -> str:
        """Return the registered domain (e.g. 'crowdstrike.com') from a URL."""
        try:
            host = urlparse(url).netloc.lower()
            # Strip www. prefix
            if host.startswith("www."):
                host = host[4:]
            # Return only the last two labels (handles sub-domains)
            parts = host.split(".")
            if len(parts) >= 2:
                return ".".join(parts[-2:])
            return host
        except Exception:
            return ""

    def get_domain(self, stem: str) -> Optional[str]:
        """Return the registered domain for a PDF stem, or None if unknown."""
        return self.stem_to_domain.get(stem.lower())


# ══════════════════════════════════════════════════════════════════════════════
# SLOT SCHEDULER
# ══════════════════════════════════════════════════════════════════════════════

class SlotScheduler:
    """
    Assigns each series a deterministic daily search slot with no state file.

      slot      = sha256(stem) % rotation_period
      today_idx = date.toordinal() % rotation_period
      search if: slot == today_idx

    toordinal() is a monotonically increasing integer that never resets on
    Jan 1, so the distribution is stable across year boundaries.
    """

    def __init__(self, today: date):
        self.epoch_day = today.toordinal()

    def is_due(self, stem: str, rotation_period: int) -> bool:
        slot = int(hashlib.sha256(stem.lower().encode()).hexdigest()[:8], 16)
        return (slot % rotation_period) == (self.epoch_day % rotation_period)


# ══════════════════════════════════════════════════════════════════════════════
# REPORT SCANNER
# ══════════════════════════════════════════════════════════════════════════════

TIER_CURRENT = "CURRENT"
TIER_STALE   = "STALE"
TIER_OLD     = "OLD"

class ReportScanner:
    """
    Scans the file tree and emits (series, target_year) search tasks for
    series that are (a) missing a newer edition and (b) due today per the
    slot scheduler.  Emits one task per missing year, newest first.
    """

    def __init__(self, config: Config, lineage: ReportLineageIndex,
                 scheduler: SlotScheduler):
        self.config       = config
        self.lineage      = lineage
        self.scheduler    = scheduler
        self.current_year = datetime.now().year

    def get_todays_tasks(self) -> List[Dict[str, Any]]:
        if not self.config.PDF_ROOT.exists():
            print(f"ERROR: PDF root not found: {self.config.PDF_ROOT}")
            return []

        print(f"Scanning {self.config.PDF_ROOT}...")
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
            latest_year  = report["year"]
            missing_years = [
                y for y in range(latest_year + 1, self.current_year + 1)
                if not self.lineage.has_year(stem, y)
            ]
            if not missing_years:
                skipped_uptodate += 1
                continue

            gap = self.current_year - latest_year
            if gap == 1:
                tier, rotation = TIER_CURRENT, self.config.rotation_current
            elif gap == 2:
                tier, rotation = TIER_STALE,   self.config.rotation_stale
            else:
                tier, rotation = TIER_OLD,     self.config.rotation_old

            if not self.scheduler.is_due(stem, rotation):
                skipped_schedule += 1
                continue

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
# RESULT CLASSIFIER
# ══════════════════════════════════════════════════════════════════════════════

class ResultClassifier:
    """
    Determines the find type for a search result URL + snippet.

    Evaluation order:
      1. Any pdf_indicator in URL               → FIND_PDF
      2. Any landing_page_indicator in URL      → FIND_LANDING
      3. Any gated_page_signal in snippet       → FIND_LANDING (snippet confirms gating)
      4. Otherwise                              → FIND_UNKNOWN

    All pattern lists come from google-search-config.json →
    find_type_classification, so no strings are hardcoded here.
    """

    def __init__(self, config: Config):
        self.config = config

    def classify(self, url: str, snippet: str) -> str:
        url_l  = url.lower()
        snip_l = snippet.lower()

        for indicator in self.config.pdf_indicators:
            if indicator.lower() in url_l:
                return FIND_PDF

        for indicator in self.config.landing_indicators:
            if indicator.lower() in url_l:
                return FIND_LANDING

        for signal in self.config.gated_signals:
            if signal.lower() in snip_l:
                return FIND_LANDING

        return FIND_UNKNOWN

    def gated_bonus(self, snippet: str) -> int:
        """Return the gated-page score bonus if snippet contains gating language."""
        snip_l = snippet.lower()
        for signal in self.config.gated_signals:
            if signal.lower() in snip_l:
                return self.config.gated_bonus
        return 0


# ══════════════════════════════════════════════════════════════════════════════
# HEURISTIC VALIDATOR  (enhanced)
# ══════════════════════════════════════════════════════════════════════════════

class HeuristicValidator:
    """
    Scores a result using keyword signals + structural bonuses.

    Enhancements over baseline:
      - Org domain match bonus: +org_domain_match_bonus when result URL is on
        the org's registered domain (parsed from README org_url column).
      - PDF domain mismatch penalty: org_domain_mismatch_pdf_penalty applied to
        FIND_PDF results whose domain does NOT match the org's registered domain.
        Landing pages from third-party aggregators are common; raw PDFs from
        unrelated hosts almost always indicate a false positive.
      - Wrong-year-in-URL hard penalty: if the URL contains a 4-digit year that
        is NOT the target year, apply wrong_year_in_url_penalty.  This catches
        cases where a filetype:pdf search surfaces a previous edition.
      - Self-reference reject: URLs pointing back to this repository are
        immediately rejected as structural noise.
      - Org name cross-check: if the org name does not appear (even loosely)
        in the combined title+snippet text, apply a configurable penalty.

    Find-type-aware bonuses (unchanged from baseline):
      FIND_PDF     — pdf_url_bonus if URL has a PDF path pattern
      FIND_LANDING — gated_bonus if snippet contains gating language

    Returns (score, reject_reason).  reject_reason is non-empty only when
    score == -999 (structural reject).
    """

    # Matches a 4-digit year embedded in a URL path segment or query string.
    _YEAR_IN_URL_RE = re.compile(r"(?<!\d)(20\d{2})(?!\d)")

    def __init__(self, config: Config, classifier: ResultClassifier,
                 org_domains: OrgDomainIndex):
        self.config      = config
        self.classifier  = classifier
        self.org_domains = org_domains

    def score(self, url: str, title: str, snippet: str,
              year: int, find_type: str,
              task_stem: str = "") -> Tuple[int, str]:
        url_l    = url.lower()
        title_l  = title.lower()
        combined = f"{url_l} {title_l} {snippet.lower()}"

        # ── Self-reference reject ─────────────────────────────────────────
        for ref_domain in self.config.self_reference_domains:
            if ref_domain.lower() in url_l:
                return -999, f"self-reference domain '{ref_domain}'"

        # ── Structural rejects ────────────────────────────────────────────
        for pat in self.config.url_reject_patterns:
            if pat.lower() in url_l:
                return -999, f"url pattern '{pat}'"

        for term in self.config.financial_title_terms:
            if term.lower() in title_l:
                return -999, f"financial term '{term}'"

        for term in self.config.exclude_terms:
            if term.lower() in combined:
                return -999, f"exclude term '{term}'"

        total = 0

        # ── Positive / negative keyword signals ───────────────────────────
        for signal, w in self.config.positive_signals.items():
            if signal.lower() in combined:
                total += w

        for signal, w in self.config.negative_signals.items():
            if signal.lower() in combined:
                total += w

        # ── Year bonuses / penalties ──────────────────────────────────────
        year_str = str(year)
        if year_str in url_l:
            total += self.config.year_in_url_bonus
        if year_str in title_l:
            total += self.config.year_in_title_bonus

        # Wrong-year-in-URL penalty: URL contains a different 4-digit year.
        # Only penalise once even if multiple years appear.
        url_years = set(self._YEAR_IN_URL_RE.findall(url_l))
        wrong_years = url_years - {year_str}
        if wrong_years:
            total += self.config.wrong_year_in_url_penalty
            wrong = ", ".join(sorted(wrong_years))
            print(f"    ⚠ Wrong year(s) in URL ({wrong}) — penalty {self.config.wrong_year_in_url_penalty}")

        # ── Org domain anchoring ──────────────────────────────────────────
        result_domain = OrgDomainIndex._extract_domain(url)
        known_domain  = self.org_domains.get_domain(task_stem) if task_stem else None

        if known_domain and result_domain:
            if result_domain == known_domain or result_domain.endswith("." + known_domain):
                total += self.config.org_domain_match_bonus
            elif find_type == FIND_PDF:
                # Raw PDFs from unrelated hosts are usually false positives;
                # landing pages on aggregator sites can still be valid.
                total += self.config.org_domain_mismatch_pdf_penalty
                print(f"    ⚠ PDF domain mismatch: result={result_domain} known={known_domain}"
                      f" — penalty {self.config.org_domain_mismatch_pdf_penalty}")

        # ── Find-type bonuses ─────────────────────────────────────────────
        if find_type == FIND_PDF:
            for pat in self.config.pdf_path_patterns:
                if pat.lower() in url_l:
                    total += self.config.pdf_url_bonus
                    break
        elif find_type == FIND_LANDING:
            total += self.classifier.gated_bonus(snippet)

        return total, ""


# ══════════════════════════════════════════════════════════════════════════════
# GOOGLE SEARCHER  (two-pass)
# ══════════════════════════════════════════════════════════════════════════════

class GoogleSearcher:
    """
    Executes searches against the Google Custom Search JSON API.

    Two-pass strategy per task:
      Pass 1 — PDF query (filetype:pdf)
        Finds direct PDF download links.  If any result scores above the
        threshold, Pass 2 is skipped for this task to conserve API quota.

      Pass 2 — Landing page query (no filetype filter)
        Runs only when Pass 1 finds nothing actionable.  Surfaces gated
        pages, resource hubs, and download landing pages.

    Returns a merged, deduplicated list of annotated result dicts, each
    tagged with the search pass that found it ("pdf" or "landing").
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

    def search_task(
        self,
        task: Dict[str, Any],
        classifier: ResultClassifier,
        validator: HeuristicValidator,
    ) -> Tuple[Optional[Dict[str, Any]], str]:
        """
        Run Pass 1 (PDF) then, if nothing passes threshold, Pass 2 (landing).
        Returns (best_candidate_or_None, pass_used).
        """
        year = task["target_year"]
        stem = task.get("stem", "")

        # Pass 1 — PDF
        print(f"  Pass 1 (PDF):     ", end="", flush=True)
        raw_pdf = self._query(self.config.gs_pdf_query, task)
        best_pdf, best_pdf_score = self._best_result(
            raw_pdf, year, classifier, validator, "pdf", stem
        )

        if best_pdf is not None and best_pdf_score >= self.config.score_threshold:
            print(f"  ✓ PDF result (score {best_pdf_score})")
            return best_pdf, "pdf"

        # Pass 2 — Landing page (only if PDF pass came up empty)
        print(f"  Pass 2 (landing): ", end="", flush=True)
        raw_landing = self._query(self.config.gs_landing_query, task)

        # Deduplicate: skip any URL already seen in Pass 1
        seen_urls = {r["url"] for r in raw_pdf}
        raw_landing = [r for r in raw_landing if r["url"] not in seen_urls]

        best_land, best_land_score = self._best_result(
            raw_landing, year, classifier, validator, "landing", stem
        )

        if best_land is not None and best_land_score >= self.config.score_threshold:
            print(f"  ✓ Landing page result (score {best_land_score})")
            return best_land, "landing"

        # Return whichever scored higher, even if below threshold, so the
        # caller can log it with the actual score for debugging.
        if best_pdf is not None and (best_land is None or best_pdf_score >= best_land_score):
            return best_pdf, "pdf"
        if best_land is not None:
            return best_land, "landing"

        print(f"  ⊘ No results")
        return None, "none"

    def _best_result(
        self,
        raw: List[Dict[str, Any]],
        year: int,
        classifier: ResultClassifier,
        validator: HeuristicValidator,
        pass_label: str,
        task_stem: str = "",
    ) -> Tuple[Optional[Dict[str, Any]], int]:
        """Score all results from one pass; return (best_dict, best_score)."""
        best: Optional[Dict[str, Any]] = None
        best_score = -9999

        for item in raw:
            url     = item["url"]
            title   = item["title"]
            snippet = item["snippet"]

            if any(d.lower() in url.lower() for d in self.config.gs_skip_domains):
                continue

            find_type = classifier.classify(url, snippet)
            score, reject_reason = validator.score(
                url, title, snippet, year, find_type, task_stem
            )

            if score == -999:
                print(f"    ✗ Rejected ({reject_reason}): {url[:60]}")
                continue

            if score > best_score:
                best_score = score
                best = {
                    "url":       url,
                    "title":     title,
                    "snippet":   snippet,
                    "find_type": find_type,
                    "pass":      pass_label,
                    "score":     score,
                }

        if best is not None:
            print(f"best: {best['url'][:60]} [{best['find_type']}] score={best_score}")
        else:
            print("no results")

        return best, best_score

    def _query(self, template: str, task: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Issue one API call and return raw result items."""
        q = (template
             .replace("{organization}", task["org"])
             .replace("{title}",        task["title"])
             .replace("{year}",         str(task["target_year"])))
        print(f"'{q[:80]}'... ", end="", flush=True)

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
                    print(f"rate limited, waiting {delay:.0f}s... ", end="", flush=True)
                    time.sleep(delay)
                    delay = min(delay * self.config.gs_backoff_mult, self.config.gs_max_delay)
                else:
                    print(f"HTTP {resp.status_code}")
                    return []
            except Exception as e:
                if attempt < self.config.gs_max_retries:
                    time.sleep(delay)
                    delay = min(delay * self.config.gs_backoff_mult, self.config.gs_max_delay)
                else:
                    print(f"error: {str(e)[:60]}")
        return []


# ══════════════════════════════════════════════════════════════════════════════
# GITHUB ISSUE CREATOR  (enhanced deduplication)
# ══════════════════════════════════════════════════════════════════════════════

class IssueCreator:
    """
    Creates GitHub issues for discovery candidates.
    Issue body and labels vary by find_type so reviewers immediately know
    whether the report is a direct PDF or a gated landing page.

    Deduplication now checks both open AND recently-closed issues so
    previously-reviewed findings don't resurface.
    """

    API = "https://api.github.com"

    def __init__(self, token: str, repo: str, score_threshold: int):
        self.headers = {
            "Authorization": f"token {token}",
            "Accept":        "application/vnd.github.v3+json",
        }
        self.repo      = repo
        self.threshold = score_threshold
        self._seen_titles: Optional[List[str]] = None

    def _fetch_seen_titles(self) -> List[str]:
        """
        Fetch titles from open issues AND recently-closed issues (last 200)
        so that previously-reviewed candidates are not re-created.
        """
        if self._seen_titles is not None:
            return self._seen_titles

        titles: List[str] = []

        for state in ("open", "closed"):
            try:
                resp = requests.get(
                    f"{self.API}/repos/{self.repo}/issues",
                    headers=self.headers,
                    params={
                        "state":    state,
                        "labels":   "report-suggestion",
                        "per_page": 100,
                    },
                    timeout=15,
                )
                if resp.status_code == 200:
                    titles.extend(i.get("title", "").lower() for i in resp.json())
                else:
                    print(f"  ! Could not fetch {state} issues: HTTP {resp.status_code}")
            except Exception as e:
                print(f"  ! Could not fetch {state} issues: {e}")

        self._seen_titles = titles
        print(f"  Dedup index: {len(titles)} issue title(s) loaded (open + closed)")
        return self._seen_titles

    def issue_exists(self, org: str, year: int) -> bool:
        fragment = f"{org} {year}".lower()
        if any(fragment in t for t in self._fetch_seen_titles()):
            print(f"  ⊘ Issue already exists (open or closed) for {org} {year}")
            return True
        return False

    def create(self, candidate: Dict[str, Any]) -> bool:
        org       = candidate["org"]
        year      = candidate["target_year"]
        find_type = candidate["find_type"]

        if self.issue_exists(org, year):
            return False

        tier_label = {
            TIER_CURRENT: "🔴 Current year",
            TIER_STALE:   "🟡 One year stale",
            TIER_OLD:     "🔵 Older gap",
        }.get(candidate["tier"], candidate["tier"])

        # Find-type label and reviewer guidance
        if find_type == FIND_PDF:
            type_badge   = "📥 Direct PDF"
            type_guidance = (
                "A direct PDF link was found. Verify the URL is publicly accessible "
                "and the file downloads correctly before adding to the repository.\n\n"
                "**Important:** Confirm the PDF is from the organisation's own domain "
                "and matches the expected year — automated searches can occasionally "
                "surface older editions or third-party mirrors."
            )
        elif find_type == FIND_LANDING:
            type_badge   = "🔒 Gated Landing Page"
            type_guidance = (
                "This report appears to be behind a gated landing page requiring "
                "form submission to access the PDF. This is exactly the type of "
                "report this repository aims to make freely available.\n\n"
                "**Reviewer options:**\n"
                "- Search for a direct PDF link (try appending `filetype:pdf` to the report name in Google)\n"
                "- Check if the PDF is archived at web.archive.org\n"
                "- Check the vendor's press release or blog for a direct link\n"
                "- Submit the form to retrieve the PDF, then upload it"
            )
        else:
            type_badge   = "❓ Unclassified"
            type_guidance = (
                "The URL could not be classified as a direct PDF or a gated page. "
                "Verify manually whether this resolves to a downloadable report."
            )

        # Surface the known org domain if available so reviewers can sanity-check
        known_domain = candidate.get("known_domain", "")
        domain_note  = (
            f"\n| **Org's Known Domain** | `{known_domain}` |"
            if known_domain else ""
        )

        # ── VirusTotal block (only present for FIND_PDF candidates) ───────
        vt_result  = candidate.get("vt_result")
        vt_section = ""
        if vt_result:
            vt_status = vt_result.get("status", "")
            if vt_status == "success":
                verdict          = vt_result["verdict"]
                malicious        = vt_result["malicious_count"]
                suspicious       = vt_result["suspicious_count"]
                total            = vt_result["total_engines"]
                vt_report_url    = vt_result["report_url"]
                sha256           = vt_result["sha256"]
                verdict_icon     = ("❌" if verdict == "Malicious"
                                    else "⚠️" if verdict == "Suspicious"
                                    else "✅")
                vt_section = (
                    f"\n\n---\n\n"
                    f"### 🛡️ VirusTotal Pre-Scan\n\n"
                    f"| Field | Value |\n"
                    f"|-------|-------|\n"
                    f"| **Verdict** | {verdict_icon} {verdict} |\n"
                    f"| **Detections** | {malicious + suspicious} / {total} engines |\n"
                    f"| **SHA-256** | `{sha256}` |\n"
                    f"| **Full Report** | [🔗 View on VirusTotal]({vt_report_url}) |\n"
                )
                if verdict == "Malicious":
                    vt_section += (
                        f"\n> ❌ **This PDF was flagged as Malicious by {malicious} engine(s). "
                        f"Do NOT add this file to the repository without thorough manual review.**\n"
                    )
                elif verdict == "Suspicious":
                    vt_section += (
                        f"\n> ⚠️ **This PDF was flagged as Suspicious by {suspicious} engine(s). "
                        f"Review the VirusTotal report before adding this file.**\n"
                    )
            elif vt_status == "failed":
                reason = vt_result.get("reason", "unknown error")
                vt_section = (
                    f"\n\n---\n\n"
                    f"### 🛡️ VirusTotal Pre-Scan\n\n"
                    f"⚠️ Scan could not be completed: `{reason[:200]}`\n\n"
                    f"Manually verify the PDF before adding it to the repository.\n"
                )

        issue_title = f"[Report Discovery] {org} {year} — {candidate['title']}"
        body = (
            f"## 📄 New Security Report Discovered\n\n"
            f"| Field | Value |\n"
            f"|-------|-------|\n"
            f"| **Organization** | {org} |\n"
            f"| **Year** | {year} |\n"
            f"| **Report** | {candidate['title']} |\n"
            f"| **URL** | {candidate['url']} |\n"
            f"| **Type** | {type_badge} |"
            f"{domain_note}\n"
            f"| **Heuristic Score** | {candidate['score']} (threshold: {self.threshold}) |\n"
            f"| **Priority** | {tier_label} (repo latest: {candidate['latest_year']}) |\n\n"
            f"**Snippet:**\n> {candidate['snippet'][:400]}\n\n"
            f"---\n\n"
            f"### 🔍 Reviewer Notes\n\n"
            f"{type_guidance}"
            f"{vt_section}\n\n"
            f"---\n"
            f"*Auto-discovered by the Security Report Discovery workflow.*"
        )

        # Use a find-type specific label so issues can be filtered in the UI
        ft_label = {
            FIND_PDF:     "direct-pdf",
            FIND_LANDING: "gated-report",
            FIND_UNKNOWN: "unclassified-find",
        }.get(find_type, "automated")

        # Append a safety label when VT flagged the PDF so it stands out in triage
        extra_labels = []
        vt_verdict = (vt_result or {}).get("verdict", "")
        if vt_verdict in ("Malicious", "Suspicious"):
            extra_labels.append("malicious-pdf" if vt_verdict == "Malicious" else "suspicious-pdf")

        issue_labels = ["report-suggestion", "automated", ft_label] + extra_labels

        try:
            resp = requests.post(
                f"{self.API}/repos/{self.repo}/issues",
                headers=self.headers,
                json={"title": issue_title, "body": body,
                      "labels": issue_labels},
                timeout=15,
            )
            if resp.status_code == 201:
                html_url = resp.json().get("html_url", "")
                print(f"  ✓ Created issue [{find_type}]: {issue_title[:60]}")
                if html_url:
                    print(f"    {html_url}")
                self._seen_titles.append(issue_title.lower())
                return True
            else:
                print(f"  ! Failed to create issue: HTTP {resp.status_code}")
                return False
        except Exception as e:
            print(f"  ! Error creating issue: {str(e)[:80]}")
            return False


# ══════════════════════════════════════════════════════════════════════════════
# VIRUSTOTAL SCANNER
# ══════════════════════════════════════════════════════════════════════════════

class VirusTotalScanner:
    """
    Downloads a direct PDF URL to a temporary file, submits it to VirusTotal,
    and returns a scan result dict.  Reuses the same API patterns as
    virus-total-scan.py — all policy values (polling, rate limits, large-file
    threshold) come from workflow-config.json via Config.

    Only called for FIND_PDF candidates.  FIND_LANDING URLs are never scanned
    because they resolve to a web page, not a PDF binary.

    Result dict shape (mirrors virus-total-scan.py for consistency):
      {
        "status":           "success" | "failed" | "skipped",
        "verdict":          "Clean" | "Suspicious" | "Malicious",  # success only
        "malicious_count":  int,
        "suspicious_count": int,
        "total_engines":    int,
        "report_url":       str,
        "sha256":           str,
        "reason":           str,   # non-empty on failure/skip
      }
    """

    _API_BASE = "https://www.virustotal.com/api/v3"

    def __init__(self, api_key: str, config: "Config"):
        self.api_key = api_key
        # Pull VT policy from workflow-config.json (same source as virus-total-scan.py)
        vt = config._load("workflow-config.json").get("workflow", {}).get("virustotal", {})
        self.large_file_threshold_mb:   int = vt.get("large_file_threshold_mb",   32)
        self.poll_attempts:             int = vt.get("poll_attempts",              5)
        self.poll_backoff_base_seconds: int = vt.get("poll_backoff_base_seconds",  10)
        self.rate_limit_sleep_seconds:  int = vt.get("rate_limit_sleep_seconds",   15)

    # ── Public entry point ────────────────────────────────────────────────

    def scan_url(self, pdf_url: str) -> Dict[str, Any]:
        """
        Download the PDF at pdf_url, scan it with VirusTotal, and return a
        result dict.  Returns a "failed" result on any download or API error
        so the caller can always proceed — a scan failure is non-blocking for
        issue creation (the result is surfaced to the reviewer in the issue body).
        """
        import tempfile

        print(f"  [VT] Downloading PDF for scan: {pdf_url[:80]}")
        tmp_path = None
        try:
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
                tmp_path = tmp.name

            # Download with a browser-like UA; follow redirects
            req = urllib.request.Request(
                pdf_url,
                headers={"User-Agent": "Mozilla/5.0 (compatible; security-report-scanner/1.0)"},
            )
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = resp.read()

            # Reject anything that is not a PDF (e.g. login-redirect HTML)
            if not data[:4].startswith(b"%PDF"):
                return {
                    "status": "failed",
                    "reason": f"Downloaded content is not a valid PDF (magic: {data[:4]!r})",
                    "verdict": "", "malicious_count": 0, "suspicious_count": 0,
                    "total_engines": 0, "report_url": "", "sha256": "",
                }

            with open(tmp_path, "wb") as f:
                f.write(data)

            print(f"  [VT] Download OK — {len(data):,} bytes")
            return self._scan_file(tmp_path)

        except Exception as exc:
            return {
                "status": "failed",
                "reason": f"Download error: {str(exc)[:120]}",
                "verdict": "", "malicious_count": 0, "suspicious_count": 0,
                "total_engines": 0, "report_url": "", "sha256": "",
            }
        finally:
            if tmp_path:
                try:
                    os.unlink(tmp_path)
                except OSError:
                    pass

    # ── Internal helpers (mirror virus-total-scan.py logic exactly) ───────

    def _headers(self) -> Dict[str, str]:
        return {
            "x-apikey":   self.api_key,
            "User-Agent": "VirusTotal GitHub Action",
            "Accept":     "application/json",
        }

    @staticmethod
    def _sha256(file_path: str) -> str:
        h = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                h.update(chunk)
        return h.hexdigest()

    def _scan_file(self, file_path: str) -> Dict[str, Any]:
        """Core scan logic — identical algorithm to virus-total-scan.py:scan_file()."""
        headers    = self._headers()
        file_hash  = self._sha256(file_path)
        base_url   = self._API_BASE
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)

        try:
            # ── 1. Hash lookup ─────────────────────────────────────────────
            lookup = requests.get(
                f"{base_url}/files/{file_hash}", headers=headers, timeout=30
            )

            if lookup.status_code == 200:
                scan_data = lookup.json()

            elif lookup.status_code == 404:
                # ── 2. Upload ──────────────────────────────────────────────
                upload_endpoint = f"{base_url}/files"

                if file_size_mb > self.large_file_threshold_mb:
                    url_resp = requests.get(
                        f"{base_url}/files/upload_url", headers=headers, timeout=30
                    )
                    if url_resp.status_code == 200:
                        upload_endpoint = url_resp.json().get("data", upload_endpoint)
                    else:
                        return {
                            "status": "failed",
                            "reason": f"Could not get large-file upload URL (HTTP {url_resp.status_code})",
                            "verdict": "", "malicious_count": 0, "suspicious_count": 0,
                            "total_engines": 0, "report_url": "", "sha256": file_hash,
                        }

                with open(file_path, "rb") as f:
                    resp = requests.post(
                        upload_endpoint, headers=headers,
                        files={"file": (os.path.basename(file_path), f)},
                        timeout=300,
                    )

                if resp.status_code != 200:
                    return {
                        "status": "failed",
                        "reason": f"Upload failed (HTTP {resp.status_code})",
                        "verdict": "", "malicious_count": 0, "suspicious_count": 0,
                        "total_engines": 0, "report_url": "", "sha256": file_hash,
                    }

                scan_id = resp.json().get("data", {}).get("id")
                if not scan_id:
                    return {
                        "status": "failed",
                        "reason": "No scan ID in upload response",
                        "verdict": "", "malicious_count": 0, "suspicious_count": 0,
                        "total_engines": 0, "report_url": "", "sha256": file_hash,
                    }

                # ── 3. Poll for completion ─────────────────────────────────
                scan_data = None
                for attempt in range(self.poll_attempts):
                    sleep_secs = self.poll_backoff_base_seconds * (attempt + 1)
                    print(f"  [VT] Polling (attempt {attempt + 1}/{self.poll_attempts}, "
                          f"wait {sleep_secs}s)...")
                    time.sleep(sleep_secs)
                    status_resp = requests.get(
                        f"{base_url}/analyses/{scan_id}", headers=headers, timeout=30
                    )
                    if status_resp.status_code == 200:
                        attrs = status_resp.json().get("data", {}).get("attributes", {})
                        if attrs.get("status") == "completed":
                            final = requests.get(
                                f"{base_url}/files/{file_hash}", headers=headers, timeout=30
                            )
                            if final.status_code == 200:
                                scan_data = final.json()
                                break

                if scan_data is None:
                    return {
                        "status": "failed",
                        "reason": "Scan did not complete within polling timeout",
                        "verdict": "", "malicious_count": 0, "suspicious_count": 0,
                        "total_engines": 0, "report_url": "", "sha256": file_hash,
                    }

            else:
                return {
                    "status": "failed",
                    "reason": f"Unexpected status checking file (HTTP {lookup.status_code})",
                    "verdict": "", "malicious_count": 0, "suspicious_count": 0,
                    "total_engines": 0, "report_url": "", "sha256": file_hash,
                }

            # ── 4. Parse result ────────────────────────────────────────────
            attrs            = scan_data.get("data", {}).get("attributes", {})
            stats            = attrs.get("last_analysis_stats", {})
            malicious_count  = stats.get("malicious", 0)
            suspicious_count = stats.get("suspicious", 0)
            total_engines    = sum(stats.values())
            verdict = ("Malicious"  if malicious_count  > 0 else
                       "Suspicious" if suspicious_count > 0 else "Clean")

            print(f"  [VT] Result: {verdict} — "
                  f"{malicious_count + suspicious_count}/{total_engines} engines")

            return {
                "status":           "success",
                "verdict":          verdict,
                "malicious_count":  malicious_count,
                "suspicious_count": suspicious_count,
                "total_engines":    total_engines,
                "report_url":       f"https://www.virustotal.com/gui/file/{file_hash}",
                "sha256":           file_hash,
                "reason":           "",
            }

        except Exception as exc:
            return {
                "status": "failed",
                "reason": str(exc)[:200],
                "verdict": "", "malicious_count": 0, "suspicious_count": 0,
                "total_engines": 0, "report_url": "", "sha256": "",
            }


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main() -> int:
    ap = argparse.ArgumentParser(description="Security Report Discovery")
    ap.add_argument("--artifacts-dir",   default=".github/artifacts")
    ap.add_argument("--max-discoveries", type=int, default=None)
    ap.add_argument("--date", default=None,
                    help="Override today's date for testing (YYYY-MM-DD)")
    args = ap.parse_args()

    today = date.fromisoformat(args.date) if args.date else date.today()

    print(f"\n{'='*70}")
    print(f"Security Report Discovery  —  {today.isoformat()}")
    print(f"{'='*70}\n")

    try:
        config = Config(args.artifacts_dir)
    except Exception as e:
        print(f"ERROR loading config: {e}")
        return 1

    max_issues = args.max_discoveries if args.max_discoveries is not None else config.max_issues

    print(f"✓ Config loaded")
    print(f"  Max issues/run    : {max_issues}")
    print(f"  Max tasks/run     : {config.max_tasks}")
    print(f"  Score threshold   : {config.score_threshold}")
    print(f"  Rotation (current): {config.rotation_current} days")
    print(f"  Rotation (stale)  : {config.rotation_stale} days")
    print(f"  Rotation (old)    : {config.rotation_old} days")
    print()

    gh_token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN", "")
    repo     = os.environ.get("GITHUB_REPOSITORY", "")
    if not gh_token or not repo:
        print("ERROR: GH_TOKEN / GITHUB_REPOSITORY required")
        return 1

    # VirusTotal scanner — optional; only active when the API key is present.
    # Direct PDF finds are scanned before issue creation; landing-page finds
    # are never scanned because they resolve to a web page, not a PDF binary.
    vt_api_key = os.environ.get("VIRUS_TOTAL_API_KEY", "")
    vt_scanner: Optional[VirusTotalScanner] = None
    if vt_api_key:
        vt_scanner = VirusTotalScanner(vt_api_key, config)
        print(f"✓ VirusTotal scanner active (direct PDF finds will be scanned)")
    else:
        print(f"⊘ VIRUS_TOTAL_API_KEY not set — PDF pre-scanning skipped")
    print()

    print(f"{'='*70}")
    print("Building lineage index...")
    print(f"{'='*70}\n")
    lineage    = ReportLineageIndex(config.PDF_ROOT)
    org_domains = OrgDomainIndex()          # parses README.md
    scheduler  = SlotScheduler(today)
    scanner    = ReportScanner(config, lineage, scheduler)

    print()
    tasks = scanner.get_todays_tasks()

    if not tasks:
        print("\n⊘ No searches scheduled for today.")
        return 0

    tasks_to_run = tasks[: config.max_tasks]
    if len(tasks) > config.max_tasks:
        print(f"\n⚠ {len(tasks)} tasks due — capping at {config.max_tasks}")

    print(f"\n{'='*70}")
    print(f"Running {len(tasks_to_run)} task(s)  [2 API calls each, issue limit: {max_issues}]")
    print(f"{'='*70}\n")

    try:
        searcher = GoogleSearcher(config)
    except RuntimeError as e:
        print(f"ERROR: {e}")
        return 1

    classifier = ResultClassifier(config)
    validator  = HeuristicValidator(config, classifier, org_domains)
    creator    = IssueCreator(gh_token, repo, config.score_threshold)

    stats = {
        "tasks_run":      0,
        "skip_score":     0,
        "no_results":     0,
        "issues_created": 0,
        "issues_skipped": 0,
        "pdf_finds":      0,
        "landing_finds":  0,
        "unknown_finds":  0,
        "vt_clean":       0,
        "vt_suspicious":  0,
        "vt_malicious":   0,
        "vt_failed":      0,
        "vt_skipped":     0,
    }
    tier_counts = {TIER_CURRENT: 0, TIER_STALE: 0, TIER_OLD: 0}

    for i, task in enumerate(tasks_to_run, 1):
        if stats["issues_created"] >= max_issues:
            print(f"\n⊘ Issue limit ({max_issues}) reached — stopping")
            break

        org  = task["org"]
        year = task["target_year"]
        tier = task["tier"]
        stem = task["stem"]

        print(f"\n[{i}/{len(tasks_to_run)}] {org} → {year}  [{tier}]")

        known_domain = org_domains.get_domain(stem)
        if known_domain:
            print(f"  Org domain: {known_domain}")

        stats["tasks_run"] += 1
        tier_counts[tier]  += 1

        best, pass_used = searcher.search_task(task, classifier, validator)

        if best is None or best["score"] < config.score_threshold:
            if best is None:
                stats["no_results"] += 1
            else:
                print(f"  ⊘ Best score {best['score']} < threshold {config.score_threshold} — suppressed")
                print(f"    [{best['find_type']}] {best['url'][:70]}")
                stats["skip_score"] += 1
            time.sleep(config.gs_rate_sleep)
            continue

        # ── VirusTotal pre-scan for direct PDF finds ──────────────────────
        vt_result: Optional[Dict[str, Any]] = None
        ft = best["find_type"]

        if ft == FIND_PDF:
            if vt_scanner:
                print(f"  [VT] Scanning direct PDF...")
                time.sleep(vt_scanner.rate_limit_sleep_seconds)
                vt_result = vt_scanner.scan_url(best["url"])
                vt_status = vt_result.get("status", "")
                if vt_status == "success":
                    verdict = vt_result["verdict"]
                    if verdict == "Clean":
                        stats["vt_clean"] += 1
                    elif verdict == "Suspicious":
                        stats["vt_suspicious"] += 1
                        print(f"  ⚠ VT: Suspicious — issue will be labeled")
                    elif verdict == "Malicious":
                        stats["vt_malicious"] += 1
                        print(f"  ❌ VT: Malicious — issue will be labeled, reviewer must decide")
                else:
                    stats["vt_failed"] += 1
                    print(f"  ⚠ VT scan failed: {vt_result.get('reason', '')[:100]}")
            else:
                stats["vt_skipped"] += 1

        # Assemble full candidate dict for issue creation
        candidate = {
            **best,
            "org":          org,
            "title":        task["title"],
            "target_year":  year,
            "latest_year":  task["latest_year"],
            "tier":         tier,
            "threshold":    config.score_threshold,
            "known_domain": known_domain or "",
            "vt_result":    vt_result,
        }

        if ft == FIND_PDF:
            stats["pdf_finds"] += 1
        elif ft == FIND_LANDING:
            stats["landing_finds"] += 1
        else:
            stats["unknown_finds"] += 1

        if creator.create(candidate):
            stats["issues_created"] += 1
        else:
            stats["issues_skipped"] += 1

        time.sleep(config.gs_rate_sleep)

    print(f"\n{'='*70}")
    print("Discovery Summary")
    print(f"{'='*70}")
    print(f"  Tasks run           : {stats['tasks_run']}")
    print(f"    CURRENT tier      : {tier_counts[TIER_CURRENT]}")
    print(f"    STALE tier        : {tier_counts[TIER_STALE]}")
    print(f"    OLD tier          : {tier_counts[TIER_OLD]}")
    print(f"  No results          : {stats['no_results']}")
    print(f"  Suppressed (score)  : {stats['skip_score']}")
    print(f"  Issues created      : {stats['issues_created']}")
    print(f"    Direct PDF finds  : {stats['pdf_finds']}")
    print(f"    Gated page finds  : {stats['landing_finds']}")
    print(f"    Unclassified      : {stats['unknown_finds']}")
    print(f"  Issues skipped(dup) : {stats['issues_skipped']}")
    if vt_scanner:
        print(f"  VirusTotal scans    :")
        print(f"    Clean             : {stats['vt_clean']}")
        print(f"    Suspicious        : {stats['vt_suspicious']}")
        print(f"    Malicious         : {stats['vt_malicious']}")
        print(f"    Failed            : {stats['vt_failed']}")
    else:
        print(f"  VT scans skipped    : {stats['vt_skipped']} (no API key)")
    print(f"{'='*70}")

    print(f"DISCOVERY_TASKS={stats['tasks_run']}")
    print(f"DISCOVERY_CREATED={stats['issues_created']}")
    print(f"DISCOVERY_SUPPRESSED={stats['skip_score']}")
    print(f"DISCOVERY_SKIPPED={stats['issues_skipped']}")
    print(f"DISCOVERY_PDF_FINDS={stats['pdf_finds']}")
    print(f"DISCOVERY_LANDING_FINDS={stats['landing_finds']}")
    print(f"DISCOVERY_TIER_CURRENT={tier_counts[TIER_CURRENT]}")
    print(f"DISCOVERY_TIER_STALE={tier_counts[TIER_STALE]}")
    print(f"DISCOVERY_TIER_OLD={tier_counts[TIER_OLD]}")
    print(f"DISCOVERY_VT_CLEAN={stats['vt_clean']}")
    print(f"DISCOVERY_VT_SUSPICIOUS={stats['vt_suspicious']}")
    print(f"DISCOVERY_VT_MALICIOUS={stats['vt_malicious']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())