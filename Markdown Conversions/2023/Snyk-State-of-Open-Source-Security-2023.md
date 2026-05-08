# 2023 State of Open Source Security

## Table of Contents
- [Executive Summary](#executive-summary)
- [Introduction](#introduction)
- [Open Source & Supply Chain Security Tools and Processes Not Keeping Pace with Development](#open-source--supply-chain-security-tools-and-processes-not-keeping-pace-with-development)
- [40% of Organizations Still Don’t Use Key Supply Chain Security Technologies Like SCA or SAST](#40-of-organizations-still-dont-use-key-supply-chain-security-technologies-like-sca-or-sast)
- [31% of Respondents Ignore Invisible Risk of Indirect Dependencies](#31-of-respondents-ignore-invisible-risk-of-indirect-dependencies)
- [Security Tooling Has Not Fully Shifted Left: Only 40% of Organizations Have Security Tooling in Their IDE](#security-tooling-has-not-fully-shifted-left-only-40-of-organizations-have-security-tooling-in-their-ide)
- [How Organizations Are Responding: Big Log4Shell Reaction, but SBOM Confusion](#how-organizations-are-responding-big-log4shell-reaction-but-sbom-confusion)
- [Automation and AI Injects Uncertainty, Risk and Opportunity](#automation-and-ai-injects-uncertainty-risk-and-opportunity)
- [Where Open Source Packages are Most Exposed](#where-open-source-packages-are-most-exposed)
- [The Open Source Ecosystem is Making Fixes Faster](#the-open-source-ecosystem-is-making-fixes-faster)
- [Conclusion](#conclusion)
- [Methodology and Respondent Composition](#methodology-and-respondent-composition)

---

## Executive Summary
The "2023 State of Open Source Security Report" explores the adoption of security tools, practices, and technologies and the impact of automation and artificial intelligence (AI) in software development. The findings are based on a survey of technical employees in the United States and anonymized data collected from Snyk product usage. Our research found that, while open source software dominates the technology landscape, security measures and tooling in the software supply chain are lagging behind the pace of development.

Despite most organizations following some best practices, there are significant gaps in adopting security practices and tooling. 62% of survey respondents indicated their organizations apply a software lifecycle assurance process. Yet many organizations still do not use basic security tools; for example, 40% do not use foundational supply chain security technologies like software composition analysis (SCA) and static application security testing (SAST). While transitive software dependencies (primarily open source packages and libraries) are now recognized as a key source of invisible security risk in open source software development, 31% of survey respondents are not monitoring these indirect dependencies.

The Log4Shell incident has had an impact on security behavior. Nearly two-thirds of organizations implemented new tooling or new practices or increased the frequency of security scans in response to Log4Shell. AI and automation are changing the way development teams build software: 92% of organizations indicated they are using AI tooling, and most are using automation of software development security practices. That said, over half of developers are concerned about AI introducing code vulnerabilities. And automation is increasing false positive vulnerability alerts, with 62% of respondents indicating more than a quarter of all reports were false positive. Collectively, these findings paint a picture of software development that is rapidly changing and responding to pressures to improve security but also lagging behind in key areas of supply chain security practices and processes.

## Introduction
Today, Open source software dominates the technology landscape thanks to its ability to boost development speed dramatically. Interconnected and intricate, the open source ecosystem is built on modularity, sharing, and community interconnection. As a crucial part of modern software development, open source has understandably become a favorite target of bad actors. Attackers increasingly seek to exploit vulnerabilities in open source applications, libraries, packages, and tooling. An obvious reason why these artifacts and systems are such attractive targets is that exploiting a single vulnerability can have an impact on many victims, as the compromised code is often widely distributed and used – a key element of the software supply chain.

In late 2021, the Log4Shell vulnerability was discovered in Log4j — the open source logging library used by millions of applications and open source projects. Beyond that headlining vulnerability, bad actors continuously attempt to compromise users of package managers, like npm and Maven, and package repositories like PyPI, which are critical components in the distribution and updating of the broad open source ecosystem. The interconnectedness is so profound that even disgruntled maintainers of small but widely-adopted packages can adversely impact large swathes of the public internet. This is precisely what happened with the left-pad incident when an unhappy maintainer pulled down public repositories for a small JavaScript module that was used for aligning text, causing thousands of applications to cease functioning normally.

With these risks in mind, this report analyzes the current state of software supply chain security, focusing on open source security. Over the past two years, dozens of solutions have emerged, attempting to address different aspects of software supply chain security. Coding assistants powered by artificial intelligence have become commonplace and are often cited as both increasing and decreasing the risks of supply chain attacks. But what progress have we made over the past two years? More specifically, what progress has been made in securing the open source software supply chain, which accounts for the majority of software applications running in the world today?

To answer this question, we extensively surveyed hundreds of technical employees across the United States and analyzed anonymized data collected from Snyk product usage to paint an accurate picture. As part of our research, we asked questions about how organizations use AI and automation, how they ship code, and what types of tools they deploy. Our goal was to gain a broader understanding of the underlying shifts in software development that are likely shaping the future of supply chain security. We hope you'll use our findings to help guide your security programs and methodologies in the coming years.

## Open Source & Supply Chain Security Tools and Processes Not Keeping Pace with Development
![Chart: How often do you audit your codebase for security vulnerabilities?]

This topic requires a detailed exploration of the software development process through the lens of security. Our survey found that software supply chain security broadly, and open source security in particular, remains a work in progress. While the majority of respondents indicate they are following some or many of the best practices, there are considerable lags in the adoption of both practices and tooling in this regard. It is also important to note that open source is now the dominant form of developer tooling software. Over 60% of respondents said their organizations have a developer tool stack comprising 50% or greater open source tools. This is a strong number, considering that many of the most widely used developer tooling, such as package managers npm, Gradle, and Maven Central, and code repository platforms GitHub and GitLab, are proprietary or a mixture of open source and proprietary.

The more frequently that code is changed, the greater the risks of supply chain vulnerabilities — unless secure development best practices are followed. We found that 80% of organizations are shipping code daily or weekly. This is much faster than a few years ago and is likely indicative of the shift towards more modular code architectures built on open source applications and libraries which require constant updates due to their complexities and dependency structures.

As ship speed increases, patch speed needs to increase as well. The faster vulnerabilities are patched, the less risk there is of an attack. Our survey indicated that 66% of organizations can remediate critical open source vulnerabilities within a day, and 27% do so within a few hours. Fast remediation implies strong security, DevOps, developer agility, and responsiveness to potential supply chain risks. There remains room for improvement in code auditing, though; only 27% of organizations continuously audit code for vulnerabilities. Another 28% audit code daily, and 29% audit code weekly. Continuous or high-frequency audits improve safety due to the increasing incidence of zero-day vulnerabilities.

## 40% of Organizations Still Don’t Use Key Supply Chain Security Technologies Like SCA or SAST
![Chart: Which of the following processes does your organization apply?]

Despite cyber attacks hitting records year over year and an increasing number of attacks focusing on open source code, a high percentage of responding organizations still don’t use the two most fundamental supply chain security technologies, software composition analysis (SCA, for open source dependencies) and static application security testing (SAST, for non-public implementations of open source code and proprietary/first-party code). Cloud native security measures, like configuration checks for infrastructure as code tools and secrets scanning, are adopted by even fewer.

Checking the security posture of open source packages is critical for maintaining a secure software supply chain. This is even more important given the rising incidences of package-based attacks, such as person-in-the-middle, dependency confusion, typosquatting, and malicious code insertion. Automated systems to check that packages follow security best practices, such as Snyk Advisor or OpenSSF Scorecard, are the most reliable way to analyze the risk of different packages programmatically. These systems, however, are the least popular methods for checking the safety of open source packages; only 40% of respondents use Snyk Advisor and only 34% use security scorecards.

The most common method is to use information from the registry or package manager. This is an increasingly useful method as more package managers deploy “trusted package” rating systems, but at present, this information often does not disclose key security findings and is rarely programmatic. Other methods used, like looking at ratings, download stats, release frequency, and community activity, are indirect measures that can be gamed and may not be relevant. Particularly surprising is that only 52% of respondents verify that all packages have a “responsible disclosures” policy – which should be table stakes for any package to be used.

## 31% of Respondents Ignore Invisible Risk of Indirect Dependencies
![Chart: Does your company track which open source libraries your applications are using?]
![Chart: How do you (or how does your team) check the safety of the open source packages?]

A critical challenge in supply chain security is monitoring dependencies of third-party open source packages and libraries. Direct dependencies are relatively easy to monitor with simple dependency management tooling. Indirect (transitive) dependencies, which might be buried deep inside other open source applications, are harder to monitor. Indirect dependencies are often transient and potentially nested within other indirect dependencies, often several degrees removed from the direct dependency package or library. Organizations clearly recognize that dependency tracking is critical to security, with 67% of organizations using a tool like Snyk to track direct and transitive dependencies. Another 25% track direct dependencies only. Tracking both direct and indirect dependencies is crucial for maintaining a strong overall application security posture, as demonstrated by Log4Shell.

Tracking indirect dependencies produces a more holistic and accurate view of the entire attack surface, often surfacing hidden supply chain security weaknesses. These weaknesses often cannot be easily remedied due to the fact that nested dependencies are embedded in open source packages and libraries maintained by parties with at least one degree of separation from the direct dependency.

## Security Tooling Has Not Fully Shifted Left: Only 40% of Organizations Have Security Tooling in Their IDE
![Chart: In your organisation, where do developers have security tools integrated into their workflow?]

Shifting security to the left has been a priority for many engineering organizations seeking to proactively improve code security and reduce vulnerabilities that are inadvertently inserted into code during software development. This improves speed and efficiency in the SDLC as fewer builds are blocked in pre-deployment testing and routed back to developers to fix. Shifting left also remains unfinished business as only 40% of respondents indicated that their organization deploys security tooling into IDEs, with an even smaller percentage using them locally on the command line.

The most common locations for security tooling are in build tools and code repositories, both around 65%. Developers do tend to invoke their build tools, but usually only when they are at a significant milestone in code development. Security tooling in the IDE or CLI might be used more frequently than in the build system or code repository during the development process. Locating security tooling in the build tools or in code repositories is a more traditional setup and is less “shifted left” because those tools are frequently controlled by other teams, even if they might be used or invoked by developers.

## How Organizations Are Responding: Big Log4Shell Reaction, but SBOM Confusion
![Chart: How have you or your organization been impacted by an open source supply chain security vulnerability in the past year?]

Between the United States Executive Order on Improving the Nation’s Cybersecurity, additional pending regulation in the European Union (the Cyber Resilience Act), and a steady stream of supply chain attacks, the past year has brought increasing pressure on engineering and security teams to improve software supply chain security broadly and open source security in particular.

The responses to the survey indicate that the software supply chain security crisis is real and impacting organizations in a variety of ways. The strong majority of respondents were impacted by one or more supply chain issues within the past year. In terms of specific impacts, 53% had to patch one or more vulnerabilities and 61% implemented new tooling and practices for supply chain security indicating that many are taking action only after the impacts of a supply chain attack affect them directly.

### 94% of Organizations Made Significant Changes in Response to Log4Shell
![Chart: How did your organization change its open source supply chain security practices after the Log4J incident?]

This mirrored the overall response to Log4Shell, where clearly organizations are responding with significant changes. In response to the incident, 63% of respondents said their organizations increased code scan frequency, 59% added new tooling, and 53% gave dev teams additional training on secure coding practices. Log4Shell also appeared to improve the security hygiene of most organizations; 58% of respondents said they applied required patches more quickly, motivated by Log4Shell. While the incident may have caused short-term chaos as organizations frantically sought to identify and patch nested exposures, the longer-term impact appears to be beneficial: teams have upped their security game at least in part as a direct response to the incident.

Only 4% of respondents said their organization is not doing anything specific to address supply chain security problems. However, beneath this encouraging top line, the actual adoption of software supply chain security best practices appears scattered. To this point, only 53% of organizations have a formal supply chain security program.

### SBOM Confusion: Rapid Growth in Usage but Scattered Correlation
![Chart: Which of the following open source software supply chain security practices has your organisation adopted?]
![Chart: If your organisation uses SBOMs, which tool generates your SBOM?]

Clearly, the message that SBOMs are a useful tool is getting through to engineering and security teams; 42% of respondents are already using SBOMs, and 31% plan to adopt them in the near future, forecasting impressive growth. That said, respondents said they are generating SBOMs from various software development and CI/CD tools, as well as from dedicated supply chain security systems. This may be due to the relative fragmentation in the SBOM technology space. There remain two dueling standards (Cyclone, SPDX) with no accepted standards for interoperability.

## Automation and AI Injects Uncertainty, Risk and Opportunity
![Chart: Has the use of AI code suggestion tools, like GitHub Copilot, Ghostwriter, or ChatGPT, improved your organisation’s code security?]

As the pace of cybersecurity attacks and updates continue to increase, and the attack surface continues to sprawl, an increasing number organizations are turning to automation of security processes to keep up and reduce demand on overburdened developers and AppSec teams. More recently, artificial intelligence for software development has become widely available.

AI code-generating tools have achieved blanket penetration and are now deployed by 92% of organizations. 76.5% of respondents believe that these tools have improved their organization’s code security. Only 14.9% of respondents said the AI tools had introduced “a lot” of vulnerabilities into their code. In contrast, 73% said AI had introduced “very few” or “a moderate amount” of vulnerabilities into their code. Yet, 59% of respondents said they are concerned that AI tools will introduce security vulnerabilities into their code, and 50% are concerned AI will introduce licensing violations into their code.

### False Positives and Automation Overload: 61% of Respondents Say Automation Has Increased False Positives
![Chart: How many vulnerabilities have been introduced into your code by AI coding tools?]

A high percentage of organizations are automating some or all of their security measures in the code pipeline. 64% of organizations have automated code analysis, 61% have automated software update management, 59% have automated testing (unit, security), and 58% have automated secure coding practices (linters, formatting, etc.). Nearly half have automated container and infrastructure configuration scanning. Automation of secrets detection lags at only 38%. Respondents indicated that automated security tooling has considerably increased the rate of false positives in vulnerability reports. Twice as many respondents said security automation had increased false positives, with 60% stating automation had increased false positives versus 30% saying automation had decreased false positives.

## Where Open Source Packages are Most Exposed
![Chart: Ignored Vulns by Ecosystem / 20 or more appearances]

There are many ways to analyze and categorize attack surfaces. Considering that most attacks take advantage of existing vulnerabilities, one way to measure the exposure of attack surface across different open source ecosystems is to look at CVEs which are the most frequently ignored.

For this analysis, we considered vulnerabilities that at least 20 organizations had chosen to ignore (based on Snyk data). With a vast ecosystem of legacy code and a packaging system (.jar files) that frequently obfuscates vulnerabilities and dependencies, it’s no surprise that Java has the largest percentage of ignored vulnerabilities at 42.4%. JavaScript, with its numerous packages – many for minute functions and functionalities – is understandably second, with 30.7% of ignored vulnerabilities. Debian, the Linux distribution family, takes a distant third, at 13.6%.

### Ignored Vulnerability Types: DDoS, Prototype Pollution and Deserialization Dominate
![Chart: Vuln type (with 50 accounts ignoring)]

The type of vulnerabilities ignored by organizations provides useful information on attack surface and risks that are accepted, either consciously or subconsciously. By far, the dominant type of threat among the CVEs ignored by at least 50 accounts were flavors of denial of service (DoS). These vulnerabilities made up 31.3% of all ignored vulnerabilities. Deserialization of untrusted data made up 14.3% of CVEs ignored by over 50 accounts. The third most common, prototype pollution (at 12.5%), mostly impacts the JavaScript community.

## The Open Source Ecosystem is Making Fixes Faster
![Chart: Days to fix (2019-2022)]

While there remains considerable room for improvement in the realm of secure coding practices, the ecosystem appears to be making improvements in reactive security. We tracked TTF (Time-to-Fix) over the past four complete calendar years and found that the average TTF has steadily increased for proprietary applications and steadily decreased for open source applications since 2019. For the first time since we have tracked this metric, TTF for open source applications fell below TTF for proprietary applications.

### Better Scanning of Open Source Code Results in Faster Fixes of Critical Vulnerabilities
![Chart: Average Time to Fix by severity; OSS]

TTF as an aggregate is important data. Equally important is TTF by the severity of the vulnerability. After witnessing a major spike in TTF average of critical and high-priority vulnerabilities in 2019 and 2020, for the past two years it has fallen dramatically. From 2021 to 2022, the average TTF for those two critical designations fell roughly by half – 51% for critical and -49.4% for high-priority vulnerabilities.

### Most Major Open Source Ecosystems Are Making Fixes Faster
![Chart: Avg Ecosystem time to fix]

The TTF did vary across open source ecosystems and declined markedly for the majority of major open source ecosystems tracked by Snyk. The greatest declines in average TTF were in Java and Python, at 50.8% and 43.4%, respectively. The largest total decline in terms of days was in Go and Python, with Go logging a 147-day reduction in average TTF and Python notching a 115-day reduction.

## Conclusion
Open standards and open source projects are critical for enhancing supply chain security through transparency and collaboration. Notably, the Open Source Security Foundation (OpenSSF) consolidates various initiatives, facilitating a unified approach to best practices, standards, and tools.

Over the past few years, technology organizations have made great strides in improving open source and supply chain security. They have learned the lessons of Log4Shell and made adjustments, including more tooling, more training, and greater scan frequency. A majority of organizations are adding basic code security to developer tools, including format checkers and linters. Three out of five organizations are using important security tools like SCA and SAST on a more frequent basis, and that frequency appears to be increasing.

On the flip side, there remains considerable room for improvement in open source security. Concerningly high percentages of organizations are still not using foundational security technologies like SCA and SAST. The constant rising tide of vulnerabilities continues to lead to security backlogs and decisions not to fix vulnerabilities. Part of the challenge here is false positives, which have increased alongside growing security processes and tooling automation.

Overall, we appear to be in a great period of transition, moving from older approaches to newer methods and technologies. Open source supply chain security has clearly come a long way, and we are, in the aggregate, more secure as a community than before.

## Methodology and Respondent Composition
We surveyed 404 respondents from organizations ranging from small companies to very large multinationals. The largest percentage worked at either small companies with less than 100 employees or at companies with between 100 and 10,000 employees. Respondents were all in technical disciplines, including software development, infrastructure, operations, and security. All respondents were working in the United States. For the directly measured portions of the report, we analyzed aggregated, anonymized data from security scans and Snyk product usage. The coverage of this analysis was from April 2022 through March 2023 unless otherwise noted.