# 9th Annual State of the Software Supply Chain

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

Sonatype’s industry-defining research on the rapidly changing landscape of open source, software development, and software supply chain security.

**PRESENTED BY**

## Contents
Introduction.....................................................................................3 CHAPTER 3 Global partnerships....................................................47
Modernizing Open Source Are software supply chain
State of the Software Dependency Management.....................................23 regulations working? .................................................48
Supply Chain by the numbers...................................4 Open source consumers Navigating the policy frontier:
are not paying attention ...........................................24 Global cybersecurity regulations...........................49
CHAPTER 1 What makes an optimal
Open Source Supply, open source component? ......................................26 CHAPTER 6
Demand, and Security.......................................................5 Understanding component AI in Software Development.....................................51
Open source supply sees a resurgence ..............7 upgrade urgency.........................................................27 Sonatype’s risks &
Open source consumption is decelerating.........8 Downloads by upgrade urgency..........................29 rewards of AI survey .................................................52
Individual ecosystem analysis.................................10 Global patterns of open The intersection of AI
Open source software security source consumption behavior ...............................31 and software development....................................52
concerns see no sign of slowing ...........................10 Navigating concern ...................................................53
Notable malicious packages CHAPTER 4 AI’s open source toolkit:
and vulnerabilities.........................................................11 Software Supply Chain Maturity......................34 Components and models in focus.......................55
Differentiating software Software Supply Chain Conclusion: A collaborative future.......................59
vulnerabilities and malware......................................12 Maturity — Peer Insights...........................................35
Consumption behavior How mature are today’s About the Analysis..............................................................60
contributing to security concerns...........................12 software supply chains?............................................36
A global view of vulnerable How have software supply Acknowledgements...........................................................61
open source downloads ...........................................16 chain management trends changed?..................37
CHAPTER 2 CHAPTER 5
Open Source Security Practices.......................17 Establishment and Expansion
The state of scorecard check scores....................18 of Software Supply Chain
The Importance of Maintenance............................21 Regulations and Standards....................................42
Year-Over-Year Differences......................................21 United States................................................................43
Conclusion....................................................................22 European Union...........................................................46
Canada ...........................................................................47
2
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

## Introduction
In today’s fast-paced world, the pursuit of excellence is a relentless journey. We all understand the significance of innovation, efficiency, and the individuals at the core of it all: developers. From our past eight State of the Software Supply Chain reports, we know that developer productivity soars when they have access to superior tools and better open source components, making them the driving force behind better security and better products.

But what exactly does “better” mean in the ever-expanding landscape of technology choices? This question, in part, is the reason we’ve been studying the software supply chain for the last nine years. As we deliver the 9th version of this State of the Software Supply Chain report, that question is more paramount than ever. As we explore how to make “better” software, it’s not just about the introduction of AI or cutting-edge technologies; it’s about addressing fundamental issues that, in many ways, have not changed in nine years. It’s about the often-overlooked, yet vital, element that lies within our software supply chain: open source consumption behavior.

We aim to sift through the labyrinthine market of software components, not to add to the cacophony of choices but to streamline it. Why? Because choice is a double-edged sword. The consequences of choosing poorly are far-reaching.

Consider this — last year, we revealed that a staggering 85% of projects in Maven Central — the largest public repository for Java open source components — are inactive. In other words, developers are faced with a perplexing array of choices, with only a fraction of them leading to active, well-maintained projects. Yet, we also found, and re-affirmed this year, that 96% of all vulnerable downloads from Maven Central, had known fixes available. There are so many choices to make, and only with the right tools, the right automation, can developers truly be set up for success.

As we dissect the intricacies of open source adoption and consumption, we validate a frustrating truth — development practices remain rife with inconsistency. When choices are made poorly, this inconsistency translates into increased risks, discontent among developers, and, perhaps most significantly, a loss of both time and money.

The State of the Software Supply Chain report each year isn’t just a cautionary tale, but a call to action. It is a response to the pressing need to redefine our priorities and a testament to our willingness to evolve. We find ourselves in a period of revolution. Modernization is our ally. With regulations a focus in nearly every region, an uncertain economic climate demanding cost savings and efficiencies, and malicious activity more prominent than ever, it’s time for change.

In the following pages, we provide you with an in-depth update on open source usage trends and security practices. We continue to draw from public and proprietary data sources to illustrate a host of issues with effective supply chain management. We’ll look at:

- Ongoing growth of the software supply chain, as well as persistent security concerns
- The advantages of using well-maintained open source packages
- Open source consumption and trends in upgrade urgency of components
- Peer insights into the use of SBOMs and mature software supply chain management
- The rise of open source and software supply chain regulations
- What role AI and ML play in assisting developers, and the challenges that AI practitioners face in developing AI products

We also look at what it really means to have a Software Bill of Materials (SBOM) and a Software Composition Analysis (SCA) program, and ultimately shed light on the path to a more efficient, cost-effective, and secure development.
3
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

## State of the Software Supply Chain by the numbers
- **1 in 8** open source downloads have known risk
- **245,000** malicious packages discovered — 2X all previous years combined
- **18.6%** of open source projects across Java and JavaScript that were maintained in 2022, are no longer maintained today
- **96%** of vulnerable releases had a fixed version available
- **10** superior versions of components are typically available, for every nonoptimal component upgrade made
- **2x** When paired with optimal upgrades, good data saves you twice as much time or nearly 1.5 months of time per application, per year when upgrading components.
- **135%** increase in the adoption of AI and ML components within corporate environments, over the last year
- **67%** of survey respondents feel confident that their applications do not rely on known vulnerable libraries, despite 10% of respondents reporting their organizations had security breaches due to open source vulnerabilities in the last 12 months
4
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

---

## CHAPTER 1
# Open Source Supply, Demand, and Security

A monk by the name of John of Salisbury wrote a famous phrase in a 12th century manuscript, borrowed by Sir Isaac Newton and hundreds of others since:

> “We are like dwarfs sitting on the shoulders of giants. We see more, and things that are more distant, than they did, not because our sight is superior or because we are taller than they, but because they raise us up, and by their great stature add to ours.”

The meaning of the passage is simple: The progress we make only happens because of the progress in learning and understanding others have made before us.

Nowhere else is this seen more than in the adoption of open source. Nearly all of the software shipped today relies on previous innovation that is distributed freely on scaffolding built by the utmost experts in the world, available to all developers free of charge.

In past State of the Software Supply Chain reports, we’ve estimated that up to 90% of the code we run in production is of open source origin. Therefore, the economics of open source are good indicators of trends and challenges in the wider software market.

For the 9th consecutive year, we continue to track the growth of open source adoption across the top four major open source ecosystems. These collectively account for four of the top five languages in GitHub, and a 60% share of the most popular programming languages according to PYPL Language popularity index[^1].

Leveraging our continued monitoring, we present the combined statistics of each ecosystem in the table below.

FIGURE 1.1
**OPEN SOURCE ADOPTION AS PROJECTED FOR 2023**

| Ecosystem | Total Projects | Total Project Versions | 2023 Annual Request Volume Estimate | YoY Download Growth Estimate | YoY Project Growth Estimate | Average Versions Released per Project |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Java (Maven) | 557k | 12.2M | 1.0T | 28% | 25% | 22 |
| JavaScript (npm) | 2.5M | 37M | 2.6T[^2] | 27% | 18% | 15 |
| Python (PyPI) | 475k | 4.8M | 261B[^3] | 28% | 31% | 10 |
| .NET (NuGet Gallery) | 367k | 6M | 162B[^4] | 28% | 43% | 17 |
| Totals / Avgs | 3.9M | 60M | 4T | 29% | 33% | 15 |

[^1] https://pypl.github.io/PYPL.html Accessed August 2023
[^2] Figure estimated using npm download counts from January to August 2023 as queried from https://github.com/npm/registry/blob/master/docs/download-counts.md
[^3] YoY growth estimated based on known PyPI downloads from January to August 2023 as queried from https://console.cloud.google.com/marketplace/product/gcp-public-data-pypi/
[^4] YoY growth estimated based on known NuGet Gallery downloads from January to August 2023 as queried from https://www.nuget.org/stats

6
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

7
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

### Open source supply sees a resurgence
The supply side of open source is an interesting metric to gauge the pace and scale of innovation that occurs in a given ecosystem. The more open source projects are published every year, the more innovation occurs in a given ecosystem. New open source projects across the monitored ecosystems have been published at a relatively steady 15% average rate[^5] in recent years, which was a significant reduction in pace from highs seen in 2019 and before.

FIGURE 1.2
**OPEN SOURCE NEW PROJECT GROWTH RATE OVER THE PAST 4 YEARS**
![Open source new project growth rate over the past 4 years chart]

FIGURE 1.3
**OPEN SOURCE PROJECTS AND VERSIONS GROWTH**
![Open source projects and versions growth chart]

[^5] In the 2021 report, we used a different method of estimating project counts for NuGet which resulted in a reduced number of projects being reported in 2022. We have corrected the NuGet historic numbers based on statistics published by the NuGet Gallery.

8
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

This two-year slump is most likely related to the COVID-19 pandemic period and associated slowdown. While some studies suggest productivity did increase during the 2020-2023 period in the U.S., a negative correlation emerges in open source production trends. This is further supported by another study that found productivity rates in information and communication technology did decline towards 2022. One other explanation could be that a lot of these projects are in fact coming from commercial activity and not people with spare time, which was in abundance during the pandemic.

To date, the data in 2023 shows the innovation slowdown is now over. Each monitored ecosystem showed a remarkably consistent project growth rate, varying just 2% across all four of monitored ecosystems to a total average growth rate of 29% year-over-year.

The rate of production growth is recovering across the board, and both Maven Central and NuGet are on track to exceed the rate of growth seen in 2020.

PyPi and npm, although growing, have not yet caught up to their original rate of growth but are on an upward trend. In a later section, we will see how breakthroughs and interest in AI and its related tooling are fueling the rate of growth in these ecosystems.

Between 2022 and 2023, the number of available open source projects grew an average of 29%. The average open source project in 2023 has released 15 versions available for consumption, with specific ecosystem averages ranging from 10 to 22 across the different open source registries. That means 1-2 new versions every month and adds up to 60 million combined releases made available in the observed ecosystems.

### Open source consumption is decelerating
While we’re seeing supply increase, consumption isn’t keeping pace. The rate of download growth in open source consumption has slowed the past two years. In 2023, this trend continued with the average download growth rate sitting at 33%, which is exactly what it was last year. This is a stark comparison to the all-time high of 2021, which saw 73% year-over-year growth. There is a sign of slowdown in growth in the largest ecosystems, which is not surprising given the market saturation they already have.

Despite this, both of the largest ecosystems, Maven and npm, are each estimated to reach over a trillion requests in 2023, with npm reaching a staggering 2.6 trillion requests in total, continuing a modest growth that surpasses the total request rate of PyPI in 2022.

These two ecosystems account for 90% of the requests served with the remaining two growing at above average pace.

FIGURE 1.4
**CUMULATIVE ESTIMATED REQUESTS PER ECOSYSTEM OVER 6 YEARS**
![Cumulative estimated requests per ecosystem over 6 years chart]

9
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

FIGURE 1.5
**GROWTH RATE OF THE MONITORED OPEN SOURCE ECOSYSTEMS OVER 5 YEARS**
![Growth rate of the monitored open source ecosystems over 5 years chart]

Requests are the fundamental measure of how popular an open source ecosystem is and how lively its usage is. Other factors within an ecosystem may vary, such as the larger size and complexity of Java packages compared to JavaScript packages.

Investigating the rate of growth for requests can reveal information about the state of open source adoption, as well as the growth of the software industry at large.

Figure 1.5 charts these individual growth rates over time and displays an average across all 4 ecosystems.

Download requests for all open source ecosystems are still growing, but for a third year in a row there are signs that the pace of growth is slowing down.

FIGURE 1.6
**TOTAL OPEN SOURCE REQUESTS OVER 6 YEARS**
![Total open source requests over 6 years chart]

We can see a clear delineation between the stabilization of large ecosystems like Maven and npm, and continued accelerated growth in PyPI and NuGet.

Figure 1.6 charts the overall aggregate request growth across all ecosystems. It illustrates that although the pace of growth is slowing down, the absolute scale of growth continues to compound on previous years’ rates. To put it simply, the pace of open source adoption still shows no signs of stopping.

**2023 BY THE NUMBERS**

- **JavaScript (npm)**: 2.1 trillion projected request volume | 32% YOY growth estimated
- **Python (PyPI)**: 261 billion projected request volume | 31% YOY growth estimated
- **.NET (NuGet)**: 162 billion projected request volume | 43% YOY growth estimated
- **Java (Maven)**: 1 trillion projected request volume | 25% YOY growth estimated

10
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

### Individual ecosystem analysis

#### Java (Maven)
Through the first 7 months of 2023, 512 billion Java components were requested from the Maven Central Repository. This is a significant jump compared to the 821 billion requests in 2022.

Java continues to grow at a healthy pace, hitting an estimated 25% YoY request growth rate. If previous years are any indication, we may well see a spike towards the end of the year.

#### JavaScript (npm)
npm is the juggernaut of open source registries, with an estimated download request count of over 2.6 trillion components (or to display it in full numbers: 2,579,310,885,518).

The growth of npm is the slowest of all the monitored ecosystems — estimated to be at 18% YoY. Nevertheless, owing to npm’s substantial footprint, this translates to a staggering 400 billion requests, surpassing the combined total of requests served by PyPI and NuGet.

#### Python (PyPI)
Python continues to expand at a high pace, fueled by the language’s popularity and innovative uses, including AI. In 2023, PyPI served over 178 billion requests. This year, we estimate PyPI request volume will hit 261 billion packages. This represents 31% YoY growth.

#### .NET (NuGet)
NuGet is the chosen ecosystem of the .NET family of languages and continues to serve engineers working with the growing set of Microsoft technologies. The rate of growth in NuGet is estimated to be the fastest amongst the cohort. Developers downloaded 113 billion NuGet packages in 2022, which was well above our estimate last year. In 2023, NuGet is estimated to serve 162 billion requests, representing 43% YoY growth.

### Open source software security concerns see no sign of slowing
In 2022, we reported a massive increase in the growth of malicious attacks on the software supply chain. Since our last report, this method of propagating security threats using trusted developer utilities and ecosystems has continued to evolve and flourish.

A troubling trend has emerged in the software supply chain over the past few years of tailor-made packages designed to run a malicious payload on download — without any developer interaction. This form of intrusion relies on developers not recognizing that the build breakage resulting from the fake package might be an indication that something nefarious has already happened on their system. We did a deep dive into types of malicious attacks in last year’s report.

11
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

### Notable malicious packages and vulnerabilities
In our YoY monitoring, at the time of writing in September 2023, we have logged 245,032 malicious packages — meaning in the last year, we’ve seen the number of malicious packages tripled. Looking at it a different way, it also indicates that in one year alone, we’ve seen twice as many supply chain attacks as the cumulative numbers in previous years.

