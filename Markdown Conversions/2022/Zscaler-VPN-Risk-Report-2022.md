2022
VPN RISK
REPORT

TABLE OF CONTENTS
Overview 3
Remote Access Environment 4
State of VPN 8
VPN Vulnerabilities and Risk 11
Future of Remote Access 15
Key Takeaways 19
Methodology & Demographics 20

OVERVIEW
Organizations have relied on VPNs for decades to deliver secure remote access to employees. During
the COVID-19 pandemic, companies were forced to rapidly shift to remote work to stay productive
and profitable. However, using VPN for remote access puts those organizations at significant risk, as
traditional VPN architectures often trust too readily and excessively. Bad actors can exploit the VPN
attack surface to infiltrate the network and launch ransomware, phishing attacks, denial of service,
and other means of exfiltrating critical business data. As reported by countless news articles about
VPN exploits, almost 500 known VPN vulnerabilities are listed on the CVE database.
This 2022 VPN Risk Report surveyed 351 cybersecurity professionals to provide fresh insight into the
state of remote access and VPN within the enterprise, the rise in VPN vulnerabilities, and the role that
zero trust plays in enabling the next generation of secure access.
KEY FINDINGS INCLUDE:
• 78% of organizations are concerned about ransomware attacks
• 44% witnessed an increase in exploits targeting their VPN since adopting remote work
• 65% of companies are considering adopting VPN alternatives
• 80% of companies are in the process of adopting zero trust in 2022
• 68% say their focus on remote work accelerated the priority of zero trust projects,
up from 59% in 2021
Many thanks to Zscaler for supporting this important research project.
We hope this report is informative and helpful as you continue your efforts to protect your IT
environments.
Thank you,
Holger Schulze
Holger Schulze
CEO and Founder
Cybersecurity Insiders
2022 VPN RISK REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 3

REMOTE ACCESS
ENVIRONMENT
2022 VPN RISK REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 4

SECURE ACCESS FOR WHO...
While the shift to remote work has already accelerated the adoption of remote access solutions, the
latest survey found that this trend has only continued in 2021 and 2022. Now 95% of organizations
are leveraging a VPN service for secure remote access (up from 93% last year). So let’s dive into
more detail about the current state of VPN and drivers for remote access.
Are you currently using a VPN service within your organization?
95% 5%
YES NO
When it comes to requiring secure access to business apps, employees continue to take priority. Sixty-
nine percent of organizations are making employee access their first priority. However, the relative
priority has shifted compared to the previous year, as organizations are increasingly providing secure
access to customers (21%, up seven percentage points compared to last year), along with partners, and
contractors (5%, up two percentage points - each compared to last year).
When requiring secure access to business 6appl1icat%ions, whicohf g crooump tpakaens ipersiority?
have 3+ VPN
gateways
38%
22%
69% 21% 5% 5% 57% North America
83%
14% 54%
3% 11% 12% Europe
Asia
Employees Customers Contractors Partners
None 1 2 3 4 5+
South America
29% Africa
39%
30% Australia
2022 VPN RISK REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 5
74%
Data center
70%
27% Combination
of both Private cloud 49%
Majority
corporate 45%
Public cloud (Azure)
device
3% Majority 44%
Public cloud (AWS)
BYOD
22%
Public cloud (Google)

FOR WHAT...
Remote work in today’s hybrid and highly distributed work environments includes more than
employees. Other important stake 6 h 9 ol % ders with varying 2 1 ne % eds of secure acc5e%ss include custom5e%rs, 57% North America
83%
54%
partners and contractors - notably larger organizations with more than 2,000 employees are more
Europe
likely to extend secure access to those groups. Security teams must consider: who is accessing
Asia
their applications, from what deEvmicepsl,o fyoer ewshat purpCouses taonmd ferorsm wherCe?o ntractors Partners
South America
Organizations have a variety of device choices and policies when enabling secure access to remote
29% Africa
employees. Seventy percent of organizations report they offer predominantly corporate devices. A
39%
small percentage have majority BYOD/personal devices (3%). Enforcing security measures on BYOD 30% Australia
devices makes device security and access control more challenging, especially in remote work scenarios.
What devices are workers using to connect to business resources and applications?
74%
Data center
70%
27% Combination
of both Private cloud 49%
Majority
corporate Public cloud (Azure) 45%
device
3% Majority 44%
Public cloud (AWS)
BYOD
22%
Public cloud (Google)
2022 VPN RISK REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 6

