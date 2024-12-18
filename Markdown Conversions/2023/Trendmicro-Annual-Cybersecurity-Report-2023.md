CALIBRATING 
EXPANSION

2 0 2 3 A N N U A L C Y B E R S E C U R I T Y R E P O R T

03

APT
CAMPAIGNS

07

RANSOMWARE
THREATS

CLOUD AND

13 ENTERPRISE

THREATS

16

MITRE ATT\&CK
DETECTIONS

20

THREAT
LANDSCAPE

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

FEB MAR APR MAY

JUN

JUL

AUG

SEP

OCT

NOV

DEC

APT28’s NTLMv2
hash relay attacks

APT28’s more recent 
credential phishing campaign

Gamaredon

Earth Lusca

Earth Estries

Kimsuky’s continued activity

Void Rabisu’s slimmed down 
ROMCOM variant

Turla attacks using
Capibar and Kazuar

APT34’s targeted
phishing attack

Mustang Panda

APT38

Konni Group

APT29’s VovaMirage
spear phishing campaig

APT28’s NTLMv2
hash relay attacks
April 2022 – August 2023

Targets:
 • Organizations involved in a wide 
 range of ﬁelds, but primarily in
 foreign aﬀairs, energy, defense,
 and transportation 

Possibly an attempt to brute\-force its 
way into target networks

Exploited CVE\-2023\-23397 that was 
patched in March 2023, at which point 
APT28 used more elaborate methods 
that involved scripts hosted on 
Mockbin sent to targets

APT28’s more recent 
credential phishing campaign
November – December 2023

Targets:
 • Various government organizations
 in Europe

Shares similarities to the earlier hash 
relay campaign in technical indicators, 
such as sharing the same computer 
name used to send out spear\-phishing 
emails and to craft LNK ﬁles.

3

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|APTCAMPAIGNSGamaredon
January – November 2023

Earth Lusca
January – June 2023

Targets:
 • Government organizations in
 Ukraine
Gamaredon continues its activity with 
attacks using Remote Template 
Injection and self\-extracting executable 
ﬁles

The timeline of increased activity of the 
investigated sample suggests the 
campaign was launched to intensify 
espionage activities

Earth Estries 
January 2023 – present

Targets:
 • Government organizations and
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

Targets:
 • Government departments involved
 in foreign aﬀairs, technology, and
 telecommunications in countries in
 Southeast Asia, Central Asia, and
 the Balkans, with scattered attacks 
 on Latin American and African
 countries

The decrypted payload is a 
Linux\-targeted backdoor, a new variant 
named SprySOCKS

Targets the public\-facing servers of its 
victims

Kimsuky’s continued activity
April 2022, and April – May 2023

Targets:
 • Individuals working in ﬁelds related
 to the Democratic People’s
 Republic of Korea
 • Possibly organizations related to
 military, diplomacy, and
 uniﬁcations, and Korean\-language
 support groups, based on
 Kimsuky’s previous campaign
 history

Delivered as an email ﬁle

Likely aimed to gather information on 
geopolitical events, diplomatic 
strategies, and activities impacting the 
target’s interests

Could also be launched to gather 
armament\-related information and for 
cryptocurrency\-related attacks

44

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Void Rabisu’s slimmed down 
ROMCOM variant 
June – August 2023

Turla attacks using
Capibar and Kazuar
July 2023

Targets:
 • Military personnel and political
 leaders in Europe

Exploited the then zero\-day 
vulnerability CVE\-2023\-36884

Primarily known for cyberespionage 
activities targeting governments and 
military with ﬁnancial motivations

Targets:
 • Diplomatic and military
 organizations in Ukraine

In this phishing campaign, the Capibar 
malware was used for intelligence 
gathering, while the Kazuar malware 
was used for credential theft.

Turla has been active since 2014, and is 
known for its cyberespionage activities.

APT34’s targeted
phishing attack
August 2023

Mustang Panda
August 2023 – present

Targets:
 • Possibly organizations inside the
 Kingdom of Saudi Arabia

The malicious document in the 
phishing scam dropped a new malware 
designed for espionage, capable of 
identifyiung the machine, reading and 
uploading ﬁles from the machine, and 
downloading another ﬁle or malware.

APT34 is known for its cyberespionage 
activities targeting government 
agencies, organizations involved in 
critical infrastructure, and 
telecommunications in the Middle East.

