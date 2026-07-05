# Global Threat Intelligence Report 2026

## Table of Contents
- [Executive Summary](#executive-summary)
- [The 2025 Intrusion Model](#the-2025-intrusion-model)
- [How Vulnerability Exploitation Shifted into Business-Critical Systems](#how-vulnerability-exploitation-shifted-into-business-critical-systems)
- [Identity, Supply Chain, and Operational Disruption in Major Incidents](#identity-supply-chain-and-operational-disruption-in-major-incidents)
- [Tactics and Intrusion Patterns That Shaped Attacker Success](#tactics-and-intrusion-patterns-that-shaped-attacker-success)
- [How Collaboration, Scale and Identity Abuse Shaped the Adversary Landscape](#how-collaboration-scale-and-identity-abuse-shaped-the-adversary-landscape)
- [Geopolitical Tension and Cyber Spillover in 2025](#geopolitical-tension-and-cyber-spillover-in-2025)
- [Top Attack Indicators](#top-attack-indicators)
- [2026 Predictions](#2026-predictions)

---

## Executive Summary

Cyber activity in 2025 reflected a decisive shift in how modern intrusions are conducted and scaled. Rather than relying on novel malware or perimeter exploitation alone, threat actors increasingly combined speed, coordination, and identity abuse to turn initial access points into high-impact incidents. Vulnerability exploitation remained a dominant entry vector, with a 17% increase from 2024 comparatively, but the year was defined by how quickly disclosed flaws were weaponized and how often the same vulnerabilities were exploited in parallel by state-aligned and criminal actors.

Enterprise platforms—ERP systems, collaboration servers, identity services, and SaaS ecosystems—became preferred targets because compromise translated immediately into privileged access, operational disruption, and leverage over regulated data.

**Cyber Incidents by the Numbers[^1]:**
- **United States (31,020):** Recorded 31,020 cyber incidents in 2025, making it the most targeted country by a large margin.
- **Germany (7,144):** Reported 7,144 incidents, representing a significant portion of Europe’s total cyberattack volume.
- **United Kingdom (2,622):** Logged 2,622 cyber incidents, reflecting persistent targeting in financial, telecom, and retail sectors.
- **Canada (2,581):** Saw 2,581 reported attacks, closely aligned with broader North American threat activity.

Across the year’s most significant cyber events, consistent patterns emerged:
- SaaS supply-chain abuse allowed attackers to pivot across hundreds of organizations without exploiting core platforms directly.
- Ransomware campaigns increasingly targeted operational continuity rather than encryption alone.
- AI-enabled automation accelerated phishing, payload generation, and attack execution at scale.
- In sectors such as retail, automotive, aviation, and manufacturing, cyber incidents produced tangible economic effects.

---

## The 2025 Intrusion Model

![Diagram showing the 2025 Intrusion Model: Rapid Social Engineering -> Valid Credentials -> Lateral Movement -> Disruption/Data Exfiltration]

These trends show that identity, cloud, and SaaS are now the primary targets for attacks, accounting for about 22% of incidents.[^6]

---

## How Vulnerability Exploitation Shifted into Business-Critical Systems

Vulnerability exploitation remained one of the most dominant intrusion vectors in 2025. Across observed intrusions, vulnerability exploitation accounted for an estimated 25–35% of successful ransomware incidents.

### Unauthenticated ERP RCE Enables Deep SAP NetWeaver Compromise
(SAP NetWeaver – CVE-2025-31324, CVSS 10.0)
CVE-2025-31324 became one of the year’s defining ERP vulnerabilities because it allowed unauthenticated remote code execution on SAP NetWeaver systems. Multiple Chinese threat actors—including Chaya004 and Cotton Sandstorm—weaponized the flaw rapidly.

### SharePoint RCE Turns Collaboration Servers into Identity Gateways
(Microsoft SharePoint – CVE-2025-53770, CVSS 9.8)
Attackers abused the `ToolPane.aspx` endpoint for remote code execution, deployed web shells, and extracted machine keys. More than 400 organizations were impacted globally.

### Cl0p Zero-Day Exploitation of Oracle ERP Core Systems
(Oracle E-Business Suite – CVE-2025-61882, CVSS 9.8)
Cl0p adopted this flaw as a zero-day against Oracle E-Business Suite, enabling remote code execution deep inside ERP modules responsible for HR, finance, and supply-chain operations.

---

## Identity, Supply Chain, and Operational Disruption in Major Incidents

### Salesforce Ecosystem and OAuth Supply-Chain Breaches
The wave of intrusions affecting Salesforce and its connected SaaS ecosystem was driven primarily by ShinyHunters, with involvement from Scattered Spider and LAPSUS$. Rather than exploiting Salesforce itself, actors abused OAuth integrations and connected apps (e.g., Salesloft’s Drift, Gainsight) to obtain legitimate API access.

### The JLR Cyber Incident Reshaped Automotive Sector Weaknesses
Jaguar Land Rover (JLR) experienced a major cyber incident that disrupted core digital systems supporting vehicle production, forcing manufacturing shutdowns. The incident highlighted how dependency on shared digital infrastructure has become a primary operational risk for automotive manufacturers.

### Retail Sector Attacks and the Expansion of Identity-Driven Extortion
During Q2 2025, ransomware incidents in the global retail sector increased by 58% quarter over quarter. Attacks on Marks & Spencer, Harrods, and Co-op were characterized by identity compromise, where attackers manipulated IT personnel into resetting credentials to bypass MFA.

---

## Tactics and Intrusion Patterns That Shaped Attacker Success

### IT Staff Impersonation
Impersonating IT staff became a core initial-access vector. Scattered Spider practitioners convinced help-desk teams to reset MFA tokens or grant remote access through tools like Quick Assist.

### Ransomware’s Shift Toward AI-Enabled Automation
Around 80% of ransomware campaigns incorporated AI at some stage of the attack lifecycle. The emergence of **PromptLock**—the first AI-directed proof-of-concept—demonstrated how LLMs could autonomously create dynamically changing ransomware payloads.

### How ClickFix Turned Verification Prompts Into Infection Paths
ClickFix activity increased by over 500% in 2025, representing 8% of blocked attack attempts. It uses fake CAPTCHAs and verification prompts to push users into executing malicious scripts.

---

## How Collaboration, Scale and Identity Abuse Shaped the Adversary Landscape

### The Scattered LAPSUS$ Hunters Collective
A loose but highly active collective drawing from a pool of young English-speaking SIM-swappers and social engineers. They utilized a repeatable playbook: reconnaissance of high-privilege employees and aggressive social engineering to hijack help-desk workflows.

### The LockBit, DragonForce, and Qilin Ecosystem
These groups functioned less as discrete entities and more as a shared operating environment, characterized by shared tooling, overlapping affiliate networks, and the continued influence of leaked Conti v3 source code.

---

## Geopolitical Tension and Cyber Spillover in 2025

- **India–Pakistan:** Cyber operations became an immediate extension of geopolitical crises, with nationalist hacktivism combined with targeted APT activity (e.g., APT36).
- **Israel–Iran:** The June 13, 2025, "Operation Rising Lion" marked a direct alignment of kinetic action and cyber escalation, including GPS-spoofing and attacks on financial infrastructure like Bank Sepah.
- **Russia–Ukraine:** Ukraine’s CERT handled more than 3,000 incidents in the first half of 2025. Russian campaigns (e.g., Sandworm) were synchronized with missile and drone strikes.

---

## Top Attack Indicators

| Category | Details |
| :--- | :--- |
| **Top Attack Vectors** | Phishing, NPM supply chain attacks, SEO poisoning, Identity-based attacks, Vulnerability exploitations |
| **Top Ransomware** | Qilin, Akira, Cl0p, Play, INCransom |
| **Top Malwares** | Asyncrat, Remcos, Vidar, Xworm, OysterLoader |
| **Top LOLBins** | PowerShell, Mshta, Certutil, Schtasks.exe, Wmic.exe |
| **Top Abused RMMs** | AnyDesk, UltraVNC, MeshAgent, ScreenConnect, LogMeIn |

---

## 2026 Predictions

1. **Cyber criminals will have a tactical advantage with AI:** Attackers leveraging AI do not need the same level of precision as defenders. The rapid adoption of agentic AI compounds this challenge, as these autonomous agents mimic human behavior, blurring the line between legitimate and malicious activity. Organizations that fail to rethink identity access management and privilege models for an AI-driven environment will expose themselves to systemic vulnerabilities.

[^1]: Data based on CyberProof 2025 incident tracking.
[^2]: Retail sector ransomware statistics, Q2 2025.
[^3]: Global retail cyberattack survey, 2025.
[^4]: Manufacturing sector attack volume analysis, 2025.
[^5]: Education sector ransomware report, H1 2025.
[^6]: Identity, cloud, and SaaS incident attribution study.
[^7]: Vulnerability weaponization speed analysis.
[^8]: SAP NetWeaver CVE-2025-31324 impact report.
[^9]: Microsoft SharePoint CVE-2025-53770 campaign analysis.
[^10]: Oracle E-Business Suite CVE-2025-61882 extortion analysis.
[^11]: JLR incident government impact assessment.
[^12]: UK economic impact of cyber incidents, 2025.
[^13]: UK retail sector cyber incident report.
[^14]: Scattered Spider/ShinyHunters/LAPSUS$ activity report.
[^15]: Marks & Spencer incident financial impact analysis.
[^16]: Luxury retail extortion trends, 2025.
[^17]: UK government cybersecurity breach survey, 2025.
[^18]: Collins Aerospace ransomware incident report.
[^19]: Aviation sector passenger data breach analysis.
[^20]: Korean Air/KLM-Air France third-party incident report.
[^21]: Scattered Spider/ShinyHunters/LAPSUS$ leak site monitoring.
[^22]: Indian airport GPS-spoofing incident report.
[^23]: Microsoft Teams impersonation vulnerability report.
[^24]: AI-enabled ransomware lifecycle study.
[^25]: KillSec AI-tooling usage report.
[^26]: Funklocker AI-ransomware deployment analysis.
[^27]: IntelBroker media interview analysis.
[^28]: ClickFix browser-based social engineering study.
[^29]: Scattered LAPSUS$ Hunters Collective formation report.
[^30]: Conti v3 source code influence analysis.
[^31]: LockBit/DragonForce/Qilin collaboration announcement.
[^32]: Kimsuky/Lazarus operational integration report.
[^33]: Russian/North Korean APT operational alignment study.
[^34]: ShinyHunters extortion demand analysis.
[^35]: Qilin ransomware volume report.
[^36]: Qilin leak site activity monitoring, Nov 2025.
[^37]: India-Pakistan cyber conflict timeline.
[^38]: Bank Sepah/Nobitex attack analysis.
[^39]: Israel-Iran cyber-kinetic escalation report.
[^40]: Ukraine CERT incident volume report.
[^41]: Ukrainian Railways ticketing system disruption analysis.

---

ffectively monitor or control AI agents, creating blind spots that adversaries will
exploit. In short, unless security leaders shift their mindset from reactive defense to proactive risk prioritization, cybercriminals
will dominate the battlefield in 2026, leveraging AI to outpace and outmaneuver traditional security paradigms.
Confidential and Proprietary. © 2026 CyberProof 40

2
The Rise of Vishing, Deepfakes, and Identity Deception
The convergence of voice-based social engineering and artificial intelligence is set to define a new era of attacks in 2026,
with a significant rise predicted in vishing attacks embedding deepfake technology. The second half of 2025 saw a
noticeable increase in vishing attacks leveraging platforms like Microsoft Teams . The introduction of features like "Chat with
anyone" on Teams, which allows contact between individuals across different tenants, creates a critical new attack vector. An
attacker can easily impersonate a trusted entity, such as an IT staff member, to initiate a social engineering attack.
The attack sequence, which is becoming dangerously efficient with deepfake components and the condensed time to
execute, usually looks similar to this:
Initial Contact: The attacker contacts an employee via the collaboration platform and sends a malicious URL.
Credential Theft: The link prompts for credentials and subsequently attempts to install an RMM tool—again,
weaponizing legitimate software.
Lateral Movement and Deception: If successful, the attacker gains remote access. To further manipulate the victim
and their colleagues, the attacker introduces deepfake technology. This highly convincing impersonation can be
used to instill a false sense ofsecurityso the victim will authorize fraudulent transactions, or provide further access,
This combination of vishing and deepfake technology is predicted to dramatically reduce the overall attack time and
accelerate data exfiltration and financial theft by rapidly enabling lateral movement and manipulating human
verification safeguards.
Confidential and Proprietary. © 2026 CyberProof 41

3
Cloud Misconfigurations
Settings will Persist
In 2026, cloud misconfigurations will continue to be a
leading cybersecurity threat, despite increasing
awareness and investment in cloud security. As
organizations expand their use of complex, multi-cloud
environments, the overall attack surface grows—
introducing more potential entry points and
vulnerabilities than ever before.
The risk of human error—such as misconfigured settings
and insecure APIs—will persist as a primary entry point
for attackers. The ongoing challenge of managing these
dynamic and sprawling cloud ecosystems means that
misconfiguration is expected to remain the top cause of
cloud-related breaches next year.
CCoonnffiiddeennttiiaall aanndd PPrroopprriieettaarryy.. ©© 22002266 CCyybbeerrPPrrooooff 4422

4
Increasing Use of Regulatory
Exposure as Deliberate Leverage
In 2026, we expect extortion groups to increasingly use
regulatory exposure as deliberate leverage. After the
major consumer-facing breaches and stricter reporting
rules that followed, attackers have realized that the
threat of investigations, fines, and public scrutiny can be
more damaging to organizations than the breach itself.
Ransom notes are already referencing GDPR, UK
reporting timelines, and sector-specific disclosure rules,
with some groups threatening to notify regulators
directly or leaking small data samples to force
mandatory reporting. This turns compliance obligations
into an attack surface: the pressure doesn’t only come
from encrypted systems or stolen data, but from the
legal and reputational consequences adversaries now
know how to exploit.
CCoonnffiiddeennttiiaall aanndd PPrroopprriieettaarryy.. ©© 22002266 CCyybbeerrPPrrooooff 4433

5
The Blurring Lines: Abuse of Legitimate Software
The year 2026 is projected to see a continued surge in the abuse of legitimate software, particularly Remote Management
and Monitoring (RMM) tools. Attackers are successfully turning these necessary administrative utilities into powerful
conduits for their campaigns, allowing them to gain "hands-on-keyboard" access to target environments.
This technique is highly effective because RMM tools are often trusted, whitelisted, and essential for business
operations. Once control is established, attackers perform reconnaissance and collect critical user and machine
information, setting the stage for devastating, later-stage attacks, most notably extortion (ransomware) campaigns.
Some illustrative case studies we’ve seen this year includes:
RMM Vulnerability Exploitation: In February 2025, a vulnerability in SimpleHelp RMM was reported. While the initial
discovery protected some clients, a subsequent campaign around May 2025 saw the DragonForce ransom cartel
successfully abuse this vulnerability to attack a Managed Service Provider (MSP) in the UK, highlighting the speed at
which exploits move from discovery to weaponization. 42
Supply Chain Subversion: Further demonstrating the challenge of software trust, CyberProof researchers identified
ConnectWise ScreenConnect binaries with valid digital signatures making outbound connections to suspicious
command-and-control (C2) servers.43 This attack involved Authenticode Stuffing—injecting malicious code while
preserving the integrity of the original signature. Although the certificate was later revoked, these backdoored
droppers were subsequently used by other threat actors to distribute infostealers, underscoring the risk of
compromised software integrity.
Confidential and Proprietary. © 2026 CyberProof 44

6 Shadow AI will emerge as the next unmanaged risk surface
As enterprises continue to rush to harness generative AI, many are discovering that their greatest risk may lie not in
external attacks but in potential exposures due to ungoverned internal use. Employees are increasingly adopting
personal or unvetted AI tools to accelerate daily tasks, introducing the idea of shadow AI. Without clear policies on data
access, model usage, and output validation, sensitive information can easily be exposed or misused.
The KPMG AI Security Benchmark Survey found that a significant portion of organizations lack defined AI vulnerability
processes, incident-response playbooks or resilience plans.44 In 2026, this unmanaged layer will grow as generative
models become embedded in productivity platforms and code environments. In addition, while existing policies have
been well developed over the past decade to ensure that wider technologies and tools are well-integrated and subject to
approval processes, the sheer volume of the logs creates a serious visibility challenge, taking many companies back to
square one in regards to shadow IT. Forward-looking organizations will respond by embedding AI-governance controls
into existing cyber and data-protection programs, treating model access, prompt integrity, and data lineage as core
exposure-management priorities.
Confidential and Proprietary. © 2026 CyberProof 45

Recommendations for Improving Cyber Readiness
1 Treat Identity as the Primary 2 Harden Help-Desk and IT
Security Control Plane Support Workflows Against
Social Engineering
The majority of high-impact incidents in 2025
began with attackers operating as legitimate users
Repeated breaches across retail, aviation, and enterprise
rather than exploiting technical defenses.
SaaS environments demonstrated that IT support
Organizations should prioritize identity assurance
functions have become a preferred intrusion vector.
as a core security discipline, with continuous
validation of user behavior, privilege use, and
MFA reset procedures, account recovery processes, and
authentication context across cloud, SaaS, and
remote-support approvals should be treated as high-risk
on-prem environments. Controls designed solely
transactions and protected with strict verification
to protect network perimeters or endpoints are no
requirements, escalation controls, and monitoring.
longer sufficient when attackers can bypass them
Organizations should assume that attackers will
through credential abuse, OAuth misuse, or help-
impersonate internal IT staff and design workflows
desk manipulation.
accordingly, rather than relying on informal trust or
speed-of-service incentives.
CCoonnffiiddeennttiiaall aanndd PPrroopprriieettaarryy.. ©© 22002266 CCyybbeerrPPrrooooff 4466

| 3   | Enforce Governance and  | 4   | Reduce Single-Point           |
| --- | ----------------------- | --- | ----------------------------- |
|     | Visibility Over SaaS    |     | Dependency Risk in            |
|     | Integrations and OAuth  |     | Third-Party and Supply-Chain  |
|     | Access                  |     | Systems                       |
OAuth abuse and connected-app compromise  Incidents across automotive manufacturing, aviation,
enabled attackers to access hundreds of  and food retail highlighted how disruption of a single
organizations without exploiting core platforms  vendor or shared service can cascade across entire
in 2025. Enterprises should maintain continuous  ecosystems. Organizations should identify third-party
visibility into SaaS integrations, enforce least- platforms that support operational continuity—such
privilege API access, and regularly audit token  as production scheduling, logistics, identity services,
scope, duration, and usage patterns.  or customer-facing systems—and incorporate them
into resilience planning, incident response exercises,
Token revocation, application allow listing, and  and contractual security requirements.
behavioral monitoring of API activity should be
treated as standard controls, not incident- Cyber risk management should explicitly account for
response measures. operational blast radius, not just data exposure.
Confidential and Proprietary. © 2026 CyberProof 4477

5 Prepare for Ransomware Monitor and Respond to
6
That Prioritizes Disruption Narrative and Reputation-Based
Over Encryption Extortion
Threat actors increasingly integrated media outreach,
Ransomware campaigns in 2025 increasingly
leak-site signaling, and public messaging into their
focused on operational pressure rather than
extortion strategies. Organizations should treat
file encryption alone. Defensive planning
narrative control as part of incident response, with
should account for scenarios where attackers
predefined processes for monitoring attacker
steal data, disrupt services, or manipulate
communications, coordinating legal and
systems without deploying traditional
communications teams, and managing public
ransomware payloads.
disclosure timelines.
Backup strategies, recovery testing, and
Ignoring attacker-driven narrative escalation can
incident response playbooks must address
amplify operational and regulatory impact even when
partial outages, identity compromise, and SaaS
technical containment is achieved.
disruption—not just encrypted endpoints.
Confidential and Proprietary. © 2026 CyberProof 4488

7 Align Cyber Preparedness
With Geopolitical Risk
Exposure
Cyber activity in 2025 repeatedly escalated
alongside geopolitical conflict, with spillover
affecting organizations far beyond conflict zones.
Enterprises operating in sensitive sectors or
regions should integrate geopolitical risk into
threat modeling, monitoring, and response
planning.
This includes anticipating hacktivist surges, state-
aligned opportunistic targeting, and increased
exploitation of exposed systems during periods of
political unrest or military escalation.
CCoonnffiiddeennttiiaall aanndd PPrroopprriieettaarryy.. ©© 22002266 CCyybbeerrPPrrooooff 4499

Conclusion
What distinguished 2025 was not the emergence of
entirely new threats, but the efficiency with which
existing ones were executed and replicated.
The events and trends of 2025 illustrate a threat landscape
Collaboration among threat actors, the
that has matured in both structure and intent. Attackers no
industrialization of extortion, and the systematic
longer rely on isolated exploits or single-point
targeting of enterprise platforms transformed cyber
compromises; instead, they blend vulnerability exploitation,
incidents into business-level crises with regulatory,
social engineering, identity abuse, and supply-chain
financial, and geopolitical implications. At the same
leverage into cohesive intrusion models designed for scale
time, ongoing geopolitical conflicts demonstrated
and speed. The rapid combination of state-aligned and
how cyber operations are now routinely integrated
criminal tradecraft has reduced defenders’ margin for error,
with physical and political pressure, reinforcing their
turning newly disclosed vulnerabilities and trusted access
role as a permanent feature of modern conflict.
paths into immediate strategic risks.
As organizations move forward, the lessons of 2025
are clear. Security strategies built primarily around
perimeter defense and reactive patching are no
longer sufficient. Trust relationships, identity systems,
and third-party dependencies now represent the most
challenging terrain. Understanding how attackers
chain these elements together—and how quickly they
operationalize successful techniques—will be critical
to navigating the threat landscape in the year ahead.
Confidential and Proprietary. © 2026 CyberProof 50

About CyberProof
We believe that working closely with our clients and
CyberProof delivers threat-led, co-managed security
partners through a better security, together model, jointly
operations with the belief that better security is achieved
empowers us to defend against the greatest of threats.
through the right partnerships, technology and client
experiences. Our threat-led, cloud-first, and AI-powered
To learn more:
approach to security, delivers industry-leading security
services which drives real and measurable business
outcomes.
Visit the CyberProof website
See 2026 Global Threat Intelligence:
Mapping Threats and Trends Report
research & findings
CCoonnffiiddeennttiiaall aanndd PPrroopprriieettaarryy.. ©© 22002266 CCyybbeerrPPrrooooff 5511

22. https://www.cybersecurity-insiders.com/indian-airports-targeted-by-gps-
Endnotes spoofing-cyber-attack/?utm_source=chatgpt.com
23. https://www.cyberproof.com/blog/teams-social-engineering-attack-threat-
actors-impersonate-it-to-steal-credentials-via-quick-assist/
1. https://www.cloudsek.com/knowledge-base/countries-most-targeted-by- 24. https://cybersecuritynews.com/ai-powered-ransomware/
cyberattacks 25. https://www.cyberproof.com/cyber-threat-intelligence/cyberproof-2025-mid-year-
2. https://www.infosecurity-magazine.com/news/retail-ransomware-jump- cyber-threat-landscape-report/
globally-q2/ 26. https://cyberinsider.com/first-ai-powered-ransomware-promptlock-discovered-
3. https://heimdalsecurity.com/blog/retail-cybersecurity-statistics/ in-the-wild/
4. https://deepstrike.io/blog/top-industries-targeted-by-hackers-2025 27. https://thecyberexpress.com/intelbroker-interview-exclusive/
5. https://cybersecuritynews.com/most-of-the-ransomware-attacks-targeting- 28. https://www.cysecurity.news/2025/11/clickfix-silent-cyber-threat-tricking.html
organizations/ 29. https://www.infosecurity-magazine.com/news/scattered-spider-shinyhunters/
6. https://deepstrike.io/blog/compromised-credential-statistics-2025 30. https://thehackernews.com/2025/10/lockbit-qilin-and-dragonforce-join.html
7. https://cybersecuritynews.com/most-of-the-ransomware-attacks-targeting- 31. https://thehackernews.com/2025/10/lockbit-qilin-and-dragonforce-join.html
organizations/ 32. https://malware.news/t/kimsuky-and-lazarus-join-forces-in-coordinated-
8. https://www.bleepingcomputer.com/news/security/chinese-hackers-behind- attacks/101864
attacks-targeting-sap-netweaver-servers/ 33. https://www.techworm.net/2025/11/russia-north-korea-potentially-syncing-
9. https://techcrunch.com/ cyberattacks.html
10. https://gbhackers.com/clop-ransomware/ 34. https://krebsonsecurity.com/2025/10/shinyhunters-wage-broad-corporate-
11. https://www.darkreading.com/cyberattacks-data-breaches/jaguar-land-rover- extortion-spree/
cyber-incident 35. https://gbhackers.com/qilin-ransomware-3/
12. https://www.reuters.com/world/uk/uk-economy-grows-01-q3-2025-11-13/ 36. https://socradar.io/blog/dark-web-profile-qilin-agenda-ransomware/
13. https://www.cysecurity.news/2025/09/retail-cyberattacks-surge-as- 37. https://www.cyberproof.com/blog/cyber-attacks-rise-as-tension-mounts-across-
service.html india-pakistan-border-post-terrorist-attack/
14. https://www.cyberproof.com/blog/coordinated-cyberattacks-strike-on-uk- 38. https://www.bleepingcomputer.com/news/security/pro-israel-hackers-hit-irans-
retail-sector/ nobitex-exchange-burn-90m-in-crypto/
15. https://www.webpronews.com/marks-spencer-cdo-rachel-higham-departs- 39. https://www.cyberproof.com/blog/beyond-the-blast-radius-irans-digital-
after-300m-cyberattack/ retaliation-expands-westward/
16. https://www.cyberproof.com/blog/when-hackers-empty-the-shelves-grocery- 40. https://securityaffairs.com/183222/apt/ukraine-sees-surge-in-ai-powered-
retail-supply-cyber-threats/ cyberattacks-by-russia-linked-threat-actors.html
17. https://itbrief.co.uk/story/uk-cyberattacks-surge-129-fuelling-risk-losses 41. https://www.reuters.com/world/europe/ukraine-railway-says-its-online-systems-
18. https://www.bbc.com/news/articles/cqjeej85452o targeted-large-scale-cyberattack-2025-03-24/
19. https://infotechlead.com/security/qantas-airways-confirms-cybersecurity- 42. https://www.cyberproof.com/case-studies/advanced-threat-hunting/
incident-targeting-contact-centers-90151 43. https://www.cyberproof.com/blog/connectwise-screenconnect-attacks-
20. https://www.bleepingcomputer.com/news/security/air-france-and-klm- continued-surge-in-rmm-tool-abuse/
disclose-data-breaches-impacting-customers/ 44. https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2024/2024-kpmg-ai-
21. https://ia.acs.org.au/article/2025/qantas-customer-data-leaked-to-dark- security-benchmark-survey-results.pdf
web.html
CCoonnffiiddeennttiiaall aanndd PPrroopprriieettaarryy.. ©© 22002266 CCyybbeerrPPrrooooff 5522