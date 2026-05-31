# Networks-OT-IoT-Security-Report 2025

## Table of Contents
- [Executive Overview](#1-executive-overview)
- [Introduction](#2-introduction)
- [Threat Intelligence: Understanding Regional and Industry Risk Exposure](#3-threat-intelligence-understanding-regional-and-industry-risk-exposure)
  - [3.1 Industry Insights](#31-industry-insights)
  - [3.2 Regional Insights](#32-regional-insights)
- [Is Your Wireless Network Clean? A Security Hygiene Audit](#4-is-your-wireless-network-clean-a-security-hygiene-audit)
  - [4.1 The Unseen Risks of Industrial Wireless Environments](#41-the-unseen-risks-of-industrial-wireless-environments)
  - [4.2 Common Threats Targeting Wireless Networks](#42-common-threats-targeting-wireless-networks)
  - [4.3 Unprotected Wireless Networks Are Vulnerable to Deauthentication](#43-unprotected-wireless-networks-are-vulnerable-to-deauthentication)
  - [4.4 Wireless Network Managed Frame Protection Status](#44-wireless-network-managed-frame-protection-status)
  - [4.5 Protecting Critical Infrastructure for Operational Continuity](#45-protecting-critical-infrastructure-for-operational-continuity)
- [Navigating Device Vulnerability Trends: Key Stats for Security Strategy](#5-navigating-device-vulnerability-trends-key-stats-for-security-strategy)
  - [5.1 Number of CVEs Released by Sector](#51-number-of-cves-released-by-sector)
  - [5.2 Number of CWEs Associated with CVEs](#52-number-of-cwes-associated-with-cves)
  - [5.3 Risk Score Statistics](#53-risk-score-statistics)
- [The Botnet Epidemic: Statistics, Threats, and Defenses](#6-the-botnet-epidemic-statistics-threats-and-defenses)
  - [6.1 Attack Source Locations](#61-attack-source-locations)
  - [6.2 Number of Unique Daily Attacker IPs](#62-number-of-unique-daily-attacker-ips)
  - [6.3 Top Credentials Used](#63-top-credentials-used)
  - [6.4 Top Executed Commands](#64-top-executed-commands)
  - [6.5 Top Payload File Types](#65-top-payload-file-types)
  - [6.6 Top Payload Packers](#66-top-payload-packers)
- [Insights Into the Latest OT Malware](#7-insights-into-the-latest-ot-malware)
  - [7.1 BUSTLEBERM aka FrostyGoop](#71-bustleberm-aka-frostygoop)
  - [7.2 OrpaCrab aka IOCONTROL](#72-orpacrab-aka-iocontrol)
  - [7.3 Ransomware in OT](#73-ransomware-in-ot)
- [Recommendations](#8-recommendations)
  - [8.1 Implement a risk reduction strategy](#81-implement-a-risk-reduction-strategy)
  - [8.2 Prioritize anomaly detection and response](#82-prioritize-anomaly-detection-and-response)
  - [8.3 Adopt regional and industry-specific threat intelligence](#83-adopt-regional-and-industry-specific-threat-intelligence)
  - [8.4 Strengthen wireless network security with regular audits](#84-strengthen-wireless-network-security-with-regular-audits)
  - [8.5 Enhance vulnerability management with key metrics](#85-enhance-vulnerability-management-with-key-metrics)
  - [8.6 Fortify defenses against botnet attacks](#86-fortify-defenses-against-botnet-attacks)
  - [8.7 Work with your partners](#87-work-with-your-partners)

---

## 1. Executive Overview

Cyberattacks on the world’s critical infrastructure are on the rise. Global tensions continue to escalate, ransomware operators act with impunity, geopolitical conflict rises, cyber-espionage persists, and cyber has become an integral part of military strategies. The systems we design and defend must not only withstand a barrage of threats in today’s multipolar world but also balance the need to operate safely at scale, where human lives are at stake.

Multi-year adversarial operations such as Volt Typhoon and Salt Typhoon have recently been exposed, highlighting how nation-state actors have infiltrated critical infrastructure and communications systems, often remaining undetected for years.

The Nozomi Networks Labs team delivers this semi-annual report to provide insights into how the world’s largest industrial organizations and critical infrastructure operators can protect themselves from these advanced threats. Leveraging a network of more than 50,000 global honeypots, wireless monitoring sensors, inbound telemetry, partnerships, threat intelligence and other resources, our team uncovers trends, novel attack methods and unique insights that are critical for safeguarding operational technology (OT) and cyber-physical systems.

While cybersecurity reports often focus on threats targeting wired networks—such as Ethernet, industrial Ethernet and fiber—our capabilities extend beyond wired networks to encompass a multitude of wireless transport protocols. This expanded visibility enables our research team to access insights that are otherwise unavailable. Threats do not solely reside in Wi-Fi access points; wireless protocols like ZigBee, Bluetooth, LoRaWAN and others are heavily relied upon in industrial environments including power grids, transportation systems, security devices and medical equipment. Alarmingly, our findings reveal that 94% of Wi-Fi networks lack sufficient protections against deauthentication attacks, which are frequently leveraged as part of larger incidents. These vulnerabilities expose organizations to risks such as credential theft, traffic interception, man-in-the-middle attacks and spoofing, any of which could compromise the integrity of critical control systems.

![Infographic showing 94% of Wi-Fi networks lack protection against deauthentication attacks]

For example, manufacturing was the most targeted sector during the reporting period, and the U.S. was the most attacked country, up from #5 during the first half of 2024. Together these findings signal that U.S. manufacturers should increase their vigilance, as they are regularly targeted by ransomware and espionage campaigns.

In addition to reviewing the key threats from second half of 2024 such as malware, botnets and vulnerabilities, the report also delivers clear recommendations for how to navigate these emerging risks in the coming year. By understanding these evolving threats and leveraging actionable insights, we can defend our critical systems to ensure resilience, safety and operational continuity in an increasingly uncertain world.

---

## 2. Introduction

In this report we analyze unique telemetry from hundreds of real OT and IoT environments to provide a comprehensive overview of the dynamic threat landscape in the second half of 2024. The report breaks out our findings by region and industry to help you fine-tune your defense strategies.

Because wireless network security has emerged as a critical factor in maintaining operational continuity, our latest research includes a special section that examines the hidden risks of industrial wireless environments, including threats such as deauthentication attacks, which can compromise critical systems and processes. The results of a special security hygiene audit reveal common vulnerabilities and underscore why monitoring wireless networks is vital for protecting infrastructure.

We also explore broader trends in ICS asset vulnerability advisories, presenting key statistics on the top affected sectors and Common Weakness Enumerations (CWEs). We assess the current impact of botnet activity on IoT systems and provide guidance for protecting against this persistent threat.

Finally, we dig into recent OT malware attack patterns — including new families such as BUSTLEBERM (also known as FrostyGoop) and OrpaCrab (also known as IOCONTROL) to give you the insights you need to keep your OT and IoT environments safe.

---

## 3. Threat Intelligence: Understanding Regional and Industry Risk Exposure

This section analyzes Nozomi Networks’ anonymized telemetry from our participating customers to reveal top cybersecurity trends affecting key industries and regions across the world. All data was collected between July 1 – December 31, 2024.

Platform alerts have been translated to their corresponding MITRE ATT&CK tactics, techniques and procedures (TTPs), from both ICS and enterprise matrices.

The Data Manipulation technique leads the chart, occurring more than three times as often as the next most-detected threats. Various attacks performed over Application and Non-Application protocols placed 2nd and 3rd, respectively, followed by the Network Denial of Service technique, which represents various ways to disrupt network activity. Discovery phase techniques like Network Service Scanning and Remote System Discovery rank next, followed by Adversary-In-The-Middle (commonly known as MITM). Brute Force attacks, commonly used by attackers to try different combinations of credentials to establish initial access comprised 3.2% of alerts. Closely related Default Credentials and Valid Accounts techniques, which use legitimate credentials (often weak/default or stolen) to achieve initial access, made the top 10 list but accounted for less than 1% of alerts each.

### 3.1 Industry Insights

Different industries face different challenges, and it’s important to track them to provide fine-tuned solutions rather than following a one-size-fits-all approach. In this section, we look at the top techniques used by attackers in the most targeted industries.[^1]

[^1]: As always, to avoid bias towards the number of Nozomi Networks customers has in different countries, these numbers are averaged on a per-customer basis. In addition, only the industries where Nozomi Networks has at least five customers are included.

These findings reinforce the need for industrial organizations to embrace a holistic approach to cybersecurity and prioritize their efforts according to the current global trends:

- Verify that your cybersecurity solution detects Data Manipulation-related attacks and provides you with enough context to act on them.
- Make sure your network is resilient to DoS attacks and can be easily restored in case of emergency.
- Don’t ignore Discovery tactic-related techniques like Network Service Scanning. While seemingly benign, they can have big consequences during the later stages of an attack, providing malicious actors with all the information they need to succeed.
- Enforce strong credential management by immediately changing default credentials, forbidding weak passwords through company-wide policies and education, and ensure you can efficiently detect various types of Adversary-In-The-Middle attacks.

### 3.2 Regional Insights

Here, we look at the countries reporting the highest number of alerts per customer operating there. To avoid bias, only countries where Nozomi Networks has at least 5 customers are considered.

Compared to the previous 6-month period, the U.S. moved from 5th position to 1st, reflecting the relative increase in alerts in our U.S. customer environments compared to the first half of 2024. Sweden moved from 4th position to 2nd, while Colombia dropped from 3rd place to 5th. Finally, Italy and Spain were replaced by Germany and Australia in the top 5 rankings.

The main takeaway here is that, like each industry, each country has its unique profile of most prevalent threats. Knowing and understanding what threats are actively occurring in your country enables security experts to focus on achieving maximum results with available resources.

---

## 4. Is Your Wireless Network Clean? A Security Hygiene Audit

### 4.1 The Unseen Risks of Industrial Wireless Environments

Industrial environments increasingly rely on wireless communications, from handheld IoT sensors to critical control systems. Yet, most asset owners are unaware of the sheer number of devices communicating over the air within their facilities. This lack of visibility creates significant blind spots in security, leaving organizations vulnerable to threats that exploit unmonitored wireless networks.

### 4.2 Common Threats Targeting Wireless Networks

Wireless vulnerabilities can manifest in a variety of ways, often due to the inherent open nature of radio-frequency communications. Unlike wired networks, wireless networks rely on the transmission of signals through the air, making them more susceptible to interception and unauthorized access.

- **Deauthentication Attacks**: Exploit weaknesses in network protocols to force devices off the network.
- **Rogue Access Points (APs)**: Can be deployed by attackers to impersonate legitimate networks.
- **Eavesdropping**: Can occur when communications over unencrypted wireless protocols are intercepted.
- **Jamming Attacks**: Occur when malicious actors disrupt communications by overwhelming wireless channels.

### 4.3 Unprotected Wireless Networks Are Vulnerable to Deauthentication

Recent research performed by Nozomi Networks into wireless security uncovered widespread vulnerability of wireless networks to deauthentication attacks. Our most concerning finding is that only 6% of observed wireless networks today are adequately protected against deauthentication attacks, as they lack Management Frame Protection (MFP).

### 4.4 Wireless Network Managed Frame Protection Status

![Chart showing 94% of networks are unsupported/MFP disabled, 6% are mandatory/MFP required]

### 4.5 Protecting Critical Infrastructure for Operational Continuity

As a generic guideline, monitoring wireless networks provides the visibility needed to detect unauthorized devices, identify vulnerabilities and protect against attacks in real time. By using wireless security technologies, organizations can continuously monitor the frequencies used by their wireless networks, gaining insights into the devices present, the security posture of the network and any potential threats.

---

## 5. Navigating Device Vulnerability Trends: Key Stats for Security Strategy

In this section we review all ICS advisories released during the second half of 2024. During this period (July 1 – December 31), CISA released 241 advisories, with 619 vulnerabilities affecting products from approximately 70 vendors.

### 5.1 Number of CVEs Released by Sector

The Critical Manufacturing and Energy sectors lead the chart. Most notably, the Communications sector jumped onto the list in 3rd place, possibly tied to Salt Typhoon targeting telecommunications companies during this period.

### 5.2 Number of CWEs Associated with CVEs

The universal Improper Input Validation CWE once again takes first place, reminding us how important input sanitization is. As in the previous reporting period, it is followed in close succession by the Out-of-Bounds Write and Out-of-Bounds Read.

### 5.3 Risk Score Statistics

Where available, we also looked at the Common Vulnerability Scoring System (CVSS) and Exploit Prediction Scoring System (EPSS) risk scores assigned to the top ICS vulnerabilities reported during this period.

- Four vulnerabilities were marked as Known Exploited Vulnerabilities (KEVs).
- 20 vulnerabilities have an EPSS score indicating a >1% probability of being exploited in the wild.
- The average CVSS risk score was 7.43.

---

## 6. The Botnet Epidemic: Statistics, Threats, and Defenses

In this section, we explore the world of IoT botnets, examining their mechanics, the threats they pose to cybersecurity and effective strategies to combat this growing threat.

### 6.1 Attack Source Locations

As in several previous periods, most of the attacks came from China and the U.S. That’s expected given the size and the level of automation in the two most dominant countries in the world.

### 6.2 Number of Unique Daily Attacker IPs

The peak number of simultaneous attacks for this period is more than 1.5 times greater than during the previous period (roughly 1,600 vs. 1,000).

### 6.3 Top Credentials Used

Brute-forcing SSH and Telnet credentials remains one of the most popular options for attackers to establish initial access to the vulnerable devices.

### 6.4 Top Executed Commands

Apart from the universal commands needed to establish the right shell environment, attackers frequently execute commands to manipulate the `.ssh` directory to ensure persistent access.

### 6.5 Top Payload File Types

Most of the payloads comprised various types of scripts supported by multiple architectures (multi). Regarding executable payloads, 32-bit ARM payloads are still the top choice of the attackers.

### 6.6 Top Payload Packers

Once again, UPX in its many versions is the top choice of attackers.

---

## 7. Insights Into the Latest OT Malware

### 7.1 BUSTLEBERM aka FrostyGoop

The emergence of BUSTLEBERM (aka FrostyGoop) malware, reportedly used as a cyberweapon to cut energy in Ukraine, once again highlights the importance of continuous threat monitoring to safeguard critical infrastructure.

### 7.2 OrpaCrab aka IOCONTROL

First documented by QiAnXin XLab, OrpaCrab aka IOCONTROL malware was linked to Iranian actors targeting IoT and OT environments in the U.S. and Israel.

### 7.3 Ransomware in OT

While ransomware is not traditionally considered an OT threat, its ability to disrupt IT environments that are closely integrated with OT systems makes it a significant risk to critical infrastructure. In December 2024 alone, our products raised 268 alerts associated with ransomware deployment attempts.

---

## 8. Recommendations

### 8.1 Implement a risk reduction strategy
Keep your threat intelligence databases updated and ensure that your security providers prioritize OT and IoT threats.

### 8.2 Prioritize anomaly detection and response
Adopt a multi-layered defense strategy and deploy solutions capable of identifying abnormal behavior that deviates from your established baselines.

### 8.3 Adopt regional and industry-specific threat intelligence
Tailor the security measures based on insights into regional attack trends and sector-specific vulnerabilities.

### 8.4 Strengthen wireless network security with regular audits
Conduct comprehensive wireless security audits to identify potential vulnerabilities in industrial wireless environments.

### 8.5 Enhance vulnerability management with key metrics
Implement a proactive vulnerability management program that prioritizes vulnerabilities based on asset criticality and contextual factors.

### 8.6 Fortify defenses against botnet attacks
Use traffic analysis and anomaly detection tools to identify botnet activity early.

### 8.7 Work with your partners
Get the knowledge and capabilities you need by bringing together internal operational and cyber practitioners, leaning on your vendors, and participating in your industry’s ISAC.