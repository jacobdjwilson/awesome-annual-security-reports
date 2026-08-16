2025 SURVEY
SANS SOC Survey 2025
Written by Christopher Crowley
July 2025
©2025 SANS™ Institute

SANS 2025 SOC SURVEY
Key Findings
Operations and Technology Use
| 79% |     |     | 85% |     |     |     | 42% |     |     | 43% |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
 of SOCs are   of respondents   of SOCs dump   of respondents
operational 24/7. say endpoint security  all incoming data  say SIEM is the top
|     |     |     |     | alerts are their  |     |     | into a SIEM, often  |     |     |     | tech skill they seek  |     |
| --- | --- | --- | --- | ----------------- | --- | --- | ------------------- | --- | --- | --- | --------------------- | --- |
primary trigger for  without a retrieval or  when hiring—more
|     |     |     |     | response. |     |     | management plan. |     |     | than double the next  |     |     |
| --- | --- | --- | --- | --------- | --- | --- | ---------------- | --- | --- | --------------------- | --- | --- |
highest response.
|     | 42% |                |     |     | 69% |               |     |     | 69% |                      |     |     |
| --- | --- | -------------- | --- | --- | --- | ------------- | --- | --- | --- | -------------------- | --- | --- |
|     |     |  of SOCs use   |     |     |     |  of SOCs use  |     |     |     |  of SOCs still rely  |     |     |
AI/ML tools   cyber threat intelligence  on manual or mostly
“out of the box”   (CTI) data primarily for  manual processes to
|     | with no customization. |     |     |     | incident response. |     |     |     |     | report metrics. |     |     |
| --- | ---------------------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --------------- | --- | --- |
Staffing and Workforce Dynamics
| 2–10 people |     | 3–5 years |     |     |     | 73% |      | 62% |     |          | 42% |                |
| ----------- | --- | --------- | --- | --- | --- | --- | ---- | --- | --- | -------- | --- | -------------- |
|             |     |           |     |     |     |     |  of  |     |     |  of SOC  |     |  of SOC staff  |
is the most  is the most  organizations  professionals say  don’t know the
common size for a  common tenure  allow remote work  their organization  SOC’s budget,
fully staffed SOC. for SOC staff. for SOC team  isn’t doing  indicating a
|     |     |     |     |     | members at least  |     |     | enough to retain  |             |     | disconnect between  |     |
| --- | --- | --- | --- | --- | ----------------- | --- | --- | ----------------- | ----------- | --- | ------------------- | --- |
|     |     |     |     |     | some of the time. |     |     |                   | top talent. |     | technical and       |     |
business teams.

Survey Author
Christopher Crowley Christopher Crowley has 25 years of industry experience
SANS Senior Instructor managing and securing networks. He has authored
numerous courses and is considered a leading expert
in building an effective SOC. He currently works as an
CURRENTLY TEACHING
independent consultant in the Washington, DC, area
SEC595: Applied Data Science
focusing on effective computer network defense. His work
and AI/Machine Learning for
experience includes penetration testing, security operations,
Cybersecurity Professionals™
incident response, and forensic analysis. Chris holds several
SEC511: Cybersecurity
VIEW PROFILE industry certifications including the GSEC, GCIA, GCIH (gold),
Engineering: Advanced Threat
GCFA, GPEN, GPYC, GMOB, GMLE, GASF, GREM, GXPN, and CISSP.
Detection and Monitoring™
Chris was awarded the SANS 2009 Local Mentor of the
SEC504: Hacker Tools,
Year Award. The Mentor of the Year Award is given to SANS
Techniques, and Incident
Mentors who excel in leading SANS Mentor Training classes
Handling
in their local communities. He is also a faculty member
of the SANS Technology Institute and the NSA Center of
FORMERLY TAUGHT
Academic Excellence in Cyber Defense as well as a multi-
FOR585, SEC401, SEC503,
time winner of the National Cyber League Competition. Chris
SEC560, SEC575, SEC580
spends his spare time mountain biking, rock climbing, and
MGT535, MGT517
savoring epicurean treats.
Executive Summary
Over the past nine years, the SANS Institute has conducted an annual industry survey to better
understand how security operations centers (SOCs) are built, staffed, and run, and to learn more
about SOC analysts’ biggest challenges and potential industry improvements. This year’s goal was
to provide insights into SOC performance against peers, prioritize improvements for the coming
year, and gain insight into valued and less-effective technologies across the industry.
This year’s report outlines data and insights behind SOC structure comparisons, outsourcing
trends, technology considerations, areas for improvement, and ways in which various
technologies are being implemented.
Although AI is the latest technological trend, it’s notable that over the nine years of conducting this
survey, capabilities, staffing levels, outsourced services, and challenges in security operations have
remained largely consistent.
Security operations is a long-term, gradually maturing effort that demands both patience
and persistence.
SANS SOC Survey 2025 3

Demographics
Most respondents were based in the United States, with participants from 57 different countries.
The top industries represented were the usual mix of respondents from banking/finance
(16%), cybersecurity (14%), technology (14%), and government (14%) and there was a diverse
representation of organization size. Figure 1 shows the survey demographics in detail.
Top 4 Industries
Represented
| 73  | 63            | 63         | 61         |
| --- | ------------- | ---------- | ---------- |
|     | Cybersecurity | Technology | Government |
Banking and finance
Operations and
Headquarters
| 292           | 209    | 147                    | 132    |
| ------------- | ------ | ---------------------- | ------ |
|  Ops          |  Ops   |  Ops                   |  Ops   |
|               | 88     | 56                     | 23     |
| 221  HQs      |  HQs   |  HQs                   |  HQs   |
| United States | Europe | Latin or South America | Canada |
Top 4 Roles
Represented
110
| Security  |     | 42  | 41  |
| --------- | --- | --- | --- |
56
| administrator/   |             | SOC manager or  | Security manager   |
| ---------------- | ----------- | --------------- | ------------------ |
| Security analyst | SOC Analyst | director        | or director        |
Figure 1. Demographics of Survey Respondents
SANS SOC Survey 2025  4

Security Operations Center (SOC) Defined
The modern SOC in 2025 is built around a few foundational elements that define how it
functions, where its strengths lie, and how it adapts to evolving threats. These include
its core capabilities, operational model (in-house vs. outsourced), data architecture, and
staffing strategy. Based on current survey data, a typical operational SOC reflects the
following four characteristics:
• C apabilities—The core functions of a SOC and the tasks it handles on a routine basis
• I n-house vs. outsourced functions—The tasks that are handled internally vs. by
third parties
• A rchitecture—The structure for how and where data is collected, stored, and accessed
• S taffing and hours of operation—Details on team size, roles, expected skill set,
and whether the SOC operates around the clock or during limited hours
In addition, according to the data, a baseline SOC can be defined as:
• P rioritizes alert triage, threat detection, and incident response as core functions with
threat intelligence, vulnerability management, and hunting as supporting functions.
• E mploys 10 full-time team members (or full-time equivalent) with the average
length of employee tenure of three to five years.
• H andles most monitoring, detection, and incident response in-house, while
outsourcing pen-testing, digital forensics, some threat intel, and other functions
requiring higher levels of expertise or specialization.
• O perates a centralized architecture, with cloud adoption growing but still lagging
behind the cloud adoption volume of IT.
• M aintains 24/7 operational coverage in most cases, with some still relying on
rotating coverage or “as-needed” escalation.
• R eports metrics manually, even though nearly half say it’s too time-consuming.
Automation remains limited.
• R elies heavily on EDR as the most trusted and mature tool in use. AI/ML is at the
bottom of the satisfaction list.
• S tores more data than ever before, often dumping everything into SIEM or syslog
without a clear plan in place to manage or analyze it, creating visibility issues.
SANS SOC Survey 2025 5

