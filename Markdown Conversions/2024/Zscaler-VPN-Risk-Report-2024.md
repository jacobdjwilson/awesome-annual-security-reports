Zscaler
ThreatLabz 2024
VPN Risk Report
Explore key VPN security, risk, and user
experience trends as zero trust adoption
reaches critical momentum.
©2024 Zscaler, Inc. All rights reserved.

Contents
03 Overview 16 Lateral Movement in VPN Attacks
04 Key Findings 17 VPN Security Concerns After M&A
05 Security Concerns With VPN 18 Enterprise Adoption of Zero Trust
05 VPN Attacks on the Rise 18 Progress in Zero Trust Adoption
06 Major VPN Vulnerabilities in the Past Year 19 No Zero Trust Security Through VPN
07 Navigating VPN Security Concerns 19 Advancing from VPN to Zero Trust Network Access
08 Key Scenarios for Secure Access 20 Why Zero Trust Is More Secure Than VPN
09 VPN Management, Performance, and 21 Key Differences and Advantages
User Experience 22 VPN Predictions for 2024 and Beyond
09 Challenges in VPN Management 23 How Zscaler Enables VPN Replacement and
10 Common VPN User Challenges Zero Trust Transformation
11 VPN Vulnerability Exploits 24 Zero Trust Networking
12 Third-Party VPN Risk 24 Cyberthreat Protection
13 Security Issues With VPN Infrastructure 24 Data Protection
13 Overconfidence in VPN Security 25 Best Practices to Counter VPN Risks
14 Ransomware Attack Vectors 26 Methodology and Demographics
15 Ransomware Concerns
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 02

Overview
Today’s distributed and cloud-centric work environment has triggered a shift in access outlines more advanced security models, particularly zero trust, which has firmly
methods from traditional virtual private networks (VPNs) to more robust security established itself as a robust and future-proof framework to secure and accelerate
frameworks like zero trust. Traditionally, VPNs provided essential remote access digital transformation.
capabilities to connect users or entire office sites. However, the growing sophistication
We are grateful to Zscaler for contributing to this VPN risk survey. Their expertise in
of cyberthreats alongside the expansion of remote workforces and cloud technologies
zero trust and secure access solutions has significantly enriched our findings. We are
have exposed significant vulnerabilities in VPNs. Due to their legacy architecture, VPNs
confident that the insights from this report will be an essential resource for IT and
grant overly broad network access once credentials are verified, significantly increasing
cybersecurity professionals on your journey toward zero trust security.
the risk of cyberattacks if those credentials are compromised.
Thank you,
Recent high-profile exploits of VPN appliances have highlighted critical vulnerabilities
Holger Schulze, Founder, Cybersecurity Insiders
(notably CVE-2023-46805, CVE-2024-21887, and CVE-2024-21893) affecting
essential sectors, including US defense. These vulnerabilities enable attackers to bypass
authentication, execute commands with elevated privileges, and maintain persistence
after device resets. In response, the US Cybersecurity and Infrastructure Security Agency
(CISA) issued an emergency directive to federal agencies to immediately disconnect
affected VPN devices due to substantial security risks.
Through Executive Order 14028, the US government now mandates the adoption
of zero trust architectures to enhance cybersecurity, moving away from traditional
VPNs. This directive, part of a comprehensive strategy to fortify national cybersecurity,
“Over the past year, numerous critical VPN vulnerabilities have served
instructs federal agencies to implement zero trust, which verifies every access request
irrespective of origin. The Office of Management and Budget (OMB) further supports as successful entry points for attacks on large enterprises and federal
this initiative with a detailed Federal Zero Trust Strategy, underscoring the shift from entities. Considering these repeated outcomes, it’s crucial for enterprises
VPN-based implicit trust within network perimeters to continuous verification of any
to anticipate that threat actors will increasingly exploit these legacy,
and all access requests. These directives and recommendations reflect a consensus
internet-exposed assets—appliances and virtual—that enable them
within the cybersecurity community that zero trust provides a more robust defense
against complex and evolving cyberthreats, a necessity underscored by the recent to easily navigate laterally across traditional flat networks. It is essential
vulnerabilities and exploits related to traditional VPNs. to transition to Zero Trust architecture, which significantly reduces the
attack surface by eliminating legacy technologies like VPNs and firewalls,
As a result, organizations are rapidly adopting zero trust models, which do not inherently
trust any user or device inside or outside the network perimeter and require granular enforces consistent security controls with TLS inspection, and limits the
verification for every access request. This model is particularly effective in preventing blast radius with segmentation and deception, preventing damaging
lateral movement within networks—an exploit that attackers often use to deepen their
breaches.”
intrusion after gaining initial access.
—DEEPEN DESAI, CHIEF SECURITY OFFICER, ZSCALER
Based on a survey of 647 IT professionals and cybersecurity experts, this report
explores the multifaceted security and user experience challenges of VPNs to reveal
the complexity of today’s access management, vulnerabilities to various cyberattacks,
and their potential to impair organizations’ broader security posture. The report also
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 03

