# Nowhere to Hide: 2022 Falcon OverWatch Threat Hunting Report

## Table of Contents
[Executive Summary](#executive-summary)
[Interactive Intrusion Trends](#interactive-intrusion-trends)
  [Intrusion Campaign Numbers](#intrusion-campaign-numbers)
  [Intrusions by Threat Type](#intrusions-by-threat-type)
  [Intrusions by Industry Vertical](#intrusions-by-industry-vertical)
[Adversary Activity](#adversary-activity)
[Adversary Technique Insights](#adversary-technique-insights)
[Looking Back: Adversary Trends](#looking-back-adversary-trends)
[Looking Beyond the CVE](#looking-beyond-the-cve)
[LockBit and Its Technicolor Affiliate Program: How One RaaS Offering Has Spawned Diverse Tradecraft](#lockbit-and-its-technicolor-affiliate-program-how-one-raas-offering-has-spawned-diverse-tradecraft)
[Tooling Deep Dive: Emerging, Trending and Mainstay Tools](#tooling-deep-dive-emerging-trending-and-mainstay-tools)
[Better Together: OverWatch and Falcon Complete Team Up to Deliver Immediate Time-to-Value](#better-together-overwatch-and-falcon-complete-team-up-to-deliver-immediate-time-to-value)
[Looking Deeper: Interesting Tradecraft](#looking-deeper-interesting-tradecraft)
  [AQUATIC PANDA Demonstrates Deep Familiarity in Victim Network](#aquatic-panda-demonstrates-deep-familiarity-in-victim-network)
  [Healthcare Sector Finds Itself in the Crosshairs of eCrime Ransomware Affiliates](#healthcare-sector-finds-itself-in-the-crosshairs-of-ecrime-ransomware-affiliates)
  [Out with the Old, In with the ISO: How Adversaries Have Adapted to the Retirement of the Macro](#out-with-the-old-in-with-the-iso-how-adversaries-have-adapted-to-the-retirement-of-the-macro)
[Better Together: Be an Active Partner to Get the Most from Your OverWatch and Falcon Subscription](#better-together-be-an-active-partner-to-get-the-most-from-your-overwatch-and-falcon-subscription)
[Looking Ahead: OverWatch Showcases the Future of Threat Hunting](#looking-ahead-overwatch-showcases-the-future-of-threat-hunting)
  [OverWatch Takes to the Sky: Hunting for Adversaries in the Cloud](#overwatch-takes-to-the-sky-hunting-for-adversaries-in-the-cloud)
  [OverWatch’s Patented Technology Delivers Inimitable Threat Hunting Capability](#overwatchs-patented-technology-delivers-inimitable-threat-hunting-capability)
[Better Together: Three’s a CrowdStrike Powerhouse](#better-together-threes-a-crowdstrike-powerhouse)
[Conclusion](#conclusion)
[About Falcon OverWatch](#about-falcon-overwatch)
[CrowdStrike Products and Services](#crowdstrike-products-and-services)
[About CrowdStrike](#about-crowdstrike)

Nowhere to Hide: 2022 Falcon OverWatch Threat Hunting Report
CrowdStrike
2

## Executive Summary
**77,000**
Potential intrusions stopped with the help of Falcon OverWatch

**7 minutes**
The average interval at which OverWatch threat hunters uncovered potential intrusions

**1 million +**
Malicious events prevented by the Falcon platform derived from OverWatch

**50%**
Increase in interactive intrusion campaigns

The CrowdStrike Falcon OverWatch™ threat hunting team has been uncovering record volumes of hands-on intrusion attempts and tracking some marked changes in adversary tradecraft. This report shares insights from OverWatch’s around-the-clock threat hunting from July 1, 2021 through June 30, 2022.
<sup>1</sup> The findings and data in this report reflect observations derived from OverWatch’s global hunting activities.

In this 12-month period, OverWatch threat hunters directly identified more than 77,000 potential intrusions, or approximately one potential intrusion every seven minutes. This represents thousands of instances where human-driven hunting uncovered adversaries actively seeking to evade autonomous detection methods.

Crucially, OverWatch uses each of these potential intrusions as an opportunity to hone the Falcon platform’s ability to detect and prevent similar intrusions more quickly and autonomously. During the reporting period, threat hunters distilled their findings into the development of hundreds of new behavioral-based preventions, resulting in the Falcon platform’s direct prevention of over 1 million malicious events. These behavioral-based preventions enhance the Falcon platform’s power to uncover novel adversary behavior with greater speed and scale.

This year’s report starts with a close look at OverWatch’s extensive dataset covering observed interactive threat actor behaviors, which we will refer to in this report as “intrusion activity.” It uses this data to examine how and where adversaries are operating to provide a comprehensive overview of the threat landscape.

<sup>1</sup> Unless stated otherwise, the terms “this year,” “last year” or “past year” used throughout the report refer to the period from July 1, 2021 to June 30, 2022.

Nowhere to Hide: 2022 Falcon OverWatch Threat Hunting Report
CrowdStrike
4

Key findings from this data include:

+ OverWatch tracked a 50% increase in interactive intrusion activity year-over-year.
+ Breakout time for eCrime adversaries remained fast, averaging 1 hour and 24 minutes.
+ Technology, telecommunications, healthcare, manufacturing and academia were the top 5 industries most frequently targeted by interactive intrusion activity.
+ Malware-free activity accounted for 71% of all detections indexed by CrowdStrike Threat Graph®.<sup>2</sup>

Looking Back
A number of trends stood out to OverWatch as emblematic of the past year, in which the importance of proactive threat hunting shone through the proliferation of newly disclosed vulnerabilities and zero-days. In some instances, OverWatch detected zero-day exploits and notified customers of vulnerability-related intrusion activity before the vulnerability was disclosed; this was possible due to OverWatch’s relentless focus on hunting for post-exploitation tradecraft.

A vast array of affiliates are capitalizing on the availability of ransomware-as-a-service (RaaS) offerings. This has contributed to wide variations in eCrime affiliate tradecraft with threat hunters becoming skilled at identifying diverse patterns of adversary tradecraft that preceded the deployment of RaaS tooling.

This report’s retrospective concludes with a comprehensive look at the tools adversaries are leveraging. This includes an examination of emerging tools, trending tools and the tools that have remained persistently popular in adversary arsenals.

<sup>2</sup> For information on the CrowdStrike Threat Graph, see:
[https://www.crowdstrike.com/falcon-platform/threat-graph/](https://www.crowdstrike.com/falcon-platform/threat-graph/)

eCrime Breakout Time

Nowhere to Hide: 2022 Falcon OverWatch Threat Hunting Report
CrowdStrike
5

Looking Deeper
As important as it is to look at trends, it is equally important to consider outliers. The report looks at some of the most novel and sophisticated tradecraft observed this year — evidence of adversaries’ enduring capacity for innovation.

The technology sector remained a popular target for eCrime and targeted intrusion adversaries alike. A featured case study examines the array of techniques used by AQUATIC PANDA to achieve persistence, steal credentials and move around the victim network.

Healthcare is another sector heavily impacted by interactive cyber intrusions this past year. The report looks at two interesting examples of eCrime affiliate activity observed in the healthcare sector and recommends ways defenders can bolster their security against similar activity.

Finally, the report looks at the increase in the use of ISO files in phishing attacks by both targeted intrusion and eCrime adversaries.

Looking Ahead
The report closes with a look at where threat hunting is headed into 2022 and beyond. As the adoption of cloud-based technologies accelerates, so too does adversary interest in cloud-based resources. OverWatch is widening the aperture to capture this new direction in adversary targeting. The report looks at cloud-based intrusions that OverWatch and the CrowdStrike Services team handled this year and provides insights into how interactive threats are playing out in this arena.

In looking to the future, the report also details the patented technology that underpins OverWatch’s hunting capability and makes it possible to effectively scale human-driven insights.

A Note to the Reader
This report’s findings relate to interactive (i.e., hands-on) targeted<sup>3</sup> and eCrime intrusions that OverWatch tracks and do not necessarily represent the full spectrum of attacks that are stopped by OverWatch or the Falcon platform.

Moreover, the term “intrusion” is used to describe any malicious interactive activity that OverWatch uncovers in a victim environment. Intrusion is not synonymous with a “breach” and should not be understood to mean that the threat actor was able to achieve their objectives.

<sup>3</sup> The term “targeted intrusion” in this report refers to state-nexus or other advanced persistent threat actors.

Nowhere to Hide: 2022 Falcon OverWatch Threat Hunting Report
CrowdStrike
6

## Interactive Intrusion Trends

### Intrusion Campaign Numbers
Over the past year, OverWatch observed a near 50% increase in interactive intrusion campaigns. In the most recent quarter, from April to June 2022, OverWatch uncovered more intrusion campaigns than in any previous quarter.

**Intrusion Campaigns by Threat Type**
PANDAs (China)
SUSPECTED STATE-SPONSORED (Not Attributed)
KITTENs (Iran)
CHOLLIMAs (North Korea)
BEARs (Russia)
BUFFALOs (Vietnam)

July 2020 to June 2021 vs. July 2021 to June 2022
**+50%**

_Image Description: A bar chart showing the increase in intrusion campaigns from 2021 to 2022. The 2021 bar is shorter, and the 2022 bar is significantly taller, indicating a 50% increase._

Figure 1. Distribution of interactive intrusions by threat type

_Image Description: A pie chart showing the distribution of interactive intrusions by threat type. The chart is divided into four segments: eCrime (46%), Unattributed (39%), Targeted (14%), and Hacktivist (1%). The 2021 pie chart shows eCrime (43%), Unattributed (38%), Targeted (18%), and Hacktivist (1%)._

**eCrime**
Financially motivated criminal intrusion activity

**Targeted**
State-nexus intrusion activity that includes cyber espionage, destructive or disruptive attacks, and currency generation to support a regime

**Hacktivist**
Intrusion activity undertaken to gain momentum, visibility or publicity for a cause or ideology

**Unattributed**
Insufficient data available for high-confidence attribution

Nowhere to Hide: 2022 Falcon OverWatch Threat Hunting Report
CrowdStrike
7

### Intrusions by Threat Type
Of the intrusions where attribution was possible, financially motivated eCrime activity was again the dominant threat type. As shown in Figure 1, eCrime accounted for 43% of the interactive intrusion activity, while targeted intrusions increased to 18% and hacktivist activity made up 1%; the remaining 38% of intrusions were unattributed. It is important to note that the figures shown in Figure 1 differ from past reporting due to the inclusion of the unattributed intrusion data.

**Unattributed but Not Underestimated**
OverWatch decided to report publicly on unattributed intrusion activity in this year’s report because unattributable activity has been growing in prevalence year-over-year. For organizations to make informed and proactive decisions about security, it is crucial that defenders not only be aware of well-defined threats but also remain alert to the risk of emerging and unknown threats.

It is important to note that CrowdStrike does not rush to attribution. In many cases, OverWatch intercepts adversary activity during the very early stages of an attempted intrusion. In such cases, there are often few identifiable artifacts or examples indicative of tradecraft to investigate, which prevents high-confidence attribution. This issue is compounded by the continued blurring of the lines between eCrime and targeted intrusion tradecraft and tooling, which also curtails high-confidence attribution. Moreover, the motivations underlying intrusion activity are complex and diverse, and the paths that adversaries take to advance their mission can be indirect and inventive — one intrusion attempt in isolation may not reveal the full extent of an adversary’s motivations.

Organizations would be mistaken to believe that the threats they face are predictable. Considering the unknown is a cornerstone of OverWatch’s proactive hunting strategy. Rather than making assumptions about adversary motivations, OverWatch hunts for any and all evidence of post-exploitation activity across its global customer data set to provide proactive coverage against both known and unknown threats.

Nowhere to Hide: 2022 Falcon OverWatch Threat Hunting Report
CrowdStrike
8

### Intrusions by Industry Vertical
Notably, in this past year OverWatch uncovered interactive intrusion activity spanning 37 distinct industries — proof that no industry is immune, and evidence of the importance of remaining vigilant.

Figure 2 shows the relative frequency of intrusions for the top 10 industry verticals in which OverWatch uncovered interactive intrusion activity last year. This is compared with the relative frequency of intrusions in each industry vertical in the last reporting period. Figure 3 shows the top five industry verticals split out by threat type, illustrating where eCrime and targeted intrusion adversaries were most active.

_Image Description: A bar chart comparing the top 10 industry verticals impacted by interactive intrusions between July 2021 to June 2022 and July 2020 to June 2021. The chart shows the percentage of intrusions for each vertical, including Technology, Telecommunications, Manufacturing, Academic, Healthcare, Financial, Retail, Government, Pharmaceutical, and Media._

Figure 2. The figure shows which industry verticals globally were most frequently impacted by interactive intrusions in the past year and also shows any changes relative to the period from July 2020 to June 2021

Nowhere to Hide: 2022 Falcon OverWatch Threat Hunting Report
CrowdStrike
9

Technology was once again in the top spot, remaining a popular target for eCrime and targeted intrusion adversaries alike. The technology sector plays a critical role in supporting the operations of organizations across almost all other sectors; this reliance has increased in the wake of COVID-19 and the need to establish remote operations. Targeted intrusion adversaries may pursue technology companies to fulfill strategic, military, economic or scientific collection requirements, or as part of efforts to compromise supply chains or trusted relationships. Because of the potential value of data owned by technology companies and their vulnerability to disruption, they are also a sought-after target for ransomware campaigns by eCrime adversaries. The telecommunications industry remained in second place, driven in large part by targeted intrusion adversaries that conduct operations against telecommunications providers, likely to fulfill their surveillance, intelligence and counterintelligence collection priorities.

Notable changes in this year’s list include increased activity against the healthcare and academic industries. This year, intrusions in the healthcare industry were predominantly carried out by eCrime adversaries (eCrime affiliate activity against the healthcare industry is explored in detail later in this report). In contrast, last year, OverWatch reported a significant amount of targeted intrusion activity against the healthcare industry, particularly related to involvement in COVID-19 related research. Looking at the academic industry, OverWatch uncovered eCrime, hacktivist and targeted intrusion activity across the sector. The academic industry has a broad attack surface due to the nature of its users and operations, and is also a potentially high-value target for state-nexus adversaries because universities and academic institutions often possess intellectual property, and individuals of influence can be among their academic staff and alumni.

_Image Description: Two bar charts comparing the top 5 industry verticals impacted by targeted intrusion vs. eCrime adversaries between July 2021 to June 2022 and July 2020 to June 2021. The first chart shows the top 5 verticals for eCrime activity, and the second chart shows the top 5 verticals for targeted intrusion activity. The verticals include Technology, Manufacturing, Telecommunications, Government, Academic, Media, Healthcare, Retail, and Financial._

Figure 3. Comparison of the industry verticals most frequently impacted by targeted intrusion vs. eCrime adversaries, July 2021 to June 2022

_Image Description: A bar chart showing the percentage of intrusions by eCrime and Targeted Intrusions in the top 10 verticals._

**Top 5 Verticals by Intrusion Frequency**
**eCrime Activity vs. Targeted Intrusions: July 2021 to June 2022**

## Adversary Activity
In the past year, OverWatch uncovered interactive intrusion activity conducted by 36 distinct named threat actors, spanning seven groups: BEAR (Russia), CHOLLIMA (North Korea), JACKAL (hacktivist), KITTEN (Iran), PANDA (China), SPIDER (eCrime) and WOLF (Turkey).<sup>4</sup> These naming conventions are instituted by CrowdStrike to categorize adversaries according to their nation-state affiliations or motivations.

Figure 4 provides a breakdown of the threat groups observed by OverWatch.

**eCrime**
Of attributable intrusions, OverWatch tracked 12 named eCrime (aka SPIDER) threat actors; of these, PROPHET SPIDER was the most prolific, responsible for more than twice as many attributed interactive intrusions than the next most active eCrime actor, CARBON SPIDER. PROPHET SPIDER is likely an access broker — an actor that gains access with the intention to sell that access for profit rather than carrying out actions on objectives directly. Were it not for OverWatch alerting victim organizations to these PROPHET SPIDER intrusions, they likely would have progressed to a ransomware incident or breach.

ECrime adversaries remain highly capable, particularly if measured by the speed at which they can move through a victim’s environment. An important OverWatch speed measurement is breakout time: the time an adversary takes to move laterally, from an initially compromised host to another host within the victim environment. Of the hands-on eCrime intrusion activity last year where breakout time could be derived, the average was just 1 hour 24 minutes. Moreover, the OverWatch team found that in 30% of those eCrime intrusions, the adversary was able to move laterally to additional hosts in under 30 minutes.

<sup>4</sup> For more information about specific threat groups, visit the [CrowdStrike Adversary Universe](https://www.crowdstrike.com/adversary-intelligence/)

_Quote: Of the hands-on eCrime intrusion activity last year where breakout time could be derived, the average was just 1 hour 24 minutes. Moreover, the OverWatch team found that in 30% of those eCrime intrusions, the adversary was able to move laterally to additional hosts in under 30 minutes._

Nowhere to Hide: 2022 Falcon OverWatch Threat Hunting Report
CrowdStrike
11

**Targeted Intrusion**
By raw intrusion numbers, WICKED PANDA was the most prolific targeted intrusion threat actor tracked by OverWatch this year, followed closely by NEMESIS KITTEN; they were observed operating in seven and nine industry verticals, respectively.

**Hacktivism**
Hacktivist actor group FRONTLINE JACKAL was highly active this past year, seen operating across 11 industry verticals; by comparison, this threat actor was only found in four industry verticals in the previous reporting period. This increase in activity is linked to the adversary’s adoption of opportunistic initial access tactics.

Nowhere to Hide: 2022 Falcon OverWatch Threat Hunting Report
CrowdStrike
12

_Image Description: A heat map showing intrusion campaigns by adversary group and industry vertical, from July 2021 to June 2022. The heat map displays the activity of BEAR (Russia), CHOLLIMA (N. Korea), JACKAL (Hacktivist), KITTEN (Iran), PANDA (China), SPIDER (eCrime), and WOLF (Turkey) across various industry verticals._

Figure 4. Heat map of intrusion campaigns by adversary group and industry vertical, July 2021 to June 2022

A few things to note about the data presented in Figure 4:
+ The heat mapping represents the number of distinct actors active within a particular vertical.
+ The heat mapping does not represent the total number of intrusion attempts within a vertical, as multiple intrusions by the same adversary group are only represented once.
+ Attribution to a high degree of confidence is not always possible. This table does not reflect any unattributed activity that occurred in any of the industry verticals.
+ Verticals not listed indicate that OverWatch recorded no intrusions attributable to a specific actor group during this period.

Nowhere to Hide: 2022 Falcon OverWatch Threat Hunting Report
CrowdStrike
13

## Adversary Technique Insights
OverWatch carefully documents the details of each intrusion it uncovers, building a rich data set of adversary activity. With each new intrusion, threat hunters create a sharper picture of the threat landscape and tradecraft of adversaries that inhabit it — better equipping defenders to take a proactive and evidence-informed approach to protecting their environment. The following analysis draws on OverWatch’s rich repository of intrusion data collected over the past year.

**MITRE ATT&CK Heat Map**
OverWatch tracks interactive intrusion activity against the MITRE ATT&CK® Enterprise Matrix — a framework to categorize and track adversary behavior.<sup>5</sup>

The following heat map illustrates the prevalence of adversary tactics, techniques, sub-techniques and tools observed last year by OverWatch threat hunters. The heat map reflects the most current MITRE naming conventions for techniques and sub-techniques.

As stated previously, this heat map represents activity seen in interactive intrusions only and does not reflect the breadth of activity seen and stopped by the Falcon platform. This table excludes any techniques or sub-techniques not observed by OverWatch in this reporting period.

Notably, this year saw a shift in the persistence techniques favored by adversaries compared to the previous year, with increases seen in adversaries’ use of both server software components — particularly web shells — and IIS components.

Other than these slight shifts in persistence techniques, much of this year’s heat map reflects the previous year’s. Exploiting public facing infrastructure, abusing remote services (particularly RDP), dumping OS credentials and accessing unsecure credentials all remain popular and heavily represented in this year’s heat map.

<sup>5</sup> To learn more about MITRE ATT&CK, visit [https://attack.mitre.org/matrices/enterprise/](https://attack.mitre.org/matrices/enterprise/).

Nowhere to Hide: 2022 Falcon OverWatch Threat Hunting Report
CrowdStrike
14

_Image Description: A series of heat maps showing the prevalence of adversary tactics, techniques, and sub-techniques observed by OverWatch threat hunters, categorized by MITRE ATT&CK framework. The heat maps are divided into three sections, each containing multiple tables. The first section covers Initial Access, Execution, Persistence, and Privilege Escalation. The second section covers Defense Evasion, Credential Access, Discovery, and Lateral Movement. The third section covers Collection, Command and Control, Exfiltration, and Impact._

**MITRE ATT&CK Heat Map (1 of 3)**
| **Initial Access** |  | **Execution** |  | **Persistence** |  | **Privilege Escalation** |  |
|---|---|---|---|---|---|---|---|
| **Technique** | **Sub-technique** | **Technique** | **Sub-technique** | **Technique** | **Sub-technique** | **Technique** | **Sub-technique** |
| Valid Accounts | Domain Accounts | Command and Scripting Interpreter | Windows Command Shell | Valid Accounts | Domain Accounts | Valid Accounts | Domain Accounts |
|  | Local Accounts |  | PowerShell |  | Local Accounts |  | Local Accounts |
|  | Default Accounts |  | Unix Shell |  | Default Accounts |  | Default Accounts |
| Exploit Public-Facing Application |  |  | Python | Server Software Component | Web Shell | Process Injection | Process Hollowing |
| External Remote Services |  |  | Visual Basic |  | IIS Components |  | Dynamic-link Library Injection |
| Phishing | Spearphishing Attachment |  | JavaScript | Create Account | Local Account | Scheduled Task/Job | Scheduled Task |
|  | Spearphishing Link |  | Windows Management Instrumentation |  | Domain Account |  | Cron |
|  | Drive-by Compromise |  |  | System Services | Service Execution |  | Systemd Service |
|  |  |  |  |  | Windows Service | Account Manipulation | Additional Email Delegate Permissions |
|  |  |  |  |  | Systemd Service | Create or Modify System Process | Windows Service |
|  |  |  |  |  |  |  | Scheduled Task |
|  |  |  |  |  |  |  | Cron |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  