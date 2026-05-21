# Ransomware Report 2024

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [Ransomware Landscape: Top Trends and Targets](#ransomware-landscape-top-trends-and-targets)
  - [Overall rise in ransomware attacks](#overall-rise-in-ransomware-attacks)
  - [Industry verticals most impacted by ransomware](#industry-verticals-most-impacted-by-ransomware)
  - [Geographical distribution of victim organizations](#geographical-distribution-of-victim-organizations)
  - [Most active ransomware groups in 2023-2024](#most-active-ransomware-groups-in-2023-2024)
  - [Major vulnerabilities used in ransomware attacks](#major-vulnerabilities-used-in-ransomware-attacks)
- [Ransomware Roundup: What’s Making Headlines](#ransomware-roundup-whats-making-headlines)
  - [The ransomware plague in healthcare](#the-ransomware-plague-in-healthcare)
  - [The impact of the SEC’s cybersecurity ruling](#the-impact-of-the-secs-cybersecurity-ruling)
  - [Impact of law enforcement actions](#impact-of-law-enforcement-actions)
- [Top 5 Ransomware Families to Watch in 2024-2025](#top-5-ransomware-families-to-watch-in-2024-2025)
  - [#1 Dark Angels](#1-dark-angels)
  - [#2 LockBit](#2-lockbit)
  - [#3 BlackCat](#3-blackcat)
  - [#4 Akira](#4-akira)
  - [#5 Black Basta](#5-black-basta)
- [ThreatLabz Ransomware Notes Archive](#threatlabz-ransomware-notes-archive)
- [2025 Predictions](#2025-predictions)
- [How Zscaler Simplifies Ransomware Protection](#how-zscaler-simplifies-ransomware-protection)

---

## Executive Summary

Ransomware attacks have reached new heights of ambition and audacity over the past year, marked by a notable surge in extortion attacks. Adding to the increase in ransomware attacks, ThreatLabz research uncovered an unprecedented ransom payout of US$75 million—the largest ever paid by one company. This amount is nearly double the highest publicly known ransom payment.[^1] In 2023 alone, ransomware payments exceeded $1 billion, highlighting the escalating financial impact of these cybercrimes.

Ransomware threat actors’ tactics have become increasingly sophisticated and bold. Notably, they have surpassed the traditional boundaries of the corporations they attack, even going so far as to target the children of executives to provoke faster and higher ransoms.[^2] From critical infrastructure[^3] and major corporations[^4] to small and medium-sized enterprises, no organization is immune to finding themselves in the crosshairs of the next campaign or evolution of attacks.

Despite law enforcement takedowns of multiple initial access brokers under special ops “Operation Endgame” and “Operation Duck Hunt,” many of the largest active ransomware families continue to rapidly regroup and launch new attacks while barely skipping a beat. Unfortunately, many ransomware actors are beyond the reach of law enforcement, making them virtually immune to criminal prosecution. As detailed in this report, law enforcement agencies have augmented their pressure tactics through reward money, sanctions, trolling, and exposing the individuals behind ransomware using various forms of psychological tactics.

As ransomware actors continuously evolve their tactics, it is crucial to stay up to date on how the threat landscape is changing.

The Zscaler ThreatLabz 2024 Ransomware Report offers an overview of the ransomware threat landscape from April 2023 through April 2024, detailing the latest trends, targets, ransomware families, and effective defense strategies.

ThreatLabz found that ransomware attacks increased by 17.8% year-over-year based on blocked attempts in the Zscaler cloud, while ransomware attacks identified through data leak site analysis surged by 57.8%. The most common targets were businesses in the manufacturing, healthcare, and technology sectors, putting critical operations and infrastructure squarely in the line of attack.

The findings presented in this report underscore the need for organizations to prioritize protection against the relentless tide of ransomware. The insights and strategies in the report serve as a crucial guide for improving your ransomware defenses. By understanding the latest trends and vulnerabilities, and implementing recommended best practices, you can significantly reduce the risk of becoming a ransomware victim and better protect your organization’s critical assets and data.

[^1]: Bloomberg, CNA Financial Paid $40 Million in Ransom After March Cyberattack, May 20, 2021.
[^2]: Business Insider, Hackers are now targeting the children of corporate executives in ransomware attacks, May 12, 2024.
[^3]: Dark Reading, Ascension Healthcare Suffers Major Cyberattack, May 10, 2024.
[^4]: CyberScoop, Boeing confirms attempted $200 million ransomware extortion attempt, May 8, 2024.

---

## Key Findings

- Zscaler ThreatLabz research uncovered a record-breaking ransom payment of US$75 million—the largest ransomware payment by a company in history—nearly double the highest publicly known payout.
- Ransomware attacks blocked by the Zscaler cloud increased by 17.8%, and the number of extorted companies on data leak sites grew by 57.8% in the same period year-over-year despite numerous law enforcement operations, including the seizure of infrastructure along with arrests, criminal indictments, and sanctions.
- The manufacturing, healthcare, and technology sectors were the top targets of ransomware attacks, while the energy sector experienced a 500% year-over-year spike as critical infrastructure and susceptibility to operational disruptions make it particularly attractive to cybercriminals.
- The United States remains the top target of ransomware, experiencing 49.95% of overall attacks, followed by the United Kingdom, Germany, Canada, and France.
- ThreatLabz identified 19 new ransomware families during the analysis period, bringing the total number to 391 since our tracking started.
- The most active ransomware families were LockBit (22.1%), BlackCat (a.k.a. ALPHV) (9.2%), and 8Base (7.9%).
- Vulnerabilities remain an all-too-common ransomware attack vector, emphasizing the importance of timely patching and unified vulnerability management, underpinned by a zero trust architecture to provide protection even when patches are not available.
- Voice-based social engineering attacks are increasingly being used to gain access to corporate networks—a technique used by Scattered Spider and the Qakbot threat group.

---

## Ransomware Landscape: Top Trends and Targets

The dynamic nature of ransomware has placed it at the forefront of security concerns in recent years. Threat actors are constantly evolving their methods of attack and extortion, leveraging advances in artificial intelligence (AI) technology, leaked source code, and advanced encryption to maximize their impact and profitability.

This report examines the following ransomware attack trends from April 2023 through April 2024:
- Overall rise in ransomware attacks
- Industry verticals most impacted by ransomware
- Geographical distribution of victim organizations
- Top ransomware threats and record-breaking ransom payments
- Increased law enforcement action against ransomware groups and initial access brokers

### Overall rise in ransomware attacks

The latest ThreatLabz analysis reveals a concerning trend, with a 17.84% year-over-year increase in ransomware attacks based on blocked attempts observed across the Zscaler cloud. The rise in ransomware activity translates to significant disruptions and financial impacts to victim organizations of all sizes.

![Chart showing number of attempts blocked in Zscaler cloud: 1,502,175 in 2021; 2,727,114 in 2022; 3,756,858 in 2022-2023; 4,426,966 in 2023-2024]

### Industry verticals most impacted by ransomware

Ransomware extortion attacks have consistently surged, with the number of victim companies listed on data leak sites increasing by 57.81% since last year’s ThreatLabz report. The manufacturing industry was by far the most targeted industry, accounting for 653 attacks.

![Bar chart showing top 20 industries impacted by ransomware, led by Manufacturing (653), Healthcare (312), and Technology (265)]

### Geographical distribution of victim organizations

The United States faced a markedly higher volume of ransomware attacks than any other country, accounting for about 50% of all incidents globally.

![Heatmap of global ransomware victims: US (49.95%), UK (5.92%), Germany (4.09%), Canada (3.51%), France (3.26%)]

### Most active ransomware groups in 2023-2024

LockBit (22.1%), BlackCat (9.2%), and 8Base (7.9%) were the most active ransomware extortion groups over the past year.

![Bar chart showing data leak victims per ransomware family: LockBit (988), BlackCat (410), 8Base (352), Play (345), Clop (291), and others]

### Major vulnerabilities used in ransomware attacks

Vulnerabilities in software, systems, and the overall digital infrastructure can serve as critical entry points for ransomware attacks.

- **ConnectWise ScreenConnect**: CVE-2024-1708 and CVE-2024-1709.
- **Cisco ASA and FTD software**: CVE-2020-3259.
- **Cisco remote access VPN**: CVE-2023-20269.
- **Citrix NetScaler ADC and Gateway**: CVE-2023-4966 (Citrix Bleed) and CVE-2023-3519.

---

## Ransomware Roundup: What’s Making Headlines

### The ransomware plague in healthcare

The healthcare industry faced significant challenges throughout 2023 and into 2024. A healthcare technology provider for payment solutions fell victim to the BlackCat group; despite paying a $22 million ransom, the group reneged on their promise to share the ransom with the affiliate, leading to further threats of data release.

### The impact of the SEC’s cybersecurity ruling

Effective December 15, 2023, new SEC rules mandate the timely reporting of material cybersecurity incidents for publicly traded companies. This creates a challenge for ransomware actors who rely on private payment resolution, as companies are now required to disclose the breach.

### Impact of law enforcement actions

- **Operation Duck Hunt**: Targeted the Qakbot botnet, which had infected over 700,000 computers. While the infrastructure was disrupted, the group resurfaced in December 2023 with updated TTPs.
- **Operation Endgame**: Targeted initial access brokers including SmokeLoader, Pikabot, Bumblebee, and IcedID. Over 40,000 systems infected with SmokeLoader were cleaned as a result.
- **Hive Rebranding**: After the FBI disrupted Hive, the group rebranded as Hunters International in October 2023, adopting a non-negotiable price policy.

---

## Top 5 Ransomware Families to Watch in 2024-2025

### #1 Dark Angels
Known for highly targeted attacks on large enterprises and record-breaking ransom demands (e.g., $75 million). They focus on exfiltrating massive amounts of data (10-100 TB).

### #2 LockBit
The most active group by volume, utilizing a massive affiliate network. Despite infrastructure seizures by law enforcement in February 2024, the group remains active.

### #3 BlackCat
Known for cross-platform compatibility (Rust-based). Though they announced disbandment in March 2024 following an exit scam and FBI pressure, their affiliates have migrated to other RaaS networks like RansomHub.

### #4 Akira
Likely an offshoot of the Conti group. They are highly active and have not yet been subject to a major law enforcement disruption.

### #5 Black Basta
Another successor to the Conti group. They have pivoted to sophisticated voice-based social engineering (vishing) to gain initial access, often impersonating IT help desk staff.

---

## ThreatLabz Ransomware Notes Archive

Zscaler ThreatLabz maintains a public GitHub repository tracking 391 ransomware families and 945 ransom notes. This archive allows for stylometric analysis, which has successfully linked groups like Black Basta to former members of the Conti collective.

---

## 2025 Predictions

1. **Targeted Strategies**: More groups will adopt the "Dark Angels" model of high-value, low-volume targeting.
2. **Voice-based Social Engineering**: Increased use of vishing to bypass MFA and gain initial access.
3. **GenAI Adoption**: Use of AI for perfect phishing emails and voice cloning.
4. **SEC Reporting**: Continued increase in public disclosures of ransomware incidents.
5. **Encryption-less Extortion**: A rise in attacks focused solely on data exfiltration.
6. **Healthcare Targeting**: Persistent attacks on healthcare due to legacy system vulnerabilities.
7. **International Collaboration**: Continued global law enforcement efforts to disrupt RaaS infrastructure.

---

## How Zscaler Simplifies Ransomware Protection

The Zscaler Zero Trust Exchange™ platform provides a holistic approach to stopping ransomware by:
- **Making assets invisible**: Preventing attackers from discovering or exploiting users and applications.
- **Inline Inspection**: Inspecting all inbound and outbound traffic, encrypted or not.
- **Preventing Lateral Movement**: Connecting users directly to applications rather than the network, ensuring that even if a breach occurs, the attacker cannot move laterally to encrypt or steal data.

---

lls

and VPNs, often introduce blind spots,

complexity, and significant costs.

These legacy approaches fail to cost-

effectively inspect encrypted files

and traffic, leaving organizations

vulnerable to lateral movement and

ransomware attacks that exploit gaps

in visibility and control—often with

devastating consequences.

I N WITH  ZE RO TRU ST:  A zero trust
architecture assumes every user, device,

and connection is potentially compromised.

This approach mandates continuous

verification and strict access control.

By consistently verifying identities

and inspecting all traffic, including

encrypted data, zero trust significantly

reduces the risk of attacks spreading

within the network, neutralizing

ransomware threats before they can

inflict damage.

29

ThreatLabz 2024 Ransomware Report©2024 Zscaler, Inc. All rights reserved.Z S C A L E R   S TO P S   R A N S O MWA R E   AT   E V E RY
S TAG E   O F   T H E   AT TAC K   C YC L E—from initial
reconnaissance and compromise to lateral
movement, data theft, and payload execution.

Minimize the attack surface: Built on a zero
trust architecture, the Zero Trust Exchange
replaces exploitable legacy VPN and firewall
architectures that expand the attack surface.
Zscaler effectively minimizes the attack
surface by hiding users, applications, and
devices behind a cloud proxy, where they are
not visible or discoverable from the internet.
Similar to a switchboard routing calls to
authorized destinations, Zscaler only connects
the right, authorized user or device to a
particular application.

websites as well as detect unknown threats
before they reach your network. This minimizes
the risk of compromise in the first place.

Eliminate lateral movement: Leveraging user-
to-app or app-to-app segmentation, users
connect directly to applications (and apps
to other apps), not the network, eliminating
the risk of lateral movement. By centralizing
access control policy management, Zscaler acts
like a security checkpoint for internet traffic,
removing pathways for lateral movement.
Zscaler can also identify and stop potential
attackers from moving laterally, whether
external threats or malicious insiders, through
identity threat detection and response (ITDR)
and deception capabilities.

Prevent initial compromise: The Zero
Trust Exchange employs extensive TLS/SSL
inspection, browser isolation, advanced inline
sandboxing, and policy-driven access controls
to prevent users from accessing malicious

Stop data loss: Inline data loss prevention
measures, combined with full TLS/SSL
inspection, effectively thwart data theft
attempts. Zscaler ensures that data is secured
both in transit and at rest.

F I G H T I N G   A I - D R I V E N   T H R E AT S  W I T H   A I  +

Z E R O   T R U S T   I N N OVAT I O N

These AI-driven capabilities enable Zscaler to offer robust

protection against ransomware, ensuring comprehensive security

for enterprises in the evolving threat landscape:

•  AI-powered phishing and C2 detection uses inline AI-based
detection from the Zscaler Secure Web Gateway to identify

and block never-before-seen phishing sites and command-and-

control (C2) infrastructure.

•  AI-powered sandboxing offers comprehensive malware and zero-
day threat prevention by analyzing suspicious files in a

controlled environment.

•  AI-powered segmentation provides automated access policy

recommendations to minimize the attack surface and prevent

lateral movement, using user context, behavior, location,

and private app telemetry.

•  Dynamic, risk-based policy continuously analyzes the risk

associated with users, devices, and applications to enforce

dynamic security and access policies.

•  AI-powered browser isolation creates a secure gap between
users and malicious web content by rendering pages as

streams of picture-perfect images, preventing data leaks and

the delivery of active threats.

•  AI-driven data discovery and classification provides instant
data visibility and classification out of the box across

endpoint, inline, and cloud data, making it more difficult

for ransomware to target and encrypt sensitive data.

30

ThreatLabz 2024 Ransomware Report©2024 Zscaler, Inc. All rights reserved.Holistic prevention at each stage
of the attack chain

Minimize attack
surface

Prevent initial
compromise

Prevent
lateral movement

Stop data loss
& malware delivery

Gain initial
entry

Establish
foothold

Deliver
malware

Install
malware

Hide (proxy)
applications &
restrict access

Full SSL inspection, browser
isolation, advanced threat protection,
sandbox, deception decoys

Steal
credentials
& compromise
additional
systems

Connect users
directly to apps;
expose attackers
with decoys

Steal data

Install
ransomware &
demand payment

DLP (SSL) , secure SaaS
data (CASB)

Always-on SSL/TLS inspection

Figure 23: Mapping zero trust architecture across the ransomware attack chain.

31

©2024 Zscaler, Inc. All rights reserved.ThreatLabz 2024 Ransomware ReportRelated Zscaler products

Zscaler Internet Access™ (ZIA™) provides secure and direct access
to the internet, offering inline threat protection. ZIA’s advanced threat
prevention and sandboxing capabilities help thwart ransomware
downloads, and command-and-control (C2) communications, preventing
ransomware infiltration.

Zscaler Private Access™ (ZPA™) enables secure access to internal
applications without internet exposure, employing a zero trust model.
ZPA ensures that only authorized users and devices can access
critical applications, thus reducing the attack surface and preventing
ransomware attempts.

Zscaler Zero Trust Firewall intercepts and inspects TLS/SSL traffic to
detect malware hidden in encrypted traffic, preventing its infiltration into
the network.

Zscaler Deception detects and contains attackers attempting to move
laterally or escalate privileges by luring them with decoy servers,
applications, directories, and user accounts.

Zscaler Sandbox analyzes suspicious files and executables in a controlled
virtual environment, helping to identify and block malicious code, keeping
organizations ahead of file-based ransomware and zero-day attacks.

Zscaler Cloud Browser isolates web sessions and streams only pixels to
devices to effectively eliminate the risk of drive-by downloads and zero-
day exploits that may be used by ransomware operators.

Zscaler ITDR (Identity Threat Detection and Response) detects and
defends against identity-based attacks such as credential theft and
privilege abuse, Active Directory assaults, and risky entitlements.

Zscaler Data Protection provides consistent, unified security for data in
motion and data at rest across SaaS and public cloud applications, reducing
the likelihood of data exfiltration while mitigating the potential impact of
ransomware attacks.

32

ThreatLabz 2024 Ransomware Report©2024 Zscaler, Inc. All rights reserved.Ransomware Prevention

Guidance

A defense strategy rooted in zero trust architecture is a proven security measure for stopping ransomware, but tackling this multifaceted threat
demands proactive planning, ongoing collaboration, and strategic investments.

ThreatLabz experts have compiled the latest best practices to help reduce ransomware risks and safeguard your organization against existing and
emerging threats.

Implement regular and secure data
backups. Ensure all data is backed up
regularly and securely, including offline
backups. Adapt backup strategies based
on evolving threats.

Keep software updated. Apply the latest
security patches promptly to address
known vulnerabilities. Use AI-driven
threat intelligence platforms to prioritize
and manage security patches effectively.

Enable multifactor authentication (MFA).
Add an extra layer of security to user
accounts with MFA to mitigate the risk
of unauthorized access. Integrate MFA
solutions to detect and prevent account
takeovers effectively.

Establish a consistent corporate security
policy. Ensure all users follow consistent
security procedures, including MFA and
regular security updates, to help prevent
initial compromises. With a distributed
workforce, it is even more important to
implement a security service edge (SSE)
architecture to protect users no matter
where they are.

Bolster application security. Remove
applications from the public internet
to prevent ransomware actors from
exploiting vulnerabilities. Implement
a zero trust architecture for internal
applications to safeguard them against
ransomware attempts.

Enforce least-privileged access.
Implement least-privileged policies to
restrict user access to only the resources
necessary for their roles. Utilize AI-powered
solutions to dynamically analyze user behavior
and adapt access privileges accordingly.

Strengthen identity protection.
Use ITDR tools to gain visibility into
identity misconfigurations, remediate
vulnerabilities in Active Directory that
adversaries exploit to escalate privileges
and move laterally, and detect stealthy
identity threats.

Inspect all traffic. Today, 86% of threats
are delivered over encrypted channels,
which are often not inspected, making it
easy for even moderately sophisticated
attackers to bypass security controls. It’s
essential to inspect all traffic, encrypted
or not, to prevent compromise.

Implement zero trust network access
(ZTNA). Deploy granular user-to-
application and application-to-application
segmentation, brokering access via
least-privileged access controls to
eliminate lateral movement, minimize
data exposure, and enhance your overall
security posture.

33

©2024 Zscaler, Inc. All rights reserved.ThreatLabz 2024 Ransomware ReportUtilize a cloud access security broker
(CASB). Control and monitor cloud
application usage with a CASB to prevent
malicious activities like file downloads and
data exfiltration.

Provide ongoing employee training.
Conduct regular security awareness
training to educate employees about
ransomware threats. Employ simulations
of real-world ransomware scenarios to
enhance employee preparedness.

Develop a comprehensive ransomware
response plan. Create a response plan
encompassing data recovery, incident
response, and communication protocols
to act swiftly and effectively in the event
of a ransomware attack.

Utilize AI-driven browser isolation.
Protect users from web threats with AI-
based isolation of suspicious internet
content and high-risk users. By isolating
the browser experience and restricting
potentially harmful actions (like inputting
credentials), users can safely access
suspicious URLs and files without risking
their system’s security.

Employ AI-powered advanced
sandboxing. Stop never-before-seen
and elusive malware with a sandbox that
automatically detects and quarantines
unknown threats and suspicious files
leveraging AI/ML analysis.

Deploy inline data loss prevention
(DLP). Safeguard against data exfiltration
and exposure by deploying inline
DLP measures.

Leverage deception technology. Employ
deception tools and honeypots to
misdirect attackers, fortifying defenses
against system infiltration.

Follow Zscaler ThreatLabz for regular insights on the latest
ransomware threats and developments, including published

indicators of compromise (IOCs) and MITRE ATT&CK mappings. This

information can be used to train your team, improve your security

posture, and help prevent ransomware attacks.

ThreatLabz also maintains GitHub repositories with IOCs, tools
(including proof-of-concept ransomware decryption tools), and an

archive of ransomware notes from all major ransomware groups.

X @ThreatLabz | ThreatLabz security research blog

34

©2024 Zscaler, Inc. All rights reserved.ThreatLabz 2024 Ransomware ReportReport

Methodology

The research methodology for this report is a comprehensive process that uses multiple data sources
to identify and track ransomware trends. The report team collected data from a variety of sources
between April 2023 and March 2024, including:

•  The Zscaler global security cloud, which processes more than 500 trillion daily signals, blocks
more than 9 billion threats and policy violations per day, and delivers 250,000+ daily security
updates to Zscaler customers. We analyzed this data—which includes information about
  source IP addresses, destination IP addresses, and file types associated with ransomware
attacks—to identify ransomware activity.

•

External intelligence sources. We also collected data from external intelligence sources, such as
threat intelligence feeds, open source research, and law enforcement reports, which provided
additional information about ransomware attackers, their targets, and their methods.

•  The ThreatLabz team’s own analysis of ransomware samples and attack data. The ThreatLabz

Threat Intelligence team tracks ransomware families at scale through reverse engineering and
automating malware analysis to develop effective response strategies. ThreatLabz also works
closely with international law enforcement agencies and has played a significant role in recent
actions, including Operation Duck Hunt and Operation Endgame.

About ThreatLabz

ThreatLabz is the security research arm of Zscaler. This world-class team is responsible
for hunting new threats and ensuring that the thousands of organizations using the global
Zscaler platform are always protected. In addition to malware research and behavioral
analysis, team members are involved in the research and development of new prototype
modules for advanced threat protection on the Zscaler platform, and regularly conduct
internal security audits to ensure that Zscaler products and infrastructure meet security
compliance standards. ThreatLabz regularly publishes in-depth analyses of new and
emerging threats on its portal, research.zscaler.com.

About Zscaler

Zscaler (NASDAQ: ZS) accelerates digital transformation so that customers can be more
agile, efficient, resilient, and secure. The Zscaler Zero Trust Exchange™ protects thousands
of customers from cyberattacks and data loss by securely connecting users, devices, and
applications in any location. Distributed across more than 150 data centers globally, the
SASE-based Zero Trust Exchange is the world’s largest inline cloud security platform. To
learn more, visit www.zscaler.com.

35

©2024 Zscaler, Inc. All rights reserved.ThreatLabz 2024 Ransomware Report© 2024 Zscaler, Inc. All rights reserved. Zscaler™ and other trademarks listed at zscaler.com/legal/trademarks
are  either  (i)  registered  trademarks  or  service  marks  or  (ii)  trademarks  or  service  marks  of  Zscaler,  Inc.  in  the
United States and/or other countries. Any other trademarks are the properties of their respective owners.