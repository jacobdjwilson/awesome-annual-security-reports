2021
THREAT
HUNTING
REPORT

INTRODUCTION
Threat hunting continues to evolve as an innovative cybersecurity tactic that focuses on proactively
detecting and isolating Advanced Persistent Threats (APTs) that might otherwise go undetected
by traditional, reactive security technologies.
While many SOCs struggle to cope with the rising security threat workload, more organizations
are adopting threat hunting as part of their security operations. They discover that proactive
threat hunting can reduce the risk and impact of threats while improving defenses against
new attacks.
The 2021 Threat Hunting Report explores the challenges, technology preferences, and benefits
of threat hunting to gain deeper insights into the maturity and evolution of the security practice.
Key findings include:
• More than half of respondents (51%) identified reducing exposure to internal threats as their
top threat hunting goal. This is followed by reducing the number of breaches and infections
(45%) and reducing the attack surface (43%).
• The most common attacks that organizations proactively discover include malware (76%),
phishing (71%), network intrusions (46%), and ransomware (41%).
• The top data sources that organizations collect and analyze for threat hunting purposes
include endpoint activities (72%), system logs (71%), and firewall traffic (69%).
• 68% of organizations at least occasionally develop insights into adversary infrastructures as
part of their threat hunting activities. However, only 21% of organizations are fully focused on
gaining these insights.
• Organizations need to collect data from multiple sources to add context to their threat
hunting activities. The most common data sources include external threat intelligence feeds
(56%), user behavior data (56%), and file activity data.
We would like to thank LookingGlass for supporting this important research.
We hope you enjoy the report.
Thank you,
Holger Schulze
Holger Schulze
CEO and Founder
Cybersecurity Insiders
2
2021 THREAT HUNTING REPORT All Rights Reserved. ©2021 Cybersecurity Insiders

THREAT HUNTING GOALS
More than half of respondents (51%) identified reducing exposure to internal threats as their top
threat hunting goal. This is followed by reducing the number of breaches and infections (45%) and
reducing the attack surface (43%).
What are the primary goals of your organization’s threat hunting program?
| 51%             |     | 45%           |     | 43% |
| --------------- | --- | ------------- | --- | --- |
| Reduce exposure |     | Reduce number |     |     |
Reduce attack
| to internal threats |     | of breaches and |     | surface |
| ------------------- | --- | --------------- | --- | ------- |
infections
|     | 41%              |                     | 41% | 40%              |
| --- | ---------------- | ------------------- | --- | ---------------- |
|     | Reduce time to   | Reduce exposure     |     | Improve speed    |
|     | containment      | to external threats |     | and accuracy of  |
|     | (prevent spread) |                     |     | threat response  |
Reduce dwell time from infection to detection 39%  |   Optimize resources spent on threat response 31%  |  Other 7%
3
2021 THREAT HUNTING REPORT All Rights Reserved.  ©2021  Cybersecurity Insiders

MOST COMMON ATTACKS
The most common attacks that organizations proactively discover include malware (76%), phishing
(71%), network intrusions (46%), and ransomware (41%).
What are the most common attacks proactively discovered through threat hunting?
76% 71%
Malware Phishing
46% 41%
Network intrusion Ransomware
Supply chain compromise 2% | Other 2%
4
2021 THREAT HUNTING REPORT All Rights Reserved. ©2021 Cybersecurity Insiders

DATA COLLECTION SOURCES
The top data sources that organizations collect and analyze for threat hunting purposes include
endpoint activities (72%), system logs (71%), and firewall traffic (69%).
What kind(s) of data does your security organization collect and analyze?
| 72%             |          |                | 71%         |         | 69%                 |         |
| --------------- | -------- | -------------- | ----------- | ------- | ------------------- | ------- |
|                 | Endpoint |                | System logs |         | Firewall/IPS        |         |
|                 | activity |                |             |         | denied traffic      |         |
| 64%             |          | 61%            |             | 56%     |                     | 54%     |
| Firewall/IPS    |          | Web and email  |             | Network | Threat intelligence |         |
| allowed traffic |          | filter traffic |             | traffic |                     | sources |
Active directory 53%  |   DNS traffic 52%  |   Server traffic 47%   |  Web proxy logs 45%  |   User behavior 39%  |
File monitoring data 36%  |  Packet sniff/tcpdump 33%  |  Don’t know/other 12%
5
2021 THREAT HUNTING REPORT All Rights Reserved.  ©2021  Cybersecurity Insiders