Capabilities and  What activities are included in your SOC? What
activities have you outsourced either fully or partially,
Outsourcing
to external services through a managed security
service provider (MSSP) or due to cloud hosting?
The expectations of SOC
|     |     |  In-house         |  Outsourced         |     |     |  Both |     |     |
| --- | --- | ----------------- | ------------------- | --- | --- | ----- | --- | --- |
functions are robust and
|     | Alerting (triage and escalation) |     |     |     | 260 |     | 55  | 128 |
| --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- |
comprehensive. Survey
|     | Incident response |     |     |     | 275 |     | 28  | 135 |
| --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
responses make it clear: Failing
|     | Vulnerability assessments |     |     |     | 293 |     |     | 33 112 |
| --- | ------------------------- | --- | --- | --- | --- | --- | --- | ------ |
to cover core responsibilities,
whether in-house or  Security monitoring and detection 270 38 130
outsourced, results in a SOC
|                                   | Data protection                        |     |     |     | 336 |     |     | 21 80 |
| --------------------------------- | -------------------------------------- | --- | --- | --- | --- | --- | --- | ----- |
| that is ineffective at detecting  | Security architecture and engineering  |     |     |     |     |     |     |       |
|                                   |                                        |     |     |     | 347 |     |     | 18 70 |
(of systems in your environment)
and responding to threats.
|     | Security administration |     |     |     | 357 |     |     | 66  |
| --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- |
11
Although there is variety in the
|     | Pen-testing |     |     | 141 |     | 183 |     | 109 |
| --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
activities split between internal teams
|                                       | Security road map and planning |     |     |     | 358 |     |     | 67  |
| ------------------------------------- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- |
| and external vendors, such as MSSPs,  |                                |     |     |     |     |     |     | 8   |
Security tool configuration,
| the core expectations for what a SOC  |     |     |     |     | 307 |     |     | 24 102 |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------ |
integration, and deployment
must be able to do remain largely
SOC architecture and engineering
|     | (specific to the systems running your SOC) |     |     |     | 299 |     |     | 40 93 |
| --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | ----- |
consistent year-over-year with the top
|     | Compliance support |     |     |     | 316 |     |     | 34 82 |
| --- | ------------------ | --- | --- | --- | --- | --- | --- | ----- |
three activities reported as security
roadmap and planning (80%), security
|     | Digital forensics |     |     | 204 |     |     | 109 | 118 |
| --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
administration (80%), and security
|     | Threat hunting |     |     |     | 254 |     | 62  | 115 |
| --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
architecture and engineering (78%)
| (see Figure 2). | Remediation |     |     |     |     |     |     |        |
| --------------- | ----------- | --- | --- | --- | --- | --- | --- | ------ |
|                 |             |     |     |     | 310 |     |     | 17 104 |
External attack surface
|     |     |     |     |     | 232 |     | 70  | 127 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
management
|     | Threat research              |     |     |     | 224 |     | 77  | 128 |
| --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     | SOC maturity self-assessment |     |     |     | 259 |     | 60  | 107 |
|     | Red-teaming                  |     |     | 169 |     |     | 177 | 77  |
|     | Purple-teaming               |     |     | 189 |     |     | 129 | 97  |
|     | Other                        |     | 47  | 21  |     |     |     |     |
5
Figure 2. Response Count on SOC Operations Activities Related to Outsourcing
SANS SOC Survey 2025  6

In-House vs. Outsourcing SOC Capabilities
Core SOC functions like architecture, monitoring, and compliance are typically
kept in-house. This is likely because these areas demand a deep understanding
of internal systems, business priorities, and organizational context. They also
involve close coordination with legal and executive stakeholders, making them
more effective when owned internally (see Figure 3).
On the other hand, outsourcing
Which of the following best describe(s) your SOC’s
makes strategic sense for tasks
incident response capability? Select all that apply.
that are highly specialized,
repeatable, and resource
Incident response is a fully integrated
50.9%
intensive. Services like part of our internal SOC capability.
penetration testing and red We use internal incident responders
who perform response as an 47.9%
teaming often fall into this ad hoc duty when needed.
category. These are typically We use internal incident
responders who work with our 17.2%
project-based efforts where external SOC services provider.
third-party firms can provide
We utilize incident responders from
16.9%
our external SOC services provider.
targeted expertise and
scalability more efficiently than Incident response is provided by
a service provider that is not part 16.0%
internal teams. of our SOC services engagement.
We use dedicated internal incident
Security monitoring and responders, but they are separate from 14.8%
the SOC, with no plans to integrate.
incident response are often
We use internal incident responders
hybrid models—partially with whom we are trying to integrate our 12.7%
internal SOC but haven’t yet done so.
staffed in-house, with external
providers filling in for overflow Other 2.4%
or specialized coverage. This
Figure 3. Incident Response Capabilities
blended approach allows for
flexibility while maintaining core control.
Interestingly, 55% of respondents say SOC use is mandatory across their
organizations, and another 30% say there’s latitude to use external providers.
That indicates SOCs are still viewed as foundational—but organizations are
open to flexible deployment models depending on institutional requirements
and resources. Incident response remains the most internally managed
function. Given its role in real-time crisis management, it makes sense that
most organizations keep this capability under their control.
SANS SOC Survey 2025 7

Architecture
Most respondents (38%) report operating a single, centralized SOC, making it the
most common architecture today. Cloud-based SOC deployments follow at 24%, but
respondent’s indicate planned changes will increase that number to 29% over the next
12 months indicating growing interest in cloud-native security operations.
Despite the hype around cloud-based
How is your SOC infrastructure (i.e., architecture)
SOCs, centralized, on-prem architectures
currently deployed, and how might it change over
remain the prevailing model. The gap
the next 12 months? Select all that apply.
between stated cloud ambitions and
Current Next 12 Months
current deployments highlights the
reality: Cloud migration, particularly for 24.2%
Cloud-based SOC services
29.0%
security operations, is still in transition.
Informal SOC, no defined 10.5%
Although single, centralized SOCs architecture 3.0%
continue to lead, year-over-year Multiple SOCs distributed 10.5%
regionally or by business unit 11.9%
data doesn’t yet point to a decisive
7.8%
Multiple, follow the sun model
architectural shift to the cloud 9.6%
(see Figure 4). Multiple, redundant SOCs 5.8%
looking at the same data 4.7%
As global political uncertainty intensifies
37.8%
Single, centralized SOC
through 2025 and into 2026, SOCs 36.2%
can expect increased scrutiny around 3.4%
Other
4.7%
international data flows. Geopolitical
Figure 4. SOC Architecture, Current
conflict is driving greater regulatory and
and Planned
organizational focus on how and where data is stored, who can access it,
and which entities are monitoring it.
SOCs should be prepared to respond to tough questions
around cross-border visibility, third-party monitoring, and data
residency. These aren’t just technical issues—they’re legal and
strategic concerns. Security leaders should anticipate deeper
engagement from legal, compliance, and business stakeholders
as these topics rise on the agenda.
SANS SOC Survey 2025 8

Modern SOC Challenges
Today’s SOCs are under pressure to deliver faster, smarter, and more SOC employees are making
proactive security outcomes—but several critical gaps are holding them abundant use of AI/ML tools
back. AI/ML tools are being adopted rapidly, yet without intentional without intentional integration
integration and oversight, they often waste budget, increase risk, and fail
and oversight. AI/ML tools
to provide meaningful support. At the same time, threat intelligence—while
provide value, but potentially
abundant—is frequently underutilized due to inconsistent application
waste budget, add risk, and fail
and a lack of objective analysis, keeping teams stuck in reactive mode.
to deliver meaningful support
And although not a direct source of intel, TLS interception has emerged
to SOC operations—technology
as a flashpoint in the visibility debate, raising concerns about privacy,
performance, and trust. These issues collectively reflect a deeper need for satisfaction is low, but reported
strategic alignment and smarter operational practices across the SOC. use is nonetheless high.
Artificial Intelligence (AI) and Machine Learning (ML)
With the substantial influence of AI
Is AI/ML a defined
and ML tools on the SOC in recent
years, learning more about the part of your SOC 16.8% Yes
operations?
influence of both will continue to be 29.5% No, these tools are
not part of the defined
important. Interestingly, data shows
workflow, but we are
13.9% 39.8% using them.
that the majority (40%) use the tools,
but they are not part of the defined No, these tools are
prohibited.
operations (see Figure 5).
Unknown/unsure
A SOC likely has two internal tasks to
address:
Figure 5. AI/ML Within SOC Operations
1. I nternal SOC priority—Shift from uncoordinated, individual use of AI/ML tools
to a team-approved, standardized implementation—one that maximizes their
strengths while minimizing risk.
2. E xternal SOC priority—Maintain oversight of data flowing from
the organization to AI/ML platforms and unsanctioned shadow IT
deployments. Although much of this data may seem low-risk, it’s essential
to have host-based data loss prevention (DLP) tools in place as part of
your standard deployment to ensure visibility and control.
SANS SOC Survey 2025 9

Expert Corner Seth Misner
SANS Faculty Fellow and author
The 2025 SOC Survey highlights a worrisome juxtaposition; SOCs of two SANS courses: LDR414:
struggle to hire and retain skilled analysts, while AI/ML and automation SANS Training Program for CISSP®
are the most commonly planned expansions, despite ranking lowest in Certification, SEC511: Cybersecurity
value delivered. AI should augment analysts, not replace them. My Engineering: Advanced Threat
concern is that leadership may see AI as a shortcut to fill staffing gaps, Detection and Monitoring, and
instead of investing in the talent and thoughtful integration of AI SEC411: AI Security Principles and
needed for substantive SOC improvement. VIEW PROFILE Practices: GenAI and LLM Defense.
Cybersecurity teams may not own the risk of AI hallucinations or inaccurate outputs,
but the SOC can play a key role in mitigating their business impact. Governance, risk,
and compliance (GRC) teams need technical support to monitor how AI tools are
used and what systems or data they interact with.
Threat Intelligence
How is CTI data and information being utilized
Threat intelligence activities in your organization? Select all that apply.
are a significant part of SOC
Incident response 225
operations (73%) with the
Vulnerability management 184
primary usage as incident
response (69%). Figure 6 Threat hunting 183
outlines the various ways in Risk management or compliance 180
which CTI data and information Security awareness and user education
178
(including executive awareness)
are being used. CTI information
Prioritizing security controls 173
is typically disseminated
Security operations and network
through email or documents defense (proactively and continuously 168
monitoring for threats)
(56%) and/or reports (55%).
Threat modeling 129
Because threat intelligence Budget and spending prioritization,
96
including staffing and tooling
is largely analysis-driven,
Other 7
respondents were asked about
the analysis methods they Figure 6. Count of Responses on CTI
Data usage Within the Organization
most use. The most common answer (72%) was that analysts use their experience
and intuition. Although expertise is essential, there’s a strong case for incorporating
more structured analytical approaches, such as conceptual or inductive methods, to
improve consistency and reduce bias.
Additionally, most information comes from external sources, indicating there’s a
growing need to generate threat intelligence from internal data sources and not just
rely on external feeds. Leveraging internal data can enhance risk assessment, threat
hunting, and response capabilities. The most effective way to build internal threat
intelligence is through collaboration and information sharing. However, SOC-based
threat intelligence teams may lack organizational support for this. In such cases,
informal peer collaboration can serve as a practical and acceptable alternative.
SANS SOC Survey 2025 10

