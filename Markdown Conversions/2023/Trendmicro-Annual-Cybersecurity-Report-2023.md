# CALIBRATING EXPANSION 2023 ANNUAL CYBERSECURITY REPORT

## Table of Contents
- [APT CAMPAIGNS](#apt-campaigns)
- [RANSOMWARE THREATS](#ransomware-threats)
- [CLOUD AND ENTERPRISE THREATS](#cloud-and-enterprise-threats)
- [MITRE ATT&CK DETECTIONS](#mitre-attck-detections)
- [THREAT LANDSCAPE](#threat-landscape)

## APT CAMPAIGNS
![Image description: Timeline of APT campaigns from April 2022 to December 2023, showing various threat actors and their activities.]

### APT28’s NTLMv2 hash relay attacks
April 2022 – August 2023
Targets:
- Organizations involved in a wide range of fields, but primarily in foreign affairs, energy, defense, and transportation
Possibly an attempt to brute-force its way into target networks
Exploited CVE-2023-23397 that was patched in March 2023, at which point APT28 used more elaborate methods that involved scripts hosted on Mockbin sent to targets

### APT28’s more recent credential phishing campaign
November – December 2023
Targets:
- Various government organizations in Europe
Shares similarities to the earlier hash relay campaign in technical indicators, such as sharing the same computer name used to send out spear-phishing emails and to craft LNK files.

### Earth Lusca
January – June 2023
Targets:
- Government departments involved in foreign affairs, technology, and telecommunications in countries in Southeast Asia, Central Asia, and the Balkans, with scattered attacks on Latin American and African countries
Targets the public-facing servers of its victims
The decrypted payload is a Linux-targeted backdoor, a new variant named SprySOCKS

### Earth Estries
January 2023 – present
Targets:
- Government organizations and technology industries in the Philippines, Taiwan, Malaysia, South Africa, Germany, and the USA.
They use multiple backdoors and hacking tools, as well as PowerShell downgrade attacks to avoid detection
They use public services such as Github, Gmail, AnonFiles, and File.io to enhance and transfer commands and stolen data
Earth Estries is known to deploy cyberespionage campaigns.

### Kimsuky’s continued activity
April 2022, and April – May 2023
Targets:
- Individuals working in fields related to the Democratic People’s Republic of Korea
- Possibly organizations related to military, diplomacy, and unifications, and Korean-language support groups, based on Kimsuky’s previous campaign history
Likely aimed to gather information on geopolitical events, diplomatic strategies, and activities impacting the target’s interests
Could also be launched to gather armament-related information and for cryptocurrency-related attacks
Delivered as an email file

### Gamaredon
January – November 2023
Targets:
- Government organizations in Ukraine
Gamaredon continues its activity with attacks using Remote Template Injection and self-extracting executable files
The timeline of increased activity of the investigated sample suggests the campaign was launched to intensify espionage activities

### Void Rabisu’s slimmed down ROMCOM variant
June – August 2023
Targets:
- Military personnel and political leaders in Europe
Exploited the then zero-day vulnerability CVE-2023-36884
Primarily known for cyberespionage activities targeting governments and military with financial motivations

### Turla attacks using Capibar and Kazuar
July 2023
Targets:
- Diplomatic and military organizations in Ukraine
Turla has been active since 2014, and is known for its cyberespionage activities.
In this phishing campaign, the Capibar malware was used for intelligence gathering, while the Kazuar malware was used for credential theft.

### APT34’s targeted phishing attack
August 2023
Targets:
- Possibly organizations inside the Kingdom of Saudi Arabia
The malicious document in the phishing scam dropped a new malware designed for espionage, capable of identifying the machine, reading and uploading files from the machine, and downloading another file or malware.
APT34 is known for its cyberespionage activities targeting government agencies, organizations involved in critical infrastructure, and telecommunications in the Middle East.

### Mustang Panda
August 2023 – present
Targets:
- Government organizations in the Philippines, and other related organizations
Possibly launched for information gathering purposes
Samples contain strings that suggest the possibility of attacking Myanmar government officials
Utilized components of legitimate software commonly used in Southeast Asia for DLL sideloading

### APT38
May – September 2023
Targets:
- Cryptocurrency-related organization, investment firms, and banks
Detected in a sample used by BlueNoroﬀ, which is associated with APT38. The sample was later reported by SentinelOne as used in the later stages of SwiftLoader and indicated in a connection between KandyKorn and SwiftLoader
Likely financially motivated and launched to acquire foreign currency to fund armaments and espionage

### Konni Group
November 2023
Targets:
- Companies within the Republic of Korea
According to our analysis, the campaign’s malicious zip file contains an LNK file, that when executed drops html and VBScript to fetch additional payloads, possibly pointing to APT37.
Possibly launched as additional means of acquiring foreign currency
Associated with OSMIUM, Opal Sleet, SectorA07, TA406, and Kimsuky

### APT29’s VovaMirage spear phishing campaign
November 2023
Targets:
- Embassies and diplomatic entities in European countries, particularly Azerbaijan, Greece, Romania, and Italy
Exploited WinRAR vulnerability CVE-2023-38831 in a spear phishing campaign
Likely launched to gather information on strategic activities involving the respective country targets

## RANSOMWARE THREATS
### What to Watch Out For
The following tactics were observed in 2023 and could possibly be seen in the coming year as ransomware activities grow more sophisticated.
- There is a continued increase in the use of remote encryption
    - Observed in Akira, BlackCat, BlackMatter, LockBit, and Royal
    - Attackers actively map drives to encrypt on the affected endpoint instead of doing lateral movement. This could be a leap in tactics to reduce their footprint in attacks to avoid detection.
- Ransomware groups are also maximizing the convenience of intermittent encryption
    - Observed in NoEscape, Ransomware Play, BlackBasta, Agenda, and BlackCat
    - Attackers encrypt chunks of data instead of encrypting all data in one go; this process speeds up encryption while still rendering the affected data useless to the victim, and also makes for a more complicated decryption process.
- Endpoint Detection and Response (EDR) bypass using unmonitored virtual machines (VM)
    - Observed in Akira and BlackCat
    - Attackers bypass EDR by creating unmonitored VMs to navigate, map and encrypt files within the Windows Hyper-V hypervisor systems and attached VMs.
- Multi-ransomware attacks
    - The initial attacker sells its access to other ransomware groups to launch multiple attacks with a combination of malware, data theft, and wiper tools to maximize manipulation and pressure against the victims.

### Total Ransomware Detections
There has been a general downward trend in ransomware detections, with detections from 2021 to 2023 averaging less than half of the recorded detections in 2020; however, this should not be misconstrued as a cue for security operations centers and decision-makers to lower their guards. Historically, ransomware attacks were launched in “bulk,” such as spam campaigns with malicious links, but attacks that focus on quantity can more easily be blocked, as shown in our ransomware ERS and WRS data in the following figure. These figures show a general downward trend consistent with the total ransomware detections.
However, a continued increase in FRS detections could suggest that attackers are using more effective ways to evade preliminary detection by focusing on arrival and defense evasion techniques such as Living-Off-The-Land Binaries and Scripts (LOLBINs/LOLBAs), Bring Your Own Vulnerable Driver (BYOVD), zero-day exploits, and AV termination. We detect and identify ransomware payloads as malicious at endpoint as the ways they get into systems become more complex. This pattern is also observed in SPN data for overall threats blocked.
![Image description: Bar graph showing ERS detections for 2021, 2022, and 2023.]
![Image description: Bar graph showing WRS detections for 2021, 2022, and 2023.]
![Image description: Bar graph showing FRS detections for 2021, 2022, and 2023.]
![Image description: Bar graph showing total ransomware detections from 2019 to 2023.]

### Operating Systems Affected by Ransomware
![Image description: Bar graph showing ransomware detections for Linux, MacOS, and Windows in 2021, 2022, and 2023.]
Based on data from our midyear report, customer detections on Linux-targeted ransomware attacks from the first half of 2023 continues to overshadow MacOS attacks. This is consistent with data gathered from 2022, which was an exceptional year for Linux-based malware detections, making up 25% of our telemetry; previously, Linux-targeted attacks only made up two to three percent of the OS ratio. It should be noted that Windows continues to take the bulk of our ransomware detections, with the only significant decrease in 2022.
![Image description: Stacked bar graph showing percentage of ransomware detections by OS from 2019 to 2023.]
However, as our data for 2023 was completed, MacOS ransomware attacks came out higher with 9,961 detections, while Linux detections were finalized at 4,949. This could suggest that Linux-targeted attacks are stabilizing after the influx of novel Linux variants in 2022 to early 2023, but it could also be influenced by the overall decrease in ransomware activity.

### Top Countries and Regions by Detected Ransomware Attacks
![Image description: Bar graph showing ransomware detections by region (Europe, Americas, Asia).]
Thailand made up 68% of ransomware detections in Asia.
1. United States: 1,640,144
2. Thailand: 6,080,644
3. Turkey: 707,808
4. Taiwan: 454,008
5. India: 307,658

### Top Industries and Segments by Detected Ransomware Attacks
![Image description: Bar graph showing ransomware detections by industry and segment.]
Industry rankings and segment breakdowns based on unique detection counts at the endpoint shows that enterprises are the primary targets, with significant interest in the banking sector in 2023.
- Small and mid-sized businesses: 26,430
- Consumer: 21,271
- Enterprise: 166,069
- Banking: 20.3K
- Government: 9.9K
- Technology: 7.7K
- Retail: 6.3K
- Fast-Moving Consumer Goods: 5.6K

### Top Ransomware Families
![Image description: Bar graph showing top ransomware families for 2023.]
StopCrypt and LockBit maintain the top spots in terms of most prolific ransomware families for 2023 as it did in the previous year, but the former overtook the latter by a narrow margin this year. Note that this data does not include legacy ransomware families.
- Conti: 4,277
    - Requires being executed with specific arguments or parameters, additional components or in a specific environment to proceed with its routine
    - Reported to have heavily targeted India in 2023 alongside LockBit and BlackCat
- BlackCat: 4,206
- LockBit: 3,857
- StopCrypt: 2,470
![Image description: Bar graph showing top ransomware families for 2022.]
- Wannaren: 3,001
- BlackCat: 2,898
- StopCrypt: 2,781
    - Created and uses the malware StealBit for automated data exfiltration
- LockBit: 2,511
    - Launched a bug bounty program in 2022
    - LockBit 3.0 has code that shares similarities to DarkSide and BlackMatter
    - Maximizes affiliates who buy access to targets from other threat actors

## CLOUD AND ENTERPRISE THREATS
### Risk Events
![Image description: Bar graph showing top industries by risk events (ASRM).]
- Others: 10,826,646,225
- Insurance: 6,689,288,803
- Transportation: 6,857,317,526
- Education: 8,954,860,990
- Government: 12,077,150,154
- Public Services: 13,408,802,186
- Financial Services: 17,307,436,283
- Retail: 17,793,629,116
- Technology: 18,436,575,856
- Healthcare: 21,386,430,411
- Manufacturing: 10,826,646,225

### Home Network Security Top Events
![Image description: Bar graph showing top home network security events.]
With hybrid work now established as part of business operations, we looked at our Home Network Security telemetry to see what specific events cybercriminals particularly favor to use and what devices they target to maximize the larger attack surface created by remote and home workspaces.
- Brute-Force Login: 1,234,502,439
    - Might be RDP via port 3389, FTP via port 21, or SSH via port 22 to repeatedly attempt to log in to target hosts using a dictionary of common usernames and passwords
- TELNET Default Password Login -6: 322,792,561
    - Detects when a user within the network uses the default password to log in
- MISC Bitcoin/Litecoin/Dogecoin Mining Activity -1: 265,722,686
    - Related to information disclosure and possibly to Bitcoin/Litecoin/Dogecoin Mining Activity
- WEB HTTP Invalid Content-Length -2: 248,331,853
    - Caused by an error in processing HTTP packets containing negative Content-Length header field values that result in a heap buffer overflow
- MISC Cryptocurrency Monero Mining Activity -1: 125,553,894
    - Possible Monero (XMR) cryptocurrency mining activity

### Home Network Security Top Affected Device Types
![Image description: Bar graph showing top affected device types in home networks.]
Desktops and laptops recorded the most inbound attack detections based on our Home Network Security telemetry data.
- Desktop/Laptop: 862.8M
- Smartphone: 198.7M
- Tablet: 105.7M
- Game Console: 19.5M
- NAS: 18.4M

### Average Vulnerability by Vendor
![Image description: Bar graph showing average vulnerability by vendor.]
- Delta Electronics: 369
- PDF-XChange: 223
- D-Link: 176
- Microsoft: 101
- Adobe: 97

## MITRE ATT&CK DETECTIONS
### Top 5 Tactics Detected (Overall)
![Image description: Bar graph showing top 5 tactics detected overall.]
Dodging security tools, communication and control of compromised systems, and gaining a foothold within victim’s systems and networks are the most used TTPs (overall, endpoints, network, and email)
- Impact (TA0040): 33,836
- Persistence (TA0003): 23,642
- Initial Access (TA0001): 21,321
- Command and Control (TA0011): 20,465
- Defense Evasion (TA0005): 18,335

### Top Tactics, Techniques, and Procedures (TTPs) Endpoint
![Image description: Bar graph showing top TTPs for endpoints.]
- Execution (TA0002): 33,461
- Command and Control (TA0011): 15,990
- Initial Access (TA0001): 14,508
- Impact (TA0040): 14,221
- Defense Evasion (TA0005): 13,871

### Top TTPs Network
![Image description: Bar graph showing top TTPs for networks.]
- Impact (TA0040): 5,957
- Execution (TA0002): 4,642
- Initial Access (TA0001): 3,839
- Lateral Movement (TA0008): 3,356
- Command and Control (TA0011): 1,705

### TTPs Overall Trend by Detections
![Image description: Bar graphs showing TTP trends by month.]
Command and Control showed a gradual increase from September to December, while Defense Evasion peaked in March and July before declining in customer detections in subsequent months. Execution entered the top three TTPs detected in July and August, while Impact showed no clear trend despite a spike in November. Persistence only entered the top three in the first quarter of the year but was in a downward trend before dipping below the top three. Despite fluctuations, Initial Access maintains a moderate number of detections, since it is the primary goal of threat actors to gain a foothold in target victim systems and networks.
Note that the monthly detections do not show data for May and June due to a system error experienced during that period.

### Living-Off-The-Land Tactics
![Image description: Bar graphs showing detections for various Living-Off-The-Land tactics.]
There is no clear trend in the detections, though Mimikatz and Cobalt Strike continue to be the preferred legitimate tools to abuse to aid criminal activity. It can be assumed that threat actors prefer to use well-known tools instead of exploring novel ones, a logical behavior that is commonly observed as it guarantees more likelihood of success with less effort.
- Mimikatz:
    - 1H 2023: 8,956
    - 2H 2023: 7,513
    - Preferred for its effectiveness in harvesting data while evading detection
- Cobalt Strike:
    - 1H 2023: 3,747
    - 2H 2023: 3,914
    - Favored for Command and Control as this tactic requires stealth and resilience to remain undetected within compromised networks for an extended period
- Brute Ratel:
    - 1H 2023: 244
    - 2H 2023: 381
- GMER:
    - 1H 2023: 30
    - 2H 2023: 0
- Subcategory: Trojan, Fileless, Backdoor, Collection, Command and Control, Defense Evasion

## THREAT LANDSCAPE
### Malware Detection
#### Countries With the Most Malware Detections
![Image description: Table showing countries with most malware detections and top industries targeted.]
and the corresponding top industries targeted for each
1. Japan: 1,169,219,233
    - Manufacturing: 4,206
    - Education: 3,813
    - Healthcare: 3,809
2. United States: 993,996,354
    - Healthcare: 45,030
    - Technology: 36,021
    - Manufacturing: 9,410
3. India: 288,557,845
    - Manufacturing: 34,110
    - Government: 31,273
    - Banking: 30,253
4. Italy: 277,616,731
    - Healthcare: 15,086
    - Banking: 12,332
    - Government: 9,490
5. Brazil: 256,383,037
    - Government: 43,300
    - Education: 17,623
    - Financial: 8,051
Note that industry data counts are limited to customers who have elected to provide details pertaining to the business sectors in which they belong. Total malware detection counts include customers who did not provide any information on their industries.

#### Top Countries Accessing Malicious URLs
![Image description: List of top countries accessing malicious URLs.]
1. Japan: 823,057,759
2. United States: 382,881,197
3. Taiwan: 95,100,913
4. China: 84,300,801
5. Philippines: 76,730,598

#### Top Industries Affected by Malware Campaigns
![Image description: Bar graph showing top industries affected by malware campaigns.]
From the aggregate average of our Smart Protection Network (SPN) data, malware campaigns targeted government organizations the most with 302,555 detections.
- Government: 302.6K
- Healthcare: 228.1K
- Manufacturing: 212.1K
- Education: 179.8K
- Banking: 176.4K

#### Top Malware Families
![Image description: Bar graph showing top malware families for 2023 and 2022.]
A cryptocurrency mining malware surpassed prolific names in 2023.
Personal data remains the most valuable commodity in underground criminal communities; cryptocurrency wallets and crypto-related data are the most actionable data that can be stolen by malicious actors, equivalent to cash that can immediately be spent without traceability.
Cryptocurrency mining malware CoinMiner takes the lead over notorious Webshell
- Last reported exploit: Oracle WebLogic Server vulnerabilities (CVE-2020-14882)
- Reported to have been deployed by malicious Python Package Index packages targeting Linux
- Uses the victim system’s central processing unit (CPU) and/or graphical processing unit (GPU) resources to mine cryptocurrency
- The following can be observed during the infection:
    - High CPU utilization either with powershell.exe or schtasks.exe
    - Monero.Cryptocurrency.Miner app detection from the network
    - Execution source can be identified during service installation
    - WMI powershell scripts on the DC server
Despite being overtaken, Webshell remains a go-to for threat actors
- Exploits vulnerabilities in internet-facing web servers
- 2023:
    - CoinMiner: 303,399
    - Webshell: 249,949
    - Powload: 192,658
    - Nemucod: 125,204
    - Negasteal: 124,443
- 2022:
    - Downad: 74,933
    - Bondat: 59,788
    - Powload: 45,658
    - Webshell: 44,617
    - Emotet: 43,013

### Email Threats
#### Top Countries by Detection
![Image description: List of top countries by email threat detection.]
1. United States: 10,425,179,000
2. China: 2,079,512,425
3. Netherlands: 1,222,110,043
4. Russia: 1,214,975,535
5. Germany: 1,101,398,365

#### High-Risk Email Threats
![Image description: Bar graph comparing high-risk email threats between 2022 and 2023.]
While there is a decrease in malicious and phishing URL detections from 2022 to 2023, the increase in malware detection count and BEC count suggests the change in the threat landscape that finds attackers making use of more sophisticated ways to avoid detection. In this case, instead of focusing on malicious and phishing URLs to randomly victimize users, BEC schemes suggest more targeted operations, while a closer look at our malware detection count includes phishing links embedded within the attachments. This is consistent with patterns observed in our SPN data on threats blocked from 2021 to 2023, where detections that rely on attribution of URLs (WRS) and emails (ERS) show a decrease, while endpoint detections that directly identify malicious files have consistently increased.
- Total business email compromise count:
    - 2022: 19,149,460
    - 2023: 35,256,360
- Total malicious and phishing URLs count:
    - 2022: 4,263,650
    - 2023: 446,234
- Total malware detection count:
    - 2022: 25,665,848
    - 2023: 383,926

#### Top 5 Spam Attachments
![Image description: Bar graph showing top 5 spam attachments.]
- DOC: 10,262,737
- HTML: 2,007,619
- DOCX: 1,884,077
- EXE: 700,566
- PDF: 448,155

#### Spam Attachments per month of 2023
![Image description: Bar graph showing spam attachments per month of 2023.]
There is a general increasing trend for the first half of the year, where malicious spam attachment detections peaked in June. This is followed by fluctuations in the second half of the year, that eventually decline until December. Despite more cunning ways to lure victims into clicking malicious links, spam campaigns remain a go-to for cybercriminals.
- January: 2,667,467
- February: 918,126
- March: 1,297,818
- April: 1,080,318
- May: 998,806
- June: 1,062,592
- July: 2,121,029
- August: 3,972,265
- September: 1,124,230
- October: 453,181
- November: 481,862
- December: 295,801

### Threats Blocked
![Image description: Bar graph showing overall threats blocked from 2016 to 2023.]
The total number of threats blocked based on our SPN reached a record high in 2023, 10% higher from the previous year. It also continues the dramatic climb of threats blocked that began to be recorded in 2021, the first year that surpassed the previous peak of 82 billion in 2016. This coincided with the pandemic, strongly suggesting its role in driving the upswing.
- 2016: 66,495,590,128
- 2017: 94,289,585,240
- 2018: 48,473,430,401
- 2019: 54,195,862,697
- 2020: 66,495,174,311
- 2021: 81,885,110,904
- 2022: 146,408,535,569
- 2023: 161,014,076,615
![Image description: Bar graph showing threats blocked by ERS, WRS, and FRS from 2021 to 2023.]
Despite the overall threats blocked peaking in 2023, there is a fluctuating and downward trend in threats blocked under our Email Reputation Service (ERS) and Web Reputation Service (WRS), indicating that threats in these areas are being better managed or are less frequent. However, there is a continuous increase in threats blocked under our File Reputation Service (FRS).
- ERS:
    - 2021: 69,869,979,425
    - 2022: 73,858,986,744
    - 2023: 79,945,411,146
- WRS:
    - 2021: 3,468,559,504
    - 2022: 2,356,888,444
    - 2023: 2,531,040,185
- FRS:
    - 2021: 17,834,808,438
    - 2022: 82,149,430,110
    - 2023: 60,925,991,943
![Image description: Bar graph showing threats blocked by MARS, SHN, and IoTRS from 2021 to 2023.]
This could be indicative of the changing threat landscape where it can be assumed that threat actors are now opting for quality over quantity: Instead of launching attacks on a wider range of users and relying on victims clicking on malicious links in websites and emails, more sophisticated attacks are launched using specificity to trick a narrower field of high-profile victims. This also allows them to bypass early detection layers like network and email filters. It could be speculated that this contributed to the continuous increase in malicious file detections that are detected at endpoints.
There is also a continuous decrease in threats blocked under our Mobile Application Reputation Service (MARS), Smart Home Network (SHN), and Internet of Things Reputation Service (IoTRS), suggesting that cybercriminals are choosing their targets carefully rather than randomly. It remains crucial to protect all layers of the attack surface, and SOCs should realize that understanding the attackers’ targeting strategies is important for effective defense.
- MARS:
    - 2021: 1,257,448
    - 2022: 3,465,314
    - 2023: 36,547,933
- SHN:
    - 2021: 2,611,751,397
    - 2022: 2,966,079,048
    - 2023: 3,073,227,623
- IoTRS:
    - 2021: 35,762,472
    - 2022: 36,547,933
    - 2023: 37,088,836

### Android Malware Families
![Image description: Bar graph showing detections for various Android malware families.]
- XLoaderPacker is a spyware that can be manually installed by a user. It poses as an Android app using different app names, and, once installed can monitor incoming and outgoing calls, and lock the screen of the affected system.
- KeepSpy is sideloaded through a TianySpy malware delivered via smishing messages. It also poses as an Android app using different app names, and, once installed, can collect banking credentials and Wi-Fi settings.
- CovidRansom: 3,030,515
- MMRat: 2,475,757
- Xloader: 920,098
- KeepSpy: 645,888
- XLoaderPacker: 247,555

### Vulnerabilities
#### Total Vulnerabilities
(Number of published Zero-Day Initiative (ZDI) vulnerability advisories)
- 2022: 1,706
- 2023: 1,913

#### Zero-Day Exploits (ZDI) Advisories
![Image description: Bar graph showing zero-day exploit advisories per month.]
The first quarter of 2023 starts with relatively low zero-day advisories, with a significant increase by the end of the quarter in March. The second quarter fluctuates and peaks in May, while the third quarter stabilizes at a relatively high level of activity. The last quarter dips to the year’s lowest number of zero-day advisories in October, picks back up again in November, but shows a slight downturn in the last month indicating a possible decrease in threat actor activity as the year ended.
- January: 293
- February: 157
- March: 179
- April: 83
- May: 200
- June: 283
- July: 117
- August: 114
- September: 109
- October: 176
- November: 109
- December: 93

#### ZDI Industrial Control System and Zero-Day Vulnerabilities
![Image description: Bar graph showing ICS zero-day vulnerabilities per month.]
- 2023:
    - January: 8
    - February: 32
    - March: 15
    - April: 1
    - May: 36
    - June: 5
    - July: 43
    - August: 47
    - September: 4
    - October: 35
    - November: 26
    - December: 9
- ICS:
    - January: 29
    - February: 0
    - March: 0
    - April: 0
    - May: 15
    - June: 0
    - July: 0
    - August: 12
    - September: 0
    - October: 0
    - November: 0
    - December: 0

#### Non-ICS and N-Day Vulnerabilities
![Image description: Bar graph showing non-ICS and N-Day vulnerabilities per month.]
- January: 223
- February: 106
- March: 143
- April: 42
- May: 181
- June: 193
- July: 111
- August: 47
- September: 105
- October: 141
- November: 83
- December: 84

#### Riskiest CVEs by customer count
![Image description: Bar graph showing riskiest CVEs by customer count.]
- CVE-2023-23376: 57,808
- CVE-2023-21823: 59,798
- CVE-2023-24880: 57,797
![Image description: Bar graph showing 3 riskiest unpatched CVEs.]
- CVE-2023-24880: 58,173
- CVE-2023-21823: 60,731
- CVE-2023-23376: 58,184
