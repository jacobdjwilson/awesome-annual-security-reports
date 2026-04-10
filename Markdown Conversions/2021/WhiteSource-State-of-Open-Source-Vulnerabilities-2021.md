# The State of Open Source Security Vulnerabilities
## WhiteSource Annual Report 2021

## Table of Contents
- [Introduction](#introduction)
- [The Number of Open Source Vulnerabilities Continues to Rise](#the-number-of-open-source-vulnerabilities-continues-to-rise)
- [The Open Source Development and Security Communities: More Active Than Ever](#the-open-source-development-and-security-communities-more-active-than-ever)
- [Most Common CWEs in Open Source Components](#most-common-cwes-in-open-source-components)
- [Open Source Vulnerabilities in 2020: Top CWEs](#open-source-vulnerabilities-in-2020-top-cwes)
- [Open Source Vulnerabilities in Top Programming Languages](#open-source-vulnerabilities-in-top-programming-languages)
- [Open Source Vulnerabilities: Severity Breakdown](#open-source-vulnerabilities-severity-breakdown)
- [Final Thoughts](#final-thoughts)

---

## Introduction

2020 presented us all with a set of challenges no one could have expected. The pandemic initially raised a lot of uncertainty in the software development industry. Companies pivoted to remote work practically overnight and faced a series of issues encompassing everything from application security to employee well-being.

Shifting to work from home introduced new security threats. Early on, many organizations’ budgets were put under scrutiny, and many worried that investment plans for application security strategies would be put on the back burner while many industries went into survival mode.

In this report, we analyzed WhiteSource’s open source vulnerabilities database to gain insights on the state of open source security and learn how to best address the challenge of developing secure software products at the speed of DevOps.

## The Number of Open Source Vulnerabilities Continues to Rise

According to the WhiteSource database, aggregated from the NVD, dozens of security advisories, peer-reviewed vulnerability databases, and popular open source issue trackers, the number of published open source software vulnerabilities in 2020 rose once again, by over 50%.

![Chart showing Open Source Vulnerabilities per Year from 2009 to 2020, showing a steady increase peaking at 9,658 in 2020.]

## The Open Source Development and Security Communities: More Active Than Ever

There are a few possible explanations to the sharp increase in the number of known open source vulnerabilities in 2020.

First is increased activity in the open source community. While no one was sure how shifting to remote work would effect developers, it appears that in the first months of the pandemic open source developers were working harder than ever. GitHub reported a sharp increase in open source project creation in March and April 2020. This rise in activity most probably extended to more open source security research.

The addition of CVE Numbering Authorities (CNAs) also contributed to the increase in published vulnerabilities. GitHub Security Labs, launched over a year ago, invested a lot of effort in detecting, fixing, and publishing vulnerabilities in open source components. Since then, more software development organizations have joined the open source community’s efforts to ensure issues are analyzed, fixed, and published as soon as possible.

In addition to the many hands on deck, automation also explains the high number of open source vulnerabilities discovered this year. Security researchers are using automated scanning and detection tools to find vulnerabilities, enabling them to find and fix security issues quickly, and at a greater volume.

In some cases, researchers found multiple CVEs where a common problem affected many projects. Sometimes a single CVE was applied to many projects but other times it was correct for them to each have their own CVE.

## Most Common CWEs in Open Source Components

As AppSec continues to shift left into the design and development phases and responsibility over security is shared with developers, secure coding practices and tools become an important part of the DevSecOps pipeline.

In order to gain insights on secure coding with open source components, we decided to dive deep into the data on the most common CWEs in vulnerable open source components detected in 2020.

![Visual representation of top CWEs: CWE-79, CWE-200, CWE-20, CWE-787, and CWE-125.]

## Open Source Vulnerabilities in 2020: Top CWEs

![Table comparing top CWEs from 2015 to 2020.]

![Table listing the top 10 CWEs in 2020, including XSS, Out-of-bounds Write, Out-of-bounds Read, Improper Input Validation, Information Exposure, Use After Free, SQL Injection, Path Traversal, CSRF, and Integer Overflow.]

While CWE-79 (Cross-site scripting) has been at the top of the list for the past few years, CWE-787 is a new arrival to the top five.

It might seem like CWE-787 came out of nowhere, but it’s actually a descendent of the common CWE-119 (Buffer overflow), which saw a decrease this year. We can also see that CWE-125, another child of CWE-119, is also a prominent issue.

It appears there was an effort to map CVEs directly to weaknesses like CWE-787 and CWE-125 instead of categories like CWE-119. This included a large remapping effort of over 10,000 CVE entries.

Improper Input Validation and Information Exposure are other examples of categories that are being remapped into the more precise weaknesses.

## Open Source Vulnerabilities in Top Programming Languages

Continuing our research into secure coding, we also looked at some of the top programming languages, including how many and what type of open source security vulnerabilities were disclosed per language.

![Table showing top 3 CWEs for various programming languages.]

Cross-site scripting (CWE-79) continues to dominate in most of the programming languages that we looked at, especially those used for web development. Another reason for how common XSS issues are is that they are very easy to detect using automated tools.

We also see that many of the newly discovered CWE-787 Out-of-bounds write vulnerabilities were discovered in C.

![Bar chart comparing vulnerability percentages in C and C++ between 2019 and 2020.]

The increase in Buffer overflow related issues is one of the reasons that C saw so many new vulnerabilities in 2020.

According to GitHub’s 2020 Octoverse, PHP’s popularity is decreasing in the open source community. The decrease in the number of vulnerabilities in PHP is probably a result of decreased community interest.

Go, on the other hand, is gaining popularity along with increased security research. Last year Go vulnerabilities amounted to only 1% of vulnerabilities in all programming languages, compared to 5% in 2020.

Go is a relatively young language, and the rising number of vulnerabilities discovered in Go might also be because many of the Go projects are written from scratch, rather that using open source libraries and components that have been under the security microscope for years.

## Open Source Vulnerabilities: Severity Breakdown

Addressing the sharp rise in the number of open source vulnerabilities published this year is a major challenge for software development organizations. As security debt continues to rise for most, it’s important to find a way to prioritize vulnerabilities remediation.

One parameter that many organizations look to when attempting to decide what to remediate first is the vulnerabilities’ severity score.

We checked the breakdown of open source vulnerabilities’ severity scores to see if this is an effective technique.

![Pie chart showing severity breakdown: Critical 15%, High 38%, Medium 45%, Low 3%.]

The fact that over 50% of new open source security vulnerabilities are rated high or critical doesn’t help security and development teams that rely on severity scores when considering which issues to address first.

Fixing all issues, or even “only” high and critical issues, is an unrealistic plan for teams that want to keep up with the rapid pace of development.

Organizations need to leverage prioritization and remediation tools that target the vulnerabilities that will most impact their systems and business if they want to manage their security debt wisely.

## Final Thoughts

Despite how tumultuous 2020 turned out to be, it turns out application security -- and open source security in particular -- remains a top concern and priority for both the software development industry and the open source community.

The sharp increase in the overall number of open source vulnerabilities published in 2020 is another reminder that open source security must be addressed as an integral part of an organization's AppSec strategy, and requires organizations adopt a set of security practices. These include auto-remediation and a vulnerabilities prioritization strategy, ensuring that the issues that pose the biggest threat are addressed first.