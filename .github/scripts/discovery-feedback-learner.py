"""
discovery-feedback-learner.py

Reads .github/artifacts/discovery-feedback.json, analyses triage outcomes
with Gemini, and writes improved scoring adjustments back to the same file
under the `learned` key.

The updated file is then committed by the calling workflow.  All config
(model names, retry policy) comes from ai-models.json and workflow-config.json.

Usage:
    python .github/scripts/discovery-feedback-learner.py \
        [--artifacts-dir .github/artifacts] \
        [--min-events 5] \
        [--dry-run]
"""

import argparse
import json
import os
import sys
import time
import re
import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional


# ══════════════════════════════════════════════════════════════════════════════
# DEPENDENCIES
# ══════════════════════════════════════════════════════════════════════════════

try:
    from google import genai
    from google.genai import types as genai_types
    _GENAI_NEW = True
except ImportError:
    try:
        import google.generativeai as genai
        _GENAI_NEW = False
    except ImportError:
        print("ERROR: google-generativeai package required. pip install google-genai")
        sys.exit(1)

try:
    import subprocess
except ImportError:
    subprocess = None


# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

class Config:
    def __init__(self, artifacts_dir: str):
        self.dir = Path(artifacts_dir)
        wf  = self._load("workflow-config.json")
        aim = self._load("ai-models.json")
        fb  = self._load("discovery-feedback.json")
        gsc = self._load("google-search-config.json")

        # AI model
        models = aim.get("models", {})
        self.primary_model   = models.get("primary",   "gemini-2.5-flash")
        self.secondary_model = models.get("secondary", "gemini-2.5-flash")

        # AI config
        cfg = aim.get("configurations", {}).get("categorization", {})
        self.temperature      = cfg.get("temperature",      0.1)
        self.top_p            = cfg.get("top_p",            0.85)
        self.max_output_tokens = cfg.get("max_output_tokens", 4096)

        # Retry policies
        rp = aim.get("retry_policy", {})
        self.retry_max      = rp.get("max_attempts",         3)
        self.retry_delay    = rp.get("initial_delay_seconds", 2)
        self.retry_mult     = rp.get("backoff_multiplier",    2)
        self.retry_max_del  = rp.get("max_delay_seconds",    30)

        qrp = aim.get("quota_retry_policy", {})
        self.quota_max      = qrp.get("max_attempts",         3)
        self.quota_delay    = qrp.get("initial_delay_seconds", 60)
        self.quota_mult     = qrp.get("backoff_multiplier",    2)
        self.quota_max_del  = qrp.get("max_delay_seconds",   180)

        # Google Search heuristics (used as context for Gemini)
        gs = gsc.get("google_search", {})
        h  = gs.get("discovery_heuristics", {})
        self.base_positive_signals = h.get("positive_signals", {})
        self.base_negative_signals = h.get("negative_signals", {})
        self.base_threshold        = h.get("score_threshold",  20)

        # Feedback data
        self.feedback = fb

    def _load(self, name: str) -> Dict[str, Any]:
        p = self.dir / name
        if not p.exists():
            raise FileNotFoundError(f"Required config missing: {p}")
        with open(p, encoding="utf-8") as f:
            return json.load(f)


# ══════════════════════════════════════════════════════════════════════════════
# GEMINI CLIENT
# ══════════════════════════════════════════════════════════════════════════════

