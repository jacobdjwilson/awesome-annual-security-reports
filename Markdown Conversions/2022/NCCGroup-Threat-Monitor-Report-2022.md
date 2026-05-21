Basta

BlackBasta is a relatively new ransomware
group that emerged in April 2022. Despite
their recent entry into the threat landscape,
they have quickly established themselves
as a significant threat, accounting for 138
attacks (5%) of the total 2,531 observed
in 2022.

Following their emergence in April,
BlackBasta’s activity was relatively
consistent, with a slight increase in
the latter half of the year. Their peak
activity was observed in September, with
23 attacks. This rapid rise in activity
suggests that the group is well-resourced
and likely composed of experienced
operators, potentially originating from
the remnants of the Conti group.

Sectors Targeted
The top three sectors targeted by BlackBasta
were Industrials with 55 attacks (40%),
Consumer Cyclicals with 25 attacks (18%),
and Technology with 14 attacks (10%).

Industry Targeted
The top three industries targeted were
Professional and Commercial Services with
26 attacks (19%), Machinery, Tools, Heavy
Vehicles, Trains and Ships with 14 attacks
(10%), and Construction and Engineering
with 10 attacks (7%).

![Graph showing BlackBasta activity from April to December 2022]

42

2022 NCC Group Annual Threat Monitor

## Regions

In 2022, North America remained the most
targeted region for ransomware attacks,
accounting for 45% of the total incidents.
Europe followed with 32%, and the Asia-
Pacific region accounted for 14%. The
remaining 9% of attacks were distributed
across other regions, including South
America, the Middle East, and Africa.

The dominance of North America and Europe
as primary targets is consistent with previous
years, reflecting the concentration of
high-value targets and the prevalence of
digitally mature economies in these regions.
However, the increasing activity in the
Asia-Pacific region is a trend that warrants
continued monitoring, as threat actors
expand their reach to exploit emerging
markets and less-defended infrastructure.

![Chart showing regional distribution of ransomware attacks]

43

2022 NCC Group Annual Threat Monitor

## DDoS Threat Landscape

The Distributed Denial of Service (DDoS)
threat landscape in 2022 was characterized
by an increase in both the frequency and
the sophistication of attacks. While
ransomware often dominates the headlines,
DDoS attacks remain a potent tool for
disruption, extortion, and as a distraction
for other malicious activities.

Throughout 2022, we observed a shift
towards more complex, multi-vector
attacks that leverage a combination of
volumetric, protocol, and application-layer
techniques. These attacks are designed to
overwhelm target infrastructure while
evading traditional mitigation measures.

The rise of DDoS-for-hire services, or
"booter" services, has lowered the barrier
to entry for less skilled attackers, leading
to a proliferation of smaller, yet frequent,
disruptive attacks. Conversely, state-
sponsored actors and sophisticated
criminal groups have continued to deploy
large-scale, high-impact attacks against
critical infrastructure and high-profile
targets.

44

2022 NCC Group Annual Threat Monitor

## Geography

The geographical distribution of DDoS
attacks in 2022 mirrored the broader
cyber threat landscape, with a heavy
concentration of attacks targeting
organizations in North America and
Europe. These regions are home to a
significant portion of the world's critical
infrastructure, financial institutions, and
technology providers, making them
attractive targets for disruption.

However, we also observed a notable
increase in DDoS activity targeting
organizations in the Asia-Pacific region,
particularly in countries with rapidly
growing digital economies. This trend
suggests that threat actors are increasingly
targeting regions where digital adoption
is outpacing the implementation of robust
DDoS mitigation strategies.

![Map showing global DDoS attack distribution]

45

2022 NCC Group Annual Threat Monitor

## Attack Durations

In 2022, the duration of DDoS attacks
varied significantly, ranging from short-
lived, "bursty" attacks lasting only a few
minutes to prolonged, sustained campaigns
that lasted for days or even weeks.

Short-duration attacks are often used
to test the target's defenses or to
cause intermittent disruption, making
them difficult to detect and mitigate
effectively. These attacks are frequently
automated and can be launched in rapid
succession, creating a persistent state of
instability for the target.

Long-duration attacks, on the other hand,
are typically aimed at causing maximum
disruption and are often used as a
smokescreen for other malicious activities,
such as data exfiltration or the deployment
of ransomware. These attacks require
significant resources and coordination,
indicating a higher level of sophistication
on the part of the attacker.

46

2022 NCC Group Annual Threat Monitor

## Exploited Protocols

The protocols exploited in DDoS attacks
in 2022 remained consistent with
historical trends, with a heavy reliance
on reflection and amplification techniques.
These techniques allow attackers to
generate massive volumes of traffic
using a relatively small number of
compromised devices.

Commonly exploited protocols include:

- **DNS (Domain Name System)**: Used for
  reflection and amplification attacks,
  leveraging the large response sizes
  associated with DNS queries.
- **NTP (Network Time Protocol)**: Another
  popular protocol for amplification
  attacks due to its widespread use and
  vulnerability to abuse.
- **CLDAP (Connectionless Lightweight
  Directory Access Protocol)**: Increasingly
  exploited for its high amplification
  factor.
- **Memcached**: While mitigation efforts
  have reduced its prevalence, it remains
  a potent tool for large-scale volumetric
  attacks.

47

2022 NCC Group Annual Threat Monitor

## Conclusion

The 2022 threat landscape was defined by
a convergence of geopolitical instability,
the evolution of criminal business models,
and the persistent exploitation of
vulnerabilities. The conflict between
Russia and Ukraine served as a catalyst
for increased cyber activity, with both
state and non-state actors leveraging
disruptive and destructive techniques.

Ransomware remained the most significant
threat to organizations, with groups
continuing to innovate and adapt to
law enforcement interventions. The
shift towards "hack and leak" tactics
and the targeting of critical infrastructure
highlight the evolving nature of the
extortion landscape.

Looking ahead to 2023, we expect these
trends to persist. Organizations must
prioritize the development of robust
incident response plans, invest in
proactive threat intelligence, and
ensure that their security controls are
tailored to the specific threats they face.
By staying informed and prepared,
organizations can effectively navigate
the complex and ever-changing cyber
threat landscape.

48

2022 NCC Group Annual Threat Monitor

## Vulnerability Landscape

