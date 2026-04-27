# Global Threat Landscape Report: 1H 2023
A Semiannual Report by FortiGuard Labs
August 2023

## Table of Contents
- [Executive Summary](#executive-summary)
- [1H 2023 at a Glance](#1h-2023-at-a-glance)
- [Let’s Rewind: Five-Year Threat Trends](#lets-rewind-five-year-threat-trends)
- [Penetrating the Red Zone](#penetrating-the-red-zone)
- [From Exploit Prediction to Outbreak](#from-exploit-prediction-to-outbreak)
- [Global ATT&CK Heatmap](#global-attck-heatmap)
- [Technique Insights from Endpoint Telemetry](#technique-insights-from-endpoint-telemetry)
- [Protecting Your Enterprise from Evolving Threats](#protecting-your-enterprise-from-evolving-threats)
- [Conclusion and Final Outlook](#conclusion-and-final-outlook)

---

## Executive Summary

The threat landscape and organizations’ attack surfaces are constantly transforming. And the ability of cybercriminals to quickly design and adapt their techniques to exploit this evolving environment continues to pose significant risks to businesses of all sizes, regardless of industry or geography.

As we examine activity in the first half of 2023, we see cybercrime organizations and nation-state cyber-offensive groups swiftly adopting new technologies. Notably, some of these actors operate much like traditional enterprises, complete with well-defined responsibilities, deliverables, and objectives. This organizational structure, combined with deep pockets resulting from past exploits or nation-state sponsors, facilitates their offensive stance, allowing them to experiment with and incorporate game-changing technologies, such as new generative AI, that make their attacks more complex and harder to detect.

A significant uptick in the sophistication of malicious actors is especially evident in the cybersecurity domain, where threats have escalated in frequency and complexity. This is characterized by a rise in highly targeted attacks across various sectors, including intricate ransomware campaigns, substantial data breaches, and a notable shift in MITRE ATT&CK tactics, as observed through our global, AI-enhanced detection capabilities.

## 1H 2023 at a Glance

- **APT Groups**: Activity was detected for 41 of 138 (30%) APT groups identified by MITRE. These attacks are more focused and planned and also occur in quick “waves,” so seeing a third of all categorized APT groups being active is concerning.
- **Ransomware**: The ransomware rollercoaster continued, ending 1H 2023 13x higher than it began. Fewer organizations are successfully detecting ransomware than in the past (13% versus 22%), reaffirming that ransomware is also becoming more sophisticated and targeted.
- **ICS and OT Attacks**: Attacks targeting industrial control systems (ICS) and operational technologies (OT) didn’t occur at high volume but trended up over the first half of 2023. Half of organizations saw ICS or OT exploits, with energy and utilities ranking among the top targets.

### Into the Red Zone
- **Time-to-Exploitation**: The percent of all endpoint vulnerabilities targeted by attackers remained relatively steady (around 8%) in 1H 2023 compared to the previous period.
- **ATT&CK Sightings**: Our analysis shows that the top most exploitable vulnerabilities, as identified by EPSS, are 327 times more likely to be attacked within a week than others on your radar. Using our detection technologies, we observed activity for two-thirds of all known MITRE ATT&CK techniques over the first half of 2023.

![Chart showing 12.6x increase in malware detections from Jan to June 2023]

In 1H 2023, we observed significant activity among advanced persistent threat (APT) groups, a rise in ransomware frequency and complexity, increased botnet activity, a shift in MITRE ATT&CK techniques used by attackers, and more.

### A third of all categorized APT groups were active in 1H 2023
It’s worth taking a moment to spotlight the threat actors behind these trends we’re analyzing. As part of their efforts to support the ATT&CK framework, MITRE tracks 138 cyberthreat groups.[^1] Monitoring the collective activity of these groups is an essential component of mapping and analyzing the threat landscape. From January through June 2023, we observed activity attributed to 41 of these groups (30%). Of those, Turla, StrongPity, Winnti, OceanLotus, and WildNeutron were the most active based on malware genetic code analysis.

### The ransomware rollercoaster continues
While ransomware has existed for decades, in recent years, we’ve witnessed threat actors using more-sophisticated and complex strains to infiltrate networks, largely thanks to the rise of Ransomware-as-a-Service (RaaS) operations.[^2] Ransomware shows no signs of slowing, with ransomware activity ending 13 times higher than at the start of 2023 as a proportion of all malware detections.

![Figure 1: Top malware families by type, categorized by Cryptominers, Infostealers, Ransomware, and RATs]

### Wipers are waning… for now
One category of ransomware not listed above is wiper malware.[^4] Wipers are aptly named because this destructive attack technique “wipes” data off infected systems. We observed a surge in wiper use in early 2022, mainly in conjunction with the Russian-Ukrainian conflict.[^5] And while that increase persisted through the rest of the year, it slowed over the first half of 2023.

## Let’s Rewind: Five-Year Threat Trends

### Exploit variants on the rise
The count of unique exploit detections is up 68% over the past five years. This indicates that we have more ways to detect malicious attacks today than we have previously. Additionally, it demonstrates that attackers are multiplying and diversifying their exploits. But at the same time, we observed a 75% drop in exploitation attempts per organization and a 10% dip in severe exploits.

### Increased malware activity driven by organized cybercrime
Malware families and variants have exploded over the past five years, up 135% and 175%, respectively. Arguably more noteworthy is that the number of malware families that have infiltrated at least 10% of global organizations (a critical prevalence threshold) has doubled.

### Botnets become more persistent
Today, there are more active botnets (+27%) and a higher incidence rate of botnet infection among organizations (+126%). Over the last six months, the average "active days" for botnets was 83 of 183 days, representing a more than 1,000-fold increase from measurements taken at the beginning of 2018.

## Penetrating the Red Zone

We introduced the “Red Zone” in our 2H 2022 Global Threat Landscape Report to better understand how likely (or unlikely) it is that threat actors will exploit a specific vulnerability.[^6] In the first half of 2023, the proportion of CVEs under attack dropped to 8.3%.

![Figure 2: All CVEs by presence on endpoints and among attacks]
![Figure 3: CVEs for multiple platforms by presence on endpoints and among attacks]

## From Exploit Prediction to Outbreak

Since its inception, Fortinet has been a core contributor to exploitation activity data in support of the Exploit Prediction Scoring System (EPSS).[^7] Vulnerability management teams use EPSS to help prioritize their remediation efforts.

![Figure 4: Evolution of EPSS and exploitation for the MOVEit vulnerability]

### Exploitation rate of vulnerabilities with different EPSS scores
- **Within one week of CVE published**: EPSS Top 1% (22.3%) vs. EPSS Bottom 50% (<0.1%).
- **Within one year of CVE published**: EPSS Top 1% (85.3%) vs. EPSS Bottom 50% (<0.1%).

![Figure 5: Exploitation rate of vulnerabilities with different EPSS scores]

## Global ATT&CK Heatmap

MITRE offers us a better understanding of the operations of threat actors. Both easy-to-follow and actionable, ATT&CK enables defenders to categorize threat actor behaviors in a manner that is both systematic and repeatable.

![Figure 6: ATT&CK techniques in cloud data by tactic]

In the Initial Access phase, the most-prevalent technique observed is replication via removable media.[^11] In the Execution phase, we noted a surge in Exploitation for User Execution.[^14] For the Persistence phase, we continue to see high instances of DLL Sideloading (under Hijack Execution Flow).[^16]

## Technique Insights from Endpoint Telemetry

Looking at our FortiEDR data gives us another perspective regarding attacks and the initial access techniques that cybercriminals use.

![Figure 7: Top ATT&CK techniques detected by FortiEDR by month]

The most active techniques we observed during 1H 2023 include:
- Process Injection
- Input Capture
- OS Credential Dumping
- Exploit Public-Facing Application
- Exploit For Defense Evasion

## Protecting Your Enterprise from Evolving Threats

### Share and utilize threat intelligence
Fortinet is a founding member of the Cyber Threat Alliance (CTA), an organization created in 2014 to enable threat intelligence sharing among competing cybersecurity vendors.[^24]

### Understand attack flows to identify patterns and indicators of compromise
Understanding the attack flow, from initial entry points to post-exploitation activities, is essential for developing effective cybersecurity strategies.

![Figure 8: MITRE ATT&CK Flow Builder - Example Flow]

### Shore up your technologies and processes
There’s no time like now to implement new security technologies or reassess your current stack. Regardless of your chosen tools, you must ensure they can leverage AI, ML, deep learning (DL), and advanced analytics.

## Conclusion and Final Outlook

The strengthening of partnerships sharing threat intelligence between the public and private sectors is crucial in fighting this cyber war. We firmly believe that defenders today possess ample access to tools, knowledge, and support to begin altering the economics of an attack, all of which represent a powerful countermeasure against adversaries.

---

[^1]: “MITRE ATT&CK Matrix for Enterprise,” MITRE, 2015–2023.
[^2]: Douglas Jose Pereira dos Santos, “2H 2022 Global Threat Landscape Report: Key Insights for CISOs,” Fortinet, March 3, 2023.
[^3]: “2H 2022 Global Threat Landscape Report,” Fortinet, March 3, 2023.
[^4]: Geri Revay, “The Year of the Wiper,” Fortinet, January 24, 2023.
[^5]: Derek Manky, “The Latest Intel on Wipers,” Fortinet, March 23, 2023.
[^6]: Douglas Jose Pereira dos Santos, “2H 2022 Global Threat Landscape Report: Key Insights for CISOs,” Fortinet, March 3, 2023.
[^7]: “Exploit Prediction Scoring System,” FIRST.org, 2015-2023.
[^8]: James Slaughter, Fred Gutierrez, and Shunichi Imano, “MOVEit Transfer Critical Vulnerability (CVE-2023-34362) Exploited as a 0-Day,” Fortinet, June 8, 2023.
[^9]: “Threat Signal Report: MOVEit Transfer Critical Vulnerability (CVE-2023-34362),” FortiGuard Labs, June 2, 2023.
[^10]: “EPSS API,” FIRST.org, 2015–2023.
[^11]: “Replication Through Removable Media,” MITRE ATT&CK, May 31, 2017.
[^12]: “IPS Threat Encyclopedia: Raspberry.Robin.Worm,” FortiGuard Labs, July 14, 2022.
[^13]: “Increased Truebot Activity Infects U.S. and Canada-Based Networks,” Cybersecurity and Infrastructure Security Agency, July 6, 2023.
[^14]: “Exploitation for Client Execution,” MITRE ATT&CK, April 18, 2018.
[^15]: Fortinet Follina Blog Posts, accessed July 27, 2023.
[^16]: “Hijack Execution Flow: DLL Side-Loading,” MITRE ATT&CK, March 13, 2020.
[^17]: FortiGuard Labs, “3CX Desktop App Compromised (CVE-2023-29059),” Fortinet, March 30, 2023.
[^18]: “Obfuscated Files or Information,” MITRE ATT&CK, May 31, 2017.
[^19]: “Masquerading,” MITRE ATT&CK, May 31, 2017.
[^20]: “Virtualization/Sandbox Evasion,” MITRE ATT&CK, April 17, 2019.
[^21]: “OS Credential Dumping,” MITRE ATT&CK, May 31, 2017.
[^22]: “Input Capture,” MITRE ATT&CK, May 31, 2017.
[^23]: “Process Injection,” MITRE ATT&CK, May 31, 2017.
[^24]: Derek Manky, “Partnering to Disrupt Cybercrime,” Fortinet, February 14, 2023.
[^25]: Douglas Jose Pereira dos Santos, “MITRE Attack Flow Gives CISOs Valuable Context for Better Risk Management,” Fortinet, November 3, 2022.
[^26]: Geri Revay and Hossein Jazi, “WINTAPIX: A New Kernel Driver Targeting Countries in the Middle East,” Fortinet, May 22, 2023.