# 2024 Analyst Report: Managed Detection and Response

## Table of Contents
- [MDR Analyst Report for 2024](#mdr-analyst-report-for-2024)
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

# MDR analyst report for 2024

## Executive summary

- **77%** of incidents were successfully remediated after the first relevant security alert was received.
- **More than two** high-severity incidents every day.

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
- Crime — 12%[^1]

### The most popular living-off-the-land attack tools:
- `powershell.exe`
- `rundll32.exe`
- `comsvcs.dll`

### The most popular MITRE ATT&CK techniques:
- `T1566: Phishing`
- `T1204: User Execution`
- `TA0001: Initial Access`
- `TA0002: Execution`

### The distribution of reported incidents by severity:
- High — 5% (observed in 5% of incidents)
- Medium — 69% (observed in 19% of incidents)
- Low — 26%

`T1098: Account Manipulation` (`TA0003: Persistence`) observed in 18% of incidents.

*\* CIS — Commonwealth of Independent States (Armenia, Azerbaijan, Belarus, Kazakhstan, Kyrgyzstan, Moldova, Russia, Tajikistan, Uzbekistan)*

**Mean time to report:**
- High-severity incidents — 54 min
- Medium — 41 min
- Low — 38 min.

[^1]: An attack carried out using malware without observable human involvement.

---

## Recommendations

- In 2024 the number of high-severity incidents decreased by 34% compared to 2023. However, mean time to investigate and report increased by 48%, indicating a rise in the average complexity of attacks. This is supported by the analysis of triggered detection rules and IoAs — the vast majority of which were from specialized XDR tools. This marks a shift from previous years, where detection by OS logs played a significant role. In these conditions, specialized tools, like XDR[^3], are essential for successful detection and investigation of modern threats.
- Human-driven targeted attacks accounted for 43% of high-severity incidents in 2024 — 74% more than in 2023 and 43% higher than in 2022. Despite advances in automated detection tools, motivated attackers can still find ways to bypass them. To counter human-driven attacks, human-driven solutions, like Managed Detection and Response[^4] are critical. For organizations with in-house security operations teams, internal processes and technologies must be equipped to handle the modern threat landscape. Comprehensive SOC consulting services[^5] can help achieve this.
- The statistics consistently show that attackers often return after a successful attack. This is especially evident in government organizations, where attackers aim for long-term presence to conduct espionage. In such cases, combining XDR-equipped in-house SOCs or outsourced MDR with regular Compromise Assessments[^6] is an effective way to detect and investigate incidents missed by existing security measures. Attackers often use Living off the Land (LotL) methods[^7] in infrastructures lacking proper system configuration controls. A relatively large number of incidents are linked to unauthorized changes, such as adding accounts to privileged groups or weakening secure configurations. To reduce false positives in these scenarios, effective configuration management and formal procedures for implementing changes and managing access are crucial.
- In 2024, User Execution[^8] and Phishing[^9] techniques were again in the top 3 threats, with nearly 5% of high-severity incidents involving successful social engineering. Users are still the weakest link, making Security Awareness[^10] an important focus for corporate information security planning.

[^3]: Kaspersky Next XDR Expert Detection and Response
[^4]: Kaspersky Managed Consulting
[^5]: Kaspersky SOC Consulting
[^6]: Kaspersky Compromise Assessment
[^7]: Kaspersky Encyclopedia. Living off the Land attack
[^8]: MITRE ATT&CK. T1204 User Execution
[^9]: MITRE ATT&CK. T1566 Phishing
[^10]: Kaspersky Security Awareness

---

## Introduction

The annual Managed Detection and Response (MDR) analyst report presents insights based on the analysis of MDR incidents identified by Kaspersky's SOC team.

The report sheds light on the most prevalent attacker tactics, techniques, and tools, as well as the characteristics of detected incidents and their distribution across regions and industry sectors among MDR customers.

This report answers key questions, including:
- Who are the potential attackers?
- What methods are they using today?
- How can their activities be effectively detected?

### About Kaspersky MDR

MDR provides round-the-clock monitoring and threat detection. Endpoint protection platforms (EPPs) transmit telemetry for analysis by machine learning and the SOC team. For threat detection, Indicators of Attack (IoA) and manual threat hunting are used. Response actions are assigned by the SOC team and, if the user approves, the EPP executes them.

---

## Kaspersky MDR scope

Kaspersky MDR customers are represented across the world, enabling us to get a comprehensive, objective view of regional attack behaviors and tactics. The geographic distribution of MDR customers shows the largest representation is in Europe, the CIS, and the META region (APAC — 13%, CIS — 21%, Europe — 40%, Latin America — 8%, META — 15%, North America — 3%).

In Europe, the largest MDR coverage is in Italy (31%), Spain (15%), and Switzerland (13%). South Africa leads the META region.

### Industry distribution

In 2024, the MDR team observed the most incidents in industrial enterprises (25.7%), financial (14.1%) and government (11.7%) sectors.

**Figure 1: Most attacked industries**  
*(Graph reflecting the presence of MDR in relevant industries by number of customers, reported incidents, and reported high-severity incidents).*

If we consider only high-severity incidents, the distribution is somewhat different: 22.8% in IT, 18.3% in government, 17.8% in industrial, and 11.9% in the financial sector.

---

## Number of incidents

In 2024, the MDR infrastructure received and processed telemetry events every day, generating security alerts as a result. Approximately 26% of these alerts were processed by machine-learning algorithms, while 13% were analyzed by the SOC team and determined to be actual incidents. MDR customers were informed about these incidents via the MDR portal.

**Figure 2: Kaspersky MDR alerts processing funnel**
- **~ 270,000 telemetry events** received from a host (this number can vary significantly depending on host activity and sensor type).
- **> 70,000 alerts** were processed automatically using AI technologies.
- **~ 200,000 alerts** were analyzed by SOC analysts.
- **~ 87% of the alerts** were identified as false positives.
- **> 26,000 alerts** were analyzed by SOC analysts.
- **~ 13,000 incidents** which were reported to customers.

---

## Incident detection time

The incident detection process consists of several steps. First, a specialized robot assigns a generated alert to the personal queue of an available SOC analyst. Next, the analyst processes the alert based on its severity and the guaranteed service level agreement (SLA) time to detect a threat. 

### Table 1: Time to detect an incident
| Severity | Time to report, in minutes | Comments |
| :--- | :--- | :--- |
| **High** | 53.99 min<br>(2023: 36.37 min)<br>(2022: 43.75 min)<br>(2021: 41.45 min) | The most complex incidents require more time to collect additional information and build an incident timeline. In 2024, this time increased by approximately 48% compared to previous periods[^2], reflecting the nature of high-severity incidents during the year. |
| **Medium** | 41.03 min<br>(2023: 32.55 min)<br>(2022: 30.92 min)<br>(2021: 34.88 min) | Medium-severity incidents were the most frequent severity level. Most of these incidents were caused by malware activity, and fully automated remediation proved effective. |
| **Low** | 37.85 min<br>(2023: 48.01 min)<br>(2022: 34.15 min)<br>(2021: 40.24 min) | Incidents with the lowest severity were mostly related to the consequences of potentially unwanted software. In most cases, processing these incidents was largely automated. |

[^2]: Kaspersky MDR analyst report for 2023, 2022, and 2021.

---

## Incident severity

In MDR, only incidents that require any action from the customer side are reported.

- **Low**: No significant impact on customer IT systems, however, there are a number of measures that need to be taken without severe consequences.
- **Medium**: No evidence of direct human involvement in the attack, may impact customer IT systems, but without severe consequences.
- **High**: Human-driven attack or malware threats with a potential or actual significant impact on the customer’s IT systems.

In 2024, there were, on average, more than three critical incidents every two days. 

**Figure 3 & 4: Incident severity level over the years**
- **2024**: High — 4.69%, Medium — 69.39%, Low — 25.92%
- **2023**: High — 7.09%, Medium — 62.73%, Low — 30.18%
- **2022**: High — 8.13%, Medium — 71.82%, Low — 20.06%
- **2021**: High — 14.34%, Medium — 65.41%, Low — 20.25%
- **2020**: High — 9.16%, Medium — 71.78%, Low — 19.06%

---

## Response efficiency

- **Approximately 76%** of incidents were detected based on a single alert.
- **Approximately 22%** of incidents were identified based on 2-10 alerts.
- **Approximately 2%** of incidents involve more than 10 alerts.

---

## The nature of high-severity incidents

### Main causes of high-severity incidents:
1. **Targeted attacks (APT)**: 43.01%
2. **Cyber exercises**: 17.49%
3. **Severe security policy violation**: 11.89%
4. **Malicious software**: 12.06%
5. **Artifacts of targeted attacks**: 7.98%
6. **Social engineering**: 4.90%
7. **Critical vulnerability**: 1.22%
8. **Insider attack**: 0.87%
9. **Denial of Service**: 0.17%

In 2024, Kaspersky detected human-driven attacks (APTs) in one in four customers, accounting for over 43% of all high-severity incidents.

---

## Detection technologies, adversary tactics, techniques and procedures

MDR enables the detection of incidents at different attack stages using multiple sensors: Endpoint Protection Platform (EPP), Network Intrusion Detection System (NIDS), and Sandbox (SB).

### Table 2: The most popular LOLBins and the frequency of their usage
| | All incidents | High-severity incidents |
| :--- | :--- | :--- |
| `powershell.exe` | 1.64% | 10.51% |
| `rundll32.exe` | 0.81% | 6.85% |
| `comsvcs.dll` | 0.26% | 3.82% |
| `reg.exe` | 0.23% | 2.07% |
| `msiexec.exe` | 0.67% | 1.59% |
| `certutil.exe` | 0.15% | 1.59% |
| `mshta.exe` | 0.22% | 1.43% |
| `msbuild.exe` | 0.07% | 1.27% |
| `esentutl.exe` | 0.07% | 1.27% |

### Table 3: Techniques with the highest conversions
| Technique | Conversion | Comments |
| :--- | :--- | :--- |
| **T1078: Valid Accounts** | 34.82% | Domain and local accounts are often used by attackers to bypass security solutions and gain persistence. |
| **T1098: Account Manipulation** | 30.30% | Attackers often activate disabled accounts and/or add members to privileged groups. |
| **T1566.002: Spearphishing Link** | 24.50% | Phishing remains the most popular technique for gaining initial access. |
| **T1110.001: Password Guessing** | 22.18% | Popular in security assessment projects and real attacks. |
| **T1210: Exploitation of Remote Services** | 20.62% | Common for initial access and lateral movement. |
| **T1547.001: Registry Run Keys / Startup Folder** | 17.58% | The most popular persistence technique. |
| **T1021: Remote Services** | 17.14% | Second most popular lateral movement technique. |
| **T1071.002: File Transfer Protocols** | 14.78% | FTP and SMB used for concealing malicious activities. |

---

## About Kaspersky

Kaspersky is a global cybersecurity and digital privacy company founded in 1997. 
- **5,000+ professionals** work at Kaspersky.
- **50% of employees** are R&D specialists.
- **5 unique centers** of expertise.
- **467k new malicious files** detected every day.
- **200k corporate customers** worldwide.
- **4.9 bln cyberattacks** detected in 2024.

Managed Detection and Response  
www.kaspersky.com  
#kaspersky  
© 2025 AO Kaspersky Lab. Registered trademarks and service marks are the property of their respective owners.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-10-14", "model": "gemini-3.5-flash-lite"} -->
