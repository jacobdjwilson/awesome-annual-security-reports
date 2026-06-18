# Zscaler ThreatLabz 2026 AI Security Report

## Table of Contents
- [Executive Summary](#executive-summary)
- [What This Means for Enterprise Leaders](#what-this-means-for-enterprise-leaders)
- [Key Findings](#key-findings)
- [AI/ML Usage Trends](#aiml-usage-trends)
- [Global growth in AI/ML transactions](#global-growth-in-aiml-transactions)
- [Top LLM vendors, applications, and departments](#top-llm-vendors-applications-and-departments)
- [Blocked transactions](#blocked-transactions)
- [Data transferred to AI applications](#data-transferred-to-ai-applications)
- [Data loss to AI applications](#data-loss-to-ai-applications)
- [The rise of embedded AI](#the-rise-of-embedded-ai)
- [AI/ML usage by industry](#aiml-usage-by-industry)
- [AI/ML usage by country](#aiml-usage-by-country)
- [Enterprise AI Risks and Threat Landscape](#enterprise-ai-risks-and-threat-landscape)
- [Case study: GenAI-enhanced malware and social engineering in DPRK-linked campaigns](#case-study-genai-enhanced-malware-and-social-engineering-in-dprk-linked-campaigns)
- [Case study: Emerging AI indicators in campaign targeting the South Asia region](#case-study-emerging-ai-indicators-in-campaign-targeting-the-south-asia-region)
- [Case study: What’s really breaking in enterprise AI systems](#case-study-whats-really-breaking-in-enterprise-ai-systems)

---

## Executive Summary

The daily reality of AI in 2025 was defined by speed, scale, and constant motion. Enterprises now rely on artificial intelligence and machine learning (AI/ML) across the business to move faster, automate decisions, and increase productivity. AI supports development, communications, research, and operations at a pace that would have seemed unrealistic just a few years ago. But this acceleration has also come with more and more tradeoffs: more sensitive data flows through more AI/ML applications, often with less visibility and fewer guardrails.

That expanding AI footprint has widened the enterprise attack surface, and threat actors were quick to follow over the past year. Lower barriers and higher realism have made attacks faster and more convincing, while early signs of agentic and semi-autonomous AI misuse pointed to a shift in how threats are evolving. At the same time, organizations are contending with a growing mix of risks—from shadow and embedded AI to hallucinations and unsecured private models.

The Zscaler ThreatLabz 2026 AI Security Report explores how enterprises are navigating this balancing act. The report draws on analysis of 989.3 billion AI/ML transactions observed across the Zscaler Zero Trust Exchange™ from January 2025–December 2025, providing a grounded view into how AI is actually being used (and restricted) across global environments.

The data shows continued acceleration. Enterprise AI/ML activity increased 83.3% year-over-year, while data transfer volumes rose 92.6%, reaching more than 18,000 terabytes (TB). At this scale, AI behaves less like a set of discrete tools and more like always-on infrastructure, continuously moving and transforming enterprise data. Access, however, remains far from unrestricted. Organizations blocked 39% of AI/ML transactions, reflecting persistent concerns around data exposure, privacy, and policy enforcement.

Usage patterns also reveal where value and risk intersect. The AI applications employees rely on most, such as Codeium, Grammarly, and ChatGPT, sit at the center of how work gets done, driving the highest levels of activity while also appearing at the forefront in our risk findings.

In 2026, securing AI is about more than controlling AI/ML applications. It’s about securing how AI is discovered, built, used, and governed across the enterprise. Organizations need visibility into AI usage and risk, protections that harden AI systems and data in real time, and consistent controls that secure access while keeping innovation moving. This report delves into the trends and realities shaping AI security, and provides guidance for enterprises looking to reduce risk and adopt AI safely.

*Correction (February 2026): The year-over-year percentage change in AI/ML transaction volume has been updated to reflect a revised calculation.*

---

## What This Means for Enterprise Leaders

- **AI is now enterprise infrastructure.** Nearly one trillion AI transactions signal continuous, always-on operations. AI must be governed with the same rigor as cloud, identity, and data to support safe and scalable adoption.
- **Data exposure risk now scales with volume, not intent.** Petabyte-scale data movement through AI workflows increases exposure through repetition and speed, even when usage is approved and aligned with business intent.
- **Approved AI is the primary risk surface.** Mainstream, sanctioned AI tools account for the majority of enterprise AI activity and data interactions. While shadow AI remains a key concern, addressing unauthorized tools alone will not mitigate the full scope of AI-related risks and exposure.
- **Security is constraining AI adoption.** With 39% of AI transactions blocked, policy enforcement is actively shaping how AI is used. This reflects governance in action, not resistance to AI as leaders balance the tradeoff between innovation speed and risk tolerance.
- **Traditional security models are misaligned with AI workflows.** Controls designed for human-paced activity and static data cannot keep up with machine-driven, high-frequency AI interactions.
- **Competitive advantage will favor organizations that can govern AI at scale.** Enterprises that enable broad AI use with strong, inline controls will move faster than those forced to fully restrict usage due to unmanaged risk.

---

## Key Findings

ThreatLabz analyzed 989.3 billion AI and ML transactions in the Zscaler cloud from January 2025–December 2025.

- **Enterprise AI usage continues its strong upward trajectory.** AI/ML activity increased 83% year-over-year, reaching nearly one trillion transactions across an ecosystem of more than 3,400 applications.
- **Enterprises send increasingly large volumes of data to AI tools.** A total of 18,033 TB of data was transferred to AI/ML applications, a 93% year-over-year rise.
- **High block rates signal ongoing risk management.** Enterprises blocked 39% of overall AI/ML transactions, underscoring continued concerns about data exposure, privacy, and policy alignment as AI usage expands.
- **Enterprise AI is wide open to compromise.** Zscaler red teaming experts found most enterprise AI systems can be breached in just 16 minutes, and uncovered critical flaws in 100% of systems tested.
- **OpenAI dominates as the top LLM vendor.** OpenAI accounted for the vast majority of LLM-driven enterprise transactions (3x more than Codeium), establishing it as the current de facto LLM.
- **ChatGPT accounts for the overwhelming majority of DLP violations.** Across all AI/ML applications analyzed, ChatGPT generated 410 million data loss prevention (DLP) policy violations, affirming enterprise risks tied to high-context AI assistants.
- **Integrated productivity apps anchor enterprise AI usage.** Grammarly became the #1 application by transaction volume, reflecting reliance on AI that operates directly within communication and business processes.
- **Finance & Insurance and Manufacturing lead enterprise AI usage again.** For the third year in a row, these sectors represented the largest share of AI/ML traffic (23% and 20%, respectively) behind their modernization efforts and heavy documentation workflows.
- **The United States remained the primary source of AI/ML transactions.** Activity was concentrated in the U.S., which accounted for 38% of transactions, followed by India (14%) and Canada (5%).
- **AI adoption continues to expand the enterprise attack surface.** Broader use of AI across enterprise workflows has created more paths for data and access to be exposed, increasing the likelihood of data leakage, prompt misuse, and AI-assisted attacks—reinforcing the need for zero trust architecture and AI-powered security controls.

---

## AI/ML Usage Trends

Enterprise use of AI continued its steep and steady climb in 2025. ThreatLabz analysis of AI usage trends now includes more than 3,400 applications driving AI/ML transactions—four times more than the previous year.

### Global growth in AI/ML transactions
AI/ML transactions approached the trillion mark in 2025, totaling 989.3 billion. Much of this growth is tied to high-volume applications such as ChatGPT, Grammarly, and Codeium.

![Figure 1: Year-over-year comparison of AI/ML transactions (January–December 2025)]

![Figure 2: Distribution of AI/ML transactions across general and classified AI applications]

### Top LLM vendors, applications, and departments
Looking at enterprise AI usage through LLM vendors offers a unique view of how AI is operating at scale.

![Figure 3: LLM vendor transaction trends throughout 2025]

**Key LLM vendor findings:**
- **OpenAI** was the clear leader among LLM vendors in 2025, accounting for 131 billion transactions.
- **Codeium** (rebranded as Windsurf in 2025) emerged as the second-largest source of enterprise LLM traffic (42 billion transactions).
- **Perplexity** took the third position by transaction volume last year (12 billion transactions).

![Figure 4: Percentage of total AI/ML transactions driven by leading AI applications]

### Blocked transactions
Organizations blocked 39.2% of total AI/ML transactions. Grammarly comprised the single largest share of blocked activity—171.2 billion blocked transactions.

### Data transferred to AI applications
Enterprise data transfer to AI/ML applications reached 18,033 terabytes (TB)—a 93% increase year-over-year.

![Figure 6: Top AI/ML applications by the percentage of total data transferred]

### Data loss to AI applications
AI-related DLP policy violations increased 99.3% year-over-year. The most common violations specific to ChatGPT included name leakage and national identifiers.

### The rise of embedded AI
Embedded AI—features built into everyday applications that aren’t classified as GenAI apps—represents one of the fastest growing and least visible sources of enterprise AI risk.

### AI/ML usage by industry
Finance & Insurance organizations account for the largest share (23.3%) of AI/ML traffic for the second year in a row.

![Figure 7: Industries driving the largest proportions of AI transactions]

### AI/ML usage by country
The United States continued to lead in absolute usage (218.9 billion AI/ML transactions, accounting for 37.6% of global activity). India was the second-largest source of enterprise AI activity, reaching 82.3 billion transactions—a 309.9% year-over-year increase.

![Figure 8: Year-over-year growth in AI/ML transactions by country]
![Figure 9: Map displaying top 10 countries based on volume of AI/ML transactions]

---

## Enterprise AI Risks and Threat Landscape

The most significant risks fall into the following categories:
- **Data exposure and sensitive information leakage:** AI systems see some of the most sensitive data in the enterprise—source code, customer records, financial details, and legal documents.
- **Lack of visibility into AI usage and user prompts:** Security teams often lack a clear view of which AI tools employees use, what prompts they submit, and whether sensitive data is at risk.
- **Data quality, hallucinations, and model manipulation:** With AI integrated into daily business operations, mistakes in its output carry real consequences.
- **Unmapped and unsecured private AI models:** Enterprises now deploy a mix of managed and unmanaged models and AI capabilities embedded in platforms like Salesforce, ServiceNow, and Atlassian.
- **Privacy, compliance, and provider variability:** AI providers take different approaches to handling enterprise data, creating compliance challenges across frameworks like GDPR, HIPAA, and PCI DSS.

---

## Case study: GenAI-enhanced malware and social engineering in DPRK-linked campaigns

In the “Contagious Interview” campaign, linked to Democratic People’s Republic of Korea-aligned activity, threat actors weaponized GenAI to industrialize social engineering—creating and operationalizing convincing fake personas—while using AI-assisted coding in malware development.

---

## Case study: Emerging AI indicators in campaign targeting the South Asia region

Zscaler threat researchers identified code-level artifacts consistent with AI tooling in a campaign dubbed “Sheet Attack.” The campaign targets the South Asia region and uses PDF lures to trick victims into downloading an archive that contains a malicious .LNK file along with an encrypted payload.

---

## Case study: What’s really breaking in enterprise AI systems

This analysis is based on exploit data produced through Zscaler red teaming, conducted across 25+ enterprise environments, encompassing more than 222,000 adversarial attacks. Platform data shows that enterprise AI system failure clusters around core behavioral and safety controls, not obscure edge cases. Bias (49%), off-topic responses (47%), and manipulation (45%) top the list.

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