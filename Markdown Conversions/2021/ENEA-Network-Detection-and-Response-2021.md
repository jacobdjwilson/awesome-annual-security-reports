2021
NETWORK
DETECTION
AND RESPONSE
REPORT

EXECUTIVE SUMMARY
Recent high-profile incidents at companies like SolarWinds, Microsoft, T-Mobile, Facebook,
Colonial Pipeline, JBS and Acer highlight the significant harm caused by advanced cyber-
attacks. These types of attacks can successfully circumvent endpoint and perimeter
defenses, remain hidden and active in networks for a long time, and are capable of causing
extensive damage.
Network Detection and Response (NDR) solutions are designed specifically to detect and
respond to advanced cyber threats. NDR is a solution that combines the signature-based
threat detection capabilities of IDS/IPS with Network Traffic Analysis, which detects unknown
or hidden threats through the identification of behavioral anomalies in network traffic.
But how familiar are security professionals with NDR? How many have or plan to deploy an
NDR solution? What features and capabilities do they expect in an NDR solution? And what
concerns are holding some back from adopting NDR?
To find the answers to these questions, we conducted a survey of Cybersecurity
Insiders’ 500,000-member information security community.
For a panel discussion about options and strategies for addressing the needs and
concerns raised in this survey, we invite you to watch our webinar How to Use Network
Detection & Response to Mitigate the Inevitable Breach.
Many thanks to Enea Qosmos for supporting this important research project.
We hope you find the information shared by respondents useful in assessing and honing
your own cybersecurity strategies, and we hope that you enjoy reading the report.
Thanks
Holger Schulze
Holger Schulze
CEO and Founder
Cybersecurity Insiders
2021 NETWORK DETECTION AND RESPONSE REPORT All Rights Reserved. ©2021 Cybersecurity Insiders 2

KEY FINDINGS
FINDING 1:
NDR Adoption
NDR is viewed as an essential tool in the battle against advanced
persistent threats (APTs), with NDR experiencing a rapid adoption rate.
73% of respondents consider the anomaly detection capabilities of
network traffic analysis (NTA) to be critically important for detecting
APTs, and 55% have already deployed or plan to deploy a full NDR
solution that combines the anomaly detection capabilities of NTA with
threat signature detection capabilities of IDS/IPS for maximum protection
against APTs.
FINDING 2:
NDR Capabilities
Cloud adoption and IoT/IIoT are creating network and connected device
blind spots, and security professionals expect NDR to address this.
• 9 out of 10 organizations expect NDR to cover hybrid IT/IoT LAN/
WAN networks, with special concerns for cloud workload traffic and
dedicated IoT/IIoT and OT/ICS networks.
• Beyond anomaly detection, the additional capability professionals
want most in an NDR solution is connected device identification.
FINDING 3:
Threat Priorities
Command and control attacks (69%), ransomware (57%), and data
exfiltration (50%) top the rankings of specific threats respondents expect
NDR to detect.
FINDING 4:
Barriers to Adoption
The top barriers to NDR adoption are concerns over solution cost and
uncertainty regarding the maturity of machine learning-based behavioral
analytics.
2021 NETWORK DETECTION AND RESPONSE REPORT All Rights Reserved. ©2021 Cybersecurity Insiders 3

NETWORK VISIBILITY GAPS
Network visibility is an issue affecting all types of traffic, layers, and devices – and it is further complicated
by encryption and the complexities of virtualization. When asked about the most significant gaps in
network visibility, survey respondents prioritized cloud workload traffic (46%), followed by connected
device communication (42%) and SaaS apps (39%).
Where do you feel you have the most significant network visibility gaps?
| 46%      |     | 42%       |     | 39%  |     | 34%           |
| -------- | --- | --------- | --- | ---- | --- | ------------- |
| Cloud    |     | Connected |     | SaaS |     | Local traffic |
| workload |     | devices   |     | apps |     | (East-West)   |
traffic
|     | 25%              |     | 24%              |     | 20%              |     |
| --- | ---------------- | --- | ---------------- | --- | ---------------- | --- |
|     | Public internet  |     | IoT/IIoT traffic |     | Traffic between  |     |
|     | traffic          |     |                  |     | enterprise sites |     |
4
2021 NETWORK DETECTION AND RESPONSE REPORT All Rights Reserved.  ©2021 Cybersecurity Insiders