Key Findings
VPN attacks are on the rise. VPNs are no match for ransomware,
malware, and DDoS.
56% of organizations experienced one or more VPN-related
cyberattacks in the last year—up from 45% the year before— Respondents identified ransomware (56%), malware
highlighting the growing frequency and sophistication of (35%), and DDoS attacks (30%) as the top threats exploiting
attacks targeting VPNs. VPN vulnerabilities, underscoring the breadth of risks
organizations face due to inherent weaknesses in
traditional VPN architectures.
The vast majority are shifting to zero trust. The risk of lateral movement can’t be ignored.
78% of organizations plan to implement zero trust strategies in 54% of enterprises breached via VPN vulnerabilities say threat
the next 12 months. Meanwhile, 62% of enterprises agree that actors moved laterally, demonstrating containment failures at
VPNs are anti-zero trust. the initial point of compromise that underscore the risks of
traditional, flat networks.
Most have doubts about VPN security.
91% of respondents expressed concerns about VPNs
compromising their IT security environment, with recent
breaches illustrating the risks of maintaining outdated or
unpatched VPN infrastructures.
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 04

Security Concerns With VPN
VPN Attacks on the Rise
In the last 12 months, how often has your organization
The frequency and severity of attacks exploiting VPN vulnerabilities highlight the
experienced an attack that took advantage of security
ineffectiveness of conventional cybersecurity measures and underscore the persistent
vulnerabilities in your VPN servers?
risks posed by network exposure. Our survey reveals that 56% of organizations
experienced cyberattacks in the last year that took advantage of VPN vulnerabilities,
a significant increase from 45% the year before. Alarmingly, 35% of organizations
reported suffering two or more VPN-related attacks, indicating severe security gaps.
Once
15%
2-3 times
56%
Never 21%
of organizations
44%
4-5 times experienced VPN
related cyberattcks
7% in the last year
More than
5 times
13%
Recent trends confirm that attacks on VPNs are becoming not only more frequent,
but also more sophisticated. For instance, more cases of ransomware exploiting VPN
flaws—particularly in the aftermath of publicly disclosed vulnerabilities—highlight
the critical weaknesses inherent in traditional VPNs. Such vulnerabilities give attackers
easy entry points to infiltrate networks and facilitate lateral movement, leading to
substantial data breaches and operational disruption.
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 05

SECURITY CONCERNS WITH VPN
Major VPN Vulnerabilities in the Past Year
Amid the recent string of high-severity CVEs impacting VPN products, it’s no surprise that enterprises are reporting more attacks that exploit these kinds of vulnerabilities. Of course, no single
vendor or any particular technology can be immune from software vulnerabilities. In the case of VPN, the challenge for enterprises is that each CVE can represent a single security point of failure
for the enterprise: a beachhead that allows attackers to compromise a VPN asset, establish persistence, move laterally across the network, and steal data. As VPN CVEs continue to be disclosed at
this pace, they will be a persistent risk for enterprises that use VPNs for remote connectivity.
String of recent CVEs highlights an architecture flaw
CVE-2023-21888 &
CVE-2024-3400
CVE 2023-21893
CVE-2024-22394
|     |     |     | Privilege escalation | Allows attackers to execute  |     |
| --- | --- | --- | -------------------- | ---------------------------- | --- |
arbitrary code with root
|     | Allows remote attacker   |     | and server-side request  |                            |     |
| --- | ------------------------ | --- | ------------------------ | -------------------------- | --- |
|     | to bypass authentication |     |                          | privileges on the firewall |     |
forgery exploits
|            |                   |            | Ivanti discloses two       |          | PAN-OS zero-day  |
| ---------- | ----------------- | ---------- | -------------------------- | -------- | ---------------- |
|            | SonicWall SSL-VPN |            | additional vulnerabilities |          | critical exploit |
|            | January 10        |            | January 31                 |          | April 12         |
|            | 2024              |            | 2024                       |          | 2024             |
| October 27 |                   | January 11 |                            | March 12 |                  |
| 2023       |                   | 2024       |                            | 2024     |                  |
Ivanti discloses two
|                         |     | Fortinet discloses       |     | Fortinet discloses 2 ‘critical’  |     |
| ----------------------- | --- | ------------------------ | --- | -------------------------------- | --- |
| vulnerabilities ICS and |     | vulnerability on FortiOS |     | and 3 ‘high severity’ flaws      |     |
IPS products
CVE-2023-46805 & CVE-2024-23112 CVE-2024-23112, CVE-2023-48788
| CVE-2023-21887 |     |     | CVE-2023-47534 CVE-2023-36554 |     |     |
| -------------- | --- | --- | ----------------------------- | --- | --- |
Authorization bypass
| Bypass authentication  |     |     |     | CVE-2024-42789 |     |
| ---------------------- | --- | --- | --- | -------------- | --- |
allows authenticated
| check and run command  |     |     |     | RCE on admin workstation,  |     |
| ---------------------- | --- | --- | --- | -------------------------- | --- |
attacker access to another
injections exploits user bookmarks etc inside attacker can execute
arbitary codes or crafted
HTTP requests
06
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT

