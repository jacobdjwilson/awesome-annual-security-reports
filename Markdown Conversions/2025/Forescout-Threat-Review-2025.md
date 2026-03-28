# 2025H1 Threat Review

## Table of Contents
- [1. Executive Summary](#1-executive-summary)
- [2. Key Trends in the First Half of 2025](#2-key-trends-in-the-first-half-of-2025)
  - [2.1. Cybercrime – Ransomware and Infostealers](#21-cybercrime--ransomware-and-infostealers)
  - [2.2. Healthcare – Malware and Data Breaches](#22-healthcare--malware-and-data-breaches)
  - [2.3. OT – The Growth of Opportunistic Attacks](#23-ot--the-growth-of-opportunistic-attacks)
- [3. Statistics](#3-statistics)
  - [3.1. Vulnerabilities](#31-vulnerabilities)
  - [3.2. Threat Actors](#32-threat-actors)
  - [3.3. Ransomware](#33-ransomware)
- [4. Deep Dive: APT IRAN and Shifting Identities – A Continuum of Iranian Hacktivist Threats to OT/ICS](#4-deep-dive-apt-iran-and-shifting-identities--a-continuum-of-iranian-hacktivist-threats-to-otics)
  - [4.1. A Tale of Three Identities](#41-a-tale-of-three-identities)
  - [4.2. Comparative Analysis](#42-comparative-analysis)
  - [4.3. What Does It All Mean?](#43-what-does-it-all-mean)
- [5. Mitigation Recommendations](#5-mitigation-recommendations)

---

## 1. Executive Summary
In the first half of 2025, Forescout Research – Vedere Labs published a broad range of blog posts and reports analyzing prominent vulnerabilities, threat actors, and ransomware operations. This mid-year review builds on our 2024 analysis, highlighting both persistent trends and emerging shifts in adversary behavior, attack surfaces, and defensive gaps.

Cybercriminals continue to rely on IT-centric techniques for malware delivery. ClickFix, in particular, has become a favored tool among infostealer and ransomware operators. Ransomware groups are expanding the types of assets leveraged in their attacks, frequently in attempts to bypass EDR solutions. Network infrastructure remains a major initial access vector, with over 20% of newly exploited vulnerabilities affecting such devices. Recent attacks highlight the growing role of IP cameras and BSD systems in lateral movement and impact – validating our 2022 R4IoT scenario that predicted this very convergence.

Beyond cybercrime, the line between hacktivist and state-sponsored activity is increasingly blurred, especially in attacks on critical infrastructure. Once the domain of shadowy state actor groups, these attacks are now frequently attributed to hacktivist front groups or hybrid personas. We analyzed this trend in detail in an April report, but since then, rising tensions in the Middle East have escalated the threat of Iranian-linked hacktivist attacks on Western targets. The tactics observed recall the lead-up to the late 2023 Unitronics campaign orchestrated by CyberAv3ngers.

This report reviews the threat landscape from January 1 to June 30, 2025 (2025H1) comparing it with the same period in 2024. It also includes a detailed case study on Iranian threat activity, showcasing how a continuum of personas, from ICTUS TEAM to APT IRAN, reflects a sophisticated OT/ICS targeting playbook that evolves in lockstep with regional conflicts and attribution pressures.

Crucially, many of the threats in 2025H1 exploited known vulnerabilities: 47% of newly exploited CVEs were published before 2025, and many targeted perimeter infrastructure. This underscores a core theme; proactive defense gaps remain the greatest liabilities.

## 2. Key Trends in the First Half of 2025
### 2.1. Cybercrime – Ransomware and Infostealers
Most cybercriminal activity we analyzed in 2025H1 relied on two dominant malware types: ransomware and infostealers. While the growth of ransomware is addressed in section 3, this section focuses on the evolving TTPs observed in campaigns delivering both malware types.

- **Initial Access**: Increased use of Initial Access Brokers (IABs) and exploitation of vulnerabilities in specific public-facing applications, including VPNs, remote access solutions, and file transfer applications.
- **Persistence, Execution, and C2**: Remote monitoring and management (RMM) tools become a preferred mechanism for persistence and execution. Attackers often abuse native functionality, such as remote shell access, to execute commands. Legacy techniques like user creation, scheduled tasks and web shells also remain prevalent.
- **Privilege Escalation**: Use of Cobalt Strike for post-exploitation has declined, though it remains in use for credential dumping and token manipulation.
- **Defense Evasion**: Obfuscation has taken a back seat to aggressive EDR bypass techniques. Tools such as KillAV, TrueSightKiller, and EDR Kill Shifter, and ‘bring your own vulnerable driver’ (BYOVD) methods are now standard. These tools are replacing traditional event-log purging and malware obfuscation.
- **Discovery**: To evade detection, threat actors increasingly use Active Directory Service Interfaces (ADSI) instead of prebuilt PowerShell tools for internal reconnaissance.
- **Exfiltration**: Data exfiltration is now routine across most groups. Many show preferences for specific tools, like Rclone or MEGA for this phase.

Two incidents in March 2025 illustrate how ransomware operators continue to expand the device types leveraged in their attacks, particularly to evade EDR:
- Akira ransomware was deployed to Windows endpoints via a compromised IP camera, echoing our 2022 R4IoT scenario.
- A new group dubbed VanHelsing introduced a multi-platform encryptor that includes support for BSD UNIX.

Infostealers continue to grow in both volume and sophistication. In 2025H1, ClickFix campaigns became the leading innovation in delivery tactics. ClickFix campaigns use social engineering to trick victims into copying and executing attacker-supplied malicious commands (usually PowerShell).

| Infrastructure Component | Details | Purpose |
| :--- | :--- | :--- |
| Command and control domains | TLDs like .shop, .top, .club, .run | C2 Communication |
| GitHub repositories | Used for distribution and updates | Initial payload delivery |
| Telegram | Channels with bots sharing stolen data | Distribution, command and control and exfiltration |
| SEO | Distribution of ClickFix campaign links | Initial infection vector |
| Bulletproof hosting | Hosting malicious payloads | Payload storage |
| Cracked software sites | Distribution of Trojanized applications | Initial infection vector |

### 2.2. Healthcare – Malware and Data Breaches
Healthcare continues to be among the most targeted industries. In February, we identified a cluster of 29 sophisticated malware samples masquerading as DICOM viewers, delivering ValleyRAT. 

Ransomware and data breaches remain the most frequent and damaging types of cyber incidents in the healthcare sector. One notable case involved the Interlock ransomware group, which has increasingly targeted healthcare organizations using ClickFix. 

In our review of data breaches across sectors, we found that healthcare remains the most impacted. Analyzing 238 data breaches reported to the US Department of Health and Human Services (HHS) from Jan 1 to April 30, 2025, and updating for the full 2025H1 period:
- 341 healthcare breaches affecting over 500 individuals each were reported.
- 29,799,648 individuals were impacted in total.
- Five breaches affected more than one million individuals each.
- 74% of breaches occurred at healthcare providers.
- 76% of breaches were attributed to hacking/IT incidents.

### 2.3. OT – The Growth of Opportunistic Attacks
Opportunistic attacks on OT environments are increasing. We observe this through two lenses:
1. **Hacktivist Activity Against OT**: Groups like GhostSec, Arabian Ghosts, Sector16, and Z-Pentest are increasingly aligning with state interests and targeting cyber-physical systems.
2. **Internet-wide Scanning and Attacks on Honeypots**: 
   - Modbus remains the most scanned OT protocol (57%).
   - Ethernet/IP holds second place (20%).
   - BACnet has risen to third place (8%).

**PLC Honeypot Observations**: Between December 2024 and March 2025, we deployed real PLC honeypots. 98% of requests used standard web protocols (HTTP/HTTPS), while only 2% used OT-native protocols. We observed occasional attempts to alter variables, stop the PLC via web interface, or connect using an engineering workstation.

## 3. Statistics
### 3.1. Vulnerabilities
In the first half of 2025, 23,581 vulnerabilities were published, a 15% increase compared to 2024.
- ![Figure 1 – New vulnerabilities per month]
- ![Figure 2 – New vulnerabilities by CVSS score]
- 63 vulnerabilities were exploited as 0-days in 2025H1, a 46% increase. ![Figure 3 – Distribution of new exploited 0-days per month and vendor]
- 132 CVEs were added to the CISA Known Exploited Vulnerabilities (KEV) catalog. ![Figure 4 – Distribution of new KEV per month and vendor]
- 47% of new CISA KEV entries were for vulnerabilities published before 2025. ![Figure 5 – New known exploited vulnerabilities by year of publication]

### 3.2. Threat Actors
Forescout Research tracks 885 threat actors. In 2025H1, 137 had notable activity:
- Cybercriminals (51%)
- State-sponsored actors (40%)
- Hacktivists (9%)

![Figure 6 – Distribution of solar power system vendors per country (top 5)]
![Figure 7 – Threat actors by country of origin]
![Figure 8 – Top 10 targeted countries]
![Figure 9 – Top 10 targeted industries]

### 3.3. Ransomware
We observed 3,649 attacks in 2025H1, a 36% increase over 2024.
![Figure 10 – Ransomware incidents per month]
![Figure 11 – Ransomware incidents per group]
![Figure 12 – Ransomware incidents per target country]
![Figure 13 – Ransomware incidents per target industry]

## 4. Deep Dive: APT IRAN and Shifting Identities – A Continuum of Iranian Hacktivist Threats to OT/ICS
Iranian hacktivist groups have consistently targeted OT/ICS in the US and Israel since 2020. These attacks are frequently tied to geopolitical flashpoints.

### 4.1. A Tale of Three Identities
We analyzed three personas: **ICTUS TEAM**, **CyberAv3ngers**, and **APT IRAN**.
- **ICTUS TEAM**: Operated 2020–2022, focused on website defacements and HMI screenshots.
- **CyberAv3ngers**: Emerged in 2023, focused on Unitronics PLCs and English-language propaganda.
- **APT IRAN**: Active since 2024, focuses on destructive actions, including ransomware and PLC manipulation.

### 4.2. Comparative Analysis
- **Targeting**: Mix of political motivation and opportunistic targeting of exposed systems.
- **Capabilities**: Preference for defacements, development of custom tools (e.g., IOCONTROL), and progressive familiarity with OT/ICS protocols.
- **Social Media**: Use of delayed channel activation and orchestrated rebranding to maintain narrative continuity.

### 4.3. What Does It All Mean?
The recurring similarities suggest these identities are coordinated by the IRGC. They form a continuum of threats divided into three phases:
1. **Test Phase (2020-2022)**: ICTUS TEAM experiments with OT/ICS.
2. **Operational Phase (2023-2024)**: CyberAv3ngers develops credible disruption capabilities.
3. **Post-sanctions Phase (2025)**: APT IRAN inherits tactics and infrastructure, escalating to destructive ransomware.

## 5. Mitigation Recommendations
Organizations should prioritize visibility and proactive controls:
- Ensure full visibility into assets (agentless solutions).
- Understand risk profiles regarding vulnerabilities and configurations.
- Disable unused services and patch vulnerabilities.
- Change default credentials and enforce MFA.
- Encrypt sensitive data.
- Avoid exposing unmanaged/legacy devices to the internet.
- Enable IP-based access control lists for OT protocols.
- Segment networks to isolate IT, IoT, and OT devices.
- Enable comprehensive endpoint logging.
- Block suspicious TLDs and conduct social engineering training.

Ensure threat detection covers the entire organization, from entry points to final targets.