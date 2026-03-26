# AI Security Report

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

# Executive Summary

The daily reality of AI in 2025 was defined by speed, scale, and constant motion.

Enterprises now rely on artificial intelligence and machine learning (AI/ML) across the business to move faster, automate decisions, and increase productivity. AI supports development, communications, research, and operations at a pace that would have seemed unrealistic just a few years ago. But this acceleration has also come with more and more tradeoffs: more sensitive data flows through more AI/ML applications, often with less visibility and fewer guardrails.

That expanding AI footprint has widened the enterprise attack surface, and threat actors were quick to follow over the past year. Lower barriers and higher realism have made attacks faster and more convincing, while early signs of agentic and semi-autonomous AI misuse pointed to a shift in how threats are evolving. At the same time, organizations are contending with a growing mix of risks—from shadow and embedded AI to hallucinations and unsecured private models.

How do enterprises secure environments where AI touches everything, enable AI-driven innovation, and defend against AI-powered threats? (All without slowing the business, of course).

The Zscaler ThreatLabz 2026 AI Security Report explores how enterprises are navigating this balancing act. The report draws on analysis of 989.3 billion AI/ML transactions observed across the Zscaler Zero Trust Exchange™ from January 2025–December 2025, providing a grounded view into how AI is actually being used (and restricted) across global environments.

The data shows continued acceleration. Enterprise AI/ML activity increased 83.3% year-over-year, while data transfer volumes rose 92.6%, reaching more than 18,000 terabytes (TB). At this scale, AI behaves less like a set of discrete tools and more like always-on infrastructure, continuously moving and transforming enterprise data. Access, however, remains far from unrestricted. Organizations blocked 39% of AI/ML transactions, reflecting persistent concerns around data exposure, privacy, and policy enforcement.

Usage patterns also reveal where value and risk intersect. The AI applications employees rely on most, such as Codeium, Grammarly, and ChatGPT, sit at the center of how work gets done, driving the highest levels of activity while also appearing at the forefront in our risk findings.

In 2026, securing AI is about more than controlling AI/ML applications. It’s about securing how AI is discovered, built, used, and governed across the enterprise. Organizations need visibility into AI usage and risk, protections that harden AI systems and data in real time, and consistent controls that secure access while keeping innovation moving. This report delves into the trends and realities shaping AI security, and provides guidance for enterprises looking to reduce risk and adopt AI safely.

_Correction (February 2026): The year-over-year percentage change in AI/ML transaction volume has been updated to reflect a revised calculation._

---

# What This Means for Enterprise Leaders

- **AI is now enterprise infrastructure.** Nearly one trillion AI transactions signal continuous, always-on operations. AI must be governed with the same rigor as cloud, identity, and data to support safe and scalable adoption.
- **Security is constraining AI adoption.** With 39% of AI transactions blocked, policy enforcement is actively shaping how AI is used. This reflects governance in action, not resistance to AI as leaders balance the tradeoff between innovation speed and risk tolerance.
- **Data exposure risk now scales with volume, not intent.** Petabyte-scale data movement through AI workflows increases exposure through repetition and speed, even when usage is approved and aligned with business intent.
- **Approved AI is the primary risk surface.** Mainstream, sanctioned AI tools account for the majority of enterprise AI activity and data interactions. While shadow AI remains a key concern, addressing unauthorized tools alone will not mitigate the full scope of AI-related risks and exposure.
- **Traditional security models are misaligned with AI workflows.** Controls designed for human-paced activity and static data cannot keep up with machine-driven, high-frequency AI interactions.
- **Competitive advantage will favor organizations that can govern AI at scale.** Enterprises that enable broad AI use with strong, inline controls will move faster than those forced to fully restrict usage due to unmanaged risk.

---

# Key Findings

ThreatLabz analyzed 989.3 billion AI and ML transactions in the Zscaler cloud from January 2025–December 2025.