SECURITY CONCERNS WITH VPN
Navigating VPN
Security Concerns
How concerned are you that VPN may jeopardize your
ability to keep your environment secure?
The survey results reflect deep-seated concerns about VPNs compromising
security environments, echoing ongoing trends and increasing vulnerabilities in 91% are concerned that their
VPN may jeopardize their
VPN technologies. An overwhelming majority of respondents (91%, up from 88%
environment’s security
in 2023) express concerns about VPNs jeopardizing their IT security, underscoring
heightened awareness of VPN-related risks among organizations. 35
31%
This concern is justified by recent exploits targeting Ivanti VPNs, where attackers
leveraged severe vulnerabilities to infiltrate networks and exfiltrate sensitive data. 30
These incidents, involving vulnerabilities like CVE-2024-21888 and CVE-2024- 27%
21893, highlight the risks of maintaining and securing outdated or unpatched VPN
infrastructures. Moreover, the inherent architecture of VPNs poses significant
25
security risks in today’s perimeter less digital landscape. As businesses increasingly
adopt cloud services and as remote work models evolve, VPNs face new security
20%
challenges, including managing broad access rights and securing an expanding
20
attack surface.
These vulnerabilities and architectural limitations underscore a pivotal shift in
perceptions toward VPN security, aligning with broader cybersecurity trends that 15 13%
advocate for more dynamic and resilient frameworks such as zero trust.
9%
10
Forward-looking organizations transition toward zero trust
architectures to gain more granular control and significantly reduce 5
the attack surface by never conferring implicit trust, whether inside
or outside a network perimeter. Adopting such a strategy addresses
the immediate vulnerabilities of traditional VPNs and aligns with 0
a proactive cybersecurity approach, essential for adapting to the Not at all Slightly Moderately Very Extremely
concerned concerned concerned concerned concerned
evolving threat landscape.
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 07

SECURITY CONCERNS WITH VPN
Key Scenarios for
Secure Access What is the primary purpose for your
organization’s use of VPN?
Understanding why organizations use VPNs is essential, as it highlights how
they prioritize secure access across various business scenarios. It also reveals
which networking use cases are most exposed to security risks, indicating areas Access for 70%
remote employees
that require more robust and innovative access security strategies.
A significant 70% of organizations use VPNs primarily to secure access for Connecting 33%
multiple sites
remote employees. This widespread use makes remote access a prime target
for cyberattacks. Following this, 33% use VPNs to connect multiple sites,
Access for 26%
presenting substantial risks, as these connections can serve as vectors for third parties
cyberattacks if not properly secured. Next, 26% of organizations noted access
for third parties, which further complicates security due to the varying security On-campus 20%
access
postures of different external stakeholders and lack of control over security
policies. Additionally, 20% of organizations use VPNs for on-campus access,
and 19% use them for IoT/OT device connectivity. IoT/OT device 19%
connectivity
Access for 16%
unmanaged devices
0 10 20 30 40 50 60 70 80
VPNs no longer provide adequate security for critical access use cases in today’s
evolving cyberthreat landscape because they operate on outdated trust models that
grant extensive network access upon simple user authentication. This broad access
exposes organizations to significant risks by allowing potential attackers to exploit a
single point of entry to navigate and extract sensitive data across the network.
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 08

VPN Management, Performance,
and User Experience
Challenges in VPN
What’s the biggest headache in manging your
Management
VPN infrastructure?
In addition to inherent security risks, managing VPN infrastructures presents
significant challenges for IT teams as the requirements for robust access solutions Balancing VPN performance
intensify in dispersed, cloud-centric work environments. The primary management and user experience
challenge for IT professionals is the balancing act between VPN performance and 19%
user experience (19%). This issue is crucial because it directly impacts productivity:
if the VPN slows down the network or proves too cumbersome to use, it can lead 17% Constantly troubleshooting VPN
to lower employee satisfaction and slow, inefficient business processes. connectivity and stability issues
The next most common concern, cited by 17% of respondents, is constant
troubleshooting of VPN connectivity and stability issues. These problems are Juggling VPN compatibility
16%
not only time-consuming for IT staff, but also cause frustrating disruptions for with various devices, operating
systems, and applications
users. Other notable challenges include VPNs’ lack of compatibility with a diverse
range of devices, operating systems, and applications, which about 16% of IT
professionals find burdensome. Additionally, 13% of respondents struggle with the
complexity and labor-intensive nature of scaling VPN infrastructure, a critical issue 13% Navigating the complexity and effort
involved in scaling VPN infrastructure
as organizations grow and their needs increase amid a severe shortage of skilled
cybersecurity professionals.
These insights underscore the need for organizations to explore more agile, user- 11% Playing catch-up with frequent VPN
friendly, and less resource-intensive alternatives, such as zero trust network access software patches and updates
(ZTNA) models. ZTNA provides more granular control, enhanced scalability, and
9%
reduced management overhead, making it a superior choice to traditional VPN in
today’s dynamic cybersecurity landscape. Bearing the burden of
increasing VPN infrastructure
costs
Other 15%
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 09

VPN MANAGEMENT, PERFORMANCE, AND USER EXPERIENCE
Common VPN
What is the most common complaint reported by your
User Challenges
users when accessing applications via VPN?
The most frequent user complaint about VPN use, as noted by 26% of
respondents, is slow connection speeds. This highlights a critical user Slow co w nn h e e c n t i a o c n c e s s p s e in ed g 26%
productivity and satisfaction issue, as slow speeds can significantly reduce the applications
efficiency of routine tasks and access to cloud-based resources, especially in
Problem with
work-from-home environments. connection drops 19%
while using VPN
VPN connection drops represent the second-most common issue, cited by 19%
Inconsistent user
of respondents. This problem can disrupt ongoing tasks and communications, experience across different 12%
devices/platforms
significantly affecting user experience and operational continuity. Inconsistent
user experiences across different devices and platforms, reported by 12% of Complex or
cumbersome VPN 11%
users, points to a need for more uniform access performance. authentication process
Difficulty accessing
applications due to 9%
authentication issues
Inability to connect to
VPN or to access 8%
applications altogether
0 5 10 15 20 25 30
Other 15%
To address these concerns, organizations should consider adopting network
access solutions that offer more stability and consistency across various platforms.
Implementing a zero trust architecture can be particularly effective, as it enhances
security without introducing performance bottlenecks. Zero trust networks ensure that
connection issues do not compromise security and that access control is both strict
and adaptable to different user environments.
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 010