Targets:
 • Government organizations in the
 Philippines, and other related

 organizations

Utilized components of legitimate 
software commonly used in Southeast 
Asia for DLL sideloading

Possibly launched for information 
gathering purposes

Samples contain strings that suggest 
the possibility of attacking Myanmar 
government oﬃcials

55

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \| 
APT38
May – September 2023

Konni Group
November 2023 

Targets:
 • Cryptocurrency\-related

 organization, investment ﬁrms, and
 banks

Detected in a sample used by 
BlueNoroﬀ, which is associated with 
APT38\. The sample was later reported 
by SentinelOne as used in the later 
stages of SwiftLoader and indicated in 
a connection between KandyKorn and 
SwiftLoader

Likely ﬁnancially motivated and 
launched to acquire foreign currency to 
fund armaments and espionage

Targets:
 • Companies within the Republic of

 Korea

Associated with OSMIUM, Opal Sleet, 
SectorA07, TA406, and Kimsuky

According to our analysis, the 
campaign’s malicious zip ﬁle contains 
an LNK ﬁle, that when executed drops 
html and VBScript to fetch additional 
payloads, possibly pointing to APT37\.

Possibly launched as additional means 
of acquiring foreign currency

APT29’s VovaMirage spear phishing campaign
November 2023

Targets:
 • Embassies and diplomatic entities in European countries, particularly Azerbaijan,

 Greece, Romania, and Italy

Exploited WinRAR vulnerability CVE\-2023\-38831 in a spear phishing campaign 

Likely launched to gather information on strategic activities involving the respective country 
targets

66

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \| 
 
 
 
What to Watch Out For

The following tactics were observed in 2023 and could possibly be seen in the coming year as ransomware 

activities grow more sophisticated.

There is a continued increase in the use of remote encryption

• Observed in Akira, BlackCat, BlackMatter, LockBit, and Royal

• Attackers actively map drives to encrypt on the affected endpoint instead of doing lateral 

movement. This could be a leap in tactics to reduce their footprint in attacks to avoid detection.

Ransomware groups are also maximizing the convenience of intermittent encryption

• Observed in NoEscape, Ransomware Play, BlackBasta, Agenda, and BlackCat

• Attackers encrypt chunks of data instead of encrypting all data in one go; this process speeds 

up encryption while still rendering the affected data useless to the victim, and also makes for a 

more complicated decryption process. 

Endpoint Detection and Response (EDR) bypass using unmonitored virtual machines (VM)

• Observed in Akira and BlackCat

• Attackers bypass EDR by creating unmonitored VMs to navigate, map and encrypt files within the 

Windows Hyper\-V hypervisor systems and attached VMs.

Multi\-ransomware attacks

• The initial attacker sells its access to other ransomware groups to launch multiple attacks with 

a combination of malware, data theft, and wiper tools to maximize manipulation and pressure 

against the victims.

7

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|RANSOMWARETHREATSTotal Ransomware Detections

61,132,338

41,271,208

80M

60M

40M

20M

0

14,066,778

14,983,271

14,169,866

2019

2020

2021

2022

2023

There has been a general downward trend in ransomware detections, with detections from 2021 to 2023 

averaging less than half of the recorded detections in 2020; however, this should not be misconstrued as a cue 

for security operations centers and decision\-makers to lower their guards. Historically, ransomware attacks were 

launched in “bulk,” such as spam campaigns with malicious links, but attacks that focus on quantity can more 

easily be blocked, as shown in our ransomware ERS and WRS data in the following figure. These figures show a 

general downward trend consistent with the total ransomware detections.

However, a continued increase in FRS detections could suggest that attackers are using more effective ways to 

evade preliminary detection by focusing on arrival and defense evasion techniques such as Living\-Off\-The\-Land 

Binaries and Scripts (LOLBINs/LOLBAs), Bring Your Own Vulnerable Driver (BYOVD), zero\-day exploits, and AV 

termination. We detect and identify ransomware payloads as malicious at endpoint as the ways they get into 

systems become more complex. This pattern is also observed in SPN data for overall threats blocked.

7,645,171

4,917,624

6,647,565

8M

6M

4M

2M

0

5M

4M

3M

2M

1M

0

3,633,193

52\.5% 

