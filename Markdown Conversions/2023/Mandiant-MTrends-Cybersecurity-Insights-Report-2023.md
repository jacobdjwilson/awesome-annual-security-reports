# MANDIANT SPECIAL REPORT

## Table of Contents
[Introduction](#introduction)
[By the Numbers](#by-the-numbers)
[Data from Mandiant Investigations](#data-from-mandiant-investigations)
[The Invasion of Ukraine: Cyber Operations During Wartime](#the-invasion-of-ukraine-cyber-operations-during-wartime)
[Strategic Cyber Espionage and Pre-Positioning Prior to Invasion](#strategic-cyber-espionage-and-pre-positioning-prior-to-invasion)
[Initial Destructive Cyber Operations and Military Invasion](#initial-destructive-cyber-operations-and-military-invasion)
[Sustained Targeting and Attacks](#sustained-targeting-and-attacks)
[Maintaining Footholds for Strategic Advantage](#maintaining-footholds-for-strategic-advantage)
[Renewed Tempo of Disruptive Attacks](#renewed-tempo-of-disruptive-attacks)
[Information Operations Surrounding Russia’s Invasion of Ukraine](#information-operations-surrounding-russias-invasion-of-ukraine)
[Takeaways](#takeaways)
[North Korea’s Financial Operations Continue to Evolve](#north-koreas-financial-operations-continue-to-evolve)
[NFTs, Bridges, Ransomware and More: North Korean Cybercrime in 2022](#nfts-bridges-ransomware-and-more-north-korean-cybercrime-in-2022)
[Not Just Money: Continued Intelligence Collection Operations in Context](#not-just-money-continued-intelligence-collection-operations-in-context)
[Shifting Focus and Uncommon Techniques Brought Threat Actors Success in 2022](#shifting-focus-and-uncommon-techniques-brought-threat-actors-success-in-2022)
[Initial Intrustions](#initial-intrustions)
[Getting Around and Getting Out](#getting-around-and-getting-out)
[Making Things Personal](#making-things-personal)
[Lessons Learned](#lessons-learned)
[Red Team Case Study: Cloud-focused Operations](#red-team-case-study-cloud-focused-operations)
[Initial Compromise](#initial-compromise)
[Lateral Movement to Azure](#lateral-movement-to-azure)
[Attacking a Password Manager Solution](#attacking-a-password-manager-solution)
[Gaining Visibility within Azure](#gaining-visibility-within-azure)
[Privilege Escalation to Global Administrator Solution](#privilege-escalation-to-global-administrator-solution)
[Attacking the Software Development Life Cycle (SDLC)](#attacking-the-software-development-life-cycle-sdlc)
[Outcomes](#outcomes)
[Targeted Attack Lifecycle Mapping](#targeted-attack-lifecycle-mapping)
[2022 Campaigns and Global Events](#2022-campaigns-and-global-events)
[Campaigns—Threat Actors](#campaigns-threat-actors)
[Global Events—Notable Vulnerabilities](#global-events-notable-vulnerabilities)
[Notable and Recently Graduated Threat Groups](#notable-and-recently-graduated-threat-groups)
[How a Threat Cluster Becomes an APT or FIN Group](#how-a-threat-cluster-becomes-an-apt-or-fin-group)
[APT42 Conducts Highly Targeted Surveillance Operations](#apt42-conducts-highly-targeted-surveillance-operations)
[Conclusion](#conclusion)
[Bibliography](#bibliography)

## Introduction
The lines separating the real world and the cyber realm have never been hazier. We’re seeing  
Russia engage in information operations in an attempt to influence the narrative surrounding  
their invasion of Ukraine, and attempt to disrupt critical infrastructure through both physical and 
cyber attacks. We’re seeing the invasion have an influence on the broader cybercrime ecosystem, 
notably in Europe, where actors are choosing sides or shutting down operations altogether. And 
we’re seeing actors engage in cybercrime to fund espionage to support the North Korean regime, 
targeting information on topics ranging from nuclear to COVID-19.

Every day Mandiant responders are investigating and analyzing the latest attacks and threats,  
and understanding how best to respond to and mitigate them. We pass these learnings on to  
our customers through our various services, helping them to stay ahead of a constantly evolving 
threat landscape.

In releasing our annual M-Trends report, we aim to provide some of that same critical intelligence  
to the greater security community. M-Trends 2023 continues our tradition of offering details  
on the evolving cyber landscape, mitigation recommendations, and a wide variety of security  
incident-related metrics.

Let’s start with answering one of the biggest questions from our “By the Numbers” section.  
The answer is yes, attacks are being detected faster than ever before. From January 1, 2022,  
to December 31, 2022, the global median dwell time is now 16 days, down from 21 days in our 
M-Trends 2022 report. This may demonstrate an improved ability to detect attacks, but we  
also credit ransomware attacks to be a driving factor in reducing dwell time. Intrusions  
involving ransomware had a median dwell time of 9 days in 2022, compared to 5 days reported  
in M-Trends 2022.

The topics of M-Trends 2023 include:

*   **By the Numbers:** Organizations were notified of breaches by external entities in 63% of incidents 
compared to 47% in M-Trends 2022, which brings the global detection rates closer to what 
defenders experienced in 2014. We have many more signature metrics on targeted industries, 
attack types, threat groups, and malware use, along with new breakdowns based on trends  
and observations.
*   **The Invasion of Ukraine:** Russia’s invasion of Ukraine has consumed almost every aspect of 
Russia's international relationships, and has evolved as nearly the sole driver of cyber threat 
activity from Russia in 2022. We cover operations dating back to before the physical invasion in 
February, including use of destructive and disruptive attacks, and information operations.
*   **North Korean Financial Operations:** For years, North Korea has reportedly conducted various illicit 
financial activities to fund the regime. The explosive growth of cryptocurrency is converging with 
aggressive and flexible North Korean cyber capabilities, making it natural that at least some North  
Korean threat groups would expand operations into this sector.
*   **Shifting Focus and Uncommon Techniques:** In 2022, Mandiant investigated a series of high-profile 
intrusions that were successful and impactful to the targeted organizations despite significant  
deviations from common threat actor behaviors, underscoring the threat posed to organizations  
by persistent adversaries willing to eschew the unspoken rules of engagement.

M-Trends 2023 additionally contains a red team case study, tales of threat actors and vulnerabilities 
from our Campaign and Global Events team, and details from our APT42 graduation. 

M-Trends builds on our dedication to continue providing critical knowledge to those tasked with  
defending organizations. The information in this report has been sanitized to protect the identities  
of victims and their data.

## By the Numbers
### Data from Mandiant Investigations
The metrics reported in M-Trends 2023 are based on Mandiant Consulting 
investigations of targeted attack activity conducted between January 1, 2022  
and December 31, 2022. Note that this edition of M-Trends returns to a 12-month 
period compared to the 15-month period reported in M-Trends 2022.

#### Detection by Source
In 2022, Mandiant observed a general increase in the number of organizations that 
were alerted by an external entity of historic or ongoing compromise. Organizations 
were notified of breaches by external entities in 63% of incidents. This continues  
the trend observed in 2021 and brings the global detection rates closer to what 
defenders experienced in 2014. The increase in external notification observed in 
2022 is likely impacted by Mandiant’s investigative support of cyber threat activity 
which targeted Ukraine and an increase in proactive notification efforts. Proactive 
notifications from security partners enable organizations to launch response efforts 
more effectively. Analysis of Mandiant’s efforts in Ukraine are highlighted in The 
Invasion of Ukraine: Cyber Operations During Wartime.

*Image Description: A line graph titled "Detection by Source, 2011-2022" showing the percentage of external and internal detections over the years. The external detection rate has increased significantly in 2022, while the internal detection rate has decreased.*

*   **Internal detection** is when an organization independently discovers it has been compromised.
*   **External detection** is when an outside entity informs an organization it has been compromised.

*Image Description: Three bar charts titled "Detection by Source by Region, 2022" showing the percentage of external and internal detections for the Americas, EMEA, and APAC regions.*

Historically, Mandiant has observed relatively stable detection rates for 
organizations headquartered in the Americas. However, in 2022, organizations  
were notified by an external entity in 55% of incidents, compared to 40% of  
incidents last year. This is the highest percentage of external notifications the 
Americas has seen over the past six years. While organizations in the Americas 
continue to improve detection capabilities, external notifications from trusted 
security partners remain the primary way organizations are made aware of incidents. 

In 2022, 33% of the incidents Mandiant experts responded to in the Asia Pacific 
(APAC) region were originally identified by internal entities. However, over the past  
six years, Mandiant has observed a trend towards greater external notifications  
in the APAC region. This year’s 9-percentage point increase in internal detections  
when compared to 2021 demonstrates the strong variability Mandiant has observed 
in detection source in the APAC region.

Organizations in Europe, the Middle East and Africa (EMEA) were alerted of an 
intrusion by an external entity in 74% of investigations in 2022 compared to 62%  
in 2021. This marked increase in external notifications could be explained by 
Mandiant’s investigative support to Ukraine and is likely an outlier from the general 
trend. Mandiant continues to see a shift to more external notifications in the EMEA 
region over the past six years, however because of extenuating circumstances in 
2022, this trend may stabilize in the future.

*Image Description: Three line graphs titled "Detection by Source by Region, 2017–2022" showing the percentage of external and internal detections over the years for the APAC, EMEA, and Americas regions.*

*Image Description: A bar chart titled "Detection by Source, by Investigation Type, 2022" showing the percentage of external and internal detections for all investigations, ransomware investigations, and non-ransomware investigations.*

*Image Description: A pie chart titled "Ransomware Investigations—External Notification Source" showing the percentage of adversary notification and external partner notification in ransomware investigations.*

In 2022, external notifications were more prevalent as a notification source 
regardless of the investigation type. In intrusions related to ransomware, 
organizations were notified by an external entity in 70% of investigations. 
Organizations were predominantly notified by adversaries due to a fully  
executed ransomware event with 67% of investigations (8% of all investigations) 
detected due to a ransom note. Notifications from external partners comprise  
the remaining 33% of ransomware related investigations (4% of all investigations).

Similarly, organizations were notified by external entities of non-ransomware  
related intrusions more often than the organization was able to identify similar 
intrusions internally. However, Mandiant observed organizations in 2022 identify 
non-ransomware intrusions internally more often than ransomware intrusions.  
This may be due to increased visibility allowing organizations to detect intrusions 
earlier in the Targeted Attack Life Cycle. While non-ransomware operations often 
prioritize avoiding detection mechanisms, the longer operations cycles provides  
more detection opportunities when compared to the relatively short cycle  
employed by ransomware operators.

Mandiant continues to see positive collaboration between organizations and  
external partners that perform compromise notifications. These external parties 
provide effective information that aids an organization’s ability to identify intrusions 
more quickly, regardless of the investigation type.

>A ransomware related intrusion provides access for, or is associated with, a malicious actor that has the primary goal of encrypting data with the intention of extracting payment from the target in order to avoid further or undo the malicious action.

#### Global Median Dwell Time
*Image Description: A table titled "Global Median Dwell Time, 2011-2022" showing the median dwell time for all, external, and internal detections over the years.*

Global median dwell time continued to improve year over year, with organizations 
detecting incidents in just over two weeks in 2022. This is the shortest global  
median dwell time from all M-Trends reporting periods.

Notable improvement in global median dwell time where an external entity was the 
notification source may indicate that organizations respond to external notifications 
more quickly. This reflects a growing recognition of the critical role partnerships  
and information exchange play in building a resilient cybersecurity ecosystem. As 
security partners are improving the critical information contained within external 
notifications, the improvement of information sharing will enable organizations  
to act more effectively than if left to identify similar intrusions on their own.

Defenders continue to detect events faster than external entities notify. The  
global median dwell time for internally detected incidents in 2022 returned to  
similar timeframes defenders saw in 2020. In 2022, the global median dwell time for 
intrusions detected internally was 13 days. The global median dwell time was 18 days 
in 2021 and 12 days in 2020.

Similarly, Mandiant experts observed another significant decrease in the global 
median dwell time for investigations with an external notification source in 2022, 
down 32% compared to 2021. External notifications allowed for organizations to 
initiate response to intrusions within a median of 19 days of the initial compromise.

Improvements in global median dwell time in 2022, regardless of detection source, 
enabled organizations to respond to incidents faster than ever before.

>Dwell time is calculated as the number of days an attacker is present in a victim environment before they are detected. The median represents a value at the midpoint of a data set sorted by magnitude.

*Image Description: A stacked bar chart titled "Global Dwell Time Distribution, 2018-2022" showing the distribution of dwell times in days for each year.*

Global dwell time distribution continues to improve. 42% of intrusions were detected 
within a week or less, compared to 37% of intrusions in the last reporting period. 
Compared to previous years, Mandiant saw more evenly dispersed dwell times  
across investigations in 2022. Continuing trends from the last M-Trends reporting 
period, this could indicate that detection is becoming more streamlined and 
detection abilities have improved to highlight actions in the environment during  
the initial infection or the reconnaissance phases of the Targeted Attack Lifecycle.

However, as Mandiant continues to see a wider distribution for non-ransomware 
related investigations, organizations are still facing intrusions that go undetected for 
extensive periods of time. Variance in the detection capabilities of impacted 
organizations and the types of intrusions they face are likely contributors to this 
distribution spread.

*Image Description: A bar chart titled "Global Dwell Time by Investigation Type, 2022" showing the median dwell time for all, ransomware, and non-ransomware investigations.*

*Image Description: A bar chart titled "Global Median Dwell Time by Detection Source" showing the median dwell time for ransomware and non-ransomware investigations detected internally and externally.*

Mandiant experts note a decrease in the percentage of global intrusions involving 
ransomware between 2021 and 2022. In 2022, 18% of intrusions involved ransomware 
compared to 23% in 2021. Ransomware attacks continue to be a driving factor in  
a reduced dwell time. Intrusions involving ransomware had a median dwell time  
of 9 days in 2022, compared to 5 days in 2021. Mandiant observed that in instances 
where external entities are making the notification, the global median dwell time  
for intrusions involving ransomware was 7 days compared to 12 days when an 
organization detected the intrusion internally. Mandiant observed that adversaries 
leveraging ransomware remained undetected for longer periods of time in 2022 
compared to 2021.

#### Americas Median Dwell Time
*Image Description: A line graph titled "Americas Median Dwell Time, 2016-2022" showing the median dwell time for all, external, and internal detections over the years in the Americas region.*

The median dwell time for intrusions investigated in the Americas decreased  
by a full week in 2022 to 10 days compared to 17 days in 2021 and 2020. Mandiant 
observed consistent median dwell times for all detection types in the Americas,  
with internal detections decreasing to 9 days and external detections at its lowest 
with 12 days. Organizations in the Americas demonstrated another year of 
improvement for detecting adversaries faster than previous years, quicker  
than the previously smallest timeframe of 17 days observed in 2021.

*Image Description: A stacked bar chart titled "Americas Dwell Time Distribution, 2021-2022" showing the distribution of dwell times in days for each year in the Americas region.*

In the Americas, 64% of intrusions were detected in 30 days or less and 70% of these 
intrusions (45% of total intrusions in the Americas) were detected in less than one 
week. In 2022, more than half of the intrusions in the Americas were detected in less 
than two weeks. However, Mandiant observed a small uptick in intrusions that go 
undetected for longer periods of time, with 7% of total intrusions in the Americas 
remaining undetected for more than a year. This is an increase from 4% observed  
in the reporting period of M-Trends 2022. This shows that while organizations in  
the Americas were able to detect most intrusions within two weeks, due to detection 
improvements, they identified intrusions by adversaries that would have otherwise 
remained undetected for longer.

*Image Description: A bar chart titled "Americas Dwell Time Investigation by Type, 2022" showing the median dwell time for all, ransomware, and non-ransomware investigations in the Americas region.*

*Image Description: A bar chart titled "Americas Median Dwell Time by Detection Source" showing the median dwell time for ransomware and non-ransomware investigations detected internally and externally in the Americas region.*

Although the percentage of intrusions involving ransomware has decreased  
globally, Mandiant observed a consistent percentage of investigations in the 
Americas involving ransomware compared to last year. Similarly, ransomware  
dwell time continues to remain the same in the Americas region. Mandiant noted  
that these investigations have similar median dwell times regardless of internal or 
external detection source, with five days median dwell time for internally notified 
investigations, and six days when external entities make the notification. Mandiant 
continues to observe improvements in external notifications for non-ransomware 
related intrusions. In 2022 organizations in the Americas detected intrusions that  
did not relate to ransomware in 12 days, compared to 17 days in 2021.

#### APAC Median Dwell Time
*Image Description: A line graph titled "APAC Median Dwell Time, 2016-2022" showing the median dwell time for all, external, and internal detections over the years in the APAC region.*

Overall, median dwell time in APAC increased compared to the last M-Trends 
reporting period. However, organizations in APAC are still detecting intrusions  
more quickly than in previous years, with a median dwell time of 19 days for intrusions 
identified internally compared to 22 days in 2021. Organizations in APAC have 
consistently improved internal detection capabilities over the past three years.

Notifications from external entities resulted in a median dwell time of 58 days in 2022 
compared to 16 days in 2021. While this represents an increase in median dwell time, 
it is still a 58% decrease compared to external notification median dwell time in 2020 
which was 137 days. The increase to 58 days is likely a result of the median dwell time 
numbers normalizing from an abnormally short period of time observed in 2021.

*Image Description: A stacked bar chart titled "APAC Dwell Time Distribution, 2021-2022" showing the distribution of dwell times in days for each year in the APAC region.*

APAC dwell time distribution continues to show variability. Dwell time distribution 
shows 48% of APAC investigations had dwell times of 30 days or less with 76% of 
these intrusions (37% of all APAC intrusions) detected in one week or less. On the 
other side of the dwell time distribution, APAC organizations had a wider distribution 
of intrusions go undetected for longer periods of time, with 30% of investigations 
remaining undetected for a year or longer compared to 20% of investigations in 2021.

Cyber security continues to mature in APAC with ongoing detection capability 
improvements. This allows organizations to identify intrusions that would have 
otherwise gone long undetected, resulting in a wider distribution of intrusions.

*Image Description: A bar chart titled "APAC Dwell Time by Investigation Type, 2022" showing the median dwell time for all, ransomware, and non-ransomware investigations in the APAC region.*

*Image Description: A bar chart titled "APAC Median Dwell Time by Detection Source" showing the median dwell time for ransomware and non-ransomware investigations detected internally and externally in the APAC region.*

Similar to the observed decrease in global investigations involving ransomware, 
APAC saw a 6-percentage point decrease in ransomware investigations, with 32%  
in 2022 compared to 38% in 2021. This number is still almost double the percentage 
of investigations from 2020 (12.5%) and 2019 (18%).

The median dwell time for ransomware investigations in APAC was 18 days compared 
to 60 days for non-ransomware investigations. Organizations in APAC are quicker to 
detect incidents internally than externally, regardless of the type of investigation. 
However, the timeframe observed with relation to ransomware median dwell time 
does significantly impact dwell time as a whole.

#### EMEA Median Dwell Time
*Image Description: A line graph titled "EMEA Median Dwell Time, 2016-2022" showing the median dwell time for all, external, and internal detections over the years in the EMEA region.*

Organizations in EMEA detected incidents 58% faster in 2022 compared to 2021, with 
the overall median dwell time now less than three weeks. Looking closer at detection 
sources, median dwell time for intrusions that were detected by an internal source 
increased from 13 days seen in 2021 to 33 days in 2022. External notification sources 
decreased from 60 days seen in 2021 to 18 days in 2022. This large change may be 
influenced by Mandiant’s work in Ukraine, which makes up a notable portion EMEA 
investigations in 2022. However, even outside of this work, the general trend shows 
that median dwell time continues to decrease year over year.

*Image Description: A stacked bar chart titled "EMEA Dwell Time Distribution, 2021-2022" showing the distribution of dwell times in days for each year in the EMEA region.*

Dwell time distribution in EMEA showed that 54% of intrusions investigated by 
Mandiant were identified within 30 days, with 76% of those intrusions (42% of  
total EMEA investigations) identified within a week. Organizations in EMEA showed 
improvement detecting a majority of incidents more quickly. However, the general 
distribution of intrusions remains consistent with 2021 with 23% of intrusions being 
identified after a year of initial intrusion.

*Image Description: A bar chart titled "EMEA Dwell Time Investigation by Type, 2022" showing the median dwell time for all, ransomware, and non-ransomware investigations in the EMEA region.*

*Image Description: A bar chart titled "EMEA Median Dwell Time by Detection Source" showing the median dwell time for ransomware and non-ransomware investigations detected internally and externally in the EMEA region.*

In 2022, Mandiant saw a 10-percentage point decline in EMEA investigations related 
to ransomware. Additionally, Mandiant noted an increase in the median dwell time  
for ransomware specific investigations in EMEA to 33 days in 2022, up from just four 
days in 2021. This means that, in 2022, adversaries leveraging ransomware against 
organizations in EMEA spent 89% longer in compromised environments before being 
detected. However, the median dwell time for ransomware related investigations  
in EMEA in 2021 was exceptionally short, making it unsurprising that this metric 
reverted in 2022. Organizations were notified by an external entity of a ransomware 
event faster than they were able to detect the event internally in 2022. Organizations 
in EMEA were notified by an external entity within 30 days of ransomware related 
intrusions however, when similar intrusions were identified internally, adversaries 
remained undetected for 51 days.

Mandiant did see a significant improvement in non-ransomware dwell time. 
Organizations in EMEA detected non-ransomware intrusions nearly two thirds 
quicker, with the median dwell time at 19 days in 2022 compared to 60 days in 2021.

#### Industry Targeting
*Image Description: A bar chart titled "Global Industries Targeted, 2022" showing the percentage of investigations for each industry.*

Of the intrusions investigated by Mandiant in 2022, response efforts for government 
related organizations captured a quarter of all investigations. Compared to 9%  
in 2021, this primarily reflects the extensive work Mandiant has done in support  
of Ukraine. The next four most targeted industries from 2022 are consistent with  
what Mandiant experts observed in 2021. Mandiant observed business/professional 
services, financial, high tech and healthcare industries to be favored by adversaries. 
These industries remain attractive targets for both financially and espionage 
motivated actors.

#### Targeted Attacks
##### Initial Infection Vector
*Image Description: A pie chart titled "Initial Infection Vector (when identified)" showing the percentage of each initial infection vector.*

Exploits continued to be the most leveraged initial infection vector used by 
adversaries in Mandiant investigations conducted in 2022. In intrusions where  
the initial infection vector was identified, 32% of intrusions began with an exploit. 
While this was a decrease from the 37% of intrusions identified in the reporting 
period of M-Trends 2022, exploits remained a critical tool for adversaries to use 
against their targets.

In 2022, phishing returned to the second most utilized vector for initial infection 
observed in intrusions, representing 22% of intrusions where the initial infection 
vector was identified. This was an increase from 12% of intrusions seen in 2021. 
Phishing continues to be a lucrative and mainstay vector for adversaries year  
over year.

Adversaries leveraged stolen credentials more often in 2022 than 2021 in 
investigations where the initial infection vector was identified, at 14% and 9% 
respectively. Mandiant investigations uncovered an increased prevalence in both  
the use of widespread information stealer malware and credential purchasing in 
2022 when compared to previous years. In many cases, investigations identified  
that credentials were likely stolen outside of the organization’s environment and  
then used against the organization, potentially due to reused passwords or use  
of personal accounts on corporate devices.

*Image Description: A bar chart titled "Most Prevalent Initial Intrusion Vector by Region" showing the most prevalent initial intrusion vector for the Americas, EMEA, and APAC regions.*

Regionally, adversaries made use of various vectors to gain access to targeted 
organizations and complete their missions. In the Americas, in intrusions where 
initial infection vectors were identified, the use of exploits remained the most 
leveraged vector at 38% of investigations. Adversaries targeting organizations in 
APAC used access from a prior compromise to perform their intrusions more often 
than other vectors by more than 10-percentage points. In EMEA, phishing was 
leveraged by adversaries in 40% of investigations where an intrusion vector was 
identified. This variety of vectors used across regions likely indicates that 
adversaries are not leveraging the same attack paths to accomplish their missions. 
Adversaries continue to leverage the intrusion vector that is the most effective  
to gain access to their targets that reside in each region.

##### Adversary Operations
*Image Description: A bar chart titled "Financial Gain, 2020-2022" showing the percentage of intrusions with financial gain and no financial gain over the years.*

Mandiant investigations where an adversary was identified 
seeking financial gain decreased in 2022. However,  
financially motivated intrusions still comprised over  
a quarter of intrusions investigated by Mandiant. Of Mandiant 
investigations in 2022, 26% of intrusions surfaced adversaries 
seeking monetary gain through extortion, ransomware, sold 
access, illicit transfers, or payment card theft.

Compared to the reporting period of M-Trends 2022, 
ransomware related investigations conducted by Mandiant 
decreased by 5-percentage points. In 2022, 18% of all  
Mandiant investigations were related to ransomware.  
This represents the smallest percentage of Mandiant 
investigations related to ransomware since prior to 2020.

*Image Description: A line graph titled "Data Theft Observed, 2020-2022" showing the percentage of intrusions where data theft was observed over the years.*

Mandiant experts identified that in 40% of intrusions in 2022, 
adversaries prioritized data theft. Mandiant defenders have 
observed threat actors attempting to steal, or successfully 
completing data theft operations, more often in 2022 
compared to previous years. In 19% of those intrusions (8%  
of all intrusions) the data stolen was used by the threat actor 
during negotiations for payment. Mandiant continues to 
observe threat actors performing data theft operations  
for numerous goals. However, adversaries were observed 
prioritizing data theft that likely indicates intellectual property 
theft or espionage related end goals in 22% of investigations. 
The continued increase of observed data theft likely indicates 
that organizations are improving their ability to detect data 
theft operations, allowing investigators to conduct more 
complete investigations.

##### Modus Operandi
Mandiant experts continue to see a small uptick in the occurrence of opportunistic 
compromise being leveraged as a source of targeted attack activity. Campaigns  
of broad scale non-targeted activity have, in some cases, translated into targeted 
attack activity as access to compromised environments is sold to targeted threat 
actors or critical information gathered during the attack is leveraged to accomplish 
the goals of targeted attackers.

In 2022, Mandiant experts identified this activity in 6% of intrusions compared to 4% 
in 2021 and 3% in 2020. As the use of exploits continues to rise, it is no surprise that 
use of compromised architecture is also increasing. As proof of concept (POC) code 
is made available for newly identified exploits, the ability to automate compromise 
increases. This shorter cycle from POC to widespread attack allows actors to gain 
quick wins which in turn provide necessary infrastructure for additional non-
targeted attacks.

Of the Mandiant investigations where compromised architecture was observed, 
roughly 60% of the intrusions resulted in some type of crypto-mining activity. In the 
remaining nearly 40% of these intrusions, the architecture was leveraged for 
actions, including ongoing spam and/or phishing operations, as well as to further the 
distribution of botnets. Similar to previous years, intrusions related to insider threats 
made up 1% of Mandiant investigations in 2022.

##### Exploit Activity in 2022
*Image Description: A bar chart titled "Exploit Activity When Identified" showing the percentage of intrusions that involved exploits, and the percentage of those that involved specific CVEs.*

Adversaries are still making use of exploits to conduct their operations. Mandiant 
observed evidence of successful exploit activity of at least one exploit against a 
vulnerability in 36% of investigations in 2022 compared to 30% of investigations 
from 2021. Mandiant continues to observe adversaries leveraging exploits to initiate 
and continue intrusions. Perimeter devices that are accessible via the internet - 
including firewalls, virtualization solutions and virtual private network devices - 
remain a highly sought after target for attackers.

Across all investigations where a vulnerability was targeted, abuse of the Log4j1 
vulnerability represented 16% of investigations. The second and third most notable 
vulnerabilities identified were related to F5 Big-IP2 and VMware Workspace ONE 
Access and Identity Manager3.

##### Multiple Threat Groups Identified
*Image Description: A line graph titled "Multiple Threat Groups" showing the percentage of victim environments with multiple threat groups over the years.*

In more than a quarter of investigations, Mandiant experts identified multiple  
threat groups within the same environment. During these investigations, Mandiant 
observed threat groups working together to accomplish a central goal as well  
as instances where the target environment was enticing to multiple threat actors 
independently. The percentage of investigations where multiple threat actors were 
identified in 2022 increased to a similar percentage that was observed in 2020. This 
trend remains volatile, however Mandiant has observed a general rise in multiple 
threat groups identified in the same environment over the past four years.

#### Threat Groups
*Image Description: A diagram titled "Threat Groups 2022" showing the number of newly tracked and observed threat groups, the number of active APT, FIN, and UNC groups, and the geolocations of these groups.*

Mandiant tracks more than 3500 threat groups, including 900+ 
newly tracked threat groups in this M-Trends reporting period.  
Of the newly tracked groups, 265 threat groups were first 
identified during Mandiant investigations in 2022. Mandiant 
identified a total of 343 unique threat groups across all intrusions 
in 2022. Organizations faced intrusions by four named Advanced 
Persistent Threat (APT) groups. This includes government 
sponsored groups from China and Russia, five named financially 
motivated threat (FIN) groups, and 335 uncategorized threat (UNC) 
groups. Overall, organizations are still facing and responding to 
well-established threat groups while also contending with newly 
attributed groups.

*Image Description: A bar chart titled "Observed Threat Groups by Goal, 2022" showing the percentage of threat groups with financial gain, espionage, other, and unknown goals.*

These threat groups are clusters of cyber activity that include artifacts such as 
adversary infrastructure, tools, and tradecraft. When a threat grouping is first 
created, Mandiant assesses a primary goal for the group. As our knowledge of  
a threat grouping becomes sufficiently mature, in-depth research aids in assigning  
a formal designation based on established Mandiant naming conventions.

Of all threat groups observed in 2022, Mandiant assessed that 48% of these  
threat groups to have financially motivated operations, 18% with espionage related 
motivations and 9% with other motivations like, destructive operations, hacktivism,