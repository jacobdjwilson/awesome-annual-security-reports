# 2025 Cyber Threat Intelligence Report

## Table of Contents
- [Foreword](#foreword)
- [Executive Summary](#executive-summary)
  - [Malicious Infrastructure](#malicious-infrastructure)
  - [Information Stealers](#information-stealers)
  - [Research](#research)
  - [The Scope of Our Research](#the-scope-of-our-research)
- [Adversary Infrastructure Tracking](#adversary-infrastructure-tracking)
  - [Overview of Dedicated Malicious Infrastructure](#overview-of-dedicated-malicious-infrastructure)
  - [Top 10 Tracked Threats](#top-10-tracked-threats)
  - [Global Hosting Distribution](#global-hosting-distribution)
    - [United States](#united-states)
    - [China](#china)
    - [Hong Kong](#hong-kong)
  - [Offensive Security Tooling (OSTs)](#offensive-security-tooling-osts)
    - [Cobalt Strike](#cobalt-strike)
    - [Increased Adoption of Sliver and Brute Ratel](#increased-adoption-of-sliver-and-brute-ratel)
    - [Supershell](#supershell)
  - [Information Stealers](#information-stealers-1)
    - [Lumma Stealer](#lumma-stealer)
    - [Rise of Meduza Stealer](#rise-of-meduza-stealer)
    - [Redline Stealer Resists Law Enforcement](#redline-stealer-resists-law-enforcement)
  - [RATs](#rats)
    - [Gh0stRAT](#gh0strat)
    - [Quasar & Async RAT](#quasar--async-rat)
  - [CNI SOC/ MDR Service Detection Analysis](#cni-soc-mdr-service-detection-analysis)
    - [Top Five Alerts](#top-five-alerts)
    - [C2 Alert Geolocations](#c2-alert-geolocations)
    - [Top C2 Alert Categories](#top-c2-alert-categories)
    - [Top C2 Alert Countries](#top-c2-alert-countries)
- [Information Stealer Landscape](#information-stealer-landscape)
  - [Global Information Stealer Landscape](#global-information-stealer-landscape)
    - [Rising Trends in Information Stealer Compromises](#rising-trends-in-information-stealer-compromises)
  - [UK Information Stealer Landscape](#uk-information-stealer-landscape)
    - [Understanding the Threat to UK Organisations](#understanding-the-threat-to-uk-organisations)
    - [Dominance of Lumma Stealer and Redline Stealer in UK-Based Attacks](#dominance-of-lumma-stealer-and-redline-stealer-in-uk-based-attacks)
    - [The Continued Threat of StealC and Emerging Variants](#the-continued-threat-of-stealc-and-emerging-variants)
  - [Information Stealers and RaaS Ecosystem](#information-stealers-and-raas-ecosystem)
    - [Ransomware Incidents Involving Information Stealers (2024)](#ransomware-incidents-involving-information-stealers-2024)
    - [Usage of Information Stealers Across Incidents (2024)](#usage-of-information-stealers-across-incidents-2024)
    - [Information Stealers Used Across Ransomware Incidents (2024)](#information-stealers-used-across-ransomware-incidents-2024)
    - [Information Stealer Key Takeaways](#information-stealer-key-takeaways)
- [Research](#research-1)
  - [Phishing Kits and Techniques](#phishing-kits-and-techniques)
    - [Introduction](#introduction)
    - [ClickFix](#clickfix)
    - [Notable Events in ClickFix Variants](#notable-events-in-clickfix-variants)
    - [Notable Threat Actors using ClickFix](#notable-threat-actors-using-clickfix)
  - [EDRKillers, and EDRKillShifter](#edrkillers-and-edrkillshifter)
    - [Introduction](#introduction-1)
    - [Adoption](#adoption)
    - [EDRKillShifter](#edrkillshifter)
    - [Technical Analysis](#technical-analysis)
    - [Key Takeaways](#key-takeaways)
  - [Rising Prospect: Fog Ransomware](#rising-prospect-fog-ransomware)
    - [Introduction](#introduction-2)
    - [Targeting and Broad TTPs](#targeting-and-broad-ttps)
    - [A Noteworthy Tactical Shift](#a-noteworthy-tactical-shift)
    - [Noteworthy Technical Observation: Technique Doppelgänger](#noteworthy-technical-observation-technique-doppelganger)
    - [Key Takeaways](#key-takeaways-1)
- [Outlook for 2025](#outlook-for-2025)
  - [Edge Devices and Vulnerability Exploitation](#edge-devices-and-vulnerability-exploitation)
  - [Operational Relay Box (ORB) Networks](#operational-relay-box-orb-networks)
  - [Cybercrime and Ransomware Ecosystem](#cybercrime-and-ransomware-ecosystem)
  - [Cryptocurrency Theft](#cryptocurrency-theft)
  - [Generative AI](#generative-ai)
  - [Geopolitical Events](#geopolitical-events)
  - [Cloud Native Attacks](#cloud-native-attacks)
  - [RMM Tools](#rmm-tools)
- [About Bridewell Threat Intelligence](#about-bridewell-threat-intelligence)

Bridewell Threat Intelligence

# 2025 Cyber Threat
Intelligence Report

1

2025 Cyber Threat Intelligence Report

Contents

Foreword
Executive Summary
  Malicious Infrastructure
  Information Stealers
  Research
  The Scope of Our Research
Adversary Infrastructure Tracking
  Overview of Dedicated Malicious Infrastructure
  Top 10 Tracked Threats
  Global Hosting Distribution
    United States
    China
    Hong Kong
Offensive Security Tooling (OSTs)
  Cobalt Strike
  Increased Adoption of Sliver and Brute Ratel
  Supershell
Information Stealers
  Lumma Stealer
  Rise of Meduza Stealer
  Redline Resists Law Enforcement
RATs
  Gh0stRAT
  Quasar & Async RAT
CNI SOC/ MDR Service Detection Analysis
  Top Five Alerts
  C2 Alert Geolocations
  Top C2 Alert Categories
  Top C2 Alert Countries

2
4
4
4
4
5
6
6
6
8
8
8
8
9
10
11
14
15
16
18
20
21
23
24
26
25
27
28
28

Information Stealer Landscape
  Global Information Stealer Landscape
  Rising Trends in Information Stealer
  Compromises
UK Information Stealer Landscape
  Understanding the Threat to UK Organisations
  Dominance of Lumma Stealer and Redline in
  UK-Based Attacks
  The Continued Threat of StealC and
  Emerging Variants
Information Stealers and RaaS Ecosystem
  Ransomware Incidents Involving Information
  Stealers (2024)
  Usage of Information Stealers Across
  Incidents (2024)
  Information Stealers Used Across Ransomware
  Incidents (2024)
  Information Stealer Key Takeaways
Research
  Phishing Kits and Techniques
    Introduction
    ClickFix
    Notable Events in ClickFix Variants
    Notable Threat Actors using ClickFix
  EDRKillers, and EDRKillShifter
    Introduction
    Adoption
    EDRKillShifter
    Technical Analysis

29
29

29
31
31

31

32
33

34

36

37
37
38
38
38
39
42
44
45
45
45
46
46

    Key Takeaways
  Rising Prospect: Fog Ransomware
    Introduction
    Targeting and Broad TTPs
    A Noteworthy Tactical Shift
    Noteworthy Technical Observation:
    Technique Doppelgänger
    Key Takeaways
Outlook for 2025
  Edge Devices and Vulnerability Exploitation
  Operational Relay Box (ORB) Networks
  Cybercrime and Ransomware Ecosystem
  Cryptocurrency Theft
  Generative AI
  Geopolitical Events
  Cloud Native Attacks
  RMM Tools

46
47
47
47
48

48
48
49
49
50
51
53
54
55
56
57

2025 Cyber Threat Intelligence Report

2

2025 Cyber Threat Intelligence Report

# Foreword

“Our CTI Annual Report for 2025 shares insights from
our malicious infrastructure tracking program, and
intelligence gathered by our Security Operations Centre
(SOC) and Managed Detection & Response (MDR)
services. This report also spotlights the information
stealer ecosystem, and presents significant and emerging
threats in our research section.

Our goal with this report is to share security insights and
defensive recommendations that you can leverage to
improve your defence and make your organisation(s) more
resilient against cyber attacks. While monitoring persistent
threat actors to stay ahead of the emerging threat
landscape is challenging, being able to mitigate the threat
posed by adversarial infrastructure should play a key part
in your defensive security strategy.”

Overall, 2025 has continued to mirror some of the trends
seen in 2024. Based on activity we have observed as
part of our malicious infrastructure tracking and through
wider industry reporting, we have moderate confidence
that threat actors will continue to innovate and improve
capabilities to evade defences. A brief summary of these
trends can be found in the executive summary, with more
detailed information available later on in the report.

Gavin Knapp

Cyber Threat Intelligence Principal Lead

Threat actors will
continue to innovate
and improve
capabilities to
evade defences.

By Joshua Penny, Senior Cyber Threat Intelligence Analyst; Tom Igoe, Senior Cyber Threat Intelligence Analyst

Gavin Knapp, Cyber Threat Intelligence Principal Lead; Craig Smith, Senior CTI Analyst

2025 Cyber Threat Intelligence Report

3

# Executive Summary

In 2024, our CTI team made significant improvements
to our malicious infrastructure tracking capability. This
included tracking 10% more threat groups than in the
previous year.

## Malicious Infrastructure
The 2024 analysis of our malicious infrastructure tracking
capability revealed notable new activity, themes and
trends, including:
- 40% of all tracked malicious infrastructure is hosted
  within the United States (US) or China, a drop of 8%
  from 2023.
- A notable increase in Sliver and Brute Ratel command-
  and-control (C2) infrastructure, compared to a decrease
  in Cobalt Strike during 2024.
- Malware and tools closely linked to Chinese-nexus
  groups, such as ShadowPad, PlugX, Supershell, and even
  Cobalt Strike dominate the top 10 tracked threats.
- Lumma Stealer, Redline Stealer, StealC and Meduza

Stealer are the preferred information stealers of 2024,
with Lumma Stealer leading the way.

- Information stealers remain a primary initial access
  mechanism for emerging and trending ransomware
  groups such as Akira, RansomHub and Hellcat.
- Chang Way hosting is responsible for a quarter of all
  Redline Stealer servers, following law enforcement action
  in October 2024.
- AsyncRAT and QuasarRAT are amongst the most popular
   Remote Access Trojans (RATs) used used in 2024 after

Gh0stRAT.

## Information Stealers
In the information stealer landscape, major insights included:
- Law enforcement operations contributed to a drop

in the volume of global compromises. The volume of
compromises still managed to peak in holiday seasons,
however, especially in August and December 2024.
- Lumma Stealer, Redline Stealer and StealC are the
primary information stealers impacting the UK.

- In UK CNI, Racoon Stealer and StealC were the dominant
  force in ransomware intrusions that utilised information
  stealers.

## EDRKillers
- Endpoint Detection and Response Killers (EDRKillers)
  surged across ransomware groups, with EDRKillShifter
  fuelling Ransomhub’s rise as a market leader.
  - This year, we have seen wider adoption of dedicated
    sophisticated EDRKillers such as AVNeutralizer (AuKill),
    EDRKillShifter, EDRSandBlast, EDRSilencer, MS4Killer,
    and Disabler.
  - Bring-Your-Own-Vulnerable-Driver (BYOVD) is
    becoming a trending technique used by EDRKillers in
    global ransomware operations.

## Research
From a research perspective, our thematic topics include:

### Fog Ransomware
- The emergence of Fog ransomware is notable for its

### Phishing Kits
- Phishing Kits, and evolving threats such as ClickFix, are
techniques shaping a new way of deploying malicious
code via social engineering tactics.

  - Multiple diverse variants of ClickFix were seen over
    2024 with clever innovations being used and copied
    by other groups.
  - Exclusive to cyber crime between Q1 - Q3 2024,
    ClickFix exploitation expanded in Q4 when nation-state
    groups began incorporating the technique into their
    attack chains.
  - ClickFix experienced a large spike in campaigns at

  the end of 2024 and moving into 2025, a trend that
  demonstrates a developing threat.

significant overlap in Tactics, Techniques, and Procedures
(TTPs) with Akira ransomware, a prominent threat
that consistently ranked among the top 5 ransomware
intrusions throughout 2024. Geographically, 50% of Fog
Ransomware attacks targeted the US, with Germany being
the second-most frequent target at ~10%.

Finally, in Outlooks and Closing Remarks, we discuss
emerging trends. These include: edge devices and
vulnerability exploitation; operational relay box (ORB)
networks; the cyber crime and ransomware ecosystems;
cryptocurrency theft; generative artificial intelligence
(genAI); geopolitical events; the Democratic People’s
Republic of Korea’s (DPRK) exploitation of deceptive
employment tactics; cloud native attacks; and remote
management (RMM) tools.

4

2025 Cyber Threat Intelligence Report

## The Scope of Our Research

It is important to understand that we leverage a
specific set of open source and commercial tools
which do not give us full coverage of host and network
telemetry globally. Threat actors are also becoming
more adept at obfuscating their C2 infrastructure
which continues to present challenges in detecting
malicious infrastructure with strong operational
security.

In addition to this, our security operations are primarily
focused on the UK, US, and EU. As a result, the public
and private intrusion data we have access to is not
representative of all regions globally. There is also a
heavy slant towards UK critical national infrastructure
which is our primary area of focus.

Threat actors are also
becoming more adept
at obfuscating their C2
infrastructure which
continues to present
challenges.

2025 Cyber Threat Intelligence Report

5

# Adversary Infrastructure Tracking

Our adversary infrastructure program tracks threat
groups in the PRE-ATT&CK stage leveraging various
sources of telemetry to identify traffic from: Command-
and-Control (C2) servers, botnets, RATs, initial access
brokers (IABs), APTs, phishing, ransomware groups,
open directories, TDS and ORB networks.

Gathering proactive indicators of attack (IOAs) allows us
to hunt for those indicators on our clients’ networks and
alert our SOC/ MDR service.

## Overview of Dedicated Malicious
Infrastructure

In 2024, Bridewell CTI tracked over 28,000 servers
used by financially motivated threat actors and nation-
state groups associated with malware C2 servers,
phishing, payload hosting, threat actor controlled
infrastructure and Offensive Security Tooling (OSTs).

This section will cover a summary of our adversary
infrastructure tracking capability by infrastructure
geolocation, infrastructure hosting providers, top 10
tracked threats, OSTs, information stealers, and RATs.

## Top 10 Tracked Threats

The top 10 tracked threats list for 2024 saw the removal
of two major malware families: Qakbot and Raccoon
Stealer. This was the direct result of law enforcement
action and only small numbers of servers now remain
active. New to the top 10 are Panda C2 and Brute Ratel as
post-exploitation frameworks, and PlugX and ShadowPad,
two well-known malware families linked to Chinese-nexus
groups.

![Unique IPs Returned by Family]

Unique IPs Returned by Family

7k

6k

5k

4k

3k

2k

1k

0k

Cobalt Strike

Sliver

Metasploit

Burp

PlugX

SuperShell
C2

Havoc

Panda C2

Brute Ratel

ShadowPad

C2 Severs and OST

6

2025 Cyber Threat Intelligence Report

The top 10 threats in 2024 primarily consisted of
C2 frameworks, post-exploitation tools, penetration
testing utilities, and RATs that have been co-opted by
cyber criminals for malicious purposes. Cobalt Strike,
Sliver, Brute Ratel, and Panda C2 are widely used
C2 frameworks that facilitate remote control, lateral
movement, and persistence in compromised networks.
Metasploit and Burp Suite, originally designed for
security testing, are being exploited to help attackers
gain unauthorised access. PlugX and Supershell are RATs
typically linked to espionage campaigns, offering covert
access and data exfiltration capabilities.

There are some other notable observations in 2024’s
top 10. Whilst Cobalt Strike servers topped 6000
in 2024, this still marks a drop from approximately
8000 servers from last year’s report. Coupled with
this decrease in numbers is the marked increase in
C2 servers associated with Sliver and Brute Ratel
infrastructure, suggesting a move away from Cobalt
Strike amongst some threat actors.

However, the increase in Brute Ratel was most
pronounced in the mid-latter quarter. Supershell servers
continued to increase in numbers, peaking in May
2024 and remaining relatively high compared to 2023.
Metasploit and Burp Suite are likely to remain in the top
10 in upcoming years due to their extensive use amongst
pentest teams and criminals alike. This is due to their
flexibility and extensibility which enables multiple use
cases against targets.

![Unique IPs by Query Name by Month]

Unique IPs by Query Name by Month

2,000

1,500

1,000

500

0k

2024
January

2024
February

2024
March

2024
April

2024
May

2024
June

2024
July

2024
August

2024
September

2024
October

2024
November

2024
December

Brute Ratel

Cobalt Strike

Hak 5 C2

Havoc

Metasploit

Meterpreter

Mythic C2

Panda C2

Sliver

Supershell C2

7

2025 Cyber Threat Intelligence Report

When observing geographical hosting, malware and
tools closely linked to Chinese-nexus groups, such
as ShadowPad, PlugX, Supershell, and Cobalt Strike
dominated the top 10 tracked threats. This highlights
the scale and volume of possible infrastructure linked
to Chinese-affiliated threat actors.

## Global Hosting Distribution

In 2024, nearly 24% of all infrastructure we tracked was
hosted in the United States. China hosted nearly 18%.
The remaining countries were the same as in 2023, with
Hong Kong, the Netherlands, and Germany rounding
out our top five. The percentage shares for total
infrastructure remained fairly consistent throughout the
year with little deviation. This was to be expected given
the role of hosting giants such as Amazon and Ali Baba.

Compared to 2023, we observed almost identical
numbers of malicious infrastructure hosted within the
US, on the same top ASNs, along with identical ASNs
in China and Hong Kong. China saw a 6% reduction in
malicious infrastructure hosting compared to 2023,
which subsequently led to an increase in malicious
infrastructure hosted in countries like the Netherlands
and Germany.

### United States
The top 3 hosting providers were Amazon (AS14618,
AS16509), Digital Ocean (AS14061) and COLOCROSSING
(AS36352), which equated to 39% of 379 ASNs in the US,
9% of the total malicious infrastructure distribution during
2024.

### China
The top 3 hosting providers were TENCENT (AS45090),
ALIBABA (AS37963) and HWCSNET Huawei Cloud
Service (AS55990), equating to 84% of 101 ASNs tracked
in China, 14.74% of the total malicious infrastructure
distribution during 2024.

### Hong Kong
The top 3 hosting providers were ALIBABA (AS45102),
HWACENT-AS-AP (AS139471) and MYCLOUD-AS-AP
LUOGELANG FRANCE LIMITED (AS135097), equating
to 29% of 143 ASNs tracked in Hong Kong, 8.88% of the
total malicious infrastructure distribution during 2024.

| Year | Country           | Jan     | Feb     | March   | April   | May     | Jun     | Jul     | Aug     | Sep     | Oct     | Nov     | Dec     | Total   | Total   |
|------|-------------------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| 2024 | United States     | 23.89%  | 23.09%  | 23.04%  | 23.26%  | 21.68%  | 20.57%  | 21.72%  | 23.15%  | 22.68%  | 23.21%  | 22.52%  | 23.65%  | 23.63%  | 23.63%  |
|      | China             | 13.09%  | 12.75%  | 14.75%  | 16.62%  | 17.75%  | 17.74%  | 18.21%  | 18.24%  | 18.13%  | 18.46%  | 19.16%  | 19.74%  | 17.57%  | 17.57%  |
|      | Hong Kong         | 9.06%   | 9.59%   | 9.98%   | 11.32%  | 12.97%  | 13.31%  | 11.00%  | 7.46%   | 7.78%   | 7.69%   | 7.68%   | 7.22%   | 8.88%   | 8.88%   |
|      | Netherlands       | 7.28%   | 7.65%   | 7.05%   | 6.53%   | 6.17%   | 6.49%   | 7.27%   | 8.81%   | 8.69%   | 8.47%   | 8.54%   | 8.88%   | 8.40%   | 8.40%   |
|      | Germany           | 8.80%   | 8.51%   | 7.91%   | 7.20%   | 6.91%   | 7.06%   | 7.15%   | 8.29%   | 8.77%   | 8.80%   | 8.51%   | 7.75%   | 7.52%   | 7.52%   |
|      | Russian Federation| 6.20%   | 6.06%   | 5.59%   | 4.69%   | 4.37%   | 4.37%   | 3.85%   | 3.69%   | 3.23%   | 3.41%   | 2.98%   | 2.94%   | 4.51%   | 4.51%   |
|      | Singapore         | 3.29%   | 3.76%   | 3.77%   | 3.78%   | 3.76%   | 4.08%   | 4.06%   | 3.95%   | 3.71%   | 3.64%   | 3.77%   | 3.86%   | 3.54%   | 3.54%   |
|      | United Kingdom    | 3.18%   | 3.10%   | 2.83%   | 2.64%   | 2.81%   | 3.01%   | 3.31%   | 3.45%   | 3.35%   | 3.41%   | 3.10%   | 2.73%   | 2.73%   | 2.73%   |
|      | France            | 3.65%   | 3.70%   | 3.27%   | 3.09%   | 3.00%   | 2.71%   | 2.76%   | 2.89%   | 2.95%   | 2.50%   | 2.51%   | 2.44%   | 2.40%   | 2.40%   |
|      | Japan             | 2.04%   | 1.90%   | 2.08%   | 2.23%   | 2.05%   | 2.14%   | 2.05%   | 2.03%   | 1.94%   | 1.79%   | 2.31%   | 2.25%   | 2.10%   | 2.10%   |

## Offensive Security Tooling (OSTs)

![Offensive Security Tools (OST)]

Offensive Security Tools (OST)

7K

6K

5K

4K

3K

2K

1K

0K

Post-exploitation frameworks are essential components
in the arsenal of both red teams conducting security
assessments and malicious actors orchestrating cyber
attacks. These frameworks provide a suite of tools
and capabilities that enable attackers to maintain
persistence, move laterally within a compromised
network, escalate privileges, and ultimately achieve their
objectives, such as data exfiltration, system disruption,
or ransomware deployment.

Our C2 tracking capability detected over 15,000 unique
IP addresses associated with C2 frameworks in 2024.
Half of all servers were hosted in either China or the
United States (28% and 22% respectively). Sliver has
seen a notable increase in utilisation by threat actors
(12% to 17%), including Brute Ratel in the last three
months of the year (up from 1% to 7%). Additionally,
we continue to see increases in the usage of Supershell,
usually deployed on similar IP addresses to other threat
actor tools.

Cobalt Strike

Silver
Metasploit
SuperShell C2

Havoc

Panda C2

Brute Ratel

Meterpreter

Hak5 C2

Mythic
Night Hawk C2
Red Warden

Starkiller

Pupy
Covenant

Deimos C2

C2 Severs and OST

Posh

MIMPLANT C2

Armitage

Octopus
C3 Framework
Alchimist C2

Faction C2

Kalimpau C2

Kodiak

Our C2 tracking
capability detected
over 15,000 unique IP
addresses associated
with C2 frameworks
in 2024.

9

2025 Cyber Threat Intelligence Report

### Cobalt Strike
Cobalt Strike, a commercial framework initially designed for
adversary simulation and penetration testing, has become
one of the most widely utilised tools by threat actors.
Its comprehensive features, including C2 functionalities,
lateral movement techniques and payload deployment
mechanisms, have made it a favourite among both
legitimate security professionals and threat actors.

However, the dual-use nature of Cobalt Strike has led to
widespread abuse, with pirated and unlicensed versions
readily available on cyber criminal marketplaces, facilitating
its use in numerous offensive campaigns.

The popular post-exploitation framework accounted
for 42% of all servers tracked by tools under the OST
category. Of the Cobalt Strike servers tracked that aren’t
redirectors, nearly 45% are hosted in China.
These hosting providers, TENCENT (AS45090), ALIBABA
(AS37963) and HWCSNET Huawei Cloud Service
(AS55990), appear to be attractive infrastructure
hosting providers as the shelf-life of C2 servers within
China is considerable. The shelf-life of these services
is typically up to a year, suggesting an absence of any
outside interference from the hosting providers or law
enforcement. TENCENT and ALIBABA in particular account
for 80% of all Cobalt Strike servers hosted in China.

![Cobalt Strike C2 Global Distribution]

Cobalt Strike C2 Global Distribution
Cobalt Strike C2 Global Distribution

In comparison, 17% of Cobalt Strike servers were hosted on
servers in the United States. Additionally, this was broken
down in a much larger portion of hosting providers, with
37% of servers found on Digital Ocean (AS14061), Amazon
(AS14618, AS16509), and COLOCROSSING (AS36352). 11%
of Cobalt Strike servers were hosted in Hong Kong, with
ALIBABA-CN-NET (AS45102), LUCIDACLOUD LIMITED
(AS139659) and High Family Technology Co. (AS142032)
accounting for 34% of servers in this region.

In response to the prevalent misuse of Cobalt Strike,
particularly by ransomware gangs and nation-state actors,
cyber security firms, law enforcement agencies, and
industry organisations have made significant efforts to
disrupt its illicit use.

These efforts have included collaborative initiatives to
identify and dismantle malicious infrastructure associated
with Cobalt Strike.

However, we assess that whilst a decrease in the number
of Cobalt Strike servers between 2023 and 2024 could
attest to this disruptive action, numbers remain high
overall and continue to do so in other geographical areas.
Additionally, we have observed an increase in frameworks
such as Sliver and Brute Ratel which suggests a move
away from Cobalt Strike. Whilst we expected to see this
more notably in countries such as the United States, the
majority of new Brute Ratel servers are within China.

10

2025 Cyber Threat Intelligence Report

### Increased Adoption of Sliver and Brute Ratel
Sliver was developed as an open-source red team/
adversary emulation tool primarily used for security
testing purposes. It is a common tool used by a wide
range of threat actors to establish C2 within their
target’s environment and network.

Our C2 infrastructure tracking capability proactively
monitors for Sliver network indicators. The figure to the
right is a visual representing our current detection for
Sliver. In 2024, we tracked over 2000 servers linked to
Sliver.

The cyber security landscape in 2024 showed clear
indicators of a growing trend towards the adoption of
alternative post-exploitation frameworks, to Cobalt
Strike, particularly Sliver and Brute Ratel, suggesting
a shift in preferences among threat actors. This report
highlights an increase in the detection of Sliver servers
throughout the year.

While Cobalt Strike remained the dominant framework
in terms of the number of C2 servers observed, Sliver
experienced a notable rise in detections, positioning it
as a prominent alternative alongside Metasploit. The
Sliver offensive security framework has emerged as a
significant tool in the cyber threat landscape, initially
noted for its adoption by ransomware groups. However,
its versatility and effectiveness have also attracted the
attention of other malicious actors, including Advanced
Persistent Threat (APT) groups and access brokers.

![Sliver Global Distribution]

Sliver Global Distribution

Nearly 15% of OST C2 servers were attributed to
the Sliver framework in 2024. Unlike Cobalt Strike
geographical deployments, Sliver servers are vastly
different. Whilst China hosted the highest number of C2
servers (almost 45%), the highest concentration of Sliver
deployments in a single country was just 25% in the
US. Second was the Netherlands at 13% and Germany
at 11%. China drops to 5th highest with 6% of Sliver
servers.

The top 3 hosting providers associated with each
country are:
- The United States: Digital Ocean (AS14061),
  COLOCROSSING (AS36352) and UPCLOUDUSA
  (AS25697) accounted for 38% of Sliver servers in
  the US.
- The Netherlands: Stark Industries (AS44477), Digital
  Ocean (AS14061) and UPCLOUD (AS202053) accounted
  for 33% of Sliver server in the Netherlands.
- Germany: Digital Ocean (AS14061), Hetzner (AS24940)
  and Contabo (AS51167) accounted for 42% of Sliver
  servers in Germany.

11

2025 Cyber Threat Intelligence Report

Several documented instances in 2024 provide concrete
evidence of threat actors actively deploying Sliver:

- The North Korean Andariel group’s collaboration with
  Play ransomware involved the use of Sliver for
initial access, demonstrating its adoption by a nation-
  state actor. Additionally, a campaign targeting German
  entities was observed utilising a Sliver implant,
highlighting its use in targeted attacks.

- Furthermore, Sliver was reported to be delivered
  via exploits targeting vulnerable SimpleHelp Remote
  Monitoring and Management (RMM) instances,
indicating its use by actors exploiting software
  vulnerabilities for access. The reasons for Sliver’s
  popularity among diverse threat actors remain
  consistent; its open