- **Enterprise AI usage continues its strong upward trajectory.** AI/ML activity increased 83% year-over-year, reaching nearly one trillion transactions across an ecosystem of more than 3,400 applications.
- **Enterprises send increasingly large volumes of data to AI tools.** A total of 18,033 TB of data was transferred to AI/ML applications, a 93% year-over-year rise.
- **High block rates signal ongoing risk management.** Enterprises blocked 39% of overall AI/ML transactions, underscoring continued concerns about data exposure, privacy, and policy alignment as AI usage expands.
- **Enterprise AI is wide open to compromise.** Zscaler red teaming experts found most enterprise AI systems can be breached in just 16 minutes, and uncovered critical flaws in 100% of systems tested.
- **OpenAI dominates as the top LLM vendor.** OpenAI accounted for the vast majority of LLM-driven enterprise transactions (3x more than Codeium).
- **ChatGPT accounts for the overwhelming majority of DLP violations.** ChatGPT generated 410 million data loss prevention (DLP) policy violations.
- **Integrated productivity apps anchor enterprise AI usage.** Grammarly became the #1 application by transaction volume.
- **Finance & Insurance and Manufacturing lead enterprise AI usage again.** These sectors represented the largest share of AI/ML traffic (23% and 20%, respectively).
- **The United States remained the primary source of AI/ML transactions.** The U.S. accounted for 38% of transactions, followed by India (14%) and Canada (5%).
- **AI adoption continues to expand the enterprise attack surface.** Broader use of AI has created more paths for data and access to be exposed.

---

# AI/ML Usage Trends

Enterprise use of AI continued its steep and steady climb in 2025. ThreatLabz analysis now includes more than 3,400 applications driving AI/ML transactions—four times more than the previous year.

## Global growth in AI/ML transactions
AI/ML transactions approached the trillion mark in 2025, totaling 989.3 billion.

![Chart showing year-over-year growth of AI/ML transactions from 2024 to 2025]

## Top LLM vendors, applications, and departments
- **OpenAI:** 131 billion transactions.
- **Codeium:** 42 billion transactions.
- **Perplexity:** 12 billion transactions.

**Top AI Applications by Volume:**
1. Grammarly (38.71%)
2. ChatGPT (14.22%)
3. Codeium (5.01%)
4. DeepL (3.29%)
5. Microsoft Copilot (3.02%)

**Departmental Usage:**
- Engineering: 48.9%
- IT: 31.8%
- Marketing: 6.9%

## Blocked transactions
Organizations blocked 39.2% of total AI/ML transactions. Grammarly accounted for 44.2% of all blocked AI/ML transactions.

## Data transferred to AI applications
A total of 18,033 TB of data was transferred to AI/ML applications—a 93% year-over-year increase.

## Data loss to AI applications
AI-related DLP policy violations continue to be a clear signal of risk.
- ChatGPT DLP violations increased 99.3% year-over-year.
- Codeium DLP violations increased 100% year-over-year.

## The rise of embedded AI
Embedded AI—features built into everyday applications—represents one of the fastest-growing and least visible sources of enterprise AI risk.

## AI/ML usage by industry
- Finance & Insurance: 23.3%
- Manufacturing: 19.5%
- Technology & Communication: 17.4% (highest YoY growth)

## AI/ML usage by country
- United States: 37.6%
- India: 14.1%
- Canada: 4.7%

---

# Enterprise AI Risks and Threat Landscape

The most significant risks include:
1. **Data exposure and sensitive information leakage.**
2. **Lack of visibility into AI usage and user prompts.**
3. **Data quality, hallucinations, and model manipulation.**
4. **Unmapped and unsecured private AI models.**
5. **Privacy, compliance, and provider variability.**

## Case study: GenAI-enhanced malware and social engineering in DPRK-linked campaigns
Threat actors are weaponizing GenAI to industrialize social engineering, creating fake personas and using AI-assisted coding in malware development.

## Case study: Emerging AI indicators in campaign targeting the South Asia region
Zscaler researchers identified code-level artifacts consistent with AI tooling in the "Sheet Attack" campaign, which uses PDF lures to install the SHEETCREEP backdoor.

