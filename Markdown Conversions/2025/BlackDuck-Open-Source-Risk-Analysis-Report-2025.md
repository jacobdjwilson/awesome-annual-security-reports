# 2025 Open Source Security and Risk Analysis Report

## Table of Contents
- [Welcome to the 2025 OSSRA Report](#welcome-to-the-2025-ossra-report)
- [Who Should Read This Report](#who-should-read-this-report)
- [What You’ll Learn and Why It Matters](#what-you’ll-learn-and-why-it-matters)
- [About This Report’s Data and Black Duck Audits](#about-this-report’s-data-and-black-duck-audits)
- [Our Findings at a Glance](#our-findings-at-a-glance)
- [Looking at Open Source Risk and Vulnerabilities](#looking-at-open-source-risk-and-vulnerabilities)
- [Understanding Risk Management and Gaining Visibility into Your Code](#understanding-risk-management-and-gaining-visibility-into-your-code)
- [Enhancing Software Security and Transparency with SCA and SBOMs](#enhancing-software-security-and-transparency-with-sca-and-sboms)
- [Analyzing the Impact of a Vulnerability](#analyzing-the-impact-of-a-vulnerability)
- [Log4j and Equifax: Two Lessons on the Need for Visibility into Your Code](#log4j-and-equifax-two-lessons-on-the-need-for-visibility-into-your-code)
- [The Top High- and Critical-Risk Vulnerabilities](#the-top-high--and-critical-risk-vulnerabilities)
- [What the Data Tells Us](#what-the-data-tells-us)
- [Industry-Specific Insights](#industry-specific-insights)
- [Open Source Licensing](#open-source-licensing)
- [How Conflicts, Variants, and Lack of Licenses Create Risk](#how-conflicts-variants-and-lack-of-licenses-create-risk)
- [The Impact of Transitive Dependencies on License Conflicts](#the-impact-of-transitive-dependencies-on-license-conflicts)
- [The Top 10 Open Source Licenses of 2024](#the-top-10-open-source-licenses-of-2024)
- [What Are Permissive, Weak Copyleft, and Reciprocal Open Source Licenses?](#what-are-permissive-weak-copyleft-and-reciprocal-open-source-licenses)
- [How to Manage Open Source License Risk with SCA](#how-to-manage-open-source-license-risk-with-sca)
- [Industry Perspectives on License Conflicts](#industry-perspectives-on-license-conflicts)
- [If You Anticipate an M&A](#if-you-anticipate-an-m&a)
- [Maintenance and Operational Factors Impacting Risk](#maintenance-and-operational-factors-impacting-risk)
- [Conclusion: The More Things Change](#conclusion-the-more-things-change)
- [Key Recommendations](#key-recommendations)

---

## Welcome to the 2025 OSSRA Report

Open source software (OSS) has revolutionized application development, providing a vast repository of prebuilt components that offer numerous benefits such as cost savings, flexibility, and scalability. However, with all those benefits comes risks that every organization using open source needs to be prepared to acknowledge and address.

The 2025 “Open Source Security and Risk Analysis” (OSSRA) report details key findings from Black Duck® audit data, including security vulnerabilities, licensing issues, component maintenance, and industry trends. Our analysis shows that open source is ubiquitous, and that it can introduce significant risk unless properly identified and managed.

> “He will win who has prepared himself.”
> —Sun Tzu

## Who Should Read This Report

The findings of this report will be beneficial for a variety of readers, particularly those involved in securing the software supply chain, as well as those directly involved in software development, security and risk management, and merger and acquisition (M&A) activities.

Developers will gain insights into the types of vulnerabilities that we found prevalent in open source software, such as cross-site scripting (XSS) and denial-of-service (DoS) vulnerabilities. For example, the OSSRA report highlights the importance of following input validation and sanitization techniques, which can help developers build more-secure applications.

Further, this report identifies the most common open source components containing vulnerabilities, which will aid developers in making informed decisions when selecting open source libraries and frameworks. For example, development teams should be aware that our data shows that jQuery, jackson-databind, and the Spring Framework often include vulnerabilities that require regular management and patching.

OSSRA 2025 also emphasizes the risks associated with using out-of-date components and the need for all organizations to implement a process for timely updates. As one example, 90% of audited codebases were found to have open source components more than four years out-of-date. Outdated components magnify security risk, provide attackers with an expanded attack surface, and create compliance and compatibility issues. The presence of older open source also suggests that developers are not taking advantage of software improvements and are relying on code that is no longer being maintained.

Readers with a security focus can leverage the data presented in OSSRA 2025 to improve their vulnerability management processes. For example, the report identifies the top common vulnerabilities and exposures (CVEs) found in our audits, as well as their relationship to common software weaknesses (CWEs).

Risk management professionals can use OSSRA data to inform their strategic decisions about open source software adoption and risk mitigation. The ability to compare vulnerability percentages and other metrics across industries can help risk managers pinpoint areas where their organization is performing well or needs improvement.

The OSSRA data, primarily derived from analysis of M&A targets’ code, provides key insights for professionals involved in merger and acquisition transactions into the kinds of issues they may be taking on in their own transactions, such as common open source license conflicts, the security posture of the target company, and potential operational challenges that could impact the target’s IP value.

## What You’ll Learn and Why It Matters

**There’s much more open source in your software than you think:** Ninety-seven percent of the codebases we evaluated contained open source, with an average 911 OSS components found per application. From an industry perspective, the percentages ranged from 100% in the Computer Hardware and Semiconductors, EdTech, and Internet and Mobile Apps sectors, to a “low” of 79% for Manufacturing, Industrials, and Robotics.

**Open source codebases are getting bigger and more complicated:** Our data shows that the number of open source files in an average application has tripled in just the last four years. One of the reasons behind this is the use of “transitive dependencies”—open source libraries that other software components rely on to function. Open source frequently uses other open source. Our audits found that 64% of open source components identified in our scans were transitive dependencies, most nearly impossible to locate or track without using an automated tool. Finding all instances of a transitive dependency can be like searching for a needle in a haystack when you lack an up-to-date inventory of third-party code.

**Where all this open source is coming from:** Our audits show that the majority of open source is being downloaded from package manager repositories. Over 280,000 of the nearly 1 million OSS components found in our audits originated from one such repository—npm, a massive public database of JavaScript packages.

**Whether you think of open source as “free” or not, it comes at a cost:** The odds are better than 80% that an application your organization is using right now contains high- or critical-risk open source vulnerabilities, with nearly half of those introduced by transitive dependencies.

**Transitive dependencies present licensing and maintenance issues as well as security challenges:** Our audits found that over half the codebases contained license conflicts, many caused by a transitive dependencies’ incompatibility with another component’s license. Nearly 30% of component license conflicts found in our audits were caused by transitive dependencies.

**Static application security testing (SAST) and dynamic application security testing (DAST) can help identify coding errors:** These testing methods can find errors such as input validation and sensitive information exposure, and mistakes like not encrypting important data when it’s being sent over the internet, outdated or weak encryption methods, and failing to properly protect passwords or other secret information.

**Every organization using web applications and services should be evaluating them with software composition analysis (SCA) and DAST tools:** Development and security teams need to implement a multifaceted security approach integrating DAST, SAST, and SCA to achieve the comprehensive security coverage modern software demands. Our findings indicate that if such a full-spectrum approach were applied, potential exposure to critical vulnerabilities would be markedly reduced.

## About This Report’s Data and Black Duck Audits

This report uses data from the Black Duck Audit team’s evaluation of anonymized findings from 1,658 analyses of 965 commercial codebases across 16 industries during 2024.

Black Duck offers a range of services including open source audits tailored to diverse needs and objectives. Open source audits leverage a combination of automated tools, comprehensive databases, and expert analysis to provide a thorough assessment of an organization’s OSS usage. Built over two decades, the Black Duck KnowledgeBase™, a key component of these audits, contains data on millions of open source components, including their licenses, vulnerabilities, and potential risks. Sourced and curated by the Black Duck Cybersecurity Research Center (CyRC), the KnowledgeBase includes data on more than 7.8 million open source components from over 31,000 forges and repositories.

A Black Duck open source audit typically involves the following steps:

- **Codebase submission**: An organization provides Black Duck with access to the codebase to be audited. This includes source code, binaries, and other relevant artifacts.
- **Automated analysis**: Black Duck utilizes its suite of automated tools, including its SCA solution, to scan the codebase and identify all open source components and those components’ dependencies, including transitive dependencies, through advanced string search capabilities.
- **Expert review**: Black Duck’s team of open source experts reviews the results of the automated analysis, validates the findings, and ensures completeness and accuracy.
- **Report generation**: Black Duck generates a comprehensive set of reports that provide a detailed Software Bill of Materials (SBOM) of all open source components, their associated licenses, known security vulnerabilities, and potential operational risks. The reports also detail the issues cataloged in the SBOM.
- **Remediation guidance**: Black Duck provides guidance on how to address the identified issues, such as updating vulnerable components, resolving license conflicts, and mitigating operational risks.

*Note: Several improvements to how the Black Duck Audit team evaluates and presents audit data were implemented during 2024. Notably, a single submitted customer codebase is now split into multiple analyses called “projects.” The new technique provides a more granular approach to analyzing codebases and offers several benefits to customers including more-detailed reports and more-accurate component identification and dependency tracking.*

## Our Findings at a Glance

![Infographic showing 97% of codebases contained open source, 70% of scanned code had its origin in open source, and 64% of OSS components were transitive dependencies.]

- **OSS components found per application**: 911
- **Growth of open source files**: The number of open source files in an average application has tripled in the last four years (5,386 in 2020; 11,858 in 2022; 16,082 in 2024).

**Originating Repositories (2024):**
- npm (JavaScript): 282,521 components
- yarn (JavaScript): 162,327 components
- pnpm (JavaScript): 24,069 components
- Cargo (Rust): 33,327 components
- Nuget (C#, VB, F#, WiX, C++, Q#): 29,818 components
- go_mod (Go): 24,069 components
- Maven (Java): 14,097 components
- packagist (PHP): 6,112 components
- Gradle (Java, C, JavaScript): 4,615 components

**Vulnerabilities and Security:**
- 86% of risk-assessed codebases contained vulnerable open source.
- 81% of risk-assessed codebases contained high- or critical-risk vulnerabilities.
- 8 of the top 10 high-risk vulnerabilities were found in jQuery.

![Figure 1: Codebases Containing High-Risk Vulnerabilities by Industry, showing Internet and Mobile Apps at 100% down to Energy and Clean Tech at 60%.]

**Licensing:**
- 56% of all codebases had license conflicts.
- 33% of all codebases had OSS components with no license or customized license language.

**Maintenance and Operational Risk:**
- 90% of all codebases contained outdated OSS components.
- 91% of all codebases contained components more than 10 versions behind the most current version.

![Figure 2: Codebases Containing License Conflicts by Industry, showing EdTech at 71% down to Energy and Clean Tech at 37%.]

## Looking at Open Source Risk and Vulnerabilities

All Black Duck audits examine open source license compliance. Customers can opt out of the vulnerability/operational risk assessment portion of the audit at their discretion. During 2024, the Black Duck Audit team conducted vulnerability/operational risk assessments on 901 customer codebases.

### Software Security Begins with Visibility into Your Code

- 86% of the codebases contained at least one vulnerability.
- 81% of the codebases contained high- or critical-risk vulnerabilities.
- Maximum number of unique vulnerabilities found in a single codebase: 3,548.
- Mean number of unique vulnerabilities per codebase: 154.

![Figure 3: Top 10 Components Containing High- or Critical-Risk Vulnerabilities, including jQuery (32%), jQuery UI (16%), Bootstrap (15%), and others.]

## Understanding Risk Management and Gaining Visibility into Your Code

Effective open source risk management is not about finding and fixing every vulnerability—a Sisyphean task if ever there was one. Rather, risk management is about gaining the knowledge necessary to make informed decisions regarding risk to your code.

> “Less certainty requires more inquiry.”
> —Erik Seidel

## Enhancing Software Security and Transparency with SCA and SBOMs

An SBOM is a formal record containing the details and supply chain relationships of all the components used in building software. It also serves as an inventory of all the constituent parts of a software application.

**SBOMs provide benefits for:**
- Risk management
- Vulnerability management
- License compliance
- Software quality
- Mergers and acquisitions
- Secure software development
- Effective software development, deployment, and maintenance
- Consistent and readable dependency profiles
- Standardized dependency listing and automation

### How SCA Tools Generate SBOMs
- **Code scanning**: Manifest scanning, binary scanning, hybrid scanning, and snippet scanning.
- **Dependency analysis**: Analyzing relationships between direct and transitive dependencies.
- **Vulnerability and license identification**: Comparing components against databases.
- **SBOM generation**: Creating files in formats like SPDX or CycloneDX.
- **Continuous monitoring**: Keeping the SBOM up-to-date.

## Analyzing the Impact of a Vulnerability

When an SCA tool identifies vulnerabilities, reachability and impact analysis helps determine if a vulnerability exists on a “busy road” within your application’s code, making it more likely to be exploited.

**How SCA Tools Can Help:**
SCA tools can prioritize vulnerabilities based on factors such as severity, exploitability, and potential impact. Black Duck SCA prioritizes vulnerabilities based on factors such as exploitability, remediation guidance, severity scoring, and call path analysis.

## Log4j and Equifax: Two Lessons on the Need for Visibility into Your Code

The Log4Shell vulnerability of 2021 and the Equifax breach of 2017 are reminders of the importance of visibility. In both cases, a lack of awareness of the open source components in use were contributing factors to the severity of the incidents.

> “It is critical for an organization to know what assets are present within its IT environments to make accurate and informed risk determinations—such as when, and how, to patch a vulnerable system.”
> —The Equifax Data Breach, Majority Staff Report, 115th Congress, December 2018

## The Top High- and Critical-Risk Vulnerabilities

A CVE is a standardized identifier for publicly known cybersecurity vulnerabilities. A CWE is a community-developed list of software and hardware weakness types.

![Figure 5: Top CWEs Found in Codebase Scans, led by CWE-20 (Improper Input Validation) at 71%.]

![Figure 6: Top High- and Critical-Risk Vulnerabilities Found, including CVE-2020-11023 (33%) and CVE-2020-11022 (33%).]

*(Detailed descriptions of the top 10 vulnerabilities follow in the original report, focusing on jQuery XSS flaws, prototype pollution, and Babel/semver issues.)*

## What the Data Tells Us

The prevalence of CWE-79 in our results, and all the CVEs related to cross-site scripting exploits of jQuery vulnerabilities, highlights the critical importance of input validation in web development. jQuery is not inherently insecure, but it is often used in outdated versions that have available patches.

## Industry-Specific Insights

High-risk industry sectors include Internet and Mobile Apps (100%), Marketing Tech (88%), and Computer Hardware and Semiconductors (87%).

## Open Source Licensing

> “To be a programmer requires that you understand as much law as you do technology.”
> —Eric Allman

- Percentage of codebases with license conflicts: 56%
- Percentage of codebases containing open source with no license or a custom license: 33%

### How Conflicts, Variants, and Lack of Licenses Create Risk
In the U.S. and other jurisdictions, creative work is protected by exclusive copyright by default. A declared license conflict arises when the license of an open source component clashes with the overall license declared for the entire project.

### The Top 10 Open Source Licenses of 2024
1. MIT License (92%)
2. Apache License 2.0 (90%)
3. BSD 3-Clause (85%)
4. BSD 2-Clause (74%)
5. ISC License (61%)
6. Generic Public Domain (57%)
7. GNU Lesser General Public License v2.1+ (48%)
8. The Unlicense (47%)
9. Creative Commons Zero v1.0 (46%)
10. Mozilla Public License 2.0 (45%)

## What Are Permissive, Weak Copyleft, and Reciprocal Open Source Licenses?

- **Low-Risk (Permissive)**: MIT and Apache. Generally require keeping copyright notices.
- **Medium-Risk (Weak Copyleft)**: Mozilla Public License. Require modifications to be released under the same terms.
- **High-Risk (Reciprocal/Copyleft)**: GPL. May require releasing proprietary software under the same license.

## How to Manage Open Source License Risk with SCA

The first step to managing risk is using an automated SCA tool to create an up-to-date, accurate SBOM. Black Duck SCA enables development, security, and compliance teams to manage these risks by providing an accurate SBOM and data on over 2,500 open source licenses.

## Industry Perspectives on License Conflicts

Tech-heavy industries like Big Data and AI, Financial Services, and Computer Hardware exhibit a significantly higher percentage of codebases with license conflicts.

## If You Anticipate an M&A

*(Content truncated in source)*

---

ies, especially startups and smaller organizations, also have
limited resources and expertise focused on software licensing.

Moderate Risk

•  Sectors including Aerospace, Cybersecurity, Manufacturing, and Enterprise Software demonstrate a moderate level of
risk. While the percentages are lower than the high-risk group, they still have a considerable chance of encountering
licensing problems.

Lower Risk (But Not Risk-Free)

•  Industries like Healthcare and Energy show a lower percentage of license conflicts. However, this doesn’t imply

that they are immune to such issues. For example, Healthcare organizations rely on a wide range of software, from
electronic health records and medical imaging systems to telehealth platforms and AI-powered diagnostic tools.
This intricate ecosystem often involves integrating numerous third-party components and libraries, increasing the
possibility of licensing issues.

If You Anticipate an M&A

If your company plans to be involved with an M&A transaction at some point, either as seller or buyer, you will want to
involve your organization’s IP counsel or seek outside legal advice, as understanding licensing terms and conditions and
identifying conflicts among various licenses can be challenging. It’s vital to get this right the first time—especially if you
build packaged or embedded software—because license terms are often more explicit for shipped software and harder
to mitigate after the fact. Knowing what open source code is in a company’s codebase is crucial for properly managing
its use and reuse, ensuring compliance with software licenses, and staying on top of patching vulnerabilities—all
essential steps in reducing business risk.

If you’re on the buy side of a tech M&A transaction, an open source audit should be part of the software due diligence
process. A code audit enables a buyer to understand risks in the software that could affect the value of the intellectual
property, and the remediation required to address those risks. An open source audit can also be invaluable for
companies wanting a better understanding of the code’s composition. For example, using a range of tools such as
Black Duck SCA, expert auditors comprehensively identify the open source components in a codebase and flag legal
compliance issues related to those components, prioritizing issues based on their severity.

An audit uncovers known security vulnerabilities that affect open source components, as well as information such
as versions, duplications, and the state of a component’s development activity. It also provides clues as to the
sophistication of a target’s software development processes. Open source is so ubiquitous today that if a company isn’t
managing that part of software development well, it raises questions about how well it is managing other aspects.

2025 Open Source Security and Risk Analysis report  |  23

Acquirers need to identify problematic open source in the target’s code before the transaction terms are set, and a
trusted third-party audit is the best way to get a deep, comprehensive view. Identifying even permissively licensed open
source is valuable, as acquirers will want to ensure they will be able to comply with the attribution requirements of those
licenses. Sellers should prepare for questions about the composition of their code and how well they have managed
open source security and license risk. Proactive sellers may employ an audit in advance to avoid surprises in due
diligence, particularly given the amount of unknown open source in a typical company’s code.

By identifying open source code and third-party components and licenses, an open source audit can alert your firm to
potential legal and security issues in an M&A transaction.

Avoid surprises

Mitigate legal
exposure

Understand risks that
may affect software
asset values

Resolve potential issues
before they affect the
transaction

Build appropriate
protections into the
deal terms

Plan integration and
remediation of seller/
buyer code

The bottom line is that significant monetary and brand risk can be buried in the open source components of acquired
code. Evaluating that risk as part of an acquirer’s due diligence must be part of the decision-making process in an M&A
transaction.

2025 Open Source Security and Risk Analysis report  |  24

Maintenance and Operational Factors
Impacting Risk

Ideally, all of us would use only open source components sustained by robust communities. After all, support from large
and vibrant developer communities was one of the key benefits of OSS promised by open source champions when the
software was first introduced. Dedicated communities of developers would deliver enhanced code quality and security
while fostering regular improvements to the projects they were overseeing.

Unfortunately, that scenario never happened for many open source projects. As the Linux Foundation’s Census III of
Free and Open Source Software report (utilizing SCA data from Black Duck among other vendors) relates, much of the
most widely used open source today is developed and maintained by only a handful of contributors, not the thousands
or millions of developers popularly thought to be working behind the scenes. In reality, the small number of contributors
working to ensure updates—including feature improvements as well as security and stability updates—decreases over
time on almost all OSS projects.

When maintainers have stopped maintaining a project, one consequence is elevated security risk, as the data from our
scans shows.

Outdated Components

•  A very high percentage of codebases—90%—contain open source components that are more than four years out-

of-date. This indicates a widespread issue of outdated dependencies and could lead to security vulnerabilities and
compatibility issues.

Inactive Components

•  An equally high portion of codebases—91%—have components that have not seen new development in the past two
years. This suggests that many applications and web services are relying on OSS that no longer receive updates,
potentially leaving them vulnerable to undiscovered or unpatched security flaws.

•  Seventy-nine percent of codebases contain components with no activity for the last 24 months, while still using the
latest version of the component. This suggests that even up-to-date components are not being actively maintained.

•  Eighty-eight percent of codebases have components with no activity for the last 24 months and are not using the

latest version of the component—an even riskier prospect for those using the components.

90%

91%

79%

88%

of codebases
contain open source
components that are
more than four years
out-of-date

of codebases have
components that
have not seen new
development in the past
two years

of codebases contain
components with no activity
for the last 24 months, while
still using the latest version
of the component

of codebases have
components with no activity
for the last 24 months and
are not using the latest
version of the component

2025 Open Source Security and Risk Analysis report  |  25

Version Lag

•  The majority of codebases—91%—include OSS that is not the latest available version of that particular component.

•  Worse, 90% of codebases contain open source components that are more than 10 versions behind the most recent

release

A failure to keep up with current releases, which often include important bug fixes and security patches, increases risk
and technical debt.

There can be valid justifications for not keeping an open source component up-to-date. Major version updates can
introduce significant changes that might break your existing code, especially if you’ve already fallen several versions
behind. Sometimes the effort required to adapt your code isn’t feasible. Updating can be time-consuming, requiring
development time, testing, and deployment. Smaller teams or projects with limited resources might need to prioritize
more critical tasks.

But, as we’ve noted in a decade of publishing OSSRA reports, open source is different from commercial software—not
worse, not better, but different—and it requires different techniques when it comes to maintenance. For example, all
organizations that use commercial software are familiar with patches and updates being “pushed” to their software, or
at a minimum, receiving a notice from the vendor that an update is available for download. That’s seldom the case with
open source, where users are largely left to their own initiative to stay aware of a component’s status.

Given that reality, how do you stay aware of updates?

Follow project websites and repositories: Most open source projects have websites, blogs, or repositories (like
GitHub) where they announce new releases and provide changelogs. Subscribe to their mailing lists or RSS feeds
to stay informed. However, with the number of open source components in a typical application today, manually
tracking is impractical, so automated approaches become more critical.

Use package managers: Package managers (like npm, pip, or Bundler) often provide notifications about
available updates and can automate the update process. The vast majority of open source identified in our scans
originated from npm, which provides a variety of tools to upgrade packages. For example, running npm outdated
will generate a list of packages that have available updates.

Utilize version tracking tools: Tools like Dependabot or Renovate can monitor your project’s dependencies and
automatically create pull requests with updates.

Use identification and monitoring tools: Security tools like Black Duck SCA can scan your codebase for
vulnerabilities in open source components and alert you when updates with security fixes are available.

There’s only one viable solution to stay aware of the open source you use. You need an accurate, comprehensive
inventory of open source, as well as automated processes to monitor vulnerabilities, upgrades, and the overall health of
the open source in your software.

2025 Open Source Security and Risk Analysis report  |  26

Conclusion: The More Things Change

“Risk comes from not knowing what you’re doing.”

—Warren Buffet and Charles Munger

For the past 10 years, a continuing theme of Black Duck’s “Open Source Security and Risk Analysis” report has been
“Do you know what’s in your code?” The numbers have changed since 2015—in most instances, they have significantly
increased—but the question remains the same.

Whatever end of the software supply chain you reside on—
whether you’re at the top or bottom of the funnel, whether
your organization develops or uses software from different
vendors, whether that software is on-premises, in the cloud,
embedded, or on a mobile device—it’s a near-certainty that
your software contains open source code. Do you know
exactly what those OSS components are and whether they
pose security, code quality, or license risks?

When 97% of code contains open source, visibility into your
code needs to be a priority. When 91% of codebases are
using open source far behind the current version, everyone
needs to do better in keeping their code up-to-date, especially
when it comes to popular open source components.

•  OSS is overwhelmingly present in modern software:

Figure 8: Detail from the 2015 OSSRA Report

Ninety-seven percent of the commercial codebases we
evaluated contained open source, with some industry
codebases reaching 100%. Is your company in one of those high-risk sectors?

•  You can’t manage open source manually: The number of open source files in the average application has tripled in
the last four years. Transitive dependencies are a major factor in code complexity. Sixty-four percent of open source
components identified in our scans were transitive dependencies.

•  Security vulnerabilities are a pervasive risk: The majority (81%) of assessed codebases had high- or critical-risk

vulnerabilities. Many of these vulnerabilities stem from outdated open source components.

•  Many of those vulnerabilities also stem from specific coding weaknesses: Seventy-one percent of the overall open

source vulnerabilities we found were linked to improper input validation.

•  Software Bills of Materials are essential for visibility into your code: SBOMs are critical for managing risk,

vulnerabilities, license compliance, software quality, and M&A due diligence.

•  Licensing risks are a common issue: More than half of audited codebases (56%) contained license conflicts, often
due to incompatible transitive dependencies. Thirty-three percent of all codebases had OSS components with no
license or a customized license.

•  Outdated components present a major challenge: Most audited codebases (91%) contain outdated components,

with 90% of the codebases containing components more than 10 versions behind the most current version.

2025 Open Source Security and Risk Analysis report  |  27

Key Recommendations

Implement SCA: Use SCA tools to generate SBOMs, identify vulnerabilities, and manage
license compliance.

Prioritize risk management: Focus on high-risk vulnerabilities and license issues that can
impact the most important aspects of your business.

Regularly update OSS: Stay up-to-date with security advisories, and promptly patch
vulnerable software, particularly jQuery and other popular libraries.

Establish secure coding practices: Focus on input validation, sanitization, and regular
security testing of third-party code.

Monitor OSS maintenance: Stay aware of updates to open source components by tracking
project websites, using package managers, and utilizing automated security services.

Create an SBOM: Develop a detailed SBOM that lists all open source components in your
code, including licenses, versions, and provenance.

Integrate OSS management into your SDLC: Incorporate open source management into your
secure software development framework, following best practices such as those outlined by
CISA and NIST.

If you’re planning an M&A, utilize Black Duck audits to vet your acquisitions: You need
a trusted third party with access to the target’s source code and the tools and expertise to
provide the necessary insights in these high-risk situations.

As we wrote at the beginning of this report, while open source software offers numerous benefits, it also introduces
significant risks that must be actively managed. Organizations need comprehensive visibility into their software supply
chains, robust security practices, and a proactive approach to licensing and maintenance to avoid potential issues.
Implementing SCA tools, SBOMs, and proper hygiene practices is not optional—it’s a necessity in today’s software
landscape. By adopting our recommendations, organizations can mitigate risks and continue to leverage the benefits of
open source software safely and effectively.

You need to know without question what’s in your code.

2025 Open Source Security and Risk Analysis report  |  28

Contributors

The 2025 “Open Source Security and Risk Analysis” report was produced by Black Duck, with contributions from our
Audit, CyRC, Professional Services, and Marketing teams.

Special thanks to Nancy Bernstein, Conor Brolly, Kevin Collins, Scott Handy, Clement Pang, Merin McDonell, Mike
McGuire, Phil Odence, Liz Samet, Mark Van Elderen, and Jack Taylor.

Fred Bals scripsit hoc

About Black Duck

Black Duck® meets the board-level risks of modern software with True Scale
Application Security, ensuring uncompromised trust in software for the regulated,
AI-powered world. Only Black Duck solutions free organizations from tradeoffs
between speed, accuracy, and compliance at scale while eliminating security,
regulatory, and licensing risks.  Whether in the cloud or on premises, Black Duck is
the only choice for securing mission-critical software everywhere code happens.
With Black Duck, security leaders can make smarter decisions and unleash
business innovation with confidence. Learn more at www.blackduck.com.

©2025 Black Duck Software, Inc. All rights reserved. Black Duck is a trademark of Black Duck Software, Inc. in the United States and other countries. All other names
mentioned herein are trademarks or registered trademarks of their respective owners. April 2025

2025 Open Source Security and Risk Analysis report  |  29

©2024 Black Duck Software, Inc. All rights reserved. Black Duck is a trademark of Black Duck Software, Inc. in the United States and other countries. All other names
mentioned herein are trademarks or registered trademarks of their respective owners. April 2025

2025 Open Source Security and Risk Analysis report  |  30