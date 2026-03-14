# The State of Threat Exposure Management: Blue-Report 2025

Organization: Picus  
Report Title: Blue-Report  
Year: 2025

## Table of Contents
- [Introduction](#introduction)
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [Key Recommendations](#key-recommendations)
- [Methodology](#methodology)
- [Overall Prevention and Detection Effectiveness Performance](#overall-prevention-and-detection-effectiveness-performance)
- [Real-World Performance of Cybersecurity Products](#real-world-performance-of-cybersecurity-products)
- [Uncovering Critical Defensive Gaps with Automated Penetration Testing](#uncovering-critical-defensive-gaps-with-automated-penetration-testing)
- [Detection Rule Effectiveness](#detection-rule-effectiveness)
- [Performance by Industry](#performance-by-industry)
- [Performance by Region](#performance-by-region)
- [Performance by Attack Vector](#performance-by-attack-vector)
- [Performance by MITRE ATT&CK® Tactics](#performance-by-mitre-attck-tactics)
- [Performance by MITRE ATT&CK® Techniques](#performance-by-mitre-attck-techniques)
- [Performance by Threat Group](#performance-by-threat-group)
- [Spotlight on Ransomware Attacks](#spotlight-on-ransomware-attacks)
- [Spotlight on Vulnerabilities](#spotlight-on-vulnerabilities)

---

## Introduction

**At a Glance**
- Prevention Score: from 69% to 62%
- Log Score: from 54% to 54%
- Alert Score: from 12% to 14%

Currently in its third year, the 2025 edition of the Blue Report continues to deliver data-driven insights and actionable recommendations for cybersecurity professionals by evaluating the real-world effectiveness of prevention and detection capabilities. Developed by Picus Labs, this annual study is based on over 160 million attack simulations performed on the Picus Security Validation Platform, providing a comprehensive view of how security products and configurations perform across modern enterprise environments.

The Blue Report 2025 is designed to serve as a practical guide for security teams and decision-makers aiming to mature their security posture through Continuous Threat Exposure Management (CTEM). By identifying blind spots, validating assumptions, and fine-tuning defenses based on adversary behavior, organizations can reduce uncertainty, better prioritize resources, and build a more resilient cybersecurity foundation.

**What’s New This Year**
- This year, we've deepened the report's focus on prevention and detection effectiveness across attack vectors, regions, and industries. For the 2025 report, we've expanded our analysis to assess prevention performance against MITRE ATT&CK techniques, revealing alarmingly low prevention effectiveness across industries against frequently used adversary behaviors.
- The vulnerability section now focuses exclusively on CVEs disclosed in 2024 and 2025, offering a clearer view of how well organizations are addressing new and emerging threats. Findings from Attack Path Validation (APV) and Detection Rule Validation (DRV) highlight persistent gaps in lateral movement prevention, privilege escalation defense, and overall detection effectiveness.

---

## Executive Summary

The Blue Report 2025 highlights the essential role of Continuous Threat Exposure Management (CTEM) and emphasizes the critical importance of Adversarial Exposure Validation (AEV) in confronting increasingly sophisticated cyber threats and operational blind spots. While the Red Report 2025 highlighted the rise of credential-targeting malware and infostealers, the Blue Report identifies surprising defensive gaps, particularly in data exfiltration and password-based attacks.

Of particular concern, password cracking attempts succeeded in 46% of tested environments, nearly doubling the previous year's rate. Compounding this risk, attacks using Valid Accounts (T1078) achieved a 98% success rate, highlighting persistent challenges in maintaining effective password policies and detection.

Data exfiltration defenses suffered a severe decline, dropping to an alarming prevention rate of just 3%. This decrease is particularly concerning given the rise of double-extortion ransomware attacks designed specifically to evade traditional encryption-focused defenses.

Despite these critical gaps, Picus Attack Path Validation (APV) assessments reveal significant improvements. Domain administrator compromise rates notably fell from 24% in 2024 to 19% in 2025, with domain admin access also decreasing significantly from 40% to 22%. These advances demonstrate strengthened lateral movement defenses, improved network segmentation, and better operationalization of security validation insights.

Average prevention effectiveness declined from 69% to 62%, indicating that security controls lose efficacy without continuous validation and tuning. While detection effectiveness improved slightly, with alert scores rising from 12% to 14%, a significant gap remains between logging and detection alerts, with log failures found in 54% of Picus Detection Rule Validation (DRV) assessments.

The Blue Report 2025 reinforces that static defenses are no match for adaptive threats. To stay ahead, organizations must adopt AEV into their CTEM programs to move beyond assumptions, prioritize with confidence, and respond faster to the threats that matters most.

---

## Key Findings

The Blue Report 2025 reveals a shifting cybersecurity landscape, where progress in some areas is tempered by persistent and in some cases, deepening challenges and failures in others.

- **Data Exfiltration Defense Is Getting Worse Despite Rising Risk**: For the third year in a row, data exfiltration remains the least prevented attack vector, dropping from 9% in 2024 to just 3% in 2025.
- **Password Cracking Threat Intensifies**: In 46% of environments, at least one password hash was successfully cracked, nearly doubling last year's rate of 25%.
- **Significant Improvements in macOS Endpoint Security**: macOS endpoints achieved a 76% prevention rate, outpacing both Windows (79%) and Linux (69%) endpoints.
- **Prevention Effectiveness Declines**: The average prevention score fell from 69% to 62% in 2025.
- **Detection Shows Modest Recovery**: The log score remained stable at 54%, while the alert score improved slightly from 12% to 14%.
- **SIEM Rule Failures Still Mainly Due to Logging Issues**: Log collection issues caused 50% of failures.
- **BlackByte Continues to Challenge Ransomware Defense**: BlackByte remains the hardest strain to prevent, with a prevention effectiveness of just 26%.
- **Infrastructure Hardening Shows Measurable Progress with APV**: Only 19% of simulations led to full domain administrator compromise, down from 24% in 2024.
- **Cybersecurity Product Effectiveness Still Varies in Practice**: Solutions that score 100% in lab evaluations frequently fall short in production due to infrastructure differences and misconfigurations.
- **Core Adversary Techniques Remain Effective**: Valid Accounts (T1078) had the lowest prevention rate at just 2%.

---

## Key Recommendations

- **Validate Exposure, Not Just Inventory**: Shift from simply knowing where exposures exist to proving which ones matter.
- **Strengthen Data Exfiltration Defenses**: Implement and validate DLP rules, outbound traffic filters, and behavioral detection.
- **Enforce Stronger Password Hygiene**: Enforce strong password policies and regularly validate credential defenses.
- **Continuously Validate and Tune Preventive Controls**: Use real-world attack simulations to validate IPS, NGFW, and endpoint security tools.
- **Improve the End-to-End Detection Pipeline**: Strengthen the full detection pipeline from log coverage to fine-tuning correlation rules.
- **Strengthen Ransomware Defenses**: Regularly simulate full ransomware scenarios, including data exfiltration and extortion techniques.
- **Improve Detection of Common Techniques with Behavioral Analysis**: Use context-aware monitoring and identity-aware detection logic.

---

## Methodology

The findings in this year's report are based on the results of simulated attack scenarios executed by Picus Security customers from January to June 2025. The data has been anonymized and aggregated from over 160 million attack simulations.

**Definitions**
- **Prevention Effectiveness**: The percentage of successfully prevented attacks out of all simulated attacks.
- **Detection Effectiveness**: Assessed via **Log Score** (percentage of attacks logged) and **Alert Score** (percentage of attacks that generate alerts).

---

## Overall Prevention and Detection Effectiveness Performance

In 2025, the prevention effectiveness score declined to 62%, down from 69% in 2024. This marks a reversal of last year's significant 10-point gain. Detection effectiveness scores showed only modest recovery; the log score held steady at 54%, and the alert score increased slightly from 12% to 14%.

---

## Real-World Performance of Cybersecurity Products

![Chart showing variability between lab and production performance]

Cybersecurity products often show significant variability in real-world environments compared to lab tests. Control degradation is common due to configuration drift, broken integrations, operational complexity, and dynamic threats.

---

## Uncovering Critical Defensive Gaps with Automated Penetration Testing

Using Picus Attack Path Validation (APV), we found that only 19% of simulations resulted in full domain administrator compromise, down from 24% in 2024. However, password cracking success rates increased to 46%, emphasizing that compromised credentials remain a fast track to privilege escalation.

---

## Detection Rule Effectiveness

Log collection issues accounted for 50% of all detection rule failures. Other core problems included performance issues (24%) and configuration errors (13%).

---

## Performance by Industry

- **Healthcare and Pharmaceuticals**: Led all sectors with an 83% prevention effectiveness score.
- **Transportation**: Registered the lowest prevention score at 50%.
- **Entertainment & Hospitality**: Led in log score (81%) but had a modest alert score (20%).

---

## Performance by Region

- **LATAM**: Strongest performer in prevention (70%).
- **South Asia**: Most exposed region (55% prevention) and lowest alert score (9%).
- **EMEA**: Led in log score (59%).

---

## Performance by Attack Vector

- **Data Exfiltration**: Least prevented attack vector (3%).
- **Endpoint Scenarios**: 76% prevention rate.
- **Email-borne Threats**: 70% prevention rate.
- **Malware Download**: 60% prevention rate.

---

## Performance by MITRE ATT&CK® Tactics

- **Discovery**: Least prevented tactic (29.75%).
- **Exfiltration**: 30.37% prevention.
- **Credential Access**: Best performing tactic (77.71%).

---

## Performance by MITRE ATT&CK® Techniques

- **Valid Accounts (T1078)**: Lowest prevention rate (2%).
- **System Network Configuration Discovery (T1016)**: 3% prevention.
- **Data Encoding (T1132)**: 3% prevention.

---

## Performance by Threat Group

- **Outlaw**: Most successful at evading defenses (30% prevention).
- **Silver Fox**: 38% prevention.
- **Dark Caracal**: 52% prevention.

---

## Spotlight on Ransomware Attacks

- **BlackByte**: Least prevented ransomware (26%).
- **BabLock**: 34% prevention.
- **Maori**: 41% prevention.

---

## Spotlight on Vulnerabilities

Analysis focused on CVEs disclosed in 2024 and 2025.
- **macOS Sonoma CVE-2024-27878**: Least prevented (7%).
- **Linux CUPS CVE-2024-47175**: 9% prevention.
- **Windows TCP/IP CVE-2024-38063**: 10% prevention.

---

## Picus Security Customers Prevent Twice As Many Attacks

On average, customers using the Picus Security Validation Platform prevent twice as many attacks within three months. The platform includes Security Control Validation (SCV), Cloud Security Validation (CSV), Attack Path Validation (APV), Detection Rule Validation (DRV), and Attack Surface Validation (ASV).

---

## About Picus Security

Picus Security is the pioneer of Adversarial Exposure Validation, enabling organizations to understand and reduce cyber risk with precision and speed. For more information, visit [picussecurity.com](https://www.picussecurity.com).

© 2025 Picus Security. All Rights Reserved.