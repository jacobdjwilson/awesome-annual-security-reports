# 2026 Cloud-Native Security and Usage Report

## Table of Contents
- [Key trends](#key-trends)
- [Executive summary](#executive-summary)
- [It’s time for agentic AI vulnerability management](#its-time-for-agentic-ai-vulnerability-management)
- [Defending the cloud-native battlefield](#defending-the-cloud-native-battlefield)
- [AI adoption matures](#ai-adoption-matures)
- [Identity is the cloud-native perimeter](#identity-is-the-cloud-native-perimeter)
- [Growth of the open source runtime security community](#growth-of-the-open-source-runtime-security-community)
- [Conclusion](#conclusion)
- [Methodology](#methodology)

---

## Key trends

- **Organizations are laying the foundations to scale AI securely**: AI-specific packages grew 25x YoY and are building a secure surface with 6x more ML packages, with only 1.5% of these assets publicly exposed.
- **Machine-driven operations are defining the modern firewall**: Human identities account for just 2.8% of managed identities within CSPs.
- **Regulations are accelerating, not stifling, AI adoption in Europe**: More than 50% of AI and ML packages belong to European organizations.
- **Organizations are shifting to automated response actions for modern threats**: More than 70% of organizations use behavior-based detections across 91% of environments to improve signal quality, and 140% more organizations now automatically kill processes when a detection is triggered.
- **Even as cloud environments scale beyond human limits, runtime security and build discipline continue to reduce operational risk**: Running vulnerable images with known exploits dropped 74% to nearly 0%, and image bloat fell 50% YoY, with less than 1% of packages unused in running images.
- **Driven by data sovereignty, runtime is the baseline for trust in cloud security**: 9,000 organizations use Falco, with Europe representing 34%.

---

## Executive summary

Sysdig’s team of cybersecurity researchers are back at it with the ninth annual “Sysdig 2026 Cloud-Native Security and Usage Report,” and here’s the headline: the “hustle hard” era of security is coming to an end.

For years, cloud security has been a race that humans had full intentions of winning through sheer effort, better dashboards, and more caffeine. Even in last year’s report, organizations continued to make progress, but the data this year shows that they have officially hit the limits of human scale.

As with Sysdig’s past eight reports, this report uncovers what’s really happening in the cloud through the analysis of real-world customer data. The findings tell us that while defenders continue to become more sophisticated and automated security is gaining traction, attackers remain relentless, and the human element is still the most significant risk to an organization. Human error, including misconfigurations, is the root cause driving 26% of all data breaches.

We must face an uncomfortable truth: organizations have optimized human workflows as far as they can, but have reached a vulnerability ceiling despite mature processes. The problem isn’t from a lack of effort but a shift in the battlefield. Threats come in at machine speed, creating proof of concepts and exploiting vulnerabilities like React2Shell and BeyondTrust (CVE-2026-1731) within hours of disclosure. Any security process, including human input, now introduces delay — and therefore exploitability.

In previous years, security teams moved away from trying to see everything to seeing the right things. Now, the speed of attackers and the introduction of AI in security are forcing some organizations to trust machines with decisions rather than only recommendations. In large enterprises, risk reduction depends more on the use of autonomy than perfection. With too much telemetry, alerts, and attack surface for humans to keep up, doing something that is AI-driven is better than doing nothing at all. Agentic AI is the next step in cybersecurity because at cloud speeds, machine action is becoming more valuable than machine analysis alone.

---

## It’s time for agentic AI vulnerability management

### When hard work stops paying off
This year’s data points to something that a majority of security teams and developers have felt for a while now: vulnerability management is reaching the limits of human scale. It’s possible that we’ve reached a threshold for vulnerability management, even with mature tools, improved prioritization, and well-formed processes. The percentage of critical and high vulnerabilities in use remains largely unchanged since last year — a number that had consistently fallen year over year from 2023 to 2025. According to the data, organizations still have approximately 5.5% of vulnerable images present in running workloads this year. That plateau matters, because continued progress requires a new approach to the process.

![Chart showing 2026 breakdown of workloads with critical or high vulnerabilities: 83% have a fix available, 5.5% are in use, and 0.18% have an exploit available.]

### What are the right human-defined guardrails?
Humans can still guide agentic processes. Advocating for agentic security does not mean removing humans from the loop; it simply means redefining their roles. Humans can define the following:

- Write policies to define change limits.
- Scope permissions and privileges.
- Deterministic rollbacks.
- Audit logs, output, and explainability of agents.
- Risk thresholds with environmental context.

Without guardrails, agents will introduce operational risk at some point in their lifetime. Humans can advance with machine-speed security when they define and govern it.

### How security maturity breaks down bloat
Organizations are prioritizing and cleaning up the security mess left behind by the AI boom of 2025. That is, the excessive number of unused packages that come along with open source images but do nothing for your organization’s use case. After analyzing nearly 13 billion packages for image bloat, less than 1% of packages in images were unused, a reduction of 50% year over year.

### A vulnerable operating system paradox
In reviewing the top host and container operating systems with critical vulnerabilities, the majority are not end of life (EOL). In fact, the newest, actively maintained operating system (OS) versions show the highest concentration of reported critical vulnerabilities. Non-EOL hosts account for 80% of the top 10 OSs with critical vulnerabilities. Similarly, non-EOL container OSs contain 75% of critical vulnerabilities in the top 10. Risk lives where innovation grows.

---

## Defending the cloud-native battlefield

### Organizations prefer behavioral detection fidelity
Many triggered detections are often the result of developers or engineers simply trying to do their job: a container spawning a shell, a process accessing sensitive files, or an identity elevating privileges. These false positives create a lot of noise for security teams and lead to the infamous alert fatigue that many security operations center (SOC) analysts feel day in and day out.

More than 70% of organizations are using stateful detections, or behavior-based rules, across 91% of their cloud environments. The high usage of stateful detections is a clear validation that behavior-based rules are the modern standard for evaluating fewer high-fidelity alerts over raw volume.

### The rise of autonomous response
Automation used to mean tickets and dashboards; now it means decisions. For three years we’ve been reporting on automated incident responses such as killing, pausing, or stopping a container, and every year we’ve seen an increase in the number of organizations using these actions for an increasing number of runtime detection policies.

The most significant change was in the autonomous use of the “kill -9” command to kill a process following a threat detection alert. There was a 140% increase in organizations using the command across 132% more policies than last year when this policy was first enabled.

---

## AI adoption matures

AI is now an invaluable tool in the arsenal of both attackers and defenders. Threat actors use it for more than just enhanced social engineering campaigns and reconnaissance. The Sysdig TRT has found a malware script that was up to 95% AI-generated and an AI-assisted account takeover in less than 10 minutes.

### AI evolves from consumable to infrastructure
This year’s data makes one thing clear: the majority of organizations are making and shaping AI. We analyzed over 1 million more AI and ML packages than we did last year, and found strong signals indicating that AI adoption is moving from the “toy” phase to a permanent part of infrastructure. There was 25 times growth in the number of AI-specific packages year over year.

### Who leads in AI adoption
It is clear that business-to-consumer (B2C) organizations like media and internet, transportation, and retail business sectors are leading with internal AI and ML deployments as shapers and makers. Since these industries rely greatly on end user and customer happiness, building their own, deeply integrated and unique internal AI tools is important to having a competitive edge.

---

## Identity is the cloud-native perimeter

Cloud identities are the new “firewall” of modern infrastructure. They exist to provide access to users (developers, operators, security teams) and machines (workloads, pipelines, services) to build, maintain, and connect the infrastructure.

### Humans are inherently risky
We defined a risky user as a human-owned account meeting at least one of the following parameters:
- Administrator privileges.
- No multifactor authentication enabled.
- Having access keys that are not rotated.
- Inactive for 90 days.

On average, 67% of user identities are considered risky across all CSPs.

### Machine identity risk is a priority
The number of machine identities continues to grow by orders of magnitude over human identities. However, even with the increasing number of AI tools and MCP servers with elevated privileges, we witnessed a sharp decline in the risk associated with nonhuman identities that varies based on CSP.

---

## Growth of the open source runtime security community

There are over 9,000 organizations using Falco, ranging from interested parties and those testing out the tool to persistent, longtime users. Falco is an open source cloud-native runtime security tool that offers real-time detection, alerting on abnormal behaviors and potential security threats.

### Open source is a universal language
Falco has roots that spread across the world with persistent growth year after year; it’s a global standard for runtime detection, especially in those countries that require data sovereignty and covet open source.

- Europe: 34.43%
- Asia: 30.07%
- North America: 26.72%
- South America: 3.34%
- Africa: 3.42%
- Oceania: 2.02%

---

## Conclusion
The rise of open source runtime security mirrors the shifts seen throughout the report: humans cannot continuously tune permissions, triage alerts in real time, or outpace exploit weaponization. What they can do is build and trust systems that operate at the timescales necessary to act quickly.

## Methodology
The data in this report is based on anonymized, aggregated data from Sysdig’s customer base, including runtime activity, vulnerability scanning, and identity configurations, as well as threat intelligence gathered by the Sysdig Threat Research Team (TRT) and community usage data from the Falco project. Analysis covers the period from January 2025 through December 2025.

---

do so, organizations should:

  Adopt runtime as a
foundational control.

  Align runtime detections
with regulatory and

sovereignty requirements.

  Use high‑fidelity, behavior‑based
runtime detections that can safely

Invest in human‑driven detection

power autonomous response.

engineering to drive rule tuning,

  Leverage open source security
tools to increase transparency,

auditability, and breadth of

detection logic.

validation, and maintenance as a

precursor to safe agentic security.

2026 CLOUD-NATIVE SECURITY AND USAGE REPORT
45

Security and perfection are certainly not

synonymous, and that’s not what we’re

pushing for. Mature security operations

prioritize the right priorities over every‑

thing, at scale. Organizations are already

trusting machines to make recommenda‑

tions and complete tasks to enhance busi‑

ness operations. The next step is trusting

them with security workflows and deci‑

sions to keep those business operations

moving forward.

Agentic AI isn’t a leap of faith, but the

logical progression of security automa‑

tion. Once detection and response are

Conclusion

We’ve officially moved past human scale

in  cloud  security.  We’re  entering  the

machine‑scale era.

Some attackers have been operating at

trusted,  autonomous  prevention  and

machine speed for a few years now. At

remediation are the obvious next frontier.

this point, the risks in cloud environments

The goal is real risk reduction beyond the

will persist, as humans cannot manually

limits of human speed and scale.

clear the multiple security backlogs fast

enough. From this year’s data, we see

that the transition is already underway

with  improvements  to  signal  concen‑

tration and higher fidelity, growing trust

in  automated  actions,  and  a  focus  on

reducing the right risks first.

2026 CLOUD-NATIVE SECURITY AND USAGE REPORT46

Methodology

The  “2026  Cloud‑Native  Security

and  Usage  Report”  is  built  from  the

real‑world  telemetry  and  behavioral

patterns of hundreds of thousands of

cloud accounts and billions of Kuber‑

netes containers secured by Sysdig daily.

This year’s analysis represents our most

expansive datasets to date, reflecting

a modern landscape with growing and

expanding  data  given  the  shift  from

manual to autonomous practices.

From  agile  startups  to  multinational

enterprises, our anonymized data spans

a  wide  range  of  cloud‑savvy  organi‑

zations  across  the  globe,  ensuring  a

representative view of security matu‑

rity. We also used Scarf for open source

project  usage  analysis  to  facilitate

data gathering.

Our  findings  provide  a  look  at  the

evolving tactics of attackers and defen‑

sive shifts within cloud‑native ecosys‑

tems. Sysdig, with roots in Wireshark,

Falco, and Stratoshark, is passionate

about  the  open  source  philosophy  of

information sharing. The concepts and

analyses in this report are a culmina‑

tion of insights from engineers, product

managers, threat researchers, marketers,

and executives whose perspectives span

the  organization,  providing  you  with

the actual changing aspects of cloud,

container, and security trends.

2026 CLOUD-NATIVE SECURITY AND USAGE REPORT47

Where does our data come from?

Business sector

Software 32.3%

Business services 18.3%

Finance 15.4%

Manufacturing 5%

Other 5%

Telecommunications 4.1%

Retail 3.4%

Hospitality 2.9%

Government 2.5%

Energy, waste, utilities 2.3%

Media & internet 2.3%

Insurance 2%

Education 1.8%

Transportation 1.8%

Hospitals & clinics .7%

Legal .2%

Location

AMER 41%

APAC 22%

EMEA 37%

2026 CLOUD-NATIVE SECURITY AND USAGE REPORTG E T   A   D E M O

COPYRIGHT © 2026 SYSDIG,INC.

ALL RIGHTS RESERVED.

RP-017 REV. A 04/26

USAGE REPORTSysdig helps security and development teams prevent, detect, and respond to threats  instantly. No guesswork.  No black boxes. Just cloud  security, the right way.