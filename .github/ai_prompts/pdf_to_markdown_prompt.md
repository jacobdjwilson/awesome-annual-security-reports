# AI Instruction Set for Converting Technical PDFs to Markdown
## Purpose
Ensure technical PDFs are converted to Markdown with complete fidelity, preserving all content, structure, and formatting.
## Goals
1. **Full Conversion**: Include all text, quotations, footnotes, references, and technical terminology without omission or summarization.  
2. **TOC Format**: Include a fully functional Table of Contents with proper linking.  
3. **Markdown Conventions**: Use clear, consistent, and professional formatting.  
4. **Images**: Describe image contents without embedding.
## Conversion Instructions
### Content
- **Include All Text**: Retain all sections, preserving the original structure and content.  
- **Headings**: Format with `#` for main headings, `##` and `###` for subheadings.  
- **Lists**: Use `1.` for ordered lists, `-` for unordered lists.  
- **Emphasis and Formatting**: Apply `_italic_`, `**bold**`, `>` for block quotes, and \`\`\` for code blocks.  
- **Links**: Format as `[text](URL)` and ensure accuracy.
### Images
- **Do Not Embed**: Replace with descriptive text: `![Image description]`.
### Table of Contents
- Place after the document title but before the main content:
  ## Table of Contents
  - [Section Title](#section-title)
  - [Subsection Title](#subsection-title)
- Ensure anchor links work and follow the format `(#section-title)`.
### Footnotes and References
- Use Markdown footnote syntax:  
  Content with a footnote[^1].  
  [^1]: Footnote content here.
- Retain all technical and academic terms exactly.
## Verification and Quality Assurance
1. **Accuracy**: Verify the entire document is converted without omissions.  
2. **TOC Functionality**: Check all links point to the correct headings.  
3. **Readability**: Ensure professional formatting and adherence to Markdown standards. DO NOT enclose the top and bottom of the content in ```markdown and ``` . 
4. **Fidelity**: Confirm the output matches the original PDF exactly.  
---
# Report Content Below
