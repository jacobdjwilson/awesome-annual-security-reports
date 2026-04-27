# 2H 2023 Global Threat Landscape Report
A Semiannual Report by FortiGuard Labs

## Table of Contents
- [Executive Summary](#executive-summary)
- [2H 2023 Active Threat Landscape at a Glance](#2h-2023-active-threat-landscape-at-a-glance)
- [A Look at Exploit, Malware, and Botnet Trends](#a-look-at-exploit-malware-and-botnet-trends)
- [Tracking movement across malware families](#tracking-movement-across-malware-families)
- [Into the Red Zone](#into-the-red-zone)
- [Most Active APTs](#most-active-apts)
- [Penetrating the Red Zone](#penetrating-the-red-zone)
- [From Exploit Prediction to Outbreak](#from-exploit-prediction-to-outbreak)
- [Ransomware Attacks Increasingly Target Critical Industries](#ransomware-attacks-increasingly-target-critical-industries)
- [Global ATT&CK Heatmap](#global-attck-heatmap)
- [Shedding Light on Dark Web Activity](#shedding-light-on-dark-web-activity)
- [Trends from the Trenches](#trends-from-the-trenches)
- [Conclusion](#conclusion)

---

## Executive Summary

In the second half of 2023, the cybersecurity landscape saw a range of significant developments that have considerably impacted the digital attack surface. Notable among these was the rise in sophisticated cyberattacks targeting large-scale entities and essential infrastructure.

If the growing number of attacks weren’t enough to keep most CISOs awake at night, the cybersecurity domain is simultaneously grappling with the ongoing challenge of attracting and retaining skilled professionals. The rising demand for qualified cybersecurity experts, coupled with the need for organizations to offer attractive career development opportunities and work environments, continues to highlight the importance of human capital in combating cyberthreats.

The need to understand where your attack surface gaps in detection, mitigation, and response lie is more vital than ever and the most impactful thing we can do is to shed light on how the threat landscape has been shifting and how organizations need to build secure networking systems that can quickly adapt to changing business demands and the evolving threat landscape. That’s why we publish this report. Our goal is to help you navigate these changes and understand where to focus your time and energy, using your resources in the most impactful way.

The findings in this report represent the collective intelligence of FortiGuard Labs, drawn from a vast array of network sensors collecting threat events each day observed in live production environments around the world from more than 600K+ environments and 10M+ sensors capturing every detail about threats that hit our detection technology. We’ve sifted through all that data to find and extract key insights that we hope will help guide you through the cyber challenges of 2024.

## 2H 2023 Active Threat Landscape at a Glance

![Infographic showing exploit dispersion, ATT&CK sightings, APT groups, ransomware statistics, and time-to-exploitation metrics.]

## A Look at Exploit, Malware, and Botnet Trends

FortiGuard Labs monitors a vast array of globally deployed sensors that collect trillions of threat events worldwide each day. This unique vantage point gives us a detailed and comprehensive view of the cyberthreat landscape, including how exploit, malware, and botnet trends change over time.

- **Exploits**: 11,030 unique exploit detections (+10% over last half); 63 exploit detections per organization (+17% over last half); 73% of firms saw severe attacks (+4% over last half).
- **Malware**: 39,896 unique variants detected (-11% from last half); 5,962 different active families (-16% from last half); 16 families spread to more than 10% of organizations (-11% from last half).
- **Botnet**: 319 unique botnets detected (-3% from last half); 4.3 active botnets per sensor (+/-0% from last half); 85 infection days in average (+2% over last half).

### IoT exploits are on the rise
Exploitation activity captured by the FortiGuard Intrusion Prevention System (IPS) sensors running on our FortiGate Next-Generation Firewalls provides unrivaled visibility into how threat actors find vulnerabilities, exploit their targets, and build malicious infrastructure.

![Chart showing technology platforms targeted most often with exploit attempts from July to December.]

## Tracking movement across malware families

Once threat actors find an exploitable vulnerability, their next step is often to deploy malware. Samples picked up by our various anti-malware solutions offer insight into popular adversary tools for establishing a foothold, escalating privileges, maintaining presence, and moving laterally within target environments to achieve their goals.

![Table showing top malware families based on regional prevalence across Africa, Asia, Europe, Latin America, Middle East, North America, and Oceania.]

## Into the Red Zone

Once infected with malware, systems often attempt to communicate with remote hosts to download additional payloads, establish command and control (C2) channels, and open backdoors into the environment. This makes the analysis of botnet traffic an important part of monitoring the full scope of malicious activity.

![Chart showing volume of traffic associated with new botnets emerging in 2H 2023: Prometei, DarkGate, and AndroxGh0st.]

## Most Active APTs

In the first half of the year, we observed significant activity among APT groups, and that volume has held steady throughout the remainder of 2023. 

![Infographic showing most active APT groups during 2H 2023 based on FortiRecon intelligence, including Lazarus Group, APT 28, APT 29, Andariel, OilRig, Kimsuky, MuddyWater, and APT37.]

## Penetrating the Red Zone

Prioritizing vulnerabilities for remediation is more important than ever given that the rate of discovery and disclosure continues to quicken. As of this report’s publication, there are over 222,000 vulnerabilities on the Common Vulnerabilities and Exposures (CVE) list.[^33] We witnessed a new record in 2023, with a total of 30,000 new vulnerabilities published—a 17% jump from the previous year.

![Chart showing red zone activity for all CVEs across all platforms.]

## From Exploit Prediction to Outbreak

As we’ve discussed previously, when it comes to vulnerabilities, what’s old is still new in the eyes of many attackers. To understand the prevalence of this trend, we identified all vulnerability exploits and malware samples that occurred in 2H 2023 along with the proportion of organizations registering detections.

![Charts showing age and prevalence of exploits and malware detected in 2H 2023.]

## Ransomware Attacks Increasingly Target Critical Industries

Ransomware continues to keep security teams up at night. According to a recent Fortinet survey, more than 80% of leaders are “very” or “extremely” concerned about ransomware.[^39] Across our sensors, ransomware detections surged 13x higher over the first half of 2023. That was followed by a 70% drop during the latter half of the year.

![Chart showing industries with the highest volume of ransomware and wiper detections.]

## Global ATT&CK Heatmap

MITRE ATT&CK is a widely used repository of adversary tactics, techniques, and procedures (TTPs).[^41] It offers a common language developed from real-world observations that are used by organizations and cybersecurity teams to build threat models and threat-informed defenses.

![Chart showing top ATT&CK techniques observed via sandbox solutions.]

## Shedding Light on Dark Web Activity

While much of our telemetry shows us what actions attackers have taken in the past, darknet intelligence can help us anticipate what adversaries may do next. For the first time in our threat landscape reports, we’re sharing insights we’ve collected from dark web forums, marketplaces, Telegram channels, and other sources during the second half of 2023.

## Trends from the Trenches

The FortiGuard Managed Detection and Response (MDR) team manages endpoint detection and response (EDR) instances on behalf of customers across the globe. Their daily responsibilities give the team a significant snapshot of adversary activities across business verticals and geopolitical regions.

- **Poorly scoped responses result in unforced errors**: Incomplete IR plans lead to knee-jerk reactions.
- **Failure to patch**: In 86% of cases investigated, the vulnerability was already known and a patch was available.
- **Backups**: Backups connected to production 24x7 are being targeted and encrypted by ransomware operators.
- **ESXi servers**: Increasingly targeted as they offer high impact on business continuity.

## Conclusion

We hope this edition of the Fortinet threat landscape report provides valuable insights to help you prioritize and implement appropriate security measures within your organization. 

[^1]: FortiGuard Labs Outbreak Alert: IoT Vulnerabilities, 2023.
[^2]: FortiGuard Labs Outbreak Alert: Zyxel Firewalls, 2023.
[^3]: CVE-2017-18368: Zyxel Router Vulnerability.
[^4]: Zerobot Malware Analysis, 2022.
[^5]: VMware Aria Operations for Networks Command Injection Vulnerability.
[^6]: IBM Aspera Faspex Code Execution Vulnerability.
[^7]: Cisco IOS XE Web UI Attack.
[^8]: Citrix Bleed Attack.
[^9]: Apache RocketMQ Remote Command Execution Vulnerability.
[^10]: Progress MOVEit Transfer SQL Injection Vulnerability.
[^11]: MITRE ATT&CK Framework, 2023.
[^12]: JS/Agent.CY!.tr.
[^13]: JS/Agent.F022!.tr.
[^14]: JS/Agent.PIV!.tr.
[^15]: JS/Agent.NDS!.tr.
[^16]: JS/ScrInject.B!.tr.
[^17]: RAT Activity Analysis, 2011-2023.
[^18]: JS/Cryxos.5478!.tr.
[^19]: CVE-2023-46604: Apache ActiveMQ Vulnerability.
[^20]: HelloKitty Ransomware Campaign, 2023.
[^21]: FortiGuard Labs Outbreak Alert: Apache ActiveMQ.
[^22]: CVE-2021-44228: Log4j Vulnerability.
[^23]: Agent Tesla Phishing Campaign, 2023.
[^24]: CVE-2017-11882: Microsoft Office Vulnerability.
[^25]: CVE-2018-0802: Microsoft Office Vulnerability.
[^26]: CVE-2017-9841: PHPUnit Vulnerability.
[^27]: CVE-2018-15133: Laravel Framework Vulnerability.
[^28]: CVE-2021-41773: Apache Web Server Vulnerability.
[^29]: Fortinet Telemetry on AndroxGh0st.
[^30]: Prometei IPS Signature Update, 2023.
[^31]: DarkGate Malware Market Analysis, 2023.
[^32]: Qakbot Takedown Analysis, 2023.
[^33]: Common Vulnerabilities and Exposures (CVE) List, 2023.
[^34]: Fortinet Red Zone Concept, 2022.
[^35]: CVE-2021-44228 Analysis.
[^36]: CVE-2023-44487.
[^37]: Exploit Prediction Scoring System (EPSS).
[^38]: CVE-2023-28121: WooCommerce Payments Plugin.
[^39]: Fortinet Ransomware Survey, 2023.
[^40]: Fortinet 2024 Threat Predictions Report.
[^41]: MITRE ATT&CK Repository.
[^42]: Fortinet 1H 2023 Threat Landscape Report.

---

that have existed for years, often remain on threat actors’ radar as active targets.

Unfortunately, this means you can’t be so focused on safeguarding against new vulnerabilities and attacks that you

neglect the old ones. Successful security teams need to protect against the entire exploitation life cycle, and this starts

with a proactive patching and updating program.

Critical industries are top ransomware targets. The actors behind ransomware campaigns have always been industrious.

Whether it’s making rapid adjustments to ransom demands based on cryptocurrency market dynamics or creating vast

criminal enterprises to minimize cost and maximize scale, they have a penchant for making things happen. That’s what

makes the ongoing shift to targeting critical industries all the more concerning. These OT-heavy environments are

particularly susceptible to costly outages, which greatly increases the pressure to pay high ransoms to restore productivity.

While each of us has a vital role to play in fighting against our collective adversaries, no single organization can single-

handedly halt threat actors. Shared intelligence is a crucial part of how we ensure timely and precise responses

when attackers strike. The more we collaborate across the public and private sectors, the more effective we can be at

disrupting cybercrime.

41

2H 2023 Global Threat Landscape ReportFootnotes

1

2

3

4

5

6

7

8

9

FortiGuard Outbreak Alerts, FortiGuard Labs, accessed February 18, 2024.

Zyxel Multiple Firewall Vulnerabilities, FortiGuard Outbreak Alerts, June 6, 2023.

Zyxel Router Command Injection Attack, FortiGuard Outbreak Alerts, August 9, 2023.

Zerobot Attack, FortiGuard Outbreak Alerts, December 27, 2022.

VMware Aria Operations for Networks Command Injection Vulnerability, FortiGuard Outbreak Alerts, June 22, 2023.

IBM Aspera Faspex Code Execution Vulnerability, FortiGuard Outbreak Alerts, March 1, 2023.

Cisco IOS XE Web UI Attack, FortiGuard Outbreak Alerts, October 20, 2023.

Citrix Bleed Attack, FortiGuard Outbreak Alerts, November 2, 2023.

Apache RocketMQ Remote Command Execution Vulnerability, FortiGuard Outbreak Alerts, July 5, 2023.

10

Progress MOVEit Transfer SQL Injection Vulnerability, FortiGuard Outbreak Alerts, June 5, 2023.

11  MITRE ATT&CK, accessed February 18, 2024.

12

13

14

15

16

17

18

JS/Agent.CY!tr, FortiGuard Labs Encyclopedia, June 9, 2022.

JS/Agent.F022!tr, FortiGuard Labs Encyclopedia, July 10, 2023.

JS/Agent.PIV!tr, FortiGuard Labs Encyclopedia, November 1, 2021.

JS/Agent.NDS!tr, FortiGuard Labs Encyclopedia, November 7, 2023.

JS/ScrInject.B!tr, FortiGuard Labs Encyclopedia, August 30, 2011.

Ibid.

JS/Cryxos.5478!tr, FortiGuard Labs Encyclopedia, March 30, 2021.

19  CVE-2023-46604, NIST National Vulnerability Database, accessed February 18, 2024.

20

21

22

Lucian Constantin, HelloKitty Ransomware Deployed Via Critical Apache Active MQ Flaw, CSO Online, November 2, 2023.

Apache ActiveMQ Ransomware Attack, FortiGuard Outbreak Alerts, November 6, 2023.

Lazarus RAT Attack, FortiGuard Outbreak Alerts, December 12, 2023.

23  Agent Tesla Malware Attack, FortiGuard Outbreak Alerts, September 7, 2023.

24  CVE-2017-11882, NIST National Vulnerability Database, accessed February 18, 2024.

25  CVE-2018-0802, NIST National Vulnerability Database, accessed February 18, 2024.

26  CVE-2017-9841, NIST National Vulnerability Database, accessed February 18, 2024.

27  CVE-2018-15133, NIST National Vulnerability Database, accessed February 18, 2024.

28  CVE-2021-41773, NIST National Vulnerability Database, accessed February 18, 2024.

29  Cedric Pernet, Androxgh0st Malware Botnet Steals AWS, Microsoft Credentials and More, TechRepublic, January 18, 2024.

30  Ravie Lakshmanan, New Version of Prometei Botnet Infects Over 10,000 Systems Worldwide, The Hacker News, March 10, 2023.

31

The Underground Economist: Volume 3, Issue 12, ZeroFox, June 27, 2023.

32  Kevin Poireault, DarkGate and PikaBot Activity Surge in the Wake of QakBot Takedown, Infosecurity Magazine, November 21, 2023.

33  Common Vulnerabilities and Exposures index, MITRE, accessed February 18, 2024.

34  Douglas Jose Pereira dos Santos, 2H 2022 Global Threat Landscape Report: Key Insights for CISOs, Fortinet, March 3, 2023.

35  CVE-2021-44228, NIST National Vulnerability Database, accessed February 18, 2024.

36  CVE-2023-44487, NIST National Vulnerability Database, accessed February 18, 2024.

37

Exploit Prediction Scoring System, Forum of Incident Response and Security Teams, accessed February 18, 2024.

38  CVE-2023-28121, NIST National Vulnerability Database, accessed February 18, 2024.

39  The 2023 Global Ransomware Report, Fortinet, April 20, 2023.

40  Ransomware Extortion Skyrockets in 2023, Reaching $449.1M and Counting, The Hacker News, July 12, 2023.

41  MITRE ATT&CK, accessed February 18, 2024.

42

FortiGuard Labs 1H 2023 Threat Landscape Report, Fortinet, August 7, 2023.

42

2H 2023 Global Threat Landscape ReportCopyright © 2024 Fortinet, Inc. All rights reserved. Fortinet ® , FortiGate® , FortiCare® and FortiGuard®, and certain other marks are registered trademarks of Fortinet, Inc., and other Fortinet names herein may also be registered and/or common

law trademarks of Fortinet. All other product or company names may be trademarks of their respective owners. Performance and other metrics contained herein were attained in internal lab tests under ideal conditions, and actual performance

and other results may vary. Network variables, different network environments and other conditions may affect performance results. Nothing herein represents any binding commitment by Fortinet, and Fortinet disclaims all warranties, whether

express or implied, except to the extent Fortinet enters a binding written contract, signed by Fortinet’s General Counsel, with a purchaser that expressly warrants that the identified product will perform according to certain expressly-identified

performance metrics and, in such event, only the specific performance metrics expressly identified in such binding written contract shall be binding on Fortinet. For absolute clarity, any such warranty will be limited to performance in the same

ideal conditions as in Fortinet’s internal lab tests. Fortinet disclaims in full any covenants, representations, and guarantees pursuant hereto, whether express or implied. Fortinet reserves the right to change, modify, transfer, or otherwise revise

this publication without notice, and the most current version of the publication shall be applicable.

Copyright © 2024 Fortinet, Inc. All rights reserved. May 2, 2024 8:56 am    2564222-0-0-EN

www.fortinet.com