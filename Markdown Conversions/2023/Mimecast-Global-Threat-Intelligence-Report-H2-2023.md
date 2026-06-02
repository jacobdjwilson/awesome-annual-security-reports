# Global Threat Intelligence Report: October-December 2023

## Table of Contents
- [Introduction](#introduction)
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [Extortion Campaigns Grow, Cyberattacks Follow Geopolitics](#extortion-campaigns-grow-cyberattacks-follow-geopolitics)
- [Quarter Four 2023 in Charts](#quarter-four-2023-in-charts)
- [Brand Abuse Becomes More Convincing](#brand-abuse-becomes-more-convincing)
- [Threat Assessment](#threat-assessment)
- [Major Events Q4](#major-events-q4)
- [Top Threat Campaigns Q4](#top-threat-campaigns-q4)
- [Top 5 Advisories](#top-5-advisories)
- [How to Take Action](#how-to-take-action)
- [Resources](#resources)
- [Conclusion](#conclusion)

---

## Introduction
Too often, organizations receive threat intelligence as individual analyses of specific incidents, giving security teams a narrow view of the threat landscape. In this Global Threat Intelligence Report, Mimecast aims to put the previous three months’ worth of incidents into context and give companies the tools they need to understand where attackers are headed and where defenses could be improved.

Mimecast generates threat intelligence through its analysis of 1.7 billion emails per day on behalf of more than 42,000 customers. Because email is the channel through which most cyber threats launch, Mimecast sees many new threats before they become widely known. This report distills insights from the intelligence Mimecast generated throughout the fourth quarter of 2023 and combines it with external intelligence from the cybersecurity community at large. It includes an analysis of threat activity, a series of top-line statistics that shaped that activity, and recommendations for what small businesses and large enterprises alike can do to mitigate the risk those threats pose.

![1.7 Billion emails per day, 42,000 customers]

---

## Executive Summary
The fourth quarter of 2023 saw attackers continuing to shift their delivery methods toward using links for initial payloads, slowly moving away from sending malware as email attachments. In addition, threat actors are increasingly using QR codes to get around defenses designed to block malicious links and obfuscate their attacks.

Following attacks on major casinos earlier in the year, attackers continued to focus on travel, hospitality, and catering companies in Q4 2023, resulting in the sector becoming the second most targeted industry for the quarter, surpassed only by attackers’ efforts against the banking sector. While campaigns directed at human resources and recruitment services have subsided somewhat, the sector remains the third most targeted.

**Mimecast Threat Intelligence Team**
Mimecast’s threat intelligence team is comprised of a globally distributed set of engineers, scientists, analysts, and threat researchers that aid the Mimecast Security Operations Center (MSOC). Threats are continuously monitored across more than 1.7 billion emails per day. Mimecast’s cybersecurity experts reverse-engineer attack tools, investigate attacks, and test the efficacy of indicators of compromise to quickly develop threat intelligence and protections across its solutions.

---

## Key Findings

### Sectors
The sectors that experienced the most attacks in the fourth quarter of 2023 were financial institutions; travel, hospitality, and catering; and human resources and recruitment services. These attacks were driven by ransomware, data theft, and business email compromise (BEC). Additionally, across all industries, average users at small and medium-sized firms encountered more than twice the number of threats as those at large companies.

### Links vs. Attachments
For the first time, the average user was more likely to encounter a malicious link than a malicious attachment in Q4 2023. In the past, attackers were more likely to use known malware to deliver payloads.

### Generative AI
Attackers are using generative AI and machine-learning models to create more convincing phishing lures and translate attacks into other languages. Technical threat indicators, such as domain reputation, browser isolation, and malware analysis, will be increasingly necessary to block attacks.

### QR Codes
A surge in using QR codes to obfuscate links has continued, serving the same purpose as URL shortening schemes but with an additional benefit to attackers, as victims have already become acclimated to snapping pictures of QR codes.

### Geopolitics
Geopolitical tensions have increased, leading to more cyberattacks with more than 100 hacker groups claiming participation in the Israel-Gaza conflict alone. Nation-states are using cyber operations to gather intelligence on rival governments and attack critical infrastructure and information systems.

---

## Extortion Campaigns Grow, Cyberattacks Follow Geopolitics
Ransomware and breach-for-ransom campaigns continued to grow in Q4 2023, with one of the larger groups, ALPHV Blackcat, compromising more than 1,000 victims with ransomware and data extortion and reaping more than $300 million in ransom payments by the end of the quarter.

Attack strategies have evolved from crypto-ransomware (where attackers encrypt data and hold the decryption key) to breach-for-ransom campaigns (where attackers steal sensitive data and threaten to release the sensitive information unless paid) to double- and triple-extortion strategies (where attackers combine tactics for more direct consequences).

Ransomware and information-stealing groups have started using more sophisticated techniques, such as stealing tokens and account identifiers from Google Chrome. These successful tactics have led to a consolidation of the number of ransomware tools — with 43 malware families used for extortion in 2023, down from 95 in 2022 — signaling that cybercriminals and their affiliates are settling on a known set of popular platforms. Four groups — LockBit, Cl0p, ALPHV/BlackCat, and Play — dominated the ransomware landscape during the quarter, accounting for 88% of all ransomware activity.

However, while ransomware and data-breach incidents increased in 2023, companies are resisting extortion attacks. Ransom payment rates have plummeted, hitting a low of 34% in Q2 2023, down from 85% at the beginning of 2019. Three shifts in business security operations and the economics of ransomware are likely driving the change: Companies are less trusting of cybercriminals’ ability to recover data; organizations have had time to (slowly) improve their security posture; and paying ransoms to threat actors from certain nation-states now violates federal laws.

Ransomware groups are aiming to reverse the trend. Starting on Oct. 1, the LockBit ransomware group put in place new rules regarding negotiations with victims, warning its “affiliates” that offering large discounts on ransom fees is no longer acceptable.

The geopolitical situation deteriorated with the Oct. 7 terrorist attack on Israel by the militant group Hamas. Like other global conflicts, such as Russia’s invasion of Ukraine, cyberattacks have increased significantly as nation-state cyber operations, groups linked to either side, and hacktivist supporters ramped up their attacks against web sites, critical infrastructure, and computer systems. At least 90 pro-Palestinian threat actors and 23 pro-Israeli threat actors conducted attacks in Q4 2023.

There are already some signs that machine-learning models and generative AI are changing the threat landscape as well. For example, phishing lures are becoming much more convincing and easier to tailor to specific geographies because of the adoption of generative AI by threat actors, according to Mimecast’s threat intelligence team. In addition, researchers have been able to upload malicious code to GitHub linked to machine-learning components, such as PyTorch, like attacks on other open-source supply chain components.

---

## Quarter Four 2023 in Charts
1. **SMBs encounter twice as many threats**
2. **Malicious links on the rise**
3. **Phishing dominated & links the most common vector**
4. **Attacks increase across industries, HR-focused attacks subside**
5. **Top vulnerabilities over time**

### SMBs encounter twice as many threats
**Figure 1. Threats per user by company size**
The significant uptick in threats seen in Q3 seems to have subsided, but medium-sized companies still saw slightly more threats per user (TPU) than smaller firms in Q4. Average users at small and medium-sized businesses (SMBs) encountered more than twice the number of threats — 31 and 32 TPU, respectively — than users at large companies, who saw about 15 TPU in Q4.

![Chart showing TPU trends for Small, Medium, and Large companies from Q2 2022 to Q4 2023]

### Malicious links on the rise
**Figure 2a & 2b. Threats per user by type of threat**
Spam and impersonation both declined in Q4 2023 but continued to dominate malicious activity. By removing the two largest categories of threats — spam and impersonation — another trend becomes evident. In Q4, for the first time, the average user was more likely to encounter a malicious link than a malicious attachment.

![Charts showing trends for Spam, Impersonation, Known Malware, Malicious Links, and Unknown Malware]

### Phishing dominated active threats, with links the most common vector
**Figure 3a. Relative volume of all threats**
- Spam: 86%
- Phishing: 9%
- Suspicious: 2%
- Malware: 2%
- Unwanted: 1%

**Figure 3b. Malware and malicious links**
Malicious URLs continue to make up the largest portion of all major detection types. Credential harvesting is the second most identified attribute of phishing attacks.

---

## Brand Abuse Becomes More Convincing
Almost every type of email attack uses legitimate brands to gain trust. During Q4 2023, one threat actor used SendGrid’s email marketing service to send out email campaigns that impersonated human resource departments and asked targeted users to click on a link that appeared to be from a Microsoft SharePoint Online server.

**Figure 6. Attackers switch focus to Amazon prior to holiday shopping**
In Q4, attackers switched up their brand-impersonation tactics. Looking to capitalize on the holiday shopping season, fraudsters ramped up their impersonation of Amazon. During the two weeks before Black Friday, Mimecast detected more Amazon-branded threats than Microsoft-branded threats.

**Figure 7. QR Code detection over 60 days**
Emails containing QR codes now exceed 3.5 million per day regularly. Mimecast has documented two major campaigns using QR codes — one branded as Microsoft password reset and the other as DocuSign.

**Figure 8. Evernote tops popular domains for phishing attacks**
Attackers are widely using file-sharing sites that have trusted brands to serve up malicious content. The top brand for file-sharing sites for the past three quarters is Evernote.

---

## Threat Assessment
Attackers have doubled down on techniques for bypassing multifactor authentication (MFA) mechanisms. EvilProxy, a phishing-as-a-service (PhaaS) platform, targeted the financial and insurance industries with an attack that uses a proxy to bypass MFA.

- **Ransomware operators**: Continued to increase their focus on energy companies.
- **Initial access brokers (IABs)**: Actively sought out credentials and compromised systems within the networks of energy operators.
- **Nation-state cyber conflicts**: Heated up following the terrorist attack by Hamas on Israeli civilians and Israel’s military response.

---

## Major Events Q4
- **1 Oct**: Phishing Attacks Continue Against Hospitality Sector.
- **3 Oct**: EvilProxy Phishing Attack Targets U.S. Firms.
- **9 Oct**: Hacktivists Race into Israel-Hamas War on Both Sides.
- **17 Oct**: Attackers Combine DadSec Phishing, Cloudflare.
- **18 Oct**: State-Sponsored Actors Target WinRAR Flaw.
- **6 Nov**: Iranian Group Targeting Israeli Sectors.
- **12 Nov**: Energy Sector Faces Increasing Attacks During Winter.
- **29 Nov**: Financial Service Phishing Delivers LUMMA Malware.
- **6 Dec**: ChatGPT Protections can be Bypassed to Create Phishing Email.
- **19 Dec**: Law Enforcement Shutter ALPHV Site.

---

## Top Threat Campaigns Q4
- **Microsoft QR codes**: Mimecast encountered a phishing attempt that impersonates a company requesting that the targeted victim set up Microsoft authentication.
- **DocuSign QR codes**: Disguises a malicious link as a QR code purportedly leading to a document shared from a payroll department.
- **Google App Script attacks**: Abused through software vulnerabilities to create phishing pages.
- **Mexico Bank fraud spam campaign**: Targeted Latin American countries, especially Mexico, using modest spam campaigns to download malware.
- **Meta Instagram impersonation campaigns**: Impersonates Meta Instagram with a notification that appears to indicate a violation of copyright infringement.

---

## Top 5 Advisories
1. **Oct [NSA/CISA]**: NSA and CISA Red and Blue Teams Share Top Ten Cybersecurity Misconfigurations.
2. **7 Nov [FBI]**: Ransomware Actors Continue to Gain Access through Third Parties and Legitimate System Tools.
3. **16 Nov [FBI/CISA]**: Data Theft and Extortion Targets Enterprises Through Third-Party IT Providers.
4. **7 Dec [NCSC/NSA/FBI/CISA/ACSC/CCCS]**: Russian FSB Cyber Actor Star Blizzard Continues Worldwide Spear-Phishing Campaigns.
5. **19 Dec [CISA/FBI]**: #StopRansomware: ALPHV Blackcat.

---

## How to Take Action

### Threat-specific countermeasures
- **Protect sensitive positions**: Segment certain personnel from potentially malicious content.
- **Develop a secure supply chain strategy**: Create minimum security requirements for partners and service providers.
- **Slow down attackers using segmentation and deception**: Use network segmentation and honeytokens.
- **Educate users and block malicious QR codes**: Prevent the loading of images by default and educate workers on QR code dangers.

### General recommendations to combat threats
- **Assess your attack surface areas**: Embrace a zero-trust approach.
- **Minimize your attack surface by blocking unused services**: Block content hosts and websites not required for business.
- **Prioritize vulnerabilities for patching**: Use vulnerability metrics and knowledge of critical systems to prioritize.
- **Make credentials resistant to phishing**: Adopt phishing-resistant multifactor authentication.

### Steps specific to Mimecast customers
- Utilize single sign-on or Mimecast’s built-in multi-factor authentication.
- Ensure DNS authentication policies honor DMARC records.
- Optimize Impersonation Protection.
- Set an aggressive re-writing of URLs.
- Consider setting Auto-Allow policies to ‘strict’.
- Utilize pre-built integrations with SIEM and XDR vendors.
- Leverage bring-your-own threat intelligence.
- Deploy end-user tools to report potentially malicious messages.

---

## Resources
- **CISA/NSA**: NSA and CISA Red and Blue Teams Share Top Ten Cybersecurity Misconfigurations (5 Oct 2023).
- **CISA**: CISA Releases New Resources Identifying Known Exploited Vulnerabilities and Misconfigurations Linked to Ransomware (12 Oct 2023).
- **CISA**: Phishing Guidance: Stopping the Attack Cycle at Phase One (18 Oct 2023).
- **CISA/NSA**: CISA, NSA, and Partners Release New Guidance on Securing the Software Supply Chain (9 Nov 2023).
- **CISA/NCSC**: CISA and UK NCSC Unveil Joint Guidelines for Secure AI System Development (26 Nov 2023).
- **CISA/NCSC/ACSC/FBI**: Russian FSB cyber actor Star Blizzard continues worldwide spear-phishing campaigns (7 Dec 2023).

---

## Conclusion
The fourth quarter of 2023 solidified many of the trends from previous quarters. Attackers are increasingly using brands to fool users into trusting spam and phishing attacks, often marrying the brand with a QR code or a link to a legitimate file service. Geopolitical tensions have heated up following Hamas’ attack on Israeli civilians and Israel’s subsequent retaliation, resulting in more attacks related to the conflict and a new set of topics for phishing lures.

Attackers slightly changed the sectors they targeted in Q4 2023, focusing on finance, such as banking and other services; professional services, such as HR and accounting; and the travel, hospitality, and catering sector. While campaigns targeting the human resources and recruitment services sector have subsided somewhat, the industry remains the third most targeted sector.

www.mimecast.com | ©2024 Mimecast | All Rights Reserved | GL-05902