This pace of growth is astonishing. It signals the role of the supply chain as one of the fastest growing vectors for adversaries to execute malicious code. Furthermore, we have seen an increase in nation-state actors leveraging these vectors (see our deep dive section below).

FIGURE 1.7
**NEXT GENERATION SOFTWARE SUPPLY CHAIN ATTACKS (2019-2023)**
![Next generation software supply chain attacks chart]

This is alarming news. Even though many open source ecosystems have implemented new security policies, such as mandatory MFA, they usually only address the issue of protecting existing open source publishers from attack. Often, packages containing malicious code are treated very similarly to packages with new security vulnerabilities — and they are taken down entirely based on a volunteer effort following a vulnerability removal process, which is not appropriate when the code is designed to be malicious from the start. This approach can lead to the malicious packages being up longer than necessary, leaving developers at risk.

As we continue to document an overall rise in new malicious attacks on open source ecosystems, the monitored 2022-2023 period has also seen more professional criminal campaigns emerge. The software supply chain lends itself well to the cybercriminal ecosystem — either as an initial access vector to Initial Access brokers or even as a means of distributing initial access malware for Advanced Persistent Threat groups. Here are several examples we’ve seen this year:

#### Lazarus created PyPI package ‘VMConnect’ imitates VMware vSphere connector
In August 2023, Sonatype discovered a malicious Python package, ‘VMConnect,’ on PyPI, which mimics a legitimate VMware module. This is part of a wider cyber campaign called “PaperPin,” and is widely thought to originate from the Lazarus Group, a North Korean state-affiliated organization. The packages aim to download further malicious payloads from attacker-controlled URLs. The focus on VMware, a widely-used virtualization platform, is particularly concerning, as a successful compromise could have far-reaching implications for enterprise networks and is widely attractive to state affiliated actors. [Read our full deep dive](#)

12
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

#### ChatGPT histories were uncovered due to a vulnerability in Redis component used by OpenAI
In March of 2023, ChatGPT users experienced a data leak where chat histories displayed people’s queries. OpenAI identified the issue as a race condition vulnerability in an open source component called Redis, which they use for caching user data. This flaw made sensitive data of about 1.2% of ChatGPT Plus subscribers accessible to others. The vulnerability was exacerbated by a recent server change that increased the probability of the race condition occurring. The issue underscores the importance of even rarely occurring vulnerabilities, especially in widely-used components like Redis, given their potential to cause widespread disruption and data exposure. [Read our full analysis](#)

#### PyTorch namespace confusion attack targets utilities aimed at AI developers
In the past couple of holiday seasons, we’ve seen some big supply chain attacks, including one on PyTorch, a popular machine learning framework. The attackers used a tactic known as namespace confusion to specifically go after the experimental “nightly” build of PyTorch. They managed to steal sensitive data, signaling that hackers are increasingly setting their sights on AI and machine learning tools. These tools are becoming more critical in various sectors, making them attractive targets. While only the experimental build was hit, the incident serves as a wake-up call for better security in the booming AI field. [Read our full analysis](#)

#### A timeline of attacks
We have continued to curate a timeline of known malicious packages and malware campaigns. This interactive timeline summarizes other notable supply chain incidents, next-gen attacks and other incidents propagated using the software supply chain.

### Differentiating software vulnerabilities and malware
Up until now, we’ve been talking about malware and malicious attacks on the software supply chain - or maybe better stated as malware propagated using the open source supply chain. In this next section, we’re going to discuss software vulnerabilities. While the two concepts are related, they are very distinct, so we’d like to quickly define the difference between a vulnerability and a malware.

#### Software vulnerability: A flaw in the code
A software vulnerability is akin to a flaw in code, much like a faulty lock on a door. However, unlike malware, vulnerabilities are not intentional. Instead, they represent weaknesses in software components or projects.

Similar to how a faulty lock compromises the security of a building by allowing unauthorized access, a software vulnerability creates a gap in the software’s security perimeter. This gap becomes an entry point for intruders to exploit, gaining unapproved access to the system, application, or component.

#### Malware: Malicious intent in open source
Malware, short for “malicious software,” poses a significant threat to open source software ecosystems. It encompasses a wide range of malicious programs, such as viruses, worms, trojans, ransomware, spyware, and adware, all designed to gain unauthorized access to information or systems.

With its various forms, malware’s primary purpose is to steal data, install harmful software, gain control of a network, or compromise software or hardware. Threat actors employ diverse distribution methods, such as infected email attachments, malicious websites, or compromised software downloads.

### Consumption behavior contributing to security concerns
Our report last year revealed a startling statistic — nearly 96% of component downloads with known vulnerabilities could be avoided as a better, fixed version is already available. This illustrates a clear need for organizations to pay closer attention to what versions they are adopting.

13
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

FIGURE 1.8
**SOFTWARE SUPPLY CHAIN ATTACKS, DEC 2021–AUGUST 2023**
![Software supply chain attacks chart]

- **249,556,989** total Log4j downloads since Dec 15, 2021 | **29%** vulnerable
- **3,490,799** total downloads (Aug 20–27, 2023) | **23%** vulnerable

There is widening evidence that whatever the standard practice for avoiding vulnerable components today, the controls are not having the effect needed to reduce the attack surface. For example, as of September 2023, downloads vulnerable to the infamous Log4Shell vulnerability still account for nearly a quarter of all net new downloads of Log4j. It should be highlighted, that almost two years after the initial finding of this vulnerability, we’re seeing this pace continue every week — that a quarter of all downloads are of the vulnerable version of Log4j.

This is only part of the story. The reality is, nearly 1/3 of all Log4j downloads, ever, are of the vulnerable version.

As we discussed last year, the numbers for other critical vulnerabilities that have not received as much widespread media attention are even more depressing.

This warrants concern and calls for behavioral adaptation at organizations because critical vulnerabilities are widely exploited by bad actors, even at the state level. For example, Log4Shell has topped CISA/NSA charts for active state-sponsored exploitation for well over a year now. This is also echoed in the OpenSSF’s recently released Consumption Manifesto, which calls for organizations to take responsibility for the open source they use, how it is consumed, and how they manage the risk associated with that consumption.

According to a joint consortium of national operators including CISA, NSA, NCSC-UK and others, attackers are exploiting older well-known vulnerabilities much more frequently than new zero-day vulnerabilities. This is extremely important to understand. While we should of course worry about zero-days, we also know that 96% of vulnerable open source downloads have a non-vulnerable fix available. Those 96% need to be addressed.

For this year’s report, we’ve taken a closer look at how vulnerabilities are consumed from Maven Central, with a special focus on what sort of geographic variance might exist.

#### Vulnerable components consumed
Let’s start off by looking at the top level. In 2022 we saw 12% of downloads served by Maven Central[^6], contained at least one known security vulnerability.

This number is important when considering that the easiest way to reduce risk of a supply chain incident caused by a vulnerability is to simply choose a better, non-vulnerable version of a component[^7]. There is some improvement in these however, the number of vulnerable downloads in 2021 was 14% — and the number to date in 2023 sits at around 10%.

[^6] Countries and regions with over 100,000 annual requests
[^7] A limitation in this report is that the numbers reported are of security vulnerabilities known as of August 2023, even when inspecting retrospectively. The amount of vulnerabilities known at the time of download might have been lower, which might partially explain the improvement over time.

14
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

15
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

However, when investigating the downloads that contained a vulnerability in 2022, it emerges well over a third of the components consumed that had known vulnerabilities were Critical[^8] in severity — and a further 30.5% had a High Severity rating.

This trend holds true nearly universally across all regions — suggesting that component consumption is largely an unmanaged decision today. This is in contrast to the number of known critical vulnerabilities in the National Vulnerability Database — with over double the amount criticals consumed over the spread of known vulnerabilities.

FIGURE 1.9
**PERCENTAGE OF COMPONENTS WITH KNOWN VULNERABILITIES SERVED FROM MAVEN CENTRAL**
![Percentage of components with known vulnerabilities served from Maven Central chart]

FIGURE 1.10
**2022 VULNERABLE DOWNLOADS BY SEVERITY**
![2022 vulnerable downloads by severity chart]

FIGURE 1.11
**NVD — KNOWN VULNERABILITY SEVERITY**
![NVD known vulnerability severity chart]

[^8] As defined in CVSS 3.1 https://www.first.org/cvss/specification-document

16
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

FIGURE 1.12
**AVERAGE VULNERABILITIES BY COUNTRY WITH OVER 1 BILLION DOWNLOAD VOLUME**
![Average vulnerabilities by country with over 1 billion download volume chart]

### A global view of vulnerable open source downloads
Software development has evolved into one of the most globally influential industries, shaping various sectors and regions in unique ways. However, not all regions share the same level of emphasis on software development. To gain insight into how the trends we’ve explored thus far manifest on a global scale, we conducted an analysis that looks at open source vulnerability consumption, by country.

Our study focused on countries that collectively downloaded over 100 million open source components from Maven Central in the past year. By scrutinizing the percentage of vulnerabilities associated with the software downloaded in each region, we start to gain insights into how different parts of the world manage their software supply chains.

In Figure 1.12, we delineate those that have stronger management programs, from those who don’t, by plotting the percentage of vulnerabilities, against the average number of vulnerable downloads (approximately 12%) — and apply a ranking based on how countries compare to that average. But it’s important to consider the context and one of the most important figures to come out of Sonatype’s research: 96% of known vulnerabilities downloaded from Maven Central have a non-vulnerable version available.

The countries isolated above are 25 of the largest consumers of open source software in the world. Even at the low end of our criteria, around 100 million downloads, 9.5% of those downloads are vulnerable components. When you consider juggernauts of open source consumption like the United States, the EU (collectively), and China, tens of billions of vulnerabilities have entered into the supply chains that produce the software we all use and our governments run on.

While we’re only scratching the surface with this regional view of vulnerable downloads, you can see a deeper dive into open source consumption patterns within specific economic regions in Chapter 3 of this report where we further unravel the intricacies of dependency management on a global scale. We also summarize the role regulations are having on the industry in Chapter 5.

---

## CHAPTER 2
# Open Source Security Practices
17
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

### The state of scorecard check scores
In 2020 the OpenSSF project started collecting information on the software security practices employed by open source projects. This substantially increased transparency of open source development practices by centrally tracking the usage of commonly accepted best practices. In a previous version of this report, we analyzed the extent to which higher scores on these checks are associated with better security outcomes and found them to be highly predictive of vulnerability status. In this year’s report, we delve into the state of adoption of Scorecard best practices overall and also by ecosystem (focusing on Java and JavaScript). We look at checks today as well as over time, looking back at the prior year to see both how community practices have evolved and how the checks themselves have evolved over time.

#### THE CHECKS
Our dataset consists of scorecard checks from 2022-06-27 and 2023-07-03 retrieved from the Scorecard BigQuery database. Each check is scored from 0 to 10. If the check fails or there is lack of evidence for a check, the Scorecard project assigns it a score of -1. We mapped these -1 values to 0 for our analysis.

- **BINARY ARTIFACTS**: Checks whether binary artifacts are checked into the repository, reducing the score if binary artifacts are found.
- **BRANCH PROTECTION**: Checks whether the project uses branch protection on its default and release branches to prevent maintainers from circumventing workflows like CI tests or code review when pushing changes.
- **CII-BEST PRACTICES**: Checks whether a project has obtained an OpenSSF (formerly CII) Best Practices Badge.
- **CODE REVIEW**: Checks whether recent code changes have been peer reviewed before being merged.
- **DANGEROUS WORKFLOW**: Checks whether the project avoids dangerous coding patterns in GitHub Action workflows.
- **DEPENDENCY UPDATE TOOL**: Checks whether the project is using tools to help update its dependencies.
- **FUZZING**: Checks whether the project is using fuzzing tools.
- **LICENSE**: Checks that the project includes a license file.
- **MAINTAINED**: Scores the project based on the amount of commit and issue tracking activity it has had over the last 90 days.
- **PACKAGING**: Checks whether the project builds and publishes official packages from the CI/CD pipeline.
- **PINNED DEPENDENCIES**: Checks whether project dependencies (including dependencies for GitHub Actions and Docker files) are pinned to specific versions.
- **SECURITY POLICY**: Checks that the project includes a security policy.
- **SIGNED RELEASES**: Checks that the project cryptographically signs releases.
- **TOKEN PERMISSION**: Checks whether the project’s automated workflow tokens follow the principle of least privilege.
- **VULNERABILITIES**: Checks that the project and its dependencies have no open, unfixed vulnerabilities. Projects score 10 for no vulnerabilities and 1 point is deducted for each open vulnerability, down to a minimum score of 0.
- **VULNERABLE**: A binary version of Vulnerabilities that we added to the dataset. A project is vulnerable if its Vulnerabilities score is less than 10.

18
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

19
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

Code Review (e.g. requiring review of pull requests before merging) was the most important practice, followed by Binaries (not checking binary data into the repository), Dependencies Pinned (pinning dependencies to specific versions), and Branch Protection (preventing direct pushes to the main branch).

The figure below shows how widely the scorecard best practices have been adopted. The chart presents the average value for each check across our 2023 dataset. Note that Code Review, which we found last year to be the practice most highly associated with good security outcomes, is not widely-practiced in general, with an average score of less than 1. Roughly 19% of projects score greater than 0 on Code Review, and only 2% receive the full score of 10 (indicating that all code changes have undergone review). Branch Protection, which supports code review by requiring changes to go through the review process, also scores low (just 0.24 on average). The Vulnerabilities check measures whether a project has open, unpatched vulnerabilities, either associated with the project itself or with its dependencies. The Vulnerabilities score starts at 10 and is decreased by 1 for each open vulnerability with a minimum score of 0 (e.g. a project with 10 open vulnerabilities and a project with 15 open vulnerabilities both score 0). This means that the average score of 8.9 indicates that projects on average have at least 1 open vulnerability. Of course not every project is vulnerable: just over 14% of projects have a Vulnerabilities score of less than 10 (indicating they have at least one open vulnerability). If we look at just vulnerable projects, we find that on the date our 2023 data was collected they had on average at least 7.7 open vulnerabilities per project.

Another important low-scoring check is Maintained, which checks whether a project is being actively maintained, either via regular code commits or timely responses to issues. Maintenance is generally a prerequisite for security patches. On average, projects score about 0.66 on the Maintained check. Out of 1,176,407 total projects, just 118,028 of them (~11%) have a Maintained score greater than 0.

Looking at the data by ecosystem (shown in the figure below), we see that Java projects score higher on average than JavaScript projects for a number of security-relevant checks. Java projects score on average:

- 67x higher on Signed Releases
- 3.2x higher on SAST
- 3.1x higher on Maintained
- 2.0x higher on Branch Protection
- 1.7x higher on Dependency Update Tool
- 1.7x higher on Code Review

Java projects also score 10x higher on Fuzzing, though very few projects in either ecosystem take advantage of fuzzing technology. Rates of

20
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

FIGURE 2.2
**SCORECARD CHECK AVERAGES, ALL PROJECTS**
![Scorecard check averages, all projects chart]

FIGURE 2.3
**SCORECARD CHECK AVERAGES, JAVA VS JAVASCRIPT**
![Scorecard check averages, Java vs JavaScript chart]

FIGURE 2.4
**SCORECARD CHECK AVERAGES, MAINTAINED**
![Scorecard check averages, maintained chart]

21
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

vulnerability are comparable, with 15% of Java projects and 16% of JavaScript projects having unpatched vulnerabilities at the time of scan. Note that this is a measure of whether there are vulnerabilities that apply to the development branch of a project. This does not indicate whether the latest release of the project has a vulnerability, nor whether the recorded vulnerabilities will persist into the next release.

### The Importance of Maintenance
The figure above shows how the average scores change when we focus on maintained projects only (projects with a Maintained score greater than zero). There are several notable differences. Maintained projects are

- 5.9x higher on SAST
- 5.4x higher on Signed Releases
- 5.1x higher on Dependency Update Tool
- 3.6x higher on Code Review
- 3.8x higher on Branch Protection

Maintained projects also score better on Vulnerabilities and have slightly lower rates of vulnerability.

### Year-Over-Year Differences
We also looked at the data from one year ago to see how Scorecard practices have changed.

Surprisingly, we find that there has not been a steady improvement in scorecard scores. Instead, we see decreases in several key metrics. In particular, the number of maintained projects has decreased overall and also within each ecosystem. Overall, there are 24,104 projects that were maintained one year ago, but no longer qualify as maintained. This represents 18.6% of the maintained projects. Put another way, if you picked a random maintained project in 2022, there would be a 18.6% chance that this project is no longer maintained one year later.

At the same time these ~24k projects slipped out of the “maintained” category, there were 12,806 newly “maintained” projects (projects that are maintained now but did not qualify as maintained in 2022). This resulted in an overall decrease of 11,298 in the number of maintained projects. Of the projects that have become unmaintained over the last year, 1,285 were in the Maven Central (Java) ecosystem and 9,626 were in NPM (JavaScript). This decrease is not necessarily a bad thing – it could simply reflect consolidation, with maintainers focusing on a smaller set of projects that have “stood the test of time”.

Overall, these changes highlight the importance of tracking the health of dependencies over time. Just as new projects are constantly being created, projects are also constantly reaching end of life status. Identifying these changes is an important part of maintaining a healthy set of application dependencies.

We have also seen an overall decrease in the amount of code review. The number of projects that had any Code Review decreased by over 15%. The decline was slightly less for Java (~11%) than for JavaScript (~17%). Even when just looking at maintained projects, there was a decrease of 8.6% in rates of code review. Comparing trends in scorecard checks over time is complicated by the fact that the OpenSSF Scorecard team does periodically change the checks in ways that can affect scoring. However, we reviewed the changes made to the code review check and, on aggregate, they appear to make the check easier to pass (e.g. by treating a PR

22
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

merged by someone other than the contributor as a review). If this data indeed reflects a decline in the amount of code review occurring in otherwise well-maintained projects then this is a worrying trend. We recommend ensuring that any open source libraries critical to business applications are practicing code review on every pull request to the main branch.

### Conclusion
Overall, these results provide guidance for open source users when choosing dependencies and important areas of focus for open source advocates and maintainers. The value of choosing well-maintained projects stands out, as these projects tend to be more diligent about a number of important software security best practices. The fact that 18.6% of projects stopped being maintained in the last year highlights the need to not only choose good dependencies, but monitor those dependencies for changes in their quality. The overall low rates of code review, even when considering just maintained projects, provide a clear area for improvement in open source development practices – especially given the importance of code review in predicting security status (established in last year’s report).

Based on our findings, enterprises looking to minimize their open source vulnerability risk should choose well-maintained projects that perform code review and monitor them to ensure they have not reached end-of-life.

---

## CHAPTER 3
# Modernizing Open Source Dependency Management
23
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

In the last three State of the Software Supply Chain reports, we’ve delved into the intricate aspects of managing open source dependencies. We firmly believe that understanding the intricacies of both macro and micro decisions when selecting open source components fosters robust, streamlined, and secure software supply chains.

Each year, our cumulative analyses bring us closer to uncovering the key to optimal dependency management and ensuring safer, more efficient software supply chains. However, the incremental improvements we’ve observed in open source dependency management over the past three years, while noteworthy, fall short of our desired progress.

### Open source consumers are not paying attention
In last year’s report, we posed this critical question: Who is primarily responsible for creating the greater share of risk in open source ecosystems, open source maintainers, or consumers? The answer was overwhelmingly open source consumers. We wanted to see if this had changed, so re-ran some of the numbers for 2023. We saw no change in the consumption of vulnerable downloads within the Maven Central ecosystem.

This means, we once again saw that 96% of all known-vulnerable downloads were avoidable.

#### The size of the “consumer” problem is concerning
This year, we again analyzed how the world consumes open source from Maven Central across 400+ billion downloads over the year. We compared consumers downloading vulnerable dependencies without a fixed version to vulnerable dependencies where a fixed version was available but not chosen.

FIGURE 3.1
**CONSUMER VS MAINTAINER OF VULNERABLE DOWNLOADS**
![Consumer vs maintainer of vulnerable downloads chart]

- **96%** of all known-vulnerable downloads were avoidable
- **3.97 billion** vulnerable components are consumed each month, from the average 37.8 billion monthly downloads from Maven Central
- **2.1 billion** vulnerable Java Components

24
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

Developers not only contend with the initial selection and management of around 150 dependencies but are also tasked with:
- tracking an average of 1,500 dependency changes per year per application,
- possessing security and legal expertise to choose the safest versions,
- maintaining ecosystem security insights about new risks affecting projects,
- sifting through thousands of projects to pick the best one.

25
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

#### How Common Are Fixed Vulnerabilities?
From there, we found that 1.8 billion or 3.8% of the vulnerable dependencies were due to a vulnerable version with no available fix – meaning 96.2% of known-vulnerable downloads had a non-vulnerable option available. That means 2.1 billion avoidable vulnerable dependencies are being consumed each month.

Consumers opted for these no-fix-available projects due to lack of alternatives. Interestingly, even though there are only a few vulnerable versions without alternative fixes, a significant portion of vulnerable versions with available solutions are still being downloaded.

This sentiment is echoed in the Consumption Manifesto recently published by the Open Source Security Foundation (OpenSSF). The manifesto emphasizes the need for organizations to shoulder the responsibility for the open-source software they employ, their methods of consumption, and their strategies for handling the associated risks.

#### Why is making good choices so hard?
Developers face a multitude of challenges and responsibilities in their work, often leading to overwhelming and inefficient experiences when dealing with dependency management. This struggle has been humorously dubbed “Dependency Hell” in the development community. This bears repeating.

Organizations expect developers to make informed choices regarding open source components for their software projects. However, a significant portion (approximately 85%) of projects hosted on Maven Central are considered inactive, with fewer than 500 monthly downloads. This proliferation of inactive projects further complicates the already challenging task of selecting the most suitable components for a given project.

Consider for a moment the average Java application now boasts a whopping 148 dependencies, with around 10 releases occurring annually. Developers not only contend with the initial selection and management of around 150 dependencies but are also tasked with tracking an average of 1,500 dependency changes per year per application, possessing security and legal expertise to choose the safest versions, understand ecosystem nuances, and sift through thousands of projects to pick the best one. Now, imagine the scale of these decisions for enterprises with tens of thousands of developers and thousands of applications.

The additional workload described above is merely a fraction of what software developers already face in their day-to-day responsibilities. The immense pressure to meet industry demands for efficiency and speed often leads to inefficiencies and risks within enterprises. When developers are inundated with an overwhelming array of choices and limited resources, it not only hampers productivity but also jeopardizes the organization’s success.

26
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

With all of this in mind, we also recognize that developers are making their best efforts given the circumstances. As we delve deeper into this issue, we encounter several key challenges:

- **Popularity** — When deciding which dependencies to use in a development project, popularity is often used as a proxy for quality (i.e., “everyone else is using it, so it must be safe, secure, and reliable”). Theoretically, this makes sense as more popular projects should be getting fixed faster. But they aren’t. As revealed in our 2019 State of the Software Supply Chain report, the popularity of a dependency does not correlate with a faster median update time. Developers may feel safe in selecting more popular projects, but just because a dependency is popular, doesn’t necessarily mean it’s “better.”
- **Clarity** — Oftentimes, developers aren’t manually selecting individual versions when building software supply chains and those dependencies are already part of a project that’s being used or built upon. As cited in the 2020 State of the Software Supply Chain report, 80-90% of modern applications consist of open source software. If an SBOM and proper DevSecOps practices are not implemented, developers and software engineering teams may have no way of knowing that those vulnerable components are being used, pulled, or built upon.
- **Automation** — Though there are plenty of open source automation tools, very few have security capabilities built in. Similar to the issue above, this automation may mask potential vulnerable dependencies, enabling developers to unknowingly build upon projects with known vulnerabilities.
- **Inactive Releases** — There are almost 500,000 projects within Maven Central, but only ~74,000 of those projects are actively used. That means 85% of projects are sitting in this repository and taking up space, potentially overwhelming developers with available options.

#### Modern Dependency Management Practices
While not surprising, the problem of dependency management didn’t magically go away in the past year. So, as we continue on the quest to understand how we could potentially fix it, we honed in on the aspects that reflect modern dependency management — or a potential answer to solving the 96% problem.

Our emphasis lies on understanding the nuances of behavior within this domain and how it impacts the way we work. This includes:

- Defining the optimal component. What actually makes a “good open source component”
- Dissecting the optimal time to upgrade an open source dependency
- Reflecting on current upgrade behavior
- Analyzing global patterns of download behavior

### What makes an optimal open source component?
In the realm of dependency management, understanding the inherent risks and benefits of individual software component versions is paramount. To address this challenge, we conducted a comprehensive assessment of software artifacts and have developed a robust scoring system that evaluates components across five key dimensions.

These dimensions are as follows:

1. **Security**: Uses a sophisticated method to gauge the “total risk” associated with a particular component version, considering all its vulnerabilities and common weaknesses. This scoring technique allows for a thorough comparison of different versions of the same component or across components by considering vulnerability counts, severities, and types.
2. **License**: Based on License Threat Groups: Categorizes licenses into severity groups, allowing for informed decisions that align with your application’s licensing requirements.

27
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

3. **Age**: Evaluates a component’s age in relation to the latest version, emphasizing the benefits of staying current within the software ecosystem.
4. **Popularity**: Analyzes download counts across repositories and other sources, enabling an understanding of component usage trends and popularity.
5. **Release Stability**: Quantifies the stability of a version by assessing its version label, factoring in development stages, such as pre-release, beta, etc, as well as double-publishing occurrences.

Our scoring system is not arbitrary. Built on years of thinking about dependency management, it seeks to create a holistic representation of a component’s risk and value, facilitating

### Understanding component upgrade urgency
In the fast-paced realm of software development, staying current with component versions is paramount to ensure security, performance, and reliability. However, **merely having access to better versions of components does not always guarantee that an upgrade is immediately necessary.** Compare this to the way we buy and “upgrade” cars. You could get the newest model and upgrade every year. You have access to the new models (versions), and each year, there are improvements made that make it better. But, would that be effective? Usually, no. It would be even more time intensive, some of those new features may have bugs that

 require fixing, and you’re spending all your time upgrading instead of driving.

Similarly, in software development, every update to a dependency introduces change, and with change comes the potential for regressions, build breaks, or compatibility issues. Even worse, if you upgrade too frequently, you might introduce a zero-day vulnerability or a malicious package that slipped into a fresh release.

Yet, staying on an outdated version poses its own set of risks, such as missing out on critical security patches, performance improvements, and bug fixes. Finding the right balance requires understanding component upgrade urgency.

When considering an upgrade, development teams must weigh several factors:
- The severity of vulnerabilities in the current version.
- The availability of a stable, non-vulnerable fix.
- The effort required to perform the upgrade versus the risk of leaving the component untouched.

By implementing smart automation and relying on comprehensive Software Composition Analysis (SCA), organizations can cut through the noise of dependency hell, prioritize the upgrades that truly matter, and build secure, resilient software supply chains.

---

need to be worked are no issues, but it has still touched multiple
data-driven decisions in software supply chain out — and you may simply not need those fea- team members such that a five-minute change is
management. By examining these dimensions, tures. However, for example, there are definitely an hour or more. For enterprises at scale, a com-
we can assess dependency management, prior- advantages to upgrading when there are new mon component with frequent updates could
itized upgrades, and optimized software devel- safety features, you know bugs have been introduce significant interaction and waste asso-
opment practices. worked out, and of course, if there is a recall. ciated with developer time.
At first, the comparison seems unwarranted. To better understand this cost, we looked into
Buying a car is considerably more time-intensive the concept of Upgrade Urgency to shed light
than upgrading a component. However, con- on the need for a data-driven solution. Our
sider everything that needs to go into updating approach is based on a component scoring
algorithm, which not only scores a component
but also categorizes its versions into distinct
zones. These zones range from the best/opti-
mal versions to reactive (worst) versions.
Proactively managing dependencies is of
utmost importance because, as the saying goes,

28
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
TNEMEGANAM
YCNEDNEPED
ECRUOS
NEPO
GNIZINREDOM
:3 RETPAHC
FIGURE 3.2
software ages like milk, not wine. Remaining in
UPGRADE URGENCY
a reactive state is not only suboptimal from a
security perspective, but it also puts develop-
ment teams at an immediate disadvantage and
penalizes them when issues arise. Analyzing the
observed patterns reveals that teams that pro-
actively make upgrade decisions are in a signifi-
cantly better position to make the most informed
choices.
The upgrade urgency algorithm assesses how
urgently a component should be upgraded by
comparing its version score to the best avail-
able. It categorizes urgency as follows:
(cid:28)0 — Optimal version(s): Component scores in
the top 10% of the best version’s score
(cid:28)1 — Proactive: Scores between the top 10%
and 1 standard deviation below the max
(cid:28)2 — Borderline proactive: Scores 1 standard
deviation below the max but less than 2 stan-
FIGURE 3.3 dard deviations
VERSION DOWNLOAD BY UPGRADE URGENCY FROM MAVEN CENTRAL
(cid:28)3 — Reactive: Scores 2 or more standard
Upgrade Urgency Downloads by Urgency Percentage Urgency deviations below the best version for that
component.
0- Optimal (best) Version 18,055,476,664 80.6%
Unlike component scoring, upgrade urgency
1- Proactive 602,398,633 2.7% considers a version’s distance from the best
available, whereas being on the best version
2- Borderline 2,604,054,004 11.6%
eliminates the need for urgent upgrading.
3- Reactive 1,128,938,205 5% We will apply these algorithms to explore
download patterns across different urgency

29
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
TNEMEGANAM
YCNEDNEPED
ECRUOS
NEPO
GNIZINREDOM
:3
RETPAHC
zones, providing valuable insights into how With 2.6 billion downloads being classified as
During the time of
software development industry professionals “borderline” and a further 1.1 billion falling into
download, each
are making their component selections and the worst, reactive category, there is some
upgrade decisions. component, on average, cause for concern. After all, we live in a world
where it only takes just one vulnerability to “set
had 10 superior versions
the internet on fire”.
Downloads by
available.
upgrade urgency Moreover, a comprehensive analysis of the
component scores for all downloaded versions
As you know, Maven Central is the de facto brakes only worked 80% of the time, that would reveals a striking pattern: during the time of
repository for Java-based open source libraries. be unacceptable. That would mean, a 1 in 5 download, each component, on average, had 10
It acts as a centralized hub, enabling developers opportunity your brakes stopped working while superior versions available. This finding empha-
to effortlessly discover, access, and integrate driving around town. To further underscore this sizes that many developers not only miss out
dependencies into their projects. Its widespread point, think about it in terms of food preparation. on the best versions but even when selecting
adoption and comprehensive collection of arti- Maintaining strict hygiene standards for 80% of versions that are considered “good enough,”
facts have made it an essential resource for Java food products in a restaurant also means the relatively speaking, there are better alternatives
developers worldwide. majority of ingredients are safe to consume, but they could have chosen. This reveals that the
the remaining 20% could lead to food poisoning selection process is likely driven by heuristics
In our analysis, we used Maven Central to or other health risks. such as just picking the latest version. However,
examine the download patterns of component we see that even that strategy has its pitfalls.
versions. We looked at a typical month of data
and determined the upgrade urgency of each
download. In a perfect world, developers would
FIGURE 3.4
only be downloading optimal versions of their TIME SAVED WITH OPTIMAL UPGRADE DECISIONS
dependencies in order to minimize risk and
future upgrade effort.
What we found is that a significant number of
downloads (80%) are of the best available ver-
sions of the components being downloaded.
At first glance this seems commendable, but
it’s worth noting that being on the best version
doesn’t necessarily mean it’s a high-quality
component; you might be on the best version
of a really poor component. However, let’s go
back to our car analogy from above. If your

30
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
TNEMEGANAM
YCNEDNEPED
ECRUOS
NEPO
GNIZINREDOM
:3
RETPAHC
In past years, we’ve looked at optimal as being However, we also noted great variability in this
A 25% reduction in
a single component or a single version. There practice. To highlight this drawback we call atten-
false positives, over
was a right and wrong version. This year, we’ve tion to anonymized data from several companies
the course of a year, established that optimal is really a range. There in two different industries. We analyzed two
is still a “right” or a “wrong”, but on a spectrum. organizations in the energy industry with a similar
would give you a total
To further this, we examined the Maven Central number of Maven Central downloads. Out of each
resolution savings of 2X. repository to quantify wasted developer time. company’s total downloads, we found there was
In this scenario, we define wasted time as the approximately 1.8 times more wasted downloads
download of an optimal version of a component from one organization compared to the other.
A ton of wasted time when another optimal version of that same com-
In prior years, we reported on how efficient timing ponent has already been downloaded by that We also examined two significant players in the
for upgrades can yield significant cost savings. user instance. To put this into perspective, let’s online information industry. One organization had
Opting for safer versions and prolonging their use again go back to our car analogy. Would you buy 5.4% wasted time, whereas the other enterprise
can significantly reduce upgrade expenses. In a a car every time a new model year comes out? had 10.2% wasted time. That’s an 89% increase in
medium-sized enterprise with 20 dev teams, the The optimal buying period might be when the unnecessary downloads! It is evident that mature
potential gain equates to two extra development model refreshes say every five years, rather than enterprises can reduce this variability and wasted
weeks per application each year. incremental changes each year. In our analysis, time. By having a centralized platform for storing,
we consistently observed this phenomenon, managing, and distributing quality software com-
This year, we’re continuing to dissect this which is all too frequent and raises concerns. ponents, this is a very solvable issue.
cost savings coefficient further. In addition to The gains of such frequent upgrades are mini-
the above, which takes into account optimal mal and from a lead/management perspective The value of an artifact
upgrade decisions, we looked at what the time prioritization can also be optimized/aligned repository manager
savings would be when you consider the quality based on things that are in the optimal range In the scenario above, we know much of this
and accuracy of your security data, in making versus just getting the new component. wasted time could be solved by simply using a
these decisions. good repository manager, like Sonatype Nexus
Repository Manager. A centralized, binary
In answering this question, we found that when
teams use better security data that reduce false
positive findings by 25%, in combination with We examined two significant players in the online
making optimal upgrade decisions, each team
information industry. One organization had 5.4% saved a total 1.5 months of time, per application,
per year. This equates to a 2X boost in time wasted time, whereas the other enterprise had 10.2%
saved over just the optimal upgrade process we
wasted time. That’s an 89% increase in unnecessary
described in our 8th annual report last year. In
other words, if you improve the security data you downloads!
use and reduce false positives, in tandem with
upgrade efficiency, you double your gain.

31
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
TNEMEGANAM
YCNEDNEPED
ECRUOS
NEPO
GNIZINREDOM
:3
RETPAHC
repository allows you to proxy, collect, and
GLOBAL PATTERNS
manage your dependencies so that you are not OPEN SOURCE CONSUMPTION RANKINGS AMONG G7 NATIONS
constantly juggling all of these various versions.
Or, in this case, wasting time — downloading
optimal versions, when another optimal version
is already in your instance. It becomes the single
source of truth for an organization’s software
components and applications.
Global patterns
of open source
consumption behavior
In today’s interconnected global landscape,
various regional groupings and trade agree-
ments play a pivotal role in shaping international
relations, trade dynamics, and economic coop-
eration. We explored whether these groupings GLOBAL PATTERNS
also inform software development in the form of OPEN SOURCE CONSUMPTION RANKINGS BY REGION
component consumption patterns.
With the component score we can consider the
quality of the component, with upgrade urgency
we can assess how good the downloaded
version is. Bringing it all together, we exam-
ined global download patterns. We gave equal
weight to component scoring and upgrade
urgency, and a little additional weight to the
sheer quantity of downloads. Because picking
the right components and staying on the best
versions is surely harder at scale. Below are
some observed global trends.

32
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
TNEMEGANAM
YCNEDNEPED
ECRUOS
NEPO
GNIZINREDOM
:3
RETPAHC
GLOBAL PATTERNS GLOBAL PATTERNS
OPEN SOURCE CONSUMPTION RANKINGS IN ASEAN NATIONS OPEN SOURCE CONSUMPTION RANKINGS IN BRICS NATIONS
GLOBAL PATTERNS
GLOBAL PATTERNS OPEN SOURCE CONSUMPTION RANKINGS IN SOUTH
OPEN SOURCE CONSUMPTION RANKINGS IN USMCA & THE EU AMERICAN & CARRIBBEAN NATIONS

33
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
TNEMEGANAM
YCNEDNEPED
ECRUOS
NEPO
GNIZINREDOM
:3
RETPAHC
Within the Group of Seven (G7) nations, many nations undergoing a digital transforma- Latin America and the Caribbean
renowned for hosting some of the globe’s tion with heavy investment into IT infrastructure Next in the rankings were the Latin America and
most advanced economies, the United States and digital innovation. the Caribbean nations. Among the countries
emerged as the frontrunner, boasting the high- with the highest scoring downloads we saw Nic-
est cumulative score. In contrast, its northern USMCA & EU aragua and Bolivia. On the other hand, Panama,
counterpart, Canada, found itself positioned at Tied for a close second were the economic pow- and Guatemala were ranked towards the end of
the bottom of the list. Germany had the highest erhouses of North America through the North the list. Despite the sweeping digitization trends
proportion of optimal versions downloaded. Italy American Free Trade Agreement (NAFTA), which happening across this economic grouping,
had the highest proportion of reactive down- has evolved into the United States-Mexico-Can- some of the analysis was nevertheless skewed
loads among the G7 countries, at over 8%, which ada Agreement (USMCA), and the European by the significantly lower download counts
also made it one of the lowest ranked countries Union (EU), the collaborative bloc of European across many of the member countries.
across the globe on that metric, only beating nations. The USMCA trio had the US rank on top,
out China, Hong Kong, Macedonia, and San followed by Mexico, and finally Canada. Estonia BRICS nations
Marino. Some of this isn’t surprising. While we ranked among the very top of the EU. Unsur- Finally we examined the BRICS nations – Bra-
talk later in this report about the sheer volume prisingly so, given its innovative approaches to zil, Russia, India, China, and South Africa. This
of regulations taking place around securing e-government services, world recognition for a examination unveiled that these regions scored
software supply chains, the United States has by digital society and robust digital infrastructure. comparatively lower in the quality of OSS con-
far taken this issue the most seriously, at least in Germany is a prominent software developer sumption compared to the other geographical
terms of focused regulation and national policy hot spot in the EU, and closely followed Esto- groupings. In conclusion, while each region pos-
conversations. nia in its component consumption score. The sesses unique attributes that shape their com-
country’s robust economy, strong engineering ponent consumption habits, it’s crucial to rec-
ASEAN tradition, and technological infrastructure make ognize that the rankings presented are a mere
ASEAN (Association of Southeast Asian Nations) it an attractive destination for software profes- snapshot of their software landscape. They are
is a regional intergovernmental organization sionals. Cities like Berlin, Munich, and Hamburg not intended to comprehensively encapsulate
comprising ten member states in Southeast host thriving tech ecosystems, offering a blend the full scope of any individual country’s soft-
Asia. On average, the ASEAN grouping was the of innovative startups, established tech compa- ware development maturity. As these regions
highest scoring group in regard to consumption nies, and research institutions. In contrast, while navigate their own technological journeys, they
behavior. The member countries of ASEAN are the difference was not vast, it was unexpected are poised to further engage with open source
Brunei, Cambodia, Indonesia, Laos, Malaysia, to observe Sweden and the Netherlands placed initiatives, contributing to the global software
Myanmar, the Philippines, Singapore, Thailand, near the lower end of EU member states, given community’s growth and innovation.
and Vietnam. Among them are technological their well-regarded technology sectors and
hubs such as Singapore and Malaysia as well as developer practices.

CHAPTER 4
Software Supply
Chain Maturity
34
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

Software Supply Chain
the utilization of open source software (OSS) significant changes. In the past year alone, the
Maturity — Peer Insights components, dependency management, gov- emergence of generative AI capabilities and
ernance, approval processes, and tooling. introduction of global regulatory initiatives
The survey also covered questions related to spurred modernization efforts in software
In this year’s report, we dive into insights development practices, demographics, and job development across industries.
gleaned from 621 enterprise engineering pro- satisfaction levels, culminating in a more holis-
fessionals, providing invaluable perspectives tic view of software supply chain maturity at an To further understand this ever-evolving land-
on software supply chain management and enterprise and industry level. scape, we marry last year’s findings with
organizational development practices. Our what changed today. We explore interesting
analysis draws from a comprehensive survey Expanding Horizons year-over-year trends, examine the growing
that explored the multifaceted landscape of Over the last decade, the software supply demand for Software Bill of Materials (SBOMs),
software supply chain management, including chain landscape has experienced rapid and and identify key practices aimed at not wasting
developer time. Furthermore, we take a deeper
look at companies affected by open source risk,
EIGHT THEMES OF SOFTWARE SUPPLY particularly those who have experienced secu-
CHAIN MANAGEMENT PRACTICES rity breaches. Through this investigation, we aim
to shed light on how these organizations may
APPLICATION INVENTORY GIVING BACK differ from their peers and provide insights into
Do you know all the applications (Also referred to as “contribution”) Do
bolstering security measures within the software
within your organization’s develop- you actively and consistently contribute
supply chain.
ment/production pipeline, including to the OSS community?
their stakeholders/owners, archi-
POLICY CONTROL
Continuing Objectives
tectural details, and SBOMs for the
Do you have risk management policies
included OSS components? and Methodologies
in place, and do they align with your risk
SUPPLIER HYGIENE tolerance? Do you employ automated Consistent with our approach in previous edi-
Can you identify your suppliers and policy enforcement? tions, this chapter maintains two core objectives:
ensure that your OSS components
DIGITAL TRANSFORMATION
come from trusted, quality sources?
(Also known as an “execution plan”) (cid:28)Provide a benchmark and maturity model that
BUILD & RELEASE What strategies, resources, and training enables organizations to assess their prac-
Do you understand how your software initiatives are in place to support adop- tices in comparison to their industry peers.
components and processes come tion of new processes and tools as part
together to build and release applica- of your digital transformation goals?
(cid:28)Determine if reported software supply chain
tions into production?
REMEDIATION
practices align with desirable outcomes.
PROJECT CONSUMPTION How do you implement fixes to address
What are your consumption policies identified risks associated with OSS
To evaluate responses to the comprehen-
governing the selection of OSS com- components?
ponents within your projects? sive survey, we will examine them within the
35
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
YTIRUTAM
NIAHC
YLPPUS
ERAWTFOS
:4
RETPAHC

FIGURE 4.2
framework of eight key themes of mature soft- scored the responses from 1 to 5, corresponding
FIVE STAGES OF SOFTWARE SUPPLY
ware supply chain management practices. to the five stages of software supply chain matu-
CHAIN MANAGEMENT MATURITY
rity. From Unmanaged (least mature) to Monitor
Less Mature
& Measure (most mature), as noted in Figure 4.1
How mature are
Unmanaged
today’s software Perception is disconnected This first stage is referred to as the Unmanaged stage
because organizations are often operating with an
from reality – again
supply chains? "anything goes" mindset, are often reactive, and have
In last year’s survey, the data showed a notable minimal process/oversight related to the themes.
pattern: respondents tended to self-report a
We’ve distilled and presented collective insights higher level of software supply chain maturity
Exploration
from the 621 surveyed individuals in Figure 4.2. than their actual stage of advancement, leaving A realization of some sort is usually the impetus for thrusting
To develop this summary, we averaged each many with an inflated sense of security. This an organization into the Exploration stage. This is often
triggered by an “event” that causes an “all hands on deck”
individual’s responses on questions that align trend persists into this year’s findings
reaction to uncover necessary information/solutions, or
with the eight key themes. In each theme we a champion of some sort leading an improvement effort.
This stage is often focused on identifying the perceived
problem/inefficiency, learning about current implemen-
FIGURE 4.1 tations, and starting to explore potential solutions.
SOFTWARE SUPPLY CHAIN MATURITY SCORE BY THEME
Ad Hoc
In the midst of starting to define processes and imple-
ment tooling to improve the identified problem, Ad Hoc
solutions reign as the teams work toward institutional-
ization and socialization of new tooling and processes.
Control
In the Control stage, ad hoc solutions give way to more
formalized governance processes across the enter-
prise. Socialization and institutionalization of these
processes and tools is ongoing, but for the most part,
stakeholders are bought in to the need for improve-
ment measures and are working towards compliance.
Monitor & Measure
The Monitor and Measure stage occurs once new
processes and tools have been institutionalized,
and organizations have reached a phase of being
able to proactively address OSS component risk. In
addition, a healthy amount of ROI is realized, and
measurements to demonstrate success are available.
More Mature
36
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
YTIRUTAM
NIAHC
YLPPUS
ERAWTFOS
:4
RETPAHC

Overall, this year’s survey reveals that respon- predominantly received the bulk of survey
dents generally demonstrated lower levels of responses. 67%
maturity in the Digital Transformation theme
and higher levels of maturity in Remediation. To get a sense of how your organization com- of respondents feel confident that
This consistent year-over-year trend under- pares, take this short quiz on software supply their applications are not using known
scores a fascinating disparity between how chain maturity. vulnerable libraries
survey respondents self-assess their progress
in actively addressing vulnerabilities (indicative
How have software
of higher maturity) versus their capacity to gar-
ner essential buy-in, sponsorship, training, and supply chain 10%
operational processes for effective remediation
management of respondents reported that their
(reflecting lower maturity).
organization had a security breach
trends changed?
due to a vulnerability in the last 12
From this, a striking statistic emerges: 67% of
months
respondents feel confident that their applica- The software supply chain plays a vital role in
tions do not rely on known vulnerable libraries. modern development processes. Understand-
However, nearly 10% of respondents reported ing its dynamics is crucial for mitigating risk and
that their organizations had security breaches ensuring operational efficiency. This section
20%
due to open source vulnerabilities in the last 12 unveils key insights from our survey of engi-
months, while 20% were unsure if their orga- neering professionals, offering a comparative
of respondents were unsure if their
nization had been breached. Pair this with the analysis of this year’s responses to those of the
organization had been breached Iin
objective information we saw in Chapter 1 – that previous year. By analyzing these year-over-
the last 12 months
1 in 8 open source downloads have a known year trends, we gain a clear view of significant
vulnerability – and it’s clear that no matter how changes and evolutions in the landscape of the
we look at it, there continues to be a software software supply chain.
supply chain management problem.
HOW MATURE IS YOUR
In addition, aside from remediation and appli- Finding #1: Increased focus SOFTWARE SUPPLY CHAIN?
cation inventory, most respondents received on open source risk
ratings below the “4 — Control” level of matu- In a landscape marked by the growing volume
Take the quiz
rity. The “Control” level represents a crucial of open source, efficiency in software develop-
milestone, where organizations move from a ment is the key to not wasting developer time.
phase of uncertainty to a minimal level of matu- This year, our survey results highlighted the
rity that enables the production of high-quality interplay between effective tools, developer
outcomes. Notably, the three maturity levels satisfaction, and optimized work processes.
preceding “Control” (Unmanaged, Explora- Respondents reported an increase in the use
tion, Ad Hoc) are considered suboptimal and
37
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
YTIRUTAM
NIAHC
YLPPUS
ERAWTFOS
:4
RETPAHC

of integrated tooling (+9.8%), growing aware- a focus” for their organization (9.3%), and like-
Changes in Supply Chain
ness of and focus on open source risk (+9.3%),  wise, a decrease in those agreeing (-9.6%).
Management Trends
improved dependency upgrade decisions
(+9.6%), and greater comfortability in software  IMPROVED UPGRADE DECISIONS  AAAADDDDOOOOPPPPTTTTIIIIOOOONNNN    OOOOFFFF    IIIINNNNTTTTEEEEGGGGRRRRAAAATTTTEEEEDDDD    TTTTOOOOOOOOLLLLIIIINNNNGGGG
supply chain management (+7.7%) – all of which  Respondents reported a decreasing number
point to a maturing market and an increasing  of times that dependency upgrades “always/ 14.5% 9.8%
industry-wide understanding of the downstream  often/frequently” broke the functionality of their
|     | decrease recorded  | increase was found in  |
| --- | ------------------ | ---------------------- |
threats vulnerable open source poses application, and an increase in the number of  among respondents  the integration of risk
|     | who received reports  | information into con- |
| --- | --------------------- | --------------------- |
times dependency upgrades rarely or never
|     | from external sources. | tinuous integration (CI)  |
| --- | ---------------------- | ------------------------- |
An overarching theme is clear: the combination  broke their application’s functionality. Not only
and build processes
of robust tools and happy developers plays a  does this point to respondents getting better
significant role in minimizing workloads.  at handling dependency upgrades and avoid- GGGGRRRROOOOWWWWIIIINNNNGGGG    FFFFOOOOCCCCUUUUSSSS    OOOONNNN    OOOOPPPPEEEENNNN    SSSSOOOOUUUURRRRCCCCEEEE    RRRRIIIISSSSKKKK
ing breaking changes, it also shows a deeper
|     | 9.3% | 9.6% |
| --- | ---- | ---- |
ADOPTION OF INTEGRATED  understanding of open source hygiene.
TOOLING
|     | respondents disagree- | respondents agreeing  |
| --- | --------------------- | --------------------- |
One notable trend observed this year is a  GREATER COMFORT EQUALS  ing with the statement  with the statement
|     | that “open source  | that “open source  |
| --- | ------------------ | ------------------ |
decline in the reliance on ad-hoc reports for  GREATER EFFICIENCY
|     | risk is not currently  | risk is not currently  |
| --- | ---------------------- | ---------------------- |
obtaining risk information about open source  Overall, respondents feel more comfortable and  a focus” for their  a focus” for their
|     | organization  | organization  |
| --- | ------------- | ------------- |
libraries. A substantial decrease of 14.5% was  familiar with topics surrounding software supply
recorded among respondents who received  chain management this year. There was a 7.7%
reports from external sources. However, a cor- increase in those that kept up with software sup-
IIIIMMMMPPPPRRRROOOOVVVVEEEEDDDD    UUUUPPPPGGGGRRRRAAAADDDDEEEE    DDDDEEEECCCCIIIISSSSIIIIOOOONNNNSSSS
responding 9.8% increase was found in the inte- ply chain trends.
| gration of risk information into continuous inte- | 9.6% | 4.6% |
| ------------------------------------------------- | ---- | ---- |
gration (CI) and build processes. This shift aligns  However, in line with the chapter’s earlier find-
|     | Respondents reported  | increase in the num- |
| --- | --------------------- | -------------------- |
with the changing preferences, where more  ings, a broader lack of overall maturity and effi-
YTIRUTAM NIAHC YLPPUS ERAWTFOS :4 RETPAHC a decreasing number  ber of times depen-
professionals now favor obtaining risk informa- ciency in software supply chain management  of times that depen- dency upgrades
|     | dency upgrades  | rarely or never broke  |
| --- | --------------- | ---------------------- |
tion within their existing workflows, rather than  persists. While the focus on open source risk
|     | “always/often/ | their application’s  |
| --- | -------------- | -------------------- |
relying on separate reports. has intensified, this year’s findings revealed a  frequently” broke the  functionality
functionality of their
decline in the use of automated open source
application
GROWING FOCUS ON  processes, a lack of well-defined processes,
OPEN SOURCE RISK  and a lower number of respondents that follow  GGRREEAATTEERR  CCOOMMFFOORRTT  EEQQUUAALLSS
GGRREEAATTEERR  EEFFFFIICCIIEENNCCYY
Another interesting finding: open source is very  their organization’s open source approval pro-
much a focus for engineering teams, and is a  cedures. In other words, organizations continue
 7.7%
growing one at that. There was a significant  to grapple with immature practices that waste
increase in respondents disagreeing with the  time and resources – weighing teams down and  increase in those that kept up with software supply
chain trends.
statement that “open source risk is not currently  slowing development.
38
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

FIGURE 4.3
Organizations continue SBOM SURVEY RESPONSES
to grapple with
immature practices
that waste time and
resources – weighing
teams down and
slowing development.
A year-over-year decrease in agreement (9.5%)
and increase in disagreement (3.4%) with the
statement “We have executive sponsorship”
underscores that achieving software supply
chain maturity necessitates not only effective
tools but also strong organizational support
In summary, although there is an increased
focus on and awareness of open source risk,
organizations have ample ground to cover in
implementing best practices for mitigating these Finding #2: Rise in demand for This document serves as a critical resource for
risks effectively. Software Bills of Materials understanding and managing the software sup-
Thanks to mandates outlined in President ply chain. By enabling developers and organiza-
Biden’s Executive Order on Improving the tions to accurately track and assess the security
Nation’s Cybersecurity and the growing global and licensing aspects of software components,
regulatory efforts, one open source best prac- SBOMs play a vital role in software develop-
75%
tice that is experiencing a growth in adoption is ment, cybersecurity, and regulatory compliance.
the use of an SBOM. SBOMs provide transparency and visibility into
of leaders
reported generating
software composition, thereby facilitating effi-
SBOMs for their
25% An SBOM serves as a comprehensive inven- cient risk management, enhancing vulnerability
applications
tory, outlining the various components and response, and supporting effective software
of engineering
dependencies of a software application. It pro- maintenance. Ultimately, while the creation of
professionals
vides a detailed list of the software’s building SBOMs themselves doesn’t equate to security,
blocks, including open source and third-party the adoption of SBOMs contributes to build-
libraries, along with their respective versions. ing secure, reliable, and trustworthy software
39
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
YTIRUTAM
NIAHC
YLPPUS
ERAWTFOS
:4
RETPAHC

systems, benefitting both software producers Although, this finding also might just track with
and consumers. last year’s data that revealed how managers
Our survey revealed
often report higher stages of maturity compared
This year, we took a deeper look at the usage to other roles. Compared to respondents work- that only 22% of
and demand for SBOMs. Findings revealed that ing in information security, IT managers were
organizations become
nearly 53% of the surveyed engineering profes- 1.8 times more likely to strongly agree with the
sionals reported they are generating an SBOM statement “We know the Software Bill of Materi- aware of new open
for every application (Figure 4.3). Notably, als (SBOM) for every application.”
source vulnerabilities
respondents who adopted this practice were
within a day of disclosure
less likely to report security breaches. In addition, nearly half of the respondents have
started asking vendors to supply SBOMs for
However, when we contrast this with survey purchased software, underscoring a higher
results from cybersecurity leaders at large demand for increased transparency in software
enterprises (over £50 million/$50 million annual supply chains particularly those that have experienced
revenue), we observed that 75% of these security breaches.
leaders reported generating SBOMs for their Finding #3: The critical
applications. Compared to the 53% reported connection of hygiene and Our analysis revealed a connection between
by engineering professionals in our general speed in risk mitigation security breaches and suboptimal management
survey, this discrepancy underscores the height- This year, we investigated how organizations practices such as:
ened demand for SBOMs at larger enterprises. have been impacted by open source risk,
(cid:28)deploying every change directly to production;
FIGURE 4.4
TIME TO REMEDIATE KNOWN VULNERABILITIES AFTER DETECTION
(cid:28)breaking the functionality of their applications
with dependency upgrades; and
(cid:28)adhering to an entirely waterfall development
practice
Additionally, organizations that experienced
breaches exhibited delayed awareness and
mitigation of vulnerability risks. Breached orga-
nizations were 2.9x more likely to take over six
months to become aware of open source vul-
nerabilities after their discovery, and 1.7x more
likely to report never fixing a vulnerability
40
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
YTIRUTAM
NIAHC
YLPPUS
ERAWTFOS
:4
RETPAHC

In the context of organizations grappling with encompass practical strategies aimed at not
The journey toward security breaches, these findings emphasize only enhancing security but also at optimizing
the critical connection between maintaining developer productivity and reducing the waste
software supply chain
strong hygiene practices and swift risk mitiga- of developer time.
maturity is not just tion. Organizations that have already embarked
on the journey to software supply chain matu- The journey toward software supply chain matu-
a path to enhanced
rity are better equipped to effectively manage rity is not just a path to enhanced security — it’s
security — it’s also a
open source risks. With advanced software also a path to stop wasting developer time. By
path to stop wasting supply chain maturity, these organizations apply improving software supply chain maturity, orga-
streamlined processes for identifying, respond- nizations create an environment in which devel-
developer time.
ing to, and resolving vulnerabilities, significantly opers can focus on innovation, leading to more
reducing the vulnerability window and contribut- resilient and secure software.
ing to their overall maturity
Overall, our survey revealed that only 28%
of organizations become aware of new open For organizations navigating the complexities
source vulnerabilities within a day of disclosure. of open source risk and striving for swift mitiga-
Thirty-nine percent (39%) discover them within tion, the path to software supply chain maturity
one to seven days, and 29% take over a week to emerges as a pivotal strategy. This enables
become aware them to enhance their resilience, ultimately for-
tifying their security posture and safeguarding
The same survey found that 39% of respon- against potential breaches
dents require over a week to mitigate vulnera-
bilities (Figure 4.4). This means that the majority These findings align with the eight key themes
of bad actors have days to launch a malicious of software supply chain management outlined
attack on enterprise targets. at the beginning of this section. These themes
41
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
YTIRUTAM
NIAHC
YLPPUS
ERAWTFOS
:4
RETPAHC

CHAPTER 5
Establishment
and Expansion of
Software Supply
Chain Regulations
and Standards
42
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

43
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
SDRADNATS
DNA
SNOITALUGER
NIAHC
YLPPUS
ERAWTFOS
FO
NOISNAPXE
DNA
TNEMHSILBATSE
:5
RETPAHC
United States
Worldwide, we continue to see a push for digi- enhancing the security of the software supply
tal transformation not only in the private sector chain of the Department” after “best interests of
but increasingly through government guidance National the Department.”
and regulation. In 2022, the European Union Cybersecurity
Agency for Cybersecurity (ENISA) identified Strategy (NCS) FDA Cybersecurity in
the compromise of software supply chains The NCS has been hailed as the foundational Medical Devices
through software dependencies as the foremost document for advancing cybersecurity and is On December 29, 2022, the Consolidated
emerging threat. Recognizing the profound shaping legislation globally. Its comprehensive Appropriations Act, 2023 (“Omnibus”) became
implications of cyber threats to national security content underscores the urgency of enhancing law. Within it, Section 3305 titled “Ensuring
and economic stability, the United States and cybersecurity both in the US and internationally. Cybersecurity of Medical Devices” updated the
the European Union (EU) have taken the lead Addressing a wide range of areas, from infra- Federal Food, Drug, and Cosmetic Act (FD&C Act)
in orchestrating robust regulatory frameworks structure—addressing incidents like SolarWinds by introducing section 524B on device cyberse-
and providing substantive guidance to fortify and NotPetya—to SBOMs alignment with EO curity. According to the Omnibus, cybersecurity
defenses against escalating cyber risks. Their 14028, the NCS emphasizes the growing impor- mandates won’t apply to applications or submis-
comprehensive approach to cybersecurity tance of security in software design. Moreover, sions made to the FDA before March 29, 2023.
includes stringent requirements for critical infra- it underscores impending changes in account-
structure sectors, enactment of rigorous data ability for software manufacturers. Specifically, SEC Regulation
protection laws, and enhancement of interna- those unable to prove that security is inherently Similar to the FDA, the Securities and Exchange
tional cooperation to combat cybercrime. integrated into their software design will face Commission (SEC) has proposed a number of
increased responsibilities and liabilities. rules (33-11028,33-11038,34-91742) for pub-
However, various regions across the globe are lic companies, the securities market, advisers,
experiencing notable surges in cybersecurity Securing Open Source funds, and others within SEC’s regulatory scope.
endeavors outside the US and EU. Canada, Software Act of 2023 This move responds to various findings, includ-
Japan, Australia, Germany, and others are In March 2023, Congress introduced legisla- ing those by theFBI and Congress, as well as
acknowledging the criticality of securing soft- tion “To establish the duties of the Director of
ware supply chains by drafting legislation and the Cybersecurity and Infrastructure Security
building capabilities to thwart cyber threats. Agency regarding open source software secu- The National
While the bulk of documented guidance and rity, and for other purposes.”
Cybersecurity Strategy
regulation is coming from the US and EU, it’s
clear the pressing need to safeguard the digital AI for National Security Act underscores the
realm is a global imperative. In March 2023, the House Armed Services Com-
impending changes
mittee introduced legislation “To make certain
in accountability and
improvements to the enterprise-wide procure-
ment of cyber data products and services by liability for software
the Department of Defense and for other pur-
manufacturers in the US.
poses.” In subsection (b), it inserts “including by

44
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
SDRADNATS
DNA
SNOITALUGER
NIAHC
YLPPUS
ERAWTFOS
FO
NOISNAPXE
DNA
TNEMHSILBATSE
:5
RETPAHC
CISA, that state “cybersecurity incidents are initiated by EO 14028, which directed NIST to Implementation Plan (NCSIP) to align roles,
underreported.” provide guidance on secure software devel- responsibilities, and resources in cyberspace.
opment standards. EO 14028 also directed the
Among the new rules are requirements for Office of Management and Budget (OMB) to It focuses on two shifts:
organizations to demonstrate the development require federal agencies to collect information
of robust processes and procedures for vul- from software manufacturers that supply soft- (cid:28)Greater burden-sharing in cybersecurity by
nerability management, detection, mitigation, ware products to the US government. The OMB major entities
and remediation. In addition to these require- responded withMemo MM-22-18, setting the
ments, the SEC has proposed specific rules guidelines for requiring federal agencies to col- (cid:28)Promotion of long-term cybersecurity
concerning the disclosure of said processes and lect this information. investments
procedures.
As part of these guidelines, software manu- The plan outlines over 65 high-impact initiatives,
In July 2023, the SEC adopted new rules com- facturers must attest to using secure software from combating cybercrimes to building a skilled
pelling organizations to disclose significant development best practices highlighted in the cyber workforce, which is aligned to the five
cybersecurity incidents and provide annual memo and developed by NIST. While this is sim- pillars outlined in the National Cybersecurity
cybersecurity risk management, strategy, and ply a first step, it aligns with the secure-by-de- Strategy:
governance information with comparable sign-and-default approach CISA has released. It
requirements for foreign private issuers. Regis- incorporates secure software development best (cid:28)Pillar One | Defending Critical Infrastructure:
trants must also describe their cybersecurity risk practices from the NIST Secure Software Devel- This pillar focuses on updating the National
assessment processes and board oversight in opment Framework (SSDF) and asks organiza- Cyber Incident Response Plan to enhance
an annual report. tions providing software to the US government coordination during cyber incidents and pro-
to self-attest that they have embedded this guid- vide clear guidance to external partners, led
SEC Chair Gary Gensler emphasized that any ance into their software development process. by the Cybersecurity and Infrastructure Secu-
material event, including cybersecurity inci- rity Agency (CISA).
dents, should be disclosed to benefit investors National Cybersecurity Strategy
and the market. The rules mandate disclosing Implementation Plan (cid:28)Pillar Two | Disrupting and Dismantling
the specifics of a significant cybersecurity inci- In July 2023, the Biden-Harris Administration Threat Actors: This pillar aims to combat ran-
dent—namely, its nature, scope, timing, and released the National Cybersecurity Strategy somware and cybercrime with coordinated
impact—within four business days unless it’s
deemed a national security risk by the U.S. Attor-
The OMB’s Self-attestation policy will require software
ney General, in which case it can be delayed.
manufacturers doing business with the US Government
Secure Software Self-
to attest to NIST guidelines based on CISAs secure-by-
Attestation Common Form
design and secure-by-default principles established in
In April 2023, this document was released for
comments. It represents a sequence of events the National Cybersecurity Strategy.

45
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
SDRADNATS
DNA
SNOITALUGER
NIAHC
YLPPUS
ERAWTFOS
FO
NOISNAPXE
DNA
TNEMHSILBATSE
:5
RETPAHC
efforts, including disruption operations entities. It covers key areas like critical infra- The roadmap focuses on four key goals to guide
against ransomware ecosystems and offering structure defense, threat actor disruption, shap- CISA in enhancing OSS security, aligning with
resources to high-risk targets, co-chaired by ing market forces, investing in resilience, and broader cybersecurity strategies, and fostering
CISA and the FBI. forging international partnerships. collaboration with the OSS community and inter-
national partners:
(cid:28)Pillar Three | Shaping Market Forces and Cyber Strategy of the Department
Driving Security and Resilience: This pillar of Defense (Declassified) (cid:28)Goal 1: Establish CISA’s role in supporting OSS
seeks to increase software transparency In September 2023, the Department of Defense security, partnering with OSS communities,
through a Software Bill of Materials (SBOM) (DOD) released a declassified summary of its and encouraging collective action.
to reduce supply chain risks, led by CISA, and classified 2023 Cyber Strategy, aligning it with
explore a globally-accessible database for national security priorities. It builds on lessons (cid:28)Goal 2: Drive visibility into OSS usage and
end-of-life software. learned from cyber operations and the Rus- risks, understanding the prevalence of OSS,
sia-Ukraine conflict, emphasizing collaboration developing a risk prioritization framework, and
(cid:28)Pillar Four | Investing in a Resilient Future: with allies and partners. assessing threats.
Focusing on cybersecurity standards and
quantum-resistant cryptography, this pillar, The strategy aims to maximize cyber capabilities (cid:28)Goal 3: Reduce risks to the federal govern-
led by the National Institute of Standards and for integrated deterrence, enhance cyber net- ment by evaluating solutions for secure OSS
Technology (NIST), aims to enhance U.S. lead- work defense, support non-DOD agencies, and usage, developing open source program
ership in international cybersecurity standard- safeguard the defense industrial base. Notably, office (OSPO) guidance, and prioritizing fed-
ization and quantum-resistant cryptographic it commits to bolstering collective cyber resil- eral actions in OSS security.
algorithms. ience among allies and integrating cyber capa-
bilities into traditional warfighting efforts. This (cid:28)Goal 4: Harden the OSS ecosystem, advance
(cid:28)Pillar Five | Forging International Partner- marks the fourth iteration of the DOD’s cyber software bills of materials (SBOMs), foster
ships to Pursue Shared Goals: This pillar strategy, informed by significant experience in security education for OSS developers,
involves development of international cyber- cyberspace operations. publish OSS security best practices, and
space and digital policy strategies, collabora- coordinate OSS vulnerability disclosure and
tion with partners and allies, and strengthen- CISA Open Source Software response.
ing of knowledge and skills in cyberspace and Security Roadmap
digital policy, led by the Department of State. In September 2023, at the OpenSSF Secure NHTSA Cybersecurity Best
Open Source Software Summit, CISA Practices of Modern Vehicles
Overall, the strategy emphasizes resilience, announced its Open Source Software Security In September of 2022, the United States Depart-
equity, and defense in cyberspace, led by 18 Roadmap, which outlines strategic goals and ment of Transportation National Highway Traffic
government agencies and coordinated by the objectives for enhancing the security of open Safety Administration (NHTSA) published Cyber-
Office of the National Cyber Director (ONCD). source software (OSS). security Best Practices for the Safety of Modern
The NCSIP aligns with the private sector, civil Vehicles, a document aimed at addressing cyber-
society, international partners, and government security in modern vehicle manufacturing.

46
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
SDRADNATS
DNA
SNOITALUGER
NIAHC
YLPPUS
ERAWTFOS
FO
NOISNAPXE
DNA
TNEMHSILBATSE
:5
RETPAHC
Among many recommendations, the NHTSA markets. In some cases, it may discourage Network and Information
guides manufacturers to demonstrate pro- involvement in open source software in the EU Security Directive (NIS2)
cesses and procedures to inventory software altogether, putting EU-based companies far In December 2022, the European Parliament
assets, track details related to open source behind innovation and efficiency leaps in other approved updates to the Network and Informa-
software components, continuously monitor and geographical areas. tion Security Directive (NIS), referring to it going
assess risk, and disclose vulnerabilities. Most of forward as NIS2. NIS2 is an evolution intended
these recommendations are also backed by the Product Liability Directive (PLD) to modernize the approach of EU member
International Organization of Standardization The PLD delineates rules and guidance for the nations towards cybersecurity. Among a host of
(ISO) cybersecurity standards. liability and responsibility of manufacturers of updates, NIS2 includes call-outs for improved
defective products as well as suppliers of defec- software supply chain security, greater attention
tive parts for those products. A proposed update to critical vulnerabilities, the increase of attacks
European
in September 2022 marked a notable expansion via malicious threats, and the necessity of pro-
Union encompassing software and digital products, cesses for disclosure and communication, such
which had been excluded previously. as Coordinated Vulnerability Disclosure (CVD).
Cyber Resilience Act (CRA) These updates put open source software and NIS2 makes it clear that “Businesses identified
The CRA was proposed in September 2022, any related projects or activity within the poten- by the Member States as operators of essential
and it was met with mixed reviews. On the sur- tial sights of liability or responsibility associated services in the above sectors will have to take
face, it represents an improvement in holding with defects (i.e., vulnerabilities). For example, as appropriate security measures and notify rel-
manufacturers liable for the security of the soft- written, there would be potential to find distrib- evant national authorities of serious incidents.
ware products they produce. However, it also utors of parts, such as Sonatype/Maven Central, Key digital service providers, such as search
represents a different direction for holding open liable for open source vulnerabilities resulting in engines, cloud computing services and online
source projects and creators liable for vulnera- loss or in some cases even distress to software marketplaces, will have to comply with the
ble software and attempts to potentially bring product customers. security and notification requirements under
them in line with any traditional supplier. This the Directive.” In addition, there are a number of
approach presents interesting issues.
Although open source software is part of the
As currently formulated, the CRA carries the potential
software supply chain, how someone uses the
software is often outside the understanding and to pose substantial barriers to many open source
control of the creator or open source project
projects and even the distributors of open source
itself. As currently formulated, the CRA carries
the potential to pose substantial barriers to software, potentially limiting their accessibility to
many open source projects and even the dis-
European Union markets.
tributors of open source software, potentially
limiting their accessibility to European Union

47
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
SDRADNATS
DNA
SNOITALUGER
NIAHC
YLPPUS
ERAWTFOS
FO
NOISNAPXE
DNA
TNEMHSILBATSE
:5
RETPAHC
requirements imposed based on different busi- and best practices for securing software sup- (cid:28)Promotion of secure software culture: They
ness categories: Highly Critical Sectors, Critical ply chains. The document outlines the impor- aim to promote a culture where software
Sectors, and Essential Entities. In order to help tance of minimizing software supply chain risk, security is a fundamental aspect of software
countries address these requirements, ENISA including the ability of malware to compromise development.
has published guidance documentation includ- updates, and the importance of remediating
ing Good Practices for Supply Chain Security. vulnerabilities in open source software compo- (cid:28)Minimum cybersecurity guidelines: The Quad
Failure to meet the requirements established nents. Recommendations include vetting sup- partners commit to establishing minimum
within NIS2 can result in a number of sanctions. pliers, monitoring them continuously, and incor- cybersecurity guidelines for governments to
porating supply chain risk management into guide software development, procurement,
security programs. Finally, organizations should and usage, aligned with international obliga-
Canada
have recovery plans to ensure business continu- tions and domestic laws.
ity when software supply chain attacks occur.
On October 28, 2022, the Canadian Centre (cid:28)Engagement with the software industry:
for Cyber Security (the Cyber Centre) released They plan to engage with the software indus-
Global partnerships
its National Cyber Threat Assessment 2023- try to ensure secure software practices are
2024, warning that state-sponsored and crimi- integrated throughout the software devel-
nal cyber threats are increasingly likely to affect Quad Cybersecurity Partnership: opment life cycle, with the goal of reducing
Canadians. The report highlights five key areas Joint Principles for Secure Software vulnerabilities.
of concern: ransomware, critical infrastructure,
state-sponsored threats, influence operations, UNITED STATES, JAPAN, (cid:28)Secure software development practices: The
and disruptive technologies. INDIA, AND AUSTRALIA document outlines high-level secure software
Published in May 2023, the “Quad Cybersecu- development practices, including preparing
Among a number of criteria, the report also rity Partnership: Joint Principles for Secure Soft- the organization, protecting software and
cites increased risk from remote work, more ware” document outlines the commitment of the its development environment, producing
connected systems, and the proliferation of Quad partners (the United States, Japan, India, well-secured software, and responding to
cybercrime tools. In assigning responsibility, and Australia) to enhance software security. vulnerabilities.
the report points to threat actors in China,
Russia, Iran, and North Korea that pose the The main points are: (cid:28)Government procurement guidelines: Each
greatest state-sponsored risk. In response, the Quad country intends to adopt guidelines for
Canadian government has invested in cyberse- (cid:28)Recognition of security risks: The Quad government procurement of software, includ-
curity, including $875 million in Budget 2022 to partners acknowledge the risks associated ing self-attestation by software producers
bolster defenses. with the software supply chain being tam- regarding secure development practices and
pered with by adversarial and non-adversarial encouraging participation in national vulnera-
In February 2023, the Cyber Centre published threats. bility disclosure programs.
“Protecting your organization from software
supply chain threats,” which offers guidance

48
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
SDRADNATS
DNA
SNOITALUGER
NIAHC
YLPPUS
ERAWTFOS
FO
NOISNAPXE
DNA
TNEMHSILBATSE
:5
RETPAHC
(cid:28)Security measures for government software (cid:28)Australian Signals Directorate’s Australian manufacturers to prioritize security as a core
use: The Quad partners commit to implement- Cyber Security Centre (ASD’s ACSC) business objective. To achieve success, a global
ing controls and processes to protect govern- shift towards embracing Secure-by-Design
ment software and platforms from unautho- (cid:28)Canadian Centre for Cyber Security (CCCS) and Secure-by-Default practices is imperative,
rized access and usage. fostering transparency, accountability, and
(cid:28)United Kingdom’s National Cyber Security collaboration between manufacturers and cus-
The document’s purpose is to strengthen soft- Centre (NCSC-UK) tomers. This necessitates manufacturers being
ware security across Quad countries, encourage held accountable for product security outcomes
the adoption of secure software practices, and (cid:28)Germany’s Federal Office for Information and prioritizing Secure-by-Design and Secure-
establish guidelines for software procurement Security (BSI) by-Default principles when making technology
and usage in government contexts. procurement decisions. Overall, this guidance
(cid:28)Netherlands’ National Cyber Security Centre shapes future cybersecurity policies by advocat-
Secure by Design and Default (NCSC-NL) ing for proactive security measures and shared
International Support responsibility within the technology ecosystem.
(cid:28)New Zealand’s National Cyber Security Cen-
AUSTRALIA, CANADA, tre (NCSC-NZ) and Computer Emergency
Are software supply
UNITED KINGDOM, GERMANY, Response Team New Zealand (CERT NZ)
NETHERLANDS, NEW ZEALAND chain regulations
In April 2023, the Australian Cyber Security Cen- The significance of this collaboration cannot
working?
ter (ACSC) published “Shifting the Balance of be overstated as it represents a pivotal shift in
Cybersecurity Risk: Principles and Approaches cybersecurity responsibility towards software
for Security-by-Design and Default.” This is the organizations. As previously discussed, the As we’ve seen from the analysis above, we’re
same document that has become the guiding “Secure by Design and by Default” approach still in the very early stages of implementing true
foundation for the US Cybersecurity Strategy. highlights the crucial integration of security into regulation that will hold people accountable for
Though theguidance has been led by CISA the design and default settings of technology a more secure software supply chain.
and the FBI in the US, the document represents products, effectively mitigating cyber threats. It
a collaboration across many international cyber- emphasizes that the onus of security should not But, especially in the United States, the con-
security organizations: solely rest on end-users, compelling technology versation and incremental changes since
President Biden’s Executive Order on Improv-
ing the Nation’s Cybersecurity, is starting to
The significance of this collaboration cannot become noticeable. As a direct requirement of
the executive order, the Office of Management
be overstated as it represents a pivotal shift in
and Budget (OMB) was instructed to develop
cybersecurity responsibility towards software policy for federal agencies working with gov-
ernment contractors. Following that directive, organizations.
the OMB released Memo M-22-18, highlighting

49
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
SDRADNATS
DNA
SNOITALUGER
NIAHC
YLPPUS
ERAWTFOS
FO
NOISNAPXE
DNA
TNEMHSILBATSE
:5
RETPAHC
the importance and potential requirement for Respondents are increasingly investing in
SBOMs, especially as part of new self-attesta- 76% technologies to improve software supply chain
tion standards. To understand this further, we management, including vulnerability scanning
of enterprises have adopted a Soft-
surveyed 217 Cybersecurity Directors in orga- (30%), software composition analysis (24%),
ware Bill of Materials (SBOM) since
nizations with over £50 million/$50 million rev- supply chain automation (23%), threat intelli-
the President Biden’s Executive Order
enue in the UK and US respectively, and asked gence (22%), and bug bounty programs (20%).
on Improving the Nation’s Cybersecu-
how much various policies were affecting their The regulation has also fuelled investment in
rity’s introduction
actions toward software supply chain manage- skills and operations like employee training and
ment today. awareness (26%), recruiting developer talent
(21%), and processes to assess supply chain
A huge 76% of enterprises have adopted a Soft- place, only 4% adopted them over three years risks (24%).
ware Bill of Materials (SBOM) since the Order’s ago, demonstrating how much practices have
introduction. Another 16% plan to implement evolved since the Order. We also examined attitudes to regulation
SBOMs within the next year, showing increasing in the UK and the US, uncovering that large
recognition of the correlation between open Our research also confirmed the Order has enterprises generally see regulation as a good
source hygiene and cybersecurity posture. Of influenced enterprises’ software develop- thing. In fact, 41% of security decision-makers
the three-quarters of companies with SBOMs in ment practices in ways transcending SBOMs. see cyber regulation as the factor having the
FIGURE 5.1
HOW SURVEY RESPONDENTS FEEL ABOUT FIGURE 5.2
THE AMOUNT OF SECURITY GUIDANCE PERCENTAGE OF SECURITY LEADERS WHO BELIEVE REGULA-
AND REGULATION IN THEIR COUNTRY TIONS ARE EFFECTIVE FOR IMPROVING CYBERSECURITY

50
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
SDRADNATS
DNA
SNOITALUGER
NIAHC
YLPPUS
ERAWTFOS
FO
NOISNAPXE
DNA
TNEMHSILBATSE
:5
RETPAHC
greatest positive impact on software security. Three key themes have emerged:
Some, however, lament the volume of cyberse-
curity regulation, with 44% of business leaders (cid:28)The heightened emphasis on security during
believing there is too much government inter- software creation.
vention on cybersecurity overall.
(cid:28)Holding software producers accountable for
their products.
Navigating the
policy frontier: (cid:28)The need for robust processes to address
cybersecurity incidents.
Global cybersecurity
regulations The global trend of cybersecurity regulations
in 2023 demonstrates a growing collective
The global landscape of cybersecurity guidance endeavor to adapt to the ever-changing threat
and regulation in 2023 reflects a marked trans- environment. Further international cooperation
formation compared to years past driven by the in this regard will be necessary to better prior-
ever-increasing urgency to address evolving itize secure software development practices.
cyber threats. Regulations covered above as well as future
related initiatives will play a pivotal role in shap-
Initiatives and regulatory actions taken by key ing the future of cybersecurity policies and prac-
players such as the United States, European tices at scale worldwide.
Union, United Kingdom, Australia, Canada,
Japan, and New Zealand demonstrate a shared
commitment to improve digital defenses and
safeguard critical infrastructure.

CHAPTER 6
AI in Software
Development
51
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

52
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
TNEMPOLEVED
ERAWTFOS
NI
IA
:6
RETPAHC
In the ever-evolving digital landscape, artificial
intelligence (AI) and machine learning (ML) stand
Nearly half of the respondents—47% of DevOps and
out as transformative forces reshaping soft-
ware development. As innovation takes center 57% of SecOps—reported that by using AI, they saved
stage, an expanding toolkit of AI components
more than six hours a week.
and models play a pivotal role in driving this
transformation.
Sonatype’s risks &
Our exploration into the impact of AI and ML on generate code. Platforms likeOpenAI’s Codex,
software development draws from our survey rewards of AI survey which powers tools like GitHub’s Copilot, can
of more than 800 developers (DevOps) and assist developers by suggesting entire lines
application security (SecOps) professionals For our recent AI-specific survey, we engaged or blocks of code. Nearly half of the respon-
and research. These insights reveal a broad DevOps and SecOps Leads responsible for dents—47% of DevOps and 57% of SecOps—
adoption trend, with 97% currently incorporating software development, coding, developer rela- reported that by using AI, they saved more than
generative AI in their workflows to some degree. tions, application security, threat intelligence, six hours a week. Automated code suggestions
While the impact and intricacies of these tools and analysis or security operations. Our primary mean faster development cycles.
offer immense opportunities, they also present objective was to understand how teams were
challenges, including concerns for security and using AI in their workstreams. Our questions Beyond speeding up the coding process, AI
the impact on jobs. Adding to these, and of par- ranged from frequency of use to what they helps reduce the potential for human errors
ticular interest to Open Source Software and found beneficial and challenging. We asked thereby expediting time-to-market and improv-
the software supply chain, the consumption of about the tools they were using, which indus- ing the quality and maintainability of software.
AI and ML libraries has seen incredible rates of tries are facing AI-related risks, and where they Emerging AI-driven solutions can identify vul-
adoption. Unfortunately, many of the same con- see the biggest opportunities. We’ll give you a nerabilities, bugs, and inefficiencies in software
cerns are present for teams including unplanned peek at some of the fascinating results below. code more swiftly than traditional methods. By
costs and increased liability. For a more in-depth investigation, you can understanding the context and intent of the
access the full report here. code, these systems can predict potential failure
This section covers two distinct but interre-
lated questions that have emerged on this
The intersection
topic — What role do AI and ML play in assisting
The majority of SecOps
developers, and what are the challenges that AI of AI and software
and DevOps leads
practitioners face in developing AI products? We
development
explore both of those questions here surveyed said they
used AI for testing and
Code generation and testing
One of the most significant implications of analyzing.
AI in software development is its potential to

53
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
TNEMPOLEVED
ERAWTFOS
NI
IA
:6
RETPAHC
The hottest new
programming language
OPPORTUNITY FOR DEVELOPERS AT ALL LEVELS
is English.
The benefits of AI for software developers extend across all levels of the experience spectrum.
For senior developers: For juniors and seniors: points, enhancing the software’s resiliency. The
Enabling a motivated junior Streamlining with majority of SecOps (82%) and DevOps (79%)
private repositories leads surveyed said they used AI for testing and
(cid:28)Senior Developers can leverage AI tools like
analyzing.
GitHub Copilot to quickly complete tedious (cid:28) GitHub Copilot Chat allows developers to
tasks. query the repository directly.
By and large, this is where most of the benefits
(cid:28) ChatGPT offers the promptness of AI tech- (cid:28)These tools benefit developers working with a
are initially realized in software development
nology while allowing juniors to be part of the legacy project with little documentation or local
teams today.
development process and work closer with the knowledge or when they need to learn a new
Senior Devs versus just doing the “grunt work.” code base.
AI tools
(cid:28)AI tools could reduce onboarding time for new Among the 97% of DevOps and SecOps lead-
hires from several months to a few weeks.
ers who confirmed they currently employ AI to
For juniors and seniors:
some degree in their workflows, most said they
ccelerating with an
were using two or more tools daily. Topping the
extensive reference
For junior developers:
list at 86% was ChatGPT and GitHub Copilot at
Benefiting from an AI mentor
(cid:28) Generative AI tools serve as a practical refer- 70%. Notably, GitHub Copilot caters primarily to
ence book for developers of all levels.
(cid:28)Junior developers benefit from having an AI/ developer teams. The capability and widespread
(cid:28) ChatGPT helps look up common behaviors ML tool to answer quick questions and provide adoption of these tools underscores the notion
in programming languages and give clues on insight into technical terms and jargon. that “the hottest new programming language
how to accomplish something without know- is English.” Additionally, respondents also men-
(cid:28)ChatGPT saves time for senior developers by
ing basic syntax. tioned the utilization of other tools such as SCM
handling basic queries, allowing them to focus
(cid:28) Generative AI reduces time spent teaching on more complex issues. Integrations, IDE Plugins, and Sourcegraph Cody.
standard techniques to juniors and helps (cid:28) Large language model (LLM) tools can help
senior developers with brainstorming. answer questions about why a particular tool or
Navigating concern
architecture might be chosen, helping juniors
(cid:28)ChatGPT can also be a valuable tool
understand tradeoffs and potential decisions. for debugging.
While the prospects of Generative AI in soft-
ware development are undoubtedly exciting,
it doesn’t come without its challenges—even

| if those challenges are just perceived and not  |     | necessarily driven by personal preference. A  |     |
| ----------------------------------------------- | --- | --------------------------------------------- | --- |
realized. 61% of developers believe the tech- striking 75% of both groups cited feeling pres- 3 of 4
| nology is overhyped compared to the security  |     | sured from leadership to adopt AI technologies,  |     |
| --------------------------------------------- | --- | ------------------------------------------------ | --- |
DevOps Leads have expressed con-
| leads at 37%. Although the majority of respon- |     | recognizing their potential to bolster productiv- |     |
| ---------------------------------------------- | --- | ------------------------------------------------- | --- |
cerns regarding the impact of genera-
| dents are utilizing AI to varying degrees, it is not  |     | ity despite security concerns.  |     |
| ----------------------------------------------------- | --- | ------------------------------- | --- |
tive AI on security vulnerabilities
Introducing security challenges
FIGURE 6.1
Three (3) out of four (4) DevOps leads have
NUMBER ONE CONCERN ABOUT
Tools require guidance
expressed concerns regarding the impact of
USING GENERATIVE AI
|     |     | generative AI on security vulnerabilities, espe- | AI tools, particularly Large Language Models     |
| --- | --- | ------------------------------------------------ | ------------------------------------------------ |
|     |     | cially in open source code. Additionally, more   | (LLMs), offer significant assistance in various  |
DEVOPS LEADS
|     |     | than 50% of these individuals believe that this  | tasks, but they require considerable guidance to   |
| --- | --- | ------------------------------------------------ | -------------------------------------------------- |
|     |     | technology will complicate threat detection.     | check their work and look for signs of bias. LLMs  |
19% 19% Interestingly, less than 20% of SecOps profes- are not bound by fact, so they should not oper-
|                        |                          | sionals shared these concerns. | ate autonomously. For one, LLMs experience  |
| ---------------------- | ------------------------ | ------------------------------ | ------------------------------------------- |
| it will pose security  | it will require special  |                                |                                             |
hallucinations or false information that require
| and resilience risks      | code governance          |                                                 |                                                   |
| ------------------------- | ------------------------ | ----------------------------------------------- | ------------------------------------------------- |
|                           |                          | Perhaps not surprisingly, 60% of large compa-   | the person using the model to recognize when      |
|                           |                          | nies surveyed were more likely to be concerned  | a mistake is made. AI is also not bound by rules  |
| 18%                       | 14%                      |                                                 |                                                   |
|                           |                          | about security risks compared to less than 50%  | or logical constraints. There is no shortage of   |
|                           |                          | for smaller organizations. The same went for    | YouTube videos where people engage in chess       |
| it might lead to layoffs  | inherent data bias will  |                                                 |                                                   |
or replacement of  impact reliability the illegal use of unlicensed code, 49% of large  matches with ChatGPT. The tool’s highly uncon-
human workers
|     |     | organizations are worried about this, compared  | ventional moves would certainly be deemed     |
| --- | --- | ----------------------------------------------- | --------------------------------------------- |
|     |     | to 41% and 35% for mid-size and small organiza- | unacceptable in a legitimate game. This rein- |
SSEECCOOPPSS  LLEEAADDSS
|     |     | tions, respectively. | forces the concept that AI is a tool to augment  |
| --- | --- | -------------------- | ------------------------------------------------ |
human capability rather than replace it. It will
| 20% | 18% |     | require experience and knowledge to identify  |
| --- | --- | --- | --------------------------------------------- |
TNEMPOLEVED ERAWTFOS NI IA :6 RETPAHC
it might lead to layoffs  it will pose security  these mistakes when LLMs generate code. If
| or replacement of  | and resilience risks | This reinforces the  |     |
| ------------------ | -------------------- | -------------------- | --- |
not carefully monitored, the risk of developing
human workers
|     |     | concept that AI is a  | technical debt, a concern of about 15% of each  |
| --- | --- | --------------------- | ----------------------------------------------- |
surveyed group, might become a reality.
| 15%                   | 14%                        | tool to augment human   |                  |
| --------------------- | -------------------------- | ----------------------- | ---------------- |
| lack of transparency  | it will lead to increased  | capability rather than  |                  |
| in to the reasoning   | technical debt             |                         | Job implications |
| process (black box)   |                            | replace it.             |                  |
will lead to uncertain  One of the most palpable fears associated with
| results |     |     | the rise of AI and ML is job displacement. 1 in 5  |
| ------- | --- | --- | -------------------------------------------------- |
of the SecOps leads in our survey noted this as
54
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

55
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
TNEMPOLEVED
ERAWTFOS
NI
IA
:6
RETPAHC
FIGURE 6.2
their top concern. The current shortage in cyber-
NUMBER OF ENTERPRISE APPS USING AI COMPONENTS
security talent, specifically, forces organizations
to get creative to fill that gap. AI might be one
way to do that. However, the reality points to a
shift in roles rather than outright replacement.
The technology is creating an environment
where human creativity, intuition, and strategy
are more valuable than ever. As shown above,
in software engineering, junior, senior and every
level in between can benefit from the use of AI in
their workstreams and as a learning tool.
AI’s open source
toolkit: Components
and models in focus
FIGURE 6.3
these technologies to stay competitive and TOP 25 MOST POPULAR DATA
drive innovation in their operations. SCIENCE COMPONENTS
Doubling down on AI and ML:
Enterprise adoption trends The word cloud in Figure 6.3 showcases the
The usage of AI and ML components has also versatile toolkit embraced by data scientists
experienced a remarkable surge in the enter- and AI practitioners. We observed a diverse
prise. Over the past year, the adoption of these spectrum of tools and frameworks gaining
tools within corporate environments has more prominence. These range from classical
than doubled (Figure 6.2), reflecting a signif- machine learning stalwarts like scikit-learn to
icant shift in how companies approach data the deep learning powerhouse PyTorch, with
science and machine learning. With the intro- HuggingFace transformers making a notewor-
duction of advanced AI models like ChatGPT, thy ascent, highlighting the increasing influence
organizations have increasingly recognized the of transformer-based models in contemporary
potential for enhancing decision-making, auto- AI endeavors.
mating tasks, and extracting valuable insights
from their data. This surge underscores a grow- In our comprehensive analysis of the software
ing awareness of the transformative power of supply chain, we delved into the rapid expan-
AI and ML, as businesses strive to leverage sion of components tailored to create or interact
with Large Language Models (LLMs). Notably,

56
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
TNEMPOLEVED
ERAWTFOS
NI
IA
:6
RETPAHC
FIGURE 6.4 our research unveiled the meteoric ascent of
LANGUAGE LEARNING MODEL GROWTH
libraries like Langchain, OpenAI, and Transform-
ers, signifying a surging interest in harnessing
the power of natural language understanding
and generation (Figure 6.4).
Equally fascinating was the finding that this
growth wasn’t confined solely to cutting-edge
generative AI components. Instead, it radiated
across the spectrum, encompassing well-es-
tablished frameworks such as scikit-learn, Ten-
sorFlow, and PyTorch (Figure 6.5). This diver-
sification underscores a strategic shift among
enterprises as they explore multiple avenues to
extract actionable insights and value from their
data. Hence, the evolving software supply chain
embraces both novel LLM-focused tools and
enduring traditional frameworks.
FIGURE 6.5 The growth of Large Language Models (LLMs)
TRADITIONAL MACHINE LEARNING GROWTH
extends far beyond the offerings of tech giants
like Google, Microsoft, and OpenAI, encompass-
ing a thriving and diverse ecosystem within the
enterprise sector (Figure 6.6). This ecosystem
includes solutions such as Cohere, streamlining
the integration of LLMs into enterprise products
and services, as well as the rising adoption of
Langchain and Langsmith for developing appli-
cations harnessing LLM capabilities. Notably, a
significant portion of these applications are built
upon open source LLM models.
This trend towards open source AI is further
underscored by the widespread adoption of
packages like Safetensors, enhancing the secu-
rity of model weight serialization, and CUDA

57
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
TNEMPOLEVED
ERAWTFOS
NI
IA
:6
RETPAHC
FIGURE 6.6
COMPONENTS WITH THE HIGHEST GROWTH RATE IN USAGE
GPU accelerators, facilitating faster model transparency and accountability in AI-driven However, there are notable drawbacks to con-
training and fine-tuning. Additionally, tools like decision-making. sider. One significant concern is cost, as enter-
Bitsandbytes provide quantization methods prises typically pay for each token sent and
for these expansive open source models, opti- Pros and cons of LLM-as-a-service received, which can accumulate quickly with
mizing inference speed and deployment on Large Language Models (LLMs) as a service extensive usage. Data privacy and security are
resource-efficient clusters. offer several distinct advantages to enterprises also paramount concerns, as enterprises may
and companies. Firstly, they accelerate devel- lack full transparency into how their data is being
While we have witnessed the remarkable output opment, simplifying the integration of advanced utilized by the service provider, raising potential
of these multi-billion parameter models, there language capabilities into applications through privacy issues. Moreover, vendor lock-in poses
remains a compelling case for interpretable straightforward API calls. Additionally, LLMs as a substantial risk, as reliance on a particular ser-
machine learning. This demand is captured by a service can deliver impressive performance vice leaves applications vulnerable to vendor
the growth of components like Explainerdash- benefits as the bulk of the processing is handled outages, deprecated features, or unforeseen
board, designed to elucidate the predictions server-side, offloading computational demands changes in model performance that may not
made by machine learning models, ensuring from local devices. align with the specific task at hand. Balancing
these pros and cons is essential when evaluating

58
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
TNEMPOLEVED
ERAWTFOS
NI
IA
:6
RETPAHC
the integration of LLMs as a service into an (cid:28)Embeddings: The selection of embeddings model must be carefully considered. For
enterprise’s workflow. As more companies turn plays a crucial role in fine-tuning the model’s instance, if a foundational model, such as Meta’s
towards open source AI solutions, they encoun- performance for specific tasks. LLaMA, is released under a non-permissive
ter familiar challenges related to the consump- license that restricts commercial use or imposes
tion of these open source components, which, in (cid:28)Licensing and Security: While navigating other conditions, deploying a fine-tuned version
this context, are the AI models themselves. these choices, data scientists must remain with an incorrect license can inadvertently vio-
vigilant about the licensing and security impli- late those terms. This situation can lead to legal
Data scientist burden cations. They must verify the model’s release liabilities and intellectual property disputes,
Data scientists and engineers tasked with license, ensuring it aligns with their intended even if the fine-tuned model itself is released
deploying open source Large Language Models usage, and be cautious of any potential licens- with a different license. It underscores the
(LLMs) shoulder a substantial burden, encom- ing conflicts. Additionally, they must assess importance of due diligence in understanding
passing numerous critical decisions: security risks, considering the possibility and adhering to the licensing terms of both
of uncensored or potentially inflammatory the foundational and derived models to avoid
(cid:28)Model Selection: With a vast repository of responses from the model and the implications unintended legal consequences. Furthermore,
over 337,237 models available, they must of deploying versions that can be jailbroken. it necessitates model fingerprinting for lineage
carefully select the most suitable one for their tracking to avoid these consequences.
specific application. Licensing risk
Deploying open source LLMs presents signif- As we have seen, LLMs are exceptionally profi-
(cid:28)Parameter Size: Choosing from a spectrum icant opportunities for natural language inter- cient at generating human-like text and working
ranging from hundreds of millions to hundreds action with company products and knowledge code based on the input provided to them. AI
of billions of parameters, they must determine bases. However, it is imperative to recognize models have gained these capabilities in part by
the ideal model size to balance computational the potential licensing risks associated with scraping publicly available data off of the Inter-
requirements and performance. these models. In many cases, developers may net without seeking express permission from
fine-tune these models to suit specific applica- copyright holders. Thus, this capability includes
(cid:28)Context Window: Defining the appropriate tions, but the licensing terms of the foundational the potential to generate content that closely
context window, representing the number of
tokens a model can take as input, is essential
to optimize the model’s responsiveness. FIGURE 6.7
NAVIGATING LICENSING RISKS IN THE DEPLOYMENT OF OPEN SOURCE LANGUAGE MODELS
(cid:28)Version Selection: Deciding which version
of the model to use—be it chat-oriented,
instruction-tuned, or code-tuned—requires
careful consideration to align with the
project’s objectives.

59
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT
TNEMPOLEVED
ERAWTFOS
NI
IA
:6
RETPAHC
While concerns about
resembles copyrighted content. When LLMs a significant shift in software development. Our
generate text that mirrors copyrighted material job displacement persist, analysis and survey highlight this growth as a
without adequate attribution or authorization, it critical milestone in our technological era. These
the prevailing sentiment
raises serious copyright infringement concerns. advancements offer transformative benefits,
is that AI aims to including increased productivity, advanced lan-
It is clear that in this instance, technological guage understanding, and diversified AI com-
enhance human abilities
innovation is ahead of legislation. As evi- ponents in engineering workstreams. However,
rather than replace
denced by the many court battles between along with these advantages, there are also
generative AI firms and contentcreators. them. challenges to be addressed.
Inevitably some of this stems from a misunder-
standing of the technology. In contrast, there imperative for enterprises to adopt a proactive Potential errors in AI-generated code, complex-
are also some egregious examples of the out- approach. Over-reliance on a single LLM-as-a- ities in model selection, security, and licensing
put of generative AI being a lot more indicative service, or single foundational model, such as require meticulous oversight. While concerns
of memorization compared to generalization, LLaMA, may prove detrimental in the face of about job displacement persist, the prevailing
such as when artists’ ghostly signatures appear regulatory challenges. Therefore, it is prudent to sentiment is that AI aims to enhance human abil-
in AI generatedartworks. explore viable alternatives to mitigate potential ities rather than replace them. Striking a balance
consequences. In the event of a hypothetical becomes crucial. We must harness AI’s unparal-
The copyright issues around the training sets scenario wherein copyright infringement is leled capabilities while remaining mindful of its
and outputs of generative AI aren’t going away attributed to the training data of models like challenges. Transparency, accountability, and
anytime soon. While the legal, and sometimes LLaMA, the critical question arises: Can you due diligence should be emphasized.
even philosophical, debates get resolved, some ensure that your applications remain compliant
companies have taken proactive steps, offering and unaffected by their utilization of LLaMA-de- As we journey forward, it is essential to ensure
legal protection for AI copyright infringement rived models? Preparing for such contingencies a balanced and responsible coexistence
challenges to customers using products such is essential in a world where every company is between AI tools and their human counterparts.
as Microsoft’s Copilot. Overall, the devil is in becoming a data and AI company. A critical aspect of this task extends beyond
the details, and the legal challenges are likely tool assessment and involves crafting a gov-
to help democratize the AI landscape as com- ernance strategy that assesses the impact of
Conclusion: A
panies will have to become more transparent adopting both proprietary and open-source
about the training datasets, model architectures, collaborative future libraries and models on your software supply
and the checks and balances in place designed chain.. By navigating the potential pitfalls and
to safeguard intellectual property. The rapid evolution and integration of AI, espe- maximizing the profound opportunities that AI
cially Large Language Models (LLMs) such as presents, we can shape a future that optimizes
In light of the potential risks associated with GitHub’s Copilot and ChatGPT, as well as their the benefits of this technology.
copyright infringement in generative AI, it is open source alternatives, have brought about

About the Analysis
Sonatype’s 9th annual State of the Software Supply Chain report blends a broad set of public and
proprietary data and analysis, including dependency update patterns for more than 400 billion
Maven Central downloads and thousands of open source projects, survey results from 621 engi-
neering professionals, and the assessment of hundreds of thousands key enterprise applications.
This year’s report also analyzed operational supply, demand and security trends associated with the
Java (Maven Central), JavaScript (npmjs), Python (PyPI), and .Net (nuget) ecosystems. The authors
have taken great care to present statistically significant sample sizes with regard to component ver-
sions, downloads, vulnerability counts, and other data surfaced in this year’s report.
60
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

Acknowledgements
Each year, the State of the Software Supply Chain report is a labor of love. It is produced to shed
light on the patterns and practices associated with open source, development and the evolution of
software supply chain management practices.
The report is made possible thanks to a tremendous effort put forth by many team members at
Sonatype, including Aaron Linskens, Alli VanKanegan, Ax Sharma, Brian Fox, Bruce Mayhew, Eddie
Knight, Elissa Walters, Ember DeBoer, Ilkka Turunen, Jeff Wayman, Juan Morales, Leina Sanchez,
Maury Cupitt, Mitchell Johnson, Nicole Lavella, Stephen Magill, PhD, Steve Poole, Tara Condon, Tif-
fany Jennings, Todd Baseden, Vlad Drobinin, PhD and Wayne Jackson.
We would also like to offer thanks for contributions, big and small, and for sharing perspectives with
our many colleagues across the DevOps and open source development community.
Another very special thank you goes out to Alli VanKanegan and Leina Sanchez, who created the
incredible design for this year’s report.
61
9TH ANNUAL STATE OF THE SOFTWARE SUPPLY CHAIN REPORT

Sonatype is the software supply chain management company. Recognized by globally renowned analysts as a leader in the industry, Sonatype
enables organizations to innovate faster in a highly competitive market. We allow engineers to develop software fearlessly and focus on building
products that power businesses. Sonatype researchers have analyzed more than 120 million open source components – 40x more than its com-
petitors – and the Sonatype platform has automatically blocked over 245,000 malicious components from entering developers’ code. Enabling
high-quality, secure software helps organizations meet their business needs and those of their customers and partners. More than 2,000 organi-
zations, including 70% of the Fortune 100 and 15 million software developers, rely on our tools and guidance to be ambitious, move fast and do it
securely. To learn more about Sonatype, please visit www.sonatype.com.
Headquarters European Office APAC Office Sonatype Inc.
8161 Maple Lawn Blvd, Suite 250 168 Shoreditch High Street 60 Martin Place Level 1 www.sonatype.com
Fulton, MD 20759 London E1 6HU Sydney, NSW 2000 Copyright 2023
USA • 1.877.866.2836 United Kingdom Australia All Rights Reserved.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-11-12", "model": "gemini-3.5-flash-lite"} -->
