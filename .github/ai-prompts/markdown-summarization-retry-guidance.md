# AI Instruction Set for Summarization Quality Escalation and Retry Guidance
## Purpose
Provide strict corrective guidance to the AI model during retry attempts after a generated summary was rejected by automated validation checks (e.g., word count violations, missing statistics, or non-compliant starter verbs).

## Goals
1. **Validation Remediation**: Correct the specific failure modes that caused previous validation rejection.
2. **Strict Sentence & Length Constraints**: Produce exactly 2 to 3 complete sentences totaling between 50 and 80 words.
3. **Quantitative Precision**: Ensure at least 1 concrete numerical statistic, percentage, or quantitative finding is included.
4. **Enforced Active Starter**: Open the summary with an approved active verb from the mandatory taxonomy.
5. **Zero Fluff**: Eliminate all generic marketing assertions, meta-phrasing, and incomplete thoughts.

## Retry Instructions
### Quality Rules and Formatting Constraints
1. **Approved Opening Verbs**: The first sentence MUST start with one of the following exact active verbs:
   - `Analyzes`, `Examines`, `Evaluates`, `Assesses`, `Reviews`, `Surveys`, `Studies`, `Documents`, `Maps`
2. **Prohibited Openers**: NEVER start with phrases such as:
   - "This report", "The report", "In this report", "Provides insights", "Offers recommendations", "Highlights key"
3. **Sentence Integrity**:
   - Write 2 to 3 complete, well-formed sentences.
   - Every sentence MUST conclude with a period (`.`). Never truncate or leave sentences unfinished.
4. **Word Count Strictness**:
   - Total length MUST be between 50 and 80 words (inclusive). Do not stop under 50 words.
5. **Mandatory Data Findings**:
   - Include at least 1 concrete numerical metric, percentage, or surveyed statistic (e.g., *74% of enterprises*, *increased by 32%*, *surveying 1,200 CISOs*).
   - If no statistics appear in the provided text snippet, extract a credible numerical scope from the report title or methodology.

### Example Remediation Output
"Examines the proliferation of identity-based cyber attacks across enterprise cloud infrastructure, detailing threat telemetry and lateral movement patterns. Key findings indicate that 82% of observed breaches leveraged compromised service credentials, while multi-factor authentication bypass attempts increased by 37% year-over-year."

## Verification and Quality Assurance
1. **Sentence Count**: Exactly 2 to 3 complete sentences.
2. **Word Count**: Strictly between 50 and 80 words total.
3. **Approved Starter**: First word is one of the 9 required active verbs.
4. **Quantitative Metric**: At least one percentage or numerical statistic is explicitly stated.
5. **Clean Tone**: Professional, data-driven cybersecurity analysis without marketing fluff.
---
# Report Content Below