The vulnerability landscape in 2022 was
characterized by the rapid discovery and
weaponization of critical vulnerabilities.
The disclosure of vulnerabilities such as
Spring4Shell and the Confluence RCE
highlighted the speed at which attackers
can move from disclosure to exploitation.

The prevalence of unpatched systems
remains a significant challenge for
organizations. Attackers are increasingly
focusing on public-facing applications
and remote services, where a single
vulnerability can provide a foothold for
lateral movement and data exfiltration.

Furthermore, the rise of "n-day"
vulnerabilities—vulnerabilities for which
a patch is available but not yet applied—
continues to be a major risk factor.
Organizations must prioritize patch
management and vulnerability scanning
to reduce their attack surface and
mitigate the risk of exploitation.

50

2022 NCC Group Annual Threat Monitor

## Ukraine-Russia War

The conflict between Russia and Ukraine
had a profound impact on the cyber
threat landscape in 2022. The use of
wiper malware, such as AcidRain and
HermeticWiper, against Ukrainian
infrastructure demonstrated the
destructive potential of cyber operations
in a kinetic conflict.

Beyond the direct impact on Ukraine,
the conflict also led to an increase in
cyber activity globally. Hacktivist groups
aligned with both sides engaged in
DDoS attacks, website defacements,
and data leaks, further complicating
the threat environment.

The conflict also highlighted the
importance of public-private
partnerships in defending against
state-sponsored cyber threats. The
collaboration between government
agencies, security researchers, and
private sector organizations was
instrumental in identifying and
mitigating the impact of these
malicious activities.

51

2022 NCC Group Annual Threat Monitor

## Threat Spotlight: Hydra Malware

Hydra is a sophisticated credential-
stealing malware that has gained
prominence in 2022. It is primarily
distributed through phishing campaigns
and is designed to harvest sensitive
information from infected systems.

Hydra's capabilities include:

- **Credential Harvesting**: Stealing
  usernames and passwords from web
  browsers, email clients, and other
  applications.
- **Cookie Stealing**: Extracting session
  cookies to bypass multi-factor
  authentication (MFA) and gain
  unauthorized access to accounts.
- **Keylogging**: Recording keystrokes to
  capture sensitive information in real-time.
- **C2 Communication**: Communicating
  with a command-and-control (C2)
  server to receive instructions and
  exfiltrate stolen data.

52

2022 NCC Group Annual Threat Monitor

## Introduction

The emergence of Hydra malware
represents a significant evolution in
credential-stealing threats. Its ability
to bypass traditional security measures,
such as MFA, through cookie theft
makes it a particularly dangerous
threat to organizations.

Hydra is often delivered via malicious
attachments or links in phishing emails,
which are designed to trick users into
executing the malware. Once installed,
it operates stealthily, exfiltrating data
without the user's knowledge.

53

2022 NCC Group Annual Threat Monitor

## Credential-stealing Features

Hydra's credential-stealing features are
highly effective, allowing it to harvest
a wide range of sensitive information.
It targets popular web browsers,
including Chrome, Firefox, and Edge,
extracting stored credentials from their
internal databases.

In addition to browser-based credentials,
Hydra also targets email clients and
other applications that store sensitive
information. Its modular design allows
it to be easily updated with new
capabilities, making it a persistent
and evolving threat.

54

2022 NCC Group Annual Threat Monitor

## New features Stealing Cookies

One of the most concerning features of
Hydra is its ability to steal session
cookies. By extracting these cookies,
attackers can impersonate the user
and gain access to their accounts
without needing to provide a password
or complete an MFA challenge.

This technique is particularly effective
against cloud-based services and
SaaS applications, where session
cookies are used to maintain user
authentication. As organizations
increasingly rely on these services,
the risk posed by cookie-stealing
malware like Hydra continues to grow.

55

2022 NCC Group Annual Threat Monitor

## Hydra Variants

Since its initial discovery, several
variants of Hydra have been identified,
each with its own unique features and
capabilities. These variants are often
the result of ongoing development by
the threat actors behind the malware,
who are constantly refining their
techniques to evade detection.

Some variants have been observed
incorporating additional features,
such as ransomware capabilities or
the ability to download and execute
other malicious payloads. This
versatility makes Hydra a significant
threat to organizations of all sizes.

56

2022 NCC Group Annual Threat Monitor

## C2 Server Analysis

Analysis of Hydra's command-and-control
(C2) infrastructure reveals a complex
and resilient network. The threat actors
behind Hydra use a variety of techniques
to hide their C2 servers, including
the use of domain generation algorithms
(DGAs) and fast-flux DNS.

These techniques make it difficult for
security researchers and law enforcement
to track and dismantle the C2
infrastructure. By constantly rotating
their C2 servers, the attackers ensure
that their malware remains operational
even if individual servers are taken
offline.

57

2022 NCC Group Annual Threat Monitor

## Conclusion

The Hydra malware is a prime example
of the evolving threat landscape. Its
ability to steal credentials and session
cookies, combined with its resilient
C2 infrastructure, makes it a formidable
threat to organizations.

To defend against Hydra and similar
threats, organizations must implement
a multi-layered security strategy. This
includes:

- **User Awareness Training**: Educating
  employees on the risks of phishing
  and how to identify malicious emails.
- **Endpoint Protection**: Deploying
  advanced endpoint detection and
  response (EDR) solutions to detect
  and block malicious activity.
- **MFA Implementation**: Using phishing-
  resistant MFA, such as hardware
  security keys, to protect against
  credential theft.
- **Threat Intelligence**: Leveraging
  timely threat intelligence to stay
  informed about the latest threats
  and TTPs.

58

2022 NCC Group Annual Threat Monitor

## Threat Spotlight: SEO Poisoning

SEO poisoning, also known as search
engine poisoning, is a technique used
by threat actors to manipulate search
engine results to direct users to
malicious websites. By creating
fake websites that mimic legitimate
brands or services, attackers can
trick users into downloading malware
or providing sensitive information.

In 2022, we observed a significant
increase in SEO poisoning campaigns,
particularly those targeting popular
software and services. These campaigns
are often highly effective, as users
are more likely to trust search results
that appear at the top of the page.

59

2022 NCC Group Annual Threat Monitor

## Recent cases of SEO Poisoning

Recent cases of SEO poisoning have
targeted a wide range of software,
including image editing tools,
productivity software, and security
utilities. In these campaigns, attackers
create fake websites that look identical
to the official sites, complete with
legitimate-looking download links.

