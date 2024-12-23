# THE CYBERTHREAT REPORT
## Table of Contents
- [Foreword](#foreword)
- [Preface](#preface)
- [Introduction: The CyberThreat Report: June 2024](#introduction-the-cyberthreat-report-june-2024)
- [Geopolitical Events Impacting the Cyber Domain](#geopolitical-events-impacting-the-cyber-domain)
- [Highlights At-a-Glance](#highlights-at-a-glance)
- [Methodology: How We Gather and Analyze Data](#methodology-how-we-gather-and-analyze-data)
- [Report Analysis, Insights, and Data](#report-analysis-insights-and-data)
- [Nation States and Advanced Persistent Threats (APT)](#nation-states-and-advanced-persistent-threats-apt)
- [Active nation states and APT groups](#active-nation-states-and-apt-groups)
- [APT groups and countries of origin](#apt-groups-and-countries-of-origin)
- [Targeted countries and regions](#targeted-countries-and-regions)
- [Malicious tools](#malicious-tools)
- [Non-malicious tools](#non-malicious-tools)
- [Conclusion](#conclusion)
- [Volt Typhoon: Nation-state APT threats with a focus on China](#volt-typhoon-nation-state-apt-threats-with-a-focus-on-china)
- [Overview](#overview)
- [Operational timeline](#operational-timeline)
- [Tactics, techniques and procedures (TTPs)](#tactics-techniques-and-procedures-ttps)
- [Ransomware Landscape](#ransomware-landscape)
- [Evolution](#evolution)
- [Operation Cronos: Law enforcement action to disrupt LockBit](#operation-cronos-law-enforcement-action-to-disrupt-lockbit)
- [A Global look at ransomware](#a-global-look-at-ransomware)
- [The Emergence of EDR Killer and Evasion Tools](#the-emergence-of-edr-killer-and-evasion-tools)
- [January campaign using Spyboy’s EDR Terminator tool](#january-campaign-using-spyboys-edr-terminator-tool)
- [More EDR killers observed](#more-edr-killers-observed)
- [Email Remains Ripe for Attackers](#email-remains-ripe-for-attackers)
- [Election donation scams](#election-donation-scams)
- [Taxation phishing](#taxation-phishing)
- [The GenAI Arms Race: Findings from the Cybercriminal Underground](#the-genai-arms-race-findings-from-the-cybercriminal-underground)
- [‘ChatGPT in Jabber’ project possibly used by a Russian criminal APT group](#chatgpt-in-jabber-project-possibly-used-by-a-russian-criminal-apt-group)
- [GenAI adoption in InfoStealers](#genai-adoption-in-infostealers)
- [Telegram Pro Poster’ bot project](#telegram-pro-poster-bot-project)
- [Afterword](#afterword)
- [Methodology](#methodology)
- [Application: How to Use This Information](#application-how-to-use-this-information)
- [How to Understand the Analysis in this Report](#how-to-understand-the-analysis-in-this-report)
- [Resources](#resources)
- [About the Trellix Advanced Research Center](#about-the-trellix-advanced-research-center)
- [About Trellix](#about-trellix)

June 2024

Presented by

Insights Gleaned from a Global Network of 
Experts, Sensors, Telemetry, and Intelligence

INSIDE:

Rapid and Significant 
Changes in the APT 
Landscape 

LockBit Shakes 
Up Ransomware 
Ecosystem

Expanding Attacker 
Toolbox

THE CYBERTHREAT REPORT

Authored by Trellix’s Advanced Research Center, this report (1) highlights insights, 
intelligence, and guidance gleaned from multiple sources of critical data on 
cybersecurity threats, and (2) develops expert, rational, and reasonable interpretations 
of this data to inform and enable best practices in cyber defense. This edition focuses 
on data and insights captured primarily between October 1, 2023, and March 31, 2024.

1.  Rapid and Significant Changes in the APT Landscape
2.  LockBit Shakes Up Ransomware Ecosystem
3.  EDR Killers Emerge 
4.  U.S. Presidential Election Themed Scams
5.  GenAI and the Cybercriminal Underground

An EDR evasion tool was just successfully used to shut 
down endpoint detection and response capabilities at 
another organization in your industry. 
 
The cybersecurity race to outpace attackers and stop 
them from using legitimate security tools for bad is 
getting more complicated. 
 
As CISO, you have to move with agility, speed, 
confidence and control. Your CEO and Board are 
waiting to know more about your logging and alert 
tools. You task your team to identify gaps, and you 
have a plan to address them.  
 
The cybersecurity race is a triathlon. You’re competing 
in SecOps, Technology and Intelligence. The race is on, 
and it’s a game of endurance. 
As defense mechanisms become more 
sophisticated, so too do the offensive  
tools and tactics nation-state and cyber 
criminal actors.
The CyberThreat Report, June 2024
2

## Foreword
Operational threat intelligence and the ability to add context for your 
environment to global threats has never been more important to the 
role of the CISO. 
As we’re tasked to do more with less, CISOs and their SecOps teams 
require threat intelligence to anticipate threats, identify and prepare for 
the most relevant threats targeting your organization, align programs 
and budget against the most likely threats and actors, and finally, to 
move from a reactive to proactive posture. 
As “Customer Zero” for Trellix, I have never seen more potential for 
intelligence to shape the way responders move and strategize. 
Take this content, digest it, and put it to use in your strategic planning, 
budget rationalization, board education and operational support.  
I hope this insight is educational, informative and beneficial, and acts as 
a stepping stone to better guide and influence how you plan, prepare, 
and persist against APTs. 
  
	
	                 Harold Rivas  
	
	                 CISO, TRELLIX	 	
	
The CyberThreat Report, June 2024
3
## Preface
With this report, and all of our reports, we aim to provide structure 
around intelligence and context to what we’re observing. 
The landscape
The last six months have been unprecedented - a state of polycrisis 
remains and it has accelerated cybercriminal and threat actor activity 
globally. We’re seeing radical shifts in behavior, including: 
	
- The ransomware ecosystem is a-typical following law  
enforcement action,
	
- Autonomous groups are selling their wares in penetration testing 
and alternative attack methods to ransomware gangs,
	
- Warfare in Israel has triggered direct state-sponsored attacks and 
hacktivism, and 
	
- Threat actors are looking to be more sophisticated, and they have 
access to cheap and free GenAI-based tools that empower them to 
become experts overnight, and 
	
- EDR Evasion and termination tools become more important to 
threat actors.
A cat and mouse game
With larger implementation of endpoint detection and response (EDR) 
solutions, we’re seeing the cat and mouse game of cybersecurity get 
more complex. The increase of threat actors using criminal tools to 
dismantle EDR has piqued our interest and is a sharp course change 
from the use of traditional malware-based tools. 
As defenders, we have to change course, too. EDR has proven effective 
at detecting malware, ransomware and the activity of APT groups, 
but if EDR is taken offline, what’s an organization and their CISO to 
do? You need logging, you need alerting, and you need operational 
threat intelligence to keep from being blind to unusual behavior in your 
system. There’s a new layer of gameplay. 
We work diligently to share threat intelligence with the community - a 
core value of ours to keep ahead of adversaries - and track campaigns 
and threat groups at scale.
The landscape is shifting more than ever. Our aim is to support our 
customers and the industry at large with the intelligence needed to 
sharpen defenses, make countermeasures, and identify gaps. 
In this cat and mouse game, we have to play to win.
  
	
	                 John Fokker  
	
	                 HEAD OF THREAT INTELLIGENCE, TRELLIX 
The CyberThreat Report, June 2024
4
## Introduction: The CyberThreat Report: June 2024
### Geopolitical Events Impacting the Cyber Domain 
Research from the Trellix Advanced Research Center into activity 
from October 1, 2023 - March 31, 2024 has revealed a shift in threat 
activities, with a noticeable increase in geopolitically motivated 
cyber threat operations. Notably, major regional and global events 
– such as military exercises, political or economic summits, political 
conventions, and elections – drove cyber threat activities. 
Trellix analysts assess with moderate confidence that threat actors 
focused on these events to collect relevant intelligence about 
counterparts, probe networks proactively to obtain information for 
situational awareness, or preposition on IT networks strategically for 
future attacks.
	
- Presidents Biden and Xi meet in San Francisco: In November 
2023, Trellix telemetry detection data indicated an uptick in 
malicious activity from China-associated APT actor groups only 
days before the meeting between U.S. President Biden and 
China’s President Xi in San Francisco as part of the Asia-Pacific 
Economic Cooperation (APEC) meeting. The number of threat 
activities decreased significantly following the Biden-Xi summit 
and throughout the APEC summit.  
 
As the APEC summit came to an end, the level of threat activity 
fell to its lowest point in the month of November 2023. This 
pattern of threat activity from China-associated threat actor 
groups likely suggests that China’s state-sponsored threat actor 
groups were heavily influenced by geopolitical events such as 
APEC. It may also indicate that China’s APT groups may have 
deliberately withdrawn their hacking activity during a major 
political event possibly to preserve their public image and 
international reputation. 
	
- Israel-Hamas war: Threats from Iranian-linked APT threat 
actor groups have also been driven by political developments 
surrounding the Israel-Hamas war. In the United States, Trellix 
global telemetry data shows periodic surges of malicious activity 
from Iranian-linked APT threat actor groups in the last six 
months (with the exception of late November and December 
2023). Specifically, our global telemetry shows a reduction in 
threat activity from Iranian-linked APT groups targeting U.S. 
organizations during the periods of Israel hostage exchange and 
ceasefire agreements in late November 2023 and December 
2023, when the U.S. pushed for a humanitarian ceasefire in the 
Gaza Strip as Iran is an open supporter of Hamas. Additionally, 
Trellix global telemetry indicates that Iranian-linked APT threat 
actor groups has employed a variety of TTPs, including phishing, 
information stealer, backdoors, downloader, malicious webshells, 
and commonly exploited vulnerabilities to target organizations in 
Israel during the reporting period. 
The CyberThreat Report, June 2024
5
	
- Military drills: In addition, multinational military exercises to 
enhance combat readiness can trigger increased malicious 
activities. Most recently, in March 2024, Trellix global telemetry 
data shows repeated surges in threat activities in South Korea 
during the U.S.-South Korean large-scale joint military exercises, 
known as Freedom Shield, from March 4 to March 14, 2024. 
These military drills are designed to reflect the “Korea Theater of 
Operations” and counter North Korea’s evolving nuclear threat. 
Specifically, threat detections in South Korea exceeded over 
150,000 detections on March 7 and March 13, 2024, respectively, 
which is around seven times the usual 20,000 daily detections  
in the country. 
	
- Russia-Ukraine war: Continued kinetic warfare in the region 
has been accompanied by cyber initiatives large and small. Most 
notably, Russian-linked actors have been observed leveraging 
new and more advanced wiper malware to wipe thousands of 
virtual servers and PCs by attacking Ukrainian telecom provider 
Kyivstar. The attack to KyivStar is one of the highest-impact 
disruptive cyberattacks on Ukraine since Russia invaded the 
country in 2022.
### Highlights At-a-Glance
While this report serves as a repository for research from across our 
business, key themes persist:
1.  Rapid and Significant Changes in the APT Landscape
    a.  Russia-Linked Sandworm Escalates: As geopolitical tensions 
    rise, so does APT activity across the entire ecosystem. While 
    APT threats grow overall, Russia-linked Sandworm Team was 
    detected 40% more in the period observed in this report. 
    b.  China Remains Prolific: China-linked threat groups 
    remain the most prolific originator of APT activities with 
    Trellix observing more than 21 million detections of threat 
    activities from China-aligned threat actor groups. Over 23% 
    of the detections of malicious activities are directed at the 
    government sector worldwide.
    c.  VoltTyphoon Activity Spikes: As a relatively new China state-
    sponsored APT group, Volt Typhoon stands out because of its 
    unique behavior pattern and targeting practices. Since mid-
    January 2024, Trellix telemetry detected over 7,100 malicious 
    activities associated with Volt Typhoon, with periodic spikes 
    throughout the period from January through March 2024.
The CyberThreat Report, June 2024
6
2.  LockBit Shakes Up Ransomware Ecosystem
    a.  Imposters Impact Gang Reputation: Following a  
    global law enforcement action, Operation Cronos, Trellix 
    observed imposters pretending to be LockBit, all while  
    the group frantically tried to save face and restore the 
    lucrative operation. 
    b.  U.S. Remains Most Targeted: The United States remained 
    the most targeted by ransomware groups, followed by 
    Turkey, Hongkong, India and Brazil.
    c.  Transportation and Shipping Most Hit: Ransomware actors 
    threatened the transportation and shipping sector the most 
    in Q4 2023 and Q1 2024. The sector generated 53% and 45% 
    of global ransomware detections, respectively, and was 
    followed by the finance industry. 
    d.  Law Enforcement Action Leads to Sentencing: Before 
    finalizing this report, global law enforcement disclosed the 
    true identity of LockBit’s ring leader. Further action against 
    ransomware criminals took place on May 1st. The REvil 
    affiliate that attacked Kayesa and many other organizations 
    was sentenced to 13 years in prison and repayment of  
    $16 million USD.
3.  EDR Killers Emerge 
    a.  D0nut Ransomware Gang Appears: The emergence of 
    the D0nut ransomware gang was particularly noteworthy 
    for their innovative use of an EDR killer tool, showcasing 
    an advanced tactic to circumvent endpoint detection and 
    enhance the effectiveness of their attacks.
    b.  Spyboy’s EDR Evasion Tool Used to Target Telecom: A EDR 
    “killer” tool by developer Spyboy called “Terminator” was 
    used in a new campaign in January 2024. The tool is used 
    to circumvent EDR solutions, and 80% of detections were 
    targeted at the telecom sector.  
4.  U.S. Presidential Election Themed Scams
    a.  Phishing Remains Ripe: As the world looks to see the 
    outcome of November’s presidential election in the U.S., 
    scams leveraging election imagery and curated to secure 
    donations have been observed.  
The CyberThreat Report, June 2024
7
5.  GenAI and the Cybercriminal Underground
    a.  Free AI-Powered Tools: Trellix observed a free ChatGPT 
    4.0 Jabber tool available in the cybercriminal underground, 
    which both allows the developer to enable threat actors 
    to adopt GenAI into their operations and to create a GenAI 
    knowledge base to learn from other cyber criminals or even 
    steal their ideas and tools. 
    b.  InfoStealer Adoption Rises: Two InfoStealers with GenAI-
    based features were observed to be used by cybercriminals. 
    MetaStealer and LummaStealer are equipped with GenAI to 
    evade detection and to detect bots among the list of logs, 
    respectively. GenAI capabilities make these criminal tactics 
    harder to find and harder to stop. 
### Methodology: How We Gather and Analyze Data 
Experts from our Trellix Advanced Research Center gather the 
statistics, trends, and insights that comprise this report from a wide 
range of global sources, both captive and open. The aggregated data 
is fed into our Insights and ATLAS platforms. Leveraging machine 
learning, automation, and human acuity, the team cycles through an 
intensive, integrated, and iterative set of processes – normalizing the 
data, analyzing the information, and developing insights meaningful 
to cybersecurity leaders and SecOps teams on the frontlines of 
cybersecurity worldwide. For a more detailed description of our 
methodology, please see the end of this report.
The CyberThreat Report, June 2024
8
## Report Analysis, Insights, and Data 
### Nation States and Advanced Persistent Threats (APT)    
From October 2023 through March 2024, Trellix observed a 17% 
increase in APT-backed detections compared to the previous six 
months. This is notable as our last report identified a staggering 50% 
increase in these detections. The APT ecosystem is fundamentally 
different from a year ago – more aggressive, cunning and active. 
In the rapidly evolving cyber threat landscape, Advanced Persistent 
Threat (APT) groups continue to pose a significant and sophisticated 
challenge to global cybersecurity.
We aim to thoroughly analyze activities associated with Advanced 
Persistent Threats (APT) detected from Q4 2023 through Q1 2024. 
This analysis focuses on the origins of these threats, their main 
targets, and the tools used in their operations. We compare these 
findings to data from the first half of 2023 (Q2 to Q3) using two key 
metrics: percentage variance and proportional contribution variance.
	
- Percentage variance: This metric helps us see if the activity of a 
specific APT group, the targeting of certain countries, or the use 
of particular tools has gone up, gone down, or stayed the same 
over time. Understanding this helps us track how the behaviors of 
these threat actors change and how the overall landscape of cyber 
threats is evolving.
	
- Proportional contribution variance: This metric adds context by 
not just showing the raw change in activity, but how this change 
stands against the backdrop of the entire cybersecurity threat 
environment. For example, even if detections of a particular actor 
have increased significantly, this might still represent a small part of 
the total cyber threats if the overall threat environment has become 
much busier. Conversely, if their detections have decreased, but the 
rest of the threat environment has slowed down even more, this 
actor could be becoming relatively more significant.
By employing these metrics, we aim to provide a nuanced 
understanding of the shifts in APT activities, enabling us to draw 
insights into their strategic objectives, preferred methodologies, 
and the cybersecurity challenges they pose. The following sections 
delve into these findings, shedding light on the intricate world of 
APTs and the continuous efforts required to safeguard against their 
sophisticated threats.
The CyberThreat Report, June 2024
9
### Active nation states and APT groups
Further, the period spanning from October 2023 - March 2024 
witnessed significant fluctuations in the activities of various APT 
groups. These fluctuations not only underscore the dynamic nature 
of cyber threats but also highlight shifts in the operational focus and 
techniques employed by these sophisticated actors.

![Image: TOP 10 APTS BASED ON DETECTIONS BETWEEN THE LAST QUARTER OF 2023 AND THE FIRST QUARTER OF 2024]

CHANGES IN CYBER THREAT  GROUP ACTIVITY: 
VARIANCE AND PROPORTIONAL CONTRIBUTION

| Advanced Persistent Threats | Percentage Variance | Proportional Contribution Variance |
| ----------- | ----------- | ----------- |
| Sandworm Team | 1669.43% | 40.34% |
| Mustang Panda | -2.19% | -6.14% |
| Lazarus | 66.87% | 0.07% |
| APT28 | 18.67% | -1.49% |
| Turla | 2.95% | -1.74% |
| Covellite | 85.30% | 0.23% |
| APT29 | 123.98% | 0.53% |
| APT10 | 80.46% | 0.17% |
| UNC4698 | 368.75% | 1.14% |
| APT34 | 96.73% | 0.23% |
| Other | -28.99% | -33.33% |

The CyberThreat Report, June 2024
10
	
- Shift in tactics: Sandworm Team, historically known for its 
disruptive cyber operations, has seen a staggering increase in 
detections by 1669%, with a proportional contribution variance 
of 40%. This monumental rise suggests an unprecedented 
escalation in their cyber activities from the Russia-linked group.
	
- Aggressive expansion of operations: APT29, a group with 
a history of extensive cyber espionage, showed a significant 
uptick in activity, with detections increasing by 124%. Similarly, 
APT34 and Covellite also demonstrated substantial increases in 
detections, by 97% and 85% respectively, indicating heightened 
operational tempos or the initiation of new campaigns.
	
- Homeostasis: In contrast, groups like Mustang Panda, Turla, and 
APT28 saw minimal changes in their activity levels, with Mustang 
Panda showing a slight decrease of -2% and Turla a modest 
increase of 3% in detections. 
	
- New actors emerge: Noteworthy is the emergence of UNC4698, 
which saw a 363% increase in detections, suggesting the rise of a 
potentially significant new player in the APT landscape.
#### WHAT DO WE KNOW ABOUT UNC4698?
Not a lot is known about this group, but researchers have been 
able to recognize their behavior as group activity and don’t know 
yet how to attribute it.
Having said that, what is known about UNC4698 is that its focus 
is on industrial espionage, gathering sensitive operational data 
which could be used to support economic or national security 
objectives of the sponsoring state, presumably linked to China 
due to the nature and regional focus of the attacks.
Its usual targets are oil and gas organizations in Asia.
They are also known to employ a specific malware that goes by 
the name of ‘SNOWYDRIVE’.
UNC4698 employs a variety of tactics, techniques, and 
procedures (TTPs) centered around the use of malware delivered 
via USB flash drives. Here are some key TTPs associated with this 
threat actor:
	
- Initial Access via Infected USB Devices: The primary 
method of infection involves USB drives that contain 
malicious software designed to create a backdoor on the 
host system.
The CyberThreat Report, June 2024
11
	
- Execution through Malicious Files: The malware typically 
includes a dropper that writes malicious executables and 
DLLs to disk. These files often masquerade as legitimate 
software to avoid detection and are executed to establish 
further control.
	
- Persistence and Registry Modification: UNC4698 
ensures persistence on the infected systems by modifying 
the Windows registry. This allows the malware to start 
automatically whenever the system boots up.
	
- Command and Control (C2) Communication: The malware 
sets up a method for remote communication, allowing the 
attackers to issue commands and control the compromised 
systems from afar.
	
- Lateral Movement via Removable Media: The malware  
can copy itself to other USB devices connected to the 
infected machine, which helps in spreading the infection  
to other systems.
Lesser-known or unidentified groups, saw a 62% increase in 
detections, indicating a diverse and growing array of threats beyond 
the well-documented APT entities. This increase of 8% in their 
proportional contribution to the total detections highlights the 
constant evolution and diversification of cyber threats. 
### APT groups and countries of origin
WHAT DO WE KNOW ABOUT UNC4698? 

![Image: TOP 10 APT ASSOCIATED COUNTRIES BASED ON DETECTIONS CORRELATED TO CAMPAIGNS, BETWEEN THE LAST QUARTER OF 2023 AND THE FIRST QUARTER OF 2024]

The CyberThreat Report, June 2024
12
When looking at countries of origin, 
Trellix telemetry from October 2023 
through March 2024 also observed 
notable shifts in the landscape  
of state-sponsored cyber activities.  
	
- Substantial escalation in 
operations: Geopolitical 
motivations and cybersecurity capabilities are evolving across 
different nations. Our telemetry observed the following: 
    a.  Russia-linked threat groups have shown a significant 
    increase in APT detections, up by 31%, with its proportional 
    contribution rising by 4%. This indicates a substantial 
    escalation in cyber operations, possibly reflecting  
    broader strategic objectives or responses to global 
    cybersecurity dynamics.
    b.  Iran-linked threat groups  have also markedly ramped up 
    cyber activities, with an 8% increase in detections and a 
    3.89% rise in proportional contribution. This highlights a 
    significant expansion in Iran’s cyber operations, in line with its 
    geopolitical aims and involvement in the Israeli-Hamas war.
	
- Broader diversification: China remains the most prolific 
originator of APT activities, with detections slightly increasing 
by 1%. However, its proportional contribution to the overall 
detections has seen a slight decrease of -1%, which might 
suggest a broader diversification of APT origins during this 
period. February of this year also saw reports of significant efforts 
from China-backed APT Volt Typhoon targeting U.S. critical 
infrastructure; more on this in the following section. 
	
- Shift in strategy: Conversely, groups linked to North Korea, 
Vietnam, and India have seen dramatic decreases in their 
APT activities, with North Korea-linked detections dropping 
by -82%, Vietnam by -80%, and India by -82%. The significant 
downturn in North Korea’s proportional contribution (-6%) is 
particularly notable, possibly indicating a shift in focus, strategy, 
or capabilities.
	
- More countries emerging: Pakistan-linked and Belarus-linked 
groups have seen considerable increases in their APT activities, 
with detections up by 55% and an astonishing 2019%, respectively. 
These increases, particularly the exponential rise associated 
with Belarus, underscore the emergence of new or previously 
underrecognized actors in the APT arena. 
 
The category of “Other” shows a 121% increase in detections, 
indicating that APT activities are not limited to the most 
frequently cited countries. This diversity highlights the global 
nature of cyber threats and the necessity for a wide-ranging and 
adaptive cybersecurity posture. 
We will be tracking these new patterns closely in the months ahead. 
The CyberThreat Report, June 2024
13
China-linked threat groups 
remain the most prolific 
originator of APT activities
The Trellix Advanced Research Center 
assesses with a moderate level  
of confidence that the following factors 
impacted activity detected in certain 
countries and regions
Operational objectives:  
Detections in threats targeting Turkey 
increased by a staggering 1458%, translating to a 16% rise in its 
proportional contribution to the total detections. This remarkable 
increase indicates a significant shift in cyber threat focus towards 
Turkey, possibly reflecting broader geopolitical tensions or specific 
operational objectives of the APT groups. 
	
- Strategic importance: India and Italy have also experienced 
considerable increases in detections, with detections up by 614% 
and 308%, respectively. These countries’ rising prominence in the 
list of targets may point to their growing strategic importance 
in the cyber domain, whether due to economic, political, or 
technological factors
Trigona
### Targeted Countries and Regions  
This section focuses on the countries regions where Trellix detected 
APT related activity by APT groups from Q4 of 2023 through Q1 of 
2024, revealing significant shifts in focus and strategy among these 
sophisticated cyber actors. 

![Image: TARGETED COUNTRIES AND REGIONS WITH APT ASSOCIATED DETECTIONS]

The data underscores the global nature 
of cyber threats and the varying levels  
of attention different nations receive 
from APT groups.
The CyberThreat Report, June 2024
14
Turkey has seen an 
unprecedented surge in  
APT-related detections
	
- Broadening landscape: Interestingly, Vietnam and the United 
States, while still generating significant APT detections, have 
shown different trends. Vietnam’s detections increased by 9%, 
yet its proportional contribution decreased by -9%, indicating a 
broadening of the targeting landscape. The United States saw 
a moderate increase of 15% in detections but experienced a -7% 
drop in its proportional contribution, suggesting a diversification 
in the targeting strategies of APT groups.
	
- Geopolitical developments: Germany, China, Papua New Guinea, 
and Brazil have all seen increases in detections, with Germany 
and China witnessing significant proportional contribution 
changes. This diversification in targeting reflects the strategic 
and opportunistic adjustments APT groups make in response to 
global cybersecurity postures and geopolitical developments.
	
- Enhancement of national security: Conversely, Indonesia 
experienced a notable decrease in detections by -48%, coupled 
with a -4% drop in its proportional contribution. This reduction 
might suggest a temporary deprioritization or a successful 
enhancement of national cybersecurity measures.
	
- Consolidation of focus: The “Other” category, representing a 
collective of various other countries where Trellix detected APT 
related activity, saw a -23% decrease in detections and a -21% 
decline in proportional contribution. This decrease highlights a 
possible consolidation of focus by APT groups on specific high-
interest targets during this period.
We see potential for the landscape to continue changing rapidly due 
to geopolitical trends. 
### Malicious tools  
![Image: TOP 10 MALICIOUS TOOLS DETECTED BETWEEN THE LAST QUARTER OF 2023 AND THE FIRST QUARTER OF 2024]

The CyberThreat Report, June 2024
15
The analysis of malicious tools used in APT campaigns from Q4 2023 
to Q1 2024 reveals notable trends in the preferences and operational 
tactics of cyber threat actors. The variance in detection rates and their 
proportional contributions provides insights into the evolving cyber 
threat landscape and the shifting dynamics of tool usage among 
these sophisticated groups.
The following trends were observed: 
	
- Offensive tools getting stronger: Cobalt Strike remains a tool 
of choice for many Threat groups, despite a 17% decrease in 
detections. Its relatively small decrease in proportional contribution 
variance (+1%) suggests it retains its popularity and effectiveness in 
cyber operations, underlining the challenge of defending against 
versatile and widely used offensive tools.
	
- Reliance on web shells, PowerShell and Remote Access attacks: 
China Chopper, PowerSploit, and Gh0st RAT also saw significant 
decreases in detections, by 23%, 24%, and 24%, respectively. Despite 
these decreases, their slight changes in proportional contribution 
variance indicate they remain integral to the toolkit of a threat 
actor. These tools, known for their capabilities in web shell attacks, 
PowerShell exploits, and remote access, highlight the continued 
reliance on proven, versatile tools for cyber operations.
	
- Less detectable tools: Empire, Derusbi, BADFLICK, JJdoor/
Transporter, JumpKick, and MURKYTOP experienced similar 
downward trends in detections, all exceeding a 25% decrease. 
This uniform decline could reflect a broader shift in the tools 
preferred by threat groups or an adaptation to countermeasures 
and detection techniques, prompting a move towards newer, less 
detectable tools.
	
- Constant innovation: The category of “other” malicious tools saw a 
significant increase in detections, up by 30%, and a notable increase 
in its proportional contribution variance by 6.00%. This increase 
underscores the constant innovation and adaptation among threat 
actors, as they explore new tools and techniques to evade detection 
and achieve their objectives.
The evolving preferences in malicious tool usage signify  
the adaptive nature of cyber threat actors in response to  
cybersecurity developments. 
The shift towards a broader range of tools, as indicated by the increase 
in “Other” detections, highlights the necessity for continuous research, 
threat intelligence, and adaptive defense strategies to mitigate the risk 
posed by these evolving cyber threats.
As defense mechanisms become more 
sophisticated, so too do the offensive tools 
and tactics of APT groups.
The CyberThreat Report, June 2024
16
### Non-malicious tools
The use of non-malicious tools in cyber operations by APT groups 
from Q4 2023 to Q1 2024 highlights an important aspect of modern 
cyber threats: the leveraging of legitimate system tools for malicious 
purposes. This practice, known as “living off the land,” complicates 
detection efforts and underscores the sophistication of these threat 
actors. The statistics reveal significant variances in the usage of these 
tools, reflecting their strategic importance in cyber operations
	
- Versatility: PowerShell has seen a dramatic increase in 
detections, up by 105%, with a proportional contribution 
variance of 1%. This surge underscores its versatility and power 
in automating a wide range of malicious activities, from 
reconnaissance to payload delivery.
	
- Focus on network manipulation: Netsh and IPRoyal Pawns have 
both seen significant increases in detections, by 99% and 102%, 
respectively. These tools are often used for network configuration 
and proxy traffic, indicating a strategic focus on