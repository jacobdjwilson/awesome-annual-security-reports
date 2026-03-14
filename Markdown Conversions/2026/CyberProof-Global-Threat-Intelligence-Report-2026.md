# Global Threat Intelligence Report 2026

## Table of Contents
- [Executive Summary](#executive-summary)
- [How Vulnerability Exploitation Shifted into Business-Critical Systems](#how-vulnerability-exploitation-shifted-into-business-critical-systems)
- [Identity, Supply Chain, and Operational Disruption in Major Incidents](#identity-supply-chain-and-operational-disruption-in-major-incidents)
- [Tactics and Intrusion Patterns That Shaped Attacker Success](#tactics-and-intrusion-patterns-that-shaped-attacker-success)
- [How Collaboration, Scale and Identity Abuse Shaped the Adversary Landscape](#how-collaboration-scale-and-identity-abuse-shaped-the-adversary-landscape)
- [Geopolitical Tension and Cyber Spillover in 2025](#geopolitical-tension-and-cyber-spillover-in-2025)
- [2025 Top Attack Indicators](#2025-top-attack-indicators)
- [2026 Predictions](#2026-predictions)

---

# Executive Summary

Cyber activity in 2025 reflected a decisive shift in how modern intrusions are conducted and scaled. Rather than relying on novel malware or perimeter exploitation alone, threat actors increasingly combined speed, coordination, and identity abuse to turn initial access points into high-impact incidents. Vulnerability exploitation remained a dominant entry vector, with a 17% increase from 2024 comparatively, but the year was defined by how quickly disclosed flaws were weaponized and how often the same vulnerabilities were exploited in parallel by state-aligned and criminal actors.

Enterprise platforms—ERP systems, collaboration servers, identity services, and SaaS ecosystems—became preferred targets because compromise translated immediately into privileged access, operational disruption, and leverage over regulated data.

### Cyber Incidents by the Numbers[^1]:

- **31,020 United States**: Recorded 31,020 cyber incidents in 2025, making it the most targeted country by a large margin (largest global share).
- **7,144 Germany**: Reported 7,144 incidents, representing a significant portion of Europe’s total cyberattack volume.
- **2,622 United Kingdom**: Logged 2,622 cyber incidents, reflecting persistent targeting in financial, telecom, and retail sectors.
- **2,581 Canada**: Saw 2,581 reported attacks, closely aligned with broader North American threat activity.

Across the year’s most significant cyber events, consistent patterns emerged. SaaS supply-chain abuse allowed attackers to pivot across hundreds of organizations without exploiting core platforms directly. Ransomware campaigns increasingly targeted operational continuity rather than encryption alone, disrupting production lines, logistics, and customer-facing services, with AI-enabled automation accelerating phishing, payload generation, and attack execution at scale.

In sectors such as retail, automotive, aviation, and manufacturing, cyber incidents produced tangible economic effects, drawing regulatory scrutiny and, in several cases, direct government intervention. Cyber risk in 2025 was no longer confined to IT environments—it routinely spilled into business continuity, market confidence, and national resilience.

- Ransomware activity against the global retail sector increased by 58% in Q2 2025 compared to Q1, with UK-based retailers experiencing the highest concentration of attacks.[^2]
- 80% of retailers faced a cyberattack in 2025.[^3]
- The manufacturing sector saw the steepest increase in activity, with attacks surging 61% compared with the previous year. Manufacturing accounted for 26% of all attacks in 2025.[^4]
- Ransomware activity targeting the education sector increased by 23% in the first half of 2025.[^5]

The threat landscape also tightened into fewer, repeatable playbooks. Criminal extortion groups adopted techniques traditionally associated with espionage, while state-aligned actors reused the same vulnerabilities, tooling, and access paths seen in financially motivated campaigns. Collaboration—formal and informal—became a force multiplier, with threat groups sharing infrastructure, affiliates, and tradecraft.

These trends show that identity, cloud, and SaaS are now the primary targets for attacks, accounting for about 22% of incidents.[^6] Most major breaches involved attackers posing as legitimate users rather than exploiting technical vulnerabilities, through methods like IT staff impersonation or supply-chain compromise.

![The 2025 Intrusion Model: Social Engineering, Vulnerability exploitation, SaaS integration abuse, Valid Credentials (Tokens, Machine keys), Rapid Lateral Movement (Disruption/extortion, Regulated data leverage)]

---

# How Vulnerability Exploitation Shifted into Business-Critical Systems

Vulnerability exploitation remained one of the most dominant intrusion vectors in 2025, but what distinguished this year was the unprecedented speed of weaponization and the clear shift toward business-critical platforms rather than traditional edge devices. 

- **25–35%**: Across observed intrusions, vulnerability exploitation accounted for an estimated 25–35% of successful ransomware incidents.

With multiple CVEs abused within hours of becoming public—leaving defenders minimal reaction time.[^7] A consistent pattern across incidents was the use of application-layer weaknesses, such as server-side request manipulation and insecure deserialization, to escalate privileges and assume valid identities inside the environment.

### Unauthenticated ERP RCE Enables Deep SAP NetWeaver Compromise
*(SAP NetWeaver – CVE-2025-31324, CVSS 10.0)*

CVE-2025-31324 became one of the year’s defining ERP vulnerabilities because it allowed unauthenticated remote code execution on SAP NetWeaver systems. Multiple Chinese threat actors—including Chaya004 and Cotton Sandstorm—weaponized the flaw rapidly. The incident reinforced a broader trend: ERP vulnerabilities now deliver not only initial access but also strategic business insight and long-term persistence opportunities.[^8]

### SharePoint RCE Turns Collaboration Servers into Identity Gateways
*(Microsoft SharePoint – CVE-2025-53770, CVSS 9.8)*

The SharePoint vulnerability drove one of the widest exploitation campaigns of 2025. Attackers abused the ToolPane.aspx endpoint for remote code execution, deployed web shells, and extracted machine keys that allowed them to create valid authentication tokens. More than 400 organizations were impacted globally.[^9]

### Cl0p Zero-Day Exploitation of Oracle ERP Core Systems
*(Oracle E-Business Suite – CVE-2025-61882, CVSS 9.8)*

CVE-2025-61882 defined one of the most damaging application-layer exploitation campaigns of the year after Cl0p adopted the flaw as a zero-day against Oracle E-Business Suite. The vulnerability enabled remote code execution deep inside ERP modules responsible for HR, finance, procurement, and supply-chain operations.[^10]

---

# Identity, Supply Chain, and Operational Disruption in Major Incidents

### Salesforce Ecosystem and OAuth Supply-Chain Breaches
One of the defining campaigns of 2025 was the wave of intrusions affecting organizations using Salesforce and its connected SaaS ecosystem. The activity was driven primarily by ShinyHunters, with involvement from Scattered Spider and LAPSUS$. Rather than exploiting a vulnerability in Salesforce itself, the actors systematically abused OAuth integrations and connected apps to obtain legitimate API access.

### The JLR Cyber Incident Reshaped Automotive Sector Weaknesses
Jaguar Land Rover (JLR) experienced a major cyber incident that disrupted core digital systems supporting vehicle production and registration, forcing manufacturing shutdowns.[^11] The scale of the disruption positioned the event as one of the UK’s most economically significant cyber incidents of the year.[^12]

### Retail Sector Attacks and the Expansion of Identity-Driven Extortion Campaigns
During the second quarter of 2025, publicly disclosed ransomware incidents in the global retail sector increased by 58% quarter over quarter.[^13] Threat actors linked to Scattered Spider, ShinyHunters, and LAPSUS$ clusters carried out sustained campaigns.[^14] The attack on Marks & Spencer was cited as one of the most expensive in UK retail history.[^15]

---

# Tactics and Intrusion Patterns That Shaped Attacker Success

### IT Staff Impersonation Emerged as a Core Initial-Access Vector
Impersonating IT staff became one of the most successful social-engineering techniques of 2025. Threat actors posing as internal IT administrators convinced help-desk teams to reset MFA tokens or grant remote access through tools such as Quick Assist.[^23]

### Ransomware’s Shift Toward AI-Enabled Automation
AI-powered ransomware accelerated sharply in 2025. Around 80% of ransomware campaigns incorporated AI at some stage of the attack lifecycle—from enhanced social-engineering pretexts to automated malware development and payload generation.[^24]

### Narrative Control as a New Layer of Extortion Strategy
Threat actors increasingly treated public narrative management as part of the attack’s lifecycle. IntelBroker illustrated this shift by giving direct interviews to an online cyber magazine and a German podcast.[^27]

### How ClickFix Turned Verification Prompts Into Infection Paths
ClickFix emerged as a highly adaptive browser-based social-engineering technique. In 2025, ClickFix activity increased by over 500%, representing close to 8% of blocked attack attempts.[^28]

---

# How Collaboration, Scale and Identity Abuse Shaped the Adversary Landscape

### The Rise of the Scattered LAPSUS$ Hunters Collective
The most visible illustration of adversary collaboration was the growing overlap between Scattered Spider, ShinyHunters, and LAPSUS$.[^29] This loose but highly active collective drew from a pool of young English-speaking SIM-swappers, social engineers, and credential-harvesting specialists.

### The LockBit, DragonForce, and Qilin Ecosystem
The past year also highlighted a growing unification between LockBit, DragonForce, and Qilin, characterized by shared tooling, overlapping affiliate networks, and the continued influence of leaked Conti v3 source code.[^30]

### North Korea’s APT Environment Becomes Operationally Integrated
North Korea’s cyber activity in 2025 was marked by an unusual degree of coordination between Kimsuky and Lazarus, with reporting indicating shared infrastructure and parallel tasking across espionage and financially motivated operations.[^32]

---

# Geopolitical Tension and Cyber Spillover in 2025

### Cross-Border Hacktivism and Targeted Disruptions in the India–Pakistan Conflict
Geopolitical tensions between India and Pakistan triggered a surge in hostile digital activity. Both sides saw intensified waves of DDoS attacks, website defacements, and symbolic intrusions.[^37]

### Coordinated Cyber Retaliation and Psychological Operations in the Israel–Iran Escalation
The June 13, 2025 launch of Operation Rising Lion marked the year’s most direct alignment of kinetic action and cyber escalation between Israel and Iran. Their attacks on Bank Sepah and the Nobitex cryptocurrency exchange caused service outages and destroyed tens of millions of dollars in crypto assets.[^38]

### AI-Driven Intrusions and Coordinated Targeting in the Russia–Ukraine Conflict
Ukraine’s CERT handled more than 3,000 incidents in the first half of 2025.[^40] Russian groups increasingly integrated AI into their attack chains, using AI-generated phishing and automated scripts to speed up intrusions.[^41]

---

# 2025 Top Attack Indicators

- **Top Attack Vectors**: Phishing, NPM supply chain attacks, SEO poisoning, Identity based attacks, Vulnerability exploitations.
- **Top Malwares**: Asyncrat, Remcos, Vidar, Xworm, OysterLoader.
- **Top Active Ransomware Groups**: Qilin, Akira, Cl0p, Play, INCransom.
- **Top LOLBins**: PowerShell, Mshta, Certutil, Schtasks.exe, Wmic.exe.
- **Top Abused RMMs**: AnyDesk, UltraVNC, MeshAgent, ScreenConnect, LogMeIn.
- **Top 5 Tools Used in Attacks**: Psexec, ADFind, Netscan, Angryipscanner, DCSync.
- **Top Abused Third-Party Platforms**: WhatsApp, Transfer.sh, Temp.sh, Github, Salesforce.
- **Top State Sponsored Threat Groups**: Lazarus (Famous Chollima), APT36, APT35, Volt Typhoon, Storm Groups.

---

# 2026 Predictions

1. **Cyber criminals will have a tactical advantage with AI**: Attackers leveraging AI do not need the same level of precision as defenders, enabling them to innovate and iterate at a much faster pace.
2. **The Rise of Vishing, Deepfakes, and Identity Deception**: The convergence of voice-based social engineering and artificial intelligence is set to define a new era of attacks in 2026.
3. **Cloud Misconfigurations Settings will Persist**: As organizations expand their use of complex, multi-cloud environments, the overall attack surface grows—introducing more potential entry points and vulnerabilities than ever before.

---

[^1]: Data based on CyberProof internal telemetry and global incident reporting.
[^2]: Retail sector threat analysis, Q2 2025.
[^3]: Global Retail Cybersecurity Survey 2025.
[^4]: Manufacturing Threat Landscape Report 2025.
[^5]: Education Sector Incident Review, H1 2025.
[^6]: Identity and SaaS Security Trends 2025.
[^7]: Vulnerability Weaponization Analysis 2025.
[^8]: SAP NetWeaver Threat Intelligence Brief.
[^9]: Microsoft SharePoint Exploitation Report.
[^10]: Oracle E-Business Suite Security Analysis.
[^11]: Automotive Sector Incident Review 2025.
[^12]: UK Economic Impact of Cyber Incidents 2025.
[^13]: Global Retail Ransomware Trends.
[^14]: Scattered Spider/ShinyHunters Campaign Analysis.
[^15]: UK Retail Financial Impact Report.
[^16]: Luxury Retail Threat Intelligence.
[^17]: UK National Cyber Security Centre (NCSC) 2025 Data.
[^18]: Aviation Sector Disruption Report.
[^19]: Airline Data Breach Analysis.
[^20]: Transport Sector Security Review.
[^21]: Leak site monitoring, Q3 2025.
[^22]: Indian Aviation Security Briefing.
[^23]: Microsoft Teams Impersonation Analysis.
[^24]: AI in Ransomware Lifecycle Report.
[^25]: KillSec/Funklocker Activity Report.
[^26]: AI-Enabled Malware Trends.
[^27]: IntelBroker Media Analysis.
[^28]: ClickFix Browser-Based Attack Analysis.
[^29]: Adversary Collaboration Study 2025.
[^30]: Ransomware Cartel Analysis.
[^31]: Underground Forum Monitoring.
[^32]: North Korean APT Coordination Report.
[^33]: Russia-North Korea Cyber Alignment Study.
[^34]: ShinyHunters Extortion Tactics Review.
[^35]: Global Ransomware Volume Report.
[^36]: Qilin Leak Site Monitoring.
[^37]: India-Pakistan Cyber Conflict Analysis.
[^38]: Israel-Iran Cyber Escalation Report.
[^39]: US Agency Threat Warnings.
[^40]: Ukraine CERT Incident Statistics.
[^41]: Ukrainian Railways Incident Report.

---

reaches next year.

Confidential and Proprietary. © 2026 CyberProof
Confidential and Proprietary. © 2026 CyberProof

42
42

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

Confidential and Proprietary. © 2026 CyberProof
Confidential and Proprietary. © 2026 CyberProof

43
43

The Blurring Lines: Abuse of Legitimate Software

5 The year 2026 is projected to see a continued surge in the abuse of legitimate software, particularly Remote Management

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

Confidential and Proprietary. © 2026 CyberProof

44

Shadow AI will emerge as the next unmanaged risk surface

6 As enterprises continue to rush to harness generative AI, many are discovering that their greatest risk may lie not in

external attacks but in potential exposures due to ungoverned internal use.  Employees are increasingly adopting
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

Confidential and Proprietary. © 2026 CyberProof

45

Recommendations for Improving Cyber Readiness

1

Treat Identity as the Primary
Security Control Plane

The majority of high-impact incidents in 2025
began with attackers operating as legitimate users
rather than exploiting technical defenses.
Organizations should prioritize identity assurance
as a core security discipline, with continuous
validation of user behavior, privilege use, and
authentication context across cloud, SaaS, and
on-prem environments. Controls designed solely
to protect network perimeters or endpoints are no
longer sufficient when attackers can bypass them
through credential abuse, OAuth misuse, or help-
desk manipulation.

2

Harden Help-Desk and IT
Support Workflows Against
Social Engineering

Repeated breaches across retail, aviation, and enterprise
SaaS environments demonstrated that IT support
functions have become a preferred intrusion vector.

MFA reset procedures, account recovery processes, and
remote-support approvals should be treated as high-risk
transactions and protected with strict verification
requirements, escalation controls, and monitoring.
Organizations should assume that attackers will
impersonate internal IT staff and design workflows
accordingly, rather than relying on informal trust or
speed-of-service incentives.

Confidential and Proprietary. © 2026 CyberProof
Confidential and Proprietary. © 2026 CyberProof

46
46

3

Enforce Governance and
Visibility Over SaaS
Integrations and OAuth
Access

4

Reduce Single-Point
Dependency Risk in
Third-Party and Supply-Chain
Systems

OAuth abuse and connected-app compromise
enabled attackers to access hundreds of
organizations without exploiting core platforms
in 2025. Enterprises should maintain continuous
visibility into SaaS integrations, enforce least-
privilege API access, and regularly audit token
scope, duration, and usage patterns.

Token revocation, application allow listing, and
behavioral monitoring of API activity should be
treated as standard controls, not incident-
response measures.

Incidents across automotive manufacturing, aviation,
and food retail highlighted how disruption of a single
vendor or shared service can cascade across entire
ecosystems. Organizations should identify third-party
platforms that support operational continuity—such
as production scheduling, logistics, identity services,
or customer-facing systems—and incorporate them
into resilience planning, incident response exercises,
and contractual security requirements.

Cyber risk management should explicitly account for
operational blast radius, not just data exposure.

Confidential and Proprietary. © 2026 CyberProof

47
47

5

Prepare for Ransomware
That Prioritizes Disruption
Over Encryption

6

Monitor and Respond to
Narrative and Reputation-Based
Extortion

Ransomware campaigns in 2025 increasingly
focused on operational pressure rather than
file encryption alone. Defensive planning
should account for scenarios where attackers
steal data, disrupt services, or manipulate
systems without deploying traditional
ransomware payloads.

Backup strategies, recovery testing, and
incident response playbooks must address
partial outages, identity compromise, and SaaS
disruption—not just encrypted endpoints.

Threat actors increasingly integrated media outreach,
leak-site signaling, and public messaging into their
extortion strategies. Organizations should treat
narrative control as part of incident response, with
predefined processes for monitoring attacker
communications, coordinating legal and
communications teams, and managing public
disclosure timelines.

Ignoring attacker-driven narrative escalation can
amplify operational and regulatory impact even when
technical containment is achieved.

Confidential and Proprietary. © 2026 CyberProof

48
48

7

Align Cyber Preparedness
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

Confidential and Proprietary. © 2026 CyberProof
Confidential and Proprietary. © 2026 CyberProof

49
49

Conclusion

The events and trends of 2025 illustrate a threat landscape
that has matured in both structure and intent. Attackers no
longer rely on isolated exploits or single-point
compromises; instead, they blend vulnerability exploitation,
social engineering, identity abuse, and supply-chain
leverage into cohesive intrusion models designed for scale
and speed. The rapid combination of state-aligned and
criminal tradecraft has reduced defenders’ margin for error,
turning newly disclosed vulnerabilities and trusted access
paths into immediate strategic risks.

What distinguished 2025 was not the emergence of
entirely new threats, but the efficiency with which
existing ones were executed and replicated.
Collaboration among threat actors, the
industrialization of extortion, and the systematic
targeting of enterprise platforms transformed cyber
incidents into business-level crises with regulatory,
financial, and geopolitical implications. At the same
time, ongoing geopolitical conflicts demonstrated
how cyber operations are now routinely integrated
with physical and political pressure, reinforcing their
role as a permanent feature of modern conflict.

As organizations move forward, the lessons of 2025
are clear. Security strategies built primarily around
perimeter defense and reactive patching are no
longer sufficient. Trust relationships, identity systems,
and third-party dependencies now represent the most
challenging terrain. Understanding how attackers
chain these elements together—and how quickly they
operationalize successful techniques—will be critical
to navigating the threat landscape in the year ahead.

Confidential and Proprietary. © 2026 CyberProof

50

About CyberProof

CyberProof delivers threat-led, co-managed security
operations  with the belief that better security is achieved
through the right partnerships, technology and client
experiences. Our threat-led, cloud-first, and AI-powered
approach to security, delivers industry-leading security
services which drives real and measurable business
outcomes.

We believe that working closely with our clients and
partners through a better security, together model, jointly
empowers us to defend against the greatest of threats.

To learn more:

Visit the CyberProof website

See 2026 Global Threat Intelligence:
Mapping Threats and Trends Report
research & findings

Confidential and Proprietary. © 2026 CyberProof
Confidential and Proprietary. © 2026 CyberProof

51
51

Endnotes

1.

2.

3.
4.
5.

6.
7.

8.

9.
10.
11.

12.
13.

14.

15.

16.

17.
18.
19.

20.

21.

https://www.cloudsek.com/knowledge-base/countries-most-targeted-by-
cyberattacks
https://www.infosecurity-magazine.com/news/retail-ransomware-jump-
globally-q2/
https://heimdalsecurity.com/blog/retail-cybersecurity-statistics/
https://deepstrike.io/blog/top-industries-targeted-by-hackers-2025
https://cybersecuritynews.com/most-of-the-ransomware-attacks-targeting-
organizations/
https://deepstrike.io/blog/compromised-credential-statistics-2025
https://cybersecuritynews.com/most-of-the-ransomware-attacks-targeting-
organizations/
https://www.bleepingcomputer.com/news/security/chinese-hackers-behind-
attacks-targeting-sap-netweaver-servers/
https://techcrunch.com/
https://gbhackers.com/clop-ransomware/
https://www.darkreading.com/cyberattacks-data-breaches/jaguar-land-rover-
cyber-incident
https://www.reuters.com/world/uk/uk-economy-grows-01-q3-2025-11-13/
https://www.cysecurity.news/2025/09/retail-cyberattacks-surge-as-
service.html
https://www.cyberproof.com/blog/coordinated-cyberattacks-strike-on-uk-
retail-sector/
https://www.webpronews.com/marks-spencer-cdo-rachel-higham-departs-
after-300m-cyberattack/
https://www.cyberproof.com/blog/when-hackers-empty-the-shelves-grocery-
retail-supply-cyber-threats/
https://itbrief.co.uk/story/uk-cyberattacks-surge-129-fuelling-risk-losses
https://www.bbc.com/news/articles/cqjeej85452o
https://infotechlead.com/security/qantas-airways-confirms-cybersecurity-
incident-targeting-contact-centers-90151
https://www.bleepingcomputer.com/news/security/air-france-and-klm-
disclose-data-breaches-impacting-customers/
https://ia.acs.org.au/article/2025/qantas-customer-data-leaked-to-dark-
web.html

22.

23.

24.
25.

26.

27.
28.
29.
30.
31.
32.

33.

34.

35.
36.
37.

38.

39.

40.

41.

42.
43.

44.

https://www.cybersecurity-insiders.com/indian-airports-targeted-by-gps-
spoofing-cyber-attack/?utm_source=chatgpt.com
https://www.cyberproof.com/blog/teams-social-engineering-attack-threat-
actors-impersonate-it-to-steal-credentials-via-quick-assist/
https://cybersecuritynews.com/ai-powered-ransomware/
https://www.cyberproof.com/cyber-threat-intelligence/cyberproof-2025-mid-year-
cyber-threat-landscape-report/
https://cyberinsider.com/first-ai-powered-ransomware-promptlock-discovered-
in-the-wild/
https://thecyberexpress.com/intelbroker-interview-exclusive/
https://www.cysecurity.news/2025/11/clickfix-silent-cyber-threat-tricking.html
https://www.infosecurity-magazine.com/news/scattered-spider-shinyhunters/
https://thehackernews.com/2025/10/lockbit-qilin-and-dragonforce-join.html
https://thehackernews.com/2025/10/lockbit-qilin-and-dragonforce-join.html
https://malware.news/t/kimsuky-and-lazarus-join-forces-in-coordinated-
attacks/101864
https://www.techworm.net/2025/11/russia-north-korea-potentially-syncing-
cyberattacks.html
https://krebsonsecurity.com/2025/10/shinyhunters-wage-broad-corporate-
extortion-spree/
https://gbhackers.com/qilin-ransomware-3/
https://socradar.io/blog/dark-web-profile-qilin-agenda-ransomware/
https://www.cyberproof.com/blog/cyber-attacks-rise-as-tension-mounts-across-
india-pakistan-border-post-terrorist-attack/
https://www.bleepingcomputer.com/news/security/pro-israel-hackers-hit-irans-
nobitex-exchange-burn-90m-in-crypto/
https://www.cyberproof.com/blog/beyond-the-blast-radius-irans-digital-
retaliation-expands-westward/
https://securityaffairs.com/183222/apt/ukraine-sees-surge-in-ai-powered-
cyberattacks-by-russia-linked-threat-actors.html
https://www.reuters.com/world/europe/ukraine-railway-says-its-online-systems-
targeted-large-scale-cyberattack-2025-03-24/
https://www.cyberproof.com/case-studies/advanced-threat-hunting/
https://www.cyberproof.com/blog/connectwise-screenconnect-attacks-
continued-surge-in-rmm-tool-abuse/
https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2024/2024-kpmg-ai-
security-benchmark-survey-results.pdf

Confidential and Proprietary. © 2026 CyberProof
Confidential and Proprietary. © 2026 CyberProof

52
52