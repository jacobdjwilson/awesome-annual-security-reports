C a t o   N e t w o r ks :

The Cato
CTRL SASE
Threat Report

Q 1     |   2 0 2 4

Table of
Contents

Executive Summary

Introduction

About Cato CTRL

Report Structure

Section 1: General Statistics

Inbound Threats

Outbound Threats

WANbound Threats

Section 2: Mitigated Vulnerabilities (CVEs)

Inbound Traffic

Outbound Traffic

Section 3: Suspicious Activity Monitoring (SAM)

Outbound SAM

WANbound SAM

Section 4: Enterprise Security Behavior

Secure vs. Insecure Protocols

Application Usage

Section 5: Hacking Communities

Tooling

Deepfake

Careers and Development

Section 6: Recommended Actions

3

6

8

9

11

12

13

15

19

20

22

25

27

30

33

34

38

41

42

43

46

47

Executive
Summary

Below are key takeaways
from this quarter’s analysis:

AI takes the enterprise by storm
The most common AI tools used among enterprises were Microsoft Copilot,
OpenAI ChatGPT, and Emol, an application that records emotions and talks
with AI robots. The strongest adoption of these tools was seen in the travel
& tourism industry (79%), and the lowest adoption among entertainment
organizations (44%).

Get a peek into the hacker underground
As part of its research, Cato CTRL monitors discussions from various
hacker forums. The report found attackers discussing how to jailbreak
ChatGPT to create custom SQLMap commands. We spotted
advertisements for services for generating fake credentials and creating
deep fakes. We also continued to monitor recruitment for creating a
malicious ChatGPT.

3

The Cato CTRL SASE Threat Report Q1 2024

Executive Summary

Beware of where you shop
Threat actors are setting up domains that mimic well-known brands.
Booking, Amazon, and eBay are the most spoofed brands.

Enterprises are too trusting within their networks
Many enterprises continue to run unsecured protocols across their WAN,
with 62 % of all web application traffic being HTTP, 54% of all traffic being
telnet, and 46% of all traffic being SMB v1 or v2 instead of SMBv3. Lateral
movement—where attackers will move across networks—was identiﬁed
particularly in the agriculture, real estate, and travel and tourism industries.

Zero-day is the least of your problems
While we in the industry pay a lot of attention to zero-day threats the reality is
that threat actors are often trying to exploit unpatched systems, eschewing
the use of the latest vulnerabilities and instead exploiting unpatched systems.
For example, three years after its discovery, Log4J (CVE-2021-44228)
remains one of the most used exploits.

Security varies between industries
Vulnerabilities and techniques are common across industries, but there are
ones speciﬁc to industries. Entertainment, Telecommunication, and Mining &
Metals are being targeted with T1499 – Endpoint Denial of Service techniques
more than other sectors. In the Services and Hospitality sectors, threat actors
utilize the T1212—Exploitation for Credential Access more than in other
sectors. Finally, 50% of media and entertainment organizations don’t use
information security tools.

4

The Cato CTRL SASE Threat Report Q1 2024

Executive Summary

Even benign activity is becoming suspicious
As attackers evolve their techniques, they use actions and methods that might
otherwise be considered benign. How can organizations detect and stop them
before it’s too late? Through a deep understanding of network traffic patterns and
the use of AI/ML algorithms, Cato has developed suspicious activity monitoring
(SAM) for this very reason.

A case in point is dynamic DNS services traffic. Nearly half (44%) of
organizations have outbound traffic to dynamic DNS. Alone, dynamic DNS traffic
should not be blocked, as there are legitimate uses. However, many attackers
rely on dynamic DNS for their activities. By understanding the greater context
around dynamic DNS traffic, organizations can identify whether or not this traffic
is malicious.

The “Un”adoption of DNSSEC
Our data indicates that only 1% of DNS traffic utilizes Secure DNS.
We believe this is primarily due to DNS being a critical component of both the
internet and organizational operations. Organizations fear that implementation
complexities might result in misconﬁgurations, potentially disrupting their
applications and services.

5

The Cato CTRL SASE Threat Report Q1 2024

Introduction

Threat actors are always evolving. Whether it is nation-state actors,
cybercrime groups, ransomware gangs, or niche teams targeting speciﬁc
systems – new tools, techniques, and procedures are constantly introduced
by attackers. Cyber Threat Intelligence (CTI) remains fragmented and
isolated to point solutions rather than being collected and analyzed with a
holistic view that includes external data, inbound (and outbound) threats,
and network activity (WANbound). Without such a holistic view it’s difficult
to accurately evaluate the true state of cybersecurity within enterprises.

To address that need, Cato CTRL, the CTI group of Cato Networks, tapped
the data lake underlying Cato SASE Cloud to develop a holistic view of
enterprise threats. As the global network, Cato has granular data on every
traffic ﬂow from every endpoint communicating across the Cato SASE
Cloud platform. This massive data lake is further enriched with hundreds of
security feeds and analyzed by proprietary ML/AI algorithms and human
intelligence. The result is a unique data repository providing Cato CTRL
insights into the security threats and their identifying network
characteristics for all traffic, regardless of whether they emanate from or
are destined for the Internet or the WAN for all endpoints – sites, remote

6

The Cato CTRL SASE Threat Report Q1 2024

Introduction

users, and cloud resources. Even where Cato’s multitiered defense strategy
has blocked the attack, the threats are logged and identiﬁed, enabling this
kind of analysis.

This report summarizes ﬁndings Cato CTRL gathered from Cato traffic ﬂows
across more than 2,200 customers during the ﬁrst quarter of 2024. During
the quarter, we analyzed 1.26 trillion network ﬂows and blocked 21.45 billion
attacks. (To put that in context, that’s nearly four times more ﬂows than the
350 billion ﬂows we analyzed for Q1 2022.)

This report offers insights into the threats and suspicious activity across
those ﬂows. It also provides strategic, tactical, and operational information
on all traffic in all directions utilizing the MITRE ATT&CK framework. In
addition, the report highlights the applications, protocols, and tools running
on these networks.

7

The Cato CTRL SASE Threat Report Q1 2024

About
Cato CTRL

Cato CTRL is the only CTI group to fuse threat
intelligence with granular network insight made
possible by the ﬁrst and only global SASE platform,
the Cato SASE Cloud.

With dozens of former military intelligence analysts, researchers, and data
scientists, as well as industry-recognized security professionals, Cato CTRL
utilizes network data, security stack data, hundreds of security feeds, human
intelligence operations, AI and ML (Machine Learning) models, and more,
shedding light on the latest threats and threat actors.

