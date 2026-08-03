# AI Instruction Set for Report Classification
## Purpose
Classify a security report into a `Category` from a provided list.
## Goals
1.  **Precise Categorization**: Assign the most relevant category from the dynamic list provided.
2.  **Structured Output**: Respond with a simple JSON object containing the category.
3.  **No Hallucination**: Only use categories from the provided list
## Instructions
### 1. Determine the Category
Select the single most appropriate category from the list below. Use the following hierarchy of logic to ensure precise categorization:
1.  **Specificity First**: If the report focuses on a specific attack type (e.g., **Ransomware**) or a specific domain (e.g., **Identity Security**, **Physical Security**), choose that specific category over broader ones.
2.  **Environment vs. Threat**: If a report focuses on the security *posture* of an environment, categorize by environment (e.g., **Cloud Security**, **Application Security**). If it focuses on *attacks* against that environment, prioritize the attack type if a specific category exists (e.g., **Ransomware**, **Data Breaches**).
3.  **General Fallbacks**: Only select **Threat Intelligence** (for Analysis) or **Industry Trends** (for Surveys) if the report covers a broad range of topics without a single dominant focus, or if it is a "State of the Union" style report.
4.  **Emerging Tech**: If the report specifically targets GenAI, LLMs, or deepfakes, prioritize **AI and Emerging Technologies**.
**Categories:**
{{CATEGORIES}}
### 2. Format the Output
Respond with a single, clean JSON object in the following format. Do not include any other text or explanations.
```json
{
  "category": "<Chosen Category>"
}
```
## Example Output
```json
{
  "category": "Cloud Security"
}
```
## Verification and Quality Assurance
1.  **Valid JSON**: Ensure the output is a valid JSON object.
2.  **Valid Category**: Ensure the `category` is one of the options provided in the `Categories` list.
---
# Report Content Below
