# Table of Contents

- [Introduction](#introduction)
- [Naming Conventions](#naming-conventions)
- [Front-Line Snapshot](#front-line-snapshot)
- [Sector Targeting](#sector-targeting)
- [Sector Spotlights](#sector-spotlights)
- [MITRE ATT&CK Observations](#mitre-attck-observations)
- [Intrusion Trends by Adversary](#intrusion-trends-by-adversary)
- [Observations from the Front Lines](#observations-from-the-front-lines)
- [Countering the Adversary: Generative Artificial Intelligence](#countering-the-adversary-generative-artificial-intelligence)
- [Hunting Cross-Domain Adversaries](#hunting-cross-domain-adversaries)
- [Case Study: Disrupting BLOCKADE SPIDER](#case-study-disrupting-blockade-spider)
- [Case Study: Hunting OPERATOR PANDA](#case-study-hunting-operator-panda)
- [Identity Hunting](#identity-hunting)
- [Adversary Spotlight: SCATTERED SPIDER](#adversary-spotlight-scattered-spider)
- [Cloud Hunting](#cloud-hunting)
- [Case Study: Hunting GENESIS PANDA Across the Cloud Control Plane](#case-study-hunting-genesis-panda-across-the-cloud-control-plane)
- [Case Study: MURKY PANDA’s Abuse of Trusted Relationships](#case-study-murky-pandas-abuse-of-trusted-relationships)
- [Endpoint Hunting](#endpoint-hunting)
- [Case Study: Hunting GLACIAL PANDA Living off the Land](#case-study-hunting-glacial-panda-living-off-the-land)
- [Vulnerability Hunting](#vulnerability-hunting)
- [Case Study: Hunting GRACEFUL SPIDER’s Zero-Day](#case-study-hunting-graceful-spiders-zero-day)
- [Conclusion](#conclusion)
- [Recommendations](#recommendations)
- [CrowdStrike Falcon Platform](#crowdstrike-falcon-platform)
- [CrowdStrike Products](#crowdstrike-products)
- [CrowdStrike Services](#crowdstrike-services)
- [About CrowdStrike](#about-crowdstrike)

# Introduction

A new era of cyber threats has emerged with the rise of the “enterprising adversary,” as highlighted in the CrowdStrike 2025 Global Threat Report. This new breed of threat actor distinguishes itself through sophisticated and scalable tactics designed to execute attacks with calculated, business-like efficiency. These adversaries operate with strategic precision to maximize impact and quickly achieve their goals.

Innovation is a critical cornerstone to outmaneuver and disrupt the enterprising adversary. Novel technologies and threat hunting are required to anticipate the adversary's next moves, understand their evolving methodologies, and adapt defenses to stay ahead.

Today's enterprising adversary is adept at bypassing traditional cybersecurity defenses. They understand the limitations of conventional safeguards and seek to exploit security weaknesses and vulnerabilities that established systems and processes often overlook. This includes exploiting human factors through sophisticated social engineering techniques — now often enhanced by AI — and moving to unmanaged devices, which are often significant blind spots in an organization's security posture. By targeting devices outside the direct purview of IT departments, they can establish footholds, exfiltrate data, or launch further attacks without immediate detection.

The CrowdStrike Counter Adversary Operations team brings together industry-leading threat intelligence and best-in-class managed threat hunting with the AI-powered CrowdStrike Falcon® platform to detect, disrupt, and stop enterprising adversaries. Counter Adversary Operations comprises two closely integrated teams. The CrowdStrike Intelligence team provides actionable reporting that identifies new adversaries, monitors their activities, and captures emerging cyber threat developments in real time. The CrowdStrike OverWatch team uses this intelligence to conduct proactive threat hunting across customer telemetry to detect and address malicious activity. Together, these teams protect thousands of customers from the most sophisticated adversaries by providing the intelligence and threat hunting skills and resources that most organizations lack.

Enterprising adversaries are using generative AI (GenAI) to enhance their operations, underscoring the critical need for innovative defensive strategies. The integration of GenAI into insider threat operations by Democratic People’s Republic of Korea (DPRK)-nexus adversary FAMOUS CHOLLIMA rapidly made them the most GenAI-proficient adversary. FAMOUS CHOLLIMA IT workers use GenAI to create attractive résumés for companies, reportedly use real-time deepfake technology to mask their true identities in video interviews, and leverage AI code tools to assist in their job duties, all of which pose a substantial challenge to traditional security defenses.

Adversaries continually seek to stay undetected by moving to unmanaged networks and expanding their reach. Cross-domain threat hunting is critical, as adversaries increasingly operate across multiple domains — such as identity, endpoint, and cloud — in their efforts to evade detection. These cross-domain threats often generate fewer detections in a single domain or product, making the activity difficult to recognize as malicious. To stay ahead of sophisticated cross-domain adversaries such as BLOCKADE SPIDER and OPERATOR PANDA, CrowdStrike OverWatch hunters are expanding their hunting grounds with innovative next-gen security information and event management (SIEM) technology to capture adversaries’ every move.

Though adversaries that prioritize rapid execution have the most visible and immediate impact, those that emphasize stealth, prolonged presence, and the meticulous execution of a “long game” approach present an equally potent threat. These operations often include sustained access, covert data harvesting, and — in some cases — preparing a victim’s environment for future, more impactful operations. China-nexus adversaries such as GLACIAL PANDA have increasingly excelled at this approach. GLACIAL PANDA primarily targets the global telecommunications sector through patient and methodical infiltration, established persistence, and deep, quiet reconnaissance of target networks, systems, and data. The challenge in detecting these stealthy adversaries is amplified by their minimal digital footprint, allowing them to easily blend into legitimate network traffic. CrowdStrike OverWatch successfully disrupts them by conducting customized hunts that uncover trojanized software and malicious code and focusing on repeated attempts to access sensitive data sources.

In the first half of 2025, CrowdStrike OverWatch identified a 136% increase in cloud intrusions compared to all of 2024, highlighting the fact that more threat actors are becoming versed in exploiting cloud environments. China-nexus adversaries in particular have quickly gained proficiency in cloud exploitation techniques; GENESIS PANDA and MURKY PANDA, for example, have become adept at navigating cloud environments. Over the past 12 months, CrowdStrike OverWatch observed a 40% increase in cloud intrusions attributed to China-nexus adversaries. CrowdStrike OverWatch keeps pace by developing innovative hunting techniques for cloud services, workloads, and control planes as well as leveraging advances in identity protection.

In the CrowdStrike 2025 Global Threat Report, CrowdStrike reported that voice phishing (vishing) attacks increased by 442% from the first to the second half of 2024, marking a significant and effective evolution in eCrime tactics. This trend has not slowed down in the first half of 2025, where vishing attacks have already surpassed the total number seen in 2024. These attacks are successful because they exploit human vulnerabilities and leverage compromised credentials and social engineering to bypass traditional security measures, gain initial access, and move laterally within organizations at speed. One of the earliest adopters of this tactic is SCATTERED SPIDER, an eCrime adversary well known for their sophisticated social engineering and credential theft techniques. In 2025, this adversary exploded back into the eCrime landscape, and though they showcased some new techniques, help desk attacks have remained a prominent tool in SCATTERED SPIDER’s arsenal.

Also noted in the CrowdStrike 2025 Global Threat Report, 52% of vulnerabilities observed by CrowdStrike in 2024 were related to initial access. Adversaries continue to exploit internet-exposed applications for initial access. When adversaries like GRACEFUL SPIDER develop zero-day exploits, CrowdStrike OverWatch's ability to identify and hunt for post-exploitation malicious behaviors becomes a critical fail-safe, ensuring rapid and effective coverage against widespread exploitation.

The CrowdStrike 2025 Threat Hunting Report highlights key trends and shifts the CrowdStrike OverWatch team observed over the past 12 months and details how CrowdStrike Falcon® Adversary OverWatch™ leverages innovation and proactive, intelligence-informed threat hunting to track, detect, and disrupt the adversary. This year’s report presents trends the team identified from July 1, 2024, to June 30, 2025. In this time frame, CrowdStrike OverWatch observed the following:

- 81% of interactive intrusions were malware-free.
- Interactive (hands-on-keyboard) intrusions increased 27% year-over-year, highlighting that adversaries are innovating their operations to bypass legacy detection methods.
- eCrime activity represented 73% of total interactive intrusions.
- Cloud intrusions increased 136% in the first half of 2025 compared to all of 2024.
- CrowdStrike OverWatch observed a 40% year-over-year increase in intrusions by suspected cloud-conscious China-nexus actors.
- In the first half of 2025, vishing attacks already surpassed the total number seen in 2024.
- The government sector was affected by a 71% year-over-year increase in overall interactive intrusions and a 185% year-over-year increase in targeted intrusion activity.
- FAMOUS CHOLLIMA insiders infiltrated over 320 companies in the last 12 months — a 220% year-over-year increase — by leveraging GenAI at every stage of the hiring and employment process.
- SCATTERED SPIDER accelerated their operations — in one incident, the adversary moved from account takeover to ransomware deployment in just 24 hours, 32% faster than they were able to accomplish this in 2024.

This report showcases the Counter Adversary Operations team’s relentless pursuit to disrupt the adversary. In CrowdStrike customer environments, adversaries face a unified security solution that empowers every CrowdStrike threat hunter with extensive security telemetry — spanning endpoint, identity, cloud, and next-gen SIEM, along with integrated intelligence — to detect and disrupt threats quickly and effectively.

# Naming Conventions

| NATION-STATE OR CATEGORY | ADVERSARY |
| :--- | :--- |
| RUSSIA | BEAR |
| VIETNAM | BUFFALO |
| DPRK (NORTH KOREA) | CHOLLIMA |
| ROK (REPUBLIC OF KOREA) | CRANE |
| SYRIA | HAWK |
| HACKTIVIST | JACKAL |
| IRAN | KITTEN |
| PAKISTAN | LEOPARD |
| GEORGIA | LYNX |
| COLOMBIA | OCELOT |
| PEOPLE’S REPUBLIC OF CHINA | PANDA |
| KAZAKHSTAN | SAIGA |
| EGYPT | SPHINX |
| eCRIME | SPIDER |
| INDIA | TIGER |
| TÜRKIYE | WOLF |

# Front-Line Snapshot

The statistics provided in this report specifically focus on interactive intrusions — attacks where adversaries establish an active presence within a target network, often engaging in hands-on-keyboard activities to achieve their objectives. Unlike automated attacks, interactive intrusions involve human operators who interact with systems in real time, adapting their tactics as needed. They are typically more sophisticated and difficult to detect than automated attacks, and they require advanced threat hunting and incident response capabilities to identify and mitigate.

![Anatomy of an interactive intrusion: Manual Intervention, Persistence, Lateral Movement, Data Exfiltration, and Customization]

Over the past 12 months, CrowdStrike OverWatch observed interactive intrusions continue to climb, increasing 27% year-over-year. The overall distribution of interactive intrusion activity by threat type saw a noted increase in eCrime: 73% of the total 2025 reporting period volume was associated with eCrime activity, highlighting the persistent and pervasive threat of adversaries seeking financial gain.

![Interactive intrusions by frequency chart, top sectors by intrusion frequency, and interactive intrusions by motivation chart]

# Sector Targeting

The technology sector remained at the top of the list for the reporting period, making technology the most frequently targeted industry for the eighth consecutive year. This sector encompasses a broad range of organizations that develop computer software and hardware or provide IT services or technology. Due to its relationship to many other sectors, the technology sector is a high-value target for both nation-state and eCrime adversaries.

![Top targeted sectors by intrusion frequency and Nation-State vs. eCrime comparison charts]

The government and telecommunications sectors saw a significant increase in interactive intrusions during the reporting period, namely by nation-state adversaries. Russia-nexus activity accounted for most of the government targeting, while China-nexus activity accounted for most of the telecommunications targeting.

# Sector Spotlights

### Government
CrowdStrike observed a 71% increase in overall interactive intrusions and a 185% increase in nation-state activity within the government sector over the past 12 months. Though the government sector is consistently a high-value target for a variety of nation-state adversaries, this significant increase is attributed to activity conducted by Russia-nexus adversaries such as PRIMITIVE BEAR and VENOMOUS BEAR, who conduct suspected espionage operations against Ukraine government entities in direct support of the conflict in Ukraine.

### Telecommunications
CrowdStrike observed a 53% increase in overall interactive intrusions and a 130% increase in nation-state activity within the telecommunications sector over the past 12 months. This activity has primarily focused on entities in countries across Asia and North America. It is directly related to a surge in China-nexus adversaries’ operations against the telecommunications industry, which have become the most significant and consistent targeted intrusion threat to this sector over the past year. The telecommunications sector is a high-value target for nation-state adversaries, providing access to subscriber and organizational data that supports their intelligence collection and counterintelligence efforts. Telecommunication network access can also enable intrusion vectors and traffic collection against downstream customer organizations that obtain connectivity from the provider.

### Manufacturing and Retail
CrowdStrike observed notable increases in eCrime interactive intrusions targeting the manufacturing (55%) and retail (41%) sectors over the past 12 months. CURLY SPIDER emerged as a prominent threat actor conducting intrusions against North America-based retail and manufacturing entities at an increased rate. CURLY SPIDER is an eCrime group that has conducted ransomware intrusions (which predominantly involve vishing) targeting North America- and Western Europe-based entities across various sectors. Manufacturing and retail entities remain high-value targets for eCrime intrusions because these entities’ operating nature incentivizes them to pay ransoms quickly. Manufacturers cannot afford production delays, and retailers risk losing customer data and sales, especially during busy shopping seasons. These industries typically have larger budgets and complex computer systems that can be outdated, which also makes them attractive targets.

# MITRE ATT&CK Observations

CrowdStrike OverWatch tracks interactive intrusion activity against the MITRE ATT&CK® Enterprise Matrix, a framework that categorizes and tracks adversary behavior.[^1]

![MITRE ATT&CK heat map highlighting the top techniques CrowdStrike OverWatch observed adversaries employ in each tactic area, July 2024-June 2025]

[^1]: To learn more about the MITRE ATT&CK Enterprise Matrix, visit https://attack.mitre.org/matrices/enterprise/

Though CrowdStrike OverWatch observed the most total activity within the Defense Evasion tactic, five of the top 10 most commonly used MITRE ATT&CK techniques in the past 12 months were Discovery techniques. This highlights that adversaries are both spending their time orienting themselves within a network and ensuring their activities are not detected by security measures whenever possible. eCrime access brokers rely on these techniques — including Account Discovery, System Network Configuration Discovery, and Remote System Discovery — to evaluate targets as part of the threat actors’ efforts to monetize operations.

Defense Evasion techniques such as Masquerading and Disable or Modify Tools — as well as Ingress Tool Transfer, a Command and Control technique — were also in the top 10 most leveraged techniques. These techniques allow adversaries to blend their activity into expected network activity while enabling follow-on activities in various other tactic areas, such as Privilege Escalation and Credential Access.

# Intrusion Trends by Adversary

CrowdStrike’s insight into adversaries is unmatched. With detailed information about more than 265 attributed eCrime, nation-state, and hacktivist adversaries — and more than 150 active clusters of malicious activity that have not yet met CrowdStrike’s standards for adversary graduation — CrowdStrike OverWatch threat hunters are well positioned to quickly and accurately disrupt the adversary.

![Table of most intrusive adversaries categorized by sector]

# Observations from the Front Lines

## Countering the Adversary: Generative Artificial Intelligence

Enterprising threat actors have capitalized on the surge of recently developed GenAI models to conduct social engineering, technical operations, and information operations (IO). GenAI tools have likely contributed to increased speed, access to expertise, and scalability in threat actor operations. At the same time, organizations’ integration of AI into business operations has created a new attack surface for threat actors to target. Despite these observable advantages for attackers, AI-enhanced cyber operations face similar constraints to traditional cyber operations, including resource availability and authorities.

### Defining GenAI
GenAI is a subset of AI designed to create new data based on existing data. It is powered primarily by advanced machine learning models such as large language models (LLMs), which use natural language processing to generate text, and diffusion models, which create images, audio, and video content.[^2]

[^2]: Generative AI in Cybersecurity || What Is the Difference Between a Diffusion Model and LLM in Simple Terms || Explained: Generative AI

![Table showing adversary use of GenAI as a primary attack vector: Social Engineering, Technical Operations, and Information Operations]

### FAMOUS CHOLLIMA Leads in GenAI-Supported Operations
DPRK-nexus adversary FAMOUS CHOLLIMA conducts insider threat operations at an exceptionally high operational tempo. In the past 12 months, CrowdStrike OverWatch investigated over 320 incidents where FAMOUS CHOLLIMA operatives obtained fraudulent employment as remote software developers. FAMOUS CHOLLIMA has been able to sustain this pace by interweaving GenAI-powered tools that automate and optimize workflows at every stage of the hiring and employment process.

![Diagram of FAMOUS CHOLLIMA’s use of GenAI in insider threat operations: Applications, Interviews, and On the Job]

### Countering FAMOUS CHOLLIMA
These recommendations can be implemented to help protect against FAMOUS CHOLLIMA’s insider threat activity:

- Implement enhanced identity verification processes during the hiring phase that include rigorous background investigations and corroboration of online professional profiles.
- Implement real-time deepfake challenges during interview or employment assessment sessions.
- Augment security controls pertaining to remote access to corporate systems, with a particular focus on geolocation masking and endpoint security circumvention attempts.
- Validate connected USB and other peripheral devices to identify and prevent the use of physical and software-based remote tools.
- Monitor employee communication channels for manifestations of aberrant translation activities or concurrent administration of multiple accounts.
- Create training programs designed to teach hiring managers and IT personnel to recognize and report potential indicators of insider threats employing AI tools.

### Threat Actors Targeting AI Tools
The increasing adoption of AI tools and technology within organizational networks and workflows is likely to lead to a rise in adversaries targeting these tools. Threat actors are using organizations’ AI tools as initial access vectors to execute diverse post-exploitation operations.

In April 2025, CrowdStrike observed multiple threat actors exploit CVE-2025-3248, an unauthenticated code injection vulnerability in Langflow AI. Langflow is a widely used tool for building AI agents and workflows. Attackers can exploit CVE-2025-3248 using specially crafted HTTP requests to achieve unauthenticated remote code execution.

### Outlook
GenAI enhances threat actors' operations rather than replacing existing attack methodologies. The effectiveness of these tools, however, depends on system availability, defensive-offensive capability balance, and operational integration.

# Hunting Cross-Domain Adversaries

Cross-domain threat hunting enables detection of adversary activities that span multiple security areas, including identity systems, endpoints, and cloud environments. These attacks are challenging to detect because activities are distributed, resulting in a reduced footprint within each individual security domain.

![Chart of most commonly used TTPs leveraged by ransomware operators in 2025]

### Case Study: Disrupting BLOCKADE SPIDER
CrowdStrike OverWatch identified that BLOCKADE SPIDER had accessed a victim’s network via an unmanaged VPN appliance in early 2025. The adversary moved laterally to several managed systems, where they performed actions typically observed in BGH activity, including attempting to dump credentials from a Veeam Backup & Replication configuration database and delete backup files.

![Diagram of BLOCKADE SPIDER cross-domain attack path]

### Case Study: Hunting OPERATOR PANDA
To hunt for enterprising adversaries such as China-nexus OPERATOR PANDA, also known as Salt Typhoon, defenders can benefit from correlating data across multiple sources, especially from devices beyond the scope of traditional EDR coverage, such as routers, switches, VPN appliances, and firewalls. OPERATOR PANDA often gains initial access through internet-facing applications, like Cisco switches, which are known blind spots not covered by EDR.

# Identity Hunting

Vishing and help desk social engineering have continued to play a dominant role in eCrime operations in 2025. Adversaries are bypassing traditional security measures by exploiting human weaknesses, leveraging compromised credentials and social engineering to gain initial access and move laterally within organizations.

![Vishing attacks observed by month, January 2024-June 2025]

# Adversary Spotlight: SCATTERED SPIDER

Following a period of relative inactivity between December 2024 and March 2025, SCATTERED SPIDER returned in April 2025 with aggressive ransomware campaigns targeting the U.K. and U.S. aviation, insurance, and retail sectors. In most 2025 incidents to date, the adversary has leveraged help desk social engineering to gain initial access.

![Timeline of SCATTERED SPIDER social engineering attack]

# Cloud Hunting

### Case Study: Hunting GENESIS PANDA Across the Cloud Control Plane
[Content omitted in source]

### Case Study: MURKY PANDA’s Abuse of Trusted Relationships
[Content omitted in source]

# Endpoint Hunting

### Case Study: Hunting GLACIAL PANDA Living off the Land
[Content omitted in source]

# Vulnerability Hunting

### Case Study: Hunting GRACEFUL SPIDER’s Zero-Day
[Content omitted in source]

# Conclusion

[Content omitted in source]

# Recommendations

[Content omitted in source]

# CrowdStrike Falcon Platform

[Content omitted in source]

# CrowdStrike Products

[Content omitted in source]

# CrowdStrike Services

[Content omitted in source]

# About CrowdStrike

[Content omitted in source]

---

tions
on the endpoint, maintaining a minimal footprint

Identity data enables threat hunters to follow
SCATTERED SPIDER across a compromised
environment

Threat hunters may only see SCATTERED SPIDER on the
endpoint when they pivot from other domains

Identity data can:

Successful hunting requires context from other domains
to connect activity

Pinpoint where SCATTERED SPIDER interacts with
systems outside a user’s standard working hours

NEXT-GEN SIEM

Next-gen SIEM provides threat hunters with
visibility spanning multiple domains when logs are
available:

VMware logs highlight tunneling tooling on ESXi
hosts and credential harvesting activity

IAM logs allow hunters to observe SCATTERED
SPIDER authenticating to SSO-enabled
applications

Firewall logs allow hunters to identify where
tunneling traffic is originating

Provide insight into SCATTERED SPIDER’s next
target based on the context of the account used
and other identities the adversary enumerates

Identity-specific hunting for privilege escalation
tools and TTPs can help hunters track and predict
SCATTERED SPIDER’s next move

THE PUZZLE
OF DETECTING
SCATTERED SPIDER

SOFTWARE AS A SERVICE APPLICATIONS AND
PLATFORMS

SaaS applications often span multiple hunting domains

SCATTERED SPIDER uses compromised SaaS platforms
to attain persistence and store data for later exfiltration

CLOUD

SaaS data allows hunters to:

Detect suspicious access to highly sensitive
documents in documented sharing and storage
platforms such as SharePoint and OneDrive

Search for suspicious access requests to, and usage
of, database platforms

Look for signs of suspicious access to PAM platforms
to harvest credentials

Cloud data helps threat hunters identify
SCATTERED SPIDER’s presence in Entra ID
and Azure

Threat hunters can look for suspicious
new VM creation events and new MFA
device additions, correlating this activity
with unusual patterns of password resets

Self-service password reset (SSPR)
enumeration can help uncover help desk
phishing

Figure 12. Hunting SCATTERED SPIDER across domains

CROWDSTRIKE 2025 THREAT HUNTING REPORT
30

To defend against adversaries like SCATTERED SPIDER, organizations should adopt the following

proactive measures:

•  Identity Protection: Use phishing-resistant MFA (avoiding SMS-based methods), isolate privileged accounts
from regular workflows, strengthen password reset procedures, and restrict help desk involvement in MFA

enrollment.

•  Detection and Monitoring: Continuously monitor for authentication anomalies, administrative changes, and

unusual network traffic to critical systems; enable comprehensive logging and behavioral analytics; and watch

for suspicious application usage, search terms, and data access patterns that could indicate malicious activity.

•  Infrastructure Security: Secure VMware environments, segment networks to contain potential intrusions,
block the use of unauthorized tools, apply least-privilege access across cloud environments, and disable

outdated or legacy authentication methods.

•  Incident Readiness: Maintain isolated and regularly tested backups, develop and rehearse incident response

playbooks, perform regular readiness assessments, and train IT and help desk teams to recognize and respond

to social engineering tactics.

Outlook

When it comes to identities compromised by vishing, providing threat hunters with as much information regarding

the characteristics of an account up front is a necessity. Rapidly ascertaining key details — such as when an

account password was last reset, what privileges and groups an account has access to, and an account’s MFA

status — provides vital context to threat hunters assessing whether activity is likely malicious.

As enterprising adversaries like SCATTERED SPIDER expand their attacks beyond the endpoint, technologies like

identity protection and next-gen SIEM become essential. Modern threat hunting requires analysts who are able to

pivot between data sources as quickly as the adversary is able to pivot during an intrusion.

CLOUD HUNTING

The CrowdStrike 2025 Global Threat Report identified that China’s cyber espionage capabilities reached a

critical inflection point over the past year, marked by increasingly bold targeting, stealthier tactics, and expanded

operational capacity. In 2024, China-nexus threat actors employed the ORB07 operational relay box (ORB)
network9 to conduct password spraying attacks against Microsoft Azure accounts. The network, which consists

of thousands of nodes, is likely used by multiple China-nexus adversaries for the sole purpose of targeting Azure

accounts, highlighting a newfound emphasis on cloud exploitation operations.

Over the past 12 months, CrowdStrike OverWatch observed a 40% increase in cloud intrusions associated

with China-nexus adversaries. This increase suggests cloud exploitation continues to be a key focus for these

adversaries. The cloud’s vast data, scalability, and exploitable misconfigurations enable adversaries to achieve

persistence, move laterally, and exfiltrate data.

9  An ORB network is a traffic relay system — generally composed of a mix of compromised devices and leased servers — used to obfuscate

the origin and destination of malicious traffic

CROWDSTRIKE 2025 THREAT HUNTING REPORT

31

Two China-nexus adversaries — GENESIS PANDA and MURKY PANDA — have proven to be particularly adept at

navigating cloud environments over the past year, each showcasing different techniques that require different hunting

strategies. GENESIS PANDA conducts high-volume operations with less emphasis on operational security and a

suspected role as an access broker. MURKY PANDA is a more sophisticated and elusive adversary prioritizing evasion

techniques in the cloud and using trusted relationships for initial access. Figure 13 compares these adversaries’ most

prevalent TTPs.

CROWDSTRIKE OVERWATCH:
2025 CLOUD HUNTING BY THE NUMBERS

•  Leveraging CrowdStrike Falcon® Cloud Security telemetry, CrowdStrike OverWatch identified a

136% increase in cloud intrusions in the first half of 2025 compared to all of 2024

•  Over the past 12 months, CrowdStrike OverWatch observed a 40% increase in cloud-conscious

intrusions by suspected China-nexus actors

Initial Access

Execution

Persistence

Privilege Escalation

Defense Evasion

T1078.004
Valid Accounts: Cloud
Accounts

T1651
Cloud Administration
Command

T1098.004
Account Manipulation:
SSH Authorized Keys

T1078.004
Valid Accounts: Cloud
Accounts

T1550.001
Use Alternate
Authentication Material:
Application Access Token

T1190
Exploit Public-Facing
Application

T1195
Supply Chain Compromise

T1098.001
Account Manipulation:
Additional Cloud
Credentials

T1098.003
Account Manipulation:
Additional Cloud Roles

T1562.007
Impair Defenses: Disable
or Modify Cloud Firewall

T1619
Cloud Storage Object
Discovery

T1070
Indicator Removal

T1552.005
Unsecured Credentials:
Cloud Instance Metadata
API

T1016
System Network
Configuration Discovery

T1114.002
Email Collection: Remote
Email Collection

T1090.002
Proxy: External Proxy

Credential Access

Discovery

Collection

Command and Control

Y
E
K

MURKY PANDA

GENESIS PANDA

BOTH

Figure 13. Prevalent MITRE ATT&CK TTPs used by MURKY PANDA and GENESIS PANDA

CROWDSTRIKE 2025 THREAT HUNTING REPORT
32

CASE STUDY:

Hunting GENESIS PANDA Across the Cloud Control Plane

Adversary Profile

GENESIS PANDA targets a wide variety of sectors — including financial services, media, telecommunications, and

technology — in at least 11 countries. The adversary likely serves as an initial access broker to facilitate future

intelligence collection. This assessment is made with moderate confidence based on the volume of activity the adversary

conducted, their exploitation of a wide range of web-facing vulnerabilities, limited observation of data exfiltration, and

TTP overlaps with penetration testing-type activity.

MARCH 2024
Threat actor queries IMDS
for credentials

APRIL 2024
Threat actor accesses the cloud control plane
for compute instance lateral movement

JUNE 2024
Threat actor uses C2 domains
impersonating cloud services

OCTOBER 2024
Threat actor interacts with cloud storage
services using CSP command line tools

NOVEMBER 2024
Threat actor uses cloud
infrastructure for C2

2024

MAR

APR

JUN

OCT

NOV

2025

MAR

MAY

targeting cloud services

Y Cloud-conscious activity by threat actor
E
K

Cloud-supporting activity by threat actor abusing
cloud services to support their operations

MAY 2025
Threat actor hosts payload on
cloud compute infrastructure

Threat actor uses cloud compute
instance for exfiltration

MARCH 2025
Threat actor establishes cloud-based
persistence via identity-based
access key and SSH keys

Threat actor uses cloud storage
for payload hosting

Figure 14. GENESIS PANDA: Weaponizing the cloud control plane

Since at least March 2024, GENESIS PANDA has proven increasingly capable of using cloud services to support tool

deployment, command and control (C2) communications, and exfiltration. The adversary has also proven capable of

targeting cloud service provider (CSP) accounts to expand access and establish alternate forms of persistence. In

addition to hosting data on cloud services, GENESIS PANDA uses cloud infrastructure to exfiltrate the output of basic

discovery commands.

CROWDSTRIKE 2025 THREAT HUNTING REPORT
33

GENESIS PANDA’s use of CSPs to support operations underscores the

adversary’s knowledge of cloud administration and ability to move laterally

in target environments. Despite their knowledge of cloud environments,

the adversary has not been observed exfiltrating contents from S3 buckets,

further reinforcing the likelihood that they serve as an initial access broker.

Although GENESIS PANDA targets a variety of systems, they show consistent

interest in compromising cloud-hosted systems to leverage the cloud control

plane for lateral movement, persistence, and enumeration.

Cloud Service Enumeration

When compromising a cloud-hosted server, GENESIS PANDA consistently queries

the associated Instance Metadata Service (IMDS) primarily to obtain credentials

for the cloud control plane but also to enumerate network and general instance

configurations. GENESIS PANDA occasionally uses CSP command line tools,

likely in conjunction with cached credentials on compromised VMs.

In October 2024, CrowdStrike OverWatch identified hands-on-keyboard activity

from a GENESIS PANDA implant running on a cloud compute instance. The threat

actor may have used this information in preparation for lateral movement, as soon

after, they began to ping and SSH to other internal hosts. On multiple occasions,

the adversary demonstrated an interest in cloud storage service enumeration.

Pivoting to the Cloud Control Plane

GENESIS PANDA often uses credentials — likely obtained from compromised VMs —

to pivot to the target organization’s cloud account. Pivoting to the cloud control plane

grants the adversary access to run commands on other cloud-hosted VMs. During

multiple intrusions, GENESIS PANDA gained access to the target organization’s

cloud service account, added local users to various VMs, performed host-based

enumeration, and deployed malware.

GENESIS PANDA also uses the access provided by the cloud control plane to

establish various forms of persistence. In early March 2025, CrowdStrike OverWatch

identified an intrusion in which GENESIS PANDA obtained credentials to the target

organization’s cloud provider account by querying the IMDS after exploiting a

public-facing Jenkins server. The adversary then added SSH keys and created

a backdoor access key on the cloud service account. GENESIS PANDA later returned

using the backdoor access key in conjunction with a likely custom .NET-based tool to

regain access to the cloud service console. This intrusion illustrates the adversary’s

desire to establish persistence at multiple layers of the target organization and their

ability to use custom tooling for cloud-based targeting.

CROWDSTRIKE 2025 THREAT HUNTING REPORT
34

CASE STUDY:

MURKY PANDA’s Abuse of Trusted Relationships

Adversary Profile

MURKY PANDA targets various entities in North America, displaying a particular

interest in targeting cloud environments through trusted relationships between

partner organizations and their cloud tenants. The adversary almost certainly

has advanced capabilities, including access to low-prevalence malware such

as CloudedHope, and the expertise to quickly weaponize n-day and zero-day

vulnerabilities. MURKY PANDA demonstrates a high level of operations security

by deleting indicators of their presence on victim environments, targeting

edge devices for initial access, exploiting n-day or zero-day vulnerabilities,

and leveraging trusted relationship compromises. Similar to other China-nexus

adversaries, MURKY PANDA relies heavily on exploiting internet-facing appliances

for initial access.

Trusted Relationship Abuse

In late 2024, CrowdStrike Services responded to an incident in which MURKY

PANDA very likely compromised a supplier of a North American entity and used

the supplier’s administrative access to the victim entity’s Entra ID tenant to add

a temporary backdoor Entra ID account. Using this account, the threat actor

then backdoored several preexisting Entra ID service principles related to Active

Directory management and emails. The adversary’s goals appear targeted in

nature based on their focus on accessing emails.

In early 2025, CrowdStrike Services responded to another MURKY PANDA

intrusion in the environment of a customer of a third-party application for Entra

ID. During this intrusion, MURKY PANDA almost certainly compromised this

application to access victim emails as part of a trusted relationship compromise.

CrowdStrike OverWatch data indicates that service principal sign-ins for the

application typically originate from Microsoft Azure-associated IP addresses.

However, during the intrusion, service principal sign-ins also originated from a

likely compromised network-attached storage (NAS) device and a virtual private

server (VPS).

On March 7, 2025, the application vendor disclosed that they had been notified

on February 20, 2025, that a threat actor had exploited the vulnerability as a

zero-day and conducted unauthorized activity within the vendor’s Azure

environment, corroborating CrowdStrike Services’ findings.

Outlook

China-nexus adversaries are becoming increasingly skillful at exploiting and

navigating cloud environments. They use specialized techniques and tools to

support their operations. As these adversaries are likely to continue to focus on

cloud exploitation operations, with attacks growing in scale and sophistication,

understanding the differing techniques used by adversaries like GENESIS PANDA

and MURKY PANDA is crucial. This understanding will enable the necessary

adjustments to defense and hunting strategies.

CROWDSTRIKE 2025 THREAT HUNTING REPORT
35

ENDPOINT HUNTING

Though fast-moving adversaries often dominate the threat landscape, equally

dangerous threats operate on extended timelines. These patient predators

prioritize stealth and persistence, executing meticulous “long game” strategies

that include sustained access, covert data harvesting, and environmental

preparation for future operations. Their minimal digital footprint allows them

to blend seamlessly into legitimate network traffic, making detection

exceptionally challenging.

China-nexus adversaries have increasingly mastered this approach. This is

particularly evident in their increased targeting of the telecommunications sector.

CrowdStrike OverWatch observed a 130% increase in nation-state activity against

the telecommunications sector over the past 12 months. This high-value sector

offers significant intelligence value, making telecommunications entities prime

targets for stealthy actors. The sector is similarly valuable to threat hunters,

as focused hunting efforts at telecommunications entities can often uncover

new adversaries and TTPs.

CrowdStrike OverWatch threat hunters routinely identify multiple threat actors

conducting concurrent operations on the same target network, particularly at

telecommunications entities. Threat actors who conduct long-term intelligence

collection operations in specialized telecommunications environments often share

several high-level TTPs. Deep knowledge of threat actors’ characteristic behaviors

can enable threat hunters to separate and track these threat actors’ activities,

leading to new insights.

GLACIAL PANDA — a China-nexus adversary dominating the telecommunications

industry — represents such an insight. After extensive proactive hunting efforts

by CrowdStrike OverWatch, CrowdStrike Intelligence introduced GLACIAL

PANDA as the latest China-nexus adversary to specialize in this “long game”

approach to intelligence collection operations targeting telecommunications

entities. In uncovering yet another China-nexus threat actor targeting the space,

the CrowdStrike OverWatch team further demonstrated its skill in quickly and

efficiently hunting these enterprising adversaries.

CROWDSTRIKE 2025 THREAT HUNTING REPORT

36

CASE STUDY:

Hunting GLACIAL PANDA Living off the Land

GLACIAL PANDA highly likely conducts targeted intrusions for intelligence collection purposes, accessing and exfiltrating

call detail records and related communications telemetry from multiple telecommunications organizations. This activity

could have significant privacy implications for the organizations’ customers. The adversary primarily targets Linux

systems typical in the telecommunications industry, including legacy operating system distributions that support older

telecommunications technologies.

GLACIAL PANDA

Notable TTPs

Initial access via internet-facing (and frequently unmanaged) servers,
likely achieved through software exploitation or weak password provisioning

Primarily targets Linux systems, employing LOTL techniques and abusing
legitimate user accounts for lateral movement and persistence

Deploys ShieldSlide trojanized OpenSSH components to collect user
authentication sessions and credentials

Collects telecom sector-specific data, including call detail records,
network telemetry, and error logs

Vulnerabilities Exploited

Target Sectors

CVE-2016-5195 vulnerability (aka Dirty COW)

Telecommunications

CVE-2021-4034 vulnerability (aka PwnKit)

Target
Geography

Afghanistan

Hong Kong

India

Japan

Kenya

Malaysia

Mexico

Panama

Philippines

Taiwan

Thailand

U.S.

Figure 15. GLACIAL PANDA: TTPs and targets

CROWDSTRIKE 2025 THREAT HUNTING REPORT

37

GLACIAL PANDA activity is characterized by interactive intrusion tradecraft that prioritizes persistence and stealth.

This adversary is known to use:

•  Living off the land (LOTL) techniques that leverage common Linux system tools

•  Legitimate user account abuse for initial host access and lateral movement

•  Trojanized OpenSSH suite tools to capture user credentials and provide backdoor access

•  Trojanized cron daemons to hide adversary-configured jobs

•  External C2 via reverse shell connections using netcat or a publicly available Perl script

•  Access propagation between interconnected organizations, such as company subsidiaries or business relationships

Interactive intrusions involve human operators controlling systems in real time and adapting procedures according to

their objectives and the current network environment. In the telecommunications industry, legacy systems that support

older technologies can provide a beachhead, where adversaries can establish persistence while planning subsequent

stages of their intrusion. Adversaries may spend only a short time interacting with core systems. This type of activity

requires advanced threat hunting capabilities to identify and mitigate.

CrowdStrike OverWatch uses multiple hunting strategies to identify GLACIAL PANDA’s illegitimate actions among

normal user and administrative activities, necessitated by the adversary’s minimal malware footprint and legitimate

account abuse. Low-prevalence binary hunting patterns uncover trojanized software and malicious code. These binary

hunting patterns can focus on the hex representation of compiled code residing in memory in trojanized applications.

Additionally, threat hunters' deep understanding of the adversary’s characteristic command line preferences and

process invocations can locate malicious hands-on-keyboard activity among normal user sessions. Behavioral patterns

identifying repeated access to sensitive data sources on Linux hosts have also proven highly successful in identifying

GLACIAL PANDA’s aggressive and repetitive host reconnaissance and data collection procedures.

CrowdStrike OverWatch can also take advantage of the Falcon platform’s broad visibility to identify attempted

connections between separate customer networks and provide early warning of adversary activity.

ShieldSlide: Credential Harvesting and Backdoor Access via

Trojanized OpenSSH Binaries

GLACIAL PANDA deploys trojanized OpenSSH tools on compromised Linux hosts to log user authentication

events and support lateral movement by tracking remote connections to other hosts. Though several other

adversaries also modify OpenSSH components, code overlaps across variants are sufficient to attribute GLACIAL

PANDA’s tooling. This capability is collectively dubbed ShieldSlide.

ShieldSlide binaries are almost identical to legitimate OpenSSH components, except for a small modification

to the source code that logs victim credentials. The ShieldSlide-trojanized SSH server binary also provides

backdoor access, authenticating any account (including root) when a hardcoded password is entered.

Despite ShieldSlide being functionally equivalent to its legitimate counterparts, CrowdStrike OverWatch routinely

identifies maliciously modified system services using low-prevalence binary hunting techniques, alerting

customers that user accounts on their network are at risk of being compromised.

CROWDSTRIKE 2025 THREAT HUNTING REPORT

38

To hunt for and protect against threats like GLACIAL PANDA,

CrowdStrike recommends the following measures:

•  Update software on supported operating systems regularly by employing

rigorous patch management policies, and migrate end-of-life (EOL) systems to

versions with vendor update support wherever possible.

•  Monitor legacy or EOL assets that no longer receive security or software
updates, particularly for unusual network activity to and from these hosts.

•  Monitor legitimate system binaries for malicious modifications, including
/usr/bin/ssh, /usr/sbin/sshd,  /usr/sbin/cron, and OpenSSH
pluggable authentication modules.

•  Monitor SSH connections between hosts for anomalous activity, limiting which

user accounts are allowed to log in via SSH.

•  Enforce network access control policies for servers according to role and

requirement.

•  Enforce complex account password strategies — avoiding default or

generic options — for SSH authentication, and employ more secure methods

such as SSH key authentication, particularly on remotely accessible servers.

Limit situations in which server credentials (e.g., for databases) are stored

unencrypted on hosts.

•  Deploy CrowdStrike Falcon® Insight XDR on compatible hosts, ensuring

maximum network environment coverage.

VULNERABILITY HUNTING

The CrowdStrike 2025 Global Threat Report revealed that 52% of vulnerabilities

observed by CrowdStrike in 2024 were related to initial access, with exploitation

of internet-exposed applications remaining a prevalent initial access method.

Effective exposure and vulnerability management is crucial in addressing the

worst-case scenario: zero-day vulnerability exploitation.

In critical vulnerability situations, a defense-in-depth strategy is essential.

Integrating CrowdStrike OverWatch's threat hunting capabilities with exposure

management tools and solutions can provide a vital backstop, mitigating

damage during the crucial period before a patch is released. When adversaries

such as GRACEFUL SPIDER develop and deploy zero-day exploits to bypass

existing patches, CrowdStrike OverWatch's ability to identify and hunt for

post-exploitation malicious behaviors acts as a critical fail-safe, ensuring rapid

and effective coverage against subsequent widespread exploitation by

opportunistic adversaries.

CROWDSTRIKE 2025 THREAT HUNTING REPORT

39

CASE STUDY:

Hunting GRACEFUL SPIDER’s Zero-Day

A series of incidents impacting Cleo data transfer products in late 2024 highlights the intersection of detection

deployment and development, exposure management, extended detection and response (XDR), threat hunting,

and threat intelligence. On Saturday, December 7, 2024, CrowdStrike OverWatch detected suspected exploitation

of multiple Cleo products on Windows and Linux servers. The team observed compromises across Cleo instances in

multiple sectors and geographies. Based on the targets, speed, scope, and tactics demonstrated by the threat actor

during the initial wave, CrowdStrike Intelligence determined the activity was likely a zero-day file upload exploit

leading to remote code execution related to an earlier vulnerability.

DEC 7
Cleo zero-day
bypasses patch

DEC 13
Cleo discloses
CVE-2024-55956

DEC 15
GRACEFUL SPIDER
claims responsibility

DEC 7
+10 min: CrowdStrike
OverWatch customers notified

DEC 7
+1 hr: CrowdStrike OverWatch
detections implemented

DEC 9
Falcon sensor
preventions

OCT 27
Cleo discloses
CVE-2024-50623

DEC 11
Zero-day exploit
published

2024

OCT

NOV

DEC

Exploit Development and Testing

Zero-Day Campaign

Opportunistic Campaign

CrowdStrike OverWatch Provides Post-Exploitation Coverage

Figure 16. Uncovering a zero-day: A day-by-day breakdown of adversary activity

Criminal enterprises often capitalize on weekends to maximize impact — but so does CrowdStrike OverWatch. Rapidly

after the initial detection of Cleo exploitation, CrowdStrike OverWatch alerted affected customers and deployed hunting

patterns to identify malicious files being written to significant directories, providing a baseline for early-stage detection

coverage for all CrowdStrike OverWatch customers.

CrowdStrike OverWatch telemetry confirmed malicious activity began with the creation of a malicious ZIP archive file
in a temp directory corresponding to the specific Cleo product (e.g., C:\VLTrader\temp\) in Microsoft Windows
environments. The attacker then wrote a file to the autorun directory that imported the ZIP file, executing the attacker
command. When the ZIP file was imported, a malicious host definition XML file was extracted and evaluated. This XML

file defined a host structure with specific properties and included a mailbox configured to execute a system command.

CROWDSTRIKE 2025 THREAT HUNTING REPORT
40

The CrowdStrike Falcon sensor prevented further malicious post-exploitation

behaviors on compromised Cleo servers, which included process injection

and PowerShell execution. CrowdStrike Intelligence confirmed the commands

attempted to execute multiple obfuscated shellcode stages, culminating in the

download and execution of a high-prevalence, pirated version of Cobalt Strike.

These tactics, as well as the targeting of Cleo managed file transfer (MFT)

applications, were consistent with eCrime activity in general and BGH specifically.

GRACEFUL SPIDER later claimed responsibility for the initial wave of December

activities targeting Cleo on their dedicated leak site (Figure 16).

Exploit proliferation then enabled subsequent waves of exploitation. On December

11, 2024, offensive security researchers posted a functional CVE-2024-55956

exploit and a detailed technical description of the vulnerability. Opportunistic

actors rapidly adopted the exploit, and CrowdStrike Intelligence subsequently

observed numerous attempts to exploit the vulnerability, with slight formatting

variations, on the same day.

However, by this time, CrowdStrike OverWatch and the Falcon sensor could fully

backstop Cleo products against further compromise by other threat actors. By

December 9, 2025, CrowdStrike OverWatch — together with the CrowdStrike

sensor team — had successfully implemented measures to detect and prevent

Cleo post-exploitation activity within the CrowdStrike Falcon sensor.

Patch Circumvention Enables

Zero-Day Enterprise

The December 2024 CVE-2024-55956 Cleo zero-day campaigns

bypassed patch fixes for the previously disclosed file upload

vulnerability CVE-2024-50623. Though CVE-2024-50623 and

CVE-2024-55956 are distinct vulnerabilities, they share the same

fundamental root causes and exploit improper validation of input to
the /Synchronization endpoint. This endpoint is meant to be
inaccessible but could be reached by forging a fake license number.

Exploitation of this vulnerability allows arbitrary file reads and writes on

the targeted instance server, with the opportunity to pivot into remote

code/command execution.

The initial CVE-2024-50623 patch addressed, in part, the file path

validation issue but did not mitigate the improper validation bug allowing

actors to forge a fake license number. Resourceful threat actors such

as GRACEFUL SPIDER realized the initial path validation fixes could be

bypassed and once again abused the unmitigated license forgery issue

to achieve remote code execution via CVE-2024-55956.

CROWDSTRIKE 2025 THREAT HUNTING REPORT
41

To hunt for and protect against threats from emerging exploit campaigns,

CrowdStrike recommends the following measures:

•  Deploy EDR/XDR capabilities on compatible hosts to ensure maximum visibility

and coverage across the network environment.

•  Inventory and review enterprise assets to ensure visibility across the

organization.

•  Identify vulnerable assets through continuous exposure assessment and

vulnerability scanning.

•  Monitor externally exposed assets for signs of risk or potential compromise.

•  Update software by using intelligence-driven patch management policies that

prioritize exposed assets with known exploited vulnerabilities.

•  Enforce script execution policies on supported platforms to block PowerShell

and other script-based activity on hosts where it is not required.

Hunting for GRACEFUL SPIDER’s Zero-Day

Campaign Artifacts

Efforts by CrowdStrike OverWatch ensured that malicious activity and detections

led to customer notifications within hours and Falcon sensor prevention measures

could be rolled out within days. When threat actors compromise internet-exposed

services to achieve remote code execution, CrowdStrike telemetry is capable

of capturing the resulting anomalous file, network, and process activities.

During this Cleo exploitation campaign, CrowdStrike OverWatch leveraged

Falcon Next-Gen SIEM extensively to hunt for both campaign-specific

indicators and generic intrusion artifacts across sensor telemetry.

Hunting for exploited software requires an understanding of the environment

to formulate baselines in the monitored network. Though the following example

is designed for CrowdStrike customers, as it leverages the CrowdStrike Query

Language (CQL), it demonstrates concepts that are broadly applicable to all threat

hunters. It demonstrates how to monitor potentially vulnerable processes against

identified baselines to detect suspicious artifacts that may be indicative

of ongoing exploitation activity.

CROWDSTRIKE 2025 THREAT HUNTING REPORT

42

( // detect uncommon process rollups

#event_simpleName=ProcessRollup2

// replace the <process_filename> placeholder with the file name of the investigated
process, e.g., java.exe

ParentBaseFileName=<process_filename>

// regex to defeat known goods

// replace <expected_command_x> in accordance with baselines in your environment

CommandLine!=/<expected_command_1>|<expected_command_2>|<...>|<expected_command_n>/

)

OR ( // detect uncommon file write operations

#event_simpleName=/^(ELFFileWritten|PeFileWritten|NewScriptWritten)$/

// replace the <process_filename> placeholder with the file name of the investigated
process, e.g., java.exe

ContextBaseFileName=<process_filename>

// regex to defeat known goods

// replace <expected_filename_x> in accordance with baselines in your environment

TargetFileName!=/<expected_filename_1>|<expected_filename_2>|<...>|<expected_filename_n>/

)

// this formats the results in a user-friendly way

| case{

CommandLine=* | artifact:=CommandLine;

TargetFileName=* | artifact:=TargetFileName;

}

| table([@timestamp, #event_simpleName, aid, ComputerName, artifact])

Figure 17. Example CQL query: Monitoring potentially vulnerable processes

CROWDSTRIKE 2025 THREAT HUNTING REPORT

43

Conclusion

The past year marked a defining chapter in the evolution of threat hunting.

From the rapid rise of cross-domain intrusions and identity-based attacks

to the growing weaponization of GenAI and targeting of cloud infrastructure,

adversaries have demonstrated their ability to innovate, adapt, and scale

operations with speed. Whether motivated by financial gain, espionage,

or long-term access, enterprising adversaries are exploiting complexity,

leveraging trusted relationships, and moving beyond traditional attack

surfaces to evade detection.

CrowdStrike OverWatch threat hunters have revealed how adversaries

no longer operate in silos. They navigate across the identity, endpoint,

and cloud domains, using hands-on-keyboard tradecraft that challenges

traditional security tools. Defenders are rising to meet the challenge with

faster detection, deeper context, and coordinated defense rooted

in intelligence.

This report underscores that proactive, intelligence-driven hunting is essential.

Security teams must integrate telemetry across the enterprise, operationalize

threat intelligence, and use automation to extend human capability. It is not

enough to respond; defenders must anticipate, pivot, and relentlessly pursue

the adversary.

As adversaries sharpen their capabilities, the CrowdStrike Counter Adversary

Operations team remains resolute in detecting and disrupting the world’s most

sophisticated threat actors. This commitment ensures that wherever the

adversary goes, the team is already there.

CROWDSTRIKE 2025 THREAT HUNTING REPORT
Recommendations

44

Adopt AI-powered solutions to scale
security operations

As threat actors adopt AI to strike faster, scale operations, and evade detection, defenders face

mounting pressure to keep pace. Security teams are already stretched thin, grappling with growing

alerts, contending with skills shortages, and racing to respond at speed. To close these widening

gaps, security teams should operationalize agentic AI, systems capable of reasoning, adapting, and

acting autonomously within defined guardrails and organizational policies. These capabilities can scale

intelligence-driven operations by using emerging threat intelligence and expertise to triage alerts,

conduct investigations, and execute response actions. By offloading time-intensive, repetitive tasks,

agentic AI empowers human analysts to focus on proactive threat hunting and hypothesis-driven

investigation, elevating both strategic impact and operational efficiency.

Secure the entire identity ecosystem

Adversaries increasingly target identities using credential theft, MFA bypass, and social engineering

while moving laterally between on-premises, cloud, and SaaS environments via trusted relationships.

This allows them to impersonate legitimate users, escalate privileges, and evade detection.

Organizations should adopt phishing-resistant MFA solutions, such as hardware security keys, to

prevent unauthorized access. Strong identity and access policies are essential, including just-in-time

access, regular account reviews, and conditional access controls. Identity threat detection tools must

monitor behavior across endpoints and on-premises, cloud, and SaaS environments to flag privilege

escalation, unauthorized access, and backdoor account creation. Integrating these tools with XDR

platforms ensures comprehensive visibility and a unified defense against adversaries.

Additionally, organizations should educate users to recognize vishing and phishing attempts while

maintaining proactive monitoring to detect and respond to identity-based threats.

Eliminate cross-domain visibility gaps

Adversaries’ growing use of hands-on-keyboard techniques and legitimate tools makes detection and

response more difficult. Unlike traditional malware, these methods allow attackers to bypass legacy

security measures by executing commands and using legitimate software to mimic normal operations.

To counter this, organizations must modernize their detection and response strategies. XDR and

next-gen SIEM solutions provide unified visibility across endpoints, networks, cloud environments,

and identity systems, enabling analysts to correlate suspicious behaviors and see the full attack path.

Agentic AI-powered triage and investigations can extend these capabilities, autonomously analyzing

signals across domains to surface high-fidelity insights and prioritize real threats.

Proactive threat hunting and threat intelligence further enhance detection by identifying potential

attack patterns and providing insights into adversary TTPs. With real-time intelligence, organizations

can stay informed about emerging threats, anticipate attacks, and prioritize critical security efforts.

CROWDSTRIKE 2025 THREAT HUNTING REPORTRecommendations
45

Defend the cloud as core infrastructure

Cloud-focused adversaries are exploiting misconfigurations, stolen credentials, and cloud management

tools to infiltrate systems, move laterally, and maintain persistent access for malicious activities like

data theft and ransomware deployment.

Cloud-native application protection platforms (CNAPPs) with cloud detection and response (CDR)

capabilities are critical to counter these threats. These solutions provide operators with a unified view

of their cloud security posture, helping them rapidly detect, prioritize, and remediate misconfigurations,

vulnerabilities, and adversary threats. Additionally, enforcing strict access controls — such as

role-based access and conditional policies — limits exposure to critical systems and ensures

continuous monitoring for anomalies, including logins from unexpected locations.

Regular audits are also critical to maintaining security. Automated tools can uncover overly permissive

storage settings, exposed APIs, and unpatched vulnerabilities. Frequent reviews of cloud environments

ensure unused permissions and outdated configurations are addressed promptly.

Prioritize vulnerabilities with an
adversary-centric approach

Adversaries are increasingly exploiting publicly disclosed vulnerabilities and using exploit chaining,

combining multiple vulnerabilities to gain rapid access, escalate privileges, and bypass defenses.

These multi-stage attacks often rely on public resources like proof-of-concept (POC) exploits and

technical blogs, enabling adversaries to craft effective and hard-to-detect payloads.

To counter these threats, organizations must prioritize regular patching or upgrading of critical

systems, especially frequently targeted internet-facing services like web servers and VPN gateways.

Monitoring for subtle signs of exploit chaining, such as unexpected crashes or privilege escalation

attempts, can help detect attacks before they progress.

Tools like CrowdStrike Falcon® Exposure Management, built with native AI prioritization, enable teams

to reduce noise and focus on the vulnerabilities that matter most, specifically those affecting critical

and high-risk systems. By adopting proactive security approaches, discovering exposures across the

attack surface, and leveraging automation, organizations can mitigate sophisticated threats and limit

adversary opportunities.

Know the adversary and be prepared

When a cyberattack unfolds in minutes — or even seconds — being prepared can be the difference

between containment and catastrophe. An intelligence-driven approach enables security teams to

move beyond reactive defense by understanding which adversary is targeting them, how they operate,

and what their objectives are. With threat intelligence, adversary profiling, and tradecraft analysis,

security teams can prioritize resources, adapt defenses, and actively hunt for threats before they

escalate. CrowdStrike’s threat intelligence doesn’t just detect known threats — it anticipates new

and evolving tradecraft, ensuring defenders are always one step ahead. By seamlessly integrating

intelligence into security workflows, organizations can accelerate response times, disrupt adversaries,

and turn intelligence into action.

Though technology is critical to detect and stop intrusions, the end user remains a crucial link in

the chain to stop breaches. Organizations should initiate user awareness programs to combat the

continued threat of phishing and related social engineering techniques. For security teams, practice

makes perfect. Encourage an environment that routinely performs tabletop exercises and red/blue

teaming to identify gaps and eliminate weaknesses in your cybersecurity practices and response.

CROWDSTRIKE 2025 THREAT HUNTING REPORT
46

CrowdStrike
Falcon Platform

AI and Cloud-Native

Leverages the network effect of crowdsourced security data while eliminating the management

burden of cumbersome on-premises solutions

Single Lightweight Agent

Provides frictionless and scalable deployment and stops all types of attacks while eliminating agent bloat

and scheduled scans

Charlotte AI

Powers the CrowdStrike portfolio of GenAI capabilities across the Falcon platform, tapping into

the petabyte scale of CrowdStrike’s automated intelligence — and further enriched by security experts —

to accelerate analyst workflows

Falcon Fusion SOAR

Provides native security orchestration, automation, and response (SOAR) capabilities within the

Falcon platform to allow you to collect contextually enriched data and automate security operations,

threat intelligence, and incident response — all in a single platform and through the same console —

to mitigate cyber threats and vulnerabilities

CrowdStrike Asset Graph

Solves one of the most complex customer problems today: identifying assets, identities, and configurations

accurately across all systems — including cloud, on-premises, mobile, internet of things (IoT), and more —

and connecting them together in a graph form

CrowdStrike Intel Graph

Enables security teams to proactively defend against emerging threats with intelligence-driven insights by

mapping relationships between threat actors, tactics, vulnerabilities, and real-world attacks

CrowdStrike Threat Graph

Uses cloud-scale AI to correlate trillions of data points from multiple telemetry sources to identify shifts

in adversarial tactics and map tradecraft to automatically predict and prevent threats in real time across

CrowdStrike’s global customer base

Falcon Foundry

Allows customers and partners to easily build custom, no-code applications that harness the data, automation,

and cloud-scale infrastructure of the Falcon platform to solve their toughest cybersecurity challenges

CrowdStrike Marketplace

Offers an enterprise marketplace of technology partners where you can discover, try, buy, and deploy trusted

CrowdStrike and partner applications that extend the CrowdStrike Falcon platform, without adding agents or

increasing complexity

CROWDSTRIKE 2025 THREAT HUNTING REPORT
47

CrowdStrike Products

Endpoint Security

FALCON PREVENT | NEXT-GENERATION ANTIVIRUS

Prevents advanced threats like ransomware and fileless attacks with AI-powered next-gen antivirus; combines machine

learning, behavioral analysis, memory scanning, and exploit mitigation to stop modern threats

FALCON INSIGHT XDR | DETECTION AND RESPONSE FOR ENDPOINT AND BEYOND

Offers industry-leading, unified EDR and XDR with enterprise-wide visibility to automatically detect adversary activity

and respond across endpoints and all key attack surfaces

FALCON FIREWALL MANAGEMENT | HOST-BASED FIREWALL

Delivers simple, centralized host firewall management, making it easy to manage and control host firewall policies

FALCON DEVICE CONTROL | USB SECURITY

Provides the visibility and precise control required to enable safe usage of USB devices across your organization

FALCON FOR MOBILE | MOBILE THREAT DETECTION

Protects against threats to iOS and Android devices, extending XDR/EDR to your mobile devices, with advanced threat

protection and real-time visibility into app and network activity

FALCON FORENSICS | FORENSIC CYBERSECURITY

Allows you to quickly respond and recover with automated forensic data collection, enrichment, and correlation

FALCON GO | SMB CYBER PROTECTION

Gives small businesses peace of mind against cyber threats with easy-to-install next-gen antivirus, device control,

and mobile device protection

FALCON FOR XIoT | XIoT ASSET PROTECTION

Delivers real-time threat prevention and detection for extended internet of things (XIoT) assets, backed by XIoT-specific

indicators of attack (IOAs) and indicators of compromise (IOCs) from CrowdStrike’s industry-leading threat intelligence

FALCON INSIGHT FOR ChromeOS | ChromeOS PROTECTION

Delivers industry-first native detection and response for ChromeOS devices without requiring additional agents or mobile

device management (MDM) solutions, providing unified visibility through the Falcon console

FALCON FOR LEGACY SYSTEMS | PROTECTION FOR LEGACY OPERATING SYSTEMS

Provides lightweight, cloud-native protection for older Windows systems — no upgrades or added complexity

CROWDSTRIKE 2025 THREAT HUNTING REPORT
48

Counter Adversary Operations

FALCON ADVERSARY OVERWATCH | INTELLIGENCE-LED THREAT HUNTING

Provides 24/7 protection across endpoints, identities, cloud workloads, and next-gen SIEM delivered by

AI-powered threat hunting experts and includes built-in threat intelligence to expose adversary tradecraft,

vulnerabilities, and stolen credentials

FALCON ADVERSARY INTELLIGENCE | SOC AUTOMATION

Cuts response time from days to minutes across the entire SOC with end-to-end intelligence automation,

enabling you to instantly submit potential threats to an advanced malware sandbox, extract IOCs, and deploy

countermeasures — all while continuously monitoring for fraud and safeguarding your brand, employees,

and sensitive data

FALCON ADVERSARY INTELLIGENCE PREMIUM | ADVERSARY INTELLIGENCE

Delivers industry-leading intelligence reporting at your fingertips, along with prebuilt detections and

one-click hunting, to cut the time and cost required to understand and defend against sophisticated

nation-state, eCrime, and hacktivist adversaries

FALCON COUNTER ADVERSARY OPERATIONS ELITE | ON-DEMAND ANALYST

Provides an assigned analyst who leverages AI-powered investigative and threat hunting tools, enhanced by

deep adversary intelligence, to detect and disrupt adversaries across your IT environment and beyond

Cloud Security

FALCON CLOUD SECURITY: PROACTIVE SECURITY

Provides unified security posture management (USPM) and business context across cloud layers, leveraging

industry-leading threat intelligence, end-to-end attack paths, and ExPRT.AI so cloud teams can swiftly prioritize

their work, neutralize critical risks, and leave adversaries no room to strike

FALCON CLOUD SECURITY: CLOUD RUNTIME PROTECTION

Delivers leading cloud workload protection (CWP) and CDR, allowing SOC teams to detect and respond to active

threats across hybrid clouds so adversaries are stopped in their tracks

FALCON CLOUD SECURITY: CNAPP

Includes the features and capabilities of both Proactive Security and Cloud Runtime Protection for Falcon

Cloud Security

FALCON ADVERSARY OVERWATCH: CLOUD | THREAT HUNTING

Offers both proactive and protective security as a managed service through Falcon Adversary OverWatch

cross-domain threat hunting and Falcon Complete Next-Gen MDR, powered by integrated threat intelligence

to protect the cloud control plane, host operating system, and data plane

CROWDSTRIKE 2025 THREAT HUNTING REPORT
49

SaaS Security

FALCON SHIELD | SaaS APPLICATION SECURITY

Enables security teams to secure their entire SaaS stack through threat prevention, detection, and response;

proactively find and fix weaknesses across their SaaS stack; help with compliance efforts; and maintain

continuous continuous security for all configurations, human and non-human users, shadow apps, data,

devices connecting to SaaS, and SaaS GenAI

Identity Protection

FALCON IDENTITY THREAT DETECTION

Provides unified visibility across hybrid identities and AI-driven threat detection to expose identity-based

threats before they escalate

FALCON IDENTITY THREAT PROTECTION

Secures hybrid identities with AI-driven threat detection and behavioral analytics, leveraging the unified

Falcon platform to stop identity-based attacks in real time

FALCON PRIVILEGED ACCESS

Powered by Falcon Identity Protection, minimizes identity risk with just-in-time (JIT) access, granting

elevated permissions only when needed and under secure conditions

FALCON ADVERSARY OVERWATCH: IDENTITY | THREAT HUNTING

Provides 24/7 managed identity threat hunting, proactively detecting identity-based attacks, monitoring

criminal forums for stolen credentials, and enforcing MFA challenges to prevent unauthorized access

Next-Gen SIEM

FALCON NEXT-GEN SIEM | SECURITY INFORMATION AND EVENT MANAGEMENT

Empowers you to stop breaches and streamline your SOC by unifying industry-best detection, world-class

threat intelligence, blazing-fast search, and AI-led investigation in one platform

Data Protection

FALCON DATA PROTECTION FOR ENDPOINT | REAL-TIME ENDPOINT

DATA PROTECTION

Delivers real-time visibility, encryption detection, and behavioral analysis to stop unauthorized data exfiltration

across Windows and macOS devices

FALCON DATA PROTECTION FOR CLOUD | RUNTIME CLOUD

DATA PROTECTION

Provides real-time monitoring and classification of sensitive data in motion across cloud environments using

eBPF, enabling organizations to detect and respond to data risks without added complexity and with minimal

performance impact

CROWDSTRIKE 2025 THREAT HUNTING REPORT
50

Security and IT Operations

FALCON EXPOSURE MANAGEMENT | EXPOSURE MANAGEMENT

Provides full attack surface visibility, prioritizes vulnerabilities with AI, and automates remediation

to proactively reduce cyber risk and prevent breaches

FALCON EXPOSURE MANAGEMENT: CAASM

Allows you to discover and monitor managed and unmanaged assets in real time and visually

map assets and their relationships, revealing deep host insights into applications, browsers, CVEs,

and misconfigurations

FALCON FILEVANTAGE | FILE INTEGRITY MONITORING

Provides real-time, comprehensive, and centralized visibility that boosts compliance and offers

relevant contextual data

FALCON FOR IT | INTELLIGENT ENDPOINT AUTOMATION

Extends the Falcon platform to accelerate observability and response workflows for security

operations teams

FALCON ADVERSARY OVERWATCH: NEXT-GEN SIEM | THREAT HUNTING

Delivers end-to-end threat disruption by correlating first- and third-party Falcon Next-Gen SIEM data and

proactively hunting advanced threats across network edge devices, SaaS applications, email security,

operating systems, and more

Managed Services

FALCON COMPLETE NEXT-GEN MDR | MANAGED DETECTION AND RESPONSE

Provides 24/7 expert-driven protection across endpoints, identities, cloud workloads, and third-party

data, combining elite security expertise, AI-powered technology, and proactive threat hunting to detect,

disrupt, and remediate sophisticated threats in minutes

CROWDSTRIKE 2025 THREAT HUNTING REPORT
51

CrowdStrike Services

INCIDENT RESPONSE

Provides 24/7 elite incident response to contain threats, restore order, and mitigate breach impact

Incident Response Services | Provides comprehensive response and recovery in the event of a

cyber breach — spanning investigation, remediation, and recovery — backed by world-class threat

intelligence and delivered by a highly experienced incident response team

Active Defense Services | Provides cross-domain response to recover from a breach with speed

and precision

Services Retainer | Provides on-demand access to CrowdStrike expertise, from rapid response to

long-term resilience

STRATEGIC ADVISORY SERVICES

Develops and matures the security program to improve defenses

Tabletop Exercise | Simulates incident response scenarios that expose process gaps and improve

coordination across the full team, from hands-on-keyboard analysts to executive stakeholders

Maturity Assessment | Comprehensively evaluates your organization’s security posture, identifying

gaps, benchmarking capabilities, and providing a prioritized roadmap to strengthen defenses against

evolving threats

Regulation Readiness and CXO Advisory | Helps you understand and prepare for cyber-related

regulation mandates, including the evolving risk and governance responsibilities of the board of

executives

Insider Risk Program Review | Strengthens your insider risk strategy by assessing and optimizing your

current detection, prevention, and response capabilities

AI SECURITY SERVICES

Secures the AI powering your organization and uses AI to defend with scale, precision, and speed

AI Security Assessment | Provides Falcon-powered discovery and threat-informed testing to uncover

shadow AI, risky integrations, and governance gaps, delivering clear visibility and actionable guidance

AI for SecOps Readiness | Allows you to safely integrate AI into detection and response workflows

with tailored use cases, architectural guidance, and a roadmap to increase speed, precision,

and impact

AI Red Team Services | Exposes vulnerabilities in the GenAI stack that could be exploited by testing

LLM integrations for sensitive data exposure and adversarial manipulation

CROWDSTRIKE 2025 THREAT HUNTING REPORT
52

RED TEAM SERVICES

Tests and validates defenses through emulated attacks that expose weaknesses

Penetration Testing | Provides attack emulations that test the detection and response capabilities of

your people, processes, and technology to identify vulnerabilities

Red Team/Blue Team Exercise | Increases response readiness under expert guidance, as a red team

attacks systems in a simulated exercise and a blue team mounts the defense

Adversary Emulation Exercise | Gauges readiness to defend against a sophisticated adversary

infiltration that employs advanced tradecraft

Cloud Breach Emulation and Response Exercise | Helps your team quickly uncover gaps and sharpen

its response to cloud threats

TECHNICAL ASSESSMENT SERVICES

Audits and addresses security gaps across endpoints, cloud, and SaaS applications to tangibly

reduce risk

Technical Risk Assessment | Highlights security vulnerabilities, weaknesses, and gaps in the IT

environment across endpoint devices, applications, and user identities

Identity Security Assessment | Audits identity security practices and defense posture for weaknesses,

including Active Directory domain configuration, account configuration, privilege delegation, and

potential attack paths

Cloud Security Assessment | Identifies misconfigurations and vulnerabilities in the cloud estate that

could be exploited by adversaries

Compromise Assessment | Exposes and addresses undetected threat activity through a one-time

threat hunt available for endpoint, cloud, and SaaS applications

SaaS Threat Services | Assesses SaaS environments for security gaps across configurations,

access controls, data policies, and third-party integrations

TRAINING AND SECURITY UPSKILLING

Builds security acumen and closes the skills gap through CrowdStrike University, offering on-demand

training, personalized learning paths, and five certifications for deep Falcon module expertise

CROWDSTRIKE PULSE SERVICES

Provides continuous consulting engagements via focused sessions on a recurring cadence (biweekly,

monthly, or every two months) tailored to your needs, aligned with your priorities, and adapted as

needed, enabling consistent progress, improved resilience, and strategic maturity that evolves at the

speed of the adversary

CROWDSTRIKE 2025 THREAT HUNTING REPORT
CROWDSTRIKE 2025 THREAT HUNTING REPORT

53

About
CrowdStrike

CrowdStrike (Nasdaq: CRWD), a global cybersecurity leader, has redefined

modern security with the world’s most advanced cloud-native platform

for protecting critical areas of enterprise risk — endpoints and cloud

workloads, identity and data.

Powered by the CrowdStrike Security Cloud and world-class AI, the

CrowdStrike Falcon® platform leverages real-time indicators of attack,

threat intelligence, evolving adversary tradecraft and enriched telemetry

from across the enterprise to deliver hyper-accurate detections,

automated protection and remediation, elite threat hunting and prioritized

observability of vulnerabilities.

Purpose-built in the cloud with a single lightweight-agent architecture,

the Falcon platform delivers rapid and scalable deployment, superior

protection and performance, reduced complexity and immediate time-to-

value.

CrowdStrike: We stop breaches.

Learn more: www.crowdstrike.com

Follow us: Blog | X | LinkedIn | Facebook | Instagram | YouTube

Start a free trial today: www.crowdstrike.com/free-trial-guide

© 2025 CrowdStrike, Inc. All rights reserved.