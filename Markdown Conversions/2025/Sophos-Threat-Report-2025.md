# The Sophos Annual Threat Report: Cybercrime on Main Street 2025

Ransomware remains the biggest threat, but old and misconfigured network devices are making it too easy.

**Date:** April 16, 2025  
**Author:** Sean Gallagher  
**Categories:** Security Operations, Threat Research, Annual Threat Report  
**Featured:** Midsize businesses, small businesses

## Table of Contents
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

Small businesses are a prime target for cybercrime, as we highlighted in our past annual report. Many of the criminal threats we covered in that report remained a major menace in 2024, including ransomware–which remains a primary existential cyber threat to small and midsized organizations.

Ransomware cases accounted for 70 percent of Sophos Incident Response cases for small business customers in 2024—and over 90 percent for midsized organizations (from 500 to 5000 employees). Ransomware and data theft attempts accounted for nearly 30 percent of all Sophos Managed Detection and Response (MDR) tracked incidents (in which malicious activity of any sort was detected) for small and midsized businesses.

While ransomware attacks overall have declined slightly year over year, the cost of those attacks overall has risen, based on data from Sophos’ State of Ransomware report. And though many of the threats observed in 2024 were familiar in form, other data-focused threats continue to grow, and new tactics and practices have emerged and evolved:

- **Compromised network edge devices**—firewalls, virtual private network appliances, and other access devices—account for a quarter of the initial compromises of businesses in cases that could be confirmed from telemetry, and is likely much higher.
- **Software-as-a-service platforms**, which were widely adopted by organizations during the COVID pandemic to support remote work and to improve overall security posture, continue to be abused in new ways for social engineering, initial compromise, and malware deployment.
- **Business email compromise** activity is a growing proportion of the overall initial compromises in cybersecurity incidents—leveraged for malware delivery, credential theft, and social engineering for a variety of criminal purposes.
- One of the drivers of business email compromise is the phishing of credentials with adversary-in-the-middle multifactor authentication (MFA) token capture, a constantly evolving threat.
- **Fraudulent applications** carrying malware, or tied to scams and social engineering through SMS and messaging applications, lead to mobile threats for small and midsize businesses.
- Other less-technical threats leveraging the network continue to be a threat to small businesses, again with evolving patterns of scams.

This report focuses on the trends seen in cybercriminal attack patterns faced by small and midsized organizations. Details of malware and abused software most frequently encountered in endpoint detections and incidents is provided in an appendix to this report.

## A word about our data

The data used in our Annual Threat Report analysis comes from the following sources:

- **Customer reports**—this consists of detection telemetry from Sophos endpoint software running on customers’ networks, which gives a broad view of threats encountered, and analyzed within SophosLabs (in this report, referred to as endpoint detection data).
- **Incident data**—this consists of both data gathered in the course of escalations driven by detection of malicious activity on MDR customers’ networks, data gathered by MDR Incident Response from customer incidents, and data gathered by Sophos Incident Response from incidents on customer networks for organizations of 500 employees or fewer where there was little or no managed detection and response protection in place. These datasets are treated as a combined set of incident data in this report.

SecureWorks incident and detection data is not included in this report, as it was based on pre-acquisition telemetry. All data is from the 2024 calendar year, unless otherwise noted.

## Broken Windows (and gateways)

Whether simply misconfigured, using weak credential policies, or running on vulnerable software or firmware, systems on the network edge are the initial point of compromise for over a third of all incidents involving intrusion into smaller organizations. As Sophos CEO Joe Levy pointed out recently, obsolete and unpatched hardware and software constitutes an ever-growing source of security vulnerabilities, a phenomenon he referred to as “digital detritus.”

While zero-day attacks on vulnerabilities are relatively rare in cybercrime targeting small and medium businesses, published vulnerabilities can be very quickly weaponized by access brokers and other cybercriminals. 

![Table: Top published vulnerabilities as observed in Sophos MDR / IR intrusion incidents]

In some cases, even when patches have been deployed for known vulnerabilities, devices may remain vulnerable because they have already been compromised. In other cases, the patching process may have not been fully completed.

Network edge devices in particular—including virtual private network (VPN) appliances, firewalls with VPN capabilities, and other remote-access appliances—are a major contributor to cybercrime incidents. These devices collectively account for the largest single source of initial compromise of networks in intrusion incidents tracked by Sophos MDR.

