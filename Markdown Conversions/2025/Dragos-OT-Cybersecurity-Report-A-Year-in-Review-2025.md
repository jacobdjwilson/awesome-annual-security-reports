# 2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW

## Table of Contents
- [Introduction](#introduction)
- [Defender’s Guide to the Current Threat Landscape](#defenders-guide-to-the-current-threat-landscape)
- [OT-Centric Cyber Operations Increase as Geopolitical Tension and Conflicts Continue](#ot-centric-cyber-operations-increase-as-geopolitical-tension-and-conflicts-continue)
- [KAMACITE Technical Update](#kamacite-technical-update)
- [ELECTRUM Technical Update](#electrum-technical-update)
- [Geopolitical Tensions in Asia Facilitate Further VOLTZITE Activity](#geopolitical-tensions-in-asia-facilitate-further-voltzite-activity)
- [Dragos Identifies Two New Threat Groups in 2024](#dragos-identifies-two-new-threat-groups-in-2024)
- [Introducing GRAPHITE](#introducing-graphite)
- [Introducing BAUXITE](#introducing-bauxite)
- [ICS-Focused Malware Increasingly Used as a Tool in Conflict-Driven Campaigns](#ics-focused-malware-increasingly-used-as-a-tool-in-conflict-driven-campaigns)
- [An ICS Malware Definition](#an-ics-malware-definition)
- [Hacktivists Continue to Wave Their Flags in Support of Certain Geopolitical Conflicts](#hacktivists-continue-to-wave-their-flags-in-support-of-certain-geopolitical-conflicts)
- [The Ransomware Landscape](#the-ransomware-landscape)
- [Insights from Dragos Incident Response](#insights-from-dragos-incident-response)
- [Vulnerabilities](#vulnerabilities)
- [Call to Action](#call-to-action)

---

# Introduction
Throughout the year, Dragos identifies threats to operational technology (OT) and industrial control systems (ICS) infrastructure, conducts services to help defenders mature their program, and prioritizes mitigations for resilient operations. Enhanced by Dragos telemetry, we approach our eighth annual Year in Review report with field-tested guidance. It serves to provide several detailed examples of key attack paths Dragos observed as well as some of the context and motivation behind these attacks.

If this is the beginning of your OT/ICS cybersecurity journey, welcome and don’t be alarmed. Start your year off by systematically identifying your organization’s exposure and work to reduce that exposure as much as possible. Read more about threats to exposed assets such as BAUXITE on page 22 and KurtLar SCADA on page 37.

If you already know your exposure, or have a plan to reduce it, consider the attack scenarios mentioned throughout this report and decide whether you’d be susceptible to these same attacks. Use these scenarios to inform visibility and monitoring strategies, create your incident response plans, and plan segmentation efforts.

If you have a good threat prevention strategy, it’s time to test it. Consider the attack scenarios mentioned throughout this report and identify visibility gaps. Would you notice if an adversary downgraded your firmware? Read more on FrostyGoop malware and associated attack chain on page 29.

If vulnerability management seems overwhelming, read how OT vulnerability management is different than IT in the Vulnerability Trends section on page 53. Learn how to prioritize mitigation and remediation of vulnerabilities with the “Now, Next, Never” framework on page 52.

Buckle in and get ready to hunt. Hacktivists tell you who they are, but we continually observe adversaries hiding amongst the noise. Read more about ELECTRUM’s AcidPour on page 13 and VOLTZITE on page 14.

No matter your cybersecurity maturity, read on. From ICS threat groups and hacktivists to ICS malware attacks and criminal ransomware, you will learn about the latest real-world attacks, and what you can do about them. Combined with insights from our incident responders and guidance from our vulnerability team, this report provides a comprehensive look at the most important cyber threats affecting OT environments and organizations.

---

# Defender’s Guide to the Current Threat Landscape
The cybersecurity threat landscape in 2024 was shaped by escalating geopolitical tensions and their intersection with industrial operations globally. From persistent campaigns by mature threat groups to opportunistic attacks by hacktivists or ransomware operators, adversaries demonstrated a growing awareness of OT/ICS environments as potential attack vectors to achieve their goals.

## Adversaries Targeting OT: Awareness Over Sophistication
A striking trend in 2024 was the continued lowering of the barrier to entry for adversaries targeting OT/ICS. Adversaries that would have once been unaware of or ignored OT/ICS entirely now view it as an effective attack vector to achieve disruption and attention. For example, Blackjack’s Fuxnet malware, revealed in April 2024, though rudimentary compared to more sophisticated ICS-capable malware like PIPEDREAM, signaled a growing awareness of the impact that disruptive attacks on OT networks can have.[^1]

## Defender Progress: Incremental But Uneven
Defenders have made progress in understanding the importance of securing OT environments, but this progress remains uneven across sectors and regions. Regulated industries, such as electric power in North America, demonstrate higher maturity levels than less regulated sectors, such as water utilities or manufacturing.

---

# OT-Centric Cyber Operations Increase as Geopolitical Tension and Conflicts Continue
A cyber attack on a municipal energy company disrupted heat to hundreds of apartment buildings in Ukraine.[^4] A purported attack by Ukraine-aligned Blackjack group damaged critical infrastructure monitoring devices in Russia.[^5] The pro-Iranian CyberAv3ngers attacked fuel management systems in Israel.[^6] In 2024, Dragos witnessed continued offensive cyber activities linked to ongoing geopolitical conflicts.

---

# KAMACITE Technical Update
Tracking KAMACITE is important because they hand off their access to OT teams, like ELECTRUM, which has technical overlaps with Sandworm, tracked by other organizations.[^8]

![KAMACITE attack chain diagram showing spear-phishing, malware delivery, and command and control]

---

# ELECTRUM Technical Update
One of Dragos’s oldest threat groups, ELECTRUM is responsible for multiple ICS attacks, including the CRASHOVERRIDE event in 2016, which blacked out a portion of Kyiv for about an hour, and the failed Industroyer2 attempt in 2022.

![Timeline of ELECTRUM wiper capabilities from 2022 to 2024]

---

# Geopolitical Tensions in Asia Facilitate Further VOLTZITE Activity
Throughout the year, the threat group VOLTZITE continued its activities, compromising small office and home office (SOHO) routers and interacting with geographic information systems (GIS).

![Diagram of VOLTZITE infrastructure usage including ORBs and botnets]

---

# Dragos Identifies Two New Threat Groups in 2024
Shifting away from the existing Dragos-designated groups, two newly coined Dragos threat groups were also very active during this period, conducting a series of conflict-adjacent campaigns.

## Introducing GRAPHITE
Dragos designated GRAPHITE as a new threat group after discovering a campaign targeting hydroelectric generation facilities to steal credentials.

## Introducing BAUXITE
Dragos-designated threat group BAUXITE was implicated in multiple global campaigns targeting OT/ICS entities and specific devices.

---

# ICS-Focused Malware Increasingly Used as a Tool in Conflict-Driven Campaigns
![Image description: Overview of Fuxnet and FrostyGoop malware impact areas]

---

# An ICS Malware Definition
## Three Properties of ICS Malware
1. **ICS-Capable**: The malware has the ability to interact with industrial protocols or hardware.
2. **Designed with Malicious Intent**: The malware is built to disrupt, damage, or manipulate industrial processes.
3. **The Ability for Adverse Effects on OT Environments**: The malware can cause physical or operational impact.

---

# Hacktivists Continue to Wave Their Flags in Support of Certain Geopolitical Conflicts
Hacktivists claim impacts to critical infrastructure, often using basic techniques to manipulate internet-exposed HMI settings.

---

# The Ransomware Landscape
Ransomware attacks against industrial organizations increased 87 percent over the previous year.

![Chart showing the increase in ransomware groups from 50 in 2023 to 80 in 2024]

---

# Insights from Dragos Incident Response
Dragos incident response teams continue to observe operational errors causing incidents, legacy malware, and the critical importance of network security monitoring.

---

# Vulnerabilities
## “Now, Next, Never” Vulnerability Framework
A structured approach to prioritizing mitigation and remediation of vulnerabilities based on risk and exploitability.

---

# Call to Action
Defenders must move beyond basic compliance and focus on active hunting, visibility, and understanding the specific threat landscape of their industrial environment.

---

[^1]: Hackers Linked to Russia’s Military Claim Credit for Sabotaging U.S. Water Utilities - Wired.
[^4]: Impact of FrostyGoop ICS Malware on Connected OT Systems - Dragos Inc.
[^5]: Strategic Overview of the Fuxnet Malware - Dragos Inc.
[^6]: Iran-linked crew used custom ‘cyberweapon’ in U.S. critical infrastructure attacks – The Register.
[^8]: Sandworm Team - MITRE.

---

compromising Unitronics
• VoIP Business
Brute Force SSH   Desk Phones
Unistream and Vision series
• Xiongmai
| programmable logic controllers       | WEAPONIZE |   IoT devices |     |
| ------------------------------------ | --------- | ------------- | --- |
| (PLCs) exposed on the internet. The  |           | HSS           |     |
adversary is capable of downloading  RECON DELIVER INSTALL ACT
logic to these controllers, causing a
|     | TARGET | EXPLOIT | COMMAND |
| --- | ------ | ------- | ------- |
+ CONTROL
d e n ia l   o f  s e r v ic e  ( D o S )  equivalent to  Default Creds: 1111
ex e c u t e   a n  I C S  a t t ac k .
Australia,  Water/Wastewater,
US, Ireland Food/Beverage,
| In late 2023, Dragos’s investigation  | Chemical |     |     |
| ------------------------------------- | -------- | --- | --- |
uncovered widespread exploitation  Stage 2:
ICS Attack
tactics, including SSH brute-force
INSTALL/
TEST MODIFY
attacks targeting a diverse set of
vulnerable hosts and internet of  DELIVER )65202/PCT( EXECUTE
|     | DEVELOP |  MOCP |     |
| --- | ------- | ----- | --- |
ICS ATTACK
things (IoT) devices, such as Hikvision
HSS
IP cameras, automatic tank gauges,
Ladder logic
|                                     |     | Unitronics  download (w/ | Caused Denial  |
| ----------------------------------- | --- | ------------------------ | -------------- |
| VoIP business desk phones, Control  |     |                          | of Service     |
devices GAZA in it)
| ID access control systems, Xiongmai   |     | Unistream Series |     |
| ------------------------------------- | --- | ---------------- | --- |
| IoT devices, Heatcraft refrigeration  |     | Vision Series    |     |
controllers, and Cisco TelePresence
codec devices.32
According to
Neighborhood Keeper,
Cisco TelePresence codec
assets are found in mining,
worldwide.
32Cyber Av3ngers Hacktivist Group Targeting Israel-Made OT Devices - Dragos Inc.
23

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
Sophos Firewall Attack  If you use a satellite internet provider, such as Starlink or Viasat, you may be
(April 2024-May 2024) inadvertently exposing your equipment to the internet. Consider these scenarios
when assessing your organization’s exposure.
BAUXITE targeted vulnerable Sophos
firewalls, resulting in enterprise impact
Satellite Internet Provider
on chemical, food and beverage, and
water and wastewater industries.
Dragos Services conducted an incident
response to a U.S. oil and natural gas
(ONG) organization where BAUXITE
compromised Sophos firewalls at
|     | Offshore Oil Rigs |     |     | Offshore Oil Rigs |     |     | Offshore Oil Rigs |     |
| --- | ----------------- | --- | --- | ----------------- | --- | --- | ----------------- | --- |
oil rig sites.
|     | Sophos |     |     | Sophos |     |     | Sophos |     |
| --- | ------ | --- | --- | ------ | --- | --- | ------ | --- |
According to Dragos telemetry, Sophos
|     | Firewalls |     |     | Firewalls |     |     | Firewalls |     |
| --- | --------- | --- | --- | --------- | --- | --- | --------- | --- |
devices are found in North America in oil
and natural gas and electric utilities.
|             | Router     | DC         |     | Router      | DC         |     | Router      | DC         |
| ----------- | ---------- | ---------- | --- | ----------- | ---------- | --- | ----------- | ---------- |
| File Server |            | OT Servers |     | File Server | OT Servers |     | File Server | OT Servers |
|             | Controller |            |     | Controller  |            |     | Controller  |            |
5%
Example of Compromised Infrastructure
OT Watch identified
5 percent of customers
communicating to external addresses
via PPTP protocol.
RCE on Sophos Firewall
*A minor portion of these
≤ V19.0 MR1 (19.0.1)
environments are untuned. (CVE-2022-3236) Add users similar to existing
accounts
|          |     |              |     | Auth bypass on Sophos  |     | Alter PPTP configuration |     |     |
| -------- | --- | ------------ | --- | ---------------------- | --- | ------------------------ | --- | --- |
| Stage 1: |     | VPN provider |     | Firewall ≤ v18.5 MR3   |     |                          |     |     |
Exploits
| Intrusion |     |     | with public     | (18.5.3) (CVE-2022-1040) |                   | Update firewall group config    |     |     |
| --------- | --- | --- | --------------- | ------------------------ | ----------------- | ------------------------------- | --- | --- |
|           |     |     | information or  |                          |                   | Create firewall rules to allow  |     |     |
|           |     |     | POCs available  |  )4444/PCT( SPTTH        | )344/PCT( SPTTH & |                                 |     |     |
PPTP communication
Hunt for yourself in the Dragos
Platform. To identify PPTP
WEAPONIZE
communicating to non RFC-
|     | RECON |     | DELIVER |     |     | INSTALL |     | ACT |
| --- | ----- | --- | ------- | --- | --- | ------- | --- | --- |
1918 addresses:
|     |     | TARGET |     | EXPLOIT |     |     | COMMAND |     |
| --- | --- | ------ | --- | ------- | --- | --- | ------- | --- |
type:Communications AND  + CONTROL
NOT ip_dst_network_id:* AND
protocol:PPTP AND dst_port_
| o2r: * | Opportunistic,  | Oil & Natural Gas |     |     |     |     |     |     |
| ------ | --------------- | ----------------- | --- | --- | --- | --- | --- | --- |
Sophos devices
24

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
Reconnaissance Scanning Campaign
(June 2024-July 2024)
BAUXITE accessed multiple
OT/ICS OEMs and utility web
pages. This activity was likely
Enumeration
conducted to gather intelligence on of Siemens S7 Bulletproof
devices, CIMON hosting provider
products, services, and other critical Automation Stark Industries
devices, OPC/
information that could support future UA, Omron
FINS, CODESYS
operational objectives. protocol
WEAPONIZE
BAUXITE conducted port scanning
of multiple internet-exposed OT/ICS
RECON DELIVER INSTALL ACT
devices, likely to identify potential
targets for future operations. The TARGET EXPLOIT + C O C M ON M T A R N O D L
Stage 1:
following internet-exposed devices Intrusion
were targeted: CIMON US Energy
Automation company
• Siemens S7 devices via s7comm
CODESYS
(TCP/102). Thermonova
• CIMON Automation devices via
CIP (TCP/44818).
• Devices running OPC Unified
Architecture (OPC/UA) Server via
UDP/4840.
• Omron Factory Interface
Network Service (FINS)
TCP/9600.
• Devices running CODESYS
(TCP/11740, TCP/1217, and
UDP/1740-1743).
These protocols overlap with
CHERNOVITE-developed
PIPEDREAM.
25

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
IOControl Campaign  Stage 1: Widespread intrusion against non-OT devices
(Late 2023-2024)  Owned
VPS
BAUXITE compromised over 400
|     |     | On-Device   |     |     | Unknown effects  |
| --- | --- | ----------- | --- | --- | ---------------- |
|     |     | Management  |     |     | on other victim  |
global OT/ICS devices and firewalls  Panels Possible SSH  BAUXITE  devices
Infrastructure
Shared Key or
| by installing a custom-embedded  |     | HSS | admin passwords,  |     |     |
| -------------------------------- | --- | --- | ----------------- | --- | --- |
)3888/PCT(
|                                   |           |     | or brute force  |  TTQM |     |
| --------------------------------- | --------- | --- | --------------- | ----- | --- |
| Linux backdoor called IOControl.  | WEAPONIZE |     | attacks         |       |     |
IOControl is a remote access trojan
|     | RECON | DELIVER |     | INSTALL | ACT |
| --- | ----- | ------- | --- | ------- | --- |
and communicates to the C2 server
| using Message Queuing Telemetry  | TARGET |     | EXPLOIT | COMMAND |     |
| -------------------------------- | ------ | --- | ------- | ------- | --- |
+ CONTROL
| Transport (MQTT) on TCP/8883.  |     |     |     | IOCONTROL  |     |
| ------------------------------ | --- | --- | --- | ---------- | --- |
on all target
| This communication is established  |     |     |     | devices |     |
| ---------------------------------- | --- | --- | --- | ------- | --- |
Internet-exposed devices manufactured by:
to a hardcoded domain hosted on
Fortinet, Hikvision, Orange LiveBox, Sonicwall,
Teltonika, Ubiquiti, Watchguard
Cloudflare via DNS over HTTPS
| (DoH). As of publication, this domain  | Stage 2:   |      |     |          |                     |
| -------------------------------------- | ---------- | ---- | --- | -------- | ------------------- |
| is sinkholed, mitigating risk to       | Attack on  |      |     |          |                     |
|                                        | OT Devices |      |     |          | Accidental Effect:  |
| defenders. Each IOControl sample       |            |      |     |          | Orpak DoS due to    |
|                                        |            | TEST |     | INSTALL/ | installation error  |
| is unique to the targeted device,      |            |      |     | MODIFY   |                     |
with newer samples that can wipe
|     |     |     | DELIVER | E X E C U T E |     |
| --- | --- | --- | ------- | ------------- | --- |
DEVELOP IC S  A T T A C K Port Scanning
| the system via memory technology  |     |     |     |     | devices |
| --------------------------------- | --- | --- | --- | --- | ------- |
Install IOControl
|                            |     |     |                              | on target OT  )3888/PCT( | Data            |
| -------------------------- | --- | --- | ---------------------------- | ------------------------ | --------------- |
| device (MTD) manipulation. |     |     |                              |  TTQM                    |                 |
|                            |     |     |                              | devices                  | Exfiltration    |
|                            |     |     | Connect to Internet-exposed  |                          | Disruption via  |
Wiper Attack
Orpak, Phoenix Contact, Red  C2 over MQTT
to Bauxite
|     |     |     | Lion Controls, Unitronics,      |                 | Arbitrary  |
| --- | --- | --- | ------------------------------- | --------------- | ---------- |
|     |     |     | Tridium, and Baicells devices,  | Infrastructure  | command    |
to manage
|     |     |     | using admin passwords,      |         | execution    |
| --- | --- | --- | --------------------------- | ------- | ------------ |
|     |     |     | brute force attacks or SSH  | malware | for unknown  |
|     |     |     | Shared Key.                 |         | objective    |
According to Neighborhood Keeper, Orpak  Phoenix Contact devices are used in North
devices are used in electric generation in  America, Asia, and Europe, in the following
| Australia and New Zealand. | industries: |     |     |     |     |
| -------------------------- | ----------- | --- | --- | --- | --- |
Electric Transportation & Logistics
Manufacturing
Chemical
Mining
26

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
ICS-Focused Malware Increasingly
Used as a Tool in Conflict-Driven
Campaigns
Two new variants of ICS malware were observed in
Teams are often unaware of default credentials. Dragos
April 2024, both of which occurred in association
flags default credentials in only 6 percent of architecture
with the Ukraine-Russia conflict. While the use of
reviews, but approximately 1 in every 4 penetration tests
ICS malware as a toolset in geopolitical conflicts is
find default credentials in industrial environments. Active
not a new concept, the alleged deployment by both
inspections are the best way to identify this issue.
parties to the Ukraine-Russia war indicates a tit-for-
tat escalation with implications for the larger OT/ICS
community. Using the Fuxnet malware, BlackJack claimed to disable
thousands of sensors and destroy sensor gateway devices,
BlackJack Claims Disruption of rendering them unable to transmit information. Additionally,
BlackJack asserted they exfiltrated organizational data,
Industrial Sensors in Moscow
defaced social media accounts, accessed the emergency
In April 2024, the self-named hacktivist group BlackJack service number 112, and factory reset devices and
claimed to breach Moskollektor, a municipal organization workstations. They also released screenshots of the Fuxnet
that maintains Moscow’s communication system for a source code; however, they did not provide a sample of
gas, water, and sewage network. BlackJack asserts that it the Fuxnet binary, and it has not appeared in any public
compromised communications to thousands of sensors malware repositories or Dragos telemetry.
responsible for maintaining operations in the Moscow
region. After analyzing all the data released by BlackJack, it is
likely that disruption to the industrial sensors and sensor
Stolen data released by BlackJack on a public website gateways did occur. However, the extent of the disruption
indicates they accessed routers and sensor gateway devices, was not as significant as BlackJack claimed. The released
likely through default credentials. These gateways are screenshots indicate that Fuxnet likely would lead to
connected to industrial sensors through a serial connection the disruption or destruction of the sensor gateways if
which monitors Moskollektor’s underground tunnel deployed. It is unclear if Fuxnet caused a permanent or
infrastructure and collects and transmits physical data. temporary DoS condition on the sensors themselves.
27

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
The Fuxnet Malware
Pending evidence of its compiled form, Fuxnet is the eighth known ICS-specific malware due to its ability to disrupt
Meter-bus communication to the industrial sensors.33 According to the source code screenshots released by BlackJack,
Fuxnet contains two major components:
THE DESTRUCTOR CONSISTS OF THREE PARTS
Sensor Gateway
Destructor
|     | File System |     |     | UBI Volume |     |     | Flash Memory |
| --- | ----------- | --- | --- | ---------- | --- | --- | ------------ |
1
Stops and removes  Destroys UBI volume; leaves UBI  Destroys MTD flash
The sensor gateways
critical services; deletes  Volume Update IOCTL operation  memory via erase-then-
provide internet access
critical files. hanging by writing a less- write technique to wear
to sensor-collected
|     |     |     | than-promised amount of data,  |     |     |     | out NAND memory. |
| --- | --- | --- | ------------------------------ | --- | --- | --- | ---------------- |
industrial data.
effectively bricking the device.
Overwhelms sensors by sending many Meter-Bus requests over a serial connection. These
2 requests are randomly generated packets of data that loosely conform to the Meter-Bus
standard, thus fuzzing the device to cause a potential DoS condition.
Sensor Meter-Bus DoS
The Sensor Gateway
Stage 1:
| Destructor component is a  | Intrusion |     |     |     |     |     |     |
| -------------------------- | --------- | --- | --- | --- | --- | --- | --- |
Likely network
| more generic Linux wiper  |     |     |     | vulnerabilities or  |     |     |     |
| ------------------------- | --- | --- | --- | ------------------- | --- | --- | --- |
spearphishing
| malware, whereas the  |     | WEAPONIZE |     |     |     |     |     |
| --------------------- | --- | --------- | --- | --- | --- | --- | --- |
Meter-Bus DoS component
|     | RECON |     | DELIVER |     | INSTALL |     | ACT |
| --- | ----- | --- | ------- | --- | ------- | --- | --- |
provides unique ICS-specific
| capability. Meter-bus is a  |     | TARGET |     | EXPLOIT |     | COMMAND |     |
| --------------------------- | --- | ------ | --- | ------- | --- | ------- | --- |
+ CONTROL
European standard protocol
for reading specific sensor
|     | Russian  | Emergency  |     |     |     |     |     |
| --- | -------- | ---------- | --- | --- | --- | --- | --- |
data from water, gas, and
|     | Federation | services and  |     |     |     |     |     |
| --- | ---------- | ------------- | --- | --- | --- | --- | --- |
utilities
|                         |     |                    |     |     | TEST |     | INSTALL/ |
| ----------------------- | --- | ------------------ | --- | --- | ---- | --- | -------- |
| electricity meters. By  |     | Industrial sector  |     |     |      |     | MODIFY   |
and Monitoring
overwhelming the device
i nf r a s tr u c t u r e ,  E X E C U T E
|     |     | M o s k o l le c k t o | r   | DEVELOP |     | DELIVER | IC S  A T T A C K |
| --- | --- | ---------------------- | --- | ------- | --- | ------- | ----------------- |
with randomly generated
Deploy
| requests, it is possible Fuxnet  |     |     |     |     |     |     | Fuxnet to  |
| -------------------------------- | --- | --- | --- | --- | --- | --- | ---------- |
sensor
Stage 2:
| triggered unknown zero- |     |     |     |            |     |                 | g at e w a y s   |
| ----------------------- | --- | --- | --- | ---------- | --- | --------------- | ---------------- |
|                         |     |     |     | ICS Attack |     | Likely default  | Caused outage    |
an d  M e t e r bus
|     |     |     |     |     |     | credentials | devices Sensor Gateway  |
| --- | --- | --- | --- | --- | --- | ----------- | ----------------------- |
day vulnerabilities in the
Destructor wiped file
system UBI volumes and
industrial sensor’s Meter-bus
flash memory
protocol stack, thus rendering  Sensor Meter-bus Denial
of Service via Serial
them inoperable. The sensor
communication
33Strategic Overview of the Fuxnet Malware - Dragos
28

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
gateways were likely physically damaged and required  commonplace in operational facilities. Dragos telemetry
device replacement to resume normal operations. indicates that default credentials are still commonly used
in environments.
Lessons from Fuxnet
However, the SANS ICS 5 Critical Controls34 can
The attack on Moskollektor underscores the  strengthen an organization’s security posture and better
defend against threats like the Fuxnet malware. Asset
normalization of attacks on industrial devices by
owners should be sure to identify and mitigate ICS
groups driven by geopolitical conflicts. Fuxnet was
highly tailored to Moskollektor and is unlikely to be  components with default credentials as part of a risk-
used against another industrial environment without  based vulnerability management program and implement
significant changes to the codebase. Poor practices such  thorough asset hardening and strict access controls to
strengthen their defensible architecture.
as default credentials greatly help adversaries and can be
FrostyGoop Malware Impacts Heating in Ukraine
In April 2024, Dragos discovered
FrostyGoop, the ninth known ICS
| malware.35 FrostyGoop modified  |     |     |     |     |     | Dump SAM  |
| ------------------------------- | --- | --- | --- | --- | --- | --------- |
registry hive and
|                                  | Stage 1:  |     |     | Unknown          | ReGeorg  |                   |
| -------------------------------- | --------- | --- | --- | ---------------- | -------- | ----------------- |
| instrument measurements of ENCO  |           |     |     |                  |          | steal credentials |
|                                  | Intrusion |     |     | MicroTik router  | Webshell |                   |
controllers resulting in heating outages  vulnerabilities  smmoc PT2L
exploited
WEAPONIZE  & ROT
for over 600 apartment buildings in
Ukraine during the winter. FrostyGoop
|     | RECON |     | DELIVER |     | INSTALL | ACT |
| --- | ----- | --- | ------- | --- | ------- | --- |
interacts with ICS devices over Modbus
COMMAND
| TCP/502, a standard ICS protocol  |     | TARGET |     | EXPLOIT | + CONTROL |     |
| --------------------------------- | --- | ------ | --- | ------- | --------- | --- |
used worldwide, combining generic,
publicly available Modbus libraries
|     | Ukraine | Municipal District  |     |     |     |     |
| --- | ------- | ------------------- | --- | --- | --- | --- |
Energy
with logging capabilities to adaptively
send commands to read and write
registers on ICS devices. Dragos tracks
| this activity as TAT24-24. |     |     | TEST |     | INSTALL/ |     |
| -------------------------- | --- | --- | ---- | --- | -------- | --- |
MODIFY
|     | Stage 2: | DEVELOP |  subdoM )205/PCT( | DELIVER | EXECUTE |     |
| --- | -------- | ------- | ----------------- | ------- | ------- | --- |
ICS ATTACK
The January 2024 cyber attack
|     | ICS Attack |     |     |     | Adversaries  |     |
| --- | ---------- | --- | --- | --- | ------------ | --- |
against a municipal district energy  downgraded   subdoM )205/PCT(
ENCO Controllers’
Hardcoded IPs
| company in Ukraine involving  |     |                     |                     |            | firmware |     |
| ----------------------------- | --- | ------------------- | ------------------- | ---------- | -------- | --- |
|                               |     | Dragos identified   | indicate potential  | Moscow IP  |          |     |
|                               |     | at least 9 samples  | testing on          | addresses  |          |     |
FrostyGoop was likely a part of  FrostyGoop connects and writes to
|     |     | uploaded to VT | internet-exposed  |     |     |     |
| --- | --- | -------------- | ----------------- | --- | --- | --- |
multiple modbus registers. Changes
hybrid warfare in support of the  ENCO controllers  caused inaccurate measurements,
|     |     | The working  | in Eastern Europe |     |     |     |
| --- | --- | ------------ | ----------------- | --- | --- | --- |
sample  resulting in heating outages in
Ukraine during Winter
Ukraine-Russia conflict. The Cyber  was named  No known outage
|     |     | “FrostyGoop” | associated |     |     |     |
| --- | --- | ------------ | ---------- | --- | --- | --- |
Security Situation Center (CSSC),
a part of the Security Service of
Ukraine (Служба безпеки України),
34The Five ICS Cybersecurity Critical Controls - SANS; 35Impact of FrostyGoop Modbus Malware on Connected OT Systems - Dragos
29

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
shared details with Dragos about the incident. Analysis
suggests that FrostyGoop was also used to target ENCO
Execution Flow for FrostyGoop
controllers with TCP/502 open to the public-facing
internet. ENCO controllers are found throughout Eastern
Europe and Dragos’s investigation of FrostyGoop
Parse command
Modbus TCP/502
revealed that there were over 46,000 internet-exposed line arguments communications to PLC
and/or JSON file
ICS devices communicating over Modbus worldwide.
While FrostyGoop was used to target ENCO devices, its
functionality is not specific to these devices, allowing Initiate TCP/502 Connection
Send Modbus Command
it to interact with numerous other commonly used ICS
Receive response
devices such as PLCs, DCS, sensors, actuators, and field Close TCP connection
devices. PLC
Windows
Machine
Most concerning was the inability of common antivirus
software to detect FrostyGoop due to its blending of
Log TCP/502
malicious activity with normal operations. Exploitation communications
of well-known ICS protocols is becoming more frequent
within ICS malware development, underscoring the need
for more sophisticated OT-aware detection and response
methods. TAT24-24 downgraded the controller firmware
before the attack. Many Modbus devices have a default UnitID of 254, so
FrostyGoop has the potential to impact several other
The attack’s involvement of internet-exposed controllers Modbus-speaking devices not specific to ENCO Control
and insufficient network segmentation highlights the risks devices.
of not implementing basic cybersecurity controls and the
importance of doing so. Lessons from FrostyGoop
Natively, FrostyGoop can impact any Modbus device
The FrostyGoop Malware
with a UnitID of 254. Dragos recommends looking for
Dragos identified FrostyGoop and eight other similar vulnerable devices in your own network and continuously
samples on an opensource repository, VirusTotal. It was monitoring them, including monitoring devices for new
written in Go and accepts a json file with a list of target IP Modbus connections on TCP/502. Dragos also recommends
addresses. It is capable of reading and writing to Modbus restricting access to Modbus TCP/502 and ensuring Modbus
registers over TCP/502 and has a hardcoded UnitID of 254. devices are not accessible from the public-facing internet.
Tips for Hunting Here’s the Dragos Platform query to search for
Modbus devices with a unitID of 254 in your
OT Watch hunts for
downgraded firmware. own environment:
Would you notice if an
adversary downgraded type:”modbus” AND modbus_unit_id:”254” AND
your controllers? modbus_function_code: (3 OR 6 OR 16)
30

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
Attack Path for FrostyGoop Impacts
Adversary @
Moscow IPs
Adversary
2 4
3
5
Deploy ReGeorg Modify register
Use FrostyGoop
Webshell on victim values on Cause faulty
via Webshell
network via L2TP controller measurements
Internet
1
GPRS
Compromise
Ethernet
MikroTik Router
Modbus
Server
Database
Radio
Frequency
Ethernet/USB
M-Bus
MikroTik Heat Meter
ENCO Reader and ENCO Controller ENCO Box
Router
ENCO MS PC
Adversary
compromised an USB MBus
unknown vulnerability
Radio
Frequency
ENCO Terminal Gas/Electric ENCO Box
Meter
Radio
Frequency
Water Meter Water Meter
Automated
Heating
Substation Heat Allocator Heat Allocator
Module
6 6
Heat Heat
Disruption Disruption
31

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
An ICS Malware Definition
In 2024, Dragos created a definition of ICS malware Here are a few examples of ICS-capable software:
based on historical data and our own experiences. • Software that speaks ICS protocols like IEC104, OPCUA,
For defenders, this provides assurance that ICS and HART
malware is a credible, real-world threat worth • Software that can upload or download ladder logic
considering in scenario-based defensive applications programs
such as incident response planning, tabletop • Software that runs on the PLC interacting with ladder
exercises, and threat baselines. logic runtime or other operating system internals
• Software that runs on the engineering workstation
ICS Malware Definition that interacts with or modifies the engineering
software (e.g., modifies project files).
At Dragos, ICS malware is defined as follows:
The ICS-Capable property distinguishes the subset of
ICS-capable software intentionally designed for
ICS software from other types of software like standard
adverse effects on operational technology (OT)
Windows or Linux tools. Tools like Process Hacker, day-to-
environments.
day Windows and Linux malware implants, and various
ransomware variants are not considered ICS malware
The definition requires that ICS Malware contain three
because they are not ICS-capable.
properties:
• The software must be ICS-capable. Designed with Malicious Intent
• The software must be designed with malicious intent.
• The software must have the ability for adverse effects Malicious Intent is important for distinguishing malware
on OT environments. from defender tools and other tools designed for a
benign purpose. In the IT world, PSExec can be used by
Identifying a sample as ICS malware is an evidence-based adversaries for lateral movement. Dragos does not call
intelligence assessment. If sufficient evidence for all three PSExec malware because it was designed for system
properties is found, the ICS malware designator is applied administrators.36 In the same way, something that looks
to the sample. like ICS malware but does not have malicious intent
could be ICS research, an ICS red team tool, or a sub-
Three Properties of ICS Malware component of a vendor’s engineering software abused
for malicious purposes.
ICS-Capable
To determine if the software was designed with malicious
ICS-Capable, according to SANS, means the software
intent, Dragos uses evidence like code capabilities and
contains OT/ICS functions for navigating, altering, or
behavior, binary similarity, developer information, threat
retrieving information from OT networks, devices, or
group association, incident response data, and victim/
software. In other words, its code allows for speaking ICS
deployment information.
protocols or interacting with PLCs and other OT devices.
36PsExec – Microsoft Learn
32

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
The Ability for Adverse Effects
What if the malware does not work? If a tool is ICS-capable
on OT Environments
and designed with malicious intent but has no ability for
This property introduces a burden of proof on the analyst adverse effects, it is likely broken malware or malware in
to show that the software can achieve an adverse outcome development. Depending on how close it is to functioning,
and specifies the category of actions considered detrimental it may be called “potential ICS Malware.”
for OT. Identifying this property answers the question: What
adverse consequences can the ICS-capable software cause?
Adverse Effects are like those described as Stage 2 effects
in the ICS Cyber Kill Chain and vary by site and industry.37
Here are a few examples of Adverse Effects:
• Collecting sensitive process information
• Enabling unauthorized access to OT devices
• Downloading arbitrary ladder logic or executable code
to PLCs
• Bypassing OT firewalls or other security controls
• Manipulation of set points, variables, or other PLC
settings
37The Industrial Control System Kill Chain - SANS
33

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
What Does the ICS Malware
Definition Mean for Asset Owners?
If your organization is implementing the SANS ICS
5 Critical Controls, then our list of ICS malware is a
concrete guidepost for prioritizing defenses.38
For example, if your organization relies on Modbus/TCP,
it might be at risk for a FrostyGoop-style attack. Using
information about the malware, you can vet various Targeted disablement of operations via ICS malware is a
aspects of your organization’s implementation of the 5 common concern of our customers and one of many threat
event categories reviewed as part of Dragos’s new Threat
Critical Controls by asking questions about each control.
Baseline service. With Threat Baselines, Dragos has helped
organizations identify the potential repercussions of a
In the same way, asset owners can refer to any ICS FrostyGoop Modbus TCP attack against devices in their
networks and helped them identify a mitigation path and
malware family that has been reported and design a
recover against such an attack. Completing Threat Baselines
similar exercise when considering their defensive posture. in 2024 highlighted that industrial environments are uniquely
A version using FrostyGoop as the example is presented in configured, and reviewing threats from different perspectives
helped identify common and uncommon insecurities.
the figure below.
ICS Incident Defensible Network Visibility Secure Remote Risk-Based
Response Plan Architecture & Monitoring Access Vulnerability
(Scenario Planning) (Asset ID/Crown Jewels) Management
• What would an • Which processes are • Are devices in my • Are Modbus/TCP • Investigation of the
adversary need to do controlled by Modbus/ network emitting devices exposed to FrostyGoop attack
to attack our Modbus/ TCP devices? Modbus/TCP the internet? suggests that the
TCP components? unnecessarily? adversaries may have
• How many Modbus/
gained access to the
• Are there online TCP devices are in my • Can we identify
victim network via
and offline backups environment? new and potentially
a vulnerability in an
of program and unwanted
externally facing router.
configuration files communications to
What vulnerabilities exist
for Modbus/TCP Modbus/TCP devices?
for my internal routers?
components in my
Are they mitigated
environment?
adequately?
38The Five ICS Cybersecurity Critical Controls – SANS
34

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
Hacktivists Continue to Wave
Their Flags in Support of Certain
Geopolitical Conflicts
Recent geopolitical conflicts, such as the Israel-Hamas Since 2022, hacktivists increasingly use freely and
and Ukraine-Russia conflicts, have intensified the commercially available tools, such as Shodan, Censys,
relationship between hacktivism and state objectives. or Kali Linux, to discover and exploit vulnerable or
The hacktivist group CyberArmyofRussia_Reborn misconfigured targets, including OT/ICS OEM products.
(CARR) continues to target critical sectors in the U.S.,
specifically water and wastewater and oil and natural OT-CERT Notifies TAT24-76 Victims
gas, with confirmed incidents in California, Florida, of HMI Compromise
and Pennsylvania.
Dragos OT-CERT is the Operational Technology – Cyber
The pro-Russia hacktivist group CyberVolk threatened Emergency Readiness Team dedicated to addressing the
OT resource gap that exists in industrial infrastructure.
Pakistan’s critical infrastructure and announced the
Designed to support asset owners and operators of industrial
development of a new CyberVolk ransomware. This infrastructure, Dragos OT-CERT provides free cybersecurity
alarming trend suggests that hacktivists could leverage resources for the OT/ICS community.
destructive malware to extend the impact of their operations.
In September 2024, Dragos discovered a Python-based
In July 2024, the Holy League formed as a coalition of malware named kurtlar.exe/kurtlar_scada.exe. The
pro-Russian hacktivists including CARR, CyberVolk, and malware connects to internet-exposed VNC servers and
over 50 other active personas. This alliance represents captures a screenshot of the access. Using evidence from
a substantial threat, targeting NATO, European nations, the malware, Dragos identified a Telegram channel where
Ukraine, and Israel. Their coordinated capabilities heighten TAT24-76 claimed to have used kurtlar.exe to compromise
risks for industrial organizations globally. several internet-exposed VNC servers hosting HMIs.
Hacktivists Claim Impacts Dragos uses Temporary Activity Threads (TATs) for
tracking and disseminating information about unidentified
to Critical Infrastructure
or developing cyber threat groups or activity. TATs serve
Hacktivism is a contemporary form of digital activism. It as a provisional classification for clusters of cyber threat
employs tactics like launching distributed denial of service activities that have not yet reached a level of analytical
(DDoS) attacks, defacing websites, and accessing internet- rigor to be designated as a threat group.
exposed devices to draw attention to political or social
causes amplified through social media. These hacktivist TAT24-76 developed kurtlar.exe/kurtlar_scada.exe and
personas may appear as formal groups or individuals, but, advertised a variety of offerings in their channel, including:
in practice, their names and branding are self-proclaimed • Initial access into organizations, public and private, via
monikers rather than established organizational entities. web shells
35

• VNC access to HMI and SCADA
devices
• Exploits (primarily focused on
WordPress)
• Database dumps
• DDoS tools
• A VIP channel containing private
hacking courses (including how
to identify Internet-exposed
devices, additional exploits, and
malware)
Example Screenshot of HMI Screen TAT24-76 Compromised
TAT24-76 uses their Telegram
channel to sell their malware by
Kurtlar_SCADA
showing evidence of successful runs on Windows
systems Take screenshot
compromises. This evidence included
and sell access
Stage 1:
screenshots of compromised HMIs, as
Intrusion Brute force
seen in the graphic at right. credentials
WEAPONIZE
After investigating the screenshots,
Dragos determined that a subset of RECON DELIVER INSTALL ACT
the victims were compromised and
TARGET EXPLOIT COMMAND
+ CONTROL
notified them through Dragos’s OT-
CERT victim notification service.
OT-CERT successfully notified Internet- Preference for
exposed victims in Israel
compromised victims, restricting VNC and the U.S.
servers
access to TAT24-76 and further
manipulation from buyers.
TEST INSTALL/
MODIFY
Despite their simplicity, kurtlar.exe Stage 2: DEVELOP DELIVER IC E S X A E T C T U A T C E K
and kurtlar_scada.exe are still ICS Attack In some cases,
defaced HMIs
effective against internet-exposed with Mr Robot
theme to prove
and poorly secured industrial devices access
running VNC servers. Strategies to
mitigate this threat include:
• Restricting access to any VNC
9%
server, especially on ports
TCP/5800, TCP/5900, and OT Watch identified 9 percent of
TCP/5901. If remote access is customers with VNC communicating
with external addresses.
required, use a VPN.
*A minor portion of these environments are untuned.
• Ensuring default and weak
credentials are changed.
CNV
)0095/PCT(
CNV
)0095/PCT(
2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
36

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
Execution Flow of kurtlar.exe and kurtlar_scada.exe
| The kurtlar.exe /  |                         | Input IP file as | Iterate over IPs and  |     |
| ------------------ | ----------------------- | ---------------- | --------------------- | --- |
|                    | Unsure how to find IPs  | CLI argument     | for each one perform  |     |
| kurtlar_scada.exe  | of exposed devices?     |                  |                       |     |
the next actions
TAT24-76 provides a
| VNC Malware | class in their paid VIP  |     |     |     |
| ----------- | ------------------------ | --- | --- | --- |
192.168.1.2:5900
|     | channel |     |     | 192.168.1.3:5900 |
| --- | ------- | --- | --- | ---------------- |
192.168.1.4:5900
kurtlar.exe iterates through a list
|     |     | ips.txt |     | . . . |
| --- | --- | ------- | --- | ----- |
of target IP addresses.

| kurtlar_scada.exe attempts to  |                |             | Connection not  |                     |
| ------------------------------ | -------------- | ----------- | --------------- | ------------------- |
|                                | Exit once all  | Brute force |                 | Attempt connection  |
successful,
|                                      | IPs have been  | credentials with |                 | without        |
| ------------------------------------ | -------------- | ---------------- | --------------- | -------------- |
| connect over VNC on TCP ports 5800,  |                |                  | Authentication  |                |
|                                      | connected to   | hardcoded list   |                 | authentication |
required
5900, and 5901, trying a hardcoded list
of credentials. If successful, it captures
a screenshot, with the IP address and
|     |     | Connection | Take  | Connection |
| --- | --- | ---------- | ----- | ---------- |
credentials used.
|     |     | Successful | screenshot | Successful |
| --- | --- | ---------- | ---------- | ---------- |
CyberArmyofRussia_Reborn  Based on their confirmed attacks and operations targeting
and Z-Pentest OT/ICS organizations, the U.S. Department of Treasury
sanctioned the members of CARR in July 2024.39
The CyberArmyofRussia (CARR), tracked by Dragos as
TAT24-22, is a self-proclaimed pro-Russia hacktivist group.
In September 2024, Z-Pentest, tracked by Dragos as TAT24-
TAT24-22 targets NATO and Eastern European countries
56, emerged on the scene and took on most operations
to gain clout and likely formal support from the Russian
targeting internet-exposed OT/ICS devices.
government.
Hunt3r Kill3rs
TAT24-22 uses DDOS attacks and accesses internet-
exposed OT/ICS devices. However, it is debatable whether  The hacktivist persona Hunt3r Kill3rs, tracked by Dragos
they understand the interfaces of OT/ICS devices they gain  as TAT24-45, escalated its activities by targeting internet-
exposed OT/ICS devices in Europe, Israel, and the United
access to or the impacts caused by their manipulations.
States, and focusing on weak or default authentication
In numerous incidents, after accessing an OT device, they
settings.
miscategorized the device’s location and industry facility
type. While their skillset is debatable, there are confirmed
attacks on U.S. water and wastewater and energy facilities,  Despite possessing limited technical capabilities, Hunt3r
Kill3rs achieved Stage 2 of the ICS Cyber Kill Chain for the
causing various levels of disruption. There are probable
third time, manipulating device data fields and resetting
attacks targeting organizations in:
passwords on exposed controllers. Although Dragos could
•  Water & Wastewater in Romania, Poland, and France
•  Food & Beverage in Spain, not verify operational impacts from the victims, these
•  Energy in United States and Germany compromises could cause loss of control, loss of view, and
operational disruptions.
39Treasury Sanctions Leader and Primary Member of the Cyber Army of Russia Reborn – U.S. Dept. of the Treasury
37

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
Hunt3r Kill3rs’ opportunistic targeting and visibility
on Telegram underscore a growing threat to industrial
environments, particularly where even trivial compromises
can cause operational disruptions. Dragos has observed
Hunt3r Kill3rs leveraging internet-exposed devices to
garner notoriety. This behavior aligns with broader trends
among self-proclaimed hacktivists.
Convergence of Adversaries
and Hacktivists
There is a growing convergence of interests between
sophisticated adversaries and hacktivist personas.
Dragos has seen them both use shared infrastructure and
intelligence to attack OT/ICS targets. Since at least 2022,
Dragos has confirmed convergence between:
• GRAPHITE and CARR
• KAMACITE and CARR
• ELECTRUM and CARR The strategic implications for ICS defenders are significant,
• ELECTRUM and KillNet as adversaries may transition between espionage-focused
• ELECTRUM and Solntsepek campaigns and destructive operations based on broader
• KAMACITE and XakNet objectives while leveraging hacktivist personas to conduct
lower-sophistication attacks. The role of hacktivist
There is also suspected convergence between: personas, whether as a deliberate distraction from the
• DYMALLOY and CARR primary attack or for other purposes, remains a subject of
• ALLANITE and CARR ongoing analysis and debate.
KillNet
Solntsepek
Confirmed Suspected
CARR
XakNet
Confirmed and Suspected Overlaps in Ukraine
38

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
The Ransomware Landscape
Ransomware is viewed as a legitimate threat for
multiple industries because of the disruptive nature
Although Dragos did not observe any specific ICS-
of a successful attack. Dragos first observed an tailored ransomware variants in 2024, ransomware
uptick in ransomware attacks against industrial adversaries halted production lines, impaired supply
chains, and exfiltrated sensitive data that could easily
organizations in 2022, and since then, the number of
be used in follow-on malicious activity. It is very likely
attacks has doubled year over year.
ransomware operators in 2024 implemented some
level of victim selection with a preference towards
In 2024, Dragos observed 1,693 industrial organizations organizations with a low tolerance for downtime.
with sensitive data and information posted onto various
ransomware groups’ dedicated leak sites (DLS). Although a
DLS posting is not indicative of a successful ransomware groups earlier in the year, an increasing number of intrusion
attack on its own, the sheer volume and clear upward vectors as the year went on, and/or the emergence of new
trend of industrial organizations getting attacked by ransomware adversaries later in the year.
numerous ransomware groups clearly highlight that
all OT/ICS asset owners and operators and industrial Manufacturing remains the top target for ransomware
organizations must be mindful of the current ransomware attacks against industrial organizations; more than 50
threat landscape and how it pertains to their respective percent of all observed ransomware victims were in
security posture and operations. the manufacturing sector, representing 1,171 attacks.
Ransomware groups know that even brief disruptions can
There was more than double the number of attacks in cause significant financial and logistical fallout, putting
the second half of 2024 over the previous two quarters. It safety at risk and making manufacturers more likely to pay.
is unclear what factors might have driven an increase in Other industrial sectors, including energy, transportation,
ransomware activity. Possible contributors could include law and industrial control system vendors, also remain high
enforcement actions taken against prominent ransomware on the list as ransomware groups refine their tactics to
Manufacturing
1,171
Industrial Control Systems Transportation Oil & Gas Communications
177 176 44 41
Electric Government Water Mining Renewables Datacenter
30 20 12 11 7 4
Ransomware by Sector
39

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
984
North America 419
Europe
137
Asia
47
Middle
24
East
Africa
56
26
South America
Australia/
New Zealand
Ransomware by Region
maximize pressure and impact. With these threats showing 2024. That number more than doubled during the second
no sign of slowing, organizations must prioritize resilience, half of the year (see chart next page).
proactive defenses, and incident response readiness.
The most active ransomware groups against industrial
Ransomware attacks against industrial organizations are organizations were RansomHub, Fog, and LockBit3.0.
not evenly distributed, and certain regions bear the brunt due Notably, RansomHub quickly escalated activities starting
to geopolitical tensions, economic incentives, and adversary in February 2024 by attracting ransomware affiliates from
focus. North America accounted for 984 attacks – 58 percent Cyclops and Knight. They claimed more than 300 victims
of all cases. Europe followed with 419 attacks, making up 25 across multiple critical infrastructure sectors in 2024. Fog
percent of the total. Understanding these regional patterns similarly expanded their operations into industrial sectors
is key to strengthening defenses, anticipating future threats, as 2024 went on and they were also one of the primary
and ensuring security strategies align with real-world risks. ransomware groups observed targeting vulnerable remote
services and appliances. LockBit3.0 operations were
Dragos tracked nearly 80 ransomware groups in 2024, disrupted by the international law enforcement effort
a 60 percent increase from the 50 groups observed in “Operation Cronos” in February 2024, but they were persistent
2023. Collectively, these groups attacked an average of 34 and remained a viable threat to industrial organizations
industrial organizations per week during the first half of throughout the year.40, 41
40The NCA Announces the disruption of LockBit with Operation Cronos - NCA; 41Unveiling the Fallout: Operation Cronos’ Impact on LockBit Following Landmark Disruption - TrendMicro
40

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
193
186
158
125
90
86
| LOCKBIT 3.0 |     | RANSOMHUB |     | PLAY |     | AKIRA |     | HUNTERS INT’L |     | BLACK BASTA |     |
| ----------- | --- | --------- | --- | ---- | --- | ----- | --- | ------------- | --- | ----------- | --- |
64
55
54
|       |     |              |     |       |     |        | 48  |           | 48  |             | 43  |
| ----- | --- | ------------ | --- | ----- | --- | ------ | --- | --------- | --- | ----------- | --- |
| 8BASE |     | MEDUSALOCKER |     | QILIN |     | CACTUS |     | MEOWLEAKS |     | DRAGONFORCE |     |
|       | 43  |              | 42  |       | 40  |        |     |           |     |             |     |
|       |     |              |     |       |     |        | 37  |           | 33  |             |     |
29
| INC RANSOM |     | BLACKSUIT |     | BIANLIAN |     | FOG |     | KILL SECURITY |     | LYNX |     |
| ---------- | --- | --------- | --- | -------- | --- | --- | --- | ------------- | --- | ---- | --- |
24
|           |     |          | 18  |          | 17  |                  | 14  |             | 14  |            | 13  |
| --------- | --- | -------- | --- | -------- | --- | ---------------- | --- | ----------- | --- | ---------- | --- |
| EL DORADO |     | RA GROUP |     | SAFEPAY  |     | FUNKSEC          |     | RANSOMHOUSE |     | CICADA3301 |     |
|           | 13  |          | 13  |          | 12  |                  | 11  |             |     |            |     |
|           |     |          |     |          |     |                  |     |             | 10  |            | 10  |
| NITROGEN  |     | RHYSIDA  |     | STORMOUS |     | DRAGONRANSOMWARE |     | ALPHV       |     | CL0P       |     |
10
|            |     |            | 9   |         | 8   |             | 8   |             | 7   |          | 7   |
| ---------- | --- | ---------- | --- | ------- | --- | ----------- | --- | ----------- | --- | -------- | --- |
| SARCOMA    |     | MONTI      |     | ABYSS   |     | BRAINCIPHER |     | ARCUS MEDIA |     | HELLDOWN |     |
|            | 7   |            | 7   |         | 7   |             | 6   |             | 6   |          | 5   |
| MEDUSABLOG |     | SPACEBEARS |     | THREEAM |     | ARGONAUTS   |     | TRIGONA     |     | EVEREST  |     |
|            | 4   |            | 4   |         | 4   |             | 4   |             | 4   |          | 4   |
D NUT LEAKS KAIROS MAD LIBERATOR TEAM UNDERGROUND TERMITE VALENCIA
|     | 3   |     | 3   |     | 3   |     | 3   |     | 3   |     | 3   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
BLACKOUT CLOAK DARKVAULT DISPOSSESSOR METAENCRYPTOR RANSOMEXX
|           | 2   |                | 2   |         | 2   |           | 2   |         | 2   |        | 2   |
| --------- | --- | -------------- | --- | ------- | --- | --------- | --- | ------- | --- | ------ | --- |
| BLACKBYTE |     | CIPHBIT        |     | DANON   |     | EMBARGO   |     | HELLCAT |     | ORCA   |     |
|           | 1   |                | 1   |         | 1   |           | 1   |         | 1   |        | 1   |
| BLUEBOX   |     | CUBA           |     | HANDALA |     | INTERLOCK |     | KNIGHT  |     | MALLOX |     |
|           | 1   |                | 1   |         |     |           |     |         |     |        |     |
| MYDATA    |     | RED RANSOMWARE |     |         |     |           |     |         |     |        |     |
Ransomware by Group/Strain
41

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
Ransomware Trends in 2024
Of the ransomware incidents Dragos responded
Dragos observed two noteworthy trends within the 2024
to in 2024, victim organizations that enforced strict
ransomware threat landscape:
network segmentation between IT and OT systems
• Ransomware adversaries using remote tools and and conducted offline backup testing significantly
shortened the recovery times and avoided paying
services.
the ransom. Conversely, organizations that did not
• Convergence of geo-politics, hacktivism, and employ network segmentation and had poorly
ransomware. secured remote access pathways led to more lengthy
recovery times, more involved incident response
efforts, more severe production downtime, and
Ransomware Adversaries Using
increased remediation costs.
Remote Tools and Services
Starting in 2023, Dragos noted a general trend of
adversaries targeting remote services and taking
PowerShell, certutil.exe, PsExec) to conceal malicious
advantage of the lack of basic network security defense
activities and remain undetected for extended periods
principles. That trend continued in 2024 as ransomware
of time.
adversaries largely used these resources – particularly VPN
appliances – to gain initial intrusion into victim networks
Dragos’s incident response efforts for ransomware
and move laterally through compromised systems, thereby
victims mirrored much of the observed “targeting
achieving Stage 1 of the ICS Cyber Kill Chain. Ransomware
remote services” trend. In fact, more than 50 percent of
adversaries were also observed leveraging credential-based
the ransomware incidents Dragos responded to in 2024
tactics, including pass-the-hash, brute force, and credential-
involved some element of a remote service, such as a
stuffing techniques to bypass multi-factor authentication
VPN appliance or remote desktop protocol (RDP) server
(MFA). Two examples of this are as follows:
being leveraged by adversaries. Further, 25 percent
• Eldorado and Play ransomware groups attacked
of the ransomware incidents resulted in a full OT/ICS
VMware ESXi environments to encrypt or disable
shutdown, and the other 75 percent of the incidents
virtual machines.42, 43
resulted in partial disruptions.
• Akira ransomware group consistently exploited
vulnerable VPN appliances to gain initial access Dragos’s observations from incident response
throughout 2024. engagements were reflected within the ransomware
ecosystem where initial access brokers (IABs) commonly
In addition to taking advantage of vulnerable remote exploited unpatched vulnerabilities in hypervisors, VPN
services, ransomware groups also continued using LOTL appliances, and remote access solutions, often within
strategies by using native administrative tools (e.g., hours of public disclosure, granting ransomware affiliates
20% 4433%%
OT Watch identified
43 percent of customers
OT Watch identified communicating to external
VMware ESXi in addresses via RDP protocol.
20 percent of customer *A minor portion of these
environments. environments are untuned.
42New Eldorado Ransomware Targets Windows, VMware ESXi VMs – Bleeping Computer; 43Play Ransomware Group’s New Linux Variant Targets ESXi, Shows Ties with Prolific Puma – Trend Micro
42

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
a low-barrier-of-entry method for attacking industrial ransomware within their operations in 2024: Handala, Kill
organizations and establishing a critical foothold within Security, and CyberVolk.
victim’s environments.
CyberVolk is the most unique example due to their
These findings strongly indicate that numerous ransomware launching a ransomware-as-a-service (RaaS) in June 2024
groups are leveraging low-barrier-of-entry intrusion tactics and then announcing they were developing a proprietary
against industrial organizations and capitalizing on a lack “CyberVolk” ransomware in July 2024.44 CyberVolk is a
of basic network and security hygiene practices. Until these self-proclaimed member of the hacktivist alliance called
elements are properly addressed and secured, ransomware Holy League, whose membership includes hacktivist
groups will continue exploiting them. personas such as CyberArmyofRussia_Reborn (CARR),
and they primarily target NATO-aligned countries using
Convergence of Geo-Politics, DoS attacks and ransomware. Based on their activities
Hacktivism, and Ransomware and claims on social media, CyberVolk appears to support
Russian state interests.
In 2023 and into early 2024, Dragos observed a trend of
hacktivist groups, or self-proclaimed hacktivist groups, There’s a realistic probability that this fusion of economic,
actively targeting and achieving Stage 2 of the ICS Cyber political, and ideological interests has the potential to
Kill Chain against industrial organizations and critical shape the ransomware threat landscape in 2025 and
infrastructure and services worldwide. A new concerning beyond, particularly in sectors critical to public safety and
evolution in the hacktivism threat landscape emerged economic stability that are viewed as strategic targets
in 2024, with hacktivist and self-proclaimed hacktivist of interest by hacktivist and self-proclaimed hacktivist
groups employing ransomware as part of their operations groups. Consequently, OT/ICS asset owners must become
against a variety of targets. more geopolitically aware if their organizations operate
within certain high-tension regions or are in sectors that
Three notable hacktivist groups were actively using supply critical services and utilities to the public.
44Ransomware Groups Demystified: CyberVolk Ransomware - RAPID7
43

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
Insights from Dragos Incident
Response
was operational errors due to hardware misconfiguration,
Throughout 2024, Dragos Incident Response mainly
hardware failure, or human error. Each incident involved
observed three kinds of incidents: ransomware
a disruption to operations to some degree. Although each
compromise, operational errors, and legacy
of these incidents was initially reported to Dragos as
malware infection. Incidents involving ransomware
potentially related to adversary activity, an investigation
or operational errors led to either partial or full
by incident responders concluded that they were not OT-
disruption to OT operations. Legacy malware
related cybersecurity incidents. Dragos recommends that
continues to be a problem in OT environments and
organizations activate their incident response retainer
leads to a weaker security posture.
even if it is unclear if they are dealing with an event
Ransomware Incidents caused by an adversary. With their abilities to analyze
network and host data, incident responders provide a
Ransomware compromises accounted for the majority capability that process engineers and operators often lack.
of cases that Dragos responded to, with 25 percent This alone can significantly reduce the time needed to
resulting in a complete shutdown of an OT site, and 75 complete root cause analysis, thereby decreasing mean
percent resulting in at least some disruption to operations. time to recovery.
Twenty percent of all incidents involved an exploitation
of remote access, including VPN exploits, remote access Legacy Malware
applications, and RDP from corporate.
Dragos Incident Response also encountered incidents
due to legacy malware. Though similar to ransomware,
While data exfiltration is common in IT-related
Dragos tracks this separately due to strains such as
ransomware incidents, Dragos did not find signs of an
WannaCry and other malware historically present
adversary exfiltrating data from OT environments. Even
within OT systems. This malware lingers within legacy
though the adversaries explicitly threatened organizations
environments and uses exploits successfully due to
with data exfiltration and disclosure as part of their
inadequate patching, architectural deficiencies, and other
ransom demands, they failed to act on those threats.
factors introduced by out-of-date operating systems.
No ransoms were paid, and organizations possessed
Often, the malware discovered is found “headless” in
adequate capacity to restore operations without engaging
that the malware will continue to spread but will not be
adversaries. Despite this capacity to recover, Dragos noted
accessible by any recent adversaries. While the presence
that backups were not always readily accessible and that
of headless malware is not an indicator of an active
sites were often materially impacted as part of incidents
intrusion, it degrades general cybersecurity readiness and
reported this year.
leads to time-consuming remediation efforts. Further, the
Operational Errors Causing Incidents security monitoring alerts generated by headless malware
can be symptomatic of wider issues such as additional
Aside from ransomware, the next highest type of incident policy violations and poor patching practices.
44

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
The Importance of Network If process logs did not record setpoint changes or read
Security Monitoring operations, it would be impossible to verify access and
potential process manipulation. Deploying ICS protocol
ICS protocol aware network visibility is key in quickly aware networking monitoring pre-incident would have
scoping the extent of a potential compromise and detected read/write communication to controllers, making
identifying systems to further analyze the root cause of it easier to verify potential process manipulation. Even
a compromise. In one case, due to the Dragos Platform if the root cause is human error or hardware failure,
having been deployed at the affected site before an monitoring helps identify the issue more quickly, reducing
incident, and the Dragos OT Watch team actively both analysis time and overall downtime.
monitoring the Platform, root cause analysis, remediation,
and mitigation was performed in about 15 hours. The Basics Matter
In other cases, even when monitoring was deployed post- It bears repeating that an organization that is implementing
incident, it still played a key role in significantly shortening the SANS ICS 5 Critical Controls will be able to significantly
the time needed to make an informed decision about reduce the impact to OT in case of a breach, likely have
reconnecting an isolated OT network, thereby minimizing enough time to react to a breach before it turns into a full
downtime. If network-based security monitoring was not compromise, will be aware of key processes and systems to
feasible for whatever reason, the analysis for scoping and protect and collect data from if analysis is needed, and have
root cause depended entirely on host-based forensics and incident response playbooks that focus on the most likely
log review. This not only demanded considerable effort scenarios, allowing responders to streamline their efforts.
to collect forensic data from OT systems in the field, but Investing in the efforts of doing the basics right, will result
also significantly extended the time required for analysis. in less impact and lower downtime.
45

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
Vulnerabilities
Industrial systems weren’t built with cybersecurity identified as a new area to explore. In the short-term,
in mind, yet today’s adversaries are actively hunting Dragos now has signature-based detections for a variety
for weaknesses in OT devices and protocols. From of attacks using CANopen over a common PLC network
unpatchable flaws to design limitations, these protocol. Longer-term, Dragos plans to implement tooling
vulnerabilities create openings for adversaries to to address Turducken protocols in fieldbus equipment. This
disrupt operations or gain initial access. As threats tooling will provide greater visibility for detecting attacks
evolve, so must our approach - focusing not just on and identifying potential misconfigurations.
patching, but on understanding and mitigating risks
before they can be exploited. Turducken protocols are application layer protocols which
are layered atop one another. In the case of Dragos’s
Fieldbus: Servo Drives 2024 research, the protocol layers were Modbus-RTU,
Drive New Research Areas layered atop CANopen, which was layered inside of the
proprietary CODESYS protocol. During documentation
Dragos continued fieldbus protocol research in 2024.45 review, Dragos also identified products which layer
This year, research focused on the CANopen protocol Modbus-RTU atop CANopen atop Modbus/TCP.
implemented in servo drives. A major finding from this
research was highlighting the risk that layered protocols Previously, Dragos researched a number of Turducken
like CANopen pose to organizations and the lack of protocols related to LOGIIC Project 12, where the HART
detection mechanisms for those attacks. These layered protocol was often layered on top of both proprietary
protocols are called ‘Turducken’ protocols and have been protocols and common industrial protocols.46 In a different
45Fieldbus - Wikipedia; 46Excerpt: LOGIIC’s Project 12 Safety Instrumentation Report – Global Cybersecurity Alliance
46

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
effort, Dragos researched Omron devices which showed Fortunately, end user security recommendations for both
EtherCAT layered over a proprietary NXBus protocol, itself types of exposure can be performed using control systems
placed inside of HTTP requests.47 logic itself.48 Sensitive settings can be monitored by the
controller logic, with safe shutdown logic executed if
Dragos considers most fieldbus equipment as insecure- device settings are changed out-of-band.
by-design. This means that engineering issues exposed
by the bottom-level protocol are not necessarily worthy of To protect fieldbus equipment, ICS community awareness
CVEs. Still, detections should determine if attacks, or even must change. A common assumption is that field devices,
erroneous changes, are made against this equipment. and especially instruments and actuators, are insecure-
by-design. What is not well-considered by owners is the
These protocols are often composable (as with Modbus- accessibility of this equipment.
RTU/CANopen/X, where X may be CIP or CODESYS If you use a device type manager (DTM) to manage fieldbus
or Modbus/TCP), and each layer of the composable equipment over an Ethernet network, the underlying
protocol has its own quirks, such as fields with variable protocol for access may not be secure. While the protocol
lengths, request pipelining, and even undocumented may be nested and appear complex or even nonsensical at
functionality, making it difficult to write network-based first glance, the apparent complexity of the protocol may
analytics for them. be overcome by researchers and threat groups.
As interest increases in identifying attacks against low- If you do not use DTMs to manage your fieldbus
level equipment, the natural engineering response should equipment, the devices may still be exposed, so restrict
be composable dissectors: the ability to easily extract an access to engineering ports on, for example, PLCs which
inner payload and pass it to a choice of inner dissectors, have fieldbus communications features and to fieldbus
ad infinitum, until the entire Turducken is unraveled. couplers and protocol translators. These devices may
Looking through Dragos Neighborhood Keeper datasets, translate fieldbus protocols into more common Modbus/
“several models of PLCs with Turducken protocol support TCP, Ethernet/IP, DNP3, or other process bus protocols.
were identified. Dragos Neighborhood Keeper is an opt- It is important to consider not just how you use and
in collective defense and community-wide visibility manage your devices, but also how they could be used and
solution that enables a more informed industrial defense managed – potentially by someone other than you.
by sharing threat intelligence across industries and
geographic regions. Several PLC models with Turducken IoT Equipment in ICS Environments
protocol support include:
Several vulnerabilities in IoT devices were exploited as
• Rockwell Automation ControlLogix systems with
recently as November 2024 to propagate the Mirai botnet,
HART-aware IO modules. These modules allow direct
which maintained upwards of 15,000 active IP addresses
access to instrumentation, including attacks outlined
used to conduct DDoS attacks.49 This long-running botnet
in LOGIIC Project 12.
executes fully automated infection of IoT and OT devices
• Schneider Electric controllers using CODESYS runtime
allowing it to hide malicious processes, scan for vulnerable
and CANopen support. These devices provide direct
devices, proliferate, and update itself. This botnet is
SDO access to CANopen devices including the ability to
successful because most IoT equipment runs inadequately
reconfigure and remotely operate these components,
hardened, open source GNU/Linux under the hood.
out of band with the process control logic.
47Exploiting Omron’s NEX PLC Runtime and Protocol – S4, Logan Carpenter; 48Safety Instruments Testing: Spotting and Stopping Process Attacks - Dragos; 49Mirai Botnet Variant Exploits Four-Faith Router
Vulnerability for DDoS Attacks – The Hacker News
47

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
With easy to exploit exposures such as TELNET or SSH capabilities to capture Real-Time Streaming Protocol
enabled by default and trivial infection mechanisms (RTSP) streams, perform brute forcing of authentication
like unauthenticated command injection, many of these over multiple protocols, conduct DoS attacks, and more. IoT
devices have ‘low-hanging fruit’ type vulnerabilities Exploit contains roughly 175 exploits targeting OT devices
that can give low-level access to tamper with the device with the ability to speak numerous industrial protocols,
firmware. The shared operating systems and CPU as well as hundreds of additional exploits for generic IoT
architectures of these devices make them vulnerable to devices. While this toolkit appears to be a red teaming
existing tools. Thus, building management systems like tool developed for vulnerability scanning purposes, its
HVAC, lighting, physical access control, and physical public existence will no doubt filter into automated tools.
security systems are easy targets for adversaries. While Dragos has no evidence of malicious use of the IoT Exploit
these systems may not directly maintain production, toolkit in our telemetry. “Dual-use tools” – those created for
an outage of any one of them can stop production. research or defensive purposes with the ability to be used
For example, if a lighting control system falls offline, maliciously – are commonly used amongst adversaries. As
workers may not be able to work. Similarly, in regulated such, there is a strong likelihood that IoT Exploit or some
environments such as pharmaceuticals and food component of it will eventually be used maliciously.
manufacturing, loss of HVAC and climate control systems
will often require production to halt. As such, it is best to One of the best ways to protect IoT systems is simple:
view IoT hardware used in an industrial setting as a ‘part of identify and change default passwords. This is especially
the process’ from a plant perspective. important in internet-exposed systems.50 Additionally,
restrict access to device management interfaces and
In 2023, Dragos analyzed a tool called IoT Exploit, an monitor for exploitation of these devices. And, most
“IoT device vulnerability scanning, verification, and importantly, have a plan in place should these systems
exploitation toolkit” that bundles more than a thousand stop functioning correctly. For example, the ability to
publicly available exploits targeting IP cameras, NVRs, manually turn off magnetic door latches should be a part
DVRs, routers, and industrial devices. It contains of every plant’s safety plan.
50OT Cybersecurity Best Practices for SMBs: Managing Default Passwords and Identifying OT/ICS Devices Exposed to the Internet - Dragos
48

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
Supply Chain and Third-Party applications and equipment to add functionality, simplify
integration, and improve compatibility with other systems.
Components: Acknowledging
Hidden Risks
Products often rely on third-party components, so any
vulnerabilities in those components can directly impact
Third-party components expand or support the capabilities
the security and functionality of the dependent products.
of OT equipment and systems. These components, often
While a vendor-manufactured product, such as a PLC, may
unknown to the end-users, can have vulnerabilities
be up to date with its own security patches for issues under
that compromise the security of the component and,
the vendor’s control, it could still include a third-party add-
consequently, the entire product into which it is built.
on component with an unaddressed vulnerability. In such
Fortunately, these risks can be mitigated through
cases, the vendor might implement temporary mitigations
vulnerability management, software bill of materials
to reduce the risk, but addressing the root cause of the
(SBOM) implementation, and other proactive strategies.
issue would largely depend on the third-party creator to
provide a proper fix.
Third-party components are software or hardware
modules created by an external entity other than the
In April 2024, the Bianlian ransomware group attempted
developer of the underlying core software. Often, these
to use the Palo Alto Networks PAN-OS vulnerability,
third-party components are designed by a company,
CVE-2024-3400, against organizations in the water
developers, or research organizations to integrate products
and wastewater, manufacturing, and mining sectors in
from different vendors and add functionality to products.
multiple regions. Notably, the Siemens RUGGEDCOM
For example, OEMs of industrial products may incorporate
APE1808 product integrates Palo Alto Networks PAN-
software modules from another vendor into their
OS as a third-party component. Since CVE-2024-3400
exists in PAN-OS, the Siemens product is susceptible
to the same vulnerability. While there is no evidence of
Siemens products being actively targeted due to CVE-
19%
2024-3400, this example highlights the risk of third-party
of advisories analyzed in components. The Siemens product’s reliance on PAN-OS
2024 were related to third- provides a potential avenue for exploitation to adversaries
party vulnerabilities.
and, as a result, exposes the owning organizations to
intrusion.
49

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
Practical Solutions for and more efficient responses to critical vulnerabilities.
Managing Third-Party Risks This transparency fosters operational resilience and
supports proactive risk management specific to third-party
Asset operators and owners should focus on vulnerability
integrations.
management by identifying and addressing the most
critical vulnerabilities in their environment. This approach
DLL Hijacking:
helps reduce the likelihood of exploitation, protects critical
An Ongoing Problem for OT
operations, and keeps systems running smoothly by
addressing risks before an adversary can take advantage
Dragos currently tracks 104 dynamic-link library (DLL)
of a vulnerability. The Dragos Platform, which supports
hijacking vulnerabilities impacting industrial software.
risk-based vulnerability management and prioritization,
Dragos vulnerability researchers view these vulnerabilities
can simplify this process. Additionally, following the SANS
as low-hanging fruit; they are usually easy to discover and
ICS 5 Critical Controls framework, which emphasizes
exploit. These exploits are highly versatile and can allow an
actions like secure configurations and continuous
adversary to gain initial access, escalate privileges, evade
vulnerability monitoring, can provide a structured and
detection, or gain persistence on a Windows host system.53
effective approach to managing these risks.51
DLL hijacking is a type of vulnerability that abuses a
For vendors, implementing an SBOM is essential.52 This
DLL search order algorithm in the Microsoft Windows
document should list all software versions and add-on
operating system to trick a vulnerable application into
components within a product. By providing clear visibility
loading adversary-created code.
into a product’s components, an SBOM enables faster
Malicious DLL is Planted in a Location Searched Before Where the Legitimate DLL Resides
Attacker plants
malicious DLL
1. Directory where app loaded
2. System directory
3. 16-bit system directory
4. Windows directory
Legit DLL
5. Current directory
found here
6. Directories listed in PATH env var
51The Five ICS Cybersecurity Critical Controls – SANS; 52SBOM - CISA; 53Suggested Practices to Defend Against DLL Hijacking - Dragos Inc.
50

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
Historically, DLL hijacking has been leveraged against industrial organizations several times.
Stuxnet exploited CVE-2012-3015 to trick Siemens SIMATIC manager software into executing a
June
malicious DLL masquerading as S7hkimdb.dll, which then decrypts and loads the main Stuxnet payload
2010
with administrator privileges.54 Stuxnet was deployed to slow Iran’s development of enriched uranium.
APT10 used DLL hijacking to deploy credential theft tools in Operation Cloud Hopper, a cyber espionage
April
2017 campaign targeting multiple sectors, including industrial manufacturing, energy, mining, and more.55
MuddyWater leveraged DLL side-loading in the POWGOOP malware, a remote access trojan that
February targeted government, oil and gas, telecommunications, and more.56 While remote access trojans (RATs)
2022
can allow adversaries to gain full administrative privileges and remote control of a target computer,
public reporting indicates that this activity was primarily espionage-focused.
Cotx/CotSam/DNSep malware targeted military industrial organizations in Eastern Europe and
August
Afghanistan and used DLL hijacking in security software to decrypt backdoors.57 These backdoors
2022
provided arbitrary command execution and collected host information. Kaspersky states that analysis
of threat activity indicates these malware families were deployed for cyberespionage purposes.
The Meatball and FourteenHi malware families targeted Eastern European industrial organizations and
July
2023
the Russian government. They used DLL hijacking to install a remote access trojan.58
MuddyWater used DLL hijacking to escalate privileges in a campaign against Israeli airlines and airports
Sept
2023 in September and October 2023.59
A variant of the HEADLACE malware family, a Batch-based backdoor used by GRAPHITE, contained a
Sept DLL side-loading component. CERT-UA reported that HEADLACE was used against a Ukrainian critical
2023
infrastructure entity.60
July APT41 used DLL hijacking to execute the DUSTTRAP malware, a remote access trojan used against the
2024
automotive sector and shipping and logistics organizations.61
Dragos encourages ICS asset owners to hunt for DLL • Audit application directories to ensure Everyone and
hijacking vulnerabilities in their systems and implement Standard Users groups do not have write access.
mitigations, such as:
• Enabling the CWDIllegalInDllSearch registry key on an Dragos encourages OT vendors to review the Microsoft
application-specific basis. Dynamic-Link Library Security webpage for best
• Following the principle of least privilege when running programming practices to reduce the occurrence of the
applications. vulnerability in their software products.
54Stuxnet 0.5: The Missing Link – Symantec (via gwu.edu); 55Operation Cloud Hopper - PwC, BAE; 56MAR-10369127, MuddyWater – CISA; 57Targeted attack on industrial enterprises and public institutions –
Kaspersky; 58Common TTPs of attacks against industrial organizations – Kaspersky; 59Iranian Nation-State APT Groups ‘Black Box’ Leak - ClearSky; 60APT28 Cyber attack – CERT-UA; 61APT41 Has Arisen From
the DUST – Mandiant
51

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
“Now, Next, Never” Now vulnerabilities are:
• Remotely exploitable
Vulnerability Framework
• Require no authentication or authentication is easily
The Common Vulnerability Scoring System (CVSS) is bypassed
inadequate for prioritizing vulnerabilities in ICS.62 CVSS • Impact ICS processes or allow new access to ICS
relies on numerical scoring to evaluate vulnerabilities • Actively exploited by advisories or
based on technical attributes, but it was not originally have a public proof of concept
designed with industrial systems in mind. As a result,
CVSS lacks the contextual information necessary Now vulnerabilities have a patch
or alternative mitigation, such as
for conducting risk assessments specific to ICS.
restricting access to vulnerable ports,
For example, CVSS fails to account for whether a
or proper engineering process design.
vulnerability impacts the ICS process, or if mitigating
These account for 6 percent of vulnerabilities in ICS.
a vulnerability will render a device inoperable for the
owner. To address these situations, Dragos developed
a framework for sorting vulnerabilities into three
Next vulnerabilities are:
categories: Now, Next, and Never. This framework helps
• Remotely exploitable
asset owners identify and prioritize the vulnerabilities
• Not actively targeted by adversaries
with the highest risk to their operational process.
• Could impact operations
• Require adversaries to do prep
Dragos monitors emerging threats, their techniques,
work such as credential stealing
and the vulnerabilities they exploit. The “Now, Next,
Never” model helps accurately capture the true impact
of these vulnerabilities, empowering organizations
Next vulnerabilities are mostly
with the guidance needed to respond effectively to mitigated through good network
emerging threats. hygiene or measures like network
segmentation included as part
of the Defensible Architecture control in the SANS ICS
The high-level vulnerability attributes covered by this
5 Critical Controls. These account for 63 percent of
process include: vulnerabilities in ICS.
• Impacts to Operations
• Active Exploitation or Public Proof-of-Concepts
• Network Exploitability
Never vulnerabilities are:
• Insecure-by-Design Features and Mitigation
• Difficult to execute
Availability
• The same risk that exists
• Authentication and User Interaction Requirements
inherently in ICS
• Broader ICS Network Access Capabilities
(insecure-by-design).
Never vulnerabilities account for
31 percent of vulnerabilities in
ICS, and are not worth the effort to remediate.
62Common Vulnerability Scoring System SIG - FIRST
52

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
Vulnerability Trends on protecting critical systems and mitigating risks while
maintaining operational needs with little to no disruption.
Because OT environments are subject to different
regulations and must remain operational for safety Dragos prioritizes vulnerabilities that, if exploited,
and production, asset owners cannot mitigate can cause a deep impact on industrial processes. Key
system vulnerabilities in the same timeframe as in IT considerations include:
environments. While IT can be more flexible in allowing • Are the vulnerabilities actively exploited?
updates to mitigate vulnerabilities, OT’s emphasis on • Do the vulnerabilities provide direct access to
maintaining day-to-day operations without interruption OT/ICS networks?
complicates vulnerability management and needs • Can the vulnerabilities cause a loss of view or
a strategic plan. Dragos focuses on vulnerability loss of control to the process?
management with OT challenges at the forefront, focusing
As our research has shown, CVSS scores alone often do not reflect the risk in operational environments. Dragos
digs deeper to find true severity levels and mitigation options, score and accuracy corrections, and provide context
to help defenders. In 2024, Dragos found that:
This growth is due in part to the number of
perimeter devices being actively exploited
in industrial organizations related to
hacktivism, ransomware, and threat groups.
1166%%
in 2023
4.5% 7700%% 2222%% 3399%%
of vulnerabilities had a Proof- of vulnerabilities were deep of advisories were of vulnerabilities could cause
of-Concept (POC) and were within the ICS network. This network-exploitable both a loss of view and a loss
actively exploited means that devices associated and perimeter-facing of control.
with the vulnerabilities were
Purdue Level 3.5 and below,
closer to the process.
53

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
In 2024, 22 percent of advisories contained incorrect data, Some advisories alerted asset owners to
which can prevent accurate prioritization for a problem without a solution.
patch management and mitigation.
2%
Only 2266%% of public advisories
provided
offered no patch.
alternate
mitigations 1188%% of public advisories
to a provided
had no patch and
patch or
no mitigation.
primary
1111%% 77%% 33%% mitigation
advice. 47%
of CVEs HAD were MORE were LESS
Dragos provided
ERRORS in them, SEVERE than the SEVERE than alternate mitigation
advice for 47 percent
which makes it public advisory reported
of advisories that were
more difficult to missing both patches
and mitigations.
prioritize correctly
Out of 606 public advisories that Dragos assessed in 2024:
606
advisories 5577%% The number of
113
ICS-specific protocol
network-exploitable
had a patch but
vulnerability advisories
no mitigations, a
that provided alternate
3 percent
mitigation decreased by 47
increase from
more than half: from
2023
113 in 2023 to 47 in 2024.
2023 2024
Overall, there was a marked decline in the number of errors seen in assessed CVEs from 2023 to 2024.
CVE errors CVEs with Proof of Concepts After more research… Advisories with actively
exploited CVE errors
2299%% 22% 151 (7 percent)
538
of CVEs 5%↑
in 2023 in 2024
scored higher
387
after further
research
27 of 31
151 included
55
POCs
2023 2024 2023 2024
CVE errors fell from 55 (27 percent)
29 percent in 2023 to 22 percent Dragos researchers also observed a scored In exploit analysis, 2024 saw an
in 2024, indicating that vendors drastic decrease in the total number of lower increase by 5 percent in the total
and researchers are scoring CVEs with POCs. In 2023, there were number of advisories with CVEs that
vulnerabilities more accurately 538 CVEs with POCs and only 387 in were actively exploited.
upon release. 2024.
54

2025 OT/ICS CYBERSECURITY REPORT • YEAR IN REVIEW
#2 Defensible Architecture
Call to Action
Fully understand your attack surface. Proactively
conduct annual attack surface analysis and prioritize
Industrial operations are now firmly in the network gateways and perimeter resources such as VPN,
crosshairs of state-sponsored threat groups, cyber RDP, and SSH devices targeted by BAUXITE. One easy
criminals, and hacktivists, all seeking to exploit way to accomplish this would be to leverage tools such
ICS vulnerabilities for espionage, disruption, and as Shodan and Censys to perform external analysis of
destruction. The 2025 OT/ICS Cybersecurity Report assets that may be “exposed” to the public-facing internet.
makes one fact abundantly clear: adversaries are Once inside the network, audit firewall rules and validate
evolving faster than defenders. the attack surface within the network to prevent lateral
movement from adversaries like VOLTZITE with NP-View.
Adversaries are not just testing OT networks—they
are actively embedding themselves within critical #3 Visibility and Monitoring
infrastructure, positioning for long-term access,
Increase visibility and monitoring. OT-aware monitoring
operational disruption, and potential large-scale
solutions, like the Dragos Platform, can detect adversaries’
consequences. The use of living-off-the-land techniques,
subtle movements before they strike, steal information,
ICS malware, and targeted reconnaissance proves that
or take other actions. The Dragos Platform also alerts on
these groups understand industrial systems better than
configuration and command code changes, helping teams
ever before.
decipher between security events and engineering mishaps.
Organizations can no longer afford passive defense
strategies or outdated security postures. The time for
#4 Secure Remote Access
reactive security is over. Defenders must move toward
continuous monitoring, proactive threat hunting,
Focus on remote access. Vendor remote access continues
and incident response capabilities tailored for OT
to be an attack vector seen in Dragos Incident Response
environments. Foundational practices like the SANS ICS 5
cases. Ad hoc access points should undergo the same
Critical Controls still provide OT/ICS asset owners with the
scrutiny as main firewalls and corporate VPN connections
best means to prepare for potential cyber events stemming
with increased access logging, alerting, and multifactor
from geopolitical conflict.
authentication.
#1 Incident Response Plan:
#5 Risk-Based Vulnerability
Update OT Incident Response Plans – or ensure that you Management
have one. Adversaries are becoming more OT/ICS aware,
Ensure your approach to vulnerability mitigation is
and their tactics, techniques, and procedures (TTPs) are
strategic and focused on real-world threats that apply
targeting deeper into industrial environments. Ensure
to your industry. Enrich your understanding of CVEs to
your plans have ways to respond to and recover, for
verify they are accurate, focusing on those that will cause
example whether SCADA servers have been encrypted by
a loss of view or control of the process. Then, make a plan
ransomware or BAUXITE-modified PLC logic.
and execute the plan, even if it is a multi-year plan.
55

Dragos is an industrial (OT/ICS) cybersecurity
company on a mission to safeguard civilization.
Dragos is privately held and headquartered in
the Washington, D.C. area with regional presence
around the world, including Canada, Australia,
New Zealand, Europe, and the Middle East.
Request a Demo Contact Us
Copyright © 2025 Dragos, Inc. All Rights Reserved.