2025 SURVEY
State of ICS/OT
Security 2025
Written by Jason D. Christopher
November 2025
©2025 SANS™ Institute

Foreword
For nearly a decade, these surveys have tracked the industry’s
progress toward cybersecurity maturity and identified the key
drivers behind actions, both taken and not taken, within each
sector. In collaboration with industry experts, the SANS team
designs the survey to deliver actionable insights for readers.
In recent years, Jason Christopher has elevated this report to
a new level of excellence.
Over the years, the world has evolved: organizations have
deepened their capabilities, adversaries have adapted, and
expectations for corporate cybersecurity performance continue to
rise. Given this reality, both the survey questions and the analysis of
responses must mature to capture the nuances that matter most to
leaders shaping and advancing their programs.
In this year’s survey, Jason Christopher delivers a true masterclass
for the industry, capturing historical trends, identifying This report is essential
the current state of the field, and forecasting where it’s
reading for anyone in a
heading. His work provides the ICS/OT community with
leadership role across critical
valuable context on where peers stand today, why, and
where they go next. infrastructure environments.
I am excited to see how leaders across the industry
put these insights into action, and I look forward to watching this
survey continue to evolve as a vital tool in the defense of critical
infrastructure worldwide!
Tim Conway
SANS Fellow
State of ICS/OT Security 2025 2

SANS 2025 STATE OF ICS/OT SECURITY SURVEY
Key Findings
Incidents remain high and disruptive.
More than one in five organizations (22%) reported a cybersecurity
incident in the past year, with 40% causing operational disruption and
nearly 20% taking over a month to remediate.
Detection is improving, but recovery lags.
Nearly half of incidents were detected within 24 hours and 60% contained
within 48 hours, yet remediation often stretches into days or weeks (and
can even take over a year).
Regulation drives maturity.
Sites under mandatory compliance had similar incident rates as peers but
experienced ~50% fewer financial losses and safety impacts.
Threat intelligence pays dividends.
Organizations leveraging ICS-specific threat intelligence were more likely to
adjust defensive priorities—improving monitoring, segmentation, and detection.
Remote access remains a top risk.
Unauthorized external access accounted for half of all incidents, yet only 13%
of organizations have fully implemented advanced controls such as session
recording or ICS/OT-aware access.
Preparedness is uneven.
Just 14% of respondents felt fully prepared for emerging threats, but those
that included frontline technicians in exercises were nearly 1.7 times more
likely to report strong readiness.
Investment momentum is clear.
Asset visibility, threat detection, and secure remote access dominate both
2025 deployments and 2026–2027 planned investments, showing where
organizations see the greatest value.

Survey Author
Jason Christopher Over the past 20 years, Jason D. Christopher has worked
SANS Certified Instructor across multiple industries in unique roles ranging from
engineering to incident response and national security.
Most notably, Jason was the federal technical lead for
CURRENTLY TEACHING
the NERC CIPv5 while at the Federal Energy Regulatory
ICS418: ICS Security Essentials
Commission, where he was involved in several rulemakings
for Leaders
and policy statements. Jason was also the program lead
ICS456: Essentials for
for the US Department of Energy Cybersecurity Capability
NERC Critical Infrastructure
VIEW PROFILE Maturity Model (C2M2). He has served as a C-level executive,
Protection
security researcher, and incident responder across his
career. He previously held the role of director of Cyber Risk
for Dragos, Inc. Today, Jason is the senior vice president
of Cybersecurity and Digital Transformation for Research
and Innovation at Energy Impact Partners (EIP), a $4 billion
global investment firm custom-built to invest in the energy
transition. Jason has been invited to speak before the US
Congress on several occasions.
Robert M. Lee
Expert Corner
SANS Faculty Fellow
The 2025 SANS State of ICS/OT Security Survey rightfully highlights the
increasing frequency of disruptive incidents to OT organizations despite COURSES TAUGHT
these incidents going underreported in media and traditional sources. ICS310: ICS Cybersecurity
Practitioners in this space have long understood that when we look
Foundations
more we start to find more; threats have gone undetected for far too
long and we’ve had more “near misses” in the community than we can VIEW PROFILE ICS515: ICS Visibility, Detection,
afford in the future. Leveraging the SANS ICS Five Critical Controls is a and Response
great baseline for organizations to follow to enhance their security
FOR578: Cyber Threat Intelligence
posture without overspending against the risk. Government leaders and
policymakers, board of director members, and OT cybersecurity
practitioners are chiefly aware that we have broadly underinvested in
the portion of our businesses that generates revenue and where our
local and national security interests reside. It is imperative to influence
the mindsets outside of these circles and in the traditional enterprise IT
security leaders to highlight the rapid and appropriate investments
necessary to protect our communities.
SSttaattee ooff IICCSS//OOTT SSeeccuurriittyy 22002255 44

Introduction
Since 2017, the SANS State of ICS/OT Security Survey has tracked the practices, challenges,
and progress of organizations securing critical infrastructure worldwide. Over nearly a
decade, these annual benchmarks have documented how the industry has matured—from
ad-hoc protection measures to more structured programs shaped by regulation, threat
intelligence, and incident response lessons learned.
This year’s survey, based on responses from 330 professionals across diverse industrial
sectors, arrives at a pivotal moment. Threat activity against operational environments
continues to rise, with ransomware, supply chain compromise, and nation-state alignment
shaping the landscape. At the same time, regulatory mandates are expanding in scope and
enforcement, requiring organizations to demonstrate not just compliance but resilience.
The report explores the state of ICS/OT security through three lenses: past trends, current
practices, and future plans—offering practitioners, executives, and policymakers a clear
view of progress, gaps, and the actions needed to build sustainable, resilient operations.
See Figure 1 for the full demographics.
Top 4 Industries
Represented
16%
| 20% |     | 10% | 9%  |
| --- | --- | --- | --- |
Information
| Energy | Technology | Other | Government |
| ------ | ---------- | ----- | ---------- |
Regions
| 248 Ops       | 130 Ops | 116 Ops | 112 Ops |
| ------------- | ------- | ------- | ------- |
| 183 HQs       | 58 HQs  | 27 HQs  | 22 HQs  |
| United States | Europe  | Canada  | Asia    |
Top 4 Roles
Represented
8%
| 10% | 9%  |     | 8%  |
| --- | --- | --- | --- |
Security
ICS/OT Cybersecurity  ICS/OT Cybersecurity  Administrator/ ICS/OT Security
| Analyst | Manager | Security Analyst | Architect |
| ------- | ------- | ---------------- | --------- |
Figure 1. Demographics
State of ICS/OT Security 2025  5

2025 Trends: Increased Threats and
Evolving Regulations
Historically, ICS/OT cybersecurity programs have responded to two major external factors:
threats and regulations. As explored in previous years, the most mature organizations for
industrial security leverage ICS-specific threat intelligence and standards. This year’s data
supports those findings, as organizations that leverage both continue to demonstrate
quicker detection, containment, and remediation during a cybersecurity incident.
Industrial Cyber Incidents
Similar to previous years, 22% of respondents suffered a cybersecurity incident. Of those,
a majority (50%) came from unauthorized external access and/or ransomware (38%). A full
breakdown of threat actors can be found in Figure 2.
Did your organization experience any security incidents in your ICS/OT
environment in the past 12 months?
Unauthorized access (external actor) 50%
Insider misuse or error 41%
Yes, one, or more
confirmed incidents 15% Ransomware 38%
Malicious code detection 33%
8%
No known incidents
Supply chain compromise (e.g., third-
22% 30%
party breach, software tampering)
Unknown/Unsure Data loss or modification 21%
Engineering system
15%
Unable to answer due degradation or outage
to company policy 55%
Safety or reliability event triggered 8%
Other 5%
Figure 2. ICS/OT Security
These incidents have real-world impacts, with 40% of incidents causing a disruption in
Incidents by Type
ICS/OT operations, 13% resulting in financial losses or data compromise, 8% posing a risk to
physical safety or reliability, and 6% involving the theft of intellectual property. Interestingly,
regulated sites had roughly the same amount of ICS/OT incidents but both financial
losses and risks to physical safety impacts were ~50% less than their unregulated peers.
State of ICS/OT Security 2025 6