Using industry-standard frameworks such as MITRE ATT&CK, multiple
intelligence disciplines, and years of ﬁeld experience with red and blue team
techniques, Cato CTRL conducts the full intelligence lifecycle of collecting,
processing, analyzing, and producing cutting-edge CTI. Whether it is
tactical data for the SOC, operational threat landscape for managers, or
strategic intel for management and board, Cato CTRL has you covered.

8

The Cato CTRL SASE Threat Report Q1 2024

Report
Structure

This report is divided into six sections

General Statistics
This section provides an overview of the general statistics and metrics collected
from the private global networks relying on the Cato SASE Cloud Platform.

Mitigated Common Vulnerabilities
and Exposures (CVEs)

This section discusses the CVEs identiﬁed and mitigated within Cato’s
systems. Highlighted are the proactive measures to address known
vulnerabilities and prevent potential exploits.

9

The Cato CTRL SASE Threat Report Q1 2024

Report Structure

Suspicious Activity Monitoring (SAM)
Security Events
This section explores the security events that might otherwise be
considered benign but are identiﬁed as being associated with attacks on
Cato’s SAM system. By analyzing these events, Cato CTRL identiﬁes
potential threats, anomalies, and patterns that require further
investigation or immediate action.

Enterprise Security Behavior
In this section, Cato CTRL delves into organizations’ security behavior,
examining the usage of secure and insecure protocols, employee
applications, and other relevant data points.

Hacking Communities and AI Tool
Usage by Threat Actors

Cato CTRL closely monitors threat actor activities in forums, the dark web, and
private chat channels to gain insights into threat actor’s latest trends and
techniques, and in particular, the growing use of artiﬁcial intelligence (AI) tools.

Recommended Actions for Security Improvement
In the ﬁnal section, Cato CTRL provides actionable recommendations based on
the ﬁndings from the previous sections.

10

The Cato CTRL SASE Threat Report Q1 2024

S e c t i o n   1

General
Statistics

General Statistics

To stop cyberattacks, enterprises should be using house machine learning
modules based on company data and threat intelligence feeds. They also need
to be careful of compromised systems within their organizations. Threat actors
are leveraging them to scan (mainly SMB scanning) the network for
vulnerabilities. Lateral movement threats were particularly prominent within
lateral movement threats within the agriculture, real estate, and travel &
tourism industries. Education experiences more brute force attacks than other
industries. Users should continue to be educated about online fraud and
phishing when web browsing, particularly when visiting Apple, Amazon, and
Booking. The three were the most spoofed brands in our research.

Inbound Threats
The most common type of inbound threat was detected by our reputation engine.
Some examples of reputation-based threats found in our research include. IP feeds
for exploitation, spam, scanners and malicious domains.

4% 2%

2%

1%

Top Inbound Threats

Reputation

Network Scan

Web Application
Attack

Vulnerability Scan

Brute Force

91%

12

The Cato CTRL SASE Threat Report Q1 2024

General Statistics

When we break down the inbound threats by industry verticals, we see that the
healthcare sector leads in web application attacks and scanning activities,
while education suffers from the most brute-force attacks of any industry. These
attacks are being launched against Remote Desktop Protocol (RDP) ports

Inbound Threats by Industry Verticals

100%

90%

80%

70%

60%

50%

40%

30%

20%

10%

0%

Web Application Attack

Vulnerability Scan

Remote Code Execution

Network Scan

Lateral Movement

Outbound Threats
Network scans (87% of ﬂows associated with outbound threats) were the most
common outbound threat, a basic tool for attackers to use in reconnaissance for
targets outside the organization. Most attacks are mitigated during the network
scan, blocking attempts to scan public services. Most blocked traffic from outbound
threats, though, stems from attempts to scan SMB ports.

13

The Cato CTRL SASE Threat Report Q1 2024

General Statistics

4% 1% 0%

8%

Top Outbound Threats

Network Scan

Command and Control

Reputation

Malware

Exﬁltration

87%

When analyzing outbound threats across industry verticals, we ﬁnd that the
consulting and media sectors are more vulnerable to exﬁltration threats than other
sectors. Within the consulting sector, data is more commonly being sent by FTP to
low-reputation domains. Regardless of the sector, the most common approach to
preventing attacks is being done by Cato’s reputation-based mitigation engine.

14

The Cato CTRL SASE Threat Report Q1 2024

General Statistics

Outbound Threats by Industry Verticals

100%

90%

80%

70%

60%

50%

40%

30%

20%

10%

0%

Reputation

Network Scan

Malware

Exﬁltration

Command and Control

Upon examining outbound traffic, it is evident that most attacks are being mitigated
during the network scan, indicating that attempts to scan public services are being
blocked. Analysis of the data reveals that the majority of the blocked traffic consists
of attempts to scan SMB ports.

WANbound Threats
In web application attacks, we witnessed multiple attempts to detect vulnerable web
applications by scanning known URLs. We also saw lateral movement in the
Windows environment, where attempts were made to use Windows Management
Instrumentation (WMI) to query system information and then execute commands
remotely. We also saw heavy use of WinRS Encrypted Execution to hide malicious
code in Windows Remote Shell (WinRS) by encrypting it.

15

The Cato CTRL SASE Threat Report Q1 2024

General Statistics

3% 2% 2%

9%

Top WANbound Threats

Network Scan

Web Application Attack

Lateral Movement

Vulnerability Scan

Remote Code Execution

84%

Agriculture, real estate, and travel & tourism experienced the most
lateral-movement-related activities when compared to other industries

WANbound Threats by Industry Verticals

100%

90%

80%

70%

60%

50%

40%

30%

20%

10%

0%

16

Web Application Attack

Vulnerability Scan

Remote Code Execution

Network Scan

Lateral Movement

The Cato CTRL SASE Threat Report Q1 2024

General Statistics

Top Spoofed Brands
Cybercriminals often exploit strong brands in their attacks, using tactics
such as phishing and spooﬁng. Cybersquatting, also known as domain
squatting, involves using a domain name to proﬁt from the reputation and
recognition of a trademark that belongs to someone else. To combat this
issue, Cato Networks has developed a machine-learning algorithm that
can successfully detect instances of cybersquatting.

Top Spoofed Brands

11

35

250

200

150

100

201

50

0

5

62

89

1
4

132

1
8

28

60

3

79

20

85

1

34

14

2

1
16

26

0

31

10

1

24

14

Booking

Amazon

Ebay

Pinterest

Google

Apple

Netﬂix

Microsoft

Instagram

Youtube

homographsquatting

levelsquatting

typosquatting

combosquatting

