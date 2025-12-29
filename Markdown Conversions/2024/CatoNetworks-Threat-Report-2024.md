# The Cato CTRL SASE Threat Report Q1 2024

## Table of Contents
- [Executive Summary](#executive-summary)
- [Introduction](#introduction)
- [About Cato CTRL](#about-cato-ctrl)
- [Report Structure](#report-structure)
- [Section 1: General Statistics](#section-1-general-statistics)
  - [Inbound Threats](#inbound-threats)
  - [Outbound Threats](#outbound-threats)
  - [WANbound Threats](#wanbound-threats)
- [Section 2: Mitigated Vulnerabilities (CVEs)](#section-2-mitigated-vulnerabilities-cves)
  - [Inbound Traffic](#inbound-traffic-1)
  - [Outbound Traffic](#outbound-traffic-1)
  - [WANbound Traffic](#wanbound-traffic-1)
- [Section 3: Suspicious Activity Monitoring (SAM)](#section-3-suspicious-activity-monitoring-sam)
  - [Outbound SAM](#outbound-sam)
  - [WANbound SAM](#wanbound-sam)
- [Section 4: Enterprise Security Behavior](#section-4-enterprise-security-behavior)
  - [Secure vs. Insecure Protocols](#secure-vs-insecure-protocols)
  - [Application Usage](#application-usage)
- [Section 5: Hacking Communities](#section-5-hacking-communities)
  - [Tooling](#tooling)
  - [Deepfake](#deep-fake)
  - [Careers and Development](#careers-and-development)
- [Section 6: Recommended Actions](#section-6-recommended-actions)

---

Cato Networks:

The Cato
CTRL SASE
Threat Report

Q1 | 2024

---

## Executive Summary

Below are key takeaways
from this quarter’s analysis:

### AI takes the enterprise by storm
The most common AI tools used among enterprises were Microsoft Copilot,
OpenAI ChatGPT, and Emol, an application that records emotions and talks
with AI robots. The strongest adoption of these tools was seen in the travel
& tourism industry (79%), and the lowest adoption among entertainment
organizations (44%).

### Get a peek into the hacker underground
As part of its research, Cato CTRL monitors discussions from various
hacker forums. The report found attackers discussing how to jailbreak
ChatGPT to create custom SQLMap commands. We spotted
advertisements for services for generating fake credentials and creating
deep fakes. We also continued to monitor recruitment for creating a
malicious ChatGPT.

---
The Cato CTRL SASE Threat Report Q1 2024

## Executive Summary

### Beware of where you shop
Threat actors are setting up domains that mimic well-known brands.
Booking, Amazon, and eBay are the most spoofed brands.

### Enterprises are too trusting within their networks
Many enterprises continue to run unsecured protocols across their WAN,
with 62 % of all web application traffic being HTTP, 54% of all traffic being
telnet, and 46% of all traffic being SMB v1 or v2 instead of SMBv3. Lateral
movement—where attackers will move across networks—was identified
particularly in the agriculture, real estate, and travel and tourism industries.

### Zero-day is the least of your problems
While we in the industry pay a lot of attention to zero-day threats the reality is
that threat actors are often trying to exploit unpatched systems, eschewing
the use of the latest vulnerabilities and instead exploiting unpatched systems.
For example, three years after its discovery, Log4J (CVE-2021-44228)
remains one of the most used exploits.

### Security varies between industries
Vulnerabilities and techniques are common across industries, but there are
ones specific to industries. Entertainment, Telecommunication, and Mining &
Metals are being targeted with T1499 – Endpoint Denial of Service techniques
more than other sectors. In the Services and Hospitality sectors, threat actors
utilize the T1212—Exploitation for Credential Access more than in other
sectors. Finally, 50% of media and entertainment organizations don’t use
information security tools.

---
The Cato CTRL SASE Threat Report Q1 2024

## Executive Summary

### Even benign activity is becoming suspicious
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

### The “Un”adoption of DNSSEC
Our data indicates that only 1% of DNS traffic utilizes Secure DNS.
We believe this is primarily due to DNS being a critical component of both the
internet and organizational operations. Organizations fear that implementation
complexities might result in misconfigurations, potentially disrupting their
applications and services.

---
The Cato CTRL SASE Threat Report Q1 2024

## Introduction

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

---
The Cato CTRL SASE Threat Report Q1 2024

## Introduction

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

---
The Cato CTRL SASE Threat Report Q1 2024

## About Cato CTRL

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

---
The Cato CTRL SASE Threat Report Q1 2024

## Report Structure

This report is divided into six sections

### General Statistics
This section provides an overview of the general statistics and metrics collected
from the private global networks relying on the Cato SASE Cloud Platform.

### Mitigated Common Vulnerabilities
and Exposures (CVEs)

This section discusses the CVEs identified and mitigated within Cato’s
systems. Highlighted are the proactive measures to address known
vulnerabilities and prevent potential exploits.

---
The Cato CTRL SASE Threat Report Q1 2024

## Report Structure

### Suspicious Activity Monitoring (SAM)
Security Events
This section explores the security events that might otherwise be
considered benign but are identified as being associated with attacks on
Cato’s SAM system. By analyzing these events, Cato CTRL identifies
potential threats, anomalies, and patterns that require further
investigation or immediate action.

### Enterprise Security Behavior
In this section, Cato CTRL delves into organizations’ security behavior,
examining the usage of secure and insecure protocols, employee
applications, and other relevant data points.

### Hacking Communities and AI Tool
Usage by Threat Actors

Cato CTRL closely monitors threat actor activities in forums, the dark web, and
private chat channels to gain insights into threat actor’s latest trends and
techniques, and in particular, the growing use of artificial intelligence (AI) tools.

### Recommended Actions for Security Improvement
In the final section, Cato CTRL provides actionable recommendations based on
the findings from the previous sections.

---
The Cato CTRL SASE Threat Report Q1 2024

# Section 1

General
Statistics

---

## General Statistics

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

### Inbound Threats
The most common type of inbound threat was detected by our reputation engine.
Some examples of reputation-based threats found in our research include. IP feeds
for exploitation, spam, scanners and malicious domains.

![Top Inbound Threats Chart](https://i.imgur.com/example1.png)

*Top Inbound Threats*
- Reputation: 91%
- Network Scan: 4%
- Web Application
Attack: 2%
- Vulnerability Scan: 2%
- Brute Force: 1%

---
The Cato CTRL SASE Threat Report Q1 2024

## General Statistics

When we break down the inbound threats by industry verticals, we see that the
healthcare sector leads in web application attacks and scanning activities,
while education suffers from the most brute-force attacks of any industry. These
attacks are being launched against Remote Desktop Protocol (RDP) ports

![Inbound Threats by Industry Verticals Chart](https://i.imgur.com/example2.png)

*Inbound Threats by Industry Verticals*

### Outbound Threats
Network scans (87% of flows associated with outbound threats) were the most
common outbound threat, a basic tool for attackers to use in reconnaissance for
targets outside the organization. Most attacks are mitigated during the network
scan, blocking attempts to scan public services. Most blocked traffic from outbound
threats, though, stems from attempts to scan SMB ports.

---
The Cato CTRL SASE Threat Report Q1 2024

## General Statistics

![Top Outbound Threats Chart](https://i.imgur.com/example3.png)

*Top Outbound Threats*
- Network Scan: 87%
- Command and Control: 8%
- Reputation: 4%
- Malware: 1%
- Exfiltration: 0%

When analyzing outbound threats across industry verticals, we find that the
consulting and media sectors are more vulnerable to exfiltration threats than other
sectors. Within the consulting sector, data is more commonly being sent by FTP to
low-reputation domains. Regardless of the sector, the most common approach to
preventing attacks is being done by Cato’s reputation-based mitigation engine.

---
The Cato CTRL SASE Threat Report Q1 2024

## General Statistics

![Outbound Threats by Industry Verticals Chart](https://i.imgur.com/example4.png)

*Outbound Threats by Industry Verticals*

Upon examining outbound traffic, it is evident that most attacks are being mitigated
during the network scan, indicating that attempts to scan public services are being
blocked. Analysis of the data reveals that the majority of the blocked traffic consists
of attempts to scan SMB ports.

### WANbound Threats
In web application attacks, we witnessed multiple attempts to detect vulnerable web
applications by scanning known URLs. We also saw lateral movement in the
Windows environment, where attempts were made to use Windows Management
Instrumentation (WMI) to query system information and then execute commands
remotely. We also saw heavy use of WinRS Encrypted Execution to hide malicious
code in Windows Remote Shell (WinRS) by encrypting it.

---
The Cato CTRL SASE Threat Report Q1 2024

## General Statistics

![Top WANbound Threats Chart](https://i.imgur.com/example5.png)

*Top WANbound Threats*
- Network Scan: 84%
- Web Application Attack: 9%
- Lateral Movement: 3%
- Vulnerability Scan: 2%
- Remote Code Execution: 2%

Agriculture, real estate, and travel & tourism experienced the most
lateral-movement-related activities when compared to other industries

![WANbound Threats by Industry Verticals Chart](https://i.imgur.com/example6.png)

*WANbound Threats by Industry Verticals*

---
The Cato CTRL SASE Threat Report Q1 2024

## General Statistics

### Top Spoofed Brands
Cybercriminals often exploit strong brands in their attacks, using tactics
such as phishing and spoofing. Cybersquatting, also known as domain
squatting, involves using a domain name to profit from the reputation and
recognition of a trademark that belongs to someone else. To combat this
issue, Cato Networks has developed a machine-learning algorithm that
can successfully detect instances of cybersquatting.

![Top Spoofed Brands Chart](https://i.imgur.com/example7.png)

*Top Spoofed Brands*

Booking, Amazon and Ebay were the top three spoofed brands using at
least one of four techniques:
*   Typosquatting creates domain names that incorporate typical typos
    users input  when attempting to access a legitimate site, such as
    “catonetwrks.com”, which leaves out the “o” in networks.
*   Combosquatting creates a domain that combines the legitimate
    domain with additional words or letters, such as “cato-networks.com”,
    which adds a hyphen to Cato’s URL catonetworks.com.

---
The Cato CTRL SASE Threat Report Q1 2024

## General Statistics

*   Levelsquatting inserts the target domain into the subdomain of the
    cybersquatting URL, such as login.catonetworks.com.fake.com.
*   Homographsquatting uses various character combinations that
    resemble the target domain visually, such as “catonet0rks.com”, which
    uses a zero digit that looks like the letter “o.”

Learn more about Cybersquatting and the different types in our blog.

---
The Cato CTRL SASE Threat Report Q1 2024

# Section 2

Mitigated
Vulnerabilities
(CVEs)

---

## Mitigated Vulnerabilities (CVEs)

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

### Inbound Traffic
As seen in the data, newer vulnerabilities do not necessarily mean that they
are the most common. The pie chart shows threat actors targeting unpatched
vulnerabilities, some of which are quite old. For example, one well-known
attack found across 33% of customer flows targets the PHPUnit testing
framework (CVE-2017-9841), which allows for arbitrary code execution in
PHP, has been around for more than seven years.

---
The Cato CTRL SASE Threat Report Q1 2024

## Mitigated Vulnerabilities (CVEs)

![Top 10 Inbound CVE by Traffic Volume Chart](https://i.imgur.com/example8.png)

*Top 10 Inbound CVE by
Traffic Volume*
- CVE-2017-9841 PHP arbitrary code execution vulnerability: 33%
- CVE-2021-44228 - Apache-Log4j Remote Code Execution: 18%
- CVE-2022-41040 - Microsoft Exchange server-side request forgery (SSRF): 12%
- CVE-2022-21371 - Oracle WebLogic Server Local File Inclusion: 11%
- CVE-2021-43798 - Grafana Directory Traversal: 8%
- CVE-2021-41773 - Apache HTTP Server Path Traversal: 7%
- CVE-2018-19629 - Denial of Service vulnerability in the ImageNow Server: 5%
- CVE-2021-26855 - Microsoft Exchange server-side request forgery (SSRF): 4%
- Dasan GPON home routers bypass authentication. This vulnerability is broadly used
by Mirai and may indicate an infected device.: 3%
- CVE-2021-34523 - ProxyShell - Microsoft Exchange Server Elevation of Privilege: 3%

We have classified each CVE according to its corresponding tactic in MITRE ATT@CK
Technique (see this blog for a detailed explanation of ATT@CK). Our analysis reveals
that threat actors are targeting Entertainment, Telecommunication, and Mining &
Metals with T1499 – Endpoint Denial of Service techniques more than other sectors.

![Inbound Traffic - MITRE ATT&CK Techniques by Industry for
Common Vulnerabilities and Exposures (CVEs) Chart](https://i.imgur.com/example9.png)

*Inbound Traffic - MITRE ATT&CK Techniques by Industry for
Common Vulnerabilities and Exposures (CVEs)*

---
The Cato CTRL SASE Threat Report Q1 2024

## Mitigated Vulnerabilities (CVEs)

### Outbound Traffic
Outbound threats refer to traffic originating within the organization and going out
to the public internet. The presence of an outbound threat may indicate that the
attacker is already present within the organization and could be using the network
to launch an attack on another enterprise. The most exploited vulnerabilities by
outbound threats in our research were Windows MSHTML elevation of privileges
(CVE-2023-29324), Apache Log4j RCE (CVE-2021-44228), and Windows DNS
Remote Code Execution (CVE-2021-26897).

![Top 10 Outbound CVE
by Traffic Volume Chart](https://i.imgur.com/example10.png)

*Top 10 Outbound CVE
by Traffic Volume*
- CVE-2023-29324 -  Windows MSHTML Platform
Elevation of Privilege: 33%
- CVE-2021-44228 - Apache-Log4j Remote
Code Execution: 30%
- CVE-2021-26897 - Windows DNS Remote
Code Execution: 10%
- CVE-2018-19629 - Denial of Service vulnerability
in the ImageNow Server: 10%
- CVE-2021-41773 - Apache HTTP Server
Path Traversal: 7%
- CVE-2021-26857 - Unsafe deserialization issue has
been identified in Exchange: 4%
- CVE-2021-21872 - Lantronix PremierWave 2050
Remote Code Execution: 2%
- CVE-2022-21907 - IIS Unauthenticated Remote
Code Execution: 2%
- CVE-2023-22527 - Atlassian Confluence
Data Center and Confluence Server
Remote Code Execution: 1%
- CVE-2021-43798 - Grafana Directory Traversal: 1%

In the Services and Hospitality sectors, more so than others, threat actors
utilize the Exploitation for Credential Access. They’re trying to exploit
CVE-2023-29324 for Windows MSHTML Platform Elevation of Privileges,
a component in Internet Explorer used to render web pages.

---
The Cato CTRL SASE Threat Report Q1 2024

## Mitigated Vulnerabilities (CVEs)

![Outbound Traffic - MITRE ATT&CK Techniques by Industry
for Common Vulnerabilities and Exposures (CVEs) Chart](https://i.imgur.com/example11.png)

*Outbound Traffic - MITRE ATT&CK Techniques by Industry
for Common Vulnerabilities and Exposures (CVEs)*

### WANbound Traffic
The most common vulnerability in WANbound traffic is web application-related
CVEs. As you can see in the graphic, all the CVEs are related to web applications.
Additionally, the percentage of WANbound traffic associated with CVE may be
influenced by how many organizations are using vulnerability scanners to identify
vulnerable systems within their network to prevent potential exploitation because
of its severe consequences.

---
The Cato CTRL SASE Threat Report Q1 2024

## Mitigated Vulnerabilities (CVEs)

![Top 10 WANbound CVE by
Traffic Volume Chart](https://i.imgur.com/example12.png)

*Top 10 WANbound CVE by
Traffic Volume*
- CVE-2021-44228 - Apache-Log4j Remote Code Execution: 19%
- CVE-2022-21371 - Oracle WebLogic Server Local File Inclusion: 17%
- CVE-2021-26085 - Atlassian Confluence Server Arbitrary
File Read: 16%
- CVE-2022-22963 - Spring Cloud Remote Code Execution: 10%
- CVE-2021-41773 - Apache HTTP Server Path Traversal: 8%
- CVE-2009-2445 - Oracle iPlanet Web Server Sensitive
Data Exposure: 7%
- CVE-2020-14750 - Oracle WebLogic Server RCE: 7%
- CVE-2013-0625 - Adobe ColdFusion Remote Code Execution: 6%
- CVE-2021-43798 - Grafana Directory Traversal: 5%
- CVE-2021-44832 - Apache Log4j RCE: 5%

Our analysis indicates that the most commonly used CVE in the Entertainment
sector is Text4Shell Apache Commons Text RCE (CVE-2022-42889).  Meanwhile,
in the Telecommunications sector, the most frequently used technique is Endpoint
Denial of Service (T1499).

![WANbound traffic - MITRE ATT&CK Techniques by Industry
for Common Vulnerabilities and Exposures (CVEs) Chart](https://i.imgur.com/example13.png)

*WANbound traffic - MITRE ATT&CK Techniques by Industry
for Common Vulnerabilities and Exposures (CVEs)*

---
The Cato CTRL SASE Threat Report Q1 2024

# Section 3
Suspicious
Activity
Monitoring
(SAM)

---

## Suspicious Activity Monitoring (SAM)

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
can detect suspicious behavior and alert the organization using XDR. Each SAM
signature has an associated risk: Low, Medium, or High. We also mapped SAM
signatures to their corresponding MITRE ATT@CK tactics.

Understanding and analyzing suspicious events can help reduce an organization’s
attack surface. By monitoring suspicious activities, we can trace them back and
attribute them to specific threat actors. Based on the activity identified by
monitoring these events, honeypots and deception techniques can be deployed.

![SAM by Traffic
Direction Chart](https://i.imgur.com/example14.png)

*SAM by Traffic
Direction*
- Wanbound: 54%
- Outbound: 46%
- Inbound: 0%

---
The Cato CTRL SASE Threat Report Q1 2024

## Suspicious Activity Monitoring (SAM)

### Outbound SAM
We can see that the highest-risk SAMs for outbound traffic are traffic to dynamic
DNS services in HTTP (44%), EXE download over non-browser HTTP traffic
(28%), and a possible malicious EXE file downloaded from a WordPress site
(12 %). Alone, these actions would not be categorized as malicious as they do not
constitute an attack. But by understanding the underlying network traffic patterns
of attacks, Cato recognizes that these actions are often part of larger threat
patterns -- hence the term “suspicious.”

![Top 10 HIGH Risk
Suspicious Activities
in Outbound Traffic Chart](https://i.imgur.com/example15.png)

*Top 10 HIGH Risk
Suspicious Activities
in Outbound Traffic*
- Traffic towards dynamicDNS services in HTTP: 44%
- EXE download over HTTP non-browser traffic: 28%
- Possible malicious exe file downloaded from
wordpress site.: 12%
- Ngrok agent attempted to establish a tunnel
with Ngrok cloud: 6%
- Downloaded Netcat: 4%
- Download of a Binary File by Autoit: 2%
- Downloading Splashtop: 2%
- System Information Exfiltration: 1%
- Curl client downloads a portable
executable file: 1%
- Rclone Exfiltration Client: 0%

If we examine the SAMs of medium-risk activities, we observe that HTTP
requests over non-standard ports to less popular destinations (21%),
WinINet/Winsock (Native Windows Client) to low-popularity domains (19%), and
IP checking services (11%) are ranked highest on the list.

---
The Cato CTRL SASE Threat Report Q1 2024

## Suspicious Activity Monitoring (SAM)

![Top 10 MEDIUM Risk
Suspicious Activities
in Outbound Traffic Chart](https://i.imgur.com/example16.png)

*Top 10 MEDIUM Risk
Suspicious Activities
in Outbound Traffic*
- HTTP Requests Over Non Standard Ports To
Low Popularity Destinations: 21%
- Wininet/Winsock (Native Windows Client) to
low Popularity Domain: 19%
- IP checking services: 11%
- FTP Client (WinSCP) over SSH: 9%
- Suspicious Chrome Extensions originated
not from webstore: 8%
- SAM - Outbound FileZilla traffic: 8%
- Wininet/Winsock (Native Windows Client) to
low Popularity IP: 8%
- AnyDesk Remote Desktop Connection
Initiation: 7%
- PuTTY SSH Connection To Low Reputation IP: 7%
- Bot downloading EXE file: 6%

Cato’s popularity score involves multiple data points, including real-time traffic
data from our network, which measures the application’s occurrences across
our network and is correlated with additional online sources. Typically, an
application that is less popular and less known poses a greater risk than a
well-established domain.

In the low-risk SAMs, the top indicators are domain reputation-based signature
(newly registered domain), TLS with low reputation and non-standard ports, and
SSH to high ports.

---
The Cato CTRL SASE Threat Report Q1 2024

## Suspicious Activity Monitoring (SAM)

![Top 10 LOW Risk
Suspicious Activities
in Outbound Traffic Chart](https://i.imgur.com/example17.png)

*Top 10 LOW Risk
Suspicious Activities
in Outbound Traffic*
- Domain reputation based signature - Newly
Registered Domain: 24%
- TLS With Low Reputation and Non-standard Ports: 22%
- SSH to High Ports: 13%
- Ms-office 2016 document autoupdate attempt.: 10%
- cURL over HTTP to low popularity domains: 7%
- Java over HTTP to low popularity domains: 7%
- Bitsadmin administration tool - using suspicious
user agent & domain: 5%
- Postman over HTTP to low popularity domains: 5%
- Python over HTTP to low popularity domains: 5%
- Long DNS Query: 4%

Manufacturing, technology, and consumer goods are the most common industries that
engage in suspicious activities. The most prevalent threat techniques are Application
Layer Protocol (T1071), Non-Standard Port (T1571), and Ingress Tool Transfer (T1105).

![Outbound Suspicious Activities by Industry Verticals Chart](https://i.imgur.com/example18.png)

*Outbound Suspicious Activities by Industry Verticals*

---
The Cato CTRL SASE Threat Report Q1 2024

## Suspicious Activity Monitoring (SAM)

### WANbound SAM
We can see that the median-risk SAMs for WAN-bound traffic are LDAP Search
Query – Groups (53%), Querying Groups in the Domain (28%), and Moving
Executable Laterally to a Temp directory (8%).

![Top 10 HIGH Risk
Suspicious Activities
in WANbound Traffic Chart](https://i.imgur.com/example19.png)

*Top 10 HIGH Risk
Suspicious Activities
in WANbound Traffic*
- LDAP Search Query - Groups: 53%
- Querying Groups in the Domain: 28%
- Moving Executable Laterally To a Temp directory: 8%
- Execution of Remote RemCom Service: 6%
- Using PsExec to Transfer Executable in SMB: 2%
- Execution of Remote PAExec Service: 2%
- WinRM Unecrypted Execution Powershell: 1%
- PSexec Impersonates as a Regular Executable: 0%
- Transferring Mimikatz over SMB: 0%
- Remote Execution of PowerShell: 0%

---
The Cato CTRL SASE Threat Report Q1 2024

## Suspicious Activity Monitoring (SAM)

After analyzing the SAMs of WANbound traffic that pose a medium risk, we have
observed that three actions are the most common. These actions include
Enumerating All Users on the Domain Controller by using SAMR RPC (14%),
Querying Admin Groups in the Domain (14%), and Querying a Built-in
Administrator Account (12 %).

![Top 10 MEDIUM Risk
Suspicious Activities
in WANbound Traffic Chart](https://i.imgur.com/example20.png)

*Top 10 MEDIUM Risk
Suspicious Activities
in WANbound Traffic*
- Enumerating All Users on the Domain Controller -
Using SAMR RPC: 14%
- Querying Admin Groups in the Domain: 14%
- Querying A Built-in Administrator Account: 12%
- LDAP Search Query - Domain Computers: 11%
- Executable File Transfer Over SMB With
Impersonated Extension: 11%
- Create new service on remote host via windows
service manager: 8%
- Execute service on remote host via windows
service manager: 8%
- Executing Commands on a Remote Computer
Using WMI: 7%
- Delete service on remote host via windows
service manager: 7%
- FTP Client (WinSCP) over SSH: 6%

In WANbound traffic, the top indicators for low-risk SAMs are remotely querying a
computer using WMI, long DNS queries, and registering a new scheduled task on
the remote host.

---
The Cato CTRL SASE Threat Report Q1 2024

## Suspicious Activity Monitoring (SAM)

![Top 10 LOW Risk
Suspicious Activities
in WANbound Traffic Chart](https://i.imgur.com/example21.png)

*Top 10 LOW Risk
Suspicious Activities
in WANbound Traffic*
- Remotely Querying a Computer
Using WMI: 63%
- Remotely Querying a Computer
Using WMI: 14%
- Registering a new scheduled task
on the remote host: 14%
- Transferring a Powershell Script
Over SMB: 9%

Our analysis indicates that the most commonly used CVE in the Entertainment
sector is Text4Shell Apache Commons Text RCE (CVE-2022-42889).  Meanwhile,
in the Telecommunications sector, the most frequently used technique is Endpoint
Denial of Service (T1499).

![WANbound Suspicious Activities by Industry Verticals Chart](https://i.imgur.com/example22.png)

*WANbound Suspicious Activities by Industry Verticals*

---
The Cato CTRL SASE Threat Report Q1 2024

# Section 4
Enterprise
Security
Behavior

---

## Enterprise Security Behavior

Enterprises have long trusted their legacy MPLS networks, sending data
unencrypted and relying on edge firewalls for protection. Unfortunately, that
belief continues for many today, as they use insecure protocols for their
WANbound communications. This is a mistake, but it’s not the only one common
to enterprises. DNSSEC, which could be valuable in protecting against many
attacks, has not gained momentum.

Application use of AI tools is evident across all sectors. The technology and
manufacturing sectors have increased their use of AI tools monthly. We have also
observed that many of the surveyed entertainment organizations lack adequate
information security tools.     In addition, each industry vertical uses a unique set
of applications and protocols, which may expose them to different threats.

### Secure vs. Insecure Protocols
One of the best ways to reduce an organization’s attack surface is to use secure
protocols