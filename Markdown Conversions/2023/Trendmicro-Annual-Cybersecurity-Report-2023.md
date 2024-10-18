CALIBRATING 
EXPANSION
2 0 2 3A NNUA LC YBERSECURIT YR EPORT
APT
CAMPAIGNS
03
RANSOMWARE
THREATS
07
MITRE ATT\&CK
DETECTIONS
16
THREAT
LANDSCAPE
20
13 ENTERPRISE
THREATS
CLOUD AND
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 3
APT
CAMPAIGNS
APR
2022
MAY
JUN
JUL
AUG
SEP
OCT
NOV
DEC
JAN
2023
FEB
MAR
APR
MAY
JUN
JUL
AUG
SEP
OCT
NOV
DEC
APT28s NTLMv2
hash relay attacks
APT28s more recent 
credential phishing campaign
Gamaredon
Earth Lusca
Earth Estries
Kimsukys continued activity
Void Rabisus slimmed down 
ROMCOM variant
Turla attacks using
Capibar and Kazuar
APT34s targeted
phishing attack
Mustang Panda
APT38
Konni Group
APT29s VovaMirage
spear phishing campaig
APT28s NTLMv2
hash relay attacks
April 2022 August 2023
Targets:
Organizations involved in a wide 
range of elds, but primarily in
foreign aairs, energy, defense,
and transportation 
Possibly an attempt to brute\-force its 
way into target networks
Exploited CVE\-2023\-23397 that was 
patched in March 2023, at which point 
APT28 used more elaborate methods 
that involved scripts hosted on 
Mockbin sent to targets
APT28s more recent 
credential phishing campaign
November December 2023
Targets:
Various government organizations
in Europe
Shares similarities to the earlier hash 
relay campaign in technical indicators, 
such as sharing the same computer 
name used to send out spear\-phishing 
emails and to craft LNK les.
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 4
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 4
Earth Lusca
January June 2023
Targets:
Government departments involved
in foreign aairs, technology, and
telecommunications in countries in
Southeast Asia, Central Asia, and
the Balkans, with scattered attacks 
on Latin American and African
countries
Targets the public\-facing servers of its 
victims
The decrypted payload is a 
Linux\-targeted backdoor, a new variant 
named SprySOCKS
Earth Estries 
January 2023 present
Targets:
Government organizations and
technology industries in the
Philippines, Taiwan, Malaysia,
South Africa, Germany, and the
USA.
They use multiple backdoors and 
hacking tools, as well as PowerShell 
downgrade attacks to avoid detection
They use public services such as 
Github, Gmail, AnonFiles, and File.io to 
exhance and transfer commands and 
stolen data
Earth Estries is known to deploy 
cyberespionage campaigns.
Kimsukys continued activity
April 2022, and April May 2023
Targets:
Individuals working in elds related
to the Democratic Peoples
Republic of Korea
Possibly organizations related to
military, diplomacy, and
unications, and Korean\-language
support groups, based on
Kimsukys previous campaign
history
Likely aimed to gather information on 
geopolitical events, diplomatic 
strategies, and activities impacting the 
targets interests
Could also be launched to gather 
armament\-related information and for 
cryptocurrency\-related attacks
Delivered as an email le
Gamaredon
January November 2023
Targets:
Government organizations in
Ukraine
Gamaredon continues its activity with 
attacks using Remote Template 
Injection and self\-extracting executable 
les
The timeline of increased activity of the 
investigated sample suggests the 
campaign was launched to intensify 
espionage activities
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 5
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 5
Void Rabisus slimmed down 
ROMCOM variant 
June August 2023
Targets:
Military personnel and political
leaders in Europe
Exploited the then zero\-day 
vulnerability CVE\-2023\-36884
Primarily known for cyberespionage 
activities targeting governments and 
military with nancial motivations
Turla attacks using
Capibar and Kazuar
July 2023
Targets:
Diplomatic and military
organizations in Ukraine
Turla has been active since 2014, and is 
known for its cyberespionage activities.
In this phishing campaign, the Capibar 
malware was used for intelligence 
gathering, while the Kazuar malware 
was used for credential theft.
APT34s targeted
phishing attack
August 2023
Targets:
Possibly organizations inside the
Kingdom of Saudi Arabia
The malicious document in the 
phishing scam dropped a new malware 
designed for espionage, capable of 
identifyiung the machine, reading and 
uploading les from the machine, and 
downloading another le or malware.
APT34 is known for its cyberespionage 
activities targeting government 
agencies, organizations involved in 
critical infrastructure, and 
telecommunications in the Middle East.
Mustang Panda
August 2023 present
Targets:
Government organizations in the Philippines, and other related
organizations
Possibly launched for information 
gathering purposes
Samples contain strings that suggest 
the possibility of attacking Myanmar 
government ocials
Utilized components of legitimate 
software commonly used in Southeast 
Asia for DLL sideloading
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 6
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 6
APT38
May September 2023
Targets:
Cryptocurrency\-related organization, investment rms, and banks
Detected in a sample used by 
BlueNoro, which is associated with 
APT38\. The sample was later reported 
by SentinelOne as used in the later 
stages of SwiftLoader and indicated in 
a connection between KandyKorn and 
SwiftLoader
Likely nancially motivated and 
launched to acquire foreign currency to 
fund armaments and espionage
Konni Group
November 2023 
Targets:
Companies within the Republic of Korea
According to our analysis, the 
campaigns malicious zip le contains 
an LNK le, that when executed drops 
html and VBScript to fetch additional 
payloads, possibly pointing to APT37\.
Possibly launched as additional means 
of acquiring foreign currency
Associated with OSMIUM, Opal Sleet, 
SectorA07, TA406, and Kimsuky
APT29s VovaMirage spear phishing campaign
November 2023
Targets:
Embassies and diplomatic entities in European countries, particularly Azerbaijan, Greece, Romania, and Italy
Exploited WinRAR vulnerability CVE\-2023\-38831 in a spear phishing campaign 
Likely launched to gather information on strategic activities involving the respective country 
targets
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 7
RANSOMWARE
THREATS
What to Watch Out For
The following tactics were observed in 2023 and could possibly be seen in the coming year as ransomware 
activities grow more sophisticated.
There is a continued increase in the use of remote encryption
Observed in Akira, BlackCat, BlackMatter, LockBit, and Royal
Attackers actively map drives to encrypt on the affected endpoint instead of doing lateral 
movement. This could be a leap in tactics to reduce their footprint in attacks to avoid detection.
Ransomware groups are also maximizing the convenience of intermittent encryption
Observed in NoEscape, Ransomware Play, BlackBasta, Agenda, and BlackCat
Attackers encrypt chunks of data instead of encrypting all data in one go; this process speeds 
up encryption while still rendering the affected data useless to the victim, and also makes for a 
more complicated decryption process. 
Endpoint Detection and Response (EDR) bypass using unmonitored virtual machines (VM)
Observed in Akira and BlackCat
Attackers bypass EDR by creating unmonitored VMs to navigate, map and encrypt files within the 
Windows Hyper\-V hypervisor systems and attached VMs.
Multi\-ransomware attacks
The initial attacker sells its access to other ransomware groups to launch multiple attacks with 
a combination of malware, data theft, and wiper tools to maximize manipulation and pressure 
against the victims.
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 8
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 8
Total Ransomware Detections
There has been a general downward trend in ransomware detections, with detections from 2021 to 2023 
averaging less than half of the recorded detections in 2020; however, this should not be misconstrued as a cue 
for security operations centers and decision\-makers to lower their guards. Historically, ransomware attacks were 
launched in bulk, such as spam campaigns with malicious links, but attacks that focus on quantity can more 
easily be blocked, as shown in our ransomware ERS and WRS data in the following figure. These figures show a 
general downward trend consistent with the total ransomware detections.
However, a continued increase in FRS detections could suggest that attackers are using more effective ways to 
evade preliminary detection by focusing on arrival and defense evasion techniques such as Living\-Off\-The\-Land 
Binaries and Scripts (LOLBINsLOLBAs), Bring Your Own Vulnerable Driver (BYOVD), zero\-day exploits, and AV 
termination. We detect and identify ransomware payloads as malicious at endpoint as the ways they get into 
systems become more complex. This pattern is also observed in SPN data for overall threats blocked.
2M
0
4M
6M
8M
2023
2022
2021
7,645,171
ERS
15\.0% 
3,633,193
6,647,565
52\.5% 
2M
1M
0
3M
4M
5M
2023
2022
2021
2,535,399
WRS
48\.4% 
1,782,349
4,917,624
29\.7% 
4M
2M
0
6M
8M
10M
2023
2022
2021
4,802,701
FRS
92\.0% 
8,754,324
2,501,589
82\.3% 
0
20M
40M
60M
80M
2022
2023
2021
2020
2019
61,132,338
41,271,208
14,066,778
14,983,271
14,169,866
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 9
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 9
Operating Systems Affected by Ransomware
0
20K
10K
30K
40K
2023
2022
2021
3,790
27,602
4,949
15,154
11,000
9,961
Linux
MacOS
Based on data from our midyear report, customer detections on Linux\-targeted ransomware attacks from the 
first half of 2023 continues to overshadow MacOS attacks. This is consistent with data gathered from 2022, which 
was an exceptional year for Linux\-based malware detections, making up 25% of our telemetry; previously, Linux\-
targeted attacks only made up two to three percent of the OS ratio. It should be noted that Windows continues to 
take the bulk of our ransomware detections, with the only significant decrease in 2022\.
Windows
MacOS
Linux
0%
20%
40%
60%
80%
100%
2023
2022
2021
2020
2019
97%
3%
0%
94%
5%
1%
92%
5%
3%
71%
4% 25%
92%
5%
3%
However, as our data for 2023 was completed, MacOS ransomware attacks came out higher with 9,961 
detections, while Linux detections were finalized at 4,949\. This could suggest that Linux\-targeted attacks are 
stabilizing after the influx of novel Linux variants in 2022 to early 2023, but it could also be influenced by the 
overall decrease in ransomware activity.
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 10
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 10
Top Countries and Regions by 
Detected Ransomware Attacks
Thailand made up 68% of ransomware detections in Asia.
1,640,144
United States
2
6,080,644
Thailand
1
307,658
India
5
707,808
Turkey
3
454,008 
Taiwan
4
0
6M
4M
2M
8M
10M
Europe
Americas
Asia
1,911,891
1,095,868
8,842,873
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 11
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 11
Top Industries and Segments by 
Detected Ransomware Attacks
20\.3K
Banking
9\.9K
Government
7\.7K
Technology
6\.3K
Retail
5\.6K
Fast\-Moving
Consumer Goods
0
100K
50K
150K
200K
Small and
mid\-sized
businesses
Consumer
Enterprise
26,430
21,271
166,069
Industry rankings and segment breakdowns based on unique detection counts at the endpoint shows that 
enterprises are the primary targets, with significant interest in the banking sector in 2023\.
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 12
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 12
0
1K
2K
3K
4K
5K
Conti 
BlackCat
LockBit 
StopCrypt 
4,277
4,206
3,857
2,470
 Requires being executed with specic
 arguments or parameters, additional
 componens or in a specic environment
 to proceed with its routine
 Reported to have heavily targeted India
 in 2023 alongside LockBit and BlackCat
