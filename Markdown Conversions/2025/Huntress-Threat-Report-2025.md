# 2025 Cyber Threat Report

## Table of Contents
- [Executive Summary](#executive-summary)
- [The 2024 Threat Landscape](#the-2024-threat-landscape)
- [Attack Breakdown by Industry](#attack-breakdown-by-industry)
- [Healthcare Sector Threats](#healthcare-sector-threats)
- [Technology Sector Threats](#technology-sector-threats)
- [Education Sector Threats](#education-sector-threats)
- [Government Sector Threats](#government-sector-threats)
- [Manufacturing Sector Threats](#manufacturing-sector-threats)
- [Ransomware In 2024](#ransomware-in-2024)
- [Ransomware Groups](#ransomware-groups)
- [Time-To-Ransom (TTR) Measurement](#time-to-ransom-ttr-measurement)
- [Activity Before Ransom](#activity-before-ransom)
- [Attacker Tools and Techniques](#attacker-tools-and-techniques)
- [Hacking Tools](#hacking-tools)
- [Remote Access Trojans](#remote-access-trojans)
- [RMM Abuse](#rmm-abuse)
- [Exploit-Driven Campaigns in 2024](#exploit-driven-campaigns-in-2024)
- [ScreenConnect Exploitation (CVE-2024-1709 & CVE-2024-1708)](#screenconnect-exploitation-cve-2024-1709--cve-2024-1708)
- [CrushFTP Exploitation (CVE-2024-4040)](#crushftp-exploitation-cve-2024-4040)
- [ProxyShell Exchange Exploitation (CVE-2021-31207)](#proxyshell-exchange-exploitation-cve-2021-31207)
- [MITRE ATT&CK Phases](#mitre-attck-phases)
- [Scripting Abuse](#scripting-abuse)
- [Persistence Mechanisms](#persistence-mechanisms)
- [Credential Access](#credential-access)
- [Defense Evasion](#defense-evasion)
- [Security Bypasses](#security-bypasses)
- [Third-Party EDR Coverage](#third-party-edr-coverage)
- [Breaking Down Hacker Activity](#breaking-down-hacker-activity)
- [Operational Timeframes](#operational-timeframes)
- [Identity Threats](#identity-threats)
- [Inbox Rule Modifications](#inbox-rule-modifications)
- [Token Theft](#token-theft)
- [Credential Theft](#credential-theft)
- [VPN and Proxy Abuse](#vpn-and-proxy-abuse)
- [Phishing Activity in 2024](#phishing-activity-in-2024)
- [Voicemail Luring](#voicemail-luring)
- [E-Signature Impersonation](#e-signature-impersonation)
- [Image-Based Content](#image-based-content)
- [QR Codes](#qr-codes)
- [Fake “Threads” / Reply Chains](#fake-threads--reply-chains)
- [Living Off Trusted Sites (LoTS)](#living-off-trusted-sites-lots)
- [Impersonated Brands](#impersonated-brands)
- [Conclusions](#conclusions)

## Executive Summary
Last year, threat actors were prolific. They showed remarkable adaptability and used more sophisticated tools, tactics, and techniques across industries like healthcare, technology, education, government, and manufacturing. The gap between sophistication in attacks on large enterprises and smaller businesses has narrowed—in fact, it’s all but disappeared. Attackers are taking the methods and strategies they’ve tested on larger organizations and are standardizing them across businesses of all sizes to maximize efficiency. Advanced methods like defense tampering, bring your own vulnerable driver (BYOVD) privilege escalations, and UAC (User Account Control) bypasses have become the norm, underscoring the urgent need for comprehensive defenses, proactive patching, and enhanced endpoint monitoring.

This report gives a detailed analysis of key adversarial behaviors, techniques, and trends we saw in 2024, highlighting the escalating risks that non-enterprise businesses and managed service providers (MSPs) need to be aware of. This analysis will empower organizations of all sizes to strengthen their defenses against modern cyber threats by giving them actionable insights into a constantly evolving threat landscape.

Recent takedowns of ransomware groups like Hive, Dharma/Crysis, Phobos, and the partial disruption of LockBit have fragmented ransomware groups into smaller, more agile affiliate networks like RansomHub and INC/Lynx. These affiliates have attracted hackers by offering significantly higher payouts, often reaching 80–90% of the ransom paid out. Meanwhile, ransomware strategies are shifting as detection improves, with groups like BianLian focusing on data theft and extortion rather than data encryption. We believe this strategy will continue to evolve, highlighting the value of data loss prevention, network monitoring, and awareness.

Abuse of remote access trojans and RMMs (e.g., AsyncRAT, Jupyter, NetSupport, and Trickbot), administrator tools like SysInternals Suite, and LOLBins like rdrleakdiag or netsh were still widespread in 2024. Scripting languages like PowerShell, VBScript, and JavaScript were heavily exploited for malicious code execution, persistence, and lateral movement. While comprehensive hacking tool suites like Cobalt Strike saw a decline in use, specialized tools like Mimikatz and CrackMapExec continued to be abused globally. Additionally, opportunistic exploitation of software vulnerabilities and the abuse of remote monitoring and management (RMM) tools emerged as critical risks, which helped attackers compromise large numbers of machines in a short time.

## The 2024 Threat Landscape
In 2024, cybercriminals leveled up their game, using smarter tactics and turning everyday tools into weapons. Drawing from extensive monitoring of thousands of organizations and millions of endpoints, we’ve identified several critical trends that shaped the cybersecurity environment in 2024 and will carry into 2025:

- **Proliferation of Remote Access Trojans (RATs)**
  Over three-quarters of remote access incidents involved RATs like AsyncRAT, NetSupport, and Jupyter. Similar to Jupyter, many tools will likely change from an infostealer to a multi-stage backdoor with advanced capabilities as the need for these tools keeps growing. As the malware market gets more competitive, we’ll see them adapt, forcing developers to add more complex features into malware. This emphasizes the need for layered defenses that EDR provides in order to provide protection for even trivial infections. System administrators and IT professionals need to be extra vigilant as attackers can infiltrate and move faster than ever, with the window from initial compromise to data theft or ransomware delivery getting shorter and shorter.

- **Shifts in Ransomware Strategies**
  A focus on data theft and extortion over encryption emerged, as groups like BianLian, RansomHub, and Akira targeted businesses with high affiliate payouts. These high payouts drove more ransomware actors to use their ransomware. Time will tell if ransomware operators move into extortion (or double extortion) schemes more: this is the result of success from EDR and ransomware protection services as well as pressure from government takedown services. While these defenses have thrived, data loss prevention (DLP) services have hardly made any advances and are often only installed in mature corporate environments. Attackers are becoming more aware of these circumstances and are opting to steal data and hold it for ransom.

- **Sophisticated Use of “Living Off the Land” Techniques**
  Adversaries relied more and more on legitimate administrative tools like Sysinternals Suite and LOLBins for evasion and persistence and relied less on malicious executables. LOLBins and all of their related sub-categories have long been a strategy used by attackers, even before they were named. This trend will only grow, as their misuse often requires complex defenses in place to determine valid vs invalid scenarios in most circumstances. Reducing attack surface by identifying which LOLBins are available on systems and removing these software components adds an extra step for attackers that could help identify them before system compromise. Adapting execution policies to include only what’s needed also is a successful strategy against these attacks.

- **Rising Phishing Sophistication**
  Techniques like QR code phishing, image-based content, and brand impersonation exploited user trust and bypassed traditional email filters. With phishing still a primary means of initial access and reconnaissance, attackers’ efforts will continue to become more advanced. These methods will likely attempt more secondary device targeting like scanning with phones or include methods to target users personally in order to steal credentials. Malicious frameworks are being successfully developed that only require an attacker to input a name and an email address. The system then crawls social media and finds systems to determine a user’s interests and custom delivers a phishing email to the victim.

- **Increased Exploitation of Remote Monitoring and Management (RMM) Tools**
  Attackers abused RMM tools like ConnectWise ScreenConnect, TeamViewer, and LogMeIn to gain access, move laterally, and maintain persistence. Attackers have learned that these trusted applications let them blend in and stealthily infiltrate and move laterally within compromised networks. Increased vigilance, enhanced access controls, and monitoring of RMM tools are highly suggested for environments that use them.

While the 2024 cybersecurity landscape was marked by rapid changes in attacker strategies and types, we set out to identify which methods were most prevalent.  
![Image description: Figure 1: Most common threat categories throughout 2024. A pie chart showing the frequency of threats overall. Infostealer: 24%, Malicious Script: 22%, Malware: 17%, RAT: 13%, Ransomware: 9.5%, RMM Abuse: 6.5%, Lateral Movement: 4%, Hacking Tool: 4%.]

Infostealers represented nearly a quarter (24%) of all observed incidents, highlighting attackers’ focus on harvesting credentials, financial information, and sensitive data. Malicious scripts were a close second at 22% of incidents, demonstrating their utility for attackers aiming to evade detection and automate their exploits.

These trends indicate that attackers are not only refining their techniques but also doubling down on approaches that yield the most success. The prevalence of infostealers and malicious scripts shows a shift toward tactics that prioritize speed and scale. Meanwhile, the persistence of malware and ransomware underlines the need for robust defenses at every stage of the attack chain.

To better understand these trends, Huntress did a year-long analysis to track changes and fluctuations in threat types and techniques and honed in on emerging threats and shifts in attacker methodologies. Our findings underscore the need for proactive defenses and adaptive strategies.

## Attack Breakdown By Industry
Attackers targeted a wide range of industries throughout 2024, with healthcare and education being targeted the most, followed by significant activity against technology, manufacturing, and government sectors.

We saw hackers focusing many of their attacks on healthcare and educational facilities, with these two industries making up 38% of all incidents observed last year. Attacks on technology companies, manufacturing, and government made up almost a third of all incidents we observed.

![Image description: Figure 2: Industries targeted by percentage in 2024. A pie chart showing the industries targeted. Education: 21%, Healthcare: 17%, Technology: 12%, Government: 11%, Manufacturing: 9%, Other: 30%.]

Each industry faced distinct threats, with malicious scripts, remote access trojan (RAT) deployments, and abuse of remote monitoring and management (RMM) tools as recurring attack methods.

Healthcare environments were particularly vulnerable to script-based attacks and exploitation of legacy systems. The technology and education sectors saw heightened risks from credential theft, lateral movement via RMM tools, and malicious updates disguised as legitimate software. Government entities were targeted with information-stealing malware, RATs, and advanced hacking tools, highlighting the persistent and varied tactics employed by attackers across industries. Ransomware was a consistent threat across all industries in 2024. With cryptocurrency prices skyrocketing later in the year, attackers were more brazen with their attacks, even against non-enterprise environments. These findings mean that businesses of all sizes need tailored defenses and proactive measures to address their industry’s unique vulnerabilities.

![Image description: Figure 3: Threat frequency by industry in 2024. A bar graph showing threats by industry. Healthcare, Technology, Education, Government, Manufacturing, and Other are listed on the x-axis. Infostealer, RAT, Ransomware, Malware, Hacking Tool, RMM Abuse, Malicious Script, and Lateral Movement are listed as different colored bars for each industry.]

![Image description: Figure 3: Threat frequency by industry in 2024. A bar graph showing threats by industry. Healthcare, Technology, Education, Government, Manufacturing, and Other are listed on the x-axis. Infostealer, RAT, Ransomware, Malware, Hacking Tool, RMM Abuse, Malicious Script, and Lateral Movement are listed as different colored bars for each industry.]

## Healthcare Sector Threats
In healthcare, the biggest risk throughout the industry in 2024 was malicious script executions. These were primarily scripts being abused for persistence like Javascript components of malware, downloaders, and system analysis components used before gathering additional components. Because Huntress intercepted many of these malicious scripts before they could run, we weren’t able to positively associate many of these scripts with their appropriate malware family. That said, most of these appear to be related to infostealers like Gootloader as well as PowerShell components being abused for obfuscation or anti-analysis like Windows Event Log modifications or searching. Malicious scripts would often query the Windows Registry to gather data for exfiltration, or make modifications to it such as changing COM object values to establish persistence. After these, the second-most frequent script goal was download components originating from PowerShell or WScript components. Many of these downloaders tried to get other malware components, while a few of these were attempting to download packages installing RATs.

While there don’t appear to be any RAT tools specifically geared towards healthcare, many of them look to be using Java-based technology. While many environments have removed the use of Java, the healthcare industry still depends on Java applications and development for many medical usage technologies and software suites. Attackers seem to know this and are taking advantage of these overlooked areas, deploying JRat/Adwind and STRRAT at higher frequencies than other industries. JavaScript-based attacks are also extremely common in healthcare, where suspicious Javascript execution patterns and child process rules were triggered in the majority of incidents. While most of these are generic components of malware, some of these appear to be related to Gootloader or SOCGholish Javascript loaders.

![Image description: Figure 4: Healthcare threats by type in 2024. A pie chart showing the types of threats targeting healthcare. Infostealer: 19%, RAT: 7%, Ransomware: 8%, Malware: 16%, Hacking Tool: 4%, RMM Abuse: 9%, Malicious Script: 22%, Lateral Movement: 4%, Other: 11%.]

Attackers targeting healthcare can easily identify these environments as more than 38% of Hands-On-Keyboard activity involved in this environment was related to network or domain environment analysis or reconnaissance. In many cases, this was the initial hands-on-keyboard activity we saw, as attackers used infostealers or other scripts to identify the domain, then a human attacker would later remotely access the infected machine. Lateral movement in healthcare, when not automated, was often achieved with hacking tools primarily Mimikatz or abusing known LOLBins (ntdsutil, diskshadow, and rdrleakdiag were the most common) to dump memory or NT directory services info tree in order to access cached credentials or hashes.

Ransomware in the healthcare industry looks to be slowly shifting to more data theft and extortion than traditional decryption-based ransoms. This is a trend we’re seeing elsewhere, as attackers are developing these tactics to defeat file encryption protection: a key defense for thwarting traditional ransomware. Throughout 2024, INC/Lynx and RansomHub were the three primary groups that targeted hospitals and other medical services. In many cases, these ransomware deliveries were used in conjunction with threat groups like Vanilla Tempest, who often partnered with INC to deploy their ransomware on victims after they gained access and exfiltrated their primary targeted data.

![Image description: Figure 5: Healthcare hands-on-keyboard activity in 2024. A pie chart showing healthcare hands-on-keyboard activity. Network Enumeration: 38%, Lateral Movement: 22%, Persistence: 11%, Credential Harvesting: 14%, Exfiltration: 7%, Defense Evasion: 6%, Other: 2%.]

## Technology Sector Threats
In the technology sector, we saw attackers shift their strategies to use different tools and mechanisms utilized by employees to blend into networks. Most notable is the abuse of RMM tools to either gain access or move laterally within the network. It appears many of these tech-related environments were using RMM tools to manage employee machines, and attackers implemented several ways to abuse these trusted network applications. We identified several password/memory dumping and keylogging campaigns using Mimikatz, lazagne, or the infostealers Meduza and Strela specifically targeting technology companies, then later using swiped credentials to laterally move to other targets.

While these tools don’t specifically target RMM tools, some infostealers will try to gain access to credential managers to gather stored credentials, which are then used to access other machines. Attackers will then install a persistence mechanism, gather information, dump available credentials, and install logging and monitoring tools to steal other users’ login credentials. This process is then repeated ad nauseam until domain controllers, source code, backup servers, or other critical infrastructure is accessed. At this point, we often see the theft of proprietary data, leveraging existing trust relationships, or ransomware deployment as the three main goals.

Attackers often target third-party tools used to store passwords, such as password managers, but this wasn’t exclusive to the tech industry. These were a major target for attackers using tools and infostealer malware families that can identify and grab credentials. Attackers would often target technology companies as an entry point to migrate into their customers. Most targeted systems handled IT management, consulting, development, and similar tech management for clients. Attackers would use these companies’ access to spread to additional targets.

Another behavior seen in the tech sector was attackers bringing their own IP scanners to identify targets. While this behavior wasn’t exclusive to the tech industry, detection of these third-party network scanners was the highest in the tech and education sectors.

![Image description: Figure 6: Technology threats by type in 2024. A pie chart showing the types of threats targeting technology. Infostealer: 18%, RAT: 9%, Ransomware: 8%, Malware: 14%, Hacking Tool: 6%, RMM Abuse: 14%, Malicious Script: 19%, Lateral Movement: 6%, Other: 6%.]

## Education Sector Threats
Education-based environments face similar threats to the healthcare industry; however, malicious scripts are the most-identified threat detected in these environments. In many scenarios, the goal was the same: persistence or downloading additional components to further the chain of infection in these networks. Unlike in healthcare, PowerShell, VBScript, and WMI abuse were the top threats seen in the education sector, with far fewer Java threats, as opposed to what was seen in healthcare environments.

Similar to the tech sector, we noticed RMM abuse in educational environments at a slightly higher rate. The reason for this was likely similar to tech companies because educational systems rely on these for remote administration, and attackers focused on abusing these to gain access and leverage gaps in security to laterally move across systems. Huntress saw spearphishing attacks disguised as RMM updates and RMM components to be a technique that attackers favored, often trojanizing RMM services or deploying fake RMM software. Attackers could then detect which RMM services many of these victims were using via reconnaissance.

Chromeloader was prevalent across the educational sector, accounting for almost 70% of all infostealers across our partner environments. RAT detections were relatively low due to many RAT loaders being classified as malicious scripts being neutralized before RATs were loaded. A majority of these were NewCoreRAT, HiddenNetSupport, and AsyncRAT as the likely culprits.

![Image description: Figure 7: Education threats by type in 2024. A pie chart showing the types of threats targeting education. Infostealer: 16%, RAT: 6%, Ransomware: 7%, Malware: 13%, Hacking Tool: 3%, RMM Abuse: 13%, Malicious Script: 24%, Lateral Movement: 4%, Other: 14%.]

## Government Sector Threats
Government environments were targeted at high rates in 2024, with most detected attempts being information-stealing components, downloaders/persistence mechanisms, and RATs. SOCGholish, AsyncRAT, and JupiterRAT were popular malware families used to remotely access government targets. NewCoreRAT also showed brief upticks, which coincided when variants of JupiterRAT were less popular.

Most malicious scripts targeting government entities were PowerShell and Javascript components, and both are likely related to SOCGholish and AsyncRAT components attempting persistence or downloading components via BITS or HTTPS.

As for hacking tools, government targets saw an increase of Cobalt Strike and Bloodhound toolkits being used against them more than other industries, but those numbers were far less than LOLBin abuse of PSExec, ntdsutil, and other built-in Windows network management software. Mimikatz and PowerSploit were also used frequently in these environments.

![Image description: Figure 8: Government threats by type in 2024. A pie chart showing the types of threats targeting government. Infostealer: 21%, RAT: 10%, Ransomware: 5%, Malware: 16%, Hacking Tool: 4%, RMM Abuse: 9%, Malicious Script: 18%, Lateral Movement: 8%, Other: 9%.]

![Image description: Extract of a Huntress intrusion where ScreenConnect and Cobalt Strike were leveraged in a county government’s network. Cobalt Strike beacon. ScreenConnect persistence.]

## Manufacturing Sector Threats
The last industry we analyzed was manufacturing, and this was a unique environment based on the data we saw for 2024. We saw a high number of RAT installations in these environments, with AsyncRAT, Trickbot, NetSupport, and NewCoreRAT as the most commonly witnessed families.

Manufacturing companies were under attack by the most evenly distributed list of scripting languages from malicious scripts. PowerShell was still the most common, but WMI, JavaScript, and VBScript were also used. Java-based attacks were also successful against these environments, as attackers were likely able to successfully recon these targets before deploying them.

An interesting trend we noticed was malware disguising themselves as Adobe components, and this type of obfuscation made up 23% of all methods used in this sector. The next-most common method, mimicking Windows or Defender components, was only at 11%.

Outside of typical RMM abuse, attackers were often seeing abusing Windows RDP components in similar manners.  Attackers were witnessed injecting and manipulating RDP components in order to steal credentials, lower security within sessions.

Information theft in this sector also primarily focused on domain passwords, with attackers migrating to higher-priority machines as fast as possible. Attempts to laterally move were almost exclusively done using traditional Windows LOLBins and domain tools such as ADExplorer, WMI, PsExec, and Net.exe.

![Image description: Figure 9: Manufacturing threats by type in 2024. A pie chart showing the types of threats targeting manufacturing. Infostealer: 15%, RAT: 13%, Ransomware: 6%, Malware: 17%, Hacking Tool: 8%, RMM Abuse: 12%, Malicious Script: 15%, Lateral Movement: 6%, Other: 8%.]

## Ransomware In 2024
In late 2023 and early 2024, ransomware operations faced significant disruption due to global collaboration among cybersecurity groups, law enforcement, and private researchers. Notable takedowns and disruptions included LockBit, which splintered into sub-groups like RansomHub, and the dismantling of Dharma/Crysis, Hive, and Phobos, reshaping the ransomware landscape. Groups like BianLian shifted tactics from encryption to data theft and extortion, reflecting a cost-saving response to improved ransomware detection and remediation efforts. RansomHub, Lynx, and Akira dominated ransomware activity, collectively accounting for 54% of incidents, while newer groups like BlackSuit aggressively targeted SMBs, showing a rise in sophisticated attacks.

Ransomware groups varied significantly in their tactics and timelines. Time-to-ransom (TTR) analysis revealed that groups like Akira deployed ransomware within six hours of initial access, favoring quick, high-impact attacks. Others like Cl0p and Medusa adopted slower, more deliberate methodologies. The number of malicious actions before ransomware deployment also varied, with extortion-focused groups performing more extensive reconnaissance, privilege escalation, and data exfiltration compared to groups prioritizing rapid encryption.

These findings highlight the evolving ransomware strategies and the critical need for proactive defenses to reduce response times and disrupt attackers before they get what they want.

> 54% of ransomware incidents were linked to RansomHub, Lynx, and Akira

## Ransomware Groups
The dirty business of ransomware became a tumultuous year for operators as global cybersecurity groups, law enforcement, government agencies, and private researchers came together throughout the year to bring down several notable ransomware groups.

Starting with the February takedown of LockBit, the group has splintered into several sub-groups. RansomHub has become the primary new home for most ex-LockBit operators, topping the list of top ransomware operators at 21%. While LockBit 3.0 and now 4.0 are still very much in the wild, they’ve shifted away from non-enterprise businesses and kept looking for larger payouts from more established enterprises, critical infrastructure, governments, and manufacturing targets.

The departure of Dharma/Crysis, Hive, and Phobos due to several multi-agency takedown operations shifted the playing field for ransomware operators in 2024. In addition, groups like BianLian have stopped deploying ransomware and instead chose to exfiltrate and extort targets for their data. This represents a cost-saving tactic from criminals, as detection for ransomware mechanisms, decryption tools, and resistant backup strategies become more widespread; these groups will turn to alternative methods to extort victims.

![Image description: Figure 10: Most prevalent ransomware affiliates in 2024. A bar graph showing the top ransomware operators. RansomHub, Inc/Lynx, Play, Medusa, Akira, Black Basta, BlackSuit, LockBit, Cl0p, and BianLian are listed on the x-axis.]

Huntress’ clients faced ransomware attacks from RansomHub, Lynx (the ransom group formerly known as Inc), and Akira. These three groups represented 54% of our ransomware incidents throughout the year, and all three appear to be offering affiliates high percentages and aren’t shy about targeting small to medium-sized businesses. All of them pursue quantity over quality of targets and will often target low-hanging fruit with minimal effort to hit exposed systems.

We saw the rise of BlackSuit (aka Royal) in 2024, a group that aggressively targeted business workforces throughout the world. As this group grows, we’ll likely see more sophisticated attacks and methods coming from them.

![Image description: Figure 11: Ransomware groups incident frequency from 2023 to 2024. A bar graph comparing ransomware groups incident frequency from 2023 to 2024. RansomHub, Inc/Lynx, Akira, Play, Dharma, Hive, LockBit, Medusa, Black Basta, Phobos, BianLian, Cl0p, and BlackSuit are listed on the x-axis.]

![Image description: Figure 12: Table of ransomware gains and losses since 2023. A table showing ransomware family, 2023 frequency, 2024 frequency & status, and losses and gains.]

## Time-To-Ransom (TTR) Measurement
During the year, Huntress investigated incidents where ransomware was deployed and crawled through activity logs to determine the ransomware operator’s initial access time. This could have been accessing an account through stolen credentials, abusing an RMM software, gaining access via an initial access broker, or through exploitation or social engineering. From here, we recorded the average time an attacker would move from initial access, reconnaissance, lateral movement, exfiltration, and ransomware deployment. We then attributed these per group based on the attempted delivered ransomware note.

![Image description: Figure 13: Average time-to-ransom (TTR) by ransomware group. A bar graph showing the average time-to-ransom (TTR) by ransomware group. Play, Dharma/Crysis, Akira, RansomHub, INC/Lynx, Maze, Uncategorized, Black Basta, Conti, LockBit, CryptoWall, MedusaLocker, Cl0p, Phobos, and Rapid are listed on the y-axis.]

Using data going back to late 2023, we developed a time-to-ransom (TTR) chart based on available incident information. Based on these findings, the overall average TTR we saw was almost 17 hours. And looking at that broken down by different ransomware groups, some groups prefer smash-and-grab techniques versus slow-and-low methodologies. With generic ransomware detections as the baseline, we saw that Play, Dharma/Crysis, and Akira tend to deploy ransomware the fastest, all in around six hours.

Multiple variables are at play in these scenarios:
- The initial access point where ransomware operators start their attack: what permissions did they start with, and what permissions did they require?
- Network pathing and availability of other systems
- User interaction as a deterrent? Waiting after business hours
- Does the victim have data they’re interested in and does it need to be exfiltrated?
- Some data may not have been ransomware operator, but from another attacker gaining access to the machine and then later providing access to the ransomware group (this is often the case with some RaaS)
- The phase at which Huntress was installed (installed as a response to a suspected incident)

Considering these as best we could, the Huntress team is further investigating options to improve this measurement in the future.

There are other groups that tend to move slower such as Cl0p, Medusa, and, oddly enough, Rapid. We saw a correlation between TTR and incident counts throughout the year, and it seems that TTR can be used as a rough basis for guessing how much time victims have to respond to prevent worst-case scenarios.

> Average time-to-ransom (TTR) is almost 17 hours
> 18 actions on average are taken before ransomware

![Image description: Figure 14: Activity prior to ransomware deployment by group. A bar graph showing the average number of actions before ransom. Conti, Play, Black Basta, MedusaLocker, Dharma/Crysis, RansomHub, INC/Lynx, Akira, Average Actions, Uncategorized, Sodinokibi, CryptoWall, LockBit, Cl0p, Maze, and Phobos are listed on the y-axis.]

## Activity Before Ransom
Another measure we looked at was how many actions groups performed before triggering a ransomware payload. These were the number of actions we were able to identify in a 48-hour window before attempting to deploy ransomware on the victim’s machine. Actions in this context are defined as malicious activity related to their goal such as efforts to perform reconnaissance. escalate privileges, move laterally, execute terminal commands, run scripts, download additional files, exfiltrate files, etc.

As seen in Figure 14, ransomware groups took an average of 18 actions that we could identify before triggering ransomware. But as we saw with TTR, some ransomware groups take more actions than others.

This demonstrates behavior within groups reflecting on goals and methodology from group to group. Attackers focusing on extortion, data theft, and espionage tend to perform more actions, with pivoting, data harvesting, and exfiltrating being those extra activities.

Attackers who rely on receiving ransomware payments for decryption tend to perform a lower number of actions as they’re basically smashing and grabbing.

Attackers keep exfiltrating data right up to the point of ransoming a victim, with many attackers implementing RAR or ZIP to bundle up data and exfiltrate it to their C2 servers. We saw more sophisticated attackers starting to use encrypted P2P services like Cloudflare tunneling to not only exfiltrate, but to deliver tools and malware. Other actions right before ransomware execution tend to be elevating privileges or disabling EDR or system backups/restoration settings to ensure file encryption is successfully executed. In other cases, it was lateral movement to a privileged server or device that had access to backups or critical data to get maximum impact.

While also not definitive as this data set has similar caveats to the above TTR chart, this can be used as a rough reference for how many opportunities defense tools and teams have before attackers ransomware victims. One interpretation of this data is to measure each group’s ability to identify and execute campaigns on targets based on efficiency. This could be based on the initial access brokers, RaaS, or affiliates each group uses, showing where some groups lack while others excel.

![Image description: Activity Immediately Prior to Ransomware. Adversary infrastructure. Adversary persistence. Enumeration phase. Huntress guidance. An example from the BianLian ransomware group, forgoing malicious encryption with their malicious tooling to prioritize data exfiltration and extortion.]

![Image description: Figure 15: Actions taken immediately before ransom. A bar graph showing the percentage of actions taken immediately before ransom. Privilege Elevation, Credential Access, Lateral Movement, Defense Evasion, and Exfiltrate Data are listed on the x-axis.]

## Attacker Tools and Techniques
In 2024, hackers relied heavily on specialized tools and techniques to automate tasks, gain access, and maintain control over compromised systems. While full-scale hacking tools suites like Cobalt Strike, Metasploit, and Sliver saw a decrease in usage, specialized tool and administrative tools like Mimikatz and Sysinternals Suite were critical for password sniffing, memory dumping, lateral movement, and privilege elevation. Remote access trojans (RATs) like AsyncRAT, NetSupport RAT, and Jupyter dominated remote access methods, contributing to more than 75% of incidents. Jupyter in particular evolved from an infostealer into a multi-stage backdoor with sophisticated capabilities.

The abuse of remote monitoring and management (RMM) tools, including ConnectWise ScreenConnect, TeamViewer, and LogMeIn also surged, representing 17.3% of remote access methods. Attackers abused these tools for stealthy persistence and lateral movement, with a significant campaign targeting ScreenConnect vulnerabilities early in the year. These trends highlight the increasing sophistication of hacking tools and the critical need for robust defenses to mitigate the risks posed by these techniques.

![Image description: Figure 16: Most common remote access methods used across 2024. A pie chart showing the most common remote access methods used. Generic RAT: 42.7%, AsyncRAT: 8.4%, Jupyter RAT: 6.7%, NewSupport RAT: 9.5%, NewCore RAT: 0.6%, JRAT: 0.8%, CinaRAT: 0.5%, PowerSplit: 0.4%, Meterpreter: 1.3%, Hacktool Generic: 1.6%, Cobalt Strike: 2.5%, Trickbot RAT: 6.7%, Generic RMM: 2.9%, ScreenConnect: 12.3%, SSH 1.1%.]

![Image description: Figure 17: Hacking tool usage in 2024. A bar graph showing hacking tool usage. CrackMapExec, SharpDump, Bloodhound, Empire, Network Scanner, Other, Atomic Red Team, PowerSploit, Hack Tool, Other, Metasploit, Advanced IP Scanner, Sysinternals, Mimikatz, and Cobalt Strike are listed on the y-axis.]

## Hacking Tools
When compromising machines en masse, hackers will automate many tasks as quickly as possible to attempt to gain access during the window of opportunity they have. To make this possible, hackers will turn to hack tools to perform all of these actions as quickly and efficiently as possible. These bundles of software can perform many complex hacking activities like password sniffing, memory dumping, decrypting of files, manipulation of targeted applications, install persistence, or remote access to a compromised machine with a simple button press. The origin of these tools dates back to the days of Back Orifice and Sub7 remote access tools in the late 1900s, and has evolved into Metasploit, Cobalt Strike, Mimikatz, and Empire.

Alternatively, attackers can also use tools that were designed for administrative tasks and abuse them to perform malicious actions. Examples of popular system tools that are abused by attackers are the Sysinternals Suite and network scanners.

Cobalt Strike remains the top hacking tool we saw, whether it’s abused by cybercriminals via cracked versions or legitimate red team usage in engagements. Cobalt Strike has even been adopted by a few known APT groups so they can operate with plausible deniability, like Ocean Lotus, APT31, Cinnamon Tempest, and Wizard Spider. Of all the hacking tools we see, Cobalt Strike occurs about one-third of the time.

Mimikatz, the cute cat password-dumping tool that was developed in 2011 by Benjamin Delpy and featured in Mr. Robot, is our second-most identified hacking tool. Attackers have been implementing this tool in payloads for nearly 14 years and it’s often delivered via download and execution payloads or implemented in PowerShell. Huntress has seen this tool associated with attacks delivered by Blue Mockingbird, Play ransomware, and Akira ransomware groups.

Network scanners are still an important tool for