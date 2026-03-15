# Software Under Siege 2025

## Table of Contents
- [Executive summary](#executive-summary)
- [Software is under siege](#software-is-under-siege)
- [The software threat landscape: Attacks are prolific and continuous](#the-software-threat-landscape-attacks-are-prolific-and-continuous)
    - [Attack volume](#attack-volume)
    - [Attack breakdowns](#attack-breakdowns)
- [Software vulnerabilities: The cracks are widening](#software-vulnerabilities-the-cracks-are-widening)
- [Defenders are fighting at a massive disadvantage](#defenders-are-fighting-at-a-massive-disadvantage)
    - [Speed of attackers](#speed-of-attackers)
    - [Speed of defenders](#speed-of-defenders)
    - [Time to patch](#time-to-patch)
- [Proactive application defense changes the game](#proactive-application-defense-changes-the-game)

---

## Executive summary

Defenders who are responsible for protecting today’s applications from attack face relentless pressure on two fronts: a surge in targeted attack activity from determined adversaries, and a growing backlog of serious vulnerabilities. Both trends are exacerbated by the widespread use of AI for software development and generating attacks.

Contrast’s runtime security platform continuously monitors and reports on vulnerabilities and attacks that target applications, Application Programming Interfaces (APIs) and libraries, shining a spotlight on the usually invisible front lines of application-layer threats. This deep telemetry provides insights into the inner workings of real-world applications and APIs worldwide, showing that:

- **Apps and APIs have become the battleground of choice for modern attackers.** Application attacks are more prolific than ever before. The average application is exposed to 81 confirmed, viable attacks each month, that evade other defenses, alongside more than 10,000 probes and other unsuccessful attack attempts.
- **At the same time, applications have never been more exposed**, with an average of close to 30 serious, exploitable vulnerabilities per application.
- **The deck is stacked against software developers and AppSec teams.** Applications face an average of 17 new vulnerabilities per month, driven by ongoing development as well as vulnerabilities in third-party dependencies. This rate far exceeds the ability for AppSec and DevOps teams to patch, and the growing use of AI-generated code exacerbates the problem.
- **The challenge is just as daunting for SecOps teams.** Attackers are able to exploit new vulnerabilities in just a few days, while defenders often take months to spot and contain intrusions. A core challenge for SecOps analysts: Traditional detection and response tools employed in the SOC are blind to attacks that target the application layer.
- **A new approach changes the game:** It’s urgent for organizations to move beyond traditional application defenses, such as WAF and EDR, and adopt a modern runtime approach to application defense, such as Application Detection and Response. Organizations that do so can eliminate their exposure to the most prevalent application attacks, including deserialization attacks, injection attacks and many more. This not only reduces the risk of breach but also significantly reduces the burden on overworked AppSec, SecOps and development teams.

### Runtime data gives a real-world view of application risk
Contrast’s data is collected from real-world running applications and Application Programming Interfaces (APIs), using a lightweight sensor that allows full visibility into the complete runtime context. This “inside-out” approach gives us continuous visibility into how applications behave and are targeted in real-world production environments.

As requests flow through monitored applications, the sensors track runtime behavior, including control flow, data flow and backend interactions such as file access, SQL queries and external service calls. This extensive context allows Contrast to determine not just whether a vulnerability exists in an application or library, but whether it is reachable by user input, triggerable in real-world execution paths, and exploitable given the specific data flows and environment in which the application runs.

This report is built from anonymized aggregate telemetry collected from thousands of live applications, incorporating more than 1.6 trillion security-critical observations every day. The result is a high-fidelity view of the most impactful attack techniques in play today, and which vulnerabilities matter most.

---

## Software is under siege

Application-layer attacks have become one of the most common and consequential methods adversaries use to gain access and compromise organizations. These attacks target the custom code, APIs, and logic that power modern applications, often slipping past traditional detection tools such as Endpoint Detection and Response (EDR) and network-based defenses such as Web Application Firewalls (WAFs). Data from industry analysts highlights the challenge.

**APPLICATION ATTACKS ARE PROLIFIC**
The 2025 Verizon DBIR found that web application attacks were in the top 3 types of reported incidents in 2024.[^1] It goes on to show consistent heavy use of vulnerability exploits over the last 5 years.

**APPLICATION ATTACKS CAUSE ENORMOUS DAMAGE**
IDC reports that application-related catalysts, such as a supply chain attack, unpatched vulnerabilities or a zero day, have triggered recent ransomware incidents for 35% of surveyed organizations,[^2] with an average cost of $4.91 million per ransomware incident,[^3] according to IBM.

**APPLICATION VULNERABILITIES ARE A MAJOR SOURCE OF RISK**
Data from Mandiant’s M-Trends 2025 report reveals that 33% of breaches began with a vulnerability exploit.[^4] Forrester’s State of Application Security 2025 shows that application exploits are among the top external attack vectors.[^5] Guidepoint reports that the number of new Known Exploited Vulnerabilities (KEVs) increased 75% year-over-year in Q1 2025.[^6]

**SOC TEAMS STRUGGLE TO DETECT BREACHES IN A TIMELY MANNER**
Mandiant's M-Trends 2025 report indicates that more than half (57%) of intrusions are being discovered through external sources[^7] rather than internal security measures. This suggests significant limitations in existing detection capabilities within many organizations, leading to lengthy delays in identifying and responding to threats.

On top of all this, the application attack footprint is large and getting exponentially bigger. ![Figure 1: Average number of applications and APIs per organization, by employee count]

Looking forward, IDC predicts that by 2028, there will be over 1 billion new cloud-native applications to protect.[^8] The rapid adoption of AI and LLMs is increasing the challenge; Forrester reports that the number of AI-related APIs increased 807% in 2025, and the number of AI-related CVEs increased 1,025% from 2023 to 2024.[^9]

The numbers tell a clear story, but the real-world impact is even more revealing. Many of the most significant ransomware campaigns and similar cyber attacks leverage applications as a point of initial entry.

### The Contrast Graph — unleashing deep application-layer observability
The Contrast Graph lies at the core of the Contrast runtime security platform, powering advanced capabilities including optional Agentic AI workflows that help teams respond faster and fix smarter. The Graph builds a real-time digital twin of an organization’s application and API environment, mapping live attack paths; correlating runtime behavior; and exposing how vulnerabilities, threats and assets are connected.

---

## The software threat landscape: Attacks are prolific and continuous

The volume and variety of attacks targeting the application layer have expanded significantly. This shift reflects both the growing reliance on custom software and APIs and the evolving tactics of adversaries who have learned where defenses are often weakest.

### Attack volume
Application-layer attacks are a constant fact of life in the modern enterprise. Contrast’s telemetry shows that the average application is targeted by attacks more than 14,000 times each month, which translates to approximately once every 3 minutes.

**Understanding attack categories**
- **Probe attacks**: These typically represent broad, automated attempts to discover vulnerabilities.
- **Suspicious attacks**: These attacks show clear signs of malicious intent, often including exploit payloads, tampering attempts or evasion techniques.
- **Viable attacks**: These are confirmed attacks against reachable and exploitable vulnerabilities.

![Figure 2: Average number of attacks per application per month, by type]

![Figure 3: Attack rate distribution]

### Attack breakdowns
While the volume of application-layer attacks is striking, the nature of those attacks offers deeper insights.

![Figure 4: Top types of application probe attacks]

![Figure 5: Top types of viable application attacks]

![Figure 6: Prevalence of top probes vs. top viable attacks]

![Figure 7: Top five viable attack techniques by industry vertical]

**Technique spotlight: Method tampering**
- **What it is**: Method tampering (sometimes called HTTP verb tampering) is an attack against HTTP authentication or authorization systems that have implicit "allow all" settings or excessive permissions in their security configuration.
- **How attackers exploit it**: By manipulating the HTTP method associated with a request to a web application, attackers can force unauthorized actions like elevating privileges, altering transactions or bypassing authentication controls.
- **How to defend**: Ensure only necessary HTTP methods are enabled on HTTP servers. Use a simple allow list.

![Figure 8: Top five viable attack techniques by programming language]

**Technique spotlight: Untrusted deserialization**
- **What it is**: Untrusted deserialization attacks exploit vulnerabilities in libraries designed to unpack structured data such as JSON, Java objects or PHP serialization.
- **How attackers exploit it**: Attackers craft malicious serialized objects that, when processed by the application, can trigger remote code execution, escalate privileges or disrupt service.
- **How to defend**: Avoid deserialization of untrusted input, use safer formats like JSON, keep libraries updated, and enable runtime protections.

---

## Software vulnerabilities: The cracks are widening

Behind every successful application-layer attack is an unpatched, misconfigured or unknown vulnerability.

![Figure 9: Average vulnerability findings per application, by severity]

**What is a “Serious” vulnerability?**
For purposes of this report, Serious vulnerabilities are those rated by Contrast as High or Critical severity. These represent the highest combination of likelihood of exploitation and potential impact.

![Figure 10: Percentage of applications with vulnerability findings]

![Figure 11: Percentage of applications with a vulnerability by agent language]

---

## Defenders are fighting at a massive disadvantage

### Speed of attackers
Recent research from Google and Mandiant shows that the average time between the disclosure of a new vulnerability and active exploitation in the wild is now just **five days**.[^13] CrowdStrike’s 2025 Global Threat Report notes the average breakout time is just **48 minutes**.[^14]

### Speed of defenders
According to IBM’s 2024 Cost of a Data Breach Report, the average time to identify a breach is **194 days**, and the time to contain it is an additional **64 days**.[^15][^16]

### Time to patch
While a new vulnerability may be exploited in five days, our data shows that the average time to remediate even the most critical vulnerabilities is **84 days**.

![Figure 12: Vulnerability escape rate per application, by severity]

![Figure 13: Vulnerability backlog growth over time]

---

## Proactive application defense changes the game

An effective approach to managing application cyber risk relies on two critical, complementary workflows:
1. **Risk-based application-layer vulnerability management**
2. **Real-time detection and blocking for application-layer attacks**

Implementing proactive application defense allows organizations to block the viable attacks that target unpatched vulnerabilities.

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