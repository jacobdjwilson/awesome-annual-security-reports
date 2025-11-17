name: 💡 Suggest a New Report
description: Found an annual security report that should be on the list? Let us know here!
title: "Suggest Report: [Organization Name] - [Report Name]"
labels: ["new report", "contribution"]
body:
  - type: markdown
    attributes:
      value: |
        Thank you for contributing! Please provide a direct link to the report's landing page or PDF.
        
        Our automated pipeline will process the report once it's been reviewed and added by a maintainer.

  - type: input
    id: report_url
    attributes:
      label: Report URL
      description: "Please paste the full URL (e.g., https://www.example.com/2025-threat-report.pdf)"
      placeholder: "https://..."
    validations:
      required: true

  - type: textarea
    id: comments
    attributes:
      label: Additional Comments
      description: "Is there anything else we should know about this report? (e.g., key findings, specific focus)"