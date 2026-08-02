# Special Report: Mandiant M-Trends 2026

## Table of Contents
- [Introduction](#introduction)
- [By the Numbers](#by-the-numbers)
- [Campaigns & Global Events](#campaigns--global-events)
- [Targeted Attacks](#targeted-attacks)
  - [Targeted Industries](#targeted-industries)
  - [Initial Infection Vector](#initial-infection-vector)
  - [Most Frequently Exploited Vulnerabilities](#most-frequently-exploited-vulnerabilities)
  - [Global Detection by Source](#global-detection-by-source)
  - [Global Median Dwell Time](#global-median-dwell-time)
  - [Global Dwell Time Distribution](#global-dwell-time-distribution)
  - [Post-Compromise Activity](#post-compromise-activity)
  - [Insider Threat](#insider-threat)
  - [Malware](#malware)
  - [Threat Groups](#threat-groups)
- [Ransomware](#ransomware)

---

## Introduction

M-Trends serves as a definitive look at the threats and tactics used in breaches, grounded in over 500k hours of frontline incident investigations conducted by Mandiant in 2025. Together with Google Threat Intelligence Group (GTIG), we have a comprehensive view of the modern threat landscape, and emerging threats that may drive future attacks.

One of the dynamics influencing the threat landscape is AI. Recent GTIG reporting confirms that state-sponsored and financially motivated actors are integrating AI to accelerate the attack lifecycle. Attackers are increasingly relying on large language models (LLMs) as a strategic force multiplier to move beyond mass email campaigns toward hyper-personalized, rapport-building social engineering. In the wild, malware families like PROMPTFLUX and PROMPTSTEAL actively query LLMs mid-execution to evade detection, while "distillation attacks" threaten intellectual property by extracting the proprietary logic and specialized training data of high-value machine learning models.

To ensure organizations are prepared for these evolving capabilities, Mandiant red teams are actively incorporating these AI-driven techniques into engagements, rigorously testing defenses against emerging threats. However, despite threat actors increasingly leveraging AI, especially during the early phases of the attack lifecycle, we don’t consider 2025 to be the year where breaches were the direct result of AI.

From our view on the frontlines, the vast majority of successful intrusions still stem from human and systemic failures. M-Trends 2026 contains these critical insights that organizations must think about today, alongside the actionable guidance required to stay ahead of modern threats.

We are tracking a significant shift toward voice-based social engineering (vishing), which has risen to the number two spot for initial infection vectors. Exploits remain the most common vector for a sixth consecutive year. Furthermore, our investigations highlight a rising "hand-off" trend, where one threat actor gains initial access, and then provides access to a separate actor that typically conducts higher impact operations like ransomware. This hand-off is happening so fast (sometimes under 30 seconds) that it creates a scenario where alerts traditionally considered "lower priority" can very quickly become significant compromises.

Other M-Trends 2026 observations include:

- **Global median dwell time has risen to 14 days** from 11 days, driven largely by long-term espionage and DPRK IT worker operations. The longer adversaries remain undetected, the greater the cost and complexity of remediation.
- **Financially motivated and cyber espionage groups continue to abuse native functionalities** in on-premises and cloud environments, as well as legitimate tools, to reduce opportunities for detection. This means traditional endpoint security relying on malware signatures is not sufficient.
- **Ransomware operators have shifted their primary objective from data theft to deliberate recovery denial**, systematically targeting backup infrastructure, identity services, and virtualization management planes. By destroying the ability to recover, threat actors put immense pressure on organizations to pay ransom demands.

Mandiant converts frontline observations into the strategic intelligence required to help organizations fortify their defenses. To defend against the activity in M-Trends 2026, organizations should prioritize the security of infrastructure such as backups, identity services, and the virtualization layer, which attackers are now systematically targeting to deny recovery. Hardening edge and core network devices remains critical, especially since exploits continue to be the most common entry point for adversaries. By addressing these specific visibility gaps and focusing on the tactics that actually bring attackers success, defenders will strengthen their cyber resilience.

Mandiant consultants operate globally on the frontlines of the latest cyber incidents, observing the most relevant adversary tactics, techniques, and procedures (TTPs). This perspective provides us with a unique understanding of the modern threat landscape, and the strategies required to defend against it. We translate this intelligence into action by proactively hardening client environments against these TTPs, and helping them feel confident in their cybersecurity readiness. The information in this report has been sanitized to protect the identities of targeted organizations and their data.

---

## By the Numbers

Since 2010, Mandiant has provided statistics and analysis of threats observed in the previous year's incident investigations. In M-Trends 2026, Mandiant examines data collected from more than 500,000 hours of incident response engagements globally, highlighting trends and significant insights.

This information can be useful to inform risk assessments and to support planning for threat hunts, which can improve an organization’s abilities to counter future threats effectively. The metrics contained in By The Numbers are based on targeted attack activity identified by Mandiant between Jan. 1 and Dec. 31, 2025.

---

## Campaigns & Global Events

Campaigns are a set of impactful intrusions conducted by an attacker or multiple attackers in cooperation toward a single objective at multiple targets within a relevant time frame.

Global Events are a set of impactful intrusions conducted by multiple unrelated adversaries in parallel campaigns involving a similar theme, target, or resource.

To provide a comprehensive view of the global threat landscape, Google Threat Intelligence Group (GTIG) tracks impactful activity through two distinct categories: Campaigns and Global Events. Campaigns represent focused efforts by one or more threat groups pursuing a single objective, while Global Events encompass multiple groups using similar tactics, such as exploiting a new vulnerability. These records are continuously updated with new indicators of compromise (IOCs), tactics, techniques, and procedures (TTPs), and affected industries and regions. Whenever possible, GTIG provides examples, context, and information about threat cluster behaviors, tools, and malware, as well as actionable defensive and preventative measures. This intelligence is based on real-world data collected from Mandiant investigations and GTIG research, enabling our clients to respond effectively and decisively to active threats at first discovery and as they evolve.

In 2025, GTIG initiated 83 campaigns and eight global events and continued to track activity identified in previous years. These campaigns affected every industry vertical and 73 countries across six continents based on GTIG’s direct observations. A subset of this activity—specifically 35 campaigns and six global events—include incidents that Mandiant investigated. Insights drawn from the investigations provide deep forensic insight into these events and broader trends.

The diagram below summarizes the Campaigns and Global Events. Prominent examples include the exploitation of CVE-2025-31324 in SAP NetWeaver, and the data theft extortion campaign exploiting a zero-day vulnerability and using GOLDVEIN.JAVA.

One of the most active global events was the growing adoption of the ClickFix social engineering technique, which involves clusters using a prompt, typically on a phishing page, to convince users to execute PowerShell or other system-level commands under the guise of fixing problems or verifying their legitimacy. Variants of the technique observed in 2025 used a variety of lures, including CAPTCHAs, verifications for video conference and meeting invitations, driver or operating system updates, and enterprise software compliance verification. In 2025, GTIG identified dozens of threat clusters incorporating this technique, particularly threat clusters focused on widespread initial access operations.

![2025 Campaigns and Global Events Related to Mandiant Incident Investigations Diagram]

---

## Targeted Attacks

### Targeted Industries

An industry category describes an organization’s primary industry. Organizations are typically assigned to only one category that best describes its primary industry, though many organizations have links to multiple industries. For example, a cryptocurrency exchange relates both to the financial and technology sectors, but for the purposes of this section, it would be categorized as a financial sector organization.

In 2025, Mandiant responded to incidents in the high-tech sector most frequently, followed by the financial sector, business and professional services, and healthcare. These sectors consistently appear at the top of the list for industry distribution, though in 2025 investigations in the high-tech sector outpaced those of financial sector organizations, which had the largest share of Mandiant investigations in 2024 and 2023.

#### Targeted Industries, 2025

| Industry | Percent of Investigations |
| --- | --- |
| High Tech | 17% |
| Financial | 14.6% |
| Business and Professional Services | 13.3% |
| Healthcare | 11.9% |
| Retail and Hospitality | 7.3% |
| Government | 5.8% |
| Education | 4.6% |
| Telecommunications | 4.6% |
| Construction and Engineering | 4.1% |
| Entertainment and Media | 4.1% |
| Transportation and Logistics | 3.4% |
| Aerospace and Defense | 2.7% |
| Energy | 2.2% |
| Utilities | 2.2% |
| Other | 1.5% |
| Agricultural and Forestry | 0.5% |
| Nonprofits | 0.2% |

---

### Initial Infection Vector

For the sixth year running, exploits represented the most frequently observed initial infection vector in 2025 Mandiant incident response investigations. Exploits comprised 32% of investigations in which an initial infection vector could be identified.

#### Initial Infection Vector, 2025

- **Exploit**: 32%
- **Voice Phishing**: 11%
- **Stolen Credentials**: 9%
- **Prior Compromise**: 8%
- **Web Compromise**: 8%
- **Email Phishing**: 6%
- **Insider Threat**: 6%
- **Third-Party Compromise**: 5%
- **Other**: 13%

In 2025, threat clusters used an increasingly diverse array of social engineering tactics across email, voice, messaging platforms, and social media. To capture this nuance, GTIG has refined these categories to distinguish between interactive human engagement, such as voice phishing and non-interactive technical lures, such as email phishing. While email phishing often relies on volume and opportunistic delivery, interactive methods involve a live person steering the conversation in real-time. This distinction is critical for defenders: interactive attacks are significantly more resilient against automated technical controls and require different detection strategies.

Globally, email phishing was no longer a top observed initial intrusion vector. At 6% of 2025 intrusions, it continues to see a steady decline from its 14% share in 2024. Conversely, the proportion of incidents stemming from social engineering through voice phishing and messaging apps noticeably increased in 2025 compared to prior years, with voice phishing emerging as the second-most commonly observed vector in 2025 investigations at 11%.

One of the more pervasive examples of this activity was a campaign that spanned the first half of 2025, in which UNC6040 used voice phishing to convince targets to provide credentials and authorize an attacker-controlled version of a legitimate software-as-a-service (SaaS) application to access organizations' data. These organizations later received ShinyHunters-branded extortion notes demanding payment for the non-release of stolen data. Given the significant time lapse between the initial data theft activity and the extortion operations, GTIG tracks the extortion activity as UNC6240. Another example of a long-term voice phishing campaign came from UNC3944, a financially motivated threat cluster that has been active since at least early 2022 and overlaps with public reporting on Scattered Spider. UNC3944 targeted help desk staff by impersonating employees requesting password resets and changes to multi-factor authentication (MFA) settings.

#### Email Phishing Declines as an Initial Infection Vector, 2022-2025

- **2022**: 22%
- **2023**: 17%
- **2024**: 14%
- **2025**: 6%

Though there was a decline in email phishing as an initial infection vector, email phishing continues to be a consistently leveraged tactic. For example, UNC6345 used a phishing email with malicious employee rewards and benefits-themed PDF to compromise a user. Successful email phishing has also been known to extend the reach of a compromise; for example, UNC3203 gained access to a Microsoft 365 environment, created mailbox forwarding rules to forward received emails to an external address, then leveraged the access to send phishing emails internally and externally. In a similar case, another threat cluster used phishing emails containing malicious attachments disguised as financial documents to deploy malware that uses Outlook COM automation to hijack targeted users' mailboxes and facilitate lateral movement.

Prior compromise was the third-most common initial infection vector across investigations performed in 2025. In 2024, prior compromise was the fifth-most common form of initial infection, found in 8% of investigations. Mandiant identified stolen credentials as the initial infection vector in 9% of 2025 investigations, which is a decline from 16% in 2024. Web compromise remained relatively stable at 8% of investigations.

The share of incidents traced back to malicious insiders increased from 5% in 2024 to 6% in 2025. Consistent with 2024, the majority of these insiders were North Korean IT workers, though Mandiant also identified evidence of financially motivated threat clusters bribing employees or contractors for their corporate credentials.

Third-party compromise represented 5% of identified initial infection vectors in 2025 investigations. This figure includes a number of incidents involving compromises of software-as-a-service (SaaS) platforms. Additional initial infection vectors included software supply chain compromise, brute force, server compromise, ClickFix, and SQL injection.

#### Initial Infection Vectors Definitions

- **Exploits** include initial access achieved by exploitation of a software vulnerability with a CVE identifier.
- **Social engineering** operations involve threat clusters attempting to trick targets into supplying credentials, downloading malware, or otherwise providing the attacker with access to sensitive information and/or systems. Commonly referred to as phishing, this can take place over email, the phone, chat or messaging applications, SMS, or social media.
- **Prior compromise** refers to incidents in which a threat cluster gained access to a targeted environment through a foothold established by a separate threat cluster.
- **Stolen credentials** can be sourced directly from infostealers, harvested from inadvertently exposed databases or source code repositories, or indirectly gathered from dark web forums or database leaks. These typically include incidents in which the first evidence of malicious activity is the threat actor logging on using valid credentials.
- **Web compromise** encompasses drive-by compromise, the use of malicious advertisements, search engine optimization (SEO) poisoning, and compromised websites.
- **Insider threat** describes compromises traced back to people within the organization, such as employees, former employees, contractors, or business associates who abuse or misuse their access, leading to attackers gaining information about an organization’s security practices, data, and computer systems.
- **Third-party compromises** occur when an attacker gains unauthorized access to accounts or infrastructure belonging to one organization and then uses that foothold to gain access to additional targets.

*For guidance regarding protecting credentials and securing against common initial infection vectors including stolen credentials, please see: [Keys to the Kingdom: A Defender’s Guide to Privileged Account Monitoring]*

*For additional resources about voice phishing threats, please see:*
- *[Hello, Operator? A Technical Analysis of Vishing Threats]*
- *[The Cost of a Call: From Voice Phishing to Data Extortion]*

---

### Most Frequently Exploited Vulnerabilities

The most frequently exploited vulnerabilities identified in 2025 Mandiant incident response investigations were zero-days affecting internet-facing web application servers. These vulnerabilities, either alone or chained with additional flaws, enabled unauthenticated code execution against enterprise platforms that provide centralized access to an organization’s financial data, business operations data, or internal documents. Threat clusters often see these types of targets as opportunities for reconnaissance and a beachhead from which they can expand further into a compromised network.

#### Key Vulnerabilities Observed:
- **SAP NetWeaver**: CVE-2025-31324
- **Oracle E-Business Suite**: CVE-2025-61882
- **Microsoft SharePoint**: CVE-2025-53770

#### CVE-2025-31324
CVE-2025-31324 is an improper authorization vulnerability in SAP NetWeaver Visual Composer, specifically in its Metadata Uploader component, allowing unauthenticated attackers to upload arbitrary files. This flaw can lead to unauthorized access and be chained with another vulnerability, such as CVE-2025-42999, to achieve code execution.

Mandiant responded to a number of incidents in which threat actors exploited CVE-2025-31324. GTIG observed evidence that at least four separately tracked threat clusters likely exploited CVE-2025-31324 as a zero day in early 2025. After SAP issued a patch in April 2025, GTIG tracked six additional threat clusters, including several suspected PRC-nexus cyber espionage clusters, exploiting the vulnerability as an n-day. The activities observed post compromise were limited to attackers establishing a foothold in targeted environments with web shells or backdoors and conducting reconnaissance.

#### CVE-2025-61882
CVE-2025-61882 is an improper authentication vulnerability affecting Oracle E-Business Suite (EBS) that allows an unauthenticated, remote attacker with network access to achieve arbitrary code execution. Mandiant investigated multiple incidents involving the exploitation of CVE-2025-61882.

In September 2025, a threat cluster claiming affiliation with the CL0P extortion brand sent extortion emails claiming that they had compromised organizations' Oracle E-Business Suite (EBS) applications and stolen documents. In related incident response engagements, Mandiant identified evidence of attempted exploitation of Oracle EBS dating back to July 2025, and successful exploitation in August 2025 that may constitute zero-day exploitation of CVE-2025-61882. Following exploitation, the threat actors deployed Java payloads, including GOLDVEIN.JAVA.

GTIG attributes this activity to a suspected FIN11 threat cluster based on several similarities with past FIN11 campaigns, including the use of the CL0P data leak site (DLS). The in-memory Java-based loader GOLDVEIN.JAVA that fetches a second-stage payload is reminiscent of the GOLDVEIN downloader and GOLDTOMB backdoor observed during the mass exploitation of the Cleo Managed File Transfer (MFT) vulnerability in late 2024, which was attributed to another suspected FIN11 cluster. More broadly, exploitation of a zero-day vulnerability in a widely used enterprise application, followed by a large-scale, branded extortion campaign weeks later is a hallmark of activity historically attributed to FIN11.

*For more information about the CVE-2025-61882 exploitation, please see: [Oracle E-Business Suite Zero-Day Exploited in Widespread Extortion Campaign]*

#### CVE-2025-53770
Microsoft SharePoint Server was affected by a deserialization of untrusted data vulnerability, CVE-2025-53770, which allows an unauthenticated, remote attacker to execute arbitrary code on the affected SharePoint server. This flaw can be chained with CVE-2025-53771 in an exploit known as ToolShell. CVE-2025-53771 is a path traversal and spoofing vulnerability that enables unauthorized access to SharePoint content, internal configurations, and system files, as well as the deployment of web shells and other post-exploitation activities.

Mandiant investigated several incidents involving exploitation of these vulnerabilities, and GTIG tracked evidence of widespread exploitation, including at least two threat clusters exploiting CVE-2025-53770 as a zero day, with an additional three threat clusters observed exploiting the flaws after the July 20 and 21 patches were released. Most observed post-compromise activity, including by suspected PRC-nexus cyber espionage threat cluster UNC6349, was focused on reconnaissance and establishing a foothold. In contrast, the financially motivated threat cluster UNC6357 exploited the SharePoint vulnerabilities to ultimately deploy the LOCKBIT.WARLOCK ransomware.

---

### Global Detection by Source

In 2025, 52% of organizations detected evidence of malicious activity internally. External entities, such as law enforcement, CERTs, or cybersecurity companies, notified organizations of a potential compromise in 34% of cases. Adversaries informed organizations of a compromise, typically in the form of a ransom note, in 14% of cases. The proportion of internally detected compromises increased from 43% in 2024 to 52% in 2025, while external entity notifications declined from 43% to 34%.

#### Global Detection by Source, 2025 Breakdown
- **Internal Detection**: 52%
- **External Entity Notification**: 34%
- **Adversary Notification**: 14%

*(Internal detection is when an organization independently discovers it has been compromised, such as through an internal security appliance alert or internal personnel notification of suspicious activity. External entity notification is when an outside entity informs an organization it has been compromised, such as law enforcement agencies, cybersecurity companies, or industry partners.)*

---

### Global Median Dwell Time

Global median dwell time across 2025 Mandiant investigations was **14 days**. This is an increase from 11 days in 2024. Median dwell time for incidents discovered internally in 2025 remained fairly consistent with 2024 at 9 days. Organizations were made aware of an incident by an external notification in 25 days in 2025, a significant increase in the external notification global median dwell time from 2024 (11 days).

#### Median Dwell Time by Detection Source, 2025
- **All**: 14 days
- **Adversary**: 7 days (Median dwell time for incidents in which adversaries notified organizations of a compromise, often in the form of a ransom demand, was seven days in 2025, slightly higher than five days in 2024.)
- **External Entity**: 26 days
- **Internal**: 9 days

---

### Global Dwell Time Distribution

Comparing dwell time distributions from 2024 to 2025 reveals a slight shift: very short dwell times decreased, while intermediate dwell times (one week to six months) saw a marginal increase. There was a small decrease in the share of incidents discovered in a week or less, down from 45.1% to 41.5%. The share of incidents that went undiscovered for more than a week to a month, showed a small increase from 17.6% to 20.1%. A similar increase was observed for incidents that remained undetected for one to six months, growing from 23.9% to 26.7%.

This observed shift toward longer dwell times likely reflects the quantity of incidents in which threat clusters prioritize maintaining long-term access to targeted environments, including cyber espionage, North Korean IT workers, and other types of compromises. Mandiant has directly observed these types of groups make concerted efforts to remain undetected. They leverage living-off-the-land (LotL) techniques, minimize use of custom malware, remove artifacts, favor obfuscation, and mimic legitimate products or system tools already present within the victim’s environment. The median dwell times for incidents assessed to be motivated by cyber espionage, as well as North Korean IT worker incidents, were both 122 days, or about four months.

The percentages of incidents discovered more than six months after the first evidence of malicious activity declined. Despite the shifts in the distribution of dwell times across our datasets from 2024 to 2025 revealing more dwell times in the intermediate range in 2025, the multi-year comparison of dwell time distribution continues to indicate that, in the long term, dwell times are getting shorter.

---

### Post-Compromise Activity

#### Financial Gain
Threat actors used monetization techniques in 30% of the investigations that Mandiant performed in 2025. This is a decline from 35% of 2024 incidents. 

- **Extortion-related intrusions** (which includes ransomware as well as data theft extortion without ransomware encryption): represented **23%** of 2025 intrusions and approximately three fourths of financially motivated intrusions.
- **Ransomware deployments** (attempted or successful): comprised **13%** of the incidents Mandiant investigated in 2025.
- **Multifaceted extortion** (incidents involving both ransomware encryption and data theft extortion): constituted **6%** of 2025 compromises.
- **No Observed Monetization**: **70%**

In addition to extortion-related incidents, Mandiant encountered threat clusters pursuing a variety of other monetization methods, including North Korean IT worker employment fraud, payment redirection fraud, selling access to compromised networks, ATM malware, use of web skimmers to capture credit card information, as well as theft of cryptocurrency, loyalty points, and gift card data.

#### Data Theft
Mandiant identified evidence of data theft in **40%** of investigations performed in 2025. This is slightly higher than the proportion from 2024 (37%). 

- **Data Theft Extortion**: Represented **10%** of investigations.
- **Multifaceted Extortion**: Represented **6%** of investigations.
- **No Observed Data Theft**: **60%**

In many of the 2025 investigations in which Mandiant identified evidence of data theft, threat actors targeted credentials and reconnaissance data useful for maintaining persistence, lateral movement, and escalating privileges. Other examples of data theft appeared to be wholesale and opportunistic. In several cases, threat actors targeted personally identifiable information (PII), such as customer records listing contact and order information. Mandiant identified threat clusters that used stolen PII in subsequent voice phishing attempts.

Mandiant responded to several incidents in which the threat actors targeted code repositories that they subsequently mined for credentials and keys, including several compromises attributed to UNC6395. Mandiant identified several cyber espionage groups, including a suspected UNC5221 cluster; the PRC-nexus cyber espionage cluster UNC5807, which overlaps with the publicly reported "Salt Typhoon"; and a suspected APT44 threat cluster, that compromised third-party service providers to facilitate data theft from customers of these service providers.

Mandiant also identified evidence of selective data theft. For example, in multiple incidents attributed to disparate PRC-nexus cyber espionage groups, including UNC5221, Mandiant identified evidence that the threat clusters targeted particular users or subjects of interest. While UNC5221 has been used synonymously with the actor publicly reported as Silk Typhoon, GTIG does not currently consider the two clusters to be the same.

![UNC5221 Targeting Third-Party SaaS Providers Diagram]

*For more information about UNC6395, please see: [Widespread Data Theft Targets Salesforce Instances via Salesloft Drift]*

---

### Insider Threat

In 2025, Mandiant responded to a number of incidents involving North Korean IT workers using false or stolen identities to carry out employment fraud and ultimately provide revenue for the North Korean regime. The IT workers Mandiant identified targeted organizations in a variety of industries, including the business and professional services, financial, government, technology, healthcare, and hospitality sectors. Many of the IT workers remained undetected in target environments for long periods of time, in several cases more than one year. The median dwell time for the IT worker incidents Mandiant responded to was 122 days, or about four months.

Mandiant also identified financially motivated threat clusters bribing contractors to provide corporate credentials or other access into targeted organizations, leading to data theft and attempted extortion.

*For more information about North Korean IT Workers, please see:*
- *[The Ultimate Insider Threat: North Korean IT Workers]*
- *[DPRK IT Workers Expanding in Scope and Scale]*
- *[Staying a Step Ahead: Mitigating the DPRK IT Worker Threat]*

---

### Malware

GTIG began tracking 714 new malware families in 2025, a significant increase from 632 in 2024, which brought the total number of tracked malware families to more than 6,000. A total of 224 malware families were observed in the investigations Mandiant performed in 2025, which includes 126 newly tracked families and an additional 98 malware families that were first discovered in prior years. For comparison, GTIG observed 205 malware families and 83 malware families were both newly tracked and observed in 2024 investigations.

As with prior years, the majority of newly tracked malware (72%) and malware families observed (63%) in 2025 investigations were effective on Windows. These percentages are consistent with 2024 findings. Malware families that are effective exclusively on Linux accounted for 12% of newly tracked families and 11% of observed malware families. The percentage of newly tracked malware families effective only on Linux remained stable compared to 2024, but the percent of observed malware families effective only on Linux declined slightly from 17% in 2024. In addition to Windows and Linux, GTIG tracked malware families effective on MacOS, BSD, and Unix.

#### Tracked and Observed Malware Families in 2025
- **Total tracked as of 2025**: >6,000
- **Newly Tracked**: 714
  - **Windows**: 581 (72% effective exclusively on Windows)
  - **Linux**: 146 (11.6% effective exclusively on Linux)
  - **MacOS**: 55 (2.8% effective exclusively on MacOS)
- **Observed**: 224
  - **Windows**: 182 (63.8% effective exclusively on Windows)
  - **Linux**: 65 (10.7% effective exclusively on Linux)
  - **MacOS**: 26 (4.5% effective exclusively on MacOS)

#### Malware Families by Category

**Newly Tracked Malware**
Of these families, 33% were backdoors, 14% were droppers, 14% were downloaders, 6% were ransomware, 6% were launchers, 5% were credential stealers, and 5% were data miners. The "Other" category includes keyloggers, tunnelers, utilities, rootkits, ATM malware, disruptive malware, and point-of-sale malware, each of which make up less than 5% of the malware families observed in 2025. Compared to 2024, there were fewer downloaders (19% in 2024), but other proportions remained consistent with findings from prior years.

**Observed Malware**
The most frequently observed roles of malware families observed in Mandiant's 2025 investigations included backdoors at 36%, followed by downloaders at 11%, ransomware at 10%, droppers at 10%, credential stealers at 9%, with 24% of observed malware families falling into other roles. Despite an increase in newly tracked ransomware families and variants, ransomware declined in its share of observed malware from 14% in 2024, while downloaders increased from 7%, and credential stealers increased from 5%.

#### Malware Definitions
- **Backdoor**: A program whose primary purpose is to allow a threat cluster to interactively issue commands to the system on which it is installed.
- **Credential Stealer**: A utility whose primary purpose is to access, copy, or steal authentication credentials.
- **Data Miner**: A utility whose primary purpose is to gather ("mine") data, typically for theft by threat clusters. Excludes utilities that gather, such as credentials used for the purpose of escalating privileges or information used for system or network reconnaissance.
- **Downloader**: A program whose sole purpose is to download (and perhaps launch) a file from a specified address, and that does not provide any additional functionality or support any other interactive commands.
- **Dropper**: A program whose primary purpose is to extract, install, and potentially launch or execute one or more files.
- **Launcher**: A program whose primary purpose is to execute an external payload or shell command. A launcher does not contain or configure a payload it executes. Examples include a program that starts an executable file located on disk and a program that reads a payload from disk and executes it in memory.
- **Ransomware**: A program whose primary purpose is to perform some malicious action (such as encrypting data) with the goal of extracting payment from the target in order to avoid or undo the malicious action.
- **Tunneler**: A program that proxies or tunnels network traffic.
- **Utility**: A program that has a specialized purpose that does not fit into any other defined category (such as keylogger or sniffer).
- **Other**: Includes all other malware categories, such as rootkits, keyloggers, and point-of-sale.

#### Most Frequently Seen Malware Families, 2025
1. **GOLDVEIN.JAVA**: 3.2%
2. **REDBIKE**: 2.9%
3. **JSPKIT**: 2.4%
4. **BEACON**: 1.9%
5. **BRICKSTORM**: 1.2%
6. **SPAWNSNARE**: 1.2%
7. **KRABDRIP**: 1.2%
8. **SAGEGIFT**: 1.2%

The proportion of BEACON malware observed in Mandiant investigations has declined each year since 2021, from 28% to just 2% in 2025.

#### Malware Descriptions
- **GOLDVEIN.JAVA**: GOLDVEIN.JAVA is a downloader written in Java for compromised Oracle WebLogic servers that connects to a hard-coded command-and-control (C2 or C&C) server over TCP to download an encrypted Java class payload. The downloaded payload is decrypted using a rolling XOR scheme with a hard-coded key and then directly invoked in memory through reflective loading. GOLDVEIN.JAVA is functionally similar to the original PowerShell version of GOLDVEIN; however, it uses the marker "TLSv3.1" in the C2 packet instead of the original "TLS v3".
- **REDBIKE**: REDBIKE is a ransomware written in C++. This malware, also known as AKIRA, is designed to encrypt files on local drives and network shares. It operates as a stand-alone tool via command-line arguments that allow an operator to specify target paths, including files containing lists of network shares. REDBIKE employs a hybrid encryption scheme, using symmetric ciphers like ChaCha or KCipher-2 to encrypt file contents and an embedded RSA public key to protect the symmetric keys. More recent variants use a combination of ChaCha8 and KCipher-2 for file encryption. After encryption, it renames files by appending the ".akira" extension and creates a ransom note named "akira_readme.txt" in affected directories. To hinder recovery, the ransomware terminates a list of predefined processes and executes a PowerShell command to delete volume shadow copies. The malware avoids encrypting critical system files and directories by using an exclusion list for specific paths and extensions, such as ".exe," ".dll," and ".sys". REDBIKE does not contain a persistence mechanism and relies on an external tool or operator for execution. Some variants are verbose and will log their activity to a file in the user’s temporary directory. REDBIKE exhibits some code overlap with CONTI ransomware.
- **JSPKIT**: Publicly available JSP web shell known as JSP KIT or JSP SHELL or "cmd.jsp."
- **BEACON**: BEACON is a backdoor written in C/C++ that is part of the Cobalt Strike framework. Supported backdoor commands include shell command execution, file transfer, file execution, and file management. BEACON can also capture keystrokes and screenshots as well as act as a proxy server. BEACON may also be tasked with harvesting system credentials, port scanning, and enumerating systems on a network. BEACON communicates with a command-and-control (C2 or C&C) server via HTTP or DNS.
- **BRICKSTORM**: BRICKSTORM is a backdoor written in Go that communicates over WebSockets Secure (WSS). BRICKSTORM supports the ability to set itself up as a web server, perform file and directory manipulation, perform file operations such as upload/download, run shell commands, and perform SOCKS relaying.
- **SPAWNSNARE**: SPAWNSNARE is a utility written in C that allows for extraction of the uncompressed Linux kernel image into a file and encrypts it using AES without the need for any other command-line utilities. Supported commands include writing a Bash script to disk, encrypting a file using AES-128 in CBC mode, decrypting a file using AES-128 in CBC mode, and acting as a BusyBox to run a set of statically linked applets. The dropped Bash script includes all of the necessary logic and commands for extraction of the kernel.
- **KRABDRIP**: KRABDRIP is a downloader written in Rust. It uses an embedded configuration containing an AES key, IV, and an encrypted C2 URL to retrieve a payload. The malware communicates with its C2 server via HTTP to download an encrypted payload, which it decrypts using the embedded AES key and IV. The decrypted payload is treated as position-independent code and is injected into an instance of explorer.exe for execution. KRABDRIP performs anti-analysis checks, such as looking for a debugger and verifying the existence of a specific file in the temp directory. For evasion, it copies itself to the `%TEMP%` directory, relaunches from the new location, and then deletes both the original and copied files. The malware does not contain its own persistence mechanism.
- **SAGEGIFT**: SAGEGIFT is an in-memory dropper written in Java for compromised Oracle WebLogic servers that reflectively loads an embedded Java class to execute in memory. SAGEGIFT returns its status through an encoded HTML comment in its response. SAGEGIFT has been observed loading SAGELEAF.

---

### Threat Groups

GTIG began tracking 661 net new threat clusters in 2025, bringing the total number of tracked threat clusters to more than 5,000. In 2025 investigations, Mandiant encountered 288 threat groups, 205 of which were newly tracked. The counts for these figures are slightly lower than the count of groups newly tracked and observed in 2024. While these figures align with a slight downward trend during the last five years, the consistent discovery of newly tracked groups underscores a decade-long trend of expanding threat activity. While "known" threats persist, the use of threat intelligence to continually identify and analyze new activity drives new detections and research, increasing defenders’ ability to implement protections against both established and emerging adversaries.

#### Observed Groups by Goal
- **Financial Gain**: 41% (This category includes six different North Korean threat groups seeking financial gain on behalf of the North Korean Government.)
- **Unknown**: 37%
- **Espionage**: 16% (The proportion of cyber espionage groups observed in Mandiant investigations increased from 8% in 2024, while financially motivated groups declined from 55%.)
- **Notoriety**: 4%
- **Other**: 2%

---

## Ransomware

Extortion operations, including ransomware, data theft extortion, and multifaceted extortion, continue to represent the most impactful form of cyber crime. Ransomware-related intrusions accounted for 13% of Mandiant investigations in 2025. This is a result of the combined frequency of extortion incidents, and the disruption that extends beyond the targeted organization to affect clients, suppliers, and communities. Ransomware-related incidents Mandiant investigated in 2025 affected a wide range of organizations in the Americas; Europe, the Middle East, and Africa (EMEA); and Japan-Asia Pacific (JAPAC) including healthcare, technology, government, pharmaceutical, financial, education, aerospace and defense, business and professional services, and construction and engineering.

### Initial Infection Vector
Across Mandiant-led ransomware investigations during 2025, we observed multiple ransomware operations relying on initial access partnerships, most commonly for malware distribution services, which we tra

---

ck as prior compromises. In 2025, prior compromise was the most
frequently confirmed initial infection vector for ransomware-related incidents that Mandiant
investigated. This is a marked increase from 15% observed in 2024, to 30% in 2025. In these
incidents, the initial access threat cluster most commonly gained access via web compromises.
GTIG tracks dozens of threat clusters that specialize in widespread initial access operations.
These threat clusters focus on gaining an initial foothold at many organizations via high volume,
opportunistic infection vectors, then selling or handing off this access to other threat clusters
for post-compromise exploitation. This “hand-off” pattern is commonly observed in incidents
that result in ransomware deployment.
The second-most common initial infection vector was exploits, at 27%. Brute-force attacks
were the vector for 20% of ransomware-related intrusions, followed by stolen credentials and
web compromise at 10% each.
Initial Infection Vector, 2025
Initial Infection Vector, 2025
Ransomware-Related
Ransomware-Related
Prior Exploit Brute Force
Compromise %
20
Stolen Web
Credentials Compromise
%
% %
%
10
%
Other
30 27 10 3

Special Report: Mandiant M-Trends 2026 30
Detection by Source
Consistent with the extortion business model, in 2025, organizations most frequently learned of
a ransomware incident from the attacker. In 44% of Mandiant’s 2025 investigations, the intrusion
was self-disclosed by the attacker either through direct extortion demands or the deployment
of ransomware. Organizations discovered evidence of malicious activity internally in 41% of
cases, and from an external entity such as law enforcement or a cybersecurity company in 15%
of ransomware incidents. In 2024, adversary notifications comprised 49% of ransomware cases,
and external entity notifications made up 21% of notification sources, figures roughly in line with
2025. However, internal discovery in 2024 represented 30%, compared to 41% in 2025.
DDeetetcetiocnt biyo Snou brcye,  2S0o25urce, 2025
%
10
100%
Adversary
| %   | %   |     |                 |
| --- | --- | --- | --------------- |
| 14  | 44  |     | External Entity |
%
| %   |     | 37  | Internal |
| --- | --- | --- | -------- |
75% 34
| 50% | %   |     |     |
| --- | --- | --- | --- |
| %   |     | %   |     |
15
| 52  |     | 53  |     |
| --- | --- | --- | --- |
%
41
25%
0%
| All | Ransomware | Non-Ransomware |     |
| --- | ---------- | -------------- | --- |

Special Report: Mandiant M-Trends 2026 31
Ransomware vs. Global Dwell Time
Median dwell time for ransomware-related events in 2025 was nine days overall, five days
for attacker-notified events, 12 days for internally discovered events, and eight days for
compromises that organizations discovered due to notifications from external entities, such
as law enforcement.
Dwell Time Distribution,
Ransomware vs. Global
Comparing the distribution of dwell times for 2025 ransomware-related events to the overall
dataset and non-ransomware-related incidents shows that ransomware-related incidents
remain undiscovered for much shorter periods of time than other types of compromises.
Ransomware-related intrusions were identified within one week 48.1% of the time, as opposed
to 41.5% of the time for all incidents. In 2024, the concentration of ransomware-related dwell
times in the one week or less category was slightly more pronounced, at 56.5%.
snoitagitsevnI
5202
fo
%
Global Dwell Time Distribution, 2025
Global Dwell Time Distribution, 2025
All % 20.1% 26.7%
41.5
5.6% 5.8% 0.2%
Ransomware % 29.6% 18.5%
48.1
3.7% 0% 0%
Ransom
N
w
o
a
n
re
-
40.5
% 18.7% 27.9%
5.9% 6.7% 0.3%
≤ 1 week 8 to 30 days 31 days to > 6 months > 1 year 5 years
6 months to 1 year to 5 years or more

Special Report: Mandiant M-Trends 2026 32
Malware
The top malware category for ransomware-related intrusions was, appropriately, ransomware
(49%), followed by backdoors (19%), downloaders (10%), and tunnelers (7%). Compared to the
global metrics for 2025, ransomware-related intrusions had less variety of malware categories.
Two trends may contribute to this. First, ransomware operators often use legitimate utilities
and remote monitoring and management (RMM) tools, which would not appear on this list.
Second, the ransomware-related dataset does not include initial access operations prior
to the hand-off, which would be characterized by more frequent use of droppers, launchers,
and credential stealers.
The most frequently observed
Observed Malware Families by Category, 2025
ROabnsseormvweadr Me-aRlewlaatreed Families by Category, 2025
malware family in 2025 Mandiant
Ransomware-Related
ransomware-related incident
Downloader
|     |     | Backdoor |     | response investigations was  |     |
| --- | --- | -------- | --- | ---------------------------- | --- |
Ransomware
REDBIKE (aka Akira) at 15%,
|     |     | %   |     | followed by AGENDA (aka Qilin)  |     |
| --- | --- | --- | --- | ------------------------------- | --- |
and ADAPTAGENT, the back-
%
door component of the publicly
|     |     | 19               | 10      | available AdaptixC2 pentesting  |     |
| --- | --- | ---------------- | ------- | ------------------------------- | --- |
|     | %   | Tunneler Dropper | Utility | framework, both at 5%. The INC  |     |
%
ransomware variant was also
|     |     | %   | %   |     |     |
| --- | --- | --- | --- | --- | --- |
5
in the top-observed malware
Other %
category, observed in 4%
| 49  |     | 7 6 | 3   |     |     |
| --- | --- | --- | --- | --- | --- |
of ransomware-related
investigations.
The SYSTEMBC tunneler was the fifth-most  Most Frequently Seen Malware, 2025  Most Frequently Seen Malware, 2025
| frequently seen malware family in 2025   |     |     | Ransomware-Related |     |     |
| ---------------------------------------- | --- | --- | ------------------ | --- | --- |
Ransomware-Related
ransomware-related intrusions, reflecting
15
| its popularity among multiple groups  |     |     | %   |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- |
15
that conduct ransomware operations.
SYSTEMBC was among the most frequently
| observed malware families in 2024  |     |     | snoisurtnI fo % 10 |     |     |
| ---------------------------------- | --- | --- | ------------------ | --- | --- |
ransomware-related instructions as well.
CHERRYQUIRK has been observed
downloading and executing ADAPTAGENT.
5
% %
|     |     |     |     | 5 5 | % % |
| --- | --- | --- | --- | --- | --- |
4 4 %
2
0
|     |     |     | REDBIKE | ADAPTAGENT | SYSTEMBC    |
| --- | --- | --- | ------- | ---------- | ----------- |
|     |     |     | (Akira) | AGENDA INC | CHERRYQUIRK |
(Qilin)
Malware Family

Special Report: Mandiant M-Trends 2026 33
Mandiant observed commercially available and legitimate tools used much more frequently than
malware in ransomware-related intrusions in 2025. The most common category of tools was
utilities, which make up 35% of the dataset. The second-most frequently seen type of tools were
reconnaissance tools, followed by archivers, such as WinRAR, remote control and administration
tools, lateral movement tools, and credential stealers such as Mimikatz.
Observed Tools, 2025
Observed Tools, 2025
Ransomware-Related
Ransomware-Related
Reconnaissance Archiver Remote Control
& Administration
Utility
% %
%
8 8
16 Tunneler Lateral Movement
Other %
%
6
%
% Credential Stealer
%
35 13 7 5
Tool Roles
Utility A utility is a program that has a specialized purpose that does not fit into any other
defined category (such as keylogger, sniffer, or credential theft). Examples may
include tools designed to overwrite or clear log files, encode or decode files, etc.
Reconnaissance A reconnaissance tool is a program whose primary purpose is to conduct some type of
Tool system or network reconnaissance (for example, enumerating accounts or systems, or
conducting port scanning).
Archiver An archiver is a program whose primary purpose is to package one or more files into
an archive and may also extract files from an existing archive. The program may have
additional options to compress or encrypt the archived files. Common examples
include RAR, ZIP, and TAR.
Remote A remote control and administration tool is a legitimate program whose primary
Control and purpose is to remotely access and control or administer a system.
Administration
Tool
Tunneler A tunneler is a program that proxies or tunnels network traffic.
Lateral A lateral movement tool is a program whose primary purpose is to facilitate lateral
Movement movement within a network.
Credential A credential stealer is a utility whose primary purpose is to access, copy, or steal
Stealer authentication credentials.

Special Report: Mandiant M-Trends 2026 34
The tools Mandiant encountered most often in 2025 ransomware-related events were the RAR
archiver, which is commonly used to prepare data for theft, and nltest, which is a utility for
interacting with domain controllers and domain services. Ransomware operators frequently
use nltest to conduct reconnaissance or within ransomware deployment scripts. Threat clusters
take advantage of the useful functionalities of all of these tools to accomplish their malicious
activities as well as reduce the likelihood that their activity will be detected as malicious.
Most Frequently Seen Tools, 2025
Most Frequently Seen Tools, 2025
Ransomware-Related
Ransomware-Related
10
snoisurtnI fo %
| %   | %   |     |     |
| --- | --- | --- | --- |
| 7   | 7   | % % |     |
6.5 6.5
| 5   |     |     | %   |
| --- | --- | --- | --- |
5.5 % %
5 5
0
| NLTEST | PSEXEC | RCLONE  | POWERSHELL |
| ------ | ------ | ------- | ---------- |
|        | RAR    | NETSCAN | ADVIPSCAN  |
Tool Family

Special Report: Mandiant M-Trends 2026 35
Tools
Nltest Nltest is a Windows command-line utility used to list domain controllers and information
about domain trust relationships.
RAR RAR is the RAR command-line archive utility; it may be distributed as part of the WinRAR
package.
PsExec PsExec, a utility within the Microsoft Sysinternals suite created by Mark Russinovich, is a
command-line tool that executes processes on remote Windows systems. While designed
for legitimate remote administration, it is frequently used by threat clusters for lateral
movement within compromised networks because it does not require pre-installing
software on the target machine.
SoftPerfect NetScan is a SoftPerfect network scanner, a free multi-threaded IPv4/IPv6 scanner
Network that pings computers, scans for listening TCP/UDP ports, discovers shared folders, and
Scanner retrieves information about network computers via Windows Management Instrumentation
(WMI), Simple Network Management Protocol (SNMP), HTTP, and NetBIOS.
rclone rclone is a publicly available command-line utility to sync files and directories to and from
numerous cloud-based resources, such as Amazon Drive, Dropbox, File Transfer Protocol
(FTP), Google Drive, HTTP, Mega, Microsoft OneDrive, rsync.net, Secure File Transfer
Protocol (SFTP), and the local file system.
Advanced Advanced IP Scanner (ADVIPSCAN) is a publicly available network scanner developed
IP Scanner by Famatech that has remote control capabilities.
PowerShell PowerShell is a publicly available cross-platform task automation and configuration
management utility framework, consisting of a command-line shell and scripting language.
Unlike most shells, which accept and return text, PowerShell is built on top of the .NET
Common Language Runtime (CLR) and accepts and returns .NET objects.
Mimikatz Mimikatz is a credential stealer written in C that targets Windows authentication
credentials. Techniques employed include stealing password hashes, keys, and
Kerberos tickets. Credentials can be printed to the console or saved to disk. Mimikatz
also supports privilege escalation, extracting credentials from the Windows Local
Security Authority Subsystem Service (LSASS) and Security Account Managers (SAM)
database, and service manipulation.
FileZilla FileZilla is a cross-platform, publicly available FTP utility.
Impacket Impacket is a Python library that allows users to work with various network protocols.
AnyDesk AnyDesk is a commercially available remote monitoring and management (RMM) application
that is supported on Windows, macOS, Linux, Android, and ChromeOS devices.

Special Report: Mandiant M-Trends 2026 36
Ransomware Operations
Data leak sites The ransomware-as-a-service (RaaS) business model is characterized by threat clusters
(DLS) are websites
specializing in components of the threat lifecycle, such as initial access operations, and
that publish stolen
data of companies interoperability between threat groups and ransomware brands. A centralized group may
that refuse to pay maintain the ransomware itself as well as the data leak site (DLS) infrastructure, while numerous
a ransom. While
affiliates deploy the ransomware. While the total volume of DLS posts has increased in 2025,
this data is skewed
toward targets disruptions, such as law enforcement operations or internal conflict between clusters, have
who refused to
led to the disappearance or decline of previously prolific RaaS groups like LockBit and ALPHV
pay attackers’
ransom demands, (BlackCat). However, the well-established AGENDA (Qilin) and REDBIKE (Akira) RaaS brands
it is still useful for emerged as the most prolific DLS in 2025.
understanding
broad trends
in extortion
operations.
Jan Feb March April May June July Aug Sept Oct Nov Dec
sgnitsiL
SLD
fo
tnuoC
2025 DLS Listings for Qilin and Akira
250
Qilin
Akira
200
150
100
50
00
AGENDA (aka Qilin)
The Qilin RaaS and associated DLS first emerged in 2022. In 2025, it became the single-most
prolific RaaS based on count of DLS listings, though AGENDA was the second-most commonly
observed ransomware in Mandiant incident response in 2025. GTIG tracks multiple threat
clusters that have deployed AGENDA, which is the name GTIG uses to track the ransomware
commonly referred to as Qilin, including UNC2465 and UNC6276.
UNC2465 is a financially motivated threat cluster that has been active since at least April
2019. They frequently obtain access to environments via malicious installers, masquerading as
legitimate software—usually IT administration tools—that lead to the SMOKEDHAM backdoor.
SMOKEDHAM may be exclusive to UNC2465. The threat cluster has used malicious advertising
(malvertising) for malware distribution, but has often sought traffic providers as well.
UNC2465 has remained interested in monetizing accesses via ransomware operations and is
likely leveraging AGENDA ransomware in their current operations; they have previously used
HIVELOCKERS.HUNTERS (aka Hunters International), LOCKBIT, and DARKSIDE ransomware.
UNC2465 SMOKEDHAM LOCKBIT CAMP.25.017

Special Report: Mandiant M-Trends 2026 37
UNC6276 is a financially motivated threat cluster that has been active since at least May 2025
and has targeted organizations in North America, including legal and professional services
and manufacturing, to deploy ransomware. GTIG observed UNC6276 gain initial network access
through the use of either stolen or brute-forced virtual private network (VPN) credentials.
UNC6276 has leveraged publicly available tools such as PINGCASTLE, NETSCAN, and MIMIKATZ
for reconnaissance and credential theft and deployed SYSTEMBC.LINUX for command
and control. These intrusions have led to the deployment of AGENDA ransomware and data
theft extortion.
UNC6276 SYSTEMBC.LINUX CAMP.25.058
REDBIKE (aka Akira)
The Akira RaaS and DLS were established in 2023, and the RaaS has increased its market
share, as measured by count of DLS listings, steadily since then to become the second-most
prolific DLS in 2025. REDBIKE, which is the name GTIG uses to track the ransomware, was
the second-most frequently seen malware family across all Mandiant investigations in 2025,
and the most commonly observed ransomware variant. GTIG tracks multiple threat clusters
using REDBIKE, including UNC6361 and a suspected FIN6 cluster.
UNC6361 compromises target environments through the exploitation of known vulnerabilities
in network edge devices. These compromises lead to lateral movement further into the target
environment, followed by the eventual deployment of REDBIKE ransomware in support of this
cluster’s extortion operations.
UNC6361 REDBIKE CAMP.25.051
FIN6 is a financially motivated threat cluster active since mid-2014. Since mid-2019, FIN6
has used job-themed lures and fake personal websites to deliver BULLZLINK, followed by
SQUIDSLEEP and SQUIDGATE. Notably, in 2025 FIN6 used a financial-themed lure to deliver
an updated version of SQUIDGATE. While GTIG has not directly observed FIN6 monetize access
recently, overlaps identified with suspected affiliates suggest the group likely supports or
conducts REDBIKE ransomware operations. Historically, the group compromised point-of-sale
(POS) environments using TRINITY (aka FrameworkPOS), used SCRAPMINT malware to steal
payment card data, and targeted card-not-present (CNP) data in e-commerce environments.
As of mid-2018, at least one FIN6-affiliated cluster began deploying ransomware, including
LOCKERGOGA, RYUK, MEGACORTEX, and MAZE.

Special Report: Mandiant M-Trends 2026 38
Cloud
Compromises
Cloud In 2025, the most common initial infection vector found during Mandiant investigations of
compromises
cloud-related compromises was voice phishing, at 23%, followed by third-party compromise
consist of
intrusions where (17%), stolen credentials (16%), email phishing (15%), insider threat (14%), and exploits (6%).
threat clusters Mandiant identified evidence of data theft in 59% of cloud compromises. Just over a third of
access a target
cases, 34%, supported financially motivated objectives, including employment fraud, data theft
organization’s
cloud environment, extortion, ransomware, payment redirection fraud, and theft.
excluding the
misuse of cloud Voice phishing facilitated significant data theft extortion campaigns attributed to UNC3944 and
services for attacker
UNC6240 in 2025. In terms of post-compromise operations in cloud environments, UNC3944
operations or
infrastructure such conducted extensive reconnaissance of targeted organizations’ cloud resources, including
as staging payloads
SharePoint, Azure Portal, M365 email, and privileged access management (PAM) solutions, and
or data theft.
extracted sensitive data for attempted extortion. UNC6040 used native utilities to automate
large-scale data collection and theft. In several cases, UNC6040 used bulk application program-
For more ming interface (API) operations to extract broad datasets to use for extortion.
information
about UNC6240, Cloud Initial Infection Vectors, 2025 In another significant set of
please see:
activity targeting cloud
Vishing for Access:
Tracking the Voice Third-Party Email Insider environments, GTIG tracked
Expansion Compromise Phishing Threat the PRC-nexus cyber
Phishing
of ShinyHunters-
Branded SaaS % espionage cluster UNC6201’s
Data Theft use of stealthy tactics and
% % lightweight malware to
For more 17
maintain long-term access
information about
Stolen
BRICKSTORM 15 14 to targeted environments.
Credentials
activity, please see:
Other Exploit Mandiant investigated a
% %
Another % % number of incidents in 2025
BRICKSTORM:
Stealthy Backdoor in which the threat cluster
Enabling Espionage 23 16 9 6 deployed the BRICKSTORM
into Tech and Legal
backdoor on appliances
Sectors
that do not support endpoint detection and response (EDR), including Linux- and BSD-based
For the VMware appliances from multiple manufacturers. Using valid credentials likely captured on the network
vSphere hardening
guide, please see: device, UNC6201 then accessed VMware vCenter servers and ESXi hosts. With access to
From Help Desk vCenter, the threat cluster cloned virtual machines (VMs), which included single sign-on (SSO)
to Hypervisor: identity providers, secret vaults, and domain controllers. By accessing targeted data and
Defending Your
credentials in the cloned but powered off VMs, the threat cluster circumvented security alerting
VMware vSphere
Estate from on those systems. Mandiant also identified evidence of UNC6201 leveraging this access to target
UNC3944
and datamine sensitive cloud-based resources, such as mailboxes belonging to developers and
system administrators as well as individuals involved in matters that align with the economic
and espionage interests of the People’s Republic of China.

Special Report: Mandiant M-Trends 2026 39
Artificial
Intelligence
GTIG has closely tracked threat cluster interest in, as well as use and misuse of, artificial
intelligence (AI) in malicious operations. In 2025, threat clusters have increasingly adopted
AI tools to achieve productivity gains in different stages of the attack lifecycle, particularly in
tasks such as reconnaissance, social engineering, and malware development. In 2025,
Mandiant investigations identified threat clusters using AI-themed lures, stealing credentials
for AI applications, and targeting companies developing AI technologies.
Notably, threat clusters have also relied on AI tools within the compromised environment to
help carry out their operations. For example, Mandiant investigated an NPM package manager
software supply chain compromise that led to the installation of the QUIETVAULT credential
stealer. Upon activation, QUIETVAULT checks to see if AI command-line interface (CLI) tools
are installed on the targeted machine, and if so, executes a predefined prompt to search for
configuration files. The tool then attempts to collect GitHub and NPM tokens and, if found,
copy them to a publicly accessible GitHub repository.
Threat Actor Use and Abuse of AI
For more information about threat actor use and abuse of AI, please see:
GTIG AI Threat Tracker: Distillation, Experimentation, and (Continued) Integration
of AI for Adversarial Use
Adversarial Misuse of Generative AI
GTIG AI Threat Tracker: Advances in Threat Actor Usage of AI Tools
UNC1069 Targets Cryptocurrency Sector with New Tooling and AI-Enabled
Social Engineering
Text-to-Malware: How Cybercriminals Weaponize Fake AI-Themed Websites
AI Risk and Resilience: A Mandiant Special Report

Special Report: Mandiant M-Trends 2026 40
Threat
  Techniques
MITRE ATT&CK® is a  Since the M-Trends 2020 report, Mandiant has supported the security industry by aligning
globally accessible
its findings with the MITRE ATT&CK framework. To help organizations bolster their
knowledge base of
security, Mandiant provides metrics around the most commonly observed adversary tactics
adversary tactics
and techniques  and sub-techniques. This information can enable organizations to prioritize the development
based on real-world
of detection capabilities that address these prevalent threats, then inform strategic decisions
observations. The
ATT&CK knowledge  on further security planning to improve security capabilities.
base is used as
a foundation for  In October 2025, MITRE released ATT&CK version 18, a release that updates Techniques,
the development
Groups, Campaigns and Software for Enterprise, Mobile, and ICS. Similar to version 16, this
of specific threat
models and  change did not introduce a significant number of new techniques and sub-techniques to
methodologies in  the already established framework. The observed MITRE ATT&CK techniques mapped to the
the private sector,
government, and  Mandiant Targeted Attack Lifecycle can be found in the appendix of this report.
the cybersecurity
product and service
community.
MITRE ATT&CK Techniques
Used Most Frequently
Top 10 Most Frequently Seen MITRE ATT&CK Techniques
| Rank | Technique                                | Percent |
| ---- | ---------------------------------------- | ------- |
| 1    | T1059: Command and Scripting Interpreter | 45.9%   |
| 2    | T1074: Data Staged                       | 39.6%   |
| 3    | T1083: File and Directory Discovery      | 33.5%   |
| 4    | T1021: Remote Services                   | 30.6%   |
| 5    | T1190: Exploit Public-Facing Application | 27.7%   |
| 6    | T1027: Obfuscated Files or Information   | 27.2%   |
| 7    | T1070: Indicator Removal                 | 24.8%   |
| 8    | T1105: Ingress Tool Transfer             | 24.5%   |
| 9    | T1033: System Owner/User Discovery       | 24.0%   |
| 10   | T1133: External Remote Services          | 23.8%   |

Special Report: Mandiant M-Trends 2026 41
MITRE ATT&CK Sub-Techniques
Used Most Frequently
Top 10 Most Frequently Seen MITRE ATT&CK Sub-Techniques
| Rank | Technique                                | Percent |
| ---- | ---------------------------------------- | ------- |
| 1    | T1059.003: Windows Command Shell         | 26.2%   |
| 2    | T1059.001: PowerShell                    | 24.0%   |
| 3    | T1021.001: Remote Desktop Protocol       | 22.1%   |
| 4    | T1021.002: SMB/Windows Admin Shares      | 19.4%   |
| 5    | T1204.002: Malicious File                | 16.5%   |
| 6    | T1070.004: File Deletion                 | 15.5%   |
| 7    | T1505.003: Web Shell                     | 14.8%   |
| 8    | T1569.002: Service Execution             | 14.3%   |
| 9    | T1016.001: Internet Connection Discovery | 14.1%   |
| 10   | T1021.004: SSH                           | 12.9%   |
Command and Scripting Interpreter (T1059) remains a top MITRE ATT&CK tactic, technique,
and procedure (TTP) for the fifth consecutive year, followed by Data Staged (T1074), File and
Directory Discovery (T1083), and Remote Services (T1021). The consistency in Command
and Scripting Interpreter (T1059) is expected given, by MITRE’s own definition, most systems
come with some built-in command-line interface and scripting capabilities. These built-in
command-line capabilities allow threat clusters to leverage living off the land (LotL) to perform
actions across multiple stages of the attacker lifecycle, with the added benefits of convenience
and lowered chances of getting detected. The latter is also why Indicator Removal (T1070)
remains a consistent top observed TTP year over year. Remote Services (T1021), System Owner/
User Discovery (T1033), and File and Directory Discovery (T1083) are foundational to
post-exploitation internal reconnaissance and privilege escalation. As denoted in the Mandiant
Attack Lifecycle, threat clusters will often perform internal reconnaissance and move laterally
after gaining access to environments, whether to escalate privileges, maintain access, or quickly
gather information and steal data, potentially to be used later in extortion.
Several techniques returned to the Top 10 after a multi-year hiatus, including Data Staged
(T1074), File and Directory Discovery (T1083), and Ingress Tool Transfer (T1105). This resurgence,
paired with a similarly observed increase in System Owner/User Discovery (T1033), shows heavy
emphasis on internal reconnaissance and lateral movement. Notably, Data Encrypted for Impact
(T1486) was not in the top 10, where it appeared for the first time in 2024. While this indicates
a decline in encryption-based ransomware operations, the rise of Data Staging (T1074) suggests
a tactical shift toward data theft and pure extortion-based models.

Special Report: Mandiant M-Trends 2026 42
Regional
Breakouts
Americas
Americas
Initial Infection Vector
In 2025, exploits (28%) remained as the leading entry for compromises in the Americas
where Mandiant was able to determine an initial infection vector. While email phishing saw
a significant decline—down to 5% from 16% in 2024—web compromises claimed a spot in
the top three. This follows similar trends observed globally, where similar declines in email
phishing and increases in web compromises were noted.
AMERICAS
Exploit
28%
AMERICAS
Stolen Credentials Detection by Source
Exploit
18%
28% In 2025, GTIG observed an increase in external notifications for activity Mandiant investigated
Email Phishing
16% Voice Phishing in the Americas. This increase brings external notification in line with internal notifications in
14% an even distribution. Of these external notifications, one-third (33%) originated from external
Web Compromise partners such as law enforcement and cybersecurity companies, while the remaining 17% came
10% directly from threat clusters via ransom notes or extortion attempts.
Internal
External
egatnecreP
The metrics reported in this section are based on Mandiant investigations
affecting organizations in North, Central, and South America.
Americas Detection by Source, 2017-2025
100
80
60
40
20
0
2017 2018 2019 2020 2021 2022 2023 2024 2025

Special Report: Mandiant M-Trends 2026 43
Median Dwell Time
This year, the median dwell time for intrusions Mandiant investigated in the Americas in 2025 was
12 days overall, an increase of two days. The median dwell time for internally notified events was
nine days, consistent with last year’s median dwell time. However, externally notified events saw
an increase to 17 days, which is a notable increase from last year’s 10-day median dwell time.
Americas Median Dwell Time, 2016-2025
150
All
External
125
Internal
)syaD( emiT llewD 100
75
50
25
17
12 9
0
|     | 2016 | 2017 | 2018 |     | 2019 | 2020 | 2021 2022 | 2023 | 2024 2025 |
| --- | ---- | ---- | ---- | --- | ---- | ---- | --------- | ---- | --------- |
The 2025 dwell time distribution for the Americas also shows increases in longer duration
incidents compared to 2024, specifically, incidents lasting between one and six months, and
one to five years. Similar to longer dwell times observed globally, this shift in the Americas likely
reflects a larger proportion of incidents in which threat actors prioritize maintaining long-term
access to targeted environments, including cyber espionage, North Korean IT workers, and
other types of compromises.
Americas Dwell Time Distribution, 2021-2025
| 2021 | %    |      | %   |      | %   | %    | %   |     | %   |
| ---- | ---- | ---- | --- | ---- | --- | ---- | --- | --- | --- |
|      | 38.8 | 18.0 |     | 28.2 |     | 11.1 | 3.6 | 0.4 |     |
| 2022 | %    |      | %   |      | %   | %    | %   |     | %   |
|      | 44.5 | 19.4 |     | 26.2 |     | 4.5  | 2.6 | 2.8 |     |
| 2023 | %    |      | %   |      | %   | %    | %   |     | %   |
45.0
|     |     | 23.5 |     | 22.3 |     | 4.8 | 4.2 | 0.3 |     |
| --- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- |
|     | %   |      | %   |      | %   | %   | %   |     | %   |
2024
|     | 46.6 | 18.4 |     | 23.8 |     | 6.6 | 5.0 | 0.0 |     |
| --- | ---- | ---- | --- | ---- | --- | --- | --- | --- | --- |
|     | %    |      | %   |      | %   | %   | %   |     | %   |
2025
|     | 41.8     | 20.2         |     | 27.7        |         | 4.8        | 5.5        | 0.0 |          |
| --- | -------- | ------------ | --- | ----------- | ------- | ---------- | ---------- | --- | -------- |
|     | ≤ 1 week | 8 to 30 days |     |             | 31 days | > 6 months | > 1 year   |     | 5 years  |
|     |          |              |     | to 6 months |         | to 1 year  | to 5 years |     | or more  |

Special Report: Mandiant M-Trends 2026 44
Threat Groups
One of the most frequently observed threat clusters in Mandiant engagements in the Americas
in 2025 was UNC5267, which is the designation GTIG uses to track most North Korean IT worker
activity. This set of activity likely contributed to the observation that greater proportions of
incidents in the Americas had longer dwell times in 2025, as North Korean IT workers seek to
remain undetected and collect paychecks as long as possible.
Another frequently observed threat cluster was UNC6395. This threat cluster compromised a
software-as-a-service (SaaS) provider and stole authentication tokens for many of the organi-
zation’s clients. Then UNC6395 used those tokens to access the client environments, download
code repositories, and identify additional credentials and keys contained within them.
Campaigns and Global Events
In 2025, the GTIG tracked multiple campaigns and global events that directly correlated
to Mandiant investigations in the Americas. The Campaigns and Global Events timeline
summarizes prominent threat activity observed in the region.
Please see the graphic on the following page for more detail.

|     |     |     |     |     |     |     |     |     |     |     |     | Special Report: Mandiant M-Trends 2026 |     |     | 45  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- |
2025 Americas Campaigns and Global Events Related to Mandiant Incident Investigations
| 2024 |     |     |     |     |     |     | 2025 |     |     |     |     |     |     | 2026 |     |
| ---- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | ---- | --- |
Nov Dec Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec Jan Feb
|     |  UNC1543   |  FAKEUPDATES |     |     |     |     |     |     |     |     |             |     |     | CAMP.25.039 |     |
| --- | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | ----------- | --- |
|     |  UNC6207   |  LAKESNAKE   |     |     |     |     |     |     |     |     | CAMP.25.034 |     |     |             |     |
   UNC6201   BRICKSTORM   CVE-2024-21887   CVE-2023-46805 CAMP.25.044
|     |  UNC2165  |  FAKEUPDATES |     |                |     |     |     |     |             |     | CAMP.24.024 |     |               |     | 100.52.LABOLG |
| --- | --------- | ------------ | --- | -------------- | --- | --- | --- | --- | ----------- | --- | ----------- | --- | ------------- | --- | ------------- |
|     |  MULTIPLE |              |     |                |     |     |     |     |             |     |             |     | GLOBAL.25.001 |     |               |
|     |  UNC5518  |  UNC5774     |     |  CORNFLAKE.V2  |     |     |     |     |             |     |             |     | CAMP.24.062   |     |               |
|     |  UNC3944  |              |     |                |     |     |     |     | CAMP.25.043 |     |             |     |               |     |               |
   FIN11   GOLDVEIN   CVE-2024-50623   CVE-2024-55956  CAMP.24.081
|     |     |     |  UNC5883  |  SNAKEBITE  |  CVE-2024-20953 |     |     | CAMP.25.005 |     |     |     |     |     |     |               |
| --- | --- | --- | --------- | ----------- | --------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | ------------- |
|     |     |     |           |             |                 |     |     |             |     |     |     |     |     |     | 600.42.LABOLG |
 MULTIPLE   SIGSEGA   LUNALIGHT   CVE-2024-0012   CVE-2024-9474 GLOBAL.24.006

|     |  UNC5923   |  SIGSEGA               |              |  CVE-2024-0012  |  CVE-2024-9474  |     | CAMP.24.080 |               |             |     |             |             |              |     |     |
| --- | ---------- | ---------------------- | ------------ | --------------- | --------------- | --- | ----------- | ------------- | ----------- | --- | ----------- | ----------- | ------------ | --- | --- |
|     |  UNC2465   |  SMOKEDHAM             |              |  LOCKBIT        |                 |     |             |               |             |     |             | CAMP.25.017 |              |     |     |
|     |  UNC5862   |                        |              |                 | CAMP.25.021     |     |             |               |             |     |             |             |              |     |     |
|     |  UNC6016   |  SLOWFALL              |              |                 |                 |     |             |               |             |     |             |             | CAMP.25.007  |     |     |
|     |  UNC6040   |  UNC6240               |              |                 |                 |     |             |               | CAMP.25.032 |     |             |             |              |     |     |
|     |  UNC5978   |                        | CAMP.25.004  |                 |                 |     |             |               |             |     |             |             |              |     |     |
|     |  UNC6448   |  SELFDRIVE, AUTOPILOT  |              |                 |                 |     |             |               |             |     |             |             | CAMP.25.062  |     |     |
|     |            |  UNC1069               |  BIGMACHO    |                 |                 |     |             |               |             |     | CAMP.25.042 |             |              |     |     |
|     |            |  UNC4696               |  HAVOCDEMON  |                 |                 |     | CAMP.25.019 |               |             |     |             |             |              |     |     |
|     |            |  UNC5221               |  BRUSHFIRE   |                 |  CVE-2025-22457 |     |             | GLOBAL.25.002 |             |     |             |             |              |     |     |

|     |     |     |  UNC6361  |  REDBIKE  |     |     |     |     |     |     | CAMP.25.051 |     |     |     |     |
| --- | --- | --- | --------- | --------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |

|     |     |     |     |    UNC6072   |  LUMMAC.V2       |             | CAMP.25.014      |             |             |                 |                 |                 |               |             |               |
| --- | --- | --- | --- | ------------ | ---------------- | ----------- | ---------------- | ----------- | ----------- | --------------- | --------------- | --------------- | ------------- | ----------- | ------------- |
|     |     |     |     |    UNC6395   |  GATO-X          |             |                  |             |             |                 | CAMP.25.053     |                 |               |             |               |
|     |     |     |     |    UNC6226   |                  |             | CAMP.25.029      |             |             |                 |                 |                 |               |             |               |
|     |     |     |     |    MULTIPLE  |  CVE-2025-31324  |             |                  |             |             |                 |                 |                 | GLOBAL.25.003 |             |               |
|     |     |     |     |              |    UNC6286       |  RHYSIDA    |                  |             |             |                 |                 |                 | CAMP.25.050   |             |               |
|     |     |     |     |              |                  |  UNC6181    |  SNOWLIGHT       |             | CAMP.25.035 |                 |                 |                 |               |             |               |
|     |     |     |     |              |                  |    UNC6276  |  SYSTEMBC.LINUX  |             |             |                 | CAMP.25.058     |                 |               |             |               |
|     |     |     |     |              |                  |             |                  |    UNC6493  |             |  GOLDVEIN.JAVA  |                 |  CVE-2025-61882 |               | CAMP.25.075 |               |
|     |     |     |     |              |                  |             |                  |             |  UNC6345    |                 | CAMP.25.049     |                 |               |             |               |
|     |     |     |     |              |                  |             |                  |             |             |                 |                 |                 |               |             | 400.52.LABOLG |
|     |     |     |     |              |                  |             |                  |  MULTIPLE   |             |                 |  CVE-2025-53770 | GLOBAL.25.004   |               |             |               |

   UNC6357   LOCKBIT.WARLOCK  CVE-2023-29357   CVE-2023-24955 CAMP.25.072
|     |     |     |     |     |     |     |     |              |  UNC6564        |  UNC6240 |     | CAMP.25.078   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------------- | -------- | --- | ------------- | --- | --- | --- |
|     |     |     |     |     |     |     |     |    MULTIPLE  |  CVE-2025-55182 |          |     | GLOBAL.25.008 |     |     |     |
800.52.LABOLG
|     |     |     |     |     |     |     |    UNC6362  |     |  CHILLCHIRP  |           |  CVE-2025-4632  |  CVE-2025-55182 |     | CAMP.26.007 |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | --------- | --------------- | --------------- | --- | ----------- | --- |
|     |     |     |     |     |     |     |             |     |  UNC6588     |  COMPOOD  |                 |  CVE-2025-55182 |     | CAMP.25.083 |     |
|     |     |     |     |     |     |     |             |     |    UNC6602   |           |  HOTTEA         |  CVE-2025-55182 |     | CAMP.26.001 |     |
Financially motivated
|     |     |     |     |     |     |     |    UNC6590  |     |  XMRIG  |  TRUFFLEHOG  |     |  CVE-2025-55182 |     | CAMP.26.002 |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | ------------ | --- | --------------- | --- | ----------- | --- |
Espionage
|     | Multiple/Unknown |     |     |     |     |     |     |     |     |  UNC6555  |  SIRENSONG |     | CAMP.26.004 |     |     |
| --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ----------- | --- | --- |
CAMP.25.079
| = Actor   |     | = Vulnerability |     |     |     |     |     |     |    UNC6566  |     |  “Shai-Hulud” |     |     |     |     |
| --------- | --- | --------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------- | --- | --- | --- | --- |
| = Malware |     | = Tool          |     |     |     |     |     |     |             |     |               |     |     |     |     |

Special Report: Mandiant M-Trends 2026 46
The metrics reported in this section are based on Mandiant Consulting
investigations affecting organizations in Europe, the Middle East,
EMEA and Africa (EMEA).
Initial Infection Vector
For Mandiant investigations affecting EMEA in 2025, the top initial infection vectors were
exploits (51%), email phishing (12%), and prior compromise (9%). Exploits and prior compromise
were the first- and third-most commonly observed vectors globally in 2025, but email phishing
had a higher prevalence in EMEA than in global statistics. In 2024 investigations, the top two
categories were also exploits and email phishing, though the third-most common vector was
brute-force attacks.
EMEA
Detection by Source
Exploit
51% Organizations first detected evidence of malicious activity internally in 60% of the
Email Phishing compromises Mandiant investigated in EMEA in 2025, and external notifications were the
12% first indication in 40% of cases. This is a reversal from 2024, when internally discovered
Prior Compromise incidents represented 41%, and externally notified events represented 59%
9%
EMEA Detection by Source, 2017-2025
100
Internal
External
80
60
40
20
0
2017 2018 2019 2020 2021 2022 2023 2024 2025
egatnecreP

Special Report: Mandiant M-Trends 2026 47
Median Dwell Time
The median dwell time for Mandiant investigations in EMEA in 2025 was 20 days, 19 days for
internally discovered incidents, and 21 days for externally notified events. Compared to 2024,
the overall median dwell time for incidents investigated decreased by seven days.
)syaD(
emiT
llewD
EMEA Median Dwell Time, 2016-2025
500
All
450
External
400
Internal
350
300
250
200
150
100
50 2021
19
0
2016 2017 2018 2019 2020 2021 2022 2023 2024 2025
The EMEA dwell time distribution reveals that over the long term, dwell times for incidents
Mandiant investigated in EMEA have grown more concentrated towards shorter dwell times.
For example, incidents discovered within one week increased from 36.7% in 2024 to 40.3%
in 2025, and incidents discovered between one week and one month increased from 16.5%
to 19.4%.
EMEA Dwell Time Distribution, 2021-2025
2021 % % % % % %
33.0 14.0 22.0 12.0 14.0 6.0
2022 % % % % % %
41.6 12.2 17.7 10.2 11.5 7.0
2023 % % % % % %
35.9 20.5 23.1 6.4 14.1 0.0
2024 % % % % % %
36.7 16.5 27.8 3.8 12.7 2.5
% % % % % %
2025
40.3 19.4 25.4 4.5 9.0 1.5
≤ 1 week 8 to 30 days 31 days > 6 months > 1 year 5 years
to 6 months to 1 year to 5 years or more

Special Report: Mandiant M-Trends 2026 48
For more
information
Threat Groups
about UNC1549,
please see:
Mandiant investigated several incidents affecting organizations in EMEA related to two distinct
Frontline
activity clusters exploiting CVE-2025-31324 as a zero-day. Observed activity was largely limited
Intelligence:
Analysis of UNC1549 to establishing an initial foothold, for example through dropping the JSPKIT web shell.
TTPs, Custom
Tools, and Malware In 2025, Mandiant encountered multiple compromises that GTIG attributes to the Iranian
Targeting the
cyber espionage threat cluster UNC1549 in EMEA. Prior to discovery, the threat cluster had
Aerospace and
Defense Ecosystem maintained access to compromised organizations for periods spanning months to upwards of
two years. UNC1549 deployed custom malware including MINIBIKE and TWOSTROKE backdoors
and targeted credentials both for privilege escalation and for potential utility in targeting
additional organizations.
Campaigns and Global Events
In 2025, the GTIG tracked multiple campaigns and global events that directly correlated to
Mandiant investigations in EMEA. The Campaigns and Global Events timeline summarizes
prominent threat activity observed in the region.
Please see the graphic on the following page for more detail.

Special Report: Mandiant M-Trends 2026 49
2025 EMEA Campaigns and Global Events Related to Mandiant Incident Investigations
| 2024 |     |     |     |     |     |     | 2025 |     |     |     |     |     |     | 2026 |
| ---- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | ---- |
Nov Dec Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec Jan Feb
|     |  UNC1543   |  FAKEUPDATES |     |     |     |     |     |     |     |     |     |     |     | CAMP.25.039 |
| --- | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- |

|     |  UNC2165  |  FAKEUPDATES |     |     |     |     |     |     |     |     | CAMP.24.024 |     |               |     |
| --- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------- | --- |
|     |  MULTIPLE |              |     |     |     |     |     |     |     |     |             |     | GLOBAL.25.001 |     |

600.42.LABOLG
   MULTIPLE   SIGSEGA   LUNALIGHT   CVE-2024-0012   CVE-2024-9474 GLOBAL.24.006
|     |  UNC5923  |  SIGSEGA  |     |  CVE-2024-0012  |  CVE-2024-9474 |     | CAMP.24.080 |     |     |     |     |     |     |     |
| --- | --------- | --------- | --- | --------------- | -------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |

CAMP.25.017
|     |  UNC2465   |  SMOKEDHAM             |              |  LOCKBIT |     |     |             |     |             |     |             |     |              |     |
| --- | ---------- | ---------------------- | ------------ | -------- | --- | --- | ----------- | --- | ----------- | --- | ----------- | --- | ------------ | --- |
|     |  UNC6016   |  SLOWFALL              |              |          |     |     |             |     |             |     |             |     | CAMP.25.007  |     |
|     |  UNC6040   |  UNC6240               |              |          |     |     |             |     | CAMP.25.032 |     |             |     |              |     |
|     |  UNC5978   |                        | CAMP.25.004  |          |     |     |             |     |             |     |             |     |              |     |
|     |  UNC6448   |  SELFDRIVE, AUTOPILOT  |              |          |     |     |             |     |             |     |             |     | CAMP.25.062  |     |
|     |            |  UNC1069               |  BIGMACHO    |          |     |     |             |     |             |     | CAMP.25.042 |     |              |     |
|     |            |  UNC4696               |  HAVOCDEMON  |          |     |     | CAMP.25.019 |     |             |     |             |     |              |     |

|     |     |  UNC5221  |  BRUSHFIRE  |  CVE-2025-22457 |                  |           |     | GLOBAL.25.002 |     |     |     |     |               |     |
| --- | --- | --------- | ----------- | --------------- | ---------------- | --------- | --- | ------------- | --- | --- | --- | --- | ------------- | --- |
|     |     |           |             |    MULTIPLE     |  CVE-2025-31324  |           |     |               |     |     |     |     | GLOBAL.25.003 |     |
|     |     |           |             |                 |    UNC6286       |  RHYSIDA  |     |               |     |     |     |     | CAMP.25.050   |     |
400.52.LABOLG
|     |     |     |     |     |     |     |     |    MULTIPLE   |     |  CVE-2025-53770 |     | GLOBAL.25.004 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------------- | --- | ------------- | --- | --- |
   UNC6357   LOCKBIT.WARLOCK  CVE-2023-29357   CVE-2023-24955 CAMP.25.072
|     |     |     |     |     |     |     |     |     |    UNC6337  |  TOOLSHELL  |     |  CVE-2025-53770 |     | CAMP.25.046 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | --- | --------------- | --- | ----------- |
|     |     |     |     |     |     |     |     |     |  UNC6564    |  UNC6240    |     | CAMP.25.078     |     |             |
800.52.LABOLG
|     |     |     |     |     |     |     |     |    MULTIPLE  |  CVE-2025-55182 |               |                 | GLOBAL.25.008 |     |             |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------------- | ------------- | --------------- | ------------- | --- | ----------- |
|     |     |     |     |     |     |     |     |              |  UNC6588        |  COMPOOD      |  CVE-2025-55182 |               |     | CAMP.25.083 |
|     |     |     |     |     |     |     |     |              |    UNC6566      |  “Shai-Hulud” |                 |               |     | CAMP.25.079 |
Financially motivated
Espionage
Multiple/Unknown
| = Actor   |     | = Vulnerability |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| = Malware |     | = Tool          |     |     |     |     |     |     |     |     |     |     |     |     |

Special Report: Mandiant M-Trends 2026 50
The metrics reported in this section are based on Mandiant investigations
JAPAC affecting organizations in the Japan and Asia Pacific regions (JAPAC).
Initial Infection Vector
The most frequently observed initial infection vector for 2025 Mandiant investigations in
JAPAC was exploits, at 33%, followed by stolen credentials at 23%. The ranking of these two
vectors is consistent with 2024 investigations; however, exploits were much more prominent
in 2024, representing the vector for 64% of compromises. The third-most common vector in
2025 investigations in JAPAC was prior compromise at 16%.
JAPAC
Detection by Source
Exploit
33% Organizations were notified of a potential compromise from an external organization in 51% of
Stolen Credentials the compromises Mandiant investigated in JAPAC in 2025, while internally discovered incidents
23% represented 49% of the dataset. This is a significant shift compared to 2024, when external
Prior Compromise notifications accounted for 69% of investigations, and internal discovery 31%.
16%
JAPAC Detection by Source, 2017-2025
100
Internal
External
80
60
40
20
0
2017 2018 2019 2020 2021 2022 2023 2024 2025
egatnecreP

Special Report: Mandiant M-Trends 2026 51
Median Dwell Time
Median dwell time for compromises Mandiant investigated in JAPAC in 2025 was 15 days overall,
seven days for internally discovered incidents, and 38 days for externally notified incidents. The
overall and externally notified medians are significantly higher than observed in 2024—6 and 10,
respectively. The increases in 2025 likely reflect the presence of a number of intrusions in which
threat clusters prioritized stealth and remained undiscovered for extended periods, including
cyber espionage incidents as well as financially motivated clusters conducting reconnaissance
for months before executing payment transfer fraud.
1100
1000
500
450
400
350
300
250
200
150
100
50 38
15 7
0
2016 2017 2018 2019 2020 2021 2022 2023 2024 2025
)syaD(
emiT
llewD
JAPAC Median Dwell Time, 2016-2025
All
External
Internal
The dwell time distribution for JAPAC investigations also reflects this shift, with greater propor-
tions of 2025 incidents falling into the one week to a month (21.6%), one month to six months
(21.6%) and six months to one year (11.8%) time windows compared to 2024.
JAPAC Dwell Time Distribution, 2021-2025
2021 % % % % % %
36.4 23.6 20.0 3.6 3.6 12.7
2022 % % % % % %
37.7 11.7 21.6 8.4 16.7 5.0
2023 % % % % % %
48.1 18.5 20.4 7.4 5.6 0.0
2024 % % % % % %%
51.2 14.0 18.6 4.7 11.6 00..00
% % % % % %
2025
43.1 21.6 21.6 11.8 2.0 0.0
≤ 1 week 8 to 30 days 31 days > 6 months > 1 year 5 years
to 6 months to 1 year to 5 years or more

Special Report: Mandiant M-Trends 2026 52
Threat Groups
In 2025, multiple Mandiant investigations in JAPAC were attributed to a suspected PRC-nexus
cyber espionage cluster exploiting CVE-2025-31324 after the patch date in April 2025.
This threat cluster sent basic reconnaissance commands to web shells installed on vulnerable,
compromised devices, but it is unclear whether this cluster installed the web shells.
Mandiant encountered another threat cluster in multiple JAPAC compromises in 2025 that
also exploited CVE-2025-31324 after the patch date. This threat cluster typically installed the
KRABDRIP downloader and conducted reconnaissance.
Campaigns and Global Events
In 2025, GTIG tracked multiple campaigns and global events that directly correlated to
Mandiant investigations in the JAPAC region. The Campaigns and Global Events timeline
summarizes prominent threat activity observed in the region.
Please see the graphic on the following page for more detail.

Special Report: Mandiant M-Trends 2026 53
2025 JAPAC Campaigns and Global Events Related to Mandiant Incident Investigations
| 2024 |     |     |     |     | 2025 |     |     |     |     | 2026 |
| ---- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | ---- |
Nov Dec Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec Jan Feb 100.52.LABOLG
|    MULTIPLE |           |                |     |     |     |     |     |     | GLOBAL.25.001 |     |
| ----------- | --------- | -------------- | --- | --- | --- | --- | --- | --- | ------------- | --- |
|  UNC5518    |  UNC5774  |  CORNFLAKE.V2  |     |     |     |     |     |     | CAMP.24.062   |     |

|    UNC6016   |  SLOWFALL              |              |                  |     |     |     |     |     | CAMP.25.007   |     |
| ------------ | ---------------------- | ------------ | ---------------- | --- | --- | --- | --- | --- | ------------- | --- |
|    UNC6448   |  SELFDRIVE, AUTOPILOT  |              |                  |     |     |     |     |     | CAMP.25.062   |     |
|              |                        |    MULTIPLE  |  CVE-2025-31324  |     |     |     |     |     | GLOBAL.25.003 |     |
400.52.LABOLG
|     |     |     |     |     |    MULTIPLE   |     |  CVE-2025-53770 |     | GLOBAL.25.004 |     |
| --- | --- | --- | --- | --- | ------------- | --- | --------------- | --- | ------------- | --- |
   UNC6357   LOCKBIT.WARLOCK  CVE-2023-29357   CVE-2023-24955 CAMP.25.072
800.52.LABOLG
|     |     |     |     |             |    MULTIPLE  |  CVE-2025-55182 |              |                 | GLOBAL.25.008 |             |
| --- | --- | --- | --- | ----------- | ------------ | --------------- | ------------ | --------------- | ------------- | ----------- |
|     |     |     |     |             |              |  UNC6602        |  HOTTEA      |  CVE-2025-55182 |               | CAMP.26.001 |
|     |     |     |     |    UNC6590  |              |  XMRIG          |  TRUFFLEHOG  |  CVE-2025-55182 |               | CAMP.26.002 |
Financially motivated
Espionage
Multiple/Unknown
| = Actor   | = Vulnerability |     |     |     |     |     |     |     |     |     |
| --------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| = Malware | = Tool          |     |     |     |     |     |     |     |     |     |

SPECIAL REPORT: MANDIANT M-TRENDS 2023 54
O
G
R
A
B
M
E

Special Report: Mandiant M-Trends 2026 55
A Minor Infection Today
Can Be a Ransomware Attack Tomorrow
In recent years, Mandiant has observed a gradual upward trend toward increased specialization of threat groups within
a broader cybercrime ecosystem. In 2025, 9% of the incidents Mandiant investigated followed a “division of labor”
model for the initial intrusion, up from 4% in 2022. This model involves two or more threat groups, where one group
focuses exclusively on initial access operations to gain a foothold in an environment, and the subsequent group
or groups perform the remaining stages of the attack lifecycle. Initial access partners, the threat clusters specializing
in initial access operations, have employed low-impact, opportunistic techniques, such as malicious advertisements or
non-targeted drive-by downloads to breach an organization and establish persistence. Subsequently, the initial access
partner performs a “hand-off” and provides access to a secondary threat group. These secondary threat groups often
engage in high-impact activity, such as deploying ransomware, during the latter stages of the targeted attack lifecycle.
Mandiant has observed evidence indicative of closer coincided with their earliest interactive activity. However,
collaboration between initial access partners and Mandiant has also regularly observed incidents in which
secondary groups. A key signal is the time delta between a longer time delta existed between a secondary group’s
the earliest activity by an initial access partner and earliest activity and their earliest interactive activity.
the hand-off to a secondary threat cluster, which has In these cases, activity is attributed to a secondary
been steadily decreasing since 2023. In this context, group before that group ever interacts with an
the “earliest activity” is the earliest activity in the environment, indicating that the initial access partner
environment that can be attributed to an attacker. established access directly on behalf of the secondary
This includes non-interactive events, such as the group for them to utilize on their own timeline. While
distribution of malware, and represents the moment this still provides defenders with an opportunity to stop
at which a group gains access to an environment, the attack before it becomes more consequential, the
whether they utilize it or not. A hand-off occurs at the timeline is likely more constrained than if the threat actor
moment of earliest activity by a secondary group. had to sell access via underground channels.
In 2022, Mandiant identified the median time between
This changing cybercrime ecosystem poses substantial
initial access and subsequent hand-off was greater
challenges to security teams. Under a closer partnership
than 8 hours. However, in 2025, the median time between
model, organizations now have significantly less time to
initial access and the time at which a second group had
remediate low-impact initial intrusion and persistence
access to the environment was 22 seconds. In many
events before a secondary group leverages that access
cases, this reflects the often automated process
for higher-impact activity. Organizations hunting solely
through which initial access partners deliver malware
for high-impact tactics, techniques, and procedures
directly on behalf of the secondary group instead of
(TTPs) in their environment may not have high-priority
advertising access in an underground forum.
detections in place for low-impact initial intrusion vectors.
This is when the clock starts for defenders; security While triaging low-impact alerts in a high-volume
teams will ideally remediate the intrusion before the environment places downward pressure on security
moment of earliest interactive activity. The “earliest teams, stopping an intrusion at a single-system stage is
interactive activity” refers to the earliest event that significantly easier than recovering from follow-on activity.
signifies interactive operations, such as conducting
reconnaissance or moving laterally. In some cases,
the earliest activity attributed to a secondary group

Special Report: Mandiant M-Trends 2026 56
financially motivated threat clusters such as UNC5774
Initial Access Partners
purchased access to distribution services created
Initial intrusion to an environment by an initial access by UNC5518 to distribute their own tooling. These
partner is generally opportunistic and leverages secondary groups sometimes also partner with
low-impact TTPs. Over the last year, Mandiant has ransomware-as-a-service (RaaS) operators to obtain
observed initial access partners utilizing Phishing both the ransomware they deploy and support for the
(T1566), Drive-by Compromise (T1189), and Malvertising extortion of compromised organizations.
(T1583.008) techniques to later harvest credentials
with infostealers, create persistence mechanisms,
UNC6016
and conduct reconnaissance in infected environments.
UNC6016 is a malware distribution threat cluster which
In some cases, an initial access partner gains a foothold
has been active since at least November 2024. The
into an environment prior to selling that access. This
group uses search engine optimization techniques and
type of partner casts a wide net to build an inventory
malicious advertising, or “malvertising”, to direct users
of compromised networks which they can later monetize
to compromised websites. Once on these sites, users
within the broader cybercrime ecosystem. They then
are lured to download malware disguised as legitimate
advertise access based on multiple factors, including
popular software. While this technique is neither novel
the revenue of the target, industry vertical, country,
nor sophisticated, it continues to be an effective means
and type of access being sold. Some of these groups
of initial access for opportunistic infections. In one
will simply sell credentials, while others sell access to
investigation involving UNC6016, Mandiant identified
an existing malware infection or bot. Another category
evidence that a user was directed to a compromised
of initial access partner sells their ability to distribute
website through malicious advertising and downloaded
malware or gain access on behalf of secondary groups
a backdoored version of a popular SSH client. Once
prior to compromising an environment. These initial
the user executed the trojanized application, infecting
access partners either advertise their availability to
their local endpoint, UNC6016 provided UNC4696
distribute malware on behalf of secondary groups, or
access to the resulting backdoor. UNC4696 is a financially
respond to advertisements posted by groups seeking
motivated threat actor that monetizes access by
initial access or malware distribution.
deploying ransomware. Mandiant’s investigation iden-
One example of an initial access partner that creates their tified that this secondary impact group moved laterally,
own foothold is the financially motivated threat cluster installed command and control (C2) backdoor implants,
UNC5518. In a campaign tracked by the Google Threat and eventually stole a significant volume of customer
Intelligence Group (GTIG) in 2024 and 2025, Mandiant data. Ultimately, UNC4696 deployed ransomware across
found that UNC5518 typically compromised legitimate the environment and made extortion demands.
websites to distribute the JavaScript downloader
While Mandiant was investigating and helping the
FAKETREFF to unsuspecting users. This campaign has
customer regain access to their environment, UNC6016
evolved over time. Initially, UNC5518 injected a fake
regained access to the same environment when an
browser update lure into vulnerable websites that
unrelated trojanized application was downloaded and
redirected users to threat-actor-controlled infrastructure
executed. UNC6016 provided this foothold to another
and dropped FAKETREFF. More recently in 2025, UNC5518
secondary group, UNC6286. UNC6286 is a financially
began using the ClickFix technique, where a malicious
motivated actor that almost exclusively uses UNC6016’s
pop-up instructs the user to execute the first-stage
malvertising to distribute trojanized software. In this
FAKETREFF payload via the Windows Run dialog or
case, UNC6286 deployed additional malware, including
the PowerShell console. This technique bypasses the
a dropper, a downloader, and a tunneler. The threat
need to download any artifacts onto the user’s machine
actors moved laterally, created new accounts, but were
directly from the browser, limiting opportunities for
quickly intercepted when they attempted to acquire
detection by endpoint tools and reducing the forensic
credentials and domain information. Unlike the initial
footprint of the suspicious activity. Following a successful
infection where UNC4696 was able to achieve their final
compromise, the FAKETREFF malware initiates the down-
objective, UNC6286’s activity was remediated within two
load of a secondary payload to establish persistence.
hours of accessing the environment.
Mandiant has identified evidence to indicate that

Special Report: Mandiant M-Trends 2026 57
The swift reaction to the second intrusion was driven by activity. Additionally, investigators can expect a longer
the heightened vigilance of the security team during the period of inactivity between the initial intrusion and
first incident. This allowed the security team to contain follow-on activity while access is advertised and
the activity while the impact to the business was still purchased.
minimal. However, it was the actions of the secondary
group which spurred the timely response, when early This time delta between initial access and the earliest
detection and removal of the trojanized download could interactive activity by a secondary group is critical for
have limited impact to a single system. These intrusions defenders; breaking the persistent access and changing
highlight the necessity of a shift toward a more aggressive impacted passwords can prevent intrusions from
security posture beyond the period of active incidents, escalating. In this hand-off model, the delta is, in part,
as even routine malware infections require deliberate determined by internal and external market forces of
attention and remediation to respond to security the cybercrime ecosystem. One such factor is the type
Frisikgs euffercetiv e1ly:. Initial Access Partner vso fS acececsso bneindg asorldy. F oGr erxaomuplep, c eTrtTainP follow-on
Initial Access Partner Secondary Group
Initial Establish Internal Escalate Internal Mission
Compromise Foothold Recon Privileges Recon Complete
Actor Hand-off
Figure 1: Initial Access Partner vs Secondary Group TTP
Handing Off
threat groups may prefer SSH credentials over installed
Initial access partners can follow any one of several backdoors. Some follow-on actors will refuse to purchase
models for handing off access, each of which access to organizations in certain industry verticals,
manifests differently during an investigation. In the possibly due to perceived risk levels. Major cybersecurity
classic model, the initial access partner opportunistically incidents in an industry can also act as a signal to
acquires access to multiple environments. The group the cybercrime ecosystem to focus efforts on that
then advertises that access on underground forums industry. Additionally, high revenue in an industry may
with general information about the compromised indicate to threat groups a higher reward for the
organization and environment, including location, potential risk. Recent changes in tradecraft, including
industry sector, company revenue, and type of access. but not limited to the availability of 0-days or the release
Second-stage threat groups monitor those channels of publicly available tooling, can also affect market
and purchase access in the form of IP addresses, conditions. Initial access partners may also internally
credentials, backdoors, or other mechanisms. In these assess operational risks such as the threat of sanctions
cases, there is likely to be very little overlap in TTPs or investigations by governments when choosing to
between the initial access operations and follow-on partner with follow-on groups.

Special Report: Mandiant M-Trends 2026 58
Another model for a hand-off is led by the second-stage UNC1543, UNC2165, and RansomHub
threat group, rather than by the initial access partner.
One such pair of closely linked threat groups is the initial
In these scenarios, a second-stage threat actor advertises
access partner UNC1543 and the ransomware operator
on underground channels that they are seeking initial
group UNC2165. UNC2165 is a financially motivated threat
access to organizations in specific countries or possibly
group that shares significant overlap with the threat group
with specific target revenues. Some threat groups may
publicly reported as “Evil Corp,” which was sanctioned
indicate that they are unwilling to buy access to certain
by the Office of Foreign Assets Control in 2019. Although
industry verticals, such as healthcare, government,
UNC1543 has provided initial access to multiple groups,
or critical infrastructure due to operational risks. The
UNC2165 almost exclusively obtains access to environ-
second-stage threat groups offer a cut of the profits from
ments from UNC1543. UNC1543 typically gains access to
a compromise, typically 20-50%, as payment for initial
an environment opportunistically via drive-by download
access. Some second-stage threat groups also advertise
distributing FAKEUPDATES, a JavaScript downloader
that they are seeking partners to distribute their own
that communicates over HTTP and is often used to install
or preferred malware, which they can leverage for
secondary payloads.
high-impact activity. In these scenarios, because the initial
access partner does not need to find a buyer, the time In one case investigated by Mandiant in 2025, the earliest
between initial intrusion and earliest interactive follow-on evidence of attacker activity was traced to a browser
activity is likely to be shortened. The substantial session accessing a compromised website that led to
decrease in the time delta observed since 2022 between a FAKEUPDATES infection. Mandiant observed a period
initial access and the earliest event attributed to a of inactivity of approximately 70 minutes between the
secondary group may indicate a rise in the prevalence creation time of FAKEUPDATES on the target system and
of this hand-off model. Depending on the requirements the hand-off to UNC2165. UNC1543 used FAKEUPDATES
of the buyer, TTPs between initial access partner and to drop VIPERTUNNEL, a Python-based network tunneler
follow-on groups can either be distinct or closely linked, associated with UNC2165. The earliest interactive activity
depending on the preferences of the secondary group. attributed to UNC2165 occurred approximately 45 minutes
later, when UNC2165 used VIPERTUNNEL and reverse
A third, but less well defined, model for a hand-off
SSH connections to C2 addresses to establish persistent
involves initial access partners and second-stage threat
tunnels and conduct reconnaissance. The threat actors
groups who choose to partner with each other. Often, the
dumped credentials and moved laterally throughout
exact agreements between the two or more threat groups
the target network, then staged and stole terabytes
involved are unknown, and the delineation between the
of data through standard cloud-based file sync utilities.
groups can be blurred. In these cases, Mandiant generally
To complete the mission, UNC2165 destroyed system
observes the time between initial intrusion activity and
backups, then deployed RansomHub, a RaaS offering
the earliest activity attributed to a second-stage group
that abruptly ceased operations in April 2025, on both
is less than 30 seconds, consistent with the behavior of
Windows and virtual management servers.
a distribution cluster. The TTPs between the two groups
can often be distinct, and a close partnership can give The use of a RaaS further demonstrates specialization
network defenders an advantage. If a detection is raised within the cybercrime ecosystem. Since February 2024,
for TTPs consistent with an initial access partner which multiple threat clusters, including UNC2165 and the
has a known relationship to a second-stage group, the high-impact ransomware group UNC3944, have deployed
intelligence related to both groups can guide the hunt for the RansomHub encryptor during incidents. This is
follow-on activity. consistent with RansomHub advertising for affiliates
on underground sites. In RansomHub’s business model,
affiliates, who were asked to pay a $5,000 deposit, kept
90% of any ransom payments made, and the remaining
10% went to the service operators. UNC2165 historically
deployed exclusive ransomware variants but has shifted
to RaaS in recent years; Mandiant previously reported
that this shift may have been made to impede attribution

Special Report: Mandiant M-Trends 2026 59
and avoid sanctions. Partnering with specialized service IT teams can integrate with security teams to deliver
providers not only reduces the technical requirements on detailed requirements of their common workflows and
a single threat group, but also supports anonymity. help define the baseline activity which can be expected
to occur within their environments. By generating a set
FAKEUPDATES itself is a low-impact malware sample. The
of pre-approved and centrally stored tools for IT teams
distribution method, drive-by downloads, is opportunistic
and users, security teams can help reduce the variety
and not indicative of a targeted attack. However, due to
of process execution expected for each business unit.
relationships such as those observed between UNC1543
Either proactively deploying the tools users need or
and UNC2165, security teams can associate alerts for
providing a low-friction interface for installation can
FAKEUPDATES with high criticality response efforts due
help reduce the occurrence of opportunistic infections
to the likelihood of high-impact follow-on activity.
originating from self-installs of potentially trojanized
tools. Security teams can, in turn, build detections based
Recommendations on the requirements provided to them by each business
unit. In an environment where the pre-approved tools are
The risks posed by threat groups acting in concert to
provided to users, detections relating to the installation
hand off access to compromised environments force a
of tools or execution of binaries which fall outside of
significant workload onto both security and IT staff.
the pre-approved tooling should drop precipitously.
Many of the initial access partners rely on opportunistic
Such detections can either be associated with potential
infection as opposed to targeted compromise. This
attacker activity or provide an opportunity to better
can result in the activity associated with initial access
educate users as to the use of pre-approved tools defined
partners never rising to the level of concern that matches
by the requirements they provided.
the potential impact of the secondary groups to which
they provide access. The disparity between the criti- Reducing the variety of the expected behavior in an
cality of low-impact alerts and potential high-impact environment allows security teams the necessary space
outcomes necessitates a restructuring of how IT teams to review detections of low-impact activity and respond
operate and the response playbooks used by the security in the time frame necessary to protect their environments.
teams tasked with protecting the organization while also While the creation and maintenance of the baselines
enabling business continuity. needed to support this outcome are time intensive, the
ability to respond rapidly to risks such as initial access
As the potential risk posed by low-impact activity rises,
partners is a key factor of success for any security team.
the leeway for security teams to deprioritize the response
Organizations can further limit the potential impacts
to alerts for that activity drops significantly. However,
of a hand-off by optimizing their workflows for detection
the volume of low-impact alerts and the personnel needed
and focusing on event correlation during alert review and
to review and resolve them presents a natural barrier to
response procedures. Enriching alerts with contextual data
the effective security of an organization. Security teams
can help highlight patterns of behavior which may indicate
are regularly overwhelmed by alert volume, leading to
a potential high-impact intrusion pattern. Organizational
a condition commonly referred to as “alert fatigue” in
alignment towards these outcomes is a crucial aspect
which analysts are desensitized to alerts or alerts simply
of a mature security posture. By appropriately staffing
pile up until they are bulk resolved without proper analysis.
security teams, encouraging collaboration, and increasing
This outcome can be attacked from multiple angles by
the signal-to-noise ratio in detection tooling, organizations
creating a symbiotic relationship between security teams,
create a strong foundation on which they can build.
IT teams, and the users that they support. Ensuring that
This foundation helps ensure that as the organization
all three groups are working towards the common goal
grows, the security infrastructure and culture necessary
of a secure environment that enables their work can help
to achieve the desired outcomes keeps pace.
reduce the volume of low-impact alerts which security
teams have to triage.

Special Report: Mandiant M-Trends 2026 60
Ransomware is Now a Resilience Problem
The traditional framing of ransomware as simply a dual threat of encryption and data theft no longer captures the
reality of modern extortion operations. Ransomware operators and affiliates have increasingly prioritized denying
targeted organizations the ability to recover. Threat actors are targeting system and administrative planes also known
as trusted service infrastructure . The terminology of “trusted service infrastructure” (TSI) is typically associated
with management interfaces for platforms and technologies that provide core services for an organization such
as backup technologies and virtualization platforms. This allows ransomware operators and affiliates to reduce an
organization’s ability to recover while maximizing the pressure to pay. They do this by attacking identity services,
virtualization management planes, and backup infrastructure.
This evolution in tactics has compressed the intrusion timelines observed by Mandiant during investigations.
Ransomware operators have collapsed the year-over-year dwell times for ransomware compromises, frequently
seizing administrative control within hours of initial access. The velocity of these intrusions often forces defenders
to preemptively disconnect their own Identity Providers (IdP) to halt the spread, effectively triggering a self-inflicted
business outage to prevent total compromise. As a result, organizational survivability predicated on Endpoint Detection
and Response (EDR) or traditional backup restoration at the endpoint layer are no longer sufficient recovery models.
Instead, a model focused on resilience, which seeks to address the primary objectives attackers pursue, represents
the best chance for organizations to keep pace with the rapid evolution of ransomware operators.
In this context, the TSI fabric is not simply an inventory of “critical assets”. It is the operational terrain on which
ransomware campaigns achieve scale and where recovery is either enabled or prevented.
password rotation requirements. Mandiant has also inves-
Attackers Weaponize
tigated incidents where attackers used administrative
the Administrative Fabric
commands and specialized extraction tools to steal the
Modern ransomware campaigns are no longer random entire AD database, exposing every hash and effectively
smash-and-grab operations; they are, instead, structured compromising every user credential in the domain.
takeovers of the IT administrative infrastructure. Attackers
Threat actors have also started to engage in forms of
understand that an enterprise is an interdependent web
high-volume credential harvesting and disruption activity
of trust. In 2025, Mandiant investigated multiple breaches
during intrusions. In several investigations, Mandiant
in which threat actors used “Living Off the Land”
identified evidence that the threat actors targeted the
techniques, turning an organization’s own administrative
organization’s domain controllers (DC) and then accessed
tooling and trusted security controls into primary
localized enterprise credential vaults to extract dozens
attack vectors.
of high-privilege credentials in a single session. To further
destabilize the environment, adversaries executed rapid
The Identity Core
reconnaissance followed by scheduled tasks which forced
The path to total control of a targeted environment almost password changes for privileged administrative accounts.
always begins with identity, but sophisticated groups This combination of actions locked defenders out of their
have moved beyond simple credential theft and are, own emergency accounts during a crisis.
instead, manipulating the identity control plane. In many
In some attacks, the targeting of identity extended to the
of the ransomware incidents which Mandiant investi-
cloud. Adversaries pivoted from a compromised Microsoft
gated in 2025, attackers exploited misconfigured Active
Entra ID tenant to hijack associated Azure storage
Directory (AD) Certificate Services templates to issue
accounts, utilizing the corporate identity provider to
certificates and create or impersonate admin accounts.
unlock and destroy the infrastructure backend.
These attacker-controlled accounts weren’t subject to
multi-factor authentication (MFA) and were excluded from

Special Report: Mandiant M-Trends 2026 61
Fleet Management instantly. The impact of targeting the virtualization layer
can often be comprehensive. An Akira ransomware attack
Many of the tools on which organizations rely for
resulted in the successful encryption of most virtualized
day-to-day operations often become targets during
servers. This resulted in a complete loss of investiga-
ransomware events. Ransomware threat actors have
tive visibility due to network telemetry logs having been
extended this targeting to even include the tools
encrypted alongside the production servers. The loss
which were designed for patching and security due to
of critical telemetry created substantial friction in the
their ability to distribute packages at scale within the
organization’s efforts to identify data theft.
environment. Mandiant has identified evidence of threat
actors weaponizing group policy objects (GPO)
Targeting Safety Nets
to create scheduled tasks across thousands of endpoints
which execute immediately, turning the domain’s own The final and often most devastating stage of the
management fabric into a mass-distribution engine for compromise is the destruction of backups. Attackers
ransomware. In other instances, attackers compromised actively perform reconnaissance on backup architectures,
Microsoft Endpoint Manager service accounts, leveraging accessing admin consoles and documentation repositories
their administrative privileges to pivot directly to a to map out storage locations, SQL configurations, and
DC and seize control of the entire domain hierarchy. retrieve encryption configurations. Once the location and
In some cases, threat actors use the organization’s fleet access to resources are mapped out, threat actors will
management capabilities to disable features, such as often systematically destroy the elements critical to the
PowerShell logging, which can be critical to attacker recovery of the environment. The information gleaned
detection across the environment. from the reconnaissance phase of the intrusion can also
form the basis for the escalation of privileges necessary
The Virtualization Layer to impact backup infrastructure. In one example, Mandiant
identified evidence that the threat actor compromised
In recent investigations, Mandiant has identified attacker
backup management servers in order to extract and
behaviors that indicate threat actors are treating the
decrypt credentials which were stored in the configuration
hypervisor as more than a target for encryption. Rather
database. The exposed credentials granted the threat
than only encrypting the hypervisor and guest operating
actors direct access to the administrative passwords
systems, threat actors are also using it as a staging
for storage controllers and cloud accounts. The threat
ground for data theft. In recent investigations, Mandiant
actors used the stolen credentials and keys to execute
identified evidence of threat actors compromising
broad-scale deletion commands, wipe millions of backup
virtualization hosts to execute reconnaissance tools
objects from cloud storage, and delete dozens of local
and archiving utilities directly on the virtualization host.
system backups.
Attackers used archiving tools directly on the hypervisor
to compress and archive the Virtual Hard Disks of backup In on-premises scenarios, the deletion activity can
servers. This allowed the attackers to steal critical data be equally as destructive and thorough. Mandiant
volumes while bypassing data loss prevention controls identified evidence that the attackers deleted the backup
running inside the guest operating systems. configurations from the backup server which unlinked
the virtualization environment from the backup platform.
Adversaries also exploit the convergence of Identity and
While the backup data was held on immutable storage
Virtualization to seize control. Mandiant has identified
and not destroyed, it became inaccessible through the
ransomware threat actors weaponizing the default
backup platform user interface and required a lengthy
virtualization admin group used in some AD integrations.
engagement with the vendor of the backup solution
By adding a compromised service account to the
to start recovery. In another example, threat actors
AD group, they automatically inherited administrator
compromised network-attached storage (NAS) appliances
privileges on all domain-joined virtualization hosts.
via SSH to enable the local admin account and change
This allowed the threat actor to disable firewalls and
passwords. The attackers then installed data theft
mass-deploy ransomware to dozens of hypervisors
tools to steal critical volumes before encrypting those
same volumes, ensuring that the local recovery point
was destroyed.

Special Report: Mandiant M-Trends 2026 62
Where Recovery Can Fail Velocity
The compromise and weaponization of Tier-0 assets The encryption or destruction of virtualization and backup
transcend a simple service outage; it creates a funda- control planes can severely impede the progress of
mental recovery deadlock during which the foundational restoration activity in impacted environments. When an
trust required for restoration is lost. In such scenarios, organization’s hypervisors are encrypted alongside the
the standard incident response playbooks break down on-premises backups, the hardware may still function,
because the tools and trust required to execute them are but the logical infrastructure is inoperable. In cases
unavailable. Mandiant’s frontline experience highlights where backup catalogs are wiped or cloud buckets are
three primary failure scenarios that can rapidly escalate deleted via stolen keys, the organization loses its primary
the criticality of a ransomware incident. recovery capability. As a result, teams working to restore
the environment are forced to rely on slower, older
Identity archival data, leading to a risk of additional data loss and
extended downtime.
When the identity fabric is fundamentally compromised,
such as via Windows NT directory service theft or AD
Re-Compromise
Certificate Service forgery, the organization faces a
systematic identity collapse. Defenders cannot simply The recovery of compromised environments often relies
reset passwords because the attacker possesses the on workflows where teams reimage impacted systems
cryptographic keys necessary to complete the reset. and restore data from backups. These workflows, in turn,
This can often force a “Greenfield” recovery during rely on the availability of trusted restoration sources.
which a new, trusted AD forest is created while operations A critical aspect of recovery denial activity is the embed-
remain impacted in the production environment. This ding of persistence mechanisms into the infrastruc-
form of recovery imposes a staggering operational tax ture used to manage the recovery. By configuring fleet
as restoration timelines stretch from days to weeks, and management tools or hypervisor templates to include
financial losses compound as IT teams are forced the deployment of attacker-controlled backdoors as part
to rebuild the entire identity backbone manually rather of deployment operations, threat actors ensure they
than simply restoring data. Crucially, this often extends are able to retain access to the targeted environment.
to organizational communication channels as well. Consequently, the very process of remediation triggers a
If the compromised identity provider federates to reinfection of the environment, turning the organization’s
corporate email or collaboration platforms, defenders own recovery tools into a distribution mechanism for the
lose their primary means of coordination during response threat actor.
activity. As a result, they are forced to rely on out-of-band
communications or risk leaking sensitive information to
an attacker who retains broad access to the collaboration
and email platforms.

Figure 2: The Resilience Maturity Matrix Special Report: Mandiant M-Trends 2026 63
High
Tier-0
Isolation
Fragile Prevention Active Resilience
• Over-indexed on prevention • Hardened identity
Zero Standing
Privileges • No isolated recovery capability • Recovery severed from
• Hard perimeter, fragile defense attack surface
• Balanced friction and recovery
Hardened
Minimal Identity
Viable
Security Weak
Identity
Existential Exposure Repetitive Recovery
• No defense friction • Recovery-heavy capabilities
Standing
Privileges • Insufficient safety nets • Cannot stop recurring compromise
• Fundamental architecture deficits • Loop breach and restoration
Flat
Network
Low Mutable Shared File-Level Immutable Identity Active High
Backups Identity Strategy Storage Isolation IRE
Recovery Path Reliability
Figure 2: The Resilience Maturity Matrix
In contrast, Fragile Prevention occurs when organizations
Implementing Active Resilience
are over-indexed on prevention but lack ancillary recovery
The Resilience Maturity Matrix infrastructure such as isolated recovery capability,
immutable storage, or off-network copies of data. While
Resilience is not a single metric; it is the product of
the perimeter is difficult to breach, the defenses are rigid
prevention and recovery. Prevention can be measured
and fragile. Consequently, a single control plane bypass
as the degree of friction a threat actor experiences
can result in an unrecoverable event because the recovery
in trying to move through a targeted environment.
fabric shares the fate of the production environment.
Recovery can be measured by the level of confidence
an organization has in the restored environment. In Repetitive Recovery, the organization has invested
The controls which influence these values can be heavily in safety nets but lacks the defensive friction
mapped against two primary axes; Minimal Viable required to contain attackers after the initial breach.
Security and Recovery Path Reliability. While they can restore their data, they cannot stop the
recurring compromise. This leaves the organization able
The first quadrant, Existential Exposure, represents a
to survive the initial event but suffering high operational
state where an organization operates with fundamental
costs and continuous downtime cycles; trapped in a loop
architectural deficits. A lack of defensive friction allows
of breach and restoration.
adversaries to move unimpeded within the environment,
while the absence of offline safety nets ensures that Active Resilience is the target state, characterized by
the recovery environment is likely destroyed along- balanced friction and trusted recovery. The adversary is
side production. The outcome is often severe; recovery slowed by hardened identity controls, and the recovery
is statistically unlikely without acceding to extortion fabric is architecturally severed from the attack surface.
demands, and even then, success is not guaranteed. In this state, attacks are degraded from existential crises
into containable incidents. The organization retains the
authority to refuse extortion demands, secure in the
knowledge that their recovery path remains untainted.

Special Report: Mandiant M-Trends 2026 64
Active Resilience Hypervisor Hardening and Tier-0 Isolation
To move from Existential Exposure to Active Resilience, Virtualization control planes are force multipliers for
organizations should aim to increase defensive friction threat actors; a single compromise can translate into
and isolate the recovery path. broad operational failure. Formally treating hypervisors
and their management planes as TSI ensures the strictest
access constraints and highest-priority monitoring.
Increase Minimal Viable Security (MVS)
Severing AD integration reduces the risk that identity
Focus: Hardening Identity, Network, and
compromise becomes instant hypervisor-wide control,
Virtualization Layers.
and dedicated out-of-band management with local,
MFA-protected accounts reinforces that separation.
Secure Identity and Device Perimeters
Identity is the fastest path to TSI control, which is why Advance Recovery Path Reliability (RPR)
modern ransomware operations aim for control of priv-
Focus: Survivability and Identity Isolation.
ilege mechanisms and not just passwords. Conditional
access and Privileged Identity Management (PIM) matter
Survivable Recovery and Disaster Planning
because they make administrative access time-bound,
justified, and observable rather than ambient. Hardening Recovery often fails when trust anchors are compro-
high-impact identity pathways, such as auditing SPN mised alongside production, especially identity. Offline
accounts for Kerberoasting exposure and maintaining or immutable versions of Tier-0 assets create a recovery
a practiced process to reset the KRBTGT twice during option that doesn’t share the fate of production when
incident response, helps increase the friction of attacker attackers delete backups, corrupt catalogs, or seize
movement and confidence in restoration. Administrative admin consoles.
endpoints are part of the control plane. Using hardened
A dedicated, isolated recovery environment allows
Privileged Access Workstations (PAWs), enforcing MFA
teams to clean, validate, and stage system restores
and strong authentication, and reducing lateral movement
before reconnecting to production. An isolated recovery
shortcuts increases the attacker’s cost to move from
environment can directly mitigate a reinfection loop
foothold to domain-level control.
commonly found in the Second Wave failure mode.
This requires a formal Disaster Recovery process that
Network and System Hardening
assumes loss of the primary site and primary identity
Ransomware resilience improves when environments fabric, to account for ransomware operators increasingly
are intentionally difficult to traverse quickly. Zero-Trust designing their operations to target those resources as
segmentation that isolates TSI limits lateral movement a means of denying recovery.
into the administrative fabric and slows the sequence
that typically precedes large-scale encryption or backup
sabotage. Decommissioning end-of-life systems, proto-
cols, and configurations can remove common footholds
and reduce blind spots. Telemetry should be tuned to
the “Living Off the Land” behaviors, particularly partial
WMI execution and unauthorized PowerShell activity,
so defenders can identify the administrative takeover
phase before it impacts the environment more broadly.

Special Report: Mandiant M-Trends 2026 65
Tactical Governance and Threat Intelligence In this hostile landscape, the convergence of Information
Security and Business Continuity is absolute. A strategy
Static policies can become liabilities when attackers
reliant solely on prevention is inherently fragile as once
adapt to regain access or sabotage restoration.
an adversary renders the infrastructure unresponsive to
Updating verification procedures based on emerging
control, traditional detection stacks offer little in the way
tactics, techniques, and procedures, such as tightening
of mitigation. Resilience requires an architecture designed
help-desk workflows when social engineering patterns
to endure and recover from the compromise of these
shift, helps reduce reentry opportunities during the
internal control planes.
most fragile phase of recovery. Governance is of equal
importance during a recovery. Organizational leaders Ultimately, the transition to Active Resilience is achieved
must proactively define decision recovery playbooks through architectural discipline rather than tool
that prioritize integrity of the recovery fabric over acquisition. It necessitates the strict decoupling of
short-term uptime. This enables responders to preserve critical systems, the implementation of friction to impede
trusted recovery even under pressure. lateral movement, and recovery abilities that operate
independently of the primary identity fabric. Shifting
towards Active Resilience enables leaders to do
Resilience as a Contested Domain
more than just secure their data; it helps ensure an
The emergence of recovery denial marks a strategic
organization can maintain their operations while under
inflection point in the landscape of cyber extortion.
adversarial pressure.
Historically, organizations architected defenses under
the assumption that, while production environments
were contested, recovery environments remained secure.
Adversaries have industrialized the targeting of
Tier-0 administrative infrastructure, recognizing that
compromising an organization’s ability to recover is as
effective a lever for extortion as the theft of data.

Special Report: Mandiant M-Trends 2026 66
Multi-Year Intrusions Highlighting
Extreme Persistence
Sophisticated threat actors seeking long-term access to targeted environments remain a persistent and effective threat.
As threat actors continuously evolve to circumvent modern security technologies, the risk of covert attacker activity
going unnoticed increases. While these adversaries may deploy custom malware when necessary, they frequently
prioritize stolen credentials, limit their tooling to what is available in the targeted environment, and target systems less
likely to be instrumented with security tooling. Taken as a whole, state-sponsored espionage threat actors represent
heightened risk while presenting fewer and fewer opportunities for detection. Recent activity, such as UNC6201’s
BRICKSTORM campaigns, and UNC5807’s targeting of telecommunications networks, illustrates the ongoing adaptability
of sophisticated threat actors. Similarly, UNC1549’s targeting of third-party accounts to compromise their intended
targets demonstrates the concerted efforts espionage threat actors may engage in as they seek long term access.
Mandiant has also identified evidence of suspected state sponsored threat groups using anti-forensics techniques
to further obscure the activities they take in an environment. In all four campaigns, these suspected espionage threat
actors masqueraded as legitimate users within the target environment, and consistently pursued efforts that focused
on long-term access. As a result, in all four campaigns, the threat actors were able to maintain multi-year intrusions into
some of the targeted environments. Intrusions that span extended time periods force defenders and investigators to
rely on data sources that are historically under-utilized to answer critical questions regarding the security of the
environment and the actions of the attacker.
service account activity. The combination of legitimate
Observations
credentials and operational discipline that minimized
The operational discipline required to sustain multi-year
detection opportunities enabled UNC6201 to ensure
intrusions is perhaps best exemplified by UNC6201’s
pervasive access to targeted environments for extended
BRICKSTORM campaign. UNC6201 is a suspected
periods of time.
PRC-nexus espionage threat group that uses a
sophisticated backdoor called BRICKSTORM to target Similar to UNC6201, the PRC-nexus cyber espionage
virtualization infrastructure. While notable overlaps in group UNC5807, likely active since 2020, tends to focus
UNC6201 and UNC5221 activity have been reported its efforts on telecommunication backbones and network
as synonymous with the threat actor “Silk Typhoon” in routing infrastructure. UNC5807’s activity is generally
public reporting, Google Threat Intelligence Group (GTIG) consistent with the threat actor discussed in public
does not currently consider the two clusters of activity reporting as “Salt Typhoon.” UNC5807 systematically
to be the same. With an average dwell time exceeding exploits vulnerabilities in exposed network edge devices
390 days, UNC6201 established persistent footholds such as VPN solutions and routers to establish initial
in compromised environments using BRICKSTORM, access. Upon establishing an initial foothold, UNC5807
and often focused follow-on activity towards network commonly targets authentication protocols such as
edge appliances that sit outside the reach of endpoint TACACS+ and RADIUS for collection using packet capture
detection and response (EDR) tools. This threat actor in functionalities native to the appliances they compromise.
particular focuses on gathering credentials by cloning To sustain these complex operations, UNC5807 uses
sensitive virtual machines, such as Domain Controllers a specialized, purpose-built toolkit designed to bypass
and Privileged Access Management (PAM) systems. By the limitations of traditional security telemetry on
securing a cache of valid credentials, UNC6201 was able non-standard appliance platforms.
to blend in with legitimate activity, effectively hiding their
malicious actions as potential system administrator and

Special Report: Mandiant M-Trends 2026 67
While some actors focus on the hardware edge, a Telemetry Gaps
suspected Iranian cluster of cyber espionage activity,
While many organizations have invested in better
tracked by GTIG as UNC1549, exploits the boundaries
visibility into their environment through EDR telemetry
of organizational trust. Primarily targeting the global
and network logging, few have opted to retain that data
aerospace and defense sectors, UNC1549 uses highly
for long-term analysis. In many environments, logs that
targeted spear phishing lures to gain a foothold into
are either native on hosts or forwarded to SIEMs do not
environments. They frequently pivot through less
extend far enough back in time to scope initial access
well-defended third-party service providers, taking
if a multi-year compromise is identified in their environ-
advantage of established network connectivity to reach
ment. As an example, the average dwell time of a case
their intended targets. In one intrusion Mandiant
in which BRICKSTORM was deployed was 393 days,
investigated, UNC1549 authenticated to an instance
but many organizations only log data for 90 days due
within a customer’s Virtual Desktop Infrastructure (VDI)
to cost-saving measures. In some cases, organizations
using stolen credentials. The desktop instance UNC1549
opt to keep logs for 360 days but these would still be
targeted was originally provisioned to provide access
insufficient to scope the full activity of the average
to a third-party vendor. Once authenticated, the threat
BRICKSTORM campaign. In such instances, evidence likely
actors bypassed process launch policies configured
will not exist to determine the initial access vector, which
to limit the types of applications that could run on the
severely impacts the confidence an organization can have
instance. By bypassing the controls on the instance,
in remediation activity.
UNC1549 was able to pivot into the environment of their
intended target. EDR tooling acts as an enabler for security teams in the
ongoing defense of their environments, but EDR solutions
Lastly, Mandiant identified a suspected state-sponsored
present similar challenges with regards to deployment
threat actor using anti-forensics and in-memory
and retention. While EDR alerts are often retained for 180
persistence techniques to reduce the opportunities
days or more, real-time telemetry is typically limited to the
for detection related to their activities. During recent
7 to 30 day range. Long-term retention of telemetry data
investigations, the threat group demonstrated effective
within the EDR platform can be prohibitively expensive
anti-forensics techniques by using built-in tools to
and impact the responsiveness of the analysis platform in
remove evidence of their activity from system resources
ongoing monitoring. Filtered real-time telemetry produced
such as the Linux WTMP login records and entries in
by EDR solutions that is copied to long-term storage
the Audit system log files. The threat group also used
can provide a secondary high-fidelity source of data if
timestomping techniques to mask file system modification
a compromise that extends past the retention window is
timestamps of the files with which they interacted or
identified. By partnering with infrastructure and opera-
altered. To maintain a minimal on-disk footprint, the threat
tions groups, internal security teams can define a set of
actor frequently deleted malware binaries after execution,
event types that correspond to the most critical questions
allowing the process to run exclusively in volatile memory
raised during an investigation. Events that detail authen-
on systems that underwent infrequent reboot cycles.
tication behavior, process execution, internal access to
Limited EDR capabilities and restricted network logging
sensitive resources, and privilege escalation are a good
also contributed to the threat group’s ability to remain
starting point for collection. Including events such as
undetected for multiple years.
registry modification, service and scheduled task creation,
and command script details helps add additional context
Challenges and depth to the set of events forwarded to long-term
storage. Security teams can then assess the volume of
Investigations into threat actor activity with long dwell
data being collected as well as the frequency of individual
times often highlight several challenges to early detection
event types to identify potentially noisy feeds. Partnering
and efficient incident scoping. Gaps in network visibility
further with infrastructure and operations teams can help
and telemetry, asset management inefficiencies,
determine the bounds of expected events generated from
and limitations in data retention can all contribute to
those environments and create additional tuning rules for
the operational friction experienced by organizations
the filtered logs.
as they seek to identify and remediate a compromise
of their environment.

Special Report: Mandiant M-Trends 2026 68
An additional obstacle is the common lack of visibility into Asset Blind Spots
activity within the network. While most organizations place
Asset management is a fundamental aspect of a mature
a premium on visibility into external activity targeting the
cybersecurity program; however, it is frequently not
perimeter, many give the internal environment far less
implemented with the rigor needed to support complex
attention. The absence of inter-network traffic logging
investigations. During complex investigations, gaps in
or, alternatively, system authentication logging beyond
asset management are often quickly highlighted. These
Windows Domain Controller Security event logs, prevents
gaps most commonly manifest when network defenders
investigators from accurately mapping lateral movement
attempt to identify an asset associated with potential
between internal systems and network segments. This
malicious activity, only to find that no centralized source
problem is further compounded as threat groups learn to
of truth exists. The time and resources required to track
mask malicious behavior and blend into the environments
down the system in question injects significant friction
they compromise. Limited logging also hinders the ability
into the process. Even in cases where an organization has
to identify a threat actor’s specific targets and objectives.
retained sufficient log data to support the analysis, the
In one case that Mandiant investigated, a client’s logging
inability to pivot quickly from a finding to the identification
configuration resulted in all cloud-bound traffic from
and analysis of the system impacts the speed at which
a compromised on-premises segment appearing as
network defenders can respond to potential threats or
though it originated from a single egress IP. The lack
scope long-term compromises.
of visibility into the on-premises segment made it
impossible to isolate traffic from known compromised Gaps in an organization’s management and tracking of
hosts. Failing to log access to high-criticality systems their assets can occur for a variety of reasons. Appliances
or those that proxy connections on behalf of others such as network edge devices, routers, and hypervi-
can constitute a significant telemetry gap. sors are often excluded from asset management. These
specialized appliances frequently lack support for
Prioritizing the forwarding of logs to a centralized location
conventional monitoring and security tooling, which can
can help improve the retention of telemetry and secure
make them prime targets for sophisticated threat actors
them from anti-forensics activity. This also helps secure
seeking long-term covert access to an environment. This
the integrity of log sources against threat actors who
often results in diminished visibility into these assets for
seek to wipe or modify log sources on the hosts they
network defenders, which can compound other gaps in
compromise. Furthermore, logging repositories should
visibility when the assets are unknowingly excluded from
be configured to generate alerts if a source of logging
security and logging improvements.
is unexpectedly terminated. These alerts provide
operations teams the opportunity to correct logging Additionally, as organizations grow in size, the challenges
misconfigurations or, potentially, identify the intentional of asset management increase if a strict culture of
disabling of logs by a threat actor. While the duration organizational collaboration doesn’t exist. If individual
of logs stored is a critical metric, the scope of logging business units make decisions with respect to infrastruc-
sources should also be audited and, where possible, ture without the cooperation of the larger organization,
improved to cover frequently overlooked assets. Logs they can introduce systems that lack appropriate
from hypervisors, network edge devices, and routers, instrumentation and asset tracking. The ability to create
as well as authentication data for all Windows and an accounting of unmanaged systems in an environment
Linux servers in an environment, help reduce the areas during an investigation into suspicious behavior, or worse,
in which long-term intrusions can hide. Finally, logging while investigating a multi-year intrusion, is a costly
configurations should be audited periodically to and time consuming endeavor. A collaborative culture
ensure logs are not only being captured, but that the that demonstrates the value of interdependency between
appropriate level of detail is being provided. business units and security teams can help ensure
answers to critical questions are delivered in a timely
manner while also helping reduce visibility gaps.

Special Report: Mandiant M-Trends 2026 69
Organizations should regularly test the assumptions their
Recommendations
teams have of the environment to identify and validate
Much like any emergency, the worst possible time to
the data. During these audits, efforts to ensure complete
discover that your response preparedness is lacking
coverage of the environment should coincide with an
is during a live crisis. Maintaining the velocity of the
ongoing effort to identify and remove unused technology
response to a successful attack is crucial to a positive
and systems to reduce administrative burden and risk.
outcome and the recovery of the environment.
By working to overcome the limitations of standard
As investigators and security teams work to scope the
logging and EDR through a proactive review of total
intrusion and ultimately remove the attacker from the
available telemetry, identifying and closing gaps, and
environment, many of the assumptions which internal
maintaining appropriate detail in documentation,
teams have of their systems and workflows are tested
defenders can more efficiently and effectively respond to
and it is not uncommon to find gaps in knowledge,
incidents. Doing this prework enables defenders to move
instrumentation, and logging. Visibility gaps, security
beyond atomic IOC searches, which are less effective
instrumentation deployments, or even simple infrastruc-
against threat actors that proactively avoid techniques
ture documentation such as network diagrams can
susceptible to static detections. It allows them to focus on
slow an investigation dramatically as critical resources
more advanced analysis techniques like stack ranking data
are pulled from the response to find answers that the
to look for outliers and comparison of data against known
security teams require. A compromise in which threat
good systems. These techniques are much more effective
actor activity spans multiple years compounds these
in identifying sophisticated threat actor activity.
issues while also raising difficult questions. In lacking
adequate data to detail the scope of an intrusion and Organizations should also implement a routine of proac-
potential data theft, organizations risk a loss of trust tive threat hunting. Relying solely on reactive alerts
with customers during disclosure and can face scrutiny generated by conventional security tools is insufficient
relating to breach disclosure laws. Without the ability for detecting sophisticated, evasive threat actors.
to quantify data theft, organizations may find they are Proactive hunting serves to bridge this critical visibility
forced to assume the worst. gap and can significantly curtail the dwell time of an
adversary within the network. Since threat actors
While prevention of a compromise is an ideal outcome
frequently use legitimate, native administrative utilities
for any targeted attack, the preparation required to
to hide their actions in plain sight, detection hinges on
respond to the successful attacks requires long-term
the analyst’s ability to distinguish benign administrative
support and planning. User education which focuses
activity from an attacker’s malicious actions. Furthermore,
on turning users into assets that can help drive positive
integrating the latest threat intelligence into the hunting
security outcomes and open collaboration between
process allows organizations to focus on specific tech-
security teams and the business units they support
niques currently employed by adversaries. Ultimately,
provide the best foundation for building mature security
the systematic practice of proactive threat hunting not
programs. A collaborative effort to ensure the organiza-
only identifies existing breaches but also highlights and
tion has an appropriate accounting of and visibility into
enables the refinement or remediation of operational
the systems on which they rely also helps set the stage
deficiencies in the defense posture.
for active validation of the results.

Special Report: Mandiant M-Trends 2026 70
Adversary Focus on
Virtualized Infrastructure
In recent years, threat actors have increasingly targeted virtualized infrastructure to accomplish their objectives
in a targeted environment. Virtualization platforms often consist of three main components: a dedicated, centralized
management server to administer virtual machines, hypervisors to handle hardware allocation, and the virtual
machines themselves. Mandiant has identified threat actor activity targeting each of the three components of
virtualized infrastructure throughout the attacker lifecycle–from achieving initial access to stealing sensitive data.
Privilege Escalation
Weaponizing the
A critical advantage in attacking the hypervisor, which
Virtualization Stack
hosts a system of operational interest to the attacker
Evasion of Security Tooling instead of the system itself, is the ability to steal sensitive
data without directly interacting with the target system.
Modern defenses for the virtualization stack often rely
This tactic can often be deployed by a threat actor as
on Endpoint Detection and Response (EDR) solutions
part of their privilege escalation techniques once they’ve
designed to protect the guest operating systems on
gained access to the hypervisor. A common path for
which they are installed. The hypervisors themselves,
privilege escalation includes stealing the ntds.dit file,
however, may run specialized proprietary operating
which is the core database file for the Active Directory
systems that are incompatible with modern EDR
(AD) Domain Services. To accomplish this, threat actors
solutions. This creates a blind spot for security teams
compromise a Domain Controller, elevate their privi-
and a potential means through which threat actors can
leges, and often run additional tooling in order to steal
pursue their objectives while remaining undetected.
the ntds.dit file. During each of these operations, threat
Recent data substantiates this claim; Mandiant identified
actors create opportunities for detection especially as
several malware families capable of targeting virtual
the access to ntds.dit is a common indicator of attacker
infrastructure, including REDBIKE, commonly known as
activity supported by all modern EDR solutions. However,
“Akira” ransomware. In 2025, REDBIKE was the malware
in an attack where the domain controller is part of
family most frequently identified by Mandiant during
virtualized infrastructure, threat actors can simply target
ransomware investigations.
the virtualization storage layer directly. Using a technique
In some investigations, Mandiant identified evidence of commonly referred to as “Snapshot Mounting,” adver-
threat actors not only targeting virtualized infrastructure saries create a snapshot of a running Domain Controller,
but also creating new unmanaged virtual machines clone or mount that snapshot’s virtual disk (VMDK)
to support ongoing operations in the targeted environ- to a rogue virtual machine, and extract the ntds.dit file.
ment. These virtual machines existed outside of By targeting the virtualization storage layer, the EDR
the organization’s asset management and security on the guest operating system remains unaware of the
monitoring systems, which enabled the threat actor access to the underlying files. Similarly, the hypervisor’s
to conduct deeper staging operations without being management of physical resources such as memory
flagged by EDR or SIEM alerts. The existence of presents another avenue through which threat actors
unmanaged and unaccounted for virtual machines can escalate privileges. By targeting the individual virtual
can also result in severe delays when security teams memory files through a compromised hypervisor, threat
are attempting to investigate suspicious behavior. actors can transfer those files out of the environment,
The overhead in identifying an unknown system while where they are parsed by tools such as Mimikatz to
trying to triage potential attacker activity can impact the extract credentials.
velocity of the investigation or, worse, lead to dead ends
where high-confidence determinations cannot be made.

Special Report: Mandiant M-Trends 2026 71
Figure 3: Ransomware impact
While direct interaction with resources managed by
the hypervisor represents a high level of risk, threat
actors have also been found to rely on the same
Malicious Webshell
hypervisor management platforms and interfaces that Binary Upload
the organization uses for day-to-day operations.
In environments where the hypervisor and management
server are integrated with AD and domain-joined, threat
actors can exploit this trust relationship to achieve
unauthorized administrative control. Specifically, by Rogue Backdoored
VM VIBS
compromising a privileged AD account, an attacker
can create or manipulate the AD group responsible
for provisioning rights across the virtual infrastructure
to grant themselves full administrative access. Figure 3: Ransomware impact
Persistence Ransomware Impact
Adversaries frequently target the virtualization To combat the impacts of ransomware incidents,
platform to establish persistence within an environment organizations have developed comprehensive recovery
through access to the hypervisor’s shell. By executing plans and backup solutions. As such, more recent
commands directly within this environment, they can ransomware campaigns prioritize the destruction of
deploy persistence mechanisms that survive standard backups to eliminate recovery options and increase
remediations and system reboots. For instance, leverage during extortion demands. Many enterprise
Mandiant identified evidence to indicate attackers backup solutions offer plug-ins to virtualization manage-
exploited vulnerabilities to upload web-based backdoors, ment servers and virtual machine architecture to
effectively turning the web management interface facilitate easy restoration from backups. In two recent
itself into a persistent gateway for command execution. cases, Mandiant identified evidence that the threat
Others established persistence by registering malicious actor compromised the service accounts used for the
systemd services. Systemd is the default system and communications between the backup provider and the
service management interface for Linux distributions. virtualization platform. The threat actor then used the
Creating a malicious service ensured that the threat compromised service accounts to destroy backup and
actor’s backdoors automatically restart whenever the restoration resources, limiting the ability of the targeted
host reboots. organization to recover independently.
A more sophisticated example of targeting the hyper- Threat actors also prioritize stealthy ransomware
visor for persistence involved the use of an open-source deployment methods to avoid automated detection
machine emulator, QEMU, launched as a raw process and response from EDR tooling. Modern EDRs have the
on the hypervisor. In this example, the threat actor created capability to respond in real time to detect, quarantine,
an unmanaged VM and installed command and control and block the execution of ransomware binaries them-
frameworks alongside tunneling utilities to create a secure selves or the actions commonly employed by ransomware
backdoor. Because this VM was running on the hypervisor threat actors. The virtualization stack, however, presents
instead of being run by the hypervisor, the virtual instance threat actors with the opportunity to deploy ransom-
failed to show up on listings of guest instances. This ware at the hypervisor level. Rather than deploying an
allowed the VM to not only avoid detection through EDR encryptor to individual virtual machines that are more
solutions and scanning, but also obscure the origin point likely to have EDR tooling installed, the threat actor can
of the instance itself. encrypt the datastore files, such as .VMDKs and .VMEMs,
stored on the hypervisor. Encrypting these datastore files
on the hypervisor renders any associated virtual machine
inoperable and unrecoverable without decryption or an
unaffected backup. In 2025, Mandiant identified evidence

Special Report: Mandiant M-Trends 2026 72
of threat actors deploying and executing custom malware  The Data Plane
such as FOULFOG.LINUX or INC.LINUX on compromised
While management logs offer a high-level narrative,
hypervisors. Mandiant’s analysis of recovered malware
samples revealed that on execution, these binaries shut  hypervisor-level logging captures the granular
execution of the kernel and the physical state of the
down the virtual machines running on the hypervisor
and explicitly targeted virtual machine datastore files   underlying hardware. This provides a distinct telemetry
source for monitoring direct host shell access and
for encryption.
low-level networking events to address critical visibility
gaps in detection and response workflows.
Logging Guidance
Virtualization platform logs can provide high-quality
|     |     |     | HHoosstt  AAuutthheennttiiccaattiioonn     | PPrriivviilleeggee  aanndd     | NNeettwwoorrkk  aanndd     |
| --- | --- | --- | ------------------------------------------ | ------------------------------ | -------------------------- |
detailed data regarding the operations and use of
|     |     |     | aanndd  AAcccceessss | IInntteeggrriittyy  MMoonniittoorriinngg | IIssoollaattiioonn  VViioollaattiioonnss |
| --- | --- | --- | -------------------- | ---------------------------------------- | ---------------------------------------- |
the virtualization tools in an environment. Unfortunately,
|     |     |     | SSH Remote Access:   | Privilege Escalation:   | Promiscuous Mode:  |
| --- | --- | --- | -------------------- | ----------------------- | ------------------ |
Mandiant has found that these logs are often excluded  Logs capturing remote  Logs recording the use    Logs indicating a VM’s
from enterprise logging solutions. By forwarding   logins via SSH to the  of su (substitute user)   vNIC was set to
|     |     |     | hypervisor. | or sudo commands within  | “Promiscuous Mode”  |
| --- | --- | --- | ----------- | ------------------------ | ------------------- |
virtualization platform logs to a centralized location,   the host shell to elevate  allowing it to sniff all traffic
|     |     |     |     | permissions from a   | on the virtual switch. |
| --- | --- | --- | --- | -------------------- | ---------------------- |
such as a SIEM, security teams significantly enhance
standard user to root.
their ability to identify and alert on malicious activity
that targets the management server and hypervisors.   Direct Console/Shell  Unsigned Package/  MAC Address
|     |     |     | Access: Logs showing   | Module Loading:   | Impersonation:   |
| --- | --- | --- | ---------------------- | ----------------- | ---------------- |
This can help close the gap in visibility into threat actor
|     |     |     | interaction with the   | Alerts when an   | Logs detecting a VM  |
| --- | --- | --- | ---------------------- | ---------------- | -------------------- |
activity occurring outside the standard guest   physical TTY, KVM, or   administrator attempts to  attempting to send traffic
|     |     |     | Direct Console User  | force-install an unsigned  | using a Source MAC  |
| --- | --- | --- | -------------------- | -------------------------- | ------------------- |
OS monitoring. Interface (DCUI). driver, kernel module,   address different from
|     |     |     |     | or VIB (vSphere Installation  | its assigned one. |
| --- | --- | --- | --- | ----------------------------- | ----------------- |
Bundle), which can
| The Control Plane |     |     |     | be a vector for rootkits   |     |
| ----------------- | --- | --- | --- | -------------------------- | --- |
or malware.
Management server-level logs can provide a high-level
|     |     |     | Direct Web/API Access:  | Host Configuration  | Host Firewall Modification:  |
| --- | --- | --- | ----------------------- | ------------------- | ---------------------------- |
narrative of attacks targeting the platform by recording  Logs capturing the Web/ Tampering: Logs capturing  Changes to the
|     |     |     | API authentication directly  | manual edits to critical  | hypervisor’s local firewall  |
| --- | --- | --- | ---------------------------- | ------------------------- | ---------------------------- |
identity-driven events, such as logins, task initiations,
|     |     |     | to the hypervisor. | system configuration   | rules (e.g., opening   |
| --- | --- | --- | ------------------ | ---------------------- | ---------------------- |
and permission changes. These platforms typically utilize  files (e.g., /etc/passwd, esx. unexpected ports like
|     |     |     |     | conf) performed   | HTTP or Telnet) to expose   |
| --- | --- | --- | --- | ----------------- | --------------------------- |
a dedicated application-layer log source, distinct from
|     |     |     |     | via the command line. | the management interface  |
| --- | --- | --- | --- | --------------------- | ------------------------- |
to the open internet.
the underlying operating system, to track user actions,
permission changes, and authentication events.
Proactive Security Recommendations
| AAuutthheennttiiccaattiioonn     | VVMM  LLiiffeeccyyccllee  aanndd     | CCoonnffiigguurraattiioonn  aanndd   |     |     |     |
| -------------------------------- | ------------------------------------ | ------------------------------------ | --- | --- | --- |
The security of an organization’s virtualization platform
| aanndd  AAuutthhoorriizzaattiioonn   | SSttaattee  CChhaannggeess | IInnvveennttoorryy  CChhaannggeess |     |     |     |
| ------------------------------------ | -------------------------- | ---------------------------------- | --- | --- | --- |
defines the security of every VM it supports. When
| Logon/Logoff Events:  | Power Operations:   | Hardware Reconfiguration:   |     |     |     |
| --------------------- | ------------------- | --------------------------- | --- | --- | --- |
Track high-level login  Power On, Power Off,   Adding/removing vCPUs,  hosting Tier-0 services like Active Directory or Secrets
| successful authentication  | Reset, and Suspend   | changing RAM allocation,  |     |     |     |
| -------------------------- | -------------------- | ------------------------- | --- | --- | --- |
and failures. operational logs. or expanding virtual disks. Management, the underlying virtualization environ-
ment must be hardened as a Tier-0 asset. Without strict
Role/Permission Changes:  Snapshot Activity:  Network Changes:  isolation and equivalent protection levels, these critical
| Logs indicating that  | Creation, deletion,   | Modifications to virtual  |     |     |     |
| --------------------- | --------------------- | ------------------------- | --- | --- | --- |
systems are only as secure as the management plane
| a user was granted  | and consolidation   | switches, port groups,   |     |     |     |
| ------------------- | ------------------- | ------------------------ | --- | --- | --- |
| "Administrator"     | of snapshots.       | or VLAN tagging.         |     |     |     |
on which they run.
privileges or added
to a sensitive group.
API Access: If you use  VM Creation/Deletion:   Storage Changes:  Identity Modernization
| automation (Terraform,  | Logs capturing the   | Mounting or unmounting  |     |     |     |
| ----------------------- | -------------------- | ----------------------- | --- | --- | --- |
| Ansible), log the       | deployment of new    | datastores/LUNs.        |     |     |     |
Configuring hypervisors as domain-joined hosts
| authentication of service  | or removal of VMs. |     |     |     |     |
| -------------------------- | ------------------ | --- | --- | --- | --- |
accounts accessing   can present inherent risks to an environment. Where
the API.
possible, organizations should review the practicality
Web Request Logs:   Migrations:   Host Operations:   of removing hypervisors from their domain to prevent
| These logs trace   | Logs showing VMs   | Putting a host into  |     |     |     |
| ------------------ | ------------------ | -------------------- | --- | --- | --- |
incoming web requests,  moving between hosts. “Maintenance Mode”   threat actors from using a compromised domain to
| including the source IP  |     | or adding/removing   |     |     |     |
| ------------------------ | --- | -------------------- | --- | --- | --- |
gain administrative control over a virtualization platform.
| address connecting to   |     | a host from a cluster. |     |     |     |
| ----------------------- | --- | ---------------------- | --- | --- | --- |
the web client. Phishing-resistant Multi-Factor Authentication (MFA)

Special Report: Mandiant M-Trends 2026 73
such as FIDO2 for all hypervisor logins and privileged access to the hypervisor should only be granted through
accounts can reduce the threat of credential theft and a monitored “Break Glass” procedure for emergency
lateral movement. troubleshooting. Infrastructure teams should partner
with their security teams to ensure that high-priority
Organizations can further reduce their attack surface
detections exist for the specific break glass procedures
by deploying a dedicated Infrastructure-Only Identity
they use.
Provider (IdP) or a hardened Privileged Access
Management (PAM) solution. A dedicated IdP ensures Finally, protecting the most critical workloads requires the
that infrastructure administrative accounts exist in implementation of VM-level encryption for Tier-0 assets
a separate, restricted directory that is entirely such as Domain Controllers. Encrypting these virtual
independent of the corporate domain. Alternatively, machines can prevent threat actors from stealing virtual
a PAM-centric approach can provide strong controls disks to steal sensitive data.
such as enforcing Just-in-Time (JIT) access. This
ensures that administrative privileges are granted Backup Protection
only on a temporary and as-needed basis, which helps
Threat actors frequently prioritize the destruction of
reduce the availability of persistent high-level access
recovery infrastructure to eliminate an organization’s
threat actors seek to exploit for long-term presence
ability to restore systems. To counter this, backup
in the environment.
environments should be decoupled from the production
virtualization environment and isolated from corporate
Stack Hardening
identity stores. Integrating these platforms with the
Mandiant has identified threat actors targeting corporate Active Directory environment introduces a risk
virtualization platforms to achieve persistence and where an adversary can leverage a single compromised
large-scale data destruction. Enforcing strict security credential to delete both production and recovery data.
controls through validated baselines is essential to Organizations should apply the same identity standards
disrupt these objectives. A defense-in-depth strategy to backup infrastructure as they do to the virtualization
that seeks to align virtual platform configurations with platform, including phishing-resistant MFA and dedicated,
the official configuration and hardening guidance from non-AD integrated identity sources.
the vendor can help provide a known security baseline
Resilience against data destruction requires immutable
for virtualization platforms.
storage, such as Write-Once-Read-Many technology,
A strong hardening posture begins with the hardware to ensure backup repositories cannot be modified or
root of trust by activating UEFI Secure Boot and enabling encrypted by privileged accounts. Maintaining offsite
the execInstalledOnly setting in conjunction with a and air-gapped copies of backup resources can provide
supported TPM 2.0 chip. Secure Boot enforces kernel- a definitive barrier against network-based attacks.
level signature verification for all binaries while the TPM While this separation can introduce operational
provides hardware-backed integrity checking of the complexity, organizations should implement regular
boot process. This combination can prevent a threat restoration testing from these isolated environments
actor from maintaining persistence through the addition to verify that backups will function as intended during
of malicious installation bundles specific to the virtualiza- a high-pressure recovery event.
tion product or unauthorized drivers that would otherwise
compromise the integrity of the hypervisor.
Going beyond host-based security controls, organizations
should isolate the management plane to help prevent
lateral movement from the general corporate environ-
ment. This can be achieved by restricting virtualization
platform management traffic to a dedicated and
firewalled network segment only accessible through
hardened Privileged Access Workstations (PAW).
To further minimize the attack surface, management
shells and remote access protocols such as SSH should
be disabled by default across all hosts. Direct remote

Special Report: Mandiant M-Trends 2026 74
The Cascading Impact of
Third-Party SaaS Compromises
The modern enterprise security landscape has shifted from the traditional network perimeter to a complex ecosystem of
interconnected infrastructure and Software as a Service (SaaS) platforms. These integrated platforms play a vital role in
identity management, workforce collaboration, and streamlining internal processes, among other applications. However,
the interconnectedness of SaaS platforms with enterprise cloud infrastructure has introduced the risk of threat actors
targeting identities used by SaaS integrations as a means to pivot into other parts of the environment. These incidents
often occur through a combination of the exploitation of third-party integrations, over-permissive identities, and miscon-
figurations. Because of the deeply integrated nature of cloud and SaaS, a compromise on a single SaaS application can
allow threat actors to move laterally into other areas of the environment with ease. In these scenarios, the failure of a
singular trusted component triggers a chain reaction across the entire enterprise. As organizations accelerate towards
cloud-first infrastructure, oversights such as unmonitored OAuth grants and broad API permissions increase the risk of
a single compromised token causing a materially significant incident.
In 2025, a strategic shift emerged as threat actors bypassed traditional defenses like firewalls and multi-factor authenti-
cation (MFA) by abusing Non-Human Identities (NHIs) and stolen secrets such as OAuth and refresh tokens. By targeting
vendor platforms that act as a centralized “source of truth” for identity integrations, adversaries can harvest legitimate,
pre-authorized tokens to compromise downstream environments. This effectively transforms a single-vendor breach into
a large-scale supply chain attack, where the stolen tokens act as reusable keys to the customers’ sensitive data stores.
Observed Threat Actors and Trends in 2025
Lateral Movement
Throughout 2025, attackers exploited systemic
Across Boundaries
weaknesses in how organizations manage SaaS inter-
One form of SaaS integration compromise that Mandiant
connectivity and permissions for initial access. A primary
encountered in 2025 involved threat actors compromising
driver of this was OAuth token compromise as some threat
code repositories by gaining access to Personal Access
groups prioritized the theft of session cookies and refresh
Tokens. The threat actors then used automated scanning
tokens over brute-forcing passwords. Because these
tools to search the code repositories for hardcoded
tokens often remain valid post-logout, attackers can
integration tokens. This process often begins with
hijack sessions immediately without triggering MFA alerts.
a compromise on a SaaS developer’s workstation or
This risk is compounded by widespread SaaS misconfigu-
Source Code Management (SCM) account. Long-lived
rations, specifically those related to identities and secret
tokens found on the workstation or in the SCM account
management. Mandiant identified instances in which
could allow the threat actor to pivot to the production
integrations that required only minimal access were
cloud infrastructure. In some instances, access to cloud
provisioned API keys with broad privileges. For example,
infrastructure could reveal OAuth refresh tokens for
an integration intended only for log reading could be
customer integrations, turning a single compromised
misconfigured with rights such as the ability to edit
repository into a potential supply chain event.
or delete storage buckets. Another common finding
included the existence of API keys with wildcard permis-
sions. Due to the prevalence and potential impact of
these vulnerabilities, some threat actors have started
to focus on stealing NHIs for third-party integrations
from SaaS vendors. In 2025, Mandiant identified evidence
of threat actors using NHIs, which were stolen during
previous engagements.

Special Report: Mandiant M-Trends 2026 75
The Push: The Fall: The Impact:
SCM Compromise Lateral Movement via NHIs Production & Supply
Chain Compromise
Cloud Provider Keys
Secret Data
Attacker Developer Scanning Tool Theft
Workstation
Cloud
Environment
Hardcoded Data Warehouse
Secrets Tokens
Found
Persistent
Access
Code Repository
(SCM) OAuth Refresh
Tokens
Personal Access Over-provisioned Potential
Token (PAT) API Keys Supply Chain
Event
Figure 4: The SaaS Domino Effect Attack Chain
Mandiant has identified distinct threat clusters driving automated scanners on the exported data. Their goal
this shift, most commonly financially motivated actors. was to locate hardcoded keys, tokens, and Personal
On the human-centric side of the spectrum, groups Access Tokens, which could be used for further down-
such as the financially motivated threat cluster stream compromise. UNC6564, a financially motivated
UNC3944 prioritize aggressive social engineering over cluster, exemplified “Living off the Cloud” tactics, in which
technical exploitation for initial access. These actors attackers rely on native cloud infrastructure and tools.
frequently target IT help desks, utilizing voice-based This group operated from dedicated cloud infrastructure
phishing (vishing) to impersonate employees and to blend in with legitimate traffic and abused previously
convince support staff to bypass MFA or enroll compromised application tokens to gain access to target
attacker-controlled devices. In some cases, following environments, then stole sensitive data.
the compromise of a user account in a SaaS platform
through similar human-centric techniques to those Prevention
used by UNC3944, threat actors performed credential
Preventing a third-party SaaS application compromise
mining in the target environments for highly privileged
from becoming a materially significant event involves
keys that would allow them to compromise further
a defense-in-depth approach similar to a traditional
downstream customer environments.
enterprise environment, but with specific considerations
Groups like UNC6395 and UNC6564 demonstrated due to the nature of SaaS applications. There are
a focus on identity and SaaS integrations in 2025. two threat profiles to keep in mind when designing
UNC6395, a threat group Google Threat Intelligence prevention strategies for SaaS: third-party compromise,
Group (GTIG) began tracking in 2025, compromised which can include supply chain attacks, and the compro-
a SaaS vendor and obtained a large number of SaaS mise of internal human and non-human identities linked
integration tokens, which they used to perform mass to SaaS applications. The methods for both remediating
data exports from downstream organizations with and proactively preventing SaaS compromise from either
native command-line interfaces. They then ran threat profile are similar. Security controls need to
shift from static network blocking to dynamic identity

Special Report: Mandiant M-Trends 2026 76
verification with identity being the common denominator and automated posture checks are crucial. Finally,
among most SaaS attacks. A proactive prevention organizations should inventory and assess the logging
strategy incorporating these elements should be built and monitoring capabilities of each SaaS application,
on four pillars: knowing the environment, strategy and identify gaps in telemetry, and ensure critical
policy, identity and access management hardening, and logs are being ingested into a centralized security
continuous lifecycle management and detection. monitoring platform.
Strategy and Policy
Environment Inventory and Controls
Effective SaaS security management begins with A strong governance framework is essential to manage
comprehensive visibility and an understanding of the the risks associated with SaaS adoption and integration.
interconnected application landscape. A fundamental This begins with a robust Third-Party Risk Management
step is to maintain a complete inventory of all SaaS program to vet SaaS vendors before onboarding and
applications used across the enterprise. This inventory on an ongoing basis. Key evaluation criteria include the
should go beyond just listing applications; it must vendor’s security certifications, data handling practices,
include business owners, the types of data processed support for Single Sign-On, granular audit logging, and
or stored, and all integration points. Organizations secure development practices. Organizations should
often overlook SaaS applications in traditional asset mandate necessary security features, which are often
management, creating significant visibility gaps. not standard, as part of the procurement process.
Additionally, organizations must understand how data
Clear policies must also be established and enforced.
flows between integrated systems in order to identify
Enforcing a policy requiring all SaaS applications
high-risk pathways and data aggregation points, and
to be integrated with the corporate Identity Provider
to implement Data Loss Prevention (DLP) controls
(IdP) using secure federation protocols centralizes
where sensitive data may be leaving the administrative
identity management and reduces reliance on
boundaries of the environment.
application-specific credentials. Policies for the secure
Furthermore, proactive secret discovery and manage- storage, rotation, and access control of all secrets
ment are essential. This involves inventorying all secrets, should mandate the use of approved secrets
including API keys, OAuth tokens, and service account management solutions and prohibit the use of
credentials used for SaaS integrations. It is critical hardcoded secrets. Organizations can create a clear
to identify where these secrets are stored, their dates hierarchy of acceptable use policies, security policies,
of expiration, and who has access. Automated tools standards, and procedures that explicitly address
can scan code repositories, configuration files, and SaaS security, covering data handling, identity and
cloud environments for hardcoded or insecurely stored access management, incident response, and vendor
secrets. To help prevent unintentional inclusion of management. Lastly, it is critical to maintain a risk
credentials in private or public code repositories, register to document and track known risks associated
pre-commit hooks can be configured to identify strings with SaaS applications, integrations, and vendors,
that match common formats and halt commits to a reviewing and prioritizing risks for remediation regularly.
repository. Enforcing pre-commit hooks on every
Strong policies governing end-user permissions and
repository, even those intended for personal use, helps
capabilities are also a critical component of SaaS
reduce the risk of unintentional credential exposure.
security. Administrators can disable the ability for end
To aid in managing this complex environment, organiza- users to consent to unverified third-party applica-
tions can deploy Cloud Access Security Brokers for tions, ensuring that only vetted applications can obtain
visibility and control over SaaS application usage, and persistent tokens and effectively blocking the path for
SaaS Security Posture Management tools to assess malicious OAuth applications to be granted those tokens.
and remediate misconfigurations continuously across the
SaaS estate. Given the diverse configuration options of
each SaaS application, centralized management

Special Report: Mandiant M-Trends 2026 77
Identity and Access Management Hardening web monitoring to identify when specific corporate
credentials or session tokens are being sold or shared
Given that identity is part of the new perimeter, hard-
as an early warning to trigger immediate rotation.
ening identity and access controls is paramount.
By implementing multi-layered prevention strategies,
Enforcing the principle of least privilege for all integra-
organizations can significantly reduce the risk of a single
tions can help preclude over-provisioned API keys and
point of failure within their SaaS ecosystem.
OAuth tokens. This includes avoiding wildcard permis-
sions and granting only the specific scopes required for
Outlook
the integration to function, as well as assigning unique
identities and credentials for each integration to limit the Organizations are no longer defending a static fortress;
potential impact of a compromise of a single integration. instead, they are securing an interconnected web of trust
Where possible, transitioning from static API keys relationships where the perimeter is defined not just
and long-lived tokens to OpenID Connect (OIDC) by firewalls, but also by the entire identity and access
federation for integrations between SaaS platforms management layer. To adapt to this shift, organizations
and the IdP reduces the attack surface associated must move beyond the assumption that any authenticated
with stolen secrets. To minimize standing privileges for human user, service account, or third-party integration
both human and non-human identities, organizations is inherently safe. Strategies for securing these assets
can implement Just-in-Time access mechanisms, must change from static prevention to continuous
granting elevated or sensitive permissions only for verification. This requires a cultural shift towards
the duration needed to complete a specific task. an architecture that forces IT teams to treat identity
Sender-constrained tokens can mitigate token theft verification as a frontline defense. By recognizing that
and replay attacks through mechanisms like a risk accepted in a third-party application deployed
Demonstrated Proof-of-Possession or enforcing into an interconnected environment is also a risk in the
device compliance and context-aware access policies, production core, organizations reframe their view of
ensuring tokens are only valid from trusted devices identity and access controls. Enforcing policies that
and locations. align to the principle of least privilege, and adopting a
“Never Trust, Always Verify” mindset allows organizations
Continuous Lifecycle Management to get ahead of threat actors that target third-party
SaaS integrations and turn potential systemic failure into
and Detection
a contained, manageable event.
SaaS security is not a one-time setup; it requires
continuous monitoring, maintenance, and adaptation.
Organizations can implement automated processes for
rotating all secrets, including API keys, OAuth refresh
tokens, and service account credentials. Enforcing
short lifespans for access tokens and browser sessions
minimizes the window of opportunity for attackers
leveraging stolen cookies or tokens; this is particularly
critical as infostealer logs and active session cookies are
traded on underground markets, where the value of a
credential drops significantly the moment it expires or
is rotated. Administrators can conduct periodic access
reviews and recertification campaigns for both human
and non-human identities to ensure permissions are
still required and appropriate, automatically revoking
unused permissions after a defined period. Similarly,
implementing audit processes to detect and disable
dormant user accounts as well as unused integrations
helps reduce the attack surface available to threat
actors. Organizations can also integrate targeted dark

Special Report: Mandiant M-Trends 2026 78
Systematic Exploitation of
Edge and Core Network Devices
Over the past several years, Mandiant has seen an increase of malicious actors targeting edge and core network
devices. Attackers have taken advantage of the fact that many of these devices are not able to run enterprise security
tooling that provides increased visibility into threat actor actions and can interdict and prevent malicious activity.
At the same time, Google Threat Intelligence Group (GTIG) has observed that the mean time to exploit (TTE) for
vulnerabilities has continually decreased from 63 days in 2018 to -1 day in 2024 and further downward to an estimated
-7 days in 2025. A negative number indicates that exploitation of a vulnerability, on average, occurred before a patch
was released. This trend is compounded by threat actors’ evolving interest in security appliances and networking
infrastructure. Because these assets provide critical inspection of data ingress and egress points, they grant significant
visibility and permissions to those who gain access to them. Additionally, they often show signs of extended uptime
periods, delays in patching, and can often be excluded from vulnerability management altogether. This has allowed
threat actors the opportunity to exploit n-day vulnerabilities in these devices repeatedly without needing to identify
novel vulnerabilities.
Attackers have long used edge devices as a launch point decrease. Investigating attacker activity performed
into targeted environments. Historically, systems with on these devices presents a significant challenge for
traditional operating systems such as Windows, Linux, security teams. A lack of asset inventories and
and macOS have been the primary operating space sub-standard telemetry originating from the devices
attackers have used to complete their mission themselves results in added difficulty when security
objectives. However, in recent years, Mandiant has teams attempt to assess evidence of compromise.
observed attackers shift tactics, increasingly performing Edge and core network devices are designed to have
more phases of the attack lifecycle from edge and core minimal operating systems to maximize computing
network devices. Many of these devices offer built-in power. As a result, traditional file system forensics,
administrative functionality. Threat actors have leveraged log analysis, and memory forensics can be limited, as
this capability in a number of ways, including to facilitate onboard storage for these devices is typically limited
long term access, perform reconnaissance, move laterally to storing configuration files and required binaries.
through an environment, escalate privileges, and perform All of these limitations compound so that when security
data collection. Mandiant has identified threat actors, teams do identify suspicious activity on these assets,
in some cases, pivot to collecting the data that traverses there are often limited forensic artifacts to confirm
management planes or resides on core network devices an attacker’s presence or that a vulnerability was
themselves, as opposed to obtaining it from traditional successfully exploited.
sources such as workstations, servers or databases.
In 2025, Mandiant investigated a diverse group of
This method of data collection has allowed these actors
attackers targeting edge devices. The espionage actor,
to further avoid security monitoring and remain
UNC5807, used their access to core network devices
undetected for long periods of time.
to collect data for intelligence purposes. Another
While the exploitation of edge devices and core network intelligence-focused actor, UNC5221, repeatedly
devices is not a new phenomenon, the abuse of these targeted edge devices, demonstrating an extensive
devices has steadily increased as the TTE continues to knowledge of security appliances and using both
zero-day and n-day flaws in order to maintain long-term
stealthy access to organizations.

Special Report: Mandiant M-Trends 2026 79
UNC5807 relied heavily on application subshells built
Real-World Examples
into the platforms they compromised. These subshells
UNC5807 exposed features that are commonly restricted for
normal users but which enhanced the visibility and reach
The feature set of many core and edge network
UNC5807 had into the targeted environment. In order to
appliances has grown beyond relatively simple packet
maintain long-term multi-layered access to compromised
routing and switching devices. As the tools have grown
assets, the threat group created local admin accounts
in complexity, that same complexity has often come
on the appliances and enabled services such as SSH on
at the cost of security instrumentation, high friction,
non-standard ports.
and costly logging infrastructure. Threat actors have
started to target this gap between feature sets The relatively long uptime common to core and edge
and a lagging security posture by targeting these network appliances provided long-term stability for
platforms as a primary aspect of their campaigns UNC5807’s persistence, as well as for data collection
within an environment. activities. UNC5807 used the packet-capturing function-
ality built into the platforms to collect copies of live traffic
UNC5807, a sophisticated PRC-nexus espionage
that transited the devices. By analyzing the captured
operator, has been observed targeting the
data, UNC5807 identified passwords from cleartext
telecommunications sector. UNC5807’s activity is
network protocols and, using the various functions built
generally consistent with the threat actor discussed
into the subshell, leveraged those credentials to move
in public reporting as “Salt Typhoon”. In multiple
through the network. Once the threat actors identified
instances, UNC5807’s objectives appeared to
a system through which sensitive data was transmitted,
align with the collection of highly sensitive data
they used device-native utilities to capture live traffic.
for intelligence-gathering purposes. Mandiant
This data was staged on systems which supported
identified evidence that the threat group targeted
common file transfer protocols and was subsequently
internet-accessible network infrastructure within
moved to devices in the edge network where traffic
a variety of organizations and relied primarily on the
and security monitoring were less comprehensive.
feature sets inherent to those platforms to scope
Once staged in the edge network, UNC5807 uploaded
the environment before moving deeper into the network.
the data to threat actor-controlled infrastructure.
As they moved through the environment, UNC5807
followed a demonstrable playbook in which high-impact UNC5807’s successes in compromising and using edge
actions were limited to areas of the environment least and core network appliances highlight the need for a
likely to raise alarm. comprehensive threat model that can be applied to
common user devices and relatively obscure corporate
infrastructure devices alike. The ability to launch tooling
that provides admin-level capabilities on systems which
are rarely patched and power cycled—much less actively
monitored for access—represents an enticing feature
Figure 5: UNC5807 Attack Flow set for threat actors.
Enabling sub-shell
Internal environments
Enumerated
reconnaissance Escalated privileges, on core Performed
environments to
via built in by performing network devices. packet captures,
Access of internet identify systems
commands packet captures Within these collecting
exposed network where key network
and copying on network traffic environments, traffic with
devices traffic transited
configuration carrying plain configured SSH intelligence
and laterally moved
files from text credentials on non-standard value
to those systems
Network devices ports in order to
maintain presence
Figure 5: UNC5807 Attack Flow

Special Report: Mandiant M-Trends 2026 80
UNC5221 management systems, as well as analyzing administrative
history log files and internal documentation repositories
UNC5221 is an advanced PRC-nexus espionage actor
for plaintext credentials. In one case, UNC5221 accessed
and has been observed targeting a range of different
a backup infrastructure device where they exported
industries. While UNC5221 has been used synonymously
a privileged authentication management system backup
with the threat actor publicly reported as “Silk Typhoon,”
and uploaded it to a cloud-based storage service.
GTIG does not currently consider the two clusters to
The threat actors were able to analyze the backup and
be the same. UNC5221’s operations are characterized
gain access to privileged credentials outside of the
by the use of custom malware toolsets designed for
targeted environment.
stealth and persistence. In 2025, UNC5221 demonstrated
a relentless focus on edge devices by exploiting two To solidify long-term access, UNC5221 moved laterally
unique zero-day vulnerabilities in the same VPN product into the virtualization and management layers of the
during a three-month period. This campaign highlights network where they compromised virtualization
a strategic drive to maintain access to these critical infrastructure and support management appliances.
gateways despite vendor remediation efforts. Upon These systems provided a privileged vantage point for
gaining access to a targeted environment, UNC5221 internal reconnaissance, allowing the actor to map
prioritized stealth and evasion, deploying specialized virtual machines and scan the network topology.
malware such as TRAILBLAZE and BRUSHFIRE directly To maintain command and control (C2) without raising
to the appliance. TRAILBLAZE is an in-memory only alarms, the group deployed lightweight backdoors which
dropper that injects a hook into the web process. tunneled communications over HTTPS through legitimate
BRUSHFIRE is a passive backdoor that acts as an third-party services. By using trusted external platforms
SSL_read hook. It first executes the original SSL_read for C2 traffic, UNC5221 was able to bypass standard
function and checks to see if the returned data begins network security filtering while maintaining persistent
with a specific string. If the data begins with the defined control over the compromised infrastructure devices.
marker string, it will XOR decrypt then execute shellcode
contained in the data. Consistent with their previous UNC5221 has demonstrated a pattern of maintaining
campaigns targeting VPN edge devices, UNC5221 relied long-term stealthy access to environments by targeting
on non-persistent tactics and aggressive on-disk cleanup the visibility gap. By focusing their efforts on devices
to remove evidence of exploitation and minimize the risk that do not support traditional endpoint detection and
of discovery. response (EDR) tools, as well as avoiding actions that
are likely to raise alarms, UNC5221 dramatically reduced
Using the pivot point provided by the compromised the opportunities in which defenders could identify
VPN edge devices, UNC5221 utilized legitimate their activity. UNC5221’s success in maintaining long-
credentials harvested from the appliance’s own term access using these methods emphasizes the need
configuration files to authenticate to the VPN service for organizations to improve visibility and logging for
and move laterally through the environment. The group non-traditional assets, as these devices are increasingly
followed a methodical approach to privilege escalation, becoming attractive targets for threat actors.
including targeting backup and infrastructure
Figure 6: UNC5221 Attack Flow
Attacker exploited Attacker
Attacker laterally Attacker continued
an edge security Attacker harvested performed extensive
moved to backup to perform
appliance to gain credentials from reconnaissance
and virtualization reconnaissance and
initial access to the exploited device and privilege
infrastructure privilege escalation
the environment and connected to escalation, searching
devices and in order to maintain
and deployed the VPN appliance for plaintext
deployed C2 malware long-term access
custom malware with stolen credentials credentials across
for persistence to the environment
to the appliance the environment
Figure 6: UNC5221 Attack Flow

Special Report: Mandiant M-Trends 2026 81
Hardening, Visibility Organizations should also commit to regularly testing
and updating these response playbooks through tabletop
The challenge of detecting threats originating from edge
exercises. Additionally, it is prudent to understand, before
and core network devices primarily stems from three
an incident, precisely how and what forensic collections
factors: limited visibility, inadequate documentation,
could be taken from network devices. Given that network
and strict business continuity requirements. The general
devices are rarely altered or updated due to business
lack of visibility into actions performed on or from
criticality, the collection process requires robust planning
networking devices, beyond standard traffic logging,
to ensure business continuity. This pre-incident
represents a significant friction point for successful
planning should define whether external support,
detection and response efforts. Common enterprise
such as a vendor, is required, and what the potential
logging configurations provide a foundational security
limitations of the forensic collections supported mean
and business continuity layer. However, by focusing on
for analysis. During collection, preserving the integrity
user activity on endpoints as the primary sources of
of evidence is paramount; forensic artifacts may be
data to forward to a centralized location, security teams
lost if a system is powered off. Organizations should
frequently exclude critical log sources from core and
establish documented procedures for creating, storing,
edge network devices. The large volume of this data
and transferring forensic images, including retaining
relative to its perceived security value also makes it
the cryptographic hash for validation and meticulously
difficult for analysts to sift through and identify threat
recording all actions taken to maintain chain of custody.
actor activity. Typically, log data for network devices
is focused around the Network, Transport and Session Due to common delays in patching and power cycling
layers. Application logging, such as accounting logs, of edge and core network devices, the processes often
are usually stored locally, if at all. However, these require more robust planning to ensure the network can
logs are among the strongest data sets available for either continue to function or prepare for downtime.
a security team to identify anomalies during an Additionally, vulnerability management is essential not
investigation into possible network device abuse. only for identifying immediate risks but also for serving as
a secondary check for asset management by discovering
A successful logging strategy should balance resource
uncatalogued systems. Program success is dependent on
efficiency with the preservation of critical evidence.
timely remediation. Clearly defined oversight mechanisms
This relies on two main pillars: aligning logging objectives
and ownership for mitigation ensure accountability, as
with the organization’s specific threat model, and
unaddressed vulnerabilities remain a primary target for
integrating logging as a core requirement within the
unauthorized access. To enhance vulnerability manage-
system development lifecycle for all new and acquired
ment processes, organizations should leverage their
systems. Logging requirements should be reviewed
existing vulnerability management solution to conduct
regularly to ensure alignment with organizational goals;
comprehensive network discovery scans that include
retention times should be adjusted against the
fingerprinting publicly available devices and IP address
Mean Time to Detect to enable shorter and more
space from unauthenticated sources. While exploiting
cost-effective retention periods. In general, Mandiant
zero-day and n-day vulnerabilities are the most common
recommends minimum retention periods of 1 year for
initial access vectors, these devices are also susceptible
administrative activity logs, 90 days for security-related
to abuse of legitimate protocols such as publicly available
events, and 30 days for informational logs used to
FTP and SSH services, using stolen credentials.
contextualize other events.
Organizations should establish a formalized, staggered
The specialized nature of edge and core network device
assessment schedule to ensure total visibility without
configurations often results in a knowledge gap
overtaxing network resources. Scans should be deployed
for security personnel, who typically focus on endpoint
in phases until enterprise-wide coverage is achieved.
analysis, packet captures, and basic TCP/UDP
The objective is to transition into a consistent cadence
protocols. Security teams should maintain detailed
where every endpoint is assessed for vulnerabilities
playbooks outlining the network architecture, including
at least twice monthly. Vulnerability data should be
diagrams, device administrators, IP addresses, and
analyzed through a business context lens, prioritizing
hostnames. These playbooks are vital for technical
remediation based on the asset’s value and its impact
responders to follow critical steps and for executives
on business operations. To drive this process, the
to make sound decisions during a security event.

Special Report: Mandiant M-Trends 2026 82
vulnerability management team should distribute targeted
reports to stakeholders that include a clear description
of the identified risk, a list of affected endpoints, the
severity level specific to each asset, identification of
deviations from internal security policies, and specific
recommendations for remediation.
Furthermore, security teams should be included in
general architecture discussions to develop relationships
between teams, ensure proper telemetry is collected,
and to establish a clear understanding of where devices
fit into the network. This can help ensure that these
critical devices are not identified as a problem only after
a threat has moved deeper into the environment.
Outlook
Security monitoring and controls on traditional assets
continue to gain greater adoption and higher effective-
ness at identifying and stopping threats. At the same
time, edge devices have seen an increase in the number
of vulnerabilities identified. While edge and core network
devices are not novel targets for sophisticated actors,
Mandiant expects these devices to become increasingly
high priority targets for actors of all levels of sophistica-
tion. The challenges in security instrumentation combined
with the difficulty in remediating compromised edge and
core network devices present a significant headwind for
network defenders. Threat actors will likely shift their
tactics toward performing more of the attack lifecycle
on this class of device and away from traditional assets.
Furthermore, Mandiant expects exploitation of network
devices will continue to be an enticing initial access vector
for threat actors, as they look for remaining safe havens
in targeted environments.
Given the exposure, lack of visibility and critical location
of these devices in most networks, organizations must
take steps to identify the risks that unauthorized access to
these systems pose. Organizations should work to identify
these assets in their networks and implement robust patch
management, logging, and access controls to limit the risk
associated with compromise of these devices.

SPECIAL REPORT: MANDIANT M-TRENDS 2023 83
O
G
R
A
B
M
E

Special Report: Mandiant M-Trends 2026 84
Our threat intelligence analysts have observed Building a comprehensive security program now means
adversaries leveraging AI to accelerate attacks, securing developer and AI toolchains, treating identity
shifting from mass, static email campaigns toward as the ultimate perimeter, and ensuring recovery
hyper-personalized, voice-based social engineering, capabilities are fundamentally segmented from the
and deploying malware capable of querying large production environment.
language models mid-execution. Yet, despite these
The Mandiant mission is to help keep every organization
rapid technological advancements, the incidents
secure from cyber threats and confident in their
investigated by Mandiant for M-Trends 2026
readiness. Our annual M-Trends report, powered by the
primarily stemmed from fundamental human and
collective intelligence of frontline incident responders
systemic failures.
and the Google Threat Intelligence Group, is a core
We saw a stark divergence in adversary pacing. component of advancing that mission. We will continue
While cybercriminal groups optimized for immediate to share our frontline knowledge to help defenders close
impact and deliberate recovery denial, systematically critical visibility gaps, outmaneuver modern adversaries,
targeting backup infrastructure, identity services, and and build true operational resilience.
virtualization management planes, cyber espionage
groups and DPRK IT workers optimized for extreme
persistence. By operating from unmonitored edge
devices and utilizing native network functionalities
to evade detection, these stealthy actors drove the
global median dwell time up to 14 days.
Defending against these tactics, techniques and
procedures requires organizations to move at the speed
of the adversary. A proactive, resilient defense must go Mandiant, part of Google Cloud, has been at the
beyond static tools; it necessitates continuous identity forefront of cyber security and threat intelligence
verification, rigorous protection of critical control planes, since 2004. Our incident responders are on the
and expansive visibility across the entire ecosystem, frontlines of the world’s most complex breaches.
including the virtualization layer and EDR-less network We have a deep understanding of both existing
appliances. Security teams must be rigorously tested and emerging threat actors, as well as their rapidly
through realistic red team engagements that incorporate changing tactics, techniques, and procedures.
modern AI-driven tactics. Furthermore, organizations Mandiant helps organizations quickly get back to
should conduct regular tabletop exercises to update business after a security breach and applies front-
incident response playbooks for modern extortion line expertise to guide effective threat detection,
pipelines, and maintain a cyber incident response retainer
preparation, and to reduce business risk and build
to ensure immediate access to expert help before a minor
overall resiliency—before, during, and after an
alert becomes a catastrophic compromise.
incident. Since 2010, Mandiant has been dedicated
to publishing comprehensive trends based on our
Exploits (32%) remained the most common initial
infection vector for the sixth consecutive year, followed incident response engagements, providing critical
closely by a significant surge in highly interactive voice insights into the evolving threat landscape through
phishing (11%). Foundational security practices must the M-Trends report.
evolve to meet these specific realities. Organizations
If your organization suspects a cyber incident, or
must aggressively manage internet-facing attack
you are experiencing a security breach, please
surfaces, strictly isolate external-facing web application
contact Mandiant for Incident Response Assistance.
servers, and pivot security awareness training beyond
the inbox to address live, interactive social engineering.

Appendix: Mandiant M-Trends 2026 Report 85
MITRE
ATT&CK
Mandiant’s Targeted Attack Lifecycle is the
Techniques Related to
predictable sequence of events cyber attackers
use to carry out their attacks. Mandiant Targeted
Attack Lifecycle, 2025
Initial Reconnaissance
Reconnaissance
I ndicates T1593: Search Open Websites/Domains 16.3%
techniques
T1590: Gather Victim Network Information 4.4% T1590.002: DNS 4.4%
in the Cloud
matrix, T1592: Gather Victim Host Information 2.9%
introduced in
ATT&CK v18. T1598: Phishing for Information 2.4%
T1595: Active Scanning 1.0% T1595.002: Vulnerability Scanning 0.5%
T1595.001: Scanning IP Blocks 0.2%
T1595.003: Wordlist Scanning 0.2%
T1589: Gather Victim Identity Information 0.2% T1589.001: Credentials 0.2%
Resource Development
T1608: Stage Capabilities 11.7% T1608.001: Upload Malware 3.9%
T1608.003: Install Digital Certificate 2.9%
T1608.005: Link Target 2.2%
T1608.002: Upload Tool 1.9%
T1608.006: SEO Poisoning 0.5%
T1588: Obtain Capabilities 8.5% T1588.003: Code Signing Certificates 8.3%
T1588.007: Artificial Intelligence 0.2%
T1583: Acquire Infrastructure 6.8% T1583.003: Virtual Private Server 6.8%
T1584: Compromise Infrastructure 3.2%
T1587: Develop Capabilities 0.5% T1587.002: Code Signing Certificates 0.2%
T1587.003: Digital Certificates 0.2%

Appendix: Mandiant M-Trends 2026 Report 86
Initial Compromise
Initial Access
| T1190: Exploit Public-Facing Application  | 27.7%                                 |      |
| ----------------------------------------- | ------------------------------------- | ---- |
| T1133: External Remote Services           | 23.8%                                 |      |
| T1078: Valid Accounts                     | 17% T1078.004: Cloud Accounts         | 9.5% |
| T1566: Phishing                           | 14.1% T1566.004: Spearphishing Voice  | 6.1% |
|                                           | T1566.002: Spearphishing Link         | 3.2% |
|                                           | T1566.003: Spearphishing via Service  | 2.7% |
|                                           | T1566.001: Spearphishing Attachment   | 1.0% |
| T1189: Drive-by Compromise                | 6.3%                                  |      |
T1195: Supply Chain Compromise  1.7% T1195.002: Compromise Software Supply Chain 1.5%
|                                            | T1195.003: Compromise Hardware Supply Chain | 0.2% |
| ------------------------------------------ | ------------------------------------------- | ---- |
| T1200: Hardware Additions                  | 1.0%                                        |      |
| T1091: Replication Through Removable Media | 0.5%                                        |      |
| T1199: Trusted Relationship                | 0.5%                                        |      |
| T1659: Content Injection                   | 0.2%                                        |      |

Appendix: Mandiant M-Trends 2026 Report 87
Initial Compromise
Credential Access
| T1003: OS Credential Dumping | 13.6% T1003.003: NTDS                  | 4.4% |
| ---------------------------- | -------------------------------------- | ---- |
|                              | T1003.008: /etc/passwd and /etc/shadow | 3.2% |
|                              | T1003.001: LSASS Memory                | 3.2% |
|                              | T1003.002: Security Account Manager    | 2.4% |
|                              | T1003.006: DCSync                      | 1.7% |
|                              | T1003.004: LSA Secrets                 | 0.2% |
T1552: Unsecured Credentials  10.4% T1552.002: Credentials in Registry 2.7%
|     | T1552.001: Credentials In Files         | 1.7% |
| --- | --------------------------------------- | ---- |
|     | T1552.003: Bash History                 | 1.5% |
|     | T1552.007: Container API                | 1.2% |
|     | T1552.004: Private Keys                 | 1.0% |
|     | T1552.006: Group Policy Preferences     | 0.2% |
|     | T1552.005: Cloud Instance Metadata API  | 0.2% |
T1555: Credentials from Password Stores  6.1% T1555.006: Cloud Secrets Management Stores  2.4%
|                                                 | T1555.003: Credentials from Web Browsers | 2.2% |
| ----------------------------------------------- | ---------------------------------------- | ---- |
|                                                 | T1555.005: Password Managers             | 1.0% |
|                                                 | T1555.004: Windows Credential Manager    | 0.2% |
| T1111: Multi-Factor Authentication Interception | 4.9%                                     |      |
| T1110: Brute Force                              | 4.1% T1110.001: Password Guessing        | 1.5% |
|                                                 | T1110.004: Credential Stuffing           | 1.0% |
|                                                 | T1110.003: Password Spraying             | 0.7% |
T1556: Modify Authentication Process  2.7% T1556.006: Multi-Factor Authentication  1.5%
|     | T1556.003: Pluggable Authentication Modules | 0.2% |
| --- | ------------------------------------------- | ---- |
|     | T1556.002: Password Filter DLL              | 0.2% |
T1558: Steal or Forge Kerberos Tickets 2.7% T1558.003: Kerberoasting 1.9%
|                                                    | T1558.001: Golden Ticket   | 0.2% |
| -------------------------------------------------- | -------------------------- | ---- |
|                                                    | T1558.004: AS-REP Roasting | 0.2% |
|                                                    | T1558.002: Silver Ticket   | 0.2% |
| T1040: Network Sniffing                            | 1.0%                       |      |
| T1187: Forced Authentication                       | 0.7%                       |      |
| T1528: Steal Application Access Token              | 0.2%                       |      |
| T1539: Steal Web Session Cookie                    | 0.2%                       |      |
| T1649: Steal or Forge Authentication Certificates  | 0.2%                       |      |

Appendix: Mandiant M-Trends 2026 Report 88
Establish Foothold
Execution
T1059: Command and Scripting Interpreter  45.9% T1059.003: Windows Command Shell 26.2%
|                        | T1059.001: PowerShell               | 24%   |
| ---------------------- | ----------------------------------- | ----- |
|                        | T1059.007: JavaScript               | 5.6%  |
|                        | T1059.004: Unix Shell               | 5.3%  |
|                        | T1059.006: Python                   | 4.6%  |
|                        | T1059.005: Visual Basic             | 3.2%  |
|                        | T1059.012: Hypervisor CLI           | 2.2%  |
|                        | T1059.010: AutoHotKey & AutoIT      | 0.5%  |
|                        | T1059.009: Cloud API                | 0.5%  |
| T1204: User Execution  | 19.9% T1204.002: Malicious File     | 16.5% |
|                        | T1204.001: Malicious Link           | 2.2%  |
|                        | T1204.004: Malicious Copy and Paste | 1.2%  |
T1569: System Services 15.0% T1569.002: Service Execution 14.3%
|     | T1569.003: Systemctl | 0.5% |
| --- | -------------------- | ---- |
T1053: Scheduled Task/Job 11.2% T1053.005: Scheduled Task 9.0%
|                                           | T1053.003: Cron | 1.7% |
| ----------------------------------------- | --------------- | ---- |
| T1047: Windows Management Instrumentation | 7.0%            |      |
| T1129: Shared Modules                     | 2.7%            |      |
| T1559: Inter-Process Communication        | 1.9%            |      |
| T1651: Cloud Administration Command       | 0.5%            |      |
| T1203: Exploitation for Client Execution  | 0.2%            |      |
| T1609: Container Administration Command   | 0.2%            |      |
| T1610: Deploy Container                   | 0.2%            |      |

Appendix: Mandiant M-Trends 2026 Report 89
Establish Foothold
Persistence
| T1133: External Remote Services | 23.8% |     |
| ------------------------------- | ----- | --- |
T1098: Account Manipulation  18.7% T1098.007: Additional Local or Domain Groups 7.8%
|                        | T1098.005: Device Registration           | 3.6% |
| ---------------------- | ---------------------------------------- | ---- |
|                        | T1098.001: Additional Cloud Credentials  | 1.0% |
|                        | T1098.004: SSH Authorized Keys           | 0.5% |
|                        | T1098.003: Additional Cloud Roles        | 0.2% |
| T1078: Valid Accounts  | 17.0% T1078.004: Cloud Accounts          | 9.5% |
T1543: Create or Modify System Process 16.7% T1543.003: Windows Service 8.3%
|     | T1543.002: Systemd Service | 1.9% |
| --- | -------------------------- | ---- |
|     | T1543.004: Launch Daemon   | 0.2% |
T1505: Server Software Component 14.8% T1505.003: Web Shell 14.8%
T1053: Scheduled Task/Job 11.2% T1053.005: Scheduled Task 9.0%
|                        | T1053.003: Cron                | 1.7% |
| ---------------------- | ------------------------------ | ---- |
| T1136: Create Account  | 10.2% T1136.001: Local Account | 3.2% |
|                        | T1136.003: Cloud Account       | 1.5% |
|                        | T1136.002: Domain Account      | 1.0% |
T1547: Boot or Logon Autostart Execution 8.3% T1547.001: Registry Run Keys / Startup Folder 7.5%
|     | T1547.009: Shortcut Modification     | 1.0% |
| --- | ------------------------------------ | ---- |
|     | T1547.013: XDG Autostart Entries     | 0.5% |
|     | T1547.005: Security Support Provider | 0.2% |
T1574: Hijack Execution Flow 7.3% T1574.011: Services Registry Permissions Weakness 6.8%
|     | T1574.001: DLL                                | 0.5% |
| --- | --------------------------------------------- | ---- |
|     | T1574.008: Path Interception by Search Order  | 0.2% |
Hijacking
T1546: Event Triggered Execution  6.1% T1546.003: Windows Management Instrumentation  4.1%
Event Subscription
|                                       | T1546.015: Component Object Model Hijacking      | 0.7% |
| ------------------------------------- | ------------------------------------------------ | ---- |
|                                       | T1546.007: Netsh Helper DLL                      | 0.5% |
|                                       | T1546.010: AppInit DLLs                          | 0.2% |
|                                       | T1546.004: Unix Shell Configuration Modification | 0.2% |
|                                       | T1546.001: Change Default File Association       | 0.2% |
| T1671: Cloud Application Integration  | 4.6%                                             |      |
T1556: Modify Authentication Process 1.5% T1556.006: Multi-Factor Authentication  1.5%
T1037: Boot or Logon Initialization Scripts 0.5% T1037.001: Logon Script (Windows) 0.2%
|     | T1037.004: RC Scripts | 0.2% |
| --- | --------------------- | ---- |
T1176: Software Extensions 0.5% T1176.001: Browser Extensions 0.2%
T1137: Office Application Startup  0.2% T1137.005: Outlook Rules  0.2%
| T1554: Compromise Host Software Binary | 0.2% |     |
| -------------------------------------- | ---- | --- |

Appendix: Mandiant M-Trends 2026 Report 90
Escalate Privileges
Credential Access
| T1003: OS Credential Dumping | 13.6% T1003.003: NTDS                  | 4.4% |
| ---------------------------- | -------------------------------------- | ---- |
|                              | T1003.008: /etc/passwd and /etc/shadow | 3.2% |
|                              | T1003.001: LSASS Memory                | 3.2% |
|                              | T1003.002: Security Account Manager    | 2.4% |
|                              | T1003.006: DCSync                      | 1.7% |
|                              | T1003.004: LSA Secrets                 | 0.2% |
T1552: Unsecured Credentials  10.4% T1552.002: Credentials in Registry 2.7%
|     | T1552.001: Credentials In Files         | 1.7% |
| --- | --------------------------------------- | ---- |
|     | T1552.003: Bash History                 | 1.5% |
|     | T1552.007: Container API                | 1.2% |
|     | T1552.004: Private Keys                 | 1.0% |
|     | T1552.006: Group Policy Preferences     | 0.2% |
|     | T1552.005: Cloud Instance Metadata API  | 0.2% |
T1555: Credentials from Password Stores  6.1% T1555.006: Cloud Secrets Management Stores  2.4%
|                                                 | T1555.003: Credentials from Web Browsers | 2.2% |
| ----------------------------------------------- | ---------------------------------------- | ---- |
|                                                 | T1555.005: Password Managers             | 1.0% |
| T1111: Multi-Factor Authentication Interception | 4.9%                                     |      |
| T1110: Brute Force                              | 4.1% T1110.001: Password Guessing        | 1.5% |
|                                                 | T1110.004: Credential Stuffing           | 1.0% |
|                                                 | T1110.003: Password Spraying             | 0.7% |
T1556: Modify Authentication Process  2.7% T1556.002: Password Filter DLL 2.0%
|     | T1556.003: Pluggable Authentication Modules | 2.0% |
| --- | ------------------------------------------- | ---- |
|     | T1556.006: Multi-Factor Authentication      | 1.5% |
T1558: Steal or Forge Kerberos Tickets 2.7% T1558.003: Kerberoasting 1.9%
|                                                    | T1558.001: Golden Ticket   | 0.2% |
| -------------------------------------------------- | -------------------------- | ---- |
|                                                    | T1558.004: AS-REP Roasting | 0.2% |
|                                                    | T1558.002: Silver Ticket   | 0.2% |
| T1040: Network Sniffing                            | 1.0%                       |      |
| T1187: Forced Authentication                       | 0.7%                       |      |
| T1528: Steal Application Access Token              | 0.2%                       |      |
| T1539: Steal Web Session Cookie                    | 0.2%                       |      |
| T1649: Steal or Forge Authentication Certificates  | 0.2%                       |      |

Appendix: Mandiant M-Trends 2026 Report 91
Escalate Privileges
Privilege Escalation
| T1078: Valid Accounts  | 17% T1078.004: Cloud Accounts  | 9.5% |
| ---------------------- | ------------------------------ | ---- |
T1543: Create or Modify System Process 16.7% T1543.003: Windows Service 8.3%
|     | T1543.002: Systemd Service | 1.9% |
| --- | -------------------------- | ---- |
|     | T1543.004: Launch Daemon   | 0.2% |
T1053: Scheduled Task/Job 11.2% T1053.005: Scheduled Task 9.0%
|     | T1053.003: Cron | 1.7% |
| --- | --------------- | ---- |
T1547: Boot or Logon Autostart Execution 8.3% T1547.001: Registry Run Keys / Startup Folder 7.5%
|     | T1547.009: Shortcut Modification     | 1.0% |
| --- | ------------------------------------ | ---- |
|     | T1547.013: XDG Autostart Entries     | 0.5% |
|     | T1547.005: Security Support Provider | 0.2% |
T1098: Account Manipulation 7.8% T1098.007: Additional Local or Domain Groups 7.8%
T1574: Hijack Execution Flow 7.3% T1574.011: Services Registry Permissions Weakness 6.8
|     | T1574.001: DLL                                | 0.5% |
| --- | --------------------------------------------- | ---- |
|     | T1574.008: Path Interception by Search Order  | 0.2% |
Hijacking
T1546: Event Triggered Execution  6.1% T1546.003: Windows Management Instrumentation  4.1%
Event Subscription
|                                              | T1546.015: Component Object Model Hijacking      | 0.7% |
| -------------------------------------------- | ------------------------------------------------ | ---- |
|                                              | T1546.007: Netsh Helper DLL                      | 0.5% |
|                                              | T1546.010: AppInit DLLs                          | 0.2% |
|                                              | T1546.004: Unix Shell Configuration Modification | 0.2% |
|                                              | T1546.001: Change Default File Association       | 0.2% |
| T1055: Process Injection                     | 1.0%                                             |      |
| T1068: Exploitation for Privilege Escalation | 1.0%                                             |      |
T1548: Abuse Elevation Control Mechanism  1.0% T1548.002: Bypass User Account Control 0.5%
|     | T1548.003: Sudo and Sudo Caching | 0.2% |
| --- | -------------------------------- | ---- |
|     | T1548.001: Setuid and Setgid     | 0.2% |
T1134: Access Token Manipulation 0.7% T1134.001: Token Impersonation/Theft 0.7%
T1484: Domain or Tenant Policy Modification  0.7% T1484.001: Group Policy Modification 0.7%
T1037: Boot or Logon Initialization Scripts 0.5% T1037.001: Logon Script (Windows) 0.2%
|     | T1037.004: RC Scripts | 0.2% |
| --- | --------------------- | ---- |

Appendix: Mandiant M-Trends 2026 Report 92
Internal Reconnaissance
Discovery
| T1083: File and Directory Discovery |     | 33.5% |
| ----------------------------------- | --- | ----- |
| T1033: System Owner/User Discovery  |     | 24.0% |
T1087: Account Discovery  20.9% T1087.002: Domain Account 11.9%
T1087.001: Local Account 10.7%
T1087.004: Cloud Account  1.9%
T1087.003: Email Account  0.2%
T1016: System Network Configuration Discovery 19.4% T1016.001: Internet Connection Discovery 14.1%
T1016.002: Wi-Fi Discovery 0.7%
| T1082: System Information Discovery  |     | 18.2% |
| ------------------------------------ | --- | ----- |
T1518: Software Discovery  17.0% T1518.001: Security Software Discovery 1.2%
| T1057: Process Discovery |     | 14.6% |
| ------------------------ | --- | ----- |
T1069: Permission Groups Discovery  14.1% T1069.002: Domain Groups 8.3%
T1069.001: Local Groups 3.4%
T1069.003: Cloud Groups  1.7%
| T1049: System Network Connections Discovery |     | 10.0% |
| ------------------------------------------- | --- | ----- |
| T1482: Domain Trust Discovery               |     | 8.5%  |
| T1012: Query Registry                       |     | 5.1%  |
| T1018: Remote System Discovery              |     | 4.9%  |
| T1007: System Service Discovery             |     | 3.9%  |
| T1580: Cloud Infrastructure Discovery       |     | 3.4%  |
| T1619: Cloud Storage Object Discovery       |     | 3.4%  |
| T1046: Network Service Discovery            |     | 2.9%  |
| T1201: Password Policy Discovery            |     | 1.7%  |
T1614: System Location Discovery  1.5% T1614.001: System Language Discovery 1.5%
| T1124: System Time Discovery         |     | 1.2% |
| ------------------------------------ | --- | ---- |
| T1040: Network Sniffing              |     | 1.0% |
| T1654: Log Enumeration               |     | 1.0% |
| T1673: Virtual Machine Discovery     |     | 1.0% |
| T1680: Local Storage Discovery       |     | 0.7% |
| T1120: Peripheral Device Discovery   |     | 0.5% |
| T1538: Cloud Service Dashboard       |     | 0.5% |
| T1652: Device Driver Discovery       |     | 0.5% |
| T1217: Browser Information Discovery |     | 0.2% |
| T1526: Cloud Service Discovery       |     | 0.2% |

Appendix: Mandiant M-Trends 2026 Report 93
Lateral Movement
Execution
T1059: Command and Scripting Interpreter  45.9% T1059.003: Windows Command Shell 26.2%
|                        | T1059.001: PowerShell               | 24.0% |
| ---------------------- | ----------------------------------- | ----- |
|                        | T1059.007: JavaScript               | 5.6%  |
|                        | T1059.004: Unix Shell               | 5.3%  |
|                        | T1059.006: Python                   | 4.6%  |
|                        | T1059.005: Visual Basic             | 3.2%  |
|                        | T1059.012: Hypervisor CLI           | 2.2%  |
|                        | T1059.010: AutoHotKey & AutoIT      | 0.5%  |
|                        | T1059.009: Cloud API                | 0.5%  |
| T1204: User Execution  | 19.9% T1204.002: Malicious File     | 16.5% |
|                        | T1204.001: Malicious Link           | 2.2%  |
|                        | T1204.004: Malicious Copy and Paste | 1.2%  |
T1569: System Services 15% T1569.002: Service Execution 14.3%
|     | T1569.003: Systemctl | 0.5% |
| --- | -------------------- | ---- |
T1053: Scheduled Task/Job 11.2% T1053.005: Scheduled Task 9.0%
|                                           | T1053.003: Cron | 1.7% |
| ----------------------------------------- | --------------- | ---- |
| T1047: Windows Management Instrumentation | 7.0%            |      |
| T1129: Shared Modules                     | 2.7%            |      |
| T1559: Inter-Process Communication        | 1.9%            |      |
| T1651: Cloud Administration Command       | 0.5%            |      |
| T1203: Exploitation for Client Execution  | 0.2%            |      |
| T1609: Container Administration Command   | 0.2%            |      |
| T1610: Deploy Container                   | 0.2%            |      |

Appendix: Mandiant M-Trends 2026 Report 94
Lateral Movement
Lateral Movement
T1021: Remote Services 30.6% T1021.001: Remote Desktop Protocol 22.1%
T1021.002: SMB/Windows Admin Shares 19.4%
T1021.004: SSH 12.9%
T1021.006: Windows Remote Management 2.4%
T1021.008: Direct Cloud VM Connections 0.5%
T1021.003: Distributed Component Object Model 0.5%
T1021.005: VNC 0.2%
T1550: Use Alternate Authentication Material 6.3% T1550.001: Application Access Token 5.3%
T1550.002: Pass the Hash 1.0%
T1570: Lateral Tool Transfer 1.0%
T1091: Replication Through Removable Media 0.5%
T1080: Taint Shared Content 0.2%

Appendix: Mandiant M-Trends 2026 Report 95
Maintain Presence
Defense Evasion
T1027: Obfuscated Files or Information  27.2% T1027.015: Compression 5.6%
|     | T1027.002: Software Packing       | 4.4% |
| --- | --------------------------------- | ---- |
|     | T1027.010: Command Obfuscation    | 4.4% |
|     | T1027.009: Embedded Payloads      | 2.2% |
|     | T1027.004: Compile After Delivery | 1.5% |
|     | T1027.013: Encrypted/Encoded File | 1.2% |
|     | T1027.001: Binary Padding         | 0.2% |
T1070: Indicator Removal  24.8% T1070.004: File Deletion 15.5%
|     | T1070.009: Clear Persistence                  | 5.1% |
| --- | --------------------------------------------- | ---- |
|     | T1070.001: Clear Windows Event Logs           | 4.6% |
|     | T1070.006: Timestomp                          | 3.2% |
|     | T1070.007: Clear Network Connection History   | 1.9% |
and Configurations
|                        | T1070.002: Clear Linux or Mac System Logs | 0.5% |
| ---------------------- | ----------------------------------------- | ---- |
|                        | T1070.003: Clear Command History          | 0.5% |
|                        | T1070.010: Relocate Malware               | 0.5% |
|                        | T1070.008: Clear Mailbox Data             | 0.2% |
| T1078: Valid Accounts  | 17.0% T1078.004: Cloud Accounts           | 9.5% |
T1562: Impair Defenses  16.5% T1562.001: Disable or Modify Tools  10.2%
|                                                | T1562.004: Disable or Modify System Firewall    | 9.0% |
| ---------------------------------------------- | ----------------------------------------------- | ---- |
|                                                | T1562.002: Disable Windows Event Logging        | 4.4% |
|                                                | T1562.003: Impair Command History Logging       | 0.7% |
|                                                | T1562.012: Disable or Modify Linux Audit System | 0.2% |
| T1140: Deobfuscate/Decode Files or Information | 15.3%                                           |      |
| T1564: Hide Artifacts                          | 14.6% T1564.003: Hidden Window                  | 4.4% |
|                                                | T1564.001: Hidden Files and Directories         | 4.4% |
|                                                | T1564.008: Email Hiding Rules                   | 3.9% |
|                                                | T1564.011: Ignore Process Interrupts            | 1.7% |
|                                                | T1564.012: File/Path Exclusions                 | 1.7% |

Appendix: Mandiant M-Trends 2026 Report 96
Maintain Presence
Defense Evasion (Continued)
T1218: System Binary Proxy Execution 11.2% T1218.011: Rundll32 6.6%
T1218.007: Msiexec 4.6%
T1218.005: Mshta 0.5%
T1218.002: Control Panel 0.2%
T1218.014: MMC 0.2%
T1112: Modify Registry 10.0%
T1036: Masquerading 9.2% T1036.001: Invalid Code Signature 1.7%
T1036.005: Match Legitimate Resource Name 1.5%
or Location
T1036.011: Overwrite Process Arguments 0.2%
T1036.008: Masquerade File Type 0.2%
T1036.003: Rename Legitimate Utilities 0.2%
T1553: Subvert Trust Controls 8.3% T1553.002: Code Signing 8.3%
T1222: File and Directory Permissions Modification 7.5% T1222.002: Linux and Mac File and Directory 6.6%
Permissions Modification
T1222.001: Windows File and Directory 1.0%
Permissions Modification
T1574: Hijack Execution Flow 7.3% T1574.011: Services Registry Permissions Weakness 6.8%
T1574.001: DLL 0.5%
T1574.008: Path Interception by Search 0.2%
Order Hijacking
T1550: Use Alternate Authentication Material 6.3% T1550.001: Application Access Token 5.3%
T1550.002: Pass the Hash 1.0%
T1202: Indirect Command Execution 4.6%
T1666: Modify Cloud Resource Hierarchy 4.6%
T1006: Direct Volume Access 3.4%
T1556: Modify Authentication Process 2.7% T1556.006: Multi-Factor Authentication 1.5%
T1556.003: Pluggable Authentication Modules 0.2%
T1556.002: Password Filter DLL 0.2%
T1656: Impersonation 1.7%
T1578: Modify Cloud Compute Infrastructure 1.5% T1578.003: Delete Cloud Instance 1.2%
T1578.005: Modify Cloud Compute 0.2%
Configurations
T1055: Process Injection 1.0%

Appendix: Mandiant M-Trends 2026 Report 97
Maintain Presence
Defense Evasion (Continued)
T1548: Abuse Elevation Control Mechanism 1.0% T1548.002: Bypass User Account Control 0.5%
T1548.003: Sudo and Sudo Caching 0.2%
T1548.001: Setuid and Setgid 0.2%
T1134: Access Token Manipulation 0.7% T1134.001: Token Impersonation/Theft 0.7%
T1484: Domain or Tenant Policy Modification 0.7% T1484.001: Group Policy Modification 0.7%
T1207: Rogue Domain Controller 0.5%
T1127: Trusted Developer Utilities Proxy Execution 0.2% T1127.001: MSBuild 0.2%
T1220: XSL Script Processing 0.2%
T1221: Template Injection 0.2%
T1599: Network Boundary Bridging 0.2% T1599.001: Network Address Translation Traversal 0.2%
T1610: Deploy Container 0.2%
T1620: Reflective Code Loading 0.2%
T1647: Plist File Modification 0.2%
T1672: Email Spoofing 0.2%

AAppppeennddiixx::  MMaannddiiaanntt  MM--TTrreennddss  22002266  RReeppoorrtt 98
Maintain Presence
Persistence
| T1133: External Remote Services | 23.8% |     |
| ------------------------------- | ----- | --- |
T1098: Account Manipulation  18.7% T1098.007: Additional Local or Domain Groups 7.8%
|                        | T1098.005: Device Registration           | 3.6% |
| ---------------------- | ---------------------------------------- | ---- |
|                        | T1098.001: Additional Cloud Credentials  | 1.0% |
|                        | T1098.004: SSH Authorized Keys           | 0.5% |
|                        | T1098.003: Additional Cloud Roles        | 0.2% |
| T1078: Valid Accounts  | 17.0% T1078.004: Cloud Accounts          | 9.5% |
T1543: Create or Modify System Process 16.7% T1543.003: Windows Service 8.3%
|     | T1543.002: Systemd Service | 1.9% |
| --- | -------------------------- | ---- |
|     | T1543.004: Launch Daemon   | 0.2% |
T1505: Server Software Component 14.8% T1505.003: Web Shell 14.8%
T1053: Scheduled Task/Job 11.2% T1053.005: Scheduled Task 9.0%
|                        | T1053.003: Cron                | 1.7% |
| ---------------------- | ------------------------------ | ---- |
| T1136: Create Account  | 10.2% T1136.001: Local Account | 3.2% |
|                        | T1136.003: Cloud Account       | 1.5% |
|                        | T1136.002: Domain Account      | 1.0% |
T1547: Boot or Logon Autostart Execution 8.3% T1547.001: Registry Run Keys / Startup Folder 7.5%
|     | T1547.009: Shortcut Modification     | 1.0% |
| --- | ------------------------------------ | ---- |
|     | T1547.013: XDG Autostart Entries     | 0.5% |
|     | T1547.005: Security Support Provider | 0.2% |
T1574: Hijack Execution Flow 7.3% T1574.011: Services Registry Permissions Weakness 6.8%
|     | T1574.001: DLL                                | 0.5% |
| --- | --------------------------------------------- | ---- |
|     | T1574.008: Path Interception by Search Order  | 0.2% |
Hijacking
T1546: Event Triggered Execution  6.1% T1546.003: Windows Management Instrumentation  4.1%
Event Subscription
|                                       | T1546.015: Component Object Model Hijacking      | 0.7% |
| ------------------------------------- | ------------------------------------------------ | ---- |
|                                       | T1546.007: Netsh Helper DLL                      | 0.5% |
|                                       | T1546.010: AppInit DLLs                          | 0.2% |
|                                       | T1546.004: Unix Shell Configuration Modification | 0.2% |
|                                       | T1546.001: Change Default File Association       | 0.2% |
| T1671: Cloud Application Integration  | 4.6%                                             |      |
T1556: Modify Authentication Process 1.5% T1556.006: Multi-Factor Authentication  1.5%
T1037: Boot or Logon Initialization Scripts 0.5% T1037.001: Logon Script (Windows) 0.2%
|     | T1037.004: RC Scripts | 0.2% |
| --- | --------------------- | ---- |
T1176: Software Extensions 0.5% T1176.001: Browser Extensions 0.2%
T1137: Office Application Startup  0.2% T1137.005: Outlook Rules  0.2%
| T1554: Compromise Host Software Binary | 0.2% |     |
| -------------------------------------- | ---- | --- |

Appendix: Mandiant M-Trends 2026 Report 99
Maintain Presence
Command And Control
| T1105: Ingress Tool Transfer | 24.5% |     |
| ---------------------------- | ----- | --- |
T1102: Web Service 15.5% T1102.002: Bidirectional Communication 0.5%
T1071: Application Layer Protocol 11.2% T1071.001: Web Protocols 3.4%
|                                       | T1071.004: DNS                     | 3.2% |
| ------------------------------------- | ---------------------------------- | ---- |
|                                       | T1071.002: File Transfer Protocols | 0.7% |
| T1095: Non-Application Layer Protocol | 10.9%                              |      |
| T1572: Protocol Tunneling             | 8.0%                               |      |
T1573: Encrypted Channel 2.9% T1573.002: Asymmetric Cryptography 2.9%
| T1090: Proxy | 2.7% T1090.001: Internal Proxy | 1.0% |
| ------------ | ------------------------------ | ---- |
|              | T1090.003: Multi-hop Proxy     | 0.5% |
|              | T1090.002: External Proxy      | 0.5% |
T1219: Remote Access Software 1.0% T1219.002: Remote Desktop Software 0.5%
|                          | T1219.003: Remote Access Hardware | 0.5% |
| ------------------------ | --------------------------------- | ---- |
| T1571: Non-Standard Port | 0.7%                              |      |
| T1659: Content Injection | 0.2%                              |      |

Appendix: Mandiant M-Trends 2026 Report 100
Mission Completion
Collection
| T1074: Data Staged  | 39.6% T1074.001: Local Data Staging | 3.6% |
| ------------------- | ----------------------------------- | ---- |
|                     | T1074.002: Remote Data Staging      | 0.7% |
T1213: Data from Information Repositories  12.6% T1213.002: Sharepoint  6.1%
|     | T1213.004: Customer Relationship Management  | 2.7% |
| --- | -------------------------------------------- | ---- |
Software
|     | T1213.003: Code Repositories                    | 1.2% |
| --- | ----------------------------------------------- | ---- |
|     | T1213.006: Data from Information Repositories:  | 0.5% |
Databases
|     | T1213.005: Messaging Applications  | 0.2% |
| --- | ---------------------------------- | ---- |
T1560: Archive Collected Data 11.4% T1560.001: Archive via Utility 5.6%
| T1005: Data from Local System | 11.2% |     |
| ----------------------------- | ----- | --- |
T1114: Email Collection  7.3% T1114.003: Email Forwarding Rule  0.7%
|                                       | T1114.002: Remote Email Collection  | 0.2% |
| ------------------------------------- | ----------------------------------- | ---- |
| T1039: Data from Network Shared Drive | 3.4%                                |      |
| T1530: Data from Cloud Storage        | 2.7%                                |      |
| T1115: Clipboard Data                 | 1.7%                                |      |
T1602: Data from Configuration Repository 1.2% T1602.002: Network Device Configuration Dump 1.2%
|                                  | T1602.001: SNMP (MIB Dump) | 0.2% |
| -------------------------------- | -------------------------- | ---- |
| T1113: Screen Capture            | 0.5%                       |      |
| T1025: Data from Removable Media | 0.2%                       |      |
| T1125: Video Capture             | 0.2%                       |      |

Appendix: Mandiant M-Trends 2026 Report 101
Mission Completion
Exfiltration
| T1041: Exfiltration Over C2 Channel | 7.8% |     |
| ----------------------------------- | ---- | --- |
T1567: Exfiltration Over Web Service  5.8% T1567.002: Exfiltration to Cloud Storage 2.9%
|     | T1567.001: Exfiltration to Code Repository    | 0.5% |
| --- | --------------------------------------------- | ---- |
|     | T1567.003: Exfiltration to Text Storage Sites | 0.2% |
T1020: Automated Exfiltration 0.5% T1020.001: Traffic Duplication 0.2%
T1011: Exfiltration Over Other Network Medium 0.2% T1011.001: Exfiltration Over Bluetooth 0.2%
| T1030: Data Transfer Size Limits | 0.2% |     |
| -------------------------------- | ---- | --- |
T1052: Exfiltration Over Physical Medium 0.2% T1052.001: Exfiltration over USB 0.2%
Impact
| T1486: Data Encrypted for Impact  | 17.7% |     |
| --------------------------------- | ----- | --- |
| T1489: Service Stop               | 10.7% |     |
| T1657: Financial Theft            | 10.4% |     |
T1565: Data Manipulation 6.1% T1565.001: Stored Data Manipulation 3.9%
| T1490: Inhibit System Recovery  | 2.7%                                 |      |
| ------------------------------- | ------------------------------------ | ---- |
| T1485: Data Destruction         | 2.2%                                 |      |
| T1496: Resource Hijacking       | 1.5%                                 |      |
| T1491: Defacement               | 1.2% T1491.002: External Defacement  | 0.5% |
|                                 | T1491.001: Internal Defacement       | 0.2% |
| T1529: System Shutdown/Reboot   | 1.2%                                 |      |
| T1531: Account Access Removal   | 1.2%                                 |      |

SPECIAL REPORT: MANDIANT M-TRENDS 2023 102
O
G
R
A
B
M
E