# AI Instruction Set for Report Classification
## Purpose
Classify a security report into a `Report Type` (Analysis or Survey) and a `Category` from a provided list.
## Goals
1.  **Accurate Typing**: Correctly determine if the report is an `Analysis Report` or a `Survey Report` based on its methodology.
2.  **Precise Categorization**: Assign the most relevant category from the dynamic list provided.
3.  **Structured Output**: Respond with a simple JSON object containing the type and category.
## Instructions
### 1. Determine the Report Type
Review the report content to identify its methodology:
*   **Survey Report**: If the report's findings are primarily based on collecting feedback, interviews, or survey responses from individuals or organizations, classify it as `Survey`.
*   **Analysis Report**: If the report's findings are primarily based on data collected from technical sources like sensor networks, endpoint data, consulting engagements, incident responses, or network traffic analysis, classify it as `Analysis`.
### 2. Determine the Category
Select the single most appropriate category from the list below. Use the following hierarchy of logic to ensure precise categorization:
1.  **Specificity First**: If the report focuses on a specific attack type (e.g., **Ransomware**) or a specific domain (e.g., **Identity Security**, **Physical Security**), choose that specific category over broader ones.
2.  **Environment vs. Threat**: If a report focuses on the security *posture* of an environment, categorize by environment (e.g., **Cloud Security**, **Application Security**). If it focuses on *attacks* against that environment, prioritize the attack type if a specific category exists (e.g., **Ransomware**, **Data Breaches**).
3.  **General Fallbacks**: Only select **Threat Intelligence** (for Analysis) or **Industry Trends** (for Surveys) if the report covers a broad range of topics without a single dominant focus, or if it is a "State of the Union" style report.
4.  **Emerging Tech**: If the report specifically targets GenAI, LLMs, or deepfakes, prioritize **AI and Emerging Technologies**.
**Categories:**
{{CATEGORIES}}
### 3. Format the Output
Respond with a single, clean JSON object in the following format. Do not include any other text or explanations.
```json
{
  "type": "<Analysis or Survey>",
  "category": "<Chosen Category>"
}
```
## Example Output
```json
{
  "type": "Analysis",
  "category": "Cloud Security"
}
```
## Verification and Quality Assurance
1.  **Valid JSON**: Ensure the output is a valid JSON object.
2.  **Correct Type**: Verify the `type` is either `Analysis` or `Survey`.
3.  **Valid Category**: Ensure the `category` is one of the options provided in the `Categories` list.
---
# Report Content Below