DETECTION METHODS
More than half of organizations (59%) spend less than 50% of their time proactively innovating to prevent
a security threat, while 51% spend the same time in reactive response.
In a typical week, what percentage of your threat management time is spent with
alert triage or reactive response to security threats versus engaging in proactive and
innovative detection methods?
51%
0-25 24%
26-50 27% Are spending less than 50%
of their time in reactive response
REACTIVE of security threats
23%
51-75
76-100 26%
59%
34%
0-25
Are spending less than 50%
26-50 25%
of their time in proactive prevention
of security threats
PROACTIVE
21%
51-75
76-100 20%
6
2021 THREAT HUNTING REPORT All Rights Reserved. ©2021 Cybersecurity Insiders

THREAT INDICATORS
Developing effective defense strategies requires understanding the indicators that compromise
the organization’s security posture. Research reveals that hunt teams most frequently investigate
behavioral anomalies (71%), followed by denied/flagged connections (60%), suspicious IP addresses
(56%), and suspicious domain names (51%).
What kinds of indicators are most frequently investigated by your hunt team?
|                      | 71%                  | 60%            | 56%          |
| -------------------- | -------------------- | -------------- | ------------ |
| Behavioral anomalies |                      | Denied/flagged | Suspicious   |
|                      | (unauthorized access | connections    | IP addresses |
attempts, etc.)
51% 31%
Domain names File names
Not sure/other 13%
7
2021 THREAT HUNTING REPORT All Rights Reserved.  ©2021  Cybersecurity Insiders

INSIGHTS INTO ADVERSARIES
68% of organizations, at least occasionally develop insights into adversary infrastructures as part
of their threat hunting activities. However, only 21% of organizations are fully focused on gaining
these insights.
How often do you develop insights into adversary infrastructure (domains and IP
addresses) as part of your hunt activities?
21% Of organizations fully focus on developing
insights into adversary infrastructures
as part of their threat hunting activities
26%
21%
20%
Almost Frequently Occasionally Almost
every time never
Don’t know 12%
What are the most useful insights into adversary infrastructure that threat hunting
produces?
Actionable IoCs, for immediate
70%
response/blocking
Understanding adversary tendencies and trends to
70%
assist in identifying infrastructure or adversary intent
Generating rule sets or other automation
57%
to alert on future similar activity
Related infrastructure, for historic 37%
or related analysis
37%
Full threat actor attribution
Attributed IoCs, for law enforcement
33%
or other actions
Other 3%
8
2021 THREAT HUNTING REPORT All Rights Reserved. ©2021 Cybersecurity Insiders

THREAT HUNTING TECHNOLOGIES
Many technologies are available to hunt threats. Endpoint detection and response is the clear leader
with 63% of organizations integrating these tools into their threat hunting efforts, followed by SIEM
(56%) and anti-phishing or other messaging security software (54%).
Which technologies do you use as part of your organization’s threat hunting approach?
|     | 63% |     | 56% |     | 54% |     |
| --- | --- | --- | --- | --- | --- | --- |
Anti-phishing or
Endpoint Detection SIEM
|     | & Response (EDR) |     |     |     | other messaging |     |
| --- | ---------------- | --- | --- | --- | --------------- | --- |
security software
|     | 53% |     | 53% | 50% |     | 43% |
| --- | --- | --- | --- | --- | --- | --- |
Vulnerability
| NGFW, IPS, AV,  |     | Network IDS/ |     |     | Threat intelligence  |     |
| --------------- | --- | ------------ | --- | --- | -------------------- | --- |
management
| web application  |     | Network Detection  |     |     |     | platform |
| ---------------- | --- | ------------------ | --- | --- | --- | -------- |
| firewall, etc.   |     | and Response (NDR) |     |     |     |          |
Enrichment and investigation tools 29%  |  Security Orchestration, Automation, and Response (SOAR) 19%  |  Not sure/
other 12%
9
2021 THREAT HUNTING REPORT All Rights Reserved.  ©2021  Cybersecurity Insiders

THREAT HUNTING DATA
Organizations need to collect data from multiple sources to add context to their threat hunting
activities. External threats intel feeds (56%), user behavior data (56%), and file activity data (46%)
are the most common means for collecting this data.
Which contextual information do you use as part of your threat hunting data?
| 56%             |     | 56%           |     | 46%           |      |
| --------------- | --- | ------------- | --- | ------------- | ---- |
| External threat |     | User behavior |     | File activity |      |
| intel feeds     |     | data          |     |               | data |
| 44%             | 43% |               | 43% |               | 41%  |
System patch User permission Network protocol Source blacklist
| status | data |     | data |     |     |
| ------ | ---- | --- | ---- | --- | --- |
Asset inventory data 41%  |   Data classification 38%  |  File permission data 38%  |   Other 3%
10
2021 THREAT HUNTING REPORT All Rights Reserved.  ©2021  Cybersecurity Insiders