2023
Top Ransomware Families
StopCrypt and LockBit maintain the top spots in terms of most prolific ransomware families for 2023 as it did in 
the previous year, but the former overtook the latter by a narrow margin this year. Note that this data does not 
include legacy ransomware families.
0
500
1\.5K
2\.5K
3\.5K
Wannaren
BlackCat
StopCrypt
LockBit
3,001
2,898
2,781
2,511
 Created and uses the malware StealBit
 for automated data exltration
 Launched a bug bounty program in 2022
 LockBit 3\.0 has code that shares
 similarities to DarkSide and BlackMatter
 Maximizes aliates who buy access to
 targets from other threat actors
2022
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 13
CLOUD AND
ENTERPRISE 
THREATS
Risk Events
Top Industries by Risk Events (ASRM)
21,386,430,411
18,436,575,856
17,793,629,116
17,307,436,283
13,408,802,186
12,077,150,154
8,954,860,990
6,857,317,526
6,689,288,803
10,826,646,225
0
5B
10B
15B
20B
25B
Others
Insurance
Transportation
Education
Government
Public Services
Financial Services
Retail
Technology
Healthcare
Manufacturing
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 14
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 14
Home Network Security Top Events
1,234,502,439
322,792,561
265,722,686
248,331,853
125,553,894
0
300M
600M
900M
1\.2B
1\.5B
Brute\-Force Login
Might be RDP via port 3389, FTP via port 21, or SSH via port 22 to repeatedly attempt to log in to 
target hosts using a dictionary of common usernames and passwords
TELNET Default Password Login \-6
Detects when a user within the network uses the default password to log in
MISC BitcoinLitecoinDogecoin Mining Activity \-1
Related to information disclosure and possibly to BitcoinLitecoinDogecoin Mining Activity
WEB HTTP InvalidContent\-Length \-2 
Caused by an error in processing HTTP packets containing negative Content\-Length header field 
values that result in a heap buffer overflow
MISC Cryptocurrency Monero Mining Activity \-1 
Possible Monero (XMR) cryptocurrency mining activity
With hybrid work now established as part of business operations, we looked at our Home Network Security 
telemetry to see what specific events cybercriminals particularly favor to use and what devices they target to 
maximize the larger attack surface created by remote and home workspaces.
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 15
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 15
Home Network Security Top Affected Device Types 
Desktops and laptops recorded the most inbound attack detections based on our Home Network Security 
telemetry data.
862\.8M
Desktop
Laptop
198\.7M
Smartphone
105\.7M
Tablet
19\.5M
Game Console
18\.4M
NAS
0
250K
500K
283,384
51,262
46,338
55,915
443,361
Devices
0
17\.5K
35K
NAS
Game Console
Tablet
Smartphone
DesktopLaptop
23,314
4,627
3,676
4,782
33,900
Average
Vulnerability by Vendor
0
100
200
300
400
Delta
Electronics
PDF\-XChange
D\-Link
Microsoft
Adobe
369
223
176
101
97
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 16
MITRE ATT\&CK
DETECTIONS
Top 5 Tactics Detected 
(Overall)
Dodging security tools, communication and control of compromised systems, and gaining a foothold within 
victims systems and networks are the most used TTPs (overall, endpoints, network, and email)
0
5K
15K
25K
35K
Impact
(TA0040\)
Persistence
(TA0003\)
Initial
Access
(TA0001\)
Command
and Control
(TA0011\)
Defense
Evasion
(TA0005\)
33,836
23,642
21,321
20,465
18,335
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 17
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 17
Top Tactics, Techniques, and Procedures (TTPs) Endpoint
Top TTPs Network
0
5K
15K
25K
35K
Execution
(TA0002\)
Command
and Control
(TA0011\)
Initial
Access
(TA0001\)
Impact
(TA0040\)
Defense
Evasion
(TA0005\)
33,461
15,990
14,508
14,221
13,871
0
2K
4K
6K
Impact
(TA0040\)
Execution
(TA0002\)
Initial
Access
(TA0001\)
Lateral
Movement
(TA0008\)
Command
and Control
(TA0011\)
5,957
4,642
3,839
3,356
1,705
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 18
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 18
0
2K
4K
6K
Impact
(TA0040\)
Defense
Evasion
(TA0005\)
Persistence
(TA0003\)
2,837
1,728
5,299
January
0
2K
4K
6K
Initial
Access
(TA0001\)
Impact
(TA0040\)
Persistence
(TA0003\)
1,636
1,587
5,275
February
0
2K
4K
8K
6K
Initial
Access
(TA0001\)
Impact
(TA0003\)
Defense
Evasion
(TA0005\)
3,573
1,947
6,015
March
0
2K
4K
6K
Initial
Access
(TA0001\)
Impact
(TA0040\)
Persistence
(TA0003\)
1,679
1,649
5,012
April
0
2K
4K
6K
Collection
(TA0009\)
Execution
(TA0002\)
Defense
Evasion
(TA0005\)
5,244
4,567
5,440
July
0
1K
2K
3K
Initial
Access
(TA0001\)
Execution
(TA0002\)
Defense
Evasion
(TA0005\)
2,457
2,112
2,620
August
0
1K
2K
3K
Impact
(TA0040\)
Initial
Access
(TA0001\)
Command
and Control
(TA0011\)
2,399
1,713
2,695
September
0
1K
2K
3K
Impact
(TA0040\)
Initial
Access
(TA0001\)
Command
and Control
(TA0011\)
2,532
1,714
2,980
October
0
1\.75K
3\.5K
Impact
(TA0040\)
Initial
Access
(TA0001\)
Command
and Control
(TA0011\)
2,638
2,386
3,305
November
0
1\.75K
3\.5K
Impact
(TA0040\)
Initial
Access
(TA0001\)
Command
and Control
(TA0011\)
2,579
1,739
3,804
December
TTPs Overall Trend by Detections
Command and Control showed a gradual increase from September to December, while Defense Evasion peaked 
in March and July before declining in customer detections in subsequent months. Execution entered the top 
three TTPs detected in July and August, while Impact showed no clear trend despite a spike in November. 
Persistence only entered the top three in the first quarter of the year but was in a downward trend before 
dipping below the top three. Despite fluctuations, Initial Access maintains a moderate number of detections, 
since it is the primary goal of threat actors to gain a foothold in target victim systems and networks. 
Note that the monthly detections do not show data for May and June due to a system error experienced during 
that period.
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 19
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 19
Living\-Off\-The\-Land Tactics
There is no clear trend in the detections, though Mimikatz and Cobalt Strike continue to be the preferred 
legitimate tools to abuse to aid criminal activity. It can be assumed that threat actors prefer to use well\-known 
tools instead of exploring novel ones, a logical behavior that is commonly observed as it guarantees more 
likelihood of success with less effort.
0
10K
20K
Mimikatz
8,956
7,513
Preferred for its eectiveness in harvesting
data while evading detection
0
4K
8K
Cobalt
Strike
3,747
3,914
Favored for Command and Control as this tactic
requires stealth and resilience to remain
undetected within compromised networks for an
extended period 
0
400
800
Brute
Ratel
244
381
0
15
30
GMER
30
0
1H 2023
2H 2023
Subcategory:
TTP:
Trojan
Fileless
Backdoor
Collection
Command
and Control
Defense Evasion
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 20
THREAT
LANDSCAPE
Malware Detection
Countries With the Most Malware Detections
and the corresponding top industries targeted for each
1,169,219,233
Japan
Manufacturing
Education
Healthcare
4,206 
3,813 
3,809
1
993,996,354
United States
Healthcare
Technology
Manufacturing
45,030 
36,021 
9,410
2
256,383,037
Brazil
Government
Education
Financial
 43,300
