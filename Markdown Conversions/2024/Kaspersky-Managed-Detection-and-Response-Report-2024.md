2024

Analyst report

Managed Detection
and Response

## Table of Contents
- [Executive Summary](#executive-summary)
- [Recommendations](#recommendations)
- [Introduction](#introduction)
- [About Kaspersky MDR](#about-kaspersky-mdr)
- [Kaspersky MDR Scope](#kaspersky-mdr-scope)
- [Industry Distribution](#industry-distribution)
- [Number of Incidents](#number-of-incidents)
- [Incident Detection Time](#incident-detection-time)
- [Incident Severity](#incident-severity)
- [Response Efficiency](#response-efficiency)
- [The Nature of High-Severity Incidents](#the-nature-of-high-severity-incidents)
- [Detection Technologies. Adversary Tactics, Techniques and Procedures](#detection-technologies-adversary-tactics-techniques-and-procedures)
- [Adversary Tactics and Detection Technologies](#adversary-tactics-and-detection-technologies)
- [Adversary Techniques](#adversary-techniques)
- [MITRE ATT&CK® Incidents Classification](#mitre-attck-incidents-classification)
- [About Kaspersky](#about-kaspersky)

# Executive Summary

More than two
high-severity
incidents every day

77% of incidents were
successfully remediated
after the first relevant
security alert was received

Key regions by
number of customers:

Key European
countries:

Industries with the highest number of reported
incidents:

Europe — 40%

CIS*  — 21%

META — 15%

Italy — 31%

Spain — 15%

Switzerland — 13%

Industrial —
26%

Financial —
14%

Government —
12%

The most common attacker profile in high-severity
incidents:

APT —
43%

Security
Assessment —
17%

Crime1 —
12%

The most popular living-off-the-land attack tools:

powershell.exe

rundll32.exe

comsvcs.dll

The distribution of reported incidents by severity:

High — 5%

Medium — 69%

Low — 26%

The most popular MITRE ATT&CK techniques:

T1566: Phishing
TA0001: Initial Access

observed in 24%
of incidents

T1204: User
Execution
TA0002: Execution

observed in 19%
of incidents

T1098: Account Manipulation
TA0003: Persistence

observed in 18% of incidents

* CIS — Commonwealth of Independent States (Armenia, Azerbaijan, Belarus, Kazakhstan,

Kyrgyzstan, Moldova, Russia, Tajikistan, Uzbekistan)

1 An attack carried out using malware without observable human involvement

Mean time to report high-severity incidents — 54 min,
medium — 41 min, low — 38 min.

# Recommendations

	' In 2024 the number of high-severity incidents decreased by 34% compared to 2023. However,

mean time to investigate and report increased by 48%, indicating a rise in the average complexity
of attacks. This is supported by the analysis of triggered detection rules and IoAs — the vast
majority of which were from specialized XDR tools. This marks a shift from previous years, where
detection by OS logs played a significant role. In these conditions, specialized tools, like XDR3, are
essential for successful detection and investigation of modern threats.

	' Human-driven targeted attacks accounted for 43% of high-severity incidents in 2024 — 74%
more than in 2023 and 43% higher than in 2022. Despite advances in automated detection
tools, motivated attacker can still find ways to bypass them. To counter human-driven attacks,
human-driven solutions, like Managed Detection and Response4 are critical. For organizations with
in-house security operations team, internal processes and technologies must be equipped to handle
the modern threat landscape. Comprehensive SOC consulting services5 can help achieve this.

	' The statistics consistently show that attackers
often return after a successful attack. This
is especially evident in government organizations,
where attackers aim for long-term presence
to conduct espionage. In such cases, combining
XDR-equipped in-house SOCs or outsourced
MDR with regular Compromise Assessments6
is an effective way to detect and investigate
incidents missed by existing security measures.
Attackers often use Living off the Land (LotL)
methods7 in infrastructures lacking proper system
configuration controls. A relatively large number
of incidents are linked to unauthorized changes,
such as adding accounts to privileged groups
or weakening secure configurations. To reduce
false positives in these scenarios, effective
configuration management and formal procedures
for implementing changes and managing access
are crucial.

	' In 2024, User Execution8 and Phishing9 techniques
were again in the top 3 threats, with nearly 5%
of high-severity incidents involving successful
social engineering. Users are still the weakest link,
making Security Awareness10 an important focus
for corporate information security planning.

3 Kaspersky Next XDR

Expert

4

Kaspersky Managed
Detection and
Response

5

Kaspersky SOC
Consulting

6

Kaspersky
Compromise
Assessment

7 Kaspersky

Encyclopedia. Living
off the Land attack

8

MITRE ATT&CK.
T1204 User
Execution

9

MITRE ATT&CK.
T1566 Phishing

10

Kaspersky Security
Awareness

# Introduction

The annual Managed Detection and Response (MDR) analyst report presents insights based on the analysis
of MDR incidents identified by Kaspersky's SOC team.

The report sheds light on the most prevalent attacker tactics, techniques, and tools, as well as the
characteristics of detected incidents and their distribution across regions and industry sectors among MDR
customers.

This report answers key questions, including:

What methods are
they using today?

Who are the
potential attackers?

How can their activities
be effectively detected?

# About Kaspersky MDR

MDR provides round-the-clock monitoring and threat detection. Endpoint protection platforms (EPPs) transmit
telemetry for analysis by machine learning and SOC team. For threat detection Indicators of Attack (IoA)
and manual threat hunting are used. Response actions are assigned by SOC team and, if user approves, EPP
executes it.

# Kaspersky MDR Scope

Kaspersky MDR customers are represented across the world, enabling us to get a comprehensive, objective view
of regional attack behaviors and tactics. The chart below shows the geographic distribution of MDR customers.
The largest representation is in Europe, the CIS, and the META region.

APAC — 13%

CIS — 21%

Europe — 40%

Latin America — 8%

META — 15%

North America — 3%

In Europe, the largest MDR coverage is in Italy, Spain
and Switzerland.

South Africa leads the META region.

2%2%

2%

4%

6%

7%

9%

9%

31%

Italy

Spain

Switzerland

Austria

Serbia

Netherlands

Bosnia and
Herzegovina

United
Kingdom

Germany

Other

36%

15%

France

13%

6%

8%

8%

21%

11%

10%

South Africa

Côte
d'Ivoire

Saudi Arabia

Egypt

Kuwait

Angola

Other

# Industry Distribution

In 2024, the MDR team observed the most incidents in the industrial enterprises (25.7%), financial (14.1%) and
government (11.7%) sectors.

Figure 1
Most attacked industries

Development

Education

Financial

Food

Government

Healthcare

IT

Industrial

Mass Media

Retail

Telecom

Transportation

Other

Number of customers, %

Number of reported incidents, %

Number of reported high-severity incidents, %

The graph reflects the presence of MDR in the relevant industry, by number of customers.
Comparing it to distribution by number of incidents enables us to roughly estimate the
frequency of incidents in that industry.

If we consider only high-severity incidents, the distribution is somewhat different:
22.8% in IT, 18.3% in government, 17.8% in industrial, and 11.9% in the financial sector.

# Number of Incidents

In 2024, the MDR infrastructure received and processed telemetry events every day, generating security alerts
as a result. Approximately 26% of these alerts were processed by machine-learning algorithms, while 13% were
analyzed by the SOC team and determined to be actual incidents. MDR customers were informed about these
incidents via the MDR portal.

Figure 2
Kaspersky MDR alerts processing funnel

~  270,000

security alerts received

~ 15,000

telemetry events from a host

This number can vary significantly depending
on host activity and sensor type

~ 200,000

alerts were analyzed by SOC analysts

> 70,000

alerts were processed automatically
using AI technologies

~87%

of the alerts were identified as false
positives by SOC analysts

~ 13,000

incidents which were reported
to customers

> 26,000

alerts were analyzed

The lower number of alerts is due to extensive work to improve the detection logic
efficiency, which resulted in an increase in the overall IoA conversion from 10% up to 13%
and a reduction in the number of false positives processed by the SOC analytics.

# Incident Detection Time

The incident detection process consists of several steps. First, a specialized robot assigns a generated alert
to the personal queue of an available SOC analyst. Next, the analyst processes the alert based on its severity
and the guaranteed service level agreement (SLA) time to detect a threat. If the analysis results in a false
positive, the alert is ignored, and filters are created at customer or global level. Otherwise, the alert is imported
into a new or existing incident which, after in-depth investigation, can be closed as a false positive again
or reported to the customer through the MDR portal with a recommended response. If the customer approves
the recommended response, the endpoint agents automatically implement them.

Table 1
Time to detect an incident

Severity

Time to report,
in minutes

Comments

       High

       Medium

       Low

53.99 min

2023: 36.37 min
2022: 43.75 min
2021: 41.45 min

41.03 min

2023: 32.55 min
2022: 30.92 min
2021: 34.88 min

37.85 min

2023: 48.01 min
2022: 34.15 min
2021: 40.24 min

The most complex incidents require more
time to collect additional information and build
an incident timeline.
In 2024, this time increased by approximately 48%
compared to previous periods2, reflecting the
nature of high-severity incidents during the year.

Medium-severity incidents were the most
frequent severity level. Most of these incidents
were caused by malware activity, and fully
automated remediation proved effective.
However, the time required increased by 26%
compared to 2024, due to a slight increase in the
number of medium-severity incidents in 2024.

Incidents with the lowest severity were mostly
related to the consequences of potentially
unwanted software. in most cases, processing
these incidents was largely automated.

2 Kaspersky MDR analyst report for 2023

Kaspersky MDR analyst report for 2022

Kaspersky MDR analyst report for 2021

# Incident Severity

In MDR, only incidents that require any action from the customer side are reported.

         Low

         Medium

         High

No significant impact
on customer IT systems, however,
there are a number of measures
that need to be taken

No evidence of direct human
involvement in the attack, may
impact customer IT systems, but
without severe consequences

Human-driven attack or malware
threats with a potential or actual
significant impact on the
customer’s IT systems

In 2024, there were, on average, more than three critical incidents every two days. While 2021 saw the highest
number of high-severity incidents, the trend since then shows a decline in their proportion, accompanied
by an increase in low- and medium-severity incidents.

Figure 3
Incident severity level

Figure 4
Severity of incidents detected
by MDR over the years

4.69%

4.69%

69.39%

25.92%

High

Medium

Low

69.39%

25.92%

2024

2023

2022

2021

2020

7.09%

62.73%

30.18%

8.13%

71.82%

20.06%

14.34%

65.41%

20.25%

9.16%

71.78%

19.06%

The shift from high-severity to medium-severity incidents can be attributed to early detection and instrumental
remediation. At the time of detection, there was often insufficient evidence of direct human involvement
in the attack. In these cases, activities such as malicious email campaigns, drive-by-download compromises,
connections to potentially malicious Internet resources, network reconnaissance, brute force attempts,
or vulnerability exploitation were detected. However, the Kaspersky MDR team determined that the nature
of these activities and their associated risks did not warrant classification as high-severity.

The number of incidents largely depends on the scope of monitoring. The diagram below
shows the expected number of incidents for each severity level across 10,000 monitored
endpoints, categorized by industry.

Distribution of expected number of incidents from 10,000 endpoints
by severity and industry

Figure 5

High

Medium

Low

The diagram shows that the highest relative number of incidents occurred in the mass media, development, and
telecoms industries.

Figure 6
Distribution of expected number of incidents from 10,000 endpoints
by severity and industry compared to the previous year

High

Medium

Low

Compared to 2023, the mass
media, development, and telecoms
industries saw a significant increase
in the number of incidents.

In 2024, high-severity incidents accounted for less than 5% of the total, making them visually
insignificant in the overall incident volume. The following diagram focuses exclusively on high-
severity incidents.

Figure 7
The expected number of critical incidents from 10,000 endpoints
by industry compared to the previous year

High

The chart highlights a significant decrease in high-severity incidents in the government and development
sectors, while the number of incidents in the industrial sector remained stable or increased. A relatively large
increase was observed in the food industry, with a slight increase in IT and telecoms.
Although the mass media experienced a huge increase in incidents, this trend was
not reflected in high-severity incidents. This supports the earlier observations that
many attack attempts were promptly detected and mitigated, preventing their
severity from exceeding medium levels.

# Response Efficiency

Figure 8
Distribution of incidents
by number of relevant alerts

Figure 9
Distribution of incidents
by severity and number
of relevant alerts

76%

22%

2%

Incidents
with 1 alert

Incidents
with 2–10 alerts

Incidents
> 10 alerts

2.76%

68.69%

28.55%

9.11%

72.89%

18.01%

32.38%

59.43%

8.20%

Incidents with
1 alert

Incidents with
2–10 alerts

Incidents with
>10 alerts

High

Medium

Low

Approximately 76% of incidents were detected based on a single alert. An attack was deemed successfully
stopped if no further relevant alerts were generated. This category also includes typical incidents with clear
response scenarios. Critical incidents accounted for less than 3%, while the vast majority were incidents
of medium (69%) and low (29%) severity.

Approximately 22% of incidents were identified based on 2-10 alerts. To make it difficult to bypass detection,
we use a set of technologies to create different alerts for the same threat. For example, the use of a tool can
be detected simultaneously by the EPP based on the threat binary and by its behavior. On the MDR side, the
detection may be based on particular command lines and on detection of access to certain registry hives. This
category reflects incidents that were not automatically resolved after the first alert: either a person was involved
in the response, or the first relevant alert was incorrectly classified.

Approximately 2% of incidents involves more than 10 alerts. These cases typically arise when the response was
either rejected by the customer or was ineffective. Examples include a new targeted attack requiring thorough
investigation before responding, or scenarios where the customer requested monitoring of an attack without
active countermeasures (cyber exercises scenario). The share of high-severity incidents here is the largest,
exceeding 32%. About 8% of low-severity incidents in this category are explained by the presence of low-priority
response actions on the part of MDR users, which were not implemented either due to internal reasons
or the incident’s non-critical nature. While these inactions do not lead to further attack development, the MDR
infrastructure continues receiving related alerts linked to reported incidents.

# The Nature of High-Severity Incidents

Main causes of high-severity incidents

Figure 10
The number of critical
incidents by type

Figure 11
The number of companies
where critical incidents were
observed, by type

0.87%

0.17%

1.22%

4.90%

8.39%

2.66%

1.9% 0.38%

7.98%

11.89%

12.06%

43.01%

9.89%

18.63%

25.48%

17.49%

17.48%

15.59%

Targeted
attacks

Cyber
exercises

Malicious
software

Severe internal
security policy
violation

Artifacts
of targeted
attacks

Social
engineering

Critical
vulnerability

Insider

Denial
of Service
attack

In 2024, Kaspersky detected human-driven attacks (APTs) in one in four customers. These attacks accounted for
over 43% of all high-severity incidents. Human-driven attacks confirmed by customers as cyber exercises made
up more than 17% of incidents and were observed in more than 17% of customers. Approximately 12% of incidents
involved severe security policy violations, which were reported in more than 18% of customers. Incidents related
to malware ranked third in 2024, with just over 12% of these high-severity incidents reported in less than 16%
of customers.

More than 8% of incidents were related to the detection of artifacts from past human-driven attacks that were
no longer active at the time of detection, affecting less than 10% of customers. While vulnerability detection
is not a core focus for MDR, technical capabilities are available. More than 1% of such high-severity incidents were
identified in less than 3% of customers. Suspicious actions by legitimate users are classified
by default as security policy violation. If confirmed by the customers as intentionally
malicious, these incidents are reclassified as insider activity. This very rare scenario
accounted for less than 1% of high-severity incidents in less than 2% infrastructures.

Number of high-severity incidents by industry

The graph below shows the distribution of high-severity incidents by type and industry.

Figure 12
Number of high-severity incidents by type and industry

Targeted
attacks

Cyber
exercises

Malicious
software

Severe internal
security policy
violation

Artifacts
of targeted
attacks

Social
engineering

Critical
vulnerability

Insider

Denial
of Service
attack

The following conclusions can be drawn from the statistics:

	' Human-driven targeted attacks were observed in all
sectors except telecoms. The IT and government
sectors lead with 14.7% and 13.8% respectively.

	' All types of incidents were observed in the industrial
sector, which ranked third in 2024 for the total
number of high-severity incidents. This included 0.17%
of detected DoS attacks.

	' The financial sector ranked fourth place in total

high-severity incidents and was affected by all MDR
incident types.

	' Security assessments remain a popular practice,

and incidents of this type were observed across all
economic sectors except education and healthcare.

	' Malware-related high-severity incidents were

observed mainly in the financial (2.6%), industrial (2.3%)
and IT (1.6%) sectors.

	' Incidents involving artifacts from previous APT attacks
mirrored the distribution of active human-driven attacks.
In development and education, active human-driven
attacks were detected, but no incidents with artifacts
of past attacks were reported.

	' Severe violations of internal security policies were

observed in all industries except education and mass
media. The IT (2.8%), industrial (2.3%) and financial (1.6%)
sectors were most affected. Confirmed malicious insider
actions were observed in financial, food, government and
industrial sectors.

	' Successful social engineering attacks that led

to further development ranked sixth in the total number
of high-severity incidents. The industrial (1.2%) and
government (1.1%) sectors were most affected.

	' Incidents related to critical
vulnerabilities in 2024 were
reported in the industrial,
transportation, food and
healthcare sectors.

Number of organizations that experienced
high-severity incidents

The graph below shows what percentage of the total number of MDR customers, with detected high-severity
incidents of particular type, distributed by industry. This chart is useful for analyzing the overall picture from all
customers.

Figure 13
Number of MDR customers that experienced high-severity incidents
by industry

Targeted
attacks

Cyber
exercises

Malicious
software

Severe internal
security policy
violation

Artifacts
of targeted
attacks

Social
engineering

Critical
vulnerability

Insider

Denial
of Service
attack

In addition to earlier observations, the following conclusions can be drawn from the diagram:

	' High-severity incidents were observed across all industries.
	' The highest percentage of companies targeted by human-driven attacks belonged to the industrial (9.3%) and government

(10.7%) sectors.

	' Severe security policy violations ranked second in terms of the number of affected organizations. Such incidents were

observed in nearly all organizations monitored by Kaspersky, with IT (7.9%), industrial (7.1%) and financial (5.7%) sectors leading.

	' Malware attacks were most commonly observed in enterprises within the industrial (6.4%)

and financial (5.7%) sectors.

	' The financial (8.6%) and industrial (7.1%) sectors experienced the highest number of incidents

related to cyber exercises.

To compare the number of attacked organizations across sectors and within a sector,
consider the following graph. The percentages represent the ratio of organizations with the
corresponding type of incident to the total number of organizations in a given industry.

Figure 14
Number of attacked organizations across sectors and within a sector

Targeted
attacks

Cyber
exercises

Malicious
software

Severe internal
security policy
violation

Artifacts
of targeted
attacks

Social
engineering

Critical
vulnerability

Insider

Denial
of Service
attack

Key points from this visualization:

	' In the education sector, the only type of high-severity incidents observed were human-driven attacks. Furthermore, APT

incidents were reported in 83% of government organizations, 75% of organizations in the transportation and food sectors, and
half of organizations in the development, healthcare, and retail sectors.

	' Security policy violations were reported in all organizations within the telecoms sector and 79% of IT organizations.
	' DoS attacks were reported in half of organizations within the industrial sector.
	' Cybersecurity exercises were notably prevalent in the mass media sector (two-thirds of organizations), financial sector (55%),

development sector (50%).

	' Traces of previous human-driven attacks were detected in 32% of financial organizations, 33% of mass

media organizations, and 25% of organizations in the food and transportation sectors.

	' Successful social engineering attacks affected 50% of development organizations, 33% of mass

media organizations and 25% of transportation organizations.

# Detection Technologies. Adversary Tactics, Techniques and Procedures

MDR enables the detection of incidents at different attack stages. While most incidents progress through all
stages of an attack (at outlined by MITRE ATT&CK® tactics), the diagram below highlights the earliest tactics
associated with the alerts for each incident.

Figure 15
Adversary tactics

High

Medium

Low

TA0043:
Reconnaissance

TA0042:
Resource Development

TA0001:
Initial Access

TA0002: Execution

TA0003: Persistence

TA0004: Privilege
Escalation

TA0005: Defense
Evasion

TA0006:
Credential Access

TA0007:
Discovery

TA0008:
Lateral Movement

TA0009:
Collection

TA0011: Command and
Control

TA0010:
Exfiltration

TA0040: Impact

0.10%

2.29%

0.24%

0.83%

7.73%

2.03%

0.51%

30.25%

2.49%

1.42%

9.06%

3.75%

0.56%

3.73%

7.73%

0.37%

4.34%

0.70%

0.08%

1.34%

0.75%

0.27%

4.26%

1.25%

0.07% 0.31% 0.14%

0.07%

7.53%

0.36%

0.02

0.02%

0.02%

0.05%

3.80%

0.98%

0.03%

0.03%

0.42%

0.07%

Adversary tactics that Kaspersky uses to detect incidents:

TA0043:
Reconnaissance

Incidents detected at this stage are mainly related to various types of scans. The
severity of these incidents depends on the goals of the scan. Incidents classified
as high-severity are typically related to successful spear phishing that lead to further
attack development. Incidents related to known APT campaigns are also observed
at this stage.

TA0042:
Resource
Development

TA0001:
Initial Access

Incidents attributed to this tactic are primarily associated with the detection
of malicious or unwanted software, even when there are no signs of its execution.
The severity of these incidents is determined by the classification of the detected tools.

The vast majority of incidents detected at this stage involve phishing emails containing
various types of malicious objects classified as medium-severity. High-severity
incidents include successful social engineering attacks, remote service compromises
leading to further attack development, and activities attributed to known targeted
attacks. Low-severity incidents are usually phishing attempts that were clicked by users
and therefore reported, but did not lead to any impact due to successful automatic
remediation.

TA0002:
Execution

Because launching specialized attack tools tends to be noisy, the largest number
of high-severity incidents were detected at this stage. In general, the severity
of the incident is determined by the classification of the executed malicious tool.

TA0003: Persistence

Incidents at this stage include the substitution of accessibility features, suspicious
or unsafe network resources configurations, and bootkits. High-severity is assigned
when there is clear evidence of an active human attacker involvement. Medium- and
low-severity incidents are registered based on potential impact. Most low-severity
incidents detected here involve account manipulation, such as enablement of local
admin or guest accounts.

TA0004:
Privilege
Escalation

TA0005:
Defense
Evasion

The vast majority of incidents where this was the earliest tactic — adding an account
to various privileged groups, such as Domain Admins, Enterprise Admins, etc. This
includes incidents related to the use of specialized tools for privilege escalation,
detected either as separate files and already loaded into system memory by EPP. It also
covers detection of vulnerable drivers, changes to UAC configurations or attempts
to bypass UAC.

A relatively small percentage of incidents are detected at this stage, but the variety
of activities detected is extensive. Examples include: suspicious SPN settings on a host,
scheduled tasks masqueraded as legitimate Windows components, log deletion,
alteration of digital signature checks, use of different LOLBins11, and attempts
to modify endpoint configurations. The proportion of false positives here is the lowest,
as the detected techniques and tools are rarely associated with legitimate activity.

11

Living Off The Land Binaries, Scripts and Libraries

TA0006:
Credential Access

The vast majority of incidents related to this tactic are attempts
to access LSASS process memory, dumps of sensitive registry
hives, detects on different types of keyloggers, brute force
or password spraying attempts. As in the previous case,
incidents identified here are rarely false positives, with the
exception of some types of confirmed cyber exercises.

TA0007:
Discovery

Detection at this stage is associated with a high number of false positives, so there are
few relevant IoAs that convert into alerts. The existing incidents are primarily related
to various types of internal networks scans, Active Directory configuration discovery
or detection of the use of specialized tools – Bloodhound12, for example.

TA0008:
Lateral Movement

As Lateral Movement has a low false positive rate, it is promising tactic for planning the
development of new IoAs. The vast majority of incidents in 2024 were related to network
remote exploitation attempts. Different anomaly-based detections of suspicious
network logins using legitimate credentials also fall into this category.

TA0009:
Collection

TA0010:
Exfiltration

Observed activity at this stage is based on detection of special tools. Some incidents
were also identified by an anomaly detection engine powered by machine learning.

In 2024, only a few incidents reached this stage. The detected incidents are extremely
difficult to distinguish from TA0011, as the most common scenario is T1041: Exfiltration
over C2 channel13 using standard application layer protocols. Incidents were attributed
to this tactic when the evidence is clear — such as specific command-line activity
indicating that an action involved exfiltration, for example.

TA0011:
Command and
Control

The vast majority of detections at this stage were made based on Threat Intelligence:
access to a malicious resource. The severity of the incident is determined by the known
purpose of C2: if it’s associated with an APT, the incident is classified as high-severity.
Detects of known C&C frameworks, like Cobalt Strike14, Sliver15, MSF16 , etc., also fall into
this category.

TA0040:
Impact

In this tactic, most incidents are identified through the detection of specific
malware when earlier detection and response weren’t possible. In 2024, the vast
majority of incidents that reached this stage were related to either the detection
of crypto-miners or ransomware.

12

MITRE ATT&CK. S0521 BloodHound

15

MITRE ATT&CK. S0521 BloodHound

13

MITRE ATT&CK. T1041 Exfiltration Over C2 Channel

16

MITRE ATT&CK. T1041 Exfiltration Over C2 Channel

14 MITRE ATT&CK. S0154 Cobalt Strike

# Adversary Tactics and Detection Technologies

Kaspersky MDR uses different sensors: Endpoint Protection Platform (EPP), Network Intrusion Detection
System (NIDS), Sandbox (SB). The last two sensors are part of Kaspersky Anti Targeted Attack (KATA).

For the purposes of this report, IDS verdicts that are part of the EPP are counted as endpoint alerts.

In many cases, incidents were detected using multiple types of sensors. However, for the purposes of the
diagram below, we count only the alert that was detected first and used by the SOC analyst to form the incident.
As a result, the predominance of incidents detected by the EPP does not necessarily mean that they couldn’t
also have been detected by the IDS or Sandbox as part