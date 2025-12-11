# Threat Intelligence Report 2025

The official report URL is: https://www.telecomtv.com/content/security/nokia-report-reveals-alarming-extent-of-telco-cybersecurity-threats-53994/

# Report Content Below

## Threat Intelligence Report 2025

### Executive Summary

Threat actors have broadened their horizons and raised their attack sophistication, making telecoms a key target in 2024-2025.

Beyond ransomware and data theft, campaigns systematically targeted lawful interception systems, mobile core signaling, orchestration layers, and subscriber databases. The patterns indicate coordinated infrastructure compromise rather than isolated opportunistic attacks.

“Salt Typhoon was definitely a change of strategy. It was a big investment, impacted a lot of people and it took six to nine months.”
- CISO, Leading Communications Service Provider (CSP) in North America

This year’s report draws on Nokia’s broad security expertise: intelligence from our NetGuard and Deepfield portfolios, real-world insights from Managed Security Services operations, advanced research from Nokia Bell Labs, and expertise in cybersecurity consulting and quantum-safe networking. These are complemented by fresh quantitative and qualitative insights from a global survey of telecom security leaders conducted this summer, capturing the full scale and nature of this shift.

The impact is measurable.

This report is based on public data and provided for informational purposes only. It does not constitute legal, regulatory, or security advice, and shall not replace independent risk assessments or professional judgment.

2

Threat Intelligence Report 2025

Over 63% of surveyed operators faced at least one “living off the land” attack last year, and 32% saw four or more, reinforcing that stealthy techniques are now a persistent reality in telecom networks.

Hygiene gaps still open doors. 76% of vulnerabilities stem from missing patches. Application-layer issues, including poor access controls and exploitable software flaws, remain prevalent as digital services expand.

Human factors still drive the majority of high-cost breaches. 59% are caused by human error or insider activity, yet fewer than one-third of decision makers view training gaps as a major challenge.

Targeted malware is growing: 55% of operators report threats adapted to telecom infrastructure, and 45.1% have faced custom-built toolkits.

Recovery times are slow: 63% of major incidents take more than a week to fully recover, long enough to hurt uptime, revenue, and trust.

DDoS attacks have reached new heights. Residential proxy botnets now include over 100 million compromised endpoints, enabling terabit-scale floods. 52% of DDoS campaigns now target multiple hosts simultaneously, 58% of them utilize multiple attack vectors, and 78% are completed within five minutes (37% within two minutes).

Timelines for the deployment of quantum-safe cryptography are accelerating. While some standards have been finalized, migration is still in its infancy. Certificate validity periods were also announced to be shrinking from 398 days now to 47 days by 2029, making manual management impossible at telecom scale.

Global cybersecurity regulation is accelerating, driving CSPs to meet tighter reporting deadlines, secure supply chains, and adopt risk frameworks.

By 2028, over half of telecom operators expect to run highly or fully autonomous SOCs. Success will depend on how well these systems are governed and secured to maintain trust while operating at full speed.

3

Threat Intelligence Report 2025

## Telecom sector attack trends

4

Threat Intelligence Report 2025

### Major incidents in 2024-2025

Adversaries shifted strategy. Instead of opportunistic strikes, they now execute multi-year campaigns targeting telecom infrastructure.

Incidents show persistent exploitation of vulnerabilities, compromised credentials, ransomware, and web shells, causing operational disruption and large-scale data exposure.

