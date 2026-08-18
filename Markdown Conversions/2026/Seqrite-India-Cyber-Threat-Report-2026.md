# India Cyber Threat Report 2026

Organization: Seqrite  
Report Title: India-Cyber-Threat-Report  
Year: 2026  

Copyright ©2025.
All rights reserved. Quick Heal Technologies Ltd.  
This report has been developed by Quick Heal Technologies Limited (“Seqrite”). The information contained herein has been obtained or derived from sources believed by Seqrite to be reliable. However, Seqrite disclaims all warranties as to the accuracy, completeness, or adequacy of such information. This report is made available on “as-is” basis and we shall bear no liability for errors, omissions, or inadequacies in the information contained herein, or interpretations or reliance thereof.  
The information contained herein should not be relied upon as a substitute for specific professional advice. Professional advice should always be sought before taking any action based on the information provided.  
The material in this publication is copyrighted and protected by intellectual property legislations. You must not distribute, modify, transmit, reuse, or use the contents of the report for public or commercial purposes, including the text, images, presentations, etc., without prior written consent from authorised representative of Seqrite.  

INDIA CYBER THREAT REPORT 2026 3

## Table of Contents
- [Foreword](#foreword)
- [Executive Summary](#executive-summary)
- [India Under Cyber Siege: The 2025 Threat Outlook](#india-under-cyber-siege-the-2025-threat-outlook)
- [The State of Malware in India](#the-state-of-malware-in-india)
- [Malware Warranting Attention](#malware-warranting-attention)
- [Detection Metrics Across Infrastructure Type: Cloud vs On-Premises](#detection-metrics-across-infrastructure-type-cloud-vs-on-premises)
- [The State of Ransomware](#the-state-of-ransomware)
- [Top Ransomware and Hacktivist Groups 2025](#top-ransomware-and-hacktivist-groups-2025)
- [Network-Based Exploits](#network-based-exploits)
- [Host-Based Exploits](#host-based-exploits)
- [Android Threat Landscape](#android-threat-landscape)
- [Top Zero-Day Threats 2025](#top-zero-day-threats-2025)
- [Geographical Hotspots](#geographical-hotspots)
- [Industry Insights](#industry-insights)
- [Windows Threat Landscape](#windows-threat-landscape)
- [Major Cyber Campaigns of 2025](#major-cyber-campaigns-of-2025)

---

## Foreword

It gives me great pride to present the India Cyber Threat Report 2026, a comprehensive analysis from Seqrite Labs, India’s largest malware analysis centre, monitoring over 8 million endpoints. The past year has been shaped by global political tensions, accelerated digital adoption, and the growing role of artificial intelligence in both innovation and threat creation.  

No sector and no state in India are immune to cyberattacks. As the digital ecosystem expands, fraud and scams have emerged as universal concerns. In response, we launched AntiFraud.AI, India’s first predictive fraud prevention platform, using behavioural analytics to protect citizens against digital financial fraud.  

Our annual Cybersecurity Maturity Survey, with participation from over 180 organisations, highlighted gaps in predictive threat detection, incident response readiness, and data privacy governance. Guided by these insights, we strengthened our enterprise offerings, including Seqrite Data Privacy, to help organisations anticipate threats, safeguard sensitive data, and meet regulatory requirements. We also launched Seqrite Threat Intelligence, Seqrite Malware Analysis Platform, and Seqrite Intelligent Assistant, as well as a deep dive into the threat landscape and partaking in agentic-AI capabilities. This year, we further unveil Ransomware Recovery as a Service and Digital Risk Protection Service which will enable organisations to move from reactive cybersecurity to strategic cyber resilience, protecting their digital footprint, safeguarding their brand reputation, and ensuring uninterrupted operations. At the core of these solutions is AI driven intelligence, powered by our patented GoDeep.AI technology. Last year, we received our ninth patent, reflecting our commitment to innovation. Our products continue to achieve the highest scores from AVLab Poland and AV-TEST certifications, validating their effectiveness.  

Adversaries are evolving rapidly, utilizing automation and generative AI to adapt in real-time. The report highlights rising risks from AI-generated phishing, cloud identity compromise, and data integrity manipulation. It emphasizes predictive defense, AI-powered threat correlation, zero-trust identity management, ransomware resilience, and cross-industry collaboration as pillars for strengthening digital defenses. In all we do, we remain true to our core purpose to innovate, simplify, and secure the digital ecosystem for citizens and enterprises alike.  

Quick Heal Technologies Limited continues to represent India on the global cybersecurity stage, collaborating with the US NIST-NCCoE’s data classification initiatives. As the first Indian cybersecurity-focused company to join the United States Artificial Intelligence Safety Institute Consortium, we advance responsible AI development and safer global digital ecosystems.  

Our teams defend the nation’s digital frontiers with vigilance and expertise. I invite you to explore this report’s findings, predictions, and recommendations. Together, we can create a secure, trusted, and resilient digital future for India.  

**Dr. Kailash Katkar**  
Chairman and Managing Director  
Quick Heal Technologies Ltd  

INDIA CYBER THREAT REPORT 2026 4

## Foreword

I am pleased to welcome you to the 2026 Seqrite Threat Report, an in-depth analysis of India’s evolving cyber landscape. The past year has been one of unprecedented complexity; it was a year that witnessed a war with our neighbouring country, as well as the emergence of a parallel cyber conflict that tested the strength and resilience of our digital infrastructure.  

Hence, the country has witnessed a significant surge in cyber incidents, reflecting both the rapid pace of digital adoption and the growing sophistication of adversaries. Seqrite Labs, India’s largest malware analysis centre monitoring over 8 million endpoints, has tracked and analysed this surge, providing actionable intelligence to enterprises, government institutions, and citizens.  

Our findings indicate that India’s cyber threat landscape is being shaped by increasingly automated, AI-assisted, and cross-platform attacks. Maharashtra, Gujarat, and Delhi were the most affected states, with Mumbai, New Delhi, and Kolkata emerging as the top cities in terms of incident density. Across various industries, including Education, Healthcare and Pharmaceuticals, and Manufacturing, these sectors remained the most targeted, reflecting both their economic and societal criticality. We also observed that Trojans and infectors together formed nearly 70 percent of all attacks, while ransomware exceeded one million detections, driven by double extortion campaigns and supply chain infiltration.  

Among the alarming trends of 2025, AI-assisted phishing frameworks capable of real-time, contextual responses and the weaponization of OAuth tokens for cloud identity compromise stood out, alongside modular malware that combines remote access Trojans with automation, signalling the industrialization of cybercrime in India.  

As we look ahead to 2026 and beyond, the threat environment will continue to evolve, becoming faster, smarter, and more adaptive. Generative AI will shape both attack and defense, hybrid and cloud-native surfaces will expand, and trust-based systems, including digital identities, will come under greater scrutiny. To keep enterprises a step ahead of evolving threats, Seqrite this year further strengthens its portfolio by launching two new services including Ransomware Recovery as a Service and Digital Risk Protection Service, which will help enterprises safeguard operational uptime and brand reputation by combining rapid post-attack recovery with proactive identification and neutralization of external digital threats. In addition, Seqrite Labs remains committed to equipping organisations with predictive intelligence, AI-powered defense capabilities, and actionable insights to help safeguard digital assets and preserve trust.  

This report is an invitation to all stakeholders, including enterprises, policymakers, and citizens, to understand the evolving threats, recognise their implications, and engage in collective, proactive cybersecurity practices.  

**Dr. Sanjay Katkar**  
Joint Managing Director  
Quick Heal Technologies Ltd.  

INDIA CYBER THREAT REPORT 2026 5

## Executive Summary

Between October 2024 and September 2025, Seqrite’s unified threat telemetry recorded 265.52 million detections across more than 8 million endpoints in India — averaging 505 detections every minute. This staggering volume underscores the relentless and adaptive nature of cyber threats targeting Indian enterprises, driven by a blend of legacy malware, fileless intrusions, AI-assisted phishing, and ransomware-as-a-service (RaaS) operations.  

Behaviour-based technologies such as Next-Gen Antivirus (NGAV) and Anti-Ransomware (ARW) engines identified over 34 million anomalous detections, proving their value as the predictive defense layer against fileless and unknown attacks. Meanwhile, signature-based detections exceeded 230 million, highlighting that despite advances in evasion, traditional malware distribution remains a core component of India’s cybercrime ecosystem. The malware ecosystem remained dominated by Trojans (43%), File Infectors (35%), and Potentially Unwanted Applications (6%), reflecting adversaries’ continued success through social engineering, cracked software, and legacy vulnerabilities.  

Emerging threats such as cryptojacking and fileless persistence showcased a pivot toward stealth and sustained monetization, rather than overt disruption.  

Ransomware, although accounting for less than 1% of total detections, had the highest strategic and financial impact. Activity peaked in January 2025, with 185 incidents and 113,000 detections, driven by campaigns like Xelera and Weaxor.  

From an industry standpoint, the Education, Healthcare, and Manufacturing sectors together accounted for nearly 47% of all detections, underscoring how resource constraints, legacy infrastructure, and open collaboration networks continue to attract large-scale attacks.  

On the geographical front, Maharashtra, Gujarat, and Delhi topped the list of affected states, while Mumbai, New Delhi, and Kolkata emerged as the most targeted cities — a reflection of dense financial, political, and industrial activity zones.  

Globally connected ransomware groups such as Qilin, Akira, Cl0p, and Babuk2 dominated Indian campaigns, while hacktivist entities like Cyber Error System and INDOHAXSEC leveraged geopolitical flashpoints to launch DDoS, phishing, and defacement operations under banners like Operation Sindoor. This convergence of cybercrime and hacktivism marks a growing trend toward hybrid cyber warfare, where financial, political, and ideological motives overlap.  

On the exploitation front, network-based attacks targeting WordPress Plugins, Apache Tomcat, and SysAid reflected continued exploitation of poor patch hygiene, while LNK-based host exploits reaffirmed that simple vectors remain devastatingly effective in unmanaged environments.  

Emerging attack surfaces such as AI frameworks (Langflow) and cloud consoles indicate a shift toward targeting development and automation layers, signaling the beginning of AI stack exploitation.  

The year also witnessed 25 major global and regional cyber campaigns, including Operation Sindoor, GrassCall, and Weaxor, revealing sophisticated supply-chain infiltration, phishing deception, and data extortion tactics. Additionally, the surge in zero-day weaponization from Oracle E-Business Suite to Cisco IOS demonstrates that patch latency remains one of the most exploited weaknesses across enterprises.  

Looking ahead, Seqrite forecasts that 2026 will usher in the era of cognitive intrusions, where adversaries leverage AI to automate reconnaissance, deception, and persistence. The threat battlefield will evolve from code-based to context-aware attacks, demanding defenses that are predictive, autonomous, and intelligence-led.  

INDIA CYBER THREAT REPORT 2026 8

### Key Highlights
- **265.52M Detections**: Recorded across over 8 million endpoints averaging 505 detections every minute.
- **Top Malware Families**: Trojans (~88.4M) and File Infectors (~71.1M) dominated, together making up nearly 70% of all malware detections.
- **Behaviour-Based Detections**: NGAV + Anti-Ransomware blocked ~34M advanced threats, including fileless and encryption-based attacks.
- **Sector Targets**: Education, Healthcare, and Manufacturing sectors recorded 12.5 million detections, accounting for 47% of total volume.
- **Most Affected States**: Maharashtra (36.1M), Gujarat (24.1M), and Delhi (15.4M).
- **Cryptojacking**: Outpaced Ransomware (~0.65M vs ~0.81M), indicating a shift toward stealth monetization.
- **Ransomware Activity**: Peaked in January 2025 with 185 incidents and 113,000 detections, led by Xelera and Weaxor campaigns.
- **Network-Based Exploits**: Exceeded 9.2 million scans, targeting WordPress, Apache Tomcat, and SysAid systems.

ANNUAL THREAT REPORT INDIA 2026 10

## India Under Cyber Siege: The 2025 Threat Outlook

Between October 2024 and September 2025, Seqrite’s unified telemetry recorded an astounding 265.52 million detections over 8 million endpoints, translating to nearly 727,000 detections per day or around 505 detections every minute.  

This data reflects the unrelenting pace and sophistication of cyberattacks targeting Indian organisations, driven by a mix of legacy exploits, fileless malware, and evolving ransomware campaigns.  

### Yearly Detection Overview
Detection volumes remained consistently high throughout the 12-month period, fluctuating between 17.6 million and 23.1 million detections per month.  

Peaks were observed in October 2024 and January 2025, coinciding with major ransomware and phishing activity, while a steady plateau from April to August reflected sustained but controlled intrusion attempts.  

This consistency suggests that India’s threat ecosystem has shifted from episodic outbreaks to continuous, automation-driven attack patterns.  

Threat actors are no longer waiting for opportunities. They are constantly scanning, exploiting, and monetizing digital weaknesses.  

### Behaviour-Based Detections: The Predictive Shield
Behavioural analytics — powered by Next-Gen Antivirus (NGAV) and Anti-Ransomware (ARW) technologies identified over 34 million detections during the year.  

These detections focused on identifying anomalous execution, encryption activity, and fileless intrusion techniques, often bypassing traditional signature-based models.  

Behaviour-based detections saw notable spikes during Q1 2025, correlating with heightened ransomware activity and large-scale phishing-to-ransomware conversion chains.  

This clearly indicates that proactive behavioural layers now form the first line of defense against emerging and unknown threats.  

### Signature-Based Detections: The Dominant Volume Layer
Signature-based detections encompassing network, memory, and email scans accounted for the majority of observed threat activity, exceeding 415 million detections[^1].  

While traditional in nature, these detections remain crucial in catching mass malware distribution, brute-force network intrusions, and exploit-driven attacks.  

Network scanning remained the most exploited entry point, accounting for more than 90% of total detections underscoring that exposed, unpatched systems continue to be the weakest link in enterprise security posture.  

[^1]: *Note: Total cumulative signature and network scan logs across comprehensive enterprise telemetry.*

INDIA CYBER THREAT REPORT 2026 12

## The State of Malware in India

The malware ecosystem remained heavily skewed toward high-volume, low-complexity threats such as Trojans, Infectors, and Worms. Together, these accounted for over 65% of all detections, underscoring how adversaries continue to rely on social engineering, cracked software, and legacy vulnerabilities to compromise systems at scale.  

While overall detection volumes stayed steady across the year, newer monetization-driven campaigns, particularly cryptojacking signalled a shift towards stealthy, profit-centric cybercrime.  

### Trojans
**The Prime Infection Driver (~ 88.44M Detections)**  
Trojans represented the single largest malware family, contributing roughly four in every ten infections.  

They acted as the initial payload in multistage campaigns, enabling credential theft, data exfiltration, or ransomware deployment. Dominant variants such as `W32.Pioneer.CZ1`, `Trojan.Agent`, and `W32.Expiro.R3` leveraged phishing attachments, weaponized documents, and compromised websites.  

Trojans continue to serve as the backbone of cybercrime operations due to their adaptability and modular design.  

### Infectors
**Persistent Legacy Threats (~ 71.09M Detections)**  
File-infecting malware remained the second-largest category, reflecting continued exposure in unpatched Windows environments and older endpoint infrastructures.  

Infectors modify legitimate executables to ensure reinfection and persistence, often spreading through USB drives and shared folders. Despite improved behavioural detection, their endurance highlights slow patch adoption and outdated software ecosystems in several sectors.  

INDIA CYBER THREAT REPORT 2026 14

### Worms
**Enduring Network Pests (~ 13.81M Detections)**  
Worms continued exploiting SMB and AutoRun vulnerabilities, particularly in education, manufacturing, and small business networks. Their ability to propagate laterally and reactivate after cleaning makes them a persistent concern for unmanaged and legacy systems.  

### PUAs
**Hidden Gateways for Intrusion (~ 13.27M Detections)**  
PUAs accounted for nearly one in every fifteen detections, reflecting widespread presence across both home and enterprise endpoints. While often dismissed as low-risk, these applications act as launchpads for credential stealers, adware, and miners. Most originate from cracked utilities, fake browser extensions, or deceptive installers, blurring the boundary between nuisanceware and active threats.  

### Exploits
**From Mass Attacks to Targeted Intrusions (~ 9.20M Detections)**  
Exploits contributed a smaller share of detections but posed a significant strategic risk. Attackers increasingly targeted specific web servers, email gateways, and ERP systems rather than launching broad exploit-kit campaigns. This shift toward precision reflects the evolution of exploitation tactics from opportunistic compromise to controlled entry for APT operations.  

### Cryptojacking
**The Silent Profit Engine (~ 6.49M Detections)**  
Cryptojacking emerged as one of the fastest-growing categories, with detections nearing five million. Adversaries hijacked compute power to mine Monero and PKT coins, primarily by exploiting RDP, Docker, or cloud misconfigurations. Its stealthy nature causing performance degradation rather than data loss makes it a profitable, low-noise alternative to ransomware.  

### Ransomware
**Low Frequency, High Impact (~ 0.81M Detections)**  
Ransomware volume remained relatively small, but the impact per incident was severe. Modern strains like Weaxor, Xelera, and WantToCry used multi-extortion tactics, combining encryption, data theft, and public leaks. Most infections originated from Trojans or credential abuse, demonstrating ransomware’s evolution into a post-compromise weapon rather than a random payload.  

### Adware
**Declining but Widespread (~ 0.49M Detections)**  
Adware showed the steepest decline, partly due to stronger browser protection and mobile OS security.  

However, millions of detections still originated from malvertising networks and bundled installers.  
While relatively benign, adware contributes to alert fatigue and can conceal more serious payloads within telemetry data.  

INDIA CYBER THREAT REPORT 2026 15

## Malware Warranting Attention

### W32.Expiro.R3
- **Type:** File Infector
- **Risk Level:** High
- **Description:** A legacy yet highly destructive file infector that targets executable files (both 32-bit and 64-bit). It spreads through cracked software and removable drives, and once active, it modifies application files, spreads through network drives, and can execute remote commands, allowing large-scale propagation across networks.

### Trojan.KillAv.DR
- **Type:** Trojan
- **Risk Level:** High
- **Description:** A Trojan known for disabling antivirus processes (“Kill AV”). It spreads through malicious email attachments or compromised sites and often disguises itself with legitimate Windows icons. Once executed, it can steal system and network information and deliver additional payloads such as spyware or remote access tools.

### Trojan.Floxif.E5
- **Type:** Trojan
- **Risk Level:** High
- **Description:** Distributed through infected USB drives and bundled software installers (notably a tampered version of CCleaner). It collects user and system details including unique IDs and MAC addresses, and transmits them to command-and-control servers, acting as both a data stealer and downloader for further infections.

### Worm.Autoit.Sohanad.S
- **Type:** Worm
- **Risk Level:** High
- **Description:** A self-replicating worm that spreads rapidly through messaging apps, removable drives, and network shares. It disguises itself as a Windows folder icon (`.exe`), tricking users into execution, after which it replicates to all connected drives enabling fast, uncontrolled spread in local networks.

### W32.Brontok.Q
- **Type:** Worm
- **Risk Level:** Medium
- **Description:** A resilient worm transmitted through infected USB devices and email attachments. It disables security tools, alters system settings, and modifies the HOSTS file to block access to security websites. Though older, it remains active in networks with weak endpoint protection.

### Trojan.NSIS.Miner.SD
- **Type:** Trojan/Cryptominer
- **Risk Level:** High
- **Description:** A resource-abusing Trojan that installs through malicious freeware or compromised websites. It secretly uses system resources for cryptocurrency mining (e.g., Bitcoin), heavily degrading performance. Additionally, it modifies system files, opens backdoors, and enables further malware infiltration.

INDIA CYBER THREAT REPORT 2026 17

## Detection Metrics Across Infrastructure Type: Cloud vs On-Premises

Seqrite’s telemetry data highlights a clear distinction between detection trends across cloud and on-premise environments, underscoring differences in adoption, exposure, and risk density.  

Over the 12-month period, detections across cloud and on-prem infrastructures revealed that while cloud adoption is steadily increasing, on-prem systems remain the dominant source of threats due to legacy dependencies and broader endpoint bases.  

### Key Insights
- **On-Premises Risks**: On-premises environments account for 91% of all threat activity on-prem (~3.5M monthly supported by stronger controls, but faces exposure to automated attacks.
- **Cloud Exposure**: Cloud contributes only 9% of detections, much larger endpoint base (~19 lakh), legacy systems, and higher exposure to targeted threats such as identity monitoring critical.
- **Endpoint Visibility**: Visibility alone is not enough for cloud. Many cloud intrusions bypass traditional malware vectors and therefore do not surface in endpoint detection logs, making configuration drift, identity misuse, and access control monitoring critical.
- **Hybrid Defense Needs**: With high-volume on-prem and stealthy, identity-centric cloud attacks, enterprises require integrated visibility and AI-powered security to close the gap. Legacy and unmanaged devices remain the primary attack surface.

INDIA CYBER THREAT REPORT 2026 19

## The State of Ransomware

Ransomware activity through FY25 revealed a clear pattern — a sharp escalation in the early months, steady containment mid-year, and a resurgence toward the close of the fiscal period.  

The telemetry highlights how adversaries continuously evolved tactics, transitioning from mass-scale attacks to precision-targeted campaigns.  

- **Early 2025: The Apex of Ransomware Activity**  
  January 2025 recorded the highest surge, with 185 incidents and over 113,000 detections, representing a major ransomware wave driven by campaigns such as Xelera and Weaxor.  
  Attackers leveraged large phishing infrastructures, cracked software, and malicious loaders to propagate payloads at scale, exploiting weak patch hygiene and credential reuse.  

- **Mid-Year: Stabilization Through Proactive Containment**  
  February through April saw a gradual decline in detections from 74,000 to 69,000 per month signaling effective containment through behavioural and anti-ransomware controls.  
  Despite the reduction, incident volumes remained steady, underscoring the persistent probing nature of ransomware operators testing endpoint and network defenses.  

INDIA CYBER THREAT REPORT 2026 20

- **May 2025: Tactical Shift to Targeted Intrusions**  
  A distinct inflection was observed in May, with 126 incidents but comparatively lower detections (~57,000). This mismatch indicates low-volume, high-impact enterprise-focused intrusions, where attackers infiltrated environments through supply-chain or remote service vectors before triggering encryption.  

- **Late 2025: Variant Recycling and Renewed Activity**  
  August and September marked another climb, with detections exceeding 60,000 per month and incidents rising to 107. The activity corresponds to the re-emergence of retooled ransomware families, leveraging old exploits and stolen credentials, a trend consistent with post-compromise persistence tactics.  

### Key Insights
1. **Sustained Threat Pressure**: Ransomware remained one of the most consistent and financially motivated threats across the year, with continuous detection events despite intermittent declines.  
2. **Behavioural Defense Effectiveness**: The incident-to-detection ratio averaged 1:700, demonstrating that early-stage behavioural and heuristic layers successfully disrupted most encryption attempts.  
3. **Shift to Enterprise-Grade Targets**: The spike in incidents during May points to strategic targeting of high-value environments over indiscriminate mass campaigns.  
4. **Persistent Scanning Activity**: Even during quieter months, detections never dropped below 55,000 - confirming that adversaries maintained ongoing network reconnaissance and payload testing.  
5. **Resilient Defense Posture**: By late 2025, defenses matured to intercept ransomware across pre-encryption and lateral movement stages, reflecting stronger response automation and visibility across infrastructures.  

INDIA CYBER THREAT REPORT 2026 21

## Top Ransomware & Hacktivist Groups 2025

### The Human Faces Behind Automation: Mapping the Global and Indian Threat Ecosystem
Following the surge in ransomware detections and incidents in 2025, Seqrite Labs traced the operational footprints of major ransomware and hacktivist groups that shaped the global and Indian threat landscape.  

The data reveals an increasingly industrialized ecosystem — where ransomware syndicates operate like businesses, and hacktivist groups exploit geopolitical tensions to amplify chaos and influence public discourse.  

2025 marked the consolidation of ransomware-as-a-service (RaaS) operations, with Qilin, Akira, and Cl0p dominating globally. These groups shifted tactics from mass encryption to data extortion and cloud compromise, often using OAuth and API abuse for lateral movement.  

Groups like Play and Ransomhub leveraged automation and AI for faster reconnaissance and adaptive encryption payloads. Emerging players like Incransom and Lynx illustrated how smaller affiliates are rapidly scaling through shared tooling and leaked RaaS infrastructure.  

INDIA CYBER THREAT REPORT 2026 23

India’s ransomware landscape reflects global-to-local spillover — where international syndicates operate through localized affiliates and regionalized campaigns.  

Groups like KillSec and Babuk2 were especially active against BFSI, healthcare, and manufacturing, exploiting remote desktop exposure and supply chain vulnerabilities.  

New entrants such as FunkSec and TheGentlemen targeted SMBs and educational institutions, leveraging phishing and infector hybrids.  

The data underscores how India is increasingly part of the global ransomware economy, not just a peripheral target.  

INDIA CYBER THREAT REPORT 2026 24

Hacktivism in 2025 evolved from symbolic website defacements to coordinated psychological and influence operations. Leading groups such as Cyber Error System, INDOHAXSEC, and HellR00ters orchestrated large-scale DDoS, phishing, and defacement attacks on Indian government and media entities, often timed around geopolitical flashpoints.  

Their campaigns blended propaganda, misinformation, and digital disruption, reflecting a new phase of cyber activism intertwined with geopolitics. Notably, the activity spike during Operation Sindoor highlighted hacktivism’s transition from nuisance-level attacks to strategic cyber offensives with real-world impact.  

INDIA CYBER THREAT REPORT 2026 25

### Strategic Takeaways
- **Ransomware Ecosystem**: Now an organized economy with affiliate networks, revenue sharing, and service-based operations (RaaS).
- **India’s Growing Digital Footprint**: Makes it a lucrative ransomware frontier, with both local and global groups exploiting hybrid infrastructures.
- **Hacktivism Has Matured**: Into cyber influence warfare, blurring lines between political protest, state-sponsored disinformation, and cybercrime.
- **Defensive Posture**: Must evolve toward predictive intelligence, attribution-driven detection, and cross-sector information sharing to disrupt these ecosystems early.

INDIA CYBER THREAT REPORT 2026 26

## Network-Based Exploits

Network exploitation remained a dominant intrusion vector through 2025, reflecting a concerning mix of poor patch hygiene, expanding attack surfaces, and rapid weaponization of newly disclosed vulnerabilities. Seqrite telemetry revealed that attackers actively targeted internet-facing applications such as CMS platforms, middleware, and administrative consoles, with exploit traffic often automated through botnets and mass-scan tools.  

### Top Network Exploits Observed

#### WordPress Plugins Exploitation: The New CMS Epidemic
- **Total affected customers:** 3,075  
- **Detection count:** 394  
- **Vulnerability:** CVE-2025-3102 – SureTriggers/OttoKit Authentication Bypass  
- Attackers leveraged missing validation in authentication tokens to create rogue admin accounts, leading to full site takeover, defacement, and SEO poisoning.  
- This campaign was largely automated, with exploit traffic originating from botnets leveraging compromised VPS nodes and targeting Indian SMEs and content-hosting providers.  

#### Langflow RCE: AI Development Environments Under Fire
- **Total affected customers:** 2,861  
- **Detection count:** 12  
- **Vulnerability:** CVE-2025-3248 – Unauthenticated RCE through API endpoint  
- Exploitation attempts involved Python `exec()` abuse, granting full code execution through unsecured `/api/v1/validate/code` endpoints.  
- The appearance of this CVE in active telemetry marks the first wave of AI stack–oriented attacks, signaling that developer and ML infrastructure are becoming valuable targets for reconnaissance and persistence.  

INDIA CYBER THREAT REPORT 2026 27

#### Apache Tomcat Exploitation: Persistent Entry through Middleware
- **Total affected customers:** 234  
- **Detection count:** 97  
- **Vulnerability:** CVE-2025-24813 – Path Equivalence / Partial PUT Exploit  
- Attackers exploited writable servlet paths to overwrite serialized objects, deploy webshells, and establish persistence within application servers. These intrusions align with tactics used by APT actors and cybercrime groups focusing on data theft and internal pivoting from compromised middleware.  

#### SysAid XXE Exploit: Targeting IT Management Consoles
- **Total affected customers:** 225  
- **Detection count:** 57  
- **Vulnerability:** CVE-2025-2775 – XML External Entity Injection  
- Adversaries exploited `/mdm/checkin` and `/serverurl` endpoints to read system files and escalate privileges. Given SysAid’s privileged position in IT infrastructure, successful exploitation provides attackers with network-wide administrative access.  

#### MailEnable XSS: Phishing Through Infrastructure
- **Total affected customers:** 245  
- **Detection count:** 40  
- **Vulnerability:** CVE-2025-44148 – Reflected XSS (`failure.aspx`)  
- Exploits used crafted URLs to inject JavaScript into admin sessions, leading to session hijacking and malicious redirects. While older in nature, MailEnable’s wide usage across self-hosted enterprise mail servers keeps it a consistent target for exploit recycling.  

### Key Takeaways
- HTTP-based exploitation is now a dominant attack vector, driven by automated reconnaissance and public exploit kits.  
- CMS platforms like WordPress remain persistently vulnerable, serving as a convenient entry point into corporate and government networks.  
- Middleware and DevOps tools (Tomcat, Langflow, SysAid) represent high-value targets, bridging application and infrastructure layers for lateral movement.  
- The expansion of exploit activity into AI ecosystems marks a major evolution in threat targeting for 2026 and beyond.  
- Network defense must shift toward continuous exposure management, real-time patch orchestration, and behavioural network detection to counter this new era of stealth exploitation.  

INDIA CYBER THREAT REPORT 2026 28

## Host-Based Exploits

A surge in LNK-based exploits dominated host-level detections this year, revealing how attackers continue to exploit simple Windows shortcut vulnerabilities to achieve code execution, persistence, and lateral movement. Over 8 million detections were recorded, with `LNK.Cmd.Exploit.F` leading due to its ability to self-propagate across USBs and shared drives. These exploits thrive in environments with weak removable media controls, legacy systems, and user-driven file interactions, making them a persistent challenge for enterprises.  

### LNK.Cmd.Exploit.F
The most widespread host exploit, capable of autonomously spreading through removable drives, shared folders, and emails. It executes malicious code when users open or preview infected shortcut files, often installing secondary malware and causing rapid propagation across internal networks.  

### LNK.Exploit.Gen
A generic Windows shortcut exploit that triggers arbitrary code when parsed. It is widely distributed through phishing campaigns and compromised archives, enabling attackers to deploy payloads or escalate privileges with minimal user interaction.  

### LNK.Exploit.Cpl.Gen
Abuses Control Panel shortcut (`.CPL`) handling flaws to execute hidden payloads. Often used to gain persistence or deploy backdoors, allowing attackers to maintain long-term footholds within enterprise networks.  

INDIA CYBER THREAT REPORT 2026 29

### LNK.USB.Exploit
Targets USB autorun behaviours to inhite hosts when removable media is accessed. It spreads silently across devices and is commonly observed in controlled or isolated environments where network security tools have limited visibility.  

### HTML/IFrame_Exploit.CE
A browser-based exploit using malicious HTML or iFrame injections to execute drive-by payloads. It takes advantage of outdated browser plugins or unpatched vulnerabilities, enabling silent compromise during routine browsing.  

### Recommended Actions
- **Harden Endpoint and USB Controls**: Disable Windows autorun features and restrict `.LNK` and `.CPL` execution from removable or shared drives. Enforce device control policies to prevent unauthorised USB usage.
- **Implement Application Allowlisting**: Allow only trusted executables to run. Block unknown or unsigned binaries, especially those launched through explorer or shortcut parsing.
- **Proactive Threat Hunting and Monitoring**: Regularly scan for LNK-related artifacts and suspicious explorer-launched processes. Monitor network shares for abnormal file creation or replication activity.
- **Update Legacy Systems and Patches**: Apply security updates that fix known shortcut parsing flaws (e.g., CVE-2010-2568) to eliminate long-standing exploit vectors.
- **Build User Awareness**: Educate employees about risks associated with unknown USB drives, phishing attachments, and shortcut-based files to minimize accidental infections.

INDIA CYBER THREAT REPORT 2026 30

## Android Threat Landscape

### 1. Lured and Compromised: The Rise of Digital Honey Traps
Digital honey traps have become a powerful social engineering tool where attackers build emotional connections over social media, WhatsApp, or dating apps to extract sensitive information. These profiles are often AI-generated, complete with realistic photos and crafted backstories. Conversations typically begin casually, then shift toward personal bonding, and finally, subtle probing for workplace details, internal documents, or private media.  

In several Indian cases, personnel from the Army, paramilitary forces, and defense research units were targeted through such tactics. Victims were manipulated into sharing operational details or compromising information, which attackers later used for blackmail or coercion. The danger of honey traps lies in the fact that no malware is required. The breach occurs purely through trust exploitation. Raising awareness and encouraging quick reporting remain the strongest defenses.  

- **Risk Level:** Medium  
- **Target Sectors:** Government, Defense, Intelligence  
- **Region:** India, Asia-Pacific  

### 2. ‘NextGen mParivahan’ Malware Returns with Enhanced Stealth
A more sophisticated version of the fake “NextGen mParivahan” malware resurfaced alongside the app’s rebranding. Attackers send SMS messages about pending traffic challans, complete with vehicle numbers and violation codes, directing users to download a malicious APK. The fake app looks identical to the real government interface, making detection difficult for average users.  

Once installed, it requests invasive permissions, hides its icon, and silently collects device notifications, SMS, and sensitive user’s data. It also shows a fake challan-payment page to steal UPI or card details. The malware relies on encrypted communication and dynamically generated C2 addresses, allowing it to bypass traditional detection methods.  

These campaigns highlight the growing trend of government-service impersonation for fraud and identity theft.  
- **Seqrite Labs Detection:** Android.Dropper  
- **Risk Level:** High  
- **Region:** India  

### 3. High-Security Registration Plate (HSRP) Scam
The HSRP scam targets vehicle owners by mimicking official booking portals and promoting them through Google ads, SMS alerts, and WhatsApp forwards. These fake sites look authentic, asking users to enter vehicle information and make online payments for plate installation.  

Some campaigns now include links to “HSRP verification apps” that request access to SMS or call data, enabling OTP theft and unauthorised UPI transactions. Victims lose money upfront and unknowingly expose personal information such as RC numbers, addresses, and phone details, and this data is later used for additional fraud. The scam’s success relies on urgency messaging (“final notice”, “fine imposed”) and the lack of verification from users.  

Seqrite blocks malicious URLs linked to this scam.  
- **Risk Level:** Medium  
- **Region:** India  

### 4. SparkKitty Spyware
SparkKitty is a cross-platform spyware family found embedded inside modified versions of gaming apps, TikTok clones, and adult-content apps popular in Southeast Asia. Users often download these apps from third-party stores, unaware that the embedded code silently extracts photos, device information, and app tokens once installed.  

The spyware operates quietly in the background, sending stolen data to remote servers through encrypted channels. Unlike targeted espionage malware, SparkKitty operates broadly, collecting large volumes of personal media from infected devices. Its presence in apps that sometimes pass basic store checks suggests an increased risk from malicious SDKs and developer-side compromise.  

- **Seqrite Labs Detection:** Android.SparkKitty  
- **Risk Level:** High  
- **Region:** Southeast Asia, China  

INDIA CYBER THREAT REPORT 2026 32

### 5. Evolving Android Banking Trojans Pose Serious Financial Threats
Banking Trojans on Android grew significantly more advanced during the year.  

OctoV2 spreads through phishing pages disguised as AI or productivity apps and abuses Accessibility permissions to read screens, stream activity, and perform on-device fraud. Zanubis, originally spotted in Latin America, continues to evolve into a full device-control Trojan that locks screens and captures banking credentials while posing as legitimate service apps.  

The most sophisticated, TsarBot, impersonates Google Play Services and uses precise overlay screens to steal banking logins, credit-card details, and OTPs. It communicates through WebSockets, allowing attackers to execute real-time transactions. These Trojans are part of organized, monetization-driven ecosystems that target global users and rely heavily on social engineering for installation.  

- **Seqrite Labs Detection:** Android.Banker  
- **Risk Level:** High  
- **Region:** Global  

## Top Zero-Day Threats 2025

2025 marked a surge in zero-day weaponization across enterprise, network, and endpoint ecosystems. Threat actors including ransomware and extortion groups — exploited critical flaws within days of disclosure. These attacks underscored the urgent need for faster patch cycles, application isolation, and continuous threat-hunting across hybrid infrastructures.  

### 1. Oracle E-Business Suite (CVE-2025-61882)
A critical unauthenticated RCE flaw exploited by CL0P-linked actors to compromise ERP servers, steal business data, and issue extortion demands.  
- **Impact:** Complete system takeover, database exposure, and lateral movement inside finance and HR networks.  
- **Action:** Patch immediately; restrict public access to EBS; review logs for unusual commands or outbound transfers.  

INDIA CYBER THREAT REPORT 2026 33

### 2. Microsoft Windows Core (CVE-2025-59230 / 24990 / 47827)
Multiple Windows zero-days patched in October 2025 after confirmed in-the-wild exploitation.  
- **Impact:** Privilege escalation and remote execution across enterprise endpoints — enabling domain compromise.  
- **Action:** Deploy the October updates enterprise-wide; verify no deferred patching; hunt for new admin accounts or scheduled tasks.  

### 3. Cisco SNMP “Zero Disco” (CVE-2025-20352)
A remote-code flaw in Cisco IOS/XE devices used to implant rootkits for long-term persistence & network monitoring.  
- **Impact:** Network-level compromise allowing traffic interception and covert C2 channels.  
- **Action:** Patch and restrict SNMP; validate firmware integrity; monitor for rogue outbound traffic from network devices.  

### 4. 7-Zip Symbolic-Link Vulnerabilities (CVE-2025-11001 & 11002)
Two archive-parsing flaws enabling malicious ZIP files to overwrite system files and execute code.  
- **Impact:** Endpoint compromise through user-interaction or automated file extraction.  
- **Action:** Upgrade 7-Zip across all systems; disable auto-extraction on servers; reinforce user awareness on malicious attachments.  

### 5. Adobe AEM Forms (CVE-2025-54253)
An OGNL injection bug allowing pre-authentication code execution; leveraged in ransomware intrusions.  
- **Impact:** Full control of web servers hosting digital forms and portals; potential internal pivot.  
- **Action:** Patch AEM immediately; restrict admin access; scan for webshells and unknown uploads.  

### Strategic Observations
- **Exploitation Latency**: Exploitation now begins within a week of disclosure.
- **Target Attack Surfaces**: Business platforms (ERP, CMS, network firmware), not just endpoints.
- **Patching Effectiveness**: Organisations with strong threat-hunting and asset visibility contained breaches fastest.

INDIA CYBER THREAT REPORT 2026 34

## Geographical Hotspots

INDIA CYBER THREAT REPORT 2026 35

### Top Affected States
1. **Maharashtra** (36.13M detections)  
   Maharashtra registers the highest threat activity, supported by one of India’s largest digital estates, including 556K+ engineering & manufacturing units, 1.5M+ healthcare entities, 473K+ IT & software units, and 765K+ education institutions, creating unmatched adversarial exposure.  
2. **Gujarat** (24.13M detections)  
   Gujarat’s elevated threat levels reflect its massive industrial backbone, comprising millions of manufacturing, engineering, chemical, and textile units, forming dense endpoint clusters frequently targeted by automated and supply-chain-oriented attacks.  
3. **Delhi (NCR)** (15.41M detections)  
   Delhi’s position is anchored in its high-value concentration of 231K+ education entities, 20.9K+ media organisations, 65K+ financial services units, and critical government infrastructure, making it continuously attractive for threat actors.  
4. **West Bengal** (14.35M detections)  
   West Bengal’s threat density is driven by its exceptionally large Energy & Utilities sector (159,983 units), Media & Entertainment (192,077 units), major government networks, and public-service institutions that are recurrent targets.  
5. **Uttar Pradesh** (13.94M detections)  
   Uttar Pradesh reports high detections due to its broad endpoint distribution across 1.14M+ misc. businesses, 163K+ education units, 71K+ IT entities, 111K+ healthcare units, and expansive government services.  
6. **Karnataka** (11.64M detections)  
   Karnataka’s threat profile correlates with its massive IT & software ecosystem (65,714 units), 225K+ engineering & manufacturing units, and 329K+ education organisations, with Bengaluru’s digital-first environment amplifying exposure.  
7. **Tamil Nadu** (7.51M detections)  
   Tamil Nadu’s detections stem from robust industrial networks including 18.9K automotive units, 142K engineering & manufacturing units, 62K consumer goods entities, and 68K real-estate and construction organisations.  
8. **Madhya Pradesh** (7.33M detections)  
   Madhya Pradesh maintains high activity through 106K+ engineering & manufacturing units, 36K+ healthcare entities, 43K+ education units, and 36K+ logistics & transportation organisations, contributing to broad digital exposure.  
9. **Rajasthan** (6.80M detections)  
   Rajasthan’s threat landscape is shaped by its extensive public-sector services, large education systems, and expanding manufacturing and construction footprints, driving significant endpoint presence.  
10. **Telangana** (6.59M detections)  
    Telangana’s exposure is driven by very large healthcare & life sciences clusters (232,863 units), 259K+ education entities, and 182K+ engineering & manufacturing units, alongside Hyderabad’s expanding IT infrastructure.  

INDIA CYBER THREAT REPORT 2026 36

### Top Targeted Cities
1. **Mumbai**: India’s financial capital with dense BFSI, media, and enterprise networks makes it the most targeted.  
2. **New Delhi**: High concentration of government, public-sector, and critical infrastructure drives sustained threat activity.  
3. **Kolkata**: Large public-sector institutions, utilities, and media ecosystems attract continuous intrusion attempts.  
4. **Pune**: Major IT, R&D, education, and manufacturing clusters create a wide and diverse attack surface.  
5. **Surat**: Massive textile and SME manufacturing hubs lead to dense endpoint presence vulnerable to automated attacks.  
6. **Bengaluru**: India’s tech hub with thousands of IT firms and startups creates high-value digital exposure.  
7. **Ahmedabad**: Strong industrial base across textile, chemical, and manufacturing sectors attracts threat actors.  
8. **Hyderabad**: Large healthcare, life sciences, and IT ecosystems make it a lucrative target for data-driven attacks.  
9. **Chennai**: Automotive, manufacturing, and retail supply chains contribute to sustained malware activity.  
10. **Jaipur**: Rapidly growing digital adoption across education, SMEs, and government services increases exposure.  

INDIA CYBER THREAT REPORT 2026 37

## Industry Insights

INDIA CYBER THREAT REPORT 2026 38

### 1. Education & Training (4.92M detections | 18.45%)
Education remained the most targeted sector. Attackers exploited unpatched systems, shared Wi-Fi networks, and poorly secured research infrastructure. Frequent use of `Trojan.Pioneer.CZ1` and `W32.Expiro.R3` malware families indicates large-scale credential theft, coin-mining, and data exfiltration campaigns across universities and training institutions.  

### 2. Healthcare & Pharmaceuticals (3.79M detections | 14.24%)
Healthcare continued to face relentless exploitation, driven by data-rich hospital networks and patient management systems. Malware such as `W32.Expiro.R3` and `Trojan.Eqtonex` were observed compromising EHR platforms, while RAT-based intrusions indicated sustained espionage efforts targeting pharma R&D data and clinical trials.  

### 3. Engineering & Manufacturing (3.79M detections | 14.22%)
Manufacturing and industrial units saw a spike in malware-laced CAD tools, spear-phishing campaigns, and lateral movement through SMB exploits. `Nsis.Bitmin`, `Trojan.Shadowbrokers`, and `KillAv.DR` families dominated detections, underscoring the vulnerability of production and design systems integrated with legacy OT assets.  

### 4. Government (2.88M detections | 10.80%)
The government sector was consistently targeted by state-backed APT campaigns and ransomware groups. Malware such as `LNK.HoudRAT.47401` and `Eqtonex` facilitated espionage, file exfiltration, and disruption of e-governance portals. Increased APT activity points toward strategic intelligence collection and digital disruption motives.  

### 5. Information Technology & Software (2.76M detections | 10.35%)
The IT sector, serving as a backbone for India’s digital economy, faced high malware activity, especially fileless and loader-based attacks. Infections driven by `W32.Mofksys.A4`, `Trojan.GenericPMF` variants, and `Miner.SD` reveal a trend toward supply-chain infiltration and payload staging on developer endpoints.  

### 6. Metals, Mining & Materials (1.23M detections | 4.62%)
This sector witnessed targeted intrusions focused on industrial design theft, production data compromise, and OT system exploitation. `Trojan.Eqtonex` and `PMF.S3146672` were primary threats, often delivered through phishing or compromised ERP environments.  

### 7. Financial Services (1.16M detections | 4.36%)
Financial institutions faced ongoing threats from credential stealers, banking Trojans, and fake update campaigns. Detections of `Trojan.CryptRI`, `Risktool.Bitcoinminer`, and Infostealer variants underline the persistence of financially motivated cybercrime targeting digital banking systems and fintech platforms.  

INDIA CYBER THREAT REPORT 2026 39

### 8. Construction & Real Estate (918K detections | 2.80%)
Construction and real estate saw social engineering-based intrusions leveraging fake tenders and invoice attachments. Malware such as `Trojan.KillAv.DR` and `Hacktool.Keygen` were prevalent, indicating a shift toward industrial espionage and financial fraud campaigns.  

### 9. Consumer Goods & Retail (918K detections | 2.28%)
Retail and consumer goods industries continued to attract attackers through point-of-sale (POS) malware, phishing, and credential-harvesting loaders. Detections suggest exploitation of e-commerce APIs, misconfigured databases, and weakly protected vendor systems.  

### 10. Energy & Utilities (609K detections | 2.9%)
The energy sector recorded steady but significant threats linked to `W32.Sality` and `Eqtonex` variants, hinting at adversaries probing critical power and oil infrastructure. Attacks mainly focused on data reconnaissance and lateral movement, emphasizing the need for continuous OT-IT convergence security.  

### Key Takeaways
- **Education, Healthcare, & Manufacturing** together contribute over 47% of all detections, underlining their critical exposure.  
- **Government & IT Sectors** remain under dual pressure from espionage-driven APTs and commodity malware.  
- **Energy, Finance, & Infrastructure** industries are witnessing cross-domain attack convergence — where traditional IT malware targets OT and supply-chain endpoints.  
- **Malware-as-a-Service (MaaS) & AI-Assisted Phishing** are accelerating infection rates across both high-value and mid-tier enterprises.  

INDIA CYBER THREAT REPORT 2026 40

## Windows Threat Landscape

INDIA CYBER THREAT REPORT 2026 41

The Windows malware ecosystem in 2025 continued to evolve — not through new malware families, but through the reinvention of old ones. Seqrite’s telemetry reveals that legacy malware such as `W32.Pioneer.CZ1`, `W32.Expiro.R3`, `Trojan.Agent`, and `LNK.Cmd.Exploit.F` remains dominant, accounting for the bulk of detections. These families have endured for years, but their latest variants exhibit increased automation, stealth, and persistence, making them harder to eradicate across enterprise networks and hybrid work setups.  

### Key Threat Insights
1. **Legacy Persistence, Modern Stealth**  
   Despite being over a decade old, file infectors such as Pioneer.CZ1 and Expiro.R3 continue to dominate detections, reflecting ongoing gaps in patch hygiene and endpoint segmentation. Modern variants incorporate obfuscation and anti-sandbox techniques, turning simple file infectors into resilient loaders capable of evading first-generation antivirus detection.  

2. **Shortcut and Autorun Exploits Re-emerge**  
   `LNK.Cmd.Exploit.F` and related trojans showed strong, recurring activity across multiple quarters. These infections thrive in hybrid work environments where USB drives and offline data transfers remain common. They underline a low-tech but highly effective intrusion tactic that continues to bypass network-layer defenses.  

INDIA CYBER THREAT REPORT 2026 42

3. **Cryptomining Quietly Expands**  
   `Nsis.Bitmin` and `Trojan.NSIS.Miner.SD` represented the stealthier monetization vector of 2025. Attackers now deploy miners that automatically adapt CPU usage to avoid detection. The combination of miner payloads and compromised enterprise compute resources suggests monetization-driven persistence campaigns running parallel to espionage or ransomware operations.  

4. **Modular Trojans Become the Norm**  
   Families like `Trojan.Agent`, `Trojan.Floxif.E5`, and `Trojan.KillAv.DR` demonstrate modular evolution—each designed to deploy, disable, or adapt. Once a system is compromised, these trojans establish persistence, disable protections, and act as conduits for ransomware or espionage modules, effectively turning endpoints into multi-purpose launchpads.  

5. **A Blended Threat Environment**  
   Across 2024–2025, the data reveals a convergence of traditional malware, cryptominers, and backdoor implants. Attackers increasingly reuse known codebases, wrapping them in modern evasion frameworks, resulting in familiar signatures but far more capable behaviour.  

### 2025 Takeaways
- Legacy malware remains dominant, proving that attackers prioritize reliability and reach over novelty.  
- Shortcut-based and autorun infections surged, underscoring the ongoing importance of USB security and removable drive control.  
- Cryptomining and stealth monetization replaced visible ransomware spikes, highlighting attackers’ preference for silent profit.  
- Trojans evolved into modular ecosystems, enabling persistent infiltration and multi-stage payload delivery.  
- The Windows threat landscape in India remains a mix of the old and the adaptive, demanding continuous visibility, behavioural analysis, and faster patch cycles to reduce reinfection risk.  

INDIA CYBER THREAT REPORT 2026 43

## Major Cyber Campaigns of 2025

### Operation Sindoor
**Anatomy of a Digital Siege**  
Uncovered by Seqrite Labs, Operation Sindoor exposed a coordinated campaign involving state-sponsored APT36 and SideCopy groups, working alongside hacktivist collectives. The operation blended cyber espionage, data theft, and digital disruption, representing a new phase of hybrid warfare targeting India’s critical sectors. Attackers used spear-phishing emails, spoofed government domains, and malware-laced lure files to infiltrate defense and government IT systems. The introduction of Ares RAT, a modular and evasive remote access tool, enabled persistent surveillance and data exfiltration. Simultaneously, hacktivist groups launched defacements, DDoS attacks, and data leaks, amplifying impact through Telegram channels under banners like `#OpIndia` and `#OperationSindoor`.  
- **Risk Level:** High  
- **Target Regions:** India  
- **Target Sectors:** Government, Defense, Intelligence, IT, Healthcare, Telecom, Education  

INDIA CYBER THREAT REPORT 2026 44

### XELERA Ransomware Campaign
**Fake Food Corporation of India Job Offers Targeting Tech Aspirants**  
Cybercriminals are once again exploiting the aspirations of India’s young tech professionals, this time using fake government job offers to deliver a sophisticated ransomware campaign. Attackers posed as the Food Corporation of India (FCI) and circulated deceptive job descriptions and application documents that secretly deployed XELERA ransomware.  

Victims received a malicious document titled `FCEI-job-notification.doc`, containing a PyInstaller-packed executable named `jobnotification2025.exe`. Upon execution, the malware connected to a Discord-based command-and-control (C2) server to steal data and receive commands, while simultaneously encrypting files and demanding ransom payments in Litecoin.  

Beyond encryption, XELERA disrupted infected systems by terminating Windows Explorer processes unless a decoy file was open, and it downloaded a destructive MBR-corrupting Trojan (`MEMZ.exe`) that rendered systems unbootable. It also changed wallpapers, deleted files, flooded desktops with ransom notes, altered window titles, and used Text-to-Speech synthesis to verbally demand ransom.

---

R THREAT REPORT 2026 45

Speech to broadcast ransom demands.
This campaign demonstrates how attackers now combine fake job offers, Python-based malware, and Discord-based
controls to evade detection and target vulnerable job seekers.
Seqrite Labs Detection: OLE.Ransom.49280.GC, Ransom.Variant.Xelera
High
India
Google Salesforce Breach
A Deep Dive into the Chain and Extent of the Compromise
In June 2025, Google’s internal Salesforce system was breached in a well-planned cyber-extortion campaign
conducted by groups UNC6040 and UNC6240, linked to the ShinyHunters collective. Attackers impersonated Google
IT staff in vishing attacks, tricking an employee into approving a malicious OAuth application.
The compromised access was then exploited using custom Python scripts mimicking Salesforce’s DataLoader API
to extract massive datasets including business contacts, emails, and phone numbers while masking their activity
through Mullvad VPN and TOR.
INDIA CYBER THREAT REPORT 2026 46

INDIA CYBER THREAT REPORT 2026 47

Subsequently, a related attack by UNC6395 exploited Salesloft Drift AI integrations, leveraging stolen OAuth tokens
and SOQL queries to read Salesforce objects like user accounts and cases. The attackers sought AWS keys,
Snowflake tokens, and sensitive credentials for lateral attacks or resale.
This campaign reveals the rising trend of OAuth abuse and voice-based social engineering.
Enterprises must enforce strict OAuth governance, monitor API activity, and strengthen zero-trust identity policies.
High
Education, IT, Financial Services
India
Unveiling Swan Vector APT
Targeting Taiwan and Japan with Varied DLL Implants
Swan Vector, a multi-stage APT campaign, targeted educational and mechanical engineering institutions across
Taiwan and Japan in May 2025. The threat employed malicious RAR/ZIP packages with .LNK shortcuts, fake resumes,
and payment-related lures.
The attack chain unfolded in four stages:
• LNK launches rundll32.exe to execute a malicious DLL (Pterois).
• Pterois resolves APIs via hashed lookups and abuses timer objects for stealth.
• A second DLL (Isurus) decrypts shellcode from configuration files using RC4 and executes it via syscall-based
in-memory loading.
• A Cobalt Strike beacon establishes long-term remote control.
• These sophisticated techniques — DLL sideloading, Google Drive abuse, export-table hashing — show meticulous
OPSEC and stealth.
Seqrite Labs Detection: Trojan.Pterois.S36007342, Trojan.49524.GC, Trojan.49518.GC
High
Education, Engineering
Taiwan, Japan
INDIA CYBER THREAT REPORT 2026 48

Goodbye HTA, Hello MSI
New TTPs and Clusters of an APT Driven by Multi-Platform Attacks
The SideCopy APT group, linked to Pakistan, has evolved its infection strategy — shifting from HTA-based to MSI
(Microsoft Installer)-based attacks since December 2024.
The group expanded its focus to include Railways, Oil & Gas, External Affairs, and Defense Ministries.
New infection chains used malicious MSI installers and .pdf.lnk shortcuts, employing DLL sideloading, reflective
loading, and open-source RATs like Xeno RAT, Spark RAT, and CurlBack.
One cluster targeted Linux systems with Go-based binaries, while others retained HTA-based delivery with encrypted
resources.
Attackers impersonated officials, cloned e-governance domains, and even compromised the National Hydrology
Project’s legitimate site to host payloads.
Seqrite Labs Detection: LNK.SideCopy.49245.Gen, HTA.SideCopy.49247.Gen
High
Defense, Railways, Oil & Gas, Education
India
INDIA CYBER THREAT REPORT 2026 49

Operation HollowQuill
Malware Delivered into Russian R&D Networks via Research Decoy PDFs
Operation HollowQuill targeted the Baltic State Technical University (BSTU) in Russia using malicious research
invitation PDFs. The infection chain began with a .NET-based dropper deploying a Golang shellcode loader into the
OneDrive process via APC injection, finally loading a Cobalt Strike beacon.
The dropper ensured persistence through Windows Startup shortcuts and evaded detection with anti-analysis
checks.
Domains like phpsymfony[.]com were used for C2 communication, disguised with legitimate user agents.
Analysts traced multiple payloads through Go build IDs, uncovering shared infrastructure with AsyncRAT campaigns
pointing to a persistent, well-funded actor targeting strategic research institutions.
Seqrite Labs Detection: Trojan.Ghanarava
Medium
R & D, Education
Russia
ANNUAL THREAT REPORT INDIA 2026 50

Weaxor
Rebranded Mallox Ransomware with a Unique Payload Delivery Method
Weaxor, a rebranded Mallox ransomware, specifically targets Microsoft SQL (MSSQL) servers. Attackers exploit weak
credentials to run hidden PowerShell commands via sqlps.exe, which downloads two heavily obfuscated payloads
encoded in Base64 and XOR.
The attack includes AMSI bypass, process injection, and Cobalt Strike beacon deployment. Once the beacon connects
to its C2 servers, the final ransomware payload encrypts files, appending the .rox extension and demanding ransom
through TOR links.
Seqrite Labs Detection: Weaxor.Ransomware.49258.GC
High
Technology, Financial Institutions
India, China
Unmasking GrassCall Campaign
The Hackers Behind Job Recruitment Cyber Scams
The GrassCall campaign exploited global job seekers by posing as recruiters for crypto and Web3 roles. Victims were
contacted on job boards, redirected to Telegram, and asked to download “video interview” software like VibeCall.exe,
which installed the Rhadamanthys stealer on Windows or AMOS Stealer on macOS.
The malware exfiltrated credentials, cryptocurrency wallets, and browser data. GrassCall exemplifies the social
engineering evolution blending fake corporate infrastructure, realistic UX design, and cross-platform trojans.
Seqrite Labs Detection: Trojan.GrassCallCiR, Trojan.Rhadamanth
High
Job Seekers
Global
ANNUAL THREAT REPORT INDIA 2026 51

SnakeKeylogger
A Multistage Info Stealer Malware Campaign
Seqrite identified a multi-stage SnakeKeylogger campaign spreading via .img attachments. Once opened, an
executable masquerading as a PDF downloaded obfuscated payloads from an Apache server, decrypted in-memory to
bypass AV detection.
The second-stage payload used InstallUtil.exe process hollowing, executing SnakeKeylogger to harvest credentials,
FTP logins, and Wi-Fi details. The malware’s in-memory decryption, delegate injection, and rotating payload directories
indicate Malware-as-a-Service distribution.
Seqrite Labs Detection: Downldr.Snakeloggr.S35164149
High
Windows Users
INDIA CYBER THREAT REPORT 2026 52

Exposed SMB
The Hidden Risk Behind ‘WantToCry’ Ransomware Attacks
The WantToCry ransomware exploits misconfigured SMB services, brute-forcing credentials to remotely encrypt drives
and NAS devices.
Files are appended with .want_to_cry, and ransom notes direct victims to Telegram and Tox channels.
Because encryption occurs remotely without leaving local traces, traditional AVs often fail to detect early stages. Or-
ganisations must harden SMB/FTP/RPC configurations, disable public access, and monitor for brute-force anomalies.
Seqrite Labs Detection: HEUR:Trojan.Win32.EncrSD
High
Global
New Steganographic Campaign
Distributing Multiple Malware
The StegoCampaign (SteganoAmor) resurfaced in 2025, distributing Remcos, AsyncRAT, VIPKeylogger, Xworm, and
AgentTesla.
Malspam emails delivered benign-looking .jpg files embedding final payloads through steganography, effectively by-
passing content filters.
Seqrite Labs Detection: Backdoor.Remcos, Trojan.LoaderCiR
High
Global
INDIA CYBER THREAT REPORT 2026 53

Demystifying PKT and Monero Cryptocurrency
Deployed on MSSQL Servers
Seqrite discovered PKT Classic and Monero mining operations hijacking SQL servers via certutil-based payload down-
loads. Attackers deployed PacketCrypt mining tools through Base64 PowerShell commands and Themida-packed
binaries.
The campaign illustrated creative abuse of server resources for covert crypto-mining and bandwidth theft.
Seqrite Labs Detection: Trojan.Alevaul
High
India
INDIA CYBER THREAT REPORT 2026 54

Threat Actors Targeting US Tax-Session
with Stealerium Infostealer
Phishing campaigns during the U.S. tax season distributed LNK-based payloads disguised as IRS forms. The attack in-
volved nested Base64 PowerShell commands downloading a PyInstaller executable that dropped Stealerium v1.0.35,
exfiltrating credentials and browser data.
Seqrite Labs Detection: Trojan.Win32.PH
Low
United States
Unveiling Silent Lynx APT
Targeting Entities Across Kyrgyzstan
The Silent Lynx APT targeted Kyrgyzstan’s National Bank and Ministry of Finance using RAR attachments with C++
loaders and Golang reverse shells. The campaigns used Telegram bots for C2, and Google Drive for payload delivery.
Attribution suggests overlap with YoroTrooper operations from Kazakhstan.
Seqrite Labs Detection: Trojan.SLynx
Medium
Kyrgyzstan
INDIA CYBER THREAT REPORT 2026 55

INDIA CYBER THREAT REPORT 2026 56

Unmasking the SVG Threat
How Hackers Use Vector Graphics for Phishing Attacks
Attackers weaponized SVG files to deliver phishing redirects using embedded JavaScript. When opened in browsers,
SVGs silently executed scripts that redirected users to fake Office 365 credential pages.
Seqrite Labs Detection: Xml.Trojan.49854.GC
Medium
BFSI, Healthcare, Telecom
India, EU, United States
False GPS Signals
Disrupt Aircraft Navigation in India
Multiple flights reported sudden GPS inconsistencies caused by spoofed GNSS signals during landing approaches.
Authorities are investigating unidentified external sources. Spoofing is far more dangerous than jamming
because it feeds credible but false navigation data, risking incorrect positioning, approach deviation, and reduced
situational awareness.
High
Aviation
India
INDIA CYBER THREAT REPORT 2026 57

Fake CAPTCHA Lures Victims
Lumma Stealer Abuses Clipboard and PowerShell
Attackers deployed fake Cloudflare CAPTCHA pages that tricked users into pasting malicious commands copied to
their clipboard.
The payload downloaded Lumma Stealer, which harvested clipboard contents, screenshots, and credentials while
using hash-based API resolution and anti-sandbox checks.
Seqrite Labs Detection: Trojan.LummaStealerCiR
High
Global
Plague
A Silent PAM-Based Backdoor Threatening Linux Authentication Layers
Plague is a stealthy Linux backdoor that embeds directly into the Pluggable Authentication Module (PAM) stack
to bypass login security and grant persistent attacker access. Unlike traditional Linux malware, it integrates within
trusted authentication routines, enabling invisible privilege escalation without relying on external binaries or network
callbacks. The backdoor uses static passwords, multi-layered obfuscation, and anti-sandbox logic to evade detection,
while sanitizing session traces and redirecting logs to /dev/null. Its advanced design allows it to survive system up-
dates, remain undetected in forensic scans, and persist long-term in enterprise and cloud environments.
Medium
Linux-based systems, Enterprise servers, Cloud infrastructure
Global
INDIA CYBER THREAT REPORT 2026 58

ZuRu Malware
Weaponizing macOS Developer Tools for Stealthy Persistence
The ZuRu malware resurfaced in 2025, targeting macOS users through a tampered version of the legitimate Termius
SSH client. The compromised app embeds malicious code in its helper process, allowing it to run silently while ap-
pearing legitimate. Once executed, it downloads a Khepri RAT variant as a second-stage payload, enabling full remote
control, file theft, and command execution. ZuRu maintains persistence via LaunchDaemon tasks, disguises network
communication as DNS traffic, and uses a custom signature to evade macOS security checks. Its abuse of trusted
developer tools underscores a growing threat to developer ecosystems and unmanaged macOS environments.
High
Apple and Mac OS
Global
XCSSET Malware
Targeting Apple Developers
XCSSET is a macOS-specific malware that infects Xcode development environments to spread malicious payloads.
By injecting code into project build phases, it ensures execution whenever a developer compiles code. The malware
steals browser data, credentials, and session tokens, and disables macOS security updates to maintain persistence.
Using modified tools like HackBrowserData and persistence via LaunchDaemons and Git repositories, XCSSET
remains hidden across shared developer projects. It poses significant risk to software supply chains, especially where
Xcode projects are reused or distributed among teams.
Medium
Apple and Mac OS
Global
Masslogger Fileless Variant
Spreads via .VBE, Hides in Registry
Seqrite Labs identified a fileless variant of Masslogger, a credential-stealing malware that operates entirely from
Windows Registry without writing files to disk. Delivered via phishing emails containing .VBE scripts, it loads
multiple encoded stages into memory using PowerShell SendKeys automation. The final payload injects into
legitimate processes like AddInProcess32.exe to steal browser credentials, email logins, clipboard data, and
screenshots. With geo-targeted variants and multi-channel exfiltration through FTP, SMTP, and Telegram, this variant
exemplifies modern fileless persistence and anti-forensic evasion.
Medium
Enterprise Windows Users
Global
INDIA CYBER THREAT REPORT 2026 59

Exploit Targeting SAP NetWeaver Development Server
Mass RCE Attacks (CVE-2025-31324)
A critical remote code execution (RCE) flaw in SAP NetWeaver Development Server is being weaponized globally.
Attackers exploit the insecure metadata uploader endpoint to upload malicious ZIP/JAR files, gaining persistent
access and deploying JSP web shells. Since mid-2025, groups like LAPSUS$ Hunters and ShinyHunters have
automated the exploit, leading to mass compromises across manufacturing, telecom, and retail sectors. In many
cases, attackers dropped the Auto-Color Linux backdoor, enabling lateral movement and data exfiltration from ERP
systems. Over 1,200 SAP servers are confirmed exposed, highlighting a widespread enterprise-level threat to
mission-critical infrastructure.
High
SAP ERP Environment
Global
INDIA CYBER THREAT REPORT 2026 60

Zero-Click AI Theft
“EchoLeak” Exploits Microsoft 365 Copilot for Data Exfiltration
The EchoLeak exploit (CVE-2025-32711) demonstrates how attackers can abuse AI assistants like Microsoft 365
Copilot to perform zero-click data theft. By embedding prompt injection payloads in emails, adversaries trigger Copilot
to autonomously send sensitive data — such as emails, documents, and tokens — to attacker-controlled servers. This
occurs without any user interaction, making detection nearly impossible. The exploit manipulates Copilot’s trusted
access to Outlook, OneDrive, and Teams, turning an AI assistant into an unintentional data exfiltration agent. EchoLeak
marks the first recorded zero-click attack on an enterprise AI platform, exposing a critical new vector in AI-driven
security ecosystems.
High
Enterprise Microsoft 365 Copilot Users
Global
Clickfix HijackLoader Campaign
Phishing-Fueled Malware-as-a-Service Expansion
The Clickfix HijackLoader campaign illustrates the evolution of loader-based attacks in the cybercrime ecosystem.
Distributed via malicious .msi installers on fake download sites and malvertising networks, it delivers HijackLoader, a
modular loader capable of injecting payloads like DeerStealer. Used in financially motivated campaigns, HijackLoader
is often part of Malware-as-a-Service ecosystems, where actors like TAG-150 and CastleLoader collaborate to deliver
credential stealers and remote access tools. Its multi-stage execution and integration with external loaders highlight
the growing commercialization and efficiency of malware delivery networks.
High
Financial Institutions
Europe, Middle East
INDIA CYBER THREAT REPORT 2026 61

Operation CargoTalon
UNG0901 Targets Russian Aerospace & Defense
Operation CargoTalon (UNG0901) is a spear-phishing campaign aimed at the Russian aerospace and defense sector,
using logistics-themed lures to deliver the EAGLET implant. The infection chain (Emai/ LNK/DLL/decoy XLS) relies
on LOLBIN execution to deploy the implant while presenting a benign document. EAGLET acts as a lightweight HTTP
C2 backdoor, capable of executing commands, downloading additional payloads, and exfiltrating files. Infrastructure
overlaps link the campaign loosely to previously known threat clusters, suggesting an ongoing espionage operation
targeting sensitive defense data.
Medium
Aerospace and Defense
Russia
WinRAR Vulnerabilities
Directory Traversal & NTFS ADS (CVE-2025-6218 & CVE-2025-8088)
Two severe flaws in WinRAR for Windows — CVE-2025-6218 and CVE-2025-8088 allow attackers to write malicious
files outside extraction directories, enabling RCE and stealthy persistence. Threat actors including RomCom and
Paper Werewolf (GOFFEE) have exploited these vulnerabilities in phishing campaigns. CVE-2025-6218 abuses
directory traversal, while CVE-2025-8088 hides payloads in NTFS Alternate Data Streams, making them invisible to
users. Exploitation enables auto-execution on login or side-loading by other processes, posing long-term risks to
enterprise networks and individual users alike.
Medium
Enterprise Windows Users
Global
INDIA CYBER THREAT REPORT 2026 62

INDIA CYBER THREAT REPORT 2026 63

INDIA CYBER THREAT REPORT 2026 64

INDIA CYBER THREAT REPORT 2026 65

/{ industry
cybersecurity
preparedness
survey };
KEY FINDINGS ACROSS CYBERSECURITY DOMAINS
Cyber Hygiene
Organisations continue strengthening their security culture, but gaps remain in foundational practices.
invest in cybersecurity culture through
52.5% 13.3% 74%
training and awareness
have higher maturity of the participating
in defining and organisations have yet
practicing cyber to implement cyber 65% have defined and implemented
hygiene practices security processes
hygiene practices
Securing Assets
Asset visibility and lifecycle management remain a mixed issue.
75.7% 80.1% maintain an updated 39.8% still operate End-of-Life
Configuration Management (EOL/EOS) systems
Database (CMDB )
have higher
maturity in asset
(hardware/
81.2% securely handle data 11.6% have no mechanism to
software/data, etc) during asset disposal secure assets
protection
INDIA CYBER THREAT REPORT 2026 66

Data Security
Organisations have strengthened their data protection measures but still face challenges in managing the sensitive
data lifecycle.
75.7% have data leakage controls
7.2% 74.6%
of the participants have their data
don’t have any classified
controls in
protecting data 64.1% have secure data wipe
processes
Malware Protection
The adoption of advanced malware defenses is high, although a small portion still relies on basic protection.
4.90%
rely only on basic protection
62% of the participants don’t have any
controls in protecting data
use advanced malware
86.7%
protection technologies
Access Control
Identity and access governance continues to mature steadily.
have defined workflows
79.6%
47.5% for access provisioning
and revocation
have a proper access control mechanism for
managing identity and ensuring only authorised
follow best practices for
access to the data 75.7%
credentials and password
policies
Secure Configuration
Configuration hardening remains one of the weakest domains.
6.6% have not implemented any poli- 47.5% enforce secure configurations
cies to protect their assets based on best practices
INDIA CYBER THREAT REPORT 2026 67

Software Updates & Patch Management
Patch discipline varies significantly across organisations.
64.1% have implemented a patch  1.7% focus only on critical &
management process essential updates
69.6% prioritize patches irrespective  7.2% have no defined patch
of severity management process
Backup & Recovery
Backup hygiene shows strong adoption, but a small number remain unprepared.
| 78.5% |     | 2.8% | 83.4% | 80.7% |
| ----- | --- | ---- | ----- | ----- |
have defined and  securely handle  restrict unauthorised  store backups offline
| implemented a   |     | data during asset  | access to backups |     |
| --------------- | --- | ------------------ | ----------------- | --- |
| backup strategy |     | disposal           |                   |     |
| Incident        |     | Security Process   |                   |     |
| Response        |     | Management         |                   |     |
IR maturity reveals Process effectiveness is inconsistent across organisations.
significant gaps in
readiness and execution.
|     |     |     | 67.4% | 39.2% |
| --- | --- | --- | ----- | ----- |
72.4%
|     |     |     | test processes  | never revisited  |
| --- | --- | --- | --------------- | ---------------- |
have a defined
|     |     |     | regularly | processes after  |
| --- | --- | --- | --------- | ---------------- |
11%
| incident response  |     |     |     | introduction |
| ------------------ | --- | --- | --- | ------------ |
process to detect &
respond to threats
don’t test
their
| 27.6%     | 79.6%      |           |       |                |
| --------- | ---------- | --------- | ----- | -------------- |
|           |            | security  | 36.5% | 34.8%          |
| lack an   | have       |           |       |                |
| incident  | employee   | processes |       |                |
| manage-   | awareness  |           |       | have partially |
have defined
| ment | on IR |     |     | defined and |
| ---- | ----- | --- | --- | ----------- |
processes
| process |     |     |     | untested processes |
| ------- | --- | --- | --- | ------------------ |
but never tested
INDIA CYBER THREAT REPORT 2026 68

Threat Exposure & Attack Patterns
A significant proportion of organisations reported facing attacks; social engineering remains the top attack vector.
| 56.9%                | 16.6%           | 8.8%                    |     | 1.1%                |
| -------------------- | --------------- | ----------------------- | --- | ------------------- |
| of participated      | reported        | reported facing         |     | experienced         |
| organisations were   |                 |                         |     | cyber-attacks very  |
|                      | experiencing a  | multiple cyberattacks,  |     |                     |
| unsure whether they  |                 |                         |     | often               |
|                      | cyberattack at  | occurring weekly or     |     |                     |
had experienced a
|     | some point in the  | monthly |     |     |
| --- | ------------------ | ------- | --- | --- |
cyberattack
past 12 months
| Most observed threat types |     | Cyber Resiliency |     |     |
| -------------------------- | --- | ---------------- | --- | --- |
Organisations demonstrate varying levels of resilience in
•  Social engineering
the aftermath of an attack.
(phishing/vishing/
smishing) – highest
|     |     | 50.8% |     | 9.4% |
| --- | --- | ----- | --- | ---- |
•  Malware attacks
|     |     | reported no     |     | faced business  |
| --- | --- | --------------- | --- | --------------- |
|     |     | impact despite  |     | disruption      |
being targeted
•  Web application
attacks
| •  10% attributed to |     | 7.7% |     | 5.5% |
| -------------------- | --- | ---- | --- | ---- |
ransomware
|     |     | suffered  |     | faced          |
| --- | --- | --------- | --- | -------------- |
|     |     | data loss |     | financial loss |
•  ~6% linked to AI/ML-
based attacks
| •  ~5% supply chain |     | 3.8% | suffered regulatory |     |
| ------------------- | --- | ---- | ------------------- | --- |
implications
attacks
•  Spoofing attacks
remain concerning
INDIA CYBER THREAT REPORT 2026 69

Top 5 Challenges in Cybersecurity Adoption (2026)
| Lack of    | Lack of    | Budget      | Lack of     | Low priority  |
| ---------- | ---------- | ----------- | ----------- | ------------- |
| knowledge/ | manpower/  | constraints | senior      | within the    |
| experience | skilled    |             | management  | organisation  |
|            | resources  |             | support     |               |
Threat Intelligence Adoption
41.4%
of participated organisations consume threat intelligence (OSINT, commercial, or
both) to support proactive cyber defense.
Attack Surface Monitoring
33.7%
 of participated organisations continuously monitor their attack surface and take
timely remedial actions.
Top Priorities for Cyber Security Investment
| Threat    | Endpoint | Data       | Cloud    | Employee |
| --------- | -------- | ---------- | -------- | -------- |
| 1.        | 2.       | 3.         | 4.       | 5.       |
| Detection | Security | Protection | Security | Training |
& Response
Adoption of AI for Cyber Threat Defense
INDIA CYBER THREAT REPORT 2026 70

Cybersecurity Maturity Radar Map
The Cybersecurity Maturity Radar Map offers a comprehensive snapshot of the current state of cybersecurity
readiness. By evaluating critical areas such as incident response, malware protection, data security, and access
control, the map effectively highlights both strengths and areas for improvement within the cybersecurity
framework. Each axis on the radar corresponds to a specific category, with scores ranging from 0 to 10, providing a
clear measure of maturity levels in those areas. Here’s a detailed breakdown
People: Assesses staff awareness and training to address cybersecurity risks.
Process: Evaluates the strength and efficiency of cybersecurity management processes.
Technology: Measures the use of advanced tools to protect systems and data.
Data Security: Reviews mechanisms for safeguarding sensitive data against unauthorized access and breaches.
Malware Protection: Examines the ability to prevent, detect, and respond to malware threats.
Access Control: Evaluates the effectiveness of restricting access to systems and information.
Secure Configuration: Focuses on applying secure settings to reduce vulnerabilities.
Software Updates & Patches: Tracks efficiency in addressing known vulnerabilities through updates.
Backup & Restore: Assesses the reliability of backups and data recovery capabilities.
Incident Response: Measures readiness and effectiveness in managing security incidents.
For the analysed sample size, the maturity score stands at 6.3/10, indicating a moderate level of maturity with room
for improvement.
INDIA CYBER THREAT REPORT 2026 71

INDIA CYBER THREAT REPORT 2026 72

EVALUATION PARAMETERS
Cyber Securing Data Malware
Hygiene Assets Security Protection
evaluates how well assesses the organisation’s evaluates the protection of examines the deployment
organisations build a ability to identify, track, and sensitive and business- of advanced anti-malware
security-first culture protect all hardware and critical information through tools, scanning practices,
through employee software assets through ac- data classification, leakage firewall usage, and restric-
awareness, responsible curate inventories, updated controls, encryption, and tions on unauthorised
behaviour, and regular CMDBs, secure disposal, secure data wipe or unsafe software. This
training. The goal is to and removal of EOL/EOS processes. The goal is to helps assess how prepared
understand how effectively systems. The purpose is determine how effectively organisations are to defend
employees function as the to measure asset visibility organisations preserve against malware,
first line of defense and and assess how effectively confidentiality, integrity, and ransomware, and modern
how consistently security organisations mitigate ex- availability while preventing attack vectors.
practices are followed posure and safeguard their unauthorised access or
across daily operations. infrastructure. leakage.
Access Secure Software Updates Backup &
Control Configuration & Patch Recovery
reviews how organisations focuses on system hardening Management assess the implementation of
manage identities, privileges, practices, removal of default reliable, protected, and offline
evaluate the consistency and
and authentication through or weak settings, disabling backup strategies covering
completeness of deploying
role-based access, unused features, and critical systems and cloud en-
patches and updates across
provisioning workflows, strong adherence to industry vironments. The purpose is to
environments, including
password practices, and baselines such as CIS understand the organisation’s
prioritization and structured
restricted admin usage. The standards. The goal is to capability to restore opera-
processes. This aims to mea-
aim is to evaluate the strength understand how effectively tions quickly and maintain
sure how well organisations
of controls that prevent organisations minimize continuity during disruptions
mitigate known vulnerabilities
unauthorised access to misconfigurations — a leading or cyber incidents.
before they are exploited.
systems and data. cause of security incidents.
Incident Response Security Process Management
assesses the presence of defined processes, employee reviews how regularly organisations test, update, and
awareness, and readiness to detect, respond to, and validate their cybersecurity processes. The objective is
recover from an incident. The goal is to determine how to assess whether organisations continuously strength-
effectively organisations can limit the impact and restore en their security posture and adapt to evolving threats
normal operations during cyberattacks. through ongoing governance and improvement.
INDIA CYBER THREAT REPORT 2026 73

/{ threat
forecast
2026
the age of cognitive
intrusions };
INDIA CYBER THREAT REPORT 2026 74

Seqrite’s 2025 threat forecasts achieved a 70% validation rate, accurately anticipating the surge in AI-powered attacks,
hybrid warfare operations (Operation Sindoor), and the evolution of ransomware into data-extortion ecosystems.
The global threat surface expanded faster than defenses driven by AI adoption, geopolitical friction, and systemic
dependency on digital ecosystems.
INDIA CYBER THREAT REPORT 2026 75

KEY PREDICTIONS
• Poisoning the Well: Direct Attacks on AI Systems
As critical sectors increasingly adopt AI for decision-making—medical imaging, credit scoring, industrial control,
fraud detection—attackers will target AI lifecycles directly. By inserting biased, mislabeled, or strategically crafted
samples into training data, adversaries can distort model behaviour, implant logic-based backdoors, or trigger
dangerous misclassifications at runtime.
These compromises can persist for months due to the opaque nature of AI pipelines. Organisations will need
integrity checks, adversarial testing frameworks, and secure training environments to maintain trust in AI systems.
• AI-Powered Deception: Hyper-Personalized Social Engineering
AI will make social engineering almost indistinguishable from legitimate interaction. Attackers will construct
“digital twins” of victims’ contacts mimicking writing styles, speech patterns, and even video presence. This
mirrors early-stage impersonation patterns seen in campaigns like GrassCall, where staged conversations were
used to deliver malware.
In 2026, these techniques will merge with AI-enhanced mobile banking malware capable of auto-filling credentials,
bypassing biometrics, and executing fraud autonomously. Enterprises must adopt phishing-resistant MFA and
continuous user authentication to counter the precision of AI-driven deception.
• The Rise of Cognitive APTs: AI-Enhanced Strategic Deception
State-backed APT groups and organized cybercriminal syndicates will integrate AI into reconnaissance,
vulnerability discovery, lateral movement, and real-time payload adaptation. Operations resembling Operation
Sindoor, which combined espionage, psychological operations, and false attribution signals, foreshadow how AI
will amplify misdirection and obfuscation.
AI-enabled APTs will autonomously refine their TTPs, mutate malware, and spoof the behavioural patterns of rival
groups, further complicating attribution and response.
• Zero-Days at Machine Speed: Exploit and Supply Chain Attacks
Exploit development cycles will compress dramatically due to AI-assisted vulnerability research. Attacks on
high-value systems like SAP NetWeaver (CVE-2025-31324), Oracle EBS, and archive parsing vulnerabilities (e.g.,
7-Zip CVEs) already demonstrate how quickly adversaries exploit weaknesses.
In 2026, supply chain compromise—CI/CD pipelines, SDKs, container registries, and cloud integrations—will
remain the most efficient pathway to large-scale infiltration. Organisations must adopt automated patch
orchestration, software bill of materials (SBOM) visibility, and hardened build systems.
• The Hidden Canvas: SVG File Abuse
SVG files—frequently treated as harmless assets—will emerge as powerful malware carriers. Recent cases
involving Xml.Trojan-embedded SVG payloads preview how attackers embed JavaScript or redirection logic inside
vector graphics.
INDIA CYBER THREAT REPORT 2026 76

With creative teams, marketing workflows, and AI design tools increasingly exchanging SVG files, attackers will
use them to infiltrate automated pipelines and collaboration systems, bypassing traditional filters and sandboxing.
• AI-Led Ransomware: Autonomous RAT Deployment
Ransomware operators will deploy AI-based orchestration engines capable of autonomously mapping network
topologies, selecting RAT payloads, evolving anti-analysis behaviour, and performing adaptive privilege escalation.
Early versions of automated delivery chains—such as the Weaxor ransomware SQL-based RAT deployment—hint
at what fully autonomous ransomware operations may look like in 2026.
These attacks will mimic legitimate processes, rotate execution behaviour, and reduce detection windows to
minutes.
• Ransomware 2.0: Multi-Stage, Stealth-Oriented Campaigns
Ransomware attacks will increasingly unfold as multi-phase operations rather than single-event encryptions.
Campaigns like Xelera and Weaxor, which combined reconnaissance, data theft, C2 beaconing, and eventual
encryption, reflect this shift.
In 2026, ransomware will operate with extended dwell time, using memory injection, sandbox evasion, and
multi-stage loaders to remain invisible until final impact. Data theft, financial fraud, lateral movement, and
crypto-mining will often precede encryption.
• Ghosted Defenses: EDR Freeze & Kernel-Level Suspension
Attackers will target endpoint security directly using thread suspension, dump manipulation (e.g., WerFault,
MiniDump), and vulnerable driver exploitation. While this tactic did not appear widely in the 2025 dataset, it aligns
with increased abuse of kernel-level components for stealth persistence.
In 2026, these attacks will allow malware to operate on “healthy-looking” systems where EDR is running but
silently neutralized. Continuous telemetry validation and strict driver policies will be essential
• Living Off WMI: Fileless Persistence and Remote Control
Fileless attacks will continue to rise, with adversaries increasingly weaponizing WMI for persistence, stealthy
command execution, and lateral movement. Campaigns similar to the Masslogger fileless variant, which used
registry-only payloads and PowerShell execution, show how attackers avoid leaving artifacts.
In 2026, permanent WMI event subscriptions and remote WMI RPC calls will become high-signal indicators of
compromise, requiring SOCs to baseline and monitor WMI behaviour.
• Adaptive Mobile Threats: Bypassing Google’s App Rules
Google’s enforcement of verified-developer requirements for all sideloaded apps will reshape Android malware
delivery. Threat actors will increasingly purchase or compromise verified developer identities to push malicious
apps through trusted channels.
The fake NextGen mParivahan malware campaign demonstrates how attackers already mimic trusted services.
As verification tightens, adversaries will pivot to Progressive Web Apps (PWAs), malicious ads, and outdated
devices outside enforcement coverage.
INDIA CYBER THREAT REPORT 2026 77

• NFC Exploitation: The Next Wave of Contactless Fraud
With global expansion of tap-and-pay services, NFC-based attacks will scale. Attackers will exploit compromised
Android devices as relay nodes, intercepting HCE tokens and manipulating transactions in real time.
Although the 2025 dataset did not observe direct NFC fraud, the pattern of credential-stealing mobile malware
suggests a high potential for evolution in 2026.
• Hybrid Hacktivism: Statecraft in the Digital Age
Hacktivism is evolving into a geopolitical instrument, blending cyberattacks with disinformation campaigns.
Groups linked to operations like Operation Sindoor and emerging hacktivist clusters show how “volunteer” groups
engage in state-aligned narratives while maintaining plausible deniability.
In 2026, expect coordinated DDoS attacks, data leaks, deepfake propaganda, and symbolic disruptions of critical
infrastructure tied to political timelines.
• The Fragmented Underground: Cybercrime Without Borders
The cybercrime ecosystem will fracture into small, decentralized cells as large ransomware groups face
shutdowns. Campaigns spreading across variant families—KillSec, FunkSec, Lynx, StegoCampaign loaders, and
HijackLoader (ClickFix)—already signal distributed specialization.
Access brokers, exploit developers, and data extortion operators will collaborate in modular, service-based
structures, making takedowns harder and reconstitution faster.
• Dual-Use Exploitation: Weaponizing Legitimate Tools
Ransomware actors will increasingly rely on living-off-the-land binaries, signed drivers, and low-level utilities to
neutralize EDR. Examples like Weaxor’s use of sqlps.exe, Masslogger’s InstallUtil.exe abuse, and WantToCry’s
SMB-based lateral movement reflect this pattern.
In 2026, AI will assist attackers in selecting the least-detectable pathways, including kernel rootkits, cloud admin
APIs, and syscalls that bypass user-mode monitoring.
• Identity as the New Battlefield: Credential Abuse at Scale
Identity will remain the most valuable target. Credential-stealing campaigns—such as Stealerium, SnakeKeylogger,
and OAuth abuse during the Google Salesforce breach—show how attackers bypass perimeter defenses entirely
by impersonating legitimate users.
With widespread adoption of SSO, federated identity models, and cloud-native access, a single compromised
identity could unlock entire enterprise environments. Identity threat detection, privileged access controls, and
continuous authentication will define future defense strategies.
INDIA CYBER THREAT REPORT 2026 78

/{ recommendations &
beyond
2026
from reactive defense to
cognitive resilience };
1. Prioritize Predictive Intelligence
By 2026, attacks will no longer depend solely on exploits but on deception and adaptive behaviour. rganizations must
integrate AI-driven threat prediction, anomaly detection, and telemetry correlation to anticipate attacks before impact.
Invest in cross-layer visibility — endpoints, cloud, identity, and network — to identify behavioural deviations in real time.
2. Accelerate Patch Orchestration
Vulnerability-to-exploit time has compressed from weeks to days. Automated patch orchestration, vulnerability
prioritization, and virtual patching through EDR/XDR must become standard across hybrid infrastructures.
3. Reinforce Identity as the New Perimeter
Identity will remain the primary attack vector. Adopt Zero Trust principles, enforce strong MFA, and continuously moni-
tor for credential replay, token abuse, and privilege escalation.
4. Harden the AI Layer
AI models, copilots, and data pipelines are emerging as new breach surfaces. Implement AI security governance, mod-
el integrity validation, and adversarial data testing to prevent prompt injection and model poisoning attacks.
5. Advance to Autonomous Detection and Response
Move from manual SOC triage to autonomous security operations powered by GenAI and context-aware correlation.
Integrating tools like Seqrite’s Intelligent Assistant (SIA) can enhance decision support, triage efficiency, and analyst
productivity.
INDIA CYBER THREAT REPORT 2026 79

6. Build Cyber Resilience Frameworks
Accept that compromise is inevitable; containment and continuity define maturity.
Develop cyber crisis playbooks, simulate breach drills, and measure Mean Time to Remediate (MTTR) as a
board-level KPI.
7. Strengthen Ecosystem Collaboration
Cybercrime today is borderless. Enterprises must collaborate across industry ISACs, government CERTs, and global
intelligence exchanges to share IoCs, TTPs, and defense playbooks in near real time.
8. Secure the Human Element
Despite AI’s dominance, social engineering remains the attacker’s most effective weapon. Embed continuous cyber
awareness, phishing simulations, and behaviour-driven access policies to reduce human error.
9. Defend Against the New Frontier – Cognitive Threats
2026 will usher in AI-augmented adversaries capable of autonomous reconnaissance and deception.
Defenders must match this evolution with AI-augmented defense, ensuring every layer — from SOC to endpoint — can
detect and respond dynamically.
The next frontier of cybersecurity will not be defined by who has more tools, but who adapts faster.
As threat actors evolve into cognitive adversaries, capable of mimicking users and weaponizing AI platforms, India’s
cybersecurity strategy must focus on resilience, adaptability, and intelligence.
The coming year will test the readiness of enterprises to embrace autonomous protection, predictive defense, and
human-machine collaboration in real time. Only those who see cyber defense not as a cost, but as a strategic differen-
tiator, will thrive in the digital future.
INDIA CYBER THREAT REPORT 2026 80

/{ expert
quotes };
INDIA CYBER THREAT REPORT 2026 81

“The future of security lies beyond the device, our new mission is safeguarding the lifeblood of the digital
enterprise: data. As India accelerates into an AI-driven, cloud-native economy, the old guard of endpoint-centric
controls must yield to a dynamic, data-centric security vision. Leadership is not just about protecting resources,
but about shaping a culture where data protection is woven into every decision, partnership, and innovation.
Building digital trust for tomorrow demands an unwavering commitment to resilient, intelligent, and ethical data
stewardship. This is the paradigm shift that will secure India’s digital ambitions for generations to come.”
PRAVEEN KUMAR
CISO, Nykaa
“In BFSI sector, the threat landscape is unforgiving. Cybercriminals know that trust is our most valuable currency, and
they target it relentlessly. Over the last year, we have seen sophisticated fraud schemes, account takeovers, and ran-
somware campaigns aimed directly at disrupting financial stability. For us, cybersecurity is no longer a back-office
function, it is core to customer confidence and regulatory compliance. The future will belong to institutions that can
combine real-time fraud detection with proactive intelligence, ensuring security and trust go hand in hand.”
C. SHERMUGADURAI
CISO, Tamil Nadu Mercantile Bank (TMB)
“The insights from the India Cyber Threat Report 2026 mirror the realities we face in engineering, construc-
tion & manufacturing. As IT and OT environments merge, even small security gaps can trigger large-scale
operational disruptions. Our priority today is ensuring visibility across industrial networks, tightening access
controls, and predicting anomalies before they halt production & operations. Cybersecurity has become a
key enabler for business because in engineering & construction industry, every minute of uptime counts &
reliability of platforms is of paramount importance”
UDAY DESHPANDE
CISO, Larsen & Toubro
“As enterprises embrace cloud, mobility, and connected devices, the attack surface is expanding faster than security
teams can cover it. Our traditional models built for fixed perimeters no longer apply. Security must move closer to
identity, data, and behaviour wherever they reside. The concept of a ‘secure boundary’ has become entirely digital. This
shift has also transformed how attacks are launched — with adversaries now using AI to scale, automate, and adapt.
Defending against AI-driven threats requires AI-driven defense: security built to match the speed and intelligence of
the attackers themselves.”
ASHISH ADHVARYU
VP & Delivery Head - Cyber Security Practice, Infosys
INDIA CYBER THREAT REPORT 2026 82

“In BFSI sector, the threat landscape is unforgiving. Cybercriminals know that trust is our most valuable
currency, and they target it relentlessly. Over the last year, we have seen sophisticated fraud schemes,
account takeovers, and ransomware campaigns aimed directly at disrupting financial stability. For us,
cybersecurity is no longer a back-office function, it is core to customer confidence and regulatory
compliance. The future of secure banking will belong to institutions that blend real-time fraud detection with
proactive intelligence, where security, resilience, and trust go hand in hand.”
RADHAKRISHNAN S.
CISO, Indian Overseas Bank, Chennai
“Cyber threats are no longer episodic—they are a continuous reality. Cybercriminals, empowered by AI and automation,
now launch attacks in hours instead of months, making them faster, stealthier, and more persistent.
Traditional defenses alone won’t suffice. Organisations must embrace adaptive security—where detection, response,
and resilience are embedded into core operations and recognize that employees are the first line of defense. Building
a strong human firewall through awareness and training is as critical as deploying advanced technologies. This shift
from static protection to dynamic resilience will define who thrives in the digital era.”
DILEEP KUMAR MUKUNDAN
CISO, IFTAS
“Threat intelligence has evolved rapidly, moving beyond static threat lists to AI systems that can analyze data
across sectors and predict attacks before they happen. This shift is especially critical for education, where
schools, universities, and learning platforms hold sensitive student data, research records, and personal
information. If India strengthens national-level intelligence sharing and combines it with adaptive, locally
responsive defense across public systems, private enterprises, and educational institutions, we can protect
millions of learners and build one of the most secure digital ecosystems in the world, but only if we act
now before threats outpace our defenses.”
GOUTHAM NANJUNDASWAMY
CTO, Ethnus
INDIA CYBER THREAT REPORT 2026 83

Acknowledgement
AUTHORS
Shayak Tarafdar, Sr. Manager - Engineering
Priyabrata Dash, Manager - Engineering
Jyoti Karlekar, Senior Content Writer
CONTRIBUTORS
Sangmesh S, Vice President & Head of Seqrite Labs
Jaswinder Singh, Director, Engineering
SURVEY DESIGNER AND SCORE CARD CREATOR
Bhupendra Shirsath, Lead, Performance Marketing
Bandu Sudnye, Manager, Web Development
EDITORS
Deepti Uppal, Director, Marketing Communications
Om Puran, Director - Marketing
DESIGN
Siddharth Sarathi, Design Manager
Kinkar De Sarkar, Senior Executive - Design

Seqrite is a leading enterprise cybersecurity solutions provider. With a focus on simplifying cybersecurity, Seqrite delivers
comprehensive solutions and services through our patented, AI/ML-powered tech stack to protect businesses against the latest threats
by securing devices, applications, networks, cloud, data, and identity. Seqrite is the Enterprise arm of the global cybersecurity brand,
Quick Heal Technologies Limited, the only listed cybersecurity products and solutions company in India.
We are the first and only Indian company to have solidified India’s position on the global map by collaborating with the Govt. of the USA
on its NIST NCCoE’s Data Classification project. We are differentiated by our easy-to-deploy, seamless-to-integrate comprehensive
solutions providing the highest level of protection against emerging and sophisticated threats powered by state-of-the-art threat
intelligence and playbooks backed by world-class service provided by best-in-class security experts at India’s largest malware analysis
lab – Seqrite Labs. We are the only Indian full-stack company aligned with CSMA architecture recommendations, offering award-
winning Endpoint Protection, Enterprise Mobile Device Management, Data Privacy, Zero Trust Network Access, and many more.
Seqrite Data Privacy Management solution enables organisations to stay fully compliant with the DPDP Act and global regulations.
Seqrite also offers the Seqrite Malware Analysis Platform (SMAP) for deep, multi-layered malware analysis, along with Seqrite Threat
Intel, a real-time cyber defense hub delivering enriched, actionable threat intelligence.
We have recently launched Digital Risk Protection Services for external threat monitoring and Ransomware Recovery as a Service for
rapid, guided restoration after ransomware attacks. Seqrite has also unveiled SIA, an LLM-powered security co-pilot built on GoDeep.AI
to help enterprises navigate growing cyber complexity with intelligent, conversational analysis.
Today, 30,000+ enterprises in more than 70 countries trust Seqrite with their cybersecurity needs. For more information, please visit:
https://www.seqrite.com

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-08-14", "model": "gemini-3.5-flash-lite"} -->