When a user clicks on these links,
they are prompted to download a
malicious file, which is often
disguised as the legitimate software.
Once executed, the malware can
steal credentials, deploy ransomware,
or provide the attacker with remote
access to the system.

60

2022 NCC Group Annual Threat Monitor

## BATLOADER

BATLOADER is a prominent malware
loader that has been frequently
distributed through SEO poisoning
campaigns. It is designed to download
and execute other malicious payloads,
such as ransomware or information-
stealing trojans.

BATLOADER's distribution method
is highly effective, as it leverages
the trust that users place in search
engine results. By appearing at the
top of search results for popular
software, the attackers can reach a
large number of potential victims
with minimal effort.

61

2022 NCC Group Annual Threat Monitor

## Conclusion

SEO poisoning is a powerful technique
that exploits user trust to distribute
malware. As threat actors continue to
refine their methods, organizations
must be vigilant and take steps to
protect their users.

To defend against SEO poisoning,
organizations should:

- **Educate Users**: Teach employees
  to be cautious when clicking on
  sponsored search results and to
  verify the URL before downloading
  any software.
- **Use Official Sources**: Encourage
  users to download software only
  from official websites or trusted
  app stores.
- **Implement Web Filtering**: Use
  web filtering solutions to block
  access to known malicious websites
  and domains.
- **Monitor Search Results**: Regularly
  monitor search engine results for
  your brand or services to identify
  any potential SEO poisoning
  campaigns.

62

2022 NCC Group Annual Threat Monitor

---

Basta

Finally, whilst BlackBasta ranked in
fourth place, given their possible link to
Conti and number of overall attacks, 153
(6%), they remain important. The group
observed a steady incline in numbers
before a minute drop in June (by 1).
Notably, this is a rather small shift given
that the overall threat landscape saw
a substantial decline from 237 in May
to 135 in June, with many threat actors
observing much greater decreases.
Maintaining more or less the same
numbers despite an overall drop in June
as well as accounting for 12% of attacks
that month and ranking in second place
is illustrative of the groups powerful entry
into the landscape.

Numbers fluctuated more dramatically
following July with a major decrease
observed in November, which was
particularly notable as the figures for
November increased overall. Whilst
cases rose in December, this increase
remained small where compared to
additional threat actors and previous
months. For example, although
BlackBasta’s numbers increased from
5 to 14 incidents in December, attacks
in December rose across the board
meaning that the group only accounted
for 5%, a small proportional increase
of 2% from November. At present, this
suggests that BlackBasta’s numbers are
down, however, this may be the result
of seasonal fluctuations and remains to
be seen whether they will spike as we
move into 2023.

42

Sectors Targeted
BlackBasta’s sectors focused on Industrials
with 73 attacks (48%), followed by Consumer
Cyclicals with 32 (21%), and finally
Technology with 14 (9%). These align with
both the wider threat landscape and Conti’s
targeting alike.

Industry Targeted
Industries targeted concerned, Machinery,
Tools, Heavy Vehicles, Trains & Ships with 25
attacks (16%), followed by Construction and
Engineering with 17 incidents (11%), and
Professional and Commercial Services with
14 (9%).

Looking Ahead
Looking ahead at 2023, the data suggests
that Lockbit will likely maintain a prominent

if not primary position on the leader board
given their consistent and substantial
targeting. Organisations should consider
Lockbit a continuous threat and familiarise
themselves with relevant TTPs, sectors,
and industries of interest to maintain or
establish, a strong security protection
perimeter against the group. In addition,
similar importance should be placed upon
protection against BlackCat and BlackBasta
TTPs as their numbers appear to be on the
incline, as well as having been responsible
for a great number of ransomware attacks
this year. For now, Conti appears to have
rebranded/filtered off into affiliated groups,
though remaining aware of historic TTPs
and targeting will continue to serve as
valuable, wherein similarities may manifest
across the likes of BlackBasta or Hive.

2021

2022

30

25

20

15

10

5

0

J
a
n
u
a
r
y

F
e
b
r
u
a
r
y

M
a
r
c
h

A
p
r
i
l

M
a
y

J
u
n
e

J
u
y

l

A
u
g
u
s
t

O
c
t
o
b
e
r

S
e
p
t
e
m
b
e
r

N
o
v
e
m
e
b
e
r

D
e
c
e
m
b
e
r

Figure 25 Hack & Leak Numbers for BlackBasta 2021-2022

2022 NCC Group Annual Threat Monitor

Regions

Finally, as evoked in our monthly reports,
North America and Europe suffered the
greatest number of attacks across 2022.
North America took the greatest hit with
1106 attacks (44%), followed by Europe 896
(35%), Asia 287 (11%), South America 128
(5%), Oceania 62 (3%), Africa 42 (2%) and 9
undisclosed reflecting those attacks with
victim names yet to be confirmed due to
new threat actor hack and leak methods.

Whilst North America took the lead,
this reflects a 24% decrease from 1447
incidents in 2021 and an 11% proportional
decrease. Europe observed an 11%
increase in attack numbers from 810 to
896, yet only a 5% proportional increase
from 2021, thus presenting a similar level
of targeting to the previous year. Asia
rose slightly from 237 incidents in 2021 to
287 in 2022, a 21% increase, although only
reflecting a small proportional growth of
2%. South American numbers increased
from 97 to 128 attacks, a 31% increase
and 2% proportional growth. Attacks in
Oceania rose from 53 to 62, reflecting a
17% increase and 1% proportional growth.
Finally, ransomware in Africa almost
doubled from 23 to 42 attacks, reflecting
an 83% increase and 1% proportional
increase.

43

As such, there were a number of notable
increases in raw numbers, certainly amongst
Asia, South America and Africa. Proportionally
however, these regions accounted for a very
similar amount of attacks to that of last year.
Hence, where the wider threat landscape is
concerned, little variation in the overall share
of targeting was observed.

region. Naturally, as North America accounts
for a vast number of global businesses, the
sheer size exposes it to a greater number
of risks and higher number of ransomware
attacks in consequence. Organisations
globally should continue to practice strong
cyber security measures irrespective of
decline, or similar proportional targeting.

North America observed the only decrease
in percentage and proportional change,
suggesting that targeting within the region is
declining in both respects. That said, although
taking up slightly less of the attack surface
than last year, numbers remain high within the

44%

2%

3%

5%

11%

35%

Europe

Asia

South America

Oceania

Africa

Undisclosed

North America

