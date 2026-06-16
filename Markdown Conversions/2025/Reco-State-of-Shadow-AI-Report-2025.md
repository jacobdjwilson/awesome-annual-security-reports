# 2025 State of Shadow AI Report

## Table of Contents
- [Executive Summary: The Shadow AI Era Is Here](#executive-summary-the-shadow-ai-era-is-here)
- [Methodology](#methodology)
- [Glossary](#glossary)
- [Setting the Stage: Why We Should All Be Paying Attention to Shadow AI](#setting-the-stage-why-we-should-all-be-paying-attention-to-shadow-ai)
- [Our Findings](#our-findings)
  - [Finding 1 - 10 Shadow AI Apps Putting Your Data at Risk](#finding-1---10-shadow-ai-apps-putting-your-data-at-risk)
  - [Finding 2 - The Popularity Trap: High Adoption Doesn't Mean High Security](#finding-2---the-popularity-trap-high-adoption-doesnt-mean-high-security)
  - [Finding 3 - OpenAI Accounts for 53% of All Shadow AI Usage Across Enterprises](#finding-3---openai-accounts-for-53-of-all-shadow-ai-usage-across-enterprises)
  - [Finding 4 - Shadow AI Isn't Temporary: Uncovering Months of Unsanctioned AI Usage](#finding-4---shadow-ai-isnt-temporary-uncovering-months-of-unsanctioned-ai-usage)
  - [Finding 5 - Understaffed and Overexposed: 27% of Small Company Employees Use Shadow AI](#finding-5---understaffed-and-overexposed-27-of-small-company-employees-use-shadow-ai)
- [Recommendations for Security Leaders](#recommendations-for-security-leaders)
- [Leveraging Reco to Tackle Shadow AI](#leveraging-reco-to-tackle-shadow-ai)
- [Conclusion](#conclusion)

---

## Executive Summary: The Shadow AI Era Is Here

Security leaders face an unprecedented reality: Shadow AI has infiltrated nearly every corner of the enterprise, creating massive blind spots that traditional security approaches cannot address. Our in-depth analysis of shadow AI usage across our customer base reveals five critical findings that demand immediate action.

*   **The threat is real and it's massive.** We identified the 10 riskiest AI applications currently proliferating across our customer base, with security scores so low they should alarm any CISO. Three applications (Jivrus Technologies, Happytalk, and Stability AI) received failing grades meaning that they lack fundamental security controls like RBAC, MFA, and audit logging. These aren’t just any tools, they're processing corporate data daily.
*   **Mass adoption doesn't equal enterprise readiness.** The most widely adopted AI tools aren't the most secure. CreativeX and Otter.ai boast thousands of users despite security scores that should disqualify them from enterprise use. Organizations are choosing AI tools like they choose consumer apps: based on features and convenience, not security.
*   **The OpenAI monopoly.** OpenAI commands 53% of all shadow AI usage across the organizations we assessed, processing data from over 10,000 enterprise users in our study. This unprecedented concentration means half of all AI-related risk flows through a single platform. Any security incident, policy change, or service disruption at OpenAI could simultaneously impact the majority of enterprise AI workflows.
*   **Shadow AI runs deeper than most realize.** These tools do not disappear after the testing and experimentation ends. For example, some apps run unsanctioned for over 400 days on average. In our study, we found CreativeX and System.com to have the longest standing access on average. Once embedded in workflows for months, these applications become nearly impossible to remove without disrupting business operations and upsetting its users. Every day they persist, the security debt compounds.
*   **Smaller organizations face disproportionate risk.** The smaller the organization, the bigger the shadow AI problem. Companies with 11-50 employees show the highest risk concentration: 27% of their workforce uses unsanctioned AI tools. These organizations face the perfect storm: maximum AI adoption with minimum security resources to manage it.

**The bottom line:** Shadow AI is here, running loose across enterprises and invisible to traditional security tools. Smart security teams are implementing shadow AI discovery and governance solutions to turn this challenge into competitive advantage. The path forward is clear: AI adoption won't slow down because of security concerns. Security teams must get ahead of shadow AI now or face mounting risks and compliance challenges later.

---

## Methodology

Reco identified high-risk shadow AI applications through detailed analysis of anonymized, real-world usage data collected across its customer base. This comprehensive assessment included:

*   **Internal telemetry and SaaS audit logs:** Identifying unsanctioned AI apps actively used by employees.
*   **Evaluation across multiple security-relevant factors:**
    *   Total user count: Number of employees actively using each AI app
    *   Usage duration and frequency: Level and pattern of employee engagement with the app
    *   Registration type: Whether employees registered using corporate credentials or personal email accounts
    *   Authorization visibility: Assessment of whether apps integrated transparently via standard corporate channels or operated covertly
    *   Security policy compliance: Alignment with essential enterprise security controls, such as SSO, data retention policies, and encryption standards.
*   **Correlation of policy violations and risk signals:**
    *   Data Loss Prevention (DLP) and shadow AI discovery alerts
    *   Abnormal data flows or other suspicious activities linked to shadow AI app usage.

**Detailed Security Indicator Assessment**
Specific security indicators assessed included Encryption at Rest, Password Complexity, Auto-Renewal Subscription status, SSO Support, User Geo-Location Control, Content Security Policy (CSP), Audit Logs, Valid Certificate, Transport Security (HTTPS), 2FA Provisioning, Data Classification, Encryption Key Rotation, User Audit Logs, and Data Retention Policies. Each indicator was classified with clear statuses (Pass, Warn, or Fail), contributing to a composite risk score.

![Example of Reco risk assessment across 20 indicators]

By correlating these comprehensive indicators, Reco identified the shadow AI applications posing the greatest real-world risk. All findings reflect aggregated data across multiple Reco customers, ensuring an industry-wide perspective.

---

## Glossary

| Term | Definition |
| :--- | :--- |
| **Shadow AI** | Unsanctioned artificial intelligence applications adopted by employees without explicit IT or security approval. |
| **Generative AI (GenAI)** | AI models capable of creating original content—text, images, or code—from minimal prompts. |
| **AI Agent** | Autonomous or semi-autonomous AI systems integrated directly into enterprise software platforms, automating tasks with extensive user privileges. |
| **Model Context Protocol (MCP)** | An emerging protocol enabling real-time integration between AI models and enterprise data sources or tools. |
| **Prompt Injection** | A technique embedding malicious instructions into AI prompts to trigger unintended actions or data disclosures. |
| **OAuth Integrations** | Protocol allowing third-party applications secure access to enterprise systems without directly handling login credentials. |
| **Security Score** | A numerical rating (typically 0-100) evaluating an application's security posture based on factors like encryption, authentication mechanisms, compliance certifications, and data handling practices. |
| **Attack Surface** | The sum of all possible entry points where unauthorized users could access a system or extract data, expanded significantly by unsanctioned AI tool adoption. |
| **AI Sprawl** | A security model that requires continuous verification of identity and context for every user and device attempting to access resources, regardless of their location, to minimize risks from both internal and external threats. |

---

## Setting the Stage: Why We Should All Be Paying Attention to Shadow AI

Picture this: Your marketing team just connected an AI tool to your CRM to automate campaigns. Your engineers are debugging proprietary code through the latest AI coding assistant. And your HR team? They're processing sensitive employee data through an AI platform with a security score that would fail any basic audit.

Welcome to 2025, where AI transforms how every team works. The productivity gains are real. The innovation is undeniable. But so are the risks. Shadow AI has created a new security landscape where every employee's tool choice can open doors that security teams didn't even know existed (aka unknown unknowns).

### Why This Report Matters Now
This report is landing at the right time for a multitude of reasons. Enterprise AI adoption has introduced a lot of unknowns including shadow AI and how it impacts the traditional security paradigm. Hard data from IBM's Cost of a Data Breach Report 2025 confirms the financial risk, as breaches among organizations with high levels of shadow AI cost organizations an extra $670,000 USD.

Last month's EchoLeak vulnerability in Microsoft 365 Copilot (CVE-2025-32711, CVSS 9.3) delivered a wake-up call: even vetted, enterprise-grade AI tools can become attack vectors. Attackers could exfiltrate data from Outlook, SharePoint, and Teams with a single crafted email. Minimal user interaction required.

If that's what happens with AI that went through procurement, security review, and vendor assessments, imagine the vulnerabilities in the 100+ Shadow AI tools your employees are using right now.

### The Numbers Tell the Story
*   **38%** of employees admit to uploading sensitive data to AI tools (the real number is likely higher).
*   **71%** of knowledge workers use AI without IT approval.
*   **20%** of organizations studied in IBM's Cost of a Data Breach Report said they suffered a breach due to security incidents involving shadow AI.
*   **20%** of enterprises have experienced data leaks from shadow AI tools.

### Integration Risks
The risk multiplies with every new integration. ChatGPT's enterprise connectors to Box, HubSpot, and Google Drive are typically activated by individual users, not IT. Each connection expands the attack surface. Each integration creates new data flow paths that security teams can't monitor.

Emerging protocols like MCP allow AI models to interact directly with internal systems. While powerful for productivity, they create sophisticated attack vectors that traditional security tools weren't designed to detect.

### A Critical Distinction
Not all shadow AI is inherently insecure. "Shadow" simply means it's being used without IT or security approval. Some unsanctioned tools may have better security than approved alternatives. The risk comes from the lack of visibility and governance, not the tools themselves.

### The Speed of Adoption vs. The Pace of Security
AI tools are adopted in minutes but assessed in months, if they are ever discovered. By the time security teams complete a threat model, employees have already embedded these tools into critical workflows.

Getting shadow AI under control is not about stifling innovation. It's about preventing your intellectual property from becoming training data for the next public model, or your customer data from appearing in someone else's AI-generated content.

---

## Our Findings

### Finding 1 - 10 Shadow AI Apps Putting Your Data at Risk
Our analysis across our customer base revealed the top ten riskiest shadow AI apps currently proliferating across enterprises. We've ranked these applications by comprehensive security scores.

![Chart: Top 10 Most Dangerous Shadow AI Applications]

*   **Severe security failures (F-rated):** We identified three applications—Jivrus Technologies, Happytalk, and Stability AI—that received failing grades. Our assessment found that these applications operate without a combination of fundamental security controls:
    *   No encryption for data in transit or at rest
    *   Absence of multi-factor authentication or SSO integration
    *   Complete lack of audit logging capabilities
    *   No compliance certifications or security attestations
*   **High-risk applications (D-rated):** We discovered seven additional applications that pose significant threats with a D grade: HomeDesignsAI, agent.ai, RedactAI, Copy.ai, Clueify, CreativeX, and WaveAI. These lacked a combination of security controls including data retention policies, encryption implementation, access controls, and visibility into data processing.

---

### Finding 2 - The Popularity Trap: High Adoption Doesn't Mean High Security
Our analysis uncovered a dangerous misconception: the most popular AI tools aren't necessarily the most secure.

![Chart: Correlation Between Security Score and User Adoption]

*   **The high-risk favorites:** CreativeX and Otter.ai revealed a troubling pattern: sky-high adoption rates paired with security scores that should raise red flags.
*   **Hidden gems:** Applications like LegalMation and Gamma demonstrated the opposite phenomenon: excellent security scores coupled with minimal adoption.
*   **The security leaders:** OpenAI and Valence Chat Bot achieved the ideal combination: high adoption rates paired with strong security scores above 85.

**Recommendation:** Create and publish a pre-approved AI tools list. Guide employees to vetted alternatives before they adopt insecure apps.

---

### Finding 3 - OpenAI Accounts for 53% of All Shadow AI Usage Across Enterprises
Our analysis reveals an unprecedented concentration of risk: OpenAI alone accounts for 53% of all shadow AI usage across enterprises, with over 10,000 users tracked in our study.

![Chart: Top 10 Shadow AI Applications by User Count]

*   **Extreme market concentration:** OpenAI's usage dwarfs all competitors combined. This dominance means that any security incident, service disruption, or policy change at OpenAI could impact a substantial amount of enterprise AI workflows simultaneously.
*   **The shadow within the shadow:** While security teams scramble to address OpenAI risks, platforms like Perplexity AI, Valence Chat Bot, Blip, and Synthesia quietly expand their footprint.

**Recommendation:** Implement OpenAI-specific monitoring and controls. Create dedicated policies for OpenAI that include data classification requirements, approved use cases, and mandatory security training.

---

### Finding 4 - Shadow AI Isn't Temporary: Uncovering Months of Unsanctioned AI Usage
Our analysis of median usage duration uncovered a critical truth: shadow AI is sticky and tough to get rid of once adopted.

![Chart: Top 10 Shadow AI Applications by Median Usage Duration]

*   **Long-term exposure:** CreativeX and System.com lead with median usage durations exceeding one year (403 and 401 days respectively).
*   **Accumulating risk:** Each day of unsanctioned AI use compounds the potential damage. A tool used for 400 days has likely processed exponentially more sensitive data than one used for 40 days.

**Recommendation:** Conduct audits of any AI tool showing 60+ days of use in your environment. This duration indicates embedded usage that requires formal security assessment.

---

### Finding 5 - Understaffed and Overexposed: 27% of Small Company Employees Use Shadow AI
Our analysis uncovered a striking paradox: small-to-medium size businesses (SMBs) face disproportionately higher shadow AI exposure per capita than larger enterprises.

![Chart: Shadow AI Tools by Company Size]

*   **David v. Goliath:** Organizations with 11-50 employees show the highest concentration of shadow AI usage, averaging 269 tools per 1,000 employees.
*   **Mid-market challenges:** Companies with 501-1,000 employees maintain dangerous exposure levels at 200 shadow AI tools per 1,000 employees.

**Recommendation:** Focus your limited resources on the highest-risk AI categories first. Start by blocking or monitoring AI tools that access email, process customer data, or generate code.

---

## Recommendations for Security Leaders

To transform shadow AI from risk to opportunity, security leaders should focus on five core practices:

1.  **Implement Real-Time Shadow AI Discovery:** Deploy continuous discovery tools to identify all AI tools employees are using. You cannot secure what you cannot see.
2.  **Create and Publish Pre-Approved AI Tool Lists:** Get ahead of risky adoption by publishing vetted alternatives for common use cases.
3.  **Establish OpenAI-Specific Controls:** Implement specific policies covering data classification requirements, approved use cases, and mandatory security training for OpenAI.
4.  **Prioritize High-Risk Tool Remediation:** Focus immediate action on the F-rated tools. For tools showing 90+ days of usage, conduct formal security assessments within 30 days.
5.  **Monitor AI Agent and NHI Proliferation:** As AI agents become autonomous, they create new categories of non-human identities. Implement controls specifically for AI agents, including credential rotation and access reviews.

---

## Leveraging Reco to Tackle Shadow AI

At Reco, we've built our dynamic SaaS security platform specifically to address the shadow AI governance challenges outlined in this report. Our AI-based graph technology maps all SaaS applications, identities, and relationships across your enterprise.

### How We Discover Shadow AI
*   **Identity Provider Integration:** We sync with Entra ID/Okta to establish your approved application baseline.
*   **Email Metadata Analysis:** We scan Gmail/Outlook headers to detect unauthorized AI tool communications.
*   **Advanced NLP Matching:** We consolidate identities and accurately map them to AI applications.
*   **Real-Time Alerts:** We notify you instantly when new shadow AI tools are deployed.

### Real Customer Impact
*   **BigID:** Eliminated months of manual work using pre-built threat detections.
*   **Wellstar Health System:** Discovered over 1,100 SaaS applications in their environment.

---

## Conclusion

Shadow AI has fundamentally altered the enterprise security landscape. Our data reveals the reality: while security teams plan their next moves, employees have already deployed hundreds of AI tools, processing sensitive data through applications that would fail basic security audits.

The evidence is overwhelming: F-rated applications handle corporate data daily. OpenAI processes 53% of all AI activity. Small companies see 27% of their workforce using unsanctioned tools. These aren't anomalies.

The opportunity is now. Every day these tools become more embedded in workflows. Every integration expands the attack surface. Teams that implement discovery and governance now will outpace and out-innovate those who don’t. Every organization must decide whether to chase shadow AI incidents after they happen or get ahead with real governance. The tools exist. The data is definitive. Shadow AI isn't going away, but with the right approach, it doesn't have to stay in the shadows.

---
*This report presents analysis conducted by Reco and authored by The Cybersecurity Pulse, based on comprehensive shadow AI data from Reco's enterprise customer base.*