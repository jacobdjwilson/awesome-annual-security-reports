Cato Networks:
The Cato
CTRL SASE
Threat Report
| Q 1   |   |   2 0 | 2 4 |
| ----- | --------- | --- |

Table of
Contents
Executive Summary 3
Introduction 6
About Cato CTRL 8
Report Structure 9
Section 1: General Statistics 11
Inbound Threats 12
Outbound Threats 13
WANbound Threats 15
Section 2: Mitigated Vulnerabilities (CVEs) 19
Inbound Traffic 20
Outbound Traffic 22
Section 3: Suspicious Activity Monitoring (SAM) 25
Outbound SAM 27
WANbound SAM 30
Section 4: Enterprise Security Behavior 33
Secure vs. Insecure Protocols 34
Application Usage 38
Section 5: Hacking Communities 41
Tooling 42
Deepfake 43
Careers and Development 46
Section 6: Recommended Actions 47

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
3 The Cato CTRL SASE Threat Report Q1 2024

Executive Summary
Beware of where you shop
Threat actors are setting up domains that mimic well-known brands.
Booking, Amazon, and eBay are the most spoofed brands.
Enterprises are too trusting within their networks
Many enterprises continue to run unsecured protocols across their WAN,
with 62% of all web application traffic being HTTP, 54% of all traffic being
telnet, and 46% of all traffic being SMB v1 or v2 instead of SMBv3. Lateral
movement—where attackers will move across networks—was identified
particularly in the agriculture, real estate, and travel and tourism industries.
Zero-day is the least of your problems
While we in the industry pay a lot of attention to zero-day threats the reality is
that threat actors are often trying to exploit unpatched systems, eschewing
the use of the latest vulnerabilities and instead exploiting unpatched systems.
For example, three years after its discovery, Log4J (CVE-2021-44228)
remains one of the most used exploits.
Security varies between industries
Vulnerabilities and techniques are common across industries, but there are
ones specific to industries. Entertainment, Telecommunication, and Mining &
Metals are being targeted with T1499 – Endpoint Denial of Service techniques
more than other sectors. In the Services and Hospitality sectors, threat actors
utilize the T1212—Exploitation for Credential Access more than in other
sectors. Finally, 50% of media and entertainment organizations don’t use
information security tools.
4 The Cato CTRL SASE Threat Report Q1 2024

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
complexities might result in misconfigurations, potentially disrupting their
applications and services.
5 The Cato CTRL SASE Threat Report Q1 2024

Introduction
Threat actors are always evolving. Whether it is nation-state actors,
cybercrime groups, ransomware gangs, or niche teams targeting specific
systems – new tools, techniques, and procedures are constantly introduced
by attackers. Cyber Threat Intelligence (CTI) remains fragmented and
isolated to point solutions rather than being collected and analyzed with a
holistic view that includes external data, inbound (and outbound) threats,
and network activity (WANbound). Without such a holistic view it’s difficult
to accurately evaluate the true state of cybersecurity within enterprises.
To address that need, Cato CTRL, the CTI group of Cato Networks, tapped
the data lake underlying Cato SASE Cloud to develop a holistic view of
enterprise threats. As the global network, Cato has granular data on every
traffic flow from every endpoint communicating across the Cato SASE
Cloud platform. This massive data lake is further enriched with hundreds of
security feeds and analyzed by proprietary ML/AI algorithms and human
intelligence. The result is a unique data repository providing Cato CTRL
insights into the security threats and their identifying network
characteristics for all traffic, regardless of whether they emanate from or
are destined for the Internet or the WAN for all endpoints – sites, remote
6 The Cato CTRL SASE Threat Report Q1 2024

Introduction
users, and cloud resources. Even where Cato’s multitiered defense strategy
has blocked the attack, the threats are logged and identified, enabling this
kind of analysis.
This report summarizes findings Cato CTRL gathered from Cato traffic flows
across more than 2,200 customers during the first quarter of 2024. During
the quarter, we analyzed 1.26 trillion network flows and blocked 21.45 billion
attacks. (To put that in context, that’s nearly four times more flows than the
350 billion flows we analyzed for Q1 2022.)
This report offers insights into the threats and suspicious activity across
those flows. It also provides strategic, tactical, and operational information
on all traffic in all directions utilizing the MITRE ATT&CK framework. In
addition, the report highlights the applications, protocols, and tools running
on these networks.
7 The Cato CTRL SASE Threat Report Q1 2024

About
Cato CTRL
Cato CTRL is the only CTI group to fuse threat
intelligence with granular network insight made
possible by the first and only global SASE platform,
the Cato SASE Cloud.
With dozens of former military intelligence analysts, researchers, and data
scientists, as well as industry-recognized security professionals, Cato CTRL
utilizes network data, security stack data, hundreds of security feeds, human
intelligence operations, AI and ML (Machine Learning) models, and more,
shedding light on the latest threats and threat actors.
Using industry-standard frameworks such as MITRE ATT&CK, multiple
intelligence disciplines, and years of field experience with red and blue team
techniques, Cato CTRL conducts the full intelligence lifecycle of collecting,
processing, analyzing, and producing cutting-edge CTI. Whether it is
tactical data for the SOC, operational threat landscape for managers, or
strategic intel for management and board, Cato CTRL has you covered.
8 The Cato CTRL SASE Threat Report Q1 2024

