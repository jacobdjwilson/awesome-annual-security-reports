# PRESENTED BY THE ADVERSARY PURSUIT GROUP ANNUAL THREAT REPORT 2024

## Table of Contents
- [Chapter 1: Executive Summary](#chapter-1-executive-summary)
- [Chapter 2: The 2023 Cyberthreat Landscape](#chapter-2-the-2023-cyberthreat-landscape)
- [Chapter 3: Citrix Bleed Vulnerability Case Study](#chapter-3-citrix-bleed-vulnerability-case-study)
- [Chapter 4: Cloud Security Trends and Insights](#chapter-4-cloud-security-trends-and-insights)
- [Chapter 5: Threat Actor Profiles](#chapter-5-threat-actor-profiles)
- [Chapter 6: Industry-Specific Threat Analysis](#chapter-6-industry-specific-threat-analysis)
- [Chapter 7: Predictions and Preparations for 2024](#chapter-7-predictions-and-preparations-for-2024)
- [Chapter 8: Cybersecurity Best Practices](#chapter-8-cybersecurity-best-practices)
- [Chapter 9: Conclusion](#chapter-9-conclusion)
- [Chapter 10: Glossary](#chapter-10-glossary)
- [Chapter 11: Contributors](#chapter-11-contributors)

## Chapter 1   Executive Summary

Executive Summary
2023 marked a year of intensified cyberthreats, with small- and medium-sized businesses (SMBs) finding themselves increasingly in the crosshairs of sophisticated cybercriminal operations. Blackpoint witnessed evolving ransomware and phishing attempts, advantageous Initial Access Brokers (IABs), an influx of Business Email Compromise (BEC) attempts, and the ongoing exploitation of legitimate applications. All of which created a challenging environment for organizations working hard to actively safeguard their hybrid environments.

REPORTING PERIOD: DECEMBER 2022-NOVEMBER 2023

While the year began with the dominance of access attempts, it gradually diversified to include credential access, Command and Control (C2), and phishing. We witnessed a noticeable sophistication of phishing attacks. Cybercriminals fine-tuned their social engineering (SE) tactics to craft highly convincing and personalized emails, websites, and messages. These phishing campaigns, often initiating multi-stage attacks, no longer aim solely at indiscriminate credential theft. Instead, they have become tools for installing malware, initiating lateral movement within networks, and setting the stage for more devastating attacks.

Lastly, threat actors increasingly exploited public-facing applications, capitalizing on common vulnerabilities and misconfigurations. Web servers, content management systems, and remote management interfaces, such as Remote Monitoring and Management (RMM) and Remote Desktop Protocol (RDP), were among the frequently targeted assets.

![Phishing Attacks]
![The Exploitation of Public-Facing Applications]

Ransomware attacks continued prominently with the existence of double extortion schemes, even triple at times, schemes adding a complex layer to the already daunting threat. Cybercriminals not only encrypt victim data but also threaten public release or deletion of sensitive information unless they receive the ransom. This tactic compounded the dilemma for businesses, forcing them to consider the dire consequences of data exposure, in addition to the operational paralysis caused by data encryption.

Supply chain attacks emerged as a critical vector, exploiting the interconnected nature of business operations. Attackers capitalized on the potential to breach one entity and infiltrate several others, exploiting the trust and relationships between businesses, their vendors, and Managed Service Providers (MSPs). These attacks had far-reaching ramifications, affecting multiple organizations through a single breach.

![Ransomware Attacks]
![Supply Chain Attacks]

In 2023, IABs, who specialize in breaching systems and selling unauthorized access to the highest bidder, significantly increased their activities. The commoditization of access turned into a booming business, fueling subsequent attacks, including ransomware and data theft.

Amidst these evolving threats, the ongoing threat of BEC persisted, often targeting SMBs with perceived lower defenses. In these schemes, attackers often impersonate company executives or partners to authorize fraudulent transactions, leading to significant financial losses and eroding trust in business communications.

![Inital Access Brokers]
![Business Email Compromise]

## Chapter 1   Executive Summary

In Summary
The 2023 landscape served as a stark reminder of the escalating sophistication and interconnectedness of cyberthreats. For SMBs, the year was a stark reminder to fortify their security defenses by:
- Prioritizing cybersecurity training
- Monitoring their networks with vigilance
- Having regular vulnerability assessments
- Patching vulnerabilities promptly
- Adhering to strict email security measures
- Proactively addressing emerging threats
- Monitoring the security practices of those they are partnered with
- Adopting the Defense in Depth (DiD) approach

In the face of these multifaceted threats, the importance of resilience, vigilance, and proactive threat mitigation strategies cannot be overstated, as we all navigate the intricacies of modern cyber-risks.

What is Defense in Depth?
A cybersecurity strategy that involves the implementation of multiple layers of security, each layer protecting against different types of security threats.

Train your team on cybersecurity and business best practices for free, today.
[LEARN MORE](https://www.blackpointcyber.com/)

## Chapter 2   The 2023 Cyberthreat Landscape

Understanding Initial Access in Cybersecurity
A common thread you will find throughout our threat report is the subject of initial access. Initial access covers the various methods a threat actor may use to gain unauthorized entry into a computer network or system. It is where a threat actor begins, and, when up against Blackpoint’s 24/7 Security Operations Center (SOC), is detained.

The Speed of Cyberthreats & Blackpoint’s Response
Experts often discuss cybercriminals’ dwell time in terms of days, but the initial stages of the attack chain occur in a much shorter timeframe. According to the SOC’s 2023 data, the average time between initial access and lateral movement for a threat actor was 83 minutes. With that in mind, CrowdStrike's recommended response framework seems sufficient. The 1/10/60 rule suggests one minute to detect the intrusion, 10 minutes to understand what the threat actor is trying to do, and one hour to contain the threat. At Blackpoint though, we see firsthand the critical nature of stopping initial access attempts, responding to discovered breaches within 15 minutes.

In fact, Blackpoint observed that attempts to gain initial access and move laterally through an organization, specifically targeting endpoint devices, constituted 95% of the threat landscape seen on these devices. This marks an increase from 2022’s already high percentage of 86%. The growth in this space can be attributed to several factors, such as:
- Implicit trust on binaries that support live-off-the-land (LotL)
- Easy access to trusted enterprise-level software such as RMM tools
- The rise of Software-as-a-Service (SaaS) that operates in the cloud and unifies entire organizations using just an email address

These factors and more, have led to a growing market for various threat actors acting as IABs for other groups.

Diverse Tactics for Initial Access
To gain initial access, threat actors have an arsenal of methods to pull from. Phishing and spear-phishing attacks, of course, continued to be prevalent methods. In 2023, a series of severe software vulnerabilities exposed organizations to the risk of remote code execution (RCE). The MSPs we partner with encountered a continual increase in attempts to compromise business email accounts through brute force and stolen credentials. With unfettered access into various industries, MSPs are highly desirable targets for supply chain attacks due to the implicit trust placed upon them by their customers and the powerful tools embedded in their environments, such as RMMs.

_83 minutes_
The average time between initial access and lateral movement for threat actors.

_15 minutes_
The average time Blackpoint SOC takes to respond to initial access attempts.

_95%_
of endpoint device incidents were initial access attempts.

The 2023 Cyberthreat Landscape

## Chapter 2   The 2023 Cyberthreat Landscape

The Growing Trend of RMM Tool Exploitation
With that in mind, threat actors frequently exploited RMM tools to gain initial access. Blackpoint observed this trend back in the spring of 2022, when threat actors were using these tools to deploy malicious payloads. Then, at the start of 2023, the Cybersecurity and Infrastructure Security Agency (CISA), National Security Agency (NSA), and Multi-State Information Sharing and Analysis Center (MS-ISAC) released a joint Cybersecurity Advisory (CSA) warning of the dangers presented by RMMs. Throughout 2023, we continued to see threat actors use these legitimate enterprise tools to gain initial access and propagate through organizations. In each case, the RMM being used was available through trial versions that lack human verification.

The Role of Live-off-the-Land in Cyberattacks
The increased use of enterprise software such as RMM tools is one of the primary reasons threat actors can work so quickly within an environment. These tools often use native binaries and libraries that support the LotL strategy, which enable a threat actor to remain undetected, avoid dependency on external tools, facilitate lateral movement, and more. In 2023, we observed over 1,000 instances of threat actors using the LotL strategy against our partners, with software such as PowerShell, Wscript, and Mshta amongst the most common native binaries. By doing so, IABs ensure wide-spread access before selling to other groups.

The Threat of Initial Access Brokers
IABs employ a variety of techniques, not limited to living off the land. They also use phishing attacks, stolen credentials, and exploitable vulnerabilities to gain initial access to systems. The increased demand for access has led to the growth of this offering with prices ranging from $500 to upwards of $20k. In late 2023, the takedown operation of Qakbot saw the seizure of over $8.6 million in cryptocurrencies, demonstrating how much revenue is generated by IAB groups.

The Ongoing Threat of Ransomware
Initial Access Brokers’ increased activity and profitability has aided groups specializing in ransomware. Over 2023, ransomware continued to take center stage with notable attacks against a plethora of organizations and industries, with the most damaging and publicly reviewed being those that adopt double extortion tactics. Notable instances throughout 2023 include LockBit’s attack against the Royal Mail in the United Kingdom, BlackCat’s attack on Leigh Valley Health Network that led to follow-on lawsuits against the company, and Royal’s attack on the City of Dallas that resulted in over $8.5 million dollars in restoration services.

Thankfully, our SOC has effectively prevented ransomware threat actors from infiltrating our systems yet again in 2023. As a result, the Adversary Pursuit Group (APG) utilized various open-source intelligence (OSINT) methods at the end of 2023 to evaluate the threat landscape. This approach led us to significant findings:
- We observed an approximate 64% increase in ransomware attacks employing double extortion tactics from 2022 to 2023.
- Almost 50% of ransomware attacks in 2023 were carried out by LockBit, a notorious Ransomware-as-a-Service (RaaS) known for its 'StealBit' tool, which facilitates efficient data exfiltration.

_64% increase_
in ransomware attacks employing double extortion tactics from 2022 to 2023.

_1,000+ incidents_
of threat actors using the LotL strategy were observed in 2023.

## Chapter 2   The 2023 Cyberthreat Landscape

![Top 10 Ransomware Threat Actors in 2023]

LockBit
2,387 records
1
2
3
4
5
6
7
8
9
10
BlackCat
681 records
CL0P
477 records
BianLian
370 records
Conti
333 records
Play
318 records
PYSA
307 records
Black Basta
260 records
8Base
252 records
Hive
207 records

In Summary
Due to the nature of our services, initial access accounts for 95% of our view of the cyberthreat landscape involving endpoint devices. Before threat actors can get any further, we have halted their steps. Whether a threat actor plans to exploit an RMM tool in a supply chain attack, deploy ransomware, or is an IAB looking to profit off access, time is of the essence. Advanced security services are required to go up against, and defeat, threat actors such as LockBit, BlackCat, and CL0P.

LockBit 3.0: 1,381 records
LockBit 2.0: 1,006 records

_Almost 50%_
of attacks committed in 2023 were by LockBit.

## Chapter 3   Case Study

One effective way to withstand advanced threats is through a SOC powered by Managed Detection, Response and Remediation (MDR+R). With our people and technology, we can respond to new threats and exploits in real time, such as the exploitation of RMM tools in 2022 and public-facing applications in 2023.

In October 2023, when the SOC was made aware of the critical ‘Citrix Bleed’ vulnerability (CVE-2023-4966), the team immediately familiarized itself with the indicators of compromise (IoCs) as well as how to identify and respond to the threats associated. Two months later, their preparation paid off and they encountered the exploitation firsthand. Blackpoint’s MDR+R alerted to multiple successful share mounts in one of our MSP’s end client environments.

Our Technical Director of Threat Operations, Jason Rathbun, triaged the environment and within one minute of initial triage, began containing the incident. Jason identified malicious activities, including scheduled tasks and suspicious remote executions, which are often signs of an ongoing cyberattack. The threat actors used advanced tactics and tried various methods to establish persistence in the environment, including:

Citrix Bleed Vulnerability Exploitation
- Based on the overall technical investigation, the SOC concluded the threat actors exploited the ‘Citrix Bleed’ vulnerability to gain initial access to the end client’s NetScaler Gateway. This appliance is pivotal for streamlining remote access infrastructure, as it enables single sign-on (SSO) capabilities for a variety of applications. This vulnerability, if left unpatched, can allow threat actors to execute arbitrary code remotely.

MDR-Powered SOC Combats Citrix Bleed Vulnerability Exploitation

## Chapter 3   Case Study

Domain Admin Session Theft
- From there, they stole a domain admin session, giving them high-level access privileges within the network, and set up two separate scheduled tasks in the environment to maintain persistence.

Persistence Setup
- Both scheduled tasks were designed to set up Go Simple Tunnel[^1], an OSINT resource used in this instance to help create SOCKS5 proxies[^2] to establish a backdoor connection.

Lateral Movement
- The threat actors then switched to the default domain administrator account and began using Impacket, a suite of tools for network protocols, to move laterally to a Domain Controller (DC) in the environment.
- Next, they switched accounts again and used Windows Remote Management (WinRM) to get to the Veeam server.

Data Access
- The threat actors also tried to conduct remote executions using PowerShell to expose the Structured Query Language (SQL) database of the Veeam servers and establish a Go Simple Tunnel connection from the DC to their Command and Control (C2), with the possible goal of accessing, modifying, deleting, or extracting data, as one would for double extortion.

Throughout the investigation, the SOC found numerous locations where the threat actors had set up persistence mechanisms, the most prevalent being scheduled tasks. The threat actors moved quickly and showed multiple defense evasion techniques such as rotating through valid accounts. They were methodical and blended in, using general windows management instrumentation (WMI) to evade antivirus (AV) and Endpoint Detection and Response (EDR) detection.

The SOC successfully contained the incident, which could have led to extensive data exfiltration and ransomware deployment. They then contacted the MSP, providing them with key details, time stamps, and remediation steps, such as blocking IoCs in their firewalls, to help eradicate the threat actors and prevent further malicious activity.

[^1]: Go Simple Tunnel is a tool used to create secure, encrypted communication channels. This connection would allow for data exfiltration and remote control of compromised systems.
[^2]: So Simple Tunnel is a tool used to create secure, encrypted communication channels. This connection would allow for data exfiltration and remote control of compromised systems.

The EDR Gap
Hear about real cases of EDR blind spots, and how MDR stepped in for the save.
[READ NOW](https://www.blackpointcyber.com/)

## Chapter 4   Cloud Security Trends and Insights

Immense Increase in Cloud Security Incidents
While we continued to combat on-premises threats, such as the ‘Citrix Bleed’ vulnerability, cloud security incidents have escalated significantly over the last year. We introduced the first-ever cloud MDR for Microsoft 365 in the spring of 2022, followed by Google Workspace protection in the fall of 2023. Due to the increasing reliance on cloud services and broadening threat landscape, along with our unmatched visibility, cloud-related incidents rose drastically in the last year. What accounted for 56.91% of Blackpoint’s incidents in December 2022 took up 88.46% in September 2023.

_78.78%_
of all incidents from December 2022 to November 2023 were cloud related.

_31.55% increase_
in cloud-related incidents from December 2022 to September 2023.

Cloud Security Trends and Insights

![Percentage of Cloud Incidents Encountered Each Month]

Nov.
2023
Oct.
2023
Sept.
2023
Aug.
2023
July
2023
June
2023
May
2023
April
2023
March
2023
Feb.
2023
Jan.
2023
Dec.
2022
40
60
80
100
56.91%
60.87%
73.58%
76.96%
84.62%
86.05%
88.46%
86.51%
86.17%
48.41%
60.00%
65.47%

## Chapter 4   Cloud Security Trends and Insights

Dominance of VPN-Related Incidents
A striking aspect of the year's cloud security landscape was the dominant role of virtual private networks (VPNs) in these incidents. We have observed consistently high VPN usage, present in over 99% of cloud incidents, suggesting they are heavily abused in cyberattacks. This trend emphasizes the criticality of secure and well-managed VPN solutions as part of the broader cloud security framework.

Shift in Attack Vectors: Initial Access and Diversification of Threats
As previously discussed, initial access formed a significant portion of the incident response activities performed by our SOC, accounting for over half of the cloud incidents at certain points during the year. It drastically increased in May 2023 and peaked in August 2023 at 214 attempts. Password spraying attacks, where threat actors use brute force to perform BEC, emerged as one of the largest perpetrators of gaining initial access. In the past year, BEC attempts rose by an average of 210%, reaching a total number of 42,688 incidents, with the highest number recorded in October.

![Business Email Compromise Attempts]

Dec.
2022
1,000
2,000
3,000
4,000
5,000
6,000
Nov.
2023
Oct.
2023
Sept.
2023
Aug.
2023
July
2023
June
2023
May
2023
April
2023
March
2023
Feb.
2023
Jan.
2023
Dec.
2022
5,404
5,834
5,747
4,299
4,747
3,767
3,163
2,608
2,744
1,879
1,437
1,059

_Over 99%_
of all cloud incidents include the presence of VPN usage.

_214 attempts_
of password spraying attacks were seen in August 2023.

_210% increase_
in BEC attempts over the last year, reaching a total number of 42,688 incidents.

## Chapter 4   Cloud Security Trends and Insights

In Summary
Our analysis of data from December 2022 to November 2023 reveals the growing complexities and evolving challenges in cloud security. Cloud security incidents significantly increased during this period, reflecting the increased dependence on cloud services and ever-expanding threat landscape. The data shows attackers making concentrated efforts to breach cloud defenses, likely driven by the valuable data within these environments.

VPN-related incidents dominated this period, highlighting the critical need for secure and effectively managed VPN solutions. Furthermore, there was a noticeable shift in attack vectors, initially dominated by access attempts but gradually diversifying to include credential access, C2, and phishing in the latter half of the year. These trends demonstrate the need for robust, adaptive, and comprehensive security strategies to combat the evolving cyberthreats and ensure the protection of cloud environments.

## Chapter 5   Threat Actor Profiles

Threat Actor Profiles
As the cybersecurity landscape continues to evolve, being able to recognize significant threat actors behind the threats we have discussed will be essential. While attribution is not always possible due to the speed at which our SOC operates, we encountered five particularly dominant cyber adversaries this year. BlackCat, LockBit, QakBot, RedLine Stealer, and Akira have established themselves in the cyberthreat landscape as frontrunners due to their advanced tactics, techniques, and procedures (TTPs), specific targets, and unique business approaches.

## Chapter 5   Threat Actor Profiles

BlackCat
BlackCat, a RaaS operation, is a possible rebranding of the group DarkSide. They were the first ransomware group to create a public data leaks site and target large enterprises, such as MGM Resorts in September 2023. BlackCat is written in Rust, enabling them to target Windows and Linux devices. Most recently, they escalated their tactics by filing an SEC complaint against a victim who did not disclose a cyberattack. Despite government interference, BlackCat continues to reemerge.

ALIASES:
ALPHV, AlphaV, Noberus

EMERGENCE:
Mid-November 2021

## Chapter 5   Threat Actor Profiles

![BlackCat TTPs]
Reconnaissance
T1598 Phishing for Information
Resource Development
T1586 Compromise Accounts
Initial Access
T1190 Exploit Public-Facing Application
T1078 Valid Accounts
Execution
T1059 Command and Scripting Interpreter
T1059.003 Windows Command Shell
T1047 Windows Management Instrumentation
Persistence
T1078 Valid Accounts
Privilege Escalation
T1548 Abuse Elevation Control Mechanism
T1548.002 Bypass User Account Control
T1134 Access Token Manipulation
T1078 Valid Accounts
Defense Evasion
T1548 Abuse Elevation Control Mechanism
T1548.002 Bypass User Account Control
T1134 Access Token Manipulation
T1562 Impair Defenses
T1562.001 Disable or Modify Tools
T1562.009 Safe Mode Boot
T1112 Modify Registry
T1078 Valid Accounts
Credential Access
T1557 Adversary-in-the-Middle
T1555 Credentials from Password Stores

## Chapter 5   Threat Actor Profiles

![BlackCat TTPs]
Discovery
T1087 Account Discovery
T1087.002 Domain Account
T1083 File and Directory Discovery
T1135 Network Share Discovery
T1069 Permission Groups Discovery
T1069.002 Domain Groups
T1057 Process Discovery
T1018 Remote System Discovery
T1082 System Information Discovery
T1016 NetworkConfiguration Discovery
T1033 System Owner / User Discovery
Lateral Movement
T1570 Lateral Tool Transfer
Collection
T1557 Adversary-in-the-Middle
Command and Control
T1071 Application Layer Protocol
T1219 Remote Access Software
Exfiltration
T1048 Exfiltration Over Alternative Protocol
T1041 Exfiltration Over C2 Channel
T1567 Exfiltration Over Web Service
Impact
T1486 Data Encrypted for Impact
T1491 Defacement
T1491.002 External Defacement
T1561 Disk Wipe
T1561.001 Disk Content Wipe
T1490 Inhibit System Recovery
T1489 Service Stop

## Chapter 5   Threat Actor Profiles

Typical Attack Chain:
Initial Access:
BlackCat is known to use OSINT (T1598) and advanced SE tactics, often pretending to be legitimate IT staff. They do so to trick users into providing additional information. This is done with the aim of social engineering other individuals or acquiring credentials (T1586), which can then be used to gain access to the system.

Follow-On Activities:
- Deploy legitimate software (e.g., AnyDesk, Splashtop, Mega Sync, Plink, and Ngrok) for remote access and to prepare for data exfiltration (T1041)
- Create a connection to C2 servers such as Brute Ratel C4 or Cobalt Strike (T1071)
- Deploy attack frameworks such as Evilginx2 to capture multifactor authentication (MFA), login credentials, and session cookies (T1557)
- Use access token manipulation (T1134), or credentials from the DC, local networks, and backups (T1555) to gain elevated credentials that will enable enumeration and lateral movement
- Exfiltrate system data through the C2 channel (T1041), web services (T1567), or alternative protocol (T1048)

Impact:
- BlackCat often extorts victims with the threat of releasing their exfiltrated sensitive data to other threat actors.
- They are known to encrypt all systems and files (T1486) and/or completely erase content (T1561).
- They may deface (T1491) and inhibit system recovery (T1490).

Other Tools Seen:
Mega.nz, Dropbox, Metasploit, POORTRY, STONESTOP, The Onion Router (Tor), sragent.exe, psexec32.exe, version.dll

EVOLUTION:
BlackCat represents a new wave of ransomware threats, evolving from previous groups like DarkSide and BlackMatter. BlackCat is written in Rust, which indicates sophistication on the part of their developers. It enables them to target both Windows and Linux devices, and often evade detection by traditional security tools.

BUSINESS MODEL:
BlackCat operates under a RaaS model, where developers offer malware to affiliates in exchange for a percentage of the ransom payments. They have gained recognition for their sophisticated double and sometimes triple extortion tactics. Recently, they escalated their tactics by including the filing of an SEC complaint against a victim for not disclosing a cyberattack.

INNOVATIVE TECHNIQUES:
BlackCat is notable for being the first ransomware group to create a public data leaks site on the open internet and for employing typo-squatted replicas of victim websites to post stolen data, enhancing the pressure on victims.

TARGET PROFILE:
They target a broad range of global entities including universities, government agencies, and companies in the energy, technology, manufacturing, and transportation sectors. Recent highly impacted targets include MGM Resorts International and Caesars Entertainment.

ASSOCIATED GROUPS:
They are linked to discontinued RaaS groups like DarkSide and BlackMatter. Some speculate that it may be a rebranding of DarkSide or a successor to REvil.

## Chapter 5   Threat Actor Profiles

LockBit
LockBit is well known for its continuous evolution through versions 2.0 and 3.0. They operate as a RaaS and have been known to recruit insiders from the companies they target. They tend to target healthcare facilities and schools, particularly those with Linux devices.

ALIASES:
ABCD Ransomware

EMERGENCE:
September 2019

## Chapter 5   Threat Actor Profiles

![LockBit TTPs]
Initial Access
T1189 Drive-by Compromise
T1190 Exploit Public-Facing Application
T1133 External Remote Services
T1566 Phishing
T1078 Valid Accounts
Execution
T1059 Command and Scripting Interpreter
T1059.003 Windows Command Shell
T1053 Scheduled Task/Job
T1072 Software Deployment Tools
T1204 User Execution
Persistence
T1547 Boot or Logon Autostart Execution
T1133 External Remote Services
T1574 Hijack Execution Flow
T1053 Scheduled Task/Job
T1078 Valid Accounts
Privilege Escalation
T1548 Abuse Elevation Control Mechanism
T1134 Access Token Manipulation
T1547 Boot or Logon Autostart Execution
T1484 Domain Policy Modification
T1484.001 Group Policy Modification
T1574 Hijack Execution Flow
T1053 Scheduled Task/Job
T1053.005 Scheduled Task
T1078 Valid Accounts
Defense Evasion
T1548 Abuse Elevation Control Mechanism
T1134 Access Token Manipulation
T1140 Deobfuscate/Decode Files or Information
T1484 Domain Policy Modification
T1574 Hijack Execution Flow
T1562 Impair Defenses
T1562.001 Disable or Modify Tools

## Chapter 5   Threat Actor Profiles

![LockBit TTPs]
T1070 Indicator Removal
T1070.001 Clear Windows Event Logs
T1070.004 File Deletion
T1027 Obfuscated Files or Information
T1027.002 Software Packing
T1127 Trusted Developer Utilities Proxy Execution
T1078 Valid Accounts
Credential Access
T1110 Brute Force
T1003 OS Credential Dumping
T1003.001 LSASS Memory
Discovery
T1083 File and Directory Discovery
T1046 Network Service Discovery
T1135 Network Share Discovery
T1057 Process Discovery
T1018 Remote System Discovery
T1082 System Information Discovery
Lateral Movement
T1570 Lateral Tool Transfer
T1021 Remote Services
T1021.001 Remote Desktop Protocol
T1021.002 SMB/Windows Admin Shares
T1072 Software Deployment Tools
Command and Control
T1095 Non-Application Layer Protocol
T1572 Protocol Tunneling
T1219 Remote Access Software
Exfiltration
T1041 Exfiltration Over C2 Channel
T1567 Exfiltration Over Web Service
T1567.002 Exfiltration to Cloud Storage
Impact
T1485 Data Destruction
T1486 Data Encrypted for Impact
T1491 Defacement
T1491.001 Internal Defacement
T1490 Inhibit System Recovery
T1489 Service Stop

## Chapter 5   Threat Actor Profiles

Typical Attack Chain:
Initial Access:
LockBit affiliates typically use compromised servers (T1189) or exploit external services (T1133) such as RDP. LockBit has also been seen gaining access through phishing attempts (T1566) and valid accounts (T1078).

Follow-On Activities:
- Execute batch scripts (T1059) or Chocolatey package manager (T1072) to begin attack deployment
- Use compromised user accounts (T1078) and find additional accounts with tools such as Mimikatz (T1003) to gain privilege escalation with which persistence can be established via scheduled tasks (T1053) and autostart execution (T1574)
- Evade detection and impair defenses (T1562) by attempting to disable EDR processes using tools such as Backstab, Defender Control, GMER, PCHunter, PowerTool, Process Hacker, or TDSSKiller
- Use Splashtop Remote Desktop, Cobalt Strike (T1570), and remote services (T1021) for lateral movement throughout the network
- Conduct C2 using tools such as FileZilla, SOCKS5 TCP tunnels, and AnyDesk (T1219)
- Exfiltrate data using tools like Rclone, FreeFileSync, or Mega (T1567)

Impact:
- LockBit encrypts Windows, Linux, and VMware instances, using Advanced Encryption Standard (AES) with randomly generated keys to hold for ransom (T1486).
- They change wallpapers and icons to custom LockBit 3.0 ones (T1491).
- They delete volume shadow copies (T1485) and terminate processes and services (T1489) to reduce the likelihood of recovery.

Other Tools Seen:
Blister Loader, ExtPassword, LostMyPassword, SystInternals Prodump, ThunderShell, Plink, Atera RMM, ScreenConnect, TeamViewer

EVOLUTION:
LockBit has evolved significantly since its inception, with notable advancements seen in their 2.0 and 3.0 versions. LockBit 2.0 surfaced in June 2021, followed by 3.0 in March 2022. These evolutions include improved encryption methods, targeting strategies, and the introduction of innovative tools like "StealBit" for data exfiltration.

BUSINESS MODEL:
LockBit operates as a RaaS group using double extortion tactics and offers ransomware to affiliates, sharing profits from the ransom payments.

INNOVATIVE TECHNIQUES:
They developed “StealBit” for efficient data exfiltration, and target Linux devices, focusing on ESXi servers, showcasing their adaptability and technical sophistication.

TARGET PROFILE:
They predominantly target the healthcare and education sectors, with significant attacks in Brazil, India, and the United States.

ASSOCIATED GROUPS:
They collaborate with various criminal groups and network access brokers, even recruiting insiders from targeted companies.

## Chapter 5   Threat Actor Profiles

QakBot
QakBot is a versatile botnet that offers a suite of tools, often setting the stage for Conti, Egregor, and others’ ransomware deployments. Despite government interference, QakBot continues to return with new, innovative tactics.

ALIASES:
Qbot, Quackbot, Pinkslipbot, TA570

EMERGENCE:
2008. They are one of the longest-standing threats in the cyber landscape.

## Chapter 5   Threat Actor Profiles

![QakBot TTPs]
Execution
T1106 Native API
T1047 Windows Management Instrumentation
Defense Evasion
T1140 Deobfuscate/Decode Files or Information
T1112 Modify Registry
T1027 Obfuscated Files or Information
T1027.001 Binary Padding
T1027.010 Command Obfuscation
T1027.011 Fileless Storage
T1027.006 HTML Smuggling
T1027.005 Indicator Removal from Tools
T1027.002 Software Packing
Credential Access
T1110 Brute Force
T1539 Steal Web Session Cookie
Discovery
T1010 Application Window Discovery
T1482 Domain Trust Discovery
T1083 File and Directory Discovery
T1135 Network Share Discovery
T1120 Peripheral Device Discovery
T1057 Process Discovery
T1018 Remote System Discovery
T1518 Software Discovery
T1518.001 Security Software Discovery
T1082 System Information Discovery
T1016 System Network Configuration Discovery
T1016.001 Internet Connection Discovery
T1049 System Network Connections Discovery
T1033 System Owner/User Discovery
T1124 System Time Discovery

## Chapter 5   Threat Actor Profiles

![QakBot TTPs]
Lateral Movement