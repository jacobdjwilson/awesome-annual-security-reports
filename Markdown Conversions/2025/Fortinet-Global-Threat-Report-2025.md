# 2025 Global Threat Landscape Report

A Report by FortiGuard Labs

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

## Introduction: Acceleration of the Adversary Advantage

This 2025 Threat Landscape Report reveals a dramatic escalation in both the scale and sophistication of cyberattacks. Data shows adversaries are moving faster than ever, automating reconnaissance, compressing the time between vulnerability disclosure and exploitation, and scaling their operations through the industrialization of cybercrime. Across all attack phases, FortiGuard Labs observed that threat actors are leveraging automation, commoditized tools, and AI to erode the traditional advantages held by defenders systematically.

The challenge is clear: Your adversary’s advantage is accelerating. From pre-attack reconnaissance to post-compromise persistence, attackers now operate with unprecedented speed, precision, and reach, challenging organizations to shift from reactive defense to proactive exposure management.

### Key findings
- **Reconnaissance is surging.** Cybercriminals are deploying automated scanning at a global scale. Active scanning in cyberspace reached unprecedented levels in 2024, rising by 16.7% worldwide.
- **AI is supercharging the cybercrime supply chain.** Threat actors leverage AI for phishing, impersonation, extortion, and evasion tactics.
- **Exploitation volumes are soaring as speed remains steady.** FortiGuard Labs recorded over 97 billion exploitation attempts during the year.
- **Post-exploitation tactics are getting stealthier.** Cybercriminals increasingly “live off the land,” using trusted tools and protocols to escalate privileges and persist undetected.
- **Cloud attacks are evolving, but misconfigurations still reign.** Cloud environments remain a top target, with adversaries exploiting persistent weaknesses, such as open storage buckets, over-permissioned identities, and misconfigured services.

---

## One: Cyber Reconnaissance Surge: The Rising Threat of Automated Scanning

Active scanning in cyberspace reached unprecedented levels in 2024, rising by 16.7% worldwide. Intrusion prevention system (IPS) engines in FortiGate Next-Generation Firewalls (NGFWs) detected an intensification of these scans across all geographies.

![Behavioral Trend Analysis chart showing 1.16 trillion detections in 2024 compared to 993 billion in the previous year]

### Millions of active scans: what threat actors are looking for
Attackers are targeting widely used protocols in key sectors, such as telecommunications, industry, OT, industrial control systems (ICS), and financial services:
- **SIP (VoIP):** SIP represented over 49% of detected scans.
- **Modbus TCP:** Modbus TCP accounted for about 1.6% of scans, highlighting concerns about industrial infrastructure and SCADA systems.

### Which scanning tools are cybercriminals using?
- **SIPVicious:** Responsible for nearly 50% of detected scanning events.
- **Qualys:** Appears in about 2.5% of scans.
- **Nmap:** Detected in less than 1% of events.
- **Nessus and OpenVAS:** Widely used to explore vulnerabilities in enterprise systems.

---

## Two: Shedding Light on the Darknet: How Adversaries Prepare to Strike

The darknet has evolved from a mere refuge for cybercriminals into a supply chain for cyberattacks. The FortiGuard Labs team has identified a rapidly growing underground ecosystem where stolen credentials, corporate access, exploits, and AI-powered tools are bought, sold, and developed.

### Credentials are the currency of cybercrime
In 2024, over 100 billion records were shared in underground forums, a 42% increase from 2023. This surge is largely driven by "combo lists"—massive data files containing email addresses, usernames, and passwords obtained from past breaches.

### Credential Theft-as-a-Service: the industrialized rise of infostealers
In 2024, FortiGuard Labs observed a 500% increase in logs from systems compromised by infostealer malware. Top infostealers include:
- **Redline (60%):** Favored for its affordability and ease of use.
- **Vidar (27%):** Specializes in harvesting credentials and session tokens.
- **Racoon (12%):** Focuses on mass data exfiltration.

### AI-enabled cybercrime
The FortiGuard Labs team has identified numerous AI-driven tools helping adversaries, including:
- **FraudGPT and WormGPT:** AI-powered text generators for phishing and malicious code.
- **BlackmailerV3:** An AI-driven extortion toolkit.
- **ElevenLabs and Voicemy.ai:** AI voice synthesis tools used for vishing and bypassing voice authentication.

