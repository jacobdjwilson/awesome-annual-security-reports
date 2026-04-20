# Managed Detection and Response Report 2024

## Table of Contents
- [Executive Summary](#executive-summary)
- [Recommendations](#recommendations)
- [Introduction](#introduction)
- [About Kaspersky MDR](#about-kaspersky-mdr)
- [Kaspersky MDR Scope](#kaspersky-mdr-scope)
- [Industry Distribution](#industry-distribution)
- [Number of Incidents](#number-of-incidents)
- [Incident Detection Time](#incident-detection-time)
- [Incident Severity](#incident-severity)
- [Response Efficiency](#response-efficiency)
- [The Nature of High-Severity Incidents](#the-nature-of-high-severity-incidents)
- [Detection Technologies, Adversary Tactics, Techniques and Procedures](#detection-technologies-adversary-tactics-techniques-and-procedures)
- [About Kaspersky](#about-kaspersky)

---

## Executive Summary

- **More than two high-severity incidents every day**
- **77% of incidents** were successfully remediated after the first relevant security alert was received.

### Key regions by number of customers:
- Europe — 40%
- CIS* — 21%
- META — 15%

### Key European countries:
- Italy — 31%
- Spain — 15%
- Switzerland — 13%

### Industries with the highest number of reported incidents:
- Industrial — 26%
- Financial — 14%
- Government — 12%

### The most common attacker profile in high-severity incidents:
- APT — 43%
- Security Assessment — 17%
- Crime¹ — 12%

### The most popular living-off-the-land attack tools:
- powershell.exe
- rundll32.exe
- comsvcs.dll

### The distribution of reported incidents by severity:
- High — 5%
- Medium — 69%
- Low — 26%

### The most popular MITRE ATT&CK techniques:
- **T1566: Phishing (TA0001: Initial Access)**: observed in 24% of incidents
- **T1204: User Execution (TA0002: Execution)**: observed in 19% of incidents
- **T1098: Account Manipulation (TA0003: Persistence)**: observed in 18% of incidents

* *CIS — Commonwealth of Independent States (Armenia, Azerbaijan, Belarus, Kazakhstan, Kyrgyzstan, Moldova, Russia, Tajikistan, Uzbekistan)*
* *¹ An attack carried out using malware without observable human involvement*

**Mean time to report high-severity incidents — 54 min, medium — 41 min, low — 38 min.**

---

## Recommendations

- In 2024 the number of high-severity incidents decreased by 34% compared to 2023. However, mean time to investigate and report increased by 48%, indicating a rise in the average complexity of attacks. This is supported by the analysis of triggered detection rules and IoAs — the vast majority of which were from specialized XDR tools. This marks a shift from previous years, where detection by OS logs played a significant role. In these conditions, specialized tools, like XDR³, are essential for successful detection and investigation of modern threats.

- Human-driven targeted attacks accounted for 43% of high-severity incidents in 2024 — 74% more than in 2023 and 43% higher than in 2022. Despite advances in automated detection tools, motivated attacker can still find ways to bypass them. To counter human-driven attacks, human-driven solutions, like Managed Detection and Response⁴ are critical. For organizations with in-house security operations team, internal processes and technologies must be equipped to handle the modern threat landscape. Comprehensive SOC consulting services⁵ can help achieve this.

- The statistics consistently show that attackers often return after a successful attack. This is especially evident in government organizations, where attackers aim for long-term presence to conduct espionage. In such cases, combining XDR-equipped in-house SOCs or outsourced MDR with regular Compromise Assessments⁶ is an effective way to detect and investigate incidents missed by existing security measures. Attackers often use Living off the Land (LotL) methods⁷ in infrastructures lacking proper system configuration controls. A relatively large number of incidents are linked to unauthorized changes, such as adding accounts to privileged groups or weakening secure configurations. To reduce false positives in these scenarios, effective configuration management and formal procedures for implementing changes and managing access are crucial.

- In 2024, User Execution⁸ and Phishing⁹ techniques were again in the top 3 threats, with nearly 5% of high-severity incidents involving successful social engineering. Users are still the weakest link, making Security Awareness¹⁰ an important focus for corporate information security planning.

---

## Introduction

The annual Managed Detection and Response (MDR) analyst report presents insights based on the analysis of MDR incidents identified by Kaspersky's SOC team.

The report sheds light on the most prevalent attacker tactics, techniques, and tools, as well as the characteristics of detected incidents and their distribution across regions and industry sectors among MDR customers.

---

## About Kaspersky MDR

MDR provides round-the-clock monitoring and threat detection. Endpoint protection platforms (EPPs) transmit telemetry for analysis by machine learning and SOC team. For threat detection Indicators of Attack (IoA) and manual threat hunting are used. Response actions are assigned by SOC team and, if user approves, EPP executes it.

---

## Kaspersky MDR Scope

![Geographic distribution chart of MDR customers]

- Europe — 40%
- CIS — 21%
- META — 15%
- APAC — 13%
- Latin America — 8%
- North America — 3%

---

## Industry Distribution

In 2024, the MDR team observed the most incidents in the industrial enterprises (25.7%), financial (14.1%) and government (11.7%) sectors.

![Most attacked industries chart]

---

## Number of Incidents

In 2024, the MDR infrastructure received and processed telemetry events every day, generating security alerts as a result.

![Kaspersky MDR alerts processing funnel]

---

## Incident Detection Time

The incident detection process consists of several steps. First, a specialized robot assigns a generated alert to the personal queue of an available SOC analyst.

| Severity | Time to report, in minutes |
| :--- | :--- |
| High | 53.99 min |
| Medium | 41.03 min |
| Low | 37.85 min |

---

## Incident Severity

In MDR, only incidents that require any action from the customer side are reported.

- **Low**: No significant impact on customer IT systems, however, there are a number of measures that need to be taken.
- **Medium**: No evidence of direct human involvement in the attack, may impact customer IT systems, but without severe consequences.
- **High**: Human-driven attack or malware threats with a potential or actual significant impact on the customer’s IT systems.

![Incident severity level chart]

---

## Response Efficiency

- **76%**: Incidents with 1 alert
- **22%**: Incidents with 2–10 alerts
- **2%**: Incidents > 10 alerts

---

## The Nature of High-Severity Incidents

In 2024, Kaspersky detected human-driven attacks (APTs) in one in four customers. These attacks accounted for over 43% of all high-severity incidents.

![Number of critical incidents by type chart]

---

## Detection Technologies, Adversary Tactics, Techniques and Procedures

MDR enables the detection of incidents at different attack stages.

![Adversary tactics heatmap]

### Adversary tactics that Kaspersky uses to detect incidents:
- **TA0043: Reconnaissance**: Scans and spear phishing.
- **TA0042: Resource Development**: Malicious or unwanted software.
- **TA0001: Initial Access**: Phishing emails and remote service compromises.
- **TA0002: Execution**: Launching specialized attack tools.
- **TA0003: Persistence**: Bootkits and suspicious network configurations.
- **TA0004: Privilege Escalation**: Adding accounts to privileged groups.
- **TA0005: Defense Evasion**: Log deletion and masquerading.
- **TA0006: Credential Access**: LSASS memory dumps and brute force.
- **TA0007: Discovery**: Internal network scans.
- **TA0008: Lateral Movement**: Network remote exploitation.
- **TA0009: Collection**: Special tools and machine learning anomaly detection.
- **TA0010: Exfiltration**: Exfiltration over C2 channels.
- **TA0011: Command and Control**: Access to malicious resources.
- **TA0040: Impact**: Crypto-miners or ransomware.

---

## About Kaspersky

Kaspersky is a global cybersecurity and digital privacy company founded in 1997. Our deep threat intelligence and security expertise is constantly transforming into innovative security solutions and services to protect businesses, critical infrastructure, governments and consumers around the globe.

- 5,000+ professionals work at Kaspersky
- 50% of our employees are R&D specialists
- 200 k corporate customers worldwide
- 4.9 bln cyberattacks detected by Kaspersky in 2024

---

[^1]: Kaspersky Next XDR Expert
[^2]: Kaspersky Managed Detection and Response
[^3]: Kaspersky SOC Consulting
[^4]: Kaspersky Compromise Assessment
[^5]: Kaspersky Encyclopedia. Living off the Land attack
[^6]: MITRE ATT&CK. T1204 User Execution
[^7]: MITRE ATT&CK. T1566 Phishing
[^8]: Kaspersky Security Awareness
[^9]: Kaspersky MDR analyst report for 2023
[^10]: Kaspersky MDR analyst report for 2022
[^11]: Kaspersky MDR analyst report for 2021
[^12]: Living Off The Land Binaries, Scripts and Libraries
[^13]: MITRE ATT&CK. S0521 BloodHound
[^14]: MITRE ATT&CK. T1041 Exfiltration Over C2 Channel
[^15]: MITRE ATT&CK. S0154 Cobalt Strike
[^16]: Qualys Community. Unmasking Lumma Stealer: Analyzing Deceptive Tactics with Fake CAPTCHA
[^17]: MITRE ATT&CK. T1218.005 System Binary Proxy Execution: Mshta
[^18]: MITRE ATT&CK. T1127.001 Trusted Developer Utilities Proxy Execution: MSBuild
[^19]: MITRE ATT&CK. T1543.003 Create or Modify System Process: Windows Service
[^20]: MITRE ATT&CK. S0404 esentutl
[^21]: Github. Msedge.exe
[^22]: Kaspersky Online File Reputation
[^23]: Github. Impacket