## Case study: What’s really breaking in enterprise AI systems
Zscaler red teaming conducted across 25+ enterprise environments found:
- **16 minutes:** Median time to first critical failure.
- **100%:** Systems tested contained critical flaws.
- **Top failure categories:** Bias (49%), Off-topic (47%), and Manipulation (45%).

[^1]: Correction (February 2026): The year-over-year percentage change in AI/ML transaction volume has been updated to reflect a revised calculation.

---

mon, but safety (64%) and business alignment (60%)
followed closely, indicating that models struggle not just with protection but with staying within
defined task and policy boundaries. Hallucination and trust failures (42%) remain widespread,
while custom, domain-specific tests (19%) also surfaced meaningful weaknesses.

Critical failures are universal
Every AI system tested failed at least once. Across all targets, 100% exhibited one or more
critical vulnerabilities. These are not rare misconfigurations or unusual deployments. They are
universal traits of enterprise AI systems today.

For security leaders, this reinforces a simple reality: no AI system is safe by default, and
continuous adversarial testing is mandatory, not optional.

Most enterprises fail on the very first test
In 72% of enterprises, the very first test executed uncovered a critical vulnerability. This shows
how quickly high-severity risks surface once systems are exposed to adversarial pressure—
most organizations don’t need hours of testing to fail; they fail immediately. For CISOs, this
underscores that critical risk is present from day one, even in mature environments, and must be
addressed with continuous testing and runtime controls.

K E Y   F I N D I N G

Our red teaming experts uncovered one or more
critical vulnerabilities in 100% of systems tested,
proving that no AI system is safe by default.

©2026 Zscaler, Inc. All rights reserved.

35

Zscaler ThreatLabz 2026 AI Security ReportCase study: What’s really breaking in enterprise AI systems

Most common successful exploits

TO P   VA R I AT I O N S   BY   FA I LU R E   R AT E

n
o
i
t
a
i
r
a
V

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

0

10

20

30

40

50

Failed %

Figure 18: Breakdown of top variations (exploit techniques that modify inputs) by

failure rate. Only variation types with ≥50 attempts are included.

S U CC E S S F U L   E X P LO I T S   C O N S I S T E N T LY   FA L L   I N TO   F O U R   C AT E G O R I E S :

1.  Data leakage: Frequent failures involving

3.  Jailbreaks and harmful content:

privacy, PII exposure, context leakage, and
Base64/translation variations show how
easily models can be induced to reveal
sensitive information.

Multimodal variations like DALL-E images,
Salt-and-pepper noise, Gaussian filters,
and mirrored images routinely bypass
safety mechanisms.

2.  Prompt injection and manipulation: High
failure rates across manipulation, off-topic
prompts, unstable Q&A, and language
or encoding variations (LeetSpeak,
Multilanguage, StringJoin) reveal
brittle guardrails that break with minor
input changes.

4.  RAG poisoning and trust failures:
Hallucination, RAG precision, and
grounding-related variations (Translate,
ImplicitVariation) show how easily retrieval
pipelines can be misled or corrupted.

Across text, image, audio, and encoded inputs, attackers succeed by
changing format, language, or structure—how a request is expressed—
revealing broad systemic weaknesses in enterprise AI systems.

Zscaler ThreatLabz 2026 AI Security Report

©2026 Zscaler, Inc. All rights reserved.

36

Case study: What’s really breaking in enterprise AI systems

Simplicity wins: the most effective attack strategies

The most effective attacks are often the least complex:

•  One-shot attacks achieve the highest failure rate (60%), with the largest sample size,

proving many systems fail without escalation or chaining.

•  Tree of Attacks, Crescendo, and Multi-Shot methods consistently degrade model

•

behavior under iterative pressure.
Even defensive-aware strategies, including retries and multi-step prompts, continue to
succeed, exploiting weaknesses in reasoning, memory, and safety alignment.

One-Shot

Tree Of Attack

Crescendo

Multi-Shot

Multi-Step

One-Shot With Retry

Delayed Attack

Jailbreak Strategy

y
g
e
t
a
r
t
S

