CALIBRATING 
EXPANSION2 0 2 3A NNUA LC YBERSECURIT YR EPOR T03APT
CAMPAIGNS07RANSOMWARE
THREATSCLOUD AND13 ENTERPRISETHREATS16MITRE ATT\&CK
DETECTIONS20THREAT
LANDSCAPEAPR
2022MAYJUNJULAUGSEPOCTNOVDECJAN
2023FEB MAR APR MAYJUNJULAUGSEPOCTNOVDECAPT28s NTLMv2
hash relay attacksAPT28s more recent 
credential phishing campaignGamaredonEarth LuscaEarth EstriesKimsukys continued activityVoid Rabisus slimmed down 
ROMCOM variantTurla attacks using
Capibar and KazuarAPT34s targeted
phishing attackMustang PandaAPT38Konni GroupAPT29s VovaMirage
spear phishing campaigAPT28s NTLMv2
hash relay attacks
April 2022 August 2023Targets:
Organizations involved in a wide 
range of elds, but primarily in
foreign aairs, energy, defense,
and transportationPossibly an attempt to brute\-force its 
way into target networksExploited CVE\-2023\-23397 that was 
patched in March 2023, at which point 
APT28 used more elaborate methods 
that involved scripts hosted on 
Mockbin sent to targetsAPT28s more recent 
credential phishing campaign
November December 2023Targets:
Various government organizations
in EuropeShares similarities to the earlier hash 
relay campaign in technical indicators, 
such as sharing the same computer 
name used to send out spear\-phishing 
emails and to craft LNK les.3CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|APTCAMPAIGNSGamaredon
January November 2023Earth Lusca
January June 2023Targets:
Government organizations in
Ukraine
Gamaredon continues its activity with 
attacks using Remote Template 
Injection and self\-extracting executable 
lesThe timeline of increased activity of the 
investigated sample suggests the 
campaign was launched to intensify 
espionage activitiesEarth Estries 
January 2023 presentTargets:
Government organizations and
technology industries in the
Philippines, Taiwan, Malaysia,
South Africa, Germany, and the
USA.They use multiple backdoors and 
hacking tools, as well as PowerShell 
downgrade attacks to avoid detectionThey use public services such as 
Github, Gmail, AnonFiles, and File.io to 
exhance and transfer commands and 
stolen dataEarth Estries is known to deploy 
cyberespionage campaigns.Targets:
Government departments involved
in foreign aairs, technology, and
telecommunications in countries in
Southeast Asia, Central Asia, and
the Balkans, with scattered attacks 
on Latin American and African
countriesThe decrypted payload is a 
Linux\-targeted backdoor, a new variant 
named SprySOCKSTargets the public\-facing servers of its 
victimsKimsukys continued activity
April 2022, and April May 2023Targets:
Individuals working in elds related
to the Democratic Peoples
Republic of Korea
Possibly organizations related to
military, diplomacy, and
unications, and Korean\-language
support groups, based on
Kimsukys previous campaign
historyDelivered as an email leLikely aimed to gather information on 
geopolitical events, diplomatic 
strategies, and activities impacting the 
targets interestsCould also be launched to gather 
armament\-related information and for 
cryptocurrency\-related attacks44CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Void Rabisus slimmed down 
ROMCOM variant 
June August 2023Turla attacks using
Capibar and Kazuar
July 2023Targets:
Military personnel and political
leaders in EuropeExploited the then zero\-day 
vulnerability CVE\-2023\-36884Primarily known for cyberespionage 
activities targeting governments and 
military with nancial motivationsTargets:
Diplomatic and military
organizations in UkraineIn this phishing campaign, the Capibar 
malware was used for intelligence 
gathering, while the Kazuar malware 
was used for credential theft.Turla has been active since 2014, and is 
known for its cyberespionage activities.APT34s targeted
phishing attack
August 2023Mustang Panda
August 2023 presentTargets:
Possibly organizations inside the
Kingdom of Saudi ArabiaThe malicious document in the 
phishing scam dropped a new malware 
designed for espionage, capable of 
identifyiung the machine, reading and 
uploading les from the machine, and 
downloading another le or malware.APT34 is known for its cyberespionage 
activities targeting government 
agencies, organizations involved in 
critical infrastructure, and 
telecommunications in the Middle East.Targets:
Government organizations in the
 Philippines, and other relatedorganizationsUtilized components of legitimate 