Actions an Attacker Takes to Compromise an ICS Facility
ICS attack
Attacker IT Attacker action ICS capability Attack ICS attack Attack adjustments execution
entry point pivot to ICS development validation delivery and modifications
ICS Compromise-to-Detection Gap
Detection-to-Containment Gap
Containment-to-
Remediation Gap
Common IT ICS asset hardening ICS threat Incident Recover operational
security controls and controls detection declared integrity
Traditional ICS ICS situational awareness Containment and
perimeter controls and data protection eradication
Actions the Defender Takes and/or is Reliant on to Thwart the Attack
Figure 3. ICS Cyber Incident Timeline
As we teach across the SANS ICS curriculum, incident timelines can be broken into
three distinct stages, as shown in Figure 3:
1. Compromise-to-detection
2. Detection-to-containment
3. Containment-to-remediation
The distributions for these timelines across the 2025 participants that suffered an
ICS/OT cyber incident can be found in Figure 4.
Compromise-to-Detection Gap
27%
22%
14% 13%
8% 8%
3% 2% 2% 2%
<6 hours 6–24 hours 2–7 days 8–30 days 1–3 months 4–6 months 7–12 months 1 year Over a year Unknown
Detection-to-Containment Gap
40%
25%
13%
8%
5% 5%
3% 2%
0% 0%
<6 hours 6–24 hours 2–7 days 8–30 days 1–3 months 4–6 months 7–12 months 1 year Over a year Unknown
Containment-to-Remediation Gap
24%
22%
13% 14% 13%
8%
2% 2% 3%
0%
<6 hours 6–24 hours 2–7 days 8–30 days 1–3 months 4–6 months 7–12 months 1 year Over a year Unknown
Figure 4. ICS Cyber Incident Timeline Distributions for 2025
State of ICS/OT Security 2025 7

Two trends have maintained from previous years. First, industry continues to improve in
detection times for ICS/OT incidents, with nearly 50% of incidents being detected within
the first 24 hours. Second, we are similarly improving on containment, with over 65%
of detection-to-containment gaps being addressed in the proceeding 24 hours. That
means, on average, ICS/OT incidents are detected and contained within 48 hours.
That, however, is where the good news ends. Remediation, which includes the act of
eradicating the threat and recovering operational integrity, still takes days to achieve, on
average, with 22% taking two to seven days to recover. The risks here are real, with 19% of
incidents in 2025 taking over a month to remediate (and a striking 3% taking over a year).
Preparation is still key to responding and recovering quickly during
Without an ICS/OT-specific incident
an industrial cyber incident. 57% of respondents have a dedicated
response plan, most organizations
ICS/OT incident response plan, a minor increase from previous years
take up to a week just to detect an
that represents further maturity across the industry. If an organization
incident. Annual testing can cut that
has both threat intelligence capabilities and is regulated, the coverage
for ICS/OT-specific incident response plans jumps to 70%. timeline down to hours.
Most organizations (39%) test their incident response plan annually.
While this decreased from previous years, that is because we saw a sharp increase in
the number of organizations that are now testing their incident response plan quarterly
(25%). Interestingly, those that perform more regular incident response testing also have
more variety in the ways they test, and they are far more likely to have operational drills,
red and purple team exercises,
and executive-level tabletops— What methods are used to test the incident response plan?
ensuring a wide range of training Select all that apply.
and practical experience for
Paper-based tabletop exercises 68%
responders. A full breakdown of
Operational drills (onsite) 47%
testing methods can be found in
Technical simulations
Figure 5. 44%
(e.g., red/purple teaming, cyber range)
Executive- or board-level
Nearly 80% of respondents with scenario exercises 41%
incident response plans updated Other 3%
them in 2025. Beyond changes in
Figure 5. ICS/OT Incident
the organization or technology used for incident response there were two major drivers Response Testing
for these updates: threat intelligence (41%) and regulatory changes or audit feedback
(40%). This once again highlights how industrial cybersecurity is impacted by both
external forces.
State of ICS/OT Security 2025 8

ICS/OT-Specific Threats, Intelligence, and Information Sharing
Starting with threat intelligence, 67% of respondents leverage threat intelligence
in some capacity, with an additional 16% planning to use it over the next year. The
majority (79%) of threat intelligence programs for ICS/OT environments are built on
vendor-provided intelligence feeds, with government and public reporting sources
coming in at a close second (77%) along with peers or industry information sharing
and analysis centers (ISACs) (72%).
On ISACs in particular, there is room for improvement across industrial sectors with
only a minority (22%) of participants actively contributing information and a third (34%)
primarily consuming information without additional collaboration. For programs that
rely heavily on ISACs or peer information sharing, there may be a false sense of security
regarding the sample size of peers providing threat and vulnerability data.
That said, respondents that
What value has your organization gained from participation in
participate in information
these ICS/OT information sharing activities? Select all that apply.
sharing activities noted clear
benefits and measurable value
Early awareness of threats or vulnerabilities 63%
for these activities, as seen in
Strategic planning or risk prioritization 50%
Figure 6.
Improved detection engineering
48%
or threat hunting
Although threat intelligence
Building trust and relationships within the sector 47%
and information sharing are
separate activities, they both add Enhanced incident response preparedness 39%
to how industrial organizations No measurable value yet 7%
categorize and monitor threats
Figure 6. Observed Value of ICS/OT Information Sharing
and, as mentioned, adapt their incident response capabilities.
Based on these activities, respondents have seen an increase in
ransomware targeting OT environments (64%), nation-state-aligned
threats (57%) and supply chain compromises (52%) over the past year.
Similar to incident response,
Has your organization adjusted any defensive priorities in
these threat trends further
response to threat intel in the past year? Select all that apply.
inform defensive priorities, as
seen in Figure 7, where some Updated detection logic or rules 58%
clear benefits to increasing
Changed asset monitoring coverage 53%
asset monitoring (53%) or
Accelerated segmentation or
49%
architecture improvements
accelerating segmentation or
Flagged new training or awareness needs 47%
architecture improvements (49%)
were a direct result of threat Prioritized tabletop or scenario planning 31%
intelligence. Flagged a specific vendor or 24%
software for reassessment
No changes made based on threat intel 9%
Other 2%
Figure 7. Threat-Informed Defensive Priorities
State of ICS/OT Security 2025 9

ICS-Specific Security Regulations
Across the SANS ICS curriculum, we have noted the increase in ICS/OT cybersecurity-
specific regulations over the past few years.1 It therefore came as no surprise that
58% of respondents reported having at least one facility subject to mandatory
cybersecurity compliance requirements. Of that group, 26% reported having a possible
violation from an audit or self-report. Smaller compliance programs (fewer than 10
facilities in scope) were mostly impacted, accounting for nearly 40% of those possible
violations, indicating a possible need for additional resources in those environments.
Similar to threat intelligence,
these compliance programs Which of the following areas have seen investment due
have direct impact on to compliance-driven priorities? Select all that apply.
investment priorities for
Logging, monitoring, and
72%
detection capabilities
industrial organizations, as
Asset inventory and management tools 67%
seen in Figure 8.
Secure remote access platforms 52%
Regulations have had some
Risk assessments or third-party reviews 50%
clear benefits to programmatic
improvement, including Vulnerability management tools 50%
executive-level visibility and Incident response documentation 40%
or tabletop planning
capabilities being prioritized.
Workforce training 39%
Although there are some
Process improvements 31%
pain points around evidence
Document management/evidence
30%
collection, many of these collection improvements
priorities are widely considered None 4%
to be beneficial to overall Other 1%
ICS/OT cybersecurity.
Figure 8. Compliance-Driven
Investment Priorities
Detecting Today’s Threats and Managing Vulnerabilities
Detection capabilities were a common theme across the 2025 data. They are the
No. 1 prioritized response for threat intelligence (58% of respondents update threat
detections based on intel) and compliance programs (72% have
increased investment in logging, monitoring, and detection due to Only one in eight organizations report full
regulations). Increased detection also leads to improved incident ICS Kill Chain visibility—but those that
response metrics. achieve it almost always run a SOC with IT
The 2025 State of ICS/OT Security Survey highlights the old phrase and OT sharing detection tools.
“protection is ideal, detection is a must.”
1 A more in-depth breakdown can be found in our 2023 SANS ICS Summit presentations: www.youtube.com/watch?v=3mhkEJ9QrL4
State of ICS/OT Security 2025 10

