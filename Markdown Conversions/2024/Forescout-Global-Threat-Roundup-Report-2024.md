# Global-Threat-Roundup-Report 2024

## Table of Contents
- [1. Executive Summary](#1-executive-summary)
- [2. Main Findings](#2-main-findings)
  - [2.1. Location – Russia Retakes China’s Position](#21-location--russia-retakes-chinas-position)
  - [2.2. Autonomous Systems – New Techniques for Routing Attacks](#22-autonomous-systems--new-techniques-for-routing-attacks)
  - [2.3. Attacked Services – the Web Is the Undisputed Leader](#23-attacked-services--the-web-is-the-undisputed-leader)
  - [2.4. Weak Credentials – a Return to Generic Usernames](#24-weak-credentials--a-return-to-generic-usernames)
  - [2.5. Exploits – There’s Still Much Beyond KEV](#25-exploits--theres-still-much-beyond-kev)
  - [2.6. OT Attacks – Increased Focus on Building Automation](#26-ot-attacks--increased-focus-on-building-automation)
  - [2.7. Attacker Actions/TTPs – the Rise of Discovery](#27-attacker-actionsttps--the-rise-of-discovery)
  - [2.8. Malware – Botnets Again at the Top](#28-malware--botnets-again-at-the-top)
  - [2.9. Threat Actors – More Conflicts Bring More Threat Actors to the Scene](#29-threat-actors--more-conflicts-bring-more-threat-actors-to-the-scene)
- [3. Evolution of Attacks on Critical Infrastructure](#3-evolution-of-attacks-on-critical-infrastructure)
  - [3.1. Who Is Being Attacked?](#31-who-is-being-attacked)
  - [3.2. Who Is Attacking?](#32-who-is-attacking)
- [4. Conclusion](#4-conclusion)

---

## 1. Executive Summary
From the financial impact of attacks to geopolitical tensions that lead to cyber warfare, cybersecurity is top of mind for enterprise and government organizations in 2025. In this report, we look back at the 900 million attacks we analyzed in the threat landscape of 2024. Additionally, we offer organizations tactical insights and strategic recommendations for improving defenses this year.

Cyber attacks are on the rise once again – including an uptick of targets in critical infrastructure in the last year. Since 2022, however, reported incidents in critical infrastructure rose from 50 to 384 globally – or 668%, according to data from the European Repository of Cyber Incidents, an independent research consortium that provides scientific analysis of cyber incidents.

Take note: We also include information on vulnerabilities and exploits that are not on the CISA-KEV list but are being exploited today.

---

## Where Does Our Data Come From?
Most data used for our analysis comes from the Vedere Labs Adversary Engagement Environment (AEE), a set of honeypots on the open internet luring attackers and recording their interactions. Data points in the AEE are called attacks. They can represent a multitude of malicious actions, including port scanning and brute forcing. The AEE recorded more than 900 million attacks between January and December 2024. A subset of these attacks contains exploits – attempts to exploit vulnerabilities.

Our data differs from what is seen in many other threat reports because it comes from specialized IT/OT/IoT honeypots that either mimic realistic device profiles – including exposed protocols, banners and parts of the filesystem – or are real specialized devices, instead of generic honeypots capturing every kind of attack.

Our Malware Analysis Lab (MAL) collects and analyzes samples dropped by attackers on the AEE or shared on public repositories. Our goal is not to analyze as many samples as possible, but to focus on those that are unique. We analyzed more than 100,000 unique malware samples between January and December 2024.

Also, we constantly hunt for new command and control (C2) infrastructure and maintain a threat actor knowledgebase with data about more than 800 threat actors.

![Diagram showing the relationship between Attackers, AEE, MAL, Threat Actor Knowledgebase, Security Researcher, Intel Factory, Infrastructure, and C2 Hunting]

---

## 2. Main Findings

### 2.1. Location – Russia Retakes China’s Position
![Figure 1 – Distribution of attacks by IP address country of origin]

Figure 1 shows the distribution of attacks detected by country of origin. We detected attacks originating from 213 countries and territories (1 more than in 2023 and 22 more than in 2022). Countries appear in this list due to the presence of legitimate hosting providers being abused by attackers; the presence of bulletproof hosting providers that cater specifically to cybercriminal activities; or the use of compromised hosts to launch attacks.

This year, the top 10 countries accounted for 78% of the malicious traffic. This is a negligible difference of 1% more than in 2023 but consistent with the growth observed since 2022 (73%). The top 10 list of countries originating attacks has only one entry different from 2023: Poland replaced Singapore. However, the ranks have changed considerably. The most notable change: Russia rose from 9% to 16% of attacks. China decreased from 18% to 8%.

It is important to stress that it is not direct attribution for attack locations. It is only where we can see attacks coming from as they hit our honeypots. Our threat actor database shows that most actors are still located in China — although it does not necessarily mean it is the source of individual attacks.

**Fact**: China and Russia have been in the top 3 of IP address attack origin since 2022.

**Insight for Defenders**: Country of origin alone continues to be ineffective to judge the risk of a particular IP address. However, if your organization does not do business with – or in – countries with the highest number of IP addresses that attack, blocking those IP ranges may help reduce SOC noise.

### 2.2. Autonomous Systems – New Techniques for Routing Attacks
![Figure 2 – Distribution of attacks by originating Autonomous System]

Attacks again originated from more than 500 autonomous systems (AS), which are blocks of IP addresses under the control of an organization. Figure 2 shows the percentage of attacks coming from the three types of AS we observe:

- Internet Service Providers (ISPs) increased from 53% in 2023 to 57% in 2024
- Business, Government, and others decreased from 36% to 33%.
- Hosting or cloud providers decreased from to 11% to 10%.

As we discussed last year, the large chunk of attacks coming from ISPs as well as business, government and other organizations signifies an increase in the use of compromised devices to launch attacks as opposed to leasing infrastructure from dedicated providers.

In 2023, we attributed this to the increased popularity of “residential proxy” services. However, advanced persistent threat actors have now gone even further and developed Operational Relay Boxes (ORB) networks, where they mix virtual private servers, compromised IoT and hijacked network perimeter devices, creating layers of proxying to make detection and attribution of attacks more challenging.

**Fact**: Autonomous Systems continue to be a better sign of risk than country of origin.

**Insight for Defenders**: IPs belonging to known risky autonomous systems should always be treated with care — especially those that remain in the top 10 for years, such as Digital Ocean. Continued attacker interest in compromised devices to route action shows organizations need real-time threat intelligence about compromised devices in the wild and the types of device attackers focus on.

### 2.3. Attacked Services – the Web Is the Undisputed Leader
![Figure 3 – Distribution of attacked ports and services]

Figure 3 shows the share of traffic targeting each type of network service. Web applications increased from 26% in 2022 and 2023 to 41% in 2024, continuing to be the most attacked service type.

- Remote management protocols (RDP, VNC, SSH, Telnet) increased from 26% in 2023 to 33% this year.
- Remote storage protocols (SMB, FTP) remained relatively stable at 19%.
- Networking protocols (DNS, DHCP, CWMP/TR-069) decreased from 10% to 3%.
- Database services decreased from 6% to 1%.
- E-mail services remained unchanged at less than 1%.

**Fact**: Web applications are, without a doubt, the most attacked service type, continuing the trend from 2023.

**Insight for Defenders**: Ensure that defenses, such as web application firewalls, are in place to detect and prevent attacks such as command injections, cross-site scripting and SQL injections as early as possible.

### 2.4. Weak Credentials – a Return to Generic Usernames
![Figure 4 – Top abused credentials]

Figure 4 shows the most abused credentials. Generic usernames include “root,” “admin,” “user,” “guest” and several other such credentials. The increase from 85% in 2023 to 95% in 2024 shows that attackers are again relying more heavily on brute-forcing and simple dictionary attacks.

**Fact**: Best practices for credential management are crucial to prevent attacks leveraging weak credentials.

**Insight for Defenders**: NIST released an updated version of its digital identity guidelines in August 2024 that challenges some long-held assumptions in the cybersecurity community about password complexity and the need for periodic changes.

### 2.5. Exploits – There’s Still Much Beyond KEV
![Figure 5 – Vulnerabilities exploited during the study period]

Exploit attempts against web servers and applications have been on a steady rise since 2022, reaching 56% in 2024. Exploits against network infrastructure devices increased to 14%.

The percentage of exploited vulnerabilities not in CISA’s Known Exploited Vulnerabilities (KEV) increased from 65% to 73%.

| Vendor | Products | CVEs |
| :--- | :--- | :--- |
| Apsystems | Altenergy Power Control Software | CVE-2023-28343 |
| Carel | pCOWeb | CVE-2019-11370 |
| CHIYU Technology | CHIYU BF-430, BF-431 and BF-450M | CVE-2021-31250 |
| CONTEC | SolarView Compact | CVE-2023-23333, CVE-2022-29303, CVE-2022-40881, CVE-2023-29919 |
| Eaton | Intelligent Power Manager | CVE-2018-12031 |
| Emerson | Building Automation System | CVE-2021-41293 |
| Emerson | Dixell XWEB-500 | CVE-2021-45420 |
| Endress+Hauser | WirelessHART Fieldgate SWG70 | CVE-2018-16059 |
| frangoteam | FUXA | CVE-2023-33831 |
| Honeywell | Honeywell PM43 | CVE-2023-3710 |
| KevinLAB | Building Energy Management System | CVE-2021-37291 |
| Linear | eMerge | CVE-2019-7254, CVE-2019-7256, CVE-2022-46381 |
| Loytec | LGATE-902 | CVE-2018-14918 |
| Open Automation Software | OAS Platform | CVE-2022-26833 |
| Schneider Electric | EVlink City, Parking and Smart Wallbox | CVE-2021-22707 |
| Schneider Electric | SpaceLogic C-Bus Home Controller | CVE-2022-34753 |
| Teltonika | Teltonika RUT9XX series | CVE-2018-17532 |
| Viessman | Vitogate 300 BN/MB | CVE-2023-45852 |
| WAGO | WAGO products (multiple) | CVE-2023-1698 |
| ZKTeco | ZKTeco ZEM500-510-560-760, ZEM600-800, ZEM720, ZMM | CVE-2022-42953 |

**Insight for defenders**: Blocking communications simply by country of origin is not effective. Knowing what their goals are and what industries they are attacking can help to prioritize strategic security investments.

### 2.6. OT Attacks – Increased Focus on Building Automation
![Figure 6 – Attacks against OT protocols]

Figure 6 shows the distribution of attacks targeting OT protocols:
1. Modbus: 40%
2. EtherNet/IP: 28%
3. Step7: 8%
4. DNP3: 8%
5. BACnet: 7%

The most relevant increase is in the building automation category.

**Fact**: Monitoring the traffic to and from OT devices is now as critical as monitoring IT traffic.

**Insight for defenders**: Attackers are constantly probing OT/ICS assets for weaknesses. Many organizations will be blind to them because they do not have visibility into their OT/IoT infrastructure.

### 2.7. Attacker Actions/TTPs – the Rise of Discovery
![Figure 7 – Top executed commands]

Figure 7 shows the distribution of top 10 commands executed after initial access:
- **TA0007 – Discovery**: 84% of post-exploitation activities.
- **TA0003 – Persistence**: 12% of observed commands.
- **TA0002 – Execution**: 4% of observed commands.

**Fact**: An increase in discovery actions means attackers are spending more time interacting with a breached system before moving on to other targets.

**Insight for Defenders**: More time spent on discovery creates new opportunities for detection before more damaging actions are taken on a device.

### 2.8. Malware – Botnets Again at the Top
![Figure 8 – Distribution of observed malware samples and C2 servers]

Botnets are at the top, followed by infostealers and RATs. 5 of the most popular malware families of 2024 were not in the 2023 list: Lumma, Gafgyt, Healer, Credential Flusher, and Remcos.

**Fact**: Although individual malware samples and families evolve every day, the basic nature of malware remains unchanged.

**Insight for defenders**: It is much more productive for defenders to detect and hunt for TTPs and anomalous behavior than to rely solely on file hashes and C2 IPs which change constantly.

### 2.9. Threat Actors – More Conflicts Bring More Threat Actors to the Scene
![Figure 9 – Distribution of threat actors]

We maintain a database of more than 800 threat actors:
- Cybercriminals: 45%
- State-sponsored actors: 48%
- Hacktivists: 7%

The increase in state-sponsored actors is a reflection of the increasing number and complexity of geopolitical conflicts.

**Insight for defenders**: Blocking communications simply by country of origin is not effective. Knowing what their goals are and what industries they are attacking can help to prioritize strategic security investments.

---

## 3. Evolution of Attacks on Critical Infrastructure

### 3.1. Who Is Being Attacked?
![Figure 10 – Incidents per year on the EuRepoC database]
![Figure 11 – CI incidents per country]
![Figure 12 – CI incidents per sector]

The total number of incidents increased by 12% from 2023 to 2024. Healthcare was the sector with most incidents (17%), followed by financial services (17%).

### 3.2. Who Is Attacking?
![Figure 13 – Vertical industry data]

The number of threat actors between 2023 and 2024 has increased the most in energy (93%), manufacturing (71%) and healthcare (55%). Spearphishing Link (T1566.002) is still the preferred initial access technique.

---

## 4. Conclusion
In this report, we analyzed data relating to the attacks, exploits, malware, and threat actors we observed in 2024. We recommend organizations focus on three key pillars of cybersecurity:

- **Risk & Exposure Management**: Identify every asset, change default credentials, disable unused services, and patch vulnerabilities.
- **Network Security**: Do not expose unmanaged devices directly to the internet. Segment networks to isolate IT, IoT and OT devices.
- **Threat Detection & Response**: Use an IoT/OT-aware, DPI-capable monitoring solution to alert on malicious indicators and behaviors.

© 2025 Forescout Technologies, Inc. All rights reserved.