Incident Response Is Reactive, Not Proactive
The SOC’s incident response capability is primarily described as either fully
integrated as part of the internal SOC (51%) or provided through internal incident
responders who perform ad hoc as needed (48%). The data also showed that
incident response starts are primarily triggered by internal security alerts
(85%). When asked about satisfaction levels for incident response capabilities,
respondents are most satisfied with EDR and adversary containment and are least
satisfied with deception technologies, a consistent trend since 2022. Only AI/ML
tools have ranked worse in recent years.
When asked about threat hunting, the picture was similar. Most teams described
partially automated hunting using vendor-provided tools (48%). Although
technically a form of hunting, this often amounts to retroactive analysis rather than
true, technique-driven hunts. The distinction matters because effective hunting
requires skilled analysts, who remain in short supply. A lack of skilled staff remains
the top-cited barrier for why teams aren’t taking the time to do more sophisticated
hunting (16%). More details on this in the next section.
Running Windows Defender with updated signatures and scanning the file system
is not threat hunting. It’s basic detection. Although historical search capabilities
are improving due to advancements in vendor tools, SOCs need to stop calling this
“hunting.” There’s still real value in doing it the hard way. True threat hunting relies
on proven methodologies, hypothesis-driven analysis, and deep familiarity with
attacker behavior. Alerts are designed to catch known threats, but sophisticated
adversaries don’t always trigger them. They operate quietly, below the detection
threshold—and if you’re not actively hunting, you’re not going to find them.
Running Windows Defender scans isn’t threat hunting, it’s basic
detection. True threat hunting involves hypothesis-driven analysis
and deep knowledge of attacker behavior to uncover stealthy
threats that evade alerts.
SANS SOC Survey 2025 11

SOC Staff and Retention
Despite a growing “return to office” (RTO) trend in the United States, 73%
of respondents indicated that SOC staff can work from home. However,
responses show that if they are permitted, it depends on the specific role
and skill set. In short, although most SOCs support
One of the most common questions SOC leaders
remote work in principle, not every team member
is granted that flexibility—even when the necessary face is: How many people does it take to run a SOC?
technology is in place. The most common answer is 10 (expressed as
SOC teams are perennially short on highly skilled fulltime equivalents) and it’s a good place to start
staff. It’s a continuous struggle, and SOC leaders your planning. This allows for adequate coverage
say their organizations aren’t doing enough to across key functions like monitoring, incident
keep the best people they have. Retention isn’t just
response, threat intelligence, and engineering. Of
an HR issue. It’s a signal of leadership’s priorities.
course, in large, multinational enterprises, SOC
And it’s hard to keep a SOC operating at its highest
teams can easily scale into the hundreds. But for
efficiency and effectiveness if the turnover rate is
most organizations aiming to maintain a solid
too high. If you want your team to stay, show them
internal capability, 10 is the number to plan around.
you’re serious about understanding the factors
that lead to job satisfaction.
While the lack of skilled staff continues to be cited as the top challenge
facing SOCs, 62% of respondents express a clear lack of confidence in
their organization’s ability or willingness to address it through meaningful
retention efforts (see Figure 7). This disconnect highlights a deeper issue:
Retention strategies may
How is human capital addressed in your environment?
exist, but they aren’t visible or
Select the best option.
credible to the people they’re
meant to support. Improving Management listens to the requests of SOC
leads/managers regarding hiring skilled,
transparency around retention 120
experienced staff, but does not understand
programs and demonstrating the urgency to retain these skilled people.
Management pays close attention to the
real follow-through—not just
needs of SOC leads/managers regarding 108
marketing platitudes—can go hiring and retaining skilled, experienced staff.
Management does not pay attention to
a long way toward rebuilding
the unique staffing needs of a SOC and
59
trust and keeping talent in place. does little to encourage hiring skilled,
experienced staff or retain them.
Interestingly, even with this lack of
Management thinks hiring multiple,
confidence, respondents tend to less-skilled employees to stare at alerts 25
is an acceptable strategy for mitigating
stay employed three to five years cybersecurity threats in their environment.
in a SOC environment (31%) with
Other 17
very few staying 10-plus years (4%).
Figure 7. Count of Responses on Retention Efforts
SANS SOC Survey 2025 12

Year-over-year comparisons show that
What is the most effective method you have
compensation and engaging work are
found to retain SOC employees?
increasingly seen as effective retention
strategies. Although career progression Career progression Money Meaningful work
opportunities dipped in importance in 2024,
40%
they appear to be making a strong comeback
in 2025 (see Figure 8). 30%
What SOC Leaders Want 20%
in an Employee
10%
When asked about the most important
0%
technical skill deficit when hiring staff for 2022 2023 2024 2025
technical roles (i.e., which skill is most Figure 8. Effective Methods for Employee Retention
lacking), respondents
identified information
What is the most important technical skill deficit
systems and network security
when you hire staff for technical roles?
(14%) and digital forensics
(12%) as the highest, followed Information systems & network security 13.8%
by a broad range of other Digital forensics 12.0%
Threat analysis 8.1%
competencies outlined in
Data analysis 7.4%
Figure 9. For nontechnical
Incident management 7.4%
skills, risk management Technology fluency 6.0%
topped the list at 14%. Other 6.0%
Data security 5.1%
Vulnerabilities assessment 3.9%
Intelligence analysis 3.7%
Enterprise architecture 3.5%
Computer languages 3.2%
Software development 2.5%
System administration 2.5%
Infrastructure design 1.8%
Mathematical reasoning 1.6%
Collection operations 1.4%
Operations support 1.4%
Database administration 1.2%
Network management 1.2%
Software testing and evaluation 0.9%
Systems integration 0.9%
Encryption 0.7%
Identity management 0.7%
Information technology assessment 0.7%
Physical device security 0.7%
Operating systems 0.5%
Requirements analysis 0.5%
Systems testing and evaluation 0.5%
Target development 0.2%
Telecommunications 0.2%
Figure 9. Skill Deficits
SANS SOC Survey 2025 13

Expert Corner Joshua Wright
SANS Faculty Fellow and
Survey indicates that 62% of SOC professionals say their organization isn’t Author of SEC504: Hacker
doing enough to retain top staff. A great SOC isn’t created by tooling, it’s Tools, Techniques, and
created with culture that recognizes and rewards the analysts who do amazing Incident Handling.
work. When analysts feel connected to the company mission and understand
their contributions are an important part of that mission, they bring the
energy, resourcefulness, and creativity needed to be successful. Managers
VIEW PROFILE
need to recognize the talented analysts who set the model for success at all
levels of technical ability and empower them to be leaders for others to follow.
What’s Hot, What’s Not in SOC Technology
If company leadership isn’t prepared to fully commit the resources to
make a tool effective, it would be better not to deploy it at all. A shiny new
technology that seems like a great solution requires budget, training, time,
and integration into workflow.
Endpoint or extended detection and response (EDR/XDR) once again tops the list for satisfaction,
and it’s the only technology this year to earn a score above a 3 out of 4 (when comparing
technologies used and level of satisfaction). It’s the most fully deployed, most trusted tool in the
stack. EDR/XDR earns high satisfaction ratings because it’s fully deployed, effective for initiating
incident response workflows, and backed by proper training and support.
AI/ML tools continue to underperform. Of the three AI/ML technologies measured, two ranked at
the very bottom, including generative language tools, which scored just a 2 out of 4.
AI/ML tools underperform because they’re new, often introduced without clear ownership or
authorization, adequate deployment budget, or plans for integration into day-to-day operations.
Overall, established tools continue to earn the highest marks. EDR remains the top-rated
technology, because it’s trusted for its reliability and maturity. These are the workhorses
of the SOC: well understood, widely deployed, and proven over time.
In contrast, newer technologies like AI/ML and deception are still
struggling to meet expectations. Satisfaction remains low,
suggesting that although interest is high, real-world
performance and integration haven’t caught up yet.
This is very likely to change over time, and vendors
of AI/ML technology shouldn’t despair. Back in
2017, “asset discovery and inventory” held the
bottom spot and now it’s solidly mid-pack.
Progress for AI is likely.
SANS SOC Survey 2025 14
14

