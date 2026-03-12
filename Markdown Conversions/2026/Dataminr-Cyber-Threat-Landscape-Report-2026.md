# Dataminr 2026 Cyber Threat Landscape Report

## Table of Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Executive Summary](#executive-summary)
- [Key statistics from 2025](#key-statistics-from-2025)
- [Dominant Threat Actors and Tactics](#dominant-threat-actors-and-tactics)
- [Critical Vulnerabilities](#critical-vulnerabilities)
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

In the report, you will find security trends and analysis relevant to your security operations organization—threat actor activity, external digital risks, frequently exploited vulnerabilities, and more. Moving beyond just the security operation centers (SOCs), it will also help readers understand business impact by quantifying the risk associated with vulnerabilities and malware.

The trends and data in this report not only represent the evolution of the threat landscape, but show how critical it is that SOCs are provided with the most accurate, relevant intelligence possible. When these teams are served up the latest intelligence about the most likely secondary and tertiary threats to their unique environment that could emerge, they gain precious minutes or hours needed to stay ahead of malicious actors.

## Methodology

This report was written with both qualitative and quantitative approaches and relied primarily on data from Dataminr and ThreatConnect. In the event a data point was sourced from third parties, it was noted as such. The goal of the report is to provide cybersecurity teams with actionable insight into the cyber threat landscape as it has evolved over the past year so they can understand trends that would be helpful for the ongoing protection for their organization or agency.

## Executive Summary

Dataminr’s 2026 Cyber Threat Landscape Report aggregates global cyber intelligence to provide security leaders with a clear, quantified view of evolving risks—from the exponential rise in identity-centric attacks and high-impact “mega-losses” to the persistent threats posed by sophisticated, well-funded criminal and state-aligned groups.

Our analysis confirms that the window of time between targeting, initial access, and payload execution or data exfiltration has greatly diminished. This makes proactive, context-rich, and even predictive threat intelligence the non-negotiable requirement for organizational resilience in 2026.

### Dominant Threat Actors and Tactics

- **Qilin**: Identified as the most active ransomware group of 2025, Qilin consolidated the market by offering high payouts and a stable platform for affiliates.
- **Cl0p**: This group utilized a “restraint and precision” strategy, focusing on encryption-less extortion to siphon terabytes of data while maintaining a low profile.
- **Scattered Lapsus$ Hunters**: Demonstrated the vulnerability of the “human element” by using AI-enhanced social engineering to bypass technical security measures.
- **NoName05716**: Remained the most active pro-Russian hacktivist collective, primarily utilizing crowd-sourced DDoS attacks against critical infrastructure.

### Key statistics from 2025

- **5,000+**: threat actors tracked
- **225%**: increase in monthly threat actor alerts from 2024-2025
- **18,000+**: alerts on ransomware activity
- **2,000,000+**: domain impersonations
- **425,000+**: instances of brand fraud
- **110,000+**: alerts on doxxing or leaked credential databases

### Critical Vulnerabilities

The report emphasizes that technical severity based on the common vulnerability scoring system (CVSS) does not always equal business risk. While there were certainly high-scoring CVEs that also carried high remediation costs, such as CVE 2025-55182, it is always important to layer in factors such as likelihood of exploitation, potential business impact, and frequency of targeting. This allows organizations to move beyond the very binary approach of whether the CVSS score deems a vulnerability important enough for their teams to patch them.

## The Cyber Risk Landscape

It is impossible for humans alone to keep tabs on everything happening that presents cyber risk. Regardless of size, every organization and government agency has a complex infrastructure of assets to manage. For larger ecosystems, that number could reach millions of endpoints, software versions, and individuals across the globe that could be exposed to risk. All of these contribute to a complex web of assets and telemetry across an organization’s infrastructure that need to be constantly evaluated, monitored, and protected.

### Our View of the 2025 Cyber Risk Landscape

- **6.3M+**: External threat alerts (Ex: Malware, hacktivism, ransomware, APTs)
- **4.8M+**: Vulnerability alerts (Ex: Exploits, emerging vulnerabilities, disclosures.)
- **3.1M+**: Digital risk alerts (Ex: Domain impersonation, phishing, doxxing, data exposure)

The numbers above represent why so many security and infrastructure teams feel overwhelmed. It’s crucial to ensure only the most relevant alerts are being presented to the team. In situations like this, relevance can be tied to whether the risk is present in that organization’s environment in the first place, what the organization’s risk tolerance is, or what the potential impact is to the organization if the risk is left unresolved.

## Vulnerabilities

Software vulnerabilities can be highly effective points of initial compromise and access for a threat actor—especially when they’re discovered in widely-used solutions. Threat actors are constantly poking and prodding at software to find mistakes in code and bypass security measures. These risks could also present themselves at other points of an organization’s supply chain if a deeply integrated technology is compromised, which unknowingly creates an access point to sensitive information.

Once the actor finds a way to exploit a weakness, their next step will depend on their end objectives. Many will try to sell the exploit code or tailored access by advertising it for sale on Dark Web forums or in Telegram channels. Some will take the riskier, but potentially more lucrative step, which is to use the exploit to access an organization’s valuable data and either exfiltrate it, sell it or render it inaccessible as part of a ransomware attack.

Threat actors have long made practice of analyzing newly published vulnerabilities and newly released patches to understand where weak points may exist and reverse-engineer vulnerabilities to target systems that remain unpatched. This window of opportunity between when a vulnerability is disclosed, when the patch is released, and the vulnerable system is actually patched by system owners is frequently when the attacker has their best chance of success.

However, in 2025, the security landscape was defined by a “patch bypass epidemic,” where critical fixes for major platforms were often immediately re-exploited due to incomplete root-cause remediation by the software vendor. The most prominent example was observed with a Microsoft SharePoint vulnerability, where attackers bypassed the initial July patches (CVE-2025-49706/49704) within days by using simple path traversal techniques, forcing the issuance of new CVEs (CVE-2025-53770/53771) for the same underlying flaws.

![Figure 2. Vulnerability Reexploitation SharePoint Toolshell with Dataminr alerting enhanced by ReGenAI and Intel Agents.]

This pattern was repeated in Windows Server Update Services (WSUS) and SAP NetWeaver, where initial patches for critical vulnerabilities failed to account for all deserialization vectors, necessitating emergency out-of-band updates and secondary CVE assignments. Similarly, Grafana attempted to fix a vulnerability using client-side restrictions that were easily circumvented, rather than validating server-side input. Collectively, these four incidents highlighted a systemic failure in “variant analysis,” leaving organizations vulnerable even after applying vendor-supplied updates.

In addition to this challenge around re-exploitation, teams are monitoring and managing tens of thousands of new vulnerabilities every year. Many are rated “High” or “Critical” based on their Common Vulnerability Scoring System (CVSS) scores, which only take into account the technical impacts. While CVSS remains useful for understanding exploit mechanics, it provides limited insight into which vulnerabilities actually matter to a specific organization. Without additional context, security teams are left with an undifferentiated backlog of critical findings that obscures what truly warrants action, investment, and executive attention. A consistent observation is that severity does not always equal risk.

![Figure 3. CVE risk impact matrix]

Adopting this approach enables security leaders to distinguish between vulnerabilities that are noisy but economically bounded and those that present systemic, enterprise-level exposure. More importantly, it represents the path forward for modern threat intelligence and vulnerability analysis—one that connects technical findings to business outcomes, aligns remediation with actual risk, and supports defensible, data-driven decision-making at both the operational and executive levels.

## Digital Risk

Aside from direct threats or vulnerabilities, organizations also need to be aware of external factors that could pose serious challenges in regards to third-party risks, brand reputation, and potential compliance violations. This is referred to as digital risk, which encompasses challenges such as domain impersonation, brand abuse in phishing campaigns, brand fraud, hacking services for sale, doxxing and leaked credentials, intellectual property and other data leaks.

![Figure 4. Data from the Dataminr Knowledge Graph (January 1, 2025 - December 31, 2025)]

- **2,000,000+**: Domain impersonation alerts
- **443,000+**: Phishing alerts
- **424,000+**: Company fraud alerts
- **185,000+**: Hacking services alerts
- **109,000+**: Doxxing or leaked credentials alerts
- **86,000+**: Data exposure or breach alerts

Events tied to these risk vectors typically occur outside of an organization’s immediate purview. For example, if a third-party (or third-party software) is breached and an organization’s customer or employee credentials are compromised, it might take days or weeks for their security team to become aware of the incident. In that time, the threat actor has a window of opportunity to quietly advance their attack on customers or enter their infrastructure and execute a further damaging attack.

If customer data is part of a breach, the organization could suddenly be held accountable for the financial implications—especially if there are any compliance violations involved. In some cases, threat actors will use a tactic called double extortion and threaten to notify the SEC or equivalent government body about a ransomware attack if the target organization doesn’t pay up. For public sector organizations, that same scenario can lead to national security risks and help adversarial nation-states sow distrust in the government by claiming to have accessed the most personal data about citizens.

![Figure 5. Threat actor group Scattered LAPSUS$ Hunters (SLH) exhibits its use of double extortion in its Telegram channel.]

Domain impersonation, brand fraud, and phishing kits targeting an organization all threaten the integrity of an organization. Depending on the actor’s intentions, these can be used to target both customers and employees. While most sizable organizations operate under the assumption that there is likely an actor out there executing one of these attacks and therefore have protections in place against the eventual compromise that could take place, there’s a fine line between commodity phishing kits and an advanced, multi-pronged attack that fraudulently represents an organization.

Doxxing, data breaches, and leaked credentials represent a more imminent threat to an organization’s systems, data, and employees. Data breaches are often the sources of follow-on activity like doxxing or leaked credentials, which makes it critical for an organization to know when a threat actor might be advertising their data for sale on a Dark Web forum or Telegram channel. With that knowledge, that organization can at least try to get ahead of eventual compromise by instituting proactive measures like company-wide password resets and additional monitoring for anomalous user behavior.

It’s also important for an organization to know when a third-party vendor with access to sensitive data or systems is involved in a cyber attack or data breach. This can also extend to cloud infrastructure platforms that, if compromised, could unintentionally end up exposing customer instances. Being notified as early as possible about a possible breach elsewhere in the digital supply chain can be the difference between having a window of opportunity to remove any connection with the compromised platform and dealing with a significant data breach.

Third-party risk is just one of many reasons that resilience, or the ability to withstand a direct or third-party breach, is so important in the cloud. Many organizations align to a widely-known approach that takes into account three key principles - confidentiality, or preventing unauthorized data access; integrity, which ensures data is accurate and hasn’t been tampered with; and availability, which guarantees that data is accessible even during disruptions.

![Figure 6. Timeline of key events pertaining to the PowerSchool breach as detected by Dataminr]

## Malware

SOC teams must be aware of chatter across the Dark Web, Telegram channels, and other places where adversaries discuss their next move or what tools they’re finding most effective. They also need to know when independent researchers and other security teams come across novel malware or see a resurgence of existing malicious tools. This section provides an overview of the malware families with the most aggregate alerts from all sources in the Dataminr platform.

![Figure 7. An alert showing that activity around Lumma Stealer is spiking.]

For instance, knowing if a specific malware family is being deployed against a peer organization in a certain industry can be highly beneficial to informing proactive defensive posture. Threat actor groups frequently stick to successful methods, so if they manage to compromise several organizations within one industry using a particular type of malware, they are likely to repeat that attack chain.

| MALWARE FAMILY | DESCRIPTION | BEHAVIOR |
| :--- | :--- | :--- |
| Mirai | Exploits weak default credentials and vulnerabilities in devices like routers and cameras to form massive botnets. | Can generate traffic bursts over 100 Gbps, targeting various sectors. Its proliferation and adaptation pose a growing risk to critical infrastructure. |
| Lumma Stealer | Sophisticated, MaaS infostealer distributed through Russian forums. | Uses anti-debugging and custom XOR obfuscation for evasion. Stolen data is exfiltrated via HTTP POST to a C2 server, delivered as EXE, DLL, or PowerShell. |
| Formbook | Also tracked as xloader (MaaS) infostealer, stealing browser credentials, keystrokes, clipboard content, screenshots, and web form data, and can download other files. | Employs sophisticated evasion techniques, including DLL search order hijacking, generating mutex names using SHA-1 hashes, and resolving API addresses with CRC32/RC4 encryption. |
| Rhadamanthys | MaaS infostealer. Linked to Hidden Bee, its authors treat it as a long-term business, selling it for a monthly fee via Tor and Telegram. | The multi-stage infection uses loaders and employs new anti-analysis checks and a proprietary “XS” file format to evade PE parsers. Recent versions added browser fingerprinting. C2 configuration allows multiple servers and is downloaded as PNGs. Communication uses WebSocket with RC4-encrypted strings. |
| VoltRuptor | ICS & SCADA-specific malware strain reportedly developed by Russia-aligned hacking group Infrastructure Destruction Squad (IDS). | Designed for cross-platform operations. It features multi-protocol support, as well as persistence and anti-forensics capabilities. |
| Agent Tesla | Keylogger and RAT that captures clipboard data, screenshots, and audio/video. | Accepts nearly 40 commands for file management, command execution, process manipulation, and loading additional malware. The latest activity also utilizes .NET executables to decode and inject variants into processes. |
| NjRAT | RAT used for unauthorized system control. Facilitates malicious activities like keylogging, credential theft, webcam access, ransomware deployment, and system manipulation. | Collects data, disables security tools, manages files, and modifies Registry keys, typically spreading via phishing and drive-by downloads to grant command-line access. |

![Figure 8. Information that Dataminr provides about malware families as exemplified by NjRAT.]

| MALWARE FAMILY | DESCRIPTION | BEHAVIOR |
| :--- | :--- | :--- |
| Remcos | RAT that grants attackers full control over infected systems for data exfiltration and keystroke logging. | Evades detection using obfuscation, API hash values, Vectored Exception Handling, and process hollowing. |
| ASyncRAT | Stealthy, polymorphic RAT targeting Windows. Capabilities include screen control, keystroke logging, file exfiltration, webcam capture, and remote desktop. | Suspends legitimate processes (like a renamed “dllhost.exe”), injecting code, then resumes them. |
| Brickstorm | Sophisticated, cross-platform backdoor malware primarily used for long-term cyber espionage. Attributed to People’s Republic of China (PRC) state-sponsored threat actors. | Achieves persistence by modifying the registry or creating new services, and evades detection using encrypted communications and anti-analysis techniques. Exfiltrates system data to a C2 server and can execute various commands, including downloading plugins, terminating processes, and updating itself. Uses advanced techniques to hide its command-and-control (C2) traffic, including DNS-over-HTTPS (DoH), nested TLS encryption, and WebSockets. This makes its malicious traffic look like legitimate web browsing. Includes a “self-watching” function that automatically restarts or reinstalls itself if it is killed. It also modifies system initialization scripts to ensure it survives reboots. |

## Dual use tools

In addition to outright malicious software, it’s also important to be aware of tools that are legitimate, but can be leveraged by threat actors for malicious activity. This falls under the umbrella of a tactic known as “living off the land”, which implies that the threat actor is able to infiltrate the organization and use existing tools, binaries, and scripts to execute malicious activities. This is not a novel tactic, and as such there is an open-source project known as Living Off The Land Binaries, Scripts, and Libraries (LOLBAS) meant to catalogue all binaries, scripts, and libraries that can be used in this tactic.

While these tools shouldn’t be used without internal oversight, they’re so widely used for legitimate reasons that they’re rarely on block lists.

| TOOL | PRIMARY LEGITIMATE USE | WHY THREAT ACTORS USE IT |
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

![Figure 10. Dataminr alerts on threats pertaining to popular dual-use tools.]

## 2025 Financial Impact Trends

From a financial loss perspective, 2025 marked a clear shift from “frequent but contained” cyber losses toward fewer events with materially larger financial and mission impact. While ransomware volumes stabilized, single-incident losses increased, driven by multi-vector attacks that combined credential theft, data exfiltration, operational disruption, and regulatory exposure into one event.

The most consequential losses increasingly stemmed from identity compromise, third-party concentration risk, and exploitation of trusted business processes, rather than purely technical exploits—pushing cyber risk firmly into the category of balance-sheet and earnings volatility, not just security operations cost.

## The Rise of the “Mega-Loss”

The Normalized Severity Distribution confirms that 2025 is the year of the “tail event.”

- **Loss density shift**: The 2025 KDE (Kernel Density Estimation) shows a distinct migration of loss probability toward the right. Large-scale clusters have appeared at the $100M and $1B+ levels, which were virtually absent in 2024.
- **Ransomware tail risk**: For ransomware, the 2025 probability curve is significantly flatter and longer, indicating that multi-billion dollar losses are no longer black swan events but are increasing in likelihood.

![Figure 11. The Normalized Severity Distribution.]

## Changing Tactics for the Attacker and Company

Attack types have become more specialized and impactful per incident. The following statistics are from ThreatConnect Risk Quantifier, which is built on more than 20 years of historical loss data gathered from filings, industry data, and our own research.

- **Identity is the new perimeter**: Nearly one in three (30%) cyber intrusions now involve the use of valid credentials—attackers are “logging in” rather than “breaking in.” This is fueled by an 84% increase in infostealer malware delivered through phishing.
- **Phishing resilience**: Phishing remains the dominant intrusion vector in 60% of cases. By early 2025, AI-supported phishing campaigns represented over 80% of observed social engineering activity worldwide.
- **Payment refusal trends**: Despite higher severity, organizations are pushing back; 63% of organizations opted not to pay ransoms in 2025, up from 59% in the prior year.
- **Supply Chain Gravity**: One in four modern breaches now exploits a third-party vulnerability (CVE), escalating the risk magnitude by 20% compared to direct internal attacks. This “Vendor Pivot” is characterized by extreme velocity; 96% of these vulnerabilities are weaponized within the same calendar year of disclosure, frequently bypassing internal detection and resulting in twice the data impact per incident.

## Threat Actor Activity

Over the course of 2025, threat actor activity consistently increased and represents a significant jump from 2024. In fact, there was a sizable 225% increase in average monthly alerts (1,490/month to 4,840/month), with the busiest month in 2024 not even reaching the quietest month in 2025. These statistics are derived from the Dataminr Knowledge Graph, which tracks all events and leverages AI to tag them with the appropriate threat actors.

![Figure 12. Threat Actor Activity: 2024 vs 2025.]

For any team tasked with protecting against cyber threats, they face the challenge that the dwell time between initial breach and catastrophic data theft has effectively been reduced to zero, making the earliest possible signaling of a campaign a critical requirement for survival. Because these modern adversaries often use dual-use administrative tools to “live off the land” once inside, traditional signature-based detection is often ineffective.

![Figure 13. Timeline of key events pertaining to CVE-2025-6446 as detected by Dataminr]

## High Impact Groups

Advanced collectives moved away from traditional software exploits in favor of “identity-centric” warfare, where the human element became the primary entry point through AI-enhanced social engineering. The group that most prominently executed the identity-centric playbook was Scattered Lapsus$ Hunters, or SLH, an alliance of three sub-groups of the cybercrime collective known as The Com. Not only has SLH arguably perfected the use of AI-enhanced social engineering by leveraging voice phishing (vishing) and other tactics to compromise entire organizations, but they also managed to compromise SaaS solutions so deeply integrated into other systems that the actors could compromise dozens of organizations at once.

Simultaneously, the focus shifted from simple system disruption to massive, “encryption-less” data exfiltration. By weaponizing zero-day vulnerabilities in common enterprise file transfer and resource planning platforms, these actors were able to compromise handfuls of organizations in a short window, holding corporate reputations and proprietary intellectual property hostage rather than merely locking down operational files.

![Figure 14. High Criticality Threat Actor Activity: 2025 vs 2025.]

### Group Summaries

- **Cl0p | Russia**: Cl0p’s 2025 activity highlights a “restraint and precision” strategy. By avoiding the noise of system encryption, they maintain a lower profile while dwell-time increases, allowing them to siphon terabytes of data before an intrusion is even detected by the victim.
- **Scattered Lapsus$ Hunters | United States & United Kingdom**: The 2025 SLH proved that technical “un-hackability” is irrelevant if the human at the help desk can be manipulated. Their success forced a global shift toward phishing-resistant MFA (FIDO2) as the only viable defense against their social engineering prowess.
- **Infrastructure Destruction Squad (IDS) / Dark Engine | Russia**: They emerged in 2025 as a highly aggressive and technically capable “hacktivist”. Despite an independent, ideological persona, their sophisticated targeting in 2025 suggests close alignment with state-level strategic interests.
- **Qilin | Russia**: By providing the most stable platform and high payouts, they effectively consolidated the ransomware market, turning disparate cybercriminal cells into a unified, high-tempo threat.
- **Everest | Likely Russia**: By acting as both the intruder and the broker, Everest has become a “force multiplier” for the entire cybercrime economy, making them a primary threat to enterprise-level supply chains.
- **JR Intel | Europe**: JR Intel represents the “Data Brokerage” evolution of cybercrime. In 2025, their activity proved that the value of stolen intellectual property (e.g. source code and schematics) often exceeds the value of a ransomware payout, as this data can be sold repeatedly to state actors or industrial competitors.
- **Inc Ransom | Likely Russia**: Inc Ransom’s success in 2025 stems from their “business-like” reliability. Unlike more volatile groups, they have gained a reputation for providing working decryptors upon payment and honoring “no-leak” agreements, which ironically makes victims more likely to pay.

## Threat Actor Spotlight: jrintel

jrintel (also known as JR Intel, hubz, or hubzXjrintel) is a high-profile, financially motivated mercenary information broker that emerged in August 2025. Unlike state-sponsored groups, jrintel operates as an opportunistic independent broker, specializing in trafficking sensitive military, intelligence, and government data from a wide range of geopolitical adversaries, including the U.S., China, Russia, Israel, and NATO.

![Figure 15. Dataminr alert of jrintel claim from DarkForums.]

## Operational Evolution

The actor’s capabilities have evolved rapidly through three distinct phases:

- **PHASE 1: Military Technical Espionage (Aug–Oct 2025)**: Focused on high-tech military hardware to establish credibility. Key leaks included schematics for the U.S. Navy Arleigh Burke-class destroyer, SpaceX Raptor engines, and the Sukhoi S-70 Okhotnik-B drone.
- **PHASE 2: Broad Intelligence & PII Theft (Nov–Dec 2025)**: Expanded into bulk personal identifiable information (PII) and civilian databases. Notable activity included leaking data on CIA, MI5, and Mossad agents, and a database purportedly covering all UAE citizens. Recruited social engineering operators to target cryptocurrency investors, with observed TTPs and chatter suggesting a connection between jrintel and the predominantly English-language cybercrime ecosystem known as “The Com.”
- **PHASE 3: Hybrid Operations & Services (Dec 2025–Jan 2026)**: Transitioned into “Espionage-as-a-Service,” merging digital theft with physical-world activities. This includes recruiting for physical reconnaissance in Mali and seeking U.S. government insiders with access to confidential military blueprints.

![Figure 16. Image of post of DarkForums from Dataminr alert of jrintel publishing purported passports of China Foreign Affairs Ministry officials.]

## Most active actors by alert volume

This section dives into the most active actors by alert volume over the course of the year. Unsurprisingly, these actors are more focused on less sophisticated and highly repeatable attacks like DDoS. For an infrastructure security team, DDoS attacks can be massive challenges—especially if they’re being used to distract the team away from a larger attack, take down core operations, or have knock-on effects on customers.

It’s interesting to observe that, while most actors rely on botnets to gain the critical mass needed to execute a DDoS attack, NoName05716 crowd-sources its critical mass and gamifies the process with its followers.

![Figure 17. A screenshot from Telegram where NoName05716 is trying to recruit local actors.]

### Group Summaries

- **NoName05716**: The most active pro-Russian hacktivist collective, despite significant international law enforcement pressure.
- **Hezi Rash (meaning “Black Force”)**: A relatively new but hyper-aggressive Kurdish nationalist group.
- **Keymous+**: One of the most sophisticated “hybrid” actors, seamlessly switching between state-aligned espionage and high-value financial theft.
- **RomCom**: A group focused on zero-day exploitation, malware upload via portal abuse, spearphishing, and backdoors.

## Conclusion

The findings in this report demonstrate two critical, undeniable takeaways for any enterprise or government security team: the power of interconnected intelligence and the need for purpose-built AI to handle the chaos of today’s cyber threat landscape.

A siloed view of cyber risk and threats is no longer viable, and organizations must move beyond generic scoring and analysis. Now, to get the full picture, it’s important to look at how a few key factors intersect and overlap.

- **Holistic Visibility**: Merging vulnerability data with real-time threat actor activity and external digital risks, such as domain impersonation and credential leaks, provides a complete view of an organization’s attack surface.
- **Contextual prioritization**: The report proves that technical severity (CVSS) does not always equal business risk. True intelligence requires layering in the likelihood of exploitation and frequency of targeting given an organization’s unique infrastructure.
- **Operational resilience**: By connecting technical findings to business outcomes, organizations can transition from a reactive “undifferentiated backlog” to data-driven decision-making that protects the balance sheet from “mega-losses.”

When it comes to AI, the data in this report shows that the threat landscape has reached a level of complexity and speed where human-only teams can no longer manage the chaos on their own.

- **Collapsing time to exfiltration**: With the window of time between initial breach and data theft getting shorter every year, security teams require the earliest possible signaling of a threat actor activity to survive.
- **Combatting AI with AI**: Advanced adversaries are already using AI to lower the barrier to entry for unskilled actors and enhance the social engineering capabilities of experts. Only platforms built with proprietary LLMs and Agentic AI can ingest the 43+ terabytes of data daily required to identify these signals.
- **Bridging the talent gap**: As agencies and operators remain critically understaffed, specialized AI platforms act as a force multiplier—automating the correlation of signals from millions of sources to provide the foresight needed to take action when every second counts.

## Appendix 1

| CVE | CVSS | At-risk industries | Overall Risk |
| :--- | :--- | :--- | :--- |
| CVE-2025-55182 | 10.0 | Many | Critical |
| CVE-2024-1709 | 9.8 | Government MSPs | Very High |
| CVE-2025-53770 | 9.8 | Many | Very High |
| CVE-2025-32433 | 10 | Telecommunications | High |
| CVE-2025-5777 | 9.4 | Financial Services | High |
| CVE-2024-55591 | 9.6 | Government | High |
| CVE-2025-31324 | 9.8 | Manufacturing | Moderate |

## About Dataminr & ThreatConnect

Dataminr, now together with ThreatConnect, remains dedicated to its mission of delivering the most relevant and accurate AI-powered real-time event, threat & risk intelligence to its customers. Combining best-in-class intelligence with more than a decade of experience building a platform with AI at its core, Dataminr ensures its customers receive the most relevant and accurate intelligence with unmatched speed, scale, and accuracy—hours or even days ahead of conventional sources, integrating external and proprietary internal data.

---

0M)

CVE-2024-4577
CVSS: 9.8 | At-risk industries: Many | Overall Risk: Moderate

ABOUT

IMPACT

DESCRIPTION

MITIGATION STEPS

LIKELIHOOD OF IMPACT

FINANCIAL RISK
($-$$$$$)

Patch the CVE or use WAF
rules targeting known
exploit patterns.

Effectively a bypass of a
long-standing PHP CGI fix
originally implemented to
stop CVE-2012-1823.

Attackers gain the same
privileges as the web
server processes.

Moderate

$$

Mostly targeted hosted
sites.

Primarily effects windows
servers with php running
in CGI mode. Some
mitigations (such as WAF
rules should already be in
place).

CVE-2023-6553
CVSS: 9.8 | At-risk industries: Many | Overall Risk: Low

ABOUT

IMPACT

DESCRIPTION

MITIGATION STEPS

LIKELIHOOD OF IMPACT

FINANCIAL RISK
($-$$$$$)

Affects Backup Migration
plugin for WordPress. It
allows unauthenticated
attackers to execute
arbitrary PHP code on
affected servers via a flaw
in the plugin’s file handling
logic.

Attackers can gain remote
code execution (RCE).

Patch the CVE, disable the
plugin, or restrict public
access (if possible).

Very High

$

No authentication
required to create the
exploitation.

Most Wordpress usage is
on marketing sites that
don’t have connectivity to
production systems.
The impact would be
minor

42

@ 2026 Dataminr. All rights reserved. | DATAMINR.COMDataminr 2026 Cyber Threat Landscape Report  |CVE-2024-36401
CVSS: 9.8 | At-risk industries: Government | Overall Risk: Low

ABOUT

IMPACT

DESCRIPTION

MITIGATION STEPS

LIKELIHOOD OF IMPACT

FINANCIAL RISK
($-$$$$$)

A remote code execution
vulnerability in GeoServer,
an open-source Java
server used to publish,
share, and edit geospatial
data using Open
Geospatial Consortium
(OGC) standards—such as
WFS, WMS and WPS.

Exploitation could
fully compromise the
underlying systems.

Remove the vulnerable
library module and/or
patch.

High

$

Typically behind a set of
defenses (Firewall, DMZ),
so attackers have to get
through existing defenses
to execute an attack.

Agencies using Geoserver
would expect to spend
$500K to $5M per
affected environment for
remediation. This does
not take into account the
mission impact of losing
access to geo data for key
missions.

About ThreatConnect

ThreatConnect provides solutions to enable
cyber defenders to continuously manage threat
exposure and improve cyber resilience. Our
threat and risk-informed defense products give
defenders the advantage over adversaries with
rich context, risk-based prioritization, and the
ability to quickly and precisely act on emerging
threats. Our products span threat, risk, and
security operations, and come together in a
single intelligence hub. More than 250 global
enterprises rely on ThreatConnect every day to
contextualize and prioritize emerging threats and
automate defenses.

About Dataminr

Dataminr is the global leader in AI-powered
real-time event, threat & risk intelligence.
The company delivers the earliest actionable
intelligence on breaking events, emerging
threats, and unexpected risks across the physical,
digital, and cyber domains. Dataminr first
pioneered Multi-Modal Fusion AI, synthesizing
text in 150 languages, image, video, audio, and
sensor signals across 1M public data sources
to deliver the fastest, most accurate real-time
detection. Dataminr’s AI innovations, including
ReGenAI, Intel Agents, and PreGenAI, build on
this foundation by delivering Live Briefs, Agentic
AI-powered context, and Predictive Intelligence.
More than 100 U.S. government agencies,
20 international governments, two-thirds of
the Fortune 50, and half of the Fortune 100
trust Dataminr to protect people, assets, and
operations and respond with unmatched speed
and confidence.

43

@ 2026 Dataminr. All rights reserved. | DATAMINR.COMDataminr 2026 Cyber Threat Landscape Report  |