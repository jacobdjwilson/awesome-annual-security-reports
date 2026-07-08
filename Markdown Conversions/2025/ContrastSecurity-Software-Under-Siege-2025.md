# Software Under Siege 2025

## Table of Contents
- [Executive summary](#executive-summary)
- [Software is under siege](#software-is-under-siege)
- [The software threat landscape: Attacks are prolific and continuous](#the-software-threat-landscape-attacks-are-prolific-and-continuous)
- [Attack breakdowns](#attack-breakdowns)
- [Software vulnerabilities: The cracks are widening](#software-vulnerabilities-the-cracks-are-widening)
- [Defenders are fighting at a massive disadvantage](#defenders-are-fighting-at-a-massive-disadvantage)
- [Proactive application defense changes the game](#proactive-application-defense-changes-the-game)

## Executive summary
Defenders who are responsible for protecting today’s applications from attack face relentless pressure on two fronts: a surge in targeted attack activity from determined adversaries, and a growing backlog of serious vulnerabilities. Both trends are exacerbated by the widespread use of AI for software development and generating attacks.

Contrast’s runtime security platform continuously monitors and reports on vulnerabilities and attacks that target applications, Application Programming Interfaces (APIs) and libraries, shining a spotlight on the usually invisible front lines of application-layer threats. This deep telemetry provides insights into the inner workings of real-world applications and APIs worldwide, showing that:

- **Apps and APIs have become the battleground of choice for modern attackers.** Application attacks are more prolific than ever before. The average application is exposed to 81 confirmed, viable attacks each month, that evade other defenses, alongside more than 10,000 probes and other unsuccessful attack attempts.
- **At the same time, applications have never been more exposed**, with an average of close to 30 serious, exploitable vulnerabilities per application.
- **The deck is stacked against software developers and AppSec teams.** Applications face an average of 17 new vulnerabilities per month, driven by ongoing development as well as vulnerabilities in third-party dependencies. This rate far exceeds the ability for AppSec and DevOps teams to patch, and the growing use of AI-generated code exacerbates the problem.
- **The challenge is just as daunting for SecOps teams.** Attackers are able to exploit new vulnerabilities in just a few days, while defenders often take months to spot and contain intrusions. A core challenge for SecOps analysts: Traditional detection and response tools employed in the SOC are blind to attacks that target the application layer.

A new approach changes the game: It’s urgent for organizations to move beyond traditional application defenses, such as WAF and EDR, and adopt a modern runtime approach to application defense, such as Application Detection and Response. Organizations that do so can eliminate their exposure to the most prevalent application attacks, including deserialization attacks, injection attacks and many more. This not only reduces the risk of breach but also significantly reduces the burden on overworked AppSec, SecOps and development teams.

## Software is under siege
Application-layer attacks have become one of the most common and consequential methods adversaries use to gain access and compromise organizations. These attacks target the custom code, APIs, and logic that power modern applications, often slipping past traditional detection tools such as Endpoint Detection and Response (EDR) and network-based defenses such as Web Application Firewalls (WAFs).

- **Application attacks are prolific:** The 2025 Verizon DBIR found that web application attacks were in the top 3 types of reported incidents in 2024.[^1]
- **Application attacks cause enormous damage:** IDC reports that application-related catalysts have triggered recent ransomware incidents for 35% of surveyed organizations,[^2] with an average cost of $4.91 million per incident.[^3]
- **Application vulnerabilities are a major source of risk:** Mandiant’s M-Trends 2025 report reveals that 33% of breaches began with a vulnerability exploit.[^4]
- **SOC teams struggle to detect breaches in a timely manner:** Mandiant's M-Trends 2025 report indicates that more than half (57%) of intrusions are being discovered through external sources.[^7]

![Figure 1: Average number of applications and APIs per organization, by employee count]

## The software threat landscape: Attacks are prolific and continuous
Application-layer attacks are a constant fact of life in the modern enterprise. Contrast’s telemetry shows that the average application is targeted by attacks more than 14,000 times each month, which translates to approximately once every 3 minutes.

### Understanding attack categories
- **Probe attacks:** Broad, automated attempts to discover vulnerabilities.
- **Suspicious attacks:** Attacks showing clear signs of malicious intent, including exploit payloads or evasion techniques.
- **Viable attacks:** Confirmed attacks against reachable and exploitable vulnerabilities.

![Figure 2: Average number of attacks per application per month, by type]

## Attack breakdowns
![Figure 4: Top types of application probe attacks]
![Figure 5: Top types of viable application attacks]
![Figure 6: Prevalence of top probes vs. top viable attacks]

### Technique spotlight: Method tampering
**What it is:** Method tampering (sometimes called HTTP verb tampering) is an attack against HTTP authentication or authorization systems that have implicit "allow all" settings or excessive permissions in their security configuration.

### Technique spotlight: Untrusted deserialization
**What it is:** Untrusted deserialization attacks exploit vulnerabilities in libraries designed to unpack structured data such as JSON, Java objects or PHP serialization.

## Software vulnerabilities: The cracks are widening
![Figure 9: Average vulnerability findings per application, by severity]
![Figure 10: Percentage of applications with vulnerability findings]
![Figure 11: Percentage of applications with a vulnerability by agent language]

## Defenders are fighting at a massive disadvantage
- **Speed of attackers:** The average time between the disclosure of a new vulnerability and active exploitation is now just 5 days.[^13]
- **Speed of defenders:** The average time to identify a breach is 194 days, and the time to contain it is an additional 64 days.[^15][^16]

### Time to patch
While a new vulnerability may be exploited in five days, the average time to remediate even the most critical vulnerabilities is 84 days. On average, development and AppSec teams are remediating just six vulnerabilities per application per month.

![Figure 12: Vulnerability escape rate per application, by severity]
![Figure 13: Vulnerability backlog growth over time]

## Proactive application defense changes the game
An effective approach to managing application cyber risk relies on two critical, complementary workflows:
1. **Risk-based application-layer vulnerability management:** Focusing attention on the few vulnerabilities that truly matter.
2. **Real-time detection and blocking for application-layer attacks:** Implementing Application Detection and Response (ADR) to eliminate blindspots and protect applications from within.

---
[^1]: Verizon 2025 Data Breach Investigations Report, Apr 23, 2025
[^2]: IDC Market Insights: Application Detection and Response, Feb 2025
[^3]: IBM Cost of a Data Breach Report 2024, July 30, 2024
[^4]: Google Mandiant M-Trends 2025, Apr 23, 2025
[^5]: Forrester Research, The State Of Application Security, 2025
[^6]: GuidePoint Security, GRIT 2025 Q1 Ransomware & Cyber Threat Report
[^7]: Google Mandiant M-Trends 2025, Apr 23, 2025
[^8]: IDC Market Insights: Application Detection and Response, Feb 2025
[^9]: Forrester Research, The State Of Application Security, 2025
[^10]: Clop Ransomware Likely Sitting on MOVEit Transfer Vulnerability (CVE-2023-34362) Since 2021, June 8, 2023
[^11]: ScreenConnect 25.2.4 Security Patch, April 24, 2025
[^12]: CVE-2024-40711 - Veeam Backup and Replication deserialization vulnerability exploited by ransomware actors, October 30, 2024
[^13]: How Low Can You Go? An Analysis of 2023 Time-to-Exploit Trends. Oct 15, 2024
[^14]: CrowdStrike 2025 Global Threat Report, Feb 27, 2025
[^15]: IBM Cost of a Data Breach Report 2024, July 30, 2024
[^16]: IBM Cost of a Data Breach Report 2024, July 30, 2024