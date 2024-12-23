# 9th Annual State of the Software Supply Chain Report

## Table of Contents
- [Introduction](#introduction)
- [State of the Software Supply Chain by the numbers](#state-of-the-software-supply-chain-by-the-numbers)
- [CHAPTER 1: Open Source Supply, Demand, and Security](#chapter-1-open-source-supply-demand-and-security)
  - [Open source supply sees a resurgence](#open-source-supply-sees-a-resurgence)
  - [Open source consumption is decelerating](#open-source-consumption-is-decelerating)
  - [Individual ecosystem analysis](#individual-ecosystem-analysis)
  - [Open source software security concerns see no sign of slowing](#open-source-software-security-concerns-see-no-sign-of-slowing)
  - [Notable malicious packages and vulnerabilities](#notable-malicious-packages-and-vulnerabilities)
  - [Differentiating software vulnerabilities and malware](#differentiating-software-vulnerabilities-and-malware)
  - [Consumption behavior contributing to security concerns](#consumption-behavior-contributing-to-security-concerns)
  - [A global view of vulnerable open source downloads](#a-global-view-of-vulnerable-open-source-downloads)
- [CHAPTER 2: Open Source Security Practices](#chapter-2-open-source-security-practices)
  - [The state of scorecard check scores](#the-state-of-scorecard-check-scores)
  - [The Importance of Maintenance](#the-importance-of-maintenance)
  - [Year-Over-Year Differences](#year-over-year-differences)
  - [Conclusion](#conclusion)
- [CHAPTER 3: Modernizing Open Source Dependency Management](#chapter-3-modernizing-open-source-dependency-management)
  - [Open source consumers are not paying attention](#open-source-consumers-are-not-paying-attention)
  - [What makes an optimal open source component?](#what-makes-an-optimal-open-source-component)
  - [Understanding component upgrade urgency](#understanding-component-upgrade-urgency)
  - [Downloads by upgrade urgency](#downloads-by-upgrade-urgency)
  - [Global patterns of open source consumption behavior](#global-patterns-of-open-source-consumption-behavior)
- [CHAPTER 4: Software Supply Chain Maturity](#chapter-4-software-supply-chain-maturity)
  - [Software Supply Chain Maturity — Peer Insights](#software-supply-chain-maturity-peer-insights)
  - [How mature are today’s software supply chains?](#how-mature-are-todays-software-supply-chains)
  - [How have software supply chain management trends changed?](#how-have-software-supply-chain-management-trends-changed)
  - [Finding #1: Increased focus on open source risk](#finding-1-increased-focus-on-open-source-risk)
  - [Finding #2: Rise in demand for Software Bills of Materials](#finding-2-rise-in-demand-for-software-bills-of-materials)
  - [Finding #3: The critical connection of hygiene and speed in risk mitigation](#finding-3-the-critical-connection-of-hygiene-and-speed-in-risk-mitigation)
- [CHAPTER 5: Establishment and Expansion of Software Supply Chain Regulations and Standards](#chapter-5-establishment-and-expansion-of-software-supply-chain-regulations-and-standards)
  - [United States](#united-states)
  - [European Union](#european-union)
  - [Canada](#canada)
  - [Global partnerships](#global-partnerships)
  - [Are software supply chain regulations working?](#are-software-supply-chain-regulations-working)
  - [Navigating the policy frontier: Global cybersecurity regulations](#navigating-the-policy-frontier-global-cybersecurity-regulations)
- [CHAPTER 6: AI in Software Development](#chapter-6-ai-in-software-development)
  - [Sonatype’s risks & rewards of AI survey](#sonatypes-risks-rewards-of-ai-survey)
  - [The intersection of AI and software development](#the-intersection-of-ai-and-software-development)
  - [Navigating concern](#navigating-concern)
  - [AI’s open source toolkit: Components and models in focus](#ais-open-source-toolkit-components-and-models-in-focus)
  - [Conclusion: A collaborative future](#conclusion-a-collaborative-future)
- [About the Analysis](#about-the-analysis)
- [Acknowledgements](#acknowledgements)

Sonatype’s industry-defining research on the
rapidly changing landscape of open source, software
development, and software supply chain security
State the
9th Annual
Software
Supply Chain
PRESENTED BY
of
Contents

Introduction.....................................................................................3
State of the Software
Supply Chain by the numbers...................................4
CHAPTER 1
Open Source Supply,
Demand, and Security.......................................................5
Open source supply sees a resurgence ..............7
Open source consumption is decelerating.........8
Individual ecosystem analysis.................................10
Open source software security
concerns see no sign of slowing ...........................10
Notable malicious packages
and vulnerabilities.........................................................11
Diferentiating software
vulnerabilities and malware......................................12
Consumption behavior
contributing to security concerns...........................12
A global view of vulnerable
open source downloads ...........................................16
CHAPTER 2
Open Source Security Practices.......................17
The state of scorecard check scores....................18
The Importance of Maintenance............................21
Y
ear-Over-Y
ear Diferences......................................21
Conclusion.................................................................... 22
CHAPTER 3
Modernizing Open Source
Dependency Management.....................................23
Open source consumers
are not paying attention ...........................................24
What makes an optimal
open source component? ...................................... 26
Understanding component
upgrade urgency.........................................................27
Downloads by upgrade urgency.......................... 29
Global patterns of open
source consumption behavior ...............................31
CHAPTER 4
Software Supply Chain Maturity......................34
Software Supply Chain
Maturity — Peer Insights...........................................35
How mature are today’s
software supply chains?............................................36
How have software supply
chain management trends changed?..................37
CHAPTER 5
Establishment and Expansion
of Software Supply Chain
Regulations and Standards....................................42
United States ................................................................43
European Union...........................................................46
Canada ...........................................................................47
Global partnerships....................................................47
Are software supply chain
regulations working? .................................................48
Navigating the policy frontier:
Global cybersecurity regulations...........................49
CHAPTER 6
AI in Software Development.....................................51
Sonatype’s risks &
rewards of AI survey ................................................. 52
The intersection of AI
and software development.................................... 52
Navigating concern ...................................................53
AI’s open source toolkit:
Components and models in focus....................... 55
Conclusion: A collaborative future....................... 59
About the Analysis..............................................................60
Acknowledgements...........................................................61
2

# Introduction
In today’s fast-paced world, the pursuit of excel-
lence is a relentless journey. We all understand
the signiﬁcance of innovation, efciency, and
the individuals at the core of it all: developers.
From our past eight State of the Software Sup-
ply Chain reports, we know that developer pro-
ductivity soars when they have access to supe-
rior tools and better open source components,
making them the driving force behind better
security and better products.

But what exactly does “better” mean in the
ever-expanding landscape of technology
choices? This question, in part, is the reason
we’ve been studying the software supply chain
for the last nine years. As we deliver the 9th
version of this State of the Software Supply
Chain report, that question is more paramount
than ever. As we explore how to make “better”
software, it’s not just about the introduction
of AI or cutting-edge technologies; it’s about
addressing fundamental issues that, in many
ways, have not changed in nine years. It’s about
the often-overlooked, yet vital, element that lies
within our software supply chain: open source
consumption behavior.

We aim to sift through the labyrinthine market
of software components, not to add to the
cacophony of choices but to streamline it. Why?
Because choice is a double-edged sword.
The consequences of choosing poorly are
far-reaching.

Consider this — last year, we revealed that a
staggering 85% of projects in Maven Central
— the largest public repository for Java open
source components — are inactive. In other
words, developers are faced with a perplexing
array of choices, with only a fraction of them
leading to active, well-maintained projects. Yet,
we also found, and re-afrmed this year, that
96% of all vulnerable downloads from Maven
Central, had known ﬁxes available. There are so
many choices to make, and only with the right
tools, the right automation, can developers truly
be set up for success.

As we dissect the intricacies of open source
adoption and consumption, we validate a frus-
trating truth — development practices remain
rife with inconsistency. When choices are
made poorly, this inconsistency translates into
increased risks, discontent among developers,
and, perhaps most signiﬁcantly, a loss of both
time and money.

The State of the Software Supply Chain report
each year isn’t just a cautionary tale, but a call
to action. It is a response to the pressing need
to redeﬁne our priorities and a testament to our
willingness to evolve. We ﬁnd ourselves in a
period of revolution. Modernization is our ally.
With regulations a focus in nearly every region,
an uncertain economic climate demanding cost
savings and efciencies, and malicious activity
more prominent than ever, it’s time for change.
In the following pages, we provide you with an
in-depth update on open source usage trends
and security practices. We continue to draw
from public and proprietary data sources to
illustrate a host of issues with efective supply
chain management. We’ll look at:
▷Ongoing growth of the software supply chain,
as well as persistent security concerns
▷The advantages of using well-maintained open
source packages
▷Open source consumption and trends in
upgrade urgency of components
▷Peer insights into the use of SBOMs and
mature software supply chain management
▷The rise of open source and software supply
chain regulations
▷What role AI and ML play in assisting develop-
ers, and the challenges that AI practitioners
face in developing AI products

We also look at what it really means to have a
Software Bill of Materials (SBOM) and a Soft-
ware Composition Analysis (SCA) program, and
ultimately shed light on the path to a more ef-
cient, cost-efective, and secure development.
3

# State of the Software Supply Chain by the numbers
1 in 8
open source
downloads
have known risk
245,000
malicious packages
discovered —2X all
previous years combined
18.6%
of open source projects across Java
and JavaScript that were maintained in
2022, are no longer maintained today
96%
of vulnerable downloaded
releases had a fixed
version available
10
superior versions of components are
typically available, for every nonoptimal
component upgrade made
2x
When paired with optimal upgrades, good data saves
you twice as much time or nearly 1.5 months of time per
application, per year when upgrading components.
135%
increase in the adoption of AI and
ML components within corporate
environments, over the last year
67%
of survey respondents feel confident that their applications do not rely on known vulnerable
libraries, despite 10% of respondents reporting their organizations had security breaches due
to open source vulnerabilities in the last 12 months
4

# CHAPTER 1
# Open Source Supply, Demand, and Security
6

C H A P T E R  1 :  O P E N  S O U R C E  S U P P LY  A N D  D E M A N D
A monk by the name of John of Salisbury wrote
a famous phrase in a 12th century manuscript,
borrowed by Sir Isaac Newton and hundreds of
others since:
> “We are like dwarfs sitting on the shoulders of
giants. We see more, and things that are more
distant, than they did, not because our sight is
superior or because we are taller than they, but
because they raise us up, and by their great
stature add to ours.”

The meaning of the passage is simple: The
progress we make only happens because of the
progress in learning and understanding others
have made before us.

Nowhere else is this seen more than in the
adoption of open source. Nearly all of the soft-
ware shipped today relies on previous innova-
tion that is distributed freely on scafolding built
by the utmost experts in the world, available to
all developers free of charge.

In past State of the Software Supply Chain
reports, we’ve estimated that up to 90% of the
code we run in production is of open source
origin. Therefore, the economics of open source
are good indicators of trends and challenges in
the wider software market.

For the 9th consecutive year, we continue to
track the growth of open source adoption across
the top four major open source ecosystems.
These collectively account for four of the top ﬁve
languages in GitHub, and a 60% share of the
most popular programming languages accord-
ing to PYPL Language popularity index[^1].

Leveraging our continued monitoring, we pres-
ent the combined statistics of each ecosystem in
the table below.

![Open Source Adoption as Projected for 2023]
FIGURE 1.1
OPEN SOURCE ADOPTION AS PROJECTED FOR 2023
| Ecosystem | Total Projects | Total Project Versions | 2023 Annual Request Volume Estimate | YoY Project Growth | YoY Download Growth Estimate | Average Versions Released per Project |
|---|---|---|---|---|---|---|
| Java (Maven) | 557k | 12.2M | 1.0T | 28% | 25% | 22 |
| JavaScript (npm) | 2.5M | 37M | 2.6T[^2] | 27% | 18% | 15 |
| Python (PyPI) | 475k | 4.8M | 261B[^3] | 28% | 31% | 10 |
| .NET (NuGet Gallery) | 367k | 6M | 162B[^4] | 28% | 43% | 17 |
| Totals / Avgs | 3.9M | 60M | 4T | 29% | 33% | 15 |

[^1]: https://pypl.github.io/PYPL.html Accessed August 2023
[^2]: Figure estimated using npm download counts to from January to August 2023 as queried from https://github.com/npm/registry/blob/master/docs/download-counts.md
[^3]: YoY growth estimated based on known PyPI downloads from January to August 2023 as queried from https://console.cloud.google.com/marketplace/product/gcp-public-data-pypi/
[^4]: YoY growth estimated based on known NuGet Gallery downloads from January to August 2023 as queried from https://www.nuget.org/stats

7

C H A P T E R  1 :  O P E N  S O U R C E  S U P P LY  A N D  D E M A N D
### Open source supply sees a resurgence
The supply side of open source is an interesting
metric to gauge the pace and scale of innovation
that occurs in a given ecosystem. The more open
source projects are published every year, the
more innovation occurs in a given ecosystem.

New open source projects across the monitored
ecosystems have been published at a relatively
steady 15% average rate[^5] in recent years, which
was a signiﬁcant reduction in pace from highs
seen in 2019 and before.

![Open Source New Project Growth Rate Over the Past 4 Years]
FIGURE 1.2
OPEN SOURCE NEW PROJECT GROWTH RATE OVER THE PAST 4 YEARS

![Open Source Projects and Versions Growth]
FIGURE 1.3
OPEN SOURCE PROJECTS AND VERSIONS GROWTH

[^5]: In the 2021 report, we used a diferent method of estimating project counts for NuGet which resulted in a reduced number of projects being reported in 2022. We have corrected the NuGet historic numbers based on
statistics published by the NuGet Gallery.

8

C H A P T E R  1 :  O P E N  S O U R C E  S U P P LY  A N D  D E M A N D
This two-year slump is most likely related to
the COVID-19 pandemic period and associated
slowdown. While some studies suggest produc-
tivity did increase during the 2020-2023 period
in the U.S., a negative correlation emerges in
open source production trends. This is further
supported by another study that found produc-
tivity rates in information and communication
technology did decline towards 2022. One
other explanation could be that a lot of these
projects are in fact coming from commercial
activity and not people with spare time, which
was in abundance during the pandemic.

To date, the data in 2023 shows the innovation
slowdown is now over. Each monitored ecosys-
tem showed a remarkably consistent project
growth rate, varying just 2% across all four
monitored ecosystems to a total average growth
rate of 29% year-over-year.

The rate of production growth is recovering
across the board, and both Maven Central and
NuGet are on track to exceed the rate of growth
seen in 2020.

PyPi and npm, although growing, have not yet
caught up to their original rate of growth but are
on an upward trend. In a later section, we will
see how breakthroughs and interest in AI and its
related tooling are fueling the rate of growth in
these ecosystems.

Between 2022 and 2023, the number of avail-
able open source projects grew an average
of 29%. The average open source project in
2023 has released 15 versions available for
consumption, with speciﬁc ecosystem averages
ranging from 10 to 22 across the diferent open
source registries. That means 1-2 new versions
every month and adds up to 60 million com-
bined releases made available in the observed
ecosystems.

### Open source consumption is decelerating
While we’re seeing supply increase, consump-
tion isn’t keeping pace. The rate of download
growth in open source consumption has slowed
the past two years. In 2023, this trend continued
with the average download growth rate sitting at
33%, which is exactly what it was last year. This
is a stark comparison to the all-time high of 2021,
which saw 73% year-over-year growth. There
is a sign of slowdown in growth in the largest
ecosystems, which is not surprising given the
market saturation they already have.

Despite this, both of the largest ecosystems,
Maven and npm, are each estimated to reach
over a trillion requests in 2023, with npm reach-
ing a staggering 2.6 trillion requests in total, con-
tinuing a modest growth that surpasses the total
request rate of PyPI in 2022.

These two ecosystems account for 90% of the
requests served with the remaining two growing
at above average pace.

![Cumulative Estimated Requests per Ecosystem Over 6 Years]
FIGURE 1.4
CUMULATIVE ESTIMATED REQUESTS PER ECOSYSTEM OVER 6 YEARS

9

C H A P T E R  1 :  O P E N  S O U R C E  S U P P LY  A N D  D E M A N D
Requests are the fundamental measure of
how popular an open source ecosystem is and
how lively its usage is. Other factors within an
ecosystem may vary, such as the larger size
and complexity of Java packages compared to
JavaScript packages.

Investigating the rate of growth for requests
can reveal information about the state of open
source adoption, as well as the growth of the
software industry at large.

Figure 1.5 charts these individual growth rates
over time and displays an average across all 4
ecosystems.

Download requests for all open source ecosys-
tems are still growing, but for a third year in a
row there are signs that the pace of growth is
slowing down.

We can see a clear delineation between the
stabilization of large ecosystems like Maven and
npm, and continued accelerated growth in PyPI
and NuGet.

Figure 1.6 charts the overall aggregate request
growth across all ecosystems. It illustrates that
although the pace of growth is slowing down,
the absolute scale of growth continues to com-
pound on previous years’ rates. To put it simply,
the pace of open source adoption still shows no
signs of stopping.

![Growth Rate of the Monitored Open Source Ecosystems Over 5 Years]
FIGURE 1.5
GROWTH RATE OF THE MONITORED OPEN SOURCE ECOSYSTEMS OVER 5 YEARS

![Total Open Source Requests Over 6 Years]
FIGURE 1.6
TOTAL OPEN SOURCE REQUESTS OVER 6 YEARS

2023 BY THE NUMBERS
2.1 trillion
projected request volume
32%
YOY growth estimated
JAVASCRIPT
261 billion
projected request volume
31%
YOY growth estimated
PYTHON
162 billion
projected request volume
43%
YOY growth estimated
.NET
JAVA
1 trillion
projected request volume
25%
YOY growth estimated

10

C H A P T E R  1 :  O P E N  S O U R C E  S U P P LY  A N D  D E M A N D
### Individual ecosystem analysis
#### Java (Maven)
Through the ﬁrst 7 months of 2023, 512 billion Java
components were requested from the Maven Cen-
tral Repository. This is a signiﬁcant jump compared
to the 821 billion requests in 2022.

Java continues to grow at a healthy pace, hitting
an estimated 25% YoY request growth rate. If
previous years are any indication, we may well
see a spike towards the end of the year.

#### JavaScript (npmjs)
npm is the juggernaut of open source registries,
with an estimated download request count of
over 2.6 trillion components (or to display it in
full numbers: 2,579,310,885,518).

The growth of npm is the slowest of all the mon-
itored ecosystems — estimated to be at 18%
YoY. Nevertheless, owing to npm’s substantial
footprint, this translates to a staggering 400 bil-
lion requests, surpassing the combined total of
requests served by PyPI and NuGet.

#### Python (PyPI)
Python continues to expand at a high pace,
fueled by the language’s popularity and innova-
tive uses, including AI. In 2023, PyPI served over
178 billion requests. This year, we estimate PyPI
request volume will hit 261 billion packages. This
represents 31% YoY growth.

#### .NET (NuGet)
NuGet is the chosen ecosystem of the .NET
family of languages and continues to serve engi-
neers working with the growing set of Microsoft
technologies. The rate of growth in NuGet is
estimated to be the fastest amongst the cohort.
Developers downloaded 113 billion NuGet pack-
ages in 2022, which was well above our estimate
last year. In 2023, NuGet is estimated to serve 162
billion requests, representing 43% YoY growth.

### Open source software security concerns see no sign of slowing
In 2022, we reported a massive increase in the
growth of malicious attacks on the software
supply chain. Since our last report, this method
of propagating security threats using trusted
developer utilities and ecosystems has contin-
ued to evolve and ﬂourish.

A troubling trend has emerged in the soft-
ware supply chain over the past few years
of tailor-made packages designed to run a
malicious payload on download — without any
developer interaction. This form of intrusion
relies on developers not recognizing that the
build breakage resulting from the fake package
might be an indication that something nefarious
has already happened on their system. We did a
deep dive into types of malicious attacks in last
year’s report.

11

C H A P T E R  1 :  O P E N  S O U R C E  S U P P LY  A N D  D E M A N D
In our YoY monitoring, at the time of writing in
September 2023, we have logged 245,032
malicious packages — meaning in the last year,
we’ve seen the number of malicious packages
tripled. Looking at it a diferent way, it also indi-
cates that in one year alone, we’ve seen twice
as many supply chain attacks as the cumulative
numbers in previous years
This pace of growth is astonishing. It signals
the role of the supply chain as one of the fast-
est growing vectors for adversaries to execute
malicious code. Furthermore, we have seen an
increase in nation-state actors leveraging these
vectors (see our deep dive section below).

This is alarming news. Even though many open
source ecosystems have implemented new
security policies, such as mandatory MFA, they
usually only address the issue of protecting
existing open source publishers from attack.
Often, packages containing malicious code
are treated very similarly to packages with new
security vulnerabilities — and they are taken
down entirely based on a volunteer efort follow-
ing a vulnerability removal process, which is not
appropriate when the code is designed to be
malicious from the start. This approach can lead
to the malicious packages being up longer than
necessary, leaving developers at risk.

### Notable malicious packages and vulnerabilities
As we continue to document an overall rise in
malicious attacks on open source ecosystems,
the monitored 2022-2023 period has also seen
more professional criminal campaigns emerge.
The software supply chain lends itself well to the
cybercriminal ecosystem — either as an initial
access vector to Initial Access brokers or even
as a means of distributing initial access malware
for Advanced Persistent Threat groups. Here are
several examples we’ve seen this year:

#### Lazarus created PyPI package ‘VMConnect’ imitates VMware vSphere connector
In August 2023, Sonatype discovered a mali-
cious Python package, ‘VMConnect,’ on PyPI,
which mimics a legitimate VMware module. This
is part of a wider cyber campaign called “Paper-
Pin,” and is widely thought to originate from the
Lazarus Group, a North Korean state-afliated
organization. The packages aim to download
further malicious payloads from attacker-con-
trolled URLs. The focus on VMware, a wide-
ly-used virtualization platform, is particularly
concerning, as a successful compromise could
have far-reaching implications for enterprise
networks and is widely attractive to state afli-
ated actors. Read our full deep dive

![Next Generation Software Supply Chain Attacks (2019-2023)]
FIGURE 1.7
NEXT GENERATION SOFTWARE SUPPLY CHAIN ATTACKS (2019-2023)

#### ChatGPT histories were uncovered due to a vulnerability in Redis component used by OpenAI
In March of 2023, ChatGPT users experienced
a data leak where chat histories displayed other
people’s queries. OpenAI identiﬁed the issue
as a race condition vulnerability in an open
source component called Redis, which they use
for caching user data. This ﬂaw made sensitive
data of about 1.2% of ChatGPT Plus subscribers
accessible to others. The vulnerability was exac-
erbated by a recent server change that increased
the probability of the race condition occurring.
The issue underscores the importance of even
rarely occurring vulnerabilities, especially in
widely-used components like Redis, given their
potential to cause widespread disruption and
data exposure. Read our full analysis.

#### PyTorch namespace confusion attack targets utilities aimed at AI developers
In the past couple of holiday seasons, we’ve
seen some big supply chain attacks, including
one on PyTorch, a popular machine learning
framework. The attackers used a tactic known
as namespace confusion to speciﬁcally go after
the experimental “nightly” build of PyTorch. They
managed to steal sensitive data, signaling that
hackers are increasingly setting their sights on
AI and machine learning tools. These tools are
becoming more critical in various sectors, mak-
ing them attractive targets. While only the exper-
imental build was hit, the incident serves as a
wake-up call for better security in the booming
AI ﬁeld. Read our full analysis.

#### A timeline of attacks
We have continued to curate a timeline of
known malicious packages and malware cam-
paigns. This interactive timeline summarizes
notable supply chain incidents, next-gen attacks
and other incidents propagated using the soft-
ware supply chain.

### Differentiating software vulnerabilities and malware
Up until now, we’ve been talking about malware
and malicious attacks on the software supply
chain - or maybe better stated as malware prop-
agated using the open source supply chain. In
this next section, we’re going to discuss soft-
ware vulnerabilities. While the two concepts are
related, they are very distinct, so we’d like to
quickly deﬁne the diference between a vulnera-
bility and a malware.

#### Software vulnerability: A flaw in the code
A software vulnerability is akin to a ﬂaw in code,
much like a faulty lock on a door. However,
unlike malware, vulnerabilities are not inten-
tional. Instead, they represent weaknesses in
software components or projects.

Similar to how a faulty lock compromises the
security of a building by allowing unauthorized
access, a software vulnerability creates a gap
in the software’s security perimeter. This gap
becomes an entry point for intruders to exploit,
gaining unapproved access to the system, appli-
cation, or component.

#### Malware: Malicious intent in open source
Malware, short for “malicious software,” poses a
signiﬁcant threat to open source software eco-
systems. It encompasses a wide range of mali-
cious programs, such as viruses, worms, trojans,
ransomware, spyware, and adware, all designed
to gain unauthorized access to information or
systems.

With its various forms, malware’s primary pur-
pose is to steal data, install harmful software,
gain control of a network, or compromise soft-
ware or hardware. Threat actors employ diverse
distribution methods, such as infected email
attachments, malicious websites, or compro-
mised software downloads.

### Consumption behavior contributing to security concerns
Our report last year revealed a startling statistic —
nearly 96% of component downloads with known
vulnerabilities could be avoided as a better, ﬁxed
version is already available. This illustrates a clear
need for organizations to pay closer attention to
what versions they are adopting.

12

C H A P T E R  1 :  O P E N  S O U R C E  S U P P LY  A N D  D E M A N D
13

C H A P T E R  1 :  O P E N  S O U R C E  S U P P LY  A N D  D E M A N D
![Software Supply Chain Attacks, Dec 2021–August 2023]
FIGURE 1.8
SOFTWARE SUPPLY CHAIN ATTACKS, DEC 2021–AUGUST 2023

There is widening evidence that whatever the
standard practice for avoiding vulnerable com-
ponents today, the controls are not having the
efect needed to reduce the attack surface. For
example, as of September 2023, downloads vul-
nerable to the infamous Log4Shell vulnerability
still account for nearly a quarter of all net new
downloads of Log4j. It should be highlighted,
that almost two years after the initial ﬁnding of
this vulnerability, we’re seeing this pace con-
tinue every week — that a quarter of all down-
loads are of the vulnerable version of Log4j.
This is only part of the story. The reality is, nearly
1/3 of all Log4j downloads, ever, are of the vul-
nerable version.

As we discussed last year, the numbers for other
critical vulnerabilities that have not received
as much widespread media attention are even
more depressing.

This warrants concern and calls for behavioral
adaptation at organizations because critical vul-
nerabilities are widely exploited by bad actors,
even at the state level. For example, Log4S-
hell has topped CISA/NSA charts for active
state-sponsored exploitation for well over a
year now. This is also echoed in the OpenSSF’s
recently released Consumption Manifesto,
which calls for organizations to take respon-
sibility for the open source they use, how it is
consumed, and how they manage the risk asso-
ciated with that consumption.

According to a joint consortium of national oper-
ators including CISA, NSA, NCSC-UK and oth-
ers, attackers are exploiting older well-known
vulnerabilities much more frequently than new
zero-day vulnerabilities. This is extremely
important to understand. While we should of
course worry about zero-days, we also know
that 96% of vulnerable open source downloads
have a non-vulnerable ﬁx available. Those 96%
need to be addressed.

For this year’s report, we’ve taken a closer look
at how vulnerabilities are consumed from Maven
Central, with a special focus on what sort of geo-
graphic variance might exist.

#### Vulnerable components consumed
Let’s start of by looking at the top level. In 2022
we saw 12% of downloads served by Maven
Central[^6], contained at least one known security
vulnerability.

This number is important when considering that
the easiest way to reduce risk of a supply chain
incident caused by a vulnerability is to simply
choose a better, non-vulnerable version of a
component.[^7] There is some improvement in
these however, the number of vulnerable down-
loads in 2021 was 14% — and the number to date
in 2023 sits at around 10%.

[^6]: Countries and regions with over 100,000 annual requests
[^7]: A limitation in this report is that the numbers reported are of security vulnerabilities known as of August 2023, even when inspecting retrospectively. The amount of vulnerabilities known at the time of download might
have been lower, which might partially explain the improvement over time.

14

C H A P T E R  1 :  O P E N  S O U R C E  S U P P LY  A N D  D E M A N D
249,556,989
total Log4j downloads since Dec 15,
2021 | 29% vulnerable
23%
Vulnerable downloads (Aug 20–27,
2023) | 3,490,799 total downloads
According to a joint
consortium of national
operators including
CISA, NSA, NCSC-UK
and others, attackers
are exploiting older well-
known vulnerabilities
much more frequently
than new zero-day
vulnerabilities.

[^8]: As