Unfortunately, there is a lot of improvement required to improve on ICS/OT detection and
its relationship to threats and real-world incidents. When asked, only 13% of respondents
reported having full visibility across the ICS Cyber Kill Chain with a clear majority (42%)
reporting partial visibility with major gaps.2 The remaining 31% reported minimal or no
alignment across IT and ICS/OT environments to provide visibility across the entire kill chain
(from initial access to ICS/OT impacts).
Compounding this issue, only 49% of respondents have ICS/OT-specific detection with
significant gaps in capabilities as seen in Figure 9. Of those with detection, only 26% describe
their capabilities as “highly effective” in identifying ICS-relevant threats with a majority
(53%) describing their detection program as “moderately effective,” highlighting areas for
improvement both in terms of coverage and actionability with their current investments.
Are you using ICS/OT-specific What types of ICS/OT-specific detection capabilities
detection capabilities? are currently in use? Select all that apply.
Protocol-aware anomaly detection 75%
Yes
Passive visibility tools 68%
16%
Signature/IOC detection
No, but we are specific to OT environments 64%
planning on these
Host-based detection on engineering
capabilities in 59%
11% workstations or servers
the next 12 to 24
months
49%
Active visibility tools
(where safe and possible without 35%
negative impacts to operations)
N
no
o ,
p
a
l
n
an
d
s
we have
24%
D
bu
e
i
t
l
e
t
c
f
t
o
io
r
n
IT
p
, a
la
d
t
a
fo
p
r
t
m
ed
s
f
o
o
r
r
i g
O
in
T
ally
30%
Custom-developed detection logic
26%
(e.g., internal baselines, rules)
Unknown/unsure
Other 1%
Figure 9. ICS/OT Detection
Organizations that have achieved some level of visibility across the ICS Cyber Kill
Capabilities
Chain largely do so through coordinated, but separate, IT and OT teams with shared
log aggregation and correlation
tools, as seen in Figure 10. How is IT/OT visibility and monitoring integration performed
in your organization? Select all that apply.
Although a security operations
center (SOC) is not necessary Coordinated but separate
50%
IT and OT teams
for visibility, most organizations
Shared log aggregation and
48%
find the constructs useful for correlation tools (e.g., SIEM)
Shared detection tools/platforms 42%
aligning capabilities. A majority
(57%) of respondents either have Joint alert triage or escalation processes 35%
a single IT-OT SOC or a parallel Manual or ad hoc coordination only 29%
OT-specific SOC, with another No integration between IT
8%
and OT monitoring
23% performing centralized
Other 3%
monitoring without a SOC.
Figure 10. Integration of IT and OT Visibility
2 More information about the Industrial Control System Cyber Kill Chain can be found at www.sans.org/white-papers/36297
State of ICS/OT Security 2025 11

Cloud and Secure Remote Access
As previously explored, 50% of incidents reported in the 2025 survey
originated from unauthorized external access. External access
can come in many forms, and
cloud access, in particular,  What extent are cloud-connected environments
integrated into your organization’s IT/OT security
has certainly become an
monitoring or visibility strategy?
increasing part of everyday life
for industrial operations. Only
| 17% of respondents reported  | 13% | 29% |     | 29% | 9% 17% | 4%  |
| ---------------------------- | --- | --- | --- | --- | ------ | --- |
no cloud usage in their ICS/OT
|     | 0%  | 20% | 40% | 60% | 80% | 100% |
| --- | --- | --- | --- | --- | --- | ---- |
environments or IT networks,
  Fully integrated,cloud activity is monitored    Not integrated,cloud-connected assets are not
meaning 83% of respondents  alongside IT and/or OT actively monitored
need to actively integrate cloud    Largely integrated, cloud activity is monitored    No cloud use in ICS/OT or IT environments
alongside IT and/or OT, but there are gaps
| visibility to monitor for threats.  |     |     |     |   Unknown/unsure |     |     |
| ----------------------------------- | --- | --- | --- | ---------------- | --- | --- |
  Partially integrated, only some cloud activity
As seen in Figure 11, there are
is visible
some coverage concerns as only
Figure 11. Cloud Monitoring Across IT/OT Networks
13% reported fully integrated visibility and cloud monitoring for
ICS/OT or IT networks. The majority (58%) report gaps or minimal
coverage for cloud, which may
have direct and persistent
What visibility or security measures are in place to monitor
access to the ICS/OT network. cloud-connected systems? Select all that apply.
When monitoring of the cloud
|     | Cloud-native logging or telemetry  |     |     |     |     | 46% |
| --- | ---------------------------------- | --- | --- | --- | --- | --- |
platforms (e.g., CloudTrail, Azure Monitor)
environment is performed,
|                             | Ingesting cloud logs into existing SEIM  |     |     |     | 39% |     |
| --------------------------- | ---------------------------------------- | --- | --- | --- | --- | --- |
| there is no clear “winner”  | or SOAR alongside IT/OT logs and data    |     |     |     |     |     |
Ingesting cloud logs into existing
| regarding capabilities, as  |     |     |     |     | 32% |     |
| --------------------------- | --- | --- | --- | --- | --- | --- |
IT/OT detection platforms
| outlined in Figure 12, with  | Dedicated third-party monitoring  |     |     |     |     |     |
| ---------------------------- | --------------------------------- | --- | --- | --- | --- | --- |
31%
tools or agents for cloud assets
cloud-native logging or
|     | Unknown/unsure |     |     | 14% |     |     |
| --- | -------------- | --- | --- | --- | --- | --- |
telemetry as the most popular
No active monitoring of
|     | cloud-connected environments |     |     | 11% |     |     |
| --- | ---------------------------- | --- | --- | --- | --- | --- |
solution (46%) and dedicated
|     | Other |     | 2%  |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- |
third-party monitoring tools
and agents the least (31%).  Figure 12. Cloud Monitoring Capabilities
State of ICS/OT Security 2025  12

Secure remote access continues to be a challenge for ICS/OT environments.
Although industry has improved with multifactor authentication (MFA),
there are still plenty of coverage gaps and capabilities missing in standard
deployments, as highlighted in Figure 13.
What is the level of coverage for the following secure remote
access controls across your ICS/OT access points?
Remote access segmentation
|     |     |     |     | 32% |     | 27% |     | 18% | 11% | 6%  | 7%  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(e.g., OT DMZ or dedicated gateway)
ICS-specific protocol or device awareness/access   13% 22% 23% 26% 9% 8%
(beyond engineering workstation access)
Vendor-managed or third-party access restrictions 21% 26% 25% 11% 6% 11%
| MFA enforcement |     |     |     | 30% |     | 25% |     | 22% | 11% | 5%  | 8%  |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Timeout or auto-disconnect configuration 20% 23% 25% 16% 8% 8%
| Session recording and replay |     |     | 12% | 15% |     | 23% |     | 33% |     | 9%  | 8%  |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Session logging              |     |     | 23% |     | 21% |     | 29% |     | 13% | 6%  | 8%  |
| Real-time session approval   |     |     | 13% | 18% |     | 23% |     | 30% |     | 7%  | 9%  |
 Session brokering or jump host enforcement 24% 19% 25% 16% 8% 8%
|     |                                 | 0%  |     | 20%                       |     | 40% | 60%              |     | 80% |     | 100% |
| --- | ------------------------------- | --- | --- | ------------------------- | --- | --- | ---------------- | --- | --- | --- | ---- |
|     |   Fully implemented across all  |     |     |   Partially implemented   |     |     |   Unknown/unsure |     |     |     |      |
|     | ICS/OT remote access points     |     |     | (less than 50% coverage)  |     |     |                  |     |     |     |      |
  N/A (no response)
|     |   Largely implemented   |     |     |   Not implemented |     |     |     |     |     |     |     |
| --- | ----------------------- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
(more than 50% coverage)
Figure 13. ICS/OT Secure Remote
Standard practices, like remote access segmentation, MFA, and vendor-
Access Capabilities
managed/third-party access restrictions, are all fairly high in level of
implementation. These capabilities are all drastically increased when
looking at regulated sites, where there are common secure
Half of 2025 incidents began with external
remote access mandatory compliance obligations. There
access. Yet fewer than 15% of organizations
are still plenty of industrial environments, however, that
have advanced remote access controls in place.
may benefit from exploring ICS-specific protocol or device
awareness/access, session recording and replay, and  This remains the weakest link.
real-time session approvals, which were all reported as
“fully implemented” by 13% or less across the 2025 survey respondents.
Considering the high degree of real-world incidents stemming
from remote access, these capabilities may benefit many industrial
organizations as they plan for increased cyber defenses.
| State of ICS/OT Security 2025  |     |     |     |     |     |     |     |     |     |     | 13  |
| ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