15\.0% 

10M

8M

6M

4M

2M

0

2,535,399

1,782,349

48\.4% 

29\.7% 

2021

2022

ERS

2023

2021

2023

2021

2022

WRS

8,754,324

4,802,701

2,501,589

92\.0% 

82\.3% 

2023

2022

FRS

88

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Operating Systems Affected by Ransomware

40K

30K

20K

10K

0

11,000

27,602

15,154

3,790

9,961

4,949

2021

2022

2023

Linux

MacOS

Based on data from our midyear report, customer detections on Linux\-targeted ransomware attacks from the 

first half of 2023 continues to overshadow MacOS attacks. This is consistent with data gathered from 2022, which 

was an exceptional year for Linux\-based malware detections, making up 25% of our telemetry; previously, Linux\-

targeted attacks only made up two to three percent of the OS ratio. It should be noted that Windows continues to 

take the bulk of our ransomware detections, with the only significant decrease in 2022\.

2019

2020

2021

2022

2023

97%

94%

92%

71%

92%

3% 0%

5% 1%

5% 3%

4% 25%

5% 3%

0%

20%

40%

60%

80%

100%

Windows

MacOS

Linux

However, as our data for 2023 was completed, MacOS ransomware attacks came out higher with 9,961 

detections, while Linux detections were finalized at 4,949\. This could suggest that Linux\-targeted attacks are 

stabilizing after the influx of novel Linux variants in 2022 to early 2023, but it could also be influenced by the 

overall decrease in ransomware activity.

99

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Top Countries and Regions by 
Detected Ransomware Attacks

Thailand made up 68% of ransomware detections in Asia.

2

1,640,144
United States

3

707,808
Turkey

4

454,008 
Taiwan

5

307,658
India

6,080,644
Thailand

1

10M

8,842,873

8M

6M

4M

2M

0

1,911,891

1,095,868

Asia

Americas

Europe

1010

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Top Industries and Segments by 
Detected Ransomware Attacks

20\.3K

Banking

9\.9K

Government

7\.7K

Technology

166,069

200K

150K

100K

50K

0

26,430

21,271

6\.3K

Retail

5\.6K

Fast\-Moving
Consumer Goods

Enterprise

Consumer

Small and
mid\-sized
businesses

Industry rankings and segment breakdowns based on unique detection counts at the endpoint shows that 

enterprises are the primary targets, with significant interest in the banking sector in 2023\.

1111

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Top Ransomware Families

StopCrypt and LockBit maintain the top spots in terms of most prolific ransomware families for 2023 as it did in 

the previous year, but the former overtook the latter by a narrow margin this year. Note that this data does not 

include legacy ransomware families.

• Created and uses the malware StealBit

for automated data exﬁltration

• Launched a bug bounty program in 2022
• LockBit 3\.0 has code that shares
 similarities to DarkSide and BlackMatter
• Maximizes aﬃliates who buy access to

targets from other threat actors

3,001

2,898

2,781

2022

2,511

LockBit

StopCrypt

BlackCat

Wannaren

• Requires being executed with speciﬁc
 arguments or parameters, additional
 componens or in a speciﬁc environment

to proceed with its routine

• Reported to have heavily targeted India
in 2023 alongside LockBit and BlackCat

4,277

4,206

3,857

2023

2,470

StopCrypt 

LockBit 

BlackCat

Conti 

3\.5K

2\.5K

1\.5K

500

0

5K

4K

3K

2K

1K

0

1212

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \| 
 
 
 
Risk Events

Top Industries by Risk Events (ASRM)

Manufacturing

Healthcare

Technology

Retail

Financial Services

Government
Public Services

Education

Transportation

Insurance

Others

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

13

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CLOUD ANDENTERPRISE THREATSHome Network Security Top Events

With hybrid work now established as part of business operations, we looked at our Home Network Security 

telemetry to see what specific events cybercriminals particularly favor to use and what devices they target to 

maximize the larger attack surface created by remote and home workspaces.

1\.5B

1,234,502,439

1\.2B

900M

600M

300M

0

322,792,561

265,722,686

248,331,853

125,553,894

Brute\-Force Login

• Might be RDP via port 3389, FTP via port 21, or SSH via port 22 to repeatedly attempt to log in to 

target hosts using a dictionary of common usernames and passwords