Report
Structure
This report is divided into six sections
General Statistics
This section provides an overview of the general statistics and metrics collected
from the private global networks relying on the Cato SASE Cloud Platform.
Mitigated Common Vulnerabilities
and Exposures (CVEs)
This section discusses the CVEs identified and mitigated within Cato’s
systems. Highlighted are the proactive measures to address known
vulnerabilities and prevent potential exploits.
9 The Cato CTRL SASE Threat Report Q1 2024

Report Structure
Suspicious Activity Monitoring (SAM)
Security Events
This section explores the security events that might otherwise be
considered benign but are identified as being associated with attacks on
Cato’s SAM system. By analyzing these events, Cato CTRL identifies
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
techniques, and in particular, the growing use of artificial intelligence (AI) tools.
Recommended Actions for Security Improvement
In the final section, Cato CTRL provides actionable recommendations based on
the findings from the previous sections.
10 The Cato CTRL SASE Threat Report Q1 2024

Section 1
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
4%
2%
2%
Top Inbound Threats
1%
Reputation
Network Scan
Web Application
Attack
Vulnerability Scan
Brute Force
91%
12 The Cato CTRL SASE Threat Report Q1 2024

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
Web Application Attack
50%
Vulnerability Scan
40%
Remote Code Execution
30%
20% Network Scan
10%
Lateral Movement
0%
Outbound Threats
Network scans (87% of flows associated with outbound threats) were the most
common outbound threat, a basic tool for attackers to use in reconnaissance for
targets outside the organization. Most attacks are mitigated during the network
scan, blocking attempts to scan public services. Most blocked traffic from outbound
threats, though, stems from attempts to scan SMB ports.
13 The Cato CTRL SASE Threat Report Q1 2024

General Statistics
0%
4% 1%
8%
Top Outbound Threats
Network Scan
Command and Control
Reputation
Malware
Exfiltration
87%
When analyzing outbound threats across industry verticals, we find that the
consulting and media sectors are more vulnerable to exfiltration threats than other
sectors. Within the consulting sector, data is more commonly being sent by FTP to
low-reputation domains. Regardless of the sector, the most common approach to
preventing attacks is being done by Cato’s reputation-based mitigation engine.
14 The Cato CTRL SASE Threat Report Q1 2024

General Statistics
Outbound Threats by Industry Verticals
100%
90%
80%
70%
Reputation
60%
Network Scan
50%
40% Malware
30% Exfiltration
20%
Command and Control
10%
0%
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
15 The Cato CTRL SASE Threat Report Q1 2024

General Statistics
2% 2%
3%
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
Web Application Attack
70%
60% Vulnerability Scan
50%
Remote Code Execution
40%
Network Scan
30%
20% Lateral Movement
10%
0%
16 The Cato CTRL SASE Threat Report Q1 2024

General Statistics
Top Spoofed Brands
Cybercriminals often exploit strong brands in their attacks, using tactics
such as phishing and spoofing. Cybersquatting, also known as domain
squatting, involves using a domain name to profit from the reputation and
recognition of a trademark that belongs to someone else. To combat this
issue, Cato Networks has developed a machine-learning algorithm that
can successfully detect instances of cybersquatting.
Top Spoofed Brands
250
11
35 homographsquatting
200
levelsquatting
150 5 typosquatting
1
4
62 combosquatting
100 201 3 1
8
28
132
79
50 89 85 1 2 1 0 1
60 34 16 31 24
0 20 14 26 10 14
Booking Amazon Ebay Pinterest Google Apple Netflix Microsoft Instagram Youtube
Booking, Amazon and Ebay were the top three spoofed brands using at
least one of four techniques:
• Typosquatting creates domain names that incorporate typical typos
users input when attempting to access a legitimate site, such as
“catonetwrks.com”, which leaves out the “o” in networks.
• Combosquatting creates a domain that combines the legitimate
domain with additional words or letters, such as “cato-networks.com”,
which adds a hyphen to Cato’s URL catonetworks.com.
17 The Cato CTRL SASE Threat Report Q1 2024

General Statistics
• Levelsquatting inserts the target domain into the subdomain of the
cybersquatting URL, such as login.catonetworks.com.fake.com.
• Homographsquatting uses various character combinations that
resemble the target domain visually, such as “catonet0rks.com”, which
uses a zero digit that looks like the letter “o.”
Learn more about Cybersquatting and the different types in our blog.
18 The Cato CTRL SASE Threat Report Q1 2024

Section 2
Mitigated
Vulnerabilities
(CVEs)