Figure 26  Percentage of Victims by Region for Hack & Leak Victims (2022)

2022 NCC Group Annual Threat Monitor

DDoS Threat
Landscape

Geography

There were 230,519 observed DDoS events over the whole
of 2022. Of these, an astonishing 45% targeted the United
States. Mirroring the observations made for DDoS events
as a whole, the United States experienced their highest
number of attacks in January with 27% of their yearly total.
Similarly, the US experienced the fewest number of attacks
in October, with 3% of their yearly total. The United States
was consistently the most targeted nation around the world,
retaining the top spot for every month of the year.

France claimed 2nd place, representing only 5% of the
global total. Likewise with the United States, and the
observations of the total global attacks, France experienced
their most attacks in January with a total of 22% of their total
yearly attacks, and the fewest in October with 3% of their
yearly total.

Behind France as the 3rd most targeted nation for DDoS
attacks in 2022 is the United Kingdom. The UK experienced
4.5% of the global total of DDoS attacks. Continuing the
trend established by the US and France, the UK experienced
the most attacks in January and the fewest in October
with 34% of their yearly total and 2% of their yearly total
respectively.

In this section we will expand upon
the DDoS data we began analysing
in October’s Threat Pulse, looking at
2022 in its entirety and asking some
of the pertinent questions we as
intelligence analysts use to drive
future intelligence requirements. We
will dive into the where, when, and
how of DDoS attacks across 2022,
asking the following questions:

•  Where were most attacks

targeted geographically?

•  When were the top targeted

countries attacked during 2022?

•  How were victims attacked?

•  How long were attacks carried

out for?

45

2022 NCC Group Annual Threat Monitor

We can see from the below graphical representation the
proportion of yearly global attacks levied against the 10
most targeted nations.

Though the US was consistently the most targeted nation
globally for DDoS attacks, the holders of 2nd and 3rd
most targeted were not as consistent. 8 countries shared
second and third place at different stages throughout the
year, these countries are:

It is likely that this elevated level of
targeting returned to normal levels
after June, as the specific campaign
responsible for elevating them either
concluded or was mitigated through
implementation of defensive measures.

A geographic hot map, used for
visualisation of data, can be found on
the next page, helping to represent
the scale of attacks observed by the
top ten most targeted nations around
the globe for the entirety of 2022.

United States

France

United Kingdom

Germany

China

Canada

Brazil

Afghanistan

Russia

Poland

0.00

10.00

20.00

30.00

40.00

50.00

Figure 27 Top 1 0 Targeted Nations as a % of Overall Global Total

•  UK
•  Canada
•  France
•  China
•  Iran
•  Germany
•  Brazil
•  Afghanistan

Of these 8 nations, the standout is Iran. Iran only featured
in the top 10 most targeted nations once in 2022: in
June, when they experienced 2,351 denial of service
events and were the 2nd most targeted nation globally
at that time. Outlier instances like this potentially indicate
the existence of a specific campaign against the Islamic
Republic. It is possible that this outlier represented a
targeted campaign by one actor or collection of actors
with a joint purpose. Coincidentally, an interesting
observation also outlined in this report was the targeting
of Iranian steel companies in June 2022, by the self-
proclaimed hacktivist group, Predatory Sparrow aka
Gonjeshke Darande. See the section, Predatory Sparrow
attack on Iran Steel Plant.

46

2022 NCC Group Annual Threat Monitor

When examining attacks for the top 5
most targeted nations, after the United
States (France, United Kingdom,
Germany, China, and Canada), they
mostly follow the pattern set by the
month-by-month percentages of total
attacks across the globe throughout the
year. Though each of the five nations is
at various stages recording either higher
or lower volumes of attacks proportional
to their total than that of the global total
of all nations, represented by the grey
columns, they all roughly align individually
with what is observed happening at a
global scale. This potentially indicates
that despite following the spikes and
dips of the overall percentages for the
most part, there may have been specific
events which triggered elevated targeting
levels of specific nations.

Alternatively, as these are 5 of the
top 10 most targeted nations around
the globe, it is likely that there are
multiple campaigns being conducted
against them at the same time, and
so these spikes and dips could
align simply with the initiation and
conclusion of different campaigns with
a resulting varying level of overlap.

Figure 28 Hotspot Map Representing Concentration of Global Attacks

40

35

30

25

20

15

10

5

0

France

United Kingdom

Germany

China

Canada

% of total

J
a
n
u
a
r
y

F
e
b
r
u
a
r
y

M
a
r
c
h

A
p
r
i
l

M
a
y

J
u
n
e

J
u
y

l

A
u
g
u
s
t

S
e
p
t
e
m
b
e
r

O
c
t
o
b
e
r

N
o
v
e
m
e
b
e
r

D
e
c
e
m
b
e
r

Figure 29 Month-by-Month Proportional Breakdown for 5 Most Targeted Nations (after the US) Compared to the Global Overall % Total

47

2022 NCC Group Annual Threat Monitor
A representative graph of attack time frames can be found below:

24h+

12-24h

6-12h

5-6h

4-5h

3-4h

2-3h

1.5-2h

1-1.5h

45-60m

30-45m

15-30m

10-15m

5-10m

4-5m

3-4m

2-3m

1-2m

<1m

0

5

10

15

20

25

30

35

Figure 30 Attack Durations as % of Global Total Attacks

Though the modal duration of attacks was 5-10 minutes for the year as a whole, and for 10
out of 12 months individually, the mean or average attack time was much longer. This skewing
of attack durations is due to the occurrence of multiple attacks each month which lasted,
not in the minutes range, but in the days. The longest attack of the year was levied against
Afghanistan, and lasted for 51 days in total, across April, May, and June.

Attack Durations

The overwhelming majority of DDoS
events observed in 2022 resulted in a
service disruption lasting between 5
to 10 minutes. Of the 230,519 observed
events, 30% lasted for this length of
time. This is more than twice as many
as the next most common duration of
between 3 to 4 minutes, representing
14% of the yearly total. Though the
second most common length of
time which a disruption lasted, this is
the highest number of attacks for a
single-minute duration, as opposed
to the 5-minute window between 5
and 10 minutes which represented
the majority of attacks. This attack
duration, of 5-10 minutes, was the
most common throughout the year,
containing the highest number of
events every month except for August
and September. In these months, the
3–4-minute window was the most
prevalent, though the 5–10-minute
window was not far behind with the
second highest number of attacks in
both months.

