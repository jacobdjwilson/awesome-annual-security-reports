# 2020 Threat Detection Report

## Table of Contents
- [Introduction](#introduction)
- [Top Techniques](#top-techniques)
- [Technique T1055: Process Injection](#technique-t1055-process-injection)
- [Technique T1053: Scheduled Task](#technique-t1053-scheduled-task)
- [Technique T1077: Windows Admin Shares](#technique-t1077-windows-admin-shares)
- [Technique T1086: PowerShell](#technique-t1086-powershell)
- [Technique T1105: Remote File Copy](#technique-t1105-remote-file-copy)
- [Technique T1036: Masquerading](#technique-t1036-masquerading)
- [Technique T1064: Scripting](#technique-t1064-scripting)
- [Technique T1038: DLL Search Order Hijacking](#technique-t1038-dll-search-order-hijacking)
- [Technique T1482: Domain Trust Discovery](#technique-t1482-domain-trust-discovery)
- [Technique T1089: Disabling Security Tools](#technique-t1089-disabling-security-tools)
- [Additional Research: Technique T1003: Credential Dumping](#additional-research-technique-t1003-credential-dumping)
- [Additional Research: Technique T1047: Windows Management Instrumentation](#additional-research-technique-t1047-windows-management-instrumentation)
- [Additional Research: Technique T1193: Spearphishing Attachment](#additional-research-technique-t1193-spearphishing-attachment)

F O C U S   O N   W H AT   M AT T E R S

## 2020 Threat Detection Report

### Introduction

Welcome to the 2020 Threat Detection Report. This in-depth look at the most prevalent ATT&CK® techniques is designed to help you and your team focus on what matters most.

![Image description]

6M INVESTIGATIVE LEADS
15K CONFIRMED THREATS
1 REPORT

Welcome to Red Canary’s 2020 Threat Detection Report. Based on in-depth analysis of tens of thousands of threats detected across our customers’ environments, this research arms security leaders and their teams with a unique understanding of the threats they’re facing.

We’ve leveraged the common language of MITRE ATT&CK to categorize confirmed threats, but our analysis focuses on providing a comprehensive view of adversary techniques that are most likely to occur in your environment. You’ll find unique intelligence to inform your thinking, help you prioritize investments, and educate your team on how to detect and shut down adversaries.

#### What’s New in 2020

*   **Year-over-year trending**: Last year’s inaugural report summarized all such data available across Red Canary’s entire history. This year’s report focuses on the more than 15,000 threats we detected between January and December 2019, comparing them to threats detected over the same period in the prior year.
*   **Common co-occurrences**: ATT&CK techniques do not occur in isolation, so it is important to understand how adversaries leverage multiple techniques to accomplish their goals. This year’s report identifies ATT&CK techniques that are used in concert by adversaries and their tools.
*   **Actionable insights**: Each technique section includes detailed guidance on data sources security teams can use to observe related threats. We also provide specific telemetry patterns that are useful for detecting threats, as well as those that are prone to false positives.
*   **Additional research**: Our threat rankings are determined entirely by detection volume. As a result, a sizable outbreak in one environment can have a disproportionate impact on our entire dataset. To combat that, we’ve included analysis on supplemental techniques that are outside the top 10 but affected many customers.

How to use the report:
*   Start looking through the most prevalent techniques to see what we’ve observed in our customers’ environments
*   Explore how to detect and mitigate specific techniques, with ideas and recommendations from our detection engineers
*   Talk with your team about how the ideas, recommendations, and priorities fit in with your environment

#### Behind the Data

Since 2013, Red Canary has delivered high-quality threat detection to organizations of all sizes. Our platform collects hundreds of terabytes of endpoint telemetry every day, surfacing evidence of threats that are analyzed by our Cyber Incident Response Team (CIRT). Confirmed threats are tied to corresponding ATT&CK techniques so that our customers clearly understand what is happening in their environments. This report is a summary of confirmed threats derived from this data.

The report excludes low-severity detection of unwanted software, such as adware. We’ve tagged each confirmed threat with corresponding ATT&CK technique(s) based on the logic used to identify the threat.

### Meet the Authors

*   **Keith McCammon**
    CHIEF SECURITY OFFICER & CO-FOUNDER
    Keith leads Red Canary’s security, open source, and educational strategies, as well as community partnerships. He has spent 20 years in InfoSec, including over a decade of service to the US Department of Defense and Intelligence Community.

*   **Brian Donohue**
    ANALYST
    Brian has been writing about and researching information security for the last decade. He started his career as a journalist covering security and privacy. He later consulted as a threat intelligence analyst, researching adversaries and techniques for a variety of major banks, retailers, and manufacturers. At Red Canary, Brian helps guide research publication and technical messaging efforts.

*   **Jeff Felling**
    DIRECTOR OF INTELLIGENCE
    Jeff Felling is a puzzle solver who currently contemplates the conundrums confounding corporate computer custodians, aka a threat hunter. After nearly a dozen years analyzing anomalies, foraging for forensic artifacts, and mulling over malware for the DoD, Jeff returned home to Indiana in 2016 where he helped create Anthem, Inc.’s threat hunting program, ORION, prior to joining Red Canary in April 2019. Jeff holds degrees in mathematics from Johns Hopkins University (MS) and Purdue University (BS), and is certified in security, incident handling, and forensic analysis through SANS.

*   **Tony Lambert**
    INTELLIGENCE ANALYST
    Tony is a professional geek who loves to jump into all things related to detection and digital forensics. After working in enterprise IT administration and detection engineering for several years, he now applies his DFIR skills to research malware, detect malicious activity, and recommend remediation paths. Tony is a natural teacher and regularly shares his findings and expertise through blogs, research reports, and presentations at conferences and events.

#### Acknowledgements

It takes an army to produce a research piece of this magnitude. Thanks to the detection engineers, data analysts, editors, designers, developers, and project managers who invested countless hours in this report. And a huge thanks to the MITRE ATT&CK team, whose framework has helped the community take a giant leap forward in understanding and tracking adversary behaviors.

## Top Techniques

This chart illustrates how often each ATT&CK technique is leveraged in a confirmed threat in our customers’ environments.

1.  17% of total threats: T1055 Process Injection
2.  13%: T1053 Scheduled Task
3.  13%: T1077 Windows Admin Shares
4.  12%: T1086 PowerShell
5.  9%: T1105 Remote File Copy
6.  7%: T1036 Masquerading
7.  5%: T1064 Scripting
8.  5%: T1038 DLL Search Order Hijacking
9.  5%: T1482 Domain Trust Discovery
10. 5%: T1089 Disabling Security Tools
11. 5%: T1003 Credential Dumping
12. 4%: T1035 Service Execution
13. 4%: T1047 Windows Management Instrumentation
14. 3%: T1085 Rundll32
15. 2%: T1140 Deobfuscate/Decode Files or Information
16. 2%: T1093 Process Hollowing
17. 2%: T1015 Accessibility Features
18. 2%: T1168 Local Job Scheduling
19. 2%: T1170 Mshta
20. 2%: T1193 Spearphishing Attachment

NOTE: This report was based on the October 2019 version of the MITRE ATT&CK framework (v6.3). Some technique names and numbers used here may not map to the current matrix.

## Technique T1055: Process Injection

Process Injection was the most common threat we observed in our customers’ environments in 2019, largely because TrickBot uses the technique to run arbitrary code through the Windows Service Host (svchost.exe).

#1 OVERALL RANK
35% ORGANIZATIONS AFFECTED
2,734 CONFIRMED THREATS

**Analysis**
*   **2018**: 1
*   **2019**: 1
Process Injection rose to the top of our rankings due to widespread TrickBot and Emotet outbreaks in late 2018 that continued through 2019.

### Why do adversaries use Process Injection?

Process Injection tops our list as the most common ATT&CK technique across our customer base due to a very specific threat: TrickBot. However, the technique is actually quite versatile, facilitating a range of actions as broad as nearly any other ATT&CK technique. Categorized under both Defense Evasion and Privilege Escalation, Process Injection is arguably an Execution technique as well.

Process Injection is a technique whereby an adversary is able to carry out some nefarious activity in the context of a legitimate process. In this way, malicious activity—whether it’s an overtly malicious binary or a process that’s been co-opted as such—blends in with routine operating system processes.

Stealth, however, is just one of the benefits of Process Injection. Its most useful function may be that arbitrary code, once injected into a legitimate process, can inherit the privileges of that process or, similarly, access parts of the operating system that shouldn’t be otherwise available.

#### How do adversaries use Process Injection?

In the environments we monitor, the vast majority of Process Injection activity results from TrickBot infections. Specifically, TrickBot launches svchost.exe and then uses Process Injection to carry out malicious activity.

Some other common variations of Process Injection include:
*   Remotely injecting code libraries into running processes
*   Using seemingly benign processes such as notepad.exe to make external network connections and later injecting code that performs malicious actions
*   Leveraging Microsoft Office applications to create RemoteThread injections into dllhost.exe for the purposes of conducting attacks with malicious macros
*   Cross-process injection initiated by lsass.exe into taskhost.exe
*   Metasploit injecting itself into processes such as svchost.exe to avoid suspicion and increase stability
*   Injecting code into a browser process to enable snooping on a user’s browsing session, which is a common characteristic of banking and other credential-stealing trojans

In addition to TrickBot, we have also seen the following malware families carry out Process Injection:
*   PlugX
*   Dridex
*   Emotet
*   AgentTesla
*   Hancitor
*   Ursnif/Dreambot

**Sighted with**
We most commonly see Process Injection occurring in tandem with Scheduled Tasks (T1053) across our customer base because TrickBot sometimes uses Scheduled Tasks for persistence.

We also often see Process Injection paired with Remote File Copy (T1105) and Windows Admin Shares (T1077). Code injected into TrickBot downloads additional libraries for execution, explaining its occurrence with Remote File Copy, while TrickBot and common follow-on trojan Emotet use Windows Admin Shares to move laterally on an infected network.

Far less often we see Process Injection alongside Uncommonly Used Port (T1509)—likely because code injected by TrickBot may communicate on tcp/447 and tcp/449 for command and control—and Mshta (T1170). The latter is the result of newer .NET exploitation tools such as DotNetToJScript and CACTUSTORCH that allow attackers to inject code from HTML Applications.

#### Definition
T1055: Process Injection
Process Injection is a method of executing arbitrary code in the address space of a separate live process. Running code in the context of another process may allow access to the process’s memory, system/network resources, and possibly elevated privileges. Execution via Process Injection may also evade detection from security products since the execution is masked under a legitimate process.

#### Detection
**MITRE’s data sources**
*   API monitoring
*   Windows Registry
*   File monitoring
*   DLL monitoring
*   Process monitoring
*   Named Pipes

#### Collection requirements
*   **Process monitoring**: Process monitoring is a minimum requirement for reliably detecting Process Injection. Even though injection can be invisible to some forms of process monitoring, the effects of the injection can become harder to miss once you compare process behaviors against expected functionality.
*   **API monitoring**: If possible, monitor API system calls that include CreateRemoteThread in Windows. This will indicate a process is using the Windows API to inject code into another process. Security teams should monitor for the ptrace system calls on Linux as well.

#### Detection suggestions
The detection of Process Injection involves hunting for legitimate processes doing unexpected things. This may involve processes making external network connections and writing files, or it may involve processes spawning with unexpected command-line arguments.

Some good examples of odd behavior within a process include:
*   Svchost.exe making network connections on tcp/447 and tcp/449
*   Notepad.exe making external network connections
*   Mshta.exe calling CreateRemoteThread to inject code

Some good examples of odd paths or command lines that may indicate injection:
*   Rundll32.exe, regasm.exe, regsvr32.exe, regsvcs.exe, svchost.exe, and werfault.exe process executions without command-line options may indicate they are targets of process injection.
*   Microsoft processes such as vbc.exe with command lines including /scomma, /shtml, or /stext may indicate the injection of Nirsoft tools for credential access.
*   Linux processes with memfd: in their path indicate they were spawned from code injected into another process.

Specific to TrickBot, we have two behavioral analytics that look for untrusted processes launching svchost.exe. Collectively, these two analytics—on their own and in tandem—uncovered more than 4,200 confirmed threats. A third analytic looks for a mix of svchost.exe injection and network connections. It converted into a confirmed threat nearly 2,500 times.

In addition, adversaries may modify some files or environment variables on macOS and Linux systems to signal intent for Process Injection:
*   On macOS, modifying the DYLD_INSERT_LIBRARIES environment variable may allow injection.
*   On Linux systems, modifying the /etc/ld.so.preload file or the environment variables LD_PRELOAD or LD_LIBRARY_PATH may allow injection.

#### Weeding out false positives
The analytics that produced the most false positives came from looking for CreateRemoteThread calls from any and all processes. Many tools in Windows use Process Injection legitimately for debugging and virtualization. If you want to write analytics around this API call, focus them on unusual source processes, such as Microsoft Office products and tools that commonly deliver first-stage malware like scripts and Mshta.

#### Testing
Start testing your defenses against Process Injection using Atomic Red Team—an open source testing framework of small, highly portable detection tests mapped to MITRE ATT&CK.

**Getting started**
View Atomic tests for T1055: Process Injection. In most environments, these should be sufficient to generate a useful signal for defenders.

Run this test on a Windows system using PowerShell:
```powershell
Invoke-WebRequest “https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1055/src/x64/T1055.dll” -OutFile “$env:TEMP\T1055.dll”
$mypid = (get-process spoolsv).id
mavinject $mypid /INJECTRUNNING $env:\TEMP\T1055.dll
```

#### Useful telemetry will include:
*   **DATA SOURCE**: Process monitoring, **TELEMETRY**: powershell.exe, mavinject.exe
*   **DATA SOURCE**: DLL monitoring, **TELEMETRY**: T1055.dll
*   **DATA SOURCE**: API monitoring, **TELEMETRY**: VirtualAllocEx, WriteProcessMemory, CreateRemoteThread

#### Review and repeat
Now that you have executed one or several common tests and checked for the expected results, it’s useful to answer some immediate questions:
*   Were any of your actions detected?
*   Were any of your actions blocked or prevented?
*   Were your actions visible in logs or other defensive telemetry?

Repeat this process, performing additional tests related to this technique. You can also create and contribute tests of your own.

**DETECTION STRATEGIST**
Jason Killam
DETECTION ENGINEER
The detection strategies in this section were brought to you by Jason Killam, who works on Red Canary’s Cyber Incident Response Team (CIRT) as a detection engineer. Prior to that, Jason worked as an incident responder for security teams in the financial sector.

## Technique T1053: Scheduled Task

Scheduled Task is another technique that owes its prominence largely to TrickBot, which schedules tasks to launch malicious binaries and persist on host machines.

#2 OVERALL RANK
33% ORGANIZATIONS AFFECTED
2,079 CONFIRMED THREATS

**Analysis**
*   **2018**: 2
*   **2019**: 2
With an increase in the percentage of customers affected and a decrease in percentage of total threat volume, Scheduled Task was the second most prevalent threat in both 2018 and 2019.

### Why do adversaries use Scheduled Tasks?

Scheduled Tasks allow adversaries to carry out certain actions at pre-specified times, enabling execution, persistence, and privilege escalation. Like many of the techniques analyzed in this report, Scheduled Tasks are a functionally necessary component of the Windows operating system. They execute routinely, and malicious tasks readily blend in with benign ones.

Scheduled Tasks represent a versatile tool for adversaries. With the requisite privileges, an attacker can schedule tasks remotely. The technique is also useful for execution and persistence in conjunction with a variety of widely used scripting languages, such as PowerShell.

#### How do adversaries use Scheduled Tasks?

Adversaries create Scheduled Tasks to run scripts, execute processes, or persist on endpoints to execute later.

Behaviors we frequently observe include:
*   Adware updating itself by using Scheduled Tasks to launch unsigned binaries from AppData
*   Malware using the Task Scheduler Engine (taskeng.exe) to launch a malicious binary that then executes the Service Host process (svchost.exe)
*   Scheduled Tasks executing PowerShell payloads for persistent access

The above behaviors triggered thousands of detections across our customer base and are common characteristics of adware, TrickBot, and QBot infections, respectively.

While TrickBot and Emotet influence the prominence of Scheduled Tasks in our detection data, adversaries of every sophistication level—from adware peddlers to national intelligence agencies—rely on Scheduled Tasks.

**Sighted with**
Scheduled Tasks very commonly occur alongside:
*   Masquerading (T1036)
*   Process Injection (T1055)
*   Disabling Security Tools (T1089)
*   Domain Trust Discovery (T1482)
*   Remote File Copy (T1105)
*   Windows Admin Shares (T1077)

With the possible exception of Masquerading, TrickBot commonly leverages each of these techniques.

#### Definition
T1053: Scheduled Task
Utilities such as at and schtasks, along with the Windows Task Scheduler, can be used to schedule programs or scripts to be executed at a date and time. A task can also be scheduled on a remote system, provided the proper authentication is met to use RPC and file and printer sharing is turned on. Scheduling a task on a remote system typically required being a member of the Administrators group on the remote system. An adversary may use task scheduling to execute programs at system startup or on a scheduled basis for persistence, to conduct remote Execution as part of Lateral Movement, to gain SYSTEM privileges, or to run a process under the context of a specified account.

#### Detection
**MITRE’s data sources**
*   File monitoring
*   Process monitoring
*   Process command-line parameters
*   Windows event logs

#### Collection requirements
*   **API monitoring**: API monitoring is an additional data source that is useful in certain contexts for observing adversaries leveraging Scheduled Task. In some attack campaigns, adversaries have used the Windows Component Object Model and Distributed COM technique (T1175) to create a Scheduled Task via macros or other methods. API monitoring provides visibility into this and other covert methods for creating a Scheduled Task.
*   **File monitoring**: File monitoring provides a useful data source for observing the malicious use of Scheduled Tasks. Defenders should consider tracking the schtasks.exe or at.exe binary because it will enable them to continue observing Scheduled Tasks, even if the binary has been moved to a different path or renamed entirely. A Scheduled Task that has been moved or renamed can be a good indicator of malice.
*   **Process monitoring**: Monitoring process execution of schtasks.exe and at.exe is important because these processes have the ability to set tasks locally or remotely, enabling lateral movement. Historically, adversaries have set Scheduled Tasks to start under a different user context (administrator, for example).
    More recently, PowerShell has a cmdlet (new-ScheduledTask) that provides the same functionality as schtasks.exe. Understanding the processes that normally spawn Scheduled Tasks and monitoring parent-child process relationships is useful for observation as well.
*   **Process command-line parameters**: Process command-line parameters are another rich source for observing malicious Scheduled Tasks. While they might provide the highest fidelity of alerting, they also offer adversaries the most potential for blending in. Understanding the various parameters and what to look for in a given environment requires extensive research and testing, but tracking via the command-line is ultimately the way that most teams monitor for Scheduled Task abuse.
*   **Windows event logs**: Windows event logs may also provide useful information about start and stop times for task execution, as well as additional details about the task itself.

#### Detection suggestions
Security teams should begin by reviewing all process and command-line execution of schtasks.exe and at.exe, ranking the results from most common to least. Where possible, you should also try to collect all Scheduled Tasks across an environment using a tool such as OSQuery or Sysinternals Autoruns. Again, you’ll want to organize the associated processes and command-lines by occurrence, so that you understand which tasks occur often and which do not.

You’ll want to take a close look at less commonly used command-line switches for schtasks.exe. One example might be /XML. It’s entirely possible that searching for this in your environment may turn up nothing, but if you do happen to find it, you’ll want to examine the contents of that XML file.

It’s also a good idea to monitor for tasks that spawn at seemingly strange intervals. For example, something like /sc minute /mo 20, which means that the task will run every 20 minutes, should be viewed with suspicion. There are few legitimate reasons that a task would need to run every 20 minutes—or at any other fixed interval.

Tracking for Scheduled Tasks that load binaries (.exe, for example) or scripts (.ps1, .vbe, and .vbs to name a few) from suspicious paths is a quick win for detection. The default execution path for schtasks.exe or at.exe is c:\windows\system32\ and c:\windows\syswow64\, so any deviation from those should raise concerns that the binary has been moved. Also consider monitoring for suspicious execution paths such as \appdata\ and \windows\tasks\, as it is pretty suspicious for a Scheduled Task to execute from either of these paths.

As is the case with Masquerading, you should review binary metadata. Binary metadata includes a field for internal names, which are often good indicators of a binary’s true identity. It’s a good idea to raise an alert when it appears that schtasks.exe or at.exe have been renamed.

Ultimately, you’ll want to understand what parent processes normally spawn Scheduled Tasks. Is it normal in your environment for SYSTEM to create a task? If the answer is “no,” then you’ll want to consider alerting on that behavior. Similarly, you may want to track when users spawn schtasks.exe from PowerShell or cmd.exe.

#### Weeding out false positives
We should note that tracking schtasks.exe command-line parameters may generate a high volume of data and false positives at first. By default, Windows runs a number of common tasks. The same is essentially true at the organizational level, with application and server-specific tasks. Once you identify and tune out the normal, deviations are pretty reliable indicators of maliciousness.

Some automated software deployment utilities (e.g., SCCM, Kaseya) may utilize Scheduled Tasks to deploy software or keep systems up to date—and may contribute to high false positive rates.

#### Testing
Start testing your defenses against Scheduled Task using Atomic Red Team—an open source testing framework of small, highly portable detection tests mapped to MITRE ATT&CK.

**Getting started**
View Atomic tests for T1053: Scheduled Task. In most environments, these should be sufficient to generate a useful signal for defenders.

Run this test on a Windows system using Command Prompt:
```cmd
SCHTASKS /Create /SC ONCE /TN spawn /TR cmd.exe /ST 21:00
```

#### Useful telemetry will include:
*   **DATA SOURCE**: Process monitoring, **TELEMETRY**: schtasks.exe
*   **DATA SOURCE**: Process command line, **TELEMETRY**: “/SC ONCE”, “cmd.exe”, “/ST 21:00”
*   **DATA SOURCE**: Registry monitoring, **TELEMETRY**: for storage of scheduled task details

#### Review and repeat
Now that you have executed one or several common tests and checked for the expected results, it’s useful to answer some immediate questions:
*   Were any of your actions detected?
*   Were any of your actions blocked or prevented?
*   Were your actions visible in logs or other defensive telemetry?

Repeat this process, performing additional tests related to this technique. You can also create and contribute tests of your own.

**DETECTION STRATEGIST**
Michael Haag
DIRECTOR, ADVANCED THREAT DETECTION AND RESEARCH
The detection strategies in this section were brought to you by Michael Haag! Michael has more than a decade of experience in security architecture and operations. His specialties include advanced threat hunting and investigations, testing, and technological evaluations and integrations.

## Technique T1077: Windows Admin Shares

Self-propagating threats—most notably those that leverage ETERNALBLUE—contributed to the rise of Windows Admin Shares among confirmed threats in the environments we monitor.

28% ORGANIZATIONS AFFECTED
1,995 CONFIRMED THREATS
#3 OVERALL RANK

**Analysis**
*   **2018**: 10
*   **2019**: 3
Change: 7
Windows Admin Shares experienced a dramatic shift in prevalence from 2018 to 2019, climbing from 10 to three and almost quintupling in threat volume.

### Why do adversaries use Windows Admin Shares?

Windows Admin Shares are enabled by default on most Windows systems, and administrators regularly use them to conduct remote host management. Since Windows Admin Share activity is so common, it provides adversaries with a powerful, discreet way to move laterally within an environment. Self-propagating ransomware and cryptocurrency miners, both rapidly emerging threats, rely on Windows Admin Shares.

Many popular lateral movement and execution tools leverage Windows Admin Shares, including:
*   PsExec
*   RemCom
*   CSExec
*   PAExec
*   Impacket wmiexec

#### How do adversaries use Windows Admin Shares?

Adversaries commonly use administrative tools such as PsExec (and the various clones of it) to deploy malware from one machine to another. Admin shares can also be used to store the output of commands for easy access.

The rise of ETERNALBLUE—a prominent, publicly available exploit for a vulnerability in the Windows server message block (SMB) protocol—is a major factor in increased detection of Windows Admin Shares and related activity. To that point, many of our ETERNALBLUE-related analytics map partially to Windows Admin Shares and alert on threats such as:
*   WannaCry
*   TrickBot
*   Several cryptocurrency miners
*   Metasploit
*   Cobalt Strike
*   Other post-exploitation frameworks that use Impacket wmiexec
*   Red teams

**Sighted with**
Windows Admin Shares are often used in conjunction with behaviors relating to Remote File Copy (T1105)—because adversaries commonly use the technique to remotely copy files—and Network Share Discovery (T1135). It can also occur with New Service (T1050) and Service Execution (T1035) because PsExec deploys its receiver executable to admin shares, scheduling a service to execute it.

#### Definition
T1077: Windows Admin Shares
Windows systems have hidden network shares that are accessible only to administrators and provide the ability for remote file copy and other administrative functions. Example network shares include C$, ADMIN$, and IPC$. Adversaries may use this technique in conjunction with administrator-level Valid Accounts to remotely access a networked system over server message block (SMB) to interact with systems using remote procedure calls (RPCs), transfer files, and run transferred binaries through remote Execution. Example execution techniques that rely on authenticated sessions over SMB/RPC are Scheduled Task, Service Execution, and Windows Management Instrumentation. Adversaries can also use NTLM hashes to access administrator shares on systems with Pass the Hash and certain configuration and patch levels.

The Net utility can be used to connect to Windows admin shares on remote systems using net use commands with valid credentials.

#### Detection
**MITRE’s data sources**
*   Process use of network
*   Authentication logs
*   Process monitoring
*   Process command-line parameters

#### Collection requirements
*   **Process use of network**: The malicious use of Windows Admin Shares is often accompanied by large numbers of internal network connections to hosts over the SMB protocol on port 445. Monitoring for this type of activity—high volumes of network connections over port 445—has been instrumental in helping us identify adversarial uses of Windows Admin Shares.
*   **Authentication logs, process monitoring, process command-line parameters**: Authentication logs are a useful data source for observing certain aspects of malicious Windows Admin Shares. So too is process monitoring, which is often used in conjunction with Scheduled Tasks, Service Execution, and Windows Management Instrumentation (WMI). Process command-line parameters are useful as well, particularly for localhost shares.
*   **Network shares**: While MITRE doesn’t list it explicitly, security teams should also consider monitoring network shares (e.g., ADMIN$, C$, and PRINT$), because malicious use of Windows Admin Shares frequently coincides with execution from network shares. An example of this might include the redirection of host or other data in the service of conducting reconnaissance on the localhost admin share.

#### Detection suggestions
Some telemetry patterns to help detect this type of behavior include the use of cmd.exe with the names of shares such as localhost\ADMIN$ or 127.0.0.1\ADMIN$.

#### Weeding out false positives
Because admin shares are often used within the enterprise, but are rarely used uniformly across enterprises, generic detection strategies frequently lead to high false positive rates.

If admin shares are being legitimately used, process and process command-line monitoring may allow you to build a list of processes and attributes that are known, so that you can alert on any deviations. For example, if you expect process ntoskrnl.exe to make a local admin share modification to a specific file at path 127.0.0.1\admin$\[name-of-file], then these can be suppressed and any other process may generate an alert.

Other common sources of false positives are inventory and asset discovery systems. Extend the whitelisting strategy above, adding criteria for initiating system(s), frequency, time of day, and other limiting factors. Just be sure to closely monitor the integrity of any system that you add to your list of trusted initiators, as these systems may be useful targets to an adversary.

#### Testing
Start testing your defenses against Windows Admin Shares using Atomic Red Team—an open source testing framework of small, highly portable detection tests mapped to MITRE ATT&CK.

**Getting started**
View Atomic tests for T1077: Windows Admin Shares. In most environments, these should be sufficient to generate a useful signal for defenders.

Run this test on a Windows system using Command Prompt:
```cmd
cmd.exe /Q /c hostname 1> \\127.0.0.1\ADMIN$\output.txt 2>&1
```

#### Useful telemetry will include:
*   **DATA SOURCE**: Process monitoring, **TELEMETRY**: cmd.exe
*   **DATA SOURCE**: Process use of network, **TELEMETRY**: connection to 127.0.0.1, access to admin shares

#### Review and repeat
Now that you have executed one or several common tests and checked for the expected results, it’s useful to answer some immediate questions:
*   Were any of your actions detected?
*   Were any of your actions blocked or prevented?
*   Were your actions visible in logs or other defensive telemetry?

Repeat this process, performing additional tests related to this technique. You can also create and contribute tests of your own.

**DETECTION STRATEGIST**
Keya Horiuchi
DETECTION ENGINEER
The detection strategies in this section were brought to you by Keya Horiuchi! Keya has experience in multiple areas of information security, including security audits, web and network infrastructure assessments, and network system administration.

## Technique T1086: PowerShell

A core component of many effective attack toolkits, PowerShell is ubiquitous, versatile, and as popular among administrators—who use it for remote system management—as it is among adversaries.

#4 OVERALL RANK
55% ORGANIZATIONS AFFECTED
1,886 CONFIRMED THREATS

**Analysis**
*   **2018**: 4
*   **2019**: 4
Malicious PowerShell affected a slightly smaller number of customers in 2019 than in 2018. Over the same time period, PowerShell accounted for a slightly higher percentage of total threats.

### Why do adversaries use PowerShell?

Installed by default on nearly every Windows system in the world, PowerShell is a dynamic command-line shell and scripting language that IT teams routinely use to conduct remote system administration. Not only is PowerShell activity expected in most Windows environments, system administrators often use the utility in unique and creative ways. As a result, it can be difficult to reliably differentiate legitimate from malicious PowerShell.

Furthermore, administrators and adversaries use many of the same PowerShell features, whether they’re remotely configuring Windows machines and enforcing patch management policies or conducting reconnaissance, running malicious scripts, and installing binaries.

On a more technical level, PowerShell can execute code directly in memory, often using obfuscated commands and reflective injection, making it more difficult to observe and detect. By default, the tool enjoys highly privileged access to the Windows operating system—through application programming interfaces (API), processes such as Windows Management Instrumentation (WMI), and the .NET framework, to name a few.

While newer versions of PowerShell (starting with version 3) offer robust logging capabilities that are helpful for observation and detection, version two and prior remain widely used and lack even basic logging functionalities. We have yet to see any significant malicious use of PowerShell on non-Windows systems, but it’s worth noting that the tool is cross-platform and open source.

Its ease of use and platform availability contribute to PowerShell’s inclusion in countless red team tools and attack simulation platforms, including:
*   PowerShell Empire
*   PowerSploit
*   Invoke-Mimikatz
*   Metasploit
*   Atomic Red Team
*   Cobalt Strike

#### How do adversaries use PowerShell?

PowerShell is highly utilitarian, offering an adversary far more use cases than we can examine in this report. It’s most commonly used to remotely execute scripts and payloads. We regularly see adversaries leveraging embedded macros to launch PowerShell from Office documents—a set of behaviors that we map to both the PowerShell and Spearphishing Attachment (T1193) techniques.

Adversaries also use PowerShell to:
*   Launch Meterpreter sessions
*   Inject into processes
*   Bypass execution policy
*   Execute code filelessly, entirely in CLI to avoid writing scripts to disk
*   Store code