| Date                 | Target(s)                      | Type           | Actor (as reported)        | Key impact (per resources)                                                              |
| :------------------- | :----------------------------- | :------------- | :------------------------- | :-------------------------------------------------------------------------------------- |
| Late 2023 - Feb 2024 | Undisclosed telecom operators  | Espionage      | Suspected Lightbasin       | GTPDoor malware reportedly used for covert data exfiltration                            |
| Sep - Oct 2024       | Major telecom operators        | Espionage      | Salt Typhoon (Microsoft attribution) | Intrusion into lawful interception systems                                              |
| Jan 2025             | Regional telecom operator      | Ransomware     | RansomHouse (attacker-claimed) | Attacker claims unauthorized access to some customer data                               |
| Feb 2025             | European telecom operator      | Data breach    | Unknown                    | Data of individuals and organizations exposed                                           |
| Mar 2025             | ISP (attacker-claimed)         | Ransomware     | Arkana Security (attacker-claimed) | Attacker claims theft of ~2.6M records; unverified                                      |
| Mar 2025             | Asian telecom operators        | Espionage      | Weaver Ant (Sygnia attribution) | Web shells deployed for persistent access                                               |
| Apr 2025             | Asian telecom operator         | Data breach    | Unknown                    | ~26.95M USIM records exposed; SIM-cloning risk; BPFDoor on HSS                          |
| Apr 2025             | African telecom group          | Unauthorized access | Unknown                    | Unauthorized access to personal info in select markets                                  |
| May 2025             | Urban areas in Turkey          | Telecom fraud  | Local group (7 arrested)   | Fake base stations used for spoofed SMS                                                 |
| May 2025             | US regional telecom operator   | Cyber incident | Unknown                    | Multi-day outage                                                                        |
| May - Aug 2025       | Major telecom operator (attacker-claimed) | Data breach    | HellCat (attacker-claimed) | Attacker claims theft of internal files (~106 GB); validity disputed                    |
| Jun 2025             | Major telecom operator (attacker-claimed) | Data breach    | Dedale (attacker-claimed)  | Attacker claims theft of ~22M customer records; unverified                              |

Table 1: Publicly reported or research-attributed incidents 2024–2025 (Based on open-source intelligence; attribution and impact details reflect public reporting as of Sept 2025.)

What is known and reported can only represent the tip of the iceberg. This is especially true of state actors’ “living off the land” attacks, where adversaries use legitimate tools and deep knowledge of telecom technologies to blend in and evade detection.

Reflecting industry concerns at TM Forum DTW Ignite 2025, BT Group’s Howard Watson described the threat as “unprecedented,” noting a 160-170% increase in security events compared to the previous year.

| Date     | Target(s)                   | Type                | Actor (as reported) | Key impact (per resources)                               |
| :------- | :-------------------------- | :------------------ | :------------------ | :------------------------------------------------------- |
| Jul 2025 | European telecom operator   | Unauthorized access | Unknown             | Internal systems compromised; service disruptions        |
| Jul 2025 | European telecom operator   | Service disruption  | Unknown             | Targeted cyberattack disrupted services                  |
| Aug 2025 | European telecom operator   | Data breach         | Unknown             | ~6.4M accounts exposed                                   |
| Aug 2025 | Enterprise connectivity provider | Ransomware          | WarLock (attacker-claimed) | Attacker claims support systems disrupted and ~1M documents stolen |
| Aug 2025 | European telecom operator   | Data breach         | Unknown             | Unauthorized access to certain data from 850,000 customer accounts |
| Aug 2025 | Australian telecom operator | Data breach (credential theft) | Unknown             | ~280K records exposed                                    |
| Sep 2025 | Asian telecom operator      | Data breach (via fake base stations) | Unknown             | ~19,000 users affected; IMSI leak and fraud risk         |
| Sep 2025 | Submarine cable infrastructure (regional corridor) | Service disruption  | Unknown             | Multiple cable faults caused rerouting and elevated latency |
| Sep 2025 | Asian telecom operators     | Initial access sale | NetworkBrokers (with Psych1c) | Access offered for sale; RCE vulnerability reportedly enables root access; unverified |
| Sep 2025 | Regional ISP                | Data breach         | Sorb                | Attacker claims ~209K user records exposed; unverified   |
| Sep 2025 | Multiple telecom operators  | Cyber espionage     | UNC1549             | Devices compromised via LinkedIn lure; credential theft and data collection |
| Sep 2025 | Unknown                     | Abuse of telecom systems | Unknown             | Large SIM-server network discovered; capable of automating swatting attacks and disrupting emergency services |

Table 1: Publicly reported or research-attributed incidents 2024–2025 (Based on open-source intelligence; attribution and impact details reflect public reporting as of Sept 2025.)

5

Threat Intelligence Report 2025

### The Salt Typhoon Campaign

#### Context

Salt Typhoon is an advanced persistent threat (APT) group linked to a large-scale cyber-espionage campaign targeting telecom infrastructure. The group exploited vulnerabilities in network operating systems, including IOS XE, to gain persistent, high-privilege access at the device level, bypassing traditional security controls. This access enabled the exfiltration of call detail records and some lawful-interception data for selected high-value targets.

#### Key Facts

