# Global Threat Intelligence Report October-December 2023 Q4

## Table of Contents
- [INTRODUCTION](#introduction)
- [EXECUTIVE SUMMARY](#executive-summary)
- [KEY FINDINGS](#key-findings)
- [EXTORTION CAMPAIGNS GROW, CYBERATTACKS FOLLOW GEOPOLITICS](#extortion-campaigns-grow-cyberattacks-follow-geopolitics)
- [QUARTER FOUR 2023 IN CHARTS](#quarter-four-2023-in-charts)
  - [01. SMBs encounter twice as many threats](#01-smbs-encounter-twice-as-many-threats)
  - [02. malicious links on the rise](#02-malicious-links-on-the-rise)
  - [03. phishing dominated & links the most common vector](#03-phishing-dominated--links-the-most-common-vector)
  - [04. attacks increase across industries, HR-focused attacks subside](#04-attacks-increase-across-industries-hr-focused-attacks-subside)
  - [05. top vulnerabilities over time](#05-top-vulnerabilities-over-time)
- [BRAND ABUSE BECOMES MORE CONVINCING](#brand-abuse-becomes-more-convincing)
  - [Attackers use different brands depending on context](#attackers-use-different-brands-depending-on-context)
  - [File-share abuse is about brands](#file-share-abuse-is-about-brands)
- [THREAT ASSESSMENT](#threat-assessment)
- [MAJOR EVENTS Q4](#major-events-q4)
- [TOP THREAT CAMPAIGNS Q4](#top-threat-campaigns-q4)
  - [Microsoft QR codes](#microsoft-qr-codes)
  - [DocuSign QR codes](#docusign-qr-codes)
  - [Mexico Bank fraud spam campaign](#mexico-bank-fraud-spam-campaign)
  - [Meta Instagram impersonation campaigns](#meta-instagram-impersonation-campaigns)
  - [Google App Script attacks](#google-app-script-attacks)
- [TOP ADVISORIES](#top-advisories)
- [HOW TO TAKE ACTION](#how-to-take-action)
  - [Threat-specific countermeasures](#threat-specific-countermeasures)
  - [General recommendations to combat threats](#general-recommendations-to-combat-threats)
  - [Steps specific to Mimecast customers](#steps-specific-to-mimecast-customers)
- [CONCLUSION](#conclusion)
- [RESOURCES](#resources)

## INTRODUCTION

Too often, organizations receive threat intelligence as individual analyses of specific incidents, giving security teams a narrow view of the threat landscape. In this Global Threat Intelligence Report, Mimecast aims to put the previous three months’ worth of incidents into context and give companies the tools they need to understand where attackers are headed and where defenses could be improved.

Mimecast generates threat intelligence through its analysis of 1.7 billion emails per day on behalf of more than 42,000 customers. Because email is the channel through which most cyber threats launch, Mimecast sees many new threats before they become widely known.

This report distills insights from the intelligence Mimecast generated throughout the fourth quarter of 2023 and combines it with external intelligence from the cybersecurity community at large. It includes an analysis of threat activity, a series of top-line statistics that shaped that activity, and recommendations for what small businesses and large enterprises alike can do to mitigate the risk those threats pose.

We invite you to explore our Q4 2023 threat intelligence report. We look forward to sharing more insights in the future.

![Graphic showing +1.7 Billion emails per day] **+ 1.7 Bill** emails per day
![Graphic showing 42,000 customers] **42 000** customers

> **Mimecast Threat Intelligence team**
> Mimecast’s threat intelligence team is comprised of a globally distributed set of engineers, scientists, analysts, and threat researchers that aid the Mimecast Security Operations Center (MSOC). Threats are continuously monitored across more than 1.7 billion emails per day. Mimecast’s cybersecurity experts reverse-engineer attack tools, investigate attacks, and test the efficacy of indicators of compromise to quickly develop threat intelligence and protections across its solutions.

## EXECUTIVE SUMMARY

The fourth quarter of 2023 saw attackers continuing to shift their delivery methods toward using links for initial payloads, slowly moving away from sending malware as email attachments. In addition, threat actors are increasingly using QR codes to get around defenses designed to block malicious links and obfuscate their attacks.

Following attacks on major casinos earlier in the year, attackers continued to focus on travel, hospitality, and catering companies in Q4 2023, resulting in the sector becoming the second most targeted industry for the quarter, surpassed only by attackers’ efforts against the banking sector. While campaigns directed at human resources and recruitment services have subsided somewhat, the sector remains the third most targeted.

## KEY FINDINGS

![Graphic representing Q4]

- **Sectors**
  The sectors that experienced the most attacks in the fourth quarter of 2023 were financial institutions; travel, hospitality, and catering; and human resources and recruitment services. These attacks were driven by ransomware, data theft, and business email compromise (BEC). Additionally, across all industries, average users at small and medium-sized firms encountered more than twice the number of threats as those at large companies.

- **Links vs. Attachments**
  For the first time, the average user was more likely to encounter a malicious link than a malicious attachment in Q4 2023. In the past, attackers were more likely to use known malware to deliver payloads.

- **Geopolitics**
  Geopolitical tensions have increased, leading to more cyberattacks with more than 100 hacker groups claiming participation in the Israel-Gaza conflict alone. Nation-states are using cyber operations to gather intelligence on rival governments and attack critical infrastructure and information systems.

- **Generative AI**
  Attackers are using generative AI and machine-learning models to create more convincing phishing lures and translate attacks into other languages. Technical threat indicators, such as domain reputation, browser isolation, and malware analysis, will be increasingly necessary to block attacks.

- **QR Codes**
  A surge in using QR codes to obfuscate links has continued, serving the same purpose as URL shortening schemes but with an additional benefit to attackers, as victims have already become acclimated to snapping pictures of QR codes.

## EXTORTION CAMPAIGNS GROW, CYBERATTACKS FOLLOW GEOPOLITICS

Ransomware and breach-for-ransom campaigns continued to grow in Q4 2023, with one of the larger groups, ALPHV Blackcat, compromising more than 1,000 victims with ransomware and data extortion and reaping more than $300 million in ransom payments by the end of the quarter.

Attack strategies have evolved from crypto-ransomware (where attackers encrypt data and hold the decryption key) to breach-for-ransom campaigns (where attackers steal sensitive data and threaten to release the sensitive information unless paid) to double- and triple-extortion strategies (where attackers combine tactics for more direct consequences).

Ransomware and information-stealing groups have started using more sophisticated techniques, such as stealing tokens and account identifiers from Google Chrome. These successful tactics have led to a consolidation of the number of ransomware tools — with 43 malware families used for extortion in 2023, down from 95 in 2022 — signaling that cybercriminals and their affiliates are settling on a known set of popular platforms. Four groups — LockBit, Cl0p, ALPHV/BlackCat, and Play — dominated the ransomware landscape during the quarter, accounting for 88% of all ransomware activity.

However, while ransomware and data-breach incidents increased in 2023, companies are resisting extortion attacks. Ransom payment rates have plummeted, hitting a low of 34% in Q2 2023, down from 85% at the beginning of 2019. (The rate that companies acquiesced to ransom demands ticked up slightly in Q3 2023.) Three shifts in business security operations and the economics of ransomware are likely driving the change: Companies are less trusting of cybercriminals’ ability to recover data; organizations have had time to (slowly) improve their security posture; and paying ransoms to threat actors from certain nation-states now violates federal laws.

Ransomware groups are aiming to reverse the trend. Starting on Oct. 1, the LockBit ransomware group put in place new rules regarding negotiations with victims, warning its “affiliates” that offering large discounts on ransom fees is no longer acceptable.

The geopolitical situation deteriorated with the Oct. 7 terrorist attack on Israel by the militant group Hamas. Like other global conflicts, such as Russia’s invasion of Ukraine, cyberattacks have increased significantly as nation-state cyber operations, groups linked to either side, and hacktivist supporters ramped up their attacks against web sites, critical infrastructure, and computer systems. At least 90 pro-Palestinian threat actors and 23 pro-Israeli threat actors conducted attacks in Q4 2023.

There are already some signs that machine-learning models and generative AI are changing the threat landscape as well. For example, phishing lures are becoming much more convincing and easier to tailor to specific geographies because of the adoption of generative AI by threat actors, according to Mimecast’s threat intelligence team. In addition, researchers have been able to upload malicious code to GitHub linked to machine-learning components, such as PyTorch, like attacks on other open-source supply chain components.

## QUARTER FOUR 2023 IN CHARTS

The sectors that experienced the most attacks in the fourth quarter of 2023 were financial institutions; travel, hospitality, and catering companies; and human resource departments. These attacks were driven by ransomware, data theft, and BEC.
Additionally, across all industries, typical users at small and medium-sized firms encountered more threats — on average, twice as many — compared to users at large companies.

### 01. SMBs encounter twice as many threats

**Encounter rates: SMBs encounter twice as many threats**

The significant uptick in threats seen in Q3 seems to have subsided, but medium-sized companies still saw slightly more threats per user (TPU) than smaller firms in Q4. Average users at small and medium-sized businesses (SMBs) encountered more than twice the number of threats — 31 and 32 TPU, respectively — than users at large companies, who saw about 15 TPU in Q4.

The larger risk for SMBs is due to a greater share of employees in critical roles; targeting those users results in a higher level of threats per user. In addition, because SMBs rely on credential-based cloud services for much of their operations, attackers are more focused on credential theft, a common phishing goal.

The fourth quarter of each year tends to see a lower volume of threats, compared to the preceding quarter, so the drop in TPU across all organizations is common.

![Figure 1. Threats per user by company size chart showing TPU from Q2 2022 to Q4 2023 for All, Small, Medium, and Large companies. Large companies consistently have lower TPU (around 15 in Q4 23), while Small and Medium fluctuate higher (around 31-32 in Q4 23).]

### 02. malicious links on the rise

**Encounter rates: malicious links on the rise**

Spam and impersonation both declined in Q4 2023 but continued to dominate malicious activity directed at users’ email inboxes, with Mimecast defenses blocking 9.5 and 6.3 emails classified as either spam or impersonation, respectively, per average user. The unknown malware category, which Mimecast blocks based on detecting exploit code in attachments, is too small to be visible on the first chart.

By removing the two largest categories of threats — spam and impersonation — another trend becomes evident. In Q4, for the first time, the average user was more likely to encounter a malicious link than a malicious attachment. With users ignoring the overwhelming volume of email messages blocked as either spam or impersonation (phishing), attackers are clearly shifting from delivering payloads as malware to sending links to malicious sites, which then deliver the payload.

![Figure 2a. Threats per user by type of threat chart showing Spam and Impersonation as the highest volume threats from Q2 2022 to Q4 2023, with Spam around 9.5 and Impersonation around 6.3 TPU in Q4 2023. Known malware and Malicious links are much lower.]

![Figure 2b. Threats per user for malware & malicious links chart showing Known malware, Malicious links, and Unknown malware from Q2 2022 to Q4 2023. In Q4 2023, Malicious links (around 1.2 TPU) surpassed Known malware (around 1.0 TPU) for the first time. Unknown malware is negligible.]

### 03. phishing dominated & links the most common vector

**Threat types: phishing dominated active threats, with links the most common vector**

While spam continues to account for the largest volume of malicious and suspicious email messages rejected, accounting for 86% of all blocked messages (see Figure 3(a)), looking at the top threats apart from spam highlights interesting trends (see Figure 3(b)).

![Figure 3a. Relative volume of all threats pie chart showing Spam (86%), Phishing (9%), Suspicious (2%), Malware (2%), Unwanted (1%).]

Malicious URLs continue to make up the largest portion of all major detection types, including phishing, malware, and suspicious and unwanted emails. Credential harvesting is the second most identified attribute of phishing attacks, underscoring the importance of strong credentials — and hardening them with multifactor authentication — to protect businesses as they increasingly adopt cloud services and infrastructure.

![Figure 3b. Malware and malicious links breakdown chart showing detailed categories within Phishing (Blocked URL 48%, Credential Harvesting 35%, etc.), Suspicious (Blocked URL 56%, Malicious File 44%), Malware (Blocked URL 57%, Exploit 19%, etc.), and Unwanted (Blocked URL 100%).]

### 04. attacks increase across industries, HR-focused attacks subside

**Industry snapshot: attacks increase across industries, while HR-focused attacks subside**

The average number of attacks, excluding spam and impersonation, fell in Q4 2023, with users in the formerly most attacked sector — human resources and recruitment services — encountering 60% fewer threats than in the previous quarter, causing that sector to drop to third place in Q4 2023. Meanwhile, the IT software and software as-a-service sector dropped out of the top five most targeted sectors, falling all the way to No. 20 in Q4 2023.

However, the remaining sectors all saw increases in the most significant threats, which include known malware, malicious links, and unknown malware, over the prior quarter. Users in the banking sector continued to encounter a significant number of attacks, as did users in the travel, hospitality, and catering industry, which includes casinos. The average user across all industries encountered 1.2 threats during the quarter, slightly less than the average of 1.3 threats per user in Q3 2023.

![Figure 4. Top 5 threats per user by Industry for malware & malicious links chart comparing Q1-Q4 2023. Q4 shows Finance & Banking highest (around 7 TPU), followed by Travel, Hospitality & Catering (around 6 TPU), HR & Recruitment (around 3 TPU), Admin & Support (around 2.5 TPU), and Other Financial Services (around 2 TPU).]

### 05. top vulnerabilities over time

**Vulnerability snapshot: top vulnerabilities over time**

The total number of vulnerabilities decreased over the quarter, which is a typical pattern for the fourth quarter as businesses close and both attackers and victims take a break at the end of the year.

The top-5 vulnerabilities showed distinct usage patterns. The most common vulnerability used in malware — a remote code execution flaw in the Equation Editor in Microsoft Office 2007 through 2016 (CVE-2018-0802) — was the workhorse of attackers in Q4 2023. Another attack exploiting a memory corruption vulnerability in Microsoft Office (CVE-2017-11882) saw minimal use until a spike in the third week of November corresponding with the most popular shopping days of the year.

Only a single vulnerability in the top-5 list — and only two in the top-10 list — were from 2023, highlighting the notion that attackers tend to prefer exploiting what they deem to be the most vulnerable software, even if the exploited flaw tends to be old.

![Figure 5a. Total vulnerabilities blocked in Q4 2023 line chart showing weekly totals decreasing from around 6000-8000 early in the quarter to below 2000 by the end of December.]

![Figure 5b. Top 5 vulnerability detections for Q4 2023 line charts showing weekly detection counts for CVE-2018-0802 (consistently high), CVE-2017-11882 (spike late Nov), CVE-2022-42889, CVE-2016-7262, and CVE-2023-38831 (lower, variable usage).]

## BRAND ABUSE BECOMES MORE CONVINCING

Almost every type of email attack uses legitimate brands to gain trust and convince users to take actions that undermine their security, such as parting with sensitive information or clicking on links. During Q4 2023, for example, one threat actor used SendGrid’s email marketing service to send out email campaigns that impersonated human resource departments and asked targeted users to click on a link that appeared to be from a Microsoft SharePoint Online server.

As attackers increasingly use generative AI to create official-sounding notifications and abuse legitimate services to bypass reputation-focused defenses, brand abuse will only become more problematic.

Meanwhile, attackers are using QR codes to obfuscate the destination of a link, while also relying on branding to convince users that QR codes are from official sources. This has moved from a niche attach methodology to mainstream as seen with emails that contain QR codes exceeding 3.5 million per day regularly (see figure 7). Mimecast has documented two major campaigns using QR codes — one branded as Microsoft password reset and the other as DocuSign.

![Figure 7. QR Code detection over 60 days line chart showing daily detections from Nov '23 to Jan '24, frequently exceeding 3.5 million.]

### Attackers use different brands depending on context

The perennial impersonated brand is Microsoft, as data from our Q3 2023 report demonstrated. However, specific events may result in attackers using other brands to attempt to gain trust. In 2020, during the coronavirus pandemic, for example, Amazon, Apple, and the Social Security Administration were the top-three most impersonated brands.

In Q4, attackers again switched up their brand-impersonation tactics. Looking to capitalize on the holiday shopping season, fraudsters ramped up their impersonation of Amazon, leading to a spike of spam and phishing detections for the brand. During the two weeks before Black Friday, considered to be the start of the holiday shopping season in the United States, Mimecast detected more Amazon-branded threats than Microsoft-branded threats.

![Figure 6. Attackers switch focus to Amazon prior to holiday shopping line chart showing weekly detection counts for Microsoft and Amazon branded threats from Oct to Dec 2023. Amazon detections spike above Microsoft detections in mid-November before Black Friday.]

### File-share abuse is about brands

Attackers increasingly are using links rather than attachments for payloads — whether the payload is a phishing site for stealing credentials or malware for the victim to download. To escape detection by security solutions and garner users’ trust, attackers are widely using file-sharing sites that have trusted brands to serve up malicious content (see figure 8).

The top brand for file-sharing sites for the past three quarters is the notetaking and sharing service Evernote. Microsoft SharePoint comes in a distant second, while ShareFile managed storage service follows in third place.

![Figure 8. Evernote tops popular domains for phishing attacks bar chart showing relative usage of domains like evernote.com, sharepoint.com, sharefile.com, box.com, google.com, etc., with evernote.com having the highest bar.]

## THREAT ASSESSMENT

Attackers have doubled down on techniques for bypassing multifactor authentication (MFA) mechanisms. EvilProxy, a phishing-as-a-service (PhaaS) platform, targeted the financial and insurance industries with an attack that uses a proxy to bypass MFA, while another group used the DadSec PhaaS platform to send victims to a proxy that acts as an adversary-in-the-middle (AitM) to capture MFA requests and compromise victims’ Microsoft 365 accounts.

Ransomware operators have continued to increase their focus on energy companies in Q4. Initial access brokers (IABs) actively sought out credentials and compromised systems within the networks of energy operators.

Nation-state cyber conflicts heated up following the terrorist attack by Hamas on Israeli civilians and Israel’s military response and invasion of Gaza. Added to the online operations that continue as part of the Russian-Ukraine conflict, state-sponsored cyberattacks have become more common.

## MAJOR EVENTS Q4

- **1 Oct**
  **Phishing Attacks Continue Against Hospitality Sector**
  Attackers targeted the hospitality sector with sophisticated phishing attacks, leading to breaches such as those of MGM and Caesars. Mimecast data shows the hospitality sector was the No. 2 target in Q4.
  [READ ARTICLE](#)

- **3 Oct**
  **EvilProxy Phishing Attack Targets U.S. Firms**
  Researchers describe an attack using emails disguised as notifications from job board Indeed.com that had a redirection vulnerability. The attack was launched through PHaaS platform EvilProxy and targeted executives in the banking and insurance industries.
  [READ ARTICLE](#)

- **9 Oct**
  **Hacktivists Race into Israel-Hamas War on Both Side**
  Dozens, and more likely hundreds, of sites and networks came under attack as cyber operations ramped up following Hamas’ terrorist attack on Israel and Israel’s subsequent military response. The International Committee of the Red Cross released rules of engagement for civilian hackers to minimize harm to civilians during the war.
  [READ ARTICLE](#)

- **17 Oct**
  **Attackers Combine DadSec Phishing, Cloudflare**
  In what has become a typical combination to bypass two-factor authentication, an AitM phishing attack used fake emails containing a link, Cloudflare’s Turnstile tool for human verification, and a fake Microsoft 365 site to convince users to part with their log-in credentials and their two-factor codes.
  [READ ARTICLE](#)

- **18 Oct**
  **State-Sponsored Actors Target WinRAR Flaw**
  The Russia-linked threat actor Sandworm, also known as FrozenBarents and Black Energy, impersonated a Ukrainian drone warfare training school and sent out a malicious ZIP file exploiting a vulnerability in the WinRAR archiving utility.
  [READ ARTICLE](#)

- **6 Nov**
  **Iranian Group Targeting Israeli Sectors**
  The Iran-linked group Agonizing Serpens continued a campaign of data-theft and wiping attacks aimed at Israel’s higher education and technology sectors. The attacks are not related to ransom but aim to cause massive data loss.
  [READ ARTICLE](#)

- **12 Nov**
  **Energy Sector Faces Increasing Attacks During Winter**
  IABs are actively seeking out stolen credentials and other methods of compromising energy networks. Reported ransomware attacks on the energy sector increased through the latter part of 2023, especially in North America, Asia, and the European Union (EU).
  [READ ARTICLE](#)

- **29 Nov**
  **Financial Service Phishing Delivers LUMMA Malware**
  Phishing emails using fake invoices led to a malicious site that redirects users to a JavaScript file that installs the information stealing LUMMA malware.
  [READ ARTICLE](#)

- **6 Dec**
  **ChatGPT Protections can be Bypassed to Create Phishing Email**
  The BBC used the paid version of ChatGPT and prompt engineering to create a private bot dubbed Crafty Emails that performed nearly all the malicious phishing tasks requested by the news service. The service created variations of popular scams, such as the “Hi Mum” scheme asking for money from a parent and spear-phishing emails. The bot made creating culturally distinct versions easy as well.
  [READ ARTICLE](#)

- **19 Dec**
  **Law Enforcement Shutter ALPHV Site**
  The data-leak and negotiation sites for the ALPHV/BlackCat ransomware gang disappeared from the Internet, following reported action by law enforcement. The U.S. Department of Justice claimed to have shut down the sites and offered 500 victims a decryption tool, but the group later reportedly recovered access to the sites.
  [READ ARTICLE](#)

## TOP THREAT CAMPAIGNS Q