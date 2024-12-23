# A Semiannual Report by FortiGuard Labs
## Global Threat Landscape Report
### 2H 2023

## Table of Contents
- [Executive Summary](#executive-summary)
- [2H 2023 Active Threat Landscape at a Glance](#2h-2023-active-threat-landscape-at-a-glance)
- [A Look at Exploit, Malware, and Botnet Trends](#a-look-at-exploit-malware-and-botnet-trends)
- [Tracking movement across malware families](#tracking-movement-across-malware-families)
- [New bots on the block: AndroxGh0st, Prometei, and DarkGate](#new-bots-on-the-block-androxgh0st-prometei-and-darkgate)
- [Most Active APTs](#most-active-apts)
- [Penetrating the Red Zone](#penetrating-the-red-zone)
- [From Exploit Prediction to Outbreak](#from-exploit-prediction-to-outbreak)
- [Ransomware Attacks Increasingly Target Critical Industries](#ransomware-attacks-increasingly-target-critical-industries)
- [Global ATT&CK Heatmap](#global-attck-heatmap)
- [Shedding Light on Dark Web Activity](#shedding-light-on-dark-web-activity)
- [Trends from the Trenches](#trends-from-the-trenches)
- [Conclusion](#conclusion)
- [Footnotes](#footnotes)

## Executive Summary
In the second half of 2023, the cybersecurity landscape saw a range of significant developments that have considerably impacted the digital attack surface. Notable among these was the rise in sophisticated cyberattacks targeting large-scale entities and essential infrastructure.

If the growing number of attacks weren’t enough to keep most CISOs awake at night, the cybersecurity domain is simultaneously grappling with the ongoing challenge of attracting and retaining skilled professionals. The rising demand for qualified cybersecurity experts, coupled with the need for organizations to offer attractive career development opportunities and work environments, continues to highlight the importance of human capital in combating cyberthreats.
The need to understand where your attack surface gaps in detection, mitigation, and response lie is more vital than ever and the most impactful thing we can do is to shed light on how the threat landscape has been shifting and how organizations need to build secure networking systems that can quickly adapt to changing business demands and the evolving threat landscape. That’s why we publish this report. Our goal is to help you navigate these changes and understand where to focus your time and energy, using your resources in the most impactful way.
The findings in this report represent the collective intelligence of FortiGuard Labs, drawn from a vast array of network sensors collecting threat events each day observed in live production environments around the world from more than 600K+ environments and 10M+ sensors capturing every detail about threats that hit our detection technology. We’ve sifted through all that data to find and extract key insights that we hope will help guide you through the cyber challenges of 2024.

## 2H 2023 Active Threat Landscape at a Glance
![Image description: A graphic showing key statistics for the 2H 2023 threat landscape. It includes percentages for endpoint vulnerabilities targeted, organizations detecting exploits less than a month old, MITRE ATT&CK techniques observed, active APT groups, ransomware targeting the industrial sector, and time-to-exploitation.]
- 8.8% +0.5% since last half
  The percent of all endpoint vulnerabilities targeted by attacks remained steady, around 9%.
- 41%
  Attacks can spread quickly. 41% of organizations detected activity for exploits less than one month old.
- 91.2%
  Sandbox and network detection and response (NDR) sensors observed activity for over two-thirds of MITRE ATT&CK techniques.
- 67.1%
  Into the Red Zone
- 32.9%
  Exploit Dispersion
- 59%
  ATT&CK Sightings
- 38/143
  FortiRecon intelligence indicates 38 of the 143 advanced persistent threat (APT) groups listed by MITRE were active during this time.
- 40%+
  More than 40% of ransomware and wipers targeted the industrial sector, indicating that cybercriminals are focused on OT and the supply chain.
- 43%
  On average, for new exploits identified, attacks occurred in 4.76 days after discovery. That’s 43% faster than the prior period.
- Orgs seeing exploits <1 month old +0.4% since last half
- APT Groups
- Ransomware
- Time-to-Exploitation

## A Look at Exploit, Malware, and Botnet Trends
FortiGuard Labs monitors a vast array of globally deployed sensors that collect trillions of threat events worldwide each day. This unique vantage point gives us a detailed and comprehensive view of the cyberthreat landscape, including how exploit, malware, and botnet trends change over time.

This data, outlined in the chart above, shows that the creation and prevalence of exploits are on the rise. Cybercriminals are targeting the ever-increasing number of new vulnerabilities resulting from the exponential growth in the number and variety of connected devices and an explosion in new applications and online services. It’s only natural that attacks looking to exploit those vulnerabilities would rise as well. This increase in exploit volume per organization is undoubtedly contributing to the prevalence of overwhelmed security teams.
Interestingly, after rising over the first half of 2023, the volume of malware samples detected by our sensors subsided in the latter half of the year. Unfortunately for defenders, this doesn’t mean that malware is falling out of favor among clever attackers. The observed slowdown is likely because certain types of malware, particularly ransomware, are taking a more targeted approach, leading to an increase in cost-per-ransomware incident. This also explains why bot traffic remained steady during this same time.
IoT exploits are on the rise
Exploitation activity captured by the FortiGuard Intrusion Prevention System (IPS) sensors running on our FortiGate Next-Generation Firewalls provides unrivaled visibility into how threat actors find vulnerabilities, exploit their targets, and build malicious infrastructure. These sensors are often the first point of contact with an adversary probing for exposures. Let’s start with a view of the technologies attackers are probing most aggressively. Not surprisingly, Internet-of-Things (IoT) devices, shown in red in the corresponding chart, are popular targets, largely because they are often under protected or unprotected.
- Exploits
  - 11,030 unique exploit detections, +10% over last half
  - 63 exploit detections per organization, +17% over last half
  - 73% of firms saw severe attacks, +4% over last half
- Malware
  - 39,896 unique variants detected, -11% from last half
  - 5,962 different active families, -16% from last half
  - 16 families spread to more than 10% of organizations, -11% from last half
- Botnet
  - 319 unique botnets detected, -3% from last half
  - 4.3 active botnets per sensor, +/-0% from last half
  - 85 infection days in average, +2% over last half

Vulnerabilities affecting routers, cameras, and other IoT devices were the focus of several outbreak alerts published by FortiGuard Labs throughout 2023.[^1]
Zyxel Networks equipment was a favorite target for exploits throughout the second half of the year, with FortiGuard Labs issuing an outbreak alert about the company’s firewalls.[^2] Perhaps smelling blood in the water, attackers rediscovered and exploited a Zyxel Networks vulnerability relating to an end-of-life router, which was initially published in 2017.[^3]
Speaking of old vulnerabilities attracting new attention, exploits targeting Zivif web cameras (CVE-2017-17107) made the top 10 list in December 2023. These exploits appear to be related to ongoing Zerobot attacks we alerted security practitioners to in late 2022.[^4] This scenario shows that old vulnerabilities can always be made new (and better) by enterprising threat actors.
![Image description: A table showing the technology platforms targeted most often with exploit attempts, broken down by month from July to December.]
While we have highlighted outbreak alerts for IoT devices here, our FortiGuard Labs team had their radars filled with all manner of additional vulnerability exploits in 2H 2023. Here’s a quick recap of some of those:
- VMware Aria Operations for Networks Command Injection Vulnerability[^5]
- IBM Aspera Faspex Code Execution Vulnerability[^6]
- Cisco IOS XE Web UI Attack[^7]
- Citrix Bleed Attack[^8]
- Apache RocketMQ Remote Command Execution Vulnerability[^9]
- Progress MOVEit Transfer SQL Injection Vulnerability[^10]

We are closing out this exploit review with another chart demonstrating the wide scope of activity detected by our IPS sensors. Here is a look at the top five exploit detections associated with four key MITRE ATT&CK techniques[^11] of Active Scanning, Exploit Public-Facing Apps, Brute Force, and Network DoS.
![Image description: A chart showing the top five exploit detections associated with four key MITRE ATT&CK techniques: Active Scanning, Exploit Public-Facing Application, Brute Force, and Network Denial-of-Service.]
- Active Scanning (T1595)
  - 53% SIPVicious.SIP.Scanner
  - 42% DNS.PTR.Records.Scan
  - 2.0% Qualys.Vulnerability.Scanner
  - 0.85% Port.Scanner
  - 0.73% Nessus.Scanner
- Exploit Public-Facing Application (T1190)
  - 63% HTTP.Suspicious.Headers.With.Special.Characters
  - 7.4% MS.SMB.Server.Trans.Peeking.Data.Information.Disclosure
  - 6.2% SSL.Anonymous.Ciphers.Negotiation
  - 3.0% Modbus.TCP.Unauthorized.Read.Request.PLC
  - 3.0% Apache.Log4j.Error.Log.Remote.Code.Execution
- Brute Force (T1110)
  - 35% SSH.Connection.Brute.Force
  - 22% SMB.Login.Brute.Force
  - 17% MS.RDP.Connection.Brute.Force
  - 11% MySQL.Login.Brute.Force
  - 6.1% SIP.Register.Brute.Force
- Network Denial-of-Service (T1498)
  - 64% NTP.Monlist.Command/DoS
  - 15% IP.Land
  - 11% BlackNurse.ICMP.Type.3.Code.3.Flood.Dos
  - 2.4% Memcached.UDP.Amplification.Detection
  - 1.8% DNS.Amplificatioj.Detection
Most prevalent recon and initial access detections associated with MITRE ATT&CK techniques

Network security appliances provide intelligence on the left side of the MITRE ATT&CK framework, which helps us understand more about the threats that malicious actors are using to try to get inside organizations. Ideally, when applying the ATT&CK framework across your enterprise, we recommend collating ATT&CK sources and creating a consolidated heatmap for using in threat hunting, purple teaming, adversarial emulation, and detection engineering.

## Tracking movement across malware families
Once threat actors find an exploitable vulnerability, their next step is often to deploy malware. Samples picked up by our various anti-malware solutions offer insight into popular adversary tools for establishing a foothold, escalating privileges, maintaining presence, and moving laterally within target environments to achieve their goals.
The figure on the next page measures the proportion of organizations in each region that detected variants of the most common malware families during the second half of the year. Malware that gains a foothold in one region of the world, such as the JS/Agent family, gains similar traction across most other geographies.
![Image description: A chart showing the top malware families based on regional prevalence across Africa, Asia, Europe, Latin America, Middle East, North America, and Oceania.]
- 40.9% JS/Agent
- 17.6% JS/Phishing
- 17.4% MSIL/Kryptik
- 16.5% HTML/Phish
- 13.1% JS/ScrInject
- 28.6% JS/Cryxos
- 20.8% MSIL/GenKryptik
- 12.8% PDF/Phishing
- 19.1% MSIL/GenericKDS
- 13.1% HTML/Phishing
- 16.1% MSIL/Agent
- 15.0% MSOffice/CVE_2018_0798
- 7.7% JS/Redirector
- 14.6% MSIL/Stealer
- 13.4% NSIS/Injector
- 12.1% MSOffice/CVE_2017_11882
- 11.8% HTML/infObfus
- 9.1% BAT/Agent
- 11/9% W32/Injector
- 12/3% MSExcel/CVE_2017_11882

However, two malware families have bucked the regional uniformity trend: JS/ScrInject and JS/Cryxos. For the former, the variant responsible is JS/ScrInject.B!.tr.[^16] This Remote Access Trojan (RAT) has been circulating since 2011 and has a very regular weekly activity cycle.[^17] The other is JS/Cryxos and, in particular, the JS/Cryxos.5478!.tr variant.[^18] This Trojan, known to have a variety of surreptitious capabilities, appears to be driving the bulk of detections across Asia.
Outside the most prevalent generic families depicted above, four additional malware campaigns caught our attention in the second half of 2023: AndroxGh0st, Apache ActiveMQ ransomware, Lazarus RATs, and Agent Tesla. We cover AndroxGh0st extensively in the botnet section, so we’ll summarize the other three here.
- Apache ActiveMQ
  Apache ActiveMQ is a popular open-source message broker. A vulnerability was disclosed (CVE-2023-46604) in fall 2023 that allowed a remote attacker with network access to a broker to run arbitrary shell commands by manipulating serialized class types in the OpenWire protocol.[^19] Reports emerged in November that attackers were taking advantage of that flaw in the form of the HelloKitty ransomware.[^20] FortiGuard Labs released an outbreak alert detailing how threat actors were exploiting this flaw by running ransomware campaigns targeting servers running outdated and vulnerable versions of Apache ActiveMQ.[^21]
- Lazarus RATs
  The Lazarus Group is an APT group sponsored by the North Korean government. In this new campaign, Lazarus was observed employing DLang-based RAT malware in the wild. Lazarus’s initial access begins with the successful exploitation of CVE-2021-44228, the infamous Log4j vulnerability discovered in 2021.[^22]
- Agent Tesla
  FortiGuard Labs captured a phishing campaign that spreads a new Agent Tesla variant.[^23] This well-known malware family uses a .Net-based RAT and data stealer to gain initial access by exploiting Microsoft Office vulnerabilities CVE-2017-11882 and CVE-2018-0802.[^24] [^25] The Agent Tesla core module can collect sensitive information from the victim’s device such as saved credentials, keylogging information, and device screenshots.

In case you’d like to double-check your antivirus scans for the most common JS/Agent variants, here are the top three to look for, plus a final variant that moved up the popularity ranks quickly in 2H 2023:
- JS/Agent.CY!.tr[^12]
- JS/Agent.F022!.tr[^13]
- JS/Agent.PIV!.tr[^14]
- JS/Agent.NDS!.tr[^15]

## New bots on the block: AndroxGh0st, Prometei, and DarkGate
Once infected with malware, systems often attempt to communicate with remote hosts to download additional payloads, establish command and control (C2) channels, and open backdoors into the environment. This makes the analysis of botnet traffic an important part of monitoring the full scope of malicious activity.
A chart of the most active botnets is inevitably filled with many of the same ones we’ve seen for years, including Gh0st, Mirai, and ZeroAccess. This demonstrates two things:
- Botnets are resilient. They’re created to persist and, despite coordinated law enforcement takedowns, can be hard to kill.
- Botnet remediation is a slow process. Much of the botnet traffic we detect comes from infected systems attempting to communicate with botnets that are no longer active.
That said, new botnets do emerge occasionally that warrant attention. In the second half of 2023, three new botnets took the spotlight: AndroxGh0st, Prometei, and DarkGate.
- 14.6% New botnets
- 85.4% Old versus new bots
- 15% of volume Into the Red Zone
![Image description: A chart showing the volume of traffic associated with new botnets emerging in 2H 2023, including Prometei, DarkGate, and AndroxGh0st.Malware, broken down by month from July to December.]

- AndroxGh0st
  The AndroxGh0st botnet is related to the Python-based malware of the same name. It primarily targets user environment (.env) files, which often contain credentials for a variety of high-profile applications. AndroxGh0st includes numerous malicious functions to abuse Simple Mail Transfer Protocols (SMTP). It also scans and exploits exposed credentials and APIs and deploys web shells to maintain persistent access to systems.
  We continue to observe widespread activity of AndroxGh0st malware in the wild exploiting multiple vulnerabilities. It specifically targets the PHPUnit (CVE-2017-9841), Laravel Framework (CVE-2018-15133), and Apache Web Server (CVE-2021-41773) vulnerabilities to spread and conduct information-gathering attacks on the target networks.[^26] [^27] [^28] Fortinet was credited with exposing telemetry on AndroxGh0st, showing over 40,000 devices infected by the botnet.[^29]
- Prometei
  Prometei is malware that can remotely control infected machines. It’s capable of spreading laterally across networks, stealing password credentials, executing arbitrary commands, and downloading and executing additional malicious components. Prometei can also perform cryptocurrency mining and has self-updating capabilities.
  This malware strain was recently reinvented, and we created new IPS signatures to aid in detection.[^30] This retooling worked well, as the Prometei botnet has subsequently been catapulted to the sixth spot on our list for total traffic volume across our sensors in 2H 2023.
- DarkGate
  Though it’s a distant third to AndroxGh0st and Prometei, the DarkGate botnet warrants mention. The DarkGate malware, which has a range of capabilities from remote access to cryptomining to information stealing, was first reported in 2017. Since then, its creators have used it only for specific campaigns. But in mid-2023, the purported author offered to sell it, and the malware soon began making wider rounds.[^31] We saw the DarkGate botnet emerge after the Qakbot takedown as a possible successor.[^32] Whether DarkGate has a future as a leading tool for cybercriminals remains to be seen.

## Most Active APTs
In the first half of the year, we observed significant activity among APT groups, and that volume has held steady throughout the remainder of 2023. APT groups continue to be highly adaptable to changes in the digital landscape and are increasingly stealthy as they carefully plan and execute attacks. The image below offers a look at the most active APT groups during the second half of the year.
![Image description: A graphic showing the most active APT groups during 2H 2023 based on FortiRecon intelligence. It includes APT 28, Lazarus Group, Kimsuky, APT 29, OilRig, and APT37.]
- Most active APT groups during 2H 2023 based on FortiRecon intelligence
  - APT 28 Government
  - Actor: Lazarus Group Top Target(s): Technology
  - Kimsuky Government
  - APT 29 Government
  - Andariel Technology
  - OilRig Government, Healthcare
  - Andariel Technology
  - OilRig Government, Healthcare
  - MuddyWater Telecom
  - APT37 Aerospace Defense, Civil Society, and Manufacturing

Researchers’ latest findings indicate a definitive shift in the tactics of the North Korean APT group, Lazarus. Over the past year and a half, they have disclosed three different RATs built using uncommon technologies during development, like QtFramework, PowerBasic, and DLang. This indicates that Lazarus Group is a mature and capable organization, generally using N-Day exploits and known techniques to breach companies in the technology sector, such as blockchain exchanges and software development firms. The group’s attacks have been quite lucrative, netting north of $100 million in crypto thefts alone.
Another group that was active these last months of 2023 was APT 28, using N-Day vulnerabilities in Outlook and Winrar to steal New Technology Lan Manager (NTLM) credentials, focusing on breaching government organizations as well as companies in the higher education, manufacturing, and aerospace industries. The group targeted organizations in Eastern Europe, with multiple campaigns aimed at disrupting operations and stealing information from these enterprises. This same group also used previously undisclosed zero days this year to carry on cyberespionage and steal data. APT 28 has also moved away from using backdoors and compromising peripheral devices in the network and is now using legitimate services such as Google Drive and Microsoft OneDrive to exfiltrate sensitive data.

## Penetrating the Red Zone
Prioritizing vulnerabilities for remediation is more important than ever given that the rate of discovery and disclosure continues to quicken. As of this report’s publication, there are over 222,000 vulnerabilities on the Common Vulnerabilities and Exposures (CVE) list.[^33] We witnessed a new record in 2023, with a total of 30,000 new vulnerabilities published—a 17% jump from the previous year.
In 2022, we introduced the concept of the “red zone,” which helps readers better understand how likely (or unlikely) it is that threat actors will exploit a specific vulnerability.[^34] This allows security teams to focus on the vulnerabilities that present the most risk by prioritizing remediation efforts.
Thankfully, our data shows a small subset (12.5%) of all historical CVEs are present and unremediated on endpoints in live environments. This is depicted in the ratio of blue versus gray squares in the adjacent chart.
Further, only a fraction (<1%) of all vulnerabilities were exploited in 2H 2023. That proportion has remained remarkably steady over time, which is good news for security teams.
- 30K new vulnerabilities across all industries were published in 2023, marking a 17% increase from the prior year.
![Image description: A chart showing red zone activity for all CVEs across all platforms, indicating the proportion of CVEs that are absent, present, and attacked.]
- About 0.7% of all CVEs observed on endpoints and under attack
- Absent
- Present
- Attacked
- 1.6K

Of course, the red zone for many prominent software platforms is substantially larger. For example, Microsoft’s attack surface is 20x larger than the overall average (14%) and twice that of Apple (7%) and Linux (5%). Practically speaking, the larger the red zone, the more effort and automated patching is required for timely remediation of high-risk vulnerabilities with active exploits.
![Image description: A chart showing red zone activity for CVEs affecting prominent platforms, including Microsoft, Adobe, Apple, Linux, Oracle, and Google.]
- Microsoft (14.2%)
- Adobe (13.6%)
- Apple (7.1%)
- Linux (5.3%)
- Oracle (3.6%)
- Google (2.6%)
- Absent
- Present
- Attacked

Here is a look at the top five vulnerabilities that comprise each platform’s red zone based on the prevalence of detected exploit attempts:
![Image description: A chart showing the CVEs with the highest exploit activity for each prominent software platform, including Microsoft, Oracle, Linux, Google, Apple, and Adobe.]
- CVEs with the highest exploit activity for each prominent software platform
  - Microsoft
    - CVE-2017-0147
    - CVE-2016-3212
    - CVE-2017-0068
    - CVE-2021-31207
    - CVE-2022-24463
    - 0.9%
    - 0.9%
    - 0.9%
    - 0.9%
    - 0.9%
    - 5%
    - 0.4%
    - 88%
    - 99%
  - Oracle
    - CVE-2019-0948
    - CVE-2019-0537
    - CVE-2016-3427
    - CVE-2012-5081
    - CVE-2013-2416
    - 0.08%
    - 0.1%
    - 0.6%
  - Linux
    - CVE-2013-2461
    - CVE-2015-2590
    - CVE-2021-44228
    - CVE-2014-0160
    - CVE-2016-1000110
    - 0.1%
    - 0.2%
    - 0.2%
  - Google
    - CVE-2015-2331
    - CVE-2014-0224
    - CVE-2013-2912
    - CVE-2021-30632
    - CVE-202130538
    - 8%
    - 9%
    - 9%
    - 12%
    - 21%
  - Apple
    - CVE-2019-13720
    - CVE-2020-15994
    - CVE-2018-4443
    - CVE-2017-13798
    - CVE-2018-4312
    - 8%
    - 8%
    - 16%
    - 16%
    - 16%
  - Adobe
    - CVE-2020-9802
    - CVE-2018-4386
    - CVE-2017-16391
    - CVE-2008-2992
    - CVE-2023-26397
    - 3%
    - 3%
    - 5%
    - 35%
    - 6%
    - 33%
    - 65%

The share of red zone activity across vulnerabilities differs dramatically among platforms. A full 99% of Linux’s red zone is dominated by exploits targeting CVE-2021-44228.[^35] Compare that to Apple, where the top three vulnerabilities each account for approximately 16% of exploit activity.
Most of these red zone vulnerabilities aren’t new. Only two were published in 2023, and just one of those emerged in the second half of the year (CVE-2023-44487).[^36] The rest span the last decade. And keep in mind that the exploitation “old” vulnerabilities isn’t slowing—the top vulnerability for half the platforms listed was discovered at least five years prior.

## From Exploit Prediction to Outbreak
As we’ve discussed previously, when it comes to vulnerabilities, what’s old is still new in the eyes of many attackers. To understand the prevalence of this trend, we identified all vulnerability exploits and malware samples that occurred in 2H 2023 along with the proportion of organizations registering detections. We then charted those signatures according to when they were created and added to Fortinet devices. The charts on the next page measure the active lifespan of exploit and malware threats.
![Image description: A chart showing the age and prevalence of exploits detected in 2H 2023, with the x-axis representing the age of the triggered signature and the y-axis representing the percent of organizations targeted monthly.]
![Image description: A chart showing the age and prevalence of malware detected in 2H 2023, with the x-axis representing the age of the triggered signature and the y-axis representing the percent of organizations targeted monthly.]
- Percent of Orgs Targeted Monthly
  - 2
  - 4
  - 6
  - 8
  - 10
  - 12
  - 14
  - 16
  - 18
  - 0%
  - 10%
  - 20%
  - 30%
  - 40%
  - 20
  - 0
  - 50%
  - 40.9% of orgs reported exploitation activity <1 month
  - 47.3% of orgs reported exploitation activity 2 months to 1 year
  - IPS Detections
  - Age of Triggered Signature
  - 97.6% of orgs reported exploitation activity 5+ years
- Percent of Orgs Targeted Monthly
  - 0
  - 0%
  - 10%
  - 20%
  - 2
  - 4
  - 6
  - 8
  - 10
  - 12
  - 14
  - 16
  - 18
  - 20
  - 22
  - 24
  - 26
  - 28
  - 30%
  - 40.5% of orgs reported virus activity <1 month
  - 38.7% of orgs reported virus activity 2 months to 1 year
  - Malware Detections
  - Age of Triggered Signature
  - 53.8% of orgs reported virus activity 5+ years

We continue to observe threat actors exploiting vulnerabilities more than 15 years old. Nearly all organizations (98%) have detected exploits that have existed for at least five years. Yet there’s plenty of room for new threats to make their way onto the scene: 41% of organizations also detected exploits from signatures less than one month old. But when it comes to malware, just over half of organizations have detected variants that have been around for five or more years—much less than what we see for exploits.
This analysis yields some critical insights into the cyberthreat landscape. Exploits and malware have very similar speeds and scopes related to their spread, but the longevity of each differs. Malware variants die off more quickly as new code replaces the old. Exploits show a much longer active lifespan because the vulnerabilities cybercriminals target can remain unpatched for years.
Practically speaking, this reinforces the importance of remaining vigilant about security hygiene, as attackers aren’t likely to stop exploiting older vulnerabilities. It’s also a great reminder to security practitioners to act quickly through a consistent patching and updating program when new vulnerabilities emerge that are likely to be exploited.
How can you track emerging vulnerabilities that are most likely to be attacked? The Exploit Prediction Scoring System (EPSS) exists for this exact purpose.[^37] Fortinet is a major contributor to the exploitation data that drives EPSS. The chart below shows the vulnerabilities released in 202 that were most targeted by exploit activity in the latter half of the year.
![Image description: A chart showing the most widely exploited CVEs published in 2023 with EPSS score, including CVE-2023-1389, CVE-2023-23752, CVE-2023-27350, CVE-2023-28121, CVE-2023-32315, CVE-2023-20887, CVE-2023-34133, CVE-2023-23489, CVE-2023-26347/CVE-2023-38205, and CVE-2023-2732.]
- Most widely exploited CVEs published in 2023 with EPSS score
  - Prevalence
  - EPSS Ranking
  - 0%
  - 5%
  - 10%
  - 15%
  - 20%
  - 25%
  - Top 10 Actively Exploited CVEs: 2023
    - CVE-2023-1389 (TP-Link) Top 7.2%
    - CVE-2023-23752 (Joomla) Top 2.3%
    - CVE-2023-27350 (PaperCut) Top 0.2%
    - CVE-2023-28121 (WordPress/WooCommerce) Top 2.1%
    - CVE-2023-32315 (OpenFire) Top 0.6%
    - CVE-2023-20887 (VMWare Aria) Top 0.6%
    - CVE-2023-34133 (SonicWall) Top 72.9%
    - CVE-2023-23489 (WordPress/EasyDigital) Top 5.0%
    - CVE-2023-26347/CVE-2023-38205 (Adobe ColdFusion) Top 1.8%
    - CVE-2023-2732 (WordPress/MStore) Top 25.7%
    - Top 4.2%

- 98% of organizations have detected exploits that have been in existence for at least five years.

Let’s take a closer look at just how accurate EPSS is in identifying vulnerabilities that are likely to be exploited. The chart below highlights EPSS scoring for the vulnerability affecting the WooCommerce Payments plugin for WordPress (CVE-2023-28121).[^38] This CVE was published on April 12, 2023, and was initially assessed by EPSS as having a low probability of exploitation. That assessment was revised dramatically after a Nuclei template and Metasploit module were released in early July. Given these changes, the vulnerability rose to the top 3% of EPSS scores with a 71% chance of exploitation in the next 30 days.
Shortly after this revision of EPSS, our team observed the first signs of exploitation in the wild on July 19. In this case, EPSS provided an effective early warning system prior to the outbreak of attacks, giving defenders a valuable head start on remediation.
![Image description: A chart showing the evolution of EPSS and the exploitation of the WooCommerce vulnerability, with the x-axis representing time from April to January and the y-axis representing EPSS probability and exploitation prevalence.]
- Evolution of EPSS and the exploitation of the WooCommerce vulnerability
  - Daily Published Value
  - EPSS Probability
  - Exploitation Prevalence
  - 