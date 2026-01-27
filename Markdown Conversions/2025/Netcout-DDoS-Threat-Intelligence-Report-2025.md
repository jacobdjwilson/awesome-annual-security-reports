# DIGITAL AFTERSHOCKS: COLLATERAL DAMAGE FROM DDoS ATTACKS
## DDoS Threat Intelligence Report
### ISSUE 15: FINDINGS FROM 1H 2025

## Table of Contents
- [INTRODUCTION: Key Findings](#introduction-key-findings)
- [Section 1: State of DDoS](#section-1-state-of-ddos)
- [Section 2: Geopolitical Events Drive Global DDoS Trends](#section-2-geopolitical-events-drive-global-ddos-trends)
- [Section 3: Botnets and Familiar Foes Drive DDoS Attack Activity](#section-3-botnets-and-familiar-foes-drive-ddos-attack-activity)
- [Section 4: Threat Actor Profiles](#section-4-threat-actor-profiles)
- [Conclusion](#conclusion)
- [Methodology](#methodology)
- [How NETSCOUT Can Help](#how-netscout-can-help)

---

## INTRODUCTION: Key Findings

The NETSCOUT® 1H 2025 report is a concise, research-based analysis of the evolving distributed-denial-of-service (DDoS) attack and defense landscape. Designed to quickly equip readers with actionable intelligence, it delivers insights critical for ongoing network operations and strategic planning.

The digital battlefield of 2025 is defined by an unprecedented escalation in DDoS warfare, with more than 8 million attacks recorded in the first half alone. These attacks have evolved beyond simple disruption tools into precision-guided weapons of geopolitical influence, capable of destabilizing critical infrastructure at the most crucial moments. High-profile events have become focal points for this digital warfare. During the World Economic Forum in January, for example, Switzerland saw attack volumes double to over 1,400 incidents compared to similar time periods in December. This occurred alongside relentless campaigns from hacktivist groups like NoName057(16), who orchestrated hundreds of coordinated strikes monthly. Arms-length nation-state actors have weaponized DDoS to target communications, transportation, energy, and defense sectors, often operated by private industry, creating cascading effects across interconnected networks.

Driving this surge is the democratization of attack tools. Readily available DDoS-for-hire services have erased the barrier to entry, enabling even novice actors to launch sophisticated campaigns. This accessibility is amplified by new technologies: Artificial Intelligence (AI)-enhanced automation, multi-vector attacks, and carpet-bombing techniques now overwhelm traditional defenses with ease. Vast botnets compromising of tens of thousands of compromised Internet of Things (IoT) devices, servers, and routers deliver sustained attacks averaging 18 minutes, more than enough time to inflict significant operational disruption. The recent Iran-Israel cyber conflict, which generated more than 15,000 attacks, shows how quickly regional tensions rapidly escalate into global digital warfare.

This evolving threat landscape demands immediate action. Organizations can no longer rely on reactive defenses against attackers that adapt faster than security teams can respond. The integration of AI, the persistence of botnets that swiftly regroup after takedowns, and the exploitation of known vulnerabilities create a perfect storm of cyber risk. Without comprehensive visibility into attack patterns, real-time threat intelligence, and proactive mitigation strategies, organizations remain vulnerable to attacks that not only target them directly but also create collateral damage across entire service provider networks. The urgency for adaptive, intelligence-driven DDoS protection has never been greater.

### KEY FINDINGS

- **Global DDoS Attack Volume Remains Massive, with Regional Variations**: The first half of 2025 recorded 8,062,971 attacks globally, with EMEA bearing the heaviest burden at 3.2 million attacks. Peak attacks reached devastating speeds of 3.12 Tbps and 1.5 Gpps, demonstrating sustained intensity despite volume fluctuations.
- **Geopolitical Events Trigger Unprecedented DDoS Campaigns**: Major political events catalyzed massive attack spikes; during the World Economic Forum Switzerland saw more than 1,400 attacks (double normal rates when compared to similar time periods in December), Italy faced sustained targeting during political discussions, and the India-Pakistan conflict saw hacktivist groups such as SYLHET GANG-SG and Keymous+ target Indian government and financial sectors, while the Iran-Israel conflict generated more than 15,000 attacks against Iran versus 279 against Israel.
- **Botnet-Driven Attacks Dominate with Increased Sophistication**: March 2025 averaged 880 bot-driven DDoS attacks daily, peaking at 1,600 incidents. Attack durations increased to an average of 18 minutes and 24 seconds, with threat actors employing complex multi-vector combinations and exploiting known vulnerabilities in IoT devices, servers, and routers.
- **NoName057(16) Maintains Dominance Among Familiar Threat Actors**: The hacktivist group claimed more than 475 attacks in March alone, 337% more than the next most active group, targeting government websites in Spain, Taiwan, and Ukraine with TCP ACK floods, TCP SYN floods, and HTTP/2 POST requests.
- **New Threat Actors Emerge with DDoS-as-a-Service Capabilities**: DieNet orchestrated over 60 attacks since March 2025, while Keymous+ confirmed 73 attacks across 28 industry sectors in 23 countries. Both groups leverage shared DDoS-for-hire infrastructure, lowering barriers to entry and expanding the threat landscape.

---

## SECTION 01: STATE OF DDoS

To understand the gravity of today's DDoS threat landscape, we must first examine raw data revealing attack patterns across global regions. The following analysis breaks down attack volumes, vectors, and intensities that shaped the first half of 2025, providing critical context for the geopolitical and tactical trends that follow.

### Global Highlights
- **Total Attack Count**: 8,062,971

### NAMER Highlights
- **Attack Count**: 1,306,278
- **Largest Attack by Throughput**:
  - Date: 3/30/25
  - Max Throughput: 612.90 Mpps
  - Average Packet Size: 200 Bytes
  - Target: United States
  - Vectors: TCP ACK
- **Largest Attack by Bandwidth**:
  - Date: 6/13/25
  - Max Bandwidth: 1.48 Tbps
  - Average Packet Size: 1,390 Bytes
  - Target: United States
  - Vectors: CLDAP Amplification, UDP Flood

### LATAM Highlights
- **Attack Count**: 1,070,492
- **Largest Attack by Throughput**:
  - Date: 2/3/25
  - Max Throughput: 290.38 Mpps
  - Average Packet Size: 51 Bytes
  - Target: Brazil
  - Vectors: DNS, DNS Amplification, ICMP, NTP Amplification, TCP ACK, TCP RST, TCP SYN, TCP SYN/ACK Amplification
- **Largest Attack by Bandwidth**:
  - Date: 1/23/2025
  - Max Bandwidth: 477.53 Gbps
  - Average Packet Size: 1,312 Bytes
  - Target: Puerto Rico
  - Vectors: DNS, DNS Amplification, ICMP, TCP ACK, TCP RST, TCP SYN/ACK Amplification

### EMEA Highlights
- **Attack Count**: 3,268,863
- **Largest Attack by Throughput**:
  - Date: 4/25/25
  - Max Throughput: 1.50 Gpps
  - Average Packet Size: 36 Bytes
  - Target: Germany
  - Vectors: CLDAP Amplification, DNS, L2TP Amplification, MS SQL RS Amplification, NTP Amplification, NetBIOS Amplification, RIPv1
- **Largest Attack by Bandwidth**:
  - Date: 2/24/25
  - Max Bandwidth: 3.12 Tbps
  - Average Packet Size: 1,384 Bytes
  - Target: Netherlands
  - Vectors: DNS, DNS Amplification, ICMP, L2TP Amplification, MS SQL RS Amplification, NetBIOS Amplification, RIPv1 Amplification, SNMP

### APAC Highlights
- **Attack Count**: 1,846,922
- **Largest Attack by Throughput**:
  - Date: 2/20/2025
  - Max Throughput: 741.80 Mpps
  - Average Packet Size: 61 Bytes
  - Target: Indonesia
  - Vectors: DNS, ICMP, TCP SYN
- **Largest Attack by Bandwidth**:
  - Date: 3/2/2025
  - Max Bandwidth: 1.43 Tbps
  - Average Packet Size: 540 Bytes
  - Target: Australia
  - Vectors: CLDAP Amplification, L2TP Amplification, NTP Amplification, NetBIOS Amplification, SNMP Amplification, SSDP Amplification, TCP SYN, Chargen Amplification, mDNS Amplification

_Note: The sum of regional attack counts differs from the global attack count due to differences in GeoIP enrichment availability._

---

## SECTION 02: Global DDoS Trends Mirror Geopolitical Unrest

Although these statistics paint a sobering picture of DDoS prevalence, the numbers alone don't reveal the calculated timing and political motivations driving many attacks. The following section explores how major geopolitical events served as catalysts for coordinated DDoS campaigns, transforming digital attacks into instruments of political influence and disruption.

### Switzerland: JANUARY 20–24
#### DDoS Attacks at the World Economic Forum

During the annual World Economic Forum (WEF) held in Davos-Klosters, Switzerland, from January 20th to 24th, several notable events garnered significant media attention. Notably, prominent political figures delivered several special addresses that drew substantial public interest. NETSCOUT’s ASERT team observed a notable surge in DDoS attacks shortly preceding and during at least one of these addresses.

During the event’s commencement and conclusion, ASERT detected more than 1,400 DDoS attacks of diverse magnitudes and attack vectors. Notably, the observed attack frequency during and immediately preceding the WEF was approximately double that of comparable time periods in December.

![Figure 1: Three DDoS attack metrics (Attacks, Max Impact Gbps, Max Impact Mpps) as observed by ASERT during the WEF. Grey regions mark the official schedule, showing spikes coinciding with political addresses.]

### Italy: FEBRUARY 16 – MARCH 03
#### Italy in the Crosshairs

During the period of February to March 2025, a series of political discussions appear to have attracted the attention of several threat actors, including NoName057(16). The targeted industries exhibit similar patterns observed in previous incidents. However, it is noteworthy that some additional targeting may not have been intentional.

ASERT identified a substantial proportion of publicly reported DDoS attacks occurring between February 16 and March 03, which were specifically targeted at public sector entities within regional and local Italian jurisdictions.

![Figure 2: Overview of three months of cyber incidents publicly claimed by threat actors against Italian organizations, showing a significant surge in incidents between Feb 15 and March 01.]

### India: MAY 03–09
#### DDoS Attacks in India Amid India-Pakistan Conflict

Escalating geopolitical tensions between India and Pakistan have extended into the realm of cyberspace, resulting in a notable surge in claims of DDoS attacks directed at Indian organizations. Hacktivist groups have seized public social media platforms to publicly display their online operations against critical Indian infrastructure. These groups include SYLHET GANG-SG, Keymous+, AnonSec, and others.

![Figure 3: Adversary Attack Claims (count by website) showing various attack types including DDoS, Defacement, and Data Breach.]

![Figure 4: Daily Attack Count + Maximum Bits-Per-Second (Gbps) for India, showing peak attack counts exceeding 1,500 per day in early May.]

### Iran & Israel: JUNE 13
#### Iran-Israel Cyberwarfare Escalates

Upon the commencement of Operation Rising Lion on June 13, 2025, the Iran-Israel cyber conflict intensified, characterized by substantial DDoS attacks. Iran endured more than 15,000 cyberattacks in comparison to Israel’s 279 since June 13, 2025, with a peak of nearly 2,800 attacks occurring within a single day.

![Figure 5: Daily DDoS attack frequency through June 25, 2025, comparing Israel and Iran. Iran shows significantly higher attack volumes, peaking near 3,000 attacks daily.]

---

## SECTION 03: Botnets and Familiar Foes Drive DDoS Attack Activity

Behind these politically motivated campaigns lies a robust infrastructure of botnets and experienced threat actors who have perfected their craft.

Attackers didn’t need new exploits to drive more than 27,000 botnet-driven DDoS attacks in March 2025. Instead, they exploited previously known vulnerabilities to execute more sophisticated and enduring campaigns that targeted service providers with an average of one attack every two minutes.

NETSCOUT detected persistent bot-driven DDoS activity directed at the service provider sector throughout March 2025. On average, approximately 880 confirmed DDoS attack events per day were recorded, with a peak on March 10 when more than 1,600 incidents were observed. These attacks were fueled by substantial, distributed botnets constructed via the exploitation of predominantly known vulnerabilities in web servers, routers, and IoT devices.

The hacktivist group NoName057(16) maintained its dominance in both claimed operations and actual attack activity. The group frequently employed various techniques, including TCP ACK floods, TCP SYN floods, and even HTTP/2 POST requests.

![Image description: A composite chart showing the Number of DDoS Attack Events in March 2025, peaking mid-month, and a bar chart of DDoS Vector Combinations including TCP SYN, TCP ACK, and DNS Amplification.]

![Image description: Bar chart showing the Number of Claimed DDoS Attacks in March 2025 by Threat Actor. NoName057(16) leads significantly with over 400 claims, followed by Keymous+, Dark Storm Team, and others.]

---

## SECTION 04: Threat Actor Profiles

### A New Hacktivist Threat, Profiling DieNet

In the spring of 2025, DieNet, a newly formed hacktivist group, orchestrated more than 60 DDoS attacks, targeting critical infrastructure from United States transit systems to Iraqi government websites. The group made its public debut on March 7, 2025. ASERT has identified that DieNet utilizes DDoS-as-a-service infrastructure, shared with other groups such as OverFlame and DenBots Proof. DieNet’s targets encompass transportation, energy, medical systems, and digital commerce.

![Figure 6: Daily attack count prior to and following DieNet's launch, showing a sharp increase in attacks featuring DieNet associated infrastructure starting in early March.]

---

## CONCLUSION

The relentless evolution of DDoS threats demands equally sophisticated defenses. NETSCOUT's comprehensive protection ecosystem, including Arbor Edge Defense® for perimeter security, Arbor Sightline for network-wide visibility and detection, and the Arbor Threat Mitigation System™ for surgical attack response, provides the multi-layered defense required in today's threat landscape. NETSCOUT's Arbor DDoS Protection leverages AI to counter AI-enhanced attacks, while the AI-powered ATLAS Intelligence Feed® delivers real-time threat data from defending two-thirds of global IPv4 space.

### CONTRIBUTORS
- Chris Conrad, Writer/Editor
- Richard Hummel, Writer/Editor
- Gary Sockrider, Writer/Editor
- Filippo Vitale, Writer
- Marcin Nawrocki, Writer
- Max Resing, Writer

---

## METHODOLOGY

NETSCOUT maps the DDoS landscape via passive, active, and reactive vantage points, providing unparalleled visibility into global attack trends. We protect two-thirds of the routed IPv4 space, securing network edges that faced global peak traffic of over 800Tbps in 1H 2025. By tracking multiple botnets and DDoS-for-hire services that leverage millions of abused or compromised devices, we monitor tens of thousands of daily DDoS attacks.

### ABOUT ASERT
ASERT is NETSCOUT’s elite group of engineers and researchers specializing in information security. Their breadth and depth of knowledge and real-world experience combined with NETSCOUT’s unique, unrivaled visibility into global internet traffic and the threat landscape, enables them to provide insights and mediation for customers to manage active threats and their long-term security profile.

### ABOUT NETSCOUT
NETSCOUT SYSTEMS, INC. (NASDAQ: NTCT) is a leading provider of observability, AIOps, cybersecurity, and DDoS attack protection solutions. NETSCOUT protects the connected world from cyberattacks and performance and availability disruptions through its unique visibility platform and solutions powered by its pioneering deep packet inspection at scale technology.

---

## HOW NETSCOUT CAN HELP

### NETSCOUT ARBOR DDoS ATTACK PROTECTION SOLUTIONS
The intelligent combination of AI/ML-powered on-premises and cloud-based protection is designed to manage all modern-day DDoS attacks.

![Image description: Architectural diagram of NETSCOUT Arbor DDoS Protection. It shows the Internet connecting to an ISP Backbone containing Arbor Cloud (16 scrubbing centers, 15Tbps+ capacity) and Sightline + TMS for automated detection and surgical mitigation. The traffic then flows to the On-Prem Inline environment protected by Arbor Edge Defense (AED) before reaching Applications & Services.]

#### NETSCOUT Solutions
- **ATLAS Intelligence Feed (AIF)**: AI/ML-powered analysis continuously updates DDoS products and services.
- **Adaptive DDoS Protection**: Neutralizes attacks against enterprises and service providers; leverages AIF to automatically and accurately block malicious traffic.

#### Best Practices for DDoS Defense
- **Enterprise**: Hybrid on-premises or inline plus cloud-based solutions; intelligent and automated integration; robust defenses against all types of DDoS attacks.
- **Service Providers**: AI- and ML-powered DDoS attack mitigation of NETSCOUT Arbor Sightline and NETSCOUT Arbor Threat Mitigation System (TMS) to protect complex large-scale networks.

### Summary of Support
- **Geopolitical Events**: Geopolitical unrest serves as a driving force behind DDoS attacks. Arbor Sightline and TMS provide automated detection and substantial mitigation capabilities.
- **Botnet-Driven Attacks**: Arbor DDoS protection offers a hybrid combination of on-premises and cloud-based mitigation against increasingly sophisticated multi-vector botnets.
- **Threat Actors with DDoS-as-a-Service**: Arbor Edge Defense, Sightline, Threat Mitigation System and the ATLAS Intelligence Feed effectively thwart sophisticated attacks from actors using AI-enhanced DDoS-for-hire services.

---
**NETSCOUT.COM**
Follow @NETSCOUT
©2025 NETSCOUT SYSTEMS, INC. All rights reserved.
SECR_001_EN-2501 1H 2025 08/2025