# Kaspersky Incident Response Report 2024

## Table of Contents
- [Executive Summary](#executive-summary)
- [Introduction](#introduction)
- [About Kaspersky Incident Response](#about-kaspersky-incident-response)
- [Geography of IR service requests](#geography-of-ir-service-requests)
- [Industries](#industries)
- [Organizational maturity](#organizational-maturity)
- [Attack duration](#attack-duration)
- [Reasons for requesting the service](#reasons-for-requesting-the-service)
- [Initial attack vector](#initial-attack-vector)
- [Adversaries’ tools](#adversaries-tools)
- [Examples of usage tools in real cases](#examples-of-usage-tools-in-real-cases)
- [The most common vulnerabilities](#the-most-common-vulnerabilities)
- [Full list of used CVEs](#full-list-of-used-cves)
- [MITRE ATT&CK tactics and techniques heatmap](#mitre-att-and-ck-tactics-and-techniques-heatmap)
- [About Kaspersky](#about-kaspersky)

## Executive Summary

### Initial attack vectors
- Exploit of a public-facing application: 39%
- Valid Accounts: 31%
- Trusted relationship: 13%

### Move around and get things done
- Implement rules for the detection of pervasive tools used by adversaries
- Conduct frequent, regular compromise assessment activities
- Employ a security tool stack with EDR-like telemetry

### Impact
- Files encrypted: 42%
- Data leakage: 17%
- Persistence installed for future impact: 11%

### Industries Targeted
- Industrial: 24%
- Government: 16%
- Financial: 13%

### Recommendations
- Implement a robust password policy and multifactor authentication
- Remove management ports from public access
- Establish a zero-tolerance policy for patch management

### Most Used Tools
- Mimikatz: 22%
- PsExec: 20%
- SoftPerfect Network Scanner: 15%

### Recommendations
- Regularly back up all critical data and store backups securely
- Establish role-based access control
- Work with an IR partner to guarantee rapid response times
- Learn adversaries and attacks targeting your industry and region to prioritize security investments

### Geographic Focus
- CIS: 51%
- Middle East: 16%
- Europe: 11%

### Security operations metrics view

#### Attack duration
- Rush (hours and days): <1 day
- Average (weeks): 13 days
- Long-lasting (months): 253 days

*Most of faster attacks are incidents with visible impact and are Ransomware attacks.*

#### Detection reasons
- Files encrypted: 39%
- Suspicious endpoint activity: 18%
- Suspicious file: 10%
- Suspicious network activity: 10%

*Notifications from security tools about suspicious activities allow to detect attacks on earlier stages and decrease the impact.*

#### Remediation duration
- Average (rush attacks): 40 hours
- Average (long-lasting attacks): 50 hours
- Average (weeks): 33 hours

*If you desire to decrease the remediation time, start preparing your IR team before incident.*

## Introduction

This analyst report contains information about cyberattacks investigated by Kaspersky in 2024. Kaspersky provides a wide range of services — incident response, digital forensics, malware analysis, etc. — to help organizations affected by information security incidents. The data used in this report is derived from working with organizations that have sought assistance with responding to incidents or held professional events for their internal incident response teams. Incident investigation and response services are provided by Kaspersky’s Global Emergency Response Team (GERT) with experts in Russia, Europe, Asia, Americas, the Middle East and Africa.

The statistics help us to identify trends relating to the most relevant threats to organizations across various sectors of the economy and regions. This enables us to develop priority protection methods and formulate recommendations which, when implemented, will help organizations enhance their security levels and prepare for incident response in the future, preventing or minimizing damage from attacks. It also gives us a figure for the threat landscape per region and per industry.

## About Kaspersky Incident Response

Kaspersky Incident Response (IR) provides a comprehensive and detailed analysis of security incidents. The service covers the entire investigation and response process, including initial response, evidence collection, identifying the primary attack vector, and developing a mitigation plan. It is an integral part of Kaspersky Security Services[^7] which ensures your organization is equipped to contain and neutralize threats with confidence.

[^7]: Kaspersky Security Services

## Geography of IR service requests

2024 saw a shift in the geography of the service coverage. The Middle East region rose to second place in terms of incident response requests with 15.7% of requests, displacing the Americas to fourth place. CIS[^8] maintains a dominant position with 50.6% of requests and continues to grow.

![Figure 1: Geography of requests for Kaspersky Incident Response services in 2024](Image description: A bar chart showing the percentage of requests for Kaspersky Incident Response services by region for 2023 and 2024. CIS is the largest region in both years. The Middle East shows a significant increase in 2024.)

- CIS[^8]: 2024 — 50.6%, 2023 — 47.3%
- Middle East: 2024 — 15.7%, 2023 — 10.9%
- Europe: 2024 — 10.8%, 2023 — 9.1%
- Americas: 2024 — 10.2%, 2023 — 21.8%
- APAC: 2024 — 7.3%, 2023 — 3.6%
- Africa: 2024 — 5.4%, 2023 — 7.3%

*Ngwxk tmmtvd? Px'ox zhm rhnk utvd, vhgmtvm nl*
*Shift is the first 2 numbers of the year of Kaspersky foundation*

Get in touch

[^8]: Commonwealth of Independent States (Armenia, Azerbaijan, Belarus, Kazakhstan, Kyrgyzstan, Moldova, Russia, Tajikistan, Uzbekistan)

## Industries

Every organization today is vulnerable to cyberattacks, as reflected in the request statistics across different industries. Last year, industrial, government, and financial sectors reached out to us the most. This is largely because these organizations tend to have more employees and higher levels of computerization, which increases their attack surface. Consequently, they are both more susceptible to attacks and more attractive targets for cybercriminals.

![Figure 2: Distribution of requests for Kaspersky Incident Response services by industry](Image description: A stacked bar chart showing the distribution of requests for Kaspersky Incident Response services by industry for 2023 and 2024. Industrial, Government, and Financial sectors consistently have the highest number of requests.)

- Industrial
- Government
- Financial
- IT
- Retail
- Transportation
- Healthcare
- Telecom
- Education
- Mass Media
- Other

## Organizational maturity

Looking at the reasons organizations make Kaspersky Incident Response service requests in more detail, we can divide them into two groups.

### Group I
(reasons and impact were already known at the time of the request)

These victims typically become aware of an attack when it had already occurred and the damage is evident.

Based on the results of our analysis, these suspicious activities had the following impacts:
- Files encrypted: 41.6%
- Data leakage: 16.9%
- Persistence installed for future impact: 10.7%
- Active Directory compromised: 9.6%
- Account takeover: 5.6%
- Data destruction: 3.4%
- Defacement: 1.7%
- Money theft: 0.6%
- Service unavailable: 0.6%
- None (False alarm): 4.5%
- None (Attack prevented or not finished): 4.5%
- Data manipulation: 0.6%

Of course, some of these incidents could also potentially escalate into more severe incidents. Detecting them at an earlier stage of the attack helps to minimize their impact.

### Group II
(attacks with indicators of suspicious activity)

### Attack duration

All incident cases can be grouped into three categories with different adversary dwell times, incident response duration, initial access, and attack impact.

#### Rush
(Hours and days)
Major high-velocity ransomware attacks that present the biggest challenge even for mature security operations. Mostly noisy adversary behavior building up on low-hanging fruit — publicly available and easily identifiable security issues.

#### Average
(Weeks)
Ransomware has made many attacks indistinguishable from faster ones (Rush attacks). In many cases in this group, there is a significant delay between initial access and the subsequent stages of the attack.

#### Long-lasting
(A month or more)
Irregular periods of active and passive phases during the attack. The duration of active phases is very similar to the previous (Average) group.

| Category | Initial vector                                        | Percentage of attacks | Average duration (median) | Incident Response duration (median) | Impact                               |
| :------- | :---------------------------------------------------- | :-------------------- | :------------------------ | :---------------------------------- | :----------------------------------- |
| Rush     | Valid Accounts                                        | 44.5%                 | <1 day                    | 33 hours                            | Encrypted data                       |
| Average  | Exploit Public-Facing Application, Trusted Relationship | 20.3%                 | 13 days                   | 40 hours                            | Encrypted data & money theft         |
| Long-lasting | Exploit Public-Facing Application, Trusted Relationship, Valid Accounts | 35.2 %                | 253 days                  | 50 hours                            | Encrypted data & data leakage        |

## Reasons for requesting the service

![Figure 3: Reasons for requesting Kaspersky Incident Response services by region](Image description: A bar chart showing the reasons for requesting Kaspersky Incident Response services by region. Files encrypted and Suspicious endpoint activity are the most common reasons across most regions.)

- Files encrypted: 38.9%
- Suspicious endpoint activity: 18.2%
- Suspicious file: 10.1%
- Suspicious network activity: 10.1%
- Data leakage: 6.6%
- Unauthorized access: 5.6%
- Security tool alert: 5.6%
- Suspicious e-mail message: 1.5%
- Money theft: 0.5%

*Suspicious activities were among the most common reasons for requests in 2024, as they can indicate the presence of attacker within the network. However, suspicious activities are also the main source of false alarms. Despite this, we recommend investigating all suspicious activities to ensure that no real attacks are missed.*

## Initial attack vector

Public-facing applications have been the main initial vector of attack for many years. In 2024, they once again ranked first, accounting for 39.2% of incidents. Trusted relationships saw an increase compared to 2023 but remained in third place at 12.8%. Valid Accounts held their position as the second most common vector at 31.4%. We also noted that phishing continues to be a prevalent initial vector, used in nearly one out of every 10 cases.

![Figure 4: Initial attack vector and resulting impact](Image description: A bar chart showing the initial attack vectors and their corresponding impacts. Exploit Public-Facing Application is the most common vector, followed by Valid Accounts and Trusted Relationship.)

- Exploit Public-Facing Application: 39.2%
- Valid Accounts: 31.4%
- Trusted Relationship: 12.7%
- Phishing: 9.8%

![Figure 5: Initial access, and attack duration](Image description: A timeline showing the relationship between initial access and attack duration, illustrating that attacks can go undetected for extended periods regardless of the initial vector.)

Based on these statistics, it can be concluded that regardless of the attackers’ initial vector, detection time is primarily influenced by the organization’s level of information security. For example, attacks using the most popular vectors can go undetected for anywhere from several days to several months.

## Adversaries’ tools

In nearly all investigations, adversaries use legitimate tools at various stages of their attacks. While different attacker groups often use their own set of tools which can be used to identify them, widely-used tools such as Mimikatz or PsExec can be used by almost any attackers for password extraction and lateral movement during post-exploitation.

### Distribution and frequency of tools used in incidents

- **Frequent, 8–22%**: Mimikatz, PsExec, ProcDump, PowerShell, BloodHound, Process Hacker, SoftPerfect Network Scanner, Impacket, ADRecon, gs-netcat, Nmap, NSSM, WMIC, Ngrok, AnyDesk, Advanced Port Scanner, Chisel, DiskCryptor, gmer.exe, Remcom, Advanced IP Scanner, netscan.exe, LaZagne
- **Average, 4–8%**: (No specific tools listed in this frequency range in the provided text)
- **Rare, 1–4%**: (No specific tools listed in this frequency range in the provided text)

Attackers most commonly use a range of utilities for remote control, evading defenses, and exploring the victim's infrastructure.

| Category            | Percentage | Tools