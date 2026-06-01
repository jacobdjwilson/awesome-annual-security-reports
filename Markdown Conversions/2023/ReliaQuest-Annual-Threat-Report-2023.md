# ReliaQuest Annual Cyber-Threat Report 2023

## Table of Contents
- [Executive Summary](#executive-summary)
- [The Evolving Cyber Threat Landscape: Understanding the Current Risks](#the-evolving-cyber-threat-landscape-understanding-the-current-risks)
- [What Our Data Revealed](#what-our-data-revealed)
- [Active Months and Targeted Sectors](#active-months-and-targeted-sectors)
- [Most Common Kill Chain Phases](#most-common-kill-chain-phases)
- [Most Commonly Detected Techniques](#most-commonly-detected-techniques)
- [GreyMatter Digital Risk Protection (GMDRP) Alert Trends](#greymatter-digital-risk-protection-gmdrp-alert-trends)
- [Most Common GMDRP Risk Alerts](#most-common-gmdrp-risk-alerts)
- [Alerts via Sector](#alerts-via-sector)
- [What Steps Should Defenders Take Now?](#what-steps-should-defenders-take-now)
- [Initial Access Broker (IAB) Trends](#initial-access-broker-iab-trends)
- [Most Common Access Types](#most-common-access-types)
- [Most Commonly Targeted Countries](#most-commonly-targeted-countries)
- [Most Commonly Targeted Sectors](#most-commonly-targeted-sectors)
- [Case Study: Exotic Lily](#case-study-exotic-lily)
- [Initial Access Malware](#initial-access-malware)
- [Vulnerability Intelligence](#vulnerability-intelligence)
- [Where the Risks Lie](#where-the-risks-lie)
- [Risk Calculation](#risk-calculation)
- [Vulnerabilities Deep Dive](#vulnerabilities-deep-dive)
- [Ransomware Intelligence](#ransomware-intelligence)
- [Ransomware Attack Kill Chain](#ransomware-attack-kill-chain)
- [Most Targeted Sectors](#most-targeted-sectors)
- [Most Active Ransomware Groups](#most-active-ransomware-groups)
- [Case Study: LockBit](#case-study-lockbit)

---

## Executive Summary
This report offers an in-depth and inclusive view of the cyber-threat landscape, over what has been an exceptionally challenging 12 months for cyber security professionals (1 February 2022 to 1 February 2023). Over the course of this period, the ReliaQuest Threat Research Team has identified trends across several data sources and analyzed them to provide readers with insights into cyber-threat trends and observations. During a reporting period that saw Russia’s invasion of Ukraine, a continued risk of ransomware attacks and data extortion, and an avalanche of high-risk vulnerabilities, we identified the following key events and patterns:

- The attempted exploitation of exposed remote services was the most commonly detected attack technique. Those services, including virtual private networks (VPNs) and remote desktop protocol (RDP), pose a very high risk. A wide range of attackers, including cybercriminals and nation-state–aligned groups, have exploited them to access a network or establish persistence on it.
- ReliaQuest identified wide use of defense evasion techniques, notably indicator removal, data destruction, and the sub-technique of clear command history. This emphasizes the significant efforts threat actors place on obfuscating their activity.
- ReliaQuest’s GreyMatter Digital Risk Protection (GMDRP) service yielded data that identified especially vulnerable sectors. They are most susceptible to: fraud via impersonating retail web domains, significant risk from exposed credentials (particularly for financial services), and exploitation of open ports at utilities companies.
- CVE-2022-22965 (aka Spring4Shell) is regarded to pose the greatest risk of all high-risk vulnerabilities, for its available and easy exploits and its potential to cause a technical and business impact.
- The most common access type advertised by initial access brokers (IABs) was RDP, which accounted for 24.4% of all ReliaQuest “tippers” published in the reporting period. RDP access was also the costliest type being offered, with an average median price of approximately $1,000.
- Initial-access malware continued to be delivered mainly by phishing emails. Threat actors adapted their techniques to circumvent organizational controls, and in ReliaQuest customer environments, we detected many instances of the “Emotet,” “SocGholish,” “IcedID,” “GootLoader,” and “Bumblebee” malware.
- “LockBit” was, overwhelmingly, the most active ransomware group, and is increasingly using the SocGholish malware distribution framework to gain initial access to networks which is making their efforts more potent. We anticipate even more use of SocGholish by ransomware groups during 2023.
- NameCheap was the most common registrar of Cobalt Strike team servers, followed by Ename Technology and MarkMonitor. These registrars are primarily content delivery networks (CDNs) used for domain fronting. Domain fronting is used to conceal user traffic and is commonly used by threat actors for command and control (C2) purposes.

## The Evolving Cyber Threat Landscape: Understanding the Current Risks
The cyber threat landscape is increasingly complex and subject to consistent change. The rapid advancement of technology and reliance on digital systems leave individuals and organizations facing an array of cyber threats. While cybercriminals and nation-state aligned threats use varying techniques, there are consistent observable trends that are used by many of these groups. Taking a deep dive into these trends by collating and analyzing data sources across our customer environments, allowed us to identify several insights into the state of the current cyber threat landscape.

## What Our Data Revealed
The data for this analysis was extracted from customer incidents collated by ReliaQuest. The data set covers February 1, 2022, 00:00:00 UTC to February 1, 2023, 00:00:00 UTC (12 months). There were 35,024 true-positive incidents during that reporting period.

### Active Months and Targeted Sectors
![Figure 1: Number of true-positive tracked incidents per month]
Figure 1 shows a steady increase in true positives[^1], notably between August 2022 and January 2023, but with a noticeable drop-off in December 2023—potentially because threat actors were less active over the end-of-year festive holiday season.

[^1]: A True Positive or Confirmed Incident is an event or alert which identified malicious activity that resulted in either an attempt or successful unauthorized access, use, modification, or destruction of any information system or data.

![Figure 2: Average number of incidents per customer sector]
The number in front of each Figure 2 sector shows how many incidents, on average, any given client in that sector can expect to see over the course of a year. Construction had the most during this reporting period, followed by transportation, then wholesale trade.

### Most Common Kill Chain Phases
![Figure 3: Kill chain phases detected in incidents, ranked by prevalence]
Figure 3 highlights the most commonly detected kill-chain phases, identified through incident data.

### Most Commonly Detected Techniques
![Figure 4: Top 10 most detected techniques]
Taken from our collection of true positive incident data was the most commonly observed attacker techniques. Figure 4 highlights the top 10 of these techniques, including T1133 External Remotes Services which was overwhelmingly the most commonly seen technique.

![Figure 5: Top 10 most commonly observed sub-techniques]

## GreyMatter Digital Risk Protection (GMDRP) Alert Trends
By continually monitoring open, deep, and dark web sources to isolate legitimate threats and provide quick and easy remediation, it provides a unique view of security threats outside an organization.

### Most Common GMDRP Risk Alerts
![Figure 6: Most common risk types, by thousands of GMDRP alerts]
The most common was, overwhelmingly, credential exposure—unsurprising, given the abundance of third-party breaches, risky user practices, and insufficient controls over managing credentials.

### Alerts via Sector
![Figure 7: Ten ReliaQuest-customer sectors that received the most alerts, divided by total number of clients]

During the reporting period (February 1, 2022 to February 1, 2023), ReliaQuest identified 231,150 impersonating domains and 162,895 impersonating subdomains.

[Table 1: Ten most common risk types per sector, by number of GMDRP alerts]
*(Table content omitted for brevity, but includes data for Finance, Health Care, Retail, etc.)*

![Figure 8: Excerpt of a port-scanning guide shared on a cybercriminal forum]
![Figure 9: Forum advertisement of a phishing kit dedicated to spoofing Google]

## What Steps Should Defenders Take Now?
- In order to minimize Defence Evasion and Impact techniques, organizations should ensure sufficient monitoring is in place to identify suspicious or abnormal activity.
- Credential exposure: Identify breached credentials, validate that the credentials are current, contain the credentials usage, and educate the credential’s user.
- Exposed ports: Enumerate and document which services are publicly accessible. Close those that do not need to be.
- Domain impersonation: Ensure that registered domains, branding information, IP address ranges, and other assets are all sufficiently monitored.

## Initial Access Broker (IAB) Trends
IABs act as the “middlemen” in cyber threat operations: finding vulnerable organizations, exploiting them to access their systems, then selling that access to the highest bidder on dark-web forums.

### Most Common Access Types
![Figure 10: Most common IAB access types listed for sale, and price ranges from 01 Feb 2022 – 01 Feb 2023]
The most common access type listed by IABs was RDP, which accounted for 24.4% of all tippers released during the reporting period.

![Figure 11: AVC site Russian Market sells compromised RDP credentials]

### Most Commonly Targeted Countries
![Figure 12: Countries most commonly targeted by IAB activity between 01 Feb 2022 – 01 Feb 2023]
The most commonly targeted country for IAB activity was overwhelmingly the US.

### Most Commonly Targeted Sectors
![Figure 13: Sectors most commonly targeted by IAB activity]
Manufacturing took top place, prompting the publication of 142 tippers.

### Case Study: Exotic Lily
![Figure 14: Typical IAB lifecycle, as observed with Exotic Lily]
ReliaQuest uncovered a good example to hold up for examination. The “Exotic Lily” IAB began by sending elaborate phishing emails from what appeared to be a potential business prospect, to the inbox of a high-profile employee.

### Initial Access Malware
- **QakBot**: Frequently used malicious OneNote files to deliver malware.
- **Emotet**: Distributed through malicious Word files containing macros.
- **GootLoader**: A first-stage downloader designed to attack Windows-based systems.
- **IcedID**: Developed into a malware dropper employed on compromised systems.
- **SocGholish**: Employs social engineering and drive-by compromise to drop malware on endpoints.

![Figure 15: HTML Smuggling attack lifecycle]
![Figure 16: SocGholish fake update message and linked button]

## Vulnerability Intelligence
Given that there were over 24,000 CVEs in 2022, knowing which to prioritize is challenging.

![Figure 17: Relationships of vulnerability intelligence]

## Where the Risks Lie
![Figure 18: Number of CVEs found in top technologies used by ReliaQuest]

## Risk Calculation
To enhance the risk assessment of CVEs, we have developed an automated scoring tool that effectively integrates intrinsic CVE data and the insights our Vulnerability Intelligence team gathers and analyzes continuously.

[Table 2: Highest risk CVEs found in products most used by ReliaQuest customers, by technology vendor]

## Vulnerabilities Deep Dive
- **Spring4Shell (CVE-2022-22965)**: A critical remote code execution (RCE) flaw discovered in the widely used Spring Core framework for Java in March 2022.
- **Log4Shell (CVE-2021-44228)**: Found in the Apache Log4J 2 Java library.
- **Oracle EBS (CVE-2022-21587)**: Allowed an attacker to upload arbitrary files on devices.
- **Fortinet (CVE-2022-40684)**: Adversaries were exploiting the flaw to bypass authentication and log on to the vulnerable systems as an administrator.

![Figure 19: PoC for CVE-2022-21587 shared on cybercriminal forum]

## Ransomware Intelligence
Ransomware poses the biggest cyber threat to organizations globally.

### Ransomware Attack Kill Chain
![Figure 20: Five typical steps of a ransomware attack]

### Most Targeted Sectors
![Figure 21: Number of victims named on ransomware data-leak sites, by month]
![Figure 22: Number of ransomware attacks in the reporting period, by sector]

### Most Active Ransomware Groups
![Figure 23: Most active ransomware groups as indicated by number of attacks]
The most active group, by far, was LockBit, with 946 posts naming victims on the group’s data-leak site.

### Case Study: LockBit
ReliaQuest investigated an incident involving the LockBit ransomware and its eponymous operating group.

---

tial access
was found to be the result of a SocGholish infection. Following this, Cobalt Strike was loaded on to the host and C2
established. The threat actor began to move laterally in the environment via a combination of Cobalt Strike and RDP. After
a few days of movement in the network, they had obtained credentials for a service account with domain administrator
permissions.
Then began a two-month-plus period of inactivity, for no clear reason. One theory relates to the timing of the intrusion,
which started within a day of the Russian invasion of Ukraine. Geopolitical tension in the region was high following the
invasion and included groups and individuals within the cybercrime community. This tension may have played a factor in
the long dormancy. However, there was an increase in organizations named on LockBit’s data-leak site during those two
months, so the war may not have had much impact on operations at the time.
Make Security Possible
25

After the dormant period, LockBit returned and resumed its operation by continuing to cement a foothold in the
environment. The group moved laterally to additional high-value servers via RDP and compromised additional
administrator-level accounts.
Next, LockBit began staging the encryptor 昀椀le and a copy of psexec on a network. A new Group Policy Object (GPO)
was created to launch and execute a BAT 昀椀le via a scheduled task. The BAT 昀椀le attempted to halt speci昀椀c process and
services, such as antivirus or endpoint detection and response (EDR), as well as stop the backup service and delete
Shadow Volume Copies. It copied the encryptor and psexec from the network share, then used psexec to execute the
encryptor. Finally, it was set to clear all tokens from error logs using wevutil.
One unique technique is LockBit’s compromise of an account with administrator-level privileges in the organization’s
EDR console, and use of it to deregister EDR sensors on all hosts in the environment. With defenses fully disabled, a GPO
update was pushed, setting off encryption throughout the environment.
What Steps Can Defenders Take Now?
Network Recommendations
• Segment networks: Ensure proper network segmentation of devices so that they can only communicate with other
devices needed to support their speci昀椀c business functions.
• Monitor external-facing assets: For accidental exposure and out-of-date services, remove any accidental exposure
and patch any out-of-date services, prioritizing services that have known vulnerabilities. Threat actors frequently scan
the internet for public-facing assets that have an exploitable vulnerability and gain initial access that way.
Internal System Recommendations
• Use application control: Where appropriate and, if possible, only permit the execution of signed scripts. Consider
redirecting the default application for JavaScript, Visual Basic, and other executable script formats to open in
notepad.exe instead of wscript.exe by default. The use of weaponized script 昀椀les is used heavily by initial access
malware.
• Comprehensive coverage: Ensure coverage is enabled for antivirus/EDR tools within your environment to provide
as much visibility as possible to exploit or threat activity. Valuable detection use cases require endpoint logging or
visibility.
• Use automatic updates: Apply a software update feature to your computer, mobile device, and other connected
devices wherever possible and pragmatic.
Account Recommendations
• Inventory accounts: Service and other privileged accounts in the environment should be accounted for. Ensure
that they follow the principle of least privilege (PoLP) and are con昀椀gured with long, complex passwords. Service
accounts are highly targeted in ransomware intrusions, given that they are often con昀椀gured improperly with domain
administrator rights.
• Use standard user accounts: Internal systems should only use standard user accounts, instead of administrative
accounts that grant overarching administrative system privileges and do not ensure PoLP.
Make Security Possible
26

Cobalt Strike Ransomware Intelligence
So, an IAB has identi昀椀ed your network prone for targeting. Exploited an unpatched system that shouldn’t be externally
facing, before selling the access onto one of the dozens of ransomware groups looking for their next victim. Our new
unauthorized friends are busy hopping around the network looking for methods of maintaining their persistence, while
also identifying which systems might be candidates for encryption, or hold data that can be stolen. What is the method
used by most groups to coordinate their activity? Enter Cobalt Strike.
The C2 framework that is overwhelmingly used by ransomware groups is that of the legitimate penetration testing tool
Cobalt Strike. Its popularity is likely owing to a combination of effectiveness and user-friendliness. Attackers often
rely heavily on C2 communications to start and progress attacks, including human-operated ransomware attacks. C2
infrastructure enables attackers to control infected devices, perform malicious activity, and quickly adapt to a targeted
organization’s environment in pursuit of valuable data and assets.
Breaking this link to C2 infrastructure disrupts attacks—either by stopping the communication completely or delaying
its progression, allowing more time for a SOC to investigate and mitigate the intrusion. By default, Cobalt Strike enables
payload staging via a valid checksum8 request; a checksum refers to a process of checking a 昀椀le’s integrity. The Cobalt
Strike team server will then return a shellcode payload, from which security researchers can extract the payload’s
con昀椀guration. The con昀椀guration contains details of how the implant operates, including the C2 address, the C2 port, the
spawn to process, and the license ID.
The default con昀椀gurations of team servers have been well documented by members of the intel community. By searching
for unique values in the HTTP response headers, JARM signatures, and default certi昀椀cates, through network scan data
services like Shodan, ReliaQuest can pro昀椀le potential Cobalt Strike team servers.
With a compiled list of potential team servers, scans can be made in an attempt to retrieve a payload. If a payload is
returned, an IP address/domain can be con昀椀rmed as a team server, which can then be added to our threat feeds for
alerting. These domains/IP addresses can be a high-昀椀delity indicator of a malicious actor in the environment. Given the
ease of collection, these indicators are a great supplement to other behavior-based detections.
What Our Data Tells Us
Table 3 shows the top countries in which Cobalt Strike team servers were hosted; Table 4 shows the top autonomous
system numbers (ASNs) used to host these team servers. China hosted the vast majority of the identi昀椀ed Cobalt Strike
team servers, followed by the US and Hong Kong. This is unsurprising, given that the abuse of Cobalt Strike is not limited
to cybercriminals; it is also used heavily by Chinese nation-state–aligned groups.
Country Servers Hosted
China 4,830
US 3176
Hong Kong 781
Russia 325
Singapore 176
Lithuania 175
Romania 150
United Kingdom 128
Netherlands 122
Germany 114
Table 3: Number of Cobalt Strike team servers, by host country
Make Security Possible
27

China is also, unsurprisingly, widely represented in the ASNs hosting Cobalt Strike team servers, harboring the large
majority of the top ten. An autonomous system is a large network or group of networks that have a single routing policy.
Each autonomous system is assigned a unique ASN, which is a number that identi昀椀es the autonomous system. These are
typically owned and operated by a single service provider.
ASN Count
45090 - TENCENT-NET-AP Shenzhen Tencent Computer Systems Company Limited, CN 2,695
37963 - ALIBABA-CN-NET Hangzhou Alibaba Advertising Co.,Ltd., CN 1,136
14061 - DIGITALOCEAN-ASN, US 674
20473 - AS-CHOOPA, US 390
16509 - AMAZON-02, US 373
8075 - MICROSOFT-CORP-MSN-AS-BLOCK, US 203
14618 - AMAZON-AES, US 190
55990 - HWCSNET Huawei Cloud Service data center, CN 181
132203 - TENCENT-NET-AP-CN Tencent Building, Kejizhongyi Avenue, CN 177
134548 - DXTL-HK DXTL Tseung Kwan O Service, HK 164
Table 4: Number of Cobalt Strike team servers, by ASN
The most common C2 ports can be seen in Table 5; the default ports for HTTP and HTTPS (80 and 443) are the most
commonly used for communication.
C2 port Count
443 4,892
80 3,829
8080 675
8443 541
8090 271
8888 247
8081 183
9999 177
4444 172
8088 167
Table 5: Most commonly used C2 ports during reporting period, by number of instances
Of the Beacon payloads recorded during the time period, most were con昀椀gured with an IP address for C2. The C2 address
is often the same as the team server address. For beacons that used a domain for C2, a majority used content delivery
networks, such as those of Tencent, CloudFront, and Azure. The use of these services helps beaconing blend in with
legitimate tra昀케c. Table 6 highlights the top registrars used for C2 domains.
NameCheap was the most common registrar of Cobalt Strike team servers, followed by Ename Technology and
MarkMonitor. These registrars—which can be seen represented by the stars right of their name—are primarily content
delivery networks (CDNs) used for domain fronting. Domain fronting is used to conceal user tra昀케c and is commonly used
by threat actors for C2 purposes.
Make Security Possible
28

Registrar Count
NAMECHEAP, INC. 353
ENAME TECHNOLOGY CO.,LTD. * 330
MARKMONITOR, INC. * 295
GODADDY.COM, LLC 247
OWNREGISTRAR, INC. 171
NICENIC INTERNATIONAL GROUP CO., LIMITED 122
GANDI SAS 103
NAMESILO, LLC 99
HOSTING CONCEPTS B.V. D/B/A REGISTRAR.EU 95
AMAZON REGISTRAR, INC. 86
Table 6: Most commonly used registrars during reporting period, by number of uses
Our data identi昀椀ed the most commonly used “spawn to” processes: temporary processes spawned by the Cobalt Strike
implant, which are used to inject code that carries out post-exploitation commands. Each beacon con昀椀guration will list a
spawn to process for x86 and x64 architecture. However, the process selected is typically the same for both. The default
spawn to process is rundll32.exe. This is a great detection opportunity, as many of the top spawn to processes are rarely
executed without command line arguments.
Spawn to x64 Count
%windir%\sysnative\rundll32.exe 8,087
%windir%\sysnative\dllhost.exe 1,342
%windir%\sysnative\gpupdate.exe 232
%windir%\sysnative\svchost.exe 195
%windir%\sysnative\WUAUCLT.exe 185
%windir%\sysnative\runonce.exe 184
%windir%\sysnative\regsvr32.exe 149
%windir%\sysnative\WerFault.exe 105
%windir%\sysnative\WerFault -a 73
%windir%\sysnative\choice.exe 45
Table 7: Most commonly used spawn to processes (x64) during reporting period, by number of uses
Spawn to x86 Count
%windir%\syswow64\rundll32.exe 8,087
%windir%\syswow64\dllhost.exe 1,342
%windir%\syswow64\gpupdate.exe 233
%windir%\syswow64\svchost.exe 196
%windir%\syswow64\runonce.exe 184
%windir%\syswow64\WUAUCLT.exe 173
%windir%\syswow64\regsvr32.exe 150
%windir%\syswow64\WerFault.exe 106
%windir%\syswow64\WerFault -a 75
%windir%\syswow64\choice.exe 45
Table 8: Most commonly used spawn to processes (x86) during reporting period, by number of uses
Make Security Possible
29

The watermark is the unique license ID for each Cobalt Strike build. Trial versions, cracked versions, and stolen legitimate
versions of Cobalt Strike have been leaked and distributed in the wild, making it di昀케cult to attribute based on the
watermark. However, it can be helpful when clustering infrastructure with additional con昀椀guration settings. Table 9 shows
the top watermark IDs seen in the data.
Watermark Count
1234567890 2,343
0 1,692
305419896 1,216
426352781 1,016
100000 698
1580103824 662
1359593325 542
391144938 431
206546002 387
Table 9: Most commonly used Cobalt Strike watermark ID during reporting period, by number of uses
What Steps Can Defenders Take Now?
• Many of the C2 domains are newly registered domains and are categorized as such by many forward proxies. If your
forward proxy solution supports this, consider setting policies to block domains categorized as recently registered.
• Ensure that network telemetry is centrally logged, so that monitoring can be put in place to detect anomalous
connections.
• Host-based telemetry offered by EDR technologies play a crucial role in detecting behaviors of Cobalt Strike and other
post-exploitation frameworks. Ensure there is signi昀椀cant EDR coverage across the host within your environment, to
provide as much visibility as possible
Conclusion
This report aimed to identify trends related to the current cyber threat landscape, looking at data and observations of
activity tracked by ReliaQuest in 2022. From our observations we can draw several conclusions based on our data.
• Each sector faces unique challenges, many of which are highly dependent on a company’s business model or
operating requirements. As identi昀椀ed by our breakdown of GMDRP alerts, some risks will be more pertinent for certain
sectors; however steps can be taken to minimize any possible impact. Visibility and context is key - understand what
speci昀椀c threats your business face and apply compensating controls where appropriate.
• The most commonly observed attacker technique was aimed at exploiting external-facing remote services. These
were attempted to either initially access and/or persist within a network. This highlights the ongoing problem of
su昀케ciently hardening remote services, which includes the use of Citrix, VPN, and notably, RDP. The exploitation of
remote services will continue to represent arguably the most common abuse point for entering your network, by
both cybercriminals and nation-state aligned threat actors, across all sectors. Ensure that remote services are not
unnecessarily external facing, patched with strong authentication measures in place, using the principle of least
privilege to ensure only individuals who need to do their job can access them.
Make Security Possible
30

• Taking a patch-all approach to vulnerability management is an ineffective method of tackling vulnerability risk. Adding
vulnerability intelligence can guide your security team in tackling the CVEs that represent the greatest chance of
causing an impact to your business. Getting a robust, consistent, and repeatable vulnerability remediation program in
place can go a long way in raising your overall cyber resilience.
• Initial access malware continues to be delivered via phishing emails, with threat actors adapting their techniques
to minimize the effectiveness of organizational controls. This is likely to go hand in hand with the ongoing risk
associated with ransomware activity, who often use IAB and associated techniques as the point of entry onto a target
network. Increasing resilience to IA malware is best accomplished through a combination of email security controls,
group policy to minimize the chance of a malicious 昀椀le being delivered/opened, and user awareness programs.
• Ransomware remains the biggest risk facing business in 2023. Ransomware actors are agile, resourceful, and capable
of reacting to defenders’ actions in changing their tactics. It is likely that the ransomware ecosystem will become
more saturated in 2023, with the introduction of several new groups. Keeping abreast of the latest developments in
TTPs of ransomware activity, in addition to tracking groups known to be targeting your sector, is the best way to stay
ahead of the curve from this pernicious activity.
• Use the trends identi昀椀ed in this report to inform your own threat model and act accordingly. It’s always better to ‘stay
left of boom’ and act in a proactive manner. Prevention is always a better approach than remediation.
How ReliaQuest can help:
Put our threat intelligence technology to work for you. With the ReliaQuest GreyMatter security operations platform, you
can get unparalleled visibility into your entire ecosystem—and beyond.
The GreyMatter Intel capability is fully con昀椀gurable; use our pre-de昀椀ned set of threat feeds or even add your own. We’ll
take that data and return actionable insights on threats and IoCs. And with Digital Risk Protection (DRP), you can be sure
your data is safe outside your environment too.
To learn more, visit www.reliaquest.com. Set up a custom demo to walk through your environment and learn how
ReliaQuest can help.
If you would like any further information on any of the threats detailed in this report, please contact ReliaQuest’s Threat
Research team.
reliaquest.com 800.925.2159 info@reliaquest.com
Copyright © 2023 ReliaQuest, LLC. All Rights Reserved. ReliaQuest, GreyMatter, Digital Shadows, and all related logos, product and services names, designs, and slogans are trademarks or registered
trademarks of ReliaQuest, LLC or its a昀케liates or licensors. All other product names or slogans mentioned in this document may be trademarks or registered trademarks of their respective owners or
companies. The ReliaQuest software, platform, portal and its entire contents, features, and functionality are owned by ReliaQuest, LLC and its a昀케liates. These materials are protected by United States
Manda inkteern Satieoncaul croiptyyrig Pht,o trsadseimbalrke, patent, trade secret, and other intellectual property or proprietary rights laws. All other information presented is provided for informational purposes with no
representations or warranties provided of any kind and should not be relied upon for any purpose. ReliaQuest has no obligation to amend, modify, or update the information contained in this document 31
in the event that such information changes or subsequently becomes inaccurate. Printed in the USA.