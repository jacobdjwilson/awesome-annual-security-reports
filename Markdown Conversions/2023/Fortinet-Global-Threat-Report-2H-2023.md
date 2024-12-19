# A Semiannual Report by FortiGuard Labs
# Global Threat Landscape Report
## 2H 2023

## Table of Contents
[Executive Summary](#executive-summary)
[2H 2023 Active Threat Landscape at a Glance](#2h-2023-active-threat-landscape-at-a-glance)
[A Look at Exploit, Malware, and Botnet Trends](#a-look-at-exploit-malware-and-botnet-trends)
[Most Active APTs](#most-active-apts)
[Penetrating the Red Zone](#penetrating-the-red-zone)
[From Exploit Prediction to Outbreak](#from-exploit-prediction-to-outbreak)
[Ransomware Attacks Increasingly Target Critical Industries](#ransomware-attacks-increasingly-target-critical-industries)
[Global ATT&CK Heatmap](#global-attck-heatmap)
[Shedding Light on Dark Web Activity](#shedding-light-on-dark-web-activity)
[Trends from the Trenches](#trends-from-the-trenches)
[Conclusion](#conclusion)
[Footnotes](#footnotes)

## Executive Summary
In the second half of 2023, the cybersecurity landscape saw a range of significant developments that have considerably impacted the digital attack surface. Notable among these was the rise in sophisticated cyberattacks targeting large-scale entities and essential infrastructure.

If the growing number of attacks weren’t enough to keep most CISOs awake at night, the cybersecurity domain is simultaneously grappling with the ongoing challenge of attracting and retaining skilled professionals. The rising demand for qualified cybersecurity experts, coupled with the need for organizations to offer attractive career development opportunities and work environments, continues to highlight the importance of human capital in combating cyberthreats.

The need to understand where your attack surface gaps in detection, mitigation, and response lie is more vital than ever and the most impactful thing we can do is to shed light on how the threat landscape has been shifting and how organizations need to build secure networking systems that can quickly adapt to changing business demands and the evolving threat landscape. That’s why we publish this report. Our goal is to help you navigate these changes and understand where to focus your time and energy, using your resources in the most impactful way.

The findings in this report represent the collective intelligence of FortiGuard Labs, drawn from a vast array of network sensors collecting threat events each day observed in live production environments around the world from more than 600K+ environments and 10M+ sensors capturing every detail about threats that hit our detection technology. We’ve sifted through all that data to find and extract key insights that we hope will help guide you through the cyber challenges of 2024.

## 2H 2023 Active Threat Landscape at a Glance
*   **8.8%** The percent of all endpoint vulnerabilities targeted by attacks remained steady, around 9%.
*   **41%** Attacks can spread quickly. 41% of organizations detected activity for exploits less than one month old.
*   **91.2%** Sandbox and network detection and response (NDR) sensors observed activity for over two-thirds of MITRE ATT&CK techniques.
*   **67.1%** FortiRecon intelligence indicates 38 of the 143 advanced persistent threat (APT) groups listed by MITRE were active during this time.
*   **32.9%** More than 40% of ransomware and wipers targeted the industrial sector, indicating that cybercriminals are focused on OT and the supply chain.
*   **59%** On average, for new exploits identified, attacks occurred in 4.76 days after discovery. That’s 43% faster than the prior period.
    *   **+0.5%** since last half
    *   **+0.4%** since last half
    *   **38/143**
    *   **40%+**
    *   **43%**
*   **Into the Red Zone**
*   **Exploit Dispersion**
*   **ATT&CK Sightings**
*   **APT Groups**
*   **Ransomware**
*   **Time-to-Exploitation**
*   **Orgs seeing exploits <1 month old**

## A Look at Exploit, Malware, and Botnet Trends
FortiGuard Labs monitors a vast array of globally deployed sensors that collect trillions of threat events worldwide each day. This unique vantage point gives us a detailed and comprehensive view of the cyberthreat landscape, including how exploit, malware, and botnet trends change over time.

This data, outlined in the chart above, shows that the creation and prevalence of exploits are on the rise. Cybercriminals are targeting the ever-increasing number of new vulnerabilities resulting from the exponential growth in the number and variety of connected devices and an explosion in new applications and online services. It’s only natural that attacks looking to exploit those vulnerabilities would rise as well. This increase in exploit volume per organization is undoubtedly contributing to the prevalence of overwhelmed security teams.

Interestingly, after rising over the first half of 2023, the volume of malware samples detected by our sensors subsided in the latter half of the year. Unfortunately for defenders, this doesn’t mean that malware is falling out of favor among clever attackers. The observed slowdown is likely because certain types of malware, particularly ransomware, are taking a more targeted approach, leading to an increase in cost-per-ransomware incident. This also explains why bot traffic remained steady during this same time.

IoT exploits are on the rise

Exploitation activity captured by the FortiGuard Intrusion Prevention System (IPS) sensors running on our FortiGate Next-Generation Firewalls provides unrivaled visibility into how threat actors find vulnerabilities, exploit their targets, and build malicious infrastructure. These sensors are often the first point of contact with an adversary probing for exposures. Let’s start with a view of the technologies attackers are probing most aggressively. Not surprisingly, Internet-of-Things (IoT) devices, shown in red in the corresponding chart, are popular targets, largely because they are often under protected or unprotected.

*   **Exploits**
    *   11,030 unique exploit detections, +10% over last half
    *   63 exploit detections per organization, +17% over last half
    *   73% of firms saw severe attacks, +4% over last half
*   **Malware**
    *   39,896 unique variants detected, -11% from last half
    *   5,962 different active families, -16% from last half
    *   16 families spread to more than 10% of organizations, -11% from last half
*   **Botnet**
    *   319 unique botnets detected, -3% from last half
    *   4.3 active botnets per sensor, +/-0% from last half
    *   85 infection days in average, +2% over last half

Vulnerabilities affecting routers, cameras, and other IoT devices were the focus of several outbreak alerts published by FortiGuard Labs throughout 2023.[^1]

Zyxel Networks equipment was a favorite target for exploits throughout the second half of the year, with FortiGuard Labs issuing an outbreak alert about the company’s firewalls.[^2] Perhaps smelling blood in the water, attackers rediscovered and exploited a Zyxel Networks vulnerability relating to an end-of-life router, which was initially published in 2017.[^3]

Speaking of old vulnerabilities attracting new attention, exploits targeting Zivif web cameras (CVE-2017-17107) made the top 10 list in December 2023. These exploits appear to be related to ongoing Zerobot attacks we alerted security practitioners to in late 2022.[^4] This scenario shows that old vulnerabilities can always be made new (and better) by enterprising threat actors.

**Technology platforms targeted most often with exploit attempts**

| Rank | July                      | Aug                       | Sep                        | Oct                       | Nov                       | Dec                       |
|------|---------------------------|---------------------------|----------------------------|---------------------------|---------------------------|---------------------------|
| 1    | PHP.CGI (37%)             | PHP.CGI (37%)             | PHPUnit.Eval-stdin (36%)   | Apache.Log4j (40%)        | Apache.Log4j (43%)        | Zyxel.zhttpd (38%)        |
| 2    | Linux.Kernel (35%)        | PHPUnit.Eval-stdin (36%)  | Linux.Kernal (36%)         | PHPUnit.Eval-stdin (37%)  | Zyxel.zhttpd (38%)        | D-Link.Devices (35%)      |
| 3    | PHPUnit.Eval-stdin (34%)  | Linux.Kernal (35%)        | Telerik.Web (34%)          | Linux.Kernal (35%)        | Linux.Kernel (35%)        | Multiple.Routers (34 %)   |
| 4    | Telerik.Web (33%)         | Telerik.Web (33%)         | ThinkPHP.Controller (32%) | Telerik.Web (32%)         | Telerik.Web (33%)         | Dasan.GPON (34%)          |
| 5    | ThinkPHP.Controller (33%) | Apache.Log4j (30%)        | Apache.HTTP (31%)          | PHP.URI (29%)             | PHPUnit.Eval-stdin (33%)  | NETGEAR.DGN1000 (31%)     |
| 6    |                           | Backdoor.Cobalt (29%)      |                            | Bash.Function (25%)       | Apache.Log4j (27%)        | Multiple.Routers (40%)    |
| 7    |                           |                           |                            | Java.Debug (28%)          |                           | Zyxel.zhttpd (37%)        |
| 8    |                           |                           |                            |                           |                           | Dasan.GPON (34%)          |
| 9    |                           |                           |                            |                           |                           | D-Link.Devices (34%)      |
| 10   |                           |                           |                            |                           |                           | MikroTik.RouterOS (30%)   |

*A table showing the top ten technologies targeted by exploits each month from July to December 2023.*

While we have highlighted outbreak alerts for IoT devices here, our FortiGuard Labs team had their radars filled with all manner of additional vulnerability exploits in 2H 2023. Here’s a quick recap of some of those:

*   VMware Aria Operations for Networks Command Injection Vulnerability[^5]
*   IBM Aspera Faspex Code Execution Vulnerability[^6]
*   Cisco IOS XE Web UI Attack[^7]
*   Citrix Bleed Attack[^8]
*   Apache RocketMQ Remote Command Execution Vulnerability[^9]
*   Progress MOVEit Transfer SQL Injection Vulnerability[^10]

We are closing out this exploit review with another chart demonstrating the wide scope of activity detected by our IPS sensors. Here is a look at the top five exploit detections associated with four key MITRE ATT&CK techniques[^11] of Active Scanning, Exploit Public-Facing Apps, Brute Force, and Network DoS.

**Most prevalent recon and initial access detections associated with MITRE ATT&CK techniques**

*   **Active Scanning (T1595)**
    *   53% SIPVicious.SIP.Scanner
    *   42% DNS.PTR.Records.Scan
    *   2.0% Qualys.Vulnerability.Scanner
    *   0.85% Port.Scanner
    *   0.73% Nessus.Scanner
*   **Exploit Public-Facing Application (T1190)**
    *   63% HTTP.Suspicious.Headers.With.Special.Characters
    *   7.4% MS.SMB.Server.Trans.Peeking.Data.Information.Disclosure
    *   6.2% SSL.Anonymous.Ciphers.Negotiation
    *   3.0% Modbus.TCP.Unauthorized.Read.Request.PLC
    *   3.0% Apache.Log4j.Error.Log.Remote.Code.Execution
*   **Brute Force (T1110)**
    *   35% SSH.Connection.Brute.Force
    *   22% SMB.Login.Brute.Force
    *   17% MS.RDP.Connection.Brute.Force
    *   11% MySQL.Login.Brute.Force
    *   6.1% SIP.Register.Brute.Force
*   **Network Denial-of-Service (T1498)**
    *   64% NTP.Monlist.Command/DoS
    *   15% IP.Land
    *   11% BlackNurse.ICMP.Type.3.Code.3.Flood.Dos
    *   2.4% Memcached.UDP.Amplification.Detection
    *   1.8% DNS.Amplificatioj.Detection

*A chart showing the top five exploit detections associated with four key MITRE ATT&CK techniques.*

Network security appliances provide intelligence on the left side of the MITRE ATT&CK framework, which helps us understand more about the threats that malicious actors are using to try to get inside organizations. Ideally, when applying the ATT&CK framework across your enterprise, we recommend collating ATT&CK sources and creating a consolidated heatmap for using in threat hunting, purple teaming, adversarial emulation, and detection engineering.

### Tracking movement across malware families
Once threat actors find an exploitable vulnerability, their next step is often to deploy malware. Samples picked up by our various anti-malware solutions offer insight into popular adversary tools for establishing a foothold, escalating privileges, maintaining presence, and moving laterally within target environments to achieve their goals.

The figure on the next page measures the proportion of organizations in each region that detected variants of the most common malware families during the second half of the year. Malware that gains a foothold in one region of the world, such as the JS/Agent family, gains similar traction across most other geographies.

**Top malware families based on regional prevalence**

| Malware Family        | Africa | Asia  | Europe | Latin America | Middle East | North America | Oceania |
|-----------------------|--------|-------|--------|---------------|-------------|---------------|---------|
| JS/Agent              | 40.9%  | 34.2% | 34.0%  | 37.4%         | 30.9%       | 30.0%         | 35.9%   |
| JS/Phishing           | 17.6%  | 15.9% | 19.2%  | 19.8%         | 12.7%       | 12.0%         | 18.5%   |
| MSIL/Kryptik          | 17.4%  | 22.6% | 19.8%  | 16.6%         | 16.9%       | 4.8%          | 7.5%    |
| HTML/Phish            | 16.5%  | 19.9% | 18.6%  | 15.2%         | 13.9%       | 7.9%          | 12.0%   |
| JS/ScrInject          | 20.1%  | 13.1% | 11.9%  | 18.6%         | 33.4%       | 10.3%         | 18.7%   |
| JS/Cryxos             | 12.8%  | 28.6% | 13.6%  | 14.7%         | 12.1%       | 13.3%         | 18.7%   |
| MSIL/GenKryptik       | 14.6%  | 20.8% | 17.9%  | 16.1%         | 15.4%       | 4.3%          | 7.2%    |
| PDF/Phishing          | 14.1%  | 12.8% | 14.9%  | 12.9%         | 11.2%       | 8.9%          | 14.1%   |
| MSIL/GenericKDS       | 11.8%  | 19.1% | 15.2%  | 13.6%         | 12.7%       | 3.7%          | 6.1%    |
| HTML/Phishing         | 12.5%  | 13.1% | 12.0%  | 9.6%          | 9.2%        | 5.6%          | 7.3%    |
| MSIL/Agent            | 11.6%  | 16.1% | 14.6%  | 11.4%         | 12.1%       | 3.5%          | 5.6%    |
| MSOffice/CVE_2018_0798 | 9.8%   | 15.0% | 15.1%  | 9.4%          | 10.2%       | 3.4%          | 4.7%    |
| JS/Redirector         | 13.7%  | 7.7%  | 9.6%   | 8.0%          | 7.8%        | 7.5%          | 10.7%   |
| MSIL/Stealer          | 9.5%   | 14.6% | 11.8%  | 10.3%         | 10.3%       | 2.8%          | 4.5%    |
| NSIS/Injector         | 8.5%   | 13.4% | 13.1%  | 7.1%          | 10.1%       | 2.4%          | 5.3%    |
| MSOffice/CVE_2017_11882 | 8.4%   | 12.1% | 11.0%  | 17.6%         | 9.5%        | 2.5%          | 3.4%    |
| HTML/infObfus         | 11.8%  | 5.9%  | 6.3%   | 4.2%          | 10.1%       | 10.5%         | 15.7%   |
| BAT/Agent             | 5.5%   | 9.1%  | 6.3%   | 9.0%          | 6.7%        | 3.7%          | 4.3%    |
| W32/Injector          | 8.6%   | 11/9% | 8.9%   | 6.8%          | 9.0%        | 2.2%          | 3.0%    |
| MSExcel/CVE_2017_11882 | 8.2%   | 12/3% | 8.6%   | 5.0%          | 7.4%        | 2.3%          | 3.3%    |

*A table showing the top 20 malware families based on regional prevalence.*

However, two malware families have bucked the regional uniformity trend: JS/ScrInject and JS/Cryxos. For the former, the variant responsible is JS/ScrInject.B!.tr.[^16] This Remote Access Trojan (RAT) has been circulating since 2011 and has a very regular weekly activity cycle.[^17] The other is JS/Cryxos and, in particular, the JS/Cryxos.5478!.tr variant.[^18] This Trojan, known to have a variety of surreptitious capabilities, appears to be driving the bulk of detections across Asia.

Outside the most prevalent generic families depicted above, four additional malware campaigns caught our attention in the second half of 2023: AndroxGh0st, Apache ActiveMQ ransomware, Lazarus RATs, and Agent Tesla. We cover AndroxGh0st extensively in the botnet section, so we’ll summarize the other three here.

### Apache ActiveMQ
Apache ActiveMQ is a popular open-source message broker. A vulnerability was disclosed (CVE-2023-46604) in fall 2023 that allowed a remote attacker with network access to a broker to run arbitrary shell commands by manipulating serialized class types in the OpenWire protocol.[^19] Reports emerged in November that attackers were taking advantage of that flaw in the form of the HelloKitty ransomware.[^20] FortiGuard Labs released an outbreak alert detailing how threat actors were exploiting this flaw by running ransomware campaigns targeting servers running outdated and vulnerable versions of Apache ActiveMQ.[^21]

### Lazarus RATs
The Lazarus Group is an APT group sponsored by the North Korean government. In this new campaign, Lazarus was observed employing DLang-based RAT malware in the wild. Lazarus’s initial access begins with the successful exploitation of CVE-2021-44228, the infamous Log4j vulnerability discovered in 2021.[^22]

### Agent Tesla
FortiGuard Labs captured a phishing campaign that spreads a new Agent Tesla variant.[^23] This well-known malware family uses a .Net-based RAT and data stealer to gain initial access by exploiting Microsoft Office vulnerabilities CVE-2017-11882 and CVE-2018-0802.[^24] [^25] The Agent Tesla core module can collect sensitive information from the victim’s device such as saved credentials, keylogging information, and device screenshots.

> In case you’d like to double-check your antivirus scans for the most common JS/Agent variants, here are the top three to look for, plus a final variant that moved up the popularity ranks quickly in 2H 2023:
> *   JS/Agent.CY!.tr[^12]
> *   JS/Agent.F022!.tr[^13]
> *   JS/Agent.PIV!.tr[^14]
> *   JS/Agent.NDS!.tr[^15]

### New bots on the block: AndroxGh0st, Prometei, and DarkGate
Once infected with malware, systems often attempt to communicate with remote hosts to download additional payloads, establish command and control (C2) channels, and open backdoors into the environment. This makes the analysis of botnet traffic an important part of monitoring the full scope of malicious activity.

A chart of the most active botnets is inevitably filled with many of the same ones we’ve seen for years, including Gh0st, Mirai, and ZeroAccess. This demonstrates two things:

*   Botnets are resilient. They’re created to persist and, despite coordinated law enforcement takedowns, can be hard to kill.
*   Botnet remediation is a slow process. Much of the botnet traffic we detect comes from infected systems attempting to communicate with botnets that are no longer active.

That said, new botnets do emerge occasionally that warrant attention. In the second half of 2023, three new botnets took the spotlight: AndroxGh0st, Prometei, and DarkGate.

*   **14.6%** New botnets
*   **85.4%** Old versus new bots
*   **15%** of volume
*   **Into the Red Zone**

*A pie chart showing the volume of traffic associated with new botnets versus old botnets.*

**Volume of traffic associated with new botnets emerging in 2H 2023**

*A line chart showing the volume of traffic associated with the AndroxGh0st, Prometei, and DarkGate botnets from July to December 2023.*

### AndroxGh0st
The AndroxGh0st botnet is related to the Python-based malware of the same name. It primarily targets user environment (.env) files, which often contain credentials for a variety of high-profile applications. AndroxGh0st includes numerous malicious functions to abuse Simple Mail Transfer Protocols (SMTP). It also scans and exploits exposed credentials and APIs and deploys web shells to maintain persistent access to systems.

We continue to observe widespread activity of AndroxGh0st malware in the wild exploiting multiple vulnerabilities. It specifically targets the PHPUnit (CVE-2017-9841), Laravel Framework (CVE-2018-15133), and Apache Web Server (CVE-2021-41773) vulnerabilities to spread and conduct information-gathering attacks on the target networks.[^26] [^27] [^28] Fortinet was credited with exposing telemetry on AndroxGh0st, showing over 40,000 devices infected by the botnet.[^29]

### Prometei
Prometei is malware that can remotely control infected machines. It’s capable of spreading laterally across networks, stealing password credentials, executing arbitrary commands, and downloading and executing additional malicious components. Prometei can also perform cryptocurrency mining and has self-updating capabilities.

This malware strain was recently reinvented, and we created new IPS signatures to aid in detection.[^30] This retooling worked well, as the Prometei botnet has subsequently been catapulted to the sixth spot on our list for total traffic volume across our sensors in 2H 2023.

### DarkGate
Though it’s a distant third to AndroxGh0st and Prometei, the DarkGate botnet warrants mention. The DarkGate malware, which has a range of capabilities from remote access to cryptomining to information stealing, was first reported in 2017. Since then, its creators have used it only for specific campaigns. But in mid-2023, the purported author offered to sell it, and the malware soon began making wider rounds.[^31] We saw the DarkGate botnet emerge after the Qakbot takedown as a possible successor.[^32] Whether DarkGate has a future as a leading tool for cybercriminals remains to be seen.

## Most Active APTs
In the first half of the year, we observed significant activity among APT groups, and that volume has held steady throughout the remainder of 2023. APT groups continue to be highly adaptable to changes in the digital landscape and are increasingly stealthy as they carefully plan and execute attacks. The image below offers a look at the most active APT groups during the second half of the year.

**Most active APT groups during 2H 2023 based on FortiRecon intelligence**

*A graphic showing the most active APT groups during 2H 2023. The groups listed are APT 28, Lazarus Group, Kimsuky, APT 29, OilRig, and APT37.*

*   **APT 28** Government
*   **Lazarus Group**
    *   Actor: Lazarus Group
    *   Top Target(s): Technology
*   **Kimsuky** Government
*   **APT 29** Government
*   **OilRig** Government, Healthcare
*   **APT37** Aerospace Defense, Civil Society, and Manufacturing

Researchers’ latest findings indicate a definitive shift in the tactics of the North Korean APT group, Lazarus. Over the past year and a half, they have disclosed three different RATs built using uncommon technologies during development, like QtFramework, PowerBasic, and DLang. This indicates that Lazarus Group is a mature and capable organization, generally using N-Day exploits and known techniques to breach companies in the technology sector, such as blockchain exchanges and software development firms. The group’s attacks have been quite lucrative, netting north of $100 million in crypto thefts alone.

Another group that was active these last months of 2023 was APT 28, using N-Day vulnerabilities in Outlook and Winrar to steal New Technology Lan Manager (NTLM) credentials, focusing on breaching government organizations as well as companies in the higher education, manufacturing, and aerospace industries. The group targeted organizations in Eastern Europe, with multiple campaigns aimed at disrupting operations and stealing information from these enterprises. This same group also used previously undisclosed zero days this year to carry on cyberespionage and steal data. APT 28 has also moved away from using backdoors and compromising peripheral devices in the network and is now using legitimate services such as Google Drive and Microsoft OneDrive to exfiltrate sensitive data.

## Penetrating the Red Zone
Prioritizing vulnerabilities for remediation is more important than ever given that the rate of discovery and disclosure continues to quicken. As of this report’s publication, there are over 222,000 vulnerabilities on the Common Vulnerabilities and Exposures (CVE) list.[^33] We witnessed a new record in 2023, with a total of 30,000 new vulnerabilities published—a 17% jump from the previous year.

In 2022, we introduced the concept of the “red zone,” which helps readers better understand how likely (or unlikely) it is that threat actors will exploit a specific vulnerability.[^34] This allows security teams to focus on the vulnerabilities that present the most risk by prioritizing remediation efforts.

Thankfully, our data shows a small subset (12.5%) of all historical CVEs are present and unremediated on endpoints in live environments. This is depicted in the ratio of blue versus gray squares in the adjacent chart.

Further, only a fraction (<1%) of all vulnerabilities were exploited in 2H 2023. That proportion has remained remarkably steady over time, which is good news for security teams.

*   **30K** new vulnerabilities across all industries were published in 2023, marking a 17% increase from the prior year.

*A graphic showing the ratio of present, absent, and attacked vulnerabilities.*

Of course, the red zone for many prominent software platforms is substantially larger. For example, Microsoft’s attack surface is 20x larger than the overall average (14%) and twice that of Apple (7%) and Linux (5%). Practically speaking, the larger the red zone, the more effort and automated patching is required for timely remediation of high-risk vulnerabilities with active exploits.

**Red zone activity for all CVEs across all platforms**

*   About 0.7% of all CVEs observed on endpoints and under attack
*   Absent
*   Present
*   Attacked
*   **1.6K**

*A graphic showing the ratio of present, absent, and attacked vulnerabilities for all platforms.*

**Red zone activity for CVEs affecting prominent platforms**

*   Microsoft (14.2%)
*   Adobe (13.6%)
*   Apple (7.1%)
*   Linux (5.3%)
*   Oracle (3.6%)
*   Google (2.6%)
*   Absent
*   Present
*   Attacked

*A graphic showing the ratio of present, absent, and attacked vulnerabilities for prominent platforms.*

Here is a look at the top five vulnerabilities that comprise each platform’s red zone based on the prevalence of detected exploit attempts:

**CVEs with the highest exploit activity for each prominent software platform**

*   **Microsoft**
    *   CVE-2017-0147
    *   CVE-2016-3212
    *   CVE-2017-0068
    *   CVE-2021-31207
    *   CVE-2022-24463
    *   0.9%
    *   0.9%
    *   0.9%
    *   0.9%
    *   0.9%
    *   5%
    *   0.4%
    *   88%
    *   99%
*   **Oracle**
    *   CVE-2016-3427
    *   CVE-2012-5081
    *   CVE-2013-2416
    *   CVE-2013-2461
    *   CVE-2015-2590
    *   0.08%
    *   0.1%
    *   0.6%
*   **Linux**
    *   CVE-2021-44228
    *   CVE-2014-0160
    *   CVE-2016-1000110
    *   CVE-2015-2331
    *   CVE-2014-0224
    *   0.1%
    *   0.2%
    *   0.2%
*   **Google**
    *   CVE-2013-2912
    *   CVE-2021-30632
    *   CVE-202130538
    *   CVE-2019-13720
    *   CVE-2020-15994
    *   8%
    *   9%
    *   9%
    *   12%
    *   21%
*   **Apple**
    *   CVE-2018-4443
    *   CVE-2017-13798
    *   CVE-2018-4312
    *   CVE-2020-9802
    *   CVE-2018-4386
    *   8%
    *   8%
    *   16%
    *   16%
    *   16%
*   **Adobe**
    *   CVE-2017-16391
    *   CVE-2008-2992
    *   CVE-2023-26397
    *   CVE-2017-16383
    *   CVE-2018-5019
    *   3%
    *   3%
    *   5%
    *   35%
    *   6%
    *   33%
    *   65%

*A graphic showing the top five vulnerabilities for each prominent software platform.*

The share of red zone activity across vulnerabilities differs dramatically among platforms. A full 99% of Linux’s red zone is dominated by exploits targeting CVE-2021-44228.[^35] Compare that to Apple, where the top three vulnerabilities each account for approximately 16% of exploit activity.

Most of these red zone vulnerabilities aren’t new. Only two were published in 2023, and just one of those emerged in the second half of the year (CVE-2023-44487).[^36] The rest span the last decade. And keep in mind that the exploitation “old” vulnerabilities isn’t slowing—the top vulnerability for half the platforms listed was discovered at least five years prior.

## From Exploit Prediction to Outbreak
As we’ve discussed previously, when it comes to vulnerabilities, what’s old is still new in the eyes of many attackers. To understand the prevalence of this trend, we identified all vulnerability exploits and malware samples that occurred in 2H 2023 along with the proportion of organizations registering detections. We then charted those signatures according to when they were created and added to Fortinet devices. The charts on the next page measure the active lifespan of exploit and malware threats.

**Age and prevalence of exploits and malware detected in 2H 2023**

*   **IPS Detections**
    *   *A line chart showing the percentage of organizations targeted monthly by exploits based on the age of the triggered signature.*
    *   40.9% of orgs reported exploitation