class GeminiClient:
    def __init__(self, config: Config):
        api_key = os.environ.get("GEMINI_API_KEY", "")
        if not api_key:
            raise RuntimeError(
                "GEMINI_API_KEY not set. Add it under Settings -> Secrets and variables -> Actions."
            )
        if _GENAI_NEW:
            self.client = genai.Client(api_key=api_key)
        else:
            genai.configure(api_key=api_key)
            self.client = None
        self.config = config

    def generate(self, prompt: str, model_override: Optional[str] = None) -> str:
        for model_name in (model_override or self.config.primary_model,
                           self.config.secondary_model):
            result = self._try_model(prompt, model_name)
            if result is not None:
                return result
            print(f"  [Gemini] {model_name} failed — trying secondary")
        raise RuntimeError("Both primary and secondary Gemini models failed.")

    def _try_model(self, prompt: str, model_name: str) -> Optional[str]:
        delay = self.config.retry_delay
        for attempt in range(1, self.config.retry_max + 1):
            try:
                if _GENAI_NEW:
                    response = self.client.models.generate_content(
                        model=model_name,
                        contents=prompt,
                        config=genai_types.GenerateContentConfig(
                            temperature=self.config.temperature,
                            top_p=self.config.top_p,
                            max_output_tokens=self.config.max_output_tokens,
                        ),
                    )
                else:
                    response = genai.GenerativeModel(model_name).generate_content(
                        prompt,
                        generation_config={
                            "temperature":       self.config.temperature,
                            "top_p":             self.config.top_p,
                            "max_output_tokens": self.config.max_output_tokens,
                        },
                    )
                return response.text.strip() if response.text else ""
            except Exception as e:
                err = str(e).lower()
                if "401" in err or "403" in err or "api_key" in err:
                    raise RuntimeError(f"Auth error — check GEMINI_API_KEY: {str(e)[:100]}")
                if "429" in err or "resource_exhausted" in err or "quota" in err:
                    wait = min(self.config.quota_delay * (self.config.quota_mult ** (attempt - 1)),
                               self.config.quota_max_del)
                    print(f"  [Gemini] Quota (429) — waiting {wait}s")
                    time.sleep(wait)
                elif attempt < self.config.retry_max:
                    print(f"  [Gemini] Error attempt {attempt}: {str(e)[:60]} — retry in {delay}s")
                    time.sleep(delay)
                    delay = min(delay * self.config.retry_mult, self.config.retry_max_del)
                else:
                    print(f"  [Gemini] All retries exhausted for {model_name}")
                    return None
        return None



# ══════════════════════════════════════════════════════════════════════════════
# CLOSURE COMMENT READER
# ══════════════════════════════════════════════════════════════════════════════

class ClosureCommentReader:
    """
    Fetches closed discovery issues and reads their comments to extract
    the reason for closure.  Enriches triage_log entries that lack a
    reason, and surfaces patterns that Gemini can act on.

    Uses the GH CLI (gh) which is pre-installed on GitHub Actions runners.
    Falls back gracefully when GH_TOKEN or gh CLI is unavailable.
    """

    MAX_ISSUES = 100  # closed issues to scan per run

    def __init__(self):
        self.token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN", "")
        self.repo  = os.environ.get("GITHUB_REPOSITORY", "")
        self.available = bool(self.token and self.repo)
        if not self.available:
            print("ℹ️  GH_TOKEN / GITHUB_REPOSITORY not set — closure comment reading skipped")

    def enrich_triage_log(self, triage_log: List[Dict]) -> List[Dict]:
        """
        For entries in triage_log that have no reason, try to fetch the
        first human comment from the GitHub issue and use it as the reason.
        Returns the enriched log.
        """
        if not self.available:
            return triage_log

        enriched_count = 0
        for entry in triage_log:
            if entry.get("reason") or not entry.get("issue"):
                continue
            reason = self._fetch_first_human_comment(str(entry["issue"]))
            if reason:
                entry["reason"] = reason[:300]
                enriched_count += 1

        if enriched_count:
            print(f"  Enriched {enriched_count} triage log entries with closure comments")
        return triage_log

    def fetch_recent_closed_patterns(self) -> List[Dict[str, str]]:
        """
        Fetch recently-closed automated discovery issues and extract
        (outcome, org, url, comment_text) tuples for Gemini to analyse.
        """
        if not self.available:
            return []

        import urllib.request
        import urllib.parse

        patterns = []
        headers = {
            "Authorization": f"token {self.token}",
            "Accept":        "application/vnd.github.v3+json",
            "User-Agent":    "discovery-feedback-learner",
        }

        try:
            url = (
                f"https://api.github.com/repos/{self.repo}/issues"
                f"?state=closed&labels=automated,report-suggestion"
                f"&per_page={self.MAX_ISSUES}&sort=updated&direction=desc"
            )
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                issues = json.loads(resp.read())

            for issue in issues:
                num    = issue.get("number")
                title  = issue.get("title", "")
                labels = [l.get("name", "") for l in issue.get("labels", [])]
                outcome = next(
                    (l for l in labels if l in
                     ("false-positive", "duplicate", "mismatch", "accepted")), ""
                )
                if not outcome or not num:
                    continue

                comment_text = self._fetch_first_human_comment(str(num))
                if comment_text:
                    patterns.append({
                        "issue":   num,
                        "title":   title[:120],
                        "outcome": outcome,
                        "comment": comment_text[:400],
                    })

        except Exception as e:
            print(f"  WARNING: Could not fetch closed issues: {str(e)[:80]}")

        print(f"  Fetched {len(patterns)} closure comment(s) from GitHub")
        return patterns

    def _fetch_first_human_comment(self, issue_num: str) -> str:
        """Return the text of the first non-bot comment on an issue, or ''."""
        import urllib.request

        headers = {
            "Authorization": f"token {self.token}",
            "Accept":        "application/vnd.github.v3+json",
            "User-Agent":    "discovery-feedback-learner",
        }
        try:
            url = f"https://api.github.com/repos/{self.repo}/issues/{issue_num}/comments?per_page=10"
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                comments = json.loads(resp.read())

            for comment in comments:
                author = comment.get("user", {}).get("login", "")
                body   = comment.get("body", "").strip()
                # Skip bot comments and triage-command lines
                if author.endswith("[bot]") or body.startswith("/"):
                    continue
                # Strip markdown quote blocks (> ...) from triage acknowledgements
                lines = [l for l in body.splitlines()
                         if l.strip() and not l.strip().startswith(">")
                         and not l.strip().startswith("_This outcome")]
                clean = " ".join(lines)[:300]
                if len(clean) > 10:
                    return clean
        except Exception:
            pass
        return ""