TELNET Default Password Login \-6

• Detects when a user within the network uses the default password to log in

MISC Bitcoin/Litecoin/Dogecoin Mining Activity \-1

• Related to information disclosure and possibly to Bitcoin/Litecoin/Dogecoin Mining Activity

WEB HTTP Invalid Content\-Length \-2 

• Caused by an error in processing HTTP packets containing negative Content\-Length header field 

values that result in a heap buffer overflow

MISC Cryptocurrency Monero Mining Activity \-1 

• Possible Monero (XMR) cryptocurrency mining activity

1414

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Home Network Security Top Affected Device Types 

Desktops and laptops recorded the most inbound attack detections based on our Home Network Security 

telemetry data.

862\.8M

Desktop/
Laptop

Devices

283,384

443,361

198\.7M

Smartphone

105\.7M

Tablet

19\.5M

Game Console

18\.4M

NAS

Average

33,900

23,314

Desktop/Laptop

Smartphone

4,782

51,262

46,338

55,915

Tablet

Game Console

NAS

4,627

3,676

500K

250K

0

0

17\.5K

35K

Vulnerability by Vendor

369

223

176

101

97

400

300

200

100

0

Adobe

Microsoft

D\-Link

PDF\-XChange

Delta
Electronics

1515

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Top 5 Tactics Detected 
(Overall)

Dodging security tools, communication and control of compromised systems, and gaining a foothold within 

victim’s systems and networks are the most used TTPs (overall, endpoints, network, and email)

23,642

21,321

20,465

18,335

33,836

35K

25K

15K

5K

0

Defense
Evasion
(TA0005\)

Command
and Control
(TA0011\)

Initial
Access
(TA0001\)

Persistence
(TA0003\)

Impact
(TA0040\)

16

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|MITRE ATT\&CKDETECTIONSTop Tactics, Techniques, and Procedures (TTPs) Endpoint

33,461

35K

25K

15K

5K

0

15,990

14,508

14,221

13,871

Defense
Evasion
(TA0005\)

Impact
(TA0040\)

Initial
Access
(TA0001\)

Command
and Control
(TA0011\)

Execution
(TA0002\)

Top TTPs Network

5,957

6K

4,642

4K

2K

0

3,839

3,356

1,705

Command
and Control
(TA0011\)

Lateral
Movement
(TA0008\)

Initial
Access
(TA0001\)

Execution
(TA0002\)

Impact
(TA0040\)

1717

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|TTPs Overall Trend by Detections

Command and Control showed a gradual increase from September to December, while Defense Evasion peaked 

in March and July before declining in customer detections in subsequent months. Execution entered the top 

three TTPs detected in July and August, while Impact showed no clear trend despite a spike in November. 

Persistence only entered the top three in the first quarter of the year but was in a downward trend before 

dipping below the top three. Despite fluctuations, Initial Access maintains a moderate number of detections, 

since it is the primary goal of threat actors to gain a foothold in target victim systems and networks. 

Note that the monthly detections do not show data for May and June due to a system error experienced during 

that period.

January

February

March

5,299

6K

4K

2K

0

2,837

1,728

5,275

6K

4K

2K

0

1,636

1,587

6,015

8K

6K

4K

2K

0

3,573

1,947

Persistence
(TA0003\)

Defense
Evasion
(TA0005\)

Impact
(TA0040\)

Persistence
(TA0003\)

Impact
(TA0040\)

Initial
Access
(TA0001\)

Defense
Evasion
(TA0005\)

Impact
(TA0003\)

Initial
Access
(TA0001\)

April

July

August

September

5,440

5,244

4,567

5,012

6K

4K

2K

0

1,679

1,649

6K

4K

2K

0

2,620

2,457

2,112

3K

2K

1K

0

2,695

2,399

1,713

3K

2K

1K

0

Persistence
(TA0003\)

Impact
(TA0040\)

Initial
Access
(TA0001\)

Defense
Evasion
(TA0005\)

Execution
(TA0002\)

Collection
(TA0009\)

Defense
Evasion
(TA0005\)

Execution
(TA0002\)

Initial
Access
(TA0001\)

Command
and Control
(TA0011\)

Initial
Access
(TA0001\)

Impact
(TA0040\)

3K

2K

1K

0

2,980

October

2,532

November

December

3,305

3\.5K