Booking, Amazon and Ebay were the top three spoofed brands using at
least one of four techniques:
• Typosquatting creates domain names that incorporate typical typos
users input  when attempting to access a legitimate site, such as
“catonetwrks.com”, which leaves out the “o” in networks.
• Combosquatting creates a domain that combines the legitimate
domain with additional words or letters, such as “cato-networks.com”,
which adds a hyphen to Cato’s URL catonetworks.com.

17

The Cato CTRL SASE Threat Report Q1 2024

General Statistics

• Levelsquatting inserts the target domain into the subdomain of the
cybersquatting URL, such as login.catonetworks.com.fake.com.
• Homographsquatting uses various character combinations that
resemble the target domain visually, such as “catonet0rks.com”, which
uses a zero digit that looks like the letter “o.”
Learn more about Cybersquatting and the different types in our blog.

18

The Cato CTRL SASE Threat Report Q1 2024

S e c t i o n   2

Mitigated
Vulnerabilities
(CVEs)

Mitigated Vulnerabilities (CVEs)

As we examine mitigated vulnerabilities (CVEs) we found that while some are
shared among industries, there are also industry-speciﬁc threats. Regardless,
threat actors are trying to exploit unpatched systems and are not always using
the latest vulnerabilities. (Disclaimer: The data may contain scanner activity.)

Three years after its discovery, Apache Log4J RCE (CVE-2021-44228) remains
one of the most used exploits. Other vulnerabilities being exploited across
industries include Microsoft Exchange server-side request forgery (SSRF,
CVE-2021-26855), PHP arbitrary code execution (CVE-2017-9841), and
Microsoft Exchange server-side request forgery (CVE-2022-41040).

Within the technology sector, we saw Amazon Redshift JDBC42 Remote Code
Execution (CVE-2022-41828). The manufacturing sector showed signiﬁcant
usage of Adobe ColdFusion Insecure Deserialization (CVE-2023-26360). Within
the construction sector, we saw the use of SolarView Remote Code Execution
(CVE-2023-23333).

Inbound Traffic
As seen in the data, newer vulnerabilities do not necessarily mean that they
are the most common. The pie chart shows threat actors targeting unpatched
vulnerabilities, some of which are quite old. For example, one well-known
attack found across 33% of customer ﬂows targets the PHPUnit testing
framework (CVE-2017-9841), which allows for arbitrary code execution in
PHP, has been around for more than seven years.

20

The Cato CTRL SASE Threat Report Q1 2024

Mitigated Vulnerabilities (CVEs)

5%

8%

11%

3% 3%

3%

4%

Top 10 Inbound CVE by
Traffic Volume

33%

CVE-2017-9841 PHP arbitrary code execution vulnerability

CVE-2021-44228 - Apache-Log4j Remote Code Execution

CVE-2022-41040 - Microsoft Exchange server-side request forgery (SSRF)

CVE-2022-21371 - Oracle WebLogic Server Local File Inclusion

CVE-2021-43798 - Grafana Directory Traversal

CVE-2021-41773 - Apache HTTP Server Path Traversal

CVE-2018-19629 - Denial of Service vulnerability in the ImageNow Server

CVE-2021-26855 - Microsoft Exchange server-side request forgery (SSRF)

Dasan GPON home routers bypass authentication. This vulnerability is broadly used
by Mirai and may indicate an infected device.

CVE-2021-34523 - ProxyShell - Microsoft Exchange Server Elevation of Privilege

12%

18%

We have classiﬁed each CVE according to its corresponding tactic in MITRE ATT@CK
Technique (see this blog for a detailed explanation of ATT@CK). Our analysis reveals
that threat actors are targeting Entertainment, Telecommunication, and Mining &
Metals with T1499 – Endpoint Denial of Service techniques more than other sectors.

Inbound Traffic - MITRE ATT&CK Techniques by Industry for
Common Vulnerabilities and Exposures (CVEs)

Not mapped

100%

90%

80%

70%

60%

50%

40%

30%

20%

10%

0%

T1598 - Phishing for Information

T1592 - Gather Victim Host Information

T1589 - Gather Victim Identity Information

T1583 - Acquire Infrastructure

T1566 - Phishing

T1559 - Inter-Process Communication

T1556 - Modify Authentication Process

T1552 - Unsecured Credentials

T1539 - Steal Web Session Cookie

T1528 - Steal Application Access Token

T1505 - Server Software Component

T1499 - Endpoint Denial of Service

T1498 - Network Denial of Service

T1496 - Resource Hijacking

T1485 - Data Destruction

T1221 - Template Injection

T1212 - Exploitation for Credential Access

T1211 - Exploitation for Defense Evasion

T1210 - Exploitation of Remote Services

T1204 - User Execution

T1190 - Exploit Public-Facing Application

T1136 - Create Account

T1133 - External Remote Services

T1098 - Account Manipulation

T1087 - Account Discovery

T1083 - File and Directory Discovery

T1082 - System Information Discovery

T1078 - Valid Accounts

T1072 - Software Deployment Tools

T1068 - Exploitation for Privilege Escalation

T1059 - Command and Scripting Interpreter

T1055 - Process Injection

T1049 - System Network Connections Discovery

T1041 - Exﬁltration Over C2 Channel

T1006 - Direct Volume Access

T1005 - Data from Local System

T1003 - OS Credential Dumping

21

The Cato CTRL SASE Threat Report Q1 2024

Mitigated Vulnerabilities (CVEs)

Outbound Traffic
Outbound threats refer to traffic originating within the organization and going out
to the public internet. The presence of an outbound threat may indicate that the
attacker is already present within the organization and could be using the network
to launch an attack on another enterprise. The most exploited vulnerabilities by
outbound threats in our research were Windows MSHTML elevation of privileges
(CVE-2023-29324), Apache Log4j RCE (CVE-2021-44228), and Windows DNS
Remote Code Execution (CVE-2021-26897).

2% 1% 1%

2%

4%

33%

7%

10%

10%

30%

Top 10 Outbound CVE
by Traffic Volume

CVE-2023-29324 -  Windows MSHTML Platform
Elevation of Privilege

CVE-2021-44228 - Apache-Log4j Remote
Code Execution

CVE-2021-26897 - Windows DNS Remote
Code Execution

CVE-2018-19629 - Denial of Service vulnerability
in the ImageNow Server

CVE-2021-41773 - Apache HTTP Server
Path Traversal

CVE-2021-26857 - Unsafe deserialization issue has
been identiﬁed in Exchange

CVE-2021-21872 - Lantronix PremierWave 2050
Remote Code Execution

CVE-2022-21907 - IIS Unauthenticated Remote
Code Execution