*   **Activity window**: Public reporting from September 2024 onward; likely active since at least 2019
*   **Confirmed targets**: Telecom providers and critical infrastructure operators across 80+ countries
*   **Likely objectives**: Access to call detail records and some lawful-interception data for high-value targets
*   **Initial access methods**: Exploitation of network infrastructure vulnerabilities, including IOS XE
*   **Tactics**: GRE/IPsec tunnels, firmware/config tampering, credential theft, traffic mirroring, and “living off the land” (LOTL) tools (PsExec, Impacket)
*   **Malware/tooling**: GhostSpider, Masol RAT, Demodex rootkit used for persistence and EDR evasion in telecom environments

#### Impact

A joint Cybersecurity Advisory issued on August 27, 2025, confirmed that the campaign affected telecom and critical infrastructure networks in more than 80 countries. Confirmed compromises include systems supporting lawful interception, which are essential for regulated communications monitoring.

Authorities have described this as one of the most significant telecom-targeted campaigns disclosed in recent years, due to its global reach, the sensitivity of the data accessed, and the attackers’ ability to maintain long-term control within core network environments.

“Salt Typhoon was the most significant cybersecurity incident we faced in the last 12 months. This was an attack against the infrastructure that was well planned and well thought through…some of the entry points were put in place years ago, just sitting and waiting for the right moment to trigger.”
- CISO, Leading CSP in North America

7

Threat Intelligence Report 2025

### Recommended Mitigations

*   **Patch and harden infrastructure**: Apply telecom patches rapidly; audit for unauthorized accounts, tunnels, or firmware tampering
*   **Strengthen access controls**: Enforce MFA, rotate privileged credentials, and isolate lawful-interception and management systems; adopt zero trust principles
*   **Enhance monitoring & detection**: Deploy advanced EDR/XDR for real-time endpoint visibility across IT and OT assets; analyze OE&M and control traffic in real time; use traffic analysis, UEBA, and proactive threat hunting to detect fileless, “living off the land,” and covert attacks
*   **Improve response readiness**: Establish immutable logging, maintain updated IOCs via CERTs/ISACs, and rehearse tailored incident response playbooks

#### The Typhoon Cohort

Microsoft uses the “Typhoon” naming convention for multiple threat groups targeting critical infrastructure sectors. Salt Typhoon has been linked to telecom-focused intrusions, while other Typhoon groups have been reported in open-source intelligence as targeting sectors such as energy, IT supply chain, and IoT.

| Group          | Primary targets                               | Tactics                               | Tools / Techniques                               |
| :------------- | :-------------------------------------------- | :------------------------------------ | :----------------------------------------------- |
| Salt Typhoon   | Telecom operators                             | Vulnerability exploits, backdoors     | GhostSpider, Demodex                             |
| Volt Typhoon   | Critical infrastructure                       | LOTL, credential theft                | Built-in admin tools, proxies                    |
| Flax Typhoon   | IoT networks, SOHO devices                    | IoT exploitation, botnet operations   | Mirai-based malware variants                     |
| Charcoal Typhoon | Gov, education, energy                        | Phishing, AI-assisted social engineering | Phishing kits, LLM misuse                        |
| Salmon Typhoon | Defense, crypto tech                          | Espionage, custom malware             | Exfiltration tools, RATs                         |
| Silk Typhoon   | IT supply chain, MSPs                         | Supply chain compromise, zero-day exploits | Web shells, stolen API keys                      |

Table 2: The Typhoon cohort. Based on Microsoft’s threat actor taxonomy and open-source intelligence; subject to change.

Surveyed telecom operators report their lowest readiness for nation-state attacks, just 7% feel fully prepared.

8

Threat Intelligence Report 2025

### BPFDoor and the Compromise of USIM Systems

#### Context

South Korea’s Ministry of Science and ICT confirmed a breach involving BPFDoor, a Linux backdoor known for stealth and persistence. BPFDoor uses Berkeley Packet Filter (BPF) to capture traffic at the kernel level and activates via “magic packets,” bypassing firewalls without opening ports.

#### Impact

BPFDoor enabled stealthy, kernel-level persistence, bypassing traditional defenses and leading to large-scale exposure of subscriber identifiers.

#### Key Facts

*   **Persistence**: Long-term presence suspected; exact start date unconfirmed
*   **Scope**: MSIT confirmed compromise of USIM systems and exfiltration of ~26.96M IMSI records
*   **Impact**: SIM-cloning risk prompted a nationwide SIM replacement campaign
*   **Techniques**: Passive packet capture, firewall bypass, reverse shell via magic packets, process masquerading

9

Threat Intelligence Report 2025

#### Recommended Mitigations

