# Travel & Tour Operations Industry Threat Landscape Report

**Organization:** Cyberint  
**Year:** 2025  
**Authors:** Josh Puentes, Manasa Pisipati, and Ben Johnathan Neeman  
**Date:** May 2025

## Table of Contents
- [Executive Summary](#executive-summary)
- [Cyber Incidents](#cyber-incidents)
- [Timeline of Notable Events](#timeline-of-notable-events)
- [Cyber Incidents Details](#cyber-incidents-details)
- [Top 10 Most Critical TTPs in this Sector](#top-10-most-critical-ttps-in-this-sector)
- [Trend Predictions](#trend-predictions)
- [Cyberint, Now a Check Point Company Solutions](#cyberint-now-a-check-point-company-solutions)
- [Conclusions and Recommendations](#conclusions-and-recommendations)
- [Appendix](#appendix)

---

## Executive Summary
Cyberint, now a Check Point Company, conducted a threat landscape report focusing on the Travel and Tour Operation Industry. The following report outlines recent cyber events, cyber threat predictions, and an overview of Cyberint services as a solution to mitigating digital threats.

From 2023 to 2025, the global travel sector faced a surge in targeted cyber attacks, including DDoS disruptions, ransomware incidents, data breaches via misconfigured cloud storage, and third-party supply chain compromises. The report includes an outline of events spanning worldwide. It also includes a list of the prominent TTPs (tools and techniques) relating to the attackers and a list of related IOCs that should be noted and blocked.

Below are the trend predictions Cyberint, now a Check Point Company anticipates, based on the related incidents:

- **DDoS Attacks Disrupting Booking Systems**: These attacks are often timed to peak travel periods and exploit the industry's reliance on real-time online services.
- **Data Breaches via Misconfigured Cloud Storage**: Attackers are increasingly using advanced tools and automated scripts to identify and exfiltrate data from exposed cloud storage.
- **Phishing and Credential Exploitation**: Attackers are using advanced social engineering techniques, including impersonation and AI-generated phishing lures, to harvest employee credentials.
- **Supply Chain Compromise and Third-Party Risks**: Threat actors are bypassing hardened perimeters by targeting vendors in payment processing, authentication, and cloud infrastructure.

---

## Cyber Incidents

### Timeline of Notable Events
![Figure 1: Timeline of Cyber Attacks Covered in this Report]

### Cyber Incidents Details

**A professional air ticket consolidator DDoS Attack**  
In March 2025, a cyber attack disrupted a professional air ticket consolidator’s operations. Their booking system was impacted due to a potential DDoS attack.

**Australian Travel agency attack due to publicly exposed AWS bucket**  
In January 2025, an Australian travel agency suffered a breach of 112,000 records (26.8GB) from a non-password-protected database, including passport images, visas, itineraries, and partial credit card numbers. The breach was due to a publicly exposed Amazon AWS Cloud Storage bucket.

**A major Air Traffic Control State-Sponsored Threat Actor Attack**  
In August 2024, the German Air Traffic Control’s administrative IT infrastructure was attacked by Fancy Bear (APT28), allowing unauthorized access to sensitive data.

**A major European countries’ transport department Credential Access and Privilege Escalation Attack**  
In September 2024, Transport for London (TfL) was hit with a cyber attack, impacting booking systems and access card registrations. Attackers used `LicensingUI.exe` to execute payloads, necessitating a reset of 30,000 employee passwords.

**Major US Airport Ransomware Attack**  
In September 2024, critical systems at a major US Airport were encrypted by Rhysida affiliates. The breach exposed personal information of 90,000 individuals, including Social Security numbers and medical information.

**Major Asian Airline Potential DDoS Attack**  
In December 2024, a major Asian airline experienced flight delays due to a surge in traffic, suggesting a DDoS attack.

**A Major European Airline Web Skimming Attack**  
In October 2023, IncRansom gained unauthorized access to an airline's payment system, likely via web skimming, exposing credit card data and personal identification details.
![Figure 2: Screenshot from INCRansomware DLS affecting European Airline]

**A major resort Social Engineering and Ransomware Cyber Attack**  
In September 2023, a major US resort chain was targeted by Scattered Spider and ALPHV. Attackers used social engineering to gain administrator access to Okta and Azure environments, subsequently deploying ransomware across VMware ESXi servers.

**French travel agency Ransomware Attack**  
In May 2023, Lockbit attacked a French travel agency, publishing 7,000 to 10,000 passport photocopies on the dark web after the agency refused to pay the ransom.

---

## Top 10 Most Critical TTPs in this Sector
![Figure 3: List of Top 10 TTPs associated with Tour Operations and Travel Sector]

1. **Valid Accounts (T1078)**: Used for persistence and evasion.
2. **Exploit Public-Facing Application (T1190)**: Common initial access point.
3. **Command and Scripting Interpreter (T1059)**: Core execution method.
4. **Phishing (T1566)**: Widely used for initial access.
5. **Obfuscated Files or Information (T1027)**: Used to avoid detection.
6. **Process Injection (T1055)**: Critical for evading AV/EDR.
7. **LSASS Memory Dumping (T1003.003)**: Credential harvesting.
8. **Remote Desktop Protocol (RDP) (T1021.001)**: Lateral movement.
9. **Modify Registry (T1112)**: Disable protections/persistence.
10. **Data Encrypted for Impact (T1486)**: Core ransomware activity.

---

## Trend Predictions
1. **Surge in DDoS attacks targeting booking and ticketing systems**: Expected rise in extortion schemes leveraging AI-driven botnets.
2. **Increased data breaches via misconfigured cloud storage**: Continued exploitation of S3 buckets using automated scanning tools.
3. **Phishing campaigns exploiting employee credentials**: Rise in AI-powered phishing and voice imitation targeting support staff.
4. **Supply Chain Attacks via Third-Party Vendors**: Exploitation of smaller, less secure vendors to infiltrate larger organizations.

---

## Cyberint, Now a Check Point Company Solutions
Cyberint provides continuous monitoring of domains, emails, external IP addresses, and high-impact employees.
- **Attack Surface Monitoring (ASM)**: Daily scans of domains, subdomains, and cloud storage (AWS, Azure, Google Cloud).
- **Threat Intelligence Monitoring**: Phishing detection via "Phishing Beacon" and monitoring of underground forums/code repositories.
- **Supply Chain Monitoring**: Alerts for vendor mentions in breaches, ransomware attacks, or leaked source code.
- **Dedicated Analyst Services**: Expert configuration and tuning of the Cyberint solution to meet specific organizational needs.

---

## Conclusions and Recommendations
The travel industry must shift toward proactive, external-facing threat intelligence. 
- **Recommendations**:
    - Implement cloud-based DDoS protection and stress-test platforms.
    - Conduct continuous configuration audits for cloud storage.
    - Enforce monitoring for brand impersonation and lookalike domains.
    - Monitor third-party vendor ecosystems for compromise indicators.
    - Block provided IOCs in endpoint protection and firewall policies.

---

## Appendix
*(The appendix contains a comprehensive list of TTPs and detailed IOC tables for threat actors including Rhysida, Lockbit, IncRansom, Fancy Bear, and ALPHV. Please refer to the original document for the full technical tables.)*

[^1]: Note: This document is a conversion of the provided technical report. All technical terms and data points have been preserved.

---

mresorts-okta[.]com       | Phishing domain                |
| IP         | 99.25.84[.]9                | Observed IP in campaigns       |
| IP         | 144.76.136[.]153            | Observed IP in campaigns       |
| Ransomware | BlackCat/ALPHV              | Used by group                  |
| Ransomware | RansomHub                   | Used by group                  |
| Ransomware | Qilin                       | Used by group                  |
Travel & Tour Operations Industry Threat Landscape         36

EXTERNAL REFERENCES OUTSIDE OF CYBERINT
1. https://blog.netwrix.com/mgm-cyber-attack
2. https://www.reuters.com/technology/cybersecurity/iag-flags-air-europas-customers-person
al-data-leak-wsj-reports-2024-03-21/
3. https://apnews.com/article/japan-jal-cyberattack-flights-travel-04fbd4848f3015a77057339a5
c90ca32
4. https://apnews.com/article/seattle-airport-cyberattack-ransomware-rhysida-95cd980a9f451
12f0fdce488233eec9c
5. https://www.theguardian.com/uk-news/article/2024/sep/02/transport-for-london-dealing-wit
h-cyber-attack
6. https://www.voyageursdumonde.fr/voyage-sur-mesure/Img/institutionnel/info-fi/data/2023/P
R_Voyageurs_du_Monde_17.5.2023.pdf
7. https://www.skynews.com.au/australia-news/australian-travel-agency-hit-by-data-breach-le
aking-passport-and-travel-details-of-thousands-of-customers/news-story/73072684e13a253
e315d326b916280c1
8. https://icsstrive.com/incident/aerticket-suffers-cyberattack-causing-technical-failures/
9. https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a
10. https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a
11. https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-108
12. https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-110a
13. https://www.sentinelone.com/anthology/inc-ransom/
14. https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a
Travel & Tour Operations Industry Threat Landscape 37

CONTACT US
ISRAEL USA
Tel: +972-73-226-4555 Tel: 1-800-429-4391
5 Shlomo Kaplan Street 100 Oracle Parkway, Suite 800
Tel Aviv 6789159 Redwood City, CA 94065
PHILIPPINES
SINGAPORE
Tel: +63 2 8465 9200
Tel: +65-6435-1318
Unit 2005, 20th Floor, Zuellig Building,
78 Shenton Way, #09-01 Tower 1,
Makati Avenue, corner Paseo de Roxas
Singapore 079120
Makati City 1223, Metro Manila
UK AND IRELAND JAPAN
Tel: +44 20 7628 4211 Tel: +81-3-6205-8340
85 London Wall, 4th Floor, Toranomon Kotohira Tower 25F,
London, EC2M 7AD 1-2-8, Toranomon Minato-ku, Tokyo 105-0001
ABOUT CYBERINT
Cyberint, now a Check Point company, reduces risk by helping organizations detect and mitigate
external cyber threats before they have an adverse impact. The Check Point External Risk
Management solution provides superior visibility through continuous discovery of the evolving
attack surface, combined with the automated collection and analysis of vast quantities of
intelligence from across the open, deep and dark web. A team of global military-grade
cybersecurity experts work alongside customers to rapidly detect, investigate, and disrupt relevant
threats – before they have the chance to develop into major incidents. Global customers, including
Fortune 500 leaders across all major market verticals, rely on Check Point External Risk
Management to protect themselves from an array of external risks, including vulnerabilities,
misconfigurations, phishing, impersonation attacks, malware infections, exposed credentials, data
leaks, fraud, and 3rd party risks.
For more information visit: https://cyberint.com / checkpoint.com/erm
© Cyberint, 2025. All Rights Reserved.
Travel & Tour Operations Industry Threat Landscape 38