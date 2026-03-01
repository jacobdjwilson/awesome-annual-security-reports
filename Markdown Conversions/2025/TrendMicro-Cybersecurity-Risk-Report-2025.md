# Trend 2025 Cyber Risk Report

**Organization:** Trend Micro  
**Report Title:** Cybersecurity-Risk-Report  
**Year:** 2025

## Table of Contents
- [Outpacing the Adversary](#outpacing-the-adversary)
- [The Cyber Risk Index](#the-cyber-risk-index)
- [Cyber Risk Index Data](#cyber-risk-index-data)
- [Risk Events and Detections](#risk-events-and-detections)
- [Home Network Security Top Events](#home-network-security-top-events)
- [Vulnerabilities, Patch, and Response Data](#vulnerabilities-patch-and-response-data)
- [External Threat Data Sections](#external-threat-data-sections)
- [From Reactive to Proactive](#from-reactive-to-proactive)
- [Endnotes](#endnotes)

## Outpacing the Adversary

The Trend 2025 Cyber Risk Report sustains our shift towards proactive security. Protecting enterprises is no longer about stopping breaches but is now about staying ahead, making cybersecurity a business enabler. This report looks at our telemetry from 2024: by looking at last year’s risk landscape, we recognize exposures and understand attacker behavior to be able to implement countermeasures for the year ahead. This way, we transform security from a challenge to a catalyst for innovation and business growth.

This report harnesses data from the Cyber Risk Exposure Management[^1] (CREM) solution of our flagship cybersecurity platform Trend Vision One™[^2]. Telemetry from this solution identifies exposures across attack surfaces to help prioritize and address risk areas. Combined with data from our native eXtended Detection and Response[^3] (XDR) tools and threat intelligence, this report primes enterprises with information on adversaries along with risk insights to reduce their Cyber Risk Index and stay ahead of the curve.

## The Cyber Risk Index

To achieve a proactive approach to cybersecurity, we capitalize on data from our Cyber Risk Exposure Management solution, which is designed to protect organizations’ digital assets from attacks by evaluating risks across the attack surface, prioritizing them, and implementing appropriate countermeasures.

CREM calculates an enterprise’s Cyber Risk Index (CRI), a metric that quantifies the overall security risk of an organization based on a consolidation of individual assets and risk factor scores. Our research[^4] has found that organizations with a CRI above the average have a greater likelihood to suffer from attacks than those with a lower CRI. Like how preventive health check-ups reveal the overall state of health, analyze risks the body might be exposed to, and creates an action plan on how to prevent these risks, CREM works to identify the CRI and creates a strategy to reduce them and therefore improve an organization’s security posture.

While risk is evaluated qualitatively, the CRI quantifies it by using a scale from 0-100 to represent and give a clearer picture of where enterprises or sectors stand in terms of security and risk.

CREM uses the risk event catalog to formulate a risk score for each asset type and an index for organizations by multiplying an asset’s attack, exposure, and security configuration by the asset criticality. The risk scores are calculated individually for every asset, with each score considering asset type and criticality. The result is an integer between zero and 100 that falls into one of three levels.

*   **Low Risk (0-30):**
    *   Organizations in this category are considered relatively secure
    *   Immediate significant measures are generally not necessary
*   **Medium Risk (31-69):**
    *   Organizations in this category have several risk factors that need to be addressed
    *   It is advisable to consider and implement appropriate countermeasures
*   **High Risk (70-100):**
    *   Organizations in this category are exposed to severe risks
    *   Prompt and robust security measures are essential to mitigate potential threats

Learn more with our Cyber Risk Index Overview[^5] and our technical report on how to understand risk score calculations[^6].

This report covers telemetry from February to December 2024; it excludes data from January as the CREM dashboard algorithm was updated at the end of that month with a weight summation method that affects CRI computation. Telemetry from February to December 2024 was computed with the same algorithm and provides a more accurate average CRI. Future improvements to CREM computation will be disclosed accordingly. Also note that industry CRI data do not include industries with a sample size too small to be statistically relevant.

## Cyber Risk Index Data

### Overall average CRI
![Chart showing the overall average CRI for 2024, trending downward from 42.5 in February to 36.3 in December.]

**Average CRI for 2024: 38.4**

| Month | CRI Score |
| :--- | :--- |
| FEB | 42.5 |
| MAR | 39.9 |
| APR | 39.2 |
| MAY | 39.3 |
| JUN | 39.0 |
| JUL | 38.4 |
| AUG | 37.6 |
| SEP | 37.3 |
| OCT | 36.7 |
| NOV | 36.9 |
| DEC | 36.3 |

The overall average CRI in 2024 improved consistently per month, with a 6.2-point difference from the overall average in February to December. While this improvement suggests that enterprises have been successfully operationalizing cyber risk management, a 36.3 overall CRI still falls within medium risk, an average indicative that organizations still have several risk factors that need addressing. This emphasizes the need for continuous monitoring of the attack surface risk life cycle, which includes discovery, assessment, and risk mitigation through necessary countermeasures.

### Regional Average CRI per month (February 2024 - December 2024)

**Regional Average CRI for 2024:**
*   **Europe:** 37.9
*   **Americas:** 39.8
*   **AMEA:** 37.9
*   **Japan:** 34.3

![Line chart showing regional CRI trends. Europe shows the most significant improvement, dropping from 43.7 in February to 36.7 in December. Japan remains the lowest risk region throughout the year.]

Our regional telemetry is consistent to the overall average CRI data. There is a general downtrend in risk indices among the regions; Europe exhibiting the biggest improvement from February to December with a 7-point difference. The region is pushing for increased cyber hygiene and resilience with the Digital Operational Resilience Act[^7] and the Cyber Resilience Act[^8], which could influence enterprises to take a more proactive approach in cybersecurity through patching, fixing configurations, and refining user access and permissions, among others.

While CRI among regions improved in the past year, each region’s risk index is still within the medium risk level: enterprises from each region still have unsecure assets that might expose the organization to threats.

### Top industries with the highest average CRI by quarter

| Industry | Feb-Mar | Apr-Jun | Jul-Sep | Oct-Dec |
| :--- | :--- | :--- | :--- | :--- |
| Agriculture | 43.9 | 43.9 | 43.7 | 42.9 |
| Communications | 43.7 | 42.3 | 41.3 | 41.6 |
| Construction | 44.5 | 45.1 | 42.6 | 43.7 |
| Education | 43.7 | 42.6 | 43.1 | 40.7 |
| Energy | 40.7 | 41.4 | 40.0 | 41.0 |
| Financial Services | 41.4 | 39.5 | 39.3 | 38.5 |
| Government and Public Services | 41.1 | 41.2 | 38.8 | 39.5 |
| Healthcare | 40.3 | 40.3 | 39.8 | 39.6 |
| Insurance | 37.9 | 39.1 | 39.4 | 39.7 |
| Transportation | 42.6 | 40.8 | 39.4 | 37.8 |

The education sector had the highest average CRI at the beginning of the year and is still among the sectors with the highest CRI by the last quarter of 2024. Enterprises and organizations in this sector are vulnerable to cyberattacks that could mean disruption of educational services, data breaches, intellectual property theft, and reputational damage.

Factors that affect the education sector’s CRI could include legacy systems with outdated hardware and software and unpatched applications. The sector’s diverse group of users who create a larger attack surface with the adoption of remote learning environments also increases the likelihood of human error that result in security misconfigurations or exposure to phishing attacks. Educational institutions, especially public ones, also grapple with limited resources that could affect how much they are able to secure their systems and networks.

Enterprises in the agriculture and construction industries also have work to do. Attack surfaces of enterprises in these sectors are more vulnerable to attacks than other industries, which could mean operational disruption. Both sectors have a strategic position in global supply chains, so the impact of successful attacks might have a ripple effect on an international scale.

The average CRI of enterprises in the agriculture and construction industries could be affected by the use of legacy systems that might not be adequately secured. The increase in use of automated machinery and IoT devices improve operations in both sectors but also introduces new vulnerabilities with the expanded attack surface. Third-party vendors and service providers can also introduce additional security risks if those parties have weak cybersecurity measures.

Other sectors involved in the supply chain, such as the energy and transportation sectors, should also shift to a more proactive risk management approach to reduce their overall exposure and make their organizations resilient to attacks.

### Average risk index by company size

| Company Size (Employees) | CRI Score |
| :--- | :--- |
| More than 10,000 | 44.2 |
| 5,001 - 10,000 | 44.0 |
| 2,001 - 5,000 | 43.9 |
| 1,001 - 2,000 | 42.3 |
| 501 - 1,000 | 39.6 |
| 101 - 500 | 35.8 |
| 1 - 100 | 31.7 |

Larger enterprises typically have more complex networks; with more employees comes a larger attack surface, and so their respective security operations centers face a more challenging task of patching vulnerabilities, maintaining proper security configurations, and securing endpoints.

But any enterprise, regardless of size, has a complex attack surface as businesses globalize and expand. Attackers thrive on this complexity, and complex defense can be an expensive — but worthy — investment. Trend Vision One simplifies defense by centralizing cyber risk exposure management, security operations, and a robust layered protection to help security operations centers predict and prevent threats, thereby accelerating proactive security outcomes. At the center of the capabilities that Vision One provides is a risk-informed approach that allows enterprises to stay ahead of threats.

## Risk Events and Detections

In this section, we look at the top detections in our telemetry on risky events, misconfigurations, Extended Detection and Response (XDR) model hits, Security Analytics Engine (SAE) and Endpoint Detection and Response (EDR) hits.

### Overall Top 10 Risky Events
1. Risky Cloud App Access
2. Stale Microsoft Entra ID Account
3. Sandbox Detected Email Threat
4. On-Premises AD Account with Weak Sign-In Security Policy - Password Expiration Disabled
5. Advanced Spam Protection - Policy Violation
6. Data Loss Prevention - Email Violation
7. Microsoft Entra ID Account with Weak Sign-In Security Policy - MFA Disabled
8. Microsoft Entra ID Account with Weak Sign-In Security Policy - Password Expiration Disabled
9. Stale On-Premises AD Account
10. On-Premises AD Account with Weak Sign-In Security Policy - Password Not Required

Risky cloud app access continues to top the most detected risky event in enterprise environments. This could be influenced by the continuing transition of organizations to cloud environments, which in turn require cloud adoption and user education, a security measure that might not yet be among companies’ priorities.

Other risky events are tied to email risk and user accounts and credential security. Risky events related to email risk include the detection of suspicious email attachments. Emails continue to be a favorite vector for cybercriminals to deliver suspicious payloads; in 2024, the Trend Vision One – Email and Collaboration Protection[^9] solution detected and blocked 57 million high-risk email threats, a 27% increase from 45 million high-risk emails detected and blocked in 2023. But email can also be a way to exfiltrate or leak data from the victim: data loss prevention violations ranked top six, which indicates that employees in enterprises are sending emails with content or attachments that contain sensitive information, financial data, or intellectual property without the proper security sensitivity settings.

### Risk Event Counts on Weak Authentication

| Event Name | Total Event Count |
| :--- | :--- |
| Microsoft Entra ID Account with Weak Sign-In Security Policy - MFA Disabled | 1,011,628,400 |
| Microsoft Entra ID Account with Weak Sign-In Security Policy - Password Expiration Disabled | 606,548,251 |
| On-Premises AD Account with Weak Sign-In Security Policy - Password Not Required | 413,916,224 |
| Microsoft Entra ID Account with Weak Sign-In Security Policy - Strong Password Disabled | 389,998,623 |

Risky events related to user accounts and credential security suggest that protecting, strengthening, and updating user passwords is not a high priority for a number of enterprises. Enterprises need to prioritize and automate mitigation of identity risk to eliminate breaches in today’s boundaryless workplace. Trend Vision One™ - Identity Security[^10] can help organizations do some spring cleaning on stale user accounts, which can be exploited by attackers, former employees, or insiders for unauthorized access to sensitive data and the enterprise’s network.

### Top Detected XDR Model Hits
1. Possible OS Credential Dumping*
2. Possible Data Encrypted for Impact*
3. Behavior Monitoring Detection for Built-in Windows Tools
4. Impair Defenses*
5. Hacking Tool Detection
6. Targeted Attack Detection
7. Remote Code Execution via HTTP
8. Possible Malicious Activity via System Services*
9. System Binary Proxy Execution*
10. Webshell Detection
*(Heuristic attribute)*

Trend XDR collects and correlates data across multiple security layers like email, endpoint, server, cloud, and network to enable faster threat detection, investigation, and response through advanced analytics and automated analysis.

From this telemetry, we extracted data on the top Security Analytics Engine (SAE) and Endpoint Detection and Response (EDR) detections, which revealed that the top hits are threats that are further along in the infection chain. While this might suggest that attackers are employing more sophisticated defense evasion techniques, enterprises should also maximize tools available to them that can provide early detection of suspicious behavior and activity within their environments. Trend Vision One™ - Endpoint Security[^11] provides broad coverage for diverse environments that gives enterprises comprehensive visibility, which enables risk mitigation.

### Overall Top Vision One Misconfigurations

| Rank | Misconfiguration | Max Risk Score |
| :--- | :--- | :--- |
| 1 | Web Reputation Settings in Trend Vision One™ - Endpoint Security Not Optimized | 69 |
| 2 | Device Control Settings in Endpoint Security Not Optimized | 65 |
| 3 | Endpoint Security Not Supported | 56 |
| 4 | Predictive Machine Learning Settings in Endpoint Security Not Optimized | 69 |
| 5 | Smart Feedback Settings in Endpoint Security Not Optimized | 65 |
| 6 | Anti-Malware Scanning Settings in Endpoint Security Not Optimized | 68 |
| 7 | Firewall Settings in Endpoint Security Not Optimized | 59 |
| 8 | Behavior Monitoring Settings in Endpoint Security Not Optimized | 69 |
| 9 | Application Control Settings in Endpoint Security Not Optimized | 59 |
| 10 | Vulnerability Protection Settings in Endpoint Security Not Optimized | 65 |

In listing the top detected misconfigurations among Trend Vision One customer environments, we also provide their corresponding maximum risk score, which shows they are on the higher end of medium-risk level. These configuration issues emphasize the need for organizations to enable advanced detection capabilities and behavior monitoring AI and ML technology to improve the ability to detect new threats. Enterprises should maximize tools that provide visibility and help eliminate blind spots with a zero-trust approach to minimize their CRI.

### Overall Top Cloud Misconfigurations
1. Non-Compliant AWS Infrastructure Configuration
2. Non-Compliant Azure Infrastructure Configuration
3. Non-Compliant Amazon S3 Infrastructure Configuration (Access Control)
4. Non-Compliant Amazon S3 Infrastructure Configuration (Common Configuration)
5. Non-Compliant Amazon S3 Infrastructure Configuration (Security Configuration)
6. Non-Compliant GCP Infrastructure Configuration
7. Non-Compliant AWS Infrastructure Configuration Revealed by Amazon Inspector Findings
8. Non-Compliant Amazon S3 Infrastructure Configuration (Amazon Macie Findings)
9. Non-Compliant Amazon S3 Infrastructure Configuration

The top detected cloud misconfigurations represent a narrower, but more recent average with data only from July to December of 2024. Our telemetry revealed common issues across various cloud platforms such as AWS, Azure, and GCP. For Non-Compliant AWS Infrastructure Configurations, potential problems could include mismanagement of Identity and Access Management (IAM) policies, security groups, and network access control lists (ACL), as well as risks from unused or excessive permissions. For Amazon S3, various non-compliance issues on access control, common configuration, and security configuration could be related to public read/write settings, overly permissive bucket policies, and lack of encryption and versioning. Enterprises using GCP might also be facing problems with IAM policies and insufficient network security configurations. Meanwhile, Amazon Inspector Findings could mean security issues in workloads and insufficient security assessments.

Regular audits and updates to IAM policies, security groups, and network access controls are essential to prevent unauthorized access. Enterprises should also avoid public access settings, implement strict bucket policies, enable server-side encryption and versioning, and review lifecycle policies and logging mechanisms. Organizations should maximize solutions that enhance visibility on their cloud environments for more effective cloud risk management. Trend Vision One™ - Cloud Security[^12] supports operational efficiency by protecting an enterprise’s cloud environment from development to deployment, and during operations.

### Risk Events and Detections by Region and by Industry (July - December 2024)

#### Europe
*   **Top Risky Event:** Risky Cloud App Access
*   **Top XDR Model Hit:** Possible Disabling of Antivirus Software
*   **Top Vision One Misconfiguration:** Application Control Settings Not Optimized
*   **Top Cloud Misconfiguration:** Non-Compliant AWS Infrastructure Configuration

#### AMEA
*   **Top Risky Event:** Risky Cloud App Access
*   **Top XDR Model Hit:** Hacking Tool Detection - Blocked
*   **Top Vision One Misconfiguration:** Web Reputation Settings Not Optimized
*   **Top Cloud Misconfiguration:** Non-Compliant AWS Infrastructure Configuration

#### Americas
*   **Top Risky Event:** Risky Cloud App Access
*   **Top XDR Model Hit:** Threat Intelligence Sweeping
*   **Top Vision One Misconfiguration:** Web Reputation Settings Not Optimized
*   **Top Cloud Misconfiguration:** Non-Compliant AWS Infrastructure Configuration

#### Agriculture Sector
*   **Top Risky Event:** Risky Cloud App Access
*   **Top XDR Model Hit:** Threat Intelligence Sweeping
*   **Top Vision One Misconfiguration:** Web Reputation Settings Not Optimized
*   **Top Cloud Misconfiguration:** Non-Compliant AWS Infrastructure Configuration

#### Communications Industry
*   **Top Risky Event:** Sandbox Detected Email Threat
*   **Top XDR Model Hit:** Possible Disabling of Antivirus Software
*   **Top Vision One Misconfiguration:** Application Control Settings Not Optimized
*   **Top Cloud Misconfiguration:** Non-Compliant AWS Infrastructure Configuration

#### Education Sector
*   **Top Risky Event:** Stale Microsoft Entra ID Account
*   **Top XDR Model Hit:** Threat Intelligence Sweeping
*   **Top Vision One Misconfiguration:** Endpoint Sensor Settings Not Optimized
*   **Top Cloud Misconfiguration:** Non-Compliant AWS Infrastructure Configuration

#### Energy Sector
*   **Top Risky Event:** Sandbox Detected Email Threat
*   **Top XDR Model Hit:** Hacking Tool Detection - Blocked
*   **Top Vision One Misconfiguration:** Behavior Monitoring Settings Not Optimized
*   **Top Cloud Misconfiguration:** Non-Compliant AWS Infrastructure Configuration

#### Insurance Industry
*   **Top Risky Event:** Risky Cloud App Access
*   **Top XDR Model Hit:** Possible Disabling of Antivirus Software
*   **Top Vision One Misconfiguration:** Anti-Malware Scanning Settings Not Optimized
*   **Top Cloud Misconfiguration:** Non-Compliant AWS Infrastructure Configuration

## Home Network Security Top Events

| Rule Name | Rule ID |
| :--- | :--- |
| RDP Brute Force Login | 1059803 |
| MISC Bitcoin/LiteCoin/Dogecoin Mining Activity -1 | 1059684 |
| WEB Hikvision Product Web Server Command Injection -1.1 (CVE-2021-36260) | 1139937 |
| TELNET Default Password Login -6 | 1133113 |
| WEB HTTP Invalid Content-Length -2 | 1139797 |
| MISC Cryptocurrency Monero Mining Activity -1 | 1134390 |
| SSH Brute Force Login | 1059418 |
| WEB Remote Command Execution via Shell Script -1.h | 1133253 |
| SMB Microsoft Windows SMB Server SMBv1 CVE-2017-0147 Information Disclosure -1 | 1133710 |
| MALWARE Suspicious IoT Worm TELNET Activity -1 | 1133148 |

Apart from our cyber risk management data, our Home Network Security shows security risks within home networks by detecting risky network events occurring in devices connected to home routers; an attack surface worth monitoring in the age of remote work across enterprises.

Our telemetry shows that attackers continue to rely on time-tested techniques to gain an initial foothold into their victim’s systems with the top detected event being brute force login. There is also a significant amount of cryptocurrency mining activity that can impact enterprises in terms of information disclosure.

The vulnerability found in Hikvision cameras[^13] (CVE-2021-36260[^14]) is notably high in the detections list; when this vulnerability is exploited, an attacker can launch a command injection attack by sending messages with malicious commands. Considering that this vulnerability has been around since 2021, enterprises should allot effort into employee cybersecurity and risk education so they can maximize tools to secure their personal and home devices. These devices can be an extension of the enterprise’s attack surface if they connect to the organization’s network.

## Vulnerabilities, Patch, and Response Data

### Top risky CVEs, most detected and unpatched

| Rank | CVE ID | NIST Severity Score |
| :--- | :--- | :--- |
| 1 | CVE-2024-21357[^15] | 8.1 High |
| 2 | CVE-2024-30086[^16] | 7.8 High |
| 3 | CVE-2024-30082[^17] | 7.8 High |
| 4 | CVE-2024-30087[^18] | 7.8 High |
| 5 | CVE-2024-35250[^19] | 7.8 High |
| 6 | CVE-2024-30091[^20] | 7.8 High |
| 7 | CVE-2024-30049[^21] | 7.8 High |
| 8 | CVE-2024-30084[^22] | 7.0 High |
| 9 | CVE-2024-30050[^23] | 5.4 Medium |
| 10 | CVE-2024-30037[^24] | 5.5 Medium |

The most detected unpatched vulnerabilities have patches released in the first half of 2024; this emphasizes the need for enterprises to continuously monitor and scan for vulnerabilities and patch as soon as possible. Most of the top detected vulnerabilities are classified as high severity being related to Elevation of Privilege (EoP), except for the most detected and unpatched among systems, which is a Remote Code Execution (RCE) vulnerability.

### Average Mean Time To Patch (MTTP) by region

| Region | Average Days to Patch |
| :--- | :--- |
| Europe | 23.5 |
| Japan | 27.5 |
| Americas | 29.2 |
| AMEA | 32.9 |

Trend CREM data on mean time to patch shows the average number of days that organizations within a certain category are able to patch vulnerabilities. Europe has the fastest average mean time to patch among regions. Japan has the second fastest MTTP, reflecting our telemetry of it having the lowest CRI in 2024.

### Average MTTP by industry

**Top Industries with the fastest average MTTP:**
1. Non-profit (19.0 days)
2. Service (19.7 days)
3. Technology (22.1 days)
4. Agriculture (23.7 days)
5. Entertainment (23.8 days)

**Top Industries with the slowest average MTTP:**
1. Healthcare (41.5 days)
2. Telecommunications (38.0 days)
3. Financial Services (35.1 days)
4. Communications (34.1 days)
5. Insurance (30.6 days)

### Average MTTP by company size

| Company Size (Employees) | Average Days to Patch |
| :--- | :--- |
| 1 – 100 | 36.6 |
| 101 – 500 | 37.3 |
| 501 – 1,000 | 41.3 |
| 1,001 – 2,000 | 28.8 |
| 2,001 – 5,000 | 22.0 |
| 5,001 – 10,000 | 29.3 |
| More than 10,000 | 22.5 |

### Overall Top Response Playbooks in Use
1. Automated Response Playbook
2. Custom
3. CVEs with Global Exploit Activity - Internal Assets
4. CVEs with High or Medium Global Exploit Activity
5. Risk Event Response
6. Account Response
7. CVEs with High or Medium Global Exploit Activity - Internet-Facing Assets
8. CVEs with Global Exploit Activity - Internet-Facing Assets
9. Account Exposure - Weak Sign-in Policies, Excessive Admin Accounts, and Stale Accounts
10. Endpoint Response

## External Threat Data Sections

### Notable uses of AI in cybercrime
*   **LLM risks[^25]:** OWASP Top 10 Risk List for LLMs includes vector weaknesses, misinformation, and unbounded consumption.
*   **Rogue AI[^26]:** Malicious rogues or subverted AI resources caused by human error or technology limitations.
*   **Improved Reconnaissance[^27]:** AI used to pull vast amounts of info to identify victims and expedite analysis of exfiltrated data.
*   **Disinformation campaigns[^28]:** Deepfake content used to shape public perceptions, ranging from social media misinformation to large-scale election interference.
*   **Pig butchering[^29] and virtual kidnapping[^30]:** Deepfake technology used in extortion schemes and voice cloning for virtual kidnapping.
*   **Intensified phishing schemes and malicious digital twins[^31]:** Generative AI produces convincing messages and scales operations through automation.

### Ransomware

**Top Ransomware Intrusion Sets (by number of breaches):**
1. RansomHub: 266
2. Akira: 249
3. Medusa: 187
4. 8Base: 176
5. Qilin: 133
6. LockBit: 119
7. Play: 106
8. Hunters International: 95
9. BianLian: 95
10. Black Basta: 92

Our leak site monitoring shows that ransomware groups have the most victim enterprises from North America, with 369 successful breaches on companies that did not pay ransom in that region. Leak sites also published 104 successful breaches from enterprises in Europe and 47 from Asia. Companies in retail, wholesale, and distribution make up most of the breaches published in leak sites (13.9%).

### Notable APT campaigns

*   **Earth Kurma (Nov 2020 - ongoing):** Targets Southeast Asia governments (Philippines, Vietnam, Malaysia, Brunei, Thailand) for espionage.
*   **Famous Chollima (Oct 2023 – ongoing):** Exploits job listings to propagate malware among developers to acquire foreign currency.
*   **KONNI Group (Oct 2024 – ongoing):** Targets Russia for diplomatic information gathering using LNK files and decoy PDFs.
*   **Earth Koshchei (Aug - Oct 2024):** Rogue RDP campaign targeting Ukrainian governments and military organizations.
*   **Pawn Storm (Aug 2024 - ongoing):** Clipboard and reCAPTCHA abuse targeting Ukrainian government organizations.
*   **Earth Dahu (Ongoing):** Abuses TryCloudFlare to target Ukrainian central and local government.
*   **Matryoshka (Sep 2023 - Nov 2024):** Disinformation campaign related to the US presidential elections.
*   **Chinese threat actor (Sep 2023 - Nov 2024):** Targeting sensitive industries (Manufacturing, Tech) in Europe and Asia using Shadowpad malware.

### Malware

**Top malware families (by detections):**
1. CoinMiner: 51,040
2. Negasteal: 45,821
3. Nemucod: 42,418
4. Prometei: 35,883
5. DownAd: 33,188
6. Bondat: 32,752
7. Powload: 32,208
8. Gamarue: 31,918
9. Dloader: 30,856
10. WebShell: 29,689

### ZDI (Zero-Day Initiative)
Trend Zero-Day Initiative is the world’s largest agnostic bug bounty program. Our ZDI monitoring shows an increase in the use of zero-day exploits by ransomware groups. Since 2020, there have been 59 zero-day exploits leveraged by ransomware attacks.

**Vulnerabilities discovered by region:**
*   Europe: 1,310
*   Japan: 258
*   Americas: 146
*   AMEA: 27

### External threat monitoring heatmap

**Top countries with the most ransomware attacks (detected and blocked):**
1. United States: 1,347,243
2. Thailand: 1,134,833
3. Turkey: 514,019
4. Taiwan: 474,488
5. Japan: 394,351

**Top countries with the most malware detections:**
1. Japan: 1,008,580,748
2. United States: 661,026,169
3. India: 193,155,280
4. Germany: 188,554,351
5. Taiwan: 176,754,704

**Top countries with the most detected email threats (originating IP):**
1. United States: 4,095,791,263
2. India: 1,030,130,818
3. France: 1,022,307,312
4. China: 947,614,419
5. Germany: 827,350,062

## From Reactive to Proactive

A risk-based approach to cybersecurity will shift an enterprise’s strategy from being reactive to proactive. By identifying the weaknesses in the defenses and by understanding how cybercriminals are using these exposures to their benefit, enterprises can take the necessary countermeasures to create a more secure defense before the inevitable next cyberattack happens.

**Recommendations:**
1. Optimize security settings to maximize product features and be alerted on misconfigurations, vulnerabilities, and other risks.
2. When a risky event is detected, contact the device and/or account owner to verify the event, and investigate using the Vision One Workbench.
3. Inventory stale accounts to delete inactive and unused ones. Disable risky accounts, reset passwords, and enable multi-factor authentication (MFA).
4. Apply the latest patches or upgrade the version of applications regularly.
5. Apply the latest patches or upgrade the operating system version regularly.

## Endnotes

[^1]: Trend Micro. (n.d.). Trend Micro. “Cyber Risk Exposure Management”. Accessed on Mar. 21, 2025, at: Link.
[^2]: Trend Micro. (n.d.). Trend Micro. “One Platform”. Accessed on Mar. 21, 2025, at: Link.
[^3]: Trend Micro. (n.d.). Trend Micro. “XDR (Extended Detection and Response)”. Accessed on Mar. 21, 2025, at: Link.
[^4]: Trend Micro. (February 10, 2025). Trend Micro. “From Vulnerable to Resilient: Cutting Ransomware Risk with Proactive Attack Surface Management”. Accessed on Mar. 21, 2025, at: Link.
[^5]: Trend Micro. (n.d.). Trend Micro. “Trend Vision One Risk Index Overview”. Accessed on Mar. 21, 2025, at: Link.
[^6]: Trend Micro. (n.d.). Trend Micro. “More Than a Number: Your Risk Score Explained”. Accessed on Mar. 21, 2025, at: Link.
[^7]: Digital Operational Resilience Act. (n.d.). Digital Operational Resilience Act. “Official Website”. Accessed on Mar. 21, 2025, at: Link.
[^8]: European Commission. (n.d.). Digital Strategy - European Commission. “Cyber Resilience Act”. Accessed on Mar. 21, 2025, at: Link.
[^9]: Trend Micro. (n.d.). Trend Micro. “Email and Collaboration Security”. Accessed on Mar. 21, 2025, at: Link.
[^10]: Trend Micro. (n.d.). Trend Micro. “Identity and Access Management”. Accessed on Mar. 21, 2025, at: Link.
[^11]: Trend Micro. (n.d.). Trend Micro. “Endpoint Security”. Accessed on Mar. 21, 2025, at: Link.
[^12]: Trend Micro. (n.d.). Trend Micro. “Hybrid Cloud Security”. Accessed on Mar. 21, 2025, at: Link.
[^13]: CISA. (Sep. 28, 2021). Cybersecurity & Infrastructure Security Agency (CISA). “RCE Vulnerability in Hikvision Cameras (CVE-2021-36260)”. Accessed on Mar. 21, 2025, at: Link.
[^14]: NIST. (Sep. 22, 2021). National Institute of Standards and Technology (NIST). “CVE-2021-36260 Detail”. Accessed on Mar. 21, 2025, at: Link.
[^15]: NIST. (Feb. 13, 2024)”. National Vulnerability Database (NVD). “CVE-2024-21357”. Accessed on Mar. 21, 2025, at: Link.
[^16]: NIST. (June 11, 2024). National Vulnerability Database (NVD). “CVE-2024-30086”. Accessed on Mar. 21, 2025, at: Link.
[^17]: NIST. (June 11, 2024). National Vulnerability Database (NVD). “CVE-2024-30082”. Accessed on Mar. 21, 2025, at: Link.
[^18]: NIST. (June 11, 2024). National Vulnerability Database (NVD). “CVE-2024-30087”. Accessed on Mar. 21, 2025, at: Link.
[^19]: NIST. (June 11, 2024). National Vulnerability Database (NVD). “CVE-2024-35250”. Accessed on Mar. 21, 2025, at: Link.
[^20]: NIST. (June 11, 2024). National Vulnerability Database (NVD). “CVE-2024-30091”. Accessed on Mar. 21, 2025, at: Link.
[^21]: NIST. (May 14, 2024). National Vulnerability Database (NVD). “CVE-2024-30049”. Accessed on Mar. 21, 2025, at: Link.
[^22]: NIST. (June 11, 2024). National Vulnerability Database (NVD). “CVE-2024-30084”. Accessed on Mar. 21, 2025, at: Link.
[^23]: NIST. (May 14, 2024). National Vulnerability Database (NVD). “CVE-2024-30050”. Accessed on Mar. 21, 2025, at: Link.
[^24]: NIST. (May 14, 2024). National Vulnerability Database (NVD). “CVE-2024-30037”. Accessed on Mar 21, 2025, at: Link.
[^25]: Gennai Security Project. (Nov. 17, 2024). Gennai Security Project. “OWASP Top 10 for LLM Applications 2025”. Accessed on Mar. 21, 2025, at: Link.
[^26]: AI Team. (Aug. 15, 2024). Trend Micro. “Rogue AI: Part 1”. Accessed on Mar. 21, 2025, at: Link.
[^27]: Nada Elrayes. (Sep. 26, 2024). Trend Micro. “Countering AI-Driven Threats with AI-Powered Defense”. Accessed on Mar. 21, 2025, at: Link.
[^28]: Trend Micro. (Sep. 19, 2024). Trend Micro. “The Illusion of Reality”. Accessed on Mar. 21, 2025, at: Link.
[^29]: Trend Micro. (n.d.). Trend Micro. “Pig Butchering Scams”. Accessed on Mar. 21, 2025, at: Link.
[^30]: Trend Micro. (n.d.). Trend Micro. “Virtual Kidnapping”. Accessed on Mar. 21, 2025, at: Link.
[^31]: Trend Micro. (n.d.). Trend Micro. “Malicious Digital Twins”. Accessed on Mar. 21, 2025, at: Link.

---

Choice: Uncovering Electoral Deceptions in the Age of AI”. Accessed on Mar. 21, 2025, at:

Link.

61

Trend 2025 Cyber Risk Report29 Trend Research. (n.d.). Trend Micro. “Unmasking Pig Butchering Scams and Protecting Your Financial Future”. Accessed on Mar. 21, 2025, at: Link.

30 Craig Gibson, Josiah Hagen. (June 28, 2023). Trend Micro. “How Cybercriminals Can Perform Virtual Kidnapping Scams Using AI Voice Cloning

Tools and ChatGPT”. Accessed on Mar. 21, 2025, at: Link.

31  Trend Micro. (Dec. 16, 2024). Trend Micro. “Trend Micro Predicts Emergence of Deepfake-Powered Malicious Digital Twins”. Accessed on Mar. 21,

2025, at: Link.

32 Trend Micro. (n.d.). Trend Micro. “Coinminer.Win32.MalXMR.Ads”. Accessed on Mar. 21, 2025, at: Link.

33 Trend Micro. (n.d.). Trend Micro. “LNK_Bondat.SM”. Accessed on Mar. 21, 2025, at: Link.

34 Trend Micro. (n.d.). Trend Micro. “Tspy_Negasteal”. Accessed on Mar. 21, 2025, at: Link.

35 Trend Micro. (n.d.). Trend Micro. “Trojan.PS1.Powload.JKP”. Accessed on Mar. 21, 2025, at: Link.

36 Trend Micro. (n.d.). Trend Micro. “JS_Nemucod.SMC”. Accessed on Mar. 21, 2025, at: Link.

37 Trend Micro. (n.d.). Trend Micro. “Worm_Gamarue.SMJA”. Accessed on Mar. 21, 2025, at: Link.

38 Trend Micro. (n.d.). Trend Micro. “Trojan.Win32.Prometei.E”. Accessed on Mar. 21, 2025, at: Link.

39 Trend Micro. (n.d.). Trend Micro. “Worm.Win32.Dloader.LGA”. Accessed on Mar. 21, 2025, at: Link.

40 Trend Micro. (n.d.).Trend Micro. “Troj_Downad.E”. Accessed on Mar. 21, 2025, at: Link.

41 Trend Micro. (n.d.). Trend Micro. “Trojan.PHP.Webshell.SBJKUC”. Accessed on Mar. 21, 2025, at: Link.

62

Trend 2025 Cyber Risk ReportTrend Micro, a global cybersecurity leader, helps make the world safe for exchanging digital information. Fueled by decades of security expertise, global threat

research, and continuous innovation, Trend’s AI-powered cybersecurity platform protects over 500,000 organizations and millions of individuals across clouds,

networks, devices, and endpoints.

Trend’s platform delivers advanced threat defense techniques, extended detection and response (XDR), attack surface management (ASM), and integration across the

IT ecosystem, including AWS, Microsoft, and Google. This enables organizations to better understand, communicate, and mitigate cyber risk.

Trend’s global threat research team delivers unparalleled intelligence and insights that power the platform and help protect organizations around the world from

hundreds of millions of threats daily.

With 7,000 employees across 70 countries, Trend is singularly focused on cybersecurity by enabling organizations to simplify their connected world. TrendMicro.com.

Trend Micro Standard Copyright Notice

Copyright ©2025 Trend Micro Incorporated. All rights reserved. Trend Micro, the Trend Micro logo, and the t-ball logo are trademarks or registered trademarks of Trend

Micro Incorporated. All other company and/or product names may be trademarks or registered trademarks of their owners. Information contained in this document is

subject to change without notice. Trend Micro, the Trend Micro logo, and the t-ball logo Reg. U.S. Pat. & Tm. Off.

For details about what personal information we collect and why, please see our Privacy Notice on our website at: trendmicro.com/privacy