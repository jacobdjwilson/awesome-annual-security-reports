# State of AI Data Security Report 2025

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Survey Findings](#key-survey-findings)
- [01 AI Deployment Outpaces Control](#01-ai-deployment-outpaces-control)
- [AI Deployments Create Systemic Risk Exposure](#ai-deployments-create-systemic-risk-exposure)
- [Blind Spots Define AI Risk](#blind-spots-define-ai-risk)
- [Controls Lag Behind Reality](#controls-lag-behind-reality)
- [Governance Without Readiness](#governance-without-readiness)
- [02 Agents and Prompts: The Exposed Edge](#02-agents-and-prompts-the-exposed-edge)
- [Agents and Prompts Are the Pain Point](#agents-and-prompts-are-the-pain-point)
- [Guardrails Missing at the Prompt Layer](#guardrails-missing-at-the-prompt-layer)
- [03 The Identity Gap in AI Governance](#03-the-identity-gap-in-ai-governance)
- [AI Still Lacks Its Own Identity](#ai-still-lacks-its-own-identity)
- [Over-Access Is Built Into AI](#over-access-is-built-into-ai)
- [Data and Identity Are Siloed](#data-and-identity-are-siloed)
- [Best Practices for Securing Enterprise AI](#best-practices-for-securing-enterprise-ai)
- [Conclusion](#conclusion)
- [Methodology & Demographics](#methodology--demographics)

---

## Executive Summary

Artificial Intelligence (AI) has crossed the tipping point. 83% of enterprises already use AI in daily operations, yet only 13% report strong visibility into how it is being used. The result is a widening gap: sensitive data is leaking into AI systems beyond enterprise control, autonomous agents are acting beyond scope, and regulators are moving faster than enterprises can adapt. AI is now both a driver of productivity and one of the fastest-expanding risk surfaces CISOs must defend.

This report, based on a comprehensive survey of 921 IT and cybersecurity professionals, sets out to answer a critical question: as AI becomes embedded in the enterprise, are CISOs equipped to govern it with the same rigor applied to users, systems, and data? The findings reveal a clear tension: AI adoption has gone mainstream, but visibility, monitoring, and access frameworks remain shallow and fragmented. Left unchecked, AI functions as a shadow identity—powerful, fast, and often unaccountable.

## Key Survey Findings

- **AI adoption without oversight**: 83% already use AI, yet only 13% have strong visibility, leaving most enterprises blind to how AI interacts with their data.
- **Controls lag reality**: Nearly a quarter have no prompt or output controls, and only 11% can automatically block risky AI activity.
- **Agents are the new shadow risk**: 76% say autonomous AI agents are the hardest to secure, with 70% pointing to external prompts.
- **Governance gaps persist**: Only 7% have a dedicated AI governance team, and just 11% feel fully prepared for regulation.
- **AI as a shadow identity**: Only 16% treat AI as a distinct identity, while two-thirds have caught AI over-accessing data.

The chapters that follow examine these findings across three themes: how AI deployment is outpacing control, why agents and prompts create new exposures, and why identity and access management must be redefined for AI.

To guide the response, each chapter connects survey data with the OWASP Top 10 for LLM Applications—the leading community framework for AI security risks such as prompt injection, excessive agency, and unbounded consumption. By aligning enterprise experience with OWASP’s categories, this report offers CISOs not only evidence of the gaps but also a practical roadmap for closing them.

---

## 01 AI Deployment Outpaces Control

AI has become nearly universal in the enterprise, but adoption has surged faster than the guardrails needed to manage it. Organizations are embedding AI into daily workflows, yet most lack visibility, monitoring, or the ability to enforce controls, leaving a governance gap that regulators are beginning to notice.

- 83% of organizations already use AI, yet the majority (57%) remain in early maturity stages.
- Only 13% report good or full visibility into AI usage; nearly half admit they have little to no visibility.
- Logs are treated more as forensics than defense: a third of organizations review them only after incidents.
- Only 11% can automatically block risky AI activity; one-third acknowledge awareness without controls.
- Governance lags behind adoption, with only 7% having a dedicated AI governance team and 11% fully prepared to meet regulatory requirements.

Together these findings confirm a simple truth: the enterprise risk surface created by AI is expanding far faster than the governance and enforcement structures meant to contain it.

### AI Deployments Create Systemic Risk Exposure

While 83% of enterprises already use AI in some capacity, most remain in shallow stages: more than half are limited to pilots (55%) and only 28% report extensive adoption. Maturity lags even further, with the largest share describing themselves as only “emerging” (39%).

The AI model footprint is highly concentrated. Nearly four in five rely on ChatGPT or OpenAI (79%), while Microsoft Copilot (57%) and Google Gemini (41%) follow close behind. The most common uses are content and knowledge generation (75%) and productivity and collaboration (71%), which may appear routine, yet they already touch the very operational data that defines how enterprises run.

![Chart showing AI usage: 83% Yes, 55% in pilot/limited, 28% extensively, 11% no but planning, 4% no plans.]

OWASP’s 2025 guidance reinforces this reality: early adoption without oversight maps directly to LLM02 Sensitive Information Disclosure and LLM10 Unbounded Consumption. Continuous discovery of AI tools, classification of the data they touch, and real-time logging of prompts and outputs must begin at the pilot stage. Without these controls, enterprises risk compounding governance debt as adoption spreads.

### Blind Spots Define AI Risk

Over 8 out of 10 enterprises use AI, yet only 13% report robust visibility into how it is being used. Nearly half admit to have no or low visibility. The result is that most CISOs cannot reliably answer where and how AI is operating inside their own organizations. Oversight remains reactive: a third of enterprises review AI activity logs only after incidents, while just 9% monitor in real time. Only 14% detect anomalous or rogue AI behavior as it happens, and more than one in five do not monitor at all.

![Chart showing visibility levels: 49% have little to no visibility, 42% minimal, 33% some, 10% good, 3% full.]

OWASP guidance aligns directly with this risk: insufficient monitoring fuels LLM02 Sensitive Information Disclosure, while post-incident log review leaves organizations vulnerable to LLM08 Vector and Embedding Weaknesses and LLM10 Unbounded Consumption. Continuous discovery, real-time logging, and anomaly detection are essential if visibility is to move from hindsight to defense.

### Controls Lag Behind Reality

Even when organizations recognize AI risk, enforcement is weak. Only 11% have automated blocking in place, while 29% rely on manual intervention. A third (33%) admit they have awareness without controls, 9% are planning to add blocking capabilities, and 15% say they cannot block misuse at all. In other words, more than half of enterprises are powerless to stop risky AI activity in real time.

![Chart showing ability to block risky AI: 57% lack ability, 11% fully automated, 29% manual, 33% awareness but no controls, 15% no capability, 9% planning.]

OWASP classifies these exposures as LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, and LLM06 Excessive Agency—a reminder that what CISOs see as operational problems are already codified as systemic risks. Automated blocking, kill switches, and rate limits must be designed-in from the start, otherwise enterprises remain one crafted prompt away from exposure.

### Governance Without Readiness

AI adoption is racing ahead, but the organizational structures to govern it are still catching up. Only 11% of organizations consider themselves fully prepared for regulatory requirements tied to AI data governance. Nearly half (44%) admit they are only partially prepared, while another 31% are aware of obligations but are unprepared.

Ownership of AI governance is equally fragmented. Just 7% report having a dedicated AI governance committee. For most, responsibility is distributed: 34% say ownership is shared, 17% place it with the CIO, and only 12% see it with the CISO.

![Chart showing regulatory readiness: 11% fully prepared, 44% partially, 31% aware but unprepared, 8% not yet aware, 6% not a priority.]

OWASP guidance makes the stakes clear: lack of clear ownership leaves enterprises exposed to LLM02 Sensitive Information Disclosure and LLM06 Excessive Agency, while shallow readiness invites compliance failure under LLM10 Unbounded Consumption.

---

## 02 Agents and Prompts: The Exposed Edge

While organizations are more comfortable with embedded AI inside trusted SaaS platforms, their confidence collapses once autonomy or external prompts come into play. Autonomous agents and public LLM prompts now define the riskiest parts of the enterprise AI surface.

- 76% say autonomous AI agents are the hardest to secure, and 70% name external prompts to public LLMs as equally high risk.
- 40% acknowledge shadow AI is already present.
- 21% grant AI broad access to sensitive data by default, and 66% have already caught AI over-accessing information.

### Agents and Prompts Are the Pain Point

Not all AI interactions carry equal risk. Three-quarters (76%) of organizations say autonomous agents are the hardest to secure, followed closely by external prompts to public LLMs at 70%. By contrast, embedded SaaS AI is flagged as difficult by only 43%.

![Chart showing hardest AI interactions to secure: 76% autonomous agents, 70% external prompts, 43% embedded SaaS, 29% API-based, 24% internal/open-source.]

OWASP maps these exposures directly: LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, and LLM06 Excessive Agency all converge when unsupervised agents and external prompts are in play.

### Guardrails Missing at the Prompt Layer

Prompts and outputs are the choke points where sensitive data most often slips into or out of AI systems, yet most organizations admit they lack meaningful safeguards. Nearly a quarter (23%) have no prompt or output controls in place at all.

![Chart showing controls in place: 41% filtering/blocking, 38% audit trails, 30% runtime monitoring, 26% output redaction, 23% none.]

OWASP identifies this gap as central to LLM01 Prompt Injection and LLM02 Sensitive Information Disclosure, compounded by LLM05 Improper Output Handling.

---

## 03 The Identity Gap in AI Governance

Identity and access management remains the cornerstone of enterprise security, but most organizations are still applying human-centric models to AI.

- Only 16% treat AI as a distinct identity class.
- 21% grant AI broad access to sensitive data by default.
- Only 9% say data security and identity controls are fully integrated for AI.

### AI Still Lacks Its Own Identity

Only 16% of respondents treat AI as a distinct identity class in their access control and monitoring systems. The majority blur the lines, either treating AI like any user (35%) or applying inconsistent rules (42%).

![Chart showing AI identity differentiation: 16% distinct class, 42% sometimes, 35% treated like any user, 7% not sure.]

OWASP guidance ties this gap to LLM06 Excessive Agency and LLM02 Sensitive Information Disclosure. Treating AI as a first-class identity is essential.

### Over-Access Is Built Into AI

One in five organizations (21%) admit their AI systems are granted broad access to sensitive data from the start. Two-thirds of organizations have already caught AI tools accessing more data than necessary.

![Chart showing AI over-access: 25% frequently, 41% occasionally, 13% no/monitoring in place, 16% not monitoring.]

### Data and Identity Are Siloed

Only 9% report that their data security and identity governance are fully integrated for AI use. 39% admit the two operate separately and 16% say they are not integrated at all.

![Chart showing integration of data security and identity: 9% fully integrated, 30% partially, 39% separate, 16% not integrated.]

---

## Best Practices for Securing Enterprise AI

1. **Build Visibility from the First Pilot**: Treat every pilot as production. The fix is continuous discovery, real-time logging, and anomaly detection from day one.
2. **Contain Agents and Prompts**: Narrow agent scopes, require approvals, and default to prompt/output filtering.
3. **Redefine Identity for AI**: Treat AI as a first-class identity with least-privilege and classification-driven access.

## Conclusion

The evidence is clear: AI adoption has outpaced data governance, and AI risks are scaling faster than data defenses. The readiness gap is real and will continue to widen. CISOs who act now can use AI as an advantage to the business. Those who wait will inherit AI as an unmanaged liability.

---

## Methodology & Demographics

This 2025 State of AI Data Security Report is based on a survey of 921 IT and cybersecurity professionals. The survey has a margin of error of ±3.2% at a 95% confidence level.

- **Primary Job Function**: IT Operations (21%), Security Analyst (18%), VP/Director of Security (18%), Security Architect (16%), CISO (13%), DevSecOps (7%), Other (7%).
- **Company Size**: <499 (12%), 500-999 (17%), 1,000-4,999 (27%), 5,000-9,999 (21%), >10,000 (23%).
- **Industry**: Financial Services (24%), Technology (22%), Healthcare (18%), Government (10%), Manufacturing (8%), Energy (6%), Other (12%).

*©2025 Cybersecurity Insiders. All Rights Reserved.*