When asked what is preventing
What factors have prevented full implementation of secure remote
organizations from achieving
access controls across ICS/OT environments? Select all that apply.
full implementation of secure
Lack of internal resources
| remote access controls across  |     |     |     |     |     |     |     |     |     | 60% |
| ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(time, budget, personnel)
ICS/OT environments, the top
|     |     | Legacy system compatibility limitations |     |     |     |     |     |     | 46% |     |
| --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
blocker was lack of internal
Organizational misalignment
35%
| resources (60%), followed by  |     | (e.g., unclear ownership between IT and OT) |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Vendor or third-party resistance
27%
| legacy system compatibility        |     | to new access controls                   |     |     |     |     |     |     |     |     |
| ---------------------------------- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|                                    |     | Security policy exists, but              |     |     |     |     |     | 26% |     |     |
| limitations (46%), as reported in  |     | enforcement is inconsistent              |     |     |     |     |     |     |     |     |
| Figure 14.                         |     | Perceived risk of operational disruption |     |     |     |     |     | 26% |     |     |
Difficulty integrating remote access
| Combined with the fact that  |     |     |     |     |     |     | 23% |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tools with existing ICS architecture
| roughly one-third (31%) of  |     | No formal secure remote  |     |     |     |     |     |     |     |     |
| --------------------------- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
7%
access policy in place
respondents have no formal
|     |     | Other |     |     |     | 6%  |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
centralized inventory—or no
Figure 14. ICS/OT Secure Remote
inventory at all—of active ICS/OT
Access Blockers
remote access points, there is an obvious divide between the “haves” and the “have-
nots” in the world of secure remote access for industrial environments. As threats
evolve and real-world incidents continue to target these assets, many organizations
should prioritize these capabilities and provide adequate resources for teams
requiring remote access.
Planning for Tomorrow’s Cyber Risks
Further examining industrial organizations and threat intelligence, it is apparent that
ICS/OT cybersecurity professionals believe, by wide margins (as shown in Figure 15),
that industrial systems are more likely to be targeted than in previous years.
Based on threat intel received, which of the following ICS/OT environments or
technologies do you believe are now more likely to be targeted?
| Edge/IoT-connected ICS devices      |     |     |     | 60% |     |     |     | 24% | 3%     | 13% |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- |
| Legacy control systems              |     |     |     | 54% |     |     |     | 31% | 4%     | 11% |
| Cloud-connected OT data platforms   |     |     |     | 53% |     |     |     | 24% | 4% 19% |     |
| Remote facilities or unmanned sites |     |     |     | 48% |     |     | 32% |     | 4% 16% |     |
Field service laptops or third-party equipment 44% 38% 7% 11%
|     |     |     |     | 39% |     |     | 40% |     | 7% 15% |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- |
Engineering workstations or historian servers
| Safety systems (SIS) |                                  |     | 24%                       |     |                                  | 51% |     |       | 7% 19% |      |
| -------------------- | -------------------------------- | --- | ------------------------- | --- | -------------------------------- | --- | --- | ----- | ------ | ---- |
|                      |                                  | 0%  |                           | 20% | 40%                              |     | 60% |       | 80%    | 100% |
|                      |  More targeted than before       |     |  No change observed       |     |  Less targeted than before       |     |     |  N/A  |        |      |
Figure 15. Threat-Focused ICS/OT Targets
|     | State of ICS/OT Security 2025  |     |     |     |     |     |     |     |     | 14  |
| --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Exploring future threat
What types of threat scenarios has your organization considered
scenarios can be challenging,
in planning or preparedness exercises? Select all that apply.
but a majority (60%) of
respondents base their Ransomware targeting OT environments 72%
preparedness on industry Supply chain compromise
67%
(e.g., trusted vendor or integrator access)
threat intelligence and
Insider threat from engineering
60%
or operations personnel
reports, followed by real-world
Simultaneous IT and OT compromise 57%
incidents (54% of respondents).
Geopolitical escalation leading to
Unsurprisingly, as seen in Figure critical infrastructure being targeted 45%
16, the most popular scenario Physical sabotage or blended 41%
physical-cyber attacks
is ransomware targeting OT AI-enabled threat automation
32%
or impersonation
environments with 72% of
Other 2%
respondents having considered
Figure 16. Cyber Threat Scenarios
the impacts as part of their
Used for Planning and Preparedness
planning or preparedness exercises.
Combined with the previously
How prepared is your organization to respond to future cyber
reported trend on increased
threats targeting ICS/OT environments?
threat information regarding
ICS/OT targets, it is apparent that
threat capabilities and targeting 14% 33% 37% 9% 8%
efforts have continued to grow
0% 20% 40% 60% 80% 100%
across industrial environments.
Fully prepared Largely prepared Partially prepared Not prepared Unknown/unsure
Unfortunately, when asked
Figure 17. Perspective on Future Cyber
how prepared organizations are to respond to future threats, only 14%
Threats and Preparedness
felt that they were fully prepared for a range of plausible and emerging
threats. As seen in Figure 17, respondents are clearly divided between
feeling fully or largely prepared (47%) and partially or not prepared (46%).
Dean Parsons
Expert Corner
SANS Principal Instructor
The data proves what ICS/OT cybersecurity defenders and engineering
staff know about protecting our critical infrastructure: Engineering- COURSES TAUGHT
informed cyber preparedness cannot be siloed. It must extend across ICS418: ICS Security Essentials
the entire plant floor and engineering operations. Involving field
for Leaders
technicians, engineers, and operators in ICS/OT tabletop exercises and
industrial incident response planning nearly doubles the likelihood that VIEW PROFILE ICS515: ICS Visibility, Detection,
an organization with ICS/OT is ready to face emerging threats that can and Response
directly impact safety. That’s no coincidence. Those closest to the
control loops, HMIs, and PLCs understand better than anyone how cyber
incidents ripple into safety, reliability, and process integrity. By
embedding engineering staff and having them lead the way into ICS/OT
cybersecurity exercises, ICS/OT organizations and critical infrastructure
operations transform preparedness from a compliance checkbox into a
true resilience capability. One that protects the operational
environment as well as continuity and human safety. After all, in an
organization that has ICS/OT, the ICS/OT is the business.
State of ICS/OT Security 2025 15

Cyber preparedness requires
Which group of stakeholders is involved in tabletops,
collaboration across multiple
after action reporting, or other threat-aware activities
stakeholders ranging from
specific to ICS/OT cybersecurity? Select all that apply.
executives to managers to
external partners. When asked
ICS/OT security team 71%
which groups were involved in
63%
Enterprise IT security team
tabletops, after action reporting,
|     | Engineers and operators |     |     | 62% |
| --- | ----------------------- | --- | --- | --- |
or other threat-aware activities
| to specific ICS/OT cyber risks,  | Directors and managers |     |     | 58% |
| -------------------------------- | ---------------------- | --- | --- | --- |
respondents largely deferred to
|     | Executive leadership (VP/C-level) |     | 37% |     |
| --- | --------------------------------- | --- | --- | --- |
ICS/OT security teams, enterprise
|     | Field technicians |     | 30% |     |
| --- | ----------------- | --- | --- | --- |
IT, and engineers/operators, as
Regulatory/compliance stakeholders
| seen in Figure 18.  | (internal audit, legal, etc.) |     | 26% |     |
| ------------------- | ----------------------------- | --- | --- | --- |
|                     | System vendors/OEMs           | 19% |     |     |
Those organizations that felt
“fully prepared” shared unique  Integration partners/consultants 17%
| characteristics, including  | External service providers  |     |     |     |
| --------------------------- | --------------------------- | --- | --- | --- |
17%
(MSSPs, MDR, IR)
being 66% more likely to
|     | Media relations | 12% |     |     |
| --- | --------------- | --- | --- | --- |
include field technicians in
| their preparedness exercises.  | Federal agencies | 10% |     |     |
| ------------------------------ | ---------------- | --- | --- | --- |
| They also were almost four     |                  | 10% |     |     |
ISACs, ISAOs, and/or CERTs
times more likely to have full
|     | Local law enforcement | 9%  |     |     |
| --- | --------------------- | --- | --- | --- |
visibility across the ICS Cyber
|     | Board members | 7%  |     |     |
| --- | ------------- | --- | --- | --- |
Kill Chain and maintained more
| secure remote access controls.  | Major customer/account representatives | 5%  |     |     |
| ------------------------------- | -------------------------------------- | --- | --- | --- |
Another notable difference is
|     | Other | 1%  |     |     |
| --- | ----- | --- | --- | --- |
that a majority (57%) of these
Figure 18. Stakeholders Involved in
organizations actively contribute
ICS/OT Cyber Preparedness Activities
to information sharing.
ICS/OT Threat Hunting and Red/Purple Exercises
As previously discussed, tabletops and specific ICS/OT cybersecurity scenarios are
valuable preparedness tools when examining future threats. However, on the more
technical end of the spectrum, organizations should also consider ICS/OT threat
hunts and red (or purple) team exercises.
Do you want to boost preparedness?
ICS/OT threat hunting is a proactive, hypothesis-driven search for stealthy
Involve field technicians. Fully
adversary activity or unsafe changes in industrial environments. Analysts
prepared organizations were seven
pivot through ICS-specific evidence, such as PLC/HMI logs, historian data,
engineering-workstation activity, and protocol captures (e.g., Modbus,  times more likely to engage them in
DNP3), all under strict safety and change control. Complementing this,
exercises than their peers.
ICS/OT red teams safely emulate real-world attacker paths from IT to OT
to test segmentation, remote access, and response. This can be done under safe
conditions at production sites, but is often conducted in a lab, digital twin, or tightly
controlled window to avoid process impact. Purple teaming adds a collaborative
loop: Red teams and defenders iterate in real time to tune detections, playbooks,
and monitoring for ICS-specific behaviors.
State of ICS/OT Security 2025  16