48

2022 NCC Group Annual Threat MonitorThe following table shows the top 10 attacks in 2022, based on time
frame and the dates they were initiated.

The average monthly attack time, which accounts for attacks
resulting in disruptions of less than a minute and more than a month,
is depicted in the below graph:

Duration (days)

Country

51

51

51

51

44

42

41

41

40

32

Afghanistan

Afghanistan

Afghanistan

Afghanistan

United States

Afghanistan

United States

Spain

Afghanistan

Afghanistan

Table 1 Top 1 0 Attack Durations

Started

20-Apr-22

20-Apr-22

20-Apr-22

20-Apr-22

08-Feb-22

29-Apr-22

08-Feb-22

08-Feb-22

20-Apr-22

06-Jan-22

Concluded

10-Jun-22

10-Jun-22

10-Jun-22

10-Jun-22

23-Mar-22

10-Jun-22

21-Mar-22

21-Mar-22

30-May-22

08-Feb-22

120

100

80

60

40

20

0

J
a
n
u
a
r
y

F
e
b
r
u
a
r
y

M
a
r
c
h

A
p
r
i
l

M
a
y

J
u
n
e

J
u
y

l

A
u
g
u
s
t

O
c
t
o
b
e
r

S
e
p
t
e
m
b
e
r

N
o
v
e
m
e
b
e
r

D
e
c
e
m
b
e
r

Figure 31 Average Attack Duration (in minutes) Month-by-Month

Looking at the average duration of an attack allows for the significant gap
between the shortest and longest attacks made each month. It can also
potentially provide insight as to which types of protocols can be exploited
for, or which nations experience longer, more disruptive attacks, and in turn
provide insight to help defend against future attacks.

49

2022 NCC Group Annual Threat MonitorLDAP, standing for Lightweight Directory
Access Protocol is a protocol commonly
used to provide open and standard
access for directory information such as
permissions, users, or file shares. It is
probably best known for being used in
Microsoft’s Active Directory. LDAP can
be used for injection attacks, similarly to
how SQL injection attacks are conducted,
utilising similar exploitation techniques, and
has been observed being used in DDoS
attacks since at least 2016.

DNS amplification attacks are reflection-
based volumetric attacks leveraging open
DNS resolvers to overwhelm target systems
with traffic, causing them to overload and
crash. Frequently exploited by botnets, each
bot spoofs its IP with the real IP address of
the target network, which gets overloaded

with DNS responses it did not initiate.
To amplify the attack, threat actors will
structure their initial DNS requests in order
to receive as large a response as possible,
amplifying the effect on the target system
beyond the attacker’s initial traffic.

Source ‘protocol’ concerns the Valve
Source Engine flood, a UDP (amplification)
attack used to consume available resources
against a server. The attacks concern
sending TSource Engine Query requests to
a gaming server causing it to overload and
resulting in a denial of the gaming service.
The attack targets the games market,
and can be utilised by those gamers
wishing to cause a disruption to their
opponents’ services for their own gaming
advantage, revenge, or as simple trolling.

Idap

dns

source

ntp

dahua

mdns

open vpn

stun

lantronix

dtls

0

10

20

30

40

50

60

Figure 32 Top 1 0 Most-Exploited Protocols as % of Global Total Attacks

Exploited Protocols

NCC Group observed more than 35
different protocols being abused for
DDoS attacks in 2022. Some of them
were used consistently in attacks over
the course of the year, while some
were used less frequently.

One protocol, LDAP, was exploited
consistently throughout the year,
and at far greater numbers than
alternatives. Despite the overwhelming
prominence of the LDAP protocol,
there was a great variety in the other
protocols which were frequently
utilised by threat actors to carry out
denial of service attacks. 28 of the 35
protocols used featured in the top ten
most exploited protocols in at least
one month of the year, including the
aforementioned LDAP protocol which
accounted for 56% of all DDoS events, or
129,768 disruption attacks.

The following information
describes each of the top attack
protocols accordingly.

50

2022 NCC Group Annual Threat Monitor

We advise that all organisations take steps to
understand how the threat of a DDoS attack
may impact their operations and look at the
many service offerings offered by reputable
security providers.

Companies should also regularly
run simulations that test that the
implementation, the people and the
processes provide suitable protection
in the event of such an attack.

DDoS attacks affect the availability of
systems or services, such as customer
portals or websites. As such, the
effectiveness of DDoS mitigations or
controls are ideally measured in the amount
of ‘down-time’ to systems that have been
targeted. When conducting risk assessments
against an organisation’s critical assets,
particularly those that rely on availability, due
consideration should therefore be given to
ensuring these have adequate protections in
place.

As has been the case for a number of
years, as more and more devices become
connected to the internet (Internet of Things),
the higher the likelihood that the size of
botnets will increase, especially when one
considers the rapidly evolving use of IoT in
smart cities, connected vehicles, and smart
tech in our homes.

Conclusion

2022 kicked off with an explosion of
DDoS attacks. Though our assessment
shows that the numbers sharply
dipped from February, and despite a
couple of mini spikes, steadily declined
over the course of the year. Despite
this, they are something which has
remained in the public consciousness,
with botnets like Killnet becoming
something discussed outside of
security circles. The use of botnets
and DDoS attacks combined with
conventional military aggression in
the Russia-Ukraine conflict has made
it apparent that the cyber threat
landscape has changed. Denial of
service attacks are no longer seen as
the purview of just script-kiddies and
amateur threat actors, but also as a
significant tool of disruption utilised by
some of the most prominent global
threat actors and impactful campaigns
of disruption.

51

2022 NCC Group Annual Threat Monitor

Vulnerability
landscape

Exploiting vulnerabilities is a proven point
of entry for threat actors. In this section
we highlight critical vulnerabilities that
have been published during 2022 and
enable readers to gain insights into the
dynamics of the vulnerability landscape.

As companies have continued to adopt
hybrid and full-remote working formats
following the COVID-19 pandemic,
businesses continue to prevail against
vulnerabilities that may affect daily
operations and tasks. Cloud services that
support critical aspects of a business
remain attractive for attackers and
adversaries, with researchers from Cloud
Security Alliance (CSA) reporting that only
4% of surveyed organisations reported
sufficient security for 100% of their data
in the cloud. In the same survey, it was
also found that third parties, contractors,
and suppliers are the most commonly
targeted groups in cyberattacks. ‘The
article further references research by
security vendor Proofpoint who found
that more than 90% of monitored cloud
tenants were targeted every month,
with at least 24% successfully breached.

