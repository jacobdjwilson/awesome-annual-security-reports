2024 REPORT
State of Network
Threat Detection

Executive Summary
While “platformization” has been a hot topic in 2024, it has also been a year in which security
professionals have looked to advanced, highly specialized tools to help them solve thorny problems
that not only persist but seem to grow more challenging by the day. Among these are acute alert
fatigue, a steady erosion of network visibility, and a growing sophistication in cyberattacks.
Among the specialized tools security professionals are looking to are Network-based Threat Detection
(NTD) solutions, such as Network-based Intrusion Detection Systems (NIDS) and Network-based Threat
Detection and Response (NDR). To better understand the state of Network Threat Detection and
whether today’s solutions and supporting technologies— like deep packet inspection— are meeting
contemporary security challenges, Cybersecurity Insiders surveyed its 600,000-member information
security community. The survey reveals that while NTD tools are widely deployed and positively viewed,
they must evolve if they are going to help security professionals meet significant present-day and
emerging challenges.
Key findings:
ALERT ISSUES
• Alert prioritization is the #1 overall operational challenge for security teams
• Alert accuracy & actionability is cited as the greatest challenge with NIDS specifically
VISIBILITY CHALLENGES
• No (or poor) global attack surface visibility is the #2 overall operational challenge
• Encrypted traffic is the #1 network blind spot, which 55% report negatively impacts security
DESIRED PRODUCT ENHANCEMENTS
• AI integration: 71% consider AI integration extremely or very important for combatting
advanced threats
• Automatic scoring & prioritization of threats named the #1 must-have for an effective network
threat detection solution
DEPLOYMENT PLANS & PREFERENCES
• Majority (66%) plan to implement anomaly detection over the next 6 to 24 months; only 17% report
having an NTD solution now that uses anomaly detection
• Majority (59%) prefer standalone NTD solutions (DPI sensor, NIDS, NDR, XDR) to NTD within multi-
function security platforms (e.g., SASE, SSE)
Experts from Enea, Arista Security, and Custocy discuss options and strategies for addressing the
needs and concerns raised in this survey in a panel discussion. We invite you to watch the webinar
“2024 State of Network Threat Detection” on November 14, 2024, or afterwards on-demand.
Many thanks to Enea, Arista Security and Custocy for supporting this important research project, with
special gratitude to Enea for their invaluable contribution to this report.
Holger Schulze
Founder, Cybersecurity Insiders
ENEA | 2024 Network Threat Detection Report ©2024 Cybersecurity Insiders. All Rights Reserved. 2

Table of Contents
FINDINGS
4
Awareness
5
Challenges
13
Enhancements
16
Plans
17
Preferences
THE SURVEY
20
Methodology & Demographics
ENEA | 2024 Network Threat Detection Report ©2024 Cybersecurity Insiders. All Rights Reserved. 3

|   AWARENESS  |
Even Split on Familiarity with & Opinion of NTD
About half of respondents (44%) are very familiar with NTD tools and use them regularly, while a
similar percentage (45%) are only somewhat familiar with them and use them only occasionally. The
rest are only slightly familiar, or not familiar at all, with NTD tools.
How familiar are you with network threat detection tools and technologies?
| 44%                |     | 45%               |     |     |
| ------------------ | --- | ----------------- | --- | --- |
| Very familiar      |     | Somewhat familiar |     |     |
| I use them         |     | I have a good     |     |     |
| regularly as part  |     | understanding     |     |     |
| of my job          |     | and occasionally  |     |     |
use them
|                       | 2%  | 9%                      |     |     |
| --------------------- | --- | ----------------------- | --- | --- |
| Not familiar at all   |     | Slightly familiar       |     |     |
| I have no experience  |     | I know the basics but   |     |     |
| with these tools      |     | have limited experience |     |     |
A similar breakdown applies to the perceived effectiveness of NTD solutions: half (50%) rate them as
either extremely or very effective while 42% find them only moderately effective, and 8% find them
slightly or not at all effective. While differences in domain specialization may affect awareness and
usage, all security team team members would benefit from increased awareness of the vital role
NTD plays in contemporary multilayered defensive systems. With regard to confidence levels, much
progress can be made by focusing solution roadmaps on the important challenges identified in
this survey.
How effective do you think network threat detection is in mitigating risk and reducing your risk profile?
42%
34%
16%
7%
1%
| Extremely | Very      | Moderately | Slightly  | Not at all |
| --------- | --------- | ---------- | --------- | ---------- |
| effective | effective | effective  | effective | effective  |
ENEA   |   2024 Network Threat Detection Report   ©2024  Cybersecurity Insiders.  All Rights Reserved. 4

