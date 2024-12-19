# Table of Contents
[Introduction](#introduction)
[Overview](#overview)
[Vulnerabilities and Security](#vulnerabilities-and-security)
[Licensing](#licensing)
[Open Source Maintenance](#open-source-maintenance)
[Conclusion](#conclusion)

# Introduction
1
[2023]
OPEN SOURCE SECURITY 
AND RISK ANALYSIS REPORT

2023 Open Source Security and Risk Analysis Report | ©2023 Synopsys, Inc. 
2

[table of contents]
[introduction]......................................................................... 3
About the 2023 Open Source Security and  
Risk Analysis Report and the CyRC.
.............................................. 3
[overview].
............................................................................. 4
2023 by the Numbers.
............................................................. 4
Industries......................................................................... 5
Terminology ...................................................................... 6
[vulnerabilities and security]
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.7
Open Source Vulnerabilities and Security.
...................................... 7
The Gordian Knot: Open Source Software Risk and Supply Chain Security.
.... 8
Vulnerabilities in Industries................................................... 9
Five-Year Rewind................................................................ 11
[licensing]
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.13
Open Source Licensing........................................................... 13
Understanding License Risk .................................................... 14
[open source maintenance]
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.15
Maintenance by Open Source Developers .
....................................... 15
Beyond Known Risk.
.............................................................. 16
Maintenance by Open Source Consumers .
....................................... 17
[conclusion]
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.18
“Trust, but Verify”.
............................................................. 18
The Problem with Trust.
......................................................... 18
Verify with an SBOM.
............................................................ 18
2023 Open Source Security and Risk Analysis Report | ©2023 Synopsys, Inc. 
3
# introduction
About the 2023 Open Source 
Security and Risk Analysis 
Report and the CyRC
In its 8th edition this year, the 2023 “Open Source Security and Risk 
Analysis” (OSSRA) report delivers our annual in-depth look at the current 
state of open source security, compliance, licensing, and code quality 
risks in commercial software. We share these findings with the goal of 
helping security, legal, risk, and development teams better understand 
the open source security and license risk landscape. The Synopsys 
Cybersecurity Research Center (CyRC) provides the data for this report. 
The CyRC’s mission is to provide and publish security advisories and 
research that help organizations better develop and consume high-quality 
software. 
The annual OSSRA report represents CyRC findings from the previous 
year's data. Thus, our 2023 report is indicative of 2022 data. In 2022,  
the CyRC studied anonymized findings from over 1,700 commercial 
codebases across 17 industries. Our Audit Services team audits 
thousands of codebases for our customers each year, with the 
primary aim of identifying a range of software risks during merger and 
acquisition (M&A) transactions. Despite 2022’s economic ambiguity 
and a corresponding slowdown in tech mergers and acquisitions, audit 
numbers remained promisingly strong.
The Synopsys Black Duck® software composition analysis (SCA) 
product team and the CyRC Audit Services team have helped security, 
development, and legal teams around the world strengthen their security 
and license compliance programs for almost 20 years. Black Duck 
SCA enables organizations to identify and track open source code 
and integrate automated open source policy enforcement across their 
existing development environments. Black Duck audits cover all aspects 
of software risk and are generally performed in the context of an M&A 
transaction. The audits also provide a comprehensive, highly accurate 
software Bill of Materials (SBOM) covering the open source, third-party 
code, web services, and application programming interfaces (APIs) in an 
organization’s applications. The Audit Services team relies on data from 
the Black Duck KnowledgeBase™ to identify potential license compliance 
and security risks. This KnowledgeBase, sourced and curated by the 
CyRC, includes data on more than 6.1 million open source components 
from over 28,000 forges and repositories. 
No matter what industry you operate in, or what role you play in relation to 
organizational security and risk, the OSSRA continues to highlight the ever-
growing presence of the open source fueling your business–as well as the 
pitfalls of failing to effectively manage it. We say it every year: Open source 
is the foundation for every application we rely on today. Identifying, tracking, 
and managing open source effectively is therefore critical to a successful 
software security program. This report offers key recommendations 
and insights to help developers and consumers of open source better 
understand the open source ecosystem and how to manage it responsibly. 
> No matter what industry 
you operate in, the OSSRA 
continues to highlight the 
ever-growing presence of 
open source fueling your 
business and highlights 
the pitfalls of failing to 
effectively manage it. 
2023 Open Source Security and Risk Analysis Report | ©2023 Synopsys, Inc. 
4
# overview
*   Percentage of codebases containing 
open source 
*   Percentage of code in codebases that 
was open source
*   Percentage of codebases containing at 
least one vulnerability
*   Percentage of codebases containing  
high-risk vulnerabilities
*   of codebases had 
license conflicts
*   of codebases 
contained open source 
with no license or a 
custom license
*   of codebases contained 
open source more than 
four years out-of-date
*   of codebases contained 
components that had 
no new development in 
the past two years
*   Of the 1,703 codebases scanned in 2022, 87% included security 
and operational risk assessments.

**96%**
**76%**
**84%**
**48%**
**54%**
**31%**
**89%**
**91%**

| Year | Percentage of codebases containing open source | Percentage of code in codebases that was open source | Percentage of codebases containing at least one vulnerability | Percentage of codebases containing high-risk vulnerabilities |
|---|---|---|---|---|
| 2018 |  |  |  |  |
| 2019 |  |  |  |  |
| 2020 |  |  |  |  |
| 2021 |  |  |  |  |
| 2022 |  |  |  |  |

*The above table represents the data visually presented in the chart.*

2019
2020
2021
2022
2018
0
40
80
20
60
100
2023 Open Source Security and Risk Analysis Report | ©2023 Synopsys, Inc. 
5
## Open Source  
by Industry
*   Percentage of codebases containing open source
*   Percentage of code in codebases that was open source

| Industry | 2018 | 2019 | 2020 | 2021 | 2022 |
|---|---|---|---|---|---|
| Aerospace, Aviation, Automotive, Transportation, Logistics |  |  |  |  |  |
| Computer Hardware and Semiconductors |  |  |  |  |  |
| Enterprise Software/SaaS |  |  |  |  |  |
| Healthcare, Health Tech, Life Sciences |  |  |  |  |  |
| Internet and Software Infrastructure |  |  |  |  |  |
| Energy and Clean Tech |  |  |  |  |  |
| Financial Services and FinTech |  |  |  |  |  |
| Internet and Mobile Apps |  |  |  |  |  |
| Big Data, AI, BI, Machine Learning |  |  |  |  |  |
| Cybersecurity |  |  |  |  |  |
| Manufacturing, Industrials, Robotics |  |  |  |  |  |
| Retail and eCommerce |  |  |  |  |  |
| Virtual Reality, Gaming, Entertainment, Media |  |  |  |  |  |
| Internet of Things |  |  |  |  |  |
| Marketing Tech |  |  |  |  |  |
| Telecommunications and Wireless |  |  |  |  |  |
| EdTech |  |  |  |  |  |

*The above table represents the data visually presented in the charts.*

[overview]
2018
2019
2020
2021
2022
100
0
20
40
60
80
2018
2019
2020
2021
2022
100
0
20
40
60
80
2018
2019
2020
2021
2022
100
0
20
40
60
80
2018
2019
2020
2021
2022
100
0
20
40
60
80
2018
2019
2020
2021
2022
100
0
20
40
60
80
2018
2019
2020
2021
2022
100
0
20
40
60
80
2018
2019
2020
2021
2022
100
0
20
40
60
80
2018
2019
2020
2021
2022
100
0
20
40
60
80
2018
2019
2020
2021
2022
100
0
20
40
60
80
2018
2019
2020
2021
2022
100
0
20
40
60
80
2018
2019
2020
2021
2022
100
0
20
40
60
80
2018
2019
2020
2021
2022
100
0
20
40
60
80
2018
2019
2020
2021
2022
100
0
20
40
60
80
2018
2019
2020
2021
2022
100
0
20
40
60
80
2018
2019
2020
2021
2022
100
0
20
40
60
80
2018
2019
2020
2021
2022
100
0
20
40
60
80
2023 Open Source Security and Risk Analysis Report | ©2023 Synopsys, Inc. 
6
# overview
## Terminology 
**Codebase** 
The code and associated libraries that make up an application or service. 
**Binary analysis** 
A type of static analysis that is used to identify the contents of an 
application when access to the source code isn’t possible. 
**Black Duck Security Advisory (BDSA)** 
Detailed, timely, consistent information on an open source vulnerability, 
researched and analyzed by the CyRC security research team. BDSAs 
provide Synopsys customers with early and supplemental notification 
of open source vulnerabilities and upgrade/patch guidance. Black Duck 
Security Advisories go beyond the National Vulnerability Database (NVD) 
and provide enhanced data, completeness, and accuracy, so you get early 
warning and comprehensive insight. BDSAs deliver same-day notification, 
actionable mitigation guidance and workaround information, severity 
scoring, references, and more. 
**Software component** 
Prewritten code that developers can add to their software. A software 
component might be a utility, such as a calendar function, or a 
comprehensive software framework supporting an entire application. 
**Dependency** 
A software component becomes a dependency when other software 
uses it—that is, when software becomes dependent on that component. 
Any given application or service may have many dependencies, which 
themselves may depend on other components. 
**Open source license** 
A set of terms and conditions stating end-user obligations when an 
open source component (or a snippet of a component’s code) is used in 
software, including how the component may be used and redistributed. 
Most open source licenses fall into one of two categories.
**Permissive license** 
A permissive license allows use with few restrictions. Generally, the main 
requirement of this type of license is to include attribution of the original 
code to the original developers. 
**Copyleft license** 
A copyleft license generally includes a reciprocity obligation stating that 
modified and extended versions are released under the same terms and 
conditions as the original code, and that the source code containing 
changes must be provided upon request. Commercial entities are wary of 
including open source with copyleft licenses in their software, as its use 
can call the overall codebase’s intellectual property (IP) into question. 
**Software composition analysis (SCA)** 
A type of application security tool used to automate the process of open 
source software management. SCA tools integrate within the software 
development lifecycle to identify the open source used in a codebase, 
provide risk management and mitigation recommendations, and perform 
license compliance verification. 
**Software Bill of Materials (SBOM)** 
A comprehensive inventory of the software components and 
dependencies in a codebase, often generated by a software composition 
analysis tool. As phrased by the National Telecommunications and 
Information Administration (NTIA), “An SBOM should include a machine-
readable inventory of your software components and dependencies, 
information about these components, and their hierarchical relationships.” 
Since SBOMs are intended to be shared across companies and 
communities, having a consistent format (that is both human- and 
machine-readable) with consistent content is critical. U.S. government 
guidelines currently specify two standards as approved formats: Software 
Package Data Exchange (SPDX) and CycloneDX. 
**Executive Order 14028** 
U.S. President Biden issued an order titled “Improving the Nation’s 
Cybersecurity” in May 2021, instructing various agencies of the federal 
government to create software security guidelines for companies doing 
business with the federal government. This order includes a timeline 
 for activities that, as of the writing of this report, do not mandate 
contractual obligations. However, despite the lack of hard requirements, 
the order has prompted many organizations to re-examine their security 
practices and scrutinize their level of software security risk. The use of 
an SBOM is a key element promoted by EO 14028, as it facilitates the 
communication of software supply chain information between producers 
and consumers of software. 
**Apache Log4J2 vulnerability(ies) (BDSA- 
2021-3887, CVE-2021-44228, et al)** 
The open source component Apache Log4J2 (commonly known 
as Log4J) is broadly used within the Java community to implement 
application logging. Several vulnerabilities have been identified in Log4J, 
including remote code execution (RCE), denial of service, and LDAP 
vulnerabilities. 
**Zero-day vulnerability** 
A vulnerability either unknown to those who would be interested in its 
mitigation (including the vendor or creator of the target software) or 
known and without a patch to correct it. 
**OpenSSL vulnerabilities**
In November 2022, OpenSSL, a popular open source command-line tool, 
released an advisory warning of two critical vulnerabilities (CVE-2022-
3602 and CVE-2022-3786). Their severity level was later downgraded to 
“high.” These are buffer overflow/overrun vulnerabilities in the certificate 
validation. Exploit of the former vulnerability could lead to crashes and 
introduce the potential of arbitrary code execution, and exploit of the 
latter could lead to memory corruption issues. 
**Buffer overflow / overrun vulnerability**
Buffers are used for temporary memory storage during the execution of 
an application. When the volume of data being written to a buffer exceeds 
the buffer’s capacity, a buffer overflow or overrun occurs, which can lead 
to crashes, memory issues, or other unexpected behavior. Attackers 
can exploit this vulnerability to accomplish tasks like altering files and 
accessing sensitive information. 
2023 Open Source Security and Risk Analysis Report | ©2023 Synopsys, Inc. 
7
# vulnerabilities and security
## Open Source Vulnerabilities and 
Security
Of the 1,703 codebases analyzed by the Black Duck Audit Services team 
for this year’s report, 96% contained open source. Seventy-six percent of 
the total codebases scanned were open source, meaning 76% of the total 
code in our study was open source code. 
The average number of open source components in a given application this 
year was 595. When monitoring for security vulnerabilities and performing 
security maintenance activities, what might be practical for a small number 
of components becomes overwhelming and virtually impossible at this 
scale, and demands the use of an automated solution like SCA.
Eighty-four percent of codebases contained at least one known open 
source vulnerability, an almost 4% increase from the 2022 edition of the 
OSSRA report. And 48% of the codebases we examined contained high-risk 
vulnerabilities, down only 2% from last year. High-risk vulnerabilities are 
those that have been actively exploited, already have documented proof-of-
concept exploits, or are classified as remote code execution vulnerabilities. 

| Year | Percentage of codebases containing open source | Percentage of codebases containing at least one vulnerability | Percentage of codebases containing high-risk vulnerabilities |
|---|---|---|---|
| 2018 |  |  |  |
| 2019 |  |  |  |
| 2020 |  |  |  |
| 2021 |  |  |  |
| 2022 |  |  |  |

*The above table represents the data visually presented in the chart.*

### Vulnerabilities and High-Risk Vulnerabilities
0
20
40
60
80
100
2018
2022
2021
2020
2019
*   Percentage of codebases containing open source
*   Percentage of codebases containing at least one vulnerability 
*   Percentage of codebases containing high-risk vulnerabilities

### Components with Vulnerabilities
**Percentage of codebases containing vulnerable components**
*   47% jQuery
*   31% Lodash
*   23%  Bootstrap (Twitter)
*   11%  jackson-databind
*   10%  Spring Framework
*   6%  Netty Project
*   5% XStream
*   5%  Apache Tomcat*
*   .4% PHP*
*   .1%  Linux Kernel*

*Components containing high-risk vulnerabilities*

> All Black Duck audits examine open source 
license compliance. Customers can opt out of 
the vulnerability / operational risk assessment 
portion of the audit at their discretion. In this 
2023 edition, the Black Duck Audit Services 
team conducted 1,703 audits. Of those audits, 
87% (1,481) opted to undergo a vulnerability 
/ operational risk assessment. The data in the 
"Vulnerabilities and Security" and "Open Source 
Maintenance" sections of the 2023 OSSRA report is 
based on the 1,481 codebases that included risk 
assessments, whereas the data in the "Licensing" 
section is based on all 1,703 codebases.

2023 Open Source Security and Risk Analysis Report | ©2023 Synopsys, Inc. 
8
# vulnerabilities and security
## The Gordian Knot: Open Source 
Software Risk and Supply Chain 
Security
A recent research report, “Walking the Line: GitOps and Shift Left Security,” 
cosponsored by Synopsys and the Enterprise Strategy Group, explored 
market concerns and how organizations are tackling current security 
challenges. Seventy-three percent of organizations surveyed for that report 
said they had “significantly increased their efforts to secure open source 
software, container images, and third-party software components as a result 
of recent software supply chain attacks.” Troublingly, 34% of respondents 
also stated that they had experienced “exploit(s) that took advantage of 
known vulnerabilities in open source software” within the last 12 months.
By now, anyone remotely involved in software security is likely concerned 
with the software supply chain. Software supply chain security has 
dominated the news and touched organizations across industry verticals. 
But nearly two years out from President Biden’s executive order (EO 
14028), organizations are still struggling with supply chain basics—
understanding the breadth of their software supply chain, establishing 
visibility into the software they depend on, and satisfying growing 
transparency pressures for the software they distribute and sell. 
So what’s to be done? The first step in securing the software supply chain 
is managing the open source and third-party code in your applications. 
If you can’t effectively manage and ensure the security of your open 
source and third-party software, no other efforts made toward securing 
your supply chain will work—or frankly, even matter. Managing this 
software entails gaining complete visibility into your dependencies 
and having the ability to easily gather information pertaining to the risk 
introduced by these components. Once this risk has been identified, you 
need tooling and practices in place to manage, prioritize, and remediate it.
Further, communicating any identified risk to key stakeholders is also 
important, as it provides visibility into and support of risk management 
activities and initiatives. Additionally, all these capabilities and practices 
should be built into existing development pipelines, leveraging automation 
wherever possible. 
If it sounds complex, that’s because it is. The final product of your 
supply chain, as well as its users, are affected by every component, 
person, activity, material, and procedure involved in its creation. Only with 
complete visibility into your supply chain, and its numerous inputs, can 
you begin to secure it. And this visibility begins with verifying that you are 
truly secure. The old Russian proverb “Trust, but verify” has never been 
more fitting; managing your open source and third-party software means 
you have verified its security. Without verification, you’re placing baseless 
trust in the weakest links of your supply chain. 
> of organizations worldwide will 
have experienced attacks on their 
software supply chains by 2025
–Gartner
**+45%**
> So what’s to be done? The first step 
in securing the software supply chain 
is managing the open source and 
third-party code in your applications.
> Open source software risk 
and supply chain security 
are inextricably linked. 
2023 Open Source Security and Risk Analysis Report | ©2023 Synopsys, Inc. 
9
# vulnerabilities and security
*   Percentage of codebases containing open source 
*   Percentage of code in codebases that was open source 
*   Percentage of codebases containing vulnerabilities

## Vulnerabilities in Industries
Each year, we watch the percentage of codebases containing open 
source rise, and this year, even the industries with the smallest amount 
(Manufacturing, Industrials, and Robotics) still had open source in 92% of 
their codebases. 
We were troubled, however, when we looked at the presence of open 
source in tandem with vulnerabilities; of particular note was the 
Aerospace, Aviation, Automotive, Transportation, and Logistics sector. 
All—100%—of the codebases we examined in this sector contained open 
source, and open source made up 73% of its code. Sixty-three percent of 
its codebases contained vulnerabilities classified as high risk (those with 
a severity score of 7 or higher). 
We saw more of the same with the Energy and Clean Tech sector, in 
which 78% of the total code was open source and 69% contained high-
risk vulnerabilities. The total open source identified within this sector’s 
codebases was 95%.
Similar findings, to lesser degrees, played out across industries, painting 
a picture that security teams would do well to heed. Open source was in 
nearly everything we examined this year; it made up the majority of the 
codebases across industries, and it contained troublingly high numbers of 
known vulnerabilities that organizations had failed to patch, leaving them 
vulnerable to exploit. It is crucial to understand that while open source 
itself does not pose any inherent level of risk, failing to manage it does. 

| Industry | 2018 | 2019 | 2020 | 2021 | 2022 |
|---|---|---|---|---|---|
| Aerospace, Aviation, Automotive, Transportation, Logistics |  |  |  |  |  |
| Big Data, AI, BI, Machine Learning |  |  |  |  |  |
| Computer Hardware and Semiconductors |  |  |  |  |  |
| Cybersecurity |  |  |  |  |  |
| EdTech |  |  |  |  |  |
| Energy and Clean Tech |  |  |  |  |  |
| Enterprise Software/SaaS |  |  |  |  |  |
| Financial Services and FinTech |  |  |  |  |  |
| Healthcare, Health Tech, Life Sciences |  |  |  |  |  |
| Internet and Software Infrastructure |  |  |  |  |  |
| Internet and Mobile Apps |  |  |  |  |  |
| Internet of Things |  |  |  |  |  |
| Manufacturing, Industrials, Robotics |  |  |  |  |  |
| Marketing Tech |  |  |  |  |  |
| Retail and eCommerce |  |  |  |  |  |
| Telecommunications and Wireless |  |  |  |  |  |
| Virtual Reality, Gaming, Entertainment, Media |  |  |  |  |  |

*The above table represents the data visually presented in the charts.*

### Open Source and Vulnerabilities by Industry
2018
2019
2020
2021
2022
0
20
40
60
80
100
2018
2019
2020
2021
2022
0
20
40
60
80
100
2018
2019
2020
2021
2022
0
20
40
60
80
100
2018
2019
2020
2021
2022
0
20
40
60
80
100
2018
2019
2020
2021
2022
0
20
40
60
80
100
2018
2019
2020
2021
2022
0
20
40
60
80
100
2018
2019
2020
2021
2022
0
20
40
60
80
100
2018
2019
2020
2021
2022
0
20
40
60
80
100
2018
2019
2020
2021
2022
0
20
40
60
80
100
2018
2019
2020
2021
2022
0
20
40
60
80
100
2018
2019
2020
2021
2022
0
20
40
60
80
100
2018
2019
2020
2021
2022
0
20
40
60
80
100
2018
2019
2020
2021
2022
0
20
40
60
80
100
2018
2019
2020
2021
2022
0
20
40
60
80
100
2018
2019
2020
2021
2022
0
20
40
60
80
100
2018
2019
2020
2021
2022
0
20
40
60
80
100
2018
2019
2020
2021
2022
0
20
40
60
80
100
2023 Open Source Security and Risk Analysis Report | ©2023 Synopsys, Inc. 
10
# vulnerabilities and security
## CVEs/BDSAs
### High-Risk CVEs/BDSAs
*   Percentage of codebases with one of the 10 most-common CVEs/BDSAs

    *   BDSA-2020-0964 (CVE-2020-11023)
    *   BDSA-2014-0063
    *   BDSA-2021-3651
    *   CVE-2019-5428
    *   BDSA-2021-0392 (CVE-2021-23337)
    *   BDSA-2019-1138 (CVE-2019-11358)
    *   BDSA-2015-0567
    *   BDSA-2017-2930 (CVE-2015-9251)
    *   BDSA-2021-0375 (CVE-2020-28500)
    *   BDSA-2020-3839

*   Percentage of codebases with one of the 10 most-common high-risk CVEs/BDSAs

    *   BDSA-2015-0753 (CVE-2015-6420)
    *   CVE-2020-8022
    *   CVE-2021-41720
    *   CVE-2018-1000