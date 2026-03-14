# Blue-Report 2024

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
- [Spotlight on Vulnerabilities](#spotlight-on-vulnerabilities)

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

- **Adopt a Proactive Security Mindset**: If you haven’t already, it’s definitely time to shift from a reactive to a proactive and continuous approach to cybersecurity. This involves constantly identifying and mitigating potential threats and vulnerabilities before they can breach, infiltrate, or otherwise attack or compromise your organization.

- **Implement Continuous Threat Exposure Management (CTEM)**: Establish a comprehensive CTEM program to continually identify, prioritize, validate and fix exposures. This helps in maintaining a robust security posture even as the threat landscape continues to evolve.

- **Enhance Detection and Prevention Mechanisms**: Improve detection capabilities by optimizing the entire detection engineering pipeline, including log collection, performance, and alert mechanisms in SIEM and EDR systems. Regularly review and update detection rules to ensure they remain effective against the latest threats.

- **Strengthen Ransomware Defenses**: Implement the latest, most effective backup and recovery solutions and ensure that all endpoints have up-to-date security controls. Conduct regular simulations of ransomware attacks to test and improve the effectiveness of your response strategies.

- **Improve Endpoint Security Configuration**: Ensure that security controls on all endpoints, including macOS systems, are properly configured and that appropriate EDR tools are in place. Conduct regular audits and endpoint security assessments to identify and fix any misconfigurations.

- **Enhance Log Management and Analysis**: Address common issues in log collection and performance to improve the effectiveness of detection rules in SIEM systems. Double check proper log source consolidation and availability.

- **Prioritize Password Security**: Implement strong password policies and confirm that your password hashing methods are robust to prevent easy cracking of password hashes. Regularly audit and enforce your compliance with best practices for password security across your organization.

## Methodology

The findings in this report are based on the results of simulated attack scenarios executed by Picus Security customers from January to June 2024. The data has been anonymized and aggregated from over 136 million attack simulations. Research and analysis was completed by Picus Labs and Picus Data Science teams.

### Definitions

**Prevention Effectiveness** evaluates an organization's ability to block potential cyberattacks through its security controls. This metric is the percentage of successfully prevented attacks out of all simulated attacks executed.

**Detection Effectiveness** assesses an organization’s capability to identify potential cyber threats through its existing security controls. This report uses two key indicators:

- **Log Score**: This measures the percentage of simulated attacks where the attackers’ behavior was logged.
- **Alert Score**: This indicates the percentage of simulated attacks that generate alerts.

### Scoring Legend

| Legend | Range | Description |
| :--- | :--- | :--- |
| Optimized | 90-100% | Organizations with optimized security controls continuously monitor, refine, and update them. |
| Managed | 70-89% | Managed security controls offer a high level of protection against a wide range of threats. |
| Moderate | 40-69% | Moderate security controls provide a reasonable level of protection against various threats. |
| Basic | 20-39% | Basic security controls offer limited protection against a narrow range of threats. |
| Inadequate | 0-19% | Inadequate security controls provide almost no protection to minimal protection. |

## Overall Prevention and Detection Effectiveness Performance

This year's report highlights a complex landscape for cyberattack prevention and detection within organizations. While there was noticeable progress in some areas, other critical aspects reveal ongoing challenges.

### Prevention Effectiveness
In 2024, we observed a significant improvement in organizations' overall ability to prevent cyberattacks. The average prevention effectiveness score rose from 59% in 2023 to 69% this year.

### Detection Effectiveness
In 2024, the state of detection effectiveness among security organizations exhibited both progress and setbacks. The average log score increased from 37% to 54%. However, the alert score fell to a concerning 12%, down from 16% in 2023.

### Addressing the Gaps
More logs do not necessarily equate to more visibility or better security outcomes. While organizations have improved the data layer, detection engineering remains deficient. Organizations should adopt an "assume breach" mindset to bridge these gaps.

## Real-World Performance of Cybersecurity Products

MITRE ATT&CK® Evaluations provide a controlled environment to assess a product’s capabilities. However, real-world data shows that even best-of-breed products that score 100% in controlled settings can exhibit a wide range of prevention and detection effectiveness once deployed.

We attribute this variability to:
1. **Environmental and Configurational Differences**
2. **Context and Deployment Nuances**
3. **Dynamic Nature of Threats**

We recommend:
1. **Continuous Validation**
2. **Ongoing Fine-Tuning**

## Uncovering Critical Defensive Gaps with Automated Penetration Testing

Recent assessments utilizing the Picus Attack Path Validation (APV) have yielded critical insights. In a sobering revelation, Picus APV was able to successfully achieve domain administrator status in 24% of the tests conducted. Furthermore, in 40% of the tested environments, there was at least one instance where domain administrator access was achieved.

Picus APV incorporates the capability to crack dumped password hashes. An eye-opening 25% of the environments tested revealed that attackers were able to successfully crack these password hashes, converting them into cleartext passwords.

## Detection Rule Effectiveness

Detection rules are crucial for threat identification and response. In the analysis of common issues in detection rules, we identified several concerns:

- **Improper Log Source Consolidation**: Affecting 23% of cases.
- **Log Source Availability**: Broken Log Source (5%) and Unavailable Log Source (10%).
- **Performance-related problems**: Unfiltered Log Analysis (8%), Broad Custom Property Definition (7%), Absence of Log Source Filters (6%), Wide Time Range Parameters (5%), and Free Text Search (3%).
- **Configuration issues**: Empty Reference Set (4%).

## Performance by Industry

### Prevention Effectiveness
The Healthcare and Pharmaceuticals sector showed the most dramatic improvement, increasing from 56% in 2023 to 76% in 2024. Conversely, Government dropped significantly from 73% to 59%.

### Detection Effectiveness
The Media and Entertainment industry emerged as the leader in detection effectiveness in 2024 with an impressive log score of 85% and an alert score of 37%. Transportation and Logistics saw a decline, with log scores plummeting to 10% and alert scores to 2%.

## Performance by Region

### Prevention Effectiveness
South Asia showed the most significant improvement, rising from 44% in 2023 to 60% in 2024. Asia-Pacific (APAC) increased from 64% to 74%. North America and EMEA saw slight declines.

### Detection Effectiveness
APAC saw a considerable decline in detection capabilities, with log scores dropping from 66% to 45%. North America recorded a notable decrease, with log scores falling from 60% to 49% and alert scores plummeting from 37% to 10%.

## Performance by Attack Vector

- **Data Exfiltration**: Prevention effectiveness dropped from 18% in 2023 to 9% in 2024.
- **Endpoint Attacks**: Improved from 46% to 62%.
- **Email Attacks**: 63% prevention effectiveness.
- **Web Application Attacks**: Declined from 55% to 51%.
- **Malware Download**: 71% prevention effectiveness.
- **macOS Endpoints**: 23% prevention effectiveness.

## Performance by MITRE ATT&CK Tactic

- **Discovery**: Dropped to 29% prevention effectiveness.
- **Exfiltration**: Scored 31% in prevention effectiveness.
- **Command and Control**: Dropped to 37% from 45%.
- **Impact**: Dropped to 37% from 42%.

## Performance by Threat Group

The groups with the highest “success” rates generally were either state-linked, state-sponsored, or strongly financially motivated.
- **Gallium**: 38% prevention rate.
- **SideCopy**: 45% prevention rate.
- **Tortoiseshell**: 48% prevention rate.
- **EXOTIC LILY**: 50.52% prevention rate.
- **Red Menshen**: 50.61% prevention rate.
- **Mustang Panda**: 52.18% prevention rate.
- **MuddyWater**: 53% prevention rate.

## Spotlight on Ransomware Attacks

The top 10 ransomware strains with the lowest prevention effectiveness scores:
- **BlackByte**: 17%
- **BabLock**: 20%
- **Hive**: 30%
- **MarioLocker**: 31%
- **FAUST**: 35%
- **Mountlocker**: 38%
- **BlackKingdom**: 39%
- **LockBit**: 40%
- **AvosLocker**: 40%
- **KeRanger**: 41%

## Spotlight on Vulnerabilities

Organizations were able to prevent the ten least prevented vulnerability exploits only 5-16% of the time.
- **Log4Shell (CVE-2023-27524)**: 11%
- **Zoho ManageEngine (CVE-2022-1471)**: 11%
- **Oracle WebLogic Server (CVE-2020-14645)**: 13%
- **Python (CVE-2019-9947)**: 8%
- **Microsoft Internet Explorer (CVE-2013-1305)**: 8%
- **Microsoft Edge (CVE-2023-40404)**: 7%
- **Google Chrome (CVE-2022-1972)**: 11%
- **Jenkins (CVE-2023-41763)**: 16%

![Picus Security Platform Overview]

Picus Security provides a threat exposure management solution. On average, customers prevent twice as many attacks within just three months.

## About Picus Security

Picus Security, the leading security validation company, provides organizations a clear picture of their cyber risk based on business context. The Picus Security Validation Platform transforms security practices by correlating, prioritizing, and validating exposures across siloed findings.

For more information, visit [picussecurity.com](https://www.picussecurity.com)