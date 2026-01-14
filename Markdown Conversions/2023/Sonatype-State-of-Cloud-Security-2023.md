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
  - [Why is making good choices so hard?](#why-is-making-good-choices-so-hard)
  - [Modern Dependency Management Practices](#modern-dependency-management-practices)
  - [What makes an optimal open source component?](#what-makes-an-optimal-open-source-component)
  - [Understanding component upgrade urgency](#understanding-component-upgrade-urgency)
  - [Downloads by upgrade urgency](#downloads-by-upgrade-urgency)
  - [A ton of wasted time](#a-ton-of-wasted-time)
  - [The value of an artifact repository manager](#the-value-of-an-artifact-repository-manager)
  - [Global patterns of open source consumption behavior](#global-patterns-of-open-source-consumption-behavior)
- [CHAPTER 4: Software Supply Chain Maturity](#chapter-4-software-supply-chain-maturity)
  - [Software Supply Chain Maturity — Peer Insights](#software-supply-chain-maturity--peer-insights)
  - [How mature are today’s software supply chains?](#how-mature-are-todays-software-supply-chains)
  - [How have software supply chain management trends changed?](#how-have-software-supply-chain-management-trends-changed)
- [CHAPTER 5: Establishment and Expansion of Software Supply Chain Regulations and Standards](#chapter-5-establishment-and-expansion-of-software-supply-chain-regulations-and-standards)
  - [United States](#united-states)
  - [European Union](#european-union)
  - [Canada](#canada)
  - [Global partnerships](#global-partnerships)
  - [Are software supply chain regulations working?](#are-software-supply-chain-regulations-working)
  - [Navigating the policy frontier: Global cybersecurity regulations](#navigating-the-policy-frontier-global-cybersecurity-regulations)
- [CHAPTER 6: AI in Software Development](#chapter-6-ai-in-software-development)
  - [Sonatype’s risks & rewards of AI survey](#sonatypes-risks--rewards-of-ai-survey)
  - [The intersection of AI and software development](#the-intersection-of-ai-and-software-development)
  - [Navigating concern](#navigating-concern)
  - [AI’s open source toolkit: Components and models in focus](#ais-open-source-toolkit-components-and-models-in-focus)
  - [Conclusion: A collaborative future](#conclusion-a-collaborative-future)
- [About the Analysis](#about-the-analysis)
- [Acknowledgements](#acknowledgements)

---

## 9th Annual State of the Software Supply Chain Report

### State of the Software Supply Chain by the numbers

- 1 in 8 open source downloads have known risk
- 245,000 malicious packages discovered — 2X all previous years combined
- 18.6% of open source projects across Java and JavaScript that were maintained in 2022, are no longer maintained today
- 96% of vulnerable downloaded releases had a fixed version available
- 10 superior versions of components are typically available, for every nonoptimal component upgrade made
- 2X When paired with optimal upgrades, good data saves you twice as much time or nearly 1.5 months of time per application, per year when upgrading components.
- 135% increase in the adoption of AI and ML components within corporate environments, over the last year
- 67% of survey respondents feel confident that their applications do not rely on known vulnerable libraries, despite 10% of respondents reporting their organizations had security breaches due to open source vulnerabilities in the last 12 months

---

## CHAPTER 1

# Open Source Supply, Demand, and Security

"We are like dwarfs sitting on the shoulders of giants. We see more, and things that are more distant, than they did, not because our sight is superior or because we are taller than they, but because they raise us up, and by their great stature add to ours." - John of Salisbury

The progress we make is built upon the progress of those who came before us. This is nowhere more evident than in the adoption of open source. Nearly all software today relies on previous innovation distributed freely by experts.

For the 9th consecutive year, we track the growth of open source adoption across the top four major open source ecosystems, which account for four of the top five languages on GitHub and a 60% share of the most popular programming languages according to PYPL.

In past reports, we've estimated that up to 90% of the code we run in production is of open source origin. Therefore, the economics of open source are good indicators of trends and challenges in the wider software market.

Leveraging our continued monitoring, we present the combined statistics of each ecosystem in the table below.

### FIGURE 1.1
OPEN SOURCE ADOPTION AS PROJECTED FOR 2023

| Ecosystem | Total Projects | Total Project Versions | 2023 Annual Request Volume Estimate | YoY Project Growth | YoY Download Growth Estimate | Average Versions Released per Project |
|---|---|---|---|---|---|---|
| Java (Maven) | 557k | 12.2M | 1.0T | 28% | 29% | 22 |
| JavaScript (npm) | 2.5M | 37M | 2.6T² | 27% | 25% | 15 |
| Python (PyPI) | 475k | 4.8M | 261B³ | 28% | 18% | 10 |
| .NET (NuGet Gallery) | 367k | 6M | 162B⁴ | 28% | 31% | 17 |
| **Totals / Avgs** | **3.9M** | **60M** | **4T** | **28%** | **33%** | **15** |

* https://pypl.github.io/PYPL.html Accessed August 2023
* Figure estimated using npm download counts from January to August 2023 as queried from https://github.com/npm/registry/blob/master/docs/download-counts.md
* YoY growth estimated based on known PyPI downloads from January to August 2023 as queried from https://console.cloud.google.com/marketplace/product/gcp-public-data-pypi/
* YoY growth estimated based on known NuGet Gallery downloads from January to August 2023 as queried from https://www.nuget.org/stats

### FIGURE 1.2
OPEN SOURCE NEW PROJECT GROWTH RATE OVER THE PAST 4 YEARS

### Open source supply sees a resurgence

The supply side of open source indicates the pace and scale of innovation. More projects published annually mean more innovation.

New open source projects across monitored ecosystems have been published at a steady 15% average rate⁵ in recent years, a reduction from highs seen in 2019 and before.

### FIGURE 1.3
OPEN SOURCE PROJECTS AND VERSIONS GROWTH

This two-year slump is likely related to the COVID-19 pandemic and associated slowdown. While some studies suggest productivity increased in the U.S. during 2020-2023, a negative correlation emerges in open source production trends. Another study found productivity rates in information and communication technology declined towards 2022. Commercial activity, rather than people with spare time, might also explain this.

The data in 2023 shows the innovation slowdown is over. Each monitored ecosystem showed a consistent project growth rate, varying just 2% across all four to an average growth rate of 29% year-over-year.

Maven Central and NuGet are on track to exceed their 2020 growth rates. PyPi and npm, while growing, have not yet caught up to their original growth rates but are on an upward trend. Breakthroughs and interest in AI and its related tooling are fueling growth in these ecosystems.

Between 2022 and 2023, the number of available open source projects grew an average of 29%. The average open source project in 2023 has released 15 versions available for consumption, with specific ecosystem averages ranging from 10 to 22. This equates to 1-2 new versions every month, totaling 60 million combined releases across observed ecosystems.

### Open source consumption is decelerating

While supply is increasing, consumption isn't keeping pace. The rate of download growth in open source consumption has slowed over the past two years. In 2023, this trend continued with the average download growth rate at 33%, the same as last year. This is a stark comparison to the all-time high of 73% year-over-year growth in 2021. A slowdown in growth in the largest ecosystems is not surprising given their market saturation.

Despite this, both Maven and npm are estimated to reach over a trillion requests in 2023, with npm reaching a staggering 2.6 trillion requests, continuing a modest growth that surpasses PyPI's total request rate in 2022. These two ecosystems account for 90% of requests served, with the remaining two growing at an above-average pace.

### FIGURE 1.4
CUMULATIVE ESTIMATED REQUESTS PER ECOSYSTEM OVER 6 YEARS

### FIGURE 1.5
GROWTH RATE OF THE MONITORED OPEN SOURCE ECOSYSTEMS OVER 5 YEARS

### FIGURE 1.6
TOTAL OPEN SOURCE REQUESTS OVER 6 YEARS

Requests are the fundamental measure of an open source ecosystem's popularity and usage. Other factors, like the larger size and complexity of Java packages compared to JavaScript, may vary.

Investigating the rate of growth for requests can reveal information about the state of open source adoption and the growth of the software industry at large.

Figure 1.5 charts these individual growth rates over time and displays an average across all 4 ecosystems.

Download requests for all open source ecosystems are still growing, but for a third year in a row, the pace of growth is slowing down.

We can see a clear delineation between the stabilization of large ecosystems like Maven and npm, and continued accelerated growth in PyPI and NuGet.

Figure 1.6 charts the overall aggregate request growth across all ecosystems. It illustrates that although the pace of growth is slowing down, the absolute scale of growth continues to compound on previous years’ rates. The pace of open source adoption still shows no signs of stopping.

### 2023 BY THE NUMBERS

- **Java**: 1 trillion projected request volume, 25% YoY growth estimated
- **JavaScript**: 2.1 trillion projected request volume, 32% YoY growth estimated
- **Python**: 261 billion projected request volume, 31% YoY growth estimated
- **.NET**: 162 billion projected request volume, 43% YoY growth estimated

### Individual ecosystem analysis

#### Java (Maven)
Through the first 7 months of 2023, 512 billion Java components were requested from the Maven Central Repository, a significant jump compared to the 821 billion requests in 2022. Java continues to grow at a healthy pace, hitting an estimated 25% YoY request growth rate. If previous years are any indication, we may see a spike towards the end of the year.

#### JavaScript (npmjs)
npm is the juggernaut of open source registries, with an estimated download request count of over 2.6 trillion components. The growth of npm is the slowest of all monitored ecosystems, estimated at 18% YoY. Nevertheless, owing to npm’s substantial footprint, this translates to a staggering 400 billion requests, surpassing the combined total of requests served by PyPI and NuGet.

#### Python (PyPI)
Python continues to expand at a high pace, fueled by the language’s popularity and innovative uses, including AI. In 2023, PyPI served over 178 billion requests. This year, we estimate PyPI request volume will hit 261 billion packages, representing 31% YoY growth.

#### .NET (NuGet)
NuGet is the chosen ecosystem of the .NET family of languages and continues to serve engineers working with the growing set of Microsoft technologies. The rate of growth in NuGet is estimated to be the fastest amongst the cohort. Developers downloaded 113 billion NuGet packages in 2022, well above our estimate last year. In 2023, NuGet is estimated to serve 162 billion requests, representing 43% YoY growth.

### Open source software security concerns see no sign of slowing

In 2022, we reported a massive increase in malicious attacks on the software supply chain. Since our last report, this method of propagating security threats using trusted developer utilities and ecosystems has continued to evolve and flourish.

A troubling trend has emerged over the past few years: tailor-made packages designed to run a malicious payload on download without any developer interaction. This form of intrusion relies on developers not recognizing that build breakage from a fake package might indicate something nefarious has already happened on their system. We did a deep dive into types of malicious attacks in last year’s report.

### FIGURE 1.7
NEXT GENERATION SOFTWARE SUPPLY CHAIN ATTACKS (2019-2023)

In our YoY monitoring, at the time of writing in September 2023, we have logged 245,032 malicious packages, meaning in the last year, we’ve seen the number of malicious packages triple. Looking at it a different way, it also indicates that in one year alone, we’ve seen twice as many supply chain attacks as the cumulative numbers in previous years.

This pace of growth is astonishing. It signals the role of the supply chain as one of the fastest growing vectors for adversaries to execute malicious code. Furthermore, we have seen an increase in nation-state actors leveraging these vectors.

This is alarming news. Even though many open source ecosystems have implemented new security policies, such as mandatory MFA, they usually only address protecting existing open source publishers from attack. Often, packages containing malicious code are treated similarly to packages with new security vulnerabilities and are taken down entirely based on a volunteer effort following a vulnerability removal process, which is not appropriate when the code is designed to be malicious from the start. This approach can lead to malicious packages remaining up longer than necessary, leaving developers at risk.

### Notable malicious packages and vulnerabilities

As we continue to document an overall rise in malicious attacks on open source ecosystems, the monitored 2022-2023 period has also seen more professional criminal campaigns emerge. The software supply chain lends itself well to the cybercriminal ecosystem—either as an initial access vector to Initial Access brokers or even as a means of distributing initial access malware for Advanced Persistent Threat groups. Here are several examples we’ve seen this year:

#### Lazarus created PyPI package ‘VMConnect’ imitates VMware vSphere connector
In August 2023, Sonatype discovered a malicious Python package, ‘VMConnect,’ on PyPI, which mimics a legitimate VMware module. This is part of a wider cyber campaign called “PaperPin,” and is widely thought to originate from the Lazarus Group, a North Korean state-affiliated organization. The packages aim to download further malicious payloads from attacker-controlled URLs. The focus on VMware, a widely-used virtualization platform, is particularly concerning, as a successful compromise could have far-reaching implications for enterprise networks and is widely attractive to state-affiliated actors. Read our full deep dive.

#### ChatGPT histories were uncovered due to a vulnerability in Redis component used by OpenAI
In March of 2023, ChatGPT users experienced a data leak where chat histories displayed other people’s queries. OpenAI identified the issue as a race condition vulnerability in an open source component called Redis, which they use for caching user data. This flaw made sensitive data of about 1.2% of ChatGPT Plus subscribers accessible to others. The vulnerability was exacerbated by a recent server change that increased the probability of the race condition occurring. The issue underscores the importance of even rarely occurring vulnerabilities, especially in widely-used components like Redis, given their potential to cause widespread disruption and data exposure. Read our full analysis.

#### PyTorch namespace confusion attack targets utilities aimed at AI developers
In the past couple of holiday seasons, we’ve seen some big supply chain attacks, including one on PyTorch, a popular machine learning framework. The attackers used a tactic known as namespace confusion to specifically go after the experimental “nightly” build of PyTorch. They managed to steal sensitive data, signaling that hackers are increasingly setting their sights on AI and machine learning tools. These tools are becoming more critical in various sectors, making them attractive targets. While only the experimental build was hit, the incident serves as a wake-up call for better security in the booming AI field. Read our full analysis.

#### A timeline of attacks
We have continued to curate a timeline of known malicious packages and malware campaigns. This interactive timeline summarizes notable supply chain incidents, next-gen attacks, and other incidents propagated using the software supply chain.

### Differentiating software vulnerabilities and malware

Up until now, we’ve been talking about malware and malicious attacks on the software supply chain—or perhaps better stated as malware propagated using the open source supply chain. In this next section, we’re going to discuss software vulnerabilities. While the two concepts are related, they are very distinct, so we’d like to quickly define the difference between a vulnerability and malware.

#### Software vulnerability: A flaw in the code
A software vulnerability is akin to a flaw in code, much like a faulty lock on a door. However, unlike malware, vulnerabilities are not intentional. Instead, they represent weaknesses in software components or projects.

Similar to how a faulty lock compromises the security of a building by allowing unauthorized access, a software vulnerability creates a gap in the software’s security perimeter. This gap becomes an entry point for intruders to exploit, gaining unapproved access to the system, application, or component.

#### Malware: Malicious intent in open source
Malware, short for “malicious software,” poses a significant threat to open source software ecosystems. It encompasses a wide range of malicious programs, such as viruses, worms, trojans, ransomware, spyware, and adware, all designed to gain unauthorized access to information or systems.

With its various forms, malware’s primary purpose is to steal data, install harmful software, gain control of a network, or compromise software or hardware. Threat actors employ diverse distribution methods, such as infected email attachments, malicious websites, or compromised software downloads.

### Consumption behavior contributing to security concerns

Our report last year revealed a startling statistic—nearly 96% of component downloads with known vulnerabilities could be avoided as a better, fixed version is already available. This illustrates a clear need for organizations to pay closer attention to what versions they are adopting.

### FIGURE 1.8
SOFTWARE SUPPLY CHAIN ATTACKS, DEC 2021–AUGUST 2023

### FIGURE 1.9
PERCENTAGE OF COMPONENTS WITH KNOWN VULNERABILITIES SERVED FROM MAVEN CENTRAL

### FIGURE 1.10
2022 VULNERABLE DOWNLOADS BY SEVERITY

### FIGURE 1.11
NVD — KNOWN VULNERABILITY SEVERITY

There is widening evidence that whatever the standard practice for avoiding vulnerable components today, the controls are not having the effect needed to reduce the attack surface. For example, as of September 2023, downloads vulnerable to the infamous Log4Shell vulnerability still account for nearly a quarter of all net new downloads of Log4j. It should be highlighted that almost two years after the initial finding of this vulnerability, we’re seeing this pace continue every week—that a quarter of all downloads are of the vulnerable version of Log4j. This is only part of the story. The reality is, nearly 1/3 of all Log4j downloads, ever, are of the vulnerable version.

As we discussed last year, the numbers for other critical vulnerabilities that have not received as much widespread media attention are even more depressing.

This warrants concern and calls for behavioral adaptation at organizations because critical vulnerabilities are widely exploited by bad actors, even at the state level. For example, Log4Shell has topped CISA/NSA charts for active state-sponsored exploitation for well over a year now. This is also echoed in the OpenSSF’s recently released Consumption Manifesto, which calls for organizations to take responsibility for the open source they use, how it is consumed, and how they manage the risk associated with that consumption.

According to a joint consortium of national operators including CISA, NSA, NCSC-UK and others, attackers are exploiting older well-known vulnerabilities much more frequently than new zero-day vulnerabilities. This is extremely important to understand. While we should of course worry about zero-days, we also know that 96% of vulnerable open source downloads have a non-vulnerable fix available. Those 96% need to be addressed.

For this year’s report, we’ve taken a closer look at how vulnerabilities are consumed from Maven Central, with a special focus on what sort of geographic variance might exist.

#### Vulnerable components consumed
Let’s start off by looking at the top level. In 2022 we saw 12% of downloads served by Maven Central⁶, contained at least one known security vulnerability.

This number is important when considering that the easiest way to reduce risk of a supply chain incident caused by a vulnerability is to simply choose a better, non-vulnerable version of a component.⁷ There is some improvement in these numbers; the number of vulnerable downloads in 2021 was 14%—and the number to date in 2023 sits at around 10%.

⁶ Countries and regions with over 100,000 annual requests
⁷ A limitation in this report is that the numbers reported are of security vulnerabilities known as of August 2023, even when inspecting retrospectively. The amount of vulnerabilities known at the time of download might have been lower, which might partially explain the improvement over time.

However, when investigating the downloads that contained a vulnerability in 2022, it emerges well over a third of the components consumed that had known vulnerabilities were Critical⁸ in severity—and a further 30.5% had a High Severity rating.

This trend holds true nearly universally across all regions—suggesting that component consumption is largely an unmanaged decision today. This is in contrast to the number of known critical vulnerabilities in the National Vulnerability Database—with over double the amount of criticals consumed over the spread of known vulnerabilities.

The increase of critically vulnerable components being consumed could be due to the fact that these vulnerabilities are found and reported primarily in more popular and widely-adopted open source software. Popularity begets more attention from good and bad actors, resulting in increased likelihood of a critical issue being present. It’s also worth noting that these more popular components have an official disclosure process to communicate through. Meaning, on average, these critical vulnerabilities should be the ones that are most noticed. But, as we’ve seen with the vulnerable version of Log4j, “knowing” is only half the battle. Organizations have to care, and they have to have an automated way to address this issue.

### FIGURE 1.12
AVERAGE VULNERABILITIES BY COUNTRY WITH OVER 1 BILLION DOWNLOAD VOLUME

### A global view of vulnerable open source downloads

Software development has evolved into one of the most globally influential industries, shaping various sectors and regions in unique ways. However, not all regions share the same level of emphasis on software development. To gain insight into how the trends we’ve explored thus far manifest on a global scale, we conducted an analysis that looks at open source vulnerability consumption, by country.

Our study focused on countries that collectively downloaded over 100 million open source components from Maven Central in the past year. By scrutinizing the percentage of vulnerabilities associated with the software downloaded in each region, we start to gain insights into how different parts of the world manage their software supply chains.

In Figure 1.12, we delineate those that have stronger management programs, from those who don’t, by plotting the percentage of vulnerabilities, against the average number of vulnerable downloads (approximately 12%)—and apply a ranking based on how countries compare to that average. But it’s important to consider the context and one of the most important figures to come out of Sonatype’s research: 96% of known vulnerabilities downloaded from Maven Central have a non-vulnerable version available.

The countries isolated above are 25 of the largest consumers of open source software in the world. Even at the low end of our criteria, around a 100 million downloads, 9.5% of those downloads are vulnerable components. When you consider juggernauts of open source consumption like the United States, the EU (collectively), and China, tens of billions of vulnerabilities have entered into the supply chains that produce the software we all use and our governments run on.

While we’re only scratching the surface with this regional view of vulnerable downloads, you can see a deeper dive into open source consumption patterns within specific economic regions in Chapter 3 of this report where we further unravel the intricacies of dependency management on a global scale. We also summarize the role regulations are having on the industry in Chapter 5.

---

## CHAPTER 2

# Open Source Security Practices

In 2020 the OpenSSF project started collecting information on the software security practices employed by open source projects. This substantially increased transparency of open source development practices by centrally tracking the usage of commonly accepted best practices. In a previous version of this report, we analyzed the extent to which higher scores on these checks are associated with better security outcomes and found them to be highly predictive of vulnerability status. In this year’s report, we delve into the state of adoption of Scorecard best practices overall and also by ecosystem (focusing on Java and JavaScript). We look at checks today as well as over time, looking back at the prior year to see both how community practices have evolved and how the checks themselves have evolved over time.

### The state of scorecard check scores

In last year’s report, we conducted an analysis of the connection between scorecard checks and known vulnerabilities. One outcome of this analysis was information on which checks are most closely associated with better vulnerability status. Figure 2.2 summarizes this information.

#### THE CHECKS
Our dataset consists of scorecard checks from 2022-06-27 and 2023-07-03 retrieved from the Scorecard BigQuery database. Each check is scored from 0 to 10. If the check fails or there is lack of evidence for a check, the Scorecard project assigns it a score of -1. We mapped these -1 values to 0 for our analysis.

- **BINARY ARTIFACTS**: Checks whether binary artifacts are checked into the repository, reducing the score if binary artifacts are found.
- **BRANCH PROTECTION**: Checks whether the project uses branch protection on its default and release branches to prevent maintainers from circumventing workﬂows like CI tests or code review when pushing changes.
- **CII-BEST PRACTICES**: Checks whether a project has obtained an OpenSSF (formerly CII) Best Practices Badge.
- **CODE REVIEW**: Checks whether recent code changes have been peer reviewed before being merged.
- **DANGEROUS WORKFLOW**: Checks whether the project avoids dangerous coding patterns in GitHub Action workﬂows.
- **DEPENDENCY UPDATE TOOL**: Checks whether the project is using tools to help update its dependencies.
- **FUZZING**: Checks whether the project is using fuzzing tools.
- **LICENSE**: Checks that the project includes a license ﬁle.
- **MAINTAINED**: Scores the project based on the amount of commit and issue tracking activity it has had over the last 90 days.
- **PACKAGING**: Checks whether the project builds and publishes official packages from the CI/CD pipeline.
- **PINNED DEPENDENCIES**: Checks whether project dependencies (including dependencies for GitHub Actions and Docker ﬁles) are pinned to speciﬁc versions.
- **SECURITY POLICY**: Checks that the project includes a security policy.
- **SIGNED RELEASES**: Checks that the project cryptographically signs releases.
- **TOKEN PERMISSION**: Evaluates whether the project’s automated workﬂow tokens follow the principle of least privilege.
- **VULNERABILITIES**: Checks that the project and its dependencies have no open, unﬁxed vulnerabilities. Projects score 10 for no vulnerabilities and 1 point is deducted for each open vulnerability, down to a minimum score of 0.
- **VULNERABLE**: A binary version of Vulnerabilities that we added to the dataset. A project is vulnerable if its Vulnerabilities score is less than 10.

### FIGURE 2.1
ELEMENTS MOST USEFUL FOR IDENTIFYING VULNERABLE PROJECTS

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

Java projects also score 10x higher on Fuzzing, though very few projects in either ecosystem take advantage of fuzzing technology. Rates of vulnerability are comparable, with 15% of Java projects and 16% of JavaScript projects having unpatched vulnerabilities at the time of scan. Note that this is a measure of whether there are vulnerabilities that apply to the development branch of a project. This does not indicate whether the latest release of the project has a vulnerability, nor whether the recorded vulnerabilities will persist into the next release.

### FIGURE 2.2
SCORECARD CHECK AVERAGES, ALL PROJECTS

### FIGURE 2.3
SCORECARD CHECK AVERAGES, JAVA VS, JAVASCRIPT

### FIGURE 2.4
SCORECARD CHECK AVERAGES, MAINTAINED

### The Importance of Maintenance

The figure above shows how the average scores change when we focus on maintained projects only (projects with a Maintained score greater than zero). There are several notable differences. Maintained projects are:

- 5.9x higher on SAST
- 5.4x higher on Signed Releases
- 5.1x higher on Dependency Update Tool
- 3.6x higher on Code Review
- 3.8x higher on Branch Protection

Maintained projects also score better on Vulnerabilities and have slightly lower rates of vulnerability.

The fact that 18.6% of projects stopped being maintained in the last year highlights the need to not only choose good dependencies, but monitor those dependencies for changes in their quality.

### Year-Over-Year Differences

We also looked at the data from one year ago to see how Scorecard practices have changed. Surprisingly, we find that there has not been a steady improvement in scorecard scores. Instead, we see decreases in several key metrics. In particular, the number of maintained projects has decreased overall and also within each ecosystem. Overall, there are 24,104 projects that were maintained one year ago, but no longer qualify as maintained. This represents 18.6% of the maintained projects. Put another way, if you picked a random maintained project in 2022, there would be a 18.6% chance that this project is no longer maintained one year later.

At the same time these ~24k projects slipped out of the “maintained” category, there were 12,806 newly “maintained” projects (projects that are maintained now but did not qualify as maintained in 2022). This resulted in an overall decrease of 11,298 in the number of maintained projects. Of the projects that have become unmaintained over the last year, 1,285 were in the Maven Central (Java) ecosystem and 9,626 were in NPM (JavaScript). This decrease is not necessarily a bad thing – it could simply reflect consolidation, with maintainers focusing on a smaller set of projects that have “stood the test of time”.

Overall, these changes highlight the importance of tracking the health of dependencies over time. Just as new projects are constantly being created, projects are also constantly reaching end of life status. Identifying these changes is an important part of maintaining a healthy set of application dependencies.

We have also seen an overall decrease in the amount of code review. The number of projects that had any Code Review decreased by over 15%. The decline was slightly less for Java (~11%) than for JavaScript (~17%). Even when just looking at maintained projects, there was a decrease of 8.6% in rates of code review. Comparing trends in scorecard checks over time is complicated by the fact that the OpenSSF Scorecard team does periodically change the checks in ways that can affect scoring. However, we reviewed the changes made to the code review check and, on aggregate, they appear to make the check easier to pass (e.g. by treating a PR merged by someone other than the contributor as a review). If this data indeed reflects a decline in the amount of code review occurring in otherwise well-maintained projects then this is a worrying trend. We recommend ensuring that any open source libraries critical to business applications are practicing code review on every pull request to the main branch.

### Conclusion

Overall, these results provide guidance for open source users when choosing dependencies and important areas of focus for open source advocates and maintainers. The value of choosing well-maintained projects stands