| CHALLENGES |
Alerts & Visibility Are Top Operational Challenges
When asked for their top three operational challenges, the difficulty prioritizing alerts emerged as a
top challenge for 52% of respondents. Given the huge volume of alerts frontline security professionals
typically face, distinguishing between critical and low-risk incidents can be a major (and highly
frustrating) hurdle.
This issue is compounded by a lack of visibility into the global attack surface (50%), which opens a
crucial gap in defensive capabilities as organizations expand into cloud and hybrid environments, the
number of edge locations multiply, and information, operational and communications technologies
converge. Closely linked to challenges with visibility and alert prioritization, the number three
challenge, cited by 49% of respondents, is speed of detection and response.
What are the three biggest operational challenges for your security team?
Difficulty
prioritizing alerts 52%
No (or poor) visibility
into global attack surface 50%
Speed of detection
and response 49%
Too many security tools
and/or poor tool integration 45%
Difficulty detecting
advanced threats
38%
Balancing security
and network
performance demands 26%
ENEA | 2024 Network Threat Detection Report ©2024 Cybersecurity Insiders. All Rights Reserved. 5

| CHALLENGES |
Alert Accuracy & Actionability #1 NIDS/IDS Issue
Echoing the top response for operational challenges, the most pressing need in the specific context of
NIDS/IPS deployments is more accurate and actionable alerts (61%). As with effective prioritization of
alerts, reducing false positives and alert noise can improve the efficiency and effectiveness of security
teams, which would help address the burnout and turnover challenges cited on page 11.
Another difficulty is limited visibility into cloud workloads, cited as the second greatest challenge by
52% of respondents. Technical performance challenges come in at number three (48%), followed by
the loss of functionality for encrypted flows (42%) and limited protocol and application coverage (39%).
These are all factors respondents cite in explaining why they prefer commercial rather than open
source NIDS/IPS solutions (see page 18).
If you use a NIDS/IPS, what are your greatest challenges?
61% Alert accuracy and actionability
(less noise)
52% Limited visibility
into cloud workloads
48% Performance
(latency, throughput, etc.)
23% 42% Loss of functionality
for encrypted flows
Do not
use NIDS
39% Limited protocol and
application coverage
ENEA | 2024 Network Threat Detection Report ©2024 Cybersecurity Insiders. All Rights Reserved. 6

| CHALLENGES |
Visibility Challenges Drive Wider Sourcing
for Traffic-Related Insights
To address visibility gaps arising from evolving networks, security professionals are turning to an
expanded pool of resources for gathering network traffic-related insights. Logically enough, a
Network Intrusion Detection System (NIDS) is reported to be the most commonly used tool (67%).
Deep Packet Inspection (DPI) (49%) and non-DPI packet sniffers (35%) also make a strong showing,
which is to be expected given their long-time leading role in extracting traffic insights.
What is new is relying on sources such as endpoint agents (58%), external intelligence feeds (41%),
and device/host kernel applications (eBPF) (28%) to gather network traffic insights (with the latter
especially common in cloud workloads).
This reliance on non-network tools for network insights is a two-way street. For example, today
advanced DPI can deliver unique insights into devices and users in addition to network flows. This
diversification of resources used for cross-domain insights is a welcome development as important
strategies such as zero trust and defense-in-depth rely heavily on broadly sourced contextual data
to be effective.
Which types of tools (in embedded or standalone form) do you use to gather network
traffic-related insights?
67%
58%
49%
41%
35%
28%
Network Intrusion Software Deep Packet External Non-DPI Device/host
Detection System agents on Inspection intelligence network packet kernel
(NIDS) endpoints (DPI) feeds sniffer/parser applications
(eBPF)
ENEA | 2024 Network Threat Detection Report ©2024 Cybersecurity Insiders. All Rights Reserved. 7

