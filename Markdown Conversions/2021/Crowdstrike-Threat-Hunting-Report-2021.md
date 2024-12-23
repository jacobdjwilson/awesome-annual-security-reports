# 2021 Threat Hunting Report
Insights From the Falcon OverWatch Team
Nowhere
to Hide

## Table of Contents
- [About Falcon OverWatch](#about-falcon-overwatch)
- [Executive Summary](#executive-summary)
- [The Value of Continuous Threat Hunting](#the-value-of-continuous-threat-hunting)
- [OverWatch SEARCH Hunting Methodology](#overwatch-search-hunting-methodology)
- [Intrusion Campaigns Summary](#intrusion-campaigns-summary)
- [Adversary Technique and Tooling Insights](#adversary-technique-and-tooling-insights)
- [In Pursuit of PROPHET](#in-pursuit-of-prophet)
- [SPIDER Casts a Vishing Net for Retail Target](#spider-casts-a-vishing-net-for-retail-target)
- [Signal Interference: Threat Hunting Short-circuits Adversary Telecommunications Targeting](#signal-interference-threat-hunting-short-circuits-adversary-telecommunications-targeting)
- [OverWatch Uncovers Double Trouble in the Wires](#overwatch-uncovers-double-trouble-in-the-wires)
- [Custom Tooling Rings Alarm Bells in Intrusion by (Not So) SILENT CHOLLIMA](#custom-tooling-rings-alarm-bells-in-intrusion-by-not-so-silent-chollima)
- [Stopping Breaches Is a Race Against the Clock](#stopping-breaches-is-a-race-against-the-clock)
- [Conclusion](#conclusion)
- [About CrowdStrike](#about-crowdstrike)
- [CrowdStrike Products and Services](#crowdstrike-products-and-services)

2021 Threat Hunting Report
2

F
alcon OverWatchTM is the CrowdStrike® managed threat hunting service 
built on the CrowdStrike Falcon® platform. OverWatch conducts thorough 
human analysis on a 24/7/365 basis to relentlessly hunt for anomalous or 
novel attacker tradecraft designed to evade other detection techniques.	
	
	
	
OverWatch is an elite cross-disciplinary team that harnesses the power of the 
CrowdStrike Threat Graph® database, enriched with CrowdStrike threat intelligence, 
to continuously hunt for threat activity in customer environments. Armed with 
cloud-scale telemetry of upward of 1 trillion endpoint-related events collected per 
day, and detailed tradecraft on more than 160 adversary groups, OverWatch has 
the unparalleled ability to see and stop the most sophisticated threats — leaving 
adversaries with nowhere to hide.
[^1]
[^1]: For more information on how Falcon OverWatch performs its mission, please see 
	
https://www.crowdstrike.com/endpoint-security-products/falcon-overwatch-threat-hunting/.

<a name="about-falcon-overwatch"></a>
## About Falcon OverWatch
2021 Threat Hunting Report
3

F
or yet another year, OverWatch disrupted a record number of interactive 
intrusion attempts[^2] by identifying malicious activity early and stopping 
adversaries in their tracks. This report shares insights from OverWatch’s 
around-the-clock threat hunting from July 1, 2020 through June 30, 2021.[^3]
This year's report starts with a close look at OverWatch's extensive dataset covering 
observed interactive threat actor behaviors, which we will refer to in this report as 
"intrusion activity". It uses this data to examine how threat actors are operating in 
victim environments, highlighting both rare and common techniques that adversaries 
are employing.
The mission of OverWatch is to augment the powerful autonomous protection of the 
Falcon platform with human expertise. With the combined power of human ingenuity 
and patent-protected work flows, OverWatch systematically sifts through 1 trillion 
daily events to find potential hands-on intrusions, on average 1 every 8 minutes. 
OverWatch operates with speed and at scale to notify victim organizations of 
malicious activity in near real time, ensuring intrusion attempts that incorporate novel 
tradecraft are identified and disrupted before the breach.
Key findings from this year’s report include:
	

OverWatch has tracked a 60% increase in interactive intrusion activity in 
the past year. The threat of hands-on intrusion activity remains very real — 
OverWatch has observed and disrupted intrusions spanning all industry verticals 
and geographic regions.
	

Adversaries have moved beyond malware. They are using increasingly 
sophisticated and stealthy techniques tailor-made to evade autonomous 
detections — of all of the detections indexed by CrowdStrike Threat Graph® in 
the past three months, 68% were malware-free.
	

ECrime continues to dominate the threat landscape, making up 75% of 
interactive intrusion activity. One driver of this has been the continually evolving 
big game hunting (BGH) business model, which has seen the widespread 
adoption of both the use of access brokers to facilitate access, and the use of 
dedicated leak sites to extract payment.
	

ECrime adversaries are moving with increasing speed in pursuit of their 
objectives. OverWatch observations show they are capable of moving laterally 
within a victim environment in an average of 1 hour and 32 minutes.
	

Targeted intrusion adversaries remain a prominent threat, particularly for the 
telecommunications industry. While organizations of all sizes and in all verticals 
have the potential to become a target, the telecommunications industry stood 
out this year, accounting for 40% of all state-nexus intrusion activity observed by 
OverWatch in the past 12 months.
[^2]: The term “interactive” denotes hands-on adversary activity.
[^3]: The terms “this year” or “this past year” used throughout the report refer to the period from July 1, 2020 
to June 30, 2021.

<a name="executive-summary"></a>
## Executive Summary
This report shares 
insights into the 
latest adversary 
tradecraft, gleaned 
from OverWatch’s 
extensive intrusion 
dataset.
2021 Threat Hunting Report
4
This report features detailed case studies sharing insights into the hands-on activity 
that OverWatch tracks on a daily basis and concludes with recommendations for 
defenders looking to bolster their security program.
Note that this report’s findings relate to interactive (i.e., hands-on) targeted 
intrusions[^4] and eCrime intrusions that OverWatch tracks and are not necessarily 
representative of the full spectrum of attacks that are stopped by OverWatch or the 
Falcon platform.
Moreover, the term “intrusion” is used to describe any malicious interactive activity 
that OverWatch uncovers in a victim environment. The term “intrusion” is not 
synonymous with a “security breach” and should not be understood to mean that 
the threat actor was able to achieve their objectives.
[^4]: The term “targeted intrusion” in this report refers to state-nexus or other advanced persistent threat actors.
2021 Threat Hunting Report
5
T 
he CrowdStrike Falcon platform has proven unequivocally in dozens of 
independent tests to be a highly effective solution for protecting endpoints 
from modern threats. Still, no technology is 100% effective at blocking 
determined intruders. 
According to data from our customer base indexed by Threat Graph, 68% of 
detections from the last three months were not malware-based. Attackers are 
increasingly attempting to accomplish their objectives without writing malware to the 
endpoint, using legitimate credentials and built-in tools (living off the land) — which are 
deliberate efforts to evade detection by traditional antivirus products.
OverWatch is on a mission to find threats that technology on its own cannot. 
Threat hunting takes place at the front lines of the battle between adversaries and 
defenders. Each year OverWatch sees more adversaries, new tradecraft and faster 
intrusions. In this context, finding the threat is only half the battle; using those insights 
to disrupt adversaries at scale is where the battle is won.
In the 12 months from July 1, 2020 to June 30, 2021, OverWatch’s human threat 
hunters directly identified more than 65,000 potential intrusions, or approximately  
1 potential intrusion every 8 minutes — 24 hours a day, 365 days a year. This 
represents thousands of instances where OverWatch analysts uncovered adversaries 
actively seeking to evade autonomous detection techniques. When considered 
alongside adversaries’ demonstrated ability to begin moving through victim 
environments in just minutes — shown throughout this report — these numbers drive 
home the criticality of continuous threat hunting.
OverWatch is 
on a mission to 
find threats that 
technology on its 
own cannot.
<a name="the-value-of-continuous-threat-hunting"></a>
## The Value of Continuous Threat Hunting
6
65,000
potential intrusions were identified 
and stopped with the help of Falcon 
OverWatch
8 minutes  
is the average interval at which 
OverWatch threat hunters uncovered 
potential intrusions
68% of detections 
from the last three months 
were not malware-based
2021 Threat Hunting Report
7
Crucially, each of these potential intrusions also represents an opportunity to advance 
the autonomous detection techniques in the Falcon platform. With each pass through 
the OverWatch SEARCH threat hunting cycle, hunters hone the Falcon platform’s 
ability to detect similar intrusions more quickly and autonomously. Over the last 
year, threat hunters distilled their findings into the development of hundreds of new 
behavioral-based preventions, resulting in the direct prevention of malicious activity 
on approximately 248,000 unique endpoints. These behavioral-based preventions 
enhance the power of the Falcon platform to uncover novel adversary behavior with 
greater speed and scale.
With the right data and tools, a small team of experts can not only stop today's most 
sophisticated intrusions but also develop insights that drive continuous advancement 
at every level of the security organization.
2021 Threat Hunting Report
8
SENSE
ENRICH
ANALYZE
RECONSTRUCT COMMUNICATE
HONE
Threat Hunting Methodology
OVERWATCH SEARCH
O
verWatch finds threats that technology on its own cannot. 
Human-led threat hunting does not replace autonomous detection 
technologies — rather, it explicitly sets out to complement and augment 
technology-based defenses to ensure that defenders have the power of human 
ingenuity on their side.
OverWatch threat hunters employ the “SEARCH” hunting methodology, described 
below, to systematically detect threats at scale. Working around the clock, 
OverWatch threat hunters methodically sift through a world of unknown unknowns 
to find the faintest traces of malicious activity and deliver actionable analysis to 
CrowdStrike customers in near real time. The OverWatch SEARCH methodology 
shines a light into the darkest corners of customers’ environments — leaving 
adversaries with nowhere to hide.
<a name="overwatch-search-hunting-methodology"></a>
## OverWatch SEARCH Hunting Methodology
2021 Threat Hunting Report
9
CrowdStrike’s rich telemetry creates the foundation for OverWatch threat hunting. 
Upward of 1 trillion events per day, comprising hundreds of event types from 
millions of endpoints, are collected and cataloged by the Falcon platform to provide 
comprehensive visibility into activity across the CrowdStrike install base.
CrowdStrike's proprietary Threat Graph contextualizes events and reveals relationships 
between data points in real time. Threat hunters add a further dimension to the data by 
drawing on CrowdStrike’s up-to-the-minute threat intelligence about the tradecraft of 
more than 160 adversary groups, as well as by using their intimate working knowledge 
of the tactics, techniques and procedures (TTPs) in use in the wild. All of this is 
underpinned by OverWatch’s proprietary tools and processes, which ensure every hunt 
is optimized for maximum efficiency.
OverWatch analysts use a mix of patent-protected hunting workflows and complex 
statistical methods to identify anomalous activity. This is supported by a deep 
understanding of adversary behaviors and motivations, enabling the team to form 
hypotheses about where adversaries may strike. The breadth and depth of experience 
on the OverWatch team is world class, with representation from every corner of public 
and private industry. Further, the team is continuously building its knowledge base, 
going toe-to-toe with adversaries on the front lines, 24/7/365.
In order to take action against an adversary, it is critical to understand the full nature of 
the threat. In just minutes, OverWatch analysts reconstruct threat activity, transforming 
it from a collection of data points into a clear story. This information empowers 
organizations to not only remediate but also plug the gaps in their environment.
Time is of the essence in preventing an intrusion from becoming a breach. OverWatch 
operates as a native component of the Falcon platform. Through Falcon, OverWatch 
delivers clear, accurate and actionable information on potentially malicious activity in 
near real time, enabling organizations to respond quickly and decisively, without friction.
With each new threat, OverWatch extracts new insights to drive continuous 
advancements in automated detections and human threat hunting. The team is 
consistently fine-tuning its skills and processes to always stay a step ahead of the 
adversary.
Sense
Enrich
Analyze
Reconstruct
Communicate
Hone
2021 Threat Hunting Report
10
Intrusion Campaign Numbers
Over the past year, OverWatch tracked steadily increasing numbers of interactive 
intrusion campaigns. Year over year, OverWatch observed a near 60% increase in the 
number of campaigns. In the most recent quarter, from April to June 2021, OverWatch 
uncovered more intrusion campaigns than in any other quarter.
Adversary Motives
For yet another year, financially motivated eCrime activity dominated the interactive 
intrusion attempts tracked by OverWatch. ECrime accounted for 75% of the interactive 
intrusion activity, while targeted intrusions accounted for 24% and the remaining 1% 
was attributed to hacktivist activity. 
eCrime
eCrime
Financially motivated criminal intrusion activity
Targeted
Targeted
State-sponsored intrusion activity that includes cyber espionage, state-nexus 
destruction attacks and currency generation to support a regime
Hacktivist
Hacktivist
Intrusion activity undertaken to gain momentum, visibility or publicity for a 
cause or ideology
These figures track closely with the distribution of activity seen in the previous year. 
Seeing these figures stabilize indicates that the distribution of eCrime and targeted 
intrusion activity may be reaching an equilibrium after several years of eCrime activity 
rapidly expanding relative to targeted intrusions.
Year over year, OverWatch observed a near 60% 
increase in the number of interactive intrusion 
campaigns.
<a name="intrusion-campaigns-summary"></a>
## Intrusion Campaigns Summary
2021 Threat Hunting Report
11
INTRUSION CAMPAIGNS BY THREAT TYPE
July 2019 to June 2020 vs. July 2020 to June 2021
![Figure 1. Relative distribution of targeted intrusion, eCrime and hacktivist activity uncovered by OverWatch]
Figure 1. Relative distribution of targeted intrusion, eCrime and hacktivist activity uncovered by 
OverWatch
eCrime
There are signs that eCrime adversaries may be becoming more capable, particularly 
if measured by the speed at which they can move through a victim environment. 
OverWatch measures breakout time — the time an adversary takes to move laterally, 
from an initially compromised host to another host within the victim environment. 
Of the hands-on eCrime intrusion activity from July 1, 2020 to June 30, 2021 where 
breakout time could be derived, the average was just 1 hour 32 minutes. Moreover, the 
OverWatch team found that in 36% of those intrusions, the adversary was able to move 
laterally to additional hosts in less than 30 minutes. 
ECrime adversaries also continue to innovate and evolve their business models to 
increase their chance of success. The majority of ransomware operators engaged in 
big game hunting (BGH) activity have now adopted the threat of data leaks alongside 
data encryption as a means to extract payment from victims. Many adversaries have 
also established dedicated leak sites (DLSs) as a forum to publicize victim details and 
release the stolen data. INDRIK SPIDER is an exception to this trend toward the use of 
data extortion. 
Another feature of the eCrime threat landscape in the past 12 months is the growing 
importance of access brokers who play a role in facilitating access for other eCrime 
actors to stage their intrusions. The feature story In Pursuit of PROPHET in this report 
takes a look at access brokers in action. 
eCRIME 
BREAKOUT TIME
Initial Access
Lateral Movement
1 HOUR 
32 MINUTES
PANDAs (China)
SUSPECTED STATE-SPONSORED (Not Attributed)
KITTENs (Iran)
CHOLLIMAs (North Korea)
BEARs (Russia)
BUFFALOs (Vietnam)
2021
2020
Hacktivist 1%
Hacktivist 1%
Targeted Intrusion 23%
Targeted Intrusion 24%
eCrime 76%
eCrime 75%
PANDAs (China)
SUSPECTED STATE-SPONSORED (Not Attributed)
KITTENs (Iran)
CHOLLIMAs (North Korea)
BEARs (Russia)
BUFFALOs (Vietnam)
2021 Threat Hunting Report
12
OverWatch also recorded a 100% increase in instances of cryptojacking in interactive 
intrusions year over year. This was likely driven by steep increases in cryptocurrency 
values beginning in late 2020.
The potential for growth in eCrime activity is almost limitless, propelled by new actors, 
new vulnerabilities or failures on the part of organizations to maintain basic security 
hygiene. While OverWatch indeed saw an increase in the number of eCrime intrusion 
attempts over the past 12 months, this growth did not outpace the growth in targeted 
intrusion activity to the degree seen in previous years. 
One factor that may have stemmed the rapid acceleration of eCrime activity 
is successful interventions by law enforcement against adversary-controlled 
infrastructure and resources. These efforts touched the operations of several 
prominent eCrime groups including WIZARD SPIDER, MUMMY SPIDER, CIRCUS 
SPIDER, GRACEFUL SPIDER, TWISTED SPIDER and CARBON SPIDER. Law 
enforcement activity, however, appears to only temporarily disrupt eCrime activity, 
rather than halting operations altogether. Adversaries have shown resilience by quickly 
activating new C2 infrastructure and diversifying their toolsets.
Targeted Intrusion
Generally, adversary groups from the People’s Republic of China, the Democratic 
People’s Republic of Korea (DPRK, aka North Korea) and the Islamic Republic of 
Iran are the source of the majority of targeted intrusion[^5] activity OverWatch tracks. 
However, in the past year, OverWatch also tracked an uptick in suspected state-nexus 
activity not attributed to named actor groups.
[^5]: Again, the term “targeted intrusion” in this report refers to state-nexus or other advanced persistent 	
	
threat actors.
![Figure 2. Proportion of targeted intrusion activity conducted by different targeted adversary groups, July 2020 to June 2021]
Figure 2. Proportion of targeted intrusion activity conducted by different targeted adversary 
groups, July 2020 to June 2021
67%
20%
7%
5% 1% 1%
2021 Threat Hunting Report
13
In the year leading up to June 30, 2021, Chinese state-nexus adversaries (aka PANDAs) 
maintained a high operational tempo and conducted sustained and wide-ranging 
campaigns motivated both by intellectual property (IP) theft and intelligence gathering 
objectives. PANDAs were among the targeted intrusion adversaries most commonly 
uncovered by OverWatch threat hunters during this period. 
A notable development in early 2021 was the mass exploitation of Microsoft Exchange 
Server vulnerabilities by suspected China-nexus adversaries. This serves as a reminder 
of the diverse skill sets of China-nexus actors and highlights the ever-present threat of 
new vulnerabilities being found and exploited. A story later in this report — OverWatch 
Disrupts Microsoft Exchange Zero-Day Exploits with Falcon Complete — examines 
how CrowdStrike’s managed services worked together to disrupt and expel an as-yet-
unnamed threat.
OverWatch tracked relatively consistent levels of activity attributed to North Korea 
(CHOLLIMAs). CrowdStrike Intelligence reports that North Korean actors — including 
two actors tracked by OverWatch in the past 12 months, LABYRINTH CHOLLIMA and 
SILENT CHOLLIMA — continue to make iterative updates and improvements to their 
toolsets. An intrusion story later in this report — Custom Tooling Rings Alarm Bells in 
Intrusion by (Not So) SILENT CHOLLIMA — sheds light on how some of this custom 
tooling has been used in the wild.
In contrast to the observed China-nexus and DPRK adversary activity, OverWatch saw 
a downturn in activity stemming from Iran (KITTENs). CrowdStrike Intelligence reports 
that in 2020, many of Iran’s observed intrusion efforts focused on targets related 
to narrower geopolitical and domestic concerns; this may have contributed to the 
reduction in campaigns seen by OverWatch. 
OverWatch also uncovered a number of intrusion campaigns with all of the hallmarks 
of state-nexus activity, but that cannot at this time be attributed to any of the named 
adversary groups tracked by CrowdStrike Intelligence. Much of this activity targeted 
the telecommunications industry, explored in detail in the Signal Interference feature 
later in this report. This increase in activity attributable to diverse and globally 
dispersed mission clusters underscores the variety of targeted intrusion threats that 
exist in the current threat landscape.
Hacktivism
Hacktivism accounted for only a small fraction of the interactive activity tracked by 
OverWatch. All hacktivist activity seen by OverWatch has been attributed to a single 
adversary group — FRONTLINE JACKAL, an Iranian nationalist hacktivist group known 
to deface websites and carry out other disruptive online activity targeting U.S., Israeli 
and Saudi Arabian organizations. Adversary activity observed by OverWatch provided 
CrowdStrike Intelligence with additional visibility into this group’s operating procedures. 
Intrusions by Industry Vertical
Figure 3 shows the top 10 industry verticals that featured most frequently in the 
interactive intrusion activity uncovered by OverWatch from July 2020 to June 2021. 
The same 10 industries also made up the top 10 list for the 12-month period from July 
2019 to June 2020. Notably, the technology industry has now held the top spot for the 
past three years.
2021 Threat Hunting Report
14
TOP 10 VERTICALS BY INTRUSION FREQUENCY 
July 2020 to June 2021
![Figure 3. The figure shows which industry verticals were most frequently impacted by interactive intrusions and also shows any changes relative to the period from July 2019 to June 2020]
Figure 3. The figure shows which industry verticals were most frequently impacted by interactive 
intrusions and also shows any changes relative to the period from July 2019 to June 2020
While Figure 3 shows the prevalence of intrusion activity against particular industries 
within the OverWatch data, it does not illustrate the significant overall growth in 
the number of intrusions. As noted at the start of this report, total intrusion activity 
observed by OverWatch increased by approximately 60% year over year — and the 
growth in intrusion activity within several of the industries in this top 10 list exceeded 
that rate of increase. 
A year-over-year comparison of the total number of intrusion attempts that OverWatch 
observed finds that intrusions targeting the telecommunications and retail industries 
more than doubled. The professional services industry saw a more than 90% increase 
in interactive intrusion numbers, while the government and academic sectors both saw 
intrusion numbers increase by more than 80%.
The ranking of the top industries changes when the data is broken out by threat 
type, specifically targeted intrusion vs. eCrime activity. Figure 4 shows the top five 
industries most frequently impacted by interactive intrusions carried out by targeted 
intrusion and eCrime adversaries respectively. 
0%
5%
10%
15%
20%
Technology
Telecommunications
Manufacturing
Financial
Professional Services
Academic
Healthcare
Retail
Government
Engineering
Technology
Manufacturing
Professional Services
Financial
Retail
Telecommunications
Technology
Healthcare
Government
Academic
July 2020 to June 2021
July 2019 to June 2020
0%
5%
10%
15%
20%
25%
30%
35%
40%
45%
50%
0%
5%
10%
15%
20%
25%
30%
35%
40%
45%
50%
Change relative to July 2019 to June 2020
2021 Threat Hunting Report
15
TOP 5 VERTICALS BY INTRUSION FREQUENCY 
Targeted Intrusion vs. eCrime Activity, 
July 2020 to June 2021
![Figure 4. Comparison of the industry verticals most frequently impacted by targeted intrusion vs. eCrime threat actors. July 2020 to June 2021]
Figure 4. Comparison of the industry verticals most frequently impacted by targeted intrusion vs. 
eCrime threat actors. July 2020 to June 2021
The telecommunications industry notably accounted for 40% of all targeted intrusion 
activity uncovered by OverWatch in the 12 months to June 30, 2021, explored in detail 
in the Signal Interference feature later in this report. Other notable inclusions in the 
targeted intrusion “Top 5” are the healthcare and academic industries, which fell victim 
to ongoing targeting over the reporting period, particularly due to their involvement in 
COVID-19 related research.[^6]
ECrime intrusions, in contrast, were more evenly distributed across industry verticals. 
This is indicative of the opportunistic nature of much of eCrime activity, which leads to 
a much wider spread of activity across diverse industry verticals.
[^6]: To read more about targeting of COVID-19 research, see the 2021 CrowdStrike Global Threat Report, 	
	
and the CrowdStrike blog Don’t Get Schooled: Understanding the Threats to the Academic Industry.
0%
5%
10%
15%
20%
Healthcare
Retail
Government
Engineering
Technology
Manufacturing
Professional Services
Financial
Retail
Telecommunications
Technology
Healthcare
Government
Academic
July 2020 to June 2021
July 2019 to June 2020
0%
5%
10%
15%
20%
25%
30%
35%
40%
45%
50%
0%
5%
10%
15%
20%
25%
30%
35%
40%
45%
50%
TARGETED INTRUSIONS
eCRIME
2021 Threat Hunting Report
16
Adversary Activity
In the year to June 30, 2021, OverWatch uncovered interactive intrusion activity 
conducted by 30 distinct named threat actor groups. In addition, threat hunters 
uncovered an extensive array of activity suspected of being eCrime or targeted 
intrusion activity, but not specifically tied to a named group. 
Figure 5 provides a breakdown of the adversaries observed by OverWatch. ECrime 
activity was by far the most widespread across industry verticals, followed by intrusions 
conducted by PANDA adversaries. 
OverWatch uncovered activity by 13 named eCrime (aka SPIDER) adversary groups. 
Of these groups, WIZARD SPIDER[^7] was the most prolific, with nearly twice as many 
intrusion attempts than any other eCrime group observed by OverWatch. WIZARD 
SPIDER deployed the Cobalt Strike Beacon in more than half of these intrusions; other 
commonly seen tools included Ryuk ransomware, the Windows backdoor access tool 
BazarLoader and the Active Directory discovery tool AdFind.
For targeted intrusion activity, intrusions attributed to People’s Republic of China (aka 
PANDA) actors were the most common. OverWatch uncovered intrusion attempts 
by eight separate named China-nexus adversaries, with WICKED PANDA[^8] being the 
most active. WICKED PANDA also frequently deployed Cobalt Strike using bespoke 
loaders such as AttachLoader while also deploying the custom Winnti, ShadowPad and 
RouterGod backdoors. 
A few things to note about the data presented in Figure 5:
	

The heat mapping represents the number of distinct actors active within a particular 
vertical.
	

The heat mapping does not represent the total number of intrusion attempts within a 
vertical, as multiple intrusions by the same adversary group are only represented once. 
	

Attribution to a high degree of confidence is not always possible. This table does 
not reflect any unattributed activity that occurred in any of the industry verticals. 
	

Verticals not listed in this chart indicate that OverWatch did not record any 
intrusions attributable to a specific actor group during this period.
[^7]: To learn more about WIZARD SPIDER, check out the CrowdStrike Adversary Universe.
[^8]: To learn more about WICKED PANDA, check out the CrowdStrike Adversary Universe.
2021 Threat Hunting Report
17
![Figure 5. Heat map of intrusion campaigns by adversary group and industry vertical, July 2020 to June 2021]
Figure 5. Heat map of intrusion campaigns by adversary group and industry vertical, July 2020 to June 2021
VERTICAL
BEARs
Russia
BUFFALOs
Vietnam
CHOLLIMAs
N. Korea
JACKALs
Hacktivist
KITTENs
Iran
PANDAs
China
SPIDERs
eCrime
Academic
Aerospace
Agriculture
Automotive
Aviation
Biotechnology
Chemical
Conglomerate
Defense
Education
Energy
Engineering
Entertainment
Financial
Food & Beverage
Government
Healthcare
Hospitality
Insurance
Law Enforcement
Legal
Manufacturing
Maritime
Media
Mining
NGO
Nonprofit
Oil & Gas
Pharmaceutical
Professional Services
Rail
Real Estate
Retail
Services
Technology
Telecommunications
Think Tanks
Transportation & Logistics
2021 Threat Hunting Report
18
2021 Threat Hunting Report
18
O
verWatch is a sophisticated threat hunting team that finds and disrupts 
adversary activity on a global scale. OverWatch carefully documents the 
details of each intrusion it uncovers, building a rich data set of adversary 
activity. With each new intrusion, threat hunters create a sharper picture of the 
threat landscape and the tradecraft of the adversaries that inhabit it.
This data-driven analysis of adversary tradecraft seeks to better equip defenders to 
take a proactive and evidence-informed approach to protecting their environment. 
The analysis below draws on OverWatch’s rich repository of intrusion data collected 
over the past year. It begins with a visualization of interactive intrusion activity observed 
by OverWatch threat hunters in a MITRE ATT&CK® heat map. It then details the 
techniques and tools encountered most often by OverWatch, thereby indicating where 
defenders can potentially achieve the greatest return on hunting efforts. It goes on to 
examine outliers in the data, highlighting the more novel and sophisticated techniques 
OverWatch uncovered. 
MITRE ATT&CK Heat Map
OverWatch tracks interactive intrusion activity against the MITRE ATT&CK Enterprise 
Matrix. The following heat map illustrates the prevalence of adversary tactics, 
techniques and sub-techniques observed by OverWatch threat hunters from  
Jan. 1, 2021 to June 30, 2021.[^9] This heat map represents activity seen in interactive 
intrusions only, and does not reflect the breadth of activity seen and stopped by the 
Falcon platform. This table excludes any techniques or sub-techniques not observed  
by OverWatch in this reporting period.
[^9]: While the rest of this report covers a 12-month period, the heat map only includes data from Jan. 1, 2021, 	
	
when OverWatch began tracking against the latest MITRE ATT&CK matrix, which, among other changes, 	
	
introduced sub-techniques.
<a name="adversary-technique-and-tooling-insights"></a>
## Adversary Technique and Tooling Insights
2021 Threat Hunting Report
19
MITRE ATT&CK HEAT MAP, 1 OF 3
Initial Access
Execution
Persistence
Privilege Escalation
Def
Technique
Sub-technique
Technique
Sub-technique
Technique
Sub-technique
Technique
Sub-technique
Techniqu
Valid Accounts
Domain Accounts
Command and Scripting 
Interpreter
Windows Command 
Shell
Valid Accounts
Domain Accounts
Valid Accounts
Domain Accounts
Valid Accounts
Local Accounts
PowerShell
Local Accounts
Local Accounts
Default Accounts
Unix Shell
Default Accounts
Default Accounts
Exploit Public-Facing 
Application
Visual Basic
Scheduled Task/Job
Scheduled Task
Process Injection
Dynamic-link Library 
Injection
Masquerading
Phishing
Spearphishing 
Attachment
Python
Cron
Process Hollowing
Spearphishing Link
JavaScript
Create Account
Local Account
Portable Executable 
Injection
Spearphishing via 
Service
Windows Management 
Instrumentation
Domain Account
Thread Execution 
Hijacking
Indicator Removal o
External Remote Services
Scheduled Task/Job
Scheduled Task
Server Software Component
Web Shell
Scheduled Task/Job
Scheduled Task
Drive-by Compromise
Cron
Account Manipulation
SSH Authorized Keys
Cron
Trusted Relationship
System Services
Service Execution
Event Triggered Execution
Accessibility 
Features
Abuse Elevation Control 
Mechanism
Bypass User Account 
Control
User Execution
Malicious File
Image File Execution 
Options Injection
Elevated Execution 
with Prompt
Malicious Link
Windows 
Management 
Instrumentation 
Event Subscription
Setuid and Setgid
Exploitation for Client 
Execution
Component Object 
Model Hijacking
Sudo and Sudo 
Caching
Impair Defenses
Inter-Process Communication Dynamic Data 
Exchange
Boot or Logon Autostart 
Execution
Registry Run Keys / 
Startup Folder
Event Triggered Execution
Accessibility 
Features
Shared Modules
Security Support 
Provider
Image File Execution 
Options Injection
Signed Binary Proxy
Create or Modify System 
Process
Windows Service
Windows 
Management 
Instrumentation 
Event Subscription
External Remote Services
Component Object 
Model Hijacking
Hijack Execution Flow
DLL Search Order 
Hijacking
Boot or Logon Autostart 
Execution
Registry Run Keys / 
Startup Folder
DLL Side-Loading
Security Support 
Provider
Process Injection
Path Interception by 
Search Order 
Hijacking
Create or Modify System 
Process
Windows Service
BITS Jobs
Exploitation for Privilege 
Escalation
O ce Application Startup
O ce Template 
Macros
Hijack Execution Flow
DLL Search Order 
Hijacking
Browser Extensions
DLL Side-Loading
Modify Registry
Compromise Client Software 
Binary
Path Interception by 
Search Order 
Hijacking
Obfuscated Files or 
Information
Domain Policy Modiﬁcation
Group Policy 
Modiﬁcation
Access Token Manipulation
Hide Artifacts
File and Directory Pe
Modiﬁcation
Deobfuscate