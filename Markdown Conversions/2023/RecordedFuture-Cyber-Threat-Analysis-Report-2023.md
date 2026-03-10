# Cyber-Threat-Analysis-Report

## Table of Contents
- [Section I Setting the Stage: Technology, Geopolitics, Economics, and Policy](#section-i--setting-the-stage-technology-geopolitics-economics-and-policy)
- [Section II Cyber Threat Intelligence](#section-ii--cyber-threat-intelligence)
- [Section III Reflections on 2022 Predictions](#section-iii--reflections-on-2022-predictions)
- [Section IV Outlook](#section-iv--outlook)
- [Appendix A Top Exploited Vulnerabilities in 2023](#appendix-a--top-exploited-vulnerabilities-in-2023)

---

**Organization:** RecordedFuture  
**Report Title:** Cyber-Threat-Analysis-Report  
**Year:** 2023  
**Date:** March 21, 2024  

## FOREWORD

When creating this annual report, we had two goals: to give you insight into the adversary’s playbook and to assess future scenarios so that your organization can reasonably prepare for them.

In 2023, attack surfaces expanded, software supply-chain vulnerabilities were widely exploited, and the expanded use of generative AI increased the velocity of malicious content at scale.

The report presents the industry’s most comprehensive analysis of intelligence from 2023. It covers threat actors and their playbook of targets, methods, and attacks to help you eliminate blind spots in your current security posture. You’ll discover how:

- Threat actors exploited enterprise software at scale, as observed in CL0P ransomware group’s attack on third-party managed file transfer (MFT) services such as Fortra’s GoAnywhere and Progress Software’s MOVEit.
- Offensive tooling is increasingly targeting Linux and macOS systems: Ransomware kits continue to expand beyond Windows environments, facilitating an expanded range of victims.
- Nation-states such as China-linked Spamouflage Dragon (tracked by Insikt Group as Empire Dragon) are already using AI-generated images to improve information operations (IO).

## Executive Summary

2023 was a year of unrealized expectations. A rumored global recession failed to materialize. The Ukrainian counteroffensive did not decisively shift the tide of its war against an invading Russia. Any movement toward Israel-Saudi rapprochement was significantly set back following the October 7 Hamas terrorist attack in Israel and the launch of a new war in Gaza. Despite the initial hype around ChatGPT, disruptive applications of generative AI are likely still years off.

Nonetheless, Insikt Group continued to track cyber threat actors capitalizing on this chaos and uncertainty to steal data, conduct espionage, and disrupt their geopolitical rivals.

### 2023: The Year of the Enterprise Software Hack

While “zero trust” may be a buzzword in enterprise security, the reality is that the internet relies on trust now more than ever. The work-from-home era accelerated the adoption of “as-a-service” enterprise software, shared cloud infrastructure, and virtualized workspaces.

Cybercriminals are taking advantage of this increasingly interconnected environment to amplify their attacks. The number of weaponized vulnerabilities in enterprise software increased fourfold from the previous year. The ransomware gang behind MOVEit, CL0P, is estimated to have earned between $75 to $100 million in profit on that hack alone.

## Key Findings

- **Expanding attack surfaces increased the opportunity for mass exploitation of vulnerabilities.**
- **Early malicious use of generative AI focused on social engineering and influence operations.**
- **Software supply-chain attacks remain prevalent.**
- **Criminals targeted business process organizations to facilitate social engineering.**
- **Trusted tools are being abused through legitimate internet services.**
- **Regulation abuse failed to take hold.**
- **Offensive tooling is increasingly targeting Linux and macOS systems.**
- **The war in Gaza increased hacktivist activity, capitalizing on chaos.**
- **Valid accounts are increasingly being used for initial access, while phishing tactics evolve.**
- **There is a convergence of influence narratives between ideological groups.**

---

## Section I: Setting the Stage: Technology, Geopolitics, Economics, and Policy

### Major Technology Trends
Discussions around generative AI dominated 2023. Beyond AI, increased demand for cloud computing drove vendors to seek higher computing power. Another trend was the increased offering of passwordless authentication, such as "magic link" logins, to balance security and convenience.

### Geopolitical Events: Global Conflicts Reshape Strategic Partnerships
Russia’s invasion of Ukraine continued, with the Kremlin turning to Iran, China, and North Korea for support. The Israel-Hamas war, beginning October 7, 2023, further complicated global geopolitics, with Russia using the conflict to reframe violence as a result of failed US foreign policy.

### Macroeconomic Trends
A wave of mass layoffs hit the technology sector in 2023, with 260,000 jobs lost. This downsizing exposed the sector to potential loss of talent and created opportunities for scam campaigns preying on job seekers.

### Cyber Policy’s Uphill Battle
2023 saw major law enforcement takedowns against cybercriminal operations. Additionally, the SEC finalized regulations for covered entities to report incidents of "materiality" within four business days.

---

## Section II: Cyber Threat Intelligence

### Evolution of Exploited Vulnerabilities
![Metrics associated with key themes in the 2023 cyber threat landscape]

The most notable instances of mass exploitation were carried out by the CL0P ransomware group on two third-party MFT services: Fortra’s GoAnywhere and Progress Software’s MOVEit.

### Evolution of Cyber Threats
#### Early Malicious Use of Generative AI
While sensationalized fears of AI autonomously developing complex cyberattacks remain speculative, threat actors are using AI-powered chatbots to craft convincing phishing emails and support scam operations.

#### Third-Party Threats
Software supply-chain attacks saw an 11.8% increase. 2023 also saw the first instance of a "double-software supply-chain compromise," targeting 3CX Desktop App software via a trojanized installer of the X_TRADER platform.

#### Offensive Tooling Increasingly Targets Linux and macOS
Reporting shows that cyberattacks and malware targeting Linux and macOS systems increased from 2022 to 2023. Ransomware families like Cactus, CL0P, and Akira added Linux/ESXi variants to their toolkits.

---

## Section III: Reflections on 2022 Predictions

![Reflections on three major predictions from our 2022 Annual Report]

---

## Section IV: Outlook

### Cyber Threat Landscape
- **Vulnerabilities**: We predict at least one ransomware group will carry out a successful compromise of hundreds of targets via an enterprise third-party file transfer service in 2024.
- **Third-party threats**: We expect software supply-chain attacks to dominate, with at least a 15% growth in reported incidents.
- **Initial access**: Attackers will likely focus on stealing credentials using password spraying and credential stuffing.

### Contextual Landscape
- **Technology**: The shift toward passwordless logins will force threat actors to innovate, potentially driving a shift away from account takeover (ATO) tactics toward new account fraud (NAF).
- **Geopolitics**: Russia will likely exploit "war fatigue" among Western nations to influence public opinion ahead of elections in the US and EU.

---

## Appendix A: Top Exploited Vulnerabilities in 2023

[^1]: Footnote content here. (Note: The original document structure implies technical appendices; refer to the full Recorded Future intelligence index for specific CVE lists.)

---

tions: The increase in vulnerability exploits will drive lawmakers to shift from regulating
software safety to reforming software liability law. This would make it easier for consumers to
take legal action against software companies that produce insecure code; however, determining
what counts as coding negligence will be a significant challenge for policymakers. In response to
ongoing policies and regulations for AI, AI companies will likely shift toward synthetic data for
training their models to avoid privacy and copyright issues, speed up development, and reduce
the chances of data poisoning from threat actors.

25

TA 2024 0321

Recorded Future® | www.recordedfuture.com

THREAT ANALYSIS

Appendix A  Top Exploited Vulnerabilities in 2023

Vulnerability

Affected Product Description

CVE-2023-44487

Any product that
uses the HTTP/2
protocol

The HTTP/2 protocol allows a
denial-of-service (server resource
consumption) because request
cancellation can reset many streams
quickly. Fixes are vendor-specific.

Risk
Score

89

CVSS

7.5

CVE-2023-34362

Progress Software
MOVEit Transfer

A SQL injection vulnerability has been
found in the MOVEit Transfer web
application that could allow an
unauthenticated attacker to gain access
to MOVEit Transfer's database.

89

9.8

CVE-2023-23397

Microsoft Outlook

Elevation of privilege vulnerability

CVE-2023-4966

CVE-2023-21716

CVE-2023-24932

CVE-2023-28206

Citrix NetScaler ADC
and NetScaler
Gateway

A sensitive information disclosure
vulnerability that allows an attacker to
read large amounts of memory after the
end of a buffer

Microsoft Office
 Word)

Microsoft Word remote code execution
vulnerability

Microsoft Windows
10, 11, Server

Secure Boot security feature bypass
vulnerability

Apple macOS, iPhone
OS, iPadOS

An out-of-bounds write issue was
addressed with improved input
validation. An app may be able to
execute arbitrary code with kernel
privileges.

CVE-2023-2868

Barracuda Email
Security Gateway
Firmware

A remote command injection
vulnerability that can enable remote
code execution

CVE-2023-38831

RARLAB WinRAR

CVE-2023-41990

Apple macOS, iPhone
OS, iPadOS

RARLAB WinRAR before 6.23 allows
attackers to execute arbitrary code
when a user attempts to view a benign
file within a ZIP archive.

Apple-only ADJUST TrueType font
vulnerability that allows remote code
execution through a malicious iMessage
attachment. Exploited in Operation
Triangulation.

89

89

99

99

99

99

99

9.8

9.8

9.8

6.7

8.6

9.8

7.8

99

7.8

CVE-2023-43177

CrushFTP

CrushFTP prior to 10.5.1 is vulnerable to
Improperly Controlled Modification of

99

9.8

26

TA 2024 0321

Recorded Future® | www.recordedfuture.com

THREAT ANALYSIS

Vulnerability

Affected Product Description

Dynamically-Determined Object
Attributes.

CVE-2023-47565

QNAP QVR Firmware
4.0

An OS command injection vulnerability
that can allow authenticated users to
execute commands via a network

CVE-2023-4863

Google Chrome,
Mozilla Firefox

Heap buffer overflow in libwebp in
Google Chrome prior to 116.0.5845.187
and libwebp 1.3.2 allowed a remote
attacker to perform an out-of-bounds
memory write via a crafted HTML page.

Risk
Score

CVSS

99

99

8.8

8.8

CVE-2023-4911
(Looney Tunables)

GNU glibc on x64
Fedora
Red Hat Enterprise
Linux

CVE-2023-7024

Google Chrome

Buffer overflow vulnerability that can
allow RCE with elevated privileges

99

7.8

Heap buffer overflow in WebRTC in
Google Chrome prior to 120.0.6099.129
allowed a remote attacker to potentially
exploit heap corruption via a crafted
HTML page.

99

8.8

Table1:Tophigh-riskvulnerabilitiesdisclosedin2023 Source:RecordedFuture)

27

TA 2024 0321

Recorded Future® | www.recordedfuture.com

THREAT ANALYSIS

AboutInsiktGroup®

Recorded Future’s Insikt Group, the company’s threat research division, comprises
analysts and security researcherswithdeepgovernment,lawenforcement,military,and
intelligence agencyexperience.Theirmissionistoproduceintelligencethatreducesrisk
forclients,enablestangibleoutcomes,andpreventsbusinessdisruption.

AboutRecordedFuture®

Recorded Future is the world’s largest threat intelligence company. Recorded Future’s
Intelligence Cloud provides end-to-end intelligence across adversaries, infrastructure,
and targets. Indexing the internet across the open web, dark web, and technical
sources, Recorded Future provides real-time visibility into an expanding attacksurface
and threat landscape, empowering clients to act with speed and confidencetoreduce
risk and securely drive business forward. Headquartered in Boston with offices and
employees around the world, Recorded Future works with over 1,700 businesses and
government organizations acrossmorethan75countriestoprovidereal-time,unbiased,
andactionableintelligence.

Learnmoreatrecordedfuture.com

28

TA 2024 0321

Recorded Future® | www.recordedfuture.com