| CHALLENGES |
Encrypted Traffic Is the Most Significant Blind Spot
Among specific visibility gaps, respondents rank encrypted traffic as number one (44%), followed
closely by multi-cloud traffic (42%) and SaaS app traffic (39%). Cloud and SaaS app use poses
a double challenge to visibility: the growth rate outpaces the ability to integrate the apps into
monitoring tools and structural challenges make it difficult to extract insights from resources
controlled by third parties. Ranked fourth is intra-cloud workload traffic (34%), which underscores
the fact that this internal traffic often falls outside the purview of traditional security tools.
Additional sources of concern are public internet traffic (31%) (a challenge due partly to the
increase in remote work), IoT and IIoT traffic (28%), and OT/industrial control system traffic (14%),
where specialized devices and protocols make visibility and threat detection more difficult. These
environments are also often more sensitive to disruptions, making it harder to inspect traffic without
impacting operational performance.
Where do you feel you have the most significant network traffic visibility gaps?
Encrypted 44%
traffic
Multi-cloud 42%
traffic
SaaS app 39%
traffic
Intra-cloud
34%
workload traffic
Public
31%
internet traffic
IoT/IIOT 28%
traffic
OT/industrial
14%
control system traffic
ENEA | 2024 Network Threat Detection Report ©2024 Cybersecurity Insiders. All Rights Reserved. 8

| CHALLENGES |
Encryption Has a Negative Impact on Security
Beyond the negative impact on visibility, encrypted traffic creates many challenges for security (and
networking) teams. Ironically, though encryption was developed to strengthen security, respondents
report that their number one challenge with its use is the negative impact it has on cybersecurity
(55%). Trying to navigate the regulatory issues that govern encryption is the second most significant
challenge for respondents (40%), while a close 39% circle back to the recurring theme of visibility
impediments, with 37% also reporting that encryption has a negative impact on traffic steering.
Additionally, 28% of respondents highlight performance degradation caused by decryption and
inspection processes. This highlights a challenge with what could otherwise be a solution to visibility
difficulties: decrypting and inspecting all traffic (within the limits of regulations). This strategy is
commonly employed by SASE and SSE vendors, who recreate high-performing central gateways on
cloud perimeters.
What challenges do you have with encrypted traffic?
Negative impact on cybersecurity
(encryption used to cloak attacks)
55%
Restrictions on use of decryption & inspection
40%
due to compliance (i.e., HIPAA, PCI, GDPR, etc.)
39% Negative impact on
network visibility
Negative impact on
37%
traffic steering
Negative performance impact
28%
of decryption & inspection
6%
Encrypted traffic does not pose
a challenge for us
In any case, 11% report the formidable challenge of performing network threat detection on
encrypted traffic alone, and 57% perform it on both encrypted and clear traffic.
Do you perform network threat detection on clear or encrypted traffic?
24% 11% 5577%% 8%
Clear only Encrypted only Both Not sure
ENEA | 2024 Network Threat Detection Report ©2024 Cybersecurity Insiders. All Rights Reserved. 9

| CHALLENGES |
Reducing Attack Surface Should Be Higher Priority
Another indicator of the importance security teams place on closing visibility gaps is the divergence
between what security teams think executive priorities are for the security organization versus what
security teams think they should be.
Here, security professionals think executives consider meeting compliance requirements as the
security organization’s number two priority. However, they believe minimizing the global
attack surface should actually occupy that spot (with minimizing the global attack surface being
dependent on network visibility).
What do you think is your executive What do you think your executive
team’s top goal for your cybersecurity team’s top goal should be for your
organization today? cybersecurity organization?
31% Prevent 34%
breaches
Meet
22% 11%
compliance
requirements
Provide a company
15% competitive 9%
advantage
14% Enable business 16%
agility & efficiency
10% Minimize global 23%
attack surface
8% Reduce 7%
spending
ENEA | 2024 Network Threat Detection Report ©2024 Cybersecurity Insiders. All Rights Reserved. 10

