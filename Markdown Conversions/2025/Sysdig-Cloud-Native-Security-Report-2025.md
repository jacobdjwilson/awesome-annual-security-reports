# Cloud-Native-Security-Report 2025

## Table of Contents
- [Key trends](#key-trends)
- [Executive summary](#executive-summary)
- [Cloud detection & response in minutes](#cloud-detection--response-in-minutes)
- [Manage humans, machines, and every identity in between](#manage-humans-machines-and-every-identity-in-between)
- [Navigate risk and reward with secure AI](#navigate-risk-and-reward-with-secure-ai)
- [Manage risk in containerized environments](#manage-risk-in-containerized-environments)
- [The adoption of Falco and open source security](#the-adoption-of-falco-and-open-source-security)
- [Security starts with foundational compliance](#security-starts-with-foundational-compliance)
- [Methodology](#methodology)
- [Conclusion](#conclusion)

---

## Key trends
- **Machine identities are 7.5x more risky than human identities** and are up to 40,000x more of them to manage.
- **Workloads using AI/ML packages grew by 500%** and public exposure decreased by 38% over the last year, showing that secure AI implementation has become a clear organizational priority.
- **Real-time detection and response in under 10 minutes** — when tools alert within seconds — is possible, and companies are initiating response actions in under 4 minutes.
- **60% of containers live for 1 minute or less.**
- **In-use vulnerabilities have decreased to less than 6%**, but image bloat quintupled year over year.
- **Organizations across the globe in all business sectors are leveraging open source software**, like Falco, regardless of their size.
- **Cybersecurity regulations are essential**, and EU-based organizations are leading the charge by prioritizing compliance more than their global counterparts.

---

## Executive summary
The “Sysdig 2025 Cloud‑Native Security and Usage Report” is back for its eighth year, analyzing real‑world data and the current state of cloud security and container usage. The findings detailed here indicate that security teams have made significant advancements across key areas, not only year over year, but also looking back on previous reports. With this in mind, our 2025 report provides benchmarks for maturity and efficiency, helping security teams, developers, and organizational leaders measure progress in the coming year.

In October 2023, the Sysdig Threat Research Team (TRT) concluded that cloud attacks can take place in 10 minutes or less. In this report, we have detailed how organizations today are detecting, investigating, and responding to real‑world threats within this time frame using innovative tools and techniques. We’ve also found that open source software is not just a trend, but has become a dependency for today’s cloud security. The open source threat detection tool Falco has been downloaded over 140 million times and is used across large enterprises and small businesses (SMBs) alike, signaling that organizations of all sizes have found value in the power of open source security.

The security community has also made advancements in vulnerability management and AI workload security. For the second year in a row, we’ve identified a significant reduction in runtime vulnerabilities. We also saw significant growth in the number of workloads that use AI and machine learning (ML) packages and — despite this growth — the percentage of workloads publicly exposed to the internet has decreased significantly, an indication that organizations are prioritizing AI security.

In assessing identity management from a different perspective than years past, we found that organizations are managing exponentially more service accounts than user accounts, and that these service accounts present higher risk profiles. No wonder supply‑chain attacks have become increasingly common!

Finally, in a few surprising turns of events, it turns out that organizations are prioritizing nuanced technical security benchmarks for compliance policies over the federally prescribed regulations we often read about in the news. And last but certainly not least, our beloved container lifespan statistic of many years has taken a new form. Short‑lived workloads are purpose‑built for speed and only live long enough to complete their task — all the more reason for real‑time detection and continuous monitoring.

---

## Cloud detection & response in minutes
At the end of 2023, the Sysdig TRT set the benchmark for cloud threat detection and response, stating that cloud attacks happen in 10 minutes on average. 5 seconds to detect, 5 minutes to investigate, and 5 minutes to initiate a response might seem like a high bar, but it is both possible and necessary for organizational security. Among the most common threats to cloud infrastructure this year, as noted in the 2024 Global Threat Year-in-Review, was the exploitation of anything open source, a trend that shows no signs of stopping.

### Real-time detection in 5 seconds
Unfortunately, alerts don’t just go from an event straight to security teams. Believe it or not, there are several “hops” that data has to take to get from the scanner to the inbox or notification dashboard, and that time can quickly add up. Errors in the data transfer life cycle can cause detection alerts to be delayed by minutes, effectively eliminating the opportunity for a timely response.

What does this mean in practice? After analyzing hundreds of thousands of alerts from hosts and containers across production regions, we found that the average time it takes our users to receive an event notification is less than five seconds, right on par with the 555 Cloud Detection and Response Benchmark. Real‑time threat detection and response is imperative when an attacker can wreak havoc on an organization in minutes, and slower methods that take 15 minutes or longer have become severely outdated.

> "I don’t want to know 15 minutes after a potential threat has been identified in our environment. I need to know instantly so we can shut it down before the threat has material impact."
> — Jordan Bodily, Senior Infrastructure Security Engineer, BigCommerce

### Incident investigation in less than 5 minutes
Traditionally, organizations receive alert notifications for high‑fidelity detections, and manually review low and medium alerts daily. This practice is time‑consuming and risky, especially for newly established or small security teams.

Instead, the initial response to a potential incident should be hands‑off. Security teams should have automated response actions in place. They should also build confidence and risk reduction right into their operating practice. They can achieve this by using high‑fidelity detections that cover a large swath of the MITRE ATT&CK framework, especially for threats concerning their particular environment, tools, software, and business sector.

Incident investigation presents a key use case for the implementation of a generative AI (GenAI) security assistant. Even if manually processing security alerts is the preferred method of analysis, the right tool can help find, understand, and correlate alerts much faster and reduce the risk of missing a key indicator.

The best option for rapid and robust incident investigation that allows security teams to keep pace with cloud attacks is automating the collection and correlation of the misbehaving identities to all related events, postures, and vulnerabilities. We found, for example, that Sysdig customers using enhanced investigation and real‑time identity correlation features can visualize and understand the relationships between resources and their impact on the attack chain, completing their investigations and moving on to response in less than three‑and‑a‑half minutes on average.

> "In the cloud, you may be managing multiple environments, thousands of identities, and an untold number of workloads. Without clear and comprehensive runtime visibility across those components, investigations take weeks. If you’re not ready to investigate in minutes, you’re going to lose."
> — Cat Schwan, Senior Manager, IT Security, Apree Health

> "In the past, an investigation could take up to a week. With Sysdig, it’s a 5‑10 minute job."
> — Information Security Leader, Security Operations Provider

### …and incident response must be automated
While most users are still cautious and prefer to alert only on container drift, the number of drift control policy users who enabled automated preventive actions — such as kill, stop, or pause at the indication of container drift — nearly tripled over the last year.

There are, however, multiple actions and behaviors that can be misidentified as drift, such as a virtual machine in a container, or third‑party‑owned self‑updating containers. The automated and inadvertent pausing or stopping of these benign container actions could cause undue operational issues; therefore, automated drift control response is an indicator of advanced maturity, and more importantly, confidence, in an organization’s security program.

As container security practices have matured over the last year, Sysdig has added options for additional, high‑confidence automated response actions for threat detections and malware indicators.

### The hottest Linux malware is open source
The Sysdig TRT analyzed over 272,000 malware hashes to determine the most commonly used Linux malware families over the last year. It came as no surprise that the most common malware variant was Mirai because of its accessibility and adaptability. The Sysdig TRT often reports on attacks using this open source malware code, including the RebirthLtd distributed denial of service (DDoS)‑as‑a‑service botnet group.

Security teams should regularly use threat intelligence to refine and enhance their static threat detections. Last year, we found that 35% of attacks could be identified with indicators of compromise (IoC)‑based detections. Attackers can easily modify malware hashes to avoid these detections, however, rendering them useless. It is imperative to have a layered approach to threat detection and response that captures the broader threat landscape.

---

## Manage humans, machines, and every identity in between
It is no secret that ironclad identity management and strong identity security are necessary in cloud security. Weak or missing credentials were the initial access vector for 47% of cloud environments in the first half of 2024, according to Google Cloud’s “H1 2024 Threat Horizons Report.” Effective and well‑governed identity management is one of the most basic (but also complicated) ways to reduce the risk of attack.

### Compare identities across cloud service providers
When analyzing identity usage data, we identified a fascinating anomaly in the number of users that organizations maintain within each cloud service provider (CSP). This anomaly was present even among multicloud users. Azure had up to 67x more “users” than Amazon Web Services (AWS) and Google Cloud Platform (GCP). Intrigued, we dug in. We quickly realized that every time a user logged into a new application that relied on Entra ID (formerly known as Azure Active Directory) for identity verification, a new Azure user was tallied.

### Minimize unnecessary risk of excessive identities
So if excessive permissions are being tolerated, how many identities are organizations managing? We found that, on average, organizations have 915 users and 41,605 service accounts: no wonder identity management is hard! This is a 40,000x difference between the types of identities connected to CSPs.

Nearly 15% of organizations have no connected user accounts. This — organizations properly managing cloud identity access — is a sure sign of security maturity. These organizations likely use a third‑party‑provided SSO verification process to log into cloud accounts rather than establishing and maintaining traditional, local user, and password combinations.

### Define your identity risk
An organization’s perception of risk depends on the definition it subscribes to. During data collection and analysis for this report, we defined a “risky” user as one without MFA enabled or rotating access keys. With that definition, only 8% of organizations maintain risky users.

On the other hand, we defined a “risky” service account as an AWS service identity, Azure principal, or GCP account that had administrator‑level access without rotating access keys. By this definition, a whopping 60% of enterprises maintain risky service accounts, making them 7.5x more risky than users.

---

## Navigate risk and reward with secure AI
With ChatGPT’s viral public launch in November 2022, we’ve now experienced more than two years of widespread AI use — and security concerns have been plentiful. AI security concerns generally fall into two buckets: how to use AI to enhance security practices and how to secure AI itself, both of which are valid.

### Adoption of AI for security is on the rise
According to the Cloud Security Alliance’s “State of AI and Security Survey Report” published in April 2024, 55% of organizations planned to implement GenAI solutions in 2024. Within four months of Sysdig Sage™ becoming generally available — it’s the first GenAI cloud security analyst — 45% of Sysdig customers had enabled it.

> "Attackers are already using AI every day, so security teams can’t afford to fall behind. I wouldn’t rely on a security platform today that doesn’t leverage AI to some degree, but I’m also not blindly buying into the hype. Not all AI is created equal—glorified chatbots just don’t move the needle. Real value comes from AI that actually enhances efficiency, speeds up human response, and acts as a force multiplier."
> — Brayden Santo, Senior Security Engineer, Sprout Social

### Secure workloads that use AI
The use of AI tools in an enterprise environment, specifically large language models (LLMs), raises concerns about data governance, security, and sovereignty. 75% of our customers are using AI or ML packages in their environments, which has more than doubled since last year’s report. In addition, the number of AI/ML packages running in workloads has also grown by nearly 500% over the last year.

But how secure are those packages? In April 2024, 34% of customers’ workloads containing AI packages were publicly exposed. Even through the rapid growth in AI adoption, that public exposure rate has been reduced to less than 13% — a reduction of 38% in eight months.

---

## Manage risk in containerized environments
### Prioritize vulnerability management
We analyzed the vulnerability landscape two years ago and presented the best and most effective prioritization method: in use. We define in‑use vulnerabilities as any vulnerability associated with a package actively loaded and used in a running environment. Year over year, we have reviewed this data and found that organizations continue to drastically reduce operational risk by properly prioritizing the vulnerabilities that matter most before the thousands that don’t.

### Shrink image bloat
Image bloat, or the inclusion of excess packages that are not required for an application to run properly, poses another risk and unnecessary cost. Image bloat quintupled over the last year, and although bloated images still only make up a small fraction of all container images, we’ve also seen a 300% increase in the overall number of packages in container images.

### Optimize container lifespans
Since 2018, Sysdig has reported on the ephemerality of containers in our annual report, and since 2023, over 70% of containers have lived for five minutes or less. This year, the data says that 74% of containers now live for five minutes or less. We also found that 60% of containers live for one minute or less.

---

## The adoption of Falco and open source security
Falco is an open source tool that detects anomalous activity within containers, hosts, Kubernetes environments, and more. It has gained widespread adoption across the cloud‑native community for its real‑time threat detection and continuous monitoring of system calls and application behaviors with customizable rules.

Falco reached a significant milestone in February 2024, achieving graduation within the Cloud Native Computing Foundation (CNCF). The project now has over 140 million downloads from users across the globe.

### Development and maturity of the Falco ecosystem
Falco began as an intrusion detection system (IDS) and has evolved into a fully functional open source cloud detection and response (CDR) tool. Falco first appeared on GitHub in May 2016 with a kernel module to monitor system calls. Two years later, it introduced its first Extended Berkeley Packet Filter (eBPF) probe and, more recently, a modern compile once‑run everywhere (CO‑RE) eBPF probe.

### The sky is the limit with open source detection
One of the many facets of open source software that many people treasure is the community itself. When it comes to Falco, there are a handful of companion tools to consider:
- **Falcosidekick**: A companion tool for Falco that extends alerting and notification capabilities.
- **Falco Talon**: A command and control framework that allows users to take immediate response actions following a Falco alert.

---

## Security starts with foundational compliance
Every organization desires a strong foundation in security and compliance. While well‑known regulations like the Health Insurance Portability and Accountability Act (HIPAA) and Digital Operational Resilience Act (DORA) have security requirements, the specificity of their security controls is not sufficient enough to provide the assurance that companies require for their cloud services and IT infrastructure.

When assessing compliance postures, we found that of over 80 compliance policies, many organizations prioritize compliance with foundational security benchmarks. These benchmarks offer the most granular compliance policies at the Kubernetes network and server levels.

> "We use DISA STIGs to guide the security practices of our Kubernetes cloud environment because they are comprehensive, frequently updated, and foundational for the broader compliance policies we need to adhere to like NIST 800‑53."
> — Senior Infrastructure Security Engineer, Healthcare IT Organization

---

## Methodology
The data in this report is derived from the careful and methodical analysis of millions of cloud accounts and Kubernetes containers that Sysdig customers run and secure daily. We also used Scarf, a platform for open source project usage analysis that facilitates data gathering and correlation. Our representative sample spans a wide range of cloud‑savvy industries across the globe.

---

## Conclusion
From the startling speed of cloud attacks to the widespread reliance on open source tools like Falco, the “Sysdig 2025 Cloud‑Native Security and Usage Report” provides an invaluable snapshot of the ever‑evolving cloud security and container usage landscape. The real‑world data used to derive the report’s findings highlights the challenges and opportunities in modern cloud environments for the year to come. This year’s analysis also underscores meaningful progress in vulnerability management and AI workload security while revealing a staggering imbalance between service and user accounts, regardless of how risky they may be.

As organizations look to adapt and continue to thrive over the next 12 months, this report serves as both a benchmark and a roadmap for navigating the complexities of the cloud‑native world. To that end, open source software has truly cemented itself as a cornerstone of cloud security, bridging the gap between enterprises and small businesses alike. Until next year, keep up the good work and secure every second of your cloud journey!

![Image description: Sysdig logo and closing statement]