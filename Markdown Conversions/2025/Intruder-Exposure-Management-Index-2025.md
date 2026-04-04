# 2025 Exposure Management Index

## Table of Contents
- [Introduction](#introduction)
- [Trends in vulnerability detection & response](#trends-in-vulnerability-detection--response)
- [Criticals remain stable, but highs are on the rise](#criticals-remain-stable-but-highs-are-on-the-rise)
- [AI-driven weaponization of “old” CVEs](#ai-driven-weaponization-of-old-cves)
- [Critical issues are being fixed faster](#critical-issues-are-being-fixed-faster)
- [Early signs of the regulatory impact in Europe](#early-signs-of-the-regulatory-impact-in-europe)
- [Size matters: large estates bring risk and delays](#size-matters-large-estates-bring-risk-and-delays)
- [Software sector remediates fastest](#software-sector-remediates-fastest)
- [Vulnerabilities of the year](#vulnerabilities-of-the-year)
- [Apache Tomcat RCE](#apache-tomcat-rce)
- [Fortinet Perimeter Vulnerabilities](#fortinet-perimeter-vulnerabilities)
- [Apache mod_rewrite RCE](#apache-mod_rewrite-rce)
- [Palo Alto Auth Bypass](#palo-alto-auth-bypass)
- [ToolShell](#toolshell)
- [Looking forward](#looking-forward)
- [About Intruder](#about-intruder)

---

## Introduction

Cyber security is no longer a luxury reserved for large enterprises. For everyone but the largest, most well-resourced of enterprises, the security challenge is often structural. They face the same vulnerability landscape as expansive multinationals but with fewer resources, smaller budgets, and leaner teams. Growth often takes precedence over governance, leaving leaders forced to balance the pressure to scale with the risk of exposure.

This first edition of the Intruder Exposure Management Index is part of that effort. By analyzing data from thousands of customers, Intruder aims to give small and midsize companies the threat landscape insights that have historically been locked behind enterprise budgets and external consultants.

2025 has shown how exposure emerges from multiple fronts. AI-assisted development has created new risks as engineering teams rush code outputs into production without sufficient review. Rapid cloud adoption continues to deliver agility but also introduces a host of new potential attack vectors for bad actors to exploit. Shadow IT – unapproved or unknown tools and services that exist without security oversight – can expose sensitive data and expand the attack surface. And small vendors, often part of critical supply chains, remain attractive entry points for attackers seeking leverage over larger organizations.

The 2025 Vulnerability Response Index tracks how 3,000+ small and midsize companies (1-2,000 employees) are exposed to security vulnerabilities, how and why their responses vary, and what can be learned from those patterns.

## Trends in vulnerability detection & response

## Criticals remain stable, but highs are on the rise

### A worsening threat environment.
While a stable number of criticals mean teams aren’t necessarily fighting more fires than they were a year ago, they are being forced to prioritize a meaningfully higher volume of high-severity issues. This expansion is no doubt influenced by attackers reaping the benefits of generative AI in developing exploits. In the wider threat landscape, volumes of both critical and high severity CVEs have surged year-on-year, and are on track to finish the year 28% and 34% higher respectively.

![Chart showing average number of identified high and critical issues in 2024 vs 2025]

### More pressure on already stretched teams.
19% more high-severity vulnerabilities mean that security and engineering teams have 19% more things to worry about, but chances are headcount isn’t keeping up with the expanding threat environment. Scalable security solutions are needed to help lean security teams manage this gap.

## AI-driven weaponization of “old” CVEs

### Old CVEs are the new zero-days.
In 2025, attackers have increasingly focused on exploiting long-known weaknesses – vulnerabilities disclosed one, two, or even three years ago but still left unpatched in many environments.

### AI is increasing attackers’ pace.
Writing new exploits for older CVEs has become easier and faster, with AI-assisted coding lowering the technical barrier to developing reliable attack methods.

### Exposed infrastructure remains especially attractive.
Security appliances such as SSL VPNs, firewalls, and identity providers are deliberately internet-facing and often central to access control. When these systems are vulnerable, exploitation is widespread and highly damaging.

### Beware of ghosts in your back catalog.
This acceleration means the “back catalog” of vulnerabilities is being weaponized at a rate not seen before. For defenders, the effect is that yesterday’s weaknesses remain today’s active threats, and a failure to remediate older issues continues to present a real risk.

> "We are seeing the back catalog of CVEs and vulnerabilities being weaponized with increasing frequency." — Andy Hornegold, VP of Product at Intruder

## Critical issues are being fixed faster

### Executive attention.
High-profile incidents in 2025 appear to have made the cost of delay harder for organizations to ignore. Disruptions to healthcare services, supermarket supply chains, and consumer brands in retail and automotive kept cyber security in the headlines and on boardroom agendas. When leaders see the impact of cyber risks clearly, remediation of critical issues tends to receive more focus.

### Technology and process deliver speed.
Improved year-on-year remediation times suggest that as security processes and technology stacks mature, the organizational capacity to respond quickly to critical issues improves. Any good exposure management solution should provide actionable remediation advice that any engineer can follow and integrations with workflow tools that streamline processes and reduce time to fix.

![Chart comparing critical vulnerability remediation times 2024 vs 2025]

In 2025, 89% of critical vulnerabilities identified have been remediated within 30 days, up from 75% in 2024. North America saw average remediation times improve from 37 to 16 days. High severity vulnerabilities are also being fixed faster.

## Early signs of the regulatory impact in Europe

### Avoiding criticals.
European businesses are outperforming when it comes to avoiding critical vulnerabilities. The average European company is forecasted to have 100 fewer than their North American counterparts this year. While Europeans perform well on criticals, it’s not all good news. They experienced considerably larger volumes of high-severity issues in 2024 (423 vs. 248), and the gap is widening further in 2025.

![Chart showing average number of identified critical vulnerabilities by region]

### Regulation driving cyber hygiene.
Proponents of regulatory frameworks such as DORA, NIS2, and the Cyber Resilience Act are likely to be optimistic about the downward trend in identified critical vulnerabilities in Europe where the regulatory environment is most developed. While it is too early to declare a definitive trend, the data provides an indication that these regulations may be having the desired effect on cyber hygiene and resilience.

## Size matters: large estates bring risk and delays

### Contending with complexity.
Larger, older estates contain more heterogeneous systems, legacy applications, and bespoke integrations. More infrastructure means more to patch, and older systems add layers of complexity and risk.

### Agility wins.
Smaller organizations can act with agility, whereas larger enterprises must often navigate organizational structures, ticketing systems, approvals, and testing cycles before a change can be made. The result appears to be slower remediation even when vulnerabilities are well understood.

### Separation of “find” and “fix”.
Security teams can discover and triage issues but cannot patch them. Remediation depends on infrastructure, DevOps, or product engineering teams, and each handoff introduces friction. The larger the organization, the more these bottlenecks slow remediation.

## Software sector remediates fastest

### Buyer pressure.
Enterprise customers often require evidence of security maturity before purchasing, such as regular penetration tests, SOC 2 certification, and SSO aligned with zero-trust policies. SaaS vendors adapt early to meet these expectations.

### Modern infrastructure.
Cloud-centric environments, particularly common amongst software startups, can rollback and redeploy more quickly, reducing the friction of patching and configuration changes.

### Sector specific realities.
It's no surprise to see financial services and healthcare near the top of the industry ranking table given the sensitive data being processed by these organizations, the associated compliance requirements and high security expectations of customers.

## Vulnerabilities of the year

### Not every vulnerability is equal
Thousands of CVEs are published each year, but only a fraction become the focus of widespread exploitation or present serious, real-world impact. Intruder’s security team identified the five vulnerabilities that stood out most in 2025.

> "Assessing the threat environment is not just about what vulnerabilities are most common. The probability of exploit and potential consequences are equally important factors to consider." — Dan Andre, Head of Security

### Apache Tomcat RCE (CVE-2025-24813)
**What it is:** A remote code execution flaw in Apache Tomcat, rated CVSS 9.8.
**Why it mattered:** This was the single most commonly occurring critical CVE across customer estates from 2025. Its high severity, combined with the broad prevalence of Tomcat, made it one of the top exposures of the year.

### Fortinet Perimeter Vulnerabilities (CVE-2024-55591 & CVE-2025-32756)
**What they are:** An authentication bypass in FortiOS and a critical flaw in FortiVoice.
**Why they mattered:** These incidents underscore why edge appliances remain such high-value targets: they are internet-facing, widely deployed, and hold the keys to network access.

### Apache mod_rewrite RCE (CVE-2024-38475)
**What it is:** A vulnerability in Apache HTTP Server’s mod_rewrite module caused by improper output escaping.
**Why it mattered:** Despite being disclosed in 2024, the number of vulnerable instances still present highlights the continued relevance of this threat in 2025.

### Palo Alto Auth Bypass (CVE-2025-0108)
**What it is:** An authentication bypass in the web management interface of Palo Alto Networks PAN-OS firewall.
**Why it mattered:** This vulnerability was actively exploited in the wild and highlights a recurring theme: incomplete fixes.

### ToolShell (CVE-2025-53770)
**What it is:** A critical remote code execution flaw in Microsoft SharePoint, exploitable without authentication.
**Why it mattered:** ToolShell stood out in 2025 because it was a perfect storm. It offered reliable, unauthenticated remote code execution on systems that are often perimeter-exposed and tightly integrated with Active Directory.

## Looking forward
The 2025 data underscores a consistent theme: speed matters, but so does focus. Attackers are exploiting older vulnerabilities with new efficiency, while defenders are learning to act faster when exploitability is clear. For small and midsize organizations, the lesson is not to chase every CVE, but to prioritize the ones that matter most.

## About Intruder
Intruder's exposure management platform helps lean security teams stop breaches before they start by proactively uncovering attack surface weaknesses. By unifying attack surface management, cloud security, and continuous vulnerability management in one intuitive platform, Intruder makes it easy to secure your entire infrastructure.

Founded in 2015 by Chris Wallis, a former ethical hacker turned corporate blue teamer, Intruder was selected for GCHQ's Cyber Accelerator and is now protecting over 3,000 companies worldwide.

Start a free trial or book a call with one of our experts at intruder.io