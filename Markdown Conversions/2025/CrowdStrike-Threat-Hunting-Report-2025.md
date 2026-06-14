# CrowdStrike 2025 Threat Hunting Report

## Table of Contents
- [Introduction](#introduction)
- [Naming Conventions](#naming-conventions)
- [Front-Line Snapshot](#front-line-snapshot)
- [Sector Targeting](#sector-targeting)
- [Sector Spotlights](#sector-spotlights)
- [MITRE ATT&CK Observations](#mitre-attck-observations)
- [Intrusion Trends by Adversary](#intrusion-trends-by-adversary)
- [Observations from the Front Lines](#observations-from-the-front-lines)
- [Hunting Cross-Domain Adversaries](#hunting-cross-domain-adversaries)

---

## Introduction
A new era of cyber threats has emerged with the rise of the “enterprising adversary,” as highlighted in the CrowdStrike 2025 Global Threat Report. This new breed of threat actor distinguishes itself through sophisticated and scalable tactics designed to execute attacks with calculated, business-like efficiency.

Innovation is a critical cornerstone to outmaneuver and disrupt the enterprising adversary. Today's enterprising adversary is adept at bypassing traditional cybersecurity defenses, exploiting human factors through sophisticated social engineering—often enhanced by AI—and moving to unmanaged devices.

The CrowdStrike Counter Adversary Operations team brings together industry-leading threat intelligence and best-in-class managed threat hunting with the AI-powered CrowdStrike Falcon® platform.

## Naming Conventions
| Adversary Category | Naming Convention |
| :--- | :--- |
| Russia | BEAR |
| Vietnam | BUFFALO |
| DPRK (North Korea) | CHOLLIMA |
| ROK (Republic of Korea) | CRANE |
| Syria | HAWK |
| Hacktivist | JACKAL |
| Iran | KITTEN |
| Pakistan | LEOPARD |
| Georgia | LYNX |
| Colombia | OCELOT |
| People’s Republic of China | PANDA |
| Kazakhstan | SAIGA |
| Egypt | SPHINX |
| eCrime | SPIDER |
| India | TIGER |
| Türkiye | WOLF |

## Front-Line Snapshot
The statistics in this report focus on interactive intrusions—attacks where adversaries establish an active presence within a target network, often engaging in hands-on-keyboard activities.

![Anatomy of an interactive intrusion: Manual intervention, persistence, lateral movement, data exfiltration, and customization.]

## Sector Targeting
The technology sector remained the most frequently targeted industry for the eighth consecutive year. 

![Chart showing targeted sectors by intrusion frequency, highlighting Technology, Consulting & Professional Services, and Manufacturing.]

## Sector Spotlights
- **Government**: Observed a 71% increase in overall interactive intrusions and a 185% increase in nation-state activity, largely attributed to Russia-nexus adversaries like PRIMITIVE BEAR and VENOMOUS BEAR.
- **Telecommunications**: Observed a 53% increase in overall interactive intrusions and a 130% increase in nation-state activity, primarily driven by China-nexus adversaries.
- **Manufacturing and Retail**: Observed notable increases in eCrime interactive intrusions (55% and 41% respectively), with CURLY SPIDER emerging as a prominent threat actor.

## MITRE ATT&CK Observations
CrowdStrike OverWatch tracks interactive intrusion activity against the MITRE ATT&CK® Enterprise Matrix. While Defense Evasion is the most common tactic observed, five of the top 10 techniques are Discovery techniques, highlighting the adversary's need to orient themselves within a network.

![MITRE ATT&CK heat map highlighting top techniques including Valid Accounts, Command and Scripting Interpreter, and Masquerading.]

## Intrusion Trends by Adversary
CrowdStrike maintains detailed information on more than 265 attributed eCrime, nation-state, and hacktivist adversaries.

![Table of most intrusive adversaries categorized by sector and type.]

## Observations from the Front Lines
### Countering the Adversary: Generative Artificial Intelligence
Enterprising threat actors have capitalized on GenAI models to conduct social engineering, technical operations, and information operations. 

**FAMOUS CHOLLIMA** leads in GenAI-supported operations, particularly in insider threat activities where operatives obtain fraudulent employment as remote software developers. They utilize GenAI for:
- **Applications**: Drafting résumés and cover letters.
- **Interviews**: Using real-time deepfake technology to mask identities.
- **On the Job**: Using code assistants and translation tools to manage multiple jobs simultaneously.

## Hunting Cross-Domain Adversaries
Cross-domain threat hunting enables the detection of adversary activities that span identity systems, endpoints, and cloud environments. 

### Case Study: Disrupting BLOCKADE SPIDER
CrowdStrike OverWatch identified that BLOCKADE SPIDER accessed a victim’s network via an unmanaged VPN appliance. By leveraging identity data and Falcon Next-Gen SIEM, hunters tracked the adversary as they pivoted between on-premises systems and cloud environments, eventually shutting down their access.

![Diagram of BLOCKADE SPIDER cross-domain attack path, showing movement from VPN to Active Directory and cloud IAM environments.]

---
*Note: This report covers trends identified from July 1, 2024, to June 30, 2025.*

---

e
quick reaction times necessary for defenders to stop
BLOCKADE SPIDER and other fast-moving adversaries
in the early stages of intrusions.

CROWDSTRIKE 2025 THREAT HUNTING REPORT 25
CASE STUDY:
Hunting OPERATOR PANDA
To hunt for enterprising adversaries such as China-nexus OPERATOR PANDA,
also known as Salt Typhoon, defenders can benefit from correlating data across
multiple sources, especially from devices beyond the scope of traditional EDR
coverage, such as routers, switches, VPN appliances, and firewalls. OPERATOR
PANDA often gains initial access through internet-facing applications, like Cisco
switches, which are known blind spots not covered by EDR.
In mid-November 2024, OPERATOR PANDA targeted a U.S.-based
telecommunications entity and a U.S.-based consulting and professional services
entity. During both intrusions, the adversary gained initial access by exploiting
Cisco switches running Cisco IOS and Cisco IOS XE, widely used software for
Cisco network appliances. To further hinder detection of their activity, OPERATOR
PANDA sanitized logs from the Cisco switches they had compromised.
OPERATOR PANDA is also known to chain vulnerabilities to achieve their
objectives. For example, they leveraged CVE-2023-20198 to create a local
user account, which they then exploited to abuse another vulnerability,
CVE-2023-20273, in a different component of the Cisco web UI feature.
This allowed the adversary to inject commands with root privileges,
enabling them to run arbitrary commands on the device.
The introduction of Falcon Next-Gen SIEM logs and telemetry to the toolkit
of CrowdStrike OverWatch hunters allows them to develop new hunting equities
to look for anomalous activity on these devices. The added context provided by
next-gen SIEM data paints a more detailed, comprehensive picture of adversary
activity for threat hunters and has the potential to shift detection forward in
the attack timeline.
Outlook
Armed with data from multiple sources ingested into next-gen SIEM tools, threat
hunters can identify, track, and disrupt elusive adversaries such as BLOCKADE
SPIDER and OPERATOR PANDA, despite their sophisticated hands-on-keyboard
tradecraft and minimal endpoint footprint.
Any blind spots constitute critical weaknesses in defensive postures and allow
evasive adversaries to avoid detection and stealthily impact victims. Falcon
Next-Gen SIEM equips threat hunters with the capability to hunt across these
blind spots. Leveraging next-gen SIEM data will be key to defeating sophisticated
adversaries in the future.

CROWDSTRIKE 2025 THREAT HUNTING REPORT 26
IDENTITY HUNTING
Vishing and help desk social engineering have continued to play a dominant role in eCrime operations in 2025.
Adversaries are bypassing traditional security measures by exploiting human weaknesses, leveraging compromised
credentials and social engineering to gain initial access and move laterally within organizations. It is difficult for a
single security tool to distinguish between a legitimate employee and an adversary using stolen credentials,
leaving organizations vulnerable to identity-driven attacks. The rise of this social engineering trend was identified
in the CrowdStrike 2025 Global Threat Report, and in the first half of 2025, vishing attacks have already surpassed
the total number seen in 2024. This means that vishing is on track to double last year's volume by the end of 2025.
JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC JAN FEB MAR APR MAY JUN
2024 2025
Figure 10. Vishing attacks observed by month, January 2024-June 2025
Identity protection is a force multiplier in countering vishing attacks. By correlating activity across multiple domains —
including third-party data for phishing detection with next-gen SIEM capabilities — organizations can uncover suspicious
behaviors indicative of compromise. Proactive, intel-driven threat hunting across domains aids rapid detection and
disruption of adversary activity before it escalates.

CROWDSTRIKE 2025 THREAT HUNTING REPORT 27
ADVERSARY SPOTLIGHT:
SCATTERED SPIDER
Following a period of relative inactivity between December 2024 and March 2025, SCATTERED SPIDER returned
in April 2025 with aggressive ransomware campaigns targeting the U.K. and U.S. aviation, insurance, and retail
sectors. In most 2025 incidents to date, the adversary has leveraged help desk social engineering to gain initial
access, a technique they first used in 2023 and have since matured, leading to its widespread adoption by
multiple distinct eCrime actors.
In help desk social engineering, a threat actor impersonates a legitimate employee in a call to a targeted
organization’s help desk and requests a password and/or MFA method reset. Once the SCATTERED SPIDER caller
has passed identity verification questions, the help desk agent provides a temporary password over the phone
and/or revokes the existing MFA device or method, enabling the adversary to authenticate and configure their
own device for MFA. SCATTERED SPIDER typically uses help desk social engineering to compromise Microsoft
Entra ID, single sign-on (SSO), and virtual desktop infrastructure accounts.
During these calls, SCATTERED SPIDER has impersonated targeted organizations’ legitimate employees
and accurately provided the impersonated individuals’ employee IDs in response to the help desks’ identity
verification questions. SCATTERED SPIDER and other eCrime actors have also routinely demonstrated the ability
to acquire personally identifiable information to pass help desk verification questions. In one call where the
adversary could not provide the impersonated employee’s ID, the threat actor offered to provide the employee’s
date of birth and Social Security number as alternative verification credentials.
00:00:00
First successful
SCATTERED SPIDER
authentication to
compromised account
00:00:30
Registers own
device for MFA
00:01:00
Pivots to Microsoft
365 applications
SCATTERED SPIDER 00:02:00
calls help desk to Deletes email notifying
request password legitimate account owner of
and/or MFA reset enrollment of new MFA device
0 min 1 min 2 min 3 min 4 min 5 min
00:04:30
Performs Entra ID
bulk user export
00:03:00
Searches Microsoft
SharePoint for credentials
and network architecture
documentation
Figure 11. Timeline of SCATTERED SPIDER social engineering attack

CROWDSTRIKE 2025 THREAT HUNTING REPORT 28
Within minutes of performing the account takeover, SCATTERED SPIDER
operators can often be observed leveraging these accounts to pivot to integrated
software as a service (SaaS) applications, including data warehousing, document
management and storage, and IAM platforms. These serve as a foothold for
persistence, lateral movement, and data exfiltration techniques.
SCATTERED SPIDER often compromises accounts belonging to targeted
organizations’ IT and security staff, as these employees typically have access
to documentation on network architecture, security tooling, and incident response
procedures. The adversary has also targeted C-suite executives’ accounts,
likely due to their access to sensitive data, communications, and other
resources that may support data theft and extortion.
When SCATTERED SPIDER logs in to compromised accounts, they often configure
residential proxies (such as NSOCKS) to appear as though they are logging in
from the same geographical area and with the same user agent as the legitimate
account owner. The adversary also often compromises accounts outside of typical
local business hours, likely to enable the longest possible access to the account
before the legitimate user reports being locked out.
Account Takeover to Ransomware in 24 Hours
SCATTERED SPIDER continues to pursue ransomware deployment and data theft
and extortion as monetization methods in 2025. In one 2025 incident in which
SCATTERED SPIDER deployed ransomware, the adversary progressed from initial
access to encryption in approximately 24 hours. This progression is significantly
quicker than the adversary’s average time between their first interaction with
victims and either ransomware execution or adversary eviction in 2024 and
2023 — approximately 35.5 hours and 85 hours, respectively.
The adversary excels at using identity compromise to pivot between multiple
surfaces in a network, evading targeted organizations’ heavily monitored
endpoints. This includes performing bulk exports of Entra ID data, obtaining
credentials from privileged access management (PAM) applications, and even
performing help desk social engineering calls during the intrusion to gain access
to accounts with higher privileges. In one technique seen in most SCATTERED
SPIDER intrusions, the adversary attaches domain controller virtual machine (VM)
hard disks to unmanaged adversary-controlled VMs to dump ntds.dit without
being detected by host-based security tooling.
Countering SCATTERED SPIDER
Countering SCATTERED SPIDER requires a multi-domain approach
to threat hunting, as the adversary minimizes time spent on endpoints.
Though compromising identities is SCATTERED SPIDER’s preferred method
of initial access, examining identity data is only part of the overall puzzle that
threat hunters must consider.

CROWDSTRIKE 2025 THREAT HUNTING REPORT 29
ENDPOINT IDENTITY
SCATTERED SPIDER maneuvered away from operations Identity data enables threat hunters to follow
on the endpoint, maintaining a minimal footprint SCATTERED SPIDER across a compromised
environment
Threat hunters may only see SCATTERED SPIDER on the
endpoint when they pivot from other domains Identity data can:
Successful hunting requires context from other domains Pinpoint where SCATTERED SPIDER interacts with
to connect activity systems outside a user’s standard working hours
Provide insight into SCATTERED SPIDER’s next
target based on the context of the account used
NEXT-GEN SIEM and other identities the adversary enumerates
Next-gen SIEM provides threat hunters with Identity-specific hunting for privilege escalation
visibility spanning multiple domains when logs are tools and TTPs can help hunters track and predict
available: SCATTERED SPIDER’s next move
VMware logs highlight tunneling tooling on ESXi
hosts and credential harvesting activity
THE PUZZLE
IAM logs allow hunters to observe SCATTERED
SPIDER authenticating to SSO-enabled OF DETECTING
applications
Firewall logs allow hunters to identify where SCATTERED SPIDER
tunneling traffic is originating
SOFTWARE AS A SERVICE APPLICATIONS AND
PLATFORMS
SaaS applications often span multiple hunting domains
SCATTERED SPIDER uses compromised SaaS platforms CLOUD
to attain persistence and store data for later exfiltration
Cloud data helps threat hunters identify
SaaS data allows hunters to: SCATTERED SPIDER’s presence in Entra ID
and Azure
Detect suspicious access to highly sensitive
documents in documented sharing and storage Threat hunters can look for suspicious
platforms such as SharePoint and OneDrive new VM creation events and new MFA
device additions, correlating this activity
Search for suspicious access requests to, and usage with unusual patterns of password resets
of, database platforms
Self-service password reset (SSPR)
Look for signs of suspicious access to PAM platforms enumeration can help uncover help desk
to harvest credentials phishing
Figure 12. Hunting SCATTERED SPIDER across domains

CROWDSTRIKE 2025 THREAT HUNTING REPORT 30
To defend against adversaries like SCATTERED SPIDER, organizations should adopt the following
proactive measures:
• Identity Protection: Use phishing-resistant MFA (avoiding SMS-based methods), isolate privileged accounts
from regular workflows, strengthen password reset procedures, and restrict help desk involvement in MFA
enrollment.
• Detection and Monitoring: Continuously monitor for authentication anomalies, administrative changes, and
unusual network traffic to critical systems; enable comprehensive logging and behavioral analytics; and watch
for suspicious application usage, search terms, and data access patterns that could indicate malicious activity.
• Infrastructure Security: Secure VMware environments, segment networks to contain potential intrusions,
block the use of unauthorized tools, apply least-privilege access across cloud environments, and disable
outdated or legacy authentication methods.
• Incident Readiness: Maintain isolated and regularly tested backups, develop and rehearse incident response
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
9 An ORB network is a traffic relay system — generally composed of a mix of compromised devices and leased servers — used to obfuscate
the origin and destination of malicious traffic

| CROWDSTRIKE 2025 THREAT HUNTING REPORT |     |     |     |     |     |     |     | 31  |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
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
Initial Access Execution Persistence Privilege Escalation Defense Evasion
| T1078.004 |     | T1651 |     | T1098.004 |     | T1078.004 | T1550.001 |     |
| --------- | --- | ----- | --- | --------- | --- | --------- | --------- | --- |
Valid Accounts: Cloud  Cloud Administration Account Manipulation: Valid Accounts: Cloud  Use Alternate
Accounts Command SSH Authorized Keys Accounts Authentication Material:
Application Access Token
|     | T1190 |     |     | T1098.001 |     | T1098.003 |     |     |
| --- | ----- | --- | --- | --------- | --- | --------- | --- | --- |
Exploit Public-Facing Account Manipulation: Account Manipulation: T1562.007
Application Additional Cloud Additional Cloud Roles Impair Defenses: Disable
|     |     |     |     | Credentials |     |     | or Modify Cloud Firewall |     |
| --- | --- | --- | --- | ----------- | --- | --- | ------------------------ | --- |
T1195
| Supply Chain Compromise |     |     |       |     |     |     | T1070             |     |
| ----------------------- | --- | --- | ----- | --- | --- | --- | ----------------- | --- |
|                         |     |     | T1619 |     |     |     | Indicator Removal |     |
Cloud Storage Object
Discovery
T1552.005
|     | Unsecured Credentials:  |     | T1016 |     | T1114.002 |     |     |     |
| --- | ----------------------- | --- | ----- | --- | --------- | --- | --- | --- |
Cloud Instance Metadata  System Network  Email Collection: Remote  T1090.002
|     |                   | Configuration Discovery |           |     | Email Collection |                       |     |     |
| --- | ----------------- | ----------------------- | --------- | --- | ---------------- | --------------------- | --- | --- |
|     | API               |                         |           |     |                  | Proxy: External Proxy |     |     |
|     | Credential Access |                         | Discovery |     | Collection       | Command and Control   |     |     |
YEK
|     |     |     | MURKY PANDA | GENESIS PANDA |     | BOTH |     |     |
| --- | --- | --- | ----------- | ------------- | --- | ---- | --- | --- |
Figure 13. Prevalent MITRE ATT&CK TTPs used by MURKY PANDA and GENESIS PANDA

CROWDSTRIKE 2025 THREAT HUNTING REPORT 32
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
2024 MAR APR JUN OCT NOV 2025 MAR MAY
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
YEK Cloud-conscious activity by threat actor
targeting cloud services
Cloud-supporting activity by threat actor abusing
cloud services to support their operations
Since at least March 2024, GENESIS PANDA has proven increasingly capable of using cloud services to support tool
deployment, command and control (C2) communications, and exfiltration. The adversary has also proven capable of
targeting cloud service provider (CSP) accounts to expand access and establish alternate forms of persistence. In
addition to hosting data on cloud services, GENESIS PANDA uses cloud infrastructure to exfiltrate the output of basic
discovery commands.

CROWDSTRIKE 2025 THREAT HUNTING REPORT 33
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

CROWDSTRIKE 2025 THREAT HUNTING REPORT 34
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

CROWDSTRIKE 2025 THREAT HUNTING REPORT 35
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

CROWDSTRIKE 2025 THREAT HUNTING REPORT 36
CASE STUDY:
Hunting GLACIAL PANDA Living off the Land
GLACIAL PANDA highly likely conducts targeted intrusions for intelligence collection purposes, accessing and exfiltrating
call detail records and related communications telemetry from multiple telecommunications organizations. This activity
could have significant privacy implications for the organizations’ customers. The adversary primarily targets Linux
systems typical in the telecommunications industry, including legacy operating system distributions that support older
telecommunications technologies.
GLACIAL PANDA
Target
Notable TTPs Geography
Initial access via internet-facing (and frequently unmanaged) servers, Afghanistan
likely achieved through software exploitation or weak password provisioning
Hong Kong
Primarily targets Linux systems, employing LOTL techniques and abusing
India
legitimate user accounts for lateral movement and persistence
Japan
Deploys ShieldSlide trojanized OpenSSH components to collect user
authentication sessions and credentials Kenya
Collects telecom sector-specific data, including call detail records, Malaysia
network telemetry, and error logs
Mexico
Panama
Vulnerabilities Exploited Target Sectors
Philippines
CVE-2016-5195 vulnerability (aka Dirty COW) Telecommunications Taiwan
CVE-2021-4034 vulnerability (aka PwnKit) Thailand
U.S.
Figure 15. GLACIAL PANDA: TTPs and targets

CROWDSTRIKE 2025 THREAT HUNTING REPORT 37
GLACIAL PANDA activity is characterized by interactive intrusion tradecraft that prioritizes persistence and stealth.
This adversary is known to use:
• Living off the land (LOTL) techniques that leverage common Linux system tools
• Legitimate user account abuse for initial host access and lateral movement
• Trojanized OpenSSH suite tools to capture user credentials and provide backdoor access
• Trojanized cron daemons to hide adversary-configured jobs
• External C2 via reverse shell connections using netcat or a publicly available Perl script
• Access propagation between interconnected organizations, such as company subsidiaries or business relationships
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

CROWDSTRIKE 2025 THREAT HUNTING REPORT 38
To hunt for and protect against threats like GLACIAL PANDA,
CrowdStrike recommends the following measures:
• Update software on supported operating systems regularly by employing
rigorous patch management policies, and migrate end-of-life (EOL) systems to
versions with vendor update support wherever possible.
• Monitor legacy or EOL assets that no longer receive security or software
updates, particularly for unusual network activity to and from these hosts.
• Monitor legitimate system binaries for malicious modifications, including
/usr/bin/ssh, /usr/sbin/sshd, /usr/sbin/cron, and OpenSSH
pluggable authentication modules.
• Monitor SSH connections between hosts for anomalous activity, limiting which
user accounts are allowed to log in via SSH.
• Enforce network access control policies for servers according to role and
requirement.
• Enforce complex account password strategies — avoiding default or
generic options — for SSH authentication, and employ more secure methods
such as SSH key authentication, particularly on remotely accessible servers.
Limit situations in which server credentials (e.g., for databases) are stored
unencrypted on hosts.
• Deploy CrowdStrike Falcon® Insight XDR on compatible hosts, ensuring
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

CROWDSTRIKE 2025 THREAT HUNTING REPORT 39
CASE STUDY:
Hunting GRACEFUL SPIDER’s Zero-Day
A series of incidents impacting Cleo data transfer products in late 2024 highlights the intersection of detection
deployment and development, exposure management, extended detection and response (XDR), threat hunting,
and threat intelligence. On Saturday, December 7, 2024, CrowdStrike OverWatch detected suspected exploitation
of multiple Cleo products on Windows and Linux servers. The team observed compromises across Cleo instances in
multiple sectors and geographies. Based on the targets, speed, scope, and tactics demonstrated by the threat actor
during the initial wave, CrowdStrike Intelligence determined the activity was likely a zero-day file upload exploit
leading to remote code execution related to an earlier vulnerability.
DEC 7 DEC 13
Cleo zero-day Cleo discloses
bypasses patch CVE-2024-55956
DEC 7
+10 min: CrowdStrike DEC 15
GRACEFUL SPIDER
OverWatch customers notified
claims responsibility
DEC 7
+1 hr: CrowdStrike OverWatch
detections implemented
DEC 9
Falcon sensor
preventions
OCT 27 DEC 11
Cleo discloses Zero-day exploit
CVE-2024-50623 published
2024 OCT NOV DEC
Exploit Development and Testing Zero-Day Campaign Opportunistic Campaign
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

CROWDSTRIKE 2025 THREAT HUNTING REPORT 40
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

CROWDSTRIKE 2025 THREAT HUNTING REPORT 41
To hunt for and protect against threats from emerging exploit campaigns,
CrowdStrike recommends the following measures:
• Deploy EDR/XDR capabilities on compatible hosts to ensure maximum visibility
and coverage across the network environment.
• Inventory and review enterprise assets to ensure visibility across the
organization.
• Identify vulnerable assets through continuous exposure assessment and
vulnerability scanning.
• Monitor externally exposed assets for signs of risk or potential compromise.
• Update software by using intelligence-driven patch management policies that
prioritize exposed assets with known exploited vulnerabilities.
• Enforce script execution policies on supported platforms to block PowerShell
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

CROWDSTRIKE 2025 THREAT HUNTING REPORT 42
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

CROWDSTRIKE 2025 THREAT HUNTING REPORT 43
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

CROWDSTRIKE 2025 THREAT HUNTING REPORT 44
RReeccoommmmeennddaattiioonnss
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

CROWDSTRIKE 2025 THREAT HUNTING REPORT 45
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

CROWDSTRIKE 2025 THREAT HUNTING REPORT 46
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

CROWDSTRIKE 2025 THREAT HUNTING REPORT 47
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

CROWDSTRIKE 2025 THREAT HUNTING REPORT 48
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

CROWDSTRIKE 2025 THREAT HUNTING REPORT 49
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

CROWDSTRIKE 2025 THREAT HUNTING REPORT 50
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

CROWDSTRIKE 2025 THREAT HUNTING REPORT 51
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

CROWDSTRIKE 2025 THREAT HUNTING REPORT 52
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

CROWDSTRIKE 2025 THREAT HUNTING REPORT 53
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