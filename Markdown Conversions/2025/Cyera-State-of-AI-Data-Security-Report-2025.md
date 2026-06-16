# 2025 State of AI Data Security Report

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Survey Findings](#key-survey-findings)
- [01 AI Deployment Outpaces Control](#01-ai-deployment-outpaces-control)
- [02 Agents and Prompts: The Exposed Edge](#02-agents-and-prompts-the-exposed-edge)
- [03 The Identity Gap in AI Governance](#03-the-identity-gap-in-ai-governance)
- [Best Practices for Securing Enterprise AI](#best-practices-for-securing-enterprise-ai)
- [Conclusion](#conclusion)
- [Methodology & Demographics](#methodology--demographics)

---

## Executive Summary
Artificial Intelligence (AI) has crossed the tipping point. 83% of enterprises already use AI in daily operations, yet only 13% report strong visibility into how it is being used. The result is a widening gap: sensitive data is leaking into AI systems beyond enterprise control, autonomous agents are acting beyond scope, and regulators are moving faster than enterprises can adapt. AI is now both a driver of productivity and one of the fastest-expanding risk surfaces CISOs must defend.

This report, based on a comprehensive survey of 921 IT and cybersecurity professionals, sets out to answer a critical question: as AI becomes embedded in the enterprise, are CISOs equipped to govern it with the same rigor applied to users, systems, and data? The findings reveal a clear tension: AI adoption has gone mainstream, but visibility, monitoring, and access frameworks remain shallow and fragmented. Left unchecked, AI functions as a shadow identity—powerful, fast, and often unaccountable.

## Key Survey Findings
- **AI adoption without oversight**: 83% already use AI, yet only 13% have strong visibility, leaving most enterprises blind to how AI interacts with their data.
- **Agents are the new shadow risk**: 76% say autonomous AI agents are the hardest to secure, with 70% pointing to external prompts.
- **AI as a shadow identity**: Only 16% treat AI as a distinct identity, while two-thirds have caught AI over-accessing data.
- **Controls lag reality**: Nearly a quarter have no prompt or output controls, and only 11% can automatically block risky AI activity.
- **Governance gaps persist**: Only 7% have a dedicated AI governance team, and just 11% feel fully prepared for regulation.

The chapters that follow examine these findings across three themes: how AI deployment is outpacing control, why agents and prompts create new exposures, and why identity and access management must be redefined for AI.

---

## 01 AI Deployment Outpaces Control
AI has become nearly universal in the enterprise, but adoption has surged faster than the guardrails needed to manage it. Organizations are embedding AI into daily workflows, yet most lack visibility, monitoring, or the ability to enforce controls, leaving a governance gap that regulators are beginning to notice.

### AI Deployments Create Systemic Risk Exposure
![Chart showing AI usage: 55% pilot/limited, 28% extensive, 11% plan to use, 4% no plans]

While 83% of enterprises already use AI in some capacity, most remain in shallow stages. The AI model footprint is highly concentrated, with 79% relying on ChatGPT/OpenAI, 57% on Microsoft Copilot, and 41% on Google Gemini. 

OWASP’s 2025 guidance reinforces this reality: early adoption without oversight maps directly to **LLM02 Sensitive Information Disclosure** and **LLM10 Unbounded Consumption**.

### Blind Spots Define AI Risk
![Chart showing visibility levels: 10% good, 3% full, 42% minimal, 33% some, 7% no visibility]

Over 8 out of 10 enterprises use AI, yet only 13% report robust visibility. Oversight remains reactive: a third of enterprises review AI activity logs only after incidents, while just 9% monitor in real time.

### Controls Lag Behind Reality
![Chart showing ability to block risky AI: 11% fully automated, 29% manual, 33% awareness but no controls, 15% no capability, 9% planning]

57% of enterprises lack the ability to block or restrict risky AI activities. OWASP classifies these exposures as **LLM01 Prompt Injection**, **LLM02 Sensitive Information Disclosure**, and **LLM06 Excessive Agency**.

### Governance Without Readiness
Only 11% of organizations consider themselves fully prepared for regulatory requirements. Ownership is fragmented: 34% say ownership is shared, 17% place it with the CIO, and only 12% with the CISO.

---

## 02 Agents and Prompts: The Exposed Edge
While organizations are more comfortable with embedded AI inside trusted SaaS platforms, their confidence collapses once autonomy or external prompts come into play.

### Agents and Prompts Are the Pain Point
![Chart showing hardest to secure: 76% autonomous agents, 70% external prompts, 43% embedded SaaS AI]

Four in ten organizations report the presence of unsanctioned or “shadow AI” operating outside approval and oversight.

### Guardrails Missing at the Prompt Layer
![Chart showing controls: 41% filtering/blocking, 38% audit trails, 30% runtime monitoring, 26% output redaction, 23% none]

Nearly a quarter (23%) have no prompt or output controls in place at all. OWASP identifies this gap as central to **LLM01 Prompt Injection** and **LLM02 Sensitive Information Disclosure**, compounded by **LLM05 Improper Output Handling**.

---

## 03 The Identity Gap in AI Governance
Identity and access management remains the cornerstone of enterprise security, but most organizations are still applying human-centric models to AI.

### AI Still Lacks Its Own Identity
Only 16% of respondents treat AI as a distinct identity class. 77% do not consistently treat AI as a distinct identity class, either blurring it with human users or applying inconsistent rules.

### Over-Access Is Built Into AI
Two-thirds of organizations have already caught AI tools accessing more data than necessary. 21% grant AI broad access to sensitive data by default.

### Data and Identity Are Siloed
85% of organizations have not fully integrated their data security and identity governance for AI use. Only 9% report that these controls are fully integrated.

---

## Best Practices for Securing Enterprise AI
1. **Build Visibility from the First Pilot**: Treat every pilot as production. Implement continuous discovery, real-time logging, and anomaly detection.
2. **Contain Agents and Prompts**: Narrow agent scopes, require approvals, and default to prompt/output filtering.
3. **Redefine Identity for AI**: Treat AI as a first-class identity with least-privilege and classification-driven access.

---

## Conclusion
The evidence is clear: AI adoption has outpaced data governance, and AI risks are scaling faster than data defenses. CISOs who act now can use AI as an advantage to the business, while those who wait will inherit AI as an unmanaged liability.

---

## Methodology & Demographics
This 2025 State of AI Data Security Report is based on a survey of 921 IT and cybersecurity professionals. The survey has a margin of error of ±3.2% at a 95% confidence level.

- **Primary Job Functions**: IT Operations/Infrastructure (21%), Network Security (18%), Analyst/SOC (16%), VP/Director of Security (13%), Security Architect (7%), CISO (7%), DevSecOps (18%).
- **Company Size**: Ranging from <499 employees (12%) to >10,000 employees (23%).
- **Industry**: Financial Services (24%), Technology/Software (22%), Healthcare (18%), Government (10%), Manufacturing (8%), Energy (6%), Other (12%).

---

**Rights Notice**
©2025 Cybersecurity Insiders. All rights reserved. Limited editorial citation permitted with clear attribution to “Cybersecurity Insiders, 2025 State of AI Data Security Report” and a visible link to https://cybersecurity-insiders.com. No redistribution, derivatives, scraping, or AI/ML training.