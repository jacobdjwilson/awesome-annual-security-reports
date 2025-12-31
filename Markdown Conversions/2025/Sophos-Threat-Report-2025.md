# The Sophos Annual Threat Report: Cybercrime on Main Street 2025

## Table of Contents
- [Introduction](#introduction)
- [A word about our data](#a-word-about-our-data)
- [Broken Windows (and gateways)](#broken-windows-and-gateways)
- [STACs: Packaged playbooks, tactics, tools and procedures](#stacs-packaged-playbooks-tactics-tools-and-procedures)
- [Trends in cybercrime techniques, tactics and practices](#trends-in-cybercrime-techniques-tactics-and-practices)
  - [Remote ransomware continues to grow](#remote-ransomware-continues-to-grow)
  - [Social engineering via Teams vishing](#social-engineering-via-teams-vishing)
  - [MFA phishing](#mfa-phishing)
  - [Adversarial AI usage](#adversarial-ai-usage)
  - [Quishing](#quishing)
  - [Malvertising and SEO poisoning](#malvertising-and-seo-poisoning)
  - [EDR killers](#edr-killers)
- [Conclusion](#conclusion)
- [Acknowledgements](#acknowledgements)
- [About the authors](#about-the-authors)
- [Read Similar Articles](#read-similar-articles)

## Introduction

The Sophos Annual Threat Report: Cybercrime on Main Street 2025

Ransomware remains the biggest threat, but odd and misconfigured network devices are making it too easy

April 16, 2025

Written by Sean Gallagher

Security Operations
Threat Research
Annual Threat Report
Featured
midsize businesses
small businesses

Small businesses are a prime target for cybercrime, as we highlighted in our past annual report. Many of the criminal threats we covered in that report remained a major menace in 2024, including ransomware–which remains a primary existential cyber threat to small and midsized organizations.

Ransomware cases accounted for 70 percent of Sophos Incident Response cases for small business customers in 2024—and over 90 percent for midsized organizations (from 500 to 5000 employees). Ransomware and data theft attempts accounted for nearly 30 percent of all Sophos Managed Detection and Response (MDR) tracked incidents (in which malicious activity of any sort was detected) for small and midsized businesses.

While ransomware attacks overall have declined slightly year over year, the cost of those attacks overall has risen, based on data from Sophos' State of Ransomware report. And though many of the threats observed in 2024 were familiar in form, other data-focused threats continue to grow, and new tactics and practices have emerged and evolved:

*   Compromised network edge devices—firewalls, virtual private network appliances, and other access devices—account for a quarter of the initial compromises of businesses in cases that could be confirmed from telemetry, and is likely much higher.
*   Software-as-a-service platforms, which were widely adopted by organizations during the COVID pandemic to support remote work and to improve overall security posture, continue to be abused in new ways for social engineering, initial compromise, and malware deployment.
*   Business email compromise activity is a growing proportion of the overall initial compromises in cybersecurity incidents—leveraged for malware delivery, credential theft, and social engineering for a variety of criminal purposes.
*   One of the drivers of business email compromise is the phishing of credentials with adversary-in-the-middle multifactor authentication (MFA) token capture, a constantly evolving threat.
*   Fraudulent applications carrying malware, or tied to scams and social engineering through SMS and messaging applications, lead to mobile threats for small and midsize businesses.
*   Other less-technical threats leveraging the network continue to be a threat to small businesses, again with evolving patterns of scams.

This report focuses on the trends seen in cybercriminal attack patterns faced by small and midsized organizations. Details of malware and abused software most frequently encountered in endpoint detections and incidents is provided in an appendix to this report, which can be found here.

## Table of Contents
- A word about our data
- Broken Windows (and gateways)
- STACs: Packaged playbooks, tactics, tools and procedures
- Trends in cybercrime techniques, tactics and practices
  - Remote ransomware continues to grow
  - Social engineering via Teams vishing
  - MFA phishing
  - Adversarial AI usage
  - Quishing
  - Malvertising and SEO poisoning
  - EDR killers
- Conclusion
- Appendix: Tools of the trade—most frequently encountered malware and abused software
  - Dual-use tools
  - Attack tools
  - Information stealers
  - Top ransomware threats
    - LockBit, sort of
    - Akira and Fog
    - RansomHub

## A word about our data

The data used in our Annual Threat Report analysis comes from the following sources:

*   **Customer reports**—this consists of detection telemetry from Sophos endpoint software running on customers' networks, which gives a broad view of threats encountered, and analyzed within SophosLabs (in this report, referred to as endpoint detection data).
*   **Incident data**—this consists of both data gathered in the course of escalations driven by detection of malicious activity on MDR customers' networks, data gathered by MDR Incident Response from customer incidents, and data gathered by Sophos Incident Response from incidents on customer networks for organizations of 500 employees or fewer where there was little or no managed detection and response protection in place. These datasets are treated as a combined set of incident data in this report.

SecureWorks incident and detection data is not included in this report, as it was based on pre-acquisition telemetry.

All data is from the 2024 calendar year, unless otherwise noted.

Customer report data is a firehose of all detections from endpoints, which in most cases result in malware being blocked. Incident data, on the other hand, includes data collected from any event where malicious activity was detected on an MDR customer network or uncovered as part of an Incident Response case, and offers a somewhat deeper picture in many cases of the intent of activity and connections to other threat intelligence.

This report focuses on data specific to small and midsized organizations. Deeper dives on the data gathered from Sophos Incident Response and Sophos MDR Operations, including data on larger organizations, can be found in our Active Adversary Report (AAR) series.

## Broken Windows (and gateways)

Whether simply misconfigured, using weak credential policies, or running on vulnerable software or firmware, systems on the network edge are the initial point of compromise for over a third of all incidents involving intrusion into smaller organizations. As Sophos CEO Joe Levy pointed out recently, obsolete and unpatched hardware and software constitutes an ever-growing source of security vulnerabilities, a phenomenon he referred to as “digital detritus.”

While zero-day attacks on vulnerabilities are relatively rare in cybercrime targeting small and medium businesses, published vulnerabilities can be very quickly weaponized by access brokers and other cybercriminals. This was the case when the backup software provider Veeam released a security bulletin on CVE-2024-40711 in September 2024—within a month, cybercriminals had developed an exploit for the vulnerability, and paired it with gaining initial access through VPNs.

The Veeam vulnerability and similar documented vulnerabilities that remained unpatched by customers—some of them recent, but some over a year old—played a role in nearly 15 percent of the cases Sophos MDR tracked involving malicious intrusions in 2024. In nearly all cases, the vulnerabilities were reported for weeks if not longer before they were exploited by attackers, frequently in connection to ransomware attacks. In other cases, they were used to gain initial access by cybercriminals for other purposes—including gaining access to potentially sell to ransomware actors.

| CVE       | Description