VPN MANAGEMENT, PERFORMANCE, AND USER EXPERIENCE
VPN Vulnerability Exploits
Which types of cyberattacks do you think are most
likely to exploit your organization’s VPN vulnerabilities?
The variety of cyberattacks that exploit VPN weaknesses highlights the breadth of
risks organizations face. The survey reveals that 56% of respondents identify
56% Ransomware ransomware attacks as most likely to exploit VPN vulnerabilities, highlighting significant
attacks impact and frequent occurrences. This is followed by malware infections, reported by
35% of respondents, and DDoS attacks, noted by 30%, which compromise availability
as well as the confidentiality and integrity of systems.
35% Malware
infections
30% DDoS
attacks
26% Zero-day
exploits
24% Remote code
execution
To counter these vulnerabilities, organizations should adopt proactive
security measures like a zero trust model. Zero trust enforces stringent
access controls and continuous verification of all network connections,
regardless of their origin. This strategy effectively mitigates the risks posed
by a wide array of attacks that exploit VPN weaknesses, limiting lateral
movement and reinforcing robust access controls.
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 011

VPN MANAGEMENT, PERFORMANCE, AND USER EXPERIENCE
Third-Party VPN Risk
How concerned are you about third parties serving as a potential
The survey underscores significant concern around third-party VPN access backdoor for attackers into your network through their VPN access?
as a network security vulnerability. A notable 92% of respondents express
apprehension about this risk, marking a slight increase from 90% in 2023. This 92% are concerned about third parties
growing recognition highlights the potential for third-party access to serve as serving as a potential backdoor into
an entry point for cyberthreats. their network through VPN access
New insights into VPN vulnerabilities and breaches have further validated
these concerns. Traditional VPNs typically provide extensive network access
post-credential validation, posing risks if third-party vendors’ security 21%
measures are compromised.
30% 23%
18%
8%
Not at all concerned Extremely concerned
Not at all concerned Slightly concerned Moderately concerned
Very concerned Extremely concerned
Organizations should expedite their transition from traditional VPNs to zero trust
architectures. This shift involves implementing systems that rigorously verify access
requests based on identity and context, limiting third-party vendors to specific
resources essential for their tasks.
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 012

Security Issues With
VPN Infrastructure
Overconfidence in
VPN Security
How confident are you in your organization’s ability
to detect and mitigate VPN vulnerabilities exposing
The recent surge in VPN breaches highlights a disconnect between
it to cyberattacks?
perceived security and actual risk. Recent high-severity exploits in
VPN products underscore that even well-prepared organizations might
be underestimating the capabilities of cyber adversaries exploiting
vulnerabilities inherent in VPN technology. A significant 69% (extremely
Extremely
confident + confident) of survey respondents cited high confidence
confident
in their organization’s ability to handle VPN vulnerabilities, which may
not fully align with the escalating threat landscape where sophisticated 33%
actors exploit even minor weaknesses very quickly. Overconfidence can
Confident
be particularly risky given the complexity and persistence of recent VPN
Not
exploits, as shown by incidents involving state-sponsored groups and
36%
confident
cybercriminal gangs targeting unpatched systems for prolonged periods.
4%
Moderately
confident
Slightly
Organizations must recalibrate their security stance by
confident
incorporating rigorous vulnerability assessments, frequent 20%
updates, and comprehensive security awareness training.
7%
Adopting a layered security approach that does not overly
rely on VPNs for comprehensive protection is advisable. This
approach should include advanced monitoring, anomaly
detection, and the integration of zero trust principles.
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 013

SECURITY ISSUES WITH VPN INFRASTRUCTURE
Ransomware
What are you most concerned about as the
Attack Vectors
primary cause of ransomware?
The survey clearly identifies vulnerabilities in externally
14%
exposed assets as the most concerning potential attack vector
of ransomware, noted by 33% of respondents. This points to 26% Vulnerability
widespread recognition of the risks associated with exposed in VDI
Stolen
network services or web applications, which are often the first
identity
point of entry for ransomware attacks. 12%
Stolen identities follows closely at 26%, underscoring the role Nation-state
attack
compromised credentials play in enabling attackers to bypass
security measures and gain access to deliver ransomware
payloads. Concerns about vulnerabilities in virtual desktop
infrastructures (VDI) and nation-state attacks, at 14% and 12%
33% 11%
respectively, highlight the diverse origins of ransomware threats
that organizations must defend against. Scattered Spider (a Vulnerability Scattered
cybercriminal group that uses sophisticated social engineering in externally Spider
exposed assets
tactics, including phishing, multifactor authentication fatigue
4%
attacks, and SIM swapping) concerns 11% of participants.
Others
Organizations should enhance their defenses and identity management protocols. Implementing
comprehensive vulnerability management processes and adopting a zero trust security model can
effectively reduce the risk of ransomware attacks by denying access to network resources and
lateral spread.
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 014

SECURITY ISSUES WITH VPN INFRASTRUCTURE
Ransomware Concerns
How concerned are you about being targeted by
The survey results show 52% of respondents are very or extremely concerned about the ransomware due to unpatched vulnerabilities?
threat of ransomware due to unpatched vulnerabilities. This is justified since unpatched
vulnerabilities remain a primary attack vector for ransomware. Recent analyses show that
a substantial portion of ransomware attacks exploit these vulnerabilities, with notably
severe impact compared to other types of cyberattacks. 91% are concerned about being
targeted by ransomware due
to unpatched vulnerabilities
35
Ransomware groups are growing more sophisticated, with many now using 31%
advanced tactics that can quickly exploit newly discovered vulnerabilities before
30
organizations can patch them. This rapid exploitation cycle greatly shortens the
window for responding to critical vulnerabilities, highlighting the urgent need
for advanced security measures that reduce the attack surface.
25
21% 21%
20
18%
15
9%
10
5
0
Not at all Slightly Moderately Very Extremely
concerned concerned concerned concerned concerned
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 015