n=135443

n=135443

n=135443

n=135443

n=135443

n=135443

n=135443

0%

20%

40%

60%

Failed %

Figure 19: Breakdown of top variations (exploit techniques that modify inputs)
by failure rate. Only variation types with ≥50 attempts are included.

W H AT   T H I S   M E A N S   F O R

S E C U R I T Y   T E A M S

This case study

demonstrates that

enterprise AI risk is

inherent and persistent.

Failures repeatedly

surface in known risk

areas and do so almost

immediately once

systems are tested.

Without continuous

testing and controls,

AI systems introduce

material risk from the
moment models are

deployed.

©2026 Zscaler, Inc. All rights reserved.

37

n=13544310%18%25%28%35%46%52%60%Zscaler ThreatLabz 2026 AI Security ReportThe Latest Phase_
of AI Governance

In 2025, the focus expanded from ethical principles and how AI should
behave to how securely it must operate. With this came new mandates
for risk controls, testing, and ongoing oversight across the globe.

Security at the center
of the EU AI Act amid
shifting timelines

U.S. AI governance
leans on standards,
not statutes

The European Union Artificial Intelligence Act remains the most
comprehensive AI regulatory framework, but implementation
timelines and enforcement expectations are in flux. In late 2025,
the European Commission proposed extending compliance
deadlines for the riskiest parts of the law, particularly high-
risk AI systems (used in healthcare, law enforcement, etc.),
to December 2027, contingent on parliament and member
states approvals.3 At the same time, new guidance and
support platforms are being rolled out to help organizations
navigate requirements such as incident reporting and
conformity assessments.4

Organizations must treat the EU AI Act not as a static
compliance deadline but as a moving target, requiring ongoing
readiness and proactive security controls.

The United States still lacks comprehensive federal AI law,
but 2025 marked a clear pivot in how the U.S. government
thinks about AI: national competitiveness first, with security
and governance routed through standards and agency policy
rather than broad regulation. The National Institute of Standards
and Technology (NIST) continues to lead adoption of the AI
Risk Management Framework5 as the baseline for secure
development, adversarial testing, and operational assurances.

In December 2025, the Administration issued an executive order
aimed at preempting or challenging state AI laws that conflict
with a national AI policy framework and directing agencies
to pursue federal standards and litigation where necessary.6
Despite this, several states (including New York)7 continue to
advance their own AI safety laws, underscoring that U.S. AI
regulation in 2026 will involve navigating a complex federal-
state policy environment.

3  Reuters, EU to delay ‘high risk’ AI rules until 2027 after Big Tech pushback, November 19, 2025.
4   European Commission, Commission launches AI Act Service Desk and Single Information Platform to support AI Act implementation, October 8, 2025.
5   NIST, AI Risk Management Framework.
6   Axios, Executive order targeting state AI laws, December 11, 2025.
7   Axios, N.Y. Gov. Kathy Hochul signs sweeping AI safety bill, December 19, 2025.

38

©2025 Zscaler, Inc. All rights reserved.Zscaler ThreatLabz 2026 AI Security Report©2026 Zscaler, Inc. All rights reserved.Zscaler ThreatLabz 2026 AI Security ReportAPAC accelerates secure AI adoption

Across the Asia-Pacific region, governments
continue to advance AI strategies that explicitly
link rapid adoption with security and resilience.
Many APAC economies are emphasizing practical
governance frameworks and risk-based controls
that can scale alongside AI deployment.

Japan took a major step in 2025 with the
passage of its first comprehensive AI law, the
AI Promotion Act,8 in May 2025, establishing
a national blueprint that promotes AI R&D and
deployment while formally recognizing the need
to manage associated risks.

India followed with its 2025 AI Governance
Guidelines,9 a broad framework aimed at
“Safe and Trusted AI.” These guidelines tie AI
adoption closely to the country’s Digital Public
Infrastructure and set expectations for data
governance, algorithmic transparency, and risk
management, particularly for large-scale public
services and financial systems.