... AND WHERE
Organizations over 2,000 employees are more likely to have an international footprint. Eighty-three
percent report that their remote workers are connecting from North America, 57% have remote workers
accessing from Asia, and 54% from Europe. With users distributed across the globe, supporting secure
remote work can become a greater challenge, as different regions have varying security standards,
availability, compliance policies, etc.
From where are your remote workers connecting?
|     | 69% | 21% |     | 5%  |     | 5%  |     |     |     |     | 57% |     | North America             |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- |
83%
54%
Europe
Asia
|     | Employees | Customers |     | Contractors |     | Partners |     |     |     |     |     |     |     |
| --- | --------- | --------- | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
South America
29%
Africa
39%
|     |     |     |     |     |     |     |     |     |     |     |     | 30% | Australia                 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- |
|     |     |     | 69% | 21% |     | 5%  | 5%  |     |     |     |     | 57% | North America             |
83%
54%
Europe
Asia
|     |     |     | Employees | Customers |     | Contractors | Partners |     |     |     |     |     |     |
| --- | --- | --- | --------- | --------- | --- | ----------- | -------- | --- | --- | --- | --- | --- | --- |
South America
Consistent enforcement of security policies is m2o9r%e challenging in heterogeneAofriucas environments. In our
39%
survey, organizations report that their applications are typicall3y0 %run in data cAeunsttrealrias  (74%), followed by
74%
private clouds (49%), anDda ptuab clice cnloteudrs (45% Azure/44% AWS/22% Google Cloud).
70%
|     |     |     | 27% | Combination |     |     |                   |     |             |                                       |     |     |     |
| --- | --- | --- | --- | ----------- | --- | --- | ----------------- | --- | ----------- | ------------------------------------- | --- | --- | --- |
|     |     |     |     | of both     |     |     |                   |     | P r i v a   | t e   c lo u d                        | 49% |     |     |
|     |     |     |     |             |     |     | Where are your pr |     | iv a t e  a | p pl i ca ti on s currently running?  |     |     |     |
Majority
| corporate |     |     |     |     |     |     |     | Public cloud (Azure) |     |     | 45% |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- |
device
74%
Data center
70%
|     |     |     | 3%  | Majority |                |         |     |                    |     |               | 44% |     |     |
| --- | --- | --- | --- | -------- | -------------- | ------- | --- | ------------------ | --- | ------------- | --- | --- | --- |
|     |     |     |     |          | 27%Combination |         |     | Public cloud (AWS) |     |               |     |     |     |
|     |     |     |     | BYOD     |                | of both |     |                    |     | Private cloud |     | 49% |     |
Majority
22%
Public cloud (Google)
|     | corporate |     |     |     |     |     |     |     | Public cloud (Azure) |     |     | 45% |     |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- |
device
|     |     |     |     |     | 3%  | Majority |     |     | Public cloud (AWS) |     |     | 44% |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | ------------------ | --- | --- | --- | --- |
BYOD
22%
Public cloud (Google)
Other 1%
7
2022 VPN RISK REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved.     |

STATE OF VPN
2022 VPN RISK REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 8

95% 5%
VPN USAGE AND NUMBER OF GATEWAYS
NO
YES
The size and complexity of an organization typically drives the complexity of remote access infrastructure
and management proportionally. A majority of companies in our survey (61%) have three or more VPN
gateways – over a third of companies (38%) have even more than five.
Each gateway requires a stack of appliances, often including the VPN (RAS), Internal Firewall, Internal Load
balancer, Global Load balancer, DDoS, External Firewall, etc. The more gateways an organization has,
the more expensive secure remote access becomes and the more complicated it is for IT to administer
and manage.
How many different inbound VPN gateways do you have globally?
61% of companies
have 3+ VPN
gateways
38%
22%
14%
3% 12%
11%
None 1 2 3 4 5+
2022 VPN RISK REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 9