17,623
8,051
5
288,557,845
India
Manufacturing
Government
Banking
34,110 
31,273 
30,253
3
277,616,731
Italy
Healthcare
Banking
Government
15,086 
12,332 
9,490
4
Note that industry data counts are limited to customers who have elected to provide details pertaining to the 
business sectors in which they belong. Total malware detection counts include customers who did not provide 
any information on their industries.
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 21
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 21
Top Countries Accessing Malicious URLs
84,300,801
China
4
95,100,913
Taiwan
3
382,881,197
United States
2
823,057,759
Japan
1
76,730,598
Philippines
5
Top Industries Affected by Malware Campaigns
From the aggregate average of our Smart Protection Network (SPN) data, malware campaigns targeted 
government organizations the most with 302,555 detections.
302\.6K
Government
228\.1K
Healthcare
212\.1K
Manufacturing
179\.8K
Education
176\.4K
Banking
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 22
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 22
Top Malware Families
A cryptocurrency mining malware surpassed prolific names in 2023\.
Personal data remains the most valuable commodity in underground criminal communities; cryptocurrency 
wallets and crypto\-related data are the most actionable data that can be stolen by malicious actors, equivalent to 
cash that can immediately be spent without traceability.
Cryptocurrency mining malware CoinMiner takes the lead over notorious Webshell 
Last reported exploit: Oracle WebLogic Server vulnerabilities (CVE\-2020\-14882\)
Reported to have been deployed by malicious Python Package Index packages targeting Linux
Uses the victim systems central processing unit (CPU) andor graphical processing unit (GPU) resources to 
mine cryptocurrency
The following can be observed during the infection:
High CPU utilization either with powershell.exe or schtasks.exe
Monero.Cryptocurrency.Miner app detection from the network
Execution source can be identified during service installation
WMI powershell scripts on the DC server
Despite being overtaken, Webshell remains a go\-to for threat actors
Exploits vulnerabilities in internet\-facing web servers
0
50K
150K
250K
350K
Powload
Nemucod
Negasteal
Emotet
Webshell
0
20K
40K
60K
80K
Downad
Bondat
Powload
Webshell
CoinMiner
303,399
249,949
192,658
125,204
124,443
74,933
59,788
45,658
44,617
43,013
2022
2023
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 23
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 23
Email Threats
Top Countries by Detection
10,425,179,000 
United States
1
1,101,398,365
Germany
5
2,079,512,425
China
2
1,222,110,043
Netherlands
3
1,214,975,535
Russia
4
High\-Risk Email Threats
0
40M
80M
Total business email
compromise count
Total malicious and
phishing URLS count
Total malware
detection count
19,149,460
4,263,650
25,665,848
35,256,360
446,234
383,926
2022
2023
349% 
16% 
\-27% 
While there is a decrease in malicious and phishing URL detections from 2022 to 2023, the increase in malware 
detection count and BEC count suggests the change in the threat landscape that finds attackers making use of 
more sophisticated ways to avoid detection. In this case, instead of focusing on malicious and phishing URLs to 
randomly victimize users, BEC schemes suggest more targeted operations, while a closer look at our malware 
detection count includes phishing links embedded within the attachments. This is consistent with patterns 
observed in our SPN data on threats blocked from 2021 to 2023, where detections that rely on attribution of 
URLs (WRS) and emails (ERS) show a decrease, while endpoint detections that directly identify malicious files have 
consistently increased.
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 24
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 24
0
6M
4M
2M
8M
10M
12M
DOC
HTML
DOCX
EXE
PDF
10,262,737
2,007,619
1,884,077
700,566
448,155
Spam attachments per month of 2023
0
2M
1M
3M
4M
DEC
NOV
OCT
SEP
AUG
JUL
JUN 
MAY 
APR 
MAR 
FEB 
JAN 
295,801
481,862
453,181
1,124,230
3,972,265
2,121,029
1,062,592
998,806
1,080,318
1,297,818
918,126
2,667,467
Top 5 Spam Attachments
There is a general increasing trend for the first half of the year, where malicious spam attachment detections 
peaked in June. This is followed by fluctuations in the second half of the year, that eventually decline until 
December. Despite more cunning ways to lure victims into clicking malicious links, spam campaigns remain a go\-
to for cybercriminals.
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 25
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 25
146\.4B
Overall threats
blocked in 2022
161\.0B
Overall threats
blocked in 2023
The total number of threats blocked based on our SPN reached a record high in 2023, 10% higher from the 
previous year. It also continues the dramatic climb of threats blocked that began to be recorded in 2021, the first 
year that surpassed the previous peak of 82 billion in 2016\. This coincided with the pandemic, strongly suggesting 
its role in driving the upswing.
0
50B
100B
150B
200B
2023
2022
2021
2020
2019
2018
2017
2016
161,014,076,615
81,885,110,904
66,495,174,311
48,473,430,401
54,195,862,697
66,495,590,128
94,289,585,240
146,408,535,569
Despite the overall threats blocked peaking in 2023, there is a fluctuating and downward trend in threats blocked 
under our Email Reputation Service (ERS) and Web Reputation Service (WRS), indicating that threats in these 
areas are being better managed or are less frequent. However, there is a continuous increase in threats blocked 
under our File Reputation Service (FRS).
Threats Blocked
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 26
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 26
20B
0
40B
60B
80B
2023
2022
2021
79,945,411,146
ERS
14\.4% 
73,858,986,744
69,869,979,425
7\.6% 
500M
0
1\.5B
2\.5B
3\.5B
2023
2022
2021
2,531,040,185
WRS
27\.0% 
2,356,888,444
3,468,559,504
6\.9% 
40B
20B
0
60B
80B
100B
2023
2022
2021
60,925,991,943
FRS
241\.6% 
82,149,430,110
17,834,808,438
34\.8% 
This could be indicative of the changing threat landscape where it can be assumed that threat actors are now 
opting for quality over quantity: Instead of launching attacks on a wider range of users and relying on victims 
clicking on malicious links in websites and emails, more sophisticated attacks are launched using specificity to 
trick a narrower field of high\-profile victims. This also allows them to bypass early detection layers like network 
and email filters. It could be speculated that this contributed to the continuous increase in malicious file 
detections that are detected at endpoints.
0
1\.75B
3\.5B
2023
2022
2021
37,088,836
3,073,227,623
5,921,414
36,547,933
2,966,079,048
3,465,314
35,762,472
2,611,751,397
1,257,448
MARS
SHN
IoTRS
There is also a continuous decrease in threats blocked under our Mobile Application Reputation Service (MARS), 
Smart Home Network (SHN), and Internet of Things Reputation Service (IoTRS), suggesting that cybercriminals are 
choosing their targets carefully rather than randomly. It remains crucial to protect all layers of the attack surface, 
and SOCs should realize that understanding the attackers targeting strategies is important for effective defense.
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 27
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 27
Android Malware Families
XLoaderPacker is a spyware that can be manually installed by a user. It poses as an Android app using different 
app names, and, once installed can monitor incoming and outgoing calls, and lock the screen of the affected 
system.
KeepSpy is sideloaded through a TianySpy malware delivered via smishing messages. It also poses as an 
Android app using different app names, and, once installed, can collect banking credentials and Wi\-Fi settings.
Vulnerabilities
Total Vulnerabilities
(Number of published Zero\-Day Initiative (ZDI) vulnerability advisories)
1,706
2022
1,913
2023
0
500K
1\.5M
2\.5M
3\.5M
CovidRansom
MMRat
Xloader
KeepSpy
XLoaderPacker
3,030,515
2,475,757
920,098
645,888
247,555
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 28
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 28
Zero\-Day Exploits (ZDI) Advisories 
The first quarter of 2023 starts with relatively low zero\-day advisories, with a significant increase by the end of the 
quarter in March. The second quarter fluctuates and peaks in May, while the third quarter stabilizes at a relatively 
high level of activity. The last quarter dips to the years lowest number of zero\-day advisories in October, picks 
back up again in November, but shows a slight downturn in the last month indicating a possible decrease in 
threat actor activity as the year ended.
0
100
200
300
DEC
NOV
OCT
SEP
AUG
JUL
JUN 
MAY 
APR 
MAR 
FEB 
JAN 
93
109
176
109
114
117
283
200
83
179
157
293
ZDI Industrial Control System and Zero\-Day Vulnerabilities
0
10
20
30
40
50
DEC
NOV
OCT
SEP
AUG
JUL
JUN 
MAY 
APR 
MAR 
FEB 
JAN 
0
0
0
0
12
0
0
15
0
0
0
29
ICS
0
10
20
30
40
50
2023
9
26
35
4
47
43
5
36
1
15
32
8
ICS Zero\-Day Vulnerabilities
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 29
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 29
Non\-ICS and N\-Day Vulnerabilities
0
150
100
50
200
250
DEC
NOV
OCT
SEP
AUG
JUL
JUN 
MAY 
APR 
MAR 
FEB 
JAN 
84
83
141
105
47
111
193
181
42
143
106
223
Riskiest CVEs by 
customer count
0
20K
40K
60K
80K
CVE\-2023\-23376
CVE\-2023\-21823
CVE\-2023\-24880
57,808
59,798
57,797
0
20K
40K
60K
80K
58,184 
60,731
58,173
3 riskiest 
unpatched CVEs
CVE\-2023\-2488 (Windows SmartScreen Security Feature Bypass Vulnerability)
CVSS base score: 4\.4 medium
CVE\-2023\-21823 (Windows Graphics Component Remote Code Execution Vulnerability)
CVSS base score: 7\.8 high
CVE\-2023\-23376 (Windows Common File Log System Driver Elevation of Privilege Vulnerability)
CVSS base score: 7\.8 high
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 30
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 30
Risk Events
Top 2 Risk Events Detected 
The top two risk events detected via our attack surface risk management (ASRM) involve risky cloud applications 
and accessing risky websites.
82,976,277,500
Risky Cloud App Access
18,819,067,819
Risky Website Access Detected
SOCs are recommended diligence in monitoring cloud applications accessed by their networks, especially as 
more organizations are integrating cloud environments in their operations. 
Security teams should also conduct training to equip end\-users with the knowledge to identify and avoid 
accessing risky websites and links; human negligence remains the weakest link in cybersecurity.
Top Countries with Risk Events Detected
The United States of America recorded the most risk events at over 31\.2 billion detections, almost doubling the 
number of the country with the second most risk events, India at 16\.5 billion detections.
31,271,416,757
United States
1
16,570,427,847
India
2
7,816,148,246
Germany
5
15,060,300,143
Brazil
3
7,888,655,174
Great Britain
4
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 31
CALIBRATING EXPANSION
2023 ANNUAL CYBERSECURITY REPORT \| 31
Recommendations for Lowering Risk
Apply the latest patch or upgrade your operating system or application version.
Apply prevention rules from Trend Micro products to protect vulnerabilities from being exploited.
Optimize weak settings in current environment.
Avoid accessing the reported risky app or make the app a sanction one
Disable accounts with weak passwords or reset them with strong ones. Enable the Account Lockout 
Policy in your Active Directory.
Restrict user account usage on affected device and verify and resolve the at\-risk devices high\-risk 
events.
Trend Micro, a global cybersecurity leader, helps make the world safe for exchanging digital information. Fueled by decades of 
security expertise, global threat research, and continuous innovation, our unified cybersecurity platform protects over 500,000 
organizations and millions of individuals across clouds, networks, devices, and endpoints.
The Trend Vision One unified cybersecurity platform delivers advanced threat defense techniques, extended detection and 
response (XDR), and integration across the IT ecosystem, including AWS, Microsoft, and Google, enabling organizations to better 
understand, communicate, and mitigate cyber risk. 
Trend Micros global threat research team delivers unparalleled intelligence and insights that power our cybersecurity platform and 
help protect organizations around the world from 100s of millions of threats daily.
We have 7,000 employees across 65 countries, singularly focused on security and passionate about making the world a safer and 
better place.
Trend Micro enables organizations to simplify and secure their connected world.
TrendMicro.com
2024 by Trend Micro, Incorporated. All rights reserved. Trend Micro and the Trend Micro t\-ball logo are trademarks or registered 
trademarks of Trend Micro, Incorporated. All other company andor product names may be trademarks or registered trademarks of 
their owners.
CALIBRATING 
EXPANSION
2 0 2 3A NNUA LCY BERS EC URIT YR EPORT