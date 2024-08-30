ANNUAL
THREAT REPORTP RESENTE DB YT H EADVERSARY
PURSUIT GROUP2A NNUA LT HREA TR EPOR T2 0 2 4Table of ContentsTable of ContentsChapter 1: Executive Summary 3Chapter 2: The 2023 Cyberthreat Landscape 5Chapter 3: Citrix Bleed Vulnerability Case Study 8Chapter 4: Cloud Security Trends and Insights 10Chapter 5: Threat Actor Profiles 13Chapter 6: Industry\-Specific Threat Analysis 35Chapter 7: Predictions and Preparations for 2024 44Chapter 8: Cybersecurity Best Practices 47Chapter 9: Conclusion49Chapter 10: Glossary 50Chapter 11: Contributors 513Executive SummaryR EPORTIN GP ERIOD :DECEMBE R2 0 2 2 \- N OV EMBE R2 0 2 32023 marked a year of intensified cyberthreats, with small\- and medium\-sized businesses (SMBs) 
finding themselves increasingly in the crosshairs of sophisticated cybercriminal operations. 
Blackpoint witnessed evolving ransomware and phishing attempts, advantageous Initial Access 
Brokers (IABs), an influx of Business Email Compromise (BEC) attempts, and the ongoing 
exploitation of legitimate applications. All of which created a challenging environment for 
organizations working hard to actively safeguard their hybrid environments.Ransomware AttacksSupply Chain AttacksRansomware attacks continued prominently with the 
existence of double extortion schemes, even triple at times, 
schemes adding a complex layer to the already daunting 
threat. Cybercriminals not only encrypt victim data but also 
threaten public release or deletion of sensitive information 
unless they receive the ransom. This tactic compounded 
the dilemma for businesses, forcing them to consider the 
dire consequences of data exposure, in addition to the 
operational paralysis caused by data encryption.Supply chain attacks emerged as a critical vector, 
exploiting the interconnected nature of business 
operations. Attackers capitalized on the potential to 
breach one entity and infiltrate several others, exploiting 
the trust and relationships between businesses, their 
vendors, and Managed Service Providers (MSPs). These 
attacks had far\-reaching ramifications, affecting multiple 
organizations through a single breach.Inital Access BrokersBusiness Email CompromiseIn 2023, IABs, who specialize in breaching systems and 
selling unauthorized access to the highest bidder, significantly 
increased their activities. The commoditization of access 
turned into a booming business, fueling subsequent attacks, 
including ransomware and data theft.Phishing AttacksWhile the year began with the dominance of access attempts, 
it gradually diversified to include credential access, Command 
and Control (C2\), and phishing. We witnessed a noticeable 
sophistication of phishing attacks. Cybercriminals fine\-tuned 
their social engineering (SE) tactics to craft highly convincing 
and personalized emails, websites, and messages. These 
phishing campaigns, often initiating multi\-stage attacks, no 
longer aim solely at indiscriminate credential theft. Instead, 
they have become tools for installing malware, initiating 
lateral movement within networks, and setting the stage for 
more devastating attacks.Amidst these evolving threats, the ongoing threat of BEC 
persisted, often targeting SMBs with perceived lower 
defenses. In these schemes, attackers often impersonate 
company executives or partners to authorize fraudulent 
transactions, leading to significant financial losses and 
eroding trust in business communications.The Exploitation of
Public\-Facing Applications
Lastly, threat actors increasingly exploited public\-facing 
applications, capitalizing on common vulnerabilities and 
misconfigurations. Web servers, content management 
systems, and remote management interfaces, such 
as Remote Monitoring and Management (RMM) and 
Remote Desktop Protocol (RDP), were among the 
frequently targeted assets.ANNUAL THREAT REPORT 2024Chapter 1Executive Summary4In SummaryThe 2023 landscape served as a stark reminder of the escalating 
sophistication and interconnectedness of cyberthreats. For SMBs,
the year was a stark reminder to fortify their security defenses by:Prioritizing cybersecurity trainingMonitoring their networks with vigilanceHaving regular vulnerability assessmentsPatching vulnerabilities promptlyAdhering to strict email security measuresProactively addressing emerging threatsWhat is Defense
in Depth?A cybersecurity strategy
that involves the 
implementation of 
multiple layers of security, 
each layer protecting 
against different types of 
security threats.Monitoring the security practices of those they are partnered withAdopting the Defense in Depth (DiD) approachIn the face of these multifaceted threats, the importance of resilience, 
vigilance, and proactive threat mitigation strategies cannot be 
overstated, as we all navigate the intricacies of modern cyber\-risks.Train your team on 
cybersecurity and business 
best practices for free, today.LEAR NM OR EANNUAL THREAT REPORT 2024Chapter 1Executive Summary5The 2023 Cyberthreat 
Landscape83 minutes
The average time 
between initial access 
and lateral movement 
for threat actors.15 minutes
The average time 
Blackpoint SOC takes 
to respond to initial 
access attempts.95%
of endpoint device 
incidents were initial 
access attempts.Understanding Initial Access in Cybersecurity 
A common thread you will find throughout our threat report is the subject of initial access.
Initial access covers the various methods a threat actor may use to gain unauthorized entry
into a computer network or system. It is where a threat actor begins, and, when up against 
Blackpoints 247 Security Operations Center (SOC), is detained.The Speed of Cyberthreats \&
Blackpoints Response 
Experts often discuss cybercriminals dwell time in terms of days, but the initial stages of the 
attack chain occur in a much shorter timeframe. According to the SOCs 2023 data, the average 
time between initial access and lateral movement for a threat actor was 83 minutes. With that 
in mind, CrowdStrike's recommended response framework seems sufficient. The 11060 rule 
suggests one minute to detect the intrusion, 10 minutes to understand what the threat actor is 
trying to do, and one hour to contain the threat. At Blackpoint though, we see firsthand the critical 
nature of stopping initial access attempts, responding to discovered breaches within 15 minutes.In fact, Blackpoint observed that attempts to gain initial access and move laterally through
an organization, specifically targeting endpoint devices, constituted 95% of the threat landscape 
seen on these devices. This marks an increase from 2022s already high percentage of 86%.
The growth in this space can be attributed to several factors, such as:Implicit trust on binaries that support live\-off\-the\-land (LotL)Easy access to trusted enterprise\-level software such as RMM toolsThe rise of Software\-as\-a\-Service (SaaS) that operates in the cloud and unifies entireorganizations using just an email addressThese factors and more, have led to a growing market for various threat actors acting as IABs
for other groups.Diverse Tactics for Initial Access 
To gain initial access, threat actors have an arsenal of methods to pull from. Phishing and
spear\-phishing attacks, of course, continued to be prevalent methods. In 2023, a series of
severe software vulnerabilities exposed organizations to the risk of remote code execution (RCE). 
The MSPs we partner with encountered a continual increase in attempts to compromise business 
email accounts through brute force and stolen credentials. With unfettered access into various 
industries, MSPs are highly desirable targets for supply chain attacks due to the implicit trust 
placed upon them by their customers and the powerful tools embedded in their environments, 
such as RMMs.ANNUAL THREAT REPORT 2024Chapter 2The 2023 Cyberthreat Landscape6The Growing Trend of RMM Tool Exploitation 
With that in mind, threat actors frequently exploited RMM tools to gain initial access. Blackpoint 
observed this trend back in the spring of 2022, when threat actors were using these tools to 
deploy malicious payloads. Then, at the start of 2023, the Cybersecurity and Infrastructure 
Security Agency (CISA), National Security Agency (NSA), and Multi\-State Information Sharing 
and Analysis Center (MS\-ISAC) released a joint Cybersecurity Advisory (CSA) warning of the 
dangers presented by RMMs. Throughout 2023, we continued to see threat actors use these 
legitimate enterprise tools to gain initial access and propagate through organizations. In each 
case, the RMM being used was available through trial versions that lack human verification.1,000\+ incidents
of threat actors using 
the LotL strategy were 
observed in 2023\.The Role of Live\-off\-the\-Land in Cyberattacks 
The increased use of enterprise software such as RMM tools is one of the primary reasons threat 
actors can work so quickly within an environment. These tools often use native binaries and 
libraries that support the LotL strategy, which enable a threat actor to remain undetected, avoid 
dependency on external tools, facilitate lateral movement, and more. In 2023, we observed over 
1,000 instances of threat actors using the LotL strategy against our partners, with software such 
as PowerShell, Wscript, and Mshta amongst the most common native binaries. By doing so, IABs 
ensure wide\-spread access before selling to other groups.64% increase 
in ransomware attacks 
employing double 
extortion tactics from 
2022 to 2023\.The Threat of Initial Access Brokers 
IABs employ a variety of techniques, not limited to living off the land. They also use phishing 
attacks, stolen credentials, and exploitable vulnerabilities to gain initial access to systems. The 
increased demand for access has led to the growth of this offering with prices ranging from $500 
to upwards of $20k. In late 2023, the takedown operation of Qakbot saw the seizure of over $8\.6 
million in cryptocurrencies, demonstrating how much revenue is generated by IAB groups.The Ongoing Threat of Ransomware 
Initial Access Brokers increased activity and profitability has aided groups specializing in 
ransomware. Over 2023, ransomware continued to take center stage with notable attacks against 
a plethora of organizations and industries, with the most damaging and publicly reviewed being 
those that adopt double extortion tactics. Notable instances throughout 2023 include LockBits 
attack against the Royal Mail in the United Kingdom, BlackCats attack on Leigh Valley Health 
Network that led to follow\-on lawsuits against the company, and Royals attack on the City of 
Dallas that resulted in over $8\.5 million dollars in restoration services.Thankfully, our SOC has effectively prevented ransomware threat actors from infiltrating
our systems yet again in 2023\. As a result, the Adversary Pursuit Group (APG) utilized various 
open\-source intelligence (OSINT) methods at the end of 2023 to evaluate the threat landscape. 
This approach led us to significant findings:We observed an approximate 64% increase in ransomware attacks employingdouble extortion tactics from 2022 to 2023\.Almost 50% of ransomware attacks in 2023 were carried out by LockBit,a notorious Ransomware\-as\-a\-Service (RaaS) known for its 'StealBit' tool,
which facilitates efficient data exfiltration.ANNUAL THREAT REPORT 2024Chapter 2The 2023 Cyberthreat LandscapeLockBit 
2,387 records7Almost 50%
of attacks committed in 
2023 were by LockBit.LockBit 3\.0: 1,381 recordsLockBit 2\.0: 1,006recordsTop 10 Ransomware 
Threat Actors in 2023123456789BlackCat
681 recordsCL0P
477 recordsBianLian
370 recordsConti
333 recordsPlay
318 recordsPYSA
307 recordsBlack Basta
260 records8Base
252 records10Hive
207 recordsIn SummaryDue to the nature of our services, initial access accounts for 95% of our 
view of the cyberthreat landscape involving endpoint devices. Before 
threat actors can get any further, we have halted their steps. Whether 
a threat actor plans to exploit an RMM tool in a supply chain attack, 
deploy ransomware, or is an IAB looking to profit off access, time is of
the essence. Advanced security services are required to go up against, 
and defeat, threat actors such as LockBit, BlackCat, and CL0P.ANNUAL THREAT REPORT 2024Chapter 2The 2023 Cyberthreat Landscape8MDR\-Powered SOC 
Combats Citrix Bleed 
Vulnerability ExploitationOne effective way to withstand advanced threats is through a 
SOC powered by Managed Detection, Response and Remediation 
(MDR\+R). With our people and technology, we can respond to new 
threats and exploits in real time, such as the exploitation of RMM 
tools in 2022 and public\-facing applications in 2023\.In October 2023, when the SOC was made aware of the critical 
Citrix Bleed vulnerability (CVE\-2023\-4966\), the team immediately 
familiarized itself with the indicators of compromise (IoCs) as
well as how to identify and respond to the threats associated.
Two months later, their preparation paid off and they encountered 
the exploitation firsthand. Blackpoints MDR\+R alerted to multiple 
successful share mounts in one of our MSPs end
client environments.Our Technical Director of Threat Operations, Jason Rathbun, 
triaged the environment and within one minute of initial triage, 
began containing the incident. Jason identified malicious activities, 
including scheduled tasks and suspicious remote executions, which 
are often signs of an ongoing cyberattack. The threat actors used 
advanced tactics and tried various methods to establish persistence 
in the environment, including:Citrix Bleed Vulnerability ExploitationBased on the overall technical investigation, the SOC concluded the threat actorsexploited the Citrix Bleed vulnerability to gain initial access to the end clients NetScaler 
Gateway. This appliance is pivotal for streamlining remote access infrastructure, as it 
enables single sign\-on (SSO) capabilities for a variety of applications. This vulnerability, 
if left unpatched, can allow threat actors to execute arbitrary code remotely.ANNUAL THREAT REPORT 2024Chapter 3Case Study91\.So Simple Tunnel is a tool usedto create secure, encrypted 
communication channels. This 
connection would allow for data 
exfiltration and remote control of 
compromised systems.2\.Go Simple Tunnel is a tool used 
to create secure, encrypted 
communication channels. This 
connection would allow for data 
exfiltration and remote control 
of compromised systems.The EDR GapHear about real cases of EDR 
blind spots, and how MDR 
stepped in for the save.REA DN OWDomain Admin Session TheftFrom there, they stole a domain admin session, giving them high\-level access privileges 
within the network, and set up two separate scheduled tasks in the environment to
maintain persistence.Persistence SetupBoth scheduled tasks were designed to set up Go Simple Tunnel (1\), an OSINT resourceused in this instance to help create SOCKS5 proxies (2\) to establish a backdoor connection.Lateral MovementThe threat actors then switched to the default domain administrator account andbegan using Impacket, a suite of tools for network protocols, to move laterally to a
Domain Controller (DC) in the environment.Next, they switched accounts again and used Windows Remote Management (WinRM)to get to the Veeam server.Data AccessThe threat actors also tried to conduct remote executions using PowerShell to expose theStructured Query Language (SQL) database of the Veeam servers and establish a Go Simple 
Tunnel connection from the DC to their Command and Control (C2\), with the possible goal of 
accessing, modifying, deleting, or extracting data, as one would for double extortion.Throughout the investigation, the SOC found numerous locations 
where the threat actors had set up persistence mechanisms, the most 
prevalent being scheduled tasks. The threat actors moved quickly and 
showed multiple defense evasion techniques such as rotating through 
valid accounts. They were methodical and blended in, using general 
windows management instrumentation (WMI) to evade antivirus (AV) 
and Endpoint Detection and Response (EDR) detection.The SOC successfully contained the incident, which could have led to 
extensive data exfiltration and ransomware deployment. They then 
contacted the MSP, providing them with key details, time stamps, 
and remediation steps, such as blocking IoCs in their firewalls, to help 
eradicate the threat actors and prevent further malicious activity.ANNUAL THREAT REPORT 2024Chapter 3Case Study1 0Cloud Security Trends 
and InsightsImmense Increase in Cloud Security IncidentsWhile we continued to combat on\-premises threats, such as the Citrix Bleed vulnerability, 
cloud security incidents have escalated significantly over the last year. We introduced the 
first\-ever cloud MDR for Microsoft 365 in the spring of 2022, followed by Google Workspace 
protection in the fall of 2023\. Due to the increasing reliance on cloud services and broadening 
threat landscape, along with our unmatched visibility, cloud\-related incidents rose drastically 
in the last year. What accounted for 56\.91% of Blackpoints incidents in December 2022 took 
up 88\.46% in September 2023\.Percentage of Cloud Incidents Encountered Each Month:31\.55% increase 
in cloud\-related incidents 
from December 2022 to 
September 2023\.10088\.46%86\.17%84\.62%86\.05%86\.51%8076\.96%73\.58%60\.87%6056\.91%65\.47%60\.00%48\.41%40Dec.
2022Jan.
2023Feb.
2023March
2023April
2023May
2023June
2023July
2023Aug.
2023Sept.
2023Oct.
2023Nov.
202378\.78% 
of all incidents from 
December 2022 to 
November 2023 were 
cloud related.ANNUAL THREAT REPORT 2024Chapter 4Cloud Security Trends and Insights1 1Over 99% 
of all cloud incidents 
include the presence 
of VPN usage.Dominance of VPN\-Related Incidents 
A striking aspect of the year's cloud security landscape was the dominant role of virtual private 
networks (VPNs) in these incidents. We have observed consistently high VPN usage, present 
in over 99% of cloud incidents, suggesting they are heavily abused in cyberattacks. This trend 
emphasizes the criticality of secure and well\-managed VPN solutions as part of the broader 
cloud security framework.214 attempts 
of password spraying 
attacks were seen in 
August 2023\.Shift in Attack Vectors: Initial Access and
Diversification of Threats 
As previously discussed, initial access formed a significant portion of the incident response 
activities performed by our SOC, accounting for over half of the cloud incidents at certain
points during the year. It drastically increased in May 2023 and peaked in August 2023 at
214 attempts. Password spraying attacks, where threat actors use brute force to perform
BEC, emerged as one of the largest perpetrators of gaining initial access. In the past year,
BEC attempts rose by an average of 210%, reaching a total number of 42,688 incidents,
with the highest number recorded in October.Business Email Compromise Attempts6,0005,0004,0003,0005,8345,7475,4044,7474,2993,7673,1632,7442,608210% increase 
in BEC attempts over 
the last year, reaching 
a total number of 
42,688 incidents.2,0001,8791,4371,0591,000Dec.
Dec.
2022 
2022Jan.
2023Feb.
2023March
2023April
2023May
2023June
2023July
2023Aug.
2023Sept.
2023Oct.
2023Nov.
2023ANNUAL THREAT REPORT 2024Chapter 4Cloud Security Trends and Insights1 2In SummaryOur analysis of data from December 2022 to November 2023 
reveals the growing complexities and evolving challenges in cloud 
security. Cloud security incidents significantly increased during 
this period, reflecting the increased dependence on cloud services 
and ever\-expanding threat landscape. The data shows attackers 
making concentrated efforts to breach cloud defenses, likely 
driven by the valuable data within these environments.
VPN\-related incidents dominated this period, highlighting the 
critical need for secure and effectively managed VPN solutions.Furthermore, there was a noticeable shift in attack vectors, 
initially dominated by access attempts but gradually diversifying 
to include credential access, C2, and phishing in the latter half of 
the year. These trends demonstrate the need for robust, adaptive, 
and comprehensive security strategies to combat the evolving 
cyberthreats and ensure the protection of cloud environments.ANNUAL THREAT REPORT 2024Chapter 4Cloud Security Trends and Insights1 3A NNUA LT HREA TR EPOR T2 0 2 4Chapter 5Threat Actor ProfilesThreat Actor ProfilesAs the cybersecurity landscape continues to evolve, being able 
to recognize significant threat actors behind the threats we have 
discussed will be essential. While attribution is not always possible 
due to the speed at which our SOC operates, we encountered 
five particularly dominant cyber adversaries this year. BlackCat, 
LockBit, QakBot, RedLine Stealer, and Akira have established 
themselves in the cyberthreat landscape as frontrunners due to 
their advanced tactics, techniques, and procedures (TTPs),
specific targets, and unique business approaches.1 4BlackCatA LIASES :ALPHV, AlphaV,
NoberusE MERGENCE :Mid\-November 2021BlackCat, a RaaS operation, is a possible rebranding of the 
group DarkSide. They were the first ransomware group to create 
a public data leaks site and target large enterprises, such as 
MGM Resorts in September 2023\. BlackCat is written in Rust, 
enabling them to target Windows and Linux devices. Most 
recently, they escalated their tactics by filing an SEC complaint 
against a victim who did not disclose a cyberattack. Despite 
government interference, BlackCat continues to reemerge.ANNUAL THREAT REPORT 2024Chapter 5Threat Actor Profiles1 5BlackCat TTPsReconnaissanceT1598Phishing for InformationResourceDevelopmentT1586 CompromiseAccountsInitial AccessT1190 Exploit Public\-Facing ApplicationT1078 Valid AccountsExecutionT1059 Command and Scripting InterpreterT1059\.003 Windows Command ShellT1047 Windows Management InstrumentationPersistenceT1078 Valid AccountsPrivilege EscalationT1548 Abuse Elevation Control MechanismT1548\.002 Bypass User Account ControlT1134 Access Token ManipulationT1078 Valid AccountsDefense EvasionT1548 Abuse Elevation Control MechanismT1548\.002 Bypass User Account ControlT1562\.001 Disable or Modify ToolsT1562\.009 Safe Mode BootT1134 Access Token ManipulationT1562 Impair DefensesT1112 Modify RegistryT1078 Valid AccountsCredentialAccessT1557 Adversary\-in\-the\-MiddleT1555 Credentials from Password StoresANNUAL THREAT REPORT 2024Chapter 5Threat Actor Profiles1 6BlackCat TTPsDiscoveryT1087 Account DiscoveryT1087\.002 Domain AccountT1083 File and Directory DiscoveryT1135 Network Share DiscoveryT1069 Permission Groups DiscoveryT1069\.002 Domain GroupsT1057 Process DiscoveryT1018 Remote System DiscoveryT1082 System Information DiscoveryT1016 NetworkConfiguration DiscoveryT1033 System Owner User DiscoveryLateral MovementT1570 Lateral Tool TransferCollectionT1557 Adversary\-in\-the\-MiddleCommandand ControlT1071 Application Layer ProtocolT1219 Remote Access SoftwareExfiltrationT1048 Exfiltration Over Alternative ProtocolT1041 Exfiltration Over C2 ChannelT1567 Exfiltration Over Web ServiceImpactT1486 Data Encrypted for ImpactT1491 DefacementT1561 Disk WipeT1490 Inhibit System RecoveryT1489 Service StopT1491\.002 External DefacementT1561\.001 Disk Content WipeANNUAL THREAT REPORT 2024Chapter 5Threat Actor Profiles1 7E VO LUTION :BlackCat represents a new wave of 
ransomware threats, evolving from 
previous groups like DarkSide and 
BlackMatter. BlackCat is written in Rust, 
which indicates sophistication on the part 
of their developers. It enables them to 
target both Windows and Linux devices, 
and often evade detection by traditional 
security tools.BUSINES SM ODEL :BlackCat operates under a RaaS model, 
where developers offer malware to 
affiliates in exchange for a percentage of 
the ransom payments. They have gained 
recognition for their sophisticated double 
and sometimes triple extortion tactics. 
Recently, they escalated their tactics by 
including the filing of an SEC complaint 
against a victim for not disclosing a 
cyberattack.INN OVAT IV ET ECHNIQUES :BlackCat is notable for being the first 
ransomware group to create a public data 
leaks site on the open internet and for 
employing typo\-squatted replicas of victim 
websites to post stolen data, enhancing the 
pressure on victims.TA RGE TP ROFILE :They target a broad range of global 
entities including universities, government 
agencies, and companies in the energy, 
technology, manufacturing, and 
transportation sectors.Recent highly impacted targets include 
MGM Resorts International and Caesars 
Entertainment.ASSOCI AT E DG ROUPS :They are linked to discontinued RaaS 
groups like DarkSide and BlackMatter. 
Some speculate that it may be a rebranding 
of DarkSide or a successor to REvil.Typical Attack Chain:Initial Access:BlackCat is known to use OSINT (T1598\) and advanced SE tactics, often pretending 
to be legitimate IT staff. They do so to trick users into providing additional 
information. This is done with the aim of social engineering other individuals or 
acquiring credentials (T1586\), which can then be used to gain access to the system.Follow\-On Activities:Deploy legitimate software (e.g AnyDesk, Splashtop, Mega Sync, Plink,
and Ngrok) for remote access and to prepare for data exfiltration (T1041\)Create a connection to C2 servers such as Brute Ratel C4 or Cobalt Strike(T1071\)Deploy attack frameworks such as Evilginx2 to capture multifactorauthentication (MFA), login credentials, and session cookies (T1557\)Use access token manipulation (T1134\), or credentials from the DC,local networks, and backups (T1555\) to gain elevated credentials that
will enable enumeration and lateral movementExfiltrate system data through the C2 channel (T1041\), web services (T1567\),or alternative protocol (T1048\)Impact:BlackCat often extorts victims with the threat of releasing their exfiltratedsensitive data to other threat actors.They are known to encrypt all systems and files (T1486\) andor completelyerase content (T1561\).They may deface (T1491\) and inhibit system recovery (T1490\).Other Tools Seen:Mega.nz, Dropbox, Metasploit, POORTRY, STONESTOP, The Onion Router (Tor), 
sragent.exe, psexec32\.exe, version.dllANNUAL THREAT REPORT 2024Chapter 5Threat Actor Profiles1 8LockBitA LIASES :ABCD RansomwareE MERGENCE :September 2019LockBit is well known for its continuous evolution through 
versions 2\.0 and 3\.0\. They operate as a RaaS and have been 
known to recruit insiders from the companies they target. 
They tend to target healthcare facilities and schools, 
particularly those with Linux devices.ANNUAL THREAT REPORT 2024Chapter 5Threat Actor Profiles1 9LockBit TTPsInitial AccessT1189 Drive\-by CompromiseT1190 Exploit Public\-Facing ApplicationT1133 External Remote ServicesT1566 PhishingT1078 Valid AccountsExecutionT1059 Command and Scripting InterpreterT1059\.003 Windows Command ShellT1053 Scheduled TaskJobT1072 Software Deployment ToolsT1204 User ExecutionPersistenceT1547 Boot or Logon Autostart ExecutionT1133 External Remote ServicesT1574 Hijack Execution FlowT1053 Scheduled TaskJobT1078 Valid AccountsPrivilege EscalationT1548 Abuse Elevation Control MechanismT1134 Access Token ManipulationT1547 Boot or Logon Autostart ExecutionT1484 Domain Policy ModificationT1484\.001 Group Policy ModificationT1574 Hijack Execution FlowT1053 Scheduled TaskJobT1053\.005 Scheduled TaskT1078 Valid AccountsDefense EvasionT1548 Abuse Elevation Control MechanismT1134 Access Token ManipulationT1140 DeobfuscateDecode Files or InformationT1484 Domain Policy ModificationT1574 Hijack Execution FlowT1562 Impair DefensesT1562\.001 Disable or Modify ToolsANNUAL THREAT REPORT 2024Chapter 5Threat Actor Profiles2 0LockBit TTPsT1070 Indicator RemovalT1070\.001 Clear Windows Event LogsT1070\.004 File DeletionT1027 Obfuscated Files or InformationT1027\.002 Software PackingT1127 Trusted Developer Utilities Proxy ExecutionT1078 Valid AccountsCredential AccessT1110 Brute ForceT1003 OS Credential DumpingT1003\.001 LSASS MemoryDiscoveryT1083 File and Directory DiscoveryT1046 Network Service DiscoveryT1135 Network Share DiscoveryT1057 Process DiscoveryT1018 Remote System DiscoveryT1082 System Information DiscoveryLateralMovementT1570 Lateral Tool TransferT1021 Remote ServicesT1072 Software Deployment ToolsCommand and ControlT1095 Non\-Application Layer ProtocolT1572 Protocol TunnelingT1219 Remote Access SoftwareExfiltrationT1041 Exfiltration Over C2 ChannelT1021\.001 Remote Desktop ProtocolT1021\.002 SMBWindows Admin SharesT1567 Exfiltration Over Web ServiceT1567\.002 Exfiltration to Cloud StorageImpactT1485 Data DestructionT1486 Data Encrypted for ImpactT1491 DefacementT1491\.001 Internal DefacementT1490 Inhibit System RecoveryT1489 Service StopANNUAL THREAT REPORT 2024Chapter 5Threat Actor Profiles2 1E VO LUTION :LockBit has evolved significantly 
since its inception, with notable 
advancements seen in their 2\.0 and 
3\.0 versions. LockBit 2\.0 surfaced in 
June 2021, followed by 3\.0 in March 
1\. These evolutions include 
improved encryption methods, 
targeting strategies, and the 
introduction of innovative tools like 
"StealBit" for data exfiltration.BUSINES SM ODEL :LockBit operates as a RaaS group 
using double extortion tactics and 
offers ransomware to affiliates, 
sharing profits from the ransom 
payments.INN OVAT IV ET ECHNIQUES :They developed StealBit for 
efficient data exfiltration, and target 
Linux devices, focusing on ESXi 
servers, showcasing their adaptability 
and technical sophistication.TA RGE TP ROFILE :They predominantly target the 
healthcare and education sectors, 
with significant attacks in Brazil, 
India, and the United States.ASSOCI AT E DG ROUPS :They collaborate with various 
criminal groups and network access 
brokers, even recruiting insiders from 
targeted companies.Typical Attack Chain:Initial Access:LockBit affiliates typically use compromised servers (T1189\) or exploit external 
services (T1133\) such as RDP. LockBit has also been seen gaining access through 
phishing attempts (T1566\) and valid accounts (T1078\).Follow\-On Activities:Execute batch scripts (T1059\) or Chocolatey package manager (T1072\) to beginattack deploymentUse compromised user accounts (T1078\) and find additional accounts with tools 
such as Mimikatz (T1003\) to gain privilege escalation with which persistence can 
be established via scheduled tasks (T1053\) and autostart execution (T1574\)Evade detection and impair defenses (T1562\) by attempting to disable EDRprocesses using tools such as Backstab, Defender Control, GMER, PCHunter, 
PowerTool, Process Hacker, or TDSSKillerUse Splashtop Remote Desktop, Cobalt Strike (T1570\), and remote services(T1021\) for lateral movement throughout the networkConduct C2 using tools such as FileZilla, SOCKS5 TCP tunnels, and AnyDesk(T1219\)Exfiltrate data using tools like Rclone, FreeFileSync, or Mega (T1567\)Impact:LockBit encrypts Windows, Linux, and VMware instances, using AdvancedEncryption Standard (AES) with randomly generated keys to hold for ransom 
(T1486\).They change wallpapers and icons to custom LockBit 3\.0 ones (T1491\).They delete volume shadow copies (T1485\) and terminate processes andservices (T1489\) to reduce the likelihood of recovery.Other Tools Seen:Blister Loader, ExtPassword, LostMyPassword, SystInternals Prodump, 
ThunderShell, Plink, Atera RMM, ScreenConnect, TeamViewerANNUAL THREAT REPORT 2024Chapter 5Threat Actor Profiles2 2QakBotQakBot is a versatile botnet that offers a suite of tools, often 
setting the stage for Conti, Egregor, and others ransomware 
deployments. Despite government interference, QakBot 
continues to return with new, innovative tactics.ALIASES :Qbot, Quackbot, 
Pinkslipbot, TA570E MERGENCE :2008\. They are one of the 
longest\-standing threats 
in the cyber landscape.ANNUAL THREAT REPORT 2024Chapter 5Threat Actor Profiles2 3QakBot TTPsExecutionT1106 Native APIT1047 Windows Management InstrumentationDefense EvasionT1140 DeobfuscateDecode Files or InformationT1112 Modify RegistryT1027 Obfuscated Files or InformationT1027\.001 Binary PaddingT1027\.010 Command ObfuscationT1027\.011 Fileless StorageT1027\.006 HTML SmugglingT1027\.005 Indicator Removal from ToolsT1027\.002 Software PackingCredential AccessT1110 Brute ForceT1539 Steal Web Session CookieDiscoveryT1010 Application Window DiscoveryT1482 Domain Trust DiscoveryT1083 File and Directory DiscoveryT1135 Network Share DiscoveryT1120 Peripheral Device DiscoveryT1057 Process DiscoveryT1018 Remote System DiscoveryT1518 Software DiscoveryT1518\.001 Security Software DiscoveryT1082 System Information DiscoveryT1016 System Network Configuration DiscoveryT1016\.001 Internet Connection DiscoveryT1049 System Network Connections DiscoveryT1033 System OwnerUser DiscoveryT1124 System Time DiscoveryANNUAL THREAT REPORT 2024Chapter 5Threat Actor Profiles2 4QakBot TTPsLateral MovementT1210 Exploitation of Remote ServicesCollectionT1185 Browser Session HijackingT1005 Data from Local SystemCommand and ControlT1105 Ingress Tool TransferT1095 Non\-Application Layer ProtocolT1572 Protocol TunnelingExfiltrationT1041 Exfiltration Over C2 ChannelANNUAL THREAT REPORT 2024Chapter 5Threat Actor ProfilesTypical Attack Chain:Initial Access:QakBot has been known to be used by IABs to sell network access to other threat 
actors. Their preferred method is spear\-phishing with links or attachments (T1566\), 
which tends to be more time consuming than phishing attacks but has a better 
success rate.Follow\-On Activities:Gain a foothold using native tools such as JavaScript (T1059\.007\), PowerShell(T1059\.001\), Windows Command Prompt (T1059\.003\), scheduled tasks 
(T1053\.005\), and process injection (T1055\)Discover and move laterally to as many systems it can get access to through 
Network Share Discovery (T1135\), Network Connections Discovery (T1049\), 
exploitation of remote services (T1210\), and replicating throughout
discovered systemsCollect additional information such as Local Emails (T1114\.001\), Data fromLocal Systems (T1005\), and Browser Session information (T1185\), allowing for 
further targeting and exploitationEstablish C2 connections via Ingress Tools (T1105\), Protocol Tunnelling (T1572\),and External Proxies (T1090\.002\)Impact:Known for its initial access capabilities, QakBot often hands off its control to 
other threat actors before detonating at the impact stage. That being said, 
they are known to deliver ransomware deployments including Conti, Egregor, 
ProLock, REvil, MegaCortex, and Black Basta.Other Tools Seen:Visual Basic, Base64, Server Message Block, Dynamic Link Library (DLL) Side\-
Loading, masquerading file types, Microsoft Excel, Mobsync.exe, wermgr.exe, 
SOCKS5 protocol, ISO Files, MSIExec, Regsvr32, Brute Ratel C4, WMI2 5E VO LUTION :Initially a banking trojan, QakBot has 
transformed into a versatile botnet, 
constantly updating to include more 
sophisticated functionalities. In August 
2023, a government operation took 
down their infrastructure. By November, 
DarkGate and PikaBot appeared to be 
spinoffs. A month later, QakBot was back 
with novel tactics.BUSINES SM ODEL :QakBot is not limited to a single type of 
cybercrime. They offer a suite of tools for 
reconnaissance, lateral movement, data 
gathering, and exfiltration. They serve as 
a vector for delivering various malicious 
payloads.TA RGE TP ROFILE :QakBot focuses on global infrastructures 
with an emphasis on sectors like finance, 
emergency services, commercial facilities, 
and election infrastructure subsectors. 
Most recently, they targeted the 
hospitality industry.ASSOCI AT E DG ROUPS :They often set the stage for the 
deployment of human\-operated 
ransomware like Conti, ProLock, and 
Egregor, among others.Blackpoint Cyber Detains Qakbot 
Information\-Stealing MalwareSee how our Managed EDR solution 
detained Qakbot in under two minutes.REA DN OWANNUAL THREAT REPORT 2024Chapter 5Threat Actor Profiles2 6RedLine StealerA LIASES :No known aliasesE MERGENCE :March 2020RedLine Stealer has gained a reputation for its extensive 
information gathering and data exfiltration capabilities. It 
operates as a Malware\-as\-a\-Service (MaaS) and is used by a 
wide range of cybercriminals. RedLine attacks often target 
industries such as healthcare and manufacturing.ANNUAL THREAT REPORT 2024Chapter 5Threat Actor Profiles2 7RedLine Stealer TTPsInitial AccessT1659 Content InjectionT1189 Drive\-by CompromiseT1566 PhishingExecutionT1053 Scheduled TaskJobT1204 User ExecutionPersistenceT1053 Scheduled TaskJobPrivilege EscalationT1053 Scheduled TaskJobCredential AccessT1555 Credentials from Password StoresT1056 Input CaptureT1003 OS Credential DumpingT1539 Steal Web Session CookieT1552 Unsecured CredentialsT1552\.008 Chat MessagesDiscoveryT1087 Account DiscoveryT1217 Browser Information DiscoveryT1526 Cloud Service DiscoveryT1652 Device Driver DiscoveryT1083 File and Directory DiscoveryT1654 Log EnumerationT1057 Process DiscoveryT1518 Software DiscoveryT1614 System Location DiscoveryT1016 System Network Configuration DiscoveryANNUAL THREAT REPORT 2024Chapter 5Threat Actor Profiles2 8RedLine Stealer TTPsT1033 System OwnerUser DiscoveryT1007 System Service DiscoveryCollectionT1119 Automated CollectionT1005 Data from Local SystemT1039 Data from Network Shared DriveT1056 Input CaptureCommand and ControlT1659 Content InjectionT1105 Ingress Tool TransferExfiltrationT1020 Automated ExfiltrationT1041 Exfiltration Over C2 ChannelImpactT1657 Financial TheftANNUAL THREAT REPORT 2024Chapter 5Threat Actor Profiles2 9E VO LUTION :Since 2020, RedLine Stealer has 
continually updated. They have extensive 
information gathering and data exfiltration 
features, including the ability to load 
remote payloads.BUSINES SM ODEL :They operate as a MaaS, available on 
underground forums with different pricing 
tiers, paid for with cryptocurrencies.INN OVAT IV ET ECHNIQUES :They collect an array of data from
users browsers, including login 
information, auto\-fill form fields, and 
browser history. They use Simple Object 
Access Protocol (SOAP) Application 
Programming Interface (API) for C2 
communication and leverage Telegram
API for real\-time infection notifications.TA RGE TP ROFILE :They target a wide range of sectors, 
notably healthcare and manufacturing.ASSOCI AT E DG ROUPS :RedLine Stealer is distributed to a range of 
cybercriminals on the dark web, indicating 
a broad base of users rather than specific 
associated groups.Typical Attack Chain:Initial Access:RedLine got its start with phishing emails (T1566\) and has since expanded to 
malvertising (T1189\), free software, cheat codes, and other methods of tricking 
users into clicking on or installing software (T1659\).Follow\-On Activities:Steal stored browser information such as credentials, credit cards, and otherauto\-completed data (T1217\)Steal cryptocurrency wallets (T1005\)Steal baseline system information such as users, locations, operating system 
(OS) and software versions, hardware configurations, and installed security 
software (T1005 \& T1119\)Exfiltrate data over C2 connections configured during build with theRedLine Admin Panel (T1020 \& T1041\)Impact:RedLine Stealer has the ability to drop additional payloads (T1105\).They sell sensitive information to other threat actors for additionalfollow\-on exploitation.They are responsible for much of the market for stolen credentials.ANNUAL THREAT REPORT 2024Chapter 5Threat Actor Profiles3 0AkiraA LIASES :Akira RansomwareE MERGENCE :March 2023Akira is known for its distinctive, retro\-style Tor leak 
site, where their double extortion tactics are played out. 
They utilize leaked source code of Conti ransomware, 
suggesting collaboration of some sort. Akira typically 
targets Linux devices and VMware ESXi virtual machines.ANNUAL THREAT REPORT 2024Chapter 5Threat Actor Profiles3 1Akira TTPsInitial AccessT1190 Exploit Public\-Facing ApplicationT1133 External Remote ServicesT1566 PhishingT1199 Trusted RelationshipT1078 Valid AccountsExecutionT1059 Command and Scripting InterpreterPersistenceT1566\.001 Spearphishing AttachmentT1566\.002 Spearphishing LinkT1136 Create AccountT1136\.002 Domain AccountT1133 External Remote ServicesT1078 Valid AccountsPrivilege EscalationT1078 Valid AccountsDefense EvasionT1006 Direct Volume AccessT1562 Impair DefensesT1078 Valid AccountsCredential AccessT1562\.001 Disable or Modify ToolsT1003 OS Credential DumpingT1003\.001 LSASS MemoryANNUAL THREAT REPORT 2024Chapter 5Threat Actor Profiles3 2Akira TTPsDiscoveryT1083 File and Directory DiscoveryT1046 Network Service DiscoveryT1135 Network Share DiscoveryT1018 Remote System DiscoveryT1082 System Information DiscoveryT1016 System Network Configuration DiscoveryT1049 System Network Connections DiscoveryLateral MovementT1210 Exploitation of Remote ServicesT1570 Lateral Tool TransferT1021 Remote ServicesT1080 Taint Shared ContentCommand and ControlT1219 Remote Access SoftwareExfiltrationT1021\.001 Remote Desktop ProtocolT1021\.002 SMBWindows Admin SharesT1048 Exfiltration Over Alternative ProtocolT1048\.003 Exfiltration Over Unencrypted 
Non\-C2 ProtocolT1567 Exfiltration Over Web ServiceT1567\.002 Exfiltration to Cloud StorageImpactT1486 Data Encrypted for ImpactT1490 Inhibit System RecoveryANNUAL THREAT REPORT 2024Chapter 5Threat Actor Profiles3 3E VO LUTION :Although different from the Akira 
ransomware active in 2017, it uses the 
same .akira extension for encrypted files. 
Akira uses the leaked source code of Conti 
ransomware, demonstrating an evolution 
in its technical capabilities.BUSINES SM ODEL :Akira operates by performing double 
extortion with demands typically ranging 
from $200,000 to over $4 million.INN OVAT IV ET ECHNIQUES :Akira utilizes a unique retro\-styled Tor 
leak site, setting it apart in presentation 
and style. In September 2023, they 
exploited a zero\-day vulnerability 
(CVE\-2023\-20269\) in Cisco products to 
establish unauthorized VPN sessions, 
indicating an elevated level of technical 
sophistication.TA RGE TP ROFILE :Akira has expanded their targets to 
include Linux devices and VMware
ESXi virtual machines. Initially, they 
heavily impacted the healthcare industry. 
They are present predominantly in 
Canada and the United States.ASSOCI AT E DG ROUPS :Code similarities with Conti ransomware 
actors suggest Akira's collaboration 
or shared knowledge with these 
cybercriminal groups.Typical Attack Chain:Initial Access:Akira is a ransomware group that typically focuses on the follow\-on attack using 
credentials or access from affiliates or other threat actors. They seem to prefer 
utilizing VPN credentials but have also used phishing attacks (T1566\) and the 
exploitation of zero\-day vulnerabilities (T1190 \& T1133\).Follow\-On Activities:Create a backdoor domain account for persistent access (T1136\)Attempt to terminate any known running AV software (T1562\)Collect system (T1018\) and network information (T1016 \& T1049\)Use tools such as Mimikatz to gather additional credentials (T1003\)that may be useful for lateral movement with Living Off the Land Binaries 
(LoLBins) tools like RDP (T1021\)Use legitimate tools such as AnyDesk, Radmin, RustDesk, RClone,and FileZilla for C2 and exfiltration (T1219\)Impact:Akira uses a hybrid encryption algorithm for heightened impact (T1486\).They employ selective encryption to avoid directories and files thatmay affect its operation.They inhibit system recovery by deleting shadow copies (T1490\).Other Tools Seen:PowerTool, KillAV, PCHunter, SharpHound, AdFind, Advanced IP Scanner, 
MASSCAN, Cloudflare Tunnel, MobaXterm, Ngrok, WinSCPANNUAL THREAT REPORT 2024Chapter 5Threat Actor Profiles3 4In SummaryUnderstanding the key players and their methods
is essential for proactive, effective cybersecurity.
The distinct approaches of dominant threat actors, 
including BlackCat, LockBit, QakBot, RedLine Stealer, 
and Akira, highlight the need for targeted defensive 
strategies. With awareness of top tactics and dominant 
malicious actors under our belt, we can now look ahead 
to how to protect the most vulnerable industries and 
businesses. This full view of the cyberthreat landscape 
will help create a comprehensive security strategy for 
you to implement the rest of 2024\.ANNUAL THREAT REPORT 2024Chapter 5Threat Actor Profiles3 5Industry\-Specific 
Threat AnalysisThe threat actor groups we have just reviewed target a plethora of 
industries including education, hospitality, government, healthcare, 
and manufacturing. At Blackpoint specifically, we have seen certain 
industries get targeted with initial access attempts more than others. 
Why initial access, specifically? We encounter this tactic the most, as 
our SOCs job is to halt malicious actors before they gain entry.The most common methods for initial access include:Phishing attacksExploited vulnerabilitiesEmail compromiseThe use of stolen credentialsThese attempts often couple with the use of VPNs, which obscure 
crucial information like malicious locations and infrastructure, 
complicating detection and response. As we examine our top
attacked industry verticals, you will see that a heavy percentage of
the incidents center on initial access. We will break down other tactics, 
as well as initial access methods used. Awareness of who could be 
targeting you or your customers, as well as how they may do so, is 
crucial to fortifying your defenses accordingly.ANNUAL THREAT REPORT 2024Chapter 6Industry\-Specific Threat Analysis3 699% 
VPNs were used 
in over 99% of 
our cloud\-related 
incidents.Key Trends ObservedIn the following sections, you will note several trends:The technology sector is the most represented industry in our observations.VPNs are a common factor in most incidents across our top five industries.Initial access is the foremost tactic employed against these industries.Logins from high\-risk countries are the primary method of initial access in these cases.A few factors explain these trends. One, our partner base consists mostly of MSPs.
Two, our SOC is adept at countering initial access tactics, often neutralizing cyberthreats 
at this stage. Three, the frequent occurrence of logins from risky countries as a key initial 
access tactic is linked to the fact that VPNs often originate from these locations, where 
regulations and laws are less stringent.Percentage of Incidents
by Industry123456789Technology 
42\.44%Business Services 
13\.98%Healthcare 
4\.64%Financial Services 
4\.41%Manufacturing
3\.56%Construction 
3\.01%Energy 
2\.74%Retail
2\.42%Professional Services 
2\.32%10Real Estate 
2\.29%ANNUAL THREAT REPORT 2024Chapter 6Industry\-Specific Threat Analysis3 7A NNUA LT HREA TR EPOR T2 0 2 4Chapter 6Industry\-Specific Threat AnalysisTop Threats for the 
Top 5 Industries3 8\# 1I NDUSTR YTechnology78\.76%
VPN Usage
Within IncidentsDue to our partners primarily being MSPs and their customers,
the technology sector is our largest and most active industry, 
accounting for over 40% of our total incidents. They faced more 
execution, C2, lateral movement, impact, and exploit threats than
any other featured sector in this report. Regarding initial access tactics, 
they experienced the highest instances of RDP exploitation,
email compromise, and phishing attempts. It is worth noting 
that compared to the other industries, they dealt with the smallest 
percentage of initial access attempts and logins from high\-risk countries.6\.06%
Lateral
Movement4\.52%
Credential
Access53\.76%
Initial 
Access11\.66%
Execution9\.20%
C22\.15%
Impact.61%
OtherWhat makes them a desirable target?They are rich in intellectual property and cutting\-edge technologies.They have extensive user data and proprietary information.They integrate networks, increasing vulnerability to systemic attacks.Targeted Tactics53\.76%
Initial 
Access11\.66%
Execution9\.20%
C26\.06%
Lateral
Movement4\.52%
Credential
Access2\.15%
Impact.61%
OtherInitial Access Tactics64\.05% 
Login from Risky Country3\.00% 
Remote Access12\.27% 
Suspicious Login8\.13% 
RDP4\.71% 
API Abuse3\.85% 
Email Compromise12\.27%Suspicious Login8\.13%RDP4\.71%API Abuse3\.85%Email Compromise1\.71% 
Phishing1\.28% 
Other1\.00% 
Exploit1\.71%Phishing1\.28%Other1\.00%Exploit64\.05%Login from Risky Country3\.00%Remote AccessANNUAL THREAT REPORT 2024Chapter 6Industry\-Specific Threat Analysis3 9\# 2I NDUSTR YBusiness Services84\.07%
VPN Usage
Within IncidentsBusiness services, responsible for about 14% of incidents, encountered 
more initial access attempts and exfiltration attempts than technology, 
healthcare, financial services, or manufacturing. They also faced the 
most logins from high\-risk countries, but the least percentage of API 
abuse and email compromise, compared to the other sectors.6\.56% 
3\.98% 
What makes them a desirable target? 
C2
Credential
Access60\.42%
Initial 
Access
They have access to a wide range of corporate and customer data.4\.92% 
Lateral
Movement1\.87% 
Persistence6\.79% 
Execution1\.87% 
Impact.23%
ExltrationThey are connected to various sectors, offering broad attack surfaces.They house financial transactions and sensitive business information.Targeted Tactics60\.42%
Initial 
Access6\.79% 
Execution6\.56% 
C24\.92% 
Lateral
Movement3\.98% 
Credential
Access1\.87% 
Impact1\.87% 
Persistence.23%
ExltrationInitial Access Tactics73\.64% 
Login from Risky Country2\.34%
Other2\.33%
Email Compromise2\.33%
Remote Access8\.91%
Suspicious Login7\.75%
RDP2\.71%
API Abuse8\.91%Suspicious Login7\.75%RDP2\.71%API Abuse73\.64%Login from Risky Country2\.34%Other2\.33%Email Compromise2\.33%Remote AccessANNUAL THREAT REPORT 2024Chapter 6Industry\-Specific Threat Analysis4 0\# 3I NDUSTR YHealthcare87\.32%
VPN Usage
Within IncidentsHealthcare faced more persistence threats than the other four 
industries, but the least amount of C2 and credential access threats. 
Compared to the other sectors, they did not face as many phishing 
or exploitation attempts.55\.63%
Initial6\.34%
Execution4\.93%
C22\.82%
Lateral
Movement2\.11%
Impact2\.11%
Persistence1\.41%
Credential 
AccessAccessWhat makes them a desirable target? 
They hold sensitive personal health information.They are critical infrastructure yet are often under\-prepared for cyberthreats.They house high volumes of patient data and healthcare research.Targeted Tactics55\.63%
Initial 
Access6\.34%
Execution4\.93%
C22\.82%
Lateral
Movement2\.11%
Impact2\.11%
Persistence1\.41%
Credential 
AccessInitial Access Tactics67\.09%
Login from Risky Country3\.80%
Email Compromise16\.46%
Suspicious Login2\.53%
Remote Access5\.06%
RDP5\.06%
API Abuse5\.06%RDP5\.06%API Abuse67\.09%3\.80%Login from Risky CountryEmail Compromise16\.46%Suspicious Login2\.53%Remote AccessANNUAL THREAT REPORT 2024Chapter 6Industry\-Specific Threat Analysis4 1\# 4I NDUSTR YFinancial Services88\.72% 
VPN Usage
Within IncidentsThe financial services industry encountered more API abuse
than technology, business services, healthcare, or manufacturing. 
For the other sectors, it was the \#4 initial access threat, but 
for finance, it was \#2\. That said, it dealt with the least amount 
of suspicious logins, remote access attempts, and execution 
attempts. In fact, C2 was a more prominent threat to them than 
execution, which is unique to this sector.60\.15% 
Initial6\.02%
C24\.51%
ExecutionAccessWhat makes them a desirable target? 
They have direct access to financial assets and transactional data.3\.76%
Credential 
Access2\.26%
Lateral 
Movement1\.50%
OtherThey house sensitive customer information.They are highly reliant on digital platforms, increasing cyber\-risk exposure.Targeted Tactics60\.15% 
Initial 
Access6\.02%
C24\.51%
Execution3\.76%
Credential 
Access2\.26%
Lateral 
Movement1\.50%
OtherInitial Access Tactics71\.25%
Login from Risky Country3\.75%
RDP11\.25%
API Abuse10\.00%
Suspicious Login2\.50%
Email Compromise1\.25%
Remote Access71\.25%Login from Risky Country3\.75%RDP11\.25%API Abuse10\.00%Suspicious Login2\.50%Email Compromise1\.25%Remote AccessANNUAL THREAT REPORT 2024Chapter 6Industry\-Specific Threat Analysis4 2\# 5I NDUSTR YManufacturing83\.49%
VPN Usage
Within IncidentsManufacturing also uniquely faced more execution threats than 
C2 threats. They encountered the least amount of credential 
access attempts, but the most threats of impact. Within initial 
access, they had the highest number of suspicious login and 
remote access attempts, but the least amount of RDP abuse.
For the other four industries, remote access did not make the top 
three initial access tactics, but for Manufacturing, it came in third.58\.72%
Initial 
Access6\.42%
Credential 
Access 
What makes them a desirable target?8\.26%
C27\.34%
Execution2\.76%
Other1\.83%
Lateral 
MovementThey house industrial control systems and proprietarymanufacturing processes.They integrate with supply chains, providing multiple entry points.They house valuable trade secrets and operational data.Targeted Tactics58\.72%
Initial 
Access8\.26%
C27\.34%
Execution6\.42%
Credential 
Access2\.76%
Other1\.83%
Lateral 
MovementInitial Access Tactics67\.19%
Login from Risky Country3\.13%
API Abuse17\.19%
Suspicious Login4\.69%
Remote Access3\.13%
RDP3\.13%
Email Compromise1\.56%
Phishing67\.19%Login from Risky Country3\.13%API Abuse17\.19%Suspicious Login4\.69%Remote Access3\.13%RDP3\.13%Email Compromise1\.56%PhishingANNUAL THREAT REPORT 2024Chapter 6Industry\-Specific Threat Analysis4 3In SummaryTechnology, with a leading 42\.44% of incidents, was the most 
targeted industry, reflecting the extensive digital infrastructure 
and valuable data that MSPs house and protect. Following 
technology was business services and healthcare, indicating
a significant cyberthreat presence in service\-oriented sectors.
A notable pattern across industries is the predominance of 
initial access threats, underscoring the importance attackers 
place on gaining entry points.Following initial access, the second and third most common 
threats across all five industries were execution and C2\. Within 
initial access attempts, logins from high\-risk countries were the 
top threat across the board. These threats are often linked with 
VPN abuse, which we encountered in most incidents across all 
five industries.The diversity in threats thereafter highlights the customized 
tactics used by cybercriminals, adapting to the unique 
vulnerabilities of each sector. While threat actors do not 
discriminate, each industry must instill sector\-specific 
cybersecurity strategies. In order to detain these common 
threats, all businesses must adhere to best practices, educate 
their users on email threats, and instill advanced detection 
capabilities to stop threat actors immediately.ANNUAL THREAT REPORT 2024Chapter 6Industry\-Specific Threat Analysis4 4A NNUA LT HREA TR EPOR T2 0 2 4Chapter 7Predictions and Preparations for 2024Predictions and 
Preparations for 2024Now that we have reflected on the past years data, it is 
time to arm ourselves with lessons learned and prepare for 
the remainder of the year. In 2023, we witnessed a notable 
increase in cyber incidents overall, significantly focusing 
on initial access tactics, as well as cloud security threats. 
The growing number of incidents, especially from mid\-
year onwards, indicates cyberthreats are becoming more 
complex. This pattern suggests that in 2024, we may see a 
continued rise in advanced attacks, targeting credentials 
and exploiting various vulnerabilities, moving beyond 
VPN\-related incidents. This shift underscores the evolving 
nature of cyberthreats and the need for adaptive defense 
strategies across your hybrid work environments.4 5In 2024, we predict to seeLearn why Blackpoint Cyber 
is focusing on catching lateral 
movement, rather than malware, 
with our CEO, Jon Murchison.TUN EI NThe first three months 
of 2023 showed 
malware used 23\.8% of 
the time, whereas in 
the last three months, 
it was only present in 
9\.7% of incidents.The Abuse of Artificial Intelligence (AI):Used to enhance SE attacksUsed to create sophisticated, convincing phishing attacks anddeepfake videosUsed to make BEC appear more legitimateUsed to build more complex, automated attacksUsed in malware to adapt to defensesUsed to identify and target high\-value targets or exploitable vulnerabilitiesAn Increase in Infostealers and Malvertising:To increase search engine optimization (SEO) poisoningTo disguise malware as legitimate downloads in search resultsAn Increase in Sophisticated Tactics:To deploy more covert operations using LoLBins and RMM toolsTo depend less on malwareTo increase the difficulty in detecting threat actors within IT environments78\.78% 
of all incidents from 
December 2022 to 
November 2023 were 
cloud related.An Upward Trend in Ransomware Operations: 
To conduct more targeted and damaging ransomware attacksTo target a range of companies, from SMBs to Fortune 500 companiesTo deploy low\-effort attacks on high\-payoff targetsTo target high\-risk sectors including education, healthcare,financial services, and governmentCloud and Supply Chain AttacksTo exploit interconnected systems such MSPs with customers orcloud infrastructureTo exploit the subsystems that complex systems depend onANNUAL THREAT REPORT 2024Chapter 7Predictions and Preparations for 20244 6In SummaryThe cyberthreat landscape this year is predicted to be increasingly 
complex and sophisticated. AI is expected to play a pivotal role, 
enhancing SE attacks, creating more convincing phishing attempts, 
and facilitating BEC attacks. Infostealers and malvertising are likely 
to rise, exploiting SEO poisoning and masquerading malware 
in search results. The use of sophisticated tactics, like LoLBins 
and RMM tools, will make threat detection more challenging. 
Ransomware attacks are anticipated to become more targeted and 
damaging, potentially leveraging AI for vulnerability exploitation. 
We foresee a significant rise in cloud and supply chain attacks, due 
to their interconnected nature. This evolving threat environment 
underscores the need for adaptable defenses, a layered security 
approach, and a dedication to educating your user base.ANNUAL THREAT REPORT 2024Chapter 7Predictions and Preparations for 20244 7A NNUA LT HREA TR EPOR T2 0 2 4Chapter 8Cybersecurity Best PracticesCybersecurity
Best PracticesTo properly defend against the threat actors and 
cyberthreats we have covered in this report, you must 
empower your team members and customers to adhere 
to cybersecurity best practices. Much of the time, 
cyberattacks can be stopped through simple steps, such 
as using unique passwords, reviewing email links, and 
patching for vulnerabilities as soon as possible. Below 
you will find our suggested best practices.4 8Cybersecurity Best PracticesEmail and Online Security 
Raise awareness of phishing orspear\-phishing attacks, which involve
links or attachments.Raise awareness of malwareincorporated into online advertisements, 
known as malvertising.Be cautious about what you share onsocial media platforms, especially personal 
information and current locations.Data ProtectionNetwork and System SecurityEnable automatic updates where possible.Implement a continuous and frequentpatch plan.Review current configurations formisconfigurations or unauthorized changes.Prioritize patching once vulnerabilities aredisclosed.Phase out older, less secure authenticationmethods.Monitor logins over proxy and VPN tobypass conditional access geoblocking.Avoid storing passwords in web browsers.Maintain regular vulnerability assessments.Enforce password complexity requirements.Monitor logins from suspicious user agents.Encourage regular password changes.Implement Zero Trust principles.Avoid reusing passwords across accounts.Enforce identity and access control.Utilize MFA with authenticator apps, hardwaretokens, or biometrics.Always use secure Wi\-Fi connections. If inpublic, use a VPN or your phones Hotspot.Use secure payment methods, such as a creditcard or reliable third\-party service.Insider Threat Management 
Be mindful of potential insider threats.Manage application control and access.Adhere to the Principle of Least Privilege.Adhere to data handling best practices.Backup and InsuranceEnsure critical data is backed up regularly.Consider obtaining cyber liability insurancefor added protection.Security GuidanceAdhere to industry\-specific compliancerequirements.Abide by the DiD security framework.Follow the guidance of at least one widelyrecognized security frameworks.ANNUAL THREAT REPORT 2024Chapter 8Cybersecurity Best Practices4 9ConclusionThe cyberthreat landscape of the past year has undeniably 
reinforced the critical need for vigilant, proactive, and 
adaptive defense strategies to combat the sophisticated and 
interconnected array of threats targeting organizations, including 
SMBs. Amidst this landscape, the role of an MDR serves as an 
essential ally, offering the expertise, technology, and readiness 
needed to protect businesses assets and their people.Blackpoint prides itself on our ability to provide 247 monitoring, 
advanced analytics, and threat intelligence to ensure an ever\-
watchful eye over the businesses you work for and protect. We 
reduce the window of opportunity for attackers by detecting and 
responding to threats swiftly and effectively, all on your behalf. 
This is particularly crucial in an era where the cost and scale of 
cyberattacks continue to escalate, and where the time to detect 
and respond can be the difference between a minor security 
incident and a significant impact to revenue, reputation, and 
employees livelihood.Moreover, the expertise and resources that Blackpoint services 
provide alleviates the burden on internal IT teams, allowing 
businesses to focus on growth and innovation while ensuring 
their security posture is robust, dynamic, and aligned with the 
latest threat landscape. The path forward is one of partnership, 
with MDR\+R services at the helm, guiding organizations through 
the complexities of the modern cybersecurity landscape.This crucial integration into your organizations cybersecurity 
strategy is more than a protective measure, it is a strategic 
decision that empowers you to navigate the digital realm
with confidence and resilience.NE XTS TEP SIts time for advanced 
security, informed by 
security experts. Keep the 
conversation going with 
the researchers behind 
the report. Register for 
the webinar here.Or see how Blackpoints 
comprehensive 
ecosystem can arm your 
business and customers 
for success.GE TSTA RT E DANNUAL THREAT REPORT 2024Chapter 9Conclusion5 0GlossaryAES: Advanced Encryption StandardMFA: Multifactor authenticationAI: Artificial intelligenceAPG: Adversary Pursuit GroupAPI: Application Programming InterfaceAV: AntivirusBEC: Business Email CompromiseCISA: Cybersecurity and Infrastructure 
Security AgencyMS\-ISAC: Multi\-State Information Sharing 
and Analysis CenterMSP: Managed Service ProviderNSA: National Security AgencyOS: Operating systemOSINT: Open\-source intelligenceRaaS: Ransomware\-as\-a\-ServiceCSA: Cybersecurity AdvisoryRCE: Remote code executionC2: Command and controlRDP: Remote Desktop ProtocolDC: Domain ControllerRMM: Remote Monitoring and ManagementDiD: Defense in DepthSaaS: Software\-as\-a\-ServiceDLL: Dynamic Link LibrarySE: Social engineeringEDR: Endpoint Detection and ResponseSEO: Search engine optimizationIAB: Initial Access BrokerSOAP: Simple Object Access ProtocolIoC: Indicator of compromiseSSO: Single sign\-onLotL: live\-off\-the\-landSMBs: Small\- and medium\-sized businessesLoLBins: Living off the Land BinariesSOC: Security Operations CenterMaaS: Malware\-as\-a\-ServiceTTPs: Tactics, techniques, and proceduresMDR: Managed Detection and ResponseVPN: Virtual private networkMDR\+R: Managed Detection, Response
and RemediationWMI: Windows management 
instrumentationANNUAL THREAT REPORT 2024Chapter 10Glossary5 1ContributorsDavid Rushmer, Director of Threat ResearchC ONNEC TW IT HD AV I DO NL INKEDIN .Derick Peterson, Threat AnalystC ONNEC TW IT HD ERIC KO NL INKEDIN .Robert Russell, Senior Director
of Threat OperationsC ONNEC TW IT HR OBER TO NL INKEDIN .Alyssa Reed, Senior Content WriterC ONNEC TW IT HA LY SS AO NL INKEDIN .ANNUAL THREAT REPORT 2024Chapter 11Contributors