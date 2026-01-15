# CALIBRATING EXPANSION

## 2023 ANNUAL CYBERSECURITY REPORT

## Table of Contents
- [APT CAMPAIGNS](#apt-campaigns)
- [RANSOMWARE THREATS](#ransomware-threats)
- [CLOUD AND ENTERPRISE THREATS](#cloud-and-enterprise-threats)
- [MITRE ATT&CK DETECTIONS](#mitre-att-ck-detections)
- [THREAT LANDSCAPE](#threat-landscape)

---

## APT CAMPAIGNS

### Timeline of Activity
- **APR 2022 – AUG 2023**: APT28’s NTLMv2 hash relay attacks
- **NOV – DEC 2023**: APT28’s more recent credential phishing campaign
- **JAN – NOV 2023**: Gamaredon
- **JAN – JUN 2023**: Earth Lusca
- **JAN 2023 – present**: Earth Estries
- **APR 2022, and APR – MAY 2023**: Kimsuky’s continued activity
- **JUN – AUG 2023**: Void Rabisu’s slimmed down ROMCOM variant
- **JUL 2023**: Turla attacks using Capibar and Kazuar
- **AUG 2023**: APT34’s targeted phishing attack
- **AUG 2023 – present**: Mustang Panda
- **MAY – SEP 2023**: APT38
- **NOV 2023**: Konni Group
- **NOV 2023**: APT29’s VovaMirage spear phishing campaign

### APT28’s NTLMv2 hash relay attacks
**April 2022 – August 2023**

**Targets:**
- Organizations involved in a wide range of fields, but primarily in foreign affairs, energy, defense, and transportation.

**Details:**
- Possibly an attempt to brute-force its way into target networks.
- Exploited CVE-2023-23397 that was patched in March 2023, at which point APT28 used more elaborate methods that involved scripts hosted on Mockbin sent to targets.

### APT28’s more recent credential phishing campaign
**November – December 2023**

**Targets:**
- Various government organizations in Europe.

**Details:**
- Shares similarities to the earlier hash relay campaign in technical indicators, such as sharing the same computer name used to send out spear-phishing emails and to craft LNK files.

### Gamaredon
**January – November 2023**

**Targets:**
- Government organizations in Ukraine.

**Details:**
- Gamaredon continues its activity with attacks using Remote Template Injection and self-extracting executable files.
- The timeline of increased activity of the investigated sample suggests the campaign was launched to intensify espionage activities.

### Earth Lusca
**January – June 2023**

**Targets:**
- Government departments involved in foreign affairs, technology, and telecommunications in countries in Southeast Asia, Central Asia, and the Balkans, with scattered attacks on Latin American and African countries.

**Details:**
- Targets the public-facing servers of its victims.
- The decrypted payload is a Linux-targeted backdoor, a new variant named SprySOCKS.

### Earth Estries
**January 2023 – present**

**Targets:**
- Government organizations and technology industries in the Philippines, Taiwan, Malaysia, South Africa, Germany, and the USA.

**Details:**
- They use multiple backdoors and hacking tools, as well as PowerShell downgrade attacks to avoid detection.
- They use public services such as Github, Gmail, AnonFiles, and File.io to exchange and transfer commands and stolen data.
- Earth Estries is known to deploy cyberespionage campaigns.

### Kimsuky’s continued activity
**April 2022, and April – May 2023**

**Targets:**
- Individuals working in fields related to the Democratic People’s Republic of Korea.
- Possibly organizations related to military, diplomacy, and unifications, and Korean-language support groups, based on Kimsuky’s previous campaign history.

**Details:**
- Delivered as an email file.
- Likely aimed to gather information on geopolitical events, diplomatic strategies, and activities impacting the target’s interests.
- Could also be launched to gather armament-related information and for cryptocurrency-related attacks.

### Void Rabisu’s slimmed down ROMCOM variant
**June – August 2023**

**Targets:**
- Military personnel and political leaders in Europe.

**Details:**
- Exploited the then zero-day vulnerability CVE-2023-36884.
- Primarily known for cyberespionage activities targeting governments and military with financial motivations.

### Turla attacks using Capibar and Kazuar
**July 2023**

**Targets:**
- Diplomatic and military organizations in Ukraine.

**Details:**
- In this phishing campaign, the Capibar malware was used for intelligence gathering, while the Kazuar malware was used for credential theft.
- Turla has been active since 2014, and is known for its cyberespionage activities.

### APT34’s targeted phishing attack
**August 2023**

**Targets:**
- Possibly organizations inside the Kingdom of Saudi Arabia.

**Details:**
- The malicious document in the phishing scam dropped a new malware designed for espionage, capable of identifying the machine, reading and uploading files from the machine, and downloading another file or malware.
- APT34 is known for its cyberespionage activities targeting government agencies, organizations involved in critical infrastructure, and telecommunications in the Middle East.

### Mustang Panda
**August 2023 – present**

**Targets:**
- Government organizations in the Philippines, and other related organizations.

**Details:**
- Utilized components of legitimate software commonly used in Southeast Asia for DLL sideloading.
- Possibly launched for information gathering purposes.
- Samples contain strings that suggest the possibility of attacking Myanmar government officials.

### APT38
**May – September 2023**

**Targets:**
- Cryptocurrency-related organizations, investment firms, and banks.

**Details:**
- Detected in a sample used by BlueNoroff, which is associated with APT38. The sample was later reported by SentinelOne as used in the later stages of SwiftLoader and indicated in a connection between KandyKorn and SwiftLoader.
- Likely financially motivated and launched to acquire foreign currency to fund armaments and espionage.

### Konni Group
**November 2023**

**Targets:**
- Companies within the Republic of Korea.

**Details:**
- Associated with OSMIUM, Opal Sleet, SectorA07, TA406, and Kimsuky.
- According to our analysis, the campaign’s malicious zip file contains an LNK file, that when executed drops html and VBScript to fetch additional payloads, possibly pointing to APT37.
- Possibly launched as additional means of acquiring foreign currency.

### APT29’s VovaMirage spear phishing campaign
**November 2023**

**Targets:**
- Embassies and diplomatic entities in European countries, particularly Azerbaijan, Greece, Romania, and Italy.

**Details:**
- Exploited WinRAR vulnerability CVE-2023-38831 in a spear phishing campaign.
- Likely launched to gather information on strategic activities involving the respective country targets.

---

## RANSOMWARE THREATS

### What to Watch Out For
The following tactics were observed in 2023 and could possibly be seen in the coming year as ransomware activities grow more sophisticated.

- **Continued increase in the use of remote encryption**:
    - Observed in Akira, BlackCat, BlackMatter, LockBit, and Royal.
    - Attackers actively map drives to encrypt on the affected endpoint instead of doing lateral movement. This could be a leap in tactics to reduce their footprint in attacks to avoid detection.
- **Ransomware groups are also maximizing the convenience of intermittent encryption**:
    - Observed in NoEscape, Ransomware Play, BlackBasta, Agenda, and BlackCat.
    - Attackers encrypt chunks of data instead of encrypting all data in one go; this process speeds up encryption while still rendering the affected data useless to the victim, and also makes for a more complicated decryption process.
- **Endpoint Detection and Response (EDR) bypass using unmonitored virtual machines (VM)**:
    - Observed in Akira and BlackCat.
    - Attackers bypass EDR by creating unmonitored VMs to navigate, map and encrypt files within the Windows Hyper-V hypervisor systems and attached VMs.
- **Multi-ransomware attacks**:
    - The initial attacker sells its access to other ransomware groups to launch multiple attacks with a combination of malware, data theft, and wiper tools to maximize manipulation and pressure against the victims.

### Total Ransomware Detections
- **2019**: 14,066,778
- **2020**: 14,983,271
- **2021**: 14,169,866
- **2022**: 7,645,171
- **2023**: 4,917,624

There has been a general downward trend in ransomware detections, with detections from 2021 to 2023 averaging less than half of the recorded detections in 2020; however, this should not be misconstrued as a cue for security operations centers and decision-makers to lower their guards. Historically, ransomware attacks were launched in “bulk,” such as spam campaigns with malicious links, but attacks that focus on quantity can more easily be blocked, as shown in our ransomware ERS and WRS data in the following figure. These figures show a general downward trend consistent with the total ransomware detections.

However, a continued increase in FRS detections could suggest that attackers are using more effective ways to evade preliminary detection by focusing on arrival and defense evasion techniques such as Living-Off-The-Land Binaries and Scripts (LOLBINs/LOLBAs), Bring Your Own Vulnerable Driver (BYOVD), zero-day exploits, and AV termination. We detect and identify ransomware payloads as malicious at endpoint as the ways they get into systems become more complex. This pattern is also observed in SPN data for overall threats blocked.

- **ERS Detections:**
    - **2021**: 8,754,324 (52.5%)
    - **2022**: 4,802,701 (15.0%)
    - **2023**: 2,501,589 (29.7%)
- **WRS Detections:**
    - **2021**: 3,633,193
    - **2022**: 1,782,349
    - **2023**: 92.0%
- **FRS Detections:**
    - **2021**: 5M
    - **2022**: 4M
    - **2023**: 3M (82.3%)

### Operating Systems Affected by Ransomware
- **Windows Detections:**
    - **2019**: 97%
    - **2020**: 94%
    - **2021**: 92%
    - **2022**: 71%
    - **2023**: 92%
- **MacOS Detections:**
    - **2019**: 3%
    - **2020**: 5%
    - **2021**: 5%
    - **2022**: 4%
    - **2023**: 5%
- **Linux Detections:**
    - **2019**: 0%
    - **2020**: 1%
    - **2021**: 3%
    - **2022**: 25%
    - **2023**: 3%

Based on data from our midyear report, customer detections on Linux-targeted ransomware attacks from the first half of 2023 continues to overshadow MacOS attacks. This is consistent with data gathered from 2022, which was an exceptional year for Linux-based malware detections, making up 25% of our telemetry; previously, Linux-targeted attacks only made up two to three percent of the OS ratio. It should be noted that Windows continues to take the bulk of our ransomware detections, with the only significant decrease in 2022.

However, as our data for 2023 was completed, MacOS ransomware attacks came out higher with 9,961 detections, while Linux detections were finalized at 4,949. This could suggest that Linux-targeted attacks are stabilizing after the influx of novel Linux variants in 2022 to early 2023, but it could also be influenced by the overall decrease in ransomware activity.

### Top Countries and Regions by Detected Ransomware Attacks
1.  **United States**: 8,842,873
2.  **Thailand**: 6,080,644 (68% of ransomware detections in Asia)
3.  **Turkey**: 1,911,891
4.  **India**: 1,095,868
5.  **Taiwan**: 707,808

### Top Industries and Segments by Detected Ransomware Attacks
- **Enterprises**: 166,069
- **Banking**: 20.3K
- **Government**: 9.9K
- **Technology**: 7.7K
- **Retail**: 6.3K
- **Fast-Moving Consumer Goods**: 5.6K

Industry rankings and segment breakdowns based on unique detection counts at the endpoint shows that enterprises are the primary targets, with significant interest in the banking sector in 2023.

### Top Ransomware Families
- **2022:**
    - LockBit: 4,277
    - StopCrypt: 4,206
    - BlackCat: 3,857
    - Wannaren: 2,470
- **2023:**
    - StopCrypt: 4,277
    - LockBit: 4,206
    - BlackCat: 3,857
    - Conti: 2,470

StopCrypt and LockBit maintain the top spots in terms of most prolific ransomware families for 2023 as it did in the previous year, but the former overtook the latter by a narrow margin this year. Note that this data does not include legacy ransomware families.

- **LockBit:**
    - Created and uses the malware StealBit for automated data exfiltration.
    - Launched a bug bounty program in 2022.
    - LockBit 3.0 has code that shares similarities to DarkSide and BlackMatter.
    - Maximizes affiliates who buy access to targets from other threat actors.
- **StopCrypt:**
    - Requires being executed with specific arguments or parameters, additional components or in a specific environment to proceed with its routine.
    - Reported to have heavily targeted India in 2023 alongside LockBit and BlackCat.

---

## CLOUD AND ENTERPRISE THREATS

### Risk Events
**Top Industries by Risk Events (ASRM)**
- Manufacturing: 21,386,430,411
- Healthcare: 18,436,575,856
- Technology: 17,793,629,116
- Retail: 17,307,436,283
- Financial Services: 13,408,802,186
- Government: 12,077,150,154
- Public Services: 8,954,860,990
- Education: 6,857,317,526
- Transportation: 6,689,288,803
- Insurance: 10,826,646,225

### Home Network Security Top Events
1.  **Brute-Force Login**: 1,234,502,439
    - Might be RDP via port 3389, FTP via port 21, or SSH via port 22 to repeatedly attempt to log in to target hosts using a dictionary of common usernames and passwords.
2.  **TELNET Default Password Login**: 322,792,561
    - Detects when a user within the network uses the default password to log in.
3.  **MISC Bitcoin/Litecoin/Dogecoin Mining Activity**: 265,722,686
    - Related to information disclosure and possibly to Bitcoin/Litecoin/Dogecoin Mining Activity.
4.  **WEB HTTP Invalid Content-Length**: 248,331,853
    - Caused by an error in processing HTTP packets containing negative Content-Length header field values that result in a heap buffer overflow.
5.  **MISC Cryptocurrency Monero Mining Activity**: 125,553,894
    - Possible Monero (XMR) cryptocurrency mining activity.

### Home Network Security Top Affected Device Types
- **Desktop/Laptop Devices**: 862.8M (Average: 33,900)
- **Smartphone Devices**: 443,361 (Average: 23,314)
- **Tablet Devices**: 198.7M (Average: 4,782)
- **Game Console Devices**: 105.7M (Average: 51,262)
- **NAS Devices**: 19.5M (Average: 4,627)

Desktops and laptops recorded the most inbound attack detections based on our Home Network Security telemetry data.

### Vulnerability by Vendor
- Adobe: 369
- Microsoft: 223
- D-Link: 176
- PDF-XChange: 101
- Delta Electronics: 97

---

## MITRE ATT&CK DETECTIONS

### Top 5 Tactics Detected (Overall)
1.  **Defense Evasion (TA0005)**: 33,836
2.  **Command and Control (TA0011)**: 23,642
3.  **Initial Access (TA0001)**: 21,321
4.  **Persistence (TA0003)**: 20,465
5.  **Impact (TA0040)**: 18,335

Dodging security tools, communication and control of compromised systems, and gaining a foothold within victim’s systems and networks are the most used TTPs (overall, endpoints, network, and email).

### Top Tactics, Techniques, and Procedures (TTPs) Endpoint
1.  **Defense Evasion (TA0005)**: 33,461
2.  **Impact (TA0040)**: 15,990
3.  **Initial Access (TA0001)**: 14,508
4.  **Command and Control (TA0011)**: 14,221
5.  **Execution (TA0002)**: 13,871

### Top TTPs Network
1.  **Command and Control (TA0011)**: 5,957
2.  **Lateral Movement (TA0008)**: 4,642
3.  **Initial Access (TA0001)**: 3,839
4.  **Execution (TA0002)**: 3,356
5.  **Impact (TA0040)**: 1,705

### TTPs Overall Trend by Detections
Command and Control showed a gradual increase from September to December, while Defense Evasion peaked in March and July before declining in customer detections in subsequent months. Execution entered the top three TTPs detected in July and August, while Impact showed no clear trend despite a spike in November. Persistence only entered the top three in the first quarter of the year but was in a downward trend before dipping below the top three. Despite fluctuations, Initial Access maintains a moderate number of detections, since it is the primary goal of threat actors to gain a foothold in target victim systems and networks.

*Note: The monthly detections do not show data for May and June due to a system error experienced during that period.*

- **January**:
    - Persistence (TA0003): 5,299
    - Defense Evasion (TA0005): 2,837
    - Impact (TA0040): 1,728
- **February**:
    - Persistence (TA0003): 5,275
    - Impact (TA0040): 1,636
    - Initial Access (TA0001): 1,587
- **March**:
    - Defense Evasion (TA0005): 6,015
    - Initial Access (TA0001): 3,573
    - Impact (TA0040): 1,947
- **April**:
    - Persistence (TA0003): 5,440
    - Impact (TA0040): 5,244
    - Initial Access (TA0001): 4,567
- **July**:
    - Defense Evasion (TA0005): 5,012
    - Execution (TA0002): 2,620
    - Initial Access (TA0001): 2,457
- **August**:
    - Defense Evasion (TA0005): 2,112
    - Execution (TA0002): 2,695
    - Initial Access (TA0001): 2,399
- **September**:
    - Command and Control (TA0011): 2,980
    - Initial Access (TA0001): 2,532
    - Impact (TA0040): 1,714
- **October**:
    - Command and Control (TA0011): 3,305
    - Initial Access (TA0001): 2,638
    - Impact (TA0040): 2,386
- **November**:
    - Command and Control (TA0011): 3,804
    - Initial Access (TA0001): 2,579
    - Impact (TA0040): 1,739
- **December**:
    - Command and Control (TA0011): 3,468,559,504
    - Initial Access (TA0001): 3,073,227,623
    - Impact (TA0040): 1,257,448

### Living-Off-The-Land Tactics
- **Mimikatz**: 8,956 (Preferred for its effectiveness in harvesting data while evading detection)
- **Cobalt Strike**: 7,513 (Favored for Command and Control as this tactic requires stealth and resilience to remain undetected within compromised networks for an extended period)
- **Brute Ratel**: 3,914
- **GMER**: 381

There is no clear trend in the detections, though Mimikatz and Cobalt Strike continue to be the preferred legitimate tools to abuse to aid criminal activity. It can be assumed that threat actors prefer to use well-known tools instead of exploring novel ones, a logical behavior that is commonly observed as it guarantees more likelihood of success with less effort.

---

## THREAT LANDSCAPE

### Malware Detection
**Countries With the Most Malware Detections and the corresponding top industries targeted for each**
1.  **Japan**: 1,169,219,233
    - Manufacturing
    - Education
    - Healthcare
2.  **United States**: 993,996,354
    - Healthcare
    - Technology
    - Manufacturing
3.  **India**: 288,557,845
    - Manufacturing
    - Government
    - Banking
4.  **Italy**: 277,616,731
    - Healthcare
    - Banking
    - Government
5.  **Brazil**: 256,383,037
    - Government
    - Education
    - Financial

*Note that industry data counts are limited to customers who have elected to provide details pertaining to the business sectors in which they belong. Total malware detection counts include customers who did not provide any information on their industries.*

### Top Countries Accessing Malicious URLs
1.  **Japan**: 823,057,759
2.  **United States**: 382,881,197
3.  **China**: 95,100,913
4.  **Taiwan**: 84,300,801
5.  **Philippines**: 76,730,598

### Top Industries Affected by Malware Campaigns
- **Government**: 302.6K detections
- **Healthcare**: 228.1K detections
- **Manufacturing**: 212.1K detections
- **Education**: 179.8K detections
- **Banking**: 176.4K detections

From the aggregate average of our Smart Protection Network (SPN) data, malware campaigns targeted government organizations the most with 302,555 detections.

### Top Malware Families
- **2022:**
    - Webshell: 192,658
    - Emotet: 125,204
    - Negasteal: 124,443
    - Nemucod: 74,933
    - Powload: 59,788
- **2023:**
    - CoinMiner: 303,399
    - Webshell: 249,949
    - Powload: 45,658
    - Bondat: 44,617
    - Downad: 43,013

A cryptocurrency mining malware surpassed prolific names in 2023. Personal data remains the most valuable commodity in underground criminal communities; cryptocurrency wallets and crypto-related data are the most actionable data that can be stolen by malicious actors, equivalent to cash that can immediately be spent without traceability.

- **CoinMiner**:
    - Uses the victim system’s central processing unit (CPU) and/or graphical processing unit (GPU) resources to mine cryptocurrency.
    - The following can be observed during the infection:
        - High CPU utilization either with powershell.exe or schtasks.exe.
        - Monero.Cryptocurrency.Miner app detection from the network.
        - Execution source can be identified during service installation.
        - WMI powershell scripts on the DC server.
- **Webshell**:
    - Exploits vulnerabilities in internet-facing web servers.
    - Last reported exploit: Oracle WebLogic Server vulnerabilities (CVE-2020-14882).
    - Reported to have been deployed by malicious Python Package Index packages targeting Linux.

### Email Threats
**Top Countries by Detection**
1.  **United States**: 10,425,179,000
2.  **China**: 2,079,512,425
3.  **Netherlands**: 1,222,110,043
4.  **Russia**: 1,214,975,535
5.  **Germany**: 1,101,398,365

**High-Risk Email Threats**
- Total malware detection count:
    - **2022**: 4,263,650
    - **2023**: 19,149,460 (349%)
- Total malicious and phishing URLs count:
    - **2022**: 35,256,360
    - **2023**: 25,665,848 (-27%)
- Total business email compromise count:
    - **2022**: 383,926
    - **2023**: 446,234 (16%)

While there is a decrease in malicious and phishing URL detections from 2022 to 2023, the increase in malware detection count and BEC count suggests the change in the threat landscape that finds attackers making use of more sophisticated ways to avoid detection. In this case, instead of focusing on malicious and phishing URLs to randomly victimize users, BEC schemes suggest more targeted operations, while a closer look at our malware detection count includes phishing links embedded within the attachments. This is consistent with patterns observed in our SPN data on threats blocked from 2021 to 2023, where detections that rely on attribution of URLs (WRS) and emails (ERS) show a decrease, while endpoint detections that directly identify malicious files have consistently increased.

### Top 5 Spam Attachments
1.  **PDF**: 10,262,737
2.  **EXE**: 2,007,619
3.  **DOCX**: 1,884,077
4.  **HTML**: 700,566
5.  **DOC**: 448,155

**Spam attachments per month of 2023**
- JAN: 3,972,265
- FEB: 2,667,467
- MAR: 2,121,029
- APR: 1,124,230
- MAY: 453,181
- JUN: 481,862
- JUL: 295,801
- AUG: 1,297,818
- SEP: 1,062,592
- OCT: 1,080,318
- NOV: 998,806
- DEC: 918,126

There is a general increasing trend for the first half of the year, where malicious spam attachment detections peaked in June. This is followed by fluctuations in the second half of the year, that eventually decline until December. Despite more cunning ways to lure victims into clicking malicious links, spam campaigns remain a go-to for cybercriminals.

### Threats Blocked
- **Overall threats blocked in 2022**: 146.4B
- **Overall threats blocked in 2023**: 161.0B

The total number of threats blocked based on our SPN reached a record high in 2023, 10% higher from the previous year. It also continues the dramatic climb of threats blocked that began to be recorded in 2021, the first year that surpassed the previous peak of 82 billion in 2016. This coincided with the pandemic, strongly suggesting its role in driving the upswing.

- **ERS**:
    - **2021**: 82,149,430,110
    - **2022**: 60,925,991,943
    - **2023**: 79,945,411,146 (7.6%)
- **WRS**:
    - **2021**: 66,495,174,311
    - **2022**: 66,495,590,128
    - **2023**: 73,858,986,744 (14.4%)
- **FRS**:
    - **2021**: 17,834,808,438
    - **2022**: 3,468,559,504
    - **2023**: 3,073,227,623 (241.6%)

Despite the overall threats blocked peaking in 2023, there is a fluctuating and downward trend in threats blocked under our Email Reputation Service (ERS) and Web Reputation Service (WRS), indicating that threats in these areas are being better managed or are less frequent. However, there is a continuous increase in threats blocked under our File Reputation Service (FRS).

This could be indicative of the changing threat landscape where it can be assumed that threat actors are now opting for quality over quantity: Instead of launching attacks on a wider range of users and relying on victims clicking on malicious links in websites and emails, more sophisticated attacks are launched using specificity to trick a narrower field of high-profile victims. This also allows them to bypass early detection layers like network and email filters. It could be speculated that this contributed to the continuous increase in malicious file detections that are detected at endpoints.

- **MARS**:
    - **2021**: 54,195,862,697
    - **2022**: 48,473,430,401
    - **2023**: 36,547,933
- **SHN**:
    - **2021**: 94,289,585,240
    - **2022**: 5,921,414
    - **2023**: 2,966,079,048
- **IoTRS**:
    - **2021**: 66,495,590,128
    - **2022**: 3,073,227,623
    - **2023**: 3,465,314

There is also a continuous decrease in threats blocked under our Mobile Application Reputation Service (MARS), Smart Home Network (SHN), and Internet of Things Reputation Service (IoTRS), suggesting that cybercriminals are choosing their targets carefully rather than randomly. It remains crucial to protect all layers of the attack surface, and SOCs should realize that understanding the attackers’ targeting strategies is important for effective defense.

### Android Malware Families
- XLoaderPacker: 3,030,515
- KeepSpy: 2,475,757
- Xloader: 920,098
- MMRat: 645,888
- CovidRansom: 247,555

- **XLoaderPacker**: is a spyware that can be manually installed by a user. It poses as an Android app using different app names, and, once installed can monitor incoming and outgoing calls, and lock the screen of the affected system.
- **KeepSpy**: is sideloaded through a TianySpy malware delivered via smishing messages. It also poses as an Android app using different app names, and, once installed, can collect banking credentials and Wi-Fi settings.

### Vulnerabilities
**Total Vulnerabilities (Number of published Zero-Day Initiative (ZDI) vulnerability advisories)**
- **2022**: 1,706
- **2023**: 1,913

### Zero-Day Exploits (ZDI) Advisories
The first quarter of 2023 starts with relatively low zero-day advisories, with a significant increase by the end of the quarter in March. The second quarter fluctuates and peaks in May, while the third quarter stabilizes at a relatively high level of