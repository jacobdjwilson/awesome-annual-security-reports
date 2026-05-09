# Cyber-Annual-Threat-Report 2024

## Table of Contents
- [Chapter 1: Executive Summary](#chapter-1-executive-summary)
- [Chapter 2: The 2023 Cyberthreat Landscape](#chapter-2-the-2023-cyberthreat-landscape)
- [Chapter 3: Citrix Bleed Vulnerability Case Study](#chapter-3-citrix-bleed-vulnerability-case-study)
- [Chapter 4: Cloud Security Trends and Insights](#chapter-4-cloud-security-trends-and-insights)
- [Chapter 5: Threat Actor Profiles](#chapter-5-threat-actor-profiles)
- [Chapter 6: Industry-Specific Threat Analysis](#chapter-6-industry-specific-threat-analysis)
- [Chapter 7: Predictions and Preparations for 2024](#chapter-7-predictions-and-preparations-for-2024)
- [Chapter 8: Cybersecurity Best Practices](#chapter-8-cybersecurity-best-practices)
- [Chapter 9: Conclusion](#chapter-9-conclusion)
- [Chapter 10: Glossary](#chapter-10-glossary)
- [Chapter 11: Contributors](#chapter-11-contributors)

---

## Chapter 1: Executive Summary

2023 marked a year of intensified cyberthreats, with small- and medium-sized businesses (SMBs) finding themselves increasingly in the crosshairs of sophisticated cybercriminal operations. Blackpoint witnessed evolving ransomware and phishing attempts, advantageous Initial Access Brokers (IABs), an influx of Business Email Compromise (BEC) attempts, and the ongoing exploitation of legitimate applications.

### Ransomware Attacks
Ransomware attacks continued prominently with the existence of double extortion schemes, even triple at times. Cybercriminals not only encrypt victim data but also threaten public release or deletion of sensitive information unless they receive the ransom.

### Supply Chain Attacks
Supply chain attacks emerged as a critical vector, exploiting the interconnected nature of business operations. Attackers capitalized on the potential to breach one entity and infiltrate several others, exploiting the trust and relationships between businesses, their vendors, and Managed Service Providers (MSPs).

### Initial Access Brokers
In 2023, IABs, who specialize in breaching systems and selling unauthorized access to the highest bidder, significantly increased their activities.

### Business Email Compromise
Amidst these evolving threats, the ongoing threat of BEC persisted, often targeting SMBs with perceived lower defenses.

### Phishing Attacks
Cybercriminals fine-tuned their social engineering (SE) tactics to craft highly convincing and personalized emails, websites, and messages. These phishing campaigns have become tools for installing malware, initiating lateral movement, and setting the stage for more devastating attacks.

### The Exploitation of Public-Facing Applications
Threat actors increasingly exploited public-facing applications, capitalizing on common vulnerabilities and misconfigurations. Web servers, content management systems, and remote management interfaces, such as Remote Monitoring and Management (RMM) and Remote Desktop Protocol (RDP), were frequently targeted.

> **What is Defense in Depth?**
> A cybersecurity strategy that involves the implementation of multiple layers of security, each layer protecting against different types of security threats.

---

## Chapter 2: The 2023 Cyberthreat Landscape

*   **83 minutes**: The average time between initial access and lateral movement for threat actors.
*   **15 minutes**: The average time Blackpoint SOC takes to respond to initial access attempts.
*   **95%**: Of endpoint device incidents were initial access attempts.

### Understanding Initial Access
Initial access covers the various methods a threat actor may use to gain unauthorized entry into a computer network or system. 

### The Growing Trend of RMM Tool Exploitation
Throughout 2023, threat actors continued to use legitimate enterprise tools to gain initial access and propagate through organizations. In each case, the RMM being used was available through trial versions that lack human verification.

### The Role of Live-off-the-Land (LotL)
In 2023, we observed over 1,000 instances of threat actors using the LotL strategy against our partners, with software such as PowerShell, Wscript, and Mshta amongst the most common native binaries.

### The Ongoing Threat of Ransomware
We observed an approximate 64% increase in ransomware attacks employing double extortion tactics from 2022 to 2023. Almost 50% of ransomware attacks in 2023 were carried out by LockBit.

![Top 10 Ransomware Threat Actors in 2023 chart showing LockBit, BlackCat, CL0P, BianLian, Conti, Play, PYSA, Black Basta, 8Base, and Hive]

---

## Chapter 3: Citrix Bleed Vulnerability Case Study

In October 2023, the SOC was made aware of the critical ‘Citrix Bleed’ vulnerability (CVE-2023-4966). Blackpoint’s MDR+R alerted to multiple successful share mounts in one of our MSP’s end client environments.

### Incident Investigation Findings:
1.  **Initial Access**: Exploitation of the ‘Citrix Bleed’ vulnerability to gain access to the NetScaler Gateway.
2.  **Persistence Setup**: Scheduled tasks were designed to set up Go Simple Tunnel to establish SOCKS5 proxies.
3.  **Lateral Movement**: Use of Impacket to move laterally to a Domain Controller (DC).
4.  **Data Access**: Remote executions using PowerShell to expose SQL databases.

---

## Chapter 4: Cloud Security Trends and Insights

Cloud-related incidents rose drastically in the last year. What accounted for 56.91% of Blackpoint’s incidents in December 2022 took up 88.46% in September 2023.

*   **VPN Usage**: Present in over 99% of cloud incidents.
*   **BEC Attempts**: Rose by an average of 210%, reaching a total of 42,688 incidents.

---

## Chapter 5: Threat Actor Profiles

We encountered five particularly dominant cyber adversaries this year:

### BlackCat (ALPHV)
A RaaS operation written in Rust, enabling them to target Windows and Linux devices. They are known for double and triple extortion tactics.

### LockBit
Well known for its continuous evolution through versions 2.0 and 3.0. They operate as a RaaS and have been known to recruit insiders from the companies they target.

### QakBot
A versatile botnet that offers a suite of tools, often setting the stage for ransomware deployments. Despite government interference, QakBot continues to return with new, innovative tactics.

### RedLine Stealer
Operates as a Malware-as-a-Service (MaaS) and is used by a wide range of cybercriminals for extensive information gathering and data exfiltration.

### Akira
Known for its distinctive, retro-style Tor leak site. They utilize leaked source code of Conti ransomware and typically target Linux devices and VMware ESXi virtual machines.

---

## Chapter 6: Industry-Specific Threat Analysis

The technology sector is the most represented industry in our observations (42.44%).

### Top 5 Industries by Incident Volume:
1.  **Technology** (42.44%)
2.  **Business Services** (13.98%)
3.  **Healthcare** (4.64%)
4.  **Financial Services** (4.41%)
5.  **Manufacturing** (3.56%)

---

## Chapter 7: Predictions and Preparations for 2024

In 2024, we predict:
*   **The Abuse of Artificial Intelligence (AI)**: Used to enhance social engineering, create deepfakes, and automate complex attacks.
*   **An Increase in Infostealers and Malvertising**: Disguising malware as legitimate downloads in search results.
*   **An Increase in Sophisticated Tactics**: More covert operations using LoLBins and RMM tools with less reliance on traditional malware.

---

## Chapter 8: Cybersecurity Best Practices
*   Prioritizing cybersecurity training.
*   Monitoring networks with vigilance.
*   Having regular vulnerability assessments.
*   Patching vulnerabilities promptly.
*   Adhering to strict email security measures.
*   Adopting the Defense in Depth (DiD) approach.

---

## Chapter 9: Conclusion
The 2023 landscape served as a stark reminder of the escalating sophistication and interconnectedness of cyberthreats. Resilience, vigilance, and proactive threat mitigation strategies are essential to navigate modern cyber-risks.

---

## Chapter 10: Glossary
*(Content omitted in original report)*

---

## Chapter 11: Contributors
*(Content omitted in original report)*

---

lated.

An Upward Trend in Ransomware Operations:
•  To conduct more targeted and damaging ransomware attacks

•  To target a range of companies, from SMBs to Fortune 500 companies

•  To deploy low-effort attacks on high-payoff targets

•  To target high-risk sectors including education, healthcare,

financial services, and government

Cloud and Supply Chain Attacks

•  To exploit interconnected systems such MSPs with customers or

cloud infrastructure

•  To exploit the subsystems that complex systems depend on

ANNUAL THREAT REPORT 2024Chapter 7   Predictions and Preparations for 20244 6

In Summary

The cyberthreat landscape this year is predicted to be increasingly
complex and sophisticated. AI is expected to play a pivotal role,
enhancing SE attacks, creating more convincing phishing attempts,
and facilitating BEC attacks. Infostealers and malvertising are likely
to rise, exploiting SEO poisoning and masquerading malware
in search results. The use of sophisticated tactics, like LoLBins
and RMM tools, will make threat detection more challenging.
Ransomware attacks are anticipated to become more targeted and
damaging, potentially leveraging AI for vulnerability exploitation.
We foresee a significant rise in cloud and supply chain attacks, due
to their interconnected nature. This evolving threat environment
underscores the need for adaptable defenses, a layered security
approach, and a dedication to educating your user base.

ANNUAL THREAT REPORT 2024Chapter 7   Predictions and Preparations for 20244 7

A N N U A L   T H R E A T   R E P O R T   2 0 2 4

Chapter 8   Cybersecurity Best Practices

Cybersecurity
Best Practices

To properly defend against the threat actors and
cyberthreats we have covered in this report, you must
empower your team members and customers to adhere
to cybersecurity best practices. Much of the time,
cyberattacks can be stopped through simple steps, such
as using unique passwords, reviewing email links, and
patching for vulnerabilities as soon as possible. Below
you will find our suggested best practices.

4 8

Cybersecurity Best Practices

Email and Online Security
•  Raise awareness of phishing or

spear-phishing attacks, which involve
links or attachments.

•  Raise awareness of malware

incorporated into online advertisements,
known as malvertising.

•  Be cautious about what you share on

social media platforms, especially personal
information and current locations.

Data Protection

Network and System Security

•  Enable automatic updates where possible.

•  Implement a continuous and frequent

patch plan.

•  Review current configurations for

misconfigurations or unauthorized changes.

•  Prioritize patching once vulnerabilities are

disclosed.

•  Phase out older, less secure authentication

methods.

•  Monitor logins over proxy and VPN to

bypass conditional access geoblocking.

•  Avoid storing passwords in web browsers.

•  Maintain regular vulnerability assessments.

•  Enforce password complexity requirements.

•  Monitor logins from suspicious user agents.

•  Encourage regular password changes.

•  Implement Zero Trust principles.

•  Avoid reusing passwords across accounts.

•  Enforce identity and access control.

•  Utilize MFA with authenticator apps, hardware

tokens, or biometrics.

•  Always use secure Wi-Fi connections. If in

public, use a VPN or your phone’s Hotspot.

•  Use secure payment methods, such as a credit

card or reliable third-party service.

Insider Threat Management
•  Be mindful of potential insider threats.

•  Manage application control and access.

•  Adhere to the Principle of Least Privilege.

•  Adhere to data handling best practices.

Backup and Insurance

•  Ensure critical data is backed up regularly.

•  Consider obtaining cyber liability insurance

for added protection.

Security Guidance

•  Adhere to industry-specific compliance

requirements.

•  Abide by the DiD security framework.

•  Follow the guidance of at least one widely

recognized security frameworks.

ANNUAL THREAT REPORT 2024Chapter 8   Cybersecurity Best Practices4 9

Conclusion

The cyberthreat landscape of the past year has undeniably
reinforced the critical need for vigilant, proactive, and
adaptive defense strategies to combat the sophisticated and
interconnected array of threats targeting organizations, including
SMBs. Amidst this landscape, the role of an MDR serves as an
essential ally, offering the expertise, technology, and readiness
needed to protect businesses’ assets and their people.

Blackpoint prides itself on our ability to provide 24/7 monitoring,
advanced analytics, and threat intelligence to ensure an ever-
watchful eye over the businesses you work for and protect. We
reduce the window of opportunity for attackers by detecting and
responding to threats swiftly and effectively, all on your behalf.
This is particularly crucial in an era where the cost and scale of
cyberattacks continue to escalate, and where the time to detect
and respond can be the difference between a minor security
incident and a significant impact to revenue, reputation, and
employees’ livelihood.

Moreover, the expertise and resources that Blackpoint services
provide alleviates the burden on internal IT teams, allowing
businesses to focus on growth and innovation while ensuring
their security posture is robust, dynamic, and aligned with the
latest threat landscape. The path forward is one of partnership,
with MDR+R services at the helm, guiding organizations through
the complexities of the modern cybersecurity landscape.

This crucial integration into your organization’s cybersecurity
strategy is more than a protective measure, it is a strategic
decision that empowers you to navigate the digital realm
with confidence and resilience.

N E XT   S T E P S

It’s time for advanced
security, informed by
security experts. Keep the
conversation going with
the researchers behind
the report. Register for
the webinar here.

Or see how Blackpoint’s
comprehensive
ecosystem can arm your
business and customers
for success.

G E T   STA RT E D

ANNUAL THREAT REPORT 2024Chapter 9   Conclusion5 0

Glossary

AES: Advanced Encryption Standard

MFA: Multifactor authentication

AI: Artificial intelligence

APG: Adversary Pursuit Group

API: Application Programming Interface

AV: Antivirus

BEC: Business Email Compromise

CISA: Cybersecurity and Infrastructure
Security Agency

MS-ISAC: Multi-State Information Sharing
and Analysis Center

MSP: Managed Service Provider

NSA: National Security Agency

OS: Operating system

OSINT: Open-source intelligence

RaaS: Ransomware-as-a-Service

CSA: Cybersecurity Advisory

RCE: Remote code execution

C2: Command and control

RDP: Remote Desktop Protocol

DC: Domain Controller

RMM: Remote Monitoring and Management

DiD: Defense in Depth

SaaS: Software-as-a-Service

DLL: Dynamic Link Library

SE: Social engineering

EDR: Endpoint Detection and Response

SEO: Search engine optimization

IAB: Initial Access Broker

SOAP: Simple Object Access Protocol

IoC: Indicator of compromise

SSO: Single sign-on

LotL: live-off-the-land

SMBs: Small- and medium-sized businesses

LoLBins: Living off the Land Binaries

SOC: Security Operations Center

MaaS: Malware-as-a-Service

TTPs: Tactics, techniques, and procedures

MDR: Managed Detection and Response

VPN: Virtual private network

MDR+R: Managed Detection, Response
and Remediation

WMI: Windows management
instrumentation

ANNUAL THREAT REPORT 2024Chapter 10   Glossary5 1

Contributors

David Rushmer, Director of Threat Research

C O N N E C T   W I T H   D AV I D   O N   L I N K E D I N .

Derick Peterson, Threat Analyst

C O N N E C T   W I T H   D E R I C K   O N   L I N K E D I N .

Robert Russell, Senior Director
of Threat Operations

C O N N E C T   W I T H   R O B E R T   O N   L I N K E D I N .

Alyssa Reed, Senior Content Writer

C O N N E C T   W I T H   A LY S S A   O N   L I N K E D I N .

ANNUAL THREAT REPORT 2024Chapter 11   Contributors