# State of Attacks 2025

## Table of Contents
- [Introduction](#introduction)
- [Executive summary](#executive-summary)
- [Prominent changes](#prominent-changes)
- [General findings](#general-findings)
- [Top weaknesses](#top-weaknesses)
- [Vulnerability remediation](#vulnerability-remediation)
- [Vulnerability remediation support](#vulnerability-remediation-support)

---

## Introduction

At Fluid Attacks, as an application security (AppSec) company, we are dedicated to helping our clients identify, prioritize, and remediate security vulnerabilities in their software products by integrating various automated tools, artificial intelligence models, and a highly certified team of pentesters.

In 2024, we assessed and contributed to the security of our clients' systems through our comprehensive Continuous Hacking solution during the entire software development lifecycle (SDLC). When we refer to a system, it may include all three, two, or just one of the following targets of evaluation: application source code, running application, and infrastructure.*

The State of Attacks 2025 report, like those from previous years, can help you benchmark and improve your company's cybersecurity posture. Many of the conclusions we drew after reviewing a full year of data from security testing and management can serve you as a guide for setting more effective goals, focusing on secure development practices and rapid vulnerability remediation to protect your systems, data, operations, and users.

Data collection period: Jan 1 - Dec 31, 2024
*Hereinafter, "source code," "application," and "infrastructure," respectively.

### Focus on risk exposure rather than the number of vulnerabilities

Before delving into the findings for 2024 as a whole, it is important to note that at Fluid Attacks, we recognize that the fact that a system has few vulnerabilities is not synonymous with a high level of security. The key is to keep the risk exposure to a minimum. In other words, for example, having ten vulnerabilities with a CVSS score of 1.0 in a system does not represent the same degree of risk exposure as having one vulnerability with a score of 10.0. Based on this reasoning, we developed the CVSSF metric, a modification of the CVSS score that allows organizations to prioritize their vulnerability remediation efforts more effectively.

![Illustration of balance scale comparing ten low-risk vulnerabilities to one high-risk vulnerability]

The CVSSF overcomes many of the shortcomings of the CVSS, such as aggregation and comparison, providing clearer visibility of the magnitude of risk exposure. Thus, following the example in the previous paragraph and the CVSSF equation,* as we can see in the illustration, those ten vulnerabilities on the left side of the balance merely reach a CVSSF of 0.2. In contrast, the vulnerability on the right has a huge value of 4,096.0, a comparison of values closer to the reality of risks.

*CVSSF = 4^(CVSS-4)

---

## Executive summary

Check out the most impactful results

[1] The number of systems we assessed for security using Continuous Hacking in 2024 grew by 27.6% in comparison to 2023.

[2] Although we reported 59.3% more vulnerabilities than the previous year, total identified risk exposure (CVSSF units) decreased by 3.8%.

[3] This year, on average, organizations took 18.5% less time to remediate their security vulnerabilities. Moreover, the mean time to remediate critical-severity issues decreased by a considerable 65%.

[4] Vulnerability remediation in systems that broke the build took, on average, 50% less time compared to those that did not.

[5] The remediation rate for systems that broke the build was 62.4%, while for those that did not, it was 31.5%.

[6] Our pentesters, compared to our automated tools, reported 71% of the total risk exposure.

[7] Almost 99% of critical-severity vulnerabilities were detected by our pentesters (our tool had already found the rest).

[8] The most persistent security weakness among the assessed systems was "Unverifiable files."

[9] The weakness that represented the highest total risk exposure during the year was "Improper authorization control for web services."

[10] High- and critical-severity vulnerabilities showed the best cumulative remediation rates at the end of the year, with 57.4% and 73.2%, respectively.

---

## Prominent changes

### Assessed systems
The number of systems we evaluated with Continuous Hacking increased by 27.6% compared to the previous year.* In addition, 57.6% of the systems under assessment with our solution in 2023 continued to be evaluated in 2024, a year in which nearly 55% of the systems were new.

![Graphic showing 27.6% increase in Continuous Hacking]

*We emphasize that this is a comparison limited to the Continuous Hacking solution. In 2023, there were still a few systems being tested with our One-Shot Hacking solution, no longer offered.

### Risk exposure
In 2024, from Continuous Hacking, we reported a total risk exposure 3.8% lower than in 2023. It dropped from about 32.5 million to 31.3 million units (following our CVSSF metric). Accordingly, the mean and median risk exposure per system decreased by 24.6% and 33.2%, respectively.

### High and critical severity vulnerabilities
62.3% of all systems under assessment showed at least one high- or critical-severity vulnerability, representing a reduction with respect to the previous year, when that figure stood at 66.6%.

### Manual detection methods
We constantly improve our tools in terms of their scope and vulnerability detection capabilities, yet our team of pentesters continues to achieve much higher results in terms of risk exposure and critical-severity vulnerabilities identified.

### Vulnerability remediation
The mean time to remediate (MTTR) vulnerabilities was about 55 days. This is a reduction of almost 19% compared with the 68 days of the previous year. Furthermore, it should be noted that the MTTR for critical severity vulnerabilities was reduced by a significant 65%.

---

## General findings

- Reported vulnerabilities: 872,612
- Mean number of vulnerabilities by system: 824
- Reported risk exposure (CVSSF units): 31,295,535
- Mean risk exposure by system: 29,552

### Risk exposure by severity
Nearly all of the risk exposure in the systems evaluated, i.e., 91.6%, was due to high- and critical-severity vulnerabilities.

| Severity | Total vulnerabilities | Total risk exposure |
| :--- | :--- | :--- |
| Critical | 10,802 | 17,456,578.79 |
| High | 34,009 | 11,197,833.43 |
| Medium | 126,110 | 2,620,324.37 |
| Low | 701,691 | 20,798.08 |

![Chart: Vulnerabilities and risk exposure by severity]

---

## Top weaknesses

### Top 10 weaknesses by risk exposure
Starting in the second half of 2024, we decided to discontinue the weakness categories "011. Use of software with known vulnerabilities," "393. Use of software with known vulnerabilities in development," and "435. Use of software with known vulnerabilities in environments."

| Weakness | Systems | Persistence | Exposure | MEx |
| :--- | :--- | :--- | :--- | :--- |
| 039. Improper authorization control for web services | 263 | 10,356 | 8,490,025.9 | 819.8 |
| 006. Authentication mechanism absence or evasion | 161 | 7,463 | 7,690,775.4 | 1,030.5 |
| 096. Insecure deserialization | 173 | 13,262 | 1,947,603.2 | 146.9 |
| 100. Server-side request forgery (SSRF) | 304 | 7,053 | 1,724,486.6 | 244.5 |
| 359. Sensitive information in source code - Credentials | 331 | 13,415 | 893,774.0 | 66.6 |

---

## Vulnerability remediation

Less than half of the identified vulnerabilities were remediated. Systems that broke the build had a remediation rate of 62.4% by the end of the year, significantly higher than those that did not, which had a rate of 31.5%.

### Time to remediate
- Breaking the build: 28 median days
- Not breaking the build: 56 median days

---

## Vulnerability remediation support

At Fluid Attacks, we offer different support channels for vulnerability remediation. The main ones are Autofix, Custom Fix, and Talk to a Pentester.

- 34.7% of systems used "Talk to a Pentester."

We invite you to take full advantage of this and the other support channels we offer, which can undoubtedly help you improve your remediation rates and times, thereby benefiting your organization's security posture.