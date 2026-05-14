# THE 2024 TIDELIFT MAINTAINER IMPACT REPORT

November 2024

## Table of Contents
- [Introduction](#introduction)
- [Whose job is it to keep open source secure?](#whose-job-is-it-to-keep-open-source-secure)
- [The impact of paying open source maintainers to keep their projects secure](#the-impact-of-paying-open-source-maintainers-to-keep-their-projects-secure)
- [PART 1: Case story: the business impact of paying open source maintainers to scale real world application security](#part-1-case-story-the-business-impact-of-paying-open-source-maintainers-to-scale-real-world-application-security)
- [PART 2: How paying maintainers improves project security and resilience](#part-2-how-paying-maintainers-improves-project-security-and-resilience)
- [How Tidelift can help](#how-tidelift-can-help)

---

## Introduction

Open source is everywhere. Almost all modern applications contain open source, and in many applications it makes up 70% or more of the code. For good reason: open source speeds up innovation, and it is almost impossible to imagine a world today where applications are developed without it.

But as open source continues to become more ubiquitous each year in enterprise applications, the risks organizations using open source are expected to manage also grow. High profile security vulnerabilities impacting open source, headlined by the Log4Shell and xz utils incidents, have made open source software security a critical board-level issue in many organizations, potentially impacting revenue, data, and customers.

Governments around the world are stepping up efforts to improve cybersecurity and reduce risk to consumer data and national security. Efforts like the Cyber Resilience Act (CRA) and Product Liability Directive (PLD) in the EU and the National Cybersecurity Strategy and White House Executive Order 14028 on Improving the Nation’s Cybersecurity in the United States place new responsibilities on organizations building software applications to ensure their products are secure, and codify paths to pursue damages if they are not. Many organizations already have efforts underway to ensure the software they build in-house complies with these new regulations, but it is still an open question for many how they will keep the open source code that in many cases makes up the majority of their application secure and compliant as well.

## Whose job is it to keep open source secure?

So whose job, exactly, is it to ensure the open source code that most modern applications rely on is secure, well maintained, and resilient?

Many people believe the security and maintenance of open source code is the job of the maintainers who write it, and commercial users do not bear the responsibility for insecure open source software they bring into their applications.

This perception is not only wrong; it is dangerous.

As we’ll share in more detail in this report, much of the open source software our enterprises rely on is built and maintained by volunteer maintainers who aren’t being paid to keep it up to date and secure. Sixty percent of maintainers report they are unpaid hobbyists, and only 12% of maintainers consider themselves professionals who earn most or all of their income from their maintenance work.

Open source code downloaded from the internet is being provided “as is,” which means the user—your organization—is taking responsibility for any issues that arise from its use.

This responsibility is being codified into new cybersecurity regulations like the aforementioned Product Liability Directive in the EU. Here’s a direct quote from the PLD (emphasis ours):

> “Where free and open source software supplied outside the course of a commercial activity is subsequently integrated by a manufacturer as a component into a product in the course of a commercial activity and is thereby placed on the market, it should be liable to hold that manufacturer liable for damage caused by the defectiveness of such software but not the manufacturer of the software because they would not have fulfilled the conditions of placing a product or component on the market.”

In other words, if your organization makes the decision to use an open source component that is later found to be insecure and it results in damages, your organization would be liable for the damages—not the open source maintainer who created the component.

## The impact of paying open source maintainers to keep their projects secure

Open source is an amazing resource, and it is not a realistic option for organizations to quit using open source and expect to stay relevant. A recent Harvard Business School study estimated that it would cost 3.5 times more to build software without utilizing open source. Most organizations can’t wait 3.5 times as long or spend 3.5 times as much to build their applications and still remain competitive in their industry. They need a way to take full advantage of open source while reducing risks to their revenue, data, and customers.

Thankfully there is an answer for how organizations can continue to get the business benefits of open source while still controlling their security risk: paying maintainers to do the important work to ensure their projects follow secure software development practices—and continue to do so into the future.

We wrote this maintainer impact report to share the evidence of the positive security outcomes that organizations can expect to achieve—outcomes that reduce organizational risk and improve operational efficiency—when they invest directly in their open source software supply chain by paying maintainers.

We’ll share this story in two parts. First we’ll share a case story of how one customer improved the security and resilience of an important Python application used to analyze and forecast commercial pricing in a highly regulated industry over a multi-year period while simultaneously saving over $1 million in organizational time and significantly reducing application risk.

Next, we’ll share recent evidence from our 2024 Tidelift state of the open source maintainer report where maintainers report first hand what kinds of security practices they are able to implement when they are paid for their work. We’ll also bring in supporting data from other sources, like the Sonatype State of the Software Supply Chain report and the Atlantic Council report O$$ Security: Does More Money for Open Source Software Mean Better Security?

We’ll end by sharing how Tidelift can help organizations use these findings to decrease their own risk and improve organizational efficiency proactively, while still making optimal use of open source.

---

## PART 1: Case story: the business impact of paying open source maintainers to scale real world application security

What if your team could save $1 million while improving the security and resilience of an application that your company depends on to deliver revenue? Here’s a story about a team that did just that.

As we stated in the introduction, over the past few years organizations have become increasingly focused on improving the security of the open source powering their applications. Vulnerabilities like Log4Shell in 2021 have highlighted the risk to organizations’ revenue, data, and customers that can result from insecure or under-maintained open source packages.

Some industry leaders have pushed for codifying security practices for open source projects, and then measuring how well projects follow these practices. The OpenSSF Scorecard has been the most visible of these efforts. But while a Scorecard score may provide good information about the security, health, and resilience of a package when the data is accurate, it is not actually making the package more secure, healthy, or resilient. The Scorecard is simply a historic snapshot of observable activities.

For this maintainer impact report, we wanted to analyze the impact of paying open source maintainers to implement industry-leading secure software development practices in real world situations, and see if it is making a difference in customers’ bottom line and their ability to increase the velocity of their business.

As a case story, we zeroed in on a Python application that one of our customers uses to analyze and forecast commercial pricing in a competitive, highly regulated industry. We wanted to see how they were able to improve the application’s security and resilience over a two-year period with help from Tidelift and our open source maintainer partners.

Let’s start with the bottom line results: This customer is able to set accurate pricing, drive profitability, and improve their margins because their developers have been able to reduce the organization’s reliance on abandoned, end-of-life, or otherwise insecure open source packages that are costing them time and money.

Specifically, they:
- Saved $1.1 million of organizational time across engineering, legal, and security that would have been spent on requirements research and engineering implementation time
- Reduced application risk by turning 37% of this customer’s independently maintained packages from an “unknown future” to reliably secured and maintained, with a plan in place to grow that percentage to 58% in 2025 and 80% in 2026

### Improving visibility

In 2021, before the customer began to track this application with Tidelift, they had limited visibility into the health, security, and resilience of their open source dependencies. At best, the customer would have visibility into CVEs affecting package releases in the application, alongside information from the OpenSSF Scorecard about package maintenance and discoverable security policies.

After starting to work with Tidelift, their visibility into the health, security, and resilience of their open source software supply chain increased radically. On day one, the customer could answer questions like:
- What are the known CVEs affecting package releases?
- Which of these CVEs are false positives, or don’t affect the way the package is used?
- Which packages have a maintainer available to take in security research? Is security research being ignored?
- Which packages are backed by foundations or corporations?
- Does the package maintainer release patches for known vulnerabilities?
- Which packages have been abandoned?
- What is the abandonment risk from transitive open source packages pulled in by direct dependencies?
- What packages are showing signals that they may go “end-of-life” or be abandoned?

### 100% supplier visibility

![Chart showing the transition from 0% supplier visibility before Tidelift to 100% supplier visibility with Tidelift, broken down by Tidelift-partnered maintainers, corporation-backed, foundation-backed, and no assurances found.]

The company instantly had contractual commitments from the maintainers of 19% of their dependencies who were already being paid by Tidelift to implement enterprise-grade secure software development practices, and continue to keep these practices in place over time. Over the following two years, Tidelift recruited additional maintainers, and now the percentage of packages backed by Tidelift-partnered maintainers is at 29% and continuing to rise.

### 100% risk visibility

![Chart comparing risk visibility before and with Tidelift, showing the reduction of unknown risk and the categorization of packages into known reliable, no security policy, and end of life.]

With Tidelift, they now have 100% risk visibility, with data on other forms of risk beyond security vulnerabilities. Almost half of the packages in the application (48%) are now known to be reliable. Meanwhile, in addition to the 10% of known vulnerable releases, they can also see that 10% of their package versions have been declared end of life, and 32% have no security policy in place.

### Improving security and resilience over time

In 2022, when this customer first came to Tidelift, 22% of the application components were already backed by corporations or foundations. Tidelift has historically focused on providing income primarily to independent open source maintainers rather than those backed by corporations or foundations because, as Tidelift co-founder Luis Villa describes in his blog post *Paying maintainers: the HOWTO*, smaller, independently maintained projects often have fewer avenues for funding.

![Chart showing the percentage of independently maintained open source components in the application with contractual security and maintenance, growing from 24% in 2022 to a forecast of 80% by 2026.]

### Business impact

**Reduced costs**
With an abundance of open source packages available to modern software developers, it may seem like it would be easy to simply remove an open source package that is, or appears to be, abandoned. But it is rarely that easy. The package may be deeply embedded into the application and its dependency graphs, so the rework required may be extensive.

> “We’re just starting to account for the cost of ripping out a package as budgets tighten, and we know it’s large. A proof of concept, legal, security, and other checks are required... A minimal change can drag out 3 months, average 6 months, and replacing a platform or major framework can take a year.” — Senior IT Director

**Reduced risk**
The number of reported CVEs is rapidly increasing each year. Tidelift’s partnered maintainers are the front lines of managing their dependencies on behalf of this customer’s internal development team. Maintainers are able to mark false positives and apply patches—or move off of a dependency when a patch is not available.

![Diagram showing a package dependency graph (aiohttp) and how a paid maintainer ensures the entire graph is safe from risk.]

---

## PART 2: How paying maintainers improves project security and resilience

A growing body of evidence shows that paying maintainers to ensure their projects follow secure software development practices is an effective way to reduce security risk while keeping packages resilient over time.

### Paid maintainers are 55% more likely to implement critical security and maintenance practices than unpaid maintainers

For the 2024 survey, over 400 maintainers participated. Nearly across the board, paid maintainers are 8–26 percentage points (or, on average 55%) more likely to implement many critical security and maintenance practices than unpaid maintainers.

![Chart comparing security practices implemented by professional/semi-professional maintainers vs. unpaid hobbyist maintainers, showing higher adoption rates for 2FA, static analysis, and vulnerability fixes among paid maintainers.]

### Paying maintainers to improve OpenSSF Scorecard scores

In last year’s maintainer impact report, we reported the results of a project where we paid a cohort of maintainers specifically to complete a set of defined tasks that would improve the project’s OpenSSF Scorecard scores. We found that the average score at the end of the project was 7.2 (out of a possible 10) from a starting point of just over 4.

### Other research showing the security benefits of paying maintainers

In their 10th annual State of the Software Supply Chain report, Sonatype shared:
> “Paid maintainers show a clear lead in security practices... components with paid support resolve outstanding vulnerabilities up to 45% faster and have half the vulnerabilities overall.”

The Atlantic Council also reported:
> “In short, these findings indicate with moderate confidence that there is a meaningful connection between more open-source project funding and improved security posture.”

### The bad news: 60% of maintainers are still not paid for their work

The chart below shows that 60% of maintainers categorize themselves as unpaid hobbyists. The percentage of maintainers saying they earn most or all of their income from maintaining projects is only 12%.

![Chart showing the breakdown of maintainer compensation status: 60% unpaid, 24% semi-professional, 12% professional, 4% other.]

### Many maintainers have quit or considered quitting

60% of maintainers have quit or considered quitting maintaining a project. This means that throughout your open source software supply chain, you may have packages that are at risk of becoming insecure or abandoned.

---

## How Tidelift can help

The core thesis of this impact report is that organizations can proactively improve the security and resilience of their software supply chain by paying maintainers of the open source projects they rely on to follow secure software development practices.

Tidelift helps organizations increase the security and resilience of their applications by partnering directly with open source maintainers. Tidelift is the only company that pays them to:
- Implement industry-leading secure software development practices and validate the practices they follow.
- Contractually commit to continue these practices into the future.

Tidelift helps organizations use open source for building their applications with confidence. Our customers:
- Reduce security risk by eliminating attack entry points.
- Improve productivity by reducing vulnerability fire drills.
- Improve application quality by ensuring they build with healthy and resilient open source packages.
- Increase operational efficiency by saving costly manual package evaluation and remediation time.

If you are interested in having a strategic partner in this effort, please reach out to us. We’d love to help.