Mitigated Vulnerabilities (CVEs)
As we examine mitigated vulnerabilities (CVEs) we found that while some are
shared among industries, there are also industry-specific threats. Regardless,
threat actors are trying to exploit unpatched systems and are not always using
the latest vulnerabilities. (Disclaimer: The data may contain scanner activity.)
Three years after its discovery, Apache Log4J RCE (CVE-2021-44228) remains
one of the most used exploits. Other vulnerabilities being exploited across
industries include Microsoft Exchange server-side request forgery (SSRF,
CVE-2021-26855), PHP arbitrary code execution (CVE-2017-9841), and
Microsoft Exchange server-side request forgery (CVE-2022-41040).
Within the technology sector, we saw Amazon Redshift JDBC42 Remote Code
Execution (CVE-2022-41828). The manufacturing sector showed significant
usage of Adobe ColdFusion Insecure Deserialization (CVE-2023-26360). Within
the construction sector, we saw the use of SolarView Remote Code Execution
(CVE-2023-23333).
Inbound Traffic
As seen in the data, newer vulnerabilities do not necessarily mean that they
are the most common. The pie chart shows threat actors targeting unpatched
vulnerabilities, some of which are quite old. For example, one well-known
attack found across 33% of customer flows targets the PHPUnit testing
framework (CVE-2017-9841), which allows for arbitrary code execution in
PHP, has been around for more than seven years.
20 The Cato CTRL SASE Threat Report Q1 2024

Mitigated Vulnerabilities (CVEs)
3%
3% Top 10 Inbound CVE by
3%
4% Traffic Volume
5%
CVE-2017-9841 PHP arbitrary code execution vulnerability
33%
CVE-2021-44228 - Apache-Log4j Remote Code Execution
CVE-2022-41040 - Microsoft Exchange server-side request forgery (SSRF)
8%
CVE-2022-21371 - Oracle WebLogic Server Local File Inclusion
CVE-2021-43798 - Grafana Directory Traversal
CVE-2021-41773 - Apache HTTP Server Path Traversal
CVE-2018-19629 - Denial of Service vulnerability in the ImageNow Server
11%
CVE-2021-26855 - Microsoft Exchange server-side request forgery (SSRF)
Dasan GPON home routers bypass authentication. This vulnerability is broadly used
by Mirai and may indicate an infected device.
CVE-2021-34523 - ProxyShell - Microsoft Exchange Server Elevation of Privilege
12% 18%
We have classified each CVE according to its corresponding tactic in MITRE ATT@CK
Technique (see this blog for a detailed explanation of ATT@CK). Our analysis reveals
that threat actors are targeting Entertainment, Telecommunication, and Mining &
Metals with T1499 – Endpoint Denial of Service techniques more than other sectors.
Inbound Traffic - MITRE ATT&CK Techniques by Industry for
Common Vulnerabilities and Exposures (CVEs)
Not mapped
T1598 - Phishing for Information
100% T1592 - Gather Victim Host Information
T1589 - Gather Victim Identity Information
T1583 - Acquire Infrastructure
90% T1566 - Phishing
T1559 - Inter-Process Communication
T1556 - Modify Authentication Process
80% T1552 - Unsecured Credentials
T1539 - Steal Web Session Cookie
T1528 - Steal Application Access Token
70% T1505 - Server Software Component
T1499 - Endpoint Denial of Service
60% T T 1 1 4 4 9 9 8 6 - - R N e e s tw ou o r r c k e D H e i n ja ia c l k o in f g Service
T1485 - Data Destruction
50% T1221 - Template Injection
T1212 - Exploitation for Credential Access
T1211 - Exploitation for Defense Evasion
40% T1210 - Exploitation of Remote Services
T1204 - User Execution
T1190 - Exploit Public-Facing Application
30% T1136 - Create Account
T1133 - External Remote Services
T1098 - Account Manipulation
20% T1087 - Account Discovery
T1083 - File and Directory Discovery
T1082 - System Information Discovery
10% T1078 - Valid Accounts
T1072 - Software Deployment Tools
0% T T 1 1 0 0 6 59 8 - - C Ex o p m lo m it a a n ti d o n a n fo d r S P c r r iv ip il t e in g g e I E n s te c r a p la re ti t o e n r
T1055 - Process Injection
T1049 - System Network Connections Discovery
T1041 - Exfiltration Over C2 Channel
T1006 - Direct Volume Access
T1005 - Data from Local System
T1003 - OS Credential Dumping
21 The Cato CTRL SASE Threat Report Q1 2024

Mitigated Vulnerabilities (CVEs)
Outbound Traffic
Outbound threats refer to traffic originating within the organization and going out
to the public internet. The presence of an outbound threat may indicate that the
attacker is already present within the organization and could be using the network
to launch an attack on another enterprise. The most exploited vulnerabilities by
outbound threats in our research were Windows MSHTML elevation of privileges
(CVE-2023-29324), Apache Log4j RCE (CVE-2021-44228), and Windows DNS
Remote Code Execution (CVE-2021-26897).
2% 1% 1% Top 10 Outbound CVE
2%
by Traffic Volume
4%
CVE-2023-29324 - Windows MSHTML Platform
7%
Elevation of Privilege
CVE-2021-44228 - Apache-Log4j Remote
33%
Code Execution
CVE-2021-26897 - Windows DNS Remote
Code Execution
10%
CVE-2018-19629 - Denial of Service vulnerability
in the ImageNow Server
CVE-2021-41773 - Apache HTTP Server
Path Traversal
CVE-2021-26857 - Unsafe deserialization issue has
been identified in Exchange
CVE-2021-21872 - Lantronix PremierWave 2050
10% Remote Code Execution
CVE-2022-21907 - IIS Unauthenticated Remote
Code Execution
CVE-2023-22527 - Atlassian Confluence
Data Center and Confluence Server
Remote Code Execution
30%
In the Services and Hospitality sectors, more so than others, threat actors
utilize the Exploitation for Credential Access. They’re trying to exploit
CVE-2023-29324 for Windows MSHTML Platform Elevation of Privileges,
a component in Internet Explorer used to render web pages.
22 The Cato CTRL SASE Threat Report Q1 2024