# ══════════════════════════════════════════════════════════════════════════════
# FEEDBACK ANALYSER
# ══════════════════════════════════════════════════════════════════════════════

class FeedbackAnalyser:
    """
    Builds a structured summary of triage events and asks Gemini to suggest
    scoring improvements.  All output is validated before writing to disk.
    """

    def __init__(self, config: Config, client: GeminiClient):
        self.config = config
        self.client = client

    def analyse(self) -> Dict[str, Any]:
        log     = self.config.feedback.get("triage_log", [])
        counts  = self.config.feedback.get("outcome_counts", {})
        total   = sum(counts.values())

        if total == 0:
            print("No triage events yet — nothing to learn from.")
            return {}

        print(f"\nAnalysing {total} triage event(s):")
        for k, v in counts.items():
            print(f"  {k}: {v}")

        # ── Segment events by outcome ────────────────────────────────────
        fp_events  = [e for e in log if e.get("outcome") == "false_positive"]
        dup_events = [e for e in log if e.get("outcome") == "duplicate"]
        mm_events  = [e for e in log if e.get("outcome") == "mismatch"]
        tp_events  = [e for e in log if e.get("outcome") == "true_positive"]

        # Enrich triage log with GitHub closure comments
        comment_reader = ClosureCommentReader()
        log = comment_reader.enrich_triage_log(log)
        closure_patterns = comment_reader.fetch_recent_closed_patterns()

        # Build compact event summaries to avoid token overuse
        def summarise_events(events: List[Dict], max_count: int = 30) -> str:
            rows = []
            for e in events[:max_count]:
                rows.append(
                    f"- org={e.get('org','?')} year={e.get('year','?')} "
                    f"score={e.get('score','?')} find_type={e.get('find_type','?')} "
                    f"url={e.get('url','?')[:80]} "
                    f"reason={e.get('reason','')[:100]}"
                )
            extra = len(events) - max_count
            if extra > 0:
                rows.append(f"... and {extra} more")
            return "\n".join(rows) if rows else "(none)"

        prompt = f"""You are an expert at tuning information-retrieval heuristics for a
cybersecurity report discovery pipeline.  The pipeline searches Google for annual
security reports and scores each result.  Below is a summary of how human reviewers
have triaged the issues the pipeline created.

=== CURRENT SCORING CONFIG ===
Score threshold (min to create issue): {self.config.base_threshold}

Positive keyword signals (signal → score bonus):
{json.dumps(self.config.base_positive_signals, indent=2)}

Negative keyword signals (signal → score penalty, values already negative):
{json.dumps(self.config.base_negative_signals, indent=2)}

=== TRIAGE OUTCOMES ===
Total events : {total}
True positive: {len(tp_events)}
False positive: {len(fp_events)}
Mismatch     : {len(mm_events)}
Duplicate    : {len(dup_events)}

FALSE POSITIVE events (wrong/unrelated result — we want fewer of these):
{summarise_events(fp_events)}

MISMATCH events (correct org, wrong year/edition/category):
{summarise_events(mm_events)}

DUPLICATE events (already in repo or repeat discovery):
{summarise_events(dup_events)}

TRUE POSITIVE events (valid finds — we want to keep these):
{summarise_events(tp_events)}

=== CLOSURE COMMENTS FROM GITHUB ===
These are the actual comments left by reviewers when closing issues.
They provide richer context than just the outcome label:
{closure_comment_block}

=== YOUR TASK ===
Analyse the patterns in false positive, mismatch, duplicate events, AND the
closure comments above.  Suggest scoring adjustments that would reduce bad
issues WITHOUT eliminating true positive results.  Pay special attention to
recurring language in closure comments (e.g. "already in repo", "wrong year",
"financial report") as these are the strongest signals.

Respond ONLY with a valid JSON object matching this schema exactly.
Do not include any markdown, explanation, or commentary outside the JSON:

{{
  "signal_weight_deltas": {{
    "positive": {{"<signal_keyword>": <integer_delta>, ...}},
    "negative": {{"<signal_keyword>": <integer_delta>, ...}}
  }},
  "domain_blocklist": ["<domain1>", ...],
  "domain_trustlist": ["<domain1>", ...],
  "org_specific_signals": {{
    "<org_name_lowercase>": {{
      "positive": {{"<keyword>": <integer>, ...}},
      "negative": {{"<keyword>": <integer>, ...}}
    }}
  }},
  "title_patterns": {{
    "reject": ["<regex_pattern>", ...],
    "trust":  ["<regex_pattern>", ...]
  }},
  "score_threshold_delta": <integer>,
  "gemini_rejection_patterns": ["<phrase found repeatedly in false positive snippets>"],
  "validation_threshold": <float between 0.3 and 1.0>,
  "url_blocklist": ["<specific URL to permanently block>"],
  "summary": "<2-3 sentence plain-English explanation of main adjustments>"
}}

Rules:
- signal_weight_deltas: only include signals that NEED changing.
- domain_blocklist: only add domains with 2+ false positives.
- domain_trustlist: only add domains with 2+ true positives.
- score_threshold_delta: clamp ±5; 0 if no change needed.
- title_patterns.reject: regex patterns seen across 2+ false positives.
- gemini_rejection_patterns: short phrases (3-6 words) that appear repeatedly
  in the title/snippet of false positive closures. These are fed to the
  Gemini pre-validator to reject similar candidates before heuristic scoring.
- validation_threshold: adjust only if similarity dedup is producing too many
  false "duplicate" suppressions (lower it) or too many actual dups pass through (raise it).
  Default is 0.75. Only adjust if there is clear evidence to do so.
- url_blocklist: add a URL only if it appears in 3+ false positive events
  AND is clearly a noise source (e.g. an aggregator mirror, a blog post, etc.)
- Keep all arrays and objects present even if empty.
"""

        # Format closure comments for inclusion in the prompt
        if closure_patterns:
            rows = [
                "- issue #{} [{}] \"{}\" -> {}".format(
                    p["issue"], p["outcome"], p["title"][:60], p["comment"][:200]
                )
                for p in closure_patterns[:30]
            ]
            closure_comment_block = "\n".join(rows)
        else:
            closure_comment_block = "(none available)"
        prompt = prompt.replace("{closure_comment_block}", closure_comment_block)

        print("\nSending triage data to Gemini for analysis...")
        raw = self.client.generate(prompt)

        # Strip markdown fences if present
        raw = re.sub(r"^```(?:json)?\s*", "", raw.strip(), flags=re.MULTILINE)
        raw = re.sub(r"\s*```$", "", raw.strip(), flags=re.MULTILINE)

        try:
            suggestions = json.loads(raw)
        except json.JSONDecodeError as e:
            print(f"ERROR: Gemini response was not valid JSON: {e}")
            print(f"Raw response (first 500 chars):\n{raw[:500]}")
            return {}

        print(f"\nGemini analysis complete.")
        print(f"  Summary: {suggestions.get('summary', '(no summary)')}")

        return suggestions