Conclusion: Encouraging Trends,
but There’s Still Work to Do
The 2025 SOC Survey confirms that the SOC is continuing to evolve encouragingly in the
direction of established trends, but very slowly in some areas. Core capabilities are strong,
but the balance still tilts toward reactive work. AI/ML remains underwhelming. Threat
hunting is limited by staffing. And tool satisfaction, as always, depends on full deployment
and thoughtful integration.
The 2025 SOC Survey paints a familiar picture: solid capability, some hopeful trends, but
limited forward motion and ongoing staff dissatisfaction.
What’s clear is that progress takes intention—in hiring, training, architecture, and tool use.
Collecting data is easy. Using it wisely is the hard part.
SOC teams know what they need—tools that work, staff who stay, and time to do more
than respond to alerts. But budget, turnover, and shifting priorities continue to get in the
way. Metrics are tracked, but still manually. Cloud adoption ebbs and flows. AI/ML tools
remain overhyped and under-delivering.
Five Reasons to Be Optimistic
Meanwhile, a growing number of
organizations are defaulting to “just store About the Future of the SOC
everything in the SIEM,” a trend that’s
Widespread 24/7 coverage
easy to justify today and hard to pay for
79% of SOCs now operate around the clock, signaling SOC
tomorrow. It’s a visibility strategy that risks
maturity and commitment to continuous monitoring and
collapsing under its own weight.
support from business stakeholders who recognize the
Tools don’t solve these problems on their seriousness of global cyber threats.
own. People do. And while progress is
Increased cloud use
happening, it’s uneven and often held
Although centralized SOCs are the most common architecture,
back by the same structural issues year migration to cloud resources is reportedly planned for the
after year. The bottom line is that SOCs SOC systems.
aren’t stuck—but they’re not moving fast
Growing reporting of proactive detection
either. Real gains will come from clarity,
Even if it’s still a minority, more teams report using SIEM searches
coordination, and the decision to stop
and threat hunting, not just alerts.
calling retroactive workflows “hunting.”
More clarity on AI/ML use
Organizations are very slowly starting to intentionally integrate
AI/ML tools into workflows, which proves it can be done when
there’s a plan.
Career progression tops retention factors
People want to stay where they are, but only if they see a future.
That’s a call to action for leadership.
SANS SOC Survey 2025 15

Sponsors
SANS would like to thank this survey’s sponsors:
SANS SOC Survey 2025 16

About the SANS Research Program
The SANS Research Program is a key initiative by the SANS Institute and a
premier global provider of cybersecurity research and information. SANS
Research Program is designed to provide cybersecurity practitioners and
leaders with data-driven insights, thought leadership and solutions that
help them better understand and respond to evolving security challenges.
All content is authored by SANS instructor experts from around the world
who apply their years of experience from hands-on practitioner work in the
field, advisory roles and the classroom to provide education, guidance, and
actionable insights that help make the cyber world a safer place.
To learn about Sponsorship opportunities for research and content,
in-person, or virtual events, email us at Sponsorships@sans.org or
go to www.sans.org/sponsorship.
SANS SOC Survey 2025 17

Product Briefings for SOC
The 2025 SOC Survey represents the latest edition of
SANS Institute’s poll of security professionals. The
sponsors of this year’s survey all offer advanced
capabilities that we believe will be of interest to SANS’
clients, and, for this reason, we’re presenting the
following product briefings on a relevant offering.

PRODUCT BRIEFING
Eliminating Alert Fatigue and Empowering
Security Teams with Dropzone AI
Insights from the 2025 SANS Institute SOC Survey
July 2025 ©2025 SANS™ Institute
Organizations face critical gaps that keep their security operations centers (SOCs) Key Findings
reactive and under immense pressure: alert overload and fatigue, staffi ng and
retention crisis, reactive posture and limited threat hunting, and unperforming AI
tools. To secure the organization and outperform attackers, organizations need
sophisticated and automated guidance and support.
Alert Overload and Fatigue
Dropzone AI: Your Autonomous AI SOC Analyst
85% of SOC analysts say endpoint security alerts
Dropzone AI’s AI SOC Analyst is purpose-built to autonomously investigate security are the primary trigger for response.
alerts, addressing these pain points and transforming security operations for 42% of SOCs dump all incoming data into a SIEM,
enterprises and managed security service providers (MSSPs). often without a retrieval or management plan.
Dropzone AI offers a pretrained, autonomous AI SOC analyst that replicates the
investigative techniques of elite analysts and autonomously investigates every
alert. Designed to seamlessly integrate into existing security stacks, Dropzone AI
eliminates the need for playbooks, code, or prompts, delivering fast time-to-value.
Staffi ng and Retention Crisis
Dropzone AI’s process for alert investigation mimics human analysts through three
62% of SOC professionals feel their organization
core stages (see Figure 1): isn’t doing enough to retain top talent.
• Collect—Dropzone AI connects and retrieves relevant data from your fragmented 82% of SOCs are operational 24/7, yet staffi ng for
this continuous coverage is a major challenge. The
security tools and data stack, including email server logs, SIEM, EDR, IAM, IDP, IDS, FW,
most common SOC size is 2–10 people.
and SaaS applications. It leverages over 60 integrations with platforms like Microsoft
Defender, CrowdStrike, Splunk, Google Workspace, Okta, and Palo Alto Networks.
Reactive Posture and
Limited Threat Hunting
48% of teams use partially automated
threat hunting.
Underperforming AI/ML Tools
30% formally use AI/ML tools in the SOC.
42% of SOCs using AI/ML tools don’t tune or
Figure 1. Dropzone AI’s Three Core Stages of Alert Investigation customize the tools.

• Comprehend—Leveraging large language models (LLMs), • A chieving proactive security—By automating triage and
security pretraining, and your organization’s unique investigations, Dropzone AI generates signifi cant time
context, Dropzone AI runs a full end-to-end investigation. savings that SOCs can then reinvest into proactive security
It reasons through investigative threads, from URL activities like true threat hunting. Dropzone AI enables
and attachment analysis to previous organizational SOCs to quickly identify important alerts that are worth
communications. This includes organizational context escalating, further reducing risk.
memory, which learns company-specifi c details like owned
• D elivering on the promise of AI—Unlike many AI tools
IP ranges, allowed VPN services, and critical servers, to
that underperform due to poor integration, Dropzone AI is
ensure tailored and accurate analysis.
designed for seamless, no-code integration with existing
• Conclude—Dropzone AI generates detailed, decision-ready security tools via APIs. It includes guardrails to protect
reports with a severity conclusion, executive summaries, against hallucinations and prioritizes explainability and
and key evidence, providing full insights in plain English. data lineage, ensuring humans can easily verify decisions
Human analysts can quickly validate the AI’s logical and the evidence on which they are based. This intentional
reasoning based on a complete report of crucial factors integration ensures Dropzone AI provides meaningful
and a chain of raw evidence to support its conclusion. support and helps organizations fi nally realize the potential
of AI in their security operations (see Figure 2).
In addition, the Dropzone AI system can be
confi gured to take automatic containment
actions, such as blocking IPs or disabling users.
The system learns from user feedback and
previous investigations.
Addressing SOC Challenges Head-On
Dropzone AI directly tackles the most pressing
challenges identifi ed in the 2025 SANS SOC Survey,
delivering concrete benefi ts to security teams:
• Eliminating alert overload and reducing
mean time to resolution (MTTR)—Dropzone
AI reduces manual alert analysis time by 95%.
Figure 2. Dropzone AI’s AI-Driven Alert Investigation with Detailed Reports and Evidence
By automating Tier 1 alert triage, it dramatically
• C omprehensive coverage and seamless integration—
shortens MTTR by up to 90%, from hours to minutes. This
Dropzone AI supports a wide range of alert types, including
allows SOCs to achieve 100% alert coverage, ensuring no
phishing, endpoint, network, cloud, identity, and insider threat.
alerts, even low-severity ones, go uninvestigated.
• B uilt for trust and security—Dropzone AI is SOC 2 Type 2
• Empowering analysts and boosting retention—Dropzone
certifi ed and employs a single-tenant architecture with no
AI acts as a “Tier 1 SOC analyst always in the zone,”
data comingling. Critically, Dropzone AI does not use any
handling the repetitive, time-consuming investigations.
customer data to train its AI models or its sub-processors’
This frees up human analysts for higher-value work, such
models and contractually prohibits its LLM providers from
as threat hunting, policy updates, incident response
storing or retaining customer data beyond immediate query
planning, and strategic projects. By reducing burnout
processing. Dropzone AI encrypts data at rest and in transit
and increasing job satisfaction, Dropzone AI can help
and undergoes annual third-party penetration tests.
organizations retain top talent and make the SOC analyst
job more enjoyable. Furthermore, it speeds up the Dropzone AI is a trusted teammate that adapts to your
onboarding of junior analysts, allowing them to learn from environment, works 24/7, and always shows its work, bringing
Dropzone AI’s investigations and quickly understand the unlimited intelligence to your analysts for fast, detailed, and
environment and available data sources. accurate investigations.
Empower your SOC. Transform your security operations.
To experience Dropzone AI autonomously investigating security alerts, try the self-guided demo at
www.dropzone.ai/self-guided-demo or forward a suspicious email to scan@try-dropzone.ai for a tailored analysis report in minutes.
Note that SANS Product Briefi ngs do not represent a SANS endorsement of a sponsor or its products, but rather an overview of its offerings and their capabilities.

