# Agent Coding Standards and Security Guidelines

When working on this repository, you must adhere to the following strict guidelines:

## 1. Workflow Architecture and Script Coding Standards
- **Do not embed scripts in workflows.** All GitHub Actions workflows must reference external scripts (e.g., in `.github/scripts/`) rather than embedding inline script logic. This ensures extensibility, reusability, testability, and automated linting.
- **Single Responsibility.** Each script in `.github/scripts/` must fulfill a focused operational step in the CI/CD pipeline.
- **Standardized Script Architecture.** All Python scripts in `.github/scripts/` must adhere to a consistent, modular structural approach:
  1. **Header & Docstring**: Declare the operational purpose, required environment variables, outputs, and JSON artifact dependencies.
  2. **Imports**: Group imports cleanly: Standard Library -> Third-party -> Typing.
  3. **Configuration Loader**: Encapsulate configuration retrieval within a dedicated loader (`ConfigLoader` class or `load_config()` function) that strictly loads from `.github/artifacts/` with fail-fast validation.
  4. **Domain Logic**: Implement testable, modular functions and classes with type hints and comprehensive error handling.
  5. **Standardized Process Entrypoint**: Execute under `if __name__ == "__main__":` and exit cleanly using standard exit codes:
     - `0`: Success.
     - `1`: General or operational failure with actionable diagnostic logs.
     - Documented specialized codes (e.g., `EXIT_QUOTA_EXHAUSTED = 2` for pipeline retry control).

## 2. Configuration and Artifact Standards
- **No Hardcoded Values.** Scripts must never hardcode configuration values, thresholds, retry counts, time delays, model names, prompt paths, label names, or operational settings.
- **Use JSON Artifacts.** All configuration must be loaded from JSON artifacts located in `.github/artifacts/` (e.g., `workflow-config.json`, `ai-models.json`, `report-categories.json`, `discovery-feedback.json`, `readme-updater-config.json`, `google-search-config.json`).
- **Standardized Artifact Architecture.** All JSON artifacts in `.github/artifacts/` must adhere to uniform structural principles:
  1. **Self-Documenting Schema**: Include `_comment` or `comment` attributes on complex sections or thresholds explaining operational rationale.
  2. **Semantic Hierarchy**: Organize settings into logical sub-objects by pipeline task or domain (e.g., `workflow.discovery`, `workflow.conversion`, `configurations.<task>`, `task_models.<task>`).
  3. **Explicit Numeric Units**: Encode time, sizes, and counts explicitly in key names (e.g., `_seconds`, `_mb`, `_days`, `_bytes`, `_multiplier`, `_limit`).
  4. **POSIX Path Conventions**: All file and prompt paths referenced within artifacts must use forward slashes (e.g. `.github/ai-prompts/foo.md`) for seamless cross-platform execution.
- **Fail Fast on Missing Config.** If a required JSON artifact or configuration key is missing or invalid, scripts must raise an explicit exception (`ValueError`, `FileNotFoundError`, or `KeyError`) with descriptive remediation advice. Never fall back to unversioned, hardcoded default literals in script source code.

## 3. AI Prompts and Instruction Sets
- **Extract all prompts.** Any AI calls that rely on a prompt, instruction set, schema description, retry guidance, or fallback instructions must never define prompt text inline within code.
- **Use Markdown for Prompts.** All prompt text must be extracted into standalone `.md` files in `.github/ai-prompts/`.
- **Dynamic Prompt Paths.** Prompt filepaths must be declared in `workflow-config.json` and loaded dynamically by scripts at runtime.
- **Standardized Prompt Architecture.** All prompt markdown files in `.github/ai-prompts/` must adhere strictly to the repository's standardized instruction set structure:
  1. `# AI Instruction Set for <Task Name>` (H1 Title)
  2. `## Purpose` (Concise operational intent of the AI step)
  3. `## Goals` (Numbered list of specific objectives and non-functional constraints)
  4. `## Instructions` / `## Conversion Instructions` / `## Extraction Instructions` / `## Retry Instructions` (Detailed operational rules, negative constraints, and output formatting)
  5. `### Example Output` (Representative demonstration showing expected output structure where applicable)
  6. `## Verification and Quality Assurance` (Numbered checklist of criteria for model validation)
  7. **Runtime Sentinel**: A horizontal rule (`---`) followed by a terminal delimiter line (e.g. `# Report Content Below`, `# Document Metadata Below`, or `# Candidate Context Below`) where dynamic execution context is appended at runtime.

## 4. Model Tiering and Fallback Hierarchy
- **Task-Based Routing.** AI operations must load model configurations from `.github/artifacts/ai-models.json` via `task_models`, routing complex tasks (such as document layout parsing in PDF conversions) to capable models (e.g., `gemini-3.8-flash`) while lightweight tasks (categorization, discovery validation) route to high-throughput models (e.g., `gemini-3.5-flash-lite`).
- **Fallback Chains.** Scripts making AI calls must support fallback ladders (`primary` -> `secondary` -> `tertiary`) loaded from `ai-models.json`.
- **Quota Error Handling.** Quota exhaustion (HTTP 429 / `RESOURCE_EXHAUSTED`) must be differentiated from transient errors. Scripts must respect API-supplied retry delays when provided, and otherwise apply `quota_retry_policy` backoff curves from `ai-models.json`.

## 5. Automation Safeguards and Concurrency Gating
- **Enforce Operational Caps.** Automated workflows must query and enforce pipeline caps before initiating processing:
  - `max_open_automated_prs` from `workflow-config.json` prevents automated PR accumulation.
  - `max_open_automated_issues` from `workflow-config.json` limits open discovery triage suggestions.
- **PR Branch Deduplication.** Workflows that generate conversions or updates must check existing open PR branches before processing files to prevent duplicate PR creation and git merge conflicts.
- **Gating Between Pipelines.** Dependent pipelines must verify the status of prerequisite workflow runs (checking `workflow.gating` configuration) before modifying shared assets.

## 6. Repository Data Integrity and Formatting Standards
- **README Entry Format.** All entries added to `README.md` must adhere strictly to:
  `- [Organization](WebsiteURL) - [Title](PDFPath) (Year) - Summary`
  - `WebsiteURL` must be the organization's landing page or full report landing page, never truncated to a bare top-level domain.
  - `Summary` must be 50–80 words, start with an approved active verb (e.g., *Analyzes*, *Examines*, *Evaluates*, *Assesses*, *Reviews*, *Surveys*, *Studies*, *Documents*, *Maps*), and include at least one concrete numerical metric or percentage.
- **Conversion Metadata.** All generated Markdown conversions must append a trailing `<!-- CONVERSION_METADATA: {"source": "...", "date": "YYYY-MM-DD", "model": "..."} -->` block to preserve provenance and facilitate automated staleness detection.

## 7. Agent Operational Security and Workspace Hygiene
- **Public Rules, Private State.** `AGENTS.md` is public and maintained at the repository root to declare development standards transparently.
- **Keep `.agents/` Ignored.** The `.agents/` directory is reserved for local agent working information, conversation transcripts, IDE telemetry, and scratch artifacts. It must ALWAYS be listed in `.gitignore` and never committed to version control.
- **No Secret Leaks.** Scripts and agent interactions must never log, commit, or persist API secrets (e.g., `GEMINI_API_KEY`, `GH_TOKEN`, `VT_API_KEY`).