CVE-2023-22527 - Atlassian Conﬂuence
Data Center and Conﬂuence Server
Remote Code Execution

In the Services and Hospitality sectors, more so than others, threat actors
utilize the Exploitation for Credential Access. They’re trying to exploit
CVE-2023-29324 for Windows MSHTML Platform Elevation of Privileges,
a component in Internet Explorer used to render web pages.

22

The Cato CTRL SASE Threat Report Q1 2024

Mitigated Vulnerabilities (CVEs)

Outbound Traffic - MITRE ATT&CK Techniques by Industry
for Common Vulnerabilities and Exposures (CVEs)

Not mapped

100%

90%

80%

70%

60%

50%

40%

30%

20%

10%

0%

T1589 - Gather Victim Identity Information

T1566 - Phishing

T1559 - Inter-Process Communication

T1556 - Modify Authentication Process

T1552 - Unsecured Credentials

T1539 - Steal Web Session Cookie

T1528 - Steal Application Access Token

T1499 - Endpoint Denial of Service

T1212 - Exploitation for Credential Access

T1211 - Exploitation for Defense Evasion

T1190 - Exploit Public-Facing Application

T1136 - Create Account

T1133 - External Remote Services

T1083 - File and Directory Discovery

T1082 - System Information Discovery

T1078 - Valid Accounts

T1072 - Software Deployment Tools

T1059 - Command and Scripting Interpreter

T1055 - Process Injection

T1049 - System Network Connections Discovery

T1005 - Data from Local System

WANbound Traffic
The most common vulnerability in WANbound traffic is web application-related
CVEs. As you can see in the graphic, all the CVEs are related to web applications.
Additionally, the percentage of WANbound traffic associated with CVE may be
inﬂuenced by how many organizations are using vulnerability scanners to identify
vulnerable systems within their network to prevent potential exploitation because
of its severe consequences.

23

The Cato CTRL SASE Threat Report Q1 2024

Mitigated Vulnerabilities (CVEs)

5%

5%

6%

19%

7%

7%

8%

10%

16%

Top 10 WANbound CVE by
Traffic Volume

CVE-2021-44228 - Apache-Log4j Remote Code Execution

CVE-2022-21371 - Oracle WebLogic Server Local File Inclusion

CVE-2021-26085 - Atlassian Conﬂuence Server Arbitrary
File Read

CVE-2022-22963 - Spring Cloud Remote Code Execution

CVE-2021-41773 - Apache HTTP Server Path Traversal

CVE-2009-2445 - Oracle iPlanet Web Server Sensitive
Data Exposure

CVE-2020-14750 - Oracle WebLogic Server RCE

CVE-2013-0625 - Adobe ColdFusion Remote Code Execution

17%

Our analysis indicates that the most commonly used CVE in the Entertainment
sector is Text4Shell Apache Commons Text RCE (CVE-2022-42889).  Meanwhile,
in the Telecommunications sector, the most frequently used technique is Endpoint
Denial of Service (T1499).

WANbound traffic - MITRE ATT&CK Techniques by Industry
for Common Vulnerabilities and Exposures (CVEs)

Not mapped

T1598 - Phishing for Information

100%

90%

80%

70%

60%

50%

40%

30%

20%

10%

0%

T1592 - Gather Victim Host Information

T1589 - Gather Victim Identity Information

T1583 - Acquire Infrastructure

T1566 - Phishing

T1559 - Inter-Process Communication

T1556 - Modify Authentication Process

T1552 - Unsecured Credentials

T1539 - Steal Web Session Cookie

T1528 - Steal Application Access Token

T1505 - Server Software Component

T1499 - Endpoint Denial of Service

T1498 - Network Denial of Service

T1496 - Resource Hijacking

T1485 - Data Destruction

T1221 - Template Injection

T1212 - Exploitation for Credential Access

T1211 - Exploitation for Defense Evasion

T1210 - Exploitation of Remote Services

T1204 - User Execution

T1190 - Exploit Public-Facing Application

T1136 - Create Account

T1133 - External Remote Services

T1098 - Account Manipulation

T1087 - Account Discovery

T1083 - File and Directory Discovery

T1082 - System Information Discovery

T1078 - Valid Accounts

T1072 - Software Deployment Tools

T1068 - Exploitation for Privilege Escalation

T1059 - Command and Scripting Interpreter

T1055 - Process Injection

T1049 - System Network Connections Discovery

T1041 - Exﬁltration Over C2 Channel

T1006 - Direct Volume Access

T1005 - Data from Local System

T1003 - OS Credential Dumping

24

The Cato CTRL SASE Threat Report Q1 2024

S e c t i o n   3
Suspicious
Activity
Monitoring
(SAM)

Suspicious Activity Monitoring (SAM)

The threat landscape is constantly evolving, providing opportunities for threat
actors to exploit and compromise organizations in a covert manner. New methods
of bypassing security products are revealed on a weekly basis. To remain
undetected, threat actors use techniques such as LOLBAS (Living Off The Land
Binaries, Scripts, and Libraries) and LOTS (Living Off Trusted Sites). However, the
use of these techniques does not necessarily mean that your organization has
already been compromised. Additionally, other suspicious activities, such as
communication with known protocols but not via the standard port, checking
public IPs (often used in malware), and other behaviors, should also be monitored.

To tackle this issue, Cato Networks has developed SAM, a set of capabilities that
can detect suspicious, behavior and alert the organization using XDR. Each SAM
signature has an associated risk: Low, Medium, or High. We also mapped SAM
signatures to their corresponding MITRE ATT@CK tactics.

Understanding and analyzing suspicious events can help reduce an organization’s
attack surface. By monitoring suspicious activities, we can trace them back and
attribute them to speciﬁc threat actors. Based on the activity identiﬁed by
monitoring these events, honeypots and deception techniques can be deployed.

0%

46%

SAM by Traffic
Direction

Wanbound

Outbound

Inbound

54%

26

The Cato CTRL SASE Threat Report Q1 2024

Suspicious Activity Monitoring (SAM)

Outbound SAM
We can see that the highest-risk SAMs for outbound traffic are traffic to dynamic
DNS services in HTTP (44%), EXE download over non-browser HTTP traffic
(28%), and a possible malicious EXE ﬁle downloaded from a WordPress site
(12 %). Alone, these actions would not be categorized as malicious as they do not
constitute an attack. But by understanding the underlying network traffic patterns
of attacks, Cato recognizes that these actions are often part of larger threat
patterns -- hence the term “suspicious.”

2% 1% 1% 0%

2%

4%

6%

12%

28%