Mitigated Vulnerabilities (CVEs)
Outbound Traffic - MITRE ATT&CK Techniques by Industry
for Common Vulnerabilities and Exposures (CVEs)
Not mapped
T1589 - Gather Victim Identity Information
100%
T1566 - Phishing
90% T1559 - Inter-Process Communication
T1556 - Modify Authentication Process
80%
T1552 - Unsecured Credentials
70% T1539 - Steal Web Session Cookie
T1528 - Steal Application Access Token
60% T1499 - Endpoint Denial of Service
T1212 - Exploitation for Credential Access
50%
T1211 - Exploitation for Defense Evasion
40% T1190 - Exploit Public-Facing Application
T1136 - Create Account
30%
T1133 - External Remote Services
20% T1083 - File and Directory Discovery
T1082 - System Information Discovery
10%
T1078 - Valid Accounts
0% T1072 - Software Deployment Tools
T1059 - Command and Scripting Interpreter
T1055 - Process Injection
T1049 - System Network Connections Discovery
T1005 - Data from Local System
WANbound Traffic
The most common vulnerability in WANbound traffic is web application-related
CVEs. As you can see in the graphic, all the CVEs are related to web applications.
Additionally, the percentage of WANbound traffic associated with CVE may be
influenced by how many organizations are using vulnerability scanners to identify
vulnerable systems within their network to prevent potential exploitation because
of its severe consequences.
23 The Cato CTRL SASE Threat Report Q1 2024

Mitigated Vulnerabilities (CVEs)
5%
5%
19%
Top 10 WANbound CVE by
6%
Traffic Volume
CVE-2021-44228 - Apache-Log4j Remote Code Execution
7%
CVE-2022-21371 - Oracle WebLogic Server Local File Inclusion
CVE-2021-26085 - Atlassian Confluence Server Arbitrary
File Read
7%
CVE-2022-22963 - Spring Cloud Remote Code Execution
17%
CVE-2021-41773 - Apache HTTP Server Path Traversal
CVE-2009-2445 - Oracle iPlanet Web Server Sensitive
Data Exposure
8%
CVE-2020-14750 - Oracle WebLogic Server RCE
CVE-2013-0625 - Adobe ColdFusion Remote Code Execution
10%
16%
Our analysis indicates that the most commonly used CVE in the Entertainment
sector is Text4Shell Apache Commons Text RCE (CVE-2022-42889). Meanwhile,
in the Telecommunications sector, the most frequently used technique is Endpoint
Denial of Service (T1499).
WANbound traffic - MITRE ATT&CK Techniques by Industry
for Common Vulnerabilities and Exposures (CVEs)
Not mapped
T1598 - Phishing for Information
T1592 - Gather Victim Host Information
100% T1589 - Gather Victim Identity Information
T1583 - Acquire Infrastructure
T1566 - Phishing
90% T1559 - Inter-Process Communication
T1556 - Modify Authentication Process
T1552 - Unsecured Credentials
80% T1539 - Steal Web Session Cookie
T1528 - Steal Application Access Token
T1505 - Server Software Component
70% T1499 - Endpoint Denial of Service
T1498 - Network Denial of Service
T1496 - Resource Hijacking
60% T1485 - Data Destruction
T1221 - Template Injection
T1212 - Exploitation for Credential Access
50% T1211 - Exploitation for Defense Evasion
T1210 - Exploitation of Remote Services
40% T1204 - User Execution
T1190 - Exploit Public-Facing Application
T1136 - Create Account
30% T1133 - External Remote Services
T1098 - Account Manipulation
T1087 - Account Discovery
20% T1083 - File and Directory Discovery
T1082 - System Information Discovery
T1078 - Valid Accounts
10% T1072 - Software Deployment Tools
T1068 - Exploitation for Privilege Escalation
T1059 - Command and Scripting Interpreter
0% T1055 - Process Injection
T1049 - System Network Connections Discovery
T1041 - Exfiltration Over C2 Channel
T1006 - Direct Volume Access
T1005 - Data from Local System
T1003 - OS Credential Dumping
24 The Cato CTRL SASE Threat Report Q1 2024

Section 3
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
attribute them to specific threat actors. Based on the activity identified by
monitoring these events, honeypots and deception techniques can be deployed.
0%
46% SAM by Traffic
Direction
Wanbound
Outbound
Inbound
54%
26 The Cato CTRL SASE Threat Report Q1 2024