SECURITY ISSUES WITH VPN INFRASTRUCTURE
Lateral Movement in
Of all the attacks your organization has experienced,
VPN Attacks
what percentage involved threats spreading laterally after
gaining access through VPN?
Most respondents (54%) report that more than 25% of VPN-related attacks involved
lateral movement, demonstrating significant containment failures at the initial point of
50 46%
compromise. Nearly one-third (32%) experienced lateral movements in more than half of
attacks, indicating major challenges in controlling threat spread once adversaries breach
network defenses.
40
Lateral movement is a significant risk with VPNs, as attackers can obtain broad network
access similar to that of an authenticated user. This enables them to stealthily move
across the network and target sensitive areas.
30
In this way, VPNs can compound risks and expand the scope of an attack beyond its
25%
initial entry point. Resolving this necessitates stringent segmentation, ideally with
user-to-application traffic via a zero trust architecture and continuous monitoring. This 22%
substantially reduces the blast radius of lateral movement by enabling granular access to a
20
smaller set of applications for each individual user, while the rest are rendered invisible.
10 7%
The rising sophistication of attacks exploiting VPN vulnerabilities underscores
the need for a shift toward a zero trust framework. By enforcing strict access
0
controls and continuous verification, zero trust limits unauthorized lateral
<25% 25-50% 51-75% >75%
movements and enhances security across expanding digital landscapes.
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 016

SECURITY ISSUES WITH VPN INFRASTRUCTURE
VPN Security Concerns
Are you concerned about becoming a victim of attack
After M&A
post M&A with your current infrastructure?
Concerns around the impact of mergers and acquisitions (M&A) on existing
VPN infrastructure spotlight the potential vulnerabilities that arise from
organizational changes and the integration of disparate networks.
A substantial 69% of respondents express apprehension about cyberattacks No
Yes
post-M&A, highlighting widespread concern over the security risks
associated with these corporate transformations. This sentiment reflects 69% 31%
a clear understanding that M&A activities can destabilize existing security
frameworks, heightening exposure to cyberthreats.
Transition periods during M&A present unique opportunities for organizations to phase out
antiquated, vulnerable VPN technologies in favor of zero trust frameworks. Specifically, zero trust
architectures enhance security by providing comprehensive segmentation of the environment
between users and applications, between workloads, branch locations, and devices, whether
managed devices, unmanaged devices, IoT, or OT systems. This approach significantly bolsters
security during and after a transition through rigorous verification of all users and devices,
comprehensive segmentation, and strict enforcement of least-privileged access controls.
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 017

Enterprise Adoption of Zero Trust
Progress in Zero Trust Adoption
The survey reflects a strong trend toward adopting zero trust security
frameworks, underscoring the growing recognition of their importance in
enhancing organizational cybersecurity. A significant 31% of respondents are
What are your plans for adopting a zero trust
already implementing zero trust (up from 27% in 2023), indicating a growing
strategy for your organization?
proactive effort to better protect network resources.
Additionally, 27% of organizations plan to implement a zero trust strategy
within the next six months (up from 18% in 2023), and another 20% of
organizations plan to make the shift within the next 12 months, demonstrating
a widespread commitment to transitioning to zero trust in the near future. 31% Already implementing
This confirms that more than three-quarters of survey respondents (78%) a zero trust strategy
recognize the urgency and benefits of zero trust.
However, 17% of respondents are still considering a zero trust strategy without
a specific timeline (down from 23% in 2023), highlighting some hesitancy 27% Planning to implement a
or potential challenges in planning or initiating the transition. Only a small zero trust strategy within
fraction (5%) report no plans to adopt zero trust (down from 8% in 2023), the next 6 months
possibly due to a lack of resources.
20% Planning to implement
An analysis by company size indicates that larger organizations in our survey, a zero trust strategy within
particularly those with over 20,000 employees, are more likely and are the next 12 months
faster to adopt zero trust strategies, with 33% already implementing them. In
contrast, smaller companies with 1,000-5,000 employees show a slightly
lower adoption rate at 29%, suggesting that scale and resource availability may 17% Considering a zero trust
influence the pace and scope of zero trust integration. strategy but no specific timeline
5%
No plans to adopt a
Organizations still on the fence or planning to adopt zero trust
zero trust strategy
should start by assessing their current security posture and network
architecture to identify specific needs and potential challenges.
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 018