TRAFFIC DATA SOURCES
Which data sources are most relevant to tap into to gain better visibility into network traffic? Cybersecurity
professionals in our survey primarily rely on logs from network equipment, such as routers, switches,
firewalls, etc. (85%). This is followed by logs from host applications, such as web servers, or email servers
(58%) and logs and notifications from endpoint agents (54%).
What individual data sources do you currently rely on for network traffic visibility?
|                   | 85%       |     | 58%             |     | 54%                |     |
| ----------------- | --------- | --- | --------------- | --- | ------------------ | --- |
|                   | Logs from |     | Logs from host  |     | Logs/notifications |     |
| network equipment |           |     | applications    |     | from endpoint      |     |
agents
|     | (routers, switches,   |             | (web server,        |         |     |             |
| --- | --------------------- | ----------- | ------------------- | ------- | --- | ----------- |
|     | firewalls, SWG, etc.) |             | email server, etc.) |         |     |             |
|     | 44%                   |             | 41%                 | 31%     |     | 22%         |
|     | Network sensors       | Alerts from |                     | NetFlow |     | Full packet |
|     | with Deep Packet      |             | IDS                 | records |     | capture     |
Inspection (DPI)
(via SPAN, mirror port,
or network TAP)
5
2021 NETWORK DETECTION AND RESPONSE REPORT All Rights Reserved.  ©2021 Cybersecurity Insiders

NETWORK TRAFFIC ANALYSIS
Network traffic analysis is rising in importance, especially when detecting anomalies that evade traditional
endpoint detection. 73% of cybersecurity professionals agree that traffic analysis is important or critically
important to detecting such anomalies.
How important has network traffic analysis become in your environment to detect anomalies that have
evaded traditional endpoint detection?
73% consider network traffic analysis
important to critical in detecting
anomalies that have evaded
traditional endpoint detection
33%
40%
19%
Somewhat important Critical
Somewhat important Important Critical
Not sure 8%
2021 NETWORK DETECTION AND RESPONSE REPORT All Rights Reserved. ©2021 Cybersecurity Insiders 6

NETWORK-BASED
INTRUSION DETECTION
Intrusion detection systems are a critical component in organizations’ security posture. They can be
deployed in standalone form, or integrated into broader security platforms. 41% of organizations confirm
they are using standalone IDS in their network. Of those who don’t use a standalone IDS, 17% have plans
to deploy one.
Do you use a standalone network-based IDS?
41%
25%
|           | 17%      |           | 17%      |
| --------- | -------- | --------- | -------- |
| YES       | NO,      | NO        | Not sure |
|           | but plan | plans at  |          |
| to deploy |          | this time |          |
7
2021 NETWORK DETECTION AND RESPONSE REPORT All Rights Reserved.  ©2021 Cybersecurity Insiders

NDR USAGE
Network detection and response solutions are rapidly gaining momentum as part of organizations’
security investments. 35% of organizations are already using NDR solutions in their network and 20%
have plans to deploy one.
Do you use an NDR solution?
55%have either already deployed
an NDR solution or have
plans to do so
20%
35%
25%
NO plans at this time YES
No plans at this time No, but plan to deploy Yes
Not sure 20%
2021 NETWORK DETECTION AND RESPONSE REPORT All Rights Reserved. ©2021 Cybersecurity Insiders 8

THREAT DETECTION & RESPONSE
PRIORITIES
Cybersecurity professionals prioritize threats within the complex and evolving threat landscape based
on their likelihood and capacity to inflict damage. Command and control attacks (69%) top the list of
threats considered most essential to be addressed by network detection and response. This is followed
by ransomware (57%) and data exfiltration (50%).
Which threats do you consider it most important for your NDR to address?
| 69%         |     | 57%        |     | 50%          |      |
| ----------- | --- | ---------- | --- | ------------ | ---- |
| Command     |     | Ransomware |     |              | Data |
| and control |     |            |     | exfiltration |      |
attacks
|                  | 43% |                    | 40% |              | 34% |
| ---------------- | --- | ------------------ | --- | ------------ | --- |
| Malware lateral  |     | Malware intrusion  |     | DDoS attacks |     |
movements
(file analysis)
Phishing attacks 26%  |  Illicit cryptomining 16%
9
2021 NETWORK DETECTION AND RESPONSE REPORT All Rights Reserved.  ©2021 Cybersecurity Insiders

