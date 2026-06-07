# API-Threat-Stats-Report 2025

## Table of Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Spotlight on Agentic AI Security](#spotlight-on-agentic-ai-security)
- [Top 5 API Breaches in Q1 2025](#top-5-api-breaches-in-q1-2025)
- [API Vulnerability Trends](#api-vulnerability-trends)
- [Conclusion](#conclusion)
- [About Wallarm](#about-wallarm)

---

## Introduction
Welcome to the Wallarm API threatStats™ report for Q1 2025. These quarterly reports, and their annual counterpart, are designed to track the API threat landscape, identifying trends and changes. Our goal is to provide consistent assessment of how API threats are evolving so that practitioners can be better informed and more effectively defend their organizations.

In the first quarter of 2025, API threats continued to evolve rapidly, fueled by growing complexity in cloud-native infrastructure, the rise of agentic AI systems, and a surge in software supply chain risks. Through this analysis, we’ll uncover patterns and actionable insights that CISOs, security architects, and DevSecOps teams can use to prioritize risk and harden their defenses.

## Methodology
In order to produce this analysis, we’ve examined multiple datasets, using both AI and manual methods to classify conditions. The data includes:

- **CISA Known Exploited Vulnerabilities (KEV)**: The KEV catalog was reviewed in full, tagging vulnerabilities that are API related, and dividing them into modern and legacy APIs.
- **API Breaches**: The dataset includes nine incidents involving misconfigurations, hardcoded secrets, leaked API keys, and CVE exploitation.
- **Vulnerabilities**: We analyzed all published API-related vulnerabilities from Q1 2025. Each entry was mapped to OWASP and API-specific risk categories and scored using CVSS.
- **Agentic AI GitHub Repositories**: New to the threatStats report this quarter, we analyzed 2,869 issues across agentic AI projects, filtering for API-relevant and security-related issues.

## Spotlight on Agentic AI Security
If you’re reading this report and you’re not aware of Agentic AI, you’re in the minority. While the definition isn’t always clear, we tend to label AI models and frameworks capable of autonomous task execution as Agents. And they present new security concerns, particularly around prompt injection, insecure API integrations, and hardcoded credentials.

APIs play a central role in all Agentic AI workflows, but the established cybersecurity standards like CVE and CISA KEV are trailing indicators of the API risk, and overall risk, presented by Agentic AI. In order to get ahead of the proverbial curve on Agentic AI security, we turned to GitHub. We chose to analyze GitHub security issues for Agentic AI repositories from October 2019 through March 2025, using some clever keyword filtering to identify them.

In fact, GitHub security data supports what we hypothesized: AI agent security risk largely stems from APIs. Of the 2,869 security issues analyzed in agentic AI projects, 1,858 (or 65%) were API-related, underscoring the inseparability of agent security and API security.

![Chart showing high volume of API-relevant issues in Agentic AI repositories]

### Remediation Trends
The average time to close a security issue was 42 days, with many fixed within a week. However, some issues remained open for over 90 days, with the longest time to resolution being 1,284 days (approximately 3.5 years). Of the issues analyzed, 716 remain open, accounting for 25% of the total. It seems, not surprisingly, that active repositories are likely to address reported security issues quickly, while a significant percentage will simply ignore them.

It’s clear from this data that agentic AI faces the same security challenges as other types of code. Furthermore, based on this data, AI agents are likely to have a large percentage of API-related vulnerabilities, making API security a clear requirement for Agentic AI security.

## Top 5 API Breaches in Q1 2025
As usual, we analyzed all the API-related breaches that occurred within the quarter. There were a total of 9 qualifying incidents in Q1 2025. Through this analysis, we’ve ranked and shared the top 5.

| RANK | VENDOR | IMPACT | WHAT HAPPENED | WHY IT MATTERS |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Oracle Cloud | 6M Records | An attacker claimed to have exploited CVE-2021-35587, a vulnerability in Oracle Cloud’s log-infrastructure to access keys and passwords.[^1] | This breach shows how a previously known CVE—present in the wild for years—can still lead to massive compromise if patching is incomplete. |
| 2 | DeepSeek | 1M+ Records | A publicly accessible database disclosed API secrets.[^2] | Highlights the importance of database access control, especially when sensitive API keys or secrets are exposed without authentication. |
| 3 | Common Crawl | 11,908 Live Secrets | Common Crawl, a dataset used to train LLMs, was found to contain thousands of live API secrets.[^3] | This breach draws attention to insecure software development practices, particularly around how secrets are managed and stored. |
| 4 | Volkswagen | 800K Records | A weak JWT implementation allowed API access to user and vehicle data.[^4] | Illustrates how a misconfigured API can expose sensitive customer information, even in large, security-conscious enterprises. |
| 5 | NHS UK | Undisclosed | NHS patient data was exposed by Medefer via an unauthenticated API.[^5] | The breach underscores the risks associated with aging infrastructure in critical sectors like healthcare, where legacy APIs are often overlooked. |

[^1]: https://orca.security/
[^2]: https://www.wiz.io/
[^3]: https://cybersecuritynews.com/
[^4]: https://media.ccc.de/
[^5]: https://www.computerweekly.com/

## API Vulnerability Trends
The vulnerability landscape for APIs in Q1 2025 was shaped by classic access control issues and newer risks introduced by cloud-native and AI-powered systems.

- **Volume**: 582 API-related vulnerabilities were disclosed in Q1.
- **Severity**: The average CVSS score was 7.42.

The analysis shows that while there are a variety of security issues in APIs, access control (authentication and authorization) top the list as a category, followed by resource consumption issues.

## Conclusion
The data from Q1 2025 reinforces that APIs are not just part of the attack surface—they are the attack surface. From legacy system exposures to AI-native risks like hardcoded keys and injection vulnerabilities, attackers are targeting APIs as both the entry point and the objective.

### Key Takeaways
1. **Agentic AI = New API Threat Frontier**: Security issues in AI agent repositories on GitHub are widespread, API-heavy, and under-remediated.
2. **Top API Breach Causes**: Misconfiguration, hardcoded secrets, and unauthenticated access are recurring breach drivers.
3. **Threat Type Trends**: Access control is where it’s at! The dominant vulnerabilities center on access control, authentication, and data exposure.
4. **Mitigation Momentum**: With 15 API-related CVEs added to the CISA KEV list this quarter, the trend of API vulnerabilities dominating the exploit landscape continues.

## About Wallarm
Wallarm is the only unified platform for API and agentic AI security successfully deployed in enterprise production environments. Wallarm was founded to protect APIs, and has built a market leading platform for API protection, including API discovery, API abuse prevention, and AI protection. 

Wallarm detects and blocks API attacks across legacy and modern API protocols, including REST, gRPC, GraphQL, SOAP, Websockets, XML-RPC, and more. Wallarm is headquartered in San Francisco, California, and is backed by Toba Capital, Y Combinator, Partech, and other investors.

Learn more at [wallarm.com](https://wallarm.com).