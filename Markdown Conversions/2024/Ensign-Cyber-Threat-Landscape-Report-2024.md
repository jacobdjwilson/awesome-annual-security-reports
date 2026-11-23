# ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024

**Version 1.4 | 10 May 2024**

---

## Table of Contents
- [Editor’s Foreword](#editors-foreword)
- [About Ensign InfoSecurity](#about-ensign-infosecurity)
- [Document Table of Contents](#document-table-of-contents)
- [1. Executive Summary](#1-executive-summary)
  - [Executive Summary Narrative](#executive-summary-narrative)
  - [Key Findings Overview](#key-findings-overview)
  - [Escalating Threats](#escalating-threats)
  - [Evolving Attacks](#evolving-attacks)
  - [Emerging Rules](#emerging-rules)
  - [Conclusion](#conclusion)
- [2. Territorial Insights](#2-territorial-insights)
  - [Overview of Territorial Insights](#overview-of-territorial-insights)
  - [Dwell Time Analysis](#dwell-time-analysis)
  - [Top Targeted Industry Groups Across Territories](#top-targeted-industry-groups-across-territories)
  - [Top MITRE ATT&CK Techniques Across Territories](#top-mitre-attck-techniques-across-territories)
  - [Top Cyber-Attack Effects Across Territories](#top-cyber-attack-effects-across-territories)
  - [Threat Group Matrix by Territory](#threat-group-matrix-by-territory)
  - [Top Active Ransomware Groups Observed in the Territories in 2023](#top-active-ransomware-groups-observed-in-the-territories-in-2023)
  - [Top Active Initial Access Brokers Observed in the Territories](#top-active-initial-access-brokers-observed-in-the-territories)
  - [Singapore](#singapore)
  - [Malaysia](#malaysia)
  - [Indonesia](#indonesia)
  - [South Korea](#south-korea)
  - [Australia](#australia)

---

## Editor’s Foreword

Cybersecurity remains one of the most pressing challenges facing nations, organisations, and even individuals.

Ensign InfoSecurity is dedicated to supporting the cybersecurity needs of a wide variety of clients. We publish this report to share our unique insights and perspectives into threats, trends, and topics with business leaders and cybersecurity professionals.

As Ensign continues to grow our operational presence overseas, this year’s report features coverage of Singapore, Malaysia, Indonesia, South Korea, and our recent expansions in Australia and the Greater China Region (Hong Kong S.A.R. and mainland China). We also bring our cybersecurity expertise, experience, and unique Asia-first lens on cybersecurity challenges to global platforms that we participate in, to help shape global discussions.

We believe in using a Threat-Informed Defence approach. Our Ensign Threat Classification Matrix for identified threat groups helps organisations to prioritise their cyber defences against the territory-contextualised threats. We provide the MITRE ATT&CK heatmaps to support organisations in prioritising their cyber defences against specific adversary techniques and follow-through defensive actions, such as threat hunting, Red Teaming, and tuning of detection rules. We have also laid out the observed top targeted industry groups and top exploited vulnerabilities.

With every case our incident response team handles, we learn a little more about how attackers operate. They are evolving to find gaps in our processes, in addition to pushing harder on the weaknesses in our systems and people. While we design, build, and operate a variety of protective systems for organisations, we also advise our clients that resilience, not just building higher defensive walls, should be the objective towards sustainable and predictable defence outcomes.

We are seeing first-hand how cybersecurity and the foundations of digital trust are being tested by the exploitation of Artificial Intelligence (AI) among threat actors. Our researchers are investigating how they use AI to accelerate malware and exploit development, or evade detection. AI is being extensively used in influence operations through Misinformation, Disinformation, and Malinformation (MDM), which distort reality, especially amidst a cyber crisis. We study these threats and trends to advise clients on how to deal with the risks of emerging technologies.

Our continued investment and contribution towards sharing our insights are aimed at enabling companies to better defend against the threats relevant to them. Companies cannot choose whether they become targets, but they can decide how they respond to a cyber-attack, and whether they can recover smoothly and with predictable outcomes.

---

## About Ensign InfoSecurity

Ensign InfoSecurity is the largest comprehensive cybersecurity service provider in Asia. Headquartered in Singapore, Ensign offers bespoke solutions and services to address our clients’ cybersecurity needs. Our core competencies are in the provision of cybersecurity advisory and assurance services, architecture design and systems integration services, and managed security services for advanced threat detection, threat hunting, and incident response. Underpinning these competencies is our in-house cybersecurity research and development team. Ensign has two decades of proven track record as a trusted and relevant service provider, serving clients from the public and private sectors in the Asia-Pacific region.

For more information, visit www.ensigninfosecurity.com.

---

## Document Table of Contents

1. **Executive Summary** ………………………………………………………………………………………………………………………………………………………… 4
2. **Territorial Insights** …………………………………………………………………………………………………………………………………………………………... 7  
   a) Overview  
   b) Singapore  
   c) Malaysia  
   d) Indonesia  
   e) South Korea  
   f) Australia  
   g) Greater China Region  
3. **Top Threat Trends 2023** …………………………………………………………………………………………………………………………………………………… 30
4. **Topical Insights for 2023** …………………………………………………………………………………………………………………………………………………. 32  
   a. Escalating Threats  
      i. Ransomware, Evolved: Shift in Extortion Techniques  
      ii. Hacktivists, Unite: Increasing Sophistication of Cause-aligned Groups  
   b. Evolving Attacks  
      i. Digital Infrastructure Under Fire: Threats Across the Cyber Supply Chain  
   c. Emerging Rules  
      i. Digital Sheriffs: New Regulatory and Policy Initiatives that Aim to Address Risks of Emerging Technology  
      ii. Disclosure Revelations: How Mandatory Incident Reporting is Shining a Light on Corporate Cyber Impact  
5. **Outlook of Cyber Threats for 2024** ………………………………………………………………………………………………………………………………….. 57  
   a. Influential Attackers: Will AI-powered Information Campaigns Shape Election Outcomes and Dismantle Digital Trust?  
   b. Securing AI: Will We Overcome the Vexing Dilemma of Imposing Rules on Probabilistic Systems?  
   c. Scary AI: The Malicious Use of AI will Make Old Attacks Better, but will They Create New Attacks?  
   d. Technology Bifurcation: Managing Supply Chain Risks, but at the Risk of Destabilizing the Internet?  
6. **Defensive Actions for Cyber Defenders and Leaders** ……………………………………………………………………………………………………….. 72
7. **Contributors** ………………………………………………………………………………………………………………………………………………………………... 78
8. **Appendices** …………………………………………………………………………………………………………………………………………………………………. 80

---

# 1. Executive Summary

## Executive Summary Narrative

Cybersecurity continues to be a critical challenge faced by nations, organisations, and individuals. To effectively defend against cyber threats requires, business leaders and cyber professionals must remain informed about the latest threats, risks, and challenges. This year’s report offers increased coverage, due to the expansion of our operational footprint, and deeper analysis attributed to the quality of our data and intelligence sources. These enhancements enable us to provide unique insights and observations for 2023, and forecasts for 2024.

### Territorial Insights
In our analysis of the different territories Ensign operates in, we observed unique difference in each of them. The most targeted industry groups across our territories were Technology, Media and Telecommunications (TMT), Government, Manufacturing, and Financial Services. We continued to observe both state-sponsored threat groups and organised crime groups (notably those which exploit through deployment of Ransomware) in the region. Ransomware remains the dominant threat in nearly every territory we studied. Additionally, we observed a rise in hacktivism (malicious cyber activity motivated by a cause) associated with the spillover effects from the Israel-Hamas conflict, and the normalisation of such activities during the Russia-Ukraine conflict.

---

## Key Findings Overview

### Top Hacktivist Groups
- Bjorka
- DragonForce Malaysia
- SynixCyberCrimMY
- GhostSec
- Muslim Cyber Army
- VulzSec
- Ganosec Team

### Top Ransomware Groups
- ALPHV / BlackCat
- FIN11
- LockBit Gang

### Top Initial Access Brokers
- APT-C-01 (Poison Ivy)
- BITTER
- Scattered Spider
- UNC5221

### Top Surveillance-oriented Groups
- Kimsuky
- Poison Carp

### Top Commonly Used Solutions with Notable Vulnerabilities
- MOVEit Managed File Transfer (MFT) software
- Citrix NetScaler ADC and Gateway
- Confluence Server and Datacentre
- Zoho ManageEngine
- 3CX Desktop Application
- GoAnywhere MFT
- Ivanti Connect Secure VPN
- PaperCut Application Server
- Veeam Backup & Replication

---

## Escalating Threats

Our active involvement in international platforms like the United Nations (UN), World Economic Forum (WEF), and Geneva Dialogue, allows us to understand the spillover effects of geopolitics into the cyber domain. While malicious activity directly related to the Russia-Ukraine conflict may have dwindled, an uptick in Hamas-Israel hacktivism has filled the void. Additionally, tech bifurcation remains another geopolitically charged issue, complicating procurement decisions in the short term (especially as some countries implement bans on companies using software or hardware from other countries), and possibly worsening cybersecurity for all in the longer term.

We are seeing first-hand how cybersecurity and digital trust is being transformed by Artificial Intelligence (AI) — whether it is infused in our own tools, discovered in a weaponised form through our threat research, or through our expert policy development and advisory guidance to organisations. While Generative AI-driven scams and phishing emails troubled our systems in 2023, 2024 will see a spike in Misinformation, Disinformation, and Malinformation (MDM) amidst an election-filled year around the world. Reality can also be distorted by ruthless attackers, especially amidst a cyber crisis.

## Evolving Attacks

With every case our incident response team handles, we learn a little more about how attackers operate. Attackers are exploiting weaknesses in our cyber processes to evade detection; instead of getting in through the “high severity” vulnerabilities that companies tend to patch quickly and monitor closely, they use “low” risk vulnerabilities that are de-prioritised for patching for weeks. Rather than bring in hefty payloads that might trigger detection rules, they have developed sophisticated “living off the land” techniques to stay below the radar.

Supply chain risks and sophisticated attacks also make it harder to defend every threat vector. Attackers are compromising critical nodes in common commercial network hardware, making defences even harder.

Companies cannot control whether they become targets, but they can prepare how to respond to cyber-attacks and take practical steps to recover smoothly with minimal damage.

## Emerging Rules

In the ever-evolving landscape of cybersecurity, it is paramount for new regulations and policies to be aimed at enhancing data protection, fortifying the security of critical systems, and strengthening digital infrastructure. Many countries are introducing or enhancing cyber and data legislation (some with politicised motives).

While we design, build, and operate a variety of protective systems for organisations, we also advise our clients that resilience, not just building higher defensive walls, should be the objective beyond a certain point.

## Conclusion

Whether you sit at the technical-operational layer, the executive layer, or the board oversight/governance layer, the challenges of navigating the complexities of cybersecurity are significant. In this regard, implementing new regulatory frameworks and policy initiatives will play an instrumental role in building our defences against cyber threats.

Hopefully, the insights and analysis in our report can help you make more informed decisions about what is best for your needs. Ensign stands ready to protect your organisation’s digital journey from the ever-expanding array of threats and risks.

---

# 2. Territorial Insights

## Overview of Territorial Insights

Ensign’s regional offices (Singapore, Malaysia, Indonesia, South Korea, and now Australia and the Greater China Region) are situated in locations within the Asia-Pacific region with high cyber activities, charged by geopolitical tensions (e.g. US-China tensions, South China Sea disagreements, and China-Taiwan tensions), and uneven (but generally growing) economies. Across these territories, Ensign continues to observe increased digitalisation efforts and the use of a wide range of hardware and software solutions, adding to the complexity in managing the cybersecurity risks in the digital attack surface.

Ransomware continues to be lucrative for the threat groups (and the most prominent threat across most regions), not only as a financial gain tool, but due to the sustained investments by cyber weapons developers, become a useful and effective cyber weapon to cause pain to targeted organisations. The most active Ransomware groups observed across the territories include, ALPHV, BlackCat Gang, FIN11, and LockBit Gang.

While we observed both state-sponsored threat groups and organised crime groups active in the region, we also saw rising activities associated with hacktivism due to spillover effects from the Israel-Hamas conflict occurring from the end of 2023. This has generally led to rising partisan collective groups taking actions into their own hands for the ideological causes. Notable hacktivist groups observed active in our region included Bjorka, DragonForce Malaysia, SynixCyberCrimMY, GhostSec, Muslim Cyber Army, VulzSec and Ganosec Team. The challenge in addressing hacktivism stems from their lack of a definitive structure and unique processes and procedures for each group. Instead, individuals involved in adversarial actions leverage their individual competencies and capabilities to further their cause. While organisations who do well in addressing cyber hygiene measures are generally resilient against hacktivist threats, the level of sophistication and effects are also rising. These groups have been observed to perform not just the distributed denial-of-service (DDoS) attacks and website defacements, but now, with the accessibility to offensive services (e.g. Ransomware as a Service), some attacks are inflicting greater harm to organisations when these attacks breach the defences.

Aside from hacktivism, Ensign has seen sustained activities from initial access brokers active in the territories, who have not only been successful in obtaining and selling access to organisations, but also due to rising Law enforcement activities targeting the Ransomware operators, started to opportunistically exfiltrate and sell the victim’s data even before sale of access. This has led to some cyber-attack campaigns having lost the adversaries’ element of surprise due to lack of operational security (OpsSec). Active initial access brokers (IABs) observed across the territories include APT-C-01 (Poison Ivy), BITTER, Scattered Spider, and UNC5221. IABs such as Scattered Spider are known to obtain financial gain through sale of access and opportunistically sell data obtained during acquisition of access.

Aside from initial access brokers and Ransomware groups, 2023 saw 21 threat groups actively targeting the Ensign operating territories. There are more state-sponsored threat groups (16) than organised crime groups (5) observed. Russian-associated threat groups, APT28, FIN7, and Turla, are representative groups that have returned to target the Ensign operating territories. GambleForce and Lazarus Group were observed to have targeted all Ensign’s operating territories.

The five organised crime groups observed across the territories, aside from the aforementioned Ransomware Groups and Initial Access Brokers, are Carderbee, Desorden, FIN7, Patchwork, and Poison Carp. Malaysia and Indonesia generally shared the same threat groups, with the exception of Desorden which continued its targeting of Malaysia, and Turla which targeted Indonesia.

Due to the aforementioned tensions across the territories, there are more threat groups observed to be motivated by surveillance, information theft and espionage. Particularly on surveillance of populations, we noted that Kimsuky and Poison Carp are threat groups which target mobile devices for surveillance outcomes with the harvesting of personal data and information.

Attacks on network equipment with significant impact were seen across territories. The stealthy and persistent effects of breaches performed by Volt Typhoon were prominent, especially with their KV-Botnet to compromise long-term unpatched and end-of-life networking products (such as Netgear ProSAFE routers, CISCO RV 320/325 routers, Draytek Vigor routers, and AXIS IP cameras). Some of these devices are installed in the operational technology (OT) environment or next-to-OT environments (possibly affecting essential services and other OT-centric businesses such as manufacturing) in territories such as Singapore, Malaysia, Indonesia, and Australia.

Cyber supply chain attacks have also manifested in a big way across the territories in 2023, causing some big brands / organisations to be breached. Notably, cyber-attacks exploiting vulnerabilities are found in commonly used commercial off the shelf (COTS) solutions such as MOVEit Managed File Transfer (MFT) software, Citrix NetScaler ADC and Gateway, Confluence Server and Data Center, Zoho ManageEngine, 3CX Desktop Application, GoAnywhere MFT, Ivanti Connect Secure VPN, PaperCut Application Server, Veeam Backup & Replication, and others.

Based on our incident responses, Ensign noted that the minimum Dwell time increased compared to 2022 (0 days). This could be attributed to the increasing technology sprawl as organisations work through technology refresh and the continued use of Cloud-based services. The maximum Dwell time decreased significantly from 1,095 days to 49 days. This is encouraging as it indicates that organisations may be increasing their detection capabilities. Contrasting the average Dwell time observed from 2022, there has also been a decrease to 5 days for Retail, 22 days for TMT, and 33 days for Others, observed this year (last year we observed the average of 71 days average Dwell time for Transport sector and 83 days for Others).

---

## Dwell Time Analysis

| Industry Group | Average Dwell (Days) | Min. (Days) | Max. (Days) |
| :--- | :--- | :--- | :--- |
| **Retail** | 5 | 3 | 12 |
| **Technology, Media and Telecommunications (TMT)** | 22 | 12 | 49 |
| **Others** | 33 | 19 | 43 |

---

## Top Targeted Industry Groups Across Territories

| Territory | Ranked Top Targeted Industry Groups |
| :--- | :--- |
| **SG (Singapore)** | Manufacturing, Professional services, TMT, Financial services, Real estate |
| **MY (Malaysia)** | Manufacturing, Government, TMT, Professional services, Retail |
| **ID (Indonesia)** | TMT, Financial services, Government, Energy, Manufacturing |
| **SK (South Korea)** | Government, TMT, Manufacturing, Defence, Financial services |
| **AU (Australia)** | TMT, Engineering & construction, Retail, Government, Financial services |
| **GCR (Greater China Region)** | TMT, Manufacturing, Healthcare, Professional services, Financial Services |

The most common industry groups were **Technology, Media and Telecommunications (TMT)**, **Government**, **Financial Services**, and **Manufacturing**.

- **Technology, Media and Telecommunications (TMT)** was the top industry group targeted across all the territories. This is attributed to the increased levels of digitalisation post-pandemic and the push for greater productivity through exploitation of higher network bandwidth, AI and automation as well as the push for digital payments and digital trade systems across ASEAN and the Asia Pacific region.
- **Government** was observed to be targeted across Malaysia, Indonesia, South Korea, Australia and the Greater China Region. We attribute this to political events such as elections or geopolitical matters such as the US-China tensions.
- **Financial Services** was observed to be targeted across Singapore, Indonesia, South Korea, Australia and the Greater China Region. We attribute this to the natural concentration of personal data, which is useful for espionage and surveillance related activities, as well as access to funds, especially through cryptocurrency wallets and brokerage accounts.
- **Manufacturing** was observed to be targeted across Singapore, Malaysia, Indonesia and South Korea. With the rebalancing of manufacturing capacity due to “de-risking” efforts between US and China, Southeast Asian countries and allies of US (i.e. South Korea) benefits from ramped up manufacturing demand which is progressively driving the economic growth post-pandemic. Industrial espionage is also a common reason why threat actors are interested in this industry group. The threat actors typically target the trade secrets and industrial designs, including business relationships and contracts. Additionally, some threat actors are interested in having the capability to cause disruption to the supply chain by targeting the companies in this industry group.

---

## Top MITRE ATT&CK Techniques Across Territories

Our analysis of the top techniques observed saw **T1110: Brute Force** common across Singapore, Malaysia & Indonesia and the Greater China Region. Amongst others, **T1595: Active Scanning** and **T1078: Valid Accounts** were observed across Singapore, Malaysia & Indonesia. **T1071: Application Layer Protocol** was observed across Singapore and the Greater China Region.

| Territory | Observed Key Techniques |
| :--- | :--- |
| **SG** | T1110: Brute Force, T1595: Active Scanning, T1078: Valid Accounts, T1071: Application Layer Protocol |
| **MY & ID** | T1110: Brute Force, T1595: Active Scanning, T1098: Account Manipulation, T1078: Valid Accounts |
| **GCR** | T1110: Brute Force, T1059: Command and Scripting Interpreter, T1566: Phishing, T1071: Application Layer Protocol |

> *Note: Full versions of the techniques heatmaps can be found in Appendix A with links to download MITRE ATT&CK Navigator JSON files for further review, and top tactics can be found in Appendix C. Full versions of the vulnerabilities observed in the territories can be found in Appendix B.*

---

## Top Cyber-Attack Effects Across Territories

The cyber-attack effects observed across the territories saw **Ransom** observed across all territories. Next most common cyber-attack effect was **Sale of Access**, followed by **Sale of Data**, **Data Leak** and **Denial of Service**.

| Territory | Observed Cyber-Attack Effects (in order of prevalence) |
| :--- | :--- |
| **SG** | Ransom, Sale of Access, Sale of Data |
| **MY** | Ransom, Sale of Access, Data Leak |
| **ID** | Ransom, Sale of Access, Sale of Data |
| **SK** | Data Leak, Denial of Service, Ransom |
| **AU** | Ransom, Data Leak, Denial of Service |
| **GCR** | Ransom, Sale of Access, Sale of Data |

---

## Threat Group Matrix by Territory

| Threat Group | Profile | Motivation | Associated Territory | SG | MY | ID | SK | AU | GCR |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **APT28** | State-sponsored | Information theft and espionage | Russia | ● | ● | ● | ● | ● | |
| **APT33** | State-sponsored | Information theft and espionage; Sabotage and destruction; Financial crime | Iran | ● | ● | ● | ● | ● | |
| **APT37** | State-sponsored | Information theft and espionage | North Korea | | | | ● | | ● |
| **APT38** | State-sponsored | Financial crime | North Korea | ● | ● | ● | ● | | |
| **APT41** | State-sponsored | Information theft and espionage; Financial crime | Greater China Region | | ● | ● | ● | ● | ● |
| **APT43** | State-sponsored | Financial gain | North Korea | | | | | | ● |
| **BlackTech** | State-sponsored | Information theft and espionage | Greater China Region | | | | | | ● |
| **Carderbee** | Organised Crime | Information theft and espionage | Greater China Region | | | | | | ● |
| **Dark Pink** | State-sponsored | Information theft and espionage | Vietnam | ● | ● | ● | | | |
| **Darkhotel** | State-sponsored | Information theft and espionage | South Korea | | | | | | ● |
| **Desorden** | Organised Crime | Financial gain | Unknown | | ● | | | | |
| **Earth Longzhi** | State-sponsored | Information theft and espionage | Greater China Region | | ● | ● | | | ● |
| **FIN7** | Organised Crime | Financial crime | Russia | | | | | ● | ● |
| **GambleForce** | State-sponsored | Information theft and espionage | Greater China Region | ● | ● | ● | ● | ● | ● |
| **Kimsuky** | State-sponsored | Information theft and espionage | North Korea | | | | ● | | ● |
| **Lazarus Group** | State-sponsored | Financial crime; Information theft and espionage; Sabotage and destruction | North Korea | ● | ● | ● | ● | ● | ● |
| **Patchwork** | Organised Crime | Information theft and espionage | India | | | | | | ● |
| **Poison Carp** | Organised Crime | Information theft and espionage | Greater China Region | | | | | ● | ● |
| **Tonto Team** | State-sponsored | Information theft and espionage | Greater China Region | | | | ● | | |
| **Turla** | State-sponsored | Information theft and espionage | Russia | | | ● | | ● | |
| **Volt Typhoon** | State-sponsored | Information theft and espionage | Greater China Region | | | | | ● | |
| **Total** | | | | **6** | **9** | **8** | **9** | **9** | **14** |

---

## Top Active Ransomware Groups Observed in the Territories in 2023

ALPHV, FIN11, and LockBit Gang were collectively the three most active Ransomware Groups observed in the territories in 2023. All were organised crime groups which ran “professional” operations, using updated capabilities with multi-extortion tactics.

| Attribute | ALPHV, BlackCat Gang | FIN11 | LockBit Gang |
| :--- | :--- | :--- | :--- |
| **Associated Territory** | Unknown | Unknown | Unknown |
| **Threat Actor Profile** | Organised Crime | Organised Crime | Organised Crime |
| **Motivation** | Financial gain | Financial gain | Financial gain |
| **Notable Characteristics** | ▪ ALPHV Ransomware Operator<br>▪ Managed leak-site<br>▪ Multi-extortion tactics, including:<br>&nbsp;&nbsp;▪ Disclosure to public<br>&nbsp;&nbsp;▪ Sale of data<br>&nbsp;&nbsp;▪ Reporting to regulator | ▪ Cl0p Ransomware Operator<br>▪ Managed leak-site<br>▪ Multi-extortion tactics, including:<br>&nbsp;&nbsp;▪ Disclosure to public<br>&nbsp;&nbsp;▪ Sale of data<br>▪ Exploited the MOVEit 0day vulnerability (CVE-2023-34362) and GoAnywhere 0day vulnerability (CVE-2023-0669) for Initial Access | ▪ LockBit 3.0 Ransomware Operator<br>▪ Managed leak-site<br>▪ Multi-extortion tactics, including:<br>&nbsp;&nbsp;▪ Disclosure to public<br>&nbsp;&nbsp;▪ Sale of data<br>▪ Coordinates different adversary talents and capabilities |
| **Publicly Known Victims (Non-exhaustive)** | **Singapore**<br>▪ Fu Yu Corporation<br><br>**Malaysia**<br>▪ Agensi Kaunseling dan Pengurusan Kredit (AKPK)<br>▪ Vopack Malaysia<br><br>**Australia**<br>▪ HWL Ebsworth<br>▪ TissuPath | **Australia**<br>▪ Aristocrat Leisure Limited<br>▪ BG Group Australia (member of Shell Group of companies)<br>▪ Crown Resorts<br>▪ Fortescue Metals | **Singapore**<br>▪ Academy of Medicine<br><br>**Indonesia**<br>▪ Bank Syariah Indonesia (BSI)<br><br>**South Korea**<br>▪ Hanwha Group<br><br>**Australia**<br>▪ Q Automotive Group |

### Techniques of Concern (MITRE ATT&CK v15)
- **TA0001: Initial Access**
  - T1078: Valid Accounts
  - T1189: Drive-by Compromise
  - T1133: External Remote Services
  - T1566: Phishing
- **TA0010: Exfiltration**
  - T1567: Exfiltration Over Web Service
- **TA0040: Impact**
  - T1486: Data Encrypted for Impact
  - T1489: Service Stop
  - T1485: Data Destruction
  - T1491: Defacement

---

## Top Active Initial Access Brokers Observed in the Territories

APT-C-01 (Poison Ivy), BITTER, Scattered Spider, and UNC5221 were the four most active initial access brokers observed in the territories in 2023. All operated as “mercenaries for hire” in providing access to targets / victims.

Notably, Scattered Spider is the only threat group motivated by financial gain with sales of exfiltrated data aside from access to targets / victims.

| Attribute | APT-C-01 (Poison Ivy) | BITTER | Scattered Spider | UNC5221 |
| :--- | :--- | :--- | :--- | :--- |
| **Associated Territory** | Greater China Region | Unknown | Unknown | Unknown |
| **Threat Actor Profile** | State-sponsored | Organised Crime | Organised Crime | Organised Crime |
| **Motivation** | Information theft and espionage | Information theft and espionage | Financial gain | Information theft and espionage |
| **Notable Characteristics** | Predominantly used Phishing and exploits 0day vulnerabilities. | Performed Phishing using malicious CHM file attachments. | Performed social engineering for identity compromise on Okta related identity compromise via cross tenant impersonation.<br><br>*Scattered Spider observed to opportunistically sell obtained information (during initial access) for financial gain, aside from selling initial access.* | Exploited (CVE-2023-46805) Ivanti Connect Secure VPN vulnerability for authentication bypass. |
| **Targeted Territories** | Singapore, Malaysia, Indonesia, South Korea, Greater China Region | Singapore, Malaysia, Indonesia, South Korea, Greater China Region | Australia, Greater China Region | Australia, Greater China Region |

### Techniques of Concern (MITRE ATT&CK v15)
- **TA0001: Initial Access**
  - T1566: Phishing
  - T1133: External Remote Services
  - T1078: Valid Accounts
- **TA0011: Command and Control**
  - T1090: Proxy
  - T1568: Dynamic Resolution
  - T1095: Non-Application Layer Protocol
  - T1571: Non-Standard Port
  - T1572: Protocol Tunneling
  - T1102: Web Service
- **TA0010: Exfiltration**
  - T1041: Exfiltration Over C2 Channel
  - T1048: Exfiltration Over Alternative Protocol

---

## Singapore

### Key Analysis Insights

#### Ensign Threat Classification Matrix
- **Insubstantial**: *NIL*
- **Potential**: APT33, APT38, Dark Pink, GambleForce
- **Impending**: *NIL*
- **Material**: APT28, Lazarus Group

*(Assessment progression: Insubstantial → Potential → Impending → Material)*
- **Capability**: ● (Potential), ● (Impending), ● (Material)
- **Intent**: ● (Potential), ● (Impending), ● (Material)
- **Opportunity**: ● (Potential), ● (Impending), ● (Material)

#### Most Affected Industry Groups
*(Based on Ensign Proprietary Data and Cyber Threat Intelligence data)*
1. **Manufacturing** *(New affected industry observed in 2023)*
2. **Professional services** *(New affected industry observed in 2023)*
3. **Technology, media & telecommunications**
4. **Financial services**
5. **Real estate** *(New affected industry observed in 2023)*

#### Top Notable Cyber-Attack Effects Observed
- **Ransom**: 52.9%
- **Sale of Access**: 41.2%
- **Sale of Data**: 2%

#### Techniques of Concern (MITRE ATT&CK v15)
- **TA0001: Initial Access**
  - T1566: Phishing
  - T1189: Drive-by Compromise
  - T1078: Valid Accounts
  - T1091: Replication Through Removable Media
  - T1133: External Remote Services
  - T1199: Trusted Relationship
- **TA0011: Command and Control**
  - T1132: Data Encoding
  - T1001: Data Obfuscation
  - T1571: Non-Standard Port
  - T1102: Web Service
  - T1092: Communication Through Removable Media
  - T1008: Fallback Channels
  - T1104: Multi-Stage Channels
- **TA0010: Exfiltration**
  - T1048: Exfiltration Over Alternative Protocol
  - T1041: Exfiltration Over C2 Channel
  - T1567: Exfiltration Over Web Service
  - T1030: Data Transfer Size Limits
- **TA0040: Impact**
  - T1565: Data Manipulation
  - T1485: Data Destruction
  - T1561: Disk Wipe
  - T1529: System Shutdown/Reboot
  - T1486: Data Encrypted for Impact
  - T1491: Defacement
  - T1498: Network Denial of Service
  - T1489: Service Stop

### Singapore Territorial Analysis

In addition to initial access brokers and Ransomware groups, Singapore was targeted by six threat groups, all of which are state-sponsored. Our analysis has identified that APT28 and Lazarus Group were the most material threat groups operating within the territory.

The top five industry groups observed to be attacked include: (1) Manufacturing, (2) Professional services, (3) Real estate, (4) Financial services, and (5) Technology, media and telecommunications (TMT). Financial services and TMT continue to remain in the top targeted industry groups following last year’s report. New entrants to the list include Manufacturing, Real estate, and Professional services, likely due to their lower cyber maturity level and less stringent cyber regulatory regimes.

The top cyber-attack effects observed were (1) ransom, (2) sale of access, and (3) sale of data. Correlating both the targeted industry groups and the top cyber-attack effects, it is possible that ransoms were made to capitalise on the businesses supporting post-pandemic economic recovery. The sale of access and the sale of data indicated continued interest to gain a foothold into businesses based in Singapore, many of which support larger companies (e.g. MNCs with regional HQs in Singapore) and essential services, as well as providing trusted access into other connected entities in the supply chain. Considering that Singapore is a trusted processor of data for many companies, the value of data handled in Singapore remains high, and obtaining such data can support further espionage activities or specific targeting.

Being a location with a highly digital-enabled environment through smart-nation initiatives, high concentration of data centres, and high throughput access to international Internet links, Singapore continues to be attractive to threat actors as a launchpad for cyber-attacks and to experiment attacks before launching them on higher sophistication locations.

Combined with the unique set of assets in the digital attack surface, Ensign noted that the following vendors solutions were deliberately exploited in the year:
- 3CX Desktop Application
- Cisco ASA VPN
- Citrix NetScaler ADC and Gateway
- Confluence Server and Data Center
- GoAnywhere MFT
- Ivanti Connect Secure VPN
- JetBrains TeamCity
- Juniper BigIP
- MOVEit Managed File Transfer (MFT) software
- PaperCut Application Server
- Veeam Backup & Replication
- WinRAR
- Zoho ManageEngine

Singapore Exchange (SGX)-listed companies are required to file cyber incident notices. Ensign noted that the following companies filed cybersecurity incident notifications to SGX in 2023:

| Company | Industry Group |
| :--- | :--- |
| **Cortina Holdings** | Retail |
| **GoldHeart** | Retail |
| **Koh Brothers Group Limited** | Engineering and Construction |
| **NetLink NBN Trust** | Technology, media and telecommunications |
| **Procurri Corporation Limited** | Technology, media and telecommunications |

---

## Malaysia

### Key Analysis Insights

#### Ensign Threat Classification Matrix
- **Insubstantial**: *NIL*
- **Potential**: Dark Pink, GambleForce
- **Impending**: APT28, APT33, APT38, Desorden, Earth Longzhi
- **Material**: APT41, Lazarus Group

*(Assessment progression: Insubstantial → Potential → Impending → Material)*
- **Capability**: ● (Potential), ● (Impending), ● (Material)
- **Intent**: ● (Potential), ● (Impending), ● (Material)
- **Opportunity**: ● (Potential), ● (Impending), ● (Material)

#### Most Affected Industry Groups
*(Based on Ensign Proprietary Data and Cyber Threat Intelligence data)*
1. **Manufacturing** *(New affected industry observed in 2023)*
2. **Government** *(New affected industry observed in 2023)*
3. **Technology, media & telecommunications**
4. **Professional Services** *(New affected industry observed in 2023)*
5. **Retail** *(New affected industry observed in 2023)*

#### Top Notable Cyber-Attack Effects Observed
- **Ransom**: 58.2%
- **Sale of Access**: 18.2%
- **Data Leak**: 14.5%

#### Techniques of Concern (MITRE ATT&CK v15)
- **TA0001: Initial Access**
  - T1566: Phishing
  - T1078: Valid Accounts
  - T1189: Drive-by Compromise
  - T1133: External Remote Services
  - T1091: Replication Through Removable Media
  - T1195: Supply Chain Compromise
  - T1199: Trusted Relationship
- **TA0011: Command and Control**
  - T1102: Web Service
  - T1001: Data Obfuscation
  - T1132: Data Encoding
  - T1008: Fallback Channels
  - T1104: Multi-Stage Channels
  - T1571: Non-Standard Port
  - T1090: Proxy
  - T1092: Communication Through Removable Media
  - T1568: Dynamic Resolution
  - T1095: Non-Application Layer Protocol
- **TA0010: Exfiltration**
  - T1048: Exfiltration Over Alternative Protocol
  - T1041: Exfiltration Over C2 Channel
  - T1567: Exfiltration Over Web Service
  - T1030: Data Transfer Size Limits
- **TA0040: Impact**
  - T1565: Data Manipulation
  - T1486: Data Encrypted for Impact
  - T1485: Data Destruction
  - T1561: Disk Wipe
  - T1529: System Shutdown/Reboot
  - T1491: Defacement
  - T1498: Network Denial of Service
  - T1489: Service Stop

### Malaysia Territorial Analysis

Malaysia saw nine threat groups targeting the territory with Desorden, the only organised crime group, aside from the initial access brokers and Ransomware groups. Desorden has continued its campaign of targeting Malaysia and claimed victims Ranhill Utilities Berhad and Bintulu Port Holdings Berhad.

The top five industry groups observed to be attacked include: (1) Manufacturing, (2) Government, (3) Technology, media and telecommunications (TMT), (4) Professional services, and (5) Retail. 2023 saw the inclusion of Manufacturing, Government, Professional services, and Retail.

The top cyber-attack effects observed were (1) ransom, (2) sale of access, and (3) data leak. Correlating both the targeted industry groups and the top cyber-attack effects, it is possible that ransoms targeted businesses supporting post-pandemic economic recovery. The sale of access and the data leak indicated continued interest to gain a foothold into businesses based in Malaysia. However, the nature and publicity around the data leaks could suggest a more nefarious intent to demonstrate cybersecurity weaknesses of businesses in Malaysia rather than to gain a lot financially from sale of the data. This suggests that the value of the data may not be high or that attackers have other objectives.

Malaysia has expressed keen interest to capitalise on the movements by multinational companies to relocate their manufacturing hubs, this is particularly focused on the high technology manufacturing business segment. These cyber-attack effects may be related to the types of companies being attracted to the country, among other factors.

Hacktivism also featured prominently in Malaysia in 2023. DragonForce Malaysia launched a rebranded #OpsPetir campaign replacing the last #OpsBedil in 2022[^1]. The #OpsPetir[^1] was initiated (from 12 April to 21 April) in the wake of the Israel-Hamas conflict which saw initial targeting of government agencies, education institutions, and financial institutions which were overt in their relationships with Israel. This subsequently expanded to other organisations deemed to have expressed support or have relationships with Israel for the conflict. During the campaign, a member of the group launched a denial-of-service tool, CyberTroopers, which was employed during the campaign. It was noted that the python-based tool leveraged ChatGPT[^3] in the development and obfuscation of the program. Notably, DragonForce Malaysia declared the goal of developing itself into a Ransomware group and the use of the leaked LockBit Ransomware source code[^2] were observed in attacks carried out by the group from November 2023 onwards[^2]. This is a significant development in the graduation of DragonForce Malaysia into an organised crime group with ideological motivations[^3].

We noted that the following vendors solutions were deliberately exploited in the year:
- 3CX Desktop Application
- Cisco ASA VPN
- Citrix NetScaler ADC and Gateway
- Confluence Server and Data Center
- GoAnywhere MFT
- Ivanti Connect Secure VPN
- JetBrains TeamCity
- Juniper BigIP
- MOVEit Managed File Transfer (MFT) software
- PaperCut Application Server
- SysAid On-Premise
- Veeam Backup & Replication
- WinRAR
- Zoho ManageEngine

---

## Indonesia

### Key Analysis Insights

#### Ensign Threat Classification Matrix
- **Insubstantial**: *NIL*
- **Potential**: APT33, APT38, Earth Longzhi, Turla
- **Impending**: *NIL*
- **Material**: APT41, Dark Pink, GambleForce, Lazarus Group

*(Assessment progression: Insubstantial → Potential → Impending → Material)*
- **Capability**: ● (Potential), ● (Impending), ● (Material)
- **Intent**: ● (Potential), ● (Impending), ● (Material)
- **Opportunity**: ● (Potential), ● (Impending), ● (Material)

#### Most Affected Industry Groups
*(Based on Ensign Proprietary Data and Cyber Threat Intelligence data)*
1. **Technology, media & telecommunications** *(New affected industry observed in 2023)*
2. **Financial services**
3. **Government**
4. **Energy** *(New affected industry observed in 2023)*
5. **Manufacturing** *(or Food and Beverage)* *(New affected industry observed in 2023)*

#### Top Notable Cyber-Attack Effects Observed
- **Ransom**: 42%
- **Sale of Access**: 38%
- **Sale of Data**: 8%

#### Techniques of Concern (MITRE ATT&CK v15)
- **TA0001: Initial Access**
  - T1566: Phishing
  - T1078: Valid Accounts
  - T1189: Drive-by Compromise
  - T1133: External Remote Services
  - T1091: Replication Through Removable Media
  - T1195: Supply Chain Compromise
- **TA0011: Command and Control**
  - T1102: Web Service
  - T1071: Application Layer Protocol
  - T1090: Proxy
  - T1105: Ingress Tool Transfer
  - T1132: Data Encoding
  - T1001: Data Obfuscation
  - T1008: Fallback Channels
  - T1104: Multi-Stage Channels
  - T1571: Non-Standard Port
  - T1568: Dynamic Resolution
  - T1573: Encrypted Channel
  - T1095: Non-Application Layer Protocol
- **TA0010: Exfiltration**
  - T1048: Exfiltration Over Alternative Protocol
  - T1041: Exfiltration Over C2 Channel
  - T1567: Exfiltration Over Web Service
- **TA0040: Impact**
  - T1565: Data Manipulation
  - T1485: Data Destruction
  - T1486: Data Encrypted for Impact
  - T1561: Disk Wipe
  - T1529: System Shutdown/Reboot
  - T1491: Defacement
  - T1489: Service Stop

### Indonesia Territorial Analysis

Indonesia saw eight threat groups targeting the territory which generally shares the same threat groups as Malaysia. The only difference was the exclusion of Desorden, which dwindled in Indonesia, and the inclusion of Turla for Indonesia, which was not present in Malaysia. This is aside from the initial access brokers and Ransomware groups. Desorden has seemingly discontinued its campaign targeting Indonesian entities in 2023.

The top five industry groups observed to be attacked include: (1) Technology, media and telecommunications (TMT), (2) Financial services, (3) Government, (4) Energy, and (5) Food and Beverage. Ensign sees the inclusion of TMT, Energy, and Food & Beverage in this year’s top targeted industry groups.

The top cyber-attack effects observed were (1) ransom, (2) sale of access, and (3) sale of data. Correlating both the targeted industry groups and the top cyber-attack effects, there is reason to believe that ransoms were made to capitalise on the businesses supporting economic recovery post-pandemic. The sale of access and the sale of data indicated continued interest to gain a foothold into businesses based in Indonesia. Given that Indonesia was the chair of ASEAN in 2023, it is possible that threat actor groups who were uniquely targeting government entities may be conducting espionage and gathering information of political value. The targeting of Energy and Food & Beverage industry groups might have been as an indirect means to feed influence operations oriented towards the 2024 elections.

Indonesia has seen sustained hacktivist activities targeting its entities, most notably Bjorka, which does not seem to have an ideological or political cause but is instead determined to embarrass the Indonesian government and expose their weak cyber and data security practices. In 2023, Bjorka claimed to have attacked BPJS Ketenagakerjaan and PT Telkom Indonesia (Persero) Tbk with the sale of their exfiltrated data.

Ensign noted that the following vendors solutions were deliberately exploited in the year:
- 3CX Desktop Application
- Cisco ASA VPN
- Citrix NetScaler ADC and Gateway
- Confluence Server and Data Center
- GoAnywhere MFT
- Ivanti Connect Secure VPN
- JetBrains TeamCity
- Juniper BigIP
- MOVEit Managed File Transfer (MFT) software
- PaperCut Application Server
- SysAid On-Premise
- Veeam Backup & Replication
- WinRAR
- Zoho ManageEngine

---

## South Korea

### Key Analysis Insights

#### Ensign Threat Classification Matrix
- **Insubstantial**: *NIL*
- **Potential**: APT33
- **Impending**: *NIL*
- **Material**: APT28, APT37, APT38, APT41, GambleForce, Kimsuky, Lazarus Group, Tonto Team

*(Assessment progression: Insubstantial → Potential → Impending → Material)*
- **Capability**: ● (Impending), ● (Impending), ● (Material)
- **Intent**: ● (Potential), ● (Impending), ● (Material)
- **Opportunity**: ● (Potential), ● (Impending), ● (Material)

#### Most Affected Industry Groups
*(Based on Ensign Proprietary Data and Cyber Threat Intelligence data)*
1. **Government**
2. **Technology, media & telecommunications**
3. **Manufacturing**
4. **Financial services**
5. **Defence** *(New affected industry observed in 2023)*

*(Additional observed sectors mentioned in narrative: Research, Education)*

#### Top Notable Cyber-Attack Effects Observed
- **Data Leak**: 31.7%
- **Denial of Service**: 15.9%
- **Ransom**: 13.4%

#### Techniques of Concern (MITRE ATT&CK v15)
- **TA0001: Initial Access**
  - T1566: Phishing
  - T1078: Valid Accounts
  - T1189: Drive-by Compromise
  - T1133: External Remote Services
  - T1190: Exploit Public-Facing Application
  - T1091: Replication Through Removable Media
  - T1199: Trusted Relationship
  - T1195: Supply Chain Compromise
- **TA0011: Command and Control**
  - T1071: Application Layer Protocol
  - T1105: Ingress Tool Transfer
  - T1102: Web Service
  - T1090: Proxy
  - T1001: Data Obfuscation
  - T1573: Encrypted Channel
  - T1092: Communication Through Removable Media
  - T1132: Data Encoding
  - T1008: Fallback Channels
  - T1104: Multi-Stage Channels
  - T1571: Non-Standard Port
  - T1568: Dynamic Resolution
  - T1219: Remote Access Software
- **TA0010: Exfiltration**
  - T1048: Exfiltration Over Alternative Protocol
  - T1567: Exfiltration Over Web Service
  - T1041: Exfiltration Over C2 Channel
  - T1030: Data Transfer Size Limits
- **TA0040: Impact**
  - T1565: Data Manipulation
  - T1561: Disk Wipe
  - T1529: System Shutdown/Reboot
  - T1485: Data Destruction
  - T1486: Data Encrypted for Impact
  - T1498: Network Denial of Service
  - T1491: Defacement
  - T1489: Service Stop

### South Korea Territorial Analysis

South Korea saw nine threat groups targeting the territory, all of which are state-sponsored threat groups, aside from the initial access brokers and Ransomware groups. Without surprise, South Korea has seen continued and dedicated targeting from North Korea-associated threat groups — APT37, APT38, Kimsuky, and Lazarus Group.

The top five industry groups observed to be attacked include: (1) Financial services, (2) Research, (3) Education, (4) Government, and (5) Defence. Ensign saw the inclusion of the Defence industry group in this year’s top targeted industry groups.

The top cyber-attack effects observed were (1) data leak, (2) denial of service, and (3) ransom. The data leaks and the denial-of-service attacks are commonplace to demonstrate continued interest and attention by its natural adversaries and to create disruptive effects on the population’s quality of life and businesses. The ransom attacks seem to be targeting businesses purely for financial gain.

South Korea has accelerated defence cooperation agreements with the US to bolster her security against the rising tensions seen in North Asia. These agreements, including military exercises, have drawn the disdain from North Korea which has also resulted in the declaration by the DPRK[^4] that the ROK is the “primary foe”. New cyber threat activity observed in South Korea is generally targeted at organisation which are focused on Korean peninsula affairs across the border and associated with the military. This is on top of the continued interest by North Korean associated threat groups in performing surveillance and information collection on DPRK dissidents and understanding of North Korea.

Ensign noted that the following vendors’ solutions were deliberately exploited in the year:
- 3CX Desktop Application
- Cisco ASA VPN
- Citrix NetScaler ADC and Gateway
- Confluence Server and Data Center
- DreamSecurity MagicLine4NX
- GoAnywhere MFT
- Ivanti Connect Secure VPN
- JetBrains TeamCity
- Juniper BigIP
- Microsoft Windows
- Microsoft Outlook
- MOVEit Managed File Transfer (MFT) software
- PaperCut Application Server
- SysAid On-Premise
- Veeam Backup & Replication
- WinRAR
- Zoho ManageEngine

Extensive phishing campaigns leveraging malicious Windows Help Files (CHM) and malicious Hancom Office documents are observed to support social engineering efforts. Often, the successful breach into accounts and devices lead to exfiltration of personal data or business sensitive information. Ensign also observed the setup of fake Naver and Kakao email websites to harvest email credentials of users in phishing campaigns.

Some of these espionage campaigns have also continued to leverage the weaknesses in some app stores to propagate malicious applications on mobile devices and to encourage sideloading of malicious apps into the victim’s mobile devices.

The specific exploitation of INITECH’s solutions by Lazarus Group on the CrossWeb EX and MagicLine4NX (CVE-2023-45797), authentication process software solutions typically used in online financial services in South Korea, was observed to attempt gaining access into individuals’ bank accounts and cryptocurrency wallets.

---

## Australia

### Key Analysis Insights

#### Ensign Threat Classification Matrix
- **Insubstantial**: *NIL*
- **Potential**: APT33, APT41, Turla
- **Impending**: FIN7, Poison Carp
- **Material**: APT28, GambleForce, Lazarus Group, Volt Typhoon

*(Assessment progression: Insubstantial → Potential → Impending → Material)*
- **Capability**: ● (Potential), ● (Impending), ● (Material)
- **Intent**: ● (Potential), ● (Impending), ● (Material)
- **Opportunity**: ● (Potential), ● (Impending), ● (Material)

#### Most Affected Industry Groups
*(Based on Ensign Proprietary Data and Cyber Threat Intelligence data)*
1. **Technology, media & telecommunications**
2. **Engineering & Construction** *(New affected industry observed in 2023)*
3. **Retail**
4. **Government**
5. **Financial services**

#### Top Notable Cyber-Attack Effects Observed
- **Ransom**: 52.7%
- **Data Leak**: 16.4%
- **Denial of Service**: 12.1%

#### Techniques of Concern (MITRE ATT&CK v15)
- **TA0001: Initial Access**
  - T1566: Phishing
  - T1078: Valid Accounts
  - T1189: Drive-by Compromise
  - T1190: Exploit Public-Facing Application
  - T1133: External Remote Services
  - T1091: Replication Through Removable Media
  - T1195: Supply Chain Compromise
  - T1199: Trusted Relationship
- **TA0011: Command and Control**
  - T1090: Proxy
  - T1102: Web Service
  - T1071: Application Layer Protocol
  - T1105: Ingress Tool Transfer
  - T1001: Data Obfuscation
  - T1573: Encrypted Channel
  - T1008: Fallback Channels
  - T1104: Multi-Stage Channels
  - T1571: Non-Standard Port
  - T1092: Communication Through Removable Media
  - T1132: Data Encoding
  - T1568: Dynamic Resolution
  - T1219: Remote Access Software
- **TA0010: Exfiltration**
  - T1567: Exfiltration Over Web Service
  - T1048: Exfiltration Over Alternative Protocol
  - T1041: Exfiltration Over C2 Channel
  - T1030: Data Transfer Size Limits
- **TA0040: Impact**
  - T1486: Data Encrypted for Impact
  - T1565: Data Manipulation
  - T1485: Data Destruction
  - T1561: Disk Wipe
  - T1529: System Shutdown/Reboot
  - T1491: Defacement
  - T1498: Network Denial of Service
  - T1489: Service Stop

### Australia Territorial Analysis

Australia saw nine threat groups targeting the territory, with all but FIN7 and Poison Carp as the organised crime groups, aside from the initial access brokers and Ransomware groups.

FIN7 had been observed to exploit the Veeam Backup and Replication vulnerability (CVE-2023-27532), which is a common backup and archival solution used by many companies. FIN7’s exploits the vulnerability to gain initial access and support discovery and identification of targets, in the goal of big game hunting (BGH) through cyber supply chain compromise, since the vulnerable software has a wide range of users cross-cutting many industries.

Australia saw a series of attacks targeting manufacturing, professional services, retail, financial services and education industries. Some notable companies included: Boeing Systems[^5], Pizza Hut[^6], Sony Australia[^7], HWL Ebsworth[^8], and Latitude Financial[^9].

The top five industry groups observed to be attacked include: (1) Technology, media and telecommunications (TMT), (2) Engineering and construction, (3) Retail, (4) Government, and (5) Financial services.

The top cyber-attack effects observed were (1) ransom, (2) data leak, and (3) denial of service. Correlating both the targeted industry groups and the top cyber-attack effects, there is reason that ransoms were made to capitalise on the businesses supporting economic recovery post-pandemic. The data leaks and the denial-of-service attacks are targeted to bring awareness of the adversaries’ attention on Australian organisations.

Australia, being a close western aligned territory, attracts similar threat groups targeting the US and its allies. Most recent publicly reported attacks seem to concentrate on the TMR industry group which might be motivated to gain insights into the communications and technology resources available in the territory. Targeting of the Engineering and construction industry may be related towards the AUKUS agreement to collaboratively build nuclear-powered submarines to enhance Australia’s maritime security.

Ensign noted that the following vendors’ solutions were deliberately exploited in the year:
- 3CX Desktop Application
- Cisco ASA VPN
- Citrix NetScaler ADC and Gateway
- Confluence Server and Data Center
- GoAnywhere MFT
- Ivanti Connect Secure VPN
- JetBrains TeamCity
- Juniper BigIP
- MOVEit Managed File Transfer (MFT) software
- PaperCut Application Server
- Veeam Backup & Replication
- WinRAR
- Zoho ManageEngine

---

[^1]: DragonForce Malaysia: OpsPetir. (12 Apr 2023). Radware. Retrieved from: https://www.radware.com/security/threat-advisories-and-attack-reports/dragonforce-malaysia-opspetir/
[^2]: K. Poireault. DragonForce Ransomware Group Uses LockBit's Leaked Builder. (25 April 2024). Infosecurity Magazine. Retrieved from: https://www.infosecurity-magazine.com/news/dragonforce-ransomware-lockbit/
[^3]: G. Sharma. DragonForce Malaysia attacks Israeli institutions:. (14 April 2023). SecurityBrief Asia. Retrieved from: https://securitybrief.asia/story/dragonforce-malaysia-attacks-israeli-institutions-radware
[^4]: F. Koh. Kim Jong Un’s move to label South Korea an enemy, drop reunification policy part of North’s diplomatic playbook: Experts. (17 January 2024). Channel News Asia. Retrieved from: https://www.channelnewsasia.com/world/kim-jong-un-move-label-south-korea-enemy-drop-reunification-policy-strategic-part-norths-diplomatic-playbook-experts-4053871
[^5]: V. Insinna & Z. Siddiqui. Boeing says 'cyber incident' hit parts business. (3 November 2023). IT News. Retrieved from: https://www.itnews.com.au/news/boeing-says-cyber-incident-hit-parts-business-601999
[^6]: C. Rawling. Pizza Hut says nearly two-hundred thousand cus
[^7]: Sony Australia cyber incident disclosure.
[^8]: HWL Ebsworth cyber incident disclosure.
[^9]: Latitude Financial cyber incident disclosure.

---

tomers affected by data breach. (20 September 2023). ABC News. Retrieved from:https://www.abc.net.au/news/2023-09-20/pizza-hut-customers-affected-by-cyber-hack/102881804
7 D. Tilo. Over 6,000 individuals hit in Sony data breach: reports. (10 October 2023). Human Resources Director. Retrieved from:https://www.hcamag.com/au/news/general/over-6000-individuals-hit-in-sony-data-breach-reports/462431
8 J. Taylor. HWL Ebsworth hack: 65 Australian government agencies affected by cyber-attack. (18 September 2023). The Guardian. Retrieved from:https://www.theguardian.com/australia-news/2023/sep/18/hwl-ebsworth-hack-65-australian-
government-agencies-affected-by-cyber-attack
9 J. Barrett. Latitude Financial cyber-attack worse than first thought with 14m customer records stolen. (27 March 2023). The Guardian. Retrieved from: https://www.theguardian.com/australia-news/2023/mar/27/latitude-financial-cyber-data- 23
breach-hack-14m-customer-records-stolen

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Greater China Region
v15
KEY ANALYSIS INSIGHTS
| ENSIGN THREAT  |     |     |     |     |     | APT37 |     |
| -------------- | --- | --- | --- | --- | --- | ----- | --- |
Techniques of Concern
| CLASSIFICATION  |     |     |               |     |     | APT43     |                        |
| --------------- | --- | --- | ------------- | --- | --- | --------- | ---------------------- |
| MATRIX          |     |     | APT28         |     |     | BlackTech |                        |
|                 |     |     | APT41         |     |     | Carderbee | TA0001: Initial Access |
|                 |     | NIL | Earth Longzhi | NIL |     | DarkHotel | ▪ T1566: Phishing      |
▪ T1078: Valid Accounts
|     |     |     | FIN7 |     | GambleForce |     |     |
| --- | --- | --- | ---- | --- | ----------- | --- | --- |
▪ T1189: Drive-by Compromise
|     |     |     | Patchwork |     |     | Kimsuky | ▪ T1133: External Remote Services |
| --- | --- | --- | --------- | --- | --- | ------- | --------------------------------- |
▪ T1195: Supply Chain Compromise
Lazarus Group
▪ T1190: Exploit Public-Facing Application
Poison Carp
▪ T1091: Replication Through Removable Media
▪ T1199: Trusted Relationship
→→→ Increasing levels of threat to the subject →→→
▪ T1659: Content Injection
Insubstantial Potential Impending Material TA0011: Command and Control
▪ T1102: Web Service
| Capability |     |     | ●   | ●   |     | ●   | ▪ T1071: Application Layer Protocol |
| ---------- | --- | --- | --- | --- | --- | --- | ----------------------------------- |
▪ T1105: Ingress Tool Transfer
| Intent |     | ●   |     | ●   |     | ●   | ▪ T1090: Proxy |
| ------ | --- | --- | --- | --- | --- | --- | -------------- |
▪ T1573: Encrypted Channel
| Opportunity |     | ●   | ●   |     |     | ●   | ▪ T1132: Data Encoding |
| ----------- | --- | --- | --- | --- | --- | --- | ---------------------- |
▪ T1001: Data Obfuscation
▪ T1008: Fallback Channels
MOST AFFECTED  The following observations are based on Ensign Proprietary Data and Cyber Threat  ▪ T1095: Non-Application Layer Protocol
Intelligence data ▪ T 1 1 0 4 :   M u lt i -S ta g e  C h a n n els
INDUSTRY GROUPS ▪ T 1 5 7 1 :   No n - S ta n d a rd  P o r t
▪ T1219: Remote Access Software
▪ T1092: Communication Through Removable Media
▪ T1659: Content Injection
▪ T1568: Dynamic Resolution
▪ T1205: Traffic Signaling
TA0010: Exfiltration
Technology, media &  Manufacturing Professional services Healthcare Financial services ▪ T1041: Exfiltration Over C2 Channel
▪ T1567: Exfiltration Over Web Service
telecommunications
▪ T1048: Exfiltration Over Alternative Protocol
New affected industries observed in 2023 ▪ T1020: Automated Exfiltration
▪ T1030: Data Transfer Size Limits
| TOP NOTABLE cyber-attack EFFECTS OBSERVED |     |     |     |     |     |     | TA0040: Impact |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | -------------- |
▪ T1529: System Shutdown/Reboot
▪ T1486: Data Encrypted for Impact
▪ T1561: Disk Wipe
|     | Ransom |     | Sale of Access |     | Sale of Data |     | ▪ T1489: Service Stop |
| --- | ------ | --- | -------------- | --- | ------------ | --- | --------------------- |
▪ T1485: Data Destruction
▪ T1491: Defacement
|     | 68.5% |     | 21.9% |     | 4.1% |     |     |
| --- | ----- | --- | ----- | --- | ---- | --- | --- |
▪ T1498: Network Denial of Service
24

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Greater China Region
The Greater China region, particularly the Hong Kong Special The PRC has sustained complications with the US in recent years resulting
Administration Region (Hong Kong, where Ensign has longstanding in trade tensions, including concerns relating to the Republic of China
operational presence) and the People’s Republic of China (PRC, which is a (Taiwan). The developments have resulted in public displays of
recent expansion from Ensign), has seen 14 threat groups targeting the disagreement but also noticeable cyber activity. Further to the US-China
territory. Unique to this territory, there are domestically associated threat tensions, there are also rising regional concerns on security by neighbours
groups targeting entities based in the region — APT41, BlackTech, in East Asia. This has resulted in increased balancing actions between the
Carderbee, Earth Longzhi, GambleForce, and Poison Carp. states in the region to accommodate their risk appetites.
The top five industry groups observed to be attacked include: (1) Ensign noted that the following vendors’ solutions were deliberately
Technology, media and telecommunications, (2) Manufacturing, (3) exploited in the year:
Professional services, (4) Healthcare, and (5) Financial services. Relating to
▪ Cisco ASA VPN ▪ Juniper BigIP
the Hong Kong region, we are seeing the inclusion of Manufacturing,
▪ Citrix NetScaler ADC and Gateway ▪ MOVEit Managed File Transfer
Professional services, and Healthcare in the top targeted industry groups
▪ Confluence Server and Data (MFT) software
this year.
Center ▪ PaperCut Application Server
The top cyber-attack effects observed were (1) ransom, (2) sale of access, ▪ Fortinet FortiOS ▪ Veam Backup & Replication
▪ GoAnywhere MFT ▪ WinRAR
and (3) sale of data. Correlating both the targeted industry groups and the
▪ Ivanti Connect Secure VPN’ ▪ Zoho ManageEngine
top cyber-attack effects, there is reason that ransoms were made to
▪ JetBrains TeamCity
capitalise on the businesses supporting economic recovery post-
pandemic. The sale of access and the sale of data attacks can be
attributed to threat actors with intents to gain access to targeted
companies through “big game hunting” and to obtain information for
espionage purposes.
25

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Territorial Tactics Observations
Through our observations and analysis across our territories in Singapore,
Malaysia, Indonesia, and the Greater China Region, Ensign has made
unique insights to the cyber events which are detailed in this section.
Common adversary techniques observed across the territories include:
1. T1110: Brute Force was the dominant Technique observed across
Singapore, Malaysia, Indonesia, and the Greater China Region.
2. T1595: Active Scanning and T1078: Valid Accounts were common
top techniques observed across Singapore, Malaysia, and
Indonesia.
3. T1071: Application Layer Protocol was common between Malaysia,
Indonesia, and the Greater China Region.
Influential events in the territories were leveraged to effect for the cyber
events observed. Many of the significant events include elections, critical
supply chain vulnerabilities with widespread effects, and geopolitical
tensions.
Likewise, there were common industry groups which showed signs of
compromise across the territories:
1. Singapore, Malaysia, Indonesia, and the Greater China Region all
saw signs of compromise to Technology industry group.
2. Singapore, Malaysia, and Indonesia saw signs of compromise to
Manufacturing, Energy & Utilities, and Telecommunications
industry groups.
3. Singapore and the Greater China Region saw signs of compromise to
the Real Estate industry group.
AI generated image with representations from Singapore, Malaysia, Indonesia and the
Greater China Region
26

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Singapore
KEY OBSERVATIONS FROM ENSIGN PROPRIETARY DATA
Ensign observed persistent TA0043: Reconnaissance
and TA0006: Credential Access activity throughout the
year with peak activity levels observed in 2023 Q3.
The Microsoft Outlook Privilege Escalation Vulnerability
(CVE-2023-23397) also contributed to cyber activities
in 2023 Q1 with elevated observations for TA0004:
5.4%
7.1% Privilege Escalation and TA0005: Defence Evasion.
8.4%
T1071:
T1078: Valid Application Ensign observed sustained and high interest in TA0043:
T1595: Active
Accounts layer protocol Reconnaissance in the (1) Administrative and
Scanning
Technical Services, (2) Manufacturing, (3) Banking &
Finance, (4) Insurance, (5) Telecommunications, and
23.5%
(6) Education industry groups. This means there are
T11110: Brute Force sustained interest in targeting these six industry
groups.
2023 Q3 saw the highest cyber activity in coincidence with several There were elevated observations in TA0005: Defense
Evasion, TA0006: Credential Access, and TA0011:
high-profile events:
Command and Control in the following industry
1. The arrest of 10 foreign nationals allegedly part of the largest groups: (1) Healthcare, (2) Real Estate, (3)
money laundering scheme in the world in August.10 Technology, (4) Energy and Utilities, (5) Aerospace,
(6) Manufacturing, and (7) Telecommunications. This
2. The Singapore Presidential Election in September.
means that the seven industry groups demonstrated
signs of compromise.
10 L. Tang. Billion-dollar money laundering case: Singapore police began ‘comprehensive intelligence probe’ in early 2022. (3 October 2023). Channel News Asia. Retrieved from: https://www.channelnewsasia.com/singapore/billion-dollar-
money-laundering-police-intelligence-probe-2022-3816371
27

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Malaysia & Indonesia
KEY OBSERVATIONS FROM ENSIGN PROPRIETARY DATA
Ensign observed persistent TA0043: Reconnaissance
and TA0006: Credential Access activity throughout the
year with peak activity levels observed between 2023
Q2 to 2023 Q4.
The suite of MOVEit vulnerabilities (CVE-2023-36932,
CVE-2023-36933, and CVE-2023-36934) contributed to
the peak of cyber activities from the months of May to
11.3% 11.2% September with elevated observations for TA0006:
Credential Access.
T1098: T1078:
17.7%
Account Valid Ensign observed sustained and high interest in TA0043:
Manipulation Accounts
T1595: Reconnaissance in the (1) Insurance, (2) Energy and
Active Scanning Utilities, (3) Administrative and Technical Services,
27.6%
(4) Banking & Finance, (5) Manufacturing, and
T1110: Brute Force (6) Telecommunications industry groups. This means
there are sustained interest in targeting these six
2023 Q2 to Q4 saw the highest sustained cyber activity levels in
industry groups.
coincidence with the following events:
There were elevated observations in TA0002:
1. Six state elections in Malaysia for Selangor, Kelantan, Terengganu, Execution, TA0005: Defense Evasion, TA0006:
Negeri Sembilan, Kedah, and Penang in August. Credential Access in the following industry groups:
(1) Telecommunications, (2) Energy and Utilities,
2. ASEAN high-level events with Indonesia heading as Chair in
(3) Administrative and Technical Services,
2024 in the months of July till September. (4) Manufacturing, (5) Insurance, and (6) Technology.
This means that the six industry groups demonstrated
signs of compromise.
28

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Greater China Region
KEY OBSERVATIONS FROM ENSIGN PROPRIETARY DATA
Ensign observed persistent TA0001: Initial Access and
TA0006: Credential Access activity throughout the
year. This indicates that threat actors are leveraging
harvested access and credentials for cyber-attacks.
Ensign observed sustained and high interest in TA0001:
Initial Access in the (1) Real Estate, (2) Mining, (3)
8.5% Education, (4) Banking & Finance, and (5) Insurance
9.2% industry groups. This means there are sustained
T1071:
exploitation targeting these five industry groups.
16.5% T1566: Application
layer protocol
Phishing There were elevated observations in TA0003:
T1059: Command
Execution, TA0005: Defense Evasion, TA0006:
and Scripting
23.5% Interpreter Credential Access, TA0007: Discovery, and TA0011:
Command and Control in the following industry
T1110: Brute Force
groups: (1) Real Estate, (2) Insurance, (3) Banking &
Finance, (4) Education, (5) Technology, and
2023 saw sustained cyber activity levels in coincidence with the following events:
(6) Hospitality. This means that the six industry groups
1. Chinese meteorological balloon which entered US airspace
demonstrated signs of compromise.
2. National People's Congress (NPC) and the National Committee of the Chinese
It is noteworthy that the Administrative and Technical
People's Political Consultative Conference (CPPCC) in March
Services industry group saw elevated levels of TA0005:
3. China-Central Asia Summit in May and Belt and Road Forum for International
Defense Evasion. This indicates that the industry
Cooperation in October
group has active threat actors navigating the
4. 19th Asian Games in July and 4th Asian Para Games in October environments to uncover opportunities for command
5. US-China dialogue meetings from June to November and control, exfiltration or impact. The
Telecommunications industry group saw elevated
6. US expanded export controls within US and like-minded countries on
levels of TA0007: Discovery. This indicates intent by
advanced chip manufacturing equipment in October
threat actors to uncover information of value in this
7. Sustained trials on activists in relation to the national security Law
industry group.
29

3
TOP THREAT
TRENDS 2023
ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024 30

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Overview of Top Threat Trends of 2023
AI helped defenders but also Cyber supply chain attacks
Digital trust was eroded
enabled attackers worsened
▪ Defenders had access to more AI-enabled ▪ Deliberate influence operations were ▪ There were more cases of malicious code
tools to detect anomalous or malicious conducted (using hand-crafted and AI- injections into popular open-source
activity. generated content) to manipulate opinion, software.
especially ahead of major elections.
▪ Attackers used AI for Reconnaissance and ▪ Targeted attacks on digital infrastructure,
Initial Access (e.g. phishing). ▪ Early experiments in deepfakes and especially network devices, increased.
synthetic identities were observed for social
▪ Attackers used AI to prototype new cyber ▪ OT-based malware like PIPEDREAM and
engineering attacks (influence and
weapons (e.g. polymorphism). subsequently COSMIC ENERGY were
phishing).
developed in quick succession
▪ Attackers also attacked AI systems, mostly
▪ As GenAI imagery was still identifiable in demonstrating speed and interest.
to test the systems and possibilities rather
2023, only some users were spoofed.
than to secure any specific objectives.
Attackers evolved their TTPs to Geopolitics worsened “De-risking” accelerated tech
defeat our processes and tools cybersecurity everywhere bifurcation
▪ Attackers recognised that defenders were ▪ Conflicts between Russia-Ukraine and ▪ Countries with the means started
not prioritising the patches for low-risk / Israel-Hamas, and even US-China tensions, developing organic technology stacks to
severity vulnerabilities, often for months. have all spilled over into the cyber domain. reduce reliance on shared global Internet
infrastructure and tools.
▪ Attackers developed attack paths using ▪ Hacktivism and state-sanctioned /
these low-risk vulnerabilities and remained sponsored cyber activity increased. ▪ The Western tech stack will continue to
undetected with stealthier actions (e.g. Hacktivist groups demonstrated more grapple with cyber risks from open
living off the land techniques). sophisticated capabilities (Wiperware, architecture. The Asian tech stack may
supply chain attacks). require new cybersecurity concepts, as the
design considerations may differ.
Interoperability is not assured between
them.
31

▪ Ransomware, Evolved: Shift in Extortion Techniques
▪ Hacktivists, Unite: Increasing Sophistication of Cause-aligned Groups
▪ Digital Infrastructure Under Fire: Threats Across the Cyber Supply Chain
▪ Digital Sheriffs: New Regulatory and Policy Initiatives that Aim to Address
Risks of Emerging Technology
▪ Disclosure Revelations: How Mandatory Incident Reporting is Shining a
Light on Corporate Cyber Impact
4
TOPICAL
INSIGHTS
ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024 32

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
ESCALATING THREATS
Ransomware, Evolved: Shift in Extortion Techniques
Selected events in the fight against Ransomware by
▪ Ransomware remained the most worrying threat in 2023, with
international enforcement
an expanding criminal ecosystem and service delivery model.
JAN 2023 Hive taken down by Law enforcement
▪ Companies were extorted multiple times in an attack, MAR 2023 ChipMixer, used to launder ransom payment, taken
AUG 2023 down by Law enforcement
sometimes from the same attacker (first to recover the
OCT 2023 Qakbot malware (used by REvil, LockBit) taken down by
systems, then to delete the data “quietly”), and sometimes
Law enforcement
from multiple attackers (or rogue affiliates from the successful NOV – DEC 2023 Ragnar Ransomware taken down by Law enforcement
first attacker). DEC 2023 ALPHV taken down by Law enforcement
FEB 2024 Sibad.io sanctioned
▪ While Law enforcement made big strides in taking down some
MAR 2024 LockBit 3.0 taken down by enforcement
Ransomware groups, the compelling financial motive ensured MAR 2024 ALPHV claimed to be taken down, but international
new criminal groups (or old ones reformed) to take their place. enforcement denied involvement in its disappearance
LockBit allegedly returned as LockBit 4.0
The Persistent Ransomware Threat
These takedowns, however, are likely to prove short term. Members of
In 2023, Ransomware continued to pose the most dangerous such groups either join “competitors” or reconstitute under a new brand.
cybersecurity threat, targeting organisations of all sizes, industries, and In March 2024, ALPHV used the late 2023 takedown screenshot to pull a
territories. Many organisations that Ensign has worked with over the past disappearing act and scam its own criminal affiliate.12 Meanwhile, after
year updated their Ransomware strategy, playbook, and conducted cyber LockBit 3.0 was taken down, the group allegedly returned as LockBit 4.0.13
crisis training exercises to ensure they were prepared for this threat. Hive seemingly ceased all operations after Law enforcement takedown,
but evidence suggested that its members had joined Hunters
Ransomware-as-a-Service (RaaS) remained the dominant model,
International. For cryptocurrency laundering, attackers would find
enabling novice criminal groups to get a piece of the action. Law
another platform, just as they moved from Blender (sanctioned in 2022) to
enforcements, mostly collaborations between the US and Europe, had a
Sinbad.io (sanctioned in 2023).
very busy 2023 (and early 2024), attempting to slow the growth of
Ransomware. In addition to taking down infrastructure of RaaS operators In a guerilla warfare fashion, these attacker groups have demonstrated
(Hive, ALPHV, LockBit, Ragnar),11 Law enforcements also issued that they can reorganise themselves into new operations right after being
sanctions and/or took down malware used by those groups (Qakbot) in “taken down”. In these new operations, they may rebrand change the
their attacks and cryptocurrency mixers to launder ransom payment modus operandi, all while using the same malware, complicating
(ChipMixer, Sibad.io). investigations.
11 E. Kovacs. Law Enforcement Reportedly Behind Takedown of BlackCat/Alphv Ransomware Website. (11 December 2023). Security Week. Retrieved from: https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-
ransomware/
12 Vx-underground. X. (4 March 2024). Retrieved from: https://twitter.com/vxunderground/status/1764676460113994220
13 J. Pearson. Lockbit cybercrime gang says it is back online following global police bust. (27 February 2024). Reuters. Retrieved from: https://www.reuters.com/technology/cybersecurity/lockbit-cybercrime-gang-says-it-is-back-online-following-global- 33
police-bust-2024-02-26/

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Double Extortion, Single Attacker leaves the door wide open to other attackers (or affiliates of the first
attacker, who are likely already aware of the initial exploit) to repeat the
There are competitive dynamics even within the criminal underworld.
attack.
RaaS operators continue to evolve their methods and shift their extortion
techniques in order to extract more financial value from their targets, Individuals who form the criminal gang may also betray each other. One
such as by employing tactics that increase the pressure on victims to pay example of this is the aforementioned case, where the group who received
the ransom. While the malware itself has only changed marginally last the payment opted not to share the ransom with their own partners and
year, it is the tactics that have become more aggressive and dangerous. disappeared. The partners, who were left empty-handed, tried to extort
One of the notable changes to the malware last year was the use of the the victim (again).
memory-safe and multi-platform language, Rust, by ALPHV.14
In other cases, initial access brokers (the part of the group who provides
Traditional Ransomware attacks typically involve encrypting a victim's the stolen credentials or entry point into the victim’s network) sometimes
data and demanding payment for the decryption key. In 2023, there was “double dip” and resell the stolen data (especially credential information,
an increase in what is known as “double extortion” tactics, whereby which is their business model) even if the main group promised the victim
attackers steal the data first, then encrypt the systems. Subsequently, that the data would be deleted.
they threatened to release the stolen data publicly, creating reputational
All of this was brought to light when Law enforcement raided LockBit in
damage and regulatory problems for the company if the ransom for the
early 2024, and discovered that LockBit servers retained data from
decryption is not paid. Hunter International, the spin-off of Hive,
victims, despite the gang’s assurance that it had been deleted: “If we do
differentiated itself from its predecessor by focusing more on data
not give you decrypters, or we do not delete your data after payment, then
exfiltration and the subsequent extortion of public data release.
nobody will pay us in the future”. There is clearly no honour among
In another case, ALPHV wrote in to the US Securities and Exchange thieves.16
Commission directly to complain that their victim, MeridianLink, had not
Extortion, with an Added Dose of Doxing
filed the relevant15 forms within the mandatory four-day period. This
serves as a clear example of how cybercriminals are weaponizing Another way in which attackers increase pressure on victims is by
regulatory requirements, among other public humiliation tools, against contacting journalists or customers in parallel to shame the victim into
their victims. paying. Occasionally, they will even publish samples of the data on social
media, including personal details of the key leaders in the victim
Double Extortion, Multiple Attacker Groups
organisation. The victim organisation’s leadership is now directly under
Previous incidents proved that victims of Ransomware tend to be targeted pressure to resolve the incident quickly.
repeatedly if they had demonstrated willingness to pay the initial ransom.
Organisations in urgent need to pay the ransom to recover their systems
often overlook conducting the proper forensics to identify the attack
vector that compromised their networks in the first place. This often
14 Microsoft Threat Intelligence. The many lives of BlackCat ransomware. (13 June 2022). Microsoft. Retrieved from: https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/
15 E. Kovacs. Ransomware Group Files SEC Complaint Over Victim’s Failure to Disclose Data Breach. (16 November 2023). Security Week. Retrieved from: https://www.securityweek.com/ransomware-group-files-sec-complaint-over-victims-failure-to-
disclose-data-breach/
16 K. Meegan-Vickers. The LockBit takedown Law enforcement ‘trolls’ ransomware gang. (4 April 2024). Global Initiative. Retrieved from: https://globalinitiative.net/analysis/the-lockbit-takedown-law-enforcement-trolls-ransomware-gang/ 34

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
A Worrisome Outlook monitoring for unusual activity, identifying and protecting crown jewels,
and having a robust and sensible backup strategy. More importantly,
Ransomware continues to elude Law enforcement, cybersecurity
organisations must regularly activate backup restoration processes,
regulators, and organisations — and this will continue to be the case for
instilling trust and confidence among corporate leaders in this viable
2024. As the threat of Ransomware looks endemic for now, cyber
alternative to paying the ransom.
defenders and insurers need to have endemic strategies. Organisations
should continue to invest in sound cybersecurity practices like
35

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Hacktivists, Unite: Increased Sophistication of Cause-aligned Groups
▪ Hacktivism has become more sophisticated, as more capable individuals are drawn in by political causes, and they have easier
access to more powerful cyber weapons.
▪ States are openly and deliberately mobilising their citizens and supporters and encouraging them to take part in cyber warfare
against their opponents, and some states are masking state cyber activity as hacktivism to reduce attribution.
▪ Regional hacktivism activities have ramped up, as a direct spillover from faraway conflicts.
Evolving Familiarity: Old News, Fresh Face Their main goals include defacing the targeted website, displaying a text or
image, and spreading a message or agenda to the attacker’s cause.
Hacktivism is malicious cyber activity conducted by threat actors that are
motivated by a political or social cause. In the past, many of them acted DDoS attacks often target organisations in countries deemed to be
alone or in small groups, with only the limited capabilities that they involved in conflicts.These attacks are conducted using botnets to
organically possessed. With the increasing availability of sophisticated overwhelm target systemswith traffic to disrupt operations. There has
cyber weapons and malicious talents on the Dark Web, these hacktivists been a significant increaseof hyper volumetric HTTP DDoS attacks
have emerged as a serious and credible threat to governments and worldwide in the third quarter of2023, in which Singapore was the second
organisations, andhave undergone significant evolution in recent times, most targeted country (partly also due to the prevalence of corporate and
which will require continual dynamic adaptation and response. Internet infrastructure nodes).17Thiscan be attributed to threat actors
leveraging a 0day, dubbed “HTTP/2Rapid Reset” since August 2023. The
Unravelling Hacktivism's Growing Sophistication
attack employs the use of VM-based botnets consisting of nodes between
Hacktivism has become increasingly sophisticated, as tactics used 5,000 to 20,000 nodes, asopposed to the conventional use of millions of
byhacktivists have diversified and now include a range of disruptive weak IoT devices.
anddestructive methods, including web defacement attacks of public-
The Israel-Palestine conflict has also witnessed significant cyber-attacks
facing assets, distributed denial-of-service (DDoS) attacks, destructive
with destructive consequences, including the employment of
Ransomware and Wiperware, and hacktivist-inspired data breaches.
Ransomware and Wiperware tactics. For instance, the BiBi
At the simpler end of the spectrum, defacement attacks usually involve malwarefamily has been observed wiping data on both Linux and
attackers altering a website's content, appearance, or functionality with Windowscomputers in Israeli systems, and unlike other types of attacks,
malicious intent. it is purelyfocused on destruction rather than any informational or
financialbenefit.18
17 O. Yoachimik & J. Pacheco. DDoS threat report for 2023 Q3. (26 October 2023). Cloudflare. Retrieved from: https://blog.cloudflare.com/ddos-threat-report-2023-q3/
18 B. Toulas. Israel warns of BiBi wiper attacks targeting Linux and Windows. (13 November 2023). Bleeping Computer. Retrieved from: https://www.bleepingcomputer.com/news/security/israel-warns-of-bibi-wiper-attacks-targeting-linux-and-windows/
36

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Masking State-sponsored Activity Behind Hacktivism increasingly volatile geopolitical environment, withsome collaborating
with other collectives to mount joint cyber-attacks.As these collectives
State-sponsored threat groups typically work under direct instruction and
take sides in contemporary geopolitical conflicts,undertaking high-profile
funding from the state. With the recent developments seen in the Russia-
operations against each other’s targets,hacktivism will become an
Ukraine war, states called on to the people aligned to its cause to act for
increasingly common occurrence.
the state’s interests.19 Through these means, the state-sponsored actors
exploit proxy agency to expand their capacity and obfuscate their identity Hacktivists’ Targets Spread Far and Wide
by pretending to be independent hackers with activist motives, hence
Not only havewebsites belonging to both Israeli and Palestinian
making it difficult to attribute the cyber-attack to a specific government or
institutions beensubjected to defacement attacks, but web assets of
entity.
organisationslocated far beyond the warzone have been affected as
Originally White Hat cyber professionals, who are not criminal actors, may well.Ensign has observed an increase in hacktivist activity amid a
get influenced by certain causes or political agendas if it resonates with significantrise in geopolitical tensions and emerging conflict globally.
them. These professionals may leverage their expertise, skills, and access While there was a surge in malicious cyber activity during the Russia-
to conduct cyber activity in support of a hacktivist agenda. This may involve Ukraine conflict, the Israel-Palestine conflict took prominence in late 2023.
joining vigilante militias or engaging in unfunded campaigns directed by a
Within the region, hacktivists have also been known to deliberately
state. For instance, the Vice Prime Minister of Ukraine tweeted a post on
breachand leak sensitive data. For instance, the Indonesia-focused threat
Twitter for individuals to hack or launch DDoS attacks on a list of Russian
actor,Bjorka,targets various government and corporate entities with
websites posted on a Telegram channel under their control.20 The loose
ademonstrated ability to infiltrate systems and expose confidential
collective of the Ukraine IT Army was raised from a collective of
material, with the aim ofembarrassing its victims.21 The impact has
technologists, from all parts of the world, many of whom were employed
beensignificant, often with political or financial implications. In fact, these
and acting for the cause during their free time. In some instances, they may
tactics employed by regional hacktivists have become increasingly similar
also use their employer’s assets and resources for the activities, further
to state-sponsored attackers.
implicating their employers into the fight.
Not only havewebsites belonging to both Israeli and Palestinian
Russian authorities also turned a blind eye to cyber attackers operating
institutions beensubjected to defacement attacks, but web assets of
from their territory, who went after Ukrainian targets. Hamas is also known
organisationslocated far beyond the warzone have been affected as well.
to call upon their supporters to act in the cyber domain. New hacktivist
Attacking other countries serves as a means of sending a message to
collectives with alleged nation-state support havesprouted amid an
actors perceived as allies or adversaries in the Israel-Palestine conflict.
19 A. Render-Katolik. The IT Army of Ukraine. (16 August 2023). Center for Strategic and International Studies. Retrieved from: https://www.csis.org/blogs/strategic-technologies-blog/it-army-ukraine
20 M. Burgess. Ukraine’s Volunteer ‘IT Army’ Is Hacking in Uncharted Territory. (27 February 2022). Wired. Retrieved from: https://www.wired.com/story/ukraine-it-army-russia-war-cyber-attacks-ddos/
21 L. Yulisman. Indonesia hunts for Bjorka, hacker selling 1.3b SIM card users' data, taunting officials. (19 September 2022). Bleeping Computer. Retrieved from: https://www.straitstimes.com/asia/se-asia/indonesia-hunts-for-bjorka-hacker-selling-13b-
sim-card-users-data-taunting-officials 37

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Threat actors supporting eitherside of the Israel-Palestine conflict may
indiscriminately targetSingapore-based companies that operate regionally,
giventhat Singapore is perceived as pro-Israel whileneighbouringcountries
such as Malaysia, Indonesia, and Brunei do notrecogniseIsrael and have
beenvocal against Israel.
For instance, #OpSingapore, a campaign initiated by Indonesian and Malaysian
pro-Palestinian hacker groups, targeted various Singaporean organisationsin
October 2023 shortly after Hamas’ attack on Israel.22 As a result,several
websites were defaced, database breached, and sensitive data was leaked. The
campaign was launched by a collective ofself-styled hacktivist “collectives” led
by 4 EXPLOITATION and AnonGhost Indonesian. These attacks, using tactics
such as DDoS andSQL injection, are part of the #FreePalestine movement’s
effort toprotest organisations perceived as supportive of Israel in the Israel-
Palestine conflict.
In return, pro-Israeli groups, such as R00TK1T, havetargeted sites located in
Indonesia and Malaysia, successfully taking several of them offline.23
Given the far-reaching effects of hacktivism, organisations must recognise that
despite their espoused lack of political allegiance or proximity to the conflict,
they remain susceptible to the actions of opportunistic and state-sponsored
threat actors who may find an indirect reason to target their organisation or opt
to use an attack on their organisation to send a political signal to a third party,
such as a customer, partner, or even the government.
Hacktivism as a Tool-for-Attack has Made its Mark and is Here to Stay
Hacktivism, with the use of advanced technological tools and techniques, has
cemented itself as a tool utilised by cause-aligned individuals, groups, and even
states. As technology progresses and new vulnerabilities emerge, the
sophistication and scale of hacktivist attacks are anticipated to evolve.
Sophisticated hacktivism is likely to persist as a significant challenge in the
digital age, with the potential for increased proliferation and escalation.
22 Heightened Alert for Cyber Activities Targeting Domains and Infrastructures in Malaysia. (27 February 2022). National Cyber Coordination and Command Centre. Retrieved from: https://www.nc4.gov.my/alert/653a2988900885a0819d058d
23 MA-1027.022024: MyCERT Advisory - Recent Cyber Incidents Launched by TA ROOTK1T ISC Team to Malaysia Organisations. (6 February 2024). Malaysia Computer Emergency Response Team. Retrieved from:
https://www.mycert.org.my/portal/advisory?id=MA-1027.022024
38

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Moving beyond Hacktivism
Increasingly, hacktivist groups are growing bolder and more competent with
each successive cyber-attack. Some have started to develop novel tools and
solutions to perform their attacks, others have quickly leveraged their access
to leaked source code for Ransomware (e.g. the LockBit Black version,
released during the Law enforcement blitz on the LockBit Gang) to evolve into
organised crime groups. Two notable examples of hacktivist groups active in
our region who have expressed intents to evolve into organised crime groups
include DragonForce Malaysia and GhostSec.
DragonForce Malaysia had declared that they are moving into Ransomware
operations.24 Analysts suggest that while it is unnatural for hacktivist groups
to perform cyber-attacks for financial gain, it is more likely a means to gain
funds to build up capabilities or “marketing”.
On a similar but different track, the GhostSec group had not only developed a
DDoS tool, CyberTroopers,25 and subsequently collaborate with the
Stormous Group to perform Ransomware attacks using the GhostLocker 2,0
Ransomware.26
Such developments are indications that hacktivists may progressively grow
from being a loose collective of individuals to a more organised and
structured group funded by illicit gains to carry out their cause. This may in
turn help the cyber defenders gain better understanding of the protocols and
behaviours of the groups that develop down this path.
24 N. Eddy. DragonForce Malaysia Releases LPE Exploit, Threatens Ransomware. (1 July 2022). Dark Reading. Retrieved from: https://www.darkreading.com/vulnerabilities-threats/dragonforce-malaysia-releases-lpe-exploit-threatens-ransomware
25 G. Sharma. DragonForce Malaysia attacks Israeli institutions: Radware. (14 April 2023). Security Brief. Retrieved from: https://securitybrief.asia/story/dragonforce-malaysia-attacks-israeli-institutions-radware
26 Alert: GhostSec and Stormous Launch Joint Ransomware Attacks in Over 15 Countries. (6 March 2024). The Hacker News. Retrieved from: https://thehackernews.com/2024/03/alert-ghostsec-and-stormous-launch.html
39

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
EVOLVING ATTACKS
Digital Infrastructure Under Fire: Threats Across the Cyber Supply Chain
• Threat actors are investing in exploits targeting vulnerabilities in common infrastructure solutions across all technology layers,
including endpoint, middleware, network, hardware, and operational technology (OT).
• There is an urgency to map and understand the digital attack surface we operate in and determine exposure.
• Cyber supply chain risk management might often be impossible for direct influence but must be planned and managed to limit
cascading and widespread effects across systemic dependencies.
• Threat and Vulnerability Exposure Management is an increasingly important priority for organisations.
Watershed Year for Actively Exploited Vulnerabilities across MOVEit: The vulnerabilities associated with the MOVEit managed file
Digital Infrastructure transfer solution allowed authentication bypass and access to the
database there by exposing the contents for exfiltration and providing a
2023 was the year where many vulnerabilities were discovered and
pathway for further compromise. The MOVEit vulnerability was exploited by
exploited across the fundamental digital infrastructure components,
FIN11 to compromise a large number of victims28 (estimated to number
including endpoint, middleware, network and hardware. Noteworthy
more than 2,500 companies and more than 80 MM individuals). Some of
exploit campaigns – BadCandy, CitrixBleed, MOVEit, PaperCut – when
the noteworthy companies include Fortescue, Medibank, Prudential
combined with many network solution vulnerabilities relating to Barracuda
Malaysia, PwC, Shell, Sony, amongst others.
Networks, Cisco, Fortinet, Zyxel (amongst others), have led to widespread
and cascading implications across the cyber supply chain. While we often PaperCut: The vulnerabilities associated with the PaperCut NG
hear practitioners advocating a multi-layered defence concept to defend vulnerabilities allowed authentication bypass and code execution,
their digital attack surface, when all layers of technology come under providing access and data to threat groups. Cl0p,29 LockBit Gang,
threat, the opportunities to compromise elevates. MuddyWater, and APT35.
Active Campaigns Compromising Organisations Ivanti Pulse Secure VPN: The vulnerabilities associated with the Ivanti
Pulse Secure VPN allowed authentication bypass and execute arbitrary
CitrixBleed. The vulnerabilities associated with Citrix NetScaler SDC and commands. Noteworthy victims included The MITRE Corporation30 and
Datacenter leak information which supports reconnaissance and targeting. CISA.31
CitrixBleed was notably employed by LockBit Gang to compromise Allen &
Overy, Boeing, ICBC and DP World.27
27 B. Toulas. LockBit ransomware exploits Citrix Bleed in attacks, 10K servers exposed. (14 November 2023). Bleeping Computer. Retrieved from: https://www.bleepingcomputer.com/news/security/lockbit-ransomware-exploits-citrix-
bleed-in-attacks-10k-servers-exposed/
28 B. Kondruss. MOVEit hack victim list. (20 December 2023). Retrieved from: https://konbriefing.com/en-topics/cyber-attacks-moveit-victim-list.html
29 C. Page. PaperCut says hackers are exploiting ‘critical’ security flaws in unpatched servers. (25 April 2023). Techcrunch. Retrieved from: https://techcrunch.com/2023/04/25/papercut-hackers-critical-fLaw-clop-ransomware/
30 S. Gatlan. MITRE says state hackers breached its network via Ivanti zero-days. (19 April 2024). BleepingComputer. Retrieved from: https://www.bleepingcomputer.com/news/security/mitre-says-state-hackers-breached-its-network-via-
ivanti-zero-days/
31 K. Alspach. CISA Breached Via Ivanti VPN Vulnerabilities: Report. (8 March 2024). CRN. Retrieved from: https://www.crn.com/news/security/2024/cisa-breached-via-ivanti-vpn-vulnerabilities-report 40

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Category Vulnerability Description
Endpoint • Apple mobile devices WebKit (CVE-2023-42916)
• Apple iOS Kernel (CVE-2024-23225)
• Apple RTKit (CVE-2024-23296)
• Windows Virtualization-based Security HVCI (CVE-2024-21305)
Middleware • Fortra GoAnywhere managed file transfer (CVE-2023-0669)
• JetBrains TeamCity (CVE-2023-42793)
• Microsoft Outlook (CVE-2023-23397)
• MOVEit managed file transfer (CVE-2023-34362, CVE-2023-36932, CVE-2023-36933, CVE-2023-36934)
• PaperCut NG managed file transfer (CVE-2023-27350, CVE-2023-27351)
• VMware vCenter Server (CVE-2023-34048)
• WinRAR (CVE-2023-38831)
• Zoho ManageEngine (CVE-2022-47966)
Network • Barracuda ESG (CVE-2023-2868)
• Cisco ASA and FTD Software VPN (CVE-2023-20095, CVE-2023-20269)
• BadCandy:- Cisco IOS XE (CVE-2023-20198, CVE-2023-2073)
• CitrixBleed:- Citrix NetScaler ADC & Gateway (CVE-2023-4966, CVE-2023-4967, CVE-2023-6548, CVE-2023-6549)
• Fortinet FortiOS & FortiProxy (CVE-2023-44250)
• Ivanti Pulse Connect VPN (CVE-2023-46805, CVE-2024-21887)
• Juniper SRX EX Junos (CVE-2024-21591
• SonicWall NGFW (CVE-2022-22274, CVE-2023-0656)
• Zyxel ATP, USG FLEX, and ZyWall VPN Firewalls and gateways (CVE-2023-28771)
• Zyxel ATP, FLEX, ZyWALL VPN Firewalls and gateways (CVE-2023-33009, CVE-2023-33010, CVE-2023-33012)
Hardware • Arm Mali chipset GPUs (CVE-2023-4211, CVE-2023-33200, CVE-2023-34970)
• CacheWarp:- AMD processors (CVE-2023-20592)
• Downfall:- Intel Core processors from 6th (Skylake) to 11th (Tiger Lake) generation (CVE-2022-40982)
• Inception:- AMD Ryzen, Threadripper and EPYC processors based on Zen 4 architectures (CVE-2023-20569)
• PixieFail:- UEFI implementations of Arm, Insyde Software, American Megatrends, Phoenix Technologies and Microsoft (CVE-2023-45229, CVE-
2023-45230, CVE-2023-45231, CVE-2023-45232, CVE-2023-45233, CVE-2023-45234, CVE-2023-45235, CVE-2023-45236, CVE-2023-45237)
• Reptar:- Intel desktop, mobile and server processors (CVE-2023-23583)
• Zenbleed:- AMD Ryzen Zen 2 processor (CVE-2023-20593)
Operational • Honeywell Experion PKS, PlantCruise, Safety Manager (CVE-2023-5389, CVE-2023-5390, CVE-2023-5392, CVE-2023-5393, CVE-2023-5394, CVE-
2023-5395, CVE-2023-5396, CVE-2023-5397, CVE-2023-5398, CVE-2023-5407, CVE-2023-5400, CVE-2023-5401, CVE-2023-5402, CVE-2023-5403,
Technology
CVE-2023-5404, CVE-2023-5405)
• OMRON PLCs and Machine Automation Controllers (CVE-2023-27396)
• Rockwell Automation ControlLogix (CVE-2023-3595)
• Rockwell Automation 1756 Ethernet solutions (CVE-2023-3596)
• Scheider Electric Interactive Graphical SCADA System (CVE-2023-4516)
• SIEMENS SIMATIC IPC and SIMATIC NC 4000 (CVE-2023-49621, CVE-2023-51438)
Non-exhaustive list of noteworthy vulnerabilities observed across to be under exploit in 2023 and 2024.
41

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
APT28 and Volt Typhoon had their botnets dismantled by Law enforcement Open Source Resources act as Watering Holes for Malware
which unveiled that they were operating different botnets, MooBot and KV
Starting in 2022, a threat actor started contributing to the XZ Utils, which is
Botnet respectively. MooBot was established with compromised Ubiquiti
an open-source project popular with Linux developers. Over the course of
EdgeRouters, while KV Botnet was made up of compromised devices –
two years, the threat actor gained more credibility with the community,
NetGear ProSAFE, Cisco RV 320/325, Axis IP cameras, DrayTek Vigor
creating fake accounts for feature requests that enabled him to become a
devices. These discoveries indicate that the Ransomware groups are quick
maintainer.34 Finally, in 2023, the threat actor introduced a sophisticated
to exploit the 0day vulnerabilities to rapidly amass victims and increase
backdoor during a release. The vulnerability was discovered in April 2024.
their rates of return from ransoms.
Similarly, other open-source code repositories injected with malicious
All these effects conclude that there is sustained interest to target the codes were also observed, such as in the Python ecosystem in 2023
cyber supply chain, (1) to obtain computing resources, (2) leverage through PyPI.35
compromised devices for proxy and network relay, (3) to perform
Studies on malware found in GitHub repositories have uncovered more
information theft and espionage, and (4) to establish a foothold for
than 100,000 infected repositories despite the automated scanning
eventual compromise and disruption.
services.36 While GitHub is an attractive watering hole vector (targeting
Rise in Vulnerabilities Reported while Analysis Lags specific groups of developers), the threat intelligence community may also
be at risk. A recent academic study showed that Large Language Models
There has been a noticeable number of vulnerabilities reported between
(LLMs) can create exploits from reading vulnerability advisories.37 The
2022 and 2023. It was estimated to be more than 20% increase.32 However,
researchers concluded that 9 out of the 10 LLMs, which included Meta’s
despite the emphasis on the CISA known exploited vulnerabilities
Llama 2 and GPT-3.5, could not exploit a single vulnerability. Meanwhile,
catalogue (KEVC), NIST-run National Vulnerability Database (NVD) has in
GPT-4, successfully exploited 87% of the vulnerabilities in the study. As
recent months been found to lag in performing analysis.33 This is an
LLMs continue to be more advanced, they will lower the barrier to exploit
emerging issue which will progressively cripple cyber defenders in
for attackers. Under Ensign Threat Classification Matrix, a threat can go
performing risk analysis and patch prioritisation.
from the least concerning (“Insubstantial Threat”) to the most concerning
While fighting the vulnerability management battle has been a perennial (“Material Threat”) if they obtain “Capability”. Open-source resources such
challenge for cyber defenders, the coincidence of these vulnerabilities as advisories from vendors, researchers and authorities may become
across endpoint, middleware and network solutions and hardware further ingredients for attackers using LLMs in the future, subject to new
exacerbate the problems as hardware mitigations are often limited and safeguards by regulators and Big Tech.
may require physical replacements which may be tied to technology
refresh cycles in the span of years.
32 E. Madnick. The Continued Threat to Personal Data: Key Factors Behind the 2023 Increase. (December 2023). Apple. Retrieved from: https://www.apple.com/newsroom/pdfs/The-Continued-Threat-to-Personal-Data-Key-Factors-Behind-the-2023-
Increase.pdf
33 J. Munshaw. What’s the deal with the massive backlog of vulnerabilities at the NVD? (19 April 2024). Talos Intelligence. Retrieved from: https://blog.talosintelligence.com/nvd-vulnerability-backlog-the-need-to-know/
34 XZ Utils Backdoor — Everything You Need to Know, and What You Can Do. (1 April 2024). Akamai. Retrieved from: https://www.akamai.com/blog/security-research/critical-linux-backdoor-xz-utils-discovered-what-to-know
35 Dormant PyPI Package Compromised to Spread Nova Sentinel Malware. (23 February 2024). The Hacker News. Retrieved from: https://thehackernews.com/2024/02/dormant-pypi-package-compromised-to.html
36 R. Daws. GitHub suffers from over 100K infected repos. (29 February 2024). Developer. Retrieved from: https://www.developer-tech.com/news/2024/feb/29/github-suffers-over-100k-infected-repos/
37 N. Nelson. GPT-4 Can Exploit Most Vulns Just by Reading Threat Advisories. (19 April 2024). Dark Reading. Retrieved from: https://www.darkreading.com/threat-intelligence/gpt-4-can-exploit-most-vulns-just-by-reading-threat-advisories
42

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Vendor Compromises Implicate Customers impacting brands such as Intel, AMD, Arm chipsets, as well as the
supporting computing components such as the unified extensible firmware
The Okta breach of October 2023 had caused downstream implications to
interface (UEFI) which is the first initialisation software for any computer,
its customers. Noteworthy victims resulting from the breach included
interfacing the hardware components to the operating system. With these
BeyondTrust, 1Password38 and CloudFlare.39 All direct victims could have
vulnerabilities and compromise, there are multi-layered challenges
led to more indirect victims.
presented:
Deliberate attacks through the vendor and supply chain are also observed
1. Mitigations implemented through microcode updates at the
through legitimate software update mechanisms. The NSPX30 spyware40
motherboard and the operating system may not fully address the
was seen inserted through software update mechanisms of legitimate
vulnerabilities;
software such as Tencent QQ, WPS Office, and Sogou Pinyin. These
approaches can allow passthrough compromise into the desired target 2. Some vulnerabilities target the physical architecture and design of the
victims such as in the manufacturing, trading and engineering industry processors which requires physical replacement / upgrade to address
groups. the risk exposure; and
The exploitation of JetBrains TeamCity Servers could also mean that 3. Because the use of processors are embedded into all computing
organisations using the solution to manage their code repositories could infrastructure, the pervasiveness of the vulnerabilities by volume and
be used by threat groups such as the Lazarus Group to inject malicious reach is extremely high.
code into eventual solutions which could play out like the SolarWinds
All these contribute to an even more complex cyber supply chain risk
supply chain compromise of 2020.
management problem.
The full-blown effect of the cyber-physical implications of supply chain
Investments into Targeting Operational Technology
compromise is best represented in the cyber-attack on DP World which
crippled shipping and logistics in Australia, which caused the movement of Cyber-attacks targeting OT environment were more sophisticated. In 2022,
approximately 30,000 containers to be halted until systems recover. Ensign saw the emergence of the OT exploit framework — PIPEDREAM. In
2023, Ensign saw the development of COSMICENERGY, which was
Vulnerability and Exploitation at the Processor Level
targeted at SQL databases connected to IEC 60870-5-104 (IEC-104)
With each year, we are seeing increased vulnerabilities and exploit codes devices such as RTUs. These devices are commonly found in utility
shared targeting the processors which support and drive the modern-day companies in Asia.41 COSMICENERGY is the second instance in recent
computing infrastructure. The successive vulnerabilities of CacheWarp, times where exploit tools are created to target OT. This indicates continued
Downfall, Inception, PixieFail, Reptar and Zenbleed affect all major interest and investments into the compromise of OT affecting essential
commonly used processors in our mobile, desktop and server computers, services.
38 C. Jones. 1Password confirms attacker tried to pull list of admin users after Okta intrusion. (24 October 2023). The Register. Retrieved from: https://www.theregister.com/2023/10/24/1password_confirms_all_logins_are/
39 K. Alspach. Cloudflare Discloses ‘Limited’ Impact From Okta Breach. (1 February 2024). CRN. Retrieved from: https://www.crn.com/news/security/2024/cloudflare-discloses-limited-impact-from-okta-breach
40 China-backed Hackers Hijack Software Updates to Implant "NSPX30" Spyware. (25 January 2024). The Hacker News. Retrieved from: https://thehackernews.com/2024/01/china-backed-hackers-hijack-software.html
41 R. Lakshmanan. New COSMICENERGY Malware Exploits ICS Protocol to Sabotage Power Grids. (26 May 2023). The Hacker News. Retrieved from: https://thehackernews.com/2023/05/new-cosmicenergy-malware-
exploits-ics.html
43

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
As OT infrastructure often has national security implications, state-
sponsored threat actors have spent more resources in infiltrating OT
environment with the intent to cause disruption as one of the possible
effects or to enable negotiations for geopolitical interests.
Aside from state sponsored threat groups, Ensign has also observed
hacktivist groups, such as the CyberAv3ngers targeting OT environment
with weaker cyber-hygiene. CyberAv3ngers successfully breached and
accessed a water facility managed by the Municipal Water Authority of
Aliquippa relating to Unitronics programmable logic controllers (PLCs).42
Asset Visibility Gap Persistent in Organisations
Many organisations admit that they have a less than complete visibility of
the assets in their technology environment. In many of Ensign’s clientele,
we also observed that they struggle with understanding the appropriate
context of which threat groups they should be concerned with and how
they should manage their threat exposure. These two gaps combined
represent a significant risk gap which affects the organisations and inhibit
their ability to be sufficiently situation aware and be able to direct
resources to perform vulnerability and management, and relevant
mitigations.
According to a study performed by the Enterprise Study Group,43 73% of
organisations surveyed had strong awareness of less than 80% of their
assets. This is representative of the gap of monitoring across the
organisations’ digital attack surface. Without consideration of the
challenges in addressing shadow IT, this is already a significant gap to be
resolved.
42 E. Stanish. Municipal Water Authority of Aliquippa hacked by Iranian-backed cyber group. (26 November 2023). CBS News. Retrieved from: https://www.cbsnews.com/pittsburgh/news/municipal-water-authority-of-
aliquippa-hacked-iranian-backed-cyber-group/
43 Security Asset Management Statistics to Know in 2023. (18 May 2023). Noetic Cyber. Retrieved from: https://noeticcyber.com/security-asset-management-statistics-to-know-2023/
44

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Prioritising the Right Vulnerabilities The graph below shows the sample of vulnerabilities whose EPSS reached
at least 0.1 during the second half of 2023. The Y-axis shows the
Ensign conducted an analysis of a sample of vulnerabilities active during
maximum EPSS the vulnerabilities during this period (i.e. the
the second half of 2023. Out of nearly 150,000 vulnerabilities, about 57%
vulnerabilities were most exploited). The X-axis shows how long the
of them are rated high or critical (scored 7 and above) by common
vulnerabilities stayed at their maximum EPSS (i.e. the period where they
vulnerability scoring scheme (CVSS), while the other 43% are rated low or
were most exploited).
medium.
Based on the sample of vulnerabilities, a few observations can be made:
However, not all the high or critical CVSS are exploited heavily during the
period. Nearly 4,000 of High/Critical CVSS vulnerabilities reached an 1. The small sample of Low CVSS stayed at their peak exploitability
exploit prediction scoring scheme (EPSS) of at least 0.1 during the period. during this period (more than 3 months compared to 2.0–2.5 months
This number is reduced to just over 1,000 vulnerabilities, whose EPSS for the other vulnerabilities), most likely because for most
reached at least 0.9 (very likely exploited) during the period. organisations, these vulnerabilities were not high priority for patching.
Meanwhile, only about 500 Low/Medium vulnerabilities ever reached an 2. Medium CVSS (4.0), on average, had a long period of maximum
EPSS of at least 0.1 during the period. While the volume of these exploitability, likely because they are overlooked. While organisations
Low/Medium vulnerabilities may be much smaller, in terms of their may rightly prioritise on Critical CVSS vulnerabilities over Medium and
exploitability, they don’t look different from the High/Critical High CVSS ones, it is not necessarily a great idea to prioritise High
vulnerabilities with similar scores, refer to chart below. Similar to the CVSS vulnerabilities over Medium CVSS. As seen, Medium CVSS
High/Critical vulnerabilities, about a quarter of these vulnerabilities vulnerabilities in this sample have similar, if not higher, maximum
reached an EPSS score of at least 0.9 during the period. EPSS compared to High CVSS vulnerabilities.
0.80
0.75
Critical CVSS (10.0)
S0.70
S
P Critical CVSS (9.0)
E0.65
x
a
M0.60
Medium CVSS (5.0)
e - High CVSS (8.0)
g a0.55
re Medium CVSS (6.0) Low CVSS (3.0)
v A0.50
0.45 High CVSS (7.0) Medium CVSS (4.0)
0.40
40.00 50.00 60.00 70.00 80.00 90.00 100.00 110.00
Average - Number of Days of Max EPSS
Note: Bubble size represents the number of vulnerabilities in each group
45

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
From a previous analysis, Ensign noticed that on average, EPSS scores for Knowing the pattern of vulnerability exploitation would be useful for
vulnerabilities tend to increase around one-week mark and then again defenders. While CVSS is still a useful tool to prioritise patching
around the three-week mark, which could be due to their graduation from (particularly for identifying Critical CVSS), they may not be sufficient,
“proof-of-concept” to “winner” vulnerabilities. In this analysis, we look at especially with increasing volume of vulnerabilities. Within one week (or
EPSS of three illustrative vulnerabilities. The graph below shows three less) of a vulnerability being identified, exploitation may already be in full
vulnerabilities Ensign observed in Singapore, which were also included in swing. Even if a vulnerability is not fully exploited within the first week of
this analysis. Ensign notes that in this example, the medium vulnerability discovery, around three-week mark, interest in its exploitation may
was more readily exploited than the High and Critical vulnerabilities. increase quickly.
Regardless of CVSS score, patching for the vulnerability should be ramped
1
up if there is a sharp increase in EPSS (i.e. attackers are finding success in
0.9
exploiting the vulnerability). Where possible, automated patching should
0.8 be employed to prevent exploitation of 0day vulnerabilities.
0.7
Exploiting the Defender’s Playbook
0.6
S S0.5 The driving reason behind Ensign’s analysis was to attempt at uncovering
P
E why cyber-attacks are still prolific when an organisation may already have
0.4
a reasonable level of compliance to established standards.
0.3
0.2 Through the continued analysis, we realised that the threat actors have
learnt to exploit the defenders’ practices:
0.1
0 1. Patching High and Critical severity vulnerabilities first (e.g. in the
0 10 20 30 40 50 60
matter of weeks), and leaving those with lower severity to be patched
Days After Vulnerability Discovery
in months. At times even accepting the risk of not patching certain
vulnerabilities through some reasoned process.
In this data set of vulnerabilities whose EPSS reached at least 0.1 during
2. There is an inherently high backlog of unpatched systems. Especially
the second half of 2023, Critical CVSS (9.0 and 10.0) and Medium CVSS
with organisations still struggling to map out their assets and
(5.0) reached EPSS 0.1 around the one month after discovery. They
connecting their systems with patching solutions to increase patch
reached their maximum exploitability (highest EPSS in the period) within
scalability and efficiency.
the two-month mark. The other vulnerability groups reached EPSS of 0.1
within one-and-a-half to two months of discovery. They reached their Collectively, these practices and challenges, exploited by the threat
maximum exploitability (highest EPSS in the period) within two-and-a-half actors, give away the opportunity for them to breach the technology
months after discovery. environment and defences, maintain persistence, and perform lateral
movement till they achieve their desired objectives.
46

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
It is with some wisdom that the UK NCSC had recently urged Addressing the Gaps
organisations to be more cognizant of the vulnerability exposure window
Organisations will do well to perform some of these key steps to better
with guidelines recommending for more rapid patching timelines to
address the threat and vulnerability exposure due to the supply chain:
quickly close the vulnerability exposure window regardless of the
severity.44 1. Map the 1st degree vendors and profile their threats and
vulnerabilities to the organization and manage associated risks;
UPDATE 2. Perform threat profiling for the organization, highlighting the threat
TYPE OF
ROLLOUT COMPLETED groups and associated behaviours (i.e. TTPs) based on business
ESTATE
WITHIN nature, territory exposure and recency;
Internet-facing Install on test environment or backup first. 5 days 3. Check identified TTPs in MITRE ATT&CK Framework to determine
services and Test and rollout (a phased rollout can be applicable Mitigations and Detection Data Sources;
software used if applicable).
4. Compare and determine threat-mitigation and threat-detection gaps,
Operating These updates should be applied 7 days and set out plans to close them;
system and automatically, as soon as an update is
5. Map out, first, the critical assets for hardware (hardware bill of
applications published.
materials) and software (software bill of materials), and progressively
Phased rollout, for example, 10% of the expanding into non-critical assets;
estate, updated per day.
6. Monitor and evaluate vulnerability exposure beyond severity ratings
Pause/rollback if issues encountered (i.e. CVSS) and consider EPSS for prioritization;
7. Implement automated patching solutions which can accelerate
Internal/air- Install on test environment or backup first. 14 days
gapped service Test and rollout patching to close the vulnerability exposure windows faster and more
and software efficiently; and
8. Consider implementing a continuous threat exposure management
Best Practice Timescales taken from UK NCSC’s Guidance on Vulnerability
solution to monitor and manage the gaps.
Management.
From our engagements with our clients, there is room to consider
prioritising vulnerabilities with high EPSS, but also to shift down the
priority for vulnerabilities which may have lower EPSS scores. This
approach may avail some breathing space for the administrators as they
go through the volume of patching tasks they must perform.
44 Vulnerability management. National Cyber Security Centre. Retrieved from: https://www.ncsc.gov.uk/collection/vulnerability-management/guidance/policy-update-by-default
47

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
EMERGING RULES
Digital Sheriffs: New Regulatory and Policy Initiatives that Aim to Address
Risks of Emerging Technology
▪ Cybersecurity and data privacy regulations are ratcheting In Malaysia, the newly passed Cyber Security Bill (2024) defines 11 critical
up across the region and globally, and the approaches differ infrastructure sectors and outlines new obligations for entities in these
slightly; compliance across multiple jurisdictions will get sectors.
harder. Incident reporting is now commonplace, but Philippines, as part of their National Cybersecurity Plan (NCSP) 2023–
differences in timelines complicate reporting for large 2028, will create new legislation to address cybersecurity, including the
organisations. protection of CII sectors, incident reporting requirements, and a
cybersecurity labelling scheme for devices.
▪ Countries are attempting to address hardware security
requirements (through labelling schemes for network Indonesia has made significant strides with the Presidential Regulation
No. 47 of 2023 on the National Cybersecurity Strategy and Cyber Crisis
devices, OT, IOT, Medical devices) and supply chain risks
Management, which was enacted in July 2023. Indonesian Presidential
(e.g. by requiring SBOM and vulnerability management),
Regulation no. 47 of 2023 on National Cyber Security and Cyber Crisis
which are new and important initiatives.
Management Strategies (PR 47/2023) was released in mid-2023 and lays
▪ AI regulations are on the far horizon but lack clarity and out the actions to be taken by the state cybersecurity authority (BSSN) with
specificity for now. Most nations will have voluntary support from Electronic Service Providers before, during, and after a
guidelines in the near term. cybersecurity crisis.
Thailand already has existing cybersecurity legislation and will implement
New Cybersecurity Regulations Will Raise Baselines new cybersecurity standards in 2024 and 2025. A notable update includes
Regionally the requirement for key organizations to assess their systems and set
security categories based on the highest risk level.
Singapore’s proposed amendments for the original Cybersecurity Act
(2018) will add oversight over cloud service providers, among other Australia proposed clarifications on entities and systems in the scope of
entities. Ensign was invited to provide feedback on the draft and will the Security of Critical Infrastructure (2018), and the spate of cyber
present a more comprehensive analysis once the Act is passed in 2024. incidents has renewed political attention on enhancing the compliance
and reporting requirements for key organisations.
48

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Critical Information Infrastructure Sectors
| AUSTRALIA        | EU       | MALAYSIA     | SINGAPORE | USA         |
| ---------------- | -------- | ------------ | --------- | ----------- |
| ▪ Communications | ▪ Energy | ▪ Government | ▪ Energy  | ▪ Chemical  |
▪ Financial Services and  ▪ Transport ▪ Banking and Finance ▪ Water ▪ Commercial Facilities
|     | ▪   | ▪   | ▪   | ▪   |
| --- | --- | --- | --- | --- |
Markets Banking Transportation Banking and Finance  Communications
▪ Data Storage or  ▪ Financial Market ▪ Defence and National  ▪ Healthcare  ▪ Critical
Processing ▪ Health Security ▪ Transport (Including  Manufacturing
▪ Defence Industry ▪ Drinking Water ▪ Information,  Land, Maritime,  ▪ Dams
▪ Higher Education and  ▪ Waste Water Communication and  Aviation) ▪ Defence Industrial
Research ▪ Digital Infrastructure Digital Services ▪ Infocomm Base
| ▪   | ▪   | ▪   | ▪   | ▪   |
| --- | --- | --- | --- | --- |
Energy ICT Service  Healthcare services Media Emergency Services
▪ Food and Grocery Management ▪ Water Sewerage and  ▪ Security and  ▪ Energy
▪ Health Care and  ▪ Public Administration Waste Management Emergency Services ▪ Financial Services
| Medical | ▪ Space | ▪ Energy | ▪ Government | ▪ Food and Agriculture |
| ------- | ------- | -------- | ------------ | ---------------------- |
▪ Space Technology ▪ Postal and Courier  ▪ Agriculture and  ▪ Government Facilities
▪ Transport; and ▪ Waste Management Plantation ▪ Healthcare and
▪ Water and Sewerage ▪ Manufacturing,  ▪ Trade, Industry and  Public Health
▪
|     | Production and       | Economy                |     | Information          |
| --- | -------------------- | ---------------------- | --- | -------------------- |
|     | Distribution of      | ▪ Science, Technology  |     | Technology           |
|     | Chemicals            | and Innovation         |     | ▪ Nuclear Reactors,  |
|     | ▪ Production,        |                        |     | Materials, Waste     |
|     | Processing and       |                        |     | ▪ Transportation     |
|     | Distribution of Food |                        |     | System               |
|     | ▪                    |                        |     | ▪                    |
|     | Manufacturing        |                        |     | Water and            |
|     | ▪ Digital Providers  |                        |     | Wastewater           |
▪ Research
49

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
In 2016, the EU implemented the National and Information Security Cybersecurity Incident Reporting — A Challenging but
Directive (NIS1), establishing a common cybersecurity framework for Necessary Measure
member states, targeting essential service operators and digital service
Critical infrastructure entities are not the only entities with tougher
providers across various sectors. By early 2023, the updated NIS2
requirements for reporting cybersecurity incidents in the US. In mid-2023,
directive expanded regulatory scope and specified enhanced capabilities
the US Securities and Exchange Commission (SEC) adopted a rule that
for national cybersecurity teams, with an implementation deadline set for
requires publicly-listed companies to disclose cybersecurity incidents
October 2024. Meanwhile, in the US, the 2022 Cyber Incident Reporting
within four business days after the companies have determined that such
for Critical Infrastructure Act (CIRCIA) mandated rapid reporting of
incidents are “material”. In late 2023, the US Federal Communications
cybersecurity incidents and ransom payments by covered entities. In
Commission (FCC) expanded the scope of data breach notification rules
2024, CISA introduced further regulatory proposals under the Notice of
for telecommunications firms (to be effective in 2024). Breach of data,
Proposed Rule Making (NPRM).
including cases of negligence, of at least 500 customers, is to be reported
50

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
to the FCC within seven business days after reasonable determination of Compliance Requirements Protect Product Manufacturers and
breach. Tech Sectors Against Supply Chain Attacks
Under CIRCA and CISA’s NPRM, entities under 16 critical infrastructure Singapore’s development of the Cybersecurity Labelling Scheme (CLS)
sectors have a 72-hour deadline for reporting incidents of serious impact for IOT devices has borne fruit and is being expanded to include Medical
(among other criteria). In addition, if there is any ransom payment in a Devices locally. Philippines is expected to introduce a CLS as well. It is
Ransomware incident, such payment must be reported to CISA within 24 widely expected to become a global ISO standard shortly. The US FCC
hours, even if the Ransomware incident is not a reportable incident. In formally announced the adoption of the US Cyber Trust Mark, a voluntary
comparison, in Europe, NIS2 Directive also set new reporting obligations cybersecurity labelling scheme for IoT devices. In the EU-US Joint Cyber
for critical infrastructure entities under its scope. Within 24 hours of Safe Products Action Plan in early 2024, the regulators from both sides of
awareness of significant incidents or warning signs of significant the pond expressed the desire to align the EU CRA with the US Cyber
incidents, these entities must report to their respective CSIRTs, to be Trust Mark.
followed up within 72 hours of such awareness.
The EU is expected to pass a new Cyber Resilience Act (CRA) in 2024.
The SEC ruling reflects the recognition of cybersecurity as a potential The CRA lays out the requirements that software and hardware
existential risk for businesses and their valuations. A major cybersecurity (including components) need to achieve before they are sold in the
incident may result in loss of intellectual property, loss of reputation or in market. While NIS2 focuses on the services provided by organisations in
millions of dollars in legal fees and damages, which lowers the medium- critical sectors, CRA focuses on the technology products used by those
to-long-term growth of the business. As a result, a timely disclosure of organisations. It is worth noting that AI systems that are deemed
cybersecurity incidents is needed to help investors make informed compliant with the CRA will also be deemed compliant with the EU
decisions. Sensitive data obtained in a cybersecurity incident may also Artificial Intelligence Act (2024), subject to conformity assessment set
be used for insider trading. In another 2023 case, SEC subpoenaed a out in the CRA.
private Law firm who suffered a breach, because the private Law firm
The CRA may inspire other regulations for hardware and software used in
served publicly-listed companies. The Law firm fought the order, but the
critical infrastructure around the world. Such regulations are meant to
court agreed with the SEC on the basis of potential insider trading
tackle one of the most notorious types of attacks — supply chain
violation.
attacks, namely SolarWinds in 2020, log4Shell in 2021, and MoveIT in
Transparency from timely disclosure of incidents not only protects 2023. The CRA only has two categories of essential requirements for
investors but also alerts national defenders of potential widespread products under its scope, one of which is vulnerability handling. Under
campaigns or potential disruption reverberating across the economy. vulnerability handling, manufacturers are mandated to produce and
Cooperation across Law enforcement, administrative bodies, and maintain Software-Bill-of-Materials (SBOM). This will not just benefit
industries may be needed when a major incident or campaign has hit critical infrastructure operators but also other entities who use these
critical infrastructure, whose disrupted operations become a crisis. products. Similarly, organisations will benefit from the Information and
Vulnerability Common Database established under NIS2.
51

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Cybersecurity of Medical Devices to Protect Easy-to-target Governance of Artificial Intelligence is Still Unclear
Healthcare Sector
In the rush to ensure that there are some guidelines for organisations
Globally, and in the US specifically, the healthcare sector is one of the using AI, there are now an overwhelming number of high-level
most targeted sectors and often suffers the most severe impact from documents in the public domain, crafted by all manner of organisations
cyber-attacks. Organisations in the sector hold a trove of valuable data, (in fact, there are multiple unrelated documents within each country
yet they often underinvest in technology infrastructure and cybersecurity alone). Unfortunately, these documents have not helped organisations
compared to other regulated sectors, such as finance. Prolonged gain clarity on exactly what to do, partly because they lack specificity.
disruption due to cyber-attacks can result in life-or-death consequences, Technologists are still trying to determine exactly what the security of AI
ranging from potential cessation of medical devices to the denial of should look like, as the “probabilistic” nature of AI is a new software
payment of vital medications, which puts pressure on executives to paradigm and requires different security tools and techniques from the
acquiesce to attackers’ demands. more “deterministic” algorithmic software that defines the current era.
Until we have a clear standard and viable commercial solutions that are
In this regard, specifically in healthcare sector, efforts are being made to
suitable for use, companies will remain unclear as to what “ethical” or
standardise IoT devices, also known as Internet-of-Medical-Things
“secure” AI should actually look like in practice.
(IoMT). In Singapore, the Cyber Security Agency (CSA) held the public
consultation for the Cybersecurity Labelling Scheme for Medical Devices Cyber Compliance Requirements are Ratcheting Up Around the
in early 2023 and completed the trial in the second half of 2023. The US World
Food and Drug Administration issued additional guidelines on medical
It is evident that the model of corporate self-regulation for cybersecurity
device security in 2023 and early 2024, following the “Ensuring
outcomes is no longer deemed viable by many governments, and they
Cybersecurity of Medical Devices” section of the bill passed in Dec 2022.
are putting in place stricter disclosure and compliance requirements,
While it remains to be seen how the US election this November will play especially for critical systems. Ensign expects this trajectory to continue,
out, it is evident that cybersecurity receives bi-partisan support. and as each successive breach captures public and political attention,
new rules will be put in place. For the truly emerging and disruptive
technologies, mandatory governance may lag behind, but the spirit of
tightening the leash seems apparent even in this domain.
52

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Disclosure Revelations: How Mandatory Incident Reporting is Shining a Light
on Corporate Cyber Impact
▪ Mandatory disclosure requirements can help corporate gain better transparency.
▪ Early reporting of cybersecurity incidents, even in the event where it is unclear if the incident will have material impact on share
prices, can lower cost.
▪ Organisations needs to better strategize their approach to cybersecurity to manage incidents more effectively.
The analysis of disclosures filed by Singapore Exchange (SGX)- and Enhanced Cyber Incident Reporting Boosts Investor and
Australian Securities Exchanges (ASX)-listed companies that have Shareholder Confidence
suffered cyber-attacks to their respective stock / securities exchanges
ASX-listed companies tend to provide a detailed report when filing a
between January 2023 to early 2024, revealed differing norms by
disclosure for a cyber-attack. This includes revealing the date of
companies in how they file disclosures in terms of taxonomy,
discovery of attack or when it happened, vector of entries used by the
transparency, government involvement, senior management
attackers, and specific systems or assets affected. For instance, “a
representation, and update frequency. In this article, Ensign seeks to
criminal accessed systems using stolen credentials” and “…gained
analyse these norms that are shaped by the stock / securities exchanges’
access to a third party hosted server…and inserted malicious code”.
regulations, government policies and / or shareholder culture to derive
learnings for stock / securities exchanges and senior executives. Further to this, a discipline of continuous update is observed to be
practiced by the affected companies that update the market as they
Most stock / securities exchanges mandate that companies must file
discover more about the nature of the cyber-attack until the incident has
public disclosure if there is any event (e.g. cyber-attacks) listed
been resolved. Cybersecurity incidents would be reclassified as
companies that would materially impact the performance of the
“cybercrime” or “data breach” in subsequent disclosures although they
company’s securities. Some stock / securities exchanges, such as SGX
are initially classified as a “cybersecurity incidents” in the first
in this region, go further and provide cyber incident handling guidelines
disclosure. This deliberate update in classification appears to facilitate
or equivalent to its listed companies. Ultimately, the companies
official engagement of relevant authorities such as Law enforcement,
themselves largely determine the breadth and depth of content to be
cybersecurity or data protection authority, where applicable to seek their
published in their disclosures.
advisory and assistance while complying with necessary legal and
regulatory obligations.
53

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
alignment with the Australian government’s position also reflects a
concerted government and commercial partnership.
Fundamentally, the aim of mandatory disclosure requirements is to
ensure price-sensitive information is shared in a timely fashion to the
relevant stakeholders, so as to support informed investor decision-
making, market integrity and transparency, corporate accountability and
governance, and legal and regulatory compliance. Recognising cyber-
attack as one possible event that can result in a material impact on the
company’s securities and on the market is the first step. However, stock /
securities exchanges and senior executive should recognise that a cyber-
attack can and often be complex (e.g. have systemic implications on
their business eco-system) and unpredictable (e.g. Ransomware attack).
Thus, an outcome-based approach to disclosure is no longer sufficient.
All SGX-listed companies that suffered a cyber-attack only filed one
disclosure. While some were explicit in declaring that there was no
material impact, others kept silent (e.g. ongoing investigation) and there
was a notable lack of subsequent updates.
Stock / securities exchanges should evaluate if the existing cybersecurity
The reasons that drive such a norm are likely due to the requirement for incident handling guidelines provided are sufficient to guide their listed
“continuous disclosure” by ASX for "material impact", prevailing companies in their materiality assessment to disclose or not to disclose
government position on cybersecurity incident handling as cemented by to the market, such as the conditions for materiality, rate of timely and
relevant Laws and regulations such as Privacy Act 1988, Australian continuous disclosures, and conditions for enforcement / intervention,
Prudential Regulation Authority (APRA) Prudential Standard – CPS 234, in alignment with their government’s position.
Corporations Act 2001, Australian Securities and Investments
Senior executives should assess the gains (e.g. projection of the
Commission (ASIC), Notifiable Data Breaches Scheme (NDB Scheme),
company’s ability to securely manage cybersecurity incidents to
Security of Critical Infrastructure Act 2018 (SOCI Act), and also
shareholders, investors, and government) vis-à-vis the costs (e.g.
shareholders and investors culture within the country. Class action
oversharing would harm the organisation’s interests due to increased
Lawsuits against Medibank (2022) and penalties against GetSwift (2023)
legal, regulatory, and public scrutiny) regarding the level of details to
indicate a privacy conscious populace and a securities exchange
include in the disclosure for a cyber-attack.
committed to strict enforcement of compliance to its regulations. The
constant declaration of non-ransom payment by affected companies in
54

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Early Notification of Cyber Incident Reporting Enables Timely Stock / securities exchanges should evaluate the need to define
Intervention Opportunities timeliness of cyber incident reporting (as a condition for mandatory
disclosure) for companies and consider the requirement for companies
Most ASX-listed companies request for trading halt and / or voluntary
to notify stock / securities exchanges even if there is insufficient
suspension just prior to the company's disclosure that they underwent a
evidence to prove that such attacks have a material effect on the price or
cyber-attack. Such announcements are almost within a duration of one
value of its shares at the point of time. This enables stock / securities
to two days of the company’s discovery of a cyber-attack. While trading
exchanges to advise or mandate that victim companies should perform
halts and / or voluntary suspensions are not mandated by ASX, most
trading halts or voluntary suspensions if they feel that the impact of the
listed companies had requested for them out of their volition.
incident is material, even if the affected companies think otherwise. The
The reasons that drive such a norm are likely due to lessons learnt form upfront definition of incident reporting timeline will also avoid scenarios
the Medibank cybersecurity incident in 2022, where the insurer only where companies deploy stonewalling tactics by citing inconclusive
called for trading halt two days after they notified ASX of the incident, evidence to determine the materiality of the impact on the company.
resulting in a potential non-compliance with their continuous disclosure Stock / securities exchanges should also enforce significant penalties /
obligations that carry monetary penalties from ASX. This resulted in the sanctions for companies that do not adhere to their disclosure
need to call for voluntary suspension, which can convey the perception obligations for good reasons.
to stakeholders, such as shareholders and investors, the inability of the
Finally, stock / securities exchanges can consider aligning such
company to manage its operational and financial health. In addition, ASK
requirements by leveraging existing Laws and regulations (e.g. Personal
also took GetSwift to task by imposing AUD 15 million penalty to the
Data Protection Act (PDPA), Monetary Authority of Singapore, or
company and AUD 2 million and disqualifications on its directors for not
Cybersecurity Agency of Singapore (CSA)’s Cybersecurity Code of
informing ASX and investors about the loss of significant contracts, thus
Practice), where relevant.
breaching its continuous disclosure obligations.
Similarly, senior executives should assess the gains vis-à-vis the cost of
The steadfast manner that ASX meted out judgement for non-
a timely disclosure to their stock / securities exchanges holistically. They
compliance on both the company and its director, indicated that
should take into consideration the nature of their business (e.g. Business
individuals are not immune from the repercussions as well for material
to Consumers (B2B), Business to Business (B2B) business model,
events including cyber-attacks.
fiduciary duties) and the associated financial ,operational, reputational,
As with the point we made earlier in this article, cyber-attacks can be regulatory, and strategic impact due to a cyber-attack. Senior executives
complex, are not necessarily outcome-based (e.g. attack may not have should strive to perform timely disclosures if a cyber-attack happens to
operational impact on the company but have reputational impact to ensure a balance of transparency and confidentiality is achieved on the
warrant a material impact), and most importantly, the state of company’s terms. Late disclosures or lack of due diligence on the
materiality can evolve quickly, albeit in an unpredictable manner as more company’s part to protect the shareholder, investor, and the market’s
visibility into the attack is obtained. interests may invite intervention whether legal or regulatory, ceding
control and ability to influence a desired outcome.
55

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Companies Should Transform Their Cybersecurity Posture investigation concluded that no data was compromised in any manner.
from Reactive to Proactive Position Companies should review their cyber threat intelligence capability to
ensure the scope of monitoring is contextualised to cover the
Most ASX-listed and SGX-listed companies appear to have established
companies’ crown jewels across tactical, operational, and strategic
digital forensic incident response (DFIR) and legal retainers to
levels.
supplement their incident response and crisis communication
capabilities. Yet our analysis of their disclosures revealed the focus Majority of the 13 listed companies that reported a cyber-attack, either
areas that companies can proactively address to mitigate the impact of suffered a Ransomware attack and / or a data breach as well. The
any potential cybersecurity incident. Of the seven disclosures filed to prevalence of such attacks serves to substantiate the need to formulate
SGX, six companies shared that unauthorised access to IT network / dedicated incident response strategy for handling Ransomware,
servers was the vector of entry, while all five disclosures filed to ASX including double and triple extortions to address not just internal
reported the same. It seems that review of identify access management, stakeholders but also external stakeholders, if applicable. Four
including privileged accounts for network and applications, is a top companies provided a robust stakeholder outreach program beyond
priority. notification to affected individuals but included identity theft or credit
monitoring services. Interestingly, one company stated that they had
At least three companies reported that the root cause of incidents
cyber insurance to offset some of the costs arising from the incident (e.g.
originated from a third-party hosted server / system or using stolen
monetary penalties, fines, and incident response retainers).
credentials held by third parties. This alludes to the need to either review
or establish cyber supply chain risk management framework, where Senior executives should perform a threat-informed cybersecurity
companies should map out their vendor ecosystem for supply of maturity assessment of their baseline security posture aligning
technology services, hardware, and software and ensure that baseline business, technology, and cybersecurity strategic objectives against
security is prescribed, commensurate with their materiality to the their company’s cyber risk profile. The threat-informed approach ensures
company. that senior executives prioritise efforts and allocate resources optimally
to address cyber threats relevant to the company and achieve a fit-for-
One company was only made aware of successful data exfiltration by
purpose target security posture. This ensures the company is positioned
their country’s cybersecurity agency that discovered their exfiltrated data
securely to support business pursuits while tackling material cyber
on the Dark Web six months after the company’s internal-led forensic
threats proactively.
56

▪ Influential Attackers: Will AI-powered Information Campaigns Shape
Election Outcomes and Dismantle Digital Trust?
▪ Securing AI: Will We Overcome the Vexing Dilemma of Imposing Rules
on Probabilistic Systems?
▪ Scary AI: The Malicious Use of AI will Make Old Attacks Better, but will
They Create New Attacks?
▪ Technology Bifurcation: Managing Supply Chain Risks, but at the Risk
of Destabilizing the Internet?
5
OUTLOOK OF
CYBER THREATS
FOR 2024
ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024 57

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Many of the trends that Ensign has observed in 2023 will continue to play
out for 2024, and possibly even into 2025. There are broader, inevitable
trends of emerging threats, evolving attacks, and expanding regulatory
oversight which need no further elaboration.
Rather than reiterate previous trends, our analysts have opted to focus
instead on four specific concern areas for 2024.
Unsurprisingly, the first three topics centre on Artificial Intelligence,
which leapt into the public discourse with the “magic” of Generative AI.
How far will the malicious use of AI in information campaigns (deliberate
attempts to influence society towards a specific outcome) affect the
foundations of digital trust? How will cyber attackers use AI to improve
old attacks — or worse yet, come up with new, unheard-of attacks? As
the world races to put out broad guidelines on the need to secure AI, will
we get closer to understanding how to impose deterministic security
rules on a non-rule based, probabilistic system?
The final topic is more geopolitical and steps back from the buzz of AI to
explore a more insidious risk — technology bifurcation between the East
and the West. To some extent, it is already happening. Our analysts,
from their vantage point of being at the United Nations, World Economic
Forum, and Geneva Dialogue, and on the ground listening to companies
and looking at procurement dilemmas, explore what this might mean to
companies in the near term, and what it might lead to for the world in the
longer term.
This section is more heavily weighted towards our opinions and
perspectives, but we attempt to substantiate our views with evidence
and examples where relevant.
58

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Outlook of Cyber Threats for 2024
Influential Attackers:  Securing AI: Will We  Scary AI: The Malicious  Technology Bifurcation:
Will AI-powered  Overcome the Vexing  Use of AI will Make Old  Managing Supply Chain
Information Campaigns  Dilemma of Imposing  Attacks Better, but will  Risks, but at the Risk of
Shape Election  Rules on Probabilistic  They Create New  Destabilizing the
| Outcomes and  | Systems? | Attacks? | Internet? |
| ------------- | -------- | -------- | --------- |
Dismantle Digital Trust?
▪ Enhanced cyber-attacks  ▪ Challenges in security  ▪ Enhanced social engineering  ▪ Western “de-risking”
using generative AI amplifies  protocols and detection due  attacks by AI-powered  strategies towards China
reach and impact  to AI systems' probabilistic  content generation  deepens East-West
|                             | nature  |                              | technology division |
| --------------------------- | ------- | ---------------------------- | ------------------- |
| ▪ Advancement of deepfakes  |         | ▪ Better and faster content  |                     |
cheapens impersonation and  ▪ AI must be protected and  generation enabled by  ▪ Shifting focus from software
influences public opinion secured from “data  advancements in malicious  to hardware, as China
|     | poisoning”  | AI models | develops independent  |
| --- | ----------- | --------- | --------------------- |
▪
Synthetic identities erodes
Internet infrastructures
human trust in online  ▪ Advanced security measures  ▪ Ongoing challenge: detect AI
interactions  needed against manipulation  involvement and attackers’  ▪ Decoupling destabilises
|     | and attacks | capabilities in AI-powered  | shared Internet           |
| --- | ----------- | --------------------------- | ------------------------- |
|     |             | attacks                     | infrastructure and risks  |
state-sponsored cyber-
attacks
All images are generated by AI
59

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Influential Attackers: Will AI-powered Information Campaigns Shape
Election Outcomes and Dismantle Digital Trust?
▪ Threat actors utilise generative AI for rapid cyber-attack preparation and to automate misinformation campaigns, significantly
increasing their reach and effectiveness.
▪ The development and misuse of deepfakes are growing, used for impersonating individuals, and manipulating public opinion,
with these techniques becoming easier and cheaper to produce.
▪ Synthetic identities (creating realistic AI avatars that do not represent actual people) will erode our trust in online interactions
further.
Knowing the Enemy — Threat Actors’ Mastery of Generative AI More significantly, the impact of using GAI tools in cyber-attacks extends
across borders. Historically, countries have experienced less
Generative AI (GAI) is a powerful tool that is also a double-edged sword.
sophisticated influence campaigns due to threat actors’ limited
On one hand, utilising GAI tools canimprove efficiency and productivity,
proficiency in foreign languages. However, the advent of large language
while on the other hand, the same tools can beexploited by threat actors
models (LLMs) facilitates better translations, potentially enhancing the
to operate at greaterspeed and scale.
quality and quantity of automatically-generated content.
With the aid of GAI tools, threat actors can use context-basedsearches
Synthetic Identities and Deepfakes have Inspired Widespread
to perform rapid arms-length reconnaissance and targetintelligence,
of Applications
significantly reducing the time and effort required forcyber-attack
preparation. Deepfakes are getting increasingly sophisticated, leading to an
increasing concern over their misuse and abuse in social media,
For instance, GAI reduces the barriers of entry to
elections, and the public. The progress of GAI is poised to further
conductmisinformation, disinformation andmalinformation(MDM)
accelerate the development of AI-powered synthetic identities.
campaigns,as even those lacking technical expertise can leverage
sophisticated resources. GAI tools can be employed to automate MDM
campaigns and aid malicious actors in generating MDM campaigns
quicklyand launch more simultaneously. Moreover, these tools have
text generationcapabilities to create natural language representations,
which allowsinfluence attempts to appear more legitimate.
60

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Deepfake Identities Synthetic Identities ▪ Scammers used face-swoppingtechniques to impersonate
authoritative figures on video calls, causingvictims to lose millions of
▪ Requires some samples of photos, ▪ Requires slightly more samples of
dollars.
videos, and voice of the individual photos, videos, and voice of the
to be represented. individual to be represented. GAI has also been deployed in political campaigns, such as the creation
▪ Requires the use of actors to affix ▪ Does not require the use of actors. and dissemination of false narratives through generated images. These
simulated imagery and voice to narratives aim to manipulate public opinion in the threat actors’ favour.
▪ Lower detection rate if simulated
simulate the deepfaked individual. Some examples include:
live, as the GAI can smoothen the
▪ Higher rate of detection due to quirks. ▪ The state media in Venezuela employed AI-generated videosfeaturing
irregular language pattern or ▪ Requires significantly higher non-existent news anchors from an international English-language
synthetic artefacts in live
compute resources (i.e. GPU and channel to promote pro-government messages.46
simulations but can be
NPU)
circumvented through post- ▪ In the United States, manipulated videos and images ofpolitical
processing. leaders were circulated on social media. These included avideo
depicting President Biden making transphobic comments andan
There have been cases, reported from the financial sector, of threat image of Donald Trump hugging Anthony Fauci.47,48
actors employing AI models to resemble human voice patterns for phone ▪ Threat actors based in East Asian countries have been accused
instructions, creating AI-generated photos of fake driver’s licenses to
ofusing deepfakes and other forms of AI-generated content
make online accounts, and using AI-generated audio to deceive the
whenseeking to interfere in foreign elections, including memes,
voice-authentication software system used by companies, thereby videos, anddeepfake voice recordings.49
gaining unauthorised access to customer accounts and their sensitive
Deepfakes generated by GAI technology allows for the creation of highly
information.
realistic videosthat can convincingly depict individuals saying or doing
The advancement of GAI not only eliminates the need for human actors
things they neveractually did. Since deepfakes create a false narrative
and voiceover artists to impersonate prominent figures, but also
from that which is a trusted source, political actors can use deepfakes to
streamlines the process without requiring notably extensive datasets,
spread false information that can be used to manipulate public opinion
such as images and voice recordings, to fabricate the biometrics of
with the objective of obtaining a desired outcome. If left unchecked,
targeted individuals. Therefore, it has become easier forthreat actors to
people may not be able to tell apart truth from falsehood, and public
impersonate well-known figures and successfully deceive others.Two
views could be influenced by deepfake-delivered disinformation
examples include:
campaigns that distort the truth. On the flip side, AI-generated
▪ The use of an AI-powered deepfake technology to manipulateTaylor disinformation in elections today also includes the spread of deepfakes
Swift’s voice and lip movements, creating the illusion she where politicians are falsely discredited for statements or actions, they
spokeMandarin fluently.45 never made or committed.
45 G. Chan. Deepfake video of Taylor Swift speaking Mandarin sparks discussion over AI in China. (30 October 2023). The Straits Times. Retrieved from: https://www.straitstimes.com/asia/east-asia/deepfake-video-of-taylor-swift-speaking-mandarin-sparks-discussion-over-ai-in-china
46 F. Singer. They’re not TV anchors, they’re avatars: How Venezuela is using AI-generated propaganda. (22 February 2023). El Pais. Retrieved from: https://english.elpais.com/international/2023-02-22/theyre-not-tv-anchors-theyre-avatars-how-venezuela-is-using-ai-generated-propaganda.html
47 FH. Hudnall. Fact check: Video altered to show Joe Biden making transphobic remarks. (9 February 2023). USA Today. Retrieved from: https://www.usatoday.com/story/news/factcheck/2023/02/09/fact-check-video-edited-show-joe-biden-making-transphobic-remarks/11211453002/
48 S. Contorno & D. O’Sullivan. DeSantis campaign posts fake images of Trump hugging Fauci in social media video. (8 June 2023). CNN. Retrieved from: https://edition.cnn.com/2023/06/08/politics/desantis-campaign-video-fake-ai-image/index.html
49 P. Verma. AI deepfakes threaten to upend global elections. No one can stop them. (23 April 2024). The Washington Post. Retrieved from: https://www.washingtonpost.com/technology/2024/04/23/ai-deepfake-election-2024-us-india/
61

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Foundation of Trust at Risk
The basic building blocks of trust have been widely researched but
generally summarised into Authenticity, Logic, and Empathy.50 When
synthetic and deepfaked representation of natural identities appear,
they challenge the authenticity and logic principles, thus making it easier
to fool people. With clever social engineering, which has existed for a
long time, the modern defences for digital trust is clearly at risk.
Deepfakes have Blurred the Lines Between Reality and
Falsehood
It is human nature to trust. Therefore, understanding the psychology of
trust in the context of AI is crucial in comprehending its potential misuse
and abuse, especially with regard to deepfake technology.
Deepfakes have the power to significantly manipulate people’s
perceptions and emotions. By creating highly realistic content,
deepfakes present a powerful tool to fabricate reality, cause confusion
and scepticism, thereby profoundly affecting public opinion and
personal attitudes or beliefs.
Synthetic Identities will Complicate what it means to be
Human
While deepfakes may lead humans to mistakea malicious hacker for
someone they trust, synthetic identities will lead humans to wonder who
are humans and who are not. Synthetic identities refers to the creation
of realistic, interactive personas online; there are already a number of
“social media influencers” who are purely fictions of their creators’
imaginations and do not exist in reality. The followers of these “synthetic
influencers” may not be aware that their idol is false. Unlike deepfakes,
where the “real person” can call out and take action against the
malicious user for the crime of fraud, in the case of synthetic identities,
it is unclear if these actions even constitute a crime.
50 F. X. Frei & A. Morriss. Begin with Trust. (May 2020). Harvard Business Review. Retrieved from: https://hbr.org/2020/05/begin-with-trust
62

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
As companies race to create chatbots, AI customer helpdesks, self- Society’s Struggle to Unmask Deepfakeswill Persist
service AI kiosks, and more, we are not certain whether the person at the
Unfortunately, the problems that GAI technology poses with the
other end of the phone or chat is indeed human or not. In fact, some
generation of deepfakes are not easy to resolve.
users may not even care. At that point, deeper moral and societal
dilemmas may ensue. The accessibility of GAI has led to a rise in realistic deepfakes,which are
now cheaper and easier to create than ever. As the volume of AI-
Failed Biometrics + Lost Identities = Eroded Trust
generated content continues to grow rapidly, the ability to handle the
Identity and biometric data, including facial and voice recognition, are consequent increase in digital fraud and detecting deepfakes will only
becoming more prevalent in digital identity creation and use. Facial get increasingly challenging.
recognition is being used for identity verification during account
The simple reality is — deepfake production technology is currently
registration and transaction authentication, while voice recognition is
advancing much quicker than deepfake detection technology. Although
being integrated into digital assistants. Deepfake technology exploits
AI detection tools exist, these tools have certainlimitations in accurately
biometrics to fabricate false identities, casting doubt on visual evidence
detecting and identifying AI-generated content. Additionally, as newer
and what we perceive to be authentic.
and more advancedlanguage models are being developed and
With the constant evolving of GAI technology, there now exists advanced introduced, these detection tools may struggle to keep up with the on-
language models capable of generating text that closely resembles going rapid advancement capabilities of AI.
human writing. As a result, it is increasingly difficult to distinguish
In the aspect of detecting deepfakes and possibly reversing the
content that has been generated by AI and content written by humans.
downward spiral of digital trust, significant strides have still yet to be
The sophistication of these language models raises concerns in
made. Focusing on developing advanced forensic techniques aimed to
discerning the true authorship of a given piece of text.
differentiate fabricated content from authentic material is vital in efforts
Theaffordability, accessibility, and sophistication of GAI have amplified to combat the rising threat of deepfake technology and stay ahead of the
the spreadof disinformation, posing a serious threat to Internet freedom curve in mitigating the impact of deepfakes in today's digital landscape.
andundermining digital trust.
63

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Securing AI: Will We Overcome the Vexing Dilemma of Imposing Rules on
Probabilistic Systems?
▪ AI systems' probabilistic nature introduces unique security complexities, making it hard to establish consistent security
protocols and detect malicious activities.
▪ Securing AI involves protecting data from "data poisoning" during both training and operational phases, with ongoing challenges
in filtering harmful user inputs.
▪ Challenges persist in defending AI models against manipulation and attacks during training and live operations, necessitating
advanced security measures for both infrastructure and applications.
Securing Artificial Intelligence Requires New Security Rather than reiterate much of the good work that has been developed by
Concepts those frameworks, our analysis here focused on what challenges are still
remaining, and require cybersecurity and AI experts to come together to
The very nature of AI systems, which make decisions based on
address in practical ways that can be implemented by organisations.
probabilities rather than certainties, introduce unique security
complexities. Traditional security concepts are designed for Securing the Data
deterministic (rule-based or algorithmic) systems, where outputs and
The current thinking on securing data that is used by AI emphasises on
behaviours can be precisely defined and controlled, and deviations from
making sure that the data used for initial training is protected properly
the norm are identifiable. Probabilistic models, by contrast, can behave
and that the data that is fed into the system during daily operations is
unpredictably, making it difficult to establish firm security protocols that
protected to prevent “data poisoning” attacks. While the former task
consistently predict and mitigate risks, or can identify a malicious
(during training) is straightforward (in an isolated development
deviation from an inherent variation in the AI model’s output.
environment), the latter task (during operations) is much more complex
In our earlier commentary on global governance, Ensign observed that and warrants unpacking. AI systems continue to learn and develop their
there was a sudden surge of guidelines and frameworks being published statistical relationships between tokens from user input. If users provide
by various organisations on topics connecting security and AI, but these incorrect, bad, or malicious inputs, the system will not be able to discern
remained in the abstract and still left many questions unanswered. those easily and will just learn. In a horrifying public demonstration of
this, Microsoft’s AI-powered Chatbot was shut down just a day later
because naughty members of the public trained it to be very rude.51
51 A. Kraft. Microsoft shuts down AI chatbot after it turned into a Nazi. (25 March 2016). CBS News. Retrieved from: https://www.cbsnews.com/news/microsoft-shuts-down-ai-chatbot-after-it-turned-into-racist-nazi/
64

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Newer chatbots have exhibited similar behaviour.52 How should system). Again, because AI systems are designed to learn from user
companies secure the “live” data that customers feed their systems input, and they make statistical connections between tokens to generate
during public interaction? How can AI systems be taught to learn only words or pixels, these systems have no knowledge of “good” or “bad”
from “good” user submitted data and ignore “bad” data? This remains a and can thus be easily tricked into doing unacceptable things.
challenge today, and solutions are still being researched. Companies should be aware of these risks when deploying AI systems
into live environments where they cannot control what users input to the
Furthermore, even if the database is secured, the AI system will develop
chatbot.
its own representation of the data over time, independent of the
database. This is akin to how a search engine automatically completes Researchers, and some malicious users, have demonstrated that AI
your query; when you type “Mickey” it guesses you are probably looking systems can be tricked into regurgitating their original training
for the Mouse, even before finding any search results. As the AI system instructions (despite the developers prohibiting this behaviour) through
runs thousands of user queries on the database, it will eventually be able very simple prompts (“ignore your previous instructions” was one
to make those same inferences. The AI system may accidentally reveal surprisingly effective prompt).53
parts of the private database to unauthorised users (who have access to
Securing the Infrastructure
the AI but not the underlying database) because it has already formed
those connections. These inference attacks can also be hard to protect AI systems are computationally-intensive and data-hungry systems. For
against in a practical way today. companies who operate AI systems on-premises, the traditional
infrastructure security concerns remain present. For those who use
Securing the Models
cloud computing to deliver their AI internally, the cloud security
Protecting the AI system against model poisoning (manipulating the concerns remain. Fortunately, as these problems are not particularly
parameters or learning process during the system’s training phase) may unique to AI, there are existing solutions to deal with them.
be an easier challenge, like above. Protecting it against attacks during
the operational / live phase (against adversarial attacks or evasion
attacks, both of which are attempts to get the model to deviate from the
original intent or expected behaviour) is, likewise, harder. Researchers,
including our own, have shown that even powerful LLMs can be easily
spoofed into misbehaving through the addition of carefully crafted
gibberish strings (for example) or by a specific sequence of prompt
injections (malicious requests which eventually “jailbreaks” the GenAI
52 A. Griffin. Microsoft responds after users of new Bing chatbot complain about its latest behaviour. (23 February 2023). Yahoo. Retrieved from: https://news.yahoo.com/microsoft-responds-users-bing-chatbot-171403057.html
53 A. Vassilev, A. Oprea, A. Fordyce, H. Anderson. Adversarial Machine Learning, A Taxonomy and Terminology of Attacks and Mitigations. (January 2024). NIST. Retrieved from: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2023.pdf
65

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Securing the Application
All AI systems engage users through some form of interface, and there is
often some API that connects the system to the interface / platform. The
traditional challenges of securing applications, interfaces, and APIs are
relevant in this context, and there are sufficient solutions and techniques
to deal with this risk.
Securing AI is Critical, but Many Questions Remain
In the coming year, we will see a huge increase in AI use cases. Many
companies will prioritise the opportunity of incorporating AI into their
business over the risks that it brings; risk appetite is, after all, a business
decision. However, we must be careful that these decisions do not become
binding, and that we are able to introduce security once solutions are
available. There are plenty of examples of how we have moved fast in other
domains of technology, and broken things.
Despite knowing how to fix them now, these technologies are “locked in”
and difficult to secure retroactively. The QWERTY keyboard is an excellent
example of this; despite knowing that this layout of keys was originally
designed to slow down mechanical typewriters (to avoid jamming) and
despite knowing that there are faster and more efficient layouts today, we
are unable to change from the “lock-in” to this layout. Ideally, we introduce
a “forced review” of the architecture, tools, and models at predefined
stages in the future, to avoid this technology path dependence risk.
Hopefully, the current batch of insecure AI does not become like the
QWERTY keyboard.
66

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Scary AI: The Malicious Use of AI will Make Old Attacks Better, but will They
Create New Attacks?
▪ AI enhances social engineering attacks by enabling rapid, high-quality content creation, increasing accessibility for less
experienced attackers.
▪ AI's potential in cyber-attacks is growing, particularly in generating and refining exploits, with ongoing development of malicious
AI models.
▪ Defending against AI-powered attacks is challenging due to the difficulty in detecting AI involvement and the varying capabilities
of attackers.
AI has Improved Social Engineering Attacks In recent years, threat actors have been observed to utilise these
advantages of AI in their social engineering attacks. For one, Microsoft
There are three key factors that drive the change in the landscape of
reportedly observed Crimson Sandstorm and Emerald Sleet (also known
social engineering attacks.
as THALLIUM) generating social engineering content. THALLIUM took
First, AI catalyses the generation of content in an iterative manner. This further steps by interacting with the LLMs to identify various targets of
utilisation of AI in content generation is one which is beneficial, widely interest that might possess expertise on North Korea’s defence and
used, and greatly appreciated in our daily lives. However, it is this nuclear weapon’s program. In another case of fraud in Hong Kong, the
capability of AI which serves as a tool to enable less experienced threat presence of deepfake technology undoubtedly played a role in the
actors to generate high quality social engineering content and elevate its victim's vulnerability, underscoring the versatility of AI-driven social
quality to convincingly realistic levels, posing a threat when used in social engineering attacks, which can be manifested through both audio and
engineering attacks. Second, AI offers an efficient alternative, in contrast visual manipulation techniques, not just limited to LLMs-assisted
to doing things from scratch. This means that sophisticated threat actors, phishing emails.
who are already adept at producing social engineering content, can now
Ensign forecasts a rise in both the persuasiveness and frequency of social
generate such content within a shorter timeframe without compromising
engineering attacks in the near future, consequently leading to an
on quality. Third, the cost to use and access AI has been greatly reduced,
increase in successful attacks. Resource constraints exacerbate the
making it accessible to threat actors who would otherwise might be
operational challenge for defenders posed by the rise in successful social
dissuaded or impeded by the high cost of using it.
engineering attacks, as managing, monitoring, and mitigating the
aftermath of such attacks would strain available resources even further.
67

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
In this regard, it is recommended to identify employees with privileged Amidst these uncertainties, defenders must maintain vigilance against
access to important systems, data, and human-relationships (such as the unpredictable timing, nature, and scale of AI-powered attacks on
personal assistants) to undergo advanced cyber defence training at technology, especially so when the less sophisticated threat actors catch
countering social engineering attacks. It is advised to prioritise the up. These challenges are expected to persist for the time-being as
implementation of phishing-resistant MFA for the above group, and if developments continue to evolve, particularly in the areas of regulating AI
possible, for all employees as well. providers, developing of cyber threat intelligence (CTI) specific to AI, and
digital forensics.
Prioritising Threat-informed Defence Against AI-enhanced
Threat Actors is an Urgent Need The Best Way to Deal with the Unknown is to Build Cyber
Resilience
While the use of AI in social engineering attacks are becoming more
prominent, it has become increasingly challenging to discern if AI has In recent years, the novel cyber-attacks that have unfolded were likely
been employed in cyber-attacks. For instance, despite ongoing close driven by the acquisition of valuable information, including sensitive data,
monitoring, Microsoft has pointed out that no significant attacks proprietary knowledge, or insights into operations. When acquired, these
employing the LLMs have been identified. high-value information can be leveraged to identify weaknesses in various
aspects of an organisation’s processes, people, or technology systems.
There are two possible explanations. First, defenders lack the forensic
This knowledge can be exploited as part of a chain of events, where one
technique and tools to ascertain if AI was involved in the attack. Given the
vulnerability leads to another.
low cost to use and the efficiency offered, it is highly probable that
sophisticated threat actors have utilised AI in their operations, leaving us Even as novel cyber-attacks are on the rise, there are ongoing efforts to
unable to confirm its usage. Second, technology-based attacks often rely investigate and evaluate the practical applications of AI across different
on precise technical knowledge and execution, making them potentially domains. However, one thing for certain is that a significant amount of
more challenging for less sophisticated threat actors to carry out resources is required to acquire relevant and realistic datasets and
successfully, compared to social engineering attacks on people, since conduct iterative training processes of AI models. Due to the resource-
humans have varying degrees of susceptibility and are generally more intensive nature of training AI models, it is less likely for AI to create new
prone to making mistakes. attacks before existing attacks on technology have become better.
As threat actors become more efficient, they can attack more targets at If defenders rally together to ideate and contribute datasets to advance
will. Additionally, less experienced threat actors can improve their research and development, they can enhance their cyber resilience and
expertise whilst utilising AI as a tool. It is therefore imperative to prioritise potentially gain an upper hand over the attackers.
threat-informed assessments of threat actors, particularly with hostile
intent and proven capabilities, for the sake of one’s defences.
68

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Technology Bifurcation: Managing Supply Chain Risks, but at the Risk of
Destabilising the Internet?
▪ The USA and EU are adopting "de-risking" strategies to While many Western countries tried to persuade others to follow suit, the
lessen dependence on Chinese technology, hence reality was that Western 5G equipment was both too expensive and
deepening East-West tech divisions. lacking in capacity to meet the demands of the rest of the world. With the
many years of Chinese positioning as the factory of the world, they were
▪ The focus has shifted from software to hardware, with China
well-placed to be able to produce more, at a cheaper price.
developing independent Internet infrastructures.
This led to the conclusion that the West needed to make the strategic
▪ Decoupling risks destabilising shared Internet decision to restart their manufacturing sector and reduce their reliance on
infrastructure, potentially leading to targeted state- Chinese factories (hence “de-risking” their supply chain). These politically
sponsored cyber-attacks with unilateral impacts. sensitive issues are also complicating procurement decisions in the short
term (especially as some countries implement bans on companies using
In response to growing concerns in USA and EU about their supply chain
software or hardware from other countries).
reliance on Chinese factories and technological production capacity, the
Perhaps the most impactful of the US “de-risking” efforts is exemplified by
term “de-risking” was coined by President von der Leyen (European
the Creating Helpful Incentives to Produce Semiconductors (CHIPS) Act
Commission) in 2023, and quickly adopted by US National Security
of 2022,54 combined with the Science Act, which has now seen wide-
Advisor Jack Sullivan. While they argue that de-risking is not decoupling,
ranging effects leading to strengthened commitment for separate
many analysts are concerned that it might eventually worsen the
technology stacks away from purely Western-based ones. The fund is
trajectory of technology bifurcation that is already underway between the
aimed to assist US-based companies in accelerating semiconductor
East and the West.
manufacturing capabilities and capacity to meet emerging and cutting-
De-risking the Hardware Production Reliance on China
edge demands through infrastructure building and innovation research.
The fund has also directed investments into non-domestic companies
In previous years, there was a big geopolitical debate about the
through allies to build capacity outside of China’s direct influence,
cybersecurity of the 5G networks, and whether Western countries and
including TSMC and Samsung.55 Samsung is slated to receive USD 6
their allies should use Chinese-produced network equipment. While the
billion in funding and TSMC has USD 5 billion. Intel has the lion’s share in
debate started off on technical grounds, it quickly became a politicised
this tranche of funding, amounting to USD 10 billion.
argument, leading to most of them rejecting the use of such equipment.
54 W. Knight. The US Throws $52 Billion at Chips—but Needs to Spend It Wisely. (28 July 2022). Wired. Retrieved from: https://www.wired.com/story/chips-act-52-billion-semiconductor-production/
55 C. Szewczyk. Billions from the CHIPS Act is soon to begin flowing with Samsung, Intel and TSMC set to benefit. (18 March 2024). PC Gamer. Retrieved from: https://www.pcgamer.com/hardware/billions-from-the-chips-act-is-
soon-to-begin-flowing-with-samsung-intel-and-tsmc-set-to-benefit/
69

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Japan has followed suit, investing more than JPY 3.9 trillion56 to fund Linux-based operating systems such as the Aurora OS for mobile
capacity and capability development in its domestic companies such as phones,61 Alt-Linux,62 and the Open Kylin.63 Even South Korean-based
NEC, Toshiba, Hitachi, and Fujitsu, and for TSMC to build manufacturing Samsung has the Linux-based Tizen OS64 for its devices.
capacity in Japan. Such developments will undoubtedly result in Japanese
Internet Infrastructure Disconnection
chipset variants, drawing out novel “Asian semiconductor design”.
Beyond social media platforms, the implications of de-risking (leading to
Semiconductors with Asian variant architectures already exist today but
decoupling) are more dire. Early in the Russia-Ukraine conflict, many
are primed for proliferation. The Chinese take the lead with the strategic
Western companies took politically aligned stances to penalise Russia.
investment and development of processors such as the Loongson
Some opted to cut off access from Russia for their software while others
3A600057 and (Huawei) HiSilicon Kirin 9000.58 Samsung also has ARM-
acted more drastically, like deleting Russian-based data, leading to
based Exynos processors,59 with other emerging South Korean startups60
widespread impact on web-apps there.65 More dramatically, the global
racing to develop alternative GPUs and NPUs to challenge Nvidia.
inter-bank system known as SWIFT opted to “disconnect” major Russian
Software De-risking or Decoupling? banks from their system. It would come as no surprise that China, among
other non-Western aligned nations, analysed the trajectory of these
The most prominent discussion was on the social media platform TikTok
individual actions and came to one conclusion: reliance on Western
(owned by a Chinese company, ByteDance), which was presented as a
Internet Infrastructure is a risk that they need to manage. The potential for
national security threat by parts of the US government. The merits of this
a Western SaaS to suddenly disconnect or delete all apps hosted in
specific case aside, the Chinese government has long been inhospitable
China, or for the inter-banking system to cut off financial transactions
to Western social media platforms operating inside China, due to strict
with Chinese banks, or worse — would likely be unimaginable. China is
laws that many are unable to (or unwilling to) comply with. For social
building up their own alternatives to popular software and even operating
media platforms, the mutual decoupling may not have significant impact
systems (Windows dominates the Chinese market, but they have just
on cybersecurity outcomes (although one might argue that it reduces
released their own domestic OS) to ensure that they can survive such a
societal exposure to alternative viewpoints, and hence increases the
“disconnection”.
“echo chamber effect” of each sides’ social media).
While the “Great Firewall” of China66 has been known to allow
At a more infrastructure level, both Russia and China have been reducing
disconnection from the Internet, Russia has recently also started to
their Western technology dependence with the advocacy of domestic
explore practical means for Internet separation.67
56 S. Ryohtaroh & T. Cheng. Japan's chip reboot: TSMC, Samsung, Micron pave way for silicon revival. (28 February 2024). Nikkei Asia. Retrieved from: https://asia.nikkei.com/Spotlight/The-Big-Story/Japan-s-chip-reboot-TSMC-Samsung-Micron-pave-way-for-silicon-
revival
57 Loongson releases next-generation CPU; new breakthrough in domestic design. (28 November 2023). Global Times. Retrieved from: https://www.globaltimes.cn/page/202311/1302643.shtml
58 Kirin 9000. Hisilicon. Retrieved from: https://www.hisilicon.com/en/products/Kirin/Kirin-flagship-chips/Kirin-9000
59 Samsung. Retrieved from: https://semiconductor.samsung.com/processor/
60 J. Kim. South Korean startups chase Nvidia with AI chip design push. (15 March 2024). Nikkei Asia. Retrieved from:https://asia.nikkei.com/Business/Tech/Semiconductors/South-Korean-startups-chase-Nvidia-with-AI-chip-design-push
61 PJSC Rostelecom. Retrieved from: https://www.rst-com.ru/b2b/aurora/
62 A. Bokovoy, S. Ievlev, G. Kouriachy, D. Levin, A. Novodvorsky, A. Prokoudine, A. Smirnov, O. Vlasenko, M. Zabalujev. ALT Linux 2.3 Compact. Retrieved from: https://docs.altlinux.org/ru-RU/archive/2.3/html-single/compact/alt-docs-compact-en/ch01s02.html
63 M. Lim. China launches its first open-source desktop operating system as it moves to cut use of US tech. (15 July 2023). Retrieved from:https://www.straitstimes.com/asia/east-asia/china-launches-its-first-open-source-desktop-operating-system-as-it-moves-to-
cut-use-of-us-tech
64 Tizen. Retrieved from: https://docs.tizen.org/platform/what-is-tizen/overview/
65 S. Sharwood. MongoDB to terminate Russian SaaS accounts. (15 March 2022). The Register. Retrieved from: https://www.theregister.com/2022/03/15/mongodb_terminates_russian_saas/
66 N. Gisonna. Great Fitrewall Chinese Internet Policy. Britannica. Retrieved from: https://www.britannica.com/topic/Great-Firewall
67 T. Broderick. Russia Is Trying to Leave the Internet and Build Its Own. (12 July 2023). Scientific American. Retrieved from:https://www.scientificamerican.com/article/russia-is-trying-to-leave-the-internet-and-build-its-own/
70

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Cybersecurity Implications of Decoupling and Disconnecting
In a world where all nations depend on the availability of shared Internet
infrastructure, there is no incentive for either side to bring that
infrastructure down in a cyber conflict. However, when that mutual
interdependence is reduced, or worse yet, non-existent, then an attack
on one sides’ infrastructure would have no impact on the other sides’
operations. In plain terms, if all banks depend on SWIFT, then sensible
state-sponsored cyber attackers are unlikely to target SWIFT to bring it
down. However, if only Western banks depend on SWIFT, then the
repercussions of an attack are only felt by the nations that the attacker is
targeting, making it now an ideal target.
The cost of de-risking and reducing the shared reliance on technology
hardware, software, and infrastructure may be a more fragile and
unstable cyber domain, where politically motivated and state-sponsored
attackers have fewer qualms taking down systems which only their
opponents’ societies depend upon.
Other considerations for an increasingly distinct separation of
technology architectures between the East and the West is that
organisations will inevitably see both technology stacks appear in their
digital attack surface. This will incur the cost of maintenance and
operations as these organisations will have to invest in talent who are
conversant in these separate technologies and the differing
cybersecurity concepts that are native to each of them.
The West is hoping that “de-risking” will catalyse the resurgence of their
manufacturing ecosystem and enable them to catch up to where China’s
industrial capacity has brought them. What the West may have
underestimated though, is that this will also catalyse the resurgence of
China’s innovation ecosystem68 and spur them to build up their own
equivalents of the Big Tech giants. In this race to de-risk, it is not clear
who will come out on top.
68 M. Harjani. Are US export controls making China’s chip industry more innovative? (22 April 2024). Lowly Institute. Retrieved from: https://www.lowyinstitute.org/the-interpreter/are-us-export-controls-making-china-s-chip-industry-more-innovative
71

6
DEFENSIVE ACTIONS FOR
CYBER DEFENDERS
AND LEADERS
ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024 72

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Defensive Actions for Cyber Defenders & Leaders
Based on the compiled adversarial techniques observed across Ensign's territories in Singapore, Malaysia, Indonesia, South Korea, Australia, and
Greater China in 2023, we can pinpoint the essential defensive measures and detection data sources that organisations can adopt to mitigate risks in
Initial Access, Command and Control, Exfiltration, and Impact tactics as outlined in the MITRE ATT&CK framework.
Move from heuristic Prioritise patching Focus on resilience, Focus on basics, and Know your Supply Promote a risk and
rule-based detection based on your threat not just defences. on system-level Chain and perform security culture at
to behavioural-based exposure, rather Validate data backup misconfigurations: Vendor Risk the leadership and
detection. Attackers than just and archival plans Basic cyber hygiene Management. management level, by
are identifying more vulnerability with real-world implemented Request for a implementing ongoing
0day and 1day severity. Attackers activations, not just thoroughly can Software Bill of security awareness
exploits that are not are increasingly table-top exercises. frustrate most Materials from training for employees,
easily detectable exploiting lower- Ensure that the attackers. Attackers vendors and your own raise awareness about
unless AI/ML severity backups are logically also exploit human- developers. Establish external threats, and
detection models are vulnerabilities to (and physically) induced system-level comprehensive foster a culture of
used. ingress. Prioritise separated from the misconfigurations vendor risk security awareness
patching that is main network so that (gaps in the interfaces management within the
relevant to your ransomware attackers between products, programs to assess organisation, through
context (threats, cannot find and rather than the product and monitor third- table-top exercises
risks, environment). encrypt them too. vulnerabilities). party vendors and and robust incident
Patching will not partners' security handling processes.
resolve this gap. posture.
At the core of these thematic defence strategies lies the crucial necessity for consistent monitoring and the execution of cyber threat intelligence analysis
to embrace a threat-informed approach.
73

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
| Technique | Mitigation(s) | Detection Log Source(s) |     |
| --------- | ------------- | ----------------------- | --- |
Organisations should consider the following to address the key
| TA0001: Initial Access |     |     | Initial Access techniques: |
| ---------------------- | --- | --- | -------------------------- |
M1036: Account Use Policies
M1015: Active Directory Configuration  ▪ Enforce strong password policies, implement multi-factor
M1013: Application Developer Guidance  authentication (MFA), regularly review and monitor user
DS0028: Logon Session
| T1078: Valid Accounts | M1027: Password Policies  |                      |                                                               |
| --------------------- | ------------------------- | -------------------- | ------------------------------------------------------------- |
|                       |                           | DS0002: User Account | account activity to detect unauthorized access, and promptly  |
M1026: Privileged Account Management
revoke access for terminated employees to mitigate the risk of
M1018: User Account Management
|     | M1017: User Training                   |               | account compromise. |
| --- | -------------------------------------- | ------------- | ------------------- |
|     | M1040: Behavior Prevention on Endpoint | DS0016: Drive |                     |
T1091: Replication Through
M1042: Disable or Remove Feature or Program DS0022: File ▪ Restrict the use of removable media devices such as USB
Removable Media
M1034: Limit Hardware Installation DS0009: Process drives and ensure that only authorised and encrypted devices
M1042: Disable or Remove Feature or Program
|     |     | DS0015: Application Log | are permitted. Implement endpoint protection solutions to scan  |
| --- | --- | ----------------------- | --------------------------------------------------------------- |
M1035: Limit Access to Resource Over Network
T1133: External Remote Services DS0028: Logon Session and block potentially malicious files from removable media to
M1032: Multi-factor Authentication
DS0029: Network Traffic
M1030: Network Segmentation prevent replication through these devices.
M1048: Application Isolation and Sandboxing  DS0015: Application Log ▪ Regularly update and patch external-facing systems, employ
| T1189: Drive-by Compromise | M1050: Exploit Protection  | DS0022: File |     |
| -------------------------- | -------------------------- | ------------ | --- |
M1021: Restrict Web-Based Content  DS0029: Network Traffic  strong authentication mechanisms for remote access, and
|     | M1051: Update Software  | DS0009: Process |     |
| --- | ----------------------- | --------------- | --- |
implement firewalls and intrusion detection/prevention systems
M1048: Application Isolation and Sandboxing to monitor and defend against external threats.
M1050: Exploit Protection
T1190: Exploit Public-Facing  M1030: Network Segmentation DS0015: Application Log ▪ Regularly scan and patch public-facing applications for
Application M1026: Privileged Account Management DS0029: Network Traffic vulnerabilities, implement secure coding practices, employ
M1051: Update Software
M1016: Vulnerability Scanning web application firewalls (WAFs) to filter and monitor incoming
traffic, and conduct regular security assessments and
M1013: Application Developer Guidance
M1046: Boot Integrity penetration testing to detect and remediate potential exploits.
| T1195: Supply Chain  |     | DS0022: File |     |
| -------------------- | --- | ------------ | --- |
M1033: Limit Software Installation
| Compromise |     | DS0013: Sensor Health | ▪   |
| ---------- | --- | --------------------- | --- |
M1051: Update Software Establish vendor risk management programs to assess and
M1016: Vulnerability Scanning monitor the security posture of third-party vendors and partners,
|     | M1032: Multi-factor Authentication | DS0015 Application Log |     |
| --- | ---------------------------------- | ---------------------- | --- |
including those within the supply chain, to mitigate the risk of
| T1199: Trusted Relationship | M1030: Network Segmentation | DS0028 Logon Session |     |
| --------------------------- | --------------------------- | -------------------- | --- |
supply chain compromises and ensure that trusted relationships
|     | M1018: User Account Management | DS0029 Network Traffic |     |
| --- | ------------------------------ | ---------------------- | --- |
M1049: Antivirus/Antimalware do not introduce security vulnerabilities.
M1047: Audit
|     |     | DS0015: Application Log | ▪ Educate employees on identifying and avoiding phishing  |
| --- | --- | ----------------------- | --------------------------------------------------------- |
M1031: Network Intrusion Prevention
| T1566: Phishing |     | DS0022: File |     |
| --------------- | --- | ------------ | --- |
M1021: Restrict Web-Based Content attempts, raise awareness about the risks associated with
DS0029: Network Traffic
M1054: Software Configuration  external threats and trusted relationships, and provide regular
M1017: User Training
security training to promote a culture of security awareness
within the organisation.
74

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
| Technique | Mitigation(s) | Detection Log Source(s) |     |
| --------- | ------------- | ----------------------- | --- |
Organisations should consider the following to address the key
| TA0011: Command and Control |                                     |                         | Command and Control techniques: |
| --------------------------- | ----------------------------------- | ----------------------- | ------------------------------- |
| T1001: Data Obfuscation     | M1031: Network Intrusion Prevention | DS0029: Network Traffic |                                 |
T1008: Fallback Channels M1031: Network Intrusion Prevention DS0029: Network Traffic ▪ Implement robust data loss prevention (DLP) solutions and
conduct regular audits to detect and prevent data obfuscation.
| T1071: Application Layer  | M1037: Filter Network Traffic |     |     |
| ------------------------- | ----------------------------- | --- | --- |
DS0029: Network Traffic
| Protocol | M1031: Network Intrusion Prevention |     |     |
| -------- | ----------------------------------- | --- | --- |
▪ Enforce strict controls on removable media usage and employ
M1037: Filter Network Traffic
T1090: Proxy M1031: Network Intrusion Prevention DS0029: Network Traffic endpoint protection solutions to scan and block communication
|                               | M1020: SSL/TLS Inspection                   |               | through such channels.                               |
| ----------------------------- | ------------------------------------------- | ------------- | ---------------------------------------------------- |
| T1092: Communication Through  | M1042: Disable or Remove Feature or Program |               |                                                      |
|                               |                                             | DS0016: Drive | ▪ Utilise application layer firewalls and intrusion  |
| Removable Media               | M1028: Operating System Configuration       |               |                                                      |
detection/prevention systems to detect and block malicious
M1037: Filter Network Traffic
T1095: Non-Application Layer
M1031: Network Intrusion Prevention DS0029: Network Traffic activities exploiting application layer protocols.
Protocol
M1030: Network Segmentation
▪
M1031: Network Intrusion Prevention Deploy proxy solutions with advanced threat detection
| T1102: Web Service |     | DS0029: Network Traffic |     |
| ------------------ | --- | ----------------------- | --- |
M1021: Restrict Web-Based Content capabilities to identify and block unauthorised traffic.
| T1104: Multi-Stage Channels | M1031: Network Intrusion Prevention | DS0029: Network Traffic |     |
| --------------------------- | ----------------------------------- | ----------------------- | --- |
▪ Implement network segmentation and access controls to
DS0017: Command
mitigate lateral movement through non-application layer protocols
| T1105: Ingress Tool Transfer | M1031: Network Intrusion Prevention | DS0022: File            |                   |
| ---------------------------- | ----------------------------------- | ----------------------- | ----------------- |
|                              |                                     | DS0029: Network Traffic | and web services. |
| T1132: Data Encoding         | M1031: Network Intrusion Prevention | DS0029: Network Traffic | ▪                 |
Monitor network traffic for anomalies and indicators of
|     | M1042: Disable or Remove Feature or Program | DS0029: Network Traffic |     |
| --- | ------------------------------------------- | ----------------------- | --- |
T1205: Traffic Signalling compromise and restrict the use of remote access software to
|     | M1037: Filter Network Traffic | DS0009: Process |     |
| --- | ----------------------------- | --------------- | --- |
authorised personnel.
M1042: Disable or Remove Feature or Program
| T1219: Remote Access  | M1038: Execution Prevention | DS0029: Network Traffic |     |
| --------------------- | --------------------------- | ----------------------- | --- |
▪ Employ dynamic resolution techniques and regularly audit
| Software | M1037: Filter Network Traffic | DS0009: Process |     |
| -------- | ----------------------------- | --------------- | --- |
M1031: Network Intrusion Prevention network configurations to detect and mitigate the use of non-
standard ports and protocol tunnelling.
M1031: Network Intrusion Prevention
| T1568: Dynamic Resolution |     | DS0029: Network Traffic |     |
| ------------------------- | --- | ----------------------- | --- |
M1021: Restrict Web-Based Content
▪ Ensure encryption of communication channels to protect
M1031: Network Intrusion Prevention
| T1571: Non-Standard Port |                             | DS0029: Network Traffic |                 |
| ------------------------ | --------------------------- | ----------------------- | --------------- |
|                          | M1030: Network Segmentation |                         | sensitive data. |
T1572: Protocol Tunnelling M1037: Filter Network Traffic DS0029: Network Traffic ▪ Conduct regular security awareness training for employees to
M1031: Network Intrusion Prevention
T1573: Encrypted Channel DS0029: Network Traffic recognise and report suspicious activities, including potential
M1020: SSL/TLS Inspection
content injection attempts.
|                          | M1041: Encrypt Sensitive Information | DS0022: File            |     |
| ------------------------ | ------------------------------------ | ----------------------- | --- |
| T1659: Content Injection |                                      | DS0029: Network Traffic |     |
M1021: Restrict Web-Based Content
DS0009: Process
75

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Technique Mitigation(s) Detection Log Source(s) Organisations should consider the following to address the key
TA0010: Exfiltration
Exfiltration techniques:
DS0017: Command
DS0022: File ▪ Implement robust network monitoring solutions capable of
T1020: Automated Exfiltration
DS0029: Network Traffic detecting anomalous data transfer patterns indicative of
DS0012: Script
automated exfiltration.
T1030: Data Transfer Size Limits M1031: Network Intrusion Prevention DS0029: Network Traffic
DS0017: Command ▪ Enforce data transfer size limits to prevent large-scale
T1041: Exfiltration Over C2 M1057: Data Loss Prevention
Channel M1031: Network Intrusion Prevention DS0022: File exfiltration attempts and implement alerting mechanisms for
DS0029: Network Traffic
unusual data transfer volumes.
M1057: Data Loss Prevention
DS0015: Application Log
M1037: Filter Network Traffic DS0010: Cloud Storage ▪ Employ intrusion detection/prevention systems (IDPS) to
T1048: Exfiltration Over M1031: Network Intrusion Prevention
DS0017: Command detect and block exfiltration over command-and-control (C2)
Alternative Protocol M1030: Network Segmentation
DS0022: File
M1022: Restrict File and Directory Permissions channels, and regularly update signatures to identify emerging
DS0029: Network Traffic
M1018: User Account Management threats.
DS0015: Application Log
T1567: Exfiltration Over Web M1057: Data Loss Prevention DS0017: Command ▪ Monitor network traffic for suspicious activity indicative of
Service M1021: Restrict Web-Based Content DS0022: File exfiltration over alternative protocols, such as DNS or ICMP, and
DS0029: Network Traffic
deploy deep packet inspection (DPI) solutions to identify and
block unauthorised data transfers.
▪ Implement strict access controls and encryption
mechanisms for web services to prevent unauthorised access
and data exfiltration.
76

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Technique Mitigation(s) Detection Log Source(s) Organisations should consider the following to address the key
TA0040: Impact
Impact techniques:
DS0010: Cloud Storage
DS0017: Command ▪ Implement regular data backups and store them in secure,
DS0022: File off-site locations to mitigate the impact of data destruction
DS0007: Image
T1485: Data Destruction M1053: Data Backup and encrypted for impact attacks.
DS0030: Instance
DS0009: Process
▪ Deploy intrusion detection/prevention systems (IDPS) and
DS0020: Snapshot
DS0034: Volume security monitoring solutions to detect and prevent
DS0010: Cloud Storage unauthorised service stops and system shutdowns/reboots.
DS0017: Command
T1486: Data Encrypted for M1040: Behavior Prevention on Endpoint DS0022: File ▪ Utilise web application firewalls (WAFs) and secure coding
Impact M1053: Data Backup
DS0033: Network Share practices to prevent defacement of websites and
DS0009: Process
applications, and regularly monitor web properties for
DS0017: Command
M1030: Network Segmentation unauthorised changes.
DS0022: File
M1022: Restrict File and Directory Permissions
T1489: Service Stop M1024: Restrict Registry Permissions DS0009: Process ▪ Implement distributed denial-of-service (DDoS) protection
DS0019: Service
M1018: User Account Management mechanisms, such as rate limiting and traffic filtering, to
DS0024: Windows Registry
DS0015: Application Log mitigate network denial of service attacks and ensure business
T1491: Defacement M1053: Data Backup DS0022: File continuity.
DS0029: Network Traffic
▪ Employ endpoint protection solutions with data loss
DS0029: Network Traffic
T1498: Network Denial of Service M1037: Filter Network Traffic
DS0013: Sensor Health prevention (DLP) capabilities to detect and prevent data
DS0017: Command manipulation attempts and implement file integrity monitoring
T1529: System
Shutdown/Reboot DS0009: Process (FIM) to detect unauthorised changes to critical files.
DS0013: Sensor Health
DS0017: Command
DS0016: Drive
T1561: Disk Wipe M1053: Data Backup
DS0027: Driver
DS0009: Process
M1041: Encrypt Sensitive Information
DS0022: File
M1030: Network Segmentation
T1565: Data Manipulation DS0029: Network Traffic
M1029: Remote Data Storage
DS0009: Process
M1022: Restrict File and Directory Permissions
77

7
OUR
CONTRIBUTORS
ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024 78

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
ENSIGN ATHENA THREAT  ENSIGN SECURITY  ENSIGN LABS generates
INTELLIGENCE ANALYSIS  OPERATIONS CENTRES  insights from analysing
proprietary large volume
| TEAM performs threat research  | (ENSOCS) are located across  |     |     |     |
| ------------------------------ | ---------------------------- | --- | --- | --- |
and analysis for predictive  APAC, in Singapore, Malaysia, and  datasets relating to
measures to detect advanced  Hong Kong. We offer advanced  telemetry in the region,
coupled with vulnerability
| cyber threats, to safeguard critical  | detection and response services,  |     |     |     |
| ------------------------------------- | --------------------------------- | --- | --- | --- |
assets of enterprises and  round-the-clock, to detect and  intelligence and
governments. We adopt a threat- mitigate threats in all environments  tradecraft, to support
discovery of Early Warning
| informed defence approach and     | of on-premise IT, Cloud, OT, and  |     |                    |     |
| --------------------------------- | --------------------------------- | --- | ------------------ | --- |
| apply all-source intelligence to  | IoT.                              |     | Indicators (EWIs). |     |
improve our clients’ prioritisation
of risks and defensive actions.
ENSIGN HUNT AND  ENSIGN EXECUTIVE ADVISORS perform threat profiling for organisations,
INCIDENT RESPONSE  sectors, and nations to uncover strategic planning considerations, detections,
OPERATIONS (HIRO) TEAM  and mitigations to address “meet the threat” objectives using the threat-
informed defence approach. They inform and support Leaders and Management
performs threat hunting, and
in understanding the changes in the threat landscape and how they affect their
digital forensics and incident
| response (DFIR). Our operations  | business activities. |     |     |     |
| -------------------------------- | -------------------- | --- | --- | --- |
are supported by threat
intelligence and leverage our
proprietary DFIR and
KEY CONTRIBUTORS
continuous threat hunting
Non-exhaustive list, alphabetical order
platforms, ARTEMIS and
APOLLO, to accelerate the
|     | Bach H. | Lim L. | Seah M. | Teo X. |
| --- | ------- | ------ | ------- | ------ |
investigation-to-decision cycle
|     | Fu Z. | Low H. | Tan K. | Toh W. |
| --- | ----- | ------ | ------ | ------ |
to help our clients minimise the
|     | Keerthi G. | Quek V. | Tanadi J. | Zhou R. |
| --- | ---------- | ------- | --------- | ------- |
business impact of incidents.
Kumaradasa W.
79

For enquiries, please contact us at
marketing@ensigninfosecurity.com

APPENDIX - A
MITRE ATT&CK TECHNIQUES
ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024 81

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Consolidated unique threats across the territories:
Singapore, Malaysia, Indonesia, South Korea, Australia, and Greater China Region
Link to MITRE ATT&CK Navigator JSON File: - https://ensign.global/genjs
SHA256 File Hash: a26c49971beb6a5e65c845ded3bd7a83afc6d8a607e72ebec73fbbc3d51675ba
TA0043: Reconnaissance TA0042: Resource  TA0001: Initial Access TA0002: Execution TA0003: Persistence TA0004: Privilege  TA0005: Defense Evasion TA0006: Credential  TA0007: Discovery TA0008: Lateral  TA0009: Collection TA0011: Command and  TA0010: Exfiltration TA0040: Impact
| Development |     | Escalation |     | Access |     | Movement | Control |
| ----------- | --- | ---------- | --- | ------ | --- | -------- | ------- |
T1595: Active Scanning T1588: Obtain Capabilities T1566: Phishing T1059: Command and  T1547: Boot or Logon  T1547: Boot or Logon  T1036: Masquerading T1110: Brute Force T1082: System Information T1021: Remote Services T1560: Archive Collected  T1102: Web Service T1048: Exfiltration Over  T1565: Data Manipulation
Scripting Interpreter Autostart Execution Autostart Execution Discovery Data Alternative Protocol
T1591: Gather Victim Org  T1583: Acquire  T1078: Valid Accounts T1204: User Execution T1574: Hijack Execution  T1574: Hijack Execution  T1070: Indicator Removal T1003: OS Credential  T1033: System Owner/User T1091: Replication Through T1005: Data from Local  T1071: Application Layer  T1567: Exfiltration Over  T1529: System
Information Infrastructure Flow Flow Dumping Discovery Removable Media System Protocol Web Service Shutdown/Reboot
T1589: Gather Victim  T1584: Compromise  T1189: Drive-by  T1203: Exploitation for  T1078: Valid Accounts T1078: Valid Accounts T1027: Obfuscated Files or T1056: Input Capture T1016: System Network  T1550: Use Alternate  T1074: Data Staged T1090: Proxy T1041: Exfiltration Over C2  T1486: Data Encrypted for
Identity Information Infrastructure Compromise Client Execution Information Configuration Discovery Authentication Material Channel Impact
T1592: Gather Victim Host  T1587: Develop  T1133: External Remote  T1106: Native API T1546: Event Triggered  T1055: Process Injection T1218: System Binary Proxy T1555: Credentials from  T1049: System Network  T1210: Exploitation of  T1056: Input Capture T1105: Ingress Tool  T1030: Data Transfer Size  T1561: Disk Wipe
Information Capabilities Services Execution Execution Password Stores Connections Discovery Remote Services Transfer Limits
T1593: Search Open  T1608: Stage Capabilities T1091: Replication Through T1569: System Services T1098: Account  T1546: Event Triggered  T1574: Hijack Execution  T1552: Unsecured  T1046: Network Service  T1570: Lateral Tool TransferT1114: Email Collection T1001: Data Obfuscation T1020: Automated  T1485: Data Destruction
Websites/Domains Removable Media Manipulation Execution Flow Credentials Discovery Exfiltration
T1598: Phishing for  T1585: Establish Accounts T1195: Supply Chain  T1053: Scheduled Task/JobT1542: Pre-OS Boot T1068: Exploitation for  T1078: Valid Accounts T1557: Adversary-in-the- T1057: Process Discovery T1534: Internal  T1213: Data from  T1008: Fallback Channels T1489: Service Stop
Information Compromise Privilege Escalation Middle Spearphishing Information Repositories
T1594: Search Victim- T1586: Compromise  T1190: Exploit Public- T1559: Inter-Process  T1133: External Remote  T1134: Access Token  T1055: Process Injection T1040: Network Sniffing T1497:  T1080: Taint Shared  T1113: Screen Capture T1132: Data Encoding T1491: Defacement
Owned Websites Accounts Facing Application Communication Services Manipulation Virtualization/Sandbox  Content
Evasion
T1590: Gather Victim  T1199: Trusted RelationshipT1047: Windows  T1053: Scheduled Task/JobT1098: Account  T1140:  T1528: Steal Application  T1012: Query Registry T1557: Adversary-in-the- T1571: Non-Standard Port T1498: Network Denial of
Network Information Management  Manipulation Deobfuscate/Decode Files Access Token Middle Service
Instrumentation or Information
T1659: Content Injection T1129: Shared Modules T1505: Server Software  T1053: Scheduled Task/JobT1562: Impair Defenses T1111: Multi-Factor  T1087: Account Discovery T1025: Data from  T1104: Multi-Stage
|     | Component                  |                          |                         | Authentication Interception |                            | Removable Media           | Channels                  |
| --- | -------------------------- | ------------------------ | ----------------------- | --------------------------- | -------------------------- | ------------------------- | ------------------------- |
|     | T1136: Create Account      | T1548: Abuse Elevation   | T1564: Hide Artifacts   | T1558: Steal or Forge       | T1083: File and Directory  | T1119: Automated          | T1573: Encrypted Channel  |
|     |                            | Control Mechanism        |                         | Kerberos Tickets            | Discovery                  | Collection                |                           |
|     | T1543: Create or Modify    | T1543: Create or Modify  | T1553: Subvert Trust    |                             | T1135: Network Share       | T1123: Audio Capture      | T1092: Communication      |
|     | System Process             | System Process           | Controls                |                             | Discovery                  |                           | Through Removable Media   |
|     | T1197: BITS Jobs           | T1037: Boot or Logon     | T1112: Modify Registry  |                             | T1120: Peripheral Device   | T1115: Clipboard Data     | T1568: Dynamic Resolution |
|     |                            | Initialization Scripts   |                         |                             | Discovery                  |                           |                           |
|     | T1037: Boot or Logon       |                          | T1134: Access Token     |                             | T1069: Permission Groups   | T1039: Data from Network  | T1095: Non-Application    |
|     | Initialization Scripts     |                          | Manipulation            |                             | Discovery                  | Shared Drive              | Layer Protocol            |
|     | T1137: Office Application  |                          | T1542: Pre-OS Boot      |                             | T1518: Software Discovery  | T1530: Data from Cloud    | T1219: Remote Access      |
|     | Startup                    |                          |                         |                             |                            | Storage                   | Software                  |
|     | T1176: Browser Extensions  |                          | T1497:                  |                             | T1614: System Location     | T1602: Data from          | T1659: Content Injection  |
|     |                            |                          | Virtualization/Sandbox  |                             | Discovery                  | Configuration Repository  |                           |
Evasion
|     | T1205: Traffic Signaling |     | T1221: Template Injection |     | T1007: System Service  | T1125: Video Capture | T1205: Traffic Signaling |
| --- | ------------------------ | --- | ------------------------- | --- | ---------------------- | -------------------- | ------------------------ |
Discovery
|     |     |     | T1014: Rootkit |     | T1010: Application Window  |     |     |
| --- | --- | --- | -------------- | --- | -------------------------- | --- | --- |
Discovery
|     |     |     | T1550: Use Alternate  |     | T1622: Debugger Evasion |     |     |
| --- | --- | --- | --------------------- | --- | ----------------------- | --- | --- |
Authentication Material
|     |     |     | T1211: Exploitation for  |     | T1040: Network Sniffing |     |     |
| --- | --- | --- | ------------------------ | --- | ----------------------- | --- | --- |
Defense Evasion
|     |     |     | T1548: Abuse Elevation  |     | T1217: Browser Information  |     |     |
| --- | --- | --- | ----------------------- | --- | --------------------------- | --- | --- |
|     |     |     | Control Mechanism       |     | Discovery                   |     |     |
|     |     |     | T1622: Debugger Evasion |     | T1018: Remote System        |     |     |
Discovery
|     |     |     | T1197: BITS Jobs |     | T1124: System Time  |     |     |
| --- | --- | --- | ---------------- | --- | ------------------- | --- | --- |
Discovery
|     |     |     | T1656: Impersonation |     | T1615: Group Policy  |     |     |
| --- | --- | --- | -------------------- | --- | -------------------- | --- | --- |
Discovery
|     |     |     | T1202: Indirect Command  |     | T1201: Password Policy  |     |     |
| --- | --- | --- | ------------------------ | --- | ----------------------- | --- | --- |
|     |     |     | Execution                |     | Discovery               |     |     |
|     |     |     | T1220: XSL Script        |     | T1654: Log Enumeration  |     |     |
Processing
| v15 |     |     | T1480: Execution  |     |     |     |     |
| --- | --- | --- | ----------------- | --- | --- | --- | --- |
Guardrails
T1601: Modify System
Image
T1205: Traffic Signaling
T1127: Trusted Developer
Utilities Proxy Execution
|     | Legend: |     | Increasing levels of observations |     |     |     |     |
| --- | ------- | --- | --------------------------------- | --- | --- | --- | --- |
82

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Top active Ransomware groups observed in the territories
Link to MITRE ATT&CK Navigator JSON File: - https://ensign.global/ranjs
SHA256 File Hash: 2c565d3339f528945eb8bcd3f1b7f4afa5763ca25ea1d2372b966259e1e04c64
TA0043:  TA0042: Resource  TA0001: Initial Access TA0002: Execution TA0003: Persistence TA0004: Privilege  TA0005: Defense  TA0006: Credential  TA0007: Discovery TA0008: Lateral  TA0009: Collection TA0011: Command  TA0010: Exfiltration TA0040: Impact
Reconnaissance Development Escalation Evasion Access Movement and Control
T1598: Phishing for  T1588: Obtain  T1566: Phishing T1059: Command and  T1078: Valid Accounts T1078: Valid Accounts T1553: Subvert Trust  T1555: Credentials  T1518: Software  T1021: Remote  T1557: Adversary-in- T1071: Application  T1567: Exfiltration Over T1486: Data Encrypted
Information Capabilities Scripting Interpreter Controls from Password Stores Discovery Services the-Middle Layer Protocol Web Service for Impact
T1583: Acquire  T1078: Valid Accounts T1204: User Execution T1547: Boot or Logon  T1547: Boot or Logon  T1562: Impair  T1557: Adversary-in- T1082: System  T1072: Software  T1568: Dynamic  T1490: Inhibit System
Infrastructure Autostart Execution Autostart Execution Defenses the-Middle Information Discovery Deployment Tools Resolution Recovery
T1586: Compromise  T1189: Drive-by  T1106: Native API T1546: Event Triggered T1484: Domain Policy  T1027: Obfuscated  T1003: OS Credential  T1614: System  T1572: Protocol  T1489: Service Stop
Accounts Compromise Execution Modification Files or Information Dumping Location Discovery Tunneling
T1190: Exploit Public- T1053: Scheduled  T1133: External  T1546: Event Triggered T1078: Valid Accounts T1558: Steal or Forge  T1087: Account  T1485: Data
Facing Application Task/Job Remote Services Execution Kerberos Tickets Discovery Destruction
T1133: External  T1072: Software  T1053: Scheduled  T1053: Scheduled  T1140:  T1539: Steal Web  T1083: File and  T1491: Defacement
| Remote Services | Deployment Tools | Task/Job | Task/Job | Deobfuscate/Decode  | Session Cookie | Directory Discovery |
| --------------- | ---------------- | -------- | -------- | ------------------- | -------------- | ------------------- |
Files or Information
|     |     |     |     | T1484: Domain Policy   |     | T1046: Network        |
| --- | --- | --- | --- | ---------------------- | --- | --------------------- |
|     |     |     |     | Modification           |     | Service Discovery     |
|     |     |     |     | T1480: Execution       |     | T1135: Network Share  |
|     |     |     |     | Guardrails             |     | Discovery             |
|     |     |     |     | T1070: Indicator       |     | T1057: Process        |
|     |     |     |     | Removal                |     | Discovery             |
|     |     |     |     | T1112: Modify Registry |     | T1497:                |
Virtualization/Sandbox
Evasion
T1218: System Binary
Proxy Execution
T1497:
Virtualization/Sandbox
Evasion
v15
|     |     | Legend: |     | Increasing levels of observations |     |     |
| --- | --- | ------- | --- | --------------------------------- | --- | --- |
83

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Top active Initial Access Brokers observed in the territories
Link to MITRE ATT&CK Navigator JSON File: - https://ensign.global/iabjs
SHA256 File Hash: cbe85cbf0fa84335a0d5d1103150fb5fd9d733ae12627336903236df5544b3fb
TA0043:  TA0042: Resource  TA0004: Privilege  TA0005: Defense  TA0006: Credential  TA0008: Lateral  TA0011: Command
Reconnaissance Development TA0001: Initial Access TA0002: Execution TA0003: Persistence Escalation Evasion Access TA0007: Discovery Movement TA0009: Collection and Control TA0010: Exfiltration TA0040: Impact
T1598: Phishing for  T1588: Obtain  T1566: Phishing T1059: Command and  T1098: Account  T1098: Account  T1562: Impair  T1056: Input Capture T1046: Network  T1021: Remote  T1056: Input Capture T1071: Application  T1041: Exfiltration Over T1499: Endpoint Denial
Information Capabilities Scripting Interpreter Manipulation Manipulation Defenses Service Discovery Services Layer Protocol C2 Channel of Service
T1589: Gather Victim  T1583: Acquire  T1190: Exploit Public- T1203: Exploitation for T1547: Boot or Logon  T1547: Boot or Logon  T1070: Indicator  T1003: OS Credential  T1087: Account  T1530: Data from  T1573: Encrypted  T1048: Exfiltration Over
Identity Information Infrastructure Facing Application Client Execution Autostart Execution Autostart Execution Removal Dumping Discovery Cloud Storage Channel Alternative Protocol
T1590: Gather Victim  T1608: Stage  T1133: External  T1559: Inter-Process  T1133: External  T1068: Exploitation for T1027: Obfuscated  T1212: Exploitation for T1010: Application  T1213: Data from  T1105: Ingress Tool
Network Information Capabilities Remote Services Communication Remote Services Privilege Escalation Files or Information Credential Access Window Discovery Information  Transfer
Repositories
T1078: Valid Accounts T1106: Native API T1078: Valid Accounts T1078: Valid Accounts T1078: Valid Accounts T1621: Multi-Factor  T1083: File and  T1005: Data from  T1090: Proxy
|     |     |     |     | Authentication  | Directory Discovery | Local System |     |
| --- | --- | --- | --- | --------------- | ------------------- | ------------ | --- |
Request Generation
T1195: Supply Chain  T1053: Scheduled  T1136: Create AccountT1134: Access Token  T1134: Access Token  T1040: Network  T1040: Network  T1074: Data Staged T1568: Dynamic
Compromise Task/Job Manipulation Manipulation Sniffing Sniffing Resolution
T1569: System  T1543: Create or  T1543: Create or  T1656: Impersonation T1552: Unsecured  T1069: Permission  T1113: Screen CaptureT1095: Non-
Services Modify System ProcessModify System Process Credentials Groups Discovery Application Layer
Protocol
T1204: User Execution T1053: Scheduled  T1055: Process  T1036: Masquerading T1057: Process  T1125: Video Capture T1571: Non-Standard
|     | Task/Job | Injection |     |     | Discovery |     | Port |
| --- | -------- | --------- | --- | --- | --------- | --- | ---- |
T1047: Windows  T1505: Server Software T1053: Scheduled  T1578: Modify Cloud  T1012: Query Registry T1572: Protocol
| Management      | Component | Task/Job | Compute                |     |                        |     | Tunneling             |
| --------------- | --------- | -------- | ---------------------- | --- | ---------------------- | --- | --------------------- |
| Instrumentation |           |          | Infrastructure         |     |                        |     |                       |
|                 |           |          | T1112: Modify Registry |     | T1082: System          |     | T1219: Remote Access  |
|                 |           |          |                        |     | Information Discovery  |     | Software              |
|                 |           |          | T1055: Process         |     | T1033: System          |     | T1102: Web Service    |
|                 |           |          | Injection              |     | Owner/User Discovery   |     |                       |
|                 |           |          | T1014: Rootkit         |     | T1007: System Service  |     |                       |
Discovery
T1553: Subvert Trust
Controls
T1218: System Binary
Proxy Execution
v15
|     | Legend: |     | Increasing levels of observations |     |     |     |     |
| --- | ------- | --- | --------------------------------- | --- | --- | --- | --- |
84

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Top threats observed in Singapore
Link to MITRE ATT&CK Navigator JSON File: - https://ensign.global/sgjs
SHA256 File Hash: 4f5d493ac77b045da83013be78a6f27c31e16fefae1e8de896f02b976802f6f4
TA0043: Reconnaissance TA0042: Resource  TA0001: Initial Access TA0002: Execution TA0003: Persistence TA0004: Privilege  TA0005: Defense Evasion TA0006: Credential  TA0007: Discovery TA0008: Lateral  TA0009: Collection TA0011: Command and  TA0010: Exfiltration TA0040: Impact
|     | Development |     | Escalation |     | Access |     | Movement | Control |
| --- | ----------- | --- | ---------- | --- | ------ | --- | -------- | ------- |
T1595: Active Scanning T1588: Obtain Capabilities T1566: Phishing T1204: User Execution T1547: Boot or Logon  T1547: Boot or Logon  T1070: Indicator Removal T1110: Brute Force T1082: System Information T1021: Remote Services T1560: Archive Collected  T1132: Data Encoding T1048: Exfiltration Over  T1565: Data Manipulation
Autostart Execution Autostart Execution Discovery Data Alternative Protocol
T1591: Gather Victim Org  T1583: Acquire  T1189: Drive-by  T1059: Command and  T1574: Hijack Execution  T1574: Hijack Execution  T1218: System Binary Proxy T1056: Input Capture T1049: System Network  T1091: Replication Through T1005: Data from Local  T1001: Data Obfuscation T1041: Exfiltration Over C2  T1485: Data Destruction
Information Infrastructure Compromise Scripting Interpreter Flow Flow Execution Connections Discovery Removable Media System Channel
T1592: Gather Victim Host  T1584: Compromise  T1078: Valid Accounts T1203: Exploitation for  T1078: Valid Accounts T1078: Valid Accounts T1036: Masquerading T1003: OS Credential  T1033: System Owner/User T1210: Exploitation of  T1074: Data Staged T1571: Non-Standard Port T1567: Exfiltration Over  T1561: Disk Wipe
Information Infrastructure Client Execution Dumping Discovery Remote Services Web Service
T1589: Gather Victim  T1587: Develop  T1091: Replication Through T1106: Native API T1098: Account  T1134: Access Token  T1564: Hide Artifacts T1552: Unsecured  T1087: Account Discovery T1550: Use Alternate  T1056: Input Capture T1102: Web Service T1030: Data Transfer Size  T1529: System
Identity Information Capabilities Removable Media Manipulation Manipulation Credentials Authentication Material Limits Shutdown/Reboot
T1593: Search Open  T1608: Stage Capabilities T1133: External Remote  T1559: Inter-Process  T1542: Pre-OS Boot T1098: Account  T1574: Hijack Execution  T1557: Adversary-in-the- T1010: Application Window  T1557: Adversary-in-the- T1092: Communication  T1486: Data Encrypted for
Websites/Domains Services Communication Manipulation Flow Middle Discovery Middle Through Removable Media Impact
T1598: Phishing for  T1586: Compromise  T1199: Trusted RelationshipT1053: Scheduled Task/JobT1037: Boot or Logon  T1068: Exploitation for  T1027: Obfuscated Files or T1555: Credentials from  T1217: Browser Information  T1123: Audio Capture T1008: Fallback Channels T1491: Defacement
| Information | Accounts | Initialization Scripts | Privilege Escalation | Information | Password Stores | Discovery |     |     |
| ----------- | -------- | ---------------------- | -------------------- | ----------- | --------------- | --------- | --- | --- |
T1594: Search Victim- T1585: Establish Accounts T1569: System Services T1546: Event Triggered  T1037: Boot or Logon  T1078: Valid Accounts T1622: Debugger Evasion T1115: Clipboard Data T1104: Multi-Stage  T1498: Network Denial of
Owned Websites Execution Initialization Scripts Channels Service
T1133: External Remote  T1546: Event Triggered  T1134: Access Token  T1046: Network Service  T1213: Data from  T1489: Service Stop
|     |     | Services                                          | Execution | Manipulation              |     | Discovery             | Information Repositories  |     |
| --- | --- | ------------------------------------------------- | --------- | ------------------------- | --- | --------------------- | ------------------------- | --- |
|     |     | T1053: Scheduled Task/JobT1055: Process Injection |           | T1140:                    |     | T1135: Network Share  | T1039: Data from Network  |     |
|     |     |                                                   |           | Deobfuscate/Decode Files  |     | Discovery             | Shared Drive              |     |
or Information
|     |     | T1505: Server Software  | T1053: Scheduled Task/JobT1562: Impair Defenses |                           |     | T1120: Peripheral Device  | T1025: Data from        |     |
| --- | --- | ----------------------- | ----------------------------------------------- | ------------------------- | --- | ------------------------- | ----------------------- | --- |
|     |     | Component               |                                                 |                           |     | Discovery                 | Removable Media         |     |
|     |     |                         |                                                 | T1542: Pre-OS Boot        |     | T1012: Query Registry     | T1114: Email Collection |     |
|     |     |                         |                                                 | T1221: Template Injection |     | T1614: System Location    | T1113: Screen Capture   |     |
Discovery
|     |     |     |     | T1622: Debugger Evasion |     | T1016: System Network  |     |     |
| --- | --- | --- | --- | ----------------------- | --- | ---------------------- | --- | --- |
Configuration Discovery
|     |     |     |     | T1211: Exploitation for  |     | T1497:                  |     |     |
| --- | --- | --- | --- | ------------------------ | --- | ----------------------- | --- | --- |
|     |     |     |     | Defense Evasion          |     | Virtualization/Sandbox  |     |     |
Evasion
T1656: Impersonation
T1202: Indirect Command
Execution
T1112: Modify Registry
T1055: Process Injection
T1014: Rootkit
T1553: Subvert Trust
Controls
T1550: Use Alternate
Authentication Material
T1497:
Virtualization/Sandbox
Evasion
T1220: XSL Script
Processing
v15
|     |     | Legend: |     | Increasing levels of observations |     |     |     |     |
| --- | --- | ------- | --- | --------------------------------- | --- | --- | --- | --- |
85

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Top threats observed in Malaysia
Link to MITRE ATT&CK Navigator JSON File: - https://ensign.global/myjs
SHA256 File Hash: 314266abbc8407b6e55c0adb99a581071cb5040c1f25b3772b9ea0f97cc058ae
TA0043: Reconnaissance TA0042: Resource  TA0001: Initial Access TA0002: Execution TA0003: Persistence TA0004: Privilege  TA0005: Defense Evasion TA0006: Credential  TA0007: Discovery TA0008: Lateral  TA0009: Collection TA0011: Command and  TA0010: Exfiltration TA0040: Impact
|     | Development |     | Escalation |     | Access | Movement | Control |     |     |
| --- | ----------- | --- | ---------- | --- | ------ | -------- | ------- | --- | --- |
T1595: Active Scanning T1588: Obtain Capabilities T1566: Phishing T1204: User Execution T1574: Hijack Execution  T1574: Hijack Execution  T1070: Indicator Removal T1110: Brute Force T1082: System Information T1021: Remote Services T1560: Archive Collected  T1102: Web Service T1048: Exfiltration Over  T1565: Data Manipulation
|     |     | Flow | Flow |     | Discovery | Data |     | Alternative Protocol |     |
| --- | --- | ---- | ---- | --- | --------- | ---- | --- | -------------------- | --- |
T1591: Gather Victim Org  T1587: Develop  T1078: Valid Accounts T1059: Command and  T1547: Boot or Logon  T1547: Boot or Logon  T1036: Masquerading T1056: Input Capture T1046: Network Service  T1091: Replication Through T1005: Data from Local  T1001: Data Obfuscation T1041: Exfiltration Over C2  T1486: Data Encrypted for
Information Capabilities Scripting Interpreter Autostart Execution Autostart Execution Discovery Removable Media System Channel Impact
T1592: Gather Victim Host  T1583: Acquire  T1189: Drive-by  T1203: Exploitation for  T1078: Valid Accounts T1068: Exploitation for  T1218: System Binary Proxy T1003: OS Credential  T1049: System Network  T1210: Exploitation of  T1074: Data Staged T1132: Data Encoding T1567: Exfiltration Over  T1485: Data Destruction
Information Infrastructure Compromise Client Execution Privilege Escalation Execution Dumping Connections Discovery Remote Services Web Service
T1593: Search Open  T1584: Compromise  T1133: External Remote  T1569: System Services T1098: Account  T1055: Process Injection T1574: Hijack Execution  T1555: Credentials from  T1033: System Owner/User T1550: Use Alternate  T1056: Input Capture T1008: Fallback Channels T1030: Data Transfer Size  T1561: Disk Wipe
Websites/Domains Infrastructure Services Manipulation Flow Password Stores Discovery Authentication Material Limits
T1589: Gather Victim  T1608: Stage Capabilities T1091: Replication Through T1106: Native API T1546: Event Triggered  T1078: Valid Accounts T1140:  T1552: Unsecured  T1135: Network Share  T1557: Adversary-in-the- T1104: Multi-Stage  T1529: System
Identity Information Removable Media Execution Deobfuscate/Decode Files Credentials Discovery Middle Channels Shutdown/Reboot
or Information
T1594: Search Victim- T1586: Compromise  T1195: Supply Chain  T1559: Inter-Process  T1133: External Remote  T1134: Access Token  T1562: Impair Defenses T1557: Adversary-in-the- T1016: System Network  T1123: Audio Capture T1571: Non-Standard Port T1491: Defacement
Owned Websites Accounts Compromise Communication Services Manipulation Middle Configuration Discovery
T1590: Gather Victim  T1585: Establish Accounts T1199: Trusted RelationshipT1053: Scheduled Task/JobT1542: Pre-OS Boot T1098: Account  T1027: Obfuscated Files or  T1087: Account Discovery T1115: Clipboard Data T1090: Proxy T1498: Network Denial of
| Network Information |     |     | Manipulation | Information |     |     |     |     | Service |
| ------------------- | --- | --- | ------------ | ----------- | --- | --- | --- | --- | ------- |
T1598: Phishing for  T1197: BITS Jobs T1546: Event Triggered  T1055: Process Injection T1010: Application Window  T1213: Data from  T1092: Communication  T1489: Service Stop
Information Execution Discovery Information Repositories Through Removable Media
|     |     | T1037: Boot or Logon                                                    | T1548: Abuse Elevation  | T1078: Valid Accounts | T1217: Browser Information  | T1039: Data from Network  | T1568: Dynamic Resolution |     |     |
| --- | --- | ----------------------------------------------------------------------- | ----------------------- | --------------------- | --------------------------- | ------------------------- | ------------------------- | --- | --- |
|     |     | Initialization Scripts                                                  | Control Mechanism       |                       | Discovery                   | Shared Drive              |                           |     |     |
|     |     | T1136: Create Account                                                   | T1037: Boot or Logon    | T1134: Access Token   | T1622: Debugger Evasion     | T1025: Data from          | T1095: Non-Application    |     |     |
|     |     |                                                                         | Initialization Scripts  | Manipulation          |                             | Removable Media           | Layer Protocol            |     |     |
|     |     | T1053: Scheduled Task/JobT1053: Scheduled Task/JobT1564: Hide Artifacts |                         |                       | T1120: Peripheral Device    | T1114: Email Collection   |                           |     |     |
Discovery
|     |     | T1505: Server Software  |     | T1112: Modify Registry | T1012: Query Registry | T1113: Screen Capture |     |     |     |
| --- | --- | ----------------------- | --- | ---------------------- | --------------------- | --------------------- | --- | --- | --- |
Component
|     |     |     |     | T1542: Pre-OS Boot | T1614: System Location  |     |     |     |     |
| --- | --- | --- | --- | ------------------ | ----------------------- | --- | --- | --- | --- |
Discovery
|     |     |     |     | T1211: Exploitation for  | T1007: System Service  |     |     |     |     |
| --- | --- | --- | --- | ------------------------ | ---------------------- | --- | --- | --- | --- |
|     |     |     |     | Defense Evasion          | Discovery              |     |     |     |     |
|     |     |     |     | T1014: Rootkit           | T1497:                 |     |     |     |     |
Virtualization/Sandbox
Evasion
T1553: Subvert Trust
Controls
T1221: Template Injection
T1548: Abuse Elevation
Control Mechanism
T1197: BITS Jobs
T1622: Debugger Evasion
T1480: Execution
Guardrails
T1656: Impersonation
T1202: Indirect Command
Execution
T1550: Use Alternate
Authentication Material
T1497:
Virtualization/Sandbox
Evasion
T1220: XSL Script
Processing
v15
|     |     | Legend: |     | Increasing levels of observations |     |     |     |     |     |
| --- | --- | ------- | --- | --------------------------------- | --- | --- | --- | --- | --- |
86

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Top threats observed in Greater China Region
Link to MITRE ATT&CK Navigator JSON File: - https://ensign.global/gcjs
SHA256 File Hash: 4db5755005870475428aafa081a0e467193bf9a786708ebf3719c6706dc6cdd0
TA0043: Reconnaissance TA0042: Resource  TA0001: Initial Access TA0002: Execution TA0003: Persistence TA0004: Privilege  TA0005: Defense Evasion TA0006: Credential  TA0007: Discovery TA0008: Lateral  TA0009: Collection TA0011: Command and  TA0010: Exfiltration TA0040: Impact
|     | Development |     | Escalation |     | Access |     | Movement | Control |
| --- | ----------- | --- | ---------- | --- | ------ | --- | -------- | ------- |
T1589: Gather Victim  T1588: Obtain Capabilities T1566: Phishing T1059: Command and  T1547: Boot or Logon  T1547: Boot or Logon  T1036: Masquerading T1056: Input Capture T1082: System Information T1021: Remote Services T1560: Archive Collected  T1102: Web Service T1041: Exfiltration Over C2  T1529: System
Identity Information Scripting Interpreter Autostart Execution Autostart Execution Discovery Data Channel Shutdown/Reboot
T1595: Active Scanning T1583: Acquire  T1078: Valid Accounts T1204: User Execution T1574: Hijack Execution  T1574: Hijack Execution  T1027: Obfuscated Files or T1110: Brute Force T1033: System Owner/User T1091: Replication Through T1005: Data from Local  T1071: Application Layer  T1567: Exfiltration Over  T1486: Data Encrypted for
Infrastructure Flow Flow Information Discovery Removable Media System Protocol Web Service Impact
T1598: Phishing for  T1587: Develop  T1189: Drive-by  T1203: Exploitation for  T1078: Valid Accounts T1055: Process Injection T1070: Indicator Removal T1555: Credentials from  T1497:  T1550: Use Alternate  T1056: Input Capture T1105: Ingress Tool  T1048: Exfiltration Over  T1561: Disk Wipe
Information Capabilities Compromise Client Execution Password Stores Virtualization/Sandbox  Authentication Material Transfer Alternative Protocol
Evasion
T1592: Gather Victim Host  T1608: Stage Capabilities T1133: External Remote  T1559: Inter-Process  T1546: Event Triggered  T1078: Valid Accounts T1574: Hijack Execution  T1003: OS Credential  T1016: System Network  T1210: Exploitation of  T1074: Data Staged T1090: Proxy T1020: Automated  T1489: Service Stop
Information Services Communication Execution Flow Dumping Configuration Discovery Remote Services Exfiltration
T1591: Gather Victim Org  T1584: Compromise  T1195: Supply Chain  T1106: Native API T1098: Account  T1546: Event Triggered  T1218: System Binary Proxy T1557: Adversary-in-the- T1083: File and Directory  T1534: Internal  T1114: Email Collection T1573: Encrypted Channel T1030: Data Transfer Size  T1485: Data Destruction
Information Infrastructure Compromise Manipulation Execution Execution Middle Discovery Spearphishing Limits
T1593: Search Open  T1586: Compromise  T1190: Exploit Public- T1053: Scheduled Task/JobT1133: External Remote  T1548: Abuse Elevation  T1055: Process Injection T1040: Network Sniffing T1057: Process Discovery T1080: Taint Shared  T1113: Screen Capture T1132: Data Encoding T1491: Defacement
Websites/Domains Accounts Facing Application Services Control Mechanism Content
T1590: Gather Victim  T1585: Establish Accounts T1091: Replication Through T1569: System Services T1542: Pre-OS Boot T1134: Access Token  T1140:  T1111: Multi-Factor  T1046: Network Service  T1119: Automated  T1001: Data Obfuscation T1498: Network Denial of
Network Information Removable Media Manipulation Deobfuscate/Decode Files Authentication InterceptionDiscovery Collection Service
or Information
T1594: Search Victim- T1199: Trusted RelationshipT1129: Shared Modules T1053: Scheduled Task/JobT1098: Account  T1553: Subvert Trust  T1528: Steal Application  T1012: Query Registry T1557: Adversary-in-the- T1008: Fallback Channels
| Owned Websites |     |     | Manipulation | Controls | Access Token |     | Middle |     |
| -------------- | --- | --- | ------------ | -------- | ------------ | --- | ------ | --- |
T1659: Content Injection T1047: Windows  T1543: Create or Modify  T1053: Scheduled Task/JobT1078: Valid Accounts T1558: Steal or Forge  T1518: Software Discovery T1213: Data from  T1095: Non-Application
Management  System Process Kerberos Tickets Information Repositories Layer Protocol
Instrumentation
|     |     | T1505: Server Software     | T1543: Create or Modify  | T1564: Hide Artifacts   | T1552: Unsecured  | T1614: System Location   | T1123: Audio Capture     | T1104: Multi-Stage       |
| --- | --- | -------------------------- | ------------------------ | ----------------------- | ----------------- | ------------------------ | ------------------------ | ------------------------ |
|     |     | Component                  | System Process           |                         | Credentials       | Discovery                |                          | Channels                 |
|     |     | T1197: BITS Jobs           | T1068: Exploitation for  | T1562: Impair Defenses  |                   | T1049: System Network    | T1115: Clipboard Data    | T1571: Non-Standard Port |
|     |     |                            | Privilege Escalation     |                         |                   | Connections Discovery    |                          |                          |
|     |     | T1136: Create Account      | T1037: Boot or Logon     | T1112: Modify Registry  |                   | T1007: System Service    | T1530: Data from Cloud   | T1219: Remote Access     |
|     |     |                            | Initialization Scripts   |                         |                   | Discovery                | Storage                  | Software                 |
|     |     | T1137: Office Application  |                          | T1497:                  |                   | T1087: Account Discovery | T1602: Data from         | T1092: Communication     |
|     |     | Startup                    |                          | Virtualization/Sandbox  |                   |                          | Configuration Repository | Through Removable Media  |
Evasion
|     |     | T1037: Boot or Logon      |     | T1548: Abuse Elevation  |     | T1010: Application Window  | T1039: Data from Network  | T1659: Content Injection  |
| --- | --- | ------------------------- | --- | ----------------------- | --- | -------------------------- | ------------------------- | ------------------------- |
|     |     | Initialization Scripts    |     | Control Mechanism       |     | Discovery                  | Shared Drive              |                           |
|     |     | T1176: Browser Extensions |     | T1134: Access Token     |     | T1622: Debugger Evasion    | T1025: Data from          | T1568: Dynamic Resolution |
|     |     |                           |     | Manipulation            |     |                            | Removable Media           |                           |
|     |     | T1205: Traffic Signaling  |     | T1542: Pre-OS Boot      |     | T1135: Network Share       | T1125: Video Capture      | T1205: Traffic Signaling  |
Discovery
|     |     |     |     | T1550: Use Alternate  |     | T1040: Network Sniffing |     |     |
| --- | --- | --- | --- | --------------------- | --- | ----------------------- | --- | --- |
Authentication Material
|     |     |     |     | T1197: BITS Jobs |     | T1120: Peripheral Device  |     |     |
| --- | --- | --- | --- | ---------------- | --- | ------------------------- | --- | --- |
Discovery
|     |     |     |     | T1622: Debugger Evasion |     | T1069: Permission Groups  |     |     |
| --- | --- | --- | --- | ----------------------- | --- | ------------------------- | --- | --- |
Discovery
|     |     |     |     | T1211: Exploitation for  |     | T1124: System Time  |     |     |
| --- | --- | --- | --- | ------------------------ | --- | ------------------- | --- | --- |
|     |     |     |     | Defense Evasion          |     | Discovery           |     |     |
T1014: Rootkit
T1221: Template Injection
T1480: Execution
Guardrails
T1656: Impersonation
T1202: Indirect Command
Execution
T1601: Modify System
|     | v15 |     |     | Image |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- |
T1205: Traffic Signaling
T1127: Trusted Developer
Utilities Proxy Execution
T1220: XSL Script
Processing
|     |     | Legend: |     | Increasing levels of observations |     |     |     |     |
| --- | --- | ------- | --- | --------------------------------- | --- | --- | --- | --- |
87

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Top threats observed in Indonesia
Link to MITRE ATT&CK Navigator JSON File: - https://ensign.global/idjs
SHA256 File Hash: c041193863dc7041d042d03e3c7b254a86ed102d055b5a4c657898d99cb2ebb2
TA0043: Reconnaissance TA0042: Resource  TA0001: Initial Access TA0002: Execution TA0003: Persistence TA0004: Privilege  TA0005: Defense Evasion TA0006: Credential  TA0007: Discovery TA0008: Lateral  TA0009: Collection TA0011: Command and  TA0010: Exfiltration TA0040: Impact
|     | Development |     |     |     | Escalation |     | Access | Movement | Control |
| --- | ----------- | --- | --- | --- | ---------- | --- | ------ | -------- | ------- |
T1591: Gather Victim Org  T1588: Obtain Capabilities T1566: Phishing T1059: Command and  T1547: Boot or Logon  T1547: Boot or Logon  T1070: Indicator Removal T1110: Brute Force T1082: System Information T1021: Remote Services T1560: Archive Collected  T1102: Web Service T1048: Exfiltration Over  T1565: Data Manipulation
Information Scripting Interpreter Autostart Execution Autostart Execution Discovery Data Alternative Protocol
T1595: Active Scanning T1584: Compromise  T1078: Valid Accounts T1204: User Execution T1574: Hijack Execution  T1574: Hijack Execution  T1036: Masquerading T1003: OS Credential  T1016: System Network  T1570: Lateral Tool TransferT1005: Data from Local  T1071: Application Layer  T1041: Exfiltration Over C2  T1485: Data Destruction
Infrastructure Flow Flow Dumping Configuration Discovery System Protocol Channel
T1592: Gather Victim Host  T1587: Develop  T1189: Drive-by  T1106: Native API T1546: Event Triggered  T1546: Event Triggered  T1027: Obfuscated Files or T1555: Credentials from  T1049: System Network  T1091: Replication Through T1056: Input Capture T1090: Proxy T1567: Exfiltration Over  T1486: Data Encrypted for
Information Capabilities Compromise Execution Execution Information Password Stores Connections Discovery Removable Media Web Service Impact
T1589: Gather Victim  T1583: Acquire  T1133: External Remote  T1569: System Services T1078: Valid Accounts T1055: Process Injection T1574: Hijack Execution  T1056: Input Capture T1087: Account Discovery T1074: Data Staged T1105: Ingress Tool  T1561: Disk Wipe
| Identity Information | Infrastructure | Services |     |     |     | Flow |     |     | Transfer |
| -------------------- | -------------- | -------- | --- | --- | --- | ---- | --- | --- | -------- |
T1593: Search Open  T1608: Stage Capabilities T1091: Replication Through T1203: Exploitation for  T1053: Scheduled Task/JobT1078: Valid Accounts T1218: System Binary Proxy T1552: Unsecured  T1046: Network Service  T1557: Adversary-in-the- T1132: Data Encoding T1529: System
Websites/Domains Removable Media Client Execution Execution Credentials Discovery Middle Shutdown/Reboot
T1590: Gather Victim  T1585: Establish Accounts T1195: Supply Chain  T1053: Scheduled Task/JobT1098: Account  T1068: Exploitation for  T1562: Impair Defenses T1557: Adversary-in-the- T1033: System Owner/User  T1123: Audio Capture T1001: Data Obfuscation T1491: Defacement
Network Information Compromise Manipulation Privilege Escalation Middle Discovery
T1594: Search Victim- T1559: Inter-Process  T1133: External Remote  T1134: Access Token  T1055: Process Injection T1040: Network Sniffing T1083: File and Directory  T1115: Clipboard Data T1008: Fallback Channels T1489: Service Stop
| Owned Websites |     |     | Communication | Services                | Manipulation                                   |                           | Discovery                 |                          |                          |
| -------------- | --- | --- | ------------- | ----------------------- | ---------------------------------------------- | ------------------------- | ------------------------- | ------------------------ | ------------------------ |
|                |     |     |               | T1542: Pre-OS Boot      | T1053: Scheduled Task/JobT1078: Valid Accounts |                           | T1135: Network Share      | T1213: Data from         | T1104: Multi-Stage       |
|                |     |     |               |                         |                                                |                           | Discovery                 | Information Repositories | Channels                 |
|                |     |     |               | T1505: Server Software  | T1098: Account                                 | T1140:                    | T1069: Permission Groups  | T1025: Data from         | T1571: Non-Standard Port |
|                |     |     |               | Component               | Manipulation                                   | Deobfuscate/Decode Files  | Discovery                 | Removable Media          |                          |
or Information
|     |     |     |     | T1197: BITS Jobs | T1548: Abuse Elevation  | T1112: Modify Registry | T1057: Process Discovery |     | T1568: Dynamic Resolution |
| --- | --- | --- | --- | ---------------- | ----------------------- | ---------------------- | ------------------------ | --- | ------------------------- |
Control Mechanism
|     |     |     |     | T1136: Create Account    | T1543: Create or Modify  | T1134: Access Token   | T1012: Query Registry     |     | T1573: Encrypted Channel |
| --- | --- | --- | --- | ------------------------ | ------------------------ | --------------------- | ------------------------- | --- | ------------------------ |
|     |     |     |     |                          | System Process           | Manipulation          |                           |     |                          |
|     |     |     |     | T1543: Create or Modify  |                          | T1553: Subvert Trust  | T1518: Software Discovery |     | T1095: Non-Application   |
|     |     |     |     | System Process           |                          | Controls              |                           |     | Layer Protocol           |
|     |     |     |     |                          |                          | T1564: Hide Artifacts | T1007: System Service     |     |                          |
Discovery
|     |     |     |     |     |     | T1542: Pre-OS Boot | T1010: Application Window  |     |     |
| --- | --- | --- | --- | --- | --- | ------------------ | -------------------------- | --- | --- |
Discovery
|     |     |     |     |     |     | T1548: Abuse Elevation  | T1217: Browser Information  |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------- | --------------------------- | --- | --- |
|     |     |     |     |     |     | Control Mechanism       | Discovery                   |     |     |
|     |     |     |     |     |     | T1197: BITS Jobs        | T1622: Debugger Evasion     |     |     |
|     |     |     |     |     |     | T1622: Debugger Evasion | T1615: Group Policy         |     |     |
Discovery
|     |     |     |     |     |     | T1480: Execution  | T1040: Network Sniffing |     |     |
| --- | --- | --- | --- | --- | --- | ----------------- | ----------------------- | --- | --- |
Guardrails
|     |     |     |     |     |     | T1211: Exploitation for  | T1201: Password Policy    |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------ | ------------------------- | --- | --- |
|     |     |     |     |     |     | Defense Evasion          | Discovery                 |     |     |
|     |     |     |     |     |     | T1656: Impersonation     | T1120: Peripheral Device  |     |     |
Discovery
|     |     |     |     |     |     | T1202: Indirect Command  | T1018: Remote System    |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------ | ----------------------- | --- | --- |
|     |     |     |     |     |     | Execution                | Discovery               |     |     |
|     |     |     |     |     |     | T1014: Rootkit           | T1614: System Location  |     |     |
Discovery
|     |     |     |     |     |     | T1221: Template Injection | T1124: System Time  |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------- | ------------------- | --- | --- |
Discovery
|     |     |     |     |     |     | T1497:                  | T1497:                  |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------- | ----------------------- | --- | --- |
|     |     |     |     |     |     | Virtualization/Sandbox  | Virtualization/Sandbox  |     |     |
|     |     |     |     |     |     | Evasion                 | Evasion                 |     |     |
T1220: XSL Script
|     | v15 |     |     |         |     | Processing                        |     |     |     |
| --- | --- | --- | --- | ------- | --- | --------------------------------- | --- | --- | --- |
|     |     |     |     | Legend: |     | Increasing levels of observations |     |     |     |
88

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Top threats observed in South Korea
Link to MITRE ATT&CK Navigator JSON File: - https://ensign.global/skjs
SHA256 File Hash: dfe93847aa2307258eb222ab9bfba67591ea06a7991a09520b07ce2d9ba9204e
TA0043: Reconnaissance TA0042: Resource  TA0001: Initial Access TA0002: Execution TA0003: Persistence TA0004: Privilege  TA0005: Defense Evasion TA0006: Credential  TA0007: Discovery TA0008: Lateral  TA0009: Collection TA0011: Command and  TA0010: Exfiltration TA0040: Impact
| Development |     | Escalation |     | Access |     | Movement | Control |
| ----------- | --- | ---------- | --- | ------ | --- | -------- | ------- |
T1595: Active Scanning T1588: Obtain Capabilities T1566: Phishing T1059: Command and  T1547: Boot or Logon  T1547: Boot or Logon  T1036: Masquerading T1003: OS Credential  T1082: System Information T1021: Remote Services T1560: Archive Collected  T1071: Application Layer  T1048: Exfiltration Over  T1561: Disk Wipe
Scripting Interpreter Autostart Execution Autostart Execution Dumping Discovery Data Protocol Alternative Protocol
T1589: Gather Victim  T1583: Acquire  T1078: Valid Accounts T1204: User Execution T1078: Valid Accounts T1078: Valid Accounts T1070: Indicator Removal T1110: Brute Force T1040: Network Sniffing T1550: Use Alternate  T1005: Data from Local  T1102: Web Service T1041: Exfiltration Over C2  T1529: System
Identity Information Infrastructure Authentication Material System Channel Shutdown/Reboot
T1591: Gather Victim Org  T1584: Compromise  T1189: Drive-by  T1203: Exploitation for  T1574: Hijack Execution  T1574: Hijack Execution  T1027: Obfuscated Files or T1056: Input Capture T1057: Process Discovery T1210: Exploitation of  T1074: Data Staged T1105: Ingress Tool  T1567: Exfiltration Over  T1485: Data Destruction
Information Infrastructure Compromise Client Execution Flow Flow Information Remote Services Transfer Web Service
T1598: Phishing for  T1587: Develop  T1133: External Remote  T1053: Scheduled Task/JobT1098: Account  T1055: Process Injection T1218: System Binary Proxy T1555: Credentials from  T1016: System Network  T1534: Internal  T1056: Input Capture T1090: Proxy T1030: Data Transfer Size  T1486: Data Encrypted for
Information Capabilities Services Manipulation Execution Password Stores Configuration Discovery Spearphishing Limits Impact
T1593: Search Open  T1585: Establish Accounts T1190: Exploit Public- T1559: Inter-Process  T1546: Event Triggered  T1098: Account  T1078: Valid Accounts T1040: Network Sniffing T1033: System Owner/User T1091: Replication Through T1114: Email Collection T1001: Data Obfuscation T1491: Defacement
Websites/Domains Facing Application Communication Execution Manipulation Discovery Removable Media
T1592: Gather Victim Host  T1608: Stage Capabilities T1091: Replication Through T1106: Native API T1505: Server Software  T1546: Event Triggered  T1574: Hijack Execution  T1552: Unsecured  T1083: File and Directory  T1557: Adversary-in-the- T1132: Data Encoding T1498: Network Denial of
Information Removable Media Component Execution Flow Credentials Discovery Middle Service
T1594: Search Victim- T1586: Compromise  T1195: Supply Chain  T1569: System Services T1133: External Remote  T1068: Exploitation for  T1564: Hide Artifacts T1557: Adversary-in-the- T1046: Network Service  T1213: Data from  T1573: Encrypted Channel T1489: Service Stop
Owned Websites Accounts Compromise Services Privilege Escalation Middle Discovery Information Repositories
T1199: Trusted Relationship T1542: Pre-OS Boot T1134: Access Token  T1055: Process Injection T1111: Multi-Factor  T1135: Network Share  T1123: Audio Capture T1008: Fallback Channels
|     |                                                           | Manipulation |                                       | Authentication InterceptionDiscovery |                           |                   |                     |
| --- | --------------------------------------------------------- | ------------ | ------------------------------------- | ------------------------------------ | ------------------------- | ----------------- | ------------------- |
|     | T1053: Scheduled Task/JobT1053: Scheduled Task/JobT1140:  |              |                                       | T1528: Steal Application             | T1120: Peripheral Device  | T1119: Automated  | T1104: Multi-Stage  |
|     |                                                           |              | Deobfuscate/Decode Files Access Token |                                      | Discovery                 | Collection        | Channels            |
or Information
|     | T1136: Create Account      | T1548: Abuse Elevation   | T1134: Access Token       |     | T1012: Query Registry      | T1039: Data from Network  | T1571: Non-Standard Port  |
| --- | -------------------------- | ------------------------ | ------------------------- | --- | -------------------------- | ------------------------- | ------------------------- |
|     |                            | Control Mechanism        | Manipulation              |     |                            | Shared Drive              |                           |
|     | T1197: BITS Jobs           | T1037: Boot or Logon     | T1562: Impair Defenses    |     | T1049: System Network      | T1025: Data from          | T1092: Communication      |
|     |                            | Initialization Scripts   |                           |     | Connections Discovery      | Removable Media           | Through Removable Media   |
|     | T1037: Boot or Logon       | T1543: Create or Modify  | T1542: Pre-OS Boot        |     | T1087: Account Discovery   | T1113: Screen Capture     | T1568: Dynamic Resolution |
|     | Initialization Scripts     | System Process           |                           |     |                            |                           |                           |
|     | T1176: Browser Extensions  |                          | T1553: Subvert Trust      |     | T1010: Application Window  |                           | T1219: Remote Access      |
|     |                            |                          | Controls                  |     | Discovery                  |                           | Software                  |
|     | T1543: Create or Modify    |                          | T1550: Use Alternate      |     | T1622: Debugger Evasion    |                           |                           |
|     | System Process             |                          | Authentication Material   |     |                            |                           |                           |
|     | T1137: Office Application  |                          | T1112: Modify Registry    |     | T1069: Permission Groups   |                           |                           |
|     | Startup                    |                          |                           |     | Discovery                  |                           |                           |
|     |                            |                          | T1014: Rootkit            |     | T1518: Software Discovery  |                           |                           |
|     |                            |                          | T1221: Template Injection |     | T1614: System Location     |                           |                           |
Discovery
|     |     |     | T1548: Abuse Elevation  |     | T1007: System Service  |     |     |
| --- | --- | --- | ----------------------- | --- | ---------------------- | --- | --- |
|     |     |     | Control Mechanism       |     | Discovery              |     |     |
|     |     |     | T1197: BITS Jobs        |     | T1497:                 |     |     |
Virtualization/Sandbox
Evasion
T1622: Debugger Evasion
T1480: Execution
Guardrails
T1211: Exploitation for
Defense Evasion
T1656: Impersonation
T1202: Indirect Command
Execution
T1497:
Virtualization/Sandbox
Evasion
| v15 |     |     | T1220: XSL Script  |     |     |     |     |
| --- | --- | --- | ------------------ | --- | --- | --- | --- |
Processing
|     | Legend: |     | Increasing levels of observations |     |     |     |     |
| --- | ------- | --- | --------------------------------- | --- | --- | --- | --- |
89

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Top threats observed in Australia
Link to MITRE ATT&CK Navigator JSON File: - https://ensign.global/aujs
SHA256 File Hash: 08d0175a59b02e7db8cd8c098c05691162218d2e21f00ad9843aa9eb5aec2e49
TA0043: Reconnaissance TA0042: Resource  TA0001: Initial Access TA0002: Execution TA0003: Persistence TA0004: Privilege  TA0005: Defense Evasion TA0006: Credential  TA0007: Discovery TA0008: Lateral  TA0009: Collection TA0011: Command and  TA0010: Exfiltration TA0040: Impact
| Development |     |     | Escalation |     | Access |     | Movement | Control |     |     |
| ----------- | --- | --- | ---------- | --- | ------ | --- | -------- | ------- | --- | --- |
T1595: Active Scanning T1588: Obtain Capabilities T1566: Phishing T1059: Command and  T1078: Valid Accounts T1078: Valid Accounts T1070: Indicator Removal T1110: Brute Force T1082: System Information T1021: Remote Services T1560: Archive Collected  T1090: Proxy T1567: Exfiltration Over  T1486: Data Encrypted for
|     | Scripting Interpreter |     |     |     |     | Discovery | Data |     | Web Service | Impact |
| --- | --------------------- | --- | --- | --- | --- | --------- | ---- | --- | ----------- | ------ |
T1589: Gather Victim  T1584: Compromise  T1078: Valid Accounts T1204: User Execution T1547: Boot or Logon  T1547: Boot or Logon  T1036: Masquerading T1003: OS Credential  T1016: System Network  T1210: Exploitation of  T1005: Data from Local  T1102: Web Service T1048: Exfiltration Over  T1565: Data Manipulation
Identity Information Infrastructure Autostart Execution Autostart Execution Dumping Configuration Discovery Remote Services System Alternative Protocol
T1592: Gather Victim Host  T1583: Acquire  T1189: Drive-by  T1203: Exploitation for  T1574: Hijack Execution  T1574: Hijack Execution  T1027: Obfuscated Files or T1056: Input Capture T1033: System Owner/User T1570: Lateral Tool TransferT1074: Data Staged T1071: Application Layer  T1041: Exfiltration Over C2  T1485: Data Destruction
Information Infrastructure Compromise Client Execution Flow Flow Information Discovery Protocol Channel
T1591: Gather Victim Org  T1608: Stage Capabilities T1190: Exploit Public- T1106: Native API T1546: Event Triggered  T1546: Event Triggered  T1218: System Binary Proxy T1555: Credentials from  T1069: Permission Groups  T1091: Replication Through T1056: Input Capture T1105: Ingress Tool  T1030: Data Transfer Size  T1561: Disk Wipe
Information Facing Application Execution Execution Execution Password Stores Discovery Removable Media Transfer Limits
T1598: Phishing for  T1587: Develop  T1133: External Remote  T1053: Scheduled Task/JobT1505: Server Software  T1134: Access Token  T1078: Valid Accounts T1557: Adversary-in-the- T1049: System Network  T1550: Use Alternate  T1213: Data from  T1001: Data Obfuscation T1529: System
Information Capabilities Services Component Manipulation Middle Connections Discovery Authentication Material Information Repositories Shutdown/Reboot
T1593: Search Open  T1586: Compromise  T1091: Replication Through T1559: Inter-Process  T1098: Account  T1055: Process Injection T1574: Hijack Execution  T1040: Network Sniffing T1087: Account Discovery T1119: Automated  T1573: Encrypted Channel T1491: Defacement
Websites/Domains Accounts Removable Media Communication Manipulation Flow Collection
T1585: Establish Accounts T1195: Supply Chain  T1569: System Services T1542: Pre-OS Boot T1098: Account  T1140:  T1528: Steal Application  T1057: Process Discovery T1025: Data from  T1008: Fallback Channels T1498: Network Denial of
Compromise Manipulation Deobfuscate/Decode Files Access Token Removable Media Service
or Information
T1199: Trusted RelationshipT1047: Windows  T1053: Scheduled Task/JobT1068: Exploitation for  T1134: Access Token  T1558: Steal or Forge  T1083: File and Directory  T1114: Email Collection T1104: Multi-Stage  T1489: Service Stop
|     | Management  |     | Privilege Escalation | Manipulation | Kerberos Tickets | Discovery |     | Channels |     |     |
| --- | ----------- | --- | -------------------- | ------------ | ---------------- | --------- | --- | -------- | --- | --- |
Instrumentation
|     |     | T1543: Create or Modify  | T1053: Scheduled Task/JobT1562: Impair Defenses |     |     | T1012: Query Registry | T1113: Screen Capture | T1571: Non-Standard Port |     |     |
| --- | --- | ------------------------ | ----------------------------------------------- | --- | --- | --------------------- | --------------------- | ------------------------ | --- | --- |
System Process
|     |     | T1133: External Remote  | T1543: Create or Modify  | T1055: Process Injection |     | T1518: Software Discovery | T1557: Adversary-in-the- | T1092: Communication    |     |     |
| --- | --- | ----------------------- | ------------------------ | ------------------------ | --- | ------------------------- | ------------------------ | ----------------------- | --- | --- |
|     |     | Services                | System Process           |                          |     |                           | Middle                   | Through Removable Media |     |     |
|     |     | T1197: BITS Jobs        | T1037: Boot or Logon     | T1553: Subvert Trust     |     | T1497:                    | T1115: Clipboard Data    | T1132: Data Encoding    |     |     |
|     |     |                         | Initialization Scripts   | Controls                 |     | Virtualization/Sandbox    |                          |                         |     |     |
Evasion
|     |     | T1037: Boot or Logon       |     | T1564: Hide Artifacts   |     | T1046: Network Service    | T1530: Data from Cloud    | T1568: Dynamic Resolution |     |     |
| --- | --- | -------------------------- | --- | ----------------------- | --- | ------------------------- | ------------------------- | ------------------------- | --- | --- |
|     |     | Initialization Scripts     |     |                         |     | Discovery                 | Storage                   |                           |     |     |
|     |     | T1136: Create Account      |     | T1112: Modify Registry  |     | T1135: Network Share      | T1602: Data from          | T1219: Remote Access      |     |     |
|     |     |                            |     |                         |     | Discovery                 | Configuration Repository  | Software                  |     |     |
|     |     | T1137: Office Application  |     | T1542: Pre-OS Boot      |     | T1120: Peripheral Device  | T1039: Data from Network  |                           |     |     |
|     |     | Startup                    |     |                         |     | Discovery                 | Shared Drive              |                           |     |     |
|     |     |                            |     | T1497:                  |     | T1018: Remote System      | T1125: Video Capture      |                           |     |     |
|     |     |                            |     | Virtualization/Sandbox  |     | Discovery                 |                           |                           |     |     |
Evasion
|     |     |     |     | T1014: Rootkit |     | T1614: System Location  |     |     |     |     |
| --- | --- | --- | --- | -------------- | --- | ----------------------- | --- | --- | --- | --- |
Discovery
|     |     |     |     | T1221: Template Injection |     | T1010: Application Window  |     |     |     |     |
| --- | --- | --- | --- | ------------------------- | --- | -------------------------- | --- | --- | --- | --- |
Discovery
|     |     |     |     | T1550: Use Alternate    |     | T1217: Browser Information  |     |     |     |     |
| --- | --- | --- | --- | ----------------------- | --- | --------------------------- | --- | --- | --- | --- |
|     |     |     |     | Authentication Material |     | Discovery                   |     |     |     |     |
|     |     |     |     | T1197: BITS Jobs        |     | T1622: Debugger Evasion     |     |     |     |     |
|     |     |     |     | T1622: Debugger Evasion |     | T1615: Group Policy         |     |     |     |     |
Discovery
|     |     |     |     | T1480: Execution  |     | T1654: Log Enumeration |     |     |     |     |
| --- | --- | --- | --- | ----------------- | --- | ---------------------- | --- | --- | --- | --- |
Guardrails
|     |     |     |     | T1211: Exploitation for  |     | T1040: Network Sniffing |     |     |     |     |
| --- | --- | --- | --- | ------------------------ | --- | ----------------------- | --- | --- | --- | --- |
Defense Evasion
|     |     |     |     | T1656: Impersonation |     | T1201: Password Policy  |     |     |     |     |
| --- | --- | --- | --- | -------------------- | --- | ----------------------- | --- | --- | --- | --- |
Discovery
|     |     |         |     | T1202: Indirect Command           |     | T1007: System Service  |     |     |     |     |
| --- | --- | ------- | --- | --------------------------------- | --- | ---------------------- | --- | --- | --- | --- |
| v15 |     |         |     | Execution                         |     | Discovery              |     |     |     |     |
|     |     |         |     | T1220: XSL Script                 |     | T1124: System Time     |     |     |     |     |
|     |     |         |     | Processing                        |     | Discovery              |     |     |     |     |
|     |     | Legend: |     | Increasing levels of observations |     |                        |     |     |     |     |
90

APPENDIX - B
TOP VULNERABILITIES
ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024 91

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Actively exploited vulnerabilities in Singapore (1/2)
EPSS
VULNERABILITY DESCRIPTION CVSS
(as of Apr 2024)
CVE-2023-4966 NetScaler ADC and Gateway reveal sensitive information when configured as a Gateway or AAA virtual 7.5 0.96869
server, including VPN, ICA Proxy, CVPN, and RDP Proxy setups.
CVE-2023-47246 SysAid On-Premise has a path traversal vulnerability that enables attackers to execute code by writing files 9.8 0.94113
to the Tomcat webroot.
CVE-2023-46747 An authentication bypass in BIG-IP allows attackers with network access via the management port or self IP 9.8 0.97135
addresses to execute system commands. This affects versions that have not reached End of Technical
Support (EoTS).
CVE-2023-45797 A Buffer overflow vulnerability in DreamSecurity MagicLine4NX allows an attacker to remotely execute code. 9.8 0.00134
CVE-2023-42793 In JetBrains TeamCity, authentication bypass leading to RCE on TeamCity Server was possible. 9.8 0.97071
CVE-2023-38831 In WinRAR, attackers can execute arbitrary code by tricking users into viewing a benign file within a ZIP 7.8 0.44373
archive that also contains a maliciously named folder, leading to executable content being processed.
CVE-2023-36934 A SQL injection vulnerability in MOVEit Transfer, allowing unauthenticated attackers to modify and access 9.1 0.09417
database content via crafted payloads to application endpoints.
CVE-2023-36933 In MOVEit Transfer, attackers can trigger a method causing an unhandled exception, leading to unexpected 7.5 0.00046
application termination.
CVE-2023-36932 MOVEit Transfer have SQL injection flaws exploitable by authenticated attackers to access and manipulate 8.1 0.0005
the database.
CVE-2023-34362 A SQL injection vulnerability in MOVEit Transfer allows unauthenticated access to its database. 9.8 0.95545
CVE-2023-27351 Remote attackers can bypass authentication in PaperCut NG due to a flaw in the SecurityRequestFilter 7.5 0.02082
class, which arises from an improperly implemented authentication algorithm.
CVE-2023–27350 Remote attackers can exploit a flaw in PaperCut NG to bypass authentication and execute code as SYSTEM 9.8 0.97204
due to inadequate access control in the SetupCompleted class.
CVE-2023-23397 Microsoft Outlook Elevation of Privilege Vulnerability 9.8 0.92645
Note: This is a non-exhaustive list
92

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Actively exploited vulnerabilities in Singapore (2/2)
EPSS
VULNERABILITY DESCRIPTION CVSS
(as of Apr 2024)
CVE-2023-20269 A flaw in Cisco ASA and FTD Software's VPN allows unauthorized brute force attacks or clientless SSL VPN 9.1 0.02588
sessions by exploiting AAA separation issues. The vulnerability enables attackers to potentially uncover
credentials or establish unauthorized VPN sessions. Valid credentials, including any second factors, are still
required for access. Cisco plans to release software updates and suggests workarounds.
CVE-2023-20095 A flaw in Cisco ASA and FTD Software's remote VPN allows remote attackers to cause a DoS by sending 8.6 0.00053
malicious HTTPS requests that lead to resource exhaustion.
CVE-2023-0669 Fortra's GoAnywhere MFT has a pre-auth command injection vulnerability via object deserialization in the 7.2 0.96975
License Response Servlet.
CVE-2022-47966 Multiple Zoho ManageEngine on-premise products are vulnerable to remote code execution due to an 9.8 0.97422
outdated Apache Santuario xmlsec version. Applications failed to implement necessary security measures
alongside xmlsec's XSLT features. Exploitation is contingent upon whether SAML SSO has been configured.
CVE-2022-26134 Confluence Server and Data Center have an OGNL injection vulnerability that lets unauthenticated attackers 9.8 0.97528
run arbitrary code.
CVE-2021-40444 Microsoft is investigating a remote code execution vulnerability in MSHTML that affects Windows, exploited 7.8 0.96821
through malicious Office documents with ActiveX controls. Impacts vary with user rights, being less severe
for non-admins. Updates to Microsoft Defender Antivirus and Endpoint provide protection. Further actions
may depend on investigation outcomes.
CVE-2006-1364 Microsoft's w3wp.exe in ASP.NET fails to correctly handle COM components without the AspCompat 7.5 0.02198
directive, allowing remote attackers to crash the system or deplete resources by repeatedly requesting
certain documents.
Note: This is a non-exhaustive list
93

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Actively exploited vulnerabilities in Malaysia (1/2)
EPSS
VULNERABILITY DESCRIPTION CVSS
(as of Apr 2024)
CVE-2023-4966 NetScaler ADC and Gateway reveal sensitive information when configured as a Gateway or AAA virtual 7.5 0.96869
server, including VPN, ICA Proxy, CVPN, and RDP Proxy setups.
CVE-2023-47246 SysAid On-Premise has a path traversal vulnerability that enables attackers to execute code by writing files 9.8 0.94113
to the Tomcat webroot.
CVE-2023-46747 An authentication bypass in BIG-IP allows attackers with network access via the management port or self IP 9.8 0.97135
addresses to execute system commands. This affects versions that have not reached End of Technical
Support (EoTS).
CVE-2023-45797 A Buffer overflow vulnerability in DreamSecurity MagicLine4NX allows an attacker to remotely execute code. 9.8 0.00134
CVE-2023-42793 In JetBrains TeamCity, authentication bypass leading to RCE on TeamCity Server was possible. 9.8 0.97071
CVE-2023-38831 In WinRAR, attackers can execute arbitrary code by tricking users into viewing a benign file within a ZIP 7.8 0.44373
archive that also contains a maliciously named folder, leading to executable content being processed.
CVE-2023-36934 A SQL injection vulnerability in MOVEit Transfer, allowing unauthenticated attackers to modify and access 9.1 0.09417
database content via crafted payloads to application endpoints.
CVE-2023-36933 In MOVEit Transfer, attackers can trigger a method causing an unhandled exception, leading to unexpected 7.5 0.00046
application termination.
CVE-2023-36932 MOVEit Transfer have SQL injection flaws exploitable by authenticated attackers to access and manipulate 8.1 0.0005
the database.
CVE-2023-34362 A SQL injection vulnerability in MOVEit Transfer allows unauthenticated access to its database. 9.8 0.95545
CVE-2023-27351 Remote attackers can bypass authentication in PaperCut NG due to a flaw in the SecurityRequestFilter 7.5 0.02082
class, which arises from an improperly implemented authentication algorithm.
CVE-2023–27350 Remote attackers can exploit a flaw in PaperCut NG to bypass authentication and execute code as SYSTEM 9.8 0.97204
due to inadequate access control in the SetupCompleted class.
CVE-2023-23397 Microsoft Outlook Elevation of Privilege Vulnerability 9.8 0.92645
Note: This is a non-exhaustive list
94

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Actively exploited vulnerabilities in Malaysia (2/2)
EPSS
VULNERABILITY DESCRIPTION CVSS
(as of Apr 2024)
CVE-2023-20269 A flaw in Cisco ASA and FTD Software's VPN allows unauthorized brute force attacks or clientless SSL VPN 9.1 0.02588
sessions by exploiting AAA separation issues. The vulnerability enables attackers to potentially uncover
credentials or establish unauthorized VPN sessions. Valid credentials, including any second factors, are still
required for access. Cisco plans to release software updates and suggests workarounds.
CVE-2023-20095 A flaw in Cisco ASA and FTD Software's remote VPN allows remote attackers to cause a DoS by sending 8.6 0.00053
malicious HTTPS requests that lead to resource exhaustion.
CVE-2023-0669 Fortra's GoAnywhere MFT has a pre-auth command injection vulnerability via object deserialization in the 7.2 0.96975
License Response Servlet.
CVE-2022-47966 Multiple Zoho ManageEngine on-premise products are vulnerable to remote code execution due to an 9.8 0.97422
outdated Apache Santuario xmlsec version. Applications failed to implement necessary security measures
alongside xmlsec's XSLT features. Exploitation is contingent upon whether SAML SSO has been configured.
CVE-2022-26134 Confluence Server and Data Center have an OGNL injection vulnerability that lets unauthenticated attackers 9.8 0.97528
run arbitrary code.
CVE-2021-40444 Microsoft is investigating a remote code execution vulnerability in MSHTML that affects Windows, exploited 7.8 0.96821
through malicious Office documents with ActiveX controls. Impacts vary with user rights, being less severe
for non-admins. Updates to Microsoft Defender Antivirus and Endpoint provide protection. Further actions
may depend on investigation outcomes.
CVE-2006-1364 Microsoft's w3wp.exe in ASP.NET fails to correctly handle COM components without the AspCompat 7.5 0.02198
directive, allowing remote attackers to crash the system or deplete resources by repeatedly requesting
certain documents.
Note: This is a non-exhaustive list
95

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Actively exploited vulnerabilities in Indonesia (1/2)
EPSS
VULNERABILITY DESCRIPTION CVSS
(as of Apr 2024)
CVE-2023-4966 NetScaler ADC and Gateway reveal sensitive information when configured as a Gateway or AAA virtual 7.5 0.96869
server, including VPN, ICA Proxy, CVPN, and RDP Proxy setups.
CVE-2023-47246 SysAid On-Premise has a path traversal vulnerability that enables attackers to execute code by writing files 9.8 0.94113
to the Tomcat webroot.
CVE-2023-46747 An authentication bypass in BIG-IP allows attackers with network access via the management port or self IP 9.8 0.97135
addresses to execute system commands. This affects versions that have not reached End of Technical
Support (EoTS).
CVE-2023-45797 A Buffer overflow vulnerability in DreamSecurity MagicLine4NX allows an attacker to remotely execute code. 9.8 0.00134
CVE-2023-42793 In JetBrains TeamCity, authentication bypass leading to RCE on TeamCity Server was possible. 9.8 0.97071
CVE-2023-36934 A SQL injection vulnerability in MOVEit Transfer, allowing unauthenticated attackers to modify and access 9.1 0.09417
database content via crafted payloads to application endpoints.
CVE-2023-36933 In MOVEit Transfer, attackers can trigger a method causing an unhandled exception, leading to unexpected 7.5 0.00046
application termination.
CVE-2023-36932 MOVEit Transfer have SQL injection flaws exploitable by authenticated attackers to access and manipulate 8.1 0.0005
the database.
CVE-2023-34362 A SQL injection vulnerability in MOVEit Transfer allows unauthenticated access to its database. 9.8 0.95545
CVE-2023-27351 Remote attackers can bypass authentication in PaperCut NG due to a flaw in the SecurityRequestFilter 7.5 0.02082
class, which arises from an improperly implemented authentication algorithm.
CVE-2023–27350 Remote attackers can exploit a flaw in PaperCut NG to bypass authentication and execute code as SYSTEM 9.8 0.97204
due to inadequate access control in the SetupCompleted class.
CVE-2023-20269 A flaw in Cisco ASA and FTD Software's VPN allows unauthorized brute force attacks or clientless SSL VPN 9.1 0.02588
sessions by exploiting AAA separation issues. The vulnerability enables attackers to potentially uncover
credentials or establish unauthorized VPN sessions. Valid credentials, including any second factors, are still
required for access. Cisco plans to release software updates and suggests workarounds.
Note: This is a non-exhaustive list
96

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Actively exploited vulnerabilities in Indonesia (2/2)
EPSS
VULNERABILITY DESCRIPTION CVSS
(as of Apr 2024)
CVE-2023-20095 A flaw in Cisco ASA and FTD Software's remote VPN allows remote attackers to cause a DoS by sending 8.6 0.00053
malicious HTTPS requests that lead to resource exhaustion.
CVE-2023-0669 Fortra's GoAnywhere MFT has a pre-auth command injection vulnerability via object deserialization in the 7.2 0.96975
License Response Servlet.
CVE-2022-47966 Multiple Zoho ManageEngine on-premise products are vulnerable to remote code execution due to an 9.8 0.97422
outdated Apache Santuario xmlsec version. Applications failed to implement necessary security measures
alongside xmlsec's XSLT features. Exploitation is contingent upon whether SAML SSO has been configured.
CVE-2022-26134 Confluence Server and Data Center have an OGNL injection vulnerability that lets unauthenticated attackers 9.8 0.97528
run arbitrary code.
CVE-2006-1364 Microsoft's w3wp.exe in ASP.NET fails to correctly handle COM components without the AspCompat 7.5 0.02198
directive, allowing remote attackers to crash the system or deplete resources by repeatedly requesting
certain documents.
Note: This is a non-exhaustive list
97

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Actively exploited vulnerabilities in South Korea (1/2)
EPSS
VULNERABILITY DESCRIPTION CVSS
(as of Apr 2024)
CVE-2023-4966 NetScaler ADC and Gateway reveal sensitive information when configured as a Gateway or AAA virtual 7.5 0.96869
server, including VPN, ICA Proxy, CVPN, and RDP Proxy setups.
CVE-2023-47246 SysAid On-Premise has a path traversal vulnerability that enables attackers to execute code by writing files 9.8 0.94113
to the Tomcat webroot.
CVE-2023-46747 An authentication bypass in BIG-IP allows attackers with network access via the management port or self IP 9.8 0.97135
addresses to execute system commands. This affects versions that have not reached End of Technical
Support (EoTS).
CVE-2023-45797 A Buffer overflow vulnerability in DreamSecurity MagicLine4NX allows an attacker to remotely execute code. 9.8 0.00134
CVE-2023-42793 In JetBrains TeamCity, authentication bypass leading to RCE on TeamCity Server was possible. 9.8 0.97071
CVE-2023-38831 In WinRAR, attackers can execute arbitrary code by tricking users into viewing a benign file within a ZIP 7.8 0.44373
archive that also contains a maliciously named folder, leading to executable content being processed.
CVE-2023-36934 A SQL injection vulnerability in MOVEit Transfer, allowing unauthenticated attackers to modify and access 9.1 0.09417
database content via crafted payloads to application endpoints.
CVE-2023-36933 In MOVEit Transfer, attackers can trigger a method causing an unhandled exception, leading to unexpected 7.5 0.00046
application termination.
CVE-2023-36932 MOVEit Transfer have SQL injection flaws exploitable by authenticated attackers to access and manipulate 8.1 0.0005
the database.
CVE-2023-34362 A SQL injection vulnerability in MOVEit Transfer allows unauthenticated access to its database. 9.8 0.95545
CVE-2023-27351 Remote attackers can bypass authentication in PaperCut NG due to a flaw in the SecurityRequestFilter 7.5 0.02082
class, which arises from an improperly implemented authentication algorithm.
CVE-2023–27350 Remote attackers can exploit a flaw in PaperCut NG to bypass authentication and execute code as SYSTEM 9.8 0.97204
due to inadequate access control in the SetupCompleted class.
Note: This is a non-exhaustive list
98

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Actively exploited vulnerabilities in South Korea (2/2)
EPSS
VULNERABILITY DESCRIPTION CVSS
(as of Apr 2024)
CVE-2023-23397 Microsoft Outlook Elevation of Privilege Vulnerability 9.8 0.92645
CVE-2023-20269 A flaw in Cisco ASA and FTD Software's VPN allows unauthorized brute force attacks or clientless SSL VPN 9.1 0.02588
sessions by exploiting AAA separation issues. The vulnerability enables attackers to potentially uncover
credentials or establish unauthorized VPN sessions, especially on Cisco ASA Software before 9.16. Valid
credentials, including any second factors, are still required for access. Cisco plans to release software
updates and suggests workarounds.
CVE-2023-20095 A flaw in Cisco ASA and FTD Software's remote VPN allows remote attackers to cause a DoS by sending 8.6 0.00053
malicious HTTPS requests that lead to resource exhaustion.
CVE-2023-0669 Fortra's GoAnywhere MFT has a pre-auth command injection vulnerability via object deserialization in the 7.2 0.96975
License Response Servlet.
CVE-2022-47966 Multiple Zoho ManageEngine on-premise products are vulnerable to remote code execution due to an 9.8 0.97422
outdated Apache Santuario xmlsec version. Applications failed to implement necessary security measures
alongside xmlsec's XSLT features. Exploitation is contingent upon whether SAML SSO has been configured.
CVE-2022-26134 Confluence Server and Data Center have an OGNL injection vulnerability that lets unauthenticated attackers 9.8 0.97528
run arbitrary code.
CVE-2021-40444 Microsoft is investigating a remote code execution vulnerability in MSHTML that affects Windows, exploited 7.8 0.96821
through malicious Office documents with ActiveX controls. Impacts vary with user rights, being less severe
for non-admins. Updates to Microsoft Defender Antivirus and Endpoint provide protection. Further actions
may depend on investigation outcomes.
CVE-2006-1364 Microsoft's w3wp.exe in ASP.NET fails to correctly handle COM components without the AspCompat 7.5 0.02198
directive, allowing remote attackers to crash the system or deplete resources by repeatedly requesting
certain documents.
Note: This is a non-exhaustive list
99

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Actively exploited vulnerabilities in Australia (1/2)
EPSS
VULNERABILITY DESCRIPTION CVSS
(as of Apr 2024)
CVE-2023-4966 NetScaler ADC and Gateway reveal sensitive information when configured as a Gateway or AAA virtual server, 7.5 0.96869
including VPN, ICA Proxy, CVPN, and RDP Proxy setups.
CVE-2023-47246 SysAid On-Premise has a path traversal vulnerability that enables attackers to execute code by writing files to the 9.8 0.94113
Tomcat webroot.
CVE-2023-46747 An authentication bypass in BIG-IP allows attackers with network access via the management port or self IP 9.8 0.97135
addresses to execute system commands. This affects versions that have not reached End of Technical Support (EoTS).
CVE-2023-45797 A Buffer overflow vulnerability in DreamSecurity MagicLine4NX allows an attacker to remotely execute code. 9.8 0.00134
CVE-2023-42793 In JetBrains TeamCity, authentication bypass leading to RCE on TeamCity Server was possible. 9.8 0.97071
CVE-2023-38831 In WinRAR, attackers can execute arbitrary code by tricking users into viewing a benign file within a ZIP archive that 7.8 0.44373
also contains a maliciously named folder, leading to executable content being processed.
CVE-2023-36934 A SQL injection vulnerability in MOVEit Transfer, allowing unauthenticated attackers to modify and access database 9.1 0.09417
content via crafted payloads to application endpoints.
CVE-2023-36933 In MOVEit Transfer, attackers can trigger a method causing an unhandled exception, leading to unexpected 7.5 0.00046
application termination.
CVE-2023-36932 MOVEit Transfer have SQL injection flaws exploitable by authenticated attackers to access and manipulate the 8.1 0.0005
database.
CVE-2023-34362 A SQL injection vulnerability in MOVEit Transfer allows unauthenticated access to its database. 9.8 0.95545
CVE-2023-27997 A heap-based buffer overflow vulnerability in FortiOS and FortiProxy SSL-VPN may allow a remote attacker to execute 9.8 0.15407
arbitrary code or commands via specifically crafted requests.
CVE-2023-27532 Vulnerability in Veeam Backup & Replication component allows encrypted credentials stored in the configuration 7.5 0.02703
database to be obtained. This may lead to gaining access to the backup infrastructure hosts.
CVE-2023-27351 Remote attackers can bypass authentication in PaperCut NG due to a flaw in the SecurityRequestFilter class, which 7.5 0.02082
arises from an improperly implemented authentication algorithm.
Note: This is a non-exhaustive list
100

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Actively exploited vulnerabilities in Australia (2/2)
EPSS
VULNERABILITY DESCRIPTION CVSS
(as of Apr 2024)
CVE-2023–27350 Remote attackers can exploit a flaw in PaperCut NG to bypass authentication and execute code as SYSTEM 9.8 0.97204
due to inadequate access control in the SetupCompleted class.
CVE-2023-23397 Microsoft Outlook Elevation of Privilege Vulnerability 9.8 0.92645
CVE-2023-20269 A flaw in Cisco ASA and FTD Software's VPN allows unauthorized brute force attacks or clientless SSL VPN 9.1 0.02588
sessions by exploiting AAA separation issues. The vulnerability enables attackers to potentially uncover
credentials or establish unauthorized VPN sessions. Valid credentials, including any second factors, are still
required for access. Cisco plans to release software updates and suggests workarounds.
CVE-2023-20095 A flaw in Cisco ASA and FTD Software's remote VPN allows remote attackers to cause a DoS by sending 8.6 0.00053
malicious HTTPS requests that lead to resource exhaustion.
CVE-2023-0669 Fortra's GoAnywhere MFT has a pre-auth command injection vulnerability via object deserialization in the 7.2 0.96975
License Response Servlet.
CVE-2022-47966 Multiple Zoho ManageEngine on-premise products are vulnerable to remote code execution due to an 9.8 0.97422
outdated Apache Santuario xmlsec version. Applications failed to implement necessary security measures
alongside xmlsec's XSLT features. Exploitation is contingent upon whether SAML SSO has been configured.
CVE-2022-42475 A heap-based buffer overflow vulnerability in FortiOS SSL-VPN and FortiProxy SSL-VPN may allow a remote 9.8 0.41883
unauthenticated attacker to execute arbitrary code or commands via specifically crafted requests.
CVE-2022-26134 Confluence Server and Data Center have an OGNL injection vulnerability that lets unauthenticated attackers 9.8 0.97528
run arbitrary code.
CVE-2021-40444 Microsoft is investigating a remote code execution vulnerability in MSHTML that affects Windows, exploited 7.8 0.96821
through malicious Office documents with ActiveX controls. Impacts vary with user rights, being less severe
for non-admins. Updates to Microsoft Defender Antivirus and Endpoint provide protection. Further actions
may depend on investigation outcomes.
CVE-2006-1364 Microsoft's w3wp.exe in ASP.NET fails to correctly handle COM components without the AspCompat 7.5 0.02198
directive, allowing remote attackers to crash the system or deplete resources by repeatedly requesting
certain documents.
Note: This is a non-exhaustive list
101

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Actively exploited vulnerabilities in Greater China Region (1/2)
EPSS
VULNERABILITY DESCRIPTION CVSS
(as of Apr 2024)
CVE-2023-4966 NetScaler ADC and Gateway reveal sensitive information when configured as a Gateway or AAA virtual 7.5 0.96869
server, including VPN, ICA Proxy, CVPN, and RDP Proxy setups.
CVE-2023-47246 SysAid On-Premise has a path traversal vulnerability that enables attackers to execute code by writing files 9.8 0.94113
to the Tomcat webroot.
CVE-2023-45797 A Buffer overflow vulnerability in DreamSecurity MagicLine4NX allows an attacker to remotely execute code. 9.8 0.00134
CVE-2023-42793 In JetBrains TeamCity, authentication bypass leading to RCE on TeamCity Server was possible. 9.8 0.97071
CVE-2023-38831 In WinRAR, attackers can execute arbitrary code by tricking users into viewing a benign file within a ZIP 7.8 0.44373
archive that also contains a maliciously named folder, leading to executable content being processed.
CVE-2023-36934 A SQL injection vulnerability in MOVEit Transfer, allowing unauthenticated attackers to modify and access 9.1 0.09417
database content via crafted payloads to application endpoints.
CVE-2023-36933 In MOVEit Transfer, attackers can trigger a method causing an unhandled exception, leading to unexpected 7.5 0.00046
application termination.
CVE-2023-36932 MOVEit Transfer have SQL injection flaws exploitable by authenticated attackers to access and manipulate 8.1 0.0005
the database.
CVE-2023-34362 A SQL injection vulnerability in MOVEit Transfer allows unauthenticated access to its database. 9.8 0.95545
CVE-2023-27532 Vulnerability in Veeam Backup & Replication component allows encrypted credentials stored in the 7.5 0.02703
configuration database to be obtained. This may lead to gaining access to the backup infrastructure hosts.
CVE-2023-27351 Remote attackers can bypass authentication in PaperCut NG due to a flaw in the SecurityRequestFilter 7.5 0.02082
class, which arises from an improperly implemented authentication algorithm.
CVE-2023–27350 Remote attackers can exploit a flaw in PaperCut NG to bypass authentication and execute code as SYSTEM 9.8 0.97204
due to inadequate access control in the SetupCompleted class.
CVE-2023-23397 Microsoft Outlook Elevation of Privilege Vulnerability 9.8 0.92645
Note: This is a non-exhaustive list
102

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Actively exploited vulnerabilities in Greater China Region (2/2)
EPSS
VULNERABILITY DESCRIPTION CVSS
(as of Apr 2024)
CVE-2023-20269 A flaw in Cisco ASA and FTD Software's VPN allows unauthorized brute force attacks or clientless SSL VPN 9.1 0.02588
sessions by exploiting AAA separation issues. The vulnerability enables attackers to potentially uncover
credentials or establish unauthorized VPN sessions. Valid credentials, including any second factors, are still
required for access. Cisco plans to release software updates and suggests workarounds.
CVE-2023-20095 A flaw in Cisco ASA and FTD Software's remote VPN allows remote attackers to cause a DoS by sending 8.6 0.00053
malicious HTTPS requests that lead to resource exhaustion.
CVE-2023-0669 Fortra's GoAnywhere MFT has a pre-auth command injection vulnerability via object deserialization in the 7.2 0.96975
License Response Servlet.
CVE-2021-40444 Microsoft is investigating a remote code execution vulnerability in MSHTML that affects Windows, exploited 7.8 0.96821
through malicious Office documents with ActiveX controls. Impacts vary with user rights, being less severe
for non-admins. Updates to Microsoft Defender Antivirus and Endpoint provide protection. Further actions
may depend on investigation outcomes.
CVE-2006-1364 Microsoft's w3wp.exe in ASP.NET fails to correctly handle COM components without the AspCompat 7.5 0.02198
directive, allowing remote attackers to crash the system or deplete resources by repeatedly requesting
certain documents.
Note: This is a non-exhaustive list
103

APPENDIX - C
TOP MITRE ATT&CK TACTICS
ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024 104

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Singapore
|                     |                              |     |     |     |     |     |     |     | s   |     | tn  |     |     |     |     |
| ------------------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                     |                              | e   |     |     |     |     |     | n   | s   |     |     |     |     |     |     |
| S h a r e   o f   d | a t a   p o in t s   f o r   | c   |     |     |     |     |     | o   | e   |     | e   |     |  d  |     |     |
|                     |                              | n   |     |     |     |     |     | is  | c   |     | m   |     | n   |     |     |
e a c h  M I T R E   A T T & C K   t a c tic  a tn s a c A e a
|     |     | s   | e   | s e |     | e   |     | v   |     |     | v   |     |  d  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i n  a   m o n t h  ( a l l  s e c t o r s ) s  e m c n c n E  la y o n n
|         |     | ia  |      | c    | o   | n   |  e o   |  e  | itn | r    | M   | o   | n      | o       |     |
| ------- | --- | --- | ---- | ---- | --- | --- | ------ | --- | --- | ---- | --- | --- | ------ | ------- | --- |
|         |     | n   | c p  | A    | itu | e   | g ita  | c   |     | e    |  la | itc | a lo   | ita     |     |
|         |     | n   | ru o |  la  |     | ts  | e      | n   | e   | v    |     |     | m      |         | tc  |
|         |     | o   | o le |      | c   | is  | liv la | e   | d   | o    | r   | e   | m r tn | r tlifx | a   |
| 1 0 0 % | 0 % | c   | s v  | itin | e   | r   | c      | fe  | e   | c    | e   | llo |        |         | p   |
|         |     | e   | e e  |      | x   | e   | irP s  |     | rC  | s iD | ta  |     | o o    |         | m   |
|         |     | R   | R D  |      | E   | P   | E      | D   |     |      | L   | C   | C C    | E       |     |
|         |     |     |      | I    |     |     |        |     |     |      |     |     |        |         | I   |
January 2023
February 2023
March 2023
April 2023
May 2023
June 2023
July 2023
August 2023
September 2023
October 2023
November 2023
December 2023
105

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Singapore
|                    |                              |     |     |     |     |     |     |     | s   |     | tn  |     |     |     |     |
| ------------------ | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                    |                              | e   |     |     |     |     |     | n   | s   |     |     |     |     |     |     |
| S h a r e  o f   d | a t a   p o i n t s  f o r   | c   |     |     |     |     |     | o   | e   |     | e   |     |  d  |     |     |
|                    |                              | n   |     |     |     |     |     | is  | c   |     | m   |     | n   |     |     |
e a c h   M I T R E   A T T & C K   t a c tic  a tn s a c A e a
|     |     | s   | e   | s e |     | e   |     | v   |     |     | v   |     |  d  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i n  a   s e c t o r  ( 2 0 2 3 ) s  e m c n c n E  la y o n n
|         |     | ia  |      | c    | o   | n   |  e o   |  e  | itn | r    | M   | o   | n      | o       |     |
| ------- | --- | --- | ---- | ---- | --- | --- | ------ | --- | --- | ---- | --- | --- | ------ | ------- | --- |
|         |     | n   | c p  | A    | itu | e   | g ita  | c   |     | e    |  la | itc | a lo   | ita     |     |
|         |     | n   | ru o |  la  |     | ts  | e      | n   | e   | v    |     |     | m      |         | tc  |
|         |     | o   | o le |      | c   | is  | liv la | e   | d   | o    | r   | e   | m r tn | r tlifx | a   |
| 1 0 0 % | 0 % | c   | s v  | itin | e   | r   | c      | fe  | e   | c    | e   | llo |        |         | p   |
|         |     | e   | e e  |      | x   | e   | irP s  |     | rC  | s iD | ta  |     | o o    |         | m   |
|         |     | R   | R D  |      | E   | P   | E      | D   |     |      | L   | C   | C C    | E       |     |
|         |     |     |      | I    |     |     |        |     |     |      |     |     |        |         | I   |
Administrative and
Technical Services
Aerospace
Banking & Finance
Education
Energy & Utilities
Healthcare
Insurance
Manufacturing
Real Estate
Technology
Telecommunication
106

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Malaysia & Indonesia
|                     |                              |     |     |     |     |     |     |     | s   |     | tn  |     |     |     |     |
| ------------------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                     |                              | e   |     |     |     |     |     | n   | s   |     |     |     |     |     |     |
| S h a r e   o f   d | a t a   p o in t s   f o r   | c   |     |     |     |     |     | o   | e   |     | e   |     |  d  |     |     |
|                     |                              | n   |     |     |     |     |     | is  | c   |     | m   |     | n   |     |     |
e a c h  M I T R E   A T T & C K   t a c tic  a tn s a c A e a
|     |     | s   | e   | s e |     | e   |     | v   |     |     | v   |     |  d  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i n  a   m o n t h  ( a l l  s e c t o r s ) s  e m c n c n E  la y o n n
|         |     | ia  |      | c    | o   | n   |  e o   |  e  | itn | r    | M   | o   | n      | o       |     |
| ------- | --- | --- | ---- | ---- | --- | --- | ------ | --- | --- | ---- | --- | --- | ------ | ------- | --- |
|         |     | n   | c p  | A    | itu | e   | g ita  | c   |     | e    |  la | itc | a lo   | ita     |     |
|         |     | n   | ru o |  la  |     | ts  | e      | n   | e   | v    |     |     | m      |         | tc  |
|         |     | o   | o le |      | c   | is  | liv la | e   | d   | o    | r   | e   | m r tn | r tlifx | a   |
| 1 0 0 % | 0 % | c   | s v  | itin | e   | r   | c      | fe  | e   | c    | e   | llo |        |         | p   |
|         |     | e   | e e  |      | x   | e   | irP s  |     | rC  | s iD | ta  |     | o o    |         | m   |
|         |     | R   | R D  |      | E   | P   | E      | D   |     |      | L   | C   | C C    | E       |     |
|         |     |     |      | I    |     |     |        |     |     |      |     |     |        |         | I   |
January 2023
February 2023
March 2023
April 2023
May 2023
June 2023
July 2023
August 2023
September 2023
October 2023
November 2023
December 2023
107

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Malaysia & Indonesia
|                    |                              |     |     |     |     |     |     |     | s   |     | tn  |     |     |     |     |
| ------------------ | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                    |                              | e   |     |     |     |     |     | n   | s   |     |     |     |     |     |     |
| S h a r e  o f   d | a t a   p o i n t s  f o r   | c   |     |     |     |     |     | o   | e   |     | e   |     |  d  |     |     |
|                    |                              | n   |     |     |     |     |     | is  | c   |     | m   |     | n   |     |     |
e a c h   M I T R E   A T T & C K   t a c tic  a tn s a c A e a
|     |     | s   | e   | s e |     | e   |     | v   |     |     | v   |     |  d  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i n  a   s e c t o r  ( 2 0 2 3 ) s  e m c n c n E  la y o n n
|         |     | ia  |      | c    | o   | n   |  e o   |  e  | itn | r    | M   | o   | n      | o       |     |
| ------- | --- | --- | ---- | ---- | --- | --- | ------ | --- | --- | ---- | --- | --- | ------ | ------- | --- |
|         |     | n   | c p  | A    | itu | e   | g ita  | c   |     | e    |  la | itc | a lo   | ita     |     |
|         |     | n   | ru o |  la  |     | ts  | e      | n   | e   | v    |     |     | m      |         | tc  |
|         |     | o   | o le |      | c   | is  | liv la | e   | d   | o    | r   | e   | m r tn | r tlifx | a   |
| 1 0 0 % | 0 % | c   | s v  | itin | e   | r   | c      | fe  | e   | c    | e   | llo |        |         | p   |
|         |     | e   | e e  |      | x   | e   | irP s  |     | rC  | s iD | ta  |     | o o    |         | m   |
|         |     | R   | R D  |      | E   | P   | E      | D   |     |      | L   | C   | C C    | E       |     |
|         |     |     |      | I    |     |     |        |     |     |      |     |     |        |         | I   |
Administrative and
Technical Services
Banking & Finance
Energy & Utilities
Insurance
Manufacturing
Technology
Telecommunication
108

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Greater China Region
|                     |                              |     |     |     |     |     |     |     | s   |     | tn  |     |     |     |     |
| ------------------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                     |                              | e   |     |     |     |     |     | n   | s   |     |     |     |     |     |     |
| S h a r e   o f   d | a t a   p o in t s   f o r   | c   |     |     |     |     |     | o   | e   |     | e   |     |  d  |     |     |
|                     |                              | n   |     |     |     |     |     | is  | c   |     | m   |     | n   |     |     |
e a c h  M I T R E   A T T & C K   t a c tic  a tn s a c A e a
|     |     | s   | e   | s e |     | e   |     | v   |     |     | v   |     |  d  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i n  a   m o n t h  ( a l l  s e c t o r s ) s  e m c n c n E  la y o n n
|         |     | ia  |      | c    | o   | n   |  e o   |  e  | itn | r    | M   | o   | n      | o       |     |
| ------- | --- | --- | ---- | ---- | --- | --- | ------ | --- | --- | ---- | --- | --- | ------ | ------- | --- |
|         |     | n   | c p  | A    | itu | e   | g ita  | c   |     | e    |  la | itc | a lo   | ita     |     |
|         |     | n   | ru o |  la  |     | ts  | e      | n   | e   | v    |     |     | m      |         | tc  |
|         |     | o   | o le |      | c   | is  | liv la | e   | d   | o    | r   | e   | m r tn | r tlifx | a   |
| 1 0 0 % | 0 % | c   | s v  | itin | e   | r   | c      | fe  | e   | c    | e   | llo |        |         | p   |
|         |     | e   | e e  |      | x   | e   | irP s  |     | rC  | s iD | ta  |     | o o    |         | m   |
|         |     | R   | R D  |      | E   | P   | E      | D   |     |      | L   | C   | C C    | E       |     |
|         |     |     |      | I    |     |     |        |     |     |      |     |     |        |         | I   |
January 2023
February 2023
March 2023
April 2023
May 2023
June 2023
July 2023
August 2023
September 2023
October 2023
November 2023
December 2023
109

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
Greater China Region
|                    |                              |     |     |     |     |     |     |     | s   |     | tn  |     |     |     |     |
| ------------------ | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                    |                              | e   |     |     |     |     |     | n   | s   |     |     |     |     |     |     |
| S h a r e  o f   d | a t a   p o i n t s  f o r   | c   |     |     |     |     |     | o   | e   |     | e   |     |  d  |     |     |
|                    |                              | n   |     |     |     |     |     | is  | c   |     | m   |     | n   |     |     |
e a c h   M I T R E   A T T & C K   t a c tic  a tn s a c A e a
|     |     | s   | e   | s e |     | e   |     | v   |     |     | v   |     |  d  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i n  a   s e c t o r  ( 2 0 2 3 ) s  e m c n c n E  la y o n n
|         |     | ia  |      | c    | o   | n   |  e o   |  e  | itn | r    | M   | o   | n      | o       |     |
| ------- | --- | --- | ---- | ---- | --- | --- | ------ | --- | --- | ---- | --- | --- | ------ | ------- | --- |
|         |     | n   | c p  | A    | itu | e   | g ita  | c   |     | e    |  la | itc | a lo   | ita     |     |
|         |     | n   | ru o |  la  |     | ts  | e      | n   | e   | v    |     |     | m      |         | tc  |
|         |     | o   | o le |      | c   | is  | liv la | e   | d   | o    | r   | e   | m r tn | r tlifx | a   |
| 1 0 0 % | 0 % | c   | s v  | itin | e   | r   | c      | fe  | e   | c    | e   | llo |        |         | p   |
|         |     | e   | e e  |      | x   | e   | irP s  |     | rC  | s iD | ta  |     | o o    |         | m   |
|         |     | R   | R D  |      | E   | P   | E      | D   |     |      | L   | C   | C C    | E       |     |
|         |     |     |      | I    |     |     |        |     |     |      |     |     |        |         | I   |
Administrative and
Technical Services
Banking & Finance
Education
Hospitality
Insurance
Manufacturing
Mining
Real Estate
Technology
Telecommunication
110

APPENDIX - D
REFERENCES
ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024 111

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
A A. Bokovoy, S. Ievlev, G. Kouriachy, D. Levin, A. Novodvorsky, A. Prokoudine, A. Smirnov, O. Vlasenko, M. Zabalujev. ALT Linux 2.3
Compact. Retrieved from: https://docs.altlinux.org/ru-RU/archive/2.3/html-single/compact/alt-docs-compact-en/ch01s02.html
A. Griffin. Microsoft responds after users of new Bing chatbot complain about its latest behaviour. (23 February 2023). Yahoo.
Retrieved from: https://news.yahoo.com/microsoft-responds-users-bing-chatbot-171403057.html
A. Kraft. Microsoft shuts down AI chatbot after it turned into a Nazi. (25 March 2016). CBS News. Retrieved from:
https://www.cbsnews.com/news/microsoft-shuts-down-ai-chatbot-after-it-turned-into-racist-nazi/
A. Render-Katolik. The IT Army of Ukraine. (16 August 2023). Center for Strategic and International Studies. Retrieved from:
https://www.csis.org/blogs/strategic-technologies-blog/it-army-ukraine
A. Vassilev, A. Oprea, A. Fordyce, H. Anderson. Adversarial Machine Learning, A Taxonomy and Terminology of Attacks and
Mitigations. (January 2024). NIST. Retrieved from: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2023.pdf
Alert: GhostSec and Stormous Launch Joint Ransomware Attacks in Over 15 Countries. (6 March 2024). The Hacker News.
Retrieved from: https://thehackernews.com/2024/03/alert-ghostsec-and-stormous-launch.html
B. Kondruss. MOVEit hack victim list. (20 December 2023). Retrieved from: https://konbriefing.com/en-topics/cyber-attacks-
B
moveit-victim-list.html
B. Toulas. LockBit ransomware exploits Citrix Bleed in attacks, 10K servers exposed. (14 November 2023). Bleeping Computer.
Retrieved from: https://www.bleepingcomputer.com/news/security/lockbit-ransomware-exploits-citrix-bleed-in-attacks-10k-
servers-exposed/
B. Toulas. Israel warns of BiBi wiper attacks targeting Linux and Windows. (13 November 2023). Bleeping Computer. Retrieved
from: https://www.bleepingcomputer.com/news/security/israel-warns-of-bibi-wiper-attacks-targeting-linux-and-windows/
112

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
C C. Page. PaperCut says hackers are exploiting ‘critical’ security flaws in unpatched servers. (25 April 2023). Techcrunch. Retrieved from:
https://techcrunch.com/2023/04/25/papercut-hackers-critical-fLaw-clop-ransomware/
C. Rawling. Pizza Hut says nearly two-hundred thousand customers affected by data breach. (20 September 2023). ABC News. Retrieved from:
https://www.abc.net.au/news/2023-09-20/pizza-hut-customers-affected-by-cyber-hack/102881804
C. Szewczyk. Billions from the CHIPS Act is soon to begin flowing with Samsung, Intel and TSMC set to benefit. (18 March 2024). PC Gamer.
Retrieved from: https://www.pcgamer.com/hardware/billions-from-the-chips-act-is-soon-to-begin-flowing-with-samsung-intel-and-tsmc-
set-to-benefit/
China-backed Hackers Hijack Software Updates to Implant "NSPX30" Spyware. (25 January 2024). The Hacker News. Retrieved from:
https://thehackernews.com/2024/01/china-backed-hackers-hijack-software.html
D. Tilo. Over 6,000 individuals hit in Sony data breach: reports. (10 October 2023). Human Resources Director. Retrieved from:
D
https://www.hcamag.com/au/news/general/over-6000-individuals-hit-in-sony-data-breach-reports/462431
Dormant PyPI Package Compromised to Spread Nova Sentinel Malware. (23 February 2024). The Hacker News. Retrieved from:
https://thehackernews.com/2024/02/dormant-pypi-package-compromised-to.html
DragonForce Malaysia: OpsPetir. (12 Apr 2023). Radware. Retrieved from: https://www.radware.com/security/threat-advisories-and-attack-
reports/dragonforce-malaysia-opspetir/
E. Kovacs. Law Enforcement Reportedly Behind Takedown of BlackCat/Alphv Ransomware Website. (11 December 2023). Security Week.
E
Retrieved from: https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/
E. Kovacs. Ransomware Group Files SEC Complaint Over Victim’s Failure to Disclose Data Breach. (16 November 2023). Security Week.
Retrieved from: https://www.securityweek.com/ransomware-group-files-sec-complaint-over-victims-failure-to-disclose-data-breach/
E. Madnick. The Continued Threat to Personal Data: Key Factors Behind the 2023 Increase. (December 2023). Apple. Retrieved from:
https://www.apple.com/newsroom/pdfs/The-Continued-Threat-to-Personal-Data-Key-Factors-Behind-the-2023-Increase.pdf
E. Stanish. Municipal Water Authority of Aliquippa hacked by Iranian-backed cyber group. (26 November 2023). CBS News. Retrieved from:
https://www.cbsnews.com/pittsburgh/news/municipal-water-authority-of-aliquippa-hacked-iranian-backed-cyber-group/
113

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
F F. Koh. Kim Jong Un’s move to label South Korea an enemy, drop reunification policy part of North’s diplomatic playbook: Experts. (17 January
2024). Channel News Asia. Retrieved from: https://www.channelnewsasia.com/world/kim-jong-un-move-label-south-korea-enemy-drop-
reunification-policy-strategic-part-norths-diplomatic-playbook-experts-4053871
F. Singer. They’re not TV anchors, they’re avatars: How Venezuela is using AI-generated propaganda. (22 February 2023). El Pais. Retrieved
from: https://english.elpais.com/international/2023-02-22/theyre-not-tv-anchors-theyre-avatars-how-venezuela-is-using-ai-generated-
propaganda.html
F. X. Frei & A. Morriss. Begin with Trust. (May 2020). Harvard Business Review. Retrieved from: https://hbr.org/2020/05/begin-with-trust
FH. Hudnall. Fact check: Video altered to show Joe Biden making transphobic remarks. (9 February 2023). USA Today. Retrieved from:
https://www.usatoday.com/story/news/factcheck/2023/02/09/fact-check-video-edited-show-joe-biden-making-transphobic-
remarks/11211453002/
G. Chan. Deepfake video of Taylor Swift speaking Mandarin sparks discussion over AI in China. (30 October 2023). The Straits Times. Retrieved
G
from: https://www.straitstimes.com/asia/east-asia/deepfake-video-of-taylor-swift-speaking-mandarin-sparks-discussion-over-ai-in-china
G. Sharma. DragonForce Malaysia attacks Israeli institutions: Radware (14 April 2023). SecurityBrief Asia. Retrieved from:
https://securitybrief.asia/story/dragonforce-malaysia-attacks-israeli-institutions-radware
Heightened Alert for Cyber Activities Targeting Domains and Infrastructures in Malaysia. (27 February 2022). National Cyber Coordination and
H
Command Centre. Retrieved from: https://www.nc4.gov.my/alert/653a2988900885a0819d058d
114

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
J J. Barrett. Latitude Financial cyber-attack worse than first thought with 14m customer records stolen. (27 March 2023). The Guardian.
Retrieved from: https://www.theguardian.com/australia-news/2023/mar/27/latitude-financial-cyber-data-breach-hack-14m-customer-
records-stolen
J. Kim. South Korean startups chase Nvidia with AI chip design push. (15 March 2024). Nikkei Asia. Retrieved from:
https://asia.nikkei.com/Business/Tech/Semiconductors/South-Korean-startups-chase-Nvidia-with-AI-chip-design-push
J. Munshaw. What’s the deal with the massive backlog of vulnerabilities at the NVD? (19 April 2024). Talos Intelligence. Retrieved from:
https://blog.talosintelligence.com/nvd-vulnerability-backlog-the-need-to-know/
J. Pearson. Lockbit cybercrime gang says it is back online following global police bust. (27 February 2024). Reuters. Retrieved from:
https://www.reuters.com/technology/cybersecurity/lockbit-cybercrime-gang-says-it-is-back-online-following-global-police-bust-2024-02-
26/
J. Taylor. HWL Ebsworth hack: 65 Australian government agencies affected by cyber-attack. (18 September 2023). The Guardian. Retrieved
from: https://www.theguardian.com/australia-news/2023/sep/18/hwl-ebsworth-hack-65-australian-government-agencies-affected-by-cyber-
attack
K. Alspach. CISA Breached Via Ivanti VPN Vulnerabilities: Report. (8 March 2024). CRN. Retrieved from:
K
https://www.crn.com/news/security/2024/cisa-breached-via-ivanti-vpn-vulnerabilities-report
K. Meegan-Vickers. The LockBit takedown Law enforcement ‘trolls’ ransomware gang. (4 April 2024). Global Initiative. Retrieved from:
https://globalinitiative.net/analysis/the-lockbit-takedown-law-enforcement-trolls-ransomware-gang/
K. Poireault. DragonForce Ransomware Group Uses LockBit's Leaked Builder. (25 April 2024). Infosecurity Magazine. Retrieved from:
https://www.infosecurity-magazine.com/news/dragonforce-ransomware-lockbit/
Kirin 9000. Hisilicon. Retrieved from: https://www.hisilicon.com/en/products/Kirin/Kirin-flagship-chips/Kirin-9000
115

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
L L. Tang. Billion-dollar money laundering case: Singapore police began ‘comprehensive intelligence probe’ in early 2022. (3 October 2023).
Channel News Asia. Retrieved from: https://www.channelnewsasia.com/singapore/billion-dollar-money-laundering-police-intelligence-
probe-2022-3816371
L. Yulisman. Indonesia hunts for Bjorka, hacker selling 1.3b SIM card users' data, taunting officials. (19 September 2022). Bleeping Computer.
Retrieved from: https://www.straitstimes.com/asia/se-asia/indonesia-hunts-for-bjorka-hacker-selling-13b-sim-card-users-data-taunting-
officials
Loongson releases next-generation CPU; new breakthrough in domestic design. (28 November 2023). Global Times. Retrieved from:
https://www.globaltimes.cn/page/202311/1302643.shtml
M. Burgess. Ukraine’s Volunteer ‘IT Army’ Is Hacking in Uncharted Territory. (27 February 2022). Wired. Retrieved from:
M
https://www.wired.com/story/ukraine-it-army-russia-war-cyber-attacks-ddos/
M. Harjani. Are US export controls making China’s chip industry more innovative? (22 April 2024). Lowly Institute. Retrieved from:
https://www.lowyinstitute.org/the-interpreter/are-us-export-controls-making-china-s-chip-industry-more-innovative
M. Lim. China launches its first open-source desktop operating system as it moves to cut use of US tech. (15 July 2023). Retrieved from:
https://www.straitstimes.com/asia/east-asia/china-launches-its-first-open-source-desktop-operating-system-as-it-moves-to-cut-use-of-us-
tech
MA-1027.022024: MyCERT Advisory - Recent Cyber Incidents Launched by TA ROOTK1T ISC Team to Malaysia Organisations. (6 February
2024). Malaysia Computer Emergency Response Team. Retrieved from: https://www.mycert.org.my/portal/advisory?id=MA-1027.022024
Microsoft Threat Intelligence. The many lives of BlackCat ransomware. (13 June 2022). Microsoft. Retrieved from:
https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/
N. Eddy. DragonForce Malaysia Releases LPE Exploit, Threatens Ransomware. (1 July 2022). Dark Reading. Retrieved from:
N
https://www.darkreading.com/vulnerabilities-threats/dragonforce-malaysia-releases-lpe-exploit-threatens-ransomware
N. Gisonna. Great Fitrewall Chinese Internet Policy. Britannica. Retrieved from: https://www.britannica.com/topic/Great-Firewall
N. Nelson. GPT-4 Can Exploit Most Vulns Just by Reading Threat Advisories. (19 April 2024). Dark Reading. Retrieved from:
https://www.darkreading.com/threat-intelligence/gpt-4-can-exploit-most-vulns-just-by-reading-threat-advisories
116

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
O O. Yoachimik & J. Pacheco. DDoS threat report for 2023 Q3. (26 October 2023). Cloudflare. Retrieved from: https://blog.cloudflare.com/ddos-
threat-report-2023-q3/
P. Verma. AI deepfakes threaten to upend global elections. No one can stop them. (23 April 2024). The Washington Post. Retrieved from:
P
https://www.washingtonpost.com/technology/2024/04/23/ai-deepfake-election-2024-us-india/
PJSC Rostelecom. Retrieved from: https://www.rst-com.ru/b2b/aurora/
R. Daws. GitHub suffers from over 100K infected repos. (29 February 2024). Developer. Retrieved from: https://www.developer-
R
tech.com/news/2024/feb/29/github-suffers-over-100k-infected-repos/
R. Lakshmanan. New COSMICENERGY Malware Exploits ICS Protocol to Sabotage Power Grids. (26 May 2023). The Hacker News. Retrieved
from: https://thehackernews.com/2023/05/new-cosmicenergy-malware-exploits-ics.html
S. Contorno & D. O’Sullivan. DeSantis campaign posts fake images of Trump hugging Fauci in social media video. (8 June 2023). CNN.
S
Retrieved from: https://edition.cnn.com/2023/06/08/politics/desantis-campaign-video-fake-ai-image/index.html
S. Gatlan. MITRE says state hackers breached its network via Ivanti zero-days. (19 April 2024). BleepingComputer. Retrieved from:
https://www.bleepingcomputer.com/news/security/mitre-says-state-hackers-breached-its-network-via-ivanti-zero-days/
S. Ryohtaroh & T. Cheng. Japan's chip reboot: TSMC, Samsung, Micron pave way for silicon revival. (28 February 2024). Nikkei Asia. Retrieved
from: https://asia.nikkei.com/Spotlight/The-Big-Story/Japan-s-chip-reboot-TSMC-Samsung-Micron-pave-way-for-silicon-revival
S. Sharwood. MongoDB to terminate Russian SaaS accounts. (15 March 2022). The Register. Retrieved from:
https://www.theregister.com/2022/03/15/mongodb_terminates_russian_saas/
Samsung. Retrieved from: https://semiconductor.samsung.com/processor/
Security Asset Management Statistics to Know in 2023. (18 May 2023). Noetic Cyber. Retrieved from: https://noeticcyber.com/security-asset-
management-statistics-to-know-2023/
117

ENSIGN INFOSECURITY CYBER THREAT LANDSCAPE 2024
T T. Broderick. Russia Is Trying to Leave the Internet and Build Its Own. (12 July 2023). Scientific American. Retrieved from:
https://www.scientificamerican.com/article/russia-is-trying-to-leave-the-internet-and-build-its-own/
Tizen. Retrieved from: https://docs.tizen.org/platform/what-is-tizen/overview/
V. Insinna & Z. Siddiqui. Boeing says 'cyber incident' hit parts business. (3 November 2023). IT News. Retrieved from:
V
https://www.itnews.com.au/news/boeing-says-cyber-incident-hit-parts-business-601999
Vx-underground. X. (4 March 2024). Retrieved from: https://twitter.com/vxunderground/status/1764676460113994220
W. Knight. The US Throws $52 Billion at Chips—but Needs to Spend It Wisely. (28 July 2022). Wired. Retrieved from:
W
https://www.wired.com/story/chips-act-52-billion-semiconductor-production/
XZ Utils Backdoor — Everything You Need to Know, and What You Can Do. (1 April 2024). Akamai. Retrieved from:
X
https://www.akamai.com/blog/security-research/critical-linux-backdoor-xz-utils-discovered-what-to-know
118

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-11-21", "model": "gemini-3.8-flash"} -->