One of the most severe vulnerabilities of the
year demonstrates the ongoing trend for
attacks against remote working. In November,
Citrix disclosed several authentication bypass
critical vulnerabilities that affected Gateway
and ADC products. As the professional world
continues to adapt to hybrid and remote
working patterns, we expect to see this
trend continuing into 2023 – in particular,
attacks against third-party providers that may
exist as a proxy for actors to infiltrate other
organisations and businesses that may also
rely on these services.

Historic vulnerabilities continue to be
an issue for organisations that may not
have implemented patches or mitigations.
Log4Shell (CVE-2021-44228), Zerologon
(CVE-2020-1472), ProxyShell (CVE-2021-
31207, CVE-2021-34473, CVE-2021-
34523) and Atlassian Confluence Server &
Data Centre (CVE-2021-26084) are some
of the most routinely exploited vulnerabilities
in businesses that have improperly patched
their estates. This demonstrates the
importance of maintaining a proper patching
routine across your enterprise to provide a
robust defence against attackers that are still
targeting dated vulnerabilities and flaws.

Following the infamous Colonial Pipeline
ransomware attack in 2021, there has
also been a sharp increase in the number
of vulnerabilities disclosed in operational
technology (OT) environments. Skybox
Security reported an 88% rise in disclosed
vulnerabilities between 2020 and 2021,
and we continue to see a trend of attacks
on industrial systems and critical national
infrastructure as environments become
more connected. In June, the Cybersecurity
& Infrastructure Security Agency (CISA)
released multiple Industrial Controls
Systems Advisories (ICSAs) in response to
Forescout’s research, dubbed OT:ICEFALL,
that exposed 56 vulnerabilities caused by
insecure-by-design practices in operational
technology across multiple vendors prevalent
in industries such as oil and gas, nuclear and
manufacturing.

Overall, we have seen an upward trend
in disclosed vulnerabilities across
different sectors, environments, and
technologies. According to CVE Details,
during 2022 around 25,226 vulnerabilities
have been identified and assigned CVE
numbers. Overall, this is an increase of
approximately 25% compared to 2021.

53

2022 NCC Group Annual Threat Monitor

Total Per Quarter

Critical CVEs%

7000

6000

5000

4000

3000

2000

1000

0

%
% 1
6

4
1

%
6
1

%
5
1

%
7
1

%
3
1

%
4
1

%
6
1

%
4
1

%
2
1

%
2
1

%
5
1

%
7
1

%
8
1

%
6
1

%
6
1

2019

2020

2021

2022

Figure 33 CVEs Disclosed by Quarter

As can be seen in the above figure, CVE’s Disclosed by Quarter, 2022 has
done nothing but set record highs, both in terms of total CVE’s disclosed and
the number of them that were critical quarter-by-quarter. Before 2022, the
highest number of critical vulnerabilities disclosed in one quarter was 811 (in
the first quarter of 2020), yet every individual quarter of 2022 has surpassed
this; 968 were critical in Q1, 1127 in Q2, 1146 in Q3, and 1019 in Q4.
Critical vulnerabilities are typically unauthenticated and allow remote code
execution thereby increasing their severity, and 2022 has been a busy year for
vulnerabilities such as these, showing how vigilant vendors and customers alike
have had to be.

Looking at the data we have from the past few years there appears to be
a pattern arising where one year experiences less vulnerabilities, and the
following year makes up for this with an increase (this is particularly evident
when looking at 2020 and 2021). However, 2022 appears to break this trend
where the number has increased once again but in all quarters of the year. It
is very difficult to attribute trends to the disclosure of vulnerabilities in systems

due to them being mostly arbitrary and unpredictable apart from the one
constant: Vendors being forced to disclose vulnerabilities due to discovery/
exploitation in the wild. With threat actors like LockBit seemingly favouring
vulnerability exploitation with their bug bounty program, it could be argued
that threat actors are beginning to take a preference to vulnerabilities for initial
access, thereby increasing the total disclosures.

As for what we will see in 2023, it is difficult to predict based on what has
already been observed, but if more threat actors follow in LockBit’s footsteps
and develop bug bounty schemes, it wouldn’t be farfetched to forecast yet
another increase in 2023. However, one thing is almost undeniable based on
the data presented to us; it is unlikely that we will return to the lows displayed
in 2019 and prior, meaning organisations should continue to focus on stringent
patch management and mature threat intelligence capabilities to mitigate these
risks as much as possible.

54

2022 NCC Group Annual Threat Monitor

Ukraine-Russia
War

Perhaps one of the most notable events
in 2022 was the invasion of Ukraine by
Russian forces in February. The conflict
between Russia and Ukraine had of
course been ongoing for quite some
time, but escalating tensions towards
the back end of 2021 and 2022 gave hint
to more to come.

Whilst we have not seen the so-
called ‘cybergeddon’ that some were
expecting from the next big conflict on
our globe, one thing is absolutely certain;
cyber warfare has proven itself to be a
critical element in a hybrid cyber-kinetic
battlefield. In this conflict, we have seen
the use of simple defacement and
hacktivist activity, Distributed Denial of
Service (DDoS) attacks, and even the
deployment of malware designed for
sabotage and destruction of critical
national infrastructure.

In the weeks leading up to the invasion, we
observed several disinformation campaigns
and false flag operations launched by Russia,
creating a pre-text and justification for the
invasion to come. This was also followed
by targeting of Ukrainian infrastructure and
essential public services through the use
of ‘wiper malware’, of which, several new
variants were deployed over the course of
the year.

There has also been an increased number
of Nation State espionage-type campaigns
across the globe since the invasion, and
these haven’t been limited to Russian activity.
Several campaigns launched by China
against Western and Asian countries as well
as Russia were identified. Additionally, China
themselves stated that they were subject to
campaigns launched by western countries,
specifically the United States.

This wiper malware was successful in
creating challenges for Ukrainian authorities
and military, especially in the final few days
preceding the physical invasion, when the
American Satellite communications provider,
Viasat, was affected. One particular strain
of malware, AcidRain, was used to target
Viasat’s KA-SAT satellite broadband service
to wipe SATCOM modems, rendering
them inoperable.