---

## Three: From Exposure to Initial Access and Exploitation: How (and Where) Attackers Get the Keys to the Kingdom

Fortinet IPS sensors detected over 97 billion exploitation attempts in 2024. Asia-Pacific (APAC) accounts for the largest share (42%) of recorded exploitation attempts, followed by EMEA (26%), North America (20%), and Latin America (11%).

### Attackers’ favorite entry points
- **Windows SMB Information Disclosure Vulnerability (CVE-2017-0147):** 26.7% of exploitation attempts.
- **Apache Log4j Remote Code Execution (CVE-2021-44228):** 11.6% of activity.
- **Netcore Netis Devices Hardcoded Password (CVE-2019-18935):** 8% of exploitation attempts.

### IoT devices are consistently easy targets
Over 20% of all recorded exploitation attempts targeted IoT devices. Routers (Netcore, TP-Link, D-Link) account for the highest percentage of attacks, followed by surveillance cameras.

---

## Four: Beyond Initial Access: Post-Exploitation, Lateral Movements, and C2

In the post-exploitation phase, cybercriminals consolidate their presence, move stealthily across networks, and establish persistent control.

### Malware used for post-exploitation
- **Xeno RAT:** Feature-rich, open-source malware.
- **SparkRAT:** Supports command execution and system manipulation.
- **Async RAT and Trickbot:** Associated with cyber espionage and credential theft.

### Lateral movement tactics
- Malicious executable downloads within SMB traffic.
- Anomalies in SMB protocol implementation.
- WMI ExecMethod lateral movement.
- RDP-based lateral movement (involved in 88% of incidents investigated in 2024).

### MITRE ATT&CK Matrix
The report includes a comprehensive mapping of observed techniques across the MITRE ATT&CK framework, covering Reconnaissance, Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Command and Control, Exfiltration, and Impact.

---

## Five: The Cloud Battlefield: Navigating the New Cybersecurity Landscape

Cloud environments are a battleground where adversaries exploit misconfigurations, compromised identities, and insecure APIs.

### The silent breach: identity compromise
- **New logins from unusual locations:** 70% of cases involved new logins from unexpected geographies.
- **New API activity for existing users:** Occurred in 20% of cases.
- **Credential leaks in code repositories:** Publicly accessible API keys are frequently exploited.

### Cloud workloads under siege
- **Execution via Command and Scripting Interpreters:** 47 detected incidents.
- **Command and Control via Web Services:** 23 cases.
- **Resource Hijacking:** 24 incidents of cryptojacking.

---

## Six: Adversary Landscape Analysis

The threat landscape of 2024 was marked by the rapid evolution of cybercriminal groups and the rise of new ransomware actors.

### Ransomware landscape
RansomHub (13%), LockBit 3.0 (12%), Play (8%), and Medusa (4%) were the most active ransomware groups. 13 new groups operating leak sites emerged in 2024.

### Hacktivism and espionage
- **Hacktivism:** Groups like RipperSec and Z-BL4CX-H4T used Telegram for coordination. Over 60% of campaigns focused on geopolitical causes.
- **Espionage:** State-sponsored actors, particularly from China and Russia, led cyber activity. Top groups included Lazarus (21%), Kimsuky (18%), APT28 (13%), Volt Typhoon (12%), and APT29 (10%).

---

## Conclusion: Helping CISOs Defeat Adversaries

A static security posture is a failed security posture. CISOs must shift from reactive defense to Continuous Threat Exposure Management (CTEM).

### The CISO playbook for adversary defense
1. **Simulate real-world attacks:** Conduct red and purple teaming exercises.
2. **Reduce attack surface exposure:** Deploy attack surface management (ASM) tools.
3. **Prioritize high-risk vulnerabilities:** Use risk-based frameworks like EPSS and CVSS.
4. **Automate security testing:** Use Breach and Attack Simulation (BAS).
5. **Leverage dark web intelligence:** Monitor marketplaces for emerging threats and attribution.

For questions related to this report, please contact FortiGuard Labs.