Top 10 HIGH Risk
Suspicious Activities
in Outbound Traffic

Traffic towards dynamicDNS services in HTTP

EXE download over HTTP non-browser traffic

Possible malicious exe ﬁle downloaded from

wordpress site.

Ngrok agent attempted to establish a tunnel

with Ngrok cloud

Downloaded Netcat

Download of a Binary File by Autoit

Downloading Splashtop

System Information Exﬁltration

Curl client downloads a portable

executable ﬁle

Rclone Exﬁltration Client

44%

If we examine the SAMs of medium-risk activities, we observe that HTTP
requests over non-standard ports to less popular destinations (21%),
WinINet/Winsock (Native Windows Client) to low-popularity domains (19%), and
IP checking services (11%) are ranked highest on the list.

27

The Cato CTRL SASE Threat Report Q1 2024

Suspicious Activity Monitoring (SAM)

Cato’s popularity score involves multiple data points, including real-time traffic
data from our network, which measures the application’s occurrences across
our network and is correlated with additional online sources. Typically, an
application that is less popular and less known poses a greater risk than a
well-established domain.

6%

7%

21%

7%

8%

8%

8%

9%

11%

Top 10 MEDIUM Risk
Suspicious Activities
in Outbound Traffic

HTTP Requests Over Non Standard Ports To

Low Popularity Destinations

Wininet/Winsock (Native Windows Client) to

low Popularity Domain

IP checking services

FTP Client (WinSCP) over SSH

Suspicious Chrome Extensions originated

not from webstore

SAM - Outbound FileZilla traffic

Wininet/Winsock (Native Windows Client) to

low Popularity IP

AnyDesk Remote Desktop Connection

Initiation

PuTTY SSH Connection To Low Reputation IP

Bot downloading EXE ﬁle

15%

In the low-risk SAMs, the top indicators are domain reputation-based signature
(newly registered domain), TLS with low reputation and non-standard ports, and
SSH to high ports.

28

The Cato CTRL SASE Threat Report Q1 2024

Suspicious Activity Monitoring (SAM)

4%

5%

5%

5%

24%

5%

7%

10%

22%

13%

Top 10 LOW Risk
Suspicious Activities
in Outbound Traffic

Domain reputation based signature - Newly
Registered Domain

TLS With Low Reputation and Non-standard Ports

SSH to High Ports

Ms-office 2016 document autoupdate attempt.

cURL over HTTP to low popularity domains

Java over HTTP to low popularity domains

Bitsadmin administration tool - using suspicious
user agent & domain

Postman over HTTP to low popularity domains

Python over HTTP to low popularity domains

Long DNS Query

Manufacturing, technology, and consumer goods are the most common industries that
engage in suspicious activities. The most prevalent threat techniques are Application
Layer Protocol (T1071), Non-Standard Port (T1571), and Ingress Tool Transfer (T1105).

Outbound Suspicious Activities by Industry Verticals

100%

90%

80%

70%

60%

50%

40%

30%

20%

10%

0%

29

Not mapped

T1588 - Obtain Capabilities

T1583 - Acquire Infrastructure

T1573 - Encrypted Channel

T1572 - Protocol Tunneling

T1571 - Non-Standard Port

T1570 - Lateral Tool Transfer

T1569 - System Services

T1568 - Dynamic Resolution

T1567 - Exﬁltration Over Web Service

T1566 - Phishing

T1531 - Account Access Removal

T1505 - Server Software Component

T1219 - Remote Access Software

T1204 - User Execution

T1197 - BITS Jobs

T1176 - Browser Extensions

T1105 - Ingress Tool Transfer

T1102 - Web Service

T1090 - Proxy

T1087 - Account Discovery

T1071 - Application Layer Protocol

T1059 - Command and Scripting Interpreter

T1057 - Process Discovery

T1048 - Exﬁltration Over Alternative Protocol

T1041 - Exﬁltration Over C2 Channel

T1021 - Remote Services

T1020 - Automated Exﬁltration

T1016 - System Network Conﬁguration Discovery

The Cato CTRL SASE Threat Report Q1 2024

Suspicious Activity Monitoring (SAM)

WANbound SAM
We can see that the median-risk SAMs for WAN-bound traffic are LDAP Search
Query – Groups (53%), Querying Groups in the Domain (28%), and Moving
Executable Laterally to a Temp directory (8%).

2% 2% 1% 0% 0%

6%

8%

28%

Top 10 HIGH Risk
Suspicious Activities
in WANbound Traffic

LDAP Search Query - Groups

Querying Groups in the Domain

Moving Executable Laterally To a Temp directory

Execution of Remote RemCom Service

Using PsExec to Transfer Executable in SMB

Execution of Remote PAExec Service

WinRM Unecrypted Execution Powershell

PSexec Impersonates as a Regular Executable

Transferring Mimikatz over SMB

53%

30

The Cato CTRL SASE Threat Report Q1 2024

Suspicious Activity Monitoring (SAM)

After analyzing the SAMs of WANbound traffic that pose a medium risk, we have
observed that three actions are the most common. These actions include
Enumerating All Users on the Domain Controller by using SAMR RPC (14%),
Querying Admin Groups in the Domain (14%), and Querying a Built-in
Administrator Account (12 %).

7%

7%

14%

8%

8%

8%

11%

11%

Top 10 MEDIUM Risk
Suspicious Activities
in WANbound Traffic

Enumerating All Users on the Domain Controler -
Using SAMR RPC

Querying Admin Groups in the Domain

Querying A Built-in Administrator Account

LDAP Search Query - Domain Computers

Executable File Transfer Over SMB With
Impersonated Extension

Create new service on remote host via windows
service manager

Execute service on remote host via windows service
manager

Executing Commands on a Remote Computer
Using WMI

Delete service on remote host via windows
service manager

FTP Client (WinSCP) over SSH

14%

12%

In WANbound traffic, the top indicators for low-risk SAMs are remotely querying a
computer using WMI, long DNS queries, and registering a new scheduled task on
the remote host.

31

The Cato CTRL SASE Threat Report Q1 2024

Suspicious Activity Monitoring (SAM)

9%

14%

14%

Top 10 LOW Risk
Suspicious Activities
in WANbound Traffic

Remotely Querying a Computer
Using WMI

Remotely Querying a Computer
Using WMI

Registering a new scheduled task
on the remote host

Transferring a Powershell Script
Over SMB

63%

Our analysis indicates that the most commonly used CVE in the Entertainment
sector is Text4Shell Apache Commons Text RCE (CVE-2022-42889).  Meanwhile,
in the Telecommunications sector, the most frequently used technique is Endpoint
Denial of Service (T1499).

