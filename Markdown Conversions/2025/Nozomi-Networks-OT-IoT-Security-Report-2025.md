# OT/IoT Cybersecurity Trends and Insights: 2024 2H Review

**February 2025**

**About Nozomi Networks Labs**

Nozomi Networks Labs is dedicated to reducing cyber risk for the world’s industrial and critical infrastructure organizations. Through its cybersecurity research and collaboration with industry and institutions, it helps defend the operational systems that support everyday life.

The Labs team conducts investigations into industrial device vulnerabilities and, through a responsible disclosure process, contributes to the publication of advisories by recognized authorities.

To help the security community with current threats, they publish timely blogs, research papers and free tools. The Threat Intelligence and Asset Intelligence services of Nozomi Networks are supplied by ongoing data generated and curated by the Labs team.

To find out more, and subscribe to updates, visit [nozominetworks.com/labs](nozominetworks.com/labs)

## Table of Contents
- [1. Executive Overview](#1-executive-overview)
- [2. Introduction](#2-introduction)
- [3. Threat Intelligence: Understanding Regional and Industry Risk Exposure](#3-threat-intelligence-understanding-regional-and-industry-risk-exposure)
  - [3.1 Industry Insights](#31-industry-insights)
  - [3.2 Regional Insights](#32-regional-insights)
- [4. Is Your Wireless Network Clean? A Security Hygiene Audit](#4-is-your-wireless-network-clean-a-security-hygiene-audit)
  - [4.1 The Unseen Risks of Industrial Wireless Environments](#41-the-unseen-risks-of-industrial-wireless-environments)
  - [4.2 Common Threats Targeting Wireless Networks](#42-common-threats-targeting-wireless-networks)
  - [4.3 Unprotected Wireless Networks Are Vulnerable to Deauthentication](#43-unprotected-wireless-networks-are-vulnerable-to-deauthentication)
  - [4.4 Wireless Network Managed Frame Protection Status](#44-wireless-network-managed-frame-protection-status)
  - [4.5 Protecting Critical Infrastructure for Operational Continuity](#45-protecting-critical-infrastructure-for-operational-continuity)
- [5. Navigating Device Vulnerability Trends: Key Stats for Security Strategy](#5-navigating-device-vulnerability-trends-key-stats-for-security-strategy)
  - [5.1 Number of CVEs Released by Sector](#51-number-of-cves-released-by-sector)
  - [5.2 Number of CWEs Associated with CVEs](#52-number-of-cwes-associated-with-cves)
  - [5.3 Risk Score Statistics](#53-risk-score-statistics)
- [6. The Botnet Epidemic: Statistics, Threats, and Defenses](#6-the-botnet-epidemic-statistics-threats-and-defenses)
  - [6.1 Attack Source Locations](#61-attack-source-locations)
  - [6.2 Number of Unique Daily Attacker IPs](#62-number-of-unique-daily-attacker-ips)
  - [6.3 Top Credentials Used](#63-top-credentials-used)
  - [6.4 Top Executed Commands](#64-top-executed-commands)
  - [6.5 Top Payload File Types](#65-top-payload-file-types)
  - [6.6 Top Payload Packers](#66-top-payload-packers)
- [7. Insights Into the Latest OT Malware](#7-insights-into-the-latest-ot-malware)
  - [7.1 BUSTLEBERM aka FrostyGoop](#71-bustleberm-aka-frostygoop)
  - [7.2 OrpaCrab aka IOCONTROL](#72-orpacrab-aka-iocontrol)
  - [7.3 Ransomware in OT](#73-ransomware-in-ot)
- [8. Recommendations](#8-recommendations)
  - [8.1 Implement a risk reduction strategy](#81-implement-a-risk-reduction-strategy)
  - [8.2 Prioritize anomaly detection and response](#82-prioritize-anomaly-detection-and-response)
  - [8.3 Adopt regional and industry-specific threat intelligence](#83-adopt-regional-and-industry-specific-threat-intelligence)
  - [8.4 Strengthen wireless network security with regular audits](#84-strengthen-wireless-network-security-with-regular-audits)
  - [8.5 Enhance vulnerability management with key metrics](#85-enhance-vulnerability-management-with-key-metrics)
  - [8.6 Fortify defenses against botnet attacks](#86-fortify-defenses-against-botnet-attacks)
  - [8.7 Work with your partners](#87-work-with-your-partners)

## 1. Executive Overview

Cyberattacks on the world’s critical infrastructure are on the rise. Global tensions continue to escalate, ransomware operators act with impunity, geopolitical conflict rises, cyber-espionage persists, and cyber has become an integral part of military strategies. The systems we design and defend must not only withstand a barrage of threats in today’s multipolar world but also balance the need to operate safely at scale, where human lives are at stake.

Multi-year adversarial operations such as Volt Typhoon and Salt Typhoon have recently been exposed, highlighting how nation-state actors have infiltrated critical infrastructure and communications systems, often remaining undetected for years.

The Nozomi Networks Labs team delivers this semi-annual report to provide insights into how the world’s largest industrial organizations and critical infrastructure operators can protect themselves from these advanced threats. Leveraging a network of more than 50,000 global honeypots, wireless monitoring sensors, inbound telemetry, partnerships, threat intelligence and other resources, our team uncovers trends, novel attack methods and unique insights that are critical for safeguarding operational technology (OT) and cyber-physical systems.

While cybersecurity reports often focus on threats targeting wired networks—such as Ethernet, industrial Ethernet and fiber—our capabilities extend beyond wired networks to encompass a multitude of wireless transport protocols. This expanded visibility enables our research team to access insights that are otherwise unavailable. Threats do not solely reside in Wi-Fi access points; wireless protocols like ZigBee, Bluetooth, LoRaWAN and others are heavily relied upon in industrial environments including power grids, transportation systems, security devices and medical equipment. Alarmingly, our findings reveal that 94% of Wi-Fi networks lack sufficient protections against deauthentication attacks, which are frequently leveraged as part of larger incidents. These vulnerabilities expose organizations to risks such as credential theft, traffic interception, man-in-the-middle attacks and spoofing, any of which could compromise the integrity of critical control systems.

Our threat intelligence, enriched by indicators of compromise, threat actor profiles and vulnerability data from Mandiant, empowers customers to proactively defend their systems. By analyzing telemetry informed by this intelligence, our researchers uncover actionable trends and patterns.

![Image description: 94% of Wi-Fi networks lack protection against deauthentication attacks]

For example, manufacturing was the most targeted sector during the reporting period, and the U.S. was the most attacked country, up from #5 during the first half of 2024. Together these findings signal that U.S. manufacturers should increase their vigilance, as they are regularly targeted by ransomware and espionage campaigns.

In addition to reviewing the key threats from second half of 2024 such as malware, botnets and vulnerabilities, the report also delivers clear recommendations for how to navigate these emerging risks in the coming year.

By understanding these evolving threats and leveraging actionable insights, we can defend our critical systems to ensure resilience, safety and operational continuity in an increasingly uncertain world.

![Image description: Most Targeted Sectors: Critical Manufacturing (462), Energy (174), Transportation Systems (56), Commercial Facilities (48), Communications (74). Most Attacked Countries H1 2024: Italy, Spain, Colombia, Sweden, United States. H2 2024: United States, Sweden, Germany, Australia, Colombia.]

## 2. Introduction

In this report we analyze unique telemetry from hundreds of real OT and IoT environments to provide a comprehensive overview of the dynamic threat landscape in the second half of 2024. The report breaks out our findings by region and industry to help you fine-tune your defense strategies.

Because wireless network security has emerged as a critical factor in maintaining operational continuity, our latest research includes a special section that examines the hidden risks of industrial wireless environments, including threats such as deauthentication attacks, which can compromise critical systems and processes.

The results of a special security hygiene audit reveal common vulnerabilities and underscore why monitoring wireless networks is vital for protecting infrastructure.

We also explore broader trends in ICS asset vulnerability advisories, presenting key statistics on the top affected sectors and Common Weakness Enumerations (CWEs). We assess the current impact of botnet activity on IoT systems and provide guidance for protecting against this persistent threat.

Finally, we dig into recent OT malware attack patterns — including new families such as BUSTLEBERM (also known as FrostyGoop) and OrpaCrab (also known as IOCONTROL) to give you the insights you need to keep your OT and IoT environments safe.

## 3. Threat Intelligence: Understanding Regional and Industry Risk Exposure

This section analyzes Nozomi Networks’ anonymized telemetry from our participating customers to reveal top cybersecurity trends affecting key industries and regions across the world. All data was collected between July 1 – December 31, 2024.

Platform alerts have been translated to their corresponding MITRE ATT&CK tactics, techniques and procedures (TTPs), from both ICS and enterprise matrices.

The Data Manipulation technique leads the chart, occurring more than three times as often as the next most-detected threats. Various attacks performed over Application and Non-Application protocols placed 2nd and 3rd, respectively, followed by the Network Denial of Service technique, which represents various ways to disrupt network activity. Discovery phase techniques like Network Service Scanning and Remote System Discovery rank next, followed by Adversary-In-The-Middle (commonly known as MITM). Brute Force attacks, commonly used by attackers to try different combinations of credentials to establish initial access comprised 3.2% of alerts. Closely related Default Credentials and Valid Accounts techniques, which use legitimate credentials (often weak/default or stolen) to achieve initial access, made the top 10 list but accounted for less than 1% of alerts each.

| ID     | Technique name                 | Tactic name                      | %        |
| :----- | :----------------------------- | :------------------------------- | :------- |
| T1565  | Data Manipulation              | Impact                           | 39.54%   |
| T1071  | Application Layer Protocol     | Command and Control              | 12.29%   |
| T1095  | Non-Application Layer Protocol | Command and Control              | 12.29%   |
| T1498  | Network Denial of Service      | Impact                           | 8.86%    |
| T0841  | Network Service Scanning       | Discovery                        | 7.89%    |
| T0846  | Remote System Discovery        | Discovery                        | 7.89%    |
| T1557  | Adversary-in-the-Middle        | Credential access; Collection    | 5.48%    |
| T1110  | Brute Force                    | Credential access                | 3.20%    |
| T0812  | Default Credentials            | Lateral Movement                 | 0.89%    |
| T0859  | Valid Accounts                 | Persistence; Lateral Movement    | 0.89%    |

_Top 10 Most Common MITRE ATT&CK™ Techniques Associated with Raised Alerts_

These findings reinforce the need for industrial organizations to embrace a holistic approach to cybersecurity and prioritize their efforts according to the current global trends:

-   Verify that your cybersecurity solution detects Data Manipulation-related attacks and provides you with enough context to act on them.
-   Make sure your network is resilient to DoS attacks and can be easily restored in case of emergency.
-   Don’t ignore Discovery tactic-related techniques like Network Service Scanning. While seemingly benign, they can have big consequences during the later stages of an attack, providing malicious actors with all the information they need to succeed.
-   Enforce strong credential management by immediately changing default credentials, forbidding weak passwords through company-wide policies and education, and ensure you can efficiently detect various types of Adversary-In-The-Middle attacks.

### 3.1 Industry Insights

Different industries face different challenges, and it’s important to track them to provide fine-tuned solutions rather than following a one-size-fits-all approach. In this section, we look at the top techniques used by attackers in the most targeted industries.<sup>1</sup>

Here are the top general industries associated with the highest number of alerts per customer in the second half of 2024:

-   Manufacturing
-   Transportation
-   Minerals & Mining
-   Business Services
-   Energy, Utilities & Waste

The following pages break down the top 5 MITRE ATT&CK techniques by sector according to available customer data during the reporting period.

For the Manufacturing sector, more than half of all the reported attacks were associated with the Data Manipulation technique. It is followed by Network Denial of Service technique and closely related Network Service Scanning and Remote System Discovery techniques.

| ID     | Technique name             | Tactic name                      | %        |
| :----- | :------------------------- | :------------------------------- | :------- |
| T1565  | Data Manipulation          | Impact                           | 59.57%   |
| T1498  | Network Denial of Service  | Impact                           | 9.62%    |
| T0841  | Network Service Scanning   | Discovery                        | 9.19%    |
| T0846  | Remote System Discovery    | Discovery                        | 9.19%    |
| T1557  | Adversary-in-the-Middle    | Credential access; Collection    | 4.17%    |

_Manufacturing_

In the Transportation sector, the proportion of Data Manipulation-related attacks is more than twice as low as in the Manufacturing sector. In addition, Brute Force attacks were much more prevalent, comprising around 17% of all the reported attacks.

To summarize, different sectors pose different challenges. That’s why it’s so important to reinforce a comprehensive cybersecurity program with protection against the known threats facing your industry.

| ID     | Technique name             | Tactic name                      | %        |
| :----- | :------------------------- | :------------------------------- | :------- |
| T1565  | Data manipulation          | Impact                           | 26.72%   |
| T1110  | Brute Force                | Credential access                | 17.11%   |
| T1557  | Adversary-in-the-Middle    | Credential access; Collection    | 14.28%   |
| T1498  | Network Denial of Service  | Impact                           | 11.48%   |
| T0875  | Change Program State       | Execution; Impair process control | 8.86%    |

_Transportation_

| ID     | Technique name             | Tactic name                      | %        |
| :----- | :------------------------- | :------------------------------- | :------- |
| T0841  | Network Service Scanning   | Discovery                        | 37.97%   |
| T0846  | Remote System Discovery    | Discovery                        | 37.97%   |
| T1498  | Network Denial of Service  | Impact                           | 10.12%   |
| T1565  | Data manipulation          | Impact                           | 6.75%    |
| T1200  | Hardware Additions         | Initial access                   | 2.25%    |

_Minerals & Mining_

| ID     | Technique name             | Tactic name                      | %        |
| :----- | :------------------------- | :------------------------------- | :------- |
| T1565  | Data Manipulation          | Impact                           | 43.25%   |
| T0841  | Network Service Scanning   | Discovery                        | 22.96%   |
| T0846  | Remote System Discovery    | Discovery                        | 22.96%   |
| T1498  | Network Denial of Service  | Impact                           | 4.63%    |
| T1557  | Adversary-in-the-Middle    | Credential access; Collection    | 3.98%    |

_Energy, Utilities & Waste_

| ID     | Technique name             | Tactic name                      | %        |
| :----- | :------------------------- | :------------------------------- | :------- |
| T1557  | Adversary-in-the-Middle    | Credential access; Collection    | 50.38%   |
| T1110  | Brute Force                | Credential access                | 27.98%   |
| T1498  | Network Denial of Service  | Impact                           | 15.23%   |
| T0841  | Network Service Scanning   | Discovery                        | 1.58%    |
| T0846  | Remote System Discovery    | Discovery                        | 1.58%    |

_Business Services_
<br>
<sup>1</sup> As always, to avoid bias towards the number of Nozomi Networks customers has in different countries, these numbers are averaged on a per-customer basis. In addition, only the industries where Nozomi Networks has at least five customers are included.

### 3.2 Regional Insights

Here, we look at the countries reporting the highest number of alerts per customer operating there. To avoid bias, only countries where Nozomi Networks has at least 5 customers are considered. Here is the top five ranking for the second half of 2024, compared to the previous six months:

| H1 2024       | H2 2024       |
| :------------ | :------------ |
| 1. Italy      | 1. United States |
| 2. Spain      | 2. Sweden     |
| 3. Colombia   | 3. Germany    |
| 4. Sweden     | 4. Australia  |
| 5. United States | 5. Colombia   |

Compared to the previous 6-month period, the U.S. moved from 5th position to 1st, reflecting the relative increase in alerts in our U.S. customer environments compared to the first half of 2024. Sweden moved from 4th position to 2nd, while Colombia dropped from 3rd place to 5th. Finally, Italy and Spain were replaced by Germany and Australia in the top 5 rankings.

Now, let’s delve into the MITRE ATT&CK techniques associated with the alerts seen most frequently by customers in these countries.

The top threat techniques reported in U.S. customer environments reflect the top global techniques in the same descending order but in slightly different proportions.

| ID     | Technique name                 | Tactic name                      | %        |
| :----- | :----------------------------- | :------------------------------- | :------- |
| T1565  | Data Manipulation              | Impact                           | 47.91%   |
| T1071  | Application Layer Protocol     | Command and Control              | 15.32%   |
| T1095  | Non-Application Layer Protocol | Command and Control              | 15.32%   |
| T1498  | Network Denial of Service      | Impact                           | 7.02%    |
| T0841  | Network Service Scanning       | Discovery                        | 5.54%    |

_United States_

| ID     | Technique name             | Tactic name                      | %        |
| :----- | :------------------------- | :------------------------------- | :------- |
| T1498  | Network Denial of Service  | Impact                           | 34.13%   |
| T1565  | Data manipulation          | Impact                           | 28.77%   |
| T1557  | Adversary-in-the-Middle    | Credential access; Collection    | 11.60%   |
| T0841  | Network Service Scanning   | Discovery                        | 4.82%    |
| T0846  | Remote System Discovery    | Discovery                        | 4.82%    |

_Sweden_

In Colombia, the proportion of the network DoS attacks is significantly higher than in other countries, contributing to a whopping 86+% of total attacks seen here.

The main takeaway here is that, like each industry, each country has its unique profile of most prevalent threats. Knowing and understanding what threats are actively occurring in your country enables security experts to focus on achieving maximum results with available resources.

| ID     | Technique name                 | Tactic name                      | %        |
| :----- | :----------------------------- | :------------------------------- | :------- |
| T0841  | Network Service Scanning       | Discovery                        | 36.10%   |
| T0846  | Remote System Discovery        | Discovery                        | 36.10%   |
| T1498  | Network Denial of Service      | Impact                           | 14.17%   |
| T1071  | Application Layer Protocol     | Command and Control              | 2.98%    |
| T1095  | Non-Application Layer Protocol | Command and Control              | 2.98%    |

_Germany_

| ID     | Technique name             | Tactic name                      | %        |
| :----- | :------------------------- | :------------------------------- | :------- |
| T1498  | Network Denial of Service  | Impact                           | 86.13%   |
| T0841  | Network Service Scanning   | Discovery                        | 2.85%    |
| T0846  | Remote System Discovery    | Discovery                        | 2.85%    |
| T1557  | Adversary-in-the-Middle    | Credential access; Collection    | 2.36%    |
| T1110  | Brute Force                | Credential access                | 2.31%    |

_Colombia_

| ID     | Technique name             | Tactic name                      | %        |
| :----- | :------------------------- | :------------------------------- | :------- |
| T1498  | Network Denial of Service  | Impact                           | 23.38%   |
| T0841  | Network Service Scanning   | Discovery                        | 21.10%   |
| T0846  | Remote System Discovery    | Discovery                        | 21.10%   |
| T1557  | Adversary-in-the-Middle    | Credential access; Collection    | 20.05%   |
| T1110  | Brute Force                | Credential access                | 4.99%    |

_Australia_

## 4. Is Your Wireless Network Clean? A Security Hygiene Audit

### 4.1 The Unseen Risks of Industrial Wireless Environments

Industrial environments increasingly rely on wireless communications, from handheld IoT sensors to critical control systems. Yet, most asset owners are unaware of the sheer number of devices communicating over the air within their facilities. This lack of visibility creates significant blind spots in security, leaving organizations vulnerable to threats that exploit unmonitored wireless networks.

Wireless networks, particularly in industrial environments, often operate outside traditional IT controls. Devices can communicate on legacy protocols or unsecured channels, making them attractive targets for attackers. One of the most underestimated challenges in wireless security is the difficulty of understanding which devices are active, what protocols they are using and how vulnerable these communications might be.

Without comprehensive monitoring, it is nearly impossible to know whether your wireless network truly secure.

### 4.2 Common Threats Targeting Wireless Networks

Wireless vulnerabilities can manifest in a variety of ways, often due to the inherent open nature of radio-frequency communications. Unlike wired networks, wireless networks rely on the transmission of signals through the air, making them more susceptible to interception and unauthorized access. This open communication channel provides ample opportunity for attackers to exploit weaknesses, often without leaving a trace. As industries increasingly rely on wireless technologies for critical operations, the need to identify and address these vulnerabilities has never been more urgent.

Below are some of the most common threats faced by industrial wireless environments:

-   **Deauthentication Attacks** exploit weaknesses in network protocols to force devices off the network, disrupting operations and potentially paving the way for further attacks. They leverage a built-in feature in the Wi-Fi protocol, specifically in the management frames used for communication between devices and access points. By transmitting fake deauthentication frames, attackers can force devices to disconnect from the network. This can escalate into more severe disruptions, such as data interception and unauthorized access, especially when combined with additional malicious actions.
-   **Rogue Access Points (APs)** can be deployed by attackers to impersonate legitimate networks, tricking devices into connecting and exposing sensitive data.
-   **Eavesdropping** can occur when communications over unencrypted wireless protocols are intercepted, enabling attackers to steal credentials, read sensitive data or monitor operations. This threat is especially common over free, public Wi-Fi services in airports, hotels, etc.
-   **Jamming Attacks** occur when malicious actors disrupt communications by overwhelming wireless channels, leading to downtime or operational inefficiencies.

In addition to traditional wireless vulnerabilities, **Unauthorized UAV (Drone) Overflight** has emerged as a growing concern, particularly in industrial environments. Drones, equipped with advanced communication technologies, can pose significant risks, including:

-   **Signal Interception and Espionage:** Drones can fly over facilities, intercepting unencrypted wireless communications. This allows attackers to eavesdrop on sensitive data, such as proprietary designs, operational information, and control signals. In addition to intercepting signals, drones can be equipped with digital cameras to conduct visual surveillance, capturing images or videos of physical infrastructure, sensitive equipment, or areas that may otherwise be restricted. This form of espionage enables attackers to gather critical intelligence about a facility’s operations, weaknesses, or security measures, potentially leading to the theft of intellectual property, strategic plans, or access to vulnerable systems.
-   **Signal Jamming:** Drones can intentionally interfere with wireless communications by emitting strong signals on the same frequencies as those used by the targeted network. This type of attack can disrupt network operations, leading to temporary or prolonged downtime and potentially compromising the integrity of critical processes.
-   **Network Access Attempts:** Some drones are equipped with technologies designed to exploit weaknesses in wireless networks. These drones may attempt to connect to unsecured or poorly protected networks, creating an entry point for cyber attackers to gain access to industrial control systems, allowing for further exploitation or manipulation.

The growing accessibility and capability of drones make this form of attack particularly dangerous, as they can operate covertly, monitoring or disrupting operations without detection. When combined with espionage capabilities, drones present a serious and evolving risk to industrial wireless security.

The common wireless threats described here are particularly alarming in industrial environments, where the consequences extend beyond data breaches to include operational disruption, safety risks and regulatory non-compliance.

### 4.3 Unprotected Wireless Networks Are Vulnerable to Deauthentication

Recent research performed by Nozomi Networks into wireless security uncovered widespread vulnerability of wireless networks to deauthentication attacks. Our most concerning finding is that only 6% of observed wireless networks today are adequately protected against deauthentication attacks, as they lack Management Frame Protection (MFP), a crucial security feature designed to prevent attackers from spoofing management frames. In other words, the vast majority of wireless networks, including those in mission-critical environments, remain highly exposed to these kinds of attacks. In healthcare, for example, vulnerabilities in wireless networks could lead to unauthorized access to patient data or interference with critical systems. Similarly, in industrial environments, these attacks could disrupt automated processes, halt production lines or create safety hazards for workers.

### 4.4 Wireless Network Managed Frame Protection Status

**Mitigation Steps Against Deauthentication Attacks**

To protect against deauthentication attacks and improve wireless network security, organizations can take these immediate actions:

1.  **Enable 802.11w (MFP)**, which is essential for defending against deauthentication attacks. This standard adds encryption to management frames, making it significantly harder for attackers to forge deauthentication messages and disrupt the network.
2.  **Upgrade to WPA3**, which provides enhanced security features, including Protected Management Frames (PMFs). This protocol helps to protect against deauthentication attacks and ensures a more robust defense against wireless threats.
3.  **Regularly monitor wireless networks** for signs of suspicious activity. By scanning for devices conducting deauthentication attacks or other disruptive behaviors, organizations can quickly identify and respond to threats.

![Image description: 802.11w MFP Configuration Status Across Observed Wi-Fi Networks. 6% Mandatory (MFP required to connect), 94% Unsupported (MFP disabled).]

### 4.5 Protecting Critical Infrastructure for Operational Continuity

As a generic guideline, monitoring wireless networks provides the visibility needed to detect unauthorized devices, identify vulnerabilities and protect against attacks in real time. By using wireless security technologies, organizations can continuously monitor the frequencies used by their wireless networks, gaining insights into the devices present, the security posture of the network and any potential threats. This proactive approach is key for detecting attacks before they can escalate into more serious incidents.

Real-time monitoring also enables organizations to react swiftly to ongoing threats, minimizing the impact of attacks like deauthentication or other forms of signal disruption. Additionally, by continuously scanning the air, organizations can ensure that any unauthorized access points or rogue devices are identified and removed, reducing the likelihood of further compromise.

Ultimately, the importance of monitoring wireless networks cannot be overstated. As the number of wireless devices and connected systems grows, so too does the potential attack surface. By implementing comprehensive monitoring solutions and ensuring that wireless networks are properly secured, asset owners can protect their devices, ensure business continuity and safeguard sensitive information from potential cyber threats.

The solution begins with awareness. By deploying technology capable of scanning wireless frequencies and extracting telemetry, asset owners can achieve unprecedented insight into their environments. Telemetry collected includes device identities, communication protocols, and vulnerability assessments, enabling proactive defenses against potential threats.

## 5. Navigating Device Vulnerability Trends: Key Stats for Security Strategy

In this section we review all ICS advisories released during the second half of 2024, identifying new trends and highlighting changes. During this period (July 1 – December 31), CISA released 241 advisories, with 619 vulnerabilities affecting products from approximately 70 vendors. Here’s a closer look at these vulnerabilities.

_If you’re a Nozomi Networks customer, you are covered for these vulnerabilities because asset intelligence, including CVEs, is baked into our product by the Nozomi Networks Labs._

### 5.1 Number of CVEs Released by Sector

The chart on the right identifies the top 10 industries affected by the vulnerabilities highlighted in the ICS advisories during this period.

As with the previous six-month period, the Critical Manufacturing and Energy sectors lead the chart. Most notably, the Communications sector jumped onto the list in 3rd place, possibly tied to Salt Typhoon targeting telecommunications companies during this period. Increased scrutiny of exploitable vulnerabilities may have led researchers to discover and report more CVEs. The emergence of the Communications sector on the list displaced perennially targeted sectors such as Transportation, Commercial Facilities and Water and Wastewater Systems by one position each. Given the importance of communications systems in our daily lives, we will closely monitor

![Image description: Top 10 Sectors by Number or ICS CVE Advisories July 1 to December 31, 2024. Critical Manufacturing (462), Energy (174), Communications (74), Commercial Facilities (48), Transportation Systems (56), Water and Wastewater Systems(20), Chemical (28), Government Services and Facilities (43), Food and Agriculture (31), Healthcare and Public Health (38).]

vulnerabilities associated with this sector to help ensure our customers are protected.

The rise of vulnerabilities affecting Government Services and Facilities is another highlight from this period, after the sector dropped off the list in the first half of 2024. Nozomi Networks is proud to take part in multiple initiatives around the globe aiming to improve the cybersecurity posture of government organizations at various levels.

### 5.2 Number of CWEs Associated with CVEs

Now, let’s turn to the top Common Weakness Enumeration (CWE) categories associated with these vulnerabilities.

The universal Improper Input Validation CWE once again takes first place, reminding us how important input sanitization is. As in the previous reporting period, it is followed in close succession by the Out-of-Bounds Write and Out-of-Bounds Read. CWEs Path Traversal and Uncontrolled Resource Consumptions also reappear, albeit in slightly different positions. The recurrence of these familiar CWEs reinforces the need to integrate the best available OT/ICS-specific threat intelligence into your cybersecurity platform to ensure you can automatically detect known issues in your environment.

![Image description: Top 10 CWEs Associated With ICS Advisories July 1 to December 31, 2024. Improper input validation - CWE-20, Out-of-bounds write - CWE-787, Out-of-bounds read - CWE-125, Stack-based buffer overﬂow - CWE-121, Missing authentication for critical function - CWE-306, Heap-based buffer overﬂow - CWE-122, Uncontrolled resource consumption - CWE-400, Improper limitation of a pathname to a restricted directory ('path traversal') - CWE-22, Improper restriction of operations within the bounds of a memory buffer - CWE-119, Improper neutralization of special elements used in a command ('command injection') - CWE-77.]

### 5.3 Risk Score Statistics

Where available, we also looked at the Common Vulnerability Scoring System CVSS (v4 where available, otherwise v3) and Exploit Prediction Scoring System (EPSS) risk scores assigned to the top ICS vulnerabilities reported during this period. Here’s what we found:

-   Four vulnerabilities were marked as Known Exploited Vulnerabilities (KEVs), meaning they have been observed as actively exploited in the wild.
-   20 vulnerabilities have an EPSS score indicating a >1% probability of being exploited in the wild. This threshold is generally considered high.
-   The average CVSS risk score was 7.43.
    -   ~71% of vulnerabilities received a High or Critical risk score (≥7.0).
-   The average EPSS score was 0.012.

The identification of four Known Exploited Vulnerabilities (KEVs) is significant because it highlights vulnerabilities that are actively being targeted by threat actors, emphasizing the need for immediate mitigation. Similarly, the 20 vulnerabilities with the EPSS score above 1% underscores their high likelihood of exploitation, signaling a crucial area of focus for proactive risk management.

As we can see, the CVSS risk scores for vulnerabilities affecting OT are generally high, emphasizing the need for organizations to resolve them promptly. High EPSS scores and the KEV flag are excellent indicators for prioritization. While the total number of vulnerabilities flagged this way remains relatively low, these are generally the most critical vulnerabilities to address first.

To handle vulnerabilities efficiently, organizations should also adopt metrics tailored to their unique environments — such as the criticality of individual assets — to make more informed prioritization decisions and ensure risk scores reflect how your organization assigns risk.

![Image description: Distribution of Vulnerabilities by CVSS Risk Score* July 1 to December 31, 2024. Critical (14%), High (57%), Medium (27%), Low (2%). * Where available]

## 6. The Botnet Epidemic: Statistics, Threats, and Defenses

In this section, we explore the world of IoT botnets, examining their mechanics, the threats they pose to cybersecurity and effective strategies to combat this growing threat. All data is collected by our globally distributed chain of honeypots, completely unrelated to our customers’ environments. From this vantage point, we analyze the tactics, techniques and procedures currently employed by botnets to help asset owners better protect their systems and more quickly spot anomalies

_If you’re a Nozomi Networks customer, you are covered for these IoT threats because intelligence regarding them is baked into our product by the Labs team._

### 6.1 Attack Source Locations

This chart represents the distribution IoT botnet attacks on our honeypots during the second half of 2024, based on absolute number of attacks from each country of origin. Typically, the attacks come from compromised devices.

Note that the countries with