| CHALLENGES |
Security Teams Feel Unprepared & Overwhelmed
The top organizational challenge cited by respondents is inadequate in-house skills and training,
followed closely by staff burnout and turnover.
Given the high importance respondents placed on AI integration in network threat detection
solutions (see page 13), it is likely staff have confidence that one of AI’s benefits will be to make them
feel better equipped to meet ever more sophisticated attacks. And successfully addressing the top
operational challenges of alert fatigue and poor attack surface visibility – also likely with AI support –
could certainly be expected to reduce staff burnout and turnover.
What are the three biggest organizational challenges facing your security team?
53%
49%
42%
38%
35%
28%
Inadequate Insufficient Insufficient Lack of Difficulty Cost of
in-house staff and/or budget for executive meeting breaches
skills and burnout/ tools support compliance and
training turnover requirements insurance
ENEA | 2024 Network Threat Detection Report ©2024 Cybersecurity Insiders. All Rights Reserved. 11

|   CHALLENGES  |
Challenges with ML/AI-Based Network Threat Detection
Of those who use ML/AI, the number one challenge cited is model selection, followed by data
acquisition and data cleansing and normalization. Regarding the 4th and 5th challenges, managing
drift and model tuning, vendors are providing more tools to empower users to address these natural
AI lifecycle evolutions on their own, though more than one third (35%) still provide only black box
access to their ML/AI solutions.
For ML/AI-based network threat detection, which of the following do you find challenging?
29%
Maintaining quality
results over time
| 52% | 43% | 40% | (e.g., managing drift) |
| --- | --- | --- | ---------------------- |
25%
Model tuning
23%
| Model selection | Data acquisition | Data cleansing/ |     |
| --------------- | ---------------- | --------------- | --- |
normalization
Feature selection
If you currently have a commercial network threat detection product that uses AI/ML for advanced
threat detection, what access and support does the vendor provide?
|     | An ongoing tuning service to maintain model |     | 54% |
| --- | ------------------------------------------- | --- | --- |
performance as input data evolves (i.e., manage drift)
|     | Tools for your team to self-tune models | 45% |     |
| --- | --------------------------------------- | --- | --- |
|     | Black box access only                   | 35% |     |
White box access
29%
to the model
|     | Uncertain 20% |     |     |
| --- | ------------- | --- | --- |
ENEA   |   2024 Network Threat Detection Report   ©2024  Cybersecurity Insiders.  All Rights Reserved. 12

| ENHANCEMENTS |
Very High Confidence in AI’s Value
A striking 71% of respondents consider it very (38%) or extremely (33%) important for network threat
detection to incorporate AI. Another 23% consider it moderately important, with only 6% considering
it slightly important (4%) or not important (2%).
Part of this confidence may be tied to AI’s ability to rapidly analyze large volumes of network traffic
and detect subtle patterns or anomalies—especially within encrypted or highly complex traffic—that
are indicative of sophisticated attacks (which, in turn, increasingly employ AI).
However, given that the three top operational challenges for security teams are 1) the difficulty of
prioritizing alerts, 2) no (or poor) visibility into the global attack surface, and 3) unsatisfactory speed of
detection and response, it is logical to assume that security teams have faith that AI can be used to
address a wide variety of challenges.
How important do you think it is for network threat detection to incorporate AI for advanced
threat detection?
71% of respondents think it is very or extremely important
to incorporate AI for advanced threat detection
38%
23%
33%
4%
2%
Not at all important Extremely important
Not at all important Slightly important Moderately important Very important Extremely important
ENEA | 2024 Network Threat Detection Report ©2024 Cybersecurity Insiders. All Rights Reserved. 13

