# OT/ICS Cybersecurity Report - 8th Annual Year in Review - 2025

## Table of Contents
- [Introduction](#introduction)
- [Defender’s Guide to the Current Threat Landscape](#defenders-guide-to-the-current-threat-landscape)
- [Adversaries Targeting OT: Awareness Over Sophistication](#adversaries-targeting-ot-awareness-over-sophistication)
- [Defender Progress: Incremental But Uneven](#defender-progress-incremental-but-uneven)
- [OT-Centric Cyber Operations Increase as Geopolitical Tension and Conflicts Continue](#ot-centric-cyber-operations-increase-as-geopolitical-tension-and-conflicts-continue)
- [The Ukraine-Russian Conflict Fuels Activity for Established Dragos Threat Groups](#the-ukraine-russian-conflict-fuels-activity-for-established-dragos-threat-groups)
- [KAMACITE Technical Update](#kamacite-technical-update)
- [KAMACITE Campaigns](#kamacite-campaigns)
- [ELECTRUM Technical Update](#electrum-technical-update)
- [ELECTRUM Campaigns](#electrum-campaigns)
- [Geopolitical Tensions in Asia Facilitate Further VOLTZITE Activity](#geopolitical-tensions-in-asia-facilitate-further-voltzite-activity)
- [VOLTZITE Technical Update](#voltzite-technical-update)
- [VOLTZITE Campaigns](#voltzite-campaigns)
- [Ivanti VPN Zero-Day Campaign (December 2023)](#ivanti-vpn-zero-day-campaign-december-2023)
- [Telecom and EMS Campaign (January 2024)](#telecom-and-ems-campaign-january-2024)
- [ISP and Telecommunications Campaign (August 2024)](#isp-and-telecommunications-campaign-august-2024)
- [JDY Botnet (Late 2024)](#jdy-botnet-late-2024)
- [Dragos Identifies Two New Threat Groups in 2024](#dragos-identifies-two-new-threat-groups-in-2024)
- [Introducing GRAPHITE](#introducing-graphite)
- [GRAPHITE Campaigns](#graphite-campaigns)
- [Introducing BAUXITE](#introducing-bauxite)
- [BAUXITE Campaigns](#bauxite-campaigns)
- [Unitronics Campaign (November 2023-January 2024)](#unitronics-campaign-november-2023-january-2024)
- [Sophos Firewall Attack (April 2024-May 2024)](#sophos-firewall-attack-april-2024-may-2024)
- [Reconnaissance Scanning Campaign (June 2024-July 2024)](#reconnaissance-scanning-campaign-june-2024-july-2024)
- [IOControl Campaign (Late 2023-2024)](#iocontrol-campaign-late-2023-2024)
- [ICS-Focused Malware Increasingly Used as a Tool in Conflict-Driven Campaigns](#ics-focused-malware-increasingly-used-as-a-tool-in-conflict-driven-campaigns)
- [BlackJack Claims Disruption of Industrial Sensors in Moscow](#blackjack-claims-disruption-of-industrial-sensors-in-moscow)
- [The Fuxnet Malware](#the-fuxnet-malware)
- [Lessons from Fuxnet](#lessons-from-fuxnet)
- [FrostyGoop Malware Impacts Heating in Ukraine](#frostygoop-malware-impacts-heating-in-ukraine)
- [The FrostyGoop Malware](#the-frostygoop-malware)
- [Lessons from FrostyGoop](#lessons-from-frostygoop)
- [An ICS Malware Definition](#an-ics-malware-definition)
- [ICS Malware Definition](#ics-malware-definition)
- [Three Properties of ICS Malware](#three-properties-of-ics-malware)
- [ICS-Capable](#ics-capable)
- [Designed with Malicious Intent](#designed-with-malicious-intent)
- [The Ability for Adverse Effects on OT Environments](#the-ability-for-adverse-effects-on-ot-environments)
- [What Does the ICS Malware Definition Mean for Asset Owners?](#what-does-the-ics-malware-definition-mean-for-asset-owners)
- [Hacktivists Continue to Wave Their Flags in Support of Certain Geopolitical Conflicts](#hacktivists-continue-to-wave-their-flags-in-support-of-certain-geopolitical-conflicts)
- [Hacktivists Claim Impacts to Critical Infrastructure](#hacktivists-claim-impacts-to-critical-infrastructure)
- [OT-CERT Notifies TAT24-76 Victims of HMI Compromise](#ot-cert-notifies-tat24-76-victims-of-hmi-compromise)
- [The kurtlar.exe / kurtlar_scada.exe VNC Malware](#the-kurtlar.exe--kurtlar_scada.exe-vnc-malware)
- [CyberArmyofRussia_Reborn and Z-Pentest](#cyberarmyofrussia_reborn-and-z-pentest)
- [Hunt3r Kill3rs](#hunt3r-kill3rs)
- [Convergence of Adversaries and Hacktivists](#convergence-of-adversaries-and-hacktivists)
- [The Ransomware Landscape](#the-ransomware-landscape)
- [Ransomware Trends in 2024](#ransomware-trends-in-2024)
- [Ransomware Adversaries Using Remote Tools and Services](#ransomware-adversaries-using-remote-tools-and-services)
- [Convergence of Geo-Politics, Hacktivism, and Ransomware](#convergence-of-geo-politics-hacktivism-and-ransomware)
- [Insights from Dragos Incident Response](#insights-from-dragos-incident-response)
- [Ransomware Incidents](#ransomware-incidents)
- [Operational Errors Causing Incidents](#operational-errors-causing-incidents)
- [Legacy Malware](#legacy-malware)
- [The Importance of Network Security Monitoring](#the-importance-of-network-security-monitoring)
- [The Basics Matter](#the-basics-matter)
- [Vulnerabilities](#vulnerabilities)
- [Fieldbus: Servo Drives Drive New Research Areas](#fieldbus-servo-drives-drive-new-research-areas)
- [IoT Equipment in ICS Environments](#iot-equipment-in-ics-environments)
- [Supply Chain and Third-Party Components: Acknowledging Hidden Risks](#supply-chain-and-third-party-components-acknowledging-hidden-risks)
- [Practical Solutions for Managing Third-Party Risks](#practical-solutions-for-managing-third-party-risks)
- [DLL Hijacking: An Ongoing Problem for OT](#dll-hijacking-an-ongoing-problem-for-ot)
- [“Now, Next, Never” Vulnerability Framework](#now-next-never-vulnerability-framework)
- [Vulnerability Trends](#vulnerability-trends)
- [Call to Action](#call-to-action)

# Introduction
Throughout the year, Dragos identifies threats to operational technology (OT) and industrial control systems (ICS) infrastructure, conducts services to help defenders mature their program, and prioritizes mitigations for resilient operations. Enhanced by Dragos telemetry, we approach our eighth annual Year in Review report with field-tested guidance. It serves to provide several detailed examples of key attack paths Dragos observed as well as some of the context and motivation behind these attacks. 
If this is the beginning of your OT/ICS cybersecurity journey, welcome and don’t be alarmed. Start your year off by systematically identifying your organization’s exposure and work to reduce that exposure as much as possible. Read more about threats to exposed assets such as BAUXITE on page 22 and KurtLar SCADA on page 37.
If you already know your exposure, or have a plan to reduce it, consider the attack scenarios mentioned throughout this report and decide whether you’d be susceptible to these same attacks. Use these scenarios to inform visibility and monitoring strategies, create your incident response plans, and plan segmentation efforts.
If you have a good threat prevention strategy, it’s time to test it. Consider the attack scenarios mentioned throughout this report and identify visibility gaps. Would you notice if an adversary downgraded your firmware? Read more on FrostyGoop malware and associated attack chain on page 29.
If vulnerability management seems overwhelming, read how OT vulnerability management is different than IT in the Vulnerability Trends section on page 53. Learn how to prioritize mitigation and remediation of vulnerabilities with the “Now, Next, Never” framework on page 52. 
Buckle in and get ready to hunt. Hacktivists tell you who they are, but we continually observe adversaries hiding amongst the noise. Read more about ELECTRUM’s AcidPour on page 13 and VOLTZITE on page 14.
No matter your cybersecurity maturity, read on. From ICS threat groups and hacktivists to ICS malware attacks and criminal ransomware, you will learn about the latest real-world attacks, and what you can do about them. Combined with insights from our incident responders and guidance from our vulnerability team, this report provides a comprehensive look at the most important cyber threats affecting OT environments and organizations.

![KEY HIGHLIGHTS: BY THE NUMBERS]

Key Vulnerabilities Findings
- 22% of advisories had incorrect data in 2024.
- Dragos provided mitigations for 47 percent of the advisories that had none.
- 70% of vulnerabilities reside deep within the network.
- 22% of advisories were network exploitable and perimeter facing in 2024.
- 39% of the advisories that Dragos analyzed could cause both a loss of view and loss of control, down from 53 percent in the previous year.
- Dragos tracks 23 THREAT GROUPS, 9 of which were active in 2024.
  - KAMACITE
  - PARISITE
  - GRAPHITE
  - BAUXITE
  - ELECTRUM
  - VOLTZITE
  - MAGNALLIUM
  - CHERNOVITE
  - WASSONITE
  - New in 2024
- ICS Cyber Kill Chain Stage 2 Capability

Key Ransomware Findings
- Ransomware attacks against industrial organizations increased 87 percent over the previous year.
- Dragos tracked 60 percent more ransomware groups impacting OT/ICS in 2024.
- 69% of all ransomware attacks targeted 1,171 manufacturing entities in 26 unique manufacturing subsectors.

![OT Protocols Used, Industries Targeted, Ransomware Groups, IT Protocols Used]

- OT Protocols Used
  - Modbus
  - SSH
  - FINS
  - RDP
  - Meter-bus
  - VNC
  - CIP
  - HTTP
  - OPC/UA
  - HTTPS
  - S7comm
  - PPTP
  - IMAP
  - CODESYS
  - WebDAV (over HTTPS)
- Industries Targeted
  - Electric
  - Water & Wastewater
  - Manufacturing
  - Maritime
  - Telecommunications
  - Defense Industrial Base
  - Oil & Gas
  - Food & Beverage
  - Mining
  - Transportation & Logistics
  - Chemical Manufacturing
- Ransomware Groups
  - Ransomware Groups in 2023
  - Ransomware Groups in 2024
- 50% target Manufacturing

# Defender’s Guide to the Current Threat Landscape
The cybersecurity threat landscape in 2024 was shaped by escalating geopolitical tensions and their intersection with industrial operations globally. From persistent campaigns by mature threat groups to opportunistic attacks by hacktivists or ransomware operators, adversaries demonstrated a growing awareness of OT/ICS environments as potential attack vectors to achieve their goals. This year highlighted the increasingly complex threat landscape and the corresponding escalating pressure on defenders to enhance visibility into and resilience of OT/ICS networks.

## Adversaries Targeting OT: Awareness Over Sophistication
A striking trend in 2024 was the continued lowering of the barrier to entry for adversaries targeting OT/ICS. Adversaries that would have once been unaware of or ignored OT/ICS entirely now view it as an effective attack vector to achieve disruption and attention. For example, Blackjack’s Fuxnet malware, revealed in April 2024, though rudimentary compared to more sophisticated ICS-capable malware like PIPEDREAM, signaled a growing awareness of the impact that disruptive attacks on OT networks can have. Similarly, the hacktivist persona CyberArmyofRussia_Reborn’s (CARR) campaigns targeting internet-exposed OT devices through much of 2024 demonstrated that even basic techniques, such as manipulating internet-exposed human-machine interface (HMI) settings remotely, could result in tangible disruptions.[^1]

This shift is not indicative of a deeper technical understanding of OT but reflects a more widespread recognition of its utility in achieving adversary goals. For ransomware operators, this has meant targeting manufacturing environments where downtime directly pressures victims to pay ransom. For hacktivists, targeting OT offers a fast and disruptive way to amplify their messages. These attacks reinforce a crucial reality: sophistication is not always necessary to achieve impactful outcomes, and the proliferation of adversaries amplifies the overall risk.

This focus on simplicity highlights a critical point for defenders: effective implementation of the SANS ICS 5 Critical Controls[^2] remains the best defense against OT-targeting adversaries. Organizations with strong incident response capabilities, defensible architectures, secure remote access protocols, and robust network monitoring are far better positioned to reduce the risk of a successful attack on the enterprise OT even in this increasingly complex environment.

## Defender Progress: Incremental But Uneven
Defenders have made progress in understanding the importance of securing OT environments, but this progress remains uneven across sectors and regions. Regulated industries, such as electric power in North America, demonstrate higher maturity levels than less regulated sectors, such as water utilities or manufacturing. Initiatives like the Dragos Community Defense Program (CDP)[^3] contribute to increased awareness, but visibility into OT environments lags behind adversary tactics in many cases. 

Highlighting uneven progress, many organizations implement secure remote access but lack the internal network monitoring and visibility to find third-party and legacy connections that leave their networks open to compromise. In one case, the Dragos team identified a legacy vendor connection inside an organization’s OT network weeks before a ransomware group compromised the vendor. Removing the legacy connection prevented the organization from harmful exposure to the vendor’s compromised network. Whether it is OT virtual private networks (VPN) with direct access to the internet or demilitarized zones (DMZs) with insecure configurations, Dragos Services engagements routinely observe organizations that lack visibility and monitoring to identify ad hoc additions to their environment.

While a lack of visibility prevents organizations from understanding attack vectors inside their network, it is the root of why organizations fail to understand their external attack surface, leaving them vulnerable to opportunistic adversaries relying on tools like Shodan and Censys to discover exposed devices. Internet-exposed ICS devices were among the most exploited vectors for OT-targeting attacks in 2024. The harmful assumption that “we won’t be targeted” remains a significant hurdle for defenders, particularly in organizations with limited resources or competing priorities.

2024 demonstrated that OT is no longer a niche target. The proliferation of adversaries—enabled by greater awareness and understanding of OT and the effectiveness of basic attack techniques — has made defending critical infrastructure more challenging than ever. Skilled adversaries remain hidden within critical infrastructure while hacktivists exploit exposed weak infrastructure. Both are enabled by an environment where a majority of the community is not yet aware of the specific threat to OT differentiated from IT, or worse, is informed but knowingly chooses to ignore or downplay its veracity. Doing the basics continues to be the prime directive for most of the community. Now more than ever, defenders who can uncover and illuminate hidden threats are stepping up to hunt.

![SERVICES DATA ANALYSIS]
Dragos conducts on-site visits at various industrial sites to assess security gaps and provide actionable recommendations through architecture reviews, penetration tests, tabletop exercises, and more. In 2022, Dragos revamped the collection and analysis of data from these on-site engagements to better present the state of industrial cybersecurity with more accurate MITRE ATT&CK for ICS tagging, industry delineation, and deeper analysis of security findings. These firsthand field observations are used to communicate trends in industrial cybersecurity, provide industry specific insights, and share key issues to address in efforts to enhance security.

## OT-Centric Cyber Operations Increase as Geopolitical Tension and Conflicts Continue
A cyber attack on a municipal energy company disrupted heat to hundreds of apartment buildings in Ukraine.[^4] A purported attack by Ukraine-aligned Blackjack group damaged critical infrastructure monitoring devices in Russia.[^5] The pro-Iranian CyberAv3ngers attacked fuel management systems in Israel.[^6] In 2024, Dragos witnessed continued offensive cyber activities linked to ongoing geopolitical conflicts. Threat groups, including hacktivists, shifted to more overt cyber operations aligned to the goals of their respective side, and the more mature groups sought to cause disruptive effects. 

## The Ukraine-Russian Conflict Fuels Activity for Established Dragos Threat Groups
KAMACITE and ELECTRUM continue to collaborate in support of Russian military objectives by targeting critical infrastructure in Ukraine. KAMACITE establishes a foothold into victim IT networks and hands control to ELECTRUM for OT operations, such as the 2016 CRASHOVERRIDE attack, which temporarily cut power to part of Kyiv.[^7] 

In 2024, KAMACITE used the Kapeka backdoor targeting Ukrainian critical infrastructure entities supplying heat, water, and electricity. Meanwhile, ELECTRUM collaborated with hacktivist groups to obscure its cyber attack against Kyivstar, a Ukrainian telecommunications company. 

This new KAMACITE and ELECTRUM activity illustrates the accelerating effects of the Ukraine-Russia conflict on the development of OT-related cyber attack techniques.

## KAMACITE Technical Update
Tracking KAMACITE is important because they hand off their access to OT disruption teams, like ELECTRUM, which has technical overlaps with Sandworm, tracked by other organizations.[^8]

Since 2015, KAMACITE conducted at least three disruptive campaigns targeting electric infrastructure in Ukraine, deploying GreyEnergy and BlackEnergy, as well as developing and using VPNFilter and CyclopsBlink botnets. In 2024, KAMACITE introduced new, custom Windows-based malware strains and expanded its focus to European oil and natural gas (ONG) entities.

KAMACITE targets organizations in Ukraine, Eastern and Central Europe in the following verticals:
- Oil & Natural Gas
- Electric
- Manufacturing
- Defense Industrial Base

Given KAMACITE’s role as an initial access provider and their consistent use of phishing, Dragos urges organizations to conduct regular user education to identify phishing attempts. Additionally, proper segmentation between enterprise IT and OT/ICS is critical in preventing a KAMACITE compromise from escalating to a disruptive event. Finally, visibility into north-south traffic in ICS environments is important. Defenders should monitor for suspicious activity, such as terminated connections between control centers or abnormal polling of substations to toggle breaker statuses.

## KAMACITE Campaigns
### Kapeka Campaign (2022-2023) 
Discovered in 2024, KAMACITE used Kapeka in a campaign targeting multiple Ukrainian critical infrastructure operators beginning in March 2023.[^9],[^10] Kapeka has technical overlaps with GreyEnergy, and analysis reflects ongoing development efforts within KAMACITE’s toolset. The number of discovered Kapeka samples is low, suggesting this malware has been used in low-volume, likely targeted attacks since at least mid-2022.

![Kapeka Campaign (2022-2023)]

### DarkCrystal RAT (2022-2024)
KAMACITE continues to use criminally sourced, commodity malware in spear-phishing campaigns targeting Ukrainian entities. DarkCrystal RAT (DCRat) was used for surveillance and information theft.

### LummaStealer and GIE Conference Campaign (2024)
KAMACITE used LummaStealer and employed a commodity loader service, now tracked by Dragos as TAT24-97.[^11],[^12] These capabilities are primarily delivered via spear phishing, using domains that resemble prominent technology provider names. 

KAMACITE targeted European ONG organizations, using the 2024 Gas Infrastructure Europe (GIE) conference hosted in Germany as a spear-phishing theme. The campaign relied on a relatively complex infection chain, leading to the deployment of another custom-developed Windows backdoor named “Edam.” This was a notable shift from an exclusive focus on Ukraine to broader European targets. This coincided with the expiration of an agreement allowing Russian state-owned company Gazprom to supply gas to Eastern and Central Europe. 

![LummaStealer and GIE Conference Campaign (2024)]

Hunt for WebDAV Communication to the Internet
WebDAV is a protocol that runs on top of HTTP and may be observed for syncing files across a network; if you see this communication between unexpected assets, such as to the internet, dig in.

![Reports per Year (Percent)]
Percent of service engagements, by vertical, that had insecure PowerShell configurations similar to ones exploited in KAMACITE’s Edam attack.

As more PowerShell related tactics, techniques, and procedures (TTPs) are attributed to tracked threat groups like KAMACITE, Dragos is increasingly critical of related security configurations. Enabling PowerShell logging to support incident response, and enabling AMSI to block malicious scripts are the most common PowerShell related recommendations from Dragos security assessments.

## ELECTRUM Technical Update
One of Dragos’s oldest threat groups, ELECTRUM is responsible for multiple ICS attacks, including the CRASHOVERRIDE event in 2016, which blacked out a portion of Kyiv for about an hour, and the failed Industroyer2 attempt in 2022. ELECTRUM has technical overlaps with the Sandworm APT.[^13] While they were not as active as KAMACITE in 2024, ELECTRUM used hacktivist personas to conceal their other operations and developed a new wiper capability, AcidPour.

ELECTRUM demonstrated their ability to reach Stage 2 - Execute ICS Attack of the ICS Cyber Kill Chain. 

ELECTRUM targets Ukraine, though Dragos also observed the targeting of energy companies in Germany.

Electric

Given ELECTRUM’s history of wiper malware usage, asset owners should implement basic security measures to prevent or at least monitor binary execution within control system environments or monitor when such files transfer into the ICS network. End users should disallow new service installs, disable service changes, and implement application whitelisting so only authorized applications can execute on devices if possible. Asset owners and operators must be prepared to not merely prevent such actions but also ensure quick recovery in these circumstances. Robust backups of engineering files such as project logic, IED configuration files, and ICS application installers should be offline and tested.

![Timeline of ELECTRUM Wiper Capabilities]

## ELECTRUM Campaigns
### KyivStar Attack and Hacktivists Cover (December 2023)
Ukraine’s primary telecommunications provider, Kyivstar, experienced a cyber attack, resulting in significant service disruptions nationwide. Following the incident, two pro-Russian hacktivist online personas, KillNet and Solnetspek, claimed responsibility through nearly identical messages posted on their Telegram channels. In early 2024, Dragos analyzed the Kyivstar incident and determined that ELECTRUM used the resources and reputation of the hacktivist persona Solnetspek to obfuscate its operational activities.

### AcidPour Wiper (March 2024)
Dragos analyzed ELECTRUM’s new capability, AcidPour. AcidPour is a binary compiled for Linux operating systems that can search and wipe Unsorted Block Images (UBI) directories in embedded devices, including devices in OT environments.

![AcidPour Wiper Capabilities]
AcidPour extended the functionality of AcidRain, a previously used wiper, in February 2022. AcidRain impacted ViaSat modems and caused a partial interruption of KA-SAT’s consumer-oriented satellite broadband service. The attack also impacted wind turbines in Germany.[^14]

The discovery and implications of AcidPour underscore the persistent threat posed by ELECTRUM’s arsenal of wiper malware, particularly considering their potential to inflict substantial operational disruptions and damage in OT environments. 

## Geopolitical Tensions in Asia Facilitate Further VOLTZITE Activity
Throughout the year, the threat group VOLTZITE continued its activities, compromising small office and home office (SOHO) routers and interacting with geographic information systems (GIS). Analysis reveals that VOLTZITE and its affiliates are using infrastructure from compromised organizations as relay points for use in a botnet. These actions facilitate adversary-controlled peer-to-peer (P2P) relay networks that enumerate internet-exposed critical infrastructure, impacting sectors such as electric, oil and gas, water and wastewater, and government entities. 

## VOLTZITE Technical Update
VOLTZITE is arguably the most crucial threat group to track in critical infrastructure. Due to their dedicated focus on OT data, they are a capable threat to ICS asset owners and operators. This group shares extensive technical overlaps with the Volt Typhoon threat group tracked by other organizations.[^15] VOLTZITE has a history of OT network intrusions, and like in previous years, Dragos observed VOLTZITE continuing to use different proxy networks and steal GIS data, OT network diagrams, and OT operating instructions from their victims. Aided by this ICS-focused data, VOLTZITE could craft a malicious OT-specific tool capable of operational disruption. Instead, this threat group uses tools already available on the systems known as living-off-the-land (LOTL) techniques. With careful monitoring and investigation of “odd” network communication, defenders can identify and defend against VOLTZITE.

VOLTZITE disguises its operations by setting up complex chains of network infrastructure. Dragos tracked their continuing provision of operational relay box (ORB) networks and compromised SOHO routers operated by electric utilities that provide telecommunications infrastructure and energy services to a specific region. Since these routers’ IP addresses would look neutral to network defenders, VOLTZITE likely intended to use these compromised routers to exploit other critical infrastructure targets.

![Historical VOLTZITE Infrastructure Usage]

VOLTZITE conducts slow and steady reconnaissance efforts from multi-layered network infrastructure and shares infrastructure with other groups attributed to the Chinese state by others. Dragos observed this network reconnaissance against critical infrastructure network edge devices, such as VPN gateways and firewalls from known VOLTZITE co-opted botnets, such as the JDY botnet. 

VOLTZITE continues to focus on exfiltrating OT-related data from its victims’ networks. In many cases, Dragos observed VOLTZITE exfiltrating GIS data containing critical information about the spatial layout of energy systems. 

VOLTZITE usually exploits vulnerabilities in internet-facing VPN appliances or firewalls for initial access. Dragos encourages asset owners and operators to implement adequate patch management and system integrity plans on those types of assets in their network. Dragos expects VOLTZITE operations against critical infrastructure of the United States and Western-aligned nations to continue into 2025. Defenders must monitor activity at every level of the Purdue model, from internet-facing VPN appliances to the business network through DMZs and within OT networks to identify VOLTZITE. The best way to identify VOLTZITE is by monitoring its behaviors; it purposely blends in with trusted networks and uses tools already available. Compare any unusual lateral movement with expected traffic within your network and validate suspicious user activity that originates from regular employee accounts. 

Confirmed victims of VOLTZITE were found in North America, Guam, Europe, Asia, New Zealand, and Africa. Its campaigns have affected industrial sectors, including:
- Electric Power Generation, Transmission, and Distribution
- Emergency Management
- Telecommunication
- Defense Industrial Base
- Satellite Services

65% of sites Dragos assessed had insecure remote conditions. This includes insecure configurations, unpatched systems, and poor network architecture related to remote access appliances and applications. 

## VOLTZITE Campaigns
### Ivanti VPN Zero-Day Campaign (December 2023)
By combining the exploits, VOLTZITE can execute remote code, enabling theft of configuration data, reverse tunneling from the ICS VPN appliance, and other malicious behaviors.[^16]

Monitor SYS32039 and SYS32040 for new files being created.

![Ivanti VPN Zero-Day Campaign (December 2023)]

### Telecom and EMS Campaign (January 2024)
VOLTZITE conducted reconnaissance of U.S. telecommunications and command-and-control (C2) activity with U.S. Emergency Services GIS endpoints.[^17]

![Telecom and EMS Campaign (January 2024)]

### ISP and Telecommunications Campaign (August 2024)
VOLTZITE compromised SOHO devices in electric, utility, and telecommunications cooperative infrastructure for use in operational relay networks to support future operations.

![ISP and Telecommunications Campaign (August 2024)]

### JDY Botnet (Late 2024)
VOLTZITE scanned targets with JDY botnet certificates. Target organizations were in the electric, oil and natural gas, manufacturing, and defense industrial base sectors.

![JDY Botnet (Late 2024)]

Tips for Hunting
Do I have an adversary in my network collecting and exfiltrating GIS data? 
To help answer this question, you may need to evaluate your visibility, please refer to the Collection Management Framework.

![Remote Access Gateway]

## Dragos Identifies Two New Threat Groups in 2024
Shifting away from the existing Dragos-designated groups, two newly coined Dragos threat groups were also very active during this period, conducting a series of conflict-adjacent campaigns. 

GRAPHITE targets entities in the energy, oil and gas, logistics, and government sectors associated with the conflict in Ukraine, spanning across Eastern Europe and the Middle East.

Moving to the conflict in the Middle East, BAUXITE targets entities in oil and gas, electric, water and wastewater, and chemical manufacturing in the United States, Europe, Australia, and the Middle East. BAUXITE demonstrates technical alignment with the pro-Iranian group CyberAv3ngers. BAUXITE is likely to enhance its capabilities and continue disruptive activities against OT/ICS entities globally, especially those party to the Israel-Hamas conflict.

## Introducing GRAPHITE
Dragos designated GRAPHITE as a new threat group after discovering a campaign targeting hydroelectric generation facilities to steal credentials. Since then, Dragos observed GRAPHITE targeting industrial and energy organizations in Eastern Europe and Asia. The group has strong technical overlaps with the cluster identified as APT28 and other names.[^18] GRAPHITE focuses on organizations with relevance to the military situation in Ukraine, observable since Russia’s invasion of Ukraine in February 2022. 

In early 2023, Dragos identified GRAPHITE conducting a spear-phishing campaign targeting hydroelectric generation facilities, and other ICS organizations throughout Eastern Europe and the Middle East. The campaign exploited a no-click flaw in Microsoft Outlook allowing GRAPHITE to steal Windows authentication data.[^19] 

Concurrently, GRAPHITE conducted near-constant phishing operations using custom script-based malware. While these two campaigns used different tools and techniques, they targeted organizations in critical industries across a similar geography.

GRAPHITE used a network of compromised Ubiquiti Edge Routers to distribute malware and maintain C2 channels. GRAPHITE used this network as early as 2022 and their network remained active until February 2024, when the U.S. Justice Department announced a court-approved disruption of the botnet.[^20] Since 2024, Dragos observed GRAPHITE relying more on legitimate internet services (LIS), such as API endpoint testing services or GitHub, for staging payloads and C2 activities. 

GRAPHITE is a relevant threat for OT/ICS organizations as its targeting profile may shift in response to geopolitical developments in Eastern Europe but has not yet demonstrated Stage 2 capabilities. Dragos encourages defenders of industrial organizations, especially those involved in any way with Ukraine, to familiarize themselves with this adversary. 

Since at least March 2022, GRAPHITE conducted numerous campaigns achieving Stage 1 ICS Cyber Kill Chain impacts. Confirmed victims of GRAPHITE were found throughout Eastern Europe and the Middle East. Its campaigns have affected multiple critical infrastructure sectors, including:
- Electric
- Oil & Natural Gas
- Rail/Freight Logistics
- Aviation Logistics
- Defense Industrial Base

Dragos penetration testers also use internet infrastructure to test for C2 channels. 17 percent of penetration tests in 2024 resulted in findings related to C2 communication, with DNS channels being the primary contributor. If you can resolve internet addresses (e.g., www.dragos.com), adversaries can use this to remotely access those networks.

Tips for Hunting
Would we see an adversary spearphishing through legitimate internet services? Note: focus on spearphishing hooks and behaviors instead of their hosting source. 

## GRAPHITE Campaigns
From March 2022 to October 2023, a spear-phishing campaign targeted natural gas pipeline operators and hydroelectric generation facilities in Eastern Europe and West Asia. A vulnerability in Microsoft Outlook allowed for malicious attachments to capture credentials.[^21],[^22]

![GRAPHITE Campaigns - March 2022 to October 2023]

From 2023 to February 2024, a spear-phishing campaign targeted government entities in Poland and Ukraine. Compromised Ubiquiti Edge Routers were used to deliver MASEPIE malware. This Python backdoor allowed for encrypted reverse proxy connections to C2 infrastructure.[^23],[^24]

![GRAPHITE Campaigns - 2023 to February 2024]

Throughout 2023, spear-phishing campaigns targeted energy and government entities in Poland and the Middle East. Malicious websites delivered a Windows batch script backdoor dubbed HEADLACE, which allowed remote command execution.[^25]

![GRAPHITE Campaigns - Throughout 2023]

From 2023 to present, a spear-phishing campaign targeted government entities in Ukraine and Poland. Malicious websites are used to deliver OCEANMAP malware. This C# backdoor allowed remote commands on victim devices over IMAP.

![GRAPHITE Campaigns - 2023 to present]

In early 2024, a spear-phishing campaign targeted Ukrainian entities. A vulnerability in the WinRAR archiver tool infects emails and sends malicious attachments that deploy a PowerShell stealer dubbed STEELHOOK. This malware allows the adversary to extract login data from Google Chrome and Microsoft Edge browsers.[^26],[^27]

![GRAPHITE Campaigns - early 2024 - STEELHOOK]

Simultaneous campaigns in 2024 saw GRAPHITE maintaining malicious websites designed to appear as legitimate web login portals of popular service providers such as Outlook on the Web (OWA) and ukr.net (a popular Ukrainian online service). Using a credential-phishing toolkit, likely custom to GRAPHITE, adversaries could successfully bypass two-factor authentication and Captcha solving to profile a victim’s browser and location.[^28] 

![GRAPHITE Campaigns - 2024 - credential-phishing]

OT Watch Identified 14 percent of customers communicating to external addresses via IMAP protocol. 
*A minor portion of these environments are untuned.

Hunt for yourself in the Dragos Platform. 
To identify IMAP communicating to non RFC-1918 addresses:
type:Communications AND NOT ip_dst_network_id:* AND protocol:IMAP AND dst_port_o2r: *

## Introducing BAUXITE
Dragos-designated threat group BAUXITE was implicated in multiple global campaigns targeting OT/ICS entities and specific devices. This group shares substantial technical overlaps, based on capabilities and network infrastructure, with the pro-Iranian hacktivist persona CyberAv3ngers, which has explicit affiliations with the Iranian Revolutionary Guard Corps—Cyber and Electronic Command (IRGC-CEC), as reported by the U.S. Government.[^29] The U.S. Government sanctioned multiple members of the CyberAv3ngers, including their leader.[^30]

BAUXITE is on OT/ICS-focused forums, where they ask questions about OT/ICS original equipment manufacturer (OEM) hardware. They extensively monitor security advisories from OEMs and ICS protocols, likely documenting and cataloging known vulnerabilities to target in future campaigns. 

Given BAUXITE’s technical alignment with CyberAv3ngers and its reported ties to the IRGC-CEC, its targeting strategies and operational focus evolved under state-sponsored directives or geopolitical pressures. Throughout 2025, BAUXITE is expected to enhance its capabilities and attempt to conduct disruptive operations against OT/ICS entities globally. 

Since late 2023, Dragos observed four BAUXITE campaigns, including those with Stage 2 ICS Cyber Kill Chain impacts via trivial compromises of exposed devices. Confirmed victims of BAUXITE are in the United States, Europe, Australia, and West Asia. Its campaigns affected multiple critical infrastructure sectors, including: 
- Electric
- Oil