Singapore continued to mature its AI governance
ecosystem through 2025, expanding its AI Verify
testing framework and related GenAI assurance
initiatives,10 shifting further toward continuous
testing, monitoring, and assurance.

Australia also advanced its approach through
Guidance for AI Adoption released in October
202511 alongside its Safe and Responsible AI
agenda—efforts that emphasize guardrails,
testing, and stronger oversight for higher-risk
deployments, particularly in regulated sectors.

With several substantial 2025 frameworks
moving forward in parallel, APAC is increasingly
positioning itself as a global leader in pragmatic,
security-first AI innovation and adoption.

8   IT Business Today, Japan’s AI Regulation is a Significant Step Forward with the AI Promotion Act, October 29, 2025.
9   AI, Data & Analytics Network, India unveils new AI governance guidelines to encourage responsible adoption, November 6, 2025.
10  IMDA, Singapore launches new tools to help businesses protect data and deploy AI in a trusted ecosystem, July 7, 2025.
11  Australian Government, DISR, Guidance for AI Adoption, October 21, 2025.

Expectations for AI security should rise

sharply in 2026. Even as global and regional

governance evolve—and enforcement

remains uneven—organizations will need to

take ownership of securing their AI adoption.

Policymakers may push for evidence-based

controls, but converging frameworks alone

won’t reduce risk. AI success will ultimately
depend on internal security discipline.

Organizations that implement zero trust,

continuously test models, and monitor for

evolving threats will be best positioned to

deploy AI responsibly.

©2026 Zscaler, Inc. All rights reserved.

39

Zscaler ThreatLabz 2026 AI Security ReportZscaler ThreatLabz 2026 AI Security ReportAI Security
Predictions for 2026

1

2

Autonomous and human
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

Attacks on the AI supply chain will target the core components that power
enterprise AI systems. ThreatLabz discoveries in 2025 exposed how
weaknesses in common model files and processing layers could be used to
access sensitive systems. Attackers will increasingly focus on tampering with
the underlying pieces of AI (models and datasets) rather than only misusing
AI at the application level. As more organizations import third-party AI
components into their environments, compromising these foundational
elements will provide powerful access. Securing the AI supply chain will
remain as important as securing the application built on top of it.

40

©2025 Zscaler, Inc. All rights reserved.Zscaler ThreatLabz 2026 AI Security Report©2026 Zscaler, Inc. All rights reserved.Zscaler ThreatLabz 2026 AI Security Report3

Embedded AI security risks

5

Fraudulent AI embedded in
enterprise workflows

Embedded AI inside everyday applications will introduce hidden access that
traditional security tools may overlook. AI features built directly into popular
business applications, cloud platforms, and mobile tools—think Zoom’s AI
meeting summaries or Microsoft 365 Copilot assistant—will create subtle
risks that are easy to miss. These embedded AI capabilities often have broad
access to sensitive content, making them attractive targets for misuse.
Enterprises should expect attackers to increasingly try to exploit these
built-in functions to exfiltrate valuable intel or gain access and move quietly
within an environment, taking advantage of the fact that many organizations
still lack full visibility into where AI has been embedded in the software
supply chain.

Deceptive AI services and platforms will shift from isolated scams to deeply
embedded footholds inside business workflows. The steady rise of AI tool
adoption in 2025 has already shown how easy it is for malicious AI services
to slip into real workflows. Expect attackers to move beyond fake AI landing
pages and begin releasing full-featured malicious copilots that act like real
productivity assistants while blending into everyday use. This next phase will
make rogue assistants harder to spot, contributing greatly to the risks from
unapproved or shadow AI used by enterprise employees.

4

Ransomware & nation-state
attacks on GenAI data stores

6

Enterprise-wide AI security
and accountability

As enterprises move from GenAI pilots to full deployments in 2026, far more
internal systems will funnel sensitive information into AI-driven workflows.
Attackers will take advantage of this shift by targeting the data stores
behind GenAI applications. These stores contain more than raw data, but
also context and intent, giving adversaries far greater visibility into internal
decision cycles—and, as a result, more leverage than most traditional
breaches offer. Compromising LLM data stores will become a high-yield
tactic for espionage and ransomware extortion in the year ahead.