3,804

3\.5K

1,714

1\.75K

0

2,638

2,386

1\.75K

0

2,579

1,739

Command
and Control
(TA0011\)

Initial
Access
(TA0001\)

Impact
(TA0040\)

Command
and Control
(TA0011\)

Initial
Access
(TA0001\)

Impact
(TA0040\)

Command
and Control
(TA0011\)

Initial
Access
(TA0001\)

Impact
(TA0040\)

1818

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Living\-Off\-The\-Land Tactics

Preferred for its eﬀectiveness in harvesting
data while evading detection

Favored for Command and Control as this tactic
requires stealth and resilience to remain
undetected within compromised networks for an
extended period 

8,956

7,513

Mimikatz

3,747

3,914

Cobalt
Strike

0

0

Brute
Ratel

10K

20K

0

4K

8K

244

381

30

GMER

400

800

0

15

0

30

1H 2023

2H 2023

Subcategory:

Trojan

Fileless

Backdoor

TTP:

Collection

Command
and Control

Defense Evasion

There is no clear trend in the detections, though Mimikatz and Cobalt Strike continue to be the preferred 

legitimate tools to abuse to aid criminal activity. It can be assumed that threat actors prefer to use well\-known 

tools instead of exploring novel ones, a logical behavior that is commonly observed as it guarantees more 

likelihood of success with less effort.

1919

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Malware Detection

Countries With the Most Malware Detections
and the corresponding top industries targeted for each

2

993,996,354
United States
Healthcare
Technology
Manufacturing

45,030 
36,021 
9,410

4

277,616,731
Italy
Healthcare
Banking
Government

15,086 
12,332 
9,490

1

1,169,219,233
Japan
Manufacturing
Education
Healthcare

4,206 
3,813 
3,809

5

256,383,037
Brazil
Government
Education
Financial

 43,300
17,623
8,051

3

288,557,845
India
Manufacturing
Government
Banking

34,110 
31,273 
30,253

Note that industry data counts are limited to customers who have elected to provide details pertaining to the 

business sectors in which they belong. Total malware detection counts include customers who did not provide 

any information on their industries.

20

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|THREATLANDSCAPETop Countries Accessing Malicious URLs

2

382,881,197
United States

4

84,300,801
China

823,057,759
Japan

1

3

95,100,913
Taiwan

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

2121

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|A cryptocurrency mining malware surpassed prolific names in 2023\.

Top Malware Families

Personal data remains the most valuable commodity in underground criminal communities; cryptocurrency 

wallets and crypto\-related data are the most actionable data that can be stolen by malicious actors, equivalent to 

cash that can immediately be spent without traceability.

303,399

249,949

350K

250K

150K

50K

0

2022

74,933

80K

2023

59,788

45,658

44,617

43,013

192,658

125,204

124,443

60K

40K

20K

0

Webshell

Emotet

Negasteal

Nemucod

Powload

CoinMiner

Webshell

Powload

Bondat

Downad

Cryptocurrency mining malware CoinMiner takes the lead over notorious Webshell 

• Last reported exploit: Oracle WebLogic Server vulnerabilities (CVE\-2020\-14882\)

• Reported to have been deployed by malicious Python Package Index packages targeting Linux

• Uses the victim system’s central processing unit (CPU) and/or graphical processing unit (GPU) resources to 

mine cryptocurrency

• The following can be observed during the infection:

• High CPU utilization either with powershell.exe or schtasks.exe

• Monero.Cryptocurrency.Miner app detection from the network

• Execution source can be identified during service installation

• WMI powershell scripts on the DC server

Despite being overtaken, Webshell remains a go\-to for threat actors

• Exploits vulnerabilities in internet\-facing web servers

2222

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Email Threats

Top Countries by Detection

1

10,425,179,000 
United States

3

1,222,110,043
Netherlands

4

1,214,975,535
Russia

1,101,398,365
Germany

5

2,079,512,425
China

2

High\-Risk Email Threats

Total malware
detection count

Total malicious and
phishing URLS count

Total business email
compromise count

4,263,650

19,149,460

35,256,360

25,665,848

383,926

446,234

349% 

\-27% 

16% 

0

40M

80M

2022

2023

While there is a decrease in malicious and phishing URL detections from 2022 to 2023, the increase in malware 