Although generally
Organizations that perform (or plan to perform) ICS/OT threat
considered a mature
hunting and red/purple team exercises
set of practices,
many organizations
Red/purple 21% 21% 40% 19%
can benefit from the teaming
technical information
(and after-action items) Threat 21% 31% 31% 17%
hunting
that come from a
0% 20% 40% 60% 80% 100%
completed threat hunt
or red/purple team Yes No, but planning in next 12 months No, not planned Unknown/unsure
exercise. Unfortunately, Figure 19. Preparedness Activities
Performed or Planned
as seen in Figure 19, only one in five respondents reported performing either
preparedness activity.
Again, the organizations that identified themselves as being fully prepared for
future cyber threats are at the top end for either, with over 55% performing ICS/OT
threat hunts today and nearly half (48%) performing red or purple team exercises.
By the Levels: Detection and Proactive Capabilities in the
Purdue Model
In the 2025 survey, we wanted to further explore how mature certain capabilities
were across the Purdue Model,3 namely:
• ICS/OT-specific detection
• Risk-based vulnerability management
• ICS/OT threat hunting
• Safety-minded penetration testing (red/purple team exercises)
To do so, we asked about coverage across each. For example, if ICS/OT-specific
detection was in place, what was the degree of visibility across each level of the
Purdue Model?
A comprehensive breakdown can be found in Figure 20 (seen on the next page)
and the data provides some insights into the gaps across ICS/OT security programs.
For example, while 49% of respondents reported having ICS/OT-specific detection
capabilities, most do not have full visibility across their environments. Only 20%
report full visibility at Level 3, which drops in half to 10% for Level 2. Remote sites
similarly lack in any significant level of visibility with 18% reporting visibility as
largely or fully covered by their ICS/OT visibility program.
3 A more complete discussion of the Purdue Model can be found in the Appendix.
State of ICS/OT Security 2025 17

And detection is,
ICS/OT Capabilities by Coverage for Each Level of the Purdue Model
by far, the most
| mature capability         | Detection      |     |     | 28% |       | 13% | 3%  | 37% |     | 19% |     |
| ------------------------- | -------------- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
| discussed in this year’s  | Vulnerability  |     |     |     |       |     |     |     |     |     |     |
|                           | 4 LEVEL        |     | 18% |     | 9% 4% |     |     | 55% |     | 13% |     |
management
survey. Vulnerability
|     | Threat hunting |     | 11% | 6% 4% |     |     |     | 62% |     | 17% |     |
| --- | -------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
management has
| moderate coverage  | Pentesting |     | 9% 4% | 6%  |     |     | 62% |     |     | 19% |      |
| ------------------ | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | ---- |
|                    |            | 0%  |       | 20% |     | 40% |     | 60% | 80% |     | 100% |
across the higher levels
|                       |           |     | 23% |     | 15% | 6%  |     | 39% |     | 18% |     |
| --------------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| of the Purdue Model,  | Detection |     |     |     |     |     |     |     |     |     |     |
5.3 LEVEL
| with threat hunting  | Vulnerability  |     | 14% | 14% | 5%  |     |     | 54% |     |     | 13% |
| -------------------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
management
and penetration testing
|     | Threat hunting |     | 7% 8% | 5%  |     |     |     | 63% |     | 17% |     |
| --- | -------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
barely peaking above
|     | Pentesting |     | 7% 8% | 5%  |     |     | 62% |     |     | 19% |     |
| --- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
20% of respondents in
|     |     | 0%  |     | 20% |     | 40% |     | 60% | 80% |     | 100% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
any level as partially
|     | Detection |     | 20% |     | 17% | 9%  |     | 38% |     | 17% |     |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
covered or better.
3 LEVEL Vulnerability
|                       |                |     | 12%    | 15% | 6%  |     |     | 55% |     |     | 13% |
| --------------------- | -------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| When revisiting real- | management     |     |        |     |     |     |     |     |     |     |     |
| world incidents,      | Threat hunting |     | 6% 10% | 5%  |     |     |     | 62% |     | 17% |     |
|                       | Pentesting     |     | 8% 5%  | 5%  |     |     | 63% |     |     | 19% |     |
increased threats, and
|     |     | 0%  |     | 20% |     | 40% |     | 60% | 80% |     | 100% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
evolving regulations
| across ICS/OT the      | Detection      |     | 10% | 15% |     | 18% |     | 39% |     | 18% |     |
| ---------------------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| message is clear: Our  | Vulnerability  |     |     |     |     |     |     |     |     |     |     |
|                        | 2 LEVEL        |     | 8%  | 13% | 10% |     |     | 56% |     |     | 13% |
management
industry needs to
|     | Threat hunting | 4%  | 6%  | 9%  |     |     |     | 64% |     |     | 17% |
| --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
bridge gaps across our
|     | Pentesting | 4%  | 6%  | 7%  |     |     | 65% |     |     | 19% |     |
| --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
programs and critical
|     |     | 0%  |     | 20% |     | 40% |     | 60% | 80% |     | 100% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
sites to meet tomorrow’s
| challenges. | Detection |     | 6% 11% |     | 15% |     |     | 48% |     | 20% |     |
| ----------- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
1/0 LEVEL Vulnerability
|     | management |     | 7% 7%  | 12% |     |     |     | 61% |     |     | 13% |
| --- | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
|     |            | 2%  | 4% 10% |     |     |     | 67% |     |     | 17% |     |
Threat hunting
|     | Pentesting | 4%3% | 5%  |     |     |     | 69% |     |     | 19% |      |
| --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |            | 0%   |     | 20% |     | 40% |     | 60% | 80% |     | 100% |
SETIS ETOMER/DLEIF
|     | Detection |     | 8%  | 10% | 19% |     |     | 41% |     | 22% |     |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Vulnerability
|     |     |     | 9%  | 9%  | 13% |     |     | 57% |     |     | 13% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
management
|     | Threat hunting | 2%  | 7%    | 7%  |     |     | 66% |     |     | 17% |      |
| --- | -------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     | Pentesting     | 3%  | 5% 6% |     |     |     | 66% |     |     | 19% |      |
|     |                | 0%  |       | 20% |     | 40% |     | 60% | 80% |     | 100% |
 Full ICS/OT program coverage  Partially covered by ICS/OT program  Unknown/unsure