PRODUCT BRIEFING
Elevate Your SOC with Elastic Security’s
AI-Driven Capabilities
Insights from the 2025 SANS Institute SOC Survey
July 2025 ©2025 SANS™ Institute
Security operations centers (SOCs) are contending with a multitude Key Findings
of signifi cant challenges—from the sheer volume of incoming data to
staffi ng woes and the practical integration of advanced technologies—
that hinder their effectiveness and put organizations at heightened
risk. Key challenges facing modern SOCs include overwhelming alert
fatigue and low signal-to-noise ratio, persistent cyber skills shortages
and staffi ng defi ciencies, challenges with data onboarding and legacy
SIEM lock-in, underperformance and underutilization of AI tools,
Overwhelming Alert Noise
reactive incident response, and limited proactive threat hunting.
85% of SOC analysts say endpoint security alerts
are the primary trigger for response.
Addressing Core SOC Challenges
with AI-Driven Solutions 42% of SOCs dump all incoming data into a SIEM,
often without a retrieval or management plan.
Elastic specifi cally designed its AI and automation features to tackle
these real-world problems head-on.
• Attack Discovery is an innovative feature that holistically assesses
incoming alerts to reveal advancing attacks, guiding analysts to
stop them. Instead of individual one-off events, Attack Discovery
processes alerts as a cohesive narrative, enabling analysts to
prioritize actual attacks, not just isolated alerts. It automates the Persistent Cyber Skills Shortage
time-consuming task of alert triage and suggests the next steps
62% of SOC professionals feel their organization isn’t
for investigators. Using LLMs, Attack Discovery surfaces, labels, and
doing enough to retain top talent.
maps to MITRE ATT&CK™ the most signifi cant attacks. This provides
16% say a lack of skilled staff is the top barrier
a simple, quick summary of the attack chain and details the
to threat-hunting.
chronological order of events, vastly accelerating the investigation
process. Attack Discovery reduces the triage time for hundreds of
alerts from hours to minutes or seconds.
• Elastic designed the AI Assistant for Security to make every user
a power user, elevating every practitioner regardless of their
experience level. It guides analysts through triage, investigation,
and response, and assists administrators with routine tasks. The AI Slow Data Onboarding and
Assistant provides a natural language interface for query generation. Legacy SIEM Migration
This provides actionable guidance, tailored to the organization-
Organizations often struggle to quickly integrate
specifi c knowledge through retrieval augmented generation (RAG), custom data sources and migrate existing
and much more (see Figure 1 on the next page). detection rules from legacy SIEMs.

• E lastic’s Automatic Import enables rapid
onboarding of custom data sources in
minutes, not days. This feature uses
AI to develop, test, and tweak new
integration packages until they pass
validation, expanding visibility and
powering detection rules with minimal
manual effort. Elastic ships with over
400 prebuilt data integrations, but
for unique custom logs, Automatic
Import provides a seamless capability
that reduces the time to collect and
normalize a new data source from one
to four days to just 10 minutes.
• Automatic Migration minimizes the
Figure 1. Automatic Query Generation
time and expertise needed to move
legacy detection rules to Elastic Security, streamlining SIEM • Security and privacy—Elastic prioritizes data safety, making it
adoption and reducing risk. It expedites the translation of easy for organizations to anonymize or redact confi dential data
complex rules, including lookups and macros, and ensures by default and as needed, with document-level control. This
detection continuity by minimizing translation errors. It prevents accidental relaying of sensitive internal data by analysts.
also helps streamline rule upkeep by mapping legacy SIEM
detections to Elastic Security Labs’ prebuilt rules. This The Tangible Impact of Elastic AI in the SOC
feature can create or convert a detection rule in 15 minutes, Elastic’s AI capabilities ensure SOC teams can focus on fi nding and
down from one to three hours. Automatic troubleshooting stopping threats, rather than being bogged down by data wrangling
leverages LLMs to detect confl icting EDR and AV software or schema modifi cation. AI acts as an acceleration of the team, not
running on a host with Elastic Defend and suggests a replacement for analysts.
processes to be trusted to resolve the confl ict.
Real-world results demonstrate the power of Elastic’s AI:
Powered by the Elastic Search AI Platform • Sitecore has automated 96% of its security workfl ows with Elastic.1
Elastic’s AI capabilities are built upon the robust Elastic Search AI • Profi cio has seen a 34% improvement in alert triage time.2
Platform, which acts as a powerful vector database. This platform • The Texas A&M University System saves over 100 analyst hours
safely surfaces hyper-relevant knowledge, enabling public per month by automating documentation and other security
LLMs to perform as if custom-trained for private use cases. processes with Elastic Security.3
• RAG—A core component, RAG grounds responses in • Studies indicate that Elastic’s security solutions have:
proprietary data by enriching user prompts with real-time
- Reduced false-positive security alerts by 75%
organizational context. This approach provides meaningful
- Reclaimed 74% of full-time security employee hours with AI
results without the need to build and retrain bespoke LLMs
- Reduced security incidents by 90%
on constantly changing internal data. Elastic uses its search
- Reduced annual risk exposure by 36%
capabilities to retrieve and surface uniquely relevant data to
the LLM, ensuring accurate and helpful answers. Elastic is uniquely positioned to help SOC teams harness generative
AI by providing LLMs access to an unrivaled corpus of information,
• Flexible LLM connectors and ecosystem—Elastic
retrieving uniquely relevant data, and dramatically reducing the
understands that the state of generative AI is rapidly
cost and complexity of data collection, storage, and analysis.
evolving. It provides fl exibility through a growing set of
integrated models and services, including Google Vertex AI, Elastic Security’s AI capabilities empower SOC teams to gain
OpenAI, Amazon Bedrock, and Azure OpenAI Service and an unfair advantage, accelerating onboarding, triaging alerts
also offers a managed LLM out of the box. The multitude of down to critical attacks in seconds, and boosting productivity by
choices ensures users can control cost, speed, accuracy, and augmenting analyst and admin expertise with generative AI. This is
privacy, now and in the future. the future of SIEM, delivered today.
1 “Sitecore wins new business, reduces costs, and accelerates security operations with Elastic,” www.elastic.co/customers/sitecore-security
2 “Profi cio protects global customers with advanced cyber threat detection and response tools from Elastic Security,” www.elastic.co/customers/profi cio
2 “The Texas A&M University System protects students, emergency responders, and leading research institutions with Elastic Security,”
www.elastic.co/customers/tamus
Note that SANS Product Briefi ngs do not represent a SANS endorsement of a sponsor or its products, but rather an overview of its offerings and their capabilities.

PRODUCT BRIEFING
Fortinet SecOps Platform: Unifi ed AI-Driven
Security for Modern Threat Landscapes
Insights from the 2025 SANS Institute SOC Survey
July 2025 ©2025 SANS™ Institute
Modern security operations centers (SOCs) face formidable hurdles in Key Findings
defending against an increasingly sophisticated and pervasive threat
landscape. Attack campaigns are continuously evolving in their tactics and
procedures, making detection more diffi cult. The expansion of digital presence,
including remote work environments, connected IoT/OT devices, and cloud
applications, signifi cantly broadens the attack surface. This growing complexity
leads to an overwhelming volume of security products, information, and alerts,
making it challenging for security teams to identify genuine threats amidst
the noise. Furthermore, a persistent industry-wide shortage of cybersecurity Alert Overload and Fatigue
expertise frequently results in overburdened security teams, hindering their
85% of SOC analysts say endpoint
ability to effectively manage and respond to these complex threats.
security alerts are the primary trigger
for response.
The Fortinet Security Operations (SecOps) Platform
Fortinet designed its Security Operations (SecOps) Platform to provide
comprehensive, AI-driven security for organizations at any stage of their
security journey. It seamlessly integrates behavior-based sensors to detect
and disrupt threat actors across the entire attack surface and along the cyber
kill chain. Backed by FortiOS, Fortinet’s operating system, the platform delivers
centralized investigation and remediation SecOps teams can orchestrate,
automate, and augment to reduce cyber risk, cost, and operational effort. Staffi ng and Retention Crisis
This platform offers a broad range of sensors that use AI and other advanced 62% of SOC professionals feel their
analytics to continuously assess activity across devices, users, fi les, networks, organization isn’t doing enough to
email, applications, clouds, logs, retain top talent.
and even the dark web, helping to
identify signs of cyber threats. This
approach fundamentally shifts the
security operations paradigm from
merely “detect and respond” to
“detect and disrupt,” followed by
“investigate and respond,” resulting
in faster containment and more Suboptimal Integration and
time for thorough investigation and Underperformance of AI/ML Tools
comprehensive remediation. The in SOC Operations
platform unifi es and automates threat 42% of SOCs using AI/ML tools don’t
response using AI-driven analytics, tune or customize the tools.
threat intelligence, and generative AI
40% of SOCs report using AI/ML tools, but
(GenAI) assistance (see Figure 1).
they are not part of the defi ned workfl ow.
Figure 1. Fortinet SecOps Platform

