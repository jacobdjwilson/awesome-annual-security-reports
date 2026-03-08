# 2025 State of Shadow AI Report

## Table of Contents
- [Executive Summary: The Shadow AI Era Is Here](#executive-summary-the-shadow-ai-era-is-here)
- [Methodology](#methodology)
- [Glossary](#glossary)
- [Setting the Stage: Why We Should All Be Paying Attention to Shadow AI](#setting-the-stage-why-we-should-all-be-paying-attention-to-shadow-ai)
- [Our Findings](#our-findings)
    - [Finding 1: 10 Shadow AI Apps Putting Your Data at Risk](#finding-1-10-shadow-ai-apps-putting-your-data-at-risk)
    - [Finding 2: The Popularity Trap: High Adoption Doesn't Mean High Security](#finding-2-the-popularity-trap-high-adoption-doesnt-mean-high-security)
    - [Finding 3: OpenAI Accounts for 53% of All Shadow AI Usage Across Enterprises](#finding-3-openai-accounts-for-53-of-all-shadow-ai-usage-across-enterprises)
    - [Finding 4: Shadow AI Isn't Temporary: Uncovering Months of Unsanctioned AI Usage](#finding-4-shadow-ai-isnt-temporary-uncovering-months-of-unsanctioned-ai-usage)
    - [Finding 5: Understaffed and Overexposed: 27% of Small Company Employees Use Shadow AI](#finding-5-understaffed-and-overexposed-27-of-small-company-employees-use-shadow-ai)
- [Recommendations for Security Leaders](#recommendations-for-security-leaders)
- [Leveraging Reco to Tackle Shadow AI](#leveraging-reco-to-tackle-shadow-ai)
- [Conclusion](#conclusion)

---

## Executive Summary: The Shadow AI Era Is Here

Security leaders face an unprecedented reality: Shadow AI has infiltrated nearly every corner of the enterprise, creating massive blind spots that traditional security approaches cannot address. Our in-depth analysis of shadow AI usage across our customer base reveals five critical findings that demand immediate action.

*   **Shadow AI runs deeper than most realize.** These tools do not disappear after the testing and experimentation ends. For example, some apps run unsanctioned for over 400 days on average. Once embedded in workflows for months, these applications become nearly impossible to remove without disrupting business operations.
*   **Smaller organizations face disproportionate risk.** The smaller the organization, the bigger the shadow AI problem. Companies with 11-50 employees show the highest risk concentration: 27% of their workforce uses unsanctioned AI tools.
*   **The threat is real and it's massive.** We identified the 10 riskiest AI applications currently proliferating across our customer base. Three applications (Jivrus Technologies, Happytalk, and Stability AI) received failing grades, meaning they lack fundamental security controls like RBAC, MFA, and audit logging.
*   **Mass adoption doesn't equal enterprise readiness.** The most widely adopted AI tools aren't the most secure. CreativeX and Otter.ai boast thousands of users despite security scores that should disqualify them from enterprise use.
*   **The OpenAI monopoly.** OpenAI commands 53% of all shadow AI usage across the organizations we assessed. Any security incident, policy change, or service disruption at OpenAI could simultaneously impact the majority of enterprise AI workflows.

## Methodology

Reco identified high-risk shadow AI applications through detailed analysis of anonymized, real-world usage data. This assessment included:

- **Internal telemetry and SaaS audit logs**: Identifying unsanctioned AI apps actively used by employees.
- **Evaluation across multiple security-relevant factors**: Total user count, usage duration, registration type, authorization visibility, and security policy compliance.
- **Correlation of policy violations and risk signals**: Data Loss Prevention (DLP) alerts and abnormal data flows.

![Example of Reco's 20-indicator risk assessment chart]

## Glossary

- **Shadow AI**: Unsanctioned artificial intelligence applications adopted by employees without explicit IT or security approval.
- **Generative AI (GenAI)**: AI models capable of creating original content—text, images, or code—from minimal prompts.
- **AI Agent**: Autonomous or semi-autonomous AI systems integrated directly into enterprise software platforms.
- **Model Context Protocol (MCP)**: An emerging protocol enabling real-time integration between AI models and enterprise data sources.
- **Prompt Injection**: A technique embedding malicious instructions into AI prompts to trigger unintended actions.
- **OAuth Integrations**: Protocol allowing third-party applications secure access to enterprise systems without directly handling login credentials.
- **Security Score**: A numerical rating (0-100) evaluating an application's security posture.
- **Attack Surface**: The sum of all possible entry points where unauthorized users could access a system.
- **AI Sprawl**: The rapid, unmanaged proliferation of AI tools across an organization.

## Setting the Stage: Why We Should All Be Paying Attention to Shadow AI

Welcome to 2025, where AI transforms how every team works. The productivity gains are real, but so are the risks. Shadow AI has created a new security landscape where every employee's tool choice can open doors that security teams didn't even know existed.

Hard data from IBM's *Cost of a Data Breach Report 2025* confirms the financial risk, as breaches among organizations with high levels of shadow AI cost organizations an extra $670,000 USD.

### The Numbers Tell the Story
- **38%** of employees admit to uploading sensitive data to AI tools.
- **71%** of knowledge workers use AI without IT approval.
- **20%** of enterprises have experienced data leaks from shadow AI tools.
- **20%** of organizations suffered a breach due to security incidents involving shadow AI.

## Our Findings

### Finding 1: 10 Shadow AI Apps Putting Your Data at Risk
We identified the top ten riskiest shadow AI apps. 
- **Severe security failures (F-rated)**: Jivrus Technologies, Happytalk, and Stability AI. These lack encryption, MFA/SSO, and audit logging.
- **High-risk applications (D-rated)**: HomeDesignsAI, agent.ai, RedactAI, Copy.ai, Clueify, CreativeX, and WaveAI.

![Chart showing the Top 10 Most Dangerous Shadow AI Applications]

### Finding 2: The Popularity Trap: High Adoption Doesn't Mean High Security
Our analysis uncovered a dangerous misconception: the most popular AI tools aren't necessarily the most secure. CreativeX and Otter.ai show high adoption rates paired with low security scores. Conversely, tools like LegalMation and Gamma show excellent security scores but minimal adoption.

### Finding 3: OpenAI Accounts for 53% of All Shadow AI Usage Across Enterprises
OpenAI processes more corporate data than the next nine platforms combined. With 10,000+ enterprise users, this concentration creates a single point of failure for enterprise AI workflows.

### Finding 4: Shadow AI Isn't Temporary: Uncovering Months of Unsanctioned AI Usage
Shadow AI is "sticky." CreativeX and System.com lead with median usage durations exceeding one year (403 and 401 days respectively). Once employees find an AI solution that works, they rarely seek alternatives, even if more secure options exist.

### Finding 5: Understaffed and Overexposed: 27% of Small Company Employees Use Shadow AI
Organizations with 11-50 employees show the highest concentration of shadow AI usage, averaging 269 tools per 1,000 employees. These organizations face the perfect storm: maximum AI adoption with minimum security resources to manage it.

## Recommendations for Security Leaders

1. **Implement Real-Time Shadow AI Discovery**: Deploy continuous discovery tools to identify all AI tools, including web apps and browser extensions.
2. **Establish OpenAI-Specific Controls**: Implement dedicated policies for OpenAI, including data classification and mandatory training.
3. **Create and Publish Pre-Approved AI Tool Lists**: Guide employees to vetted alternatives before they adopt insecure apps.
4. **Prioritize High-Risk Tool Remediation**: Focus immediate action on F-rated tools and those with 90+ days of usage.
5. **Scale Security for Smaller Teams**: Use a "default deny" approach and whitelist 3-5 essential AI tools.

## Leveraging Reco to Tackle Shadow AI

Reco provides a dynamic SaaS security platform that maps all SaaS applications, identities, and relationships. 
- **Discovery**: Syncs with Entra ID/Okta, scans email metadata, and uses advanced NLP matching.
- **Real-Time Alerts**: Notifies security teams instantly when new shadow AI tools are deployed.
- **Vendor Risk Score**: Prioritizes dangerous applications and provides remediation paths.

## Conclusion

Shadow AI has fundamentally altered the enterprise security landscape. The employees creating these risks are driving unprecedented productivity gains; they are not reckless, they are resourceful. Any security strategy that ignores this reality will fail. Teams that implement discovery and governance now will outpace and out-innovate those who don’t.

---
*This report presents analysis conducted by Reco and authored by The Cybersecurity Pulse, based on comprehensive shadow AI data from Reco's enterprise customer base.*