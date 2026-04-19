# Incident-Response-Analyst-Report 2024

## Table of Contents
- [Executive Summary](#executive-summary)
- [Introduction](#introduction)
- [About Kaspersky Incident Response](#about-kaspersky-incident-response)
- [Geography of IR Service Requests](#geography-of-ir-service-requests)
- [Industries](#industries)
- [Organizational Maturity](#organizational-maturity)
- [Attack Duration](#attack-duration)
- [Reasons for Requesting the Service](#reasons-for-requesting-the-service)
- [Initial Attack Vector](#initial-attack-vector)
- [Adversaries’ Tools](#adversaries-tools)
- [The Most Common Vulnerabilities](#the-most-common-vulnerabilities)
- [Full List of Used CVEs](#full-list-of-used-cves)
- [MITRE ATT&CK Tactics and Techniques Heatmap](#mitre-attck-tactics-and-techniques-heatmap)
- [About Kaspersky](#about-kaspersky)

---

## Executive Summary

### Initial Attack Vectors
- 39% Exploit of a public-facing application
- 31% Valid Accounts
- 13% Trusted relationship

### Impact
- 42% Files encrypted
- 17% Data leakage
- 11% Persistence installed for future impact

### Most Popular Tools
- 22% Mimikatz
- 20% PsExec
- 15% SoftPerfect Network Scanner

### Recommendations
- Implement rules for the detection of pervasive tools used by adversaries.
- Conduct frequent, regular compromise assessment activities.
- Employ a security tool stack with EDR-like telemetry.
- Implement a robust password policy and multifactor authentication.
- Remove management ports from public access.
- Establish a zero-tolerance policy for patch management.
- Regularly back up all critical data and store backups securely.
- Establish role-based access control.
- Work with an IR partner to guarantee rapid response times.
- Learn adversaries and attacks targeting your industry and region to prioritize security investments.

---

## Introduction
This analyst report contains information about cyberattacks investigated by Kaspersky in 2024. The data is derived from working with organizations that sought assistance with incident response. Services are provided by Kaspersky’s Global Emergency Response Team (GERT).

---

## About Kaspersky Incident Response
Kaspersky Incident Response (IR) provides a comprehensive analysis of security incidents, including initial response, evidence collection, identifying the primary attack vector, and developing a mitigation plan. It is an integral part of Kaspersky Security Services[^7].

[^7]: Kaspersky Security Services

---

## Geography of IR Service Requests
2024 saw a shift in service coverage. The Middle East rose to second place (15.7%), while CIS maintained a dominant position (50.6%).

![Figure 1: Geography of requests for Kaspersky Incident Response services in 2024]

---

## Industries
Industrial, government, and financial sectors reached out the most, likely due to their larger employee bases and higher levels of computerization.

![Figure 2: Distribution of requests for Kaspersky Incident Response services by industry]

---

## Organizational Maturity
Requests are divided into two groups:
- **Group I**: Reasons and impact were already known (e.g., files encrypted, data leakage).
- **Group II**: Attacks with indicators of suspicious activity.

---

## Attack Duration
- **Rush (Hours and days)**: <1 day median duration. 44.5% of attacks.
- **Average (Weeks)**: 13 days median duration. 20.3% of attacks.
- **Long-lasting (Months)**: 253 days median duration. 35.2% of attacks.

---

## Reasons for Requesting the Service
Suspicious activities (endpoint, file, network) were among the most common reasons for requests in 2024.

![Figure 3: Reasons for requesting Kaspersky Incident Response services by region]

---

## Initial Attack Vector
Public-facing applications remain the primary vector (39.2%), followed by Valid Accounts (31.4%).

![Figure 4: Initial attack vector and resulting impact]
![Figure 5: Initial access, and attack duration]

---

## Adversaries’ Tools
Adversaries frequently use legitimate tools for remote control, defense evasion, and infrastructure exploration.

- **Frequent (8–22%)**: Mimikatz, PsExec, ProcDump, PowerShell, BloodHound, Process Hacker, SoftPerfect Network Scanner.

---

## Examples of Usage Tools in Real Cases
- **Ransomware Intrusion (T1083)**: Use of File Explorer searches to identify sensitive keywords like "Confidential" or "Finance".
- **Account Discovery (T1087.002)**: Use of PowerShell to manage Active Directory and domain accounts.
- **OS Credential Dumping (T1003)**: Automated scripts to dump LSASS memory.
- **Persistence via RMM (T1219)**: Exploitation of CVE-2023-48788 to install remote management tools like ScreenConnect.

---

## The Most Common Vulnerabilities
Over 90% of exploited vulnerabilities in 2024 were published more than a year ago.

![Figure 6: Vulnerabilities from previous years that were exploited in 2024]

---

## Full List of Used CVEs
- **CVE-2016-0099**: Microsoft Windows (Secondary Logon Service) - Privilege Escalation.
- **CVE-2017-0176**: Microsoft Windows (gpkcsp.dll) - RCE.
- **CVE-2019-1458**: Microsoft Windows (Win32k) - Privilege Escalation.
- **CVE-2020-1472**: Microsoft Windows (Netlogon) - Privilege Escalation.
- **CVE-2020-0688**: Microsoft Exchange Server - RCE.
- **CVE-2020-0787**: Microsoft Windows (BITS) - Privilege Escalation.
- **CVE-2021-42287**: Microsoft Active Directory - Privilege Escalation.
- **CVE-2021-26855**: Microsoft Exchange Server - RCE.
- **CVE-2021-31207**: Microsoft Exchange Server - Security Feature Bypass.
- **CVE-2021-42278**: Microsoft Active Directory - Privilege Escalation.
- **CVE-2021-34523**: Microsoft Exchange Server - Privilege Escalation.
- **CVE-2021-34473**: Microsoft Exchange Server (Autodiscover) - RCE.
- **CVE-2022-27228**: Bitrix Site Manager - RCE.
- **CVE-2023-27532**: Veeam Backup & Replication - Missing Authentication.
- **CVE-2023-38408**: OpenSSH (ssh-agent) - RCE.
- **CVE-2023-29357**: Microsoft SharePoint Server - Privilege Escalation.
- **CVE-2023-20273**: Cisco IOS XE (Web UI) - RCE.
- **CVE-2023-20198**: Cisco IOS XE (Web UI) - Privilege Escalation.
- **CVE-2023-48788**: FortiClientEMS - SQL Injection.
- **CVE-2024-6387**: OpenSSH (sshd) - RCE.
- **CVE-2024-6409**: OpenSSH (sshd) - RCE.

---

## MITRE ATT&CK Tactics and Techniques Heatmap
The report provides a comprehensive heatmap covering tactics from Reconnaissance (TA0043) to Impact (TA0040).

---

## About Kaspersky
Kaspersky is a global cybersecurity company founded in 1997. 
- 5,000+ professionals.
- 467k new malicious files detected daily.
- 4.9 billion cyberattacks detected in 2024.