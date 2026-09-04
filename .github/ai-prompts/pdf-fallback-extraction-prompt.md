# AI Instruction Set for Direct PDF-to-Markdown Extraction
## Purpose
Directly inspect and convert an uploaded technical PDF document to clean, high-fidelity Markdown when local text extraction fails or produces empty/stub output.

## Goals
1. **Full Text and Layout Extraction**: Extract all body sections, tables, callouts, and technical findings directly from the PDF pages.
2. **Table Preservation**: Reconstruct data tables faithfully into GitHub Flavored Markdown table format.
3. **Structured Table of Contents**: Include a complete Table of Contents with valid Markdown anchor links.
4. **Zero Omission**: Do not summarize or truncate technical findings, statistics, or methodology sections.
5. **Clean Formatting**: Output clean Markdown without surrounding code block fences or conversational commentary.

## Extraction Instructions
### Content & Layout
- Reconstruct the document heading hierarchy starting with `# [Document Title]`, followed by `##` for main sections and `###` for sub-sections.
- Convert multi-column layouts into linear, sequential Markdown reading order.
- Format all tables using standard Markdown table syntax (`| Header 1 | Header 2 |`).
- Describe visual charts or architecture diagrams succinctly using `![Chart description]`. Do not attempt to embed binary images.
- Retain all footnotes, citations, and specialized cybersecurity terminology exactly as published.

### Table of Contents
- Place the Table of Contents immediately following the document title and metadata:
  ```markdown
  ## Table of Contents
  - [Executive Summary](#executive-summary)
  - [Key Findings](#key-findings)
  ```
- Ensure anchor links accurately reference lowercased, hyphenated section titles.

### Output Constraints
- DO NOT enclose the entire response in triple-backtick markdown fences (` ```markdown `). Return raw Markdown directly.
- DO NOT add conversational preambles or postscripts (e.g., "Here is the converted document:").

## Verification and Quality Assurance
1. **Completeness**: All pages, sections, and callouts from the PDF are fully transcribed without summarization.
2. **Table Fidelity**: Tables have consistent columns, headers, and cell values.
3. **Anchor Validity**: Table of Contents links match section headings.
4. **Accuracy**: Numerical metrics and statistics match the source PDF verbatim.
---
# Document Metadata Below