AI security will become an enterprise-wide requirement as oversight and
accountability increase. After a year of high-profile concerns and growing
scrutiny in 2025, organizations face mounting expectations around how they
manage AI: how models are vetted, how data is handled, and how potential
misuse is monitored. Securing AI systems in 2026 will no longer be optional
or limited to technical teams. Leadership will need clear visibility into AI risk,
and security policies need to extend across every part of the business that
interacts with AI.

41

©2025 Zscaler, Inc. All rights reserved.Zscaler ThreatLabz 2026 AI Security Report©2026 Zscaler, Inc. All rights reserved.Zscaler ThreatLabz 2026 AI Security ReportBest_Practices:
Secure Enterprise
AI Adoption

5 hard truths of AI security in 2026

1

2

3

4

5

You can’t secure what you can’t see. Shadow AI and embedded
AI functionality make visibility the new perimeter.

Vendor defaults aren’t built for enterprise risk. AI features
often ship “on” and overly permissive.

AI governance is a moving target. Policies must evolve as
capabilities and threats shift.

Zero trust now extends to AI models. They require the same
level of access control as human users.

AI is an undeniable part of the attack surface. Model
vulnerabilities and agentic AI attacks are here.

The good news: you don’t have to accept these

“hard truths” as the cost of AI adoption. Use the

2026 enterprise security checklist that follows to

prioritize the right protections first.

Zscaler ThreatLabz 2026 AI Security Report

©2026 Zscaler, Inc. All rights reserved.

42

©2025 Zscaler, Inc. All rights reserved.2026 enterprise
AI security checklist

The following best practices establish a strong baseline for secure AI use.

Enterprises should also define governance standards and rules of
engagement for how AI is adopted and managed.

Inventory all GenAl apps and apps with embedded
AI functionality

Enforce AI guardrails with
inline inspection

Update AI governance often

Conduct adversarial testing and model red teaming

•  Create a continuously updated catalog of
every standalone GenAl tool and every
SaaS or internal app that includes AI
functionality or features.

•

Ensure inline inspection across all AI/ML
traffic to prevent external malicious activity
from compromising AI systems and stop
sensitive data from being exposed via
prompts or in outputs.

•

Refresh policies, access controls, and
risk classifications regularly to keep pace
with rapid changes in AI capabilities and
regulatory requirements.

•  Continuously test models for jailbreaks,

prompt injection, data leakage, and other
exploitable weaknesses before attackers
find them.

Disable risky AI defaults

Validate model lineage and supply chain

Mandate human review for regulated workflows

Secure the AI development lifecycle end-to-end

•  Turn off auto-enabled AI functionality in

•  Verify model provenance, updates,

•

SaaS and productivity apps until they have
been reviewed and configured to match
your risk posture.

datasets, and dependencies of every model
to reduce risk from tampering, poisoning,
or compromised components.

Ensure humans remain in the loop
wherever AI influences decisions tied to
safety, compliance, financial decisions, or
public sector determinations.

•  Apply controls from dataset ingestion
through training, deployment, and
monitoring to prevent vulnerabilities from
entering production systems.

Apply zero trust to all model interactions

•

Implement least-privilege access for every
user, service, and system that interacts
with an AI model.

©2026 Zscaler, Inc. All rights reserved.

43

Zscaler ThreatLabz 2026 AI Security ReportHow enterprises are
safely rolling out GenAI:
a real-world playbook

AI risk came from both sides of the enterprise boundary in 2025. Threat actors
used GenAI to accelerate and facilitate their operations, while internal exposure
increasingly stemmed from everyday AI use without formal oversight—allowing
data to reach AI systems before security teams could assess or control the risk.

Their real-world playbook looks like this:

The organizations that avoided incidents were the

ones that introduced GenAI in controlled phases and

enabled only what they could govern.

B E G I N  W I T H   A   Z E R O   T R U S T   S TA N C E   A N D

