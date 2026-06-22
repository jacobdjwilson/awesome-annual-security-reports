# Dataminr 2026 Cyber Threat Landscape Report

## Table of Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Executive Summary](#executive-summary)
- [The Cyber Risk Landscape](#the-cyber-risk-landscape)
- [Vulnerabilities](#vulnerabilities)
- [Digital Risk](#digital-risk)
- [Malware](#malware)
- [Dual use tools](#dual-use-tools)
- [2025 Financial Impact Trends](#2025-financial-impact-trends)
- [The Rise of the “Mega-Loss”](#the-rise-of-the-mega-loss)
- [Changing Tactics for the Attacker and Company](#changing-tactics-for-the-attacker-and-company)
- [Threat Actor Activity](#threat-actor-activity)
- [High Impact Groups](#high-impact-groups)
- [Group Summaries](#group-summaries)
- [Threat Actor Spotlight: jrintel](#threat-actor-spotlight-jrintel)
- [Operational Evolution](#operational-evolution)
- [Most active actors by alert volume](#most-active-actors-by-alert-volume)
- [Conclusion](#conclusion)
- [Appendix 1](#appendix-1)
- [About Dataminr & ThreatConnect](#about-dataminr--threatconnect)

---

## Introduction
The 2026 Cyber Threat Landscape Report comes at a time when security and risk analysts, operators, and agencies are both under immense pressure from being critically understaffed and an overwhelming volume of cyber events occurring every day. These events contribute to a rapidly expanding threat landscape that has been put into overdrive due to malicious use of AI that lowers the barrier to entry for unskilled actors and greatly increases the capabilities of advanced adversaries. Keeping up with the resulting chaos of today’s cyber risk landscape is an ever-growing challenge.

This report looks at data from calendar year 2025. Using aggregated data from our industry-leading dataset and the expertise of leading cybersecurity experts, we are able to identify global trends and information. Dataminr ingests more than 43 terabytes of event, threat, and risk signals every day—an unmatched amount of data aggregation that feeds more than 55 proprietary LLMs and Agentic AI solutions as well as thousands of detection models.

These detections are further augmented and enriched with a proprietary knowledge graph of over 3 billion entities including unique IOCs and other objects. With Dataminr, customers gain the foresight they need to implement predictive and preemptive measures against possible threats, focus on threats with the most potential impact to their organization, and take the right action when every second counts.

Dataminr’s detection models constantly identify, validate, and correlate risk signals from more than 1 million data sources. These sources include all the places that APTs, cybercrime groups, and lone wolf actors leave digital footprints, allowing Dataminr to detect activity across new and existing Telegram channels, data dump sites, breach forums, and any developments across the deep and dark web with unmatched speed and precision. With the acquisition of ThreatConnect, Dataminr now also includes critical cyber incident loss data that enables sophisticated risk quantification metrics for unified threat intelligence, greatly enhancing the data conveyed in this report and the value it provides security teams worldwide.

In the report, you will find security trends and analysis relevant to your security operations and organization—threat actor activity, external digital risks, frequently exploited vulnerabilities, and more. Moving beyond just the security operation centers (SOCs), it will also help readers understand business impact by quantifying the risk associated with vulnerabilities and malware.

The trends and data in this report not only represent the evolution of the threat landscape, but show how critical it is that SOCs are provided with the most accurate, relevant intelligence possible. When these teams are served up the latest intelligence about the most likely secondary and tertiary threats to their unique environment that could emerge, they gain precious minutes or hours needed to stay ahead of malicious actors.

## Methodology
This report was written with both qualitative and quantitative approaches and relied primarily on data from Dataminr and ThreatConnect. In the event a data point was sourced from third parties, it was noted as such. The goal of the report is to provide cybersecurity teams with actionable insight into the cyber threat landscape as it has evolved over the past year so they can understand trends that would be helpful for the ongoing protection for their organization or agency.

## Executive Summary
Dataminr’s 2026 Cyber Threat Landscape Report aggregates global cyber intelligence to provide security leaders with a clear, quantified view of evolving risks—from the exponential rise in identity-centric attacks and high-impact “mega-losses” to the persistent threats posed by sophisticated, well-funded criminal and state-aligned groups.

Our analysis confirms that the window of time between targeting, initial access, and payload execution or data exfiltration has greatly diminished. This makes proactive, context-rich, and even predictive threat intelligence the non-negotiable requirement for organizational resilience in 2026.

### Key statistics from 2025
- **5,000+**: threat actors tracked
- **225%**: increase in monthly threat actor alerts from 2024-2025
- **18,000+**: alerts on ransomware activity
- **2,000,000+**: domain impersonations
- **425,000+**: instances of brand fraud
- **110,000+**: alerts on doxxing or leaked credential databases

### Dominant Threat Actors and Tactics
- **Qilin**: Identified as the most active ransomware group of 2025, Qilin consolidated the market by offering high payouts and a stable platform for affiliates.
- **Cl0p**: This group utilized a “restraint and precision” strategy, focusing on encryption-less extortion to siphon terabytes of data while maintaining a low profile.
- **Scattered Lapsus$ Hunters**: Demonstrated the vulnerability of the “human element” by using AI-enhanced social engineering to bypass technical security measures.
- **NoName05716**: Remained the most active pro-Russian hacktivist collective, primarily utilizing crowd-sourced DDoS attacks against critical infrastructure.

### Critical Vulnerabilities
The report emphasizes that technical severity based on the common vulnerability scoring system (CVSS) does not always equal business risk. While there were certainly high-scoring CVEs that also carried high remediation costs, such as CVE 2025-55182, it is always important to layer in factors such as likelihood of exploitation, potential business impact, and frequency of targeting. This allows organizations to move beyond the very binary approach of whether the CVSS score deems a vulnerability important enough for their teams to patch them.

## The Cyber Risk Landscape
It is impossible for humans alone to keep tabs on everything happening that presents cyber risk. Regardless of size, every organization and government agency has a complex infrastructure of assets to manage. For larger ecosystems, that number could reach millions of endpoints, software versions, and individuals across the globe that could be exposed to risk. All of these contribute to a complex web of assets and telemetry across an organization’s infrastructure that need to be constantly evaluated, monitored, and protected.

### Our View of the 2025 Cyber Risk Landscape
- **6.3M+**: External threat alerts (Ex: Malware, hacktivism, ransomware, APTs)
- **4.8M+**: Vulnerability alerts (Ex: Exploits, emerging vulnerabilities, disclosures.)
- **3.1M+**: Digital risk alerts (Ex: Domain impersonation, phishing, doxxing, data exposure)

## Vulnerabilities
Software vulnerabilities can be highly effective points of initial compromise and access for a threat actor—especially when they’re discovered in widely-used solutions. Threat actors are constantly poking and prodding at software to find mistakes in code and bypass security measures. These risks could also present themselves at other points of an organization’s supply chain if a deeply integrated technology is compromised, which unknowingly creates an access point to sensitive information.

Once the actor finds a way to exploit a weakness, their next step will depend on their end objectives. Many will try to sell the exploit code or tailored access by advertising it for sale on Dark Web forums or in Telegram channels. Some will take the riskier, but potentially more lucrative step, which is to use the exploit to access an organization’s valuable data and either exfiltrate it, sell it or render it inaccessible as part of a ransomware attack.

Threat actors have long made practice of analyzing newly published vulnerabilities and newly released patches to understand where weak points may exist and reverse-engineer vulnerabilities to target systems that remain unpatched. This window of opportunity between when a vulnerability is disclosed, when the patch is released, and the vulnerable system is actually patched by system owners is frequently when the attacker has their best chance of success.

However, in 2025, the security landscape was defined by a “patch bypass epidemic,” where critical fixes for major platforms were often immediately re-exploited due to incomplete root-cause remediation by the software vendor. The most prominent example was observed with a Microsoft SharePoint vulnerability, where attackers bypassed the initial July patches (CVE-2025-49706/49704) within days by using simple path traversal techniques, forcing the issuance of new CVEs (CVE-2025-53770/53771) for the same underlying flaws.

![Vulnerability Reexploitation SharePoint Toolshell with Dataminr alerting enhanced by ReGenAI and Intel Agents.]

This pattern was repeated in Windows Server Update Services (WSUS) and SAP NetWeaver, where initial patches for critical vulnerabilities failed to account for all deserialization vectors, necessitating emergency out-of-band updates and secondary CVE assignments. Similarly, Grafana attempted to fix a vulnerability using client-side restrictions that were easily circumvented, rather than validating server-side input. Collectively, these four incidents highlighted a systemic failure in “variant analysis,” leaving organizations vulnerable even after applying vendor-supplied updates.

In addition to this challenge around re-exploitation, teams are monitoring and managing tens of thousands of new vulnerabilities every year. Many are rated “High” or “Critical” based on their Common Vulnerability Scoring System (CVSS) scores, which only take into account the technical impacts. While CVSS remains useful for understanding exploit mechanics, it provides limited insight into which vulnerabilities actually matter to a specific organization. Without additional context, security teams are left with an undifferentiated backlog of critical findings that obscures what truly warrants action, investment, and executive attention. A consistent observation is that severity does not always equal risk.

![CVE risk impact matrix]

Adopting this approach enables security leaders to distinguish between vulnerabilities that are noisy but economically bounded and those that present systemic, enterprise-level exposure. More importantly, it represents the path forward for modern threat intelligence and vulnerability analysis—one that connects technical findings to business outcomes, aligns remediation with actual risk, and supports defensible, data-driven decision-making at both the operational and executive levels.

## Digital Risk
Aside from direct threats or vulnerabilities, organizations also need to be aware of external factors that could pose serious challenges in regards to third-party risks, brand reputation, and potential compliance violations. This is referred to as digital risk, which encompasses challenges such as domain impersonation, brand abuse in phishing campaigns, brand fraud, hacking services for sale, doxxing and leaked credentials, intellectual property and other data leaks.

| Metric | Count |
| :--- | :--- |
| Domain impersonation alerts | 2,000,000+ |
| Phishing alerts | 443,000+ |
| Company fraud alerts | 424,000+ |
| Hacking services alerts | 185,000+ |
| Doxxing or leaked credentials alerts | 109,000+ |
| Data exposure or breach alerts | 86,000+ |

Events tied to these risk vectors typically occur outside of an organization’s immediate purview. For example, if a third-party (or third-party software) is breached and an organization’s customer or employee credentials are compromised, it might take days or weeks for their security team to become aware of the incident. In that time, the threat actor has a window of opportunity to quietly advance their attack on customers or enter their infrastructure and execute a further damaging attack.

If customer data is part of a breach, the organization could suddenly be held accountable for the financial implications—especially if there are any compliance violations involved. In some cases, threat actors will use a tactic called double extortion and threaten to notify the SEC or equivalent government body about a ransomware attack if the target organization doesn’t pay up. For public sector organizations, that same scenario can lead to national security risks and help adversarial nation-states sow distrust in the government by claiming to have accessed the most personal data about citizens.

![Threat actor group Scattered LAPSUS$ Hunters (SLH) exhibits its use of double extortion in its Telegram channel.]

Domain impersonation, brand fraud, and phishing kits targeting an organization all threaten the integrity of an organization. Depending on the actor’s intentions, these can be used to target both customers and employees. While most sizable organizations operate under the assumption that there is likely an actor out there executing one of these attacks and therefore have protections in place against the eventual compromise that could take place, there’s a fine line between commodity phishing kits and an advanced, multi-pronged attack that fraudulently represents an organization.

Doxxing, data breaches, and leaked credentials represent a more imminent threat to an organization’s systems, data, and employees. Data breaches are often the sources of follow-on activity like doxxing or leaked credentials, which makes it critical for an organization to know when a threat actor might be advertising their data for sale on a Dark Web forum or Telegram channel. With that knowledge, that organization can at least try to get ahead of eventual compromise by instituting proactive measures like company-wide password resets and additional monitoring for anomalous user behavior.

It’s also important for an organization to know when a third-party vendor with access to sensitive data or systems is involved in a cyber attack or data breach. This can also extend to cloud infrastructure platforms that, if compromised, could unintentionally end up exposing customer instances. Being notified as early as possible about a possible breach elsewhere in the digital supply chain can be the difference between having a window of opportunity to remove any connection with the compromised platform and dealing with a significant data breach.

![Timeline of key events pertaining to the PowerSchool breach as detected by Dataminr]

## Malware
SOC teams must be aware of chatter across the Dark Web, Telegram channels, and other places where adversaries discuss their next move or what tools they’re finding most effective. They also need to know when independent researchers and other security teams come across novel malware or see a resurgence of existing malicious tools. This section provides an overview of the malware families with the most aggregate alerts from all sources in the Dataminr platform.

Beyond just knowing about the malware families, understanding how they’re used, when activity associated with them is spiking, and what they target is crucial. For instance, knowing if a specific malware family is being deployed against a peer organization in a certain industry can be highly beneficial to informing proactive defensive posture. Threat actor groups frequently stick to successful methods, so if they manage to compromise several organizations within one industry using a particular type of malware, they are likely to repeat that attack chain.

| Malware Family | Description | Behavior |
| :--- | :--- | :--- |
| Mirai | Exploits weak default credentials and vulnerabilities in devices like routers and cameras to form massive botnets. | Can generate traffic bursts over 100 Gbps, targeting various sectors. Its proliferation and adaptation pose a growing risk to critical infrastructure. |
| Lumma Stealer | Sophisticated, MaaS infostealer distributed through Russian forums. | Uses anti-debugging and custom XOR obfuscation for evasion. Stolen data is exfiltrated via HTTP POST to a C2 server, delivered as EXE, DLL, or PowerShell. |
| Formbook | Also tracked as xloader (MaaS) infostealer, stealing browser credentials, keystrokes, clipboard content, screenshots, and web form data, and can download other files. | Employs sophisticated evasion techniques, including DLL search order hijacking, generating mutex names using SHA-1 hashes, and resolving API addresses with CRC32/RC4 encryption. |
| Rhadamanthys | MaaS infostealer. Linked to Hidden Bee, its authors treat it as a long-term business, selling it for a monthly fee via Tor and Telegram. | The multi-stage infection uses loaders and employs new anti-analysis checks and a proprietary “XS” file format to evade PE parsers. Recent versions added browser fingerprinting. C2 configuration allows multiple servers and is downloaded as PNGs. Communication uses WebSocket with RC4-encrypted strings. |
| VoltRuptor | ICS & SCADA-specific malware strain reportedly developed by Russia-aligned hacking group Infrastructure Destruction Squad (IDS). | Designed for cross-platform operations. It features multi-protocol support, as well as persistence and anti-forensics capabilities. |
| Agent Tesla | Keylogger and RAT that captures clipboard data, screenshots, and audio/video. | Accepts nearly 40 commands for file management, command execution, process manipulation, and loading additional malware. The latest activity also utilizes .NET executables to decode and inject variants into processes. |
| NjRAT | RAT used for unauthorized system control. Facilitates malicious activities like keylogging, credential theft, webcam access, ransomware deployment, and system manipulation. | Collects data, disables security tools, manages files, and modifies Registry keys, typically spreading via phishing and drive-by downloads to grant command-line access. |
| Remcos | RAT that grants attackers full control over infected systems for data exfiltration and keystroke logging. | Evades detection using obfuscation, API hash values, Vectored Exception Handling, and process hollowing. Suspends legitimate processes (like a renamed “dllhost.exe”), injecting code, then resumes them. |
| ASyncRAT | Stealthy, polymorphic RAT targeting Windows. Capabilities include screen control, keystroke logging, file exfiltration, webcam capture, and remote desktop. | Achieves persistence by modifying the registry or creating new services, and evades detection using encrypted communications and anti-analysis techniques. Exfiltrates system data to a C2 server and can execute various commands, including downloading plugins, terminating processes, and updating itself. |
| Brickstorm | Sophisticated, cross-platform backdoor malware primarily used for long-term cyber espionage. Attributed to People’s Republic of China (PRC) state-sponsored threat actors. | Uses advanced techniques to hide its command-and-control (C2) traffic, including DNS-over-HTTPS (DoH), nested TLS encryption, and WebSockets. This makes its malicious traffic look like legitimate web browsing. Includes a “self-watching” function that automatically restarts or reinstalls itself if it is killed. It also modifies system initialization scripts to ensure it survives reboots. |

## Dual use tools
In addition to outright malicious software, it’s also important to be aware of tools that are legitimate, but can be leveraged by threat actors for malicious activity. This falls under the umbrella of a tactic known as “living off the land”, which implies that the threat actor is able to infiltrate the organization and use existing tools, binaries, and scripts to execute malicious activities. This is not a novel tactic, and as such there is an open-source project known as Living Off The Land Binaries, Scripts, and Libraries (LOLBAS) meant to catalogue all binaries, scripts, and libraries that can be used in this tactic.

While these tools shouldn’t be used without internal oversight, they’re so widely used for legitimate reasons that they’re rarely on block lists.

| Tool | Primary Legitimate Use | Why Threat Actors Use It |
| :--- | :--- | :--- |
| Metasploit | The industry standard for penetration testing and exploit development. | Provides a massive library of ready-to-use exploits to break into systems. |
| Interactsh | Testing for “Out-of-Band” (OOB) vulnerabilities like SSRF or Blind SQLi. | Used to confirm if an exploit worked by pinging a server they control. |
| Sliver | An open-source adversary simulation (C2) framework. | A powerful, free alternative to expensive tools like Cobalt Strike. |
| GoPhish | An open-source phishing framework used by companies to train employees. | It makes setting up and tracking a mass phishing campaign very easy. |
| Burp Suite | The leading tool for web application security testing. | Used to intercept and modify web traffic to find or exploit web vulnerabilities. |
| Hak5 Cloud | Managing Hak5 hardware (like the Rubber Ducky or WiFi Pineapple). | Allows remote control of physical hardware used to compromise local networks. |
| Mythic | A modular, collaborative C2 framework for Red Team operations. | Its modular nature makes it very hard for defenders to create a single "fingerprint." |
| Cobalt Strike | High-end commercial software for adversary simulation. | The “gold standard” for professional hacking. Attackers often use cracked versions. |
| XMRig | A high-performance, open-source Monero (cryptocurrency) miner. | The most abused on this list. It is frequently bundled into malware for "cryptojacking." |
| Havoc | A modern, open-source C2 framework focused on evasion. | Designed to bypass modern antivirus (AV) and EDR, making it perfect for stealth. |

## 2025 Financial Impact Trends
From a financial loss perspective, 2025 marked a clear shift from “frequent but contained” cyber losses toward fewer events with materially larger financial and mission impact. While ransomware volumes stabilized, single-incident losses increased, driven by multi-vector attacks that combined credential theft, data exfiltration, operational disruption, and regulatory exposure into one event.

The most consequential losses increasingly stemmed from identity compromise, third-party concentration risk, and exploitation of trusted business processes, rather than purely technical exploits—pushing cyber risk firmly into the category of balance-sheet and earnings volatility, not just security operations cost.

## The Rise of the “Mega-Loss”
The Normalized Severity Distribution confirms that 2025 is the year of the “tail event.”

![The Normalized Severity Distribution]

This chart illustrates a rightward shift in loss severity from 2024 to 2025. While both years show low probability at the extremes—small losses and catastrophic ($1B+) events—the median loss was higher and more frequent in 2024, reflecting a greater concentration of moderate, repeatable incidents. In contrast, 2025 exhibits a thinner middle but a heavier tail, indicating fewer typical losses yet a meaningfully higher probability of very large, outlier-driven cyber loss events, consistent with increased systemic and concentration risk.

## Changing Tactics for the Attacker and Company
Attack types have become more specialized and impactful per incident.

- **Identity is the new perimeter**: Nearly one in three (30%) cyber intrusions now involve the use of valid credentials—attackers are “logging in” rather than “breaking in.” This is fueled by an 84% increase in infostealer malware delivered through phishing.
- **Phishing resilience**: Phishing remains the dominant intrusion vector in 60% of cases. By early 2025, AI-supported phishing campaigns represented over 80% of observed social engineering activity worldwide.
- **Payment refusal trends**: Despite higher severity, organizations are pushing back; 63% of organizations opted not to pay ransoms in 2025, up from 59% in the prior year.
- **Supply Chain Gravity**: One in four modern breaches now exploits a third-party vulnerability (CVE), escalating the risk magnitude by 20% compared to direct internal attacks. This “Vendor Pivot” is characterized by extreme velocity; 96% of these vulnerabilities are weaponized within the same calendar year of disclosure, frequently bypassing internal detection and resulting in twice the data impact per incident.

## Threat Actor Activity
Over the course of 2025, threat actor activity consistently increased and represents a significant jump from 2024. In fact, there was a sizable 225% increase in average monthly alerts (1,490/month to 4,840/month), with the busiest month in 2024 not even reaching the quietest month in 2025.

![Threat Actor Activity: 2024 vs 2025]

For any team tasked with protecting against cyber threats, they face the challenge that the dwell time between initial breach and catastrophic data theft has effectively been reduced to zero, making the earliest possible signaling of a campaign a critical requirement for survival. Because these modern adversaries often use dual-use administrative tools to “live off the land” once inside, traditional signature-based detection is often ineffective.

## High Impact Groups
Advanced collectives moved away from traditional software exploits in favor of “identity-centric” warfare, where the human element became the primary entry point through AI-enhanced social engineering. The group that most prominently executed the identity-centric playbook was Scattered Lapsus$ Hunters, or SLH, an alliance of three sub-groups of the cybercrime collective known as The Com.

Simultaneously, the focus shifted from simple system disruption to massive, “encryption-less” data exfiltration. By weaponizing zero-day vulnerabilities in common enterprise file transfer and resource planning platforms, these actors were able to compromise handfuls of organizations in a short window, holding corporate reputations and proprietary intellectual property hostage rather than merely locking down operational files.

## Group Summaries
- **Cl0p (Russia)**: Highlights a “restraint and precision” strategy. By avoiding the noise of system encryption, they maintain a lower profile while dwell-time increases.
- **Scattered Lapsus$ Hunters (US & UK)**: Proved that technical “un-hackability” is irrelevant if the human at the help desk can be manipulated.
- **Infrastructure Destruction Squad (IDS) / Dark Engine (Russia)**: Emerged in 2025 as a highly aggressive and technically capable “hacktivist” with close alignment to state-level strategic interests.
- **Qilin (Russia)**: By providing the most stable platform and high payouts, they effectively consolidated the ransomware market.
- **Everest (Likely Russia)**: Acts as both the intruder and the broker, becoming a “force multiplier” for the entire cybercrime economy.
- **JR Intel (Europe)**: Represents the “Data Brokerage” evolution of cybercrime, where stolen intellectual property often exceeds the value of a ransomware payout.
- **Inc Ransom (Likely Russia)**: Success stems from their “business-like” reliability, gaining a reputation for providing working decryptors upon payment.

## Threat Actor Spotlight: jrintel
jrintel (also known as JR Intel, hubz, or hubzXjrintel) is a high-profile, financially motivated mercenary information broker that emerged in August 2025. Unlike state-sponsored groups, jrintel operates as an opportunistic independent broker, specializing in trafficking sensitive military, intelligence, and government data from a wide range of geopolitical adversaries.

## Operational Evolution
The actor’s capabilities have evolved rapidly through three distinct phases:
1. **Military Technical Espionage (Aug–Oct 2025)**: Focused on high-tech military hardware to establish credibility.
2. **Broad Intelligence & PII Theft (Nov–Dec 2025)**: Expanded into bulk personal identifiable information (PII) and civilian databases.
3. **Hybrid Operations & Services (Dec 2025–Jan 2026)**: Transitioned into “Espionage-as-a-Service,” merging digital theft with physical-world activities.

## Most active actors by alert volume
This section dives into the most active actors by alert volume over the course of the year. Unsurprisingly, these actors are more focused on less sophisticated and highly repeatable attacks like DDoS.

- **NoName05716**: The most active pro-Russian hacktivist collective, utilizing crowd-sourced DDoS attacks and gamification.
- **Hezi Rash (Black Force)**: A relatively new but hyper-aggressive Kurdish nationalist group.
- **Keymous+**: Represents the 2025 trend of “mercenary hacktivism”—groups that use ideological slogans to build a brand for their commercial DDoS services.
- **RomCom (Storm-0978)**: One of the most sophisticated “hybrid” actors, seamlessly switching between state-aligned espionage and high-value financial theft.

## Conclusion
The findings in this report demonstrate two critical, undeniable takeaways for any enterprise or government security team: the power of interconnected intelligence and the need for purpose-built AI to handle the chaos of today’s cyber threat landscape.

A siloed view of cyber risk and threats is no longer viable. Organizations must move toward:
- **Holistic Visibility**: Merging vulnerability data with real-time threat actor activity and external digital risks.
- **Contextual prioritization**: Layering in the likelihood of exploitation and frequency of targeting given an organization’s unique infrastructure.
- **Operational resilience**: Connecting technical findings to business outcomes to protect the balance sheet from “mega-losses.”

## Appendix 1
- **CVE-2025-55182**: CVSS 10.0. An unauthorized RCE vulnerability allowing attackers with no authentication to run arbitrary code. Likelihood: Very High. Financial Risk: $$$$$
- **CVE-2024-1709**: CVSS 9.8. Critical authentication bypass in ConnectWise ScreenConnect. Likelihood: High. Financial Risk: $$$$
- **CVE-2025-53770**: CVSS 9.8. (Details pending)

## About Dataminr & ThreatConnect
Dataminr, now together with ThreatConnect, remains dedicated to its mission of delivering the most relevant and accurate AI-powered real-time event, threat & risk intelligence to its customers. Combining best-in-class intelligence with more than a decade of experience building a platform with AI at its core, Dataminr ensures its customers receive the most relevant and accurate intelligence with unmatched speed, scale, and accuracy.

---

RISK
($-$$$$$)
| oolShell—a remote        | Beyond patching,     | Moderate | $$$$ |
| ------------------------ | -------------------- | -------- | ---- |
| code executing (RCE) in  | users should enable  |          |      |
on-premises Microsoft  Antimalware Scan  This CVE exploits on  The impact of the
SharePoint Server that  Interface (AMSI) in  premise SharePoint  SharePoint CVE would
allows an unauthenticated  sharepoint to ensure EDR  installations, which means  involve remediation, DFIR,
|                            |                             | an attacker would first  | and operational impacts at  |
| -------------------------- | --------------------------- | ------------------------ | --------------------------- |
| attacker to run arbitrary  | platforms are set up to     |                          |                             |
|                            |                             | have to bypass existing  | a minimum. These could      |
| code on the SharePoint     | detect this type of attack. |                          |                             |
server over the network. controls in order to exploit  range from $500K to $10M
|     |     | this CVE. | (depending on the size of  |
| --- | --- | --------- | -------------------------- |
the company). If this CVE
leads to a data breach
or Ransomware Event,
the impacts could easily
exceed $50M to $100M+.
CVE-2025-32433
CVSS: 10 | At-risk industries: Telecommunications | Overall Risk: High
| ABOUT |     | IMPACT |     |
| ----- | --- | ------ | --- |
FINANCIAL RISK
| DESCRIPTION           | MITIGATION STEPS       | LIKELIHOOD OF IMPACT | ($-$$$$$) |
| --------------------- | ---------------------- | -------------------- | --------- |
| A critical remote     | Patch the CVE or use   | Very High            | $$$       |
| code execution (RCE)  | firewalls to restrict  |                      |           |
vulnerability in the SSH  SSH access to trusted  Internet facing machines  Impacts would include
server implementation  management hosts only. can be exploited by  remediation ($3-15M),
|     |     | attacks that do not require  | containment ($1- |
| --- | --- | ---------------------------- | ---------------- |
of the Erlang/OTP (Open
|     |     | authentication. | 5M), and exposures  |
| --- | --- | --------------- | ------------------- |
Telecom Platform). Could
| grant attackers full access  |     |     | via Ransomware or      |
| ---------------------------- | --- | --- | ---------------------- |
| to a system.                 |     |     | Databreach ($15M-100M) |
@ 2026 Dataminr. All rights reserved. | DATAMINR.COM
Dataminr 2026 Cyber Threat Landscape Report  | 40

CVE-2025-5777
CVSS: 9.4 | At-risk industries: Financial Services | Overall Risk: High
| ABOUT |     | IMPACT |     |
| ----- | --- | ------ | --- |
DESCRIPTION MITIGATION STEPS LIKELIHOOD OF IMPACT FINANCIAL RISK
($-$$$$$)
CitrixBleed 2— Out-of- Patch the CVE, ensure DLP  Very High $$$
| bounds memory read  | is in place and configured  |     |     |
| ------------------- | --------------------------- | --- | --- |
vulnerability affecting  correctly, and monitor  Internet facing machines  Stealing data is always
Citrix NetScaler ADC  logs and network traffic  can be exploited by  dangerous but the
(Application Delivery  to look for anomalous  attacks that do not require  attacker would have to see
|                         |                             | authentication. | the right data at the right  |
| ----------------------- | --------------------------- | --------------- | ---------------------------- |
| Controller) and Citrix  | authentication and session  |                 |                              |
time to cause material
| NetScaler Gateway  | activity. |     |                              |
| ------------------ | --------- | --- | ---------------------------- |
| depending on       |           |     | impact. The most likely      |
| configuration.     |           |     | costs for this involve DFIR  |
($250K-1.5M) and $1-5M
| Could allow attackers to  |     |     | in remediation (patching,    |
| ------------------------- | --- | --- | ---------------------------- |
| steal memory contents     |     |     | cleanup). If the attack      |
| from the appliance.       |     |     | leads to a data breach, the  |
impact would be much
higher.
CVE-2024-55591
CVSS: 9.6 | At-risk industries: Government | Overall Risk: High
| ABOUT |     | IMPACT |     |
| ----- | --- | ------ | --- |
DESCRIPTION MITIGATION STEPS LIKELIHOOD OF IMPACT FINANCIAL RISK
($-$$$$$)
| A critical authentication  | Patch the CVE and        | Very High | $$$ |
| -------------------------- | ------------------------ | --------- | --- |
| bypass vulnerability in    | ensure http/https admin  |           |     |
Fortinet FortiOS and  interfaces are disabled,  Internet facing machines  Impacts would include
FortiProxy, the core  admin access is restricted  can be exploited by  DFIR ($250k-2M), $2-15M
operating system that  to only trusted IP’s, and  attacks that do not require  for remediation), and if a
|                              |                    | authentication. | ransomware attack were  |
| ---------------------------- | ------------------ | --------------- | ----------------------- |
| runs on Fortinet firewalls,  | remote management  |                 |                         |
to occur, $50M+ (though
| SSL-VPN gateways, and  | interfaces from public IP”s  |     |     |
| ---------------------- | ---------------------------- | --- | --- |
secure proxy appliances. is restricted. the impact to government
agencies would be to the
| It leads to unauthenticated  |     |     | mission, not financial). |
| ---------------------------- | --- | --- | ------------------------ |
remote exploitation (no
code required).
@ 2026 Dataminr. All rights reserved. | DATAMINR.COM
Dataminr 2026 Cyber Threat Landscape Report  | 41

CVE-2025-31324
CVSS: 9.8 | At-risk industries: Manufacturing | Overall Risk: Moderate
| ABOUT |     | IMPACT |     |
| ----- | --- | ------ | --- |
DESCRIPTION MITIGATION STEPS LIKELIHOOD OF IMPACT FINANCIAL RISK
($-$$$$$)
| A Remote Code        | Beyond patching, ensuring  | Low | $$  |
| -------------------- | -------------------------- | --- | --- |
| Exploitation on SAP  | that network access to     |     |     |
NetWeaver that allows for  the vulnerable systems  Typically behind a set of  Customers use SAP for key
Remote Code Execution  (firewall rules, etc) is key. defenses (Firewall, DMZ)  parts of their business and
(RCE) attacks. so attackers have to get  as such, the impact would
|     |     | through existing defenses  | be high (comparable to a  |
| --- | --- | -------------------------- | ------------------------- |
Attackers scan place web  to execute an attack. Nork Hydro—$150M+ in
| shells or arbitrary binaries  |     |     | losses, Maersk—$250M+,  |
| ----------------------------- | --- | --- | ----------------------- |
| and then control the entire   |     |     | or Merck—$300M)         |
system, thus crippling a
company.
CVE-2024-4577
CVSS: 9.8 | At-risk industries: Many | Overall Risk: Moderate
| ABOUT |     | IMPACT |     |
| ----- | --- | ------ | --- |
FINANCIAL RISK
| DESCRIPTION | MITIGATION STEPS | LIKELIHOOD OF IMPACT |     |
| ----------- | ---------------- | -------------------- | --- |
($-$$$$$)
Effectively a bypass of a  Patch the CVE or use WAF  Moderate $$
| long-standing PHP CGI fix  | rules targeting known  |     |     |
| -------------------------- | ---------------------- | --- | --- |
originally implemented to  exploit patterns. Primarily effects windows  Mostly targeted hosted
|     |     | servers with php running  | sites. |
| --- | --- | ------------------------- | ------ |
stop CVE-2012-1823.
in CGI mode. Some
| Attackers gain the same  |     | mitigations (such as WAF    |     |
| ------------------------ | --- | --------------------------- | --- |
| privileges as the web    |     | rules should already be in  |     |
| server processes.        |     | place).                     |     |
CVE-2023-6553
CVSS: 9.8 | At-risk industries: Many | Overall Risk: Low
| ABOUT |     | IMPACT |     |
| ----- | --- | ------ | --- |
DESCRIPTION MITIGATION STEPS LIKELIHOOD OF IMPACT FINANCIAL RISK
($-$$$$$)
@ 2026 Dataminr. All rights reserved. | DATAMINR.COM
Affects Backup Migration  Patch the CVE, disable the  Very High $
| plugin for WordPress. It  | plugin, or restrict public  |     |     |
| ------------------------- | --------------------------- | --- | --- |
allows unauthenticated  access (if possible). No authentication  Most Wordpress usage is
attackers to execute  required to create the  on marketing sites that
arbitrary PHP code on  exploitation. don’t have connectivity to
production systems.
affected servers via a flaw
The impact would be
in the plugin’s file handling
| logic. |     |     | minor |
| ------ | --- | --- | ----- |
Attackers can gain remote
code execution (RCE).
Dataminr 2026 Cyber Threat Landscape Report  | 42

CVE-2024-36401
CVSS: 9.8 | At-risk industries: Government | Overall Risk: Low
| ABOUT |     | IMPACT |     |
| ----- | --- | ------ | --- |
DESCRIPTION MITIGATION STEPS LIKELIHOOD OF IMPACT FINANCIAL RISK
($-$$$$$)
| A remote code execution      | Remove the vulnerable  | High | $   |
| ---------------------------- | ---------------------- | ---- | --- |
| vulnerability in GeoServer,  | library module and/or  |      |     |
an open-source Java  patch. Typically behind a set of  Agencies using Geoserver
server used to publish,  defenses (Firewall, DMZ),  would expect to spend
share, and edit geospatial  so attackers have to get  $500K to $5M per
|     |     | through existing defenses  | affected environment for  |
| --- | --- | -------------------------- | ------------------------- |
data using Open
|     |     | to execute an attack. | remediation. This does  |
| --- | --- | --------------------- | ----------------------- |
Geospatial Consortium
| (OGC) standards—such as  |     |     | not take into account the  |
| ------------------------ | --- | --- | -------------------------- |
| WFS, WMS and WPS.        |     |     | mission impact of losing   |
access to geo data for key
| Exploitation could  |     |     | missions. |
| ------------------- | --- | --- | --------- |
fully compromise the
underlying systems.
| About Dataminr  |     | About ThreatConnect |     |
| --------------- | --- | ------------------- | --- |
Dataminr is the global leader in AI-powered  ThreatConnect provides solutions to enable
real-time event, threat & risk intelligence.  cyber defenders to continuously manage threat
The company delivers the earliest actionable  exposure and improve cyber resilience. Our
intelligence on breaking events, emerging  threat and risk-informed defense products give
threats, and unexpected risks across the physical,  defenders the advantage over adversaries with
digital, and cyber domains. Dataminr first  rich context, risk-based prioritization, and the
pioneered Multi-Modal Fusion AI, synthesizing  ability to quickly and precisely act on emerging
text in 150 languages, image, video, audio, and  threats. Our products span threat, risk, and
sensor signals across 1M public data sources  security operations, and come together in a
to deliver the fastest, most accurate real-time  single intelligence hub. More than 250 global
detection. Dataminr’s AI innovations, including  enterprises rely on ThreatConnect every day to
ReGenAI, Intel Agents, and PreGenAI, build on  contextualize and prioritize emerging threats and  @ 2026 Dataminr. All rights reserved. | DATAMINR.COM
| this foundation by delivering Live Briefs, Agentic  |     | automate defenses. |     |
| --------------------------------------------------- | --- | ------------------ | --- |
AI-powered context, and Predictive Intelligence.
More than 100 U.S. government agencies,
20 international governments, two-thirds of
the Fortune 50, and half of the Fortune 100
trust Dataminr to protect people, assets, and
operations and respond with unmatched speed
and confidence.
Dataminr 2026 Cyber Threat Landscape Report  | 43