Suspicious Activity Monitoring (SAM)
Outbound SAM
We can see that the highest-risk SAMs for outbound traffic are traffic to dynamic
DNS services in HTTP (44%), EXE download over non-browser HTTP traffic
(28%), and a possible malicious EXE file downloaded from a WordPress site
(12%). Alone, these actions would not be categorized as malicious as they do not
constitute an attack. But by understanding the underlying network traffic patterns
of attacks, Cato recognizes that these actions are often part of larger threat
patterns -- hence the term “suspicious.”
Top 10 HIGH Risk
2% 1% 1%
2% 0% Suspicious Activities
4%
in Outbound Traffic
6%
Traffic towards dynamicDNS services in HTTP
EXE download over HTTP non-browser traffic
Possible malicious exe file downloaded from
12% wordpress site.
Ngrok agent attempted to establish a tunnel
with Ngrok cloud
Downloaded Netcat
44% Download of a Binary File by Autoit
Downloading Splashtop
System Information Exfiltration
Curl client downloads a portable
executable file
28%
Rclone Exfiltration Client
If we examine the SAMs of medium-risk activities, we observe that HTTP
requests over non-standard ports to less popular destinations (21%),
WinINet/Winsock (Native Windows Client) to low-popularity domains (19%), and
IP checking services (11%) are ranked highest on the list.
27 The Cato CTRL SASE Threat Report Q1 2024

Suspicious Activity Monitoring (SAM)
Cato’s popularity score involves multiple data points, including real-time traffic
data from our network, which measures the application’s occurrences across
our network and is correlated with additional online sources. Typically, an
application that is less popular and less known poses a greater risk than a
well-established domain.
Top 10 MEDIUM Risk
6%
Suspicious Activities
7%
21%
in Outbound Traffic
HTTP Requests Over Non Standard Ports To
7%
Low Popularity Destinations
Wininet/Winsock (Native Windows Client) to
low Popularity Domain
IP checking services
8%
FTP Client (WinSCP) over SSH
Suspicious Chrome Extensions originated
not from webstore
15%
SAM - Outbound FileZilla traffic
8%
Wininet/Winsock (Native Windows Client) to
low Popularity IP
AnyDesk Remote Desktop Connection
Initiation
8%
11% PuTTY SSH Connection To Low Reputation IP
Bot downloading EXE file
9%
In the low-risk SAMs, the top indicators are domain reputation-based signature
(newly registered domain), TLS with low reputation and non-standard ports, and
SSH to high ports.
28 The Cato CTRL SASE Threat Report Q1 2024

Suspicious Activity Monitoring (SAM)
Top 10 LOW Risk
4%
5%
Suspicious Activities
5%
24% in Outbound Traffic
5%
Domain reputation based signature - Newly
Registered Domain
TLS With Low Reputation and Non-standard Ports
5%
SSH to High Ports
Ms-office 2016 document autoupdate attempt.
cURL over HTTP to low popularity domains
7%
Java over HTTP to low popularity domains
Bitsadmin administration tool - using suspicious
user agent & domain
Postman over HTTP to low popularity domains
10% 22%
Python over HTTP to low popularity domains
Long DNS Query
13%
Manufacturing, technology, and consumer goods are the most common industries that
engage in suspicious activities. The most prevalent threat techniques are Application
Layer Protocol (T1071), Non-Standard Port (T1571), and Ingress Tool Transfer (T1105).
Outbound Suspicious Activities by Industry Verticals
Not mapped
T1588 - Obtain Capabilities
100% T1583 - Acquire Infrastructure
T1573 - Encrypted Channel
90%
T1572 - Protocol Tunneling
T1571 - Non-Standard Port
80%
T1570 - Lateral Tool Transfer
70% T1569 - System Services
T1568 - Dynamic Resolution
60% T1567 - Exfiltration Over Web Service
T1566 - Phishing
50% T1531 - Account Access Removal
T1505 - Server Software Component
40% T1219 - Remote Access Software
T1204 - User Execution
30% T1197 - BITS Jobs
T1176 - Browser Extensions
20% T1105 - Ingress Tool Transfer
T1102 - Web Service
10% T1090 - Proxy
T1087 - Account Discovery
0%
T1071 - Application Layer Protocol
T1059 - Command and Scripting Interpreter
T1057 - Process Discovery
T1048 - Exfiltration Over Alternative Protocol
T1041 - Exfiltration Over C2 Channel
T1021 - Remote Services
T1020 - Automated Exfiltration
T1016 - System Network Configuration Discovery
29 The Cato CTRL SASE Threat Report Q1 2024

Suspicious Activity Monitoring (SAM)
WANbound SAM
We can see that the median-risk SAMs for WAN-bound traffic are LDAP Search
Query – Groups (53%), Querying Groups in the Domain (28%), and Moving
Executable Laterally to a Temp directory (8%).
2%
1%0% Top 10 HIGH Risk
2% 0%
6% Suspicious Activities
in WANbound Traffic
8%
LDAP Search Query - Groups
Querying Groups in the Domain
Moving Executable Laterally To a Temp directory
Execution of Remote RemCom Service
Using PsExec to Transfer Executable in SMB
53%
Execution of Remote PAExec Service
WinRM Unecrypted Execution Powershell
28%
PSexec Impersonates as a Regular Executable
Transferring Mimikatz over SMB
30 The Cato CTRL SASE Threat Report Q1 2024