![Figure 2: Relative frequency of initial compromise points by cybercriminals against small and medium businesses]

![Figure 3: Relative frequency of initial compromise points specifically observed in ransomware and data exfiltration/extortion attacks]

## STACs: Packaged playbooks, tactics, tools and procedures

Rather than tracking “threat groups,” Sophos MDR focuses on identifying specific patterns of behavior to track a set of actors across multiple incidents. These include tools, tactics and procedures (TTPs), support infrastructure, and other characteristics that reflect the use of a shared playbook or set of scripted tools. We refer to these as Security Threat Activity Clusters (STACs) and track their activity as campaigns.

![Figure 4: Frag Ransomware note associated with a STAC5881 attack]

Frag appears to be a “junk gun” ransomware—crudely coded, cheap ransomware produced as an alternative to ransomware-as-a-service.

![Figure 5: Most active security threat activity clusters in 2024 ordered by number of incidents]

## Trends in cybercrime techniques, tactics and practices

### Remote ransomware continues to grow
While the overall number of incidents in 2024 was slightly down, ransomware-related crime is not fading away. Sophos X-Ops found in an examination of telemetry that use of remote ransomware increased 50 percent in 2024 over last year, and 141 percent since 2022.

![Figure 6: Remote ransomware attacks from 2022 to 2024 by quarter]

### Social engineering via Teams vishing
In the second half of 2024, we saw the adoption of a combination of technical and social engineering attacks used by threat actors to target organizations using Microsoft 365. These attacks used “email bombing”—the sending of a large volume of emails to targeted people—followed by a fake technical support call over Microsoft Teams.

### MFA phishing
Criminals have also adjusted their deception techniques for gathering user credentials. MFA phishing relies on an “adversary-in-the-middle” approach, where the phishing platform acts as a proxy to the actual authentication process.

![Figure 7: A developer browser view of a FlowerStorm phishing page]

### Adversarial AI usage
Cybercriminals engaged in intrusion-style attacks have made limited use of artificial intelligence. Most of the use of generative AI by cybercriminals has focused on social engineering tasks: creating images, videos and text for fake profiles, and for use in communication with targets to mask language fluency issues and identity.

![Figure 8: The login screen for a RaccoonStealer Office365-focused credential theft portal]
![Figure 9: The source of the image, on the generative AI site OpenArt]

### Quishing
Around the same time that RockStar was peaking, Sophos X-Ops discovered a “quishing” campaign targeting Sophos employees. Emails with QR codes alleged to provide secure access to a document were embedded in a PDF attachment; the QR code in fact contained a link to a fraudulent document-sharing site.

![Figure 10: A phishing email with a QR code targeting Sophos employees]
![Figure 11: The fake authentication window for the phishing site]

### Malvertising and SEO poisoning
Malvertising is the use of malicious web advertisements, including paid listings on search results. It continues to be a favored method of distributing malware.

### EDR killers
Sophos X-Ops has observed a variety of malicious software tools developed for the criminal marketplace over the past two years referred to as “EDR killers.” These tools are intended to exploit kernel drivers to gain privileged access to the operating system and kill targeted protected processes—specifically, endpoint security software.

![Figure 12: Top 10 EDR-killer malware detected by Sophos endpoint protection]

## Conclusion

The threat landscape for small and midsized businesses remains highly dynamic. Responding to this environment is more than most small organizations can handle without external support.

Small and midsized organizations can reduce their risk profile with these steps:
- Migrate from passwords to passkeys for account credentials.
- For accounts that can’t be secured with passkeys, use multifactor authentication.
- If accounts cannot be secured by either method, closely monitor them through an identity threat detection and response strategy.
- Prioritize patching edge devices such as firewalls and VPN devices.
- Make sure endpoint security software is deployed across all your assets.
- Enlist outside help to audit and monitor your external attack surfaces regularly.

## Acknowledgements
Sophos X-Ops thanks Anna Szalay, Colin Cowie and Morgan Demboski of Sophos MDR Threat Intelligence and Chester Wisniewski, Director, Global Field CISO for their support in the production of this report.

## About the authors
**Sean Gallagher**  
Sean Gallagher is Principal Threat Researcher, Sophos X-Ops. Prior to joining Sophos, he was an information security and technology journalist for over 30 years, including 10 as information security and national security editor for Ars Technica.

---
© 2025 Sophos Ltd. All Rights Reserved.