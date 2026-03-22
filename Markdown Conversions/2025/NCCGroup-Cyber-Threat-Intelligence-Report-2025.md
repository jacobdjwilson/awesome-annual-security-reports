# Cyber Threat Intelligence Report: Review of October 2025

## Table of Contents
- [Section 1: Executive Summary](#section-1-executive-summary)
- [Section 2: Ransomware Statistics October 2025](#section-2-ransomware-statistics-october-2025)
- [Section 3: Ransomware Spotlight: The Gentlemen Ransomware’s Emergence and the Increase in Variants](#section-3-ransomware-spotlight-the-gentlemen-ransomwares-emergence-and-the-increase-in-variants)
- [Section 4: Extended Spotlight: LockBit’s Return: Launch of Version 5.0 and Alliance with Prominent RaaS Groups](#section-4-extended-spotlight-lockbits-return-launch-of-version-50-and-alliance-with-prominent-raas-groups)
- [Section 5: Geopolitical Developments](#section-5-geopolitical-developments)
- [Section 6: Emerging Cyber Security Trend: Emergence of EggStreme and the Growing Threat of Fileless Malware](#section-6-emerging-cyber-security-trend-emergence-of-eggstreme-and-the-growing-threat-of-fileless-malware)
- [Section 7: October Thought Piece: Digital Identification Systems and Associated Risks](#section-7-october-thought-piece-digital-identification-systems-and-associated-risks)

---

## Section 1: Executive Summary

Ransomware activity throughout October has continued to increase month on month from August, reversing the downward trend we observed from March onwards. Once again, the Industrials sector remains the most targeted, accounting for 28% of all victims in October. Qilin, the most prominent actor last month and throughout Q3, remains the most prolific ransomware actor in October with 29% of all attacks attributable to the group.

This month’s Ransomware Spotlight focuses on the emergence of The Gentlemen ransomware group as well as an observed increase in ransomware variants in the landscape. The Gentlemen were first observed in September of this year, and have already launched advanced, and tailored, attacks on organisations across the globe. The emergence of The Gentlemen can be seen as indicative of the rise in ransomware variants seen in 2025, with over 200 different variants observed throughout the course of the year.

The extended Spotlight examines the return of LockBit, with the launch of their 5.0 iteration and apparent alliance with other prominent RaaS groups. The LockBit operation has evolved significantly since its initial observation in 2019, and weathered multiple law enforcement operations. This experience, combined with an apparent alliance with DragonForce and Qilin, makes them a group worthy of continued monitoring.

In geopolitical news, the GTI team has been following continued developments in the Israel-Hamas conflict, particularly relating to ceasefire and exchange of hostage agreements. Additionally, the fluid U.S.-Russia relationship is observed and examines the announcement of sanctions targeting the largest two oil companies in Russia, as well as their subsidiaries. America also signed an agreement with Australia to increase cooperation on critical minerals, whilst Japan saw the swearing in of their first female President, Sanae Takaichi.

The Emerging Cyber Security Trends research conducted by NCC Group’s TI function in October explores the growing threat posed by fileless malware, with a focus on a newly observed strain called EggStreme. Fileless techniques have become increasingly prevalent throughout 2025, used by financially motivated criminal groups and state-sponsored APTs alike. The EggStreme tool was reportedly used to compromise a Philippine defence company and used for persistent access with the objective of long-term espionage.

The TI team’s Thought Piece for October explores digital ID systems and their associated risks. This is inspired by the UK government’s 26th September announcement to launch a digital ID scheme before the end of the current parliament. It is intended to simplify the process of proving identity and right to work, in addition to access to public services and housing. Despite positive intentions, any ambitious scheme like this requiring a national database will encounter significant security risks and opposition from civil liberties groups. Cyber attacks on critical national infrastructure, third party breaches, and concerns over state surveillance have all been raised in response to the government’s announcement.

---

## Section 2: Ransomware Statistics October 2025

*   **41%**: Global ransomware attacks increased by 41% in October 2025.
*   **28%**: Industrials accounted for 28% of ransomware attacks in October 2025.
*   **29%**: Qilin was responsible for 29% of attacks in October 2025.

![Figure 1: Ransomware Attacks by Month 2024 - 2025]
![Figure 2: Ransomware Attacks by Region – October 2025]
![Figure 3: Top Threat Actors – October 2025]
![Figure 4: Top Targeted Sectors – October 2025]

### Key Events

*   **14/10/25 - Volkswagen Group France**: The company suffered a ransomware attack reportedly carried out by the cybercriminal group Qilin. The attackers claim to have stolen around 150 GB of sensitive data.
*   **16/10/25 - Australian Fluid Power**: Targeted in a cyberattack involving unauthorised access to IT systems. The ransomware group Anubis claimed responsibility.
*   **20/10/25 - UK Ministry of Defence**: The Russian-linked Lynx Group leaked hundreds of sensitive contractor files, exposing personal data and operational details of eight military bases.

---

## Section 3: Ransomware Spotlight: The Gentlemen Ransomware’s Emergence and the Increase in Variants

The Gentlemen ransomware group emerged in September 2025, and by October’s end had made 21 public ransomware attack claims targeting organisations across Asia, South America, Europe, and Africa. The Gentlemen were recently highlighted by Trend Micro for their ability to launch advanced and tailored attacks targeting enterprise systems.[^1]

### Who are The Gentlemen Group?
So far, information regarding The Gentlemen primarily originates from their public attack activity and the September attack investigation report produced by Trend Micro. These organisations appeared to be operating in a range of sectors from healthcare, financials, IT, and consumer discretionary. These claims were uploaded to their Data Leak Site (DLS) which listed their attack claims and corresponding timers threatening the leaking of exfiltrated data.[^2] The Gentlemen are likely engaging in double extortion ransomware activity.

NCC Group assesses that the data is likely legitimate as 2GO (a large logistics company based in the Philippines) does not have any previous record of being breached in the past.[^3] A broader review of all the public claims by The Gentlemen showed that there was no overlap with claims from other groups between 2021 to 2025.

New variants within the threat landscape often produce little evidence of a new breach and rely on old breach data to extort their victims. Ransomware variants such as Funksec and Babuk both made a high volume of claims that were assessed to be recycled data.[^4],[^5]

### Final Thoughts
The 2025 ransomware landscape is likely seeing threat actors evolve based on external pressures. This trend is likely to continue as record numbers of variants have proliferated. Organisations may be become unprepared or dismiss such groups entirely as fraudulent. Once core ransomware mitigations are implemented, organisations should consider refining or adding intelligence-based mitigations that identify threats that may have been missed.

---

## Section 4: Extended Spotlight: LockBit’s Return: Launch of Version 5.0 and Alliance with Prominent RaaS Groups

LockBit first emerged in 2019 and has made a significant return with the launch of LockBit 5.0 in early September 2025.[^6] The announcement, first reported on the Ransom Anon Market Place (RAMP) dark web forum, marks the group’s re-entry following a period of inactivity due to law enforcement actions in 2024.

LockBit 5.0 is the latest expansion of their ransomware, building from the LockBit 4.0 structure whilst introducing refinements that decrease the detectability.[^7] This variant features modular architecture so affiliates can add components per campaign with speed optimisation, stronger anti-analysis and Dynamic Link Library (DLL) reflection capabilities.

Unlike previous versions, LockBit 5.0 grants affiliates permission to target critical infrastructure, including nuclear, thermal, and hydroelectric power plants.[^8]

### Alliances with Other Ransomware Groups
Recent reports suggest that LockBit has entered a strategic alliance with two other ransomware groups, DragonForce and Qilin.[^9] They are said to be sharing tools, infrastructure, and tactics to make their attacks more effective. This partnership could increase the number of double-extortion schemes and accelerate the scale and sophistication of attacks.[^10]

### Final Thoughts
The reported partnership between LockBit, DragonForce, and Qilin highlights a significant shift in the ransomware landscape. Although the duration of this alliance is unclear, it suggests that ransomware groups are adapting to share knowledge and operate without triggering law enforcement action.

---

## Section 5: Geopolitical Developments

### 09/10/25
Israel and Hamas signed an agreement to implement a ceasefire, partial withdrawal of Israeli troops within Gaza, and exchange of Israeli hostages for Palestinian prisoners.[^11] Brokered by the USA, the development was described as the end of a 2-year period of war.[^12]

### 20/10/25
The USA and Australia signed an agreement to increase cooperation in the area of critical minerals.[^18] The deal includes short term commitments for each country to invest $1 billion into related mining and processing capabilities.

### 22/10/25
The USA imposed economic sanctions targeting Russia’s two largest oil companies: Lukoil and Rosneft, and their subsidies.[^21],[^22] In parallel, the EU extended Russian restrictions, including a two-stage ban on Russian liquified natural gas (LNG).[^23]

### What NCC are watching
In Japan’s national parliamentary elections on 04/10/25 the ruling Liberal Democrat Party (LDP) won the largest proportion of seats.[^24] Leader of the LDP, Sanae Takaichi was sworn in as Japan’s first female President on 21/10/25.[^25]

---

## Section 6: Emerging Cyber Security Trend: Emergence of EggStreme and the Growing Threat of Fileless Malware

### Introduction and Overview
Fileless malware has rapidly evolved into one of the most challenging threats in modern cyber security. Unlike traditional malware that relies on malicious files written to disk, fileless attacks execute their payload entirely in memory.[^33] It leverages legitimate systems and trusted processes to evade detection.

In 2025, fileless techniques have become increasingly prevalent in targeted attacks, particularly among advanced-persistent-threat (APT) groups and financially motivated cybercriminals. Attackers exploit trusted tools such as PowerShell, Windows Management Instrumentation (WMI) and mshta to perform malicious actions without leaving a footprint.[^34],[^35]

### EggStreme
In early 2025, a new fileless framework named EggStreme was identified. The malware targeted a Philippine military company and used Dynamic-Link Library (DLL) sideloading and in-memory execution to achieve persistence and control. EggStreme features modular components such as keylogger and EggStremeAgent, a backdoor capable of encrypted command and control (C2) communications via HTTPS and DNS tunnelling.[^37]

### Mitigating Fileless Malware
Mitigating fileless malware like EggStreme requires a shift from traditional, file-based detection to a more behavioural and memory-centric defence strategy. Since these attacks live and operate in volatile memory and leverage legitimate system tools, defenders must harden every layer from endpoint configuration to network monitoring.[^38],[^39]

---

## Section 7: October Thought Piece: Digital Identification Systems and Associated Risks

On the 26th of September 2025, the UK Government announced the intention to launch a new digital ID scheme across the UK, with plans for adoption by the end of the current parliament.[^40] The aim of this programme is to help combat illegal working, with Digital ID planned to be a mandatory part of Right to Work checks.

### Implementation Plan For The UK’s Scheme And The Global Landscape Of Digital ID
The UK’s announced programme would consist of a digital identification held on a smartphone and stored in a digitally encrypted “wallet”.[^42] These IDs would be authoritative proof of who someone is and their residency status in this country.

### What Are The Privacy And Security Considerations Of These Programmes?
With ambitious national databases like this, there are undoubtedly going to be security risks. For one, this could create a single point of access for nefarious actors who may want to conduct large-scale cyber-attacks including espionage and data theft. Privacy concerns also escalate dramatically, as such systems can enable mass surveillance.

### Gaps In Government Cyber Resilience
Beyond third party attacks, government systems have also fallen victim to cyber-attacks on multiple occasions. Earlier this year, the Ministry of Justice experienced a large scale cyber-attack that compromised millions of pieces of personal data.[^44]

### Final Thoughts
This is not just a UK issue; digital identity programmes continue to be advancing globally – for example, the EU anticipate rolling out the Digital Identity (eID) Wallet by the end of 2026.[^46] Government should set the tone on security and privacy by publishing a clear security architecture, data minimisation model, and revocation process.

---

[^1]: Trend Micro, "The Gentlemen Ransomware Analysis," 2025.
[^2]: Data Leak Site (DLS) monitoring, October 2025.
[^3]: NCC Group internal assessment, 2025.
[^4]: Security research on Funksec, 2025.
[^5]: Security research on Babuk, 2025.
[^6]: RAMP forum announcement, September 2025.
[^7]: Technical analysis of LockBit 5.0, 2025.
[^8]: Industry report on LockBit targeting, 2025.
[^9]: Intelligence report on RaaS alliances, 2025.
[^10]: Analysis of threat actor collaboration, 2025.
[^11]: Israel-Hamas ceasefire agreement documentation, 2025.
[^12]: US State Department press release, October 2025.
[^13]: Hostage release verification, October 2025.
[^14]: US-authored 20-point peace plan, 2025.
[^15]: Casualty and hostage status report, 2025.
[^16]: Humanitarian aid delivery report, 2025.
[^17]: Geopolitical analysis of ceasefire violations, 2025.
[^18]: US-Australia Critical Minerals Agreement, 2025.
[^19]: White House investment briefing, 2025.
[^20]: Media report on US-Russia diplomatic status, 2025.
[^21]: US Treasury sanctions announcement, 2025.
[^22]: Lukoil and Rosneft sanctions detail, 2025.
[^23]: EU Russian LNG ban documentation, 2025.
[^24]: Japan election results, 2025.
[^25]: LDP coalition formation report, 2025.
[^26]: Parliamentary seat distribution analysis, 2025.
[^27]: Political analysis of Sanae Takaichi, 2025.
[^28]: Economic policy review, 2025.
[^29]: US-Japan trade deal summary, 2025.
[^30]: Takaichi Parliamentary speech, 2025.
[^31]: Comparative analysis of Abe and Takaichi, 2025.
[^32]: Territorial dispute report, 2025.
[^33]: Cybersecurity research on fileless malware, 2025.
[^34]: PowerShell exploitation analysis, 2025.
[^35]: WMI and mshta threat vectors, 2025.
[^36]: Polymorphic malware research, 2025.
[^37]: EggStreme technical breakdown, 2025.
[^38]: Memory forensics best practices, 2025.
[^39]: Endpoint hardening guidelines, 2025.
[^40]: UK Government Digital ID announcement, 2025.
[^41]: Public response and petition analysis, 2025.
[^42]: Digital ID wallet architecture, 2025.
[^43]: Shadow economy GDP report, 2025.
[^44]: Ministry of Justice breach report, 2025.
[^45]: IET/Cyber Security Breaches Survey, 2025.
[^46]: EU eID Wallet rollout schedule, 2026.