NDR ADVANTAGES OVER IDS/IPS
We asked cybersecurity professionals what advantages they see provided by network detection and
response versus standalone intrusion detection/protection solutions. 74% highlight the better capacity
to detect anomalous and suspicious behavior, followed by enablement of proactive threat hunting (57%)
and the provision of contextual data to improve alert investigation and analysis (50%).
What do you think are the most important advantages of NDR versus standalone IDS/IPS?
| 74%              | 57%              |     | 50%                |     |
| ---------------- | ---------------- | --- | ------------------ | --- |
| Detect anomalous | Enable proactive |     | Provide contextual |     |
| or suspicious    | threat-hunting   |     | data to improve    |     |
behavior alert investigation
| (flows, packets, users, |     |     | and analysis |     |
| ----------------------- | --- | --- | ------------ | --- |
endpoints)
| 47% | 33% | 29% |     | 22% |
| --- | --- | --- | --- | --- |
Discover unmanaged/ Reduce false Improve Provide visibility on
unauthorized positive IDS/IPS  post-incident  encrypted traffic
| devices on the | alerts | forensics |     |     |
| -------------- | ------ | --------- | --- | --- |
network
10
2021 NETWORK DETECTION AND RESPONSE REPORT All Rights Reserved.  ©2021 Cybersecurity Insiders

NETWORK MONITORING & PROTECTION
We asked organizations what networks they think a network detection and response solution should
monitor and protect. 9 out of 10 organizations prioritize support for IT and hybrid IT/IoT LAN/WAN (91%),
followed by cloud workload traffic (70%) and traffic on dedicated IoT/IIot networks (63%).
What kind of networks do you think an NDR solution should be able to monitor and protect?
91%
70%
63%
55%
20%
IT and hybrid Cloud Traffic on OT/industrial Private 5G
IT/IoT workload dedicated control system
LAN/WAN IoT/IIoT networks
networks
2021 NETWORK DETECTION AND RESPONSE REPORT All Rights Reserved. ©2021 Cybersecurity Insiders 11

NDR SOLUTION CAPABILITIES
What network detection and response capabilities do organizations see as most important? Device
detection is the single most mentioned capability (60%), followed by flexible querying capabilities for
threat hunting (47%) and automatic suggestions for rules and incidence response (45%).
Beyond anomaly detection, what additional capabilities do you think are most important for an NDR
solution?
| 60% |     | 47% |     | 45% |     |
| --- | --- | --- | --- | --- | --- |
Auto-suggestions
| Device | Flexible querying |     |     |     |     |
| ------ | ----------------- | --- | --- | --- | --- |
for rules and
| detection |     | capabilities for |     |     |     |
| --------- | --- | ---------------- | --- | --- | --- |
incidence response
threat hunting
| 43%     |                 | 41% | 38%                   |     | 36%            |
| ------- | --------------- | --- | --------------------- | --- | -------------- |
| Malware | Integration of  |     | L2-L7 classification  |     | Easy pivoting  |
detection external threat  of encrypted traffic  from an alert
|     | intelligence feeds |     | without using  |     | to relevant  |
| --- | ------------------ | --- | -------------- | --- | ------------ |
|     |                    |     | decryption     |     | source data  |
Phishing detection 33%  |  DNS/IP reputation 31%  |  Service-based support from external threat analyst professionals
26%  |  SSL proxy for decryption and inspection 17%  |  Other 3%
12
2021 NETWORK DETECTION AND RESPONSE REPORT All Rights Reserved.  ©2021 Cybersecurity Insiders