| ENHANCEMENTS |
Automatic Threat Scoring & Prioritization
Most-Valued Capability
Respondents place automation and simplification at the top of their must-have capabilities
for network threat detection solutions. 62% of respondents see automatic threat scoring and
prioritization as a must-have, while 59% value correlation of relevant data, events, and alerts into
single incidents. Close behind, 57% desire automated and/or guided response processes, and 53%
want their solution to automatically add contextual data to alerts.
Against this backdrop of a deep desire for automation, it is interesting to note that generative-AI (or
GenAI) assistance, which involves a collaborative dialogue between the security analyst and the AI
application, comes near the end of the must-haves. It is an indicator, perhaps, that full automation is
now valued more highly than interactive assistance.
What capabilities do you think are must-haves for a good network threat detection solution?
62% 59% 57% 53%
Automatically score Correlate relevant Automate and/or Automatically
and prioritize threats data/events/alerts guide response add contextual
to single incidents processes data to alerts
48% 41% 35% 31% 28% 14%
Integrate external Support threat Block known Generate Incorporate Support offline
threat intelligence hunting and threats MITRE ATT&CK generative-AI packet capture
sources forensics mappings assistance (pcap) processing
ENEA | 2024 Network Threat Detection Report ©2024 Cybersecurity Insiders. All Rights Reserved. 14

| ENHANCEMENTS |
Reduction in Breaches Tops KPI List
Respondents consider the reduction in the number of breaches as the most useful KPI for judging
threat detection effectiveness. In a network threat detection context, this does not mean blocking
threats at the perimeter, but rather finding and stopping infiltrations before data is accessed and
released, exfiltrated, or encrypted. And for this, one has to be aware of breaches in order to measure
their reduction over time, hence high rankings of reducing time from detection to resolution (63%),
increasing true positive detections - i.e., not missing actual threats (54%), and reducing false positives
(43%), which take valuable time away from finding and stopping legitimate threats.
What metric(s) do you think are most useful for evaluating the efficacy of a network threat
detection solution?
2 3
Reduction in Increase in
time from true positive 4
detection to detection rate
1 resolution Reduction
in false
Reduction in positive alerts
number
of breaches
54% 5
63% 43% Reduction in
total labor hours
37%
6
65% Improved staff
31% satisfaction
and retention
ENEA | 2024 Network Threat Detection Report ©2024 Cybersecurity Insiders. All Rights Reserved. 15

| PLANS |
Broad Expansion for Anomaly Detection
Network intrusion detection systems use two principal techniques for identifying breaches. One
analyzes traffic for specific patterns, or signatures, of known threats, while the other looks for
anomalous behaviors. The latter typically works by creating a baseline of what normal (safe) traffic
looks like, and then uses statistical and/or machine learning to detect anomalies indicative of a
breach or vulnerability.
Anomaly detection is used to a limited extent in conventional IDS/IPS but is a key pillar of NDR
solutions. It offers a more effective method of catching advanced threats than signatures, as hackers
rapidly adapt their techniques once an attack method is exposed and codified via a signature.
Reflecting confidence in this capacity to catch advanced attacks, 83% of all organizations say they
either currently use anomaly detection (17%) or plan to do so over the next 6-24 months (66%).
15% are uncertain of their organization’s intent to use it. Only 2% report no plans for using anomaly-
based network threat detection.
What are your plans regarding anomaly-based network threat detection capabilities
in your organization?
66% plan to implement
in 6-24months
14%
12-24 months
35%
next 12 months
17%
17%
15% 2%
next 6 months
Already Plans to Not sure No plans
implemented implement
ENEA | 2024 Network Threat Detection Report ©2024 Cybersecurity Insiders. All Rights Reserved. 16

