# 2022 Falcon OverWatch Threat Hunting Report

## Table of Contents
- [Executive Summary](#executive-summary)
- [Interactive Intrusion Trends](#interactive-intrusion-trends)
  - [Intrusion Campaign Numbers](#intrusion-campaign-numbers)
  - [Intrusions by Threat Type](#intrusions-by-threat-type)
  - [Intrusions by Industry Vertical](#intrusions-by-industry-vertical)
- [Adversary Activity](#adversary-activity)
- [Adversary Technique Insights](#adversary-technique-insights)
- [Looking Back: Adversary Trends](#looking-back-adversary-trends)
- [Looking Beyond the CVE](#looking-beyond-the-cve)
- [LockBit and Its Technicolor Affiliate Program: How One RaaS Offering Has Spawned Diverse Tradecraft](#lockbit-and-its-technicolor-affiliate-program-how-one-raas-offering-has-spawned-diverse-tradecraft)
- [Tooling Deep Dive: Emerging, Trending and Mainstay Tools](#tooling-deep-dive-emerging-trending-and-mainstay-tools)
- [Better Together: OverWatch and Falcon Complete Team Up to Deliver Immediate Time-to-Value](#better-together-overwatch-and-falcon-complete-team-up-to-deliver-immediate-time-to-value)
- [Looking Deeper: Interesting Tradecraft](#looking-deeper-interesting-tradecraft)
  - [AQUATIC PANDA Demonstrates Deep Familiarity in Victim Network](#aquatic-panda-demonstrates-deep-familiarity-in-victim-network)
  - [Healthcare Sector Finds Itself in the Crosshairs of eCrime Ransomware Affiliates](#healthcare-sector-finds-itself-in-the-crosshairs-of-ecrime-ransomware-affiliates)
  - [Out with the Old, In with the ISO: How Adversaries Have Adapted to the Retirement of the Macro](#out-with-the-old-in-with-the-iso-how-adversaries-have-adapted-to-the-retirement-of-the-macro)
- [Better Together: Be an Active Partner to Get the Most from Your OverWatch and Falcon Subscription](#better-together-be-an-active-partner-to-get-the-most-from-your-overwatch-and-falcon-subscription)
- [Looking Ahead: OverWatch Showcases the Future of Threat Hunting](#looking-ahead-overwatch-showcases-the-future-of-threat-hunting)
  - [OverWatch Takes to the Sky: Hunting for Adversaries in the Cloud](#overwatch-takes-to-the-sky-hunting-for-adversaries-in-the-cloud)
- [OverWatch’s Patented Technology Delivers Inimitable Threat Hunting Capability](#overwatchs-patented-technology-delivers-inimitable-threat-hunting-capability)
- [Three’s a CrowdStrike Powerhouse](#threes-a-crowdstrike-powerhouse)
- [Conclusion](#conclusion)
- [About Falcon OverWatch](#about-falcon-overwatch)
- [CrowdStrike Products and Services](#crowdstrike-products-and-services)
- [About CrowdStrike](#about-crowdstrike)

---

# Executive Summary

77,000
Potential intrusions stopped
with the help of Falcon
OverWatch

7 minutes
The average interval at which
OverWatch threat hunters
uncovered potential
intrusions

1 million +
Malicious events prevented
by the Falcon platform
derived from OverWatch

50%
Increase in interactive
intrusion campaigns

The CrowdStrike Falcon OverWatch™ threat hunting team has been uncovering record volumes of hands-on intrusion attempts and tracking some marked changes in adversary tradecraft. This report shares insights from OverWatch’s around-the-clock threat hunting from July 1, 2021 through June 30, 2022.¹ The findings and data in this report reflect observations derived from OverWatch’s global hunting activities.

In this 12-month period, OverWatch threat hunters directly identified more than 77,000 potential intrusions, or approximately one potential intrusion every seven minutes. This represents thousands of instances where human-driven hunting uncovered adversaries actively seeking to evade autonomous detection methods.

Crucially, OverWatch uses each of these potential intrusions as an opportunity to hone the Falcon platform’s ability to detect and prevent similar intrusions more quickly and autonomously. During the reporting period, threat hunters distilled their findings into the development of hundreds of new behavioral-based preventions, resulting in the Falcon platform’s direct prevention of over 1 million malicious events. These behavioral-based preventions enhance the Falcon platform’s power to uncover novel adversary behavior with greater speed and scale.

This year’s report starts with a close look at OverWatch’s extensive dataset covering observed interactive threat actor behaviors, which we will refer to in this report as “intrusion activity.” It uses this data to examine how and where adversaries are operating to provide a comprehensive overview of the threat landscape.

¹ Unless stated otherwise, the terms “this year,” “last year” or “past year” used throughout the report refer to the period from July 1, 2021 to June 30, 2022.

## eCrime Breakout Time

Key findings from this data include:
* OverWatch tracked a 50% increase in interactive intrusion activity year-over-year.
* Breakout time for eCrime adversaries remained fast, averaging 1 hour and 24 minutes.
* Technology, telecommunications, healthcare, manufacturing and academia were the top 5 industries most frequently targeted by interactive intrusion activity.
* Malware-free activity accounted for 71% of all detections indexed by CrowdStrike Threat Graph®.²

## Looking Back

A number of trends stood out to OverWatch as emblematic of the past year, in which the importance of proactive threat hunting shone through the proliferation of newly disclosed vulnerabilities and zero-days.

In some instances, OverWatch detected zero-day exploits and notified customers of vulnerability-related intrusion activity before the vulnerability was disclosed; this was possible due to OverWatch’s relentless focus on hunting for post-exploitation tradecraft.

A vast array of affiliates are capitalizing on the availability of ransomware-as-a-service (RaaS) offerings. This has contributed to wide variations in eCrime affiliate tradecraft with threat hunters becoming skilled at identifying diverse patterns of adversary tradecraft that preceded the deployment of RaaS tooling.

This report’s retrospective concludes with a comprehensive look at the tools adversaries are leveraging. This includes an examination of emerging tools, trending tools and the tools that have remained persistently popular in adversary arsenals.

² For information on the CrowdStrike Threat Graph, see: [https://www.crowdstrike.com/falcon-platform/threat-graph/](https://www.crowdstrike.com/falcon-platform/threat-graph/)

## Looking Deeper

As important as it is to look at trends, it is equally important to consider outliers. The report looks at some of the most novel and sophisticated tradecraft observed this year — evidence of adversaries’ enduring capacity for innovation.

The technology sector remained a popular target for eCrime and targeted intrusion adversaries alike. A featured case study examines the array of techniques used by AQUATIC PANDA to achieve persistence, steal credentials and move around the victim network.

Healthcare is another sector heavily impacted by interactive cyber intrusions this past year. The report looks at two interesting examples of eCrime affiliate activity observed in the healthcare sector and recommends ways defenders can bolster their security against similar activity.

Finally, the report looks at the increase in the use of ISO files in phishing attacks by both targeted intrusion and eCrime adversaries.

## Looking Ahead

The report closes with a look at where threat hunting is headed into 2022 and beyond. As the adoption of cloud-based technologies accelerates, so too does adversary interest in cloud-based resources. OverWatch is widening the aperture to capture this new direction in adversary targeting. The report looks at cloud-based intrusions that OverWatch and the CrowdStrike Services team handled this year and provides insights into how interactive threats are playing out in this arena.

In looking to the future, the report also details the patented technology that underpins OverWatch’s hunting capability and makes it possible to effectively scale human-driven insights.

## A Note to the Reader

This report’s findings relate to interactive (i.e., hands-on) targeted³ and eCrime intrusions that OverWatch tracks and do not necessarily represent the full spectrum of attacks that are stopped by OverWatch or the Falcon platform.

Moreover, the term “intrusion” is used to describe any malicious interactive activity that OverWatch uncovers in a victim environment. Intrusion is not synonymous with a “breach” and should not be understood to mean that the threat actor was able to achieve their objectives.

³ The term “targeted intrusion” in this report refers to state-nexus or other advanced persistent threat actors.

---

# Interactive Intrusion Trends

## Intrusion Campaign Numbers

SUSPECTED STATE-SPONSORED (Not Attributed)
KITTENs (Iran)
CHOLLIMAS (North Korea)
BEARs (Russia)
BUFFALOs (Vietnam)
PANDAs (China)

Over the past year, OverWatch observed a near 50% increase in interactive intrusion campaigns. In the most recent quarter, from April to June 2022, OverWatch uncovered more intrusion campaigns than in any previous quarter.

## Intrusions by Threat Type

July 2020 to June 2021 vs. July 2021 to June 2022

+50%

Hacktivist 1%
Hacktivist 1%

Targeted 18%
Targeted 14%

eCrime 46%
eCrime 43%

Unattributed 39%
Unattributed 38%

2021
2022

Figure 1. Distribution of interactive intrusions by threat type

* **eCrime**: Financially motivated criminal intrusion activity
* **Targeted**: State-nexus intrusion activity that includes cyber espionage, destructive or disruptive attacks, and currency generation to support a regime
* **Hacktivist**: Intrusion activity undertaken to gain momentum, visibility or publicity for a cause or ideology
* **Unattributed**: Insufficient data available for high-confidence attribution

## Intrusions by Industry Vertical

Notably, in this past year OverWatch uncovered interactive intrusion activity spanning 37 distinct industries — proof that no industry is immune, and evidence of the importance of remaining vigilant.

Figure 2 shows the relative frequency of intrusions for the top 10 industry verticals in which OverWatch uncovered interactive intrusion activity last year. This is compared with the relative frequency of intrusions in each industry vertical in the last reporting period. Figure 3 shows the top five industry verticals split out by threat type, illustrating where eCrime and targeted intrusion adversaries were most active.

### Top 10 Verticals by Intrusion Frequency

July 2021 to June 2022 vs. July 2020 to June 2021

Technology
Telecommunications
Manufacturing
Academic
Healthcare
Financial
Retail
Government
Pharmaceutical
Media

July 2021 to June 2022
July 2020 to June 2021

0% 5% 10% 15% 20%

Figure 2. The figure shows which industry verticals globally were most frequently impacted by interactive intrusions in the past year and also shows any changes relative to the period from July 2020 to June 2021

### Top 5 Verticals by Intrusion Frequency

* **Technology**: Technology was once again in the top spot, remaining a popular target for eCrime and targeted intrusion adversaries alike. The technology sector plays a critical role in supporting the operations of organizations across almost all other sectors; this reliance has increased in the wake of COVID-19 and the need to establish remote operations. Targeted intrusion adversaries may pursue technology companies to fulfill strategic, military, economic or scientific collection requirements, or as part of efforts to compromise supply chains or trusted relationships. Because of the potential value of data owned by technology companies and their vulnerability to disruption, they are also a sought-after target for ransomware campaigns by eCrime adversaries.
* **Telecommunications**: The telecommunications industry remained in second place, driven in large part by targeted intrusion adversaries that conduct operations against telecommunications providers, likely to fulfill their surveillance, intelligence and counterintelligence collection priorities.
* **Manufacturing**
* **Academic**: Notable changes in this year’s list include increased activity against the healthcare and academic industries. This year, intrusions in the healthcare industry were predominantly carried out by eCrime adversaries (eCrime affiliate activity against the healthcare industry is explored in detail later in this report). In contrast, last year, OverWatch reported a significant amount of targeted intrusion activity against the healthcare industry, particularly related to involvement in COVID-19 related research. Looking at the academic industry, OverWatch uncovered eCrime, hacktivist and targeted intrusion activity across the sector. The academic industry has a broad attack surface due to the nature of its users and operations, and is also a potentially high-value target for state-nexus adversaries because universities and academic institutions often possess intellectual property, and individuals of influence can be among their academic staff and alumni.
* **Healthcare**

### eCrime Activity vs. Targeted Intrusions: July 2021 to June 2022

* **Technology**: 21% (eCrime), 14% (Targeted)
* **Telecommunications**: 10% (eCrime), 9% (Targeted)
* **Manufacturing**: 8% (eCrime), 5% (Targeted)
* **Academic**: 7% (eCrime), 4.5% (Targeted)
* **Healthcare**: 6% (eCrime), 5% (Targeted)
* **Financial**: 5% (eCrime), 5% (Targeted)
* **Retail**: 5% (eCrime), 5% (Targeted)
* **Government**: 5% (eCrime), 5% (Targeted)
* **Pharmaceutical**: 5% (eCrime), 5% (Targeted)
* **Media**: 5% (eCrime), 5% (Targeted)

Figure 3. Comparison of the industry verticals most frequently impacted by targeted intrusion vs. eCrime adversaries, July 2021 to June 2022

---

# Adversary Activity

In the past year, OverWatch uncovered interactive intrusion activity conducted by 36 distinct named threat actors, spanning seven groups: BEAR (Russia), CHOLLIMA (North Korea), JACKAL (hacktivist), KITTEN (Iran), PANDA (China), SPIDER (eCrime) and WOLF (Turkey).⁴ These naming conventions are instituted by CrowdStrike to categorize adversaries according to their nation-state affiliations or motivations.

Figure 4 provides a breakdown of the threat groups observed by OverWatch.

## eCrime

Of attributable intrusions, OverWatch tracked 12 named eCrime (aka SPIDER) threat actors; of these, PROPHET SPIDER was the most prolific, responsible for more than twice as many attributed interactive intrusions than the next most active eCrime actor, CARBON SPIDER. PROPHET SPIDER is likely an access broker — an actor that gains access with the intention to sell that access for profit rather than carrying out actions on objectives directly. Were it not for OverWatch alerting victim organizations to these PROPHET SPIDER intrusions, they likely would have progressed to a ransomware incident or breach.

ECrime adversaries remain highly capable, particularly if measured by the speed at which they can move through a victim’s environment. An important OverWatch speed measurement is breakout time: the time an adversary takes to move laterally, from an initially compromised host to another host within the victim environment. Of the hands-on eCrime intrusion activity last year where breakout time could be derived, the average was just 1 hour 24 minutes. Moreover, the OverWatch team found that in 30% of those eCrime intrusions, the adversary was able to move laterally to additional hosts in under 30 minutes.

> Of the hands-on eCrime
> intrusion activity last year
> where breakout time could be
> derived, the average was just
> 1 hour 24 minutes. Moreover,
> the OverWatch team found
> that in 30% of those eCrime
> intrusions, the adversary
> was able to move laterally to
> additional hosts in under
> 30 minutes.

⁴ For more information about specific threat groups, visit the [CrowdStrike Adversary Universe](https://www.crowdstrike.com/cybersecurity-101/threat-intelligence/adversary-universe/).

## Targeted Intrusion

By raw intrusion numbers, WICKED PANDA was the most prolific targeted intrusion threat actor tracked by OverWatch this year, followed closely by NEMESIS KITTEN; they were observed operating in seven and nine industry verticals, respectively.

## Hacktivism

Hacktivist actor group FRONTLINE JACKAL was highly active this past year, seen operating across 11 industry verticals; by comparison, this threat actor was only found in four industry verticals in the previous reporting period. This increase in activity is linked to the adversary’s adoption of opportunistic initial access tactics.

---

# MITRE ATT&CK Heat Map (1 of 3)

| Technique | Sub-technique | Technique | Sub-technique | Technique | Sub-technique | Technique | Sub-technique |
|---|---|---|---|---|---|---|---|
| Domain Accounts |  | Windows Command Shell |  | Domain Accounts |  | Domain Accounts |  |
| Valid Accounts |  | Local Accounts |  | Exploit Public-Facing Application |  | External Remote Services |  |
| Phishing |  | Default Accounts |  | Command and Scripting Interpreter | PowerShell | Windows Management Instrumentation |  |
|  |  |  |  | Unix Shell |  | Python |  |
|  |  |  |  | Visual Basic |  | JavaScript |  |
| Drive-by Compromise |  | System Services |  | Service Execution |  | Scheduled Task/Job | Scheduled Task |
|  |  |  |  |  |  | Cron |  |
| User Execution |  | Malicious File |  | Exploitation for Client Execution |  | Shared Modules |  |
| Software Deployment Tools |  | External Remote Services |  | Valid Accounts |  | Local Accounts |  |
| Valid Accounts |  | Local Accounts |  | Valid Accounts |  | Local Account |  |
| Server Software Component | Create Account | Account Manipulation |  | Scheduled Task/Job | Create or Modify System Process | Default Accounts |  |
| Web Shell | IIS Components | Local Account |  | Domain Account |  | Additional Email Delegate Permissions | SSH Authorized Keys |
| Scheduled Task | Cron | Windows Service | Systemd Service | Process Injection | Scheduled Task/Job | Create or Modify System Process |
| Exploitation for Privilege Escalation | Abuse Elevation Control Mechanism | Default Accounts | Process Hollowing | Dynamic-link Library Injection | Scheduled Task | Cron |
| Windows Service | Systemd Service | Bypass User Account Control | Sudo and Sudo Caching | Setuid and Setgid | Elevated Execution with Prompt | Boot or Logon Autostart Execution |
| Kernel Modules and Extensions | Registry Run Keys / Startup Folder | DLL Side-Loading | Hijack Execution Flow | DLL Search Order Hijacking | Dynamic Linker Hijacking | BITS Jobs |
| Event Triggered Execution | Boot or Logon Initialization Scripts | Accessibility Features | Image File Execution Options Injection | Component Object Model Hijacking | Windows Management Instrumentation Event Subscription | Logon Script (Windows) | Startup Items |
|  |  |  |  |  |  | Domain Policy Modification | Group Policy Modification |

---

# MITRE ATT&CK Heat Map (2 of 3)

| Technique | Sub-technique | Technique | Sub-technique | Technique | Sub-technique | Technique | Sub-technique |
|---|---|---|---|---|---|---|---|
| Domain Accounts |  | LSASS Memory |  | System Owner/User Discovery |  | Valid Accounts |  |
| Local Accounts |  | Security Account Manager |  | System Network Configuration Discovery | Internet Connection Discovery | Remote Desktop Protocol |  |
| SMB/Windows Admin Shares | Indicator Removal on Host | Default Accounts | File Deletion | Timestomp | Clear Windows Event Logs | Clear Linux or Mac System Logs | Clear Command History |
| Network Share Connection Removal | Disable or Modify Tools | OS Credential Dumping | /etc/passwd and /etc/shadow | Process Discovery | Remote Services | SSH |
| NTDS | DCSync | Bash History | System Information Discovery | Account Discovery | Domain Account | Local Account |
| File and Directory Discovery | Lateral Tool Transfer | Windows Remote Management | VNC | Distributed Component Object Model | Credentials In Files | Remote System Discovery |
| Exploitation of Remote Services | Unsecured Credentials | Private Keys | Credentials in Registry | System Network Connections Discovery | Permission Groups Discovery | Remote Service Session Hijacking | RDP Hijacking |
| Domain Groups | Local Groups | Use Alternate Authentication Material | Pass the Hash | Pass the Ticket | Disable or Modify System Firewall | Group Policy Preferences | Impair Defenses |
| Disable Windows Event Logging | Brute Force | Password Guessing | Network Service Discovery | Impair Command History Logging | Password Spraying | Domain Trust Discovery | Software Deployment Tools |
| Safe Mode Boot | Downgrade Attack | Password Cracking | Query Registry | Credentials from Password Stores | Windows Credential Manager | Software Discovery | Security Software Discovery |
| Obfuscated Files or Information | Compile After Delivery | Credentials from Web Browsers | Network Share Discovery | Indicator Removal from Tools | Match Legitimate Name or Location | Masquerade Task or Service | Rename System Utilities |
| Steal or Forge Kerberos Tickets | Kerberoasting | Golden Ticket | Keylogging | System Time Discovery | System Service Discovery | Group Policy Discovery | Input Capture |
| Credential API Hooking | Network Sniffing | Masquerading | Modify Registry | Steal Web Session Cookie | Double File Extension | Network Sniffing | Password Policy Discovery |
| System Location Discovery | Hidden Window | Exploitation for Credential Access | Peripheral Device Discovery | Hide Artifacts | Hidden Files and Directories | Adversary-in-the-Middle | ARP Cache Poisoning |
| File and Directory Permissions Modification | Process Injection | Deobfuscate/Decode Files or Information | Abuse Elevation Control Mechanism | Hidden Users | NTFS File Attributes | Linux and Mac File and Directory Permissions Modification | Windows File and Directory Permissions Modification |
| Process Hollowing | Dynamic-link Library Injection | Bypass User Account Control | Sudo and Sudo Caching | Setuid and Setgid | Elevated Execution with Prompt | DLL Side-Loading | Hijack Execution Flow |
| DLL Search Order Hijacking | Dynamic Linker Hijacking | Rundll32 | Regsvr32 | Mshta | System Binary Proxy Execution | Msiexec | MMC |
| Control Panel | InstallUtil | BITS Jobs | Access Token Manipulation | Create Process with Token | Token Impersonation/Theft | Trusted Developer Utilities Proxy Execution | MSBuild |
| Relective Code Loading | Indirect Command Execution | Use Alternate Authentication Material | Pass the Hash | Pass the Ticket | Rootkit | Domain Policy Modification | Group Policy Modification |

---

# MITRE ATT&CK Heat Map (3 of 3)

| Technique | Sub-technique | Technique | Sub-technique | Technique | Sub-technique | Technique | Sub-technique |
|---|---|---|---|---|---|---|---|
| Archive Collected Data | Archive via Library | Web Protocols | Ingress Tool Transfer | Exfiltration Over C2 Channel | Data from Local System | Application Layer Protocol | File Transfer Protocols |
| Exfiltration Over Alternative Protocol | Local Data Staging | DNS | Exfiltration Over Unencrypted Non-C2 Protocol | Exfiltration Over Asymmetric Encrypted Non-C2 Protocol | Exfiltration Over Symmetric Encrypted Non-C2 Protocol | Exfiltration Over Web Service | Exfiltration to Cloud Storage |
| Non-Standard Port | Protocol Tunneling | Data Transfer Size Limits | Exfiltration Over Other Network Medium | System Shutdown/Reboot | Data Destruction | Data Manipulation | Stored Data Manipulation |
| Data Staged | Data from Information Repositories | Data from Network Shared Drive | Input Capture | Screen Capture | Automated Collection | Adversary-in-the-Middle | ARP Cache Poisoning |
| Keylogging | Credential API Hooking | Proxy | External Proxy | Internal Proxy | Multi-hop Proxy | Standard Encoding | Non-Standard Encoding |
| Bidirectional Communication | One-Way Communication | Non-Application Layer Protocol | Data Encoding | Web Service | Data Obfuscation | Encrypted Channel | Symmetric Cryptography |

Figure 5. MITRE ATT&CK heat map showing the techniques and sub-techniques observed by OverWatch in interactive intrusion attempts from July 1, 2021, to June 30, 2022

---

# Looking Back
## Adversary Trends

Understanding trends in past adversary behavior is key to formulating an effective and proactive defense into the future. Looking back over the past year, several trends stand out to OverWatch threat hunters.

There was a continued shift from malware use, with malware-free activity accounting for 71% of all detections indexed by CrowdStrike Threat Graph®. This is related, in part, to adversaries’ prolific abuse of valid credentials to facilitate access and persistence in victim environments. Another contributing factor is the rate at which new vulnerabilities are being disclosed and the speed with which adversaries are able to operationalize exploits. Many organizations are finding themselves behind the 8-ball, unable to keep up with the pace at which these new threats are emerging. Rather than looking for fires, defenders need to learn to smell the smoke — to search for patterns of post-exploitation activity, which is proven effective in detecting early evidence of threats stemming from both known and unknown vulnerabilities.

As part of the ongoing effort to understand the behaviors of adversaries, OverWatch has been closely tracking the diversification of ransomware affiliates’ tradecraft. In particular, the LockBit RaaS program has attracted a vast array of affiliates. This report shares the details of four distinct LockBit intrusions uncovered last year by OverWatch, providing insights into the commonalities and differences in adversary tradecraft that can exist around a single piece of malware.

The final part of this section examines some of the tools that OverWatch encountered over the past year. This starts with a look at emerging tools that, though not highly prevalent across our data set, offer clues into where adversaries are turning their attention. Next is an exploration of trending tools that defenders should watch for as they have been commonly observed in OverWatch’s data set. Finally, the report looks at the tools that have become mainstays of the adversary toolkit.

---

# Looking Beyond the CVE

The number of zero-days and newly disclosed CVEs continued to rise year-over-year; concurrently, the time narrowed between the disclosure of these vulnerabilities and active exploitation attempts being observed in the wild.⁶

Organizations worldwide are grappling with a seemingly limitless onslaught of new vulnerabilities. Many organizations get caught in a reactive cycle of putting out the fires of individual vulnerabilities in the short term, while failing to adequately address the risks of these vulnerabilities in the long term. As a result, legacy vulnerabilities often remain unpatched, leaving organizations susceptible to exploit chaining in which adversaries combine newly publicized vulnerabilities with older, overlooked exploits.

While this situation may seem insurmountable, defenders have one very important fact on their side: Adversaries frequently adhere to common patterns of post-exploitation tradecraft. Threat hunters are therefore able to uncover malicious activity regardless of the initial access vector, effectively disarming the CVE or zero-day exploit.

Never before has it been more important for defenders to pivot from focusing on assessing and improving detection and mitigation capabilities to seeking proactive hunting solutions capable of addressing threats at scale.

⁶ The CrowdStrike 2022 Global Threat Report detailed Chinese actors’ exploit-acquisition capabilities, particularly against Microsoft Exchange vulnerabilities and other enterprise software hosted on internet-facing servers. For more information about the China-nexus vulnerability exploitation view, see the [CrowdStrike 2022 Global Threat Report](https://www.crowdstrike.com/resources/reports/crowdstrike-global-threat-report/).

## New CVEs, Same Old Tricks

The number of new vulnerabilities reported in 2021 exceeded 20,000, surpassing any previous year.⁷ There is no sign of this abating in 2022, with over 10,000 new vulnerabilities reported as of the start of June 2022. While the specific vulnerability exploited varies, the post-exploitation tradecraft and behaviors observed by OverWatch often remain similar.

Examining the tactics, techniques and procedures (TTPs) deployed during hands-on intrusions reveals common patterns of activity. Successful exploitation is routinely followed by the deployment of web shells, which are subsequently used to conduct discovery operations, harvest credentials, and retrieve and execute remotely hosted tooling.

Timely and comprehensive patching continues to play a crucial role in preventing successful exploitations. However, this solution is not always immediately available to defenders, particularly in the case of unknown or very recently disclosed CVEs. Augmenting robust security hygiene practices with around-the-clock hunting shifts the defensive mindset from chasing individual vulnerabilities to identifying known bad behaviors. This provides security teams with a vital advantage in the ability to identify and disrupt hands-on activity associated with the exploitation of unpatched or as-yet-unknown vulnerabilities.

## Outpacing the Zero-Day with Proactive Hunting

On June 2, 2022, a newly discovered Confluence vulnerability, allowing unauthenticated remote code execution (RCE) on a compromised host, was publicly disclosed. Proof of concept (POC) code quickly emerged, alongside public reporting noting active exploitation attempts from both criminally motivated and targeted intrusion actors.

⁷ For data on the distribution of vulnerabilities over time, see the National Vulnerability Database: [https://nvd.nist.gov/general/visualizations/vulnerability-visualizations/cvss-severity-distribution-over-time](https://nvd.nist.gov/general/visualizations/vulnerability-visualizations/cvss-severity-distribution-over-time)

While defenders scrambled to mitigate the risks of this CVE in the absence of an immediate patch, OverWatch for several days had already been notifying victim organizations of observed malicious activity consistent with a web service compromise, providing them with the actionable context needed to disrupt the adversary. In late May 2022, approximately one week prior to the vulnerability disclosure, OverWatch began observing hands-on malicious activity on Linux hosts at entities spanning numerous industry sectors including technology and academia. This activity included web shell deployment, interactive reconnaissance, attempted credential harvesting and the retrieval of remotely hosted tooling. By virtue of OverWatch’s focus on hands-on, post-exploitation behaviors rather than hunting specific CVEs, impacted organizations were provided with actionable and timely context that allowed for early disruption of the adversary activity. This is a clear illustration of how behavior-based proactive hunting provides earlier and more comprehensive coverage than more targeted efforts to mitigate CVEs as they come to light.

## Bad Things Come in Threes

As seen above, adversaries are quick to exploit new vulnerabilities, but they are equally eager to capitalize on vulnerabilities that persist as a consequence of patching delays.

As part of the prolonged targeting of Microsoft Exchange servers over the last year, OverWatch observed adversary use of exploit chaining. Of note is the ProxyShell exploit chain in which three discrete CVEs (CVE-2021-34473,⁸ CVE-2021-34523⁹ and CVE-2021-31207¹⁰) are chained to achieve RCE capabilities, escalate privileges and enable authentication bypass on vulnerable systems. The practice of exploit chaining enables adversaries to reach their objectives quickly, allowing them to outmaneuver defenders that continue to focus on reactively mitigating individual vulnerabilities. Such an approach does little to curtail a determined adversary that will simply pivot if one exploit attempt proves unsuccessful.

⁸ For more information on this vulnerability, see: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34473](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34473).
⁹ For more information on this vulnerability, see: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34523](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34523).
¹⁰ For more information on this vulnerability, see: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-31207](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-31207).

Notably, while the ProxyShell vulnerabilities were disclosed in the first half of 2021, OverWatch has continued to observe numerous instances of attempted exploitation deep into 2022. It is telling of the defensive challenges facing organizations that even 12 months on, adversaries continue to have success with older, widely publicized and patchable exploits.

Specifically, the ProxyShell exploit chain has been leveraged by both eCrime and state-nexus actors, including CARBON SPIDER and NEMESIS KITTEN, respectively. These intrusion attempts were carried out against entities operating across a range of industry verticals including government, healthcare, and manufacturing and spanning multiple regions. However, looking more closely at the post-exploitation behavior again revealed a common combination of adversary techniques, as shown in the image below:

*   **Initial Access**: MS Exchange exploitation
*   **Execution**: PowerShell
*   **Persistence**: Web shell deployment
*   **Defense Evasion**: Disabling Windows Defender and masquerading malicious binaries
*   **Credential Access**: A variety of credential dumping techniques
*   **Discovery**: Exchange enumeration and host reconnaissance
*   **Command & Control**: Retrieval and deployment of actor tooling from remote locations
*   **Lateral Movement**: Lateral movement between multiple hosts using SSH, RDP and WMI

The image below further illustrates the post-exploitation behavior:

*   **Collection**: Use of unique keylogging and screen capture tooling for input capture
*   **Initial Access**: Use of a collection of valid and backdoored accounts on Linux and Windows hosts
*   **Discovery**: Host and user reconnaissance conducted, including enumeration of domain group and host information
*   **Credential Access**: Numerous credential dumping and harvesting techniques employed, inducing sensitive file enumeration, use of disguised keyloggers and a distinctive screen capture tool
*   **Defense Evasion**: Use of disguised and renamed actor tooling and anti-forensic techniques, and attempts to weaken host security posture
*   **Lateral Movement**: Lateral movement between multiple hosts using SSH, RDP and WMI

## Action Items for Defenders

*   **Invest in scalable defense solutions that allow your organization to look beyond the CVE or zero-day.** As we look to the end of 2022 and beyond, the profusion of CVEs and their rapid exploitation by adversaries is a trend that shows no signs of slowing. It is no longer feasible for defenders to tackle these vulnerabilities in isolation, nor advisable to ignore them in aggregate. Organizations must adopt a security solution that can scale effectively. Threat hunting offers this solution, keeping organizations informed of active threats to their security by focusing on the post-exploitation behaviors that remain constant rather than vulnerabilities that remain in flux.

---

# LockBit and Its Technicolor Affiliate Program: How One RaaS Offering Has Spawned Diverse Tradecraft

Verticals Impacted by LockBit from July 1, 2021, to June 30, 2022:
* Retail
* Healthcare
* Transportation and Logistics
* Academic
* Manufacturing
* Professional Services
* Telecommunications
* Technology

The proliferation of eCrime activity has been a constant theme over the last several years. The growth of the eCrime ecosystem is characterized by a vast array of threat actors and the rapid innovation in adversary tradecraft designed to maximize profits. As a result, threat hunters now more than ever need to be familiar with a diverse range of adversary tradecraft and expect the unexpected.

Ransomware as a service (RaaS) affiliate models have exacerbated this situation. There is a common misconception that ransomware events follow a single pattern. In reality, different affiliate groups often use distinct tradecraft to deploy the same tooling. This makes threat hunters’ job of identifying early stages of ransomware preparation more complex, requiring awareness of a vast array of intrusion tactics and methodologies leveraged by affiliates.

To demonstrate exactly how the strategy of different affiliates can vary, the following analysis examines four distinct LockBit intrusions from last year. Because of its popularity and reputation, LockBit has an extensive affiliate program. Each case study details the notable TTPs used by affiliates and highlights key similarities and differences, providing security teams with insight into the operational effort of tracking today’s diverse eCrime adversaries and the additional controls that should be applied to mitigate against observed tradecraft. While not explicitly called out in each intrusion case study, readers should note that, when correctly configured, the Falcon platform will prevent the execution of the LockBit and StealBit binaries.

The intrusions discussed here impacted organizations in the retail, healthcare, and transportation and logistics industry verticals.

LockBit was one of the most prolific ransomware families over the last year, measured both by activity on their dedicated leak site and by OverWatch data on interactive intrusion campaigns. OverWatch also observed LockBit in other sectors including academia, manufacturing, professional services, telecommunications and technology.

## Scenario 1: VPN Compromise and Tools-A-Plenty

In Q3 2021, OverWatch observed an interactive intrusion stemming from a compromised VPN appliance. The LockBit affiliate leveraged a valid user account to begin ransomware preparation activity.