# Cisco Talos Year in Review 2023

## Table of Contents
- [Telemetry trends](#telemetry-trends)
- [Ransomware and extortion](#ransomware-and-extortion)
- [Network infrastructure](#network-infrastructure)
- [APTs: China](#apts-china)
- [APTs: Russia](#apts-russia)
- [APTs: Middle East](#apts-middle-east)
- [Commodity loaders: Qakbot, Emotet, Trickbot, IcedID, Ursnif](#commodity-loaders-qakbot-emotet-trickbot-icedid-ursnif)

---

## Introduction

Ransomware, commodity loaders and APTs dominated the threat landscape in 2023. As we’ll outline in the second annual Cisco Talos Year in Review, global conflict influenced cybersecurity trends, shifting many threat actors’ tactics and approaches in operations ranging from espionage to cybercrime.

Cisco’s global presence and Talos’ world-class expertise provided a massive amount of data to sift through — endpoint detections, incident response engagements, network traffic, email corpus, sandboxes, honeypots and much more. Thankfully, our teammates include subject matter experts from all ends of the cybersecurity space to help us turn this intelligence into actionable information for defenders and users. Leveraging these rich, complex sources of information, we analyzed the major trends that shaped the threat landscape in 2023.

Ransomware continued to threaten enterprises globally in 2023, with LockBit remaining the top threat in this space for the second year in a row. Health care was the top targeted industry this year, as adversaries maintained their focus on entities that have cybersecurity funding constraints and low downtime tolerance. Not all things were the same, though, as we saw actors such as Clop deploy a collection of zero-day exploits, behavior we usually associate with advanced persistent threat (APT) activity. At the same time, leaked ransomware source code allowed low-skilled actors to enter the fray. Further complicating matters, we observed a new trend of ransomware actors turning to pure extortion, skipping encryption altogether while threatening to leak sensitive data.

Commodity loaders are still being used to deliver these ransomware threats, and many of the same families as last year remained prevalent, such as Qakbot and IcedID. This is reflected in our telemetry, as the most commonly spoofed brands were in financial services and shipping, hallmarks of these adversaries. But these loaders are shedding all remnants of their banking trojan past as they position themselves more as sleek payload delivery mechanisms. Developers and operators are adapting to improved defenses, finding new ways to bypass increasing security updates and compromise victims. And although we again observed a takedown of a large botnet, this year being Qakbot, our experience shows that this does not necessarily mean that the threat has been eliminated.

One of the newer cross-regional trends we have observed this year is an increase in the targeting of network devices from APTs and ransomware actors. Both groups rely on exploiting recently disclosed vulnerabilities and weak/default credentials, one of the reasons why the use of valid accounts was consistently a top weakness in Talos IR engagements. Whatever the sophistication and intent of the adversary is, the reason behind the targeting is the same: network devices are extremely high value while possessing many security weaknesses.

Geopolitical instability is manifesting in APT activity. This is reflected in our telemetry, which shows a rise in suspicious traffic during major geopolitical events. For Chinese groups, as relationships with the West and Asia Pacific become further strained, we see an emboldening in operations, such as a greater willingness to cause destruction. We also observe this in their targeting of telecommunications organizations, which possess numerous critical infrastructure assets in strategically important geographies such as Guam and Taiwan. For Russian APTs, Gamaredon and Turla targeted Ukraine at an accelerated pace, but Russian activity in general for 2023 did not reflect the full range of destructive cyber capabilities we have seen it deploy in the past, potentially because of the concerted efforts of defenders.

One bright spot this year was Cisco’s determined efforts to create and deliver inventive security solutions that help strengthen our partners. Talos’ Ukraine Task Force continues to thwart attacks against critical Ukrainian partners. This year, we spear-headed an effort to stabilize Ukraine’s power grid against the effects of global positioning system (GPS) jamming on the battlefield by delivering modified Cisco switches into an active war zone. Cisco also launched the Network Resilience Coalition with leading industry partners, focusing on increasing awareness and providing actionable recommendations for improving network security. Relatedly, Talos’s Vulnerability Discovery and Research Team made investigating small office, home office (SOHO) and industrial routers a major priority, reporting 289 vulnerabilities to vendors to date, published across 141 Talos advisories.

As conflict in the Middle East worsens, we are once again positioned to help protect our customers and partners. Therefore, perhaps the overarching story of 2023 is this: as the daringness, sophistication, and persistence of our adversaries grows, so too does the resolve of defenders to interdict them in any way we can.

---

## Telemetry trends

![Chart showing regional suspicious traffic volume over time]

### Section highlights
- Suspicious network traffic captured by Cisco Security products revealed sharp increases in activity that often corresponded with major geopolitical events and global cyber attacks.
- The most targeted vulnerabilities were older security flaws in common applications, consistent with the U.S. Cybersecurity and Infrastructure Security Agency’s (CISA) findings in recent years.
- Threat actors abused common file extensions and spoofed well-known brands, common techniques that underscore the use of social engineering to enable operations like phishing and business email compromise (BEC).
- Financial services and shipping companies accounted for the brands we observed being spoofed most often in email telemetry.
- The use of valid accounts was a top-observed MITRE ATT&CK technique, underscoring adversaries’ reliance on compromised credentials.

---

## Ransomware and extortion

### Section highlights
- Ransomware and pre-ransomware incidents continue to affect customers at a consistent rate — totaling the same 20 percent of Talos IR incidents as last year — with health care being the most targeted vertical.
- For the second year in a row, LockBit was the most prolific ransomware-as-a-service (RaaS) gang.
- ALPHV, Clop and BianLian also dominated the threat landscape.
- We saw Clop affiliates consistently exploit zero-day vulnerabilities, a highly unusual tactic suggesting the group possesses a level of sophistication matched only by APTs.
- Actors are turning to data extortion more than ever, with this being the top threat that Talos IR responded to in Q2 2023.

---

## Network infrastructure

### Section highlights
- Advanced actors are attacking networking devices at a concerning rate this year, particularly China and Russia-based groups.
- Other cybercriminals are starting to follow suit, adopting this technique to sell unauthorized access to these devices on the dark web.
- Actors take advantage of security weaknesses, such as default credentials and unpatched vulnerabilities, to gain initial access.
- Three of the five most targeted device vulnerabilities in this space are critical or severe.
- Talos is helping to combat this threat by supporting the Network Resilience Coalition.

---

## APTs: China

### Section highlights
- China-affiliated activity occurred at a rigorous pace this year, likely in response to geopolitical events.
- Beijing may be directing more aggressive intelligence collection and prepositioning for future attacks.
- Actors have improved in terms of deeply entrenching themselves in targeted networks and dodging detection.
- Talos observed several instances of ransomware actors compromising a target closely following a long-term, covert APT intrusion.
- Telecommunications organizations were a top target of Chinese cyber operations in 2023.

---

## APTs: Russia

*(Content omitted in source)*

---

## APTs: Middle East

*(Content omitted in source)*

---

## Commodity loaders: Qakbot, Emotet, Trickbot, IcedID, Ursnif

*(Content omitted in source)*

---

© 2023 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com

---

attacks
potentially represent a dangerous new destructive
element to PRC-affiliated APT attacks that we assess
reveals an escalation from previous years.

More rigorous pace of operations
likely linked to shifts in
geopolitical environment

Activity conducted by China-affiliated APTs occurred at a
fast tempo this past year, likely due in part to geopolitical
factors that Chinese leadership perceived as threats to
the Communist Party of China’s (CCP’s) governance. We
quantified this increase in activity based on the number
of government partner intelligence shares, collaboration
projects with CISA, related infrastructure targeting cases,
and high-priority investigations into China-affiliated
activity affecting Cisco customers.

This shift in tempo may reflect a difference in intent, a
type of signaling we have not observed in years past.
Beijing typically directs cyber activity with the intent of
collecting intelligence to address the economic, political
and strategic goals of the CCP. Though some of these
goals, such as their Five-Year Plans, are routinely set
as long-term objectives for growth, other provisional
needs are determined based upon China’s relationships
with other nations. For example, if a relationship with a
nation China relies on for exports deteriorates, Chinese

“Activity conducted by
China-affiliated APTs
occurred at a fast tempo
this past year, likely due in
part to geopolitical factors
that Chinese leadership
perceived as threats to the
Communist Party of China’s
(CCP’s) governance.”

© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com

page 19

2023YEAR IN REVIEWThreat actor
highlight:
Volt Typhoon

Volt Typhoon is a China-
affiliated threat group that made
headlines this past year for their
long-term operation targeting
U.S. critical infrastructure
organizations and military bases.

Talos investigated a sustained
Volt Typhoon intrusion targeting
the telecommunications sector
in Guam, which is notably the
site of a U.S. military base
significant for the defense of
Taiwan. Our research revealed
the actors maintained persistent
access to and exfiltrated data
from networks of a service
provider and certain high-value
customers for at least a year
and a half. Talos continues to
closely collaborate with public
and private partners on hunting
this threat group’s activity
and investigate the group’s
anonymization infrastructure.

Advanced persistent threats: China

actors may seek to exfiltrate proprietary data,
focused on espionage yet deliberately quiet,
that can boost their self-reliance in developing
whatever that export is. If a relationship with
a nation becomes increasingly contentious,
China may seek to establish footholds in the
networks of that nation’s critical infrastructure
and preposition themselves for future
destructive attacks.

Numerous geopolitical events affected China’s
relationships with the West and Asia Pacific
this year, potentially leading to CCP directives
for more aggressive targeting activity. Talos
performed intensive incident response
operations for strategic targets in both of
these regions.

Deepening divide between
China and the West

One major factor that has deepened the
divide between China and the West this year
has been the PRC’s alliance with Russia,
particularly as other world leaders have
vehemently denounced Moscow’s actions in
the Russia-Ukraine war. The two countries
have strengthened their trade relationship,
and China’s rapidly increasing exports to
Russia have tempered the impact of numerous
Western sanctions that have been levied
against the country since its invasion of
Ukraine. Russia and China have also united to
expand their presence in the Middle East and
developing countries, conducting joint military
exercises in the Gulf of Oman in March 2023,
and inviting numerous nations to join BRICS
group in August 2023, bolstering the trade bloc

against competition from the West.

U.S. policies and positions regarding China
have not softened this year, with the U.S.
continuing to categorize China as a top security
threat. The Director of National Intelligence
named China the “most consequential threat”
to U.S. national security in 2023, and the
U.S. has steadily expanded sanctions against
Chinese companies and organizations because
of such concerns. These security issues were
exemplified by an incident in early 2023 when
a Chinese spy balloon flew over the U.S.,
gathered intelligence from military bases, and
transmitted the information back to Beijing
before being shot down. The U.S., Japan and
South Korea also bolstered their alliance in
2023, with the countries’ leaders meeting at
Camp David in August and committing to work
together to address security challenges from
China and North Korea. Beijing swiftly criticized
this meeting, publicly stating attempts to form
military blocs in the Asia Pacific will be met
with “vigilance and opposition.”

Growing conflict in the
Asia Pacific

Meanwhile, China is already facing conflict
with neighboring nations in the Asia Pacific.
Tensions have been rising between China
and Taiwan, exacerbated by U.S. support in
expanding Taiwan’s self-defense capabilities.
The People’s Liberation Army (PLA) has upped
its military pressure on the island, routinely
sending warplanes, drones and ships past
the median line of the Taiwan Strait in shows
of force. China has also become increasingly

aggressive in the South China Sea, doubling
down on their claims to sovereignty over
almost all of the disputed area. Their robust
military presence in the region has incurred
standoffs and conflict throughout the past year
with neighboring countries that have competing
claims for the territory, as well as with the
U.S. military that is present there. Finally,
China’s relationship with Japan has also seen
challenges in the past year, with events like
Japan restricting exports of semiconductors
and Tokyo’s decision to release water from the
Fukushima Daiichi nuclear power plant, which
elicited criticism from Beijing.

Targeting of the
telecommunications
sector expands collection
and prepositions actors for
future attacks

We responded to several intrusions into
telecommunications providers by China-
affiliated APTs this year, particularly in areas
that are of strategic interest to Beijing.

Telecommunications organizations are
attractive targets for these groups, as they
often control numerous critical infrastructure
assets in the country, such as national satellite
systems, internet services, and telephone
networks that are vital to the private and
public sectors. China-affiliated APTs can
use their unauthorized access to establish
footholds to disrupt critical services, such as
communication infrastructure, in the event of a
conflict with the targeted nation. They can also

pivot into the networks of additional high-value
targets of interest and conduct widespread
exfiltration of sensitive data.

There are several ways in which use of this
latter technique can challenge remediation
efforts. A service provider may not immediately
realize or have visibility into the extent of
an intrusion targeting other businesses,
subscribers or third-party providers, giving
the actors ample time to burrow themselves
deeper into compromised networks. The
guidance for notifying customers of a breach
also varies by country, potentially delaying
incident response based on the geographic
location of the initial victim. Finally, given
delicate diplomatic relations that may exist
between the targeted country and adversary,
U.S.-based incident response teams may face
challenges and political sensitivities when
assisting in certain regions. Victims in certain
countries may be hesitant to assign attribution
to a particular threat group, could have strong
organizational ties to China, and/or may be
wary of sharing key details of the compromise
with American teams.

© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com

page 20

2023YEAR IN REVIEWAdvanced
persistent
threats: Russia

Section highlights

•  Russian state-sponsored APT Gamaredon has remained a major player
in threats against Ukraine and was the top threat that the Cisco Talos
Ukraine Task Unit responded to this year.

•

In 2023, Gamaredon primarily targeted entities in North America and
Europe, with a disproportionate number of victims in Western Europe.
Additionally, over half of the entities targeted were in the transportation
and utilities sectors, reflecting Russia’s focus on critical infrastructure.

•  Turla, another Russian government-affiliated APT, was largely active
between September 2022 and February 2023, but their operations
diminished significantly around May 2023, coinciding with the U.S. Justice
Department’s disruption of Turla’s Snake malware.

•  The number of affected sectors and volume of victims between these two
groups vastly differed, contrasting Gamaredon’s broader targeting with
Turla’s more limited activity against highly selective victims.

•  Beyond Gamaredon and Turla activity, we also observed a spike in

SmokeLoader activity — malware used by a variety of different groups
— in late April and early May, aligning with CERT-UA’s reporting of mass
distribution of SmokeLoader targeting Ukrainian entities.

•  To stabilize Ukraine’s power grid against the effects of global positioning
system (GPS) jamming on the battlefield, Cisco hardware and software
engineers modified one of our commercial network switches to provide
holdover for Ukraine’s power grid equipment during these outages.

© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com

page 21

Subhead herelyhere2023YEAR IN REVIEWYEAR IN REVIEW2023Advanced persistent threats: Russia

T hreats from Russian state-sponsored or state-aligned APTs remain a

mainstay in our threat tracking and research efforts this year. Since the

onset of the Russian invasion of Ukraine, Russian APTs’ engagement in

cyber espionage, cyber influence, and destructive attacks has intensified. In

line with activity reported in last year’s report, Russian APTs continue to adapt

to geopolitical challenges stemming from the war and NATO and allied nations’

military assistance to Ukraine. Additionally, 2023 saw a global law enforcement

effort to dismantle the Snake malware, considered one of the most prolific

and sophisticated cyber espionage tools in the Federal Security Service of

the Russian Federation’s (FSB) arsenal commonly deployed against systems

globally.

Gamaredon and Turla
remain top threats,
targeting patterns vary

Russia-affiliated APT groups Gamaredon and Turla
continue to persist as top threats in this space,
updating aspects of their attacks and toolkits to
support their TTPs, despite international efforts to
combat the Russian cyber threat.

Cisco Talos closely tracks activities associated with
Gamaredon, an APT broadly suspected to be a team
of Russian government-supported actors based
in Crimea. While the group in recent months has
concentrated their efforts on cyberespionage against
Ukrainian entities, they also target entities globally,
with a less focused victimology as compared to other

Russian APTs operating in this space. Turla
also conducts long-term espionage and data
exfiltration operations that are in line with Russian
intelligence priorities that the U.S. government
attributes to a unit within the FSB. In contrast to
Gamaredon, who we observed targeting a range of
sectors in 2023 (Figure 10), Turla is known for much
more targeted operations against a smaller number
of strategically important entities. Turla, who is
publicly assessed to operate on behalf of a different
unit than Gamaredon in the FSB, is likely capable of
compromising a much broader spectrum of entities
worldwide but limits their operations to what they
perceive to be high-value targets.

The number of sectors and volume of victims that
Gamaredon and Turla targeted vastly differed, based
on our telemetry (Figures 10 and 11).

FIGURE 10

Industry verticals targeted by Gamaredon

FIGURE 11

Industry verticals targeted by Turla

Note: Percentages may not equal 100% due to rounding.

© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com

page 22

2023YEAR IN REVIEWAdvanced persistent threats: Russia

FIGURE 12

Gamaredon malicious download activity throughout the year

FIGURE 13

Activity across Turla malware variants Gazer, Kazuar, Mosquito and Neptun this year

“Beyond highlighting the
sectors that Gamaredon
and Turla targeted this
year, the data is also largely
representative of the
volume of attacks Snort
helped prevent.”

The largest spread of Gamaredon victims were
located in North America, followed by Europe
and the Middle East, with a disproportionate
number of victims in western Europe. Over half of
Gamaredon’s targeting activity impacted the utilities
and transportation industry sectors, consistent with
Russia’s targeting of critical infrastructure entities,
likely to cause the most disruption to strategic
entities to stymie Ukraine’s war efforts.

In September and December 2022 and September
2023, we saw three clear spikes in Gamaredon
activity (Figure 12), potentially representing clusters
of specific targeted operations. The ramped
up Gamaredon activity as seen in Figure 12 in

August 2023 is consistent with the group’s activity
levels according to a report by Ukraine’s National
Coordination Center for Cybersecurity (NCCC).

In contrast to the range of industry verticals
Gamaredon targeted this year, Turla targeted
fewer victims across a smaller number of sectors
and geographies, in line with the group’s precise
operations. The manufacturing and financial services
sectors were equally impacted, with education and
agriculture targeted to a lesser degree (Figure 11).
Beyond highlighting the sectors that Gamaredon
and Turla targeted this year, the data is also largely
representative of the volume of attacks Snort
helped prevent.

Malware deployed by and custom to Turla, including
various backdoors and implants used for persistent
access, are seen to congregate in a series of events
largely occurring between September 2022 and
February 2023. While the reason for the heightened
activity during that period is unknown, we asses
it is likely to have stemmed from an increased
operational tempo in response to the Russian
invasion on Ukraine. These four malware families —
Gazer, Kazuar, Mosquito and Neptun — while not an
exhaustive list of Turla malware, are part of Turla’s
large arsenal of bespoke malware and modified
open-source malware, which are constantly updated
or replaced with more advanced versions.

This clustering over time, as seen in Figure 13,
of custom Turla malware continues to convey the
narrative of Turla’s operational tempo, likely highly
based on the selectivity of targets. Notably, the
depiction of Turla malware activity in Figure 13
(while not an exhaustive list) diminishes significantly
around May 2023, coinciding with the U.S. Justice
Department’s disruption of Turla’s Snake malware.
For nearly 20 years, Turla deployed Snake to steal
and exfiltrate data from targeted systems through
numerous relay nodes scattered around the world.
While the effects of the Snake disruption on Turla’s
current and future operations are still unknown, the
diminished malware activity may represent changes
in Turla’s toolkit as a result of the disruption.

© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com

page 23

2023YEAR IN REVIEWYEAR IN REVIEW

Advanced persistent threats: Russia

FIGURE 14

Top threats in Ukraine task force investigations

FIGURE 15

Top five malicious activities affecting Ukraine partners

Internal Task Unit continues to
monitor threats to Ukraine

Talos’ ongoing support for Ukraine continues to be a
large focus of our operational efforts this year. As part
of the Task Unit’s work, we monitor suspicious activity
in endpoint telemetry for nearly three dozen Ukrainian
partners across critical infrastructure sectors, including
government, utilities, financial services, health care and
transportation, among others.

While the threats against these organizations may not
all be designated as APT activity, the volume of threats
and volatile geopolitical climate they are deployed in
poses a significant risk to network defenders protecting
critical assets.

Gamaredon is the most dominant threat to Ukraine
that our task force has responded to (Figure 14). The
group has historically targeted predominantly Ukrainian
entities — particularly those responsible for the
country’s defense, diplomacy and internal security.

Gamaredon, and portions of their attack chain,
consistently appear in top threat hunting alerts from
Cisco Secure Endpoint that notified our Ukrainian
partners (Figure 15). For example, these top five
behaviors demonstrate the consistent use of LoLBins
and the techniques associated with them, such as
Wscript execution — a legitimate Windows process
likely used to masquerade malware deployment under
the guise of expected activity — that continue to be
leveraged to support a variety of threats across an
attack lifecycle. Activity commonly linked to financially
motivated cybercriminals, like the deployment of
cryptocurrency mining and information stealers, also
continue to impact Ukrainian organizations across
numerous industries, speaking to the broad range of
threats facing Ukraine.

© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com

page 24

2023Advanced persistent threats: Russia

FIGURE 16

SmokeLoader malware activity throughout the year

“The significant cyber
defense resources we
continue to devote to
protecting our Ukrainian
partners has undoubtedly
had a significant impact
on this threat space as
well, thwarting significant
disruptions by mitigating
attacks in the early stages.”

Beyond highlighting the consistent tempo of
Gamaredon activities above, Figures 14 and 15
also help to demonstrate the multitude of threats
the Task Unit has responded to this year. This
includes activities from malware threats such
as loaders, information stealers, ransomware,
cryptocurrency miners and Raspberry Robin,
a prolific malware family covered in last year’s
annual report, which remains a consistent threat to
enterprise environments. For example, SmokeLoader
is a downloader leveraged by a variety of groups

that the Task Unit has repeatedly responded to
this year (Figure 14). Typically delivered via email,
SmokeLoader drops malware on infected machines
and since early May, has been consistently reported
by Ukraine’s Computer Emergency Response Team
(CERT-UA) further highlighting its persistent use in
the threat landscape.

We observed a spike in SmokeLoader activity in
late April and early May, aligning with CERT-UA’s
reporting of mass distribution of SmokeLoader
targeting Ukrainian entities (Figure 16).

While the Task Unit has continuously responded
to a myriad of cyber threats since the onset of the
Russia-Ukraine war, the observed activity in 2023
was far less sophisticated than what is typically
associated with the sophisticated adversaries we
would expect to see in this space. The activity
was dynamic this year but does not reflect the
full range of destructive cyber capabilities Russia
has previously demonstrated against Ukraine and/
or its NATO allies. The reasons behind this have
been debated by industry partners and experts,

and it is likely the result of combined efforts from
the cybersecurity industry, U.S. government,
foreign partners, and Ukraine’s own commitment to
protecting its people. The significant cyber defense
resources we continue to devote to protecting our
Ukrainian partners has undoubtedly had a significant
impact on this threat space as well, thwarting
significant disruptions by mitigating attacks in the
early stages.

© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com

page 25

2023YEAR IN REVIEWAdvanced persistent threats: Russia

Project PowerUp: Keeping
the lights on in Ukraine

Leveraging Talos’ unique relationships with industry,
government, and Ukraine, we spearheaded an effort to
help stabilize Ukraine’s power grid against the effects of
GPS jamming on the battlefield.

Faced with the complex problem of how to make
Ukraine’s substations resistant to operational failures
caused by downed GPS signals, Cisco hardware and
software engineers modified one of our commercial
network switches, the Cisco Industrial Ethernet switch,
to provide holdover for Ukraine’s power grid equipment
during these outages.

After months of development and coordination with
various partners, the devices were delivered to Ukraine
and installed in substations around the country, no small
feat during an active war zone. This story will be featured
in Cisco’s annual Purpose Report later this year. This
example further demonstrates how Cisco’s efforts have
helped safeguard Ukraine’s critical infrastructure from
severe Russian cyberattacks in 2023.

How is Ukraine’s
power grid
affected when
GPS goes down?

Many of Ukraine’s high-voltage
electrical substations — which
play a vital role in the country’s
domestic transmission of
power — make extensive use
of the availability of precise
GPS timing information to
help operators anticipate,
react and diagnose a complex
high-voltage electric grid.
When GPS signals are
widely disrupted, substations
cannot synchronize their time
reporting accurately because
they cannot assign accurate
timestamps. Without good
synchronized data, efforts
to manage loads between
different parts of the system
can be affected, and this
management avoids outages
and failure, especially during
peak demand and surge
times. This disruption can be
widespread, causing wide
areas to lose GPS service for
long periods of time.

© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com

page 26

2023YEAR IN REVIEWAdvanced persistent threats: Russia

FIGURE 17

YoroTrooper threat actor matrix

Some YoroTrooper
members hail from
pro-Russia Kazakhstan

Earlier this year, Cisco Talos disclosed information
on a new threat actor we named “YoroTrooper,”
who we assess with high confidence consists,
at least in part, of individuals from Kazakhstan.
YoroTrooper is a highly motivated threat actor
whose low sophistication is complemented with
aggressive targeting of entities using a multitude of
commodity malware families. Since 2022, the group
has conducted operations aimed at espionage and
data theft against victims in the government or
energy sectors in Azerbaijan, Tajikistan, Kyrgyzstan
and other members of the Commonwealth of
Independent States (CIS).

APT activity from Russian allies

Talos’ research and monitoring efforts of regional threats have
expanded to APT activity attributed to countries formerly part of
the Soviet Union, whose intelligence goals, TTPs and victimology
often align with the Kremlin. Given the long-standing political
union between these governments, collaboration is plausible.
However, we do not have direct evidence of Russian government
involvement.

We assess YoroTrooper also targets organizations of strategic
value across European and Turkish governments (Figure 17). For
example, YoroTrooper has compromised accounts for at least
two international organizations, including a critical European

Union (EU) health care agency and the World Intellectual
Property Organization (WIPO). Successful compromises also
included embassies of European countries including Azerbaijan
and Turkmenistan.

This year, Talos has also been monitoring GhostWriter operational
activities, which is a group allegedly linked to the Belarusian
government, according to CERT-UA. We have observed several
GhostWriter campaigns against government entities, military
organizations and civilian users in Ukraine and Poland. We judge
that these operations, often seen promoting anti-NATO narratives
that aim to undermine regional security cooperation, are very
likely aimed at stealing information and gaining persistent remote

access. Recent activities, also tracked by CERT-UA, demonstrate
the group’s exploitation of the WinRAR ZIP parsing vulnerability,
CVE-2023-38831. The vulnerability allows attackers to hide
malicious code in ZIP archives masquerading as popular file
formats including JPG or TXT files, which GhostWriter
leveraged to deploy Cobalt Strike and the malware
downloader, PicassoLoader.

We cannot rule out Russian contributions to YoroTrooper
or GhostWriter at this time. These operations and targeting
patterns, often strongly aligning with Russian strategic interests,
are key for understanding regional threats against the backdrop
of the Russian invasion of Ukraine.

© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com

page 27

2023YEAR IN REVIEWSection highlights

•  Events in early October 2023 between Hamas and Israel contributed to
several politically motivated hacktivist groups launching uncoordinated
and mostly unsophisticated attacks against both sides, similar to what we
observed at the beginning of the Russia-Ukraine war.

•  The Middle East’s complicated geopolitical environment continued to

be dynamic this year, and we will likely see that impact the cyber realm
going forward. As longtime regional adversaries attempt to normalize ties,
and decades-old conflicts spark new violence, major cyber players with
economic and political interests in the Middle East, like China and Iran,
may be more motivated to influence outcomes through direct or proxy
operations.

•  Middle East-based APT groups targeted telecommunications firms in the
region, following the trend we have seen of sophisticated adversaries
targeting this sector. As part of this activity, we identified a new intrusion
set, ShroudedSnooper, deploying novel implants we dubbed HTTPSnoop
and PipeSnoop against related entities.

•  The Iran state-sponsored MuddyWater APT group relied less on

the commonly used Syncro tool — essential for remote access and
malware deployment — than in previous years, likely in response to the
cybersecurity industry’s action against known MuddyWater TTPs.

Advanced
persistent
threats:
Middle East

© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com

page 28

Subhead herelyhere2023YEAR IN REVIEWYEAR IN REVIEW2023Advanced persistent threats: Middle East

R egional state-sponsored groups continue to conduct

Europe, the Middle East and Asia. Telecommunications

pervasive cyber attacks against entities in North America,

companies endured the most of these attacks, a trend that

has transcended multiple APTs, as outlined in other parts of

this report. Our work in this space resulted in the discovery of

a new actor we named ShroudedSnooper that appears intent

on targeting major telecommunications entities in the region.

The Iran state-sponsored MuddyWater APT actor remains a

key player in this threat space and was the focus of much of

our research efforts this year. While the group continues to use

many of the same techniques to advance their primary goals of

stealing intellectual property and collecting intelligence, industry

action has likely influenced the group’s ability to use certain tools,

including the Syncro remote management and monitoring (RMM)

platform that the group was using at the end of 2022.

The Middle East is arguably the most complicated geopolitical

region in the world, and the conflict that ignited between Hamas

and Israel in October 2023 reminds us that events with global

consequences can unfold quickly and with little notice. The

everchanging geopolitical landscape here will undoubtedly affect

cyber activity going forward, as established regional players like

Iran remain intent on achieving certain geopolitical goals and new

actors like China seek to expand its influence.

Hamas-Israel conflict brings
influx of hacktivist groups

Hamas’ surprise attack on Israel in October not only
had global implications but also has affected the
cyber realm, immediately drawing in actors from both
sides of the conflict. Politically motivated hacktivist
groups — including well-known actors like Killnet and
Anonymous Sudan as well as lesser-known groups —
launched uncoordinated and mostly unsophisticated
attacks at the outset, as the threat space was quickly
flooded with many different actors. Several hacktivist
groups quickly announced support for both sides in
the Israel-Hamas conflict, posted threatening political
messages, called on followers to join in and claimed
responsibility for DDoS attacks against targets of
interest — typical hacktivist TTPs. This is broadly
consistent with what we observed at the start of the
Russia-Ukraine war, when an influx of cyber activity
became concentrated on these countries
seemingly overnight.

Significant geopolitical events like this also invite the
participation of much more sophisticated adversaries,
including those supported and funded by foreign
state governments. We have seen this most recently
in Ukraine, where advanced state-sponsored actors
from Russia like Gamaredon and Turla have been
relentless in their targeting of Ukranian entities since
the start of the war. Likewise, we expect to see an
increase in Iranian cyber activity in the Middle East
following Hamas’ attack on Israel. Iran and Israel
are longstanding adversaries, and their decades-
old conflict has major influence on Iran’s cyber
operations. Iran is also a key backer of several
anti-Israel militant and terrorist groups, including
Hamas, Hezbollah, and the Palestinian Islamic Jihad,
which were all involved in this most recent spate
of violence against Israel. Iran’s support for these
groups and Tehran’s historical hostility with Israel
strongly suggests Iran may use its cyber capabilities
to influence the outcome of the crisis, much like other
nations rely on cyber as an essential tool to advance
foreign policy objectives.

“The Iran state-sponsored MuddyWater APT actor remains a key player
in this threat space and was the focus of much of our research efforts
this year. While the group continues to use many of the same techniques
to advance their primary goals of stealing intellectual property and
collecting intelligence, industry action has likely influenced the group’s
ability to use certain tools.”

© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com

page 29

2023YEAR IN REVIEWAdvanced persistent threats: Middle East

Chinese ambitions
in the region portend possible
cyber operations

While China has traditionally held a prominent economic role
in the Middle East as one of the largest foreign investors,
PRC leadership sought to also expand their political
presence in the region this past year by engaging in regional
conflict mediation. In March, Beijing brokered an agreement
between longtime adversaries Iran and Saudi Arabia to
reestablish diplomatic ties, and in September, China and Syria
announced a strategic partnership, as Syrian President Bashar
Assad begins to reenter the international fold after more than
a decade of brutal civil war. The China-Syria deal may also
provide great economic incentives for Beijing, which could
become a major financial backer of Syria’s reconstruction
efforts. These strategic moves by China come at a time when
the U.S. has largely withdrawn from the region following the
post-9/11 period, and Beijing likely sees this as an opportunity
to capitalize on waning U.S. involvement and influence there.

Because of China’s growing political presence in the
Middle East, we expect to see more Chinese APT activity
in the region. We have observed Chinese APTs, among
the most active and persistent of state-sponsored threats,
supplementing financial endeavors with espionage
operations in regions it is invested in, targeting private sector
organizations and governments whose intellectual property
aligns with economic goals. Future operations would likely
be in-line with well-established Chinese APT TTPs, like
targeting entities and individuals that operate in industries
essential to China’s strategic plans, establishing long-term
and stealthy access to targeted networks, and stealing
intellectual property and technology.

FIGURE 18

HTTPSnoop URLs masquerading as
OfficeCore’s LBS System

Because of China’s growing political
presence in the Middle East, we
expect to see more Chinese APT
activity in the region.

telecommunication firms. OfficeTrack is an application
promoted as a workforce management solution
developed by OfficeCore, a software company
that helps users manage administrative tasks. In
several instances, we saw URLs ending in “lbs” and
“LbsAdmin,” references to the application’s former
name (OfficeCore’s LBS System) before it was
rebranded to OfficeTrack (Figure 18).

Throughout our analysis of the ShroudedSnooper
implants, the adversary used multiple URLs consisting
of patterns mimicking provisioning services from
telecommunications companies, including an Israeli
telecommunications provider, likely to blend into
typical network traffic. The DLL-based variants of
HTTPSnoop usually rely on DLL hijacking in benign
applications and services to get activated on the
infected system, which was highlighted as a top
technique this year in earlier sections of this report.

Telecommunications sector
remains key target for regional
threat actors

In 2023, we discovered a new intrusion set,
ShroudedSnooper, deploying novel backdoor
implants, HTTPSnoop and PipeSnoop, against
telecommunications providers in the Middle East,
a continuation of a trend we have been monitoring
in which sophisticated actors frequently target this
sector. There is currently not enough evidence to
link ShroudedSnooper activity to a specific country.
However, the group’s consistent masquerading of
software applications used by telecommunication
firms in the region and impact to several regional
providers highly aligns with likely state-sponsored
actors and sophisticated adversaries around
the world.

The HTTPSnoop and PipeSnoop implants consist of
novel techniques to listen to incoming requests for
specific HTTP(S) URLs and execute on an infected
endpoint. Some of the HTTPSnoop implants use
URLs that masquerade as those belonging to
OfficeTrack, which is especially marketed toward

© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com

page 30

2023YEAR IN REVIEWAdvanced persistent threats: Middle East

Industry actions likely affected
MuddyWater operations

In late 2022, it was first reported that Iranian-backed APT group
MuddyWater was using the Syncro remote management tool to take
over target devices. This activity is consistent with Talos IR data from
Q4 2022 (October - December 2022), where a growing number of
adversaries were increasingly relying on Syncro, observed in nearly 30
percent of engagements.

In December 2022, Syncro released a statement addressing concerns
about MuddyWater’s deployment of Syncro in spear phishing
campaigns targeting organizations in the Middle East and Asia. The
company implemented additional verification measures for new trial
account creation to limit the use of Syncro by illegitimate actors, and
monitored for irregular account information and usage, terminating
accounts that violate these new policies.

This swift action taken by Syncro most certainly has had an impact
on MuddyWater operations, highlighting the direct effect industry can
have on thwarting components of advanced adversaries’ operations.
While the reason for Syncro’s increased usage in Q4 2022 was
unknown, its use as a fully featured remote access platform for
managed service providers (MSPs) and its ubiquity across enterprise
environments likely made it an attractive option.

“This swift action taken by Syncro most
certainly has had an impact on MuddyWater
operations, highlighting the direct effect
industry can have on thwarting components
of advanced adversaries’ operations.”

Syncro leveraged to
maintain access

In an incident affecting a
telecommunications company,
Talos IR identified company email
accounts sending phishing emails
with subject lines that translated
from Arabic to “Staff Promotion.”
The emails contained OneDrive
and OneHub phishing links with a
compressed Microsoft Windows
Installer (MSI) file that installed
Syncro. The adversary used
Syncro to stay connected to
the targeted user’s workstation.
During analysis of the MSI
file, multiple Syncro services
were also installed, including
SyncroRecovery (SyncroLive) and
SyncroOvermind. The adversary’s
tactics appeared to focus on
maintaining initial access through
installation of Syncro. The lack
of MFA for email access allowed
the adversary to perform phishing
attacks, highlighting the need
to ensure MFA across all critical
assets.

© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com

page 31

2023YEAR IN REVIEWCommodity
loaders

Section highlights

•  Commodity loaders such as Qakbot, Ursnif, Emotet, Trickbot and IcedID
represent some of the most impactful and pervasive threats, as actors
routinely rely on them to enable key parts of their operations. Their use
as downloaders for information-stealers, ransomware, and other malware
have made them mainstays in the threat environment, indiscriminately
affecting entities globally.

•  All these loaders formerly functioned solely as banking trojans, and

developers have diversified their capabilities in recent years to support
more advanced operations. In 2023, new versions of IcedID, Ursnif, and
Qakbot appeared to be tailored specifically for ransomware actors, based
on their enhanced reconnaissance features, removal of functions that
might trigger antivirus detections, and quick adoption by ransomware
groups and initial access brokers.

•  Microsoft’s disabling of macros by default caused commodity loader

actors to invent new ways to use macros undetected or avoid using them
entirely. Qakbot operators used a wide variety of file types, scripting
languages, packers, and exploits to deploy the loader. Emotet, IcedID,
and Ursnif varied their techniques, although less frequently compared to
Qakbot, and also tended to still rely on older TTPs.

•

It can be challenging to eradicate the threat of commodity loaders
even after the botnet is dismantled, as developers have been known to
continue operating on behalf of different malware groups or rebuild their
botnets. Furthermore, previously compromised infrastructure could be
leveraged by other threat actors for malicious activity.

© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com

page 32

Subhead herelyhere2023YEAR IN REVIEWYEAR IN REVIEW2023Commodity loaders

A ctors have consistently relied on

was no different. Many of these threats

commodity loaders for years, and 2023

are widely available for purchase on underground

FIGURE 19

IcedID activity increased around release of the new variant

forums, provide a low barrier of entry for

unsophisticated actors, and are highly modular,

allowing threat actors to carry out multiple

phases of an attack. Throughout 2023, Qakbot,

Ursnif, Emotet, Trickbot and IcedID stood out as

the most impactful threats in this space.

Commodity loaders’ updates seem
tailored to support ransomware activity

In late 2023, we observed the latest variants of IcedID and Ursnif,
and a new automated feature in Qakbot, supporting ransomware
deployment, following a trend of commodity loaders playing an
integral part in the ransomware infection chain. These updates
were tailored to enhance the malware’s dropper functionalities,
likely signifying a further shift away from their original intended use
as banking trojans. Trickbot and Emotet are also known to facilitate
ransomware attacks, however, they did not receive similar upgrades
in 2023.

In November 2022 and February 2023, IcedID developers released
two new versions that were stripped of their banking functionalities
and designed to solely function as droppers. In 2023, these versions,
dubbed “Forked” and “Lite,” were used by initial access brokers,
known for commonly selling network accesses to ransomware groups.
While the original version was also used by initial access brokers and
ransomware groups, the new versions are likely a more attractive
option because they were stripped of functions that might trigger AV
signatures, thereby making them stealthier. IcedID activity increased

between November 2022 and February 2023—
corresponding with the new versions’ release—
suggesting actors were keenly interested in trying
out the threat’s latest capabilities (Figure 19).

The latest Ursnif variant, which was similarly
retooled to exclude banking trojan functionality,
was also seemingly intended to support
ransomware deployment. In 2023, this updated
version (released in 2022) was adopted by
the prolific ransomware group Royal, the first
instance of any ransomware gang incorporating
Ursnif into their operations. Since Royal is the
only group that has been observed leveraging
this new variant, there may be a professional
association between the developers. Royal is a

group of sophisticated cyber criminals first active
in September 2022, and suspected by many
security professionals to be a rebrand of the
prolific Russian ransomware group Conti. Royal
tightly controls their malware and ransomware
operations, unlike many other ransomware
groups that arose in the last two years who
chose to operate as a RaaS. Therefore, an
exclusive partnering of the new Ursnif variant
and Royal is likely intentional and could imply an
affiliation between the developers.

Finally, in late 2022, Qakbot deployed several
new automated features, including a capability
ideally suited to helping ransomware groups
determine valuable targets prior to deployment.

The updates included a list of reconnaissance
commands to map out the customer’s
environment upon initial infection. The output of
these commands enumerated data that would
be most useful to ransomware groups, including
domain groups, the domain name, and names
of domain controllers. This information could
assist with lateral movement resulting in Active
Directory takeover, a tactic commonly used by
ransomware groups. Qakbot’s new automated
reconnaissance capabilities also may have
helped ransomware groups evade detection,
because the gathered data could be used to
formulate a detailed plan of attack, minimizing the
time between initial infection and encryption.

© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com

page 33

2023YEAR IN REVIEWCommodity loaders

Commodity loader operators evolved
TTPs in response to new security
updates blocking macros, continuing
a trend that began in mid-2022

In 2023, Microsoft blocked macros by default, a notable change
that caused actors to modify their initial access and malware
delivery techniques. Prior to the change, macros would run
automatically when Microsoft Office documents were opened.
Macros have been heavily abused by threat actors to execute

malware automatically when a victim clicks on a malicious
attachment in a phishing email. Now, the user receives a security
warning if they click on a potentially malicious attachment,
reducing the likelihood of downloading malware. Microsoft’s
disabling of macros continued to have an impact throughout
2023, as threat actors invented new ways to use macros
undetected, or to avoid using macros entirely. When Microsoft
created a new patch to update security features, threat actors
were able to quickly change their TTPs in a game of cat-and-
mouse (Figure 20).

FIGURE 20
Commodity loaders allow threat actors to quickly change TTPs in response to changing security features

Sample reconnaissance
commands we observed
deployed by Qakbot
affiliates in 2023

Threat actors conduct reconnaissance to gather
information for additional operations. We observed
Qakbot affiliates abusing common Windows utilities
that allow for command execution in an attempt to
hide among legitimate activity. Below are just a few
examples to demonstrate the potential harmful impact
of these commands.

Netstat -nao: Used to obtain a list of open ports that
are particularly vulnerable to malicious attacks and a
list of active connections between the infected host
and other systems, such as a cloud environment, to
determine whether the victim can access data that is
of value to the threat actor.

Net localgroup: Used to identify administrator
accounts (i.e., accounts with elevated privileges that
can access sensitive data and make changes to the
system). This information helps a threat actor know
which accounts to prioritize in their targeting efforts.

Arp -a: Used to display the ARP cache, a record
of each IP address and its corresponding MAC
address that made a connection to the infected
host. With this information, an attacker can position
themselves between the communication of two or
more networked devices to steal additional data or
manipulate transmitted data.

© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com

page 34

2023YEAR IN REVIEWCommodity loaders

In a trend that began in 2022 and continued throughout 2023, adversaries using
commodity loaders repeatedly changed their TTPs in response to new Microsoft security
updates. In November 2022, Microsoft issued two patches to detect and block macros-
enabled content within container files, such as ZIP and LNK, which had been a popular
method for surreptitiously using macros. Just a few weeks later, we observed a surge
in threat actors, including those using Qakbot, Emotet and IcedID using OneNote file
attachments to deploy malware. While using OneNote to deliver malware was not a new
technique, it facilitated delivery of macros-enabled documents without being detected,
which is highly favorable among affiliates wishing to bypass AV detection (Figure 21).

Then in January, Microsoft quietly issued an update, so all macros-enabled documents
embedded within OneNote files would be blocked by default, meaning the user would
receive a security warning when opening a OneNote attachment embedded with macros.
We still saw threat actors using OneNote, but with crafty social engineering techniques
that manipulated victims into ignoring the warnings. In one observed campaign deploying
IcedID, the threat actor used a DocuSign lure to trick the victim into clicking a button with
an embedded link. The “Decrypt and View Message” button actually contained a malicious
HTML Application (HTA) file (Figure 22). When opened, the HTA file was dropped into the
OneNote directory for execution.

FIGURE 21

Sample infection chain using OneNote with an embedded macro-enabled file to deliver malware

FIGURE 22

Sample infection chain attempting to manipulate victims into ignoring a security alert

page 35

2023YEAR IN REVIEWCommodity loaders

FIGURE 23

Sample infection chains that do not rely on macros

FIGURE 24

Emotet infection chain using binary padding

Finally, in April 2023, Microsoft issued another update
that blocked users from opening files with a potentially
dangerous extension embedded in OneNote. To open an
attachment marked as potentially dangerous, OneNote
users would need to save the file to their device and open
it from there, allowing security applications running on the
device to detect any malicious code in the attachment. This
latest update caused many operators to abandon OneNote
as a method to hide the use of macros. Instead, we
observed actors turning to filetypes that execute malware
without relying on macros, such as JavaScript files which
rely on LoLBins for execution (Figure 23).

Aside from OneNote, threat actors also experimented with
other methods of deploying malware that did not rely on
macros or could use macros without detection. Since at
least December 2022, we have observed threat actors co-
opting the Google Ads platform to deploy malware such
as Ursnif, IcedID, and Trickbot, a method that completely
avoids using macros. The attack chain in these campaigns
begins with a user entering a search term for a software
or service in the Google search engine. Once Google’s
results page loads, the malicious ads will typically be first in
the list of results, as the actors have been observed using

search engine optimization (SEO) to increase visibility. If
the user clicks on the malicious ad, a Google Ad services
URL will be generated, which then generates a secondary
URL that leads the user to the malicious, spoofed domain
with download links that deliver the various threats. Talos
observed legitimate software products spoofed in these
campaigns, such as Microsoft Teams and WhatsApp, and
popular password managers like 1Password. Threat actors’
use of Google Ads and Google Search makes their lures
appear highly legitimate, as users are probably less likely to
question the authenticity of paid advertisements prioritized
at the top of their search results.

While many affiliates introduced new TTPs in 2023 in
response to evolving security updates, we also observed
commodity loaders using older methods. For example,
Emotet, IcedID, and Ursnif were all observed using macros-
enabled Office documents in the initial infection chain.
Furthermore, we observed Emotet being delivered in
phishing emails with old “RedDawn” templates first seen in
2020 (Figure 24). While these operators may be capable
of more sophisticated attacks, it’s possible they have
still found success using older TTPs, especially against
unpatched, enterprise legacy systems.

© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com

page 36

2023YEAR IN REVIEWFIGURE 25

World map of regions impacted by commodity, from most to least targeted

Commodity loaders

Top five commodity
loaders are similarly
deployed against
sectors globally in
mass opportunistic
campaigns

In 2023, we observed all five commodity
loaders impacting businesses worldwide,
primarily affecting North America and
Europe (Figure 25). These geographical
targets do not necessarily reflect a
coordinated preference among operators
because the threats are sold as a
malware-as-a-service (MaaS). Therefore,
patterns in targeting are aligned with
whatever group is executing the campaign
and can vary.

We predominantly observed mass
spam campaigns that opportunistically
attempted to compromise vulnerable
targets, likely with the intent to move
laterally towards a more hardened target
after the initial infection. Adversaries

will typically tailor phishing lures for the
targeted geography. For example, in
2023, we observed Ursnif predominantly
deployed against businesses located
in the U.S. and Italy in mass “spray
and pray” spam campaigns using the
languages of the targeted countries.

We have observed loaders primarily
deployed against businesses, as opposed
to targeting individuals’ financial data, a
shift that occurred as the malware was
less frequently used as banking trojans.
This is reflected in the phishing lures we
observed. For example, in late-March,
we saw an uptick in Emotet targeting U.S.
businesses that pay quarterly taxes. The
lures used themes related to the Internal
Revenue Service (IRS) with subject lines
such as “IRS Tax Forms W-9,” which
was also seen last year at the end of
the November 2022 business quarter.
W-9 forms are typically distributed by
companies or financial institutions to
their employees.

© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com

page 37

2023YEAR IN REVIEWCommodity loaders

FIGURE 26

Trickbot activity over time

Threats from commodity
loaders can persist
long after their botnets
are dismantled

In August 2023, the prolific Qakbot commodity
loader was disrupted in a major global law
enforcement operation, but dismantling
botnet infrastructure does not always mean
cybercriminals cease to operate. Going forward,
it’s possible Qakbot may reemerge after a
several-month hiatus — as we have seen in similar
scenarios involving other loaders like Emotet —
further underscoring the need to monitor and
report on this threat. Notably, the threat actors
behind Qakbot were not apprehended during the
global takedown, and our latest findings indicate

they are still active—albeit delivering different
threats – leaving open the possibility that they
rebuilt the Qakbot botnet or rebrand themselves
under a different name.

We have seen other malware developers
also continuing to operate in the cyber threat
landscape after their botnets were dismantled.
For example, even after Trickbot took down its
infrastructure in February 2022, the U.S. and UK
still sanctioned the developers in February and
September 2023, implying they are still active
in the cyber threat landscape. The developers
may have chosen to create other types of
malware, or work with other groups they have
had longstanding relations with, such as Emotet
and Conti. In 2022, a series of leaks revealed
close professional relations between developers
of Trickbot and Conti and in 2021, Trickbot lent

portions of its infrastructure to help rebuild the
Emotet botnet.

in the charts above by a more dramatic spike or
irregular patterns.

Even if threat actors opt to cease cybercriminal
activity, we may still observe zombie activity from
infected Qakbot devices. We have seen this from
Trickbot, where our telemetry picked up activity
throughout 2023 even though their infrastructure
was dismantled in February 2022. This is
likely due to old infections that have yet to be
remediated or threat actors leveraging previously
compromised infrastructure. Looking at Trickbot
activity over the past year, we can see it hovered
around the same median number, supporting our
assessment that the botnet is still active in some
capacity, but the developers are not actively
engaged in growing the botnet (Figure 26).
Any new campaigns or infrastructure, such as
IPs or C2 servers, would likely be represented

Meanwhile there are always new commodity
loaders to replace formerly prolific botnets like
Qakbot and Trickbot. For example, IcedID may
be a logical choice to fill the void left by Qakbot.
There is a historical precedence, as IcedID
attracted affiliates after Emotet was dismantled
in 2021. Furthermore, many Qakbot affiliates
are likely already familiar with IcedID because
there are numerous instances of the two being
deployed together as part of the same campaign.
Finally, the recent advanced IcedID update shows
the developers are capable of, and motivated to,
maintain a high-quality product.

© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com

page 38

2023YEAR IN REVIEW