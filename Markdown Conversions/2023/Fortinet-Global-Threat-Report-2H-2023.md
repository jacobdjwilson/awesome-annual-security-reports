# 2H 2023 Global Threat Landscape Report

## Table of Contents
- [Executive Summary](#executive-summary)
- [Active Threat Landscape at a Glance](#active-threat-landscape-at-a-glance)
- [A Look at Exploit, Malware, and Botnet Trends](#a-look-at-exploit-malware-and-botnet-trends)
- [Most Active APTs](#most-active-apts)
- [Penetrating the Red Zone](#penetrating-the-red-zone)
- [From Exploit Prediction to Outbreak](#from-exploit-prediction-to-outbreak)
- [Ransomware Attacks Increasingly Target Critical Industries](#ransomware-attacks-increasingly-target-critical-industries)
- [Global ATT&CK Heatmap](#global-attck-heatmap)
- [Shedding Light on Dark Web Activity](#shedding-light-on-dark-web-activity)
- [Trends from the Trenches](#trends-from-the-trenches)
- [Conclusion](#conclusion)
- [Footnotes](#footnotes)

# 2H 2023

## Global Threat Landscape Report
A Semiannual Report by FortiGuard Labs

In the second half of 2023, the cybersecurity landscape saw a range of significant developments that have considerably impacted the digital attack surface. Notable among these was the rise in sophisticated cyberattacks targeting large-scale entities and essential infrastructure.

If the growing number of attacks weren’t enough to keep most CISOs awake at night, the cybersecurity domain is simultaneously grappling with the ongoing challenge of attracting and retaining skilled professionals. The rising demand for qualified cybersecurity experts, coupled with the need for organizations to offer attractive career development opportunities and work environments, continues to highlight the importance of human capital in combating cyberthreats.

The need to understand where your attack surface gaps in detection, mitigation, and response lie is more vital than ever and the most impactful thing we can do is to shed light on how the threat landscape has been shifting and how organizations need to build secure networking systems that can quickly adapt to changing business demands and the evolving threat landscape. That’s why we publish this report. Our goal is to help you navigate these changes and understand where to focus your time and energy, using your resources in the most impactful way.

The findings in this report represent the collective intelligence of FortiGuard Labs, drawn from a vast array of network sensors collecting threat events each day observed in live production environments around the world from more than 600K+ environments and 10M+ sensors capturing every detail about threats that hit our detection technology. We’ve sifted through all that data to find and extract key insights that we hope will help guide you through the cyber challenges of 2024.

## Executive Summary

### Active Threat Landscape at a Glance

#### Into the Red Zone
- **Exploit Dispersion**: 41% of organizations detected activity for exploits less than one month old.
- **ATT&CK Sightings**: Sandbox and network detection and response (NDR) sensors observed activity for over two-thirds of MITRE ATT&CK techniques.

#### APT Groups
- FortiRecon intelligence indicates 38 of the 143 advanced persistent threat (APT) groups listed by MITRE were active during this time.

#### Ransomware
- More than 40% of ransomware and wipers targeted the industrial sector, indicating that cybercriminals are focused on OT and the supply chain.

#### Time-to-Exploitation
- On average, for new exploits identified, attacks occurred in 4.76 days after discovery. That’s 43% faster than the prior period.

#### Exploit Dispersion
- 41% of organizations detected activity for exploits less than one month old.

#### ATT&CK Sightings
- Sandbox and network detection and response (NDR) sensors observed activity for over two-thirds of MITRE ATT&CK techniques.

#### Exploit Dispersion
- 41% of organizations detected activity for exploits less than one month old.

#### APT Groups
- FortiRecon intelligence indicates 38 of the 143 advanced persistent threat (APT) groups listed by MITRE were active during this time.

#### Ransomware
- More than 40% of ransomware and wipers targeted the industrial sector, indicating that cybercriminals are focused on OT and the supply chain.

#### Time-to-Exploitation
- On average, for new exploits identified, attacks occurred in 4.76 days after discovery. That’s 43% faster than the prior period.

## A Look at Exploit, Malware, and Botnet Trends

FortiGuard Labs monitors a vast array of globally deployed sensors that collect trillions of threat events worldwide each day. This unique vantage point gives us a detailed and comprehensive view of the cyberthreat landscape, including how exploit, malware, and botnet trends change over time.

### Exploits
- 11,030 unique exploit detections, +10% over last half
- 63 exploit detections per organization, +17% over last half
- 73% of firms saw severe attacks, +4% over last half

### Malware
- 39,896 unique variants detected, -11% from last half
- 5,962 different active families, -16% from last half
- 16 families spread to more than 10% of organizations, -11% from last half

### Botnet
- 319 unique botnets detected, -3% from last half
- 4.3 active botnets per sensor, +/-0% from last half
- 85 infection days in average, +2% over last half

This data, outlined in the chart above, shows that the creation and prevalence of exploits are on the rise. Cybercriminals are targeting the ever-increasing number of new vulnerabilities resulting from the exponential growth in the number and variety of connected devices and an explosion in new applications and online services. It’s only natural that attacks looking to exploit those vulnerabilities would rise as well. This increase in exploit volume per organization is undoubtedly contributing to the prevalence of overwhelmed security teams.

Interestingly, after rising over the first half of 2023, the volume of malware samples detected by our sensors subsided in the latter half of the year. Unfortunately for defenders, this doesn’t mean that malware is falling out of favor among clever attackers. The observed slowdown is likely because certain types of malware, particularly ransomware, are taking a more targeted approach, leading to an increase in cost-per-ransomware incident. This also explains why bot traffic remained steady during this same time.

#### IoT exploits are on the rise
Exploitation activity captured by the FortiGuard Intrusion Prevention System (IPS) sensors running on our FortiGate Next-Generation Firewalls provides unrivaled visibility into how threat actors find vulnerabilities, exploit their targets, and build malicious infrastructure. These sensors are often the first point of contact with an adversary probing for exposures. Let’s start with a view of the technologies attackers are probing most aggressively. Not surprisingly, Internet-of-Things (IoT) devices, shown in red in the corresponding chart, are popular targets, largely because they are often under protected or unprotected.

While we have highlighted outbreak alerts for IoT devices here, our FortiGuard Labs team had their radars filled with all manner of additional vulnerability exploits in 2H 2023. Here’s a quick recap of some of those:
- VMware Aria Operations for Networks Command Injection Vulnerability[^5]
- IBM Aspera Faspex Code Execution Vulnerability[^6]
- Cisco IOS XE Web UI Attack[^7]
- Citrix Bleed Attack[^8]
- Apache RocketMQ Remote Command Execution Vulnerability[^9]
- Progress MOVEit Transfer SQL Injection Vulnerability[^10]

#### Technology platforms targeted most often with exploit attempts
| Month | Top Target 1 | Top Target 2 | Top Target 3 | Top Target 4 | Top Target 5 | Top Target 6 | Top Target 7 | Top Target 8 | Top Target 9 | Top Target 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| July | Zyxel.zhttpd (38%) | Multiple.Routers (40%) | Zyxel.zhttpd (39%) | Apache.Log4j (40%) | Zyxel.zhttpd (37%) | Apache.Log4j (43%) | PHP.CGI (37%) | PHP.CGI (37%) | Multiple.Routers (37%) | Zyxel.zhttpd (37%) |
| Aug | Linux.Kernal (36%) | Zyxel.zhttpd (37%) | Linux.Kernel (35%) | Zyxel.zhttpd (37%) | PHPUnit.Eval-stdin (36%) | PHPUnit.Eval-stdin (37%) | Multiple.Routers (34%) | Linux.Kernel (35%) | D-Link.Devices (35%) | PHPUnit.Eval-stdin (36%) |
| Sep | Linux.Kernal (36%) | Zyxel.zhttpd (37%) | PHPUnit.Eval-stdin (33%) | Multiple.Routers (35%) | PHPUnit.Eval-stdin (34%) | Linux.Kernal (35%) | Telerik.Web (33%) | Multiple.Routers (34 %) | Dasan.GPON (33%) | D-Link.Devices (30%) |
| Oct | Zyxel.zhttpd (38%) | Apache.Log4j (40%) | Zyxel.zhttpd (39%) | Apache.Log4j (43%) | Zyxel.zhttpd (37%) | Apache.Log4j (43%) | PHP.CGI (37%) | PHP.CGI (37%) | Multiple.Routers (37%) | Zyxel.zhttpd (37%) |
| Nov | Linux.Kernal (36%) | Zyxel.zhttpd (37%) | Linux.Kernel (35%) | Zyxel.zhttpd (37%) | PHPUnit.Eval-stdin (36%) | PHPUnit.Eval-stdin (37%) | Multiple.Routers (34%) | Linux.Kernel (35%) | D-Link.Devices (35%) | PHPUnit.Eval-stdin (36%) |
| Dec | Linux.Kernal (36%) | Zyxel.zhttpd (37%) | PHPUnit.Eval-stdin (33%) | Multiple.Routers (35%) | PHPUnit.Eval-stdin (34%) | Linux.Kernal (35%) | Telerik.Web (33%) | Multiple.Routers (34 %) | Dasan.GPON (33%) | D-Link.Devices (30%) |

Vulnerabilities affecting routers, cameras, and other IoT devices were the focus of several outbreak alerts published by FortiGuard Labs throughout 2023.[^1]

Zyxel Networks equipment was a favorite target for exploits throughout the second half of the year, with FortiGuard Labs issuing an outbreak alert about the company’s firewalls.[^2] Perhaps smelling blood in the water, attackers rediscovered and exploited a Zyxel Networks vulnerability relating to an end-of-life router, which was initially published in 2017.[^3]

Speaking of old vulnerabilities attracting new attention, exploits targeting Zivif web cameras (CVE-2017-11882) made the top 10 list in December 2023. These exploits appear to be related to ongoing Zerobot attacks we alerted security practitioners to in late 2022.[^4] This scenario shows that old vulnerabilities can always be made new (and better) by enterprising threat actors.

We are closing out this exploit review with another chart demonstrating the wide scope of activity detected by our IPS sensors. Here is a look at the top five exploit detections associated with four key MITRE ATT&CK techniques[^11] of Active Scanning, Exploit Public-Facing Apps, Brute Force, and Network DoS.

#### Most prevalent recon and initial access detections associated with MITRE ATT&CK techniques
- **Active Scanning (T1595)**: SIPVicious.SIP.Scanner (53%), DNS.PTR.Records.Scan (42%), Qualys.Vulnerability.Scanner (2.0%), Port.Scanner (0.85%), Nessus.Scanner (0.73%)
- **Exploit Public-Facing Application (T1190)**: MS.SMB.Server.Trans.Peeking.Data.Information.Disclosure (63%), SSL.Anonymous.Ciphers.Negotiation (7.4%), Modbus.TCP.Unauthorized.Read.Request.PLC (6.2%), Apache.Log4j.Error.Log.Remote.Code.Execution (3.0%), HTTP.Suspicious.Headers.With.Special.Characters (3.0%)
- **Brute Force (T1110)**: SSH.Connection.Brute.Force (35%), SMB.Login.Brute.Force (22%), MS.RDP.Connection.Brute.Force (17%), MySQL.Login.Brute.Force (11%), SIP.Register.Brute.Force (6.1%)
- **Network Denial-of-Service (T1498)**: NTP.Monlist.Command/DoS (64%), IP.Land (15%), BlackNurse.ICMP.Type.3.Code.3.Flood.Dos (11%), Memcached.UDP.Amplification.Detection (2.4%), DNS.Amplificatioj.Detection (1.8%)

Network security appliances provide intelligence on the left side of the MITRE ATT&CK framework, which helps us understand more about the threats that malicious actors are using to try to get inside organizations. Ideally, when applying the ATT&CK framework across your enterprise, we recommend collating ATT&CK sources and creating a consolidated heatmap for using in threat hunting, purple teaming, adversarial emulation, and detection engineering.

#### Tracking movement across malware families
Once threat actors find an exploitable vulnerability, their next step is often to deploy malware. Samples picked up by our various anti-malware solutions offer insight into popular adversary tools for establishing a foothold, escalating privileges, maintaining presence, and moving laterally within target environments to achieve their goals.

The figure on the next page measures the proportion of organizations in each region that detected variants of the most common malware families during the second half of the year. Malware that gains a foothold in one region of the world, such as the JS/Agent family, gains similar traction across most other geographies.

#### Top malware families based on regional prevalence
| Region | JS/Agent | JS/Phishing | MSIL/Kryptik | HTML/Phish | JS/ScrInject | JS/Cryxos | MSIL/GenKryptik | PDF/Phishing | MSIL/GenericKDS | HTML/Phishing | MSIL/Agent | MSOffice/CVE_2018_0798 | JS/Redirector | MSIL/Stealer | NSIS/Injector | MSOffice/CVE_2017_11882 | HTML/infObfus | BAT/Agent | W32/Injector | MSOffice/CVE_2017_11882 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Africa | 40.9% | 17.6% | 17.4% | 16.5% | 20.1% | 12.8% | 14.6% | 14.1% | 11.8% | 12.5% | 11.6% | 9.8% | 13.7% | 9.5% | 8.5% | 8.4% | 11.8% | 5.5% | 8.6% | 8.2% |
| Asia | 34.2% | 15.9% | 22.6% | 19.9% | 13.1% | 28.6% | 20.8% | 12.8% | 19.1% | 13.1% | 16.1% | 15.0% | 7.7% | 14.6% | 13.4% | 12.1% | 5.9% | 9.1% | 11/9% | 12/3% |
| Europe | 34.0% | 19.2% | 19.8% | 18.6% | 11.9% | 13.6% | 17.9% | 14.9% | 15.2% | 12.0% | 14.6% | 15.1% | 9.6% | 11.8% | 13.1% | 11.0% | 6.3% | 6.3% | 8.9% | 8.6% |
| Latin America | 37.4% | 19.8% | 16.6% | 15.2% | 18.6% | 14.7% | 16.1% | 12.9% | 13.6% | 9.6% | 11.4% | 9.4% | 8.0% | 10.3% | 7.1% | 17.6% | 4.2% | 9.0% | 6.8% | 5.0% |
| Middle East | 30.9% | 12.7% | 16.9% | 13.9% | 33.4% | 12.1% | 15.4% | 11.2% | 12.7% | 9.2% | 12.1% | 10.2% | 7.8% | 10.3% | 10.1% | 9.5% | 10.1% | 6.7% | 9.0% | 7.4% |
| North America | 30.0% | 12.0% | 4.8% | 7.9% | 10.3% | 13.3% | 4.3% | 8.9% | 3.7% | 5.6% | 3.5% | 3.4% | 7.5% | 2.8% | 2.4% | 2.5% | 10.5% | 3.7% | 2.2% | 2.3% |
| Oceania | 35.9% | 18.5% | 7.5% | 12.0% | 18.7% | 18.7% | 7.2% | 14.1% | 6.1% | 7.3% | 5.6% | 4.7% | 10.7% | 4.5% | 5.3% | 3.4% | 15.7% | 4.3% | 3.0% | 3.3% |

However, two malware families have bucked the regional uniformity trend: JS/ScrInject and JS/Cryxos. For the former, the variant responsible is JS/ScrInject.B!.tr.[^16] This Remote Access Trojan (RAT) has been circulating since 2011 and has a very regular weekly activity cycle.[^17] The other is JS/Cryxos and, in particular, the JS/Cryxos.5478!.tr variant.[^18] This Trojan, known to have a variety of surreptitious capabilities, appears to be driving the bulk of detections across Asia.

Outside the most prevalent generic families depicted above, four additional malware campaigns caught our attention in the second half of 2023: AndroxGh0st, Apache ActiveMQ ransomware, Lazarus RATs, and Agent Tesla. We cover AndroxGh0st extensively in the botnet section, so we’ll summarize the other three here.

#### Apache ActiveMQ
Apache ActiveMQ is a popular open-source message broker. A vulnerability was disclosed (CVE-2023-46604)[^19] in fall 2023 that allowed a remote attacker with network access to a broker to run arbitrary shell commands by manipulating serialized class types in the OpenWire protocol. Reports emerged in November that attackers were taking advantage of that flaw in the form of the HelloKitty ransomware.[^20] FortiGuard Labs released an outbreak alert detailing how threat actors were exploiting this flaw by running ransomware campaigns targeting servers running outdated and vulnerable versions of Apache ActiveMQ.[^21]

#### Lazarus RATs
The Lazarus Group is an APT group sponsored by the North Korean government. In this new campaign, Lazarus was observed employing DLang-based RAT malware in the wild. Lazarus’s initial access begins with the successful exploitation of CVE-2021-44228, the infamous Log4j vulnerability discovered in 2021.[^22]

#### Agent Tesla
FortiGuard Labs captured a phishing campaign that spreads a new Agent Tesla variant.[^23] This well-known malware family uses a .Net-based RAT and data stealer to gain initial access by exploiting Microsoft Office vulnerabilities CVE-2017-11882[^24] and CVE-2018-0802.[^25] The Agent Tesla core module can collect sensitive information from the victim’s device such as, saved credentials, keylogging information, and device screenshots.

### Into the Red Zone

#### New bots on the block: AndroxGh0st, Prometei, and DarkGate
Once infected with malware, systems often attempt to communicate with remote hosts to download additional payloads, establish command and control (C2) channels, and open backdoors into the environment. This makes the analysis of botnet traffic an important part of monitoring the full scope of malicious activity.

#### New botnets
- 15% of volume
- 85.4%

A chart of the most active botnets is inevitably filled with many of the same ones we’ve seen for years, including Gh0st, Mirai, and ZeroAccess. This demonstrates two things:
- Botnets are resilient. They’re created to persist and, despite coordinated law enforcement takedowns, can be hard to kill.
- Botnet remediation is a slow process. Much of the botnet traffic we detect comes from infected systems attempting to communicate with botnets that are no longer active.

That said, new botnets do emerge occasionally that warrant attention. In the second half of 2023, three new botnets took the spotlight: AndroxGh0st, Prometei, and DarkGate.

#### Volume of traffic associated with new botnets emerging in 2H 2023
| Month | Prometei | DarkGate | AndroxGh0st.Malware |
|---|---|---|---|
| Jul |  |  |  |
| Aug |  |  |  |
| Sep |  |  |  |
| Oct |  |  |  |
| Nov |  |  |  |
| Dec |  |  |  |

#### AndroxGh0st
The AndroxGh0st botnet is related to the Python-based malware of the same name. It primarily targets user environment (.env) files, which often contain credentials for a variety of high-profile applications. AndroxGh0st includes numerous malicious functions to abuse Simple Mail Transfer Protocols (SMTP). It also scans and exploits exposed credentials and APIs and deploys web shells to maintain persistent access to systems.

We continue to observe widespread activity of AndroxGh0st malware in the wild exploiting multiple vulnerabilities. It specifically targets the PHPUnit (CVE-2017-9841)[^26], Laravel Framework (CVE-2018-15133)[^27], and Apache Web Server (CVE-2021-41773)[^28] vulnerabilities to spread and conduct information-gathering attacks on the target networks. Fortinet was credited with exposing telemetry on AndroxGh0st, showing over 40,000 devices infected by the botnet.[^29]

#### Prometei
Prometei is malware that can remotely control infected machines. It’s capable of spreading laterally across networks, stealing password credentials, executing arbitrary commands, and downloading and executing additional malicious components. Prometei can also perform cryptocurrency mining and has self-updating capabilities.

This malware strain was recently reinvented, and we created new IPS signatures to aid in detection.[^30] This retooling worked well, as the Prometei botnet has subsequently been catapulted to the sixth spot on our list for total traffic volume across our sensors in 2H 2023.

#### DarkGate
Though it’s a distant third to AndroxGh0st and Prometei, the DarkGate botnet warrants mention. The DarkGate malware, which has a range of capabilities from remote access to cryptomining to information stealing, was first reported in 2017. Since then, its creators have used it only for specific campaigns. But in mid-2023, the purported author offered to sell it, and the malware soon began making wider rounds.[^31] We saw the DarkGate botnet emerge after the Qakbot takedown as a possible successor.[^32] Whether DarkGate has a future as a leading tool for cybercriminals remains to be seen.

## Most Active APTs

In the first half of the year, we observed significant activity among APT groups, and that volume has held steady throughout the remainder of 2023. APT groups continue to be highly adaptable to changes in the digital landscape and are increasingly stealthy as they carefully plan and execute attacks. The image below offers a look at the most active APT groups during the second half of the year.

#### Most active APT groups during 2H 2023 based on FortiRecon intelligence
- **Actor**: Lazarus Group
  - **Top Target(s)**: Technology
- **APT 28**
  - **Top Target(s)**: Government
- **APT 29**
  - **Top Target(s)**: Government
- **Andariel Technology**
- **OilRig**
  - **Top Target(s)**: Government, Healthcare
- **Kimsuky**
  - **Top Target(s)**: Government
- **Andariel Technology**
- **OilRig**
  - **Top Target(s)**: Government, Healthcare
- **MuddyWater**
  - **Top Target(s)**: Telecom
- **APT37**
  - **Top Target(s)**: Aerospace Defense, Civil Society, and Manufacturing

Researchers’ latest findings indicate a definitive shift in the tactics of the North Korean APT group, Lazarus. Over the past year and a half, they have disclosed three different RATs built using uncommon technologies during development, like QtFramework, PowerBasic, and DLang. This indicates that Lazarus Group is a mature and capable organization, generally using N-Day exploits and known techniques to breach companies in the technology sector, such as blockchain exchanges and software development firms. The group’s attacks have been quite lucrative, netting north of $100 million in crypto thefts alone.

Another group that was active these last months of 2023 was APT 28, using N-Day vulnerabilities in Outlook and Winrar to steal New Technology Lan Manager (NTLM) credentials, focusing on breaching government organizations as well as companies in the higher education, manufacturing, and aerospace industries. The group targeted organizations in Eastern Europe, with multiple campaigns aimed at disrupting operations and stealing information from these enterprises. This same group also used previously undisclosed zero days this year to carry on cyberespionage and steal data. APT 28 has also moved away from using backdoors and compromising peripheral devices in the network and is now using legitimate services such as Google Drive and Microsoft OneDrive to exfiltrate sensitive data.

## Penetrating the Red Zone

Prioritizing vulnerabilities for remediation is more important than ever given that the rate of discovery and disclosure continues to quicken. As of this report’s publication, there are over 222,000 vulnerabilities on the Common Vulnerabilities and Exposures (CVE) list.[^33] We witnessed a new record in 2023, with a total of 30,000 new vulnerabilities published—a 17% jump from the previous year.

In 2022, we introduced the concept of the “red zone,” which helps readers better understand how likely (or unlikely) it is that threat actors will exploit a specific vulnerability.[^34] This allows security teams to focus on the vulnerabilities that present the most risk by prioritizing remediation efforts.

Thankfully, our data shows a small subset (12.5%) of all historical CVEs are present and unremediated on endpoints in live environments. This is depicted in the ratio of blue versus gray squares in the adjacent chart.

Further, only a fraction (<1%) of all vulnerabilities were exploited in 2H 2023. That proportion has remained remarkably steady over time, which is good news for security teams.

#### 30K new vulnerabilities across all industries were published in 2023, marking a 17% increase from the prior year.

Of course, the red zone for many prominent software platforms is substantially larger. For example, Microsoft’s attack surface is 20x larger than the overall average (14%) and twice that of Apple (7%) and Linux (5%). Practically speaking, the larger the red zone, the more effort and automated patching is required for timely remediation of high-risk vulnerabilities with active exploits.

#### Red zone activity for all CVEs across all platforms
- About 0.7% of all CVEs observed on endpoints and under attack
- **Absent**: 1.6K
- **Present**:
- **Attacked**:

#### Red zone activity for CVEs affecting prominent platforms
- **Microsoft (14.2%)**
- **Adobe (13.6%)**
- **Apple (7.1%)**
- **Linux (5.3%)**
- **Oracle (3.6%)**
- **Google (2.6%)**

Here is a look at the top five vulnerabilities that comprise each platform’s red zone based on the prevalence of detected exploit attempts:

#### CVEs with the highest exploit activity for each prominent software platform
- **Microsoft**: CVE-2017-0147, CVE-2016-3212, CVE-2017-0068, CVE-2021-31207, CVE-2022-24463
- **Adobe**: CVE-2017-16391, CVE-2008-2992, CVE-2023-26397, CVE-2017-16383, CVE-2018-5019
- **Apple**: CVE-2018-4443, CVE-2017-13798, CVE-2018-4312, CVE-2020-9802, CVE-2018-4386
- **Linux**: CVE-2013-2912, CVE-2021-30632, CVE-202130538, CVE-2019-13720, CVE-2020-15994
- **Oracle**: CVE-2021-44228, CVE-2014-0160, CVE-2016-1000110, CVE-2015-2331, CVE-2014-0224
- **Google**: CVE-2019-0948, CVE-2019-0537, CVE-2016-3427, CVE-2012-5081, CVE-2013-2416

The share of red zone activity across vulnerabilities differs dramatically among platforms. A full 99% of Linux’s red zone is dominated by exploits targeting CVE-2021-44228.[^35] Compare that to Apple, where the top three vulnerabilities each account for approximately 16% of exploit activity.

Most of these red zone vulnerabilities aren’t new. Only two were published in 2023, and just one of those emerged in the second half of the year (CVE-2023-44487).[^36] The rest span the last decade. And keep in mind that the exploitation “old” vulnerabilities isn’t slowing—the top vulnerability for half the platforms listed was discovered at least five years prior.

## From Exploit Prediction to Outbreak

As we’ve discussed previously, when it comes to vulnerabilities, what’s old is still new in the eyes of many attackers. To understand the prevalence of this trend, we identified all vulnerability exploits and malware samples that occurred in 2H 2023 along with the proportion of organizations registering detections. We then charted those signatures according to when they were created and added to Fortinet devices. The charts on the next page measure the active lifespan of exploit and malware threats.

#### Age and prevalence of exploits and malware detected in 2H 2023

##### IPS Detections
- **40.9% of orgs reported exploitation activity <1 month**
- **47.3% of orgs reported exploitation activity 2 months to 1 year**
- **97.6% of orgs reported exploitation activity 5+ years**
- **Age of Triggered Signature**: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20

##### Malware Detections
- **40.5% of orgs reported virus activity <1 month**
- **38.7% of orgs reported virus activity 2 months to 1 year**
- **53.8% of orgs reported virus activity 5+ years**
- **Age of Triggered Signature**: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28

We continue to observe threat actors exploiting vulnerabilities more than 15 years old. Nearly all organizations (98%) have detected exploits that have existed for at least five years. Yet there’s plenty of room for new threats to make their way onto the scene: 41% of organizations also detected exploits from signatures less than one month old. But when it comes to malware, just over half of organizations have detected variants that have been around for five or more years—much less than what we see for exploits.

This analysis yields some critical insights into the cyberthreat landscape. Exploits and malware have very similar speeds and scopes related to their spread, but the longevity of each differs. Malware variants die off more quickly as new code replaces the old. Exploits show a much longer active lifespan because the vulnerabilities cybercriminals target can remain unpatched for years.

Practically speaking, this reinforces the importance of remaining vigilant about security hygiene, as attackers aren’t likely to stop exploiting older vulnerabilities. It’s also a great reminder to security practitioners to act quickly through a consistent patching and updating program when new vulnerabilities emerge that are likely to be exploited.

How can you track emerging vulnerabilities that are most likely to be attacked? The Exploit Prediction Scoring System (EPSS)[^37] exists for this exact purpose. Fortinet is a major contributor to the exploitation data that drives EPSS. The chart below shows the vulnerabilities released in 2023 that were most targeted by exploit activity in the latter half of the year.

#### Most widely exploited CVEs published in 2023 with EPSS score
- **Top 10 Actively Exploited CVEs: 2023**
  - **EPSS Ranking**: CVE-2023-1389 (TP-Link) (Top 72.9%), CVE-2023-23752 (Joomla) (Top 25.7%), CVE-2023-27350 (PaperCut) (Top 7.2%), CVE-2023-28