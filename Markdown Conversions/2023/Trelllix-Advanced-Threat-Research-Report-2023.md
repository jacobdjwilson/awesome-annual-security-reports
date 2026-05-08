# Advanced-Threat-Research-Report: The CyberThreat Report (June 2023)

## Table of Contents
- [Introduction](#introduction)
- [Q1 2023 Highlights At-A-Glance](#q1-2023-highlights-at-a-glance)
- [Report Analysis, Insights, and Data](#report-analysis-insights-and-data)
- [Security Incidents](#security-incidents)
- [Ransomware](#ransomware)
- [Nation-State Activity](#nation-state-activity)
- [Vulnerability Intelligence](#vulnerability-intelligence)
- [Email Security](#email-security)
- [Network Security](#network-security)
- [Cloud Incidents](#cloud-incidents)
- [Methodology](#methodology)
- [Resources](#resources)
- [About Trellix Advanced Research Center & Trellix](#about-trellix-advanced-research-center--trellix)

---

## Introduction
Authored by Trellix’s Advanced Research Center, this report highlights insights, intelligence, and guidance gleaned from multiple sources of critical data on cybersecurity threats between January 1, 2023, and March 31, 2023.

### Strategic Context: An Unsettled World
Major drivers of cyber risk include:
- **Russia’s Invasion of Ukraine**: Escalation of espionage, warfare, and disinformation.
- **China’s Geopolitical Aspirations**: Assertive foreign policy and corporate espionage.
- **Developing Economies**: Rapid infrastructure expansion often lacking cybersecurity focus.
- **Global Inflation**: Pressures on cybersecurity budgets.
- **Supply Chain Disruptions**: Continued need for zero-trust capabilities.
- **MacOS Security**: The myth of Apple’s superior security persists as threat actors leverage Golang-based malware.
- **Artificial Intelligence**: Both a tool for defense and a disruption to the threat landscape.

### Cybersecurity: CISO Challenges and the SecOps Revolution
Current headwinds include outdated technology (96% of CISOs need better solutions), a sea of security tools (average of 25 per organization), alert fatigue (45% false positives), and insufficient resources.

---

## Q1 2023 Highlights At-A-Glance
- **Ransomware**: Remains the primary cyberattack type. Cuba (9%) and Play (7%) were the most prevalent families.
- **Nation-State**: China-affiliated actors (e.g., Mustang Panda) dominated, generating 79.3% of all nation-state activity.
- **Vulnerability Intelligence**: Many critical vulnerabilities were bypasses to patches for older CVEs.
- **Email Security**: Shift toward SEO poisoning, OneNote, and Zip attachments; increased use of legitimate brand names (PayPal, Google) for phishing.
- **Cloud Incidents**: Valid accounts remain the dominant attack technique.

---

## Report Analysis, Insights, and Data

### Security Incidents
Threat actors continue to exploit paths of least resistance using Windows binaries and third-party tools.
- **Top Windows Binaries**: 1. PowerShell, 2. Windows CMD, 3. Scheduled Task, 4. RunDLL32, 5. WMIC.
- **Top Third-Party Tools**: Cobalt Strike, Mimikatz, cURL, 7-Zip, and UPX.

### Ransomware
- **Top Ransomware Families**: Royal Ransom (7%), Trigona (4%), Maui (4%).
- **Targeting**: The U.S. (15%) and Turkey (14%) were the most impacted.
- **Victimology**: Mid-sized businesses (51-200 employees) are the most common targets.

### Nation-State Activity
- **Most Active Group**: Mustang Panda (72% of activity).
- **Top Malicious Tools**: PlugX (38%), Cobalt Strike (35%).
- **Top Targeted Country**: The Philippines (34% of detections).

### Vulnerability Intelligence
The report highlights the persistence of "yesterday's news," such as the resurgence of vulnerabilities like CVE-2021-21974 (VMware ESXi) and the use of primitives similar to the FORCEDENTRY exploit in Apple devices.

### Email Security
- **Top Malware**: Formbook (44%) and Agent Tesla.
- **Top Targeted Countries**: United States (30%) and South Korea (29%).
- **Evasion**: 302 Redirect-based evasion (79%) and Captcha-based attacks (46%) are the primary techniques.

### Network Security
- **Trends**: Stop ransomware activity declined by 94%, while Android malware activity increased by 12.5%.
- **Top Signatures**: Metasploit VxWorks WDB Agent Scanner Detection (111K counts).

### Cloud Incidents
- **AWS/Azure/GCP**: Valid accounts remain the primary vector for cloud infrastructure attacks.

---

## Methodology
Trellix gathers data from captive sources (telemetry from over a billion sensors) and open sources (dark web, leak sites). Data is normalized and analyzed using machine learning and human expertise to identify correlations and trends.

---

## Resources
- [Trellix Threat Report Archives](https://www.trellix.com)
- [The Mind of the CISO](https://www.trellix.com)

---

## About Trellix Advanced Research Center & Trellix
The Trellix Advanced Research Center provides intelligence and cutting-edge content to security analysts. Trellix is a global company redefining the future of cybersecurity through its open and native extended detection and response (XDR) platform, empowering over 40,000 business and government customers.

[^1]: Trellix, “2023 Report: The Mind of the CISO,” 2023.
[^2]: IDC Voice of the Analysts, 2021.
[^3]: Ponemon Institute, 2020.

![Image: Chart showing top Windows binaries used in Q1 2023]
![Image: Chart showing top third-party tools used in Q1 2023]
![Image: Chart showing top sectors targeted in Q1 2023]
![Image: Chart showing top countries targeted in Q1 2023]
![Image: Chart showing top ransomware used in Q1 2023]
![Image: Chart showing ransomware groups reporting most victims per leak sites]
![Image: Chart showing cloud incident detections by MITRE ATT&CK techniques]