Fortinet SecOps Platform: Directly
Tackling the SOC’s Pressing Challenges
Fortinet SecOps Platform directly addresses the most
pressing challenges identifi ed in the 2025 SANS SOC
Survey, delivering concrete benefi ts to security teams
(see Figure 2):
• Fortinet’s platform uses AI-powered detection
to improve accuracy and reduce false
positives. FortiAI-Assist is designed to prioritize
notifi cations, suppress duplicate alerts, and only
fl ag high-confi dence threats, directly combating
alert fatigue.
Figure 2. Fortinet SOC Automation
• Fortinet designed its SecOps solutions for rapid detection,
investigation, and response. Timely protection and proactive
The platform’s proactive exposure assessment, defense are a result of AI-powered security and GenAI
comprehensive threat intelligence, and AI-powered assistance built into analyst workfl ows, which expedites
analysis include: incident management and threat hunting.
• AI-driven security and automation reduces cyber risk • Fortinet’s SecOps Platform provides broad sensors to avoid
by speeding detection and containment, as well as blind spots. It offers continuous threat exposure management
investigation and remediation. The FortiAI GenAI assistant and complete digital asset visibility through automated
is built into analyst workfl ows to inform and expedite discovery and monitoring.
incident management and threat hunting. This includes
• Fortinet’s automation and augmentation speeds response and
capabilities like automated alert triage, adaptive threat
eases the burden on in-house security teams. FortiAI-Assist
hunting, root-cause tracing, and auto confi guration.
boosts analyst effectiveness by providing instant answers and
• Complete digital asset visibility with automated asset detailed guidance as well as automating tasks like alert triage,
discovery and monitoring offers real-time insights into confi guration, and policy creation, enabling security teams to
networks, cloud environments, and web applications. be more effi cient and consistent.
Advanced analytics and risk scoring help prioritize
• Fortinet’s SecOps Platform supports adaptive threat hunting
vulnerabilities and strategically allocate resources.
by scanning logs, network traffi c, and user behavior for threats
• Comprehensive threat intelligence from FortiGuard Labs, without constant human input. Solutions like FortiDeceptor
an elite research team with over 15 years of AI experience, offer deception-based breach protection for early detection
provides proactive risk mitigation and ensures security and isolation of sophisticated attacks, while FortiNDR identifi es
teams stay ahead of potential attackers. incidents in progress based on anomalous network activity.
• Rapid incident response aims to signifi cantly reduce The Fortinet SecOps Platform is a fl exible, integrated solution that
detection and response times. With correlated alerts, unifi es and optimizes threat response using GenAI and AI-driven
reduced attack surface, and improved overall visibility, analytics, threat intelligence, and automation. FortiAI-Assist,
the Fortinet SecOps Platform can achieve an average Fortinet’s GenAI offering, is embedded throughout the Fortinet
time to detect and contain threat actors of one hour and Security Fabric, combining intelligent analytics and automation to
an average time to investigate and remediate incidents accelerate detection, reduce overhead, and improve operational
of 11 minutes. effi ciency at AI speed.
• C onsolidated platform and seamless integration with Customers choose Fortinet for its comprehensive security
Fortinet’s broad range of security products provides solutions, which have proven to deliver signifi cant operational
a single vendor look to security operations. Fortinet effi ciencies and improved risk management. Case studies
Security Fabric enables deeper visibility, offers a wider illustrate how Fortinet solutions help organizations cut outages,
range of actions, and supports 500-plus connectors for identify network weaknesses, streamline network management,
multivendor security infrastructure. and drastically reduce suspicious emails.
Note that SANS Product Briefi ngs do not represent a SANS endorsement of a sponsor or its products, but rather an overview of its offerings and their capabilities.

PRODUCT BRIEFING
Infoblox Threat Defense: Preemptively Blocking
Threats and Unifying Security Operations
Insights from the 2025 SANS Institute SOC Survey
July 2025 ©2025 SANS™ Institute
Organizations are drowning in security alerts despite massive investments in Key Findings
cybersecurity tools. Security operations center (SOC) teams battle overwhelming alert
fatigue as multiple systems fl ood security information and event management (SIEM)
platforms with duplicates and false positives, driving up costs while ransomware
and breaches persist. Meanwhile, fragmented security across hybrid and multicloud
environments leaves blind spots at critical egress points. Without clear attribution
linking malicious activity to specifi c users and devices, incident response crawls to a
halt just when speed matters most.
Alert Overload and Fatigue
Infoblox Threat Defense:
42% of SOCs dump all incoming data into
The Foundational Protective DNS Solution a SIEM, often without a solid plan for
retrieval or management.
Infoblox Threat Defense directly addresses these pervasive challenges by leveraging
the critical role of DNS as the fi rst point of detection for cyberattacks. By blocking
attacks early, Infoblox Threat Defense reduces the volume of malicious traffi c
reaching downstream security tools and the number of alerts they generate.
The core strength of Infoblox Threat Defense lies in its predictive DNS threat intelligence
and advanced algorithmic protections, enabling it to detect threats before other tools and
that other tools often miss. This preemptive approach transforms security effectiveness
Fragmented Security and
by putting DNS at the center of protecting all infrastructure, from cloud to core.
Lack of Unifi ed Visibility
Key Capabilities and Preemptive Power
85% of SOC analysts say endpoint
security alerts are their
• Preemptive and predictive protection, which enables detection and disruption
primary trigger for response.
of cybercrime often before attacks are even launched. Infoblox can block 82% of
threats before the fi rst DNS query. Furthermore, Infoblox identifi es high-risk or
suspicious domains an average of more than two months before the rest of the
industry confi rms them as malicious, while maintaining an ultra-low false-positive
rate of 0.0002% out of more than 20 million indicators.
• Comprehensive DNS monitoring with full DNS behavior monitoring to meticulously
track all DNS record types for malicious activity
Slow and Ineffi cient
• Lookalike domain detection and mitigation to proactively identify and mitigate
Incident Response
lookalike/doppelganger domains, which are frequently used in phishing and other
69% of SOCs still rely on
advanced targeted attacks to deceive users and compromise brands
manual or mostly manual processes
• Z ero-day DNS protection that identifi es new or emerging domains that could pose a to report metrics.
threat to an organization, offering protection against previously unknown threats

• Behavior-based DNS tunneling detection, which often is per month. In fact, customers have reported as much as a
used for data exfi ltration/infi ltration and command and 50% reduction of alerts on next-generation fi rewalls (NGFW)
control (C2) communications and endpoint detection and response (EDR) tools alone.
The reduction in alerts and increase in productivity drives
• Proactive suspicious/high-risk domain protection that
both employee cost savings—as much as $400,000 per
identifi es and preemptively blocks suspicious domains that
year—and a concomitant reduction in data sent to SIEMs,
are likely to be used in future malicious campaigns
which further reduces costs.
• Proactive threat distribution systems (TDS) detection
• E nhanced security ecosystem integrations—Infoblox
and disruption, which is used to identify threat actor TDS
Threat Defense maximizes existing security investments by
infrastructure to counter threat actors rotating across
seamlessly integrating with various tools across the security
numerous domains to evade detection
stack, including SIEM; security orchestration, automation,
• Simplifi ed and intuitive UI that lets security teams
and response (SOAR); vulnerability management (VM);
understand what’s happening within their environment and
threat intelligence platforms (TIP); network access control
suggest ways to decrease security risks
(NAC); NGFW; IT service management (ITSM); and IT
• “ Protection Before Impact” monitor that enables CISOs and operations management (ITOM). This breaks down silos,
security teams to confi dently report to the board with clear, enhances threat detection, automates workfl ows, and
quantifi able metrics on threats neutralized before impact improves response capabilities across hybrid, multicloud,
and on-premises environments, addressing the pervasive
Automating Asset discovery, Context and
challenge of fragmented security.
Enhancing SOC Effi ciency
• I mproved threat intelligence utilization—The SANS SOC
Infoblox Threat Defense enhances SOC effi ciency through
survey highlights that 69% of SOCs primarily use cyber
intelligent automation and AI-driven analytics. With automatic
threat intelligence (CTI) data for incident response. Infoblox
asset context enrichment, correlating network context
provides highly accurate, predictive DNS-based threat
without the need for clients or sink holing, it provides direct
intelligence, fi lling potential gaps in an organization’s CTI
attribution to impacted users, devices and cloud workloads
and signifi cantly enhancing incident response capabilities.
that is crucial for accelerating
investigations.
Infoblox applies AI-driven
analytics to correlate DNS
threat and asset data. It
distills tens of thousands
of alerts into a handful of
actionable SOC insights,
alleviating the need for
manual processes to
report metrics and analyze
incoming data. By automating
correlation and triage,
Figure 1. Integrating Infoblox Threat Defense into the Environment
Infoblox drastically reduces the amount of data sent to SIEM
systems and the time required for remediation (see Figure 1).
Infoblox Threat Defense, whether deployed on premises, in
Tangible Benefi ts and Accelerated ROI
the cloud, or in a hybrid model, offers foundational security
Infoblox Threat Defense transforms security operations for protection anywhere, enabling organizations to take a
(SecOps) and provides a strong return on investment: more proactive stance against evolving cyber threats.
• Substantial manpower and cost savings—By blocking To learn more about how Infoblox Threat Defense can strengthen
threats much earlier and reducing alert volume, Infoblox your cybersecurity posture and uplift SecOps effi ciency, talk
Threat Defense saves SOC analysts an average of 500 hours to an expert or enroll in a security workshop today.
Note that SANS Product Briefi ngs do not represent a SANS endorsement of a sponsor or its products, but rather an overview of its off erings and their capabilities.

