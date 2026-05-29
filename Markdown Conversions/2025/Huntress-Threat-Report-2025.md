# 2025 Cyber Threat Report

## Table of Contents
- [Executive Summary](#executive-summary)
- [The 2024 Threat Landscape](#the-2024-threat-landscape)
- [Attack Breakdown by Industry](#attack-breakdown-by-industry)
  - [Healthcare Sector Threats](#healthcare-sector-threats)
  - [Technology Sector Threats](#technology-sector-threats)
  - [Education Sector Threats](#education-sector-threats)
  - [Government Sector Threats](#government-sector-threats)
  - [Manufacturing Sector Threats](#manufacturing-sector-threats)
- [Ransomware In 2024](#ransomware-in-2024)
  - [Ransomware Groups](#ransomware-groups)
  - [Time-To-Ransom (TTR) Measurement](#time-to-ransom-ttr-measurement)
  - [Activity Before Ransom](#activity-before-ransom)
- [Attacker Tools and Techniques](#attacker-tools-and-techniques)
  - [Hacking Tools](#hacking-tools)
  - [Remote Access Trojans](#remote-access-trojans)
  - [RMM Abuse](#rmm-abuse)
- [Exploit-Driven Campaigns in 2024](#exploit-driven-campaigns-in-2024)
  - [ScreenConnect Exploitation (CVE-2024-1709 & CVE-2024-1708)](#screenconnect-exploitation-cve-2024-1709--cve-2024-1708)
  - [CrushFTP Exploitation (CVE-2024-4040)](#crushftp-exploitation-cve-2024-4040)
  - [ProxyShell Exchange Exploitation (CVE-2021-31207)](#proxyshell-exchange-exploitation-cve-2021-31207)
- [MITRE ATT&CK Phases](#mitre-attck-phases)
  - [Scripting Abuse](#scripting-abuse)

---

## Executive Summary

Last year, threat actors were prolific. They showed remarkable adaptability and used more sophisticated tools, tactics, and techniques across industries like healthcare, technology, education, government, and manufacturing. The gap between sophistication in attacks on large enterprises and smaller businesses has narrowed—in fact, it’s all but disappeared. Attackers are taking the methods and strategies they’ve tested on larger organizations and are standardizing them across businesses of all sizes to maximize efficiency. Advanced methods like defense tampering, bring your own vulnerable driver (BYOVD) privilege escalations, and UAC (User Account Control) bypasses have become the norm, underscoring the urgent need for comprehensive defenses, proactive patching, and enhanced endpoint monitoring.

This report gives a detailed analysis of key adversarial behaviors, techniques, and trends we saw in 2024, highlighting the escalating risks that non-enterprise businesses and managed service providers (MSPs) need to be aware of. This analysis will empower organizations of all sizes to strengthen their defenses against modern cyber threats by giving them actionable insights into a constantly evolving threat landscape.

Recent takedowns of ransomware groups like Hive, Dharma/Crysis, Phobos, and the partial disruption of LockBit have fragmented ransomware groups into smaller, more agile affiliate networks like RansomHub and INC/Lynx. These affiliates have attracted hackers by offering significantly higher payouts, often reaching 80–90% of the ransom paid out. Meanwhile, ransomware strategies are shifting as detection improves, with groups like BianLian focusing on data theft and extortion rather than data encryption. We believe this strategy will continue to evolve, highlighting the value of data loss prevention, network monitoring, and awareness.

Abuse of remote access trojans and RMMs (e.g., AsyncRAT, Jupyter, NetSupport, and Trickbot), administrator tools like SysInternals Suite, and LOLBins like rdrleakdiag or netsh were still widespread in 2024. Scripting languages like PowerShell, VBScript, and JavaScript were heavily exploited for malicious code execution, persistence, and lateral movement. While comprehensive hacking tool suites like Cobalt Strike saw a decline in use, specialized tools like Mimikatz and CrackMapExec continued to be abused globally. Additionally, opportunistic exploitation of software vulnerabilities and the abuse of remote monitoring and management (RMM) tools emerged as critical risks, which helped attackers compromise large numbers of machines in a short time.

## The 2024 Threat Landscape

In 2024, cybercriminals leveled up their game, using smarter tactics and turning everyday tools into weapons. Drawing from extensive monitoring of thousands of organizations and millions of endpoints, we’ve identified several critical trends that shaped the cybersecurity environment in 2024 and will carry into 2025:

- **Proliferation of Remote Access Trojans (RATs)**: Over three-quarters of remote access incidents involved RATs like AsyncRAT, NetSupport, and Jupyter.
- **Shifts in Ransomware Strategies**: A focus on data theft and extortion over encryption emerged, as groups like BianLian, RansomHub, and Akira targeted businesses with high affiliate payouts.
- **Increased Exploitation of Remote Monitoring and Management (RMM) Tools**: Attackers abused RMM tools like ConnectWise ScreenConnect, TeamViewer, and LogMeIn to gain access, move laterally, and maintain persistence.
- **Sophisticated Use of “Living Off the Land” Techniques**: Adversaries relied more and more on legitimate administrative tools like Sysinternals Suite and LOLBins for evasion and persistence and relied less on malicious executables.
- **Rising Phishing Sophistication**: Techniques like QR code phishing, image-based content, and brand impersonation exploited user trust and bypassed traditional email filters.

![Frequency of Threats Overall chart showing Infostealer at 24%, Malicious Script at 22%, Malware at 17%, RAT at 13%, Ransomware at 9.5%, RMM Abuse at 6.5%, Hacking Tool at 4%, and Lateral Movement at 4%.]

## Attack Breakdown by Industry

Attackers targeted a wide range of industries throughout 2024, with healthcare and education being targeted the most, followed by significant activity against technology, manufacturing, and government sectors.

![Industries targeted by percentage in 2024: Education 21%, Healthcare 17%, Government 11%, Manufacturing 9%, Technology 12%, Other 30%.]

### Healthcare Sector Threats

In healthcare, the biggest risk throughout the industry in 2024 was malicious script executions. These were primarily scripts being abused for persistence like Javascript components of malware, downloaders, and system analysis components.

![Healthcare threats by type: Malicious Script 22%, Infostealer 19%, Malware 16%, Other 11%, RMM Abuse 9%, Ransomware 8%, RAT 7%, Hacking Tool 4%, Lateral Movement 4%.]

### Technology Sector Threats

In the technology sector, we saw attackers shift their strategies to use different tools and mechanisms utilized by employees to blend into networks. Most notable is the abuse of RMM tools to either gain access or move laterally within the network.

![Technology threats by type: Malicious Script 19%, Infostealer 18%, Malware 14%, RMM Abuse 14%, RAT 9%, Ransomware 8%, Hacking Tool 6%, Lateral Movement 6%, Other 6%.]

### Education Sector Threats

Education-based environments face similar threats to the healthcare industry; however, malicious scripts are the most-identified threat detected in these environments.

![Education threats by type: Malicious Script 24%, Infostealer 16%, Other 14%, Malware 13%, RMM Abuse 13%, Ransomware 7%, RAT 6%, Lateral Movement 4%, Hacking Tool 3%.]

### Government Sector Threats

Government environments were targeted at high rates in 2024, with most detected attempts being information-stealing components, downloaders/persistence mechanisms, and RATs.

![Government threats by type: Infostealer 21%, Malicious Script 18%, Malware 16%, RAT 10%, RMM Abuse 9%, Other 9%, Lateral Movement 8%, Ransomware 5%, Hacking Tool 4%.]

### Manufacturing Sector Threats

The last industry we analyzed was manufacturing, and this was a unique environment based on the data we saw for 2024. We saw a high number of RAT installations in these environments.

![Manufacturing threats by type: Malware 17%, Infostealer 15%, Malicious Script 15%, RAT 13%, RMM Abuse 12%, Hacking Tool 8%, Other 8%, Ransomware 6%, Lateral Movement 6%.]

## Ransomware In 2024

In late 2023 and early 2024, ransomware operations faced significant disruption due to global collaboration among cybersecurity groups, law enforcement, and private researchers.

### Ransomware Groups

The dirty business of ransomware became a tumultuous year for operators as global cybersecurity groups, law enforcement, government agencies, and private researchers came together throughout the year to bring down several notable ransomware groups.

![Top Ransomware Operators chart showing RansomHub at the top with 21%.]

### Time-To-Ransom (TTR) Measurement

During the year, Huntress investigated incidents where ransomware was deployed and crawled through activity logs to determine the ransomware operator’s initial access time.

![Average TTR by ransomware group chart showing Rapid at 43.42 hours and Play at 4.22 hours.]

### Activity Before Ransom

Another measure we looked at was how many actions groups performed before triggering a ransomware payload. These were the number of actions we were able to identify in a 48-hour window before attempting to deploy ransomware on the victim’s machine.

![Activity prior to ransomware deployment by group chart showing Phobos at 37 actions and Play at 8 actions.]

## Attacker Tools and Techniques

In 2024, hackers relied heavily on specialized tools and techniques to automate tasks, gain access, and maintain control over compromised systems.

### Hacking Tools

When compromising machines en masse, hackers will automate many tasks as quickly as possible to attempt to gain access during the window of opportunity they have.

![Hacking tool usage in 2024: Cobalt Strike 31.7%, Mimikatz 17.6%, Sysinternals 17.1%, Advanced IP Scanner 10%, Metasploit 7.9%, Hack Tool Other 6.1%, PowerSploit 2.7%, Atomic Red Team 2.6%, Network Scanner Other 2.4%, Empire 2.3%, Bloodhound 1.1%, SharpDump 0.1%, CrackMapExec 0.1%.]

### Remote Access Trojans

Remote access trojans, also known as RATs, let hackers remotely operate and control compromised systems as if they were sitting in front of these devices.

![Remote access trojan frequency in 2024: Generic RAT 56.1%, NetSupport RAT 12.5%, AsyncRAT 11.1%, Trickbot RAT 8.8%, Jupyter RAT 8.8%, NewCore RAT 0.8%, JRAT 0.8%, CinaRAT 0.7%, BitRAT 0.4%.]

### RMM Abuse

Similar to 2023, hackers have continued to abuse existing commercial tools to remotely gain access to compromised devices.

![Top Abused Remote Access Tools: ConnectWise (ScreenConnect) 74.5%, RDP 14.6%, LogMeIn 4.7%, TeamViewer 4.4%, Atera 0.7%, VNC 0.6%, NinjaRMM 0.4%.]

## Exploit-Driven Campaigns in 2024

Traditional exploitation of CVEs to gain initial access or move laterally in non-enterprise environments is very different from enterprise and other verticals.

### ScreenConnect Exploitation (CVE-2024-1709 & CVE-2024-1708)

The most notable event involving RMM abuse in 2024 was a campaign targeting CVE-2024-1709 & CVE-2024-1708—which Huntress coined SlashAndGrab—to exploit ScreenConnect installations in February.

![ScreenConnect exploitation from January to October 2024 graph showing a massive spike in February.]

### CrushFTP Exploitation (CVE-2024-4040)

In addition, CVE-2024-4040, which exploits a zero day authentication bypass in CrushFTP, was used by attackers to steal credentials and gain access to these systems.

### ProxyShell Exchange Exploitation (CVE-2021-31207)

We saw several campaigns focusing on targeting the Microsoft Exchange vulnerability CVE-2021-31207 to execute elevated to gain launch webshells from mailbox servers.

![ProxyShell exploitation campaigns during early 2024 graph.]

## MITRE ATT&CK Phases

At Huntress throughout 2024, we excelled in catching attackers during the execution phase (TA0002), which is where attackers must execute their payloads to perform devious actions on a vulnerable host.

![MITRE ATT&CK phase where Huntress detection occurred: Execution 65.5%, Persistence 15.5%, Defense Evasion 8.6%, Lateral Movement 5.2%, Privilege Elevation 2.9%, Credential Access 2.3%.]

### Scripting Abuse

Once they’ve gained access to a system, attackers perform a wide range of initial tasks and other malicious activities to prepare the system for further compromise.

![Scripting Language Abuse: PowerShell 45%, Javascript 15.6%, Batch File 14.7%, VB Script 6.3%, Python 3.9%, WMI 3%, MSHTA 2.9%, Wscript 2.5%, Java 2.5%, MSIX 1.5%, PHP 1.3%, Scripting Other 0.9%, Lua 0.1%.]

---

tion�
Figure 27: Scripting abuse techniques used in 2024
We saw this method in attempts to create
user accounts or perform network and domain
reconnaissance before lateral movement events�
Compared to corporate environments where
Python abuse is more common, it was only
seen 3�9% of the time; however, it was still more
common than Windows Scripting Host, WMI, and
MSHTA abuse over the year� These languages
were once major sources of exploitation
five years ago but have all fallen out in favor
of PowerShell due to planned legacy and
reduced support�
45

Once common across workplace environments, these languages are now signs
of compromise and attackers have adapted accordingly� However, there are
still malware families and hacking groups that still use them to this day� The
Ursnif info stealer family still employs MSHTA files as a method for both execution
and persistence�
WMI instances originated primarily from persistence methods of Crypto miners, and
a few PUP toolkits still refuse to migrate to newer scripting languages� Another usage
of WMI is being used for reconnaissance and system information gathering� Very few
groups are still using WMI for file execution, a typical pivoting method abused during
the Office macro exploitation days�
WScript�exe, which is Windows Script Host, can be a wide range of scripting
languages like VBS, WSH, JScript (not to be confused with Javascript) and is still
implemented by many malware families� A few variants of AsycRAT were the
primary source of WScript that we encountered throughout 2024�
45%
of attacks utilized
PowerShell as the scripting
language
8.4%
of scripting abuse
incidents involved MSHTA,
WMI, and WScript
46

MITRE ATT&CK Phases
Persistence Persistence Methods
Mechanisms Registry Run Keys
41.2%
Regsvr32
16.7%
Our second-most established area of countering
infection is identifying persistence mechanisms
(TA0003)� A majority of this detection came the IFEO
8.9%
minute Huntress was installed on an endpoint—
often identifying overlooked incidents that
existed on the host before our agent was Autoruns
7.9%
installed� Persistence still comes in many forms
today, from autorun executions, service abuse,
DLL hijacking, to COM object manipulation, and Rundll32
6.4%
scheduled tasks�
Attackers targeting businesses aren’t typically
Scheduled Tasks
5.8%
using advanced methods of persistence as
methods that are nearly 20 years old are still
working just fine for them�
SvcHost
2.7%
Typical Registry Run keys and AutoRun entries
are the two most common strategies attackers
COM Hijack
are using to survive reboots—they’re choosing 2.7%
these nearly five out of ten times� Methods
involving COM installation via RegSvr32 or
Userinit
COM Hijacking are nearly 20% of all persistent 1.9%
mechanisms encountered during 2024�
Image File Execution Options (IFEO) injections Start Menu
1.5%
were a surprisingly common method and also
doubled as a way to disable some EDRs—both
of which found their way in several common Winlogan
1.2%
malware families like SunBurst and SDBot for
installation of secondary components�
Process Hijack
0.6%
Exotic persistence mechanisms like targeting
Windows Active Setup subsystems and SSP
injections were attempted during the year as
DLL Hijack
0.4%
well� The SSP method is most often associated
with PowerSploit attacks, while Active Setup
is an ancient method dating back to PoisonIvy
BITS
days nearly 14 years ago� 0.3%
Logon Scripts
0.1%
Figure 28: Vectors for maintaining persistence used in 2024
47

MITRE ATT&CK Phases
Credential Credential Dumping
Methods
Access
Misc
28.1%
Once they gain a foothold into a system, Mimikatz
26.9%
attackers will often scour memory, processes,
files, and other data locations to access login
credentials� Throughout the year, hackers LOLBin
19.3%
achieved this primarily by using Mimikatz,
generic malware, or hacking tools to access
system credentials� These made up over half LSASS
8.1%
the number of incidents we saw involving
credential access�
WDigest
4.9%
Both PowerDump and PowerSploit give
attackers using PowerShell the ability to harvest
credentials in memory or actively intercept them PowerSploit
4.2%
using Kerberoasting or other methods�
Following Mimikatz, attackers would often
NTDS
4.1%
use LOLBins to gain access to credentials; this
proved to be the case 19�3% of the time� We saw
quite a few different LOLBins abused in 2024 to
Lazagne
3.4%
access credentials, with the majority of attempts
originating from ProcDump, NTDSUtil, Cmdkey,
Reg SAM dumps, and ComSvcs�
PowerDump
0.9%
Figure 29: Credential dumping methods used in 2024
48

LOLBin Credential Dumping Usage
25
20
15
10
5
0
Findstr Impersonate CmdKey Reg SAM RPCPing RDRLeakDiag DiskShadow ProcDump INTDSUtil Dump64 CreateDump Comsvcs Adplus
Figure 30: LOLBin credential dumping frequency in 2024
49

MITRE ATT&CK Phases
Defense Evasion
Surprisingly enough, nearly 9% of attackers who
tried to be stealthy and evade defenses got burned�
Many of the environments we’re looking at don’t
have the complex running environments many
large corporations have—so attackers trying to
blend in are actually sticking out� Attackers often
use scrambled and obfuscated command lines,
encrypted scripts, mangled filenames, or corrupted
registry entries to hide from users� We focus on
Defense evasion attempt
these oddities and have turned them from evasive
maneuvers to indicators of compromise, thus using
attackers’ tactics against them�
Further breaking these down, we see that attackers
targeting business environments are still using most
of the same mechanisms that we see in the wild�
Extract from a Huntress Process Insights detection
Because few attackers tailor their kits for non- for commodity malware attempting and failing to use
enterprise environments, this plays out in our favor PowerShell obfuscation to evade defenses
for detection at this phase�
Defense Evasion Techniques
Registry Obfuscation 6.2% 6.8% Security Bypass
Obfuscated Command 27.4%
59.6% File Obfuscation
Figure 31: Initial defense evasion techniques used in 2024
50

File name obfuscation like impersonating other files, unicode tricks, double
extensions, and similar visual methods were the main methods we saw attackers use
trying to blend in� This accounted for 55�7% of evasive maneuvers we saw in 2024�
These tactics are often used for social engineering purposes more than traditional
evasion of detection mechanisms or applications�
Obfuscated commands come in second, with 27�4% occurrence during the year�
While this may seem like a bread-and-butter tactic for most malicious tools,
attackers may not implement these against businesses, or their actions were caught
before getting to the stage of command line execution� Huntress saw the vast
majority of obfuscated command line abuse originating from PowerShell scripting
command lines with Windows Command Shell as secondary�
One of the most common evasion techniques we saw in 2024 was Registry Null Byte
insertion—this is often a tactic used by many RAT families like Jupyter to evade string
searching within REG_SZ, REG_MULTI_SZ, REG_EXPAND_SZ data types� This tactic
was used in almost 40% of all evasion methods we saw throughout the year�
55.7%
of evasive
maneuvers used file
name obfuscation
40%
of all evasion
methods used Registry
Null Byte insertion
51

MITRE ATT&CK Phases
Security Bypasses
Attackers generally focus on two categories of defense bypass techniques: indirect
methods like downgrading security by modifying settings or bypassing UAC, and
direct methods like targeting EDR defenses� These approaches are becoming more
common as malware authors and hacking tool developers strive to stay competitive
by incorporating them as standard features� While the more advanced and
sophisticated techniques are usually reserved for high-end malware and toolkits,
Huntress has seen a growing trend of these methods being deployed against non-
enterprise targets� This trend is expected to escalate significantly in 2025�
UAC bypasses and other security downgrade tactics have long been a staple for
sophisticated attackers� These methods and strategies, once used only by APTs
years ago, have made their way into mainstream malware families and common
ransomware operators’ toolkits� These methods introduce flaws in processing or
thresholds of how defenses operate without actively disabling EDR processes
themselves� These methods are often more subtle and less effective than
direct methods�
The five most common methods Huntress saw during 2024 are illustrated in Figure 32�
Security Bypass Methods
40%
30%
20%
10%
0%
Disabling via LOLBin COM Object DLL Hijacks Scheduled Task
Registry Abuse Abuse and Sideloads Hijacking
Figure 32: Indirect security bypass methods used in 2024
52

An attacker who successfully disables, hinders, or
disrupts a victim’s EDR can significantly impact the
outcome of an attack� This creates a critical window
for executing normally detectable payloads like
mass file encryption, critical system modifications, or
accessing protected processes and monitored data� To
achieve this, attackers use a range of techniques, from
simple registry modifications to using malicious third-
party drivers that elevate privileges and disable EDR
functionality� In 2024, we saw diverse levels of activity
related to EDR tampering, with attackers using various
methods to achieve their objectives�
The trend of EDR disabling and tampering reached
its peak in July, when many ransomware groups and
RAT malware families began bundling EDR bypass
mechanisms� During the year, we witnessed EDR being Extract of a batch script Huntress identified during an
attacked in 3�6% of all incidents� While this number intrusion, manipulating the Windows Registry and installing
drivers to bypass security defenses
may seem small, this trend lines up well with media
coverage of EDR bypass techniques and the malware
that delivered them� Coincidence? Not likely�
Monthly EDR Tampering by Method
25
20
15
10
5
0
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
File Tampering Registry Modification Driver Abuse Malicious Scripts
Elevated Process Exclusion Modification LOLBin Abuse Monthly Trend
Figure 33: Monthly occurrences of EDR tampering techniques
53

We also saw new breakout methods emerge and be used against customers in 2024�
Primarily, we saw attackers using driver BYOVD exploitation with Truesight, Process
Explorer (AUKill), and HRSword being the three main culprits� This method was used
extensively in the summer for ransomware and RAT variants to disable third-party
defenses and other protected processes� By October, this method died down, but by
the end of 2024, we saw a resurgence of this strategy and believe this will continue in
RATs and ransomware as a standard feature moving into 2025 and beyond�
An interesting find during investigating BYOVD abuse goals throughout 2024 was
the separation of privilege elevation versus EDR tampering� With typically less
sophisticated EDRs installed in non-enterprise environments, Huntress noticed that
over 90% of BYOVD usages were to elevate privileges in order to execute ring 0 code
and gain complete control of a system in order to remain persistent instead of merely
tampering or disabling EDR� This likely is a reflection of less sophisticated defense
mechanisms in place for most of these non-enterprise environments preventing these
attackers from full system compromise� But as we see more of these environments
adopt security software, these numbers will likely shift to more attackers requiring an
EDR tampering phase to be successful�
Search Volume of EDR Bypass Methods
EDR Bypass EDR Killing Malware
30000
20000
10000
0
Jan Feb Mar Apr May Jun
Figure 34: Google search hits pertaining to EDR bypass and malware-killing EDR
54

Driver Abuse Strategies
9.5% EDR Tampering
Privilege Elevation 90.5%
Figure 35: Driver abuse in the wild - EDR tampering vs� privilege elevation usage
Another novel use we saw in 2024 was the abuse of System Settings Admin Flows, which
incorporates a known LOLBin to disable EDRs� This was often seen in conjunction with the
INC (now Lynx) ransomware group and was discovered by Huntress in April� Other LOLBin
abuse to disable EDR involves modifying binaries, abusing installers, or removing protected
processes by abusing EDR tools themselves� In July, we saw a resurgence of this strategy that
mimicked the INC ransomware strategy and incorporated tools to abuse a LOLBin writeup
from November 2023�
The most common methods we saw in 2024 that involved disabling EDRs and other security
settings were from four sources: registry modifications, file tampering, killing from an
elevated process, or the use of malicious scripts to tamper defenses� These combined made
up 88% of all methods attempted throughout the year�
Usage of these tools appeared to align with overall EDR tampering trends� We did notice that
during the months where more sophisticated attacks weren’t being used, these older and
more primitive methods were deployed� This shows that hacking groups are influenced by the
news of emerging strategies and will often fall back to tried-and-true traditional methods
when new shiny methods aren’t working�
55

Monthly EDR Tampering by
LOLBins and Driver Abuse
25
20
15
10
5
0
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
LOLBin Abuse Driver Abuse
Figure 36: Monthly EDR tampering via LOLBin abuse vs� drivers in 2024
Monthly EDR Tampering by
Common Methods
20
15
10
5
0
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
Registry Medication File Tampering Elevated Process Malicious Script
Figure 37: EDR tampering by month via trivial methods
56

Third-Party EDR
Coverage
57

Third- EDR Coverage
SentinelOne
33%
Party EDR
BitDefender
16.9%
Coverage
Webroot
15.3%
Trend Micro
8.8%
Huntress has always
been about protecting all
Malwarebytes
5.4%
businesses, not just the 1%.
Sophos
As such, our EDR is often used alongside others 4%
to help protect businesses around the world
or deployed post-incident where another EDR
ESET
might have missed an event� Because of this, 3.5%
Huntress has a unique view on protections
being used in all sectors� In 2024, SentinelOne
Cylance
was present in 33% of all systems that had 2.4%
incidents during the year� BitDefender and
Webroot made up nearly another third of
CrowdStrike
all coverage that non-enterprise businesses 1.6%
choose to implement�
With cybersecurity becoming a must for AVG
1.2%
everyday business operations, EDR coverage
appears to be strong throughout the year� Not
taking Microsoft Defender into consideration,
Figure 38: Third-party EDR product coverage during 2024
91% of systems impacted by a cybersecurity
incident in 2024 had an EDR present at the
time� Of those, 7% had multiple third-party
EDR vendors installed to maximize protection�
This means only 9% of the systems impacted
decided to forgo their security posture and
didn’t have any EDR installed�
58

Of the 7% of multiple-vendor EDRs we saw, there were some noteworthy
combinations with two record-holders having four different vendor EDRs installed
simultaneously� We applaud the patience of the employees who were able to work
with so many agents simultaneously installed on their workstations!
Huntress is often deployed by MSPs and IT teams to identify and remediate systems
after a cybersecurity incident� In those cases, one of the first actions Huntress
performs is analyzing any existing footholds or evidence of prior persistence on
the system deployed� Analyzing the number of persistence methods still remaining
on these environments, in conjunction with their EDR configuration, shows the
effectiveness of modern-day EDR solutions�
EDR Protection at Start of Incident
Multiple EDRs 7%
No EDR 9%
84% Single EDR
Figure 39: Number of EDRs deployed during incidents in 2024
59

In scenarios where Huntress was deployed Persistence Remained Prior
post-incident and the environment had no
to Huntress Installation
EDR, we saw evidence of persistence (active
or otherwise) 78% of the time� This number
dropped dramatically for environments with
EDRs deployed: 21% for single EDR, and 14% 78% No EDR
for multiple EDRs�
Not taking into account attackers that were 21% Single EDR
fully removed from systems or made systems
inaccessible after these events, this could
14% Multiple EDR
potentially highlight the diminishing returns of
having multiple EDRs vs� a single solution�
As noted previously, attackers at all levels are
Figure 40: Persistence remaining by EDR
starting to use multiple levels of counterdefense configuration prior to Huntress install
that were exclusive to sophisticated and skilled
hackers only a few years ago� The reason for
this comes down to the competitive market
of malware-as-a-service (MaaS) and similar
development practices of hacking tools� Put
simply, these capabilities are no longer exclusive
to premium levels of malware, and hackers
have to use these to survive� At Huntress,
we constantly identify and use these new
technologies and techniques to have the best
possible defense regardless of business size,
sector, or industry�
60

Breaking Down
Hacker Activity
61

Breaking Down
Hacker Activity
Hands-On-Keyboard (HOK) Activity
Identifying patterns within signals helps us determine hacker behavior and trends�
In 2024, we wanted to be able to distinguish between attackers running automated
tools or scripts and when they were active or “hands-on-keyboard” (HOK)� Activity
like lateral movement, manual command execution, network reconnaissance
commands, file system scouring, and interactive shell payloads are all indicative
of HOK activity�
By tracking these events, we see when attackers were likely the most successful�
Usually, HOK activity signifies more sophisticated attackers and individuals who
perform more precise actions in the end phases of campaigns�
Interaction Type Breakdown by Month
Automated Hands-On-Keyboard
January
February
March
April
May
June
July
August
September
October
November
December
0% 25% 50% 75% 100%
Figure 41: Automated vs� HOK activity during 2024
62

Based on this analysis, we can conclude that HOK Activity in 2024
attackers were very active in attempting
exploitation and lateral movement in February,
June, July, and November 2024� Throughout the
Domain Enumeration
year, we saw most HOK activity revolve around 18.6%
reconnaissance, lateral movement, and custom
scripting or tool usage in environments—with
Lateral Movement
these 3 scenarios resulting in about half of the 17.0%
cases where HOK activity was observed�
While these usually involve a skilled attacker 14.1% Tool Execution
being active on a compromised machine, in
many cases, it led to the detection of suspicious
activity due to their commands� In 2024, we Credential Dumping
8.6%
saw more than 187 suspicious “whoami”
requests, username, or domain info requests,
Get-WMIObject username, or similar red flags Data Exfiltration
7.1%
that triggered investigations and burned the
attacker’s access�
Network Scanning
6.5%
Persistence Installation
5.6%
Malware Installation
5.5%
Defense Evasion
3.4%
HOK Activity by Month
New User Creation
3.3%
Jan
Dec Feb
Network Enumeration
3.3%
Nov Mar
Reverse Shell Activity
3.0%
User Enumeration
2.7%
Oct Apr
Figure 43: Type of HOK activity
Sep May
Aug Jun
Jul
Figure 42: HOK activity by month
63

Breaking Down Hacker Activity
Operational Timeframes
By mapping HOK activity by hourly occurrence, we can see the approximate times
hackers are most active� Based on our collected data, it appears that 12:00 UTC
through 20:00 UTC is when we encounter the most hands-on-keyboard activity
from attackers�
This timeframe lines up closely with US East Coast business times, which could
mean that attackers are active during these times to actively monitor victims’
activities or to hide their events and logged activities during normal business times�
Attackers may also need to be on active devices for network access or for social
engineering purposes�
Hands-On-Keyboard Activity %
12%
10%
8%
6%
4%
2%
0%
0 5 10 15 20
Hour (UTC)
Figure 44: Breakout of UTC time during HOK activity
64
%
KOH

Identity Threats
65

Identity Threats
In 2024, attacks on Microsoft 365 environments became more prevalent and
sophisticated, prompting Huntress to roll out new technology like attacker-in-the-
middle (AitM) detection in Q4 to address these emerging threats� Nearly half of all
detections during the year stemmed from access rule violations like attempts to
access resources from restricted VPNs or unauthorized geolocations� Additionally,
advancements in our browser activity monitoring helped detect suspicious
tooling, plugins, and spoofing techniques used by attackers to compromise cloud
infrastructure� These techniques, often a mainstay for targeting large corporations,
are becoming more available due to increased focus by attackers on these tools�
This appears to directly reflect the increased adoption rate that businesses and
environments are implementing these cloud resources�
ITDR Incident Frequency
Credential Theft 8%
Token Theft 5.4%
Malicious Application 30.3% VPN Rule Violation
Deployment 4.8%
Attacker-in-the-Middle
Attempt 1.9%
Inbox Rule Modification 9.2% Suspicious Browser Data
25.4%
15.1% Location Rule Violation
Figure 45: Identity threat detection and response (ITDR) incidents encountered during 2024
66

Identity Threats
Inbox Rule
Modifications
Preparing for
invoice scam
Similar to 2023, attackers accessing a Microsoft 365
account would often modify inbox rules to persist,
communicate back to their C2, or siphon email
Extract of a Huntress intrusion for an inbox rule hiding
information� We expanded detection for this activity legitimate invoice emails, with adversary’s goal of
throughout the year and identified several strategies deploying an invoice scam
that attackers were using�
As was the case last year, attackers favored moving
content to the RSS Feeds Folder, which accounted for
more than 50% of malicious activity pertaining to Inbox
Rule modifications, and over a third of detections
involved moving content to the Conversation History
Folder� Attackers also resorted to strategies like
marking content as ‘read’ or ‘read and deleted’
less than one out of 10 times�
Suspicious Inbox Rule Activity
Suspicious Geo Location 1.1%
Marked as Read and Deleted
1.9%
Moving to RSS Feeds Folder
Maked as Read 8% 52%
Moving to Conversation
History Folder 35.4%
Figure 46: Inbox rule abuse methods in 2024
67

Identity Threats
Token Theft
Attackers attempting to hijack or steal users’ tokens accounted for nearly 6% of all
ITDR events during the year� When done correctly, this method can be incredibly hard
to detect as attackers must correctly identify and use the victim’s browser, location,
network tunnel or VPN typically used (or lack thereof), and operating system� Info
stealers will often grab all this information and then data brokers will sell it on the
black market to attackers for less than $10 per individual� Attackers will then attempt
to recreate the environment and use the stolen token to mimic a user’s session and
gain access to their network and corporate data�
Surprisingly, attackers failed to identify or implement the same OS more than a
third of the time, leading to their detection� The bad news here? Attackers have
gotten much better at identifying the target’s location, whereas only 7% of detected
attempts were due to mismatching of location data� Mismatching VPN usage and the
browser the victim regularly uses accounted for the remaining incidents, occurring
approximately 29% and 28% respectively�
Token Theft Detection Triggers
Location 7.2%
27.8% Browser
VPN 28.9%
36.1% OS
Figure 47: Token theft detections in 2024
68

Identity Threats
Credential Theft
We found attackers who were able to steal credentials
and access resources directly without MFA or used Axios user agent
in conjunction with an MFA bypass using a similar
methodology� Mismatching OS occurred nearly half of
the time, as attackers are often seen using customized
Linux-based attack systems like Kali to perform many
of these actions� Attackers stealing credentials seem
Extract of Huntress ITDR event data, showing the details
to have less insight on victims’ locations, as they behind an identity intrusion associated with Axios phishing
failed to correctly account for geolocation four times
more than those attempting token theft� The correct
VPN policy was more accurately determined by
attackers who attempted credential theft versus those
attempting token theft�
Credential Theft Detection Triggers
31.2% Location
OS Mismatch 48.4%
20.4% VPN
Figure 48: Credential theft detections in 2024
69

Identity Threats
VPN and VPN Abuse Frequency
Proxy Abuse
NordVPN
20%
SurfEasy VPN
11.8%
Cybercriminals will often abuse Virtual Private
Networks (VPNs) or proxy systems in their
attacks to conceal their real IP address or try ExpressVPN
11.8%
to bypass geolocation fencing rules so they
can access resources or login information�
During the latter half of 2024, we updated TunnelBear
7.5%
our technology to be able to identify
VPNs and proxies—even when they were
“hidden”—to see which services attackers HMA VPN
5.8%
preferred to abuse�
NordVPN was the top offender, accounting for Surfshark VPN
4.7%
one-fifth (20%) of all incidents we detected�
This popular VPN skyrocketed to infamy in
the last few years due to its marketing push PIA VPN
4.6%
via YouTube and social media influencers�
Attackers seem to have bought into the hype
as well and made it their go-to method for Messon Network VPN
3.9%
targeting Microsoft 365 resources�
SurfEasy and ExpressVPN combined accounted Proton VPN
3.3%
for 23% of incidents in 2024, as both are
similarly popular and readily available VPN
platforms� An interesting finding was the Touch VPN
2.9%
abuse of the Meson Network in nearly 4% of
incidents: this blockchain-based bandwidth
trading protocol is often used by decentralized IPRoyal VPN
2.9%
systems for storage and decentralized apps
(DAPPs), as well as computational needs� TOR
proxy, once a staple protocol for sophisticated VPN Super Free VPN
1.7%
attackers to stay anonymous, was only abused
less than 2% of the time throughout 2024� We
included a chart of the top 15 offending VPN Mullvad VPN
1.5%
and proxy providers so that defenders can
implement these into their own reputational
analysis systems� TOR
1.4%
Lantern VPN
1.2%
Figure 49: VPNs abused to target M365 environments in 2024
70

Phishing Activity
in 2024
71

Phishing Activity
in 2024
Huntress works with Security Awareness Training (SAT) learners to gather potential
phishing email threats reported by victims� We implemented a vision-based
identification process to catalog, organize, and perform in-depth analysis on these
malicious emails� This analysis led us to categorize the most prevalent threats
into 285 unique groups of attacks targeting customers� While these groups don’t
represent all potential attacks, there were clear recurring themes and techniques
that were consistently abused across all industries�
Notable Phishing Email Themes
Other 21.1% e-Signature Impersonation
28.8%
Living Off Trusted Sites
7%
Fake Thread/Reply Chains
2.1% 4.9% Voicemail Lures
4.2% Financial Docs
QR Codes 8.1%
23.9% Image-Based Content
Figure 50: Prevalent phishing themes in 2024
72

Phishing Activity in 2024
Voicemail Luring
Attackers exploit the concept and urgency of missed phone calls and voicemail notifications
to convince users to interact with malicious emails� These attempts typically prompt the
victim to click on links to “hear their voicemail” or get a transcript of their missed call—often
leading to a malicious landing page designed to steal credentials or a malicious download
delivering malware�
From: Susan Fry [mailto:sfry@yourcompany.com]
Sent: Tuesday, January 9, 2025 9:25 AM
To: Hamil, James <james.hamil@yourcompany.com
Subject: Please handle ASAP
- External email. Foward any suspicious emails to bad@yourcompany.com -
VoiceMail Center
Voicemail Transcript
New Incoming voicemall Added
• caller ID: 998003829
Malicious link disguise•d C aalsl Duration: 00:01:22
voicemail transcript • Date: 7/23/2024
Please view and confirm below
Play Transcript
Privacy Statement
Microsoft Corporation, One Microsoft Way, Redmond, WA 98052
Voicemail luring phishing email attempt
73

Phishing Activity in 2024
E-Signature Impersonation
E-signing documents, especially those that look like they come from Docusign and Adobe,
were the most prevalent form of phishing targeting customers in 2024� Attacks using this
technique typically appear in two different forms� The first is attackers crafting fake graphical
emails that look like they originate from the e-signature provider� This technique is usually
detected by environments with email gateway analysis in place, but for those without these
security measures, these emails can look legit� The second, more sophisticated method
involves abusing the actual service provider to host a malicious document or document linking
to a malicious website� These are then sent to the victim and bypass many detection-based
systems, so the victim is socially engineered to log in to a malicious site for attackers to steal
credentials or deliver a malicious payload�
From: Susan Fry [mailto:sfry@yourcompany.com]
Sent: Tuesday, January 9, 2025 9:25 AM
To: Hamil, James <james.hamil@yourcompany.com
Subject: Please handle ASAP
- External email. Foward any suspicious emails to bad@yourcompany.com -
A document has been sent to you. To view the details of your document,
click the button below.
REVIEW DOCUMENT
Link to malicious document
hosted by a legitimate
Please click the ‘Review Document’ button to view the document sent to you.
service provider
Thank you for choosing DocuSign.
Do Not Share This Email
This email contaAinns ae xseacmurpe llein ko tfo aD oDcouSciugSn iPglnea pseh idsoh ninogt s ehamrea tihl isa ettmeamil, plintk, or access code
with others
About DocuSign
Sign documents electronically in just minutes it’s safe, secure, and legally binding Whether you’re in
an office, at home, on-the-go -- or even across the globe -- DocumSign provides a professional
trusted solution for Digital Transaction Management
74

Phishing Activity in 2024
Image-Based Content
To bypass text-based spam filters, attackers often send an image render of their phish design
where an entire image is hyperlinked to point to their malicious landing page� This image is
often the only element included in the email and is a tactic that has been used for many years�
Email gateway scanners can eliminate these before reaching victims, but attackers still find
ways to bypass these and sneak into inboxes�
From: Susan Fry [mailto:sfry@yourcompany.com]
Sent: Tuesday, January 9, 2025 9:25 AM Malicious hyperlink via
To: Hamil, James <james.hamil@yourcompany.com embedded image render
Subject: Please handle ASAP
You don’t often get email from administrator@778392929.com. Learn why this is important
Microsoft 365 sign-in for multi-factor authentication
Hello:
• The multi-factor authentication for your Microsoft account is set to expire today.
• Please re-authenticate now to continue using Microsoft 365 apps and services without
interruption
Re-Authenticate
Contact Microsoft help desk if you have any questions.
This email was sent from an unmonitored mailbox.
You are receiving this email because you have subscribed to Microsoft Office 365.
Privacy Statement
Microsoft Corporation, One Microsoft Way, Redmond, WA 98052 USA
Microsoft
An example of an image-based phishing email attempt
75

Phishing Activity in 2024
QR Codes
To avoid scrutiny on links in their phishing emails, many attackers have pivoted to embedding
QR codes in their messages instead� There is less security awareness around safe handling of
QR codes and victims often scan these with personal mobile devices without organizational
security controls in place� These accounted for slightly more than 8% of phishing attacks in our
data subset, but we expect this method in particular to escalate in 2025�
From: Susan Fry [mailto:sfry@yourcompany.com]
Sent: Tuesday, January 9, 2025 9:25 AM
To: Hamil, James <james.hamil@yourcompany.com
Subject: Please handle ASAP
Microsoft 365 sign-in for multi-factor
authentication
• The multi-factor authentication for is set to expire within 24 hours.
• Scan the barcode below to reauthorize your multi-factor authentificiation within 24
hours and stay connected to Microsoft 365 apps and services.
Malicious QR code
An example of a QR code phishing email attempt
76

Phishing Activity in 2024
Fake “Threads”
/ Reply Chains
A clever tactic from attackers is showing “social proof�” These schemes appear to show a
conversation between multiple people and then are forwarded on to the victim� These emails
often contain malicious attachments used to deploy initial stage malware to steal information
and download subsequent components onto the victim’s machine�
[EXT] uni-ugrad-dept-sales FW: *UPDATED FORM*
Undergraduate Achievement Bursaries: Application form
Sam Smith, Administrative Officer <sam.smith@adminoffice.com>
Mon 2/4/2025 8:30 AM
To: John Williams
Notice: This message was sent from outside the Kent Admin email system. Please be cautious with links and sensitive information.
Hi there,
Please review the latest documents for your department project:
Achievement Bursaries Forms.zip
If you have any questions, Please contact me.
From: Vicky Fitzick, Deans Assistant Malicious attachments
Sent: Monday 10/01/2024 10:33 AM
To: John Doe
Cc: Susan Fry
Subject: “UPDATED FORM” Undergraduate Achievement Bursaries: Application form
This year, 13 bursaries of $1,500 each will be awarded to exceptional students in the university. Students
should be advised to return completed forms to the office of the Dean by 12/31/2024.
Forwarded “social proof”
TERMS OF REFERENCE:
Achievement Bursaries recogize undergraduate students who have demonstrated outstanding commitment
to the pursuit of excellence in their endeavors. Areas where individual expression becomes public are
recognized through these bursaries. Recipients must have demonstrated financial need and a minimum 3.5
sessional grade point average for students continuing at or transferring to the university or a 70% admission
average for students commencing post-secondary studies for the first time.
University officers will distribute application forms to prospective students, who will complete and return
them to thAe On ffeicxe aofm thpe lDee oanf, aFa mcualtyl iocfi toheu sU nfaivekresit yt hbrye thaed d eeamdlinaei.l phishing attempt
77

Phishing Activity in 2024
Living Off Trusted
Sites (LoTS)
In order to get past email security gateways and land directly in inboxes, attackers are using
trusted file-sharing and collaboration sites with free tiers� Instead of putting a malicious link
in a phishing email, they put the link within a document on the trusted site and share that
document to the victim from the trusted site� This is an effective tactic because many users put
their guard down outside their inbox and on “trusted” sites�
From: Susan Fry [mailto:sfry@yourcompany.com]
Sent: Tuesday, January 9, 2025 9:25 AM
To: Hamil, James <james.hamil@yourcompany.com
Subject: Please handle ASAP
Hi there,
In case you missed it, Susan Fry (dropboxadmin@outlook.com) shared
“proposal.pdf” with you on Dropbox.
Document containing View on Dropbox
the malicious link
Thanks! Link to malicious document
–The Dropbox Team via a trusted site
Dropbox, Inc. © 2024 Dropbox
PO Box 77767, San Francisco, CA 94107
View Privacy Policy | Unsubscribe
An example of a LoTS phishing email attempt
78

Phishing Activity in 2024
Impersonated
Brands
Attackers targeted Microsoft 365 users along with a common subset of brands to socially
engineer victims to open their phishing emails� Out of the 285 groups, Microsoft-branded
emails were the most common accounting for nearly 40% of incidents while Docusign was the
second most common impersonation at nearly 25%� Other brands being mimicked to send
malicious emails were Dropbox, Sharefile, Adobe, Paychex and Apple�
Prevalence of Common Brands
125
100
75
50
25
0
Microsoft Docusign Generic Dropbox Sharefile Adobe Paychex Apple Other
Figure 51: Prevalence of common brands impersonated during phishing incidents
79

Conclusions
This 2025 Cyber Threat Report shows how quickly the threat landscape is evolving,
with more and more insidious attacks across organizations of all sizes and in all
industries� Key trends from 2024 like the proliferation of aggressive smaller, more
dynamic ransomware affiliate networks, abuse of remote access trojans (RATs), and
exploitation of remote monitoring and management (RMM) tools, highlight attackers’
adaptability in targeting both enterprise and non-enterprise environments�
Advanced tactics like EDR tampering, complex scripting abuse, and credential theft
continue to be a threat, so robust, layered defenses and proactive threat detection
mechanisms are needed now more than ever�
Looking ahead, we anticipate certain trends escalating: ransomware operators
are likely to refine their extortion strategies, and many will look to changing their
extortion methodologies to those that prioritize data theft over encryption, while
exploitation involving LOLBins, credential stealers, and deploying RATs to maintain
control will remain staples in attackers’ arsenals� The rise in phishing sophistication,
including the use of QR codes, image-based content, and impersonation of trusted
brands, means that greater vigilance and security awareness training are crucial�
Additionally, with the increasing reliance on cloud services, we foresee a surge in
attacks targeting Microsoft 365 environments and similar platforms� To mitigate
these threats, organizations must have comprehensive defenses, including endpoint
monitoring, timely patching, and user education�
The TL;DR? Stay vigilant and resilient, because cyber threats won’t stop evolving�
80

About Huntress
Founded in 2015 by former NSA cyber operators, Huntress protects
over 3 million endpoints and 1 million identities worldwide, elevating
under-resourced IT and security teams and empowering them with
protection that works as hard as they do� Powered by a 24/7 team of
expert security analysts and researchers, our enterprise-grade, fully
owned technology is built for all businesses, not just the 1% with big
budgets�
With fully managed EDR, ITDR, and SIEM solutions and Security
Awareness Training, the Huntress platform helps end users quickly
deploy and manage real-time protection for endpoints, email, and
employees, all from a single dashboard�
Huntress exists to level the cybersecurity playing field and elevate
our community through award-winning technology and world-class
people� We’re ethical badasses who love what we do: wrecking
hackers and protecting businesses from real threats�
Learn More