ENTERPRISE ADOPTION OF ZERO TRUST
No Zero Trust Security Advancing from VPN to
Through VPN Zero Trust Network Access
The survey results reflect a significant divide in beliefs about the compatibility of VPNs The survey results show that most organizations are making a strategic shift, with 53%
with zero trust security frameworks. Most (62%) believe that VPNs are fundamentally of respondents citing plans to replace their existing VPN solutions with ZTNA solutions
“anti-zero trust,” confirming that traditional VPN architectures do not align with the in the near future. ZTNA offers a more flexible and secure approach by enforcing policies
principles of zero trust. Conversely, 38% of respondents view VPNs, especially cloud- based on user context, location, and device security, without assuming trust based on
based platforms, as compatible with zero trust architectures. network location. This contrasts with traditional VPNs, which generally grant broad
access to a network, creating security vulnerabilities.
While this perspective may stem from VPN vendors claiming that their cloud-based
solutions align with zero trust principles, it’s important to scrutinize these assertions For the 53% of organizations moving toward ZTNA, it is crucial to ensure a smooth
critically. Simply hosting a VPN service in the cloud, for example, does not automatically transition by planning comprehensive risk assessments, updating access policies, and
confer zero trust attributes. Zero trust security requires more than just a secure hosting educating users about new protocols. Meanwhile, the 47% not yet planning to switch
environment; it mandates a fundamental shift from perimeter-based defenses to a model should evaluate their current security challenges and consider whether ZTNA could
where security is dynamic, granular, and context-based. address these more effectively than VPN.
Do you believe you can achieve zero trust security with VPNs? Do you have plans to replace your current VPN
solution with a Zero Trust Network Access (ZTNA)
No, VPNs solution in the near future?
are anti 62%
zero trust
Yes, VPN in
the cloud is
38%
zero trust
architecture
0 10 20 30 40 50 60 70 80
53%
True zero trust security involves continuously validating all users and devices, applying
least-privileged access, and segmenting traffic to prevent lateral movement—features
have plans to replace VPN with a ZTNA
that traditional VPNs, even cloud-based ones, do not provide. Therefore, organizations solution in the near future
must confirm that any claimed “zero trust” VPN actually incorporates these core
principles, rather than relying solely on marketing promises.
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 019

ENTERPRISE ADOPTION OF ZERO TRUST
Why Zero Trust is More Secure Than VPN
Architecturally, zero trust and ZTNA are more secure than traditional VPNs for several time-consuming tasks like user provisioning, routing table management, connectivity
reasons, primarily due to a robust security framework that never inherently places troubleshooting, patching, monitoring, and performance optimization.
trust in any single connection. Traditional VPN-based architectures are susceptible to a
single point of failure. When a VPN or device is compromised (such as through a new In a zero trust architecture, no single connection is ever trusted. Users connect directly
CVE), threat actors can exploit the trust inherent in a flat network to gain access to the to applications—never to the underlying network. Moreover, every connection
entire network, move laterally, steal data, and deploy ransomware. This is why security is automatically terminated, regardless of origin, before being verified by seven
practitioners are increasingly concerned about the security risks of VPN. layers of zero trust security controls. Zero trust architecture allows organizations to
comprehensively segment their environments with granular access—from users to
On-premises and cloud-delivered VPNs present similar security vulnerabilities. applications, between workloads, between branch locations, and between devices,
Additionally, VPNs introduce complexity, resulting in unnecessary overhead and including IoT and OT devices.
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 020

ENTERPRISE ADOPTION OF ZERO TRUST
Key Differences and Advantages
Significantly Reduced Attack Surface Granular Access and Segmentation
A zero trust architecture enables inside-out connectivity By dividing network resources into separate segments—
that hides critical assets, applications, servers, and more between users and apps, between workloads, between
from the public internet, while removing the need for devices—zero trust isolates potential breaches to
vulnerable assets like VPNs and firewalls. This allows smaller zones, greatly reducing the impact of an attack.
enterprises to provide hybrid connectivity for their While organizations often try to segment their network
workforces while greatly shrinking their attack surface. environments, it’s an operationally complex and costly
In contrast, VPN- and firewall-based architectures process that, in practice, often remains incomplete,
require enterprises to expand the attack surface to requires hundreds of discrete firewall rules, and exposes
accommodate increased connectivity. broader network areas to authenticated users.
Continuous Verification Empowering Today’s Hybrid Workforce
Zero trust models enforce continuous security verification Zero trust makes it possible to easily extend lightning-
of credentials and security posture before granting fast access to private applications across remote users in
access to resources, making it much more difficult for addition to HQ, branch offices, and third-party partners.
unauthorized entities to gain and maintain access to
sensitive information and systems. Meanwhile, with VPNs, Improved User Experience and Reduced Complexity
Zero trust enhances user experiences by eliminating
the user or device often has extensive access to network
the need for all remote traffic to route through a central
resources once access is granted.
network point, a common performance bottleneck
Least-Privileged Access with VPN. This architecture is better able to handle the
Zero trust principles enforce least-privileged access scaling requirements of modern networks that include
policies, ensuring that users and devices only have IoT and BYOD policies. Additionally, zero trust reduces
access to the resources necessary for their specific roles. management overhead by automating security controls
This minimizes the risk of internal threats and lateral and simplifying the enforcement of security policies
movement within a network, which are common across the network.
vulnerabilities in VPN setups.
These architectural advantages make zero trust a compelling alternative to traditional VPNs, particularly in today’s
increasingly sophisticated and distributed threat landscape. For organizations looking to bolster their cybersecurity
defenses, adopting a zero trust approach provides a more robust, flexible, and scalable security infrastructure.
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 021