*   Treat USIM systems as Tier-0 assets; enforce isolation and immutable logging
*   Apply MFA and rotate credentials across admin systems
*   Patch IMS/signaling infrastructure and segment management networks
*   Deploy telco-grade network function security with anomaly detection of stealth patterns
*   Strengthen supply chain security for orchestration platforms

44.4% of operators rank reputational harm as the #1 breach consequence, more than financial or technical impact. Crisis communication and transparency are now core components of cybersecurity strategy.

74% of operators say they’re prepared for malware/ransomware, yet 83% of incidents cost over $500K, half exceed $1M.

#### How BPFDoor Becomes a Malicious Implementation of BPF

01 Attacker sends packets to any port with magic credentials
02 Implant sees packet at the same time as firewall
03 Starts a shell on TCP port
04 IPRouting tables changes after magic packet received
05 Any data exfiltration flow achievable as traffic appears to go to legit port but being routed in intended direction

Graph 1: BPFDoor attack flow

Implant
Kernel
Service
Magic Packet Dispatch
IPTables Redirect
Host
Firewalls
Threat Actor
Shell Or Backdoor

10

Threat Intelligence Report 2025

### Insider and Third-Party Risks

#### Context

Insider-driven incidents, malicious or accidental, are a leading cause of costly breaches. Telecom’s complex supply chain amplifies the risk.

#### Observed Trends Based on Global Survey

*   59% of the most impactful incidents stem from people-related causes, yet only 30% of decision makers cite inadequate staff training as a challenge
*   Vendor and third-party compromise accounts for 10% of these incidents, despite ranking among telecoms’ top security concerns

#### Impact

Gaps in detection for insider-like behavior, including stolen credential misuse, leave operators exposed to outages, espionage, and fraud.

#### Recommended Mitigations

*   Deploy telecom-specific UEBA that integrates OSS/BSS, EPC, RAN, lawful interception telemetry
*   Combine UEBA with PAM, EDR, and network telemetry in a central view to detect:
    *   Privileged misuse - Admins or engineers accessing sensitive systems (e.g. signaling, subscriber DBs) without valid tickets
    *   Privilege escalation - Unauthorized jumps in access level (e.g. OSS Tier 1 to Core Admin)
    *   Credential compromise - Phished or stolen credentials used to mimic insider behavior
    *   Remote access anomalies - Unusual logins to EPC, 5GC, or RAN from unexpected geos or hours
    *   Data exfiltration - Stealthy transfers of subscriber data, config files, or interception logs
    *   Behavioral outliers - Sudden spikes in access, external connections from management zones, or logins outside normal patterns

Learn more about NetGuard Cybersecurity Dome

#### Real-World Example: Physical Access Exploited in Regional Server Breach

A senior technical leader at a major North American CSP described a breach where an individual gained physical access to a regional server room and planted a device. “The more we think about AI and sophisticated threats, the more we drop guard on traditional threats.” - he said. The intrusion went undetected until a ransom demand revealed access to sensitive billing and customer data.

“Someone physically walked into a server room and planted something … That was one of the days that I feared for my job.”

While the attacker’s identity wasn’t confirmed, the executive noted they may have posed as or exploited contractor-level access, prompting a network-wide audit and overhaul of physical ports and access controls.

“We had to disable every unused physical port and overhaul contractor access management after the incident.”

“People are always known to be the weakest point in an organization… Securing them is probably the hardest part.”
- Security Strategy Lead, Major CSP in Europe

11

Threat Intelligence Report 2025

### Operational Security Telemetry and Threat Patterns

Access abuse is now a systemic risk. Access misuse dominated incident logs. These were not brute-force intrusions but subtle violations of operational norms:

*   Privileged commands executed outside change windows triggered outages and compliance violations
*   Logins to critical devices during non-maintenance periods increased operational risk
*   Unauthorized access to PII files and credential sharing exposed sensitive subscriber data
*   Privilege escalation attempts often mimicked routine admin activity

Telecom interfaces show persistent architectural weaknesses. Security assessments across SS7, GTP, Diameter, and RAN interfaces revealed systemic gaps:

*   Signaling firewall configurations showed incomplete packet inspection and inconsistent handling of HLR/HSS queries
*   RAN backhaul lacked sufficient traffic separation and topology obfuscation, creating lateral movement opportunities
*   IMSI catching remains unresolved due to legacy SIMs unable to compute SUCI
*   Fake BTS attachments bypassed core network authentication in LTE/5G deployments
*   Firewall configuration gaps widen the attack surface. Firewall audits identified recurring configuration weaknesses:
    *   Some firewall policies included overly permissive any-to-any rules
    *   Logging and monitoring were disabled, leaving SOCs blind to traffic anomalies
    *   Weak SNMP strings and outdated firmware exposed devices to remote control and data leaks

