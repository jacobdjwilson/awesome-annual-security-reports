# AI SOC Report 2026

## Table of Contents
- [Foreword](#foreword)
- [Data & methodology](#data--methodology)
- [Bottom line up front (BLUF)](#bottom-line-up-front-bluf)
- [Endpoint](#endpoint)
- [Malware deep dive](#malware-deep-dive)
- [Windows](#windows)
- [Linux](#linux)
- [Installers](#installers)
- [Weaponized software](#weaponized-software)
- [Network](#network)
- [Scanners](#scanners)
- [Code Sandboxes](#code-sandboxes)
- [I see plain-text passwords](#i-see-plain-text-passwords)
- [Phishing](#phishing)
- [Identity](#identity)
- [Cloud](#cloud)
- [About Intezer](#about-intezer)
- [Appendix](#appendix)

---

## Foreword

In 2025, Intezer AI SOC analyzed more than 25 million security alerts across live enterprise SOC environments. This report is grounded in the triage, investigation, and resolution of every one of those alerts, at a forensic level, across Intezer’s global customer base.

With this massive scale of alert volume analyzed, reality is revealed about how attacks actually unfold, where defenses fail, and how SOCs spend their time under pressure.

### The big reset of "acceptable security risk"
For years, security leaders have made tradeoffs in the face of an unsolvable equation where alert volumes rapidly grow and human teams do not. Whether operated in-house or through an MDR, most SOCs are forced to triage aggressively, ignoring and auto-closing a majority of alerts, particularly those that are low-severity or informational.

Surveys consistently show that over 60% of alerts are never reviewed, simply because it is mathematically impossible for human analysts to investigate everything. This reality has become the accepted status quo, and understandably so.

But the emergence of AI-driven SOC platforms that can perform high-fidelity analysis at scale, completely resets the definition of “acceptable risk”. It’s now an imperative to reexamine long-standing risk tolerance, especially when data shows that real threats originate in places we historically had no choice but to ignore.

### Real threats hiding in low-severity alerts
One of the most consequential findings in this report is how frequently genuine threats originate from alerts initially labeled as low-severity or informational. Across endpoint, cloud, identity, network, and phishing categories, nearly 1% of all incidents are traced back to alerts classified at the lowest severity levels. At scale, this is far from trivial.

With enterprises generating an average of 450,000 alerts annually, this equates to roughly 54 real threats per year, or about one per week, slipping by unnoticed.

Within endpoint alerts, that number rose to nearly 2% low-severity endpoint alerts representing genuine threats.

In practice, these threats are rarely uncovered by in-house or external SOC teams. Most AI SOC platforms that exclusively rely on AI agents, are also limited to triaging high- and medium-severity alerts. These “below the radar” alerts can only be identified through highly scalable, automated and forensic-grade triage that can examine behavior, lineage, and intent, for 100% of all ingested alerts.

### Noise, stealth, and misjudged risk
In cloud environments, however, the most frequent alerts related to defense evasion and infrastructure generated some of the highest alert volumes, while identity telemetry was flooded with “impossible travel” detections.

Scanning of public-facing services through token manipulation and obfuscation, reflecting attackers’ focus on stealth, long-term access, and abuse of legitimate persistence.

Taken together, these findings point to a consistent pattern. While alert volume is increasing, severity and risk are often misaligned with meaningful threats frequently hidden among signals that are deprioritized or ignored.

The sections that follow break down these patterns in detail and translate them into operational lessons drawn from a year of large-scale forensic triage. This is the State of the SOC as it exists in practice, shaped by millions of alerts, real adversaries, and the constraints security teams face every day.

As always, Intezer’s AI SOC platform along with our experienced security analysts and researchers, stand ready to deliver stronger security outcomes and real risk reduction that scales with your business.

_Itai Tevet, Intezer CEO and Co-Founder_

---

## Data & methodology

This report is based on a comprehensive analysis of threat activity observed across Intezer’s global customer base throughout 2025. To identify emerging attack patterns, evasion techniques, and security weaknesses, a broad and diverse dataset was examined.

- **25M** alerts triaged
- **10M** monitored endpoints and identities
- **180M** files analyzed
- **3M** domains and URLs analyzed
- **7M** IP addresses investigated
- **82K** endpoint forensic investigations, including live memory scans
- **550K** emails analyzed

All data used in this study were processed in accordance with strict privacy and security standards. Intezer’s research methodology is designed to ensure no sensitive, personal, or customer-identifying information is accessed, retained, or included in the analysis.

Findings are aggregated and anonymized, focusing solely on technical threat indicators and behavioral trends.

---

## Bottom line up front (BLUF)

### Intezer AI SOC overall stats
- Less than 2% of all the alerts were escalated by Intezer to a human.
- 98% verdict accuracy.
- Sub-minute median triage time.
- Across all alert types, 0.6% of escalations came from low-severity or informational events.

### Triaged alert type breakdown
![Chart showing alert distribution: SIEM 84%, EDR 14%, Email 2%]

### Endpoint stats
- 2% of escalations came from low-severity or informational endpoint alerts.
- 180 million files analyzed.
- Over 82,000 forensic investigations performed on endpoints. In over 1.6% of the forensic scans, we found that the endpoint was still compromised even though the EDR reported the threat had been mitigated.
- Threat actors deploying stealers and RATs use increasingly complex, multi-stage loaders.
- Akira Ransomware has topped our results as one of the most active ransomware groups in 2025.
- Strains of Mirai were the most prevalent malware identified on Linux hosts.

### Network stats
- Over 1M alerts on IP addresses were for scanning activity. 88% were blocked at the source.
- Of the remaining 12% that required triage, only 6% were confirmed as malicious.
- Code sandboxes are being heavily abused to host phishing sites.
- A significant amount of internal network traffic remains unencrypted.

### Phishing stats
- Over half a million user-reported phishing emails were analyzed.
- Over 3 million phishing and malware-related URLs investigated. Microsoft was the most impersonated brand.
- Threat actors have increased their use of CAPTCHA to make detection more difficult.
- PayPal's infrastructure is being heavily abused for callback scams.

### Identity stats
- The most common identity alert was for location or session anomalies (36%).
- Most "impossible travel" alerts are false positives.

### Cloud alert stats
- Most cloud-based alerts fall in the defense evasion and persistence category.
- Amazon S3 is involved in the majority of AWS misconfigurations.

---

## Endpoint: What 9.25M alerts revealed about triage shortcomings

In 2025, Intezer AI SOC investigated 9.25M endpoint alerts. 43% were classified as informational or low-severity. Of these, nearly 2% were real incidents.

Additionally, over half of all endpoint alerts were not automatically mitigated by their endpoint protection solution. Of these non-mitigated alerts, almost 9% were confirmed as malicious.

> **Note:** While it’s possible these numbers reflect a vendor issue when it comes to mitigating or correctly labeling threats, there can be many other legitimate factors at play. All that is certain is that SOC teams need to be vigilant.

---

## Malware deep dive

One of Intezer’s proprietary investigative tools is an endpoint scanner which performs live memory forensics on a host and identifies malicious code running within a process.

**Top malware families compromising endpoints (detected in memory):**
- Mimikatz
- Meterpreter
- Metasploit
- Cobalt Strike
- Winos
- SharpHound
- Donut Injector
- XMRig Miner
- StrelaStealer

---

## Windows

Windows remains the most popular operating system for endpoints, accounting for 51% of all endpoints.

### Stealers
Credential and information stealers remained a prevalent threat, with **Agent Tesla** dominating the landscape (40.3% of all detections). It was followed by Snake Keylogger and Formbook.

### Ransomware
The ransomware activity observed shows a clear concentration around a few dominant families with **Akira**, **INC**, and **LockBit** appearing as the most active groups.

---

## Linux

**Mirai** remains the most prevalent threat in Linux environments, reflecting the continued exploitation of vulnerable IoT and server infrastructure. We also observe ransomware families targeting Linux systems alongside Windows environments, with Akira and INC remaining the most dominant.

---

## Installers

The breakdown highlights how frequently specific installers are abused for malware delivery:
- **NSIS**: 33.4%
- **WinRAR.SFX**: 45.8%
- **WEXTRACT**: 6.7%
- **InnoSetup**: 6.9%
- **7-Zip.SFX**: 4.1%
- **Other**: 3.1%

---

## Weaponized software

### PNGPlug and ValleyRAT
Our research team uncovered a campaign that utilized a newly observed multi-stage loader called **PNGPlug** to deliver the well-known remote access trojan, **ValleyRAT**. Attackers are focusing on layered execution and loader obfuscation to bypass traditional detections.

### Zero-day vulnerabilities
In collaboration with Solis, Intezer identified two previously unknown zero-day vulnerabilities (**CVE-2024-57968** and **CVE-2025-25181**) that were being actively exploited by the **XE Group** threat group targeting the VeraCore warehouse management platform.

---

## Network: Noise masking real threats, exposure risks, and emerging abuse

### Scanners
Web scanners account for a significant portion of the alerts triaged by Intezer AI SOC with over one million alerts this year alone. 88% were mitigated by firewalls; of the remaining 12%, 6% were confirmed as genuine threats.

### Code Sandboxes
Code sandboxes (e.g., Vercel, CodePen, JSitor) are being heavily abused to host phishing sites. They offer immediate deployment, a trusted domain, and no infrastructure cost.

---

## I see plain-text passwords

We found roughly a five-to-one ratio of internal detections vs. external ones regarding plain-text passwords. 

- **Internal networks**: Most detections were linked to directory services and other authentication mechanisms that still rely on unencrypted LDAP.
- **External networks**: The most frequent cases involved database protocols, unencrypted file transfer traffic, and HTTP sessions without TLS encryption.

---

## Phishing: Scale, signal, and evolving techniques

In 2025, Intezer AI SOC processed 550,000 phishing emails. A bit less than 8% were confirmed as malicious.

### Brand impersonation and callback scams
- **Brand Impersonation**: 25.3%
- **Callback Scam**: 28.7%
- **Credential phishing link**: 7.8%

Microsoft and DocuSign accounted for nearly 85% of brand impersonation cases.

### New phishing threats and attack vectors
Intezer uncovered a shift in attacker strategy, from simple deception to structural and contextual evasion:
1. **Encoded JavaScript in SVG images.**
2. **Hidden URLs in PDF annotations.**
3. **Malicious URLs in OneDrive shares.**
4. **MHT files embedded in OpenXML documents.**

---

## Identity: High-value signals, high false-positive volume

The majority of identity alerts were driven by location-based anomalies (37%) and login failures (22%).

### Impossible travel
Only ~2% of impossible-travel alerts were confirmed as real compromises. High false-positive rates are driven by:
- **VPN Usage**: 30% of all impossible-travel alerts.
- **Mobile phones**: Data centers routing traffic far from the user’s physical location.
- **Security tools**: Overlapping security products (Zero Trust, secure web gateways) triggering alerts against each other.

---

## Cloud: Persistence, evasion, and configuration drift

The cloud alert data shows a strong concentration of activity around **Defense Evasion** and **Persistence**.

### Not the best practices
Across all services, **S3** accounts for the largest share of control violations (70% of all findings relate to S3 security hardening). The most frequently violated S3 controls are those requiring SSL for bucket access, enforcing server access logging, and restricting bucket policies.

---

## About Intezer

Intezer AI SOC delivers 24/7, forensic-grade cyber alert triage across 100% of alerts, with only 2% escalated for human review. Powered by **ForensicAI™**, Intezer specializes in deep forensic investigation to deliver unmatched accuracy and speed. Intezer is trusted by global enterprises including NVIDIA, MGM Resorts, Equifax, Salesforce, and Ferguson.

---

## Appendix: The Rise and Fall of CrazyHunter

In early 2025, Intezer and Taiwan-based AIShield investigated the **CrazyHunter** ransomware group. The campaign targeted Taiwan’s healthcare, education, and energy sectors.

### CrazyHunters Arsenal
- **Hunter Ransomware (Prince)**: Rebranded open-source encryptor.
- **ZammOcide**: AV-killer exploiting CVE-2018-6606.
- **Syscall Phantom**: Loader using manual syscalls to bypass EDR hooks.
- **GoStealthFile**: Golang utility for exfiltration.

Taiwanese authorities have identified the operator behind the CrazyHunter ransomware as a man surnamed Luo from Zhejiang, China. This confirmation marks a rare and significant instance of clear attribution in a ransomware investigation.