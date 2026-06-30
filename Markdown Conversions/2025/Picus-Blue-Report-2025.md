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

![Infographic showing Data Theft (3% Prevention Effectiveness), Password Cracking (46% Success Rate), and Valid Accounts (98% Prevention Failure Rate)]

The Blue Report 2025 highlights the essential role of Continuous Threat Exposure Management (CTEM) and emphasizes the critical importance of Adversarial Exposure Validation (AEV) in confronting increasingly sophisticated cyber threats and operational blind spots. While the Red Report 2025 highlighted the rise of credential-targeting malware and infostealers, the Blue Report identifies surprising defensive gaps, particularly in data exfiltration and password-based attacks.

Of particular concern, password cracking attempts succeeded in 46% of tested environments, nearly doubling the previous year's rate. Compounding this risk, attacks using Valid Accounts (T1078) achieved a 98% success rate, highlighting persistent challenges in maintaining effective password policies and detection.

Data exfiltration defenses suffered a severe decline, dropping to an alarming prevention rate of just 3%. This decrease is particularly concerning given the rise of double-extortion ransomware attacks designed specifically to evade traditional encryption-focused defenses.

Despite these critical gaps, Picus Attack Path Validation (APV) assessments reveal significant improvements. Domain administrator compromise rates notably fell from 24% in 2024 to 19% in 2025, with domain admin access also decreasing significantly from 40% to 22%. These advances demonstrate strengthened lateral movement defenses, improved network segmentation, and better operationalization of security validation insights.

Average prevention effectiveness declined from 69% to 62%, indicating that security controls lose efficacy without continuous validation and tuning. While detection effectiveness improved slightly, with alert scores rising from 12% to 14%, a significant gap remains between logging and detection alerts, with log failures found in 54% of Picus Detection Rule Validation (DRV) assessments.

The Blue Report 2025 reinforces that static defenses are no match for adaptive threats. To stay ahead, organizations must adopt AEV into their CTEM programs to move beyond assumptions, prioritize with confidence, and respond faster to the threats that matters most.

---

## Key Findings

The Blue Report 2025 reveals a shifting cybersecurity landscape, where progress in some areas is tempered by persistent and in some cases, deepening challenges and failures in others.

**Data Exfiltration Defense Is Getting Worse Despite Rising Risk**
For the third year in a row, data exfiltration remains the least prevented attack vector, but this year the prevention score has deteriorated even further, dropping from 9% in 2024 to just 3% in 2025.

**Password Cracking Threat Intensifies**
In 46% of environments, at least one password hash was successfully cracked and converted into cleartext, nearly doubling last year's rate of 25%.

**Significant Improvements in macOS Endpoint Security**
In a notable reversal from last year (23%), macOS endpoints achieved a 76% prevention rate, outpacing both Windows (79%) and Linux (69%) endpoints.

**Prevention Effectiveness Declines**
After a strong improvement in 2024, the average prevention score fell slightly from 69% to 62% in 2025.

**Detection Shows Modest Recovery**
The log score remained stable at 54%. However, alert score improved ever so slightly from 12% to 14%.

**SIEM Rule Failures Still Mainly Due to Logging Issues**
Analysis on detection rules revealed that log collection issues caused 50% of failures.

**BlackByte Continues to Challenge Ransomware Defense**
Ransomware remains a top concern, and BlackByte continues to be the hardest strain to prevent, with a prevention effectiveness of just 26%.

**Infrastructure Hardening Shows Measurable Progress with APV**
In 2025, only 19% of simulations led to full domain administrator compromise, down from 24% in 2024.

**Cybersecurity Product Effectiveness Still Varies in Practice**
Solutions that score 100% in MITRE ATT&CK evaluations frequently fall short in production due to infrastructure differences, misconfigurations, and integration gaps.

**Core Adversary Techniques Remain Effective**
In 2025, Valid Accounts (T1078) had the lowest prevention rate at just 2%.

---

## Key Recommendations

1. **Validate Exposure, Not Just Inventory**: Shift from simply knowing where exposures exist to proving which ones matter.
2. **Strengthen Data Exfiltration Defenses**: Implement and validate data loss prevention (DLP) rules, outbound traffic filters, and behavioral detection.
3. **Enforce Stronger Password Hygiene**: Enforce strong password policies and regularly validate credential defenses.
4. **Continuously Validate and Tune Preventive Controls**: Use real-world attack simulations to continuously validate IPS, NGFW, and endpoint security tools.
5. **Improve the End-to-End Detection Pipeline**: Strengthen the full detection pipeline from ensuring comprehensive log coverage to fine-tuning correlation rules.
6. **Strengthen Ransomware Defenses in the Era of Encryptionless Extortion**: Regularly simulate full ransomware scenarios, including data exfiltration and extortion techniques.
7. **Improve Detection of Common Techniques with Behavioral Analysis**: Techniques like Valid Accounts (T1078) and early-stage Discovery techniques require context-aware monitoring.

---

## Methodology

The findings in this year's report are based on the results of simulated attack scenarios executed by Picus Security customers from January to June 2025. The data has been anonymized and aggregated from over 160 million attack simulations.

**Definitions**
- **Prevention Effectiveness**: The percentage of successfully prevented attacks out of all simulated attacks executed.
- **Detection Effectiveness**: Assessed via **Log Score** (percentage of attacks where behavior was logged) and **Alert Score** (percentage of attacks that generate alerts).

---

## Overall Prevention and Detection Effectiveness Performance

In 2025, the prevention effectiveness score declined to 62%, down from 69% in 2024. This marks a reversal of last year's significant 10-point gain. The detection effectiveness scores showed only modest recovery; the log score held steady at 54%, and the alert score increased slightly from 12% to 14%.

---

## Real-World Performance of Cybersecurity Products

![Chart showing Prevention and Detection Scores]

Our analysis shows that control degradation is more common than most teams realize due to configuration drift, broken integrations, operational complexity, and dynamic threats. We recommend treating lab evaluations as guidance, expecting degradation, and making continuous validation part of your workflow.

---

## Uncovering Critical Defensive Gaps with Automated Penetration Testing

This year's findings from Picus APV assessments show clear progress in infrastructure hardening. In 2025, only 19 percent of simulations resulted in full domain administrator compromise, down from 24 percent in 2024. However, password cracking success rates increased dramatically to 46%.

---

## Detection Rule Effectiveness

Log collection issues accounted for 50% of all detection rule failures. Other core problems included performance issues (24%) and configuration errors (13%). Improper Log Source Coalescing was the single most common failure point, affecting 21% of assessed rules.

---

## Performance by Industry

- **Healthcare and Pharmaceuticals**: 83% prevention effectiveness.
- **Manufacturing and Engineering**: 81% prevention effectiveness.
- **Transportation**: 50% prevention effectiveness (lowest).
- **Entertainment & Hospitality**: Led in log score (81%) but had a modest alert score (20%).

---

## Performance by Region

- **Latin America (LATAM)**: 70% prevention effectiveness (highest).
- **South Asia**: 55% prevention effectiveness (lowest).
- **EMEA**: Led in log score (59%).
- **North America**: Highest alert score (20%).

---

## Performance by Attack Vector

- **Data Exfiltration**: 3% prevention effectiveness (lowest).
- **Endpoint Scenarios**: 76% prevention effectiveness.
- **Email-borne Threats**: 70% prevention effectiveness.
- **Web Application Attacks**: 63% prevention effectiveness.
- **Malware Download**: 60% prevention effectiveness.

---

## Performance by MITRE ATT&CK® Tactics

- **Discovery**: 29.75% (least prevented).
- **Exfiltration**: 30.37%.
- **Credential Access**: 77.71% (highest prevention).

---

## Performance by MITRE ATT&CK® Techniques

- **Valid Accounts (T1078)**: 2% prevention rate.
- **System Network Configuration Discovery (T1016)**: 3% prevention rate.
- **Data Encoding (T1132)**: 3% prevention rate.

---

## Performance by Threat Group

- **Outlaw**: 30% prevention score (most successful at evading).
- **Silver Fox**: 38%.
- **Dark Caracal**: 52%.

---

## Spotlight on Ransomware Attacks

- **BlackByte**: 26% prevention effectiveness (hardest to prevent).
- **BabLock**: 34%.
- **Maori**: 41%.

---

## Spotlight on Vulnerabilities

Analysis focused on CVEs disclosed in 2024 and 2025.
- **macOS Sonoma CVE-2024-27878**: 7% prevention effectiveness.
- **Linux CUPS CVE-2024-47175**: 9%.
- **Linux needrestart library CVE-2024-48990**: 9%.
- **Windows TCP/IP CVE-2024-38063**: 10%.

---

## Picus Security Customers Prevent Twice As Many Attacks

On average, our customers prevent twice as many attacks within just three months. The Picus Security Validation Platform helps organizations continuously validate and reduce their cyber risk through SCV, CSV, APV, DRV, and ASV modules.

---

## About Picus Security

Picus Security is the pioneer of Adversarial Exposure Validation, enabling organizations to understand and reduce cyber risk with precision and speed.

For more information, visit [picussecurity.com](https://picussecurity.com)

© 2025 Picus Security. All Rights Reserved.