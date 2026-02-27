# 2025 Global Threat Landscape Report

**Organization:** Fortinet  
**Report Title:** Global Threat Landscape Report  
**Year:** 2025  
**Author:** A Report by FortiGuard Labs

## Table of Contents
- [Introduction: Acceleration of the Adversary Advantage](#introduction-acceleration-of-the-adversary-advantage)
- [One: Cyber Reconnaissance Surge: The Rising Threat of Automated Scanning](#one-cyber-reconnaissance-surge-the-rising-threat-of-automated-scanning)
- [Two: Shedding Light on the Darknet: How Adversaries Prepare to Strike](#two-shedding-light-on-the-darknet-how-adversaries-prepare-to-strike)
- [Three: From Exposure to Initial Access and Exploitation: How (and Where) Attackers Get the Keys to the Kingdom](#three-from-exposure-to-initial-access-and-exploitation-how-and-where-attackers-get-the-keys-to-the-kingdom)
- [Four: Beyond Initial Access: Post-Exploitation, Lateral Movements, and C2](#four-beyond-initial-access-post-exploitation-lateral-movements-and-c2)
- [Five: The Cloud Battlefield: Navigating the New Cybersecurity Landscape](#five-the-cloud-battlefield-navigating-the-new-cybersecurity-landscape)
- [Six: Adversary Landscape Analysis](#six-adversary-landscape-analysis)
- [Conclusion: Helping CISOs Defeat Adversaries](#conclusion-helping-cisos-defeat-adversaries)

---

![Image description: 2025 Global Threat Landscape Report cover page by FortiGuard Labs]

![Image description: MITRE ATT&CK framework diagram showing the progression from Reconnaissance and Resource Development to Initial Access, Privilege Escalation, Lateral Movement, Command & Control, Exfiltration, and Impact.]

## Introduction: Acceleration of the Adversary Advantage

This 2025 Threat Landscape Report reveals a dramatic escalation in both the scale and sophistication of cyberattacks. Data shows adversaries are moving faster than ever, automating reconnaissance, compressing the time between vulnerability disclosure and exploitation, and scaling their operations through the industrialization of cybercrime. Across all attack phases, FortiGuard Labs observed that threat actors are leveraging automation, commoditized tools, and AI to erode the traditional advantages held by defenders systematically.

The challenge is clear: Your adversary’s advantage is accelerating. From pre-attack reconnaissance to post-compromise persistence, attackers now operate with unprecedented speed, precision, and reach, challenging organizations to shift from reactive defense to proactive exposure management.

### Key findings

*   **Reconnaissance is surging.** Cybercriminals are deploying automated scanning at a global scale. Active scanning in cyberspace reached unprecedented levels in 2024, rising by **16.7%** worldwide. FortiGuard Labs observed billions of scan attempts each month, equating to **36,000 scans per second**, revealing an intensified focus on mapping exposed services, such as SIP and RDP, and OT/IoT protocols like Modbus TCP. Tools like SIPVicious and commercial scanning tools are weaponized to identify soft targets before patches can be applied, signaling a significant “left-of-boom” shift in adversary strategy.
*   **AI is supercharging the cybercrime supply chain.** Threat actors leverage AI for phishing, impersonation, extortion, and evasion tactics. Tools like FraudGPT, BlackmailerV3, and ElevenLabs are automating the generation of malware, deepfake videos, phishing websites, and synthetic voices, fueling more scalable, believable, and effective campaigns.
*   **CaaS is fueling initial access at scale.** The underground economy for stolen credentials and direct corporate access has exploded. FortiGuard Labs observed a **42% increase** in compromised credentials for sale and a rise in Initial Access Broker (IAB) activity offering VPNs, RDPs, and admin panels. Infostealers like Redline and Vidar drove a **500% increase** in credential logs on darknet forums.
*   **Adversaries are fragmented in form and unified in function.** While 13 new ransomware groups entered the Ransomware-as-a-Service (RaaS) market, demonstrating fragmentation, the top four groups still accounted for **37%** of observed attacks, indicating concentrated influence. Meanwhile, hacktivists have begun adopting ransomware tactics, and nation-state actors remain active in targeting manufacturing, government, education, and tech sectors. Telegram remains a dominant coordination hub for sharing exploits and infrastructure, offering a layer of operational unity across otherwise disconnected threat groups.
*   **Exploitation volumes are soaring as speed remains steady.** While the average time to exploit newly disclosed vulnerabilities held relatively steady in 2024, closely tracking the 5.4-day average observed in 2023, the scale of exploitation attempts surged. FortiGuard Labs recorded over **97 billion exploitation attempts** during the year, reflecting increased automation and broader targeting across industries. Attackers prioritized exposed IoT devices, routers, firewalls, and cameras, frequently used for botnet command and control (C2), lateral movement, and persistent access. CVE-2024-21887, a command injection vulnerability in Ivanti products, was exploited just six days after disclosure, underscoring how quickly adversaries can still act when opportunity aligns with impact.
*   **Post-exploitation tactics are getting stealthier.** Despite the number of CVEs growing 39% from 2023 to 2024, zero-day attacks only account for a small percentage of observed threats. Cybercriminals increasingly “live off the land,” using trusted tools and protocols to escalate privileges and persist undetected. FortiGuard Labs has identified advanced post-compromise behaviors, including Active Directory (AD) manipulation (such as DCShadow and DCSync), RDP-based lateral movement, and encrypted C2 via DNS and SSL.
*   **Cloud attacks are evolving, but misconfigurations still reign.** Cloud environments remain a top target, with adversaries exploiting persistent weaknesses, such as open storage buckets, over-permissioned identities, and misconfigured services. Lacework FortiCNAPP telemetry shows a steady rise in cloud compromises, often involving identity abuse, insecure APIs, and privilege escalation. These vectors are frequently combined in multi-stage attacks that leverage automation and legitimate services for stealth and persistence. Reconnaissance remains the most prevalent tactic, with attackers probing APIs, enumerating permissions, and scanning for exposed assets. In **70%** of observed incidents, attackers gained access through logins from unfamiliar geographies, highlighting the critical role of identity monitoring in cloud defense.

### A call to action: shift left, act fast, reduce exposure

The evidence is clear: Attackers invest heavily in automation, reconnaissance, and scalable operations. Their playbooks emphasize speed, stealth, and scalability, while far too many organizations remain overburdened with reactive patch cycles and static security strategies.

Defenders must shift from traditional threat detection toward Continuous Threat Exposure Management (CTEM) to counter this asymmetry. This proactive approach emphasizes the following:

*   Continuous attack surface monitoring
*   Real-world emulation of adversary behavior
*   Risk-based prioritization of remediation
*   Automation of detection and defense responses

The security landscape has radically changed. Staying ahead of attackers now means countering their next move before they make it, which means that traditional security solutions are no longer enough.

---

## One: Cyber Reconnaissance Surge: The Rising Threat of Automated Scanning

Active scanning in cyberspace reached unprecedented levels in 2024, rising by **16.7%** worldwide, highlighting a sophisticated and massive collection of information on exposed digital infrastructure. Intrusion prevention system (IPS) engines in FortiGate Next-Generation Firewalls (NGFWs) detected an intensification of these scans across all geographies, with attackers leveraging advanced left-of-boom techniques to map attack surfaces before launching targeted offensives.

![Image description: Behavioral Trend Analysis chart showing 1.16 trillion current detections in 2024, compared to 993 billion in the previous period, representing a 16.71% year-over-year growth.]

This unprecedented volume of automated scans suggests a rise in large-scale reconnaissance campaigns. These scans seek obvious vulnerabilities and explore critical infrastructures to determine which assets can be exploited with minimal effort. As the weaponization phase of attacks becomes smaller, threat actors can now maintain a near-real-time understanding of attack surfaces across many targets. Then, when a vulnerability becomes available, attackers can strike quickly, impacting organizations that have not proactively applied patches.

### Millions of active scans: what threat actors are looking for

Millions of scanning attempts are detected worldwide every hour, revealing the persistent effort by cybercriminals to map exposed systems before launching their attacks. This number adds up to billions monthly, demonstrating the sheer scale of automated reconnaissance operations. To effectively protect an organization, defenders must understand what attackers are searching for and how their scans translate into real-world risks.

Attackers are targeting widely used protocols in key sectors, such as telecommunications, industry, OT, industrial control systems (ICS), and financial services, and regularly rely on the following:

*   **SIP (VoIP):** SIP represented over **49%** of detected scans. Widely used in telecommunications, SIP vulnerabilities can allow interception attacks and call fraud. For example, APT28 has used legitimate credentials to gain initial access, maintain access, and exfiltrate data from a victim network. The group has also leveraged manufacturers’ default passwords to gain initial access to corporate networks via IoT devices, such as VoIP phones, printers, and video decoders.
*   **Modbus TCP:** Modbus TCP accounted for about **1.6%** of scans, highlighting concerns about industrial infrastructure and supervisory control and data acquisition (SCADA) systems. The Department of Energy (DOE), the Cybersecurity and Infrastructure Security Agency (CISA), the National Security Agency (NSA), and the Federal Bureau of Investigation (FBI) released a joint Cybersecurity Advisory (CSA) to warn that certain advanced persistent threat (APT) actors have exhibited the capability to gain full system access to multiple ICS/SCADA devices.

### Which scanning tools are cybercriminals using to find system weaknesses?

Threat actors are leveraging sophisticated tools to automate attack surface mapping, hereby optimizing their exploitation campaigns. These tools include:

*   **SIPVicious:** SIPVicious is responsible for nearly **50%** of detected scanning events. The SIPVicious suite is a set of tools for auditing SIP-based VoIP systems. Malicious actors have adopted this suite to exploit vulnerable SIP servers. This suite contains five tools: swamp, svwar, svcrack, report, and crash.
*   **Qualys:** This vulnerability scanner appears in about **2.5%** of scans and is used by legitimate security teams and attackers seeking weaknesses in critical infrastructure.
*   **Nmap:** Detected in less than **1%** of events, Nmap remains a key tool for identifying open ports and vulnerable services. Also known as Network Mapper, this is an open-source tool used for network exploration and security auditing. It was originally designed to scan large networks rapidly.
*   **Nessus and OpenVAS:** While representing a smaller percentage of scans, these tools are still widely used to explore vulnerabilities in enterprise systems.

---

## Two: Shedding Light on the Darknet: How Adversaries Prepare to Strike

While much of our telemetry shows what actions attackers have previously taken, darknet intelligence helps us understand what threat actors may do next. Adversaries in the depths of the darknet continue developing, acquiring, and trading resources that enable them to execute large-scale attacks with alarming precision. Security breaches do not begin when an organization detects suspicious activity in its network. By the time an adversary successfully compromises a system, the attacker has already spent significant time planning and testing the attack, with all necessary resources already in place.

The darknet has evolved from a mere refuge for cybercriminals into a supply chain for cyberattacks. The FortiGuard Labs team has identified a rapidly growing underground ecosystem where stolen credentials, corporate access, exploits, and AI-powered tools are bought, sold, and developed to facilitate malicious operations.

### Credentials are the currency of cybercrime

One of the darknet’s most active markets is the trade of compromised credentials. In 2024, over **100 billion records** were shared in underground forums, a **42% increase** from 2023.

This means that attackers no longer need to rely solely on their technical skills. Regardless of technical know-how, any adversary can acquire ready-made resources, significantly lowering the barrier to entry for cybercrime, especially for attackers with lower skills, which ultimately increases the volume, velocity, and sophistication of targeted attacks.

This surge is largely driven by combo lists: massive data files containing email addresses, usernames, and passwords obtained from past breaches. More than **50%** of darknet posts are related to leaked databases, which, if acquired, can easily allow cybercriminals to automate credential-stuffing attacks and gain unauthorized access to corporate systems.

Among the most active cybercriminal groups in this market are:

*   **BestCombo (20%):** This high-volume supplier of stolen credentials frequently sells fresh breaches bundled into massive, ready-to-use lists.
*   **BloddyMery (12%):** Known for aggregating and enhancing leaked data, this group makes stolen credentials more valuable for resale and enhances targeted attacks.
*   **ValidMail (12%):** This group specializes in credential validation services, ensuring buyers receive only functional login details, which increases attack success rates.

### The business of corporate infiltration

Stolen credentials are not the only valuable commodity being sold. In 2024, the darknet saw a sharp increase in IABs, which sell direct access to corporate infrastructures. This service allows adversaries to infiltrate networks without searching for and exploiting vulnerabilities. IABs offer far more than just individual credentials, with some of their most sought-after assets being:

*   Corporate VPN credentials (**20%**)
*   RDP access (**19%**)
*   Admin panels (**13%**)
*   Webshells (**12%**)

IAB groups such as **sandocan (26%)**, **F13 (16%)**, and **JefryG (12%)** lead this economy, offering pre-compromised internal network access to current and aspiring cybercriminals.

### Credential Theft-as-a-Service: the industrialized rise of infostealers

Credentials available on the darknet are not just from past data breaches. In 2024, FortiGuard Labs observed a **500% increase** in logs from systems compromised by infostealer malware, with **1.7 billion stolen credential records** shared in underground forums. The top identified infostealers include:

*   **Redline (60%):** The most widely used infostealer, Redline is favored for its affordability, ease of use, and ability to target multiple data sources. Sold on underground forums for as little as $150, it steals credentials from web browsers, email clients, cryptocurrency wallets, and messaging apps like Telegram and Discord.
*   **Vidar (27%):** Known for its advanced capabilities, Vidar specializes in harvesting credentials and session tokens and multi-factor authentication (MFA) bypass data. This allows attackers to maintain persistent access to accounts even after passwords are reset.
*   **Racoon (12%):** Unlike other infostealers, Racoon focuses on mass data exfiltration, collecting financial records, stored passwords, credit card information, and cryptocurrency wallets.

### Exploit brokers: how attackers obtain and develop their capabilities

Underground forums don’t just trade access and credentials—they also serve as a marketplace for sophisticated exploit kits targeting a wealth of vulnerabilities. In 2024, more than **40,000 vulnerabilities** were added to the National Vulnerability Database, representing a **39% increase** over 2023.

In 2024, **331 zero-day vulnerabilities** were identified in darknet forums with a high percentage of available exploits:
*   **182 (55%)** had publicly available proof-of-concept (POC) exploit code.
*   **106 (32%)** featured fully functional exploit code ready for attacks.
*   **98 (30%)** were actively being exploited in ransomware and APT campaigns.

### AI-enabled cybercrime: the role of AI in the automation of cybercrime

The growing cybercrime market is thriving on cheap and accessible wins. And as AI evolves, it’s already lowering the barrier to entry for aspiring cybercriminals. Beyond enhancing accessibility, AI enables malicious actors to create more believable phishing threats.

The FortiGuard Labs team has identified numerous AI-driven tools that are helping adversaries gain new efficiencies, including:

*   **DeepFaceLab and Faceswap:** Used to create realistic AI-generated videos to bypass identity verification on banking and crypto platforms.
*   **FraudGPT and WormGPT:** AI-powered text generators that help cybercriminals craft compelling phishing emails and fraudulent documents without ethical restrictions.
*   **BlackmailerV3:** An AI-driven extortion toolkit that automates customized blackmail emails using scraped personal and corporate data.
*   **AI-generated phishing pages (EvilProxy, Robin Banks):** Platforms that use AI to auto-generate phishing websites mimicking legitimate portals, some offering Adversary-in-the-Middle (AiTM) capabilities to steal MFA-protected credentials.
*   **ElevenLabs and Voicemy.ai:** AI voice synthesis tools used to clone voices for vishing (voice phishing) and bypassing voice authentication systems.
*   **AI-powered social engineering bots (Goose, Telegram fraud bots):** Chatbots that impersonate customer support to trick victims into sharing sensitive information.

---

## Three: From Exposure to Initial Access and Exploitation: How (and Where) Attackers Get the Keys to the Kingdom

The cybersecurity battlefield has shifted dramatically. Attackers no longer have to identify vulnerabilities manually. Instead, they can leverage automated scanning, machine learning (ML), and neatly packaged exploit kits to weaponize newly disclosed security flaws within hours of discovery.

In our latest analysis, Fortinet IPS sensors detected over **97 billion exploitation attempts**, showcasing how cybercriminals are continuously probing for exposed systems.

![Image description: Global Distribution of Exploitation Attempts map showing APAC at 42.4%, EMEA at 26.3%, North America at 20.2%, and LATAM at 11.1%.]

### Attackers’ favorite entry points

Not all vulnerabilities are equal. FortiGuard Labs IPS telemetry highlights key vulnerabilities that remain highly attractive to adversaries:

*   **Windows SMB Information Disclosure Vulnerability (CVE-2017-0147):** Representing **26.7%** of exploitation attempts in 2024, this remains a primary target for infiltrating enterprise networks via the SMB protocol.
*   **Apache Log4j Remote Code Execution (CVE-2021-44228):** With **11.6%** of activity, this vulnerability continues to be a threat, proving many organizations have yet to implement necessary fixes.
*   **Netcore Netis Devices Hardcoded Password (CVE-2019-18935):** This IoT vulnerability accounts for **8%** of all exploitation attempts.

### IoT devices are consistently easy targets in automated exploitation

The surge in exploitation against IoT devices highlights a fundamental security gap. Over **20%** of all recorded exploitation attempts targeted IoT devices.

| IoT Device | % of Exploitation Attempts | Associated CVE | CVSS Score | Potential Impact |
| :--- | :--- | :--- | :--- | :--- |
| Netcore Netis Routers | 18.4% | CVE-2019-18935 | 9.8 | Remote control, botnet recruitment |
| WiFi P2P GoAhead Cameras | 10.5% | CVE-2017-18377 | 8.3 | Unauthorized access, espionage, data exfiltration |
| Zyxel Firewalls and Routers | 3.2% | CVE-2022-30525 | 9.8 | Remote access, configuration tampering |
| TP-Link Archer AX21 Routers | 2.1% | CVE-2023-1389 | 9.0 | Traffic hijacking, credential theft, persistence |
| GPON Routers (Multiple Brands) | 0.9% | CVE-2018-10561 | 9.4 | Persistent access, botnet inclusion, DDoS attacks |

---

## Four: Beyond Initial Access: Post-Exploitation, Lateral Movements, and C2

Once an attacker breaches a system, initial access is just the beginning. In the post-exploitation phase, cybercriminals consolidate their presence, move stealthily, and establish persistent control.

### What type of malware was used for post-exploitation in 2024?

The FortiGuard Labs team identified several notorious Remote Access Trojans (RATs) active in 2024:
*   **Xeno RAT:** Feature-rich, open-source malware capable of screen capture, data exfiltration, and Socks5 reverse proxy.
*   **SparkRAT:** Supports command execution, system manipulation (shutdown/restart), and file/process control.
*   **Async RAT and Trickbot:** Associated with cyber espionage, credential theft, and persistent network intrusion.

### How do attackers move laterally across networks without detection?

The FortiGuard Labs team detected various lateral movement tactics in 2024:
*   Malicious executable downloads within SMB traffic.
*   Anomalies in SMB protocol implementation (e.g., incorrect PID field usage in IMpacket).
*   WMI ExecMethod lateral movement detections.
*   **RDP-based lateral movement**, which played a role in **88%** of incidents investigated in 2024.

### How do attackers map and manipulate Active Directory?

FortiGuard Labs identified multiple adversarial discovery techniques:
*   **DCShadow attacks:** Introducing a rogue domain controller to manipulate AD.
*   **DCSync attacks:** Unauthorized replication of domain controller data.
*   **Active Directory Enumeration:** Suspicious queries for users, groups, and domain trusts.

### How do attackers maintain control over compromised systems?

FortiNDR Cloud identified various C2 techniques:
*   SSL C2 beacons to evade detection in encrypted traffic.
*   Cobalt Strike DNS requests.
*   DNS tunneling and long DNS queries.
*   Domain Generation Algorithm (DGA) domains used to create changing C2 endpoints.

### FortiNDR ATT&CK Matrix (Observed Techniques)

*   **Reconnaissance:** Active Scanning
*   **Initial Access:** Exploit Public-Facing Application, External Remote Services, Valid Accounts, Phishing (Spearphishing Link)
*   **Execution:** Command and Scripting Interpreter (PowerShell), Windows Management Instrumentation, System Services (Service Execution)
*   **Persistence:** Scheduled Task/Job, Create or Modify System Process (Windows Service), Server Software Component (Web Shell), Boot or Logon Autostart Execution
*   **Privilege Escalation:** Exploitation for Privilege Escalation, Valid Accounts (Domain Accounts), Rogue Domain Controller
*   **Defense Evasion:** Obfuscated Files or Information (Stripped Payloads), Indicator Removal (Clear Windows Event Logs), Deobfuscate/Decode Files, System Binary Proxy Execution (Regsvr32), Subvert Trust Controls
*   **Credential Access:** Brute Force, Forced Authentication, OS Credential Dumping (DCSync), Steal or Forge Kerberos Tickets (AS-REP Roasting / Kerberoasting)
*   **Discovery:** Network Service Discovery, Account Discovery, File and Directory Discovery, Permission Groups Discovery, System Network Connections/Configuration Discovery, Remote System Discovery
*   **Lateral Movement:** Remote Services (SMB/Windows Admin Shares), Windows Remote Management, Lateral Tool Transfer, Exploitation of Remote Services
*   **Command and Control:** Application Layer Protocol (DNS, Web Protocols), Proxy (External, Multi-hop), Remote Access Software, Non-Standard Port
*   **Exfiltration:** Exfiltration Over Alternative Protocol (Unencrypted, Asymmetric Encrypted), Exfiltration Over C2 Channel, Exfiltration Over Web Service
*   **Impact:** Network Denial of Service, Resource Hijacking

---

## Five: The Cloud Battlefield: Navigating the New Cybersecurity Landscape

Cloud environments are now a battleground where adversaries exploit misconfigurations, compromised identities, and insecure APIs.

![Image description: Distribution of MITRE ATT&CK Tactics in Cloud Environments: Discovery 25.3%, Initial Access 14.7%, Persistence 12.3%, Privilege Escalation 10.6%, Impact 8.4%, Credential Access 7.9%, Lateral Movement 6.8%, Defense Evasion 6.1%, Collection 3.5%, Exfiltration 3.3%, Execution 1.2%.]

### The silent breach: identity compromise in the cloud

Indicators of cloud identity compromise include:
*   **New logins from unusual locations:** 70% of cases involved unexpected geographies.
*   **New API activity for existing users:** Occurred in 20% of cases.
*   **Credential leaks in code repositories:** API keys found on GitHub and GitGuardian.

### Cloud workloads under siege: the rise of compromised hosts

Common tactics used in compromised cloud hosts:
*   **Execution via Command and Scripting Interpreters (T1059):** Payloads executed through Bash, PowerShell, and Python.
*   **Command and Control via Web Services (T1102):** Abusing legitimate cloud-hosted applications.
*   **Resource Hijacking (T1496):** Rampant abuse for cryptojacking.

---

## Six: Adversary Landscape Analysis

The threat landscape of 2024 was marked by the rapid evolution of cybercriminal groups and the convergence of hacktivism and ransomware.

![Image description: Top APT Adversaries chart: Lazarus 21%, Kimsuky 18%, APT28 13%, Volt Typhoon 12%, APT29 10%, Others 26%.]

### Ransomware landscape: the evolution of digital organized crime

In 2024, **RansomHub (13%)**, **LockBit 3.0 (12%)**, **Play (8%)**, and **Medusa (4%)** were the most active groups. The landscape saw the rise of **13 new groups** operating leak sites.

*   **Affected sectors:** Manufacturing (17%), Business Services (11%), Construction (9%), and Retail (9%).
*   **Geographic distribution:** United States (61%), United Kingdom (6%), and Canada (5%).

### Hacktivism and ransomware: a dangerous convergence

Hacktivist groups such as CyberVolk, Handala, and KillSec started leveraging ransomware. Over **60%** of hacktivist campaigns focused on geopolitical causes (#SavePalestine, #OpIsrael, #OpIndia, #OpUSA).

### Espionage: the quiet cyber war

China and Russia led cyber activity, with groups like **Lazarus (21%)**, **KIMSUKY (18%)**, **APT28 (13%)**, **Volt Typhoon (12%)**, and **APT29 (10%)** conducting advanced campaigns primarily targeting government, technology, and education sectors.

---

## Conclusion: Helping CISOs Defeat Adversaries

A static security posture is a failed security posture. Attackers are accelerating reconnaissance and rapidly exploiting vulnerabilities, shrinking the time between detection and exploitation.

### The CISO playbook for adversary defense

1.  **Simulate real-world attacks with adversary emulation:** Conduct red and purple teaming exercises mimicking threats like LockBit and APT29.
2.  **Reduce attack surface exposure:** Deploy attack surface management (ASM) tools and monitor darknet forums for emerging threats.
3.  **Prioritize high-risk vulnerabilities:** Use frameworks like EPSS and CVSS, focusing on vulnerabilities discussed by cybercrime groups.
4.  **Automate security testing with Breach and Attack Simulation (BAS):** Regularly test defenses against real ransomware payloads and validate zero-trust architectures.
5.  **Leverage dark web intelligence and threat attribution:** Monitor marketplaces for RaaS (PlayBoy, Rape, Medusa) and track hacktivist coordination.

For questions related to this report, please contact us. Digital copies are available at Fortiguard.com/ThreatLandscapeReport.

---

**Copyright © 2025 Fortinet, Inc. All rights reserved.**  
Fortinet®, FortiGate®, FortiCare® and FortiGuard®, and certain other marks are registered trademarks of Fortinet, Inc.  
May 1, 2025 4:16 PM / MKTG-1414-A-0-EN  
www.fortinet.com