software commonly used in Southeast 
Asia for DLL sideloadingPossibly launched for information 
gathering purposesSamples contain strings that suggest 
the possibility of attacking Myanmar 
government ocials55CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \| 
APT38
May September 2023Konni Group
November 2023Targets:
Cryptocurrency\-related organization, investment rms, and
 banksDetected in a sample used by 
BlueNoro, which is associated with 
APT38\. The sample was later reported 
by SentinelOne as used in the later 
stages of SwiftLoader and indicated in 
a connection between KandyKorn and 
SwiftLoaderLikely nancially motivated and 
launched to acquire foreign currency to 
fund armaments and espionageTargets:
Companies within the Republic of KoreaAssociated with OSMIUM, Opal Sleet, 
SectorA07, TA406, and KimsukyAccording to our analysis, the 
campaigns malicious zip le contains 
an LNK le, that when executed drops 
html and VBScript to fetch additional 
payloads, possibly pointing to APT37\.Possibly launched as additional means 
of acquiring foreign currencyAPT29s VovaMirage spear phishing campaign
November 2023Targets:
Embassies and diplomatic entities in European countries, particularly Azerbaijan, Greece, Romania, and ItalyExploited WinRAR vulnerability CVE\-2023\-38831 in a spear phishing campaignLikely launched to gather information on strategic activities involving the respective country 
targets66CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|What to Watch Out ForThe following tactics were observed in 2023 and could possibly be seen in the coming year as ransomwareactivities grow more sophisticated.There is a continued increase in the use of remote encryptionObserved in Akira, BlackCat, BlackMatter, LockBit, and RoyalAttackers actively map drives to encrypt on the affected endpoint instead of doing lateralmovement. This could be a leap in tactics to reduce their footprint in attacks to avoid detection.Ransomware groups are also maximizing the convenience of intermittent encryptionObserved in NoEscape, Ransomware Play, BlackBasta, Agenda, and BlackCatAttackers encrypt chunks of data instead of encrypting all data in one go; this process speedsup encryption while still rendering the affected data useless to the victim, and also makes for amore complicated decryption process.Endpoint Detection and Response (EDR) bypass using unmonitored virtual machines (VM)Observed in Akira and BlackCatAttackers bypass EDR by creating unmonitored VMs to navigate, map and encrypt files within theWindows Hyper\-V hypervisor systems and attached VMs.Multi\-ransomware attacksThe initial attacker sells its access to other ransomware groups to launch multiple attacks witha combination of malware, data theft, and wiper tools to maximize manipulation and pressureagainst the victims.7CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|RANSOMWARETHREATSTotal Ransomware Detections61,132,33841,271,20880M60M40M20M014,066,77814,983,27114,169,86620192020202120222023There has been a general downward trend in ransomware detections, with detections from 2021 to 2023averaging less than half of the recorded detections in 2020; however, this should not be misconstrued as a cuefor security operations centers and decision\-makers to lower their guards. Historically, ransomware attacks werelaunched in bulk, such as spam campaigns with malicious links, but attacks that focus on quantity can moreeasily be blocked, as shown in our ransomware ERS and WRS data in the following figure. These figures show ageneral downward trend consistent with the total ransomware detections.However, a continued increase in FRS detections could suggest that attackers are using more effective ways toevade preliminary detection by focusing on arrival and defense evasion techniques such as Living\-Off\-The\-LandBinaries and Scripts (LOLBINsLOLBAs), Bring Your Own Vulnerable Driver (BYOVD), zero\-day exploits, and AVtermination. We detect and identify ransomware payloads as malicious at endpoint as the ways they get intosystems become more complex. This pattern is also observed in SPN data for overall threats blocked.7,645,1714,917,6246,647,5658M6M4M2M05M4M3M2M1M03,633,19352\.5%15\.0%10M8M6M4M2M02,535,3991,782,34948\.4%29\.7%20212022ERS20232021202320212022WRS8,754,3244,802,7012,501,58992\.0%82\.3%20232022FRS88CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Operating Systems Affected by Ransomware40K30K20K10K011,00027,60215,1543,7909,9614,949202120222023LinuxMacOSBased on data from our midyear report, customer detections on Linux\-targeted ransomware attacks from thefirst half of 2023 continues to overshadow MacOS attacks. This is consistent with data gathered from 2022, whichwas an exceptional year for Linux\-based malware detections, making up 25% of our telemetry; previously, Linux\-targeted attacks only made up two to three percent of the OS ratio. It should be noted that Windows continues totake the bulk of our ransomware detections, with the only significant decrease in 2022\.2019202020212022202397%94%92%71%92%3% 0%5% 1%5% 3%4% 25%5% 3%0%20%40%60%80%100%WindowsMacOSLinuxHowever, as our data for 2023 was completed, MacOS ransomware attacks came out higher with 9,961detections, while Linux detections were finalized at 4,949\. This could suggest that Linux\-targeted attacks arestabilizing after the influx of novel Linux variants in 2022 to early 2023, but it could also be influenced by theoverall decrease in ransomware activity.99CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Top Countries and Regions by 
Detected Ransomware AttacksThailand made up 68% of ransomware detections in Asia.21,640,144
United States3707,808
Turkey4454,008 
Taiwan5307,658
India6,080,644
Thailand110M8,842,8738M6M4M2M01,911,8911,095,868AsiaAmericasEurope1010CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Top Industries and Segments by 
Detected Ransomware Attacks20\.3KBanking9\.9KGovernment7\.7KTechnology166,069200K150K100K50K026,43021,2716\.3KRetail5\.6KFast\-Moving
Consumer GoodsEnterpriseConsumerSmall and
mid\-sized
businessesIndustry rankings and segment breakdowns based on unique detection counts at the endpoint shows thatenterprises are the primary targets, with significant interest in the banking sector in 2023\.1111CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Top Ransomware FamiliesStopCrypt and LockBit maintain the top spots in terms of most prolific ransomware families for 2023 as it did inthe previous year, but the former overtook the latter by a narrow margin this year. Note that this data does notinclude legacy ransomware families.Created and uses the malware StealBitfor automated data exltrationLaunched a bug bounty program in 2022
LockBit 3\.0 has code that shares
similarities to DarkSide and BlackMatter
Maximizes aliates who buy access totargets from other threat actors3,0012,8982,78120222,511LockBitStopCryptBlackCatWannarenRequires being executed with specic
arguments or parameters, additional
componens or in a specic environmentto proceed with its routineReported to have heavily targeted India
in 2023 alongside LockBit and BlackCat4,2774,2063,85720232,470StopCryptLockBitBlackCatConti3\.5K2\.5K1\.5K50005K4K3K2K1K01212CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Risk EventsTop Industries by Risk Events (ASRM)ManufacturingHealthcareTechnologyRetailFinancial ServicesGovernment
Public ServicesEducationTransportationInsuranceOthers21,386,430,41118,436,575,85617,793,629,11617,307,436,28313,408,802,18612,077,150,1548,954,860,9906,857,317,5266,689,288,80310,826,646,22505B10B15B20B25B13CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CLOUD ANDENTERPRISE THREATSHome Network Security Top EventsWith hybrid work now established as part of business operations, we looked at our Home Network Securitytelemetry to see what specific events cybercriminals particularly favor to use and what devices they target tomaximize the larger attack surface created by remote and home workspaces.1\.5B1,234,502,4391\.2B900M600M300M0322,792,561265,722,686248,331,853125,553,894Brute\-Force LoginMight be RDP via port 3389, FTP via port 21, or SSH via port 22 to repeatedly attempt to log in totarget hosts using a dictionary of common usernames and passwordsTELNET Default Password Login \-6Detects when a user within the network uses the default password to log inMISC BitcoinLitecoinDogecoin Mining Activity \-1Related to information disclosure and possibly to BitcoinLitecoinDogecoin Mining ActivityWEB HTTP InvalidContent\-Length \-2Caused by an error in processing HTTP packets containing negative Content\-Length header fieldvalues that result in a heap buffer overflowMISC Cryptocurrency Monero Mining Activity \-1Possible Monero (XMR) cryptocurrency mining activity1414CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Home Network Security Top Affected Device TypesDesktops and laptops recorded the most inbound attack detections based on our Home Network Securitytelemetry data.862\.8MDesktop
LaptopDevices283,384443,361198\.7MSmartphone105\.7MTablet19\.5MGame Console18\.4MNASAverage33,90023,314DesktopLaptopSmartphone4,78251,26246,33855,915TabletGame ConsoleNAS4,6273,676500K250K0017\.5K35KVulnerability by Vendor369223176101974003002001000AdobeMicrosoftD\-LinkPDF\-XChangeDelta
Electronics1515CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Top 5 Tactics Detected 
(Overall)Dodging security tools, communication and control of compromised systems, and gaining a foothold withinvictims systems and networks are the most used TTPs (overall, endpoints, network, and email)23,64221,32120,46518,33533,83635K25K15K5K0Defense
Evasion
(TA0005\)Command
and Control
(TA0011\)Initial
Access
(TA0001\)Persistence
(TA0003\)Impact
(TA0040\)16CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|MITRE ATT\&CKDETECTIONSTop Tactics, Techniques, and Procedures (TTPs) Endpoint33,46135K25K15K5K015,99014,50814,22113,871Defense
Evasion
(TA0005\)Impact
(TA0040\)Initial
Access
(TA0001\)Command
and Control
(TA0011\)Execution
(TA0002\)Top TTPs Network5,9576K4,6424K2K03,8393,3561,705Command
and Control
(TA0011\)Lateral
Movement
(TA0008\)Initial
Access
(TA0001\)Execution
(TA0002\)Impact
(TA0040\)1717CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|TTPs Overall Trend by DetectionsCommand and Control showed a gradual increase from September to December, while Defense Evasion peakedin March and July before declining in customer detections in subsequent months. Execution entered the topthree TTPs detected in July and August, while Impact showed no clear trend despite a spike in November.Persistence only entered the top three in the first quarter of the year but was in a downward trend beforedipping below the top three. Despite fluctuations, Initial Access maintains a moderate number of detections,since it is the primary goal of threat actors to gain a foothold in target victim systems and networks.Note that the monthly detections do not show data for May and June due to a system error experienced duringthat period.JanuaryFebruaryMarch5,2996K4K2K02,8371,7285,2756K4K2K01,6361,5876,0158K6K4K2K03,5731,947Persistence
(TA0003\)Defense
Evasion
(TA0005\)Impact
(TA0040\)Persistence
(TA0003\)Impact
(TA0040\)Initial
Access
(TA0001\)Defense
Evasion
(TA0005\)Impact
(TA0003\)Initial
Access
(TA0001\)AprilJulyAugustSeptember5,4405,2444,5675,0126K4K2K01,6791,6496K4K2K02,6202,4572,1123K2K1K02,6952,3991,7133K2K1K0Persistence
(TA0003\)Impact
(TA0040\)Initial
Access
(TA0001\)Defense
Evasion
(TA0005\)Execution
(TA0002\)Collection
(TA0009\)Defense
Evasion
(TA0005\)Execution
(TA0002\)Initial
Access
(TA0001\)Command
and Control
(TA0011\)Initial
Access
(TA0001\)Impact
(TA0040\)3K2K1K02,980October2,532NovemberDecember3,3053\.5K3,8043\.5K1,7141\.75K02,6382,3861\.75K02,5791,739Command
and Control
(TA0011\)Initial
Access
(TA0001\)Impact
(TA0040\)Command
and Control
(TA0011\)Initial
Access
(TA0001\)Impact
(TA0040\)Command
and Control
(TA0011\)Initial
Access
(TA0001\)Impact
(TA0040\)1818CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Living\-Off\-The\-Land TacticsPreferred for its eectiveness in harvesting
data while evading detectionFavored for Command and Control as this tactic
requires stealth and resilience to remain
undetected within compromised networks for an
extended period8,9567,513Mimikatz3,7473,914Cobalt
Strike00Brute
Ratel10K20K04K8K24438130GMER4008000150301H 20232H 2023Subcategory:TrojanFilelessBackdoorTTP:CollectionCommand
and ControlDefense EvasionThere is no clear trend in the detections, though Mimikatz and Cobalt Strike continue to be the preferredlegitimate tools to abuse to aid criminal activity. It can be assumed that threat actors prefer to use well\-knowntools instead of exploring novel ones, a logical behavior that is commonly observed as it guarantees morelikelihood of success with less effort.1919CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Malware DetectionCountries With the Most Malware Detections
and the corresponding top industries targeted for each2993,996,354
United States
Healthcare
Technology
Manufacturing45,030 
36,021 
9,4104277,616,731
Italy
Healthcare
Banking
Government15,086 
12,332 
9,49011,169,219,233
Japan
Manufacturing
Education
Healthcare4,206 
3,813 
3,8095256,383,037
Brazil
Government
Education
Financial 43,300
17,623
8,0513288,557,845
India
Manufacturing
Government
Banking34,110 
31,273 
30,253Note that industry data counts are limited to customers who have elected to provide details pertaining to thebusiness sectors in which they belong. Total malware detection counts include customers who did not provideany information on their industries.20CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|THREATLANDSCAPETop Countries Accessing Malicious URLs2382,881,197
United States484,300,801
China823,057,759
Japan1395,100,913
Taiwan76,730,598
Philippines5Top Industries Affected by Malware CampaignsFrom the aggregate average of our Smart Protection Network (SPN) data, malware campaigns targetedgovernment organizations the most with 302,555 detections.302\.6KGovernment228\.1KHealthcare212\.1KManufacturing179\.8KEducation176\.4KBanking2121CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|A cryptocurrency mining malware surpassed prolific names in 2023\.Top Malware FamiliesPersonal data remains the most valuable commodity in underground criminal communities; cryptocurrencywallets and crypto\-related data are the most actionable data that can be stolen by malicious actors, equivalent tocash that can immediately be spent without traceability.303,399249,949350K250K150K50K0202274,93380K202359,78845,65844,61743,013192,658125,204124,44360K40K20K0WebshellEmotetNegastealNemucodPowloadCoinMinerWebshellPowloadBondatDownadCryptocurrency mining malware CoinMiner takes the lead over notorious WebshellLast reported exploit: Oracle WebLogic Server vulnerabilities (CVE\-2020\-14882\)Reported to have been deployed by malicious Python Package Index packages targeting LinuxUses the victim systems central processing unit (CPU) andor graphical processing unit (GPU) resources tomine cryptocurrencyThe following can be observed during the infection:High CPU utilization either with powershell.exe or schtasks.exeMonero.Cryptocurrency.Miner app detection from the networkExecution source can be identified during service installationWMI powershell scripts on the DC serverDespite being overtaken, Webshell remains a go\-to for threat actorsExploits vulnerabilities in internet\-facing web servers2222CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Email ThreatsTop Countries by Detection110,425,179,000 
United States31,222,110,043
Netherlands41,214,975,535
Russia1,101,398,365
Germany52,079,512,425
China2High\-Risk Email ThreatsTotal malware
detection countTotal malicious and
phishing URLS countTotal business email
compromise count4,263,65019,149,46035,256,36025,665,848383,926446,234349%\-27%16%040M80M20222023While there is a decrease in malicious and phishing URL detections from 2022 to 2023, the increase in malwaredetection count and BEC count suggests the change in the threat landscape that finds attackers making use ofmore sophisticated ways to avoid detection. In this case, instead of focusing on malicious and phishing URLs torandomly victimize users, BEC schemes suggest more targeted operations, while a closer look at our malwaredetection count includes phishing links embedded within the attachments. This is consistent with patternsobserved in our SPN data on threats blocked from 2021 to 2023, where detections that rely on attribution ofURLs (WRS) and emails (ERS) show a decrease, while endpoint detections that directly identify malicious files haveconsistently increased.2323CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Top 5 Spam Attachments12M10,262,73710M8M6M4M2M02,007,6191,884,077700,566 448,155PDFEXEDOCXHTMLDOCSpam attachments per month of 20233,972,2652,667,4672,121,0291,124,230453,181481,862295,8011,297,8181,062,5921,080,318998,806918,1264M3M2M1M0JANFEBMARAPRMAYJUNJULAUGSEPOCTNOVDECThere is a general increasing trend for the first half of the year, where malicious spam attachment detectionspeaked in June. This is followed by fluctuations in the second half of the year, that eventually decline untilDecember. Despite more cunning ways to lure victims into clicking malicious links, spam campaigns remain a go\-to for cybercriminals.2424CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Threats Blocked146\.4BOverall threats
blocked in 2022161\.0BOverall threats
blocked in 2023The total number of threats blocked based on our SPN reached a record high in 2023, 10% higher from theprevious year. It also continues the dramatic climb of threats blocked that began to be recorded in 2021, the firstyear that surpassed the previous peak of 82 billion in 2016\. This coincided with the pandemic, strongly suggestingits role in driving the upswing.200B150B161,014,076,615146,408,535,569100B81,885,110,90466,495,174,31194,289,585,24066,495,590,12854,195,862,69748,473,430,40150B020162017201820192020202120222023Despite the overall threats blocked peaking in 2023, there is a fluctuating and downward trend in threats blockedunder our Email Reputation Service (ERS) and Web Reputation Service (WRS), indicating that threats in theseareas are being better managed or are less frequent. However, there is a continuous increase in threats blockedunder our File Reputation Service (FRS).2525CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|79,945,411,1463,468,559,50480B60B40B20B069,869,979,42573,858,986,7443\.5B2\.5B1\.5B7\.6%500M014\.4%202320212022ERS2,531,040,1852,356,888,44427\.0%6\.9%100B80B60B40B20B082,149,430,11060,925,991,94317,834,808,43820212022WRS20232021241\.6%34\.8%20232022FRSThis could be indicative of the changing threat landscape where it can be assumed that threat actors are nowopting for quality over quantity: Instead of launching attacks on a wider range of users and relying on victimsclicking on malicious links in websites and emails, more sophisticated attacks are launched using specificity totrick a narrower field of high\-profile victims. This also allows them to bypass early detection layers like networkand email filters. It could be speculated that this contributed to the continuous increase in malicious filedetections that are detected at endpoints.37,088,8363,073,227,6235,921,41420212022202336,547,9332,966,079,0483,465,31435,762,4722,611,751,3971,257,44801\.75B3\.5BMARSSHNIoTRSThere is also a continuous decrease in threats blocked under our Mobile Application Reputation Service (MARS),Smart Home Network (SHN), and Internet of Things Reputation Service (IoTRS), suggesting that cybercriminals arechoosing their targets carefully rather than randomly. It remains crucial to protect all layers of the attack surface,and SOCs should realize that understanding the attackers targeting strategies is important for effective defense.2626CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Android Malware Families3,030,5152,475,757920,098645,888247,5553\.5M2\.5M1\.5M500K0XLoaderPackerKeepSpyXloaderMMRatCovidRansomXLoaderPacker is a spyware that can be manually installed by a user. It poses as an Android app using differentapp names, and, once installed can monitor incoming and outgoing calls, and lock the screen of the affectedsystem.KeepSpy is sideloaded through a TianySpy malware delivered via smishing messages. It also poses as anAndroid app using different app names, and, once installed, can collect banking credentials and Wi\-Fi settings.VulnerabilitiesTotal Vulnerabilities
(Number of published Zero\-Day Initiative (ZDI) vulnerability advisories)1,706
20221,913
20232727CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Zero\-Day Exploits (ZDI) AdvisoriesThe first quarter of 2023 starts with relatively low zero\-day advisories, with a significant increase by the end of thequarter in March. The second quarter fluctuates and peaks in May, while the third quarter stabilizes at a relativelyhigh level of activity. The last quarter dips to the years lowest number of zero\-day advisories in October, picksback up again in November, but shows a slight downturn in the last month indicating a possible decrease inthreat actor activity as the year ended.29328317620017915710993109114117833002001000JANFEBMARAPRMAYJUNJULAUGSEPOCTNOVDECZDI Industrial Control System and Zero\-Day VulnerabilitiesICSICS Zero\-Day Vulnerabilities4743263536329451158000000000JAN 
2023FEBMARAPRMAYJUNJULAUGSEPOCTNOVDEC12152950403020100010203040502828CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Non\-ICS and N\-Day Vulnerabilities22319318114184831051111431064742250200150100500JANFEBMARAPRMAYJUNJULAUGSEPOCTNOVDECRiskiest CVEs by 
customer count3 riskiest 
unpatched CVEs60,73158,18458,173CVE\-2023\-24880CVE\-2023\-21823CVE\-2023\-2337659,79857,80857,79780K60K40K20K0020K40K60K80KCVE\-2023\-2488 (Windows SmartScreen Security Feature Bypass Vulnerability)CVSS base score: 4\.4 mediumCVE\-2023\-21823 (Windows Graphics Component Remote Code Execution Vulnerability)CVSS base score: 7\.8 highCVE\-2023\-23376 (Windows Common File Log System Driver Elevation of Privilege Vulnerability)CVSS base score: 7\.8 high2929CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Risk EventsTop 2 Risk Events DetectedThe top two risk events detected via our attack surface risk management (ASRM) involve risky cloud applicationsand accessing risky websites.82,976,277,500
Risky Cloud App Access18,819,067,819
Risky Website Access DetectedSOCs are recommended diligence in monitoring cloud applications accessed by their networks, especially asmore organizations are integrating cloud environments in their operations.Security teams should also conduct training to equip end\-users with the knowledge to identify and avoidaccessing risky websites and links; human negligence remains the weakest link in cybersecurity.Top Countries with Risk Events DetectedThe United States of America recorded the most risk events at over 31\.2 billion detections, almost doubling thenumber of the country with the second most risk events, India at 16\.5 billion detections.131,271,416,757
United States47,888,655,174
Great Britain7,816,148,246
Germany516,570,427,847
India2315,060,300,143
Brazil3030CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Recommendations for Lowering RiskApply the latest patch or upgrade your operating system or application version.Apply prevention rules from Trend Micro products to protect vulnerabilities from being exploited.Optimize weak settings in current environment.Avoid accessing the reported risky app or make the app a sanction oneDisable accounts with weak passwords or reset them with strong ones. Enable the Account LockoutPolicy in your Active Directory.Restrict user account usage on affected device and verify and resolve the at\-risk devices high\-riskevents.3131CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT \|Trend Micro, a global cybersecurity leader, helps make the world safe for exchanging digital information. Fueled by decades of security expertise, global threat research, and continuous innovation, our unified cybersecurity platform protects over 500,000 organizations and millions of individuals across clouds, networks, devices, and endpoints.The Trend Vision One unified cybersecurity platform delivers advanced threat defense techniques, extended detection and response (XDR), and integration across the IT ecosystem, including AWS, Microsoft, and Google, enabling organizations to better understand, communicate, and mitigate cyber risk. Trend Micros global threat research team delivers unparalleled intelligence and insights that power our cybersecurity platform and help protect organizations around the world from 100s of millions of threats daily.We have 7,000 employees across 65 countries, singularly focused on security and passionate about making the world a safer and better place.Trend Micro enables organizations to simplify and secure their connected world.TrendMicro.com2024 by Trend Micro, Incorporated. All rights reserved. Trend Micro and the Trend Micro t\-ball logo are trademarks or registered trademarks of Trend Micro, Incorporated. All other company andor product names may be trademarks or registered trademarks of their owners.CALIBRATING EXPANSION2023 ANNUAL CYBERSECURITY REPORT