# CALIBRATING EXPANSION: 2023 ANNUAL CYBERSECURITY REPORT

**Organization:** Trend Micro  
**Year:** 2023  

---

## Table of Contents
- [Executive Overview](#executive-overview)
- [APT Campaigns](#apt-campaigns)
  - [APT28’s NTLMv2 Hash Relay Attacks](#apt28s-ntlmv2-hash-relay-attacks)
  - [APT28’s More Recent Credential Phishing Campaign](#apt28s-more-recent-credential-phishing-campaign)
  - [Gamaredon](#gamaredon)
  - [Earth Lusca](#earth-lusca)
  - [Earth Estries](#earth-estries)
  - [Kimsuky’s Continued Activity](#kimsukys-continued-activity)
  - [Void Rabisu’s Slimmed Down ROMCOM Variant](#void-rabisus-slimmed-down-romcom-variant)
  - [Turla Attacks Using Capibar and Kazuar](#turla-attacks-using-capibar-and-kazuar)
  - [APT34’s Targeted Phishing Attack](#apt34s-targeted-phishing-attack)
  - [Mustang Panda](#mustang-panda)
  - [APT38](#apt38)
  - [Konni Group](#konni-group)
  - [APT29’s VovaMirage Spear Phishing Campaign](#apt29s-vovamirage-spear-phishing-campaign)
- [Ransomware Threats](#ransomware-threats)
  - [What to Watch Out For](#what-to-watch-out-for)
  - [Total Ransomware Detections](#total-ransomware-detections)
  - [Operating Systems Affected by Ransomware](#operating-systems-affected-by-ransomware)
  - [Top Countries and Regions by Detected Ransomware Attacks](#top-countries-and-regions-by-detected-ransomware-attacks)
  - [Top Industries and Segments by Detected Ransomware Attacks](#top-industries-and-segments-by-detected-ransomware-attacks)
  - [Top Ransomware Families](#top-ransomware-families)
- [Cloud and Enterprise Threats](#cloud-and-enterprise-threats)
  - [Risk Events (ASRM)](#risk-events-asrm)
  - [Home Network Security Top Events](#home-network-security-top-events)
  - [Home Network Security Top Affected Device Types](#home-network-security-top-affected-device-types)
  - [Vulnerabilities by Vendor](#vulnerabilities-by-vendor)
- [MITRE ATT&CK Detections](#mitre-attck-detections)
  - [Top 5 Tactics Detected (Overall)](#top-5-tactics-detected-overall)
  - [Top Tactics, Techniques, and Procedures (TTPs) Endpoint](#top-tactics-techniques-and-procedures-ttps-endpoint)
  - [Top TTPs Network](#top-ttps-network)
  - [TTPs Overall Trend by Detections](#ttps-overall-trend-by-detections)
  - [Living-Off-The-Land Tactics](#living-off-the-land-tactics)
- [Threat Landscape](#threat-landscape)
  - [Malware Detection](#malware-detection)
  - [Top Countries Accessing Malicious URLs](#top-countries-accessing-malicious-urls)
  - [Top Industries Affected by Malware Campaigns](#top-industries-affected-by-malware-campaigns)
  - [Top Malware Families](#top-malware-families)
  - [Email Threats](#email-threats)
  - [Threats Blocked](#threats-blocked)
  - [Android Malware Families](#android-malware-families)
  - [Vulnerabilities](#vulnerabilities)
  - [Risk Events](#risk-events)
  - [Recommendations for Lowering Risk](#recommendations-for-lowering-risk)
- [About Trend Micro](#about-trend-micro)

---

## Executive Overview

- **03** APT Campaigns
- **07** Ransomware Threats
- **13** Cloud and Enterprise Threats
- **16** MITRE ATT&CK Detections
- **20** Threat Landscape

---

## APT Campaigns

![Timeline of APT Campaigns spanning April 2022 through December 2023, featuring APT28, Gamaredon, Earth Lusca, Earth Estries, Kimsuky, Void Rabisu, Turla, APT34, Mustang Panda, APT38, Konni Group, and APT29]

### APT28’s NTLMv2 Hash Relay Attacks
- **Timeline:** April 2022 – August 2023
- **Targets:** Organizations involved in a wide range of fields, but primarily in foreign affairs, energy, defense, and transportation.
- **Details:**
  - Possibly an attempt to brute-force its way into target networks.
  - Exploited **CVE-2023-23397**, which was patched in March 2023. At that point, APT28 shifted to more elaborate methods involving scripts hosted on Mockbin sent to targets.

### APT28’s More Recent Credential Phishing Campaign
- **Timeline:** November – December 2023
- **Targets:** Various government organizations in Europe.
- **Details:**
  - Shares similarities to the earlier hash relay campaign in technical indicators, such as sharing the same computer name used to send out spear-phishing emails and to craft LNK files.

### Gamaredon
- **Timeline:** January – November 2023
- **Targets:** Government organizations in Ukraine.
- **Details:**
  - Gamaredon continues its activity with attacks using Remote Template Injection and self-extracting executable files.
  - The timeline of increased activity of the investigated sample suggests the campaign was launched to intensify espionage activities.

### Earth Lusca
- **Timeline:** January – June 2023
- **Targets:** Government departments involved in foreign affairs, technology, and telecommunications in countries across Southeast Asia, Central Asia, and the Balkans, with scattered attacks on Latin American and African countries.
- **Details:**
  - The decrypted payload is a Linux-targeted backdoor, a new variant named **SprySOCKS**.
  - Targets the public-facing servers of its victims.

### Earth Estries
- **Timeline:** January 2023 – present
- **Targets:** Government organizations and technology industries in the Philippines, Taiwan, Malaysia, South Africa, Germany, and the USA.
- **Details:**
  - Uses multiple backdoors and hacking tools, as well as PowerShell downgrade attacks to avoid detection.
  - Abuses public services such as GitHub, Gmail, AnonFiles, and File.io to exchange and transfer commands and stolen data.
  - Earth Estries is known to deploy cyberespionage campaigns.

### Kimsuky’s Continued Activity
- **Timeline:** April 2022, and April – May 2023
- **Targets:**
  - Individuals working in fields related to the Democratic People’s Republic of Korea (DPRK).
  - Possibly organizations related to military, diplomacy, unifications, and Korean-language support groups, based on Kimsuky’s historical campaign footprint.
- **Details:**
  - Delivered as an email file.
  - Likely aimed to gather information on geopolitical events, diplomatic strategies, and activities impacting the target’s interests.
  - Could also be launched to gather armament-related information and conduct cryptocurrency-related attacks.

### Void Rabisu’s Slimmed Down ROMCOM Variant
- **Timeline:** June – August 2023
- **Targets:** Military personnel and political leaders in Europe.
- **Details:**
  - Exploited the then-zero-day vulnerability **CVE-2023-36884**.
  - Primarily known for cyberespionage activities targeting governments and military with financial motivations.

### Turla Attacks Using Capibar and Kazuar
- **Timeline:** July 2023
- **Targets:** Diplomatic and military organizations in Ukraine.
- **Details:**
  - In this phishing campaign, the **Capibar** malware was used for intelligence gathering, while the **Kazuar** malware was used for credential theft.
  - Turla has been active since 2014 and is known for cyberespionage activities.

### APT34’s Targeted Phishing Attack
- **Timeline:** August 2023
- **Targets:** Possibly organizations inside the Kingdom of Saudi Arabia.
- **Details:**
  - The malicious document in the phishing scam dropped a new malware designed for espionage, capable of identifying the machine, reading and uploading files from the machine, and downloading additional files or malware.
  - APT34 is known for cyberespionage activities targeting government agencies, critical infrastructure organizations, and telecommunications in the Middle East.

### Mustang Panda
- **Timeline:** August 2023 – present
- **Targets:** Government organizations in the Philippines and related entities.
- **Details:**
  - Utilized components of legitimate software commonly used in Southeast Asia for DLL sideloading.
  - Possibly launched for information gathering purposes.
  - Samples contain strings suggesting the possibility of targeting Myanmar government officials.

### APT38
- **Timeline:** May – September 2023
- **Targets:** Cryptocurrency-related organizations, investment firms, and banks.
- **Details:**
  - Detected in a sample used by **BlueNoroff**, which is associated with APT38.
  - The sample was later reported by SentinelOne as used in the later stages of **SwiftLoader** and indicated a connection between **KandyKorn** and SwiftLoader.
  - Likely financially motivated and launched to acquire foreign currency to fund armaments and espionage.

### Konni Group
- **Timeline:** November 2023
- **Targets:** Companies within the Republic of Korea.
- **Details:**
  - Associated with OSMIUM, Opal Sleet, SectorA07, TA406, and Kimsuky.
  - Campaign’s malicious ZIP file contains an LNK file that, when executed, drops HTML and VBScript to fetch additional payloads, possibly pointing to APT37.
  - Possibly launched as an additional means of acquiring foreign currency.

### APT29’s VovaMirage Spear Phishing Campaign
- **Timeline:** November 2023
- **Targets:** Embassies and diplomatic entities in European countries, particularly Azerbaijan, Greece, Romania, and Italy.
- **Details:**
  - Exploited WinRAR vulnerability **CVE-2023-38831** in a spear-phishing campaign.
  - Likely launched to gather information on strategic activities involving the targeted countries.

---

## Ransomware Threats

### What to Watch Out For
The following tactics were observed in 2023 and are anticipated to evolve as ransomware activities grow more sophisticated:

- **Continued Increase in Remote Encryption**
  - *Observed in:* Akira, BlackCat, BlackMatter, LockBit, and Royal.
  - *Tactics:* Attackers actively map drives to encrypt on the affected endpoint instead of performing lateral movement. This tactic minimizes their operational footprint on endpoints to evade detection.
- **Maximizing Intermittent Encryption**
  - *Observed in:* NoEscape, Ransomware Play, BlackBasta, Agenda, and BlackCat.
  - *Tactics:* Attackers encrypt chunks of data rather than encrypting entire files in one sequence. This accelerates the encryption process, renders data useless to the victim, and complicates decryption.
- **Endpoint Detection and Response (EDR) Bypass Using Unmonitored Virtual Machines (VMs)**
  - *Observed in:* Akira and BlackCat.
  - *Tactics:* Attackers bypass EDR software by spinning up unmonitored VMs to navigate, map, and encrypt files within Windows Hyper-V hypervisors and attached virtual environments.
- **Multi-Ransomware Attacks**
  - *Tactics:* Initial access brokers sell access to multiple ransomware groups, resulting in layered attacks combining various malware families, data exfiltration, and wiper tools to maximize extortion pressure.

---

### Total Ransomware Detections

![Bar chart showing annual total ransomware detections from 2019 to 2023]

| Year | Detections |
| :--- | :--- |
| **2019** | 61,132,338 |
| **2020** | 41,271,208 |
| **2021** | 14,066,778 |
| **2022** | 14,983,271 |
| **2023** | 14,169,866 |

There has been a general downward trend in total detections, with 2021–2023 volumes averaging less than half of the detections recorded in 2020. However, this should not be misconstrued as a signal to lower defenses. Attackers have shifted away from high-volume, bulk spam campaigns toward targeted operations.

#### Ransomware Detections Breakdown by Service Layer (2021–2023)

![Comparison chart of detections across Email Reputation Service, Web Reputation Service, and File Reputation Service]

| Service | 2021 | 2022 | 2023 | YoY Trend / Notes |
| :--- | :--- | :--- | :--- | :--- |
| **ERS** (Email Reputation Service) | 7,645,171 | 6,647,565 (-15.0%) | 3,633,193 (-52.5%) | Consistent downward trend |
| **WRS** (Web Reputation Service) | 4,917,624 | 2,535,399 (-48.4%) | 1,782,349 (-29.7%) | Downward trend |
| **FRS** (File Reputation Service) | 2,501,589 | 4,802,701 (+92.0%) | 8,754,324 (+82.3%) | Continuous significant increase |

The steady increase in FRS detections suggests attackers are bypassing preliminary perimeter filters using Living-Off-The-Land Binaries/Scripts (LOLBINs/LOLBAs), Bring Your Own Vulnerable Driver (BYOVD) techniques, zero-day exploits, and AV termination tools, forcing detection down to the endpoint payload level.

---

### Operating Systems Affected by Ransomware

#### Linux vs. macOS Detections (2021–2023)

| Year | Linux | macOS |
| :--- | :--- | :--- |
| **2021** | 3,790 | 11,000 |
| **2022** | 27,602 | 15,154 |
| **2023** | 4,949 | 9,961 |

#### Operating System Share of Telemetry (2019–2023)

![Horizontal percentage distribution of ransomware detections across Windows, macOS, and Linux from 2019 to 2023]

| Year | Windows | macOS | Linux |
| :--- | :--- | :--- | :--- |
| **2019** | 97% | 3% | 0% |
| **2020** | 94% | 5% | 1% |
| **2021** | 92% | 5% | 3% |
| **2022** | 71% | 4% | 25% |
| **2023** | 92% | 5% | 3% |

While Linux-targeted ransomware spiked in 2022 (accounting for 25% of telemetry), detections stabilized in 2023 back to historical baselines (4,949 detections, 3% share). macOS ransomware accounted for 9,961 detections in 2023. Windows continues to represent the overwhelming majority of ransomware activity.

---

### Top Countries and Regions by Detected Ransomware Attacks

#### Regional Distribution
- **Asia:** 8,842,873 detections (Thailand accounted for 68% of Asia's detections)
- **Americas:** 1,911,891 detections
- **Europe:** 1,095,868 detections

#### Top 5 Countries
1. **Thailand:** 6,080,644
2. **United States:** 1,640,144
3. **Turkey:** 707,808
4. **Taiwan:** 454,008
5. **India:** 307,658

---

### Top Industries and Segments by Detected Ransomware Attacks

#### By Segment
- **Enterprise:** 166,069 detections
- **Small and Mid-sized Businesses:** 26,430 detections
- **Consumer:** 21,271 detections

#### Top Industries
1. **Banking:** 20.3K
2. **Government:** 9.9K
3. **Technology:** 7.7K
4. **Retail:** 6.3K
5. **Fast-Moving Consumer Goods (FMCG):** 5.6K

---

### Top Ransomware Families

StopCrypt and LockBit maintained the leading positions in 2022 and 2023. In 2023, StopCrypt narrowly surpassed LockBit.

#### 2022 Detections
1. **LockBit:** 3,001
2. **StopCrypt:** 2,898
3. **BlackCat:** 2,781
4. **Wannaren:** 2,511

*LockBit Profile:*
- Created and deployed **StealBit** for automated exfiltration.
- Launched a bug bounty program in 2022.
- LockBit 3.0 shares code similarities with DarkSide and BlackMatter.
- Heavily relies on affiliate networks purchasing initial network access.

#### 2023 Detections
1. **StopCrypt:** 4,277
2. **LockBit:** 4,206
3. **BlackCat:** 3,857
4. **Conti:** 2,470

*StopCrypt Profile:*
- Execution depends on specific command-line arguments, environment configurations, or supplementary components.
- Heavily targeted India in 2023 alongside LockBit and BlackCat.

---

## Cloud and Enterprise Threats

### Risk Events (ASRM)

#### Top Industries by Attack Surface Risk Management (ASRM) Events
1. **Manufacturing:** 21,386,430,411
2. **Healthcare:** 18,436,575,856
3. **Technology:** 17,793,629,116
4. **Retail:** 17,307,436,283
5. **Financial Services:** 13,408,802,186
6. **Government:** 12,077,150,154
7. **Public Services:** 8,954,860,990
8. **Education:** 6,857,317,526
9. **Transportation:** 6,689,288,803
10. **Insurance:** 10,826,646,225 *(as reported in telemetry)*
- **Others:** Remaining event telemetry across unclassified sectors.

---

### Home Network Security Top Events

With hybrid work expanding the threat perimeter into home workspaces, Home Network Security telemetry tracked high-frequency events:

| Rank | Event Type | Detection Count | Description / Attack Vectors |
| :--- | :--- | :--- | :--- |
| **1** | **Brute-Force Login** | 1,234,502,439 | Repeated credential attacks targeting RDP (port 3389), FTP (port 21), or SSH (port 22) using automated wordlists. |
| **2** | **TELNET Default Password Login -6** | 322,792,561 | Detects default Telnet authentication attempts on internal connected devices. |
| **3** | **MISC Bitcoin/Litecoin/Dogecoin Mining Activity -1** | 265,722,686 | Information disclosure and traffic related to unauthorized cryptocurrency mining. |
| **4** | **WEB HTTP Invalid Content-Length -2** | 248,331,853 | Heap buffer overflow exploitation caused by parsing HTTP packets with negative `Content-Length` header values. |
| **5** | **MISC Cryptocurrency Monero Mining Activity -1** | 125,553,894 | Network traffic associated with unauthorized Monero (XMR) mining activity. |

---

### Home Network Security Top Affected Device Types

![Bar chart showing inbound attack counts and device distribution by category]

| Device Type | Total Inbound Attack Detections | Unique Devices Tracked | Average Events per Device |
| :--- | :--- | :--- | :--- |
| **Desktop / Laptop** | 862.8M | 283,384 | 33,900 |
| **Smartphone** | 198.7M | 443,361 | 4,782 |
| **Tablet** | 105.7M | 51,262 | 23,314 |
| **Game Console** | 19.5M | 46,338 | 4,627 |
| **NAS** | 18.4M | 55,915 | 3,676 |

---

### Vulnerabilities by Vendor

Top vendors identified in reported vulnerability advisories:

| Vendor | Disclosed Vulnerabilities |
| :--- | :--- |
| **Adobe** | 369 |
| **Microsoft** | 223 |
| **D-Link** | 176 |
| **PDF-XChange** | 101 |
| **Delta Electronics** | 97 |

---

## MITRE ATT&CK Detections

### Top 5 Tactics Detected (Overall)

Dodging security tools, maintaining command and control over compromised hosts, and gaining initial footholds represent the most prevalent tactics across endpoints, networks, and email:

1. **Defense Evasion (TA0005):** 33,836
2. **Command and Control (TA0011):** 23,642
3. **Initial Access (TA0001):** 21,321
4. **Persistence (TA0003):** 20,465
5. **Impact (TA0040):** 18,335

---

### Top Tactics, Techniques, and Procedures (TTPs) Endpoint

| TTP Category | Detections |
| :--- | :--- |
| **Defense Evasion (TA0005)** | 33,461 |
| **Impact (TA0040)** | 15,990 |
| **Initial Access (TA0001)** | 14,508 |
| **Command and Control (TA0011)** | 14,221 |
| **Execution (TA0002)** | 13,871 |

---

### Top TTPs Network

| TTP Category | Detections |
| :--- | :--- |
| **Command and Control (TA0011)** | 5,957 |
| **Lateral Movement (TA0008)** | 4,642 |
| **Initial Access (TA0001)** | 3,839 |
| **Execution (TA0002)** | 3,356 |
| **Impact (TA0040)** | 1,705 |

---

### TTPs Overall Trend by Detections

*Note: Monthly detection data omits May and June due to a logging telemetry outage during that period.*

- **Command and Control (TA0011):** Rose gradually across Q4, climbing steadily from September to December.
- **Defense Evasion (TA0005):** Peaked sharply in March and July before declining across the fourth quarter.
- **Execution (TA0002):** Reached peak top-three detection volumes in July and August.
- **Impact (TA0040):** Displayed irregular distribution, characterized by a sharp spike in November.
- **Persistence (TA0003):** Prominent in Q1 but dropped out of top-ranked positions thereafter.
- **Initial Access (TA0001):** Maintained consistent, moderate baselines throughout all operational months.

#### Monthly Top 3 TTP Breakdowns

| Month | Rank 1 TTP (Count) | Rank 2 TTP (Count) | Rank 3 TTP (Count) |
| :--- | :--- | :--- | :--- |
| **January** | Persistence [TA0003] (5,299) | Defense Evasion [TA0005] (3,573) | Impact [TA0040] (1,728) |
| **February** | Persistence [TA0003] (5,275) | Impact [TA0040] (1,636) | Initial Access [TA0001] (1,587) |
| **March** | Defense Evasion [TA0005] (6,015) | Impact [TA0040] (2,837) | Initial Access [TA0001] (1,947) |
| **April** | Persistence [TA0003] (5,012) | Impact [TA0040] (2,112) | Initial Access [TA0001] (1,679) |
| **July** | Defense Evasion [TA0005] (5,440) | Execution [TA0002] (5,244) | Collection [TA0009] (4,567) |
| **August** | Defense Evasion [TA0005] (2,620) | Execution [TA0002] (2,457) | Initial Access [TA0001] (1,649) |
| **September** | Command and Control [TA0011] (2,695) | Initial Access [TA0001] (2,399) | Impact [TA0040] (1,713) |
| **October** | Command and Control [TA0011] (2,980) | Initial Access [TA0001] (2,532) | Impact [TA0040] (1,714) |
| **November** | Command and Control [TA0011] (3,305) | Initial Access [TA0001] (2,638) | Impact [TA0040] (2,386) |
| **December** | Command and Control [TA0011] (3,804) | Initial Access [TA0001] (2,579) | Impact [TA0040] (1,739) |

---

### Living-Off-The-Land Tactics

Threat actors predominantly relied on established, dual-use administration and penetration-testing software rather than proprietary tooling to evade heuristic controls and ensure post-exploitation stability.

![Comparative bar chart comparing detections of Mimikatz, Cobalt Strike, Brute Ratel, and GMER between 1H 2023 and 2H 2023]

| Tool | Primary TTP Classification | Subcategory | 1H 2023 Detections | 2H 2023 Detections |
| :--- | :--- | :--- | :--- | :--- |
| **Mimikatz** | Credential Access / Collection | Fileless / Credential Stealer | 8,956 | 7,513 |
| **Cobalt Strike** | Command and Control (TA0011) | Backdoor / Trojan | 3,747 | 3,914 |
| **Brute Ratel** | Command and Control (TA0011) | Backdoor / C2 Framework | 244 | 381 |
| **GMER** | Defense Evasion (TA0005) | Rootkit / Anti-AV Utility | 30 | 0 |

---

## Threat Landscape

### Malware Detection

#### Top Countries With the Most Malware Detections & Targeted Industries
*Note: Industry detection counts are limited to telemetry from organizations that provide sector identification.*

1. **Japan:** 1,169,219,233 Total Detections
   - *Manufacturing:* 4,206
   - *Education:* 3,813
   - *Healthcare:* 3,809
2. **United States:** 993,996,354 Total Detections
   - *Healthcare:* 45,030
   - *Technology:* 36,021
   - *Manufacturing:* 9,410
3. **India:** 288,557,845 Total Detections
   - *Manufacturing:* 34,110
   - *Government:* 31,273
   - *Banking:* 30,253
4. **Italy:** 277,616,731 Total Detections
   - *Healthcare:* 15,086
   - *Banking:* 12,332
   - *Government:* 9,490
5. **Brazil:** 256,383,037 Total Detections
   - *Government:* 43,300
   - *Education:* 17,623
   - *Financial:* 8,051

---

### Top Countries Accessing Malicious URLs

1. **Japan:** 823,057,759
2. **United States:** 382,881,197
3. **Taiwan:** 95,100,913
4. **China:** 84,300,801
5. **Philippines:** 76,730,598

---

### Top Industries Affected by Malware Campaigns

Aggregated data from the Smart Protection Network (SPN):
- **Government:** 302,555
- **Healthcare:** 228,100
- **Manufacturing:** 212,100
- **Education:** 179,800
- **Banking:** 176,400

---

### Top Malware Families

Cryptocurrency mining malware overtook persistent web backdoors as the most prevalent commodity threat.

![Bar chart comparing top malware families between 2022 and 2023]

#### 2022 Top Families
1. **Webshell:** 303,399
2. **Emotet:** 249,949
3. **Negasteal:** 192,658
4. **Nemucod:** 125,204
5. **Powload:** 124,443

#### 2023 Top Families
1. **CoinMiner:** 74,933
2. **Webshell:** 59,788
3. **Powload:** 45,658
4. **Bondat:** 44,617
5. **Downad:** 43,013

#### CoinMiner Profile
- **Recent Vectors:** Exploitation of unpatched Oracle WebLogic Server instances (**CVE-2020-14882**) and malicious Python Package Index (PyPI) packages targeting Linux systems.
- **Objective:** Consumes host CPU and GPU capacity to mine cryptocurrency (predominantly Monero).
- **Indicators of Compromise:**
  - High CPU consumption linked to `powershell.exe` or `schtasks.exe`.
  - Detection of network indicators matching `Monero.Cryptocurrency.Miner`.
  - Persistence established via Service Installation or WMI PowerShell scripts executing on Domain Controllers.

#### Webshell Profile
- Deployed through exploits against internet-facing web applications to maintain unauthorized server persistence.

---

### Email Threats

#### Top Countries by Email Threat Detection
1. **United States:** 10,425,179,000
2. **China:** 2,079,512,425
3. **Netherlands:** 1,222,110,043
4. **Russia:** 1,214,975,535
5. **Germany:** 1,101,398,365

#### High-Risk Email Threat Trends (2022 vs. 2023)

| Threat Category | 2022 Count | 2023 Count | YoY Percentage Shift |
| :--- | :--- | :--- | :--- |
| **Total Malware Detections** | 4,263,650 | 19,149,460 | +349% |
| **Malicious & Phishing URLs** | 35,256,360 | 25,665,848 | -27% |
| **Business Email Compromise (BEC)** | 383,926 | 446,234 | +16% |

Attackers are shifting away from broad phishing link deployment toward spear-phishing, targeted BEC scams, and attachments with nested malicious code to evade perimeter URL analyzers.

#### Top 5 Malicious Spam Attachment Extensions
1. **PDF:** 10,262,737
2. **EXE:** 2,007,619
3. **DOCX:** 1,884,077
4. **HTML:** 700,566
5. **DOC:** 448,155

#### Spam Attachment Distribution per Month (2023)
- **January:** 453,181
- **February:** 481,862
- **March:** 1,297,818
- **April:** 1,062,592
- **May:** 2,121,029
- **June:** 3,972,265 *(Annual Peak)*
- **July:** 2,667,467
- **August:** 1,080,318
- **September:** 1,124,230
- **October:** 998,806
- **November:** 918,126
- **December:** 295,801

---

### Threats Blocked

In 2023, Trend Micro's Smart Protection Network (SPN) blocked **161,014,076,615** total threats—a 10% increase over 2022 (**146,408,535,569**).

#### Annual Threats Blocked (2016–2023)
- **2016:** 81,885,110,904
- **2017:** 66,495,590,128
- **2018:** 48,473,430,401
- **2019:** 54,195,862,697
- **2020:** 66,495,174,311
- **2021:** 94,289,585,240
- **2022:** 146,408,535,569
- **2023:** 161,014,076,615

#### Detections by SPN Layer (2021–2023)

![Comparative trends across ERS, WRS, and FRS protection networks]

| Layer | 2021 | 2022 | 2023 | YoY Trend |
| :--- | :--- | :--- | :--- | :--- |
| **ERS** (Email) | 73,858,986,744 | 79,945,411,146 | 69,869,979,425 | -14.4% (2023 vs 2022) |
| **WRS** (Web) | 3,468,559,504 | 2,531,040,185 | 2,356,888,444 | -6.9% (2023 vs 2022) |
| **FRS** (File) | 17,834,808,438 | 60,925,991,943 | 82,149,430,110 | +34.8% (following +241.6% in 2022) |

#### Threats Blocked Across Mobile, IoT, and Smart Home Telemetry

| Service | 2021 | 2022 | 2023 |
| :--- | :--- | :--- | :--- |
| **MARS** (Mobile App Reputation) | 37,088,836 | 36,547,933 | 35,762,472 |
| **SHN** (Smart Home Network) | 3,073,227,623 | 2,966,079,048 | 2,611,751,397 |
| **IoTRS** (IoT Reputation Service) | 5,921,414 | 3,465,314 | 1,257,448 |

---

### Android Malware Families

Top detected mobile malware packages targeting the Android platform in 2023:

1. **XLoaderPacker:** 3,030,515
   - *Profile:* Manually installed spyware masquerading as benign applications. Capable of intercepting incoming/outgoing voice calls and locking device screens.
2. **KeepSpy:** 2,475,757
   - *Profile:* Sideloaded via TianySpy smishing lures. Masquerades as legitimate apps to steal banking credentials and exfiltrate Wi-Fi settings.
3. **Xloader:** 920,098
4. **MMRat:** 645,888
5. **CovidRansom:** 247,555

---

### Vulnerabilities

#### Published Zero-Day Initiative (ZDI) Advisories
- **2022:** 1,706 advisories
- **2023:** 1,913 advisories

#### Monthly Published Zero-Day Advisories (2023)
- **January:** 109
- **February:** 109
- **March:** 283
- **April:** 157
- **May:** 293 *(Annual Peak)*
- **June:** 176
- **July:** 114
- **August:** 117
- **September:** 93
- **October:** 83
- **November:** 200
- **December:** 179

#### Industrial Control Systems (ICS) vs. ICS Zero-Day Vulnerabilities (2023)

| Month | ICS Advisories | ICS Zero-Day Vulnerabilities |
| :--- | :--- | :--- |
| **January** | 9 | 0 |
| **February** | 26 | 0 |
| **March** | 35 | 0 |
| **April** | 4 | 0 |
| **May** | 47 | 12 |
| **June** | 43 | 0 |
| **July** | 5 | 0 |
| **August** | 36 | 15 |
| **September** | 1 | 0 |
| **October** | 15 | 0 |
| **November** | 32 | 0 |
| **December** | 8 | 29 |

#### Monthly Non-ICS and N-Day Vulnerabilities (2023)
- **January:** 181
- **February:** 84
- **March:** 223
- **April:** 141
- **May:** 193
- **June:** 105
- **July:** 111
- **August:** 83
- **September:** 47
- **October:** 42
- **November:** 143
- **December:** 106

#### Top 3 Riskiest Unpatched CVEs

| Vulnerability | Vulnerability Name & Scope | CVSS Base Score | Affected Customer Count | Unpatched Customer Count |
| :--- | :--- | :--- | :--- | :--- |
| **CVE-2023-24880** | Windows SmartScreen Security Feature Bypass | 4.4 (*Medium*) | 60,731 | 59,798 |
| **CVE-2023-21823** | Windows Graphics Component Remote Code Execution | 7.8 (*High*) | 58,184 | 57,808 |
| **CVE-2023-23376** | Windows Common Log File System Driver Elevation of Privilege | 7.8 (*High*) | 58,173 | 57,797 |

---

### Risk Events

#### Top 2 Risk Events Detected (ASRM)
1. **Risky Cloud App Access:** 82,976,277,500
2. **Risky Website Access Detected:** 18,819,067,819

#### Top Countries with Risk Events Detected
1. **United States:** 31,271,416,757
2. **India:** 16,570,427,847
3. **Brazil:** 15,060,300,143
4. **Great Britain:** 7,888,655,174
5. **Germany:** 7,816,148,246

---

### Recommendations for Lowering Risk

1. **Patching and System Upgrades:** Promptly install the latest security updates, vendor patches, or operating system upgrades.
2. **Virtual Patching and Prevention Rules:** Apply proactive prevention and IPS rules from security controls to shield unpatched vulnerabilities from active exploitation.
3. **Environment Hardening:** Audit and optimize weak system configurations and default credentials.
4. **Cloud Governance:** Restrict unauthorized cloud services; formally sanction approved enterprise tools while blocking high-risk shadow IT apps.
5. **Identity and Access Management (IAM):** Enforce strong password complexity, disable dormant accounts, and mandate Account Lockout Policies within Active Directory environments.
6. **Device Containment:** Restrict user accounts on compromised endpoints, isolate at-risk hosts, and remediate high-risk detections identified through telemetry.

---

## About Trend Micro

Trend Micro, a global cybersecurity leader, helps make the world safe for exchanging digital information. Fueled by decades of security expertise, global threat research, and continuous innovation, our unified cybersecurity platform protects over 500,000 organizations and millions of individuals across clouds, networks, devices, and endpoints.

The **Trend Vision One™** unified cybersecurity platform delivers advanced threat defense techniques, extended detection and response (XDR), and integration across the IT ecosystem, including AWS, Microsoft, and Google, enabling organizations to better understand, communicate, and mitigate cyber risk.

Trend Micro’s global threat research team delivers unparalleled intelligence and insights that power our cybersecurity platform and help protect organizations around the world from hundreds of millions of threats daily. We have 7,000 employees across 65 countries, singularly focused on security and passionate about making the world a safer and better place.

- **Website:** [TrendMicro.com](https://www.trendmicro.com)

*© 2024 by Trend Micro, Incorporated. All rights reserved. Trend Micro and the Trend Micro t-ball logo are trademarks or registered trademarks of Trend Micro, Incorporated. All other company and/or product names may be trademarks or registered trademarks of their owners.*

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-11-14", "model": "gemini-3.7-flash"} -->