VPN Predictions for 2024
and Beyond
1 Severe VPN vulnerabilities and exploits will increase 4 Password-spraying attacks on VPNs will
continue to grow
Given the frequency, severity, and scale of VPN vulnerabilities disclosed in the past
year, enterprises should expect this trend to continue. Threat actors and security
Attackers will increasingly find ways to exploit weak password management
researchers are aware of the heightened risk of high-severity vulnerabilities in VPN
practices and unused default VPN connection profiles through password-spraying
products. In turn, they are actively hunting for more, making it likely that additional
attacks. In these attacks, threat actors try the same password across many
CVEs will be found in the coming months and years.
VPN accounts until they successfully log in, gaining unauthorized access. With
numerous recent high-profile VPN breaches effectively leveraging this technique,
2 High-profile attacks caused by VPN enterprises should expect similar attacks to persist.
will take the spotlight
5 Enterprise spend will shift away from VPN toward zero
Closely related to our first prediction, we will see more large organizations disclose
trust connectivity
breaches that result from exploited VPN vulnerabilities. In part due to the new SEC
regulation guidelines which require public companies to disclose details around
While VPN has long enabled remote connectivity for enterprises, the technology’s
breaches with a material impact. As we have seen, threat actors consistently create
consistent and growing security challenges will make it more challenging to justify
backdoors in target environments when VPN vulnerabilities occur, only to exploit
long-term spending. As enterprises cement a consensus around zero trust as
them at later dates, even after these vulnerabilities have been patched. As the year
the preferred architecture for security and connectivity, enterprise budgets will
progresses, more of these will start to be disclosed in public SEC filings and hit
continue to shift toward zero trust initiatives to secure the remote workforce.
the news.
A surge in AI-powered VPN offerings will raise
3
security and privacy concerns
Amid ongoing advancements in AI, AI-powered VPN solutions will flood the
market. However, enterprises should evaluate these offerings with caution.
Although they will promise enhanced performance, the integration of AI will
amplify security risks and increase opportunities for attackers to exploit VPN
vulnerabilities. In addition, privacy concerns will arise from extensive data analysis
that increases the risk of sensitive information being exposed.
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 022

How Zscaler Enables VPN Replacement
and Zero Trust Transformation
Traditional firewalls and VPNs create a massive attack
surface that lets attackers see and exploit exposed
resources. By putting users on the network and letting
Zero Trust Architecture
them access any application it hosts, these legacy
approaches give attackers easy access to sensitive data.
They make it challenging and time-consuming to safely
provide access or share resources with third-party
Data
vendors, contractors, and agencies. Beyond that, they SaaS Internet Cloud Center
drive up costs and complexity, and are too slow to serve
today’s hybrid workforce.
The Zscaler Zero Trust Exchange™ platform, the world’s
largest inline security cloud, securely connects users,
workloads, IoT/OT, and B2B partners without extending
network access.
Zscaler Private Access™ (ZPA™), an essential part
of the Zero Trust Exchange, provides direct access
to private applications hidden behind the Zero Trust
Exchange, minimizing the attack surface, enabling
granular 1:1 user-to-app segmentation, eliminating
lateral movement, and delivering private app protection
and inline traffic inspection while stopping zero-day
threats—elevating your security posture. A cloud native
service, ZPA can be deployed in just hours to replace
legacy remote access tools like VPNs and VDIs.
Remote Branches B2B IoT/OT
Workers and Factories Partners Systems
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 023

HOW ZSCALER ENABLES VPN REPLACEMENT AND ZERO TRUST TRANSFORMATION
Zero Trust Networking
ZPA enables granular, segmented access with inside-out connectivity to private
applications and workloads. Moreover, ZPA includes a comprehensive set of
access control services, including AI-powered user-to-app segmentation—
with automated recommendations for user access policies and application
segments—workload-to-workload segmentation, privileged remote access,
private service edge, browser access, and more.
Cyberthreat Protection
ZPA delivers advanced cyber protection capabilities to secure your organization.
These include app protection capabilities that use inline security inspection to
stop the most prevalent application attacks and zero-day vulnerabilities, as well
as deception technology that lures attackers with decoy apps and makes it easy
to detect sophisticated threats.
Data Protection
ZPA provides holistic data protection and stops data loss across all channels
with web Data Loss Prevention (DLP), endpoint DLP, and browser isolation that
prevents data leakage for vulnerable users and BYOD endpoints.
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 024

Best Practices to Counter VPN Risks
• Minimize the attack surface: Provide direct access to
applications, ensuring that both apps and users are invisible to
the internet, effectively preventing attackers from discovering
and exploiting them for initial access.
• Prevent initial compromise: Inspect all traffic inline to
automatically stop zero-day exploits, malware, and other
sophisticated threats.
• Block unauthorized access: Use strong multifactor
authentication (MFA) such as one-time passwords or tokens,
biometrics, or FIDO2 credentials to validate user access
requests. Conversely, weak MFA often uses approaches like
password reset questions.
• Enforce least-privileged access: Restrict permissions for users,
traffic, systems, and applications based on identity and context,
ensuring only authorized users can access approved resources
(providing additional security in cases of MFA compromise or
credential theft).
• Eliminate lateral movement: Connect users directly to apps, not
the network, to limit the blast radius of a potential incident and
mitigate the risk of lateral threat movement.
• Shut down compromised users and insider threats: Enable
inline inspection and monitoring to detect compromised users
with access to your network, private applications, and data.
• Stop data loss: Inspect data in motion and data at rest to stop
active data theft during an attack.
• Deploy active defenses: Leverage deception technology with
decoys and perform daily threat hunting to derail and capture
attacks in real time.
• Test your security posture: Get regular third-party risk
assessments and conduct purple team activities to identify and
harden the gaps in your security program. Request that your
service providers and technology partners do the same and
share the results of these reports with your security team.
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 025

