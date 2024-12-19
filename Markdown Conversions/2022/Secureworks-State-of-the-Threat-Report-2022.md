# State of the Threat 2022
## A YEAR IN REVIEW

## Table of Contents
[Letter From Our Chief Threat Intelligence Officer (CTIO)](#letter-from-our-chief-threat-intelligence-officer-ctio)
[Executive Summary and Key Findings](#executive-summary-and-key-findings)
[Ransomware Remains the Primary Strategic Threat](#ransomware-remains-the-primary-strategic-threat)
[Ransomware Enablers: Loaders and Infostealers](#ransomware-enablers-loaders-and-infostealers)
[Exploitation of Remote Services is Now the Most Common Access Vector](#exploitation-of-remote-services-is-now-the-most-common-access-vector)
[Hostile Government-Sponsored Actor Activity Shows a Regional Focus](#hostile-government-sponsored-actor-activity-shows-a-regional-focus)
[Defense Evasion Offers Its Own Detection Opportunities](#defense-evasion-offers-its-own-detection-opportunities)
[Conclusion](#conclusion)
[The Secureworks View of the Threat](#the-secureworks-view-of-the-threat)

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

*   Ransomware remains the primary threat facing organizations. Detection strategies should focus on identifying ransomware precursors during the 'detection window' between initial access and ransomware deployment. The median detection window in 2022 is four and a half days.
*   Based on learnings<sup>1</sup> from Secureworks incident response engagements, exploitation of remote services has replaced credential-based access as the most common initial access vector, stressing the need for effective vulnerability management and prioritization.
*   There has been flux in the loader landscape, with the disappearance of some established loaders and the emergence of new ones. As the malware that loads second-stage payloads like ransomware, loaders form a key component of the ransomware ecosystem. There is evidence of close collaboration between the groups operating these loaders, and signs of a possible shift towards lightweight, disposable loaders in place of the complex botnets that up until now have provided this loader capability.
*   Infostealers provide the means to quickly and easily obtain credentials that can be used for initial access, making them a major enabler of ransomware operations. On a single day in June 2022, CTU researchers observed over two million credentials obtained by infostealers available for sale on just one underground marketplace. Innovative distribution methods for infostealers have included cloned websites and trojanized installers for messaging apps such as Signal.
*   Nation-state activity has been heavily focused on regional considerations. Notable examples include Russia's cyber operations in support of the invasion of Ukraine, disruptive reciprocal attacks likely conducted by Iranian and Israeli proxy actors, and China's continued focus on the South China Sea and East Asia.
*   Defense evasion is a feature of many network intrusions. However, the techniques used are generally not very sophisticated, because they do not need to be. This provides additional detection opportunities.

## Ransomware Remains the Primary Strategic Threat
The composition of the global ransomware landscape and the number of victims continue to fluctuate. Yet overall, despite a series of high-profile law enforcement interventions and public leaks, ransomware operators have maintained high levels of activity.

Analysis of Secureworks incident response engagements for May and June 2022 appears to suggest that the rate at which new, successful ransomware attacks are happening is reducing, although it is too early to say if this is trend will continue.

The demise of GOLD ULRICK's<sup>2</sup> Conti ransomware-as-a-service operation could account for some of this reduction, but not all. Other factors influencing the rate of attacks might include the disruptive effect on ransomware gangs of the war in Ukraine, economic sanctions designed to create friction for ransomware operators trying to cash in on their attacks, and the volatility of the digital currencies through which ransomware gangs realize their profits.

However, there could be something else going on. There is no corresponding trend of a year-on-year reduction in the number of organizations listed on public ransomware leak sites (figure 2). And CTU researchers are investigating whether there is a general trend in the size of those victim organizations reducing over time. Smaller organizations are likely to be less well resourced, making them a softer target and one that is less likely to bring in specialist incident response services after the event. And some ransomware gangs may have decided that hitting higher numbers of smaller organizations is less likely to provoke a strong law enforcement response than hitting large, global brands. Unfortunately, smaller organizations may also be less familiar with the mechanism for reporting to and accessing support from law enforcement and specialist security vendors, meaning that the true impact of ransomware will continue to be under reported and victims will not receive the support they need.

Regardless of the overall trend, for any individual organization ransomware remains a major threat and one that feeds on gaps in security control frameworks. Examination of Secureworks threat research and incident response data provides insights into the tactics of individual threat groups and highlights lessons that can help organizations better protect themselves.

**Figure 1.** Key developments in the ransomware landscape, June 2021 - June 2022. (Source: Secureworks)
*Image Description: A timeline graphic showing key events in the ransomware landscape from May 2021 to June 2022. The timeline includes events such as DarkSide affiliate ransomware attacks on Colonial Pipeline, DOJ indictments, the resurrection of Emotet, the shutdown of REvil, the recovery of Colonial Pipeline ransom, DarkSide rebranding as BlackMatter, Conti playbook leaks, the abandonment of TrickBot, the brief return of REvil, the Kaseya ransomware attack, Conti leaks, the shutdown of the Conti operation, and law enforcement takedowns of Raid Forums and Hydra Market.*

**Figure 2.** Publicly listed ransomware victims by month. (Source: Secureworks)
*Image Description: A line graph showing the number of publicly listed ransomware victims per month from January 2021 to June 2022. The graph shows fluctuations in the number of victims, with no clear trend of reduction over time.*

### The Window of Opportunity for Network Defenders
During any network intrusion, there is a window of opportunity for defenders. This happens between the point of initial access and the encryption of data when the threat actors are consolidating their access prior to achieving their ultimate objective. So far in 2022, the median time between initial access and ransomware detonation in intrusions investigated by Secureworks incident responders is 4.5 days, compared to 5 days in 2021. The mean dwell time in 2021 was 22 days but so far in 2022 is down at 11 days, reflecting that there have been fewer 'outliers' compared to 2021, i.e. intrusions where threat actors spent weeks or months in an environment before deploying their ransomware.

Of course, this dwell time can vary significantly. In early 2022, an organization exposed a computer in an operational technology (OT) environment to the internet with the firewall disabled to troubleshoot network connectivity issues and download patches. Within five hours the computer had been compromised and within a further hour, the threat actors had disabled Windows Defender and deployed Phobos ransomware. While only a small number of devices were affected and the network was isolated from the rest of the organization, the intrusion was sufficient to temporarily disrupt business operations at that location.

In contrast, analysis of a Lorenz ransomware attack in September 2021 showed that the threat actors, tracked by CTU researchers as GOLD LOUNGE<sup>3</sup>, had access for almost a year. The initial intrusion likely occurred in October 2020, with GOLD LOUNGE periodically re-accessing the compromised environment to run reconnaissance commands, occasionally rotating the remote IP address they connected in from. They made extensive use of SMBExec to move laterally to other hosts within the environment. In September 2021, GOLD LOUNGE staged Lorenz ransomware in the SYSVOL directory of several compromised domain controllers and created scheduled tasks with random names on target systems to download and execute the ransomware. They then deleted volume shadow copies and cleared the security event log. One hypothesis to explain this lengthy delay is that GOLD LOUNGE purchased access from an initial access broker (IAB) long after the IAB first obtained it.

Regardless of the length of the detection window, network defenders can and should exploit it. On numerous occasions, Taegis XDR countermeasures have alerted customers to ransomware precursors in their environment, allowing them to isolate impacted hosts, block the command-and-control infrastructure, and reset compromised credentials before the threat actors can capitalize on the access. The difference in terms of time to recovery, total costs incurred and business disruption, compared to organizations who did not spot the threat in time, can be huge.

>Average (median) dwell time for ransomware actors
>
>4.5 Days

### Prevent Where You Can, and Detect What Can’t Be Prevented
Undoubtedly, the best way to protect your organization against ransomware deployment is to prevent or detect the initial breach.

This requires a tight focus on good, basic security hygiene.
*   Ensure that all external and key internal systems are protected with multi-factor authentication (see chapter 5 for tips on avoiding pitfalls).
*   Implement a timely vulnerability detection and patching program (see more about vulnerabilities in chapter 3).
*   For those situations where prevention fails, visibility of the environment is critical. You can't protect what you can't see. Trying to develop that visibility after you've identified a breach is too late.
*   Deploy a comprehensive monitoring and detection solution on all endpoints, network, and cloud (see the appendix for important monitoring considerations).

**Figure 3.** Initial access vectors for ransomware incidents, June 2021 - June 2022. (Source: Secureworks)
*Image Description: A pie chart showing the distribution of initial access vectors for ransomware incidents between June 2021 and June 2022. The chart shows that exploitation of remote services accounts for 52% of initial access vectors, followed by credentials at 39%, commodity malware infection at 3%, drive-by download at 2%, phishing at 2%, and network misconfiguration at 2%.*

### New Players, Old Players
During the reporting period new ransomware groups appeared, many only briefly or with little impact, while others apparently disappeared. In some cases, this fluctuation represented a rebrand by established ransomware groups, possibly to minimize law enforcement and media scrutiny, and in some cases to disguise their identity in response to financial sanctions. In others, it may have been a result of the shifting allegiance of affiliates in the hunt for more victims and greater revenues.

**Figure 4.** Major ransomware schemes active during the period, showing number of victims per month. (Source: Secureworks)
*Image Description: A table showing the number of victims per month for various ransomware schemes from July 2021 to June 2022. The table includes ransomware groups such as LockBit, Conti, BlackCat/ALPHV, Hive, AvosLocker, Vice Society, Grief, BlackByte, Black Basta, Lorenz, and REvil, and shows the total number of victims for each group over the period.*

### Law Enforcement Actions
Over the reporting period, there have been several significant law enforcement actions or sanctions aimed at disrupting ransomware operators or their access to supporting services such as cryptocurrency money laundering.
*   U.S. Treasury OFAC sanctions<sup>4</sup> in December 2019 targeting GOLD DRAKE<sup>5</sup>, also known as Evil Corp, have led to the threat group repeatedly changing ransomware variants to complicate attribution of their attacks back to them, so that victims do not find themselves prohibited from paying the ransom. During the reporting period, they switched between several ransomware families including WastedLocker, Macaw, and potentially also LockBit<sup>6</sup>.
*   In April 2022, OFAC sanctioned Hydra Market (Hydra), the world's largest darknet market. OFAC identified that approximately $8 million in ransomware proceeds had been laundered through it. It also sanctioned Garantex, a virtual currency exchange registered in Estonia thought to have processed transactions worth nearly $6 million from GOLD ULRICK's Conti operation.
*   In May, OFAC sanctioned virtual currency mixer<sup>7</sup> Blender.io (Blender), which had allegedly obscured transactions for Russian cybercrime groups including GOLD ULRICK and GOLD BLACKBURN<sup>8</sup>, and for North Korean threat actors.
*   Also in May<sup>9</sup>, the U.S. State Department offered a financial reward for information leading to the arrest of senior members of the Conti ransomware operator.

Legal action aimed at ransomware actors over the period included the Department of Justice's partial seizure from a Darkside affiliate of the ransom paid by Colonial Pipeline; the multi-country operation that took control of REvil servers in October, forcing them offline, and operator GOLD SOUTHFIELD into hibernation; and the arrest in Russia of individuals associated with the REvil ransomware-as-a-service (RaaS) operation in January.

Action aimed at supporting services included the U.S. Department of Justice unveiling<sup>10</sup> an indictment filed in 2020 against Latvian national Alla Witte for her role as a malware developer in the operation of TrickBot. Chats contained in the Conti Leaks<sup>11</sup> showed GOLD BLACKBURN allocating funds for finding a lawyer to represent Witte. RaidForums, used to sell databases containing billions of card and banking details, as well as login credentials, also closed in April, as the result of Operation TOURNIQUET<sup>12</sup>, a complex law enforcement effort coordinated by Europol. The site was closed, its infrastructure seized, and its administrator and his accomplices arrested.

The long-term impact of increased law enforcement activity against ransomware operators remains difficult to judge. The process of having to re-brand undoubtedly introduces cost for ransomware actors, including potentially through the loss of affiliates to other RaaS schemes. And many victims do hesitate to pay ransoms to sanctioned groups. However, ransomware groups have shown an ability to recover from disruptive interventions and identify alternative means of sustaining their operations. The lack of cooperation from countries where core members of the prominent ransomware groups reside continues to hamper disruption efforts.

GOLD MYSTIC's<sup>13</sup> LockBit RaaS was the most active name-and-shame operation, listing 875 victims on its public leak site by the end of June 2022. Secureworks incident responders have responded to LockBit intrusions against organizations in the technology, business services, media, finance, and legal sectors across the Middle East, Europe, the U.S., Asia, and Australia. GOLD MYSTIC appears to have been highly effective at recruiting affiliates from other RaaS schemes, and in at least one case CTU researchers were able to link a July 2021 LockBit incident to a June 2021 REvil incident, assessing with moderate confidence that the same affiliate was responsible for both incidents as well as for an earlier January 2021 incident reported<sup>14</sup> by Ahnlab.

### The (Non) Return of REvil
On April 19, 2022, CTU researchers observed two dormant Tor sites associated with REvil become active again. Both sites were redirecting to a new Tor site that appeared to be a revamp of the original REvil leak site. The new leak site retained the original list of victims, as well as three new victims. This was odd, given that GOLD SOUTHFIELD<sup>15</sup> initially went offline shortly after the Kaseya attack<sup>16</sup> that occurred over Independence Day weekend in July 2021 and then was forced offline permanently by a collaborative law enforcement<sup>17</sup> effort in October.

Naturally, the use of the same Tor infrastructure and REvil source code caused speculation about whether REvil was back, despite the reported<sup>18</sup> arrest of members of the group by the Russian FSB in January 2022. But in spite of these early signs of a resurgence, REvil is yet to reach its former level of activity.

Intriguingly, CTU researchers identified<sup>19</sup> REvil samples compiled in March at a time when, according to the Russian authorities, members of the group were still in custody<sup>20</sup>. This could indicate that the individuals had been quietly released prior to that point, or perhaps the arrests were of fringe members and had no real impact on the group's operational capabilities. The timing also coincides with the breakdown of cooperation between Russia and the U.S. on cybercrime.

>### The Perils of Timestamps— Can They Be Trusted?
>Analysis of REvil's resurgence relied in part on analysis of compilation timestamps. Compilation timestamps show when a file, in this case a REvil ransomware binary, was created and can be useful for building a timeline of threat actor activity. But they can, and often are, falsified by threat actors. Threat intelligence analysts need to be careful in relying on them. CTU researchers have been tracking GOLD SOUTHFIELD since 2019 and have processed thousands of REvil samples. Whenever a new version of REvil has appeared, the compilation timestamp for the executable aligns with what is expected of a new release. Compilation timestamps also align for samples across multiple different campaigns. Therefore, while compilation timestamps should generally be treated cautiously, in this case they are a useful data point.

### ALPHV Works Cross-Platform
It is increasingly common for ransomware groups to compile ransomware that can be deployed across multiple operating systems. One example is GOLD BLAZER's<sup>21</sup> ALPHV ransomware, also known as BlackCat, which emerged in December 2021. Based on insights from multiple ALPHV intrusions worked by Secureworks incident responders, the operators move from initial infection to data exfiltration within a few days, to deploying ransomware within approximately one week. In one incident, GOLD BLAZER or one of its affiliates abused a single-factor authentication Virtual Private Network (VPN) for the initial infection vector. After compromising the device, the threat actors conducted reconnaissance and used Mimikatz to harvest credentials. Using these stolen credentials, the threat actors logged into domain administrator accounts and used the access to stage, compress, and exfiltrate files.

ALPHV is written in Rust, making the ransomware scalable across Windows and Linux operating systems without needing to maintain distinct codebases. Its configuration file (figure 5) includes options to terminate ESXi 'vm' and 'vm snapshot' files. The hybrid approach of listing Linux and Windows file extensions is unusual.

**Figure 5.** ALPHV configuration file. (Source: Secureworks)
*Image Description: A code snippet showing a portion of an ALPHV configuration file. The snippet includes various file extensions associated with both Windows and Linux operating systems, as well as options for terminating ESXi virtual machine files and snapshots.*

### Hive Proves Effective at Attracting Affiliates
Hive is another ransomware that has featured heavily in incident response engagements worked by Secureworks during the period. The operators of the Hive RaaS, GOLD HAWTHORNE<sup>22</sup>, have been active since at least June 2021.

Since April 2022, CTU researchers have attributed a series of Hive-related intrusions to a single affiliate, GOLD MATADOR<sup>23</sup>. GOLD MATADOR gains access to networks through VPN or Remote Desktop Protocol (RDP) servers using compromised credentials. After conducting reconnaissance to enumerate domains and harvest credentials using tools like PCHunter64, SharpView and Mimikatz, the group moves laterally using RDP with stolen credentials. The SystemBC proxy tool is used to disguise network traffic and Cobalt Strike Beacon is installed across number hosts for command and control. The group explores directories and views specific files before using FileZilla for data exfiltration and then ultimately deploying the Hive ransomware via Group Policy Object or Scheduled Task (figure 6).

**Figure 6.** Scheduled Task (veeamupdate) used by GOLD MATADOR to detonate Hive ransomware. (Source: Secureworks)
*Image Description: A screenshot showing the details of a scheduled task named "veeamupdate" used by GOLD MATADOR to execute the Hive ransomware. The task is configured to run a PowerShell command that downloads and executes the ransomware.*

### Experimentation With Hack and Leak Continues
The Secureworks 2021 State of the Threat report highlighted hack and leak incidents (where no ransomware was deployed) as a potential shift away from the traditional ransomware-based extortion model. It remains unclear whether this approach provides a viable long-term business model, but some groups such as GOLD TOMAHAWK<sup>24</sup> continue to practice it. Also known as Karakurt Team or Karakurt Lair, GOLD TOMAHAWK has been active since mid-2021.

GOLD TOMAHAWK intrusions typically start with access through internet-facing VPN endpoints, likely leveraging vulnerabilities or weak or stolen credentials. Once inside the network, GOLD TOMAHAWK does not deploy custom tooling, relying instead on off-the-shelf tools and applications, often native to the victim system, to meet its objectives. The threat group has been observed to use RDP for lateral movement, AnyDesk for remote access, 7-Zip to compress data for extraction, and the Mega and QuickPacket file-upload services for exfiltration.

Another hack and leak actor that emerged during the period is the GOLD RAINFOREST<sup>25</sup> (Lapsus$) threat group, who claimed responsibility for several high-profile breaches including against Microsoft, Samsung and Nvidia. Identified members of GOLD RAINFOREST don’t match the typical stereotype of Russian-organized cybercriminals. But the success they were able to achieve in a short space of time is a cautionary tale about the importance of understanding how easy it can be for threat actors with a moderate level of capability and, critically, a means of accessing an organization's network to carry out attacks.

**Figure 7.** GOLD TOMAHAWK (Karakurt) leak site screenshot. (Source: Secureworks)
*Image Description: A screenshot of the GOLD TOMAHAWK (Karakurt) leak site. The site displays a list of organizations that have been targeted, along with some of their data.*

## Ransomware Enablers: Loaders and Infostealers
Malware distribution forms a key component of the broad infrastructure that both supports and fuels the ransomware ecosystem. Delivery techniques continue to evolve, and the relationship between established ransomware operators and malware distribution operators remains a close one.

### Now You See Them, Now You Don't
Between July 2021 and June 2022, two big names in the loader landscape disappeared and two returned, demonstrating that writing off botnets and their associated malware, even after periods of inactivity, can be premature.

Emotet returned in November 2021, following its January 2021 takedown by international law enforcement agencies. During this downtime, its developers, tracked as the GOLD CRESTWOOD<sup>26</sup> threat group, had made some changes. The Emotet code appeared enhanced and streamlined, with more modern cryptography, different communications protocols, a switch to 64-bit architecture, more customizable execution options, and new command and control (C2) infrastructure. CTU researchers also observed evidence of GOLD CRESTWOOD experimenting with re-implementing deprecated functionality such as modules to steal credit card information from web browsers and self-propagation<sup>27</sup> using SMB and a list of hardcoded credentials.

Conti operator GOLD ULRICK was likely instrumental<sup>28</sup> in Emotet’s return, and the Conti Leaks provided evidence of the close relationship between the ransomware group and GOLD CRESTWOOD. Emotet reappeared as a DLL download from TrickBot, suggesting that GOLD CRESTWOOD aimed to rebuild the Emotet botnet by using long-time collaborator GOLD BLACKBURN's TrickBot infrastructure. Emotet was also distributed through malicious Windows App Installer packages disguised as Adobe PDF software, much like GOLD BLACKBURN's BazarBackdoor malware. In January 2022, CTU researchers observed Emotet executing reconnaissance commands (see figure 8) replacing functionality that was previously provided by intermediate payloads Qakbot and TrickBot.

**Figure 8.** Emotet executing reconnaissance commands and credential-theft tools. (Source: Secureworks)
*Image Description: A screenshot showing the command line activity of Emotet executing reconnaissance commands and credential-theft tools. The commands include "net user", "tasklist", "systeminfo", and "whoami".*

In March, Emotet resumed dropping Qakbot, using the 'azd' Qakbot campaign ID which likely refers to a GOLD LAGOON<sup>29</sup> affiliate. Qakbot had itself taken a two-month hiatus in 2021, reappearing on September 9, 2021. During the break, Qakbot's backend infrastructure was for the first time switched off rather than left to idle, leading the security community to question if the hiatus could be permanent. Since its return, Qakbot has resumed its role as a major player in the loader landscape.

On October 18, CTU researchers observed Qakbot deploying a new plugin containing the legitimate Atera remote management and monitoring (RMM) software to all infected devices (figure 9).

The TrickBot botnet stopped responding to infected systems on March 1, 2022, after a progressive decrease since mid-2021 in the tempo of updates to TrickBot-infected hosts via its C2 infrastructure. There were no signs of it returning to life by August, and it seems likely that the group intends to permanently abandon it.

**Figure 9.** msiexec.exe launching the Windows installer file that installs the Atera RMM software. (Source: Secureworks)
*Image Description: A screenshot showing the execution of msiexec.exe, which is launching a Windows installer file to install the Atera RMM software. This indicates that Qakbot is using the Atera RMM software as a plugin.*

**Figure 10.** Timeline of TrickBot activity from July 2021 through March 2022. (Source: Secureworks)
*Image Description: A timeline graphic showing the activity of TrickBot from July 2021 to March 2022. The timeline includes events such as the last C2 server update to a botnet segment, the disabling of web injects, the last observed TrickBot spam campaign, the start of Conti data leaks, the last plugin update, the start of C2 infrastructure going offline, and the complete disabling of C2 infrastructure.*

The Conti Leaks may shed some light on the decision to abandon TrickBot, as they include conversations about TrickBot's declining utility and BazarLoader's increasing maturity. In a sign of the speed with which the threat landscape can change, by April 2022 a new loader called Bumblebee was being used in Conti and Diavol ransomware attacks in preference to BazarLoader. However, TrickBot's design means GOLD BLACKBURN retains the capability to re-enable the C2 infrastructure and recapture existing bots if the group chooses to.

There were lulls in IcedID activity between July and November 2021, and between February and May 2022, but activity levels have continued to increase since May 2022. In 2021 the operators of IcedID, GOLD SWATHMORE<sup>30</sup>, reworked the malware’s networking functionality to include Base64-encoded information about the victim system in the HTTP Cookie and Authorization header (figure 11).

Distribution for IcedID also changed during 2021, to distribute ISO files containing Windows shortcut (LNK) files that execute a colocated DLL file containing the IcedID payload. In a March 2022 intrusion, an attacker compromised an internet-facing Microsoft Exchange Server via the ProxyShell vulnerability and used access to the compromised server to send internal phishing emails containing hijacked email threads and an attached IcedID payload. This technique of using compromised email servers to send internal phishing emails is likely an effort to ensure that emails appear to come from a trusted sender, bypassing security controls that warn users by tagging emails that originate externally.

**Figure 11.** IcedID HTTP POST request with encoded victim information. (Source: Secureworks)
*Image Description: A code snippet showing an IcedID HTTP POST request. The request includes encoded victim information in the Cookie and Authorization headers.*

**Figure 12.** Taegis XDR detection for IcedID malware. (Source: Secureworks)
*Image Description: A screenshot of the Taegis XDR platform showing a detection for IcedID malware. The detection highlights the process and command line activity associated with the malware.*

### New on the Scene
There have been a number of new loaders that have emerged during the reporting period, and in some cases disappeared again. CTU researchers assess that the groups operating these loaders may move away from the complex, fully-featured botnets that evolved from the early banking trojans towards more lightweight loaders that are easier to develop and maintain. That shift is likely enabled by increased use of fully featured and actively maintained post-exploitation tools such as Cobalt Strike. The role of the loader is simply to achieve an initial access point, perhaps perform some basic reconnaissance such as checking that the infected host is joined to an Active Directory domain, and then retrieve and execute the post-exploitation tool.

#### Bumblebee
CTU researchers' analysis of Bumblebee reveals rapid development and numerous active campaigns. Multiple threat actors now appear to have moved to using Bumblebee to drop payloads that include Cobalt Strike, Sliver<sup>31</sup>, and Meterpreter in order to deliver ransomware.

#### PureCrypter
PureCrypter is a fully featured malware builder and loader advertised for sale since March 2021 at $59 USD for one month and $249 for lifetime use. It is a .NET executable obfuscated with SmartAssembly. It is widely used to drop payloads for cybercriminal ends. In addition, CTU researchers assess with moderate confidence that the developers of the WhisperGate<sup>32</sup> file wiper that was deployed against targets in Ukraine prior to the Russian invasion used PureCrypter to generate the .NET code in both the loader and the initial payload.

**Figure 13.** PureCrypt and associated tool pricing at https://purecoder.sellix.io/ (Source: Secureworks)
*Image Description: A screenshot of the PureCrypter website showing the pricing for the tool, with options for one month and lifetime use.*

#### SquirrelWaffle
SquirrelWaffle loader was first detected in September 2021, delivering Qakbot and Cobalt Strike. Initially, some third-party commentators characterized it as an heir to Qakbot, Emotet, or IcedID. However, by early November, SquirrelWaffle's infrastructure had been disabled and the loader was not observed again in active distribution. CTU researchers saw only a small number of SquirrelWaffle infections across customer environments (figure 14).

**Figure 14.** iSensor IDS detection for SquirrelWaffle HTTP POST request that uses padding and a hardcoded XOR key. (Source: Secureworks)
*Image Description: A screenshot of an iSensor IDS detection for a SquirrelWaffle HTTP POST request. The detection highlights the use of padding and a hardcoded XOR key in the request.*

### Bringing the Victim to You: Drive-By-Download as an Alternative Distribution Method
'Drive-by-downloads' continue to be a popular alternative to phishing-based malware distribution. Notable examples include the prolific SocGholish malware framework, operated by GOLD PRELUDE<sup>33</sup>, and the Gootloader JavaScript-based loader distributed by the GOLD ZODIAC<sup>34</sup> threat group. A user visits a compromised website that triages the visitor and serves up a series of redirects that ultimately deliver malware.

GOLD ZODIAC uses search engine optimization (SEO) poisoning, layers of public blog posts, and a complex array of compromised WordPress sites to drive high-ranking Google search results to deliver Gootloader. Professionals who visit these infected sites to download model legal agreements or other documents are tricked into downloading GootLoader, leading to the download of Cobalt Strike as a precursor to ransomware.

**Figure 15.** Gootloader process flow. (Source: Secureworks)
*Image Description: A flowchart illustrating the process flow of Gootloader. The flow starts with a user following a poisoned Google search result to a compromised WordPress site. The site checks the user's browser and visit history, and if valid, presents a Q&A forum page with a download link. The download link redirects through compromised sites to deliver a .zip file containing the Gootloader JavaScript loader. The loader creates a scheduled task for persistence, stuffs registry keys with encoded payloads, and sends system information to a C2 server. If the machine is Active Directory joined, the C2 server returns a payload and moves to the next stage of the infection.*

**Figure 16.** Compromised WordPress site. (Source: Secureworks)
*Image Description: A screenshot of a compromised WordPress site used by GOLD ZODIAC to distribute Gootloader. The site appears to be a legitimate forum but is actually serving malicious content.*

### Infostealers: A Thriving Market
Loaders are one way of gaining access to an environment. Another is using credentials obtained by infostealers, or 'stealers'. Analysis of the sale of 'logs' (collections of stolen data) on underground forums shows that stealers are becoming increasingly popular. On a single day in June 2022, over two million logs were offered for sale on a single underground forum (figure 17).

The three main stealer markets are:
*   Genesis Market
*   Russian Market—likely tied to the now defunct Amigos market
*   2easy—claims to be the largest stealer market, but Russian Market and Genesis appear to host more logs.

**Figure 17.** Logs from popular stealers for sale on Russian Market underground forum on June 2, 2022. (Source: Secureworks)
*Image Description: A bar chart showing the number of logs from different infostealers for sale on the Russian Market underground forum on June 2, 2022. The chart shows that RedLine logs are the most numerous, followed by Vidar, Raccoon, Taurus, and Azorult. The total count of logs is also displayed.*

#### Genesis
Active since 2018, Genesis is an online marketplace for stolen account data, offering custom bot software that allows customers to clone their victims' browsers, including cookies, usernames, and passwords. When a criminal buys an identity on the market, they buy access to the bot on the victim's computer, making it easy to hijack victims' online accounts. Access to the site, which operates on the dark web and the open internet, is via invitation. It is possible to search the logs by bot name, location, or domain.

#### Russian Market
Considered to be the largest active stealer market, Russian Market sells logs from multiple vendors. It is possible to search by stealer