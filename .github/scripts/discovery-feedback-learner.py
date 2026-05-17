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
    import google.generativeai as genai
except ImportError:
    print("ERROR: google-genai required.  pip install google-genai")
    sys.exit(1)


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
        api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_GEMINI_API_KEY", "")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY or GOOGLE_GEMINI_API_KEY env var required")
        genai.configure(api_key=api_key)
        self.config = config

    def generate(self, prompt: str, model_override: Optional[str] = None) -> str:
        model_name = model_override or self.config.primary_model
        model = genai.GenerativeModel(
            model_name=model_name,
            generation_config={
                "temperature":        self.config.temperature,
                "top_p":              self.config.top_p,
                "max_output_tokens":  self.config.max_output_tokens,
            }
        )

        delay = self.config.retry_delay
        for attempt in range(1, self.config.retry_max + 1):
            try:
                response = model.generate_content(prompt)
                return response.text
            except Exception as e:
                err = str(e).lower()
                if "429" in err or "resource_exhausted" in err or "quota" in err:
                    wait = min(self.config.quota_delay * (self.config.quota_mult ** (attempt - 1)),
                               self.config.quota_max_del)
                    print(f"  [Gemini] Quota limit — waiting {wait}s (attempt {attempt}/{self.config.quota_max})")
                    time.sleep(wait)
                elif attempt < self.config.retry_max:
                    print(f"  [Gemini] Error on attempt {attempt}: {str(e)[:80]} — retrying in {delay}s")
                    time.sleep(delay)
                    delay = min(delay * self.config.retry_mult, self.config.retry_max_del)
                else:
                    raise

        # Fallback to secondary model
        print(f"  [Gemini] Primary model failed — falling back to {self.config.secondary_model}")
        response = genai.GenerativeModel(self.config.secondary_model).generate_content(prompt)
        return response.text


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

=== YOUR TASK ===
Analyse the patterns in the false positive, mismatch, and duplicate events.
Suggest scoring adjustments that would reduce bad issues WITHOUT eliminating
the types of true positive results seen above.

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
  "summary": "<2-3 sentence plain-English explanation of main adjustments>"
}}

Rules:
- signal_weight_deltas: only include signals that NEED changing; empty dict is fine.
  Positive deltas increase a positive bonus; negative deltas decrease it.
  For negative signals, a positive delta makes the penalty LESS severe; a
  negative delta makes the penalty MORE severe.
- domain_blocklist: only add domains appearing in 2+ false positive events.
- domain_trustlist: only add domains appearing in 2+ true positive events.
- score_threshold_delta: only adjust ±5 at most; 0 is fine if no change needed.
- title_patterns.reject: only add regex patterns seen across 2+ false positives.
- Keep all arrays and objects present even if empty.
"""

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
            # Clamp to ±5 per run for safety
            delta = max(-5, min(5, int(raw_delta)))
            learned["score_threshold_delta"] = learned.get("score_threshold_delta", 0) + delta

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
