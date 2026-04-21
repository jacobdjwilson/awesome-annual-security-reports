# 2022 OPEN SOURCE SECURITY AND RISK ANALYSIS REPORT

## Table of Contents
- [Introduction](#introduction)
- [About the 2022 Open Source Security and Risk Analysis Report and the CyRC](#about-the-2022-open-source-security-and-risk-analysis-report-and-the-cyrc)
- [Overview](#overview)
- [Vulnerabilities and Security](#vulnerabilities-and-security)
- [Licensing](#licensing)
- [Open Source Maintenance](#open-source-maintenance)
- [Conclusion](#conclusion)

---

## Introduction

### About the 2022 Open Source Security and Risk Analysis Report and the CyRC
Welcome to the 2022 Open Source Security and Risk Analysis (OSSRA) report. The 7th edition of OSSRA delivers our annual in-depth look at the current state of open source security, compliance, licensing, and code quality risks in commercial software. Synopsys shares these findings to help security, legal, risk, and development teams better understand the security and license risk landscape. The data in this report is possible thanks to the Synopsys Cybersecurity Research Center (CyRC), whose mission is the publication of security advisories and research that help organizations better develop and consume secure, high-quality software.

This year, CyRC researchers examined anonymized findings from over 2,400 commercial codebases across 17 industries. The growth in the number of audited codebases—64% larger than last year’s—reflects the significant increase in merger and acquisition (M&A) transactions throughout 2021. According to Morgan Stanley, 2021 saw a record number of M&A deals, with a total value of more than $4.9 trillion.[^1] The growth in audits can also be attributed to a recognition that software is often a key element of a company’s intellectual property (IP). Consequently, acquirers in M&A deals want to understand what risk may be associated with the software they’re acquiring—specifically risk around licensing, security, and the quality of the open source used in that software.

For nearly 20 years, development, security, and legal teams around the world have placed their trust in Black Duck® software composition analysis (SCA) solutions and audit services. Our SCA offerings help organizations effectively identify and track open source code and automate open source policy enforcement across development environments.

Each year, our Audit Services team audits thousands of codebases for our customers, mainly to identify a range of software risks in M&A transactions. Black Duck audits provide a comprehensive and up-to-date software Bill of Materials (SBOM) covering the open source, third-party code, web services, and APIs in an application. The Audit Services team relies on data from the Black Duck KnowledgeBase™ to identify potential license compliance and security risks. The KnowledgeBase contains information for nearly 200 million versions of over 5.1 million open source components that use data from more than 26,000 unique sources. This data is curated and validated by the CyRC.

This analysis of 2021 audit data was conducted by the CyRC’s Belfast team. In addition to their role in collecting and analyzing the data used for this report, the team issues Synopsys Black Duck Security Advisories. These detailed notifications deliver enhanced vulnerability information directly to commercial Black Duck customers.

Whatever industry you’re in, OSSRA data indicates that it’s prudent to assume open source will be part of the software your business builds and uses. As our findings underscore, open source is everywhere, as is the need to properly manage its use. Open source is the foundation for every application we rely on today. Identifying, tracking, and managing open source is critical for effective software security. This report offers key recommendations to help developers and consumers better understand the open source ecosystem and manage open source responsibly.

> Open Source is Everywhere, As Is The Need To Properly Manage ITS USE

---

## Overview

![2022 in review infographic showing statistics on open source usage, vulnerabilities, and maintenance]

### Terminology
- **Codebase**: The code and associated libraries that make up an application or service.
- **Black Duck Security Advisory (BDSA)**: A classification of open source vulnerabilities identified by the CyRC security research team.
- **Software component**: Prewritten code that developers can add to their software.
- **Dependency**: A software component becomes a dependency when other software uses it.
- **Open source license**: A set of terms and conditions stating end-user obligations when an open source component is used.
- **Permissive license**: Allows use with few restrictions, generally requiring attribution and liability disclaimer.
- **Copyleft license**: Includes a reciprocity obligation stating that derivative works must be released under the same terms.
- **Software Bill of Materials (SBOM)**: A comprehensive inventory of the open source dependencies in a codebase.
- **Software composition analysis (SCA)**: A type of application security tool used to automate the process of open source software management.
- **Apache Log4j2 vulnerabilities**: A set of vulnerabilities (e.g., Log4Shell) in the widely used Java logging utility.
- **Executive Order 14028**: A U.S. order titled “Improving the Nation’s Cybersecurity” that promotes the use of SBOMs to improve supply chain security.

### Industries in the OSSRA
![Chart showing percentage of scanned codebases containing open source across 17 industries]

---

## Vulnerabilities and Security

### Open source vulnerabilities and security
Of the 2,409 codebases analyzed by Black Duck Audit Services for this year’s report, 97% contained open source. Eighty-one percent contained at least one known open source vulnerability, a minimal decrease of 3% from the findings of the 2021 OSSRA.

We found a more dramatic decrease in the number of codebases containing at least one high-risk open source vulnerability; only 49% of this year’s audited codebases contained at least one high-risk vulnerability, compared to 60% last year.

![Chart showing percentage of codebases containing vulnerable components from 2016 to 2021]

### 2021: The Year of Open Source
Although the decrease in high-risk vulnerabilities found in the audits was encouraging, 2021 was still a year filled with open source issues including supply chain attacks,[^2] hacker exploits of Docker images,[^3] and a developer sabotaging their own open source libraries.[^4] Most notably, 2021 ended with a zero-day vulnerability in the popular Apache Log4j utility.

### Vulnerabilities in Industries
We found that 4 of the 17 industry sectors—Computer Hardware and Semiconductors, Cybersecurity, Energy and Clean Tech, and Internet of Things—contained open source in 100% of their codebases.

### The Executive Order and Supply Chain Security
In light of the uptick in security breaches this year, President Biden issued Executive Order 14028, outlining how companies doing business with the federal government should secure their software. The only way to minimize risk in the software supply chain is with a comprehensive and exhaustive SBOM.

### The top 10 vulnerabilities
Several vulnerabilities discovered in last year’s audits surfaced again this year. jQuery remains the #1 component containing vulnerabilities, found in 43% of audited codebases.

---

## Licensing

Black Duck Audit Services found that 53% of the 2021 audited codebases contained open source with license conflicts, a dramatic decrease from the 65% seen in 2020.

### Understanding license risk
Potential license risk arises when a codebase includes open source with licenses that appear to conflict with the overall license of the codebase. Twenty percent of the audited codebases contained open source with no license or a custom license.

---

## Open Source Maintenance

### Maintenance by Open Source Developers
Of the more than 2,000 codebases examined that included risk assessments, 88% contained open source that had no development activity in the last two years.

### Maintenance by Open Source Consumers
Of the more than 2,000 codebases examined, 88% contained outdated versions of open source components. That is, an update or patch was available but had not been applied.

---

## Conclusion

### A Prescription for the “Witches’ Brew” of Open Source
A core principle to any security program is the need to know what’s in the code (the “brew”) you build or use. Without this information, you’re left in the dark. Effective management of open source begins with the identification of open source.

### A Software Bill of Materials
The concept of a software Bill of Materials (SBOM) derives from manufacturing. An SBOM of open source components allows you to pinpoint at-risk components quickly and prioritize remediation appropriately. In the world of 2022, where 97% of commercial code contains open source, visibility into the open source components used in an application needs to be considered a mandatory and minimum requirement.

---

### References
[^1]: Ian Forsyth, Global M&A momentum to keep going like a train, the Press and Journal, 2/25/2022.
[^2]: Eran Orzel, 2021 Software Supply Chain Security Report, Argon Security, 2021.
[^3]: CVEdetails.com, Docker security vulnerabilities, 2021.
[^4]: Dominick Reuter, A developer sabotaged their own open-source libraries, breaking thousands of apps, in apparent protest of mega-corporations, Business Insider, 1/10/2022.