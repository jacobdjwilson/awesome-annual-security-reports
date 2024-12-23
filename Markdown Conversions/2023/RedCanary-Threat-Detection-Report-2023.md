# Red Canary 2023 Threat Detection Report

## Table of Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Trends](#trends)
    - [Ransomware](#ransomware)
    - [Initial access tradecraft](#initial-access-tradecraft)
    - [Command and control frameworks](#command-and-control-frameworks)
    - [Stealers](#stealers)
    - [Identity](#identity)
    - [Email threats](#email-threats)
    - [Adversary emulation and testing](#adversary-emulation-and-testing)
- [Threats](#threats)
    - [Qbot](#qbot)
    - [Impacket](#impacket)
    - [AdSearch](#adsearch)
    - [Gootloader](#gootloader)
    - [Mimikatz](#mimikatz)
    - [SocGholish](#socgholish)
    - [Raspberry Robin](#raspberry-robin)
    - [Cobalt Strike](#cobalt-strike)
    - [BloodHound](#bloodhound)
    - [Gamarue](#gamarue)
    - [Yellow Cockatoo](#yellow-cockatoo)
    - [Emotet](#emotet)
    - [PlugX](#plugx)
- [Techniques](#techniques)
    - [Windows Command Shell](#windows-command-shell)
    - [PowerShell](#powershell)
    - [Windows Management Instrumentation](#windows-management-instrumentation)
    - [Obfuscated Files or Information](#obfuscated-files-or-information)
    - [Rundll32](#rundll32)
    - [Ingress Tool Transfer](#ingress-tool-transfer)
    - [Process Injection](#process-injection)
    - [Service Execution](#service-execution)
    - [Rename System Utilities](#rename-system-utilities)
    - [LSASS Memory](#lsass-memory)
    - [Modify Registry](#modify-registry)
    - [Gatekeeper Bypass](#gatekeeper-bypass)
    - [Mark-of-the-Web Bypass](#mark-of-the-web-bypass)
    - [Setuid and Setgid](#setuid-and-setgid)
    - [SMB/Windows Admin Shares](#smbwindows-admin-shares)
    - [Multi-Factor Authentication Request Generation](#multi-factor-authentication-request-generation)
- [Acknowledgements](#acknowledgements)

2
table of contents
I N T R O D U C T I O N  	                           03
M E T H O D O L O G Y  	        	                  04
T R E N D S 	
	
	
            06
Introduction 
 
 
                              07 
Ransomware	
 
 
 
          08
Initial access tradecraft 
 
 
         12
Command and control frameworks	
 
         16
Stealers	 	
 
 
 
         18
Identity  
                                                                     20
Email threats 
 
                                                 22
Adversary and emulation testing	
	
         25
A C K N O W L E D G E M E N T S 	
             111
T H R E AT S  	                 	
   32
Introduction 
 
 
 
         33
Qbot	
 
 
                                                 35
Impacket	 
                                                                     37
AdSearch	
 
 
                                                 39
Gootloader	
 
 
                             41
Mimikatz	 
 
                                                 43
SocGholish	
 
                                                 45
Raspberry Robin	
 
 
                             48
Cobalt Strike	
 
 
                             51
BloodHound	
 
 
                             53
Gamarue	 
 
                                                 55
Yellow Cockatoo	
 
 
                             57
Emotet	  
 
                                                 59
PlugX	
 
 
                                                 61
Introduction 
 
 
                              64 
Windows Command Shell	
 
 
          66
PowerShell	
 
 
                              68
Windows Management Instrumentation	
          70 
Obfuscated Files or Information	
 
          73
Rundll32	 
 
                                                  76 
Ingress Tool Transfer	
 
 
          78
Process Injection	  
 
                              80
Service Execution	  
 
                              83
Rename System Utilities	
 
 
          85
LSASS Memory	
 
 
                              87
Modify Registry	
 
 
                              89
Gatekeeper Bypass	 
 
                              93
Setuid and Setgid	  
 
                              98
Mark-of-the-Web Bypass	
 
 
          101
SMB/ Windows Admin Shares	
 
          105
Multi-Factor Authentication Request Generation           109
T E C H N I Q U E S  	
               	    63
3
It is our pleasure to provide you with Red Canary’s 2023 Threat Detection Report. 
Our fifth annual retrospective, this report is based on in-depth analysis of nearly 
40,000 threats detected across our 800+ customers’ endpoints, networks, cloud 
workloads, identities, and SaaS applications over the past year. This report 
provides you with a comprehensive view of this threat landscape, including 
new twists on existing adversary techniques, and the trends that our team has 
observed as adversaries continue to organize, commoditize, and ratchet up their 
cybercrime operations. 
As the technology that we rely on to conduct business continues to evolve,  
so do the threats that we face. Here’s what’s new in this year’s report:
Cloud and identity attacks are becoming more prevalent across our 
customers’ environments and appear for the first time in this report.
Our unique visibility into email attacks, still the leading initial access 
vector used by adversaries, has put us in a position to detect even more 
attacks at earlier stages.
Adversary simulation and other authorized testing are excluded  
from our data set, leading to a more accurate representation of the 
threat landscape. 
What’s old is new: Raspberry Robin, a USB-based threat first discovered 
by Red Canary, continues to evolve and we provide updated research.
Mitigation guidance to limit adversaries’ effectiveness.
intro
HOW TO USE THIS REPORT
•	
Explore the most prevalent and impactful threats, techniques, and trends 
that we’ve observed.  
•	
Note how adversaries are evolving their tradecraft as organizations continue 
their shift to cloud-based identity, infrastructure, and applications.  
•	
Learn how to emulate, mitigate, and detect specific threats and techniques.  
•	
Shape and inform your readiness, detection, and response to critical threats.
4
methodology
As Red Canary eclipses a decade providing world-class security operations 
to organizations around the world, we continue to analyze, learn, and evolve 
based on the petabytes of raw data and trillions of signals that our XDR platform 
consumes daily. Every byte of this data is interrogated 24x7 by roughly 3,500 
analytics, and adversaries are relentlessly pursued by our expert team of 
intelligence, research, detection, and threat hunting professionals. In 2022, Red 
Canary detected and responded to nearly 40,000 threats that our customers’ 
preventative controls missed.
Behind the data 
The Threat Detection Report sets itself apart from other annual reports with 
unique data and insights that are derived from a combination of expansive 
detection coverage coupled with expert, human-led investigation and 
confirmation of threats. The data that powers Red Canary and this report are 
not mere software signals—this data set is the result of hundreds of thousands 
of expert investigations across millions of protected systems. Each of the nearly 
40,000 threats that we responded to have one thing in common: These threats 
weren’t prevented by our customers’ expansive security controls—they are the 
product of a breadth and depth of analytics that we use to detect the threats  
that would otherwise go undetected.
“In 2022, Red 
Canary detected 
and responded to 
nearly 40,000 threats 
that our customers’ 
preventative controls 
missed.”
5
What counts 
When our detection engineers develop detection analytics, they map them to 
corresponding MITRE ATT&CK® techniques. If the analytic uncovers a realized 
or confirmed threat, we construct a timeline that includes detailed information 
about the activity we observed. Because we know which ATT&CK techniques an 
analytic aims to detect, and we know which analytics led us to identify a realized 
threat, we are able to look at these data over time and determine technique 
prevalence, correlation, and much more. 
This report also examines the broader landscape of threats that leverage these 
techniques and other tradecraft, ultimately harming organizations. While Red 
Canary broadly defines a threat as any suspicious or malicious activity that 
represents a risk to you or your organization, we also track specific threats by 
programmatically or manually associating malicious and suspicious activity with 
clusters of activity, specific malware variants, legitimate tools being abused, 
and known threat actors. Our Intelligence Operations team tracks and analyzes 
these threats continually throughout the year, publishing Intelligence Insights, 
bulletins, and profiles, considering not just prevalence of a given threat, but 
also aspects such as velocity, impact, or the relative difficulty of mitigating or 
defending. The Threats section of this report synthesizes our analysis of common 
or impactful threats, which we rank by the number of customers they affect. 
Consistent with past years, we exclude unwanted software from the data we use 
to compile this report. And for the first time this year, in an effort to better reflect 
the threat landscape, we also exclude authorized testing (see a more detailed 
explanation in the Testing trend section of this report).
Limitations 
Red Canary optimizes heavily for detecting and responding rapidly to early-stage 
adversary activity. As a result, the techniques that rank skew heavily between 
the initial access stage of an intrusion and any rapid privilege escalation and 
attempts at lateral movement. This will be in contrast to incident response 
providers, whose visibility tends towards the middle and later stages of an 
intrusion, or a full-on breach.
Knowing the limitations of any methodology is important as you determine 
what threats your team should focus on. While we hope our list of top threats 
and detection opportunities helps you and your team prioritize, we recommend 
building your own threat model by comparing the top threats we share in our 
report with what other teams publish and what you observe in your  
own environment.
RECONNAISSANCE
INITIAL ACCESS
EXECUTION
PERSISTENCE
DEFENSE EVASION
CREDENTIAL ACCESS
DISCOVERY
LATERAL MOVEMENT
PRIVILEGE 
ESCALATION
RESOURCE 
DEVELOPMENT
COLLECTION
EXFILTRATION
IMPACT
COMMAND  
& CONTROL
7
trends
Red Canary performed an analysis of emerging and significant trends that we’ve 
encountered in confirmed threats, intelligence reporting, and elsewhere over the 
past year. We’ve compiled the most prominent trends of 2022 in this report to 
show major themes that may continue into 2023.
The Technique and Threat sections of this report are focused on prevalent 
ATT&CK techniques and threat associations from the nearly 40,000 confirmed 
threats we detected in 2022. The Trends section takes us one step beyond that 
data and allows us to narrate events that might not be prevalent in our detection 
data set but may be emergent or otherwise deserve your attention.
Ransomware
TRENDS
Initial access tradecraft
Command and control frameworks
Stealers
Identity
Email threats
Adversary emulation and testing
How to use our analysis 
The 2022 Trends section is intended to provide valuable insight and actionable 
recommendations for security leaders to make informed decisions. We offer 
advice to help defenders prepare, prevent, detect, and mitigate activity 
associated with each trend. The guidance we provide differs, since each trend 
requires a different approach. You might also use our analysis to help anticipate 
and plan for key trends that may continue into 2023, just as we saw with 2021 
trends extending into 2022.
WHAT’S INCLUDED 
IN THIS SECTION? 
We’ve written an extensive  
analysis of seven trends 
we tracked throughout 
2022. This PDF includes 
an abridged version of our 
analysis, describing the 
trend and explaining why 
it matters. You can view 
the full analysis—including 
mitigation, detection, and 
testing guidance—in the 
web version of this report.
8
TREND
The ransomware landscape continued to shift in 2022. While some metrics 
suggested that ransomware was less prevalent, other metrics suggested that 
ransomware was more prevalent for specific sectors. The community observed 
new ransomware groups popping up, while others disappeared. Regardless of 
the exact numbers, ransomware continues to be one of the most pressing threats 
to every organization.
What we saw in 2022
A visibility challenge 
A major challenge with ransomware is that no one sees all ransomware 
intrusions, so no one knows how bad the problem really is. From Red Canary’s 
perspective, we didn’t see much ransomware in 2022—no ransomware group 
made it into our top 20 threats, and we saw fewer ransomware incidents as 
compared to 2021. However, that reflects our visibility rather than the true 
prevalence of ransomware. As with any intrusion, ransomware doesn’t come  
out of thin air—it’s part of a larger chain of events, as depicted in this diagram.
2022 brought significant developments to the ransomware 
ecosystem, but the basic—and detectable—adversary 
behaviors remain the same. 
Ransomware
9
We focus on trying to detect ransomware precursor activity in the initial access, 
reconnaissance, and lateral movement phases and help our customers stop it 
before it gets to exfiltration or encryption. The result is that we see many more 
so-called ransomware precursors than we do actual ransomware payloads. In 
fact, eight out of our top 10 threats are regularly observed during early stages of 
ransomware intrusions:
Red Canary observes some later-stage ransomware intrusions that involve 
encryption, but these usually come to us through incident response (IR) partners 
who are called in after an organization realizes they have a ransomware intrusion 
and then bring Red Canary in for further monitoring and detection. Across the 
board, our partners reported a drastic decrease in new reported ransomware 
cases as compared to 2021. While the reason for this is unclear, one possible 
factor is the higher barrier to obtaining cyber insurance policies in 2022 due 
to the prevalence of ransomware-related claims. If fewer organizations have 
cyber insurance due to challenges obtaining it, fewer IR firms may be called in 
to respond to ransomware intrusions. This change in IR firm visibility may have 
contributed to the decrease in Red Canary’s visibility of ransomware in 2022.
What we can say is that ransomware continues to cause significant damage. 
Since none of us have perfect visibility, it’s important to also look at the visibility 
others have into the ransomware ecosystem. Recorded Future’s analysis of 
ransomware group leak sites demonstrates that ransomware is still prevalent. 
Additionally, significant ransomware attacks in 2022 such as the ones against the 
Costa Rican government and the Los Angeles School District also demonstrate 
that ransomware remains an impactful threat. 
Affiliate model 
One challenge in tracking and responding to ransomware intrusions is that 
different adversaries are often involved at different phases of the intrusion. As 
depicted in the below diagram, one adversary might be in charge of initial access, 
and then pass that access to a different adversary to continue the intrusion.
Qbot
Impacket
Gootloader
SocGholish
Mimikatz
Raspberry Robin
Cobalt Strike
BloodHound
TOP RANSOMWARE PRECURSORS
10
This makes tracking ransomware groups even more difficult, as intrusions can be 
a “mix and match” of different affiliates providing access to different ransomware 
groups. Throughout 2022, ransomware groups continued to rely on affiliates to 
give them initial access to an environment before they stole or encrypted files. 
Our partners at Microsoft have an excellent breakdown of this ecosystem we 
recommend for further reading.
Renaming 
We observed many of the same malware families that were previously 
“ransomware precursors” continue to lead to ransomware—however, they often 
led to different ransomware families than in previous years. As we’ve observed 
over the past several years, ransomware groups continued to “disappear” from 
existence under one name, often followed by another group under a new name 
appearing with similar tools and TTPs.
As this table shows, a significant ransomware development in 2021 was  
the fall of Conti and the rise of other ransomware groups. Many researchers  
assess that groups like Black Basta have some relationship to Conti based on 
similarities between tools and techniques, suggesting operators may have  
simply started operating under a different name after Conti gained widespread 
law enforcement scrutiny.
MALWARE  
FAMILY  
(PRECURSOR)
2021 
RANSOMWARE 
GROUP
2022 
RANSOMWARE 
GROUP
Qbot
Conti
Black Basta
IcedID
Conti
Quantum
Zloader/BATLOADER
Conti
Royal
11
Extortion without encryption 
As we discussed in last year’s report, adversaries aren’t just encrypting data 
anymore, they’re stealing it as well and demanding payment or they will leak 
the data. This shift toward exfiltration and extortion, often without encryption 
at all, continued in 2022. Notably, the extortion group known as LAPSUS$/DEV-
0537 conducted multiple high-profile intrusions against large organizations 
such as Nvidia and Okta. These intrusions were particularly notable because 
the adversaries stole data and threatened companies with its release if they 
didn’t pay—but unlike traditional ransomware, they never encrypted data. This 
“extortion-only” approach is significant because it changes how organizations 
need to think about this category of threat. LAPSUS$-style TTPs are also 
significantly different from traditional ransomware operators, with use of 
techniques like MFA bypass or even insider recruitment to obtain credentials, 
which influences how organizations need to think about detection and response.
Visit the Ransomware trend page for relevant detection opportunities and 
atomic tests to validate your coverage. 
Though the ransomware ecosystem certainly changed in 2022, the good 
news for defenders is that the techniques these adversaries use often remain 
the same. While there is no single silver bullet to preventing ransomware, the 
tried-and-true guidance of patching known vulnerabilities is a solid approach 
to preventing initial access, as many ransomware intrusions start this way. If an 
organization can’t keep up with patching all vulnerabilities, prioritizing based  
on something like CISA’s Known Exploited Vulnerabilities catalog may  
be helpful.
As LAPSUS$-style TTPs are being used by extortion groups, organizations 
should also consider how they could prevent techniques like MFA bypass. 
Implementing strong Conditional Access and MFA policies is the best 
mechanism to combat this technique. Preventing users from using SMS  
or phone calls for MFA is recommended and implementing a FIDO2 key  
or authenticator app with number matching or similar is preferred,  
as outlined here.
TAKE ACTION
12
TREND
In 2022 we saw major malware campaigns leverage vintage tradecraft in new 
ways, experimenting with delivery vehicles and file types in an attempt to 
evade detection. Weaponized Microsoft documents and malicious macros 
waned in favor of evil binaries hidden within nested layers of container files 
and compressed archives. Adversaries manipulated search engine ads and 
results to lure users into downloading malicious installers. USBs, a well-known 
threat vector for decades, saw a resurgence in use by new malware families and 
established adversaries.
Phishing trend: Macros are out, 
compressed files and containers are in
Macros traded in for newer delivery vehicles 
In February 2022, Microsoft announced that they would start blocking VBA 
macros by default across their entire product suite. Key to implementing this 
change is the Zone Identifier Alternate Data Stream (ADS) value assigned to 
downloaded files and attachments, with the specific value based on whether  
or not the file came from a trusted location. The internet is not considered a 
trusted source, meaning files with the Zone.Identifier ADS value of 3—commonly 
known as the Mark-of-the-Web (MOTW)—can be subject to more stringent 
security measures. 
Not all file types are automatically assigned the MOTW. It depends on several 
factors, including the software used to download the file, the file format, and 
other utilities with features that may or may not be enabled. Compressed 
archives (ZIP, RAR) and container files (ISO, VHD) are types of files that may not 
have the MOTW, meaning they won’t be restricted, blocked, or generate warning 
prompts in the same way as files that do contain the mark.
Following Microsoft’s announcement, adversaries across all verticals changed 
their techniques. They rapidly shifted away from malicious macros in their 
phishing emails and began leveraging container files and compressed files to 
deliver their malware, often nesting these file types within each other in an 
attempt to further bypass security controls. In June 2022, 7-Zip released an 
update that added an opt-in feature that could add the MOTW to ZIP files.  
Adversaries reevaluated their initial access methodologies  
in 2022 and leveraged old tradecraft in new ways at 
prodigious scale.
Initial access  
tradecraft
13
In November 2022, Microsoft released a security update that propagated MOTW 
identifiers to some ZIP and ISO files. These updates may reduce the misuse of ZIP 
and ISO files in 2023.
Compressed archives 
Throughout the year, we observed compressed archives, especially RAR or ZIP 
files, used as a malicious nested attachment’s outer layer. They do not have a 
Zone Identifier ADS attribute, so they can not have a MOTW. Again, 7-Zip’s June 
update may complicate an adversary’s ability to abuse ZIP files but only if users 
opt in. Multiple threats used compressed archives in their attachments in 2022, 
including Bumblebee, IcedID, and Qbot. 
Container files 
Optical Disk Image (ISO) files and Virtual Hard Drive (VHD) files are two types of 
container files we’ve seen delivered inside compressed archives in an attempt 
to evade MOTW restrictions. Container files like ISOs do not support a Zone 
Identifier ADS attribute and did not have a MOTW until Microsoft’s November 
2022 patch propagated MOTW flags to both the ISO and its contents. Proofpoint 
reported a 150 percent increase in the use of ISO files in malicious campaigns 
between October 2021 and June 2022. IcedID is one example of a threat that 
used ISOs, and Bumblebee leveraged both ISOs and VHDs in 2022. 
Web trends: SEO poisoning  
and malvertising
Search engine optimization poisoning 
Search engine optimization (SEO) poisoning continued to be an effective 
technique for gaining initial access in 2022. Many threats leveraged SEO 
poisoning, including Gootloader, Yellow Cockatoo, and various stealers. 
Adversaries create malicious websites that use SEO techniques like placing 
strategic search keywords in the body or title of a webpage. They attempt to 
make their malicious sites more prominent than legitimate sites when search 
results are returned by Google and other search engines. As an example, 
Zloader—also known as BATLOADER—has used keywords like “free software 
development tools” to encourage victims to navigate to their site and download 
evil installers. Another example, Gootloader, has used websites claiming to offer 
information on contracts and other legal or financial documents. This trend 
shows no signs of slowing as we move into 2023; in late 2022, one SEO poisoning 
campaign targeted almost 15,000 websites.
14
Malvertising 
SEO poisoning is not the only way adversaries use search engines to their 
advantage. Malicious advertising, also called malvertising, also persisted in 2022. 
Malvertising is the use of fake ads on search engine pages that masquerade as 
legitimate websites to download software like Zoom or TeamViewer. Threats that 
used malvertising extensively in 2022 include AdSearch, IcedID, and  
Stealers malware. 
File type trends: LNK and MSI
LNK files 
Windows shortcut files, also known as LNK files, have also seen increased 
adversarial use in 2022. Proofpoint reported a 1,675 percent increase in LNK 
files in malicious campaigns between October 2021 and June 2022. LNK files 
are neither compressed archives nor container files. Instead, LNK files provide 
adversaries a way to execute binaries, scripts, and other arguments. Based on 
the specific arguments configured when a LNK file is created, it can point to and 
execute files or include scripts configured to download additional malware. 
Some prominent threats that leveraged LNK files in 2022 include Emotet, 
Bumblebee, and other families of non-phishing malware like Raspberry Robin.
Windows Installer (MSI) files 
When the stealer Zloader combined malvertising and SEO poisoning in 2022, 
its installer took the form of Windows Installer (MSI) files. MSI files are used to 
install and update legitimate software on Windows systems. They are also used 
by adversaries to install malicious binaries, run scripts, and elevate system 
privileges. Zloader’s malicious MSI files appeared to be installers for versions of 
legitimate software. Other threats have used MSI files in their intrusions in 2022, 
including Qbot and Raspberry Robin.
What’s old is new again: USBs 
Continuing the theme of everything old being new again, a number of threats 
leveraged infected USB external drives for initial access in 2022. USBs containing 
malicious payloads that infect systems when plugged in have been an evergreen 
problem in information security for a number of reasons. As with any external 
device, security teams have less control and visibility into what they may have 
installed on them. One notable threat spread by USBs this year is Raspberry 
Robin. Many types of USB malware, such as worms, establish persistence 
that can continue for years. In 2022, Gamarue exemplified how pre-existing 
infections can be exploited by threat actors. FIN7 and other espionage groups 
also leveraged USBs in 2022. 
15
Visit the Initial access tradecraft trend page for relevant detection 
opportunities and atomic tests to validate your coverage.
Preventing container files from executing can be an effective way to avert 
damaging intrusions that attempt to evade MOTW controls. If your users do not 
have a business need to mount container files, we recommend taking steps to 
prevent Windows from auto-mounting container files. You can find additional 
mitigation guidance in the Techniques section of this report. 
One way to mitigate the effects of SEO poisoning is to prevent the malicious 
files from being able to execute. For example, Gootloader uses JScript (.js) files. 
If your users do not have a need to execute .js files, associating .js files to open 
with notepad.exe instead of wscript.exe can prevent automatic execution of 
their malicious content.
There are several options to mitigate the threat USB devices can pose in your 
environment. The best option for your organization will vary based on your 
use cases and business needs. One option could be to use group policies 
to restrict who can read, write, and execute actions from USB devices. Other 
options for mitigating USB risks can be found on the Gamarue page.
TAKE ACTION
16
TREND
Commercial and open source C2 and post-exploitation frameworks save red 
teamers time on custom development and allow them to quickly change TTPs 
in their engagements. Not surprisingly, adversaries also find them attractive 
due to their ease of use and flexibility. Since there’s no universally agreed upon 
definition that differentiates C2 from post-exploitation frameworks, we chose to 
analyze both collectively in this section. 
Adversaries have long used open source and leaked versions of commercial 
frameworks, most notably Metasploit and Cobalt Strike. While Cobalt Strike  
has received a lot of attention and remains Red Canary’s most-observed 
framework, both red teamers and adversaries have begun to leverage  
alternative frameworks.
Cobalt Strike and Metasploit continue to be the most popular C2 and  
post-exploitation frameworks seen in our customers’ environments. Cobalt 
Strike was the highest-ranking framework, coming in at #8, followed by 
Metasploit ranking 14th. While they didn’t break into our top 50 for 2022,  
Brute Ratel, Sliver, and Mythic may continue to gain popularity as adversaries 
look for alternative frameworks, so they’re worth keeping an eye on.
Brute Ratel 
Brute Ratel is a commercial post-exploitation framework with implants  
that can take many forms, including executables, service binaries, DLLs, and 
PowerShell scripts. It is capable of moving laterally via Server Message Block 
(SMB), escalating privileges, and creating processes to inject itself into for 
defense evasion. Qbot was observed delivering Brute Ratel in 2022.
Sliver 
Sliver is an open source post-exploitation framework written in Go. It executes 
commands through PowerShell or the Windows Command Shell. It supports 
several protocols for C2 including HTTP, WireGuard, and DNS. TA551 reportedly 
used Sliver in 2021, and in 2022 Team Cymru observed at least two distinct 
campaigns using it. In 2022, adversaries also took advantage of Sliver’s support 
for macOS.
Move over Cobalt Strike: Adversaries and testers have more options for 
command and control (C2) and post-exploitation frameworks than ever.
Command  
and control  
frameworks
17
Mythic 
Mythic is an open source post-exploitation framework that has a variety of 
agents and supports multiple protocols for C2 including TCP, HTTPM, DNS, 
and SMB. Two popular agents are Apfell and Apollo. Apfell is a JavaScript for 
Automation script for OSX. Apollo is a .NET Windows agent which by default 
can create and inject into Rundll32. It also has the ability to execute PowerShell 
commands. It supports using Mimikatz for lateral movement and credential 
dumping. Like Sliver, Team Cymru was able to tie some Mythic servers to 
adversaries in the wild.
Visit the Command and control frameworks trend page for relevant 
detection opportunities and atomic tests to validate your coverage.
TAKE ACTION
18
The last few years have seen organizations embrace remote work and 
technologies that allow employees to work outside the traditional perimeter of 
an enterprise network. Technologies that allow this kind of work to occur include 
VPNs, remote access solutions, web applications, and more, and all of these 
technologies require one thing to get started: credentials. As the enterprise 
network perimeter becomes less important, the access of employees becomes a 
point for adversaries to target for initial and persistent access to organizations. 
Information stealer malware such as RedLine, Vidar, and Raccoon all gather 
credentials from various sources on a computer system, including password 
managers, web browsers, files on disk, and more. When used properly, an 
instance of stealer malware can gather credentials that enable privileged and 
persistent access to an enterprise in the course of a minute or less.
Stealing the spotlight 
Red Canary and the larger information security community seemed to witness a 
rise in the use of stealer malware in 2022, with several stealers making it into our 
top 10 lists during various months throughout the year. We observed RedLine, 
Raccoon, and Vidar malware across multiple customer environments in various 
industries. We observed that no industry is immune to stealer malware and the 
spread of such malware is often opportunistic, usually through advertising and 
SEO manipulation. Most often masquerading the malware as fake or trojanized 
installer files, adversaries found victims unwittingly looking for malware on 
compromised or fake sites disguised as download pages for legitimate tools. In 
many of these instances, the adversaries deploying the malware also chose to 
sharply increase the size of their malware files with padding to prevent security 
tools and sandboxes from effectively handling the stealers during analysis. This 
large sample size can significantly hinder analysis with sandboxes due to upload 
size restrictions, and it can hinder analysis tools on your local system by causing 
them to slow down while processing a large file.
This use of stealers gained high visibility in 2022 thanks to LAPSUS$ conducting 
high-profile breaches. As part of their strategy to gain initial access to targeted 
organizations, LAPSUS$ relied on gaining initial access with credentials 
taken by RedLine and other stealer malware and sold afterward. This strategy 
proved extremely successful, resulting in multiple breaches for high-profile 
organizations such as Uber and Okta.
Stealer malware—such as RedLine, Raccoon, and Vidar—
enabled some of the highest-profile breaches in 2022.
TREND
Stealers
19
We observed RedLine, Raccoon, and Vidar most commonly during the year, 
and each of these threats has retained a long-held share of the illegal stealer 
market. In fact, Raccoon and Vidar have evolved from older families to remain 
relevant and effective. While these stealers took the spotlight, additional stealers 
operated at lesser prevalence during the year, including some new players such 
as Aurora Stealer, OriginLogger, and Rhadamanthys. Adversaries looking for 
stealer malware find no shortage of options that simply evolve and grow  
with efficacy.
TAKE ACTION
Visit the Stealers trend page for relevant detection opportunities and atomic 
tests to validate your coverage.
20
TREND
Users continue to be the weakest link in the initial chains of compromise we 
investigate. Virtual identities used by humans are the critical enabler of breaches 
that lead to intellectual property theft, ransomware, and cryptomining, to 
name just a few. It’s critical for defenders to adopt detection technologies and 
strategies that thwart identity compromises earlier in the intrusion chain. 
In 2022 adversaries demonstrated their talents for circumventing several 
types of identity verification technologies that security teams use to prevent 
unauthorized use of compromised credentials. Namely, adversaries got smarter 
in their approaches to circumventing multi-factor authentication (MFA) and 
geographic/trust-based detection heuristics. 
In most scenarios, their techniques tricked end users into accepting “ghost” MFA 
requests, commonly through a technique known as MFA Request Generation, 
which we’ve covered in depth in the Techniques section of this report. In brief, it 
involves a victim yielding to the annoyance of MFA prompts that they just want 
to go away, inadvertently enabling initial access for an adversary. In cases where 
adversaries failed to gain access to systems after initial MFA bypass, they often 
abused the trust of public cloud infrastructure to bypass single points of failure 
in static geographic or hosting provider checks performed by identity access 
management