NDR ADOPTION BARRIERS
Why are some organizations delaying the adoption of network detection and response? The primary
barriers include cost and budget factors (40%), followed by concerns about the reliability of behavioral
analytics and machine learning (31%), and a preference for NDR capabilities to be integrated into an
existing platform (rather than deploying a standalone solution) (29%).
If you do not plan to adopt NDR, what are the primary reasons?
| 40%            |     | 31%             |                     | 29%        |
| -------------- | --- | --------------- | ------------------- | ---------- |
| Too expensive/ |     | Concerns about  |                     | Prefer NDR |
|                |     | reliability of  | capabilities to be  |            |
not enough
|     |     | behavioral  | integrated into an  |     |
| --- | --- | ----------- | ------------------- | --- |
budget
|     |     | analytics and    | existing platform            |     |
| --- | --- | ---------------- | ---------------------------- | --- |
|     |     | machine learning | (rather than deploying as a  |     |
standalone solution)
|     | 26%              |     | 23%                   | 20% |
| --- | ---------------- | --- | --------------------- | --- |
|     | Too much overlap |     | Insufficient coverage |     |
Insufficient coverage
|                        | with existing | of cloud workloads |     | of OT/IoT       |
| ---------------------- | ------------- | ------------------ | --- | --------------- |
| threat detection tools |               |                    |     | network traffic |
13
2021 NETWORK DETECTION AND RESPONSE REPORT All Rights Reserved.  ©2021 Cybersecurity Insiders

XDR ADOPTION
When asked about their adoption of XDR (i.e., a platform that integrates NDR, EDR, and other threat
detection and response tools), a majority of professionals (55%) have already deployed or are planning
to deploy an XDR solution.
Have you deployed an XDR solution (i.e., a platform that integrates NDR, EDR (Endpoint Detection and
Response) and other threat detection and response tools)?
55%
have already deployed or
are planning to deploy XDR
24% 31%
Yes No, but plan
to deploy
20%
Not sure
25%No plans
for XDR
2021 NETWORK DETECTION AND RESPONSE REPORT All Rights Reserved. ©2021 Cybersecurity Insiders 14

METHODOLOGY & DEMOGRAPHICS
This report is based on the results of a comprehensive online survey of 315 cybersecurity
professionals, to gain more insight into the latest trends, key challenges, and solutions for network
detection and response. The respondents range from technical executives to managers and IT
security practitioners, representing a balanced cross-section of organizations of varying sizes
across multiple industries.
CAREER LEVEL
31% 18% 13% 11% 7% 7% 4% 4% 5%
CTO,CIO,CISO,CMO,CFO,COO Director Consultant Manager/Supervisor Specialist Vice President
Administrator CEO/President Other
DEPARTMENT
28% 26% 11% 9% 8% 2% 16%
IT Security IT Operations Product Management Engineering Security Operations Center (SOC)
Sales/Marketing Other
COMPANY SIZE
29% 18% 15% 18% 7% 13%
Less than 100 100-499 500-999 1,000-4,900 5,000-9,999 +10,000
INDUSTRY
44% 9% 9% 7% 4% 4% 4% 19%
Technology Financial Services, Banking or Insurance Retail or Ecommerce Healthcare Manufacturing
Telecommunications or ISP Energy or Utilities Other
2021 NETWORK DETECTION AND RESPONSE REPORT All Rights Reserved. ©2021 Cybersecurity Insiders 15

About Enea
Enea is one of the world’s leading specialists in software for telecommunications
and cybersecurity. The company’s cloud-native products are used to enable and
protect services for mobile subscribers, enterprise customers, and the Internet of
Things. More than 3 billion people rely on Enea technologies in their daily lives.
The Qosmos Division of Enea specializes in Deep Packet Inspection (DPI) software,
which recognizes thousands of protocols and metadata to provide the most accurate
picture of real-time data activity on networks. As a DPI sensor, the Qosmos Probe
strengthens cybersecurity through efficient data analysis and traffic visibility up to
the application level:
• Analysis of data flows in real time at n x 10 Gpbs, up to Layer 7
• Recognition of over 3600 protocols and ability to extract more than
5000 metadata
• Fewer false positives when using information from the probe to improve
IDS rules
• Forensic data reduced by up to 150x compared to full packet capture
www.qosmos.com

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-09-01", "model": "gemini-3.5-flash-lite"} -->
