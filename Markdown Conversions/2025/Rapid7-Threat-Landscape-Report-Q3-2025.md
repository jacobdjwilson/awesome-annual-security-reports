# The Q3 2025 Threat Landscape

By Rapid7 Labs

## Table of Contents
- [Introduction](#introduction)
- [The ransomware landscape: Trends and key players](#the-ransomware-landscape-trends-and-key-players)
- [Nation-state activity: Espionage and exploitation](#nation-state-activity-espionage-and-exploitation)
- [Cybersecurity incidents: Impacts and key MITRE ATT&CK techniques](#cybersecurity-incidents-impacts-and-key-mitre-attck-techniques)
  - [Initial access](#initial-access)
  - [Top 10 MITRE ATT&CK techniques for Q3](#top-10-mitre-attck-techniques-for-q3)
- [Vulnerability intelligence: Emergent threats and exploitation trends](#vulnerability-intelligence-emergent-threats-and-exploitation-trends)
- [AI-supported threats: Social engineering and evasive malware](#ai-supported-threats-social-engineering-and-evasive-malware)
  - [AI-driven social engineering](#ai-driven-social-engineering)
  - [AI-generated and evasive malware](#ai-generated-and-evasive-malware)
- [Strengthening security: Key recommendations](#strengthening-security-key-recommendations)
- [About Rapid7](#about-rapid7)

---

## Introduction

Welcome to the Q3 2025 Threat Landscape Report.

The past quarter saw relentless activity in the global cyber domain. From critical vulnerabilities exploited within days of disclosure, to the continued evolution of ransomware groups and nation-state actors, defenders faced a complex and shifting threat environment that demanded both speed and resilience.

Q3 was marked by a zero-day exploitation of Microsoft SharePoint servers and multiple critical vulnerabilities in Cisco products, both leveraged in rapid mass-exploitation campaigns. The race between disclosure and exploitation has never been tighter, with many organizations caught in the gap.

Beyond direct exploits, the Salesloft supply chain breach highlighted the growing fragility of trust in interconnected SaaS ecosystems. Attackers weaponized legitimate update and integration mechanisms, serving as a stark reminder that even trusted vendors can become an attack vector.

Ransomware groups like LockBit, Black Basta, and Qilin refined their extortion tactics, expanding their targeting toward critical services, manufacturing, and healthcare sectors. Notably, we observed an uptick in double- and triple-extortion methods, blending data theft, leaks, and sustained harassment of victims.

Geopolitically, nation-state activity such as APT29’s ongoing credential theft campaigns and China-linked espionage targeting telecom and defense supply chains reinforced that cyber remains a central theater of global competition. Emergent threats like the Brickstorm espionage campaign further blurred the line between traditional intelligence gathering and cyber-enabled disruption.

Our analysis also underscores a persistent trend: Attackers increasingly target core business systems including ERP platforms, virtualization layers, and managed file transfer technologies. These are not random, opportunistic hits; they are calculated moves designed for operational disruption and leverage.

In this report, you’ll find:
- Data-driven insights into top exploited vulnerabilities and their attacker ecosystems
- Trends in ransomware operations and victimology from our ransomware and dark web tracking
- Deep dives into notable APT campaigns and malware evolutions
- Guidance on defensive priorities drawn from our AttackerKB and Intelligence Hub correlations

As always, our mission remains to make the complex simple: Turn raw threat data into curated, actionable intelligence that empowers defenders to act decisively. Cyber threats continue to evolve, but so does our ability to anticipate, detect, and respond with precision. Thank you for joining us as we map the adversary’s next move.

— Raj Samani, Chief Scientist, Rapid7

---

## The ransomware landscape: Trends and key players

As we looked back on the first half of 2025 and ahead to Q3, we expected a prolonged powerscale rebalancing among threat actors, and this has largely come to pass. Many of the groups that at one time dominated suddenly went silent, while others announced various forms of retirement or similar pauses in activity. Other well-known groups such as Qilin and Akira have swooped in to fill the void; however, we’ve also seen the rise of “collectives” in which a few hardliners take the lead and many join in to participate in the action.

Our analysis of ransomware activity for Q3 2025 highlights the established dominance of threat actors, major groups forming alliances to further their goals of data exfiltration and extortion, and what may be a final farewell for long-absent ransomware groups. July through September was a time of power consolidation, and a broadening of scope for prolific threat actors such as Qilin, SafePay, and WorldLeaks.

While alliances can prove brittle and temporary, the previously mentioned team-up of Qilin and DragonForce with LockBit (sporting an all new version 5.0) should not be taken lightly. If the merging of tactics and infrastructure comes to fruition, it may well solidify Qilin and DragonForce’s places in the top 10 not just for Q4, but 2025 as a whole.

### At a glance

Looking at the top 10 ransomware groups in terms of number of leak site posts ![Figure 1: Top 10 ransomware groups by number of leak site posts, Q3 2025], we see that Qilin has retained the top position in Q3 2025, with Akira and INC Ransom quite a way behind in second and third place, respectively. Devman, WorldLeaks, and Everest are the only new additions to the top 10 this quarter.

In Q3, there were 88 groups actively posting to their leak sites, compared to 65 in Q2 and 76 in Q1. Of the 88 in Q3, 28 are new additions to the active group total. These new additions include (but are not limited to) Cephalus, Miga, Obscura, Radiant Group, and Yurei.

We also saw some ransomware groups go silent this past quarter. Of the 65 groups making leak posts in Q2, 19 are now inactive in terms of no visible leak posts for the months of July, August, and September.

**Popular targets in Q3:**
- Business services, manufacturing, healthcare, construction, and the financial sector were the most targeted industries in Q3 2025. The leader of the pack this quarter is business services, with 18% of posts containing these victims’ data. Second place goes to manufacturing with 15% of posts, and healthcare sits third, with a total of 13%.
- Top regional targets include the United States with 67%, Germany in distant second with 6%, and the UK and Canada in joint third place with 5%. Italy (4%) and France (3%) fill the other two top spots.

### Notable Trends

Rapid7 observed several notable trends at play in the ransomware landscape during Q3, including power consolidation among major players, evolving tactics in evading law enforcement, and innovations in operational models.

#### Hide and seek
The first half of 2025 saw new groups come and go, and many followed a trend of wanting to make a big, splashy announcement that they had arrived on the scene. Whether through slick branding or by making the most of a big compromise, being noticed by potential affiliates and other major players was the name of the game.

By contrast, Q3 brings a few tweaks to that approach. New groups aren’t necessarily charging into battle via the loudest means imaginable. In fact, they’re becoming more elusive where posting up their leaks are concerned. They’re stripping out URLs and other identifiers such as victim names, and reducing everything down to information-lite screenshots instead. This is likely designed to throw law enforcement and researchers off the scent.

#### Sliding down the ladder
The first half of the year saw a visible climb to power among a handful of groups, while former major players were shut down, disbanded, or disrupted by law enforcement. As a result, threat actors such as Akira and Qilin have solidified their position at the top in Q3. Seemingly immovable objects such as Cl0p (or at least, someone claiming to be Cl0p), FunkSec, Cactus, and BianLian have all fallen into the mist.

### Ones to watch

**Qilin**
As discussed above, the Qilin ransomware group has increased in both its visibility and impact as the year has progressed. The group has caused significant disruption in Q3, with attacks across multiple industries such as education, food/beverage, and healthcare. Qilin’s double-extortion tactics, combined with a successful RaaS business model, have contributed to its success. Add to this the recent revelation that Qilin is strengthening its infrastructure and techniques by joining forces with LockBit and DragonForce ![Figure 2: Screenshot of DragonForce admin post on the dark web site Ransombay], and we have the makings of a very strong close to the year if Qilin keeps up this kind of momentum.

**Crimson Collective**
Crimson Collective, with a fondness for operating in cloud environments, first rose to prominence after claiming responsibility for the compromise of 28,000 private Red Hat repositories. This group clearly has an eye for bigger things, and has also teamed up with the Scattered Lapsus$ Hunters collective. Most recently, Crimson Collective is claiming to have breached Nintendo’s internal systems.

**SafePay**
First observed toward the end of 2024, SafePay became increasingly active in terms of threat posts during the first half of this year. SafePay does not make use of the RaaS model at all, preferring to keep all of their activities in-house and very much hands on.

**WorldLeaks**
An interesting “new” group with quite a bit of backstory, WorldLeaks (first observed in January 2025) is an evolution of the threat actor Hunters International. Deciding that the world of ransomware, encryption, and double extortion was too risky, the group released free decryptors into the wild and focused on single extortion.

---

## Nation-state activity: Espionage and exploitation

From the vantage point of Rapid7 Labs telemetry, Intelligence Hub correlations, and AttackerKB vulnerability tracking, nation-state operations in Q3 2025 were defined by a combination of stealth, supply-chain exploitation, and the tactical use of zero-day and near-zero-day vulnerabilities.

### Russia
APT29 (Nobelium/Cozy Bear) remained one of the most active Russian-linked clusters, sustaining credential-theft campaigns that targeted Western diplomatic and defense organizations through OAuth token manipulation and misconfigured Azure app registrations.

In a continuation of its campaign against Ukrainian critical infrastructure, the Russian state-sponsored group Sandworm deployed a new, highly destructive wiper malware known as PathWiper. Russian threat actors also introduced a significant evolution in malware capabilities with the deployment of LAMEHUG, a tool used by a Pawn Storm-affiliated group that incorporates a large language model (LLM) to dynamically generate commands.

### China
China-nexus actors such as APT41 (Wicked Panda), and Volt Typhoon broadened their targeting scope beyond traditional espionage into strategic infrastructure domains. Volt Typhoon persisted in targeting maritime logistics and regional telecom operators, deploying custom router implants and SOHO exploitation chains.

One of the most notable developments this quarter was the emergence of Brickstorm, a newly detailed espionage campaign attributed to an Iranian nexus actor set. In the publicly disclosed F5 incident, reports link this breach to BRICKSTORM/UNC5221, stating that the attackers used custom malware and a long dwell time to harvest source code, internal vulnerability information, and configuration artifacts.

### DPRK
The Kimsuky and Lazarus groups maintained consistent financial and espionage campaigns. Throughout Q3 2025, the DPRK-affiliated group Void Dokkaebi (also tracked as Famous Chollima and CL-STA-0240) continued its financially motivated "Contagious Interview" campaign.

Rapid7 Labs conducted an in-depth investigation into the network of DPRK-affiliated IT workers active across freelance and outsourcing platforms. ![Figure 3: Each color cluster represents the Github account of a DPRK IT worker, where correlations denote shared projects, code, friends, etc.]

---

## Cybersecurity incidents: Impacts and key MITRE ATT&CK techniques

The third quarter of 2025 saw a diverse range of sophisticated cyber incidents, primarily characterized by compromised credentials, extensive lateral movement, and the pervasive use of ransomware.

### Initial access
Initial access vectors frequently observed by the Rapid7 Incident Response team in Q3 included:
- **Exploitation of remote access services**: This was a primary vector, particularly through vulnerable VPNs (SonicWall SSLVPN, Cisco ASA VPN, FortiGate firewall VPN) and remote desktop protocol (RDP).
- **Compromised credentials**: Threat actors gained initial access by using stolen or weak credentials.
- **Social engineering**: IT service desks were socially engineered to reset credentials or remove MFA.
- **Web shell deployment**: The deployment of web shells on compromised servers was also observed.

### Top 10 MITRE ATT&CK techniques for Q3
1. **T1078 - Valid accounts**: Widespread use of compromised credentials.
2. **T1133 - External remote services**: Exploitation of VPNs and RDP.
3. **T1059 - Command and scripting interpreter**: Use of tools like Impacket and web shells.
4. **T1003 - OS credential dumping**: Extracting MachineKey data and credential dumping.
5. **T1021 - Remote services**: Lateral movement through RDP.
6. **T1047 - Windows management instrumentation (WMI)**: Remote execution and system interaction.
7. **T1087 - Account discovery**: Active Directory enumeration tools (ADExplorer).
8. **T1018 - Remote system discovery**: Network discovery tools like Advanced IP Scanner.
9. **T1560 - Archive collected data**: Use of WinRAR and Rclone for data staging/exfiltration.
10. **T1566 - Phishing (and other forms of social engineering)**: Social engineering of IT service desks.

---

## Vulnerability intelligence: Emergent threats and exploitation trends

Rapid7 Labs tracked a total of 53 vulnerabilities, all of which were first reported as exploited in the wild in Q3. This represents a notable drop on previous quarters ![Figure 4: Number of vulnerabilities reported to be exploited in the wild for the first time, by quarter].

However, a significant number of outliers exist where the delta between disclosure and exploitation is measured in several thousand days ![Figure 5: Delta of the CVE disclosure date to the earliest exploited-in-the-wild date, Q3 2025].

The top 10 Common Weakness Enumerations (CWE) used to describe the root cause of these vulnerabilities show that CWE-502 (unsafe deserialization) has a notable lead ![Figure 6: Top 10 CWEs for reported exploited in-the-wild vulnerabilities, Q3 2025].

### Notable ETR Program Threats in Q3:
- **CVE-2025-54309**: CrushFTP zero-day exploited in the wild.
- **CVE-2025-53770**: Zero-day exploitation of Microsoft SharePoint servers (ToolPane exploit chain).
- **CVE-2025-7775**: Critical NetScaler vulnerability exploited in the wild.
- **CVE-2025-10035**: Critical unauthenticated RCE in GoAnywhere MFT.
- **CVE-2025-20333, CVE-2025-20362, CVE-2025-20363**: Multiple critical vulnerabilities affecting Cisco products.

---

## AI-supported threats: Social engineering and evasive malware

In Q3 we saw continued evidence of how AI is reshaping both the tempo and tactics of cyberattacks.

### AI-driven social engineering
Threat actors are leveraging generative AI to automate the creation of highly convincing phishing lures, deepfake audio and video for vishing campaigns, and tailored content for influence operations.

### AI-generated and evasive malware
The emergence of malware like Pawn Storm's LAMEHUG, which uses an LLM to dynamically generate its command and control logic, signals a new frontier in malware development.

---

## Strengthening security: Key recommendations

- **Develop comprehensive ransomware preparedness strategies**: Implement immutable backups, deploy EDR solutions, segment networks, and test incident response plans.
- **Prioritize MFA**: Enforce MFA across all critical systems, remote access points, and privileged accounts.
- **Maintain a mature VM program**: Continuous scanning and timely patching of all public-facing applications and network devices.
- **Harden against zero-day attacks**: Follow vendor guides, limit exposed services, and continuously monitor for anomalous activity.
- **Security awareness training**: Provide continuous training focusing on both traditional and AI-driven social engineering tactics.

---

## About Rapid7

Rapid7 is creating a more secure digital future for all by helping organizations strengthen their security programs in the face of accelerating digital transformation. Our portfolio of best-in-class solutions empowers security professionals to manage risk and eliminate threats across the entire threat landscape from apps to the cloud to traditional infrastructure to the dark web. Trusted by more than 11,000 customers worldwide, our industry-leading solutions and services help businesses stay ahead of attackers, ahead of the competition, and future-ready for what’s next.

**SECURE YOUR**
**ACCELERATE WITH**
Command Platform | Exposure Management | Cloud | Applications | Infrastructure | Network | Data
Attack Surface Management | Vulnerability Management | Cloud-Native Application Protection | Application Security | Next-Gen SIEM | Threat Intelligence | MDR Services | Incident Response Services | MVM Services

**TRY OUR SECURITY PLATFORM RISK-FREE**
Start your trial at rapid7.com