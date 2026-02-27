Organization: Sysdig
Report Title: Cloud-Native-Security-Report
Year: 2025

# 2025 Cloud-Native Security and Usage Report
**Real data. Real threats. Real benchmarks.**

![Cover image showing a timeline of reports from 2017 to 2024, leading into the 2025 report title.]

## Table of Contents
- [Key Trends](#key-trends)
- [Executive Summary](#executive-summary)
- [Cloud Detection & Response in Minutes](#cloud-detection--response-in-minutes)
- [Manage Humans, Machines, and Every Identity in Between](#manage-humans-machines-and-every-identity-in-between)
- [Navigate Risk and Reward with Secure AI](#navigate-risk-and-reward-with-secure-ai)
- [Manage Risk in Containerized Environments](#manage-risk-in-containerized-environments)
- [The Adoption of Falco and Open Source Security](#the-adoption-of-falco-and-open-source-security)
- [Security Starts with Foundational Compliance](#security-starts-with-foundational-compliance)
- [Methodology](#methodology)
- [Conclusion](#conclusion)

---

## Key Trends

- **Machine identities** are 7.5x more risky than human identities and there are up to 40,000x more of them to manage.
- **Workloads using AI/ML packages** grew by 500% and public exposure decreased by 38% over the last year, showing that secure AI implementation has become a clear organizational priority.
- **Real-time detection and response** in under 10 minutes — when tools alert within seconds — is possible, and companies are initiating response actions in under 4 minutes.
- **60% of containers** live for 1 minute or less.
- **In-use vulnerabilities** have decreased to less than 6%, but image bloat quintupled year over year.
- **Organizations across the globe** in all business sectors are leveraging open source software, like Falco, regardless of their size.
- **Cybersecurity regulations** are essential, and EU-based organizations are leading the charge by prioritizing compliance more than their global counterparts.

---

## Executive Summary

The “Sysdig 2025 Cloud-Native Security and Usage Report” is back for its eighth year, analyzing real-world data and the current state of cloud security and container usage. The findings detailed here indicate that security teams have made significant advancements across key areas, not only year over year, but also looking back on previous reports. With this in mind, our 2025 report provides benchmarks for maturity and efficiency, helping security teams, developers, and organizational leaders measure progress in the coming year.

In October 2023, the Sysdig Threat Research Team (TRT) concluded that cloud attacks can take place in 10 minutes or less. In this report, we have detailed how organizations today are detecting, investigating, and responding to real-world threats within this time frame using innovative tools and techniques. We’ve also found that open source software is not just a trend, but has become a dependency for today’s cloud security. The open source threat detection tool Falco has been downloaded over 140 million times and is used across large enterprises and small businesses (SMBs) alike, signaling that organizations of all sizes have found value in the power of open source security.

The security community has also made advancements in vulnerability management and AI workload security. For the second year in a row, we’ve identified a significant reduction in runtime vulnerabilities. We also saw significant growth in the number of workloads that use AI and machine learning (ML) packages and — despite this growth — the percentage of workloads publicly exposed to the internet has decreased significantly, an indication that organizations are prioritizing AI security.

In assessing identity management from a different perspective than years past, we found that organizations are managing exponentially more service accounts than user accounts, and that these service accounts present higher risk profiles. No wonder supply-chain attacks have become increasingly common!

Finally, in a few surprising turns of events, it turns out that organizations are prioritizing nuanced technical security benchmarks for compliance policies over the federally prescribed regulations we often read about in the news. And last but certainly not least, our beloved container lifespan statistic of many years has taken a new form. Short-lived workloads are purpose-built for speed and only live long enough to complete their task — all the more reason for real-time detection and continuous monitoring.

Read on to get the statistics for all of this year’s findings.

---

## Cloud Detection & Response in Minutes

![Graphic showing a timeline: 00:00:05 Threat Detected, 00:03:29 Investigation Complete, 00:05:00 Response Initiated. Icons represent Container Drift, Multiple Login Attempts, and Access Granted.]

At the end of 2023, the Sysdig TRT set the benchmark for cloud threat detection and response, stating that cloud attacks happen in 10 minutes on average. 5 seconds to detect, 5 minutes to investigate, and 5 minutes to initiate a response might seem like a high bar, but it is both possible and necessary for organizational security. Among the most common threats to cloud infrastructure this year, as noted in the 2024 Global Threat Year-in-Review, was the exploitation of anything open source, a trend that shows no signs of stopping.

### Real-time detection in 5 seconds
Unfortunately, alerts don’t just go from an event straight to security teams. Believe it or not, there are several “hops” that data has to take to get from the scanner to the inbox or notification dashboard, and that time can quickly add up. Errors in the data transfer life cycle can cause detection alerts to be delayed by minutes, effectively eliminating the opportunity for a timely response.

What does this mean in practice? After analyzing hundreds of thousands of alerts from hosts and containers across production regions, we found that the average time it takes our users to receive an event notification is less than five seconds, right on par with the 555 Cloud Detection and Response Benchmark. Real-time threat detection and response is imperative when an attacker can wreak havoc on an organization in minutes, and slower methods that take 15 minutes or longer have become severely outdated.

> I don’t want to know 15 minutes after a potential threat has been identified in our environment. I need to know instantly so we can shut it down before the threat has material impact.
> 
> — **Jordan Bodily**, Senior Infrastructure Security Engineer, BigCommerce

### Incident investigation in less than 5 minutes
Traditionally, organizations receive alert notifications for high-fidelity detections, and manually review low and medium alerts daily. This practice is time-consuming and risky, especially for newly established or small security teams.

Instead, the initial response to a potential incident should be hands-off. Security teams should have automated response actions in place. They should also build confidence and risk reduction right into their operating practice. They can achieve this by using high-fidelity detections that cover a large swath of the MITRE ATT&CK framework, especially for threats concerning their particular environment, tools, software, and business sector.

Incident investigation presents a key use case for the implementation of a generative AI (GenAI) security assistant. Even if manually processing security alerts is the preferred method of analysis, the right tool can help find, understand, and correlate alerts much faster and reduce the risk of missing a key indicator.

The best option for rapid and robust incident investigation that allows security teams to keep pace with cloud attacks is automating the collection and correlation of the misbehaving identities to all related events, postures, and vulnerabilities. We found, for example, that Sysdig customers using enhanced investigation and real-time identity correlation features can visualize and understand the relationships between resources and their impact on the attack chain, completing their investigations and moving on to response in less than three-and-a-half minutes on average. Again, this is well within the 555 Benchmark’s “5 minutes to investigate” suggestion.

> In the cloud, you may be managing multiple environments, thousands of identities, and an untold number of workloads. Without clear and comprehensive runtime visibility across those components, investigations take weeks. If you’re not ready to investigate in minutes, you’re going to lose.
> 
> — **Cat Schwan**, Senior Manager, IT Security, Apree Health

> In the past, an investigation could take up to a week. With Sysdig, it’s a 5-10 minute job.
> 
> — **Information Security Leader**, Security Operations Provider

### …and incident response must be automated
While most users are still cautious and prefer to alert only on container drift, the number of drift control policy users who enabled automated preventive actions — such as kill, stop, or pause at the indication of container drift — nearly tripled over the last year.

#### Define your prevention
As container security practices have matured over the last year, Sysdig has added options for additional, high-confidence automated response actions for threat detections and malware indicators. For example:

- We began by defining a **drifted binary** as any binary that was not part of the original image of the container, but was typically downloaded or compiled within the running container.
- We then introduced the ability to **detect volume-based binaries** that would treat all binaries from mounted volumes as drifted.
- Recently, we granted users the power to **define regular expression (RegEx) statements** to define exceptions. These fine-grained exceptions allow specific files or binaries to run without being incorrectly detected as drift by the Sysdig agent.

In addition to autonomously killing, stopping, or pausing a misbehaving container, users may also automatically issue a “kill -9” command on the process following a threat detection alert. In addition, it is also possible to autonomously prevent drift and malware at the system level via hooks.

### The hottest Linux malware is open source
The Sysdig TRT analyzed over 272,000 malware hashes to determine the most commonly used Linux malware families over the last year. It came as no surprise that the most common malware variant was Mirai because of its accessibility and adaptability.

**Top 5 Linux Malware Families in 2024:**
1. **Mirai**
2. **Gafgyt**
3. **Kinsing**
4. **Tsunami**
5. **XMRig**

Security teams should regularly use threat intelligence to refine and enhance their static threat detections. Last year, we found that 35% of attacks could be identified with indicators of compromise (IoC)-based detections. However, behavior-based detection is increasingly necessary as attackers mature.

---

## Manage Humans, Machines, and Every Identity in Between

![Graphic showing "Access Denied" with icons representing human and machine identities.]

Weak or missing credentials were the initial access vector for 47% of cloud environments in the first half of 2024[^1].

### Compare identities across cloud service providers
We identified an anomaly in the number of users within each cloud service provider (CSP). Azure had up to 67x more “users” than AWS and GCP. This is because every time a user logs into an application relying on Entra ID (formerly Azure Active Directory), a new Azure user is tallied (e.g., Outlook, OneDrive, etc.).

### Move past excessive permissions
In the 2024 report, we found that 98% of granted permissions go unused. While overpermissioning is risky, some organizations consider it a tolerable risk to expedite operations. Proactively implementing MFA can mitigate these risks.

### Minimize unnecessary risk of excessive identities
On average, organizations have 915 users and 41,605 service accounts — a 40,000x difference. Even after filtering for outliers, there are still 35x more service accounts to manage than users.

> **Nearly 15% of organizations have no connected user accounts.** This is a sign of security maturity, likely using third-party SSO verification.

### Define your identity risk
- **Risky User**: One without MFA enabled or rotating access keys. Only 8% of organizations maintain risky users.
- **Risky Service Account**: AWS service identity, Azure principal, or GCP account with administrator-level access without rotating keys. **60% of enterprises maintain risky service accounts**, making them 7.5x more risky than users.

---

## Navigate Risk and Reward with Secure AI

![Graphic showing a compass with AI-related questions: "Who is this user?", "Tell me more about this event", "How did this happen?", "What are my noisiest policies?"]

> Attackers are already using AI every day, so security teams can’t afford to fall behind... Real value comes from AI that actually enhances efficiency, speeds up human response, and acts as a force multiplier.
> 
> — **Brayden Santo**, Senior Security Engineer, Sprout Social

### Adoption of AI for security is on the rise
According to the Cloud Security Alliance, 55% of organizations planned to implement GenAI solutions in 2024. Within four months of Sysdig Sage™ becoming available, 45% of Sysdig customers enabled it. 75% of Sysdig Sage users are part of a SecOps team.

### Secure workloads that use AI
75% of customers are using AI or ML packages, a number that has more than doubled since last year. The number of AI/ML packages running in workloads grew by nearly 500%.

**AI Package Type Breakdown:**
- **GenAI Packages**: Increased from 15% to 36% in the last year.
- **Other AI/ML Packages**: 64%.

**Public Exposure Risk:**
In April 2024, 34% of workloads containing AI packages were publicly exposed. That rate has been reduced to less than 13% — a reduction of 38% in eight months.

---

## Manage Risk in Containerized Environments

![Graphic showing a container scan timeline: 00:00 Scan Completed, 00:04 Scan in Progress, 00:08 Scan Failed / Container Lost.]

### Prioritize vulnerability management
We define **in-use vulnerabilities** as those associated with a package actively loaded in a running environment. Of all images analyzed, less than 17% had critical or high vulnerabilities.

### Shrink image bloat
Image bloat (excess packages) quintupled over the last year. We’ve seen a 300% increase in the overall number of packages in container images. This is likely due to developers adding libraries to expedite development.

### Optimize container lifespans
74% of containers live for five minutes or less. **60% of containers live for one minute or less.**

**Reasons for short lifespans:**
- **Resource constraints**: Orchestrator policies pausing/shutting down containers.
- **Health checks**: Aggressive Kubernetes settings.
- **Purpose-built tasks**: Batch processing or CI pipelines.
- **Serverless/Microservices**: Functions designed for a single request.
- **Crash/Misconfiguration**: Application errors.

---

## The Adoption of Falco and Open Source Security

Falco achieved graduation within the Cloud Native Computing Foundation (CNCF) in February 2024. It has surpassed **140 million downloads**.

### Development and maturity of the Falco ecosystem
Falco offers three drivers to ensure detection on any host:
1. Kernel module
2. eBPF probe
3. CO-RE eBPF probe

### Open source is for everyone
**Falco Usage by Business Sector (Self-hosted):**
- Internet Software & Services: Majority
- Transportation: >22% (Likely due to large enterprise implementations)

**Falco Usage by Company Size:**
- <250 employees: 34%
- Large Enterprises: Significant portion

### Companion Tools and Plug-ins
- **Falcosidekick**: Extends alerting. 28 million lifetime downloads.
- **Falco Talon**: Response framework. 140,000 downloads by end of 2024.
- **Popular Plug-ins**: `json`, `k8smeta`, `k8saudit`, `cloudtrail`.
- **Unique Plug-ins**: Salesforce threat detection, Keycloak IAM events, Box audit logging.

---

## Security Starts with Foundational Compliance

Organizations are prioritizing technical benchmarks (CIS, DISA STIGs) over high-level regulations.

### Compliance Scores by Benchmark
| Benchmark | Average Compliance Score |
| :--- | :--- |
| CIS Distribution Independent Linux Benchmark (Level 1 – Workstation) | 100.00% |
| CIS Kubernetes V1.15 Benchmark | 100.00% |
| DISA Kubernetes STIG Category II (Medium) | 98.72% |
| DISA Kubernetes STIG Category I (High) | 97.16% |
| DISA Kubernetes STIG | 96.33% |
| CIS Distribution Independent Linux Benchmark (Level 2 – Workstation) | 94.37% |
| CIS Kubernetes V1.23 Benchmark | 90.14% |
| DISA Docker Enterprise 2.x Linux/Unix STIG | 88.34% |
| CIS Kubernetes V1.26 Benchmark | 81.81% |
| CIS Kubernetes V1.24 Benchmark | 81.35% |

> We use DISA STIGs to guide the security practices of our Kubernetes cloud environment because they are comprehensive, frequently updated, and foundational for the broader compliance policies we need to adhere to like NIST 800-53.
> 
> — **Senior Infrastructure Security Engineer**, Healthcare IT Organization

EU-based organizations (EMEA) show higher adoption of compliance policies compared to other regions, likely due to strict regulations like NIS2 and DORA.

---

## Methodology

The data in this report is derived from the analysis of millions of cloud accounts and Kubernetes containers that Sysdig customers run daily. We also used Scarf for open source project usage analysis. The sample spans early-stage startups to multinational enterprises across various industries.

---

## Conclusion

From the startling speed of cloud attacks to the widespread reliance on open source tools like Falco, the “Sysdig 2025 Cloud-Native Security and Usage Report” provides an invaluable snapshot of the ever-evolving landscape. This year’s analysis underscores progress in vulnerability management and AI security while revealing a staggering imbalance between service and user accounts. Open source software has cemented itself as a cornerstone of cloud security. Until next year, keep up the good work and secure every second of your cloud journey!

**Sysdig. Secure Every Second.**

[^1]: Google Cloud’s “H1 2024 Threat Horizons Report.”