POPULAR RECONNAISSANCE
ACTIVITIES
Port scanning is the most used activity for reconnaissance, with 73% of organizations including
this technique in their threat hunting efforts. This is followed by active directory enumeration
(54%) and host enumeration (44%).
Which of the following reconnaissance activities do you look for as part of your threat
hunting activities?
| 73%           | 54%              |     | 44%              |     |
| ------------- | ---------------- | --- | ---------------- | --- |
| Port scanning | Active directory |     | Host enumeration |     |
enumeration
| 42%                        | 41%             | 36%       |     | 33%         |
| -------------------------- | --------------- | --------- | --- | ----------- |
|                            | Password policy |           |     | Service     |
| Remote system LDAP queries |                 |           |     |             |
|                            |                 | discovery |     | enumeration |
discovery
Open share enumeration 31%  |  None 10%  |  Other 4%
11
2021 THREAT HUNTING REPORT All Rights Reserved.  ©2021  Cybersecurity Insiders

BENEFITS OF THREAT HUNTING
Threat hunting platforms provide security analysts with powerful tools to enable earlier detection,
reduce dwell time, and improve defenses against future attacks. The top benefits organizations
derive from threat hunting platforms include improved detection of advanced threats (68%) and
tying at 55% are reduced investigation time, and saved time manually correlating events.
What are the main benefits of using a threat hunting platform for security analysts?
|                     | 68% |                   |               | 55%                |          |                 |         | 55%                  |                 |         |
| ------------------- | --- | ----------------- | ------------- | ------------------ | -------- | --------------- | ------- | -------------------- | --------------- | ------- |
| Improving detection |     |                   |               |                    | Reducing |                 |         | Saving time manually |                 |         |
| of advanced threats |     |                   |               | investigation time |          |                 |         | correlating events   |                 |         |
|                     | 49% |                   | 48%           |                    |          |                 | 48%     |                      |                 | 43%     |
| Discovering         |     |                   | Reducing time |                    |          | Reducing attack |         |                      | Creating new    |         |
| threats that could  |     | wasted on chasing |               |                    |          |                 | surface |                      |                 | ways of |
| not be discovered   |     |                   | false leads   |                    |          |                 |         |                      | finding threats |         |
otherwise
Connecting disparate sources of information 39%  |  Reducing extra and unnecessary noise in the system 38%  |
Saving time scripting and running queries 35%  |   Other 3%
12
2021 THREAT HUNTING REPORT All Rights Reserved.  ©2021  Cybersecurity Insiders

METHODOLOGY & DEMOGRAPHICS
This Threat Hunting Report is based on the results of a comprehensive online survey of cybersecurity
professionals, to gain deep insight into the latest trends, key challenges, and solutions for threat
hunting management. The respondents range from technical executives to managers and IT security
practitioners, representing a balanced cross-section of organizations of varying sizes across multiple
industries.
PRIMARY ROLE
19% 16% 12% 11% 10% 7% 4% 4% 17%
IT Manager, Director or CIO CSO, CISO or VP of Security Security Analyst Security Manager or Director Systems Administrator
Security Administrator Threat Analyst Auditor Other
CAREER LEVEL
17% 16% 16% 13% 10% 8% 5% 5% 10%
Director Specialist CTO,CIO,CISO,CMO,CFO,COO Manager/Supervisor Consultant Administrator
Owner CEO/President Other
DEPARTMENT
32% 21% 11% 8% 6% 4% 18%
IT Security IT Operations Security Operations Center (SOC) Engineering Sales/Marketing Product Management
Other
COMPANY SIZE
26% 14% 14% 16% 6% 24%
Less than 100 100-499 500-999 1,000-4,999 5,000-9,999 Over 10,000
INDUSTRY
23% 18% 11% 11% 7% 6% 4% 3% 17%
Technology Financial Services, Banking or Insurance Government Healthcare Manufacturing Telecommunications or ISP
Retail or Ecommerce Energy or Utilities Other
13
2021 THREAT HUNTING REPORT All Rights Reserved. ©2021 Cybersecurity Insiders

LookingGlass develops cybersecurity solutions that empower
organizations to meet their missions with tailored, actionable threat
intelligence and threat mitigation capabilities that move at machine
speed. For more than a decade, the most advanced organizations
in the world have trusted LookingGlass to help them protect
financial systems, ensure telecommunications are cyber-resilient and
safeguard economic and national security interests.
Rooted in operationalizing threat intelligence, LookingGlass
solutions help reduce the time to detect and respond to incidents,
enable cyber investigations, optimize threat hunt operations, and
improve analyst productivity and efficiency. By linking the risks
and vulnerabilities from an organization’s external attack surface
to customized threat actor models, LookingGlass provides a more
complete view of cyber risk and enables systematic definition and
deployment of mitigations to defend against the threats that matter.
Learn more at lookingglasscyber.com

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-09-01", "model": "gemini-3.5-flash-lite"} -->