This attack not only impacted thousands
of modems across Ukraine, but many
more across the rest of Europe, and some
organisations felt the collateral impact
of this, including Enercon, who lost the
ability to remotely communicate with
their wind farm turbines in Germany.

There were some fears that there would be
retaliation by Russia against Ukraine allies,
including those countries that had imposed
sanctions against Russia. So far, we haven’t
seen any sort of targeted retaliation. But, one
thing is clear, the conflict in Ukraine has led
to several critically destructive and disruptive
cyber-attacks, some of which have impacted
global companies (albeit indirectly).

The offensive cyber-attacks launched by
both sides have been significant, but Ukraine
has shown its defensive capabilities to be
strong, and this has been due to its ability
to prepare, prevent, and detect threats. This
has highlighted the importance of threat
intelligence, and more importantly, the
sharing of this intelligence for mutual benefit.

56

2022 NCC Group Annual Threat Monitor

Threat Spotlight:
Hydra Malware

Introduction

Hydra, also known as BianLian, has been one of the most active mobile
banking malware families in 2022 alongside Sharkbot16 and Flubot. The
features implemented in this banking malware are present in most of the
banking malware families, such as injections/overlays and keylogging
(listening to Accessibility events), though notably, since June 2022, Hydra
has even introduced a cookie-stealing feature which targeted several
banking entities in Spain. This reflects a recent trend in which different
banking malware families are introducing the capability of stealing cookies.
This could originate from cybercriminals being more eager to rent banking
malware with this capability, hence giving the malware author more revenue
when implemented.

During our research, we found that a significant number of the command-
and-control (C2) servers are located in the Netherlands. This is an
interesting pattern, especially since threat actors (TAs) active in mobile
malware have been frequently hosting their infrastructure in Russia and
China.

Credential-stealing Features

Hydra is an Android banking malware, the main goal of which is stealing
credentials. This enables TAs to access those accounts and monetize them
directly or monetize them indirectly by selling them to third parties. Hydra
steals credentials using the following two strategies: Overlays/Injections and
Keylogging.

Overlays/Injections: At the beginning of the infection, Hydra sends several
requests to the C2 server, subsequently receiving a list of targeted
applications and a URL that points to a ZIP file containing the corresponding
injections. The targets consist mostly of banks and cryptocurrency wallets.
Hydra saves these injections locally and shows them to the victim once
it detects a user opening a banking application. This results in the victim
believing it to be the official application requesting credentials or credit card
information.

58

2022 NCC Group Annual Threat Monitor

When the injection is shown and
the victim enters their credentials,
the malware utilises JavaScript’s
“Console.Log” function to send the
credentials to the native Java code
of the application. This function is
reimplemented by the malware to
send credentials to the C2 server,
as shown in the figures here.

Figure 34 Server Response with a Configuration Including the URL to Download a ZIP file Containing all the Injections

Figure 35 Contents of the ZIP File with the Injections

59

2022 NCC Group Annual Threat MonitorFigure 36 Decompiled Code Used to Save the Stolen Credentials

Figure 37 Decompiled Code Used to Send the Stolen Credentials to the C2 Server

60

2022 NCC Group Annual Threat MonitorKeylogging: Hydra abuses the Accessibility
permissions to set up an Accessibility
service that receives every Accessibility
event occurring on the infected device. Using
this method, the malware receives change
events for TextFields (to steal usernames
and passwords) and button clicks.

In order to complement the credential-
stealing features, Hydra includes a screencast
component that sends screenshots to the
C2 server and receives commands used to
simulate Accessibility events (click buttons,
enter text in TextFields, etc.). This way, the
TAs can manipulate the target application on
the victim’s device to monetize the account
associated with that application. This is a good
way to bypass antifraud security measures
focused on checking IP addresses or devices
that log in to the accounts or make transfers.

Figure 38 Keylogger Code

61

2022 NCC Group Annual Threat MonitorBesides credential-stealing features, Hydra
implements additional features to steal
other information from the infected device.
They especially target information required
for successful account takeovers and
monetisation of accounts, such as received
SMS messages for OTP codes, a list of
installed applications, or the unlock code of
the device which can be used to unlock the
device and start the screencast feature.

Apart from the previously mentioned
features, Hydra developers introduced
a new and interesting feature around
June 2022: stealing cookies. With this
new feature, the malware can steal
cookies from sessions linked to bank
accounts of victims, avoiding the need
of credentials when logging in.

Figure 39 Screencast Feature Starting Code

62

2022 NCC Group Annual Threat Monitor
New features Stealing Cookies

Around June 2022 we found new samples introducing this new feature
used to steal cookies from sessions after the victims log in to their
accounts. Since the beginning until now, there have not been many
banks or other applications targeted by this feature, but the list has
been increasing in the past months.

This began with targeting a few applications, Google Mail and BBVA
Spain, as we can see in the following image:

Figure 40 Targeted Applications in the First Versions Including the Cookie-stealing Feature (June)

But after some months, TAs included two more targets - Facebook and Davivienda - to steal credentials:

Figure 41 Targeted Applications in the Latest Version

63

2022 NCC Group Annual Threat Monitor
As we can see in the previous pictures of
the decompiled code, to implement this
feature, TAs include the package name of
the targeted applications alongside the
URLs to the mobile login website. This way,
a WebView can show the victim the official
login page and, after the victim successfully
logs in to his account, the cookies of
the loaded website in the WebView are
forwarded to the C2 server.

It is interesting that TAs include the list
of targeted applications by the cookie-
stealing feature hardcoded in each sample,
while the list of targets for injections is
retrieved from the C2 server. Since it
is a new feature, it is probably in a test
phase, and after some time TAs could start
retrieving the list of cookie-stealer targets
from the C2 server instead of hardcoding
the list in the malware.

64

Figure 42 Hydra Creates a POST Request to Send Credentials or Cookies to the C2 Server

2022 NCC Group Annual Threat MonitorHydra Variants

We found that Hydra has three different variants with
small changes between them. The principal features
are present in all of them, but they include different
information about the C2 server. Hydra can be
categorized in three variants based on how it includes
the C2 server information: Using Tor, Using GitHub,
and Hardcoded C2 Server.

Using Tor: This variant includes a Tor (onion) URL to
the endpoint ‘/api/mirrors’. In response, it will receive
a Base64-encoded JSON with the list of C2 servers
to use. This variant includes code to download Tor
native libraries in order to connect to this ‘backup C2’
using the Tor network.