H O S T   A P P R OV E D   G E N A I   TO O L S   I N   A   P R I VAT E,

R E S T R I C T   U N V E T T E D   A I   S E RV I C E S

C O N T R O L L E D   E N V I R O N M E N T

Countless AI tools introduce unknown data handling and
security risks, making it critical to start from a zero trust
position. Blocking or limiting access to unvetted AI/ML
applications removes immediate exposure and prevents
early data leakage, giving security teams the space to
assess which apps are appropriate for enterprise use.

To keep full control over enterprise data, organizations should run approved GenAI
tools in a private and secure environment, such as a dedicated tenant or isolated
instance managed entirely by the company. This setup ensures that neither the vendor
nor third parties can access internal or customer data and prevents prompts and
outputs from being used to train public models. Operating GenAI this way preserves
data sovereignty and keeps sensitive information from leaving the organization.

I D E N T I F Y   A N D   VA L I DAT E   T H E   G E N A I   A P P L I C AT I O N S

E N F O RC E   S T R O N G   I D E N T I T Y   A N D

T H AT   M E E T   E N T E R P R I S E   R E QU I R E M E N T S

ACC E S S   C O N T R O L S

Determine which GenAI apps are safe to use by
checking how they handle data, whether they keep
your information isolated, how the model was built, and
whether the vendor meets your security, privacy, and
compliance requirements. Only tools that satisfy these
standards should move forward.

Place approved GenAI apps behind a zero trust
architecture with granular access policies. This ensures
each user, department, and workflow receives only the
access needed, while giving security teams end-to-
end visibility and control over all activity.

A P P LY   DATA   P R OT E C T I O N   TO   P R E V E N T

ACC I D E N TA L   O R   U N AU T H O R I Z E D   S H A R I N G

Pair approved access with enterprise-grade DLP.
Monitoring and inspecting traffic to and from
AI apps ensures sensitive information remains
contained and that no critical data is exposed
through interactions with these apps.

©2026 Zscaler, Inc. All rights reserved.

44

Zscaler ThreatLabz 2026 AI Security ReportHow Zscaler Delivers_
Comprehensive AI Protection

Securing AI at scale requires a different approach
that reduces exposure by default, continuously
verifies access, and applies security controls
wherever AI is used or built. Zero trust provides
that foundation.

Zscaler delivers an AI security platform built on
zero trust that secures AI everywhere—across
how organizations use, build, and operate AI.
By shrinking the attack surface, enforcing least-
privileged access, and inspecting all traffic inline,
Zscaler helps organizations adopt AI securely
without slowing innovation.

The findings in this report confirm that
enterprise AI adoption is accelerating fast. As a
result, an expanding attack surface, shadow and
embedded AI usage, and constantly evolving
models and infrastructure are introducing
new risks around data exposure, misuse, and
governance that legacy security approaches
cannot effectively address.

Security architectures built on firewalls, VPNs,
and perimeter-based controls were not designed
or intended for dynamic AI environments. In
practice, they add complexity and leave gaps
in visibility. They struggle to enforce consistent
controls across public AI tools, agents, private
models, and emerging components like Model
Context Protocol (MCP) servers.

Organizations are left reacting to AI risk rather
than managing it proactively.

©2026 Zscaler, Inc. All rights reserved.

45

©2025 Zscaler, Inc. All rights reserved.Zscaler ThreatLabz 2026 AI Security ReportTurning AI risk into
secure AI adoption

With zero trust as the foundation, Zscaler applies AI-native security controls that translate architecture into action.
These capabilities give organizations the visibility, guardrails, and protections needed to govern AI usage in real time-
while actively disrupting AI-powered threats across users, applications, and infrastructure.

Zscaler AI empowers organizations to:

S E C U R E LY   E N A B L E   P U B L I C   A N D   P R I VAT E   A I   U SAG E

S TAY   A H E A D   O F   A I - P OW E R E D   T H R E AT S

•

See exactly where and how AI is being used, including AI applications,
models, agents, prompts, responses, and emerging components such as
MCP servers.

