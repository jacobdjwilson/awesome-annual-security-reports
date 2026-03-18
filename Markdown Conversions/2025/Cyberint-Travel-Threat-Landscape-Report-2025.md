# Travel & Tour Operations Industry Threat Landscape

By Josh Puentes, Manasa Pisipati and Ben Johnathan Neeman

May 2025

## Table of Contents
- [Executive Summary](#executive-summary)
- [Cyber Incidents](#cyber-incidents)
  - [Timeline of Notable Events](#timeline-of-notable-events)
  - [Cyber Incidents Details](#cyber-incidents-details)
  - [Top 10 Most Critical TTPs in this Sector](#top-10-most-critical-ttps-in-this-sector)
- [Trend Predictions](#trend-predictions)
  - [1. Surge in DDoS attacks targeting booking and ticketing systems](#1-surge-in-ddos-attacks-targeting-booking-and-ticketing-systems)
  - [2. Increased data breaches via misconfigured cloud storage](#2-increased-data-breaches-via-misconfigured-cloud-storage)
  - [3. Phishing campaigns exploiting employee credentials](#3-phishing-campaigns-exploiting-employee-credentials)
  - [4. Supply chain attacks via third-party vendors](#4-supply-chain-attacks-via-third-party-vendors)
- [Cyberint, Now a Check Point Company Solutions](#cyberint-now-a-check-point-company-solutions)
  - [Attack Surface Monitoring](#attack-surface-monitoring)
  - [Threat Intelligence Monitoring](#threat-intelligence-monitoring)
  - [Dedicated Analyst Services](#dedicated-analyst-services)
- [Conclusions and Recommendations](#conclusions-and-recommendations)
  - [Conclusions](#conclusions)
  - [Recommendations](#recommendations)
- [Appendix](#appendix)
  - [Consolidated TTP List](#consolidated-ttp-list)
  - [IOCS By Threat Actor](#iocs-by-threat-actor)
  - [External References Outside of Cyberint](#external-references-outside-of-cyberint)
- [Contact us](#contact-us)

---

## Executive Summary

Cyberint, now a Check Point Company conducted a threat landscape report focusing on the Travel and Tour Operation Industry. The following report outlines recent cyber events, cyber threat predictions, and an overview of Cyberint services as a solution to mitigating digital threats.

From 2023 to 2025, the global travel sector faced a surge in targeted cyber attacks, including DDoS disruptions, ransomware incidents, data breaches via misconfigured cloud storage, and third-party supply chain compromises. The report includes an outline of events spanning worldwide. It also includes a list of the prominent TTPs (tools and techniques) relating to the attackers and a list of related IOCs that should be noted and blocked.

Below are the trend predictions Cyberint, now a Check Point Company anticipates, based on the related incidents:

**DDoS Attacks Disrupting Booking Systems**
These attacks are often timed to peak travel periods and exploit the industry's reliance on real-time online services. Threat actor groups are expected to continue leveraging botnets to cripple operations, potentially leading to extortion demands for service restoration.

**Data Breaches via Misconfigured Cloud Storage**
Attackers are increasingly using advanced tools and automated scripts to identify and exfiltrate data from exposed cloud storage. Small to mid-sized travel companies without strong DevSecOps practices remain highly vulnerable.

**Phishing and Credential Exploitation**
Attackers are using advanced social engineering techniques, including impersonation and AI-generated phishing lures, to harvest employee credentials. These attacks enable ransomware deployment, internal data exfiltration, and system persistence.

**Supply Chain Compromise and Third-Party Risks**
Threat actors are bypassing hardened perimeters by targeting vendors in payment processing, authentication, and cloud infrastructure, often leveraging outdated or insecure applications to infiltrate core systems and exfiltrate sensitive data.

To mitigate these evolving threats, Cyberint, now a Check Point Company provides continuous Threat Intelligence (TI) and Attack Surface Monitoring (ASM) tailored to the travel sector external risk environment. We detect early indicators of compromise, exposed assets, and threat actor activity through comprehensive monitoring across an extensive pool of sources. This proactive intelligence approach enables travel organizations to stay ahead of targeted threats and minimize operational and reputational impact.

---

## Cyber Incidents

### Timeline of Notable Events

![Figure 1: Timeline of Cyber Attacks Covered in this Report]

### Cyber Incidents Details

**A professional air ticket consolidator DDoS Attack**
In March 2025, a cyber attack disrupted a professional air ticket consolidator’s operations, impacting its customers in Germany, Austria, Switzerland, and worldwide. Their booking system was impacted due to a potential “DDOS” attack.

**Australian Travel agency attack due to publicly exposed AWS bucket**
In January 2025, the Australian travel agency was attacked, which led to the breach of 112,000 records from the company's non-password-protected database with a size of 26.8GB, including details such as passport images, travel visas, travel itineraries and tickets, and partial credit card numbers of customers. Spreadsheets containing detailed information of more than 13,000 customers, which included their names, email addresses, trip costs, and destinations, were discovered to have been leaked. While most impacted travelers are Australians, customers from New Zealand, Ireland, and Britain have also been affected.

The breach was due to a publicly exposed Amazon AWS Cloud Storage bucket that was incorrectly configured. These attacks usually begin with searching for exposed systems or misconfigured cloud storage. Tools or scripts were used to scan for open S3 buckets or cloud storage services (e.g., Bucket Finder, S3Scanner, Shodan, Censys, or Grayhat Warfare). Threat actors also leverage keyword-based automations to look for files like passwords.txt, .env, db_backup.sql, etc.

**A major Air Traffic Control State-Sponsored Threat Actor Attack**
In August 2024, the German Air Traffic Control’s administrative IT infrastructure, which handles internal office communications, was attacked. This allowed unauthorized access to sensitive data. Fancy Bear (aka APT28), a threat actor attributed to Russia’s military intelligence service, was attributed to this attack.

**A major European countries’ transport department Credential Access and Privilege Escalation Attack**
In September 2024, Transport for London was hit with a cyber attack, which caused them to temporarily suspend applications for access cards due to concerns over system security.

This also affected the ability to register new cards, issue refunds for incomplete pay-as-you-go journeys made using contactless cards, and improve the booking system for the Dial-a-Ride service. Also, the live travel data feed was impacted. While pre-existing bookings were honored, new bookings could only be made by phone until the system was restored. Data on 5,000 people was accessed, including names, contact details, and Oyster card refund data. This included bank account numbers and sort codes.

Attackers reportedly used LicensingUI.exe (a signed Windows binary) to execute payloads. TfL had to reset 30,000 employee passwords in person, indicating the scale of the breach. The threat actor may have established persistence and elevated privileges, possibly using scheduled tasks or admin tokens.

**Major US Airport Ransomware Attack**
In September 2024, several critical systems at A major US Airport were affected due to a cyber attack attributed to Rhysida affiliates.

Delays in luggage processing led to bags being delivered to travelers well after arrival. Due to system outages, passengers had to use handwritten boarding passes. Internal port systems were encrypted, hindering the restoration process.

The threat actors accessed and downloaded some personal information from previously used Port systems for employee, contractor, and parking data (90000 individuals). The downloaded information included names, dates of birth, Social Security numbers (or the last four digits of Social Security numbers), driver’s license or other government identification card numbers, and medical information.

Rhysida actors operate in a Ransomware-as-a-service (RaaS) capacity, where ransomware tools and infrastructure are leased out in a profit-sharing model. Rhysida actors have been observed leveraging external-facing remote services to access and persist within a network initially. They have also been observed authenticating to internal VPN access points with compromised valid credentials, notably because organizations lack MFA enabled by default. Additionally, they have been observed exploiting Zerologon - a critical elevation of privileges vulnerability in Microsoft’s Netlogon Remote Protocol- and conducting successful phishing attempts.

**Major Asian Airline Potential DDoS Attack**
In December 2024, a major Asian airline was the victim of a cyber attack that caused flight delays. While the airline did not publicly identify the specific threat actor, it confirmed that no customer data was leaked or computer viruses were detected. The incident involved a surge in traffic, suggesting a DDoS attack, which disrupted the airline's systems and ticket sales.

**A Major European Airline Web Skimming Attack**
In October 2023, IncRansom (A Russian Hacking Group) gained unauthorized access to the airline's payment system. While the method of the attack has not been confirmed, it is most likely through web skimming.

The breach exposed sensitive customer data, including credit card information such as card numbers, expiration dates, and CVV codes. The airline promptly notified affected customers and advised them to cancel their cards to prevent potential fraudulent use. In March 2024, the airline updated its disclosure, revealing that additional personal information, such as names, ID or passport numbers, dates of birth, phone numbers, email addresses, and nationalities, had been exposed.

![Figure 2: Screenshot from INCRansomware DLS affecting European Airline]

**A major resort Social Engineering and Ransomware Cyber Attack**
In September 2023, A major US resort chain was affected by a cyber attack, a combined effort of Scattered Spider and ALPHV.

Scattered Spider members researched the company’s employees on LinkedIn to gather information. They impersonated an employee and convinced the IT help desk to provide login credentials. With these, the attackers gained administrator access to the resort’s Okta and Azure environments, allowing them to move laterally within the systems. ALPHV then deployed ransomware across several VMware ESXi hypervisor servers.

These servers hosted thousands of virtual machines that supported critical hospitality systems such as gaming machines, online reservation systems, digital room keys, and websites. ALPHV also claims to have exfiltrated 6 TB of customer information during this time, upon which they initiated negotiations with the resort to prevent the public release of the stolen data.

**French travel agency Ransomware Attack**
In May 2023, Lockbit attacked a French travel agency. Following the agency's refusal to pay the ransom, LockBit published approximately 7,000 to 10,000 passport photocopies on the dark web. These documents were collected from clients participating in group travel, constituting about 2% of the agency's customer base. Lockbit works through a RaaS (Ransomware as a Service) model. Please refer to the appendix for their TTPs.

### Top 10 Most Critical TTPs in this Sector

![Figure 3: List of Top 10 TTPs associated with Tour Operations and Travel Sector]

| ID | Technique Name |
| :--- | :--- |
| T1078 | Valid Accounts |
| T1190 | Exploit Public-Facing Application |
| T1059 | Command and Scripting Interpreter |
| T1566 | Phishing |
| T1027 | Obfuscated Files or Information |
| T1055 | Process Injection |
| T1003.003 | LSASS Memory Dumping |
| T1021.001 | Remote Desktop Protocol (RDP) |
| T1112 | Modify Registry |
| T1486 | Data Encrypted for Impact |

---

## Trend Predictions

### 1. Surge in DDoS attacks targeting booking and ticketing systems
The Major attacks in march 2025 and December 2024 highlight critical attacks that involved DDoS campaigns that disrupted crucial booking and ticketing systems, causing operational delays and customer dissatisfaction. These attacks exploited the travel industry’s reliance on real-time online platforms/systems.

In the future, threat actors will likely continue deploying DDoS attacks to overwhelm booking systems or airline ticketing platforms with the aim of disrupting peak travel seasons (e.g., holidays). In addition to rising geopolitical tensions, nation-state-sponsored cyber attacks will likely also become more frequent and sophisticated with the aim to disrupt critical infrastructure and financial systems aimed at destabilizing economies.

Attackers will likely leverage botnets enhanced by AI-driven traffic amplification to bypass traditional DDoS defenses. In aviation, around 1/4 of incidents stem from vendor vulnerabilities, offering threat actors avenues to amplify traffic surges using AI-driven botnets. Smaller travel agencies with limited cyber security budgets could be particularly vulnerable, facing downtime and revenue losses.

If this trend continues, there could be a rise in extortion schemes where attackers demand ransoms to halt DDoS campaigns, exploiting the sector’s need for uninterrupted service. This tactic was seen in another sector with a 2024 healthcare ransomware attack, where BlackCat/ALPHV demanded millions to restore critical systems, highlighting the profitability of targeting time-sensitive operations. This ultimately would demand a need for the sector to invest in cloud-based DDoS protection, audit vendor security, and stress-test booking platforms.

### 2. Increased data breaches via misconfigured cloud storage
In 2025, an Australian travel company experienced a significant data breach when a cloud storage bucket on AWS was left publicly accessible without a password. As a result, over 112,000 customer records were exposed—including scanned passports and partial credit card numbers. This incident illustrates a major vulnerability affecting the broader travel and tourism industry: misconfigured cloud storage systems.

Threat actors are increasingly automating the discovery and exploitation of misconfigured cloud storage—particularly on platforms like AWS and Azure. Tools such as Bucket Finder, S3Scanner, and search engines like Shodan and Censys allow attackers to easily locate publicly accessible buckets. Once identified, overly permissive permissions (e.g., READ, LIST, or WRITE) are exploited to anonymously access or alter stored data. Attackers then deploy keyword-based scripts using AWS CLI or boto3 to hunt for sensitive files such as .env, passwords.txt, or db_backup.sql. If HTTPS is not enforced, the data can even be exfiltrated over unencrypted channels.

As the travel and tourism industry continues its shift to cloud infrastructure, particularly among small to mid-sized operators lacking robust cyber security controls, misconfigured cloud storage will remain one of the most exploited vulnerabilities. The use of automated scanning tools and AI-driven search tactics will only accelerate, allowing attackers to identify and extract valuable data at scale. We can expect an increase in targeted extortion and data-leak-based fraud, pushing regulatory bodies to tighten compliance standards and forcing businesses to implement continuous configuration audits, strict access controls, and end-to-end encryption policies.

### 3. Phishing campaigns exploiting employee credentials
The 2023 attack on a major US resort revealed a rising threat pattern: phishing and impersonation attacks are being used as the entry point to compromise internal systems. Threat actor Scattered Spider successfully posed as an employee after researching LinkedIn profiles, convincing IT help desk staff to hand over credentials, and deploying ransomware that crippled operational systems.

In 2025, we can expect a surge in AI-powered phishing campaigns specifically targeting frontline and support staff at travel agencies, airlines, and airport operators. This is especially critical with over 70% of attacks in the aviation sector focused on stealing login details and unauthorized IT infrastructure access. Attackers will use AI-generated emails mimicking trusted vendors or executives, as seen in The above’s case, to trick staff into providing access to systems like reservation platforms or payment gateways.

The travel sector’s high employee turnover and remote work trends will increase vulnerabilities. Potential increases in double-extortion tactics, where stolen customer data (e.g., passports, credit cards) are leaked if ransoms are unpaid could evolve.

Phishing attacks have long been a favored tactic among cyber criminals and with the integration of generative AI, these attacks are poised to become significantly more sophisticated. Attackers will leverage AI to craft highly personalized phishing emails, texts, or social media messages, tailored to individual targets by analyzing publicly available data. Additionally, sophisticated phishing websites are increasingly being supplemented with AI-powered chatbots. These chatbots mimic support personnel with human-like language, similar typing speeds, and dynamic content generation, making it challenging to discern their authenticity.

Newer AI speech models also enable highly convincing speech imitation. This capability provides criminals with further social engineering opportunities through phishing calls, where they can impersonate support staff, bankers, and other authoritative figures to gain access to private information or systems. Moreover, these AI tools also provide non-English-speaking Threat Actors an opportunity to target U.S personnel with higher chances of success.

### 4. Supply chain attacks via third-party vendors
The breach of a major European Airline in 2024 likely involved web skimming through a compromised payment system, exposing credit card details and personal information. Similarly, 2024 US airport attack underscored third-party system vulnerabilities, with Rhysida affiliates gaining access to employee and contractor data. These incidents reflect a broader trend: the exploitation of public-facing applications (T1190) and supply chain weaknesses that expose high-value systems in the travel sector.

With the growing dependence on cloud services and multi-vendor ecosystems, attackers are likely to continue exploiting the weakest links in digital supply chains. In 2025, supply chain attacks targeting third-party vendors, such as payment processors, booking platforms, and identity verification services, could escalate. Adversaries may focus on infiltrating smaller, less secure vendors as entry points to compromise larger travel organizations. Once inside, attackers often capture input data (T1056), extract sensitive customer or financial information from internal systems and repositories (T1213), and exfiltrate it via trusted web services or cloud platforms (T1048.003), which helps them evade traditional security detection.

These attacks have the potential to result in large-scale data exfiltration, financial fraud, and operational disruption, especially for companies relying on outdated vendor software, which increases exposure to zero-day vulnerabilities. Threat actors are also expected to continue opportunistically targeting organizations with weak supply chain defenses, capitalizing on businesses' lack of control over their third-party partners.

The European Network and Information Security Agency (ENISA) has flagged supply chain risks as a growing concern, highlighting their stealthy nature, complexity, and wide-reaching consequences. Many organizations across sectors remain underprepared for these threats. The travel industry is particularly vulnerable due to its heavy reliance on cloud platforms and intricate vendor ecosystems.

Additionally, more organizations are adopting AI large-language models (LLMs) at increasing rates during 2024, and more are expected to join throughout 2025. Threat Actors are aware of this new trend and are seeking to exploit it by carrying out data poisoning attacks on training models that LLMs are based on.

---

## Cyberint, Now a Check Point Company Solutions

Given the recent emerging threat trends, it’s essential to understand the range of services Cyberint offers to help safeguard against these risks.

Cyberint, now a Check Point Company monitors various assets, including domains, emails, external IP addresses, high-impact employees, and more. Each asset is carefully configured to meet crucial needs as security teams maneuver the many challenges they face throughout the year.

These assets are monitored daily in the Cyberint solution through attack surface monitoring (ASM) automation, threat intelligence gathering, phishing detection, and dedicated analyst collaboration.

### Attack Surface Monitoring
The Attack Surface Monitoring module in the Cyberint solution performs non-intrusive, daily, and weekly scans on the following categories of assets:
- Domains
- Subdomains
- IP Addresses
- Azure Data Lake / Storage Blobs
- Google Cloud Storage
- Amazon S3 Buckets

Automated technologies continuously monitor daily exposure, vulnerable configurations, exploitable or open ports, and other potential exposure items. When an issue is detected, an alert is automatically generated and sent to the alerts module, where the team can review and determine the appropriate next steps.

This daily scan is imperative for monitoring potential vulnerabilities on external-facing assets, especially Amazon S3 buckets, as it directly relates to the aforementioned ticketing system Cyber Attack, in which threat actors accessed an incorrectly configured cloud storage bucket.

The Attack Surface Monitoring (ASM) module provides continuous visibility into a wide range of digital assets through non-intrusive daily and weekly scans. It identifies vulnerabilities, misconfigurations, and exposed services across domains, IPs, and cloud storage, while leveraging public data and optional cloud integrations to uncover associated assets that may not be directly provided.

### Threat Intelligence Monitoring

**Phishing Detection**
Under Cyberint’s phishing protection, core domain assets can be flagged for both Threat Intelligence and Attack Surface Monitoring, enabling automatic detection of suspicious lookalike domains.

To supplement the automation, Cyberint, now a Check Point Company’s Phishing Beacon proactively identifies phishing sites by embedding a nonintrusive script within the protected website. It alerts us when malicious actors attempt to clone that same site on unauthorized domains.

**Threat Hunting**
Threat intelligence monitoring is strengthened through the strategic designation of key assets. Once identified, these assets are continuously monitored across a broad range of intelligence sources, including underground forums, code repositories, and social media, to surface potential risks. The dedicated analyst reviews collected intelligence daily and notifies relevant security teams of any relevant threats.

Additionally, the analyst team at Cyberint, now a Check Point Company constantly consume a variety of reports that allow us to adapt continuously to the ever-evolving threat landscape as it pertains to specific industries and makes recommendations on best practices to mitigate emerging threats.

**Supply Chain Monitoring**
Additionally, supply chain monitoring is a service Cyberint, now a Check Point Company offers that would allow for the addition of specific third-party vendors used by the customer organization to be continuously monitored and, if detected, automate alerts pertaining to:
- Supply Chain Vendor name mentions in Darknet forums
- Supply Chain Vendor name mentions in breaches
- A Vendor suffering from an ongoing ransomware attack
- Emerging phishing campaign related to the supply chain vendor
- Supply Chain Vendor Source Code Leaked
- Supply Chain Vendor Offered for Sale

Continuous monitoring of third-party vendors is essential because their systems and security practices can directly impact on the organization’s risk exposure.

### Dedicated Analyst Services
The analyst provides many services alongside daily threat monitoring and alerting. The dedicated analyst is considered the expert of the Cyberint Solution, looking to maximize the platform's use and ensure that all modules are running efficiently and as intended.

Some tasks the analysts perform to fine-tune the solution on an ongoing basis include:
- **Asset Configuration**: The analyst ensures that each asset received is configured to meet the customer's needs.
- **Asset Updating**: Incrementally, the analyst requests updates for to ensure up-to-date coverage.
- **Environment Metrics Monitoring**: Analysts monitor automation and alerts to suggest ways to tune the environment to meet customer needs.
- **Alert Configuration**: Analysts review alerting like such as closure reasons and customer feedback to make suggestions on alert configurations (i.e; disablements, severity overrides, corporate password policy tuning).

The dedicated analyst also holds regular meetings—typically monthly, to present key alerts and discussion points, providing customers with clear insight into the most impactful findings and the overall value of the analyst’s ongoing efforts.

---

## Conclusions and Recommendations

### Conclusions
The travel industry is facing an evolving external threat landscape, driven by enhanced DDoS attacks, phishing campaigns, cloud misconfigurations, and supply chain compromises. As attackers adapt, so must travel organizations' defensive strategies, particularly in how they understand and respond to threats beyond their internal perimeters.

As an important external threat intelligence monitoring partner, Cyberint, now a Check Point Company is positioned to play a critical role in strengthening cyber resilience by delivering timely, relevant, and actionable insights.

By combining real-time intelligence collection, external attack surface visibility, and analyst-driven insights, Cyberint, now a Check Point Company helps anticipate and mitigate cyber threats before they impact operations. In a sector as time-sensitive and customer-facing as travel, having a partner focused on what’s happening beyond the company’s firewall is no longer optional, it’s essential.

### Recommendations

**1. Defending Against DDoS Attacks on Booking and Ticketing Systems**
- Use Cyberint to Monitor for pre-attack chatter across underground forums, Telegram channels, and botnet markets where DDoS campaigns are planned or advertised.
- Track mentions of your core platforms and digital infrastructure to detect early warning signs of potential targeting.
- Implement DDoS Prevention Mechanism: enforce cloud-based DDoS protection, audit vendor security, and stress-test booking platforms.

**2. Preventing Data Breaches from Misconfigured Cloud Storage**
- Use Cyberint to Monitor for exposed data linked to your brand or customers across breach forums, paste sites, and searchable repositories.
- Use Cyberint to Enforce Monitoring for configuration-related leaks, such as .env, .bak, or backup files detected in threat actor dumps or public buckets.
- Utilize Cyberint’s ASM (Attack Surface Monitoring) Detection to continuously scan for newly exposed cloud assets, misconfigured storage, and unauthorized changes to your cloud footprint.

**3. Mitigating AI-Powered Phishing and Credential Harvesting**
- Enforce Monitoring for impersonation of your brand, executives, or customer support teams across social media, domain registrations, and phishing kits.
- Enforce Early phishing infrastructure Monitoring through lookalike domains and cloned sites using our phishing detection.

**4. Monitoring Third-Party Risk and Supply Chain Exploitation**
- Continuously monitor vendor ecosystems for compromise indicators, leaked credentials, or data mentioning your organization via third-party connections.
- Track sector-specific supply chain breaches and provide contextual threat intelligence to assess if your environment is indirectly impacted.
- **Block IOCs**: To protect your internal systems, we recommend importing the provided IOC list into your endpoint protection platform and configuring it to block or quarantine any matching threats. Additionally, apply the IPs and domains to your internal DNS or host-based firewall policies to prevent communication with known malicious infrastructure.

---

## Appendix

### Consolidated TTP List

| Technique ID | Technique Name |
| :--- | :--- |
| T1003.003 | Security Account Manager (SAM) |
| T1005 | Data from Local System |
| T1012 | Query Registry |
| T1016 | System Network Configuration Discovery |
| T1018 | Remote System Discovery |
| T1021 | Remote Services |
| T1021.001 | Remote Desktop Protocol |
| T1021.002 | SMB/Windows Admin Shares |
| T1021.004 | SSH |
| T1027 | Obfuscated Files or Information |
| T1033 | System Owner/User Discovery |
| T1047 | Windows Management Instrumentation |
| T1048.003 | Exfiltration Over Alternative Protocol: SMB/Windows Admin Shares |
| T1055 | Process Injection |
| T1055.002 | Portable Executable Injection |
| T1056 | Input Capture |
| T1056.004 | Credential API Hooking |
| T1057 | Process Discovery |
| T1059 | Command and Scripting Interpreter |
| T1059.001 | PowerShell |
| T1059.003 | Windows Command Shell |
| T1069.001 | Permission Groups Discovery: Local Groups |
| T1069.002 | Permission Groups Discovery: Global Groups |
| T1070.001 | Indicator Removal from Tools: File Deletion |
| T1070.004 | Indicator Removal from Tools: File System Metadata Deletion |
| T1071 | Application Layer Protocol |
| T1078 | Valid Accounts |
| T1087.002 | Account Discovery: Domain Account |
| T1110 | Brute Force |
| T1112 | Modify Registry |
| T1190 | Exploit Public-Facing Application |
| T1210 | Exploitation for Privilege Escalation |
| T1213 | Data from Information Repositories |
| T1219 | Remote Access Tools |
| T1482 | Domain Trust Discovery |
| T1486 | Data Encrypted for Impact |
| T1497 | Virtualization/Sandbox Evasion |
| T1530 | Data from Cloud Storage Object |
| T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder |
| T1548 | Abuse Elevation Control Mechanism |
| T1564.003 | Hide Artifacts: Hidden Files and Directories |
| T1566 | Phishing |
| T1567 | Exfiltration Over Web Service |
| T1567.002 | Exfiltration Over Web Service: Web Shell |
| T1580 | Data from Local System |
| T1587 | Acquire Infrastructure |
| T1589 | Gather Victim Identity Information |
| T1595 | Active Scanning |
| T1596.001 | Gather Victim Host Information: System Information Discovery |
| T1657 | Application Layer Protocol: Web Protocols |

### IOCS By Threat Actor

*(Note: Due to the extensive nature of the IOC tables provided in the source document, please refer to the original report pages 26-37 for the full list of hashes, IP addresses, and email indicators associated with Rhysida, Lockbit, IncRansom, Fancy Bear, and ALPHV.)*

### External References Outside of Cyberint
1. https://blog.netwrix.com/mgm-cyber-attack
2. https://www.reuters.com/technology/cybersecurity/iag-flags-air-europas-customers-personal-data-leak-wsj-reports-2024-03-21/
3. https://apnews.com/article/japan-jal-cyberattack-flights-travel-04fbd4848f3015a77057339a5c90ca32
4. https://apnews.com/article/seattle-airport-cyberattack-ransomware-rhysida-95cd980a9f45112f0fdce488233eec9c
5. https://www.theguardian.com/uk-news/article/2024/sep/02/transport-for-london-dealing-with-cyber-attack
6. https://www.voyageursdumonde.fr/voyage-sur-mesure/Img/institutionnel/info-fi/data/2023/PR_Voyageurs_du_Monde_17.5.2023.pdf
7. https://www.skynews.com.au/australia-news/australian-travel-agency-hit-by-data-breach-leaking-passport-and-travel-details-of-thousands-of-customers/news-story/73072684e13a253e315d326b916280c1
8. https://icsstrive.com/incident/aerticket-suffers-cyberattack-causing-technical-failures/
9. https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a
10. https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a
11. https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-108
12. https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-110a
13. https://www.sentinelone.com/anthology/inc-ransom/
14. https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a

---

## Contact us

**ISRAEL**
Tel: +972-73-226-4555
5 Shlomo Kaplan Street, Tel Aviv 6789159

**USA**
Tel: 1-800-429-4391
100 Oracle Parkway, Suite 800, Redwood City, CA 94065

**SINGAPORE**
Tel: +65-6435-1318
78 Shenton Way, #09-01 Tower 1, Singapore 079120

**PHILIPPINES**
Tel: +63 2 8465 9200
Unit 2005, 20th Floor, Zuellig Building, Makati Avenue, corner Paseo de Roxas, Makati City 1223, Metro Manila

**UK AND IRELAND**
Tel: +44 20 7628 4211
85 London Wall, 4th Floor, London, EC2M 7AD

**JAPAN**
Tel: +81-3-6205-8340
Toranomon Kotohira Tower 25F, 1-2-8, Toranomon Minato-ku, Tokyo 105-0001

**ABOUT CYBERINT**
Cyberint, now a Check Point company, reduces risk by helping organizations detect and mitigate external cyber threats before they have an adverse impact. For more information visit: https://cyberint.com / checkpoint.com/erm

© Cyberint, 2025. All Rights Reserved.