detection count and BEC count suggests the change in the threat landscape that finds attackers making use of 

more sophisticated ways to avoid detection. In this case, instead of focusing on malicious and phishing URLs to 

randomly victimize users, BEC schemes suggest more targeted operations, while a closer look at our malware 

detection count includes phishing links embedded within the attachments. This is consistent with patterns 

observed in our SPN data on threats blocked from 2021 to 2023, where detections that rely on attribution of 

URLs (WRS) and emails (ERS) show a decrease, while endpoint detections that directly identify malicious files have 

consistently increased.

2323

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Top 5 Spam Attachments

12M

10,262,737

10M

8M

6M

4M

2M

0

2,007,619

1,884,077

700,566 448,155

PDF

EXE

DOCX

HTML

DOC

Spam attachments per month of 2023

3,972,265

2,667,467

2,121,029

1,124,230

453,181

481,862

295,801

1,297,818

1,062,592

1,080,318

998,806

918,126

4M

3M

2M

1M

0

JAN 

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

There is a general increasing trend for the first half of the year, where malicious spam attachment detections 

peaked in June. This is followed by fluctuations in the second half of the year, that eventually decline until 

December. Despite more cunning ways to lure victims into clicking malicious links, spam campaigns remain a go\-

to for cybercriminals.

2424

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Threats Blocked

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

200B

150B

161,014,076,615

146,408,535,569

100B

81,885,110,904

66,495,174,311

94,289,585,240

66,495,590,128

54,195,862,697

48,473,430,401

50B

0

2016

2017

2018

2019

2020

2021

2022

2023

Despite the overall threats blocked peaking in 2023, there is a fluctuating and downward trend in threats blocked 

under our Email Reputation Service (ERS) and Web Reputation Service (WRS), indicating that threats in these 

areas are being better managed or are less frequent. However, there is a continuous increase in threats blocked 

under our File Reputation Service (FRS).

2525

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|79,945,411,146

3,468,559,504

80B

60B

40B

20B

0

69,869,979,425

73,858,986,744

3\.5B

2\.5B

1\.5B

7\.6% 

500M

0

14\.4% 

2023

2021

2022

ERS

2,531,040,185

2,356,888,444

27\.0% 

6\.9% 

100B

80B

60B

40B

20B

0

82,149,430,110

60,925,991,943

17,834,808,438

2021

2022

WRS

2023

2021

241\.6% 

34\.8% 

2023

2022

FRS

This could be indicative of the changing threat landscape where it can be assumed that threat actors are now 

opting for quality over quantity: Instead of launching attacks on a wider range of users and relying on victims 

clicking on malicious links in websites and emails, more sophisticated attacks are launched using specificity to 

trick a narrower field of high\-profile victims. This also allows them to bypass early detection layers like network 

and email filters. It could be speculated that this contributed to the continuous increase in malicious file 

detections that are detected at endpoints.

37,088,836

3,073,227,623

5,921,414

2021

2022

2023

36,547,933

2,966,079,048

3,465,314

35,762,472

2,611,751,397

1,257,448

0

1\.75B

3\.5B

MARS

SHN

IoTRS

There is also a continuous decrease in threats blocked under our Mobile Application Reputation Service (MARS), 

Smart Home Network (SHN), and Internet of Things Reputation Service (IoTRS), suggesting that cybercriminals are 

choosing their targets carefully rather than randomly. It remains crucial to protect all layers of the attack surface, 

and SOCs should realize that understanding the attackers’ targeting strategies is important for effective defense.

2626

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Android Malware Families

3,030,515

2,475,757

920,098

645,888

247,555

3\.5M

2\.5M

1\.5M

500K

0

XLoaderPacker

KeepSpy

Xloader

MMRat

CovidRansom

• XLoaderPacker is a spyware that can be manually installed by a user. It poses as an Android app using different 

app names, and, once installed can monitor incoming and outgoing calls, and lock the screen of the affected 

system.

• KeepSpy is sideloaded through a TianySpy malware delivered via smishing messages. It also poses as an 

Android app using different app names, and, once installed, can collect banking credentials and Wi\-Fi settings.

Vulnerabilities

Total Vulnerabilities
(Number of published Zero\-Day Initiative (ZDI) vulnerability advisories)

1,706
2022

1,913
2023

