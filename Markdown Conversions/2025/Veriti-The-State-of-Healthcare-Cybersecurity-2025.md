# THE STATE OF HEALTHCARE CYBERSECURITY 2025

A Veriti Research Report

VERITI.AI

## Table of Contents
- [Executive Summary](#executive-summary)
- [The Attack Landscape Under the Scope](#the-attack-landscape-under-the-scope)
- [Diagnosing the Threats](#diagnosing-the-threats)
- [Breaking Down Exposures](#breaking-down-exposures)
- [Severely Vulnerable Medical Devices and Applications](#severely-vulnerable-medical-devices-and-applications)
- [Notable Healthcare Events in 2024](#notable-healthcare-events-in-2024)
- [Veriti's Predictions and Challenges for 2025](#veritis-predictions-and-challenges-for-2025)

---

## Executive Summary

This report, conducted by the Veriti research team, provides a comprehensive analysis of healthcare cybersecurity in 2024, offering critical insights to shape strategies for 2025. Over the past year, healthcare organizations faced an alarming rise in cyberattacks, driven by ransomware groups leveraging sophisticated methods to exploit systemic vulnerabilities.

From IoT misconfigurations to cloud security challenges, the findings in this report underscore the urgent need for proactive cyber defenses.

Key findings include:

**Rising Threats**
Nearly 400 healthcare organizations in the U.S. reported cyberattacks in 2024, driven by ransomware groups such as LockBit 3.0, ALPHV/BlackCat, and BianLian.

**Critical Vulnerabilities**
Persistent OS and endpoint misconfigurations, combined with outdated medical devices, expose critical infrastructure to exploitation.

**Notable Events**
High-profile breaches like the ALPHV attack on Change Health and the exploitation of Mirth Connect highlight the urgency of addressing security gaps.

**Emerging Trends**
The rise of IoT devices, AI integration, and cloud-based PACS systems introduce new attack vectors.

---

## The Attack Landscape Under the Scope

The healthcare sector in the United States has experienced a staggering rise in cyberattacks, with nearly 400 healthcare organizations reporting incidents in the past year alone. This alarming trend highlights the vulnerabilities in critical infrastructure and the growing sophistication of attackers.

**Attacks on Third-Party Providers on the Rise:**
Cybercriminals are increasingly targeting third-party healthcare service providers and suppliers. These entities often have weaker defenses compared to larger healthcare organizations, making them attractive targets. Compromising these suppliers can create ripple effects, exposing sensitive patient data and disrupting healthcare operations on a broader scale.

**Collaboration Between Hostile Nation-States and Ransomware Groups:**
Emerging evidence points to collaborations between ransomware groups and nation-state actors. These partnerships increase the sophistication and scale of attacks, leveraging advanced techniques to bypass traditional defenses. Healthcare organizations remain a primary target due to the critical nature of their services and the high-value data they store.

**Geopolitical Risks and Their Impact:**
Geopolitical tensions continue to drive cyber activity in the healthcare sector. Adversaries use these tensions to disrupt national healthcare operations and steal sensitive information, posing risks that extend beyond financial losses to patient safety and national security.

**New Regulations to Strengthen Cybersecurity:**
In response to this growing threat landscape, new regulations are being implemented to enforce stronger cybersecurity standards in healthcare. These initiatives aim to ensure that organizations proactively address vulnerabilities, secure sensitive patient data, and reduce the risk of operational disruptions.

![Graph showing the rise in ransomware attacks on healthcare worldwide, with spikes in October and November 2023]

- **$3.5m**: The average cost of a data breach for healthcare organizations.
- **$398**: Average cost per exposed record.
- **50%**: Of healthcare organizations lack confidence in detecting and resolving data breaches.
- **42%**: Lack policies for unauthorized data access prevention.
- **51%**: Lack the technologies needed for breach prevention.
- **47%**: Lack the expertise to resolve breaches effectively.

---

## Diagnosing the Threats

Healthcare organizations in the U.S. continue to face relentless cyberattacks, with ransomware groups such as LockBit 3.0, ALPHV (BlackCat), and BianLian dominating the threat landscape. These groups target vulnerabilities across IT ecosystems, often leveraging unpatched systems, weak credentials, and well-known attack tactics.

### Commonality Between CVE/TTP and Ransomware Groups

| CVE/TTP | Ransomware Group |
| :--- | :--- |
| CVE-2021-44228 (Log4Shell) | LockBit 3.0, ALPHV (BlackCat) |
| CVE-2018-13379 (Fortinet SSL VPN) | LockBit 3.0, BianLian |
| CVE-2022-29464 (Wavlink, opennas web server) | ALPHV (BlackCat) |
| CVE-2019-19781 (Citrix ADC) | ALPHV (BlackCat), BianLian |
| CVE-2020-1472 (Zerologon) | LockBit 3.0, ALPHV (BlackCat) |
| Exploiting RDP and weak credentials | LockBit 3.0, BianLian |
| Double Extortion (data encryption + data theft) | LockBit 3.0, ALPHV (BlackCat), BianLian |
| Use of Cobalt Strike | LockBit 3.0, ALPHV (BlackCat) |
| Phishing campaigns for initial access | BianLian, ALPHV (BlackCat) |
| Living off the land (LOLBins) | LockBit 3.0, ALPHV (BlackCat), BianLian |

**Interesting Attacks in 2024**
A notable campaign in 2024 involved an unknown attacker targeting smaller healthcare associations by exploiting vulnerabilities in open-source tools such as the DoctorAppointmentSystem SQL Injection Vulnerability (CVE-2021-27314, CVE-2021-27319, CVE-2021-27320). IP Address Identified: 185.23.253.150.

**Key Statistics and Trends in Ransomware Attacks**
Veriti research found that from January to October 2024, there were 149 ransomware attacks on healthcare organizations worldwide, with 52% occurring in the United States.

- **Ransom Demands**: $7m Average ransom; $100m Highest demand.
- **Global Impact**: Healthcare accounts for 17% of all ransomware attacks across industries.
- **20%** of attackers are unknown.

---

## Breaking Down Exposures

Hospitals remain highly vulnerable to both outdated configurations and unpatched vulnerabilities.

### Active Vulnerabilities in HealthCare

| CVE | % of Hospitals Affected |
| :--- | :--- |
| CVE-2021-1675 | 45% |
| CVE-2021-34527 | 42% |
| CVE-2022-26809 | 40% |
| CVE-2023-21554 | 39% |
| CVE-2022-34721 | 36% |
| CVE-2022-34713 | 36% |
| CVE-2022-30190 | 31% |
| CVE-2022-26923 | 26% |
| CVE-2022-41128 | 22% |
| CVE-2022-21971 | 21% |

### OS Misconfigurations
- **NTLMv2 Authentication Protocol**: Enabled on 1,053 hosts.
- **Windows Defender SmartScreen Disabled**: Affecting 1,032 hosts.
- **Microsoft Windows Support Diagnostic Tool (MSDT)**: Enabled on 947 hosts.
- **Disable AllowInsecureGuestAuth**: 941 hosts.
- **EnableVirtualization Turned Off**: 883 hosts.

### Endpoint Misconfigurations
- **Lack of EDR Protection**: Numerous hosts lack active EDR despite having the tools installed.
- **Quarantine on Write Disabled**: Impacting 35% of hosts.
- **Volume Shadow Copy and Recovery Processes**: Misconfigurations affecting 22% of hosts.
- **Suspicious Processes**: 21% of hosts.
- **Force ASLR**: 17% of hosts.
- **SEH Overwrite Protection**: 12% of hosts.

---

## Severely Vulnerable Medical Devices and Applications

Healthcare systems are increasingly reliant on medical devices and applications, creating significant vulnerabilities.

![Map illustrating the widespread exposure of vulnerable healthcare devices across the United States]

### Vulnerabilities in MedDream and DICOM Applications
MedDream has several high-severity vulnerabilities with CVSS scores reaching up to 9.8.

*(Table of CVEs omitted for brevity, but includes scores ranging from 5.3 to 9.8 and EPSS scores up to 96.700%)*

### Most Exposed DICOM Web Viewer Interfaces
| Application | Host Count |
| :--- | :--- |
| OHIF DICOM Viewer | 902 |
| Orthanc Server Orthanc | 500 |
| NeoLogica RemotEye | 215 |
| XERO Viewer | 178 |
| Philips IntelliSite Digital Pathology | 82 |
| Butterfly Network Ultrasound | 14 |

---

## Notable Healthcare Events in 2024

### Change Health Breach by ALPHV
In early 2024, Change Health fell victim to a ransomware attack by the ALPHV/BlackCat group. The attackers exploited known misconfigurations and vulnerabilities to encrypt critical operational files, disrupting billing and claims processing for weeks.

### Mirth Connect Exploited as an Entry Point
In Q1 2024, vulnerabilities in Mirth Connect (CVE-2023-37679 and CVE-2023-43208) were actively exploited by both nation-state actors and cybercrime groups to exfiltrate patient records and deploy ransomware.

---

## Veriti's Predictions and Challenges for 2025

### IoT Hardening is Essential
IoT devices remain the "Achilles' heel" of healthcare cybersecurity. Without standardized patching protocols, IoT vulnerabilities will likely dominate the attack landscape.

### The Usage of AI in Healthcare
While AI enables advancements like genome mapping, it introduces significant privacy risks. Integration often places sensitive patient data outside hospital-controlled environments.

### Cloud Security First
The shift to cloud-based PACS and DICOM systems introduces new attack vectors, including misconfigurations and insecure APIs.

**Conclusion**
The findings in this report emphasize the critical role of cybersecurity in protecting healthcare’s digital transformation. Organizations must focus on addressing IoT vulnerabilities, ensuring secure cloud adoption, and protecting sensitive data exposed by AI-driven technologies. Veriti’s agentless approach integrates with your entire security stack to monitor and remediate these exposures proactively.