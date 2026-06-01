# ReliaQuest Annual Cyber-Threat Report 2024

## Table of Contents
- [Introduction](#introduction)
- [Executive Summary](#executive-summary)
- [Data-Driven Threat Insights](#data-driven-threat-insights)
- [Incident Metrics](#incident-metrics)
- [Critical Security Incidents Data](#critical-security-incidents-data)
- [What We Observed & Forecast](#what-we-observed--forecast)
- [Business Email Compromise Making A Big Impact](#business-email-compromise-making-a-big-impact)
- [Extortion Threat Looms Large](#extortion-threat-looms-large)
- [Social Engineering](#social-engineering)
- [Malware-Free and LotL Activity](#malware-free-and-lotl-activity)
- [TTP Evolution](#ttp-evolution)
- [Conclusions and Recommendations](#conclusions-and-recommendations)
- [Conclusions Based on 2023 Data and Analysis](#conclusions-based-on-2023-data-and-analysis)
- [General Recommendations and Best Practices](#general-recommendations-and-best-practices)
- [How ReliaQuest Can Help](#how-reliaquest-can-help)
- [Reference List](#reference-list)
- [Appendix A: Methodology](#appendix-a-methodology)
- [Appendix B: Endnotes](#appendix-b-endnotes)

---

## Introduction
The ReliaQuest Annual Cyber-Threat Report provides a comprehensive overview of the key cyber threats we observed targeting organizations from January 1 to December 31, 2023 (the reporting period). The ReliaQuest Threat Research team based this report on quantitative and qualitative analysis of cyber attacks.

Our aim is to empower organizations with actionable intelligence, delving into threat actors’ motives and tactics, techniques, and procedures (TTPs). This intelligence fosters a more profound understanding of threat operations, enabling security leaders to make informed decisions and refine cybersecurity tactics to accommodate an ever-changing cyber-threat landscape. Our analysis brings to light the most pressing cyber threats, such as business email compromise (BEC), extortion, Living off the Land (LotL) attacks, and sophisticated social engineering. This report charts threat actors’ evolution, but also anticipates potential shifts in their TTPs as we look to the future. We offer a forward-looking perspective to prepare organizations for emerging challenges they are likely to face.

Based on our observations and response to threat activity, this report provides strategic recommendations to bolster your security posture. But our mission extends beyond immediate threat mitigation. A preventative approach to cybersecurity—focusing on proactive measures and cost-effectiveness—embodies the ReliaQuest core principles:
- **Increase Visibility**
- **Reduce Complexity**
- **Manage Risk**

These principles are the bedrock of our methodology and ensure that, as a force-multiplier, we amplify your capabilities to navigate the murky waters of cyber threats. We hope that this report will serve as a valuable source of thorough analysis and actionable insights, thereby contributing to our mission to Make Security Possible.

---

## Executive Summary
Over 2023, cyber-threat actors continued to select from a wide range of TTPs to infiltrate systems and networks. Their choices varied according to specific contexts, and would have been influenced by tool or access availability, motive, and geopolitical tensions, among other factors. Our responses to incidents revealed the following key metrics and insights:

| Resolution Time | Incident Response | Phishing |
| :--- | :--- | :--- |
| **Depends on Context** | **is Improving** | **Remains Popular** |
| Incidents with the longest mean time to resolve (MTTR) occurred in sectors that rely heavily on physical infrastructure and operational technology (OT) systems. | Organizations utilizing traditional approaches saw an average Mean Time to Respond (MTTR) of 2.3 days. Those who opted to leverage some level of AI and automation saw a reduction to 58 minutes: a 98.8% decrease from 2022. Organizations who fully leveraged AI and automation are seeing reductions of MTTR down to 7 minutes or less. | Phishing links or attachments were used in 71.1% of all incidents. These methods were commonly used to aid initial access to networks or systems. |

- **Business Email Compromise (BEC) Has Surged**: BEC is bolstered by phishing-as-a-service (PhaaS) platforms, often providing threat actors with access to critical services, leading to widespread infections. Threat actors also targeted cloud and on-premises environments through social engineering, frequently employing MFA fatigue attacks.
- **Social Engineering Attacks Proliferated Dramatically**: September saw a surge in social engineering, especially QR code phishing (quishing) with a 51% increase compared to the total from January through August. One trend is combining credential harvesters with adversary-in-the-middle (AITM) activity to bypass multifactor authentication (MFA).
- **Living off the Land Binaries (LOLBins) Are in Frequent Use**: LOLBINs are popular with threat actors performing LotL activity—especially developers of fileless malware. They accounted for a significant portion of critical security incidents: 22.3%. Of these, 92% involved Rundll32, Msiexec, and Mshta.
- **Extortion Continues to Flourish**: Extortion activity increased by 74.3%, with a record 4,819 compromised entities named on data-leak websites. Just on its own, the “LockBit” ransomware group named an unprecedented 1,000-plus entities. “Clop,” “ALPHV,” and other groups adopted new extortion tactics, including filing SEC complaints, using cloned domains to leak data, and leaking data via torrents.
- **AI and Automation Are Aiding Threat Actors**: Threat actors are increasingly leveraging automation to identify and exploit vulnerabilities more quickly; this was observed with the mass exploitation of the Citrix Bleed vulnerability. It is also likely that automation and Generative AI will increasingly assist threat actors in conducting phishing at scale.
- **Billions of Exposed Credentials Pose a Significant Threat**: In 2023 we discovered more than 6 billion exposed credentials in breached data on the clear and dark web, bringing the total number we have found to 36 billion-plus. Threat actors frequently use stolen credentials to gain initial access or launch credential stuffing attacks.

### Attackers Favor Certain TTPs in High-Risk, High-Impact Activity
Analyzing our critical security incidents, we found that the most commonly used TTPs, categorized by MITRE ATT&CK® categories, were:
- **Initial Access**: Drive-by compromise was used in 29.2% of incidents related to initial access.
- **Execution**: 64.9% of incidents involved the abuse of command and scripting interpreters.
- **Persistence**: Scheduled tasks were abused in 32.8% of incidents.
- **Privilege Escalation**: In 24.1% of incidents, attackers used valid domain accounts to escalate privileges.
- **Defense Evasion**: Obfuscation techniques were employed in 23.5% of incidents.
- **Command-and-Control (C2)**: 80% of incidents involved HTTPS traffic or ingress tool transfers.
- **Lateral Movement**: Remote desktop protocol (RDP) and Server Message Block (SMB)—both Windows-supported protocols—were used in 59.3% of incidents.
- **Impact**: Financial theft was the desired impact in 88.4% of incidents, making it the primary motive.

---

## Data-Driven Threat Insights
The ReliaQuest GreyMatter® security operations platform responds to thousands of incidents every day, aiding organizations in detecting threats rapidly and reliably. In addition to providing automated alerts, we proactively hunt within our customers’ environments for threats that may have evaded security measures. In this section we present analysis of data from two sources (see Appendix A for full definitions):

- **Incident metrics**, pertaining to all incidents identified as true positives; we discuss the average response time across technologies and industries, and the most commonly observed MITRE ATT&CK techniques.
- **Critical security incidents**, which are a smaller subset of true positive incidents that had the potential to result in data breaches or theft (e.g., involving extortion, espionage, custom malware, hands-on-keyboard operations, commodity threats); we describe the most common MITRE ATT&CK techniques observed at various attack stages.

---

## Incident Metrics
### Mean Time to Resolve
MTTR is an important metric: the measurement of the average time between incident detection and customer resolution. A shorter MTTR indicates a more efficient and effective response, reducing the potential damage caused by the incident and minimizing downtime.

![Chart showing MTTR by sector in 2023]

As shown in Figure 1, the sector with the longest average MTTR was Mining, Quarrying, and Oil and Gas Extraction: 5.1 days. This was followed by Public Administration, with an MTTR of 4.8 days. In 2023, the average MTTR across all sectors dropped to 2.6 days, highlighting an improvement in customer response to incidents.

### Automating Incident Response With AI
Organizations who opted to leverage some level of AI and automation saw a reduction in their MTTR to 58 minutes: a 98.8% decrease from 2022. Those who fully leveraged AI and automation are seeing reductions of MTTR down to 7 minutes or less.

### GreyMatter Incident TTPs
Financially motivated cybercriminal groups continue to indiscriminately attack companies in almost all sectors and regions. The three most observed MITRE ATT&CK techniques in our true-positive data set involved phishing activity, accounting for approximately 71.1% of all observed TTPs in the reporting period.

![Chart showing GreyMatter true-positive incidents’ TTPs in 2023]
![Chart showing number of incidents associated with MITRE tactics in customer incidents in 2023]

---

## Critical Security Incidents Data
### Initial Access
Most TTPs used to achieve initial access to a compromised customer’s environment during the reporting period were linked to user interaction or error. Drive-by compromise was involved in 29.2% of incidents. Most frequently deployed was “SocGholish” (aka FAKEUPDATES), a malware loader often used by initial access brokers (IABs).

![Chart showing Initial-access TTPs observed in ReliaQuest customer incidents in 2023]
![Chart showing Malware distributed through drive-by compromise in 2023, by type of malware]

### Post-Exploitation Activity
#### Execution
To execute malicious code on a compromised system, threat actors frequently exploited scripting interpreters, such as PowerShell and JavaScript. PowerShell alone was involved in nearly a quarter of execution activity.

![Chart showing Execution-related TTPs observed in 2023]

#### Persistence
In 32.8% of customer incidents, attackers abused scheduled tasks to maintain access to a compromised system. The second most-observed technique for persistence, accounting for 23.1% of cases, involved the MITRE technique known as boot or logon autostart execution: registry run keys / startup folder.

![Chart showing Persistence-related TTPs observed in 2023]

#### Privilege Escalation
Threat actors often exploit the trust placed in valid accounts to gain greater access to an organization’s network or systems. Acquiring valid account credentials, whether for domain (24.1% of the cases in our data set) or local (10.3%) accounts, can be achieved in various ways.

![Chart showing Privilege-escalation–related TTPs observed in 2023]

#### Defense Evasion
To avoid detection during an attack, threat actors used obfuscated commands in payloads 23.5% of the time. In 6.4% of customer incidents, we detected the use of masquerading techniques, particularly in the dissemination of SocGholish malware.

![Chart showing Defense-evasion–related TTPs observed in 2023]

#### Discovery
The most commonly observed TTPs were system information discovery and system owner/user discovery, each making up 11% of discovery-related customer incidents.

![Chart showing Discovery-related TTPs observed in 2023]

#### C2 Activity
During the reporting period, 44.2% of C2 activity used HTTPS to establish communication with compromised systems. In 35.8% of customer incidents, threat actors opted for ingress tool transfer to move sophisticated tools (e.g., netscan, Rclone, BloodHound) onto compromised systems.

![Chart showing C2-related TTPs observed in 2023]

#### Lateral Movement
RDP was seen in 34.3% of lateral-movement activity in our customer incidents. When combined with SMB, these protocols accounted for 59.3% of all lateral movement activity.

![Chart showing Lateral-movement–related TTPs in 2023]

#### Impact
Financial theft stood out as the primary objective in 2023, driving 88.4% of customer incidents.

![Chart showing Impact-related TTPs in 2023]

---

## What We Observed & Forecast
This section provides an overview of the significant threats targeting our customers in 2023, case studies, and a forecast for 2024, covering:
- Extortion
- Social engineering
- Malware-free and LotL activity
- TTP evolution

---

## Business Email Compromise Making a Big Impact
In 2023, ReliaQuest observed a significant increase in BEC attacks. BEC typically involves sending phishing emails to deceive employees into making payments for fraudulent bills. Threat actors typically rely on a generic credential harvester, combined with an AITM component, to bypass MFA.

### Case Study: Storm-1167’s AITM Phishing Campaign Brings BEC
In October 2023, ReliaQuest notified a customer of an incident where an attacker sent more than 1,000 phishing email messages to the customer’s users via a compromised third-party business email account.

- **Initial Access**: Deployed an AITM phishing kit; sent phishing emails that resulted in compromised credentials.
- **Execution**: Relied on user interaction by using a phishing email to induce the recipient to click a malicious link.
- **Defense Evasion**: Created email rules to auto-forward emails containing specific keywords to a designated folder.
- **Lateral Movement**: Conducted internal spearphishing.
- **Collection & Credential Access**: Hosted a malicious Microsoft credential harvester.

---

## Extortion Threat Looms Large
In 2023, ransomware and other means of cyber extortion persisted as significant threats to organizations, with more than 4,800 companies named on dark-web data-leak websites. That’s 74.3% more than were named in 2022.

![Chart showing number of companies named on data-leak sites of the 20 most prolific ransomware groups in 2023]

### Case Study: Commercial Tools Lead to Ransomware Encryption
In April 2023, ReliaQuest tackled an active intrusion in which an attacker was exploiting Windows shell and PowerShell. They used Total Software Deployment software for lateral movement and RMM tool ConnectWise ScreenConnect for persistence.

---

## Social Engineering
Throughout 2023, social engineering, such as phishing and pretexting, continued to be the most common route to achieving initial access. Phishing was used in 70% of all initial-access–related incidents.

### Case Study: Scattered Spider Uses Social Engineering for Initial Access
In September 2023, ReliaQuest identified an indicator of compromise (IoC) during an automated retroactive threat hunt in a customer environment. The group had deceived a help-desk employee into resetting an IT administrator’s credentials.

---

## Malware-Free and LotL Activity
In 2023, LOLBins accounted for a large portion (22.3%) of all critical security incident detections; fileless malware accounted for 86.2%. The LOLBins we detected the most were: Rundll32, Msiexec, and Mshta.

### Case Study: Threat Actor Gains Access via IT Support, Relies on Windows Utilities
In March 2023, ReliaQuest investigated credential dumping on hosts in our customer’s environment. The attacker gained access through a compromised IT support vendor host with a VPN connection.

---

## Reference List
(Content omitted in source)

## Appendix A: Methodology
(Content omitted in source)

## Appendix B: Endnotes
[^1]: True positive: An incident that has been verified as a malicious event.
[^2]: Scheduled tasks: A Windows feature that allows users to automate the execution of programs or scripts.
[^3]: Registry run keys / startup folder: Locations in the Windows registry or file system that allow programs to run automatically at system startup.
[^4]: Live off the land (LotL): The use of legitimate system tools and binaries to perform malicious activities.
[^5]: RDP: Remote Desktop Protocol.
[^6]: AITM: Adversary-in-the-Middle.
[^7]: FBI Internet Crime Report 2022.
[^8]: Dwell time: The duration an attacker remains undetected within a network.
[^9]: Reports of AI-generated voice fraud.
[^10]: Reports of video-call deepfakes.
[^11]: Double extortion: The practice of encrypting data and threatening to leak it if a ransom is not paid.
[^12]: Big game hunting: Targeting large, high-value organizations for ransomware.
[^13]: Ransomware profit estimates.
[^14]: Data-leak websites: Sites used by ransomware groups to publish stolen data.
[^15]: Affiliate: A member of a ransomware-as-a-service (RaaS) program.
[^16]: Windows shell: The command-line interface for Windows.
[^17]: PowerShell: A task automation and configuration management framework.
[^18]: Active Directory (AD): A directory service for Windows domain networks.
[^19]: Forum posts regarding affiliate recruitment.
[^20]: Pretexting: Creating a fabricated scenario to manipulate a victim into divulging information.
[^21]: MFA fatigue: Bombarding a user with MFA prompts until they approve one.
[^22]: Fileless malware: Malware that operates in memory and does not rely on traditional files on disk.
[^23]: Snap-ins: Administrative tools used in the Microsoft Management Console (MMC).
[^24]: Hands-on-keyboard: Manual, interactive activity by a threat actor.
[^25]: Compromising network equipment: Targeting routers, firewalls, or VPN appliances.

---

campaigns. We can expect this trend to continue in 2024, as threat
actors attempt to make their operations stealthier and untraceable.
TTP Evolution
Threat actors consistently adapt and develop new TTPs, and the most notable
technological advancement in 2023 was with AI. Many businesses are now
using AI to automate manual or repetitive tasks, but threat actors have also
started exploring ways to use AI to enhance their operations and expedite
tasks through automation. (See General Recommendations and Best Practices
section for mitigation steps.) The total is
now more than
The Threat 36 billion, with
The evolution of TTPs has resulted in a growth in cyber threats in 2023. In 2020, 6 billion new
we reported discovering 15 billion credentials originating from data breaches
credentials leaked
shared on the dark web and criminal forums, and that number has escalated:
over the past year.
The total is now more than 36 billion, with 6 billion new credentials leaked
over the past year. As previously mentioned, threat actors frequently use these
stolen credentials to gain initial access or launch credential stuffing attacks.
The Following Factors Brought Notable Advancements to TTPs in 2023:
AI garnered significant attention among major cybercriminal forums, including XSS, Exploit, and BreachForums.
The establishment of a dedicated AI and machine-learning section on XSS underscores the growing interest in
weaponizing this technology.
Criminal-focused alternatives to mainstream chatbots, such as FraudGPT and WormGPT (see Figure 17), also
suggest an alarming trend of using AI for nefarious purposes; discussions have hinted at the development of
simple malware and distributed denial of service (DDoS) queries using these options.
Make Security Possible
33

Numerous ransomware groups have started
incorporating automation during various
stages of their attacks, with the idea that
targeting a single organization can lead to
the infiltration of many:
• In the reconnaissance stage, threat
actors may use tools to search the
internet for details that would help create
more convincing spearphishing emails.
Or they might use penetration-testing
tools to automate the identification of
externally facing vulnerabilities. The Clop
group frequently employed such tactics
to determine potential targets prior to
launching GoAnywhere and MOVEit
campaigns.
• In a Bring Your Own Vulnerable Driver
(BYOVD) attack26 we observed in September, Figure 17: Screenshot of BreachForums post whose author
automation helped during the enumeration claims they used WormGPT to create working DDoS queries
stage to sift through data from numerous
breaches (see case study below), effectively identifying valuable information.
• Automation continues to aid credential stuffing attacks, which pose a significant risk of account takeover,
given the prevailing lack of robust authentication controls across various services.
• ReliaQuest has observed automation to greatly increase the timeliness of the attack chain, this includes
the mass exploitation of the CitrixBleed vulnerability.
The Israel–Hamas conflict has led to a new wave of destructive hacktivism. Numerous ideologically motivated groups
emerged in 2023 to support Israel or Palestine. Their methods resembled those of pro-Russian hacktivists, but attacks
also involved data theft and leaks. The “Cyber Toufan” group exfiltrated data and attempted to wipe it from the servers
and backup servers of Israeli companies, leading to extended operational downtimes. The group claimed breaches
against hundreds of Israeli companies and more than 1,000 servers and began leaking breached data on November 18.
Stopping TTPs
Regularly update threat-intelligence Share information with industry peers
feeds to ensure timely information and government entities in a collaborative
on emerging threats. approach to threat intelligence.
Continually as sess security
Integrate threat intelligence with Train security teams to
measures to identify and close
security tools for automated analyze and apply threat
potential gaps that could be
defense updates. intelligence effectively.
exploited with new TTPs.
Make Security Possible
34

Case Study:
BYOVD Attack
Used to Bypass
EDR
In September 2023, ReliaQuest detected a suspicious process from the Windows debug directory of a
customer’s environment. Investigation revealed an attacker bypassing detection using a BYOVD strategy,
exploiting a legitimate but vulnerable driver.
This attack highlighted an evolution in cyber-threat TTPs: Automation applied during the enumeration
stage was used to mine data from multiple breaches.
Initial To initially access the targeted organization, the attacker exploited the NetScaler
Access ADC vulnerability CVE-2023-3519 to execute code on a NetScaler appliance.
To execute code in the customer’s environment, the attacker used PowerShell
Execution
and system services for command execution and evasion.
Defense To delay detection and maintain access, the attacker ingressed a vulnerable driver
Evasion with a valid signature to exploit a code flaw and disable the EDR solution.
Make Security Possible
35

To gather information about the customer’s environment, the attacker ingressed
Discovery
a tool to collect information on the OS, BIOS, and registry key values.
Lateral To access additional accounts and increase their footprint within the environment,
Movement the attacker used Impacket’s WMIEXEC module and a privileged service account.
To establish communication with compromised systems, the attacker:
C2 Activity
• Ingressed PowerShell scripts for automated enumeration.
• Generated outgoing C2 traffic to malicious hosts.
To perform extortion, the attacker encrypted files and left a ransom note
Impact
demanding contact within a set timeframe.
Make Security Possible
36

Forecast
Cybersecurity in 2024 will be heavily influenced by GenAI and the creation of malicious AI models,
and widespread automation in cyber attacks that enhance threat actors’ capabilities. Automated
dynamic playbooks will grant even unskilled attackers sophisticated ways to expedite operations,
shortening the time from breach to impact. Countering these evolving threats will require innovative
defense strategies and technologies; security defenders must accelerate their detection and response
measures to keep pace.
The UK’s National Cyber Security Centre (NCSC) anticipates a significant surge in AI-fueled cyber threats within the next
two years27. Expect more targeted social-engineering attempts and less detection, sophisticated malware innovations,
and an uptick in cybercrime driven by AI-assisted techniques.
In 2024, GenAI Will Likely be Used to Automate and Fine-tune These Aspects of Threat Campaigns:
Phishing: GenAI will likely be used in social-engineering
campaigns, to create realistic-looking phishing emails.
GenAI can read HTML from a webpage and generate fake
login pages or websites that closely resemble authentic ones.
Malware: GenAI can assist with coding to accelerate
software development and testing and can also
assist malware developers.
Vulnerability Identification: GenAI algorithms can analyze
massive amounts of data and identify potential vulnerabilities
much more efficiently than a human can.
Defense Evasion: GenAI could be used to identify
and create advanced techniques to bypass traditional
security measures.
Automation: GenAI can automate campaign workflows,
processing large amounts of data and generating results within
seconds. GenAI will also likely help develop tools that automate
complex tasks for threat actors.
Make Security Possible
37

Conclusions &
Recommendations
In this section, we present conclusions based on the metrics and
analysis covered in earlier sections, highlighting threats that defenders
will grapple with in 2024.
We also offer recommendations and best practices, building on commonly
observed MITRE ATT&CK techniques to suggest precise and impactful
actions for security defenders.
Make Security Possible
38

Conclusions Based on 2023 Data and Analysis
From the insights described in this report, it’s clear that cyber-threat actors employ a wide range of techniques,
selecting whatever is appropriate to infiltrate specific systems and networks.
They might be influenced by several factors, including their motives, geopolitical tensions, and the availability
of ever-advancing tools and techniques. To form appropriate defense strategies for 2024, security teams should
pay particular attention to the following observations of 2023 threat activity.
Smarter Social Engineering
Social-engineering tactics will almost certainly become increasingly clever and
personalized with the help of advanced AI. Phishing messages could become
indistinguishable from legitimate communication, and imitation websites near-
perfect replicas. For organizations, the risk is high as these convincing fakes are
difficult to spot.
The burgeoning use of deepfakes—AI-generated audio and video—could dupe
even more individuals into making fraudulent payments and falling victim to BEC.
Consequently, organizations urgently need to move beyond traditional security
training and upgrade authentication methods. Strengthening defenses with
biometric verification, adaptive authentication, and shorter token lifetimes, for
example, has become vital to protect against these nuanced threats.
Ransomware Adapting
Ransomware is expected to continue to be the predominant danger facing
organizations in 2024. Its alarming growth last year—up 74.3% from 2022—meant
an unprecedented scale of attacks and inventive extortion tactics, such as ALPHV
reporting victims to the SEC.
As ransomware tactics evolve rapidly, organizations must safeguard operations
by maintaining up-to-date software, ensuring networks are properly segmented,
managing risks from third-party vendors, and integrating extended detection and
response (XDR) solutions for timely attack detection and response.
Make Security Possible
39

Next Steps
As the cyber-threat landscape continues to evolve in 2024, introducing new threats that use automation, AI, and evolving
TTPs, defenders must remain vigilSatneta altnhdy uLpo ttLo adnadte M oanl wthaer ela-tFersete c Aybttearc tkhsr eats. To proactively make security possible,
companies should implement the preventative measures outlined in General Recommendations and Best Practices.
LotL tactics and malware-free attacks accounted for 86.2% of the major threats
we addressed in 2023. That activity, being notoriously hard to identify, should
present a significant challenge in 2024. To guard against such stealthy attacks,
enforce Group Policy Objects (GPOs) to block remote interactive logins, use device
certificates for secure remote authentication, limit unsanctioned connections via
firewalls or proxies, and proactively hunt for fileless malware.
Phishing for Initial Access
Analysis of true-positive incidents detected by GreyMatter revealed a heavy reliance
on phishing to gain initial access. Implementing fundamental controls, such as
robust email filters and MFA, can significantly enhance cyber resilience against
phishing attacks. Educating users will help, but prioritizing technical defenses
will more immediately and substantially reduce phishing-related breaches.
Users Allowing Access
From our critical security incidents data, we observed that user actions aided
initial attacker access in most cyber-threat events affecting customers. Attackers
solicited user interaction via spearphishing, drive-by compromise, and malicious
USB activity, among other efforts. To mitigate such risks, teach users how to
identify and respond to these tactics.
Make Security Possible
40

C2 Through HTTPS
C2 of compromised devices was usually achieved through HTTPS activity,
which security tools often permit by default and which blends in with
legitimate traffic. Consider more stringent monitoring of HTTPS traffic
and enhancing anomaly-detection measures to distinguish benign from
malicious communications.
Scheduled Persistence
Threat actors most commonly used scheduled tasks to facilitate persistence on
targeted devices. Malicious activity under the guise of scheduled tasks commonly
goes undetected amid other, legitimate processes. To counteract this, enhance
monitoring of scheduled tasks, applying behavioral analytics to detect anomalies
and differentiate between genuine and malicious activities.
RDP Abuse
Abusing remote services was a popular way to gain initial access in 2023, and
abusing susceptible instances of RDP was the most observed method of lateral
movement. Unsecured instances of RDP can present an enormous opportunity
by opening up additional areas of a network. Threat actors have taken advantage
of vulnerable RDP connections to spread ransomware more extensively
throughout networks.
As the cyber-threat landscape continues to evolve in 2024, introducing new threats that use
automation, AI, and evolving TTPs, defenders must remain vigilant and up to date on the
Next Steps
latest cyber threats. To proactively Make Security Possible, companies should implement
the preventative measures outlined in General Recommendations and Best Practices.
Make Security Possible
41

General Recommendations
and Best Practices
In addition to the advice provided throughout this report,
the ReliaQuest Threat Research Team offers the below
recommendations and best practices. Though not an exhaustive
list, these are the most beneficial steps to establish a secure
foundation and harden your environment against the general
threats and TTPs mentioned in this report.
MITRE ATT&CK Technique Mitigation:
1) Initial Access:
• Deploy EDR for immediate scanning and behavioral analysis.
• Use Content Security Policy (CSP) headers to block unauthorized resource loads and prevent
drive-by attacks.
• Enforce application control via GPOs to restrict software execution from removable media.
• Integrate interactive application security testing (IAST) tools for real-time vulnerability analysis
in public-facing apps.
2) Execution:
• Enable command-line auditing to track shell activity and raise alerts of anomalies.
• Activate PowerShell Constrained Language Mode with logging to limit and monitor script use.
• Install script management browser extensions to control and block untrusted scripts.
• Implement application allowlisting to ensure only verified applications run.
3) Persistence:
• Centralize task management for regular validation of authorized network tasks.
• Use configuration tools to guard Registry Run keys and startup items and to raise alerts for
unauthorized changes.
• Regularly audit accounts and review permissions to prevent excess access and identify misuse.
Make Security Possible
42

4) Privilege Escalation:
• Use OSquery for advanced disk inspection and system insights.
• Integrate identity and access management (IAM) with risk-based MFA for secure user access and changes.
• Perform behavioral analysis to identify unusual processes and block unauthorized code.
• Apply application allowlisting to load only authorized Dynamic Link Libraries (DLLs) and hinder sideloading.
• Strengthen device registration and management with strict security policies and auditing.
5) Defense Evasion:
• Employ threat detection with machine learning to identify and scrutinize obfuscated commands or files.
• Monitor system binaries for atypical use patterns that indicate proxy execution with security tools.
• Use EDR with memory scanning to detect and counteract reflective code loading.
• Implement file integrity monitoring to notice file or log changes that could signal potential tampering.
• Enforce naming convention rules through security policies to counteract masquerading techniques.
6) Discovery:
• Control and audit the use of system info-gathering tools and common discovery commands.
• Limit user permissions to block commands that reveal system ownership and log all attempts.
• Strengthen access controls for directory services with anomaly detection for unusual patterns.
• Regularly audit and monitor Active Directory trust relationships, limiting query abilities to authorized users.
7) C2 Channels:
• Enforce blocks on unauthorized RMM applications, using access control lists (ACLs) and firewalls to
oversee RMM traffic.
• Use Deep Packet Inspection (DPI) to detect and stop C2 traffic masquerading as normal web activity.
• Deploy network-based intrusion detection systems (NIDS) to spot atypical data flows hinting at tool or
payload transfers.
• Scrutinize outbound traffic to popular web services for potential data exfiltration or C2 communications.
• Routinely analyze traffic to uncover and probe activity on non-standard ports.
Make Security Possible
43

8) Lateral Movement:
• Activate Network Level Authentication (NLA) for RDP and use network controls to prevent unauthorized
lateral movement.
• Use ACLs and firewalls to limit SMB traffic to essential systems and users; disable admin shares
if unnecessary.
• Manage SSH keys with rigorous rotation policies and watch for irregular SSH session activity.
• Keep remote service apps patched; mandate strong passwords and MFA.
• Track file and data transfers across the network with DLP technologies, focusing on tool movements.
9) Impact:
• Secure financial transactions with anomaly detection and trigger extra verification for irregular activities.
• Use advanced ransomware protection with behavior detection and machine learning to block encryption
in real time.
• Implement cryptographic integrity checks, such as via digital signatures or hashing, for data protection.
• Monitor CPU usage with endpoint detection to identify and prevent cryptojacking.
Business Email Compromise Mitigation
Verify Transaction Requests: Monitor High-Risk Users:
Implement a dual authorization policy whereby a Develop detection rules for high-risk users when
manager or coworker must authorize large payments creating email inbox rules, allowing for a tuning period
or banking changes. Require that employees have of at least 30 days to increase the rule fidelity.
an alternative line of communication, besides email,
with individuals requesting transactions to prevent
unauthorized transfers. Create a BEC Alert Playbook:
Develop a playbook of steps to inform third-party providers
and partners about potential BEC phishing emails,
Block Newly Registered Domains: ensuring quick response to limit a compromise’s scope.
Configure forward proxy devices to block domains,
using categories like “newly registered domains.”
Educate Employees:
This helps prevent BEC operators from using Teach employees to scrutinize email headers,
links, and attachments and to report any
recently registered domains.
suspicious activity.
Make Security Possible
44

Extortion Mitigation
Implement Canary Tokens: Use Application Control:
Canary tokens provide high-fidelity, low-cost, Because weaponized script files are used heavily by
easy-to-implement security measures. These initial-access malware, only permit the execution of signed
tokens are embedded into files and trigger alerts scripts wherever appropriate and possible. Consider
whenever an attacker accesses them, allowing redirecting the default application for JavaScript, Visual
the early detection of potential breaches and Basic, and other executable script formats to open by
enhancing overall security. default in notepad.exe instead of wscript.exe.
Apply a Defense-in-Depth Strategy: Restrict PowerShell use:
Focus on defense measures that track TTPs, Use GPOs to restrict PowerShell use to only
ensure your environment’s visibility, and implement specific users or administrators who manage
multiple security controls to detect and prevent a network or Windows operating system.
ransomware activity.
Monitor External-Facing Assets: Keep all Operating Systems, Software,
and Firmware up to Date:
Threat actors frequently scan the internet for
public-facing assets that have exploitable Regularly update and patch all operating systems,
vulnerabilities that can grant them initial access. Remedy software, and firmware. Prioritize patching known
any accidental exposure and patch out-of-date services, exploited vulnerabilities within any internet-facing
prioritizing services that have known vulnerabilities. systems.
Social Engineering Mitigation
Harden MFA Mechanisms: Implement a certificate-based authentication policy. Use digital certificates to verify
the authenticity of users during the authentication process. Additionally, consider limiting the token lifetimes for
MFA—by setting a shorter timeframe, you reduce the window of opportunity for attackers to exploit them.
Add or use Alternative Authentication Factors: Consider implementing biometrics and adaptive authentication.
Biometrics can include features like fingerprint or facial recognition, and adaptive authentication verifies users
based on multiple factors, such as location, user behavior, and registered device.
Train Employees: Develop regular training sessions and simulation exercises to teach employees how to recognize
and report social engineering attempts, such as phishing emails, phone calls, and in-person scams.
Enforce Password Security: Implement password policies requiring complex passwords (12-plus characters, uppercase,
lowercase, number, and symbol), prevent password reuse, enforce password changes every 90 days, and enable MFA.
Limit Access to Sensitive Information: Restrict information access to a need-to-know basis.
Make Security Possible
45

LotL and Malware-Free Mitigation
Set RDP Timeouts and Terminate Sessions: Use Threat Hunting Services:
Define RDP timeouts and enable session Threat hunting services can help actively search for
terminations via GPOs. Closing idle or unused indicators of fileless malware. Threat hunters can
connections promptly reduces the window of analyze system logs, network traffic, and other data
opportunity for attackers to hijack active RDP sources to identify potential threats that might go
sessions. unnoticed by traditional security tools.
Restrict Arbitrary Connections to the Internet: Run EDR in Prevent/Block Modes:
By configuring firewalls or proxies to restrict Configure EDR solutions to run in prevent/block
arbitrary connections from company assets to the modes rather than detect-only modes. This will
internet, you can minimize the risk of unauthorized actively prevent or block actions associated
communication channels that could be exploited with fileless malware.
by LotL malware.
Audit Service and Local Accounts:
Regularly audit service and local accounts, ensuring that each account has a documented owner and purpose.
Auditing helps establish accountability and reduces the risk of unauthorized access. Assigning owners and
verifying the purpose of each account ensures that only authorized individuals can access them.
Hacktivism Mitigation
Prepare for DDoS Attacks: Implement a DDoS mitigation strategy, which may include using cloud-based services, a CDN,
or an anti-DDoS solution from a reputable provider. Use load balancers to mitigate DDoS attack risks and web application
firewalls (WAFs) with dynamic blocking based on rate-based rules.
Enforce Proxies: Use proxies, dedicated Domain Name System (DNS) servers, and other services while allowing
communication only over their respective ports or protocols rather than all systems within a network.
Apply ACLs: Apply extended ACLs to block unauthorized protocols outside the trusted network.
Minimize Attack Surface: Reduce your organization’s internet-facing footprint to decrease vulnerability to attacks.
Monitor Outbound Connections to Tor (The Onion Router) Nodes: Regularly check for outbound connections
to Tor nodes and abnormal network traffic from your hosts, which may indicate data exfiltration attempts or
other malicious activity.
Make Security Possible
46

How ReliaQuest Can Help
Put our threat-intelligence technology to work for you.
With the ReliaQuest GreyMatter security operations platform, you
can get unparalleled visibility into your entire ecosystem, and beyond.
The GreyMatter Threat Intelligence capability is fully configurable; use
our pre-defined set of threat feeds or add your own.
We’ll take that data and return actionable insights on threats and IoCs.
Additionally, our Digital Risk Protection (DRP) service safeguards your
data even outside your environment. It incorporates a comprehensive
collection of cyber threats present across the clear, deep, and dark web.
ReliaQuest GreyMatter
is a cloud-native security
operations platform that Visit www.reliaquest.com or set up a custom demo to walk through your
integrates with existing environment and learn more about how ReliaQuest can help.
security technologies to
improve visibility, reduce
For any additional information on the threats detailed in this report,
complexity, and manage
contact ReliaQuest’s Threat Research Team.
security risks.
Reference List
This report is based solely on reporting that has aligned with ReliaQuest’s Threat Research Team’s intelligence
requirements and thresholds and additional open-source reporting; there may have been exposures and events falling
outside these parameters that are not included. In addition to our primary-source intelligence and the sources cited
throughout this report, we consulted the following.
Federal Bureau of Investigation Internet Crime Complaint Center, Internet Crime Report 2022 (hxxps://www.ic3[.]gov/
Media/PDF/AnnualReport/2022_IC3Report.pdf)
Andrea Blanco, “A Father Is Warning Others About a New AI ‘Family Emergency Scam,” The Independent, December 6,
2023 (hxxps://www.independent.co[.]uk/news/world/americas/ai-phone-scam-voice-call-b2459449.html)
Heather Chen and Kathleen Magramo, “Finance Worker Pays Out $25 Million After Video Call With Deepfake ‘Chief
Financial Officer’,” CNN, February 4, 2024 (hxxps://www.cnn[.]com/2024/02/04/asia/deepfake-cfo-scam-hong-kong-intl-
hnk/index.html)
Chainalysis, “Crypto Crime Mid-year Update: Crime Down 65% Overall, But Ransomware Headed for Huge Year Thanks
to Return of Big Game Hunting,” July 12, 2023 (hxxps://www.chainalysis[.]com/blog/crypto-crime-midyear-2023-update-
ransomware-scams/)
Microsoft Threat Intelligence, “Volt Typhoon targets US Critical Infrastructure With Living-Off-The-Land Techniques,” May
24, 2023 (hxxps://www.microsoft[.]com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-
with-living-off-the-land-techniques/)
NCSC, “The Near-Term Impact of AI on the Cyber Threat,” January 24, 2024 (hxxps://www.ncsc.gov.uk/report/impact-of-ai-
on-cyber-threat)
Make Security Possible
47

Appendix A: Methodology
The ReliaQuest Annual Cyber-Threat Report shows analysis of 2023’s security incidents, aligning them with the MITRE
ATT&CK framework and categorizing them by access vectors, malware, and attacker tools. It highlights trends vital
for developing robust defense strategies and enhances GreyMatter Detect’s threat response capabilities.
The report draws insights from two data sets:
Incident metrics comprises all true-positive incidents Incidents we consider elevated make up the data
identified by GreyMatter—incidents that customers of critical security incidents. This data set includes
have confirmed as true positives. These incidents activity related to extortion, espionage, custom
are access attempts, or actual unauthorized access, malware, hands-on-keyboard operations, and
to use, destruct, or alter information systems. Within commodity threats, among others. These incidents
these incident metrics, we compile data relating to typically involve sophisticated attack chains
the MTTR, which measures the average time taken and TTPs, often associated with high-profile
from incident escalation to customer resolution. attack attempts.
ReliaQuest GreyMatter for Threat Detection,
Investigation, and Response
Tuned detections that deliver high-fidelity alerts,
automation that speeds investigations, and playbooks
to streamline response
Transparent investigations in which your team
can participate
Optimal use of your investments across SIEM, endpoint,
network, cloud, and on-premises technologies
Holistic metrics across detection, investigation,
and response workflows
Limitations
GreyMatter intercepts most threats before actors get a chance to fully execute their campaigns; the data used in this
report therefore focuses predominantly on the early stages of the attack lifecycle. There may be compromises via an
unknown initial-access method, if occurring in environments to which GreyMatter has not been granted access.
Our analysis prioritizes the most prevalent threats and impact evident in our data. The data in this report is likely to have
a disproportionate focus on financially motivated cyber attacks, as they are indiscriminate and affect a broad range of
targets. We also identified incidents orchestrated by nation-state actors and APT groups, but they were often highly
targeted and stealthier.
Make Security Possible
48

Appendix B: Endnotes
1. A true-positive, or confirmed, incident is an event or alert related to malicious activity that led to unauthorized access
attempts, or use, modification, or destruction of any information system or data.
2. Scheduled tasks permit users to schedule specific programs or scripts to run at predetermined times or intervals.
3. hxxps://attack.mitre[.]org/techniques/T1547/001/.
4. LotL attacks use native tools that exist on a target system to obscure malicious activity and evade detection.
5. A secure network communications protocol that enables network administrators to remotely diagnose individual
user problems, and gives them remote access to their physical work desktop computers.
6. In an AITM cyber attack, the attacker positions themself in a conversation between two parties—two users, two
devices, or a user and an application or server—so that all communications are going to or through the attacker;
hxxps://attack.mitre[.]org/techniques/T1557/.
7. hxxps://www.ic3[.]gov/Media/PDF/AnnualReport/2022_IC3Report.pdf.
8. The length of time an attacker remains in an environment.
9. hxxps://www.independent[.]co.uk/news/world/americas/ai-phone-scam-voice-call-b2459449.html.
10. hxxps://www.cnn[.]com/2024/02/04/asia/deepfake-cfo-scam-hong-kong-intl-hnk/index.html.
11. Encrypting files while also exfiltrating sensitive data, with threats to publish the data unless a ransom is paid.
12. Threat campaigns focused on a small number of high-value targets to maximize potential profit and minimize the risk
of being observed or discovered by security researchers.
13. hxxps://www.chainalysis[.]com/blog/crypto-crime-midyear-2023-update-ransomware-scams/.
14. ReliaQuest released ransomware reports for the first, second, and third quarters of 2023.
15. Affiliates of ransomware developers receive customizable ransomware from the developers to conduct attacks in
exchange for a small cut of the profits.
16. The graphical user interface for the Windows operating system.
17. A Windows command-line shell designed especially for system administrators and built on top of the .NET Framework;
includes an interactive prompt and a scripting environment that can be used independently or in combination.
18. Microsoft’s directory service that stores data about objects on the local network, and records information about users,
devices, applications, and groups.
Make Security Possible
49

19. Affiliate “LockBitSupp” has since been banned from criminal forums after allegedly scamming an IAB: LockBit
claimed that there were no agreed-upon terms for a transaction, but, following a successful ransom payment, the IAB
demanded a specified percentage of the ransom, which LockBitSupp refused to pay.
20. Fabricating a false scenario, or pretext, to trick individuals into divulging sensitive information or granting access to
secure systems.
21. MFA fatigue attacks typically involve bombarding users with repeated authentication requests until they inadvertently
approve a fraudulent one.
22. Fileless malware uses scripts, not executables, to evade detection and carry out attacks within a system’s memory.
23. Extensions for management consoles that enable administrators to configure and monitor DNS settings directly from
a unified interface.
24. In which an attacker conducts a range of manual activities, including performing reconnaissance, elevating privileges,
and moving laterally.
25. hxxps://www.microsoft[.]com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-
living-off-the-land-techniques/.
26. In which attackers implant a legitimate-but-vulnerable driver into a targeted system, then exploit the driver to perform
a malicious action.
27. hxxps://www.ncsc.gov[.]uk/report/impact-of-ai-on-cyber-threat.
reliaquest.com 800.925.2159 info@reliaquest.com
Copyright © 2024 ReliaQuest, LLC. All Rights Reserved. ReliaQuest, GreyMatter, Digital Shadows, and all related logos, product and services names, designs, and slogans are trademarks or registered
trademarks of ReliaQuest, LLC or its affiliates or licensors. All other product names or slogans mentioned in this document may be trademarks or registered trademarks of their respective owners or
companies. The ReliaQuest software, platform, portal and its entire contents, features, and functionality are owned by ReliaQuest, LLC and its affiliates. These materials are protected by United States
Manda inkteern Satieoncaul croiptyyrig Pht,o trsadseimbalrke, patent, trade secret, and other intellectual property or proprietary rights laws. All other information presented is provided for informational purposes with no
representations or warranties provided of any kind and should not be relied upon for any purpose. ReliaQuest has no obligation to amend, modify, or update the information contained in this document 50
in the event that such information changes or subsequently becomes inaccurate. Printed in the USA.