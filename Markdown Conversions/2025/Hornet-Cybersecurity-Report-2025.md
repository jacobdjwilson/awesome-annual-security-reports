# Cybersecurity-Report

## Table of Contents
- [About Hornetsecurity](#about-hornetsecurity)
- [What is the Cybersecurity Report?](#what-is-the-cybersecurity-report)
- [What is the Security Lab?](#what-is-the-security-lab)
- [Chapter 1 – Executive Summary](#chapter-1--executive-summary)
- [Chapter 2 – The Current Microsoft 365 Threat Landscape](#chapter-2--the-current-microsoft-365-threat-landscape)
  - [Email Security Trends](#email-security-trends)
  - [Spam, Malware, Advanced Threat Metrics](#spam-malware-advanced-threat-metrics)
  - [Attack Techniques Used in Email Attacks in 2024](#attack-techniques-used-in-email-attacks-in-2024)
  - [Attachment Use and Types in Attacks](#attachment-use-and-types-in-attacks)
  - [Email Threat Index for Business Verticals](#email-threat-index-for-business-verticals)
  - [Brand Impersonation](#brand-impersonation)
  - [Safety of Data in the Cloud](#safety-of-data-in-the-cloud)
  - [Passkeys and Adversary in the Middle (AitM) Attacks](#passkeys-and-adversary-in-the-middle-aitm-attacks)
  - [Vendor Overdependence Concerns Deepen](#vendor-overdependence-concerns-deepen)
  - [What is Microsoft Responsible for?](#what-is-microsoft-responsible-for)
  - [The Difficulties Posed by Multiple Tenants in the Microsoft Cloud](#the-difficulties-posed-by-multiple-tenants-in-the-microsoft-cloud)
- [Chapter 3 – An Analysis of the Major Security Incidents and Cybersecurity News of 2024](#chapter-3--an-analysis-of-the-major-security-incidents-and-cybersecurity-news-of-2024)
  - [The Crowdstrike Incident](#the-crowdstrike-incident)
  - [Change Healthcare](#change-healthcare)
  - [National Public Data](#national-public-data)
  - [Mgm And Caesar’s Casino Breach](#mgm-and-caesars-casino-breach)
  - [23andMe Dna Testing Service Breach](#23andme-dna-testing-service-breach)
  - [Lockbit’s Leader Unmasked](#lockbits-leader-unmasked)
  - [Xz Utils Backdoor](#xz-utils-backdoor)
  - [A Year of Microsoft Security Drama](#a-year-of-microsoft-security-drama)
- [Chapter 4 – Forecasting the Threat Landscape in 2025](#chapter-4--forecasting-the-threat-landscape-in-2025)
  - [Did We Get Last Year’s Predictions Right?](#did-we-get-last-years-predictions-right)
  - [The Security Lab’s Predictions](#the-security-labs-predictions)
  - [LLMs in Attacker’s Hands](#llms-in-attackers-hands)
  - [AI-Enabled Deepfakes Used for Spear-Phishing and to Influence the Public](#ai-enabled-deepfakes-used-for-spear-phishing-and-to-influence-the-public)
  - [Legal Cases Will Arise Due to AI Use and Will Lead to Regulation](#legal-cases-will-arise-due-to-ai-use-and-will-lead-to-regulation)
  - [New Regulatory Frameworks and Challenges](#new-regulatory-frameworks-and-challenges)
  - [Corruption of the Open Source Community](#corruption-of-the-open-source-community)
  - [Continued Predictions for Quantum Computing](#continued-predictions-for-quantum-computing)
  - [Increased Adoption of “Memory Safe” Languages](#increased-adoption-of-memory-safe-languages)
  - [How Much At Risk Will My Organization Be In 2025?](#how-much-at-risk-will-my-organization-be-in-2025)
  - [What Organizations Should Do to Defend Themselves](#what-organizations-should-do-to-defend-themselves)
  - [Culture Eats Strategy for Breakfast](#culture-eats-strategy-for-breakfast)
  - [A Balanced Security Strategy](#a-balanced-security-strategy)
- [Chapter 5 – Resources](#chapter-5--resources)

---

## About Hornetsecurity
Hornetsecurity empowers companies and organizations of all sizes to focus on their core business by protecting M365 workloads, email communications, securing data, and ensuring business continuity and compliance with next-generation cloud-based solutions.

Our flagship product, 365 Total Protection, is the most comprehensive cloud security solution for Microsoft 365 on the market, including email security, compliance, governance, and backup.

## What is the Cybersecurity Report?
The Cybersecurity Report by Hornetsecurity is an annual analysis of the Microsoft 365 threat landscape based on real-world data collected and studied by Hornetsecurity’s dedicated Security Lab team. Hornetsecurity’s cybersecurity solutions process more than 4 and a half billion emails every month. By analyzing the threats identified in these communications, combined with a detailed knowledge of the wider threat landscape, the Security Lab reveals major security trends, threat actor actions and can make informed projections for the future of Microsoft 365 security threats, enabling businesses to act accordingly. Those findings and data are contained within this report.

## What is the Security Lab?
The Security Lab is a division of Hornetsecurity that conducts forensic analysis of current and critical security threats, specializing in email security in the Microsoft 365 ecosystem. Our multinational team of security specialists has extensive experience in security research, software engineering, and data science.

An in-depth understanding of the threat landscape established through hands-on examination of real-world phishing attacks, malware, ransomware gangs and more, is critical to developing effective countermeasures. The detailed insights uncovered by the Security Lab serve as the foundation for Hornetsecurity’s next-gen cybersecurity solutions.

---

## Chapter 1 – Executive Summary
By leveraging its huge user dataset, Hornetsecurity is uniquely positioned to conduct a detailed examination of email-based threats as well as those threats targeting the greater Microsoft 365 ecosystem. This allows the security researchers at Hornetsecurity to distill this data into important insights for IT teams and security professionals. Email continues to be a major communication channel, particularly for companies and professional organizations. In our analysis of more than 55.6 billion emails in 2024, 36.9% are categorized as “unwanted.” 97.8% of unwanted emails are spam or rejected outright due to external indicators and 2.3% of unwanted emails were flagged as malicious.

![Classification of emails scanned by Hornetsecurity]
![Classification of unwanted emails]

When we look at the attack types used in email attacks, phishing retains its top place as the most prevalent attack method, accounting for 33.3% of attacks. This is followed closely by malicious URLs accounting for 22.7% of cases. These numbers align with the types of attacks that have gained popularity amongst threat actors over the past year - mainly in reverse-proxy style credential theft attacks that heavily leverage social engineering and malicious links.

A renewed focus on social engineering and security token / credential theft is noticeable in our data regarding malicious file types as well. We track the types of files used for the delivery of malicious payloads in email attacks and found that there are noted decreases in the use of malicious attachments period. Nearly every malicious file type saw a decrease when compared with last year. That said, HTML files, PDFs, and Archive files remain in the top three spots in a continuation from the previous year.

Threat actors have been leveraging a slightly higher volume of easier to detect (and ultimately “rejected”) email attacks over the data period. This is indicated by the slight decrease in the number of malicious emails that were classified as “Threats” and “AdvThreats”. As a result, we saw the threat index for nearly every industry drop during the data period. This is because our industry threat index compares the number of clean emails vs. the volume of “Threats” and “AdvThreats”. Also notable is the fact that there is little variation from industry to industry. Yes, there are some that are higher than others, but the data continues to show, year after year, that EVERY industry is under attack.

In terms of brand impersonations over the last year, we found that despite remaining in the position of number 1 most impersonated brand there was a large decrease in the amount of DHL impersonation attempts.

That said, the amount of FedEx impersonation attempts tripled, Docusign and Facebook both had more than double the amount of impersonation attempts, while Mastercard and Netflix both saw notable increases as well.

Finally, when we continue our annual discussion regarding the safety of data in the cloud, a key theme that we’ve seen from attackers this year is, again, the increasing use of credential / token theft toolkits via an Adversary-in-the-Middle attack. When compared with previous years, these attacks have become popular with threat actors. This is because of the ease with which they can target a large number of victims with VERY convincing landing pages with minimal effort.

These toolkits are designed to account for MFA (Multi-Factor) authentication as well, which many organizations assume (wrongly) keeps them 100% safe from said attacks. The cybersecurity industry continues to address this concern with better scanning mechanisms, security awareness training, and phishing-resistant login technologies like passkeys. However, these mitigations take time of course, and as a result, some organizations have fallen victim leading to a loss or leakage of sensitive data.

As this style of attack still makes heavy use of email communications as well as increasing use of chat communications like Microsoft Teams, a robust email and Microsoft 365 security strategy is essential for operating safely in today’s digital ecosystem.

---

## Chapter 2 – The Current Microsoft 365 Threat Landscape
On an annual basis, Hornetsecurity’s dedicated Security Lab reviews the company’s extensive data set and analyzes the state of global email threats and communication statistics. Additionally, the team regularly conducts forward-thinking exercises and provides insight into potential future threats. This chapter focuses on reviewing the data from November 1st, 2023, to October 31st, 2024, which forms the basis for projections of the changing threat landscape laid out in Chapter 4.

### Email Security Trends
Despite increasing usage of collaboration and instant messaging software, such as Microsoft Teams, email continues to be a top area of concern in terms of cyberattacks. We’ve observed a continued decrease in the number of emails categorized as Threats/AdvThreats - 2.3% this year, compared to 3.7% from last year, and 5.5% the year before that (When looking at “Unwanted” emails). That said, the risk to businesses around the globe remains high. This is primarily due to increased use in social engineering techniques via low-effort spray-style email attacks that seek to get the target user to engage somehow.

By reviewing more than 55.6 billion emails collected over the current reporting period (November 1st, 2023 - October 31st, 2024), the Security Lab has made the following determinations:

### Spam, Malware, Advanced Threat Metrics
As we’ve seen over the last decade, email continues to be one of the primary methods that threat actors use to launch attacks. Our data from this report’s data period classifies 36.9% of all emails as “Unwanted” - a 0.6 percentage point increase from 2023. The definition of “unwanted” refers to emails that are not genuine communications desired by the recipient. The chart below shows our breakdown of unwanted emails along with clean emails.

![2024. Unwanted emails by category including clean]

For a concise breakdown of percentages that make up “unwanted” emails, we classified them as follows:

![2024. Unwanted emails by category]

| CATEGORY | DESCRIPTION |
| :--- | :--- |
| Spam | These emails are unwanted and are often promotional or fraudulent. The emails are sent simultaneously to a large number of recipients. |
| Threat | These emails contain harmful content, such as malicious attachments or links, or they are sent to commit crimes like phishing. |
| AdvThreat | Advanced Threat Protection has detected a threat in these emails. The emails are used for illegal purposes and involve sophisticated technical means that can only be fended off using advanced dynamic procedures. |
| Rejected | Our email server rejects these emails directly during the initial connection from the sending email server because of external characteristics, such as the sender’s identity, and the emails are not analyzed further. |

### Attack Techniques Used in Email Attacks in 2024
In our data analysis of emails from the data period we observed the below breakdown of attack types used in email attacks:

![Attack techniques used in email attacks 2024]

What our data does show us for this data period is that phishing remains the number one attack type used in email-based attacks, followed by malicious URLs. The growing popularity of malicious URLs among attackers is largely driven by their use in reverse-proxy credential harvesting attacks, leveraging tools like Evilginx.

Outside of that, Advanced-Fee scams are still quite popular amongst threat-actors followed by extortion in 4th place. Extortion is notable as we continue to see cases where threat-actors will first exfiltrate data prior to putting ransomware in place within a given environment. Should the target refuse to pay (due to recovering from backup) the threat actor will threaten to release the data to the public.

### Attachment Use and Types in Attacks
Email attachments continue to be used by threat actors for the delivery of malicious payloads in 2024. Threat actors use attachments to hide malware as well as add an air of authenticity to their malicious communications, depending on the attached file type in use. Additionally, some rudimentary spam/malware filters may be unable to scan certain file types leading to infection by more complex attacks such as HTML smuggling. In fact, the use of malicious HTML files remains in the number one spot for most used file types used in malicious emails, as shown below.

![File-types for malicious payloads in 2024]

- PDF file usage saw a 3.6% point decrease in 2024
- Archive files saw a similar trend in a percentage point decrease of 1.8 in 2024
- We observed a near universal decrease in all malicious file types as attackers pivot to other attack styles

### Email Threat Index for Business Verticals
One of the key areas we review on an annual (and monthly) basis, is the number of threats being levied at different industry verticals. This allows us to determine if there are dedicated campaigns or targeted attacks on specific industries. It also provides some insights that business leaders can use to help determine if they’re at increased risk of attack or not.

Most notable in this year’s data is the fact that EVERY industry vertical saw a decrease of the associated email threat index. This correlates with our data above showing the number of emails classified as “Threats” and “AdvThreats” decreasing when compared with last year.

![Median threat vs clean email radio per industry]

### Brand Impersonation
Brand impersonation continues to be a major email attack technique targeting end users and businesses in 2024.

The shipping company DHL has seen perhaps the most dramatic shift in brand impersonation attempts. The brand saw a mere fraction of impersonation attempts in 2024 vs. 2023. That said, it still remains in the number one spot on our most impersonated brands list, followed closely by FedEx.

![Top 10 impersonated brands]

### Safety of Data in the Cloud
The “cloud” has been here for more than a decade now, but we’ve just started to see businesses either mass-migrating to cloud services or being established as 100% cloud-hosted businesses. Take the storage of business data for example. 10 years ago, most businesses still held some sort of on-premises file server that hosted the organization’s critical data. Now it’s becoming more common to leverage cloud storage for this. SharePoint Online and OneDrive for Business are increasingly becoming the place where data lives and is secured with services like Microsoft Entra.

### Passkeys and Adversary in the Middle (AitM) Attacks
Where defenders go, attackers follow. For several years, we here at Hornetsecurity, as well as every other security minded person and company, has advocated for MFA as a more secure replacement for the traditional username + password dance for signing in to systems.

To defeat these more sophisticated attacks, you need a phishing resistant MFA method. These methods are newer and not seeing huge adoption (yet) in the industry. Some examples include Windows Hello for Business, FIDO2 hardware USB keys and most recently Passkeys.

### Vendor Overdependence Concerns Deepen with Regards to Cloud Data Safety
Vendor Overdependence is the practice of placing many or nearly all core business processes and procedures into the hand of a vendor partner. The problem with the arrangement is if the vendor has issues of some sort (security related or otherwise), then the business suffers as a result.

### What is Microsoft Responsible for?
Many ask: “If Microsoft isn’t taking care of my data and security, what are they really responsible for?” The current stance from Microsoft on this question has not altered in 2024. To fully understand, you must be familiar with Microsoft’s Shared Responsibility Model.

The important bit is that the shared responsibility model states, THE RESPONSIBILITY IS ALWAYS RETAINED BY THE CUSTOMER FOR:
- Information and Data
- Devices (Mobiles and PC)
- Accounts and Identities

### The Difficulties Posed by Multiple Tenants in the Microsoft Cloud
As Microsoft’s core cloud services have been out for a decade or more many organizations are finding themselves in a place where they need to manage and maintain multiple Microsoft 365 environments. This could be a business that has conducted several mergers and acquisitions, or maybe you’re a managed services provider (MSP) providing IT services across multiple customers.

---

## Chapter 3 – An Analysis of the Major Security Incidents and Cybersecurity News of 2024
The last 12 months have been a rollercoaster when it comes to cyber events worldwide. If we covered all of the (big) ones this report would be twice as long, so we’ll focus on the most important ones, either based on their impact on society, or where they give us a good insight that we can all use to improve the cybersecurity posture of our organizations.

### The Crowdstrike Incident
On 19 July 2024 arguably the largest IT outage ever occured. Within a few minutes approximately 8.5 million Windows systems that were running the Crowdstrike Falcon agent globally crashed / bluescreened and continued to restart and then crash, until manually repaired.

### Change Healthcare
In February 2024, Change Healthcare, a subsidiary of UnitedHealth, experienced a massive ransomware attack that compromised the personal, financial, and healthcare records of ~100 million Americans.

### National Public Data
The National Public Data (NPD) breach, which occurred in early 2024, is one of the largest data breaches in history, exposing up to 2.9 billion records.

### Mgm And Caesar’s Casino Breach
In October 2023, MGM and Caesar’s casinos and resorts were both hit by ransomware. MGM didn’t pay the ransom, and they expect their recovery to cost 100 million USD, whereas Caesar’s did pay, about 15 million USD.

### 23andMe Dna Testing Service Breach
The large breach at the 23andMe DNA testing service was downplayed by the company for several months until in December 2023 it became clear that 6.9 million customers had their data stolen.

### Lockbit’s Leader Unmasked
In February 2024, the leaders behind LockBit, once one of the largest ransomware criminal gangs were themselves hacked, led by the British National Crime Agency, and their leader identified as Dmitry Yuryevich Khorosev.

### Xz Utils Backdoor
The XZ Utils backdoor was an interesting saga, revealed in March 2024. Here fake personas built up a relationship with the maintainer of the XZ Utils Open-Source Software (OSS) package over several years.

### A Year of Microsoft Security Drama
Microsoft hasn’t had a good last few years when it comes to security, back in June 2023 the Chinese group (Storm-0558) compromised email inboxes in 22 organizations worldwide.

---

## Chapter 4 – Forecasting the Threat Landscape in 2025

### Did We Get Last Year’s Predictions Right?
Looking back on our various predictions in the 2024 previous edition of the Cybersecurity Report is an interesting exercise, foretelling the future is always challenging, but we definitely got some things right, and a few things didn’t pan out as we expected.

### The Security Lab’s Predictions
Every year, as part of this report, the Security Lab team at Hornetsecurity looks at the state of the industry, our data, attack trends, and more to make a series of predictions for the coming year.

### LLMs in Attacker’s Hands
Last year we looked at the rise of ChatGPT and other Large Language Models (LLMs) and their impact on cybersecurity, both for attackers and defenders.

### AI-Enabled Deepfakes Used for Spear-Phishing and to Influence the Public
The use of deepfake technology in spear-phishing attacks is a growing concern and we’re likely to see this combination in 2025.

### Legal Cases Will Arise Due to AI Use and Will Lead to Regulation
This has been discussed at length since ChatGPT first made waves in the market. The question of legalities, copyright, and ownership have underpinned AI generated content at nearly every stage of evolution.

### New Regulatory Frameworks and Challenges
Speaking of regulation, the introduction of new regulatory frameworks such as NIS2, DORA, CRA, and KRITIS (Germany only) will present significant challenges for organizations.

### Corruption of the Open Source Community
For many years free and open-source software (FOSS) was seen as something of an oasis in a perceived security poor software ecosystem. With the XZ Utils incident we discussed earlier in this report, this sentiment is no longer the case.

### Continued Predictions for Quantum Computing
In past reports we’ve spoken about a threat that’s not imminent but on the horizon; Quantum Computing. While we’re still some years away from a cryptographically relevant quantum computer (CRQC), development is progressing rapidly.

### Increased Adoption of “Memory Safe” Languages
Software has long been plagued by security issues that are the result of memory management issues. As a result, the industry has started to move towards “memory safe” languages like Rust and / or Swift.

### How Much At Risk Will My Organization Be In 2025?
Our answer to this question remains much the same as it was in previous years, if your organization is capable of paying a ransom or you hold some information of intellectual property that can be sold for a profit - you ARE a target.

### What Organizations Should Do to Defend Themselves
There’s a tendency for organizations to react to specific threats and acquire point security solutions for each area, and thus focus on technology solutions, rather than covering the basics of security hygiene first.

### Culture Eats Strategy for Breakfast
To transform your organization into a cyber resilient business will take time, effort, and persistence. You cannot turn your business into a well defended cyber fortress without involving everyone and helping them see how it affects them, and why they must be part of the solution.

### A Balanced Security Strategy
[Content truncated in original source]

---

## Chapter 5 – Resources
[Content not provided in source]

---

isk manage-
ment. If you start talking about technical details, and how it works, you’ll lose anyone else in the business,
but if you translate technology and process changes into business risk (or business opportunity) language,
everyone should be onboard.

And this cyber resilient business isn’t static, just like other risks to business (geopolitical, economic, com-
petitors),  it’s  ever  changing  and  the  business  needs  to  continuously  learn  and  adapt.  Recent  examples
include the way attackers are bypassing or defeating “weaker” forms of MFA, with Attacker in the Middle
toolkits or MFA fatigue attacks. And social engineering is an ever-present risk – would your helpdesk have
been more successful in defending your business than those of Caesar’s or MGM’s?

33

A Balanced Security Strategy

To  navigate  the  challenges  of  today’s  security  ecosystem,  businesses  must  think  about  implementing
a balanced approach to security – one that addresses advanced threats specific to their industry while
ensuring foundational security measures are firmly in place.

Relying  on  a  single  security  tool  or  solution  is  no  longer  sufficient.  Organizations  should  implement  a
multi-layered strategy that protects against common attack vectors while addressing threats unique to
their business sector. This strategy should include:

•  Next-Gen Spam/Malware detection with ATP for behavioural analysis to protect against the contin-

ued barrage of email-based threats we see in this industry

•  End-User  Security  Awareness  Training  to  train  end-users  to  spot  social  engineering  attacks  and

spear-phishing attacks

•  Backup and recovery capabilities for BOTH on-premises data and data that lives in cloud services such

as M365 for recovery purposes should a ransomware attack get through

•  Compliance  and  governance  features  that  help  protect  against  accidental  data  leakage  and  ensure

that compliance controls are met.

Learning More

The methods mentioned here regarding how to keep your business safe are just the beginning. Amongst
the risk management, the vendor assessments, and the training are ever changing regulations and secu-
rity  requirements.  Not  every  organization  can  be  an  expert  when  it  comes  to  security.  Make  sure  that
you’re leveraging trusted vendors that enable you to not only keep your business safe but allow you to
take advantage of their deep knowledge in cybersecurity. For example, maybe your security staff has deep
knowledge regarding data loss prevention, but knowledge of advanced email attacks is lacking. By part-
nering with a trusted security vendor like Hornetsecurity you will be able to leverage the vendor’s knowl-
edge as well as your own. Collectively we can all work together to enhance security, so be sure to reach out
to your security vendors to learn more and see how you can more closely work together.

34

35

ABOUT THE AUTHORS

W R I T T E N   B Y

Andy Syrewicze

Andy has over 20 years’ experience in providing technology solutions across sev-
eral industry verticals. He specializes in Infrastructure, Cloud, and the Microsoft 365
Suite.

Andy holds the Microsoft MVP award in Cloud and Datacenter Management and is
one of few who is also a VMware Expert.

Paul Schnackenburg

Paul Schnackenburg started in IT when DOS and 286 processors were the cutting
edge. He runs Expert IT Solutions, a small business IT consultancy on the Sunshine
Coast, Australia. He also works as an IT teacher at a Microsoft IT Academy.

Paul is a well-respected technology author and active in the community, writing
in-depth technical articles, focused on Hyper-V, System Center, private and hybrid
cloud and Office 365 and Azure public cloud technologies.

He holds MCSE, MCSA, MCT certifications.

36

CHAPTER 5
RESOURCES

•  https://attack.mitre.org/techniques/T1027/006/

•  https://github.com/kgretzky/evilginx2

•  https://www.techtarget.com/searchSecurity/definition/double-extortion-ransomware

•  https://www.csoonline.com/article/569273/what-is-smishing-how-phishing-via-text-message-

works.html

•  https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/

•  https://youtu.be/SScaV2PjFcg?si=lvjyfnk7YmwUUnVh

•  https://www.hornetsecurity.com/en/blog/category/threat-reports/

•  https://www.youtube.com/watch?v=o3JFNaNES0Q&list=PLyKOQlbp_zWzsfkSUQ0F-

Ved_0bZXts70W&index=13

•  https://www.propublica.org/article/microsoft-solarwinds-golden-saml-data-breach-russian-

hackers

•  https://www.cisa.gov/resources-tools/groups/cyber-safety-review-board-csrb

•  https://www.microsoft.com/en-us/trust-center/security/secure-future-initiative?mso-

ckid=35a127b0490c698b23e234bd4819680d

•  https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility

•  https://techcommunity.microsoft.com/t5/microsoft-syntex-blog/welcome-to-microsoft-inspire-

2023-introducing-microsoft-365/ba-p/3874887

•  https://www.hornetsecurity.com/us/services/365-multi-tenant-manager/

•  https://techcrunch.com/2024/02/29/unitedhealth-change-healthcare-ransomware-alphv-black-

cat-pharmacy-outages/

•  https://en.wikipedia.org/wiki/2024_National_Public_Data_breach

•  https://cybernews.com/security/mgm-caesars-ransomware-attack-timeline/

•  https://www.theverge.com/2024/9/13/24243986/23andme-settlement-dna-data-breach-lawsuit

•  https://www.nationalcrimeagency.gov.uk/news/lockbit-leader-unmasked-and-sanctioned

•  https://en.wikipedia.org/wiki/XZ_Utils_backdoor

•  https://www.cisa.gov/resources-tools/resources/CSRB-Review-Summer-2023-MEO-Intrusion

•  https://www.bleepingcomputer.com/news/security/ransomware-rakes-in-record-breaking-

450-million-in-first-half-of-2024/

•  https://www.politico.eu/article/eu-commission-national-security-does-not-justify-spying-docu-

ment/

37

•  https://home.treasury.gov/news/press-releases/jy2581

•  https://virtualizationreview.com/Articles/2024/03/25/exposure-management.aspx

•  https://wca.org/security-attacks-on-iot-devices-surge-by-107-in-early-2024/

•  https://atlas.mitre.org/matrices/ATLAS

•  https://attack.mitre.org/matrices/enterprise/

•  https://www.infosecurity-magazine.com/news/156-increase-in-oss-malicious/

•  https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-

encryption-standards

•  https://www.microsoft.com/en-us/security/blog/2023/11/01/starting-your-journey-to-become-

quantum-safe

•  https://techcommunity.microsoft.com/t5/security-compliance-and-identity/microsoft-s-quantum-

resistant-cryptography-is-here/ba-p/4238780

•  https://github.com/microsoft/SymCrypt

•  https://en.wikipedia.org/wiki/Buffer_overflow

•  https://en.wikipedia.org/wiki/Dangling_pointer

•  https://securityboulevard.com/2024/10/eu-cra-good-intentions-impossible-requirements/

•  https://pubs.opengroup.org/security/zero-trust-commandments/

38