| PREFERENCES |
IDS/IPS & Specialized NTD Tools Are Popular Choices
IDS/IPS is currently the most widely deployed network threat detection tool (43%). Two other
specialized threat detection tools, SIEM/SOAR and NDR/XDR, are more widely deployed than broader
platforms like Secure SD-WAN, SASE and SSE.
Which of the following are currently deployed at your organization?
40% 37%
NDR or XDR Secure SD-WAN
3 4
31%
41%
5 SASE
SIEM/SOAR 2
30%
6
Network monitoring
or observability platform
1
43% 7
IDS/IPS 8 18%
SSE
15%
CWP, CSPM &/or CNAPP
Furthermore, per the second question below, only a minority (36%) consider integration into a
broader, multi-functional security platform to be the most effective option for their organization,
while 59% cite one of three types of specialized NTD solutions (DPI-based NTA sensor, NDR, or XDR).
This may change as SASE and SSE adoption continues to grow, but it would not be surprising to see
continued deployment of best-of-breed NTD solutions alongside such platforms.
Which type of network threat detection deployment would be most effective for your organization?
Integrated into a multi-function security platform
36% PLATFORM
(e.g., SASE, SSE, Secure SD-WAN, ZTNA)
Integrated into standalone network traffic
28%
sensor(s) with Deep Packet Inspection (DPI)
18% Integrated into a specialized Network 59%
Detection & Response (NDR) platform
SPECIALIZED
Integrated into a specialized Extended
13% Threat Detection & Response (XDR)
solution offering both NDR and
Endpoint Detection & Response (EDR)
5% Unsure
ENEA | 2024 Network Threat Detection Report ©2024 Cybersecurity Insiders. All Rights Reserved. 17

| PREFERENCES |
Commercial NIDS Preferred over Open Source
Security professionals express a preference for commercial over open source solutions (41% vs 28%),
though 16% use both. The top three reasons for the commercial preference are performance and
scalability, customer support, and protocol coverage. It is important to note, however, that most
commercial NIDS/IPS are built upon an open source NIDS/IPS foundation. For example, the Enea
Qosmos Threat Detection SDK was developed in partnership with the Open Information Security
Foundation (OISF, Suricata’s maker). It tightly integrates core functionalities from Suricata with Enea’s
deep packet inspection engine, the Enea Qosmos ixEngine®, to help solution developers meet the
unique performance demands of commercial-grade deployments.
If you use a Network Intrusion Detection System (NIDS), is it open source or commercial?
28%
Open source
41%
Commercial
1166%%
Use both
3%
12%
Do not use NIDS
Not sure
What do you see as the top three reasons to use a commercial NIDS solution?
58%
Commercial-grade 46%
performance & scaling
Professional customer
support with SLAs
37%
Extended coverage 35%
of protocols & apps
Support for encrypted
traffic classification
29%
Integration of AI/ML 24%
for innovation
More secure than
open source
ENEA | 2024 Network Threat Detection Report ©2024 Cybersecurity Insiders. All Rights Reserved. 18

| PREFERENCES |
Snort & Suricata Most Popular Open Source NTD Tools
Snort is cited as the most frequently used open source NIDS, followed closely by Suricata. The
number three most commonly cited NIDS is Zeek. These tools have been around for a long time, and
all continue to evolve and to play an important role in protecting networks worldwide.
Created in 1998, Snort was originally developed as a packet sniffer and logger and evolved to support
signature- and anomaly-based intrusion detection. First released in 2010, Suricata was originally
developed as a signature-based NIDS/IPS, but over time has added some anomaly detection
and network security monitoring capabilities. First deployed in 1995, Zeek is a network security
monitoring tool but can be used to provide some NIDS functionality.
If you use an open source NIDS, which one?
55%
Snort
48%
Suricata
35%
Zeek
21%
OpenWIPS-ng
10%
Sguil
26%
We don’t use open
source NIDS
ENEA | 2024 Network Threat Detection Report ©2024 Cybersecurity Insiders. All Rights Reserved. 19

