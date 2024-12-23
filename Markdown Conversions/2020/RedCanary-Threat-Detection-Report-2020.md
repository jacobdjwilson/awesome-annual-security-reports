# 2020 Threat Detection Report

## Table of Contents
- [Introduction](#introduction)
- [What’s new in 2020](#whats-new-in-2020)
- [Behind the data](#behind-the-data)
- [Acknowledgements](#acknowledgements)
- [Meet the authors](#meet-the-authors)
- [Top Techniques](#top-techniques)
- [#1 T1055 Process Injection](#1-t1055-process-injection)
- [#2 T1053 Scheduled Task](#2-t1053-scheduled-task)
- [#3 T1077 Windows Admin Shares](#3-t1077-windows-admin-shares)
- [#4 T1086 PowerShell](#4-t1086-powershell)
- [#5 T1105 Remote File Copy](#5-t1105-remote-file-copy)
- [#6 T1036 Masquerading](#6-t1036-masquerading)
- [#7 T1064 Scripting](#7-t1064-scripting)
- [#8 T1038 DLL Search Order Hijacking](#8-t1038-dll-search-order-hijacking)
- [#9 T1482 Domain Trust Discovery](#9-t1482-domain-trust-discovery)
- [#10 T1089 Disabling Security Tools](#10-t1089-disabling-security-tools)
- [#11 T1003 Credential Dumping](#11-t1003-credential-dumping)
- [#13 T1047 Windows Management Instrumentation](#13-t1047-windows-management-instrumentation)
- [#20 T1193 Spearphishing Attachment](#20-t1193-spearphishing-attachment)
- [Additional Research](#additional-research)

Welcome to the 2020 Threat Detection Report
This in-depth look at the most prevalent ATT&CK® techniques is designed to help you and your team focus on what 
matters most.
Welcome to Red Canary’s 2020 Threat Detection Report. Based on in-depth analysis of tens of thousands of threats 
detected across our customers’ environments, this research arms security leaders and their teams with a unique 
understanding of the threats they’re facing.
We’ve leveraged the common language of MITRE ATT&CK to categorize confirmed threats, but our analysis focuses on 
providing a comprehensive view of adversary techniques that are most likely to occur in your environment. You’ll find 
unique intelligence to inform your thinking, help you prioritize investments, and educate your team on how to detect and 
shut down adversaries.

# Introduction
6M

I N V E S T I G A T I V E
L E A D S
15K

C O N F I R M E D
T H R E A T S
1

R E P O R T
Year-over-year trending

Last year’s inaugural report summarized all such 
data available across Red Canary’s entire history. 
This year’s report focuses on the more than 
15,000 threats we detected between January 
and December 2019, comparing them to threats 
detected over the same period in the prior year.
Additional research
Our threat rankings are determined entirely by 
detection volume. As a result, a sizable outbreak 
in one environment can have a disproportionate 
impact on our entire dataset. To combat that, we’ve 
included analysis on supplemental techniques that 
are outside the top 10 but affected many customers.
Common co-occurrences
ATT&CK techniques do not occur in isolation, so it is 
important to understand how adversaries leverage 
multiple techniques to accomplish their goals. This 
year’s report identifies ATT&CK techniques that are 
used in concert by adversaries and their tools.
Actionable insights
Each technique section includes detailed guidance 
on data sources security teams can use to observe 
related threats. We also provide specific telemetry 
patterns that are useful for detecting threats, as well 
as those that are prone to false positives.

# What’s new in 2020
3
4
2020 Threat Detection Report
The report excludes low-severity detection of unwanted software, such as adware. We’ve tagged each confirmed threat 
with corresponding ATT&CK technique(s) based on the logic used to identify the threat.
Since 2013, Red Canary has delivered high-quality threat detection to organizations of all sizes. Our platform collects 
hundreds of terabytes of endpoint telemetry every day, surfacing evidence of threats that are analyzed by our Cyber 
Incident Response Team (CIRT). Confirmed threats are tied to corresponding ATT&CK techniques so that our customers 
clearly understand what is happening in their environments. This report is a summary of confirmed threats derived from 
this data.
How to use the report:
- Start looking through the most prevalent techniques to see what we’ve observed in our customers’ environments
- Explore how to detect and mitigate specific techniques, with ideas and recommendations from our 
detection engineers
- Talk with your team about how the ideas, recommendations, and priorities fit in with your environment

# Behind the data
5
It takes an army to produce a research piece of this magnitude. Thanks to the detection engineers, data analysts, editors, 
designers, developers, and project managers who invested countless hours in this report. And a huge thanks to the MITRE 
ATT&CK team, whose framework has helped the community take a giant leap forward in understanding and tracking 
adversary behaviors.

# Acknowledgements
2020 Threat Detection Report
Keith McCammon
C H I E F  S E C U R I T Y 
O F F I C E R  &  C O - F O U N D E R
Jeff Felling
D I R E C T O R  O F 
I N T E L L I G E N C E
Brian Donohue
A N A LY S T
Tony Lambert
I N T E L L I G E N C E  A N A LY S T

# Meet the authors
Keith leads Red Canary’s security, open source, and 
educational strategies, as well as community partnerships. 
He has spent 20 years in InfoSec, including over a decade of 
service to the US Department of Defense and Intelligence 
Community.
Brian has been writing about and researching information 
security for the last decade. He started his career as a 
journalist covering security and privacy. He later consulted 
as a threat intelligence analyst, researching adversaries 
and techniques for a variety of major banks, retailers, and 
manufacturers. At Red Canary, Brian helps guide research 
publication and technical messaging efforts.
Jeff Felling is a puzzle solver who currently contemplates the 
conundrums confounding corporate computer custodians, 
aka a threat hunter. After nearly a dozen years analyzing 
anomalies, foraging for forensic artifacts, and mulling over 
malware for the DoD, Jeff returned home to Indiana in 
2016 where he helped create Anthem, Inc.’s threat hunting 
program, ORION, prior to joining Red Canary in April 2019. Jeff 
holds degrees in mathematics from Johns Hopkins University 
(MS) and Purdue University (BS), and is certified in security, 
incident handling, and forensic analysis through SANS.
Tony is a professional geek who loves to jump into all things 
related to detection and digital forensics. After working 
in enterprise IT administration and detection engineering 
for several years, he now applies his DFIR skills to research 
malware, detect malicious activity, and recommend 
remediation paths. Tony is a natural teacher and regularly 
shares his findings and expertise through blogs, research 
reports, and presentations at conferences and events.
5
6

# Top Techniques
This chart illustrates how often each ATT&CK technique is leveraged in a confirmed threat in our customers’ environments.
T H R E A T  D E T E C T I O N  R E P O R T
2020 Threat Detection Report
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
T1055 Process Injection
17% of total threats
13%
13%
12%
9%
7%
5%
5%
5%
5%
5%
4%
4%
3%
2%
2%
2%
2%
2%
2%
T1053 Scheduled Task
T1077 Windows Admin Shares
T1105 Remote File Copy
T1086 PowerShell
T1036 Masquerading
T1064 Scripting
T1038 DLL Search Order Hijacking
T1482 Domain Trust Discovery
T1089 Disabling Security Tools
T1003 Credential Dumping
T1035 Service Execution
T1047 Windows Management Instrumentation
T1085 Rundll32
T1140 Deobfuscate/Decode Files or Information
T1093 Process Hollowing
T1015 Accessibility Features
T1168 Local Job Scheduling
T1170 Mshta
T1193 Spearphishing Attachment
NOTE: This report was based on the October 2019 version of the MITRE ATT&CK framework 
(v6.3). Some technique names and numbers used here may not map to the current matrix.
7

#1  T1055 Process Injection
Process Injection

Process Injection was the most common threat we observed in our customers’ environments in 2019, largely because 
TrickBot uses the technique to run arbitrary code through the Windows Service Host (svchost.exe).
Why do adversaries use Process Injection?

Process Injection tops our list as the most common ATT&CK technique across our customer base due to a very specific 
threat: TrickBot. However, the technique is actually quite versatile, facilitating a range of actions as broad as nearly any 
other ATT&CK technique. Categorized under both Defense Evasion and Privilege Escalation, Process Injection is arguably 
an Execution technique as well.
Process Injection is a technique whereby an adversary is able to carry out some nefarious activity in the context of a 
legitimate process. In this way, malicious activity—whether it’s an overtly malicious binary or a process that’s been co-
opted as such—blends in with routine operating system processes.
Stealth, however, is just one of the benefits of Process Injection. Its most useful function may be that arbitrary code, once 
injected into a legitimate process, can inherit the privileges of that process or, similarly, access parts of the operating 
system that shouldn’t be otherwise available.
Process Injection rose to the top of our 
rankings due to widespread TrickBot and 
Emotet outbreaks in late 2018 that continued 
through 2019.

O V E R A L L 

R A N K
35%

O R G A N I Z A T I O N S 
A F F E C T E D
2,734

C O N F I R M E D 
T H R E A T S
T E C H N I Q U E  T 1 0 5 5
Analysis
2018
1
2019
1
2020 Threat Detection Report
8
T H R E A T  V O L U M E
How do adversaries use Process Injection?

In the environments we monitor, the vast majority of Process Injection activity results from TrickBot infections. 
Specifically, TrickBot launches svchost.exe and then uses Process Injection to carry out malicious activity.
Some other common variations of Process Injection include: 
- Remotely injecting code libraries into running processes
- Using seemingly benign processes such as notepad.exe to make external network connections and later injecting 
code that performs malicious actions
- Leveraging Microsoft Office applications to create RemoteThread injections into dllhost.exe for the purposes of 
conducting attacks with malicious macros
- Cross-process injection initiated by lsass.exe into taskhost.exe
- Metasploit injecting itself into processes such as svchost.exe to avoid suspicion and increase stability
- Injecting code into a browser process to enable snooping on a user’s browsing session, which is a common 
characteristic of banking and other credential-stealing trojans
In addition to TrickBot, we have also seen the following malware families carry out Process Injection:
- PlugX
- Dridex
- Emotet
- AgentTesla
- Hancitor
- Ursnif/Dreambot

Sighted with
We most commonly see Process Injection occurring in tandem with Scheduled Tasks (T1053) across our customer base 
because TrickBot sometimes uses Scheduled Tasks for persistence.
We also often see Process Injection paired with Remote File Copy (T1105) and Windows Admin Shares (T1077). Code 
injected into TrickBot downloads additional libraries for execution, explaining its occurrence with Remote File Copy, 
2020 Threat Detection Report
9
while TrickBot and common follow-on trojan Emotet use Windows Admin Shares to move laterally on an infected network.
Far less often we see Process Injection alongside Uncommonly Used Port (T1509)—likely because code injected by TrickBot 
may communicate on tcp/447 and tcp/449 for command and control—and Mshta (T1170). The latter is the result of newer 
.NET exploitation tools such as DotNetToJScript and CACTUSTORCH that allow attackers to inject code from 
HTML Applications.
C U S T O M E R S  A F F E C T E D
Definition
T 1 0 5 5 :  P R O C E S S  I N J E C T I O N
Process Injection is a method of executing arbitrary code in the address space of a separate live process. Running 
code in the context of another process may allow access to the process’s memory, system/network resources, and 
possibly elevated privileges. Execution via Process Injection may also evade detection from security products since the 
execution is masked under a legitimate process.
- API monitoring
- Windows Registry
- File monitoring
- DLL monitoring
- Process monitoring
- Named Pipes
Detection
MITRE’s data sources
2020 Threat Detection Report
10
Collection requirements
Process monitoring

Process monitoring is a minimum requirement for reliably detecting Process Injection. Even though injection can be 
invisible to some forms of process monitoring, the effects of the injection can become harder to miss once you compare 
process behaviors against expected functionality.
API monitoring

If possible, monitor API system calls that include CreateRemoteThread in Windows. This will indicate a process is using 
the Windows API to inject code into another process. Security teams should monitor for the ptrace system calls on Linux 
as well.
Detection suggestions

The detection of Process Injection involves hunting for legitimate processes doing unexpected things. This may involve 
processes making external network connections and writing files, or it may involve processes spawning with unexpected 
command-line arguments.

Some good examples of odd behavior within a process include:
Some good examples of odd paths or command lines that may indicate injection:
- Svchost.exe making network connections on tcp/447 and tcp/449
- Notepad.exe making external network connections
- Mshta.exe calling CreateRemoteThread to inject code
- Rundll32.exe, regasm.exe, regsvr32.exe, regsvcs.exe, svchost.exe, and werfault.exe process executions without 
command-line options may indicate they are targets of process injection.
- Microsoft processes such as vbc.exe with command lines including /scomma, /shtml, or /stext may indicate the 
injection of Nirsoft tools for credential access.
- Linux processes with memfd: in their path indicate they were spawned from code injected into another process.
Specific to TrickBot, we have two behavioral analytics that look for untrusted processes launching svchost.exe. Collectively, 
these two analytics—on their own and in tandem—uncovered more than 4,200 confirmed threats. A third analytic looks for a 
mix of svchost.exe injection and network connections. It converted into a confirmed threat nearly 2,500 times.
In addition, adversaries may modify some files or environment variables on macOS and Linux systems to signal intent for 
Process Injection:
- On macOS, modifying the DYLD_INSERT_LIBRARIES environment variable may allow injection.
- On Linux systems, modifying the /etc/ld.so.preload file or the environment variables LD_PRELOAD or 
LD_LIBRARY_PATH may allow injection.
2020 Threat Detection Report
11
Weeding out false positives
The analytics that produced the most false positives came from looking for CreateRemoteThread calls from any and all 
processes. Many tools in Windows use Process Injection legitimately for debugging and virtualization. If you want to write 
analytics around this API call, focus them on unusual source processes, such as Microsoft Office products and tools that 
commonly deliver first-stage malware like scripts and Mshta.
Testing
Start testing your defenses against Process Injection using Atomic Red Team—an open source testing framework of small, 
highly portable detection tests mapped to MITRE ATT&CK.

Getting started
View Atomic tests for T1055: Process Injection. In most environments, these should be sufficient to generate a useful 
signal for defenders.

Run this test on a Windows system using PowerShell:
`Invoke-WebRequest “https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1055/src/x64/T1055.dll” -OutFile “$env:TEMP\T1055.dll”`
`$mypid = (get-process spoolsv).id`
`mavinject $mypid /INJECTRUNNING $env:\TEMP\T1055.dll`
2020 Threat Detection Report
12
Useful telemetry will include:
DATA SOURCE
TELEMETRY
Process monitoring
powershell.exe, mavinject.exe
DLL monitoring
T1055.dll
API monitoring
VirtualAllocEx, WriteProcessMemory, CreateRemoteThread
Review and repeat
Now that you have executed one or several common tests and checked for the expected results, it’s useful to answer some 
immediate questions:
Repeat this process, performing additional tests related to this technique. You can also create and contribute tests 
of your own.
- Were any of your actions detected?
- Were any of your actions blocked or prevented?
- Were your actions visible in logs or other defensive telemetry?
D E T E C T I O N  S T R A T E G I S T
The detection strategies in this section were 
brought to you by Jason Killam, who works on 
Red Canary’s Cyber Incident Response Team 
(CIRT) as a detection engineer. Prior to that, 
Jason worked as an incident responder for 
security teams in the financial sector.
Jason Killam
D E T E C T I O N  E N G I N E E R
2020 Threat Detection Report
13

#2  T1053 Scheduled Task
Scheduled Task

Scheduled Task is another technique that owes its prominence largely to TrickBot, which schedules tasks to launch 
malicious binaries and persist on host machines.
Why do adversaries use Scheduled Tasks?

Scheduled Tasks allow adversaries to carry out certain actions at pre-specified times, enabling execution, persistence, 
and privilege escalation. Like many of the techniques analyzed in this report, Scheduled Tasks are a functionally necessary 
component of the Windows operating system. They execute routinely, and malicious tasks readily blend in with benign 
ones.
Scheduled Tasks represent a versatile tool for adversaries. With the requisite privileges, an attacker can schedule tasks 
remotely. The technique is also useful for execution and persistence in conjunction with a variety of widely used scripting 
languages, such as PowerShell.
With an increase in the percentage of customers 
affected and a decrease in percentage of total 
threat volume, Scheduled Task was the second 
most prevalent threat in both 2018 and 2019.

O V E R A L L 

R A N K
33%

O R G A N I Z A T I O N S 
A F F E C T E D
2,079

C O N F I R M E D 
T H R E A T S
T E C H N I Q U E  T 1 0 5 3
Analysis
2018
2
2019
2
2020 Threat Detection Report
14
T H R E A T  V O L U M E
How do adversaries use Scheduled Tasks?

Adversaries create Scheduled Tasks to run scripts, execute processes, or persist on endpoints to execute later.
Behaviors we frequently observe include:
- Adware updating itself by using Scheduled Tasks to launch unsigned binaries from AppData
- Malware using the Task Scheduler Engine (taskeng.exe) to launch a malicious binary that then executes the 
Service Host process (svchost.exe)
- Scheduled Tasks executing PowerShell payloads for persistent access
The above behaviors triggered thousands of detections across our customer base and are common characteristics of 
adware, TrickBot, and QBot infections, respectively.
While TrickBot and Emotet influence the prominence of Scheduled Tasks in our detection data, adversaries of every 
sophistication level—from adware peddlers to national intelligence agencies—rely on Scheduled Tasks.

Sighted with
Scheduled Tasks very commonly occur alongside:
- Masquerading (T1036)
- Process Injection (T1055)
- Disabling Security Tools (T1089)
- Domain Trust Discovery (T1482)
- Remote File Copy (T1105)
- Windows Admin Shares (T1077)
With the possible exception of Masquerading, TrickBot commonly leverages each of these techniques.
2020 Threat Detection Report
15
C U S T O M E R S  A F F E C T E D
Definition
T 1 0 5 3 :  S C H E D U L E D  T A S K
Utilities such as at and schtasks, along with the Windows Task Scheduler, can be used to schedule programs or scripts to 
be executed at a date and time. A task can also be scheduled on a remote system, provided the proper authentication is 
met to use RPC and file and printer sharing is turned on. Scheduling a task on a remote system typically required being a 
member of the Administrators group on the remote system. An adversary may use task scheduling to execute programs 
at system startup or on a scheduled basis for persistence, to conduct remote Execution as part of Lateral Movement, to 
gain SYSTEM privileges, or to run a process under the context of a specified account.
- File monitoring
- Process monitoring
- Process command-line parameters
- Windows event logs
Detection
MITRE’s data sources
2020 Threat Detection Report
16
Collection requirements
API monitoring

API monitoring is an additional data source that is useful in certain contexts for observing adversaries leveraging Scheduled 
Task. In some attack campaigns, adversaries have used the Windows Component Object Model and Distributed COM 
technique (T1175) to create a Scheduled Task via macros or other methods. API monitoring provides visibility into this and 
other covert methods for creating a Scheduled Task.
File monitoring

File monitoring provides a useful data source for observing the malicious use of Scheduled Tasks. Defenders should 
consider tracking the schtasks.exe or at.exe binary because it will enable them to continue observing Scheduled Tasks, 
even if the binary has been moved to a different path or renamed entirely. A Scheduled Task that has been moved or 
renamed can be a good indicator of malice.
Process monitoring

Monitoring process execution of schtasks.exe and at.exe is important because these processes have the ability to set tasks 
locally or remotely, enabling lateral movement. Historically, adversaries have set Scheduled Tasks to start under a different 
user context (administrator, for example).

More recently, PowerShell has a cmdlet (new-ScheduledTask) that provides the same functionality as schtasks.exe. 
Understanding the processes that normally spawn Scheduled Tasks and monitoring parent-child process relationships is 
useful for observation as well.
Process command-line parameters

Process command-line parameters are another rich source for observing malicious Scheduled Tasks. While they might 
provide the highest fidelity of alerting, they also offer adversaries the most potential for blending in. Understanding the 
various parameters and what to look for in a given environment requires extensive research and testing, but tracking via 
the command-line is ultimately the way that most teams monitor for Scheduled Task abuse.
Windows event logs

Windows event logs may also provide useful information about start and stop times for task execution, as well as additional 
details about the task itself.
2020 Threat Detection Report
17
Detection suggestions

Security teams should begin by reviewing all process and command-line execution of schtasks.exe and at.exe, ranking the 
results from most common to least. Where possible, you should also try to collect all Scheduled Tasks across an environment 
using a tool such as OSQuery or Sysinternals Autoruns. Again, you’ll want to organize the associated processes and command-
lines by occurrence, so that you understand which tasks occur often and which do not.
You’ll want to take a close look at less commonly used command-line switches for schtasks.exe. One example might be /XML. 
It’s entirely possible that searching for this in your environment may turn up nothing, but if you do happen to find it, you’ll 
want to examine the contents of that XML file.
It’s also a good idea to monitor for tasks that spawn at seemingly strange intervals. For example, something like /sc minute 
/mo 20, which means that the task will run every 20 minutes, should be viewed with suspicion. There are few legitimate 
reasons that a task would need to run every 20 minutes—or at any other fixed interval.
Tracking for Scheduled Tasks that load binaries (.exe, for example) or scripts (.ps1, .vbe, and .vbs to name a few) from 
suspicious paths is a quick win for detection. The default execution path for schtasks.exe or at.exe is c:\windows\system32\ 
and c:\windows\syswow64\, so any deviation from those should raise concerns that the binary has been moved. Also 
consider monitoring for suspicious execution paths such as \appdata\ and \windows\tasks\, as it is pretty suspicious for a 
Scheduled Task to execute from either of these paths.
As is the case with Masquerading, you should review binary metadata. Binary metadata includes a field for internal names, 
which are often good indicators of a binary’s true identity. It’s a good idea to raise an alert when it appears that schtasks.exe or 
at.exe have been renamed.
Ultimately, you’ll want to understand what parent processes normally spawn Scheduled Tasks. Is it normal in your 
environment for SYSTEM to create a task? If the answer is “no,” then you’ll want to consider alerting on that behavior. 
Similarly, you may want to track when users spawn schtasks.exe from PowerShell or cmd.exe.
Weeding out false positives
We should note that tracking schtasks.exe command-line parameters may generate a high volume of data and false positives 
at first. By default, Windows runs a number of common tasks. The same is essentially true at the organizational level, with 
application and server-specific tasks. Once you identify and tune out the normal, deviations are pretty reliable indicators of 
maliciousness.
Some automated software deployment utilities (e.g., SCCM, Kaseya) may utilize Scheduled Tasks to deploy software or keep 
systems up to date—and may contribute to high false positive rates.
2020 Threat Detection Report
18
Testing
Start testing your defenses against Scheduled Task using Atomic Red Team—an open source testing framework of small, 
highly portable detection tests mapped to MITRE ATT&CK.

Getting started
View Atomic tests for T1053: Scheduled Task. In most environments, these should be sufficient to generate a useful 
signal for defenders.

Run this test on a Windows system using Command Prompt:
`SCHTASKS /Create /SC ONCE /TN spawn /TR cmd.exe /ST 21:00`
2020 Threat Detection Report
19
Useful telemetry will include:
DATA SOURCE
TELEMETRY
Process monitoring
schtasks.exe
Process command line
“/SC ONCE”, “cmd.exe”, “/ST 21:00”
Registry monitoring
for storage of scheduled task details
Review and repeat
Now that you have executed one or several common tests and checked for the expected results, it’s useful to answer some 
immediate questions:
Repeat this process, performing additional tests related to this technique. You can also create and contribute tests of 
your own.
- Were any of your actions detected?
- Were any of your actions blocked or prevented?
- Were your actions visible in logs or other defensive telemetry?
D E T E C T I O N  S T R A T E G I S T
The detection strategies in this section were 
brought to you by Michael Haag! Michael 
has more than a decade of experience in 
security architecture and operations. His 
specialties include advanced threat hunting 
and investigations, testing, and technological 
evaluations and integrations.
Michael Haag
D I R E C T O R ,  A D V A N C E D 
T H R E A T  D E T E C T I O N 
A N D  R E S E A R C H
2020 Threat Detection Report
20

#3  T1077 Windows Admin Shares
Windows Admin Shares

Self-propagating threats—most notably those that leverage ETERNALBLUE—contributed to the rise of Windows Admin 
Shares among confirmed threats in the environments we monitor.
Why do adversaries use Windows Admin Shares?

Windows Admin Shares are enabled by default on most Windows systems, and administrators regularly use them to 
conduct remote host management. Since Windows Admin Share activity is so common, it provides adversaries with a 
powerful, discreet way to move laterally within an environment. Self-propagating ransomware and cryptocurrency miners, 
both rapidly emerging threats, rely on Windows Admin Shares.
Many popular lateral movement and execution tools leverage Windows Admin Shares, including:
- PsExec
- RemCom
- CSExec
- PAExec
- Impacket wmiexec
Windows Admin Shares experienced a dramatic 
shift in prevalence from 2018 to 2019, climbing 
from 10 to three and almost quintupling in 
threat volume.

O V E R A L L 

R A N K
28%

O R G A N I Z A T I O N S 
A F F E C T E D
1,995

C O N F I R M E D 
T H R E A T S
T E C H N I Q U E  T 1 0 7 7
Analysis
2018
10
2019
3
2020 Threat Detection Report
Change      7
21
T H R E A T  V O L U M E
How do adversaries use Windows Admin Shares?

Adversaries commonly use administrative tools such as PsExec (and the various clones of it) to deploy malware from 
one machine to another. Admin shares can also be used to store the output of commands for easy access.
The rise of ETERNALBLUE—a prominent, publicly available exploit for a vulnerability in the Windows server message 
block (SMB) protocol—is a major factor in increased detection of Windows Admin Shares and related activity. To that 
point, many of our ETERNALBLUE-related analytics map partially to Windows Admin Shares and alert on threats 
such as:
- WannaCry
- TrickBot
- Several cryptocurrency miners
- Metasploit
- Cobalt Strike
- Other post-exploitation frameworks that use Impacket wmiexec
- Red teams
Sighted with
Windows Admin Shares are often used in conjunction with behaviors relating to Remote File Copy (T1105)—because 
adversaries commonly use the technique to remotely copy files—and Network Share Discovery (T1135). It can also occur 
with New Service (T1050) and Service Execution (T1035) because PsExec deploys its receiver executable to admin shares, 
scheduling a service to execute it.
2020 Threat Detection Report
C U S T O M E R S  A F F E C T E D
22
Definition
T 1 0 7 7 :  W I N D O W S  A D M I N  S H A R E S
Windows systems have hidden network shares that are accessible only to administrators and provide the ability for 
remote file copy and other administrative functions. Example network shares include C$, ADMIN$, and IPC$. Adversaries 
may use this technique in conjunction with administrator-level Valid Accounts to remotely access a networked system 
over server message block (SMB) to interact with systems using remote procedure calls (RPCs), transfer files, and run 
transferred binaries through remote Execution. Example execution techniques that rely on authenticated sessions over 
SMB/RPC are Scheduled Task, Service Execution, and Windows Management Instrumentation. Adversaries can also use 
NTLM hashes to access administrator shares on systems with Pass the Hash and certain configuration and patch levels. 
The Net utility can be used to connect to Windows admin shares on remote systems using net use commands with valid 
credentials.
- Process use of network
- Authentication logs
- Process monitoring
- Process command-line parameters
Detection
MITRE’s data sources
2020 Threat Detection Report
Collection requirements
Process use of network

The malicious use of Windows Admin Shares is often accompanied by large numbers of internal network connections to 
hosts over the SMB protocol on port 445. Monitoring for this type of activity—high volumes of network connections over 
port 445—has been instrumental in helping us identify adversarial uses of Windows Admin Shares.
23
2020 Threat Detection Report
Authentication logs, process monitoring, process 
command-line parameters

Authentication logs are a useful data source for observing certain aspects of malicious Windows Admin Shares. So 
too is process monitoring, which is often used in conjunction with Scheduled Tasks, Service Execution, and Windows 
Management Instrumentation (WMI). Process command-line parameters are useful as well, particularly for 
localhost shares.
Network shares

While MITRE doesn’t list it explicitly, security teams should also consider monitoring network shares (e.g., ADMIN$, C$, 
and PRINT$), because malicious use of Windows Admin Shares frequently coincides with execution from network shares. 
An example of this might include the redirection of host or other data in the service of conducting reconnaissance on the 
localhost admin share.


Detection suggestions
Some telemetry patterns to help detect this type of behavior include the use of cmd.exe with the names of shares such as 
localhost\ADMIN$ or 127.0.0.1\ADMIN$.
Weeding out false positives

Because admin shares are often used within the enterprise, but are rarely used uniformly across enterprises, generic 
detection strategies frequently lead to high false positive rates.
If admin shares are being legitimately used, process and process command-line monitoring may allow you to build a list 
of processes and attributes that are known, so that you can alert on any deviations. For example, if you expect process 
ntoskrnl.exe to make a local admin share modification to a specific file at path 127.0.0.1\admin$\[name-of-file], then 
these can be suppressed and any other process may generate an alert.
Other common sources of false positives are inventory and asset discovery systems. Extend the whitelisting strategy 
above, adding criteria for initiating system(s), frequency, time of day, and other limiting factors. Just be sure to closely 
monitor the integrity of any system that you add to your list of trusted initiators, as these systems may be useful targets to 
an adversary.
24
Testing
Start testing your defenses against Windows Admin Shares using Atomic Red Team—an open source testing framework of 