PRODUCT BRIEFING
Prophet Security: The AI Force Multiplier
That Accelerates Security Operations
Insights from the 2025 SANS Institute SOC Survey
July 2025 ©2025 SANS™ Institute
Security operations centers (SOCs) are frequently overwhelmed Key Findings
by an unmanageable infl ux of security alerts, leading to a state
of alert fatigue that hinders their ability to effectively triage
and investigate every potential threat. This often necessitates
extensive manual effort to piece together fragmented data from
disparate systems, consuming valuable analyst time on repetitive
tasks rather than proactive defense. The resulting alert fatigue 30% of SOCs
contributes to a backlog of alerts, increasing the risk of critical identify lack of skilled staff or high staffi ng
incidents being missed. Furthermore, existing automation and requirements as their biggest challenge
orchestration tools often prove complex to implement and
diffi cult to maintain, plus they lack the adaptability required to
keep pace with evolving attacker techniques.
The Prophet AI SOC Platform: A Smarter, 69% of SOCs
Scalable SOC Powered by Agentic AI continue to depend on manual or largely
manual processes for reporting metrics.
Prophet Security designed its AI SOC platform to revolutionize
how SOCs function, transforming manual, resource-intensive
processes into streamlined, AI-powered workfl ows that
empower analysts and enhance an organization’s security
posture (see Figure 1).
18% of SOCs
call out a silo mentality between incident
response and operations, lack of context, or
too many alerts as their biggest challenge
13% of SOCs
cite a lack of adequate orchestration and
Figure 1. Prophet AI SOC Platform automation as their biggest challenge

Prophet AI’s workfl ow is structured around fi ve key stages: Accelerating Security Operations by
Addressing Key Challenges
• Plan: Prophet AI immediately deduplicates and
summarizes incoming alerts, extracts key artifacts,
Extend the Impact of Your Existing Team
classifi es them, and dynamically constructs an
The 2025 SANS SOC Survey underscored a persistent
investigation plan. This plan outlines the critical
talent gap in security operations. Teams are either
questions an expert analyst would typically ask to
understaffed or stretched thin. Prophet AI SOC Platform
determine if an alert is a true or false positive.
addresses this head on by offering an expert-level AI
• Investigate: Emulating an expert analyst, Prophet
SOC Analyst capable of autonomously triaging and
AI executes the investigation plan by autonomously
investigating every alert. By eliminating manual, repetitive
retrieving, correlating, and analyzing relevant
effort, the platform allows existing teams to scale their
information. It gathers context from diverse sources,
capacity and focus on the most impactful tasks.
including SIEMs, security data lakes, security tools,
and object storage, to arrive at its conclusions. Move Beyond Playbooks to
Furthermore, its “Dig Deeper” capabilities allow True Investigative Automation
analysts to ask additional questions about a single
Automation in many SOCs is either too rigid or too
investigation or across multiple investigations,
shallow to handle complex, dynamic investigations.
or to create custom investigations using existing
The Prophet AI SOC Platform goes beyond traditional
playbooks. Prophet AI Threat Hunter works with
playbooks or prompt-based AI chatbots by using agentic
your team to perform the collection, processing, and
AI to conduct end-to-end investigations in under three
lead generation of hypothesis-driven threat hunting
minutes, compared to a 30-minute industry average. This
activities across your environment.
drastically reduces dwell time and MTTR.
• Respond: After completing an investigation, Prophet
Reduce Noise, Add Context, Connect the Dots
AI assigns a severity level based on its fi ndings,
The Prophet AI SOC Platform cuts through the noise by
prioritizing critical alerts for immediate attention. It
prioritizing the alerts that matter most and surfacing
provides concrete, one-click remediation steps to
them with full context. Its AI SOC Analyst rapidly analyzes
accelerate response. Prophet AI integrates seamlessly
telemetry, correlates signals across tools, and presents
with existing collaboration and case management
clear investigative fi ndings for human review.
tools to ensure rapid adoption and minimal
disruption to current workfl ows. See how the Prophet AI SOC Platform can help your team
investigate faster, reduce noise, and focus on what really
• Adapt: Prophet AI continuously learns and adapts to
matters. Request a demo to experience agentic AI built
the environment by ingesting organizational context
for security operations.
from analyst feedback, ensuring the system refi nes its
accuracy and effectiveness over time.
• Report: The platform provides a real-time view of
critical SOC metrics, such as alert dwell time, and Mean
Time to Investigate (MTTI) and Mean Time to Respond
(MTTR). Additionally, Prophet Security’s Detection
Advisor identifi es the noisiest alerts and detection
gaps, providing insights to detection engineering teams
for alert tuning and optimization.
Note that SANS Product Briefi ngs do not represent a SANS endorsement of a sponsor or its products,
but rather an overview of its offerings and their capabilities.

PRODUCT BRIEFING
Streamlining Security Operations
with Swimlane Turbine
Insights from the 2025 SANS Institute SOC Survey
July 2025 ©2025 SANS™ Institute
Security operations centers (SOCs) face a perfect storm of Key Findings
challenges just when organizations need them most: talent
hemorrhaging, data chaos, and operational blindness.
Top SOC analysts leave faster than they can be replaced, taking
critical expertise with them. Meanwhile, poorly managed security
information and event management (SIEM) systems inundate
teams with false positives, making it nearly impossible to spot
62% of SOC professionals believe their organization
real threats. Manual reporting processes leave leadership blind
isn’t doing enough to retain top staff.
to operational health, creating a vicious cycle of overwhelmed
teams and persistent staffi ng shortages, all while cyber threats
become increasingly sophisticated.
Swimlane Turbine: The AI Automation Platform
for Every Security Function
42% of SOCs dump all incoming data into a SIEM system,
Swimlane Turbine, an AI hyperautomation platform for every
often without a solid plan for retrieval or management.
security function, provides powerful AI-driven solutions to
address these critical gaps, enabling SOCs to operate with
unprecedented effi ciency, scale, and effectiveness. Swimlane
provides a robust set of capabilities, through the Turbine
platform, that streamline and enhance security operations
across the board:
• Hero AI is a collection of agentic and generative AI
85% of SOC analysts state that alerts from endpoint
capabilities in Turbine, built on the private Swimlane LLM. security tools are their primary trigger for response.
Hero is contextually aware and trustworthy. Its AI functions
can act as an AI assistant for any role, with capabilities
including summarizing cases, recommending actions
based on case data and Knowledge Base (KB) articles, and
generating executive summaries and after-action reports—
all while ensuring that sensitive customer data is not sent
to third parties or used to train the model (see Figure 1 on
69% of SOCs still rely on manual or mostly manual
the next page). processes to report their metrics.

