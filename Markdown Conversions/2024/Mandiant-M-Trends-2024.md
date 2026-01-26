# M-Trends 2024 Special Report

Google Cloud Security | Mandiant

## Table of Contents
- [Introduction](#introduction)
- [By the Numbers](#by-the-numbers)
    - [Global Trends](#global-trends)
    - [Campaigns and Global Events](#campaigns-and-global-events)
    - [Regional Trends](#regional-trends)
        - [Americas](#americas)
        - [JAPAC](#japac)
        - [EMEA](#emea)
    - [MITRE ATT&CK](#mitre-attck)
- [Articles](#articles)
    - [Chinese Espionage Operations Targeting The Visibility Gap](#chinese-espionage-operations-targeting-the-visibility-gap)
    - [Attacker Operations Involving Zero-Days Vary Depending on Motivation](#attacker-operations-involving-zero-days-vary-depending-on-motivation)
    - [Evolution of Phishing Amid Shifting Security Controls](#evolution-of-phishing-amid-shifting-security-controls)
    - [How Attackers Leverage AiTM to Overcome MFA](#how-attackers-leverage-aitm-to-overcome-mfa)
    - [Cloud Intrusion Trends](#cloud-intrusion-trends)
    - [Artificial Intelligence in Red (and Purple) Team Operations](#artificial-intelligence-in-red-and-purple-team-operations)
- [Conclusion](#conclusion)
- [Bibliography](#bibliography)

---

## Introduction

One of the big takeaways from our 2023 engagements, and consequently a key theme of M-Trends 2024, is that attackers are focusing more on evasion. They are aiming to avoid detection technologies (such as endpoint detection and response) and maintain persistence on networks for as long as possible, either by targeting edge devices, leveraging “living off the land” and other techniques, or through the use of zero-day vulnerabilities in security and other solutions prevalent throughout enterprises.

Despite attackers’ efforts to evade detection, defenders are continuing to get better at identifying compromises. The global median dwell time—dwell time is the number of days an attacker is on a system from compromise to detection—continued its downward trend in 2023, and is now 10 days (from 16 days in the previous year). It’s a big victory for the good guys, but ransomware is still a key factor in driving down dwell time since it tends to be detected more quickly. Furthermore, Mandiant red teams typically achieve their objectives in 5 to 7 days, so defenders must remain vigilant.

M-Trends 2024 features data and other security metrics that readers have come to expect, highlights zero-day use by espionage and financially-motivated attackers, and dives deep into evasive actions conducted particularly by Chinese espionage groups. Other key takeaways in this report include:

*   **Evolving phishing trends**: Attacker use of social media, SMS and other communications technologies.
*   **Tactics to bypass multi-factor authentication**: Adversary-in-the-middle and other techniques.
*   **Cloud intrusion trends**: Targeting of cloud infrastructure as well as attacker use of cloud resources.
*   **Use of AI in red and purple team engagements**: Focus on how new technologies can help produce better outcomes for organizations.

Mandiant consultants are always on the frontlines, investigating and analyzing the latest cyber attacks, and understanding how best to defend against them.

## By the Numbers

### Global Trends

The metrics reported in M-Trends 2024 are based on Mandiant Consulting investigations of targeted attack activity conducted between January 1, 2023 and December 31, 2023.

#### Detection by Source
In 2023, more than half of compromised organizations (54%) first learned of a compromise from an external source, while 46% first identified evidence of a compromise internally.

![Chart showing Detection by Source from 2011 to 2023. In 2023, Internal Detection is 46% and External Detection is 54%. This is a decrease in external notifications from 63% in 2022.]

**Ransomware-Related Intrusions**
In 70% of cases, organizations learned of ransomware-related intrusions from external sources. Of those external notifications, 76% came from an Adversary Notification (ransom note) and 24% from an External Partner.

#### Dwell Time
Global median dwell time continued a downward trend. In 2023, most organizations detected intrusions within 10 days.

*   **Global Median Dwell Time**: 10 days (down from 16 days in 2022).
*   **Internal Detection Dwell Time**: 9 days.
*   **External Detection Dwell Time**: 13 days.

**Global Dwell Time Distribution (2023)**
*   1 week or less: 43.3%
*   30 days or less: 22.7%
*   6 months or less: 22.3%
*   1 year or less: 5.4%
*   5 years or less: 6.0%
*   5 years or more: 0.3%

**Ransomware vs. Non-Ransomware Dwell Time**
*   **Ransomware**: 5 days (down from 9 days in 2022).
*   **Non-Ransomware**: 13 days (down from 17 days in 2022).

#### Industry Targeting
Mandiant most frequently responded to intrusions in the following sectors:

1.  **Financial**: 17.3%
2.  **Business and Professional Services**: 13.3%
3.  **High Tech**: 12.4%
4.  **Retail and Hospitality**: 8.6%
5.  **Healthcare**: 8.1%
6.  **Government**: 8.1%

#### Initial Infection Vector
When identified, the initial infection vectors were:

*   **Exploit**: 38%
*   **Phishing**: 17%
*   **Prior Compromise**: 15%
*   **Stolen Credentials**: 10%
*   **Brute Force**: 6%

**Most Frequently Seen Vulnerabilities**
1.  **MOVEit Transfer**: CVE-2023-34362
2.  **Oracle Web Applications Desktop Integrator**: CVE-2022-21587
3.  **Barracuda ESG**: CVE-2023-2868

#### Post-Compromise Activity
*   **Financial Gain**: 36% of intrusions (up from 26% in 2022).
*   **Data Theft**: 37% of intrusions.
*   **Multiple Threat Groups**: Identified in 17% of environments.

#### Threat Groups and Malware
Mandiant tracks more than 4,000 threat groups. In 2023:
*   719 newly tracked threat groups.
*   626 newly tracked malware families.
*   **Top Malware Categories**: Backdoors (33%), Downloaders (16%), Droppers (15%).

**Most Frequently Seen Malware Families (2023)**
1.  **BEACON**: 10%
2.  **ALPHV**: 5%
3.  **LEMURLOOT**: 5%
4.  **SYSTEMBC**: 5%
5.  **LOCKBIT**: 4%

### Campaigns and Global Events

Mandiant tracked 25 campaigns and global events in 2023. A prominent example was the **FIN11 MOVEit exploitation campaign (CVE-2023-34362)**.

**Timeline of CVE-2023-34362:**
*   **May 15**: First observed FIN11 scanning.
*   **May 27**: First known exploitation and start of data exfiltration.
*   **May 31**: Progress Software released patch and disclosed vulnerability.
*   **June 6**: CL0P leaks site claimed responsibility.

### Regional Trends

#### Americas
*   **Median Dwell Time**: 10 days.
*   **Internal Detection**: 49%.
*   **External Detection**: 51%.
*   **Top Vector**: Exploit (41%).
*   **Prevalent Group**: FIN11 (MOVEit and GoAnywhere MFT exploitation).

#### JAPAC
*   **Median Dwell Time**: 9 days (significant drop from 33 days in 2022).
*   **Internal Detection**: 31%.
*   **External Detection**: 69%.
*   **Top Vector**: Exploit (39%).
*   **Prevalent Group**: UNC4841 (Barracuda ESG zero-day exploitation).

#### EMEA
*   **Median Dwell Time**: 22 days.
*   **Internal Detection**: 46%.
*   **External Detection**: 54%.
*   **Top Vector**: Exploit (37%).
*   **Prevalent Group**: UNC4393 (BASTA ransomware).

### MITRE ATT&CK

Mandiant observed adversaries use 74% of MITRE ATT&CK techniques.

**Top 10 Most Frequently Seen Techniques:**
1.  **T1059**: Command and Scripting Interpreter (52.3%)
2.  **T1027**: Obfuscated Files or Information (46.5%)
3.  **T1083**: File and Directory Discovery (38.6%)
4.  **T1021**: Remote Services (37.3%)
5.  **T1082**: System Information Discovery (37.1%)
6.  **T1070**: Indicator Removal (35.1%)
7.  **T1071**: Application Layer Protocol (34.0%)
8.  **T1033**: System Owner/User Discovery (31.7%)
9.  **T1140**: Deobfuscate/Decode Files or Information (31.5%)
10. **T1190**: Exploit Public-Facing Application (28.7%)

**Top 5 Sub-Techniques:**
1.  **T1059.001**: PowerShell (32.3%)
2.  **T1071.001**: Web Protocols (29.6%)
3.  **T1021.001**: Remote Desktop Protocol (28.3%)
4.  **T1569.002**: Service Execution (26.8%)
5.  **T1070.004**: File Deletion (26.6%)

---

## Articles

### Chinese Espionage Operations Targeting The Visibility Gap

Endpoint detection and response (EDR) platforms have forced attackers to evolve. China-nexus attackers are increasingly targeting "edge devices"—firewalls, email filters, VPNs, and hypervisors—where EDR visibility is often lacking.

**Key Characteristics of these Operations:**
*   **Custom Malware for Edge Devices**: Development of tailored malware for proprietary operating systems (e.g., BOLDMOVE for Fortinet).
*   **Evasion Techniques**: Disabling logging daemons (`miglogd`, `syslogd`) and patching memory to hide activity.
*   **Living off the Land**: Using native API calls (e.g., THINCRUST) to disguise C2 traffic as legitimate management activity.
*   **Persistence via Hypervisors**: UNC3886 used VMCI sockets to communicate between ESXi hosts and guest VMs, bypassing network segmentation.

**Example Malware:**
*   **TABLEFLIP**: A network traffic redirection utility.
*   **DEPTHCHARGE**: A passive backdoor for Barracuda ESG that persists in configuration databases, surviving device replacements.

### Attacker Operations Involving Zero-Days Vary Depending on Motivation

In 2023, Mandiant tracked 97 unique zero-day vulnerabilities exploited in-the-wild, a 56% increase from 2022.

**Comparison of Motivations:**
*   **Financially Motivated (e.g., FIN11/MOVEit)**: Prioritize speed and volume. FIN11 targeted over 2,600 organizations for rapid data theft and extortion.
*   **Espionage (e.g., UNC4841/Barracuda ESG)**: Prioritize stealth and long-term access. UNC4841 targeted ~5% of vulnerable appliances for sustained intelligence gathering.

### Evolution of Phishing Amid Shifting Security Controls

With Microsoft blocking macros by default, attackers have shifted tactics:
*   **New Payloads**: Use of OneNote files, LNK files, and password-protected ZIP/RAR archives to bypass scanners.
*   **Alternative Platforms**: Phishing via Microsoft Teams, LinkedIn, and SMS (Smishing).
*   **Quishing**: Using QR codes in emails to direct users to malicious sites on mobile devices, where security visibility is lower.

### How Attackers Leverage AiTM to Overcome MFA

Adversary-in-the-Middle (AiTM) attacks use reverse proxies to intercept not just credentials, but also post-authentication session tokens. This renders traditional MFA (Push, OTP) ineffective.

**Mitigation**: Organizations should move toward phishing-resistant MFA, such as FIDO2 hardware keys or Certificate-Based Authentication (CBA).

### Cloud Intrusion Trends

Attackers are pivoting to cloud environments to target hosted data and leverage compute resources for cryptomining.
*   **Identity Abuse**: Using SIM swapping to bypass SMS-based MFA and targeting weakly stored credentials in public code repositories.
*   **Service Abuse**: Using Azure Data Factory to exfiltrate data to attacker-controlled SFTP servers.
*   **Persistence**: Using the Azure Serial Console to gain administrative access to VMs without triggering traditional network alerts.

### Artificial Intelligence in Red (and Purple) Team Operations

Mandiant's Red Teams are leveraging Generative AI (Gen AI) to improve efficiency:
*   **Social Engineering**: Rapidly drafting convincing phishing pretexts and landing pages.
*   **Tool Development**: Generating code for custom enumeration scripts and specialized exploits.
*   **Knowledge Acquisition**: Using LLMs to quickly understand complex, bespoke defensive stacks during purple team engagements.

---

## Conclusion

The continued decrease in global median dwell time is a positive trend, yet attackers are compensating by focusing on evasion. The increased use of zero-day vulnerabilities and the targeting of edge devices represent the most challenging trends for 2024. Preparation must be layered, involving not just technical hardening but also regular red team exercises and tabletop simulations.

---

## Bibliography

[^1]: https://community.progress.com/s/article/MOVEit-Transfer-Critical-Vulnerability-31May2023
[^2]: https://cloud.google.com/blog/topics/threat-intelligence/separating-signal-noise-how-mandiant-intelligence-rates-vulnerabilities-intelligence
[^6]: https://www.justice.gov/opa/pr/justice-department-announces-court-authorized-action-disrupt-illicit-revenue-generation
[^9]: https://cloud.google.com/blog/topics/threat-intelligence/unc3944-sms-phishing-sim-swapping-ransomware
[^10]: https://cloud.google.com/blog/topics/threat-intelligence/apt29-evolving-diplomatic-phishing
[^13]: https://cloud.google.com/blog/topics/threat-intelligence/apt43-north-korea-cybercrime-espionage
[^14]: https://www.justice.gov/opa/pr/justice-department-disrupts-prolific-alphvblackcat-ransomware-variant
[^23]: https://www.fbi.gov/news/stories/fbi-partners-dismantle-qakbot-infrastructure-in-multinational-cyber-takedown
[^35]: https://blog.google/technology/safety-security/googles-ai-red-team-the-ethical-hackers-making-ai-safer/
[^38]: https://cloud.google.com/blog/topics/threat-intelligence/threat-actors-generative-ai-limited

*(Note: Full bibliography contains 38 references as listed in the original report.)*