# ══════════════════════════════════════════════════════════════════════════════
# FEEDBACK WRITER
# ══════════════════════════════════════════════════════════════════════════════

class FeedbackWriter:
    def __init__(self, artifacts_dir: Path):
        self.path = artifacts_dir / "discovery-feedback.json"

    def apply(self, feedback: Dict[str, Any], suggestions: Dict[str, Any],
              dry_run: bool = False) -> Dict[str, Any]:
        """Merge Gemini suggestions into the learned block and write to disk."""
        now = datetime.datetime.utcnow().isoformat() + "Z"

        learned = feedback.setdefault("learned", {})

        # ── Signal weight deltas ─────────────────────────────────────────
        deltas = suggestions.get("signal_weight_deltas", {})
        learned_deltas = learned.setdefault("signal_weight_deltas", {"positive": {}, "negative": {}})
        for direction in ("positive", "negative"):
            src  = deltas.get(direction, {})
            dest = learned_deltas.setdefault(direction, {})
            for signal, delta in src.items():
                if isinstance(delta, (int, float)):
                    dest[signal] = int(delta)

        # ── Domain blocklist ─────────────────────────────────────────────
        new_blocks = [d for d in suggestions.get("domain_blocklist", []) if isinstance(d, str)]
        existing   = learned.get("domain_blocklist", {})
        block_list = existing.get("domains", [])
        reason_map = existing.get("reason_map", {})
        for d in new_blocks:
            if d not in block_list:
                block_list.append(d)
                reason_map[d] = "Added by Gemini learner based on false positive patterns"
        learned["domain_blocklist"] = {"domains": block_list, "reason_map": reason_map}

        # ── Domain trustlist ─────────────────────────────────────────────
        new_trusts   = [d for d in suggestions.get("domain_trustlist", []) if isinstance(d, str)]
        existing_t   = learned.get("domain_trustlist", {"domains": [], "bonus": 10})
        trust_list   = existing_t.get("domains", [])
        for d in new_trusts:
            if d not in trust_list:
                trust_list.append(d)
        existing_t["domains"] = trust_list
        learned["domain_trustlist"] = existing_t

        # ── Org-specific signals ─────────────────────────────────────────
        org_sigs = suggestions.get("org_specific_signals", {})
        dest_org = learned.setdefault("org_specific_signals", {})
        for org, sigs in org_sigs.items():
            org_l = org.lower()
            dest_org.setdefault(org_l, {"positive": {}, "negative": {}})
            for direction in ("positive", "negative"):
                for signal, weight in sigs.get(direction, {}).items():
                    if isinstance(weight, (int, float)):
                        dest_org[org_l][direction][signal] = int(weight)

        # ── Title patterns ───────────────────────────────────────────────
        tp     = suggestions.get("title_patterns", {})
        dest_tp = learned.setdefault("title_patterns", {"reject": [], "trust": []})
        for kind in ("reject", "trust"):
            for pat in tp.get(kind, []):
                if isinstance(pat, str) and pat not in dest_tp[kind]:
                    dest_tp[kind].append(pat)

        # ── Score threshold delta ────────────────────────────────────────
        raw_delta = suggestions.get("score_threshold_delta", 0)
        if isinstance(raw_delta, (int, float)):
            delta = max(-5, min(5, int(raw_delta)))
            learned["score_threshold_delta"] = learned.get("score_threshold_delta", 0) + delta

        # ── Gemini rejection patterns (new: phrases seen in rejected snippets) ──
        new_reject_phrases = [
            p for p in suggestions.get("gemini_rejection_patterns", [])
            if isinstance(p, str)
        ]
        existing_phrases = learned.setdefault("gemini_rejection_patterns", [])
        for p in new_reject_phrases:
            if p not in existing_phrases:
                existing_phrases.append(p)

        # ── Validation threshold (similarity dedup strictness) ───────────
        vt = suggestions.get("validation_threshold")
        if isinstance(vt, float) and 0.3 <= vt <= 1.0:
            learned["validation_threshold"] = vt

        # ── URL fingerprint blocklist additions from Gemini ───────────────
        url_blocks = suggestions.get("url_blocklist", [])
        if isinstance(url_blocks, list):
            fp_path = self.path
            try:
                with open(fp_path, encoding="utf-8") as f:
                    fb = json.load(f)
                fps = fb.setdefault("url_fingerprints", {"seen": {}, "blocked": []})
                import hashlib
                for url in url_blocks:
                    if isinstance(url, str):
                        h = hashlib.sha256(url.strip().lower().encode()).hexdigest()[:16]
                        if h not in fps["blocked"]:
                            fps["blocked"].append(h)
            except Exception:
                pass

        # ── Summary + timestamps ─────────────────────────────────────────
        learned["summary"]              = suggestions.get("summary", "")
        learned["last_gemini_analysis"] = now

        feedback["last_updated"]      = now
        feedback["last_learner_run"]  = now

        if dry_run:
            print("\n[DRY RUN] Would write:")
            print(json.dumps({"learned": learned}, indent=2)[:2000])
            return feedback

        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(feedback, f, indent=2)
            f.write("\n")

        print(f"\n✓ Feedback file updated: {self.path}")
        return feedback


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main() -> int:
    ap = argparse.ArgumentParser(description="Discovery Feedback Learner")
    ap.add_argument("--artifacts-dir", default=".github/artifacts")
    ap.add_argument("--min-events", type=int, default=5,
                    help="Minimum triage events before running Gemini analysis (default: 5)")
    ap.add_argument("--dry-run", action="store_true",
                    help="Analyse and print suggestions without writing to disk")
    args = ap.parse_args()

    print(f"\n{'='*70}")
    print("Discovery Feedback Learner")
    print(f"{'='*70}\n")

    # ── Load config ──────────────────────────────────────────────────────
    try:
        config = Config(args.artifacts_dir)
    except Exception as e:
        print(f"ERROR loading config: {e}")
        return 1

    total_events = config.feedback.get("total_feedback_events", 0)
    print(f"✓ Config loaded")
    print(f"  Feedback events : {total_events}")
    print(f"  Min events      : {args.min_events}")

    if total_events < args.min_events:
        print(f"\n⊘ Not enough feedback events ({total_events} < {args.min_events}) — skipping Gemini analysis.")
        print("  Keep triaging issues; the learner will run once enough data is accumulated.")
        return 0

    # ── Run Gemini analysis ──────────────────────────────────────────────
    try:
        client   = GeminiClient(config)
        analyser = FeedbackAnalyser(config, client)
    except RuntimeError as e:
        print(f"ERROR: {e}")
        return 1

    suggestions = analyser.analyse()
    if not suggestions:
        print("⊘ No suggestions generated.")
        return 0

    # ── Write results ─────────────────────────────────────────────────────
    writer = FeedbackWriter(Path(args.artifacts_dir))
    writer.apply(config.feedback, suggestions, dry_run=args.dry_run)

    print(f"\n{'='*70}")
    print("Learner Summary")
    print(f"{'='*70}")
    learned = config.feedback.get("learned", {})
    deltas  = learned.get("signal_weight_deltas", {})
    print(f"  Positive signal deltas : {len(deltas.get('positive', {}))}")
    print(f"  Negative signal deltas : {len(deltas.get('negative', {}))}")
    print(f"  Domain blocklist size  : {len(learned.get('domain_blocklist', {}).get('domains', []))}")
    print(f"  Domain trustlist size  : {len(learned.get('domain_trustlist', {}).get('domains', []))}")
    print(f"  Org-specific overrides : {len(learned.get('org_specific_signals', {}))}")
    print(f"  Threshold delta        : {learned.get('score_threshold_delta', 0):+d}")
    print(f"  Summary: {learned.get('summary', '(none)')}")
    print(f"{'='*70}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