Using GitHub: This variant includes a GitHub
repository file containing a Base64-encoded JSON
object with the list of C2 servers. This is almost
equivalent to the Tor variant, but it uses GitHub
instead of using the Tor network - it does not include
code to download and run Tor native libraries.

Figure 43 Tor ‘Backup C2’ Response

Figure 44 Tor Native Libraries Used to Connect to the Tor Network

65

2022 NCC Group Annual Threat Monitor
Hardcoded C2 server: This variant includes the C2
server in the binary itself and eventually sends a request
to the path ‘/api/mirrors’ in order to get a new list of C2
servers that it can use in the future if the hardcoded one
goes down.

Figure 45 Code to Connect to GitHub to Reach C2 Servers

Figure 46 GitHub File Response with the Base64-encoded List of C2 Servers

Figure 47 C2 Server Hardcoded in the Sample The path ‘/api/mirrors’ is used to get an updated list of C2 servers

66

2022 NCC Group Annual Threat MonitorC2 Server Analysis

During our Hydra research, we have been
collecting a significant number of C2
servers used in different samples. From
all those servers, we found that some
countries are preferred over others in
terms of hosting.

This usually happens with Russia or
China, which are the preferred countries
to host C2 servers by TAs, but surprisingly,
Hydra’s TAs are using other countries
such as the Netherlands (73), United
States (42) and Ukraine (29). In this case,
we observed only 19 servers hosted in
Russia and none in China.

In the following picture we can see a
world map with the different countries
hosting Hydra’s C2 servers. The colour
intensity increases with the increase in
number of servers.

Even though some servers use a different
configuration - different list of targeted
apps - most of the servers use the same list.
This could mean that Hydra developers ship
their malware with a default list of targets
or that attackers use a default list of targets
themselves.

Besides the different Hydra variants used
for each sample, we found that different
C2 servers are configured with a different
target list. This is normal, since this malware
is rented out by its developers, so each
TA has different interests in what banks or
applications to target. Even though most
of the servers seem to use a default list of
targets - probably all the supported banks/
apps - there are certain servers with a
smaller list of targets, usually focused on
banks or applications used in specific
countries or languages - such as LATAM and
Spanish banks.

67

Figure 48 Popular Countries for Hosting Hydra C2 Servers

2022 NCC Group Annual Threat Monitor

Typical features to steal credentials are
implemented in this family: injections/
overlays, keylogging and, from around June
2022, the developers also started to include
cookies-stealing features in the rented
samples. All these features make Hydra one
of the more interesting banking malware
families to rent for TAs. This can explain why
we observed a lot of samples of Hydra every
day, many sharing the same C2 server.

During our research we also found that TAs
are frequently hosting their C2s in the same
countries, such as the Netherlands, United
States and Ukraine, instead of hosting them
in Russia or China, as usual. Additionally,
most of the servers have enabled all the
supported injections, instead of enabling only
those applications which are more interesting
to the TA depending on, for example, the
country of the bank.

We expect this family to be one of the most
active mobile banking malware strains in
the upcoming months, with its developers
implementing new and interesting features.

Even if the credential-stealing features and
the rest of the code is the same for all the
samples we detected, we found there are
differences in the way the C2 servers are
included in various samples. For this reason,
we distinguish three different variants based
on how the C2 server is included: an Onion
service, a GitHub repository with the list of
C2 servers and, finally, just a URL to the C2
server it should use.

Conclusion

Hydra has been one of the most
active banking malware families
for Android in 2022, alongside other
notorious families such as Flubot,
Sharkbot and Teabot. This banker
is rented out through underground
forums, and TAs that rent the
malware configure the list of
targeted applications based on
their needs. However, most of the
target lists we observed in Hydra
samples are equivalent, hinting at
a default configuration.

68

2022 NCC Group Annual Threat Monitor

Threat Spotlight:
SEO Poisoning

Recent cases of SEO Poisoning

Batloader

Throughout the years, many information stealers like Redline and SolarMarker
have abused SEO Poisoning to infect many systems. SolarMarker solely
relied on this infection vector for its campaigns. Two other examples of
SEO Poisoning malware are Gootkit  and SocGholish which were known to
be linked to Ransomware operations and were observed to be using SEO
Poisoning attacks through hacked websites.

Besides spreading malware via SEO poisoning, Google Ads are also
commonly used for scamming and phishing, such as serving fake
cryptocurrency websites or dating websites to steal money. In some cases, it
is even used to serve fake login pages for banking and other online services.

In 2022, a new contestant in the SEO Poisoning field has appeared known as
BATLOADER, resulting in the distribution of many different malware families,
such as: Gozi/URSNIF, SystemBC and Cobalt Strike.

BATLOADER is distributed through Windows installers (MSI) that are
downloaded from fake software websites. These malicious websites are
either indexed by search engines, distributed through SEO poisoning,
or distributed in forum posts. These websites use a list of the following
products to lure victims into downloading the malicious Windows Installers:

•  Zoom
•  Slack
•  Teams
•  LogmeIn
•  Evernote
•  GIMP
•  Openoffice

Figure 49 A Traffer for Fraud Related Services

70

2022 NCC Group Annual Threat Monitor

Conclusion

Based on the evidence presented it
is reasonable to suggest that SEO
Poisoning for the purpose of malware
delivery is on the rise, especially with
BATLOADER’s emergence. This form
of malware delivery is arguably a
form of social engineering, where
threat actors capitalise on human
weaknesses to gain a foothold on a
victim network, and in this case, the
targeting of those that assume the
first search engine result is reliable
and trustworthy.

From an organisation’s perspective,
the mitigations are akin to those
that exist for other forms of social
engineering (e.g. phishing, smishing
etc.), such as employee training
& awareness. When employees
understand and are aware of the
cyber threats they face on a daily
basis, such as SEO poisoning, they are
more likely to hesitate before clicking
on a malicious link or website, thereby
minimising the risk of attack that can
impact both the individual and the
organisation as a whole.

Figure 50 Fake Zoom Website Distributing BATLOADER

Upon downloading from the malicious website, a download request is sent towards another
attacker operated server. This request contains campaign specific information such as the
name of the fake software product, IP address making the request and a callback value. This
callback value is the MD5 hash of the current timestamp, meaning that the server will only
reply to active and fresh campaigns.

Figure 51 BATLOADER’s Distribution Source Code

71

2022 NCC Group Annual Threat Monitor