Methodology and Demographics
This report is based on the results of a comprehensive
online survey of 647 IT and cybersecurity professionals,
conducted in April 2024, to identify the latest enterprise  Career
adoption trends, challenges, gaps, and solution  Level 31% 18% 13% 11% 10% 9% 8%
preferences related to VPN risk. Respondents range
|     | Manager/Supervisor | Director | CTO, CIO, CISO, CMO, CFO, COO |     |     | Specialist/Analyst | Founder/CEO/President | Consultant | Other |     |
| --- | ------------------ | -------- | ----------------------------- | --- | --- | ------------------ | --------------------- | ---------- | ----- | --- |
from technical executives to IT security practitioners,
representing a balanced cross-section of organizations
| Department |     | 32% |     |     | 25% |     | 15% | 8%  | 8% 12% |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- |
of varying sizes across multiple industries.
|     | IT Security | IT Operations | Engineering | Network | Infrastructure |     | Other |     |     |     |
| --- | ----------- | ------------- | ----------- | ------- | -------------- | --- | ----- | --- | --- | --- |
Primary
|     |     | 32% |     |     | 14% | 12% | 11% | 10% | 7% 6% | 8%  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
Role
Reuse of content - We encourage the
|     | IT Manager/ Director   | Systems Administrator |       | CSO, CISO or VP of Security |     | Security Analyst | Security Manager or Director |     |     |     |
| --- | ---------------------- | --------------------- | ----- | --------------------------- | --- | ---------------- | ---------------------------- | --- | --- | --- |
|     | Security Administrator | CIO                   | Other |                             |     |                  |                              |     |     |     |
reuse of data, charts, and text published
in this report under the terms of the  Company
|     |     | 39% |     |     |     | 31% |     |     | 30% |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Size
Creative Commons Attribution 4.0
International License. You’re free to share
|     | 1,000 - 5,000 | 5,000 - 20,000 |     | +20,000 |     |     |     |     |     |     |
| --- | ------------- | -------------- | --- | ------- | --- | --- | --- | --- | --- | --- |
and make commercial use of this work
as long as you attribute the report as
| Industry | 14% | 11% | 10% |     | 10% | 8% 7% | 6% 6% |     | 28% |     |
| -------- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- | --- |
stipulated in the terms of the license. For
example: “Zscaler ThreatLabz 2024 VPN
|     | Healthcare, Pharmaceuticals & Biotech |     | Computers & Electronics |     | Government | Financial Services | Software & Internet  |     |     |     |
| --- | ------------------------------------- | --- | ----------------------- | --- | ---------- | ------------------ | -------------------- | --- | --- | --- |
Risk Report with Cybersecurity Insiders.” Telecommunications Education & Research Professional Services Other
|     | 0   |     | 20  |     | 40  |     | 60  | 80  |     | 100 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
026
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT

About Zscaler About Cybersecurity
Insiders
Zscaler accelerates digital transformation so that customers can be
more agile, efficient, resilient, and secure. The Zscaler Zero Trust
Exchange™ protects thousands of customers from cyberattacks and Cybersecurity Insiders brings together 600,000+ IT security
data loss by securely connecting users, devices, and applications in professionals and world-class technology vendors to facilitate smart
any location. Distributed across more than 150 data centers globally, problem solving and collaboration in tackling today’s most critical
the SASE–based Zero Trust Exchange is the world’s largest inline cybersecurity challenges.
cloud security platform. To learn more, visit www.zscaler.com.
Our approach focuses on creating and curating unique content
that educates and informs cybersecurity professionals about the
latest cybersecurity trends, solutions, and best practices. From
About ThreatLabz
comprehensive research studies and unbiased product reviews to
practical e-guides, engaging webinars, and educational articles - we
are committed to providing resources that provide evidence-based
ThreatLabz is the security research arm of Zscaler. This world- answers to today’s complex cybersecurity challenges.
class team is responsible for hunting new threats and ensuring
that the thousands of organizations using the global Zscaler Contact us today to learn how Cybersecurity Insiders can help you
platform are always protected. In addition to malware research and stand out in a crowded market and boost demand, brand visibility,
behavioral analysis, team members are involved in the research and thought leadership presence.
and development of new prototype modules for advanced threat
protection on the Zscaler platform, and regularly conduct internal Email us at info@cybersecurity-insiders.com or
security audits to ensure that Zscaler products and infrastructure visit cybersecurity-insiders.com.
meet security compliance standards. ThreatLabz regularly publishes
in-depth analyses of new and emerging threats on its portal,
research.zscaler.com.
©2024 Zscaler, Inc. All rights reserved. ZSCALER THREATLABZ 2024 VPN RISK REPORT 027

Experience your world, secured.
About Zscaler
Zscaler (NASDAQ: ZS) accelerates digital transformation so that customers can be more agile, efficient, resilient, and secure. The © 2024 Zscaler, Inc. All rights reserved. Zscaler™, Zero Trust Exchange™, Zscaler
Zscaler Zero Trust Exchange™ protects thousands of customers from cyberattacks and data loss by securely connecting users, Internet Access™, ZIA™, Zscaler Private Access™, ZPA™ and other trademarks listed
at zscaler.com/legal/trademarks are either (i) registered trademarks or service marks
devices, and applications in any location. Distributed across more than 150 data centers globally, the SASE–based Zero Trust or (ii) trademarks or service marks of Zscaler, Inc. in the United States and/or other
Exchange is the world’s largest inline cloud security platform. To learn more, visit www.zscaler.com. countries. Any other trademarks are the properties of their respective owners.
+1 408.533.0288 Zscaler, Inc. (HQ) • 120 Holger Way • San Jose, CA 95134 zscaler.com

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-08-28", "model": "gemini-3.5-flash-lite"} -->
