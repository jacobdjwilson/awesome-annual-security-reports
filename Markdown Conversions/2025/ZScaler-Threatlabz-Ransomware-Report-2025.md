# Zscaler ThreatLabz 2025 Ransomware Report

©2025 Zscaler, Inc. All rights reserved.

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [Ransomware Landscape: Top Trends and Targets](#ransomware-landscape-top-trends-and-targets)
- [Ransomware Roundup: What’s Making Headlines](#ransomware-roundup-whats-making-headlines)
- [Top 5 Ransomware Families to Watch in 2025-2026](#top-5-ransomware-families-to-watch-in-2025-2026)
- [ThreatLabz Ransomware Notes Archive](#threatlabz-ransomware-notes-archive)
- [2026 Predictions](#2026-predictions)
- [How Zscaler Stops Ransomware with Zero Trust + AI](#how-zscaler-stops-ransomware-with-zero-trust--ai)
- [Ransomware Prevention Checklist](#ransomware-prevention-checklist)
- [Research Methodology](#research-methodology)
- [About ThreatLabz](#about-threatlabz)
- [About Zscaler](#about-zscaler)

---

## Executive Summary

Ransomware has long been a constant in the threat landscape—but how it operates is constantly changing. Today’s campaigns are more targeted, automated, and efficient, driven in part by the growing use of generative AI enhancing and accelerating everything from phishing lures to malware development. This evolution has translated into a significant surge in ransomware activity and impact.

Even amid high-profile takedown initiatives like Operation Endgame, ransomware groups show no signs of slowing down. If anything, disruption may be driving reinvention. Thirty-four new ransomware families emerged during the analysis period for this report. Meanwhile, established groups such as DragonForce, Akira, and Clop climbed to the top of the activity charts, demonstrating the resilience of mature ransomware operations.

From April 2024 to April 2025, the Zscaler cloud blocked more ransomware attempts than in any previous year—more than 10.8 million hits—marking a 145.9% year-over-year increase and the highest volume recorded since tracking began. At the same time, the number of organizations listed on ransomware leak sites rose 70.1%, underscoring a broader shift to extortion-driven attacks. Today’s campaigns are high-frequency and high-impact, designed to extract maximum leverage, often without the need for encryption. A growing number of ransomware operators are abandoning encryption altogether in favor of pure data extortion—an evolution mirrored by a 92.7% rise in data exfiltration volumes over the past year.

The Zscaler ThreatLabz 2025 Ransomware Report dives deeper into these developments and findings, covering top targeted sectors and regions, ransomware families to watch, evolving attack methodologies, and actionable guidance for defenders. Beyond threat tracking, learn how ThreatLabz plays an active role in protecting enterprises worldwide—from building custom tools for ransomware attack recovery to contributing to global efforts that expose and disrupt large-scale malware and ransomware ecosystems.

---

## Key Findings

- Ransomware attempts blocked by the Zscaler cloud increased by 145.9% year-over-year (April 2024–April 2025), marking the most significant spike we’ve seen in three years.
- Data exfiltration volumes for 10 major ransomware families increased 92.7% year-over-year to 238.5 terabytes (TB) stolen, signaling the broader shift toward data theft as a primary extortion tactic.
- Public extortion cases jumped by 70.1% based on data leak site analysis, proving the threat of reputational damage or regulatory consequences is often more compelling than encryption alone.
- Manufacturing, Technology, and Healthcare were the top targeted industries, and the Oil & Gas sector experienced a 935.3% increase in attacks.
- The United States remains the #1 global target, experiencing 50.8% of overall attacks, followed by Canada, the United Kingdom, Germany, and India.
- Generative AI is becoming a force multiplier for ransomware threat actors, helping to rapidly create phishing lures, write malicious code, automate data extraction, and more.
- RansomHub (833), Akira (520), and Clop (488) emerged as the most active ransomware families, collectively responsible for the largest share of attacks.
- Vishing (voice-based phishing) is increasingly integrated into ransomware attacks as voice scams become more convincing and more effective at gaining initial access.
- ThreatLabz identified 34 newly active ransomware families during the analysis period, bringing the total number tracked to 425 since our research began.
- Despite rising ransomware activity, coordinated law enforcement efforts—supported by industry experts like Zscaler ThreatLabz—have made meaningful strides in disrupting major ransomware infrastructure, as demonstrated by Operation Endgame.

---

## Ransomware Landscape: Top Trends and Targets

While headline-making breaches illustrate the global scale of ransomware, the most valuable insights come from analyzing targeting patterns and operational behaviors threat actors use across campaigns.

### Ransomware attacks hit new highs

Steady growth in ransomware activity is no longer surprising, but the latest data shows a dramatic surge in attack volume: attempted ransomware attacks in the Zscaler cloud have jumped 145.9% year-over-year—and sixfold since 2021.

![Figure 1: Ransomware attack indicators (events) blocked by Zscaler annually]

### Data exfiltration trends up 92.7%

Over the last year, ransomware groups have turned data theft from a supporting act into the main event. ThreatLabz analysis reveals that the total volume of data stolen increased year-over-year across 10 major ransomware groups.

![Figure 2: Data exfiltration by key ransomware groups]

### Shifting to data extortion only

The Zscaler ThreatLabz 2024 Ransomware Report examined how the Hive ransomware group rebranded as Hunters International in October 2023. Since the emergence of Hunters International, the group has been very active and heavily focused on data theft over encryption.

![Figure 3: GB of data stolen per month by Hunters International]
![Figure 4: World Leaks ransomware group website]
![Figure 5: Hunters International shutdown notice]

### Industries facing the most attacks

Manufacturing, Technology, and Healthcare remained the most frequently targeted sectors.

![Figure 6: Ransomware attacks by industry based on data leak sites (top 20 industries)]

### Year-over-year trends

Ransomware attacks on the Oil & Gas sector have spiked more than 900% year-over-year. The Agriculture sector also saw ransomware attacks skyrocket by 677.4%.

![Figure 7: Year-over-year percentage change in ransomware extortion attacks by industry]

### Global and regional hotspots

Leak site data reveals a clear geographic concentration, with a dominant share of attacks targeting organizations in the United States (50.8%).

![Figure 8: Top 15 countries based on share of ransomware attacks]

### Most active ransomware groups in 2024–2025

![Figure 12: Ransomware attacks reported on data leak websites]

### New ransomware groups on the scene

![Figure 13: New ransomware groups with data leak sites]

### Major vulnerabilities exploited in ransomware campaigns

Ransomware groups are increasingly leveraging vulnerabilities in critical enterprise technologies, including:
- **Virtualization Software**: Hypervisors such as VMware ESXi.
- **VPNs**: Exploiting devices like FortiProxy and SonicWall.
- **Remote Access Tools**: Exploiting RMM tools like SimpleHelp.
- **Backup Solutions**: Exploiting vulnerabilities like CVE-2023-27532 (Veeam).
- **File Transfer Applications**: Primary target for the Clop group.

---

## Ransomware Roundup: What’s Making Headlines

### Black Basta Leverages ChatGPT for Criminal Activities
Leaked internal chat logs reveal that Black Basta members use ChatGPT for code rewriting, problem-solving, and exploring uncensored AI models like WormGPT.

### Hello? It’s Ransomware Calling: Inside the Multi-Stage Attack Playbook
Threat actors are increasingly using "vishing" (voice phishing) to impersonate IT staff, tricking victims into granting remote access via RMM tools.

![Figure 14: Multi-stage ransomware attack methodology]
![Figure 15: A ransomware initial access broker’s fake “Filters update” website]

### Leaky LockBit: RaaS Mechanisms Exposed in Dark Web Breach
A leaked MySQL database from LockBit provided researchers with a detailed view of the group's internal operations, including affiliate trust levels and ransom payment data.

![Figure 18: Defaced LockBit admin panel]

### Healthcare Under Siege: The Era of Massive Data Theft
Healthcare institutions are increasingly targeted due to the high value of Protected Health Information (PHI).

---

## Top 5 Ransomware Families to Watch in 2025-2026

1. **Dark Angels**: Known for high-value, targeted attacks and a record-breaking $75 million ransom payment.
2. **Clop/Cl0p**: Specialists in large-scale supply chain attacks exploiting zero-day vulnerabilities in file transfer applications.
3. **DragonForce**: Operates under a "cartel" business model and has absorbed affiliates from other defunct groups.
4. **Akira**: Focuses on file encryption using Rust-based variants and targets ESXi and Windows environments.
5. **Interlock**: A newer group that leverages compliance frameworks (GDPR, HIPAA) to pressure victims.

---

## ThreatLabz Ransomware Notes Archive

Zscaler ThreatLabz maintains a public GitHub repository that added 73 new ransomware notes over the past year, bringing the total to 1,018.

---

## 2026 Predictions

1. **GenAI Weaponization**: Ransomware groups will use LLMs for phishing, malware development, and data summarization.
2. **Multi-stage Social Engineering**: A shift away from mass spam toward highly targeted, human-centric attacks.
3. **Rise of Vishing**: Increased use of AI-generated audio and voice cloning.
4. **Data Extortion Dominance**: Continued abandonment of encryption in favor of pure data theft.
5. **Leaked Code Proliferation**: Leaked builders will fuel a new wave of low-effort, high-impact attacks.
6. **Law Enforcement Focus**: Continued dismantling of ransomware enablers and infrastructure.
7. **Affiliate Volatility**: Frequent movement of affiliates between RaaS groups.

---

## How Zscaler Stops Ransomware with Zero Trust + AI

The Zscaler Zero Trust Exchange™ eliminates risks by replacing network-centric models with a cloud-native, AI-powered architecture:
- **Minimize the attack surface**: Hide users and applications behind a cloud proxy.
- **Prevent initial compromise**: Use full TLS/SSL inspection and inline sandboxing.
- **Eliminate lateral movement**: Connect users directly to applications, not the network.
- **Block data exfiltration**: Utilize inline DLP and CASB to stop data theft.

---

## Ransomware Prevention Checklist

- [ ] Implement Zero Trust architecture to eliminate lateral movement.
- [ ] Enforce strict TLS/SSL inspection for all traffic.
- [ ] Deploy inline sandboxing to detect unknown threats.
- [ ] Patch edge-facing services (VPNs, firewalls, backup systems) as a priority.
- [ ] Use AI-powered identity threat detection (ITDR).
- [ ] Implement robust data loss prevention (DLP) controls.

---

## Research Methodology

This report is based on data collected from the Zscaler cloud, which processes over 500 billion transactions daily, and analysis of ransomware leak sites and dark web forums conducted by the ThreatLabz research team between April 2024 and April 2025.

---

## About ThreatLabz

ThreatLabz is the dedicated research arm of Zscaler, responsible for tracking global threat activity and providing actionable intelligence to protect organizations.

---

## About Zscaler

Zscaler (NASDAQ: ZS) accelerates digital transformation by making customers more agile, efficient, resilient, and secure. The Zscaler Zero Trust Exchange protects thousands of customers from cyberattacks and data loss by securely connecting users, devices, and applications in any location.

---

on capabilities block unauthorized transfers to sanctioned
cloud apps, shadow IT, and command-and-control (C2) infrastructure.

©2025 Zscaler, Inc. All rights reserved.

31

Zscaler ThreatLabz 2025 Ransomware ReportK E Y   A I - P OW E R E D   R A N S O MWA R E   P R OT E C T I O N S   F R O M   Z S C A L E R

I N C LU D E:

•

•

•

Breach prediction preempts potential breach scenarios using
generative AI and multidimensional predictive models.

Phishing and C2 detection uses inline AI-based detection from the
Zscaler Secure Web Gateway to identify and block never-before-seen
phishing sites and C2 infrastructure.

Inline sandboxing offers comprehensive malware and zero-day threat
prevention by using advanced AI models to analyze suspicious files in a
controlled environment.

•  Zero Trust Browser leverages AI to identify and isolate malicious web

content, preventing data leaks and malware delivery.

•

Segmentation uses machine learning to auto-generate
recommendations for app segments and policies, ultimately minimizing
the attack surface and preventing lateral movement.

•  Dynamic, risk-based policy continuously evaluates the risk posture of
users, devices, and applications using AI-driven behavioral analysis to
enforce dynamic security and access policies.

•  Data discovery and classification instantly scans and classifies sensitive
data across endpoint, inline traffic, and cloud apps, making it more
difficult for ransomware to target and encrypt sensitive data.

•  Data loss prevention (DLP) controls block unauthorized data transfers,
backed by AI-based content inspection and policy enforcement,
preventing ransomware operators from stealing sensitive data
for extortion.

AS   R A N S O MWA R E   TAC T I C S   E VO LV E,

S O   M U S T   D E F E N S E S .  T H E   Z S C A L E R

Z E R O   T R U S T   E XC H A N G E   I S   I N T E G R A L

TO   H E L P I N G   O R GA N I Z AT I O N S   S H R I N K

T H E I R   AT TAC K   S U R FAC E,   S TO P   N OV E L

A N D   E VAS I V E   R A N S O MWA R E   T H R E AT S,

P R E V E N T   L AT E R A L   M OV E M E N T  (E V E N
P O S T- C O M P R O M I S E),  A N D   D I S R U P T

E X TO R T I O N   AT T E M P T S   B E F O R E   DATA   I S

E X F I LT R AT E D.

Zscaler ThreatLabz 2025 Ransomware Report

32

Zscaler ThreatLabz 2025 Ransomware Report©2025 Zscaler, Inc. All rights reserved.Ransomware Prevention_
Checklist

Zero trust is a must-have when it comes to stopping ransomware, but effective ransomware defense doesn’t stop there. It also depends on broader operational
layers, including employee training, secure backups, and a well-prepared response plan.

Based on insights from ThreatLabz experts, this checklist brings together the most effective steps you can take right now to reduce your ransomware risk and
build lasting resilience.

Back up data regularly

Enforce multifactor authentication (MFA)

Harden application security

•  Maintain routine, encrypted backups, both

online and offline.

•  Test recovery procedures frequently and
adapt backup strategies as ransomware
tactics evolve.

•

•

Require MFA across all user accounts,
especially for privileged access.
Integrate with identity protection to detect
and block account takeovers effectively.

•

•

Remove applications from public exposure
to prevent ransomware actors from
exploiting vulnerabilities.
Implement a zero trust architecture
for internal apps to safeguard them
against ransomware.

Keep software and systems up to date

Standardize corporate security policies

Apply least-privileged access controls

•  Apply the latest security patches promptly

to close known vulnerabilities.

•  Use AI-driven threat intelligence to prioritize

patching based on real-world risk.

•

Ensure all users follow consistent security
procedures, including MFA, software
updates, and access controls.
•  Adopt a security service edge (SSE)

architecture to protect users, whether on-
premises or remote.

•

•

Implement least-privileged policies to
limit users’ access strictly to the data and
systems required for their roles.
Employ AI-powered solutions to
dynamically analyze behavior and adjust
privileges accordingly.

33

Zscaler ThreatLabz 2025 Ransomware Report©2025 Zscaler, Inc. All rights reserved.Strengthen identity protection

Use AI-driven browser isolation

Leverage deception technology

Provide ongoing employee training

•  Use ITDR tools to monitor for identity

misconfigurations, remediate vulnerabilities
in Active Directory that adversaries exploit
to escalate privileges and move laterally,
and detect stealthy identity threats.

•

•

Safely isolate user sessions from the web to
prevent drive-by downloads, phishing, and
credential theft.
Let users access suspicious sites in a
contained, read-only environment.

•

Set traps (e.g., honeypots, fake credentials)
to detect, misdirect, and delay attackers
early in the kill chain.

•  Use alerts from deception systems to

speed up incident response.

•

•

Regularly educate users on ransomware
techniques, including phishing, social
engineering, and fake software updates.
Simulate real-world attack scenarios to
enhance employee preparedness.

Inspect all traffic—especially encrypted

Deploy AI-powered sandboxing

Control SaaS access with a CASB

Create a tested ransomware response plan

•

87% of threats hide in encrypted
channels—inspect all traffic, encrypted
or not, to uncover hidden threats and
prevent compromise.

•  Detect and block evasive, never-before-

•  Monitor and manage cloud app usage to

seen malware using AI/ML-behavior-
based analysis.

•  Quarantine suspicious files before they

•

reach endpoints.

block malicious activities like file downloads
and data exfiltration.
Enforce policies around data sharing and
downloads.

•

•

Include procedures for data
recovery, incident response, and
communication protocols.
Run regular tabletop exercises to evaluate
readiness and close gaps.

Implement zero trust network access (ZTNA)

Implement inline data loss prevention (DLP)

•

•

Replace broad network access with precise,
identity-based segmentation (user-to-app
and app-to-app).
Broker access via least-privileged access
controls to prevent lateral movement and
reduce attack surface.

•

Prevent data exfiltration and sensitive file
transfers by deploying inline DLP measures.
•  Apply policies across web, cloud, and email

channels.

Zscaler ThreatLabz 2025 Ransomware Report

34

©2025 Zscaler, Inc. All rights reserved.Research_
Methodology

The research methodology for this report is a comprehensive process that
uses multiple data sources to identify and track ransomware trends. The
ThreatLabz team collected data between April 2024 and April 2025 from
sources including:

•  The Zscaler global security cloud. Zscaler’s cloud processes more

than 500 trillion daily signals, blocks more than 9 billion total threats
and policy violations per day, and delivers 250,000+ daily security
updates to Zscaler customers. We analyzed this data, which includes
information about source IP addresses, destination IP addresses,
and file types associated with ransomware attacks, to identify
ransomware activity.

•  The ThreatLabz team’s own analysis of ransomware samples and

attack data. ThreatLabz tracks ransomware families and threat actors
along with corresponding attack telemetry. The team performs
deep-dive reverse engineering to understand the tools used by initial
access brokers as well as the ransomware itself, including the file
encryption algorithms. In a number of cases, the team has discovered
cryptographic flaws that can be exploited to decrypt files without
paying a ransom, and created decryption tools. The team provides
these tools to international law enforcement agencies to offer to
victims free of charge. ThreatLabz also has built a proprietary malware
automation platform that can automatically detect and stop threats in
Zscaler’s cloud.

•

External intelligence sources. We also compiled and compared our
own data with open source research where applicable.

About ThreatLabz

ThreatLabz is the security research arm of Zscaler.
This world–class team is responsible for hunting
new threats and ensuring that the thousands of
organizations using the global Zscaler platform are
always protected. In addition to malware research and
behavioral analysis, team members are involved in the
research and development of new prototype modules
for advanced threat protection on the Zscaler platform,
and regularly conduct internal security audits to ensure
that Zscaler products and infrastructure meet security
compliance standards. ThreatLabz regularly publishes
in-depth analyses of new and emerging threats on its
portal, research.zscaler.com.

Follow Zscaler ThreatLabz for regular
insights on the latest ransomware
threats and developments, including
published indicators of compromise
(IOCs) and MITRE ATT&CK mappings.
This information can be used to
train your team, improve your
security posture, and help prevent
ransomware attacks.

ThreatLabz also maintains GitHub
repositories with IOCs, tools
(including proof-of-concept
ransomware decryption tools), and an
archive of ransomware notes from all
major ransomware groups.

X @ThreatLabz

ThreatLabz security research blog

About Zscaler

Zscaler (NASDAQ: ZS) accelerates digital transformation so that customers can be more agile, efficient,
resilient, and secure. The Zscaler Zero Trust Exchange™ protects thousands of customers from
cyberattacks and data loss by securely connecting users, devices, and applications in any location.
Distributed across more than 160 data centers globally, the SASE–based Zero Trust Exchange is the
world’s largest inline cloud security platform. To learn more, visit www.zscaler.com.

©2025 Zscaler, Inc. All rights reserved.

35
35

©2025 Zscaler, Inc. All rights reserved.Zscaler ThreatLabz 2025 Ransomware ReportAbout Zscaler
Zscaler (NASDAQ: ZS) accelerates digital transformation so customers can be more agile, efficient, resilient, and
secure. The Zscaler Zero Trust Exchange™ platform protects thousands of customers from cyberattacks and data
loss by securely connecting users, devices, and applications in any location. Distributed across more than 160 data
centers globally, the SSE-based Zero Trust Exchange™ is the world’s largest in-line cloud security platform. Learn
more at zscaler.com or follow us on Twitter @zscaler.

© 2025 Zscaler, Inc. All rights reserved. Zscaler™ and other trademarks listed at zscaler.com/legal/trademarks are either (i) registered
trademarks or service marks or (ii) trademarks or service marks of Zscaler, Inc. in the United States and/or other countries. Any other
trademarks are the properties of their respective owners.

+1 408.533.0288

Zscaler, Inc. (HQ) • 120 Holger Way • San Jose, CA 95134

zscaler.com

Zero Trust Everywhere