|     |  Largely covered by ICS/OT program |     |     |     |  No ICS/OT program coverage |     |     |     |     |     |     |
| --- | ---------------------------------- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
Figure 20. ICS/OT Capabilities by Coverage for Each Level of the Purdue Model
| State of ICS/OT Security 2025  |     |     |     |     |     |     |     |     |     |     | 18  |
| ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Cyber Resilience, Business Continuity,
and Disaster Recovery Planning
Cyber resilience, like other aspects of risk management, must be incorporated into
broader enterprise-level efforts to be successful. This should include areas that
industrial organizations have
clear strengths in—namely  Is your organization actively incorporating ICS/OT
business continuity and disaster  cyber resilience strategies into broader enterprise
recovery (BC/DR) planning. While
disaster recovery and business continuity planning?
typically relegated to natural
| disasters, supply chain risks, or  | 10% | 28% | 30% |     | 20% | 12% |
| ---------------------------------- | --- | --- | --- | --- | --- | --- |
other reliability and operational
|     | 0%  | 20% | 40% | 60% | 80% | 100% |
| --- | --- | --- | --- | --- | --- | ---- |
concerns, cybersecurity should
|     |     |  Fully integrated      |  Largely integrated      |  Partially integrated |     |     |
| --- | --- | ---------------------- | ------------------------ | --------------------- | --- | --- |
be a key element in both disaster
|     |     |  Not currently integrated     |     |  Unknown/unsure |     |     |
| --- | --- | ----------------------------- | --- | --------------- | --- | --- |
recovery and business continuity
planning. As seen in Figure 21,  Figure 21. Cybersecurity Integration
into BC/DR Planning
less than 10% describe cybersecurity as being fully integrated into enterprise-wide
BC/DR planning—and nearly half (50%) describe it as partially or not integrated at all.
Business continuity and disaster recovery planning for ICS/OT usually defaults to
backups, as seen in Figure 22. However, BC/DR is a full chain from knowing what
matters to how fast you must recover to practicing recovery safely. Most organizations
have the technical safety net
in place: OT-specific backups/ Which of the following cyber resilience activities are integrated
failover are common (66%),  into your organization’s BC/DR planning for ICS/OT environments?
| and about half have done     | Select all that apply.                    |     |     |     |     |     |
| ---------------------------- | ----------------------------------------- | --- | --- | --- | --- | --- |
| the homework to integrate    | OT-specific backup, recovery,             |     |     |     |     |     |
|                              | or failover procedures                    |     |     |     |     | 66% |
| OT into enterprise business- | (e.g., bare metal restoration or similar) |     |     |     |     |     |
| impact analysis (53%) and    | OT business impact analysis (BIA)         |     |     |     |     |     |
|                              | integrated into enterprise risk models    |     |     |     | 53% |     |
to define recovery time and
ICS/OT recovery time objectives
|     | (RTO) and recovery point  |     |     |     | 52% |     |
| --- | ------------------------- | --- | --- | --- | --- | --- |
point objectives (RTO/RPO)
objectives (RPO) defined
| (52%). Where resilience thins    | Testing or simulation of         |     |     |     |     |     |
| -------------------------------- | -------------------------------- | --- | --- | --- | --- | --- |
|                                  | OT-specific recovery procedures  |     |     | 33% |     |     |
| is in execution: Only one-third  | (e.g., from ransomware)          |     |     |     |     |     |
Site-level resilience playbooks or
| test or simulate OT-specific  |     |     |     | 31% |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- |
contingency protocols for cyber events
| recovery, and 31% keep site-level  | Cyber-informed engineering             |     |     |     |     |     |
| ---------------------------------- | -------------------------------------- | --- | --- | --- | --- | --- |
|                                    | (CIE/CCE) used to identify or protect  |     |     | 29% |     |     |
playbooks for cyber events—both
high-consequence functions
ICS/OT risk considerations included
crucial to proving recoverability.
|     | in HAZOP, PHA, or similar safety/ |     |     | 23% |     |     |
| --- | --------------------------------- | --- | --- | --- | --- | --- |
engineering assessments
More advanced, risk-focused
|                                   | No specific OT resilience  |     | 9%  |     |     |     |
| --------------------------------- | -------------------------- | --- | --- | --- | --- | --- |
| practices such as cyber-informed  | planning included in BC/DR |     |     |     |     |     |
engineering (CIE/CCE) (29%) and
Figure 22. BC/DR Activities and
aligning OT cyber risks with safety assessments (e.g., HAZOP, PHA, or similar) (23%) are  ICS/OT Cybersecurity
still emerging. Notably, 9% report no OT-specific resilience planning, underscoring a
maturity gap between documented intent and exercised capability.
State of ICS/OT Security 2025  19

Testing of these ICS/OT specific resilience plans (e.g., recovery, failover,
engineering rebuilds, etc.) is also uncommon, with only 32% testing annually
with either a tabletop or hands-on validation. Although there is a small
population (9%) that only tests after an incident or “near-miss,” a larger cohort
(16%) admit to never formally testing their resilience plans.
Technology Deployments: Past, Present, and Future
Cyber preparedness for
In the past 12 months, which of the following technologies or
industrial environments requires
practices were newly deployed or significantly expanded in your
a careful alignment across
ICS/OT environment? Select all that apply.
business processes, technology
ICS-specific asset inventory or
deployment, and workforce 50%
network visibility tools
skill and culture. While many Secure remote access platforms with
47%
multifactor authentication (MFA)
ICS/OT systems measure life Zero trust or network segmentation
32%
initiatives in OT environments
cycles in decades, not years, the
ICS log collection and centralization
32%
combination of cyber threats and (e.g., historian logs, syslog integration)
Vulnerability management tools
32%
new regulations and standards designed for ICS/OT assets
requires ICS/OT professionals to ICS-aware threat detection
platforms (e.g., anomaly-based, 31%
constantly adapt to changes. deep packet inspection)
Threat intelligence integration
21%
(e.g., STIX/TAXII feeds, vendor alerts)
Over the last year, industrial
ICS-specific dashboarding or
19%
organizations invested in a executive-level reporting tools
Cloud-based ICS/OT data
variety of new technologies, as 17%
platforms or services
seen in Figure 23. The top areas, ICS tabletop scenario development 17%
platforms or tooling
asset inventory and visibility
No significant technology deployment 13%
(50%) and secure remote access
AI/ML-driven anomaly detection or
13%
predictive maintenance technologies
with MFA (45%), align with the
OT-specific Security Orchestration,
12%
threats and real-world incidents Automation, and Response (SOAR) tools
that were reported, along with Other 3%
increased segmentation (32%). Figure 23. Technology Deployments Over
Other categories, like ICS-specific tabletop exercises (17%) and threat the Previous 12 Months
intelligence integration (21%) were low, which correlates with previous
topics and highlights a need for increased investment in these areas as
they each have a demonstrable impact on incident response detection,
Organizations that suffered an
containment, and remediation timelines. ICS/OT-specific security
incident in 2025 invested heavily in
orchestration, automation, and response (SOAR) was the lowest area
of technology investment (12%). This trend remained true regardless response tools—after the fact. Don’t
of preparedness, regulations, or if the organization had a SOC (where wait for a breach to justify the budget.
SOAR may provide tangible benefits).
State of ICS/OT Security 2025 20

To help organizations with
Which of the following are top investment priorities for your
ICS/OT cybersecurity roadmaps
ICS/OT cybersecurity program in the next 12 to 24 months?
and associated metrics, the
Select all that apply.
2025 survey also included
future-looking technology  Asset visibility and inventory tools 54%
deployments to examine what  Threat detection and analytics platforms 43%
investments industrial sectors
Vulnerability management tools 41%
will deploy over the next 12 to
Secure remote access modernization 40%
24 months, as seen in Figure 24.
|     | Incident response tools or improvements |     | 37% |
| --- | --------------------------------------- | --- | --- |
Heading into 2026–2027,
Configuration management
32%
| organizations will continue to  | tools or improvements |     |     |
| ------------------------------- | --------------------- | --- | --- |
32%
| invest heavily in asset inventory  | Workforce training and role clarity  |     |     |
| ---------------------------------- | ------------------------------------ | --- | --- |
|                                    | Identity access management solutions |     | 31% |
and visibility (54%) and secure
remote access (40%) as they  Governance, risk, and compliance tooling 27%
did over the past 12 months.
|     | Threat hunting and response capability |     | 27% |
| --- | -------------------------------------- | --- | --- |
However, threat detection (43%)
|     | Cyber-informed engineering integration | 22% |     |
| --- | -------------------------------------- | --- | --- |
and vulnerability management
|     | Cloud architecture or data security | 20% |     |
| --- | ----------------------------------- | --- | --- |
(41%) also round out the top
Third-party and supply chain risk  17%
| investments—at a higher rate  | management tools, including SBOM |     |     |
| ----------------------------- | -------------------------------- | --- | --- |
than 2025 deployments.  None/no major investments planned 11%
| There are several factors that  | Other | 3%  |     |
| ------------------------------- | ----- | --- | --- |
influence what technologies
Figure 24. Technology Investments
industrial organizations invest in. For example (and unsurprisingly),  Over the Next 12–24 Months
regulated facilities track higher in every category for both past and
future technology deployments.
What factors have driven the technology deployments or
As a matter of fact, both
regulatory requirements and  expansions you selected above? Select all that apply.
threat landscape were listed as
Regulatory or compliance requirements 61%
the top drivers for technology
Response to evolving threat landscape
61%
| deployments (both at 61%, as  | (e.g., APT activity, ransomware groups) |     |     |
| ----------------------------- | --------------------------------------- | --- | --- |
Alignment with a digital transformation  46%
| seen in Figure 25). However, the  | or modernization initiative |     |     |
| --------------------------------- | --------------------------- | --- | --- |
| most significant determining      | Executive-level directive   |     | 34% |
or board mandate
factor and unique profile for
|                                  | Audit or insurance findings  |     | 29% |
| -------------------------------- | ---------------------------- | --- | --- |
| investment came from industrial  | Availability of new vendors  |     |     |
22%
or improved technology
organizations with SOCs that
Internal incident or near-miss 22%
include ICS/OT in some fashion—
those organizations are more  Peer or industry benchmarking 18%
| likely to have invested (and  | Other | 3%  |     |
| ----------------------------- | ----- | --- | --- |
continue to invest) in asset  Figure 25. Technology Deployment Drivers
visibility (63% in 2025 and 2026–2027), threat detection (47% in 2025
compared to 32% for organizations without a SOC), and log collection/
centralization (43% in 2025 compared to 32% for their non-SOC peers).
State of ICS/OT Security 2025  21

