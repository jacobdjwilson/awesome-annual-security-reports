# AI Instruction Set for Tuning Information-Retrieval Heuristics
## Purpose
Analyze triage outcomes and closure comments from a cybersecurity report discovery pipeline to suggest scoring adjustments that reduce bad issues without eliminating true positive results.
## Goals
1. **Analyze Triage Outcomes**: Evaluate false positives, mismatches, and duplicates.
2. **Interpret Closure Comments**: Pay special attention to recurring language in human reviewer closure comments (e.g. "already in repo", "wrong year", "financial report") as these are the strongest signals.
3. **Suggest Actionable Adjustments**: Recommend signal weight deltas, domain lists, title patterns, and score thresholds to improve accuracy.
4. **Structured Output**: Respond ONLY with a valid JSON object matching the requested schema.
## Instructions
### 1. Review Current Configuration
Analyze the `CURRENT SCORING CONFIG` to understand the baseline `Score threshold`, `Positive keyword signals`, and `Negative keyword signals`.
### 2. Analyze Outcomes and Feedback
Examine the `TRIAGE OUTCOMES` (Total, True positive, False positive, Mismatch, Duplicate events) and the `CLOSURE COMMENTS FROM GITHUB`. Look for patterns that cause false positives or mismatches.
### 3. Apply Adjustment Rules
*   **signal_weight_deltas**: Only include signals that NEED changing.
*   **domain_blocklist**: Only add domains with 2+ false positives.
*   **domain_trustlist**: Only add domains with 2+ true positives.
*   **score_threshold_delta**: Clamp ±5; 0 if no change needed.
*   **title_patterns.reject**: Regex patterns seen across 2+ false positives.
*   **gemini_rejection_patterns**: Short phrases (3-6 words) that appear repeatedly in the title/snippet of false positive closures. These are fed to the Gemini pre-validator to reject similar candidates before heuristic scoring.
*   **validation_threshold**: Adjust only if similarity dedup is producing too many false "duplicate" suppressions (lower it) or too many actual dups pass through (raise it). Default is 0.75. Only adjust if there is clear evidence to do so.
*   **url_blocklist**: Add a URL only if it appears in 3+ false positive events AND is clearly a noise source (e.g. an aggregator mirror, a blog post, etc.).
*   Keep all arrays and objects present even if empty.
### 4. Format the Output
Respond ONLY with a valid JSON object matching this schema exactly. Do not include any markdown, explanation, or commentary outside the JSON:

```json
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
```
## Verification and Quality Assurance
1. **Valid JSON**: Ensure the output is a valid JSON object without surrounding markdown fences or text.
2. **Rule Adherence**: Verify all rules regarding minimum evidence (e.g., "2+ false positives") are met before adding to blocklists or adjusting weights.
3. **Completeness**: Ensure all arrays and objects are present in the JSON, even if empty.
---
# Triage Data Below

=== CURRENT SCORING CONFIG ===
Score threshold (min to create issue): {threshold}

Positive keyword signals (signal → score bonus):
{positive_signals}

Negative keyword signals (signal → score penalty, values already negative):
{negative_signals}

=== TRIAGE OUTCOMES ===
Total events : {total}
True positive: {tp_count}
False positive: {fp_count}
Mismatch     : {mm_count}
Duplicate    : {dup_count}

FALSE POSITIVE events (wrong/unrelated result — we want fewer of these):
{fp_events}

MISMATCH events (correct org, wrong year/edition/category):
{mm_events}

DUPLICATE events (already in repo or repeat discovery):
{dup_events}

TRUE POSITIVE events (valid finds — we want to keep these):
{tp_events}

=== CLOSURE COMMENTS FROM GITHUB ===
These are the actual comments left by reviewers when closing issues.
They provide richer context than just the outcome label:
{closure_comment_block}