TOP VPN CHALLENGES
Cybersecurity professionals in our survey confirm that remote access solutions are not without challenge,
especially for larger organizations. Current VPN solutions require employee and third-party access to
the corporate network (26%) is the biggest challenge as reported by organizations. This obstacle is
followed by the high cost of security appliances and infrastructure (23%) and lack of visibility into user
activity (18%).
What is your biggest challenge with your current remote access solution?
|     |                 | 26%           |                | 23% | 18%             |     |
| --- | --------------- | ------------- | -------------- | --- | --------------- | --- |
|     | Requires giving |               | High costs     |     | Lack of         |     |
|     | employees and   |               | of security    |     | visibility into |     |
|     |                 | third-parties | appliances/    |     | user activity   |     |
|     |                 | access to the | infrastructure |     |                 |     |
corporate network
|                             |                 | 14% |                   | 12%        |                        | 7%  |
| --------------------------- | --------------- | --- | ----------------- | ---------- | ---------------------- | --- |
| Complexity of managing      |                 |     |                   | Poor user  | Inability to scale to  |     |
|                             | existing remote |     | experience due to |            | meet user demand       |     |
| access across public cloud  |                 |     | backhauls to VPN  |            |                        |     |
|                             | environments    |     |                   | gateways   |                        |     |
10
2022 VPN RISK REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved.     |

VPN VULNERABILITIES
AND RISK
2022 VPN RISK REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 11

INCREASE IN VPN THREATS
An increase in attacks and remote work has resulted in a sharp spike in the popularity of VPN-targeted
attacks amongst cybercriminals as they seek to gain unauthorized access to network resources exposed
to the internet. In fact, 97% of companies know that their VPNs are vulnerable to cyberattacks and
exploits yet still leverage this technology while aware of the risk.
Are you aware that cybercriminals are targeting VPNs to gain access to network resources through
exploits such as remote code exploits, Windows servers, ransomware, and social engineering attacks?
97% 3%
YES NO
When asked about the most concerning internet-based attacks, organizations prioritize ransomware
66%
(78%), followed by social e9ng7in%eering (70%) and malware 3(66%%) as the most critical attack vectors.
Breaches show that it only takes one infected device or stolen credential to put an entire network at risk,
which is why cybercriminals are targeting users by accessing through a VPN.
70%YES MalwareNO
49%
What type of internet-based attacks are you most concerned about?
Social
engineering
66% Web applications
70% Malware
49%
Social
engineering
Web applications
78% 45%
Ransomware DDoS attacks
78% 45%
Ransomware DDoS attacks
Other 3%
2022 VPN RISK REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 12

IMPACT OF REMOTE AND HYBRID
WORK ON THREATS
Forty-four percent of cybersecurity professionals have witnessed an increase in exploits targeting their
business’s VPN since the shift to remote and hybrid work.
Have you witnessed an increase in exploits targeting your business’s VPN since your employees have
been working remotely?
22%
Unsure
34% 44%
No Yes
2022 VPN RISK REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 13

CONCERNS OVER VPN SECURITY
Seventy-one percent of companies are concerned that VPN may jeopardize the ability to keep their IT
environments secure. This begs the question: if your secure remote access solution doesn’t deliver the
required level of security, should the remote access strategy be adjusted?
How concerned are you that VPN may jeopardize your ability to keep your environment secure?
71% are concerned that VPN
may jeopardize the ability to
keep the environment secure.
51%
29%
20%
Not concerned Very concerned
Not concerned Concerned Very concerned
2022 VPN RISK REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 14

FUTURE OF
REMOTE ACCESS
2022 VPN RISK REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 15

ACCELERATION OF ZERO TRUST ADOPTION
Zero Trust Network Access (ZTNA) and Zero Trust Architectures (ZTA) have rapidly gained traction in
recent years. With the increase of mobile and remote workers, zero trust adoption has become a priority
for many organizations, with 80% of companies actively planning or implementing a zero trust model.
Is adopting a zero trust model a priority for your organization?
80%
YES, we have plans 41% 80%
but areY iEn Sth, ew eea rhlya pvhea pselasns
41%
but are in the early phases
of companies are
YES, we have already begun to 39%
adopting or have
roll out zero trust solutions of companies are
YES, we have already begun to 39% adopted zero trust
adopting or have
roll out zero trust solutions
NO, we have no plans to
20% adopted zero trust
adopt a zero trust model yet
NO, we have no plans to
20%
adopt a zero trust model yet
The survey confirms that a majority (68%) of companies have been accelerating their zero trust projects
since the recent shift to remote and hybrid work.
Has the focus on remote work accelerated the priority of zero trust projects at your organization?
68% 32%
YES NO
68% 32%
YES NO
2022 VPN RISK REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 16

VPN ALTERNATIVES
Not surprisingly, with nearly three out of four businesses concerned with VPN security, a majority of
organizations (65%) are now considering remote access alternatives to the traditional VPN.
Have you considered remote access alternatives to traditional VPN?
65%
35%
YES NO
2022 VPN RISK REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 17