•  AIlow employees to use AI tools productively while isolating risky

web-based AI interactions and preventing sensitive data from being
unintentionally shared with external models.

•  Detect and block prompt injection, PII exposure, data poisoning, unsafe

•

•

Reduce exposure by eliminating the external attack surface and enforcing
continuous verification and least-privileged access.

Inspect all traffic, including encrypted traffic, to block AI-enhanced threats in
real time.

•  Apply predictive and generative AI to surface risks faster and improve

security operations and response.

outputs, and other AI-specific threats at runtime with built-in AI guardrails.

•  Continuously discover, classify, and protect sensitive data across endpoints,

•  Control who can use AI, which tools they can access, and how AI is used
with policies that adapt continuously to user, device, and application risk,
automatically blocking unauthorized or shadow AI.

inline traffic, and cloud environments.

•

Stop lateral movement with AI-powered segmentation that limits
attacker reach.

•

Prevent sensitive data from being sent to or returned from AI tools using
inline, AI-aware DLP controls.

•  Continuously assess AI and zero trust posture with AI-generated insights

and recommendations.

•  Maintain a detailed, searchable audit trail of AI activity to support

investigations and compliance.

These outcomes are delivered through a unified set of protections that span the AI security lifecycle, as covered in the section that follows.

46

©2025 Zscaler, Inc. All rights reserved.Zscaler ThreatLabz 2026 AI Security Report©2026 Zscaler, Inc. All rights reserved.Zscaler ThreatLabz 2026 AI Security ReportZscaler + AI: securing how
organizations use and build apps

Zscaler offers comprehensive protection—from discovery and risk assessment to securing AI
applications and access—covering public and private AI, models, pipelines, agents, and infrastructure.

A I   AS S E T

M A N AG E M E N T

S E C U R E   ACC E S S

TO   A I   A P P S

S E C U R E   A I   A P P L I C AT I O N S   A N D

I N F R AS T R U C T U R E

Discover your full
AI footprint and risks

Ensure the safe and responsible
use of AI applications

Harden AI systems and prompts
and enforce runtime protection

Full visibility into all applications,
models, pipelines, and MCP servers.

An AI-BOM to uncover supply chain
and dependency risks.

Identification of high-risk GenAI SaaS
applications and AI models.

Granular control over which users can
access which apps.

Vulnerability detection in models
and pipelines.

Inline inspection of prompts and
responses to prevent sensitive data
from being sent or returned.

Content controls to block unsafe or
harmful outputs.

Red team testing to identify exposure
and weaknesses.

Protection from prompt injections, data
poisoning, use of sensitive data, etc.

AI Governance: Stay compliant with AI frameworks via mapping of AI security controls to NIST AI Risk Management Framework and the EU AI Act.

Zscaler ThreatLabz 2026 AI Security Report

©2026 Zscaler, Inc. All rights reserved.

47

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

Follow us: X @ThreatLabz  |  ThreatLabz security research blog

©2026 Zscaler, Inc. All rights reserved.

48

Zscaler ThreatLabz 2026 AI Security ReportAbout Zscaler
Zscaler (NASDAQ: ZS) accelerates digital transformation so customers can be more agile, efficient, resilient, and
secure. The Zscaler Zero Trust Exchange™ platform protects thousands of customers from cyberattacks and data
loss by securely connecting users, devices, and applications in any location. Distributed across more than 150 data
centers globally, the SSE-based Zero Trust Exchange™ is the world’s largest in-line cloud security platform. Learn
more at zscaler.com or follow us on Twitter @zscaler.

© 2026 Zscaler, Inc. All rights reserved. Zscaler™ and other trademarks listed at zscaler.com/legal/trademarks are either (i) registered
trademarks or service marks or (ii) trademarks or service marks of Zscaler, Inc. in the United States and/or other countries. Any other
trademarks are the properties of their respective owners.

+1 408.533.0288

Zscaler, Inc. (HQ) • 120 Holger Way • San Jose, CA 95134

zscaler.com

Zero Trust Everywhere