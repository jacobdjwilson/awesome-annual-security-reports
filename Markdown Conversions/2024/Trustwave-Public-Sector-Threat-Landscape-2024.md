# 2024 Public Sector Threat Landscape

## Table of Contents
- [Executive Summary](#executive-summary)
- [Emerging and Prominent Trends](#emerging-and-prominent-trends)
- [Double-Edged Sword of Emerging Technologies](#double-edged-sword-of-emerging-technologies)
- [Convergence of IT and OT in Critical Infrastructure](#convergence-of-it-and-ot-in-critical-infrastructure)
- [Access and Data Brokers and the Dark Web](#access-and-data-brokers-and-the-dark-web)
- [Dissecting the Attack Flow for the Public Sector](#dissecting-the-attack-flow-for-the-public-sector)
- [Attack Flow Overview](#attack-flow-overview)
- [Attack Flow Steps](#attack-flow-steps)
- [Initial Foothold: Phishing, Spam & Scams](#initial-foothold-phishing-spam--scams)
- [Initial Foothold: Logging in](#initial-foothold-logging-in)
- [Initial Foothold: Vulnerability Exploitation](#initial-foothold-vulnerability-exploitation)
- [Initial Foothold: Supply Chain](#initial-foothold-supply-chain)
- [Initial Payload](#initial-payload)
- [Expansion / Pivoting](#expansion--pivoting)
- [Malware: Loaders, Infostealers and RATs](#malware-loaders-infostealers-and-rats)
- [Malware: Ransomware](#malware-ransomware)
- [Exfiltration / Post Compromise/Impact](#exfiltration--post-compromiseimpact)
- [Key Takeaways and Recommendations](#key-takeaways-and-recommendations)

---

## Executive Summary

Societies depend on government institutions to deliver stability, continuity, and security. However, cyberattacks can disrupt these vital functions. Robust cybersecurity is the cornerstone of public trust. It ensures the vast amount of sensitive data governments hold, which underpins the smooth operation of society, remains safe.

The effects of public sector cyberattacks can differ starkly from those targeting private corporations. Breaches can disrupt essential services that citizens rely on daily, from healthcare and social security to law enforcement and national defense. This can upset the very fabric of society and erode public confidence in government institutions, potentially hindering cooperation and creating a climate of fear and uncertainty. The risk to individuals is compounded by the need for us all to provide large quantities of our personal information to the government.

Furthermore, successful cyberattacks on critical infrastructure, such as power grids or transportation systems, can have a ripple effect, causing widespread economic disruption, jeopardizing public safety, and even endangering lives.

In March 2024, the White House stated that critical infrastructure, specifically water and wastewater systems, are major targets for state-sponsored threat actors. In May 2023, the Five Eyes intelligence alliance (US, UK, Canada, Australia, New Zealand) and Microsoft said a state-sponsored Chinese hacking group was spying on US critical infrastructure organizations. In October 2023, a ransomware attack by Rhysida Group forced the UK's national library to close and will cost it 40% of their financial reserves to recover after they refused to pay the ransom.

Public sector cybersecurity is a complex landscape with a number of unique factors, including:

- **Legacy and Diverse Systems**: Public sector agencies often rely on outdated legacy systems that were built without modern cybersecurity threats in mind. These systems can be difficult and expensive to patch or upgrade, and many are managed by private entities, with very little standardization, making them prime targets for exploitation.
- **Focus on Public Service**: In pursuit of public service, government agencies may prioritize accessibility and user convenience over stringent security measures. This pursuit can leave them vulnerable to phishing attacks or social engineering tactics that prey on unsuspecting employees.
- **Fragmented IT Infrastructure**: Public sector organizations can have complex and sprawling IT infrastructures with multiple departments and agencies using different systems. This fragmentation can create blind spots and make it difficult to implement consistent security policies across the board.
- **Data Trove**: Public sector agencies hold a massive amount of sensitive data on citizens, including Social Security numbers, financial information, and medical records. This data is highly valuable to cybercriminals who can use it for identity theft, financial fraud, or further cyberattacks.
- **Siloed Information Stores**: Public sector agencies have traditionally been the keepers of their own data, with a growing requirement to link and pool data, there is a risk of hidden connections being inadvertently exposed.
- **Limited Budgetary Resources**: Budgetary constraints often restrict the ability of public sector organizations to invest in the latest cybersecurity technologies and skilled personnel. These financial issues leave them vulnerable to attacks that exploit known weaknesses.
- **Regulatory Compliance**: Public sector agencies are subject to a complex web of regulations governing data privacy and security. Balancing compliance with effective cybersecurity practices can be a challenge.
- **International Focus**: Public sector networks can be targeted by foreign governments or state-sponsored actors engaged in espionage or cyberwarfare. This adds another layer of complexity to the cybersecurity landscape.

To ensure comprehensive coverage, this report examines cybersecurity challenges facing the public sector globally, which encompasses government institutions (ranging from libraries to national defense) and essential public services (ranging from law enforcement to infrastructure).

Leveraging the expertise of hundreds of security researchers, Trustwave SpiderLabs is uniquely positioned to analyze the evolving threat landscape. Our team identifies tens of thousands of vulnerabilities each year, performs thousands of penetration tests, and analyzes millions of phishing URLs daily.

This comprehensive coverage across information security disciplines – including continuous threat hunting, forensics, incident response, malware analysis, and database security – empowers us to not only understand how breaches occur, but also recommend effective mitigations and controls for organizations.

This report delves into the critical trends impacting the public sector, including the rise of emerging technologies, risks to critical infrastructure, and the increased sale of public sector assets on the Dark Web. We'll then dissect the attack flow specific to public sector entities, providing actionable intelligence, and tailored mitigation strategies at each stage.

---

## Emerging and Prominent Trends

## Double-Edged Sword of Emerging Technologies

### The Threat
Emerging technologies like generative AI and quantum computing present a double-edged sword for public-sector cybersecurity. While they offer promising possibilities for efficiency and innovation, they also raise significant security concerns should the public sector be slow to adopt them and subsequently left behind.

### What Trustwave SpiderLabs Is Seeing
AI-powered threats like hyper-realistic misinformation and social engineering attacks could manipulate public opinion and steal sensitive data. Although still in its early stages, Quantum computing could crack current encryption, jeopardizing government communications and citizen data.

However, the public sector can leverage these technologies for good. AI can be used for advanced threat detection, analyzing vast amounts of data to predict and prevent cyberattacks. Automation powered by AI can free up human resources for more complex tasks.

Moreover, the public sector also bears the added burden of adapting regulations and guidance to this evolving landscape. It's crucial to understand that traditional approaches may not be sufficient for the rapid pace of innovation. Here's what the public sector might consider:

- **Focus on security by design**: Implementing regulations that require developers to prioritize secure coding practices from the outset.
- **Standardization for post-quantum cryptography**: Encouraging research and collaboration to develop and adopt new, quantum-resistant encryption standards.
- **Transparency and accountability**: Developing frameworks that hold tech companies accountable for potential security risks associated with their products and services.
- **International collaboration**: Cyber threats transcend borders. Establishing international cooperation and information sharing is crucial for a unified approach to regulating emerging technologies.

### Mitigations to Reduce Risk
- Leverage AI for advanced threat detection and automation.
- Regulate for secure-by-design in emerging technologies.
- Increase transparency across development and hold tech companies accountable for offerings.
- Foster international collaboration on cyber threats and regulations.
- Train public sector staff and citizens on AI threats.
- Implement robust cybersecurity frameworks (zero-trust, MFA, data security).
- Repeatedly test incident response and business continuity plans to ensure they will work as expected when needed.

---

## Convergence of IT and OT in Critical Infrastructure

### The Threat
Critical infrastructure faces a complex web of security threats. The vast number of entities involved in ownership and management, from small local utilities to federal agencies, can contribute to vulnerabilities. Many critical infrastructure systems are decades old and haven't been updated due to cost concerns, making them more susceptible to attack. Additionally, cybersecurity hasn't always been a high priority for infrastructure owners.

The rise of cyber threats poses a significant danger. The lack of standardized equipment from different vendors can create issues with configuration management and contribute to security gaps. Additionally, the merging of IT and OT systems increases the attack surfaces for criminals. These systems are often inadequately segmented, allowing attackers to move freely within a network.

### What Trustwave SpiderLabs Is Seeing
The convergence of IT and OT systems has created new security challenges. Many organizations mistakenly believed their OT systems were isolated from cyber threats because they were air gapped. This led to a relaxed approach to patching and updating legacy systems.

- **Limited Asset Management**: Organizations often lack a comprehensive understanding of their OT environment. They may not have a complete inventory of all systems and their configurations.
- **Patching Challenges**: Legacy OT systems often present unique patching difficulties. These systems may be one-of-a-kind and critical to operations, making downtime for patching risky.
- **Resilience and Response**: Building redundancy into critical infrastructure systems is crucial for maintaining resilience in the face of cyberattacks.
- **The Role of Government**: Governments can play a crucial role in assisting critical infrastructure owners and operators by providing resources for technical testing and helping entities build resilience.

### Mitigations to Reduce Risk
- Prioritize a complete understanding of critical infrastructure environment, including OT systems, assets, configurations, and connections.
- Evaluate and understand the connections and functionalities of all third-party vendors involved in critical infrastructure operations.
- Acknowledge resource limitations and prioritize protection of the most critical systems and functionalities.
- Implement continuous monitoring of critical infrastructure systems to identify suspicious activity and potential vulnerabilities.
- Develop and test comprehensive backup and incident response plans to ensure a swift recovery from cyberattacks.
- Provide training programs to educate personnel on social engineering tactics and how to identify and prevent them.
- Conduct penetration or offensive testing to identify weaknesses so they can be mitigated before they are exploited.

---

## Access and Data Brokers and the Dark Web

### The Threat
A disturbing trend has emerged on the Dark Web: a significant increase in the sale of public sector assets. This includes highly sensitive data such as citizen information, law enforcement databases, election data, and more.

### What Trustwave SpiderLabs Is Seeing
Trustwave researchers found significant volumes of trade in valid accounts and access credentials pertaining to infrastructure, networks, and systems related to public sector organizations on the Dark Web.

![Image: Threat actor offering Argentinian Municipal Electoral Registry from 2023]

### Mitigations to Reduce Risk
- Databases that store sensitive data should be prioritized for robust security controls. Database security tools like Trustwave’s DbProtect that can flag misconfiguration and user rights can also help reduce risk.
- Ensure the appropriate level of protection is applied based on the criticality of information. Implement data protection controls such as data encryption in assets that need to be protected.
- Ensure appropriate segmentation, segregation, and apply Zero Trust principles are in place.
- Ensure that up-to-date backups are available as a contingency to recover from a worst-case scenario.
- Monitor the Dark Web regularly for potential compromises and have a robust incident response process to contain and manage incidents.

---

## Dissecting the Attack Flow for the Public Sector

## Attack Flow Overview
Data breaches and compromises come in many forms, but they often follow a similar pattern. Attackers gain access, escalate privileges, establish a foothold, steal, or destroy data, and then vanish.

### Attack Flow Steps
1. **Initial Foothold**: The attacker successfully triggers a security bypass.
2. **Initial Payload**: Attackers download more sophisticated tools and malware.
3. **Expansion / Pivoting**: Attackers target higher-value accounts and systems.
4. **Malware**: Deployment of RATs, infostealers, or ransomware.
5. **Exfiltration / Post Compromise**: Data theft and impact.

---

## Initial Foothold: Phishing, Spam & Scams

### The Threat
Public sector organizations are particularly vulnerable to phishing attacks. Unlike exploiting software flaws, attackers target the human element.

### Trustwave SpiderLabs Insights
In the public sector, the top three email attachment file types are HTML, Executables, and PDFs. HTML attachments comprised 78% of observed malicious attachments.

![Image: Top malicious attachment filetypes for the public sector]

- **Malicious Campaigns Targeting Local Government Finance Departments**: BEC and phishing campaigns targeting public sector organizations leveraging fake financial documents.
- **Malicious Campaigns Leveraging Tax Government Offices**: Spikes in tax-related phishing during tax seasons.
- **Fake Government Bidding Scams**: Leveraging "Request for Quotation" or "Invitation to Bid"-themed phishing.
- **Government Refund Phishing**: Impersonating government portals like Australia's "MyGov".
- **Disaster Aid-Themed Phishing**: Leveraging fake relief funds for natural disasters.

### Mitigations to Reduce Risk
- Conduct security awareness sessions to educate employees about the latest phishing tactics.
- Consistently conduct mock phishing tests.
- Implement robust anti-spoofing measures.
- Leverage web filtering and categorization technologies.
- Enable multi-factor authentication (MFA).

---

## Initial Foothold: Logging in

### The Threat
Attackers use stealthier tactics such as phishing, drive-by downloads, exploiting software vulnerabilities, or buying pre-existing access from underground marketplaces.

### Trustwave SpiderLabs Insights
Trustwave researchers found many trades in valid accounts and access credentials pertaining to public sector organizations on the Dark Web, including election systems, government infrastructure, and law enforcement portals.

### Mitigations to Reduce Risk
- Ensure proper security controls around account management, including MFA.
- Regularly monitor external access points (VPN, SSH, RDP).
- Regularly monitor Dark Web sites for possible breaches.
- Restrict access based on the principle of least privilege.
- Implement Privileged Access Management (PAM) solutions.

---

## Initial Foothold: Vulnerability Exploitation

### The Threat
Vulnerability exploitation describes how attackers leverage software bugs to bypass security controls.

### Trustwave SpiderLabs Insights
Apache Log4j and MOVEit Transfer continue to be the most common exploit attempts against public sector organizations.

![Image: Most common exploits detected through Trustwave active monitoring]

### Mitigations to Reduce Risk
- Maintain a rigorous patch management program.
- Conduct regular vulnerability scanning and penetration testing.
- Disable unnecessary services and features on public-facing servers.
- Implement web application firewalls (WAF) to block exploit attempts.

---

## Initial Foothold: Supply Chain
*(Content omitted in source text)*

## Initial Payload
*(Content omitted in source text)*

## Expansion / Pivoting
*(Content omitted in source text)*

## Malware: Loaders, Infostealers and RATs
*(Content omitted in source text)*

## Malware: Ransomware
*(Content omitted in source text)*

## Exfiltration / Post Compromise/Impact
*(Content omitted in source text)*

## Key Takeaways and Recommendations
*(Content omitted in source text)*

[^1]: Trustwave SpiderLabs, 2024 Public Sector Threat Landscape Report.

---

ant Azure AD OAuth applications. The CVSS score is considered critical
at 9.4. Exploitation of this vulnerability may potentially allow full control over
user accounts and thus, compromise sensitive data.

Fig 33: A publicly exposed Grafana instance belonging to a public sector organization

Our researchers also found publicly accessible CPanel instances which could
pose risks to organizations if left unpatched (e.g. CVE-2023-29489) or if
threat actors gain access through valid credentials.

Fig 34: A publicly exposed CPanel instance belonging to a public sector organization

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies42

SERVICE/ASSET MANAGEMENT AND SECURITY SOFTWARE

Trustwave SpiderLabs researchers found publicly accessible Ivanti instances
belonging to public sector organizations. Ivanti has released urgent patches
for two critical vulnerabilities affecting its Standalone Sentry and Neurons for
ITSM solutions. The first, CVE-2023-41724, allows unauthenticated attackers
on the same network to execute arbitrary commands in Standalone Sentry.

The second, CVE-2023-46808, affects Ivanti Neurons for ITSM, enabling
low-privileged accounts to execute commands within the web application’s
user context. Over the past year, these vulnerabilities have drawn attacks
from nation-state actors and other threat groups, leading to emergency
directives from agencies like CISA. These incidents underscore the persistent
threat landscape facing Ivanti devices. As an example, referenced in another
part of this report, we also mention that the Norwegian government verified
that they had exposure through vulnerabilities in Ivanti’s Endpoint Manager
Mobile (EPMM) in 12 of its ministries.

Fig 35: A publicly exposed Ivanti Connect Secure instance belonging to a
public sector organization

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies43

EMAIL SYSTEMS

Our researchers noted various Zimba email servers used by various public
sector organizations. Zimba is particularly interesting since in 2023, third-
party researchers uncovered a zero-day exploit targeting Zimbra. The
vulnerability tracked as CVE-2023-37580 allowed threat actors to steal
email data, user credentials, and authentication tokens. There were multiple
campaigns leveraging this exploit including campaigns targeting government
organizations in Greece, Moldova, Tunisia, Vietnam, and Pakistan, leading to
data theft and credential phishing incidents.

Fig 36: A publicly exposed Zimbra email server belonging to a
public sector organization

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies44

Mitigations to Reduce Risk

 ▪ Regularly update and patch systems to protect against known
vulnerabilities. Promptly patch critical vulnerable systems.

 ▪ Databases that store sensitive data should be a priority for system
and software patching. Database auditing tools like Trustwave’s
DbProtect that can flag misconfiguration and user rights can also
help eliminate risk.

 ▪ Utilize vulnerability assessments and penetration testing to

identify vulnerable servers.

 ▪ Implement strict access controls for critical systems, especially
databases, file servers, email servers, development tools and
network devices. Strengthen access controls to minimum
necessary levels for authorized users.

 ▪ Place all servers behind the firewall and practice proper network

segmentation for enhanced access control. Disable Internet
access for servers that do not require it.

 ▪ Address misconfigurations in network devices and other IoT

devices, ensuring firmware is updated and default passwords are
changed.

 ▪ Provide ongoing cybersecurity training and awareness programs

for employees and all users of digital applications, emphasizing the
importance of security best practices.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesInitial Foothold

Threat Actor

Business Partner

45

Initial Foothold: Supply Chain

The Threat
Rather than a direct assault, today's attackers are exploiting a clever tactic:
the supply chain attack. They target trusted third-party vendors used
by many large organizations. This approach is like a "Domino Risk." By
compromising one vendor, attackers can trigger a chain reaction, impacting
numerous organizations that rely on them.

Think of it as a flanking maneuver. By compromising a less secure third party,
attackers gain a backdoor into their target companies' data. These third
parties, with potentially weaker cybersecurity or unpatched vulnerabilities,
become a significant risk, especially for public industries.

The recent surge in supply chain attacks and the high-profile breaches
they've caused illustrate the significant return on investment for
cybercriminals. Organizations must prioritize securing their supply chains to
prevent this domino effect from crippling their cybersecurity posture.

Trustwave SpiderLabs Insights
Supply chain attacks are particularly relevant for the public sector with
complex supply chains, such as infrastructure providers, third-party
software, and many contractors. Here are some notable examples of supply
chain, third-party attacks, and root causes, augmented by SpiderLabs
original research:

THE PUBLIC SECTOR AND THIRD-PARTY IT SERVICES

Based on a review of breaches in the public sector, Trustwave SpiderLabs
observed that a large portion of supplier or vendor-related breaches
stemmed from third-party IT services, such as those provided by Cloud
Providers, Internet Service Providers (ISP) and IT Shared Services. These
third parties, in most cases, provide direct infrastructure and computing
services and breaches often lead to extensive compromises due to the level
of integration of these to the public sector organization that they cater to.
Here are some notable examples that highlight this threat:

GLOBAL AFFAIRS CANADA AND SHARED SERVICES CANADA
(DECEMBER 2023)

The organization was breached through a compromised VPN system
managed by Shared Services Canada. Shared Services Canada is a federal
department created in 2011 to take over the delivery of email, data centers,
and network services for many government departments and agencies. The
breach affected various internal drives, emails, calendars, and contacts,
disrupting remote work and external communications.

CAMBODIAN GOVERNMENT AND FAKE CLOUD SERVICES (NOVEMBER 2023)

Various Cambodian government organizations were reportedly targeted by
Chinese government hacking groups. This is believed to be part of a long-
term cyber-espionage effort by Chinese hacking groups. Though not directly
related to a third-party service breach, the threat actor leveraged domains
masquerading as cloud backup services to evade detection as this added a
sense of legitimacy to the unusual traffic coming from these organizations.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesExpansion/ PivotingMalwareExfiltration /Post CompromiseInitial Payload46

SWISS GOVERNMENT AND IT SERVICE PROVIDER (JUNE 2023)

The IT Service provider Xplain, responsible for handling classified data for
the Swiss government, was hit by the Play ransomware group. Over 65,000
sensitive documents with personal data, technical information, classified
data, and passwords were leaked.

SRI LANKAN GOVERNMENT AND SHARED CLOUD SERVICES (AUGUST 2023)

A ransomware attack encrypted files and resulted in the loss of data of
nearly 5,000 email accounts on the Lanka Government Cloud (LGC). The LGC
serves 160+ tenants and more than 200+ government organizations. Though
the LGC is technically not a third party as it is managed by the Sri Lankan
government, but this highlights the potential risks of shared IT providers
affecting multiple organizations.

FOREIGN EMBASSIES IN BELARUS AND ISPS (AUGUST 2023)

A threat group called "MoustachedBouncer" targeted foreign embassies
in Belarus at the ISP level. According to third-party researchers, the group
is said to have engaged in intercepting and redirecting network traffic
to compromise data through “adversary-in-the-middle” (AitM) attacks.
According to researchers, the threat actors are likely exploiting local ISPs to
steal data.

PUBLIC SECTOR AND THIRD-PARTY SOFTWARE

The most well-known supplier-related breaches are related to third-party
software. Some of the biggest supply chain attack headlines like SolarWinds,
Kaseya, MOVEit, and 3CX have highlighted the broad impact of these attacks
not only in the public sector, but in all industries.

VARIOUS PUBLIC SECTOR ORGANIZATIONS AND SOLARWINDS (2020)

One of the most prominent examples of a supply chain attack is the
SolarWinds breach that affected multiple organizations. SolarWinds is a
network monitoring software used by many organizations globally, including
various parts of the United States federal government. It has been reported
that attacks leveraging vulnerabilities in this software were leveraged by a
group supported by the Russian government and is considered by some as one
of the worst cyber-espionage incidents suffered by the US The attack affected
at least 200 organizations globally within days of its discovery including many
governments, private companies, and international organizations like NATO
and the European Parliament. Please refer to Trustwave SpiderLabs original
research including SolarWinds vulnerabilities discovered by Trustwave.

NORWAY GOVERNMENT MINISTRIES AND IVANTI (JULY 2023)

Threat actors exploited a zero-day vulnerability in software utilized by
numerous Norwegian ministries resulting in in disruptions to business
systems and email services. The Norwegian National Security Authority
(NSM) verified that the vulnerable software was Ivanti’s Endpoint Manager
Mobile (EPMM), used by 12 of its ministries.

PAKISTANI GOVERNMENT AND E-OFFICE APP (JULY 2023)

Threat actors modified a Microsoft installer built by a Pakistani government
entity for their “E-Office” App to inject a malicious payload. Though the
attack cannot be attributed to a specific group, Chinese threat groups may

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies47

be involved due to the involvement of the Shadowpad malware.

PUBLIC SECTOR AND CONTRACTORS

Though the most recent impactful third-party breaches were related to
third-party software like SolarWinds, so far, the highest number of third-party
related breaches we observed stemmed from government contractors. In
fact, arguably, many consider that the biggest intelligence leak in US history
stems from a contractor, Edward Snowden of Booz Allen Hamilton. Below are
some more recent, though less well-known, examples of contractor-based
breaches of public sector organizations.

CANADIAN GOVERNMENT AND MOVING SERVICES CONTRACTORS
(OCTOBER 2023)

A data breach was identified involving two Canadian government
contractors: Brookfield Global Relocation Services and SIRVA Worldwide
Relocation & Moving Services. This breach exposed the data of Canadian
law enforcement, armed forces, and government employees. The LockBit
ransomware gang leaked archives of over 1.5TB of stolen documents.

US-SOUTH KOREAN MILITARY EXERCISE AND CONTRACTORS
(AUGUST 2023)

It was reported that a spear-phishing attack by North Korean group Kimsuky
targeting unnamed South Korean contractors. The attack focused on stealing
sensitive military information though South Korean authorities claim that no
classified information was exfiltrated.

AUSTRALIAN GOVERNMENT AGENCIES AND LAW FIRM (APRIL 2023)

A cyberattack on law firm HWL Ebsworth affected 65 Australian government
departments and agencies. The ransomware group ALPHV/BlackCat claimed
to have stolen over 2.5 million documents and 3.6TB worth of data from the
law firm.

RUSSIAN MILITARY AND MISSILE DEVELOPER (MAY 2022)

The North Korean state-backed hackers “ScarCruft” and Lazarus attacked
Mashinostroyeniya (Mash), a key missile technology supplier of the Russian
military. The attack involved breaches of email servers and installation of
backdoors with the intent of espionage to gain insights into Russian missile
technology.

CHINESE GOVERNMENT AND CYBERSECURITY COMPANY (AUGUST 2023)

I-Soon, a private contractor that many believe helps the Chinese government
conduct its intelligence-gathering, hacking, and other surveillance activities,
was believed to be attacked by unknown threat actors. Around 190
megabytes of data were leaked, revealing contracts and communications
with the Chinese government including targets within at least 20 foreign
governments and territories, including India, Hong Kong, Thailand, South
Korea, the United Kingdom, Taiwan, and Malaysia.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies48

Mitigations to Reduce Risk

 ▪ Conduct a comprehensive security assessment before any form of
engagement is initiated with a third party. These should include IT
service providers, IT infrastructure providers, third party software
and IT and non-IT contractors.

 ▪ Ensure that third-party vendor contracts have strict cybersecurity
clauses. This could include mandating the conducting of regular
security audits, any notification of any breach should be done
immediately to the organization after it happens, as well as ensuring
compliance with the pertinent regulations of data protections.

 ▪ Conduct audits and review the security practice of third-party

vendors. This involves a periodic review of the service provider,
vulnerability assessments, and penetration testing to identify and
remediate any weak points posed in the security areas.

 ▪ Enforce strict access controls, change control, audit trails, and

security checks to detect and prevent unauthorized modifications in
IT systems and applications.

 ▪ Encrypt all the sensitive data both in transit and at rest. Restrict
the access of sensitive data to the principle of least privilege.
Carry out regular monitoring of the access logs so that activities of
unauthorized or suspicious nature may be detected.

 ▪ Ensure following of the industry standards and regulations like

GDPR, HIPAA, FERPA, etc., for compliance to geographical location
and nature of data handled by third-party vendors.

 ▪ Regular training sessions on phishing, social engineering tactics,

data protection and general cybersecurity hygiene can help
employees act as the first line of defense against supply chain
attacks.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies49

Initial Payload

The Threat
Gaining a foothold is just the first step. Attackers rarely expect to take over
the entire network right away. They often land on a low-level system with
restricted access. From there, they need to upgrade their tools to expand
their reach.

Initial Payload

Command Line

This might involve downloading more powerful malware. But attackers can
also be resourceful. They can use legitimate tools already on the system, like
PowerShell or common utilities (Living-off-the-Land Binaries or LOLBins), to
achieve their goals.

Malware

Trustwave SpiderLabs Insights
Execution techniques of initial payloads observed through active monitoring
mostly involved the use of command and scripting interpreters and user
execution. Command and scripting interpreters like Powershell can be used
to execute commands and scripts on compromised systems, as well as to
download and run malicious payloads. Powershell stands out for its ubiquity
in Windows environments.

Powershell offers attackers a powerful tool to execute commands and
scripts that facilitate the downloading and execution of malicious payloads.
Powershell is deeply embedded within the operating system and allows for
sophisticated operations to be carried out with minimal external footprint
which tends to complicate detection efforts. Figure 37 showcases real-world
cases concerning public organizations that highlight the various methods
that initial payloads are downloaded and executed.

65%

35%

0%

20%

40%

60%

80%

100%

Command and Scripting Interpreter

User Execution

Figure 37: Execution techniques used by threat actors

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesInitial FootholdExpansion/ PivotingMalwareExfiltration /Post CompromiseHTML Attachment50

In a particularly interesting case, Trustwave SpiderLabs researchers
investigated a phishing attempt (Fig 38) targeting a government entity that
leveraged a Powershell-based Infostealer.

Figure 38: Phishing email containing Powershell based Infostealer

The email is a fake invoice. The whole text in the message is an image with
a link anchored to it. If the user clicks anywhere on the message body, the
infection chain (Fig 39) starts, which ultimately triggers the Powershell based
malware.

redirects to

contains

Link on the email

ZIP file

URL

URL

downloads
and executes

leads to

PowerShell-based
Infostealer

Link

Figure 39: Infection chain leading to the PowerShell based Infostealer

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies51

The threat actor uses a combination of Powershell and MSHTA (Microsoft
HTML Application) commands to deliver the initial payload. First, a malicious
Powershell command is run through SyncAppvPublishingServer.vbs, a
Windows 10 file used by threat actors as a Powershell host. The Powershell
command then triggers the execution of a MSHTA command, which runs the
HTA payload hosted in a threat actor website. Finally, a Powershell-based initial
payload (Fig 40) is downloaded that exfiltrates data to a telegram account.

Figure 40: Powershell-based Infostealer that exfiltrates data to a Telegram channel

Related to command and scripting interpreters, during threat hunts,
SpiderLabs commonly encounters custom scripts and binaries in client
environments that contain hard-coded passwords or are assigned elevated
privileges. Threat actors exploit this by disguising malicious scripts within
common repositories, effectively hiding their payloads in plain sight.

Another popular technique, and equally concerning method, used by
adversaries to deliver initial payloads simply relies on a user opening a
malicious file to gain execution. Users may be subjected to social engineering
to get them to open a file leading to code execution.

Our researchers have documented many cases of user execution of initial
payloads through phishing attacks. Many interesting examples were
mentioned in previous sections of this report and our researchers have
released research articles that highlighting how threat actors social engineer
users into executing malicious payload. Among such research include recent
articles on geographic targeting, dangers in visually verifying checksums,
obfuscation and polymorphism to evade security software detection, using
artificial intelligence for more authentic lures, and using various phishing kits
such as Tycoon and Greatness to further increase the range and efficiency of
phishing attacks.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies52

Mitigations to Reduce Risk

 ▪ Educate users about the dangers of opening unknown files and
links. Regularly conduct security awareness training to help
identify and avoid phishing attempts and social engineering
tactics.

 ▪ Implement policies to restrict or monitor the execution of scripts

like VBA and Powershell. This can be done using tools like
Windows Group Policy. Microsoft also has what it calls attack
surface reduction (ASR) rules.

 ▪ Use advanced email filtering solutions like Trustwave MailMarshal
to detect and block malicious emails that may contain harmful
attachments or links.

 ▪ Employ comprehensive endpoint protection solutions that include
antivirus, anti-malware, and behavior-based threat detection to
identify and mitigate threats.

 ▪ Conduct regular audits of all applications operating within the

environment.

 ▪ Implement highly granular “allow lists” of applications on specific

hosts to minimize exposure. Prevent malicious actors from
deploying applications that masquerade as known apps to execute
malicious commands.

 ▪ Apply additional privilege restrictions to prevent unprivileged
sources from running different command shells. Additionally,
segregate critical network segments from the rest of the network
to limit exposure of assets.

 ▪ Provide IT and cybersecurity staff with secure, isolated sandbox
environments for the safe examination and testing of suspicious
files.

 ▪ Conduct frequent security audits to identify and remediate

instances of hard-coded passwords and unnecessarily elevated
privileges in scripts and binaries being used in the computing
environment.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesExpansion
/ Pivoting

Malware

Server

53

Expansion / Pivoting

The Threat
Following the initial infiltration, often on a less critical device like a
compromised laptop from a phishing attack or a network appliance such as a
VPN endpoint, the attacker proceeds to aim at more valuable accounts and
systems using the suitable tools they possess. These can include domain
admins, root accounts, active directory systems, and database servers.

Trustwave SpiderLabs Insights
From that initial foothold, often on an employee or contractor’s workstation
(phishing), an internal IP address (remote access like RDP or VPN), or
software implanted from a compromised third party, the goal of the threat
actor is privilege escalation and expansion. This step is often referred to as
“pivoting” or “lateral movement.”

As an initial step, threat actors will typically try to obtain credentials to
facilitate lateral movement. Credential access tends to be easier once initial
access or foothold has been obtained as security tends to fall off internally.
Often this is due to the mentality of “it’s behind a firewall,” so there isn’t a
need to prioritize security controls. We used to refer to this as “crab security,”
a hard shell with a soft interior.

Based on Trustwave active monitoring, credential access techniques (Fig 41)
observed in the attacks against public sector organizations relied mostly on
password brute-force attempts, but also OS credential dumping, and stealing
or forging Kerberos tickets. Additionally, in our threat hunts, our researchers
often find files containing the word “password” saved on endpoint
workstations which often leads to obtaining valid credentials.

98% 1% 1%

0%

20%

40%

60%

80%

100%

T1110 Brute Force

T10003 OS Credential Dumping

T1558 Steal or Forge Kerberos Tickets

Figure 41: Credential access techniques by threat actors

Once an initial foothold has been acquired, threat actors then obtain valid
credentials, by using various lateral movement techniques to gain further
access within the organization. Trustwave researchers observed that
lateral movement relied predominantly on leveraging remote services (Fig
42), particularly SMB/Windows Admin Shares. Threat actors typically use
this technique in conjunction with accounts they were able to harvest to
propagate across the network.

In our threat hunts, common issues we often see in our engagements
that lead to this situation are unmanaged local administrative accounts. If
compromised, these accounts allow threat actors to move laterally across the
network to access sensitive data or systems whether through SMB/Windows
Admin Shares or other means.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesInitial PayloadInitial FootholdMalwareExfiltration /Post CompromiseHTML AttachmentCommand Line54

Our researchers also often see Distributed Component Object Model (DCOM)
applications being used for lateral movement. With the right compromised
account, DCOM MMC20.Application can be used by attackers to pivot to a
remote host without the need to use PSexec, WMI, or other better-known
techniques.

100%

0%

20%

40%

60%

80%

100%

T1021 Remote Services

Figure 42: Lateral movement techniques by threat actors

As threat actors continue to move laterally across the organization, they
tend to increase their privileges as they pilfer various compromised systems
and high-value assets. Based on our active monitoring of public sector
organizations, privilege escalation techniques observed in security incidents
predominantly involved Valid Accounts where attackers use legitimate
credentials to access systems, applications, and data. Our threat hunts
also often indicate that local administrative accounts are not managed well.
In fact, our team often observed local administrative accounts that have
passwords exceeding 12 months, making them a prime target for threat
actors to exploit and gain privileged access.

It is also during this stage when the threat actors will try to establish
persistence in the network so attackers can share access with others on their
team or come back at a future time to continue the attack. Investigations by
Trustwave researchers into incidents in public sector organizations show that
persistence techniques (Fig 43) predominantly utilized Account Manipulation
(e.g., setting never expiring password), Event-Triggered Execution (e.g.,
malicious activities are initiated automatically in response to specific system
or application events), and External Remote Services (e.g., compromised
Accounts used for RDP access).

50%

25%

25%

0%

20%

40%

60%

80%

100%

T1098 Account Manipulation

T1133 External Remote Services

T1546 Event-Triggered Execution

Figure 43: Persistence techniques by threat actors

In our threat hunts, Trustwave researchers have also observed the use of browser
extensions to maintain persistence. This is an important vector to monitor and
audit, as our researchers have seen many cases where browser extensions
are weaponized. Many of these extensions are considered PUPs or PUAs that
serve advertisements, exfiltrate some form of data, or worse, distribute malware.
Browser extensions that use TOR are another way to bypass security controls
and add risk to the organization. For an example of malicious browser extensions,
please refer to Trustwave SpiderLabs' original research about Rilide (Fig 44), a
malicious browser extension for stealing cryptocurrencies.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies55

Trustwave SpiderLabs
conducts 200K hours of
pentesting each year

Figure 44: Malicious browser extension masquerading as a Google Drive browser
extension

Mitigations to Reduce Risk

 ▪ Enforcing strong security measures within the internal network

and not just at the perimeter. This includes segmenting networks,
applying the principle of least privilege, and using MFA for internal
and external access to resources.

 ▪ Monitor unusual connections in SMB/Windows Admin Shares,
DCOM, and other open services using anomaly and behavior-
based detection techniques.

 ▪ Conduct active monitoring and auditing of account usage and

access patterns to detect anomalies. Conduct regular user reviews
of local user accounts, default administrative accounts, and group
memberships to remove unnecessary privileges and outdated
accounts.

 ▪ Conduct regular audits of all applications (including browsers and
browser extensions) in the environment that could potentially be
used as entry and persistence points to the organization.

 ▪ Monitor unusual system and application events and investigate the
creation of new scheduled tasks, account manipulation, and other
indicators that may indicate attempts at persistence.

 ▪ Engage in proactive threat hunting to detect and respond to
advanced threats. Educate employees about the importance
of cybersecurity and the role they play in maintaining the
organization's security posture.

 ▪ Implement robust host-based security controls including detailed

"allow list” of applications on designated hosts to minimize
exposure.

 ▪ Impose additional restrictions on privileges to prevent

unauthorized execution of commands from unprivileged sources.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesMalware

Server

Malware

56

Malware: Loaders, Infostealers
and RATs

The Threat
Not all malware is created equal. Attackers use a specialized arsenal to
achieve their goals.

Some, like loaders/downloaders, act as the initial invaders. They sneak onto
a system and pave the way for more dangerous malware. These newcomers
can be infostealers, designed to steal passwords, contacts, and other
sensitive information. They might even target what users type online through
fake browser plugins.

Even more alarming are remote access trojans (RATs). Imagine a virtual
backdoor for attackers. RATs give them complete control, allowing them to
download files, steal data like infostealers, and even hijack webcams.

Trustwave SpiderLabs Insights
Trustwave SpiderLabs gains insights into malware in our clients’
environments by delivering our managed services, threat hunts, DFIR, and
malware analysis. Trustwave is in a unique position to detect and analyze
distinctive malware threats focusing on specific industries. Through our
various services, our researchers have identified some of the more notable
malware that is particularly active in the public sector.

Based on statistics coming from Trustwave’s MailMarshal Email Security
Solution, our researchers have observed that the top email malware
executable attachments active in the public sector are the following:

AGENT TESLA

Agent Tesla is a RAT written in .NET that first appeared in 2014. It can take
full control of a compromised system, it has a very flexible command and
control channel, and can connect to the C2 via HTTP, HTTPS, Email, or in a
Telegram channel

Agent Tesla is a RAT commonly deployed via phishing emails with archive
or disc image attachments. Agent Tesla can steal a variety of data, making
it popular. It includes a keystroke logger, the ability to access anything on
the clipboard, and can search the hard drive for any other valuable data. It
also has a flexible command and control channel and can connect to the
C2 via HTTP, HTTPS, Email, or a Telegram channel. Trustwave SpiderLabs
encounters Agent Tesla quite often, typically attached to phishing
campaigns.

Trustwave SpiderLabs has conducted extensive research about Agent
Tesla (Fig 45) and has published new original research about the continuing
evolution of this malware.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesInitial FootholdExfiltration /Post CompromiseHTML AttachmentCommand LineMalwareExpansion/ PivotingInitial Payload57

Link on the email

attaches

GZ

contains

directy downloads

AMSI bypass

tar.gz archive

.NET loader

connects

Encoded
Payload

Agent Tesla
infostealer

Proxy Server*
*other variants utilize HTTP proxies

Figure 45: Typical infection chain for Agent Tesla

AMADEY

The Amadey Bot was discovered in 2018 and is a Trojan used for stealing
sensitive information and acting as a loader for other malware. It has been
employed to deploy other malware like GrandCrab ransomware, and in 2022,
Amadey was used by LockBit affiliates to spread ransomware. This malware
can collect sensitive data from web browsers, target crypto wallets, and
terminate wallet processes. Additionally, it can intercept cryptocurrency
transactions by replacing recipient wallet addresses and is able to monitor
the clipboard, replacing copied wallet addresses with the attackers.

Amadey Bot spreads through phishing sites in addition to spam emails.
Our researchers have found Amedey to be part of multiple RAT payloads
wherein Amadey ensures its persistence by creating a shortcut (LNK) file in
the startup folder, directing it to its own executable. It is then used to initiate
retrieval of other RAT payloads

ASYNCRAT

AsyncRAT is a relatively common RAT. This malware emerged around 2016
and has gained traction due to it having a user-friendly interface and being
open source. One reason for its popularity is that it is free and open source.
The RAT is typically deployed via phishing emails and uses a chain of .BAT,
.PS1, and .VBS files to evade detection. It has a lot of common options like:
· View and record the victim's screen · Log all keystrokes · Chat mechanism
with the victim · Disable Windows Defender · Access to upload, download,
and delete files Below illustrates a multiple stage attack we observed
targeting a hospitality client that started with an email and ended the final
payload of AsyncRAT.

In an original Trustwave SpiderLabs article, our researchers highlighted the
involvement of AsyncRAT (Fig 46) as part of the infection chain abusing
OneNote documents.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies58

contains

embeds

Invoice-themed
email spam

Trojanized
OneNote

Batch
Script

creates a copy of PowerShell then
executes it with the batch scrip itself as input

PowerShell

decrypts the loader assembly
in the batch script and
loads it in the memory

decrypts the AsyncRAT assembly
in the resource section, then
loads and executes AsyncRAT
in the memory

.NET loader

AsyncRAT

Figure 46: Infection Chain for AsyncRAT leveraging a trojanized OneNote file

AVEMARIARAT

The Ave Maria malware, also known as Warzone RAT, is a remote access
trojan that was first identified in the closing months of 2018. It was notable
due to its ability to discreetly circumvent Windows User Account Control
(UAC) and is equipped with a suite of intrusive capabilities, such as
keystroke logging and the exfiltration of credentials from browsers and email
applications. Propagation of Ave Maria is typically achieved through phishing
campaigns, leveraging malicious attachments or hyperlinks to gain initial
foothold. Upon activation, the malware adeptly exploits system vulnerabilities
or manipulates user behavior to gain elevated access. Notable for its
elusiveness, Ave Maria has capabilities to evade conventional detection
methodologies and establish a persistent presence within host systems.

FORMBOOK

FormBook is an infostealer that has been operational since mid-2016. Its
primary function is to harvest sensitive information from compromised
systems, with a particular emphasis on extracting data tied to online forms,
passwords, and assorted credentials. Believed to originate in South Korea,
FormBook has been associated with multiple cybercriminal campaigns.
FormBook comprises a range of functionalities including keylogging,
screenshot capture, clipboard data recording, and the pilfering of data
from web-based forms. It is versatile and can target a diverse array of
applications, web browsers, and online services to pilfer sensitive data.

As time has progressed, FormBook has advanced its capabilities to
encompass attributes like obfuscation tactics, anti-analysis measures, and
the encryption of stolen data prior to its transmission. Our team has seen
this malware delivered often through Microsoft documents, with recorded
instances of it being distributed through OneNote attachments.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies59

GULOADER

This loader malware has been around since 2019 and specializes in deploying
Remote Access Trojans (RATs) and infostealers. GuLoader is interesting as
it uses cloud storage for hosting malicious payloads, which complicates
detection. It spreads mainly via phishing emails and leverages encryption
methods for defense evasion. Trustwave researchers have observed
GuLoader in RFQ-themed malicious spam campaigns targeting various
education institutions.

Trustwave Spiderlabs researchers have recently seen GuLoader in the uptick
of HR-themed spam emails.

REDLINE

Redline is a .Net compiled executable capable of examining and collecting
diverse system information like the operating system version, active
processes, and installed software of an infected system. It has the capability
to gather credentials from web browsers, target cryptocurrency wallets,
and acquire login details from various applications, including NordVPN and
FileZilla.

Trustwave SpiderLabs published an analysis of Redline Stealer in conjunction
with an analysis of the Lapsu$ hacker group in 2022.

REMCOS

Remcos is a RAT that surfaced in 2016. It is ostensibly presented as a tool
for legitimate remote management; however, its capabilities are frequently
exploited for malicious activities by threat actors. The malware grants
extensive control over an infected device, enabling unauthorized access to
perform keystroke logging, surveillance through screenshots or webcam
recordings, and the execution of additional malicious payloads.

The dissemination of Remcos typically occurs through sophisticated phishing
campaigns, which may involve malicious email attachments masquerading as
legitimate documents. These documents attached to emails are commonly
used as the initial vector to deliver the malware into a system. Sometimes,
to give an impression of security, threat actors sometimes use document
protection features and technology to hide their malicious code from email
scanners.

Trustwave SpiderLabs researchers have published original research about
the Remcos RAT (Fig 47) and how it leverages password-protected Word
documents with Information Rights Management (IRM) technology.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies60

Figure 47: Trustwave SEG Console displaying the scam email leading to
Remcos RAT malware

SNAKE

In late 2020, Snake Keylogger emerged as an addition to information stealing
malware. The malware was written in the .NET programming language and
exhibits a modular design making it very versatile. Among its core functions
are keylogging, pilfering of stored login credentials, screen captures, and
retrieval of clipboard data, all of which is subsequently sent to the threat
actor.

Distribution of the Snake Keylogger is typically through phishing and
spearphishing campaigns leveraging emails with malicious Microsoft Office
documents or PDF files. The malware concealed within the document
typically acts as a downloader and leverages Powershell scripts to fetch
a copy of Snake Keylogger onto the compromised system, subsequently
initiating its execution.

SPLASHTOP STREAMER

Splash Streamer is a remote access tool. Our team detected this during an
unauthorized access attempt targeting a public sector organization. The
threat actors attempted to exploit a vulnerability in Citrix or “CitrixBleed”
(CVE-2023-4966). The LockBit ransomware group was presumed to
be behind the attack. Our researchers believe that the tool was used in
a potentially preparatory phase towards a more extensive ransomware
deployment.

MASEPIE

MASEPIE is a Python backdoor leveraged by APT28 (a Russia-linked
group) as part of their botnet activities. APT28 has been actively targeting
routers globally since 2022, across various sectors in multiple countries
including government entities. MASEPIE allows for the collection of
credentials, proxying network traffic, and hosting phishing pages. Of note,
APT28 is suspected to have compromised the Hillary Clinton campaign,
the Democratic National Committee, and the Democratic Congressional
Campaign Committee in 2016 to interfere with the US presidential election.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesTRUSTWAVE‧MDR‧ELITE‧
OFFERS AN MTTA OF
15 MINUTES AND MTTR OF
<30‧MINUTES

61

PIKABOT AND WIKILOADER

Pikabot is a relatively new loader malware used often to distribute
ransomware and other malicious payloads like Cobalt Strike. Wikiloader on
the other hand is primarily used to download and install secondary payloads
like banking trojans. Based on our data, our researchers noted that malicious
PDFs targeting public sector organizations often contain URLs that lead to
these two malwares.

Mitigations to Reduce Risk

 ▪ Use host-based anti-malware tools that can assist in identifying and
quarantining specific malware, but understand they have limitations
and are often circumvented by custom malware packages.

 ▪ Enhance email security measures and educate users about the

dangers of malicious email attachments. Increase vigilance against
phishing campaigns and scrutinize email attachments. Implement
robust email filtering and monitoring systems.

 ▪ If preventing infection is not possible, audit controls become crucial
indicators of potential compromise. This involves enabling system
logs on valuable systems and workstations and implementing
network logging through flows, Network Monitoring Solutions, or
IDS devices on ingress and egress channels.

 ▪ Implement active monitoring. Merely enabling logs is insufficient;
if logs are not monitored, they lose their effectiveness. Regular
monitoring helps establish a baseline of regular activity, making
abnormal behavior or traffic more conspicuous. Additionally,
establish and regularly practice a formal incident response process.

 ▪ Perform ongoing Underground and Dark Web monitoring for

information leakage that may have been missed.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesMalware

Server

Malware

62

Malware: Ransomware

The Threat
Ransomware isn't just about locking files anymore. It's evolved into a multi-
pronged attack.

Traditionally, ransomware scrambled data, holding it hostage until you paid
a ransom. Now, attackers try to erase backups and shadow copies, making
recovery even harder.

But that's not all; many ransomware gangs are double-dipping with double
extortion. They steal data before encrypting it, threatening to leak it publicly
unless they get paid. Even if they're not paid, they can still sell the stolen
information.

Things can get even worse with triple extortion. Attackers might launch a
denial-of-service attack (DDoS) to cripple online operations, adding pressure
to pay.The most vicious tactic? Targeting victims of the data breach itself,
threatening to expose their information if the organization doesn't pay.

Trustwave SpiderLabs Insights
Trustwave SpiderLabs researchers reviewed several data sources for
known ransomware attacks on public sector organizations during the last 12
months, including various ransomware tracking projects, online news outlets,
and individual ransomware leak pages. What follows below is based on a
synthesis of those data sources.

Trustwave SpiderLabs researchers show 10 different ransomware groups (Fig
48) active in the public sector, with LockBit, Medusa, and Play being the most
prevalent.

43%

LockBit 3.0

Medusa

Play

BianLian

SnatchTeam

Royal

NoEscape

AlphV

BlackByte

Vice Society

13%

12%

6%

6%

4%

4%

4%

4%

4%

0%

10%

20%

30%

40%

50%

Figure 48: Ransomware groups attacks on public sector

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesInitial FootholdExfiltration /Post CompromiseHTML AttachmentCommand LineMalwareExpansion/ PivotingInitial Payload63

Based on our data, more than half of the organizations targeted by
ransomware groups were in the US (Fig 49) followed by Spain, Canada, and
France.

74%

US

Spain

Canada

France

Brazil

Trinidad & Tobago

Belgium

Norway

New Zealand

Philippines

4%

4%

4%

3%

3%

2%

2%

2%

2%

0%

10%

20%

30%

40%

50%

60%

70%

80%

Figure 49: Public sector organizations affected by country

Analysis of the data shows that more than half of the ransomware attacks
targeted local governments, (Fig 50) followed by transit infrastructure, and
central / federal government.

Local Government

60%

Transit Infrastructure

12%

Central Government

8%

Regional Government

Public Utilities

Emergency Services

Public Health

Judicial

Armed Forces

Correction Institutions

4%

4%

4%

2%

2%

2%

2%

0%

10%

20%

30%

40%

50%

60%

70%

Figure 50: Ransomware attacks by public sector type

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies64

Notable ransomware incidents in public sector organizations within the past
year include:

CANADIAN GOVERNMENT CONTRACTORS (OCTOBER 2023)

The LockBit ransomware gang claimed responsibility for attacks targeting
Canadian government contractors Brookfield Global Relocation Services
(BGRS) and SIRVA Worldwide Relocation & Moving Services. The group
claimed to have leaked 1.5TB of stolen documents (Fig 51). LockBit publicly
disclosed negotiations with alleged representatives from SIRVA.

Figure 51: Lockbit 3.0 claims SIRVA breach

It should be noted that just recently in Feb 2024, LockBit was targeted by
an international law enforcement operation led by Britain's National Crime
Agency (NCA), the US Federal Bureau of Investigation (FBI), Europol, and
other global police agencies. The operation, named "Operation Cronos," has
taken control of LockBit's extortion website. Despite the disruption, LockBit
claimed to have backup servers unaffected by the law enforcement action.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies65

BRITISH LIBRARY (OCTOBER 2023)

Rhysida, operating as a Ransomware-as-a-Service (RaaS) claimed an attack
(Fig 52) on the British Library where it disrupted IT systems and services.
Services affected included digital collections access, online services in
reading rooms, inter-library loan services, and the Eccles Centre Visiting
Fellowship program. The British Library On-Demand service was also
suspended and there were problems for authors under the Payment Lending
Rights scheme. A lessons learned document was released by the British
Library exploring the attack.

Figure 52: Rhysida claims British Library breach

KUWAIT’S MINISTRY OF FINANCE (SEPTEMBER 2023)

The Rhysida ransomware gang claimed responsibility (Fig 53) for an attack
against the Kuwait Ministry of Finance. In response to the attack, the Ministry
of Finance systems were isolated from other government systems to prevent
the spread of ransomware. Though concerns were raised about potential
disruptions to payment and payroll systems, the Kuwaiti government said
these systems were unaffected due to it being hosted on a separate network.

Figure 53: Rhysida claims Ministry of Finance (Kuwait) breach

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies66

SRI LANKAN GOVERNMENT (AUGUST 2023)

This event was also mentioned in the Supply Chain Attack section of this
report. The attack on the Lanka Government Cloud (LGC) encrypted data
from nearly 5,000 government email accounts. Though operations were
restored within 12 hours, data from a specific period was irretrievably lost.

Figure 54: Sri Lanka CERT advisory on ransomware attack

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies67

NATIONAL HEALTH SERVICE (NHS) UK (MAY 2023)

The ALPHV ransomware gang claimed to have stolen 70 terabytes of
sensitive data from the Barts Health NHS Trust. The data stolen included
employee identification documents and internal emails marked "confidential."
The NHS Trust acknowledged the incident and provided updates on the
impact and measures being taken.

Figure 55: ALPHV claims Barts Health NHS Trust breach

ROYAL MAIL (JANUARY 2023)

An affiliate of the LockBit ransomware group claimed an attack on Royal Mail,
which led to severe disruptions in international parcel and letter services.
This event caused a significant revenue decline and incurred additional
operational costs due to the attack.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies68

Figure 56: LockBit 3.0 claims Royal Mail breach

As seen in these examples, ransomware threat actors have targeted a wide
range of public sector organizations in many countries, from governments
to post offices to libraries. These attacks have caused significant
operational disruptions and privacy issues due to the double extortion
tactics of these gangs.

These threat groups have become proficient in exploiting technical
vulnerabilities and supplier issues, leading to the increased prevalence
of successful attacks in this sector. It should be noted though, that the
successful law enforcement operation against LockBit, arguably the most
prolific ransomware group, is an important milestone, but only time will tell
whether it has a significant impact on the overall threat landscape.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies69

Mitigations to Reduce Risk

 ▪ Use host-based anti-malware tools to assist in identifying and

quarantining ransomware, but understand they have limitations and
are often circumvented by custom malware packages.

 ▪ Enhance email security controls to protect against ransomware
distributed via email. Educate users on the risks of malicious
email attachments and phishing attempts. Enhance vigilance and
implement email filtering and monitoring systems.

 ▪ Establish and regularly practice a formal incident response process.
Ensure backups are available as a contingency to recover from a
worst-case scenario.

 ▪ Enable system logs on critical systems and workstations and

implement network logging through flows, Network Monitoring
Solutions, or IDS devices on ingress and egress channels.

 ▪ Implement active monitoring. Merely enabling logs is insufficient;
if logs are not monitored, they lose their effectiveness. Regular
monitoring helps establish a baseline of regular activity, making
abnormal behavior or traffic more conspicuous.

 ▪ Perform ongoing Underground and Dark Web monitoring for

information leakage that may have been missed.

 ▪ Ensure enforcement of least privilege; data cannot be encrypted if

the exploited user does not have access to it.

 ▪ Instill multiple levels of security, or defense in depth, including

different anti-malware scanners from multiple providers at different
layers.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies70

Exfiltration / Post Compromise/
Impact

The Threat
Once attackers have established themselves within a network and systems,
they will proceed to execute their final plan depending on their motives.

Some are like digital smash-and-grab robbers. They snatch as much data
as possible (passwords, financial info) and disappear quickly, often trying to
erase their tracks.

Others are after specific targets - a particular database, a high-profile
employee's files, or a critical system. They'll move carefully, trying to stay
hidden until they get what they came for.

Then there are the destruction crews. These attackers don't care about
stealing; they just want to cause chaos. They might unleash ransomware,
locking up data, or go on a deleting spree, wiping out files and backups alike.

Server

Exfiltration /
Post Compromise

Malware

Trustwave SpiderLabs Insights

Attacks against the public sector can be devastating to the organization
targeted and the general population they serve. In this section, Trustwave
SpiderLabs researchers explored the impact of various attacks against
various public sector organizations particularly their effect on the
government, law enforcement, public safety, and national security.

GOVERNMENT DATA LEAKS

Governments have wide-ranging functions and could encompass a variety of
areas, from legislative, housing, finance, and healthcare, among others. Data
leaks against government departments or ministries can have a profound
impact on the general population. Often, governments are stewards of their
citizen's data, and if the government is not able to protect their sensitive
data, it could significantly undermine the public trust in the government's
security and competency in general.

In a recent example, there was a data leak incident involving the US
Environmental Protection Agency (EPA) where a threat actor (alias USDoD)
claimed to have leaked a contact database with over 15 million records of
8.5 million individuals. The breach included personal and business contact
information such as names, job titles, phone numbers, email addresses, and
mailing addresses.

Figure 57: EPA data leak posted in an underground forum

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesInitial FootholdHTML AttachmentCommand LineMalwareExpansion/ PivotingInitial PayloadMalware71

The threat actor (USDoD) has been involved in other high-profile attacks,
such as INFRAGARD, Airbus, Deloitte, NATO, CEPOL (European Union Agency
for Law Enforcement Training), Europol, and Interpol.

Our researchers have also seen other government agencies having similar
issues including the National Oceanic and Atmospheric Administration
(NOAA) (Fig 58) and local government departments like the Department
of Planning and Natural Resources of the US Virgin Islands (Fig 59).
Both agencies appear to have sizeable breaches with data being sold in
underground forums and marketplaces.

Figure 58: Threat actor offering the database of the National Oceanic and
Atmospheric Administration (NOAA) USA

Figure 59: Threat actor offering data of property owners, tenants, and DPNR workers
collected from Department of Planning and Natural Resources of the US Virgin Islands

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies72

While many of the examples highlighted are from the US, data breaches are
a worldwide issue. In the examples below, our researchers identified a threat
actor offering data from Malaysian citizens (Fig 60) and a data leak from the
Philippine government's PhilHealth system (Fig 61).

Figure 60: Threat actor claiming to have hacked into Malaysia government database
and offering citizen’s data

Figure 61: Threat actor claiming to have hacked into Malaysia government database
and offering citizen’s data

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies73

Figure 62: Threat actor posting Philippine PhilHeath system data in Telegram

Aside from individual countries, our researchers have also seen many threat
actors, such as those behind the RomCom RAT targeting international
organizations such as NATO particularly when it involves Ukraine.

UNDERMINING THE ELECTORAL PROCESS

An interesting area in the public sector that can have a profound effect
is the impact of breaches and attacks on the electoral process. During
our research, we observed multiple election-related posts and offers in
underground marketplaces. Attacks focusing on election-related resources
not only expose citizen data (e.g. 2016 Philippine Commission on Election
Breach), but also confidential communications and campaign strategies of
political parties (e.g. 2016 National Democratic Convention Hack).

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies74

In the examples below, our researchers identified various threat actors selling
election-related information from various countries. Some of the posts were
related to local electoral audits (Fig 63), others are related to municipal
electoral registries (Fig 64), while others appear to be national election
campaign information (Fig 65). In a previous section (Initial Access), we
also highlighted some underground marketplace posts from Access Brokers
offering access to election-related IT infrastructure.

Figure 63: Threat actor offering election audit related information from
Cuyahoga County

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies75

Figure 64: Threat actor offering Argentinian Municipal Electoral Registry from 2023

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies76

Figure 65: Threat actor offering leaked data from Israeli Election Campaign
Management System

LAW ENFORCEMENT AND PUBLIC SAFETY

One of the more prolific offerings in underground forums and marketplaces
are related to law enforcement and judiciary. This type of information
sale affects privacy and, in certain cases, could affect public safety. Law
enforcement and judiciary departments are highly targeted due to the
sensitive data that they store. Gaining access to law enforcement databases
or court records could lead to manipulation of deletion of critical information
used in criminal investigations and judicial proceedings.

The example below illustrates the potential critical impact of an attack on law
enforcement assets. The threat actor Phoenix Group, affiliated with KillNet,
infiltrated Pakistani law enforcement servers and reportedly took control of
various services.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies77

The threat group substantiated their claims by showing actual alterations in
the police profile, creating fictitious information under the name “KillMilk” (Fig
66), allegedly with a murder charge and execution petition for stealing milk
(Fig 67).

Figure 66: Forwarded Phoenix post showing a KPK Police Human Resource policeman
profile where part of data was replaced with “KillMilk” data

Figure 67: Phoenix cyber group Telegram channel showing changes in the Pakistani
law enforcement database showing a murder charge for ”KillMilk”

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies78

Additionally, there are also numerous examples in underground forums
and marketplaces selling citizen data taken from either police or judicial
databases. In the examples below, we see a database being sold containing
data from 960 million Chinese citizens purportedly from the Shanghai
National Police (SHGA) (Fig 68).

Figure 68: Threat actor offering data for 960M Chinese citizens from a police
database

In another example, we see what appears to be a data leak stemming from a
compromised judicial agent account in Argentina (Fig 69). This is particularly
notable as it shows that access to just one account, whether obtained
through phishing or social engineering, can significantly impact an entire
organization.

Figure 69: Data leak purportedly stemming from a compromised internal agent in
Argentina

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies79

Aside from citizen data, police data was also spotted for sale on underground
forums and marketplaces. In the example below, the threat actor is offering
the personal data of 325 Peruvian police officers (Fig 70). Aside from the
obvious privacy concerns, this is a potential safety issue  for the police
officers.

Figure 70: Threat actor offering personal data of 325 Peruvian police officers

Our researchers found another post where a threat actor was selling a
database of private and commercial vehicle license numbers belonging to
the Israeli government (Fig 71). Access to government vehicle data could
potentially jeopardize the safety of government officials, facilitate targeted
attacks, or espionage efforts.

Figure 71: Threat actor offering database of private and commercial license numbers
belonging to the Israeli state

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies80

Our researchers also found threat actors selling emails for various police
department email accounts. The example below shows over 65 gigabytes
of emails from the Italian National Police (Fig 72). This can be particularly
dangerous as these might contain sensitive information about procedures,
criminal investigations, informants, officer data, and other confidential
information.

Figure 72: Threat actor offers data collected from Italian National Police email
accounts

Threat actors have increasingly been targeting law enforcement and a review
of underground marketplaces highlights this as our researchers observed
multiple requests for buying police documents and sensitive materials (Fig
73). We can only speculate on the motivations of the threat actors, but these
could include exploiting the information for financial gain, evading detection
or legal prosecution, and undermining law enforcement efforts.

Figure 73: Threat actor looking to buy police reports templates of police departments
of various countries

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies81

NATIONAL SECURITY AND CYBERWARFARE

Trustwave SpiderLabs has researched developments in cyberwarfare and
its impact on national security. Our researchers have conducted original
research on the tactics and techniques utilized by various cyber groups in
the Israeli-Hamas conflict. We have also conducted in-depth analysis and
released multiple articles on the Russia-Ukraine Cyberwar. This research
highlights how various cyber groups leverage existing techniques and
pivot them to conduct attacks that can affect defense capabilities, military
operations, and jeopardize homeland security.

Aside from the Israeli-Hamas and Russia-Ukraine conflict, our researchers
have seen multiple posts in underground forums and marketplaces that
could potentially affect the national security of the countries involved. In
the example below, a threat actor claims to have documents on the US
Department of Foreign Affairs Humphrey Plan, which contains information
about US espionage.

Figure 74: Threat actor claiming access to documents about US espionage plans

In another underground forum post, our researchers identified threat actors
selling US Immigration and Customs Enforcement (ICE) and US Citizenship
and Immigration Services (USCIS) databases (Fig 75). This type of data can
be very important for homeland security as it can be leveraged by threat
actors to gain unauthorized entry through identity theft or potentially identify
targets of investigations.

Figure 75: Threat actor offering a database belonging to ICE and USCIS

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies82

Aside from the examples provided above, there are also many more examples
of “covert” espionage types of attacks against government and military
organizations. Groups (or groups behind certain tools) like HiatusRAT, Volt
Typhoon, and Charming Kitten have been in the news recently for activities
targeting political dissidents and even military installations and infrastructure.

Finally, Trustwave SpiderLabs researchers have seen hacktivist activities
related to Distributed Denial of Service (DDoS) targeting government
websites as a form of political statements. Many threat groups like
Anonymous Sudan and NoName057(16) are very active in this area.

NoName057(16) has reportedly been targeting NATO and Czech presidential
election candidates’ websites as mentioned in a previous Trustwave
SpiderLabs report. Meanwhile, Anonymous Sudan has been targeting
Swedish, Dutch, Australian, and German organizations purportedly in
retaliation for anti-Muslim activity. In-depth research on activities and
identities of Anonymous Sudan is available through Trustwave SpiderLabs
original research.

Other threat groups such as Ali’s Justice (Edalat-e Ali) and Xiaoqiying
(Genesis Day or Teng Snake) have also been seen recently focusing on
hacktivism type of activities such as disruption and defacements. In fact, Ali’s
Justice went to the extent of hacking live Iranian TV (Fig 76) to deliver their
political message.

Figure 76: Journalist confirming that attack of the live TV and radio broadcast

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies100%

OF TRUSTWAVE'S
ADVANCED CONTINUAL
THREAT HUNTS RESULT
IN THREAT FINDINGS

83

Mitigations to Reduce Risk

 ▪ Databases that store sensitive data should be a priority for

robust security controls. Database security tools like Trustwave’s
DbProtect can flag misconfiguration and user rights can also help
reduce risk.

 ▪ Ensure that the appropriate level of protection is applied based on
the criticality of information. Ensure that data protection controls
such as data encryption are implemented in assets that need to be
protected.

 ▪ Ensure appropriate segmentation, segregation, and apply Zero
Trust principles. Review if the database needs to be accessible
to the whole network, or if it can be hidden behind certain
applications.

 ▪ Ensure that up-to-date backups are available as a contingency to

recover from a worst-case scenario.

 ▪ Use advanced email filtering solutions like Trustwave MailMarshal
to detect and block malicious emails that may contain harmful
attachments or links.

 ▪ Employ comprehensive endpoint protection solutions that include
antivirus, anti-malware, and behavior-based threat detection to
identify and mitigate threats.

 ▪ Monitor the Dark Web regularly for potential compromises and

have a robust incident response process to contain and manage
incidents.

 ▪ Conduct regular penetration tests to proactively identify

vulnerabilities and weaknesses in your systems, networks, and
applications.

 ▪ Run continuous threat hunting, like Trustwave’s Advanced

Continual Threat Hunt through your environments for undetected
compromises.

 ▪ Formalize and regularly test your incident response policy for
the scenarios that will most likely impact you. Train staff on
ransomware recognition to decrease time of response and
remediation.

 ▪ Understand your business. Recognize your risk and prepare for

the impact of politically motivated cyberattacks, particularly those
targeting infrastructure and service disruptions.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesKey Takeaways and
Recommendations

85

All organizations face cyber threats, but for governments the stakes are even higher.

Public sector organizations are tempting targets for attackers motivated by both cash and a
desire to disrupt critical services. These attackers are constantly innovating, forcing governments
to stay ahead of the curve. The public sector has some unique challenges due to the nature of the
industry, including:

 ▪ Data Sensitivity:  Often, valuable data is centralized within public sector systems, which

makes them highly sought after targets for cyberattacks. The majority, if not all, public sector
organizations handle sensitive information, including personal details of their citizens and
residents. Additionally, data handled by the public sector is essential for the provisioning of
critical public services which makes any security breach potentially devastating in terms of
national security and public safety.

 ▪ Diverse Organizations and Environments:  There are a wide range of public sector

organizations, ranging from small townships to large international organizations spanning
multiple countries. Each of these organizations could be managing a diverse range of digital
infrastructures across multiple locations with multiple potential exposures. There could also
be a diverse level of technological maturity across these organizations, with some public
systems combining outdated and modern technologies, creating gaps, and complicating the
implementation of security controls.

 ▪ Public Accountability:  The public sector caters to a broad range of stakeholders such as the
public, other government entities, non-governmental organizations, and third-party vendors
and contractors. This broad range could increase vectors and exposures to cyberattacks.
Additionally, public entities are subject to high transparency, accountability, and compliance
requirements, which could require higher technological adoption but, in some cases, without
the commensurate adoption of cybersecurity strategies and controls.

 ▪ Resource Limitations:  Though not in all cases, many public sector organizations frequently

face budgetary constraints which could restrict their ability to implement up-to-date
cybersecurity strategies and technologies. Moreover, budgetary constraints coupled with lack
of manpower due to competition with the private sector, which in many cases can provide
higher compensation, contribute to the challenges that this sector faces in cybersecurity.

As demonstrated in our attack cycle, threat actors often employ multiple vectors to persistently
target public sector organizations. While the technical aspects of these attacks may change over
time, the underlying tactics tend to remain consistent. Some of the key points to consider in the
public sector are as follows:

 ▪ Phishing‧and‧Social‧Engineering‧Threat‧Vectors:‧‧Phishing and social engineering are the
most exploited methods for gaining initial access in the public sector. These attacks are
double edged. Aside from just targeting the organizations themselves, threat actors also target
the public by impersonating the services that the public sector provides. Practical security
awareness training programs are vital to ensure staff are cognizant of the risks of phishing and
social engineering.

 ▪ Malicious Email Attachments:  The public sector frequently encounters malware through

email attachments. Our team has observed a diverse variety of RATs, Information Stealers, and
Loaders that are becoming increasingly sophisticated with advanced evasion capabilities. A
good email security gateway and host-based malware controls should always be part of the
first line of controls implemented in the organization.

 ▪ Vulnerability‧Exploitation:‧‧Apart from phishing, threat actors continue to exploit vulnerabilities
in public-facing applications. Attackers continue to rely on vulnerabilities in publicly exposed
services, including, but not limited to, Log4J and MOVEIt. A robust vulnerability and patch
management program should be in place to ensure that vulnerabilities are addressed on time.

 ▪ Exposure of Publicly Accessible Systems and Services:  There is significant exposure of

public sector assets, including potentially sensitive systems such as databases, surveillance

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies86

systems, developer tools, and email servers. Organizations must have an asset discovery
and management process to ensure that assets that can become potential attack vectors are
identified and protected.

 ▪ Malware and Ransomware Attacks:  Ransomware, as with other sectors, is a significant threat
to the public sector. Our researchers have tracked attacks from numerous ransomware groups
with the most active being LockBit, Medusa, and Play. Aside from various malware security
controls, organizations should have a robust disaster recovery and business continuity plan to
ensure that they can recover from attacks with the least impact.

 ▪ Access and Data Brokers and the Dark Web:  There is a proliferation of posts and offers of

public sector assets on the Dark Web. Some of the access and data being sold appear to be
very sensitive and includes citizen information, law enforcement data, election data, and many
more that could have national security and public safety repercussions. Organizations should
consider adopting a threat intelligence capability to look for potential threats and breaches
across various data sources such as the Dark Web and underground forums.

 ▪ Third-Party Supplier Risk:  There were many examples of public sector organizations that

have been compromised through third-party software, third-party IT service providers, and
government contractors. Insider threats stemming from contractors is also a notable risk in this
area. A third-party vendor and supplier review and due diligence process should be in place to
ensure third parties have the appropriate level of security controls to protect the assets and
data of the public sector organization.

 ▪ Hacktivism and DDoS Attacks:  Public sector organizations are particularly exposed to

hacktivism, DDoS, and disruption attacks due to political motivations of various threat groups.
Such groups often target government websites and infrastructure to protest policies, expose
alleged misconduct, or influence public opinion. DDoS and WAF-based protection should be in
place to protect externally facing assets.

 ▪ Advanced‧Persistent‧Threats‧(APTs):‧‧The public sector is often targeted by APTs which use
sophisticated techniques to infiltrate and remain undetected within networks for extended
periods. These are often attributed to nation-state threat actors with the purpose of
information gathering and espionage. Organizations should consider implementing a regular
threat hunting program to ensure prompt discovery and removal of potential threats.

Preventative measures remain the most effective defense against all types of cyberattacks. By
focusing on preventative measures, we can stop attackers in their tracks before they can gain a
foothold and wreak havoc.

As shared throughout this report, the table below offers a comprehensive list of actionable steps
to fortify your defenses against various cyber threats.

Initial Foothold

ACTIONABLE MITIGATION RECOMMENDATIONS:

 ❏ Implement robust anti-spoofing measures, including deploying technologies on email

gateways. Deploy layered email scanning with a solution like Trustwave MailMarshal to
provide better detection and protection.

 ❏ Perform routine security audits of IT applications and infrastructure to identify and

rectify vulnerabilities that could be exploited in phishing campaigns.

 ❏ Ensure that proper security controls are in place around account management. This
includes enforcing strong password policies like enabling multi-factor authentication
(MFA) for all users. Additionally, perform regular user access reviews to identify any
unauthorized access.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies87

 ❏ Educate system users and implement a training program to educate users about the
risks of phishing, spam, and scams. Utilize simulated phishing exercises to test user
security awareness and phishing readiness.

 ❏ Regularly monitor external access points and review logs for unusual activities. Public

sector organizations should also conduct periodic audits of their network infrastructure
to identify and address vulnerabilities.

 ❏ Regularly monitor Dark Web sites and underground marketplaces for possible

breaches. Put procedures in place to respond to possible breaches such as changing
affected credentials and investigating the scope of the breach.

 ❏ Restrict access to assets and sensitive data based on the principle of least privilege.

Ensure that users only have access necessary to perform their job functions.
 ❏ Enforce proper password hygiene and ensure that systems follow a consistent

password complexity requirement / standard across the organization. Additionally,
securely store credentials in password managers or leverage vaults to prevent
credential abuse.

 ❏ Utilize vulnerability assessments and penetration testing to identify vulnerable servers.
Regularly update and patch systems to protect against known vulnerabilities. Promptly
patch critical vulnerable systems.

 ❏ Databases that store sensitive data should be a priority for system and software

patching. Database auditing tools like Trustwave’s DbProtect that can flag
misconfiguration and user rights can also help eliminate risk.

 ❏ Implement strict access controls for critical systems, including databases, file

servers, network devices, and email systems. Strengthen access controls to minimum
necessary levels for authorized users.

 ❏ Conduct a comprehensive security assessment before any form of engagement
is initiated with a third party. Ensure that third-party vendor contracts have strict
cybersecurity clauses. This could include mandating the conducting of regular security
audits, any notification of any breach should be done immediately to the organization
after it happens, as well as ensuring compliance with the pertinent regulations of data
protections.

 ❏ Enforce strict access controls, change control, audit trails, and security checks to

detect and prevent unauthorized modifications.

 ❏ Conduct regular dynamic and static security testing of in-house and third-party

software products and applications.

 ❏ Encrypt all the sensitive data both in transit and at rest. Restrict the access of sensitive
data to the principle of least privilege. Carry out regular monitoring of the access logs
so that activities of unauthorized or suspicious nature may be detected.

 ❏ Ensure following of the industry standards and regulations like GDPR, HIPAA, FERPA,

etc., for compliance to geographical location and nature of data handled by third-party
vendors. If you are a third-party, ensure that data privacy compliance requirements are
understood and adhered to.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies88

Initial Payload & Expansion / Pivoting

ACTIONABLE MITIGATION RECOMMENDATIONS:

 ❏ Educate users about the dangers of opening unknown files and links. Regularly conduct

security awareness training to help them identify and avoid phishing attempts and
social engineering tactics.

 ❏ Implement policies to restrict or monitor the execution of scripts like VBA and

Powershell using tools like Windows Group Policy. Microsoft also has attack surface
reduction (ASR) rules.

 ❏ Use advanced email filtering solutions like Trustwave MailMarshal to detect and block

malicious emails that may contain harmful attachments or links.

 ❏ Employ comprehensive endpoint protection solutions that include antivirus, anti-
malware, and behavior-based threat detection to identify and mitigate threats.

 ❏ Conduct regular audits of all applications operating within the environment.
 ❏ Implement highly granular “allow lists” of applications on specific hosts to minimize
exposure. Prevent malicious actors from deploying applications that masquerade as
known apps to execute malicious commands.

 ❏ Apply additional privilege restrictions to prevent unprivileged sources from running

different command shells. Additionally, segregate critical network segments from the
rest of the network to limit exposure of assets.

 ❏ Conduct frequent security audits to identify and remediate instances of hard-coded

passwords and unnecessarily elevated privileges in scripts and binaries being used in
the computing environment.

 ❏ Enforcing strong security measures within the internal network and not just at the

perimeter. This includes segmenting networks, applying the principle of least privilege,
and using multi-factor authentication (MFA) for internal and external access to
resources.

 ❏ Monitor the use of unusual connections in SMB/Windows Admin Shares, DCOM and

other open services using anomaly and behavior-based detection techniques.
 ❏ Conduct active monitoring and auditing of account usage and access patterns to
detect anomalies. Conduct regular user reviews of local user accounts, default
administrative accounts, and group memberships to remove unnecessary privileges
and outdated accounts.

 ❏ Deploy solutions for internal security audits and Penetration Tests to identify and

remediate potential attack paths in Active Directory environments before they can be
exploited by attackers.

 ❏ Monitor vulnerabilities and ensure timely application of security patches and updates to

prevent exploitation of known vulnerabilities.

 ❏ Conduct regular audits of all applications in the environment to combat the adoption of

custom applications that could result in vulnerabilities.

 ❏ Monitor unusual system and application events, and investigate the creation of

new scheduled tasks, account manipulation, and other indicators that may indicate
attempts at persistence.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies89

 ❏ Engage in proactive threat hunting to detect and respond to advanced threats. Educate
employees about the importance of cybersecurity and the role they play in maintaining
the organization's security posture.

 ❏ Implement robust host-based security controls including detailed "allow list” of

applications on designated hosts to minimize exposure.

 ❏ Impose additional restrictions on privileges to prevent unauthorized execution of

commands from unprivileged sources.

Malware

ACTIONABLE MITIGATION RECOMMENDATIONS:

 ❏ Use host-based anti-malware tools that can assist in identifying and quarantining

specific malware, but understand they have limitations and are often circumvented by
custom malware packages.

 ❏ Enhance email security measures and educate users about the dangers of malicious

email attachments. Increase vigilance against phishing campaigns and scrutinize email
attachments. Implement robust email filtering and monitoring systems.

 ❏ If prevention of infection is not possible, audit controls become crucial indicators of
potential compromise. This involves enabling system logs on valuable systems and
workstations and implementing network logging through flows, Network Monitoring
Solutions, or IDS devices on ingress and egress channels.

 ❏ Implement active monitoring. Merely enabling logs is insufficient; if logs are not

monitored, they lose their effectiveness. Regular monitoring helps establish a baseline
of regular activity, making abnormal behavior or traffic more conspicuous. Additionally,
establish and regularly practice a formal Incident Response process.

 ❏ Perform ongoing underground and Dark Web monitoring for leaked information.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies90

Exfiltration / Post Compromise

ACTIONABLE MITIGATION RECOMMENDATIONS:

 ❏ Use host-based anti-malware tools that can assist in identifying and quarantining
ransomware, but understand they have limitations and are often circumvented by
custom malware packages.

 ❏ Enhance email security controls to protect against ransomware distributed via email.
Educate users on the risks of malicious email attachments and phishing attempts.
Enhance vigilance and implement email filtering and monitoring systems.

 ❏ Establish and regularly practice a formal incident response process. Ensure that
backups are available as a contingency to recover from a worst-case scenario.

 ❏ Enable system logs on critical systems and workstations and implementing network
logging through flows, network monitoring solutions, or IDS devices on ingress and
egress channels.

 ❏ Implement active monitoring. Merely enabling logs is insufficient; if logs are not

monitored, they lose their effectiveness. Regular monitoring helps establish a baseline
of regular activity, making abnormal behavior or traffic more conspicuous.

 ❏ Perform ongoing Underground and Dark Web monitoring for information leakage that

may have been missed.

 ❏ Ensure enforcement of least privilege, data cannot be encrypted if the exploited user

does not have access to it.

 ❏ Instill multiple levels of security, or defense in depth, including varying anti-malware

scanners from multiple providers at different layers.

2024 Public Sector Threat Landcape: Trustwave Threat Intelligence Briefing and Mitigation Strategies