WANbound Suspicious Activities by Industry Verticals

100%

90%

80%

70%

60%

50%

40%

30%

20%

10%

0%

32

Not mapped

T1570 - Lateral Tool Transfer

T1569 - System Services

T1558 - Steal or Forge Kerberos Tickets

T1505 - Server Software Component

T1486 - Data Encrypted for Impact

T1482 - Domain Trust Discovery

T1210 - Exploitation of Remote Services

T1190 - Exploit Public-Facing Application

T1105 - Ingress Tool Transfer

T1087 - Account Discovery

T1071 - Application Layer Protocol

T1069 - Permission Groups Discovery

T1059 - Command and Scripting Interpreter

T1053 - Scheduled Task/Job

T1048 - Exﬁltration Over Alternative Protocol

T1047 - Windows Management Instrumentation

T1041 - Exﬁltration Over C2 Channel

T1021 - Remote Services

T1020 - Automated Exﬁltration

T1018 - Remote System Discovery

T1016 - System Network Conﬁguration Discovery

The Cato CTRL SASE Threat Report Q1 2024

S e c t i o n   4
Enterprise
Security
Behavior

Enterprise Security Behavior

Enterprises have long trusted their legacy MPLS networks, sending data
unencrypted and relying on edge ﬁrewalls for protection. Unfortunately, that
belief continues for many today, as they use insecure protocols for their
WANbound communications. This is a mistake, but it’s not the only one common
to enterprises. DNSSEC, which could be valuable in protecting against many
attacks, has not gained momentum.

Application use of AI tools is evident across all sectors. The technology and
manufacturing sectors have increased their use of AI tools monthly. We have also
observed that many of the surveyed entertainment organizations lack adequate
information security tools.     In addition, each industry vertical uses a unique set
of applications and protocols, which may expose them to different threats.

Secure vs. Insecure Protocols
One of the best ways to reduce an organization’s attack surface is to use secure
protocols. In this section, Cato CTRL examines the use of such protocols within
the enterprise.

HTTP vs. HTTPS
The HTTP traffic analysis clearly shows that many organizations do not encrypt
their WAN traffic. This means that if an adversary is already inside the
organization’s network, they can eavesdrop on unencrypted communications
that may include personal identiﬁable information (PII) or sensitive information
such as credentials, further helping them in their lateral movement.

HTTP vs HTTPS

WANBOUND
HTTP vs HTTPS

INBOUND
HTTP vs HTTPS

OUTBOUND
HTTP vs HTTPS

19%

38%

27%

11%

81%

62%

73%

89%

HTTP

HTTPS

34

The Cato CTRL SASE Threat Report Q1 2024

Enterprise Security Behavior

After analyzing the WANbound traffic by industry verticals, we found that the top
industries not using HTTPS for WAN traffic are manufacturing, consumer goods,
construction, travel & tourism, and hospitality. Additionally, there is unencrypted
HTTP traffic within all industry verticals.

WANbound HTTP/HTTPS Traffic by Industry Verticals

100%

90%

80%

70%

60%

50%

40%

30%

20%

10%

0%

HTTP

HTTPS

SMB v1 and v2 vs. SMB v3
The Microsoft environment has long relied on the Server Message Block (SMB)
protocol for ﬁle sharing and other purposes. Our data shows that most
enterprises continue to rely on SMB v1 and v2 (66%) despite their well-known
vulnerabilities, such as EternalBlue and denial of service (DoS) attacks.
Microsoft’s latest version of the protocol, SMB v3, has ﬁxed many of these
vulnerabilities and enforces AES-128-GCM encryption, a robust encryption
standard.

35

The Cato CTRL SASE Threat Report Q1 2024

Enterprise Security Behavior

As we look at SMB adoption by industry, the top industries that still use SMB v1
and v2 are manufacturing, consumer goods, automotive, medical/healthcare,
and ﬁnance.

SMB V1 AND V2 VS SMB V3

WANBOUND
SMB V1 AND V2 VS SMB V3

INBOUND
SMB V1 AND V2 VS SMB V3

OUTBOUND
SMB V1 AND V2 VS SMB V3

34%

46%

31%

100%

66%

54%

69%

SMB_v1_v2

SMB_v3

SSH vs. TELNET
SSH is the most secure method for accessing remote servers. While
organizations increasingly use secure connections for inbound and outbound
traffic, Telnet is still being utilized inside the organizations.

SSH vs TELNET

WANBOUND
  SSH vs TELNET

INBOUND
  SSH vs TELNET

39%

54%

6%

OUTBOUND
  SSH vs TELNET
1%

61%

46%

94%

99%

SSH

TELNET

36

The Cato CTRL SASE Threat Report Q1 2024

Enterprise Security Behavior

In terms of industries, our analysis shows that Telnet is more prominent than SSH
in WANbound traffic for law practices, ﬁnance, automotive, mining & metals, and
oil & energy sectors.

WANbound Telnet/SSH Traffic by Industry Verticals

100%

90%

80%

70%

60%

50%

40%

30%

20%

10%

0%

SSH

TELNET

DNS vs. DNSSEC
DNS plays a crucial role on the internet. Since DNS’s invention in 1983 multiple
vulnerabilities have been found, such as DNS cache poisoning and
man-in-the-middle attacks. Consequently, there was a need for a more secure
DNS. In 1997, the ﬁrst speciﬁcation of DNSSEC was published. A signiﬁcant
milestone in 2010 was the signing of the root zone. Cato’s analysis of network
traffic revealed that there has been limited adoption of DNSSEC.

37

The Cato CTRL SASE Threat Report Q1 2024

Enterprise Security Behavior

DNS vs DNSSEC

0%

3%

WANBOUND
DNS vs DNSSEC
3%

INBOUND
DNS vs DNSSEC

OUTBOUND
DNS vs DNSSEC
2%

2%

97%

97%

100%

96%

DNS_OVER_U

DNSSEC

DNS_OVER_TCP

LLMNR vs. NetBIOS
LLMNR and NetBIOS are both used to resolve names on local networks. LLMNR
is designed as the successor of NetBIOS, aiming to provide a more secure
fallback option when DNS fails. However, using LLMNR and NetBIOS can pose
signiﬁcant security risks, such as LLMNR poisoning, SMB Relay Attacks,
Pass-the-Hash Attacks, and more. The alternative is to utilize a local DNS server.
Our analysis indicates that all industry verticals still rely on LLMNR and NetBIOS,
with NetBIOS being the most commonly used.

