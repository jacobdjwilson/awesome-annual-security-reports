# DIGITAL AFTERSHOCKS: COLLATERAL DAMAGE FROM DDoS ATTACKS

DDoS Threat Intelligence Report
ISSUE 15: FINDINGS FROM 1H 2025

## Table of Contents
- [Introduction: Key Findings](#introduction-key-findings)
- [Section 1: State of DDoS](#section-1-state-of-ddos)
- [Section 2: Geopolitical Events Drive Global DDoS Trends](#section-2-geopolitical-events-drive-global-ddos-trends)
- [Section 3: Botnets and Familiar Foes Drive DDoS Attack Activity](#section-3-botnets-and-familiar-foes-drive-ddos-attack-activity)
- [Section 4: Threat Actor Profiles](#section-4-threat-actor-profiles)
- [Conclusion](#conclusion)
- [Methodology](#methodology)
- [How NETSCOUT Can Help](#how-netscout-can-help)

---

## Introduction: Key Findings

The NETSCOUT® 1H2025 report is a concise, research-based analysis of the evolving distributed-denial-of-service (DDoS) attack and defense landscape. Designed to quickly equip readers with actionable intelligence, it delivers insights critical for ongoing network operations and strategic planning.

The digital battlefield of 2025 is defined by an unprecedented escalation in DDoS warfare, with more than 8 million attacks recorded in the first half alone. These attacks have evolved beyond simple disruption tools into precision-guided weapons of geopolitical influence, capable of destabilizing critical infrastructure at the most crucial moments. High-profile events have become focal points for this digital warfare. During the World Economic Forum in January, for example, Switzerland saw attack volumes double to over 1,400 incidents compared to similar time periods in December. This occurred alongside relentless campaigns from hacktivist groups like NoName057(16), who orchestrated hundreds of coordinated strikes monthly. Arms-length nation-state actors have weaponized DDoS to target communications, transportation, energy, and defense sectors, often operated by private industry, creating cascading effects across interconnected networks.

Driving this surge is the democratization of attack tools. Readily available DDoS-for-hire services have erased the barrier to entry, enabling even novice actors to launch sophisticated campaigns. This accessibility is amplified by new technologies: Artificial Intelligence (AI)-enhanced automation, multi-vector attacks, and carpet-bombing techniques now overwhelm traditional defenses with ease. Vast botnets compromising of tens of thousands of compromised Internet of Things (IoT) devices, servers, and routers deliver sustained attacks averaging 18 minutes, more than enough time to inflict significant operational disruption. The recent Iran-Israel cyber conflict, which generated more than 15,000 attacks, shows how quickly regional tensions rapidly escalate into global digital warfare.

This evolving threat landscape demands immediate action. Organizations can no longer rely on reactive defenses against attackers that adapt faster than security teams can respond. The integration of AI, the persistence of botnets that swiftly regroup after takedowns, and the exploitation of known vulnerabilities create a perfect storm of cyber risk. Without comprehensive visibility into attack patterns, real-time threat intelligence, and proactive mitigation strategies, organizations remain vulnerable to attacks that not only target them directly but also create collateral damage across entire service provider networks. The urgency for adaptive, intelligence-driven DDoS protection has never been greater.

### Key Findings
- **Global DDoS Attack Volume Remains Massive, with Regional Variations**: The first half of 2025 recorded 8,062,971 attacks globally, with EMEA bearing the heaviest burden at 3.2 million attacks. Peak attacks reached devastating speeds of 3.12 Tbps and 1.5 Gpps, demonstrating sustained intensity despite volume fluctuations.
- **Geopolitical Events Trigger Unprecedented DDoS Campaigns**: Major political events catalyzed massive attack spikes; during the World Economic Forum Switzerland saw more than 1,400 attacks (double normal rates when compared to similar time periods in December), Italy faced sustained targeting during political discussions, and the India-Pakistan conflict saw hacktivist groups such as SYLHET GANG-SG and Keymous+ target Indian government and financial sectors, while the Iran-Israel conflict generated more than 15,000 attacks against Iran versus 279 against Israel.
- **Botnet-Driven Attacks Dominate with Increased Sophistication**: March 2025 averaged 880 bot-driven DDoS attacks daily, peaking at 1,600 incidents. Attack durations increased to an average of 18 minutes and 24 seconds, with threat actors employing complex multi-vector combinations and exploiting known vulnerabilities in IoT devices, servers, and routers.
- **NoName057(16) Maintains Dominance Among Familiar Threat Actors**: The hacktivist group claimed more than 475 attacks in March alone, 337% more than the next most active group, targeting government websites in Spain, Taiwan, and Ukraine with TCP ACK floods, TCP SYN floods, and HTTP/2 POST requests.
- **New Threat Actors Emerge with DDoS-as-a-Service Capabilities**: DieNet orchestrated over 60 attacks since March 2025, while Keymous+ confirmed 73 attacks across 28 industry sectors in 23 countries. Both groups leverage shared DDoS-for-hire infrastructure, lowering barriers to entry and expanding the threat landscape.

---

## Section 1: State of DDoS

To understand the gravity of today's DDoS threat landscape, we must first examine raw data revealing attack patterns across global regions. The following analysis breaks down attack volumes, vectors, and intensities that shaped the first half of 2025, providing critical context for the geopolitical and tactical trends that follow.

### Global Highlights
- **Attack Count**: 8,062,971

### NAMER Highlights
- **Attack Count**: 1,306,278
- **Largest Attack by Throughput**: 612.90 Mpps (Date: 3/30/25, Target: United States)
- **Largest Attack by Bandwidth**: 1.48 Tbps (Date: 6/13/25, Target: United States)
- **Vectors**: TCP ACK; CLDAP Amplification, UDP Flood

### LATAM Highlights
- **Attack Count**: 1,070,492
- **Largest Attack by Throughput**: 290.38 Mpps (Date: 2/3/25, Target: Brazil)
- **Largest Attack by Bandwidth**: 477.53 Gbps (Date: 1/23/2025, Target: Puerto Rico)
- **Vectors**: DNS, DNS Amplification, ICMP, NTP Amplification, TCP ACK, TCP RST, TCP SYN, TCP SYN/ACK Amplification; DNS, DNS Amplification, ICMP, TCP ACK, TCP RST, TCP SYN/ACK Amplification

### EMEA Highlights
- **Attack Count**: 3,268,863
- **Largest Attack by Throughput**: 1.50 Gpps (Date: 4/25/25, Target: Germany)
- **Largest Attack by Bandwidth**: 3.12 Tbps (Date: 2/24/25, Target: Netherlands)
- **Vectors**: CLDAP Amplification, DNS, L2TP Amplification, MS SQL RS Amplification, NTP Amplification, NetBIOS Amplification, RIPv1; DNS, DNS Amplification, ICMP, L2TP Amplification, MS SQL RS Amplification, NetBIOS Amplification, RIPv1 Amplification, SNMP

### APAC Highlights
- **Attack Count**: 1,846,922
- **Largest Attack by Throughput**: 741.80 Mpps (Date: 2/20/2025, Target: Indonesia)
- **Largest Attack by Bandwidth**: 1.43 Tbps (Date: 3/2/2025, Target: Australia)
- **Vectors**: DNS, ICMP, TCP SYN; CLDAP Amplification, L2TP Amplification, NTP Amplification, NetBIOS Amplification, SNMP Amplification, SSDP Amplification, TCP SYN, Chargen Amplification, mDNS Amplification

*Note: The sum of regional attack counts differs from the global attack count due to differences in GeoIP enrichment availability.*

---

## Section 2: Geopolitical Events Drive Global DDoS Trends

Although these statistics paint a sobering picture of DDoS prevalence, the numbers alone don't reveal the calculated timing and political motivations driving many attacks. The following section explores how major geopolitical events served as catalysts for coordinated DDoS campaigns.

### Switzerland: DDoS Attacks at the World Economic Forum
During the annual World Economic Forum (WEF) held in Davos-Klosters, Switzerland, from January 20th to 24th, NETSCOUT’s ASERT team observed a notable surge in DDoS attacks. During the event’s commencement and conclusion, ASERT detected more than 1,400 DDoS attacks. Observed attack frequency was approximately double that of comparable time periods in December.
![Graph showing three DDoS attack metrics (Attacks, Max Impact Gbps, Max Impact Mpps) during the WEF schedule]

### Italy: Italy in the Crosshairs
During February to March 2025, political discussions attracted threat actors, including NoName057(16). Reports of cyberattacks against Italian entities experienced a surge on February 16th, persisting for two weeks. ASERT identified a substantial proportion of publicly reported DDoS attacks specifically targeted at public sector entities within regional and local Italian jurisdictions.
![Graph showing three months of cyber incidents publicly claimed by threat actors against Italian organizations]

### India: DDoS Attacks in India Amid India-Pakistan Conflict
Escalating geopolitical tensions between India and Pakistan resulted in a surge in DDoS attacks directed at Indian organizations. Hacktivist groups including SYLHET GANG-SG, Keymous+, and AnonSec asserted attacks on government, defense, and financial sectors. NETSCOUT’s ATLAS® telemetry data shows that Indian network operators successfully mitigated these threats, preventing widespread disruptions.
![Graph showing Adversary Attack Claims (count by website)]
![Graph showing Daily Attack Count + Maximum Bits-Per-Second]

### Iran/Israel: Iran-Israel Cyberwarfare Escalates
Upon the commencement of Operation Rising Lion on June 13, 2025, the Iran-Israel cyber conflict intensified. Iran endured more than 15,000 cyberattacks compared to Israel’s 279. Notably, nearly all 15,000 attacks on Iran were observed from networks outside Iran.
![Graph showing daily DDoS attack frequency through June 25, 2025]
![Graph comparing attack counts between Israel and Iran]

---

## Section 3: Botnets and Familiar Foes Drive DDoS Attack Activity

Attackers didn’t need new exploits to drive more than 27,000 botnet-driven DDoS attacks in March 2025. Instead, they exploited previously known vulnerabilities to execute more sophisticated and enduring campaigns.

- **Average Attacks**: ~880 confirmed DDoS attack events per day in March 2025.
- **Peak**: March 10, with more than 1,600 incidents.
- **Tactics**: Attackers employed intricate multi-vector combinations, expanded port targeting, and extended attack durations.
- **NoName057(16)**: Maintained dominance using TCP ACK floods, TCP SYN floods, and HTTP/2 POST requests against government websites in Spain, Taiwan, and Ukraine.

![Graph showing number of claimed DDoS attacks in March 2025 by threat actor]
![Graph showing DDoS vector combinations]

---

## Section 4: Threat Actor Profiles

### A New Hacktivist Threat, Profiling DieNet
In the spring of 2025, DieNet, a newly formed hacktivist group, orchestrated more than 60 DDoS attacks. The group made its public debut on March 7, 2025. ASERT identified that DieNet utilizes DDoS-as-a-service infrastructure, shared with other groups such as OverFlame and DenBots Proof. Their targets encompass transportation, energy, medical systems, and digital commerce.

![Graph showing daily attack count prior to and following DieNet's launch]

---

## Conclusion

The relentless evolution of DDoS threats demands equally sophisticated defenses. NETSCOUT's comprehensive protection ecosystem—including Arbor Edge Defense®, Arbor Sightline, and the Arbor Threat Mitigation System™—provides the multi-layered defense required in today's threat landscape. As DDoS solidifies its role as a primary cyberweapon, organizations must embrace proactive, intelligence-driven strategies.

---

## Methodology

NETSCOUT maps the DDoS landscape via passive, active, and reactive vantage points. We protect two-thirds of the routed IPv4 space, securing network edges that faced global peak traffic of over 800Tbps in 1H 2025. The data in this report is derived from NETSCOUT’s ATLAS Threat Intelligence, which analyzes DDoS attacks from 205 countries and territories, 398 industry verticals, and 15,612 autonomous system numbers (ASNs).

---

## How NETSCOUT Can Help

### NETSCOUT Arbor DDoS Attack Protection Solutions
The intelligent combination of AI/ML-powered on-premises and cloud-based protection is designed to manage all modern-day DDoS attacks.

- **Arbor Cloud**: In-cloud DDoS attack protection with 16 scrubbing centers and 15Tbps+ capacity.
- **Cloud Signaling**: Provides communication between NETSCOUT Arbor mitigation solutions.
- **Sightline + TMS**: Automated detection, out-of-band surgical, stateless mitigation (up to 400G per device).
- **Arbor Edge Defense (AED)**: Always-on, stateless protection (up to 200G per device) from inbound and outbound threats.

### Best Practices for DDoS Defense
- **Enterprise**: Blending the power of AI/ML-fueled NETSCOUT Arbor Edge Defense (AED) and the massive upstream DDoS scrubbing capacity of NETSCOUT Arbor Cloud.
- **Service Providers**: AI- and ML-powered DDoS attack mitigation of NETSCOUT Arbor Sightline and NETSCOUT Arbor Threat Mitigation System (TMS) to protect complex large-scale networks.

---
*©2025 NETSCOUT SYSTEMS, INC. All rights reserved.*