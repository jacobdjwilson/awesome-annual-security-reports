# X-Force Threat Intelligence Index 2023

## Table of Contents
- [Executive summary](#executive-summary)
- [Report highlights](#report-highlights)
- [Key stats](#key-stats)
- [Top initial access vectors](#top-initial-access-vectors)
- [Top actions on objectives](#top-actions-on-objectives)
- [Top impacts](#top-impacts)
- [Cyber-related developments of Russia’s war in Ukraine](#cyber-related-developments-of-russias-war-in-ukraine)
- [The malware landscape](#the-malware-landscape)
- [Threats to OT and industrial control systems](#threats-to-ot-and-industrial-control-systems)
- [Geographic trends](#geographic-trends)
- [Industry trends](#industry-trends)
- [Recommendations](#recommendations)
- [About us](#about-us)
- [Contributors](#contributors)
- [Appendix](#appendix)

---

## Executive summary

The year 2022 was another tumultuous one for cybersecurity. While there was no shortage of contributing events, among the most significant were the continuing effects of the pandemic and the eruption of the military conflict in Ukraine. Disruption made 2022 a year of economic, geopolitical and human upheaval and cost—creating exactly the kind of chaos in which cybercriminals thrive.

And thrive they did.

IBM Security® X-Force® witnessed opportunistic threat actors who capitalize on disorder, using the landscape to their advantage to infiltrate governments and organizations across the globe.

The IBM Security X-Force Threat Intelligence Index 2023 tracks new and existing trends and attack patterns and includes billions of datapoints ranging from network and endpoint devices, incident response (IR) engagements, vulnerability and exploit databases and more. This report is a comprehensive collection of our research data from January to December 2022.

We provide these findings as a resource to IBM clients, cybersecurity researchers, policymakers, the media and the larger community of security industry professionals and industry leaders. Today’s volatile landscape, with its increasingly sophisticated and malicious threats, requires a collaborative effort to protect business and citizens. More than ever, you need to be armed with threat intelligence and security insights to stay ahead of attackers and fortify your critical assets.

So you too can thrive.

### How our data analysis changed for 2022

In 2022, we modified how we examined portions of our data. The changes allow us to offer more insightful analysis and align more closely to industry standard frameworks. That, in turn, enables you to make more informed security decisions and better protect your organization from threats.

Changes to our analysis in 2022 included:

- **Initial access vectors**: Adopting the MITRE ATT&CK framework to track initial access vectors more closely aligns our research findings with the broader cybersecurity industry and allows us to identify important trends at the technique level.
- **Exploits and zero day compromises**: Extrapolating from our robust vulnerability database—which includes nearly 30 years of data—helps lend context to our analysis and identify the actual threat posed by vulnerabilities. This process also lends context to the diminishing proportion of weaponizable exploits and impactful zero days.
- **Threat actor methods and their impact**: Uncoupling the steps threat actors take during an attack from the actual impact of an incident allowed us to identify critical stages of an incident. This process, in turn, uncovered areas that responders should be prepared to handle in the aftermath of an incident.

---

## Report highlights

**Top actions on objectives observed**: In almost one-quarter of all incidents remediated in 2022, the deployment of backdoors at 21% was the top action on objective. Notably, an early year spike in Emotet, a multipurpose malware, contributed significantly to the jump in backdoor activity observed year over year. Despite this spike in backdoor activity, ransomware, which held the top spot since at least 2020, constituted a large share of the incidents at 17%, reinforcing the enduring threat this malware poses.

**Extortion was the most common attack impact on organizations**: At 27%, extortion was the clear impact of choice by threat actors. Victims in manufacturing accounted for 30% of incidents that resulted in extortion, as cybercriminals continued the trend of exploiting a strained industry.

**Phishing was the top initial access vector**: Phishing remains the leading infection vector, identified in 41% of incidents, followed by exploitation of public-facing applications in 26%. Infections by malicious macros have fallen out of favor, likely due to Microsoft’s decision to block macros by default. Malicious ISO and LNK files use escalated as the primary tactic to deliver malware through spam in 2022.

**Increase in hacktivism and destructive malware**: Russia’s war in Ukraine opened the door to what many in the cybersecurity community expected to be a showcase of how cyber enables modern warfare. Although the direst cyberspace predictions haven’t come to fruition as of this publication, there was a notable resurgence of hacktivism and destructive malware. X-Force also observed unprecedented shifts in the cybercriminal world with increased cooperation between cybercriminal groups, and Trickbot gangs targeting Ukrainian organizations.

---

## Key stats

![Infographic showing 27% of attacks with extortion, 21% share of incidents that saw backdoors deployed, and 17% ransomware’s share of attacks.]

- **41%**: Percentage of incidents involving phishing for initial access.
- **100%**: Increase in the number of thread hijacking attempts per month.
- **52%**: Drop in reported phishing kits seeking credit card data.
- **62%**: Percentage of phishing attacks using spear phishing attachments.
- **26%**: Share of 2022 vulnerabilities with known exploits.
- **31%**: Share of global attacks that targeted the Asia-Pacific region.

---

## Top initial access vectors

In 2022, X-Force moved from tracking initial access vectors as broader categories to the initial access techniques listed within the MITRE ATT&CK Matrix for Enterprise framework.

![Figure 1: Top initial access vectors X-Force observed in 2022.]

### Phishing
Phishing (T1566), whether through attachment, link or as a service, remains the lead infection vector, which comprised 41% of all incidents remediated by X-Force in 2022.

![Figure 2: Types of phishing subtechniques as a percentage of total phishing cases observed by X-Force in 2022.]

### Phishing kits lasting longer, targeting PII over credit card data
IBM Security analyzed thousands of phishing kits from around the world and discovered that the lifespan of phishing kits observed has more than doubled year over year.

- Credit card information dropped significantly from being targeted 61% of the time in 2021 to 29% of phishing kits in 2022.
- Almost every reported phishing kit analyzed sought to gather names at 98%.

### Top spoofed brands
![Figure 3: Top spoofed brands in 2021 and 2022.]

### Vulnerabilities
Vulnerability exploitation—captured for 2022 as exploitation of public-facing applications (T1190)—placed second among top infection vectors.

![Figure 4: X-Force vulnerability database view showing vulnerabilities and exploits over the past five years.]

---

## Top actions on objectives

For 2022, X-Force dissected attack classifications into two distinct categories: the specific actions threat actors took on victim networks (adversary action on objective) and the intended or realized effect (impact).

![Figure 7: Top actions on objectives observed by X-Force in 2022.]

### Ransomware
Even amid a chaotic year for some of the most prolific ransomware syndicates, ransomware was the second most common action on objective. An IBM Security X-Force study revealed there was a 94% reduction in the average time for the deployment of ransomware attacks. What took attackers over two months in 2019 took just under four days in 2021.

---

## Top impacts

The analysis found that more than one in four incidents aimed to extort victim organizations—making it the top impact observed across incidents remediated by X-Force.

![Figure 10: Top impacts X-Force observed in incident response engagements in 2022.]

---

## Cyber-related developments of Russia’s war in Ukraine

Russian state-sponsored cyber activity following Russia’s invasion of Ukraine has not, as of this publication, resulted in the widespread and high-impact attacks originally feared by Western government entities. However, Russia has deployed an unprecedented number of wipers against targets in Ukraine.

![Figure 12: Timeline of select hacktivist events 2022.]

---

## The malware landscape

### Increase in USB-spreading worms
After X-Force observed Raspberry Robin infection attempts impacting organizations in mid-May 2022, the enigmatic worm began spreading quickly within victims’ networks from users sharing Universal Serial Bus (USB) devices.

### Rust rises
The Rust Programming Language steadily increased in popularity among malware developers during 2022, thanks to its cross-platform support and low antivirus detection rates.

---

## Threats to OT and industrial control systems

2022 saw the discovery of two new OT-specific pieces of malware, Industroyer2 and INCONTROLLER (also known as PIPEDREAM), and the disclosure of many OT vulnerabilities called OT:ICEFALL.

![Figure 14: Proportion of IR cases by OT-related industry to which X-Force responded in 2022.]

---

## Geographic trends

For the second year in a row, the Asia-Pacific region holds the top spot as the most-attacked region in 2022, accounting for 31% of the incidents to which X-Force IR responded.

![Figure 15: Proportion of IR cases by region to which X-Force responded from 2020-2022.]

---

## Recommendations

[Content omitted in source text]

---

## About us

[Content omitted in source text]

---

## Contributors

[Content omitted in source text]

---

## Appendix

[Content omitted in source text]

[^1]: Footnote content here.

---

ns was the top infection vector
used against European organizations,
accounting for 32% of all incidents that
X-Force remediated in the region, several
of which led to ransomware infections.
Abuse of valid local accounts came in
second place at 18%, with spear phishing

links following at 14%, notably down
from 42% in 2021. This decrease in spear
phishing links may be a result of better
user awareness, stronger email security
defenses or more effective defenses
catching malware after installation.

Professional, business and consumer
services tied with finance and insurance
for the most-attacked industry, each
ranking 25% of the cases to which X-Force
responded. Manufacturing placed second
with 12% of cases, and energy and
healthcare tied for third place at 10%.

The United Kingdom was the most
attacked country in Europe, accounting
for 43% of cases. Germany accounted for
14%, Portugal 9%, Italy 8%, and France
7%. “X-Force also responded to smaller
numbers of cases in Norway, Denmark,
Switzerland, Austria, Greece, Greenland,
Spain, and Serbia.

Previous chapter

Next chapter

3838

10

Geographic trends

North America’s most
commonly attacked
organizations were energy
firms at 20% of cases.

#3 | North America

X-Force observed a slight increase in the
number of incidents in North America,
moving from 23% of all cases in 2021 to
25% in 2022.

Energy firms rose to the top of the victim
list in North America, constituting 20% of
all attacks to which X-Force responded
in 2022. Manufacturing and the retail-
wholesale sector tied for second place
in 14% of cases each. While retail-
wholesale held a similar position in
2021, the numbers for manufacturing
represented a 50% decline from 2021.
Professional, business and consumer
services took third place in 2022 at 12%,
amid a rise in ransomware and other
malware-related cases.

The top identified infection vectors were
exploitation of public-facing applications
at 35% and spear phishing attachments

at 20%. Ransomware incidents accounted
for 23% of cases, a few of which were the
result of detections of lingering infections
of WannaCry or Ryuk dating back to 2018
or 2019, highlighting the importance of
proper cleanup after such events. In the
region, 12% of cases were botnets, with
backdoors and BEC tying for third place at
10% each.

When looking at the top impact threat
actors had, credential harvesting took
the pole position at 25% of incidents that
X-Force remediated in North America. Data
leak and data theft tied for second place
at 17% each, with extortion accounting for
13% of cases.

The United States accounted for 80%
of the region’s attacks compared to
Canada’s 20%.

Previous chapter

Next chapter

3939

10

Geographic trends

In Latin America, Brazil
accounted for 67% of cases to
which X-Force responded.

#4 | Latin America

For the purposes of reporting, IBM
considers Latin America to include Mexico,
Central America and South America.

Incidents in Latin America bucked global
trends, returning retail-wholesale as the
most-attacked industry at 28% of cases
that X-Force remediated, and moved up
from second place in 2021. The finance and
insurance industry was the second-most
targeted with 24% of cases, followed by
energy at 20%.

Ransomware outstripped other attacks in
Latin America, accounting for 32% of cases
to which X-Force responded. Deployment
of backdoors was the second-most
identified action on objective at 16%,
while BEC and email thread hijacking

tied for third place at 11% each. Extortion
and data theft were the most commonly
seen impacts in the region at 27% of cases,
with financial loss at 20%. Data destruction
and leaks tied for third place at 13% of
cases each.

Top initial access vectors included external
remote services at 30% and exploitation of
public-facing applications at 20%. Drive-
by compromise, hardware additions, valid
domain accounts, valid local accounts and
spear phishing attachments accounted for
10% each.

In all the cases that X-Force responded to
in Latin America, Brazil accounted for 67%,
Colombia 17% and Mexico 8%. Peru and
Chile split the remaining 8%.

Previous chapter

Next chapter

4040

10

Geographic trends

#5 | Middle East and Africa

For the purpose of reporting, IBM considers
the Middle East and Africa to include the
Levant, Arabian Peninsula, Egypt, Iran and
Iraq, and the entire African continent.

Deployment of backdoors was detected in
27% of cases to which X-Force responded
in this region in 2022. Ransomware and
worms tied for the second-most common
attack type at 18% each. Extortion and
financial loss each accounted for half of
identified impacts in incidents across the
region in 2021.

Spear phishing links were used for
initial access in two-thirds of cases,
and removable media accounted for the

other third of the incidents that X-Force
remediated in the Middle East and Africa.
Finance and insurance was the most-
targeted industry in the Middle East and
Africa in 2022, accounting for 44% of
incidents and down slightly from 2021 at
48%. Professional, business and consumer
services accounted for 22% of attacks, with
manufacturing and energy tying for third
place at 11%.

Saudi Arabia comprised two-thirds of
the cases in the region to which X-Force
responded. The remaining cases were split
between Qatar, United Arab Emirates and
South Africa.

The most common attack in
this region was deployment of
backdoors at 27% of cases.

Previous chapter

Next chapter

4141

11

Industry trends

For the second year in a row, manufacturing
was the top-attacked industry, according
to X-Force incident response data. Finance
and insurance lost the top spot by just one
percentage point in 2021—after holding
the title for five consecutive years—and is
in second place again in 2022 by a larger
margin of nearly six percentage points.

Share of attacks by industry 2018 – 2022

Industry

2022

2021

2020

2019

2018

Manufacturing

24.8%

23.2

17.7

Finance and insurance

18.9%

22.4

Professional, business and
consumer services

14.6%

12.7

Energy

10.7%

8.2

Retail and wholesale

Education

Healthcare

Government

8.7%

7.3%

5.8%

4.8%

7.3

2.8

5.1

2.8

Transportation

3.9%

4

Media and telecom

0.5%

2.5

23

8.7

11.1

10.2

4

6.6

7.9

5.1

5.7

8

17

10

6

16

8

3

8

13

10

10

19

12

6

11

6

6

8

13

8

Previous chapter

Next chapter

4242

11

Industry trends

24.8%
of X-Force incident response
cases occurred in the
manufacturing sector.

#1 | Manufacturing

Manufacturing was the top-attacked
industry and by a slightly larger margin
compared to 2021. In 2022, backdoors
were deployed in 28% of incidents, beating
out ransomware, which appeared in 23%
of incidents remediated by X-Force. The
percentage of backdoor deployments also
was driven by the Emotet infection spike.
Some of these cases could have led to
ransomware attacks, among other more
malicious activity, but they were identified
early enough to be remediated.

Spear phishing attachments and
exploitation of public-facing applications
tied for the top two infection vectors
at 28% each. External remote services
came in second place at 14%, with spear

phishing links and valid default accounts
tied for third place as the initial access in
10% of cases.

Extortion was the leading impact to
manufacturing organizations, seen in 32%
of cases. Manufacturers notoriously have
little-to-no tolerance for downtime, and
this intolerance makes extortion a lucrative
strategy for attackers. Data theft was the
second-most common at 19% of incidents,
followed by data leaks at 16%. The Asia-
Pacific region saw the most incidents in
manufacturing in approximately 61% of
cases. Europe and North America tied for
second place at 14%, Latin American at 8%
and the Middle East and Africa at 4%.

Previous chapter

Next chapter

4343

11

Industry trends

18.9%
of X-Force incident response
cases occurred in the finance
and insurance sector.

#2 | Finance and insurance

Finance and insurance organizations made
up less than one in five attacks to which
X-Force responded in 2022, earning it
second place. This percentage indicated a
slight decrease over the past few years as
other industries began to gain the attention
of attackers, particularly manufacturing.

Finance and insurance organizations
tend to be further along in both digital
transformations and cloud adoption
progress relative to other industries. As a
result, attackers may need to work harder
to successfully execute attacks against
these organizations.

Backdoor attacks were the most commonly
observed action on objective at 29%,

followed by ransomware and maldocs at
11% each. The top infection vector was
spear phishing attachments, used in 53%
of attacks against this sector. Exploitation
of public-facing applications came in
second place at 18% of attacks, and spear
phishing links were the initial access vector
at 12% of cases.

Europe saw the highest volume of attacks
on finance and insurance organizations
with approximately 33% of all attacks,
with Asia-Pacific a close second place
at approximately 31%. Latin America
experienced approximately 15% of
incidents to which X-Force responded,
with North America and the Middle East
and Africa experiencing approximately
10%  each.

Previous chapter

Next chapter

4444

11

Industry trends

14.6%
of X-Force incident response
cases occurred in the
professional, business and
consumer services sector.

#3 | Professional, business
and consumer services

The professional services industry
includes consultancies, management
companies and law firms. These services
make up 52% of victims in this segment.
Business services, by contrast, include
firms, such as IT and technology
services, public relations, advertising
and communications. These services
represent 37% of victims. Consumer
services, encompassing home builders, real
estate, arts, entertainment and recreation,
accounted for 11% of cases. Together,
they form the professional, business and
consumer services category of the 2023
X-Force Threat Intelligence Index.

Professional, business and consumer
services experienced ransomware and
backdoor attacks most frequently in 18% of
cases each. The top two infection vectors
were the exploitation of public-facing
applications and external remote services
at 23% each. Spear phishing attachments
and valid local accounts were the cause of
15% of cases each.

Extortion was the most common impact in
28% of cases, with data theft, credential
harvesting and data leaks at 17% each.
X-Force responded to 47% of cases in
Europe, 33% in North America, 10% in
Asia-Pacific, 7% in the Middle East and
Africa, and 3% in Latin America.

Previous chapter

Next chapter

4545

11

Industry trends

10.7%
of X-Force incident response
cases occurred in the
energy sector.

#4 | Energy

Energy organizations, including electric
utilities and oil and gas companies, were
the fourth-most attacked industry—the
same as 2021—representing 10.7% of
attacks. The exploitation of a public-facing
application was the most common infection
vector at 40%. Spear phishing links and
external remote services accounted for
20% of cases each. Botnets were the most
frequent action on objective in 19% of
cases, with ransomware and BEC tying
for second place at 15%.

Data theft and extortion were noted in 23%
of cases, followed by credential harvesting
and botnet infections at 15% each. In
all the cases that X-Force responded to
worldwide, North American organizations
were the most common victims at 46%,
compared to Europe and Latin America
at 23% each, and just under 5% in Asia-
Pacific and the Middle East and Africa.

The energy industry remains under
pressure from a variety of global forces,
especially those exacerbated by Russia’s
war in Ukraine and how that has affected
an already tumultuous global energy trade.

Previous chapter

Next chapter

4646

11

Industry trends

8.7%
of X-Force incident response
cases occurred in the retail
and wholesale sector.

#5 | Retail and wholesale

Retailers are responsible for the sale of
goods to consumers and wholesalers.
Wholesalers are typically responsible for
the transportation and distribution of these
goods directly from manufacturers to
retailers or directly to consumers. The retail
and wholesale industry was the fifth-most
targeted industry, according to X-Force IR
data, the same as its 2021 ranking.

The most common initial access vector
in attacks on retail and wholesale was
spear phishing emails with a malicious link
at 33%. Compromised external remote

services, spear phishing with malicious
attachments and hardware additions
accounted for 17% each.

Ransomware, backdoors and BEC were the
most common actions taken by attackers,
each comprising 19% of activities. Worms
were identified in 10% of cases. Victims
experienced extortion in 50% of cases,
and credential harvesting and financial
loss at 25% each. North America and Latin
America experienced the most cases at
39% each, compared to Europe’s 22%.

Previous chapter

Next chapter

4747

11

Industry trends

7.3%
of X-Force incident response
cases occurred in the
education sector.

#6 | Education

Incidents in education involved backdoor
cases in 20% of attacks to which X-Force
responded. Ransomware, adware and
spam accounted for 13% each. Exploitation
of public-facing applications was the
most commonly observed initial access in
42% of cases, followed by spear phishing
attachments at 25%. Phishing through
service, through link and valid cloud and
local account abuse comprised 8% of
initial access vectors each. Data theft, data
leak, extortion and reconnaissance were
the impacts at 25% each. Asia-Pacific
accounted for 67% of cases, North America
for 27% and Latin America for 6%.

Previous chapter

Next chapter

4848

11

Industry trends

5.8%
of X-Force incident response
cases occurred in the
healthcare sector.

#7 | Healthcare

Healthcare dropped back to seventh
place among the top 10 industries,
further declining from sixth in 2021. The
proportion of healthcare cases to which
X-Force has responded has remained
at approximately 5%-6% for the last
three years. Backdoor attacks occurred
in 27% of cases, and web shells in 18%.
Adware, BEC, cryptominers, loaders,
reconnaissance and scanning tools, and
remote access tools comprised 9% each.
Reconnaissance comprised most of the
observed impacts at 50%, while data theft
and digital currency mining were identified
in 25% of cases each.

European-based targets accounted for 58%
of incidents, with North American cases
comprising the remainder at 42%.

Previous chapter

Next chapter

4949

11

Industry trends

4.8%
of X-Force incident response
cases occurred in the
government sector.

#8 | Government

Government targets were another top
target of backdoors, comprising 25% of
X-Force IR cases. This percentage tied
with DDoS attacks, which also accounted
for one-quarter of cases. The rich sensitive
information in public sector networks
is a common target of cyber espionage
campaigns. This information can include
extensive databases of PII and other
information that could be used by state-
sponsored groups or sold for profit by
cybercriminals. Maldocs were identified in
17% of cases, and cryptominers, credential
acquisition tools, ransomware and web
shells split the remainder of cases at 83%.

Of the cases in this sector, X-Force was
able to tie incidents to cybercriminals,
insider threats that led to data destruction,
hacktivists and state-sponsored threat
groups conducting espionage, each in
equal proportion.

Exploitation of public-facing applications
and spear phishing attachments were the
lead infection vectors at 40% each, while
abuse of valid default accounts comprised
20%. Government entities in Asia-Pacific
were the most targeted at 50% of cases,
with Europe at 30% and North America
at 20%.

Previous chapter

Next chapter

5050

11

Industry trends

3.9%
of X-Force incident response
cases occurred in the
transportation sector.

#9 | Transportation

Down from seventh place in 2021,
transportation returned to its 2020 ranking
of ninth place. However, the industry still
comprised roughly the same percentage
of incidents to which X-Force responded.
Phishing was the most common initial
access vector in 51% of cases—evenly
split between links, attachments and spear
phishing as a service. Abuse of valid local
accounts made up 33% of initial access
vectors, with valid cloud accounts serving
as the entry point for 17% of cases. The top
actions on objectives were server access

and deployment of remote access tools at
25% each, followed by spam campaigns,
ransomware, backdoors and defacement in
13% of cases each.

Data theft was most common in 50%
of cases, with extortion and impacts to
brand reputation at 25% each. European
transportation entities were the most
targeted group, comprising 62% of cases,
with Asia-Pacific in second place at just
over 37%.

Previous chapter

Next chapter

5151

11

Industry trends

0.5%
of X-Force incident response
cases occurred in the
media and telecom sector.

#10 | Media and telecom

Media and telecommunications accounted
for a small fraction of incidents to which
X-Force responded, coming in last place
for the second year running. Abuse of
external remote services, such as VPNs
and other access mechanisms, and valid
domain accounts were the observed
infection vectors. These vectors led to
ransomware attacks. The actions observed
in these cases included deployment of
ransomware and data exfiltration tools.
These actions, in turn, led to data theft,
leak, destruction and extortion.

Previous chapter

Next chapter

5252

12

Recommendations

The following recommendations are actions
you should take to secure your organization
against malicious threats, including those
presented in this report.

Manage your assets: “What do we have?
What are we defending? What data is
critical to our business?” These are the first
questions any security team should answer
to build a successful defense. Prioritizing
discovery of assets on your perimeter,
understanding your exposure to phishing
attacks and reducing those attack surfaces
further contribute to holistic security.
Finally, organizations must extend their
asset management programs to include
source code, credentials and other data
that could already exist on the internet or
dark web.

Know your adversary: While many
organizations have a broad view of the
threat landscape, X-Force recommends
organizations adopt a view that emphasizes
the specific threat actors that are most
likely to target your industry, organization
and geography. This perspective includes
understanding how threat actors operate,
identifying their level of sophistication, and
knowing which tactics, techniques
and procedures attackers are most likely
to employ.

Manage visibility: After understanding
more about the adversaries most likely to
attack, organizations must confirm they
have appropriate visibility into the data
sources that would indicate an attacker’s
presence. Maintaining visibility at key
points throughout the enterprise and
ensuring alerts are generated and acted on
in a timely manner are critical to stopping
attackers before they can cause disruption.

Previous chapter

Next chapter

53
53

12

Recommendations

Challenge assumptions: Organizations
must assume that they already have been
compromised. By doing so, teams can
continually reexamine the following:

 – How attackers can infiltrate their

systems

 – How well their detection and

response capabilities fare against
emerging tactics, techniques
and procedures

 – The level of difficulty for a likely

adversary to compromise your most
critical data and systems

The most successful security teams
perform regular offensive testing including
threat hunting, penetration testing and
objective-based red teaming to detect or
validate opportunistic attack paths into
their environments.

Act on intelligence: Apply threat
intelligence everywhere. Effective
application of threat intelligence will
enable you to analyze common attack
paths and identify key opportunities for
mitigating common attacks, in addition
to helping develop high-fidelity detection
opportunities. Application of threat
intelligence should be coupled with
understanding your adversaries and how
they operate.

Be prepared: Attacks are inevitable;
failure doesn’t have to be. Organizations
should develop incident response plans
customized for their environment. Those
plans should be regularly drilled and
modified as the organization changes, with
a focus on improving response, remediation
and recovery time.

Having a reputable IR vendor on retainer
reduces the amount of time it takes to get
skilled responders focused on mitigating
an attack. Additionally, including your IR
vendor in response plan development and
testing is critical and contributes to a more
effective and efficient response. The best
IR plans include a cross-organizational
response, incorporate stakeholders outside
of IT and test lines of communication
between technical teams and senior
leadership. Finally, testing your plan in
an immersive, high-pressure cyber range
exercise can greatly enhance your ability to
respond to an attack.

Boost security with
these actions:

  Manage your assets

Know your adversary

  Manage visibility

Challenge assumptions

Act on intelligence

  Be prepared

Previous chapter

Next chapter

54
54

13

About us

IBM Security X-Force

IBM Security X-Force is a threat-centric
team of hackers, responders, researchers
and analysts. The X-Force portfolio includes
offensive and defensive products and
services, fueled by a 360-degree view
of threats.

In an age of relentless cyberattacks, a
connected everything and increasing
regulatory mandates, organizations need
a focused security approach. X-Force
believes the threat should be the focal
point. Through penetration testing,
vulnerability management and adversary
simulation services, the X-Force Red team
of hackers assumes the role of threat actors
to find security vulnerabilities—exposing
your most important assets. Through
incident preparedness, detection and

response and crisis management services,
the X-Force Incident Response team knows
where threats may hide and how to stop
them. X-Force researchers create offensive
techniques for detecting and preventing
threats, while analysts with X-Force collect
and translate threat data into actionable
information for reducing risk.

With a deep understanding of how threat
actors think, strategize and strike, X-Force
can help you prevent, detect, respond to
and recover from incidents and focus on
business priorities.

If your organization would like support
strengthening your security posture,
schedule a one-on-one consultation with
an IBM Security X-Force expert.

Schedule a consult

IBM Security

IBM Security adapts to your ever-
expanding footprint and works in step
with you to keep you on the right track. We
help you ensure that you’re always staying
one step ahead—with greater speed and
greater accuracy—with our dynamic AI and
automation capabilities. Feel confident that
you’re making the right moves today and
tomorrow with insights from our trusted
team of industry-leading experts. From
predicting threats to helping to protect
data; working across vendors, or around
the world; no matter where your business
is headed, IBM Security can help you to
strive for ambitious business goals, while
exploring pivotal new technologies and
helping minimize unexpected threats.

Learn more

Previous chapter

Next chapter

5555

14

Contributors

Michael Worley
Christopher Caridi
Michelle Alvarez
Karlina Bakken
Yannick Bedard
Michele Brancati
Christopher Bedell
Joshua Chung
Scott Craig
Joseph DiRe
John Dwyer
Emmy Ebanks
Richard Emerson
Charlotte Hammond
Kevin Henson

Guy-Vincent Jourdan
Scott Lohr
Mitch Mayne
Dave McMillen
Kat Metrick
Scott Moore
Golo Mühr
Vio Onut
Andy Piazza
Johnny Shaieb
Benjamin Shipley
Christopher Thompson
Ole Villadsen
Reginald Wong
John Zorabedian

Previous chapter

Next chapter

56
56

15

Appendix

List of impacts

Impacts

Botnet

Brand reputation

Credential harvesting

Data destruction

Data leak

Data theft

Impacts

Digital currency mining

Espionage

Extortion

Financial loss

Production halted (OT)

Reconnaissance

Previous chapter

5757

1.  “A timeline of the biggest ransomware attacks,”

CNET, 15 November 2021

10. “BazarCall to Conti Ransomware via Trickbot and
Cobalt Strike,” The DFIR Report, 1 August 2021

© Copyright IBM Corporation 2023

2.  “International action against DD4BC cybercriminal

11. “Diavol Ransomware,” The DFIR Report, 13

group,” Europol, 12 January 2016

December 2021

IBM Corporation
New Orchard Road
Armonk, NY 10504

3.  “DD4BC, Armada Collective, and the Rise of Cyber
Extortion,” Recorded Future, 7 December 2015

12. “Quantum Ransomware,” The DFIR Report, 25

April 2022

Produced in the United States of America
February 2023

4.  “A Brief History of Ransomware.” Varonis, 10

November 2015

13. “Bumblebee Loader Linked to Conti and Used In
Quantum Locker Attacks,” Kroll, 6 June 2022

5.  “Inside Chimera Ransomware - the first

14. “This isn't Optimus Prime’s Bumblebee but it’s Still

‘doxingware’ in wild,” MalwardBytes Labs, 8
December 2015

6.  “Big Game Hunting: The Evolution of INDRIK
SPIDER From Dridex Wire Fraud to BitPaymer
Targeted Ransomware,” Crowdstrike, 14 November
2018

7.  “Operators of SamSam Continue to Receive

Significant Ransom Payments,” Crowdstrike, 11
April 2018

Transforming,” Proofpoint, 28 April 2022,

15. “Understanding REvil: REvil Threat Actors May

Have Returned (Updated),” Unit 42, 3 June 2022

16. “AdvIntel’s State of Emotet aka “SpmTools”

Displays Over Million Compromised Machines
Through 2022,” AdvIntel, 13 September 2022

17. “Back in Black: Unlocking a LockBit 3.0

Ransomware Attack,” NCC Group, 19 August 2022

8.  “Triple Extortion Ransomware: The DDoS Flavour,”

18. “Back in Black: Unlocking a LockBit 3.0

PacketLabs, 12 May 2022

Ransomware Attack,” NCC Group, 19 August 2022,

9.  “They Told Their Therapists Everything. Hackers

Leaked It All,” Wired, 4 May 2021

IBM, the IBM logo, IBM Security, and X-Force are
trademarks or registered trademarks of International
Business Machines Corporation, in the United
States and/or other countries. Other product and
service names might be trademarks of IBM or other
companies. A current list of IBM trademarks is
available on ibm.com/trademark.

Microsoft and Windows are trademarks of Microsoft
Corporation in the United States, other countries, or
both.

This document is current as of the initial date of
publication and may be changed by IBM at any time.
Not all offerings are available in every country in which
IBM operates.

THE INFORMATION IN THIS DOCUMENT IS
PROVIDED “AS IS” WITHOUT ANY WARRANTY,
EXPRESS OR IMPLIED, INCLUDING WITHOUT ANY
WARRANTIES OF MERCHANTABILITY, FITNESS FOR
A PARTICULAR PURPOSE AND ANY WARRANTY OR
CONDITION OF NON-INFRINGEMENT. IBM products
are warranted according to the terms and conditions
of the agreements under which they are provided.

Statement of Good Security Practices: No IT system
or product should be considered completely secure,
and no single product, service or security measure
can be completely effective in preventing improper
use or access. IBM does not warrant that any systems,
products or services are immune from, or will make
your enterprise immune from, the malicious or illegal
conduct of any party.

The client is responsible for ensuring compliance with
laws and regulations applicable to it. IBM does not
provide legal advice or represent or warrant that its
services or products will ensure that the client is in
compliance with any law or regulation. Statements
regarding IBM’s future direction and intent are subject
to change or withdrawal without notice, and represent
goals and objectives only.