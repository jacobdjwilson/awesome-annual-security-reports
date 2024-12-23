# The 7th Annual Report on Global Open Source Software Development
## Table of Contents
- [Introduction](#introduction)
- [CHAPTER 1 Open Source Supply, Demand, and Security](#chapter-1-open-source-supply-demand-and-security)
    - [Open Source Supply](#open-source-supply)
    - [Open Source Demand](#open-source-demand)
    - [Open Source Security](#open-source-security)
    - [Software Supply Chain Attacks Increase 650%](#software-supply-chain-attacks-increase-650)
    - [Front Page News](#front-page-news)
- [CHAPTER 2 Understanding Exemplary and Non-Exemplary Open Source Projects](#chapter-2-understanding-exemplary-and-non-exemplary-open-source-projects)
    - [Open Source Project Quality Metrics](#open-source-project-quality-metrics)
    - [Quality Metric Comparison](#quality-metric-comparison)
    - [Research Findings](#research-findings)
    - [Guidance for Open Source Project Owners and Contributors](#guidance-for-open-source-project-owners-and-contributors)
    - [Guidance for Enterprise Development Teams](#guidance-for-enterprise-development-teams)
- [CHAPTER 3 Peer Practices Associated With Micro and Macro Dependency Management](#chapter-3-peer-practices-associated-with-micro-and-macro-dependency-management)
    - [To Update or Not: An Empirical View of Micro Dependency Management](#to-update-or-not-an-empirical-view-of-micro-dependency-management)
    - [Selecting the Best Projects: Reflections on Macro Architectural Decisions](#selecting-the-best-projects-reflections-on-macro-architectural-decisions)
    - [Conclusions and Practical Recommendations](#conclusions-and-practical-recommendations)
- [CHAPTER 4 Software Supply Chain Maturity](#chapter-4-software-supply-chain-maturity)
    - [How Mature are Today’s Software Supply Chains?](#how-mature-are-todays-software-supply-chains)
    - [Reality vs. Perception on Software Supply Chain Maturity](#reality-vs-perception-on-software-supply-chain-maturity)
- [CHAPTER 5 Emergence of Software Supply Chain Regulation and Standards](#chapter-5-emergence-of-software-supply-chain-regulation-and-standards)
    - [What’s Happening in the United States?](#whats-happening-in-the-united-states)
    - [What’s Happening in the United Kingdom?](#whats-happening-in-the-united-kingdom)
    - [What’s Happening in Germany?](#whats-happening-in-germany)
    - [What’s Happening in the European Union?](#whats-happening-in-the-european-union)
    - [What’s Happening Globally?](#whats-happening-globally)
- [About the Analysis](#about-the-analysis)
- [Acknowledgments](#acknowledgments)

# Introduction
In 1849, French writer Jean-Baptiste Alphonse Karr famously said, “the more things change, the more they stay the same.” While he obviously wasn’t talking about open source software (OSS), digital supply chains, or application innovation during a global pandemic, he might as well have been. Indeed, in the year since we last published our State of the Software Supply Chain research, so much has changed in the world of software development, and yet, so much has stayed the same.

My oh my, how things have changed. COVID-19 fundamentally transformed how people live and work, how companies interact with customers, how customers shop and buy, and how physical and digital supply chains function. As the economic importance of digital innovation accelerated during the global pandemic, so too did the number of cyber-attacks aimed at exploiting software supply chains.

And yet, much has stayed the same. Top-performing companies like Apple, Goldman Sachs, and Amazon — and more recently, Zoom, Peloton, and Wayfair have mastered three key competitive advantages: knowing how to use open source and third-party innovation at scale, integrating security and risk controls into multiple phases of the software supply chain, and releasing higher quality code faster than their competitors.

Now in its seventh year, Sonatype’s 2021 State of the Software Supply Chain Report blends a broad set of public and proprietary data to reveal important findings.

Together with our partners, we are proud to share this research. We hope that you find it valuable.

Open source supply is accelerating. The top four open source ecosystems released a combined 6,302,733 new versions and introduced 723,570 brand new projects. Collectively, these communities now contain a combined 37,451,682 different versions of components, representing a 20% year over year (YoY) growth in global supply of open source.

Open source demand is exploding. In 2021 developers around the world will request more than 2.2 trillion open source packages from these same four ecosystems, representing a 73% YoY growth in developer downloads of open source components. Despite the growing volume of downloads, the percentage of available components utilized in production applications is shockingly low.

Open source vulnerabilities are most pervasive in popular projects. 29% of popular projects contain at least one known security vulnerability. Conversely, only 6.5% of non-popular projects do so. This dichotomy suggests that the vast majority of security research (blackhat and whitehat) is focused on finding and reporting vulnerabilities in projects that are most commonly utilized.

![Image description: A graphic showing statistics about open source software. It includes the following text: 37 Million OSS component versions now available, 6 Million new versions introduced in past year, 73% YoY growth of component downloads, 29% of popular projects contain known vulnerabilities, but only 6.5% of non-popular projects contain known vulnerabilities.]

Some projects are better than others. To avoid stale dependencies and minimize security risks associated with third-party open source, software engineering teams should actively embrace projects that consistently demonstrate low mean time to update (MTTU) values and high OpenSSF Criticality scores.

Dependency management practices vary widely among teams. On average, enterprise Java applications utilize 10% of the components that are available for download in the Maven Central Repository. However commercial engineering teams actively update only 25% of components utilized. Such efforts are highly variable and frequently suboptimal, yet there is wisdom in the crowd that can be distilled. Newer versions of projects are generally better, but not always best.

Standardizing architectural guidance is a path to huge efficiency gains. Intelligent automation that standardizes engineering teams on exemplary open source projects could remove 1.6M hours and $240M of real world waste spread across our sample of 100,0001 production applications. Extrapolated out to the entire software industry, the associated savings would be billions.

Supply chain attacks are increasing exponentially. In 2021 the world witnessed a 650% increase in software supply chain attacks, aimed at exploiting weaknesses in upstream open source ecosystems. For perspective, the same statistic was 430% in the 2020 version of the report.

![Image description: A graphic showing statistics about open source software. It includes the following text: 650% YoY increase in cyber-attacks aimed at open source suppliers, Only 25% of utilized components are updated actively, Intelligent automation could save companies $192,000 per year, 702 IT professionals surveyed.]

There is a disconnect between subjective survey feedback and objective data. People believe they are doing a good job remediating defective components and indicate that they understand where risk resides. Objectively, research shows development teams lack structured guidance and frequently make suboptimal decisions with respect to software supply chain management.

# CHAPTER 1
## Open Source Supply, Demand, and Security
The universal desire for faster innovation fundamentally requires that software developers reuse code frequently and efficiently. This, in turn, has led to a critical dependence on OSS libraries borrowed from third-party ecosystems. These third-party components and packages represent the building blocks of modern software development. But, what does open source supply look like? What are the demand dynamics? What is the relative quality and security of third-party code borrowed from open source suppliers?

Figure 1.1 summarizes statistics on supply, demand, usage, and security for the Java, JavaScript, Python, and .NET ecosystems. There are an order of magnitude more project versions than there are projects, with the average project having published eight to 12 versions, depending on the ecosystem. Older projects can have tens, or even hundreds of versions. Furthermore, a minefield of known (and unknown) security risks lurk within the 37 million available project versions. Such risk is far more prominent in popular projects.

### Open Source Supply
The global supply of open source libraries continues to grow exponentially, fueled by new versions of existing projects constantly being released, and by the creation of altogether new projects. Currently, the top four open source ecosystems contain a combined 37,451,682 components and packages. These same communities released a combined 6,302,733 new versions of components / packages over the past year and have introduced 723,570 brand new projects in support of 27 million developers worldwide.

#### Java
As of July 31, 2021, there are 430,995 unique projects (group-artifacts) available in the Maven Central Repository, up 13% from last year. This public catalog of Java components now offers developers a total of 7.3 million different versions (group-artifact-versions) of projects to choose from, up 19% from last year.

In the past year alone, project owners released more than 1.1 million new versions of existing components, and introduced 136,000 brand new projects to service and support approximately eight million Java developers.

![Image description: A table titled "2021 SOFTWARE SUPPLY CHAIN STATISTICS" with columns for ECOSYSTEM, TOTAL PROJECTS, TOTAL PROJECT VERSIONS, ANNUAL DOWNLOAD VOLUME, YOY DOWNLOAD GROWTH, ECOSYSTEM PROJECT UTILIZATION, VULN DENSITY FOR UTILIZED VERSIONS 10% Most Popular, and VULN DENSITY FOR UTILIZED VERSIONS 90% Least Popular. The table includes data for Java, JavaScript, Python, .NET, and Totals/Averages.]

> A minefield of known (and unknown) security risks lurk within the 37 million available project versions.

#### JavaScript
As of July 31, 2021 there were 1,864,696 JavaScript packages available in the npm repository, up 16% from last year. This public catalog of JavaScript packages offers developers a total of 21,320,796 different versions. In the past year alone, npm project owners released 3,797,675 new versions of packages, and introduced 405,243 brand new projects to service and support approximately 12 million JavaScript developers.

#### Python
336,402 packages are available in the Python Package Index (PyPI), up 18% from last year. This public catalog of Python packages offers developers a total of 3,035,265 different versions. In the past year alone, python project owners released 556,327 new versions of packages, and introduced 93,032 brand new projects to service and support approximately eight million Python developers.

#### .NET
338,423 open source projects are available in the NuGet gallery, up 14% from last year. This public catalog of .net packages offers developers a total of 5,698,716 different versions. In the past year alone, the NuGet gallery released 756,444 new versions of packages, and introduced 87,268 brand new projects.

![Image description: A bar graph titled "AVAILABLE SUPPLY OF OPEN SOURCE, 2021" showing the number of projects and project versions for Java, JavaScript, Python, and .NET.]

### Open Source Demand
In 2021, developers around the world will borrow more than 2.2 trillion open source packages or components from third-party ecosystems for two simple reasons: it makes life easier for software developers and it accelerates the pace of innovation.

#### Java
Through the first seven months of 2021, 267 billion Java components were downloaded from the Maven Central Repository. At this rate, the volume for 2021 is projected to be over 457 billion, a 71% YoY increase.

#### JavaScript
In 2020, JavaScript developers requested more than one trillion packages from npmjs. The volume for 2021 is expected to reach 1.5 trillion, a 50% YoY increase.

#### Python
In 2020, Python developers downloaded 66 billion packages from PyPi. For the full year of 2021, PyPi download volume is expected to be 127 billion packages. YoY growth of PyPi download volume is estimated to be 92%.

#### .NET
.NET developers were also eager to consume OSS packages over the past year. Developers downloaded 44 billion NuGet packages in 2020. In 2021 developers will download more than 78 billion packages, representing a 78% YoY growth.

![Image description: A bar graph titled "INCREASE IN DOWNLOADS Year Over Year 2020 – 2021" showing the percentage increase in downloads for Java, JavaScript, Python, and .NET.]

![Image description: A bar graph titled "ANNUAL DOWNLOAD VOLUMES, 2021" showing the download volumes in billions for Java, JavaScript, Python, and .NET.]

### Open Source Security
The amount of third-party code flowing through software supply chains is massive. But is it secure? Are certain open source ecosystems more or less risky? Are certain projects safer than others? Are popular projects more or less likely to have known vulnerabilities? Here’s what the data reveals.

When examining the top 10% of the most popular Java, JavaScript, Python, and .NET projects, 29% of them contain at least one known security vulnerability. Conversely, when examining the remaining 90% of less popular projects, only 6.5% of them contain known vulnerabilities. These findings indicate that the vast majority of security research (blackhat and whitehat) is focused on finding and reporting vulnerabilities in projects that are most commonly utilized.

In addition to studying the difference in vulnerability density between popular and non popular open source projects, we also present below the aggregate vulnerability density for each of the four ecosystems.

![Image description: A scatter plot titled "VULNERABLE RELEASE DENSITY VS. POPULARITY" showing the relationship between project popularity and vulnerability density.]

#### Java (Maven)
As of July 31, 2021, 612,988 (8.4%) of all component versions housed in Maven Central contain at least one known security vulnerability. To exclude low level security issues, we determined severity based on the Common Vulnerability Scoring System (CVSS), for medium (5), high (7), and critical (9), Of the issues identified:
- 356,808 (4.9%) had a CVSS of 9 or higher
- 488,826 (6.7%) had a CVSS of 7 or higher
- 598,364 (8.2%) had a CVSS of 5 or higher

For the past eight years, Sonatype has also analyzed the patterns and practices associated with Java components being downloaded from Maven Central. In 2020 and through the first seven months of 2021, 8% of the downloads had at least one known vulnerability.

#### JavaScript (npm)
As of July 31, 2021, 459,576 (2.2%) project versions housed in npm contain at least one known security vulnerability. Of the issues identified:
- 250,002 (1.2%) had a CVSS of 9 or higher
- 350,737 (1.6%) had a CVSS of 7 or higher
- 450,734 (2.1%) had a CVSS of 5 or higher

Notably, however, of the nearly 1.9 million JavaScript top level projects available, only 2% of those are being used with any regularity.

#### Python (pypi)
As of July 31, 2021, 147,994 (0.5%) package versions housed in the PyPI repository contained at least one known security vulnerability. Of the issues identified:
- 81,731 (.4%) had a CVSS of 9 or higher
- 111,970 (.4%) had a CVSS of 7 or higher
- 143,902 (.5%) had a CVSS of 5 or higher

#### .NET (Nuget)
As of July 31, 2021, 112,031 (2%) of package versions housed in the NuGet Gallery contained at least one known security vulnerability. Of the issues identified:
- 27,288 (.5%) had a CVSS of 9 or higher
- 99,096 (1.7%) had a CVSS of 7 or higher
- 110,764 (1.9%) had a CVSS of 5 or higher

### Software Supply Chain Attacks Increase 650%
Members of the world’s open source community are facing a novel and rapidly expanding threat that has nothing to do with passive adversaries exploiting known vulnerabilities in the wild — and everything to do with aggressive attackers implanting malware directly into open source projects to infiltrate the commercial supply chain.

Legacy software supply chain “exploits," such as the now infamous 2017 Struts incident at Equifax, prey on publicly disclosed open source vulnerabilities that are left unpatched in the wild. Next-generation software supply chain “attacks” are far more sinister, however, because bad actors are no longer waiting for public vulnerability disclosures to pursue an exploit. Instead, they are taking the initiative and injecting new vulnerabilities into open source projects that feed the global supply chain, and then exploiting those vulnerabilities before they are discovered. By shifting their attacks “upstream," bad actors can gain leverage and the crucial benefit of time that that enables malware to propagate throughout the supply chain, enabling far more scalable attacks on “downstream” users.

According to security researchers at the University of Bonn, SAP Labs France, and Fraunhofer FKIE, “From an attacker’s point of view, [large scale, public internet-based] package repositories represent a reliable and scalable malware distribution channel. Thus far, Node.js (npm) and Python (PyPI) repositories have been the primary targets of malicious packages, supposedly due to the fact that malicious code can be easily triggered during package installation."[^4]

From February 2015 to June 2019, 216 software supply chain attacks were recorded. Then, from July 2019 to May 2020, the number of attacks increased to 929 attacks. However, in the past year, such attacks represented a 650% YoY increase (see Figure 1.6 above).

![Image description: A bar graph titled "NEXT GENERATION SOFTWARE SUPPLY CHAIN ATTACKS (2015 – 2021) Dependency Confusion, Typosquatting, and Malicious Code Injection" showing the number of attacks from 2015 to 2021.]

#### Dependency Confusion
The most common type of attack in 2021 has been Dependency Confusion (aka namespace confusion). The novel, highly targeted, attack vector allows unwanted or malicious code to be introduced downstream automatically, without relying on typosquatting or brandjacking techniques. The technique involves a bad actor determining the names of proprietary (inner source) packages utilized by a company’s production application. Equipped with this information, the bad actor then publishes a malicious package using the exact same name, and a newer semantic version, to a public repository, like npmjs, that does not regulate namespace identity. At this point, certain pipeline build tools will automatically fetch the newer, intentionally malicious version. In the past year, namespace confusion has alone accounted for instances of attempted or confirmed supply chain attacks.[^5] This attack vector relies on the long established convention in some programming languages to fetch the “LATEST” version of any package.

#### Typosquatting
Typosquatting was the second most common technique over the past year. This indirect attack vector preys on developers making otherwise innocent typos when searching for popular components. For example, if a developer accidentally types “electorn” when their intention is to source “electron," they might accidentally install a malicious component of a similar name (see electorn, September 2020).

#### Malicious Source Code Injections
Malicious Source Code Injections are another type of attack that have been less prevalent in the past year compared to previous years. Such attacks involve injecting malicious source code directly into an open source project’s repository, and have been conducted in various ways, including:
- stealing credentials from a project maintainer (see rest-client, 8/19)
- releasing new versions of a project to a public repository (see bootstrap-sass, 4/19)
- contributing pull requests to a project that includes malicious code (see event-stream, 11/18)
- tampering with open source developer tools that inject malicious code into downstream applications (see Octopus Scanner, 5/20).

With code injections, it is likely that no one knows the malware is there, except for the person that planted it. This approach allows adversaries to surreptitiously “set traps” upstream, and then carry out attacks downstream once the vulnerability has moved through the supply chain and into the code bases of thousands of companies.

### Front Page News
In the past year, numerous high-profile and prominent attacks demonstrated how supply chain threats affect not only third-party application level libraries and tools, but also first-party source code. The European Union’s Cybersecurity Agency (ENISA) predicts these types of supply chain attacks are expected to increase 4x in 2021.

#### SolarWinds — December 2020
The massive SolarWinds Orion attack publicized in December 2020 marked the most notable supply chain attack of the past year. The attack started with threat actors gaining access to SolarWinds’ internal development tools to inject malicious code into SolarWinds’ Orion update binaries. These trojanized updates delivered a backdoor known as SUNBURST and Solorigate, to systems running Orion platform versions. The impact? Roughly, 18,000 customers automatically pulled these malicious updates, exposing the networks of large companies and government entities like the National Nuclear Security Administration and enabling the bad actors to explore and exploit their networks at will over the course of many months.

By attacking the SolarWinds software supply chain and mingling their malicious code with the legitimate, trusted code that was delivered to their clients, attackers were able to plant backdoors on the systems of tens of thousands of SolarWinds’ customers.

#### Namespace Confusion — February 2021
In February 2021, news broke of a researcher, Alex Birsan, hacking over 35 big tech firms in a novel supply chain attack dubbed “dependency confusion.” The name of this attack refers to the inability of your development environment to distinguish between a private, internally-created dependency in your software build, and a package by the same name available in a public software repository.

In other words, should an attacker register the name of your private, internally-used dependency on a public repository, such as npmjs, your software development tool may inadvertently pull in the attacker’s malicious dependency as opposed to your legitimate one.

Within 72 hours after news of the namespace attack vector became public, automated malware detection services observed 300+ copycats emerging from other researchers interested in earning a bug bounty. One week later, the number of copycat attacks increased to 575. The following week, it was 750. By March 15, 2021, Sonatype’s automated malware detection service had observed more than 10,000 dependency confusion copycats having infiltrated npm and other ecosystems.

Not all copycats were benign proof of concepts. In search of bug bounty payouts, thousands were published by bad actors with malicious intent. Some of the copycats were even aimed as “vigilante vandalism” on the open source repositories. “The fact that so much of the npm ecosystem is not namespaced has actually created potential build time malware injection possibilities. If I know the name of a package in use by a company, I could go publish a malicious package using the exact same name with a new version number and know that it’s very likely that it would be ingested over the intended, internally developed package," said Sonatype CTO Brian Fox in 2017.

Public repositories that do not strictly enforce namespace rules, including npm, PyPI, RubyGems, and NuGet, are susceptible to namespace confusion. In contrast, the Maven Central and Golang’s pkg.go.dev repositories enforce strict namespacing and verify namespace ownership before artifacts can be published.

![Image description: A timeline titled "A TIMELINE OF DEPENDENCY CONFUSION July 2020 – March 2021" showing the progression of dependency confusion attacks.]

#### Codecov — April 2021
The Codecov supply chain attack publicized in April 2021 was similar to the SolarWinds attack. In this case, bad actors compromised a Codecov server to inject their malicious code into a Bash Uploader script that was then downloaded by Codecov’s customers over the course of two months.

Using the Bash uploader script used by Codecov customers, the attackers exfiltrated sensitive information including keys, tokens, and credentials from those customers' Continuous Integration/Continuous Delivery (CI/CD) environments. Using these harvested credentials, Codecov attackers reportedly breached hundreds of customer networks, including HashiCorp, Twilio, Rapid7, Monday.com, and e-commerce giant Mercari.

Although much focus has been on the compromised Bash Uploader script, the credentials used to modify the script were originally obtained by the attackers from a flawed Docker image creation process, according to Codecov. In aggregate, the incident highlighted the importance of securing CI/CD pipelines, including scrutinizing the secrets filed in these environments, and stepping up container security.

#### Microsoft’s Winget — May 2021
In May 2021, Microsoft released the first stable version of its Windows 10 package manager, Winget, which enabled users to manage apps via the command-line. Users were able to propose or add new packages to Winget on the project’s GitHub repository. But, over the weekend after its launch, many flooded Winget's software registry with pull requests for apps that were either duplicates or malformed. Moreover, some newly added duplicate packages were corrupted (incomplete) and ended up overwriting the existing packages. Over 60 such instances were seen. The incident raised serious concerns among developers about the integrity of the Winget ecosystem.

#### Kaseya — July 2021
In July 2021, the world witnessed another form of upstream software supply-chain attack. In this case, the REvil ransomware group aka Sodinokibi discovered and exploited a zero-day vulnerability in Kaseya’s Virtual System Administrator (VSA). The VSA tool is a remote monitoring and management software platform used by dozens of managed security service providers who in turn service thousands of downstream customers.

It didn’t take long for the threat actors to follow up with a $70 million ransom demand to decrypt files for more than 1,500 victims. “This episode represents yet another incident in a long trend observed over many years: in order to scale exploitation of downstream victims, bad actors are increasingly targeting technology assets and providers that live upstream within the digital value stream. This includes open source libraries, IDEs, build servers, update servers, and, most recently in the case of Kaseya, Managed Service Providers (MSPs),” Sonatype’s Matt Howard said in a blog post following the incident.

Although there are many tools designed to protect the perimeter of downstream technology assets, the truth of the matter is this: software itself is increasingly the soft underbelly of digital risk. If the past year is any indication, we expect that attackers will continue to target upstream software supply chain assets as a preferred path to exploiting downstream victims at scale.

This Kaseya incident quickly got the attention of US law enforcement authorities, including the FBI and the Cybersecurity and Infrastructure Security Agency (CISA). It is a reminder for our industry and cyber defense teams to shift security left and focus on securing the upstream portion of the digital supply chain with the same energy and vigor that has long focused on the downstream portion.

# CHAPTER 2
## Understanding Exemplary and Non-Exemplary Open Source Projects
Given its prominence in modern software development, the quality of open source libraries used from third-party suppliers has a fundamental impact on digital innovation. But how should engineering leaders go about choosing the best open source projects? Which ones are optimal? Which ones are suboptimal? Further, how should engineering teams think about project hygiene, not only as it pertains to direct dependencies, but also transitive?

In this chapter we describe open source project quality metrics collected from the Maven Central ecosystem and compare them with recent quality metrics proposed by the Open Source Security Foundation (OpenSSF) and Libraries.io.

Our analysis reveals that MTTU, a measure of a project’s dependency update velocity, is strongly associated with improved project security. We did not find OpenSSF Criticality or Libraries.io Sourcerank to be associated with improved project security.

Thus, in order to minimize risk associated with vulnerabilities in third-party open source libraries, we recommend that software development teams adopt defined criteria for selecting open source projects. Further, we recommend that teams select projects that have low MTTU.

### Open Source Project Quality Metrics
#### Sonatype Mean Time to Update (MTTU)
MTTU is the average time required for a project to respond to new versions of its dependencies. Figure 2.1 shows how MTTU is calculated. Suppose we have a component A with dependencies B and C, both at version 1.2. Suppose B and C each release a new version (1.3) and some time later A releases a new version that bumps the version of B and C to 1.3. The time between the release of B version 1.3 and the release of A version 1.3 is the Time To Upgrade (TTU) for A’s migration to B version 1.3 (and similarly for A’s adoption of C version 1.3). The average of all these upgrade times is then the MTTU.

MTTU provides visibility into an open source projects’ dependency management practices — Lower is better. Projects that consistently react quickly to dependency upgrades in their downstream dependency chain will have low MTTU. Projects that either consistently react slowly or have high variance in their reaction time will have higher MTTU.

![Image description: A diagram titled "CALCULATING MTTU" showing how Mean Time To Update is calculated.]

Figure 2.2 shows which percentage of components achieve various MTTU performance based on update data from 2020. Note that while the percentages climb quickly (26% upgrade within 20 days, 44% within 40, and 57% within 60), there is a long tail of slow-to-upgrade components, with 9% of components taking more than 180 days to upgrade.

![Image description: A bar graph titled "MTTU PERFORMANCE, 2020" showing the percentage of components that upgrade within various timeframes.]

This slow update behavior has an even stronger impact as dependency chains grow. If a transitive dependency N levels deep releases an important security update, and each component on the dependency path takes D days to upgrade, then the top level application doesn’t benefit from this fix for N × D days. Thus, even a chain of exemplary components that each upgrade within 20 days would result in a lag time of 100 days for a dependency five levels deep.

MTTU provides a measure of project quality that is based on how quickly the project moves to update dependencies. By this measure, quality has been increasing over the years.In Figure 2.3, we provide a graph of the distribution of project MTTU values by year for every year since 2011. We can see that in addition to the number of projects growing over the years, there has been a clear trend toward faster MTTUs as shown below.
- 2011 average MTTU = 371 days
- 2014 average MTTU = 302 days
- 2018 average MTTU = 158 days
- 2021 average MTTU (as of Aug 1) = 28 days[^6]

![Image description: A line graph titled "MTTU DISTRIBUTION BY YEAR Projects on Maven Central 2011 – 2021" showing the distribution of MTTU values over the years.]

#### MTTU AND SECURITY
While MTTU does not directly measure responsiveness to security issues, our analysis in previous years has found that MTTU is correlated with mean time to remediate (MTTR), which is the time required to update dependencies that have published vulnerabilities, as shown in Figure 2.4. MTTR is defined just like MTTU, except that we take the average of those dependencies that were known to be vulnerable at the time of the update.

In our previous research[^7], we found a significant correlation between MTTR and MTTU (Pearson correlation was 0.6 with N = 17,017). MTTR is generally only available for more popular and thus more scrutinized projects. Many projects fall below the level of usage required for security researchers to perform vulnerability research and discover latent issues in the codebase. MTTU on the other hand is available for all projects, providing a common source of data for evaluating project quality. Thus, we consider MTTU to be the best metric available to determine the impact a component will have on the security of projects that incorporate it. Later in this chapter, we perform additional novel research to further confirm the value of MTTU.

![Image description: A diagram titled "CALCULATING MTTR" showing how Mean Time To Remediate is calculated.]

#### Libraries.io Sourcerank
This metric aims to measure the quality of software, mostly focusing on project documentation, maturity, and community. It is computed by evaluating a number of yes / no responses to questions such as “Is the project more than six months old?” and a set of numerical questions, such as “How many ‘stars’ does the project have?” These are distilled into a single score, with yes / no questions adding or subtracting a fixed number of “points." Numerical values are then converted into points using a formula, e.g. “log(num_stars)/2." The current maximum number of points is approximately 30.

#### OpenSSF Criticality Score
OpenSSF has a set of analyses that combine into a metric called “criticality." Criticality measures a project's community, usage, and activity. This is distilled into a score that is intended to measure how crucial the project is in the open source ecosystem.

#### OpenSSF Scorecard
OpenSSF also has a more extensive evaluation of project quality called the “Scorecard” project. This project provides support for automatically monitoring development practices, tooling use, and other project quality and maturity attributes, then reporting which checks succeed and which fail. OpenSSF does not provide a mechanism for distilling this “Scorecard” into a single metric and so we did not include it in the quantitative analysis we describe below.

### Quality Metric Comparison
Figure 2.5 summarizes the four proposed project quality frameworks by showing to what extent they incorporate information about five dimensions of quality: maturity, popularity, activity, dependency management, and development practices.

#### Popularity
Libraries.IO includes project popularity metrics (stars, subscribers, and usage) as part of their Sourcerank metric. OpenSSF’s criticality metric includes usage (the number of projects that use the library) but not stars or subscribers. OpenSSF’s Scorecard system and MTTU do not include any factors that are related to popularity.

#### Activity
All four quality frameworks include some aspect of activity analysis. Sonatype’s MTTU metric is lightly correlated with activity because fast MTTU requires frequent releases. Libraries.IO Sourcerank tracks whether a project has been updated in the last six months, another weak correlation with activity. OpenSSF’s Scorecard metric includes a check (whether there has been a commit in the last 90 days) that is also weakly correlated with activity. The OpenSSF Criticality metric includes a robust set of activity measures such as commit frequency and release count.

#### Dependencies
Sonatype’s MTTU provides the most robust measure of dependency update practices, as it measures how quickly a project updates its dependencies once new versions are released. Libraries.IO Sourcerank checks whether there were outdated dependencies at the time of scoring. OpenSSF Scorecard checks if automated dependency update tools are used. OpenSSF Criticality does not consider dependency management practices.

#### Dev Practices
The OpenSSF Scorecard is the only measure that considers development practices such as whether a code review is performed, and whether continuous integration and Static Analysis and Security Testing (SAST) tooling is used.

#### Maturity
Libraries.IO and OpenSSF metrics include measures of maturity. Libraries.IO Sourcerank includes semantic