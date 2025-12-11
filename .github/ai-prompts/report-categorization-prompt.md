# AI Instruction Set for Report Analysis
## Purpose
Analyze a security report to determine its `Report Type`, `Category`, and generate a `Summary`.
## Goals
1.  **Accurate Typing**: Correctly determine if the report is an `Analysis Report` or a `Survey Report`.
2.  **Precise Categorization**: Assign the most relevant category from the provided list.
3.  **Concise Summarization**: Generate a 1-2 sentence summary of the key findings, under 400 characters.
4.  **Structured Output**: Respond with a single JSON object containing the type, category, and summary.
## Instructions
### 1. Determine the Report Type
*   **Survey Report**: If findings are based on feedback, interviews, or survey responses, classify as `Survey`.
*   **Analysis Report**: If findings are based on technical data (network traffic, incident response, sensor data), classify as `Analysis`.
### 2. Determine the Category
Select the single most appropriate category from the list below, prioritizing specificity.
**Categories:**
{{CATEGORIES}}
### 3. Generate a Summary
Create a professional, concise summary (1-2 sentences, under 400 characters) that captures the report's key findings, threats, or insights.
### 4. Format the Output
Respond with a single, clean JSON object. Do not include any other text or explanations.
```json
{
  "type": "<Analysis or Survey>",
  "category": "<Chosen Category>",
  "summary": "<A concise 1-2 sentence summary under 400 characters>"
}
```
## Example Output
```json
{
  "type": "Analysis",
  "category": "Cloud Security",
  "summary": "The report highlights a 70% increase in cloud misconfigurations leading to data breaches, primarily driven by a lack of skilled personnel and immature IAM practices."
}
```
## Verification and Quality Assurance
1.  **Valid JSON**: Ensure the output is a valid JSON object.
2.  **Correct Fields**: Verify `type`, `category`, and `summary` are all present.
3.  **Valid Category**: Ensure `category` is one of the provided options.
4.  **Summary Length**: Ensure `summary` is under the 400-character limit.
---
# Report Content Below