Suspicious Activity Monitoring (SAM)
After analyzing the SAMs of WANbound traffic that pose a medium risk, we have
observed that three actions are the most common. These actions include
Enumerating All Users on the Domain Controller by using SAMR RPC (14%),
Querying Admin Groups in the Domain (14%), and Querying a Built-in
Administrator Account (12%).
Top 10 MEDIUM Risk
7%
14%
Suspicious Activities
7%
in WANbound Traffic
Enumerating All Users on the Domain Controler -
8%
Using SAMR RPC
Querying Admin Groups in the Domain
14%
Querying A Built-in Administrator Account
LDAP Search Query - Domain Computers
8%
Executable File Transfer Over SMB With
Impersonated Extension
Create new service on remote host via windows
service manager
Execute service on remote host via windows service
8% 12% manager
Executing Commands on a Remote Computer
Using WMI
Delete service on remote host via windows
service manager
11%
11%
FTP Client (WinSCP) over SSH
In WANbound traffic, the top indicators for low-risk SAMs are remotely querying a
computer using WMI, long DNS queries, and registering a new scheduled task on
the remote host.
31 The Cato CTRL SASE Threat Report Q1 2024

Suspicious Activity Monitoring (SAM)
9%
Top 10 LOW Risk
Suspicious Activities
14%
in WANbound Traffic
Remotely Querying a Computer
Using WMI
Remotely Querying a Computer
Using WMI
14% Registering a new scheduled task
on the remote host
Transferring a Powershell Script
63%
Over SMB
Our analysis indicates that the most commonly used CVE in the Entertainment
sector is Text4Shell Apache Commons Text RCE (CVE-2022-42889). Meanwhile,
in the Telecommunications sector, the most frequently used technique is Endpoint
Denial of Service (T1499).
WANbound Suspicious Activities by Industry Verticals
Not mapped
T1570 - Lateral Tool Transfer
100%
T1569 - System Services
90% T1558 - Steal or Forge Kerberos Tickets
80% T1505 - Server Software Component
T1486 - Data Encrypted for Impact
70%
T1482 - Domain Trust Discovery
60% T1210 - Exploitation of Remote Services
50% T1190 - Exploit Public-Facing Application
T1105 - Ingress Tool Transfer
40%
T1087 - Account Discovery
30% T1071 - Application Layer Protocol
T1069 - Permission Groups Discovery
20%
T1059 - Command and Scripting Interpreter
10%
T1053 - Scheduled Task/Job
0% T1048 - Exfiltration Over Alternative Protocol
T1047 - Windows Management Instrumentation
T1041 - Exfiltration Over C2 Channel
T1021 - Remote Services
T1020 - Automated Exfiltration
T1018 - Remote System Discovery
T1016 - System Network Configuration Discovery
32 The Cato CTRL SASE Threat Report Q1 2024

Section 4
Enterprise
Security
Behavior

Enterprise Security Behavior
Enterprises have long trusted their legacy MPLS networks, sending data
unencrypted and relying on edge firewalls for protection. Unfortunately, that
belief continues for many today, as they use insecure protocols for their
WANbound communications. This is a mistake, but it’s not the only one common
to enterprises. DNSSEC, which could be valuable in protecting against many
attacks, has not gained momentum.
Application use of AI tools is evident across all sectors. The technology and
manufacturing sectors have increased their use of AI tools monthly. We have also
observed that many of the surveyed entertainment organizations lack adequate
information security tools. In addition, each industry vertical uses a unique set
of applications and protocols, which may expose them to different threats.
Secure vs. Insecure Protocols
One of the best ways to reduce an organization’s attack surface is to use secure
protocols. In this section, Cato CTRL examines the use of such protocols within
the enterprise.
HTTP vs. HTTPS
The HTTP traffic analysis clearly shows that many organizations do not encrypt
their WAN traffic. This means that if an adversary is already inside the
organization’s network, they can eavesdrop on unencrypted communications
that may include personal identifiable information (PII) or sensitive information
such as credentials, further helping them in their lateral movement.
WANBOUND INBOUND OUTBOUND
HTTP vs HTTPS
HTTP vs HTTPS HTTP vs HTTPS HTTP vs HTTPS
11%
19%
38% 27%
62% 73%
81% 89%
HTTP HTTPS
34 The Cato CTRL SASE Threat Report Q1 2024

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
HTTP HTTPS
SMB v1 and v2 vs. SMB v3
The Microsoft environment has long relied on the Server Message Block (SMB)
protocol for file sharing and other purposes. Our data shows that most
enterprises continue to rely on SMB v1 and v2 (66%) despite their well-known
vulnerabilities, such as EternalBlue and denial of service (DoS) attacks.
Microsoft’s latest version of the protocol, SMB v3, has fixed many of these
vulnerabilities and enforces AES-128-GCM encryption, a robust encryption
standard.
35 The Cato CTRL SASE Threat Report Q1 2024

Enterprise Security Behavior
As we look at SMB adoption by industry, the top industries that still use SMB v1
and v2 are manufacturing, consumer goods, automotive, medical/healthcare,
and finance.
WANBOUND INBOUND OUTBOUND
SMB V1 AND V2 VS SMB V3
SMB V1 AND V2 VS SMB V3 SMB V1 AND V2 VS SMB V3 SMB V1 AND V2 VS SMB V3
34% 46% 100%
31%
66% 54% 69%
SMB_v1_v2 SMB_v3
SSH vs. TELNET
SSH is the most secure method for accessing remote servers. While
organizations increasingly use secure connections for inbound and outbound
traffic, Telnet is still being utilized inside the organizations.
WANBOUND INBOUND OUTBOUND
SSH vs TELNET
SSH vs TELNET SSH vs TELNET SSH vs TELNET
1%
6%
54%
39%
61% 46%
94% 99%
SSH TELNET
36 The Cato CTRL SASE Threat Report Q1 2024