Swimlane Solves the SOC’s Critical Challenges
Swimlane addresses the pain points that surfaced in the
2025 SANS SOC Survey with targeted solutions that deliver
measurable results for security teams. Turbine picks up
precisely where the SIEM leaves off, utilizing AI automation to
handle the “last mile” of alert triage and incident response
for signals originating from the SIEM or endpoint security
controls, thereby reducing dwell time and accelerating
response. The Swimlane SOC Automation Solution
signifi cantly reduces alert volume, achieving a 95% reduction
in SIEM, EDR, and XDR alerts.
Acting as a comprehensive system of record for the SOC,
Swimlane Turbine provides highly composable and self-
documenting dashboards that offer real-time visibility to
Figure 1. Swimlane Hero Chat Interface
SOC leaders, analysts, vulnerability management teams,
• Swimlane Turbine Canvas is the platform’s low-code playbook- compliance teams, and beyond. Swimlane provides an
building studio. It allows users to build playbooks three times environment-agnostic tool that can integrate with all other
faster using modular and reusable components. To further sources to pull in data, ensuring that teams don’t have to
accelerate automation building, users can download and navigate disparate tools to collect metrics. Swimlane provides
edit more than 2,500 prebuilt playbooks in the Swimlane visibility into both SOC KPIs, the actions taken, and the
Marketplace. Using conditional logic, Swimlane Turbine can decisions made during incident response.
trigger playbooks based on a variety of events and offers no-
The Swimlane Turbine platform promises a 240% return on
code capabilities such as data transformation, conditional logic,
investment (ROI) in the fi rst year with fast and seamless
parallel execution, schema inference, and more. It also allows
implementation, professionally implemented by Swimlane
for custom HTTP actions, enabling integration with any API.
in two to four weeks. Additionally, customers can expect
Robust debugging and testing functionalities are integral to the
a 20% increase in effi ciency when using Hero AI. Leading
playbook-building experience.
cybersecurity professionals have endorsed Swimlane,
• Swimlane Turbine offers robust and customizable AI-driven with feedback highlighting its ability to provide a robust
case and incident management, serving as a single system of look into the environment, enhance analyst effi ciency,
record for the SOC and streamlining incident response from unify diverse customer environments, and serve as the
escalation to resolution. The case management application powerhouse of the SOC.
enables analysts to focus on the most relevant data points while
By taking mundane, tedious, and dreaded work off analysts’
maintaining access to raw payload data. The system integrates
plates, Swimlane Turbine enables analysts to focus on
human intelligence by referencing KB and supports the
strategic tasks that foster career growth. This makes AI
correlation of alerts using fuzzy hashing to link similar incidents.
automation a powerful enabler for career development
• The platform allows for the enrichment and normalization of and retaining top talent. AI can empower a junior analyst to
indicators of compromise (IoCs) from any source. Swimlane operate at a level far beyond their years, accelerating their
Turbine integrates with third-party threat intelligence platforms professional development. Furthermore, when turnover
(TIPs) to enhance the effectiveness of existing feeds. It inevitably occurs, AI automation can pick up the slack.
maintains a reciprocal reference between IoCs and cases, Swimlane customers have reported that with Turbine, they
enabling SOCs to see trends and commonalities for improved can operate at the capacity of 20-plus additional SOC analysts
threat hunting. compared to their previous SOAR/SIEM bundled platforms.
• Swimlane Turbine is built for speed and scalability, enabling it By addressing critical challenges in staff retention, alert
to execute 25 million daily actions for a single customer. With management, and operational visibility, Swimlane Turbine
a multi-tenant architecture, enterprises and managed security empowers SOCs to move beyond reactive operations,
service providers (MSSPs) can maintain strict data isolation and enabling them to achieve true hyperautomation and deliver
privacy for each customer or business function. faster, smarter, and more proactive security outcomes.
Note that SANS Product Briefi ngs do not represent a SANS endorsement of a sponsor or its products, but rather an overview of its offerings and their capabilities.

PRODUCT BRIEFING
Empowering Threat and Risk-Informed
Cyber Defense with ThreatConnect
Insights from the 2025 SANS Institute SOC Survey
July 2025 ©2025 SANS™ Institute
Security operations centers (SOCs) are constantly under pressure, grappling Key Findings
with a multitude of challenges that hinder their ability to effectively detect,
prioritize, and respond to threats. SOC analysts are often overwhelmed
by the sheer volume of alerts and disparate data sources, struggling
to identify what is truly relevant amidst the noise. All too frequently,
they miss critical threats and waste valuable time on false positives.
Furthermore, security leaders persistently fi nd it diffi cult to demonstrate
the tangible value of cybersecurity investments to leadership in business
terms, making it challenging to secure necessary resources and combat 62% of SOC professionals say their organization
the high rates of staff burnout and turnover that plague the industry. isn’t doing enough to retain staff.
ThreatConnect’s Integrated Approach: The Intel Hub
ThreatConnect offers a comprehensive approach to cyber defense,
integrating threat intelligence, risk quantifi cation, and security
operations to build cyber resilience and enhance security effectiveness,
effi ciency, and collaboration. ThreatConnect designed the Intel Hub to
Lack of skilled staff continues to be cited as the
address these critical challenges by combining three core products:
top challenge facing SOCs.
Threat Intelligence Operations (TI Ops), Risk Quantifi er (RQ), and Polarity,
bringing together threat intelligence, cyber risk management, and
security operations teams to foster effective, effi cient, and collaborative
cyber defense, powered by AI.
• TI Ops moves beyond traditional threat intelligence platforms
(TIPs) by operationalizing all intelligence for faster, more precise
detection and response. It aggregates, normalizes, and enriches
69% of SOCs use cyber threat intelligence (CTI)
intelligence from over 300 open, commercial, and internal sources
data primarily for incident response.
using AI, making the intelligence actionable and ready for querying.
TI Ops helps create a unifi ed threat library, provides AI-powered
analytics, automates analyst work with playbooks, and enables
visualization of threat actor behaviors. With built-in reporting for
effective dissemination of intelligence, TI Ops also enables CTI teams
to manage threat intelligence and inform security operations and
leadership. Thanks to its innovative Intelligence Requirements feature,
it’s the only solution that streamlines the entire threat intelligence life 69% of SOCs still rely on manual or mostly
cycle end to end (see Figure 1 on the next page). manual processes to report metrics.

• RQ quantifi es cyber risk in fi nancial terms,
enabling organizations to make better
decisions, prioritize vulnerabilities and
actions, and communicate effectively
with leadership. RQ analyzes real-world
risk, loss, and attack data and uses AI to
automate cyber risk analysis and provide
defensible fi nancial impact insights.
This ensures that security leaders can
prioritize risk remediation for maximum
impact, communicate ROI of cybersecurity
investments in business terms, and Figure 1. ThreatConnect TI Ops
understand material risk.
The survey reveals a signifi cant concern about staff retention and burnout
• Polarity is an investigative assistant that unifi es threat
in SOCs. ThreatConnect tackles this by focusing on capacity management,
intelligence, context, and knowledge at the point of
automating mundane tasks, reducing cognitive load, and empowering SOC
analysis and decision-making. It acts as a federated search,
teams to prove their value to the business in the following ways:
correlation, and analysis tool that scans what analysts
are looking at across any application, including images • ThreatConnect’s highly scalable playbook automation runs in the
or videos, using OCR to extract text and instantly search background, handling repetitive tasks like enriching indicators or performing
hundreds of data sources. This streamlines investigations fi rst-pass triage. This frees analysts to focus on more complex, fulfi lling, and
by providing a consolidated summary view, eliminating meaningful work, which directly contributes to job satisfaction and retention.
the need to learn complex query languages,
and reducing context switching and cognitive
overhead for analysts (see Figure 2).
Solving Key Pain Points with
ThreatConnect
ThreatConnect directly addresses the critical
fi ndings identifi ed in the SANS SOC Survey,
focusing on improving the effectiveness and
retention of security teams.
The SANS survey highlights that AI/ML tools
often underperform due to lack of clear
ownership and poor integration into daily
operations. ThreatConnect’s philosophy is that
AI is a tool, not an end, and they apply AI only
Figure 2. ThreatConnect Polarity
where it can securely, safely, and effectively
solve known customer problems: • Polarity directly contributes to reducing analyst burnout by minimizing
context switching. Instead of navigating between multiple tools and
• ThreatConnect uses AI to correlate and enrich data across
windows, Polarity provides a single window for federated search across all
sources, uncover meaningful relationships, and classify
data and intelligence sources, streamlining investigations and providing
unstructured intelligence into consistent, structured data.
instant context. This drastically cuts down time on tasks and enables faster
This helps map intelligence to specifi c industries or attack
decision-making.
techniques, making it easier for analysts to fi nd relevant
information without sifting through massive volumes of data. • ThreatConnect enables SOC teams to prove their value to the business by
translating cyber risks into fi nancial terms using Risk Quantifi er. By aligning
• Polarity uses AI to accelerate analyst workfl ows by
security activities and resources with business priorities, the platform helps
delivering quick, plain-English summaries of intelligence
security teams focus on threats that pose the greatest fi nancial impact. This
reports and tailoring insights for different stakeholders.
allows SOC teams to show tangible ROI for their efforts, which can lead to
Unlike traditional approaches that require direct
increased budget, more competitive salaries, and greater investment in the
integrations with each system, Polarity overlays any tool on
team, all contributing to better retention.
the analyst’s desktop, scanning what’s on the screen and
correlating it across dozens of intelligence sources and By providing relevant, high-fi delity intelligence, automating routine tasks,
internal tools. This dramatically reduces cognitive load, and enabling security teams to communicate their impact in business terms,
accelerates understanding, and empowers rapid, informed ThreatConnect empowers defenders to proactively address threats, optimize
decision-making right at the point of analysis. resources, and foster a more engaged and effective workforce.
Note that SANS Product Briefi ngs do not represent a SANS endorsement of a sponsor or its products, but rather an overview of its offerings and their capabilities.