# AI-SOC-Report 2026

## Table of Contents
- [Foreword](#foreword)
- [Data & methodology](#data--methodology)
- [Bottom line up front (BLUF)](#bottom-line-up-front-bluf)
- [Endpoint: What 9.25M alerts revealed about triage shortcomings](#endpoint-what-925m-alerts-revealed-about-triage-shortcomings)
- [Malware deep dive](#malware-deep-dive)
- [Windows](#windows)
- [Stealers](#stealers)
- [Ransomware](#ransomware)
- [Linux](#linux)
- [Installers](#installers)
- [Weaponized software](#weaponized-software)
- [Network: Noise masking real threats, exposure risks, and emerging abuse](#network-noise-masking-real-threats-exposure-risks-and-emerging-abuse)
- [Scanners](#scanners)
- [Code Sandboxes](#code-sandboxes)
- [I see plain-text passwords](#i-see-plain-text-passwords)
- [Internal networks](#internal-networks)
- [External networks](#external-networks)
- [Phishing: Scale, signal, and evolving techniques](#phishing-scale-signal-and-evolving-techniques)
- [Identity: High-value signals, high false-positive volume](#identity-high-value-signals-high-false-positive-volume)
- [Cloud: Persistence, evasion, and configuration drift](#cloud-persistence-evasion-and-configuration-drift)
- [About Intezer](#about-intezer)
- [Appendix: The Rise and Fall of CrazyHunter](#appendix-the-rise-and-fall-of-crazyhunter)

---

## Foreword
In 2025, Intezer AI SOC analyzed more than 25 million security alerts across live enterprise SOC environments. This report is grounded in the triage, investigation, and resolution of every one of those alerts, at a forensic level, across Intezer’s global customer base.

With this massive scale of alert volume analyzed, reality is revealed about how attacks actually unfold, where defenses fail, and how SOCs spend their time under pressure.

### The big reset of "acceptable security risk"
For years, security leaders have made tradeoffs in the face of an unsolvable equation where alert volumes rapidly grow and human teams do not. Whether operated in-house or through an MDR, most SOCs are forced to triage aggressively, ignoring and auto-closing a majority of alerts, particularly those that are low-severity or informational.

Surveys consistently show that over 60% of alerts are never reviewed, simply because it is mathematically impossible for human analysts to investigate everything. This reality has become the accepted status quo, and understandably so.

But the emergence of AI-driven SOC platforms that can perform high-fidelity analysis at scale, completely resets the definition of “acceptable risk”. It’s now an imperative to reexamine long-standing risk tolerance, especially when data shows that real threats originate in places we historically had no choice but to ignore.

> Nearly 1% of all incidents are traced back to alerts classified at the lowest severity levels.

### Real threats hiding in low-severity alerts
One of the most consequential findings in this report is how frequently genuine threats originate from alerts initially labeled as low-severity or informational. Across endpoint, cloud, identity, network, and phishing categories, nearly 1% of all incidents are traced back to alerts classified at the lowest severity levels. At scale, this is far from trivial.

With enterprises generating an average of 450,000 alerts annually, this equates to roughly 54 real threats per year, or about one per week, slipping by unnoticed.

Within endpoint alerts, that number rose to nearly 2% low-severity endpoint alerts representing genuine threats.

In practice, these threats are rarely uncovered by in-house or external SOC teams. Most AI SOC platforms that exclusively rely on AI agents, are also limited to triaging high- and medium-severity alerts. These “below the radar” alerts can only be identified through highly scalable, automated and forensic-grade triage that can examine behavior, lineage, and intent, for 100% of all ingested alerts.

### Noise, stealth, and misjudged risk
Beyond severity misclassification, the data highlights a threat landscape dominated by noise masking meaningful activity. Scanning of public-facing infrastructure generated some of the highest alert volumes, while identity telemetry was flooded with “impossible travel” detections.

In cloud environments, however, the most frequent alerts related to defense evasion and persistence, reflecting attackers’ focus on stealth, long-term access, and abuse of legitimate services through token manipulation and obfuscation.

Taken together, these findings point to a consistent pattern. While alert volume is increasing, severity and risk are often misaligned with meaningful threats frequently hidden among signals that are deprioritized or ignored.

The sections that follow break down these patterns in detail and translate them into operational lessons drawn from a year of large-scale forensic triage. This is the State of the SOC as it exists in practice, shaped by millions of alerts, real adversaries, and the constraints security teams face every day.

As always, Intezer’s AI SOC platform along with our experienced security analysts and researchers, stand ready to deliver stronger security outcomes and real risk reduction that scales with your business.

*Itai Tevet, Intezer CEO and Co-Founder*

---

## Data & methodology
This report is based on a comprehensive analysis of threat activity observed across Intezer’s global customer base throughout 2025. To identify emerging attack patterns, evasion techniques, and security weaknesses, a broad and diverse dataset was examined.

- **25M** alerts triaged
- **10M** monitored endpoints and identities
- **180M** files analyzed
- **3M** domains and URLs investigated
- **7M** IP addresses analyzed
- **82K** endpoint forensic investigations, including live memory scans
- **550K** emails analyzed

All data used in this study were processed in accordance with strict privacy and security standards. Intezer’s research methodology is designed to ensure no sensitive, personal, or customer-identifying information is accessed, retained, or included in the analysis. Findings are aggregated and anonymized, focusing solely on technical threat indicators and behavioral trends.

---

## Bottom line up front (BLUF)
### Intezer AI SOC overall stats
- Less than 2% of all the alerts were escalated by Intezer to a human.
- 98% verdict accuracy.
- Sub-minute median triage time.
- Across all alert types, 0.6% of escalations came from low-severity or informational events.

### Triaged alert type breakdown
- Endpoint: 37%
- Network: 34%
- Identity: 14%
- Phishing: 6%
- DLP: 6%
- Cloud: 2.5%
- Specific/Other: <1%

### Endpoint stats
- 2% of escalations came from low-severity or informational endpoint alerts.
- 180 million files analyzed across Windows, Linux, MacOS, iOS, and Android.
- Over 82,000 forensic investigations performed. In over 1.6% of the forensic scans, we found that the endpoint was still compromised even though the EDR reported the threat had been mitigated.
- Threat actors deploying stealers and RATs use increasingly complex, multi-stage loaders.
- Akira Ransomware has topped our results as one of the most active ransomware groups in 2025.
- Strains of Mirai were the most prevalent malware identified on Linux hosts.

### Network stats
- Over 1M alerts on IP addresses were for scanning activity. 88% were blocked at the source by the firewall.
- Of the remaining 12% that required triage, only 6% were confirmed as malicious.
- Code sandboxes are being heavily abused to host phishing sites targeting cryptocurrency.
- A significant amount of internal network traffic remains unencrypted.

### Phishing stats
- Over half a million user-reported phishing emails were analyzed.
- Over 3 million phishing and malware-related URLs investigated. Microsoft was the most impersonated brand.
- Threat actors have increased their use of CAPTCHA (specifically Cloudflare Turnstile) to make detection more difficult.
- PayPal's infrastructure is being heavily abused for callback scams.

### Identity stats
- The most common identity alert was for location or session anomalies (36%). Most "impossible travel" alerts are false positives caused by VPNs and mobile phones.

### Cloud alert stats
- Most cloud-based alerts fall in the defense evasion and persistence category.
- Amazon S3 is involved in the majority of AWS misconfigurations.

---

## Endpoint: What 9.25M alerts revealed about triage shortcomings
In 2025, Intezer AI SOC investigated 9.25M endpoint alerts. 43% were classified as informational or low-severity. Of these, nearly 2% were real incidents.

Additionally, over half of all endpoint alerts were not automatically mitigated by their endpoint protection solution. Of these non-mitigated alerts, almost 9% were confirmed as malicious.

> **Note**: While it’s possible these numbers reflect a vendor issue when it comes to mitigating or correctly labeling threats, there can be many other legitimate factors at play. All that is certain is that SOC teams need to be vigilant.

---

## Malware deep dive
![Chart showing top malware families: Mimikatz, Meterpreter, Metasploit, Cobalt Strike, Winos, SharpHound, Donut Injector, XMRig Miner, StrelaStealer]

---

## Windows
Windows accounts for 51% of all endpoints. 
- **Devices**: Desktop (53%), Server (46%), Virtual (<1%), Phone/tablet (<1%).

### Stealers
Credential and information stealers remained prevalent.
- **Agent Tesla**: 39%
- **Snake Keylogger & Formbook**: >33%
- **Mimikatz, LummaC2, RedLine Stealer**: Significant activity

### Ransomware
Activity is concentrated around a few dominant families: Akira, INC, and LockBit. Other active groups include Phobos, AvosLocker, and Rhysida.

---

## Linux
Mirai remains the most prevalent threat, exploiting weak credentials and unpatched IoT/server infrastructure. Akira and INC are the most dominant ransomware families targeting Linux.

---

## Installers
![Pie chart of installer delivery mechanisms: NSIS (45.8%), WinRAR.SFX (33.4%), WEXTRACT (6.9%), InnoSetup (6.7%), 7-Zip.SFX (4.1%), Other (3.1%)]

### Weaponized software
- **PNGPlug/ValleyRAT**: A new multi-stage loader that hides payloads within PNG files.
- **XE Group**: Exploited zero-day vulnerabilities (CVE-2024-57968 and CVE-2025-25181) in the VeraCore warehouse management platform.

---

## Network: Noise masking real threats, exposure risks, and emerging abuse
### Scanners
Web scanners account for over one million alerts. 88% were mitigated by firewalls. Of the 12% not mitigated, 6% were confirmed as genuine threats.

### Code Sandboxes
Attackers are abusing platforms like **Vercel**, **CodePen**, **JSitor**, and **JSBin** to host phishing pages because they offer trusted domains and free hosting.

---

## I see plain-text passwords
There is a five-to-one ratio of internal vs. external plain-text password detections.
- **Internal**: Mostly LDAP, HTTP, FTP, Databases, and Telnet.
- **External**: Mostly Databases, FTP, HTTP, SMTP, and Apache Subversion (SVN).

---

## Phishing: Scale, signal, and evolving techniques
Intezer processed 550,000 user-reported phishing emails. Less than 8% were confirmed malicious.
- **Shift in focus**: Attackers are moving from endpoint-based attacks to browser-based attacks.
- **Brand Impersonation**: Microsoft and DocuSign account for 85% of impersonation cases.
- **Callback Scams**: Abusing PayPal and Microsoft infrastructure to bypass email security.

### New phishing threats
1. **Encoded JavaScript in SVG images**.
2. **Hidden URLs in PDF annotations**.
3. **Malicious URLs in OneDrive shares**.
4. **MHT files embedded in OpenXML documents**.

---

## Identity: High-value signals, high false-positive volume
- **Location/Geo/Session Anomalies**: 36.7%
- **Login Failures**: 22%
- **MFA Issues**: 11.9%
- **Brute Force**: 8.2%

Most identity alerts are false positives caused by VPNs, mobile data routing, and security tools inspecting traffic.

---

## Cloud: Persistence, evasion, and configuration drift
Cloud alerts focus on **Defense Evasion** and **Persistence**.
- **S3 Misconfigurations**: 70% of findings relate to S3 hardening (SSL, access logging, bucket policies).
- **EC2 Misconfigurations**: Multiple ENIs, public IPv4 addresses, and outdated instance types.

---

## About Intezer
Intezer AI SOC delivers 24/7, forensic-grade cyber alert triage across 100% of alerts, with only 2% escalated for human review. Powered by **ForensicAI™**, Intezer specializes in deep forensic investigation to deliver unmatched accuracy and speed.

---

## Appendix: The Rise and Fall of CrazyHunter
In early 2025, Intezer and AIShield investigated the "CrazyHunter" ransomware group.
- **Tactics**: Used vulnerable drivers (CVE-2018-6606) for privilege escalation and Active Directory abuse for lateral movement.
- **Tooling**: ZammOcide (AV-killer), Syscall Phantom (loader), GoStealthFile (exfiltration), and Hunter Ransomware.
- **Attribution**: Taiwanese authorities identified the operator as a man surnamed Luo from Zhejiang, China, responsible for compromising over 500 systems.