REMOTE ACCESS MOVING FORWARD
The continued shift to zero trust and working from anywhere has been a catalyst to changing how
organizations protect remote access. When asked about their outlook for remote access, 78% of
organizations say their future workforce will be hybrid, providing greater flexibility for users to work
remotely or in the office.
Fast forward to 2023, what does remote access look like at your company?
78%
15%
7%
Employees have Employees are Employees have
greater flexibility now fully remote returned to
to work remote solely working
during the week in the office
2022 VPN RISK REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 18

KEY TAKEAWAYS
While VPN has benefited from 30 years in the spotlight, the increase in VPN-targeted attacks, along
with the continued shift towards mobility and the cloud, has impressed on organizations the need for
change in their secure remote access strategy – one built upon a foundation of zero trust principles.
In conclusion, here are the key takeaways:
With remote work expanding, users are everywhere, accessing
apps from any device, and are accessing apps both in the data
center and cloud.
VPNs are increasingly risky as social engineering, ransomware,
and malware attacks continue to advance, exposing the
business to greater risk.
Businesses are concerned about VPN’s level of security and are
looking to adopt a modern remote access approach, namely a
zero trust model.
The majority of organizations have prioritized plans to adopt a
zero trust strategy. With many businesses prepared to enable a
hybrid workforce and workplace flexibility, adopting zero trust
becomes critical.
Is VPN currently opening up your business to risk?
Get a free risk assessment and discover your network’s attack surface before
threat actors can.
UNCOVER YOUR ATTACK SURFACE
2022 VPN RISK REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 19

METHODOLOGY & DEMOGRAPHICS
This report is based on the results of a comprehensive online survey of 351 IT and cybersecurity
professionals, conducted in June 2022 to identify the latest enterprise adoption trends, challenges,
gaps, and solution preferences related to VPN risk. The respondents range from technical executives to
IT security practitioners, representing a balanced cross-section of organizations of varying sizes across
multiple industries.
CAREER LEVEL
|     | 27% |     | 24% |     | 16% | 11% 7% | 6% 4% 5% |
| --- | --- | --- | --- | --- | --- | ------ | -------- |
Specialist            Director           Manager/Supervisor           CTO, CIO, CISO, CMO, CFO, COO         Vice President              Consultant
Founder/CEO/President             Other
COMPANY SIZE
|                       | 29% |                        | 28%               |     |     | 43% |     |
| --------------------- | --- | ---------------------- | ----------------- | --- | --- | --- | --- |
| 2,000-5,000 employees |     | 5,001-20,000 employees | >20,000 employees |     |     |     |     |
INDUSTRY
| 19% |     | 16% | 12% | 8%  | 8% 7% | 5% 4% 4% | 17% |
| --- | --- | --- | --- | --- | ----- | -------- | --- |
Healthcare, Pharmaceuticals & Biotech          Financial Services         Manufacturing           Government          Software & Internet
Education & Research            Professional Services          Computer & Electronics         Telecommunications            Other
20
2022 VPN RISK REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved.     |

About Zscaler
Zscaler (NASDAQ: ZS) accelerates digital transformation so that
customers can be more agile, efficient, resilient, and secure. The
Zscaler Zero Trust Exchange protects thousands of customers from
cyberattacks and data loss by securely connecting users, devices,
and applications in any location. Distributed across more than 150
data centers globally, the SASE-based Zero Trust Exchange is the
world’s largest inline cloud security platform. Learn more at zscaler.
com or follow us on Twitter @zscaler.
zscaler.com
©2022 Zscaler, Inc. All rights reserved. Zscaler™is either (i) a registered trademark or service mark or (ii) a
trademark or service mark of Zscaler, Inc. in the United States and/or other countries. Any other trademarks
are the properties of their respective owners.

Cybersecurity Insiders is a 500,000+ member online community for
information security professionals, bringing together the best minds
dedicated to advancing cybersecurity and protecting organizations across
all industries, company sizes, and security roles.
We provide cybersecurity marketers with unique marketing opportunities to
reach this qualified audience and deliver fact-based, third-party validation
thought leadership content, demand-generation programs, and brand
visibility in the cybersecurity market.
For more information please visit
www.cybersecurity-insiders.com
Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. Data can be reproduced
or referenced as long as it is sourced and linked to www.cybersecurity-insiders.com.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-08-28", "model": "gemini-3.5-flash-lite"} -->
