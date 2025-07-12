# TREND 2025 CYBER RISK REPORT

## Table of Contents
- [Outpacing the adversary](#outpacing-the-adversary)
- [The Cyber Risk Index](#the-cyber-risk-index)
- [Cyber Risk Index Data](#cyber-risk-index-data)
  - [Overall average CRI](#overall-average-cri)
  - [Regional Average CRI per month](#regional-average-cri-per-month)
  - [Top industries with the highest average CRI by quarter](#top-industries-with-the-highest-average-cri-by-quarter)
  - [Average risk index by company size](#average-risk-index-by-company-size)
- [Risk Events and Detections](#risk-events-and-detections)
  - [Overall Top 10 Risky Events](#overall-top-10-risky-events)
  - [Risk Event Counts on Weak Authentication](#risk-event-counts-on-weak-authentication)
  - [Top Detected XDR Model Hits](#top-detected-xdr-model-hits)
  - [Overall Top Vision One Misconfigurations](#overall-top-vision-one-misconfigurations)
  - [Overall Top Cloud Misconfigurations](#overall-top-cloud-misconfigurations)
  - [Risk Events and Detections by Region and by Industry](#risk-events-and-detections-by-region-and-by-industry)
    - [Europe](#europe)
    - [AMEA](#amea)
    - [Americas](#americas)
    - [Agriculture sector](#agriculture-sector)
    - [Communications industry](#communications-industry)
    - [Education sector](#education-sector)
    - [Energy sector](#energy-sector)
    - [Insurance industry](#insurance-industry)
  - [Home Network Security Top Events](#home-network-security-top-events)
- [Vulnerabilities, Patch, and Response Data](#vulnerabilities-patch-and-response-data)
  - [Top risky CVEs, most detected and unpatched](#top-risky-cves-most-detected-and-unpatched)
  - [Average Mean Time To Patch (MTTP) by region](#average-mean-time-to-patch-mttp-by-region)
  - [Average MTTP by industry](#average-mttp-by-industry)
  - [Average MTTP by company size](#average-mttp-by-company-size)
  - [Overall Top Response Playbooks in Use](#overall-top-response-playbooks-in-use)
- [External Threat Data Sections](#external-threat-data-sections)
  - [Notable uses of AI in cybercrime](#notable-uses-of-ai-in-cybercrime)
  - [Ransomware](#ransomware)
    - [Top Ransomware Intrusion Sets](#top-ransomware-intrusion-sets)
  - [Notable APT campaigns](#notable-apt-campaigns)
    - [Earth Kurma targets Southeast Asia governments](#earth-kurma-targets-southeast-asia-governments)
    - [Famous Chollima exploits job listings to propagate malware](#famous-chollima-exploits-job-listings-to-propagate-malware)
    - [Attacks targeting Russia potentially by KONNI Group](#attacks-targeting-russia-potentially-by-konni-group)
    - [Earth Koshchei’s rogue RDP campaign](#earth-koshcheis-rogue-rdp-campaign)
    - [Clipboard and reCAPTCHA abuse attributed to Pawn Storm](#clipboard-and-recaptcha-abuse-attributed-to-pawn-storm)
    - [Earth Dahu abuses TryCloudFlare](#earth-dahu-abuses-trycloudflare)
    - [Matyoshka campaign related to the US presidential elections](#matyoshka-campaign-related-to-the-us-presidential-elections)
    - [Chinese threat actor targeting sensitive industries](#chinese-threat-actor-targeting-sensitive-industries)
  - [Malware](#malware)
    - [Top malware families](#top-malware-families)
  - [ZDI](#zdi)
    - [Total vulnerabilities and monthly breakdown](#total-vulnerabilities-and-monthly-breakdown)
  - [External threat monitoring heatmap](#external-threat-monitoring-heatmap)
    - [Top countries with the most ransomware attacks](#top-countries-with-the-most-ransomware-attacks)
    - [Top countries with the most malware detections](#top-countries-with-the-most-malware-detections)
    - [Top countries with the most detected email threats](#top-countries-with-the-most-detected-email-threats)
- [From Reactive to Proactive](#from-reactive-to-proactive)
- [Endnotes](#endnotes)

## Outpacing the adversary

The Trend 2025 Cyber Risk Report sustains our shift towards proactive security. Protecting enterprises is no longer about stopping breaches but is now about staying ahead, making cybersecurity a business enabler.

This report looks at our telemetry from 2024: by looking at last year’s risk landscape, we recognize exposures and understand attacker behavior to be able to implement countermeasures for the year ahead. This way, we transform security from a challenge to a catalyst for innovation and business growth.

This report harnesses data from the Cyber Risk Exposure Management[^1] (CREM) solution of our flagship cybersecurity platform Trend Vision One™[^2]. Telemetry from this solution identifies exposures across attack surfaces to help prioritize and address risk areas. Combined with data from our native eXtended Detection and Response[^3] (XDR) tools and threat intelligence, this report primes enterprises with information on adversaries along with risk insights to reduce their Cyber Risk Index and stay ahead of the curve.

## The Cyber Risk Index

To achieve a proactive approach to cybersecurity, we capitalize on data from our Cyber Risk Exposure Management solution, which is designed to protect organizations’ digital assets from attacks by evaluating risks across the attack surface, prioritizing them, and implementing appropriate countermeasures.

CREM calculates an enterprise’s Cyber Risk Index (CRI), a metric that quantifies the overall security risk of an organization based on a consolidation of individual assets and risk factor scores. Our research[^4] has found that organizations with a CRI above the average have a greater likelihood to suffer from attacks than those with a lower CRI. Like how preventive health check-ups reveal the overall state of health, analyze risks the body might be exposed to, and creates an action plan on how to prevent these risks, CREM works to identify the CRI and creates a strategy to reduce them and therefore improve an organization’s security posture.

While risk is evaluated qualitatively, the CRI quantifies it by using a scale from 0-100 to represent and give a clearer picture of where enterprises or sectors stand in terms of security and risk.

CREM uses the risk event catalog to formulate a risk score for each asset type and an index for organizations by multiplying an asset’s attack, exposure, and security configuration by the asset criticality. The risk scores are calculated individually for every asset, with each score considering asset type and criticality. The result is an integer between zero and 100 that falls into one of three levels.

*   Low Risk (0-30):
    *   Organizations in this category are considered relatively secure
    *   Immediate significant measures are generally not necessary

4
Trend 2025 Cyber Risk Report

*   Medium Risk (31-69):
    *   Organizations in this category have several risk factors that need to be addressed
    *   It is advisable to consider and implement appropriate countermeasures

*   High Risk (70-100):
    *   Organizations in this category are exposed to severe risks
    *   Prompt and robust security measures are essential to mitigate potential threats

Learn more with our Cyber Risk Index Overview[^5] and our technical report on how to understand risk score calculations[^6].

This report covers telemetry from February to December 2024; it excludes data from January as the CREM dashboard algorithm was updated at the end of that month with a weight summation method that affects CRI computation. Telemetry from February to December 2024 was computed with the same algorithm and provides a more accurate average CRI. Future improvements to CREM computation will be disclosed accordingly. Also note that industry CRI data do not include industries with a sample size too small to be statistically relevant.

5
Trend 2025 Cyber Risk Report

## Cyber Risk Index Data

### Overall average CRI

![Bar chart showing the overall average Cyber Risk Index (CRI) per month from February to December 2024. The CRI starts at 42.5 in February and generally decreases to 36.3 in December. The average CRI for 2024 is noted as 38.4.]

(February 2024 - December 2024)

The overall average CRI in 2024 improved consistently per month, with a 6.2-point difference from the overall average in February to December. While this improvement suggests that enterprises have been successfully operationalizing cyber risk management, a 36.3 overall CRI still falls within medium risk, an average indicative that organizations still have several risk factors that need addressing. This emphasizes the need for continuous monitoring of the attack surface risk life cycle, which includes discovery, assessment, and risk mitigation through necessary countermeasures.

7
Trend 2025 Cyber Risk Report

### Regional Average CRI per month

(February 2024 - December 2024)

![Line chart showing the average Cyber Risk Index (CRI) per month for four regions: Americas, Europe, AMEA, and Japan, from February to December 2024. All regions show a general downward trend in CRI over the period. Regional average CRIs for 2024 are listed: Europe: 37.9, Americas: 39.8, AMEA: 37.9, Japan: 34.3.]

(February 2024 - December 2024)

Our regional telemetry is consistent to the overall average CRI data. There is a general downtrend in risk indices among the regions; Europe exhibiting the biggest improvement from February to December with a 7-point difference. The region is pushing for increased cyber hygiene and resilience with the Digital Operational Resilience Act[^7] and the Cyber Resilience Act[^8], which could influence enterprises to take a more proactive approach in cybersecurity through patching, fixing configurations, and refining user access and permissions, among others.

While CRI among regions improved in the past year, each region’s risk index is still within the medium risk level: enterprises from each region still have unsecure assets that might expose the organization to threats.

8
Trend 2025 Cyber Risk Report

### Top industries with the highest average CRI by quarter

(February 2024 - December 2024)

![Bar chart showing the average Cyber Risk Index (CRI) for various industries across four quarters: Feb-Mar, Apr-Jun, Jul-Sep, and Oct-Dec 2024. Industries listed include Agriculture, Communications, Construction, Education, Energy, Financial Services, Government and Public Services, Healthcare, Insurance, and Transportation. The chart highlights which industries had the highest CRI in each quarter and overall for 2024.]

(February 2024 - December 2024)

The education sector had the highest average CRI at the beginning of the year and is still among the sectors with the highest CRI by the last quarter of 2024. Enterprises and organizations in this sector are vulnerable to cyberattacks that could mean disruption of educational services, data breaches, intellectual property theft, and reputational damage.

9
Trend 2025 Cyber Risk Report

Factors that affect the education sector’s CRI could include legacy systems with outdated hardware and software and unpatched applications. The sector’s diverse group of users who create a larger attack surface with the adoption of remote learning environments also increases the likelihood of human error that result in security misconfigurations or exposure to phishing attacks. Educational institutions, especially public ones, also grapple with limited resources that could affect how much they are able to secure their systems and networks.

Enterprises in the agriculture and construction industries also have work to do. Attack surfaces of enterprises in these sectors are more vulnerable to attacks than other industries, which could mean operational disruption. Both sectors have a strategic position in global supply chains, so the impact of successful attacks might have a ripple effect on an international scale.

The average CRI of enterprises in the agriculture and construction industries could be affected by the use of legacy systems that might not be adequately secured. The increase in use of automated machinery and IoT devices improve operations in both sectors but also introduces new vulnerabilities with the expanded attack surface. Third-party vendors and service providers can also introduce additional security risks if those parties have weak cybersecurity measures.

Other sectors involved in the supply chain, such as the energy and transportation sectors, should also shift to a more proactive risk management approach to reduce their overall exposure and make their organizations resilient to attacks.

10
Trend 2025 Cyber Risk Report

### Average risk index by company size

![Bar chart showing the average Cyber Risk Index (CRI) by company size (number of employees) from February to December 2024. The chart shows that larger companies tend to have higher average CRIs: 1-100 employees (31.7), 101-500 (35.8), 501-1,000 (39.6), 1,001-2,000 (42.3), 2,001-5,000 (43.9), 5,001-10,000 (44.0), More than 10,000 (44.2).]

Larger enterprises typically have more complex networks; with more employees comes a larger attack surface, and so their respective security operations centers face a more challenging task of patching vulnerabilities, maintaining proper security configurations, and securing endpoints.

But any enterprise, regardless of size, has a complex attack surface as businesses globalize and expand. Attackers thrive on this complexity, and complex defense can be an expensive — but worthy — investment. Trend Vision One simplifies defense by centralizing cyber risk exposure management, security operations, and a robust layered protection to help security operations centers predict and prevent threats, thereby accelerating proactive security outcomes. At the center of the capabilities that Vision One provides is a risk-informed approach that allows enterprises to stay ahead of threats.

(February 2024 - December 2024)

11
Trend 2025 Cyber Risk Report

## Risk Events and Detections

In this section, we look at the top detections in our telemetry on risky events, misconfigurations, Extended Detection and Response (XDR) model hits, Security Analytics Engine (SAE) and Endpoint Detection and Response (EDR) hits.

We first present the overall top detections for each category, followed by a breakdown by region and by industry of the top detections that contribute to their corresponding CRI. Overall averages show a 2024 view of risk events and detections. In breaking down the top risk events and detections by region and by industry, we provide a narrower and more recent overview by presenting data from July to December 2024.

It is important to note, however, that the average data presented does not comprise the whole equation that results in each CRI; enterprises belonging to each region and industry are still recommended to do a thorough scan of their systems. With Trend Vision One, SOCs can more easily view a comprehensive breakdown of risk factors that contribute to their specific enterprise’s CRI. The platform also helps prioritize which issues need attention, focus resources on critical risks, rank issues based on critical impact, and provide clear actionable guidance so security teams can focus on what matters most, in the context of their organization.

### Overall Top 10 Risky Events

1.  Risky Cloud App Access
2.  Stale Microsoft Entra ID Account
3.  Sandbox Detected Email Threat
4.  On-Premises AD Account with Weak Sign-In Security Policy - Password Expiration Disabled
5.  Advanced Spam Protection - Policy Violation

13
Trend 2025 Cyber Risk Report

### Overall Top 10 Risky Events

6.  Data Loss Prevention - Email Violation
7.  Microsoft Entra ID Account with Weak Sign-In Security Policy - MFA Disabled
8.  Microsoft Entra ID Account with Weak Sign-In Security Policy - Password Expiration Disabled
9.  Stale On-Premises AD Account
10. On-Premises AD Account with Weak Sign-In Security Policy - Password Not Required

(Sorted by most detections, February 2024 - December 2024)

Risky cloud app access continues to top the most detected risky event in enterprise environments. This could be influenced by the continuing transition of organizations to cloud environments, which in turn require cloud adoption and user education, a security measure that might not yet be among companies’ priorities.

Other risky events are tied to email risk and user accounts and credential security. Risky events related to email risk include the detection of suspicious email attachments. Emails continue to be a favorite vector for cybercriminals to deliver suspicious payloads; in 2024, the Trend Vision One – Email and Collaboration Protection[^9] solution detected and blocked 57 million high-risk email threats, a 27% increase from 45 million high-risk emails detected and blocked in 2023. But email can also be a way to exfiltrate or leak data from the victim: data loss prevention violations ranked top six, which indicates that employees in enterprises are sending emails with content or attachments that contain sensitive information, financial data, or intellectual property without the proper security sensitivity settings.

14
Trend 2025 Cyber Risk Report

### Risk Event Counts on Weak Authentication

|                                                                            | Total Event Count   |
| :------------------------------------------------------------------------- | :------------------ |
| Microsoft Entra ID Account with Weak Sign-In Security Policy - MFA Disabled | 1,011,628,400       |
| Microsoft Entra ID Account with Weak Sign-In Security Policy - Password Expiration Disabled | 606,548,251       |
| On-Premises AD Account with Weak Sign-In Security Policy - Password Not Required | 413,916,224       |
| Microsoft Entra ID Account with Weak Sign-In Security Policy - Strong Password Disabled | 389,998,623       |

Risky events related to user accounts and credential security suggest that protecting, strengthening, and updating user passwords is not a high priority for a number of enterprises. Enterprises need to prioritize and automate mitigation of identity risk to eliminate breaches in today’s boundaryless workplace. Trend Vision One™ - Identity Security[^10] can help organizations do some spring cleaning on stale user accounts, which can be exploited by attackers, former employees, or insiders for unauthorized access to sensitive data and the enterprise’s network.

### Top Detected XDR Model Hits

1.  Possible OS Credential Dumping\*
2.  Possible Data Encrypted for Impact\*
3.  Behavior Monitoring Detection for Built-in Windows Tools
4.  Impair Defenses\*
5.  Hacking Tool Detection

15
Trend 2025 Cyber Risk Report

### Top Detected XDR Model Hits

6.  Targeted Attack Detection
7.  Remote Code Execution via HTTP
8.  Possible Malicious Activity via System Services\*
9.  System Binary Proxy Execution\*
10. Webshell Detection

(Sorted by most detections, February 2024 - December 2024)

\*Heuristic attribute

Trend XDR collects and correlates data across multiple security layers like email, endpoint, server, cloud, and network to enable faster threat detection, investigation, and response through advanced analytics and automated analysis.

From this telemetry, we extracted data on the top Security Analytics Engine (SAE) and Endpoint Detection and Response (EDR) detections, which revealed that the top hits are threats that are further along in the infection chain. While this might suggest that attackers are employing more sophisticated defense evasion techniques, enterprises should also maximize tools available to them that can provide early detection of suspicious behavior and activity within their environments. Trend Vision One™ - Endpoint Security[^11] provides broad coverage for diverse environments that gives enterprises comprehensive visibility, which enables risk mitigation.

16
Trend 2025 Cyber Risk Report

### Overall Top Vision One Misconfigurations

|                                                                           | Maximum Risk Score |
| :------------------------------------------------------------------------ | :----------------- |
| 1. Web Reputation Settings in Trend Vision One™ - Endpoint Security Not Optimized | 69                 |
| 2. Device Control Settings in Endpoint Security Not Optimized             | 65                 |
| 3. Endpoint Security Not Supported                                        | 56                 |
| 4. Predictive Machine Learning Settings in Endpoint Security Not Optimized | 69                 |
| 5. Smart Feedback Settings in Endpoint Security Not Optimized             | 65                 |
| 6. Anti-Malware Scanning Settings in Endpoint Security Not Optimized      | 68                 |
| 7. Firewall Settings in Endpoint Security Not Optimized                   | 59                 |
| 8. Behavior Monitoring Settings in Endpoint Security Not Optimized        | 69                 |
| 9. Application Control Settings in Endpoint Security Not Optimized        | 59                 |
| 10. Vulnerability Protection Settings in Endpoint Security Not Optimized  | 65                 |

(Sorted by most detections, July 2024 - December 2024)

In listing the top detected misconfigurations among Trend Vision One customer environments, we also provide their corresponding maximum risk score, which shows they are on the higher end of medium-risk level. These configuration issues emphasize the need for organizations to enable advanced detection capabilities and behavior monitoring AI and ML technology to improve the ability to detect new threats. Enterprises should maximize tools that provide visibility and help eliminate blind spots with a zero-trust approach to minimize their CRI.

17
Trend 2025 Cyber Risk Report

### Overall Top Cloud Misconfigurations

1.  Non-Compliant AWS Infrastructure Configuration
2.  Non-Compliant Azure Infrastructure Configuration
3.  Non-Compliant Amazon S3 Infrastructure Configuration (Access Control)
4.  Non-Compliant Amazon S3 Infrastructure Configuration (Common Configuration)
5.  Non-Compliant Amazon S3 Infrastructure Configuration (Security Configuration)
6.  Non-Compliant GCP Infrastructure Configuration
7.  Non-Compliant AWS Infrastructure Configuration Revealed by Amazon Inspector Findings
8.  Non-Compliant Amazon S3 Infrastructure Configuration (Amazon Macie Findings)
9.  Non-Compliant Amazon S3 Infrastructure Configuration

(Sorted by most detections, July 2024 - December 2024)

The top detected cloud misconfigurations represent a narrower, but more recent average with data only from July to December of 2024. Our telemetry revealed common issues across various cloud platforms such as AWS, Azure, and GCP. For Non-Compliant AWS Infrastructure Configurations, potential problems could include mismanagement of Identity and Access Management (IAM) policies, security groups, and network access control lists (ACL), as well as risks from unused or excessive permissions. For Amazon S3, various

18
Trend 2025 Cyber Risk Report

non-compliance issues on access control, common configuration, and security configuration could be related to public read/write settings, overly permissive bucket policies, and lack of encryption and versioning. Enterprises using GCP might also be facing problems with IAM policies and insufficient network security configurations. Meanwhile, Amazon Inspector Findings could mean security issues in workloads and insufficient security assessments.

Regular audits and updates to IAM policies, security groups, and network access controls are essential to prevent unauthorized access. Enterprises should also avoid public access settings, implement strict bucket policies, enable server-side encryption and versioning, and review lifecycle policies and logging mechanisms. Organizations should maximize solutions that enhance visibility on their cloud environments for more effective cloud risk management. Trend Vision One™ - Cloud Security[^12] supports operational efficiency by protecting an enterprise’s cloud environment from development to deployment, and during operations.

### Risk Events and Detections by Region and by Industry

In breaking down the top risk events and detections, we provide a more recent overview by presenting data from July to December 2024. The following section lists the most detected risky events, XDR model hits, and Vision One misconfigurations from Europe, AMEA, the Americas, and the top five industries with the highest trending average CRI.

19
Trend 2025 Cyber Risk Report

#### Europe

|    | Top Risky Events in Europe                                                              | Top XDR Model Hits in Europe                                     | Top Vision One misconfigurations in Europe                                                              | Top Cloud Misconfigurations in Europe                                                              |
| :- | :-------------------------------------------------------------------------------------- | :--------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------- |
| 1  | Risky Cloud App Access                                                                  | Possible Disabling of Antivirus Software                         | Application Control Settings in Trend Vision One™ - Endpoint Security Not Optimized                     | Non-Compliant AWS Infrastructure Configuration                                                     |
| 2  | Sandbox Detected Email Threat                                                           | Hacking Tool Detection - Blocked                                 | Device Control Settings in Endpoint Security Not Optimized                                              | Non-Compliant Azure Infrastructure Configuration                                                   |
| 3  | Stale Microsoft Entra ID Account                                                        | Threat Intelligence Sweeping                                     | File Integrity Monitoring (FIM) Settings in Endpoint Security Not Optimized                             | Non-Compliant Amazon S3 Infrastructure Configuration (Access Control)                              |
| 4  | Advanced Spam Protection - Policy Violation                                             | Possible Spear Phishing Attack via Link                          | Log Inspection Settings in Endpoint Security Not Optimized                                              | Non-Compliant Amazon S3 Infrastructure Configuration (Common Configuration)                        |
| 5  | On-Premises AD Account with Weak Sign-In Security Policy - Password Expiration Disabled | Suspicious Multiple Failed Logons via Windows Event              | Firewall Settings in Endpoint Security Not Optimized                                                    | Non-Compliant Amazon S3 Infrastructure Configuration (Security Configuration)                      |

20
Trend 2025 Cyber Risk Report

#### AMEA

|    | Top Risky Events in AMEA                                                              | Top XDR Model Hits in AMEA                                                              | Top Vision One misconfigurations in AMEA                                                              | Top Cloud Misconfigurations in AMEA                                                              |
| :- | :------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| 1  | Risky Cloud App Access                                                                | Hacking Tool Detection - Blocked                                                        | Web Reputation Settings in Trend Vision One™ - Endpoint Security Not Optimized                        | Non-Compliant AWS Infrastructure Configuration                                                   |
| 2  | Stale Microsoft Entra ID Account                                                      | Possible Disabling of Antivirus Software                                                | Device Control Settings in Endpoint Security Not Optimized                                            | Non-Compliant Amazon S3 Infrastructure Configuration (Access Control)                            |
| 3  | Sandbox Detected Email Threat                                                         | Threat Intelligence Sweeping                                                            | Behavior Monitoring Settings in Endpoint Security Not Optimized                                       | Non-Compliant Azure Infrastructure Configuration                                                 |
| 4  | Microsoft Entra ID Account with Weak Sign-In Security Policy - MFA Disabled           | [Heuristic Attribute] Backdoor File Detection                                           | Predictive Machine Learning Settings in Endpoint Security Not Optimized                               | Non-Compliant Amazon S3 Infrastructure Configuration (Common Configuration)                      |
| 5  | Data Loss Prevention - Email Violation                                                | Unknown Threat Detection and Mitigation via Predictive Machine Learning                 | Endpoint Security Agent Not Supported                                                                 | Non-Compliant Amazon S3 Infrastructure Configuration (Security Configuration)                      |

21
Trend 2025 Cyber Risk Report

#### Americas

|    | Top Risky Events in Americas                                                              | Top XDR Model Hits in Americas                                                          | Top Vision One misconfigurations in Americas                                                              | Top Cloud Misconfigurations in Americas                                                              |
| :- | :---------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------- |
| 1  | Risky Cloud App Access                                                                    | Threat Intelligence Sweeping                                                            | Web Reputation Settings in Trend Vision One™ - Endpoint Security Not Optimized                          | Non-Compliant AWS Infrastructure Configuration                                                     |
| 2  | Stale Microsoft Entra ID Account                                                          | Possible Disabling of Antivirus Software                                                | Endpoint Security Agent Not Supported                                                                     | Non-Compliant Azure Infrastructure Configuration                                                   |
| 3  | Sandbox Detected Email Threat                                                             | Hacking Tool Detection - Blocked                                                        | Device Control Settings in Endpoint Security Not Optimized                                                | Non-Compliant Amazon S3 Infrastructure Configuration (Access Control)                              |
| 4  | Microsoft Entra ID Account with Weak Sign-In Security Policy - Password Expiration Disabled | Unknown Threat Detection and Mitigation via Predictive Machine Learning                 | Predictive Machine Learning Settings in Endpoint Security Not Optimized                                   | Non-Compliant Amazon S3 Infrastructure Configuration (Common Configuration)                      |
| 5  | Advanced Spam Protection - Policy Violation                                               | Possible Spear Phishing Attack via Link                                                 | Smart Feedback Settings in Endpoint Security Not Optimized                                                | Non-Compliant Amazon S3 Infrastructure Configuration (Security Configuration)                      |

22
Trend 2025 Cyber Risk Report

#### Agriculture sector

|    | Top Risky Events in the Agriculture sector                                                | Top XDR Model Hits in the Agriculture Sector                                            | Top Vision One misconfigurations in the Agriculture Sector                                                              | Top Cloud Misconfigurations in the Agriculture Sector                                                              |
| :- | :---------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| 1  | Risky Cloud App Access                                                                    | Threat Intelligence Sweeping                                                            | Web Reputation Settings in Trend Vision One™ - Endpoint Security Not Optimized                                          | Non-Compliant AWS Infrastructure Configuration                                                                     |
| 2  | Data Loss Prevention - Email Violation                                                    | Hacking Tool Detection - Blocked                                                        | Intrusion Prevention System (IPS) Settings in Endpoint Security Not Optimized                                           | Non-Compliant Azure Infrastructure Configuration                                                                   |
| 3  | Advanced Spam Protection - Policy Violation                                               | Cybercrime Malware Mitigation                                                           | Anti-Malware Settings in Endpoint Security Not Optimized                                                                | Non-Compliant Amazon