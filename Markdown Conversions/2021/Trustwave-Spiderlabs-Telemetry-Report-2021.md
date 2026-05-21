# SpiderLabs Telemetry Report: The State of High-Profile Vulnerabilities (2021)

## Table of Contents
- [Introduction](#introduction)
- [Vulnerability Trends](#vulnerability-trends)
- [High-Profile Vulnerabilities of 2021](#high-profile-vulnerabilities-of-2021)
- [Microsoft Exchange Server: ProxyShell and ProxyToken](#microsoft-exchange-server-proxyshell-and-proxytoken)
- [Apache Tomcat HTTP Request Smuggling](#apache-tomcat-http-request-smuggling)
- [QNAP NAS Command Injection](#qnap-nas-command-injection)
- [VMware vCenter Multiple Vulnerabilities](#vmware-vcenter-multiple-vulnerabilities)
- [Pulse Connect Secure Authentication Bypass](#pulse-connect-secure-authentication-bypass)
- [F5 BIG-IP iControl REST RCE](#f5-big-ip-icontrol-rest-rce)
- [Microsoft Exchange Server: ProxyLogon](#microsoft-exchange-server-proxylogon)
- [Oracle WebLogic Server RCE](#oracle-weblogic-server-rce)
- [Summary and Recommendations](#summary-and-recommendations)

---

## Introduction
One of the primary issues discussed by cybersecurity practitioners is the ever-evolving threat landscape. The fast-changing security environment, along with a growing attack surface, has challenged organizations to adapt and keep up with their security programs. When reports of critical vulnerabilities and exploits are published, attackers will begin scanning publicly accessible hosts in their quest for vulnerable assets within minutes. This report reviews Internet-facing targets exposed to some high-profile vulnerabilities released in 2021.

Key observations from this report are that despite the high severity for some of these vulnerabilities, more than 50% of the servers had a weak security posture even weeks and months after a security update was released. This was because the servers were not patched in a timely manner or had an unsupported version of the software running. The use of deprecated protocols and remote access tools on servers accessible over the Internet is common too.

## Vulnerability Trends
A record-breaking number (~18,352) of new security vulnerabilities was reported in the year 2020, a 6% increase from 2019 and a staggering 184.66% increase from 2016. 

![Chart showing the number of vulnerabilities published in NVD from 2011-2021]

Comparing 2021 with 2020, a total of ~13,000 vulnerabilities have been reported as of September 1, 2021. 

![Chart showing the number of vulnerabilities in NVD per month in 2020-2021]

As shown in Figure 3, out of the ~13,000 vulnerabilities released until September of this year, approximately 20% were classified as “High” severity.

![Severity breakdown of vulnerabilities on NVD in 2021]

## High-Profile Vulnerabilities of 2021
Organizations’ rapid migration to the cloud has expanded the attack surface drastically. We gathered telemetry on Shodan to review vulnerable instances of publicly accessible targets on the Internet for some of 2021’s high-profile vulnerabilities.

![Table summarizing CVEs and vulnerable instances on Shodan for various high-profile vulnerabilities]

## Microsoft Exchange Server: ProxyShell and ProxyToken
The ProxyShell (CVE-2021-34473, CVE-2021-34523, and CVE-2021-31207) vulnerabilities allow an unauthenticated attacker to execute arbitrary code on Exchange Servers on port 443. As of August 31, 2021, facet analysis on Shodan reports ~45K instances verified were vulnerable to ProxyShell.

![Facet Analysis on Shodan – CVE breakdown for Microsoft Exchange ProxyShell]
![Heatmap of Exchange Servers vulnerable to ProxyShell]

Out of the 45,000 vulnerable instances, about 4.3% have RDP enabled, and 1% have SMBv1 enabled.

![Exchange Servers vulnerable to ProxyShell with SMBv1 and RDP enabled]

Additionally, the "ProxyToken" (CVE-2021-33766) vulnerability allows an unauthenticated attacker to access and steal emails. It was patched in July 2021.

![Heatmap of Exchange Servers vulnerable to ProxyToken]

## Apache Tomcat HTTP Request Smuggling
On July 12, 2021, Apache released a patch for an HTTP request smuggling vulnerability (CVE-2021-33037). 

![Breakdown of Tomcat version series on Shodan]
![Breakdown of Tomcat instances on Shodan as of July 22, 2021]

## QNAP NAS Command Injection
On June 24, 2021, QNAP released a security advisory for a command injection vulnerability (CVE-2021-28800). 

![QNAP hosts vulnerable to CVE-2021-28800 4-7 weeks after patch release]

## VMware vCenter Multiple Vulnerabilities
On May 25, 2021, VMware released patches for VMSA-2021-0010. The percentage of vulnerable hosts declined from 80.88% in May 2021 to 48.95% in August 2021.

![Breakdown of VMware vCenter versions vulnerable to CVE-2021-21985, CVE-2021-21986]

## Pulse Connect Secure Authentication Bypass
On April 20, 2021, reports surfaced regarding a zero-day vulnerability (CVE-2021-22893) in Pulse Connect Secure. It had a critical CVSS v3 score of 10.0.

![Heatmap of Pulse Connect Secure hosts affected by CVE-2021-22893, CVE-2021-22894, CVE-2021-22899, CVE-2021-22900]

## F5 BIG-IP iControl REST RCE
On March 10, 2021, F5 announced an unauthenticated remote command execution vulnerability (CVE-2021-22986). 

![Successful exploitation of F5 BIG-IP CVE-2021-22986]

## Microsoft Exchange Server: ProxyLogon
Code-named ProxyLogon, these flaws (CVE-2021-26855, CVE-2021-26858, CVE-2021-26857, CVE-2021-27065) affected on-premises versions of Exchange Server.

![Exchange Servers vulnerable to ProxyLogon with SMBv1 and RDP enabled]
![Heatmap of Exchange Servers vulnerable to ProxyLogon]

## Oracle WebLogic Server RCE
CVE-2021-2109 is an authenticated remote code execution vulnerability. Our team created a proof-of-concept (PoC) to determine hosts vulnerable to both this and the directory traversal vulnerability CVE-2020-14882.

![POST Request to check if the host is vulnerable to Oracle Weblogic vulnerabilities]
![Breakdown of WebLogic Server instances vulnerable to CVE-2021-2109 & CVE-2020-14882]

## Summary and Recommendations
Attackers are leveraging telemetry from Shodan to gather information about vulnerable instances, sometimes faster than ethical hackers. We urge organizations to:
1. Run regular scans and prioritize patching for systems that are easily accessible.
2. Maintain an up-to-date inventory of assets.
3. Continuously monitor, track, and update assets with the latest security updates.
4. Disable deprecated protocols like SMBv1 and unnecessary remote access tools like RDP on Internet-facing systems.

---
*Trustwave is a leading cybersecurity and managed security services provider. For more information, visit [www.trustwave.com](http://www.trustwave.com).*