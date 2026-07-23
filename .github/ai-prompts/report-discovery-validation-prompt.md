# AI Instruction Set for Validating Discovery Candidates
## Purpose
Validate candidate documents found by an automated security report discovery pipeline to ensure they are annual (or recurring) cybersecurity reports and not duplicates.
## Goals
1. **Validate Relevance**: Ensure the candidate is a cybersecurity report and not a financial report, webinar, blog, or product guide.
2. **Verify Recurrence**: Confirm the report is an annual or recurring publication.
3. **Detect Duplicates**: Determine if the same edition (same org + same year) already exists in the repository.
4. **Structured Output**: Respond ONLY with a valid JSON object matching the requested schema.
## Instructions
### 1. Evaluate the Candidate
Review the candidate's organization, target year, title/snippet, and URL.
### 2. Check for Duplicates
Compare the candidate's year with the `Existing reports already in this repository for this organization`.
### 3. Apply Decision Rules
*   **ACCEPT**: If the report is annual/recurring, covers a cybersecurity topic, and is NOT a duplicate of an existing year.
*   **REJECT**: If the report is not annual/recurring, not cybersecurity, a financial/investor report, webinar, blog, product guide, or is a duplicate.
*   **UNCERTAIN**: If there is not enough information to be sure.
*   **is_duplicate**: Set to `true` if the same edition (same org + same year) appears to already be in the repo.
### 4. Format the Output
Answer ONLY with a JSON object — no markdown, no explanation outside the JSON:
```json
{{
  "verdict": "ACCEPT" | "REJECT" | "UNCERTAIN",
  "reason": "<one concise sentence>",
  "is_annual": true | false,
  "is_security_topic": true | false,
  "is_duplicate": true | false
}}
```
## Verification and Quality Assurance
1. **Valid JSON**: Ensure the output is a valid JSON object without surrounding markdown fences or text.
2. **Strict Adherence to Rules**: Double-check the decision against the ACCEPT/REJECT/UNCERTAIN conditions.
---
# Candidate Context Below
Candidate:
- Organization: {org}
- Target year: {year}
- Title / snippet: {text}
- URL: {url}

Existing reports already in this repository for this organization:
{existing_years}
