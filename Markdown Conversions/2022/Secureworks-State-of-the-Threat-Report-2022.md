# State of the Threat 2022: A Year in Review

## Table of Contents
- [Letter From Our Chief Threat Intelligence Officer (CTIO)](#letter-from-our-chief-threat-intelligence-officer-ctio)
- [Executive Summary and Key Findings](#executive-summary-and-key-findings)
- [Ransomware Remains the Primary Strategic Threat](#ransomware-remains-the-primary-strategic-threat)
- [Ransomware Enablers: Loaders and Infostealers](#ransomware-enablers-loaders-and-infostealers)
- [Exploitation of Remote Services is Now the Most Common Access Vector](#exploitation-of-remote-services-is-now-the-most-common-access-vector)
- [Hostile Government-Sponsored Actor Activity Shows a Regional Focus](#hostile-government-sponsored-actor-activity-shows-a-regional-focus)
- [Defense Evasion Offers Its Own Detection Opportunities](#defense-evasion-offers-its-own-detection-opportunities)
- [Conclusion](#conclusion)
- [The Secureworks View of the Threat](#the-secureworks-view-of-the-threat)

## Letter From Our Chief Threat Intelligence Officer (CTIO)
The last twelve months have featured a series of headline-grabbing cybersecurity events. In December 2021, disclosure of a vulnerability in the popular Log4j software caused global panic as IT teams scrambled to find and patch vulnerable systems. In early 2022, the Russian military build-up on the Ukrainian border and subsequent invasion raised the specter of disruptive cyberattacks that might spill beyond Ukraine’s borders, as happened with NotPetya in 2017. And in mid-April, Conti ransomware knocked offline several Costa Rican government institutions, severely disrupting their ability to effectively deliver public services.

Our job is to dig beneath these headlines to understand the nature of the threat and mitigate the risk to our customers. We do that through up-to-date threat intelligence that is fueled by data-driven detection and analysis. The Secureworks® Counter Threat Unit™ (CTU) continues to analyze trillions of security events every week, gathered from its Taegis™ XDR platform. Together with the data processed through the Taegis Vulnerability Detection and Response (VDR) solution, proactive research, and insights gathered through engagements carried out by the Secureworks Incident Response team, this combines to create one of the most comprehensive views of the threat landscape in the industry.

The purpose of this report is to share our view on how the threat landscape has evolved over the last twelve months, with a clear focus on our first-hand observations of threat actor tooling and behaviors. The report reviews changes in the ransomware landscape, and in the behavior of threat actors enabling ransomware groups with malware like loaders and stealers. It surveys significant activity by major government-sponsored threat groups. And it examines how threat actors move swiftly to exploit new vulnerabilities, and how they combine sophisticated with more basic techniques to evade detection by defenders once inside the network. The report concludes by examining how Taegis forms the backbone of this visibility.

Across Secureworks, different teams work together to protect our customers. Our CTU™ research teams invest countless hours in developing an understanding of the threat and how it might manifest, and then in building ways to detect that threat which can be applied to our Taegis XDR and VDR platforms. Our Security Operations teams act as the watchful guardian of our customer networks, monitoring constantly for any changes that might indicate malicious activity. Our Incident Response team stands ready to support customers through the provision of proactive training, to help them prepare; and through reactive support to investigate, contain and remediate where breaches do occur. And our Secureworks Adversary Group emulates adversary behaviors to help customers test how their control frameworks perform in realistic, intelligence-driven scenarios.

Human expertise works with the technical excellence of Taegis XDR and Taegis VDR to keep Secureworks customers safe on their security journey. We hope the insights embodied in this report help you to protect your organization.

Barry Hensley
Chief Threat Intelligence Officer
Secureworks

## Executive Summary and Key Findings
Over the past year, cybersecurity events have been heavily influenced by escalating tensions in eastern Europe and the Middle East, a steady stream of critical vulnerabilities forcing organizations to scramble to patch their systems, and public leaks exposing the inner workings of organized cybercriminal ransomware gangs.

The role of the Secureworks Counter Threat Unit is to maintain an understanding of these diverse threats and apply that understanding to inform and protect customers. Between the end of June 2021 and June 2022, based on insights from customer telemetry, incident response, underground monitoring, proactive threat research and intelligence relationships, CTU researchers observed the following high-level trends across the threat landscape:

- Ransomware remains the primary threat facing organizations. Detection strategies should focus on identifying ransomware precursors during the 'detection window' between initial access and ransomware deployment. The median detection window in 2022 is four and a half days.
- Based on learnings[^1] from Secureworks incident response engagements, exploitation of remote services has replaced credential-based access as the most common initial access vector, stressing the need for effective vulnerability management and prioritization.
- There has been flux in the loader landscape, with the disappearance of some established loaders and the emergence of new ones. As the malware that loads second-stage payloads like ransomware, loaders form a key component of the ransomware ecosystem. There is evidence of close collaboration between the groups operating these loaders, and signs of a possible shift towards lightweight, disposable loaders in place of the complex botnets that up until now have provided this loader capability.
- Infostealers provide the means to quickly and easily obtain credentials that can be used for initial access, making them a major enabler of ransomware operations. On a single day in June 2022, CTU researchers observed over two million credentials obtained by infostealers available for sale on just one underground marketplace. Innovative distribution methods for infostealers have included cloned websites and trojanized installers for messaging apps such as Signal.
- Nation-state activity has been heavily focused on regional considerations. Notable examples include Russia's cyber operations in support of the invasion of Ukraine, disruptive reciprocal attacks likely conducted by Iranian and Israeli proxy actors, and China's continued focus on the South China Sea and East Asia.
- Defense evasion is a feature of many network intrusions. However, the techniques used are generally not very sophisticated, because they do not need to be. This provides additional detection opportunities.

[^1]: Learning from Incident Response: 2021 Year in Review, Secureworks. https://www.secureworks.com/resources/rp-learning-from-incident-response-team-2021-year-in-review

## Ransomware Remains the Primary Strategic Threat
The composition of the global ransomware landscape and the number of victims continue to fluctuate. Yet overall, despite a series of high-profile law enforcement interventions and public leaks, ransomware operators have maintained high levels of activity.

Analysis of Secureworks incident response engagements for May and June 2022 appears to suggest that the rate at which new, successful ransomware attacks are happening is reducing, although it is too early to say if this is trend will continue.

![Figure 1. Key developments in the ransomware landscape, June 2021 - June 2022. (Source: Secureworks)]

The demise of GOLD ULRICK's[^2] Conti ransomware-as-a-service operation could account for some of this reduction, but not all. Other factors influencing the rate of attacks might include the disruptive effect on ransomware gangs of the war in Ukraine, economic sanctions designed to create friction for ransomware operators trying to cash in on their attacks, and the volatility of the digital currencies through which ransomware gangs realize their profits.

However, there could be something else going on. There is no corresponding trend of a year-on-year reduction in the number of organizations listed on public ransomware leak sites (figure 2). And CTU researchers are investigating whether there is a general trend in the size of those victim organizations reducing over time. Smaller organizations are likely to be less well resourced, making them a softer target and one that is less likely to bring in specialist incident response services after the event. And some ransomware gangs may have decided that hitting higher numbers of smaller organizations is less likely to provoke a strong law enforcement response than hitting large, global brands. Unfortunately, smaller organizations may also be less familiar with the mechanism for reporting to and accessing support from law enforcement and specialist security vendors, meaning that the true impact of ransomware will continue to be under reported and victims will not receive the support they need.

Regardless of the overall trend, for any individual organization ransomware remains a major threat and one that feeds on gaps in security control frameworks. Examination of Secureworks threat research and incident response data provides insights into the tactics of individual threat groups and highlights lessons that can help organizations better protect themselves.

![Figure 2. Publicly listed ransomware victims by month. (Source: Secureworks)]

[^2]: GOLD ULRICK threat group profile, Secureworks. https://www.secureworks.com/research/threat-profiles/gold-ulrick

### The Window of Opportunity for Network Defenders
During any network intrusion, there is a window of opportunity for defenders. This happens between the point of initial access and the encryption of data when the threat actors are consolidating their access prior to achieving their ultimate objective. So far in 2022, the median time between initial access and ransomware detonation in intrusions investigated by Secureworks incident responders is 4.5 days, compared to 5 days in 2021. The mean dwell time in 2021 was 22 days but so far in 2022 is down at 11 days, reflecting that there have been fewer 'outliers' compared to 2021, i.e. intrusions where threat actors spent weeks or months in an environment before deploying their ransomware.

Of course, this dwell time can vary significantly. In early 2022, an organization exposed a computer in an operational technology (OT) environment to the internet with the firewall disabled to troubleshoot network connectivity issues and download patches. Within five hours the computer had been compromised and within a further hour, the threat actors had disabled Windows Defender and deployed Phobos ransomware. While only a small number of devices were affected and the network was isolated from the rest of the organization, the intrusion was sufficient to temporarily disrupt business operations at that location.

In contrast, analysis of a Lorenz ransomware attack in September 2021 showed that the threat actors, tracked by CTU researchers as GOLD LOUNGE[^3], had access for almost a year. The initial intrusion likely occurred in October 2020, with GOLD LOUNGE periodically re-accessing the compromised environment to run reconnaissance commands, occasionally rotating the remote IP address they connected in from. They made extensive use of SMBExec to move laterally to other hosts within the environment. In September 2021, GOLD LOUNGE staged Lorenz ransomware in the SYSVOL directory of several compromised domain controllers and created scheduled tasks with random names on target systems to download and execute the ransomware. They then deleted volume shadow copies and cleared the security event log. One hypothesis to explain this lengthy delay is that GOLD LOUNGE purchased access from an initial access broker (IAB) long after the IAB first obtained it.

Regardless of the length of the detection window, network defenders can and should exploit it. On numerous occasions, Taegis XDR countermeasures have alerted customers to ransomware precursors in their environment, allowing them to isolate impacted hosts, block the command-and-control infrastructure, and reset compromised credentials before the threat actors can capitalize on the access. The difference in terms of time to recovery, total costs incurred and business disruption, compared to organizations who did not spot the threat in time, can be huge.

Average (median) dwell time for ransomware actors: **4.5 Days**

[^3]: GOLD LOUNGE threat group profile, Secureworks. https://www.secureworks.com/research/threat-profiles/gold-lounge

### Prevent Where You Can, and Detect What Can’t Be Prevented
Undoubtedly, the best way to protect your organization against ransomware deployment is to prevent or detect the initial breach.

This requires a tight focus on good, basic security hygiene.
- Ensure that all external and key internal systems are protected with multi-factor authentication (see chapter 5 for tips on avoiding pitfalls).
- Implement a timely vulnerability detection and patching program (see more about vulnerabilities in chapter 3).
- For those situations where prevention fails, visibility of the environment is critical. You can't protect what you can't see. Trying to develop that visibility after you've identified a breach is too late.
- Deploy a comprehensive monitoring and detection solution on all endpoints, network, and cloud (see the appendix for important monitoring considerations).

![Figure 3. Initial access vectors for ransomware incidents, June 2021 - June 2022. (Source: Secureworks)]

### New Players, Old Players
During the reporting period new ransomware groups appeared, many only briefly or with little impact, while others apparently disappeared. In some cases, this fluctuation represented a rebrand by established ransomware groups, possibly to minimize law enforcement and media scrutiny, and in some cases to disguise their identity in response to financial sanctions. In others, it may have been a result of the shifting allegiance of affiliates in the hunt for more victims and greater revenues.

![Figure 4. Major ransomware schemes active during the period, showing number of victims per month. (Source: Secureworks)]

### Law Enforcement Actions
Over the reporting period, there have been several significant law enforcement actions or sanctions aimed at disrupting ransomware operators or their access to supporting services such as cryptocurrency money laundering.
- U.S. Treasury OFAC sanctions[^4] in December 2019 targeting GOLD DRAKE[^5], also known as Evil Corp, have led to the threat group repeatedly changing ransomware variants to complicate attribution of their attacks back to them, so that victims do not find themselves prohibited from paying the ransom. During the reporting period, they switched between several ransomware families including WastedLocker, Macaw, and potentially also LockBit[^6].
- In April 2022, OFAC sanctioned Hydra Market (Hydra), the world's largest darknet market. OFAC identified that approximately $8 million in ransomware proceeds had been laundered through it. It also sanctioned Garantex, a virtual currency exchange registered in Estonia thought to have processed transactions worth nearly $6 million from GOLD ULRICK's Conti operation.
- In May, OFAC sanctioned virtual currency mixer[^7] Blender.io (Blender), which had allegedly obscured transactions for Russian cybercrime groups including GOLD ULRICK and GOLD BLACKBURN[^8], and for North Korean threat actors.
- Also in May[^9], the U.S. State Department offered a financial reward for information leading to the arrest of senior members of the Conti ransomware operator.

Legal action aimed at ransomware actors over the period included the Department of Justice's partial seizure from a Darkside affiliate of the ransom paid by Colonial Pipeline; the multi-country operation that took control of REvil servers in October, forcing them offline, and operator GOLD SOUTHFIELD into hibernation; and the arrest in Russia of individuals associated with the REvil ransomware-as-a-service (RaaS) operation in January.

Action aimed at supporting services included the U.S. Department of Justice unveiling[^10] an indictment filed in 2020 against Latvian national Alla Witte for her role as a malware developer in the operation of TrickBot. Chats contained in the Conti Leaks[^11] showed GOLD BLACKBURN allocating funds for finding a lawyer to represent Witte. RaidForums, used to sell databases containing billions of card and banking details, as well as login credentials, also closed in April, as the result of Operation TOURNIQUET[^12], a complex law enforcement effort coordinated by Europol. The site was closed, its infrastructure seized, and its administrator and his accomplices arrested.

The long-term impact of increased law enforcement activity against ransomware operators remains difficult to judge. The process of having to re-brand undoubtedly introduces cost for ransomware actors, including potentially through the loss of affiliates to other RaaS schemes. And many victims do hesitate to pay ransoms to sanctioned groups. However, ransomware groups have shown an ability to recover from disruptive interventions and identify alternative means of sustaining their operations. The lack of cooperation from countries where core members of the prominent ransomware groups reside continues to hamper disruption efforts.

[^4]: Treasury Sanctions Evil Corp, the Russia-Based Cybercriminal Group Behind Dridex Malware, U.S. Department of the Treasury, accessed 7/27/22. https://home.treasury.gov/news/press-releases/sm845
[^5]: GOLD DRAKE threat group profile, Secureworks. https://www.secureworks.com/research/threat-profiles/gold-drake
[^6]: To HADES and Back: UNC2165 Shifts to LOCKBIT to Evade Sanctions, Mandiant, accessed 8/4/22. https://www.mandiant.com/resources/unc2165-shifts-to-evade-sanctions
[^7]: Cryptocurrency tumbler, Wikipedia, accessed 7/27/22. https://en.wikipedia.org/wiki/Cryptocurrency_tumbler
[^8]: GOLD BLACKBURN threat group profile, Secureworks. https://www.secureworks.com/research/threat-profiles/gold-blackburn
[^9]: Reward Offers for Information to Bring Conti Ransomware Variant Co-Conspirators to Justice, U.S. Department of State, accessed 8/4/22. https://www.state.gov/reward-offers-for-information-to-bring-conti-ransomware-variant-co-conspirators-to-justice/
[^10]: Latvian National Charged for Alleged Role in Transnational Cybercrime Organization, Department of Justice, accessed 7/27/22. https://www.justice.gov/opa/pr/latvian-national-charged-alleged-role-transnational-cybercrime-organization
[^11]: GOLD ULRICK Leaks Reveal Organizational Structure and Relationships, Secureworks. https://www.secureworks.com/blog/gold-ulrick-leaks-reveal-organizational-structure-and-relationships
[^12]: One of the world's biggest hacker forums taken down, Europol, accessed 7/27/22. https://www.europol.europa.eu/media-press/newsroom/news/one-of-world%E2%80%99s-biggest-hacker-forums-taken-down

### GOLD MYSTIC's LockBit RaaS
GOLD MYSTIC's[^13] LockBit RaaS was the most active name-and-shame operation, listing 875 victims on its public leak site by the end of June 2022. Secureworks incident responders have responded to LockBit intrusions against organizations in the technology, business services, media, finance, and legal sectors across the Middle East, Europe, the U.S., Asia, and Australia. GOLD MYSTIC appears to have been highly effective at recruiting affiliates from other RaaS schemes, and in at least one case CTU researchers were able to link a July 2021 LockBit incident to a June 2021 REvil incident, assessing with moderate confidence that the same affiliate was responsible for both incidents as well as for an earlier January 2021 incident reported[^14] by Ahnlab.

[^13]: GOLD MYSTIC threat group profile, Secureworks. https://www.secureworks.com/research/threat-profiles/gold-mystic
[^14]: BlueCrab ransomware that keeps performing detection evasion, ASEC, accessed 7/27/22. https://asec-ahnlab-com.translate.goog/jp/19952/?_x_tr_sl=ja&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=sc

### The (Non) Return of REvil
On April 19, 2022, CTU researchers observed two dormant Tor sites associated with REvil become active again. Both sites were redirecting to a new Tor site that appeared to be a revamp of the original REvil leak site. The new leak site retained the original list of victims, as well as three new victims. This was odd, given that GOLD SOUTHFIELD[^15] initially went offline shortly after the Kaseya attack[^16] that occurred over Independence Day weekend in July 2021 and then was forced offline permanently by a collaborative law enforcement[^17] effort in October.

Naturally, the use of the same Tor infrastructure and REvil source code caused speculation about whether REvil was back, despite the reported[^18] arrest of members of the group by the Russian FSB in January 2022. But in spite of these early signs of a resurgence, REvil is yet to reach its former level of activity.

Intriguingly, CTU researchers identified[^19] REvil samples compiled in March at a time when, according to the Russian authorities, members of the group were still in custody[^20]. This could indicate that the individuals had been quietly released prior to that point, or perhaps the arrests were of fringe members and had no real impact on the group's operational capabilities. The timing also coincides with the breakdown of cooperation between Russia and the U.S. on cybercrime.

[^15]: GOLD SOUTHFIELD threat group profile, Secureworks. https://www.secureworks.com/research/threat-profiles/gold-southfield
[^16]: Customer Advisory: Kaseya VSA Software Under Active Attack, Secureworks. https://www.secureworks.com/blog/kaseya-vsa-software-under-active-attack
[^17]: EXCLUSIVE Governments turn tables on ransomware gang REvil by pushing it offline, Reuters, accessed 8/2/22. https://www.reuters.com/technology/exclusive-governments-turn-tables-ransomware-gang-revil-by-pushing-it-offline-2021-10-21/
[^18]: Russia takes down REvil hacking group at U.S. request - FSB, Reuters, accessed 7/27/22. https://www.reuters.com/technology/russia-arrests-dismantles-revil-hacking-group-us-request-report-2022-01-14/
[^19]: REvil Development Adds Confidence About GOLD SOUTHFIELD Reemergence , Secureworks. https://www.secureworks.com/blog/revil-development-adds-confidence-about-gold-southfield-reemergence
[^20]: REvil prosecutions reach a 'dead end,' Russian media reports, Cyberscoop, accessed 8/2/22. https://www.cyberscoop.com/revil-prosecutions-reach-a-dead-end-russian-media-reports/

### The Perils of Timestamps—Can They Be Trusted?
Analysis of REvil's resurgence relied in part on analysis of compilation timestamps. Compilation timestamps show when a file, in this case a REvil ransomware binary, was created and can be useful for building a timeline of threat actor activity. But they can, and often are, falsified by threat actors. Threat intelligence analysts need to be careful in relying on them. CTU researchers have been tracking GOLD SOUTHFIELD since 2019 and have processed thousands of REvil samples. Whenever a new version of REvil has appeared, the compilation timestamp for the executable aligns with what is expected of a new release. Compilation timestamps also align for samples across multiple different campaigns. Therefore, while compilation timestamps should generally be treated cautiously, in this case they are a useful data point.

### ALPHV Works Cross-Platform
It is increasingly common for ransomware groups to compile ransomware that can be deployed across multiple operating systems. One example is GOLD BLAZER's[^21] ALPHV ransomware, also known as BlackCat, which emerged in December 2021. Based on insights from multiple ALPHV intrusions worked by Secureworks incident responders, the operators move from initial infection to data exfiltration within a few days, to deploying ransomware within approximately one week. In one incident, GOLD BLAZER or one of its affiliates abused a single-factor authentication Virtual Private Network (VPN) for the initial infection vector. After compromising the device, the threat actors conducted reconnaissance and used Mimikatz to harvest credentials. Using these stolen credentials, the threat actors logged into domain administrator accounts and used the access to stage, compress, and exfiltrate files.

ALPHV is written in Rust, making the ransomware scalable across Windows and Linux operating systems without needing to maintain distinct codebases. Its configuration file (figure 5) includes options to terminate ESXi 'vm' and 'vm snapshot' files. The hybrid approach of listing Linux and Windows file extensions is unusual.

![Figure 5. ALPHV configuration file. (Source: Secureworks)]

[^21]: GOLD BLAZER threat group profile, Secureworks. https://www.secureworks.com/research/threat-profiles/GOLD-BLAZER

### Hive Proves Effective at Attracting Affiliates
Hive is another ransomware that has featured heavily in incident response engagements worked by Secureworks during the period. The operators of the Hive RaaS, GOLD HAWTHORNE[^22], have been active since at least June 2021.

Since April 2022, CTU researchers have attributed a series of Hive-related intrusions to a single affiliate, GOLD MATADOR[^23]. GOLD MATADOR gains access to networks through VPN or Remote Desktop Protocol (RDP) servers using compromised credentials. After conducting reconnaissance to enumerate domains and harvest credentials using tools like PCHunter64, SharpView and Mimikatz, the group moves laterally using RDP with stolen credentials. The SystemBC proxy tool is used to disguise network traffic and Cobalt Strike Beacon is installed across number hosts for command and control. The group explores directories and views specific files before using FileZilla for data exfiltration and then ultimately deploying the Hive ransomware via Group Policy Object or Scheduled Task (figure 6).

![Figure 6. Scheduled Task (veeamupdate) used by GOLD MATADOR to detonate Hive ransomware. (Source: Secureworks)]

[^22]: GOLD HAWTHORNE threat group profile, Secureworks. https://www.secureworks.com/research/threat-profiles/GOLD-HAWTHORNE
[^23]: GOLD MATADOR threat group profile, Secureworks. https://www.secureworks.com/research/threat-profiles/GOLD-MATADOR

### Experimentation With Hack and Leak Continues
The Secureworks 2021 State of the Threat report highlighted hack and leak incidents (where no ransomware was deployed) as a potential shift away from the traditional ransomware-based extortion model. It remains unclear whether this approach provides a viable long-term business model, but some groups such as GOLD TOMAHAWK[^24] continue to practice it. Also known as Karakurt Team or Karakurt Lair, GOLD TOMAHAWK has been active since mid-2021.

GOLD TOMAHAWK intrusions typically start with access through internet-facing VPN endpoints, likely leveraging vulnerabilities or weak or stolen credentials. Once inside the network, GOLD TOMAHAWK does not deploy custom tooling, relying instead on off-the-shelf tools and applications, often native to the victim system, to meet its objectives. The threat group has been observed to use RDP for lateral movement, AnyDesk for remote access, 7-Zip to compress data for extraction, and the Mega and QuickPacket file-upload services for exfiltration.

Another hack and leak actor that emerged during the period is the GOLD RAINFOREST[^25] (Lapsus$) threat group, who claimed responsibility for several high-profile breaches including against Microsoft, Samsung and Nvidia. Identified members of GOLD RAINFOREST don’t match the typical stereotype of Russian-organized cybercriminals. But the success they were able to achieve in a short space of time is a cautionary tale about the importance of understanding how easy it can be for threat actors with a moderate level of capability and, critically, a means of accessing an organization's network to carry out attacks.

![Figure 7. GOLD TOMAHAWK (Karakurt) leak site screenshot. (Source: Secureworks)]

[^24]: GOLD TOMAHAWK threat group profile, Secureworks. https://www.secureworks.com/research/threat-profiles/GOLD-TOMAHAWK
[^25]: GOLD RAINFOREST threat group profile, Secureworks. https://www.secureworks.com/research/threat-profiles/gold-rainforest

## Ransomware Enablers: Loaders and Infostealers
Malware distribution forms a key component of the broad infrastructure that both supports and fuels the ransomware ecosystem. Delivery techniques continue to evolve, and the relationship between established ransomware operators and malware distribution operators remains a close one.

### Now You See Them, Now You Don't
Between July 2021 and June 2022, two big names in the loader landscape disappeared and two returned, demonstrating that writing off botnets and their associated malware, even after periods of inactivity, can be premature.

Emotet returned in November 2021, following its January 2021 takedown by international law enforcement agencies. During this downtime, its developers, tracked as the GOLD CRESTWOOD[^26] threat group, had made some changes. The Emotet code appeared enhanced and streamlined, with more modern cryptography, different communications protocols, a switch to 64-bit architecture, more customizable execution options, and new command and control (C2) infrastructure. CTU researchers also observed evidence of GOLD CRESTWOOD experimenting with re-implementing deprecated functionality such as modules to steal credit card information from web browsers and self-propagation[^27] using SMB and a list of hardcoded credentials.

Conti operator GOLD ULRICK was likely instrumental[^28] in Emotet’s return, and the Conti Leaks provided evidence of the close relationship between the ransomware group and GOLD CRESTWOOD. Emotet reappeared as a DLL download from TrickBot, suggesting that GOLD CRESTWOOD aimed to rebuild the Emotet botnet by using long-time collaborator GOLD BLACKBURN's TrickBot infrastructure. Emotet was also distributed through malicious Windows App Installer packages disguised as Adobe PDF software, much like GOLD BLACKBURN's BazarBackdoor malware. In January 2022, CTU researchers observed Emotet executing reconnaissance commands (see figure 8) replacing functionality that was previously provided by intermediate payloads Qakbot and TrickBot.

![Figure 8. Emotet executing reconnaissance commands and credential-theft tools. (Source: Secureworks)]

[^26]: GOLD CRESTWOOD threat group profile, Secureworks. https://www.secureworks.com/research/threat-profiles/GOLD-CRESTWOOD
[^27]: Lazy Passwords Become Rocket Fuel for Emotet SMB Spreader, Secureworks. https://www.secureworks.com/blog/lazy-passwords-become-rocket-fuel-for-emotet-smb-spreader
[^28]: Emotet botnet comeback orchestrated by Conti ransomware gang, Bleeping Computer, accessed 7/27/22. https://www.bleepingcomputer.com/news/security/emotet-botnet-comeback-orchestrated-by-conti-ransomware-gang/

In March, Emotet resumed dropping Qakbot, using the 'azd' Qakbot campaign ID which likely refers to a GOLD LAGOON[^29] affiliate. Qakbot had itself taken a two-month hiatus in 2021, reappearing on September 9, 2021. During the break, Qakbot's backend infrastructure was for the first time switched off rather than left to idle, leading the security community to question if the hiatus could be permanent. Since its return, Qakbot has resumed its role as a major player in the loader landscape.

On October 18, CTU researchers observed Qakbot deploying a new plugin containing the legitimate Atera remote management and monitoring (RMM) software to all infected devices (figure 9).

The TrickBot botnet stopped responding to infected systems on March 1, 2022, after a progressive decrease since mid-2021 in the tempo of updates to TrickBot-infected hosts via its C2 infrastructure. There were no signs of it returning to life by August, and it seems likely that the group intends to permanently abandon it.

![Figure 9. msiexec.exe launching the Windows installer file that installs the Atera RMM software. (Source: Secureworks)]

![Figure 10. Timeline of TrickBot activity from July 2021 through March 2022. (Source: Secureworks)]

[^29]: GOLD LAGOON threat group profile, Secureworks. https://www.secureworks.com/research/threat-profiles/gold-lagoon

The Conti Leaks may shed some light on the decision to abandon TrickBot, as they include conversations about TrickBot's declining utility and BazarLoader's increasing maturity. In a sign of the speed with which the threat landscape can change, by April 2022 a new loader called Bumblebee was being used in Conti and Diavol ransomware attacks in preference to BazarLoader. However, TrickBot's design means GOLD BLACKBURN retains the capability to re-enable the C2 infrastructure and recapture existing bots if the group chooses to.

There were lulls in IcedID activity between July and November 2021, and between February and May 2022, but activity levels have continued to increase since May 2022. In 2021 the operators of IcedID, GOLD SWATHMORE[^30], reworked the malware’s networking functionality to include Base64-encoded information about the victim system in the HTTP Cookie and Authorization header (figure 11).

Distribution for IcedID also changed during 2021, to distribute ISO files containing Windows shortcut (LNK) files that execute a colocated DLL file containing the IcedID payload. In a March 2022 intrusion, an attacker compromised an internet-facing Microsoft Exchange Server via the ProxyShell vulnerability and used access to the compromised server to send internal phishing emails containing hijacked email threads and an attached IcedID payload. This technique of using compromised email servers to send internal phishing emails is likely an effort to ensure that emails appear to come from a trusted sender, bypassing security controls that warn users by tagging emails that originate externally.

![Figure 11. IcedID HTTP POST request with encoded victim information. (Source: Secureworks)]

[^30]: GOLD SWATHMORE threat group profile, Secureworks. https://www.secureworks.com/research/threat-profiles/gold-swathmore

![Figure 12. Taegis XDR detection for IcedID malware. (Source: Secureworks)]

### New on the Scene
There have been a number of new loaders that have emerged during the reporting period, and in some cases disappeared again. CTU researchers assess that the groups operating these loaders may move away from the complex, fully-featured botnets that evolved from the early banking trojans towards more lightweight loaders that are easier to develop and maintain. That shift is likely enabled by increased use of fully featured and actively maintained post-exploitation tools such as Cobalt Strike. The role of the loader is simply to achieve an initial access point, perhaps perform some basic reconnaissance such as checking that the infected host is joined to an Active Directory domain, and then retrieve and execute the post-exploitation tool.

#### Bumblebee
CTU researchers' analysis of Bumblebee reveals rapid development and numerous active campaigns. Multiple threat actors now appear to have moved to using Bumblebee to drop payloads that include Cobalt Strike, Sliver[^31], and Meterpreter in order to deliver ransomware.

#### PureCrypter
PureCrypter is a fully featured malware builder and loader advertised for sale since March 2021 at $59 USD for one month and $249 for lifetime use. It is a .NET executable obfuscated with SmartAssembly. It is widely used to drop payloads for cybercriminal ends. In addition, CTU researchers assess with moderate confidence that the developers of the WhisperGate[^32] file wiper that was deployed against targets in Ukraine prior to the Russian invasion used PureCrypter to generate the .NET code in both the loader and the initial payload.

![Figure 13. PureCrypt and associated tool pricing at https://purecoder.sellix.io/ (Source: Secureworks)]

[^31]: BishopFox / sliver, accessed 8/4/22. https://github.com/BishopFox/sliver
[^32]: WhisperGate: Not NotPetya, Secureworks. https://www.secureworks.com/blog/whispergate-not-notpetya

#### SquirrelWaffle
SquirrelWaffle loader was first detected in September 2021, delivering Qakbot and Cobalt Strike. Initially, some third-party commentators characterized it as an heir to Qakbot, Emotet, or IcedID. However, by early November, SquirrelWaffle's infrastructure had been disabled and the loader was not observed again in active distribution. CTU researchers saw only a small number of SquirrelWaffle infections across customer environments (figure 14).

![Figure 14. iSensor IDS detection for SquirrelWaffle HTTP POST request that uses padding and a hardcoded XOR key. (Source: Secureworks)]

### Bringing the Victim to You: Drive-By-Download as an Alternative Distribution Method
'Drive-by-downloads' continue to be a popular alternative to phishing-based malware distribution. Notable examples include the prolific SocGholish malware framework, operated by GOLD PRELUDE[^33