Organizations that previously identified themselves as fully prepared  The greatest shift in technology
for future cyber threats also invested in technology differently
investment comes from organizations
from their peers, likely because they already had heavy capabilities
with ICS/OT SOC capabilities, who
in threat detection and secure remote access. In 2025, these
invest more in asset visibility, threat
organizations invested more in threat intel integration (43%), log
detection, and log centralization
centralization (40%), and vulnerability management (40%). For the
compared to their peers.
next 12–24 months, these prepared organizations plan to continue to
invest heavily in asset visibility (66%) and threat detection (55%), while
adding configuration management (55%) to the top three categories.
Despite this growth, our
How does your organization measure the success or effectiveness
industry still lacks meaningful
of these ICS/OT technology deployments? Select all that apply.
discussion on metrics and
Risk reduction metrics (e.g.,
measuring success and
|                              | impact reduction, improved  |     |     |     |     | 51% |
| ---------------------------- | --------------------------- | --- | --- | --- | --- | --- |
| effectiveness across ICS/OT  | security capabilities)      |     |     |     |     |     |
Compliance/audit readiness
technology deployments. Only
|     | indicators (e.g., control gap  |     |     |     |     | 50% |
| --- | ------------------------------ | --- | --- | --- | --- | --- |
closure, findings avoided)
16% of respondents provide
|                                  | Operational KPIs (e.g., detection        |     |     |     | 43% |     |
| -------------------------------- | ---------------------------------------- | --- | --- | --- | --- | --- |
| financial metrics and one in     | coverage, response time, system uptime)  |     |     |     |     |     |
|                                  | Cultural or adoption-based indicators    |     |     | 21% |     |     |
| five (21%) respondents reported  | (e.g., IT/OT collaboration, user uptake) |     |     |     |     |     |
Financial or ROI-based measures
| that they do not have any  |     |     |     | 16% |     |     |
| -------------------------- | --- | --- | --- | --- | --- | --- |
(e.g., cost savings, insurance incentives)
| measures for success, though  | No metrics are currently defined,  |     |     |     |     |     |
| ----------------------------- | ---------------------------------- | --- | --- | --- | --- | --- |
15%
but they are planned
planning may be underway for
|     | Success is not currently measured |     | 6%  |     |     |     |
| --- | --------------------------------- | --- | --- | --- | --- | --- |
some. Figure 26 highlights the
|     | Unknown/unsure |     | 4%  |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- |
most popular metrics as risk
reduction, compliance/audit- Figure 26. Technology Deployment Success and Effectiveness Metrics
readiness, and operational key
performance indicators (KPIs).
How would you describe your organization’s ICS/OT
| Although cultural metrics  | cybersecurity culture today? |     |     |     |     |     |
| -------------------------- | ---------------------------- | --- | --- | --- | --- | --- |
(workforce change
| management, adoption rates,  | 12% |     | 49% | 16% | 14% | 8%  |
| ---------------------------- | --- | --- | --- | --- | --- | --- |
and similar) were relatively
|     | 0%  | 20% | 40% | 60% | 80% | 100% |
| --- | --- | --- | --- | --- | --- | ---- |
low (21%), ICS/OT practitioners
 Strong, cross-functional culture with a shared understanding from the plant floor to boardroom
believe that our industry is
 Improving with growing collaboration between OT, IT, and leadership
getting better at culture with
 Fragmented with clear divides between teams or roles
a majority (62%) reporting
 Minimal, Cybersecurity is not embedded in day-to-day ICS operations
that culture is either strong or
 Unknown/unsure
improving, as seen in Figure 27.
Figure 27. Culture Divide Between IT, OT, and Leadership
State of ICS/OT Security 2025  22

Interestingly, much of this
Which of the following best reflects how ICS/OT cybersecurity
sentiment is reflected in
is embedded into your organization’s day-to-day practices?
how ICS/OT cybersecurity
Select all that apply.
is embedded into an
IT security understands and respects
| organization’s day-to-day  | OT operational constraints | 45% |
| -------------------------- | -------------------------- | --- |
activities, as highlighted in  OT personnel understand the  44%
potential impacts of cyber events
Figure 28. Similar to technology,
Security is part of operational
|                                   | decision-making                          | 43% |
| --------------------------------- | ---------------------------------------- | --- |
| there are multiple factors        | (e.g., process design, control changes)  |     |
| that correlate with improved      | Cybersecurity is regularly               |     |
|                                   | discussed in shift meetings, safety  37% |     |
| culture. Regulated entities, for  | moments, or toolbox talks                |     |
OT personnel receive regular cyber
example, tend to have more  34%
training relevant to their role
| embedded tasks and, as a  | Security champions or liaisons exist  |     |
| ------------------------- | ------------------------------------- | --- |
30%
within OT or operations teams
| high corollary, report stronger  | Security procedures are followed  |     |
| -------------------------------- | --------------------------------- | --- |
23%
without relying solely on
| ICS/OT cybersecurity culture.  | compliance requirements |     |
| ------------------------------ | ----------------------- | --- |
However, what appears to be  Frontline workers know how to escalate  21%
or report ICS/OT cyber issues
| the No. 1 indicator for having  | Cybersecurity is not embedded  |     |
| ------------------------------- | ------------------------------ | --- |
19%
into day-to-day OT activities
a strong cybersecurity culture
Unknown/unsure 5%
that stretches across IT, OT,
Figure 28. ICS/OT Cybersecurity as
and leadership may be a bit surprising: having an ICS-specific incident response plan.
Part of Day-to-Day Activities
Respondents that had one were more likely to report a strong (17%) or improving (62%)
culture with a majority reporting that IT understand OT constraints (57%), OT understands
potential cyber impacts (55%), and security is embedded in OT decision-making (57%).
Culture follows capability: Organizations with an ICS/OT
incident response plan report stronger IT-OT alignment, better
leadership engagement, and more resilient day-to-day practices.
State of ICS/OT Security 2025  23

Conclusions and Next Steps for Industry
The 2025 State of ICS/OT Cybersecurity Survey paints a mixed picture. On one hand, detection
timelines are shrinking, incident response planning is more common, and regulatory pressure
is driving long-term maturity. On the other, remediation remains slow, advanced practices such
as threat hunting and red/purple team exercises are limited, and remote access continues to
expose organizations to disproportionate risk.
By exploring the full Purdue Model and various security controls, like detection, vulnerability
management, and threat hunting, we can gain a better understanding of a risk-based and
threat-informed approach to ICS/OT security program management. The goal may not be to
have “100% coverage” in all categories, but there needs to be an informed discussion on the
trade-offs between detection, protection, and incident response. With only a small percentage of
organizations reporting full visibility across the ICS Cyber Kill Chain—and even fewer feeling they
are well-positioned for future cyber threats—it is apparent that coverage is sparse at best and
concentrated far from where consequences are most severe, including remote field sites.
Taken together, this data reveals a divide between those building truly mature programs and
those still struggling with foundational coverage. The characteristics of the most prepared
organizations are clear: They integrate IT and OT monitoring, engage field technicians in
preparedness, align resilience planning with safety engineering, and actively contribute to
information sharing. They are also more likely to embed cybersecurity into daily OT decision-
making—where culture becomes a force multiplier for technology investments.
Looking ahead, the path forward for industry is actionable:
1. I mprove coverage of ICS/OT security. Leveraging a risk-based and threat-informed
approach to ICS/OT security controls has proven to improve incident response times and
decrease reliability, safety, and financial impacts.
2. S hift from detection to resilience. Shorter time-to-containment is not enough.
Organizations must invest in faster, safer recovery through backups, failover,
and cyber-informed engineering.
3. Broaden participation. Preparedness cannot be limited to security teams—
field technicians, engineers, and executives alike need to play active roles in
threat-aware exercises.
4. L everage regulation as a springboard. Compliance requirements should be treated not
as ceilings but as baselines for stronger detection, response, and cultural integration.
The industry has made tangible progress since this survey began in 2017. Yet as the appendix
data shows, gaps persist at the very layers of the Purdue Model where consequences are most
severe. The challenge for 2026 and beyond is clear: Close those gaps before adversaries exploit
them and transform today’s incremental improvements into tomorrow’s resilience.
State of ICS/OT Security 2025 24

