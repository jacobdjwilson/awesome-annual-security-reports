```markdown
# The Top 10 Most Prevalent MITRE ATT&CK® Techniques
## SneakThief and The Perfect Heist

## Table of Contents
- [Introduction](#introduction)
- [Top 10 MITRE ATT&CK Techniques](#top-10-mitre-attck-techniques)
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [Adopters in Threat Groups & Malware](#adopters-in-threat-groups--malware)
- [Recommendations for Security Teams](#recommendations-for-security-teams)
- [The Perfect Heist](#the-perfect-heist)
- [The MITRE ATT&CK Framework](#the-mitre-attck-framework)
- [Methodology](#methodology)
- [Top 10 MITRE ATT&CK Techniques](#top-10-mitre-attck-techniques-1)
  - [#1 T1055 Process Injection](#1-t1055-process-injection)
  - [#2 T1059 Command and Scripting Interpreter](#2-t1059-command-and-scripting-interpreter)
  - [#3 T1555 Credentials from Password Stores](#3-t1555-credentials-from-password-stores)
  - [#4 T1071 Application Layer Protocol](#4-t1071-application-layer-protocol)
  - [#5 T1562 Impair Defenses](#5-t1562-impair-defenses)
  - [#6 T1486 Data Encrypted for Impact](#6-t1486-data-encrypted-for-impact)
  - [#7 T1082 System Information Discovery](#7-t1082-system-information-discovery)
  - [#8 T1056 Input Capture](#8-t1056-input-capture)
  - [#9 T1547 Boot or Logon Autostart Execution](#9-t1547-boot-or-logon-autostart-execution)
  - [#10 T1005 Data from Local System](#10-t1005-data-from-local-system)
- [Limitations](#limitations)
- [References](#references)
- [About Picus](#about-picus)

## Introduction
The Red Report™ 2025, now in its fifth year of publication, delivers a detailed analysis 
of adversaries' most prevalent tactics, techniques, and procedures TTPs observed 
over the previous year. Compiled by Picus Labs, this year's report examined over 1 
million malware samples and mapped more than 14 million malicious actions and 11 
million instances of MITRE ATT&CK® techniques, providing organizations with 
actionable intelligence to counter todayʼs most prevalent and dangerous cyber threats.
The Red Report 2025 focuses on the top ten most frequently observed MITRE 
ATT&CK® techniques, presenting a roadmap for organizations to use to understand 
and prioritize their defenses. From process injection and credential theft to impairing 
defenses and data exfiltration over encrypted channels, these techniques represent 
the core strategies employed by todayʼs attackers to achieve their objectives.
The stakes have never been higher. Attackers are no longer just exploiting 
vulnerabilities but are conducting sophisticated, multi-stage operations that resemble, 
in many cases, a precision-planned burglary. This year's findings highlight a new era 
of adversarial sophistication in infostealer attacks, epitomized by malware like 
"SneakThief," which executed in a kill chain what has come to be known as "The 
Perfect Heist." Although the SneakThief malware is a fictitious name in this scenario, 
its attack patterns reflect real-world incidents. This advanced threat leverages stealth, 
persistence, and automation to infiltrate networks, bypass defenses, and exfiltrate 
critical data – all while leaving security teams unaware of their presence.
By analyzing real-world malware behavior, the Red Report gives cybersecurity teams 
the insights they need to strengthen their resilience against today's most pressing 
threats. This year's findings underscore the fact that only organizations embracing a 
proactive, threat-informed strategy, one that continuously validates controls and 
rapidly adapts to emerging threats, will be able to achieve true cyber resilience.
## Top 10 MITRE ATT&CK Techniques
The most prevalent ATT&CK techniques identified in 2024, ordered by 
the percentage of malware samples which exhibited the behavior.
## Executive Summary
Picus Labs processed more than 1 million pieces of malware collected between 
January and December 2024 to reveal a comprehensive view of the latest tactics, 
techniques, and procedures being employed by adversaries across the planet. Each 
detected TTP was classified via the MITRE ATT&CK® Framework, which resulted in the 
identification of over 14 million malicious actions. This provided Picus with extremely 
granular insight into the most commonly deployed techniques, shedding light on critical 
information concerning these constantly shifting attack strategies. Among these, the 
most striking is that this yearʼs Red Report reveals that malware, specifically strains 
targeting credential stores, increased from 8% in 2023 to 25% in 2024, thus a 3X 
surge in prevalence, a fact that highlights the popularity and success of this emerging 
threat.
The Red Report also reveals that 93% of 2024ʼs malicious actions were carried out 
using the top ten MITRE ATT&CK techniques. These findings will help security teams 
make better-informed decisions and concentrate on defending against the most 
prevalent threats in today's cyber environments.
The Perfect Heist:
Rise of Infostealers
Infostealers essentially set the standard for sophistication in 2024. The 
new “SneakThiefˮ type of malware, used in “The Perfect Heistˮ 
operations, featured multi-stage infiltration, process injection, encrypted 
communications, and boot persistence to infiltrate networks and stay 
hidden long enough to exfiltrate valuable data. Other attackers are 
increasingly combining stealth techniques with ransomware tactics, 
evolving into prolonged campaigns that rely on data theft, sometimes 
demanding ransoms solely to prevent data leaks without using encryption.
With over 200 techniques listed in the MITRE ATT&CK Framework, just the 
top ten account for more than 90% of observed malicious activity over 
the course of the year. Among the most prevalent are T1055 Process 
Injection), T1059 Command and Scripting Interpreter), and T1555 
Credentials from Password Stores). These top techniques underscore 
how attackers exploit native scripting tools, credential vaults, and 
encrypted channels to evade detection. Meanwhile, ransomware groups 
have doubled down on these methods, evolving into multi-stage extortion 
campaigns that threaten critical infrastructure, data, and reputations with 
unequaled precision.
Addressing these threats demands far more than a reactive, patchwork 
response. Security teams need a fundamentally different approach. 
Continuous security validation, behavioral analytics, and adaptive threat 
hunting are the new cornerstones of modern cyber defense. 
Organizations need to precisely align their controls with the most 
prevalent techniques, with a renewed focus on credential hardening. 
Traditional signature-based methods, while still useful, are no longer 
sufficient; security teams must shift toward detecting and responding to 
suspicious activity in real-time. As advanced and persistent threats 
continue to intensify, successfully countering them will depend on 
disrupting the attackers' capability before they become invisible, make a 
pivot, and strike again. The goal is clear: prevent infiltration, detect 
suspicious activities faster, and, if breached, mitigate adversariesʼ ability 
to burrow deeper into your environments.
## Key Findings
The Red Report 2025 shows how modern information stealer malware is evolving, 
highlighting increasingly sophisticated threat actors who pursue multistage operations 
as part of collecting and exfiltrating data in highly organized attacks. In turn, modern 
infostealers show how attackers have continued to evolve their methods to evade 
security defenses, remain persistent, and have maximum success.
Indeed, credential theft, encrypted communications, and process injection remain 
exceedingly popular, while ransomware and espionage continue morphing into 
longer-term and higher-impact campaigns.
1. The Rise of Perfect Heists:
Sophistication Meets Coordination
Todayʼs threats are about complex, multi-staged, structurally complex 
attacks, like "The Perfect Heist" perpetrated by the SneakThief malware. 
Featuring a combination of stealth, automation, and persistence, attackers 
can intrude into network systems, neutralize defenses, exfiltrate sensitive 
information, and remain hidden for longer and longer periods.
Attackers' ability to tailor their tactics to their surroundings speaks to a 
move toward precision-centric campaigns that work to create maximum 
destruction with minimum exposure.
2. Dominance of the Top 10 Techniques:
93% of Actions Linked to Top Techniques
Todayʼs threats are about complex, multi-staged, structurally complex 
attacks, like "The Perfect Heist" perpetrated by the SneakThief malware. 
Featuring a combination of stealth, automation, and persistence, attackers 
can intrude into network systems, neutralize defenses, exfiltrate sensitive 
information, and remain hidden for longer and longer periods. Attackers' 
ability to tailor their tactics to their surroundings speaks to a move toward 
precision-centric campaigns that work to create maximum destruction with 
minimum exposure.
3. Complexity Reaches New Heights:
14 Malicious Actions per Malware
Typical modern malware now performs an average of 14 malicious actions 
and 12 ATT&CK techniques per sample, presenting an evolving level of 
sophistication along with a notable increase in attackersʼ ability to 
orchestrate different techniques and methods, thus further increasing the 
level of complexity organizations need to employ for detection and 
defense.
4. Stealth Techniques Continue to Dominate:
Evasion and Persistence at the Core 
T1055 Process Injection, seen in 31% of analyzed samples, shows further 
movement to stealthier approaches as code injected into a legitimate 
process evades detection in many security solutions. In addition, T1059 
Command and Scripting Interpreter stands out among the top techniques 
that allow attackers to conduct malicious operations through native tools, 
such as PowerShell and Bash.
5. Credential Theft Fuels Lateral Movement:
Handing over the Keys to the Kingdom
Credential theft remains one of the most dependable techniques within 
adversary playbooks, with T1555 Credentials from Password Stores 
appearing in 25% of malware samples analyzed.
A growing trend in credential theft targets password managers, 
browser-stored credentials, and cached login data to gain lateral 
movement and afford attackers elevated privileges to sensitive systems. 
Those stolen credentials are later used for lateral movement and privilege 
escalation, allowing attackers to broaden their reach within the 
environments theyʼve compromised.
6. Encrypted Communication Becomes 
Standard:
The Whispering Channels
Adversaries have generally upped their game by relying on encrypted 
communication methods such as HTTPS and DNS over HTTPS DoH) while 
exfiltrating data or communicating with C2 servers. In this way, these 
"whispering channels" allow attackers to mask malicious traffic within 
legitimate network traffic patterns that bypass traditional monitoring tools.
And this is where ransomware has now changed into more of a multi-stage 
operation involving data exfiltration over encrypted channels.
7. Ransomware Evolves into a Multi-Stage 
Operation:
To Data Encryption and Beyond
T1486 Data Encrypted for Impact stays near the top of this yearʼs list as 
ransomware operators keep innovating their tactics. Threat actors are 
increasingly coupling encryption with advanced data exfiltration by using the 
T1071 Application Layer Protocol for more effective double extortions. Many 
of the most destructive high-profile ransomware attacks of 2024 and 2025 
were campaigns that were able to move into critical infrastructure at 
high-value organizations with increasing regularity.
8. Persistence Techniques Ensure
Long-Term Access:
Boot or Logon Autostart Execution on the Rise
T1547 Boot or Logon Autostart Execution is increasingly one of the leading 
methods by which malware outlives system reboots and removal attempts. 
Given the fact that SneakThief leveraged this, the trend of 
persistence-focused hackers gaining ground in hacked networks for longer 
terms isnʼt likely to be going anywhere anytime soon.
9. Real-Time Data Theft Accelerates:
Input Capture and System Discovery
Attackers leveraged T1056 Input Capture and T1082 System 
Information Discovery to accelerate data theft in real-time from their 
targeted organizations.
Along these lines, Infostealers employed keyloggers, screen capture 
utility, and audio interceptors for monitoring the activities at 
FinexaCore while keeping pace or outpacing the organizationʼs 
defensive efforts.
10. State-Sponsored Espionage Campaigns 
Intensify:
Advanced Persistent Threats on the Rise
T1082 System Information Discovery continues to be popular, and the 
growing trend of T1071 Application Layer Protocol outlines the continuing 
rise in cyber espionage campaigns. In 2024, threat actor groups such as 
APT29 from Russia, Volt Typhoon from China, and Lazarus Group from 
North Korea were targeting critical infrastructure, government agencies, 
and private enterprises with fresh resolve. Such campaigns emphasize 
long-term access and data theft to further their geopolitical objectives.
11. AI Hype vs. Reality:
Productivity Tools, Not Doomsday Weapons
Despite widespread speculation about AI transforming the malware 
landscape, our research shows no notable uptick in the use of AI-driven 
malware techniques. While adversaries use AI for efficiency gains 
(research, code debugging, phishing content creation), no novel 
AI-driven attack capabilities have emerged yet. AI enhances 
productivity but doesnʼt yet redefine malware.

## Top 10 ATT&CK Tactics:
Adopters in Threat Groups & Malware
| ATT&CK Technique | APT Group | Malware |
|---|---|---|
| T1055 Process Injection | GhostWriter (aka UAC-0057) [^1], RomCom APT [^2] | RedLine Stealer Malware [^3], Agent Tesla Stealer Malware [^4], SmashJacker [^5], SystemBS [^6], Lumma Stealer ([^7], [^8]),  IDAT Loader [^8], Zloader [^9], PythonRatLoader [^10], Strela Stealer [^11], REMCOS RAT [^12], GhostPulse [^13], CherryLoader [^14] |
| T1059 Command and Scripting Interpreter | BlackBasta Ransomware Group [^15], Earth Estries (a.k.a Salt Typhoon) [^16], Bianlian Ransomware Group [^17], Rhysida Ransomware Group [^18], Iranian Cyber Actors [^19], Everest Ransomware Group [^20], Lazarus Group [^21], Akira Ransomware Group ([^22], [^23]), CoralRaider Campaign [^24], UAT-5647 [^25], APT40, Volt Typhoon [^26], Void Banshee Campaign [^27], Water Hydra Campaign [^28] | Cthulhu Stealer [^29], CarnavalHeist Banking Trojan [^30], BeaverTail Backdoor [^21], PowerRAT [^31], Silver & PoshC2 Frameworks, Empire [^32], PowerSploit [^33], Nishang [^34], Posh-SecMod [^35], HeavyLift [^36], MacStealer [^37], PXA Infostealer [^38], Interlock Ransoware [^39], RustClaw, DustyHammock, and ShadyHammock [^25], Brightmetricagent, DarkMe RAT [^28], Androxgh0st [^40], WarmCookie (a.k.a BadSpace) [^41], Water Makara Campaign (downloading Astaroth InfoStealer) [^42], DarkGate [^43] |
| T1555 Credentials from Password Stores | Volt Typhoon [^26], Slow Tempest APT [^44] | RedLine Stealer, Cuckoo InfoStealer [^45], DarkGate [^46], ACR Stealer [^47], SCARLETELL [^48] |
| T1071 Application Layer Protocol |  | WezRat [^49], Glutton [^50], RevC2 Backdoor [^51], DarkGate [^52], LemonDuck [^53], Snake Keylogger [^54], Trojan.Win32.Injuke.mlrx [^55], MadMxShell Backdoor [^56], GammaLoad [^57], IOCONTROL [^58], WailingCrab [^59] |
| T1562 Impair Defenses | BlackCat Ransomware Group [^60], SeleniumGreed Campaign [^61], XMRig Cryptominer [^62], Fox Kitten [^63] | INC Ransomware [^64], WhisperGate Destructive Malware [^65], amsi_patch.ps1 [^66], RansomHub Ransomware [^67], EDRKillShifter Tool [^68], Mallox Ransomware [^69], Phobos Ransomware [^70], BPFDoor [^71], Ebury Rootkit [^72], RA World Ransomware [^73], SkidMap [^74] |
| T1486 Data Encrypted for Impact | RansomHub Ransomware Group [^75], Black Basta Ransomware Group [^76], Akira Ransomware Group [^77], ALPHV Ransomware Group [^78], Rhysida Ransomware Group [^79] | Phobos Ransomware [^80], RansomHub Ransomware [^75], Black Basta Ransomware [^76], Akira Ransomware [^77], ALPHV Ransomware [^78], Rhysida Ransomware [^79], AcidRain [^81], BiBi Wiper [^82], ESET Israel Wiper [^83], Handala's Wiper [^84], Kaden [^85], Zeppelin Ransomware [^86] |
| T1082 System Information Discovery | UAT-5647 [^25], Moonstone Sleet [^87] | Interlock Ransomware [^39], SingleCamper [^25], Cuckoo Malware [^88], A Rust-based macOS Backdoor [^89], Linux Malware [^90] |
| T1056 Input Capture | TaxOff [^91], DeceptionAds [^92] | DarkVision RAT [^93], TaxOffer featuring BgJobKeylogger class [^91], MacStealer [^37] |
| T1547 Boot or Logon Autostart Execution | Ferocious APT [^94], Earth Lusca APT (a.k.a Salt Typhoon) [^95], Winti Hacking Group [^96], Transparent Tribe (a.k.a APT36) [^97] | Phobos Ransomware [^70], Medusalocker Ransomware [^98], Snake Keylogger [^99], KamiKakaBot [^100], Mandela.exe [^101],  Snapekit Rootkit [^102], PipeMon [^96], DISGOMOJI [^103], StubPath [^104] |
| T1005 Data from Local System | Bianlian Ransomware Group [^17], Mustang Panda [^105],  Twelve Hacktivist Group [^106], CRON#TRAP Campaign [^107], APT36 [^97], Shedding Zmiy [^108] | Voldemort Backdoor [^109], GLOBSHELL [^97] |

## Recommendations for Security Teams
To build resilience against the techniques on the Red Report Top Ten and other popular attack techniques,
Picus Labs suggests security teams implement the following set of actions:
Establish Multi-Stage Attack Response Procedures
With "the Perfect Heist" style attacks increasing in popularity, security teams should 
employ multilayered defenses and response methods to identify and disrupt threats at 
multiple stages.
a) Create multi-stage incident response plans and train your people on them: 
Constantly develop and practice the response process to counter a variety of 
coordinated threat vectors.
b) Create scenario-based playbooks: Document specific steps to take in the face of 
well-observed TTPs and common multi-stage attack patterns to streamline incident 
handling.
c) Automate response on early-stage indicators: Strive for minimal dwell time and 
deploy capabilities to quickly identify and neutralize nascent attacks.
d) Establish communication channels for extended incident response: Plan for 
future roles and responsibilities so teams can more easily work together during 
long-running or unusually complex attacks.
Enhance Credential Protection and Management
Credential theft continues to be a core part of most adversaries' playbooks, so good 
credential protection remains very important. 
a) Secure Credential Stores: Protect password managers, browser-stored 
credentials, and cached login data T1555) with strong security measures. Monitor 
and audit all access to password managers and browser-stored credentials.
b) Implement MFA Implement multi-factor authentication MFA) on all systems and 
applications, but with an even greater emphasis on sensitive data storage systems. 
Store credentials in MFA-enabled encrypted stores.
c) Periodic Audit & Rotation of Credentials: Periodically audit users and permission 
levels. This also includes deleting outdated or unused privileges as well as those in 
dormant accounts. Impose periodic rotation of credentials with proper, just-in-time 
access controls.
d) Implement PAM Implement sophisticated privileged access management PAM 
solutions to securely monitor and manage privileged accounts and access.
Secure Encrypted Communications
As communications increasingly become fully encrypted, including attacker 
communications, security teams will want to shift to more sophisticated detection 
and prevention techniques.
a) Implement SSL/TLS Inspection: Focus on solutions that inspect encrypted traffic 
for malware without snooping into users' privacy.
b) DNS Traffic Monitoring: Invest in DNS monitoring and filtering solutions that 
identify and contain the use of DNS for data exfiltration and command and control 
and that provide DNS visibility and analytics over HTTPS DoH) traffic patterns.
c) Invest in NGFWs: Deploy reputable Next Generation Firewalls NGFWs capable of 
providing advanced threat protection, monitoring encrypted traffic for both known 
and unknown threats.
d) Apply Zero Trust Network Access: Rely on a proven Zero-trust network access 
model, where every access to network resources is authenticated, authorized, and 
encrypted upon every user ID, location, and device posture.
Focus on the Top MITRE ATT&CK Techniques
As 93% of all malicious activity in 2024 was assigned to the top 10 MITRE ATT&CK 
techniques, security teams should make sure they have the tools in place to combat 
these threats.
a) Memory Protection Mechanisms: Deploy a solution capable of detecting or 
preventing unauthorized memory manipulation to detect process hollowing and DLL 
injection.
b) Usage of Application Control: For PowerShell, Bash, and other scripting tools, 
enforce strict application control by either whitelisting applications or by denying 
script execution T1059.
c) In-Depth Monitoring of PowerShell and Bash: Allow for detailed logging of 
PowerShell and Bash activity using PowerShell Script Block Logging and Sysmon.
d) Use Behavior-Based Detection: Adopt security solutions providing 
behavior-based detection to move away from pure signature-based solutions.
Strengthen Anti-Ransomware Capabilities
With ransomware evolving into a multi-stage operation, enterprises need to prioritize 
both comprehensive prevention and recovery strategies.
a) Solution Implementation on Data Backup and Recovery: First, keep clean backups 
of highly critical data safe offline from production networks; periodically validate your 
backup restoration processes.
b) Ransomware-specific Detection and Response: Make sure you have tools in 
place that can detect actions and/or behaviors attributed to Ransomware; for 
example, many files being quickly encrypted all at once.
c) Regular Vulnerability Assessments: Implementing continuous scanning and 
automatically executing testing as quickly as possible.
d) Creating and Testing Your Incident Response Plan: Create and regularly test your 
detailed and dedicated incident response strategy specifically for all known forms of 
ransomware and zero-day occurrences.
Address Persistent Threats and Long-Term Access
With techniques like Boot or Logon Autostart Execution on the rise, focus on 
preventing and detecting persistent threats.
a) Endpoint Detect & Response (EDR Implementation): Make sure to implement an 
EDR solution that will enable you to determine & block unauthorized modifications to 
your startup protocol.
b) Regular System Audits: Periodically audit system configurations, startup items, 
and scheduled tasks for possible persistence mechanisms. Create hunting tasks with 
a focus on unauthorized autostart execution entries.
c) Apply Application Control: Use application whitelisting to deny unauthorized 
executables from running at system startup.
d) Deploy FIM Solutions: Use File Integrity Monitoring FIM) solutions to monitor 
unauthorized changes to critical system files and configurations.
Enhance Real-Time Data Protection
To counter the techniques of real-time data theft like Input Capture and System 
Information Discovery, youʼll need to apply appropriate data protection measures.
a) Deploy a DLP Solution: Utilize Data Loss Prevention DLP) solutions that can 
monitor and block data exfiltration in real-time. Create alerts for unusual patterns of 
data access or bulk data movement.
b) Enhance UBA Deploy User Behavioral Analytics UBA) solutions to help detect 
anomalous user activities that might denote compromised accounts or insider threats.
c) Data Encryption: Ensure that all sensitive data is encrypted both at rest and in 
transit.
d) Enhance Endpoint Controls: Strengthen endpoint controls to detect and block 
unauthorized capture of input.
Counter State-Sponsored Espionage Campaigns
To address the intensifying rate and complexity of state-sponsored espionage 
campaigns, implement advanced threat detection and mitigation strategies.
a) Threat Intelligence Platforms: Utilize threat intelligence feeds and platforms to 
stay updated on current TTPs employed by state-sponsored threat actors. 
b) Network Segmentation: Perform network micro-segmentation and minimize the 
attack surface for Advanced Persistent Threats APTs.
c) Deception Technologies: Honeypot technologies are among the deployment 
methods used to detect and analyze APT activities across your network.
d) Threat Hunting: Create proactive threat-hunting programs to detect and minimize 
advanced threats that might have bypassed detection.

## The Perfect Heist
A Tale of
Precision, Persistence, 
and Stealthy Intrusion
In this year's Red Report, we introduce a fictional scenario to illustrate 
how attackers blend the most critical MITRE ATT&CK techniques into 
“The Perfect Heist.ˮ Though FinexaCore company, SneakThief 
malware, and the Dark Circle threat group are purely fictional names, 
the pattern of their attack mirrors real-life attacks that we have 
observed and analyzed in depth. The goal of this hypothetical scenario 
is simply to explain how a threat like SneakThief gains control over a 
large modern enterprise's controls, hijacks its defenses, and finally 
manages to exfiltrate data while evading the organizationʼs existing 
security mechanisms.
It all started with just a minor glitch in FinexaCoreʼs 
network logs. The multinational company is a leader in 
AI-driven financial systems. Its cybersecurity team simply 
brushed the alert off as yet another harmless false 
positive. Yet, that was actually the initial sign of
“The Perfect Heist”
At the heart of it all was SneakThief, the malware used by one of the 
most infamous cybercrime syndicates, Dark Circle. It was, in fact, a 
symphony of malicious capabilities working in tandem to infiltrate, 
exploit, exfiltrate, and ultimately destroy targets.

![Image description]
SneakThief's intrusion was surgical. Their 
malware nestled itself in applications that were 
considered trusted, such as email clients, office 
productivity tools, accounting applications, and 
even FinexaCore's own proprietary AI tools.
At this point, SneakThief injected its code into 
these processes. This would have remained 
invisible, blending in unobtrusively with 
FinexaCoreʼs legitimate operations. In the 
meantime, employees innocently helped the 
malware spread during their daily work, all while 
it was silently siphoning data in real-time.
Process Injection:
Hiding in Plain Sight
#1

![Image description]
The next thing SneakThief did was try to find
the keys to the kingdom. It targeted password managers, browser-stored credentials, and cached login data. 
Using its state-of-the-art memory scraping techniques, it exfiltrated usernames and passwords for 
FinexaCore's most sensitive systems.
Those credentials literally opened everything that was left to plunder: cloud storage accounts, financial 
databases, and even the CEO's personal email. With each password it stole, SneakThief grew stronger, its 
reach growing deeper inside FinexaCore's digital vaults.
Credentials from 
Password Stores:
The Master Keys to 
Treasure
#3

![Image description]
SneakThief spoke to its operators over 
application layer channels that appeared to be 
just like any other legitimate piece of traffic. 
Camouflaging with HTTPS and DoH allowed it to 
exfiltrate data with impunity.
These “whispering channelsˮ guaranteed that 
SneakThiefʼs operators could continue issuing 
commands and extracting information without 
detection. FinexaCoreʼs security appliances, 
swamped by the massive amount of encrypted 
traffic, remained oblivious to the malicious 
intent flowing out of their network.
Application
Layer Protocol:
The Whispering 
Channels
#4

![Image description]
SneakThief knew that no matter how careful 
they were, an anomaly would eventually be 
detected by FinexaCoreʼs cybersecurity team. 
So, it began to impair defenses by first 
stopping antivirus software. It then tampered 
with EDR tools and manipulated logs to scrub 
any trace of its presence.
The analysts in FinexaCore eventually realized 
that they were under attack. All of their efforts 
to track down the breach failed, and most of 
their tools had been compromised. Their 
defenses had been brought down, one by one, 
by SneakThief.
Impair Defenses: 
Blinding the Watchdogs
#5

![Image description]
Command and 
Scripting Interpreter:
The Puppet Master
#2
Inside, SneakThief became the puppeteer:
it deployed scripts in PowerShell, Python, and 
Bash to automate its operations.
Running those scripts, SneakThief ordered 
the disabling of firewalls, the extraction of 
data, and the creation of backdoors through 
which it could access data in the future. It 
yanked the strings of FinexaCore's 
infrastructure masterfully, using the 
company's own systems against it.

![Image description]
When the defenses were down, SneakThief 
initiated the encryption of a trove of 
FinexaCoreʼs most significant documents, 
including financial records and client contracts.
SneakThiefʼs encryption of FinexaCoreʼs critical 
data crippled the fintechʼs operations and broke 
its clientsʼ confidence in the security software 
they thought was securing them all along.
Data Encrypted for 
Impact: 
Holding Secrets 
Hostage
#6

![Image description]
Dissatisfied with just their stolen files, SneakThief wanted more. Keyloggers capture every keystroke, 
logging passwords, financial transactions, and sensitive communications. Screen capture utilities 
watched what employees were up to while audio interceptors recorded voice calls and meetings.
Even as the executives at FinexaCore discussed their response to the breach, SneakThief listened in and 
collected vital intelligence to stay a step ahead. It was like the walls of the company had ears – and the 
ears belonged to SneakThief.
Input Capture: 
Stealing in Real Time
#8

![Image description]
In fact, SneakThief managed to survive by 
planting itself in the systems' startup processes. 
Every time a system rebooted, the malware was 
reinitializing to resume its operations. Even after 
FinexaCoreʼs IT team attempted to remove it, 
SneakThief kept returning, like a debilitating cold 
that just wonʼt go away.
Patience and persistence turned SneakThief into 
a virtually impossible to eradicate platform. It was 
the ghost haunting FinexaCore's systems, always 
there, always watching, always up to some sort of 
malicious behavior.
Boot or Logon 
Autostart Execution: 
The Persistent Thief
#9

![Image description]
SneakThief gathered data from the affected 
local systems, but not just any data: they stole 
everything from financial spreadsheets to 
datasets and personal files existing in 
employees' workstations.
The compressed, encrypted data reached the 
servers of Dark Circle after exfiltration. 
FinexaCore had never experienced such a big 
digital heist, and hoped, if they were able to stay 
afloat as a business and retool their security 
systems properly, never to have to go through 
such a dark and difficult time again.
Data From Local 
System:
Harvesting
the Crown Jewels
#10

![Image description]
System Information 
Discovery:
Mapping
the Treasure Trove 
#7
Behind SneakThief were careful operators. 
Once within FinexaCore, they mapped the 
network, noting high-value targets, and 
vulnerabilities. Because they were able to sit 
within the corporationʼs environment 
undetected for so long, they were able to 
inventory and examine every server, every 
database, and every endpoint within the 
company. 
Thanks to their detailed reconnaissance, 
SneakThief became capable of striking in a 
very focused manner: no single critical asset 
would slip through its malicious net. 

## The MITRE ATT&CK Framework
The figure above maps out the connections among ATT&CK's components. It shows 
how adversaries use "Techniques" from the framework to execute "Tactics," and 
categorizes adversary tools as "Software." The framework is a robust knowledge 
base, offering insights on each technique with "Mitigation" strategies and "Data 
Sources" for detection.
The framework also chronicles threat "groups" involved in intrusions and the 
"software" they deploy, encompassing malware and various tools. Currently, ATT&CK 
contains 163 groups and 826 pieces of software. 
With 44 "mitigations," ATT&CK advises on solutions to prevent technique execution. 
Detection is supported by 41 "data sources" with "data components", pinpointing 
data sources critical to identifying techniques.
ATT&CK's "campaign" structure catalogs intrusion activity over time with shared 
objectives, currently featuring 36 campaigns.
The MITRE ATT&CK Adversarial Tactics, Techniques, and Common Knowledge) 
framework is a globally accessible knowledge base of adversary tactics and 
techniques derived from real-world observations. This resource helps organizations in 
comprehending and mitigating the tactics, techniques, and procedures TTPs 
employed in cyberattacks.
In the MITRE ATT&CK framework, a "tactic"