Application Usage
In addition to investigating protocol usage across enterprises, Cato CTRL
investigated application usage. The Cato SASE Cloud identiﬁes and classiﬁes
thousands of applications within the enterprise. We examined the three types of
applications – AI tools, information security, and anonymizers.

AI Tools
The most common AI tools used among enterprises were Microsoft Copilot,
ChatGPT, and Emol, an application that records emotions and talks with AI
robots. Copilot’s strong adoption is likely due to its integration across Microsoft
products. The strongest adoption of these tools was seen in the travel and
tourism industry (79%), and the lowest adoption was among entertainment
organizations (44%).

38

The Cato CTRL SASE Threat Report Q1 2024

Enterprise Security Behavior

AI Tools Apps Usage by Industry Vertical

4
8
6
3
7
4
9
8
7
0

.

8
4
5
3
9
1
4
7
7
0

.

2
8
8
5
0
7
4
6
7
0

.

5
0
1
2
4
8
6
3
7
0

.

3
5
5
2
4
0
4
3
7
0

.

7
2
7
2
7
2
7
2
7
0

.

7
9
6
9
6
9
6
9
6
0

.

3
4
7
3
7
2
9
6
0

.

6
2
5
0
1
2
4
8
6
0

.

9
0
7
2
2
3
9
6
6
0

.

8
5
3
7
7
3
0
6
6
0

.

5
8
5
6
3
5
8
5
6
0

.

8
5
6
9
1
1
8
5
6
0

.

4
5
1
6
4
8
3
5
6
0

.

4
2
3
7
8
8
7
4
6
0

.

1
4
6
5
2
0
1
4
6
0

.

6
6
3
3
6
6
3
3
6
0

.

7
4
9
8
7
5
1
3
6
0

.

7
7
9
6
0
9
7
2
6
0

.

3
5
2
3
1
3
8
7
5

.

0

1
6
5
7
9
0
6
5

.

0

9
7
5
8
8
8
9
5
5

.

0

5
4
5
4
5
4
5
4
5

.

0

2
6
8
5
7
2
8
4
4
0

.

4
4
4
4
4
4
4
4
4
0

.

0.9

0.8

0.7

0.6

0.5

0.4

0.3

0.2

0.1

0

Information Security
How are companies protecting their information assets? It depends on who you ask.
The vast majority of educational organizations (82%) use information security tools,
versus less than half (48%) of entertainment organizations. The most used
information security tools are: TrendMicro, Umbrella, Bitdefender, Quad9, and ESET.

Information Security Apps Usage by Industry Vertical

4
7
4
9
8
7
5
1
8

.

0

4
8
6
3
7
4
9
8
7
0

.

8
4
5
3
9
1
4
7
7
0

.

2
8
8
5
0
7
4
6
7
0

.

1
5
8
0
8
6
4
4
7
0

.

7
2
7
2
7
2
7
2
7
0

.

6
1
3
6
2
5
0
1
7
0

.

7
0
2
7
9
4
9
0
7
0

.

7
1
7
4
5
7
0
7
0

.

7
9
6
9
6
9
6
9
6
0

.

2
9
0
7
2
2
3
9
6
0

.

2
9
6
7
0
3
2
9
6
0

.

9
2
8
6
2
9
2
8
6
0

.

8
3
3
6
5
0
6
7
6
0

.

5
0
6
8
1
4
4
7
6
0

.

3
2
9
6
7
0
3
7
6
0

.

1
1
1
0
6
3
0
7
6
0

.

7
6
6
6
6
6
6
6
6
0

.

1
5
8
4
1
5
8
4
6
0

.

7
3
3
1
8
2
1
6
0

.

1
9
0
9
0
9
0
9
5

.

0

6
4
4
1
6
3
0
9
5

.

0

4
5
8
5
6
3
5
8
5

.

0

9
7
3
1
4
2
7
1
5

.

0

1
8
4
1
8
4
1
8
4
0

.

0.9

0.8

0.7

0.6

0.5

0.4

0.3

0.2

0.1

0

39

The Cato CTRL SASE Threat Report Q1 2024

Enterprise Security Behavior

Anonymizers
When enterprises are looking to mask their browsing habits, Internet addresses, and
otherwise hide personal identiﬁable information, they turn to Anonymizers. The most
commonly used anonymizes include NordVPN, Surfshark VPN, Mullvad VPN, Hola
VPN, and AdGuard. Travel & tourism organizations are the biggest users of
Anonymizers (74%), perhaps reﬂecting the need to see local sites in planning trips
that would not be viewable from other regions, versus less than a third of
entertainment organizations.

Anonymizers Apps Usage by Industry Vertical

7
4
9
8
7
5
1
3
6
0

.

9
5
0
7
4
6
7
1
6
0

.

9
7
9
2
8
3
6
0
6
0

.

3
6
3
5
6
7
7
9
5

.

0

1
8
5
6
9
1
1
8
5

.

0

6
3
7
7
3
0
6
6
5

.

0

5
4
5
4
5
4
5
4
5

.

0

5
4
5
4
5
4
5
4
5

.

0

8
3
5
1
6
4
8
3
5

.

0

7
9
2
0
7
9
2
5

.

0

5
1
5
1
5
1
5
1
5

.

0

3
2
2
4
4
9
3
1
5

.

0

7
0
9
7
2
6
1
1
5

.

0

8
0
2
5
2
9
6
0
5

.

0

5

.

0

6
4
7
7
5
9
2
9
4
0

.

8
7
8
4
0
8
7
8
4
0

.

8
6
9
0
7
8
3
8
4
0

.

1
1
2
4
8
6
3
7
4
0

.

8
1
5
9
7
8
9
6
4
0

.

3
2
9
6
7
0
3
2
4
0

.

3
8
7
1
4
0
5
1
4
0

.

7
0
2
6
8
5
7
2
3

.

0

6
9
2
6
9
2
6
9
2

.

0

5
0
1
2
4
8
6
3
7
0

.

0.8

0.7

0.6

0.5

0.4

0.3

0.2

0.1

0

40

The Cato CTRL SASE Threat Report Q1 2024

S e c t i o n   5
Hacking
Communities

Hacking Communities

As part of Cato CTRL’s activity, we use HUMINT and OSINT to monitor for threat
actor activities. These activities include discussions, the buying and selling of
goods and services, and other related actions taken by potential adversaries.
With the recent hype around LLMs (Large Language Models) we decided to
focus on threat actors' adoption of AI/ML technologies.