Appendix 1: Purdue Model Overview
The Purdue Model serves as the backbone for how ICS/OT environments are
conceptualized and secured. By breaking down industrial networks into distinct layers, it
provides a structured way to align defenses with operational realities, as seen in Figure 29.
Where:
• L evel 5 – Internet/DMZ—External-
facing services such as web and
email servers. While not always
included in ICS discussions, this
zone defines the perimeter where
enterprise IT connects to the
outside world.
• L evel 4 – Enterprise IT—
Traditional corporate systems
(e.g., business applications, SOC,
SIEM). Security maturity here is
generally the highest, but controls
often stop at this boundary.
• L evel 3 – Operations Systems—
Plant-level management systems
such as historians and operations
servers. This level acts as a
bridge between IT and OT and is
a frequent target for attackers
attempting lateral movement.
Figure 29. Purdue Model Concept
• L evel 3.5 – DMZ—A buffer zone between IT and OT, often containing jump servers,
patch servers, or antivirus update servers. It is a critical chokepoint for enforcing
segmentation.
• L evel 2 – Supervisory Control—Systems like SCADA and HMI that oversee and
visualize industrial processes. Attacks at this level can disrupt visibility into
operations or allow manipulation of setpoints.
• L evel 1 – Basic Control—PLCs, RTUs, and controllers that execute commands.
Compromise here directly affects process logic and reliability.
• L evel 0 – Physical Process—The sensors and actuators tied to real-world
operations—turbines spinning, valves opening, breakers tripping. Security here is
minimal but consequences are most severe.
• R emote Sites—Extending across Levels 0–2, these environments (wind farms,
substations, remote pumping stations) often face the same risks but with fewer
local defenses and limited connectivity to central monitoring.
State of ICS/OT Security 2025 25

Appendix 2
ICS CAREER PROGRESSION
|     |     |     |     | ICS Security  | ICS Security  | ICS Security  | ICS Security  | Process Control  | ICS/OT Security  |
| --- | --- | --- | --- | ------------- | ------------- | ------------- | ------------- | ---------------- | ---------------- |
|     |     |     |     | Analyst       | Architect     | Incident      | Leader        | Engineering      | Pen Tester       |
In a world that is seeing increasingly sophisticated and  Ensures control  Responder Builds and maintains  Tests, programs,  Discovers system
|     |     |     |     | Acquires and manages  | system network  |     | business relationships  | troubleshoots, and  | vulnerabilities and  |
| --- | --- | --- | --- | --------------------- | --------------- | --- | ----------------------- | ------------------- | -------------------- |
impactful industrial cyber threats, these courses prepare OT  resources, supports, and  Executes specifi c
|     |     |     |     | p e r f o r m s  k e y  i n d u s | tr ia l   s e c u r i ty   co m p l i a | n c e   i n d u s t ri a l  i n c id e | n t  w i t h   e n g in e e r in g   s | t a ff    o v e r s e e s   ch a n g e | s  o f  w o r k s   w it h  a s s e t   |
| --- | --- | --- | --- | --------------------------------- | --------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | --------------------------------------- |
security professionals to lead, defend, and protect industrial  s e c u r it y  p r o te c t i o n  w h il e   a n d   b e s t  p ra c ti c e s   fo r   re s p o n s e  f o r   in c id e n ts  an d   C - s u i te  s t a k e h o l d e r s  e x i s t in g   p ro c e s s e s  ow ne r s   a n d  o p e r a t o rs
control systems at the foundational, essential, management,  ad h e ri n g   to   sa f e ty   a nd  control networks  t h a t   t h re a te n  o r   by  c o m m u n i c a ti n g  a n d  o r  i m p le m e n t s  n e w   t o  m i t ig a t e   d i s c o v e r ie s
|     |     |     |     | e n g i n e e ri n g  g o a l | s   | imp a c t   c o n tr o l s y | s te m  m a n ag in g   c y b e r -t | o - en g i n e er in g  p r o c e | ss e s  a n d  p r e v e n t   e x p l o it a t io n   |
| --- | --- | --- | --- | ----------------------------- | --- | ---------------------------- | ------------------------------------ | --------------------------------- | ------------------------------------------------------ |
tactical and advanced skill sets. With SANS ICS Security, train  networks and assets,  physical risks while  through the deployment  from adversaries
|     |     |     |     |     |     |     | r e d u c i n g  s e c u r it y   ri s | k  t o   a n d  o p e r a ti o n s o | f   |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | ------------------------------------ | --- |
to defend what makes, moves, and powers the world. w h i le   m a in t a in i n g   t h e   e n g i n e e r in g   o p e r a t io n s   eng in e e ri n g  s y s t em s  a nd
|     |     |     |     |     |     | sa f e t y  a n d  r e li a b | i l i ty   and simultaneously  | automation devices |     |
| --- | --- | --- | --- | --- | --- | ----------------------------- | ------------------------------ | ------------------ | --- |
|     |     |     |     |     |     | of operations                 | prioritizing safety            |                    |     |
ICS Cybersecurity Foundations™
ICS
|     | L e a r n  t h e   c y | b e r  f u n d amentals to protecting  |     |     |     |     |     |     |     |
| --- | ---------------------- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
FOUNDATIONAL 310
|     | IC S / O T   e n v i r         | o n m e n t s |     |     |     |     |     |     |     |
| --- | ------------------------------ | ------------- | --- | --- | --- | --- | --- | --- | --- |
| ICS | ICS/SCADA Security Essentials™ |               |     |     |     |     |     |     |     |
Gain the essential skills to keep industrial
410
systems safe from cyber threats
ESSENTIAL
| ICS        | ICS Security Essentials for Leaders™    |     |     |     |     |     |     |     |     |
| ---------- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 418        | Manage the people, processes, and       |     |     |     |     |     |     |     |     |
| MANAGEMENT | technologies for OT cyber-risk programs |     |     |     |     |     |     |     |     |
| ICS        | Essentials for NERC Critical            |     |     |     |     |     |     |     |     |
Infrastructure Protection™
| 456 | Maintain a defensible compliance program  |     |     |     |     |     |     |     |     |
| --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
up to NERC CIP standards
| TACTICAL ICS | ICS Visibility, Detection, and Response™ |     |     |     |     |     |     |     |     |
| ------------ | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Monitor threats, perform incident response
515
and enhance network security
| ICS | ICS Cybersecurity In-Depth™                          |     |     |     |     |     |     |     |     |
| --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 612 | Identify threats in a real-world ICS environment to  |     |     |     |     |     |     |     |     |
protect against adversary attacks
|              | I C S / O T P e n e                                  | t ra t i o n   T e s t i n g  &   A   | s s e s s m e n ts™ |     |     |     |     |     |     |
| ------------ | ---------------------------------------------------- | ------------------------------------- | ------------------- | --- | --- | --- | --- | --- | --- |
| ADVANCED ICS | P e rf o rm  s a fe                                  | ,  h a n d s - o n   I C S / O T  p e | n e t r a tio n     |     |     |     |     |     |     |
| 613          | testing and assessments to identify vulnerabilities  |                                       |                     |     |     |     |     |     |     |
and improve operational resilience
Where multiple courses are shown for a given role, determination of the best course to take would be based on the number of years of experience and sector of work.
 sans.org/ics           ics-community.sans.org/signup           @SANSICS           linkedin.com/showcase/sans-ics           youtube.com/c/SANSICSsecurity
State of ICS/OT Security 2025  26

Sponsor
SANS would like to thank this survey’s sponsor:
State of ICS/OT Security 2025 27

About the SANS Research Program
The SANS Research Program is a key initiative by the SANS Institute and a
premier global provider of cybersecurity research and information. SANS
Research Program is designed to provide cybersecurity practitioners and
leaders with data-driven insights, thought leadership, and solutions that
help them better understand and respond to evolving security challenges.
All content is authored by SANS instructor experts from around the world
who apply their years of experience from hands-on practitioner work in the
field, advisory roles, and the classroom to provide education, guidance, and
actionable insights that help make the cyber world a safer place.
To learn about sponsorship opportunities for research, content, and
in-person or virtual events, email us at Sponsorships@sans.org or
go to www.sans.org/sponsorship.
State of ICS/OT Security 2025 28

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-08-18", "model": "gemini-3.5-flash-lite"} -->