Enterprise Security Behavior
In terms of industries, our analysis shows that Telnet is more prominent than SSH
in WANbound traffic for law practices, finance, automotive, mining & metals, and
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
SSH TELNET
DNS vs. DNSSEC
DNS plays a crucial role on the internet. Since DNS’s invention in 1983 multiple
vulnerabilities have been found, such as DNS cache poisoning and
man-in-the-middle attacks. Consequently, there was a need for a more secure
DNS. In 1997, the first specification of DNSSEC was published. A significant
milestone in 2010 was the signing of the root zone. Cato’s analysis of network
traffic revealed that there has been limited adoption of DNSSEC.
37 The Cato CTRL SASE Threat Report Q1 2024

Enterprise Security Behavior
WANBOUND INBOUND OUTBOUND
DNS vs DNSSEC
DNS vs DNSSEC DNS vs DNSSEC DNS vs DNSSEC
0% 3%
3% 2% 2%
97% 97% 100% 96%
DNS_OVER_U DNSSEC DNS_OVER_TCP
LLMNR vs. NetBIOS
LLMNR and NetBIOS are both used to resolve names on local networks. LLMNR
is designed as the successor of NetBIOS, aiming to provide a more secure
fallback option when DNS fails. However, using LLMNR and NetBIOS can pose
significant security risks, such as LLMNR poisoning, SMB Relay Attacks,
Pass-the-Hash Attacks, and more. The alternative is to utilize a local DNS server.
Our analysis indicates that all industry verticals still rely on LLMNR and NetBIOS,
with NetBIOS being the most commonly used.
Application Usage
In addition to investigating protocol usage across enterprises, Cato CTRL
investigated application usage. The Cato SASE Cloud identifies and classifies
thousands of applications within the enterprise. We examined the three types of
applications – AI tools, information security, and anonymizers.
AI Tools
The most common AI tools used among enterprises were Microsoft Copilot,
ChatGPT, and Emol, an application that records emotions and talks with AI
robots. Copilot’s strong adoption is likely due to its integration across Microsoft
products. The strongest adoption of these tools was seen in the travel and
tourism industry (79%), and the lowest adoption was among entertainment
organizations (44%).
38 The Cato CTRL SASE Threat Report Q1 2024

Enterprise Security Behavior
AI Tools Apps Usage by Industry Vertical
Information Security
How are companies protecting their information assets? It depends on who you ask.
The vast majority of educational organizations (82%) use information security tools,
versus less than half (48%) of entertainment organizations. The most used
information security tools are: TrendMicro, Umbrella, Bitdefender, Quad9, and ESET.
39
486374987.0
845391477.0 288507467.0
501248637.0 355240437.0 727272727.0 796969696.0 34737296.0 625012486.0 907223966.0 853773066.0 585635856.0 856911856.0 451648356.0 423788746.0 146520146.0 663366336.0 749875136.0 779609726.0
352313875.0 16579065.0 975888955.0 545454545.0
268572844.0 444444444.0
0.9
0.8
0.7 0.6
0.5
0.4
0.3
0.2
0.1
0
Information Security Apps Usage by Industry Vertical
474987518.0 486374987.0
845391477.0 288507467.0
158086447.0 727272727.0 613625017.0 702794907.0 71745707.0 796969696.0 290722396.0 296703296.0 928629286.0 833650676.0 506814476.0 329670376.0 111063076.0 766666666.0 158415846.0
73318216.0 190909095.0 644163095.0 458563585.0
973142715.0
184184184.0
0.9
0.8
0.7 0.6
0.5
0.4
0.3
0.2
0.1
0
The Cato CTRL SASE Threat Report Q1 2024

Enterprise Security Behavior
Anonymizers
When enterprises are looking to mask their browsing habits, Internet addresses, and
otherwise hide personal identifiable information, they turn to Anonymizers. The most
commonly used anonymizes include NordVPN, Surfshark VPN, Mullvad VPN, Hola
VPN, and AdGuard. Travel & tourism organizations are the biggest users of
Anonymizers (74%), perhaps reflecting the need to see local sites in planning trips
that would not be viewable from other regions, versus less than a third of
entertainment organizations.
Anonymizers Apps Usage by Industry Vertical
40
501248637.0
749875136.0
950746716.0 979283606.0 363567795.0 185691185.0 637730665.0
545454545.0 545454545.0 835164835.0 79207925.0
515151515.0 322449315.0 709726115.0 802529605.0 5.0 647759294.0 878408784.0 869078384.0 112486374.0 815978964.0
329670324.0 387140514.0
702685723.0
692692692.0
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0
The Cato CTRL SASE Threat Report Q1 2024