Firewall hygiene remains an area for improvement. Telcos must enforce least privilege and visibility as non-negotiable standards.

Telcos must treat insider access as a dynamic threat surface. Without behavioral baselining and privilege monitoring, attackers don’t need to break in, just simply log in.

These are architectural blind spots. Telcos must accelerate remediation or risk systemic exploitation.

SOC data highlights what attackers exploit once inside the perimeter, with incident volumes continuing to rise and exposing recurring patterns of access misuse, misconfigurations, and architectural gaps across telecom environments.

12

Threat Intelligence Report 2025

SOC telemetry shows the threat surface is expanding from within. Misuse, misconfigurations, and legacy exposure are recurring themes. Telcos must shift from reactive defense to proactive hygiene, visibility, and forensic capability, or risk being breached by what they already own.

VAPT revealed patch neglect as a primary vulnerability source. Quarterly Vulnerability Assessment and Penetration Testing (VAPT) scans across 1000+ IPs showed:

*   76% of vulnerabilities stemmed from missing security patches
*   SSL/TLS misconfigurations enabled POODLE, MITM, and DoS attacks
*   Unsecured protocols like FTP and HTTP remained in active use
*   “End-of-life” systems were still deployed in production environments

Patch latency is an active threat vector. Telcos must treat patching as a frontline defense, not a back-office task.

Application-layer vulnerabilities remain widespread. Application security scans revealed persistent flaws across telecom-facing platforms:

*   Broken access control and IDOR enabled unauthorized data access and privilege escalation
*   SQL injection and stored XSS exposed backend systems and subscriber data
*   Unrestricted file uploads allowed remote code execution and malware deployment
*   CORS misconfigurations enabled unauthorized cross-origin access

Telecom web apps are not immune to commodity exploits. As operators expand digital services, application-layer security must match infrastructure-grade rigor.

Forensic investigations highlight stealthy attacker behavior. Recent forensic investigations reveal attackers increasingly use “living off the land” tactics, leveraging legitimate tools and processes already present on telecom systems to evade detection. Instead of deploying custom malware, adversaries blend into routine operations to bypass security controls. Observed techniques include:

*   PowerShell scripts executed across multiple systems simultaneously
*   Root-level modification of security utilities to evade detection
*   Remote shell scripts used for crypto mining via SSH ports
*   Executable path manipulation mimicked legitimate processes
*   Data staging observed across five nodes, aggregating system and user info

These techniques show “living off the land” strategies are now matching traditional APT methods like zero-days and supply chain attacks.

MBSS audits show gaps in baseline hardening. Minimum Baseline Security Standards audits (MBSS audits) run by Nokia Managed Security Services teams across customer networks revealed:

*   35.3% of systems failed compliance checks in June 2024
*   Only 25.5% of non-compliant systems were remediated by May 2025
*   Common violations included:
    *   Nodes not integrated with authorized servers or SNMPv3
    *   Idle session and account lockout policy violations
    *   HTTP and TLSv1 communications still enabled
    *   Weak password complexity, age, and history enforcement

Without consistent hardening, telco infrastructure remains vulnerable to low-effort compromise and the need for frequent MBSS audits is heavily recommended.

13

Threat Intelligence Report 2025

### Global Title Abuse and Interconnect Risks

#### Context

Signaling trust assumptions are breaking down. Global Title (GT) leasing, a practice where operators lease their Global Titles to third parties, masks message origins, enabling large-scale fraud, surveillance, and abuse.

#### Impact

Sets a precedent likely to influence other regulators. Compromised GTs facilitate SMS OTP theft, location tracking, silent surveillance, and DoS.

#### Key Facts

*   GT leasing banned by Ofcom (April 2025) for UK number ranges
*   Provisions: No leasing, no sub-allocations, strengthened holder controls
*   Risks: Traceability gaps, weakened vetting, cross-border exposure

Ofcom’s GT leasing ban is a global first; expect rising scrutiny of interconnect security.

Consider joining the GSMA Global Title Leasing Code of Conduct (CoC).

14

Threat Intelligence Report 2025

#### Recommended Mitigations

