# Bridewell Threat Intelligence: 2025 Cyber Threat Intelligence Report

## Table of Contents
- [Foreword](#foreword)
- [Executive Summary](#executive-summary)
- [The Scope of Our Research](#the-scope-of-our-research)
- [Adversary Infrastructure Tracking](#adversary-infrastructure-tracking)
- [Top 10 Tracked Threats](#top-10-tracked-threats)
- [Global Hosting Distribution](#global-hosting-distribution)
- [Offensive Security Tooling (OSTs)](#offensive-security-tooling-osts)
- [Cobalt Strike](#cobalt-strike)
- [Increased Adoption of Sliver and Brute Ratel](#increased-adoption-of-sliver-and-brute-ratel)
- [Supershell](#supershell)
- [Information Stealers](#information-stealers)
- [Lumma Stealer](#lumma-stealer)
- [Rise of Meduza Stealer](#rise-of-meduza-stealer)
- [Redline Stealer Resists Law Enforcement](#redline-stealer-resists-law-enforcement)
- [RATs](#rats)
- [Gh0stRAT](#gh0strat)
- [Quasar & Async RAT](#quasar--async-rat)
- [CNI SOC/ MDR Service Detection Analysis](#cni-soc-mdr-service-detection-analysis)
- [Information Stealer Landscape](#information-stealer-landscape)
- [Global Information Stealer Landscape](#global-information-stealer-landscape)
- [UK Information Stealer Landscape](#uk-information-stealer-landscape)
- [Information Stealers and RaaS Ecosystem](#information-stealers-and-raas-ecosystem)

---

## Foreword
“Our CTI Annual Report for 2025 shares insights from our malicious infrastructure tracking program, and intelligence gathered by our Security Operations Centre (SOC) and Managed Detection & Response (MDR) services. This report also spotlights the information stealer ecosystem, and presents significant and emerging threats in our research section.

Overall, 2025 has continued to mirror some of the trends seen in 2024. Based on activity we have observed as part of our malicious infrastructure tracking and through wider industry reporting, we have moderate confidence that threat actors will continue to innovate and improve capabilities to evade defences. A brief summary of these trends can be found in the executive summary, with more detailed information available later on in the report.

> Threat actors will continue to innovate and improve capabilities to evade defences.

Gavin Knapp, Cyber Threat Intelligence Principal Lead”

---

## Executive Summary
In 2024, our CTI team made significant improvements to our malicious infrastructure tracking capability, including tracking 10% more threat groups than in the previous year.

### Malicious Infrastructure
The 2024 analysis revealed notable new activity:
- 40% of all tracked malicious infrastructure is hosted within the United States (US) or China, a drop of 8% from 2023.
- A notable increase in Sliver and Brute Ratel command-and-control (C2) infrastructure, compared to a decrease in Cobalt Strike.
- Malware and tools closely linked to Chinese-nexus groups, such as ShadowPad, PlugX, Supershell, and Cobalt Strike, dominate the top 10 tracked threats.
- Lumma Stealer, Redline Stealer, StealC, and Meduza Stealer are the preferred information stealers of 2024.

### Information Stealers
- Law enforcement operations contributed to a drop in the volume of global compromises.
- Lumma Stealer, Redline Stealer, and StealC are the primary information stealers impacting the UK.

### EDRKillers
- Endpoint Detection and Response Killers (EDRKillers) surged across ransomware groups, with EDRKillShifter fuelling Ransomhub’s rise.
- Bring-Your-Own-Vulnerable-Driver (BYOVD) is becoming a trending technique.

### Fog Ransomware
- The emergence of Fog ransomware is notable for its significant overlap in Tactics, Techniques, and Procedures (TTPs) with Akira ransomware.

---

## The Scope of Our Research
It is important to understand that we leverage a specific set of open source and commercial tools which do not give us full coverage of host and network telemetry globally. Threat actors are also becoming more adept at obfuscating their C2 infrastructure which continues to present challenges in detecting malicious infrastructure with strong operational security.

---

## Adversary Infrastructure Tracking
Our adversary infrastructure program tracks threat groups in the PRE-ATT&CK stage leveraging various sources of telemetry to identify traffic from: Command-and-Control (C2) servers, botnets, RATs, initial access brokers (IABs), APTs, phishing, ransomware groups, open directories, TDS and ORB networks.

### Top 10 Tracked Threats
The top 10 tracked threats list for 2024 saw the removal of Qakbot and Raccoon Stealer due to law enforcement action. New to the top 10 are Panda C2, Brute Ratel, PlugX, and ShadowPad.

![Chart showing unique IPs returned by malware family: Cobalt Strike, Sliver, Metasploit, Burp, PlugX, SuperShell, Havoc, Panda C2, Brute Ratel, ShadowPad]

### Global Hosting Distribution
In 2024, nearly 24% of all infrastructure we tracked was hosted in the United States. China hosted nearly 18%.

### Offensive Security Tooling (OSTs)
Post-exploitation frameworks are essential components in the arsenal of both red teams and malicious actors. Our C2 tracking capability detected over 15,000 unique IP addresses associated with C2 frameworks in 2024.

### Cobalt Strike
Cobalt Strike accounted for 42% of all servers tracked by tools under the OST category. Of the Cobalt Strike servers tracked that aren’t redirectors, nearly 45% are hosted in China.

### Increased Adoption of Sliver and Brute Ratel
The cyber security landscape in 2024 showed clear indicators of a growing trend towards the adoption of alternative post-exploitation frameworks, particularly Sliver and Brute Ratel.

### Supershell
Supershell C2 utilises web services for its operations and offers features like remote shell access, file management, and memory injection. 62% of servers were hosted in China by the end of 2024.

---

## Information Stealers
Information stealers remain an ever-present threat, acting as the initial precursive cut into a network. Prominent groups such as LockBit, RansomHub, Akira, and Hellcat were commonly associated with infections initiated by information stealers.

### Lumma Stealer
Throughout 2024, we observed Lumma Stealer rising in prevalence as the most dominant stealer on the market today. A particularly prominent method involved the use of malvertising, where malicious ads redirect users to fake CAPTCHA pages.

### Rise of Meduza Stealer
Meduza Stealer has undergone substantial technical improvements, focusing on expanding its functionality and enhancing its stealth capabilities. In June 2024, Meduza Stealer was banned from underground marketplaces due to its lack of mechanisms to mitigate infections within CIS countries.

### Redline Stealer Resists Law Enforcement
Analysis of Redline Stealer’s infrastructure highlights that the majority of the backend infrastructure linked to the stealer is hosted in Russia (55%). Despite Operation Magnus in October 2024, our dataset suggests the threat actors simply moved to other locations to resume operations.

---

## RATs
Throughout 2024, we observed persistent RAT utilisation. Amongst our dataset, we saw Gh0stRAT topping the graph for most C2 servers, followed by QuasarRAT, Dark Comet, AsyncRAT, Nanocore, NJRAT, DCRAT and SectopRAT.

### Gh0stRAT
Gh0stRAT, a well-established malicious tool first identified in 2008, continues to pose a significant threat. During 2024, the top 5 countries hosting Gh0stRAT C2 servers were the United States, Germany, Greece, China, and Japan.

### Quasar & Async RAT
By the end of 2024, QuasarRAT and AsyncRAT infrastructure ranked highest amongst RATs tracked by Bridewell.

---

## CNI SOC/ MDR Service Detection Analysis
The most prominent C2 alert we observed in clients was for ApateWeb—a network made up of thousands of C2 domains containing embedded JavaScript redirectors.

---

## Information Stealer Landscape
The data for 2024 highlights a fluctuating but persistent volume of global compromises linked to information stealers. The year began with a peak in January, recording over 620,000 incidents.

### UK Information Stealer Landscape
Our analysis shows that Lumma Stealer (41.2%) and Redline Stealer (31.96%) account for the majority of information stealer infections in UK environments.

### Information Stealers and RaaS Ecosystem
Throughout 2024, we have observed a growing overlap between ransomware-as-a-service (RaaS) operations and information stealer malware. These malware strains enable attackers to harvest credentials, session tokens, and sensitive corporate data, which can then be leveraged to gain access to organisations before deploying ransomware.

---

to ransomware attacks and how different ransomware
groups utilise them.
2025 Cyber Threat Intelligence Report 33

Information Stealer Landscape
| Ransomware Incidents Involving Information  | Sectors 2024 |     |     |     |     |     |     |
| ------------------------------------------- | ------------ | --- | --- | --- | --- | --- | --- |
Stealers (2024)
The following section provides insights and figures to
illustrate how information stealers have contributed
| to ransomware incidents across different sectors and  |     | Technology |     |     |     |     |     |
| ----------------------------------------------------- | --- | ---------- | --- | --- | --- | --- | --- |
regions in 2024.
Business Services
| The first graph shows a breakdown of ransomware  |     | Healthcare |     |     |     |     |     |
| ------------------------------------------------ | --- | ---------- | --- | --- | --- | --- | --- |
incidents linked to information stealers across various
Manufacturing
industries. The technology sector (20.08%) is the
| most frequently targeted, followed closely by business  |     | Education  |     |     |     |     |     |
| ------------------------------------------------------- | --- | ---------- | --- | --- | --- | --- | --- |
| services (17.67%) and healthcare (11.65%). These        |     | Government |     |     |     |     |     |
industries store valuable credentials and sensitive
Financial
client data, making them prime targets for credential-
| harvesting malware before ransomware deployment. | rotceS | Energy |     |     |     |     |     |
| ------------------------------------------------ | ------ | ------ | --- | --- | --- | --- | --- |
Transportation/ Logistics
Agriculture and Food
Production
Public Sector
Financial Services
Hospitality and Tourism
The technology sector is the
| most frequently targeted,     | Consumer Services      |     |     |     |     |     |     |
| ----------------------------- | ---------------------- | --- | --- | --- | --- | --- | --- |
| followed closely by business  | Information Technology |     |     |     |     |     |     |
services and healthcare.
Retail
|     |     | 0   | 10  | 20  | 30  | 40  | 50  |
| --- | --- | --- | --- | --- | --- | --- | --- |
Ransomware Incidents
2025 Cyber Threat Intelligence Report 34

Information Stealer Landscape
Figure 1 highlights that business services, technology, Information Stealers Affecting UK 2024 UK Sectors Affected by Ransomware involving
government, and healthcare were the most affected Information Stealers 2024
sectors in the UK. This aligns with broader cyber
Figure 1 Figure 3
crime trends where attackers prioritise sectors with
a high volume of sensitive records and operational
dependencies.
16.67%
Figure 2 (CNI-related ransomware incidents) shows that 33.33%
Raccoon and StealC were the most common information
16.67% 50% 50%
stealers in ransomware cases affecting CNI. This suggests
that threat actors targeting CNI may be leveraging
compromised credentials obtained through information
33.33%
stealers before executing ransomware payloads.
Figure 3 reveals that UK government and healthcare
sectors were disproportionately affected by ransomware
Sector: Business Services Technology Government Healthcare Sector: Government Healthcare
campaigns involving information stealers. Given the
reliance on third-party vendors, extensive supply chains,
and large data repositories, these sectors remain highly Ransomware Incidents UK CNI 2024
attractive targets for cyber criminals.
Figure 2
50% 50%
Stealer Variant: Raccoon StealC
2025 Cyber Threat Intelligence Report 35

Information Stealer Landscape
Usage of Information Stealers Across Ransomware Groups Usage of Information Stealers Across Incidents 2024
Incidents (2024)
This bar chart provides insight into which ransomware
groups have been actively using information stealers as
part of their attack chain. lockbit3
ransomhub
LockBit3 and RansomHub are the most prolific users of
blackbasta
information stealers, incorporating strains such as Lumma
meduza
Stealer, Raccoon, and Redline Stealer into their infection
process. cactus
funksec
BlackBasta and Meduza Stealer also show strong
stormous
associations with Lumma Stealer and StealC, indicating
that these groups have deep ties to information stealer- hunters
based credential harvesting.
akira
alphv
The diversity of stealers across different ransomware
groups suggests that cyber criminals purchase stolen hellcat
credentials from various underground sources, rather dragonforce
than relying on a single supplier. The inclusion of Vidar
fog
and DarkCrystal among certain ransomware groups
suggests that some attackers are experimenting with less rhysida
commonly detected stealers, potentially to evade security
solutions that focus on more well-known strains. 0 10 20 30 40 50
DarkCrystal
2025 Cyber Threat Intelligence Report 36
puorG
erawmosnaR
Ransomware Incidents
Lumma Raccoon Redline StealC Vidar
Stealer Stealer

Information Stealer Landscape
Information Stealers Used Across Information Stealers Used Across Ransomware Incidents 2024
Ransomware Incidents (2024)
The timeline chart (right) tracks how the use
of different information stealers has evolved in
20
ransomware incidents throughout 2024.
Lumma Stealer saw a major surge in Q3 and Q4, 15
culminating in its highest activity levels in November
to December 2024. This suggests that Lumma
10
Stealer has become the information stealer of choice
for ransomware operators, likely due to evasive
capabilities, ease of deployment, and underground 5
market availability.
Redline Stealer maintained a steady presence
0
throughout the year, reflecting its continued popularity
2024 2024 2024 2024 2024 2024 2024 2024 2024 2024 2024 2024
among cyber criminals for credential harvesting. January February March April May June July August September October November December
Raccoon Stealer saw moderate fluctuations, with
peaks in May and September, potentially linked to Stealer Variant: DarkCrystal Lumma Stealer Raccoon Redline Stealer StealC Vidar
seasonal phishing campaigns and increased dark web
sales of stolen credentials.
Information Stealer Key Takeaways
StealC and Vidar showed lower but consistent usage, Our analysis of information stealer activity highlights
suggesting they are primarily used in targeted attacks the growing threat these malware families pose across
rather than widespread campaigns. global, UK, and CNI sectors. Our research underscores
the scale of credential theft, the evolving tactics used
by cyber criminals, and the direct risks to organisations
reliant on strong identity security.
2025 Cyber Threat Intelligence Report 37
stnedicnI
Date

Research
In this section, we’ll cover three research topics which Key Social Engineering Techniques in 2024
have persisted through 2024 which we predict with
high-moderate confidence will become more prevalent
into 2025. These topics include two ongoing trends
ClickFix
phishing kits and techniques and EDRKillers, along
with an emerging trend: fog ransomware. QR Code EvilGinx
Mamba2FA (BR-UNC-003)
Phishing Kits and Techniques
ONNX (BR-PHI-003)
getRandomWiki
Introduction
Phishing remains a highly lucrative threat, as seen by V3B Panel
the adoption of multiple new phishing kits and phishing
GlinTwist
techniques in 2024.
EvilProxy
2FA has dominated the adversary-in-the-middle (AiTM) Sneaky2FA
space. The phishing kit has led to thousands of ongoing
BRC-UNC-005
campaigns targeting Microsoft 365 and bypassing Gmail
SniperDZ
accounts. These stolen cookies enable attackers to
circumvent multi-factor authentication (MFA), leading Butchershop
to unauthorised access of a user’s accounts, systems,
Tycoon2FA
and cloud services, effectively negating even layered
security defences.
0 2000 4000 6000 8000 10000
ClickFix
Of particular importance is ClickFix, a highly industrious
technique favoured by numerous threat actor types and Our analysis in 2024 revealed the use of it in intrusions
currently being adopted at an accelerated rate. It is now by three highly developed nation-state APT groups.
directly responsible for facilitating diverse motive initial Our assessment is that its highly likely that this will
access operations on a global scale. become a readily deployable social engineering strategy
for threat actors of all sizes throughout the rest of 2025,
and we strongly anticipate increased adoption and
attack volume.
2025 Cyber Threat Intelligence Report 38
taerhT
Campaigns

Research
ClickFix
ClickFix campaigns
ClickFix is a phishing technique used by multiple threat
groups to socially engineer users into running malicious 2000
scripts on their machines. ClickFix deceives users into
directly downloading and running malware, avoiding
web browser involvement in the download process and 1500
eliminating the need for manual file execution, thereby
bypassing web security and appearing less suspicious.
1000
First tracked in the community in early 2024, it remained
a steady threat in 2024 with large spikes into early
2025. However, this is not the true picture of threat 500
actor adoption as this shifted many times from a few
dedicated cyber crime groups to global cyber criminal
activity and even nation-state APTs. 0
March April May June July August September October November December January February March
2024 2024 2024 2024 2024 2024 2024 2024 2024 2024 2025 2025 2025
Date
ClickFix deceives
users into directly
downloading and
running malware.
2025 Cyber Threat Intelligence Report 39
sngiapmaC

Research
There have been many variations so far of this
technique, beginning with fake errors within a Word
document to fake CAPTCHA within Cloudflare. Whilst
there has been a spread of diverse targeting such as
utilising fake browser alerts, we have also seen groups
using this highly successful lure to go after specific
sectors and customers such as the transportation sector
and booking.com.
We have also seen groups
using this highly successful
lure to go after specific
sectors and customers such
as the transportation sector
and booking.com.
2025 Cyber Threat Intelligence Report 40

Research
Below showcases a timeline into the specific variants over the year period from March 2024-March 2025.
Timeline of ClickFix variants
Fake code securty
issues in GitHub, fake
Facebook browser
issues, specific fleet
|     |     |     | management lures |     |     |     | Clearfix - |
| --- | --- | --- | ---------------- | --- | --- | --- | ---------- |
booking.com
Fake
Fake CAPTCHA,
|     | Fake browser  |     |     |     | verification  |     |     |
| --- | ------------- | --- | --- | --- | ------------- | --- | --- |
fake Google
| Fake Word  | alerts |     |     |     | step-ups, fake  | Fake |     |
| ---------- | ------ | --- | --- | --- | --------------- | ---- | --- |
Meet conference
| doc errors |     |     |     |     | web3 | Cloudflare -  |     |
| ---------- | --- | --- | --- | --- | ---- | ------------- | --- |
hardware errors
|     |     | Fake  |     |     |     | CAPTCHA |     |
| --- | --- | ----- | --- | --- | --- | ------- | --- |
popup
windows
| Mar  | May | Jun | Aug | Sep | Dec | Feb  | Mar |
| ---- | --- | --- | --- | --- | --- | ---- | --- |
| 2024 |     |     |     |     |     | 2025 |     |
2025 Cyber Threat Intelligence Report 41

Research
Notable Events in ClickFix Variants
Originally being utilised in cyber crime with TA571, we
have seen a much wider adoption by nation-state groups
In March 2024, TA571 executed phishing campaigns with such as MuddyWater (Iran), APT28 (Russia), and DPRK
HTML attachments designed to appear as Microsoft Word intrusion sets namely Contagious Interview and Kimsuky.
documents. These attachments displayed deceptive error ClickFix also continues to be persistently used across
messages to lure users into copying and running malicious information stealers. We are yet to see this play out with
PowerShell code that deployed malware. May 2024 saw ransomware intrusions at this time, which we believe is
a threat actor named ClearFake adopt a new social a natural avenue for delivery with or without the use of
engineering scheme, ClickFix, to trick users into running initial access brokers.
malicious PowerShell via fake web browser alert pop-ups
on compromised websites.
August 2024 had ClickFix operating within a large
infrastructure of fake CAPTCHA webpages to deliver
payloads, with redirection occurring from malicious
distribution networks, including fake cracked software
websites.
September 2024 found ClickFix being used against
North American transport/ logistics, specifically
impersonating transport and fleet management software
like Samsara, AMB Logistic, and Astra Transport
Management Software (TMS) to deliver malware (Lumma
Stealer initially, later DanaBot). Users inadvertently ran
malicious PowerShell after trying to fix software errors.
During March 2025, Storm-1865 specifically used
ClickFix against booking.com customers using fake
CAPTCHA. The command downloaded and launched
malicious code through mshta.exe.
2025 Cyber Threat Intelligence Report 42

Research
It should also be highlighted that MuddyWater
has previously deployed ransomware with other  Timeline of threat actors using ClickFix
destructive attacks and may begin to use it more
regularly. Moonstone Sleet, a DPRK-nexus group
who was observed deploying ransomware in
|     |     |     | DarkGate,  |     |     | UAC-0001 |     |     |
| --- | --- | --- | ---------- | --- | --- | -------- | --- | --- |
2024, shares several techniques with Contagious  Lumma Stealer (Forest
Blizzard, APT28),
Interview campaigns. With the shared tooling and
UAC-0050,
infrastructure overlaps in North Korea, there may be
Matanbuchus,
adjacent groups to Contagious Interview beginning  AmosStealer
to implement ClickFix as well.
|     |     |     |     | Lumma Stealer,  |                   | Lazarus -   |     |              |
| --- | --- | --- | --- | --------------- | ----------------- | ----------- | --- | ------------ |
|     |     |     |     | Scamquerteo,    |                   | Contagious  |     | Storm-1865,  |
|     |     |     |     | Slavic Nation   | TA571 delivering  | Interview   |     | MuddyWater   |
|     |     |     |     | Empire (SNE)    | Xworm,            |             |     |              |
TA571
NetsupportRAT,
delivering
Brute Ratel,
|     | Matanbuchus | Clearfake |     |     |     |     | Kimsuky,  |     |
| --- | ----------- | --------- | --- | --- | --- | --- | --------- | --- |
Latrodectus
ClearFake
VidarStealer
|     | Mar | May | Jun | Jul Aug | Sep | Oct Jan | Feb | Mar |
| --- | --- | --- | --- | ------- | --- | ------- | --- | --- |
It should also be highlighted
| that MuddyWater has  | 2024 |     |     |     |     | 2025 |     |     |
| -------------------- | ---- | --- | --- | --- | --- | ---- | --- | --- |
previously deployed
ransomware with other
destructive attacks and may
begin to use it more regularly.
2025 Cyber Threat Intelligence Report 43

Research
Notable Threat Actors using ClickFix
In October 2024, UAC-0001 (APT28, Forest Blizzard)
targeted the Ukrainian government mimicking a Google
spreadsheet.
January 2025 saw ClickFix being used via Lazarus’s
established Contagious Interview operation. This
involved inviting candidates to a fake Willo Video
Interview where they attempted to execute code on
the users’ machines under the guise of fixing a falsely
blocked camera/ microphone by the web application.
February 2025 had Kimsuky (Emerald Sleet, VELVET
CHOLLIMA) pretending to be South Korean government
officials. The group were attempting to have victims
open up Powershell terminals as an administrator to
download a remote desktop tool for data exfiltration.
Finally, in March 2025, MuddyWater (Mango Sandstorm)
were seen to be using ClickFix targeting the Armenian
Police website delivering RMM tools.
2025 Cyber Threat Intelligence Report 44

Research
EDRKillers, and EDRKillShifter As a result, EDRKillers can terminate/ manipulate August saw the emergence of Ransomhub’s
EDR processes, facilitate ransomware deployment EDRKillShifter, designed to deliver configurable
Introduction and ultimately prevent alerts from reaching security vulnerable drivers. September saw Cicada3301 utilise
administrators resulting in undetected attacks. EDRSandBlast, which exploits a signed, vulnerable driver
EDRKillers are advanced tools that aim to subvert
to disable EDR and Local Security Authority Subsystem
detection and disable Endpoint Detection and
Adoption Service (LSASS) protections using both kernel and user-
Response (EDR) capabilities. They have in particularly
Throughout 2024, threat actors increasingly adopted level evasion techniques.
become a trend in ransomware operations such as
diverse EDR disabling tools. In January, Mimic
Ransomhub, AvosLocker, BlackCat, LockBit, Royal
Ransomware deployed Defender Controller. February October saw the abuse of EDRSilencer, a red team tool,
Ransomware, Meduza Stealer, BlackByte, and
saw a surge in activity, with Phobos Ransomware utilising to create WFP filters blocking outbound EDR traffic.
Circada3301, with EDRKillers becoming more available
Process Hacker, Universal Virus Sniffer, and PowerTool,
through the RaaS ecosystem.
alongside ALPHV ransomware employing POORTRY and Simultaneously, Embargo Ransomware adopted
STONESTOP to terminate security processes. MS4Killer, another BYOVD tool. November brought
EDRKillers achieve their goals by exploiting vulnerable
reports of an extortion group deploying “Disabler,”
drivers, manipulating Windows Filtering Platform (WFP),
By April, Masscan Ransomware was observed using an AV/EDR bypass tool with strong similarities to
and altering kernel structures. Techniques such as NT
HRSword. May marked a significant shift, with BlackByte EDRSandBlast.
Layer Dynamic Link Library (NTDLL) unhooking and
ransomware operators loading a bespoke vulnerable
system call (syscall) manipulation pose a serious threat
driver —RtCore64.sys— during intrusions. This The rise of BYOVD, coupled with Ransomhub’s 2024
to allowing undetected malware to run.
exemplified the broader Bring-Your-Own-Vulnerable- dominance, makes EDRKillShifter the most substantial
Driver (BYOVD) technique, a Living-Off-The-Land (LOTL) ransomware threat.
In 2024, we saw wider adoption of dedicated
tactic favoured by many actors to evade detection by
sophisticated EDRKillers such as AVNeutralizer (AuKill),
blending in with legitimate system behaviours.
EDRKillShifter, EDRSandBlast, EDRSilencer, MS4Killer,
and Disabler.
July witnessed FIN7 marketing their AVNeutralizer
(AuKill) tool on dark web forums, capable of inducing
Other less advanced toolsets are also still being used
Denial-of-Service conditions that impeded vital EDR
across ransomware attacks like Defender Controller
process calls. Notably, AvosLocker, BlackCat, LockBit,
and Universal Virus Sniffer. We are also continuing to
Royal Ransomware, Meduza Stealer, and BlackByte have
see legitimate tools being installed such as HRSword,
all employed AVNeutralizer.
GMER, PowerTool and Process Hacker to force EDR
process terminations.
2025 Cyber Threat Intelligence Report 45

Research
EDRKillShifter Key Takeaways
In August, Ransomhub, the most prevalent ransomware In Stage 1, the file unpacks and executes a malicious Our analysis indicates a high probability of escalated
group of 2024, began utilising a new tool – embedded resource directly into memory. Under EDRKiller deployment within ransomware operations,
EDRKillShifter. Despite starting operations in February, inspection, the Portable Executable (PE) file contains subsequent to observed successful intrusions
it was in August that they outlined their desire to be a unique data values such as Company Name: “ARK,” File worldwide. We further anticipate that BYOVD
global player and became the third most prolific group description: “Loader Config,” and InternalName: “Loader. methodologies will represent a key trajectory for threat
in 2024 at that time. exe.” All samples require a 64-character based password actors throughout the rest of 2025, facilitating broader
passed to the commandline to execute into memory.
exploitation.
The group leveraged expertise from affiliates and
operators in the marketplace, namely BlackCat/ALPHV, Spawned file events from the executable were
to enhance their intrusions. With this shared portfolio of observed, which we reviewed for detections. This logic
knowledge, TTPs and capability from BlackCat/ALPHV was taken because there was a decryption routine
and other groups, it was clear that they would not only which creates a file name config.ini, and other file
get ahead of other groups, but become a leader who events from this were expected.
develop novel practices such as their highly successful In Stage 2, the driver drops. We identified that the
EDRKillshifter tool. EDRKillShifter drops a randomly named ‘.sys’ driver into
‘C:\Users\AppData\Local\Temp. We were also able to
Technical Analysis gather a list of known malicious vulnerable drivers. This
From Darkweb forums, we were able to view the allowed us to develop the driver dropping detection.
targeted EDRs by EDRKillShifter. The list covered We additionally added a competing rule for executions
many common EDRs such as Crowdstrike, Microsoft at the commandline for the “Killer” executable with
Defender, TrendMicro and SentinelOne. The malware parameters such as “-pass” containing drivers with the
operates in three stages designed to first deliver and pattern matching expression that was discovered.
decrypt a malicious embedded resource, which is then
executed in memory. In Stage 3, the driver exploitation elevates privileges to
disable the EDR. EDRKillShifter creates a new service
Following this, EDRKillShifter then drops the chosen, on the victim host for the newly dropped driver and
vulnerable but legitimate driver. Finally, it exploits the then starts the service to load the new driver. The
driver to gain higher privileges to unhook and disable malware then enters a loop which enumerates running
the chosen EDR tool. processes and terminates them if the process name
matches a list of hardcoded process names.
2025 Cyber Threat Intelligence Report 46

Research
Rising Prospect: Fog Ransomware
Fog ransomware count by sectors
Introduction
While 2024 saw significant law enforcement victories
against major cyber criminal operations, the emergence
of Fog Ransomware underscores the persistent evolution While 2024 saw significant
of digital threats. Notable actions, including Operation
law enforcement victories
Cronos against LockBit and the disruption of Warzone
against major cyber criminal
RAT infrastructure, demonstrated a concerted global
operations, the emergence of
effort to combat threat actor intrusion.
Fog ransomware underscores
the persistent evolution of
Targeting and Broad TTPs
digital threats.
Fog ransomware has been observed targeting primarily
US educational institutions, though broader victimology
reveals attacks across business services, manufacturing,
government, and education sectors.
This ransomware variant, a member of the STOP/DJVU
family first identified in November 2021, exhibits notable
similarities to Akira ransomware. Specifically, shared Energy Agriculture & Food Production
infrastructure, overlapping tactics, techniques, and Financial Education
procedures (TTPs), and similar initial access methods Hospitality and Tourism Government
have been observed. Healthcare Manufacturing
Technology Business Services
Transportation/ Logistics
Given Akira’s significant activity and ranking as a top 5
ransomware threat in 2024, the emergence of Fog was
closely monitored.
2025 Cyber Threat Intelligence Report 47

Research
Further analysis reveals a connection between Fog A Noteworthy Tactical Shift
affiliates and Storm-0844, a known Akira ransomware Fog’s TTPs have evolved to include source code
affiliate. This connection suggests a shared infection exfiltration from GitLab and the public disclosure of
chain, with initial access commonly achieved through victim IP addresses. This newly adopted method poses
the exploitation of VPN vulnerabilities and the use of a risk to intellectual property, software security, and
valid credentials. business continuity, impacting diverse industries. This reflects a trend since 2023, where initial access
brokers like Trickbot and Qakbot exploited Esentutl, a
The targeting of educational institutions likely stems Exposed source code provides attackers with legitimate Windows utility, as a Living-Off-The-Land
from their perceived vulnerabilities, including limited opportunities for security exploits, corporate espionage, Binary (lolbin) to facilitate browser credential theft.
cyber security budgets and the potential for high-value and financial gain. We anticipate that its likely they will
data exfiltration. However, victimology indicates a wider deliver this as part of future triple extortion attempts. Key Takeaways
reach, with business services, manufacturing, and We can expect to see further development of Fog
government also heavily targeted. Noteworthy Technical Observation: ransomware, including potentially new variants and
Technique Doppelgänger expanded targeting. We expect the group be a major
Geographically, 50% of attacks targeted the USA, with T1555.003: Credentials From Password Stores: player into 2025. As ransomware groups continue to
Germany next at approximately 10%. The rapid evolution Credentials From Web Browsers share and refine their techniques, the lines between
of ransomware groups, and the sharing of TTPs, different families may blur, making attribution and
highlights a rise in the enterprise of cyber crime, affiliate In Fog Ransomware intrusions, operators were observed defence more challenging. Additionally, the increased
programs, and ransomware as a service (RaaS). using the legitimate Microsoft utility, “Esentutl.exe,” to use of affiliate programs may lead to a wider distribution
collect and back-up copies of sensitive login data stored of attacks, targeting a broader range of sectors.
Observed post-exploitation activities include the use on victim host machines.
of common exploitation frameworks such as Metasploit
and Cobalt Strike, alongside legitimate remote access Further analysis also revealed that this credential
tools like AnyDesk and SplashTop. Data exfiltration is access technique is similar, if not identical, to the
conducted using tools such as Rclone and cloud storage commands used within intrusions conducted by Akira
platforms like Mega and FileZilla. To hinder recovery ransomware operators.
efforts, defence evasion techniques, including volume
shadow copy deletion via custom Fog ransomware In these attacks, Akira operators used this technique to
payloads, are employed. prepare data for exfiltration.
2025 Cyber Threat Intelligence Report 48

Outlook for 2025
The following sections cover key cyber threat Centralise monitoring for threat detection: Onboard Continuously monitor for vulnerabilities: Edge
intelligence observations as we move further into 2025. logs for edge devices into security monitoring programs. devices need to be continuously monitored for new
Define use cases to detect device compromise such vulnerabilities. When zero-day vulnerabilities are
Edge Devices and Vulnerability Exploitation as suspicious file creation, modification, or unexpected announced or identified on an edge device patching
In 2024, we observed numerous attacks against edge behaviour. Where device logs do not provide the the issue is not enough. A compromise assessment
devices across our managed detection and response opportunity for granular use cases, implement use should be performed on the edge device to identify
(MDR) service. In our dataset both Fortinet and Palo cases from other telemetry such as detecting network any suspicious creation or modification of files, or
Alto Networks devices were targeted by threat actors enumeration or scanning, or remote access connections other unexpected activity on the appliance. Vendors
and, in several cases, incomplete asset inventory and into your internal network from edge devices. can provide support or provide scripts to be able to
management had ultimately led to a device not being perform these activities. Where virtual appliances are
included in patching and vulnerability management Secure by design: Ensure that both the procurement being used, there may be the possibility to capture
programs. and deployment of devices and architecture follows forensic images for analysis by threat hunt and incident
secure by design principles. response professionals. The NCSC and other global
Edge device compromise poses a key threat as many agencies have released guidance on securing edge
organisations do not onboard edge devices into Harden edge devices: Ensure that edge devices are devices which can used to prepare organisations for
security logging and monitoring systems and, in some deployed with a secure configuration disabling insecure incidents involving edge devices.
cases, they may not have extensive use cases for the or unnecessary features, ports, and services. Make sure
compromise an edge device leading to onward access that management interfaces are not directly accessible
into internal networks. from the public internet.
To combat this threat, it is important that the following Implement strong authentication: Ensure strong
step are taken to protect edge devices: access controls are in place, using strong credentials
Edge device compromise
and implementing phishing-resistant MFA.
poses a key threat to
Know what’s out there: Understand your asset inventory
organisations as many
and ensure edge devices are assessed and onboarded
organisations do not
into asset management systems.
onboard edge devices
into security logging and
monitoring systems.
2025 Cyber Threat Intelligence Report 49

Outlook for 2025
Operational Relay Box (ORB)
Networks
In 2024, we observed increased reporting on the use ORB networks are mesh
of ORB networks by threat actors in their operations. networks typically comprised
ORB networks are mesh networks typically comprised of of vulnerable or obsolete
vulnerable or obsolete routers or leased virtual private routers or leased virtual
servers (VPS) found on the global internet. They are private servers (VPS) found
geographically independent decentralised networks that on the global internet
are used by both APT and cyber crime threat actors,
most notably Chinese APT groups.
We continue to observe ORB networks being leveraged
by threat actors to evade defences, increase complexity
for detection, ultimately reducing the likelihood of
defenders performing successful attribution against this
infrastructure usage.
Understanding how ORB networks are used by threat
actors and being able to consume relevant threat
intelligence to detect and investigate ORB networks is
becoming a key requirement for defenders to be able to
deal with this growing threat to their organisations.
2025 Cyber Threat Intelligence Report 50

Outlook for 2025
Cyber Crime and Ransomware  Leveraging data from Coveware and Ransomware.live,  The top groups in 2024 were RansomHub, LockBit3,
Ecosystem we anticipate that this trend will continue. The victim  Play, Dispossessor, Akira, Qilin, Monti, Clop, and AlphV
claims by ransomware operators continues to rise  (BlackCat).
approximately with 6130 victims claimed in 2024.
Cyber crime continued to thrive in 2024, during which
the ransomware ecosystem continued to grow. There
were several notable trends observed in the period.
700
Victims
600
• Law enforcement takedowns to disrupt and impose
500
  cost on ransomware groups continued. Most notably
smitciV
|   LockBit who were disrupted by a multinational  |     | 400 |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
  policing effort.
300
•  Exit scams were also observed, most notably ALPHV
200
  (BlackCat) who allegedly received a large multi-
|   million-dollar ransom from the Change Healthcare          |     | 100                |      |                    |            |             |      |       |
| ----------------------------------------------------------- | --- | ------------------ | ---- | ------------------ | ---------- | ----------- | ---- | ----- |
|   attack and then failed to pay out the affiliates behind   |     | 0                  |      |                    |            |             |      |       |
|                                                             |     | Ransomhub Lockbit3 | Play | Dispossessor Akira | Blackbasta | Qilin Monti | Clop | Alphv |
  the attack.
Ransomware Group
•  Cyber crime networks were disrupted by police
  including Operation Destabilise in the UK.
• There was a major crackdown of Cobalt Strike under
400
|   the Digital Millennium Copyright Act (DMCA).            |     |     |     |     |     |     |     | Victims |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- |
|   Operation MORPHEUS, a three-year long investigation     |     | 350 |     |     |     |     |     |         |
|   culminated in a coordinated global effort to takedown   |     | 300 |     |     |     |     |     |         |
  unauthorised versions of Cobalt Strike. A total of 690
250
|   IP addresses were flagged to online service providers   | smitciV |     |     |     |     |     |     |     |
| --------------------------------------------------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
200
  in 27 countries. In total, 593 of these addresses were
|   taken down. |     | 150 |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
• The ‘as a service’ model was thriving with the
100
  introduction of new malware, phishing/ delivery,
50
  traffic, access/ credentials, and infrastructure services
0
  popping up on both clear and dark web sources.
|     |     | Clop | Akira | Ransomhub | Babuk | Fog | Lynx | Cactus |
| --- | --- | ---- | ----- | --------- | ----- | --- | ---- | ------ |
Ransomware Group
2025 Cyber Threat Intelligence Report 51

Outlook for 2025
In the first two months of 2025, we have observed  Ransomware (Encryption) Payment Resolution Rates
Clop as the front runner, joined by Akira, RansomHub,
Babuk2, Fog, Lynx, and Cactus ransomware groups.
100%
| Clops mass exploitation approach has seen them claim a  | 90% 15 21 |       |     |     |       |     |     |          |     |     |     |       |
| ------------------------------------------------------- | --------- | ----- | --- | --- | ----- | --- | --- | -------- | --- | --- | --- | ----- |
|                                                         |           | 27 28 | 27  | 23  |       |     |     |          |     |     |     |       |
| considerable number of victims in this recent period.   | 80%       |       | 31  |     |       |     |     |          |     |     |     |       |
|                                                         |           |       |     | 40  | 44 47 |     |     |          |     |     |     |       |
|                                                         |           |       |     |     |       | 54  | 54  |          | 55  |     |     |       |
|                                                         | 70 %      |       |     |     |       |     | 58  | 58 63 63 | 59  |     | 64  |       |
|                                                         |           |       |     |     |       |     |     |          | 66  | 71  | 72  | 68 75 |
6 0 %
We have also seen some interesting trends in the
50%
ransomware payments scene since the start of 2019.
40% 85
|                                                          | 79  | 73 72 | 73  | 77  |     |     |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| The first trend being a steady decline in the number of  |     |       | 69  |     |     |     |     |     |     |     |     |     |
|                                                          | 30% |       |     | 60  | 56  |     |     |     |     |     |     |     |
c o m p a n ie s   p a y in g   r a n s o m s .  I n  2 0 2 4 ,  t h i s  d ro p p e d  to   a   53 46 46 45
|     | 2 0 % |     |     |     |     |     | 42  | 42 37 37 |     | 41  | 36  |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
|     |       |     |     |     |     |     |     |          | 34  | 29  | 28  | 32  |
re c o rd   lo w   o f  2 5 % .   T h i s  s u g g e s ts   th a t   c o m p a n ie s  m a y   1 0 % 25
0%
have more robust security measures in place, including
|     | Q1  | Q2 Q3 | Q4 Q1 | Q2 Q3 Q4 | Q1 Q2 | Q3  | Q4 Q1 Q2 | Q3 Q4 | Q1 Q2 Q3 | Q4  | Q1 Q2 Q3 | Q4  |
| --- | --- | ----- | ----- | -------- | ----- | --- | -------- | ----- | -------- | --- | -------- | --- |
backups that are making encryption-only based attacks  2019 2019 2019 2019 2020 2020 2020 2020 2021 2021 2021 2021 2022 2022 2022 2022 2023 2023 2023 2023 2024 2024 2024 2024
less effective than in previous years. Ransom Paid (%) No Payment (%)
The second trend highlights how threat actors have
Data Exfiltration Only (DXF) Payment Resolution Rates
pivoted to data theft-only attacks, which are proving
to be more successful than encryption-based attacks.
100%
These stats align with our view that organisations are
90%
becoming better at withstanding ransomware attacks
80% 47
using encryption. However, it does highlight that the
|     | 70% | 56  |     |     | 61  |     | 60  |     |     | 57  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | 71  |     |     |     |     | 72  |     |
threat of data being leaked publicly still remains a bigger  73 72 74 77
60%
concern for organisations involved in these attacks.
50%
40%
Sources: ( https://www.coveware.com/blog/2025/1/31/q4-
30%
53
report, https://www.linkedin.com/pulse/ransomware-2024- 44 43
|     | 20% |     |     |     | 39  |     | 40  |     |     |     |     | 41  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | 27  | 28  |     | 29  |     | 26  |     |     | 28  |     |
insights-from-ransomwarelive-julien-mousqueton-2cfve/?tr 10% 23
ackingId=anbiqDtPSfGYB4%2FvdCs13Q%3D%3D)
0%
|                                       | Q1   | Q2   | Q3   | Q4   | Q1                  | Q2   | Q3                 | Q4   | Q1   | Q2   | Q3   | Q4   |
| ------------------------------------- | ---- | ---- | ---- | ---- | ------------------- | ---- | ------------------ | ---- | ---- | ---- | ---- | ---- |
|                                       | 2022 | 2022 | 2022 | 2022 | 2023                | 2023 | 2023               | 2023 | 2024 | 2024 | 2024 | 2024 |
|                                       |      |      |      |      | DXF Ransom Paid (%) |      | DXF No Payment (%) |      |      |      |      |      |
| 2025 Cyber Threat Intelligence Report |      |      |      |      |                     |      |                    |      |      |      |      | 52   |

Outlook for 2025
Cryptocurrency Theft
money laundering (AML)/ know your customer
(KYC) procedures indicate a trend towards greater
Cryptocurrency’s inherent characteristics, including its coordination. Evidence includes growing regulatory
decentralised nature and potential for anonymity, have participation in policy discussions and stricter
fostered an environment where cyber crime has not only compliance measures. However, variations in regulatory Cryptocurrency’s inherent
flourished but also become increasingly lucrative. This maturity and cross-border enforcement challenges characteristics, have
is a trend we project to continue throughout the rest introduce uncertainty. Proactive security will be fostered an environment
of 2025. essential for cryptocurrency exchanges and DeFi where cyber crime has
platforms in 2025. Attackers are continuously adapting, not only flourished but
We have high confidence that cryptocurrency cyber demanding robust security protocols, audits, and also become increasingly
crime will escalate in 2025, driven by increasingly user education. Evidence includes successful attacks lucrative.
sophisticated attacks targeting cross-chain bridges, exploiting known vulnerabilities and industry emphasis
decentralised finance (DeFi) platforms, and exchanges. on preventative measures. The persistent targeting
DPRK-linked actors will remain a significant threat, of these platforms underscores the urgent need for
demonstrating enhanced abilities to accumulate and enhanced security.
launder stolen funds through evolving tactics. Evidence
includes rising attack success rates and growing DPRK (Sources: Analysis and insights derived from the “2025
unlaundered holdings, alongside observed shifts in Crypto Crime Report” and “Recap Quarterly Crypto
money laundering methods. Policy Roundtable Q1 2025”, and “Now Live: The 2025
Crypto Crime Report”)
We are moderately confident that global regulatory
bodies will strengthen collaborative efforts against
cryptocurrency cyber crime in 2025. Increased
international dialogues and emphasis on anti-
2025 Cyber Threat Intelligence Report 53

Outlook for 2025
Generative AI Voice phishing (vishing) has seen a dramatic surge The automation of offensive procedures allows for faster
in effectiveness, largely due to advancements in and more widespread attacks, increasing the potential for
The integration of generative artificial intelligence (AI) AI voice cloning tools like ElevenLabs, which now large-scale disruptions. The ability to create highly targeted
into cyber attack methodologies is rapidly transforming enable attackers to convincingly mimic the voices of and personalised attacks further amplifies the risk.
the threat landscape, posing a significant challenge trusted individuals. While deepfake video technology
to defenders. Generative AI (Gen AI) empowers lower continues to improve, and despite remaining telltale To counter these threats, organisations must build
end cyber criminals with enhanced capabilities for signs, its rapid development poses a growing strategies and policies to address AI and to adopt AI in
automation, sophistication, and evasion, leading to more threat, as the ability to create believable visual their own defensive security controls to help them defend
effective and damaging attacks. This trend is expected impersonations becomes increasingly accessible to against growing attacker automation and sophistication.
to accelerate, as Gen AI tools become more accessible cyber criminals.
and better understood by users.
The use of AI in cyber attacks presents a multifaceted
Analysis of recent reports reveals a growing trend of AI- threat, impacting various sectors, including healthcare,
powered attacks, including the use of AI for generating finance, and critical infrastructure. AI-driven social
highly realistic phishing emails, automating vulnerability engineering attacks, such as those used by groups like
scanning and exploitation, and creating heavily Scattered Spider, are becoming increasingly effective
obfuscated malware that can evade certain security at manipulating human behaviour and bypassing
controls. Evidence includes warnings from the FBI and security controls.
cyber security firms about the increasing use of AI in
social engineering attacks, malware development, and
network intrusion.
The use of AI in cyber
AI’s ability to analyse vast datasets and learn patterns attacks presents a
enables attackers to identify and exploit vulnerabilities multifaceted threat,
more efficiently. Large Language Models (LLMs) are impacting various sectors,
being used to generate sophisticated malware code including healthcare, finance,
and social engineering campaigns. Since the release and critical infrastructure.
of LLM and Gen AI tools, we have observed a marked
increase in the sophistication of phishing campaigns
and malware obfuscation, with attacks becoming more
personalised and difficult to detect, directly mirroring
the trends highlighted in these reports.
2025 Cyber Threat Intelligence Report 54

Outlook for 2025
Geopolitical Events The Expanding Threat: DPRK’s
These operatives engage in a range of activities,
Exploitation of Deceptive including stealing intellectual property, conducting
We expect cyber attacks tied to global tensions and Employment Tactics espionage, and generating revenue through fraudulent
conflicts to increase throughout the rest of 2025. We IT work. The use of “laptop farms” in overseas locations
have moderate confidence that Russia will continue further amplifies their reach, allowing them to scale their
In 2024, we observed an increase in reporting related
to develop and express capabilities against critical operations and obfuscate their true identities. Reports
to threat actors using fake job applicants to infiltrate
infrastructure in Ukraine and allied countries. Iranian- indicate these operations are used to generate revenue
western organisations.
backed groups will continue targeting organisations and to bypass sanctions and fund DPRK weapons programs.
individuals linked to Israel, including targeting industrial
The use of deceptive employment tactics by nation-
control systems leveraging Israeli technology and The increasing sophistication of these tactics
state actors, particularly the DPRK, is a growing trend
programmable logic controllers (PLCs). necessitates a heightened awareness and proactive
that poses a significant threat to global organisations.
security posture from organisations. The DPRK’s ability
These tactics involve the strategic deployment of fake
Hacktivist groups, both pro-Russian and pro-Iranian to adapt and refine its methods, coupled with its
job applicants and overseas “laptop farms” to infiltrate
collectives like the Holy League, will use disruptive persistent pursuit of financial resources, suggests that
targeted companies for espionage and financial
Distributed Denial-of-Service (DDoS) attacks in this trend will continue to escalate. Evidence of this
gain, which directly supports the DPRK’s weapons
politically-motivated targeting. They continue to adaptation can be seen in the use of fake recruitment
programs. This approach allows the DPRK to bypass
leverage social media and messengers such as processes, even mimicking security firms, to gain
traditional cyber security defences by leveraging
Telegram to spread their message. Service providers access to sensitive information.
human vulnerabilities and exploiting the trust inherent in
have shown appetite to ban and block abusive
employer-employee relationships.
channels, however they continue to reappear after Furthermore, The US Department of the Treasury’s
takedown actions. Office of Foreign Assets Control (OFAC) sanctions and
Analysis of recent cases reveals a consistent pattern
Department of Justice (DOJ) indictments highlight the
of DPRK operatives creating convincing fake online
We expect more attacks on essential services and financial nature of these operations, directly linking
personas and resumes to secure remote IT positions.
businesses, driven by global politics. It’s important for them to the DPRK’s attempts to bypass sanctions.
They often blend into legitimate workforces, gaining
organisations to strengthen defences with the threat Companies must implement stringent vetting processes,
access to sensitive internal systems and data. Evidence
of politically-motivated targeting based on region or conduct thorough background checks, and monitor
includes numerous indictments and advisories from
industry sector. Well architected network infrastructure employee activity to mitigate the risk of infiltration.
U.S. government agencies, cyber security firms, and
and DDoS mitigation services are growing in importance
technology companies, detailing instances where DPRK
due to the prevalence of DDoS attacks being observed. (Sources: CrowdStrike, U.S. Department of Justice,
nationals have successfully infiltrated organisations.
KnowBe4, The Register, BBC News, Google Cloud, OFAC,
Palo Alto Networks Unit 42, Sasha Ingber Substack)
2025 Cyber Threat Intelligence Report 55

Outlook for 2025
Cloud Native Attacks
This is reflected in our clients’ experiences with
misconfigured hybrid connectivity and attacks targeting
We are moderately confident that the cloud attack the cloud control plane. The insider threat also remains
surface is expanding rapidly due to the continued significant as privileged access is exploited, a pattern
adoption of cloud-native and hybrid environments. This we’ve consistently seen both in public reporting and
To combat these threats, a
is a trend we’ve directly observed across our managed within our client base.
holistic security approach
security services clients.
is essential, encompassing
To combat these threats, a holistic security approach is
both on-premises and cloud
Attacks are increasingly targeting cloud misconfigurations, essential, encompassing both on-premises and cloud
environments.
Identity and Access Management (IAM) flaws, and environments. We’ve consistently advised clients to
container vulnerabilities, with a growing sophistication implement robust controls, continuous monitoring, and
shown by container escapes, serverless hijacking, and automated threat detection. Zero trust architecture and
lateral movement between on-premises and cloud strong identity management are critical, especially given
systems. We’ve witnessed a corresponding rise in data the observed prevalence of IAM-related compromises.
breaches and ransomware incidents within client cloud We recommend cloud security posture assessments to
workloads, mirroring broader industry trends. Actors such ensure the use of cloud is secured effectively, in line
as Octo Tempest have directly been seen abusing cloud with well architected security best practices.
resources such as virtual compute to evade enterprise
security controls and provide a foothold for the adversary (Sources: Microsoft Digital Defense Report 2024,
inside of the compromised network. CrowdStrike Insider’s Playbook: Defending Against Cloud
Threats, Check Point Security Report 2025, Splunk State
Hybrid environments exacerbate these issues, creating of Security 2024, Fortinet Cloud Security Report 2025,
opportunities for attackers to exploit shared accounts, Aqua Security Blog, Netskope Cloud and Threat Report
services, and applications. We also observed API’s 2025, and observations from our managed security
and network vulnerabilities being exploited for lateral services client engagements.)
movement.
2025 Cyber Threat Intelligence Report 56

Outlook for 2025
RMM Tools
As we move further into 2025, there have been It’s important that organisations are aware of the
numerous public reports that RMM usage is on the threats posed by RMM tools and take appropriate
Living-Off-The-Land (LOTL or LOL) was a popular rise. One such report by Proofpoint has also indicated action to assess and where appropriate mitigate the
approach by threat actors within 2024. Both nation- that RMM tools are increasingly being used as first associated risks.
state and cyber crime threat actors have used LOL stage payloads as opposed to other malware variants.
tactics. Most notably, we observed consistent use of We again have moderate confidence based on the (Sources: Remote Monitoring and Management
RMM tools by threat actors in both public and internal available reports that this is an attempt to bypass anti (RMM) Tooling Increasingly an Attacker’s First Choice
intrusions. We have moderate to high confidence based malware security controls. | Proofpoint US, and observations from our managed
on analysis of both open source and internal Bridewell security services client engagements.)
telemetry that these tools are being used to bypass To mitigate the threat posed by RMM tools
security controls such as web filtering and EDR, allowing organisations need to maintain a comprehensive
threat actors to blend into regular environmental traffic. inventory of all authorised RMM tools and their
legitimate users. Robust monitoring and logging
Throughout 2024, we observed over 50 instances that of RMM tool usage, including connection origins,
involved RMM tools in our threat intelligence dataset. accessed systems, and executed commands is
These tools were often deployed by threat actors required to identify suspicious or malicious activity. To mitigate the threat posed
after successfully obtaining access through phishing by RMM tools organisations
techniques, external remote services, and the use of Establishing baseline usage patterns for legitimate need to maintain a
valid credentials. In one particular incident, we observed RMM activity can also help defenders identify comprehensive inventory of
multiple RMM tools being used by the threat actor after anomalies. Organisations should implement all authorised RMM tools and
gaining initial access. application control to restrict the execution and their legitimate users.
installation of unauthorised software, and ensure
threat hunting is performed regularly for RMM usage
where it may not be possible for organisations to
implement the previously mentioned controls.
2025 Cyber Threat Intelligence Report 57

About Bridewell Threat Intelligence
Committed to our clients’ security, Bridewell Threat
Intelligence is a threat research and client-focused
team determined on disrupting attacks and delivering
robust protection against advanced threats for the
organisations we manage.
To discuss how our Threat Intelligence team can help
your organisation, get in touch via:
+44 (0)3303 110 940 hello@bridewell.com bridewell.com
2025 Cyber Threat Intelligence Report 58