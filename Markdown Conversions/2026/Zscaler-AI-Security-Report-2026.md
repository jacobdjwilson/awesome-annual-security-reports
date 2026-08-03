# ThreatLabz 2026 AI Security Report

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [AI/ML Usage Trends](#aiml-usage-trends)
- [Enterprise AI Risks and Threat Landscape](#enterprise-ai-risks-and-threat-landscape)
  - [Case study: GenAI-enhanced malware and social engineering in DPRK-linked campaigns](#case-study-genai-enhanced-malware-and-social-engineering-in-dprk-linked-campaigns)
  - [Case study: Emerging AI indicators in campaign targeting the South Asia region](#case-study-emerging-ai-indicators-in-campaign-targeting-the-south-asia-region)
  - [Case study: What’s really breaking in enterprise AI systems](#case-study-whats-really-breaking-in-enterprise-ai-systems)
- [The Latest Phase of AI Governance](#the-latest-phase-of-ai-governance)
- [AI Security Predictions for 2026](#ai-security-predictions-for-2026)
- [Best Practices: Secure Enterprise AI Adoption](#best-practices-secure-enterprise-ai-adoption)
- [How Zscaler Delivers Comprehensive AI Protection](#how-zscaler-delivers-comprehensive-ai-protection)
- [Research Methodology](#research-methodology)
- [About ThreatLabz](#about-threatlabz)

Organization: Zscaler
Report Title: AI-Security-Report
Year: 2026

---

## Executive Summary_

The daily reality of AI in 2025 was defined by speed, scale, and constant motion. 

Enterprises now rely on artificial intelligence and machine learning (AI/ML) across the business to move faster, automate decisions, and increase productivity. AI supports development, communications, research, and operations at a pace that would have seemed unrealistic just a few years ago. But this acceleration has also come with more and more tradeoffs: more sensitive data flows through more AI/ML applications, often with less visibility and fewer guardrails.

That expanding AI footprint has widened the enterprise attack surface, and threat actors were quick to follow over the past year. Lower barriers and higher realism have made attacks faster and more convincing, while early signs of agentic and semi-autonomous AI misuse pointed to a shift in how threats are evolving. At the same time, organizations are contending with a growing mix of risks—from shadow and embedded AI to hallucinations and unsecured private models. In 2026, securing AI is about more than controlling AI/ML applications. It’s about securing how AI is discovered, built, used, and governed across the enterprise. Organizations need visibility into AI usage and risk, protections that harden AI systems and data in real time, and consistent controls that secure access while keeping innovation moving. This report delves into the trends and realities shaping AI security, and provides guidance for enterprises looking to reduce risk and adopt AI safely.

Correction (February 2026): The year-over-year percentage change in AI/ML transaction volume has been updated to reflect a revised calculation.

### What This Means for Enterprise Leaders
- **AI is now enterprise infrastructure.** Nearly one trillion AI transactions signal continuous, always-on operations. AI must be governed with the same rigor as cloud, identity, and data to support safe and scalable adoption.
- **Data exposure risk now scales with volume, not intent.** Petabyte-scale data movement through AI workflows increases exposure through repetition and speed, even when usage is approved and aligned with business intent.
- **Approved AI is the primary risk surface.** Mainstream, sanctioned AI tools account for the majority of enterprise AI activity and data interactions. While shadow AI remains a key concern, addressing unauthorized tools alone will not mitigate the full scope of AI-related risks and exposure.
- **Security is constraining AI adoption.** With 39% of AI transactions blocked, policy enforcement is actively shaping how AI is used. This reflects governance in action, not resistance to AI as leaders balance the tradeoff between innovation speed and risk tolerance.
- **Traditional security models are misaligned with AI workflows.** Controls designed for human-paced activity and static data cannot keep up with machine-driven, high-frequency AI interactions.
- **Competitive advantage will favor organizations that can govern AI at scale.** Enterprises that enable broad AI use with strong, inline controls will move faster than those forced to fully restrict usage due to unmanaged risk.

---

## Key_
Findings

ThreatLabz analyzed 989.3 billion AI and ML transactions in the Zscaler cloud from January 2025–December 2025. The key findings that follow are based on data spanning varying time periods* for comparative analysis.

- **Enterprise AI usage continues its strong upward trajectory.** AI/ML activity increased 83% year-over-year, reaching nearly one trillion transactions across an ecosystem of more than 3,400 applications.
- **Enterprises send increasingly large volumes of data to AI tools.** A total of 18,033 TB of data was transferred to AI/ML applications, a 93% year-over-year rise.
- **High block rates signal ongoing risk management.** Enterprises blocked 39% of overall AI/ML transactions, underscoring continued concerns about data exposure, privacy, and policy enforcement as AI usage expands.
- **Enterprise AI is wide open to compromise.** Zscaler red teaming experts found most enterprise AI systems can be breached in just 16 minutes, and uncovered critical flaws in 100% of systems tested.
- **OpenAI dominates as the top LLM vendor.** OpenAI accounted for the vast majority of LLM-driven enterprise transactions (3x more than Codeium), establishing it as the current de facto LLM.
- **ChatGPT accounts for the overwhelming majority of DLP violations.** Across all AI/ML applications analyzed, ChatGPT generated 410 million data loss prevention (DLP) policy violations, affirming enterprise risks tied to high-context AI assistants.
- **Integrated productivity apps anchor enterprise AI usage.** Grammarly became the #1 application by transaction volume, reflecting reliance on AI that operates directly within communication and business processes.
- **Finance & Insurance and Manufacturing lead enterprise AI usage again.** For the third year in a row, these sectors represented the largest share of AI/ML traffic (23% and 20%, respectively) behind their modernization efforts and heavy documentation workflows.
- **The United States remained the primary source of AI/ML transactions.** Activity was concentrated in the U.S., which accounted for 38% of transactions, followed by India (14%) and Canada (5%).
- **AI adoption continues to expand the enterprise attack surface.** Broader use of AI across enterprise workflows has created more paths for data and access to be exposed, increasing the likelihood of data leakage, prompt misuse, and AI-assisted attacks—reinforcing the need for zero trust architecture and AI-powered security controls.

*\* Data collection periods:*
- *Annual and year-over-year analysis: January–December 2025, with year-over-year comparisons against the same period in 2024.*
- *DLP violations data and country-level data: June 2025–December 2025.*

---

## AI/ML_
Usage Trends

Enterprise use of AI continued its steep and steady climb in 2025. ThreatLabz analysis of AI usage trends now includes more than 3,400 applications driving AI/ML transactions—four times more than the previous year. While many of these apps generate limited traffic, the sheer growth in the application ecosystem itself is a meaningful indicator. It reflects just how quickly AI capabilities are proliferating across vendors, use cases, and business functions, expanding both opportunity and exposure.

To understand how this growth translates into real-world enterprise usage, ThreatLabz analyzed AI/ML activity across several layers:
- Overall AI/ML transactions, based on URL category, including both allowed and blocked activity.
- LLM vendor rankings, identifying which model providers generate the most AI/ML traffic and power enterprise AI workflows.
- Top AI/ML applications, highlighting the specific apps driving enterprise AI activity and traffic volume.
- Departmental AI usage, mapping high-volume AI applications to common enterprise departments to understand where AI is being applied in day-to-day work.

### Global growth in AI/ML transactions
AI/ML transactions approached the trillion mark in 2025, totaling 989.3 billion. Much of this growth is tied to high-volume applications such as ChatGPT, Grammarly, and Codeium.

*Figure 1: Year-over-year comparison of AI/ML transactions (January–December 2025)*
> **KEY FINDING**  
> AI/ML activity increased 83% year-over-year across an ecosystem of more than 3,400 applications.

As in previous years, a share of the traffic falls under “General AI Applications.” This reflects AI/ML transactions that don’t map to a specific known application, but are identified as AI-related by Zscaler’s AI/ML-powered URL categorization, which analyzes text, images, and other content signals to recognize AI-related activity. New AI applications emerge faster than they can be manually classified, making it essential to detect previously unknown sources of AI traffic and bring them under security policy enforcement.

Unless otherwise noted, subsequent analysis in this report focused exclusively on classified applications. This approach gives us visibility into AI adoption through established AI/ML applications.

- **Classified AI Applications (e.g., Grammarly and ChatGPT):** 66.8%
- **General Browsing:** 33.2%

*Figure 2: Distribution of AI/ML transactions across general and classified AI applications*

### Top LLM vendors, applications, and departments
Looking at enterprise AI usage through LLM vendors offers a unique view of how AI is operating at scale. While employees interact daily with individual applications and features, transaction patterns show which model providers consistently sit underneath those experiences. Vendor-level visibility is a useful way to understand how AI adoption is taking shape beneath the surface.

#### Key LLM vendor findings
- **OpenAI** was the clear leader among LLM vendors in 2025, accounting for 131 billion transactions, more than three times the volume of its nearest competitor. The release of GPT-5 in August expanded adoption across coding, multimodal reasoning, and complex task execution. OpenAI’s expanded Enterprise API options, including stronger privacy and model isolation, also reinforced its role as the backend for copilots and AI-enabled SaaS features.
- **Codeium** (rebranded as Windsurf in 2025) emerged as the second-largest source of enterprise LLM traffic (42 billion transactions). Adoption was likely driven by its coding-focused proprietary models, which appear frequently in software development pipelines and engineering environments. This mirrors the departmental analysis that follows, where engineering stands out as the most active AI user.
- **Perplexity** took the third position by transaction volume last year (12 billion transactions). Beyond AI-powered search, it also operates proprietary LLMs that power its answer engine. Accordingly, enterprise usage reflects growing dependence on AI-assisted research and knowledge synthesis.

Transaction volume remains highly concentrated among a set of widely adopted applications that sit directly in the flow of work—researching, editing, writing, coding, translating, and collaborating.

#### Key application findings
- **Grammarly** emerged as the most active AI/ML application in enterprise environments (38.7% of total transactions), overtaking ChatGPT in total transaction volume. With features ranging from summarization to advanced rewriting and tone guidance, it’s easy to see why Grammarly is prominent in everyday enterprise content workflows.
- **ChatGPT** remained a dominant general purpose assistant (14.2%), used broadly across roles for research, drafting, and analysis, making it a common touchpoint for enterprise data.
- **Codeium** entered the top five (5%), showing how AI has become a regular part of software development work where source code and proprietary logic are routinely processed.
- **DeepL** continued to see strong adoption in global organizations (3.3%), supporting multilingual communication across business-critical content.
- **Microsoft Copilot** rounded out the top five (3%), driven by its deep integration into Microsoft 365 and its role in automating daily productivity tasks.

| Application | Total Transactions |
| --- | --- |
| Grammarly | 327,311,080,013 |
| ChatGPT | 120,227,890,252 |
| Codeium | 42,337,652,986 |
| DeepL | 27,847,680,087 |
| Microsoft Copilot | 25,503,137,940 |
| Perplexity | 12,386,054,978 |
| GitHub Copilot | 11,348,420,722 |
| OpenAI | 10,352,420,115 |
| QuillBot | 8,913,115,535 |
| ChurnZero | 8,153,526,358 |
| Anthropic | 4,922,983,385 |
| Glean | 4,542,501,122 |
| GliaCloud | 3,249,239,347 |
| Claude | 2,850,954,278 |
| Google Gemini | 2,604,461,019 |
| SundaySky | 2,483,835,170 |
| Yellow Messenger | 1,734,555,650 |
| Cresta | 1,585,454,178 |
| Poe | 1,483,703,558 |

*Figure 4: Percentage of total AI/ML transactions driven by leading AI applications*

#### Share of Transactions by Department
Looking beyond which AI applications dominate overall usage, the next layer of analysis shifts from tools to teams. ThreatLabz mapped AI/ML traffic across a defined set of common enterprise departments to better understand how AI is being used in practice. This view focuses on applications with substantial usage (at least one million transactions) and associates them with the department in which they are most often used. The percentage shares shown reflect relative usage within this scoped set of departments and applications, rather than total enterprise AI traffic.

- **Engineering:** 48.9%
- **IT:** 31.8%
- **Marketing:** 6.9%
- **Customer Support:** 6.7%
- **General:** 3.7%
- **HR:** 0.7%
- **Legal:** 0.5%
- **Sales:** 0.4%
- **Finance:** 0.3%

*Figure 5: Share of AI/ML transactions by core enterprise departments*

### Blocked transactions
Organizations also tightened the reins on enterprise AI in 2025. Data exposure, privacy, and compliance concerns pushed them to block 39.2% of total AI/ML transactions, reinforcing AI governance as a standard part of daily security operations.

#### Top Blocked AI Applications
1. Grammarly
2. GitHub Copilot
3. ChatGPT
4. Microsoft Copilot
5. QuillBot
6. Codeium
7. DeepL
8. Tabnine
9. Poe
10. Perplexity

### Data transferred to AI applications
Transaction volume alone doesn’t fully capture how enterprises are using AI. To add context, ThreatLabz also examined the amount of data transferred between enterprise environments and AI/ML applications.

Over the past year, enterprise data transfer to AI/ML applications continued to rise, reaching 18,033 terabytes (TB)—a 93% increase year-over-year. Grammarly remained the top application by this measure, with 3615 TB of data transferred. Close behind was ChatGPT (2021 TB), followed by OpenAI (865 TB), DeepL (625 TB), and Codeium (387 TB)—applications that span use cases that typically handle high-value enterprise data.

> **KEY FINDING**  
> A total of 18,033 TB of data was transferred to AI/ML applications—a 93% year-over-year increase.

*Figure 6: Top AI/ML applications by the percentage of total data transferred*

### Data loss to AI applications
AI’s ability to accelerate work from idea to output in minutes comes with a high-stakes tradeoff: sensitive data can be shared with external models in seconds. What’s more, with embedded AI features inside common SaaS applications and services, content is often transmitted automatically, increasing the likelihood of unnoticed exposure. Preventing data loss to external models has become one of the most important security priorities of the year.

In the Zscaler cloud, AI-related DLP policy violations continue to be one of the clearest signals of this growing risk. These violations occur when sensitive information such as financial records, personally identifiable information (PII), source code, healthcare data, and other regulated content attempts to leave the organization through an AI application and is stopped by policy. Without Zscaler’s AI-aware DLP in place, that data would have been exposed to third-party models outside the enterprise’s control.

#### AI/ML Applications with the Most DLP Policy Violations
| Application | DLP Violations Count |
| --- | --- |
| ChatGPT | 410,181,006 |
| Codeium | 242,263,311 |
| GitHub Copilot | 31,223,009 |
| Claude | 14,417,246 |
| Wordtune | 5,161,758 |
| DeepL | 2,037,613 |
| QuillBot | 1,960,391 |
| Microsoft Copilot | 1,858,952 |
| Perplexity | 1,235,129 |
| Google Gemini | 841,374 |

*ChatGPT DLP violations increased 99.3% year-over-year. The most common violations specific to ChatGPT included name leakage and national identifiers—possibly customer records or identity details.*

*Enterprise DLP violations tied to Codeium increased 100% year-over-year, suggesting increased leakage risk for source code and proprietary logic.*

#### Top 10 AI DLP Policy Violations
1. Name leakage
2. Social Security number (US)
3. Company Number (Japan)
4. National Health Service Number (UK)
5. Source code
6. Medicare Number (Australia)
7. National Provider Identifier Number (US)
8. Social Insurance Number (Canada)
9. Medical information
10. Credit card information

### The rise of embedded AI
Not all enterprise AI usage shows up in standalone generative AI tools. More and more, it’s happening through embedded AI—features built into everyday applications that aren’t classified as GenAI apps, such as summaries, recommendations, or automated insights that invoke AI only at certain moments. These capabilities often feel like natural and expected upgrades to tools users already use. That’s also what makes it easy to overlook the fact that embedded AI also interacts with enterprise data without the same visibility or guardrails as standalone AI applications, making it a quieter but an increasingly important dimension of securing AI adoption. As a result, embedded AI represents one of the fastest growing and least visible sources of enterprise AI risk.

#### Oversharing Driven by Inherited Permissions
Embedded AI typically relies on existing access controls and content permissions. If an organization has broad access by default, outdated group memberships, or overshared collaboration spaces, embedded AI can unintentionally surface sensitive information to users who technically have access but do not need the information for their role. In practice, this can turn long-standing permission sprawl into faster and more visible data exposure.

#### Models and Connector Supply Chain Exposure
Embedded AI features frequently rely on multiple components. These can include model providers, retrieval layers that pull content from enterprise systems, and connectors that integrate across SaaS applications and data repositories. Each component can introduce new trust boundaries and new change vectors. As features evolve, the risk profile can shift through updates, configuration changes, or newly enabled integrations.

#### Indirect Prompt Manipulation Through Business Content
Embedded AI often reads enterprise content such as emails, tickets, documentation, chat logs, and attachments as part of normal operation. This introduces risk where hidden instructions or adversarial content can influence how the AI responds, what it prioritizes, or how it presents information. When AI features are tightly integrated into workflows, the content itself can become a delivery channel for manipulation.

#### Action and Automation Risks in AI-Enabled Workflows
As AI features move beyond summarization and drafting into task execution, the risk surface expands. If an AI capability can trigger actions, recommend changes, generate code, or populate records, errors or manipulated outputs can become operational issues. Even without direct action execution, AI-generated outputs can influence decisions and downstream workflows in ways that are difficult to audit.

#### Real-World Embedded AI Exploits Enable Easy Data Exfiltration
Two widely reported exploit examples in the Copilot ecosystem illustrate how low user interaction can still result in high embedded AI risk:
- **EchoLeak** is described as a zero-click prompt injection style vulnerability in Microsoft 365 Copilot that could enable data exfiltration via normal email ingestion patterns.
- **Reprompt** is a reported single-click attack that used crafted prompts via URL parameters to trigger unwanted behavior and data leakage.

### AI/ML usage by industry
AI adoption ramped up across every industry in 2025, with all sectors accounted for in the Zscaler cloud showing year-over-year increases in AI/ML activity. But the pace and maturity of adoption varies widely. In some sectors, it’s already doing real work. In others, it’s still finding its place.

Finance & Insurance organizations account for the largest share (23.3%) of AI/ML traffic for the second year in a row. Manufacturing maintained its second place position at 19.5% of total AI/ML transactions, which can be attributed to its investment in AI-driven automation, quality control, supply chain optimization, and more. Technology & Communication and Education saw the highest year-over-year increases.

#### Share of Blocked AI Transactions by Vertical
| Vertical | % of AI Transactions Blocked |
| --- | --- |
| Finance & Insurance | 39.1% |
| Manufacturing | 22.1% |
| Services | 13.5% |
| Healthcare | 8.5% |
| Technology & Communication | 6.8% |
| Government | 4.0% |
| Others | 3.4% |
| Retail & Wholesale | 2.0% |
| Education | 0.6% |

#### Industry Spotlight: Finance & Insurance remains the most AI-driven sector: 230B transactions
The Finance & Insurance sector was the biggest driver of AI activity in the Zscaler cloud in AI/ML, making up nearly one-quarter of all enterprise use. Much of this volume comes from everyday productivity tools. Grammarly, ChatGPT, and Microsoft Copilot were the most-used AI apps across banks and insurance companies for the second year in a row. At the same time, the sector is far from carefree in how it uses these tools. Finance & Insurance also blocked over 39.1% of AI/ML transactions in the Zscaler cloud—a sign of heightened sensitivity to data loss risk, regulatory scrutiny, and the need to tightly govern model interactions with sensitive financial information.

#### Industry Spotlight: Technology sees the fastest growth in enterprise AI use: +202% YoY
The Technology sector posted the highest year-over-year increase in AI/ML transactions in 2025 (202.3%), outpacing every other industry in the Zscaler cloud. Leading productivity assistants are heavily used across Technology organizations, powering everything from code generation and technical documentation to marketing content. Accordingly, Grammarly, Codeium, ChatGPT, and Perplexity were among the top AI apps behind Technology sector traffic during our analysis.

#### Industry Spotlight: Education shows quiet but explosive growth in AI adoption: +184% YoY
The Education sector accounted for only a small share of total AI/ML transactions in the Zscaler cloud in 2025, but its rate of growth told a different story. Education generated nearly 16 billion AI/ML transactions over the year, posting the second-highest year-over-year increase in AI/ML activity at 184.4%. Notably, this surge occurred with very limited friction. Fewer than 1% of AI/ML transactions in Education were blocked, suggesting that most usage is either explicitly permitted or occurring in environments where governance and guardrails are still emerging.

### AI/ML usage by country
The geographic distribution of AI/ML activity remained broadly consistent in 2025, with subtle shifts at the margins. AI is firmly established in the United States, and the country continues to claim the largest share of AI/ML traffic volume, but AI usage grew significantly across several international markets.

Although the U.S. continued to lead in absolute usage (218.9 billion AI/ML transactions, accounting for 37.6% of global activity), AI adoption expanded faster year-over-year elsewhere. That global acceleration is most evident in India, which was the second-largest source of enterprise AI activity, reaching 82.3 billion transactions—a 309.9% year-over-year increase.

#### Top Countries by Volume and Share
| Country | % Share | AI/ML Transactions |
| --- | --- | --- |
| United States | 37.6% | 219B |
| India | 14.1% | 82B |
| Canada | 4.7% | 27B |
| United Kingdom | 4.3% | 25B |
| Japan | 3.2% | 19B |
| Germany | 2.7% | 16B |
| Australia | 2.6% | 15B |
| France | 2.4% | 14B |
| China | 2.0% | 12B |
| Brazil | 1.8% | 11B |

#### Regional Snapshot: EMEA
AI/ML activity across the EMEA region remained concentrated among a small number of mature European markets. The United Kingdom, Germany, France, and Spain accounted for nearly half of regional transactions. The UK leads the region with 20.3% of AI/ML traffic between June–December 2025, followed by Germany (12.5%) and France (11.0%).

#### Regional Snapshot: APAC
AI/ML usage across the Asia-Pacific (APAC) region was shaped by a pronounced imbalance between a single high-growth market and several more established economies. India, Japan, and Australia together comprised the majority of regional AI/ML transactions, with India alone driving nearly half of all activity—46.2% of regional AI/ML traffic.

---

## Enterprise AI Risks and Threat Landscape

As our research proves, AI is threaded through every layer of the enterprise, from public GenAI tools to internal LLMs and AI-enabled SaaS suites. Organizations must manage a broader and more complex attack surface as usage grows. The most significant risks fall into the following categories.

- **Data exposure and sensitive information leakage:** AI systems see some of the most sensitive data in the enterprise—source code, customer records, financial details, and legal documents—often without clear security guardrails.
- **Lack of visibility into AI usage and user prompts:** Many organizations still struggle to answer basic questions about how AI is actually being used day to day, lacking visibility into tools used and prompts submitted.
- **Data quality, hallucinations, and model manipulation:** Mistakes in AI output carry real consequences, from hallucinations to RAG pipelines produced by biased or low-quality inputs.
- **Unmapped and unsecured private AI models:** Enterprises now deploy a mix of managed and unmanaged models and AI capabilities embedded in platforms like Salesforce, ServiceNow, and Atlassian, often lacking complete inventories or vulnerability statuses.
- **Privacy, compliance, and provider variability:** AI providers take different approaches to handling enterprise data, creating compliance challenges across GDPR, HIPAA, and PCI DSS.

### Real-world threats and vulnerabilities
The core risks of enterprise AI adoption continued to show up in real-world ways in 2025. Concerns such as data exposure, limited visibility into AI usage, hallucinations, and more surfaced as tangible security threats and operational vulnerabilities across enterprise environments.

- **AI-enabled social engineering** escalated as attackers leveraged generative AI for more convincing impersonation, including deepfake voice and video phishing ("vishing").
- **Agentic AI espionage campaigns:** Last year brought the first credible report of a cyber espionage campaign involving agentic AI. A Chinese state-sponsored group automated 80-90% of the intrusion chain with agentic AI, including recon, exploit validation, credential harvesting, lateral movement, and data exfiltration.
- **AI-assisted malware development:** In several campaigns observed by ThreatLabz, malware exhibited characteristics consistent with AI-assisted code generation.

---

### CASE STUDY
## GenAI-enhanced malware and social engineering in DPRK-linked campaigns

This case study highlights how GenAI is enabling attackers to bolster their operations without fundamentally changing attacker objectives or techniques. In the "Contagious Interview" campaign, linked to Democratic People’s Republic of Korea-aligned activity and the broader DPRK IT Worker scheme, ThreatLabz observed threat actors weaponizing GenAI to industrialize social engineering.

#### Resource Development & Social Engineering (Interview Deception)
The campaign begins with fabricating digital identities using GenAI technology, creating comprehensive study guides, generating professional yet untraceable profile pictures, and employing deepfake and voice manipulation tools to mask their identities during remote interviews.

- **AI-Generated Study Guides for Interview Mastery:** Threat actors produce detailed instructional playbooks using GenAI containing 70+ pages, featuring hallmark phrases like "Certainly!" and residual markdown formatting.
- **Identity Fabrication Using AI-Assisted Image Editing:** DPRK IT workers use AI image generation and editing technology to create fake digital identities for resumes, promotional webpages, and GitHub profiles with overly professional, edited features.
- **Initial Access & Execution:** Victims are persuaded to download trojanized software, like modified Node Package Manager (NPM) packages. Scripts exhibited distinct indicators of AI generation, featuring meticulous indentation, well-formed error messages, and a notable use of emojis.
- **Ongoing Exploitation of GitHub:** DPRK IT workers maintain GitHub repositories containing AI-generated or stolen code for applications like voice conversion tools, voice agents, face-swapping software, and image generators.

---

### CASE STUDY
## Emerging AI indicators in campaign targeting the South Asia region

As more evidence of AI-assisted malware development surfaces in the wild, Zscaler threat researchers identified code-level artifacts consistent with AI tooling in a separate campaign dubbed “Sheet Attack.” The campaign targets the South Asia region and is linked to Pakistani-based threat actors who use PDF lures to trick victims into downloading an archive containing a malicious .LNK file and an encrypted payload that installs the SHEETCREEP backdoor.

During analysis of certain variants of the SHEETCREEP backdoor, our researchers observed an unusual coding artifact: emojis embedded in error-logging routines—a stylistic trait uncommon in traditionally authored malware and increasingly associated with AI-assisted coding tools and development.

---

### CASE STUDY
## What’s really breaking in enterprise AI systems

This case study looks at what fails today when enterprise AI systems are tested under real adversarial conditions. This analysis is based on exploit data produced through Zscaler red teaming, conducted across 25+ enterprise environments, encompassing more than 222,000 adversarial attacks of which approximately 199,000 completed successfully without error.

#### Where failures happen most often
Platform data shows that enterprise AI system failure clusters around core behavioral and safety controls, not obscure edge cases. Bias (49%), off-topic responses (47%), and manipulation (45%) top the list, followed closely by competitor check, intentional misuse, and Q&A stability (all 44–45%).

| Rank | Probe Category | Fall % |
| --- | --- | --- |
| 01 | Bias | 49% |
| 02 | Off Topic | 47% |
| 03 | Manipulation | 45% |

---

## The Latest Phase of AI Governance

As organizations navigate 2026, AI governance has transitioned from an experimental policy exercise into an operational security imperative. Organizations are moving beyond blanket bans toward mature, policy-driven architectures that balance innovation with risk mitigation.

---

## AI Security Predictions for 2026

1. **Autonomous Agents Will Scale Attack Complexity:** Threat actors will increasingly operationalize agentic AI workflows, executing multi-stage intrusion chains at machine speed.
2. **Embedded AI Becomes the Primary Blind Spot:** As SaaS vendors turn on AI by default, implicit data flows will bypass traditional perimeter controls, making embedded AI the dominant vector for accidental data leakage.
3. **Regulatory Enforcement Will Target Unsecured RAG Pipelines:** Compliance frameworks will tighten scrutiny around how internal knowledge bases and external document repositories feed private LLMs.
4. **Zero Trust Mandates Expand to AI Workflows:** Identity-aware, inline inspection and runtime guardrails will become mandatory requirements for securing human-to-AI and AI-to-AI communications.

---

## Best Practices: Secure Enterprise AI Adoption

- **Establish End-to-End AI Visibility:** Discover and catalog all sanctioned, shadow, and embedded AI tools operating across your enterprise environment.
- **Implement Inline AI-Aware DLP:** Deploy data loss prevention controls capable of inspecting prompts and responses in real time to stop sensitive data leakage (PII, source code, financial records) to external models.
- **Enforce Granular Access Controls:** Restrict AI application usage based on user role, department, and sensitivity of the data involved rather than relying on blanket blocks.
- **Secure RAG and Private Model Pipelines:** Validate grounding data sources, audit permissions on connected document repositories, and protect internal models against prompt injection and data poisoning.
- **Continuously Red-Team AI Systems:** Regularly test enterprise AI assistants and custom applications under adversarial conditions to identify behavioral vulnerabilities before attackers exploit them.

---

## How Zscaler Delivers Comprehensive AI Protection

The Zscaler Zero Trust Exchange™ platform provides robust, inline security controls designed to address the unique challenges of enterprise AI adoption:
- **Comprehensive Discovery & Visibility:** Automatically detect and classify thousands of AI/ML applications and shadow AI usage across the enterprise.
- **AI-Aware Data Loss Prevention (DLP):** Prevent the exfiltration of sensitive enterprise data, source code, and regulatory identifiers to third-party LLMs.
- **Granular Policy Enforcement:** Apply context-aware inline policies to allow safe AI innovation while blocking high-risk applications and unauthorized transactions.
- **Protection Against Advanced AI Threats:** Safeguard against prompt injection, malicious AI-generated code, and modern vector-based attacks through integrated Zero Trust architecture.

---

## Research Methodology

This report is based on telemetry and analytics gathered globally from the Zscaler Zero Trust Exchange™ cloud platform. ThreatLabz analyzed 989.3 billion AI and ML transactions spanning January 2025 through December 2025. Additional datasets include regional breakdowns, departmental metrics, DLP violation logs, and red-team empirical testing outcomes across diverse enterprise environments.

---

## About ThreatLabz

Zscaler ThreatLabz is the global security research arm of Zscaler. Comprising expert threat researchers, engineers, and data scientists, ThreatLabz investigates emerging threat vectors, analyzes zero-day vulnerabilities, and delivers actionable intelligence to protect organizations worldwide against sophisticated cyber attacks.

---

ZZssccaalleerr TThhrreeaattLLaabbzz 22002266 AAII SSeeccuurriittyy RReeppoorrtt ©©22002265 ZZssccaalleerr,, IInncc.. AAllll rriigghhttss rreesseerrvveedd..

---

--- | --- | --- | --- | --------- | --- |
They break almost immediately. When full adversarial scans are run, critical  reflect everyday enterprise expectations to stay
|     |     |     | 03  | Manipulation | 45% |
| --- | --- | --- | --- | ------------ | --- |
vulnerabilities surface within minutes—and sometimes faster: on task, follow policy, avoid manipulation, and
provide reliable answers. Yet, they are where
|     |     |     | 04  | Competitor Check | 45% |
| --- | --- | --- | --- | ---------------- | --- |
models most often fail.
|     |     |     | 05  | Intentional Misuse | 44% |
| --- | --- | --- | --- | ------------------ | --- |
Structural checks and verification-oriented tasks
|      |         |      | 06  | Q&A | 44% |
| ---- | ------- | ---- | --- | --- | --- |
| 16   | 1 HOUR  | 01   |     |     |     |
such as URL validation also break frequently,
| MINUTES | 27 MINUTES | SECOND |     |           |     |
| ------- | ---------- | ------ | --- | --------- | --- |
|         |            |        | 07  | URL Check | 43% |
revealing limitations in AI reasoning and
grounding. At the same time, privacy and
Median time   90% of systems  Fastest   08 URL Check — One Shot 36%
phishing-related probes show that models can
| to first critical   | failed within  | observed   |     |                   |     |
| ------------------- | -------------- | ---------- | --- | ----------------- | --- |
|                     |                |            | 09  | Privacy Violation | 33% |
still be coerced into exposing sensitive data or
| failure | this timeframe | failure |     |     |     |
| ------- | -------------- | ------- | --- | --- | --- |
participating in harmful workflows.
|     |     |     | 10  | Phishing | 30% |
| --- | --- | --- | --- | -------- | --- |
In several instances, a single prompt was enough to trigger a high-severity
issue. This confirms that AI risk is present from the very first interaction.
Zscaler ThreatLabz 2026 AI Security Report ©2026 Zscaler, Inc. All rights reserved. 34

Case study: What’s really breaking in enterprise AI systems
Vulnerabilities span multiple risk domains
Across all environments tested, Zscaler red teaming identified a high volume of
vulnerabilities per AI system, with failures spread across multiple risk domains.
Security 64 pairs (67.3684%)
Safety 61 pairs (64.2105%)
Business Alignment 57 pairs (60.0%)
Hallucination & 40 pairs (42.1053%)
Trustworthiness
Custom 18 pairs (18.9474%)
Security issues (67%) were the most common, but safety (64%) and business alignment (60%)
followed closely, indicating that models struggle not just with protection but with staying within
defined task and policy boundaries. Hallucination and trust failures (42%) remain widespread,
while custom, domain-specific tests (19%) also surfaced meaningful weaknesses.
Critical failures are universal
Every AI system tested failed at least once. Across all targets, 100% exhibited one or more
critical vulnerabilities. These are not rare misconfigurations or unusual deployments. They are
universal traits of enterprise AI systems today.
KEY FINDING
For security leaders, this reinforces a simple reality: no AI system is safe by default, and
continuous adversarial testing is mandatory, not optional.
Our red teaming experts uncovered one or more
critical vulnerabilities in 100% of systems tested,
Most enterprises fail on the very first test
In 72% of enterprises, the very first test executed uncovered a critical vulnerability. This shows
proving that no AI system is safe by default.
how quickly high-severity risks surface once systems are exposed to adversarial pressure—
most organizations don’t need hours of testing to fail; they fail immediately. For CISOs, this
underscores that critical risk is present from day one, even in mature environments, and must be
addressed with continuous testing and runtime controls.
Zscaler ThreatLabz 2026 AI Security Report ©2026 Zscaler, Inc. All rights reserved. 35

Case study: What’s really breaking in enterprise AI systems
DALL-E Generated Image
Salt & Pepper
Mirror Image
Gaussian Filter
ImplicitVariation
Translate
Default language
Convert To Audio
DALL-E Generated Image/LeetSpeak
Multilanguage
DALL-E Generated Image/Base64
StringJoin
Default language
Multilanguage
Multilanguage
Salt & Pepper/Base64
PastVariation
Default language
Emojify
Multilanguage
Default language/LeetSpeak
RAG Variation
Gaussian Filter/Base64
Mirror Image/Base64
Default Language
Base64Encode
LeetSpeak
0 10 20 30
Failed %
Figure 18: Breakdown of top variations (exploit techniques that modify inputs) by
failure rate. Only variation types with ≥50 attempts are included.
noitairaV
Most common successful exploits
SUCCESSFUL EXPLOITS CONSISTENTLY FALL INTO FOUR CATEGORIES:
TOP VARIATIONS BY FAILURE RATE
1. Data leakage: Frequent failures involving 3. Jailbreaks and harmful content:
privacy, PII exposure, context leakage, and Multimodal variations like DALL-E images,
Base64/translation variations show how Salt-and-pepper noise, Gaussian filters,
easily models can be induced to reveal and mirrored images routinely bypass
sensitive information. safety mechanisms.
2. Prompt injection and manipulation: High 4. RAG poisoning and trust failures:
failure rates across manipulation, off-topic Hallucination, RAG precision, and
prompts, unstable Q&A, and language grounding-related variations (Translate,
or encoding variations (LeetSpeak, ImplicitVariation) show how easily retrieval
Multilanguage, StringJoin) reveal pipelines can be misled or corrupted.
brittle guardrails that break with minor
input changes.
Across text, image, audio, and encoded inputs, attackers succeed by
changing format, language, or structure—how a request is expressed—
revealing broad systemic weaknesses in enterprise AI systems.
40 50
Zscaler ThreatLabz 2026 AI Security Report ©2026 Zscaler, Inc. All rights reserved. 36

Case study: What’s really breaking in enterprise AI systems
WHAT THIS MEANS FOR
SECURITY TEAMS
This case study
demonstrates that
enterprise AI risk is
inherent and persistent.
Failures repeatedly
surface in known risk
areas and do so almost
immediately once
One-Shot
Tree Of Attack systems are tested.
Crescendo
Without continuous
Multi-Shot
testing and controls,
Multi-Step
AI systems introduce
One-Shot With Retry
Delayed Attack
material risk from the
Jailbreak Strategy
moment models are
0% 20%
Failed %
deployed.
Figure 19: Breakdown of top variations (exploit techniques that modify inputs)
by failure rate. Only variation types with ≥50 attempts are included.
ygetartS
Simplicity wins: the most effective attack strategies
The most effective attacks are often the least complex:
• One-shot attacks achieve the highest failure rate (60%), with the largest sample size,
proving many systems fail without escalation or chaining.
• Tree of Attacks, Crescendo, and Multi-Shot methods consistently degrade model
behavior under iterative pressure.
• Even defensive-aware strategies, including retries and multi-step prompts, continue to
succeed, exploiting weaknesses in reasoning, memory, and safety alignment.
60% n=135443
52% n=135443
46% n=135443
35% n=135443
28% n=135443
25% n=135443
18% n=135443
10% n=135443
40% 60%
Zscaler ThreatLabz 2026 AI Security Report ©2026 Zscaler, Inc. All rights reserved. 37

The Latest Phase_
In 2025, the focus expanded from ethical principles and how AI should
of AI Governance behave to how securely it must operate. With this came new mandates
for risk controls, testing, and ongoing oversight across the globe.
Security at the center U.S. AI governance
of the EU AI Act amid leans on standards,
shifting timelines not statutes
The European Union Artificial Intelligence Act remains the most The United States still lacks comprehensive federal AI law,
comprehensive AI regulatory framework, but implementation but 2025 marked a clear pivot in how the U.S. government
timelines and enforcement expectations are in flux. In late 2025, thinks about AI: national competitiveness first, with security
the European Commission proposed extending compliance and governance routed through standards and agency policy
deadlines for the riskiest parts of the law, particularly high- rather than broad regulation. The National Institute of Standards
risk AI systems (used in healthcare, law enforcement, etc.), and Technology (NIST) continues to lead adoption of the AI
to December 2027, contingent on parliament and member Risk Management Framework5 as the baseline for secure
states approvals.3 At the same time, new guidance and development, adversarial testing, and operational assurances.
support platforms are being rolled out to help organizations
navigate requirements such as incident reporting and In December 2025, the Administration issued an executive order
conformity assessments.4 aimed at preempting or challenging state AI laws that conflict
with a national AI policy framework and directing agencies
Organizations must treat the EU AI Act not as a static to pursue federal standards and litigation where necessary.6
compliance deadline but as a moving target, requiring ongoing Despite this, several states (including New York)7 continue to
readiness and proactive security controls. advance their own AI safety laws, underscoring that U.S. AI
regulation in 2026 will involve navigating a complex federal-
state policy environment.
3 Reuters, EU to delay ‘high risk’ AI rules until 2027 after Big Tech pushback, November 19, 2025.
4 European Commission, Commission launches AI Act Service Desk and Single Information Platform to support AI Act implementation, October 8, 2025.
5 NIST, AI Risk Management Framework.
6 Axios, Executive order targeting state AI laws, December 11, 2025.
7 Axios, N.Y. Gov. Kathy Hochul signs sweeping AI safety bill, December 19, 2025.
ZZssccaalleerr TThhrreeaattLLaabbzz 22002266 AAII SSeeccuurriittyy RReeppoorrtt ©©22002265 ZZssccaalleerr,, IInncc.. AAllll rriigghhttss rreesseerrvveedd.. 38

APAC accelerates secure AI adoption
Expectations for AI security should rise
sharply in 2026. Even as global and regional
Across the Asia-Pacific region, governments Singapore continued to mature its AI governance
continue to advance AI strategies that explicitly ecosystem through 2025, expanding its AI Verify
governance evolve—and enforcement
link rapid adoption with security and resilience. testing framework and related GenAI assurance
Many APAC economies are emphasizing practical initiatives,10 shifting further toward continuous
remains uneven—organizations will need to
governance frameworks and risk-based controls testing, monitoring, and assurance.
that can scale alongside AI deployment.
take ownership of securing their AI adoption.
Australia also advanced its approach through
Japan took a major step in 2025 with the Guidance for AI Adoption released in October
Policymakers may push for evidence-based
passage of its first comprehensive AI law, the 202511 alongside its Safe and Responsible AI
AI Promotion Act,8 in May 2025, establishing agenda—efforts that emphasize guardrails,
controls, but converging frameworks alone
a national blueprint that promotes AI R&D and testing, and stronger oversight for higher-risk
deployment while formally recognizing the need deployments, particularly in regulated sectors.
won’t reduce risk. AI success will ultimately
to manage associated risks.
With several substantial 2025 frameworks
depend on internal security discipline.
India followed with its 2025 AI Governance moving forward in parallel, APAC is increasingly
Guidelines,9 a broad framework aimed at positioning itself as a global leader in pragmatic,
Organizations that implement zero trust,
“Safe and Trusted AI.” These guidelines tie AI security-first AI innovation and adoption.
adoption closely to the country’s Digital Public
continuously test models, and monitor for
Infrastructure and set expectations for data
governance, algorithmic transparency, and risk
evolving threats will be best positioned to
management, particularly for large-scale public
services and financial systems.
deploy AI responsibly.
8 IT Business Today, Japan’s AI Regulation is a Significant Step Forward with the AI Promotion Act, October 29, 2025.
9 AI, Data & Analytics Network, India unveils new AI governance guidelines to encourage responsible adoption, November 6, 2025.
10 IMDA, Singapore launches new tools to help businesses protect data and deploy AI in a trusted ecosystem, July 7, 2025.
11 Australian Government, DISR, Guidance for AI Adoption, October 21, 2025.
ZZssccaalleerr TThhrreeaattLLaabbzz 22002266 AAII SSeeccuurriittyy RReeppoorrtt ©2026 Zscaler, Inc. All rights reserved. 39

AI Security
Predictions for 2026
Autonomous and human
1
orchestrated agentic AI
attacks
The threat of agentic AI will escalate as autonomous systems take on
more of the intrusion workload. AI agents that can plan and take actions
independently will play a larger role in cyberattacks in 2026. Early signs of
this shift already appeared in 2025 with the first reported AI-orchestrated
espionage campaign as mentioned above, where a state-sponsored
group automated 80-90% of its attack steps with agentic AI. AI-powered
ransomware attacks will accelerate the shift from encryption to high-
speed data theft with AI enabling more operations at once and reducing
attacker overhead.
AI supply chain attacks
2
Attacks on the AI supply chain will target the core components that power
enterprise AI systems. ThreatLabz discoveries in 2025 exposed how
weaknesses in common model files and processing layers could be used to
access sensitive systems. Attackers will increasingly focus on tampering with
the underlying pieces of AI (models and datasets) rather than only misusing
AI at the application level. As more organizations import third-party AI
components into their environments, compromising these foundational
elements will provide powerful access. Securing the AI supply chain will
remain as important as securing the application built on top of it.
ZZssccaalleerr TThhrreeaattLLaabbzz 22002266 AAII SSeeccuurriittyy RReeppoorrtt ©©22002265 ZZssccaalleerr,, IInncc.. AAllll rriigghhttss rreesseerrvveedd.. 40

Embedded AI security risks Fraudulent AI embedded in
3 5
enterprise workflows
Embedded AI inside everyday applications will introduce hidden access that
traditional security tools may overlook. AI features built directly into popular Deceptive AI services and platforms will shift from isolated scams to deeply
business applications, cloud platforms, and mobile tools—think Zoom’s AI embedded footholds inside business workflows. The steady rise of AI tool
meeting summaries or Microsoft 365 Copilot assistant—will create subtle adoption in 2025 has already shown how easy it is for malicious AI services
risks that are easy to miss. These embedded AI capabilities often have broad to slip into real workflows. Expect attackers to move beyond fake AI landing
access to sensitive content, making them attractive targets for misuse. pages and begin releasing full-featured malicious copilots that act like real
Enterprises should expect attackers to increasingly try to exploit these productivity assistants while blending into everyday use. This next phase will
built-in functions to exfiltrate valuable intel or gain access and move quietly make rogue assistants harder to spot, contributing greatly to the risks from
within an environment, taking advantage of the fact that many organizations unapproved or shadow AI used by enterprise employees.
still lack full visibility into where AI has been embedded in the software
supply chain.
Ransomware & nation-state Enterprise-wide AI security
4 6
attacks on GenAI data stores and accountability
As enterprises move from GenAI pilots to full deployments in 2026, far more AI security will become an enterprise-wide requirement as oversight and
internal systems will funnel sensitive information into AI-driven workflows. accountability increase. After a year of high-profile concerns and growing
Attackers will take advantage of this shift by targeting the data stores scrutiny in 2025, organizations face mounting expectations around how they
behind GenAI applications. These stores contain more than raw data, but manage AI: how models are vetted, how data is handled, and how potential
also context and intent, giving adversaries far greater visibility into internal misuse is monitored. Securing AI systems in 2026 will no longer be optional
decision cycles—and, as a result, more leverage than most traditional or limited to technical teams. Leadership will need clear visibility into AI risk,
breaches offer. Compromising LLM data stores will become a high-yield and security policies need to extend across every part of the business that
tactic for espionage and ransomware extortion in the year ahead. interacts with AI.
ZZssccaalleerr TThhrreeaattLLaabbzz 22002266 AAII SSeeccuurriittyy RReeppoorrtt ©©22002265 ZZssccaalleerr,, IInncc.. AAllll rriigghhttss rreesseerrvveedd.. 41

Best_Practices:
Secure Enterprise
AI Adoption
5 hard truths of AI security in 2026
The good news: you don’t have to accept these
You can’t secure what you can’t see. Shadow AI and embedded “hard truths” as the cost of AI adoption. Use the
1
AI functionality make visibility the new perimeter.
2026 enterprise security checklist that follows to
prioritize the right protections first.
Vendor defaults aren’t built for enterprise risk. AI features
2
often ship “on” and overly permissive.
AI governance is a moving target. Policies must evolve as
3
capabilities and threats shift.
Zero trust now extends to AI models. They require the same
4
level of access control as human users.
AI is an undeniable part of the attack surface. Model
5
vulnerabilities and agentic AI attacks are here.
Zscaler ThreatLabz 2026 AI Security Report ©©22002265 ZZssccaalleerr,, IInncc.. AAllll rriigghhttss rreesseerrvveedd.. 42

2026 enterprise
AI security checklist
The following best practices establish a strong baseline for secure AI use. Enterprises should also define governance standards and rules of
engagement for how AI is adopted and managed.
Inventory all GenAl apps and apps with embedded Enforce AI guardrails with
AI functionality inline inspection Update AI governance often Conduct adversarial testing and model red teaming
• Create a continuously updated catalog of • Ensure inline inspection across all AI/ML • Refresh policies, access controls, and • Continuously test models for jailbreaks,
every standalone GenAl tool and every traffic to prevent external malicious activity risk classifications regularly to keep pace prompt injection, data leakage, and other
SaaS or internal app that includes AI from compromising AI systems and stop with rapid changes in AI capabilities and exploitable weaknesses before attackers
functionality or features. sensitive data from being exposed via regulatory requirements. find them.
prompts or in outputs.
Disable risky AI defaults Validate model lineage and supply chain Mandate human review for regulated workflows Secure the AI development lifecycle end-to-end
• Turn off auto-enabled AI functionality in • Verify model provenance, updates, • Ensure humans remain in the loop • Apply controls from dataset ingestion
SaaS and productivity apps until they have datasets, and dependencies of every model wherever AI influences decisions tied to through training, deployment, and
been reviewed and configured to match to reduce risk from tampering, poisoning, safety, compliance, financial decisions, or monitoring to prevent vulnerabilities from
your risk posture. or compromised components. public sector determinations. entering production systems.
Apply zero trust to all model interactions
• Implement least-privilege access for every
user, service, and system that interacts
with an AI model.
Zscaler ThreatLabz 2026 AI Security Report ©2026 Zscaler, Inc. All rights reserved. 43

How enterprises are
safely rolling out GenAI:
a real-world playbook
The organizations that avoided incidents were the
AI risk came from both sides of the enterprise boundary in 2025. Threat actors
ones that introduced GenAI in controlled phases and
used GenAI to accelerate and facilitate their operations, while internal exposure
increasingly stemmed from everyday AI use without formal oversight—allowing
enabled only what they could govern.
data to reach AI systems before security teams could assess or control the risk.
Their real-world playbook looks like this:
BEGIN WITH A ZERO TRUST STANCE AND HOST APPROVED GENAI TOOLS IN A PRIVATE,
RESTRICT UNVETTED AI SERVICES CONTROLLED ENVIRONMENT
Countless AI tools introduce unknown data handling and To keep full control over enterprise data, organizations should run approved GenAI
security risks, making it critical to start from a zero trust tools in a private and secure environment, such as a dedicated tenant or isolated
position. Blocking or limiting access to unvetted AI/ML instance managed entirely by the company. This setup ensures that neither the vendor
applications removes immediate exposure and prevents nor third parties can access internal or customer data and prevents prompts and
early data leakage, giving security teams the space to outputs from being used to train public models. Operating GenAI this way preserves
assess which apps are appropriate for enterprise use. data sovereignty and keeps sensitive information from leaving the organization.
IDENTIFY AND VALIDATE THE GENAI APPLICATIONS ENFORCE STRONG IDENTITY AND APPLY DATA PROTECTION TO PREVENT
THAT MEET ENTERPRISE REQUIREMENTS ACCESS CONTROLS ACCIDENTAL OR UNAUTHORIZED SHARING
Determine which GenAI apps are safe to use by Place approved GenAI apps behind a zero trust Pair approved access with enterprise-grade DLP.
checking how they handle data, whether they keep architecture with granular access policies. This ensures Monitoring and inspecting traffic to and from
your information isolated, how the model was built, and each user, department, and workflow receives only the AI apps ensures sensitive information remains
whether the vendor meets your security, privacy, and access needed, while giving security teams end-to- contained and that no critical data is exposed
compliance requirements. Only tools that satisfy these end visibility and control over all activity. through interactions with these apps.
standards should move forward.
Zscaler ThreatLabz 2026 AI Security Report ©2026 Zscaler, Inc. All rights reserved. 44

How Zscaler Delivers_
Comprehensive AI Protection
The findings in this report confirm that Securing AI at scale requires a different approach
enterprise AI adoption is accelerating fast. As a that reduces exposure by default, continuously
result, an expanding attack surface, shadow and verifies access, and applies security controls
embedded AI usage, and constantly evolving wherever AI is used or built. Zero trust provides
models and infrastructure are introducing that foundation.
new risks around data exposure, misuse, and
governance that legacy security approaches Zscaler delivers an AI security platform built on
cannot effectively address. zero trust that secures AI everywhere—across
how organizations use, build, and operate AI.
Security architectures built on firewalls, VPNs, By shrinking the attack surface, enforcing least-
and perimeter-based controls were not designed privileged access, and inspecting all traffic inline,
or intended for dynamic AI environments. In Zscaler helps organizations adopt AI securely
practice, they add complexity and leave gaps without slowing innovation.
in visibility. They struggle to enforce consistent
controls across public AI tools, agents, private
models, and emerging components like Model
Context Protocol (MCP) servers.
Organizations are left reacting to AI risk rather
than managing it proactively.
Zscaler ThreatLabz 2026 AI Security Report ©©22002265 ZZssccaalleerr,, IInncc.. AAllll rriigghhttss rreesseerrvveedd.. 45

Turning AI risk into With zero trust as the foundation, Zscaler applies AI-native security controls that translate architecture into action.
These capabilities give organizations the visibility, guardrails, and protections needed to govern AI usage in real time-
secure AI adoption
while actively disrupting AI-powered threats across users, applications, and infrastructure.
Zscaler AI empowers organizations to:
STAY AHEAD OF AI-POWERED THREATS
SECURELY ENABLE PUBLIC AND PRIVATE AI USAGE
• See exactly where and how AI is being used, including AI applications, • Reduce exposure by eliminating the external attack surface and enforcing
models, agents, prompts, responses, and emerging components such as continuous verification and least-privileged access.
MCP servers.
• Inspect all traffic, including encrypted traffic, to block AI-enhanced threats in
• AIlow employees to use AI tools productively while isolating risky real time.
web-based AI interactions and preventing sensitive data from being
unintentionally shared with external models. • Apply predictive and generative AI to surface risks faster and improve
security operations and response.
• Detect and block prompt injection, PII exposure, data poisoning, unsafe
outputs, and other AI-specific threats at runtime with built-in AI guardrails. • Continuously discover, classify, and protect sensitive data across endpoints,
inline traffic, and cloud environments.
• Control who can use AI, which tools they can access, and how AI is used
with policies that adapt continuously to user, device, and application risk, • Stop lateral movement with AI-powered segmentation that limits
automatically blocking unauthorized or shadow AI. attacker reach.
• Prevent sensitive data from being sent to or returned from AI tools using • Continuously assess AI and zero trust posture with AI-generated insights
inline, AI-aware DLP controls. and recommendations.
• Maintain a detailed, searchable audit trail of AI activity to support
investigations and compliance.
These outcomes are delivered through a unified set of protections that span the AI security lifecycle, as covered in the section that follows.
ZZssccaalleerr TThhrreeaattLLaabbzz 22002266 AAII SSeeccuurriittyy RReeppoorrtt ©©22002265 ZZssccaalleerr,, IInncc.. AAllll rriigghhttss rreesseerrvveedd.. 46

Zscaler + AI: securing how
organizations use and build apps
Zscaler offers comprehensive protection—from discovery and risk assessment to securing AI
applications and access—covering public and private AI, models, pipelines, agents, and infrastructure.
AI ASSET SECURE ACCESS SECURE AI APPLICATIONS AND
MANAGEMENT TO AI APPS INFRASTRUCTURE
Discover your full Ensure the safe and responsible Harden AI systems and prompts
AI footprint and risks use of AI applications and enforce runtime protection
Full visibility into all applications, Granular control over which users can Vulnerability detection in models
models, pipelines, and MCP servers. access which apps. and pipelines.
An AI-BOM to uncover supply chain Inline inspection of prompts and Red team testing to identify exposure
and dependency risks. responses to prevent sensitive data and weaknesses.
from being sent or returned.
Identification of high-risk GenAI SaaS Protection from prompt injections, data
applications and AI models. Content controls to block unsafe or poisoning, use of sensitive data, etc.
harmful outputs.
AI Governance: Stay compliant with AI frameworks via mapping of AI security controls to NIST AI Risk Management Framework and the EU AI Act.
Zscaler ThreatLabz 2026 AI Security Report ©2026 Zscaler, Inc. All rights reserved. 47

Research_
Methodology
Findings are based on analysis of 989.3 billion total AI and ML transactions in the Zscaler
cloud from January 2025 through December 2025. The Zscaler global security cloud
processes more than 500 trillion daily signals and blocks 9 billion threats and policy violations
per day, delivering more than 250,000 daily security updates.
About_
ThreatLabz
ThreatLabz is the security research arm of Zscaler. This world–class team is responsible for
hunting new threats and ensuring that the thousands of organizations using the global Zscaler
platform are always protected. In addition to malware research and behavioral analysis,
team members are involved in the research and development of new prototype modules
for advanced threat protection on the Zscaler platform, and regularly conduct internal
security audits to ensure that Zscaler products and infrastructure meet security compliance
standards. ThreatLabz regularly publishes in-depth analyses of new and emerging threats
at research.zscaler.com.
Follow us: X @ThreatLabz | ThreatLabz security research blog
Zscaler ThreatLabz 2026 AI Security Report ©2026 Zscaler, Inc. All rights reserved. 48

Zero Trust Everywhere
About Zscaler
Zscaler (NASDAQ: ZS) accelerates digital transformation so customers can be more agile, efficient, resilient, and
secure. The Zscaler Zero Trust Exchange™ platform protects thousands of customers from cyberattacks and data
loss by securely connecting users, devices, and applications in any location. Distributed across more than 150 data
centers globally, the SSE-based Zero Trust Exchange™ is the world’s largest in-line cloud security platform. Learn
more at zscaler.com or follow us on Twitter @zscaler.
© 2026 Zscaler, Inc. All rights reserved. Zscaler™ and other trademarks listed at zscaler.com/legal/trademarks are either (i) registered
trademarks or service marks or (ii) trademarks or service marks of Zscaler, Inc. in the United States and/or other countries. Any other
trademarks are the properties of their respective owners.
+1 408.533.0288 Zscaler, Inc. (HQ) • 120 Holger Way • San Jose, CA 95134 zscaler.com