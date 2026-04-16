# State of Attacks 2026

## Table of Contents
- [Introduction](#introduction)
- [Executive Summary](#executive-summary)
- [Prominent Changes](#prominent-changes)
- [General Findings](#general-findings)
- [Top Weaknesses](#top-weaknesses)
- [Vulnerability Remediation](#vulnerability-remediation)
- [Vulnerability Remediation Support](#vulnerability-remediation-support)

---

## Introduction

At Fluid Attacks, we help organizations map and understand their attack surface through continuous security assessments. By combining AI, automated tools, and a team of highly certified pentesters, we uncover vulnerabilities across code and environments, helping companies reduce their risk exposure and strengthen their security posture.

In 2025, we tested our clients' systems and contributed to their security throughout the entire software development lifecycle using our Continuous Hacking solution. When we talk about a "system" in this report, we mean any of the three targets of evaluation or their combination: source code, running application*, and infrastructure.

The State of Attacks 2026 report is our annual look at a full year of security testing data.** It is designed to help you benchmark your organization's security posture and set more effective goals. The patterns we've uncovered can guide you toward more secure development practices and faster remediation, ultimately protecting your users, systems, and data.

*Data collection period: January 1 - December 31, 2025*

*\*Throughout this report, we refer to this target simply as "application".*
*\*\*Due to our recent migration to a new data infrastructure, data shown for the year 2024 might differ from the previous report.*

### Risk exposure matters more than vulnerability count
As a reminder, having fewer vulnerabilities does not mean greater security; what matters is keeping a low risk exposure. A system with ten vulnerabilities scored at CVSS 1.0 each isn't nearly as risky as a system with a single CVSS 10.0 vulnerability. But raw CVSS scores don't make that comparison easy, which is why we developed the CVSSF metric, our adjustment of the standard CVSS score. It is designed to solve its biggest limitations: poor aggregation and difficulty comparing across systems.

Using our example and the CVSSF equation,* the difference becomes stark and closer to reality. Those ten low-severity vulnerabilities add up to a CVSSF of just 0.2. The single critical vulnerability? A CVSSF of 4,096.

*CVSSF = 4^(CVSS-4)

---

## Executive Summary

Here are the most impactful results[1]:

1. The vulnerability remediation rate climbed to 62.2% by the end of 2025, a 21.2 percentage point increase over 2024.[2]
2. Our GenAI (Autofix and Custom Fix) was used to help with vulnerability remediation in 54% of the systems.[3][4]
3. Our IDE plugin and MCP users remediated on average twice as much as nonusers.
4. We reported 34% more exposure and 45% more vulnerabilities on average per system this year.[5]
5. The number of systems where we found high- and critical-severity vulnerabilities grew by 26%.[6]
6. The mean time to remediate critical vulnerabilities keeps decreasing! This year, it decreased by 18%.[7]
7. Teams that used our CI Gate remediated vulnerabilities 27% faster, on average, than those that didn't use it.[8]
8. Systems that used our CI Gate achieved a 72% remediation rate, compared to 58% for those that didn't use it.[9][10]
9. Our tools, including our new AI SAST, detected 55.8% of the total risk exposure in the systems assessed.
10. Manual testing detected an average of risk exposure 5 times higher compared to the tools.[11]
11. While our tools are constantly improving, our pentesters add a vital layer of depth: they detected 90% of risk exposure from critical vulnerabilities.[12]
12. Critical vulnerabilities had the best cumulative remediation rate by year's end, with 63.8%.

While AI-driven development is improving remediation efficiency, the attack surface is expanding rapidly in parallel. This trend suggests that despite our gains in speed, the overall volume of new code continues to increase total risk exposure.

---

## Prominent Changes

### Risk exposure
In 2025, the risk exposure detected per system increased, with the mean rising 8.5% and the median 33.5%.

### High- and critical-severity vulnerabilities
70% of assessed systems had at least one high- or critical-severity vulnerability—up from 53.3% in 2024.

| Rating | CVSSv4.0 score |
| :--- | :--- |
| Critical | 9.0 - 10.0 |
| High | 7.0 - 8.9 |
| Medium | 4.0 - 6.9 |
| Low | 0.1 - 3.9 |
| None | 0.0 |

### Manual vs. automated detection methods
Our tools identified 55.8% of total risk exposure this year, reflecting our continued work improving them. Moreover, our pentesters found most of the riskiest vulnerabilities, reporting 87% of critical-severity findings.

### Vulnerability remediation
Mean time to remediate (MTTR) for critical-severity vulnerabilities dropped 17.5%. As in previous years, teams that broke the build (i.e., used our CI Gate) remediated faster than those that didn't. This year, the median remediation time for build breakers dropped from 32 days to 21.

*Time to remediate: Time elapsed between the reporting of a vulnerability and its remediation.*
*Break the build: Security control for CI pipelines in which our CI Gate interrupts software deployment whenever there are still unaccepted vulnerabilities in the product.*

---

## General Findings

### Risk exposure by severity
High- and critical-severity vulnerabilities accounted for 79.9% of total risk exposure. These represent just 4.5% of all vulnerabilities identified, yet they carried 3 times more risk than the remaining 95.5%.

*   Reported risk exposure (CVSSF units): 27,440,146
*   Mean risk exposure per system: 31,041
*   Reported vulnerabilities: 1,119,396
*   Mean number of vulnerabilities per system: 1,266

| Severity | Total vulnerabilities | Total risk exposure |
| :--- | :--- | :--- |
| Critical | 5,609 | 8,666,452.9 |
| High | 44,886 | 13,249,647.1 |
| Medium | 261,732 | 5,494,206.7 |
| Low | 807,169 | 29,839.2 |

### Risk exposure and vulnerabilities by severity
For source code and applications, our most requested targets, low- and medium-severity vulnerabilities made up 95% of all findings (97.1% for applications, 95.3% for source code). But high- and critical-severity vulnerabilities dominated risk exposure, ranging from 80% to 99% of total risk exposure across all targets, including infrastructure.

| Target of evaluation | Total vulnerabilities | Total risk exposure |
| :--- | :--- | :--- |
| Source code | 978,820 | 23,530,544.26 |
| Application | 140,551 | 3,903,585.51 |
| Infrastructure | - | 256,016.17 |

### Risk exposure by detection method
*   **Automatic** (SAST, AI SAST⁺, SCA, DAST, CSPM): 55.8% (15,302,799.63 units)
*   **Manual** (PTaaS, SCR, RE): 44.2% (12,137,346.3 units)

*⁺AI SAST was introduced in Q4 2025*

Vulnerabilities found by our automated tools averaged 15.5 CVSSF units. Those found by our pentesters averaged 93.2 units, six times as much. Our pentesters continue to outperform automation when it comes to uncovering risk linked to critical-severity vulnerabilities.

### Vulnerabilities by detection method
Our automated tools identified 88.4% of vulnerabilities. Considering only the 50,477 high- and critical-severity vulnerabilities found in 2025, tools detected 73.4%. But for critical-severity vulnerabilities alone, 87% were identified through manual review.

---

## Top Weaknesses

### Top 10 weaknesses by risk exposure
"Authentication mechanism absence or evasion" topped this ranking, accounting for 19.1% of total risk exposure. Together, the top 10 weaknesses contributed 68.4% of overall risk exposure.

| Weakness | % Systems | Persistence | Exposure | MEx |
| :--- | :--- | :--- | :--- | :--- |
| 006. Authentication mechanism absence or evasion | 32.9 | 8,515 | 5,233,569.47 | 614.63 |
| 039. Improper authorization control for web services | 47.6 | 10,198 | 2,597,472.45 | 254.71 |
| 184. Lack of data validation | 64.5 | 40,060 | 2,134,129.46 | 53.27 |
| 390. Prototype pollution | 53.1 | 41,131 | 1,934,665.09 | 47.04 |
| 034. Insecure generation of random numbers | 48.3 | 10,197 | 1,687,058.57 | 165.45 |
| 211. Asymmetric denial of service - ReDoS | 61.8 | 82,079 | 1,427,860.84 | 17.41 |
| 100. Server-side request forgery (SSRF) | 50.1 | 14,266 | 1,207,683.75 | 84.65 |
| 359. Sensitive information in source code - Credentials | 37.4 | 7,791 | 877,409.08 | 112.62 |
| 2002. Asymmetric denial of service | 63.1 | 35,530 | 863,976.08 | 24.32 |
| 441. Non-encrypted confidential information - Azure | 4.8 | 1,789 | 809,671.94 | 452.58 |

*Weakness: The category, while the vulnerability is the particular case with a specific location that belongs to the category.*
*Persistence: Number of vulnerabilities identified belonging to the category.*
*MEx: Mean risk exposure.*

---

## Vulnerability Remediation

### All vulnerabilities
*   Remediated: 62.2%
*   In progress: 0.9%
*   Accepted: 4.1%
*   New: 49.0%

Our clients remediated nearly two-thirds of all vulnerabilities. Systems that used our CI Gate reached a 72.2% remediation rate by year's end, versus 58% for systems that didn't use it.

### Time to remediate
Comparing medians, teams remediated vulnerabilities 26.7% faster in systems that used our CI Gate (broke the build) than in those that didn't. Ideally, higher severity means faster remediation. Critical-severity vulnerabilities were remediated 36% (mean) and 50% (median) faster than low-severity ones.

### Remediation and IDE plugins adoption
23% of our clients used our IDE plugins. Clients who used our plugins had a mean remediation rate of 55.4%, versus 28.1% for those who didn't.

### Remediation with custom prioritization criteria
Around 2% of our clients set vulnerability prioritization criteria in a different arrangement to the default. Clients with a custom arrangement had a mean remediation rate of 64.4%, versus 34% for those using the default.

---

## Vulnerability Remediation Support

*   53.6% of systems used Autofix and Custom Fix.
*   24.5% of systems used Talk to a Pentester.

We offer several support channels for vulnerability remediation. The main ones are Autofix, Custom Fix, and Talk to a Pentester. The first two use generative AI in the IDE extensions, platform or both: Autofix provides automatic, suggested fixes, while Custom Fix offers comprehensive step-by-step guides. Talk to a Pentester, available only on the Advanced plan, lets you schedule 30-minute calls with our pentesters to work through complex vulnerabilities.

Autofix and Custom Fix were used in more than half the systems; Custom Fix was far more common (93% of those systems). These tools were used to help with mostly low- and medium-severity vulnerabilities.

![Image description: Chart showing the distribution of support tool usage across systems.]