Tooling
Across underground discussions, threat actors complained about the limitations
imposed by LLMs on what they can have it perform. When the ﬁrst chat based
LLMs came out, the guardrails were not high. As a result, prompts that could
potentially create malicious code and content. Today, most LLMs have rules
guarding against producing anything from potentially harmful content to
potentially copyrighted materials. Here is one example, out of many, of how
threat actors are looking for ways to jailbreak ChatGPT to create custom
SQLMap commands:

42

The Cato CTRL SASE Threat Report Q1 2024

Hacking Communities

We also observed another automated web scanner that uses AI to parse the
result and adjust the command. It uses the open-source LLAMA model by Meta:

Translation of the text -
"Advantages:

    Automation of penetration testing processes.

    Intelligent analysis of reports and recommendations for the elimination of vulnerabilities.

    Flexible settings and the ability to adapt to speciﬁc needs.

  The Llama model was used for report analysis, you can take a look at the characteristics here

  https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md

  A couple of screenshots of the project's work"

Deep Fakes
Underground services and products are not limited to malware and phishing.
Fake credentials have been bought and sold for years, and are still a thriving
industry, now fueled by the power of AI to generate top-end products. From
fake videos that can beat biometric authentication to creation of documents
and scans threat actors are experimenting with ML models to conduct
malicious activity.

43

The Cato CTRL SASE Threat Report Q1 2024

Hacking Communities

In the example below, threat actors test and share their opinions on new models
that are hosted on the Hugging Face platform (see the platform here)

Translation of the text -
"This neural network will copy any voice and use it to voice your text. They 've just rolled out a

  powerful speech synthesizer, Whisper Speech — the generation results are really impressive!

  Listen for yourself how convincingly the AI copied Peter Griffin — the written text literally spoke

  with his voice.

  Grab the free tool here. (https://huggingface.co/spaces/collabora/WhisperSpeech)”

In this conversation, we see threat actors discussing a real-time deep fake
cloning service:

Translation of the text -
"CameraI - a service for creating deepfakes. To start working, you need to write any personality as a prompt

  and connect a camera. Everything else is done by the neural network. https://www.fal.ai/camera

  Are there services that can create a voice message from a voice pattern and text?"

44

The Cato CTRL SASE Threat Report Q1 2024

Hacking Communities

Criminals are looking particularly to generate fake documents, so why not use
machine learning for such tasks? One attacker did just that:

45

The Cato CTRL SASE Threat Report Q1 2024

Hacking Communities

Careers and Development
Creating custom ML models like LLM, training models, and ﬁne-tuning models
requires work and expertise. In recent months, we have seen people marketing
their ML expert services in underground forums and cybercrime groups looking
to hire such experts to help them design their own malicious GPT variant.

Translation of the text -
"Clustering, Gradient Boosting (xgboost, LightGBM, CatBoost), k-means... I possess skills in Feature

  Engineering (construction of parameters from existing data). I am adept at ﬁne-tuning settings and

  hyperparameters for algorithms, optimal metrics for assessing model performance. I have worked with

  metrics such as Accuracy, precision, recall, F1-Score, AUC, average precision, balanced accuracy, mse,

  rmse, mspe, mae,

  The main language of programming - python. Jabber - IM Telegram: @dscoder"

Threat actors are
also recruiting
AI/ML specialists to
build custom LLMs
for malicious intent
(see this blog).

46

The Cato CTRL SASE Threat Report Q1 2024

S e c t i o n   6

Recommended
Actions

Recommended Actions

Based on the above ﬁndings, Cato CTRL
recommends enterprise IT and security
leaders take ﬁve actions:

Monitor your WAN traffic to check which insecure protocols you use and switch to
secure protocols. Continuing to run insecure protocols makes it easier for threat
actors to gather information, steal conﬁdential information traversing the network,
and exploit vulnerabilities.

Implement Zero-Trust strategies in your organization. Zero-Truest restricts users'
access to only the necessary resources, minimizing the attack surface in the event
of stolen credentials or similar attacks.

Disable LLMNR and NetBIOS and use local DNS servers. As noted, both LLMNR
and NetBIOS pose signiﬁcant security risks, which could be mitigated by relying on
local DNS servers.

Deploy vulnerability scanning in your network to ﬁnd vulnerabilities and improve
your organization's security posture. Many attacks exploit vulnerabilities that are
quite old and simply haven’t been patched. Scanning for and identifying those
vulnerabilities will go a long way to improving the enterprise’s risk posture.

Asset management is critical to mapping services, applications, and third-party
packages to detect exploitable old services and applications. Only once mapped
and understood can security teams replace the insecure protocols and remediate
the unpatched services within the enterprise, reducing the attack surface.

48

The Cato CTRL SASE Threat Report Q1 2024

Cato. WE ARE SASE.Network TransformationMPLS to SD-WAN MigrationGlobal Access OptimizationHybrid Cloud & Multi-CloudBusiness Transformation Vendor ConsolidationSpend OptimizationM&A and Geo ExpansionCato SASE Cloud PlatformConnectCloud NetworkCloud On-RampsProtectNetwork SecurityEndpoint SecurityDetectIncident Life Cycle ManagementRunUnified Management and APISecurity TransformationSecure Hybrid WorkSecure Direct Internet AccessSecure Application and Data  AccessIncident Detection and ResponseUse CasesContact Us Cato SASE Cloud PlatformAbout Cato NetworksCato provides a world-leading single-vendor SASE platform. Cato creates a seamless and elegant customer experience that effortlessly enables threat prevention, data protection,
and timely incident detection and response. Using Cato, businesses easily replace costly and rigid legacy infrastructure with an open and modular SASE architecture based on SD-WAN,
a purpose-built global cloud network, and an embedded cloud-native security stack.SaaS OptimizationSmart Egress•Dedicated IPCato ClientUniversalZTNA • EPP/EDRCato ClientUniversal ZTNA • EPP/EDRBrowser ExtensionClientlessvia Web PortalAny Edge• Any Port/Protocol •DEMAcceleration and Optimization • Selective Decryption FWaaS• SWG• IPS• DNS• NGAM• SandboxZTNA• CASB• DLP• RBI• IoT/OTThreat Prevention and Data ProtectionHigh-throughput Traffic Processing XOps (XDR + AIOps)AI/ML-driven Anomaly Detection • Analyst Workbench with Gen-AI Stories •  Incident LifecycleManagementSingle Management and API•Granular RBAC•Rich network and security analytics•Autonomous Policies•Automated Posture Management •Self-service and Co-managedMPLSCato Socket Edge  SD-WANA/A/A • Path Selection •App/Id Aware QoS • Segmentation• NGFWMulti Cloud IntegrationCato vSocket•Cloud interconnect•IPsec SPACEwwwSaaSIoTor 3rd party IPsec