2727

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Zero\-Day Exploits (ZDI) Advisories 

The first quarter of 2023 starts with relatively low zero\-day advisories, with a significant increase by the end of the 

quarter in March. The second quarter fluctuates and peaks in May, while the third quarter stabilizes at a relatively 

high level of activity. The last quarter dips to the year’s lowest number of zero\-day advisories in October, picks 

back up again in November, but shows a slight downturn in the last month indicating a possible decrease in 

threat actor activity as the year ended.

293

283

176

200

179

157

109

93

109

114

117

83

300

200

100

0

JAN 

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

ZDI Industrial Control System and Zero\-Day Vulnerabilities

ICS

ICS Zero\-Day Vulnerabilities

47

43

26

35

36

32

9

4

5

1

15

8

0

0

0

0

0

0

0

0

0

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

12

15

29

50

40

30

20

10

0

0

10

20

30

40

50

2828

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Non\-ICS and N\-Day Vulnerabilities

223

193

181

141

84

83

105

111

143

106

47

42

250

200

150

100

50

0

JAN 

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

Riskiest CVEs by 
customer count

3 riskiest 
unpatched CVEs

60,731

58,184 

58,173

CVE\-2023\-24880

CVE\-2023\-21823

CVE\-2023\-23376

59,798

57,808

57,797

80K

60K

40K

20K

0

0

20K

40K

60K

80K

CVE\-2023\-2488 (Windows SmartScreen Security Feature Bypass Vulnerability)

• CVSS base score: 4\.4 medium

CVE\-2023\-21823 (Windows Graphics Component Remote Code Execution Vulnerability)

• CVSS base score: 7\.8 high

CVE\-2023\-23376 (Windows Common File Log System Driver Elevation of Privilege Vulnerability)

• CVSS base score: 7\.8 high

2929

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Risk Events

Top 2 Risk Events Detected 

The top two risk events detected via our attack surface risk management (ASRM) involve risky cloud applications 

and accessing risky websites.

82,976,277,500
Risky Cloud App Access

18,819,067,819
Risky Website Access Detected

• SOCs are recommended diligence in monitoring cloud applications accessed by their networks, especially as 

more organizations are integrating cloud environments in their operations. 

• Security teams should also conduct training to equip end\-users with the knowledge to identify and avoid 

accessing risky websites and links; human negligence remains the weakest link in cybersecurity.

Top Countries with Risk Events Detected

The United States of America recorded the most risk events at over 31\.2 billion detections, almost doubling the 

number of the country with the second most risk events, India at 16\.5 billion detections.

1

31,271,416,757
United States

4

7,888,655,174
Great Britain

7,816,148,246
Germany

5

16,570,427,847
India

2

3

15,060,300,143
Brazil

3030

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Recommendations for Lowering Risk

Apply the latest patch or upgrade your operating system or application version.

Apply prevention rules from Trend Micro products to protect vulnerabilities from being exploited.

Optimize weak settings in current environment.

Avoid accessing the reported risky app or make the app a sanction one

Disable accounts with weak passwords or reset them with strong ones. Enable the Account Lockout 

Policy in your Active Directory.

Restrict user account usage on affected device and verify and resolve the at\-risk device’s high\-risk 

events.

3131

CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Trend Micro, a global cybersecurity leader, helps make the world safe for exchanging digital information. Fueled by decades of security expertise, global threat research, and continuous innovation, our unified cybersecurity platform protects over 500,000 organizations and millions of individuals across clouds, networks, devices, and endpoints.The Trend Vision One™ unified cybersecurity platform delivers advanced threat defense techniques, extended detection and response (XDR), and integration across the IT ecosystem, including AWS, Microsoft, and Google, enabling organizations to better understand, communicate, and mitigate cyber risk. Trend Micro’s global threat research team delivers unparalleled intelligence and insights that power our cybersecurity platform and help protect organizations around the world from 100s of millions of threats daily.We have 7,000 employees across 65 countries, singularly focused on security and passionate about making the world a safer and better place.Trend Micro enables organizations to simplify and secure their connected world.TrendMicro.com©2024 by Trend Micro, Incorporated. All rights reserved. Trend Micro and the Trend Micro t\-ball logo are trademarks or registered trademarks of Trend Micro, Incorporated. All other company and/or product names may be trademarks or registered trademarks of their owners.CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT