# Blue-Report 2024

Organization: Picus
Report Title: Blue-Report
Year: 2024

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
- [Performance by MITRE ATT&CK Tactic](#performance-by-mitre-attck-tactic)
- [Performance by Threat Group](#performance-by-threat-group)
- [Spotlight on Ransomware Attacks](#spotlight-on-ransomware-attacks)
- [Spotlight on Vulnerabilities](#spotlight-of-vulnerabilities)

---

## Introduction

Now in its second year, the 2024 edition of the Blue Report provides key findings and practical recommendations for cybersecurity professionals by evaluating the effectiveness of current detection and prevention practices. Conducted by Picus Labs, this annual study uses over 136 million attack simulations on The Picus Security Validation Platform to assess the real-world performance of leading security products. These simulations cover a diverse variety of attack vectors, threat groups, ransomware attacks, vulnerabilities, and more – highlighting both progress and ongoing challenges in threat detection and prevention.

This year's report introduces results from the Attack Path Validation (APV) and Detection Rule Validation (DRV) products on the Picus platform, offering deeper observations into organizational preparedness against automated penetration tests and the effectiveness of detection rules in SIEM systems.

The Blue Report 2024 serves as a crucial resource for cybersecurity professionals and decision-makers. It provides perspective into the current state of cybersecurity and recommends Continuous Threat Exposure Management (CTEM) for those working to adopt a holistic approach. By addressing these defensive gaps and optimizing detection and prevention strategies, organizations can enhance their resilience against even the most advanced cyber threats.

## Executive Summary

The Blue Report 2024 emphasizes the need for a holistic approach to Continuous Threat Exposure Management (CTEM) to strengthen defenses against cyber threats. While we’ve seen significant advancements since the 2023 Blue Report, several critical vulnerabilities persist, underscoring the necessity for continuously optimizing your organization’s defenses.

Automated penetration tests conducted by Picus Attack Path Validation (APV) revealed that 40% of tested environments had paths leading to domain administrator access, posing severe risks of compromised total network control.

The analysis of attack simulations performed by the Picus Security Control Validation (SCV) revealed notable variability in the real-world performance of leading cybersecurity products. Even top performers in controlled evaluations like MITRE ATT&CK showed differing effectiveness in operational environments, underscoring how critically important it is to continuously validate and fine-tune your security controls.

A bright spot, organizations exhibited significant improvement in prevention effectiveness from last year’s report, with scores rising from 59% in 2023 to 69% in 2024. However, detection effectiveness presented mixed results with log scores improving from 37% to 54% year over year, but alert scores actually declining slightly from 16% to 12%. This signals a pressing need for security teams to enhance visibility and alert mechanisms in SIEMs and EDRs. A deeper dive into SIEM system detection rules with Picus Detection Rule Validation (DRV) revealed that most issues are related to log collection (38%) and performance (33%).

Key recommendations from the report include enhancing exposure management through comprehensive validation and continuous fine-tuning of security measures. We strongly suggest organizations adopt a “proactive security” mindset to better manage their exposure to cyber threats. By adopting these strategies, organizations can more effectively protect themselves against evolving cyber threats and enhance their overall security posture.

## Key Findings

The Blue Report 2024 provides a comprehensive examination of the current state of threat exposure management. This year’s findings reveal several critical vulnerabilities and underscore cybersecurity teams’ challenges in maintaining robust defenses against evolving cyber threats. Below are some of the most significant findings from the report:

- **High-Risk Attack Paths**: The report reveals a significant vulnerability across 40% of tested environments, where attack paths could lead to domain administrator access. Such access gives attackers control over user accounts, security settings, and overall network management, much like having a master key to the network.

- **Prevention vs. Detection Effectiveness**: Despite achieving a higher Log Score, which rose from 37% to 54%, indicating better data capture and monitoring, the Alert Score fell to 12% from 16% from last year’s report. This reduction suggests that increased logging has not translated to improved visibility and faster threat detection. The disparity points to a need for organizations to prioritize optimization across their entire detection engineering pipeline.

- **Variability in Cybersecurity Product Performance**: We observed a significant variability between the performance of cybersecurity products in controlled environments versus real-world settings. Products that score 100% in evaluations like MITRE ATT&CK can unfortunately exhibit significant effectiveness variability once deployed across diverse operational environments. This underscores the necessity for continuous validation and ongoing fine-tuning.

- **Detection Rule Challenges in SIEM Systems**: The majority of issues we identified in the detection rules of SIEM systems were related to log collection (38%) and performance (33%). Improper log source consolidation affected 23% of cases, while unavailable (10%) and broken log sources (5%) further deepened detection challenges.

- **Endpoint Security Gaps**: We found that macOS endpoints were significantly more likely to be misconfigured or correctly operate without Endpoint Detection and Response (EDR) tools. As a result, they prevented only 23% of simulated attacks, compared to 62% and 65% for Windows and Linux endpoints, respectively. This underscores a substantial gap in IT and security teams' skill sets and strategies for securing macOS environments.

- **Ransomware Defense Challenges**: We found that BlackByte was the most challenging ransomware variant to defend against, with only 17% of organizations successfully preventing it. BabLock and Hive followed closely behind, with prevention rates of 20% and 30% respectively, indicating the need for organizations to develop even stronger ransomware defense strategies.

- **Easy to Crack Passwords**: In 25% of environments, attackers could successfully crack at least one dumped password hash, converting it into a cleartext password.

## Key Recommendations

The Blue Report 2024 highlights several critical areas that require attention to enhance organizations’ cybersecurity defenses. Based on our in-depth findings and analysis, we propose the following key recommendations for organizations to strengthen their threat exposure management:

- ✔ **Adopt a Proactive Security Mindset**: If you haven’t already, it’s definitely time to shift from a reactive to a proactive and continuous approach to cybersecurity. This involves constantly identifying and mitigating potential threats and vulnerabilities before they can breach, infiltrate, or otherwise attack or compromise your organization.

- ✔ **Implement Continuous Threat Exposure Management (CTEM)**: Establish a comprehensive CTEM program to continually identify, prioritize, validate and fix exposures. This helps in maintaining a robust security posture even as the threat landscape continues to evolve.

- ✔ **Enhance Detection and Prevention Mechanisms**: Improve detection capabilities by optimizing the entire detection engineering pipeline, including log collection, performance, and alert mechanisms in SIEM and EDR systems. Regularly review and update detection rules to ensure they remain effective against the latest threats.

- ✔ **Strengthen Ransomware Defenses**: Implement the latest, most effective backup and recovery solutions and ensure that all endpoints have up-to-date security controls. Conduct regular simulations of ransomware attacks to test and improve the effectiveness of your response strategies.

- ✔ **Improve Endpoint Security Configuration**: Ensure that security controls on all endpoints, including macOS systems, are properly configured and that appropriate EDR tools are in place. Conduct regular audits and endpoint security assessments to identify and fix any misconfigurations.

- ✔ **Enhance Log Management and Analysis**: Address common issues in log collection and performance to improve the effectiveness of detection rules in SIEM systems. Double check proper log source consolidation and availability.

- ✔ **Prioritize Password Security**: Implement strong password policies and confirm that your password hashing methods are robust to prevent easy cracking of password hashes. Regularly audit and enforce your compliance with best practices for password security across your organization.

## Methodology

The findings in this report are based on the results of simulated attack scenarios executed by Picus Security customers from January to June 2024. The data has been anonymized and aggregated from over 136 million attack simulations. Research and analysis was completed by Picus Labs and Picus Data Science teams.

### Definitions

**Prevention Effectiveness** evaluates an organization's ability to block potential cyberattacks through its security controls. This metric is the percentage of successfully prevented attacks out of all simulated attacks executed.

**Detection Effectiveness** assesses an organization’s capability to identify potential cyber threats through its existing security controls. This report uses two key indicators:
- **Log Score**: Measures the percentage of simulated attacks where the attackers’ behavior was logged.
- **Alert Score**: Indicates the percentage of simulated attacks that generate alerts.

### Scoring Legend

![Table showing threat exposure management scoring levels: Optimized (90-100%), Managed (70-89%), Moderate (40-69%), Basic (20-39%), and Inadequate (0-19%)]

## Overall Prevention and Detection Effectiveness Performance

This year's report highlights a complex landscape for cyberattack prevention and detection within organizations. While there was noticeable progress in some areas, other critical aspects reveal ongoing challenges.

### Prevention Effectiveness
In 2024, we observed a significant improvement in organizations' overall ability to prevent cyberattacks. The average prevention effectiveness score rose from 59% in 2023 to 69% this year.

### Detection Effectiveness
In 2024, the state of detection effectiveness exhibited both progress and setbacks. The average log score increased from 37% to 54%. However, the alert score fell to a concerning 12%, down from 16% in 2023.

### Addressing the Gaps
More logs do not necessarily equate to more visibility or better security outcomes. Organizations should adopt an "assume breach" mindset to bridge these gaps.

## Real-World Performance of Cybersecurity Products

Real-world data shows that even best-of-breed products that score 100% in controlled settings (like MITRE ATT&CK) can exhibit a wide range of prevention and detection effectiveness once deployed. We attribute this to:
1. Environmental and Configurational Differences.
2. Context and Deployment Nuances.
3. Dynamic Nature of Threats.

We recommend:
1. **Continuous Validation**: Regularly test and validate security products.
2. **Ongoing Fine-Tuning**: Security tools should not be considered set-and-forget.

## Uncovering Critical Defensive Gaps with Automated Penetration Testing

Picus Attack Path Validation (APV) was able to successfully achieve domain administrator status in 24% of the tests conducted. In 40% of the tested environments, there was at least one instance where domain administrator access was achieved. Additionally, 25% of environments tested revealed that attackers were able to successfully crack password hashes.

## Detection Rule Effectiveness

We identified several concerns regarding detection rules in SIEM systems:
- **Improper Log Source Consolidation**: 23% of cases.
- **Unavailable Log Source**: 10% of cases.
- **Broken Log Source**: 5% of cases.
- **Performance-related issues**: Collectively 33% of observed issues.

## Performance by Industry

- **Prevention**: Healthcare and Pharmaceuticals showed the most dramatic improvement (56% to 76%). Entertainment & Hospitality led at 86%.
- **Detection**: Media and Entertainment emerged as the leader in 2024 with a log score of 85% and an alert score of 37%. Transportation and Logistics saw a decline, with a log score of 10% and an alert score of 2%.

## Performance by Region

- **Prevention**: South Asia improved from 44% to 60%. APAC increased from 64% to 74%.
- **Detection**: APAC saw a decline in log scores (66% to 45%) and alert scores (21% to 6%). North America recorded a decrease in log scores (60% to 49%) and alert scores (37% to 10%).

## Performance by Attack Vector

- **Data Exfiltration**: Prevention effectiveness dropped from 18% to 9%.
- **Endpoint Attacks**: Improved from 46% to 62%.
- **Email Attacks**: 63% prevention effectiveness.
- **macOS Attacks**: Concerning prevention effectiveness score of 23%.

## Performance by MITRE ATT&CK Tactic

- **Discovery**: Dropped to 29% prevention effectiveness.
- **Exfiltration**: Scored 31% in prevention effectiveness.
- **Impact**: Dropped from 42% to 37%.

## Performance by Threat Group

Sophisticated threat groups remain difficult to prevent. Examples include:
- **Gallium**: 38% prevention rate.
- **SideCopy**: 45% prevention rate.
- **Mustang Panda**: 52.18% prevention rate.
- **OilRig**: 64% prevention rate.

## Spotlight on Ransomware Attacks

The top ransomware strains with the lowest prevention effectiveness:
- **BlackByte**: 17%
- **BabLock**: 20%
- **Hive**: 30%
- **MarioLocker**: 31%
- **FAUST**: 35%

## Spotlight of Vulnerabilities

Organizations were able to prevent top vulnerability exploits only 5-16% of the time.
- **Log4Shell (CVE-2023-27524)**: 11% prevention effectiveness.
- **Zoho ManageEngine (CVE-2022-1471)**: 11% prevention effectiveness.
- **Oracle WebLogic Server (CVE-2020-14645)**: 13% prevention effectiveness.
- **Legacy vulnerabilities (e.g., CVE-2019-9947)**: 8% prevention effectiveness.

---

### Picus Security Customers Prevent Twice As Many Attacks
Picus Security provides a threat exposure management solution—the Picus Security Validation Platform. On average, customers prevent twice as many attacks within just three months.

### About Picus Security
Picus Security, the leading security validation company, provides organizations a clear picture of their cyber risk based on business context. For more information, visit [picussecurity.com](https://picussecurity.com).