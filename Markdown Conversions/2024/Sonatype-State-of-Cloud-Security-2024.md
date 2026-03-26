# State of the Software Supply Chain 2024

## Table of Contents
- [Executive Summary](#executive-summary)
- [10 Year Look Back](#10-year-look-back)
- [Attackers and the Evolution of Software Supply Chain Exploits](#attackers-and-the-evolution-of-software-supply-chain-exploits)
- [Consumers of Open Source](#consumers-of-open-source)
- [Publishers of Open Source](#publishers-of-open-source)
- [SBOM Production by Open Source Projects](#sbom-production-by-open-source-projects)
- [A Decade of Software Regulations](#a-decade-of-software-regulations)
- [Navigating the Future of Open Source and Software Supply Chain Security](#navigating-the-future-of-open-source-and-software-supply-chain-security)
- [Scale of Open Source](#scale-of-open-source)
- [Individual Ecosystem Analysis](#individual-ecosystem-analysis)
- [Differentiating Software Vulnerabilities and Open Source Malware](#differentiating-software-vulnerabilities-and-open-source-malware)

---

## Executive Summary

As we mark the 10th annual State of the Software Supply Chain report, the transformation of open source software has been nothing short of profound. Open source consumption has exploded, with estimates placing this year’s downloads at over 6.6 trillion. This reliance on open source components, now making up to 90% of the modern software application, has ushered in both unprecedented innovation and complex challenges for software supply chains. Because of this, the industry has also become increasingly regulated, moving from a hands-off approach in the early 2010s to proactive frameworks that address growing cybersecurity risks in the global software supply chain.

This year’s report, backed by data from over 7 million open source projects, double-clicks on many of the unsettling trends in security and risk management we’ve been following in the past 10 reports. Notably, the rise of open source malware and software supply chain attacks has become a critical threat. Examples such as the LUMMA malware found in PyPI and the XZ Utils package backdoor highlight the growing sophistication of these attacks, which often bypass traditional security measures, leaving organizations vulnerable. In fact, the number of malicious packages has grown by 156% year-over-year, posing a significant risk to enterprises that fail to manage their OSS dependencies effectively.

### Open Source Scale and Consumption Behaviors
Open source software adoption is at a multitrillion request scale, with ecosystems like JavaScript (npm) and Python (PyPI) leading the charge:
- JavaScript (npm) accounted for a staggering 4.5 trillion requests in 2024, representing 70% year-over-year growth in requests.
- Python (PyPI), driven by AI and cloud adoption, is estimated to reach 530 billion package requests by the end of 2024, up 87% year-over-year.

Over 512,847 malicious packages have been logged just in the past year, a 156% increase year-over-year, highlighting a critical need for organizations to adapt their consumption practices.

### Persistent Risk and Consumer Complacency
We introduce the concept of “Persistent Risk,” a combination of unfixed and corrosive vulnerabilities that continues to erode the security integrity of software over time.
- 80% of application dependencies remain un-upgraded for over a year, even though 95% of these vulnerable versions have safer alternatives readily available.
- Only 0.5% of OSS components have no available update (No Path Forward).
- 3.6% of dependencies are still vulnerable because they were updated to another insecure version.

### Efficiency and Waste: The Time Drain on Developers
- Size of application does not matter—with the average applications containing 180 components, even small applications face unmanageable workloads.
- 92% of crowdsourced or publicly available data needed a correction once reviewed by a security researcher.
- 69% of vulnerabilities initially scored below 7 were corrected to 7 or higher on the CVSS scale upon closer review.

### A Call to Action and Vigilance
Organizations must prioritize an advanced SCA tool that helps by selecting high-quality, well-maintained components, addressing risks as early as possible, and remaining vigilant against the evolving landscape of supply chain attacks. Projects using a Software Bill of Materials (SBOM) to manage OSS dependencies showed a 264-day reduction in mean time to remediate (MTTR) compared to those that did not.

---

## 10 Year Look Back

As we look back on 10 years of data collection, this retrospective examines four key dimensions: attackers, publishers, consumers, and regulators.

![Chart showing 10-year growth metrics including 1,466% growth in release frequency and 463% CVE growth]

An SBOM mandate when it was first suggested 10 years ago (via the Royce Bill) could have redefined software security and stopped today’s supply chain attacks before they began.

## Attackers and the Evolution of Software Supply Chain Exploits

Over the past decade, the software supply chain has become a primary attack vector.
- **2014–2016**: Early warnings via Apache Struts, Heartbleed, and Shellshock.
- **2017**: The Equifax breach marked a turning point, signaling the shift from opportunistic to targeted exploitation.
- **2020**: SolarWinds demonstrated the growing sophistication of threats, infiltrating build environments.
- **2021**: Log4Shell demonstrated how vulnerabilities in obscure components ripple through the entire ecosystem.
- **2024**: The attempted XZ Utils attack marked a dangerous escalation, utilizing the “benevolent stranger” playbook to gain maintainer trust over two years.

## Consumers of Open Source

The profile of open source consumers has expanded from developers to enterprises and government agencies. Despite this, consumption practices remain poor. 13% of Log4j downloads are still for known vulnerable versions, nearly 3 years after the vulnerability’s discovery.

## Publishers of Open Source

From 2010 through 2024, there has been a consistent increase in the number of projects where release frequency grew year-over-year. However, by 2024, over 300,000 projects had slowed or halted their release cadence, indicating burnout or resource shortages. Furthermore, the mean time to remediate (MTTR) vulnerabilities has increased significantly, with some projects taking over 400 days to release secure updates.

## SBOM Production by Open Source Projects

While we have seen progress in the number of projects publishing SBOMs (CycloneDX and SPDX v3), the growth is essentially linear. In the last 12 months, 60,813 SBOMs were published compared to 6,971,092 components published. We are not keeping up with the pace of component releases.

## A Decade of Software Regulations

The 2020s have witnessed a surge in regulatory action:
- **2014**: Cyber Supply Chain Management and Transparency Act (Royce Bill).
- **2021**: U.S. Executive Order 14028.
- **2023**: EU DORA, NIS2 Directive, and CISA Secure by Design framework.
- **2024**: EU Cyber Resilience Act (CRA).
- **2025**: ASEAN unified cybersecurity regulatory framework.

## Navigating the Future of Open Source and Software Supply Chain Security

The future of the software supply chain will depend on our ability to meet these challenges head-on. As regulations continue to evolve and attackers grow more sophisticated, organizations must embrace comprehensive security measures and foster collaboration across the industry. 95% of the time, when vulnerable components are consumed, a fixed version already exists.

## Scale of Open Source

Open source adoption has reached a multi-trillion request scale.
- **Java (Maven Central)**: 1.5 Trillion estimated requests.
- **JavaScript (npm)**: 4.5 Trillion estimated requests.
- **Python (PyPI)**: 530 Billion estimated requests.
- **.NET (NuGet)**: 159 Billion estimated requests.

## Individual Ecosystem Analysis

- **Java (Maven)**: High version density (avg 28 versions per project).
- **JavaScript (npm)**: Titan of volume, heavily distorted by spam packages aiming to redeem crypto rewards.
- **Python (PyPI)**: Fastest grower in project creation and request volume, fueled by AI and cloud adoption.

## Differentiating Software Vulnerabilities and Open Source Malware

- **Software Vulnerability**: A flaw in the code (unintentional). Like a faulty lock on a door.
- **Malware**: Malicious intent (intentional). Designed to steal data or gain unauthorized access, often passed off as legitimate components or introduced via project takeovers.

---
© 2015-PRESENT, SONATYPE INC. ALL RIGHTS RESERVED.

---

software, gain control of a net-
work, or compromise software or hardware. Threat actors
employ diverse distribution methods, such as infected
email attachments, malicious websites, or compromised
software downloads.

Malware in the software supply chain is designed to tar-
get developer environments, like continuous integration
systems and are commonly seen in ransomware attacks
and sophisticated breaches. The only known cure is
prevention and avoidance.

D E F I N I I T I O N S :   S O F T WA R E  V U L N E R A B I L I T Y  V S .   M A LWA R E

A software vulnerability
creates a gap in the software’s security
perimeter, similar to how a faulty lock
compromises the security of a building by
allowing unauthorized access.

Malware’s primary purpose
is to steal data, install harmful software,
gain control of a network, or compromise
software or hardware.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN

29
2929

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINSCALE OF OPEN SOURCEVulnerabilities in the
Open Source Ecosystem

Security vulnerabilities are a fact of life — as technology
evolves and ages, it also requires maintenance. New issues
are discovered at a rate over time, and thus it’s important to
acknowledge that vulnerabilities appear all the time. A good
analogy is to think software components age like milk, not
fine wine (or a new analogy you’ll see when we talk more
about risk, it’s more like steel than aluminum) — they don’t
get better with age. They might be good for a long time, but
when a vulnerability is discovered, it’s akin to spoiled milk —
something that needs to be discarded quickly.

The challenge, of course, is the scale of new security
vulnerabilities being discovered in the different ecosys-
tems, as well as the scale of issues being discovered in
the software you manage.

N A T I O N A L  V U L N E R A B I L IT Y

D A T A B A S E  B A C K L O G

17,656

The backlog of published but unprocessed
vulnerabilities at the National Vulnerability
Database, at the time of writing.

13

The average number of Critical or High
severity security vulnerabilities being
discovered each year, per application.

Organizational Challenges
A few fundamental facts — last year we reported that the
average Java application has about 150 open source
components when counting both direct and transitive
dependencies. On average, an application has 13 Critical or
High severity security vulnerabilities being discovered each
year. Depending on the size of the organization, the effort
to remediate issues can vary wildly, from a few minutes to a
few days, depending on the breaking changes needed to
go from the current version to the non-vulnerable one.

Another challenge is the source of information about
security vulnerabilities itself — in 2024, it has become evi-
dent that relying on free sources of information is almost
considered neglectful for any organization not specializ-
ing in intelligence aggregation.

For example, the National Vulnerability Database, the
canonical catalog of known security vulnerabilities via the
Common Vulnerability Enumeration System (“CVE”), had
an outage early 2024 that caused a massive backlog of
vulnerabilities being published. At the time of writing, this
backlog of published vulnerabilities sits at 17,656 unpro-
cessed issues. This meant that in Q1 of this year, nearly no
new security issues were made available to the community.

The volume of security vulnerabilities discovered is
growing in linear ratio with the growth rate of open
source being invented and published. This is to be
expected and is uncomfortable news for organizations
seeking to manage them.

3030

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINSCALE OF OPEN SOURCESCALE OF OPEN SOURCE
EXECUTIVE SUMMARY

Open Source Malware & Next
Gen Supply Chain Attacks are Now
Commonplace, Dangerous Business

The growth of downloads hides a disturbing fact — the
continued extreme growth of malware, protestware,
and intentionally hidden vulnerabilities passed on to the
users. These types of packages are published not due
to carelessness, but with purely malicious intent. Using
open source as a medium of transport for malware isn’t
new. However, traditional scanning tools struggle to iden-
tify novel attacks, like we now see with malicious pack-
ages, otherwise known as open source malware. These
tools, while effective on known malware, are incapable of
finding malware that has not yet been identified.

Some have noble intentions, such as packages that pro-
test wars around the world, while some hide extremely
sinister motivations, including serious malware families
and ransomware gangs that sell off their victims to the
highest bidder. Every single one of them targets an often
undefended prey: developers and automated build
environments.

A great example of a successful malicious campaign tar-
geting developers is the Snowflake breach of 2024, where
developers were specifically targeted with malware fami-
lies that stole Snowflake authorization tokens. These were
later used to breach over 160 organizations.

In our YOY monitoring, at the time of writing in August
2024, we have logged 704,102 malicious open source
packages — meaning in the last year, we’ve seen the
number of malicious packages grow by 156% YOY. More
troublingly, we observe via an anonymous survey con-
ducted on more than 100k repositories that over 50% of
unprotected instances surveyed have already fallen vic-
tim and cached a piece of malware.

A sobering finding in this year’s data is that more than
512k new pieces of malware have been introduced to the
public binary repositories, with 65K of them being CVSS
>= 7 since November 2023. All of these represent yet
another facet of Persistent Risk (read more about this in
our Risk chapter), and bring a total data set of more than
700k identified, malicious open source components.

FIGURE 2.6
Next Generation Software Supply Chain Attacks (2019–2024)

Next generation software supply chain attacks (2019-2024).

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN

31
31

Malware Types

FIGURE 2.7
Malware Types Observed

As with ‘traditional’ malware, malware disguised as open
source comes in many guises and types. What is not tra-
ditional with open source malware is that it is executed
entirely without developer interaction. Once the package
is downloaded on the developers or build automation
machine it is too late to avert disaster.

Potentially Unwanted Application - 46.4%
A majority of the malware we observe being spread in
the open source ecosystem is what we call “Potentially
Unwanted Application” or PUA, which represents func-
tionality that is present in the software but not disclosed
to the end user. Examples of this include protestware,
anti-work protests, and other uninvited functionalities.
Though mostly innocent in practice, they represent a lack
of process in getting packages and act as evidence of a
hole in an organization’s open source defense.

Phishing - 13.8%
These types of packages leverage attack methods such
as dependency confusion to target organizations directly,
pretending to be an internally developed package. They
trick an organization’s build automation into downloading
them and often drop malware as they are downloaded.

Data Exfiltration - 13.7%
Data exfiltration packages read a number of pieces of
data found on the machine, such as environmental vari-
ables, authentication tokens, password files and anything
that might aid the assailant. Once collected, these files
are uploaded to an external command and control server
for future use.

Security Holding Package - 12.7%
These are packages that were found to be malicious, but
got removed by the maintainers of the ecosystem and
replaced by a holding package. Requires swift actions of
the upstream maintainers to avert disaster.

Malware types observed.

PII Exfiltration - 2.8%
A form of data exfiltration that targets Personally Identifiable
Information like personal access tokens and information.

Backdoor - 1.9%
A package that installs a backdoor virus onto the machine
that executes it. This backdoor will allow the attacker to
access the tainted machine at a later date.

Crypto Stealer / Miner - 1.2%
These types of packages aim to make money fast by
stealing any available cryptocurrency housed on the
affected machine. This category also includes pack-
ages that drop a crypto miner that hijacks the machine’s
resources to mine cryptocurrency for the hacker’s benefit.

3232

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINSCALE OF OPEN SOURCEResearch Project - 1.2%
Some malware is simply a research project, either by a
researcher or a whitehat hacker that contains malicious
code but typically does not go so far as to breach the
machine or steal information. They are often seen during
penetration tests.

Dropper - 0.7%
As the name suggests, these types of packages drop
an encrypted payload onto the affected machine, often
a Remote Access Trojan that disappears from sight and
allows hackers to return at a later date.

Other types of malicious packages - 6.8%
The rest of the malicious packages discovered range from
destructive ones aiming to corrupt the file system they
launch on, to aiming to affect the code that a developer
writes, often seen disguised as IDE or CI plugins.

Traditional malware scanning solutions are unable to
detect these novel forms of attack, leading developers
and DevOps environments to be uniquely at risk. As the
volume continues to grow so too will the clear and present
danger facing organizations.

A T I M E L I N E   O F  AT TAC KS

We have continued to curate a timeline of known malicious packages and malware campaigns. This interactive
timeline summarizes notable supply chain incidents, next-gen attacks and other incidents propagated using the
software supply chain.

May

June

June

July

August

PyPI crypto-stealer
targets Windows
users, revives
malware campaign

Russia-linked
‘Lumma’ crypto
stealer now targets
Python devs

Polyfill.io supply
chain attack hits
100,000+ websites

Npm packages
conceal macOS
malware in ‘travis.
yml’ files, drop
bogus “Safari
Updates”

Ideal typosquat
‘solana-py’ steals
your crypto wallet
keys

SEE THE FULL TIMELINE

3333

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINSCALE OF OPEN SOURCENotable Malicious Packages

As we continue to document an overall rise in malicious attacks on open source ecosystems,
the monitored 2023–2034 period has also seen more professional criminal campaigns
emerge. The software supply chain lends itself well to the cybercriminal ecosystem — either
as an initial access vector to Initial Access brokers or even as a means of distributing initial
access malware for Advanced Persistent Threat groups.

LU M M A   M A LWA R E   F O U N D   I N   PY P I   PAC K AG E
In the summer of 2024, packages published in the PyPI ecosystem were found to distribute the LUMMA
malware upon install. This malware family is linked to Russian state-affiliated hacking groups and was
reported to be a part of the information stealers used to execute the Snowflake breach of 2024.

READ OUR DEEP DIVE

T E A . X Y Z   S PA M   F LO O D S   N P M
Throughout the course of the summer of 2024, npmjs.org was flooded under a deluge of malicious
packages that intended to game a well-intentioned crypto rewards scheme called Tea. It was originally
intended as a rewards scheme to compensate developers for contributing to open source.

READ OUR ANALYSIS

X Z   PAC K AG E   H E I ST  N E A R LY  C O M P R O M I S E S   T H E
WO R L D ’ S   S E RV E R S   W I T H  A  BAC K D O O R
Discovered in early 2024, the XZ Utils vulnerability is a smoking gun that proves malware is being
created intentionally by serious, well-funded actors. This sophisticated campaign targeted an over-
worked open source maintainer, and nearly managed to insert encrypted backdoor code that would
have granted the attacker a backdoor into nearly all of the world’s servers.

READ OUR ANALYSIS

3434

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEvolution of Open Source

RISK

In the 2015 edition of Sonatype’s State of the Software Supply Chain Report, we introduced the
concept that “components age like milk, not wine.” For our 10th report, we’ve refined the metaphor: most components
age more like steel, not aluminum.

Today, software organizations resemble manufacturers, assembling products from hundreds of open source compo-
nents. Like traditional manufacturing, the quality and longevity of components determine a product’s success.

Choosing high-quality components and committing
to rigorous maintenance practices is the key to build-
ing durable and secure software. Yet, despite known
risks, many organizations ignore these best practices
and use outdated components. This exposes them to
vulnerabilities and defects that could be avoided with
the right tools, data, and strategy.

Unlike industries where defective materials are
swiftly removed, software manufacturers tolerate
flawed parts from suppliers they haven’t vetted. A
vigilant approach to supply chain management is
essential to fully benefit from open source. Manufac-
turers must prioritize quality, monitor emerging risks,
and address risks throughout the software lifecycle to
ensure long-term security and reliability.

95%percentage of vulnerable downloaded

releases that already had a fix

3535

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEVOLUTION OF OPEN SOURCE RISKOpen Source Software Quality

Vulnerabilities can make headlines, but our research shows
that the best open source projects find and fix vulnerabil-
ities quickly. Unfortunately, the majority of open source
downloads are not of the fixed, non-vulnerable version.

For example, our previous research found that ~96%
of vulnerable downloaded open source components
had a newer, non-vulnerable version available at the
time of the download. As part of our analysis this year, we
reviewed and updated our algorithm completely. Despite
our revisions, that number decreased by less than 1%, high-
lighting a considerable deficit in changing open source con-
sumption behavior, an issue we dive deep into in this year’s
report’s Optimizing Efficiency & Reducing Waste section.

The magnitude of these figures is further punctu-
ated when looking at Log4j downloads. When writing
this report, 13% of all Log4j downloads were still of

a vulnerable version, even though a non-breaking,
non-vulnerable version existed. While this is significantly
better than the 30-35% we saw in our last report — nearly
three years since the Log4Shell vulnerability made head-
lines — that number should be much closer to 0.

Despite Log4Shell being one of the most well-known
vulnerabilities encountered in the last ten years, devel-
opment teams continue to introduce risk through known
vulnerabilities regardless of available fixes. Though, we
are happy to see the decrease, which shows that this
message is reaching some audiences.

Blaming open source alone is like pointing one finger
while three point back. While vulnerabilities exist, their
impact lies not in sheer numbers but in timely fixes and
the persistence of unfixed issues and risks. More import-
ant than the number of vulnerabilities is how quickly a
vulnerability is fixed and the number of remaining unfixed
vulnerabilities, as these factor into Persistent Risk.

FIGURE 3.1
Log4j Percent Monthly Central Downloads

Downloads of vulnerable versions of Log4J still greater than 10% nearly three years after fixes were available.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN

36
3636

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEVOLUTION OF OPEN SOURCE RISKPersistent Risk

Persistent Risk is new this year. Based on our research,
we found that risk is deeply impacted by ongoing expo-
sure to vulnerabilities that remain unresolved over time.
To support this, we defined Persistent Risk using two pri-
mary factors: Unfixed and Corrosive Risk.

•  Unfixed Risk refers to vulnerabilities within software
components that have been identified but have yet
to be addressed and, in many cases, will never be
addressed. It also incorporates the time it takes to
remediate a vulnerability. These known vulnerabilities
pose a continuous threat, leaving the software open to
exploitation.

•  Corrosive Risk impacts current and historical

releases. Like Unfixed Risk, corrosive risk considers
the time needed to resolve these vulnerabilities.

FIGURE 3.2
Persistent Vuln Risk = Unfixed Risk + Corrosive Risk

However, corrosive risk also incorporates the delay in
discovering vulnerabilities in old versions. The longer
it takes to find and resolve these issues, the more the
software is exposed to potential attacks.

When combined, these two factors create Persistent Risk —
a risk that remains unfixed and corrodes the software’s
security integrity over time.

Just as corrosion slowly eats away at the metal, a long
time to discover and fix increases the corrosive potential
of Persistent Risk. The longer vulnerabilities go undis-
covered and unfixed, the more they weaken the software,
making it increasingly susceptible to breaches and failures.
This corrosive potential is not just about the immediate risk
of a known vulnerability but also about how the delayed
discovery allows the risk to compound, leading to a grad-
ual and often unnoticed security degradation over time.

The image above shows an analysis of Persistent Risk.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN

37
3737

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEVOLUTION OF OPEN SOURCE RISKPersistent Risk = Unfixed Risk + Corrosive Risk.
As time increases without addressing vulnerabilities, the
risk becomes more ingrained, corroding defenses and lead-
ing to a fundamentally compromised state of security. This is
why promptly addressing vulnerabilities is essential — delay
leads to corrosion, which can lead to catastrophic failure.

Again, a finger may appear pointed at open source soft-
ware projects; however, our analysis indicates that the
best projects will address most vulnerabilities quickly.
Those projects are also more likely to improve their secu-
rity posture and software supply chain best practices using
tools like those in the Open Source Security Foundation’s
Scorecard. Our conclusion is that Persistent Risk is driven
more by open source consumption practices than by an
inherent quality issue with open source software.

Open Source Consumption

Over the past decade, poor open source consumption has
emerged as the clearest indication of risk in the software
supply chain. As we now focus on Persistent Risk, the role
of open source consumption has only grown.

T H R E E   FACTO R S   I N F LU E N C I N G  T H E

H E A LT H   O F   S O F T WA R E   S U P P LY   C H A I N S

Choice is determined by a software
manufacturer’s selection of open
source software.

Complacency becomes a risk when
software manufacturers fail to update
& manage dependencies.

Contamination occurs when open source
malware or malicious packages infiltrate
the software supply chain.

Persistent risk is driven more by open source
consumption practices than by an inherent
quality issue with open source software.

However, defining risky behaviors and helping organiza-
tions identify low-quality components remains challenging.

This year, we partnered with Tidelift, the CHAOSS Project,
and various open source software community members
to better understand how three specific factors of open
source consumption influence the health and security of
software supply chains.

•  Choice: Choice is determined by a software manufac-

turer’s selection of open source software. Making good
choices when choosing components is critical, mean-
ing software manufacturers should prioritize avoiding
projects with Persistent Risk to ensure a robust and
secure software supply chain.

•  Complacency: Complacency becomes a risk when soft-
ware manufacturers fail to properly update and maintain
their open source software by managing dependencies.
This negligence leaves them vulnerable to corrosion, as
vulnerabilities persist and accumulate over time.

•  Contamination: Contamination occurs when open
source malware or malicious packages infiltrate the
software supply chain, often targeting the development
infrastructure. Poor choice and complacency are high-
risk consumption factors that increase the likelihood
of contamination entering software supply chains. This
underscores the need for heightened awareness and
proactive measures to protect against these threats.

Continue reading to learn how these three risk factors
affect the analysis of 7 million open source projects.

3838

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEVOLUTION OF OPEN SOURCE RISKCan We Minimize Persistent Risk

For those seven million open source software projects,
we collected data at the component level and classified
each component into distinct groups based on their
usage in enterprise applications.

For our analysis, we considered two groups: core and
peripheral components. We took a representative and
statistically significant sample from each group, then
identified which key metrics had the potential to minimize
Persistent Risk.

We also categorized these components into three spe-
cialized groups. The key difference between the core
and peripheral component groups and the specialized
groups is exclusivity – components can only belong to
one of the core or peripheral groups, while the specialized
groups are inclusive. A component can simultaneously
be part of SBOM, Foundation Support, and Paid Support.

FIGURE 3.3
Specialized Groups by Usage

The diagram shows how the specialized groups intersect with the usage groups.

C O M P O N E N T  T Y P E S  A N A LY Z E D

Core
Components

Frequently found in
enterprise applications

Peripheral
Components
Rarely, if ever, found in
enterprise applications

Each specialized group is defined by distinct practices
that influence how an open-source project provides its
components.

•  SBOM — Components published with at least one
SBOM. Projects releasing an SBOM demonstrate
responsiveness to the emergent need for better soft-
ware supply chain management practices, and we
hypothesized that this points to better security practices.

•  Foundation Supported — Components that are part
of a project supported by a foundation like Apache,
Eclipse, or The Cloud Native Computing Foundation
(CNCF). Projects under a foundation receive guidance
and are part of a larger ecosystem with established
best practices, and we hypothesized that this points to
better security practices.

•  Paid Support — Commercial organizations, such as
Tidelift, pay the open source project maintainer. The
components are part of projects that receive funding and
are given the resources to address maintenance needs
that otherwise might not get attention. We hypothesized
that this also includes better security practices.

By analyzing projects through these lenses, we better
understand how different factors contribute to or mit-
igate the risks associated with open source software
consumption. This approach underscores the importance
of selecting the right projects, maintaining vigilance in
dependency management, and avoiding contamination
to minimize the long-term risks to software supply chains.

3939

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEVOLUTION OF OPEN SOURCE RISK762,000

the number of components actively
downloaded and used in software, of the
more than 7 million available

Choice

A key goal of this year’s report is to define what consti-
tutes high-quality open source components. This effort
stems from a core belief that the principles guiding sup-
ply chain best practices are equally applicable to the
software supply chain — a belief that remains unchanged,
though our understanding has deepened.

One of the most striking insights came from our analysis
of discoverability, which revealed the vast landscape
of open source projects. Despite the seemingly infinite
number of components available (more than seven mil-
lion), only a small percentage — 10.5% — are actively cho-
sen ( just over 762,000). This disparity between the pop-
ularity and usage of open source projects underscores
the significant noise developers must sift through when
choosing a component.

We also discovered that while it’s challenging to pinpoint
a single, definitive marker of high quality, there are key
indicators that collectively paint a clearer picture of what
quality is not. While no universal standard or indicator
exists today for consumers of open source software to rely
on, we identified a set of key heuristics. We tested them
against our data and analysis. These markers are designed
to help software developers make informed choices
regarding open source software projects (suppliers).

1.  Popularity is important: Aligning usage with the mass
of other users can be a helpful starting point. We found
that popular components have 63% more vulnerabil-
ities identified, address 54% more, and fix them 32%
faster (~50 fewer days). While this is a good heuristic, it
is not a foolproof quality measure in isolation.

2. Active communities manage software quality better:
Our analysis showed that active project communities
often correlate with better-managed software quality.
However, this relationship does not necessarily reduce
Persistent Risk.

FIGURE 3.4
Open Source Developer Choice

This pie chart shows developers’ challenge when choosing among millions of
components; nearly 90% will be noise.

4040

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEVOLUTION OF OPEN SOURCE RISK3. SBOMs demonstrate good supply chain practices:

Projects that publish a Software Bill of Materials (SBOM)
make supply chain management more manageable and
tend to exhibit lower Persistent Risk. Projects investing
in good supply chain practices, such as early adoption of
SBOMs, produce higher-quality software.

5. Stars and forks shed a light on community engagement:
Our analysis confirmed that the number of stars and
forks on an open source repository correlates with the
level of community engagement. However, this metric
alone may not reliably indicate the overall quality or
Persistent Risk of a project.

4.  OpenSSF Scorecard could help reduce Persistent Risk:
The OpenSSF Scorecard was assessed for its correla-
tion with Persistent Risk. While it provides valuable
insights into various security practices, its effective-
ness as a standalone predictor of low Persistent Risk
remains inconclusive and requires further exploration.

As we refined this list, it became clear that while there are
heuristics that point towards quality, every measurement
should ultimately be assessed against risk. But risk itself
is more complex than the mere existence of a vulnera-
bility. Many projects have vulnerabilities, but how they
respond to them matters.

Based on our definition of Persistent risk, two metrics
are critical: fix rate and time to remediate across usage
and specialized groups.

FIGURE 3.5
Average Unfixed Vulnerabilities by Severity

FIGURE 3.6
Mean Time to Remediate Vulnerabilities by Severity

This chart displays the Average Unfixed Vulnerabilities by Severity.

This bar graph shows the average number of vulnerabilities by severity
(Critical, High, Medium, Low) across different groups (Core Components,
Peripheral Components, SBOM, Foundation Support, Paid Support).

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN

41
4141

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEVOLUTION OF OPEN SOURCE RISKThe Impact of Foundation Support
on Open Source Quality

Our analysis highlights a compelling trend: open source projects supported by recognized foundations, such as
the Apache Software Foundation, Eclipse, and the Cloud Native Computing Foundation, consistently outperform
non-foundation-supported projects across several key quality metrics.

Security Practices: Foundation projects are
4.1x more likely to have formal vulnerability
reporting and have a 94% higher fix rate,
showing proactive security measures.

Community Engagement: Foundation
projects have 265% more forks and 162%
more stargazers on GitHub, reflecting
broader interest and quicker updates.

Vulnerability Management: Foundation
projects resolve security issues 264 days
faster on average, minimizing risk exposure.

Release Cadence: With 72% fewer days
since their last update, foundation projects
show better maintenance, while non-
foundation projects are more prone to
becoming obsolete or reaching EOL.

Issue Management: While foundation
projects have more active issues, they close
1.8x more, ensuring sustained momentum
and backlog reduction.

Code Freshness: Non-foundation projects
use dependencies that are, on average,
10 libyears older, increasing the risk from
outdated components.

FIGURE 3.7
Comparing Open Source Foundation Supported
Components  to Components Without Foundation Support

The chart shows how foundation-supported open source components reduce risk.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN

42
4242

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEVOLUTION OF OPEN SOURCE RISK
FIGURE 3.8
Simulation: Impact of Unfixed
Vulnerabilities on Risk Growth

FIGURE 3.9
Simulated 1 Year Impact of Unfixed
& Time to Remediate on Vulnerabilities

This chart displays the Average Unfixed Vulnerabilities increasing in severity.

This graph shows the average number of vulnerabilities.

Next, we evaluated these metrics across the identified
groups to simulate a practical example of how Persistent
Risk is driven by the number of unfixed vulnerabilities and
the time (days) it takes to fix them.

In our data, SBOMs had a higher incidence of vulnera-
bilities, yet their ability to quickly address and fix most of
those vulnerabilities makes a significant difference.

The chart above demonstrates how unfixed vulnerabili-
ties can grow exponentially when not addressed. Consid-
ering the scale over the ten years we’ve been producing
the State of the Software Supply Chain Report, this shows
the potential for exponential growth.

In the next simulation, we’ve normalized based on the
average vulnerability counts we identified for a compo-
nent in a specific usage or specialized group.

Corrosiveness impacts long-term security and stability in
low-usage component groups. This underscores the impor-
tance of choosing and maintaining components wisely to
mitigate the corrosive impact on the software supply chain.

Though we’ve demonstrated the impact of unfixed
vulnerabilities and the time it takes to fix them, seeing
the benefit of open source projects’ hard work requires
proper dependency management. In other words, a fixed
vulnerability is technically unfixed until an upgrade.

I N C E N T I V E S   PAY  O F F
Paid maintainers show a clear lead in security practices. Projects with paid support are nearly three times more likely to
have a comprehensive security policy formed through best practices like those verified through the OpenSSF Scorecard
project, suggesting better vulnerability identification processes. At the same time, non-paid packages tend to accumulate
more vulnerabilities, with paid packages having only a third of the unfixed vulnerabilities seen in non-paid ones. Addition-
ally, components with paid support resolve outstanding vulnerabilities up to 45% faster and have half the vulnerabilities
overall. This data highlights that incentivized maintainers produce more secure and efficient outcomes. This is consistent
with the 2024 Tidelift State of the Open Source Maintainer Report that paid maintainers implement 55% more critical
security and maintenance practices than unpaid maintainers.

4343

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEVOLUTION OF OPEN SOURCE RISKdependencies or fail to upgrade them appropriately, the
corrosive nature of Persistent Risk takes hold, leading to
gradual and eventual decay.

Complacency is hard to spot, and dependency manage-
ment isn’t only about failing to upgrade. Upgrading to a
still-vulnerable dependency can be just as damaging. It’s
like replacing rusty steel with equally corroded material.
Once corrosion sets in, fixing it becomes costly. Fortu-
nately, our findings show this decay is entirely avoidable.

In our analysis, we first assessed how many enterprise
application dependencies had yet to be upgraded within
a year. The findings were sobering: 80% were unman-
aged and remained outdated. Delving deeper, we found
that managed and updated dependencies still used 3.4%
of components with a vulnerability. Only 0.5% of compo-
nents were without a better choice because they had no
fixed version available (no path forward or NPF).

Ultimately, the highest-quality components will reduce
risk and fix most of their vulnerabilities, and they do so
quickly. However, making the right choice is just one
aspect of mitigating Persistent Risk. Proactive depen-
dency management is essential to avoid or significantly
reduce this risk effectively. Unfortunately, our data pres-
ents a sobering reality, indicating software manufacturers
are plagued by complacency.

Complacency

Complacency is generally defined as a false sense of
security or neglect, where one is unaware or unconcerned
about potential dangers. In open source software, com-
placency manifests as the failure to update and maintain
dependencies properly, akin to neglecting rusting steel.

Open source components, like steel, rust over time. Thus,
maintenance is critical to ensure durability and structural
integrity. When software manufacturers neglect their

FIGURE 3.10
Risk of Complacent Behavior

The graphic above simulates the impact of poor dependency management practices.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN

44
4444

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEVOLUTION OF OPEN SOURCE RISK80%

of enterprise application dependencies
were unmanaged and remained outdated
within a year.

Excluding complacent behavior, the risk rate could be
lowered to 0.5% associated with NPF. However, for
complacent dependency management, the risk rate is
seven times higher at a staggering 3.6% of components
that became vulnerable but were not updated or were
updated to another vulnerable version, highlighting the
critical difference between active and passive depen-
dency management. The following diagram exemplifies
how complacent behavior results in 4 vulnerabilities that
could have been avoided.

These findings highlight how quickly risks can accumu-
late without proactive management. All open source
or commercial software will eventually have bugs that

FIGURE 3.11
Libyears

evolve into vulnerabilities; hence, the metaphor: compo-
nents age like steel, not aluminum. There is a silver lining,
though, albeit short-lived.

For the components described above, those that exhib-
ited complacent risk, 95% were avoidable by the end of
the period. In other words, for almost 95% of components
that had a vulnerability, within a year, there was at least
one newer, non-vulnerable version available. We also
know that many open source projects address vulnerabil-
ities much faster.

To better understand a project’s susceptibility to cor-
rosion, we analyzed “libyears,” a metric that captures
the cumulative age of a component’s dependencies.
The risk intensifies with End-of-Life (EOL) components,
which no longer receive updates, leading to the gradual
breakdown of software integrity. Our findings indicate
that complacent dependency management, especially
involving EOL components, results in significantly more
vulnerabilities, steadily eroding security posture and
underscoring the need for proactive management.

While libyears increase with dependency count, there is significant variation in how outdated dependencies are, even for similar-sized applications.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN

45
4545

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEVOLUTION OF OPEN SOURCE RISKLibyears reveal how outdated dependencies can harbor
significant risks. Even when choosing the latest com-
ponent version, it’s critical to assess the freshness of
its dependencies. Higher libyears correlate with more

vulnerabilities, particularly in larger applications.
This reinforces the importance of vigilance, especially as
EOL components present severe risks by leaving vulnera-
bilities unaddressed, further weakening software security.

FIGURE 3.12
More EOL Components per Application
Lead to More Security Vulnerabilities

More EOL components per application correlate with a higher number of
security vulnerabilities.

FIGURE 3.13
EOL Components Signal Broader
Vulnerabilities in Non-EOL Packages

Applications with more EOL components still show higher vulnerabilities
in non-EOL packages, suggesting EOL presence reflects broader mainte-
nance issues.

Our analysis of over 20,000 enterprise applications
shows that reliance on EOL components strongly indi-
cates increased security vulnerabilities. Simply removing
these components often offers minimal improvement,
revealing that the corrosion of complacent behavior runs
deeper, affecting the entire software framework. Vulner-
abilities aren’t limited to EOL components, and managing
only EOL components is insufficient. Still, the presence of
EOL components indicates the lack of dependency man-
agement, and like EOL components are allowed to exist,
so are vulnerable versions of other components. Routine
upgrades alone aren’t enough; without a strategic, proac-
tive approach to dependency management, corrosion will
continue to undermine software integrity.

Our analysis of over 20,000 enterprise
applications shows that reliance on EOL
components strongly indicates increased
security vulnerabilities

When considering Persistent Risk, complacent depen-
dency management compounds the corrosive aspects
of Persistent Risk. When not addressed, corrosion can
erode even the most robust systems if not actively man-
aged. And, as corrosion silently compromises software
integrity, the risks escalate, paving the way for contamina-
tion. For software manufacturers that fail to minimize Per-
sistent Risk through informed choices, contamination risk
— the new frontier of attacks — moves beyond Persistent
Risk, posing a critical, new threat many software manufac-
turers have yet to realize.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN

46
4646

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEVOLUTION OF OPEN SOURCE RISKContamination

Open source malware acts as a contaminant in the digital
supply chain, undermining the security and stability of
systems and exposing them to significant risks.

To better understand contamination, consider head-
line-grabbing attacks like NotPetya, Octopus Scanner
(NetBeans), and SunBurst (SolarWinds). These incidents
occurred despite the proliferation of malware scanning
tools, highlighting a critical gap in modern information
security practices.

The XZ Utils incident exposed the dangers of neglected
open source projects, which become easy targets with-
out proper care. While a vigilant developer averted disas-
ter, the core issue remains unresolved. It’s only a matter
of time before another neglected project faces attack.
This risk is not theoretical — it’s an urgent threat with
potentially far-reaching consequences.

Open source malware targets anyone using open
source software, but teams making poor choices and
neglecting proper dependency management practices
are at even greater risk. Once again, complacency plays
a significant role here, as many security teams need a
deeper understanding of the unique challenges posed
by open source malware.

Traditional scanning tools effectively identify and prevent
known malware but struggle with novel attacks, especially
those embedded in malicious open source packages. While
these tools can catch established threats, they often miss
the hidden dangers within open source components, par-
ticularly when the malicious code is deliberately designed
to evade detection. This limitation underscores the need
for more advanced security measures that can address the
unique challenges posed by sophisticated, elusive attacks.

FIGURE 3.14
Malware Introduced to Public Binary
Repositories Over Time

Open source malware has spiked over the past 3 months.

As part of our analysis, we examined 512,000 pieces of
open source malware that had been introduced into pub-
lic binary repositories since November of 2023. While the
majority of malware is of medium risk, a substantial por-
tion (almost 17%) poses critical security risks.

When comparing a sample of 84k components, 42k
of which are core and 42k peripheral, we found that periph-
eral components were 25x more likely to contain mal-
ware. The peripheral packages are less commonly used in
enterprise applications but target automated builds or sce-
narios where a component is set to pull the latest version.

Open source malware targets innovators, exploiting soft-
ware manufacturers with poor consumption practices.
This year’s analysis shows many are vulnerable, whether
by failing to equip developers with the right tools or rely-
ing on complacent approaches like automatic upgrades.
Malware doesn’t discriminate, and current scanning
methods don’t guarantee risk reduction. The conse-
quences of persistent contamination remain severe.

4747

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEVOLUTION OF OPEN SOURCE RISKOPTIMIZING

Efficiency & Reducing Waste

This year we estimate open source downloads to be over 6.6 trillion — the scale of open source is
unfathomable. We also know that commercial state-of-the-art software is built from as much as 90% open source code,
including hundreds of discrete libraries in a single application. While use of OSS accelerates application development
cycles and reduces expenses, it also introduces threat vectors in the form of vulnerabilities and intellectual property (IP)
risk from restrictive and reciprocal licenses.

Managing these OSS risks in DevOps organizations, with any type of success, must involve efficient security policies and
practices that are capable of keeping pace with the evolution and addition of new OSS libraries in the accelerated devel-
opment environment leading to rapidly changing risk profile.

Previously we talked about the Persistent Risk and how open source con-
sumption factors into creating that risk. We also talked about complacency
within dependency management — and found that 80% of enterprise applica-
tion dependencies were not upgraded within a year. We also know from past
analysis that of those versions that do get upgraded, 69% had a better choice.
And, that 95% of all vulnerable versions used to begin with had a non-vulnera-
ble fix available and 62% of consumers used an avoidable vulnerable version.

These sobering statistics led us to where we are now  — diving deep into how
organizations can change their consumption behaviors to optimize risk miti-
gation efforts and reduce waste, especially waste that might occur in targeting
lower priority risks.

62%

of open source
consumers used an
avoidable vulnerable
component version

4848

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINOPTIMIZING EFFICIENCY & REDUCING WASTESize Doesn’t Matter: All
Applications Have Sizable Risk

As a result, organizations need more time to remediate the
vulnerabilities. The more time you take, the higher the risk.

The average application has around 180 open source
components — that’s an increase from around 150 from
which we found last year. All of these packages, when left
unmanaged can be a source of risk and as we saw in pre-
vious chapters of this report — that risk is only growing. It
won’t be if you get breached, but when.

There is no denying the data shows the larger the appli-
cation, the larger the risk. It should come as no surprise
that as application size grows, so does the number of
dependencies. The sheer size of the code base and com-
plexity of large applications makes it harder to manage.

FIGURE 4.1
Average Number of Packages per Application

This chart shows the distribution of application dependency size.
Small: up to 25 dependencies; Medium: 26 to 150 dependencies;
Large: 151 to 400 dependencies; X-Large: 401 or more dependencies.

However, it became abundantly clear that there is no
‘small’ application that is trivial to manage. Further, our
data shows that most applications are in fact large appli-
cations — around 40%. So, there is no organization that
doesn’t have to contend with this problem. No matter
the size of an application — whether you only have 25
dependencies or you have 400 or 800 dependencies
(which is not abnormal) — it is an unmanageable manual
workload. You can and must gain efficiency across all
applications regardless of their size, especially as the
industry moves more towards microservices and mod-
ularizing applications, which will mean smaller applica-
tions. Optimizing management of 1,000 small applications
is just as beneficial as optimizing 1 large application.

So, how do enterprises get a handle on this massive issue
that is not only causing increasing risk to them and their cus-
tomers, but is also wasting an incredible amount of time? We
must first understand two interrelated key concepts:

•  Efficiency Hurdle: Development time is limited with

little or no allocation in schedules for remediation tasks
or dependency upgrade research. Stopping builds and
slowing down pipelines to review risks due to vulner-
abilities manually is impractical and goes against the
flow of DevOps, frustrating teams as a result. It also
frustrates developers, causing intense friction, which is
why organizations must prioritize reducing waste.

•  Reduce Waste: The efficiency hurdle is a solvable

problem. Enterprises can create efficiency and thus
reduce waste, by optimizing remediation via a com-
bined approach of an enterprise-scale SCA tool, highly
accurate component intelligence, and effective depen-
dency management practices.

4949

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINOPTIMIZING EFFICIENCY & REDUCING WASTEStop Wasting Developer Time —
What to Look for in an SCA Tool

FIGURE 4.2
Corrected Version Information

Integrate for effective but non intrusive
software composition analysis
Fixing vulnerabilities is a huge time drain on development
cycles. It will be faster if vulnerability detection is integrated
in development environments or CI/CD pipelines. The right
tool will provide context for the expected functionality of
the component, so developers can make informed deci-
sions on deciding the best version to use in real-time.

We’ve all now heard the concept of Shifting Left or mov-
ing the remediation as close to the beginning of the
development cycle. While we still agree with this, we’ve
found you must go even further — you must review
dependences on a continuous basis, there is no begin-
ning or end. Reviewing dependencies and remediation
needs to be incorporated into the regular flow of devel-
opment, shifting it into development rather than at ‘test’
or ‘release’ time. But, to be successful it needs to be
much more efficient than it is now, since it’s now being
done more frequently and can disrupt the development
pace. This is the only way to reduce downstream and
upstream effects, rework and wasting developer time.

For an SCA tool to be successful, it must be integrated
within the CI/CD pipelines and provide context for the
expected functionality of the component, so developers
can make informed decisions on deciding the best ver-
sion to use. If your tool does this, you’re one step closer
to reducing waste.

Demand High-Quality Open Source
Component Intelligence
Reliable component intelligence is the foundation of
efficient risk remediation and dependency management.
Component intelligence depends upon the quality of the
underlying vulnerability data.

This pie chart shows that 92% of public vulnerability information had a version
correction after deeper review.

There are two main contributing factors of high quality
vulnerability data to look for:

1.  Scoring the vulnerabilities in a consistent and repeat-

able manner, in line with industry standards

2. Comprehensive coverage of the correlation to libraries

and versions affected by the vulnerability

We’ve found that 92% of crowdsourced or publicly
available vulnerability data needed a correction once
detailed security research took place that more accu-
rately correlated the source of the vulnerability to
affected versions of the libraries.

5050

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINOPTIMIZING EFFICIENCY & REDUCING WASTEFIGURE 4.3
Score Corrected Aggregations

This bar chart depicts public vulnerability score corrections by score severity, 10 through 1.

While public data is often accurate for a single version, it
tends to be wrong when it comes to multiple versions —
usually because the version range is incorrect. This creates
a false sense of security, as you might assume, “the version
I’m using isn’t affected.” But that’s often not true; the security
researcher simply didn’t review all versions thoroughly. It’s
important to understand that while the version mentioned
in a public advisory is typically correct, many other versions
haven’t been reviewed or validated at all.

We dug deeper on accuracy of scoring and found that
69% of vulnerabilities that were initially scored below 7
were corrected to 7 or higher, and 16.5% were corrected
to 9 and higher. This creates what we’re calling surprise
risk and a false sense of comfort that you’re not at risk.

To reiterate, incorrectly scored low vulnerabilities lead to
emergency reactive work when the true threat is realized.

The surprise reactive work and surprise risk negatively
impacts the flow of development, leading to inefficiency,
in addition to a false sense of security that could result
in a breach or service interruption. Vulnerabilities
detected after a serious breach or incident demand a
higher resolution time, in addition to the lack of trust and
endangering lives, in extreme cases.

The converse is incorrectly scored high vulnerabilities
which diverts development capacity to remediate, taking
away precious time that could be spent on true high prior-
ity vulnerabilities that could lead to serious impacts.

It must be emphasized that the component intelligence
built into your SCA tool must give accurate vulnerability
data and avoid wasting development capacity, by target-
ing remediation efforts on high priority vulnerabilities.

5151

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINOPTIMIZING EFFICIENCY & REDUCING WASTEComprehensive Ecosystem Support
Different ecosystems have a different number of depen-
dencies and could directly affect the size of your appli-
cation. A general perception is that Java and JavaScript
have a lot of dependencies, while other ecosystems
are more manageable. This could cause complacency
among the developers using non-Java ecosystems,
based on the false understanding that fewer dependen-
cies mean fewer vulnerabilities or easier to manage.

Our data actually shows that the PyPI ecosystem (the
Python ecosystem which tends to have low dependen-
cies) has more vulnerabilities per package as compared

to other ecosystems. Enterprises cannot rest on using
“low-dependency” languages because even when you
think you’re using a low dependency — or lower average
number of components — you’re still very much at risk
and need to practice efficient dependency manage-
ment, thus you need a good SCA tool that covers a wide
breadth of ecosystems.

Further, most enterprises are using more than one eco-
system within their application portfolio, underscoring
the importance of having an SCA tool that supports
comprehensive ecosystems.

FIGURE 4.4
Average Number of Components (Packages)
per Application, by Ecosystem

FIGURE 4.5
Average Number of Vulnerabilities in Top 10
Most Popular Packages, by Ecosystem

This bar chart shows the average number of ecosystem packages used by
an application, covering Maven, npm, NuGet, PyPI, and Go.

This bar chart shows the average vulnerability counts for the top 10 most
popular packages by ecosystem (Maven, npm, NuGet, PyPI, and Go), along
with the number of severe vulnerabilities.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN

52
5252

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINOPTIMIZING EFFICIENCY & REDUCING WASTEMature Dependency Management Workflows
Risk based prioritization is essential to minimize the time
spent on remediating vulnerabilities. There are several
approaches to how an organization can assess and prior-
itize risks to optimize the remediation process. Some of
them include:

•  Performing Reachability Analysis to determine what

actual components in the dependency chain are being
called by the applications and are vulnerable.

•  Assessing risks due to vulnerabilities that are exploit-
able in the runtime environment of the application.

Reachability Analysis is an optimization approach to achiev-
ing a near-zero risk scenario in a limited amount of time.
Reachability involves detecting vulnerable method signa-
tures in the execution paths of an application (call graph),
regardless of whether it is directly called from the applica-
tion or through other OSS libraries. Teams can target their
remediation efforts towards these reached vulnerabilities.

However, the effectiveness of this kind of prioritization
greatly depends on a combination of the following factors:

•  The accuracy of the call graph generated

•  The accuracy of the CVE scores being targeted for

remediation (see the importance quality data)

•  CWE (determination of the impact if the vulnerability

manifests itself in an exploitable manner)

Targeting remediation of only vulnerabilities detected
after Reachability Analysis, having high CVE scores only
(9 or 10) without considering the CWEs could create a
false sense of security.

All declared vulnerabilities may not manifest themselves
as exploitable in a given runtime environment. An appli-
cation’s runtime environment (public SaaS, distributed for
customers to run and operate, having access to sensitive
information etc.) could be determinant in the priority of its
remediation. Knowledge of declared CWE and its accu-
racy, including a thorough analysis of base level weak-
nesses, variant weaknesses and composite weaknesses
(a set of weaknesses that are reachable consecutively
in order to produce an exploitable vulnerability), is a key
factor to avoiding such risks.

Aligned with Cybersecurity
Compliance Requirements
For organizations serving the federal sector, or serving
other organizations that support the federal sector, main-
taining an optimal security posture is a hard requirement
to stay in compliance with FISMA policies. This is achieved
by remediating all “high” and “critical” vulnerabilities in the
production environment.

Features like continuous monitoring and reporting
offered by SCA tools provide real-time insights into the
severity of vulnerabilities, as they are discovered at
various stages of the development cycle. Developers
can target “high” and “critical” vulnerabilities and avoid
spending time remediating others to stay in compliance.

E X A M P L E S   O F  V U L N E R A B I L I T I E S  T H AT   M AY  B E   E X P LO I TA B L E :

Network exploits could occur only if the application is
meant to run on public WAN/LAN or Internet.

Applications processing sensitive data such as PII,
classified information, and healthcare data are at risk of
accidental exposure due compromised network security
or malicious attempts to gain access.

5353

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINOPTIMIZING EFFICIENCY & REDUCING WASTEOpen Source License Risk Profile

Generally, licensing tends to lie outside of developer or
security teams interest. Swept away by the creative and
innovation waves, developers use the latest and most
popular components available to stay ahead of the curve.
Neglecting open source licenses (based on assumptions
that it is open source and free to use) is a huge business
risk. With laws and litigations coming in later, organiza-
tions could get into years of dispute and suffer financial
setbacks involving fines and loss of revenue.

Open source licensing issues, if investigated at all, will
generally not show up before release cycles due to the
effort involved. In the absence of an SCA tool, the pro-
cess to review OSS licenses is manual and time consum-
ing. It could involve reviews done by legal teams, which

FIGURE 4.6
Projects  with One or More License Changes

This pie chart shows the percentage of projects that had 1 or more license
changes through the version history.

95.56M

Total releases with a license

puts drag on external teams and resources. As a common
practice, most organizations conduct OSS license com-
pliance reviews once, just before a production release
to save resources, which is very late in the development
cycle and can ultimately create more waste.

Licenses can change from version to version
A typical open source project has an overarching license,
which might not apply to all individual files under the proj-
ect. As contributions to an open source project increase,
individual pieces of code can have different licenses,
which could impact the project downstream.

Some vendor-owned open source projects can also be
relicensed to restrict usage or better control, for exam-
ple, Terraform, previously Mozilla Public License v2.0,
changed to Business Source License (BSL) v1.1; Elas-
ticSearch, previously Apache2.0 License, changed to
non-open source dual license based on SSPL; and Redis,
previously Berkeley Software Distribution (BSD) License,
changed to Redis Source Available License.

The BSL license also gives the vendor the right to change
license further down the road with short or no notice.

Data at left depicts the magnitude of license changes
tracked for multiple projects.

Although the overall license changes appear to be 6% of all
release versions, the remediation tasks being more man-
ual in nature could set release dates back unexpectedly.
Reviewing candidate upgrade versions requires manual
checks, causing delays and sometimes no upgrades at all.

5454

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINOPTIMIZING EFFICIENCY & REDUCING WASTEFIGURE 4.7
Unique License Sets per Project

FIGURE 4.8
Open Source Compliance Legal Review Time

This bar chart shows the sum of the unique licenses sets per project (not
including the first license set) by ecosystem: Maven, npm, NuGet, PyPI, Go).

This bar chart illustrates efficiency gains in legal review time by comparing
duration without and with accurate and comprehensive legal data.

An SCA tool with a built-in license feature and accurate
OSS legal compliance database can identify potential
compliance and legal issues immediately — decreasing
review time by 2,470%.

Teams can detect license changes which can occur from
version to version for a component by reviewing the
SCA reports. If configured correctly, it can detect license
changes early in the development cycle, allowing suffi-
cient time for linked manual remediation processes (esca-
late, find forked projects with non-restrictive licenses or
adapt usage of commercially available licenses.)

Why Dependency Management Needs to be Much
More than “Just Update to the Latest Version”
Simply put, the latest version of a component may not be
the best version to use. A common practice for avoiding
known security issues is to upgrade to the latest version
of a component, to the point where this upgrade step is

often automated. There is the possibility of the license
being more restrictive than the currently used versions
license, introducing new business risks.

It can allow setting context-sensitive license policies that
are in compliance with the application context, and flag
violations within the development cycle.

Since many OSS licenses come into effect based on
the application’s production environment (distributed,
hosted, or internal), compliance issues may not arise until
a release. An SCA tool can allow setting license policies
to flag non-compliance at various stages in the SDLC
(pre-release or release.)

Backed by accurate and trusted OSS license data,
organizations can review attribution reports, and review
license obligations to stay compliant.

5555

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINOPTIMIZING EFFICIENCY & REDUCING WASTEBEST PRACTICES
EXECUTIVE SUMMARY

Best Practices

in Software Supply Chain Management

Every dollar spent on software development demands budget justification. This complicates risk
management. The open source world is always changing, with new risks appearing daily through rapid innovation. Tradi-
tional scanning tools are unable to accurately and promptly detect new potential malware. Most organizations struggle
with timely risk management due to a lack of adequate security controls and discipline to enforce better open source
component choices along with the pace of necessary security updates. This results in considerable difficulty in achieving
and maintaining an optimal Mean Time To Remediate.

Developers feel less encouraged or incentivized to adapt to
a security-savvy mindset while developing software using
open source packages due to a lack of proactive guid-
ance from tools, available security data insights, or implied
security processes. Further, the alarming increase in open
source malware and the use of open source downloads as
a vehicle for malware distribution is also highly concerning.
Amid constant backdoors, ransomware, and emerging
threats, security struggled with manual oversight of engi-
neering, whose development teams, despite being the pri-
mary risk source, often ignored security concerns.

However, the expanding risk spectrum and surge in
open source components don’t fully excuse the failure to
choose high-quality components, update them promptly,
or proactively defend against malware attacks.

Most organizations struggle with
timely risk management due to a
lack of adequate security controls
and discipline to enforce better
open source component choices
along with the pace of necessary
security updates.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN
10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN

56
56

Best Practices

Our findings reinforce the need for software manufactur-
ers to approach open source consumption with diligence.
With the right tools, processes, and best practices, man-
aging these risks and ensuring the security and reliability
of software supply chains becomes possible and efficient.

Informed Selection of Open Source
Components:

•  Prioritize components that demonstrate active and

responsive communities. These components are more
likely to address vulnerabilities quickly and maintain a
higher standard of code quality.

•  Integrate metrics like latency (the average time to vul-
nerability discovery) into your risk assessment frame-
works to better understand and mitigate the long-term
impact of complacency.

Address the Human Factor in Risk
Assessment:

•  Educate your development teams on the cognitive

biases that can lead to poor risk assessment, such as
overestimating the benefits of maintaining the status
quo. Encourage a mindset that values proactive risk
management over short-term gains.

Proactive Dependency
Management:

•  High fix rates and low time to remediate metrics are key
indicators of a component’s reliability. Also, components
with transparent supply chain practices, like publishing
an SBOM, typically exhibit lower Persistent Risk.

•  Regularly audit your open source dependencies to iden-
tify vulnerabilities, particularly those that span multiple
versions. Implement automated tools to track and reme-
diate these issues before they impact your software.

Adopt a Comprehensive Quality
Assessment Framework:

•  When selecting open source projects, go beyond

surface-level metrics like the number of stars or forks.
While popular projects often fix vulnerabilities more
quickly, they are not inherently risk-free. Ensure your
selection process incorporates more risk-related indi-
cators, such as Persistent Risk across versions.

With the right tools, processes, and
best practices, managing these
risks and ensuring the security and
reliability of software supply chains
becomes possible and efficient.

•  Develop a systematic approach for updating depen-
dencies as soon as fixes become available. This will
minimize Persistent Risk and prevent software from
“aging like steel.”

Mitigate Complacency
in Maintenance:

•  Implement policies that enforce regular reviews and

updates of all open source dependencies, particularly
those neglected for over a year. This approach will com-
bat latent risks and reduce the chances of introducing
vulnerabilities into your software.

•  Utilize tooling that provides real-time alerts for out-

dated or vulnerable dependencies, akin to a smoke
detector for your software supply chain. However, it
must only alert when action is truly required. These
tools should prompt timely updates and prevent
complacency.

5757

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINBEST PRACTICESStay Vigilant Against Malicious
Open Source Software:

•  Be particularly cautious when integrating new or

lesser-known components into your software. The
rise of malicious packages targeting innovative or less
frequently used projects necessitates heightened
awareness and rigorous validation.

•  Avoid dependency management approaches that
always update components to the latest version.
Instead, upgrades should be considered based on an
optimal version and the optimal version zone, both
strategies we addressed in last year’s report.

Collaboration and
Continuous Improvement:

•  Participate in or align with initiatives like the Open

Source Consumption Manifesto and collaborate with
industry groups to stay informed about emerging risks
and best practices.

•  Review and refine your open source consumption

policies regularly based on the latest industry research
and metrics, ensuring your organization stays ahead of
new threats and challenges.

Work in the
Upstream:

•  Participating in open source projects helps you stay
informed about bugs and vulnerabilities, align your
roadmaps with open source projects, and ensure
your interests are represented. Projects often appre-
ciate the extra set of hands as it helps with their
sustainability.

•  Active software supply chain management involves

helping maintain the open source projects you depend
on. Don’t leave it to others, and avoid making yourself
dependent on often unknown entities.

Cybersecurity is a Universal Issue

In 2024, the policies shaping this movement have
come into sharper focus and, in some cases, are
already being implemented and enforced. While each
country is dealing with its own set of regulations,
cybersecurity is a unifying issue. As such, regulations
are integral to improving the cybersecurity posture of
organizations across the globe. As a global leader in
protecting the software supply chain, we feel that regu-
lations will be foundational to how the industry mounts
effective countermeasures against the always-evolving
cybersecurity threat landscape. Liability has shifted
from just the developers to the consumers of tech-
nology, with potentially harsh financial penalties for
noncompliance.

SECURITY ISN’T JUST A DEVELOPMENT ISSUE;

IT’S A BOARDROOM ISSUE.

Securing the software supply chain has become
one of the guiding principles for this raft of legisla-
tion. As we’ve covered in this report, modern soft-
ware development relies heavily on open source
components, and protecting components is critical
to compliance with these new standards.

Before the industry can apply rules, regulations,
and best practices effectively, organizations
need to be able to understand what is being
demanded:
☑ Understanding how new policies
       interact with existing measures
☑ Knowing what organizations
      are impacted
☑ Who’s responsible for what

5858

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINBEST PRACTICESPreparing for Governance and
Regulations Around the World

United States

N I ST   S P  8 0 0 -2 1 8  A N D   S EC U R E   S O F T WA R E

D E V E LO P M E N T AT T E STAT I O N
When the White House issued Executive Order 14028
on Improving the Nation’s Cybersecurity, it was the first
federal regulation targeting the security of software
components. It was also the impetus for a wave of activ-
ity - both legislatively and industry-driven - designed to
drive immediate improvements in the nation’s IT security
posture. The order included a directive for the National
Institute for Standards and Technology (NIST) to issue
guidance on enhancing the security of the software
supply chain, which it did with an update to The Secure
Software Development Framework (SSDF) Version 1.1, or
NIST SP 800-218.

EO 14028 also requires that system integrators and soft-
ware vendors comply with the Secure Software Devel-
opment Attestation Form provided by the Cybersecurity
and Infrastructure Agency (CISA), which requires vendors
supplying software to federal entities to certify through a
CEO or an authorized designee’s signature that their soft-
ware is developed securely and adheres to the Secure
Software Development Framework (SSDF) guidelines
established by NIST.

T H E   S EC U R E   S O F T WA R E   D E V E LO P M E N T

AT T E STAT I O N   F O R M  A D D R E S S E S

F O U R   H I G H - L E V E L  P R ACT I C E  A R E A S :

☑ Prepare the Organization
Ensure that the organization’s people, processes,
and technology are prepared to perform secure
software development at the organization level
and, in some cases, for individual development
groups or projects.

☑ Protect the Software
Protect all components of the software from tam-
pering and unauthorized access.

☑ Produce Well-Secured Software
Produce well-secured software with minimal secu-
rity vulnerabilities in its releases.

☑ Respond to Vulnerabilities
Identify residual vulnerabilities in software releases
and respond appropriately to address those vul-
nerabilities and prevent similar vulnerabilities from
occurring in the future.

STAY COMPLIANT WITH NIST SP 800-218
AND CISA ATTESTATION REQUIREMENTS

5959

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINBEST PRACTICESEuropean Union

g. basic cyber hygiene practices and cybersecurity

N E T WO R K  A N D   I N F O R M AT I O N

S E C U R I T Y  D I R ECT I V E   2   ( N I S 2)
NIS2 is the European Union’s most comprehensive
cybersecurity legislation and focuses on critical infra-
structure and essential services. Taking effect on October
17th, 2024, NIS2 replaces the NIS Directive from 2016
and modernizes the legal framework to keep pace with
increased digitization and evolving cybersecurity threats.

Bolstering security for software supply chains is central
to NIS2, and like most EU-wide legislation, NIS2 provides
a minimum framework that member states must adhere
to but allows for flexibility in how it’s implemented at the
national level. In particular, it sets for minimum cybersecu-
rity risk management measures and reporting obligations
in Article 21, Section 2 of NIS2. These include:

a. policies on risk analysis and information system

security;

b. incident handling;
c. business continuity, such as backup management
and disaster recovery, and crisis management;
d. supply chain security, including security-related

aspects concerning the relationships between each
entity and its direct suppliers or service providers;
e. security in network and information systems acqui-
sition, development and maintenance, including
vulnerability handling and disclosure;

f.  policies and procedures to assess the effectiveness

of cybersecurity risk-management measures;

training;

h. policies and procedures regarding the use of cryp-

tography and, where appropriate, encryption;
i.  human resources security, access control policies

and asset management;

j.  the use of multi-factor authentication or continu-

ous authentication solutions, secured voice, video
and text communications and secured emergency
communication systems within the entity, where
appropriate

NIS2 also places an emphasis on reporting and requires
organizations to submit an early warning of significant
cybersecurity incidents within 24 hours. These need
to be submitted to the relevant CSIRT and indicate if
the significant incident is suspected of being caused
by unlawful or malicious acts. Within 72 hours, the first
report must be updated to include an initial assessment
of the incident, including severity and impact. Within a
month, a final report is required that includes a detailed
description of the incident, including its severity and
impact, the type of threat or root cause that is likely to
have triggered the incident, and ongoing mitigation
measures being taken.

DOWNLOAD THE NIS2
COMPLIANCE CHECKLIST

6060

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINBEST PRACTICES
              European Union

T H E   D I G I TA L  O P E R AT I O N A L

R E S I L I E N C E   ACT  ( D O R A)
DORA is expected to go into effect in January 2025 and
applies to every bank, investment service, and insurance
company doing business within the European Union –
more than 20,000 companies and third-party service
providers. Like other regulations, it’s also chiefly con-
cerned with the integrity of open source components and
considers software composition analysis (SCA) as a basic
security requirement that all institutions under its guid-
ance must apply. To this end, DORA includes language
outlining how to achieve a high level of digital opera-
tional resilience and emphasizes open source analysis
as a fundamental security requirement:

To reflect differences that exist across, and within,
the various financial subsectors as regards financial
entities’ level of cybersecurity preparedness, testing
should include a wide variety of tools and actions,
ranging from the assessment of basic requirements
(e.g. vulnerability assessments and scans, open
source analyses, network security assessments, gap
analyses, physical security reviews, questionnaires
and scanning software solutions, source code reviews
where feasible, scenario-based tests, compatibility
testing, performance testing or end-to-end testing) to
more advanced testing by means of TLPT.

DOWNLOAD THE DORA
COMPLIANCE CHECKLIST

T H E   CY B E R   R E S I L I E N C E  ACT  (C R A )
The European Parliament approved the CRA in March
of 2024 and most of its provisions become enforceable
starting in 2027. This sweeping legislation, which estab-
lishes essential requirements for manufacturers to ensure
their products reach the market with fewer vulnerabili-
ties, applies to any software or hardware product and its
remote data processing solutions, as well as products with
digital elements whose intended use includes a logical or
physical data connection to a device or network.

Specifically, the CRA sets a standard for digital resiliency
in the EU through a focus on the security of the software
supply chain by placing key requirements for the secu-
rity of software components, vulnerability handling, and
reporting requirements on suppliers.

Again, the CRA has been developed with an eye toward
protecting open source software. Incorporating robust
security measures into the development process is nec-
essary to strengthen your approach to OSS components
and SDLC processes that take into account established
best practices that will minimize risks. As a result of the
CRA, all software components will be required to obtain
the CE certification mark.

Organizations will be held accountable if any software or
hardware product that contains digital elements is found
to be non-compliant. If products are discovered to be
non-compliant, sanctions will apply, including fines of up to
€15 million or 2.5% of a company’s global annual turnover,
whichever is higher.

DOWNLOAD THE CRA
COMPLIANCE CHECKLIST

6161

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINBEST PRACTICESIndia

Key SBOM mandates of the CSCRF include:

This summer, the Securities and Exchange Board of India
(SEBI) introduced the Cybersecurity and Cyber Resilience
Framework (CSCRF) to help enhance cybersecurity for
regulated entities (REs). Critical to the CSCRF is mandat-
ing strict guidelines for software bill of materials (SBOMs)
in order to improve transparency, track vulnerabilities,
and mitigate supply chain risks.

•  New software: REs must obtain SBOMs for any new
software products or Software-as-a-Service (SaaS)
applications related to core and critical activities during
procurement.

•  Existing software: SBOMs must be obtained for existing
critical systems within six months of CSCRF issuance.

SEBI characterizes the importance of SBOM
management and its benefits in the CSCRF with
the following:

Recent security breaches at third-party vendors like
Apache (Log4j), SolarWinds, etc. have led to the
introduction of Software Bill of Materials (SBOM)
that enables an organization to identify possible vul-
nerabilities in the applications/ software solutions.

•  Ongoing updates: SBOMs must be updated with each

software upgrade or modification.

•  Legacy systems: Where SBOMs are unavailable for

proprietary or legacy systems, RE boards must provide
approval, detailing the rationale and risk management
approach.

FIND OUT MORE ABOUT
INDIA’S CSCRE

BENEFITS FOR REGUL ATED ENTITIES IN INDIA WITH THE INTRODUCTION OF SBOMS:

☑ Transparency
REs will become more aware of components,
versions, licenses, cryptographic hashes, etc., that they
are using in their software applications.
☑ Tracking vulnerabilities
REs will be able to track the vulnerability status for each
of the components as and when an update is made or a
component is added/ deleted.

☑ Mitigate risks
REs will be able to prevent and mitigate supply chain
risks arising due to open-source or third-party depen-
dencies in software components.
☑ Audit
REs will have the confidence that only authorized third-
party dependencies have been used in their software
applications and that they can be audited as and when
required.

6262

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINBEST PRACTICES
Australia

The Essential Eight strategies are guidelines intro-
duced by the Australian Signals Directorate’s Strategies
to Mitigate Cyber Security Incidents. The Essential Eight
mitigation strategies include:

T H E  AU ST R A L I A  E S S E N T I A L  E I G H T

M I T I GAT I O N   ST R AT EG I E S   I N C LU D E :

☑ Application Control
☑ Patch Applications
☑ Configure Microsoft Office Macro Settings
☑ User Application Hardening
☑ Restrict Administrative Privileges
☑ Patch Operating Systems
☑ Multi-factor Authentication
☑ Regular Backups

These strategies provide a framework for organizations
to evaluate current practices and increase their resiliency
against cyber threats. The Essential Eight is organized
around four maturity levels by which organizations can
evaluate and boost their cybersecurity measures.

M AT U R I T Y  L E V E L   Z E R O
This maturity level signifies that there are weaknesses
in an organization’s overall cybersecurity posture. When
exploited, these weaknesses could facilitate the compro-
mise of the confidentiality of their data or the integrity or
availability of their systems and data, as described by the
tradecraft and targeting in Maturity Level One below.

M AT U R I T Y  L E V E L   O N E
The focus of this maturity level is malicious actors who
are content to simply leverage commodity tradecraft that
is widely available in order to gain access to, and likely
control of, a system.

M AT U R I T Y  L E V E L  T W O
This maturity level focuses on malicious actors operating
with a modest step-up in capability from the previous
maturity level. These malicious actors are willing to invest
more time in a target and, perhaps more importantly, in
the effectiveness of their tools.

M AT U R I T Y  L E V E L  T H R E E
The focus of this maturity level is malicious actors who
are more adaptive and much less reliant on public tools
and techniques. These malicious actors are able to
exploit the opportunities provided by weaknesses in their
target’s cybersecurity posture, such as the existence of
older software or inadequate logging and monitoring.
Malicious actors do this not only to extend their access
once initial access has been gained to a target but also
to evade detection and solidify their presence. Malicious
actors make swift use of exploits when they become pub-
licly available, as well as other tradecraft that can improve
their chance of success.

6363

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINBEST PRACTICESAU ST R A L I A N   I S M   S O F T WA R E

D E V E LO P M E N T  G U I D E L I N E S
Another Australian measure to boost cybersecurity is the
March 2024 update to the Australian Signals Director-
ate’s Information Security Manual (ISM). The ISM provides
a framework based on risk management principles and
best practices to help CISOs, CIOs, cybersecurity profes-
sionals, and IT managers protect their systems and data
from malicious actors.

The ISM includes cybersecurity guidelines designed
to ‘provide practical guidance on how an organization
can protect its systems and data from cyber threats.’

These include Guidelines for Software Development,
which provide a useful set of guidelines for creating tra-
ditional and mobile applications to increase security. The
ISM is a framework, so organizations are not yet required
by law to comply. However, it’s a useful tool for compa-
nies to ensure they do not violate existing legislation,
and under its guidance, organizations can put up a pretty
effective defense against data breaches.

MEET AUSTRALIAN ISM SOFTWARE
DEVELOPMENT GUIDELINES

K E E P  U P  W I T H  T H E

L AT E ST  R EG U L AT I O N S

A R O U N D  T H E   WO R L D

Navigating new regulations with
key resources and guidance for
staying informed and compliant.

CHECK OUT THE RESOURCE HUB

6464

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINBEST PRACTICESReliable Dependency Management

Since our inception, Sonatype has led with the precision
and accuracy of our open source intelligence. From the
start, our core principle has been to avoid wasting engi-
neers’ time with false positives and negatives. As open
source usage and security research exploded, the num-
ber of true risk findings has increased dramatically. This
has created a significant burden on development produc-
tivity, forcing organizations to choose between ignoring
material risks and impairing productivity.

The only possible path forward as we see it is to use a reli-
able dependency management automation platform that
scales as needed and only updates component versions
when necessary. This automation cuts down the noise,
reduces Persistent Risks, improves open source compo-
nent quality and creates a better malware defense while
saving valuable engineering time with full transparency.

Implementing reliable automation for open source
dependency management can have a
transformative shift in your organization:

•  Reduced conflict and seamless collaboration between

security and engineering teams

•  Improved productivity by freeing up 5% of engineering

capacity

•  Enhanced security due to a significant drop in open

source risk levels

•  Quality and reliability improvements by integrating

high-quality open source components

•  Better competitive advantage through improved

security and increased productivity

S O N AT Y P E   L E V E R AG E S  T H R E E

U N I Q U E   DATA   S O U R C E S  TO

U N D E R STA N D   G LO BA L   O P E N

S O U R C E   S O F T WA R E   U SAG E :

1. Millions of Enterprise Applications:
Regularly analyzed to track trends and behaviors

2. Sonatype’s Nexus Repositories:
Insight into hundreds of thousands of usage patterns

3. Maven Central:
Observing Java open source consumption patterns

As many organizations continue to make suboptimal
open source version choices, Sonatype’s intelligent soft-
ware composition analysis (SCA) enhances developer
efficiency and risk management without altering work-
flows. By prioritizing risks and automating dependency
management throughout the software development life
cycle (SDLC), we achieve significant improvements. This
win-win scenario boosts competitiveness and innovation
across the board.

Intelligent dependency management automation is set
to revolutionize software supply chain optimization,
making secure and efficient development as the industry
standard. By combining dependable automation with pri-
oritizations like advanced reachability analysis, devel-
opers are empowered to produce high-quality software
more quickly within their existing workflows. Security
teams gain from enhanced risk prioritization, focusing on
actionable vulnerabilities. Our tools integrate seamlessly
with collaboration platforms, enhancing the governance
of the dependencies.

6565

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINEXECUTIVE SUMMARY10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAINBEST PRACTICESAcknowledgments

Each year, the State of the Software Supply Chain report is a labor of love. It is produced to shed light on the patterns and
practices associated with open source, development and the evolution of software supply chain management practices.
The report is made possible thanks to a tremendous effort put forth by many team members at Sonatype, including:
Bruce Mayhew, Jamie Whitehouse, Vlad Drobinin, Anna Hubbard, Juan Felipe Morales, Mike Hansen, Shweta Katre,
Jeff Wayman, Brian Fox, Kishlay Nikesh, Tim Vrablik, Ilkka Turunen, Alli VanKanegan, Elissa Walters, Megan Schmidt and
Jenna Jameson. We would also like to thank our contributors from across the DevOps and open source development
community including Georg Link (CHAOSS Community), Dawn Foster (CHAOSS Community), and Jeremy Katz (Tidelift).

About the Analysis

Sonatype’s 10th Annual State of the Software Supply Chain report blends a broad set of public and proprietary data and
analysis, including dependency update patterns for more than 1.5 trillion requests from Maven Central and thousands of
open source projects, and the assessment of hundreds of thousands of key enterprise applications. This year’s report
also analyzed operational supply, demand and security trends associated with the Java (Maven Central), JavaScript
(npm), Python (PyPI), and .NET (NuGet) ecosystems. Special analysis was included thanks to the CHAOSS Community
and their CHAOSS Community Report, as well as Tidelift and their survey of more than 400 open source maintainers as
source for The 2024 Tidelift State of the Open Source Maintainer Report. The authors have taken great care to present
statistically significant sample sizes with regard to component versions, downloads, vulnerability counts, and other data
surfaced in this year’s report.

10TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN

66

Sonatype is the software supply chain security company. We provide the world’s best end-to-end software
supply  chain  security  solution,  by  combining  the  only  proactive  malicious  protection  against  malicious
open source, the only enterprise grade SBOM management and the leading open source dependency
management platform. This empowers enterprises to create and maintain secure, quality, and innovative
software at scale. As founders of Nexus Repository and stewards of Maven Central, the world’s largest
repository  of  Java  open-source  software,  we  are  software  pioneers  and  our  open  source  expertise  is
unmatched. We empower innovation with an unparalleled commitment to build faster, safer software and
harness AI and data intelligence to mitigate risk, maximize efficiencies, and drive powerful software devel-
opment. More than 2,000 organizations, including 70% of the Fortune 100 and 15 million software devel-
opers, rely on Sonatype to optimize their software supply chains. To learn more about Sonatype, please
visit www.sonatype.com.