Methodology and Demographics
This 2024 Network Threat Detection Report is based on a comprehensive online survey of 327
cybersecurity professionals, conducted in September 2024, to gain deep insight into the latest trends,
key challenges, and solutions for network threat detection.
The survey utilized a methodology ensuring a diverse representation of respondents, from technical
executives to IT security practitioners, across various industries and organization sizes. This approach
ensures a holistic and balanced view of the insider threat landscape, capturing insights from different
organizational perspectives and experiences.
CAREER LEVEL
32% 24% 21% 11% 6% 4% 2%
Manager/Senior Manager Supervisor/Team Leader Entry-level/Individual Contributor Director/Senior Director
Vice President C-level Executive Other
DEPARTMENT
41% 17% 15% 14% 3% 10%
IT Operations IT Security Networking Engineering Compliance Other
INDUSTRY
32% 26% 14% 8% 7% 6% 7%
Technology Finance Healthcare Government/Public Sector Professional Services Education Other
COMPANY SIZE
8% 21% 25% 22% 7% 17%
Less than 50 employees 50-250 employees 251-1,000 employees 1,001-5,000 employees 5,001-10,000 employees
More than 10,000 employees
Reuse of content
We encourage the reuse of data, charts, and text published in this report under the terms of this Creative Commons
Attribution 4.0 International License. You’re free to share and make commercial use of this work as long as you
attribute the report as stipulated in the terms of the license. For example: “2024 Network Threat Detection Report by
Cybersecurity Insiders and Enea.”
ENEA | 2024 Network Threat Detection Report ©2024 Cybersecurity Insiders. All Rights Reserved. 20

About Arista Networks
Arista Networks is an industry leader in zero trust networking, delivering security and observability
across wired, wireless, and cloud infrastructure. Arista AVA™, an AI decision support system, enables
an integrated suite of security platforms for standards-based network access control, autonomous
threat hunting, and identity-aware microsegmentation. Importantly, these zero trust platforms are
built on network infrastructure powered by Arista EOS™ and NetDL™, avoiding network security
overlays and thus reducing costs while accelerating zero trust maturity and lowering breach impact.
Arista Networks has been recognized as a market leader by Gartner, Forrester, and KuppingerCole,
among others.
arista.com/security
About Enea
We are a world-leading specialist in advanced telecom and cybersecurity software with a vision
to make the world’s communications safer and more efficient. As the most widely deployed
Deep Packet Inspection (DPI) technology in cybersecurity and networking solutions, the Enea
Qosmos products classify traffic in real-time and provide granular information about network
activities. Enea also offers IDS-based threat detection capabilities as an SDK, enabling easy and
tight integration with cybersecurity solutions while remaining highly flexible and scalable. Enea is
headquartered in Stockholm, Sweden and is listed on NASDAQ Stockholm.
enea.com/dpi-tech
About Custocy
Custocy is a French spin-off from IMS Networks, specialised in cybersecurity software. Based in
Toulouse, in the Occitanie region, it has a Research and Development team of around fifteen PhDs
and engineers who have been developing an artificial intelligence engine since 2019. This engine
is integrated into a SaaS platform for Network Detection and Response. Custocy has established
a high-level collaboration with the LAAS-CNRS laboratory. Custocy is a laureate of the i-NOV
innovation competition as part of the French government’s France 2030 plan and Bpifrance. In
May 2024, Custocy was named “Product of the Year” at the Paris Cyber Show.
custocy.ai

Cybersecurity Insiders brings together 600,000+ IT security professionals
and world-class technology vendors to facilitate smart problem-solving and
collaboration in tackling today’s most critical cybersecurity challenges.
Our approach focuses on creating and curating unique content that educates
and informs cybersecurity professionals about the latest cybersecurity
trends, solutions, and best practices. From comprehensive research studies
and unbiased product reviews to practical e-guides, engaging webinars, and
educational articles - we are committed to providing resources that provide
evidence-based answers to today’s complex cybersecurity challenges.
For more information:
email us info@cybersecurity-insiders.com or visit cybersecurity-insiders.com
©2024 Cybersecurity Insiders. All Rights Reserved.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-08-28", "model": "gemini-3.5-flash-lite"} -->