Section 5
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
imposed by LLMs on what they can have it perform. When the first chat based
LLMs came out, the guardrails were not high. As a result, prompts that could
potentially create malicious code and content. Today, most LLMs have rules
guarding against producing anything from potentially harmful content to
potentially copyrighted materials. Here is one example, out of many, of how
threat actors are looking for ways to jailbreak ChatGPT to create custom
SQLMap commands:
42 The Cato CTRL SASE Threat Report Q1 2024

Hacking Communities
We also observed another automated web scanner that uses AI to parse the
result and adjust the command. It uses the open-source LLAMA model by Meta:
Translation of the text -
"Advantages:
Automation of penetration testing processes.
Intelligent analysis of reports and recommendations for the elimination of vulnerabilities.
Flexible settings and the ability to adapt to specific needs.
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
43 The Cato CTRL SASE Threat Report Q1 2024

Hacking Communities
In the example below, threat actors test and share their opinions on new models
that are hosted on the Hugging Face platform (see the platform here)
Translation of the text -
"This neural network will copy any voice and use it to voice your text. They've just rolled out a
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
44 The Cato CTRL SASE Threat Report Q1 2024

Hacking Communities
Criminals are looking particularly to generate fake documents, so why not use
machine learning for such tasks? One attacker did just that:
45 The Cato CTRL SASE Threat Report Q1 2024

Hacking Communities
Careers and Development
Creating custom ML models like LLM, training models, and fine-tuning models
requires work and expertise. In recent months, we have seen people marketing
their ML expert services in underground forums and cybercrime groups looking
to hire such experts to help them design their own malicious GPT variant.
Translation of the text -
"Clustering, Gradient Boosting (xgboost, LightGBM, CatBoost), k-means... I possess skills in Feature
Engineering (construction of parameters from existing data). I am adept at fine-tuning settings and
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
46 The Cato CTRL SASE Threat Report Q1 2024

Section 6
Recommended
Actions

Recommended Actions
Based on the above findings, Cato CTRL
recommends enterprise IT and security
leaders take five actions:
Monitor your WAN traffic to check which insecure protocols you use and switch to
secure protocols. Continuing to run insecure protocols makes it easier for threat
actors to gather information, steal confidential information traversing the network,
and exploit vulnerabilities.
Implement Zero-Trust strategies in your organization. Zero-Truest restricts users'
access to only the necessary resources, minimizing the attack surface in the event
of stolen credentials or similar attacks.
Disable LLMNR and NetBIOS and use local DNS servers. As noted, both LLMNR
and NetBIOS pose significant security risks, which could be mitigated by relying on
local DNS servers.
Deploy vulnerability scanning in your network to find vulnerabilities and improve
your organization's security posture. Many attacks exploit vulnerabilities that are
quite old and simply haven’t been patched. Scanning for and identifying those
vulnerabilities will go a long way to improving the enterprise’s risk posture.
Asset management is critical to mapping services, applications, and third-party
packages to detect exploitable old services and applications. Only once mapped
and understood can security teams replace the insecure protocols and remediate
the unpatched services within the enterprise, reducing the attack surface.
48 The Cato CTRL SASE Threat Report Q1 2024

About Cato Networks
Cato provides a world-leading single-vendor SASE platform. Cato creates a seamless and
elegant customer experience that effortlessly enables threat prevention, data protection,

and timely incident detection and response. Using Cato, businesses easily replace costly and
rigid legacy infrastructure with an open and modular SASE architecture based on SD-WAN,

a purpose-built global cloud network, and an embedded cloud-native security stack.
Cato SASE Cloud Platform
XOps (XDR + AIOps)
AI/ML-driven Anomaly Detection • Analyst Workbench with Gen-AI Stories • Incident LifecycleManagement Single Management and API
•Granular RBAC
•Rich network and security analytics
High-throughput Traffic Processing Threat Prevention and Data Protection
•Autonomous Policies
Any Edge• Any Port/Protocol •DEM FWaaS• SWG• IPS• DNS• NGAM• Sandbox •Automated Posture Management
Acceleration and Optimization • Selective Decryption ZTNA• CASB• DLP• RBI• IoT/OT •Self-service and Co-managed
SaaS
SaaS Optimization Multi Cloud Integration
www Smart Egress•Dedicated IP Cato vSocket•Cloud interconnect•IPsec
SPACE
Clientless
via Web Portal
MPLS
Cato Client Browser Extension
Cato Socket Edge SD-WAN Universal ZTNA • EPP/EDR
A/A/A • Path Selection •App/Id Aware QoS • NGFW• Segmentation
or 3rd party IPsec
Cato Client
UniversalZTNA • EPP/EDR
IoT
Cato. WE ARE SASE.
Cato SASE Cloud Platform Use Cases
Connect Network Transformation Security Transformation
Cloud Network MPLS to SD-WAN Migration Secure Hybrid Work
Cloud On-Ramps Global Access Optimization Secure Direct Internet Access
Hybrid Cloud & Multi-Cloud Secure Application and Data Access
Incident Detection and Response
Protect
Network Security Business Transformation
Endpoint Security Vendor Consolidation
Spend Optimization
Detect M&A and Geo Expansion
Incident Life Cycle Management
Run Contact Us
Unified Management and API

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-08-15", "model": "legacy"} -->