*   Continuously maintaining signaling firewall configurations to keep up with
*   Enforce strict GT filtering and transparent ownership
*   Vet third-party access rigorously
*   Monitor signaling traffic across the network for suspicious patterns, especially on roaming interconnections
*   Consider blocking GTs with obvious only malicious traffic
*   Conduct proactive signaling threat hunting

“With the advent of AI, AI-generated phishing has become really scary, particularly in this region where many people speak Arabic. And when you craft the e-mail in Arabic in a perfect manner… most people have that habit of looking at English only, but this creates a big problem.”
- Director of Security, Major CSP in the Middle East

### Offensive Use of AI by Threat Actors

#### Context

AI is increasingly influencing the attack lifecycle, accelerating phases such as reconnaissance, exploitation, and persistence. Telecom networks present a broad attack surface - RAN, signaling protocols, core functions, OSS/BSS platforms etc. - all of which could be impacted by AI-enhanced techniques.

#### Observed Trends Based on Global Survey

*   Phishing and social engineering are the leading root cause of major incidents globally, cited in 25.6% of cases
*   While credential theft drives just 10% of major incidents globally, it spikes to 27% in APAC, often linked to SIM swap attacks that enable account takeovers

#### AI Attack Capabilities

Threat actors are already using AI for phishing and credential attacks, while additional techniques are emerging as generative AI becomes more pervasive:

*   **Phishing and vishing**: AI-generated emails and voice cloning are making social engineering more convincing and scalable
*   **Credential attacks**: AI models trained on breach data accelerate password guessing and credential stuffing
*   **Malware evasion**: Early demonstrations show AI can support polymorphic techniques, enabling dynamic code mutation to evade detection
*   **Synthetic identity fraud**: Generative models could create realistic forged documents and synthetic identities for onboarding fraud
*   **Reconnaissance and exploit generation**: AI could assist in scanning telecom protocols and generating exploit scripts
*   **Adaptive botnets/DDoS**: Future scenarios include reinforcement learning optimizing attack vectors and timing for multi-vector floods

15

Threat Intelligence Report 2025

#### Impact

*   Reduced time-to-exploit across all phases of the telecom kill chain
*   Increased persistence through adaptive malware and signaling abuse
*   Lower barrier to entry via AI-driven ‘cybercrime-as-a-service’ kits

#### Recommended Mitigations

*   Real-time threat detection through continuous analysis and correlation of global intelligence feeds
*   Automated, adaptive response mechanisms that dynamically adjust security policies to evolving threat contexts
*   Just-in-Time (JIT) Security frameworks, which apply targeted protection only when and where necessary, minimizing service disruptions
*   Agentic AI architectures capable of cross-domain coordination and continuous learning to anticipate and mitigate sophisticated attacks

#### Telecom-Specific Risks

While some techniques have been demonstrated in research or limited attacks, others remain emerging scenarios that operators should monitor:

*   **Network-resident implants**: AI could adapt implants for vendor-specific VNFs, modify binaries post-update, and mimic legitimate signaling to reduce detection likelihood
*   **Signaling exploits**: AI may assist in identifying optimal interception paths across SS7/Diameter/GTP, generating fuzzing sequences for protocol edge cases, and tuning attack parameters to evade anomaly-based detection
*   **RAN and endpoint compromise**: AI could automate rogue base station configuration, optimize PCI/RSRP to attract devices, and generate polymorphic firmware variants for different RAN vendors, enabling IMSI harvesting or OTA spyware injection
*   **Supply chain**: AI might support reverse-engineering of update formats, embedding malicious code that mimics legitimate functionality and passes automated acceptance tests
*   **Manipulation of telecom AI**: Adversarial inputs, model extraction, and data poisoning could target operator AI systems for fraud detection, traffic optimization, or anomaly detection, leading to potential service disruption

“AI-driven bots trying to abuse signaling… it’s really challenging to counter that because we wouldn’t know whether it’s real traffic, malicious payload, or actual signaling itself.”
- Associate Director, Access Technology Development, Major CSP in North America

16

Threat Intelligence Report 2025

### Threats to AI/ML Models in Telecom Networks

#### Context

Telecom operators are embedding AI/ML into every layer of their networks, from OSS/BSS automation and network optimization to fraud prevention and SOC/NOC operations. These deployments face the same classes of attacks observed in the broader AI ecosystem, with clear parallels for telecom environments:

| Threat Type                 | Definition                                                                                                                            | Industry Example                                                                                             | Possible Telco Scenario